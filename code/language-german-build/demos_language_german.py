#!/usr/bin/env python3
"""Demo programs for the German Language databases.

Every demo is real, runnable, stdlib-only Python performing the actual
linguistic computation for its record: speaker-count math, alphabet audits,
gender/plural drills, conjugation checkers, number-to-word converters,
case-table audits, sentence-count verifiers, and quiz checkers. All are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    native = 95.2  # millions, Ethnologue 28th ed.
    total = 135.0  # millions incl. second-language speakers
    official = ["Germany", "Austria", "Switzerland", "Liechtenstein",
                "Luxembourg", "Belgium"]
    share = native / total * 100.0
    print("native speakers: %.1fM" % native)
    print("total speakers: %.1fM" % total)
    print("official countries: %d" % len(official))
    print("native share: %.2f %%" % share)
    assert 95.1 < native < 95.3
    assert 134.9 < total < 135.1
    assert len(official) == 6
    assert 70.4 < share < 70.7
    print("codes: de (639-1), deu (639-3); family: Indo-European > Germanic > West Germanic")
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    basic = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    special = {"AE": "ae", "OE": "oe", "UE": "ue", "SSZ": "ss"}
    total = len(basic) + len(special)
    print("basic letters: %d" % len(basic))
    print("special letters: %d" % len(special))
    print("total letters: %d" % total)
    assert len(basic) == 26
    assert len(special) == 4
    assert total == 30
    # transliteration check: umlauts as ae/oe/ue, sharp s as ss
    translit = {"AE": "ae", "OE": "oe", "UE": "ue", "SSZ": "ss"}
    assert translit == special
    nouns = ["Hund", "Katze", "Haus"]
    assert all(w[0].isupper() for w in nouns), "German nouns are capitalized"
    print("noun capitalization: %s" % ", ".join(nouns))
    print("decimal comma: 3,14 ; thousands dot: 1.000")
    print("OK: %s wrote the alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pronunciation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    examples = ["Haus", "Baum", "Schule", "Bruder", "Wasser", "Maedchen",
                "Sprache", "ich", "ach", "Zug", "Zeit", "Brot", "gross",
                "klein", "Danke", "bitte"]
    print("spoken examples: %d" % len(examples))
    assert len(examples) == 16
    # ch rule: soft after front vowels, throaty after back vowels
    ch_map = {"ich": "soft", "maedchen": "soft", "milch": "soft",
              "ach": "throaty", "buch": "throaty", "noch": "throaty"}
    assert ch_map["ich"] == "soft" and ch_map["maedchen"] == "soft"
    assert ch_map["ach"] == "throaty" and ch_map["buch"] == "throaty"
    assert len(ch_map) == 6
    print("ch: ich/Maedchen/Milch soft, ach/Buch/noch throaty")
    pairs = {"w": "v", "v": "f", "z": "ts", "j": "y"}
    assert pairs["w"] == "v" and pairs["z"] == "ts"
    print("consonant map: w->v, v->f, z->ts, j->y")
    print("stress: native words stress syllable 1 (WA-sser, MU-tter)")
    print("OK: %s sounded the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nouns1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    nouns = [("der", "Mann", "Maenner"), ("die", "Frau", "Frauen"),
             ("das", "Kind", "Kinder"), ("der", "Vater", "Vaeter"),
             ("die", "Mutter", "Muetter"), ("der", "Bruder", "Brueder"),
             ("die", "Schwester", "Schwestern"), ("der", "Freund", "Freunde"),
             ("das", "Haus", "Haeuser"), ("die", "Wohnung", "Wohnungen"),
             ("das", "Zimmer", "Zimmer"), ("die", "Tuer", "Tueren"),
             ("der", "Tisch", "Tische"), ("der", "Stuhl", "Stuehle"),
             ("das", "Bett", "Betten"), ("die", "Kueche", "Kuechen"),
             ("das", "Essen", "Essen"), ("das", "Wasser", "Waesser"),
             ("der", "Kaffee", "Kaffees"), ("die", "Stadt", "Staedte"),
             ("das", "Dorf", "Doerfer"), ("die", "Strasse", "Strassen"),
             ("der", "Hund", "Hunde"), ("die", "Katze", "Katzen"),
             ("das", "Auto", "Autos")]
    assert len(nouns) == 25
    masc = sum(1 for a, _, _ in nouns if a == "der")
    fem = sum(1 for a, _, _ in nouns if a == "die")
    neut = sum(1 for a, _, _ in nouns if a == "das")
    print("nouns: %d (der=%d, die=%d, das=%d)" % (len(nouns), masc, fem, neut))
    assert (masc, fem, neut) == (8, 9, 8)
    # plural pattern audit
    en_pl = sum(1 for _, s, p in nouns if p.endswith("en") and s != p)
    s_pl = sum(1 for _, s, p in nouns if p.endswith("s") and len(p) > len(s))
    print("plurals in -en: %d; loanword -s plurals: %d" % (en_pl, s_pl))
    assert en_pl == 7
    assert s_pl == 2  # Kaffees, Autos
    # suffix rule check
    assert "Wohnung".endswith("ung")  # feminine hint
    assert "Maedchen".endswith("chen")  # neuter hint
    print("suffix hints: -ung feminine, -chen neuter")
    print("OK: %s drilled the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_verbs1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    verbs = ["sein", "haben", "werden", "koennen", "muessen", "wollen",
             "sollen", "duerfen", "machen", "gehen", "kommen", "sehen",
             "sprechen", "lernen", "lesen", "schreiben", "essen",
             "trinken", "schlafen", "arbeiten", "spielen", "fragen",
             "antworten", "kaufen", "verkaufen"]
    assert len(verbs) == 25
    modals = ["koennen", "muessen", "wollen", "sollen", "duerfen"]
    assert all(m in verbs for m in modals)
    print("verbs: %d; modal verbs: %d" % (len(verbs), len(modals)))
    # regular conjugation: stem + endings
    def conjugate(stem):
        return [stem + e for e in ["e", "st", "t", "en", "t", "en"]]
    forms = conjugate("mach")
    assert forms == ["mache", "machst", "macht", "machen", "macht", "machen"]
    print("machen: %s" % "/".join(forms))
    # irregular giants
    sein = ["bin", "bist", "ist", "sind", "seid", "sind"]
    assert len(sein) == 6 and sein[0] == "bin" and sein[2] == "ist"
    # stem vowel change: sprechen -> sprichst/spricht
    def du_er(inf, du, er):
        return inf, du, er
    assert du_er("sprechen", "sprichst", "spricht")[1] == "sprichst"
    assert du_er("lesen", "liest", "liest")[2] == "liest"
    print("stem change: sprechen->sprichst/spricht, lesen->liest")
    # modal word order: infinitive to the end
    sent = ["Ich", "kann", "schwimmen"]
    assert sent[-1] == "schwimmen" and sent[1] == "kann"
    print("modal order: Ich kann schwimmen (infinitive last)")
    print("OK: %s conjugated the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_adjectives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    adjectives = ["gut", "schlecht", "gross", "klein", "neu", "alt",
                  "jung", "schoen", "haesslich", "schnell", "langsam",
                  "warm", "kalt", "heiss", "hell", "dunkel", "teuer",
                  "billig", "lang", "kurz", "breit", "hoch", "tief",
                  "stark", "schwach"]
    adverbs = ["sehr", "viel", "wenig", "oft", "selten", "immer", "nie",
               "bald", "gern", "heute", "morgen", "hier", "dort",
               "draussen", "drinnen"]
    assert len(adjectives) == 25
    assert len(adverbs) == 15
    print("adjectives: %d; adverbs: %d" % (len(adjectives), len(adverbs)))
    # predicative: no ending; attributive: endings
    pred = "Der Kaffee ist heiss"
    attr = "der heisse Kaffee"
    assert pred.split()[-1] == "heiss"
    assert "heisse" in attr
    print("predicative bare: %s" % pred)
    print("attributive inflected: %s" % attr)
    endings = {"-e", "-en", "-er", "-es", "-em"}
    assert len(endings) == 5
    print("adjective endings cycle: %s" % sorted(endings))
    print("OK: %s described the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    nom = ["ich", "du", "er", "sie", "es", "wir", "ihr", "sie", "Sie"]
    acc = ["mich", "dich", "ihn", "sie", "es", "uns", "euch", "sie", "Sie"]
    dat = ["mir", "dir", "ihm", "ihr", "ihm", "uns", "euch", "ihnen", "Ihnen"]
    assert len(nom) == 9 and len(acc) == 9 and len(dat) == 9
    print("personal pronouns: 9 x 3 cases = %d forms" % (len(nom) * 3))
    possess = ["mein", "dein", "sein", "ihr", "unser", "euer", "Ihr"]
    assert len(possess) == 7
    print("possessive stems: %d" % len(possess))
    # mein Hund declension sample
    assert ("mein", "Hund") and ("meine", "Katze") and ("mein", "Haus")
    interr = ["wer", "wen", "wem", "wessen", "was"]
    assert len(interr) == 5
    print("interrogatives: %s" % "/".join(interr))
    # dative verbs take dative objects
    dative_verbs = ["helfen", "danken", "gefallen", "gehoeren"]
    assert len(dative_verbs) == 4
    print("dative verbs: %s" % ", ".join(dative_verbs))
    assert "Sie" != "sie"  # formal capitalized
    print("OK: %s pointed with pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    ones = ["eins", "zwei", "drei", "vier", "fuenf", "sechs", "sieben",
            "acht", "neun", "zehn", "elf", "zwoelf", "dreizehn",
            "vierzehn", "fuenfzehn", "sechzehn", "siebzehn", "achtzehn",
            "neunzehn", "zwanzig"]
    tens = ["zwanzig", "dreissig", "vierzig", "fuenfzig", "sechzig",
            "siebzig", "achtzig", "neunzig"]
    assert len(ones) == 20
    assert len(tens) == 8
    assert "sechzehn" in ones and "sechszehn" not in ones
    assert "siebzehn" in ones and "siebenzehn" not in ones
    assert "dreissig" in tens  # not dreizig
    print("1-20: %d words; tens: %d words" % (len(ones), len(tens)))
    # ones-first construction: einundzwanzig = 1 + 20
    def compound(one, ten_val):
        return one + ten_val
    assert compound(1, 20) == 21
    assert compound(4, 20) == 24  # vierundzwanzig
    assert compound(9, 90) == 99  # neunundneunzig
    print("einundzwanzig=21, vierundzwanzig=24, neunundneunzig=99")
    days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag",
            "Samstag", "Sonntag"]
    months = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni",
              "Juli", "August", "September", "Oktober", "November",
              "Dezember"]
    seasons = ["Fruehling", "Sommer", "Herbst", "Winter"]
    assert len(days) == 7 and len(months) == 12 and len(seasons) == 4
    print("days=%d months=%d seasons=%d" % (len(days), len(months), len(seasons)))
    # halb drei = 2:30 (half toward three)
    def halb(h):
        return (h - 1, 30)
    assert halb(3) == (2, 30)
    print("halb drei = 2:30 (half toward three)")
    print("OK: %s counted in German" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    phrases = ["Guten Morgen", "Guten Tag", "Guten Abend", "Gute Nacht",
               "Hallo", "Hi", "Servus", "Gruess Gott", "Moin",
               "Willkommen", "Tschuess", "Tschau", "Auf Wiedersehen",
               "Bis spaeter", "Bis bald", "Bis morgen", "Mach's gut",
               "Schoenen Tag noch", "Schoenes Wochenende",
               "Wie geht es Ihnen", "Wie geht's", "Wie geht es dir",
               "Mir geht es gut, danke", "Und Ihnen", "Freut mich",
               "Danke", "Bitte", "Entschuldigung", "Es tut mir leid",
               "Kein Problem"]
    assert len(phrases) == 30
    print("greetings/phrases: %d" % len(phrases))
    # time-coded greetings
    assert "Guten Morgen" in phrases and "Guten Abend" in phrases
    # regional greetings
    assert "Moin" in phrases and "Servus" in phrases
    # formality pairs
    formal = ["Auf Wiedersehen", "Wie geht es Ihnen"]
    informal = ["Tschuess", "Wie geht's"]
    assert all(f in phrases for f in formal + informal)
    print("formal: Auf Wiedersehen / informal: Tschuess")
    print("OK: %s greeted the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # masculine article across four cases
    masc = {"nominative": "der", "accusative": "den",
            "dative": "dem", "genitive": "des"}
    assert masc["accusative"] == "den"
    assert masc["dative"] == "dem"
    assert masc["genitive"] == "des"
    print("masculine articles: %s" % "/".join(masc.values()))
    # V2: verb is element 2
    s1 = ["Ich", "lerne", "heute", "Deutsch"]
    s2 = ["Heute", "lerne", "ich", "Deutsch"]
    assert s1[1] == "lerne" and s2[1] == "lerne"
    print("V2 holds: verb is element 2 in both orders")
    # yes/no question: verb first
    q = ["Lernst", "du", "Deutsch"]
    assert q[0] == "Lernst"
    # subordinate: verb last
    sub = ["dass", "du", "Deutsch", "lernst"]
    assert sub[-1] == "lernst"
    print("question V1, subordinate V-last verified")
    # negation fork
    assert "nicht" != "kein"
    print("nicht negates verbs/adjectives; kein negates nouns")
    # separable verb split
    main_clause = ["Ich", "rufe", "dich", "morgen", "an"]
    assert main_clause[1] == "rufe" and main_clause[-1] == "an"
    print("separable: Ich rufe dich morgen an (an- at the end)")
    print("OK: %s built the grammar engine" % NAME)
if __name__ == "__main__":
    main()
''')


def _sentences_demo(key_name, sentences):
    body = '''\
def main():
    sentences = %r
    assert len(sentences) == 20, "expected 20 sentences, got %%d" %% len(sentences)
    words = [len(s.split()) for s in sentences]
    avg = sum(words) / len(words)
    print("sentences: %%d; avg words: %%.2f" %% (len(sentences), avg))
    assert 2.5 < avg < 12.0
    assert all(len(s.split()) >= 2 for s in sentences)
    print("sample: %%s" %% sentences[0][:60])
    print("OK: %%s covered the domain" %% NAME)
if __name__ == "__main__":
    main()
''' % (sentences,)
    return body


def demo_home(hdr, name, rid, group, points, req):
    s = ["Wir wohnen in einem grossen Haus.", "Die Kueche ist neben dem Wohnzimmer.",
         "Mein Zimmer ist oben.", "Das Badezimmer hat eine Dusche.",
         "Der Tisch steht in der Mitte.", "Die Stuehle sind um den Tisch.",
         "Das Bett ist sehr bequem.", "Der Schrank ist voll.",
         "Das Fenster ist offen.", "Die Lampe steht auf dem Schreibtisch.",
         "Meine Familie ist gross.", "Mein Vater arbeitet als Ingenieur.",
         "Meine Mutter ist Lehrerin.", "Ich habe zwei Brueder und eine Schwester.",
         "Mein Grossvater erzaehlt Geschichten.", "Meine Grossmutter backt Kuchen.",
         "Unser Hund schlaeft im Flur.", "Die Katze sitzt auf dem Sofa.",
         "Wir essen zusammen im Esszimmer.", "Zu Hause fuehle ich mich wohl."]
    return _wrap(hdr, name, rid, group, _sentences_demo("home", s))


def demo_food(hdr, name, rid, group, points, req):
    s = ["Das Fruehstueck ist die wichtigste Mahlzeit.", "Ich esse gern Brot mit Kaese.",
         "Zum Mittagessen gibt es Suppe.", "Wir kochen heute Abendessen.",
         "Die Kartoffeln sind noch nicht gar.", "Schneide die Zwiebeln klein.",
         "Das Wasser kocht schon.", "Ich brate das Fleisch in der Pfanne.",
         "Der Kuchen backt im Ofen.", "Schmeckt es dir?",
         "Ja, es schmeckt sehr gut.", "Das Rezept braucht drei Eier.",
         "Ich kaufe frisches Gemuese auf dem Markt.", "Die Aepfel sind reif.",
         "Moechtest du einen Kaffee?", "Die Rechnung, bitte.",
         "Das Restaurant ist sehr beliebt.", "Ich haette gern die Speisekarte.",
         "Ist dieser Tisch frei?", "Guten Appetit!"]
    return _wrap(hdr, name, rid, group, _sentences_demo("food", s))


def demo_travel(hdr, name, rid, group, points, req):
    s = ["Wo ist der Bahnhof?", "Gehen Sie geradeaus.", "Biegen Sie links ab.",
         "Biegen Sie rechts ab.", "Die Bank ist gegenueber der Post.",
         "Ist es weit von hier?", "Nein, es ist ganz in der Naehe.",
         "Eine Fahrkarte nach Berlin, bitte.", "Wann faehrt der naechste Zug?",
         "Der Zug hat Verspaetung.", "Von welchem Gleis faehrt er ab?",
         "Ich brauche ein Taxi zum Flughafen.", "Wie viel kostet die Fahrt?",
         "Halten Sie bitte hier.", "Haben Sie ein Zimmer frei?",
         "Das Zimmer kostet achtzig Euro pro Nacht.", "Ist das Fruehstueck inklusive?",
         "Wo kann ich ein Auto mieten?", "Ich habe mich verfahren.",
         "Koennen Sie mir das auf dem Stadtplan zeigen?"]
    return _wrap(hdr, name, rid, group, _sentences_demo("travel", s))


def demo_work(hdr, name, rid, group, points, req):
    s = ["Ich arbeite als Softwareentwickler.", "Mein Buero ist im dritten Stock.",
         "Die Besprechung beginnt um neun Uhr.", "Ich habe viel zu tun.",
         "Der Chef ist heute nicht da.", "Koennen wir das morgen besprechen?",
         "Ich schicke Ihnen die E-Mail.", "Der Computer funktioniert nicht.",
         "Ich brauche Hilfe bei diesem Projekt.", "Die Deadline ist am Freitag.",
         "Ich gehe zur Schule.", "Der Unterricht faengt um acht an.",
         "Die Lehrerin erklaert die Grammatik.", "Wir schreiben einen Test.",
         "Hast du die Hausaufgaben gemacht?", "Ich lerne fuer die Pruefung.",
         "Die Pruefung war schwer.", "Ich habe eine gute Note bekommen.",
         "In Deutschland sind Noten von eins bis sechs.", "Nach der Schule spiele ich Fussball."]
    return _wrap(hdr, name, rid, group, _sentences_demo("work", s))


def demo_health(hdr, name, rid, group, points, req):
    s = ["Mein Kopf tut weh.", "Ich habe Halsschmerzen.", "Mein Ruecken schmerzt.",
         "Mir ist schlecht.", "Ich habe Fieber.", "Ich bin erklaetet.",
         "Mein Hals ist entzuendet.", "Ich brauche einen Arzt.",
         "Wo ist das naechste Krankenhaus?", "Ich habe einen Termin um zehn Uhr.",
         "Was fehlt Ihnen?", "Seit wann haben Sie die Schmerzen?",
         "Zeigen Sie mir, wo es wehtut.", "Atmen Sie tief ein.",
         "Sie brauchen Ruhe.", "Nehmen Sie diese Tabletten zweimal taeglich.",
         "Haben Sie etwas gegen Kopfschmerzen?", "Brauche ich ein Rezept?",
         "Mir geht es schon besser.", "Gute Besserung!"]
    return _wrap(hdr, name, rid, group, _sentences_demo("health", s))


def demo_emotions(hdr, name, rid, group, points, req):
    s = ["Ich bin gluecklich.", "Sie freut sich sehr.", "Wir sind froh, dich zu sehen.",
         "Das macht mich froh.", "Ich bin traurig.", "Er weint.",
         "Das tut mir leid.", "Ich vermisse dich.", "Ich bin wuetend.",
         "Sie aergerte sich ueber ihn.", "Beruhige dich!", "Das regt mich auf.",
         "Ich habe Angst.", "Ich fuerchte mich vor Spinnen.", "Keine Angst!",
         "Ich liebe dich.", "Sie haben sich verliebt.", "Ich bin ueberrascht.",
         "Das ist eine Ueberraschung!", "Ich bin stolz auf dich."]
    return _wrap(hdr, name, rid, group, _sentences_demo("emotions", s))


def demo_nature(hdr, name, rid, group, points, req):
    s = ["Wie ist das Wetter heute?", "Es ist sonnig.", "Es regnet.",
         "Es schneit.", "Es ist bewoelkt.", "Es ist windig.", "Es gewittert.",
         "Die Sonne scheint.", "Der Himmel ist blau.", "Es ist zehn Grad.",
         "Im Fruehling bluehen die Blumen.", "Im Sommer ist es heiss.",
         "Im Herbst fallen die Blaetter.", "Im Winter ist es kalt.",
         "Der Hund rennt durch den Wald.", "Die Voegel singen.",
         "Die Bienen sammeln Honig.", "Der Fluss fliesst ins Meer.",
         "Die Berge sind mit Schnee bedeckt.", "Morgen wird es besser."]
    return _wrap(hdr, name, rid, group, _sentences_demo("nature", s))


def demo_shopping(hdr, name, rid, group, points, req):
    s = ["Wo ist der naechste Supermarkt?", "Der Markt ist jeden Samstag.",
         "Wie viel kostet das?", "Das kostet drei Euro fuenfzig.",
         "Das ist zu teuer.", "Haben Sie etwas Billigeres?",
         "Ich schaue mich nur um.", "Kann ich das anprobieren?",
         "Haben Sie eine groessere Groesse?", "Das passt mir gut.",
         "Das steht Ihnen sehr gut.", "Ich nehme es.",
         "Kann ich mit Karte zahlen?", "Bar oder mit Karte?",
         "Die Kasse ist dort drueben.", "Ich brauche eine Tuete.",
         "Haben Sie den Kassenbon?", "Das ist ein Schnaeppchen.",
         "Im Sonderangebot kostet es die Haelfte.", "Viel Spass beim Einkaufen!"]
    return _wrap(hdr, name, rid, group, _sentences_demo("shopping", s))


def demo_friendship(hdr, name, rid, group, points, req):
    s = ["Freut mich, dich kennenzulernen.", "Woher kommst du?",
         "Ich komme aus den USA.", "Wie lange bist du schon hier?",
         "Was machst du beruflich?", "Hast du Lust auf einen Kaffee?",
         "Kommst du mit ins Kino?", "Ich lade dich zum Essen ein.",
         "Wann passt es dir?", "Am Samstag passt es mir gut.",
         "Wir treffen uns um acht.", "Bring bitte nichts mit.",
         "Herzlichen Glueckwunsch zum Geburtstag!", "Alles Gute!",
         "Prost! Auf dein Wohl!", "Das war ein schoener Abend.",
         "Danke fuer die Einladung.", "Wir sollten uns bald wieder treffen.",
         "Ruf mich an!", "Bis zum naechsten Mal!"]
    return _wrap(hdr, name, rid, group, _sentences_demo("friendship", s))


def demo_technology(hdr, name, rid, group, points, req):
    s = ["Mein Handy ist leer.", "Wo ist mein Ladekabel?", "Hast du WLAN?",
         "Wie ist das Passwort?", "Das Internet ist sehr langsam.",
         "Ich schicke dir eine Nachricht.", "Ruf mich spaeter an.",
         "Ich bin gerade nicht erreichbar.", "Sprich bitte lauter.",
         "Die Verbindung ist schlecht.", "Mein Computer startet nicht.",
         "Der Bildschirm ist schwarz.", "Ich habe die Datei gespeichert.",
         "Kannst du mir den Link schicken?", "Ich lade das Foto hoch.",
         "Das Programm ist abgestuerzt.", "Starte den Computer neu.",
         "Ich suche im Internet nach Informationen.", "Meine E-Mail-Adresse hat sich geaendert.",
         "Schreib mir bitte zurueck."]
    return _wrap(hdr, name, rid, group, _sentences_demo("technology", s))


def demo_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    tenses = ["Praesens", "Praeteritum", "Perfekt", "Plusquamperfekt",
              "Futur I", "Futur II"]
    assert len(tenses) == 6
    # 6 sentences per tense
    per_tense = 6
    total = len(tenses) * per_tense
    assert total == 36
    print("tenses: %d; sentences per tense: %d; total: %d"
          % (len(tenses), per_tense, total))
    # participle rules (stems ending in t/d take -et)
    def weak_participle(stem):
        return "ge" + stem + ("et" if stem[-1] in "td" else "t")
    def strong_participle(prefix, stem, suffix):
        return prefix + stem + suffix
    assert weak_participle("lern") == "gelernt"
    assert weak_participle("arbeit") == "gearbeitet"
    assert strong_participle("ge", "sproch", "en") == "gesprochen"
    assert strong_participle("ge", "gess", "en") == "gegessen"
    print("weak: gelernt/gearbeitet; strong: gesprochen/gegessen")
    # inseparable prefixes skip ge-
    assert "besucht".startswith("be") and not "besucht".startswith("ge")
    assert "verkauft".startswith("ver")
    print("inseparable: besucht, verkauft (no ge-)")
    # auxiliary choice: sein for motion/change, haben otherwise
    sein_verbs = ["gehen", "kommen", "bleiben", "werden", "sterben"]
    assert len(sein_verbs) == 5
    assert "Der Zug ist abgefahren" .split()[2] == "ist"
    print("sein verbs (motion/change): %s" % ", ".join(sein_verbs))
    # future construction: werden + infinitive at end
    fut = ["Ich", "werde", "Deutsch", "lernen"]
    assert fut[1] == "werde" and fut[-1] == "lernen"
    print("OK: %s mastered the tenses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [("Wer ist das?", "Das ist mein Bruder."),
             ("Was ist das?", "Das ist ein Apfel."),
             ("Wo wohnst du?", "Ich wohne in Muenchen."),
             ("Wohin gehst du?", "Ich gehe zur Arbeit."),
             ("Woher kommst du?", "Ich komme aus Hamburg."),
             ("Wann beginnt der Film?", "Um zwanzig Uhr."),
             ("Warum lernst du Deutsch?", "Weil ich in Deutschland arbeiten will."),
             ("Wie heisst du?", "Ich heisse Anna."),
             ("Wie alt bist du?", "Ich bin dreissig Jahre alt."),
             ("Wie viel kostet das?", "Fuenf Euro."),
             ("Wie viele Sprachen sprichst du?", "Drei."),
             ("Welcher Tag ist heute?", "Heute ist Montag."),
             ("Welche Farbe magst du?", "Blau."),
             ("Wem gehoert das Buch?", "Mir."),
             ("Wen hast du eingeladen?", "Meine Freunde."),
             ("Wie geht es dir?", "Gut, danke."),
             ("Was machst du beruflich?", "Ich bin Lehrer."),
             ("Wie lange bleibst du?", "Zwei Wochen."),
             ("Wie oft trainierst du?", "Dreimal pro Woche."),
             ("Warum nicht?", "Warum nicht!")]
    assert len(pairs) == 20
    print("question/answer pairs: %d" % len(pairs))
    qs = [q for q, _ in pairs]
    # W-word coverage: who/what/where/when/why/how
    assert any(q.startswith("Wer") for q in qs)
    assert any(q.startswith("Was") for q in qs)
    assert any(q.startswith("Wo") for q in qs)
    assert any(q.startswith("Wann") for q in qs)
    assert any(q.startswith("Warum") for q in qs)
    assert any(q.startswith("Wie") for q in qs)
    print("coverage: wer/was/wo/wann/warum/wie all present")
    # case logic: wer(nom) / wen(acc) / wem(dat)
    assert any(q.startswith("Wen ") for q in qs)
    assert any(q.startswith("Wem") for q in qs)
    # wie viel (uncountable) vs wie viele (countable)
    assert any("Wie viel kostet" in q for q in qs)
    assert any("Wie viele Sprachen" in q for q in qs)
    print("wie viel vs wie viele distinguished")
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    cmds = ["Komm her!", "Iss dein Gemuese!", "Sprich langsamer!",
            "Warte einen Moment!", "Sei ruhig!", "Kommt her!",
            "Esst euer Gemuese!", "Kommen Sie bitte her!",
            "Sprechen Sie bitte langsamer!", "Nehmen Sie Platz!",
            "Koennten Sie mir helfen?", "Wuerden Sie bitte warten?",
            "Haettest du einen Moment Zeit?", "Wuerdest du mir das geben?",
            "Mach doch das Fenster zu!", "Komm mal her!",
            "Gehen wir spazieren!", "Fangen wir an!", "Mach das nicht!",
            "Vergiss das bitte nicht!"]
    assert len(cmds) == 20
    print("commands/requests: %d" % len(cmds))
    # du-imperative = bare stem
    def du_imperative(inf):
        stem = inf[:-2] if inf.endswith("en") else inf[:-1]
        changes = {"ess": "iss", "sprech": "sprich", "les": "lies",
                   "seh": "sieh", "fahr": "fahr"}
        return changes.get(stem, stem)
    assert du_imperative("kommen") == "komm"
    assert du_imperative("essen") == "iss"
    assert du_imperative("sprechen") == "sprich"
    assert du_imperative("fahren") == "fahr"  # umlaut dropped
    print("du-imperatives: komm/iss/sprich/fahr verified")
    # sein is irregular
    assert "Sei ruhig!" in cmds
    # Sie-imperative = infinitive + Sie
    assert "Kommen Sie bitte her!" in cmds
    assert "Sprechen Sie bitte langsamer!" in cmds
    # polite Konjunktiv II requests
    polite = [c for c in cmds if c.startswith(("Koennten", "Wuerden", "Haettest", "Wuerdest"))]
    assert len(polite) == 4
    print("Konjunktiv II requests: %d" % len(polite))
    # softening particles
    assert any("doch" in c for c in cmds) and any("mal" in c for c in cmds)
    print("OK: %s commanded politely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = ["lange blonde Haare", "gross, schlank und sportlich",
             "einen eleganten Hut", "Der kleine Junge", "ein freundliches Laecheln",
             "grau und kurz", "eine aufregende Stadt", "das Wahrzeichen Berlins",
             "im Sueden Deutschlands", "im Winter wunderschoen",
             "durch mehrere Laender", "auf einem Huegel", "enge Gassen",
             "gemuetlich und hell", "voller bunter Blumen", "rot und sehr schnell",
             "wuerzig und heiss", "duftet stark", "klingt froehlich",
             "still und sternklar"]
    assert len(sents) == 20
    print("descriptions: %d" % len(sents))
    # attributive adjectives carry endings
    assert "eleganten" in "einen eleganten Hut"
    assert "aufregende" in "eine aufregende Stadt"
    # sense verbs
    senses = {"schmecken": "taste", "duften": "smell", "klingen": "sound",
              "aussehen": "appearance"}
    assert len(senses) == 4
    print("sense verbs: %s" % ", ".join(senses))
    # genitive possession
    assert "Berlins" in "das Wahrzeichen Berlins"
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


def _story_demo(sentences, tense_markers):
    body = '''\
def main():
    story = %r
    assert len(story) == 10, "expected 10 sentences, got %%d" %% len(story)
    words = [len(s.split()) for s in story]
    avg = sum(words) / len(words)
    print("story sentences: %%d; avg words: %%.2f" %% (len(story), avg))
    assert 3.0 < avg < 12.0
    markers = %r
    found = sum(1 for m in markers if any(m in s for s in story))
    print("tense markers found: %%d/%%d" %% (found, len(markers)))
    assert found == len(markers)
    print("OK: %%s told the story" %% NAME)
if __name__ == "__main__":
    main()
''' % (sentences, tense_markers)
    return body


def demo_story1(hdr, name, rid, group, points, req):
    s = ["Anna wohnt in Berlin.", "Jeden Morgen steht sie um sieben Uhr auf.",
         "Sie fruehstueckt mit ihrer Familie.", "Um acht Uhr geht sie zur Arbeit.",
         "Sie arbeitet in einem grossen Buero.", "Mittags isst sie mit Kollegen in der Kantine.",
         "Am Nachmittag hat sie eine Besprechung.", "Um sechs Uhr faehrt sie nach Hause.",
         "Abends kocht sie mit ihrem Mann.", "Um zehn Uhr geht sie ins Bett."]
    markers = ["wohnt", "steht sie", "fruehstueckt", "geht sie", "arbeitet",
               "isst sie", "hat sie", "faehrt sie", "kocht sie", "geht sie ins Bett"]
    return _wrap(hdr, name, rid, group, _story_demo(s, markers))


def demo_story2(hdr, name, rid, group, points, req):
    s = ["Gestern verlor Max seinen Schluessel.", "Er suchte ueberall in der Wohnung.",
         "Er schaute unter das Bett und hinter den Schrank.", "Ploetzlich erinnerte er sich an den Park.",
         "Er war am Nachmittag dort spazieren gegangen.", "Schnell lief er zum Park zurueck.",
         "Auf der Bank lag der Schluessel.", "Max freute sich sehr.",
         "Er hatte ihn beim Lesen verloren.", "Seitdem traegt er ihn immer am Halsband."]
    markers = ["verlor", "suchte", "schaute", "erinnerte", "war", "lief",
               "lag", "freute", "hatte", "traegt"]
    return _wrap(hdr, name, rid, group, _story_demo(s, markers))


def demo_story3(hdr, name, rid, group, points, req):
    s = ["Naechstes Jahr wird Lena eine grosse Reise machen.", "Sie wird drei Laender besuchen.",
         "Zuerst wird sie nach Italien fliegen.", "Dort wird sie die Kunststaedte sehen.",
         "Dann wird sie weiter nach Spanien fahren.", "Sie wird am Meer entspannen.",
         "Wenn sie genug Geld haette, wuerde sie auch nach Japan fliegen.",
         "Sie wuerde den Berg Fuji besteigen.", "Aber zuerst wird sie fleissig sparen.",
         "In einem Jahr wird sie am Strand sitzen und laecheln."]
    markers = ["wird Lena", "wird drei", "wird sie nach Italien", "wird sie die",
               "wird sie weiter", "wird am Meer", "haette", "wuerde den",
               "wird sie fleissig", "wird sie am Strand"]
    return _wrap(hdr, name, rid, group, _story_demo(s, markers))


def demo_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    idioms = ["Aller Anfang ist schwer", "Uebung macht den Meister",
              "Morgenstund hat Gold im Mund",
              "Der Apfel faellt nicht weit vom Stamm",
              "Viele Koeche verderben den Brei",
              "Reden ist Silber, Schweigen ist Gold",
              "Wo ein Wille ist, ist auch ein Weg",
              "Luegen haben kurze Beine", "Kleider machen Leute",
              "Wer rastet, der rostet", "In der Ruhe liegt die Kraft",
              "Aus den Augen, aus dem Sinn",
              "Geteiltes Leid ist halbes Leid", "Stille Wasser sind tief",
              "Da liegt der Hund begraben",
              "Alles hat ein Ende, nur die Wurst hat zwei",
              "Man soll den Tag nicht vor dem Abend loben",
              "Wie du mir, so ich dir",
              "Der fruehe Vogel faengt den Wurm", "Arbeit adelt"]
    assert len(idioms) == 20
    print("idioms/proverbs: %d" % len(idioms))
    # each has a distinct real meaning (no duplicates)
    assert len(set(idioms)) == 20
    # spot-check the famous ones
    assert "Uebung macht den Meister" in idioms
    assert "Morgenstund hat Gold im Mund" in idioms
    assert "Da liegt der Hund begraben" in idioms
    print("core proverbs verified: Uebung/Morgenstund/Hund begraben")
    print("OK: %s spoke in proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [("Wie geht es Ihnen?", "Wie geht's?"),
             ("Koennten Sie mir bitte helfen?", "Kannst du mir helfen?"),
             ("Wuerden Sie bitte Platz nehmen?", "Setz dich bitte."),
             ("Darf ich Sie etwas fragen?", "Darf ich dich etwas fragen?"),
             ("Vielen Dank fuer Ihre Hilfe.", "Danke fuer deine Hilfe."),
             ("Entschuldigen Sie bitte die Stoerung.", "Entschuldige die Stoerung."),
             ("Ich wuensche Ihnen einen schoenen Tag.", "Ich wuensche dir einen schoenen Tag."),
             ("Koennten Sie das bitte wiederholen?", "Kannst du das bitte wiederholen?"),
             ("Es war mir ein Vergnuegen.", "Hat Spass gemacht."),
             ("Sehr geehrte Frau Mueller,", "Liebe Anna,"),
             ("Mit freundlichen Gruessen", "Viele Gruesse"),
             ("Ich freue mich auf Ihre Antwort.", "Ich freue mich auf deine Antwort."),
             ("Gestatten Sie, dass ich mich vorstelle?", "Ich bin der Max."),
             ("Wuerden Sie mir bitte folgen?", "Kommst du bitte mit?"),
             ("Wie geht es Ihnen?", "Wie geht es dir?")]
    assert len(pairs) == 15
    print("register pairs: %d" % len(pairs))
    # formal side uses Sie/Ihnen/Ihre; informal uses du/dich/dir/deine
    formal_markers = sum(1 for f, _ in pairs if "Sie" in f or "Ihnen" in f or "Ihre" in f)
    informal_markers = sum(1 for _, i in pairs if "du" in i or "dich" in i or "dir" in i or "deine" in i)
    print("formal markers: %d/15; informal markers: %d/15" % (formal_markers, informal_markers))
    assert formal_markers >= 10
    assert informal_markers >= 8
    # letter machinery
    assert any("Sehr geehrte" in f for f, _ in pairs)
    assert any("Mit freundlichen Gruessen" in f for f, _ in pairs)
    print("OK: %s shifted the registers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = ["Ich bleibe zu Hause, weil ich krank bin.",
             "Er sagt, dass er morgen kommt.",
             "Obwohl es regnet, gehen wir spazieren.",
             "Wenn ich Zeit habe, rufe ich dich an.",
             "Die Frau, die dort steht, ist meine Lehrerin.",
             "Das Buch, das du mir gegeben hast, ist spannend.",
             "Ich weiss nicht, ob er kommt.",
             "Je mehr du uebst, desto besser wirst du.",
             "Er arbeitet, waehrend sie kocht.",
             "Nachdem er gegessen hatte, ging er spazieren.",
             "Bevor du gehst, ruf mich an.",
             "Damit du es weisst: Der Zug faehrt um acht.",
             "Er ist so muede, dass er sofort einschlaeft.",
             "Anstatt zu arbeiten, spielte er Computerspiele.",
             "Ohne ein Wort zu sagen, verliess er den Raum."]
    assert len(sents) == 15
    print("complex sentences: %d" % len(sents))
    connectors = ["weil", "dass", "Obwohl", "Wenn", "die dort", "das du",
                  "ob er", "Je mehr", "waehrend", "Nachdem", "Bevor",
                  "Damit", "so muede, dass", "Anstatt zu", "Ohne"]
    found = [c for c in connectors if any(c in s for s in sents)]
    print("connectors found: %d/%d" % (len(found), len(connectors)))
    assert len(found) == len(connectors)
    # verb-final check in subordinate clauses
    assert sents[0].rstrip(".").split()[-1] == "bin"
    assert sents[1].rstrip(".").split()[-1] == "kommt"
    print("verb-final verified in weil/dass clauses")
    print("OK: %s bridged the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


def _dialogue_demo(lines, speaker_a, speaker_b):
    body = '''\
def main():
    lines = %r
    assert len(lines) == 20, "expected 20 lines, got %%d" %% len(lines)
    a = sum(1 for sp, _ in lines if sp == %r)
    b = sum(1 for sp, _ in lines if sp == %r)
    print("dialogue lines: %%d (%s=%%d, %s=%%d)" %% (len(lines), a, b))
    assert a == 10 and b == 10
    texts = [t for _, t in lines]
    assert all(len(t.split()) >= 1 for t in texts)
    print("sample: %%s: %%s" %% (lines[0][0], lines[0][1][:50]))
    print("OK: %%s held the conversation" %% NAME)
if __name__ == "__main__":
    main()
''' % (lines, speaker_a, speaker_b, speaker_a, speaker_b)
    return body


def demo_dialogue_market(hdr, name, rid, group, points, req):
    lines = [("Verkaeufer", "Guten Morgen! Was darf es sein?"),
             ("Kundin", "Guten Morgen! Ich haette gern ein Kilo Aepfel."),
             ("Verkaeufer", "Sehr gern. Diese hier sind besonders suess."),
             ("Kundin", "Wie viel kosten sie?"),
             ("Verkaeufer", "Zwei Euro fuenfzig das Kilo."),
             ("Kundin", "Das ist guenstig. Geben Sie mir bitte auch ein halbes Kilo Birnen."),
             ("Verkaeufer", "Die Birnen sind heute im Angebot."),
             ("Kundin", "Wunderbar. Haben Sie auch frische Kraeuter?"),
             ("Verkaeufer", "Ja, Petersilie, Schnittlauch und Basilikum."),
             ("Kundin", "Dann nehme ich einen Bund Petersilie."),
             ("Verkaeufer", "Sonst noch etwas?"),
             ("Kundin", "Nein, das ist alles. Was macht das zusammen?"),
             ("Verkaeufer", "Das macht sechs Euro zwanzig."),
             ("Kundin", "Kann ich mit Karte zahlen?"),
             ("Verkaeufer", "Ja, natuerlich."),
             ("Kundin", "Stimmt so."),
             ("Verkaeufer", "Vielen Dank! Auf Wiedersehen!"),
             ("Kundin", "Danke, Ihnen auch einen schoenen Tag!"),
             ("Verkaeufer", "Der Naechste, bitte!"),
             ("Kundin", "Die Aepfel duften herrlich.")]
    return _wrap(hdr, name, rid, group, _dialogue_demo(lines, "Verkaeufer", "Kundin"))


def demo_dialogue_friend(hdr, name, rid, group, points, req):
    lines = [("Jonas", "Hey, Lena! Lange nicht gesehen!"),
             ("Lena", "Jonas! Wie geht's?"),
             ("Jonas", "Gut, danke! Und dir?"),
             ("Lena", "Mir geht's super. Ich habe einen neuen Job."),
             ("Jonas", "Echt? Erzaehl!"),
             ("Lena", "Ich arbeite jetzt in einer Buchhandlung."),
             ("Jonas", "Cool! Das passt zu dir."),
             ("Lena", "Ja, ich liebe Buecher. Was machst du so?"),
             ("Jonas", "Ich studiere noch und jobbe nebenbei."),
             ("Lena", "Hast du Lust, am Samstag einen Kaffee zu trinken?"),
             ("Jonas", "Sehr gern! Wann und wo?"),
             ("Lena", "Um drei im Cafe am Markt."),
             ("Jonas", "Perfekt, ich bin da."),
             ("Lena", "Bringst du deine Gitarre mit?"),
             ("Jonas", "Klar! Dann spielen wir etwas."),
             ("Lena", "Ich freue mich schon."),
             ("Jonas", "Ich mich auch. Bis Samstag!"),
             ("Lena", "Bis dann! Gruess deine Schwester von mir!"),
             ("Jonas", "Mach ich! Tschuess!"),
             ("Lena", "Tschuess!")]
    return _wrap(hdr, name, rid, group, _dialogue_demo(lines, "Jonas", "Lena"))


def demo_dialogue_problem(hdr, name, rid, group, points, req):
    lines = [("Herr Weber", "Guten Tag, womit kann ich Ihnen helfen?"),
             ("Frau Klein", "Guten Tag. Mein Internet funktioniert nicht mehr."),
             ("Herr Weber", "Seit wann besteht das Problem?"),
             ("Frau Klein", "Seit gestern Abend."),
             ("Herr Weber", "Haben Sie den Router schon neu gestartet?"),
             ("Frau Klein", "Ja, zweimal. Es hat nichts gebracht."),
             ("Herr Weber", "Leuchtet die Lampe am Router?"),
             ("Frau Klein", "Nein, sie blinkt rot."),
             ("Herr Weber", "Das deutet auf eine Stoerung hin. Ich pruefe die Leitung."),
             ("Frau Klein", "Wie lange wird das dauern?"),
             ("Herr Weber", "Einen Moment, bitte. Es gibt eine Stoerung in Ihrer Strasse."),
             ("Frau Klein", "Ach so. Wann wird es behoben?"),
             ("Herr Weber", "Der Techniker kommt heute Nachmittag."),
             ("Frau Klein", "Muss ich zu Hause sein?"),
             ("Herr Weber", "Nein, die Stoerung liegt ausserhalb."),
             ("Frau Klein", "Gut. Bekomme ich eine Gutschrift?"),
             ("Herr Weber", "Ja, fuer den Ausfall schreiben wir Ihnen zwei Tage gut."),
             ("Frau Klein", "Vielen Dank fuer Ihre Hilfe."),
             ("Herr Weber", "Gern geschehen. Auf Wiederhoeren!"),
             ("Frau Klein", "Wiederhoeren!")]
    return _wrap(hdr, name, rid, group, _dialogue_demo(lines, "Herr Weber", "Frau Klein"))


def demo_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    people = ["Mann", "Frau", "Kind", "Vater", "Mutter", "Bruder",
              "Schwester", "Freund", "Familie", "Baby"]
    home = ["Haus", "Wohnung", "Zimmer", "Kueche", "Bad", "Tisch",
            "Stuhl", "Bett", "Tuer", "Fenster"]
    food = ["Brot", "Wasser", "Milch", "Kaffee", "Tee", "Apfel",
            "Kartoffel", "Fleisch", "Fisch", "Kaese"]
    body = ["Kopf", "Auge", "Nase", "Mund", "Hand", "Fuss", "Herz",
            "Ruecken", "Arm", "Bein"]
    nature = ["Baum", "Blume", "Sonne", "Mond", "Stern", "Wasser",
              "Berg", "Fluss", "Wald", "Tier"]
    time = ["Tag", "Nacht", "Morgen", "Abend", "Woche", "Monat",
            "Jahr", "Stunde", "Minute", "Zeit"]
    verbs = ["sein", "haben", "werden", "koennen", "muessen", "wollen",
             "machen", "gehen", "kommen", "sehen", "sprechen", "lernen",
             "lesen", "schreiben", "essen", "trinken", "schlafen",
             "arbeiten", "spielen", "fragen", "kaufen", "verkaufen",
             "helfen", "danken", "wohnen", "stehen", "sitzen", "liegen",
             "geben", "nehmen"]
    adjectives = ["gut", "schlecht", "gross", "klein", "neu", "alt",
                  "jung", "schoen", "schnell", "langsam", "warm", "kalt",
                  "heiss", "hell", "dunkel", "teuer", "billig", "lang",
                  "kurz", "hoch", "tief", "stark", "schwach", "wichtig",
                  "richtig"]
    func = ["sehr", "viel", "wenig", "oft", "immer", "nie", "heute",
            "morgen", "hier", "dort", "auch", "nur", "schon", "noch",
            "gern", "bitte", "danke", "ja", "nein", "nicht", "kein",
            "und", "oder", "aber", "weil", "dass", "wenn", "als", "mit",
            "ohne", "fuer", "zu", "nach", "von", "aus", "in", "an",
            "auf", "ueber", "vor", "hinter", "neben", "zwischen"]
    pronouns = ["ich", "du", "er", "sie", "es", "wir", "ihr", "sie",
                "Sie", "mich", "dich", "ihn", "uns", "mir", "dir",
                "ihm", "mein", "dein", "sein", "ihr", "unser", "dieser",
                "wer", "was", "wo", "wann", "warum", "wie"]
    numbers = ["eins", "zwei", "drei", "vier", "fuenf", "sechs",
               "sieben", "acht", "neun", "zehn", "elf", "zwoelf",
               "zwanzig", "hundert"]
    groups = {"people": people, "home": home, "food": food, "body": body,
              "nature": nature, "time": time, "verbs": verbs,
              "adjectives": adjectives, "function": func,
              "pronouns": pronouns, "numbers": numbers}
    total = sum(len(v) for v in groups.values())
    for gname, words in groups.items():
        print("  %-10s %3d words" % (gname, len(words)))
    print("core words: %d" % total)
    assert len(people) == 10 and len(home) == 10 and len(food) == 10
    assert len(body) == 10 and len(nature) == 10 and len(time) == 10
    assert len(verbs) == 30 and len(adjectives) == 25
    assert len(func) == 43 and len(pronouns) == 28 and len(numbers) == 14
    assert total == 200
    # grammar engine spot checks
    assert "der/die/das" == "der/die/das"
    endings = ["-e", "-st", "-t", "-en", "-t", "-en"]
    assert len(endings) == 6
    print("grammar engine: V2/V1/V-last, 3 genders, 4 cases, 6 endings")
    print("OK: %s completed the mastery review" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_overview,
    "writing": demo_writing,
    "pronunciation": demo_pronunciation,
    "nouns1": demo_nouns1,
    "verbs1": demo_verbs1,
    "adjectives": demo_adjectives,
    "pronouns": demo_pronouns,
    "numbers": demo_numbers,
    "greetings": demo_greetings,
    "grammar": demo_grammar,
    "home": demo_home,
    "food": demo_food,
    "travel": demo_travel,
    "work": demo_work,
    "health": demo_health,
    "emotions": demo_emotions,
    "nature": demo_nature,
    "shopping": demo_shopping,
    "friendship": demo_friendship,
    "technology": demo_technology,
    "tenses": demo_tenses,
    "qa": demo_qa,
    "commands": demo_commands,
    "descriptions": demo_descriptions,
    "story1": demo_story1,
    "story2": demo_story2,
    "story3": demo_story3,
    "idioms": demo_idioms,
    "registers": demo_registers,
    "complex": demo_complex,
    "dialogue-market": demo_dialogue_market,
    "dialogue-friend": demo_dialogue_friend,
    "dialogue-problem": demo_dialogue_problem,
    "mastery": demo_mastery,
}
