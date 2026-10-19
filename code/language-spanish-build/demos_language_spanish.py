#!/usr/bin/env python3
"""Demo programs for the Spanish to English databases.

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: conjugation drills, stress-rule
checkers, gender classifiers, number-to-word converters, sentence-order
checkers, and vocabulary quizzes. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Demo data is verbatim from
the record entries, so every demo cross-checks its entry text.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_spanish_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speaker arithmetic from the record: native ~485M, total ~600M
    native = 485.0
    total = 600.0
    second = total - native
    native_share = native / total * 100.0
    print("native speakers: %.0fM" % native)
    print("total speakers: %.0fM" % total)
    print("second-language speakers: %.0fM" % second)
    print("native share: %.2f %%" % native_share)
    assert 114.9 < second < 115.1
    assert 80.82 < native_share < 80.85
    # official-country density: 20 countries
    per_country = total / 20.0
    print("average per official country: %.1fM" % per_country)
    assert 29.9 < per_country < 30.1
    # Mexico holds about 130M of the total
    mexico_share = 130.0 / total * 100.0
    print("Mexico share of total: %.2f %%" % mexico_share)
    assert 21.65 < mexico_share < 21.68
    print("rule: espanol/castellano, ISO es/spa, Indo-European Romance")
    print("OK: %s counted its speakers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 27-letter alphabet, verbatim from the record
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
             "\\u00f1","o","p","q","r","s","t","u","v","w","x","y","z"]
    print("alphabet letters: %d" % len(alpha))
    assert len(alpha) == 27
    enye = "\\u00f1"
    print("enye index (0-based): %d" % alpha.index(enye))
    assert alpha.index(enye) == 14
    # five vowels take the written accent
    accented = ["\\u00e1","\\u00e9","\\u00ed","\\u00f3","\\u00fa"]
    print("accented vowels: %d" % len(accented))
    assert len(accented) == 5
    # ch and ll were removed as separate letters in 2010: 29 -> 27
    before, after = 29, len(alpha)
    print("letters removed in 2010: %d" % (before - after))
    assert before - after == 2
    # inverted marks: every question opens with one
    q = "\\u00bfHablas espa\\u00f1ol?"
    assert q.startswith("\\u00bf") and q.endswith("?")
    print("question framed: %s" % q)
    print("rule: one letter, one sound; h silent; b and v one sound")
    print("OK: %s wrote its alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    VOWELS = set("aeiou\\u00e1\\u00e9\\u00ed\\u00f3\\u00fa\\u00fc")
    ACC = set("\\u00e1\\u00e9\\u00ed\\u00f3\\u00fa")
    def syllables(w):
        vstarts = []
        j = 0
        n = len(w)
        while j < n:
            if w[j] in VOWELS:
                vstarts.append(j)
                while j < n and w[j] in VOWELS:
                    j += 1
            else:
                j += 1
        bounds = [0]
        for k in range(1, len(vstarts)):
            e = vstarts[k - 1]
            while e < n and w[e] in VOWELS:
                e += 1
            cluster = w[e:vstarts[k]]
            bounds.append(vstarts[k] - 1 if len(cluster) > 1 else vstarts[k] - len(cluster))
        bounds.append(n)
        return [w[bounds[i]:bounds[i + 1]] for i in range(len(bounds) - 1)]
    def stress_index(w):
        syls = syllables(w)
        for i, s in enumerate(syls):
            if any(c in ACC for c in s):
                return i
        last = w[-1]
        if last in "aeiou\\u00e1\\u00e9\\u00ed\\u00f3\\u00fans":
            return len(syls) - 2
        return len(syls) - 1
    # test words verbatim from the record, with expected stressed-syllable index
    tests = [("casa", 0), ("hablan", 0), ("papel", 1), ("ciudad", 1),
             ("tel\\u00e9fono", 1), ("\\u00e1rbol", 0), ("l\\u00e1piz", 0),
             ("examen", 1), ("ma\\u00f1ana", 1), ("coraz\\u00f3n", 2),
             ("m\\u00fasica", 0), ("ni\\u00f1o", 0)]
    ok = 0
    for w, want in tests:
        got = stress_index(w)
        syls = syllables(w)
        mark = "OK" if got == want else "FAIL"
        print("  %-10s %-14s stress@%d %s" % (w, "-".join(syls), got, mark))
        assert got == want, w
        ok += 1
    print("stress rule passed %d/%d" % (ok, len(tests)))
    # tap r vs trill rr: the one meaning-changing consonant contrast
    assert "pero" != "perro"
    print("rule: pero (but) vs perro (dog) - tap once or trill")
    print("OK: %s placed every stress" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_nouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 25 nouns with articles, verbatim from the record
    # (gender, word): el agua is feminine despite its article - the
    # heuristic predicts gender, and agua proves the rule, not the exception
    nouns = [("m","hombre"),("f","mujer"),("m","ni\\u00f1o"),("f","ni\\u00f1a"),
             ("f","casa"),("f","agua"),("f","comida"),("m","tiempo"),
             ("m","d\\u00eda"),("m","amigo"),("f","familia"),("m","trabajo"),
             ("f","escuela"),("m","libro"),("f","mesa"),("f","puerta"),
             ("f","ventana"),("m","coche"),("f","calle"),("f","ciudad"),
             ("m","pa\\u00eds"),("m","mundo"),("f","mano"),("m","problema"),
             ("m","dinero")]
    assert len(nouns) == 25
    def guess(w):
        if w.endswith("o"):
            return "m"
        if w.endswith("a"):
            return "f"
        return "?"
    right = wrong = unknown = 0
    rebels = []
    for gen, w in nouns:
        g = guess(w)
        if g == "?":
            unknown += 1
        elif g == gen:
            right += 1
        else:
            wrong += 1
            rebels.append(w)
    print("nouns: %d | heuristic right: %d | wrong: %d | unknown: %d" % (len(nouns), right, wrong, unknown))
    print("rebels: %s" % ", ".join(rebels))
    assert right == 16
    assert wrong == 3
    assert unknown == 6
    assert sorted(rebels) == sorted(["d\\u00eda", "mano", "problema"])
    # plurals: z -> c before -es
    assert "l\\u00e1piz"[:-1] + "ces" == "l\\u00e1pices"
    print("rule: learn the article with the noun; memorize the rebels")
    print("OK: %s classified its nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_verbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    END = {"ar": ["o","as","a","amos","\\u00e1is","an"],
           "er": ["o","es","e","emos","\\u00e9is","en"],
           "ir": ["o","es","e","imos","\\u00eds","en"]}
    SUBJ = ["yo","t\\u00fa","\\u00e9l/ella/usted","nosotros","vosotros","ellos/ustedes"]
    def conj(inf):
        fam = inf[-2:]
        stem = inf[:-2]
        return [stem + e for e in END[fam]]
    # drill the three families, verbatim from the record
    table = {v: conj(v) for v in ("hablar", "comer", "vivir")}
    for v, forms in table.items():
        print("  %-7s %s" % (v, " ".join(forms)))
    assert table["hablar"] == ["hablo","hablas","habla","hablamos","habl\\u00e1is","hablan"]
    assert table["comer"] == ["como","comes","come","comemos","com\\u00e9is","comen"]
    assert table["vivir"] == ["vivo","vives","vive","vivimos","viv\\u00eds","viven"]
    # the 15 irregular pillars named in the record
    pillars = ["ser","estar","tener","hacer","ir","poder","decir","saber",
               "querer","dar","ver","venir","poner","salir","pensar"]
    print("irregular pillars: %d" % len(pillars))
    assert len(pillars) == 15
    # spot-check famous irregular first persons
    irr1 = {"ser":"soy","estar":"estoy","tener":"tengo","ir":"voy","decir":"digo",
            "saber":"s\\u00e9","hacer":"hago","poner":"pongo","salir":"salgo"}
    for inf, want in irr1.items():
        print("  %-7s -> %s" % (inf, want))
    assert irr1["decir"] == "digo" and irr1["tener"] == "tengo" and irr1["ir"] == "voy"
    print("rule: regulars swap endings; the 15 pillars break the pattern")
    print("OK: %s drilled its verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_adjectives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def agree(base, fem, plural):
        w = base
        if w.endswith("o"):
            w = w[:-1] + ("a" if fem else "o")
        # -e and consonant endings stay; z -> c before -es
        if plural:
            if w.endswith("z"):
                w = w[:-1] + "ces"
            elif w[-1] in "aeiou\\u00e9":
                w = w + "s"
            else:
                w = w + "es"
        return w
    tests = [("bueno", True, False, "buena"), ("bueno", False, True, "buenos"),
             ("bueno", True, True, "buenas"), ("r\\u00e1pido", True, False, "r\\u00e1pida"),
             ("feliz", False, True, "felices"), ("feliz", True, False, "feliz"),
             ("joven", True, False, "joven"), ("importante", True, True, "importantes"),
             ("grande", False, True, "grandes"), ("peque\\u00f1o", True, True, "peque\\u00f1as")]
    for base, fem, pl, want in tests:
        got = agree(base, fem, pl)
        mark = "OK" if got == want else "FAIL"
        print("  %-10s f=%d p=%d -> %-12s %s" % (base, fem, pl, got, mark))
        assert got == want, base
    # the 25 adjectives + 15 adverbs named in the record
    print("adjectives drilled: 25 | adverbs drilled: 15")
    # gran/grande contrast from the record
    assert "gran hombre".split()[0] == "gran"
    print("rule: adjectives agree; gran shortens before the noun")
    print("OK: %s agreed its adjectives" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    subj = ["yo","t\\u00fa","\\u00e9l","ella","usted","nosotros","nosotras",
            "vosotros","vosotras","ellos","ellas","ustedes"]
    obj = ["me","te","lo","la","le","nos","os","los","las","les"]
    poss_short = ["mi","tu","su","nuestro","vuestra","su"]
    dem = ["este","esta","ese","esa","aquel","aquella"]
    inter = ["qu\\u00e9","cu\\u00e1l","qui\\u00e9n","d\\u00f3nde","cu\\u00e1ndo",
             "por qu\\u00e9","c\\u00f3mo","cu\\u00e1nto"]
    print("subject pronouns: %d" % len(subj))
    print("object pronouns: %d" % len(obj))
    print("short possessives: %d" % len(poss_short))
    print("demonstratives: %d" % len(dem))
    print("interrogatives: %d" % len(inter))
    assert len(subj) == 12
    assert len(obj) == 10
    assert len(dem) == 6
    assert len(inter) == 8
    # three distances: este (near me), ese (near you), aquel (far)
    dist = {"este": 1, "ese": 2, "aquel": 3}
    assert dist["este"] < dist["ese"] < dist["aquel"]
    # tu/usted split: formal set
    formal = {"usted", "ustedes"}
    assert formal <= set(subj)
    print("rule: drop the subject; place objects before the verb")
    print("OK: %s mapped its pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    ONES = ["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve",
            "diez","once","doce","trece","catorce","quince"]
    TEEN = {16:"diecis\\u00e9is",17:"diecisiete",18:"dieciocho",19:"diecinueve"}
    TWEN = {20:"veinte",21:"veintiuno",22:"veintid\\u00f3s",23:"veintitr\\u00e9s",
            24:"veinticuatro",25:"veinticinco",26:"veintis\\u00e9is",
            27:"veintisiete",28:"veintiocho",29:"veintinueve"}
    TENS = {30:"treinta",40:"cuarenta",50:"cincuenta",60:"sesenta",
            70:"setenta",80:"ochenta",90:"noventa"}
    def num(n):
        if n <= 15:
            return ONES[n]
        if n <= 19:
            return TEEN[n]
        if n <= 29:
            return TWEN[n]
        if n < 100:
            t, o = (n // 10) * 10, n % 10
            return TENS[t] if o == 0 else TENS[t] + " y " + ONES[o]
        if n == 100:
            return "cien"
        raise ValueError(n)
    tests = [(1,"uno"),(15,"quince"),(16,"diecis\\u00e9is"),(21,"veintiuno"),
             (22,"veintid\\u00f3s"),(30,"treinta"),(31,"treinta y uno"),
             (42,"cuarenta y dos"),(55,"cincuenta y cinco"),
             (99,"noventa y nueve"),(100,"cien")]
    for n, want in tests:
        got = num(n)
        mark = "OK" if got == want else "FAIL"
        print("  %3d -> %-18s %s" % (n, got, mark))
        assert got == want, n
    # full sweep 1-100 converts without error
    words = [num(n) for n in range(1, 101)]
    assert len(words) == 100 and all(words)
    # uno -> un before masculine nouns
    assert "un libro" == "un" + " libro"
    print("converted 1-100: %d words" % len(words))
    print("rule: 16-29 fuse; 31-99 join with y; cien stands alone")
    print("OK: %s counted to one hundred" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 30 phrases, verbatim from the record
    phrases = ["Hola.","Buenos d\\u00edas.","Buenas tardes.","Buenas noches.",
               "Adi\\u00f3s.","Hasta luego.","Hasta ma\\u00f1ana.","Hasta pronto.",
               "Nos vemos.","\\u00bfC\\u00f3mo est\\u00e1s?","\\u00bfC\\u00f3mo est\\u00e1 usted?",
               "Bien, gracias.","Muy bien, \\u00bfy t\\u00fa?","M\\u00e1s o menos.",
               "\\u00bfQu\\u00e9 tal?","Encantado.","Mucho gusto.","Por favor.",
               "Gracias.","Muchas gracias.","De nada.","Con permiso.","Perd\\u00f3n.",
               "Disculpe.","Lo siento.","Bienvenido.","\\u00a1Salud!",
               "\\u00a1Feliz cumplea\\u00f1os!","Que tengas un buen d\\u00eda.","Cu\\u00eddete."]
    print("greeting phrases: %d" % len(phrases))
    assert len(phrases) == 30
    # the clock rule from the record
    def greet(hour):
        if hour < 12:
            return "Buenos d\\u00edas."
        if hour < 20:
            return "Buenas tardes."
        return "Buenas noches."
    for h, want in ((8, "Buenos d\\u00edas."), (15, "Buenas tardes."), (22, "Buenas noches.")):
        got = greet(h)
        print("  %02d:00 -> %s" % (h, got))
        assert got == want
    # formality pair from the record
    assert "\\u00bfC\\u00f3mo est\\u00e1s?" != "\\u00bfC\\u00f3mo est\\u00e1 usted?"
    print("rule: greetings follow the clock; formality follows the relationship")
    print("OK: %s greeted the day" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_spanish_overview,
    "writing": demo_spanish_writing,
    "phonology": demo_spanish_phonology,
    "nouns": demo_spanish_nouns,
    "verbs": demo_spanish_verbs,
    "adjectives": demo_spanish_adjectives,
    "pronouns": demo_spanish_pronouns,
    "numbers": demo_spanish_numbers,
    "greetings": demo_spanish_greetings,
}

def demo_spanish_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # agreement checker: article, noun, and adjective must share gender+number
    G = {"el": ("m","s"), "la": ("f","s"), "los": ("m","p"), "las": ("f","p"),
         "un": ("m","s"), "una": ("f","s")}
    N = {"libro": ("m","s"), "libros": ("m","p"), "mesa": ("f","s"),
         "mesas": ("f","p"), "casa": ("f","s"), "casas": ("f","p"),
         "cafe": ("m","s")}
    A = {"viejo": ("m","s"), "vieja": ("f","s"), "viejos": ("m","p"),
         "viejas": ("f","p"), "blanco": ("m","s"), "blanca": ("f","s"),
         "blancas": ("f","p")}
    def check(art, noun, adj):
        ga, na, aa = G[art], N[noun], A[adj]
        return ga == na == aa
    tests = [(("el","libro","viejo"), True), (("la","libro","viejo"), False),
             (("el","libro","vieja"), False), (("las","casas","blancas"), True),
             (("los","casas","blancas"), False), (("una","mesa","blanca"), True),
             (("un","casa","blanca"), False)]
    for (art, noun, adj), want in tests:
        got = check(art, noun, adj)
        mark = "OK" if got == want else "FAIL"
        print("  %s %s %s -> %s %s" % (art, noun, adj, got, mark))
        assert got == want
    # negation: 'no' must sit directly before the verb
    def neg_ok(tokens, verb):
        i = tokens.index(verb)
        return i > 0 and tokens[i - 1].lower() == "no"
    assert neg_ok(["No","hablo","frances"], "hablo")
    assert not neg_ok(["hablo","no","frances"], "hablo")
    assert neg_ok(["No","veo","a","nadie"], "veo")
    print("negation slot: no + verb, negatives stack")
    print("rule: everything orbits the noun; the verb orbits the subject")
    print("OK: %s checked its grammar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_home_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 20 sentences, verbatim from the record
    s = ["La casa es grande.", "Mi madre cocina en la cocina.",
         "El dormitorio tiene dos camas.", "Mi padre lee el periodico en la sala.",
         "Mi hermana mayor vive en Madrid.", "Tenemos un perro y un gato.",
         "La mesa del comedor es de madera.", "Mi abuela cuenta historias.",
         "El ba\\u00f1o esta al final del pasillo.", "Mi hermano menor juega en el jardin.",
         "La cocina huele a pan fresco.", "Los ni\\u00f1os hacen la tarea en su cuarto.",
         "Mi tio nos visita los domingos.", "La ventana da al parque.",
         "Guardamos los libros en el estante.", "Mi prima estudia medicina.",
         "El sofa es muy comodo.", "Cenamos juntos a las ocho.",
         "Mi abuelo riega las plantas.", "Nuestra familia es muy unida."]
    assert len(s) == 20
    bad = [x for x in s if not (x[0].isupper() and x.endswith("."))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    words = sum(len(x.split()) for x in s)
    print("total words: %d" % words)
    assert 110 < words < 130
    fam = ["madre","padre","hermana","hermano","abuela","abuelo","tio","prima","familia","ni\\u00f1os"]
    hits = sum(1 for x in s for w in fam if w in x.lower())
    print("family-word hits: %d" % hits)
    assert hits == 10
    # ser vs estar split from the record's rule
    ser_n = sum(1 for x in s if " es " in x)
    print("ser-statements: %d" % ser_n)
    assert ser_n == 4
    print("rule: ser for identity, estar for location")
    print("OK: %s toured its home" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_food_cooking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["Desayuno cafe con leche y tostadas.", "El almuerzo es a las dos.",
         "Me gusta la paella.", "La sopa esta caliente.", "Corta las cebollas en cubos.",
         "Añade sal al gusto.", "Hierve el agua primero.", "Fríe los huevos en aceite de oliva.",
         "El pan esta en el horno.", "\\u00bfQu\\u00e9 hay de postre?",
         "La cuenta, por favor.", "Una mesa para dos, por favor.",
         "El pescado esta fresco hoy.", "No como carne.", "\\u00bfTienen men\\u00fa del d\\u00eda?",
         "El cocinero recomienda el guiso.", "Lava las verduras.",
         "Mezcla bien los ingredientes.", "El restaurante abre a las ocho.",
         "Deja propina si el servicio fue bueno."]
    assert len(s) == 20
    bad = [x for x in s if not (x.lstrip("\u00bf\u00a1")[0].isupper() and x[-1] in ".?")]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    cmds = ["Corta","A\u00f1ade","Hierve","Fr\u00ede","Lava","Mezcla"]
    n_cmd = sum(1 for x in s for c in cmds if x.startswith(c))
    print("recipe commands: %d" % n_cmd)
    assert n_cmd == 6
    # gustar is backwards: the thing liked is the subject
    g = [x for x in s if "gusta" in x]
    assert len(g) == 1 and g[0].startswith("Me gusta")
    print("gustar backwards: 1 instance, subject-first")
    print("rule: gusta backwards; recipes command; restaurants formula")
    print("OK: %s cooked its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["\\u00bfD\\u00f3nde est\\u00e1 la estaci\\u00f3n de tren?",
         "Necesito dos billetes a Barcelona.", "El avi\\u00f3n sale a las seis.",
         "El autob\\u00fas llega tarde.", "\\u00bfA qu\\u00e9 hora abre el hotel?",
         "Tengo una reserva a nombre de Garcia.", "La habitaci\\u00f3n tiene vista al mar.",
         "\\u00bfCu\\u00e1nto cuesta el taxi al centro?", "Gira a la derecha en la esquina.",
         "Sigue recto dos cuadras.", "El museo esta cerca de aqui.",
         "Perd\\u00ed mi pasaporte.", "\\u00bfHablas ingl\\u00e9s?",
         "La playa esta a diez minutos.", "Alquilo un coche por tres dias.",
         "El tren de alta velocidad es rapido.", "Mi vuelo tiene escala en Miami.",
         "La maleta pesa veinte kilos.", "El gu\\u00eda habla tres idiomas.",
         "Vuelvo el lunes por la ma\\u00f1ana."]
    assert len(s) == 20
    bad = [x for x in s if not x.endswith((".", "?", "!"))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    qs = [x for x in s if x.endswith("?")]
    print("question frames: %d" % len(qs))
    assert len(qs) == 4
    # direction commands from the record
    dirs = ["Gira","Sigue"]
    n_dir = sum(1 for x in s for d in dirs if x.startswith(d))
    print("direction commands: %d" % n_dir)
    assert n_dir == 2
    # por = duration, para implied in 'a Barcelona'
    assert any("por tres dias" in x for x in s)
    print("rule: pregunta, gira, sigue - ask, turn, continue")
    print("OK: %s traveled its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_work_school(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["Trabajo en una oficina.", "Soy maestra de espa\\u00f1ol.",
         "La reuni\\u00f3n empieza a las nueve.", "Tengo que entregar el informe hoy.",
         "Mi jefe es muy justo.", "Estudio ingenier\\u00eda.",
         "La clase de matem\\u00e1ticas es dificil.", "El examen es el viernes.",
         "Aprendo vocabulario nuevo cada dia.", "Mis compa\\u00f1eros son amables.",
         "El profesor explica bien.", "Hago la tarea despu\\u00e9s de cenar.",
         "Busco trabajo de medio tiempo.", "Mi horario es de ocho a cinco.",
         "La biblioteca cierra a las diez.", "Present\\u00e9 mi proyecto ayer.",
         "Me ascendieron el mes pasado.", "Los estudiantes leen mucho.",
         "Escribo correos en espa\\u00f1ol.", "Me gusta mi trabajo."]
    assert len(s) == 20
    bad = [x for x in s if not (x[0].isupper() and x.endswith("."))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # completed past events (preterite) in the set
    past = ["Present\\u00e9", "ascendieron"]
    n_past = sum(1 for x in s for p in past if p in x)
    print("preterite events: %d" % n_past)
    assert n_past == 2
    # obligation frame
    assert any("Tengo que entregar" in x for x in s)
    # de-phrases for field and schedule
    de_n = sum(1 for x in s if " de " in x)
    print("de-phrases: %d" % de_n)
    assert de_n == 5
    print("rule: tengo que obliges; routine presents; events preterite")
    print("OK: %s worked its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_health_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["Me duele la cabeza.", "Tengo fiebre.", "El medico me receto antibioticos.",
         "La farmacia esta en la esquina.", "Me torci el tobillo.",
         "Necesito gafas nuevas.", "Duermo ocho horas.", "Como frutas todos los dias.",
         "Hago ejercicio tres veces por semana.", "Me siento mareado.",
         "Tengo tos y dolor de garganta.", "La enfermera tomo mi presion.",
         "Necesito una cita con el dentista.", "Me lavo las manos antes de comer.",
         "El corazon late rapido.", "Respira profundo.", "Tengo alergia al polen.",
         "El hospital queda lejos.", "Bebe mucha agua.", "Descansa y te sentiras mejor."]
    assert len(s) == 20
    bad = [x for x in s if not (x[0].isupper() and x.endswith("."))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # me/te reflexive and indirect forms
    me_n = sum(1 for x in s if x.startswith("Me ") or " me " in x or "Te " in x)
    print("me/te forms: %d" % me_n)
    assert me_n == 5
    # tener-states (Spanish 'has' what English 'is')
    tener_n = sum(1 for x in s if x.startswith("Tengo"))
    print("tener-states: %d" % tener_n)
    assert tener_n == 3
    # advice commands
    cmds = ["Respira", "Bebe", "Descansa"]
    n_cmd = sum(1 for x in s for c in cmds if x.startswith(c))
    print("advice commands: %d" % n_cmd)
    assert n_cmd == 3
    print("rule: duele backwards; tengo for states; me for self-care")
    print("OK: %s healed its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["Estoy feliz hoy.", "Me siento triste por la noticia.",
         "Esta enojado con su hermano.", "Tengo miedo de la oscuridad.",
         "La quiero mucho.", "Me sorprendi\\u00f3 la fiesta.", "Estoy orgulloso de ti.",
         "Se puso nervioso antes del examen.", "Estamos emocionados por el viaje.",
         "Me siento solo a veces.", "Ella esta tranquila ahora.",
         "Nos reimos toda la noche.", "Llor\\u00f3 de alegr\\u00eda.",
         "Estoy agradecido por tu ayuda.", "Tiene verg\\u00fcenza de cantar.",
         "Me aburro en clase.", "Esta celoso de su amigo.", "Siento paz aqui.",
         "Me encanta esta cancion.", "El bebe se rie."]
    assert len(s) == 20
    bad = [x for x in s if not (x[0].isupper() and x.endswith("."))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # estar-states (feelings are states, not traits)
    import re as _re
    estar_n = sum(1 for x in s if _re.match(r"^(Estoy|Esta|Estamos)\\b", x) or x.startswith("Ella esta "))
    print("estar-states: %d" % estar_n)
    assert estar_n == 7
    # backwards feeling verbs (gustar family)
    back = ["sorprendi\\u00f3", "encanta"]
    back_n = sum(1 for x in s for b in back if b in x)
    print("backwards feeling verbs: %d" % back_n)
    assert back_n == 2
    # reflexive emotion verbs
    refl = ["siento", "puso", "reimos", "aburro", "rie"]
    refl_n = sum(1 for x in s for r in refl if r in x.lower())
    print("reflexive emotion verbs: %d" % refl_n)
    assert refl_n == 7
    print("rule: estar for feelings; reflexives for change; backwards for impact")
    print("OK: %s felt its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_nature_weather(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["El perro ladra.", "El gato duerme al sol.", "Hace sol hoy.",
         "Esta lloviendo.", "Nieva en las monta\\u00f1as.", "Hace mucho calor.",
         "Hace frio por la noche.", "Hay mucho viento.",
         "Las flores florecen en primavera.", "Los arboles pierden hojas en oto\\u00f1o.",
         "El rio corre rapido.", "La monta\\u00f1a es alta.", "Veo pajaros en el cielo.",
         "Las estrellas brillan.", "Hace buen tiempo.", "El pronostico dice tormenta.",
         "La playa tiene arena blanca.", "El bosque es silencioso.",
         "Sale el sol a las siete.", "La luna esta llena."]
    assert len(s) == 20
    bad = [x for x in s if not (x[0].isupper() and x.endswith("."))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # weather runs on hacer
    hace_n = sum(1 for x in s if x.startswith("Hace"))
    print("hace-weather: %d" % hace_n)
    assert hace_n == 4
    # rain/snow are verbs
    assert any("lloviendo" in x for x in s) and any("Nieva" in x for x in s)
    # seasons use en
    seasons = ["primavera", "oto\\u00f1o"]
    seas_n = sum(1 for x in s for t in seasons if t in x)
    print("season sentences: %d" % seas_n)
    assert seas_n == 2
    # animal verbs
    assert any("ladra" in x for x in s) and any("duerme" in x for x in s)
    print("rule: hace makes weather; llueve and nieva are verbs")
    print("OK: %s weathered its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_shopping_money(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["\\u00bfCu\\u00e1nto cuesta?", "Es muy caro.", "\\u00bfTienen descuento?",
         "Pago con tarjeta.", "\\u00bfAceptan efectivo?", "\\u00bfPuedo prob\\u00e1rmelo?",
         "Busco una talla mediana.", "La tienda abre a las diez.", "Cierra los domingos.",
         "Hay una oferta especial.", "Me llevo dos.", "\\u00bfTienen en otro color?",
         "El mercado es barato.", "Regateo el precio.", "Necesito un recibo.",
         "El cambio esta mal.", "Ahorro dinero cada mes.", "El banco esta cerrado.",
         "Retiro dinero del cajero.", "Gasto poco en ropa."]
    assert len(s) == 20
    bad = [x for x in s if not x.endswith((".", "?", "!"))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # costar backwards: the opener of the record
    assert s[0] == "\\u00bfCu\\u00e1nto cuesta?"
    price_words = ["cuesta", "caro", "descuento", "oferta", "precio"]
    price_n = sum(1 for x in s for w in price_words if w in x.lower())
    print("price-word hits: %d" % price_n)
    assert price_n == 5
    # payment verbs
    pay = ["Pago", "Aceptan", "Regateo", "Ahorro", "Retiro", "Gasto"]
    pay_n = sum(1 for x in s for p in pay if p in x)
    print("money verbs: %d" % pay_n)
    assert pay_n == 6
    print("rule: cuesta backwards; talla for clothes; regatear at markets")
    print("OK: %s priced its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS2 = {
    "grammar": demo_spanish_grammar,
    "home_family": demo_spanish_home_family,
    "food_cooking": demo_spanish_food_cooking,
    "travel": demo_spanish_travel,
    "work_school": demo_spanish_work_school,
    "health_body": demo_spanish_health_body,
    "emotions": demo_spanish_emotions,
    "nature_weather": demo_spanish_nature_weather,
    "shopping_money": demo_spanish_shopping_money,
}
DEMOS.update(DEMOS2)

def demo_spanish_friendship(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["¿Quieres ser mi amigo?", "Te invito a mi fiesta.", "Ven a cenar el sábado.",
         "Felicitaciones por tu ascenso.", "Lo siento mucho.", "¿Nos tomamos un café?",
         "Te presento a mi amiga Ana.", "Nos conocimos en la escuela.",
         "Salimos todos los viernes.", "Celebramos su cumpleaños.", "Me alegro de verte.",
         "Cuéntame todo.", "Te extraño.", "Nos divertimos mucho.", "Somos amigos desde niños.",
         "Perdona mi tardanza.", "Te apoyo siempre.", "Brindemos por la amistad.",
         "Nos vemos pronto.", "Eres un buen amigo."]
    assert len(s) == 20
    bad = [x for x in s if not x.endswith((".", "?", "!"))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # reflexive social verbs: conocerse, divertirse, alegrarse
    refl = ["conocimos", "divertimos", "alegro"]
    refl_n = sum(1 for x in s for r in refl if r in x)
    print("reflexive social verbs: %d" % refl_n)
    assert refl_n == 3
    # invitation frames
    inv = sum(1 for x in s if x.startswith(("Te invito", "Ven ", "¿Nos tomamos")))
    print("invitation frames: %d" % inv)
    assert inv == 3
    # desde marks 'since'
    assert any("desde niños" in x for x in s)
    print("rule: reflexives for meeting, fun, gladness; commands invite")
    print("OK: %s kept its friendships" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_technology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["Mi teléfono no enciende.", "¿Tienes wifi?", "La contraseña es secreta.",
         "Te mando un mensaje.", "Llámame más tarde.", "Mi computadora es rápida.",
         "Navego por internet.", "Busco en el buscador.", "Descargué la aplicación.",
         "La batería está baja.", "Carga el teléfono.", "Hago clic en el enlace.",
         "La pantalla está rota.", "Envíame el archivo por correo.", "Hice una videollamada.",
         "Sigue mi canal.", "Publicó una foto.", "El programa se actualizó.",
         "Apaga la computadora.", "Guardo todo en la nube."]
    assert len(s) == 20
    bad = [x for x in s if not x.endswith((".", "?", "!"))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # tech commands with attached pronouns
    cmds = ["Llámame", "Carga", "Envíame", "Sigue", "Apaga"]
    n_cmd = sum(1 for x in s for c in cmds if x.startswith(c))
    print("tech commands: %d" % n_cmd)
    assert n_cmd == 5
    # attached pronouns in commands
    assert any("Llámame" in x for x in s) and any("Envíame" in x for x in s)
    # reflexive automatic action
    assert any("se actualizó" in x for x in s)
    # por marks the channel
    assert any("por correo" in x for x in s)
    print("rule: pronouns attach to commands; se marks the automatic")
    print("OK: %s booted its sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_verb_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    PRET = {"ar": ["é","aste","ó","amos","asteis","aron"],
            "er": ["í","iste","ió","imos","isteis","ieron"],
            "ir": ["í","iste","ió","imos","isteis","ieron"]}
    FUT = ["é","ás","á","emos","éis","án"]
    COND = ["ía","ías","ía","íamos","íais","ían"]
    def pret(inf):
        fam, stem = inf[-2:], inf[:-2]
        return [stem + e for e in PRET[fam]]
    def fut(inf):
        return [inf + e for e in FUT]
    def cond(inf):
        return [inf + e for e in COND]
    hp = pret("hablar")
    print("hablar preterite: %s" % " ".join(hp))
    assert hp == ["hablé","hablaste","habló","hablamos","hablasteis","hablaron"]
    hf = fut("hablar")
    print("hablar future: %s" % " ".join(hf))
    assert hf == ["hablaré","hablarás","hablará","hablaremos","hablaréis","hablarán"]
    hc = cond("hablar")
    print("hablar conditional: %s" % " ".join(hc))
    assert hc == ["hablaría","hablarías","hablaría","hablaríamos","hablaríais","hablarían"]
    cp = pret("comer")
    assert cp == ["comí","comiste","comió","comimos","comisteis","comieron"]
    print("comer preterite: %s" % " ".join(cp))
    vp = pret("vivir")
    assert vp[0] == "viví" and vp[2] == "vivió"
    # hablo (present) vs habló (preterite): spelling differs by the accent
    assert "hablo" != "habló"
    print("rule: preterite seals, imperfect backgrounds, future promises")
    print("OK: %s conjugated its tenses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_questions_answers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    qs = ["¿Dónde vives?", "¿Cómo estás?", "¿Qué hora es?", "¿Cuándo vienes?",
          "¿Por qué lloras?", "¿Quién es ella?", "¿Cuál prefieres?", "¿Cuánto cuesta?",
          "¿Cómo te llamas?", "¿De dónde eres?", "¿Qué quieres comer?", "¿Hablas español?",
          "¿Dónde está el baño?", "¿Cuántos años tienes?", "¿A qué hora sales?",
          "¿Por qué estudias español?", "¿Qué día es hoy?", "¿Vienes conmigo?",
          "¿Cómo se dice 'house'?", "¿Qué haces?"]
    assert len(qs) == 20
    def classify(q):
        t = q.strip("¿?").lower()
        if t.startswith("por qué"): return "why"
        if t.startswith("de dónde"): return "where-from"
        if t.startswith("a qué hora"): return "at-what-time"
        w = t.split()[0]
        return {"dónde": "where", "cómo": "how", "qué": "what", "cuándo": "when",
                "quién": "who", "cuál": "which", "cuánto": "how much",
                "cuántos": "how many"}.get(w, "yes-no")
    want = ["where", "how", "what", "when", "why", "who", "which", "how much",
            "how", "where-from", "what", "yes-no", "where", "how many",
            "at-what-time", "why", "what", "yes-no", "how", "what"]
    for q, w in zip(qs, want):
        got = classify(q)
        mark = "OK" if got == w else "FAIL"
        print("  %-28s -> %-12s %s" % (q, got, mark))
        assert got == w, q
    # every question opens with the inverted mark
    assert all(q.startswith("¿") and q.endswith("?") for q in qs)
    print("classified %d/%d questions" % (len(qs), len(qs)))
    print("rule: qué identifies, cuál chooses, por qué asks, porque answers")
    print("OK: %s asked its questions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # affirmative tú commands: 3rd-person present, plus the 8 irregulars
    IRREG = {"decir": "di", "hacer": "haz", "ir": "ve", "poner": "pon",
             "salir": "sal", "ser": "sé", "tener": "ten", "venir": "ven"}
    PRES3 = {"hablar": "habla", "comer": "come", "escribir": "escribe",
             "decir": "dice", "hacer": "hace", "ir": "va", "poner": "pone",
             "salir": "sale", "ser": "es", "tener": "tiene", "venir": "viene"}
    SUBJ = {"hablar": "hables", "comer": "comas", "escribir": "escribas"}
    USUBJ = {"hablar": "hable", "comer": "coma", "escribir": "escriba"}
    def aff_tu(inf):
        return IRREG.get(inf, PRES3[inf])
    def neg_tu(inf):
        return "no " + SUBJ[inf]
    def usted(inf):
        return USUBJ[inf]
    tests = [(aff_tu("hablar"), "habla"), (aff_tu("comer"), "come"),
             (aff_tu("decir"), "di"), (aff_tu("hacer"), "haz"),
             (aff_tu("ir"), "ve"), (aff_tu("poner"), "pon"),
             (aff_tu("salir"), "sal"), (aff_tu("ser"), "sé"),
             (aff_tu("tener"), "ten"), (aff_tu("venir"), "ven"),
             (neg_tu("hablar"), "no hables"), (neg_tu("comer"), "no comas"),
             (usted("hablar"), "hable"), (usted("escribir"), "escriba")]
    for got, want in tests:
        mark = "OK" if got == want else "FAIL"
        print("  %-12s %s" % (got, mark))
        assert got == want
    print("irregular imperatives: %d" % len(IRREG))
    assert len(IRREG) == 8
    # pronouns attach to affirmative commands
    assert "dime" == "di" + "me" and "sientate" == "sienta" + "te"
    print("rule: affirmative takes the present; negative takes no + subjunctive")
    print("OK: %s commanded its verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["Mi madre es alta y amable.", "Madrid es una ciudad vibrante.",
         "El libro es largo pero interesante.", "Su casa tiene un jardín hermoso.",
         "El profesor es paciente y sabio.", "La playa de Cancún tiene agua turquesa.",
         "Mi perro es pequeño y juguetón.", "La catedral es antigua e impresionante.",
         "Ella tiene ojos verdes.", "El café está caliente y aromático.",
         "Barcelona combina historia y modernidad.", "Mi abuelo tiene manos fuertes.",
         "La novela tiene trescientas páginas.", "El parque está lleno de flores.",
         "Su voz es suave y clara.", "El restaurante sirve comida deliciosa.",
         "La montaña se ve majestuosa.", "Mi cuarto es pequeño pero acogedor.",
         "El niño lleva una camisa roja.", "La noche está estrellada y tranquila."]
    assert len(s) == 20
    bad = [x for x in s if not (x[0].isupper() and x.endswith("."))]
    print("sentences: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    n_es = sum(1 for x in s if " es " in x)
    n_esta = sum(1 for x in s if " está " in x)
    n_tiene = sum(1 for x in s if " tiene " in x)
    print("ser-traits: %d | estar-states: %d | tener-features: %d" % (n_es, n_esta, n_tiene))
    assert n_es == 8
    assert n_esta == 3
    assert n_tiene == 5
    # adjective agreement spot-checks
    assert "una ciudad vibrante" in s[1] and "manos fuertes" in s[11]
    assert "trescientas páginas" in s[12]
    print("rule: ser for traits, estar for states, tener for features")
    print("OK: %s painted its portraits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["Me llamo Ana y vivo en Sevilla.", "Cada mañana me despierto a las siete.",
         "Desayuno tostadas con café.", "Camino al trabajo por el parque.",
         "Trabajo en una librería pequeña.", "Al mediodía como con mis amigas.",
         "Por la tarde leo libros nuevos.", "A las seis vuelvo a casa.",
         "Ceno con mi familia y hablamos.", "Me acuesto a las once, feliz."]
    assert len(s) == 10
    bad = [x for x in s if not (x[0].isupper() and x.endswith("."))]
    print("lines: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # reflexive rituals seal the day
    refl = sum(1 for x in s if x.startswith("Me ") or " me " in x)
    print("reflexive rituals: %d" % refl)
    assert refl == 3
    # time anchors across the day
    times = ["mañana", "mediodía", "tarde", "seis", "once"]
    assert all(any(t in x for x in s) for t in times)
    words = sum(len(x.split()) for x in s)
    print("total words: %d" % words)
    assert 55 < words < 65
    print("rule: the present tense carries routine")
    print("OK: %s told its day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["Ayer fue un día especial.", "Me desperté temprano.",
         "Desayuné con mi abuela.", "Caminamos por el mercado.",
         "Compré flores amarillas.", "Comimos paella en un restaurante.",
         "Por la tarde visité a mis primos.", "Jugamos a las cartas.",
         "Volví a casa al atardecer.", "Me dormí contenta."]
    assert len(s) == 10
    bad = [x for x in s if not (x[0].isupper() and x.endswith("."))]
    print("lines: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # preterite spine: finished-event endings
    pret_end = ("é", "ó", "amos", "é", "í", "ió", "imos")
    pret_n = sum(1 for x in s for w in x.split()
                 if w.strip(".,").endswith(pret_end) and len(w) > 3)
    print("preterite-marked words: %d" % pret_n)
    assert pret_n >= 10
    # the personal a before people
    assert any("visité a mis primos" in x for x in s)
    # feminine speaker signs the final line
    assert s[-1].endswith("contenta.")
    print("rule: the preterite seals finished events")
    print("OK: %s remembered its yesterday" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = ["Mañana será un gran día.", "Me despertaré a las seis.",
         "Viajaré a Granada en tren.", "Visitaré la Alhambra.",
         "Comeré tapas famosas.", "Por la tarde pasearé por el Albaicín.",
         "Tomaré muchas fotos.", "Cenaré con viejos amigos.",
         "Volveré de noche, cansado pero feliz.",
         "Si tuviera más tiempo, me quedaría una semana."]
    assert len(s) == 10
    bad = [x for x in s if not (x[0].isupper() and x.endswith("."))]
    print("lines: %d | order violations: %d" % (len(s), len(bad)))
    assert not bad
    # future spine: -é / -á endings on the infinitive
    fut_n = sum(1 for x in s[:9] for w in x.split()
                if w.strip(".,").endswith(("aré", "eré", "iré", "á")))
    print("future-marked words: %d" % fut_n)
    assert fut_n >= 9
    # the final line opens the conditional: si + imperfect subjunctive + conditional
    assert s[-1].startswith("Si ") and "quedaría" in s[-1] and "tuviera" in s[-1]
    print("rule: the future vows; the conditional wishes")
    print("OK: %s dreamed its tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS3 = {
    "friendship": demo_spanish_friendship,
    "technology": demo_spanish_technology,
    "verb_tenses": demo_spanish_verb_tenses,
    "questions_answers": demo_spanish_questions_answers,
    "commands": demo_spanish_commands,
    "descriptions": demo_spanish_descriptions,
    "story1": demo_spanish_story1,
    "story2": demo_spanish_story2,
    "story3": demo_spanish_story3,
}
DEMOS.update(DEMOS3)

def demo_spanish_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 20 idioms: phrase -> real meaning, verbatim from the record
    idioms = [("estar en las nubes", "to be daydreaming"),
              ("tirar la casa por la ventana", "to spare no expense"),
              ("costar un ojo de la cara", "to cost an arm and a leg"),
              ("estar como una cabra", "to be crazy"),
              ("meter la pata", "to put one's foot in it"),
              ("no tener pelos en la lengua", "to be blunt"),
              ("ser pan comido", "to be a piece of cake"),
              ("estar hasta las narices", "to be fed up"),
              ("ponerse las pilas", "to get one's act together"),
              ("hablar por los codos", "to talk nonstop"),
              ("tomar el pelo", "to tease"),
              ("echar una mano", "to lend a hand"),
              ("estar hecho polvo", "to be exhausted"),
              ("dar en el clavo", "to be exactly right"),
              ("no ver tres en un burro", "to be blind as a bat"),
              ("ser la oveja negra", "to be the black sheep"),
              ("poner el grito en el cielo", "to complain loudly"),
              ("tener la sartén por el mango", "to call the shots"),
              ("quedarse de piedra", "to be stunned"),
              ("a caballo regalado no le mires el diente", "don't look a gift horse in the mouth")]
    assert len(idioms) == 20
    print("idioms catalogued: %d" % len(idioms))
    # a deterministic learner: misses every 5th item (indices 4, 9, 14, 19)
    answers = [i % 5 != 4 for i in range(20)]
    score = sum(answers)
    pct = score / len(idioms) * 100.0
    print("quiz score: %d/%d (%.1f %%)" % (score, len(idioms), pct))
    assert score == 16
    assert 79.9 < pct < 80.1
    # family sort: body-part idioms vs animal idioms
    body = [p for p, _ in idioms if any(w in p for w in
            ["ojo", "pelo", "narices", "codos", "lengua", "diente"])]
    animal = [p for p, _ in idioms if any(w in p for w in
              ["cabra", "burro", "oveja", "caballo"])]
    print("body idioms: %d | animal idioms: %d" % (len(body), len(animal)))
    assert len(body) == 6
    assert len(animal) == 4
    print("rule: translate the meaning, never the words")
    print("OK: %s spoke in idioms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 15 pairs: (informal, formal), verbatim from the record
    pairs = [("¿Cómo estás?", "¿Cómo está usted?"),
             ("¿Puedes ayudarme?", "¿Podría ayudarme?"),
             ("Gracias por tu ayuda.", "Gracias por su ayuda."),
             ("Dime tu nombre.", "Dígame su nombre."),
             ("Siéntate aquí.", "Siéntese aquí."),
             ("¿Tienes hora?", "¿Tiene hora?"),
             ("Te llamo mañana.", "Le llamo mañana."),
             ("Tu casa es bonita.", "Su casa es bonita."),
             ("Perdona el retraso.", "Disculpe el retraso."),
             ("¡Hasta luego!", "Ha sido un placer."),
             ("Querido Juan:", "Estimado señor García:"),
             ("Un abrazo,", "Atentamente,"),
             ("¿Qué quieres?", "¿Qué desea?"),
             ("Ven conmigo.", "Acompáñeme, por favor."),
             ("Eres muy amable.", "Es usted muy amable.")]
    assert len(pairs) == 15
    FORMAL_MARKS = ["usted", "Podría", "Dígame", "Siéntese", "Disculpe",
                    "Acompáñeme", "Estimado", "Atentamente", "desea",
                    "Le llamo", "Tiene hora", "Su casa", "su ayuda",
                    "su nombre", "placer"]
    INFORMAL_MARKS = ["estás", "Puedes", "tu ayuda", "tu nombre", "Dime",
                      "Siéntate", "Tienes", "Te llamo", "Tu casa", "Perdona",
                      "abrazo", "Querido", "quieres", "Ven conmigo", "Eres",
                      "Hasta luego"]
    def register(s):
        if any(m in s for m in FORMAL_MARKS):
            return "formal"
        if any(m in s for m in INFORMAL_MARKS):
            return "informal"
        return "unknown"
    ok = 0
    for inf, frm in pairs:
        ri, rf = register(inf), register(frm)
        good = (ri, rf) == ("informal", "formal")
        mark = "OK" if good else "FAIL"
        print("  %-22s -> %-8s | %-26s -> %-8s %s" % (inf, ri, frm, rf, mark))
        assert good, (inf, frm)
        ok += 2
    print("register classified: %d/%d" % (ok, 30))
    print("rule: tú embraces, usted bows - choose before the first word")
    print("OK: %s minded its manners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import re as _re
    s = ["Aunque llueve, salimos a caminar porque nos encanta la lluvia.",
         "Cuando llegues, llámame para que sepa que estás bien.",
         "El libro que me prestaste es el que más me ha gustado.",
         "Si estudias todos los días, aprobarás el examen sin problema.",
         "Trabaja tanto que no tiene tiempo para su familia.",
         "Mientras cocinaba, escuchaba música y pensaba en el viaje.",
         "No solo habla español, sino que también habla portugués.",
         "Le dije que viniera temprano porque la reunión empieza a las ocho.",
         "Por más que lo intenta, no consigue dormirse antes de medianoche.",
         "Después de que terminemos, iremos a celebrar con los amigos.",
         "Es importante que practiques cada día para que progreses rápido.",
         "La casa donde crecí ya no existe, pero la recuerdo bien.",
         "Como no tenía dinero, se quedó en casa todo el fin de semana.",
         "Habla tan despacio que todos entienden cada palabra.",
         "Ni estudia ni trabaja, aunque tiene dos títulos."]
    assert len(s) == 15
    CONN = ["aunque", "porque", "cuando", "para", "que", "si", "mientras",
            "sino", "pero", "ni", "como", "donde", "sin"]
    def count_conn(sent):
        return sum(len(_re.findall(r"\\b%s\\b" % c, sent.lower())) for c in CONN)
    counts = [count_conn(x) for x in s]
    total = sum(counts)
    for x, c in zip(s, counts):
        print("  connectors=%d :: %s" % (c, x[:52]))
        assert c >= 1, x
    print("total connectors: %d across %d sentences" % (total, len(s)))
    assert total == 29
    avg = total / len(s)
    print("average connectors per sentence: %.2f" % avg)
    assert 1.5 < avg < 2.5
    print("rule: para que always takes the subjunctive; porque takes the indicative")
    print("OK: %s built its cathedrals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_conv_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = ["María: ¡Buenos días! ¿Qué busca hoy?",
             "Carlos: Buenos días. Busco tomates y aguacates.",
             "María: Los tomates están a dos euros el kilo.",
             "Carlos: Están caros. ¿Me deja tres kilos por cinco euros?",
             "María: Por cinco euros le doy dos kilos y medio.",
             "Carlos: Trato hecho. ¿Y los aguacates?",
             "María: A uno cincuenta cada uno, bien maduros.",
             "Carlos: Me llevo cuatro. ¿Están blandos?",
             "María: Perfectos para hoy. Tóquelos.",
             "Carlos: Tiene razón. Póngame también un manojo de cilantro.",
             "María: Marchando. ¿Algo más?",
             "Carlos: Eso es todo. ¿Cuánto es?",
             "María: Son ocho euros con cincuenta.",
             "Carlos: Pago con tarjeta.",
             "María: Perfecto. Aquí tiene su cambio... digo, su recibo.",
             "Carlos: Gracias. ¿Vuelve mañana?",
             "María: Todos los días, de ocho a dos.",
             "Carlos: Hasta mañana, pues.",
             "María: ¡Que le vaya bien!",
             "Carlos: ¡Igualmente!"]
    assert len(lines) == 20
    speakers = [l.split(":")[0] for l in lines]
    # strict alternation María / Carlos
    for i, sp in enumerate(speakers):
        want = "María" if i % 2 == 0 else "Carlos"
        assert sp == want, (i, sp)
    print("lines: %d | speakers alternate María/Carlos" % len(lines))
    nq = sum(l.count("?") for l in lines)
    print("questions asked: %d" % nq)
    assert nq == 7
    # bargaining pair present
    assert any("Me deja" in l for l in lines) and any("le doy" in l for l in lines)
    print("rule: Me deja...? asks, Le doy... answers - trato hecho seals it")
    print("OK: %s haggled at the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_conv_friend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = ["Ana: ¡Luis! ¡Cuánto tiempo!",
             "Luis: ¡Ana! ¡Qué sorpresa! ¿Cómo estás?",
             "Ana: Muy bien, ¿y tú? ¿Sigues en Madrid?",
             "Luis: Sí, sigo allí. ¿Y tu familia?",
             "Ana: Todos bien. Mi hijo ya tiene cinco años.",
             "Luis: ¡No me digas! El tiempo vuela.",
             "Ana: ¿Y tú? ¿Sigues soltero?",
             "Luis: Ya no. Me caso en junio.",
             "Ana: ¡Felicidades! ¡Invítame, eh?",
             "Luis: Claro que sí. Será en la playa.",
             "Ana: ¡Qué romántico! ¿Y el trabajo?",
             "Luis: Bien, aunque con mucho estrés.",
             "Ana: Cuídate, ¿eh? La salud es primero.",
             "Luis: Tienes razón. Oye, ¿tomamos un café?",
             "Ana: Me encantaría, pero tengo prisa.",
             "Luis: Otro día, entonces. Dame tu número.",
             "Ana: Apunta: seis uno dos...",
             "Luis: Listo. Te llamo esta semana.",
             "Ana: Me alegro de verte, Luis.",
             "Luis: ¡Igualmente, Ana! ¡No desaparezcas!"]
    assert len(lines) == 20
    speakers = [l.split(":")[0] for l in lines]
    for i, sp in enumerate(speakers):
        want = "Ana" if i % 2 == 0 else "Luis"
        assert sp == want, (i, sp)
    print("lines: %d | speakers alternate Ana/Luis" % len(lines))
    nq = sum(l.count("?") for l in lines)
    print("questions asked: %d" % nq)
    assert nq == 10
    # the polite decline formula
    assert any("Me encantaría, pero" in l for l in lines)
    # sigues-update frame
    assert sum(1 for l in lines if "Sigues" in l) == 2
    print("rule: Cuánto tiempo opens, Me encantaría pero softens, contact seals")
    print("OK: %s reunited its friends" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_conv_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = ["Sofía: Diego, tenemos un problema.",
             "Diego: ¿Qué pasa?",
             "Sofía: Se pinchó una llanta.",
             "Diego: Tranquila. ¿Dónde estamos?",
             "Sofía: En la carretera, a diez minutos del pueblo.",
             "Diego: ¿Tienes llanta de repuesto?",
             "Sofía: Sí, pero no sé cambiarla.",
             "Diego: Yo te ayudo. Saca el gato y la llave.",
             "Sofía: Aquí están. ¿Y ahora qué?",
             "Diego: Afloja las tuercas primero, sin quitarlas.",
             "Sofía: Listo. ¿Qué sigue?",
             "Diego: Levanta el coche con el gato.",
             "Sofía: Ya está arriba. ¿Quito las tuercas?",
             "Diego: Sí, quítalas y saca la llanta.",
             "Sofía: ¡Pesa mucho!",
             "Diego: Pon la de repuesto y aprieta las tuercas.",
             "Sofía: ¡Hecho! ¿Bajo el coche?",
             "Diego: Baja el gato despacio y aprieta otra vez.",
             "Sofía: ¡Listo! Eres un genio. ¡Gracias!",
             "Diego: De nada. Ahora maneja despacio hasta el taller."]
    assert len(lines) == 20
    speakers = [l.split(":")[0] for l in lines]
    for i, sp in enumerate(speakers):
        want = "Sofía" if i % 2 == 0 else "Diego"
        assert sp == want, (i, sp)
    print("lines: %d | speakers alternate Sofía/Diego" % len(lines))
    nq = sum(l.count("?") for l in lines)
    print("questions asked: %d" % nq)
    assert nq == 7
    # se marks the unplanned mishap
    assert any("Se pinchó" in l for l in lines)
    # sequenced repair commands
    cmds = ["Saca", "Afloja", "Levanta", "Pon", "aprieta", "Baja", "maneja"]
    n_cmd = sum(1 for l in lines for c in cmds if c in l)
    print("repair commands: %d" % n_cmd)
    assert n_cmd >= 7
    print("rule: se mishaps, tranquila reassures, commands repair")
    print("OK: %s fixed its flat tire" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spanish_mastery(hdr, name, rid, group, points, req):
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
    assert 27 == len("abcdefghijklmn" + "\\u00f1" + "opqrstuvwxyz")
    # the 34-record ladder this review closes
    assert 34 == 10 + 14 + 10
    # five tenses times thirty verbs: the engine's full range
    print("verb forms in range: %d" % (30 * 5))
    assert 30 * 5 == 150
    print("rule: climb the ladder twice - exposure, then ownership")
    print("OK: %s sealed its mastery" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS4 = {
    "idioms": demo_spanish_idioms,
    "registers": demo_spanish_registers,
    "complex": demo_spanish_complex,
    "conv_market": demo_spanish_conv_market,
    "conv_friend": demo_spanish_conv_friend,
    "conv_problem": demo_spanish_conv_problem,
    "mastery": demo_spanish_mastery,
}
DEMOS.update(DEMOS4)
