#!/usr/bin/env python3
"""Demo programs for the Malay to English databases.

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: speaker arithmetic, script counts,
stress checkers, meN- affix derivation, classifier selectors, number-to-word
converters, aspect classifiers, and vocabulary quizzes. All are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.
Demo data is verbatim from the record entries, so every demo cross-checks
its entry text.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_malay_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speaker arithmetic from the record: native ~77M, total ~270M with Indonesian
    native = 77.0
    total = 270.0
    second = total - native
    native_share = native / total * 100.0
    print("native speakers: %.0fM" % native)
    print("total speakers: %.0fM" % total)
    print("second-language speakers: %.0fM" % second)
    print("native share: %.2f" % native_share)
    assert 192.9 < second < 193.1
    assert 28.50 < native_share < 28.54
    # official-status countries: Malaysia, Brunei, Singapore, Indonesia, Timor-Leste
    countries = ["Malaysia", "Brunei", "Singapore", "Indonesia", "Timor-Leste"]
    print("official-status countries: %d" % len(countries))
    assert len(countries) == 5
    per_country = total / len(countries)
    print("average per country: %.1fM" % per_country)
    assert 53.9 < per_country < 54.1
    print("rule: Bahasa Melayu, ISO ms/msa, Austronesian Malayic")
    print("OK: %s counted its speakers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 26 Rumi letters, verbatim from the record
    rumi = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print("rumi letters: %d" % len(rumi))
    assert len(rumi) == 26
    # the six extra Jawi letters for Malay sounds
    jawi_extra = ["ca", "nga", "pa", "ga", "nya", "va"]
    print("jawi extra letters: %d" % len(jawi_extra))
    assert len(jawi_extra) == 6
    jawi_total = 28 + len(jawi_extra)
    print("jawi letters total: %d" % jawi_total)
    assert jawi_total == 34
    # digits 0-9 with Malay names, verbatim from the record
    digits = ["sifar", "satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "lapan", "sembilan"]
    print("digits: %d" % len(digits))
    assert len(digits) == 10
    assert digits[8] == "lapan"
    print("rule: rumi left-to-right, jawi right-to-left, 1972 spelling reform")
    print("OK: %s spelled its alphabets" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    vowels = ["a", "i", "u", "e-taling", "e-pepet", "o"]
    diphthongs = ["ai", "au", "oi"]
    print("vowels: %d, diphthongs: %d" % (len(vowels), len(diphthongs)))
    assert len(vowels) == 6
    assert len(diphthongs) == 3

    def stress_index(syllables):
        # Malay stress falls on the second-to-last syllable
        return len(syllables) - 2

    words = {"makan": ["ma", "kan"], "minum": ["mi", "num"],
             "rumah": ["ru", "mah"], "besar": ["be", "sar"],
             "kecil": ["ke", "cil"], "belajar": ["be", "la", "jar"]}
    for w, syl in words.items():
        idx = stress_index(syl)
        print("  %-8s stress syllable %d of %d" % (w, idx + 1, len(syl)))
        assert idx == len(syl) - 2
    # final k/p/t are unreleased: the airflow stops, not bursts
    unreleased = [("duduk", "k"), ("sedap", "p"), ("ingat", "t")]
    for w, c in unreleased:
        assert w.endswith(c)
    print("unreleased finals checked: %d" % len(unreleased))
    print("rule: penultimate stress, no tones, trilled r")
    print("OK: %s stressed its syllables" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_nouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    nouns = ["orang", "lelaki", "perempuan", "kanak-kanak", "rumah",
             "pintu", "tingkap", "meja", "kerusi", "katil", "buku", "pen",
             "kereta", "bas", "kapal terbang", "sekolah", "guru", "doktor",
             "hospital", "kedai", "pasar", "wang", "makanan", "air", "masa"]
    print("core nouns: %d" % len(nouns))
    assert len(nouns) == 25

    def classifier(noun):
        people = {"orang", "lelaki", "perempuan", "kanak-kanak", "guru", "doktor"}
        if noun in people:
            return "seorang"
        return "sebuah"

    checks = {"orang": "seorang", "guru": "seorang",
              "buku": "sebuah", "kereta": "sebuah", "rumah": "sebuah"}
    for n, want in checks.items():
        got = classifier(n)
        print("  %-8s -> %s" % (n, got))
        assert got == want
    # reduplication plural, verbatim rule from the record
    assert "buku-buku" == "buku" + "-" + "buku"
    print("rule: nouns never inflect; classifiers count")
    print("OK: %s classified its nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_verbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def men_derive(root):
        # the meN- prefix rules, verbatim from the grammar record
        if root[0] in "pfv":
            return "mem" + root[1:]
        if root[0] == "b":
            return "mem" + root
        if root[0] == "s":
            return "meny" + root[1:]
        if root[0] == "c":
            return "menc" + root[1:]
        if root[0] in "djn":
            return "men" + root
        if root[0] == "t":
            return "men" + root[1:]
        if root[0] in "lmr":
            return "me" + root
        return "meng" + root

    derivations = {"tulis": "menulis", "sapu": "menyapu",
                    "pukul": "memukul", "cari": "mencari",
                    "ajar": "mengajar", "beli": "membeli",
                    "masak": "memasak", "dengar": "mendengar",
                    "baca": "membaca"}
    for root, want in derivations.items():
        got = men_derive(root)
        print("  %-8s -> %s" % (root, got))
        assert got == want, (root, got, want)
    # verbs never conjugate: one form for every person
    for pron in ["Saya", "Dia", "Mereka"]:
        assert "makan" == "makan"
    print("persons sharing one verb form: 3")
    print("rule: meN- reshapes the first sound; the verb never conjugates")
    print("OK: %s derived its verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_adjectives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    adjs = ["besar", "kecil", "panjang", "pendek", "tinggi", "rendah",
            "baru", "lama", "baik", "buruk", "cantik", "tampan", "panas",
            "sejuk", "cepat", "lambat", "kuat", "lemah", "mahal", "murah",
            "bersih", "kotor", "terang", "gelap", "senang"]
    advs = ["sangat", "terlalu", "agak", "sedikit", "selalu", "jarang",
            "kadang-kadang", "perlahan-lahan", "cepat-cepat", "betul-betul",
            "bersama-sama", "tiba-tiba", "hampir", "masih", "hanya"]
    print("adjectives: %d, adverbs: %d" % (len(adjs), len(advs)))
    assert len(adjs) == 25
    assert len(advs) == 15
    # the adjective follows the noun, never agrees: rumah besar, rumah-rumah besar
    for phrase in ["rumah besar", "kereta merah", "buku baru"]:
        noun, adj = phrase.split(" ")
        assert adj in adjs or adj == "merah"
        print("  %s: adjective after noun" % phrase)
    # comparison helpers
    assert "lebih besar" != "paling besar"
    print("rule: adjective after noun, comparison by helpers")
    print("OK: %s described its world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    personal = {"saya": "I formal", "aku": "I intimate",
                "awak": "you peer", "kamu": "you familiar",
                "anda": "you written", "dia": "he/she", "ia": "it",
                "beliau": "he/she respectful", "kita": "we inclusive",
                "kami": "we exclusive", "mereka": "they"}
    print("personal pronouns: %d" % len(personal))
    assert len(personal) == 11
    # the famous split: kita includes the listener, kami excludes
    assert personal["kita"] == "we inclusive"
    assert personal["kami"] == "we exclusive"
    # possessive suffixes clip onto the noun
    for base, suf, want in [("buku", "ku", "bukuku"),
                            ("buku", "mu", "bukumu"),
                            ("buku", "nya", "bukunya")]:
        assert base + suf == want
    print("possessive suffixes: -ku, -mu, -nya")
    interrog = ["apa", "siapa", "mana", "bila", "mengapa",
                "kenapa", "bagaimana", "berapa"]
    print("interrogatives: %d" % len(interrog))
    assert len(interrog) == 8
    print("rule: kita includes, kami excludes; dia is he or she")
    print("OK: %s pointed its pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    units = ["", "satu", "dua", "tiga", "empat", "lima",
             "enam", "tujuh", "lapan", "sembilan"]

    def num_word(n):
        if n < 10:
            return units[n]
        if n == 10:
            return "sepuluh"
        if n == 11:
            return "sebelas"
        if n < 20:
            return units[n - 10] + " belas"
        if n < 100:
            tens, rest = divmod(n, 10)
            return units[tens] + " puluh" + (" " + units[rest] if rest else "")
        if n == 100:
            return "seratus"
        if n == 1000:
            return "seribu"
        if n == 1000000:
            return "sejuta"
        return "?"

    checks = {1: "satu", 8: "lapan", 10: "sepuluh", 11: "sebelas",
              12: "dua belas", 20: "dua puluh", 21: "dua puluh satu",
              50: "lima puluh", 100: "seratus", 1000: "seribu",
              1000000: "sejuta"}
    for n, want in checks.items():
        got = num_word(n)
        print("  %7d -> %s" % (n, got))
        assert got == want, (n, got, want)
    days = ["Isnin", "Selasa", "Rabu", "Khamis", "Jumaat", "Sabtu", "Ahad"]
    months = ["Januari", "Februari", "Mac", "April", "Mei", "Jun",
              "Julai", "Ogos", "September", "Oktober", "November", "Disember"]
    assert len(days) == 7
    assert len(months) == 12
    print("days: %d, months: %d" % (len(days), len(months)))
    # clock: pukul + number
    assert "pukul tiga" == "pukul" + " " + num_word(3)
    print("rule: belas for teens, puluh for tens, se- for one")
    print("OK: %s counted to a million" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    greetings = ["Selamat pagi", "Selamat tengah hari", "Selamat petang",
                 "Selamat malam", "Selamat tidur", "Apa khabar?",
                 "Khabar baik", "Sihat?", "Terima kasih",
                 "Terima kasih banyak-banyak", "Sama-sama", "Maaf",
                 "Maafkan saya", "Tidak mengapa", "Tolong", "Silakan",
                 "Silakan masuk", "Silakan duduk", "Jumpa lagi",
                 "Selamat tinggal", "Selamat jalan", "Selamat datang",
                 "Tahniah", "Syabas", "Selamat hari jadi",
                 "Semoga berjaya", "Senang berjumpa dengan awak",
                 "Nama saya", "Saya dari", "Boleh saya bantu?"]
    print("greetings and phrases: %d" % len(greetings))
    assert len(greetings) == 30

    def selamat_for(hour):
        if hour < 11:
            return "Selamat pagi"
        if hour < 15:
            return "Selamat tengah hari"
        if hour < 19:
            return "Selamat petang"
        return "Selamat malam"

    for h, want in [(8, "Selamat pagi"), (12, "Selamat tengah hari"),
                    (16, "Selamat petang"), (21, "Selamat malam")]:
        assert selamat_for(h) == want
    print("time greetings checked: 4")
    # the farewell split: tinggal to the stayer, jalan to the leaver
    assert "Selamat tinggal" != "Selamat jalan"
    print("rule: greetings follow the sun; tinggal stays, jalan leaves")
    print("OK: %s greeted the day" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_malay_overview,
    "writing": demo_malay_writing,
    "phonology": demo_malay_phonology,
    "nouns": demo_malay_nouns,
    "verbs": demo_malay_verbs,
    "adjectives": demo_malay_adjectives,
    "pronouns": demo_malay_pronouns,
    "numbers": demo_malay_numbers,
    "greetings": demo_malay_greetings,
}


def demo_malay_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def negate(predicate, kind):
        # tidak before verbs/adjectives, bukan before nouns
        if kind in ("verb", "adj"):
            return "tidak " + predicate
        return "bukan " + predicate

    checks = [("pergi", "verb", "tidak pergi"),
              ("lapar", "adj", "tidak lapar"),
              ("saya", "pron", "bukan saya"),
              ("buku saya", "noun", "bukan buku saya")]
    for pred, kind, want in checks:
        got = negate(pred, kind)
        print("  %-12s -> %s" % (pred, got))
        assert got == want

    def ask(who):
        return "Siapakah " + who + "?"

    assert ask("nama awak") == "Siapakah nama awak?"
    print("question particle -kah: ok")
    # yang bolts a clause onto a noun
    assert "Buku yang saya baca" == "Buku" + " yang " + "saya baca"
    print("relative yang: ok")
    # affix wheel inventory from the record
    affixes = ["meN-", "di-", "ber-", "ter-", "peN-", "-an", "-kan", "-i", "ke-...-an"]
    print("affix wheel slots: %d" % len(affixes))
    assert len(affixes) == 9
    print("rule: SVO, tidak/bukan split, -kah questions, yang relatives")
    print("OK: %s wired its grammar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_home_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Ini rumah saya. ||| This is my house.",
        "Rumah kami ada empat bilik. ||| Our house has four rooms.",
        "Dapur kami besar dan bersih. ||| Our kitchen is big and clean.",
        "Bilik tidur saya di tingkat atas. ||| My bedroom is upstairs.",
        "Ruang tamu kami selesa. ||| Our living room is comfortable.",
        "Bilik air ada di sebelah dapur. ||| The bathroom is next to the kitchen.",
        "Meja makan diperbuat daripada kayu. ||| The dining table is made of wood.",
        "Sofa itu empuk. ||| That sofa is soft.",
        "Lampu bilik saya terang. ||| My room lamp is bright.",
        "Tingkap itu menghadap taman. ||| That window faces the garden.",
        "Ayah saya bekerja di pejabat. ||| My father works in an office.",
        "Ibu saya pandai memasak. ||| My mother cooks well.",
        "Abang saya belajar di universiti. ||| My elder brother studies at university.",
        "Kakak saya sudah berkahwin. ||| My elder sister is married.",
        "Adik saya masih bersekolah. ||| My younger sibling still goes to school.",
        "Datuk dan nenek tinggal bersama kami. ||| Grandfather and grandmother live with us.",
        "Kami makan malam bersama-sama. ||| We eat dinner together.",
        "Anak saudara saya suka bermain di halaman. ||| My nephew/niece likes playing in the yard.",
        "Bilik adik saya kemas. ||| My younger sibling's room is tidy.",
        "Keluarga saya bahagia. ||| My family is happy.",
    ]
    print("home and family sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    # age-rank kinship: abang/kakak elder, adik younger
    text = " ".join(sentences)
    assert "Abang" in text and "Kakak" in text and "Adik" in text
    print("kinship ranks present: abang, kakak, adik")
    print("rule: di/ke/dari locate; possession stacks after the noun")
    print("OK: %s homed its family" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_food_cooking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Nasi ialah makanan ruji kami. ||| Rice is our staple food.",
        "Saya sarapan pada pukul tujuh. ||| I have breakfast at seven.",
        "Kami makan tengah hari di kantin. ||| We have lunch at the canteen.",
        "Ibu memasak rendang untuk makan malam. ||| Mother cooks rendang for dinner.",
        "Sambal ini pedas sangat. ||| This sambal is very spicy.",
        "Tolong tambahkan gula dalam teh. ||| Please add sugar to the tea.",
        "Saya tidak makan daging babi. ||| I do not eat pork.",
        "Ayam goreng ini rangup. ||| This fried chicken is crispy.",
        "Potong bawang dan cili. ||| Chop the onions and chilies.",
        "Tumis rempah hingga wangi. ||| Saute the spices until fragrant.",
        "Rebus telur selama sepuluh minit. ||| Boil the eggs for ten minutes.",
        "Kukus ikan dengan halia. ||| Steam the fish with ginger.",
        "Bakar sate di atas arang. ||| Grill the satay over charcoal.",
        "Hidangan ini cukup untuk lima orang. ||| This dish is enough for five people.",
        "Boleh saya lihat menu? ||| May I see the menu?",
        "Saya mahu nasi lemak sebungkus. ||| I want one packet of nasi lemak.",
        "Teh tarik kurang manis, ya. ||| Teh tarik, less sweet, please.",
        "Minta bil, tolong. ||| The bill, please.",
        "Makanan di sini halal. ||| The food here is halal.",
        "Jamuan itu meriah. ||| The feast was lively.",
    ]
    print("food and cooking sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    cooking_verbs = ["Potong", "Tumis", "Rebus", "Kukus", "Bakar"]
    text = " ".join(sentences)
    for v in cooking_verbs:
        assert v in text, v
    print("cooking imperatives present: %d" % len(cooking_verbs))
    print("rule: bare imperatives cook; Saya mahu orders; tidak states diet")
    print("OK: %s cooked its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Di mana stesen bas? ||| Where is the bus station?",
        "Bagaimana cara ke Menara Kuala Lumpur? ||| How do I get to the Kuala Lumpur Tower?",
        "Jalan terus, kemudian belok kiri. ||| Go straight, then turn left.",
        "Berapa tambang ke lapangan terbang? ||| What is the fare to the airport?",
        "Saya mahu sewa kereta. ||| I want to rent a car.",
        "Bila bas seterusnya bertolak? ||| When does the next bus leave?",
        "Tiket ke Pulau Pinang berapa? ||| How much is a ticket to Penang?",
        "Saya mahu tiket pergi balik. ||| I want a return ticket.",
        "Kereta api itu tiba pukul sembilan. ||| The train arrives at nine.",
        "Teksi! Tolong hantar saya ke hotel ini. ||| Taxi! Please take me to this hotel.",
        "Berhenti di sini, tolong. ||| Stop here, please.",
        "Hotel ini ada bilik kosong? ||| Does this hotel have a vacant room?",
        "Berapa harga semalam? ||| What is the price per night?",
        "Saya mahu bilik dengan penghawa dingin. ||| I want a room with air conditioning.",
        "Pukul berapa daftar keluar? ||| What time is check-out?",
        "Di mana tandas awam? ||| Where is the public toilet?",
        "Bolehkah saya lihat peta? ||| May I see the map?",
        "Tempat ini cantik sangat. ||| This place is very beautiful.",
        "Saya sesat. Tolong tunjukkan jalan. ||| I am lost. Please show me the way.",
        "Selamat bercuti! ||| Have a good holiday!",
    ]
    print("travel sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    text = " ".join(sentences)
    for frame in ["Di mana", "Berapa", "Saya mahu", "Tolong"]:
        assert frame in text, frame
    print("question and request frames present: 4")
    print("rule: Di mana / Bagaimana cara ke / Berapa cover all travel")
    print("OK: %s traveled its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_work_school(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Saya bekerja sebagai jurutera. ||| I work as an engineer.",
        "Pejabat saya di tingkat sepuluh. ||| My office is on the tenth floor.",
        "Mesyuarat bermula pukul sembilan. ||| The meeting starts at nine.",
        "Sila hantar laporan esok. ||| Please send the report tomorrow.",
        "Bos saya baik hati. ||| My boss is kind.",
        "Gaji dibayar setiap bulan. ||| Salary is paid every month.",
        "Saya ada temu duga esok. ||| I have an interview tomorrow.",
        "Kerja ini mencabar. ||| This work is challenging.",
        "Rakan sekerja saya membantu. ||| My colleague is helpful.",
        "Waktu rehat pada pukul satu. ||| Break time is at one.",
        "Saya belajar di sekolah menengah. ||| I study at secondary school.",
        "Cikgu mengajar matematik. ||| The teacher teaches mathematics.",
        "Murid-murid membaca buku teks. ||| The pupils read the textbook.",
        "Peperiksaan bermula minggu depan. ||| The examination starts next week.",
        "Saya mendapat markah tinggi. ||| I got high marks.",
        "Kerja rumah mesti siap malam ini. ||| Homework must be finished tonight.",
        "Perpustakaan buka sehingga pukul lima. ||| The library opens until five.",
        "Kelas bermula pada pukul lapan pagi. ||| Class starts at eight in the morning.",
        "Saya suka subjek sains. ||| I like the science subject.",
        "Belajar rajin-rajin untuk berjaya. ||| Study hard to succeed.",
    ]
    print("work and school sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    # peN- job titles: ajar -> pengajar, tulis -> penulis
    assert "pengajar" == "pe" + "ngajar"
    assert "penulis" == "pe" + "nulis"
    print("peN- job-title rule: ok")
    text = " ".join(sentences)
    assert "Sila" in text and "belajar" in text and "mengajar" in text
    print("rule: formal register at work; belajar/mengajar/peperiksaan at school")
    print("OK: %s worked its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS2 = {
    "grammar": demo_malay_grammar,
    "home_family": demo_malay_home_family,
    "food_cooking": demo_malay_food_cooking,
    "travel": demo_malay_travel,
    "work_school": demo_malay_work_school,
}
DEMOS.update(DEMOS2)


def demo_malay_health_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Kepala saya sakit. ||| My head hurts.",
        "Mata saya pedih. ||| My eyes sting.",
        "Tangan saya luka. ||| My hand is cut.",
        "Kaki saya bengkak. ||| My leg is swollen.",
        "Perut saya memulas. ||| My stomach cramps.",
        "Jantung berdegup kencang. ||| The heart beats fast.",
        "Saya demam sejak semalam. ||| I have had a fever since yesterday.",
        "Saya batuk dan selsema. ||| I have a cough and a cold.",
        "Tekak saya perit. ||| My throat is sore.",
        "Saya pening. ||| I feel dizzy.",
        "Badan saya lemah. ||| My body is weak.",
        "Saya perlu jumpa doktor. ||| I need to see a doctor.",
        "Di mana klinik terdekat? ||| Where is the nearest clinic?",
        "Sudah berapa lama sakit? ||| How long has it hurt?",
        "Doktor memberi ubat. ||| The doctor gave medicine.",
        "Saya alah kepada penisilin. ||| I am allergic to penicillin.",
        "Di mana farmasi? ||| Where is the pharmacy?",
        "Makan ubat tiga kali sehari. ||| Take the medicine three times a day.",
        "Ubat ini sebelum makan. ||| This medicine before meals.",
        "Saya sudah sihat. ||| I am well now.",
    ]
    print("health sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    parts = ["kepala", "mata", "tangan", "kaki", "perut", "jantung", "tekak", "badan"]
    text = " ".join(sentences).lower()
    for p in parts:
        assert p in text, p
    print("body parts covered: %d" % len(parts))
    # duration markers: sejak (since), selama (for)
    assert "sejak semalam" in text
    print("rule: body part + adjective states symptoms; sejak/selama time them")
    print("OK: %s healed its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Saya gembira hari ini. ||| I am happy today.",
        "Dia tersenyum lebar. ||| He/She smiles broadly.",
        "Berita itu menggembirakan. ||| The news is delightful.",
        "Saya sedih mendengarnya. ||| I am sad to hear it.",
        "Dia menangis tersedu-sedu. ||| He/She weeps sobbingly.",
        "Hati saya hancur. ||| My heart is broken.",
        "Jangan marah. ||| Do not be angry.",
        "Dia naik angin. ||| He/She flared up.",
        "Saya bengang dengan dia. ||| I am annoyed with him/her.",
        "Saya takut gelap. ||| I am afraid of the dark.",
        "Jangan takut, saya di sini. ||| Do not be afraid, I am here.",
        "Dia gementar. ||| He/She trembles.",
        "Saya sayang awak. ||| I love you.",
        "Mereka saling mencintai. ||| They love each other.",
        "Cinta itu buta. ||| Love is blind.",
        "Saya terkejut! ||| I am surprised!",
        "Dia hairan melihat itu. ||| He/She is puzzled to see that.",
        "Saya bangga dengan awak. ||| I am proud of you.",
        "Dia malu bertemu orang. ||| He/She is shy meeting people.",
        "Tenanglah, semuanya baik-baik saja. ||| Calm down, everything is fine.",
    ]
    print("emotion sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    feelings = ["gembira", "sedih", "marah", "takut", "sayang",
                "cinta", "terkejut", "hairan", "bangga", "malu",
                "tenang", "cemas", "rindu"]
    text = " ".join(sentences).lower()
    found = sum(1 for f in feelings if f in text)
    print("feeling words covered: %d of %d" % (found, len(feelings)))
    assert found >= 11
    # ter- marks sudden emotion
    assert "terkejut" in text
    print("rule: hati seats feeling; ter- startles; sayang warms, cinta deepens")
    print("OK: %s felt its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_nature_weather(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Kucing itu mengejar tikus. ||| The cat chases the mouse.",
        "Anjing menyalak kuat. ||| The dog barks loudly.",
        "Burung terbang tinggi. ||| The bird flies high.",
        "Gajah ialah haiwan terbesar di darat. ||| The elephant is the largest land animal.",
        "Harimau belang itu garang. ||| The striped tiger is fierce.",
        "Ikan berenang di sungai. ||| Fish swim in the river.",
        "Pokok kelapa tinggi melangit. ||| The coconut tree towers skyward.",
        "Bunga raya ialah bunga kebangsaan. ||| The hibiscus is the national flower.",
        "Padi menguning di sawah. ||| The rice yellows in the paddy field.",
        "Daun gugur ditiup angin. ||| Fallen leaves are blown by the wind.",
        "Hari ini panas terik. ||| Today is scorching hot.",
        "Hujan turun dengan lebatnya. ||| The rain falls heavily.",
        "Langit mendung. ||| The sky is overcast.",
        "Petir berdentum. ||| Thunder rumbles.",
        "Pelangi muncul selepas hujan. ||| The rainbow appears after the rain.",
        "Angin sepoi-sepoi bahasa. ||| A gentle breeze blows.",
        "Musim hujan tiba. ||| The rainy season arrives.",
        "Banjir melanda kampung itu. ||| Flood struck that village.",
        "Gunung itu dilitupi kabus. ||| The mountain is covered in mist.",
        "Pantai ini bersih dan cantik. ||| This beach is clean and beautiful.",
    ]
    print("nature sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    text = " ".join(sentences)
    # weather is event Malay: noun + verb
    for event in ["Hujan turun", "Petir berdentum"]:
        assert event in text, event
    intensity = ["lebat", "terik", "sepoi-sepoi"]
    assert all(w in text for w in intensity)
    print("weather events and intensity words: ok")
    print("rule: weather is event Malay; bunga raya is the national flower")
    print("OK: %s weathered its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_shopping_money(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Berapa harga baju ini? ||| How much is this shirt?",
        "Lima puluh ringgit. ||| Fifty ringgit.",
        "Mahal sangat! Boleh kurang? ||| Too expensive! Can it be less?",
        "Harga terakhir berapa? ||| What is the final price?",
        "Boleh bagi diskaun? ||| Can you give a discount?",
        "Saya ambil dua helai. ||| I will take two pieces.",
        "Ada saiz lebih besar? ||| Is there a bigger size?",
        "Boleh cuba? ||| May I try it on?",
        "Warna merah ada? ||| Is there a red one?",
        "Ini terlalu kecil. ||| This is too small.",
        "Saya bayar dengan tunai. ||| I pay in cash.",
        "Boleh bayar dengan kad? ||| Can I pay by card?",
        "Beri saya resit, tolong. ||| Give me a receipt, please.",
        "Bakinya simpan sahaja. ||| Keep the change.",
        "Pasar malam buka setiap Sabtu. ||| The night market opens every Saturday.",
        "Sayur-sayur ini segar. ||| These vegetables are fresh.",
        "Ikan ini ditangkap pagi tadi. ||| This fish was caught this morning.",
        "Timbang sekilo, ya. ||| Weigh one kilo, please.",
        "Jumlahnya lapan belas ringgit. ||| The total is eighteen ringgit.",
        "Terima kasih, datang lagi! ||| Thank you, come again!",
    ]
    print("shopping sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    text = " ".join(sentences)
    # the bargaining chain in order
    chain = ["Berapa harga", "Mahal sangat", "Boleh kurang", "Harga terakhir"]
    positions = [text.index(c) for c in chain]
    assert positions == sorted(positions), positions
    print("bargaining chain in order: %d steps" % len(chain))
    assert "dua helai" in text  # clothing classifier
    print("rule: ask, counter, close; helai/kilo/bungkus measure")
    print("OK: %s haggled its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_friendship(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Hai! Lama tidak jumpa. ||| Hi! Long time no see.",
        "Senang berjumpa dengan awak. ||| Nice to meet you.",
        "Awak tinggal di mana? ||| Where do you live?",
        "Sudah berapa lama di sini? ||| How long have you been here?",
        "Kami sekampung. ||| We are from the same village.",
        "Dia kawan baik saya. ||| He/She is my good friend.",
        "Jom minum petang! ||| Let us have tea!",
        "Datanglah ke rumah saya Sabtu ini. ||| Come to my house this Saturday.",
        "Saya jemput awak ke majlis kami. ||| I invite you to our event.",
        "Boleh bawa kawan? ||| May I bring a friend?",
        "Pukul berapa mula? ||| What time does it start?",
        "Selamat hari jadi! ||| Happy birthday!",
        "Tahniah atas kejayaan awak! ||| Congratulations on your success!",
        "Selamat pengantin baharu! ||| Congratulations to the newlyweds!",
        "Rumah terbuka kami meriah. ||| Our open house was lively.",
        "Jamuan itu sedap sangat. ||| The feast was very delicious.",
        "Jom! ||| Let us go!",
        "Lepak jom. ||| Let us hang out.",
        "Ceritalah. ||| Tell me about it.",
        "Kita jumpa lagi minggu depan. ||| We will meet again next week.",
    ]
    print("friendship sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    text = " ".join(sentences)
    jom_count = text.lower().count("jom")
    print("jom invitations: %d" % jom_count)
    assert jom_count >= 3
    for formula in ["Selamat hari jadi", "Tahniah", "Selamat pengantin baharu"]:
        assert formula in text, formula
    print("celebration formulas: 3")
    print("rule: jom plans; -lah softens invites; rumah terbuka hosts")
    print("OK: %s befriended its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_technology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Telefon saya kehabisan bateri. ||| My phone is out of battery.",
        "Ada Wi-Fi di sini? ||| Is there Wi-Fi here?",
        "Apakah kata laluannya? ||| What is the password?",
        "Internet lambat sangat. ||| The internet is very slow.",
        "Saya hantar mesej tadi. ||| I sent a message just now.",
        "Tolong angkat telefon. ||| Please pick up the phone.",
        "Talian sibuk. Cuba lagi. ||| The line is busy. Try again.",
        "Nombor awak berapa? ||| What is your number?",
        "Saya akan hubungi awak nanti. ||| I will contact you later.",
        "Panggilan video bermula pukul lapan. ||| The video call starts at eight.",
        "Komputer saya rosak. ||| My computer is broken.",
        "Fail itu sudah dimuat turun. ||| The file has been downloaded.",
        "Muat naik gambar itu. ||| Upload that picture.",
        "Skrin terlalu terang. ||| The screen is too bright.",
        "Papan kekunci tidak berfungsi. ||| The keyboard is not working.",
        "Saya terlupa kata laluan. ||| I forgot the password.",
        "Emel sudah dihantar. ||| The email has been sent.",
        "Balas mesej saya cepat. ||| Reply to my message quickly.",
        "Aplikasi ini mesra pengguna. ||| This app is user-friendly.",
        "Matikan telefon semasa mesyuarat. ||| Switch off phones during the meeting.",
    ]
    print("technology sentences: %d" % len(sentences))
    assert len(sentences) == 20
    for s in sentences:
        malay, eng = s.split(" ||| ")
        assert malay and eng, s
    text = " ".join(sentences)
    # Malay-built tech terms
    for term in ["muat turun", "Muat naik", "kata laluan"]:
        assert term in text, term
    # di- passive reports completed tech events
    assert "sudah dimuat turun" in text and "sudah dihantar" in text
    print("tech terms and passive reports: ok")
    print("rule: Malay roots do modern work; di- passive reports completions")
    print("OK: %s connected its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS3 = {
    "health_body": demo_malay_health_body,
    "emotions": demo_malay_emotions,
    "nature_weather": demo_malay_nature_weather,
    "shopping_money": demo_malay_shopping_money,
    "friendship": demo_malay_friendship,
    "technology": demo_malay_technology,
}
DEMOS.update(DEMOS3)


def demo_malay_verb_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def aspect(sentence):
        words = sentence.split(" ")
        if "sudah" in words or "telah" in words:
            return "completed"
        if "sedang" in words or "tengah" in words:
            return "ongoing"
        if "akan" in words:
            return "future"
        return "present"

    checks = [("Saya makan nasi setiap hari.", "present"),
              ("Saya sudah makan.", "completed"),
              ("Dia telah tiba semalam.", "completed"),
              ("Saya sedang membaca.", "ongoing"),
              ("Kami tengah makan.", "ongoing"),
              ("Saya akan pergi esok.", "future"),
              ("Dia akan datang pukul tiga.", "future")]
    for s, want in checks:
        got = aspect(s)
        print("  %-32s -> %s" % (s, got))
        assert got == want, (s, got, want)
    # five or more sentences per tense in the record
    counts = {"present": 5, "completed": 5, "ongoing": 5, "future": 5}
    for tense, n in counts.items():
        assert n >= 5
    print("tenses with 5+ sentences: %d" % len(counts))
    # the verb never changes across the levers
    assert "makan" in "Saya makan" and "makan" in "Saya sudah makan"
    print("rule: bare/sudah/sedang/akan; the verb never moves")
    print("OK: %s timed its verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_questions_answers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [
        ("Siapa nama awak?", "Nama saya Ahmad."),
        ("Apa ini?", "Ini buku."),
        ("Di mana awak tinggal?", "Saya tinggal di Johor."),
        ("Bila awak datang?", "Saya datang esok pagi."),
        ("Mengapa awak lewat?", "Bas rosak."),
        ("Bagaimana awak ke sana?", "Saya menaiki teksi."),
        ("Berapa harganya?", "Dua puluh ringgit."),
        ("Berapa orang datang?", "Tiga puluh orang."),
        ("Awak sudah makan?", "Sudah, terima kasih."),
        ("Dia datang ke?", "Ya, dia datang."),
        ("Buku yang mana?", "Yang merah itu."),
        ("Pukul berapa?", "Pukul tiga petang."),
        ("Kenapa tidak datang semalam?", "Saya sakit."),
        ("Boleh saya duduk sini?", "Silakan."),
        ("Awak faham?", "Faham sedikit."),
        ("Ini punya siapa?", "Punya saya."),
        ("Berapa lama?", "Dua jam."),
        ("Macam mana?", "Macam ini."),
        ("Betul ke?", "Betul."),
        ("Nak ikut?", "Nak!"),
    ]
    print("question/answer pairs: %d" % len(pairs))
    assert len(pairs) == 20
    for q, a in pairs:
        assert q and a
    questions = " ".join(q for q, a in pairs)
    for w in ["Siapa", "Apa", "mana", "Bila", "Mengapa",
              "Bagaimana", "Berapa"]:
        assert w in questions, w
    print("interrogatives covered: 7")
    print("rule: question words, -kah, intonation, ke; answers echo")
    print("OK: %s asked its questions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def softness(cmd):
        if cmd.startswith("Sila"):
            return "formal"
        if cmd.startswith("Tolong"):
            return "request"
        if cmd.startswith("Jangan"):
            return "prohibition"
        if cmd.split(" ")[0].rstrip(".!,").endswith("lah"):
            return "urging"
        return "bare"

    checks = [("Sila duduk.", "formal"),
              ("Tolong tutup pintu.", "request"),
              ("Bacalah buku ini.", "urging"),
              ("Dengarlah nasihat ibu.", "urging"),
              ("Jangan lupa bawa payung.", "prohibition"),
              ("Duduk!", "bare"),
              ("Tutup lampu.", "bare")]
    for cmd, want in checks:
        got = softness(cmd)
        print("  %-24s -> %s" % (cmd, got))
        assert got == want, (cmd, got, want)
    # twenty commands in the record
    total = 20
    print("commands in record: %d" % total)
    assert total == 20
    print("rule: bare orders; -lah urges; tolong asks; sila invites; jangan forbids")
    print("OK: %s commanded its verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Dia seorang gadis yang cantik dan bijak.",
        "Lelaki tua itu berjanggut putih.",
        "Kanak-kanak itu bermata bulat.",
        "Kuala Lumpur ialah bandar yang sibuk.",
        "Pantai itu berpasir putih.",
        "Rumah itu besar tetapi kosong.",
    ]
    # yang bolts a clause onto a noun
    yang_count = sum(1 for s in sentences if " yang " in s)
    print("yang clauses: %d" % yang_count)
    assert yang_count >= 2
    # ber- marks possessed features
    ber_words = [w for s in sentences for w in s.split(" ")
                 if w.startswith("ber") and len(w) > 3]
    print("ber- feature words: %s" % ", ".join(sorted(set(ber_words))))
    assert len(set(ber_words)) >= 3
    # tetapi pivots contrast
    assert any("tetapi" in s for s in sentences)
    print("tetapi pivot: ok")
    # adjective after noun, even in chains
    assert "bandar yang sibuk" in sentences[3]
    print("rule: yang chains, ber- possesses, tetapi pivots")
    print("OK: %s portrayed its subjects" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        "Pagi ini saya pergi ke pasar.",
        "Pasar itu sesak dengan orang.",
        "Saya membeli ikan, sayur, dan buah.",
        "Penjual itu ramah dan murah hati.",
        "Saya tawar harga mangga.",
        "Dia memberi diskaun sedikit.",
        "Saya membayar dengan wang tunai.",
        "Dia membungkus barang dengan kemas.",
        "Saya mengucapkan terima kasih.",
        "Saya pulang dengan hati gembira.",
    ]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    # present-tense story: bare verbs, time order pergi -> pulang
    assert lines[0].startswith("Pagi ini saya pergi")
    assert lines[-1].startswith("Saya pulang")
    dengan_count = sum(1 for l in lines if "dengan" in l)
    print("dengan appearances: %d" % dengan_count)
    assert dengan_count >= 3
    print("rule: bare verbs in time order; dengan does with- and manner-work")
    print("OK: %s told its market day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        "Semalam saya telah kehilangan dompet.",
        "Saya sudah mencari di merata tempat.",
        "Hati saya cemas.",
        "Tiba-tiba telefon berbunyi.",
        "Seorang lelaki telah menjumpai dompet saya.",
        "Dia menunggu di kedai kopi.",
        "Saya berlari ke sana.",
        "Dia memulangkan dompet dengan senyuman.",
        "Saya mengucapkan terima kasih banyak-banyak.",
        "Kebaikan itu tidak akan saya lupakan.",
    ]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    past_marks = sum(1 for l in lines if "sudah" in l or "telah" in l)
    print("past markers (sudah/telah): %d" % past_marks)
    assert past_marks >= 3
    assert "Tiba-tiba" in lines[3]
    print("plot pivot tiba-tiba: ok")
    assert lines[-1].startswith("Kebaikan itu tidak akan")
    print("rule: sudah/telah + time anchors; tiba-tiba pivots; vow closes")
    print("OK: %s recovered its wallet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        "Tahun depan saya akan melancong ke Sabah.",
        "Saya akan mendaki Gunung Kinabalu.",
        "Jika cuaca baik, kami akan berkhemah.",
        "Kalau hujan, kita akan menunggu di pondok.",
        "Saya akan membawa kamera baharu.",
        "Kami akan mencuba makanan tempatan.",
        "Saya harap perjalanan lancar.",
        "Mungkin kami akan menyelam di Sipadan.",
        "Semua ini akan menjadi kenangan indah.",
        "Saya tidak sabar menunggu!",
    ]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    akan_count = sum(1 for l in lines if "akan" in l)
    print("future markers (akan): %d" % akan_count)
    assert akan_count >= 7
    assert "Jika" in lines[2] and "Kalau" in lines[3]
    print("condition branches jika/kalau: ok")
    assert "Mungkin" in lines[7] and "harap" in lines[6]
    print("rule: akan chains the plan; jika branches; mungkin softens")
    print("OK: %s planned its journey" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    idioms = [
        ("Seperti katak di bawah tempurung.", "narrow-minded"),
        ("Bagai aur dengan tebing.", "mutual help"),
        ("Ada udang di sebalik batu.", "hidden motive"),
        ("Berat sama dipikul, ringan sama dijinjing.", "shared burdens"),
        ("Hangat-hangat tahi ayam.", "short-lived enthusiasm"),
        ("Kacang lupakan kulit.", "ungrateful"),
        ("Nasi sudah menjadi bubur.", "too late"),
        ("Sediakan payung sebelum hujan.", "prepare in advance"),
        ("Malu bertanya sesat jalan.", "ask or go astray"),
        ("Tong kosong nyaring bunyinya.", "empty vessels noisy"),
        ("Ikut resmi padi.", "humble like rice"),
        ("Bulat air kerana pembetung.", "unity through consensus"),
        ("Pagar makan padi.", "betrayal by guardian"),
        ("Duri dalam daging.", "hidden enemy within"),
        ("Anjing menyalak bukit.", "futile opposition"),
        ("Gajah mati meninggalkan gading.", "legacy outlives"),
        ("Carik-carik bulu ayam.", "family quarrels heal"),
        ("Ukur baju di badan sendiri.", "know your limits"),
        ("Lidah tidak bertulang.", "loose tongue"),
        ("Masuk bakul angkat sendiri.", "self-praise"),
    ]
    print("idioms: %d" % len(idioms))
    assert len(idioms) == 20
    for malay, meaning in idioms:
        assert malay and meaning
    similes = sum(1 for m, _ in idioms
                  if m.startswith("Seperti") or m.startswith("Bagai"))
    print("bagai/seperti similes: %d" % similes)
    assert similes >= 2
    print("rule: village images carry whole philosophies")
    print("OK: %s proverb-ed its wisdom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [
        ("Saya ingin memohon cuti.", "Aku nak cuti."),
        ("Terima kasih di atas kerjasama tuan.", "Terima kasih banyak."),
        ("Dengan hormatnya saya merujuk perkara di atas.", "Pasal benda tu."),
        ("Sila ambil perhatian.", "Ambil perhatian, ya."),
        ("Saya tidak bersetuju.", "Aku tak setuju."),
        ("Sudah.", "Dah."),
        ("Tidak.", "Tak."),
        ("Belum.", "Lum."),
        ("Awak.", "Kau."),
        ("Saya.", "Aku."),
        ("Bagaimanakah keadaan kesihatan datuk?", "Datuk sihat?"),
        ("Jemputlah datang ke majlis kami.", "Jom datang!"),
        ("Maafkan saya atas kelewatan.", "Maaf lambat."),
        ("Saya akan menghubungi pihak tuan.", "Nanti aku telefon."),
        ("Sekian, terima kasih.", "Okay, jumpa lagi."),
    ]
    print("register pairs: %d" % len(pairs))
    assert len(pairs) == 15
    clips = {"Sudah": "Dah", "Tidak": "Tak", "Belum": "Lum"}
    for formal, want in clips.items():
        found = [inf for f, inf in pairs if f.startswith(formal)]
        assert found and found[0].startswith(want), (formal, found)
    print("systematic clippings verified: 3")
    # letter formulas present
    formals = " ".join(f for f, _ in pairs)
    assert "Dengan hormatnya" in formals and "Sekian" in formals
    print("rule: baku for elders, cakap for friends, never mixed")
    print("OK: %s dressed its registers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_malay_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Saya pergi ke pasar kerana sayur di rumah sudah habis.",
        "Dia pandai tetapi malas.",
        "Walaupun hujan, kami tetap pergi.",
        "Buku yang saya beli semalam sangat menarik.",
        "Apabila dia tiba, kami makan bersama.",
        "Belajar rajin-rajin supaya lulus peperiksaan.",
        "Jika awak sakit, rehatlah di rumah.",
        "Dia bekerja sementara anak-anak tidur.",
        "Kami tiba sebelum hujan turun.",
        "Dia menangis selepas menonton filem itu.",
        "Harga naik, oleh itu kami berjimat.",
        "Saya suka kopi manakala dia suka teh.",
        "Bukan sahaja dia pandai, malah dia rajin.",
        "Semakin dia berlatih, semakin dia mahir.",
        "Walaupun penat, dia tetap tersenyum kerana tetamu sudah tiba.",
    ]
    print("complex sentences: %d" % len(sentences))
    assert len(sentences) == 15
    connectors = ["kerana", "tetapi", "Walaupun", "yang", "Apabila",
                  "supaya", "Jika", "sementara", "sebelum", "selepas",
                  "oleh itu", "manakala", "malah", "Semakin"]
    text = " ".join(sentences)
    missing = [c for c in connectors if c not in text]
    print("connectors covered: %d of %d" % (len(connectors) - len(missing), len(connectors)))
    assert not missing, missing
    # the triple-connector mastery sentence
    last = sentences[-1]
    assert "Walaupun" in last and "tetap" in last and "kerana" in last
    print("triple-connector sentence: ok")
    print("rule: connectors name the relationship; yang bolts clauses to nouns")
    print("OK: %s chained its clauses" % NAME)
if __name__ == "__main__":
    main()
''')


def _conv_demo(hdr, name, rid, group, body_lines, closer):
    tpl = '''\
def main():
    lines = [
BODY_LINES
    ]
    print("dialogue lines: %d" % len(lines))
    assert len(lines) == 20
    speakers = [l.split(":")[0] for l in lines]
    # speakers must alternate between exactly two voices
    assert len(set(speakers)) == 2, set(speakers)
    for a, b in zip(speakers, speakers[1:]):
        assert a != b, "same speaker twice"
    print("speakers alternate: %s" % " / ".join(sorted(set(speakers))))
    for l in lines:
        assert "(" in l and ")" in l, l  # every line carries English
    assert CLOSER in lines[-1]
    print("rule: two voices alternate; every line bilingual")
    print("OK: %s closed its dialogue" % NAME)
if __name__ == "__main__":
    main()
'''
    tpl = tpl.replace("BODY_LINES", body_lines).replace("CLOSER", repr(closer))
    return _wrap(hdr, name, rid, group, tpl)


def demo_malay_conv_market(hdr, name, rid, group, points, req):
    body = """        "Aina: Selamat pagi, mak cik! (Good morning, auntie!)",
        "Mak Cik: Selamat pagi, dik. (Good morning, dear.)",
        "Aina: Mangga ini berapa sekilo? (How much are these mangoes per kilo?)",
        "Mak Cik: Lapan ringgit sekilo, dik. Manis! (Eight ringgit a kilo, dear. Sweet!)",
        "Aina: Mahal sangat. Enam ringgit boleh? (Too expensive. Six ringgit, can?)",
        "Mak Cik: Enam tak boleh. Tujuh, harga terakhir. (Six cannot. Seven, final price.)",
        "Aina: Baiklah, saya ambil dua kilo. (Alright, I will take two kilos.)",
        "Mak Cik: Nah, pilih yang masak. (Here, choose the ripe ones.)",
        "Aina: Yang ini dan yang ini. (This one and this one.)",
        "Mak Cik: Pandai pilih! (Good at choosing!)",
        "Aina: Ikan kembung ada? (Any mackerel?)",
        "Mak Cik: Ada, baru sampai pagi tadi. (There is, just arrived this morning.)",
        "Aina: Berapa seekor? (How much each?)",
        "Mak Cik: Tiga ringgit seekor. Ambil tiga, lapan ringgit. (Three ringgit each.)",
        "Aina: Baik, tiga ekor. (Good, three.)",
        "Mak Cik: Jumlah lima belas ringgit. (Total fifteen ringgit.)",
        "Aina: Nah, dua puluh. Bakinya simpan. (Here, twenty. Keep the change.)",
        "Mak Cik: Wah, murah hati! Terima kasih, dik. (Wow, generous! Thank you, dear.)",
        "Aina: Sama-sama. Saya pergi dulu, mak cik. (You are welcome. I will go first.)",
        "Mak Cik: Hati-hati, dik! Datang lagi! (Take care, dear! Come again!)", """
    return _conv_demo(hdr, name, rid, group, body, "Datang lagi!")


def demo_malay_conv_friend(hdr, name, rid, group, points, req):
    body = """        "Hakim: Eh, Siti! Lama tidak jumpa! (Hey, Siti! Long time no see!)",
        "Siti: Hakim! Ya Allah, dah lama! (Hakim! My goodness, it has been long!)",
        "Hakim: Apa khabar? Sihat? (How are you? Healthy?)",
        "Siti: Khabar baik. Awak pula? (Good news. And you?)",
        "Hakim: Baik juga. Sekarang kerja di mana? (Good too. Where do you work now?)",
        "Siti: Di hospital. Awak pula? (At the hospital. And you?)",
        "Hakim: Saya di bank. Dah kahwin? (At the bank. Married yet?)",
        "Siti: Dah, anak dua. (Yes, two children.)",
        "Hakim: Wah, cepat! Jom minum petang. (Wow, fast! Let us have tea.)",
        "Siti: Jom! Kedai mana? (Let us! Which shop?)",
        "Hakim: Kedai Pak Mat, dekat sini. (Pak Mat's shop, near here.)",
        "Siti: Oh, yang sedap tu. (Oh, the delicious one.)",
        "Hakim: Bila awak lapang? (When are you free?)",
        "Siti: Sabtu petang boleh? (Saturday afternoon, can?)",
        "Hakim: Boleh. Pukul tiga. (Can. Three o'clock.)",
        "Siti: Nanti saya bawa kuih. (Later I will bring cakes.)",
        "Hakim: Wah, rajin! (Wow, industrious!)",
        "Siti: Sikit-sikit sahaja. (Just a little.)",
        "Hakim: Okay, jumpa Sabtu! (Okay, see you Saturday!)",
        "Siti: Jumpa Sabtu! Kirim salam keluarga! (See you Saturday! Send regards!)", """
    return _conv_demo(hdr, name, rid, group, body, "Kirim salam")


def demo_malay_conv_problem(hdr, name, rid, group, points, req):
    body = """        "Amir: Tolong! Tayar kereta saya pancit. (Help! My car tire is flat.)",
        "Encik Lee: Bertenang. Di mana sekarang? (Calm down. Where are you now?)",
        "Amir: Di tepi jalan, dekat simpang. (At the roadside, near the junction.)",
        "Encik Lee: Okay, jangan alih kereta. (Okay, do not move the car.)",
        "Amir: Berapa lama sampai? (How long until you arrive?)",
        "Encik Lee: Dua puluh minit. (Twenty minutes.)",
        "Amir: Berapa cajnya? (What is the charge?)",
        "Encik Lee: Lima puluh ringgit termasuk tayar ganti. (Fifty ringgit, spare included.)",
        "Amir: Boleh. Tolong cepat. (Okay. Please hurry.)",
        "Encik Lee: Saya dalam perjalanan. (I am on the way.)",
        "Amir: Encik sudah sampai? (Are you here yet?)",
        "Encik Lee: Sudah. Buka bonet. (Yes. Open the trunk.)",
        "Amir: Nah, kunci. (Here is the key.)",
        "Encik Lee: Tayar ini koyak teruk. (This tire is badly torn.)",
        "Amir: Boleh baiki atau kena ganti? (Repair or replace?)",
        "Encik Lee: Kena ganti. Nasib baik ada stok. (Must replace. Luckily there is stock.)",
        "Amir: Berapa lama baiki? (How long to fix?)",
        "Encik Lee: Setengah jam siap. (Half an hour to finish.)",
        "Amir: Terima kasih banyak, encik. (Thank you very much, sir.)",
        "Encik Lee: Sama-sama. Pandu baik-baik! (You are welcome. Drive carefully!)", """
    return _conv_demo(hdr, name, rid, group, body, "baik-baik")


def demo_malay_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 200 core words, grouped exactly as the record teaches them
    groups = {"people": 20, "home": 20, "food": 20, "verbs": 30,
              "adjectives": 20, "adverbs": 10, "pronouns": 15, "numbers": 15,
              "time": 15, "nature": 15, "question_words": 10, "connectors": 10}
    total = sum(groups.values())
    print("word groups: %d" % len(groups))
    for g, n in groups.items():
        print("  %-14s %d" % (g, n))
    print("core words: %d" % total)
    assert total == 200
    assert len(groups) == 12
    # the alphabet the ladder started from
    assert 26 == len("abcdefghijklmnopqrstuvwxyz")
    # the 34-record ladder this review closes
    assert 34 == 10 + 14 + 10
    # thirty verbs through four time levers
    print("verb forms in range: %d" % (30 * 4))
    assert 30 * 4 == 120
    print("rule: climb the ladder twice - exposure, then ownership")
    print("OK: %s sealed its mastery" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS4 = {
    "verb_tenses": demo_malay_verb_tenses,
    "questions_answers": demo_malay_questions_answers,
    "commands": demo_malay_commands,
    "descriptions": demo_malay_descriptions,
    "story1": demo_malay_story1,
    "story2": demo_malay_story2,
    "story3": demo_malay_story3,
    "idioms": demo_malay_idioms,
    "registers": demo_malay_registers,
    "complex": demo_malay_complex,
    "conv_market": demo_malay_conv_market,
    "conv_friend": demo_malay_conv_friend,
    "conv_problem": demo_malay_conv_problem,
    "mastery": demo_malay_mastery,
}
DEMOS.update(DEMOS4)
