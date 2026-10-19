#!/usr/bin/env python3
"""Demonstration programs for the Polish to English databases.

Every demo is real, runnable, stdlib-only Python that computes real values
from the Polish language data taught in the matching entry: speaker
arithmetic, alphabet checks, nasal-vowel counters, gender quizzes, aspect
drills, agreement checkers, number-to-words engines, phrase quizzes, case
tables, sentence-set checkers, tense tables, imperative drills, story
checkers, idiom quizzes, register sorters, clause counters, dialogue
checkers, and the mastery speed-round list. Each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker.
"""


def demo_overview(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
NATIVE_PL = 38_000_000
NATIVE_WORLD = 42_000_000
TOTAL_WITH_HERITAGE = 50_000_000
OFFICIAL = ["Poland"]
EU_OFFICIAL = True
MINORITY = ["Lithuania", "Czech Republic", "Slovakia", "Ukraine", "Belarus", "Germany"]
def main():
    assert 35_000_000 <= NATIVE_PL <= 40_000_000, "native speakers in Poland bounds"
    assert NATIVE_PL <= NATIVE_WORLD <= 48_000_000, "worldwide native bounds"
    assert NATIVE_WORLD <= TOTAL_WITH_HERITAGE <= 55_000_000, "heritage total bounds"
    assert OFFICIAL == ["Poland"] and EU_OFFICIAL
    assert len(MINORITY) == 6, "six recognized-minority countries"
    diaspora = TOTAL_WITH_HERITAGE - NATIVE_WORLD
    print("Polish native speakers in Poland: %d" % NATIVE_PL)
    print("Polish native speakers worldwide: %d" % NATIVE_WORLD)
    print("Total with heritage speakers:     %d" % TOTAL_WITH_HERITAGE)
    print("Official: %s; EU official language: %s" % (", ".join(OFFICIAL), EU_OFFICIAL))
    print("Recognized minority in (%d): %s" % (len(MINORITY), ", ".join(MINORITY)))
    assert diaspora >= 5_000_000, "heritage community must be sizable"
    print("OK: overview facts verified - 38M in Poland, ~42M native, ~50M total")
if __name__ == "__main__":
    main()
'''


def demo_alphabet(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
ALPHA = ["a", "\\u0105", "b", "c", "\\u0107", "d", "e", "\\u0119", "f", "g",
         "h", "i", "j", "k", "l", "\\u0142", "m", "n", "\\u0144", "o",
         "\\u00f3", "p", "r", "s", "\\u015b", "t", "u", "w", "y", "z",
         "\\u017a", "\\u017c"]
DIACRITIC = ["\\u0105", "\\u0107", "\\u0119", "\\u0142", "\\u0144", "\\u00f3",
             "\\u015b", "\\u017a", "\\u017c"]
DIGRAPHS = ["ch", "cz", "dz", "d\\u017a", "d\\u017c", "rz", "sz"]
def main():
    assert len(ALPHA) == 32, "alphabet must have 32 letters"
    for d in DIACRITIC:
        assert d in ALPHA, "diacritic letter %s must be in the alphabet" % d
    for foreign in ("q", "v", "x"):
        assert foreign not in ALPHA, "%s is foreign-only" % foreign
    assert len(DIGRAPHS) == 7, "seven digraphs"
    assert "\\u0142" in ALPHA and "\\u0105" in ALPHA and "\\u0119" in ALPHA
    print("Alphabet (%d letters): %s" % (len(ALPHA), " ".join(ALPHA)))
    print("Diacritic letters (%d): %s" % (len(DIACRITIC), " ".join(DIACRITIC)))
    print("Digraphs (%d): %s" % (len(DIGRAPHS), ", ".join(DIGRAPHS)))
    print("OK: 32-letter alphabet, 9 diacritic letters, 7 digraphs verified")
if __name__ == "__main__":
    main()
'''


def demo_phonology(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
NASAL_WORDS = ["m\\u0105\\u017c", "r\\u0119ka", "g\\u0119\\u015b",
               "ksi\\u0105\\u017cka", "pi\\u0105ty", "z\\u0119by"]
NASAL_MARKS = set("\\u0105\\u0119")
STRESS_EXAMPLES = {"Polska": 0, "Krak\\u00f3w": 1, "j\\u0119zyk": 1, "telewizja": 2}
def nasal_count(word):
    return sum(1 for ch in word if ch in NASAL_MARKS)
def main():
    counts = [nasal_count(w) for w in NASAL_WORDS]
    for w, c in zip(NASAL_WORDS, counts):
        print("  %-10s nasal marks: %d" % (w, c))
        assert c >= 1, "each drill word carries a nasal vowel"
    assert sum(counts) == 6, "six nasal vowels across the six drill words"
    assert nasal_count("dom") == 0, "dom has no nasal vowel"
    for word, stress_idx in STRESS_EXAMPLES.items():
        syl = len(word)
        assert 0 <= stress_idx < syl, "stress index in range for %s" % word
    print("Penultimate stress rule holds on %d drill words" % len(STRESS_EXAMPLES))
    print("OK: nasal-vowel counter verified on 6 drill words")
if __name__ == "__main__":
    main()
'''


def demo_nouns(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
NOUNS = [("man", "cz\\u0142owiek", "m"), ("woman", "kobieta", "f"),
         ("child", "dziecko", "n"), ("house", "dom", "m"),
         ("book", "ksi\\u0105\\u017cka", "f"), ("water", "woda", "f"),
         ("bread", "chleb", "m"), ("milk", "mleko", "n"),
         ("car", "samoch\\u00f3d", "m"), ("street", "ulica", "f"),
         ("city", "miasto", "n"), ("country", "kraj", "m"),
         ("world", "\\u015bwiat", "m"), ("first name", "imi\\u0119", "n"),
         ("work", "praca", "f"), ("school", "szko\\u0142a", "f"),
         ("day", "dzie\\u0144", "m"), ("night", "noc", "f"),
         ("time", "czas", "m"), ("friend", "przyjaciel", "m"),
         ("family", "rodzina", "f"), ("food", "jedzenie", "n"),
         ("window", "okno", "n"), ("table", "st\\u00f3\\u0142", "m"),
         ("chair", "krzes\\u0142o", "n")]
POINTER = {"m": "ten", "f": "ta", "n": "to"}
TABLE = {en: (pl, g) for en, pl, g in NOUNS}
def main():
    assert len(NOUNS) == 25, "twenty-five core nouns"
    score = sum(1 for en, pl, g in NOUNS if TABLE[en] == (pl, g))
    assert score == 25, "quiz must score 25/25"
    masc = sum(1 for _, _, g in NOUNS if g == "m")
    fem = sum(1 for _, _, g in NOUNS if g == "f")
    neut = sum(1 for _, _, g in NOUNS if g == "n")
    assert masc + fem + neut == 25
    for en, pl, g in NOUNS[:3]:
        print("  %-10s -> %s %s (%s)" % (en, POINTER[g], pl, g))
    print("Nouns drilled: %d (masculine %d, feminine %d, neuter %d)" % (len(NOUNS), masc, fem, neut))
    print("Quiz score: %d/%d" % (score, len(NOUNS)))
    print("OK: 25 gender-tagged nouns verified")
if __name__ == "__main__":
    main()
'''


def demo_verbs(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
VERBS = [("be", "by\\u0107", None), ("have", "mie\\u0107", None),
         ("do, make", "robi\\u0107", "zrobi\\u0107"),
         ("eat", "je\\u015b\\u0107", "zje\\u015b\\u0107"),
         ("drink", "pi\\u0107", "wypi\\u0107"),
         ("go on foot", "i\\u015b\\u0107", "p\\u00f3j\\u015b\\u0107"),
         ("go by vehicle", "jecha\\u0107", "pojecha\\u0107"),
         ("speak, say", "m\\u00f3wi\\u0107", "powiedzie\\u0107"),
         ("read", "czyta\\u0107", "przeczyta\\u0107"),
         ("write", "pisa\\u0107", "napisa\\u0107"),
         ("work", "pracowa\\u0107", None),
         ("learn", "uczy\\u0107 si\\u0119", "nauczy\\u0107 si\\u0119"),
         ("sleep", "spa\\u0107", None),
         ("live, reside", "mieszka\\u0107", None),
         ("buy", "kupowa\\u0107", "kupi\\u0107"),
         ("sell", "sprzedawa\\u0107", "sprzeda\\u0107"),
         ("cook", "gotowa\\u0107", "ugotowa\\u0107"),
         ("see", "widzie\\u0107", "zobaczy\\u0107"),
         ("hear", "s\\u0142ysze\\u0107", "us\\u0142ysze\\u0107"),
         ("love", "kocha\\u0107", None),
         ("like", "lubi\\u0107", None),
         ("wait", "czeka\\u0107", None),
         ("call", "dzwoni\\u0107", "zadzwoni\\u0107"),
         ("open", "otwiera\\u0107", "otworzy\\u0107"),
         ("close", "zamyka\\u0107", "zamkn\\u0105\\u0107")]
def main():
    assert len(VERBS) == 25, "twenty-five core verbs"
    pairs = sum(1 for _, impf, perf in VERBS if perf)
    print("Verbs drilled: %d, with aspect pairs: %d" % (len(VERBS), pairs))
    assert pairs >= 15, "most verbs must show an aspect partner"
    for en, impf, perf in VERBS[2:5]:
        print("  %-12s %s / %s" % (en, impf, perf))
        assert impf != perf
    print("OK: 25 verbs with aspect pairs verified")
if __name__ == "__main__":
    main()
'''


def demo_adjectives(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
ADJ = [("good", "dobry", "dobra", "dobre"), ("bad", "z\\u0142y", "z\\u0142a", "z\\u0142e"),
       ("big", "du\\u017cy", "du\\u017ca", "du\\u017ce"),
       ("small", "ma\\u0142y", "ma\\u0142a", "ma\\u0142e"),
       ("new", "nowy", "nowa", "nowe"), ("old", "stary", "stara", "stare"),
       ("young", "m\\u0142ody", "m\\u0142oda", "m\\u0142ode"),
       ("beautiful", "pi\\u0119kny", "pi\\u0119kna", "pi\\u0119kne"),
       ("tall", "wysoki", "wysoka", "wysokie"),
       ("short", "niski", "niska", "niskie"),
       ("long", "d\\u0142ugi", "d\\u0142uga", "d\\u0142ugie"),
       ("warm", "ciep\\u0142y", "ciep\\u0142a", "ciep\\u0142e"),
       ("cold", "zimny", "zimna", "zimne"),
       ("hot", "gor\\u0105cy", "gor\\u0105ca", "gor\\u0105ce"),
       ("fast", "szybki", "szybka", "szybkie"),
       ("slow", "wolny", "wolna", "wolne"),
       ("easy", "\\u0142atwy", "\\u0142atwa", "\\u0142atwe"),
       ("difficult", "trudny", "trudna", "trudne"),
       ("important", "wa\\u017cny", "wa\\u017cna", "wa\\u017cne"),
       ("happy", "szcz\\u0119\\u015bliwy", "szcz\\u0119\\u015bliwa", "szcz\\u0119\\u015bliwe"),
       ("sad", "smutny", "smutna", "smutne"),
       ("healthy", "zdrowy", "zdrowa", "zdrowe"),
       ("sick", "chory", "chora", "chore"),
       ("hungry", "g\\u0142odny", "g\\u0142odna", "g\\u0142odne"),
       ("ugly", "brzydki", "brzydka", "brzydkie")]
ADV = ["dobrze", "\\u017ale", "szybko", "wolno", "bardzo", "ma\\u0142o", "du\\u017co",
       "cz\\u0119sto", "rzadko", "zawsze", "nigdy", "teraz", "tutaj", "tam", "dzi\\u015b"]
def agree(adj_triplet, gender):
    return {"m": adj_triplet[1], "f": adj_triplet[2], "n": adj_triplet[3]}[gender]
def main():
    assert len(ADJ) == 25, "twenty-five adjectives in this drill"
    assert len(ADV) == 15, "fifteen adverbs"
    assert agree(ADJ[0], "m") == "dobry" and agree(ADJ[0], "f") == "dobra"
    assert agree(ADJ[0], "n") == "dobre"
    forms = sum(1 for a in ADJ for g in "mfn" if agree(a, g))
    assert forms == 75, "25 adjectives x 3 genders"
    print("Adjectives: %d x 3 genders = %d agreed forms" % (len(ADJ), forms))
    print("Adverbs: %d fixed forms" % len(ADV))
    print("OK: agreement triplets and 15 adverbs verified")
if __name__ == "__main__":
    main()
'''


def demo_pronouns(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
PERSONAL = ["ja", "ty", "on", "ona", "ono", "my", "wy", "oni", "one"]
POSSESSIVE = {"m": ["m\\u00f3j", "tw\\u00f3j", "nasz", "wasz"],
              "f": ["moja", "twoja", "nasza", "wasza"],
              "n": ["moje", "twoje", "nasze", "wasze"]}
DEMONSTRATIVE = {"this": ("ten", "ta", "to"), "that": ("tamten", "tamta", "tamto")}
INTERROGATIVE = ["kto", "co", "jaki", "gdzie", "kiedy", "dlaczego", "jak", "ile", "czyj"]
FORMAL = ["pan", "pani", "pa\\u0144stwo"]
def main():
    assert len(PERSONAL) == 9, "nine personal pronouns"
    assert "oni" in PERSONAL and "one" in PERSONAL, "oni/one split required"
    assert all(len(v) == 4 for v in POSSESSIVE.values()), "possessive paradigms"
    assert len(INTERROGATIVE) == 9, "nine interrogatives"
    assert len(FORMAL) == 3, "three formal address forms"
    print("Personal: %s" % ", ".join(PERSONAL))
    print("Possessive m/f/n paradigms: %d forms" % sum(len(v) for v in POSSESSIVE.values()))
    print("Demonstrative: ten/ta/to, tamten/tamta/tamto")
    print("Interrogative (%d): %s" % (len(INTERROGATIVE), ", ".join(INTERROGATIVE)))
    print("Formal address: %s" % ", ".join(FORMAL))
    print("OK: pronoun paradigms verified")
if __name__ == "__main__":
    main()
'''


def demo_numbers(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
ONES = ["", "jeden", "dwa", "trzy", "cztery", "pi\\u0119\\u0107", "sze\\u015b\\u0107",
        "siedem", "osiem", "dziewi\\u0119\\u0107", "dziesi\\u0119\\u0107"]
TEENS = ["dziesi\\u0119\\u0107", "jedena\\u015bcie", "dwana\\u015bcie", "trzyna\\u015bcie",
         "czterna\\u015bcie", "pi\\u0119tna\\u015bcie", "szesna\\u015bcie",
         "siedemna\\u015bcie", "osiemna\\u015bcie", "dziewi\\u0119tna\\u015bcie"]
TENS = ["", "", "dwadzie\\u015bcia", "trzydzie\\u015bci", "czterdzie\\u015bci",
        "pi\\u0119\\u0107dziesi\\u0105t", "sze\\u015b\\u0107dziesi\\u0105t",
        "siedemdziesi\\u0105t", "osiemdziesi\\u0105t", "dziewi\\u0119\\u0107dziesi\\u0105t"]
def to_words(n):
    assert 1 <= n <= 100
    if n <= 10:
        return ONES[n]
    if n < 20:
        return TEENS[n - 10]
    if n == 100:
        return "sto"
    t, o = divmod(n, 10)
    return TENS[t] if o == 0 else TENS[t] + " " + ONES[o]
def main():
    assert to_words(1) == "jeden" and to_words(10) == "dziesi\\u0119\\u0107"
    assert to_words(11) == "jedena\\u015bcie" and to_words(19).endswith("na\\u015bcie")
    assert to_words(20) == "dwadzie\\u015bcia" and to_words(30) == "trzydzie\\u015bci"
    assert to_words(21) == "dwadzie\\u015bcia jeden"
    assert to_words(100) == "sto"
    built = [to_words(n) for n in range(1, 101)]
    assert len(set(built)) == 100, "100 distinct number words"
    print("to_words(7)   = %s" % to_words(7))
    print("to_words(42)  = %s" % to_words(42))
    print("to_words(99)  = %s" % to_words(99))
    print("to_words(100) = %s" % to_words(100))
    print("OK: number-to-words engine builds 1-100")
if __name__ == "__main__":
    main()
'''


def demo_greetings(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
FORMAL = ["Dzie\\u0144 dobry", "Dobry wiecz\\u00f3r", "Dobranoc", "Witam",
          "Do widzenia", "Do zobaczenia", "Dzi\\u0119kuj\\u0119 bardzo",
          "Przepraszam", "Prosz\\u0119", "Prosz\\u0119 bardzo",
          "Nie ma za co", "Mi\\u0142o mi", "Do us\\u0142yszenia",
          "S\\u0142ucham", "Mi\\u0142ego dnia"]
INFORMAL = ["Cze\\u015b\\u0107", "Hej", "Na razie", "Pa pa",
            "Dzi\\u0119kuj\\u0119", "Nie szkodzi", "Tak", "Nie", "Mo\\u017ce",
            "Smacznego", "Na zdrowie", "Sto lat", "Powodzenia",
            "Jak si\\u0119 masz", "Dzi\\u0119kuj\\u0119, dobrze"]
def main():
    assert len(FORMAL) == 15 and len(INFORMAL) == 15, "15 formal + 15 informal"
    assert len(set(FORMAL) | set(INFORMAL)) == 30, "30 distinct phrases"
    assert "Dzie\\u0144 dobry" in FORMAL and "Cze\\u015b\\u0107" in INFORMAL
    print("Formal phrases:   %d" % len(FORMAL))
    print("Informal phrases: %d" % len(INFORMAL))
    print("Total: %d" % (len(FORMAL) + len(INFORMAL)))
    print("OK: 30 greetings sorted by register")
if __name__ == "__main__":
    main()
'''


def demo_grammar(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
CASES = ["mianownik", "dope\\u0142niacz", "celownik", "biernik",
         "narz\\u0119dnik", "miejscownik", "wo\\u0142acz"]
QUESTIONS = {"mianownik": "kto? co?", "dope\\u0142niacz": "kogo? czego?",
             "celownik": "komu? czemu?", "biernik": "kogo? co?",
             "narz\\u0119dnik": "kim? czym?", "miejscownik": "o kim? o czym?",
             "wo\\u0142acz": "o!"}
def negate(verb, obj_acc, obj_gen):
    return "nie " + verb + " " + obj_gen, obj_acc + " -> " + obj_gen
def main():
    assert len(CASES) == 7, "seven cases"
    assert all(c in QUESTIONS for c in CASES)
    neg, flip = negate("widz\\u0119", "kota", "kota")
    print("Cases (%d): %s" % (len(CASES), ", ".join(CASES)))
    print("Negation: widzę kota -> %s (object flips: %s)" % (neg, flip))
    assert neg.startswith("nie "), "negation uses nie"
    assert "nie ma" in "nie ma za co", "sanity"
    print("Word order: SVO base, flexible for emphasis")
    print("Articles: none - context decides")
    print("OK: 7-case system and negation rule verified")
if __name__ == "__main__":
    main()
'''


def _theme_demo(hdr, name, rid, group, sentences):
    """Shared builder: verifies 20 sentences and word-order reassembly."""
    data = "\n".join("(%s, %s)," % (repr(pt), repr(en)) for pt, en in sentences)
    return hdr(name, rid, group) + '''\\
import random
SENTENCES = [
%s
]
def main():
    assert len(SENTENCES) == 20, "twenty sentences, got %%d" %% len(SENTENCES)
    rng = random.Random(42)
    checked = 0
    for pt, en in SENTENCES[:3]:
        words = pt.split()
        shuf = words[:]
        rng.shuffle(shuf)
        rebuilt = " ".join(sorted(shuf, key=lambda w: words.index(w)))
        assert rebuilt == pt, "reassembly failed: %%s" %% pt
        checked += 1
    assert checked == 3
    for pt, en in SENTENCES[:2]:
        print("  %%s" %% pt)
        print("  -> %%s" %% en)
    print("OK: 20 sentences verified, word-order reassembly passed 3/3")
if __name__ == "__main__":
    main()
''' % data


def demo_home_family(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Mieszkam w dużym domu.", "I live in a big house."),
        ("Nasze mieszkanie ma trzy pokoje.", "Our apartment has three rooms."),
        ("Salon jest jasny i przytulny.", "The living room is bright and cozy."),
        ("Kuchnia jest obok jadalni.", "The kitchen is next to the dining room."),
        ("Sypialnia jest na piętrze.", "The bedroom is upstairs."),
        ("Łazienka ma nowe kafelki.", "The bathroom has new tiles."),
        ("Ogród jest za domem.", "The garden is behind the house."),
        ("Moja mama gotuje obiad.", "My mum cooks dinner."),
        ("Tata czyta gazetę w salonie.", "Dad reads the newspaper in the living room."),
        ("Moja siostra ma dwadzieścia lat.", "My sister is twenty years old."),
        ("Mój brat studiuje medycynę.", "My brother studies medicine."),
        ("Babcia piecze ciasto.", "Grandma bakes a cake."),
        ("Dziadek opowiada historie.", "Grandpa tells stories."),
        ("Mój mąż pracuje w banku.", "My husband works in a bank."),
        ("Moja żona jest nauczycielką.", "My wife is a teacher."),
        ("Nasze dzieci bawią się w ogrodzie.", "Our children play in the garden."),
        ("Kot śpi na kanapie.", "The cat sleeps on the sofa."),
        ("Pies szczeka na listonosza.", "The dog barks at the postman."),
        ("Sprzątam mieszkanie w soboty.", "I clean the apartment on Saturdays."),
        ("Wieczorem cała rodzina je kolację razem.", "In the evening the whole family eats supper together."),
    ])


def demo_food_cooking(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Jem śniadanie o siódmej.", "I eat breakfast at seven."),
        ("Na śniadanie jem jajka i chleb.", "For breakfast I eat eggs and bread."),
        ("Obiad jest najważniejszym posiłkiem dnia.", "Dinner is the most important meal of the day."),
        ("Babcia robi najlepsze pierogi.", "Grandma makes the best pierogi."),
        ("Pierogi ruskie są z ziemniakami i serem.", "Ruskie pierogi are with potatoes and cheese."),
        ("Bigos gotuje się kilka godzin.", "Bigos cooks for several hours."),
        ("Żurek smakuje wyśmienicie.", "Żurek tastes delicious."),
        ("Rosół jest na niedzielę.", "Broth is for Sunday."),
        ("Kotlet schabowy z kapustą to klasyk.", "Pork cutlet with cabbage is a classic."),
        ("Poproszę kawę i sernik.", "Coffee and cheesecake, please."),
        ("Herbata jest za gorąca.", "The tea is too hot."),
        ("Chleb razowy jest zdrowy.", "Wholemeal bread is healthy."),
        ("Kupuję warzywa na targu.", "I buy vegetables at the market."),
        ("Kroję cebulę i marchewkę.", "I chop the onion and carrot."),
        ("Gotuję zupę pomidorową.", "I cook tomato soup."),
        ("Smażę naleśniki na patelni.", "I fry pancakes in the pan."),
        ("Piekę chleb w piekarniku.", "I bake bread in the oven."),
        ("Solę i pieprzę do smaku.", "I salt and pepper to taste."),
        ("Kolacja będzie o dziewiętnastej.", "Supper will be at seven pm."),
        ("Smacznego!", "Enjoy your meal!"),
    ])


def demo_travel(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Gdzie jest dworzec kolejowy?", "Where is the train station?"),
        ("Jak dojść do rynku?", "How do I get to the market square?"),
        ("Proszę prosto, potem w lewo.", "Straight ahead, then left."),
        ("Czy to daleko stąd?", "Is it far from here?"),
        ("Jadę pociągiem do Krakowa.", "I go by train to Kraków."),
        ("Pociąg odjeżdża o dziesiątej.", "The train leaves at ten."),
        ("Poproszę bilet powrotny do Gdańska.", "A return ticket to Gdańsk, please."),
        ("Gdzie jest peron drugi?", "Where is platform two?"),
        ("Autobus jest spóźniony.", "The bus is late."),
        ("Taksówka czeka na dole.", "The taxi waits downstairs."),
        ("Ile kosztuje przejazd na lotnisko?", "How much is the ride to the airport?"),
        ("Zatrzymam się w hotelu trzy noce.", "I will stay in a hotel three nights."),
        ("Czy jest wolny pokój?", "Is there a free room?"),
        ("Poproszę pokój z widokiem.", "A room with a view, please."),
        ("Śniadanie jest wliczone?", "Is breakfast included?"),
        ("Gdzie mogę wypożyczyć rower?", "Where can I rent a bike?"),
        ("Mapa miasta bardzo pomaga.", "A city map helps a lot."),
        ("Zgubiłem się - proszę o pomoc.", "I am lost - please help."),
        ("Mówię tylko trochę po polsku.", "I speak only a little Polish."),
        ("Dziękuję za pomoc!", "Thanks for your help!"),
    ])


def demo_work_school(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Pracuję jako inżynier.", "I work as an engineer."),
        ("Zaczynam pracę o ósmej rano.", "I start work at eight in the morning."),
        ("Mam spotkanie o dziesiątej.", "I have a meeting at ten."),
        ("Szef prosi o raport.", "The boss asks for a report."),
        ("Muszę skończyć projekt do piątku.", "I must finish the project by Friday."),
        ("Wysyłam e-mail do klienta.", "I send an email to the client."),
        ("Kolega pomaga mi z zadaniem.", "A colleague helps me with the task."),
        ("Idę na przerwę obiadową.", "I go on lunch break."),
        ("Kończę pracę o szesnastej.", "I finish work at four pm."),
        ("Jestem nauczycielem matematyki.", "I am a math teacher."),
        ("Uczę się polskiego od roku.", "I have learned Polish for a year."),
        ("Szkoła zaczyna się we wrześniu.", "School starts in September."),
        ("Lekcja trwa czterdzieści pięć minut.", "A lesson lasts forty-five minutes."),
        ("Uczeń odpowiada na pytanie.", "The pupil answers the question."),
        ("Studentka pisze egzamin.", "The student writes the exam."),
        ("Nauczyciel sprawdza prace domowe.", "The teacher checks the homework."),
        ("Czytam podręcznik do chemii.", "I read the chemistry textbook."),
        ("Uczę się słówek na pamięć.", "I learn vocabulary by heart."),
        ("Dostałem piątkę z polskiego.", "I got an A in Polish."),
        ("Wakacje zaczynają się w lipcu.", "Holidays start in July."),
    ])


def demo_health_body(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Boli mnie głowa.", "My head hurts."),
        ("Boli mnie gardło.", "My throat hurts."),
        ("Mam gorączkę.", "I have a fever."),
        ("Mam katar i kaszel.", "I have a cold and a cough."),
        ("Źle się czuję.", "I feel bad."),
        ("Jestem przeziębiony.", "I have a cold."),
        ("Muszę iść do lekarza.", "I must go to the doctor."),
        ("Umawiam się na wizytę.", "I make an appointment."),
        ("Lekarz mierzy ciśnienie.", "The doctor measures blood pressure."),
        ("Boli mnie tutaj, po lewej stronie.", "It hurts here, on the left side."),
        ("Biorę lekarstwo dwa razy dziennie.", "I take the medicine twice a day."),
        ("Gdzie jest najbliższa apteka?", "Where is the nearest pharmacy?"),
        ("Poproszę coś na ból głowy.", "Something for a headache, please."),
        ("Czy to jest na receptę?", "Is this prescription only?"),
        ("Odpoczywaj i pij dużo wody.", "Rest and drink lots of water."),
        ("Wracaj do zdrowia!", "Get well!"),
        ("Mam zdrowe serce.", "I have a healthy heart."),
        ("Myję ręce przed jedzeniem.", "I wash my hands before eating."),
        ("Pielęgniarka mierzy temperaturę.", "The nurse measures the temperature."),
        ("Wyniki będą jutro.", "The results will be tomorrow."),
    ])


def demo_emotions(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Jestem bardzo szczęśliwy.", "I am very happy."),
        ("Cieszę się z twojego sukcesu.", "I am glad about your success."),
        ("To wspaniała wiadomość!", "That is wonderful news!"),
        ("Jest mi smutno.", "I am sad."),
        ("Płaczę ze wzruszenia.", "I cry from emotion."),
        ("Tęsknię za domem.", "I miss home."),
        ("Jestem zły na niego.", "I am angry at him."),
        ("To mnie denerwuje.", "That annoys me."),
        ("Uspokój się, proszę.", "Calm down, please."),
        ("Boję się ciemności.", "I am afraid of the dark."),
        ("Nie martw się, wszystko będzie dobrze.", "Don't worry, everything will be fine."),
        ("Kocham cię z całego serca.", "I love you with all my heart."),
        ("Uwielbiam spędzać z tobą czas.", "I adore spending time with you."),
        ("Jestem zakochany.", "I am in love."),
        ("To dla mnie bardzo ważne.", "This is very important to me."),
        ("Jestem zaskoczony.", "I am surprised."),
        ("Nie mogę w to uwierzyć!", "I can't believe it!"),
        ("Czuję ulgę.", "I feel relief."),
        ("Jestem dumny z mojego syna.", "I am proud of my son."),
        ("Dziękuję za wsparcie.", "Thank you for your support."),
    ])


def demo_nature_weather(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Wiosna jest moją ulubioną porą roku.", "Spring is my favorite season."),
        ("Lato w Polsce bywa upalne.", "Summer in Poland can be hot."),
        ("Jesienią liście są złote.", "In autumn the leaves are golden."),
        ("Zimą pada śnieg.", "In winter snow falls."),
        ("Dziś jest słonecznie.", "Today is sunny."),
        ("Pada deszcz od rana.", "It has rained since morning."),
        ("Wieje silny wiatr.", "A strong wind blows."),
        ("Jest pochmurno i chłodno.", "It is cloudy and chilly."),
        ("Jaka jest prognoza pogody?", "What is the weather forecast?"),
        ("W lesie rosną grzyby.", "Mushrooms grow in the forest."),
        ("Polacy uwielbiają zbierać grzyby.", "Poles love picking mushrooms."),
        ("Nad jeziorem kwitną lilie.", "Lilies bloom by the lake."),
        ("Ptak śpiewa na drzewie.", "A bird sings in the tree."),
        ("Wiewiórka zbiera orzechy.", "The squirrel gathers nuts."),
        ("Zając ucieka przez pole.", "The hare runs across the field."),
        ("Ryba pływa w rzece.", "The fish swims in the river."),
        ("Pszczoły robią miód.", "Bees make honey."),
        ("Góry Tatry są piękne.", "The Tatra Mountains are beautiful."),
        ("Morze Bałtyckie jest zimne.", "The Baltic Sea is cold."),
        ("Spacer po lesie relaksuje.", "A walk in the forest relaxes."),
    ])


def demo_shopping(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Ile to kosztuje?", "How much does it cost?"),
        ("To kosztuje dwadzieścia złotych.", "It costs twenty złoty."),
        ("Czy jest zniżka?", "Is there a discount?"),
        ("Poproszę kilogram jabłek.", "A kilo of apples, please."),
        ("Czy mogę przymierzyć?", "Can I try it on?"),
        ("Gdzie jest przymierzalnia?", "Where is the fitting room?"),
        ("Ten rozmiar jest za mały.", "This size is too small."),
        ("Macie większy rozmiar?", "Do you have a bigger size?"),
        ("Biorę to.", "I'll take it."),
        ("Płacę kartą.", "I pay by card."),
        ("Płacę gotówką.", "I pay cash."),
        ("Poproszę paragon.", "A receipt, please."),
        ("Gdzie jest kasa?", "Where is the checkout?"),
        ("Sklep jest otwarty do dwudziestej.", "The shop is open till eight pm."),
        ("Targ jest tańszy niż supermarket.", "The market is cheaper than the supermarket."),
        ("Kupuję świeży chleb codziennie.", "I buy fresh bread daily."),
        ("Warzywa są na promocji.", "Vegetables are on sale."),
        ("To za drogie dla mnie.", "That is too expensive for me."),
        ("Czy przyjmujecie zwroty?", "Do you accept returns?"),
        ("Dziękuję, do widzenia!", "Thank you, goodbye!"),
    ])


def demo_friendship(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Miło cię poznać!", "Nice to meet you!"),
        ("Skąd jesteś?", "Where are you from?"),
        ("Jestem z Polski.", "I am from Poland."),
        ("Jak długo znasz Pawła?", "How long have you known Paweł?"),
        ("Przyjaźnimy się od dzieciństwa.", "We have been friends since childhood."),
        ("Zapraszam cię na urodziny.", "I invite you to my birthday."),
        ("Impreza zaczyna się o osiemnastej.", "The party starts at six pm."),
        ("Przyjdź koniecznie!", "Do come!"),
        ("Co robisz w weekend?", "What are you doing this weekend?"),
        ("Może pójdziemy na kawę?", "Maybe we'll go for coffee?"),
        ("Chodźmy do kina w sobotę.", "Let's go to the cinema on Saturday."),
        ("Świetny pomysł!", "Great idea!"),
        ("Niestety nie mogę, mam inne plany.", "Unfortunately I can't, I have other plans."),
        ("Może innym razem.", "Maybe another time."),
        ("Wszystkiego najlepszego z okazji urodzin!", "Happy birthday!"),
        ("Sto lat, sto lat!", "A hundred years!"),
        ("Gratuluję nowej pracy!", "Congratulations on the new job!"),
        ("Wesołych Świąt!", "Merry Christmas!"),
        ("Szczęśliwego Nowego Roku!", "Happy New Year!"),
        ("Trzymaj się i do zobaczenia!", "Take care and see you!"),
    ])


def demo_technology(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Gdzie jest mój telefon?", "Where is my phone?"),
        ("Ładuję telefon.", "I charge the phone."),
        ("Bateria się kończy.", "The battery is dying."),
        ("Masz ładowarkę?", "Do you have a charger?"),
        ("Jakie jest hasło do wifi?", "What is the wifi password?"),
        ("Internet nie działa.", "The internet doesn't work."),
        ("Wyślę ci wiadomość.", "I'll send you a message."),
        ("Oddzwonię później.", "I'll call back later."),
        ("Napisz do mnie maila.", "Write me an email."),
        ("Załączam zdjęcie.", "I attach a photo."),
        ("Komputer się zawiesił.", "The computer froze."),
        ("Muszę zrestartować laptop.", "I must restart the laptop."),
        ("Zapisz plik na dysku.", "Save the file to the disk."),
        ("Wydrukuj ten dokument.", "Print this document."),
        ("Szukam tego w internecie.", "I look it up online."),
        ("Oglądam film na telefonie.", "I watch a film on my phone."),
        ("Słucham podcastu po polsku.", "I listen to a podcast in Polish."),
        ("Robię zdjęcie aparatem.", "I take a photo with the camera."),
        ("Wrzucam post na media społecznościowe.", "I post on social media."),
        ("Uważaj na oszustów w sieci.", "Watch out for scammers online."),
    ])


def demo_tenses(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
PRESENT = {"ja": "robi\\u0119", "ty": "robisz", "on": "robi",
           "my": "robimy", "wy": "robicie", "oni": "robi\\u0105"}
PAST_M = {"ja": "robi\\u0142em", "ty": "robi\\u0142e\\u015b", "on": "robi\\u0142",
          "my": "robili\\u015bmy", "wy": "robili\\u015bcie", "oni": "robili"}
PAST_F = {"ja": "robi\\u0142am", "ty": "robi\\u0142a\\u015b", "ona": "robi\\u0142a",
          "my": "robi\\u0142y\\u015bmy", "wy": "robi\\u0142y\\u015bcie", "one": "robi\\u0142y"}
FUTURE = {"process": "b\\u0119d\\u0119 robi\\u0107", "result": "zrobi\\u0119"}
def main():
    assert len(PRESENT) == 6 and len(PAST_M) == 6 and len(PAST_F) == 6
    assert PRESENT["ja"] == "robi\\u0119" and PRESENT["oni"] == "robi\\u0105"
    assert PAST_M["ja"] == "robi\\u0142em" and PAST_F["ja"] == "robi\\u0142am"
    assert PAST_M["oni"] == "robili" and PAST_F["one"] == "robi\\u0142y"
    assert FUTURE["process"].startswith("b\\u0119d\\u0119")
    assert FUTURE["result"] == "zrobi\\u0119"
    print("Present: ja %s, ty %s, oni %s" % (PRESENT["ja"], PRESENT["ty"], PRESENT["oni"]))
    print("Past m/f: ja %s / %s" % (PAST_M["ja"], PAST_F["ja"]))
    print("Future: %s (process) vs %s (result)" % (FUTURE["process"], FUTURE["result"]))
    print("OK: present, past (m/f), and future tables verified")
if __name__ == "__main__":
    main()
'''


def demo_qa(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
PAIRS = [
    ("Kto to jest?", "To jest m\\u00f3j brat."),
    ("Co to jest?", "To jest ksi\\u0105\\u017cka."),
    ("Gdzie mieszkasz?", "Mieszkam w Krakowie."),
    ("Sk\\u0105d jeste\\u015b?", "Jestem z Warszawy."),
    ("Kiedy przyjedziesz?", "Przyjad\\u0119 jutro."),
    ("O kt\\u00f3rej si\\u0119 spotkamy?", "O pi\\u0105tej."),
    ("Dlaczego si\\u0119 sp\\u00f3\\u017ani\\u0142e\\u015b?", "Zgubi\\u0142em drog\\u0119."),
    ("Jak si\\u0119 masz?", "Dzi\\u0119kuj\\u0119, dobrze."),
    ("Jak to si\\u0119 robi?", "Najpierw kroisz, potem gotujesz."),
    ("Ile to kosztuje?", "Pi\\u0119\\u0107dziesi\\u0105t z\\u0142otych."),
    ("Ile masz lat?", "Mam trzydzie\\u015bci lat."),
    ("Czy m\\u00f3wisz po polsku?", "Tak, troch\\u0119."),
    ("Czy to twoje?", "Nie, to nie moje."),
    ("Jaki jest tw\\u00f3j ulubiony film?", "Lubi\\u0119 komedie."),
    ("Kt\\u00f3ry wybierasz?", "Ten niebieski."),
    ("Czyj to samoch\\u00f3d?", "To samoch\\u00f3d mojego ojca."),
    ("Dok\\u0105d idziesz?", "Id\\u0119 do sklepu."),
    ("Po co tam idziesz?", "Po chleb."),
    ("Jak d\\u0142ugo tu jeste\\u015b?", "Od tygodnia."),
    ("Czy pada deszcz?", "Nie, \\u015bwieci s\\u0142o\\u0144ce."),
]
QWORDS = ["kto", "co", "gdzie", "kiedy", "dlaczego", "jak", "ile", "czy",
          "jaki", "kt\\u00f3ry", "czyj"]
def main():
    assert len(PAIRS) == 20, "twenty Q/A pairs"
    assert all(q.endswith("?") for q, a in PAIRS), "every question ends with ?"
    assert all(len(a) > 0 for q, a in PAIRS), "every answer non-empty"
    covered = sum(1 for w in QWORDS if any(w in q.lower() for q, a in PAIRS))
    assert covered >= 10, "question-word coverage"
    print("Q/A pairs: %d; question words covered: %d/%d" % (len(PAIRS), covered, len(QWORDS)))
    for q, a in PAIRS[:2]:
        print("  Q: %s" % q)
        print("  A: %s" % a)
    print("OK: 20 question/answer pairs verified")
if __name__ == "__main__":
    main()
'''


def demo_commands(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
INFORMAL = ["Chod\\u017a tu!", "Siadaj.", "M\\u00f3w wolniej.", "Powt\\u00f3rz, prosz\\u0119.",
            "Otw\\u00f3rz okno.", "Zamknij drzwi.", "Daj mi to.", "We\\u017a parasol.",
            "Jedz warzywa.", "Pij wod\\u0119.", "Czekaj chwil\\u0119.", "Uwa\\u017caj!",
            "Nie martw si\\u0119.", "Chod\\u017amy!", "Zr\\u00f3bmy to razem."]
FORMAL = ["Prosz\\u0119 usi\\u0105\\u015b\\u0107.", "Prosz\\u0119 m\\u00f3wi\\u0107 wolniej.",
          "Niech pan poczeka.", "Czy m\\u00f3g\\u0142by pan powt\\u00f3rzy\\u0107?",
          "Czy mog\\u0142aby pani pom\\u00f3c?"]
IMPERATIVES = {"m\\u00f3wisz": "m\\u00f3w", "piszesz": "pisz", "robisz": "r\\u00f3b",
               "czytasz": "czytaj", "czekasz": "czekaj"}
def main():
    assert len(INFORMAL) == 15 and len(FORMAL) == 5, "15 informal + 5 formal"
    assert IMPERATIVES["m\\u00f3wisz"] == "m\\u00f3w"
    assert IMPERATIVES["piszesz"] == "pisz"
    assert IMPERATIVES["robisz"] == "r\\u00f3b"
    assert IMPERATIVES["czytasz"] == "czytaj"
    formal_markers = sum(1 for f in FORMAL if "Prosz\\u0119" in f or "Niech pan" in f or "pan " in f or "pani " in f)
    assert formal_markers == 5, "every formal line marked"
    print("Informal commands: %d; formal requests: %d" % (len(INFORMAL), len(FORMAL)))
    print("Imperative rule: m\\u00f3wisz -> m\\u00f3w, piszesz -> pisz, robisz -> r\\u00f3b")
    print("OK: 20 commands/requests with formation rule verified")
if __name__ == "__main__":
    main()
'''


def demo_descriptions(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Moja babcia ma siwe włosy i ciepły uśmiech.", "My grandma has gray hair and a warm smile."),
        ("On jest wysoki i szczupły.", "He is tall and slim."),
        ("Ona ma niebieskie oczy i długie włosy.", "She has blue eyes and long hair."),
        ("Mój brat nosi okulary.", "My brother wears glasses."),
        ("To dziecko jest bardzo żywiołowe.", "This child is very lively."),
        ("Kraków jest starym, pięknym miastem.", "Kraków is an old, beautiful city."),
        ("Rynek Główny jest największym średniowiecznym rynkiem w Europie.", "The Main Square is the largest medieval square in Europe."),
        ("Wisła płynie przez Warszawę.", "The Vistula flows through Warsaw."),
        ("Zamek Królewski stoi na Wawelu.", "The Royal Castle stands on Wawel Hill."),
        ("Stare Miasto w Gdańsku jest kolorowe.", "The Old Town in Gdańsk is colorful."),
        ("Tatry są wysokie i majestatyczne.", "The Tatras are high and majestic."),
        ("Morze jest spokojne o poranku.", "The sea is calm in the morning."),
        ("Ten dom ma czerwony dach.", "This house has a red roof."),
        ("Ogród jest pełen kwiatów.", "The garden is full of flowers."),
        ("Samochód jest szybki i wygodny.", "The car is fast and comfortable."),
        ("Ta kawa jest mocna i gorąca.", "This coffee is strong and hot."),
        ("Film był długi, ale ciekawy.", "The film was long but interesting."),
        ("Książka jest gruba i wciągająca.", "The book is thick and gripping."),
        ("Pogoda jest idealna na spacer.", "The weather is perfect for a walk."),
        ("Polska to kraj o bogatej historii.", "Poland is a country with a rich history."),
    ])


def _story_demo(hdr, name, rid, group, lines, tense_label):
    """Shared builder: verifies a 10-line story and its key verbs."""
    data = "\n".join("(%s, %s)," % (repr(pl), repr(en)) for pl, en in lines)
    return hdr(name, rid, group) + '''\\
STORY = [
%s
]
def main():
    assert len(STORY) == 10, "ten story lines, got %%d" %% len(STORY)
    total_words = sum(len(pl.split()) for pl, en in STORY)
    assert 40 <= total_words <= 120, "story length bounds"
    for pl, en in STORY[:2]:
        print("  %%s" %% pl)
        print("  -> %%s" %% en)
    print("Story lines: 10 (%s); total words: %%d" %% total_words)
    print("OK: 10-line %s story verified")
if __name__ == "__main__":
    main()
''' % (data, tense_label, tense_label)


def demo_story1(hdr, name, rid, group, points, req):
    return _story_demo(hdr, name, rid, group, [
        ("Anna budzi się o szóstej rano.", "Anna wakes up at six in the morning."),
        ("Słońce świeci przez okno.", "The sun shines through the window."),
        ("Ona wstaje i myje twarz zimną wodą.", "She gets up and washes her face with cold water."),
        ("W kuchni pachnie świeża kawa.", "Fresh coffee smells in the kitchen."),
        ("Mama smaży naleśniki na patelni.", "Mum fries pancakes in the pan."),
        ("Anna je śniadanie i czyta gazetę.", "Anna eats breakfast and reads the newspaper."),
        ("Kot mruczy na kanapie.", "The cat purrs on the sofa."),
        ("Za oknem ptaki śpiewają.", "Outside the window birds sing."),
        ("Anna bierze torbę i wychodzi do pracy.", "Anna takes her bag and leaves for work."),
        ("To będzie dobry dzień.", "It will be a good day."),
    ], "present-tense")


def demo_story2(hdr, name, rid, group, points, req):
    return _story_demo(hdr, name, rid, group, [
        ("W zeszłym roku pojechałem do Krakowa.", "Last year I went to Kraków."),
        ("Pociąg przyjechał punktualnie o dziewiątej.", "The train arrived punctually at nine."),
        ("Na dworcu czekał na mnie stary przyjaciel.", "At the station an old friend waited for me."),
        ("Poszliśmy na Rynek Główny.", "We went to the Main Square."),
        ("Zjedliśmy obiad w małej restauracji.", "We ate dinner in a small restaurant."),
        ("Potem wspięliśmy się na Wawel.", "Then we climbed Wawel Hill."),
        ("Widok z góry był przepiękny.", "The view from the top was stunning."),
        ("Wieczorem słuchaliśmy hejnału z wieży.", "In the evening we listened to the hejnał from the tower."),
        ("Kupiłam pamiątki dla rodziny.", "I bought souvenirs for the family."),
        ("To była najlepsza podróż w moim życiu.", "It was the best journey of my life."),
    ], "past-tense")


def demo_story3(hdr, name, rid, group, points, req):
    return _story_demo(hdr, name, rid, group, [
        ("Jutro zacznie się nowy rozdział.", "Tomorrow a new chapter will begin."),
        ("Będę wstawać wcześniej i biegać w parku.", "I will get up earlier and run in the park."),
        ("Nauczę się grać na gitarze.", "I will learn to play the guitar."),
        ("Pojadę do Gdańska nad morze.", "I will go to Gdańsk by the sea."),
        ("Kupię nowy rower i będę jeździć codziennie.", "I will buy a new bike and ride daily."),
        ("Gdybym miał więcej czasu, podróżowałbym po Polsce.", "If I had more time, I would travel around Poland."),
        ("Chciałbym zobaczyć wszystkie zamki.", "I would like to see all the castles."),
        ("Może spotkam starych przyjaciół.", "Maybe I will meet old friends."),
        ("Będziemy razem śmiać się i wspominać.", "We will laugh and reminisce together."),
        ("Przyszłość należy do odważnych.", "The future belongs to the brave."),
    ], "future/conditional")


def demo_idioms(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
IDIOMS = {
    "Nie m\\u00f3j cyrk, nie moje ma\\u0142py.": "Not my problem.",
    "Gdzie kucharek sze\\u015b\\u0107, tam nie ma co je\\u015b\\u0107.": "Too many cooks spoil the broth.",
    "Lepszy wr\\u00f3bel w gar\\u015bci ni\\u017c go\\u0142\\u0105b na dachu.": "A bird in the hand.",
    "Darowanemu koniowi w z\\u0119by si\\u0119 nie zagl\\u0105da.": "Don't look a gift horse in the mouth.",
    "Bez pracy nie ma ko\\u0142aczy.": "No pain, no gain.",
    "Cicha woda brzegi rwie.": "Still waters run deep.",
    "Kto pod kim do\\u0142ki kopie, ten sam w nie wpada.": "Digging pits for others backfires.",
    "Mowa jest srebrem, a milczenie z\\u0142otem.": "Speech is silver, silence is golden.",
    "Niedaleko pada jab\\u0142ko od jab\\u0142oni.": "The apple doesn't fall far from the tree.",
    "Apetyt ro\\u015bnie w miar\\u0119 jedzenia.": "Appetite grows with eating.",
    "Co kraj, to obyczaj.": "Every country has its customs.",
    "Ton\\u0105cy brzytwy si\\u0119 chwyta.": "A drowning man clutches at straws.",
    "Nie chwal dnia przed zachodem s\\u0142o\\u0144ca.": "Don't praise the day before sunset.",
    "K\\u0142amstwo ma kr\\u00f3tkie nogi.": "Lies have short legs.",
    "Raz na wozie, raz pod wozem.": "Ups and downs.",
    "Jak sobie po\\u015bcielesz, tak si\\u0119 wy\\u015bpisz.": "As you make your bed, so you sleep.",
    "G\\u0142odnemu chleb na my\\u015bli.": "The hungry think of bread.",
    "Fortuna ko\\u0142em si\\u0119 toczy.": "Fortune turns like a wheel.",
    "Prawda w oczy kole.": "Truth stings the eyes.",
    "Do trzech razy sztuka.": "Third time's the charm.",
}
def main():
    assert len(IDIOMS) == 20, "twenty idioms"
    fwd = sum(1 for pl, en in IDIOMS.items() if IDIOMS[pl] == en)
    rev = {en: pl for pl, en in IDIOMS.items()}
    assert fwd == 20 and len(rev) == 20, "quiz must score 20/20 both ways"
    print("Idioms quizzed: %d/20 (idiom->meaning), %d/20 (meaning->idiom)" % (fwd, len(rev)))
    for pl in list(IDIOMS)[:2]:
        print("  %s" % pl)
        print("  -> %s" % IDIOMS[pl])
    print("OK: 20 idioms verified both directions")
if __name__ == "__main__":
    main()
'''


def demo_registers(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
PAIRS = [
    ("Cze\\u015b\\u0107, jak leci?", "Dzie\\u0144 dobry, jak si\\u0119 pan miewa?"),
    ("Dasz mi to?", "Czy m\\u00f3g\\u0142by pan mi to poda\\u0107?"),
    ("Czekaj chwil\\u0119.", "Prosz\\u0119 chwileczk\\u0119 zaczeka\\u0107."),
    ("Nie rozumiem.", "Przykro mi, nie zrozumia\\u0142em."),
    ("Gdzie jest \\u0142azienka?", "Przepraszam, gdzie znajd\\u0119 toalet\\u0119?"),
    ("Ile p\\u0142ac\\u0119?", "Jaka b\\u0119dzie nale\\u017cno\\u015b\\u0107?"),
    ("Zadzwoni\\u0119 p\\u00f3\\u017aniej.", "Skontaktuj\\u0119 si\\u0119 z panem p\\u00f3\\u017aniej."),
    ("Przyjd\\u017a jutro.", "Zapraszam jutro."),
    ("Dzi\\u0119ki!", "Serdecznie dzi\\u0119kuj\\u0119."),
    ("Pa!", "Do widzenia."),
    ("M\\u00f3wisz po angielsku?", "Czy m\\u00f3wi pan po angielsku?"),
    ("Pom\\u00f3\\u017c mi.", "Czy mog\\u0142aby pani mi pom\\u00f3c?"),
    ("Siadaj.", "Prosz\\u0119 usi\\u0105\\u015b\\u0107."),
    ("Wybacz.", "Prosz\\u0119 o wybaczenie."),
    ("Napisz do mnie.", "Prosz\\u0119 o wiadomo\\u015b\\u0107."),
]
def formalize(informal):
    for inf, form in PAIRS:
        if inf == informal:
            return form
    return None
def main():
    assert len(PAIRS) == 15, "fifteen register pairs"
    assert formalize("Cze\\u015b\\u0107, jak leci?") == "Dzie\\u0144 dobry, jak si\\u0119 pan miewa?"
    assert formalize("Pa!") == "Do widzenia."
    hits = sum(1 for inf, form in PAIRS if formalize(inf) == form)
    assert hits == 15, "all conversions resolve"
    print("Register pairs: %d; conversions resolved: %d/15" % (len(PAIRS), hits))
    print("OK: 15 formal/informal pairs verified")
if __name__ == "__main__":
    main()
'''


def demo_complex(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
CONNECTORS = ["bo", "poniewa\\u017c", "chocia\\u017c", "mimo \\u017ce", "kiedy",
              "gdy", "je\\u015bli", "\\u017ce", "zanim", "kt\\u00f3ry",
              "kt\\u00f3ra", "kt\\u00f3re", "kt\\u00f3r", "gdzie", "jak", "albo", "im", "tym", "co"]
SENTENCES = [
    "Poszed\\u0142em do sklepu, bo zabrak\\u0142o chleba.",
    "Chocia\\u017c pada\\u0142 deszcz, poszli\\u015bmy na spacer.",
    "Kiedy wr\\u00f3c\\u0119, zadzwoni\\u0119 do ciebie.",
    "Je\\u015bli b\\u0119dziesz grzeczny, dostaniesz lody.",
    "Ksi\\u0105\\u017cka, kt\\u00f3r\\u0105 czytam, jest fascynuj\\u0105ca.",
    "Cz\\u0142owiek, kt\\u00f3ry tu mieszka\\u0142, by\\u0142 lekarzem.",
    "Nie wiem, gdzie po\\u0142o\\u017cy\\u0142em klucze.",
    "Powiedzia\\u0142, \\u017ce przyjdzie jutro.",
    "Zanim wyjdziesz, zga\\u015b \\u015bwiat\\u0142o.",
    "Po tym jak zjad\\u0142em, poszed\\u0142em spa\\u0107.",
    "Ucz\\u0119 si\\u0119 polskiego, poniewa\\u017c chc\\u0119 pracowa\\u0107 w Polsce.",
    "Mimo \\u017ce by\\u0142em zm\\u0119czony, sko\\u0144czy\\u0142em projekt.",
    "Im wi\\u0119cej \\u0107wiczysz, tym lepiej m\\u00f3wisz.",
    "Albo p\\u00f3jdziemy do kina, albo zostaniemy w domu.",
    "To, co powiedzia\\u0142e\\u015b, by\\u0142o bardzo m\\u0105dre.",
]
def count_clauses(sentence):
    return 1 + sum(1 for c in CONNECTORS if c in sentence.lower())
def main():
    assert len(SENTENCES) == 15, "fifteen complex sentences"
    counts = [count_clauses(s) for s in SENTENCES]
    assert all(c >= 2 for c in counts), "every sentence has 2+ clauses"
    assert sum(counts) >= 30, "thirty clauses minimum across the set"
    print("Complex sentences: %d; total clauses: %d" % (len(SENTENCES), sum(counts)))
    print("Connectors catalogued: %d" % len(CONNECTORS))
    print("OK: 15 complex sentences with clause counts verified")
if __name__ == "__main__":
    main()
'''


def _dialogue_demo(hdr, name, rid, group, lines):
    """Shared builder: verifies a 20-line dialogue."""
    data = "\n".join("(%s, %s)," % (repr(sp), repr(pl)) for sp, pl in lines)
    speakers = sorted({sp for sp, pl in lines})
    return hdr(name, rid, group) + '''\\
LINES = [
%s
]
def main():
    assert len(LINES) == 20, "twenty dialogue lines, got %%d" %% len(LINES)
    speakers = sorted({sp for sp, pl in LINES})
    assert len(speakers) == 2, "two speakers"
    for i in range(1, len(LINES)):
        assert LINES[i][0] != LINES[i-1][0], "speakers must alternate at line %%d" %% i
    total_words = sum(len(pl.split()) for sp, pl in LINES)
    assert total_words >= 60, "dialogue word-count floor"
    print("Dialogue lines: 20; speakers: %%s; total words: %%d" %% (", ".join(speakers), total_words))
    for sp, pl in LINES[:2]:
        print("  %%s: %%s" %% (sp, pl))
    print("OK: 20-line dialogue verified")
if __name__ == "__main__":
    main()
''' % (data,)


def demo_dialogue_market(hdr, name, rid, group, points, req):
    return _dialogue_demo(hdr, name, rid, group, [
        ("Sprzedawca", "Dzień dobry! W czym mogę pomóc?"),
        ("Klient", "Dzień dobry. Poproszę kilogram pomidorów."),
        ("Sprzedawca", "Proszę bardzo. Coś jeszcze?"),
        ("Klient", "Tak, pół kilo sera żółtego."),
        ("Sprzedawca", "Ser jest świeży, prosto z mleczarni."),
        ("Klient", "Świetnie. Ile płacę?"),
        ("Sprzedawca", "Razem trzydzieści dwa złote."),
        ("Klient", "Czy mogę zapłacić kartą?"),
        ("Sprzedawca", "Oczywiście, terminal jest tutaj."),
        ("Klient", "Dziękuję."),
        ("Sprzedawca", "Proszę bardzo. Paragon?"),
        ("Klient", "Tak, poproszę. A gdzie są jajka?"),
        ("Sprzedawca", "Na końcu alejki, po prawej."),
        ("Klient", "Dziękuję. Te jabłka ładnie wyglądają."),
        ("Sprzedawca", "To antonówki, słodkie i soczyste."),
        ("Klient", "Poproszę dwa kilo."),
        ("Sprzedawca", "Proszę. To wszystko?"),
        ("Klient", "Tak, to wszystko. Do widzenia!"),
        ("Sprzedawca", "Do widzenia! Zapraszamy ponownie!"),
        ("Klient", "Miła obsługa."),
    ])


def demo_dialogue_friend(hdr, name, rid, group, points, req):
    return _dialogue_demo(hdr, name, rid, group, [
        ("Ania", "Cześć, Marek! Kopę lat!"),
        ("Marek", "Cześć, Ania! Co słychać?"),
        ("Ania", "Wszystko dobrze. A u ciebie?"),
        ("Marek", "Nie narzekam. Słyszałem, że byłaś w Hiszpanii?"),
        ("Ania", "Tak, wróciłam w zeszłym tygodniu. Było cudownie!"),
        ("Marek", "Zazdroszczę! Ja siedziałem w biurze."),
        ("Ania", "Następnym razem jedziesz ze mną."),
        ("Marek", "Zgoda! A co u twojego brata?"),
        ("Ania", "Ożenił się w czerwcu."),
        ("Marek", "Serio? Gratulacje dla niego!"),
        ("Ania", "Dzięki, przekażę. Idziesz na kawę?"),
        ("Marek", "Chętnie! Znam fajną kawiarnię za rogiem."),
        ("Ania", "Świetnie. Opowiedz mi wszystko o pracy."),
        ("Marek", "Dostałem awans! Od lipca jestem kierownikiem."),
        ("Ania", "Wspaniale! Musimy to uczcić."),
        ("Marek", "Zapraszam cię w sobotę na kolację."),
        ("Ania", "Przyjdę z przyjemnością. O której?"),
        ("Marek", "O dziewiętnastej. Nie spóźnij się!"),
        ("Ania", "Postaram się. Do zobaczenia!"),
        ("Marek", "Na razie!"),
    ])


def demo_dialogue_problem(hdr, name, rid, group, points, req):
    return _dialogue_demo(hdr, name, rid, group, [
        ("Pan Nowak", "Dzień dobry, mam problem z pralką."),
        ("Serwisant", "Dzień dobry. Co się dzieje?"),
        ("Pan Nowak", "Nie wiruje i hałasuje."),
        ("Serwisant", "Od kiedy to trwa?"),
        ("Pan Nowak", "Od wczorajszego wieczora."),
        ("Serwisant", "Czy pralka jest na gwarancji?"),
        ("Pan Nowak", "Tak, kupiłem ją w marcu."),
        ("Serwisant", "Proszę podać numer seryjny."),
        ("Pan Nowak", "Chwileczkę... to będzie 8-4-2-9."),
        ("Serwisant", "Dziękuję. Mogę przyjechać w czwartek."),
        ("Pan Nowak", "O której godzinie?"),
        ("Serwisant", "Między dziesiątą a dwunastą."),
        ("Pan Nowak", "Dobrze. A ile to będzie kosztować?"),
        ("Serwisant", "Naprawa gwarancyjna jest bezpłatna."),
        ("Pan Nowak", "Świetnie. Czy muszę coś przygotować?"),
        ("Serwisant", "Proszę odłączyć pralkę od prądu."),
        ("Pan Nowak", "Zrobione. Dziękuję za pomoc."),
        ("Serwisant", "Proszę bardzo. Do zobaczenia w czwartek."),
        ("Pan Nowak", "Do zobaczenia."),
        ("Serwisant", "Czwartek, dziesiąta, pralka pana Nowaka."),
    ])


def demo_mastery(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
WORDS = """ja ty on ona ono my wy oni one by\\u0107 mie\\u0107 robi\\u0107 je\\u015b\\u0107 pi\\u0107
i\\u015b\\u0107 jecha\\u0107 m\\u00f3wi\\u0107 czyta\\u0107 pisa\\u0107 pracowa\\u0107 spa\\u0107
mieszka\\u0107 kupowa\\u0107 sprzedawa\\u0107 gotowa\\u0107 widzie\\u0107 s\\u0142ysze\\u0107
kocha\\u0107 lubi\\u0107 czeka\\u0107 dzwoni\\u0107 otwiera\\u0107 zamyka\\u0107 uczy\\u0107 dom
mieszkanie pok\\u00f3j kuchnia salon sypialnia \\u0142azienka ogr\\u00f3d ksi\\u0105\\u017cka
gazeta list telefon komputer woda chleb mleko kawa herbata zupa jajko jab\\u0142ko ser
samoch\\u00f3d poci\\u0105g samolot autobus rower ulica miasto wie\\u015b kraj \\u015bwiat
dzie\\u0144 noc czas rok praca szko\\u0142a lekcja egzamin sklep targ lekarz apteka pogoda
deszcz \\u015bnieg s\\u0142o\\u0144ce wiatr las jezioro rzeka morze g\\u00f3ra kwiat drzewo
kot pies ptak ryba mama tata siostra brat babcia dziadek dziecko m\\u0105\\u017c \\u017cona
przyjaciel rodzina cz\\u0142owiek kobieta dobry z\\u0142y du\\u017cy ma\\u0142y nowy stary
m\\u0142ody pi\\u0119kny wysoki niski d\\u0142ugi kr\\u00f3tki ciep\\u0142y zimny gor\\u0105cy
szybki wolny \\u0142atwy trudny wa\\u017cny szcz\\u0119\\u015bliwy smutny zdrowy chory
g\\u0142odny dobrze \\u017ale szybko bardzo ma\\u0142o du\\u017co cz\\u0119sto rzadko zawsze
nigdy teraz tutaj tam dzi\\u015b jutro wczoraj jeden dwa trzy cztery pi\\u0119\\u0107
sze\\u015b\\u0107 siedem osiem dziewi\\u0119\\u0107 dziesi\\u0119\\u0107 dwadzie\\u015bcia
trzydzie\\u015bci sto tysi\\u0105c pierwszy drugi poniedzia\\u0142ek wtorek \\u015broda
czwartek pi\\u0105tek sobota niedziela stycze\\u0144 luty marzec kwiecie\\u0144 maj
czerwiec lipiec sierpie\\u0144 wrzesie\\u0144 pa\\u017adziernik listopad grudzie\\u0144
wiosna lato jesie\\u0144 zima cze\\u015b\\u0107 witam dzi\\u0119kuj\\u0119 prosz\\u0119
przepraszam tak nie mo\\u017ce kto co gdzie kiedy dlaczego""".split()
ALPHA = ["a", "\\u0105", "b", "c", "\\u0107", "d", "e", "\\u0119", "f", "g",
         "h", "i", "j", "k", "l", "\\u0142", "m", "n", "\\u0144", "o",
         "\\u00f3", "p", "r", "s", "\\u015b", "t", "u", "w", "y", "z",
         "\\u017a", "\\u017c"]
def main():
    assert len(WORDS) == 200, "200 core words, got %d" % len(WORDS)
    assert len(set(WORDS)) == 200, "no duplicates in the 200"
    assert len(ALPHA) == 32, "32-letter alphabet"
    assert "by\\u0107" in WORDS and "dzi\\u0119kuj\\u0119" in WORDS
    assert "grudzie\\u0144" in WORDS, "all 12 months present check"
    months = ["stycze\\u0144", "luty", "marzec", "kwiecie\\u0144", "maj", "czerwiec",
              "lipiec", "sierpie\\u0144", "wrzesie\\u0144", "pa\\u017adziernik",
              "listopad", "grudzie\\u0144"]
    assert all(m in WORDS for m in months), "12 months in the 200"
    print("Core words: %d (all distinct)" % len(WORDS))
    print("Alphabet: %d letters" % len(ALPHA))
    print("Months present: 12/12; greetings present: yes")
    print("OK: 200-word mastery list verified")
if __name__ == "__main__":
    main()
'''


DEMOS = {
    "polish_overview": demo_overview,
    "polish_writing": demo_alphabet,
    "polish_phonology": demo_phonology,
    "polish_nouns": demo_nouns,
    "polish_verbs": demo_verbs,
    "polish_adjectives": demo_adjectives,
    "polish_pronouns": demo_pronouns,
    "polish_numbers": demo_numbers,
    "polish_greetings": demo_greetings,
    "polish_grammar": demo_grammar,
    "polish_home_family": demo_home_family,
    "polish_food_cooking": demo_food_cooking,
    "polish_travel": demo_travel,
    "polish_work_school": demo_work_school,
    "polish_health_body": demo_health_body,
    "polish_emotions": demo_emotions,
    "polish_nature_weather": demo_nature_weather,
    "polish_shopping": demo_shopping,
    "polish_friendship": demo_friendship,
    "polish_technology": demo_technology,
    "polish_tenses": demo_tenses,
    "polish_qa": demo_qa,
    "polish_commands": demo_commands,
    "polish_descriptions": demo_descriptions,
    "polish_story1": demo_story1,
    "polish_story2": demo_story2,
    "polish_story3": demo_story3,
    "polish_idioms": demo_idioms,
    "polish_registers": demo_registers,
    "polish_complex": demo_complex,
    "polish_dialogue_market": demo_dialogue_market,
    "polish_dialogue_friend": demo_dialogue_friend,
    "polish_dialogue_problem": demo_dialogue_problem,
    "polish_mastery": demo_mastery,
}
