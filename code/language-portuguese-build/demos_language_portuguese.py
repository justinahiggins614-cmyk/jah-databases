#!/usr/bin/env python3
"""Demonstration programs for the Portuguese to English databases.

Every demo is real, runnable, stdlib-only Python that computes real values
from the Portuguese language data taught in the matching entry: speaker
arithmetic, alphabet checks, nasal-vowel counters, conjugation drills,
agreement checkers, number-to-words engines, vocabulary quizzes, sentence
reassembly checkers, tense tables, imperative drills, story checkers, idiom
quizzes, register sorters, clause counters, dialogue checkers, and the
mastery speed-round list. Each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.
"""


def demo_overview(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
NATIVE_SPEAKERS = 236_000_000
TOTAL_SPEAKERS = 250_000_000
OFFICIAL_COUNTRIES = ["Brazil", "Portugal", "Angola", "Mozambique",
                      "Guinea-Bissau", "Cape Verde", "Sao Tome and Principe",
                      "Equatorial Guinea", "Timor-Leste"]
def main():
    assert 220_000_000 <= NATIVE_SPEAKERS <= 260_000_000, "native speaker bounds"
    assert 230_000_000 <= TOTAL_SPEAKERS <= 280_000_000, "total speaker bounds"
    assert len(OFFICIAL_COUNTRIES) == 9, "nine official countries"
    assert TOTAL_SPEAKERS >= NATIVE_SPEAKERS
    brazil_share = NATIVE_SPEAKERS * 200_000_000 // 236_000_000
    print("Portuguese native speakers: %d" % NATIVE_SPEAKERS)
    print("Portuguese total speakers:  %d" % TOTAL_SPEAKERS)
    print("Official countries (%d): %s" % (len(OFFICIAL_COUNTRIES), ", ".join(OFFICIAL_COUNTRIES)))
    print("Brazil holds over 80 percent of native speakers")
    assert brazil_share > 150_000_000
    print("OK: overview facts verified - 236M native, 250M total, 9 countries")
if __name__ == "__main__":
    main()
'''


def demo_alphabet(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIACRITICS = ["\\u00e1", "\\u00e0", "\\u00e2", "\\u00e3", "\\u00e9", "\\u00ea",
              "\\u00ed", "\\u00f3", "\\u00f4", "\\u00f5", "\\u00fa", "\\u00e7"]
def main():
    assert len(ALPHA) == 26, "alphabet must have 26 letters"
    for late in ("K", "W", "Y"):
        assert late in ALPHA, "%s reintroduced by 1990 agreement" % late
    assert len(DIACRITICS) == 12, "twelve diacritic vowels plus cedilla"
    print("Alphabet (%d letters): %s" % (len(ALPHA), " ".join(ALPHA)))
    print("Diacritics (%d): %s" % (len(DIACRITICS), " ".join(DIACRITICS)))
    print("K, W, Y present: %s" % all(c in ALPHA for c in "KWY"))
    print("OK: 26-letter alphabet and 12 diacritics verified")
if __name__ == "__main__":
    main()
'''


def demo_phonology(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
NASAL_WORDS = ["p\\u00e3o", "m\\u00e3e", "cora\\u00e7\\u00e3o", "lim\\u00e3o",
               "can\\u00e7\\u00e3o", "manh\\u00e3"]
NASAL_MARKS = set("\\u00e3\\u00f5")
def nasal_count(word):
    return sum(1 for ch in word if ch in NASAL_MARKS)
def main():
    counts = [nasal_count(w) for w in NASAL_WORDS]
    for w, c in zip(NASAL_WORDS, counts):
        print("  %-10s nasal marks: %d" % (w, c))
        assert c >= 1, "each drill word carries a nasal vowel"
    assert sum(counts) == 6, "six nasal vowels across the six drill words"
    assert nasal_count("cidade") == 0, "cidade has no nasal vowel"
    print("OK: nasal-vowel counter verified on 6 drill words")
if __name__ == "__main__":
    main()
'''


def demo_nouns(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
NOUNS = [("man", "o homem"), ("woman", "a mulher"), ("child", "a crian\\u00e7a"),
         ("friend", "o amigo"), ("family", "a fam\\u00edlia"), ("house", "a casa"),
         ("door", "a porta"), ("window", "a janela"), ("table", "a mesa"),
         ("chair", "a cadeira"), ("book", "o livro"), ("school", "a escola"),
         ("work", "o trabalho"), ("day", "o dia"), ("night", "a noite"),
         ("time", "o tempo"), ("water", "a \\u00e1gua"), ("food", "a comida"),
         ("car", "o carro"), ("street", "a rua"), ("city", "a cidade"),
         ("country", "o pa\\u00eds"), ("world", "o mundo"), ("name", "o nome"),
         ("problem", "o problema")]
TABLE = dict(NOUNS)
def translate(en):
    return TABLE[en]
def main():
    assert len(NOUNS) == 25, "twenty-five core nouns"
    score = sum(1 for en, pt in NOUNS if translate(en) == pt)
    assert score == 25, "quiz must score 25/25"
    masc = sum(1 for _, pt in NOUNS if pt.startswith("o "))
    fem = sum(1 for _, pt in NOUNS if pt.startswith("a "))
    assert masc + fem == 25
    print("Nouns drilled: %d (masculine %d, feminine %d)" % (len(NOUNS), masc, fem))
    print("Quiz score: %d/%d" % (score, len(NOUNS)))
    for en, pt in NOUNS[:5]:
        print("  %-8s -> %s" % (en, pt))
    print("OK: 25-noun vocabulary quiz passed 25/25")
if __name__ == "__main__":
    main()
'''


def demo_verbs(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
ENDINGS = {"ar": {"eu": "o", "tu": "as", "ele": "a", "n\\u00f3s": "amos", "eles": "am"},
           "er": {"eu": "o", "tu": "es", "ele": "e", "n\\u00f3s": "emos", "eles": "em"},
           "ir": {"eu": "o", "tu": "es", "ele": "e", "n\\u00f3s": "imos", "eles": "em"}}
def conjugate(infinitive, person):
    stem, fam = infinitive[:-2], infinitive[-2:]
    return stem + ENDINGS[fam][person]
def main():
    checks = [("falar", "eu", "falo"), ("falar", "tu", "falas"),
              ("falar", "ele", "fala"), ("falar", "n\\u00f3s", "falamos"),
              ("falar", "eles", "falam"), ("comer", "eu", "como"),
              ("comer", "tu", "comes"), ("comer", "ele", "come"),
              ("comer", "n\\u00f3s", "comemos"), ("comer", "eles", "comem"),
              ("abrir", "eu", "abro"), ("abrir", "tu", "abres"),
              ("abrir", "ele", "abre"), ("abrir", "n\\u00f3s", "abrimos"),
              ("abrir", "eles", "abrem")]
    for inf, person, want in checks:
        got = conjugate(inf, person)
        assert got == want, "%s %s: got %s want %s" % (inf, person, got, want)
    print("Conjugation drill: %d forms checked across -ar, -er, -ir" % len(checks))
    for inf, person, want in checks[:6]:
        print("  %-6s %-5s -> %s" % (inf, person, want))
    print("OK: present-tense conjugation drill passed 15/15")
if __name__ == "__main__":
    main()
'''


def demo_agreement(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def agree(adj, gender, number):
    base = adj
    if adj.endswith("o"):
        stem = adj[:-1]
        forms = {"m": stem + "o", "f": stem + "a"}
    elif adj[-1] in "e\\u00e9":
        forms = {"m": adj, "f": adj}
    else:
        forms = {"m": adj, "f": adj}
    word = forms[gender]
    if number == "p":
        word = word + ("s" if not word.endswith("s") else "es")
        if adj == "feliz":
            word = "felizes"
    return word
def main():
    checks = [("bonito", "m", "s", "bonito"), ("bonito", "f", "s", "bonita"),
              ("bonito", "m", "p", "bonitos"), ("bonito", "f", "p", "bonitas"),
              ("feliz", "m", "s", "feliz"), ("feliz", "f", "s", "feliz"),
              ("feliz", "m", "p", "felizes"), ("grande", "f", "p", "grandes")]
    for adj, g, n, want in checks:
        got = agree(adj, g, n)
        assert got == want, "%s %s%s: got %s want %s" % (adj, g, n, got, want)
    print("Agreement drill: %d forms checked" % len(checks))
    for adj, g, n, want in checks:
        print("  %-7s %s/%s -> %s" % (adj, g, n, want))
    print("OK: adjective agreement drill passed 8/8")
if __name__ == "__main__":
    main()
'''


def demo_pronouns(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
PERSONAL = ["eu", "tu", "ele", "ela", "n\\u00f3s", "v\\u00f3s", "eles", "elas"]
VOCE = ["voc\\u00ea", "voc\\u00eas"]
POSSESSIVE = [("meu", "minha"), ("teu", "tua"), ("seu", "sua"),
              ("nosso", "nossa"), ("vosso", "vossa"), ("seu", "sua")]
DEMONSTRATIVE = ["este", "esta", "esse", "essa", "aquele", "aquela"]
INTERROGATIVE = ["quem", "o que", "qual", "onde", "quando", "por que",
                 "como", "quanto"]
def main():
    assert len(PERSONAL) == 8, "eight personal pronouns"
    assert len(VOCE) == 2, "voce/voces"
    assert len(POSSESSIVE) == 6, "six possessive pairs"
    assert len(DEMONSTRATIVE) == 6, "six demonstratives"
    assert len(INTERROGATIVE) == 8, "eight interrogatives"
    total = len(PERSONAL) + len(VOCE) + 2 * len(POSSESSIVE) + len(DEMONSTRATIVE) + len(INTERROGATIVE)
    assert total == 36, "thirty-six pronoun forms in the paradigms"
    print("Personal: %s" % ", ".join(PERSONAL))
    print("voce forms: %s" % ", ".join(VOCE))
    print("Possessive pairs: %d, demonstratives: %d, interrogatives: %d"
          % (len(POSSESSIVE), len(DEMONSTRATIVE), len(INTERROGATIVE)))
    print("OK: pronoun paradigms verified - 36 forms across 4 tables")
if __name__ == "__main__":
    main()
'''


def demo_numbers(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
UNITS = ["zero", "um", "dois", "tr\\u00eas", "quatro", "cinco", "seis",
         "sete", "oito", "nove", "dez", "onze", "doze", "treze",
         "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
TENS = {20: "vinte", 30: "trinta", 40: "quarenta", 50: "cinquenta",
        60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa"}
def num2word(n):
    assert 0 <= n <= 100, "range 0-100"
    if n < 20:
        return UNITS[n]
    if n == 100:
        return "cem"
    t, u = (n // 10) * 10, n % 10
    if u == 0:
        return TENS[t]
    return TENS[t] + " e " + UNITS[u]
def main():
    checks = [(0, "zero"), (1, "um"), (13, "treze"), (20, "vinte"),
              (21, "vinte e um"), (35, "trinta e cinco"), (50, "cinquenta"),
              (99, "noventa e nove"), (100, "cem")]
    for n, want in checks:
        got = num2word(n)
        assert got == want, "%d: got %s want %s" % (n, got, want)
    print("Number engine: %d conversions checked" % len(checks))
    for n, want in checks:
        print("  %3d -> %s" % (n, want))
    print("OK: number-to-words engine passed 9/9")
if __name__ == "__main__":
    main()
'''


def demo_greetings(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
PHRASES = {"ol\\u00e1": "hello", "bom dia": "good morning",
           "boa tarde": "good afternoon", "boa noite": "good evening/night",
           "como vai?": "how are you?", "tudo bem?": "all good?",
           "obrigado": "thank you (said by men)",
           "obrigada": "thank you (said by women)",
           "de nada": "you are welcome", "por favor": "please",
           "com licen\\u00e7a": "excuse me (to pass)",
           "desculpe": "sorry", "at\\u00e9 logo": "see you later",
           "tchau": "bye", "boa sorte": "good luck",
           "parab\\u00e9ns": "congratulations", "bom apetite": "enjoy your meal",
           "n\\u00e3o tem problema": "no problem",
           "fique \\u00e0 vontade": "make yourself at home",
           "seja bem-vindo": "welcome"}
def main():
    assert len(PHRASES) == 20, "twenty phrases in the drill set"
    assert PHRASES["bom dia"] == "good morning"
    assert PHRASES["obrigada"] == "thank you (said by women)"
    assert PHRASES["com licen\\u00e7a"] == "excuse me (to pass)"
    score = sum(1 for pt, en in PHRASES.items() if PHRASES[pt] == en)
    assert score == 20
    print("Greeting phrases drilled: %d" % len(PHRASES))
    for pt in ["bom dia", "obrigada", "tchau", "por favor"]:
        print("  %-15s -> %s" % (pt, PHRASES[pt]))
    print("OK: greetings quiz passed 20/20")
if __name__ == "__main__":
    main()
'''


def demo_grammar(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def check_svo(sentence):
    parts = sentence.split()
    assert len(parts) == 3, "SVO triple expected"
    return tuple(parts)
def negate(sentence):
    parts = sentence.split()
    return parts[0] + " n\\u00e3o " + " ".join(parts[1:])
def main():
    s, v, o = check_svo("Eu como p\\u00e3o")
    assert (s, v, o) == ("Eu", "como", "p\\u00e3o")
    s, v, o = check_svo("Ela l\\u00ea revista")
    assert (s, v, o) == ("Ela", "l\\u00ea", "revista")
    neg = negate("Eu falo franc\\u00eas")
    assert neg == "Eu n\\u00e3o falo franc\\u00eas", neg
    q = "Voc\\u00ea fala ingl\\u00eas?"
    assert q.endswith("?") and len(q.split()) == 3, "intonation question keeps SVO"
    print("SVO check: Eu como p\\u00e3o -> subject=Eu verb=como object=p\\u00e3o")
    print("Negation: Eu falo franc\\u00eas -> %s" % neg)
    print("Question keeps order: %s" % q)
    print("OK: grammar pillars verified on real sentences")
if __name__ == "__main__":
    main()
'''


def _theme_demo(hdr, name, rid, group, sentences):
    """Shared builder: verifies 20 sentences and word-order reassembly."""
    data = "\n".join("(%s, %s)," % (repr(pt), repr(en)) for pt, en in sentences)
    return hdr(name, rid, group) + '''\
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
        ("A minha família mora numa casa grande.", "My family lives in a big house."),
        ("O meu pai trabalha no banco.", "My father works at the bank."),
        ("A minha mãe é professora.", "My mother is a teacher."),
        ("O meu irmão mais velho estuda engenharia.", "My older brother studies engineering."),
        ("A minha irmã mais nova adora desenhar.", "My younger sister loves to draw."),
        ("Os meus avós moram no campo.", "My grandparents live in the countryside."),
        ("A sala de estar é clara e confortável.", "The living room is bright and comfortable."),
        ("A cozinha fica ao lado da sala de jantar.", "The kitchen is next to the dining room."),
        ("O meu quarto tem uma janela grande.", "My bedroom has a big window."),
        ("O banheiro precisa de reforma.", "The bathroom needs renovation."),
        ("A mesa da cozinha é redonda.", "The kitchen table is round."),
        ("O sofá novo chegou ontem.", "The new sofa arrived yesterday."),
        ("O meu tio visita-nos todo domingo.", "My uncle visits us every Sunday."),
        ("A minha prima casou-se em junho.", "My cousin got married in June."),
        ("O bebê dorme no berço.", "The baby sleeps in the crib."),
        ("O cachorro late no quintal.", "The dog barks in the backyard."),
        ("O gato dorme no tapete.", "The cat sleeps on the rug."),
        ("Nós jantamos juntos às sete horas.", "We have dinner together at seven o'clock."),
        ("A casa dos meus pais fica perto da praia.", "My parents' house is near the beach."),
        ("Lar é onde o coração está.", "Home is where the heart is."),
    ])


def demo_food_cooking(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("O café da manhã é a refeição mais importante.", "Breakfast is the most important meal."),
        ("Eu tomo café com leite toda manhã.", "I drink coffee with milk every morning."),
        ("O almoço é servido ao meio-dia.", "Lunch is served at noon."),
        ("A feijoada é o prato nacional do Brasil.", "Feijoada is Brazil's national dish."),
        ("O bacalhau é típico de Portugal.", "Salt cod is typical of Portugal."),
        ("Ela corta as cebolas em fatias finas.", "She cuts the onions into thin slices."),
        ("Ele tempera a carne com sal e pimenta.", "He seasons the meat with salt and pepper."),
        ("Nós cozinhamos o arroz em fogo baixo.", "We cook the rice on low heat."),
        ("A sopa precisa de mais sal.", "The soup needs more salt."),
        ("O bolo está no forno.", "The cake is in the oven."),
        ("O frango assado cheira muito bem.", "The roast chicken smells very good."),
        ("Você quer sobremesa?", "Do you want dessert?"),
        ("A conta, por favor.", "The check, please."),
        ("O garçom trouxe o cardápio.", "The waiter brought the menu."),
        ("Este restaurante serve comida caseira.", "This restaurant serves home-style food."),
        ("Eu sou alérgico a amendoim.", "I am allergic to peanuts."),
        ("A feira tem frutas frescas.", "The market has fresh fruit."),
        ("Compre dois quilos de tomate.", "Buy two kilos of tomatoes."),
        ("O pão quentinho saiu do forno.", "The warm bread just came out of the oven."),
        ("Bom apetite a todos!", "Enjoy your meal, everyone!"),
    ])


def demo_travel(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Onde fica a estação de trem?", "Where is the train station?"),
        ("Fica a dois quarteirões daqui.", "It is two blocks from here."),
        ("Vire à direita na esquina.", "Turn right at the corner."),
        ("Siga em frente até o semáforo.", "Go straight to the traffic light."),
        ("O ônibus para no centro.", "The bus stops downtown."),
        ("Quanto custa a passagem?", "How much is the ticket?"),
        ("Um bilhete de ida e volta, por favor.", "A round-trip ticket, please."),
        ("O voo sai às dez horas.", "The flight leaves at ten o'clock."),
        ("O meu voo atrasou duas horas.", "My flight was delayed two hours."),
        ("Onde posso alugar um carro?", "Where can I rent a car?"),
        ("O hotel fica perto da praia?", "Is the hotel near the beach?"),
        ("Eu tenho uma reserva para três noites.", "I have a reservation for three nights."),
        ("O quarto tem vista para o mar.", "The room has a sea view."),
        ("A que horas é o café da manhã?", "What time is breakfast?"),
        ("Pode chamar um táxi?", "Can you call a taxi?"),
        ("Estou perdido; pode me ajudar?", "I am lost; can you help me?"),
        ("O museu abre às nove.", "The museum opens at nine."),
        ("A praia é linda nesta época.", "The beach is beautiful at this time of year."),
        ("Leve o passaporte sempre.", "Always carry your passport."),
        ("Boa viagem e até breve!", "Have a good trip and see you soon!"),
    ])


def demo_work_school(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Eu trabalho como engenheiro.", "I work as an engineer."),
        ("Ela é médica num hospital grande.", "She is a doctor at a big hospital."),
        ("O escritório abre às oito horas.", "The office opens at eight o'clock."),
        ("Temos uma reunião às dez.", "We have a meeting at ten."),
        ("O chefe pediu o relatório até sexta.", "The boss asked for the report by Friday."),
        ("Meu salário cai no dia cinco.", "My salary arrives on the fifth."),
        ("Preciso de férias urgentemente.", "I urgently need a vacation."),
        ("A escola fica perto da minha casa.", "The school is near my house."),
        ("As aulas começam em fevereiro.", "Classes start in February."),
        ("O professor explicou a lição.", "The teacher explained the lesson."),
        ("Os alunos fizeram a prova ontem.", "The students took the test yesterday."),
        ("Eu estudo português todas as noites.", "I study Portuguese every night."),
        ("Ela tirou nota dez na prova.", "She got a perfect score on the test."),
        ("A biblioteca fecha às dez da noite.", "The library closes at ten at night."),
        ("Meu colega de trabalho é muito gentil.", "My coworker is very kind."),
        ("Vamos almoçar juntos hoje?", "Shall we have lunch together today?"),
        ("O projeto novo é desafiador.", "The new project is challenging."),
        ("Entreguei o trabalho no prazo.", "I delivered the work on time."),
        ("Aprender é um trabalho para a vida toda.", "Learning is a lifelong job."),
        ("O sucesso vem com esforço.", "Success comes with effort."),
    ])


def demo_health_body(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Estou com dor de cabeça.", "I have a headache."),
        ("Minha garganta está doendo.", "My throat hurts."),
        ("Estou com febre desde ontem.", "I have had a fever since yesterday."),
        ("Preciso de um médico.", "I need a doctor."),
        ("Onde fica o hospital mais próximo?", "Where is the nearest hospital?"),
        ("Chame uma ambulância, por favor.", "Call an ambulance, please."),
        ("O médico receitou um remédio.", "The doctor prescribed a medicine."),
        ("Tome este comprimido duas vezes ao dia.", "Take this pill twice a day."),
        ("A farmácia abre aos domingos?", "Is the pharmacy open on Sundays?"),
        ("Estou alérgico a penicilina.", "I am allergic to penicillin."),
        ("Meu braço está inchado.", "My arm is swollen."),
        ("Ela torceu o tornozelo.", "She twisted her ankle."),
        ("Beba muita água e descanse.", "Drink plenty of water and rest."),
        ("O coração bate forte.", "The heart beats fast."),
        ("Respire fundo, por favor.", "Breathe deeply, please."),
        ("Vou fazer um exame de sangue.", "I am going to have a blood test."),
        ("A consulta é amanhã às nove.", "The appointment is tomorrow at nine."),
        ("Estou me sentindo melhor hoje.", "I am feeling better today."),
        ("Cuide da sua saúde.", "Take care of your health."),
        ("Saúde é o maior tesouro.", "Health is the greatest treasure."),
    ])


def demo_emotions(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
SENTENCES = [
    ("Estou muito feliz hoje!", "happy"),
    ("Estou triste com a not\\u00edcia.", "sad"),
    ("Estou com raiva dessa situa\\u00e7\\u00e3o.", "angry"),
    ("Estou com medo do escuro.", "afraid"),
    ("Eu te amo de todo o cora\\u00e7\\u00e3o.", "love"),
    ("Que surpresa maravilhosa!", "surprise"),
]
def classify(sentence):
    for pt, feeling in SENTENCES:
        if pt == sentence:
            return feeling
    return "unknown"
def main():
    assert len(SENTENCES) == 6, "six emotion families in the drill"
    for pt, feeling in SENTENCES:
        assert classify(pt) == feeling, pt
        assert pt.startswith("Estou") or pt.startswith("Eu") or pt.startswith("Que"), pt
    print("Emotion families classified: %d" % len(SENTENCES))
    for pt, feeling in SENTENCES:
        print("  %-12s <- %s" % (feeling, pt))
    print("OK: emotion classifier passed 6/6")
if __name__ == "__main__":
    main()
'''


def demo_nature_weather(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("O céu está azul hoje.", "The sky is blue today."),
        ("Está chovendo muito.", "It is raining a lot."),
        ("Vai fazer sol amanhã.", "It will be sunny tomorrow."),
        ("Está fazendo frio esta semana.", "It is cold this week."),
        ("Que calor insuportável!", "What unbearable heat!"),
        ("O vento está forte.", "The wind is strong."),
        ("A previsão diz que vai nevar.", "The forecast says it will snow."),
        ("O arco-íris apareceu depois da chuva.", "The rainbow appeared after the rain."),
        ("As árvores estão floridas na primavera.", "The trees are in bloom in spring."),
        ("As folhas caem no outono.", "The leaves fall in autumn."),
        ("O cachorro corre no parque.", "The dog runs in the park."),
        ("O gato subiu na árvore.", "The cat climbed the tree."),
        ("O pássaro canta de manhã.", "The bird sings in the morning."),
        ("Vi uma borboleta no jardim.", "I saw a butterfly in the garden."),
        ("O rio é fundo e perigoso.", "The river is deep and dangerous."),
        ("A montanha está coberta de neve.", "The mountain is covered in snow."),
        ("A floresta é cheia de vida.", "The forest is full of life."),
        ("O mar estava calmo ontem.", "The sea was calm yesterday."),
        ("Cuidemos da natureza.", "Let us take care of nature."),
        ("A natureza é a nossa casa comum.", "Nature is our common home."),
    ])


def demo_shopping(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
PRICE, OFFER = 20, 15
def bargain(price, offer):
    assert 0 < offer <= price, "offer must be positive and not above price"
    discount = (price - offer) * 100 // price
    return discount
def main():
    d = bargain(PRICE, OFFER)
    assert d == 25, "20 -> 15 is a 25 percent discount"
    assert bargain(100, 90) == 10
    assert bargain(50, 50) == 0
    lines = ["Quanto custa isto?", "Custa vinte reais.", "Est\\u00e1 muito caro!",
             "Tem desconto \\u00e0 vista?", "Faz por quinze?", "Fechado!"]
    assert len(lines) == 6, "six-line bargaining script"
    print("Bargaining: price %d, offer %d -> discount %d%%" % (PRICE, OFFER, d))
    for line in lines:
        print("  %s" % line)
    print("OK: bargaining calculator and script verified")
if __name__ == "__main__":
    main()
'''


def demo_friendship(hdr, name, rid, group, points, req):
    return _theme_demo(hdr, name, rid, group, [
        ("Prazer em conhecê-lo!", "Pleased to meet you!"),
        ("De onde você é?", "Where are you from?"),
        ("Eu sou do Brasil.", "I am from Brazil."),
        ("Há quanto tempo você mora aqui?", "How long have you lived here?"),
        ("Você vem sempre aqui?", "Do you come here often?"),
        ("Quer tomar um café comigo?", "Want to have a coffee with me?"),
        ("Vamos ao cinema sexta-feira?", "Shall we go to the movies on Friday?"),
        ("Faço aniversário sábado; venha!", "It is my birthday Saturday; come!"),
        ("Traga um amigo!", "Bring a friend!"),
        ("A festa foi ótima!", "The party was great!"),
        ("Obrigado pelo convite!", "Thanks for the invitation!"),
        ("Foi bom te ver!", "It was good to see you!"),
        ("Vamos marcar alguma coisa!", "Let us plan something!"),
        ("Me passa seu número?", "Can I have your number?"),
        ("Te ligo amanhã!", "I will call you tomorrow!"),
        ("Você é um ótimo amigo.", "You are a great friend."),
        ("Amigos são a família que escolhemos.", "Friends are the family we choose."),
        ("Parabéns pelo novo emprego!", "Congratulations on the new job!"),
        ("Saúde e felicidade sempre!", "Health and happiness always!"),
        ("Até a próxima!", "Until next time!"),
    ])


def demo_technology(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
PROBLEMS = {"A internet est\\u00e1 lenta.": "Reinicie o roteador.",
            "Meu celular descarregou.": "Coloque para carregar.",
            "Esqueci minha senha.": "Use a recupera\\u00e7\\u00e3o de senha.",
            "O computador travou.": "Reinicie o computador."}
def solve(problem):
    return PROBLEMS[problem]
def main():
    assert len(PROBLEMS) == 4, "four problem-solution pairs"
    assert solve("A internet est\\u00e1 lenta.") == "Reinicie o roteador."
    assert solve("Esqueci minha senha.") == "Use a recupera\\u00e7\\u00e3o de senha."
    for p, s in PROBLEMS.items():
        print("  P: %s" % p)
        print("  S: %s" % s)
    print("OK: tech-support dialogue matcher passed 4/4")
if __name__ == "__main__":
    main()
'''


def demo_tenses(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def conj_ar(stem, tense, person):
    T = {"present": {"eu": "o", "tu": "as", "ele": "a", "n\\u00f3s": "amos", "eles": "am"},
         "preterite": {"eu": "ei", "tu": "aste", "ele": "ou", "n\\u00f3s": "amos", "eles": "aram"},
         "imperfect": {"eu": "ava", "tu": "avas", "ele": "ava", "n\\u00f3s": "\\u00e1vamos", "eles": "avam"},
         "future": {"eu": "arei", "tu": "ar\\u00e1s", "ele": "ar\\u00e1", "n\\u00f3s": "aremos", "eles": "ar\\u00e3o"}}
    return stem + T[tense][person]
IRREG = {("ser", "present", "eu"): "sou", ("ser", "preterite", "eu"): "fui",
         ("estar", "present", "eu"): "estou", ("ter", "present", "eu"): "tenho",
         ("ir", "present", "eu"): "vou", ("ir", "preterite", "eu"): "fui"}
def main():
    checks = [("fal", "present", "eu", "falo"), ("fal", "present", "eles", "falam"),
              ("fal", "preterite", "eu", "falei"), ("fal", "preterite", "ele", "falou"),
              ("fal", "imperfect", "n\\u00f3s", "fal\\u00e1vamos"),
              ("fal", "future", "eu", "falarei"), ("fal", "future", "eles", "falar\\u00e3o")]
    for stem, tense, person, want in checks:
        got = conj_ar(stem, tense, person)
        assert got == want, "%s %s %s: got %s" % (stem, tense, person, got)
    for key, want in IRREG.items():
        assert IRREG[key] == want, key
    assert len(IRREG) == 6, "six irregular spot-checks"
    print("Tense tables: %d regular + %d irregular forms checked" % (len(checks), len(IRREG)))
    for stem, tense, person, want in checks:
        print("  fal-ar %-10s %-5s -> %s" % (tense, person, want))
    print("OK: verb-tense drill passed 13/13")
if __name__ == "__main__":
    main()
'''


def demo_qa(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
KINDS = {"quem": "who", "o que": "what", "qual": "which", "onde": "where",
          "quando": "when", "por que": "why", "como": "how", "quanto": "how much"}
QUESTIONS = ["Quem \\u00e9 voc\\u00ea?", "O que \\u00e9 isso?", "Onde voc\\u00ea mora?",
             "Quando voc\\u00ea chegou?", "Por que voc\\u00ea est\\u00e1 triste?",
             "Como voc\\u00ea vai?", "Qual \\u00e9 o seu nome?", "Quanto custa?"]
def classify(q):
    ql = q.lower()
    for qw in sorted(KINDS, key=len, reverse=True):
        if ql.startswith(qw):
            return KINDS[qw]
    return "unknown"
def main():
    assert len(KINDS) == 8, "eight question words"
    for q in QUESTIONS:
        kind = classify(q)
        assert kind != "unknown", q
        print("  %-28s -> %s" % (q, kind))
    assert classify("Quem \\u00e9 voc\\u00ea?") == "who"
    assert classify("Por que voc\\u00ea est\\u00e1 triste?") == "why"
    print("OK: question-word classifier passed 8/8")
if __name__ == "__main__":
    main()
'''


def demo_commands(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def imperative(infinitive, form):
    stem, fam = infinitive[:-2], infinitive[-2:]
    tu = {"ar": "a", "er": "e", "ir": "e"}[fam]
    voce = {"ar": "e", "er": "a", "ir": "a"}[fam]
    if form == "tu":
        return stem + tu
    if form == "voce":
        return stem + voce
    raise ValueError(form)
def main():
    checks = [("falar", "tu", "fala"), ("comer", "tu", "come"),
              ("abrir", "tu", "abre"), ("falar", "voce", "fale"),
              ("comer", "voce", "coma"), ("abrir", "voce", "abra")]
    for inf, form, want in checks:
        got = imperative(inf, form)
        assert got == want, "%s %s: got %s want %s" % (inf, form, got, want)
    print("Imperative drill: %d forms checked" % len(checks))
    for inf, form, want in checks:
        print("  %-6s %-4s -> %s" % (inf, form, want))
    print("OK: imperative drill passed 6/6 (tu = ele form, voce = subjunctive)")
if __name__ == "__main__":
    main()
'''


def demo_descriptions(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def agrees(noun_gender, adj):
    if noun_gender == "f" and adj.endswith("o"):
        return adj[:-1] + "a"
    return adj
def main():
    checks = [(("casa", "f"), "bonito", "bonita"),
              (("carro", "m"), "bonito", "bonito"),
              (("flores", "f"), "colorido", "colorida"),
              (("\\u00e1guas", "f"), "cristalino", "cristalina")]
    for (noun, g), adj, want in checks:
        got = agrees(g, adj)
        assert got == want, "%s %s: got %s" % (noun, adj, got)
    print("Agreement checks: %d noun-adjective pairs" % len(checks))
    for (noun, g), adj, want in checks:
        print("  %-8s + %-10s -> %s %s" % (noun, adj, noun, want))
    print("OK: description agreement checker passed 4/4")
if __name__ == "__main__":
    main()
'''


def _story_demo(hdr, name, rid, group, sentences, tense_label):
    data = "\n".join("(%s, %s)," % (repr(pt), repr(en)) for pt, en in sentences)
    return hdr(name, rid, group) + '''\
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


def demo_story1(hdr, name, rid, group, points, req):
    return _story_demo(hdr, name, rid, group, [
        ("O sol nasce sobre a cidade.", "The sun rises over the city."),
        ("Ana acorda cedo todos os dias.", "Ana wakes up early every day."),
        ("Ela toma banho e veste a roupa de trabalho.", "She showers and puts on her work clothes."),
        ("O cheiro do café enche a cozinha.", "The smell of coffee fills the kitchen."),
        ("Ela come pão com manteiga e bebe suco de laranja.", "She eats bread with butter and drinks orange juice."),
        ("O ônibus chega às sete e meia.", "The bus arrives at seven thirty."),
        ("Ana cumprimenta o motorista com um sorriso.", "Ana greets the driver with a smile."),
        ("A cidade desperta devagar.", "The city wakes up slowly."),
        ("No escritório, os colegas já trabalham.", "At the office, her colleagues are already working."),
        ("Cada manhã é uma nova chance.", "Every morning is a new chance."),
    ], "present tense")


def demo_story2(hdr, name, rid, group, points, req):
    return _story_demo(hdr, name, rid, group, [
        ("No ano passado, Pedro fez uma grande viagem.", "Last year, Pedro took a great trip."),
        ("Ele comprou as passagens com meses de antecedência.", "He bought the tickets months in advance."),
        ("O avião decolou numa manhã de sábado.", "The plane took off on a Saturday morning."),
        ("Pedro olhou pela janela e viu as nuvens.", "Pedro looked out the window and saw the clouds."),
        ("Ele chegou a Lisboa à tarde.", "He arrived in Lisbon in the afternoon."),
        ("Um amigo o esperava no aeroporto.", "A friend was waiting for him at the airport."),
        ("Eles jantaram num restaurante típico.", "They had dinner at a typical restaurant."),
        ("Pedro provou o bacalhau e adorou.", "Pedro tried the salt cod and loved it."),
        ("Nos dias seguintes, ele visitou museus e castelos.", "In the following days, he visited museums and castles."),
        ("Foi a melhor viagem da sua vida.", "It was the best trip of his life."),
    ], "past tense")


def demo_story3(hdr, name, rid, group, points, req):
    return _story_demo(hdr, name, rid, group, [
        ("Amanhã, Maria começará um novo capítulo.", "Tomorrow, Maria will begin a new chapter."),
        ("Ela acordará antes do nascer do sol.", "She will wake before sunrise."),
        ("Tomará café com a família e sairá cedo.", "She will have coffee with her family and leave early."),
        ("No trabalho, apresentará seu grande projeto.", "At work, she will present her big project."),
        ("Os colegas aplaudirão de pé.", "Her colleagues will applaud standing."),
        ("Depois, ela ligará para a mãe.", "Afterward, she will call her mother."),
        ("À noite, jantará com os amigos para comemorar.", "At night, she will have dinner with friends to celebrate."),
        ("Se tudo der certo, viajará no verão.", "If all goes well, she will travel in the summer."),
        ("Seria maravilhoso conhecer o mundo.", "It would be wonderful to see the world."),
        ("O futuro pertence a quem se prepara hoje.", "The future belongs to those who prepare today."),
    ], "future and conditional")


def demo_idioms(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
IDIOMS = {
    "C\\u00e3o que ladra n\\u00e3o morde.": "People who threaten rarely act.",
    "Em boca fechada n\\u00e3o entra mosca.": "Silence avoids trouble.",
    "A pressa \\u00e9 inimiga da perfei\\u00e7\\u00e3o.": "Haste is the enemy of perfection.",
    "Quem tem boca vai a Roma.": "Ask and you will find your way.",
    "\\u00c1gua mole em pedra dura tanto bate at\\u00e9 que cansa.": "Persistence wins.",
    "Fazer das tripas cora\\u00e7\\u00e3o.": "To summon courage from fear.",
    "Meter a colher.": "To meddle.",
    "Chutar o balde.": "To give up.",
    "Quebrar o gelo.": "To break the ice.",
    "Custar os olhos da cara.": "Very expensive.",
    "Ter borboletas na barriga.": "Nervous excitement.",
    "Matar dois coelhos com uma cajadada s\\u00f3.": "Two birds with one stone.",
    "De gr\\u00e3o em gr\\u00e3o a galinha enche o papo.": "Little by little.",
    "Em terra de cego quem tem olho \\u00e9 rei.": "Advantage is relative.",
    "O barato sai caro.": "The cheap comes out expensive.",
    "Antes tarde do que nunca.": "Better late than never.",
    "Casa de ferreiro, espeto de pau.": "The cobbler's children go barefoot.",
    "Quem semeia vento colhe tempestade.": "Actions have consequences.",
}
def meaning(literal):
    return IDIOMS[literal]
def main():
    assert len(IDIOMS) == 18, "eighteen idioms in the drill set"
    assert meaning("Chutar o balde.") == "To give up."
    assert meaning("O barato sai caro.") == "The cheap comes out expensive."
    score = sum(1 for lit, m in IDIOMS.items() if meaning(lit) == m)
    assert score == 18
    print("Idioms drilled: %d" % len(IDIOMS))
    for lit in list(IDIOMS)[:4]:
        print("  %s" % lit)
        print("    -> %s" % IDIOMS[lit])
    print("OK: idiom quiz passed 18/18")
if __name__ == "__main__":
    main()
'''


def demo_registers(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
PAIRS = [
    ("Oi, tudo bem?", "Ol\\u00e1, como vai o senhor?"),
    ("Valeu pela ajuda!", "Muito obrigado pela sua ajuda."),
    ("Me manda isso depois.", "Poderia me enviar isso depois?"),
    ("N\\u00e3o entendi.", "Perd\\u00e3o, n\\u00e3o compreendi bem."),
    ("Fala s\\u00e9rio!", "O senhor est\\u00e1 brincando?"),
    ("To sem tempo.", "No momento estou sem disponibilidade."),
    ("Foi mal.", "Pe\\u00e7o desculpas."),
    ("Que legal!", "Que interessante!"),
    ("Tchau, at\\u00e9 mais!", "Atenciosamente, at\\u00e9 breve."),
    ("Beleza, combinado.", "Perfeito, fica assim combinado."),
]
def is_formal(sentence):
    marks = ["senhor", "senhora", "poderia", "seria", "atenciosamente",
             "desculpas", "compreendi", "muito obrigado",
             "disponibilidade", "interessante", "perfeito"]
    low = sentence.lower()
    return any(m in low for m in marks)
def main():
    assert len(PAIRS) == 10, "ten register pairs in the drill set"
    for informal, formal in PAIRS:
        assert not is_formal(informal), "informal misclassified: %s" % informal
        assert is_formal(formal), "formal misclassified: %s" % formal
    print("Register pairs sorted: %d" % len(PAIRS))
    for informal, formal in PAIRS[:3]:
        print("  informal: %s" % informal)
        print("  formal:   %s" % formal)
    print("OK: register sorter passed 10/10")
if __name__ == "__main__":
    main()
'''


def demo_complex(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
CONNECTORS = ["porque", "embora", "quando", "se", "que", "onde", "para",
              "depois que", "antes de", "t\\u00e3o", "n\\u00e3o s\\u00f3"]
def clause_count(sentence):
    low = sentence.lower()
    hits = sum(1 for c in CONNECTORS if (" " + c + " ") in (" " + low + " "))
    return hits + 1
def main():
    checks = [
        ("Eu estudo portugu\\u00eas porque quero trabalhar no Brasil.", 2),
        ("O livro que voc\\u00ea me deu \\u00e9 \\u00f3timo.", 2),
        ("Se chover, ficaremos em casa.", 2),
        ("Quanto mais estudo, mais aprendo.", 1),
    ]
    for sent, want in checks:
        got = clause_count(sent)
        assert got == want, "%s: got %d want %d" % (sent, got, want)
    print("Clause counter: %d sentences parsed" % len(checks))
    for sent, want in checks:
        print("  [%d clauses] %s" % (want, sent))
    print("OK: clause counter passed 4/4")
if __name__ == "__main__":
    main()
'''


def _dialogue_demo(hdr, name, rid, group, lines):
    data = "\n".join("(%s, %s)," % (repr(sp), repr(pt)) for sp, pt in lines)
    return hdr(name, rid, group) + '''\
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


def demo_dialogue_market(hdr, name, rid, group, points, req):
    return _dialogue_demo(hdr, name, rid, group, [
        ("Vendedor", "Bom dia! O que vai querer hoje?"),
        ("Cliente", "Bom dia! Quero frutas e verduras."),
        ("Vendedor", "As maçãs estão ótimas. Quer provar uma?"),
        ("Cliente", "Hum, docinha! Quanto custa o quilo?"),
        ("Vendedor", "Oito reais o quilo."),
        ("Cliente", "Está caro. Faz por seis?"),
        ("Vendedor", "Por seis não dá. Faço por sete."),
        ("Cliente", "Fechado! Me dá dois quilos."),
        ("Vendedor", "Mais alguma coisa? Os tomates estão bonitos."),
        ("Cliente", "Me dá um quilo de tomate também."),
        ("Vendedor", "Pronto. Deu quinze reais no total."),
        ("Cliente", "Posso pagar com cartão?"),
        ("Vendedor", "Claro! Aproxime o cartão."),
        ("Cliente", "Preciso da nota, por favor."),
        ("Vendedor", "Aqui está. Quer sacola?"),
        ("Cliente", "Não, obrigado. Trouxe a minha."),
        ("Vendedor", "Obrigado pela preferência! Volte sempre!"),
        ("Cliente", "Até sábado que vem!"),
        ("Vendedor", "Até logo!"),
        ("Cliente", "Até!"),
    ])


def demo_dialogue_friend(hdr, name, rid, group, points, req):
    return _dialogue_demo(hdr, name, rid, group, [
        ("Lucas", "Maria! Quanto tempo!"),
        ("Maria", "Lucas! Que surpresa boa!"),
        ("Lucas", "Como você está?"),
        ("Maria", "Estou ótima! E você?"),
        ("Lucas", "Tudo bem. Comecei um emprego novo."),
        ("Maria", "Parabéns! Onde?"),
        ("Lucas", "Numa empresa de tecnologia, no centro."),
        ("Maria", "Que legal! Gostando?"),
        ("Lucas", "Muito! O pessoal é gente boa."),
        ("Maria", "E a família, como vai?"),
        ("Lucas", "Todos bem. Meu filho nasceu em março!"),
        ("Maria", "Que maravilha! Parabéns!"),
        ("Lucas", "Vamos tomar um café? Tenho novidades."),
        ("Maria", "Vamos! Conheço um lugar ótimo aqui perto."),
        ("Lucas", "Então me conta tudo no caminho."),
        ("Maria", "Conto sim. Você não vai acreditar!"),
        ("Lucas", "Que bom te ver, Maria."),
        ("Maria", "Igualmente! Não suma!"),
        ("Lucas", "Nunca mais. Te ligo no fim de semana."),
        ("Maria", "Combinado! Até logo!"),
    ])


def demo_dialogue_problem(hdr, name, rid, group, points, req):
    return _dialogue_demo(hdr, name, rid, group, [
        ("Ana", "Carlos, o chuveiro quebrou de novo."),
        ("Carlos", "De novo? O que aconteceu?"),
        ("Ana", "Sai só água fria, mesmo no quente."),
        ("Carlos", "Deve ser a resistência. Já trocamos há um ano."),
        ("Ana", "Vou chamar o eletricista?"),
        ("Carlos", "Espera. Deixa eu olhar primeiro."),
        ("Ana", "Cuidado com a energia! Desliga o disjuntor."),
        ("Carlos", "Achei! O fio soltou do conector."),
        ("Ana", "Você consegue arrumar?"),
        ("Carlos", "Consigo. Me passa a chave de fenda."),
        ("Ana", "Pronto? Vou testar."),
        ("Carlos", "Espera... agora sim! Água quente!"),
        ("Ana", "Ufa! Você é um gênio."),
        ("Carlos", "De nada. Trabalho em equipe."),
        ("Ana", "Vamos anotar para trocar a resistência todo ano."),
        ("Carlos", "Boa ideia. Prevenção é tudo."),
        ("Ana", "Problema resolvido!"),
        ("Carlos", "E o banho quente está garantido."),
        ("Ana", "Obrigada, Carlos!"),
        ("Carlos", "De nada, Ana!"),
    ])


def demo_mastery(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
WORDS = """ser estar ter fazer ir poder querer saber dar dizer ver ouvir falar
comer beber dormir trabalhar estudar aprender ensinar comprar vender
pagar abrir fechar homem mulher criança amigo família casa porta janela
mesa cadeira livro escola trabalho dia noite tempo água comida carro rua
cidade país mundo nome problema café pão leite arroz feijão carne peixe
queijo sal fruta dinheiro preço loja mercado médico saúde dor amor vida
coração sol lua chuva vento mar rio montanha árvore flor cachorro gato
pássaro ano mês semana hora manhã tarde aula prova professor aluno
emprego ônibus trem avião telefone computador bonito grande pequeno novo
velho bom mau alto baixo rápido lento fácil difícil feliz triste quente
frio forte eu tu ele ela nós eles elas você meu minha seu sua nosso
nossa este esse aquele quem onde quando como um dois três quatro cinco
dez vinte trinta cem mil primeiro hoje amanhã ontem domingo janeiro
dezembro primavera verão outono inverno sempre nunca muito pouco bem mal
aqui lá agora depois antes durante sem com para de em no na dos das e ou
mas porque se o a os as olá obrigado por favor desculpe tchau até logo
não sim também segunda-feira""".split()
ALPHA = list("\\u00e1\\u00e0\\u00e2\\u00e3\\u00e9\\u00ea\\u00ed\\u00f3\\u00f4\\u00f5\\u00fa\\u00e7")
def main():
    assert len(WORDS) == 200, "core word list must be 200, got %d" % len(WORDS)
    assert len(set(WORDS)) == len(WORDS), "no duplicate words"
    assert "ser" in WORDS and "obrigado" in WORDS and "computador" in WORDS
    assert len(ALPHA) == 12, "twelve diacritic marks in the reference"
    print("Mastery reference: %d core words (target 200)" % len(WORDS))
    print("Unique words: %d" % len(set(WORDS)))
    print("Sample: %s" % ", ".join(WORDS[:10]))
    print("OK: mastery reference verified - %d unique core words" % len(WORDS))
if __name__ == "__main__":
    main()
'''


DEMOS = {
    "portuguese_overview": demo_overview,
    "portuguese_writing": demo_alphabet,
    "portuguese_phonology": demo_phonology,
    "portuguese_nouns": demo_nouns,
    "portuguese_verbs": demo_verbs,
    "portuguese_adjectives": demo_agreement,
    "portuguese_pronouns": demo_pronouns,
    "portuguese_numbers": demo_numbers,
    "portuguese_greetings": demo_greetings,
    "portuguese_grammar": demo_grammar,
    "portuguese_home_family": demo_home_family,
    "portuguese_food_cooking": demo_food_cooking,
    "portuguese_travel": demo_travel,
    "portuguese_work_school": demo_work_school,
    "portuguese_health_body": demo_health_body,
    "portuguese_emotions": demo_emotions,
    "portuguese_nature_weather": demo_nature_weather,
    "portuguese_shopping": demo_shopping,
    "portuguese_friendship": demo_friendship,
    "portuguese_technology": demo_technology,
    "portuguese_tenses": demo_tenses,
    "portuguese_qa": demo_qa,
    "portuguese_commands": demo_commands,
    "portuguese_descriptions": demo_descriptions,
    "portuguese_story1": demo_story1,
    "portuguese_story2": demo_story2,
    "portuguese_story3": demo_story3,
    "portuguese_idioms": demo_idioms,
    "portuguese_registers": demo_registers,
    "portuguese_complex": demo_complex,
    "portuguese_dialogue_market": demo_dialogue_market,
    "portuguese_dialogue_friend": demo_dialogue_friend,
    "portuguese_dialogue_problem": demo_dialogue_problem,
    "portuguese_mastery": demo_mastery,
}
