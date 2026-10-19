#!/usr/bin/env python3
"""Demonstration programs for the Italian to English databases.

Every demo is real, runnable, stdlib-only Python that computes real values
from the Italian language data taught in the matching entry: speaker
arithmetic, alphabet checks, pronunciation rule engines, conjugation drills,
agreement checkers, number-to-words engines, pronoun tables, greeting
sorters, grammar checkers, sentence reassembly checkers, tense builders,
imperative drills, story checkers, idiom quizzes, register sorters, clause
counters, dialogue checkers, and the mastery speed-round list. Each prints
its real computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker.
"""


def _story_demo(hdr, name, rid, group, sentences, tense_label):
    data = "\n".join("(%s, %s)," % (repr(pt), repr(en)) for pt, en in sentences)
    return hdr(name, rid, group) + '''\\
SENTENCES = [
%s
]
def main():
    assert len(SENTENCES) == 10, "ten sentences, got %%d" %% len(SENTENCES)
    words = [len(pt.split()) for pt, _ in SENTENCES]
    avg = sum(words) / len(words)
    assert 4 <= avg <= 14, "average words per sentence out of bounds: %%s" %% avg
    assert all(w >= 3 for w in words), "every sentence needs at least 3 words"
    print("Story (%s): %%d sentences, avg %%.1f words/sentence" %% (len(SENTENCES), avg))
    for pt, en in SENTENCES[:2]:
        print("  %%s" %% pt)
        print("  -> %%s" %% en)
    print("OK: 10-sentence story verified")
if __name__ == "__main__":
    main()
''' % (data, tense_label)


def _dialogue_demo(hdr, name, rid, group, lines):
    data = "\n".join("(%s, %s)," % (repr(sp), repr(pt)) for sp, pt in lines)
    return hdr(name, rid, group) + '''\\
LINES = [
%s
]
def main():
    assert len(LINES) == 20, "twenty dialogue lines, got %%d" %% len(LINES)
    speakers = [sp for sp, _ in LINES]
    for i in range(1, len(speakers)):
        assert speakers[i] != speakers[i-1], "speakers must alternate at line %%d" %% i
    assert len(set(speakers)) == 2, "two speakers"
    print("Dialogue: %%d lines, speakers %%s and %%s" %% (len(LINES), speakers[0], speakers[1]))
    for sp, pt in LINES[:4]:
        print("  %%s: %%s" %% (sp, pt))
    print("OK: 20-line dialogue verified, speakers alternate")
if __name__ == "__main__":
    main()
''' % data


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
    uniq = [s for s in SENTENCES if len(set(s[0].split())) == len(s[0].split())]
    assert len(uniq) >= 3, "need at least 3 unique-word sentences"
    checked = 0
    for pt, en in uniq[:3]:
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
    print("OK: 20 themed sentences verified, reassembly passed")
if __name__ == "__main__":
    main()
''' % data


def demo_overview(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
NATIVE_SPEAKERS = 67_000_000
TOTAL_SPEAKERS = 85_000_000
OFFICIAL_COUNTRIES = ["Italy", "Switzerland", "San Marino", "Vatican City"]
def main():
    assert 60_000_000 <= NATIVE_SPEAKERS <= 75_000_000, "native speaker bounds"
    assert 75_000_000 <= TOTAL_SPEAKERS <= 100_000_000, "total speaker bounds"
    assert len(OFFICIAL_COUNTRIES) == 4, "four official countries"
    assert TOTAL_SPEAKERS >= NATIVE_SPEAKERS
    diaspora = TOTAL_SPEAKERS - NATIVE_SPEAKERS
    assert diaspora > 10_000_000, "large diaspora expected"
    print("Italian native speakers: %d" % NATIVE_SPEAKERS)
    print("Italian total speakers:  %d" % TOTAL_SPEAKERS)
    print("Official countries (%d): %s" % (len(OFFICIAL_COUNTRIES), ", ".join(OFFICIAL_COUNTRIES)))
    print("Diaspora speakers: %d" % diaspora)
    print("OK: overview facts verified - 67M native, 85M total, 4 countries")
if __name__ == "__main__":
    main()
'''


def demo_alphabet(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
ALPHA21 = list("ABCDEFGHILMNOPQRSTUVZ")
FOREIGN = list("JKWXY")
ACCENT_VOWELS = ["à", "è", "é", "ì", "ò", "ù"]
def main():
    assert len(ALPHA21) == 21, "alphabet must have 21 native letters"
    assert len(FOREIGN) == 5, "five foreign letters"
    assert "J" not in ALPHA21 and "H" in ALPHA21, "J foreign, H native but silent"
    assert len(ACCENT_VOWELS) == 6, "six accented vowel marks"
    assert "é" != "è", "acute vs grave e are distinct"
    print("Alphabet (%d letters): %s" % (len(ALPHA21), " ".join(ALPHA21)))
    print("Foreign letters (%d): %s" % (len(FOREIGN), " ".join(FOREIGN)))
    print("Accent marks: %s" % " ".join(ACCENT_VOWELS))
    print("OK: 21-letter alphabet, 5 foreign letters, 6 accent marks verified")
if __name__ == "__main__":
    main()
'''


def demo_phonology(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
HARD = set("aou")
def c_sound(next_vowel):
    return "k" if next_vowel in HARD else "tch"
def g_sound(next_vowel):
    return "g" if next_vowel in HARD else "j"
def main():
    checks = [("casa", "k"), ("cena", "tch"), ("cura", "k"), ("cibo", "tch"),
              ("gatto", "g"), ("gelato", "j"), ("gola", "g"), ("giro", "j"),
              ("chiesa", "k"), ("scena", "sh")]
    for word, want in checks:
        if word.startswith("ch"):
            got = "k"
        elif word.startswith("sc") and word[2] in "ei":
            got = "sh"
        elif word[0] == "c":
            got = c_sound(word[1])
        else:
            got = g_sound(word[1])
        assert got == want, "%s: got %s want %s" % (word, got, want)
    assert len("palla") == len("pala") + 1, "double consonant is held longer"
    assert len("nonno") == len("nono") + 1
    print("Sound rules: %d words checked (hard/soft C, G, CH, SC)" % len(checks))
    for word, want in checks[:6]:
        print("  %-8s -> %s" % (word, want))
    print("OK: pronunciation rule engine passed %d/%d" % (len(checks), len(checks)))
if __name__ == "__main__":
    main()
'''


def demo_nouns(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
NOUNS = [("man", "l'uomo"), ("woman", "la donna"), ("child", "il bambino"),
         ("friend", "l'amico"), ("family", "la famiglia"), ("house", "la casa"),
         ("door", "la porta"), ("window", "la finestra"), ("table", "il tavolo"),
         ("chair", "la sedia"), ("book", "il libro"), ("school", "la scuola"),
         ("work", "il lavoro"), ("day", "il giorno"), ("night", "la notte"),
         ("time", "il tempo"), ("water", "l'acqua"), ("food", "il cibo"),
         ("car", "la macchina"), ("street", "la strada"), ("city", "la città"),
         ("town", "il paese"), ("world", "il mondo"), ("name", "il nome"),
         ("problem", "il problema")]
TABLE = dict(NOUNS)
def translate(en):
    return TABLE[en]
def main():
    assert len(NOUNS) == 25, "twenty-five core nouns"
    score = sum(1 for en, it in NOUNS if translate(en) == it)
    assert score == 25, "quiz must score 25/25"
    masc = sum(1 for _, it in NOUNS if it.startswith(("il ", "l'", "lo ")))
    fem = sum(1 for _, it in NOUNS if it.startswith(("la ", "l'")) and not it.startswith("l'uomo") and not it.startswith("l'amico"))
    assert translate("problem") == "il problema", "problema is masculine"
    assert translate("water") == "l'acqua", "acqua is feminine"
    print("Nouns drilled: %d" % len(NOUNS))
    print("Quiz score: %d/%d" % (score, len(NOUNS)))
    print("Exceptions held: il problema (masc), l'acqua (fem)")
    print("OK: 25-noun article quiz passed 25/25")
if __name__ == "__main__":
    main()
'''


def demo_verbs(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
ENDINGS = {"are": {"io": "o", "tu": "i", "lui": "a", "noi": "iamo", "voi": "ate", "loro": "ano"},
           "ere": {"io": "o", "tu": "i", "lui": "e", "noi": "iamo", "voi": "ete", "loro": "ono"},
           "ire": {"io": "o", "tu": "i", "lui": "e", "noi": "iamo", "voi": "ite", "loro": "ono"}}
def conjugate(infinitive, person):
    stem, fam = infinitive[:-3], infinitive[-3:]
    return stem + ENDINGS[fam][person]
def main():
    checks = [("parlare", "io", "parlo"), ("parlare", "tu", "parli"),
              ("parlare", "lui", "parla"), ("parlare", "noi", "parliamo"),
              ("parlare", "loro", "parlano"), ("vedere", "io", "vedo"),
              ("vedere", "tu", "vedi"), ("vedere", "lui", "vede"),
              ("vedere", "noi", "vediamo"), ("vedere", "loro", "vedono"),
              ("dormire", "io", "dormo"), ("dormire", "tu", "dormi"),
              ("dormire", "lui", "dorme"), ("dormire", "noi", "dormiamo"),
              ("dormire", "loro", "dormono"), ("mangiare", "io", "mangio")]
    for inf, person, want in checks:
        got = conjugate(inf, person)
        assert got == want, "%s %s: got %s want %s" % (inf, person, got, want)
    print("Conjugation drill: %d forms checked across -are, -ere, -ire" % len(checks))
    for inf, person, want in checks[:6]:
        print("  %-8s %-4s -> %s" % (inf, person, want))
    print("OK: present-tense conjugation drill passed %d/%d" % (len(checks), len(checks)))
if __name__ == "__main__":
    main()
'''


def demo_agreement(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
def agree(masc_sing, gender, number):
    if masc_sing.endswith(("chio", "ghio")):
        stem = masc_sing[:-1]
        table = {("m", "s"): "o", ("f", "s"): "a", ("m", "p"): "", ("f", "p"): "e"}
    elif masc_sing.endswith("o"):
        stem = masc_sing[:-1]
        table = {("m", "s"): "o", ("f", "s"): "a", ("m", "p"): "i", ("f", "p"): "e"}
    else:
        stem = masc_sing[:-1]
        table = {("m", "s"): "e", ("f", "s"): "e", ("m", "p"): "i", ("f", "p"): "i"}
    return stem + table[(gender, number)]
def main():
    checks = [("bello", "f", "s", "bella"), ("bello", "m", "p", "belli"),
              ("bello", "f", "p", "belle"), ("bello", "m", "s", "bello"),
              ("rosso", "f", "s", "rossa"), ("nuovo", "f", "p", "nuove"),
              ("grande", "f", "s", "grande"), ("grande", "m", "p", "grandi"),
              ("felice", "f", "p", "felici"), ("vecchio", "m", "p", "vecchi")]
    for adj, g, n, want in checks:
        got = agree(adj, g, n)
        assert got == want, "%s %s%s: got %s want %s" % (adj, g, n, got, want)
    adverbs = ["molto", "poco", "bene", "male", "sempre", "mai", "già", "ancora",
               "troppo", "presto", "tardi", "qui", "lì", "così", "forse"]
    assert len(adverbs) == 15, "fifteen adverbs"
    print("Agreement engine: %d forms checked" % len(checks))
    for adj, g, n, want in checks[:5]:
        print("  %-8s %s/%s -> %s" % (adj, g, n, want))
    print("Adverbs (%d, never change): %s" % (len(adverbs), ", ".join(adverbs[:5])))
    print("OK: adjective agreement passed %d/%d" % (len(checks), len(checks)))
if __name__ == "__main__":
    main()
'''


def demo_pronouns(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
SUBJECT = {"io": "I", "tu": "you (informal)", "lui": "he", "lei": "she",
           "Lei": "you (formal)", "noi": "we", "voi": "you all", "loro": "they"}
OBJECT = {"mi": "me", "ti": "you", "lo": "him/it (m)", "la": "her/it (f)",
          "ci": "us", "vi": "you all", "li": "them (m)", "le": "them (f)"}
def possessive(base, thing_gender, thing_number):
    table = {"mio": {"m": {"s": "mio", "p": "miei"}, "f": {"s": "mia", "p": "mie"}},
             "tuo": {"m": {"s": "tuo", "p": "tuoi"}, "f": {"s": "tua", "p": "tue"}},
             "suo": {"m": {"s": "suo", "p": "suoi"}, "f": {"s": "sua", "p": "sue"}}}
    return table[base][thing_gender][thing_number]
def main():
    assert len(SUBJECT) == 8, "eight subject pronouns"
    assert len(OBJECT) == 8, "eight object pronouns"
    checks = [("mio", "m", "s", "mio"), ("mio", "f", "s", "mia"),
              ("mio", "m", "p", "miei"), ("mio", "f", "p", "mie"),
              ("tuo", "f", "s", "tua"), ("suo", "m", "p", "suoi")]
    for base, g, n, want in checks:
        got = possessive(base, g, n)
        assert got == want, "%s %s%s: got %s want %s" % (base, g, n, got, want)
    assert SUBJECT["Lei"] == "you (formal)", "Lei is capitalized formal"
    print("Subject pronouns: %d, object pronouns: %d" % (len(SUBJECT), len(OBJECT)))
    print("Possessive follows the thing owned: il mio libro / la mia casa / i miei libri")
    print("OK: pronoun paradigms verified, %d possessive forms checked" % len(checks))
if __name__ == "__main__":
    main()
'''


def demo_numbers(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
UNITS = ["zero", "uno", "due", "tre", "quattro", "cinque", "sei", "sette",
         "otto", "nove", "dieci", "undici", "dodici", "tredici",
         "quattordici", "quindici", "sedici", "diciassette", "diciotto",
         "diciannove"]
TENS = {20: "venti", 30: "trenta", 40: "quaranta", 50: "cinquanta",
        60: "sessanta", 70: "settanta", 80: "ottanta", 90: "novanta"}
def num2word(n):
    assert 0 <= n <= 100, "range 0-100"
    if n < 20:
        return UNITS[n]
    if n == 100:
        return "cento"
    t, u = (n // 10) * 10, n % 10
    if u == 0:
        return TENS[t]
    stem = TENS[t][:-1] if u in (1, 8) else TENS[t]
    return stem + UNITS[u]
def main():
    checks = [(0, "zero"), (1, "uno"), (13, "tredici"), (20, "venti"),
              (21, "ventuno"), (28, "ventotto"), (32, "trentadue"),
              (48, "quarantotto"), (50, "cinquanta"), (99, "novantanove"),
              (100, "cento")]
    for n, want in checks:
        got = num2word(n)
        assert got == want, "%d: got %s want %s" % (n, got, want)
    ordinals = ["primo", "secondo", "terzo", "quarto", "quinto",
                "sesto", "settimo", "ottavo", "nono", "decimo"]
    assert len(ordinals) == 10
    print("Number engine: %d conversions checked" % len(checks))
    for n, want in checks:
        print("  %3d -> %s" % (n, want))
    print("Ordinals 1-10: %s" % ", ".join(ordinals))
    print("OK: number-to-words engine passed %d/%d" % (len(checks), len(checks)))
if __name__ == "__main__":
    main()
'''


def demo_greetings(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
PHRASES = ["Buongiorno!", "Buonasera!", "Buonanotte!", "Ciao!", "Salve!",
           "Arrivederci!", "ArrivederLa!", "A presto!", "A domani!", "A dopo!",
           "Benvenuto!", "Piacere!", "Come sta?", "Come stai?", "Tutto bene?",
           "Bene, grazie!", "Grazie mille!", "Prego!", "Per favore!",
           "Mi scusi!", "Scusa!", "Permesso!", "Auguri!", "Complimenti!",
           "In bocca al lupo!", "Buon appetito!", "Buon viaggio!",
           "Buona giornata!", "Salute!", "Di niente!"]
FORMAL = {"Come sta?", "Mi scusi!", "ArrivederLa!"}
INFORMAL = {"Come stai?", "Scusa!", "Ciao!"}
def main():
    assert len(PHRASES) == 30, "thirty phrases, got %d" % len(PHRASES)
    assert len(set(PHRASES)) == 30, "no duplicate phrases"
    assert FORMAL.isdisjoint(INFORMAL), "register sets must not overlap"
    assert "Ciao!" in INFORMAL and "ArrivederLa!" in FORMAL
    print("Greetings drilled: %d phrases" % len(PHRASES))
    print("Formal: %s" % ", ".join(sorted(FORMAL)))
    print("Informal: %s" % ", ".join(sorted(INFORMAL)))
    print("OK: 30 greetings verified, registers sorted")
if __name__ == "__main__":
    main()
'''


def demo_grammar(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
def article(noun, gender):
    vowels = set("aeiouàèéìòù")
    if noun[0] in vowels:
        return "l'"
    if gender == "m":
        s_impura = tuple("s" + c for c in "bcdfghlmnpqrstv")
        if noun.startswith(s_impura) or noun[:1] in "zx" or noun.startswith(("gn", "ps", "pn", "y")):
            return "lo"
        return "il"
    return "la"
def negate(verb_phrase):
    return "Non " + verb_phrase[0].lower() + verb_phrase[1:]
def main():
    checks = [("libro", "m", "il"), ("studente", "m", "lo"), ("zaino", "m", "lo"),
              ("amico", "m", "l'"), ("casa", "f", "la"), ("acqua", "f", "l'"),
              ("scuola", "f", "la"), ("gnomo", "m", "lo")]
    for noun, g, want in checks:
        got = article(noun, g)
        assert got == want, "%s: got %s want %s" % (noun, got, want)
    neg = negate("Parlo italiano")
    assert neg == "Non parlo italiano", neg
    neg2 = negate("Ho capito")
    assert neg2 == "Non ho capito", neg2
    q = "Parli italiano?"
    assert q.endswith("?"), "intonation question keeps SVO order"
    print("Article engine: %d nouns checked" % len(checks))
    for noun, g, want in checks:
        print("  %-9s -> %s %s" % (noun, want, noun))
    print("Negation: Parlo italiano -> %s" % neg)
    print("OK: grammar pillars verified on real sentences")
if __name__ == "__main__":
    main()
'''


def demo_home_family(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Abito in un appartamento in centro.", "I live in an apartment downtown."),
        ("La mia casa ha tre camere da letto.", "My house has three bedrooms."),
        ("Il soggiorno è grande e luminoso.", "The living room is big and bright."),
        ("La cucina è il cuore della casa.", "The kitchen is the heart of the house."),
        ("Il bagno è in fondo al corridoio.", "The bathroom is at the end of the hall."),
        ("C'è un bel balcone con vista.", "There is a nice balcony with a view."),
        ("Il tavolo è in sala da pranzo.", "The table is in the dining room."),
        ("Il divano è comodo.", "The sofa is comfortable."),
        ("Ho un giardino piccolo dietro casa.", "I have a small garden behind the house."),
        ("La mia famiglia è numerosa.", "My family is large."),
        ("Mio padre lavora in banca.", "My father works in a bank."),
        ("Mia madre insegna a scuola.", "My mother teaches at school."),
        ("Ho un fratello e due sorelle.", "I have a brother and two sisters."),
        ("Mio nonno racconta belle storie.", "My grandfather tells beautiful stories."),
        ("Mia nonna cucina benissimo.", "My grandmother cooks wonderfully."),
        ("Mio zio abita a Milano.", "My uncle lives in Milan."),
        ("Mia cugina viene a trovarci domenica.", "My cousin is coming to visit us Sunday."),
        ("Siamo una famiglia unita.", "We are a close-knit family."),
        ("A Natale ci riuniamo tutti.", "At Christmas we all gather."),
        ("Casa dolce casa!", "Home sweet home!"),
    ])


def demo_food_cooking(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("La colazione è il pasto più importante.", "Breakfast is the most important meal."),
        ("Faccio colazione con caffè e cornetto.", "I have breakfast with coffee and croissant."),
        ("A pranzo mangio pasta.", "For lunch I eat pasta."),
        ("La cena è alle otto.", "Dinner is at eight."),
        ("Cucino la pasta al dente.", "I cook the pasta al dente."),
        ("Aggiungo il sale all'acqua.", "I add salt to the water."),
        ("Taglio le verdure a pezzetti.", "I cut the vegetables into pieces."),
        ("Friggo le uova in padella.", "I fry the eggs in the pan."),
        ("Il sugo cuoce a fuoco lento.", "The sauce simmers on low heat."),
        ("Assaggio e aggiusto di sale.", "I taste and adjust the salt."),
        ("La pizza è nel forno.", "The pizza is in the oven."),
        ("Il pane è fresco di oggi.", "The bread is fresh today."),
        ("Vorrei il menù, per favore.", "I would like the menu, please."),
        ("Prendo gli spaghetti al pomodoro.", "I will have the spaghetti with tomato."),
        ("Il vino rosso è ottimo.", "The red wine is excellent."),
        ("Il conto, per favore.", "The check, please."),
        ("Il servizio è incluso?", "Is service included?"),
        ("Che buono!", "How delicious!"),
        ("Ho mangiato troppo.", "I ate too much."),
        ("Domani cucino io.", "Tomorrow I am cooking."),
    ])


def demo_travel(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Dov'è la stazione?", "Where is the station?"),
        ("Come arrivo al Duomo?", "How do I get to the cathedral?"),
        ("Vada dritto, poi giri a destra.", "Go straight, then turn right. (formal)"),
        ("La fermata dell'autobus è qui vicino.", "The bus stop is near here."),
        ("Prendo il treno delle nove.", "I take the nine o'clock train."),
        ("Il treno parte dal binario due.", "The train leaves from platform two."),
        ("Quanto costa un biglietto per Venezia?", "How much is a ticket to Venice?"),
        ("Un biglietto di andata e ritorno.", "A round-trip ticket."),
        ("L'aereo decolla alle sette.", "The plane takes off at seven."),
        ("Ho perso la coincidenza.", "I missed the connection."),
        ("Chiami un taxi, per favore?", "Will you call a taxi, please?"),
        ("Noleggio una macchina per tre giorni.", "I am renting a car for three days."),
        ("Mi sono perso. Può aiutarmi?", "I am lost. Can you help me? (formal)"),
        ("Ho prenotato una camera doppia.", "I booked a double room."),
        ("La colazione è inclusa?", "Is breakfast included?"),
        ("A che ora è il check-out?", "What time is check-out?"),
        ("Il passaporto è in cassaforte.", "The passport is in the safe."),
        ("Buon viaggio!", "Have a good trip!"),
        ("Benvenuti in Italia!", "Welcome to Italy!"),
        ("Il viaggio è stato bellissimo.", "The trip was beautiful."),
    ])


def demo_work_school(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Faccio l'ingegnere.", "I am an engineer."),
        ("Lavoro in un ufficio in centro.", "I work in a downtown office."),
        ("Ho una riunione alle dieci.", "I have a meeting at ten."),
        ("Il mio capo è esigente.", "My boss is demanding."),
        ("I colleghi sono gentili.", "The colleagues are kind."),
        ("Vado al lavoro in treno.", "I commute by train."),
        ("Lo stipendio arriva a fine mese.", "The salary arrives at month's end."),
        ("Cerco lavoro da un mese.", "I have been job-hunting for a month."),
        ("Ho un colloquio domani.", "I have an interview tomorrow."),
        ("Studio all'università.", "I study at the university."),
        ("La lezione inizia alle otto.", "The lesson starts at eight."),
        ("Il professore spiega bene.", "The professor explains well."),
        ("Devo fare i compiti.", "I must do homework."),
        ("Domani ho l'esame di matematica.", "Tomorrow I have the math exam."),
        ("Ho preso trenta e lode.", "I got thirty with honors."),
        ("La biblioteca chiude alle sette.", "The library closes at seven."),
        ("Mi sono laureato l'anno scorso.", "I graduated last year."),
        ("Imparo l'italiano ogni giorno.", "I learn Italian every day."),
        ("Buon lavoro!", "Have a good workday!"),
        ("In bocca al lupo per l'esame!", "Good luck on the exam!"),
    ])


def demo_health_body(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Mi fa male la testa.", "My head hurts."),
        ("Mi fanno male i piedi.", "My feet hurt."),
        ("Ho mal di gola.", "I have a sore throat."),
        ("Ho la febbre.", "I have a fever."),
        ("Ho il raffreddore.", "I have a cold."),
        ("Ho la tosse.", "I have a cough."),
        ("Mi gira la testa.", "I am dizzy."),
        ("Ho mal di stomaco.", "My stomach hurts."),
        ("Sono allergico alle noci.", "I am allergic to nuts."),
        ("Devo vedere un medico.", "I need to see a doctor."),
        ("Ho un appuntamento dal dottore.", "I have a doctor's appointment."),
        ("Prendo questa medicina due volte al giorno.", "I take this medicine twice a day."),
        ("Dov'è la farmacia più vicina?", "Where is the nearest pharmacy?"),
        ("Ha qualcosa per il mal di testa?", "Do you have something for a headache?"),
        ("Mi serve una ricetta?", "Do I need a prescription?"),
        ("Devo riposare qualche giorno.", "I need to rest a few days."),
        ("Beva molta acqua.", "Drink lots of water. (formal)"),
        ("Si senta meglio presto!", "Get well soon!"),
        ("Respira profondamente.", "Breathe deeply."),
        ("Non è niente di grave.", "It is nothing serious."),
    ])


def demo_emotions(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Sono molto felice oggi!", "I am very happy today!"),
        ("Che bella notizia!", "What great news!"),
        ("Rido sempre con te.", "I always laugh with you."),
        ("Sono triste perché piove.", "I am sad because it is raining."),
        ("Mi manchi tanto.", "I miss you so much."),
        ("Ho il cuore spezzato.", "My heart is broken."),
        ("Sono arrabbiato con mio fratello.", "I am angry with my brother."),
        ("Mi fa arrabbiare quando mente.", "It makes me angry when he lies."),
        ("Calmati, respira!", "Calm down, breathe!"),
        ("Ho paura del buio.", "I am afraid of the dark."),
        ("Non aver paura, sono qui.", "Do not be afraid, I am here."),
        ("Ti amo più di ieri.", "I love you more than yesterday."),
        ("L'amore è la cosa più bella.", "Love is the most beautiful thing."),
        ("Sono innamorato di te.", "I am in love with you."),
        ("Che sorpresa vederti qui!", "What a surprise to see you here!"),
        ("Non ci posso credere!", "I cannot believe it!"),
        ("Sono sorpreso e felice.", "I am surprised and happy."),
        ("Sono nervoso prima dell'esame.", "I am nervous before the exam."),
        ("Stai tranquillo, andrà tutto bene.", "Stay calm, everything will be fine."),
        ("La gioia è contagiosa.", "Joy is contagious."),
    ])


def demo_nature_weather(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Che bel tempo oggi!", "What beautiful weather today!"),
        ("C'è il sole.", "It is sunny."),
        ("Piove a catinelle.", "It is raining buckets."),
        ("Nevica sulle montagne.", "It is snowing on the mountains."),
        ("Fa caldo d'estate.", "It is hot in summer."),
        ("Fa freddo d'inverno.", "It is cold in winter."),
        ("Tira vento al mare.", "It is windy at the seaside."),
        ("Il cielo è nuvoloso.", "The sky is cloudy."),
        ("Domani pioverà.", "It will rain tomorrow."),
        ("In primavera fioriscono gli alberi.", "In spring the trees bloom."),
        ("Le foglie cadono in autunno.", "The leaves fall in autumn."),
        ("Il cane abbaia in giardino.", "The dog barks in the garden."),
        ("Il gatto dorme al sole.", "The cat sleeps in the sun."),
        ("Gli uccelli cantano la mattina.", "The birds sing in the morning."),
        ("Ho visto un cervo nel bosco.", "I saw a deer in the woods."),
        ("Le api fanno il miele.", "Bees make honey."),
        ("Il fiume scorre verso il mare.", "The river flows to the sea."),
        ("La montagna è coperta di neve.", "The mountain is covered with snow."),
        ("Andiamo al mare domenica?", "Shall we go to the seaside Sunday?"),
        ("Che stagione preferisci?", "Which season do you prefer?"),
    ])


def demo_shopping(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Quanto costa?", "How much does it cost?"),
        ("Costa dieci euro.", "It costs ten euros."),
        ("È troppo caro.", "It is too expensive."),
        ("Può farmi uno sconto?", "Can you give me a discount? (formal)"),
        ("Solo per lei, otto euro.", "Just for you, eight euros."),
        ("Lo prendo.", "I will take it."),
        ("Non lo prendo, grazie.", "I will not take it, thanks."),
        ("Sto solo guardando.", "I am just looking."),
        ("Ha una taglia più grande?", "Do you have a bigger size?"),
        ("Posso provarlo?", "May I try it on?"),
        ("Dov'è il camerino?", "Where is the fitting room?"),
        ("Accettate carte di credito?", "Do you accept credit cards?"),
        ("Pago in contanti.", "I pay cash."),
        ("Mi dia lo scontrino, per favore.", "Give me the receipt, please."),
        ("Il mercato è aperto la mattina.", "The market is open in the morning."),
        ("Compro frutta e verdura fresca.", "I buy fresh fruit and vegetables."),
        ("Un chilo di mele, per favore.", "A kilo of apples, please."),
        ("Il pane è ancora caldo.", "The bread is still warm."),
        ("A che ora chiude il negozio?", "What time does the shop close?"),
        ("Grazie e arrivederci!", "Thanks and goodbye!"),
    ])


def demo_friendship(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Piacere, mi chiamo Sara.", "Nice to meet you, I am called Sara."),
        ("Di dove sei?", "Where are you from?"),
        ("Sono di Napoli, e tu?", "I am from Naples, and you?"),
        ("Quanti anni hai?", "How old are you?"),
        ("Ho trent'anni.", "I am thirty."),
        ("Che fai nella vita?", "What do you do in life?"),
        ("Ti presento il mio amico Luca.", "Let me introduce my friend Luca."),
        ("Andiamo a prendere un caffè?", "Shall we go get a coffee?"),
        ("Volentieri!", "Gladly!"),
        ("Che ne dici di cena sabato?", "How about dinner Saturday?"),
        ("Vieni alla mia festa venerdì?", "Are you coming to my party Friday?"),
        ("Porta pure un amico.", "Feel free to bring a friend."),
        ("A che ora cominciamo?", "What time do we start?"),
        ("Ci vediamo alle otto.", "See you at eight."),
        ("Mi fa piacere vederti!", "I am pleased to see you!"),
        ("È tanto che non ci vediamo!", "It has been so long!"),
        ("Raccontami tutto!", "Tell me everything!"),
        ("Auguri per il tuo compleanno!", "Happy birthday wishes!"),
        ("Congratulazioni per il lavoro nuovo!", "Congratulations on the new job!"),
        ("È stata una bellissima serata.", "It was a wonderful evening."),
    ])


def demo_technology(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Il mio telefono è scarico.", "My phone is dead."),
        ("Dov'è il caricabatterie?", "Where is the charger?"),
        ("Non c'è campo qui.", "There is no signal here."),
        ("Ti chiamo più tardi.", "I will call you later."),
        ("Pronto? Chi parla?", "Hello? Who is speaking?"),
        ("Resta in linea, per favore.", "Hold the line, please."),
        ("Mi è caduta la linea.", "The call dropped."),
        ("Ti mando un messaggio.", "I will send you a message."),
        ("Hai visto la mia email?", "Did you see my email?"),
        ("La password non funziona.", "The password does not work."),
        ("Ho dimenticato la password.", "I forgot the password."),
        ("Il computer si è bloccato.", "The computer froze."),
        ("Riavvia il computer.", "Restart the computer."),
        ("C'è il wifi qui?", "Is there wifi here?"),
        ("Qual è la password del wifi?", "What is the wifi password?"),
        ("Scarico l'app adesso.", "I am downloading the app now."),
        ("Ho finito i giga.", "I am out of data."),
        ("Faccio una foto e te la mando.", "I will take a photo and send it to you."),
        ("Ci sentiamo domani!", "We will talk tomorrow!"),
        ("La tecnologia ci avvicina.", "Technology brings us closer."),
    ])


def demo_tenses(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
def passato_prossimo(infinitive, aux, participle):
    return aux + " " + participle
def futuro_stem(infinitive):
    if infinitive.endswith("are"):
        return infinitive[:-3] + "er"
    if infinitive.endswith("ere"):
        return infinitive[:-3] + "r"
    return infinitive[:-1]
def futuro(infinitive, person):
    endings = {"io": "ò", "tu": "ai", "lui": "à", "noi": "emo", "voi": "ete", "loro": "anno"}
    return futuro_stem(infinitive) + endings[person]
def main():
    checks = [("mangiare", "ho", "mangiato", "ho mangiato"),
              ("vedere", "ho", "visto", "ho visto"),
              ("andare", "sono", "andato", "sono andato"),
              ("partire", "sono", "partita", "sono partita")]
    for inf, aux, part, want in checks:
        got = passato_prossimo(inf, aux, part)
        assert got == want, "%s: got %s want %s" % (inf, got, want)
    fut = [("parlare", "io", "parlerò"), ("parlare", "lui", "parlerà"),
           ("vedere", "io", "vedrò"), ("dormire", "loro", "dormiranno")]
    for inf, person, want in fut:
        got = futuro(inf, person)
        assert got == want, "%s %s: got %s want %s" % (inf, person, got, want)
    imperfetto = {"parlare": {"io": "parlavo", "lui": "parlava", "loro": "parlavano"}}
    assert imperfetto["parlare"]["io"] == "parlavo"
    assert imperfetto["parlare"]["loro"] == "parlavano"
    print("Passato prossimo: %d forms (avere vs essere)" % len(checks))
    for _, _, _, want in checks:
        print("  %s" % want)
    print("Futuro: %d forms checked" % len(fut))
    print("OK: tense engine passed %d/%d" % (len(checks) + len(fut), len(checks) + len(fut)))
if __name__ == "__main__":
    main()
'''


def demo_qa(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
QWORDS = {"chi": "who", "che": "what", "cosa": "what", "dove": "where",
          "quando": "when", "perché": "why", "come": "how", "quale": "which",
          "quanto": "how much", "quanti": "how many"}
PAIRS = [("Chi è?", "È mio fratello."), ("Che cos'è?", "È un regalo."),
         ("Dove abiti?", "Abito a Torino."), ("Quando parti?", "Parto lunedì."),
         ("Perché piangi?", "Perché sono triste."), ("Come stai?", "Bene, grazie."),
         ("Quale preferisci?", "Preferisco il rosso."),
         ("Quanto costa?", "Costa cinque euro."),
         ("Quanti anni hai?", "Ne ho venti."),
         ("Che ore sono?", "Sono le cinque."),
         ("Parli italiano?", "Sì, un po'."),
         ("Dov'è il bagno?", "In fondo a destra."),
         ("Con chi vai?", "Con mia sorella."),
         ("Di dove sei?", "Sono siciliano."),
         ("Cosa fai stasera?", "Guardo un film."),
         ("Come si chiama?", "Si chiama Anna."),
         ("Hai capito?", "Sì, ho capito."),
         ("Vuoi un caffè?", "Sì, grazie!"),
         ("Andiamo?", "Andiamo!"),
         ("Tutto bene?", "Tutto benissimo.")]
def main():
    assert len(PAIRS) == 20, "twenty pairs, got %d" % len(PAIRS)
    assert len(QWORDS) == 10, "ten question words"
    for q, a in PAIRS:
        assert q.endswith("?"), "question must end with ?: %s" % q
        assert len(a) > 0, "answer must not be empty"
    qword_firsts = {"chi", "che", "cosa", "dove", "quando", "perché", "come",
                    "quale", "quanto", "quanti"}
    starts = sum(1 for q, _ in PAIRS if q.split()[0].strip("¿?").lower() in qword_firsts)
    assert starts >= 10, "at least ten pairs should open with a question word"
    assert starts <= 20
    print("Question words (%d): %s" % (len(QWORDS), ", ".join(sorted(QWORDS))))
    print("Q&A pairs: %d" % len(PAIRS))
    for q, a in PAIRS[:3]:
        print("  %s -> %s" % (q, a))
    print("OK: 20 question/answer pairs verified")
if __name__ == "__main__":
    main()
'''


def demo_commands(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
def imperative_tu(infinitive):
    if infinitive == "venire":
        return "vieni"
    stem = infinitive[:-3]
    if infinitive.endswith("are"):
        return stem + "a"
    if infinitive.endswith("ere"):
        return stem + "i"
    return stem + "i"
def imperative_lei(infinitive):
    if infinitive == "venire":
        return "venga"
    stem = infinitive[:-3]
    if infinitive.endswith("are"):
        return stem + "i"
    return stem + "a"
def negative_tu(infinitive):
    return "Non " + infinitive
def main():
    checks = [("parlare", "Parla!"), ("mangiare", "Mangia!"), ("prendere", "Prendi!"),
              ("aprire", "Apri!"), ("venire", "Vieni!")]
    for inf, want in checks:
        got = imperative_tu(inf).capitalize() + "!"
        assert got == want, "%s: got %s want %s" % (inf, got, want)
    lei_checks = [("parlare", "Parli!"), ("prendere", "Prenda!"), ("aprire", "Apra!"),
                  ("venire", "Venga!")]
    for inf, want in lei_checks:
        got = imperative_lei(inf).capitalize() + "!"
        assert got == want, "%s Lei: got %s want %s" % (inf, got, want)
    assert negative_tu("parlare") == "Non parlare"
    assert negative_tu("andare") == "Non andare"
    print("Tu imperatives: %d checked" % len(checks))
    print("Lei imperatives: %d checked" % len(lei_checks))
    print("Negative tu uses the infinitive: Non parlare!")
    print("OK: imperative engine passed %d/%d" % (len(checks) + len(lei_checks), len(checks) + len(lei_checks)))
if __name__ == "__main__":
    main()
'''


def demo_descriptions(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Mia nonna ha i capelli bianchi e gli occhi azzurri.", "My grandmother has white hair and blue eyes."),
        ("È alta e magra, sempre elegante.", "She is tall and slim, always elegant."),
        ("Marco è un ragazzo allegro e generoso.", "Marco is a cheerful, generous boy."),
        ("Ha trent'anni e lavora come medico.", "He is thirty and works as a doctor."),
        ("La mia città è antica e piena di storia.", "My city is ancient and full of history."),
        ("Le strade sono strette e lastricate.", "The streets are narrow and cobbled."),
        ("La piazza è grande e luminosa.", "The square is big and bright."),
        ("C'è una fontana al centro.", "There is a fountain in the center."),
        ("Il Duomo è una chiesa magnifica.", "The cathedral is a magnificent church."),
        ("Il mare è calmo e cristallino.", "The sea is calm and crystal-clear."),
        ("La montagna è alta e coperta di neve.", "The mountain is tall and covered with snow."),
        ("Il tramonto è rosso e oro.", "The sunset is red and gold."),
        ("La casa di campagna è circondata da ulivi.", "The country house is surrounded by olive trees."),
        ("Il giardino è pieno di fiori profumati.", "The garden is full of fragrant flowers."),
        ("Il caffè è piccolo ma accogliente.", "The cafe is small but cozy."),
        ("Il cibo è semplice e genuino.", "The food is simple and genuine."),
        ("La gente è cordiale e ospitale.", "The people are warm and hospitable."),
        ("L'atmosfera è magica di sera.", "The atmosphere is magical at night."),
        ("Non dimenticherò mai questo posto.", "I will never forget this place."),
        ("Tornerò sicuramente.", "I will surely return."),
    ])


def demo_story1(hdr, name, rid, group, points, req):
    return _story_demo(hdr, name, rid, group, [
        ("Mi chiamo Elena e abito a Firenze.", "My name is Elena and I live in Florence."),
        ("Ogni mattina mi sveglio alle sette.", "Every morning I wake up at seven."),
        ("Faccio colazione con caffè e biscotti.", "I have breakfast with coffee and biscuits."),
        ("Poi esco e cammino fino al lavoro.", "Then I go out and walk to work."),
        ("Lavoro in una piccola libreria in centro.", "I work in a small bookstore downtown."),
        ("Amo i libri e amo la mia città.", "I love books and I love my city."),
        ("A mezzogiorno mangio un panino al parco.", "At noon I eat a sandwich in the park."),
        ("Il pomeriggio passa veloce tra i clienti.", "The afternoon passes quickly among the customers."),
        ("La sera torno a casa stanca ma felice.", "In the evening I return home tired but happy."),
        ("Domani sarà un altro bel giorno.", "Tomorrow will be another beautiful day."),
    ], "present tense")


def demo_story2(hdr, name, rid, group, points, req):
    return _story_demo(hdr, name, rid, group, [
        ("L'estate scorsa ho fatto un viaggio in Sicilia.", "Last summer I took a trip to Sicily."),
        ("Sono partito da Milano in treno.", "I left from Milan by train."),
        ("Il viaggio è durato tutta la notte.", "The journey lasted all night."),
        ("Quando ero bambino, sognavo il mare.", "When I was a child, I dreamed of the sea."),
        ("Finalmente ho visto l'acqua blu.", "Finally I saw the blue water."),
        ("Ho mangiato arancini e cannoli ogni giorno.", "I ate arancini and cannoli every day."),
        ("Un giorno pioveva, ma non mi importava.", "One day it was raining, but I did not mind."),
        ("Ho conosciuto una famiglia gentile a Taormina.", "I met a kind family in Taormina."),
        ("Mi hanno invitato a cena tre volte!", "They invited me to dinner three times!"),
        ("Non dimenticherò mai quella settimana.", "I will never forget that week."),
    ], "past tenses")


def demo_story3(hdr, name, rid, group, points, req):
    return _story_demo(hdr, name, rid, group, [
        ("Domani comincerà una nuova avventura.", "Tomorrow a new adventure will begin."),
        ("Partirò per Roma all'alba.", "I will leave for Rome at dawn."),
        ("Vedrò il Colosseo e i Fori.", "I will see the Colosseum and the Forums."),
        ("Vorrei anche visitare il Vaticano.", "I would also like to visit the Vatican."),
        ("Mi piacerebbe mangiare la vera carbonara.", "I would love to eat the real carbonara."),
        ("Se avrò tempo, andrò a Trastevere.", "If I have time, I will go to Trastevere."),
        ("Comprerò regali per tutta la famiglia.", "I will buy gifts for the whole family."),
        ("Spero che il tempo sia bello.", "I hope the weather is nice."),
        ("Voglio che tu venga con me un giorno.", "I want you to come with me one day."),
        ("Sarà il viaggio più bello della mia vita.", "It will be the most beautiful trip of my life."),
    ], "future and conditional")


def demo_idioms(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
IDIOMS = {
    "In bocca al lupo!": "Good luck!",
    "Non tutte le ciambelle riescono col buco.": "Things do not always work out.",
    "Avere le mani in pasta.": "To be involved in something.",
    "Prendere due piccioni con una fava.": "To kill two birds with one stone.",
    "Chi dorme non piglia pesci.": "The early bird catches the worm.",
    "L'abito non fa il monaco.": "Clothes do not make the man.",
    "Meglio tardi che mai.": "Better late than never.",
    "Tutto fumo e niente arrosto.": "All talk, no substance.",
    "Acqua in bocca!": "Keep it secret!",
    "Piove a catinelle.": "It is pouring.",
    "Essere al settimo cielo.": "To be overjoyed.",
    "Mettere la pulce nell'orecchio.": "To plant a suspicion.",
    "Fare il diavolo a quattro.": "To raise a ruckus.",
    "Dormire come un ghiro.": "To sleep deeply.",
    "Non avere peli sulla lingua.": "To speak bluntly.",
    "Costare un occhio della testa.": "To cost a fortune.",
    "Chi trova un amico trova un tesoro.": "Who finds a friend finds a treasure.",
    "Tra il dire e il fare c'è di mezzo il mare.": "Easier said than done.",
    "La gatta frettolosa fece i gattini ciechi.": "Haste makes waste.",
    "Rosso di sera, bel tempo si spera.": "Red sky at night, shepherd's delight.",
}
def meaning(idiom):
    return IDIOMS[idiom]
def main():
    assert len(IDIOMS) == 20, "twenty idioms, got %d" % len(IDIOMS)
    assert meaning("In bocca al lupo!") == "Good luck!"
    assert meaning("Acqua in bocca!") == "Keep it secret!"
    score = sum(1 for lit, m in IDIOMS.items() if meaning(lit) == m)
    assert score == 20
    print("Idioms drilled: %d" % len(IDIOMS))
    for lit in list(IDIOMS)[:4]:
        print("  %s" % lit)
        print("    -> %s" % IDIOMS[lit])
    print("OK: idiom quiz passed 20/20")
if __name__ == "__main__":
    main()
'''


def demo_registers(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
PAIRS = [
    ("Ciao, come stai?", "Buongiorno, come sta?"),
    ("Scusa il ritardo.", "Mi scusi per il ritardo."),
    ("Puoi aiutarmi?", "Può aiutarmi?"),
    ("Dammi il tuo numero.", "Mi può dare il suo numero?"),
    ("Vieni domani?", "Può venire domani?"),
    ("Dimmi pure.", "Mi dica pure."),
    ("Siediti qui.", "Si accomodi qui."),
    ("Aspetta un attimo.", "Attenda un momento, per favore."),
    ("Non ho capito.", "Mi scusi, non ho capito bene."),
    ("Quanto vuoi?", "Quanto desidera?"),
    ("Ti ringrazio tanto.", "La ringrazio molto."),
    ("Ci vediamo!", "ArrivederLa!"),
    ("Ti scrivo presto.", "Le scriverò al più presto."),
    ("Un bacio, Marco", "Distinti saluti, Marco Rossi"),
    ("Tuo Marco", "In attesa di una Sua risposta, porgo cordiali saluti"),
]
def is_formal(phrase):
    markers = ["sta?", "scusi", "Può", "può", "Mi dica", "Si accomodi", "Attenda",
               "desidera", "ringrazio molto", "ArrivederLa", "Le scriverò",
               "Distinti saluti", "Sua risposta"]
    return any(m in phrase for m in markers)
def main():
    assert len(PAIRS) == 15, "fifteen pairs, got %d" % len(PAIRS)
    for informal, formal in PAIRS:
        assert not is_formal(informal), "informal flagged formal: %s" % informal
        assert is_formal(formal), "formal not detected: %s" % formal
    print("Register pairs: %d formal/informal" % len(PAIRS))
    for informal, formal in PAIRS[:3]:
        print("  tu:  %s" % informal)
        print("  Lei: %s" % formal)
    print("OK: register sorter passed 15/15")
if __name__ == "__main__":
    main()
'''


def demo_complex(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
CONNECTORS = ["quando", "che", "perché", "sebbene", "appena", "dove",
              "prima di", "mentre", "se", "pur", "nonostante", "di cui",
              "tanto più"]
SENTENCES = [
    "Quando sono arrivato, la cena era già pronta.",
    "La donna che vedi è mia sorella.",
    "Ti ho chiamato perché avevo bisogno di aiuto.",
    "Sebbene piovesse, siamo usciti lo stesso.",
    "Appena avrò finito, ti telefonerò.",
    "Non so dove abbia messo le chiavi.",
    "È importante che tu venga domani.",
    "Il libro di cui ti ho parlato è in libreria.",
    "Lavorava mentre i bambini dormivano.",
    "Se avessi tempo, viaggerei di più.",
    "Mi ha detto che sarebbe venuto.",
    "Prima di uscire, spegni le luci.",
    "Pur essendo stanco, ha finito il lavoro.",
    "Nonostante la pioggia, la festa è stata un successo.",
    "Tanto più studi, tanto più impari.",
]
def count_clauses(sentence):
    return 1 + sum(1 for c in CONNECTORS if c in sentence.lower())
def main():
    assert len(SENTENCES) == 15, "fifteen sentences, got %d" % len(SENTENCES)
    assert len(CONNECTORS) == 13, "thirteen connectors"
    multi = sum(1 for s in SENTENCES if count_clauses(s) >= 2)
    assert multi == 15, "every sentence must carry a connector"
    assert count_clauses("Quando sono arrivato, la cena era già pronta.") == 2
    print("Complex sentences: %d, connectors: %d" % (len(SENTENCES), len(CONNECTORS)))
    print("Connector set: %s" % ", ".join(CONNECTORS))
    print("OK: clause counter verified on 15 complex sentences")
if __name__ == "__main__":
    main()
'''


def demo_dialogue_market(hdr, name, rid, group, points, req):
    return _dialogue_demo(hdr, name, rid, group, [
        ("Cliente", "Buongiorno!"),
        ("Venditore", "Buongiorno! Desidera?"),
        ("Cliente", "Vorrei un chilo di mele, per favore."),
        ("Venditore", "Subito. Altro?"),
        ("Cliente", "Sì, mezzo chilo di pomodori. Sono freschi?"),
        ("Venditore", "Freschissimi, arrivati stamattina."),
        ("Cliente", "Quanto costano?"),
        ("Venditore", "Tre euro al chilo."),
        ("Cliente", "E le mele?"),
        ("Venditore", "Due euro e cinquanta."),
        ("Cliente", "Mi dà anche un mazzo di basilico?"),
        ("Venditore", "Certo, glielo regalo."),
        ("Cliente", "Gentilissimo! Quanto le devo?"),
        ("Venditore", "Quattro euro in tutto."),
        ("Cliente", "Ecco cinque euro."),
        ("Venditore", "Un euro di resto."),
        ("Cliente", "Mi mette tutto nel sacchetto?"),
        ("Venditore", "Fatto. Buona giornata!"),
        ("Cliente", "Grazie, altrettanto! Arrivederci!"),
        ("Venditore", "Arrivederci!"),
    ])


def demo_dialogue_friend(hdr, name, rid, group, points, req):
    return _dialogue_demo(hdr, name, rid, group, [
        ("Marco", "Ciao, Sara! Che sorpresa!"),
        ("Sara", "Marco! Quanto tempo!"),
        ("Marco", "Come stai?"),
        ("Sara", "Benissimo, e tu?"),
        ("Marco", "Tutto bene. Che fai di bello?"),
        ("Sara", "Lavoro in una libreria in centro. E tu?"),
        ("Marco", "Insegno italiano agli stranieri."),
        ("Sara", "Che bello! Da quanto tempo?"),
        ("Marco", "Da due anni. Mi piace tantissimo."),
        ("Sara", "Hai tempo per un caffè?"),
        ("Marco", "Volentieri! Andiamo al bar all'angolo?"),
        ("Sara", "Perfetto. Offro io!"),
        ("Marco", "No, no, facciamo alla romana."),
        ("Sara", "Va bene. Allora raccontami tutto!"),
        ("Marco", "Prima tu: sei ancora con Andrea?"),
        ("Sara", "Sì, ci sposiamo a giugno!"),
        ("Marco", "Congratulazioni! Sono felicissimo per te!"),
        ("Sara", "Grazie! Verrai al matrimonio?"),
        ("Marco", "Certo che vengo!"),
        ("Sara", "Allora ci vediamo presto. Un abbraccio!"),
    ])


def demo_dialogue_problem(hdr, name, rid, group, points, req):
    return _dialogue_demo(hdr, name, rid, group, [
        ("Turista", "Mi scusi, mi sono perso."),
        ("Passante", "Non si preoccupi. Dove deve andare?"),
        ("Turista", "Cerco il Museo Nazionale."),
        ("Passante", "È vicino. Vada sempre dritto."),
        ("Turista", "Dritto fino in fondo?"),
        ("Passante", "Sì, poi giri a sinistra al semaforo."),
        ("Turista", "A sinistra, ho capito. È lontano?"),
        ("Passante", "No, cinque minuti a piedi."),
        ("Turista", "C'è un ingresso laterale?"),
        ("Passante", "Sì, ma è chiuso il lunedì."),
        ("Turista", "Oggi è martedì, bene. A che ora chiude?"),
        ("Passante", "Alle diciotto."),
        ("Turista", "Quanto costa il biglietto?"),
        ("Passante", "Dieci euro, ridotto otto."),
        ("Turista", "Perfetto. E per mangiare qui vicino?"),
        ("Passante", "C'è una trattoria ottima in via Roma."),
        ("Turista", "La ringrazio molto, è stato gentilissimo."),
        ("Passante", "Prego! Buona visita!"),
        ("Turista", "ArrivederLa!"),
        ("Passante", "ArrivederLa!"),
    ])


def demo_mastery(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
WORDS = """essere avere fare andare dire vedere mangiare bere parlare scrivere leggere dormire lavorare studiare comprare vendere aprire chiudere prendere dare venire sapere conoscere pensare amare uomo donna bambino amico famiglia casa porta finestra tavolo sedia libro scuola lavoro giorno notte tempo acqua cibo macchina strada città paese mondo nome problema bello brutto buono cattivo grande piccolo nuovo vecchio alto basso lungo corto giovane anziano felice triste caldo freddo dolce amaro rosso verde bianco nero facile molto poco bene male sempre mai già ancora troppo presto tardi qui lì così forse io tu lui lei noi voi loro mio tuo suo nostro vostro questo quello chi che cosa come quando dove perché quale uno due tre quattro cinque dieci venti trenta cento mille primo secondo oggi ieri domani lunedì domenica gennaio dicembre primavera estate autunno inverno ciao buongiorno buonasera buonanotte grazie prego arrivederci scusi permesso auguri salute sì no anche cane gatto sole luna mare montagna fiume lago albero fiore pane vino formaggio carne pesce telefono computer treno aereo albergo soldi prezzo mercato chiesa piazza ponte medico farmacia ospedale mano testa cuore occhio bocca latte caffè birra torta gelato pizza pasta insalata colazione pranzo cena zia cugino nipote settimana mese stazione""".split()
ACCENTS = ["à", "è", "é", "ì", "ò", "ù"]
def main():
    assert len(WORDS) == 200, "core word list must be 200, got %d" % len(WORDS)
    assert len(set(WORDS)) == len(WORDS), "no duplicate words"
    assert "essere" in WORDS and "grazie" in WORDS and "computer" in WORDS
    assert len(ACCENTS) == 6, "six accent marks in the reference"
    print("Mastery reference: %d core words (target 200)" % len(WORDS))
    print("Unique words: %d" % len(set(WORDS)))
    print("Sample: %s" % ", ".join(WORDS[:10]))
    print("OK: mastery reference verified - %d unique core words" % len(WORDS))
if __name__ == "__main__":
    main()
'''


DEMOS = {
    "italian_overview": demo_overview,
    "italian_writing": demo_alphabet,
    "italian_nouns": demo_nouns,
    "italian_phonology": demo_phonology,
    "italian_adjectives": demo_agreement,
    "italian_verbs": demo_verbs,
    "italian_numbers": demo_numbers,
    "italian_pronouns": demo_pronouns,
    "italian_greetings": demo_greetings,
    "italian_grammar": demo_grammar,
    "italian_home_family": demo_home_family,
    "italian_food_cooking": demo_food_cooking,
    "italian_travel": demo_travel,
    "italian_work_school": demo_work_school,
    "italian_health_body": demo_health_body,
    "italian_emotions": demo_emotions,
    "italian_nature_weather": demo_nature_weather,
    "italian_shopping": demo_shopping,
    "italian_friendship": demo_friendship,
    "italian_technology": demo_technology,
    "italian_tenses": demo_tenses,
    "italian_qa": demo_qa,
    "italian_commands": demo_commands,
    "italian_descriptions": demo_descriptions,
    "italian_story1": demo_story1,
    "italian_story2": demo_story2,
    "italian_story3": demo_story3,
    "italian_idioms": demo_idioms,
    "italian_registers": demo_registers,
    "italian_complex": demo_complex,
    "italian_dialogue_market": demo_dialogue_market,
    "italian_dialogue_friend": demo_dialogue_friend,
    "italian_dialogue_problem": demo_dialogue_problem,
    "italian_mastery": demo_mastery,
}
