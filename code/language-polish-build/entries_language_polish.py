#!/usr/bin/env python3
"""Entries for the Polish to English databases (34 ladder-ordered records).

Public records: real, fact-checked Polish language teaching - every record
carries Polish content with English translation and example sentences,
organized in the Signature system.
"""
import textwrap

ENTRIES = []


def E(**kw):
    ENTRIES.append(kw)
    return kw


E(
    key="polish_overview", name="Polish Language Overview",
    group="Language overview", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Polish (polski, język polski) is a West Slavic language of the
        Indo-European family, in the Lechitic branch alongside Kashubian and
        the extinct Polabian. About 38 million people speak it as a first
        language in Poland, and roughly 40 to 45 million speak it natively
        worldwide, with heritage communities pushing the total toward 50
        million - making Polish the most spoken Slavic language after Russian
        and Ukrainian, and the most spoken West Slavic language of all. It is
        the official language of Poland and an official language of the
        European Union, and it holds recognized minority status in Lithuania,
        the Czech Republic, Slovakia, Ukraine, Belarus, and Germany. Large
        diaspora communities keep it alive in the United States (Chicago is
        the second-largest Polish-speaking city in the world), the United
        Kingdom, Ireland, Germany, Canada, and Australia. The standard is
        based on the speech of Warsaw and Kraków, guarded by the Rada Języka
        Polskiego (Council for the Polish Language) at the Polish Academy of
        Sciences. Polish grew from the tribal dialects of the Polans, was
        first written in the Latin alphabet in the Middle Ages, survived more
        than a century of partitions when its public use was banned, and
        returned as the voice of an independent nation in 1918. This record
        is the map of the whole database: what Polish is, where it lives,
        and how the ladder below carries a learner from a first greeting to
        full conversation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the overview by anchoring every fact in a
        sentence the learner can say. Each fact - the native name polski, the
        ISO codes pl and pol, the family path, the speaker numbers, the
        official countries, the diaspora cities - appears with a plain
        English explanation and a Polish example sentence. The learner reads
        the facts, then repeats the sentences, so the overview is not
        memorized trivia but spoken language from the first record. Later
        records climb the teaching ladder: foundations (records 1-10: sounds,
        words, grammar basics), compounded (records 11-24: themed sentence
        sets and verb tenses), advanced (records 25-34: stories, idioms,
        registers, complex sentences, conversations, and a full reference)."""),
    key_points=[
        "Native name: polski / język polski; English name: Polish; ISO 639-1: pl; ISO 639-3: pol.",
        "Family: Indo-European > Balto-Slavic > Slavic > West Slavic > Lechitic.",
        "About 38 million native speakers in Poland; 40-45 million natively worldwide; near 50 million total.",
        "Official in Poland and the EU; recognized minority in Lithuania, Czechia, Slovakia, Ukraine, Belarus, Germany.",
        "Standard based on Warsaw and Kraków speech; guarded by the Rada Języka Polskiego (Polish Language Council).",
        "Every record in this database carries Polish content, English translation, and example sentences.",
    ],
    requirements=[
        "No prior knowledge of Polish is needed; this is the starting record of the ladder.",
        "Learners should read each example sentence aloud to begin training pronunciation from day one.",
    ],
    standards=[
        "ISO 639-1:1988 (pl) and ISO 639-3:2007 (pol) language codes.",
        "Rada Języka Polskiego spelling and usage rulings, Polish Academy of Sciences.",
    ],
    citations=[
        "Rada Języka Polskiego. Zasady pisowni i interpunkcji polskiej. Polish Academy of Sciences. The official spelling authority.",
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008. The standard English-language reference grammar.",
        "ISO 639-1:1988 (pl); ISO 639-3:2007 (pol).",
    ],
    sig_lens=("Through the Signature lens, a language is not a school subject - it is a "
              "kept oath between a people and its voice, and Polish is one of the great "
              "kept oaths of human history: banned from schools and offices for over a "
              "century of partitions, it was carried home in kitchens and churches and "
              "returned as the voice of a free nation. This Signature reading treats "
              "the overview as the first seal of that oath."),
)

E(
    key="polish_writing", name="Polish Writing System",
    group="Writing and sound", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Polish is written with the Latin alphabet, read left to right, using
        32 letters: a ą b c ć d e ę f g h i j k l ł m n ń o ó p r s ś t u w y
        z ź ż. The letters q, v, and x appear only in foreign words and
        names (quiz, veto, taxi). Nine letters carry diacritics: the ogonek
        (little tail) under ą and ę marks the famous nasal vowels; the kreska
        (acute stroke) over ć, ń, ó, ś, ź marks soft or changed sounds; the
        kropka (dot) over ż marks the voiced zh sound; and the stroke through
        ł turns L into an English-style W sound. The letter ó is pronounced
        exactly like u (a spelling distinction with a shared sound). Seven
        two-letter digraphs do the work of single sounds: ch (like h), cz
        (ch as in church), sz (sh), rz and ż (zh), dz, dź, dż. The letter i
        softens the consonant before it, as in dzień (day) and nie (no).
        Question marks and exclamation marks work as in English, and Polish
        uses the decimal comma where English uses a point: 3,14 for pi, with
        a thin space for thousands (1 000 000). Numerals are the familiar
        Arabic digits 0-9. Master the 32 letters and the diacritics, and
        every Polish word becomes readable on sight."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the writing system by pairing every letter and
        diacritic with a real word, its pronunciation hint, and its English
        translation. The learner copies the alphabet, sounds each letter with
        its example word - ą as in mąż (husband), ę as in ręka (hand), ł as
        in mały (small), ż as in żona (wife), ó as in Kraków - and practices
        the digraphs by reading paired words: czas (time) with cz, szum
        (rustle) with sz, chleb (bread) with ch. Because Polish spelling is
        highly regular - letters keep their sounds - this one record unlocks
        reading for the entire database."""),
    key_points=[
        "32 letters, left to right; q, v, x only in foreign words.",
        "Ogonek (ą, ę) = nasal vowels; kreska (ć, ń, ó, ś, ź) = soft/changed sounds; kropka (ż); stroke (ł = English w).",
        "ó sounds exactly like u; rz and ż share the zh sound.",
        "Seven digraphs: ch, cz, sz, rz, dz, dź, dż - each one sound.",
        "Decimal comma: 3,14. Familiar digits 0-9. Polish spelling is highly regular - learn the rules once, read everything.",
    ],
    requirements=[
        "Learners should write the alphabet by hand once and say each letter with its example word.",
        "Practice ą, ę, ł, and ś first - they carry the most distinctively Polish sounds.",
    ],
    standards=[
        "Rada Języka Polskiego: official 32-letter alphabet and diacritic rules.",
        "ISO 8859-2 / Unicode Latin Extended-A for ą ć ę ł ń ó ś ź ż.",
    ],
    citations=[
        "Rada Języka Polskiego. Zasady pisowni i interpunkcji polskiej. Polish Academy of Sciences.",
        "Wielki słownik języka polskiego PAN. Polish Academy of Sciences. The national dictionary record of standard spelling.",
    ],
    sig_lens=("Through the Signature lens, the alphabet is the forge: thirty-two "
              "letters hammered into shape over a thousand years, each diacritic "
              "a deliberate strike of the hammer. This Signature reading treats "
              "every ą and ł as proof that a people can stamp its own sound onto "
              "the Latin script and make it unmistakably its own."),
)

E(
    key="polish_phonology", name="Polish Pronunciation and Phonology",
    group="Writing and sound", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Polish pronunciation runs on a few firm rules. Stress falls on the
        penultimate (second-to-last) syllable in almost every word: POlska,
        kraKÓW, jeZYk, teleWIZja. The two nasal vowels ą and ę (as in mąż -
        husband, ręka - hand, gęś - goose) have no English equivalent - hum
        the vowel through the nose. The letter ł sounds like English w
        (mały - small, sounds like MAH-wih), and ó is simply u. Polish is
        famous for its hissing consonant families: the retroflex set sz [sh],
        cz [ch], ż/rz [zh], dż, and the softer alveolo-palatal set ś, ć, ź,
        dź - szum (rustle) versus śnieg (snow) is a distinction worth
        training the ear on. Final consonants devoice: Kraków is pronounced
        kraKUF, chleb (bread) sounds like HLEP, and w before a voiceless
        sound turns to f. The letter h and digraph ch both sound like the
        throaty ch in Scottish loch. Vowels are pure and short: a e i o u y
        never glide the way English vowels do. Ten spoken examples to train
        on: dom (house), woda (water), dzień dobry (good day), dziękuję
        (thank you), przepraszam (excuse me / sorry), tak (yes), nie (no),
        miłość (love), szczęście (happiness), Polska (Poland). Say them
        slowly, stress the penultimate syllable, keep the vowels pure, and
        Polish speakers will understand you."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronunciation by giving every sound an English
        anchor and a drill word. The learner reads the sound inventory - the
        nasal vowels, the ł, the two hissing families, final devoicing, the
        penultimate stress rule - then works the ten spoken-example words
        aloud, exaggerating the stress and the nasal vowels first and
        smoothing them out with repetition. Minimal pairs (szum vs śnieg,
        kasza vs Kasia) train the ear on the consonant families. Record
        yourself, compare with the drill words, and repeat until the stress
        lands on the penultimate syllable without thought."""),
    key_points=[
        "Stress on the penultimate syllable: POlska, kraKÓW, jeZYk.",
        "Nasal vowels ą and ę; ł = English w; ó = u.",
        "Two hissing families: retroflex (sz, cz, ż/rz) and alveolo-palatal (ś, ć, ź, dź).",
        "Final devoicing: Kraków sounds like kraKUF; chleb like HLEP.",
        "Vowels are pure and short - never glide them the English way.",
    ],
    requirements=[
        "Learners should drill the ten spoken-example words aloud daily until stress is automatic.",
        "Practice minimal pairs (szum/śnieg) to separate the two hissing families.",
    ],
    standards=[
        "IPA transcription per the Handbook of the International Phonetic Association: Polish.",
        "Standard Warsaw pronunciation as the reference accent.",
    ],
    citations=[
        "Jassem W. Polish. Journal of the International Phonetic Association. 2003. The standard IPA sketch of Polish sounds.",
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008. Pronunciation chapter.",
    ],
    sig_lens=("Through the Signature lens, pronunciation is the seal pressed "
              "into the wax: the penultimate stress a drumbeat that never "
              "moves, the nasal vowels a hum no other Slavic tongue quite "
              "shares. This Signature reading treats every correctly stressed "
              "word as the learner's own signature taking shape."),
)

E(
    key="polish_nouns", name="Polish Core Nouns I",
    group="Core vocabulary", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Every Polish noun has a gender - masculine, feminine, or neuter -
        and the gender decides the forms of the adjectives and verbs around
        it, so learn each noun with its gender from the start. These 25
        essential nouns cover people, places, and things, each with an
        example sentence: człowiek (m) - man, person: Ten człowiek jest moim
        przyjacielem (This man is my friend). kobieta (f) - woman: Ta kobieta
        jest lekarką (This woman is a doctor). dziecko (n) - child: Dziecko
        śpi (The child is sleeping). dom (m) - house: Nasz dom jest duży (Our
        house is big). książka (f) - book: Czytam ciekawą książkę (I am
        reading an interesting book). woda (f) - water: Piję zimną wodę (I
        drink cold water). chleb (m) - bread: Chleb jest świeży (The bread is
        fresh). mleko (n) - milk: Mleko stoi w lodówce (The milk is in the
        fridge). samochód (m) - car: Samochód stoi na ulicy (The car is on
        the street). ulica (f) - street: Ta ulica jest długa (This street is
        long). miasto (n) - city: Kraków to piękne miasto (Kraków is a
        beautiful city). kraj (m) - country: Polska to mój kraj (Poland is my
        country). świat (m) - world: Świat jest wielki (The world is big).
        imię (n) - first name: Moje imię to Anna (My first name is Anna).
        praca (f) - work, job: Praca zaczyna się o ósmej (Work starts at
        eight). szkoła (f) - school: Szkoła jest blisko (The school is near).
        dzień (m) - day: Dzień jest słoneczny (The day is sunny). noc (f) -
        night: Noc jest cicha (The night is quiet). czas (m) - time: Nie mam
        czasu (I have no time). przyjaciel (m) - friend: To mój najlepszy
        przyjaciel (He is my best friend). rodzina (f) - family: Moja rodzina
        jest duża (My family is big). jedzenie (n) - food: Jedzenie jest
        pyszne (The food is delicious). okno (n) - window: Otwórz okno (Open
        the window). stół (m) - table: Książka leży na stole (The book lies
        on the table). krzesło (n) - chair: Usiądź na krześle (Sit on the
        chair). Learn the gender with the word - ten dom (this house, m), ta
        książka (this book, f), to dziecko (this child, n) - and half of
        Polish grammar falls into place."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nouns as gender-tagged flashcards: each of the
        25 nouns appears with its (m)/(f)/(n) tag, its English meaning, and a
        full sentence showing it in action, with the English translation
        beside it. The learner memorizes noun plus gender together - never
        the bare word - by covering the Polish column and recalling both the
        word and its ten/ta/to pointer. The example sentences are deliberately
        simple so the noun stays the star; later records reuse these nouns in
        harder grammar."""),
    key_points=[
        "25 essential nouns: people, places, things - each with (m)/(f)/(n) gender.",
        "Gender decides adjective and verb forms - learn it with the noun.",
        "Pointers: ten (m), ta (f), to (n) - ten dom, ta książka, to dziecko.",
        "Every noun carries a full translated example sentence.",
        "These 25 nouns recur throughout the database - master them early.",
    ],
    requirements=[
        "Learners must recall each noun with its gender, not the bare word.",
        "Drill with ten/ta/to pointers until gender choice is instant.",
    ],
    standards=[
        "Gender assignment per Wielki słownik języka polskiego PAN.",
        "CEFR A1 vocabulary band: the first nouns a learner needs.",
    ],
    citations=[
        "Wielki słownik języka polskiego PAN. Polish Academy of Sciences.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998. Noun gender chapter.",
    ],
    sig_lens=("Through the Signature lens, a noun is a cornerstone: gender is "
              "the cut of the stone, and every adjective and verb must fit "
              "against it exactly. This Signature reading treats the 25 nouns "
              "as the first course of stones in the learner's own building."),
)

E(
    key="polish_verbs", name="Polish Core Verbs I",
    group="Core vocabulary", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Polish verbs come in aspect pairs: the imperfective for ongoing or
        repeated actions, the perfective for completed ones. Learn each verb
        with its partner. These 25 essential verbs each carry an example
        sentence: być - to be: Jestem zmęczony (I am tired). mieć - to have:
        Mam dwa koty (I have two cats). robić/zrobić - to do, make: Robię
        obiad / Zrobiłem zadanie (I am making dinner / I did the homework).
        jeść/zjeść - to eat: Jem śniadanie / Zjadłem wszystko (I eat
        breakfast / I ate everything). pić/wypić - to drink: Piję kawę /
        Wypiłem herbatę (I drink coffee / I drank the tea). iść/pójść - to
        go (on foot): Idę do szkoły / Poszedłem do kina (I go to school / I
        went to the cinema). jechać/pojechać - to go (by vehicle): Jadę do
        Krakowa / Pojechałem do Gdańska (I am going to Kraków / I went to
        Gdańsk). mówić/powiedzieć - to speak, say: Mówię po polsku /
        Powiedział prawdę (I speak Polish / He told the truth). czytać/
        przeczytać - to read: Czytam książkę / Przeczytałem gazetę (I read a
        book / I read the newspaper [finished]). pisać/napisać - to write:
        Piszę list / Napisałem e-mail (I write a letter / I wrote an email).
        pracować - to work: Pracuję w biurze (I work in an office).
        uczyć się/nauczyć się - to learn: Uczę się polskiego / Nauczyłem się
        pływać (I learn Polish / I learned to swim). spać - to sleep: Śpię
        osiem godzin (I sleep eight hours). mieszkać - to live, reside:
        Mieszkam w Warszawie (I live in Warsaw). kupować/kupić - to buy:
        Kupuję chleb / Kupiłem samochód (I buy bread / I bought a car).
        sprzedawać/sprzedać - to sell: Sprzedaję rower / Sprzedałem dom (I
        sell a bike / I sold the house). gotować/ugotować - to cook: Gotuję
        zupę / Ugotowałem obiad (I cook soup / I cooked dinner). widzieć/
        zobaczyć - to see: Widzę morze / Zobaczyłem ptaka (I see the sea / I
        saw a bird). słyszeć/usłyszeć - to hear: Słyszę muzykę / Usłyszałem
        dzwonek (I hear music / I heard the bell). kochać - to love: Kocham
        cię (I love you). lubić - to like: Lubię lody (I like ice cream).
        czekać - to wait: Czekam na autobus (I wait for the bus).
        dzwonić/zadzwonić - to call, ring: Dzwonię do mamy / Zadzwoniłem do
        lekarza (I call mum / I called the doctor). otwierać/otworzyć - to
        open: Otwieram okno / Otworzyłem drzwi (I open the window / I opened
        the door). zamykać/zamknąć - to close: Zamykam sklep / Zamknąłem
        walizkę (I close the shop / I closed the suitcase). Notice the
        pattern: imperfective first for the open action, perfective for the
        finished one - robić/zrobić, pisać/napisać, jeść/zjeść."""),
    how_it_works=textwrap.dedent("""\
        This record teaches verbs as aspect pairs with living sentences. Each
        of the 25 verbs shows its imperfective and perfective partner where
        the pair exists, its English meaning, and a sentence proving the
        aspect in use - open action versus finished result. The learner
        drills by converting: take an imperfective sentence and finish it
        (Robię obiad -> Zrobiłem obiad), feeling the aspect shift. Record 21
        returns to these verbs for full tense conjugation."""),
    key_points=[
        "25 essential verbs - each with its aspect partner: imperfective/perfective.",
        "Imperfective = ongoing or repeated; perfective = completed.",
        "Common perfective markers: prefixes (z-, po-, prze-, na-, u-) as in pisać/napisać.",
        "Every verb carries a full translated example sentence.",
        "iść (on foot) vs jechać (by vehicle) - Polish splits 'to go' in two.",
    ],
    requirements=[
        "Learners must learn each verb with its aspect partner, not alone.",
        "Drill the conversion: open action to finished result and back.",
    ],
    standards=[
        "Aspect pairs per Wielki słownik języka polskiego PAN.",
        "CEFR A1 verb band: the first verbs a learner needs.",
    ],
    citations=[
        "Wielki słownik języka polskiego PAN. Polish Academy of Sciences.",
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
    ],
    sig_lens=("Through the Signature lens, aspect is the craftsman's two "
              "hands: the imperfective hand keeps shaping, the perfective "
              "hand sets the work down finished. This Signature reading "
              "treats every pair as a signed choice - the learner deciding, "
              "in Polish, whether the work continues or is done."),
)

E(
    key="polish_adjectives", name="Polish Adjectives and Adverbs",
    group="Core vocabulary", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Polish adjectives agree with their noun in gender, number, and case -
        the ending changes to match. The three base forms are masculine,
        feminine, neuter: dobry/dobra/dobre (good). These 25 adjectives each
        show agreement in a sentence: dobry/dobra/dobre - good: dobry
        człowiek, dobra kobieta, dobre dziecko (a good man, woman, child).
        zły/zła/złe - bad: zły dzień (a bad day). duży/duża/duże - big: duży
        dom (a big house). mały/mała/małe - small: mały kot (a small cat).
        nowy/nowa/nowe - new: nowy samochód (a new car). stary/stara/stare -
        old: stara książka (an old book). młody/młoda/młode - young: młody
        chłopak (a young boy). piękny/piękna/piękne - beautiful: piękna
        pogoda (beautiful weather). wysoki/wysoka/wysokie - tall, high:
        wysoki budynek (a tall building). niski/niska/niskie - short, low:
        niski stół (a low table). długi/długa/długie - long: długa droga (a
        long road). krótki/krótka/krótkie - short: krótki film (a short
        film). ciepły/ciepła/ciepłe - warm: ciepła herbata (warm tea).
        zimny/zimna/zimne - cold: zimna woda (cold water). gorący/gorąca/
        gorące - hot: gorąca zupa (hot soup). szybki/szybka/szybkie - fast:
        szybki pociąg (a fast train). wolny/wolna/wolne - slow, free: wolny
        weekend (a free weekend). łatwy/łatwa/łatwe - easy: łatwe zadanie (an
        easy task). trudny/trudna/trudne - difficult: trudny egzamin (a hard
        exam). ważny/ważna/ważne - important: ważna wiadomość (important
        news). szczęśliwy/szczęśliwa/szczęśliwe - happy: szczęśliwa rodzina
        (a happy family). smutny/smutna/smutne - sad: smutna historia (a sad
        story). zdrowy/zdrowa/zdrowe - healthy: zdrowe jedzenie (healthy
        food). chory/chora/chore - sick: chory pacjent (a sick patient).
        głodny/głodna/głodne - hungry: głodny turysta (a hungry tourist).
        Adverbs do not change - 15 essentials: dobrze (well), źle (badly),
        szybko (quickly), wolno (slowly), bardzo (very), mało (little), dużo
        (a lot), często (often), rzadko (rarely), zawsze (always), nigdy
        (never), teraz (now), tutaj (here), tam (there), dziś (today).
        Mówię dobrze po polsku (I speak Polish well). On zawsze się spóźnia
        (He is always late). Note the adverb rule: many adverbs come from
        the adjective's neuter form - dobry -> dobrze, szybki -> szybko."""),
    how_it_works=textwrap.dedent("""\
        This record teaches agreement as a matching game. Each adjective
        appears in its three gender forms with a sentence proving each form
        against a noun of that gender; the learner practices by swapping the
        noun and re-cutting the ending - dobry człowiek, dobra kobieta,
        dobre dziecko. Adverbs are drilled as fixed words in sentences, with
        the adjective-to-adverb derivation rule (dobry -> dobrze) as the
        shortcut. Agreement drills from this record feed every sentence set
        that follows."""),
    key_points=[
        "25 adjectives in masculine/feminine/neuter: dobry/dobra/dobre.",
        "Adjectives agree in gender, number, and case with their noun.",
        "15 adverbs - fixed forms: dobrze, szybko, bardzo, zawsze, nigdy.",
        "Adverb shortcut: many derive from the adjective - dobry -> dobrze.",
        "Every adjective and adverb carries a translated example sentence.",
    ],
    requirements=[
        "Learners must produce all three gender forms of each adjective.",
        "Drill noun-swapping until the ending follows the noun automatically.",
    ],
    standards=[
        "Agreement rules per Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
        "CEFR A1 adjective and adverb bands.",
    ],
    citations=[
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
        "Wielki słownik języka polskiego PAN. Polish Academy of Sciences.",
    ],
    sig_lens=("Through the Signature lens, agreement is tailoring: the "
              "adjective cut to fit the noun it clothes, no loose endings. "
              "This Signature reading treats every matched ending as a "
              "fitted seam in the learner's growing garment of Polish."),
)

E(
    key="polish_pronouns", name="Polish Pronouns",
    group="Core vocabulary", ladder_rank=4, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Polish pronouns change by case, and Polish drops the subject pronoun
        whenever the verb ending already says who acts - (ja) jestem means
        the jest- ending already carries 'I'. Personal pronouns: ja (I),
        ty (you, informal singular), on (he), ona (she), ono (it), my (we),
        wy (you, plural/informal plural), oni (they, masculine-personal),
        one (they, all other). Example: Ja jestem Polakiem; ty jesteś moim
        przyjacielem (I am Polish; you are my friend). Ona czyta książkę; on
        pisze list (She reads a book; he writes a letter). Possessives agree
        like adjectives: mój/moja/moje (my), twój/twoja/twoje (your), jego
        (his), jej (her), nasz/nasza/nasze (our), wasz/wasza/wasze (your
        plural), ich (their). Mój dom, moja książka, moje dziecko (my house,
        my book, my child). Demonstratives: ten/ta/to (this), tamten/tamta/
        tamto (that). Ten pan, ta pani, to dziecko (this gentleman, this
        lady, this child). Interrogatives: kto (who), co (what), jaki/jaka/
        jakie (what kind of), gdzie (where), kiedy (when), dlaczego (why),
        jak (how), ile (how much/many), czyj/czyja/czyje (whose). Kto to
        jest? (Who is it?). Gdzie mieszkasz? (Where do you live?). Ile to
        kosztuje? (How much does it cost?). Formal address avoids ty: pan
        (sir, to a man), pani (madam, to a woman), państwo (to a couple or
        group), used with third-person verbs - Czy pan mówi po angielsku?
        (Do you speak English, sir?). Reflexive się marks actions turned
        back on the subject: nazywam się Anna (my name is Anna - literally
        'I call myself Anna'), uczę się polskiego (I learn Polish). Master
        the pronouns and half of Polish conversation is already yours."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronouns as full paradigms with sentences, not
        as a bare list. Each pronoun family - personal, possessive,
        demonstrative, interrogative - appears in a table with its gender
        forms, then in sentences that prove each form in action. The learner
        drills by substitution: take a sentence with ja and re-run it through
        ty, on, my, wy, oni, changing the verb ending each time. The formal
        pan/pani forms get their own drill, since they flip the verb to
        third person. Record 29 returns to formal address in depth."""),
    key_points=[
        "Personal pronouns: ja, ty, on/ona/ono, my, wy, oni/one - subject often dropped.",
        "oni (masculine-personal they) vs one (all other they) - a distinction English lacks.",
        "Possessives agree like adjectives: mój/moja/moje.",
        "Formal address: pan, pani, państwo with third-person verbs.",
        "Interrogatives: kto, co, gdzie, kiedy, dlaczego, jak, ile - each with a sentence.",
    ],
    requirements=[
        "Learners must drill pronoun substitution with matching verb endings.",
        "Practice pan/pani forms separately - the third-person verb flip is the trap.",
    ],
    standards=[
        "Pronoun paradigms per Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed.",
        "CEFR A1 pronoun objectives.",
    ],
    citations=[
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
    ],
    sig_lens=("Through the Signature lens, pronouns are the signet ring: small, "
              "carried everywhere, and they stamp every sentence with who is "
              "speaking. This Signature reading treats the dropped ja - the "
              "verb ending doing the work alone - as elegance: the signature "
              "implied, not repeated."),
)

E(
    key="polish_numbers", name="Polish Numbers and Time",
    group="Core vocabulary", ladder_rank=4, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Polish numbers run 1-10: jeden, dwa, trzy, cztery, pięć, sześć,
        siedem, osiem, dziewięć, dziesięć. Teens add -naście: jedenaście (11),
        dwanaście (12), trzynaście (13), czternaście (14), piętnaście (15),
        szesnaście (16), siedemnaście (17), osiemnaście (18), dziewiętnaście
        (19). Tens: dwadzieścia (20), trzydzieści (30), czterdzieści (40),
        pięćdziesiąt (50), sześćdziesiąt (60), siedemdziesiąt (70),
        osiemdziesiąt (80), dziewięćdziesiąt (90). Hundreds: sto (100),
        dwieście (200), trzysta (300); tysiąc (1000), milion (million).
        Compose freely: dwadzieścia jeden (21), sto pięćdziesiąt trzy (153).
        Ordinals: pierwszy (1st), drugi (2nd), trzeci (3rd), czwarty (4th),
        piąty (5th). Mam trzy koty (I have three cats). To jest mój pierwszy
        raz w Polsce (This is my first time in Poland). Days: poniedziałek,
        wtorek, środa, czwartek, piątek, sobota, niedziela. Months: styczeń,
        luty, marzec, kwiecień, maj, czerwiec, lipiec, sierpień, wrzesień,
        październik, listopad, grudzień. Seasons: wiosna (spring), lato
        (summer), jesień (autumn), zima (winter). W poniedziałek idę do pracy
        (On Monday I go to work). Urodziłem się w maju (I was born in May).
        Clock time: Która godzina? (What time is it?). Jest trzecia (It is
        three o'clock). Jest wpół do czwartej (It is half past three -
        literally 'half to four'). Spotkamy się o piątej (We meet at five).
        Dates: Dziś jest pierwszy maja (Today is the first of May). Numbers
        govern noun cases - jeden dom, dwa domy, pięć domów (1 house, 2
        houses, 5 houses) - the full case rule waits in record 10, but learn
        the pattern with the numbers now."""),
    how_it_works=textwrap.dedent("""\
        This record teaches numbers as a construction kit: the learner
        memorizes 1-10, the -naście teens, and the tens, then builds any
        number to 100 by composition, checking each build against the
        engine in the demonstration program. Days, months, and seasons are
        learned as recited chains with a sentence each. Clock time is taught
        with the o + locative pattern (o piątej - at five) and the famous
        wpół do (half to) construction. Every number, day, month, and time
        phrase appears in a translated example sentence."""),
    key_points=[
        "1-100 by construction: jeden...dziesięć, -naście teens, -dzieści/-dziesiąt tens.",
        "sto (100), tysiąc (1000), milion - compose freely: sto pięćdziesiąt trzy.",
        "Ordinals: pierwszy, drugi, trzeci, czwarty, piąty.",
        "Days, months, seasons as recited chains - poniedziałek through grudzień.",
        "Clock time: o + locative (o piątej); wpół do = half to the next hour.",
    ],
    requirements=[
        "Learners must build any number 1-100 from parts before moving on.",
        "Recite days and months in order, each with a sentence.",
    ],
    standards=[
        "Cardinal and ordinal forms per Wielki słownik języka polskiego PAN.",
        "CEFR A1 number, date, and time objectives.",
    ],
    citations=[
        "Wielki słownik języka polskiego PAN. Polish Academy of Sciences.",
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008. Numerals chapter.",
    ],
    sig_lens=("Through the Signature lens, numbers are the ledger: every "
              "transaction of daily life - the price, the hour, the date - "
              "entered exactly. This Signature reading treats dwadzieścia "
              "jeden as twenty-one small signatures adding up to one exact "
              "total."),
)

E(
    key="polish_greetings", name="Polish Greetings and Everyday Phrases",
    group="Core vocabulary", ladder_rank=5, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Polish politeness runs on the right greeting for the right hour and
        the right person. Thirty essentials with usage notes: Dzień dobry
        (good day - the all-purpose formal hello, morning to evening).
        Dobry wieczór (good evening - after dark). Dobranoc (good night -
        only when parting for sleep). Cześć (hi, bye - informal, friends and
        family). Hej (hey - very informal). Witam (welcome / I welcome you -
        formal, often the host's greeting). Do widzenia (goodbye - formal).
        Do zobaczenia (see you - neutral). Na razie (see you soon -
        informal). Pa pa (bye-bye - affectionate). Dziękuję (thank you);
        Dziękuję bardzo (thank you very much). Proszę (please / here you are
        / you're welcome - the great multi-tool word). Przepraszam (excuse
        me / I'm sorry). Nie ma za co (you're welcome - literally 'there is
        nothing for it'). Nie szkodzi (it doesn't matter / no harm done).
        Tak (yes). Nie (no). Może (maybe). Smacznego (enjoy your meal - said
        to fellow diners). Na zdrowie (cheers / bless you - literally 'to
        health'). Sto lat (a hundred years - the birthday song and toast).
        Powodzenia (good luck). Miłego dnia (have a nice day). Do usłyszenia
        (goodbye on the phone - 'until we hear each other'). Jak się masz?
        (how are you - informal); Jak się pan ma? (formal). Dziękuję,
        dobrze (fine, thank you). Miło mi (nice to meet you). Proszę bardzo
        (here you are / emphatic you're welcome). Słucham? (I'm listening? -
        answering the phone or asking someone to repeat). Usage notes: use
        Dzień dobry with strangers and elders, never Cześć; say proszę when
        handing something over; answer the phone with słucham or halo; wish
        Smacznego before eating together. Thirty phrases, and you can greet,
        thank, apologize, and part like a Pole."""),
    how_it_works=textwrap.dedent("""\
        This record teaches phrases as social tools, each with its exact
        situation. The learner sorts the 30 phrases into hello, goodbye,
        thanks, apology, and well-wishing piles, then role-plays each pile:
        entering a shop (Dzień dobry), leaving (Do widzenia), receiving
        change (Dziękuję), bumping someone (Przepraszam). The usage notes are
        the lesson - the wrong greeting marks the foreigner faster than the
        wrong case ending. Drill until Dzień dobry comes out before Cześć
        with strangers."""),
    key_points=[
        "30 greetings, farewells, and politeness phrases - each with a usage note.",
        "Dzień dobry for strangers and elders; Cześć only for friends and family.",
        "Proszę is the multi-tool: please, here you are, you're welcome.",
        "Phone: słucham or halo to answer; Do usłyszenia to hang up.",
        "Smacznego before meals, Na zdrowie for toasts and sneezes, Sto lat for birthdays.",
    ],
    requirements=[
        "Learners must sort phrases by situation and role-play each pile.",
        "Practice the formal/informal split until it is automatic.",
    ],
    standards=[
        "Pragmatic norms per Rada Języka Polskiego usage guidance.",
        "CEFR A1 interaction phrases.",
    ],
    citations=[
        "Rada Języka Polskiego. Usage and politeness guidance. Polish Academy of Sciences.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998. Everyday expressions.",
    ],
    sig_lens=("Through the Signature lens, a greeting is the handshake before "
              "the contract: Dzień dobry offered properly opens every door in "
              "Poland. This Signature reading treats the thirty phrases as "
              "thirty keys, each cut for its own lock."),
)

E(
    key="polish_grammar", name="Polish Grammar Essentials",
    group="Grammar", ladder_rank=5, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Polish grammar stands on seven cases - the endings that say what job
        a noun does in the sentence. The cases with their questions: 1.
        mianownik (nominative, who? what?) - kot śpi (the cat sleeps). 2.
        dopełniacz (genitive, of whom? of what?) - ogon kota (the cat's
        tail); nie mam czasu (I have no time - negation takes genitive). 3.
        celownik (dative, to whom?) - daję kotu mleko (I give the cat milk).
        4. biernik (accusative, whom? what?) - widzę kota (I see the cat).
        5. narzędnik (instrumental, with whom? with what?) - idę z kotem (I
        go with the cat); jestem lekarzem (I am a doctor - profession takes
        instrumental). 6. miejscownik (locative, about whom? where?) - mówię
        o kocie (I talk about the cat); w domu (in the house). 7. wołacz
        (vocative, O!) - kocie, chodź tu (kitty, come here). Word order is
        SVO at heart but flexible - emphasis moves words: Kota widzę (It is
        the cat I see). There are no articles - kot means 'cat', 'a cat', or
        'the cat' by context. Three genders with a masculine split:
        masculine-personal (panowie - gentlemen), masculine-animate (kot),
        masculine-inanimate (stół). Negation is nie before the verb: nie
        wiem (I don't know), nie rozumiem (I don't understand) - and nie
        flips the accusative object to genitive: widzę kota but nie widzę
        kota (I see the cat / I don't see the cat - genitive). Questions use
        rising intonation, question words (kto, co, gdzie), or czy at the
        front: Czy mówisz po polsku? (Do you speak Polish?). Commands and
        formal address wait in records 23 and 29; tenses in record 21. Learn
        the seven case questions and every ending has a reason."""),
    how_it_works=textwrap.dedent("""\
        This record teaches grammar as a job chart: each of the seven cases
        is introduced by its question word and one model sentence, and the
        learner parses new sentences by asking the questions - kto? kogo?
        komu? - until the case choice is mechanical. Word order is taught by
        moving one emphasized word and hearing the meaning shift. Negation is
        drilled as a two-step: add nie, flip the object to genitive. Every
        rule carries translated example sentences, and the demonstration
        program quizzes case identification on real sentences."""),
    key_points=[
        "Seven cases, each with its question: mianownik, dopełniacz, celownik, biernik, narzędnik, miejscownik, wołacz.",
        "No articles - context decides a/the.",
        "SVO base with flexible order for emphasis.",
        "Negation: nie + verb, and the object flips to genitive.",
        "Questions: intonation, question words, or fronted czy.",
    ],
    requirements=[
        "Learners must parse sentences by asking the case questions.",
        "Drill negation pairs until the genitive flip is automatic.",
    ],
    standards=[
        "Case system per Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed.",
        "CEFR A1-A2 grammar scope.",
    ],
    citations=[
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998. Case chapters.",
    ],
    sig_lens=("Through the Signature lens, the seven cases are seven stamps "
              "on the same document, each marking the noun's exact office. "
              "This Signature reading treats grammar not as rules to fear "
              "but as precision instruments - the signature valid only when "
              "every stamp is in place."),
)

E(
    key="polish_home_family", name="Polish Home and Family Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the house and the people in it: Mieszkam w
        dużym domu (I live in a big house). Nasze mieszkanie ma trzy pokoje
        (Our apartment has three rooms). Salon jest jasny i przytulny (The
        living room is bright and cozy). Kuchnia jest obok jadalni (The
        kitchen is next to the dining room). Sypialnia jest na piętrze (The
        bedroom is upstairs). Łazienka ma nowe kafelki (The bathroom has new
        tiles). Ogród jest za domem (The garden is behind the house). Moja
        mama gotuje obiad (My mum cooks dinner). Tata czyta gazetę w salonie
        (Dad reads the newspaper in the living room). Moja siostra ma
        dwadzieścia lat (My sister is twenty years old). Mój brat studiuje
        medycynę (My brother studies medicine). Babcia piecze ciasto (Grandma
        bakes a cake). Dziadek opowiada historie (Grandpa tells stories).
        Mój mąż pracuje w banku (My husband works in a bank). Moja żona jest
        nauczycielką (My wife is a teacher). Nasze dzieci bawią się w
        ogrodzie (Our children play in the garden). Kot śpi na kanapie (The
        cat sleeps on the sofa). Pies szczeka na listonosza (The dog barks at
        the postman). Sprzątam mieszkanie w soboty (I clean the apartment on
        Saturdays). Wieczorem cała rodzina je kolację razem (In the evening
        the whole family eats supper together). Note the family nouns -
        mama, tata, siostra, brat, babcia, dziadek, mąż, żona - and the
        locative case doing the location work: w salonie, w ogrodzie, na
        kanapie."""),
    how_it_works=textwrap.dedent("""\
        This record teaches home and family vocabulary inside complete
        sentences, never as bare words. Each of the 20 sentences pairs a
        room, a family member, or a household action with its English
        translation; the learner reads the Polish, covers it, and rebuilds
        it from the English. Location sentences double as locative-case
        practice (w salonie, na kanapie). The family nouns drilled here -
        mama, tata, siostra, brat, babcia, dziadek - return in every later
        record."""),
    key_points=[
        "20 sentences: rooms, furniture, household actions, family members.",
        "Family nouns: mama, tata, siostra, brat, babcia, dziadek, mąż, żona.",
        "Location practice doubles as locative-case training.",
        "Every sentence fully translated; rebuild Polish from English.",
        "Weekend and evening routines in natural sentences.",
    ],
    requirements=[
        "Learners must rebuild each Polish sentence from its English translation.",
        "Name every family member and room aloud without notes.",
    ],
    standards=[
        "CEFR A1 home and family vocabulary.",
        "Locative case usage per standard grammars.",
    ],
    citations=[
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
        "Narodowy Korpus Języka Polskiego. Frequency-checked everyday vocabulary.",
    ],
    sig_lens=("Through the Signature lens, the home is the first archive: "
              "every room a drawer of words, every family member a living "
              "record. This Signature reading treats dom not as a building "
              "but as the vault where the language is kept warm."),
)

E(
    key="polish_food_cooking", name="Polish Food and Cooking Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences from the Polish table - pierogi, bigos, żurek, and
        the daily kitchen: Jem śniadanie o siódmej (I eat breakfast at
        seven). Na śniadanie jem jajka i chleb (For breakfast I eat eggs and
        bread). Obiad jest najważniejszym posiłkiem dnia (Dinner is the most
        important meal of the day). Babcia robi najlepsze pierogi (Grandma
        makes the best pierogi). Pierogi ruskie są z ziemniakami i serem
        (Ruskie pierogi are with potatoes and cheese). Bigos gotuje się
        kilka godzin (Bigos cooks for several hours). Żurek smakuje
        wyśmienicie (Żurek tastes delicious). Rosół jest na niedzielę (Broth
        is for Sunday). Kotlet schabowy z kapustą to klasyk (Pork cutlet with
        cabbage is a classic). Poproszę kawę i sernik (Coffee and cheesecake,
        please). Herbata jest za gorąca (The tea is too hot). Chleb razowy
        jest zdrowy (Wholemeal bread is healthy). Kupuję warzywa na targu
        (I buy vegetables at the market). Kroję cebulę i marchewkę (I chop
        the onion and carrot). Gotuję zupę pomidorową (I cook tomato soup).
        Smażę naleśniki na patelni (I fry pancakes in the pan). Piekę chleb
        w piekarniku (I bake bread in the oven). Solę i pieprzę do smaku (I
        salt and pepper to taste). Kolacja będzie o dziewiętnastej (Supper
        will be at seven pm). Smacznego! (Enjoy your meal!). The verbs of
        the kitchen - kroić (chop), gotować (cook/boil), smażyć (fry), piec
        (bake), solić (salt) - and the great Polish dishes, all in working
        sentences."""),
    how_it_works=textwrap.dedent("""\
        This record teaches food vocabulary through the day's meals and the
        kitchen's actions. Each of the 20 sentences names a dish, an
        ingredient, or a cooking verb with its English translation; the
        learner cooks along in Polish - narrating kroję, gotuję, smażę while
        miming the actions. The classic dishes (pierogi, bigos, żurek,
        rosół, kotlet schabowy) anchor cultural vocabulary. Restaurant
        sentences (Poproszę kawę) get spoken drill until ordering is fluent."""),
    key_points=[
        "20 sentences: meals, ingredients, cooking verbs, restaurant ordering.",
        "Classic dishes: pierogi, bigos, żurek, rosół, kotlet schabowy.",
        "Kitchen verbs: kroić, gotować, smażyć, piec, solić.",
        "Poproszę + accusative is the ordering formula.",
        "Every sentence fully translated; narrate cooking in Polish.",
    ],
    requirements=[
        "Learners must narrate a full meal's preparation in Polish.",
        "Order a three-course meal aloud using Poproszę.",
    ],
    standards=[
        "CEFR A1 food and restaurant vocabulary.",
        "Culinary terms per standard usage.",
    ],
    citations=[
        "Narodowy Korpus Języka Polskiego. Everyday food vocabulary frequencies.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
    ],
    sig_lens=("Through the Signature lens, the kitchen is the laboratory "
              "where the language proves itself daily: every recipe a "
              "procedure, every shared meal a countersigned document. This "
              "Signature reading treats Smacznego as the seal on the day's "
              "work."),
)

E(
    key="polish_travel", name="Polish Travel and Directions Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for moving through Poland - transport, directions,
        tickets, lodging: Gdzie jest dworzec kolejowy? (Where is the train
        station?). Jak dojść do rynku? (How do I get to the market square?).
        Proszę prosto, potem w lewo (Straight ahead, then left). Czy to
        daleko stąd? (Is it far from here?). Jadę pociągiem do Krakowa (I
        go by train to Kraków). Pociąg odjeżdża o dziesiątej (The train
        leaves at ten). Poproszę bilet powrotny do Gdańska (A return ticket
        to Gdańsk, please). Gdzie jest peron drugi? (Where is platform two?).
        Autobus jest spóźniony (The bus is late). Taksówka czeka na dole
        (The taxi waits downstairs). Ile kosztuje przejazd na lotnisko? (How
        much is the ride to the airport?). Zatrzymam się w hotelu trzy noce
        (I will stay in a hotel three nights). Czy jest wolny pokój? (Is
        there a free room?). Poproszę pokój z widokiem (A room with a view,
        please). Śniadanie jest wliczone? (Is breakfast included?). Gdzie
        mogę wypożyczyć rower? (Where can I rent a bike?). Mapa miasta
        bardzo pomaga (A city map helps a lot). Zgubiłem się - proszę o
        pomoc (I am lost - please help). Mówię tylko trochę po polsku (I
        speak only a little Polish). Dziękuję za pomoc! (Thanks for your
        help!). The direction verbs - iść/jeździć, dojść, skręcić - and the
        ticket formulas, all in sentences a traveler actually says."""),
    how_it_works=textwrap.dedent("""\
        This record teaches travel Polish as survival scripts. Each of the
        20 sentences is a line a traveler really speaks - asking the way,
        buying the ticket, booking the room - with its English translation.
        The learner role-plays both sides: the lost traveler and the helpful
        local, swapping the direction words (prosto, w lewo, w prawo).
        Ticket and hotel sentences get drilled as fixed formulas until they
        come out under pressure."""),
    key_points=[
        "20 sentences: transport, directions, tickets, lodging.",
        "Direction core: prosto, w lewo, w prawo, daleko, blisko.",
        "Poproszę + accusative buys tickets and books rooms.",
        "Zgubiłem się - the most useful sentence a traveler knows.",
        "Role-play both sides: traveler and local.",
    ],
    requirements=[
        "Learners must ask for and give directions without notes.",
        "Buy a ticket and book a room in a spoken role-play.",
    ],
    standards=[
        "CEFR A1 travel and accommodation vocabulary.",
        "Standard transport terminology.",
    ],
    citations=[
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
        "Narodowy Korpus Języka Polskiego. Travel-domain frequencies.",
    ],
    sig_lens=("Through the Signature lens, travel sentences are the "
              "passport: each one stamped by a real situation, each one "
              "proving the bearer can move through the country. This "
              "Signature reading treats Gdzie jest dworzec? as the first "
              "stamp in the learner's own travel document."),
)

E(
    key="polish_work_school", name="Polish Work and School Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the office and the classroom: Pracuję jako
        inżynier (I work as an engineer). Zaczynam pracę o ósmej rano (I
        start work at eight in the morning). Mam spotkanie o dziesiątej
        (I have a meeting at ten). Szef prosi o raport (The boss asks for a
        report). Muszę skończyć projekt do piątku (I must finish the project
        by Friday). Wysyłam e-mail do klienta (I send an email to the
        client). Kolega pomaga mi z zadaniem (A colleague helps me with the
        task). Idę na przerwę obiadową (I go on lunch break). Kończę pracę
        o szesnastej (I finish work at four pm). Jestem nauczycielem
        matematyki (I am a math teacher - instrumental case for professions).
        Uczę się polskiego od roku (I have learned Polish for a year). Szkoła
        zaczyna się we wrześniu (School starts in September). Lekcja trwa
        czterdzieści pięć minut (A lesson lasts forty-five minutes). Uczeń
        odpowiada na pytanie (The pupil answers the question). Studentka
        pisze egzamin (The student writes the exam). Nauczyciel sprawdza
        prace domowe (The teacher checks the homework). Czytam podręcznik
        do chemii (I read the chemistry textbook). Uczę się słówek na pamięć
        (I learn vocabulary by heart). Dostałem piątkę z polskiego (I got an
        A in Polish - piątka, the top grade). Wakacje zaczynają się w lipcu
        (Holidays start in July). Note jestem + instrumental for professions
        (jestem nauczycielem), and the grade scale where 5 is the best."""),
    how_it_works=textwrap.dedent("""\
        This record teaches work and school vocabulary in the sentences
        where they live. Each of the 20 sentences carries its English
        translation; office sentences drill the instrumental of profession
        (jestem inżynierem) and deadline language (do piątku), while school
        sentences drill the grade scale and lesson vocabulary. The learner
        describes their own job and school day in Polish, swapping in their
        real details. Every sentence is a template the learner reuses with
        their own life."""),
    key_points=[
        "20 sentences: jobs, office routines, classroom, learning.",
        "Jestem + instrumental names professions: jestem nauczycielem.",
        "Grade scale: 5 (piątka) is the top grade, 1 the lowest.",
        "Deadline formula: do + genitive (do piątku - by Friday).",
        "Describe your own job and school day using these templates.",
    ],
    requirements=[
        "Learners must describe their own work or studies in 10 Polish sentences.",
        "Drill jestem + instrumental for five professions.",
    ],
    standards=[
        "CEFR A1-A2 work and education vocabulary.",
        "Instrumental of profession per standard grammars.",
    ],
    citations=[
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
        "Narodowy Korpus Języka Polskiego. Work-domain frequencies.",
    ],
    sig_lens=("Through the Signature lens, work sentences are the daily "
              "ledger entries of a life: each meeting, each lesson, each "
              "finished project signed off in Polish. This Signature reading "
              "treats Dostałem piątkę as a seal of excellence the learner "
              "can earn in the language itself."),
)

E(
    key="polish_health_body", name="Polish Health and Body Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the body, symptoms, the doctor, and the
        pharmacy: Boli mnie głowa (My head hurts - literally 'the head
        hurts me'). Boli mnie gardło (My throat hurts). Mam gorączkę (I
        have a fever). Mam katar i kaszel (I have a cold and a cough). Źle
        się czuję (I feel bad). Jestem przeziębiony (I have a cold -
        masculine) / Jestem przeziębiona (feminine). Muszę iść do lekarza
        (I must go to the doctor). Umawiam się na wizytę (I make an
        appointment). Lekarz mierzy ciśnienie (The doctor measures blood
        pressure). Boli mnie tutaj, po lewej stronie (It hurts here, on the
        left side). Od kiedy pan choruje? (Since when have you been ill,
        sir? - formal). Biorę lekarstwo dwa razy dziennie (I take the
        medicine twice a day). Gdzie jest najbliższa apteka? (Where is the
        nearest pharmacy?). Poproszę coś na ból głowy (Something for a
        headache, please). Czy to jest na receptę? (Is this prescription
        only?). Odpoczywaj i pij dużo wody (Rest and drink lots of water).
        Wracaj do zdrowia! (Get well!). Body parts: głowa (head), oko
        (eye), nos (nose), usta (mouth), ręka (hand/arm), noga (leg/foot),
        serce (heart), plecy (back). Mam zdrowe serce (I have a healthy
        heart). Myję ręce przed jedzeniem (I wash my hands before eating).
        The боли mnie + nominative pattern (boli mnie głowa) is the key to
        describing all pain."""),
    how_it_works=textwrap.dedent("""\
        This record teaches health Polish as the sentences you hope you
        never need but must have ready. Each of the 20 sentences pairs a
        body part, a symptom, or a pharmacy line with its English
        translation. The boli mnie + nominative pattern is drilled as the
        master key - swap any body part into it. The learner role-plays
        patient and doctor, then patient and pharmacist, until describing
        symptoms is fluent under stress."""),
    key_points=[
        "20 sentences: body parts, symptoms, doctor visit, pharmacy.",
        "Boli mnie + nominative is the pain pattern: boli mnie głowa.",
        "Body parts: głowa, oko, nos, ręka, noga, serce, plecy.",
        "Pharmacy formula: Poproszę coś na + accusative.",
        "Role-play patient/doctor and patient/pharmacist until fluent.",
    ],
    requirements=[
        "Learners must describe five symptoms using boli mnie without notes.",
        "Role-play a full pharmacy visit in Polish.",
    ],
    standards=[
        "CEFR A1 health vocabulary; standard medical terminology.",
        "Dative-experiencer construction per standard grammars.",
    ],
    citations=[
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
        "Wielki słownik języka polskiego PAN. Medical vocabulary.",
    ],
    sig_lens=("Through the Signature lens, health sentences are the most "
              "serious signatures a learner signs: the body reporting its "
              "state exactly, the pharmacist reading it back exactly. This "
              "Signature reading treats Boli mnie głowa as a sworn "
              "statement - precise, because precision matters."),
)

E(
    key="polish_emotions", name="Polish Emotions and Feelings Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the inner life - joy, sadness, anger, fear,
        love, surprise: Jestem bardzo szczęśliwy (I am very happy -
        masculine) / Jestem bardzo szczęśliwa (feminine). Cieszę się z
        twojego sukcesu (I am glad about your success). To wspaniała
        wiadomość! (That is wonderful news!). Jest mi smutno (I am sad -
        literally 'it is sad to me'). Płaczę ze wzruszenia (I cry from
        emotion). Tęsknię za domem (I miss home). Jestem zły na niego (I am
        angry at him). To mnie denerwuje (That annoys me). Uspokój się,
        proszę (Calm down, please). Boję się ciemności (I am afraid of the
        dark). Nie martw się, wszystko będzie dobrze (Don't worry,
        everything will be fine). Kocham cię z całego serca (I love you with
        all my heart). Uwielbiam spędzać z tobą czas (I adore spending time
        with you). Jestem zakochany (I am in love - masculine) / Jestem
        zakochana (feminine). To dla mnie bardzo ważne (This is very
        important to me). Jestem zaskoczony (I am surprised - masculine) /
        Jestem zaskoczona (feminine). Nie mogę w to uwierzyć! (I can't
        believe it!). Czuję ulgę (I feel relief). Jestem dumny z mojego syna
        (I am proud of my son). Dziękuję za wsparcie (Thank you for your
        support). Note the dative of feeling - jest mi smutno, jest mi
        zimno - feelings happen 'to me' in Polish, and cieszę się / boję się
        carry the reflexive się."""),
    how_it_works=textwrap.dedent("""\
        This record teaches emotion vocabulary as complete feeling
        statements. Each of the 20 sentences names an emotion with its
        English translation and the exact Polish construction - the dative
        of feeling (jest mi smutno), the reflexive verbs (cieszę się, boję
        się), the gender-split adjectives (szczęśliwy/szczęśliwa). The
        learner keeps a one-week feelings diary in Polish, one sentence a
        day, cycling through all six emotion families. Drill the masculine
        and feminine forms side by side."""),
    key_points=[
        "20 sentences across six families: happy, sad, angry, afraid, love, surprise.",
        "Dative of feeling: jest mi smutno, jest mi zimno.",
        "Reflexive emotion verbs: cieszę się, boję się, martwię się.",
        "Adjectives split by gender: szczęśliwy/szczęśliwa, zakochany/zakochana.",
        "Keep a one-week feelings diary in Polish.",
    ],
    requirements=[
        "Learners must produce both gender forms of each emotion adjective.",
        "Write seven diary sentences, one per day, in Polish.",
    ],
    standards=[
        "CEFR A1-A2 emotion vocabulary.",
        "Dative experiencer and reflexive constructions per standard grammars.",
    ],
    citations=[
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
        "Narodowy Korpus Języka Polskiego. Emotion vocabulary frequencies.",
    ],
    sig_lens=("Through the Signature lens, emotion sentences are the "
              "confessionals of the language: the heart signing its name to "
              "exactly what it feels. This Signature reading treats Kocham "
              "cię z całego serca as the most binding signature of all - "
              "witnessed, and meant."),
)

E(
    key="polish_nature_weather", name="Polish Nature and Weather Sentences",
    group="Themed sentences", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for animals, plants, seasons, and Polish weather
        talk: Wiosna jest moją ulubioną porą roku (Spring is my favorite
        season). Lato w Polsce bywa upalne (Summer in Poland can be hot).
        Jesienią liście są złote (In autumn the leaves are golden). Zimą
        pada śnieg (In winter snow falls). Dziś jest słonecznie (Today is
        sunny). Pada deszcz od rana (It has rained since morning). Wieje
        silny wiatr (A strong wind blows). Jest pochmurno i chłodno (It is
        cloudy and chilly). Jaka jest prognoza pogody? (What is the weather
        forecast?). W lesie rosną grzyby (Mushrooms grow in the forest).
        Polacy uwielbiają zbierać grzyby (Poles love picking mushrooms).
        Nad jeziorem kwitną lilie (Lilies bloom by the lake). Ptak śpiewa na
        drzewie (A bird sings in the tree). Wiewiórka zbiera orzechy (The
        squirrel gathers nuts). Zając ucieka przez pole (The hare runs
        across the field). Ryba pływa w rzece (The fish swims in the river).
        Pszczoły robią miód (Bees make honey). Góry Tatry są piękne (The
        Tatra Mountains are beautiful). Morze Bałtyckie jest zimne (The
        Baltic Sea is cold). Spacer po lesie relaksuje (A walk in the forest
        relaxes). Polish weather talk is a national sport - pada deszcz,
        jest słonecznie, wieje wiatr - and mushroom picking (grzybobranie)
        is a national ritual worth naming."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nature vocabulary inside weather talk and forest
        walks. Each of the 20 sentences pairs a season, an animal, a plant,
        or a weather phrase with its English translation. The learner
        narrates the view from the window in Polish every morning for a week
        - Dziś jest słonecznie, Pada deszcz - until weather talk is
        reflexive. Animal sentences drill nominative plurals in passing;
        the cultural notes (grzybobranie, Tatry, Bałtyk) root the words in
        real Poland."""),
    key_points=[
        "20 sentences: animals, plants, seasons, weather talk.",
        "Weather formulas: pada deszcz/śnieg, jest słonecznie, wieje wiatr.",
        "Seasonal locatives: wiosną, latem, jesienią, zimą.",
        "Cultural anchors: grzybobranie, Tatry, Morze Bałtyckie.",
        "Narrate the morning weather in Polish for a week.",
    ],
    requirements=[
        "Learners must describe today's weather in three Polish sentences.",
        "Name ten animals and five plants without notes.",
    ],
    standards=[
        "CEFR A1 nature and weather vocabulary.",
        "Instrumental of time per standard grammars.",
    ],
    citations=[
        "Narodowy Korpus Języka Polskiego. Nature-domain frequencies.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
    ],
    sig_lens=("Through the Signature lens, nature sentences are the "
              "landscape signing back: the forest, the sea, and the weather "
              "all countersigning the learner's words. This Signature "
              "reading treats Pada śnieg as Poland itself adding its seal "
              "to the sentence."),
)

E(
    key="polish_shopping", name="Polish Shopping and Money Sentences",
    group="Themed sentences", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the market, prices, and paying - in złotych:
        Ile to kosztuje? (How much does it cost?). To kosztuje dwadzieścia
        złotych (It costs twenty złoty). Czy jest zniżka? (Is there a
        discount?). Poproszę kilogram jabłek (A kilo of apples, please).
        Czy mogę przymierzyć? (Can I try it on?). Gdzie jest przymierzalnia?
        (Where is the fitting room?). Ten rozmiar jest za mały (This size is
        too small). Macie większy rozmiar? (Do you have a bigger size?). Biorę
        to (I'll take it). Płacę kartą (I pay by card). Płacę gotówką (I pay
        cash). Poproszę paragon (A receipt, please). Gdzie jest kasa? (Where
        is the checkout?). Sklep jest otwarty do dwudziestej (The shop is
        open till eight pm). Targ jest tańszy niż supermarket (The market is
        cheaper than the supermarket). Kupuję świeży chleb codziennie (I buy
        fresh bread daily). Warzywa są na promocji (Vegetables are on sale).
        To za drogie dla mnie (That is too expensive for me). Czy przyjmujecie
        zwroty? (Do you accept returns?). Dziękuję, do widzenia! (Thank you,
        goodbye!). Money words: złotówka (złoty coin/note), grosz (penny -
        100 groszy to the złoty), cena (price), reszta (change), rachunek
        (bill). Note the number-case dance: jeden złoty, dwa złote, pięć
        złotych - the noun changes with the number."""),
    how_it_works=textwrap.dedent("""\
        This record teaches shopping as a full transaction script. Each of
        the 20 sentences is a line from a real purchase - asking the price,
        trying the size, paying, taking the receipt - with its English
        translation. The learner runs the whole script as both customer and
        clerk, with play money in złotych, until Ile to kosztuje? and Płacę
        kartą come out without thought. The jeden złoty / dwa złote / pięć
        złotych pattern gets its own counting drill."""),
    key_points=[
        "20 sentences: market, prices, bargaining, paying.",
        "Money words: złoty, grosz, cena, reszta, rachunek, paragon.",
        "Number-case pattern: jeden złoty, dwa złote, pięć złotych.",
        "Poproszę + accusative orders goods; Czy mogę przymierzyć? tries clothes.",
        "Run full customer/clerk role-plays with play money.",
    ],
    requirements=[
        "Learners must complete a full purchase role-play without notes.",
        "Count 1-10 with złotych, hitting every case form.",
    ],
    standards=[
        "CEFR A1 shopping vocabulary; Polish currency conventions.",
        "Numeral-noun agreement per standard grammars.",
    ],
    citations=[
        "Narodowy Korpus Języka Polskiego. Shopping-domain frequencies.",
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
    ],
    sig_lens=("Through the Signature lens, every purchase is a small "
              "contract: the price named, the coins counted, the receipt "
              "kept. This Signature reading treats Poproszę paragon as the "
              "learner demanding the paperwork - in Polish, and correctly."),
)

E(
    key="polish_friendship", name="Polish Friendship and Social Life Sentences",
    group="Themed sentences", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for meeting people, invitations, and celebrations:
        Miło cię poznać! (Nice to meet you - informal). Skąd jesteś? (Where
        are you from?). Jestem z Polski (I am from Poland). Jak długo znasz
        Pawła? (How long have you known Paweł?). Przyjaźnimy się od dzieciństwa
        (We have been friends since childhood). Zapraszam cię na urodziny
        (I invite you to my birthday). Impreza zaczyna się o osiemnastej
        (The party starts at six pm). Przyjdź koniecznie! (Do come!). Co
        robisz w weekend? (What are you doing this weekend?). Może pójdziemy
        na kawę? (Maybe we'll go for coffee?). Chodźmy do kina w sobotę
        (Let's go to the cinema on Saturday). Świetny pomysł! (Great idea!).
        Niestety nie mogę, mam inne plany (Unfortunately I can't, I have
        other plans). Może innym razem (Maybe another time). Wszystkiego
        najlepszego z okazji urodzin! (Happy birthday!). Sto lat, sto lat!
        (A hundred years - sung at birthdays). Gratuluję nowej pracy!
        (Congratulations on the new job!). Wesołych Świąt! (Merry
        Christmas!). Szczęśliwego Nowego Roku! (Happy New Year!). Trzymaj
        się i do zobaczenia! (Take care and see you!). Polish friendship
        runs deep and formalities fall fast - after the first coffee comes
        the bruderszaft and the switch to ty."""),
    how_it_works=textwrap.dedent("""\
        This record teaches social Polish as invitation scripts. Each of the
        20 sentences handles a social moment - the introduction, the
        invitation, the acceptance, the graceful refusal, the celebration -
        with its English translation. The learner practices the full
        invitation cycle: invite, accept, invite, refuse politely (Może innym
        razem). Celebration lines (Sto lat, Wesołych Świąt) are drilled as
        fixed formulas to deliver with feeling."""),
    key_points=[
        "20 sentences: meeting people, invitations, celebrations.",
        "Full invitation cycle: invite, accept, refuse gracefully.",
        "Celebration formulas: Sto lat, Wesołych Świąt, Gratuluję.",
        "Może innym razem softens every refusal.",
        "Practice introductions until Miło cię poznać is automatic.",
    ],
    requirements=[
        "Learners must run a full invitation cycle in role-play.",
        "Deliver the five celebration lines with natural feeling.",
    ],
    standards=[
        "CEFR A1-A2 social interaction phrases.",
        "Pragmatic norms per Rada Języka Polskiego.",
    ],
    citations=[
        "Rada Języka Polskiego. Usage and politeness guidance.",
        "Narodowy Korpus Języka Polskiego. Social-domain frequencies.",
    ],
    sig_lens=("Through the Signature lens, friendship sentences are "
              "invitations countersigned: every Zapraszam cię a hand "
              "extended, every acceptance a seal returned. This Signature "
              "reading treats the first Miło cię poznać as the opening of a "
              "contract written in company, not ink."),
)

E(
    key="polish_technology", name="Polish Technology and Communication Sentences",
    group="Themed sentences", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the phone, the internet, and the computer:
        Gdzie jest mój telefon? (Where is my phone?). Ładuję telefon (I
        charge the phone). Bateria się kończy (The battery is dying). Masz
        ładowarkę? (Do you have a charger?). Jakie jest hasło do wifi?
        (What is the wifi password?). Internet nie działa (The internet
        doesn't work). Wyślę ci wiadomość (I'll send you a message). Oddzwonię
        później (I'll call back later). Napisz do mnie maila (Write me an
        email). Załączam zdjęcie (I attach a photo). Komputer się zawiesił
        (The computer froze). Muszę zrestartować laptop (I must restart the
        laptop). Zapisz plik na dysku (Save the file to the disk). Wydrukuj
        ten dokument (Print this document). Szukam tego w internecie (I look
        it up online). Oglądam film na telefonie (I watch a film on my
        phone). Słucham podcastu po polsku (I listen to a podcast in
        Polish). Robię zdjęcie aparatem (I take a photo with the camera).
        Wrzucam post na media społecznościowe (I post on social media).
        Uważaj na oszustów w sieci (Watch out for scammers online). Tech
        vocabulary borrows freely - komputer, internet, mail, wifi, post -
        but the verbs stay Polish: ładować, wysyłać, zapisywać, drukować."""),
    how_it_works=textwrap.dedent("""\
        This record teaches technology vocabulary through daily digital
        routines. Each of the 20 sentences is something the learner already
        does every day - charging, messaging, searching, posting - renamed
        in Polish with its English translation. The learner narrates their
        screen time in Polish for three days: Ładuję telefon, Wyślę ci
        wiadomość. Borrowed nouns (komputer, wifi) pair with native verbs
        (ładować, zapisywać) in every drill."""),
    key_points=[
        "20 sentences: phone, internet, computer, messaging.",
        "Daily routines renamed in Polish: charging, messaging, searching.",
        "Borrowed nouns, native verbs: wifi + ładować, mail + wysyłać.",
        "Narrate three days of screen time in Polish.",
        "Uważaj na oszustów w sieci - safety in the target language.",
    ],
    requirements=[
        "Learners must narrate a full day of device use in Polish.",
        "Give tech help (restart, save, print) in spoken Polish.",
    ],
    standards=[
        "CEFR A1-A2 technology vocabulary; standard computing terms.",
        "Contemporary usage per Narodowy Korpus Języka Polskiego.",
    ],
    citations=[
        "Narodowy Korpus Języka Polskiego. Technology-domain frequencies.",
        "Wielki słownik języka polskiego PAN. Computing vocabulary.",
    ],
    sig_lens=("Through the Signature lens, technology sentences are the "
              "newest wing of the archive: the old language signing its "
              "name on new machines. This Signature reading treats Wyślę "
              "ci wiadomość as proof the oath holds even over wifi."),
)

E(
    key="polish_tenses", name="Polish Verb Tenses in Sentences",
    group="Grammar", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Polish has three tenses - past, present, future - woven together
        with aspect. Present (imperfective only): robię, robisz, robi; robimy,
        robicie, robią (I/you/he do; we/you/they do). Ja czytam książkę
        (I read / am reading a book). On pracuje w szkole (He works at a
        school). My mieszkamy w Polsce (We live in Poland). Czy ty mówisz po
        polsku? (Do you speak Polish?). Dzieci bawią się w ogrodzie (The
        children play in the garden). Past adds -ł- with gender endings:
        robiłem/robiłam (I did, m/f), robiłeś/robiłaś, robił/robiła/robiło;
        robiliśmy/robiłyśmy, robiliście/robiłyście, robili/robiły. Wczoraj
        czytałem ciekawą książkę (Yesterday I read an interesting book - m).
        Ona napisała długi list (She wrote a long letter). Zjedliśmy obiad
        o trzynastej (We ate dinner at one pm - masculine-personal we).
        Poszłyśmy do kina (We went to the cinema - feminine we). Padał
        deszcz cały dzień (It rained all day). Future has two roads: będę +
        infinitive/past form for imperfective (będę czytać / będę czytał -
        I will read), and the perfective present form for completed future
        (przeczytam - I will have read). Jutro będę pracować (Tomorrow I will
        work). W przyszłym roku pojadę do Polski (Next year I will go to
        Poland - completed). Zrobię to jutro (I will do it tomorrow).
        Będziemy się uczyć razem (We will learn together). Kupię ci
        prezent (I will buy you a gift). The aspect rule of thumb:
        imperfective future for processes, perfective future for results."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the three tenses as conjugation tables with
        proof sentences. Each tense shows the full personal endings - the
        present -ę/-isz/-i pattern, the past -ł- with its gender splits, the
        two future roads - then five or more translated sentences per tense
        using the verbs from record 5. The learner converts one story
        through all three tenses: Czytam. Czytałem. Będę czytać. / Przeczytam.
        Gender-split past forms (robiłem/robiłam, poszliśmy/poszłyśmy) get
        paired drill until automatic."""),
    key_points=[
        "Three tenses: past, present, future - aspect woven through all three.",
        "Present: robię, robisz, robi; robimy, robicie, robią.",
        "Past: -ł- stem with gender endings - robiłem/robiłam, robili/robiły.",
        "Future: będę + infinitive (process) vs perfective present (result): przeczytam.",
        "Five or more translated sentences per tense; convert one story through all three.",
    ],
    requirements=[
        "Learners must conjugate robić, czytać, and pisać in all three tenses.",
        "Convert ten sentences between tenses without notes.",
    ],
    standards=[
        "Conjugation classes per Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed.",
        "CEFR A1-A2 tense objectives.",
    ],
    citations=[
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998. Verb chapters.",
    ],
    sig_lens=("Through the Signature lens, tenses are the three seals of "
              "time: what is, what was, what will be - each stamped with "
              "its own ending. This Signature reading treats the past "
              "-ł- as the archive's own mark: every robiłem a filed record "
              "of a finished act."),
)

E(
    key="polish_qa", name="Polish Questions and Answers",
    group="Grammar", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty question-and-answer pairs covering who, what, where, when,
        why, and how: Kto to jest? - To jest mój brat (Who is it? - It is
        my brother). Co to jest? - To jest książka (What is it? - It is a
        book). Gdzie mieszkasz? - Mieszkam w Krakowie (Where do you live? -
        I live in Kraków). Skąd jesteś? - Jestem z Warszawy (Where are you
        from? - I am from Warsaw). Kiedy przyjedziesz? - Przyjadę jutro
        (When will you arrive? - I will arrive tomorrow). O której się
        spotkamy? - O piątej (At what time do we meet? - At five). Dlaczego
        się spóźniłeś? - Zgubiłem drogę (Why are you late? - I lost my way).
        Jak się masz? - Dziękuję, dobrze (How are you? - Fine, thanks).
        Jak to się robi? - Najpierw kroisz, potem gotujesz (How is it done? -
        First you chop, then you cook). Ile to kosztuje? - Pięćdziesiąt
        złotych (How much is it? - Fifty złoty). Ile masz lat? - Mam
        trzydzieści lat (How old are you? - I am thirty). Czy mówisz po
        polsku? - Tak, trochę (Do you speak Polish? - Yes, a little). Czy to
        twoje? - Nie, to nie moje (Is this yours? - No, it is not mine).
        Jaki jest twój ulubiony film? - Lubię komedie (What is your favorite
        film? - I like comedies). Który wybierasz? - Ten niebieski (Which do
        you choose? - The blue one). Czyj to samochód? - To samochód mojego
        ojca (Whose car is it? - It is my father's car). Dokąd idziesz? - Idę
        do sklepu (Where are you going? - I go to the shop). Po co tam
        idziesz? - Po chleb (What for? - For bread). Jak długo tu jesteś? -
        Od tygodnia (How long have you been here? - For a week). Question
        words - kto, co, gdzie, kiedy, dlaczego, jak, ile, czy - each earn
        their pair here."""),
    how_it_works=textwrap.dedent("""\
        This record teaches questions as twenty complete exchanges. Each
        pair shows the question word, the full Polish question, the natural
        Polish answer, and both English translations. The learner drills by
        interview: one partner asks down the list, the other answers with
        true personal details - Gdzie mieszkasz? gets their real city. Then
        they swap. The question words are learned as a set, each anchored to
        its pair."""),
    key_points=[
        "20 question/answer pairs: who, what, where, when, why, how, how much, whose.",
        "Question words: kto, co, gdzie, kiedy, dlaczego, jak, ile, czy, który, czyj.",
        "Czy opens yes/no questions: Czy mówisz po polsku?",
        "Answers use true personal details - drill as a real interview.",
        "Every pair fully translated both ways.",
    ],
    requirements=[
        "Learners must ask and answer all 20 with true personal details.",
        "Produce the question word for each pair from memory.",
    ],
    standards=[
        "CEFR A1 interrogative objectives.",
        "Question formation per standard grammars.",
    ],
    citations=[
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
    ],
    sig_lens=("Through the Signature lens, a question is a summons and an "
              "answer is testimony: Kto to jest? demands the record, To jest "
              "mój brat enters it. This Signature reading treats the twenty "
              "pairs as twenty sworn exchanges, each complete."),
)

E(
    key="polish_commands", name="Polish Commands and Requests",
    group="Grammar", ladder_rank=10, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty imperatives and polite requests, informal and formal: Chodź
        tu! (Come here - informal). Siadaj (Sit down - informal). Mów wolniej
        (Speak more slowly). Powtórz, proszę (Repeat, please). Otwórz okno
        (Open the window). Zamknij drzwi (Close the door). Daj mi to (Give me
        that). Weź parasol (Take the umbrella). Jedz warzywa (Eat your
        vegetables). Pij wodę (Drink water). Czekaj chwilę (Wait a moment).
        Uważaj! (Watch out!). Nie martw się (Don't worry). Chodźmy! (Let's
        go!). Zróbmy to razem (Let's do it together). Formal requests use
        proszę + infinitive or pan/pani + third person: Proszę usiąść (Please
        sit down - formal). Proszę mówić wolniej (Please speak more slowly -
        formal). Niech pan poczeka (Please wait, sir - literally 'let the
        gentleman wait'). Czy mógłby pan powtórzyć? (Could you repeat, sir?).
        Czy mogłaby pani pomóc? (Could you help, madam?). The imperative
        forms from the present stem: mówisz -> mów, robisz -> rób, piszesz
        -> pisz; perfective imperatives for single completed acts: zrób to
        (do it [once]), przeczytaj to (read it [through]). Negative commands
        take nie: nie rób tego (don't do that). Softening with proszę turns
        any command polite."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the imperative as a volume knob from blunt to
        courtly. Each of the 20 lines shows the command, its register
        (informal, neutral, formal), and its English translation. The learner
        drills the formation rule - present stem minus ending - then runs
        the politeness ladder on one request: Mów wolniej -> Proszę mówić
        wolniej -> Czy mógłby pan mówić wolniej? Formal lines get their own
        drill, since niech pan and proszę + infinitive follow different
        grammar."""),
    key_points=[
        "20 imperatives and requests: informal, neutral, and formal.",
        "Formation: present stem minus ending - mówisz -> mów, piszesz -> pisz.",
        "Perfective imperative for one completed act: zrób to, przeczytaj to.",
        "Formal: proszę + infinitive; Niech pan/pani + third person.",
        "Proszę softens any command; nie + imperative forbids.",
    ],
    requirements=[
        "Learners must form imperatives from ten new verbs.",
        "Run the politeness ladder on five requests without notes.",
    ],
    standards=[
        "Imperative formation per Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed.",
        "CEFR A2 directive objectives.",
    ],
    citations=[
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
        "Rada Języka Polskiego. Formal address guidance.",
    ],
    sig_lens=("Through the Signature lens, a command is an order signed and "
              "a polite request is an order wrapped in courtesy - both carry "
              "the speaker's authority. This Signature reading treats Czy "
              "mógłby pan powtórzyć? as power exercised gently, the "
              "strongest signature of all."),
)

E(
    key="polish_descriptions", name="Polish Descriptions of People and Places",
    group="Themed sentences", ladder_rank=10, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences describing people, places, and things in detail:
        Moja babcia ma siwe włosy i ciepły uśmiech (My grandma has gray hair
        and a warm smile). On jest wysoki i szczupły (He is tall and slim).
        Ona ma niebieskie oczy i długie włosy (She has blue eyes and long
        hair). Mój brat nosi okulary (My brother wears glasses). To dziecko
        jest bardzo żywiołowe (This child is very lively). Kraków jest
        starym, pięknym miastem (Kraków is an old, beautiful city). Rynek
        Główny jest największym średniowiecznym rynkiem w Europie (The Main
        Square is the largest medieval square in Europe). Wisła płynie przez
        Warszawę (The Vistula flows through Warsaw). Zamek Królewski stoi na
        Wawelu (The Royal Castle stands on Wawel Hill). Stare Miasto w
        Gdańsku jest kolorowe (The Old Town in Gdańsk is colorful). Tatry są
        wysokie i majestatyczne (The Tatras are high and majestic). Morze
        jest spokojne o poranku (The sea is calm in the morning). Ten dom ma
        czerwony dach (This house has a red roof). Ogród jest pełen kwiatów
        (The garden is full of flowers). Samochód jest szybki i wygodny
        (The car is fast and comfortable). Ta kawa jest mocna i gorąca (This
        coffee is strong and hot). Film był długi, ale ciekawy (The film was
        long but interesting). Książka jest gruba i wciągająca (The book is
        thick and gripping). Pogoda jest idealna na spacer (The weather is
        perfect for a walk). Polska to kraj o bogatej historii (Poland is a
        country with a rich history). Adjective stacking, instrumental of
        description, and the great Polish places - all in working sentences."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description as adjective stacking in full
        sentences. Each of the 20 sentences describes a person, place, or
        thing with two or more agreed adjectives, with the English
        translation beside it. The learner describes their own family and
        hometown the same way - two adjectives minimum per sentence -
        checking every ending against the noun's gender. Place sentences
        double as a tour of Poland: Kraków, Wawel, Gdańsk, Tatry, Bałtyk."""),
    key_points=[
        "20 sentences describing people, places, things in detail.",
        "Adjective stacking: two or more agreed adjectives per sentence.",
        "A tour of Poland inside the sentences: Kraków, Wawel, Gdańsk, Tatry.",
        "Every ending checked against the noun's gender.",
        "Describe your family and hometown with the same patterns.",
    ],
    requirements=[
        "Learners must describe three people and three places, two adjectives each.",
        "Check every adjective ending against its noun's gender.",
    ],
    standards=[
        "CEFR A2 descriptive objectives.",
        "Agreement rules per Bielec D. Polish: An Essential Grammar.",
    ],
    citations=[
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
        "Narodowy Korpus Języka Polskiego. Descriptive frequencies.",
    ],
    sig_lens=("Through the Signature lens, description is portraiture: each "
              "agreed adjective a brushstroke, each sentence a finished "
              "likeness. This Signature reading treats Kraków jest starym, "
              "pięknym miastem as a signed portrait of a city a thousand "
              "years old."),
)

E(
    key="polish_story1", name="Polish Story I: A New Morning",
    group="Stories", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence simple story in the present tense, line by line with
        English: 1. Anna budzi się o szóstej rano. (Anna wakes up at six in
        the morning.) 2. Słońce świeci przez okno. (The sun shines through
        the window.) 3. Ona wstaje i myje twarz zimną wodą. (She gets up and
        washes her face with cold water.) 4. W kuchni pachnie świeża kawa.
        (Fresh coffee smells in the kitchen.) 5. Mama smaży naleśniki na
        patelni. (Mum fries pancakes in the pan.) 6. Anna je śniadanie i
        czyta gazetę. (Anna eats breakfast and reads the newspaper.) 7. Kot
        mruczy na kanapie. (The cat purrs on the sofa.) 8. Za oknem ptaki
        śpiewają. (Outside the window birds sing.) 9. Anna bierze torbę i
        wychodzi do pracy. (Anna takes her bag and leaves for work.) 10.
        To będzie dobry dzień. (It will be a good day.) The story uses only
        present-tense verbs and the vocabulary of records 4-9: budzić się
        (wake up), wstawać (get up), myć (wash), pachnieć (smell), smażyć
        (fry), jeść (eat), czytać (read), mruczeć (purr), śpiewać (sing),
        brać (take), wychodzić (leave). Read it aloud three times, then
        retell it without looking - the first story is the proof the
        foundations hold."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through a complete micro-story. Each of the 10
        Polish lines appears with its line-by-line English translation; the
        learner reads the whole story aloud, then retells it sentence by
        sentence from the English prompts, then finally from memory. Only
        present-tense verbs appear, so the learner's full attention goes to
        vocabulary and flow. The demonstration program checks the retelling:
        all 10 key verbs must appear in order."""),
    key_points=[
        "10-sentence story, present tense only, line-by-line English.",
        "Uses only vocabulary from records 4-9 - nothing new to decode.",
        "Read aloud three times, retell from English, retell from memory.",
        "Key verbs: budzić się, wstawać, myć, smażyć, jeść, czytać, wychodzić.",
        "The first proof the foundations hold.",
    ],
    requirements=[
        "Learners must retell the story from memory without notes.",
        "All 10 key verbs must appear in order in the retelling.",
    ],
    standards=[
        "CEFR A1 narrative objectives; present-tense narration.",
        "Controlled vocabulary per records 4-9.",
    ],
    citations=[
        "Instituto Camoes-style graded narrative method, applied to Polish.",
        "Narodowy Korpus Języka Polskiego. High-frequency verb forms.",
    ],
    sig_lens=("Through the Signature lens, the first story is the first "
              "filed dispatch: ten sentences, ten facts, one morning - "
              "signed and delivered in Polish. This Signature reading "
              "treats the memorized retelling as the learner's first "
              "original filing in the language."),
)

E(
    key="polish_story2", name="Polish Story II: The Journey",
    group="Stories", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the past tense, line by line with English:
        1. W zeszłym roku pojechałem do Krakowa. (Last year I went to
        Kraków - masculine speaker.) 2. Pociąg przyjechał punktualnie o
        dziewiątej. (The train arrived punctually at nine.) 3. Na dworcu
        czekał na mnie stary przyjaciel. (At the station an old friend
        waited for me.) 4. Poszliśmy na Rynek Główny. (We went to the Main
        Square - masculine-personal we.) 5. Zjedliśmy obiad w małej
        restauracji. (We ate dinner in a small restaurant.) 6. Potem
        wspięliśmy się na Wawel. (Then we climbed Wawel Hill.) 7. Widok z
        góry był przepiękny. (The view from the top was stunning.) 8.
        Wieczorem słuchaliśmy hejnału z wieży. (In the evening we listened
        to the hejnał from the tower.) 9. Kupiłam pamiątki dla rodziny. (I
        bought souvenirs for the family - feminine speaker.) 10. To była
        najlepsza podróż w moim życiu. (It was the best journey of my
        life.) Past-tense verbs on parade: pojechałem, przyjechał, czekał,
        poszliśmy, zjedliśmy, wspięliśmy się, był, słuchaliśmy, kupiłam,
        była - with the gender splits (pojechałem/kupiłam) and the
        masculine-personal plural (poszliśmy) doing their work. Note the
        hejnał - the hourly trumpet call from St. Mary's Tower, broken off
        mid-note in memory of the 1241 trumpeter."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the past tense inside a real journey. Each of
        the 10 Polish lines appears with its English translation; the
        learner tracks every past-tense verb, noting the gender endings -
        pojechałem vs kupiłam, poszliśmy vs poszłyśmy - and converts the
        masculine speaker's lines to feminine and back. Retell the journey
        as your own trip, changing the city and the details. The
        demonstration program verifies all 10 past-tense verbs and their
        gender forms."""),
    key_points=[
        "10-sentence story, past tense, line-by-line English.",
        "Gender splits on display: pojechałem/kupiłam, poszliśmy/poszłyśmy.",
        "Masculine-personal plural: poszliśmy, zjedliśmy, słuchaliśmy.",
        "Cultural anchor: the hejnał from St. Mary's Tower.",
        "Retell as your own journey with your own details.",
    ],
    requirements=[
        "Learners must convert every past verb between masculine and feminine.",
        "Retell the journey with a different city and personal details.",
    ],
    standards=[
        "CEFR A2 past narration; gender agreement in past tense.",
        "Past-tense formation per Swan O E. Polish Verbs & Essentials of Grammar.",
    ],
    citations=[
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
    ],
    sig_lens=("Through the Signature lens, the past tense is the archive "
              "itself: every -ł- a filed record, every journey a folder of "
              "ten documents. This Signature reading treats the retold "
              "journey as the learner filing their own first expedition "
              "report - in Polish, and true."),
)

E(
    key="polish_story3", name="Polish Story III: Tomorrow's Promise",
    group="Stories", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the future and conditional, line by line
        with English: 1. Jutro zacznie się nowy rozdział. (Tomorrow a new
        chapter will begin.) 2. Będę wstawać wcześniej i biegać w parku. (I
        will get up earlier and run in the park.) 3. Nauczę się grać na
        gitarze. (I will learn to play the guitar - completed.) 4. Pojadę do
        Gdańska nad morze. (I will go to Gdańsk by the sea.) 5. Kupię nowy
        rower i będę jeździć codziennie. (I will buy a new bike and ride
        daily.) 6. Gdybym miał więcej czasu, podróżowałbym po Polsce. (If I
        had more time, I would travel around Poland - conditional.) 7.
        Chciałbym zobaczyć wszystkie zamki. (I would like to see all the
        castles.) 8. Może spotkam starych przyjaciół. (Maybe I will meet old
        friends.) 9. Będziemy razem śmiać się i wspominać. (We will laugh and
        reminisce together.) 10. Przyszłość należy do odważnych. (The future
        belongs to the brave.) Future's two roads side by side - będę
        wstawać (process) vs nauczę się (completed result) - and the
        conditional mood: podróżowałbym, chciałbym, the -by- marker with
        gender endings. The closing proverb is real Polish wisdom to carry
        forward."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the future and the conditional inside a story
        of plans. Each of the 10 Polish lines appears with its English
        translation; the learner sorts every future verb into process
        (będę wstawać) vs result (nauczę się) piles, then drills the
        conditional -by- forms with gender endings (podróżowałbym/
        podróżowałabym). The learner writes their own ten-sentence future
        story with five plans and one conditional dream. The demonstration
        program checks the aspect sorting and the conditional forms."""),
    key_points=[
        "10-sentence story: future and conditional, line-by-line English.",
        "Two future roads: będę wstawać (process) vs nauczę się (result).",
        "Conditional: -by- with gender endings - podróżowałbym/podróżowałabym.",
        "Write your own ten-sentence future story.",
        "Closing proverb: Przyszłość należy do odważnych.",
    ],
    requirements=[
        "Learners must sort ten future verbs into process vs result.",
        "Write a personal ten-sentence future story with one conditional.",
    ],
    standards=[
        "CEFR A2-B1 future and conditional objectives.",
        "Future and conditional formation per standard grammars.",
    ],
    citations=[
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
    ],
    sig_lens=("Through the Signature lens, the future tense is a contract "
              "with tomorrow: every będę a promise signed in advance, every "
              "conditional a clause for what-ifs. This Signature reading "
              "treats the learner's own future story as their first "
              "forward-dated filing - binding, and theirs."),
)

E(
    key="polish_idioms", name="Polish Idioms and Proverbs",
    group="Register and style", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty idioms and proverbs - literal translation, real meaning, and
        an example sentence each: 1. Nie mój cyrk, nie moje małpy. (Not my
        circus, not my monkeys.) = Not my problem. To nie mój cyrk, nie
        moje małpy - radź sobie sam. 2. Gdzie kucharek sześć, tam nie ma co
        jeść. (Where there are six cooks, there is nothing to eat.) = Too
        many cooks spoil the broth. 3. Lepszy wróbel w garści niż gołąb na
        dachu. (A sparrow in the hand is better than a pigeon on the roof.)
        = A bird in the hand. 4. Darowanemu koniowi w zęby się nie zagląda.
        (Don't look a gift horse in the teeth.) 5. Bez pracy nie ma kołaczy.
        (Without work there are no kołaczy - festive cakes.) = No pain, no
        gain. 6. Cicha woda brzegi rwie. (Quiet water tears the banks.) =
        Still waters run deep. 7. Kto pod kim dołki kopie, ten sam w nie
        wpada. (Who digs pits under others falls in himself.) 8. Mowa jest
        srebrem, a milczenie złotem. (Speech is silver, silence is golden.)
        9. Niedaleko pada jabłko od jabłoni. (The apple falls not far from
        the apple tree.) 10. Apetyt rośnie w miarę jedzenia. (Appetite grows
        as one eats.) 11. Co kraj, to obyczaj. (Every country, its custom.)
        12. Tonący brzytwy się chwyta. (The drowning man clutches a razor.)
        = Clutching at straws. 13. Nie chwal dnia przed zachodem słońca.
        (Don't praise the day before sunset.) 14. Kłamstwo ma krótkie nogi.
        (A lie has short legs.) 15. Raz na wozie, raz pod wozem. (Once on the
        cart, once under it.) = Ups and downs. 16. Jak sobie pościelesz, tak
        się wyśpisz. (As you make your bed, so you sleep.) 17. Głodnemu
        chleb na myśli. (To the hungry man, bread is on his mind.) 18.
        Fortuna kołem się toczy. (Fortune turns like a wheel.) 19. Prawda w
        oczy kole. (Truth stings the eyes.) 20. Do trzech razy sztuka. (Up to
        three times is the trick.) = Third time's the charm. Spróbuję do
        trzech razy sztuka. Idioms are the soul of fluency - learn them as
        whole signed phrases."""),
    how_it_works=textwrap.dedent("""\
        This record teaches idioms as indivisible units: each of the 20
        shows the Polish, the literal English (often funny), the real
        meaning, and a sentence using it naturally. The learner never
        translates idioms word by word - they memorize the whole phrase and
        its situation, then drop one idiom per day into real conversation.
        The demonstration program quizzes meaning-from-idiom and idiom-from-
        meaning both ways."""),
    key_points=[
        "20 idioms and proverbs: literal translation + real meaning + example sentence.",
        "Never translate idioms word by word - learn the whole unit.",
        "Signature Polish originals: Nie mój cyrk, Do trzech razy sztuka.",
        "Drop one idiom per day into real conversation.",
        "Idioms are the soul of fluency.",
    ],
    requirements=[
        "Learners must use five idioms correctly in conversation.",
        "Quiz both directions: idiom to meaning and meaning to idiom.",
    ],
    standards=[
        "Idioms per Wielki słownik języka polskiego PAN.",
        "CEFR B1 idiomatic objectives.",
    ],
    citations=[
        "Wielki słownik języka polskiego PAN. Idiom entries.",
        "Narodowy Korpus Języka Polskiego. Proverb frequencies.",
    ],
    sig_lens=("Through the Signature lens, an idiom is a folk contract "
              "signed by millions: no single author, binding on all who "
              "speak. This Signature reading treats Nie mój cyrk, nie moje "
              "małpy as Poland's most exported signature - wit, sealed and "
              "delivered."),
)

E(
    key="polish_registers", name="Polish Formal and Polite Registers",
    group="Register and style", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen formal vs informal pairs - the same message in two Polands:
        1. Informal: Cześć, jak leci? / Formal: Dzień dobry, jak się pan
        miewa? (Hi, how's it going? / Good day, how are you, sir?) 2. Dasz
        mi to? / Czy mógłby pan mi to podać? (Give me that? / Could you hand
        me that, sir?) 3. Czekaj chwilę. / Proszę chwileczkę zaczekać. (Wait
        a moment. / Please wait a moment.) 4. Nie rozumiem. / Przykro mi,
        nie zrozumiałem. (I don't understand. / I'm sorry, I didn't
        understand.) 5. Gdzie jest łazienka? / Przepraszam, gdzie znajdę
        toaletę? (Where's the bathroom? / Excuse me, where is the restroom?)
        6. Ile płacę? / Jaka będzie należność? (How much do I pay? / What
        will the charge be?) 7. Zadzwonię później. / Skontaktuję się z panem
        później. (I'll call later. / I will contact you later, sir.) 8.
        Przyjdź jutro. / Zapraszam jutro. (Come tomorrow. / I invite you
        tomorrow.) 9. Dzięki! / Serdecznie dziękuję. (Thanks! / Thank you
        kindly.) 10. Pa! / Do widzenia. (Bye! / Goodbye.) 11. Mówisz po
        angielsku? / Czy mówi pan po angielsku? (Do you speak English? / Do
        you speak English, sir?) 12. Pomóż mi. / Czy mogłaby pani mi pomóc?
        (Help me. / Could you help me, madam?) 13. Siadaj. / Proszę usiąść.
        (Sit down. / Please sit down.) 14. Wybacz. / Proszę o wybaczenie.
        (Sorry. / I beg your pardon.) 15. Napisz do mnie. / Proszę o
        wiadomość. (Write me. / Please send word.) The machinery: informal
        uses ty + second person; formal uses pan/pani/państwo + third
        person, proszę + infinitive, conditional mógłby/mogłaby, and soft
        nouns (chwileczka, należność). With elders, officials, and strangers
        - always the formal."""),
    how_it_works=textwrap.dedent("""\
        This record teaches register as a conversion skill. Each of the 15
        pairs shows the same message twice - informal on the left, formal on
        the right - with English translations. The learner converts new
        sentences both ways: take an informal line and formalize it (ty ->
        pan, second person -> third, add proszę), then reverse. Role-play a
        job interview and a visit to an office, staying formal throughout;
        then a coffee with a friend, staying informal. The demonstration
        program checks conversions automatically."""),
    key_points=[
        "15 formal vs informal pairs - the same message in two registers.",
        "Informal: ty + second person. Formal: pan/pani + third person.",
        "Formal tools: proszę + infinitive, conditional mógłby/mogłaby, niech pan.",
        "Elders, officials, strangers: always formal.",
        "Convert both directions until the switch is instant.",
    ],
    requirements=[
        "Learners must convert ten sentences both directions.",
        "Hold a five-minute formal role-play without slipping to ty.",
    ],
    standards=[
        "Pragmatic norms per Rada Języka Polskiego.",
        "CEFR B1 register objectives.",
    ],
    citations=[
        "Rada Języka Polskiego. Formal address and politeness guidance.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
    ],
    sig_lens=("Through the Signature lens, register is the choice of seal: "
              "the informal a quick initial, the formal the full embossed "
              "stamp. This Signature reading treats the pan/pani switch as "
              "the learner learning exactly how much weight each signature "
              "should carry."),
)

E(
    key="polish_complex", name="Polish Compound and Complex Sentences",
    group="Register and style", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen long sentences with clauses, connectors, and relative
        clauses - parsed and translated: 1. Poszedłem do sklepu, bo
        zabrakło chleba. (I went to the shop because we ran out of bread -
        bo = because.) 2. Chociaż padał deszcz, poszliśmy na spacer.
        (Although it rained, we went for a walk.) 3. Kiedy wrócę, zadzwonię
        do ciebie. (When I return, I will call you.) 4. Jeśli będziesz
        grzeczny, dostaniesz lody. (If you are good, you will get ice
        cream.) 5. Książka, którą czytam, jest fascynująca. (The book that
        I read is fascinating - którą = relative pronoun.) 6. Człowiek,
        który tu mieszkał, był lekarzem. (The man who lived here was a
        doctor.) 7. Nie wiem, gdzie położyłem klucze. (I don't know where I
        put the keys.) 8. Powiedział, że przyjdzie jutro. (He said that he
        will come tomorrow - że = that.) 9. Zanim wyjdziesz, zgaś światło.
        (Before you leave, turn off the light.) 10. Po tym jak zjadłem,
        poszedłem spać. (After I ate, I went to sleep.) 11. Uczę się
        polskiego, ponieważ chcę pracować w Polsce. (I learn Polish because
        I want to work in Poland.) 12. Mimo że byłem zmęczony, skończyłem
        projekt. (Although I was tired, I finished the project.) 13. Im
        więcej ćwiczysz, tym lepiej mówisz. (The more you practice, the
        better you speak.) 14. Albo pójdziemy do kina, albo zostaniemy w
        domu. (Either we go to the cinema or we stay home.) 15. To, co
        powiedziałeś, było bardzo mądre. (What you said was very wise.)
        Connectors: bo/ponieważ (because), chociaż/mimo że (although),
        kiedy/gdy (when), jeśli (if), że (that), zanim (before), który
        (who/which) - each with its clause pattern."""),
    how_it_works=textwrap.dedent("""\
        This record teaches complex sentences by parsing. Each of the 15
        sentences is shown whole, then split into its clauses with the
        connector labeled and the English translation given. The learner
        builds their own: take two simple sentences and join them with each
        connector in turn - bo, chociaż, kiedy, jeśli, że, który - checking
        the word order in the subordinate clause. Relative clauses (który/
        która/które) get agreement drill against their antecedent."""),
    key_points=[
        "15 complex sentences - parsed into clauses, connectors labeled.",
        "Connectors: bo, chociaż, kiedy, jeśli, że, zanim, który, mimo że.",
        "Relative pronouns agree with their antecedent: który/która/które.",
        "Build your own: join simple pairs with each connector.",
        "Every sentence fully translated and parsed.",
    ],
    requirements=[
        "Learners must join ten simple pairs with a different connector each.",
        "Parse five complex sentences into labeled clauses.",
    ],
    standards=[
        "CEFR B1 complex-sentence objectives.",
        "Subordination per standard grammars.",
    ],
    citations=[
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998. Complex sentences.",
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
    ],
    sig_lens=("Through the Signature lens, a complex sentence is a "
              "multi-page contract: main clause the headline terms, "
              "subordinate clauses the fine print - all signed together. "
              "This Signature reading treats every correct który as a "
              "cross-reference properly filed."),
)

E(
    key="polish_dialogue_market", name="Polish Conversation at the Market",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue at the market, annotated: 1.
        Sprzedawca: Dzień dobry! W czym mogę pomóc? (Good day! How can I
        help? - formal helper.) 2. Klient: Dzień dobry. Poproszę kilogram
        pomidorów. (Good day. A kilo of tomatoes, please.) 3. Sprzedawca:
        Proszę bardzo. Coś jeszcze? (Here you are. Anything else?) 4.
        Klient: Tak, pół kilo sera żółtego. (Yes, half a kilo of yellow
        cheese.) 5. Sprzedawca: Ser jest świeży, prosto z mleczarni. (The
        cheese is fresh, straight from the dairy.) 6. Klient: Świetnie. Ile
        płacę? (Great. How much do I pay?) 7. Sprzedawca: Razem trzydzieści
        dwa złote. (Thirty-two złoty altogether.) 8. Klient: Czy mogę
        zapłacić kartą? (Can I pay by card?) 9. Sprzedawca: Oczywiście,
        terminal jest tutaj. (Of course, the terminal is here.) 10. Klient:
        [płaci] Dziękuję. (pays) Thank you. 11. Sprzedawca: Proszę bardzo.
        Paragon? (You're welcome. Receipt?) 12. Klient: Tak, poproszę. A
        gdzie są jajka? (Yes, please. And where are the eggs?) 13.
        Sprzedawca: Na końcu alejki, po prawej. (At the end of the aisle, on
        the right.) 14. Klient: Dziękuję. Te jabłka ładnie wyglądają. (Thank
        you. These apples look nice.) 15. Sprzedawca: To antonówki, słodkie
        i soczyste. (These are antonówki - sweet and juicy.) 16. Klient:
        Poproszę dwa kilo. (Two kilos, please.) 17. Sprzedawca: Proszę. To
        wszystko? (Here you are. Is that all?) 18. Klient: Tak, to wszystko.
        Do widzenia! (Yes, that's all. Goodbye!) 19. Sprzedawca: Do
        widzenia! Zapraszamy ponownie! (Goodbye! Come again!) 20. Klient:
        [do siebie] Miła obsługa. (to himself) Nice service. Annotations:
        the formal register throughout (poproszę, dziękuję), the accusative
        of purchase (kilogram pomidorów - genitive after quantity!), and the
        quantity rule: numbers 5+ take the genitive plural."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through a complete market transaction. Each of
        the 20 lines shows the Polish, the speaker, and the English
        translation, with annotations on the grammar that matters - the
        quantity genitive (kilogram pomidorów), the formal register, the
        payment formulas. The learner performs the dialogue with a partner,
        then improvises a new version buying different goods. The
        demonstration program checks that all 20 lines are present and the
        key transaction phrases appear."""),
    key_points=[
        "20-line bilingual dialogue: a full market transaction.",
        "Quantity rule: 5+ takes genitive plural - pięć złotych, dwa kilo jabłek.",
        "Formal register throughout: poproszę, dziękuję, proszę bardzo.",
        "Perform with a partner; then improvise with new goods.",
        "Annotated: every grammar point that matters is explained.",
    ],
    requirements=[
        "Learners must perform the dialogue from memory with a partner.",
        "Improvise a new market dialogue with different goods.",
    ],
    standards=[
        "CEFR A2 transactional dialogue objectives.",
        "Quantity-case rules per standard grammars.",
    ],
    citations=[
        "Narodowy Korpus Języka Polskiego. Transactional dialogues.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
    ],
    sig_lens=("Through the Signature lens, the market dialogue is a "
              "completed contract performed aloud: offer, acceptance, "
              "payment, receipt - twenty lines, zero loose ends. This "
              "Signature reading treats the performed dialogue as the "
              "learner's first witnessed transaction in Polish."),
)

E(
    key="polish_dialogue_friend", name="Polish Conversation: Meeting a Friend",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue between friends, annotated: 1.
        Ania: Cześć, Marek! Kopę lat! (Hi, Marek! Long time no see -
        literally 'a heap of years'!) 2. Marek: Cześć, Ania! Co słychać?
        (Hi, Ania! What's new?) 3. Ania: Wszystko dobrze. A u ciebie? (All
        good. And with you?) 4. Marek: Nie narzekam. Słyszałem, że byłaś w
        Hiszpanii? (Can't complain. I heard you were in Spain?) 5. Ania:
        Tak, wróciłam w zeszłym tygodniu. Było cudownie! (Yes, I returned
        last week. It was wonderful!) 6. Marek: Zazdroszczę! Ja siedziałem w
        biurze. (I'm jealous! I sat in the office.) 7. Ania: Następnym razem
        jedziesz ze mną. (Next time you come with me.) 8. Marek: Zgoda! A
        co u twojego brata? (Deal! And how is your brother?) 9. Ania:
        Ożenił się w czerwcu. (He got married in June.) 10. Marek:
        Serio? Gratulacje dla niego! (Really? Congratulations to him!) 11.
        Ania: Dzięki, przekażę. Idziesz na kawę? (Thanks, I'll pass it on.
        Are you coming for coffee?) 12. Marek: Chętnie! Znam fajną
        kawiarnię za rogiem. (Gladly! I know a nice café around the corner.)
        13. Ania: Świetnie. Opowiedz mi wszystko o pracy. (Great. Tell me
        everything about work.) 14. Marek: Dostałem awans! Od lipca jestem
        kierownikiem. (I got promoted! Since July I'm a manager.) 15. Ania:
        Wspaniale! Musimy to uczcić. (Wonderful! We must celebrate it.) 16.
        Marek: Zapraszam cię w sobotę na kolację. (I invite you Saturday for
        dinner.) 17. Ania: Przyjdę z przyjemnością. O której? (I'll come
        gladly. At what time?) 18. Marek: O dziewiętnastej. Nie spóźnij się!
        (At seven pm. Don't be late!) 19. Ania: Postaram się. Do zobaczenia!
        (I'll try. See you!) 20. Marek: Na razie! (See you!) Annotations:
        the informal register (ty forms, Cześć, Kopę lat), past-tense
        storytelling (wróciłam, ożenił się, dostałem), and the invitation
        cycle from record 19 in action."""),
    how_it_works=textwrap.dedent("""\
        This record teaches friendly conversation as a performed scene.
        Each of the 20 lines shows the Polish, the speaker, and the English
        translation, with annotations on the informal register and the
        past-tense storytelling. The learner performs it with a partner,
        then replays it with their own news - their real trip, their real
        promotion. The demonstration program verifies all 20 lines and the
        informal markers."""),
    key_points=[
        "20-line bilingual dialogue: two friends catching up.",
        "Informal register: ty forms, Cześć, Kopę lat, Na razie.",
        "Past-tense storytelling: wróciłam, ożenił się, dostałem.",
        "The invitation cycle in action: invite, accept, set the time.",
        "Replay with your own real news.",
    ],
    requirements=[
        "Learners must perform the dialogue with a partner.",
        "Replay it substituting their own real news.",
    ],
    standards=[
        "CEFR A2 informal conversation objectives.",
        "Past-tense narration per standard grammars.",
    ],
    citations=[
        "Narodowy Korpus Języka Polskiego. Conversational frequencies.",
        "Bielec D. Polish: An Essential Grammar. Routledge; 1998.",
    ],
    sig_lens=("Through the Signature lens, the friends' dialogue is the "
              "contract of company renewed: news exchanged, invitations "
              "countersigned, Kopę lat sealing the gap between meetings. "
              "This Signature reading treats the replayed version - with "
              "the learner's own news - as the signature becoming theirs."),
)

E(
    key="polish_dialogue_problem", name="Polish Conversation: Solving a Problem",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue solving a problem, annotated: 1.
        Pan Nowak: Dzień dobry, mam problem z pralką. (Good day, I have a
        problem with the washing machine.) 2. Serwisant: Dzień dobry. Co się
        dzieje? (Good day. What is happening?) 3. Pan Nowak: Nie wiruje i
        hałasuje. (It doesn't spin and it makes noise.) 4. Serwisant: Od
        kiedy to trwa? (Since when has this lasted?) 5. Pan Nowak: Od
        wczorajszego wieczora. (Since yesterday evening.) 6. Serwisant: Czy
        pralka jest na gwarancji? (Is the washer under warranty?) 7. Pan
        Nowak: Tak, kupiłem ją w marcu. (Yes, I bought it in March.) 8.
        Serwisant: Proszę podać numer seryjny. (Please give the serial
        number.) 9. Pan Nowak: Chwileczkę... to będzie 8-4-2-9. (One
        moment... it will be 8-4-2-9.) 10. Serwisant: Dziękuję. Mogę
        przyjechać w czwartek. (Thank you. I can come on Thursday.) 11. Pan
        Nowak: O której godzinie? (At what time?) 12. Serwisant: Między
        dziesiątą a dwunastą. (Between ten and twelve.) 13. Pan Nowak: Dobrze.
        A ile to będzie kosztować? (Good. And how much will it cost?) 14.
        Serwisant: Naprawa gwarancyjna jest bezpłatna. (Warranty repair is
        free.) 15. Pan Nowak: Świetnie. Czy muszę coś przygotować? (Great. Must
        I prepare anything?) 16. Serwisant: Proszę odłączyć pralkę od prądu.
        (Please unplug the washer.) 17. Pan Nowak: Zrobione. Dziękuję za
        pomoc. (Done. Thanks for the help.) 18. Serwisant: Proszę bardzo. Do
        zobaczenia w czwartek. (You're welcome. See you Thursday.) 19. Pan
        Nowak: Do zobaczenia. (See you.) 20. Serwisant: [notuje] Czwartek,
        dziesiąta, pralka pana Nowaka. (notes) Thursday, ten, Mr. Nowak's
        washer. Annotations: the formal register with a stranger (pan,
        proszę + infinitive), the problem statement pattern (mam problem z
        + instrumental), time expressions (od wczorajszego wieczora, między
        dziesiątą a dwunastą), and the full service cycle: report, diagnose,
        schedule, confirm."""),
    how_it_works=textwrap.dedent("""\
        This record teaches problem-solving conversation as a service
        script. Each of the 20 lines shows the Polish, the speaker, and the
        English translation, with annotations on the formal register and the
        service cycle. The learner performs it, then adapts it to a new
        problem - a leaking tap (cieknący kran), a broken phone (zepsuty
        telefon) - keeping the formal machinery. The demonstration program
        checks all 20 lines and the problem-solving phrases."""),
    key_points=[
        "20-line bilingual dialogue: reporting and solving a problem.",
        "Problem pattern: mam problem z + instrumental.",
        "Formal throughout: pan, proszę + infinitive, conditional.",
        "Full service cycle: report, diagnose, schedule, confirm.",
        "Adapt to a new problem keeping the formal machinery.",
    ],
    requirements=[
        "Learners must perform the dialogue staying formal throughout.",
        "Adapt it to a different broken appliance.",
    ],
    standards=[
        "CEFR A2-B1 service-encounter objectives.",
        "Formal register per Rada Języka Polskiego.",
    ],
    citations=[
        "Narodowy Korpus Języka Polskiego. Service-encounter patterns.",
        "Rada Języka Polskiego. Formal address guidance.",
    ],
    sig_lens=("Through the Signature lens, the service call is a repair "
              "order in words: the fault reported exactly, the remedy "
              "scheduled exactly, both parties signing off. This Signature "
              "reading treats the solved problem as the language proving "
              "it can fix real things."),
)

E(
    key="polish_mastery", name="Polish Mastery Review and Full Reference",
    group="Reference", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        The whole database in one teaching summary. Alphabet: a ą b c ć d
        e ę f g h i j k l ł m n ń o ó p r s ś t u w y z ź ż (32 letters;
        stress penultimate; ą/ę nasal; ł = w; ó = u). Sounds: retroflex sz
        cz ż/rz vs soft ś ć ź dź; final devoicing (Kraków = kraKUF). Core
        200 words (speed-round list): ja, ty, on, ona, my, wy, oni, być,
        mieć, robić, jeść, pić, iść, mówić, czytać, pisać, pracować, spać,
        mieszkać, kupować, widzieć, kochać, lubić, czekać, dzwonić, dom,
        książka, woda, chleb, mleko, samochód, ulica, miasto, kraj, świat,
        praca, szkoła, dzień, noc, czas, przyjaciel, rodzina, jedzenie,
        dobry, zły, duży, mały, nowy, stary, piękny, wysoki, długi, ciepły,
        zimny, szybki, łatwy, trudny, ważny, szczęśliwy, dobrze, szybko,
        bardzo, zawsze, nigdy, teraz, tutaj, jeden, dwa, trzy, pięć,
        dziesięć, dwadzieścia, sto, tysiąc, pierwszy, poniedziałek, wtorek,
        środa, piątek, niedziela, styczeń, maj, grudzień, wiosna, lato,
        jesień, zima, dzień dobry, cześć, do widzenia, dziękuję, proszę,
        przepraszam, tak, nie, kto, co, gdzie, kiedy, dlaczego, jak, ile,
        czy, głowa, ręka, noga, serce, mama, tata, siostra, brat, dziecko,
        mąż, żona, kot, pies, chleb, mleko, kawa, herbata, zupa, jabłko,
        sklep, targ, cena, pieniądz, telefon, komputer, internet, wiadomość,
        film, muzyka, książka, gazeta, list, e-mail, praca, spotkanie,
        lekcja, egzamin, lekarz, apteka, szpital, pogoda, deszcz, śnieg,
        słońce, wiatr, las, jezioro, rzeka, morze, góra, kwiat, drzewo,
        ptak, ryba, wioska, ulica, rynek, kościół, zamek, most, dworzec,
        lotnisko, hotel, restauracja, kawiarnia, muzeum, teatr, kino, park,
        ogród, kuchnia, salon, sypialnia, łazienka, okno, drzwi, stół,
        krzesło, łóżko, lustro, zegar, klucz, torba, walizka, parasol,
        okulary, zegarek, prezent, kwiat, świeca, obraz, dywan, poduszka,
        koc, ręcznik, mydło, szczotka, pasta, nożyczki, igła, nitka,
        guzik, zamek, pasek, kapelusz, czapka, szalik, rękawiczki, buty,
        skarpetki, koszula, spodnie, sukienka, płaszcz, kurtka, sweter,
        piłka, gra, zabawka, rower, samochód, pociąg, samolot, statek,
        autobus, tramwaj, taksówka, motocykl. Grammar in one breath: SVO
        flexible; 3 genders (ten/ta/to); 7 cases (mianownik, dopełniacz,
        celownik, biernik, narzędnik, miejscownik, wołacz); no articles; nie
        + verb negates (object to genitive); aspect pairs (robić/zrobić);
        present robię/robisz/robi; past robiłem/robiła; future będę
        robić / zrobię; imperative mów!; formal pan/pani + 3rd person.
        Phrase tables: 30 greetings (Dzień dobry... Do usłyszenia); 8
        question words; numbers 1-100; 20 idioms (Nie mój cyrk... Do trzech
        razy sztuka). Read top to bottom weekly, marking known/shaky/new;
        return to weak records. The 200-word speed round - Polish to
        English and back - under five minutes is the graduation test."""),
    how_it_works=textwrap.dedent("""\
        This record compresses the database into one reference page. The
        learner reads it top to bottom, marking each item known, shaky, or
        new, then returns to the weak records for another pass. The 200-word
        list is drilled as a speed round - Polish to English and back -
        until the whole list runs under five minutes. The mastery checker in
        the demonstration program verifies the 200-word count, the alphabet,
        the phrase tables, and the grammar summary against every record of
        this database, proving the reference complete. This is the record
        that turns thirty-three lessons into one language."""),
    key_points=[
        "The alphabet, the sounds, and the stress rules on one page.",
        "200 core words - the must-know list, drilled as a speed round.",
        "Grammar in one breath: order, cases, negation, aspect, tenses, imperative, formal address.",
        "Every phrase table compressed: 30 greetings, 8 question words, numbers 1-100, 20 idioms.",
        "Read weekly; mark known/shaky/new; return to weak records.",
    ],
    requirements=[
        "Run the 200-word speed round weekly until the full list takes under five minutes.",
        "Use this record as the checklist: every shaky item sends you back to its record.",
    ],
    standards=[
        "CEFR A1-B1 consolidated: the full scope of this database in one reference.",
        "Rada Języka Polskiego: standard forms throughout.",
    ],
    citations=[
        "Rada Języka Polskiego. Zasady pisowni i interpunkcji polskiej. Polish Academy of Sciences.",
        "Swan O E. Polish Verbs & Essentials of Grammar. 2nd ed. McGraw-Hill; 2008.",
        "Wielki słownik języka polskiego PAN.",
    ],
    sig_lens=("Through the Signature lens, the reference is the sealed archive "
              "itself: every record of the database compressed to its essence, "
              "every lesson countersigned in one place, the whole oath of the "
              "language in a single filing. This Signature reading treats mastery "
              "not as an ending but as the archive made portable."),
)

SIG_TAIL = ("Signature editions are his original Signature Language Method - "
            "every word a covenant between sound and meaning, every sentence a "
            "signed contract of understanding, the learner's voice the seal. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")
