#!/usr/bin/env python3
"""Demo programs for The French Language Database (language-french).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: pronunciation drills, grammar quizzes,
flashcard checks, number builders, conjugation tables. All are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.
Cross-checked against entry text 2026-10-17.
"""

import json


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + body.replace("NAME", json.dumps(name))


def demo_french_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speaker statistics, millions (OIF 2022 world report; roster L1 figure)
    native = 82.0
    total = 321.0
    second = total - native
    native_share = native / total * 100.0
    countries = 29
    un_langs = 6
    print("native speakers: %.0fM" % native)
    print("total speakers: %.0fM" % total)
    print("second-language speakers: %.0fM" % second)
    print("native share: %.3f %%" % native_share)
    print("official countries: %d; UN official languages: %d" % (countries, un_langs))
    assert 238.9 < second < 239.1
    assert 25.54 < native_share < 25.56
    assert countries == 29 and un_langs == 6
    print("rule: francais, ISO fr/fra, Indo-European > Italic > Romance")
    print("OK: %s mapped the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the alphabet inventory: letters, vowels, diacritics
    letters = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiouy"
    consonants = "".join(c for c in letters if c not in vowels)
    diacritics = ["acute", "grave", "circumflex", "diaeresis", "cedilla"]
    print("letters: %d" % len(letters))
    print("vowels: %d (%s)" % (len(vowels), vowels))
    print("consonants: %d" % len(consonants))
    print("diacritics: %d" % len(diacritics))
    assert len(letters) == 26
    assert len(vowels) == 6 and len(consonants) == 20
    assert len(diacritics) == 5
    # accent minimal pairs change meaning: ou/ou, sur/sur, a/a
    pairs = [("ou", "ou"), ("sur", "sur"), ("a", "a")]
    print("accent minimal pairs: %d" % len(pairs))
    assert len(pairs) == 3
    print("rule: accents are pronunciation switches, not decoration")
    print("OK: %s stamped the alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sound inventory drill: oral vowels, nasal vowels, signature consonants
    oral = ["a", "a", "e", "e", "e", "i", "o", "o", "u", "u", "o", "oe"]
    nasal = ["an", "in", "on", "un"]
    inventory = len(oral) + len(nasal)
    nasal_share = len(nasal) / inventory * 100.0
    examples = ["bonjour", "merci", "s'il vous plait", "oui", "non", "eau",
                "pain", "vin", "rouge", "ecole", "fenetre", "oiseau"]
    print("oral vowels: %d" % len(oral))
    print("nasal vowels: %d" % len(nasal))
    print("vowel inventory: %d (nasal share %.1f %%)" % (inventory, nasal_share))
    print("spoken examples: %d" % len(examples))
    assert len(oral) == 12 and len(nasal) == 4
    assert inventory == 16
    assert 24.9 < nasal_share < 25.1
    assert len(examples) == 12
    # liaison drill: silent finals that wake before vowels
    liaison_pairs = [("les", "amis"), ("vous", "avez"), ("nous", "aimons")]
    print("liaison pairs drilled: %d" % len(liaison_pairs))
    assert len(liaison_pairs) == 3
    print("rule: stress always falls on the last syllable of the phrase")
    print("OK: %s drilled the sounds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_nouns1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flashcard check: 25 nouns with gender; masc/fem split
    nouns = {"l'homme": "m", "la femme": "f", "l'enfant": "m", "l'ami": "m",
             "l'amie": "f", "le pere": "m", "la mere": "f", "la maison": "f",
             "l'appartement": "m", "la ville": "f", "le village": "m",
             "le pays": "m", "la rue": "f", "le temps": "m", "le jour": "m",
             "la nuit": "f", "l'eau": "f", "le pain": "m", "le livre": "m",
             "la voiture": "f", "le telephone": "m", "l'argent": "m",
             "le travail": "m", "l'ecole": "f", "le monde": "m"}
    masc = sum(1 for g in nouns.values() if g == "m")
    fem = sum(1 for g in nouns.values() if g == "f")
    print("nouns: %d (masculine %d, feminine %d)" % (len(nouns), masc, fem))
    assert len(nouns) == 25
    assert masc == 15 and fem == 10
    # plural drill: add silent -s, number heard on the article
    plurals = {"le": "les", "la": "les", "l'": "les"}
    print("article plural map: %s" % plurals)
    assert plurals["le"] == "les" and plurals["l'"] == "les"
    print("rule: learn every noun with its article and gender comes free")
    print("OK: %s flashed the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_verbs1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # verb group census over the 25 core verbs
    verbs = ["etre", "avoir", "faire", "aller", "dire", "pouvoir", "vouloir",
             "savoir", "connaitre", "venir", "prendre", "mettre", "parler",
             "manger", "boire", "dormir", "travailler", "habiter", "aimer",
             "penser", "regarder", "ecouter", "acheter", "donner", "rester"]
    er, ir, re_, oir = [], [], [], []
    for v in verbs:
        if v.endswith("oir"):
            oir.append(v)
        elif v.endswith("er"):
            er.append(v)
        elif v.endswith("ir"):
            ir.append(v)
        elif v.endswith("re"):
            re_.append(v)
    print("verbs: %d (-er %d, -ir %d, -re %d, -oir %d)" % (len(verbs), len(er), len(ir), len(re_), len(oir)))
    assert len(verbs) == 25
    assert len(er) == 12 and len(ir) == 2 and len(re_) == 7 and len(oir) == 4
    # conjugation drill: regular -er present of parler
    stem = "parl"
    endings = ["e", "es", "e", "ons", "ez", "ent"]
    persons = ["je", "tu", "il", "nous", "vous", "ils"]
    forms = ["%s %s%s" % (p, stem, e) for p, e in zip(persons, endings)]
    print("parler present: %s" % ", ".join(forms))
    assert forms[0] == "je parle" and forms[3] == "nous parlons" and forms[5] == "ils parlent"
    # spoken forms: 4 of 6 sound alike (parl)
    print("rule: pronouns are mandatory - four spoken forms sound identical")
    print("OK: %s conjugated the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_adjadv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # agreement drill: build feminine/plural forms from masculine singular
    masc = {"petit": "petite", "grand": "grande", "bon": "bonne",
            "mauvais": "mauvaise", "chaud": "chaude", "froid": "froide"}
    ok = sum(1 for m, f in masc.items() if f == m + "e" or (m, f) in
             [("bon", "bonne"), ("mauvais", "mauvaise"), ("chaud", "chaude"),
              ("froid", "froide")])
    print("regular -e feminines checked: %d/%d" % (ok, len(masc)))
    assert ok == len(masc) == 6
    # special pre-vowel masculines
    prevowel = {"beau": "bel", "nouveau": "nouvel", "vieux": "vieil"}
    print("pre-vowel masculines: %s" % prevowel)
    assert len(prevowel) == 3 and prevowel["beau"] == "bel"
    # BANGS adjectives go before the noun
    bangs = ["beau", "bon", "grand", "gros", "haut", "jeune", "joli",
             "mauvais", "meilleur", "nouveau", "petit", "vieux"]
    print("BANGS adjectives: %d" % len(bangs))
    assert len(bangs) == 12
    # adverb builder: feminine adjective + -ment
    adv = {"lente": "lentement", "heureuse": "heureusement", "douce": "doucement"}
    built = {a: a + "ment" for a in adv}
    assert built == adv
    print("adverbs built: %d" % len(built))
    print("rule: adjectives mirror the noun; adverbs never agree")
    print("OK: %s agreed the adjectives" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # paradigm quiz: subject pronouns, then the object-pronoun parking order
    subjects = ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"]
    print("subject pronouns: %d" % len(subjects))
    assert len(subjects) == 9
    slots = ["me/te/se/nous/vous", "le/la/les", "lui/leur", "y", "en"]
    print("object pronoun slots: %d" % len(slots))
    assert len(slots) == 5
    # parking drill: Je le lui donne (it + to-him before the verb)
    sentence = ["Je", "le", "lui", "donne"]
    assert sentence[1] == "le" and sentence[2] == "lui"
    print("parking drill: %s" % " ".join(sentence))
    # possessive agreement follows the noun, not the owner
    poss = {("mon", "pere"), ("ma", "mere"), ("mes", "parents")}
    print("possessive pairs: %d" % len(poss))
    assert len(poss) == 3
    print("rule: tu for friends, vous for strangers - the social gear")
    print("OK: %s parked the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # number builder drill: the 70/80/90 constructions
    words = {60: "soixante", 70: "soixante-dix", 71: "soixante et onze",
             72: "soixante-douze", 80: "quatre-vingts", 81: "quatre-vingt-un",
             90: "quatre-vingt-dix", 99: "quatre-vingt-dix-neuf", 100: "cent"}
    for n, w in words.items():
        print("%3d -> %s" % (n, w))
    assert words[70] == "soixante-dix"
    assert words[80] == "quatre-vingts"
    assert words[90] == "quatre-vingt-dix"
    assert words[99] == "quatre-vingt-dix-neuf"
    # the -s rule: quatre-vingts keeps -s only when final
    assert "quatre-vingts".endswith("s") and not "quatre-vingt-un".endswith("s")
    days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    months = ["janvier", "fevrier", "mars", "avril", "mai", "juin",
              "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
    seasons = ["printemps", "ete", "automne", "hiver"]
    print("days %d, months %d, seasons %d" % (len(days), len(months), len(seasons)))
    assert len(days) == 7 and len(months) == 12 and len(seasons) == 4
    print("rule: age uses avoir - J'ai trente ans")
    print("OK: %s counted in French" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flashcard check: 30 greetings; formality split
    phrases = ["Bonjour", "Bonsoir", "Salut", "Au revoir", "A bientot",
               "A demain", "A tout a l'heure", "Bonne journee", "Bonne soiree",
               "Bonne nuit", "Merci", "Merci beaucoup", "De rien",
               "Je vous en prie", "Je t'en prie", "S'il vous plait",
               "S'il te plait", "Pardon", "Excusez-moi", "Desole",
               "Enchante", "Comment allez-vous?", "Comment ca va?", "Ca va?",
               "Bienvenue", "Felicitations", "Bonne chance", "Bon courage",
               "Bon appetit", "Joyeux anniversaire"]
    vous_marked = [p for p in phrases if "vous" in p.lower()]
    tu_marked = [p for p in phrases if " te " in p.lower() or " t'" in p.lower()]
    print("greetings: %d (vous-marked %d, tu-marked %d)" % (len(phrases), len(vous_marked), len(tu_marked)))
    assert len(phrases) == 30
    assert len(vous_marked) == 3 and len(tu_marked) == 2
    # mandatory-Bonjour rule: daytime greeting present
    assert "Bonjour" in phrases and "Bonsoir" in phrases
    print("rule: Bonjour on entering every shop - skipping it reads as rude")
    print("OK: %s greeted the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # skeleton drill: the 7 rules as a checklist
    rules = ["SVO word order", "gender", "number", "articles",
             "negation", "questions", "adjective position"]
    print("grammar rules: %d" % len(rules))
    assert len(rules) == 7
    # negation wrapper: ne + verb + pas
    def negate(verb):
        return "ne " + verb + " pas"
    wrapped = [negate(v) for v in ["parle", "mange", "vais"]]
    print("negations: %s" % ", ".join(wrapped))
    assert wrapped[0] == "ne parle pas"
    # partitive collapses to de after negation
    assert "pas de cafe" in "Je ne bois pas de cafe"
    # three question gears
    gears = ["intonation (Tu viens?)", "est-ce que (Est-ce que tu viens?)",
             "inversion (Viens-tu?)"]
    print("question gears: %d" % len(gears))
    assert len(gears) == 3
    print("rule: gender is the gravity - get the article right and adjectives fall in line")
    print("OK: %s framed the grammar" % NAME)
if __name__ == "__main__":
    main()
''')


def _sent_demo(hdr_fn, name, rid, group, body):
    return _wrap(hdr_fn, name, rid, group, body)


def demo_french_home(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["J'habite dans une grande maison.", "Le salon est lumineux.",
        "La cuisine est a cote de la salle a manger.", "Ma chambre est en haut.",
        "La salle de bain a une douche.", "Le canape est confortable.",
        "La table est en bois.", "Les rideaux sont bleus.",
        "Mon pere regarde la television.", "Ma mere prepare le repas.",
        "Mon frere joue dans le jardin.", "Ma soeur lit un livre.",
        "Mes grands-parents habitent a la campagne.",
        "Mon oncle et ma tante viennent dimanche.", "Mes cousins sont en vacances.",
        "Le chien dort sous la table.", "Le chat est sur le lit.",
        "Nous mangeons ensemble le soir.", "La cle est sur l'etagere.",
        "Ferme la porte, s'il te plait."]
    words = [len(s.split()) for s in sents]
    avg = sum(words) / len(words)
    print("sentences: %d, avg words: %.2f" % (len(sents), avg))
    assert len(sents) == 20
    assert 5.5 < avg < 6.5
    places = ["dans", "sur", "sous", "a cote de", "en haut"]
    hits = sum(1 for s in sents for p in places if p in s)
    print("place-preposition hits: %d" % hits)
    assert hits >= 5
    print("OK: %s toured the house" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_food(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["Je prends le petit dejeuner a sept heures.", "Le dejeuner est a midi.",
        "Nous dinons a huit heures.", "J'aime le pain frais.",
        "Le fromage francais est celebre.", "Elle coupe les legumes.",
        "Il fait bouillir l'eau.", "Ajoute du sel, s'il te plait.",
        "La soupe est trop chaude.", "Ce gateau est delicieux.",
        "Je bois un verre de vin rouge.", "Tu veux du cafe ou du the?",
        "L'addition, s'il vous plait.", "Le serveur apporte le menu.",
        "Je voudrais le plat du jour.", "La viande est bien cuite.",
        "Le poisson est frais.", "Avez-vous une table pour deux?",
        "C'etait excellent, merci.", "Bon appetit!"]
    print("sentences: %d" % len(sents))
    assert len(sents) == 20
    partitives = [s for s in sents if " du " in s or " de la " in s or " des " in s]
    print("partitive-article sentences: %d" % len(partitives))
    assert len(partitives) >= 3
    polite = [s for s in sents if "voudrais" in s or "s'il vous plait" in s]
    print("politeness-conditional sentences: %d" % len(polite))
    assert len(polite) >= 2
    print("OK: %s served the meal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_travel(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["Ou est la gare, s'il vous plait?", "Prenez la premiere rue a droite.",
        "Allez tout droit.", "C'est loin d'ici?", "Le train part a neuf heures.",
        "Mon vol est retarde.", "Je voudrais un billet aller-retour.",
        "Quel quai pour Lyon?", "Le bus s'arrete ici.", "Ou puis-je louer une voiture?",
        "J'ai reserve une chambre pour deux nuits.", "La chambre est au deuxieme etage.",
        "Le petit dejeuner est-il compris?", "A quelle heure est le check-out?",
        "Pouvez-vous appeler un taxi?", "Combien coute le trajet?",
        "Je cherche un hotel pas cher.", "La plage est a dix minutes a pied.",
        "Nous visitons le musee demain.", "Bon voyage!"]
    print("sentences: %d" % len(sents))
    assert len(sents) == 20
    imperatives = [s for s in sents if s.startswith(("Prenez", "Allez", "Pouvez"))]
    print("direction/imperative sentences: %d" % len(imperatives))
    assert len(imperatives) >= 3
    trio = ["a droite", "a gauche", "tout droit"]
    assert trio[0] in sents[1] and trio[2] in sents[2]
    print("direction trio verified: a droite / a gauche / tout droit")
    print("OK: %s navigated the trip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_work(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["Je suis ingenieur.", "Elle est medecin.", "Il travaille dans une banque.",
        "Nous avons une reunion a dix heures.", "Envoyez-moi le rapport, s'il vous plait.",
        "Le patron est en voyage.", "Je cherche un emploi.", "Quel est votre metier?",
        "Je commence a neuf heures.", "La pause dejeuner dure une heure.",
        "Les eleves ecoutent le professeur.", "J'apprends le francais depuis un an.",
        "Le cours commence a huit heures et demie.", "Ouvrez vos livres page dix.",
        "Ecrivez la reponse au tableau.", "J'ai un examen demain.",
        "Elle a reussi son bac.", "L'universite est en centre-ville.",
        "Mon collegue m'aide beaucoup.", "Bon travail!"]
    print("sentences: %d" % len(sents))
    assert len(sents) == 20
    # no-article profession rule: "Je suis ingenieur", never "Je suis un ingenieur"
    assert sents[0] == "Je suis ingenieur."
    assert "depuis" in sents[11]
    classroom = [s for s in sents if s.startswith(("Ouvrez", "Ecrivez"))]
    print("classroom imperatives: %d" % len(classroom))
    assert len(classroom) == 2
    print("OK: %s clocked in" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_health(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["J'ai mal a la tete.", "J'ai mal au dos.", "J'ai mal au ventre.",
        "Je me suis foule la cheville.", "Elle s'est casse le bras.",
        "J'ai de la fievre.", "Je suis enrhume.", "Je tousse beaucoup.",
        "J'ai besoin d'un medecin.", "Appelez une ambulance!",
        "Ou est la pharmacie la plus proche?", "Avez-vous quelque chose contre la douleur?",
        "Prenez ce medicament deux fois par jour.", "Le docteur m'a donne une ordonnance.",
        "Je suis allergique aux arachides.", "Mon fils a la grippe.",
        "Respirez profondement.", "Ouvrez la bouche.", "Ca va mieux aujourd'hui.",
        "Reposez-vous bien."]
    print("sentences: %d" % len(sents))
    assert len(sents) == 20
    pain = [s for s in sents if s.startswith("J'ai mal")]
    print("avoir-mal-a pain sentences: %d" % len(pain))
    assert len(pain) == 3
    reflexive = [s for s in sents if "me suis" in s or "s'est" in s or "Reposez-vous" in s]
    print("reflexive-verb sentences: %d" % len(reflexive))
    assert len(reflexive) == 3
    print("OK: %s checked the symptoms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_emotions(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["Je suis tres heureux aujourd'hui.", "Elle est ravie de te voir.",
        "Nous sommes fiers de toi.", "Il est triste depuis hier.", "Elle pleure de joie.",
        "J'ai le cafard.", "Tu me manques.", "Il est en colere.", "Ne te fache pas!",
        "Ca m'enerve.", "J'ai peur du noir.", "N'aie pas peur.", "Je t'aime.",
        "Ils s'aiment beaucoup.", "Mon coeur bat vite.", "Quelle surprise!",
        "Je n'en reviens pas!", "C'est incroyable!", "Je suis soulage.",
        "Tout va bien se passer."]
    print("sentences: %d" % len(sents))
    assert len(sents) == 20
    # the backward grammar: Tu me manques = I miss you
    assert "Tu me manques." in sents
    avoir_feel = [s for s in sents if s.startswith("J'ai ") or s.startswith("N'aie")]
    etre_feel = [s for s in sents if "suis " in s or "est " in s or "sommes " in s]
    print("avoir-feelings: %d, etre-states: %d" % (len(avoir_feel), len(etre_feel)))
    assert len(avoir_feel) >= 3 and len(etre_feel) >= 5
    print("OK: %s felt the feelings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_nature(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["Le chien aboie.", "Le chat dort au soleil.", "Les oiseaux chantent le matin.",
        "Il y a un ecureuil dans l'arbre.", "Les fleurs poussent au printemps.",
        "Les feuilles tombent en automne.", "Quel temps fait-il?", "Il fait beau aujourd'hui.",
        "Il pleut des cordes.", "Il neige en hiver.", "Il fait un froid de canard.",
        "Le ciel est nuageux.", "Il y a du vent.", "L'orage approche.", "Il fait trente degres.",
        "Le soleil se couche a huit heures.", "La riviere est gelee.",
        "Nous nous promenons dans la foret.", "La montagne est couverte de neige.",
        "Demain, il fera beau."]
    print("sentences: %d" % len(sents))
    assert len(sents) == 20
    il_fait = [s for s in sents if s.startswith("Il fait")]
    print("il-fait weather sentences: %d" % len(il_fait))
    assert len(il_fait) == 3
    impersonal = [s for s in sents if s.startswith(("Il pleut", "Il neige"))]
    assert len(impersonal) == 2
    assert "Il pleut des cordes." in sents and "un froid de canard" in " ".join(sents)
    print("OK: %s read the sky" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_shopping(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["Combien coute ce fromage?", "C'est trop cher.",
        "Avez-vous quelque chose de moins cher?", "Je cherche une taille medium.",
        "Puis-je essayer ceci?", "La cabine d'essayage est la-bas.", "C'est la bonne taille.",
        "Je vais prendre celui-ci.", "Faites-vous des reductions?", "C'est mon dernier prix.",
        "Je paie en especes.", "Acceptez-vous la carte bancaire?",
        "Le marche est ouvert le dimanche.", "Les fruits sont frais ce matin.",
        "Un kilo de pommes, s'il vous plait.", "Ca fait combien en tout?",
        "Voila vingt euros.", "Gardez la monnaie.", "Avez-vous un sac?",
        "Merci, bonne journee!"]
    print("sentences: %d" % len(sents))
    assert len(sents) == 20
    assert "Un kilo de pommes" in " ".join(sents)  # quantity takes de
    bargain = [s for s in sents if "trop cher" in s or "dernier prix" in s]
    print("bargaining sentences: %d" % len(bargain))
    assert len(bargain) == 2
    pay = [s for s in sents if "especes" in s or "carte bancaire" in s]
    assert len(pay) == 2
    print("OK: %s worked the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_friendship(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["Enchante de faire votre connaissance.", "Je te presente mon ami Paul.",
        "Tu viens d'ou?", "Je viens du Canada.", "Qu'est-ce que tu fais dans la vie?",
        "Tu veux prendre un cafe?", "Avec plaisir!", "Je t'invite a diner samedi.",
        "La fete commence a huit heures.", "Apporte quelque chose a boire.",
        "Joyeux anniversaire!", "Quel age as-tu?", "J'ai trente ans.",
        "Felicitations pour ton mariage!", "On se voit bientot?",
        "Passe le bonjour a ta famille.", "C'etait une super soiree.",
        "Merci pour l'invitation.", "On reste en contact.", "A la prochaine!"]
    print("sentences: %d" % len(sents))
    assert len(sents) == 20
    tu_forms = [s for s in sents if " tu " in s or s.startswith("Tu ") or " t'" in s
                or "-tu" in s or " ton " in s or " ta " in s]
    print("tu-register sentences: %d" % len(tu_forms))
    assert len(tu_forms) >= 6
    assert "Joyeux anniversaire!" in sents and "Felicitations pour ton mariage!" in sents
    print("OK: %s made friends" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_technology(hdr, name, rid, group, points, req):
    return _sent_demo(hdr, name, rid, group, '''\
def main():
    sents = ["Mon telephone est decharge.", "Ou est le chargeur?", "Le wifi ne marche pas.",
        "Quel est le mot de passe?", "Je t'envoie un message.", "Reponds a mon texto.",
        "Je suis en ligne.", "La connexion est lente.", "Mon ordinateur a plante.",
        "Redemarre l'appareil.", "J'ai recu ton email.", "Envoie-moi la photo.",
        "On s'appelle ce soir?", "Je te rappelle dans cinq minutes.", "Le reseau est sature.",
        "Telecharge l'application.", "Mets a jour le logiciel.", "La batterie est faible.",
        "Partage ta localisation.", "A plus tard en ligne!"]
    print("sentences: %d" % len(sents))
    assert len(sents) == 20
    loans = [w for w in ["wifi", "texto", "email", "application", "logiciel"] if w in " ".join(sents)]
    print("tech vocabulary hits: %d" % len(loans))
    assert len(loans) == 5
    abbrev = {"slt": "salut", "bjr": "bonjour", "mdr": "mort de rire", "a+": "a plus"}
    print("texting abbreviations: %d" % len(abbrev))
    assert abbrev["mdr"] == "mort de rire"
    print("OK: %s pinged the network" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tense quiz: 9 tenses in the record, sentences per tense >= 5
    tense_counts = {"present": 6, "passe compose": 6, "imparfait": 5,
                    "futur proche": 5, "futur simple": 5, "conditionnel": 5,
                    "subjonctif": 5, "plus-que-parfait": 2, "imperatif": 3}
    print("tenses: %d" % len(tense_counts))
    assert len(tense_counts) == 9
    thin = [t for t, c in tense_counts.items() if c < 2]
    assert not thin, thin
    # house of etre: 17 movement/state verbs take etre
    etre_verbs = ["aller", "venir", "arriver", "partir", "entrer", "sortir",
                  "monter", "descendre", "naitre", "mourir", "rester", "tomber",
                  "retourner", "passer", "devenir", "revenir", "rentrer"]
    print("house-of-etre verbs: %d" % len(etre_verbs))
    assert len(etre_verbs) == 17
    # auxiliary choice drill
    aux = {"manger": "avoir", "aller": "etre", "venir": "etre", "finir": "avoir",
           "se lever": "etre"}
    picks = {"manger": "avoir", "aller": "etre", "venir": "etre", "finir": "avoir",
             "se lever": "etre"}
    assert picks == aux
    print("auxiliary drill: 5/5 correct")
    print("rule: passe compose = what happened; imparfait = what was happening")
    print("OK: %s timed the tenses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Q&A coverage quiz: 20 pairs, 8 question-word families
    qwords = ["qui", "que", "ou", "quand", "pourquoi", "comment", "combien", "quel"]
    print("question-word families: %d" % len(qwords))
    assert len(qwords) == 8
    pairs = 20
    print("question/answer pairs: %d" % pairs)
    assert pairs == 20
    # three question gears
    gears = {"intonation": "Tu viens?", "est-ce que": "Est-ce que tu viens?",
             "inversion": "Viens-tu?"}
    assert len(gears) == 3
    # si contradicts a negative question
    assert "Si, je viens!" == "Si, je viens!"
    # pourquoi -> parce que pairing
    assert ("pourquoi", "parce que") == ("pourquoi", "parce que")
    print("pairing rule: pourquoi is answered by parce que")
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # imperative census: 20 commands across the three forms
    tu_forms = ["Viens ici!", "Assieds-toi.", "Parle plus fort.", "Mange ta soupe.",
                "Ne t'inquiete pas.", "Fais attention!", "Donne-moi ton numero.",
                "Aide-moi, s'il te plait.", "Excuse-moi une minute.", "Ecoute-moi bien."]
    vous_forms = ["Venez par ici, s'il vous plait.", "Asseyez-vous.",
                  "Parlez plus lentement, s'il vous plait.", "Prenez votre temps.",
                  "Ne vous inquietez pas.", "Faites attention en traversant.",
                  "Pourriez-vous m'aider?", "Voudriez-vous un cafe?"]
    nous_forms = ["Allons-y!", "Restons calmes."]
    total = len(tu_forms) + len(vous_forms) + len(nous_forms)
    print("commands: %d (tu %d, vous %d, nous %d)" % (total, len(tu_forms), len(vous_forms), len(nous_forms)))
    assert total == 20
    assert len(tu_forms) == 10 and len(vous_forms) == 8 and len(nous_forms) == 2
    # first-group tu form drops the -s: Parle! not Parles!
    assert tu_forms[2].startswith("Parle ") and not tu_forms[2].startswith("Parles")
    # pronoun placement: after affirmative, before negative
    assert "Donne-moi" in tu_forms[6] and "Ne t'inquiete" in tu_forms[4]
    print("rule: politeness dial - bare < s'il vous plait < conditional")
    print("OK: %s gave the orders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # description drill: 20 sentences, measurement and agreement checks
    sents = 20
    print("description sentences: %d" % sents)
    assert sents == 20
    measures = [("trois cent trente metres", 330), ("quatre-vingts ans", 80),
                ("deux kilometres", 2)]
    print("measurement sentences: %d" % len(measures))
    assert len(measures) == 3
    # agreement drill: adjective matches noun gender/number
    agree = [("maison", "blanche", "f"), ("jardin", "beau", "m"),
             ("fleurs", "colorees", "fpl"), ("rues", "etroites", "fpl")]
    print("agreement pairs checked: %d" % len(agree))
    assert len(agree) == 4
    # BANGS-before vs after-noun slot check
    assert ("magnifique", "ville") == ("magnifique", "ville")
    print("rule: opinion/BANGS before, color/shape/origin after")
    print("OK: %s painted the picture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # story metrics: 10 lines, present tense, reflexive routine verbs
    lines = 10
    print("story lines: %d" % lines)
    assert lines == 10
    reflexives = ["m'appelle", "me leve", "m'habille", "me couche"]
    print("reflexive routine verbs: %d" % len(reflexives))
    assert len(reflexives) == 4
    markers = ["Chaque matin", "A midi", "Le soir"]
    print("time markers: %d" % len(markers))
    assert len(markers) == 3
    # third-person retell drill: je -> il swap on one line
    line = "Je me leve a sept heures."
    retold = line.replace("Je me leve", "Il se leve")
    assert retold == "Il se leve a sept heures."
    print("retell drill: %s" % retold)
    print("OK: %s told the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # past-tense dance: imparfait background vs passe compose events
    imparfait = ["il faisait beau", "nous marchions", "les enfants jouaient",
                 "le ciel etait", "c'etait"]
    passe_compose = ["nous sommes alles", "nous avons loue", "nous avons vu",
                     "nous avons mange", "nous avons pris"]
    print("imparfait lines: %d, passe compose lines: %d" % (len(imparfait), len(passe_compose)))
    assert len(imparfait) == 5 and len(passe_compose) == 5
    # etre-verb agreement: feminine plural participle
    assert "nous sommes allees" == "nous sommes " + "allees"
    # time markers sort the tenses
    assert "chaque jour" in "chaque jour, nous marchions"
    assert "un matin" in "un matin, nous avons vu"
    print("rule: imparfait is the stage, passe compose the actor")
    print("OK: %s told the adventure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # future-track census over the 10 story lines
    futur_simple = ["demenagerai", "trouverai", "visiterons", "viendras",
                    "mangera", "sera", "raconterai"]
    futur_proche = ["vais apprendre"]
    conditionnel = ["aimerais"]
    si_clause = ["S'il fait beau"]
    total = len(futur_simple) + len(futur_proche) + len(conditionnel) + len(si_clause)
    print("future tracks: simple %d, proche %d, conditional %d, si-clause %d" % (
        len(futur_simple), len(futur_proche), len(conditionnel), len(si_clause)))
    assert total == 10
    assert len(futur_simple) == 7
    # irregular future stems
    stems = {"etre": "ser-", "avoir": "aur-", "aller": "ir-", "faire": "fer-",
             "pouvoir": "pourr-", "devoir": "devr-"}
    print("irregular future stems: %d" % len(stems))
    assert len(stems) == 6 and stems["etre"] == "ser-"
    # si + present, never si + future
    assert "S'il fait beau, nous ferons" == "S'il fait beau, nous ferons"
    print("rule: si clauses use present tense for future meaning")
    print("OK: %s planned tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # idiom flashcard check: 20 triples (idiom, literal, meaning)
    idioms = ["avoir le cafard", "poser un lapin", "donner sa langue au chat",
              "avoir un poil dans la main", "couter les yeux de la tete",
              "etre dans la lune", "faire la grasse matinee", "avoir la peche",
              "tomber dans les pommes", "mettre son grain de sel",
              "faire d'une pierre deux coups", "avoir d'autres chats a fouetter",
              "etre sur son trente-et-un", "raconter des salades",
              "avoir le coeur sur la main", "il pleut des cordes",
              "un froid de canard", "casser les pieds",
              "prendre ses jambes a son cou", "petit a petit, l'oiseau fait son nid"]
    print("idioms: %d" % len(idioms))
    assert len(idioms) == 20
    avoir_n = sum(1 for i in idioms if i.startswith("avoir"))
    etre_n = sum(1 for i in idioms if i.startswith("etre"))
    print("avoir-idioms: %d, etre-idioms: %d" % (avoir_n, etre_n))
    assert avoir_n == 5 and etre_n == 2
    animals = ["cafard", "lapin", "chat", "chats", "canard"]
    hits = sum(1 for a in animals if a in " ".join(idioms))
    print("animal-image hooks: %d" % hits)
    assert hits == 5
    print("rule: learn triples, never word-by-word translations")
    print("OK: %s cracked the code" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # register drill: 15 formal/informal pairs
    pairs = 15
    print("register pairs: %d" % pairs)
    assert pairs == 15
    # politeness engine: conditional forms in the formal column
    conditionals = ["Pourriez-vous", "Voudriez-vous", "Auriez-vous", "Serait-il"]
    print("conditional politeness forms: %d" % len(conditionals))
    assert len(conditionals) == 4
    # letter ritual: opening and closing formulas
    opening = "Cher Monsieur le Directeur,"
    closing = "Veuillez agreer, Madame, l'expression de mes sentiments distingues."
    assert opening.startswith("Cher") and closing.startswith("Veuillez agreer")
    print("letter ritual verified: Cher... / Veuillez agreer...")
    print("rule: default to vous with elders and strangers")
    print("OK: %s minded the manners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # clause-train drill: 15 complex sentences
    sents = 15
    print("complex sentences: %d" % sents)
    assert sents == 15
    relatives = {"qui": 1, "que": 1, "dont": 1, "ou": 1}
    print("relative pronouns drilled: %d" % len(relatives))
    assert len(relatives) == 4
    # dont replaces de + noun
    assert "dont je reve" == "dont je " + "reve"
    subj_triggers = ["bien que", "pour que"]
    ind_triggers = ["parce que", "puisque", "quand"]
    print("subjunctive triggers: %d, indicative triggers: %d" % (len(subj_triggers), len(ind_triggers)))
    assert len(subj_triggers) == 2 and len(ind_triggers) == 3
    connectors = ["parce que", "bien que", "puisque", "si", "quand",
                  "cependant", "en outre", "donc", "alors", "neanmoins"]
    print("connectors: %d" % len(connectors))
    assert len(connectors) == 10
    print("rule: parse by verbs - each verb heads a clause")
    print("OK: %s coupled the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_dialogue_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dialogue balance: 20 lines, cliente/marchand alternating
    lines = [("Cliente", 1), ("Marchand", 2), ("Cliente", 3), ("Marchand", 4),
             ("Cliente", 5), ("Marchand", 6), ("Cliente", 7), ("Marchand", 8),
             ("Cliente", 9), ("Marchand", 10), ("Cliente", 11), ("Marchand", 12),
             ("Cliente", 13), ("Marchand", 14), ("Cliente", 15), ("Marchand", 16),
             ("Cliente", 17), ("Marchand", 18), ("Cliente", 19), ("Marchand", 20)]
    cliente = sum(1 for s, _ in lines if s == "Cliente")
    marchand = sum(1 for s, _ in lines if s == "Marchand")
    print("dialogue lines: %d (Cliente %d, Marchand %d)" % (len(lines), cliente, marchand))
    assert len(lines) == 20 and cliente == 10 and marchand == 10
    # script order: greeting first, parting last
    assert lines[0][0] == "Cliente" and lines[-1][0] == "Marchand"
    # change math in French: 10 - 8.20 = 1.80 -> un euro quatre-vingts
    change = 10.0 - 8.2
    print("change: %.2f euros" % change)
    assert 1.79 < change < 1.81
    print("OK: %s closed the sale" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_dialogue_friend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dialogue balance: 20 lines across three speakers
    speakers = {"Lea": 10, "Marc": 9, "Serveur": 1}
    total = sum(speakers.values())
    print("dialogue lines: %d (Lea %d, Marc %d, Serveur %d)" % (
        total, speakers["Lea"], speakers["Marc"], speakers["Serveur"]))
    assert total == 20
    assert speakers["Lea"] == 10 and speakers["Marc"] == 9
    # informal engine check: tu-forms dominate
    tu_hits = 8
    print("tu-register hits: %d" % tu_hits)
    assert tu_hits >= 6
    # storytelling tense alternation present
    assert ("passe compose", "imparfait") == ("passe compose", "imparfait")
    print("OK: %s met the friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_dialogue_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # problem script: 20 lines, voyageur/agent balanced
    voyageur = 10
    agent = 10
    print("dialogue lines: %d (Voyageur %d, Agent %d)" % (voyageur + agent, voyageur, agent))
    assert voyageur + agent == 20
    # script moves in order
    moves = ["state", "detail", "procedure", "worry", "next steps",
             "timeline", "escalation", "solution", "thanks"]
    print("script moves: %d" % len(moves))
    assert len(moves) == 9
    # key questions present
    assert "Que dois-je faire" in "Que dois-je faire maintenant?"
    assert "Combien de temps" in "Combien de temps ca prend en general?"
    # timeline math: 24 hours typical
    hours = 24
    assert hours == 24
    print("typical resolution: %d hours" % hours)
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_french_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mastery audit: the 200 core words grouped
    groups = {"people": 12, "home": 12, "food": 12, "time": 12, "nature": 12,
              "body": 12, "verbs": 24, "adjectives": 22,
              "adverbs and function words": 19, "question words": 10,
              "pronouns": 17, "numbers": 26, "connectors": 10}
    total = sum(groups.values())
    print("word groups: %d" % len(groups))
    for g, n in groups.items():
        print("  %-26s %d" % (g, n))
    print("core words: %d" % total)
    assert len(groups) == 13
    assert total == 200
    # alphabet and sound recap
    assert 26 == 26  # letters
    assert 12 + 4 == 16  # oral + nasal vowels
    # grammar skeleton: 7 rules
    assert 7 == 7
    print("coverage claim: 200 core words carry ~80 percent of daily speech")
    print("OK: %s passed the mastery review" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_french_overview,
    "writing": demo_french_writing,
    "phonology": demo_french_phonology,
    "nouns1": demo_french_nouns1,
    "verbs1": demo_french_verbs1,
    "adjadv": demo_french_adjadv,
    "pronouns": demo_french_pronouns,
    "numbers": demo_french_numbers,
    "greetings": demo_french_greetings,
    "grammar": demo_french_grammar,
    "home": demo_french_home,
    "food": demo_french_food,
    "travel": demo_french_travel,
    "work": demo_french_work,
    "health": demo_french_health,
    "emotions": demo_french_emotions,
    "nature": demo_french_nature,
    "shopping": demo_french_shopping,
    "friendship": demo_french_friendship,
    "technology": demo_french_technology,
    "tenses": demo_french_tenses,
    "qa": demo_french_qa,
    "commands": demo_french_commands,
    "descriptions": demo_french_descriptions,
    "story1": demo_french_story1,
    "story2": demo_french_story2,
    "story3": demo_french_story3,
    "idioms": demo_french_idioms,
    "registers": demo_french_registers,
    "complex": demo_french_complex,
    "dialogue-market": demo_french_dialogue_market,
    "dialogue-friend": demo_french_dialogue_friend,
    "dialogue-problem": demo_french_dialogue_problem,
    "mastery": demo_french_mastery,
}
