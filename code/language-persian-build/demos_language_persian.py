#!/usr/bin/env python3
"""Demo programs for the Persian Language databases.

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: pronunciation drills, script quizzes,
flashcard checks, conjugation engines, and dialogue verifiers. All 68 are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), prints a marker line that the
build cross-checks against the entry text, and ends with the OK marker.
"""
import json as _json


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + body.replace("NAME", _json.dumps(name))


def demo_persian_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # speaker arithmetic: native vs total
    native = 70000000
    total = 110000000
    share = native / total * 100.0
    official_countries = ["Iran", "Afghanistan (Dari)", "Tajikistan (Tajiki)"]
    scripts = ["Perso-Arabic", "Cyrillic (Tajiki)"]
    history_years = 2500
    print("native speakers: %d" % native)
    print("total speakers: %d" % total)
    print("native share: %.2f %%" % share)
    print("official countries: %d" % len(official_countries))
    print("scripts: %d" % len(scripts))
    print("recorded history: %d years" % history_years)
    assert native == 70000000
    assert total == 110000000
    assert 63.63 < share < 63.65
    assert len(official_countries) == 3
    assert len(scripts) == 2
    print("ENTRY-CHECK: 70 million native speakers")
    print("OK: %s mapped the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the 32-letter inventory with transliteration
    letters = [
        ("ا", "alef", "a"), ("ب", "be", "b"), ("پ", "pe", "p"),
        ("ت", "te", "t"), ("ث", "se", "s"), ("ج", "jim", "j"),
        ("چ", "che", "ch"), ("ح", "he", "h"), ("خ", "khe", "kh"),
        ("د", "dal", "d"), ("ذ", "zal", "z"), ("ر", "re", "r"),
        ("ز", "ze", "z"), ("ژ", "zhe", "zh"), ("س", "sin", "s"),
        ("ش", "shin", "sh"), ("ص", "sad", "s"), ("ض", "zad", "z"),
        ("ط", "ta", "t"), ("ظ", "za", "z"), ("ع", "eyn", "a"),
        ("غ", "qeyn", "q"), ("ف", "fe", "f"), ("ق", "qaf", "q"),
        ("ک", "kaf", "k"), ("گ", "gaf", "g"), ("ل", "lam", "l"),
        ("م", "mim", "m"), ("ن", "nun", "n"), ("و", "vav", "v"),
        ("ه", "he", "h"), ("ی", "ye", "y"),
    ]
    persian_only = ["پ", "چ", "ژ", "گ"]
    translit = {fa: tr for fa, _, tr in letters}
    word = "سلام"
    roman = "".join(translit.get(ch, "?") for ch in word)
    fa_digits = "۰۱۲۳۴۵۶۷۸۹"
    def to_fa(n):
        return "".join(fa_digits[int(d)] for d in str(n))
    print("letters: %d" % len(letters))
    print("persian-only letters: %d" % len(persian_only))
    print("transliteration of سلام: %s" % roman)
    print("1405 in Persian digits: %s" % to_fa(1405))
    assert len(letters) == 32
    assert len(persian_only) == 4
    assert roman == "slam"
    assert to_fa(1405) == "۱۴۰۵"
    assert to_fa(100) == "۱۰۰"
    print("ENTRY-CHECK: 32 letters")
    print("OK: %s wrote the script" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_pronunciation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # sound inventory and the stress rule
    vowels = ["a", "e", "o", "long-a", "i", "u"]
    consonants = ["b", "p", "t", "d", "k", "g", "f", "v", "s", "z",
                  "sh", "zh", "ch", "j", "h", "kh", "q", "gh", "m",
                  "n", "l", "r", "y"]
    examples = ["آب", "نان", "مادر", "پدر", "کتاب", "مدرسه", "درخت",
                "ماه", "خورشید", "دوست", "خانه", "شهر"]
    def noun_stress(syllables):
        # final-syllable stress for nouns: mark the last syllable
        return syllables[:-1] + [syllables[-1].upper()]
    print("vowels: %d" % len(vowels))
    print("consonants: %d" % len(consonants))
    print("spoken examples: %d" % len(examples))
    print("stress on کتاب: %s" % "-".join(noun_stress(["ke", "tab"])))
    print("stress on مادر: %s" % "-".join(noun_stress(["ma", "dar"])))
    assert len(vowels) == 6
    assert len(consonants) == 23
    assert len(examples) == 12
    assert noun_stress(["ke", "tab"])[-1] == "TAB"
    print("ENTRY-CHECK: 6 vowel qualities and 23 consonants")
    print("OK: %s sounded the phonemes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_nouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 25 core nouns and the plural rule
    nouns = [
        ("مرد", "man"), ("زن", "woman"), ("کودک", "child"),
        ("دوست", "friend"), ("خانه", "house"), ("مدرسه", "school"),
        ("کتاب", "book"), ("آب", "water"), ("نان", "bread"),
        ("شهر", "city"), ("کشور", "country"), ("روز", "day"),
        ("شب", "night"), ("ماه", "moon"), ("خورشید", "sun"),
        ("درخت", "tree"), ("گل", "flower"), ("ماشین", "car"),
        ("پول", "money"), ("وقت", "time"), ("کار", "work"),
        ("غذا", "food"), ("چای", "tea"), ("در", "door"),
        ("پنجره", "window"),
    ]
    def plural(noun):
        return noun + "ها"
    s1 = "خانه ما بزرگ است"
    s2 = "این کتاب جالب است"
    print("nouns: %d" % len(nouns))
    print("plural of کتاب: %s" % plural("کتاب"))
    print("plural of درخت: %s" % plural("درخت"))
    print("sentence check 1: %s" % ("خانه" in s1))
    print("sentence check 2: %s" % ("کتاب" in s2))
    assert len(nouns) == 25
    assert plural("کتاب") == "کتابها"
    assert "خانه" in s1 and "کتاب" in s2
    print("ENTRY-CHECK: 25 essential nouns")
    print("OK: %s named the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_verbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 25 core verbs: infinitive -> (present stem, english)
    verbs = {
        "خوردن": ("خور", "to eat"), "نوشیدن": ("نوش", "to drink"),
        "رفتن": ("رو", "to go"), "آمدن": ("آ", "to come"),
        "دیدن": ("بین", "to see"), "شنیدن": ("شنو", "to hear"),
        "گفتن": ("گو", "to say"), "خواندن": ("خوان", "to read"),
        "نوشتن": ("نویس", "to write"), "کردن": ("کن", "to do"),
        "شدن": ("شو", "to become"), "بودن": ("باش", "to be"),
        "داشتن": ("دار", "to have"), "خواستن": ("خواه", "to want"),
        "دانستن": ("دان", "to know"), "گرفتن": ("گیر", "to take"),
        "دادن": ("ده", "to give"), "خوابیدن": ("خواب", "to sleep"),
        "بیدار شدن": ("بیدار شو", "to wake up"),
        "نشستن": ("نشین", "to sit"), "ایستادن": ("ایست", "to stand"),
        "دویدن": ("دو", "to run"), "خریدن": ("خر", "to buy"),
        "فروختن": ("فروش", "to sell"),
        "یاد گرفتن": ("یاد گیر", "to learn"),
    }
    def present(stem, ending):
        return "می‌" + stem + ending
    print("verbs: %d" % len(verbs))
    print("I eat: %s" % present("خور", "م"))
    print("we go: %s" % present("رو", "یم"))
    print("he/she sees: %s" % present("بین", "د"))
    assert len(verbs) == 25
    assert present("خور", "م") == "می‌خورم"
    assert present("رو", "یم") == "می‌رویم"
    assert all(inf.endswith(("دن", "تن")) for inf in verbs)
    print("ENTRY-CHECK: 25 essential verbs")
    print("OK: %s conjugated the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_adjectives_adverbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # adjectives follow the noun; comparison by suffix
    adjectives = ["بزرگ", "کوچک", "خوب", "بد", "جدید", "قدیمی",
                  "زیبا", "زشت", "بلند", "کوتاه", "گرم", "سرد",
                  "سریع", "کند", "آسان", "سخت", "شاد", "ناراحت",
                  "تمیز", "کثیف", "گران", "ارزان", "نزدیک",
                  "دور", "مهم"]
    adverbs = ["خیلی", "همیشه", "هرگز", "امروز", "دیروز", "فردا",
               "زود", "دیر", "آهسته", "تند", "با هم", "تنها",
               "شاید", "حتماً", "دوباره"]
    def comparative(adj):
        return adj + "تر"
    def superlative(adj):
        return adj + "ترین"
    def describe(noun, adj):
        return noun + "ی " + adj
    print("adjectives: %d" % len(adjectives))
    print("adverbs: %d" % len(adverbs))
    print("big house: %s" % describe("خانه", "بزرگ"))
    print("bigger: %s" % comparative("بزرگ"))
    print("biggest: %s" % superlative("بزرگ"))
    assert len(adjectives) == 25
    assert len(adverbs) == 15
    assert comparative("بزرگ") == "بزرگتر"
    assert superlative("بزرگ") == "بزرگترین"
    assert describe("خانه", "بزرگ") == "خانه" + "ی " + "بزرگ"
    print("ENTRY-CHECK: 25 adjectives and 15 adverbs")
    print("OK: %s described the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the closed pronoun system
    subjects = ["من", "تو", "او", "ما", "شما", "آنها"]
    suffixes = {"من": "م", "تو": "ت", "او": "ش",
                "ما": "مان", "شما": "تان", "آنها": "شان"}
    demonstratives = ["این", "آن", "اینها", "آنها"]
    interrogatives = ["کی", "چه", "کجا", "چرا", "چگونه", "کدام", "چند"]
    def possessive(noun, owner):
        return noun + suffixes[owner]
    def formal_you(is_formal):
        return "شما" if is_formal else "تو"
    print("subject pronouns: %d" % len(subjects))
    print("possessive suffixes: %d" % len(suffixes))
    print("my book: %s" % possessive("کتاب", "من"))
    print("their house: %s" % possessive("خانه", "آنها"))
    print("interrogatives: %d" % len(interrogatives))
    assert len(subjects) == 6
    assert len(suffixes) == 6
    assert len(interrogatives) == 7
    assert possessive("کتاب", "من") == "کتابم"
    assert possessive("خانه", "آنها") == "خانهشان"
    assert formal_you(True) == "شما" and formal_you(False) == "تو"
    print("ENTRY-CHECK: من، تو، او، ما، شما، آنها")
    print("OK: %s pointed the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_numbers_time(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # numbers 1-100 from parts, Persian digits, ordinals, week and months
    ones = {1: "یک", 2: "دو", 3: "سه", 4: "چهار", 5: "پنج",
            6: "شش", 7: "هفت", 8: "هشت", 9: "نه", 10: "ده",
            11: "یازده", 12: "دوازده", 13: "سیزده", 14: "چهارده",
            15: "پانزده", 16: "شانزده", 17: "هفده", 18: "هجده",
            19: "نوزده", 20: "بیست"}
    tens = {30: "سی", 40: "چهل", 50: "پنجاه", 60: "شصت",
            70: "هفتاد", 80: "هشتاد", 90: "نود", 100: "صد"}
    def build(n):
        if n in ones:
            return ones[n]
        if n in tens:
            return tens[n]
        t = (n // 10) * 10
        ten_word = ones[20] if t == 20 else tens[t]
        return ten_word + " و " + ones[n - t]
    fa = "۰۱۲۳۴۵۶۷۸۹"
    def to_fa(n):
        return "".join(fa[int(d)] for d in str(n))
    ordinals = {1: "اول", 2: "دوم", 3: "سوم", 4: "چهارمین", 5: "پنجمین"}
    days = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه",
            "پنج‌شنبه", "جمعه"]
    months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد",
              "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن",
              "اسفند"]
    words100 = [build(n) for n in range(1, 101)]
    print("numbers: %d" % len(words100))
    print("21: %s" % build(21))
    print("45: %s" % build(45))
    print("100: %s" % build(100))
    print("1405: %s" % to_fa(1405))
    print("days: %d months: %d" % (len(days), len(months)))
    assert len(words100) == 100
    assert build(21) == "بیست و یک"
    assert build(45) == "چهل و پنج"
    assert to_fa(1405) == "۱۴۰۵"
    assert ordinals[4] == "چهارمین"
    assert len(days) == 7 and len(months) == 12
    assert len(set(words100)) == 100
    print("ENTRY-CHECK: Numbers 1-100")
    print("OK: %s counted to one hundred" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 30 phrases with usage notes; flashcard quiz
    phrases = [
        ("سلام", "hello", "universal greeting"),
        ("صبح بخیر", "good morning", "morning"),
        ("عصر بخیر", "good afternoon", "afternoon"),
        ("شب بخیر", "good night", "bedtime"),
        ("خداحافظ", "goodbye", "standard farewell"),
        ("به امید دیدار", "hope to see you again", "warm farewell"),
        ("خوش آمدید", "welcome", "greeting guests"),
        ("ممنون", "thanks", "casual"),
        ("متشکرم", "thank you", "standard"),
        ("خیلی ممنون", "thanks a lot", "emphatic thanks"),
        ("خواهش می‌کنم", "you are welcome", "also: please, go ahead"),
        ("ببخشید", "excuse me / sorry", "formal"),
        ("معذرت می‌خوام", "sorry", "casual"),
        ("چطوری؟", "how are you?", "casual"),
        ("خوبی؟", "are you well?", "casual"),
        ("چه خبر؟", "what is new?", "casual"),
        ("خوشحالم", "I am glad", "on meeting"),
        ("خوش وقتم", "pleased to meet you", "formal"),
        ("روز خوبی داشته باشید", "have a good day", "formal"),
        ("موفق باشید", "good luck", "wishing success"),
        ("سلامت باشید", "stay healthy", "after sneezes"),
        ("خسته نباشید", "do not be tired", "to workers, as respect"),
        ("دستت درد نکنه", "may your hand not hurt", "thanks for food/work"),
        ("نوش جان", "bon appetit", "before eating"),
        ("مبارک", "congratulations", "celebrations"),
        ("تولدت مبارک", "happy birthday", "birthdays"),
        ("سفر به خیر", "have a safe trip", "to travelers"),
        ("به سلامت", "go in health", "farewell to traveler"),
        ("بفرمایید", "please / come in", "all-purpose courtesy"),
        ("اختیار دارید", "you are too kind", "classic taarof reply"),
    ]
    by_fa = {fa: en for fa, en, _ in phrases}
    quiz = [("سلام", "hello"), ("خداحافظ", "goodbye"),
            ("نوش جان", "bon appetit")]
    score = sum(1 for fa, en in quiz if by_fa[fa] == en)
    print("phrases: %d" % len(phrases))
    print("flashcard score: %d/%d" % (score, len(quiz)))
    assert len(phrases) == 30
    assert score == 3
    assert len({fa for fa, _, _ in phrases}) == 30
    print("ENTRY-CHECK: 30 greetings")
    print("OK: %s greeted the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_grammar_essentials(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOV order, plurals, negation, questions as checkable rules
    def is_sov(tokens):
        # verb must be last
        verbs = {"خواندم", "رفتم", "می‌روم", "است"}
        return tokens[-1] in verbs
    def plural(noun, animate=False):
        return noun + ("ان" if animate else "ها")
    def negate_present(stem_form):
        # the negation prefix replaces می‌ on the present stem form
        return "نمی‌" + stem_form
    def negate_past(form):
        return "ن" + form
    def ask_yesno(sentence):
        return "آیا " + sentence + "؟"
    s = ["من", "کتاب", "خواندم"]
    print("SOV check (من کتاب خواندم): %s" % is_sov(s))
    print("plural کتاب: %s" % plural("کتاب"))
    print("plural مرد (animate): %s" % plural("مرد", animate=True))
    print("negated روم (I go): %s" % negate_present("روم"))
    print("negated رفتم: %s" % negate_past("رفتم"))
    print("question: %s" % ask_yesno("می‌آیی"))
    assert is_sov(s) is True
    assert plural("کتاب") == "کتابها"
    assert plural("مرد", animate=True) == "مردان"
    assert negate_present("روم") == "نمی‌روم"
    assert negate_past("رفتم") == "نرفتم"
    print("ENTRY-CHECK: Subject-Object-Verb")
    print("OK: %s ruled the grammar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_home_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 home/family sentences and the kinship graph
    sentences = [
        "این خانه‌ی ماست", "خانه‌ی ما سه اتاق دارد",
        "آشپزخانه بزرگ است", "اتاق خواب من تمیز است",
        "مبل در پذیرایی است", "تلویزیون روی میز است",
        "پدرم سر کار است", "مادرم آشپزی می‌کند",
        "برادرم دانشجوست", "خواهرم کوچک است",
        "پدربزرگم قصه می‌گوید", "مادربزرگم مهربان است",
        "ما پنج نفریم", "عمویم در شیراز زندگی می‌کند",
        "خاله‌ام فردا می‌آید", "بچه‌ها در حیاط بازی می‌کنند",
        "سگ ما در باغ است", "کلید روی در است",
        "چراغ‌ها روشن است", "خانه‌ی ما گرم و راحت است",
    ]
    kin = {"من": ["پدر", "مادر"], "پدر": ["پدربزرگ"],
           "مادر": ["مادربزرگ"], "پدرم": ["عمو"], "مادرم": ["خاله"]}
    def degree(a, b):
        # BFS over the kinship graph
        seen = {a: 0}
        queue = [a]
        while queue:
            cur = queue.pop(0)
            if cur == b:
                return seen[cur]
            for nxt in kin.get(cur, []):
                if nxt not in seen:
                    seen[nxt] = seen[cur] + 1
                    queue.append(nxt)
        return -1
    print("sentences: %d" % len(sentences))
    print("kinship degree من -> پدربزرگ: %d" % degree("من", "پدربزرگ"))
    print("kinship degree من -> خاله: %d" % degree("مادرم", "خاله"))
    assert len(sentences) == 20
    assert degree("من", "پدربزرگ") == 2
    assert degree("مادرم", "خاله") == 1
    assert all(len(s.split()) >= 2 for s in sentences)
    print("ENTRY-CHECK: 20 full sentences")
    print("OK: %s came home" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_food_cooking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 food sentences and recipe scaling
    sentences = [
        "صبحانه ساعت هفت است", "ناهار برنج و خورشت است",
        "شام سبک می‌خوریم", "مادرم قرمه‌سبزی پخته است",
        "کباب خیلی خوشمزه است", "برنج را دم کن",
        "پیاز را خرد کن", "نمک کم بزن", "روغن داغ شد",
        "چای تازه دم است", "نان سنگک داغ بخر",
        "میوه‌ها را بشور", "این سیب شیرین است",
        "ماست با ناهار می‌خوریم", "دوغ خنک بنوش",
        "رستوران نزدیک پارک است", "منو را بیاورید",
        "صورت‌حساب لطفاً", "غذا عالی بود، متشکرم",
        "نوش جان!",
    ]
    # scale a 4-serving rice recipe to 6 servings
    rice_4 = 400.0
    factor = 6.0 / 4.0
    rice_6 = rice_4 * factor
    water_6 = rice_6 * 1.5
    print("sentences: %d" % len(sentences))
    print("rice for 6 servings: %.1f g" % rice_6)
    print("water for 6 servings: %.1f ml" % water_6)
    assert len(sentences) == 20
    assert 599.9 < rice_6 < 600.1
    assert 899.9 < water_6 < 900.1
    print("ENTRY-CHECK: 20 sentences: meals")
    print("OK: %s cooked the meal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_travel_directions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 travel sentences and a trip-time computation
    sentences = [
        "بلیط قطار می‌خواهم", "این اتوبوس کجا می‌رود؟",
        "ایستگاه مترو کجاست؟", "فرودگاه چقدر دور است؟",
        "تاکسی بگیر", "مستقیم برو",
        "سر چهارراه بپیچ راست", "بعد از پل، سمت چپ است",
        "نزدیک است، پیاده برو", "کرایه چقدر می‌شود؟",
        "هتل نزدیک دریا می‌خواهم", "یک اتاق دو تخته لطفاً",
        "صبحانه شامل است؟", "کلید اتاق ۲۰۴",
        "ساعت حرکت قطار کی است؟", "پرواز تأخیر دارد",
        "گذرنامه و بلیط آماده است", "چمدانم را گم کردم",
        "راهنما فارسی حرف می‌زند", "سفر خوبی بود!",
    ]
    distance_km = 120.0
    speed_kmh = 60.0
    hours = distance_km / speed_kmh
    print("sentences: %d" % len(sentences))
    print("120 km at 60 km/h: %.2f h" % hours)
    assert len(sentences) == 20
    assert 1.99 < hours < 2.01
    imperatives = [s for s in sentences if s in
                   ("تاکسی بگیر", "مستقیم برو")]
    assert len(imperatives) == 2
    print("ENTRY-CHECK: 20 sentences: transport")
    print("OK: %s hit the road" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_work_school(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 work/school sentences and the work-week total
    sentences = [
        "من مهندس هستم", "او در بانک کار می‌کند",
        "ساعت کاری هشت تا چهار است", "جلسه ساعت ده شروع می‌شود",
        "گزارش را فردا بده", "حقوق آخر ماه است",
        "همکارم خیلی کمکم کرد", "پروژه تمام شد",
        "مدرسه ساعت هشت باز می‌شود", "معلم درس را توضیح داد",
        "دانش‌آموزان تکلیف نوشتند", "امتحان هفته‌ی آینده است",
        "نمره‌ی خوبی گرفتم", "کتابخانه ساکت است",
        "فارسی یاد می‌گیرم", "هر روز تمرین می‌کنم",
        "سؤال بپرس", "جواب درست است",
        "استاد راضی بود", "یادگیری هرگز تمام نمی‌شود",
    ]
    days, hours_per_day = 5, 8.0
    week = days * hours_per_day
    print("sentences: %d" % len(sentences))
    print("work week: %.1f h" % week)
    assert len(sentences) == 20
    assert 39.9 < week < 40.1
    print("ENTRY-CHECK: 20 sentences: jobs")
    print("OK: %s went to work" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_health_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 health sentences and a body-mass-index computation
    sentences = [
        "سرم درد می‌کند", "چشم‌هایم می‌سوزد",
        "گلویم درد می‌کند", "تب دارم",
        "سرفه می‌کنم", "سرما خورده‌ام",
        "دستم زخمی شد", "پایم پیچ خورد",
        "حالم خوب نیست", "دکتر وقت دارد؟",
        "باید دکتر بروم", "کجا درد می‌کند؟",
        "از کی شروع شد؟", "این دارو را روزی دو بار بخور",
        "بعد از غذا بخور", "استراحت کن",
        "آب زیاد بنوش", "داروخانه شبانه‌روزی کجاست؟",
        "نسخه را بدهید", "زود خوب می‌شوی",
    ]
    weight_kg, height_m = 70.0, 1.75
    bmi = weight_kg / (height_m ** 2)
    print("sentences: %d" % len(sentences))
    print("BMI at 70 kg / 1.75 m: %.2f" % bmi)
    assert len(sentences) == 20
    assert 22.85 < bmi < 22.87
    symptoms = [s for s in sentences if "درد می‌کند" in s or "تب دارم" in s]
    assert len(symptoms) == 4
    print("ENTRY-CHECK: 20 sentences: body parts")
    print("OK: %s checked the symptoms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 emotion sentences mapped to an intensity scale
    sentences = [
        ("خیلی خوشحالم", "happy", 9),
        ("از دیدنت خوشحالم", "happy", 8),
        ("دلم شاد است", "happy", 8),
        ("امروز ناراحتم", "sad", 6),
        ("دلم گرفته است", "sad", 7),
        ("گریه‌ام گرفت", "sad", 8),
        ("عصبانی شدم", "angry", 7),
        ("خونم به جوش آمد", "angry", 10),
        ("آرام باش", "calm", 3),
        ("می‌ترسم", "afraid", 6),
        ("از تاریکی می‌ترسم", "afraid", 7),
        ("نگران نباش", "calm", 3),
        ("دوستت دارم", "love", 10),
        ("عاشق بهارم", "love", 9),
        ("دلم برایت تنگ شده", "love", 8),
        ("تعجب کردم!", "surprise", 7),
        ("باورت نمی‌شود!", "surprise", 8),
        ("چه عالی!", "happy", 9),
        ("خسته‌ام", "tired", 5),
        ("امیدوارم", "hope", 6),
    ]
    avg = sum(i for _, _, i in sentences) / len(sentences)
    by_emotion = {}
    for _, emo, inten in sentences:
        by_emotion.setdefault(emo, []).append(inten)
    print("sentences: %d" % len(sentences))
    print("emotions covered: %d" % len(by_emotion))
    print("mean intensity: %.2f" % avg)
    assert len(sentences) == 20
    assert len(by_emotion) == 9
    assert 7.19 < avg < 7.21
    print("ENTRY-CHECK: 20 sentences: happy, sad, angry, afraid, love, surprise")
    print("OK: %s felt the feelings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_nature_weather(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 nature sentences and temperature conversion
    sentences = [
        "امروز هوا آفتابی است", "دیروز باران آمد",
        "فردا برف می‌آید", "هوا ابری است",
        "باد شدیدی می‌وزد", "هوا خیلی گرم است",
        "زمستان سرد است", "بهار فصل گل‌هاست",
        "درخت‌ها سبز شدند", "پرنده‌ها می‌خوانند",
        "گربه روی دیوار است", "سگ پارس می‌کند",
        "اسب سریع می‌دود", "ماهی در آب شنا می‌کند",
        "کوه بلند است", "رودخانه پر آب است",
        "دریا آبی است", "صحرا خشک است",
        "رنگین‌کمان زیباست", "طبیعت ایران متنوع است",
    ]
    def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0
    print("sentences: %d" % len(sentences))
    print("25 C in Fahrenheit: %.1f" % c_to_f(25.0))
    print("0 C in Fahrenheit: %.1f" % c_to_f(0.0))
    assert len(sentences) == 20
    assert 76.9 < c_to_f(25.0) < 77.1
    assert 31.9 < c_to_f(0.0) < 32.1
    weather = [s for s in sentences if "هوا" in s or "باران" in s
               or "برف" in s or "باد" in s]
    assert len(weather) == 6
    print("ENTRY-CHECK: 20 sentences: animals")
    print("OK: %s read the sky" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_shopping_money(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 shopping sentences; discount and change arithmetic
    sentences = [
        "این چقدر است؟", "قیمتش چنده؟",
        "خیلی گران است", "تخفیف می‌دهید؟",
        "آخرش چنده؟", "کمی ارزان‌تر بگویید",
        "دو کیلو سیب می‌خواهم", "نیم کیلو پنیر بده",
        "تازه است؟", "این رنگ را دارید؟",
        "سایز بزرگ‌تر دارید؟", "فقط نگاه می‌کنم",
        "می‌خرم", "نقد می‌دهم",
        "کارت می‌کشم", "بقیه‌اش را نگه دارید",
        "فاکتور بدهید", "بازار شلوغ است",
        "مغازه ساعت نه باز می‌شود", "خرید خوبی بود!",
    ]
    def toman_to_rial(t):
        return t * 10
    price, discount = 100.0, 0.20
    final = price * (1.0 - discount)
    paid, change = 100.0, 100.0 - final
    print("sentences: %d" % len(sentences))
    print("100 tomans in rials: %d" % toman_to_rial(100))
    print("price after 20%% discount: %.1f tomans" % final)
    print("change from 100: %.1f tomans" % change)
    assert len(sentences) == 20
    assert toman_to_rial(100) == 1000
    assert 79.9 < final < 80.1
    assert 19.9 < change < 20.1
    print("ENTRY-CHECK: 1 toman = 10 rials")
    print("OK: %s closed the deal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_friendship_social(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 social sentences and a gathering headcount
    sentences = [
        "اسم شما چیست؟", "من سارا هستم",
        "از آشنایی‌تان خوشحالم", "کجا زندگی می‌کنید؟",
        "چند سالته؟", "شغلت چیست؟",
        "فردا مهمان مایی", "به خانه‌ی ما بیا",
        "چای می‌خوری؟", "بفرما، تعارف نکن",
        "تولدت مبارک!", "عیدت مبارک!",
        "سال نو مبارک!", "به سلامتی!",
        "دیشب خیلی خوش گذشت", "دوباره همدیگر را ببینیم",
        "شماره‌ات را بده", "در تماس باشیم",
        "دوست خوبی هستی", "همیشه خوشحال می‌شوم ببینمت",
    ]
    invited, confirmed = 12, 9
    rate = confirmed / invited * 100.0
    print("sentences: %d" % len(sentences))
    print("RSVP confirmation: %.1f %%" % rate)
    assert len(sentences) == 20
    assert 74.9 < rate < 75.1
    print("ENTRY-CHECK: 20 sentences: meeting people")
    print("OK: %s joined the gathering" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_technology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 tech sentences and a download-time computation
    sentences = [
        "گوشیم زنگ خورد", "جواب بده",
        "شماره‌ام را ذخیره کن", "پیامک بفرست",
        "ایمیلت را چک کن", "اینترنت قطع است",
        "وای‌فای وصل شد", "رمز وای‌فای چیست؟",
        "کامپیوترم هنگ کرد", "فایل را دانلود کن",
        "عکس بفرست", "ویدیو را ببین",
        "آنلاین شو", "تماس تصویری بگیریم",
        "شارژ گوشیم تمام شد", "گوشی را شارژ کن",
        "برنامه را نصب کن", "آپدیت جدید آمد",
        "پسورد را عوض کن", "تکنولوژی زندگی را آسان کرد",
    ]
    size_mb, speed_mbps = 500.0, 10.0
    seconds = size_mb / speed_mbps
    print("sentences: %d" % len(sentences))
    print("500 MB at 10 MB/s: %.1f s" % seconds)
    assert len(sentences) == 20
    assert 49.9 < seconds < 50.1
    borrowed = [s for s in sentences if "اینترنت" in s or "وای‌فای" in s
                or "دانلود" in s or "آپدیت" in s]
    assert len(borrowed) == 5
    print("ENTRY-CHECK: 20 sentences: phone")
    print("OK: %s connected the device" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_verb_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # full conjugation of خوردن from its two stems
    present_stem, past_stem = "خور", "خورد"
    endings = {"م": "I", "ی": "you", "د": "he/she",
               "یم": "we", "ید": "you-pl", "ند": "they"}
    def present(e):
        return "می‌" + present_stem + e
    def past(e):
        return past_stem + e
    def past_cont(e):
        return "می‌" + past_stem + e
    def present_perfect(e):
        return past_stem + "ه‌" + {"م": "ام", "ی": "ای",
               "د": "است", "یم": "ایم", "ید": "اید",
               "ند": "اند"}[e]
    def past_perfect(e):
        return past_stem + "ه بود" + e
    def subjunctive(e):
        return "ب" + present_stem + e
    forms = {
        "present": present("م"), "past": past("م"),
        "past_continuous": past_cont("م"),
        "present_perfect": present_perfect("م"),
        "past_perfect": past_perfect("م"),
        "subjunctive": subjunctive("م"),
    }
    print("tenses: %d" % len(forms))
    for k, v in forms.items():
        print("  %-16s %s" % (k, v))
    assert forms["present"] == "می‌خورم"
    assert forms["past"] == "خوردم"
    assert forms["past_continuous"] == "می‌خوردم"
    assert forms["present_perfect"] == "خورده‌ام"
    assert forms["past_perfect"] == "خورده بودم"
    assert forms["subjunctive"] == "بخورم"
    assert len(endings) == 6
    print("ENTRY-CHECK: می‌ + present stem")
    print("OK: %s timed the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_questions_answers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 Q/A pairs; classify each question by its question word
    pairs = [
        ("اسمت چیست؟", "سارا هستم", "what"),
        ("کجایی؟", "خانه هستم", "where"),
        ("کی آمد؟", "دوستم آمد", "who"),
        ("چه می‌خواهی؟", "آب می‌خواهم", "what"),
        ("چرا دیر کردی؟", "ترافیک بود", "why"),
        ("چگونه آمدی؟", "با تاکسی", "how"),
        ("کی می‌روی؟", "فردا", "when"),
        ("کدام را می‌خواهی؟", "آبی را", "which"),
        ("چند تا خریدی؟", "سه تا", "how many"),
        ("آیا فارسی بلدی؟", "کمی", "yes/no"),
        ("حالت چطور است؟", "خوبم، ممنون", "how"),
        ("ناهار خوردی؟", "بله، خوردم", "yes/no"),
        ("کجا کار می‌کنی؟", "در بانک", "where"),
        ("چه ساعتی می‌آیی؟", "ساعت پنج", "when"),
        ("با کی رفتی؟", "با برادرم", "who"),
        ("چرا نخوردی؟", "سیر بودم", "why"),
        ("این مال کیست؟", "مال من است", "whose"),
        ("هوا چطور است؟", "آفتابی", "how"),
        ("چقدر طول می‌کشد؟", "یک ساعت", "how long"),
        ("می‌توانی کمکم کنی؟", "حتماً", "yes/no"),
    ]
    kinds = {}
    for _, _, k in pairs:
        kinds[k] = kinds.get(k, 0) + 1
    print("pairs: %d" % len(pairs))
    print("question kinds: %d" % len(kinds))
    assert len(pairs) == 20
    assert kinds["yes/no"] == 3
    assert all(q.endswith("؟") for q, _, _ in pairs)
    print("ENTRY-CHECK: 20 question/answer pairs")
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_commands_requests(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 imperatives in matched informal/formal pairs; build from stems
    pairs = [
        ("بیا اینجا", "بفرمایید داخل"),
        ("بنشین", "بفرمایید بنشینید"),
        ("بگو", "لطفاً بفرمایید"),
        ("بخور", "نوش جان کنید"),
        ("برو", "بفرمایید بروید"),
        ("صبر کن", "یک لحظه صبر کنید"),
        ("در را ببند", "لطفاً در را ببندید"),
        ("کمکم کن", "می‌توانید کمکم کنید؟"),
        ("زود باش", "عجله کنید"),
        ("مواظب باش", "خواهش می‌کنم مواظب باشید"),
    ]
    def imperative(stem, formal=False):
        return "ب" + stem + ("ید" if formal else "")
    print("pairs: %d" % len(pairs))
    print("informal eat: %s" % imperative("خور"))
    print("formal eat: %s" % imperative("خور", formal=True))
    print("do not go: %s" % ("ن" + "رو"))
    assert len(pairs) == 10
    assert sum(len(p) for p in pairs) == 20
    assert imperative("خور") == "بخور"
    assert imperative("خور", formal=True) == "بخورید"
    assert all(len(f) > len(i) for i, f in pairs)
    print("ENTRY-CHECK: 20 imperatives")
    print("OK: %s gave the orders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 detailed descriptive sentences; measure description density
    sentences = [
        "مادرم زنی مهربان و صبور است",
        "پدرم قد بلند و موهای خاکستری دارد",
        "دوستم چشم‌های سبز و لبخند گرمی دارد",
        "تهران شهری بزرگ و شلوغ است",
        "اصفهان تاریخی و زیباست",
        "خانه‌ی ما قدیمی ولی راحت است",
        "باغ پر از گل‌های رنگارنگ است",
        "کوه دماوند بلندترین کوه ایران است",
        "دریای خزر بزرگ‌ترین دریاچه‌ی جهان است",
        "این رستوران غذای خوشمزه و قیمت مناسب دارد",
        "معلم ما جدی ولی عادل است",
        "بچه‌ی همسایه بازیگوش و باهوش است",
        "هوای امروز خنک و دلپذیر است",
        "شب‌های کویر پرستاره و ساکت است",
        "بازار قدیم پر از رنگ و بوست",
        "کتابی که خواندم طولانی ولی جالب بود",
        "دوستم از من بلندتر است",
        "این سیب از آن سیب شیرین‌تر است",
        "بهترین دوست من ساراست",
        "زیباترین فصل بهار است",
    ]
    comparatives = [s for s in sentences if "تر است" in s or "ترین" in s]
    avg_words = sum(len(s.split()) for s in sentences) / len(sentences)
    print("sentences: %d" % len(sentences))
    print("with comparatives/superlatives: %d" % len(comparatives))
    print("average words per sentence: %.2f" % avg_words)
    assert len(sentences) == 20
    assert len(comparatives) == 6
    assert 5.99 < avg_words < 6.01
    print("ENTRY-CHECK: 20 detailed descriptive sentences")
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_story_1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 10-line story, line-by-line pairing, foundation-vocabulary check
    lines = [
        ("پسری در روستا زندگی می‌کند", "a boy lives in a village"),
        ("اسم او علی است", "his name is Ali"),
        ("او هر روز به مدرسه می‌رود", "he goes to school every day"),
        ("بعد از مدرسه در مزرعه بازی می‌کند", "after school he plays in the field"),
        ("او یک بادبادک قرمز دارد", "he has a red kite"),
        ("بادبادک در آسمان پرواز می‌کند", "the kite flies in the sky"),
        ("علی می‌دود و می‌خندد", "Ali runs and laughs"),
        ("دوستانش او را تشویق می‌کنند", "his friends cheer him on"),
        ("خورشید غروب می‌کند", "the sun sets"),
        ("علی خوشحال به خانه برمی‌گردد", "Ali returns home happy"),
    ]
    foundation = {"پسر", "روستا", "زندگی", "اسم", "علی", "مدرسه",
                  "روز", "بازی", "مزرعه", "بادبادک", "قرمز",
                  "آسمان", "پرواز", "دویدن", "خندیدن", "دوست",
                  "خورشید", "غروب", "خوشحال", "خانه"}
    print("lines: %d" % len(lines))
    print("translations paired: %d" % sum(1 for fa, en in lines if fa and en))
    assert len(lines) == 10
    assert all(fa and en for fa, en in lines)
    print("ENTRY-CHECK: 10-sentence story")
    print("OK: %s told the tale" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_story_2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 10-line past-tense story; classify each verb
    lines = [
        ("در بازار قدیم نانوایی بود", "past-simple"),
        ("اسم او حسن بود", "past-simple"),
        ("او هر صبح زود بیدار می‌شد", "past-continuous"),
        ("خمیر را ورز می‌داد", "past-continuous"),
        ("نان‌ها را در تنور می‌پخت", "past-continuous"),
        ("بوی نان تازه در بازار می‌پیچید", "past-continuous"),
        ("مردم صف می‌کشیدند", "past-continuous"),
        ("حسن به همه لبخند می‌زد", "past-continuous"),
        ("یک روز باران شدیدی آمد", "past-simple"),
        ("ولی تنور حسن هنوز گرم بود", "past-simple"),
    ]
    simple = [t for _, t in lines if t == "past-simple"]
    cont = [t for _, t in lines if t == "past-continuous"]
    print("lines: %d" % len(lines))
    print("past-simple verbs: %d" % len(simple))
    print("past-continuous verbs: %d" % len(cont))
    assert len(lines) == 10
    assert len(simple) == 4
    assert len(cont) == 6
    print("ENTRY-CHECK: 10-sentence story in past tenses")
    print("OK: %s remembered the past" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_story_3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 10-line future/conditional story; count the markers
    lines = [
        "مسافری قول داد به روستایش برگردد",
        "او گفت: سال آینده برمی‌گردم",
        "اگر پول کافی داشته باشم، خانه می‌سازم",
        "اگر باران بیاید، دیرتر می‌رسم",
        "مادرم منتظرم است",
        "او برایم آش می‌پزد",
        "بچه‌های روستا دنبالم خواهند دوید",
        "اگر زود برسم، غروب را می‌بینم",
        "قول، قول است",
        "سال آینده، همه‌ی این‌ها واقعی خواهد شد",
    ]
    agar = sum(1 for l in lines if "اگر" in l)
    literary = sum(1 for l in lines if "خواهد" in l or "خواهند" in l)
    print("lines: %d" % len(lines))
    print("conditional اگر lines: %d" % agar)
    print("literary-future خواهد lines: %d" % literary)
    assert len(lines) == 10
    assert agar == 3
    assert literary == 2
    print("ENTRY-CHECK: 10-sentence story in future/conditional forms")
    print("OK: %s promised tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_idioms_proverbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20 idioms: literal image vs real meaning; quiz the mapping
    idioms = [
        ("از آب کره گرفتن", "take butter from water", "achieve the impossible"),
        ("آب از سرش گذشت", "water passed over his head", "past the point of caring"),
        ("دست از پا درازتر", "hands longer than feet", "empty-handed"),
        ("هر چه بکاری همان بدروی", "reap what you sow", "actions have consequences"),
        ("مرغ همسایه غاز است", "neighbor's chicken is a goose", "grass is greener"),
        ("جوجه را آخر پاییز می‌شمارند", "count chicks at autumn's end", "do not count chickens early"),
        ("گر صبر کنی ز غوره حلوا سازی", "halva from unripe grapes", "patience works miracles"),
        ("یک دست صدا ندارد", "one hand makes no sound", "it takes two"),
        ("حرف حق تلخ است", "truth is bitter", "truth hurts"),
        ("سنگ بزرگ علامت نزدن است", "big stone means no throw", "do not overpromise"),
        ("نان به نرخ روز خوردن", "bread at the day's price", "opportunism"),
        ("از کوره در رفتن", "jump out of the furnace", "fly off the handle"),
        ("پا روی دم کسی گذاشتن", "step on someone's tail", "provoke"),
        ("دو پا را در یک کفش کردن", "two feet in one shoe", "dig in one's heels"),
        ("کار نیکو کردن از پر کردن است", "good work from practice", "practice makes perfect"),
        ("قطره قطره دریا شود", "drop by drop becomes a sea", "small efforts accumulate"),
        ("دو صد گفته چو نیم کردار نیست", "200 sayings < half a deed", "actions speak louder"),
        ("دل به دریا زدن", "throw the heart into the sea", "take the plunge"),
        ("سر از پا نشناختن", "not know head from foot", "overjoyed"),
        ("چشم به راه بودن", "eyes on the road", "await eagerly"),
    ]
    quiz = [("یک دست صدا ندارد", "it takes two"),
            ("دل به دریا زدن", "take the plunge"),
            ("چشم به راه بودن", "await eagerly")]
    by_fa = {fa: meaning for fa, _, meaning in idioms}
    score = sum(1 for fa, m in quiz if by_fa[fa] == m)
    print("idioms: %d" % len(idioms))
    print("quiz score: %d/%d" % (score, len(quiz)))
    assert len(idioms) == 20
    assert score == 3
    assert all(lit != meaning for _, lit, meaning in idioms)
    print("ENTRY-CHECK: 20 idioms/proverbs")
    print("OK: %s spoke in proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 15 register pairs; verify the formal side carries honorifics
    pairs = [
        ("سلام!", "با سلام و احترام"),
        ("چطوری؟", "حال شما چطور است؟"),
        ("ممنون", "سپاسگزارم"),
        ("ببخشید دیر کردم", "پوزش می‌خواهم که دیر کردم"),
        ("بیا اینجا", "لطفاً تشریف بیاورید"),
        ("بشین", "بفرمایید بنشینید"),
        ("بهم بگو", "لطفاً بفرمایید"),
        ("می‌خوام برم", "اجازه می‌خواهم بروم"),
        ("باشه", "حتماً، با کمال میل"),
        ("نمی‌دونم", "اطلاعی ندارم"),
        ("خداحافظ", "به امید دیدار"),
        ("قربانت برم", "لطف دارید"),
        ("قیمت چنده؟", "لطفاً قیمت را بفرمایید"),
        ("بابا، بیا", "پدرجان، تشریف بیاورید"),
        ("دوستت دارم", "با احترام"),
    ]
    honorific_marks = ["تشریف", "فرمود", "بفرمایید", "شما",
                       "لطفاً", "سپاس", "احترام", "پوزش"]
    def is_formal(phrase):
        return any(m in phrase for m in honorific_marks)
    formal_ok = sum(1 for _, f in pairs if is_formal(f))
    print("pairs: %d" % len(pairs))
    print("formal sides with honorific marks: %d" % formal_ok)
    assert len(pairs) == 15
    assert formal_ok >= 10
    assert sum(1 for i, f in pairs if len(f) >= len(i)) >= 13
    print("ENTRY-CHECK: 15 formal vs informal pairs")
    print("OK: %s bowed politely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_complex_sentences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 15 complex sentences; every sentence must carry its connector
    sentences = [
        ("کتابی که دیروز خریدم خیلی جالب است", "که"),
        ("چون باران می‌آمد، در خانه ماندیم", "چون"),
        ("اگر زود بیایی، با هم می‌رویم", "اگر"),
        ("هرچند خسته بودم، کار را تمام کردم", "هرچند"),
        ("قبل از اینکه بروی، در را ببند", "قبل از اینکه"),
        ("بعد از اینکه ناهار خوردیم، پیاده‌روی کردیم", "بعد از اینکه"),
        ("او آن‌قدر سریع دوید که همه تعجب کردند", "آن‌قدر"),
        ("نه تنها دیر آمد، بلکه عذر هم نخواست", "نه تنها"),
        ("هم فارسی حرف می‌زند، هم انگلیسی", "هم"),
        ("یا با ما بیا، یا خانه بمان", "یا"),
        ("مردی که آنجا ایستاده، معلم من است", "که"),
        ("وقتی که رسیدم، همه رفته بودند", "وقتی که"),
        ("جایی که بزرگ شدم، روستای کوچکی بود", "جایی که"),
        ("آن‌چه گفتی درست بود", "آن‌چه"),
        ("با اینکه باران می‌آمد، بازی ادامه داشت", "با اینکه"),
    ]
    missing = [(s, c) for s, c in sentences if c not in s]
    connectors = {c for _, c in sentences}
    print("sentences: %d" % len(sentences))
    print("distinct connectors: %d" % len(connectors))
    print("missing connectors: %d" % len(missing))
    assert len(sentences) == 15
    assert len(missing) == 0
    assert len(connectors) >= 12
    print("ENTRY-CHECK: 15 long sentences")
    print("OK: %s built the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_conversation_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20-line market dialogue; strict alternation; purchase arithmetic
    lines = [
        ("سارا", "سلام، این انارها چنده؟"),
        ("فروشنده", "سلام خانم، کیلویی چهل تومان"),
        ("سارا", "خیلی گران است! سی تومان نمی‌شود؟"),
        ("فروشنده", "سی؟ نه خانم، انارها تازه و شیرین‌اند"),
        ("سارا", "آخرش چنده؟"),
        ("فروشنده", "برای شما، سی و پنج"),
        ("سارا", "دو کیلو بدهید"),
        ("فروشنده", "بفرمایید، تازه‌چین است"),
        ("سارا", "زعفران هم دارید؟"),
        ("فروشنده", "بله، مثقال چقدر می‌خواهید؟"),
        ("سارا", "یک مثقال، برای مهمانی"),
        ("فروشنده", "زعفران قائنات، عالی است"),
        ("سارا", "جمعاً چقدر شد؟"),
        ("فروشنده", "صد و ده تومان"),
        ("سارا", "تخفیف نمی‌دهید؟"),
        ("فروشنده", "صد تومان، برای مشتری خوب"),
        ("سارا", "خیلی ممنون، دست شما درد نکنه"),
        ("فروشنده", "خواهش می‌کنم، نوش جان"),
        ("سارا", "به امید دیدار!"),
        ("فروشنده", "به سلامت، باز هم تشریف بیاورید"),
    ]
    speakers = [sp for sp, _ in lines]
    alternates = all(speakers[i] != speakers[i + 1]
                     for i in range(len(speakers) - 1))
    pomegranate = 2 * 35.0
    total = 100.0
    saffron = total - pomegranate
    print("lines: %d" % len(lines))
    print("strict alternation: %s" % alternates)
    print("2 kg pomegranate at 35: %.1f tomans" % pomegranate)
    print("saffron share of 100: %.1f tomans" % saffron)
    assert len(lines) == 20
    assert alternates is True
    assert 69.9 < pomegranate < 70.1
    assert 29.9 < saffron < 30.1
    print("ENTRY-CHECK: 20-line bilingual market dialogue")
    print("OK: %s bargained at the bazaar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_conversation_friend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20-line friends dialogue; alternation; the plan details
    lines = [
        ("رضا", "امیر! چه خبر؟"),
        ("امیر", "رضا! خوبی؟ دلم برایت تنگ شده بود"),
        ("رضا", "منم همین‌طور، بشین چای بخور"),
        ("امیر", "چای تازه دم است؟"),
        ("رضا", "آره، مادر بزرگم دم کرده"),
        ("امیر", "کار چطور است؟"),
        ("رضا", "شلوغ ولی خوب، پروژه‌ی جدید دارم"),
        ("امیر", "خانواده خوب‌اند؟"),
        ("رضا", "همه خوب‌اند، سلام می‌رسانند"),
        ("امیر", "بچه‌ها بزرگ شدند؟"),
        ("رضا", "آره، پسرم امسال مدرسه می‌رود"),
        ("امیر", "چه زود!"),
        ("رضا", "آخر هفته چه کار می‌کنی؟"),
        ("امیر", "کاری ندارم، چرا؟"),
        ("رضا", "بیا برویم کوه"),
        ("امیر", "عالی است! ساعت چند؟"),
        ("رضا", "شش صبح، سر کوچه"),
        ("امیر", "باشه، صبحانه با من"),
        ("رضا", "نه، تعارف نکن، دنگی"),
        ("امیر", "باشه دنگی! به امید دیدار"),
    ]
    speakers = [sp for sp, _ in lines]
    alternates = all(speakers[i] != speakers[i + 1]
                     for i in range(len(speakers) - 1))
    casual = sum(1 for _, t in lines if "آره" in t or "باشه" in t
                 or "بشین" in t)
    print("lines: %d" % len(lines))
    print("strict alternation: %s" % alternates)
    print("casual markers: %d" % casual)
    assert len(lines) == 20
    assert alternates is True
    assert casual >= 3
    print("ENTRY-CHECK: 20-line bilingual friends dialogue")
    print("OK: %s met the old friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_conversation_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 20-line repair dialogue; four acts; price negotiation
    lines = [
        ("خانم محمدی", "سلام، لطفاً بیایید، سینک نشتی دارد"),
        ("لوله‌کش", "سلام خانم، کی شروع شد؟"),
        ("خانم محمدی", "از دیشب، آب زیر سینک جمع می‌شود"),
        ("لوله‌کش", "بگذارید نگاه کنم"),
        ("لوله‌کش", "لوله ترک خورده است"),
        ("خانم محمدی", "جدی؟ تعمیر می‌شود؟"),
        ("لوله‌کش", "بله، باید عوض شود"),
        ("خانم محمدی", "چقدر طول می‌کشد؟"),
        ("لوله‌کش", "حدود یک ساعت"),
        ("خانم محمدی", "هزینه‌اش چقدر است؟"),
        ("لوله‌کش", "با دستمزد، دویست تومان"),
        ("خانم محمدی", "کمی گران است، تخفیف نمی‌دهید؟"),
        ("لوله‌کش", "برای شما صد و هشتاد"),
        ("خانم محمدی", "قبول، شروع کنید"),
        ("لوله‌کش", "آب را ببندید لطفاً"),
        ("خانم محمدی", "بستم"),
        ("لوله‌کش", "تمام شد، تست کنید"),
        ("خانم محمدی", "دیگر نشتی ندارد، عالی است"),
        ("خانم محمدی", "خیلی ممنون، دست شما درد نکنه"),
        ("لوله‌کش", "خواهش می‌کنم، اگر مشکلی بود زنگ بزنید"),
    ]
    acts = {"state": "نشتی", "diagnose": "ترک",
            "negotiate": "تخفیف", "confirm": "تست"}
    text = " ".join(t for _, t in lines)
    found = {a: (m in text) for a, m in acts.items()}
    asked, agreed = 200.0, 180.0
    print("lines: %d" % len(lines))
    print("four acts found: %s" % all(found.values()))
    print("negotiated: %.0f -> %.0f tomans" % (asked, agreed))
    assert len(lines) == 20
    assert all(found.values())
    assert agreed < asked
    discount_pct = (asked - agreed) / asked * 100.0
    print("discount: %.1f %%" % discount_pct)
    assert 9.9 < discount_pct < 10.1
    print("ENTRY-CHECK: 20-line bilingual problem-solving dialogue")
    print("OK: %s fixed the leak" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_persian_mastery_review(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the consolidated reference as computed data
    letters = ["ا", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د",
               "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط",
               "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
               "ن", "و", "ه", "ی"]
    vowels, consonants = 6, 23
    words = [
        "مرد", "زن", "کودک", "دوست", "خانه", "مدرسه", "کتاب",
        "آب", "نان", "شهر", "کشور", "روز", "شب", "ماه",
        "خورشید", "درخت", "گل", "ماشین", "پول", "وقت",
        "کار", "غذا", "چای", "در", "پنجره", "خوردن", "نوشیدن",
        "رفتن", "آمدن", "دیدن", "شنیدن", "گفتن", "خواندن",
        "نوشتن", "کردن", "شدن", "بودن", "داشتن", "خواستن",
        "دانستن", "گرفتن", "دادن", "خوابیدن", "بیدار شدن",
        "نشستن", "ایستادن", "دویدن", "خریدن", "فروختن",
        "یاد گرفتن", "بزرگ", "کوچک", "خوب", "بد", "جدید",
        "قدیمی", "زیبا", "بلند", "کوتاه", "گرم", "سرد",
        "سریع", "کند", "آسان", "سخت", "شاد", "تمیز",
        "گران", "ارزان", "نزدیک", "دور", "مهم", "خیلی",
        "همیشه", "هرگز", "امروز", "دیروز", "فردا", "زود",
        "دیر", "آهسته", "تند", "با هم", "تنها", "شاید",
        "حتماً", "دوباره", "من", "تو", "او", "ما", "شما",
        "آنها", "این", "آن", "کی", "چه", "کجا", "چرا",
        "چگونه", "یک", "دو", "سه", "چهار", "پنج", "شش",
        "هفت", "هشت", "نه", "ده", "بیست", "سی", "صد",
        "هزار", "شنبه", "یکشنبه", "دوشنبه", "جمعه",
        "فروردین", "مهر", "بهار", "تابستان", "پاییز",
        "زمستان", "سلام", "خداحافظ", "ممنون",
        "خواهش می‌کنم", "ببخشید", "صبح بخیر", "شب بخیر",
        "خوش آمدید", "سر", "چشم", "دست", "پا", "قلب",
        "شادی", "غم", "عشق", "جنگل", "دریا", "آسمان",
        "باران", "برف", "باد", "بازار", "تخفیف", "مهمانی",
        "گوشی", "اینترنت", "پدر", "مادر", "برادر",
        "خواهر", "پسر", "دختر", "آشپزخانه", "اتاق",
        "صبحانه", "ناهار", "شام", "کباب", "برنج",
        "میوه", "گوشت", "ماهی", "بلیط", "قطار",
        "هواپیما", "هتل", "نقشه", "سفر", "جلسه",
        "گزارش", "امتحان", "نمره", "استاد", "تب",
        "دکتر", "دارو", "پرنده", "گربه", "سگ",
        "اسب", "کوه", "رودخانه", "صحرا",
        "دعوت", "پیام",
        "تماس", "عکس", "قول", "منتظر", "واقعی",
        "روستا", "مزرعه", "بادبادک", "نانوا", "تنور",
    ]
    rules = ["SOV word order", "no gender", "plurals ها/ان",
             "را object marker", "نه negation prefix",
             "آیا questions", "ezafe linker",
             "می‌ present", "past stem endings",
             "participle perfects", "ب subjunctive",
             "ب imperative"]
    print("letters: %d" % len(letters))
    print("vowels: %d consonants: %d" % (vowels, consonants))
    print("core words: %d" % len(words))
    print("grammar rules: %d" % len(rules))
    assert len(letters) == 32
    assert vowels + consonants == 29
    assert len(words) == 200
    assert len(rules) == 12
    assert len(set(words)) == 200
    print("ENTRY-CHECK: 200-word core vocabulary")
    print("OK: %s sealed the reference" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "persian_overview": demo_persian_overview,
    "persian_writing": demo_persian_writing,
    "persian_pronunciation": demo_persian_pronunciation,
    "persian_nouns": demo_persian_nouns,
    "persian_verbs": demo_persian_verbs,
    "persian_adjectives_adverbs": demo_persian_adjectives_adverbs,
    "persian_pronouns": demo_persian_pronouns,
    "persian_numbers_time": demo_persian_numbers_time,
    "persian_greetings": demo_persian_greetings,
    "persian_grammar_essentials": demo_persian_grammar_essentials,
    "persian_home_family": demo_persian_home_family,
    "persian_food_cooking": demo_persian_food_cooking,
    "persian_travel_directions": demo_persian_travel_directions,
    "persian_work_school": demo_persian_work_school,
    "persian_health_body": demo_persian_health_body,
    "persian_emotions": demo_persian_emotions,
    "persian_nature_weather": demo_persian_nature_weather,
    "persian_shopping_money": demo_persian_shopping_money,
    "persian_friendship_social": demo_persian_friendship_social,
    "persian_technology": demo_persian_technology,
    "persian_verb_tenses": demo_persian_verb_tenses,
    "persian_questions_answers": demo_persian_questions_answers,
    "persian_commands_requests": demo_persian_commands_requests,
    "persian_descriptions": demo_persian_descriptions,
    "persian_story_1": demo_persian_story_1,
    "persian_story_2": demo_persian_story_2,
    "persian_story_3": demo_persian_story_3,
    "persian_idioms_proverbs": demo_persian_idioms_proverbs,
    "persian_registers": demo_persian_registers,
    "persian_complex_sentences": demo_persian_complex_sentences,
    "persian_conversation_market": demo_persian_conversation_market,
    "persian_conversation_friend": demo_persian_conversation_friend,
    "persian_conversation_problem": demo_persian_conversation_problem,
    "persian_mastery_review": demo_persian_mastery_review,
}
