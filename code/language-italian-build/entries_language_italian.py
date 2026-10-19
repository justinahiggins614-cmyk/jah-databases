#!/usr/bin/env python3
"""Entries for the Italian to English databases (34 ladder-ordered records).

Public records: real, fact-checked Italian language teaching - every record
carries Italian content with English translation and example sentences,
organized in the Signature system.
"""
import textwrap

ENTRIES = []


def E(**kw):
    ENTRIES.append(kw)
    return kw


E(
    key="italian_overview", name="Italian Language Overview",
    group="Language overview", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Italian (italiano) is a Romance language of the Indo-European family,
        the direct descendant of the Latin spoken in Italy - closer to Latin
        than any other major Romance language. It is the official language of
        Italy, Switzerland (with German and French), San Marino, and Vatican
        City, and a protected minority language in Slovenia and Croatia.
        Roughly 67 million people speak Italian as their first language and
        about 85 million speak it in total, counting the large diaspora in the
        Americas and Australia. Modern standard Italian grew out of the
        fourteenth-century Florentine literary language - the language of
        Dante, Petrarch, and Boccaccio - and was deliberately spread as the
        national language after Italian unification in 1861. The Accademia
        della Crusca, founded in Florence in 1583, is the official academy
        that watches over the language. Italy also holds dozens of regional
        languages and dialects - Sicilian, Neapolitan, Venetian, Lombard -
        which are distinct languages in their own right, not mere accents of
        Italian. Italian is the language of opera, of classical music
        terminology (piano, forte, allegro, crescendo), and of a cuisine whose
        words - pizza, pasta, espresso - traveled the world unchanged. This
        record is the map of the whole database: what Italian is, where it
        lives, and how the ladder below carries a learner from a first
        Buongiorno to full conversation. Sentences from the first step: Mi
        chiamo Anna. (My name is Anna.) Sono italiano / Sono italiana. (I am
        Italian - masculine / feminine.) Parlo un po' di italiano. (I speak a
        little Italian.)"""),
    how_it_works=textwrap.dedent("""\
        This record teaches the overview by anchoring every fact in a sentence
        the learner can say. Each fact - the native name italiano, the ISO
        codes it and ita, the language family path, the speaker numbers, the
        official countries, the Florentine literary roots, the Accademia della
        Crusca - appears with a plain English explanation and an Italian
        example sentence. The learner reads the facts, then repeats the
        sentences, so the overview is not memorized trivia but spoken language
        from the first record. Later records climb the teaching ladder:
        foundations (records 1-10: sounds, words, grammar basics), compounded
        (records 11-24: themed sentence sets and verb tenses), advanced
        (records 25-34: stories, idioms, registers, complex sentences,
        conversations, and a full reference)."""),
    key_points=[
        "Native name: italiano; English name: Italian; ISO 639-1: it; ISO 639-3: ita.",
        "Family: Indo-European > Italic > Romance > Italo-Dalmatian; closest major language to Latin.",
        "About 67 million native speakers; about 85 million total speakers worldwide.",
        "Official in Italy, Switzerland, San Marino, and Vatican City; protected in Slovenia and Croatia.",
        "Standard Italian descends from fourteenth-century Florentine; the Accademia della Crusca (1583) is the language academy.",
        "Every record in this database carries Italian content, English translation, and example sentences.",
    ],
    requirements=[
        "No prior knowledge of Italian is needed; this is the starting record of the ladder.",
        "Learners should read each example sentence aloud to begin training pronunciation from day one.",
    ],
    standards=[
        "ISO 639-1:1988 (it) and ISO 639-2:1998 (ita) language codes.",
        "Accademia della Crusca, Florence, founded 1583 - the official academy of the Italian language.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583. The official academy regulating the Italian language.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988. The standard reference grammar of Italian.",
        "Dardano M, Trifone P. Grammatica italiana con nozioni di linguistica. Zanichelli; 1995.",
    ],
    sig_lens=("Through the Signature lens, a language is not a school subject - it is a "
              "living contract between peoples, and Italian is one of the great signed "
              "contracts of human history: sixty-seven million voices keeping one oath of "
              "meaning from Florence to the world. This Signature reading treats the "
              "overview as the first seal of that contract."),
)

E(
    key="italian_writing", name="Italian Writing System",
    group="Writing and sound", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Italian is written with the Latin alphabet, read left to right, with
        21 native letters: A B C D E F G H I L M N O P Q R S T U V Z. Five
        more letters - J K W X Y - appear only in foreign words, names, and
        loanwords (jeans, kiwi, weekend, taxi, yogurt). The letter H is always
        silent: it marks the hard sounds in CH (chiesa, church) and GH
        (spaghetti), and distinguishes ho (I have) from o (or). Accents mark
        stress on final vowels: the grave accent on a, i, o, u (citta, lunedi,
        caffe, gioventu) and a choice of grave or acute on e - caffe (coffee,
        open e) vs perche (why/because, closed e). The accent is mandatory in
        writing whenever the stress falls on the final vowel: Sara (will be)
        without the accent would misread. The apostrophe marks elision where a
        vowel drops before another vowel: l'amico (the friend), un'amica (a
        friend - feminine), c'e (there is), dell'arte (of art). Question marks
        and exclamation marks work as in English, and quotation marks are
        usually « » (caporali) or " ". Numerals are the familiar Arabic digits
        0-9; the decimal system uses a comma where English uses a point (3,14
        for pi) and a period for thousands (1.000 = one thousand). Spelling is
        almost perfectly phonetic - once you know the sound rules, every word
        is pronounceable on sight, and almost every word is spelled as it
        sounds. Example lines: L'amico di Marco e simpatico. (Marco's friend
        is nice.) C'e un caffe in piazza. (There is a cafe in the square.)
        Perche no? (Why not?)"""),
    how_it_works=textwrap.dedent("""\
        This record teaches the writing system by pairing every letter and
        mark with a real word, its pronunciation hint, and its English
        translation. The learner copies the 21 letters, sounds each with its
        example word - C as in casa (house), H silent as in ho (I have) - and
        practices the accent marks by writing final-stress words by hand:
        citta, caffe, perche, lunedi. Elision is drilled by joining articles
        to vowel-words: lo + amico = l'amico; una + amica = un'amica. Because
        Italian spelling is almost perfectly phonetic, this one record unlocks
        reading for the entire database - the learner can sound out nearly
        any word they meet in later records."""),
    key_points=[
        "21 native letters; J K W X Y appear only in foreign words and names.",
        "H is always silent - it hardens C and G (chiesa, spaghetti) and marks ho vs o.",
        "Grave accent on final stressed vowels (a, i, o, u); e takes grave (caffe) or acute (perche).",
        "Apostrophe marks elision: l'amico, un'amica, c'e, dell'arte.",
        "Decimal comma (3,14), thousands period (1.000); spelling is almost perfectly phonetic.",
    ],
    requirements=[
        "Learners should write the 21 letters by hand once and say each with its example word.",
        "Practice final-stress accents first - citta, caffe, perche - they are mandatory in writing.",
    ],
    standards=[
        "Standard Italian orthography per the Accademia della Crusca.",
        "ISO 639-1:1988 (it); ISO 639-2:1998 (ita).",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, the alphabet is the contract's "
              "set of seals - twenty-one native stamps plus five foreign "
              "witnesses, every accent a raised mark proving where the "
              "stress falls. This Signature reading treats each written "
              "word as a signed line, spelled exactly as it sounds."),
)
E(
    key="italian_nouns", name="Italian Core Nouns",
    group="Core vocabulary", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five essential nouns - people, places, and things - each with
        its article (gender is part of the word), English meaning, and one
        example sentence translated. Every Italian noun is masculine or
        feminine, and the article teaches the gender: l'uomo (the man -
        masculine): L'uomo legge il giornale. (The man reads the newspaper.)
        la donna (the woman - feminine): La donna canta. (The woman sings.)
        il bambino (the child): Il bambino gioca. (The child plays.)
        l'amico / l'amica (the friend): Il mio amico arriva domani. (My friend
        arrives tomorrow.) la famiglia (the family): La famiglia e grande.
        (The family is big.) la casa (the house/home): La casa e bianca. (The
        house is white.) la porta (the door): Apri la porta. (Open the door.)
        la finestra (the window): La finestra e aperta. (The window is open.)
        il tavolo (the table): Il libro e sul tavolo. (The book is on the
        table.) la sedia (the chair): Siediti sulla sedia. (Sit on the chair.)
        il libro (the book): Leggo un libro. (I am reading a book.) la scuola
        (the school): La scuola inizia a settembre. (School starts in
        September.) il lavoro (the work/job): Il lavoro e interessante. (The
        work is interesting.) il giorno (the day): Che bel giorno! (What a
        beautiful day!) la notte (the night): Buona notte! (Good night!)
        il tempo (the time/weather): Che tempo fa? (What is the weather like?)
        l'acqua (the water - feminine): Bevo l'acqua. (I drink the water.)
        il cibo (the food): Il cibo e pronto. (The food is ready.) la macchina
        (the car): La macchina e rossa. (The car is red.) la strada (the
        street/road): La strada e lunga. (The street is long.) la citta (the
        city): Roma e una bella citta. (Rome is a beautiful city.) il paese
        (the town/country): Il mio paese e piccolo. (My town is small.)
        il mondo (the world): Il mondo e grande. (The world is big.) il nome
        (the name): Qual e il tuo nome? (What is your name?) il problema (the
        problem - masculine despite -a): Non c'e problema. (No problem.)
        Learn every noun WITH its article - il libro, la casa - because the
        article is the gender tag, and gender drives every agreement in the
        language."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nouns by the article-first method: the learner
        never meets a noun naked - it is always il libro, la casa, l'amico -
        so gender is absorbed with the word, not memorized separately. Each
        of the 25 nouns is drilled in a triple: say the noun with its article,
        say its English meaning, say the example sentence. The two
        rule-breakers are flagged early - il problema (masculine despite
        ending in -a) and l'acqua (feminine despite the apostrophe hiding the
        article) - so exceptions become familiar friends. The learner builds a
        personal picture dictionary: one page per noun, the Italian word big,
        the sentence underneath, the English small in the corner."""),
    key_points=[
        "25 core nouns: people, places, things - each with article, English, and a sentence.",
        "Gender lives in the article: learn il libro and la casa as single units.",
        "Masculine -o, feminine -a is the pattern; il problema and l'acqua are the famous exceptions.",
        "Every sentence uses only words the ladder has already taught - nothing to decode.",
        "Say each noun triple aloud: article + noun, meaning, sentence.",
    ],
    requirements=[
        "Learners should recite all 25 nouns with their articles from memory.",
        "Build a picture page for each noun with the Italian sentence underneath.",
    ],
    standards=[
        "Standard Italian nouns and articles per the Accademia della Crusca.",
        "Twenty-five nouns, each with English and a translated sentence.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, nouns are the contract's named "
              "parties - every person, place, and thing entered with its "
              "proper article-seal, masculine or feminine. This Signature "
              "reading treats each noun-with-article as a party duly "
              "identified before signing."),
)

E(
    key="italian_phonology", name="Italian Pronunciation and Phonology",
    group="Writing and sound", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The Italian sound system - every sound with an English approximation
        and example words translated. VOWELS (7 sounds, always pure - never
        diphthongs like English): a as in father - casa (house); e closed as
        in they-but-shorter - perche (why); e open as in bed - caffe (coffee);
        i as in machine - vino (wine); o closed as in go-but-shorter - sole
        (sun); o open as in bought - porta (door); u as in rule - luna (moon).
        CONSONANTS: C hard /k/ before a, o, u - casa (house), cosa (thing),
        cura (cure); C soft /tch/ before e, i - cena (dinner), cibo (food).
        G hard /g/ before a, o, u - gatto (cat), gola (throat); G soft /j/
        before e, i - gelato (ice cream), giro (tour). CH and GH are always
        hard - chiesa (church), spaghetti. SC hard /sk/ before a, o, u -
        scala (stairs); SC soft /sh/ before e, i - scena (scene). GN is the NY
        sound - gnocchi, signore (mister). GLI is the million-LL - famiglia
        (family), figlio (son). Z is /ts/ (pizza, grazie) or /dz/ (zero,
        zona). Double consonants are HELD longer - pala (shovel) vs palla
        (ball), nono (ninth) vs nonno (grandfather): hold the sound, do not
        just say it louder. STRESS falls on the second-to-last syllable -
        parlare, amico, telefono - unless the written accent says otherwise
        (citta, caffe, perche). R is trilled - practice with burro (butter).
        S between vowels is /z/ - rosa (rose), casa (house). QU is /kw/ -
        questo (this), quando (when). Twelve spoken examples to drill: casa,
        cena, gatto, gelato, chiesa, scena, gnocchi, famiglia, pizza, burro,
        perche, caffe - say each, exaggerating the target sound."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronunciation by the minimal-pair method: the
        learner drills the pairs that prove each rule - casa/cena for hard
        and soft C, gatto/gelato for G, pala/palla and nono/nonno for double
        consonants - saying each pair until the difference is physical. The
        seven vowels are learned as pure targets: the learner holds each
        vowel on one breath (a, e-closed, e-open, i, o-closed, o-open, u)
        with no English glide. Stress is practiced by clapping the syllables
        of parlare, amico, telefono, then reading accented words - citta,
        caffe, perche - with the stress slammed on the final syllable. The
        trilled R gets its own daily minute: burro, terra, carro, repeated
        until the tongue flutters."""),
    key_points=[
        "7 pure vowels: a, e-closed, e-open, i, o-closed, o-open, u - no glides.",
        "C/G hard before a, o, u; soft before e, i; CH/GH always hard; SC soft before e, i.",
        "GN = NY (gnocchi), GLI = million-LL (famiglia), Z = ts/dz (pizza, zero).",
        "Double consonants are held: pala/palla, nono/nonno - length changes meaning.",
        "Stress on the penultimate syllable unless the written accent marks the final.",
    ],
    requirements=[
        "Learners should drill the minimal pairs aloud until each contrast is automatic.",
        "Practice the trilled R for one minute daily: burro, terra, carro.",
    ],
    standards=[
        "Standard Italian pronunciation per the Accademia della Crusca.",
        "Twelve drill words, each with English approximation and translation.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, sounds are the contract read "
              "aloud - every vowel a clear tone, every double consonant a "
              "seal pressed twice for emphasis. This Signature reading "
              "treats pronunciation as the voice that gives the signature "
              "its authority."),
)

E(
    key="italian_adjectives", name="Italian Adjectives and Adverbs",
    group="Core vocabulary", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five adjectives and fifteen adverbs with example sentences -
        plus the agreement rule that governs them all. Adjectives agree in
        gender and number with the noun: -o becomes -a, -i, -e. bello (beautiful):
        un bel ragazzo (a handsome boy), una bella ragazza (a beautiful girl),
        bei ragazzi, belle ragazze. brutto (ugly): un brutto voto (a bad grade).
        buono (good): un buon caffe (a good coffee). cattivo (bad): un cattivo
        esempio (a bad example). grande (big): una grande citta (a big city).
        piccolo (small): un piccolo regalo (a small gift). nuovo (new): una
        macchina nuova (a new car). vecchio (old): un vecchio amico (an old
        friend). alto (tall): un uomo alto (a tall man). basso (short/low): una
        sedia bassa (a low chair). lungo (long): una strada lunga (a long road).
        corto (short): un racconto corto (a short story). giovane (young): una
        donna giovane (a young woman). anziano (elderly): un signore anziano
        (an elderly gentleman). felice (happy): un bambino felice (a happy
        child). triste (sad): una storia triste (a sad story). caldo (hot): un
        caffe caldo (a hot coffee). freddo (cold): una sera fredda (a cold
        evening). dolce (sweet): una torta dolce (a sweet cake). amaro
        (bitter): un caffe amaro (a bitter coffee). rosso (red): una mela rossa
        (a red apple). verde (green): un prato verde (a green lawn). bianco
        (white): una casa bianca (a white house). nero (black): un gatto nero
        (a black cat). facile (easy): un esame facile (an easy exam).
        ADVERBS (do not change form): molto (very/much): molto bello. poco
        (little): poco tempo. bene (well): canta bene. male (badly): parla
        male. sempre (always): sempre puntuale. mai (never): non esco mai.
        gia (already): ho gia mangiato. ancora (still/yet): sei ancora qui?
        troppo (too): troppo caro. presto (soon/early): a presto! tardi
        (late): arriva tardi. qui (here): vieni qui. li/la (there): mettilo li.
        cosi (so/thus): cosi bello! forse (maybe): forse domani. Agreement in
        one line: the adjective dresses to match its noun - masculine,
        feminine, singular, plural."""),
    how_it_works=textwrap.dedent("""\
        This record teaches adjectives by the matching method: the learner
        takes each adjective through its four forms - bello, bella, belli,
        belle - attached to a real noun, until agreement feels like dressing
        the noun correctly. Adverbs are drilled as the unchanging partners:
        molto, bene, sempre never change no matter what they modify. The
        learner plays the agreement game: given a noun (ragazza) and an
        adjective (bello), produce the pair (bella ragazza) - twenty-five
        rounds. Then the adverb ladder: modify each adjective sentence with
        molto, troppo, poco and feel the meaning shift."""),
    key_points=[
        "25 adjectives + 15 adverbs, each with a translated example sentence.",
        "Agreement rule: adjectives match gender and number - bello/bella/belli/belle.",
        "Most adjectives follow the noun: una macchina nuova, un caffe caldo.",
        "Adverbs never change: molto, bene, sempre, mai, troppo.",
        "Buono and bello have special short forms before nouns: un buon caffe, un bel ragazzo.",
    ],
    requirements=[
        "Learners should run all 25 adjectives through the four-form agreement drill.",
        "Play the agreement game: noun + adjective -> correct pair, 25 rounds.",
    ],
    standards=[
        "Standard Italian adjective agreement per the Accademia della Crusca.",
        "Forty words total, each with a translated example sentence.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, adjectives are the contract's "
              "descriptive clauses - each one tailored to fit its noun in "
              "gender and number, while adverbs stand as the unchanging "
              "witnesses. This Signature reading treats agreement as the "
              "grammar of a well-fitted seal."),
)

E(
    key="italian_verbs", name="Italian Core Verbs",
    group="Core vocabulary", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five essential verbs - each with its English meaning and one
        example sentence translated. The present tense is shown in the io
        form; the full conjugation engine arrives in the tenses record.
        essere (to be): Sono felice. (I am happy.) avere (to have): Ho due
        fratelli. (I have two brothers.) fare (to do/make): Faccio colazione.
        (I have breakfast.) andare (to go): Vado a scuola. (I go to school.)
        dire (to say/tell): Dico la verita. (I tell the truth.) vedere (to
        see): Vedo il mare. (I see the sea.) mangiare (to eat): Mangio la
        pizza. (I eat pizza.) bere (to drink): Bevo l'acqua. (I drink water.)
        parlare (to speak): Parlo italiano. (I speak Italian.) scrivere (to
        write): Scrivo una lettera. (I write a letter.) leggere (to read):
        Leggo un libro. (I read a book.) dormire (to sleep): Dormo otto ore.
        (I sleep eight hours.) lavorare (to work): Lavoro in banca. (I work in
        a bank.) studiare (to study): Studio medicina. (I study medicine.)
        comprare (to buy): Compro il pane. (I buy the bread.) vendere (to
        sell): Vende frutta. (He sells fruit.) aprire (to open): Apro la
        finestra. (I open the window.) chiudere (to close): Chiudo la porta.
        (I close the door.) prendere (to take): Prendo il treno. (I take the
        train.) dare (to give): Do un regalo. (I give a gift.) venire (to
        come): Vengo domani. (I come tomorrow.) sapere (to know a fact): So
        la risposta. (I know the answer.) conoscere (to know a person/place):
        Conosco Roma. (I know Rome.) pensare (to think): Penso spesso a te.
        (I often think of you.) amare (to love): Amo la mia famiglia. (I love
        my family.) Three verb families: -are (parlare, mangiare), -ere
        (vedere, scrivere), -ire (dormire, aprire) - the ending tells you the
        family, and the family tells you the pattern. Sapere vs conoscere: facts
        vs people and places - a distinction English does not make."""),
    how_it_works=textwrap.dedent("""\
        This record teaches verbs by the action method: the learner performs
        each verb as they say it - mangio with a bite mime, dormo with closed
        eyes, apro opening an imaginary window - binding the word to the
        muscle. Each verb is drilled in a triple: infinitive, English, io-form
        sentence. The three families are sorted by ending: all -are verbs
        together, all -ere, all -ire, so the pattern of each family emerges
        before any conjugation table is shown. Sapere and conoscere get a
        special contrast drill: So la risposta (fact) vs Conosco Marco
        (person) - the learner sorts ten items into the two verbs."""),
    key_points=[
        "25 core verbs: each with English meaning and a translated io-form sentence.",
        "Three families by ending: -are, -ere, -ire - the ending predicts the pattern.",
        "Sapere = know facts; conoscere = know people and places.",
        "Essere and avere are the twin pillars - every compound tense needs one.",
        "Perform each verb physically while saying it: the muscle remembers.",
    ],
    requirements=[
        "Learners should drill each verb as a triple: infinitive, meaning, sentence.",
        "Sort the 25 verbs into -are, -ere, -ire families from memory.",
    ],
    standards=[
        "Standard Italian verb forms per the Accademia della Crusca.",
        "Twenty-five verbs, each with English and a translated sentence.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, verbs are the contract's action "
              "clauses - essere and avere the twin pillars holding up every "
              "tense, each of the twenty-five a deed performed by the "
              "signer. This Signature reading treats the io form as the "
              "signature itself: I do, I am, I speak."),
)
E(
    key="italian_numbers", name="Italian Numbers and Time",
    group="Core vocabulary", ladder_rank=4, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Numbers 1 to 100, ordinals, days, months, seasons, clock time, and
        dates - each with example sentences. CARDINALS: uno, due, tre,
        quattro, cinque, sei, sette, otto, nove, dieci, undici, dodici,
        tredici, quattordici, quindici, sedici, diciassette, diciotto,
        diciannove, venti, trenta, quaranta, cinquanta, sessanta, settanta,
        ottanta, novanta, cento. Compounds join directly: ventuno (21),
        trentadue (32), quarantotto (48) - note the final vowel drops before
        uno and otto: ventuno, ventotto. Ho trent'anni. (I am thirty - years
        old.) Costa venti euro. (It costs twenty euros.) ORDINALS: primo,
        secondo, terzo, quarto, quinto, sesto, settimo, ottavo, nono, decimo.
        E il primo giorno. (It is the first day.) Abito al secondo piano. (I
        live on the second floor.) DAYS: lunedi, martedi, mercoledi, giovedi,
        venerdi, sabato, domenica. Ci vediamo lunedi. (See you Monday.) Di
        domenica riposo. (On Sundays I rest.) MONTHS: gennaio, febbraio, marzo,
        aprile, maggio, giugno, luglio, agosto, settembre, ottobre, novembre,
        dicembre. Il mio compleanno e a giugno. (My birthday is in June.)
        SEASONS: primavera, estate, autunno, inverno. In estate fa caldo. (In
        summer it is hot.) CLOCK TIME: Che ore sono? (What time is it?) E
        l'una. (It is one o'clock - singular.) Sono le due. (It is two -
        plural.) Sono le tre e mezza. (It is half past three.) Sono le quattro
        e un quarto. (It is quarter past four.) Sono le cinque meno dieci.
        (It is ten to five.) A che ora? Alle otto. (At what time? At eight.)
        DATES: Oggi e il cinque maggio. (Today is May fifth.) Sono nato il
        dieci ottobre. (I was born October tenth.) The year: duemilaventisei
        (2026) - mille + the rest, said as one flowing word."""),
    how_it_works=textwrap.dedent("""\
        This record teaches numbers by the counting method: the learner counts
        aloud 1-20, then the tens to 100, then builds compounds - trentadue,
        quarantotto - hearing the vowel drop before uno and otto. Time is
        drilled on a real clock: the learner says the actual time in Italian
        every hour - Sono le tre, Sono le tre e mezza - until E l'una vs Sono
        le due is reflex. Days and months are learned in order by planning a
        real week and a real year: appointments on lunedi, birthdays in
        giugno. The final test: give your phone number, your birthdate, and
        the current time, all in Italian, without hesitation."""),
    key_points=[
        "Cardinals 1-100: compounds join directly - ventuno, trentadue; vowel drops before uno/otto.",
        "Ordinals: primo through decimo; il primo giorno, al secondo piano.",
        "Time: E l'una (singular) vs Sono le due (plural); e mezza, e un quarto, meno dieci.",
        "Days, months, seasons learned in order by planning a real week and year.",
        "Years flow as one word: duemilaventisei for 2026.",
    ],
    requirements=[
        "Learners should count 1-100 aloud without stopping.",
        "Say the real time in Italian every hour for one full day.",
    ],
    standards=[
        "Standard Italian numbers and time expressions per the Accademia della Crusca.",
        "All forms 1-100, ordinals, days, months, seasons, clock time, and dates.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, numbers are the contract's "
              "exact figures - every price, date, and hour stamped in "
              "digits that cannot be misread, from uno to cento. This "
              "Signature reading treats the clock as the seal that dates "
              "every clause."),
)

E(
    key="italian_pronouns", name="Italian Pronouns",
    group="Core vocabulary", ladder_rank=4, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Personal, possessive, demonstrative, and interrogative pronouns - full
        paradigms with example sentences. SUBJECT PRONOUNS (usually dropped,
        used for emphasis): io (I), tu (you - informal), lui (he), lei (she),
        Lei (you - formal, capitalized), noi (we), voi (you all), loro (they).
        Io parlo italiano. (I speak Italian - emphasis: *I* do.) Parlo
        italiano. (I speak Italian - normal, pronoun dropped.) OBJECT
        PRONOUNS: mi (me), ti (you), lo/la (him/her/it), ci (us), vi (you all),
        li/le (them). Mi vedi? (Do you see me?) Ti amo. (I love you.) Lo
        compro. (I buy it - masculine.) La compro. (I buy it - feminine.)
        INDIRECT: mi, ti, gli/le (to him/to her), ci, vi, loro. Gli parlo.
        (I speak to him.) Le scrivo. (I write to her.) REFLEXIVE: mi, ti, si,
        ci, vi, si. Mi chiamo Anna. (I call myself Anna = My name is Anna.)
        Si sveglia presto. (He wakes up early.) POSSESSIVES (agree with the
        THING owned, not the owner): il mio / la mia / i miei / le mie (my),
        il tuo / la tua (your), il suo / la sua (his/her), il nostro / la
        nostra (our), il vostro / la vostra (your all), il loro / la loro
        (their - never changes). Il mio libro. (My book.) La tua casa. (Your
        house.) I suoi amici. (His friends.) DEMONSTRATIVES: questo (this -
        near me), quello (that - far). Questo libro e mio. (This book is
        mine.) Quel ragazzo e alto. (That boy is tall.) INTERROGATIVES: chi
        (who), che/cosa (what), quale (which), quanto (how much). Chi e? (Who
        is it?) Che cos'e? (What is it?) Ne replaces di + thing: Ne voglio
        due. (I want two of them.) Ci replaces a + place: Ci vado domani. (I
        go there tomorrow.)"""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronouns by the substitution method: the learner
        takes a full sentence - Compro il libro - and swaps the noun for the
        pronoun - Lo compro - feeling the pronoun slide before the verb. The
        possessive trap is drilled explicitly: il mio libro vs la mia casa
        proves the possessive follows the thing owned, never the owner. The
        subject-drop habit is built by translating English sentences with io
        and tu, then deleting them: Io parlo becomes Parlo. Reflexives are
        learned through the name ritual: Mi chiamo..., Ti chiami..., Si
        chiama... - every introduction practices the paradigm."""),
    key_points=[
        "Subject pronouns usually dropped: Parlo italiano, not Io parlo - used for emphasis.",
        "Object pronouns go before the verb: Lo compro, Mi vedi, Ti amo.",
        "Possessives agree with the thing owned: il mio libro, la mia casa, i suoi amici.",
        "Questo (near me) vs quello (far); chi/che/quale/quanto for questions.",
        "Ne (of it/them) and ci (there) are the small words that make speech fluent.",
    ],
    requirements=[
        "Learners should convert 10 noun sentences to pronoun sentences.",
        "Drill the reflexive name ritual: Mi chiamo, Ti chiami, Si chiama.",
    ],
    standards=[
        "Standard Italian pronoun paradigms per the Accademia della Crusca.",
        "Full paradigms: personal, possessive, demonstrative, interrogative.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, pronouns are the contract's "
              "shorthand - the parties named once, then referred to by "
              "their seals: lo, la, mi, ti. This Signature reading treats "
              "each pronoun as a duly appointed representative of its "
              "noun."),
)

E(
    key="italian_greetings", name="Italian Greetings and Everyday Phrases",
    group="Core vocabulary", ladder_rank=5, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Thirty greetings, farewells, and politeness phrases - each with
        English and usage notes. Buongiorno! (Good morning / good day - until
        mid-afternoon, the universal greeting.) Buonasera! (Good evening -
        from late afternoon on; never say buona notte as a greeting.)
        Buonanotte! (Good night - only when parting for sleep.) Ciao! (Hi /
        bye - informal only, friends and family.) Salve! (Hello - polite but
        not stiff, the safe middle.) Arrivederci! (Goodbye - standard.)
        ArrivederLa! (Goodbye - formal.) A presto! (See you soon!) A domani!
        (See you tomorrow!) A dopo! (See you later!) Benvenuto! / Benvenuta!
        (Welcome - masculine / feminine.) Piacere! (Pleased to meet you -
        with the handshake.) Come sta? (How are you - formal.) Come stai?
        (How are you - informal.) Tutto bene? (All good?) Bene, grazie! (Well,
        thanks!) Grazie mille! (Thanks a lot!) Prego! (You are welcome / after
        you / please come in - the hardest-working word.) Per favore! (Please!)
        Mi scusi! (Excuse me - formal.) Scusa! (Sorry - informal.) Permesso!
        (Excuse me - to pass through.) Auguri! (Best wishes! - birthdays,
        holidays, any celebration.) Complimenti! (Congratulations!) In bocca
        al lupo! (Good luck! - answer: Crepi!) Buon appetito! (Enjoy your
        meal!) Buon viaggio! (Have a good trip!) Buona giornata! (Have a good
        day!) Salute! (Bless you! - after a sneeze; also cheers.) Di niente!
        (It is nothing - you are welcome.) Non c'e di che! (Do not mention
        it!) Va bene! (OK! / All right!) D'accordo! (Agreed!) The golden rule:
        Buongiorno opens every interaction with a stranger - shops, offices,
        elevators - and skipping it is the famous foreigner mistake."""),
    how_it_works=textwrap.dedent("""\
        This record teaches greetings by the doorway method: the learner
        practices each phrase as an entrance or exit - Buongiorno stepping
        into a shop, Arrivederci leaving it, Permesso squeezing past, Prego
        holding a door. The tu/Lei pairs are drilled side by side - Come stai
        vs Come sta, Scusa vs Mi scusi - until the register choice is
        instant. The learner runs the day script: wake (Buongiorno), shop
        (Permesso, Per favore, Grazie, Arrivederci), sneeze (Salute),
        evening (Buonasera), bed (Buonanotte) - one full day of Italian
        entrances and exits."""),
    key_points=[
        "30 phrases: greetings, farewells, thanks, wishes - each with usage notes.",
        "Buongiorno opens every stranger interaction; skipping it is the classic mistake.",
        "Ciao is informal only; Salve is the safe polite middle; ArrivederLa is formal.",
        "Prego does triple duty: you are welcome, after you, please come in.",
        "In bocca al lupo needs its answer: Crepi! - learn the pair, not half.",
    ],
    requirements=[
        "Learners should perform the full day script: 15 entrances and exits in order.",
        "Drill every tu/Lei pair until the register choice is instant.",
    ],
    standards=[
        "Standard Italian greeting formulas per the Accademia della Crusca.",
        "Thirty phrases, each with English and usage notes.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, greetings are the contract's "
              "opening formalities - Buongiorno the seal broken at the "
              "start, Arrivederci the signatures exchanged at the end. "
              "This Signature reading treats every polite phrase as "
              "protocol duly observed."),
)

E(
    key="italian_grammar", name="Italian Grammar Essentials",
    group="Grammar", ladder_rank=5, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The essential grammar rules - word order, gender, number, articles,
        negation, and questions - each rule with translated example sentences.
        WORD ORDER is Subject-Verb-Object: Marco mangia la pizza. (Marco eats
        the pizza.) Adjectives usually follow the noun: una macchina rossa (a
        red car) - though common ones like bello and buono often precede: un
        bel giorno (a beautiful day). GENDER: every noun is masculine or
        feminine - il ragazzo (the boy), la ragazza (the girl). Masculine
        nouns usually end in -o, feminine in -a. NUMBER: masculine -o becomes
        -i (ragazzo/ragazzi), feminine -a becomes -e (ragazza/ragazze).
        ARTICLES: definite - il (masc. sing.), lo (masc. before s+consonant,
        z, gn: lo studente, lo zaino), la (fem. sing.: la casa), l' (before
        vowels: l'amico, l'acqua), i (masc. pl.: i ragazzi), gli (masc. pl.
        before vowels and s+consonant: gli amici, gli studenti), le (fem. pl.:
        le case). Indefinite - un (masc.: un libro), uno (before s+consonant,
        z: uno studente), una (fem.: una casa), un' (before feminine vowels:
        un'amica). Il gatto dorme. (The cat sleeps.) Ho visto un film. (I saw
        a movie.) NEGATION: non before the verb - Non parlo francese. (I do
        not speak French.) Non ho capito. (I did not understand.) Mai, niente,
        nessuno need non too: Non vedo nessuno. (I see nobody.) QUESTIONS:
        raise your intonation - Parli italiano? (Do you speak Italian?) - or
        front a question word: Dove abiti? (Where do you live?) No inversion,
        no do-support. C'E / CI SONO: C'e un problema. (There is a problem.)
        Ci sono due gatti. (There are two cats.) ESSERE vs AVERE: Sono felice.
        (I am happy.) Ho fame. (I am hungry - literally I have hunger.)"""),
    how_it_works=textwrap.dedent("""\
        This record teaches grammar by the rule-and-sentence method: each
        rule is stated in one line, then proved by three translated sentences
        the learner says aloud. The article table is drilled as a chant - il,
        lo, la, l', i, gli, le - with a noun for each slot: il libro, lo
        studente, la casa, l'amico, i libri, gli studenti, le case. Negation
        is practiced by flipping: the learner takes ten positive sentences
        from earlier records and negates them - Parlo italiano becomes Non
        parlo italiano. Questions are built by intonation first (say it
        rising), then with question words. The c'e/ci sono pair is drilled
        with a room scan: C'e un tavolo, Ci sono due sedie."""),
    key_points=[
        "SVO word order; adjectives usually follow the noun.",
        "Gender and number: -o/-a singular, -i/-e plural; the article table (il, lo, la, l', i, gli, le).",
        "Negation: non before the verb; mai/niente/nessuno still need non.",
        "Questions by intonation or question word - no inversion, no do-support.",
        "C'e (singular) vs Ci sono (plural); Ho fame (avere) vs Sono felice (essere).",
    ],
    requirements=[
        "Learners should chant the article table with one noun per slot.",
        "Flip ten positive sentences to negative with non.",
    ],
    standards=[
        "Standard Italian core grammar per the Accademia della Crusca.",
        "Every rule proved by translated example sentences.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, grammar is the contract's "
              "binding law - word order its procedure, articles its "
              "identification seals, negation its veto clause. This "
              "Signature reading treats each rule as an article of the "
              "instrument, proven by signed example sentences."),
)
E(
    key="italian_home_family", name="Italian Home and Family Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the house, its rooms, its furniture, and the
        family - the first real conversations of daily life. Abito in un
        appartamento in centro. (I live in an apartment downtown.) La mia casa
        ha tre camere da letto. (My house has three bedrooms.) Il soggiorno e
        grande e luminoso. (The living room is big and bright.) La cucina e
        il cuore della casa. (The kitchen is the heart of the house.) Il
        bagno e in fondo al corridoio. (The bathroom is at the end of the
        hall.) C'e un bel balcone con vista. (There is a nice balcony with a
        view.) Il tavolo e in sala da pranzo. (The table is in the dining
        room.) Il divano e comodo. (The sofa is comfortable.) Ho un giardino
        piccolo dietro casa. (I have a small garden behind the house.) La mia
        famiglia e numerosa. (My family is large.) Mio padre lavora in banca.
        (My father works in a bank.) Mia madre insegna a scuola. (My mother
        teaches at school.) Ho un fratello e due sorelle. (I have a brother
        and two sisters.) Mio nonno racconta belle storie. (My grandfather
        tells beautiful stories.) Mia nonna cucina benissimo. (My
        grandmother cooks wonderfully.) Mio zio abita a Milano. (My uncle
        lives in Milan.) Mia cugina viene a trovarci domenica. (My cousin is
        coming to visit us Sunday.) Siamo una famiglia unita. (We are a
        close-knit family.) A Natale ci riuniamo tutti. (At Christmas we all
        gather.) Casa dolce casa! (Home sweet home!) Family words learned
        along the way: il marito (husband), la moglie (wife), il figlio (son),
        la figlia (daughter), il nipote (grandson/nephew), la nipote
        (granddaughter/niece), i genitori (parents), i parenti (relatives).
        Note: with family members in the singular, Italian drops the article
        - mio padre, not il mio padre - except with loro (il loro padre) and
        affectionate diminutives (la mia mamma)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches home and family by the house-tour method: the
        learner walks through their real home naming each room and three
        objects in it - Il soggiorno, Il divano e comodo - then introduces
        their real family member by member: Mio padre..., Mia madre..., Ho un
        fratello... The article-drop rule with family (mio padre, not il mio
        padre) is drilled as the exception that proves the article system.
        The learner draws a family tree and labels every branch in Italian,
        then gives the house tour to a partner entirely in Italian."""),
    key_points=[
        "20 sentences: rooms, furniture, and the full family.",
        "Room scan with c'e/ci sono: C'e un bel balcone, Il tavolo e in sala.",
        "Family article rule: mio padre (no article), but il loro padre and la mia mamma.",
        "8 family words: marito, moglie, figlio, figlia, nipote, genitori, parenti.",
        "Give a real house tour and introduce your real family in Italian.",
    ],
    requirements=[
        "Learners should name every room of their home in Italian with three objects each.",
        "Draw and label a full family tree in Italian.",
    ],
    standards=[
        "Standard Italian home and family vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, the home is the contract's "
              "registered address - every room a clause, every family "
              "member a party to the covenant. This Signature reading "
              "treats the family tree as the seal's own genealogy."),
)

E(
    key="italian_food_cooking", name="Italian Food and Cooking Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for meals, ingredients, cooking actions, and the
        restaurant - Italy's delicious core. La colazione e il pasto piu
        importante. (Breakfast is the most important meal.) Faccio colazione
        con caffe e cornetto. (I have breakfast with coffee and croissant.)
        A pranzo mangio pasta. (For lunch I eat pasta.) La cena e alle otto.
        (Dinner is at eight.) Cucino la pasta al dente. (I cook the pasta al
        dente.) Aggiungo il sale all'acqua. (I add salt to the water.) Taglio
        le verdure a pezzetti. (I cut the vegetables into pieces.) Friggo le
        uova in padella. (I fry the eggs in the pan.) Il sugo cuoce a fuoco
        lento. (The sauce simmers on low heat.) Assaggio e aggiusto di sale.
        (I taste and adjust the salt.) La pizza e nel forno. (The pizza is in
        the oven.) Il pane e fresco di oggi. (The bread is fresh today.) Vorrei
        il menu, per favore. (I would like the menu, please.) Prendo gli
        spaghetti al pomodoro. (I will have the spaghetti with tomato.) Il
        vino rosso e ottimo. (The red wine is excellent.) Il conto, per
        favore. (The check, please.) Il servizio e incluso? (Is service
        included?) Che buono! (How delicious!) Ho mangiato troppo. (I ate too
        much.) Domani cucino io. (Tomorrow I am cooking.) Food words learned
        along the way: l'antipasto (starter), il primo (first course), il
        secondo (main course), il contorno (side dish), il dolce (dessert),
        il formaggio (cheese), la frutta (fruit). Meal verbs: cucinare,
        cuocere, friggere, bollire, assaggiare, condire."""),
    how_it_works=textwrap.dedent("""\
        This record teaches food by the kitchen method: the learner cooks one
        real dish narrating every step in Italian - Taglio le verdure,
        Aggiungo il sale, Assaggio - so the cooking verbs live in the hands.
        The restaurant script is rehearsed as a full performance: entrance,
        Vorrei il menu, ordering (Prendo...), the check (Il conto, per
        favore). The three-course structure - antipasto, primo, secondo,
        contorno, dolce - is learned by planning a real Italian dinner menu.
        Taste words (buono, delizioso, al dente, fresco) are attached to real
        bites."""),
    key_points=[
        "20 sentences: meals, cooking actions, restaurant script.",
        "Cooking verbs: cucinare, cuocere, friggere, bollire, assaggiare, condire.",
        "Restaurant script: Vorrei il menu -> Prendo... -> Il conto, per favore.",
        "Italian meal structure: antipasto, primo, secondo, contorno, dolce.",
        "Cook a real dish narrating every step in Italian.",
    ],
    requirements=[
        "Learners should cook one dish narrating each step in Italian.",
        "Perform the full restaurant script in pairs.",
    ],
    standards=[
        "Standard Italian food and cooking vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, the meal is the contract's "
              "celebration feast - every course a clause savored, every "
              "recipe a formula handed down and signed. This Signature "
              "reading treats the shared table as the seal pressed in "
              "good company."),
)

E(
    key="italian_travel", name="Italian Travel and Directions Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for transport, asking directions, tickets, and
        lodging. Dov'e la stazione? (Where is the station?) Come arrivo al
        Duomo? (How do I get to the cathedral?) Vada dritto, poi giri a
        destra. (Go straight, then turn right - formal.) La fermata
        dell'autobus e qui vicino. (The bus stop is near here.) Prendo il
        treno delle nove. (I take the nine o'clock train.) Il treno parte dal
        binario due. (The train leaves from platform two.) Quanto costa un
        biglietto per Venezia? (How much is a ticket to Venice?) Un biglietto
        di andata e ritorno. (A round-trip ticket.) L'aereo decolla alle
        sette. (The plane takes off at seven.) Ho perso la coincidenza. (I
        missed the connection.) Chiami un taxi, per favore? (Will you call a
        taxi, please?) Noleggio una macchina per tre giorni. (I am renting a
        car for three days.) Mi sono perso. Può aiutarmi? (I am lost. Can you
        help me? - formal.) Ho prenotato una camera doppia. (I booked a double
        room.) La colazione e inclusa? (Is breakfast included?) A che ora e il
        check-out? (What time is check-out?) Il passaporto e in cassaforte.
        (The passport is in the safe.) Buon viaggio! (Have a good trip!)
        Benvenuti in Italia! (Welcome to Italy!) Travel words learned along
        the way: il biglietto (ticket), l'orario (timetable), il binario
        (platform), il ritardo (delay), la coincidenza (connection), la
        prenotazione (reservation), la camera singola/doppia (single/double
        room). Directions toolkit: dritto (straight), a destra (right), a
        sinistra (left), vicino (near), lontano (far), dietro (behind),
        davanti (in front)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches travel by the journey method: the learner plans a
        real three-day Italian trip - trains, hotel, sights - conducting every
        step in Italian: booking (Ho prenotato una camera), ticketing (Un
        biglietto per Venezia), navigating (Dov'e la stazione?). Directions
        are drilled as give-and-take: one learner is lost (Mi sono perso),
        the other directs with the formal imperatives (Vada dritto, Giri a
        destra). The direction toolkit - dritto, destra, sinistra, vicino,
        lontano - is learned as one sealed set, and the ticket/hotel scripts
        are rehearsed until the learner can survive any Italian station or
        reception desk."""),
    key_points=[
        "20 sentences: transport, directions, tickets, lodging.",
        "Ask: Dov'e...? Come arrivo a...? Quanto costa...?",
        "Formal imperatives for strangers: Vada dritto, Giri a destra.",
        "Direction toolkit: dritto, destra, sinistra, vicino, lontano, dietro, davanti.",
        "Plan a real three-day trip conducting every step in Italian.",
    ],
    requirements=[
        "Learners should ask for and give directions to three real places.",
        "Role-play booking a hotel room and buying a train ticket.",
    ],
    standards=[
        "Standard Italian travel formulas per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, the journey is the contract's "
              "signed route - the ticket its seal, every direction a clause "
              "of the itinerary. This Signature reading treats each leg of "
              "the trip as a witnessed passage: partenza, viaggio, arrivo."),
)

E(
    key="italian_work_school", name="Italian Work and School Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for jobs, the office, the classroom, and learning.
        Faccio l'ingegnere. (I am an engineer - literally I do the
        engineer.) Lavoro in un ufficio in centro. (I work in a downtown
        office.) Ho una riunione alle dieci. (I have a meeting at ten.) Il mio
        capo e esigente. (My boss is demanding.) I colleghi sono gentili.
        (The colleagues are kind.) Vado al lavoro in treno. (I commute by
        train.) Lo stipendio arriva a fine mese. (The salary arrives at
        month's end.) Cerco lavoro da un mese. (I have been job-hunting for a
        month.) Ho un colloquio domani. (I have an interview tomorrow.) Studio
        all'universita. (I study at the university.) La lezione inizia alle
        otto. (The lesson starts at eight.) Il professore spiega bene. (The
        professor explains well.) Devo fare i compiti. (I must do homework.)
        Domani ho l'esame di matematica. (Tomorrow I have the math exam.) Ho
        preso trenta e lode. (I got 30 cum laude - the top university grade.)
        La biblioteca chiude alle sette. (The library closes at seven.) Mi
        sono laureato l'anno scorso. (I graduated last year.) Imparo
        l'italiano ogni giorno. (I learn Italian every day.) Buon lavoro!
        (Have a good workday!) In bocca al lupo per l'esame! (Good luck on
        the exam!) Work words learned along the way: il colloquio
        (interview), la riunione (meeting), il progetto (project), la pausa
        (break), il contratto (contract). School words: il voto (grade), la
        materia (subject), l'interrogazione (oral test), la laurea (degree).
        The university scale runs 18 to 30, with 30 e lode the crown."""),
    how_it_works=textwrap.dedent("""\
        This record teaches work and school by the workday method: the learner
        narrates a real workday or school day hour by hour in Italian - Ho una
        riunione alle dieci, Faccio pausa a mezzogiorno, La lezione inizia
        alle otto - anchoring time expressions to real events. Job hunting is
        practiced as a script: Cerco lavoro, Ho un colloquio domani. The
        grading scale is learned by reporting real or imagined grades: Ho
        preso ventotto. The profession pattern Faccio il/la + noun (Faccio
        l'ingegnere, Fa il medico) is drilled across ten jobs until the
        construction is automatic."""),
    key_points=[
        "20 sentences: jobs, office, classroom, learning.",
        "Professions: Faccio l'ingegnere - fare + article + job.",
        "Time anchors: alle dieci, a fine mese, da un mese (duration).",
        "University grades 18-30; 30 e lode is the top.",
        "Narrate a real workday or school day hour by hour in Italian.",
    ],
    requirements=[
        "Learners should narrate a full workday or school day in Italian.",
        "Drill Faccio il/la across ten professions.",
    ],
    standards=[
        "Standard Italian work and school vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, work and study are the contract's "
              "daily sealings - each shift a stamp, each exam a signature on "
              "the record. This Signature reading treats every workday as a "
              "page duly executed and every grade as a seal of merit."),
)


E(
    key="italian_health_body", name="Italian Health and Body Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for body parts, symptoms, the doctor, and the
        pharmacy. Mi fa male la testa. (My head hurts - literally the head
        hurts me.) Mi fanno male i piedi. (My feet hurt.) Ho mal di gola. (I
        have a sore throat.) Ho la febbre. (I have a fever.) Ho il
        raffreddore. (I have a cold.) Ho la tosse. (I have a cough.) Mi gira
        la testa. (I am dizzy - my head spins.) Ho mal di stomaco. (My
        stomach hurts.) Sono allergico alle noci. (I am allergic to nuts.)
        Devo vedere un medico. (I need to see a doctor.) Ho un appuntamento
        dal dottore. (I have a doctor's appointment.) Prendo questa medicina
        due volte al giorno. (I take this medicine twice a day.) Dov'e la
        farmacia piu vicina? (Where is the nearest pharmacy?) Ha qualcosa per
        il mal di testa? (Do you have something for a headache?) Mi serve una
        ricetta? (Do I need a prescription?) Devo riposare qualche giorno.
        (I need to rest a few days.) Beva molta acqua. (Drink lots of water -
        formal.) Si senta meglio presto! (Get well soon!) Respira
        profondamente. (Breathe deeply.) Non e niente di grave. (It is nothing
        serious.) Body words learned along the way: la testa (head),
        l'occhio (eye), il naso (nose), la bocca (mouth), il dente (tooth),
        il cuore (heart), la mano (hand), il braccio (arm), la gamba (leg),
        il piede (foot), la schiena (back), il sangue (blood)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches health by the symptom-report method: the learner
        practices the two pain frames - Mi fa male + singular, Mi fanno male
        + plural - on every body part, then role-plays the doctor visit: Ho
        la febbre, Devo vedere un medico, Prendo questa medicina. The pharmacy
        exchange is drilled as a complete script from Dov'e la farmacia to
        Mi serve una ricetta?"""),
    key_points=[
        "Pain frames: Mi fa male la testa (singular), Mi fanno male i piedi (plural).",
        "Ho la febbre, Ho il raffreddore, Ho la tosse - the symptom set.",
        "Doctor script: Devo vedere un medico, Ho un appuntamento dal dottore.",
        "Pharmacy script: Dov'e la farmacia, Ha qualcosa per..., Mi serve una ricetta?",
        "12 body parts: testa, occhio, naso, bocca, cuore, mano, braccio, gamba, piede.",
    ],
    requirements=[
        "Learners should drill the pain frames on all 12 body parts.",
        "Role-play the full doctor visit and pharmacy exchange.",
    ],
    standards=[
        "Standard Italian medical vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, the body is the vessel that "
              "carries the seal, and health the condition of the signature. "
              "This Signature reading treats each symptom reported as a "
              "status clause of the living contract."),
)


E(
    key="italian_emotions", name="Italian Emotions and Feelings Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for happiness, sadness, anger, fear, love, and
        surprise - the emotional vocabulary of real conversation. Sono molto
        felice oggi! (I am very happy today!) Che bella notizia! (What great
        news!) Rido sempre con te. (I always laugh with you.) Sono triste
        perche piove. (I am sad because it is raining.) Mi manchi tanto. (I
        miss you so much - you are missing to me.) Ho il cuore spezzato. (My
        heart is broken.) Sono arrabbiato con mio fratello. (I am angry with
        my brother.) Mi fa arrabbiare quando mente. (It makes me angry when he
        lies.) Calmati, respira! (Calm down, breathe!) Ho paura del buio. (I
        am afraid of the dark.) Non aver paura, sono qui. (Do not be afraid,
        I am here.) Ti amo piu di ieri. (I love you more than yesterday.)
        L'amore e la cosa piu bella. (Love is the most beautiful thing.)
        Sono innamorato di te. (I am in love with you.) Che sorpresa
        vederti qui! (What a surprise to see you here!) Non ci posso credere!
        (I cannot believe it!) Sono sorpreso e felice. (I am surprised and
        happy.) Sono nervoso prima dell'esame. (I am nervous before the
        exam.) Stai tranquillo, andra tutto bene. (Stay calm, everything will
        be fine.) Emotion words learned along the way: la gioia (joy), la
        tristezza (sadness), la rabbia (anger), la paura (fear), l'amore
        (love), la sorpresa (surprise), la speranza (hope)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches emotions by the feeling-journal method: the
        learner keeps a one-week diary writing one true sentence per day
        about how they feel - Sono felice perche..., Sono nervoso prima di...
        - using the frames given. Mi manchi (you are missing to me) is drilled
        as the signature Italian emotion construction, and the six emotion
        nouns are learned with their adjectives."""),
    key_points=[
        "20 sentences across six emotions: happy, sad, angry, afraid, love, surprise.",
        "Mi manchi - the missing-to-me construction, pure Italian.",
        "Essere + adjective for states: Sono felice, Sono nervoso, Sono innamorato.",
        "Avere + noun for feelings: Ho paura, Ho il cuore spezzato.",
        "Keep a one-week feeling journal in Italian.",
    ],
    requirements=[
        "Learners should write one true feeling sentence per day for a week.",
        "Drill Mi manchi / Ti amo / Non aver paura until they feel natural.",
    ],
    standards=[
        "Standard Italian emotional vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, emotions are the ink of the "
              "contract - joy the gold seal, love the binding signature. "
              "This Signature reading treats each feeling named as a clause "
              "written in the heart's own hand."),
)


E(
    key="italian_nature_weather", name="Italian Nature and Weather Sentences",
    group="Themed sentences", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for animals, plants, seasons, and weather talk -
        Italy's favorite small talk. Che bel tempo oggi! (What beautiful
        weather today!) C'e il sole. (It is sunny.) Piove a catinelle. (It is
        raining buckets.) Nevica sulle montagne. (It is snowing on the
        mountains.) Fa caldo d'estate. (It is hot in summer.) Fa freddo
        d'inverno. (It is cold in winter.) Tira vento al mare. (It is windy
        at the seaside.) Il cielo e nuvoloso. (The sky is cloudy.) Domani
        piovera. (It will rain tomorrow.) In primavera fioriscono gli alberi.
        (In spring the trees bloom.) Le foglie cadono in autunno. (The leaves
        fall in autumn.) Il cane abbaia in giardino. (The dog barks in the
        garden.) Il gatto dorme al sole. (The cat sleeps in the sun.) Gli
        uccelli cantano la mattina. (The birds sing in the morning.) Ho visto
        un cervo nel bosco. (I saw a deer in the woods.) Le api fanno il
        miele. (Bees make honey.) Il fiume scorre verso il mare. (The river
        flows to the sea.) La montagna e coperta di neve. (The mountain is
        covered with snow.) Andiamo al mare domenica? (Shall we go to the
        seaside Sunday?) Che stagione preferisci? (Which season do you
        prefer?) Nature words learned along the way: l'albero (tree), il
        fiore (flower), l'erba (grass), il bosco (woods), il lago (lake), il
        mare (sea), la spiaggia (beach), la stella (star), la luna (moon)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nature by the window method: the learner looks
        out the window and describes the real weather in Italian - C'e il
        sole, Piove, Fa freddo - then walks outside naming five natural
        things. Weather verbs are drilled as impersonals (piove, nevica, fa
        caldo), and the seasons are learned with what happens in each: In
        primavera fioriscono gli alberi."""),
    key_points=[
        "Weather impersonals: piove, nevica, fa caldo, fa freddo, c'e il sole, tira vento.",
        "Season sentences: In primavera fioriscono, Le foglie cadono in autunno.",
        "Animals in action: Il cane abbaia, Gli uccelli cantano, Le api fanno il miele.",
        "9 nature nouns: albero, fiore, erba, bosco, lago, mare, spiaggia, stella, luna.",
        "Describe the real weather outside your window in Italian daily.",
    ],
    requirements=[
        "Learners should describe the actual weather in Italian every morning.",
        "Name five natural things on a real walk, in full sentences.",
    ],
    standards=[
        "Standard Italian nature vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, nature is the contract's great "
              "witness - the sun that watches the signing, the seasons that "
              "date every page. This Signature reading treats each weather "
              "sentence as a timestamp on the seal."),
)


E(
    key="italian_shopping", name="Italian Shopping and Money Sentences",
    group="Themed sentences", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the market, prices, bargaining, and paying.
        Quanto costa? (How much does it cost?) Costa dieci euro. (It costs ten
        euros.) E troppo caro. (It is too expensive.) Puo farmi uno sconto?
        (Can you give me a discount?) Solo per lei, otto euro. (Just for you,
        eight euros.) Lo prendo. (I will take it.) Non lo prendo, grazie. (I
        will not take it, thanks.) Sto solo guardando. (I am just looking.)
        Ha una taglia piu grande? (Do you have a bigger size?) Posso
        provarlo? (May I try it on?) Dov'e il camerino? (Where is the fitting
        room?) Accettate carte di credito? (Do you accept credit cards?) Pago
        in contanti. (I pay cash.) Mi dia lo scontrino, per favore. (Give me
        the receipt, please.) Il mercato e aperto la mattina. (The market is
        open in the morning.) Compro frutta e verdura fresca. (I buy fresh
        fruit and vegetables.) Un chilo di mele, per favore. (A kilo of
        apples, please.) Il pane e ancora caldo. (The bread is still warm.)
        A che ora chiude il negozio? (What time does the shop close?) Grazie
        e arrivederci! (Thanks and goodbye!) Money words learned along the
        way: i soldi (money), il prezzo (price), lo sconto (discount), la
        moneta (coin), la banconota (banknote), il resto (change), gratis
        (free)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches shopping by the market-stall method: the learner
        role-plays buyer and seller, haggling over real or imagined goods -
        Quanto costa? E troppo caro. Puo farmi uno sconto? Lo prendo. - until
        the bargaining script flows. Prices are drilled with real euro amounts,
        and the fitting-room and payment exchanges are rehearsed as complete
        scripts."""),
    key_points=[
        "Price core: Quanto costa? Costa dieci euro. E troppo caro.",
        "Bargaining script: Puo farmi uno sconto? Solo per lei, otto euro. Lo prendo.",
        "Clothing: Ha una taglia piu grande? Posso provarlo? Dov'e il camerino?",
        "Payment: Accettate carte di credito? Pago in contanti. Lo scontrino.",
        "Market weights: Un chilo di mele - buy by the kilo like an Italian.",
    ],
    requirements=[
        "Learners should role-play buyer and seller until bargaining flows.",
        "Practice prices with real euro amounts, not just round numbers.",
    ],
    standards=[
        "Standard Italian commercial vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, the market is the contract's "
              "exchange floor - every price a term negotiated, every sconto a "
              "clause amended. This Signature reading treats the handshake "
              "deal as the seal pressed in person."),
)


E(
    key="italian_friendship", name="Italian Friendship and Social Life Sentences",
    group="Themed sentences", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for meeting people, invitations, and celebrations.
        Piacere, mi chiamo Sara. (Nice to meet you, I am called Sara.) Di
        dove sei? (Where are you from?) Sono di Napoli, e tu? (I am from
        Naples, and you?) Quanti anni hai? (How old are you?) Ho trent'anni.
        (I am thirty.) Che fai nella vita? (What do you do in life?) Ti
        presento il mio amico Luca. (Let me introduce my friend Luca.)
        Andiamo a prendere un caffe? (Shall we go get a coffee?) Volentieri!
        (Gladly!) Che ne dici di cena sabato? (How about dinner Saturday?)
        Vieni alla mia festa venerdi? (Are you coming to my party Friday?)
        Porta pure un amico. (Feel free to bring a friend.) A che ora
        cominciamo? (What time do we start?) Ci vediamo alle otto. (See you
        at eight.) Mi fa piacere vederti! (I am pleased to see you!) E tanto
        che non ci vediamo! (It has been so long!) Raccontami tutto! (Tell me
        everything!) Auguri per il tuo compleanno! (Happy birthday wishes!)
        Congratulazioni per il lavoro nuovo! (Congratulations on the new job!)
        E stata una bellissima serata. (It was a wonderful evening.)
        Torniamo a casa contenti. (We go home happy.) Social words learned
        along the way: l'invito (invitation), la festa (party), il regalo
        (gift), il brindisi (toast), gli auguri (wishes), l'amicizia
        (friendship)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches friendship by the introduction method: the learner
        rehearses the full meeting script - Piacere, Di dove sei, Quanti anni
        hai, Che fai nella vita - with real answers about themselves, then
        practices inviting and accepting: Vieni alla mia festa? Volentieri!
        The celebration sentences are learned attached to real occasions in
        the learner's life."""),
    key_points=[
        "Meeting script: Piacere, Di dove sei, Quanti anni hai, Che fai nella vita.",
        "Invitation pair: Vieni alla festa? / Volentieri! - Porta pure un amico.",
        "Celebration formulas: Auguri, Congratulazioni, E stata una bellissima serata.",
        "Coffee is the social contract: Andiamo a prendere un caffe?",
        "Answer every question with true facts about yourself.",
    ],
    requirements=[
        "Learners should rehearse the meeting script with true personal answers.",
        "Practice inviting and accepting until the exchange feels like a real plan.",
    ],
    standards=[
        "Standard Italian social vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, friendship is the contract's "
              "human counterpart - every introduction a new party joined, "
              "every coffee a small covenant renewed. This Signature reading "
              "treats the toast as the seal raised high."),
)


E(
    key="italian_technology", name="Italian Technology and Communication Sentences",
    group="Themed sentences", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the phone, the internet, the computer, and
        messaging - modern Italian life. Il mio telefono e scarico. (My phone
        is dead - discharged.) Dov'e il caricabatterie? (Where is the
        charger?) Non c'e campo qui. (There is no signal here.) Ti chiamo piu
        tardi. (I will call you later.) Pronto? Chi parla? (Hello? Who is
        speaking?) Resta in linea, per favore. (Hold the line, please.) Mi e
        caduta la linea. (The call dropped.) Ti mando un messaggio. (I will
        send you a message.) Hai visto la mia email? (Did you see my email?)
        La password non funziona. (The password does not work.) Ho dimenticato
        la password. (I forgot the password.) Il computer si e bloccato.
        (The computer froze.) Riavvia il computer. (Restart the computer.)
        C'e il wifi qui? (Is there wifi here?) Qual e la password del wifi?
        (What is the wifi password?) Scarico l'app adesso. (I am downloading
        the app now.) Ho finito i giga. (I am out of data.) Faccio una foto e
        te la mando. (I will take a photo and send it to you.) Ci sentiamo
        domani! (We will talk tomorrow!) Tech words learned along the way: lo
        schermo (screen), la tastiera (keyboard), il mouse (mouse), la
        stampante (printer), il file (file), la cartella (folder), il sito
        (website), il collegamento (link), i social (social media)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches technology by the troubleshooting method: the
        learner narrates real tech problems in Italian as they happen - Il
        computer si e bloccato, Non c'e campo qui, Ho dimenticato la password
        - and solves them with the fix sentences. The phone-call script
        (Pronto? Chi parla? Resta in linea) is drilled until it can be
        performed on a real call."""),
    key_points=[
        "Phone script: Pronto? Chi parla? Resta in linea. Mi e caduta la linea.",
        "Problem frames: Il computer si e bloccato. Non c'e campo qui. Ho finito i giga.",
        "Fix commands: Riavvia il computer. Ti chiamo piu tardi. Ti mando un messaggio.",
        "9 tech nouns: schermo, tastiera, mouse, stampante, file, cartella, sito, collegamento.",
        "Narrate your real tech problems in Italian as they happen.",
    ],
    requirements=[
        "Learners should describe one real tech problem in Italian each day.",
        "Drill the phone-call script until it works on a live call.",
    ],
    standards=[
        "Standard Italian technology vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, technology is the contract's "
              "modern courier - every message a sealed letter, every call a "
              "voice across the distance. This Signature reading treats the "
              "signal as the oath traveling by wire."),
)


E(
    key="italian_tenses", name="Italian Verb Tenses in Sentences",
    group="Grammar", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        The Italian verb tenses in sentences - present, past, and future,
        with the moods that color them. PRESENTE (present): Parlo italiano.
        (I speak Italian.) Mangiamo la pizza. (We eat pizza.) Lavori domani?
        (Are you working tomorrow? - present for near future.) Abito a Roma.
        (I live in Rome.) PASSATO PROSSIMO (recent past, with avere/essere):
        Ho mangiato la pizza. (I ate the pizza.) Abbiamo visto un film. (We
        watched a movie.) Sono andato a scuola. (I went to school - masculine
        I.) Sono andata a scuola. (I went to school - feminine I.) Sei mai
        stato a Venezia? (Have you ever been to Venice?) IMPERFETTO
        (ongoing past): Quando ero bambino, giocavo in strada. (When I was a
        child, I used to play in the street.) Pioveva e faceva freddo. (It
        was raining and it was cold.) Da giovane leggevo molto. (As a young
        person I read a lot.) PASSATO REMOTO (literary past): Nacque a Firenze
        nel 1265. (He was born in Florence in 1265.) Dante scrisse la Divina
        Commedia. (Dante wrote the Divine Comedy.) FUTURO (future): Domani
        piovera. (Tomorrow it will rain.) Verro alle otto. (I will come at
        eight.) Avremo una bella festa. (We will have a great party.)
        CONDIZIONALE (would): Vorrei un caffe. (I would like a coffee.)
        Potresti aiutarmi? (Could you help me?) Mi piacerebbe visitare Roma.
        (I would love to visit Rome.) CONGIUNTIVO (subjunctive, after che for
        wishes/doubt): Voglio che tu venga. (I want you to come.) Spero che
        piova. (I hope it rains - ironic.) E importante che studi. (It is
        important that you study.) The rule of thumb: passato prossimo for
        what happened, imperfetto for how things were, futuro for what will
        be, condizionale for what would be, congiuntivo after che for wishes
        and doubt."""),
    how_it_works=textwrap.dedent("""\
        This record teaches tenses by the timeline method: the learner tells
        one life story three times - yesterday (passato prossimo), as a child
        (imperfetto), tomorrow (futuro) - feeling the tense shift the whole
        narrative. Essere vs avere in the past is drilled with the motion
        verbs (andare, venire, partire take essere). The congiuntivo is
        introduced only through the Voglio che / Spero che frames."""),
    key_points=[
        "Presente: Parlo italiano. Also covers near future: Lavori domani?",
        "Passato prossimo: Ho mangiato / Sono andato - avere vs essere.",
        "Imperfetto: Giocavo, Pioveva - ongoing past, how things were.",
        "Futuro: Piovera, Verro. Condizionale: Vorrei, Potresti.",
        "Congiuntivo after che for wishes/doubt: Voglio che tu venga.",
    ],
    requirements=[
        "Learners should tell one story in three tenses: yesterday, childhood, tomorrow.",
        "Drill essere vs avere past with motion verbs until automatic.",
    ],
    standards=[
        "Standard Italian verb tenses per the Accademia della Crusca.",
    ],
    citations=[
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, tenses are the contract's "
              "timeline - the past its executed clauses, the future its "
              "promises, the conditional its terms under discussion. This "
              "Signature reading treats each tense as a dated seal."),
)


E(
    key="italian_qa", name="Italian Questions and Answers",
    group="Grammar", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty question-and-answer pairs covering who, what, where, when,
        why, and how - the interrogation engine of conversation. Chi e?
        E mio fratello. (Who is it? It is my brother.) Che cos'e? E un
        regalo. (What is it? It is a gift.) Cosa fai? Studio italiano. (What
        are you doing? I am studying Italian.) Dove abiti? Abito a Torino.
        (Where do you live? I live in Turin.) Di dove sei? Sono siciliano.
        (Where are you from? I am Sicilian.) Quando parti? Parto lunedi.
        (When do you leave? I leave Monday.) A che ora? Alle sette. (At what
        time? At seven.) Perche piangi? Perche sono triste. (Why are you
        crying? Because I am sad.) Come stai? Bene, grazie. (How are you?
        Well, thanks.) Come si fa? Si fa cosi. (How is it done? It is done
        like this.) Quale preferisci? Preferisco il rosso. (Which do you
        prefer? I prefer the red one.) Quanti anni hai? Ne ho venti. (How old
        are you? I am twenty.) Quanto costa? Costa cinque euro. (How much?
        Five euros.) Quanto tempo ci vuole? Un'ora circa. (How long does it
        take? About an hour.) C'e un problema? No, tutto bene. (Is there a
        problem? No, all good.) Parli italiano? Si, un po'. (Do you speak
        Italian? Yes, a little.) Hai capito? Si, ho capito. (Did you
        understand? Yes, I understood.) Vuoi un caffe? Si, grazie! (Do you
        want a coffee? Yes, thanks!) Andiamo? Andiamo! (Shall we go? Let us
        go!) The question words: chi (who), che/cosa (what), dove (where),
        quando (when), perche (why/because), come (how), quale (which),
        quanto (how much/how many). Answers stay short - Italians answer
        questions directly, then add detail."""),
    how_it_works=textwrap.dedent("""\
        This record teaches questions by the pair-drill method: each of the 20
        pairs is practiced as a rapid exchange, the learner playing both
        parts, then answering with true personal facts - Dove abiti? with
        their real city, Quanti anni hai? with their real age. The eight
        question words are drilled as a set, then each is used to interview a
        partner for two minutes."""),
    key_points=[
        "20 Q&A pairs: chi, che, cosa, dove, quando, perche, come, quale, quanto.",
        "Che/cosa for what; quale for which (choice); quanto for how much/many.",
        "Perche means both why and because - the question carries its answer.",
        "Answers stay short and direct, then add detail.",
        "Interview a partner for two minutes using only the question words.",
    ],
    requirements=[
        "Learners should answer every pair with true personal facts.",
        "Drill the 8 question words as a set until each triggers instantly.",
    ],
    standards=[
        "Standard Italian interrogatives per the Accademia della Crusca.",
    ],
    citations=[
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, questions are the contract's "
              "due diligence - every chi and perche a clause examined before "
              "signing. This Signature reading treats each answer as a "
              "sworn statement."),
)


E(
    key="italian_commands", name="Italian Commands and Requests",
    group="Themed sentences", ladder_rank=10, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty imperatives and polite requests - telling, asking, and
        inviting, formal and informal. Informal (tu): Parla piu forte! (Speak
        louder!) Mangia tutto! (Eat everything!) Vieni qui! (Come here!)
        Dimmi la verita. (Tell me the truth.) Apri la finestra. (Open the
        window.) Chiudi la porta. (Close the door.) Sbrigati! (Hurry up!)
        Sta' zitto! (Be quiet!) - note sta' with apostrophe. Formal (Lei):
        Parli piu forte, per favore. (Speak louder, please.) Mi dica. (Tell
        me.) Venga qui. (Come here.) Si accomodi. (Make yourself comfortable /
        have a seat.) Mi scusi. (Excuse me.) Plural/let us (noi): Andiamo!
        (Let us go!) Mangiamo insieme. (Let us eat together.) Plural you
        (voi): Parlate piano. (Speak quietly - you all.) Venite domani.
        (Come tomorrow - you all.) Polite requests: Per favore... (Please...);
        Potresti...? (Could you...?); Può...? (Can you...? - formal); Mi
        faresti un favore? (Would you do me a favor?); Le dispiace...? (Do
        you mind...? - formal); Vorrei... (I would like...). Softened with
        the conditional: Vorrei prenotare un tavolo. (I would like to book a
        table.) Potrebbe ripetere? (Could you repeat? - formal.) Example
        progressions: Chiudi la porta (informal order) -> Puoi chiudere la
        porta? (request) -> Potrebbe chiudere la porta, per favore? (formal
        polite request) -> Le dispiace chiudere la porta? (very polite)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches commands by the register ladder: the learner
        takes one action - close the door - and climbs from blunt informal
        (Chiudi!) through request (Puoi chiudere?) to formal polite
        (Potrebbe chiudere, per favore?). Each of the 20 sentences is
        performed as a real command in a real situation, and the tu/Lei/noi
        forms are drilled as a three-step set on five verbs."""),
    key_points=[
        "Tu imperatives: Parla! Mangia! Vieni! Dimmi! - direct and informal.",
        "Lei imperatives: Parli! Mi dica! Venga! - formal, third-person form.",
        "Noi: Andiamo! Mangiamo! - let us. Voi: Parlate! Venite! - you all.",
        "Polite ladder: Chiudi -> Puoi chiudere? -> Potrebbe chiudere, per favore?",
        "Softeners: Vorrei, Potresti, Mi faresti un favore, Le dispiace.",
    ],
    requirements=[
        "Learners should climb the politeness ladder on five real actions.",
        "Perform each command in a real situation, not just from the page.",
    ],
    standards=[
        "Standard Italian imperative and polite forms per the Accademia della Crusca.",
    ],
    citations=[
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, commands are the contract's "
              "orders and requests its motions - each imperative a directive "
              "sealed, each per favore a motion filed with courtesy. This "
              "Signature reading treats the politeness ladder as the "
              "contract's chain of command."),
)


E(
    key="italian_descriptions", name="Italian Descriptions of People and Places",
    group="Themed sentences", ladder_rank=10, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences describing people, places, and things in detail -
        the painter's vocabulary. Mia nonna ha i capelli bianchi e gli occhi
        azzurri. (My grandmother has white hair and blue eyes.) E alta e
        magra, sempre elegante. (She is tall and slim, always elegant.) Marco
        e un ragazzo allegro e generoso. (Marco is a cheerful, generous boy.)
        Ha trent'anni e lavora come medico. (He is thirty and works as a
        doctor.) La mia citta e antica e piena di storia. (My city is ancient
        and full of history.) Le strade sono strette e lastricate. (The
        streets are narrow and cobbled.) La piazza e grande e luminosa. (The
        square is big and bright.) C'e una fontana al centro. (There is a
        fountain in the center.) Il Duomo e una chiesa magnifica. (The
        cathedral is a magnificent church.) Il mare e calmo e cristallino.
        (The sea is calm and crystal-clear.) La montagna e alta e coperta di
        neve. (The mountain is tall and covered with snow.) Il tramonto e
        rosso e oro. (The sunset is red and gold.) La casa di campagna e
        circondata da ulivi. (The country house is surrounded by olive
        trees.) Il giardino e pieno di fiori profumati. (The garden is full
        of fragrant flowers.) Il caffe e piccolo ma accogliente. (The cafe is
        small but cozy.) Il cibo e semplice e genuino. (The food is simple and
        genuine.) La gente e cordiale e ospitale. (The people are warm and
        hospitable.) L'atmosfera e magica di sera. (The atmosphere is magical
        at night.) Non dimentichero mai questo posto. (I will never forget
        this place.) Tornero sicuramente. (I will surely return.) Describing
        people: alto/basso (tall/short), magro/grasso (slim/heavy), giovane/
        anziano (young/elderly), biondo/moro (blond/dark-haired), simpatico/
        antipatico (likeable/unlikeable)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description by the portrait method: the learner
        describes one real person and one real place using the sentence
        frames, filling every frame with true detail - Mia nonna ha... with
        their own grandmother's features, La mia citta e... with their own
        city's streets. Each description is built in layers: appearance,
        character, then feeling - so the 20 sentences become a template for
        describing anything."""),
    key_points=[
        "People: appearance (capelli, occhi, alto, magro), age, character (allegro, generoso).",
        "Places: streets, squares, churches, sea, mountains - built in layers.",
        "Agreement everywhere: strade strette, fiori profumati, gente cordiale.",
        "Closing feelings: Non dimentichero mai, Tornero sicuramente.",
        "Describe one real person and one real place with true detail.",
    ],
    requirements=[
        "Learners should write a full portrait of a real person in Italian.",
        "Learners should write a full portrait of a real place in Italian.",
    ],
    standards=[
        "Standard Italian descriptive vocabulary per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, description is the contract's "
              "exhibit A - every detail entered into evidence, every portrait "
              "a sworn likeness. This Signature reading treats each "
              "description as an attachment to the seal."),
)


E(
    key="italian_story1", name="Italian Story I: A New Morning",
    group="Stories", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence simple story in Italian, line by line in English -
        the present tense at work. 1. Mi chiamo Elena e abito a Firenze.
        (My name is Elena and I live in Florence.) 2. Ogni mattina mi sveglio
        alle sette. (Every morning I wake up at seven.) 3. Faccio colazione
        con caffe e biscotti. (I have breakfast with coffee and biscuits.)
        4. Poi esco e cammino fino al lavoro. (Then I go out and walk to
        work.) 5. Lavoro in una piccola libreria in centro. (I work in a
        small bookstore downtown.) 6. Amo i libri e amo la mia citta. (I love
        books and I love my city.) 7. A mezzogiorno mangio un panino al
        parco. (At noon I eat a sandwich in the park.) 8. Il pomeriggio passa
        veloce tra i clienti. (The afternoon passes quickly among the
        customers.) 9. La sera torno a casa stanca ma felice. (In the evening
        I return home tired but happy.) 10. Domani sara un altro bel giorno.
        (Tomorrow will be another beautiful day.) The story uses only present
        tense and the vocabulary of records 1-20: greetings, home, food,
        work, time. Read it aloud three times: first slowly for pronunciation,
        second for meaning, third at speaking speed - then retell it without
        looking, changing Elena to yourself."""),
    how_it_works=textwrap.dedent("""\
        This record teaches narrative by the retelling method: the learner
        reads the ten lines with their translations, then closes the page and
        retells Elena's morning in their own words - first as Elena, then as
        themselves (Mi chiamo... e abito a...). Every verb is present tense,
        so the story proves the learner can already narrate a day."""),
    key_points=[
        "10-sentence story, present tense only, line-by-line translation.",
        "Uses only vocabulary from records 1-20 - nothing new to decode.",
        "Reflexive verbs in action: mi chiamo, mi sveglio.",
        "Read three times: pronunciation, meaning, speed - then retell.",
        "Retell as yourself: change Elena to your own name and city.",
    ],
    requirements=[
        "Learners should retell the story aloud without looking.",
        "Rewrite the story as your own morning, keeping all ten frames.",
    ],
    standards=[
        "Standard Italian narrative prose per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, the story is the contract's "
              "first executed chapter - a day lived and signed in the present "
              "tense. This Signature reading treats Elena's morning as the "
              "oath performed daily."),
)


E(
    key="italian_story2", name="Italian Story II: The Journey",
    group="Stories", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the past tenses, line by line in English.
        1. L'estate scorsa ho fatto un viaggio in Sicilia. (Last summer I
        took a trip to Sicily.) 2. Sono partito da Milano in treno. (I left
        from Milan by train - masculine I.) 3. Il viaggio e durato tutta la
        notte. (The journey lasted all night.) 4. Quando ero bambino, sognavo
        il mare. (When I was a child, I dreamed of the sea - imperfetto for
        the ongoing past.) 5. Finalmente ho visto l'acqua blu. (Finally I saw
        the blue water.) 6. Ho mangiato arancini e cannoli ogni giorno. (I
        ate arancini and cannoli every day.) 7. Un giorno pioveva, ma non mi
        importava. (One day it was raining, but I did not mind.) 8. Ho
        conosciuto una famiglia gentile a Taormina. (I met a kind family in
        Taormina.) 9. Mi hanno invitato a cena tre volte! (They invited me to
        dinner three times!) 10. Non dimentichero mai quella settimana.
        (I will never forget that week.) The story contrasts passato prossimo
        (ho fatto, ho visto - what happened) with imperfetto (sognavo,
        pioveva - how things were). Notice sono partito with essere for
        motion, and mi hanno invitato with avere. Retell it as your own past
        trip, keeping the tense contrast."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the past by the contrast method: the learner marks
        every passato prossimo verb (completed events) and every imperfetto
        verb (background, ongoing states) in two colors, then retells the
        journey as their own real trip - L'estate scorsa ho... - keeping the
        same contrast. Essere-motion verbs (sono partito) get special drill."""),
    key_points=[
        "10-sentence story, past tenses, line-by-line translation.",
        "Passato prossimo vs imperfetto: ho visto vs sognavo, ha mangiato vs pioveva.",
        "Essere for motion: sono partito. Avere for the rest: ho mangiato.",
        "Mark the two pasts in colors, then retell as your own trip.",
        "Ends with a future seal: Non dimentichero mai.",
    ],
    requirements=[
        "Learners should color-mark passato prossimo vs imperfetto in the story.",
        "Retell the journey as a real trip from your own life.",
    ],
    standards=[
        "Standard Italian past tenses per the Accademia della Crusca.",
    ],
    citations=[
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, the past-tense story is the "
              "contract's executed history - every ho fatto a clause "
              "fulfilled, every imperfetto the standing conditions. This "
              "Signature reading treats the journey as the seal's travels."),
)


E(
    key="italian_story3", name="Italian Story III: Tomorrow's Promise",
    group="Stories", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the future and conditional, line by line in
        English. 1. Domani comincera una nuova avventura. (Tomorrow a new
        adventure will begin.) 2. Partiro per Roma all'alba. (I will leave
        for Rome at dawn.) 3. Vedro il Colosseo e i Fori. (I will see the
        Colosseum and the Forums.) 4. Vorrei anche visitare il Vaticano. (I
        would also like to visit the Vatican.) 5. Mi piacerebbe mangiare la
        vera carbonara. (I would love to eat the real carbonara.) 6. Se avro
        tempo, andro a Trastevere. (If I have time, I will go to Trastevere.)
        7. Comprero regali per tutta la famiglia. (I will buy gifts for the
        whole family.) 8. Spero che il tempo sia bello. (I hope the weather
        is nice - congiuntivo after spero che.) 9. Voglio che tu venga con me
        un giorno. (I want you to come with me one day - congiuntivo after
        voglio che.) 10. Sara il viaggio piu bello della mia vita. (It will
        be the most beautiful trip of my life.) The story shows futuro
        (partiro, vedro, comprero), condizionale (vorrei, mi piacerebbe),
        and congiuntivo after che (sia, venga). Write your own tomorrow
        story with five futures, two conditionals, and one spero che."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the future by the promise method: the learner
        writes their own ten-sentence tomorrow story - five future verbs,
        two conditionals, one spero che + congiuntivo - planning a real
        upcoming day or trip. The story's pattern (futuro plans, condizionale
        wishes, congiuntivo hopes) becomes the template for talking about any
        future."""),
    key_points=[
        "10-sentence story: futuro, condizionale, congiuntivo, line by line.",
        "Futuro: partiro, vedro, comprero, sara - plans stated as facts.",
        "Condizionale: vorrei, mi piacerebbe - wishes and polite desires.",
        "Congiuntivo: spero che sia, voglio che venga - hopes after che.",
        "Write your own tomorrow story: 5 futures, 2 conditionals, 1 spero che.",
    ],
    requirements=[
        "Learners should write a ten-sentence tomorrow story with the required forms.",
        "Read the story aloud, stressing the future endings.",
    ],
    standards=[
        "Standard Italian future, conditional, and subjunctive per the Accademia della Crusca.",
    ],
    citations=[
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, the future-tense story is the "
              "contract's promises section - every partiro a commitment, "
              "every vorrei a term under discussion. This Signature reading "
              "treats tomorrow's promise as the seal set on what is to come."),
)


E(
    key="italian_idioms", name="Italian Idioms and Proverbs",
    group="Register and style", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty idioms and proverbs - literal translation, real meaning, and
        example sentence each. 1. In bocca al lupo! - Into the wolf's mouth!
        = Good luck! (theater/school/exams). Domani ho l'esame: in bocca al
        lupo! 2. Non tutte le ciambelle riescono col buco. - Not all donuts
        come out with a hole. = Things do not always work out. 3. Avere le
        mani in pasta. - To have hands in the dough. = To be involved in
        something. Ha le mani in pasta in ogni progetto. 4. Prendere due
        piccioni con una fava. - To take two pigeons with one bean. = To kill
        two birds with one stone. 5. Chi dorme non piglia pesci. - Who sleeps
        catches no fish. = The early bird catches the worm. 6. L'abito non fa
        il monaco. - The habit does not make the monk. = Clothes do not make
        the man. 7. Meglio tardi che mai. - Better late than never. 8. Tutto
        fumo e niente arrosto. - All smoke and no roast. = All talk, no
        substance. 9. Acqua in bocca! - Water in the mouth! = Keep it secret!
        10. Piove a catinelle. - It rains in basins. = It is pouring. 11.
        Essere al settimo cielo. - To be in the seventh heaven. = To be
        overjoyed. 12. Mettere la pulce nell'orecchio. - To put the flea in
        the ear. = To plant a suspicion. 13. Fare il diavolo a quattro. - To
        make the devil in four. = To raise hell / make a ruckus. 14. Dormire
        come un ghiro. - To sleep like a dormouse. = To sleep deeply. 15. Non
        avere peli sulla lingua. - To have no hairs on the tongue. = To speak
        bluntly. 16. Costare un occhio della testa. - To cost an eye of the
        head. = To cost a fortune. 17. Chi trova un amico trova un tesoro. -
        Who finds a friend finds a treasure. 18. Tra il dire e il fare c'e di
        mezzo il mare. - Between saying and doing there is the sea. = Easier
        said than done. 19. La gatta frettolosa fece i gattini ciechi. - The
        hasty cat made blind kittens. = Haste makes waste. 20. Rosso di sera,
        bel tempo si spera. - Red in the evening, good weather is hoped. =
        Red sky at night, shepherd's delight. Use one idiom per day in real
        speech until all twenty are yours."""),
    how_it_works=textwrap.dedent("""\
        This record teaches idioms by the one-a-day method: the learner takes
        one idiom, learns its literal image (the wolf's mouth, the flea in
        the ear), its real meaning, and its example sentence, then uses it in
        real speech that day. The literal translations are never skipped -
        the image is what makes the idiom stick. After twenty days, the
        learner owns all twenty."""),
    key_points=[
        "20 idioms/proverbs: literal image + real meaning + example sentence.",
        "In bocca al lupo / Crepi - the good-luck ritual.",
        "Food-born idioms: mani in pasta, due piccioni con una fava, fumo e niente arrosto.",
        "Wisdom proverbs: Chi dorme non piglia pesci, Tra il dire e il fare c'e il mare.",
        "Use one idiom per day in real speech for twenty days.",
    ],
    requirements=[
        "Learners should use one new idiom in real speech each day.",
        "Always learn the literal image first - it anchors the meaning.",
    ],
    standards=[
        "Standard Italian idiomatic usage per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, idioms are the contract's "
              "sealed proverbs - centuries of witnesses condensed into one "
              "signed line. This Signature reading treats each idiom as a "
              "precedent cited in the margin."),
)


E(
    key="italian_registers", name="Italian Formal and Polite Registers",
    group="Register and style", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen formal vs informal pairs - letters, business, and elders,
        each pair translated. 1. Ciao, come stai? / Buongiorno, come sta? -
        Hi, how are you? / Good morning, how are you? 2. Scusa il ritardo. /
        Mi scusi per il ritardo. - Sorry I am late. 3. Puoi aiutarmi? / Puo
        aiutarmi? or Potrebbe aiutarmi? - Can you help me? 4. Dammi il tuo
        numero. / Mi puo dare il suo numero? - Give me your number. 5. Vieni
        domani? / Puo venire domani? - Are you coming tomorrow? 6. Dimmi pure.
        / Mi dica pure. - Tell me. 7. Siediti qui. / Si accomodi qui. - Sit
        here. 8. Aspetta un attimo. / Attenda un momento, per favore. - Wait a
        moment. 9. Non ho capito. / Mi scusi, non ho capito bene. - I did not
        understand. 10. Quanto vuoi? / Quanto desidera? - How much do you
        want? 11. Ti ringrazio tanto. / La ringrazio molto. - Thank you very
        much. 12. Ci vediamo! / ArrivederLa! - See you! / Goodbye! 13. Ti
        scrivo presto. / Le scrivero al piu presto. - I will write soon. 14.
        Un bacio, Marco / Distinti saluti, Marco Rossi - A kiss, Marco /
        Kind regards, Marco Rossi (letter closings). 15. Tuo Marco / In attesa
        di una Sua risposta, porgo cordiali saluti - Yours, Marco / Awaiting
        your reply, kind regards (formal letter closing - Sua capitalized).
        Rules: Lei always takes the third-person verb; possessives and
        pronouns referring to Lei are capitalized in writing (La ringrazio,
        Sua risposta); in speech, use Lei with strangers over ~30, elders,
        officials, and in all business; switch to tu only when invited
        (Possiamo darci del tu? - Shall we use tu?). Never use Ciao with
        Lei-people - Buongiorno is the safe bridge."""),
    how_it_works=textwrap.dedent("""\
        This record teaches registers by the letter method: the learner
        writes two versions of one real message - a note to a friend (tu) and
        a note to a teacher or official (Lei) - using the pairs as models.
        The 15 pairs are drilled as transformations: take the informal, make
        it formal, checking verb person and capitalization. The golden rule is
        practiced as a reflex: when in doubt, Lei."""),
    key_points=[
        "15 formal/informal pairs: greetings, requests, closings.",
        "Lei takes third-person verbs; written Lei-forms capitalized: La ringrazio, Sua risposta.",
        "Use Lei with strangers, elders, officials, business - tu only when invited.",
        "Formal letter closing: In attesa di una Sua risposta, porgo cordiali saluti.",
        "When in doubt, Lei - it is never wrong to be polite.",
    ],
    requirements=[
        "Learners should write the same message twice: once tu, once Lei.",
        "Drill all 15 pairs as transformations until the formal form is instant.",
    ],
    standards=[
        "Standard Italian formal register per the Accademia della Crusca.",
    ],
    citations=[
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, register is the contract's "
              "protocol - tu for parties who have signed together, Lei for "
              "honored counterparts. This Signature reading treats each "
              "formal phrase as a bow before the seal is pressed."),
)


E(
    key="italian_complex", name="Italian Compound and Complex Sentences",
    group="Register and style", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen long sentences with clauses, connectors, and relative
        clauses - parsed and translated. 1. Quando sono arrivato, la cena era
        gia pronta. (When I arrived [time clause], dinner was already ready.)
        2. La donna che vedi e mia sorella. (The woman whom you see [relative
        clause] is my sister.) 3. Ti ho chiamato perche avevo bisogno di
        aiuto. (I called you because [cause] I needed help.) 4. Sebbene
        piovesse, siamo usciti lo stesso. (Although it was raining
        [concession], we went out anyway.) 5. Appena avro finito, ti
        telefonero. (As soon as I have finished [time], I will call you.) 6.
        Non so dove abbia messo le chiavi. (I do not know where I put
        [indirect question, congiuntivo] the keys.) 7. E importante che tu
        venga domani. (It is important that you come [congiuntivo] tomorrow.)
        8. Il libro di cui ti ho parlato e in libreria. (The book about which
        [di cui] I told you is in the bookstore.) 9. Lavorava mentre i bambini
        dormivano. (He worked while [time] the children were sleeping.) 10.
        Se avessi tempo, viaggerei di piu. (If I had time [hypothetical], I
        would travel more.) 11. Mi ha detto che sarebbe venuto. (He told me
        that he would come [reported future-in-past].) 12. Prima di uscire,
        spegni le luci. (Before going out [infinitive clause], turn off the
        lights.) 13. Pur essendo stanco, ha finito il lavoro. (Although
        being tired [gerund concession], he finished the work.) 14. Tanto piu
        studi, tanto piu impari. (The more you study [correlative], the more
        you learn.) 15. Nonostante la pioggia, la festa e stata un successo.
        (Despite the rain [prepositional], the party was a success.)
        Connectors learned: quando, che, perche, sebbene, appena, dove,
        prima di, mentre, se, pur, tanto...tanto, nonostante, di cui."""),
    how_it_works=textwrap.dedent("""\
        This record teaches complex sentences by the parsing method: the
        learner brackets each clause in the 15 sentences - [main] [time
        clause] [relative clause] - names the connector, and checks the verb
        mood in each bracket. Then the learner builds five original complex
        sentences by combining two simple sentences from earlier records with
        a connector: La cena era pronta + Sono arrivato = Quando sono
        arrivato, la cena era pronta."""),
    key_points=[
        "15 sentences parsed: time, cause, concession, relative, hypothetical clauses.",
        "Che/cui/di cui relatives: La donna che vedi; Il libro di cui ti ho parlato.",
        "Congiuntivo triggers: E importante che, Non so dove, sebbene.",
        "Se + imperfetto + condizionale: Se avessi tempo, viaggerei.",
        "Build complex sentences by joining two simple ones with a connector.",
    ],
    requirements=[
        "Learners should bracket and name every clause in all 15 sentences.",
        "Build five original complex sentences from earlier simple ones.",
    ],
    standards=[
        "Standard Italian complex syntax per the Accademia della Crusca.",
    ],
    citations=[
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, complex sentences are the "
              "contract's long articles - main clauses the terms, subordinate "
              "clauses the conditions and exceptions. This Signature reading "
              "treats each connector as the hinge between provisions."),
)


E(
    key="italian_dialogue_market", name="Italian Conversation at the Market",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue at the market, annotated. 1.
        Cliente: Buongiorno! (Good morning! - the required greeting.) 2.
        Venditore: Buongiorno! Desidera? (Good morning! What would you like?
        - desidera is the polite shop form.) 3. Cliente: Vorrei un chilo di
        mele, per favore. (I would like a kilo of apples, please - vorrei
        softens the request.) 4. Venditore: Subito. Altro? (Right away.
        Anything else?) 5. Cliente: Si, mezzo chilo di pomodori. Sono freschi?
        (Yes, half a kilo of tomatoes. Are they fresh?) 6. Venditore:
        Freschissimi, arrivati stamattina. (Very fresh, arrived this morning -
        -issimi is the absolute superlative.) 7. Cliente: Quanto costano?
        (How much are they?) 8. Venditore: Tre euro al chilo. (Three euros a
        kilo.) 9. Cliente: E le mele? (And the apples?) 10. Venditore: Due
        euro e cinquanta. (Two fifty.) 11. Cliente: Mi da anche un mazzo di
        basilico? (Will you give me a bunch of basil too? - mi da is the
        friendly request form.) 12. Venditore: Certo, glielo regalo. (Of
        course, it is a gift - glielo = to you + it.) 13. Cliente: Gentilissimo!
        Quanto le devo? (Very kind! How much do I owe you? - le devo keeps
        the formal register.) 14. Venditore: Quattro euro in tutto. (Four
        euros all together.) 15. Cliente: Ecco cinque euro. (Here is five
        euros.) 16. Venditore: Un euro di resto. (One euro change.) 17.
        Cliente: Mi mette tutto nel sacchetto? (Will you put it all in the
        bag?) 18. Venditore: Fatto. Buona giornata! (Done. Have a good day!)
        19. Cliente: Grazie, altrettanto! Arrivederci! (Thanks, same to you!
        Goodbye!) 20. Venditore: Arrivederci! (Goodbye!) Annotations teach:
        the greeting duty, vorrei vs voglio, the -issimi superlative, glielo
        (combined pronouns), formal le with the shopkeeper, resto (change).
        Perform it in pairs, then improvise your own market run."""),
    how_it_works=textwrap.dedent("""\
        This record teaches conversation by the performance method: two
        learners perform the 20 lines with the annotations, then improvise a
        new market dialogue buying three different items, keeping the frames
        - Vorrei..., Quanto costa?, Mi da...? The annotations are the lesson:
        each explains WHY the line is built that way, so the improvisation
        keeps the grammar right."""),
    key_points=[
        "20-line bilingual market dialogue with grammar annotations.",
        "Vorrei (I would like) - the polite request verb of shopping.",
        "-Issimi absolute superlative: freschissimi = very fresh indeed.",
        "Glielo = combined pronouns: to you + it, in one word.",
        "Perform it, then improvise your own market run with three items.",
    ],
    requirements=[
        "Learners should perform the dialogue in pairs with the annotations.",
        "Improvise a new market dialogue buying three different items.",
    ],
    standards=[
        "Standard Italian conversational usage per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, the market dialogue is the "
              "contract negotiated live - offer, counter, agreement, receipt. "
              "This Signature reading treats each line as a spoken clause "
              "sealed with Buona giornata."),
)


E(
    key="italian_dialogue_friend", name="Italian Conversation: Meeting a Friend",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue meeting a friend, annotated. 1.
        Marco: Ciao, Sara! Che sorpresa! (Hi, Sara! What a surprise! - ciao
        and che sorpresa mark close friends.) 2. Sara: Marco! Quanto tempo!
        (Marco! It has been ages! - quanto tempo = long time no see.) 3.
        Marco: Come stai? (How are you? - informal tu.) 4. Sara: Benissimo, e
        tu? (Great, and you? - benissimo: very well indeed.) 5. Marco:
        Tutto bene. Che fai di bello? (All good. What are you up to? -
        literally what do you do that is beautiful.) 6. Sara: Lavoro in una
        libreria in centro. E tu? (I work in a bookstore downtown. And you?)
        7. Marco: Insegno italiano agli stranieri. (I teach Italian to
        foreigners - agli = a + gli.) 8. Sara: Che bello! Da quanto tempo?
        (How nice! Since when? - da quanto tempo asks duration.) 9. Marco: Da
        due anni. Mi piace tantissimo. (For two years. I like it enormously.)
        10. Sara: Hai tempo per un caffe? (Do you have time for a coffee? -
        the Italian social ritual.) 11. Marco: Volentieri! Andiamo al bar
        all'angolo? (Gladly! Shall we go to the bar on the corner? - bar =
        cafe in Italian.) 12. Sara: Perfetto. Offro io! (Perfect. My treat! -
        literally I offer.) 13. Marco: No, no, facciamo alla romana. (No, no,
        let us split - alla romana = Roman style, each pays their share.) 14.
        Sara: Va bene. Allora raccontami tutto! (OK. Then tell me everything!)
        15. Marco: Prima tu: sei ancora con Andrea? (You first: are you still
        with Andrea?) 16. Sara: Si, ci sposiamo a giugno! (Yes, we are
        getting married in June!) 17. Marco: Congratulazioni! Sono felicissimo
        per te! (Congratulations! I am so happy for you!) 18. Sara: Grazie!
        Verrai al matrimonio? (Thanks! Will you come to the wedding?) 19.
        Marco: Certo che vengo! (Of course I am coming!) 20. Sara: Allora ci
        vediamo presto. Un abbraccio! (Then see you soon. A hug!) Annotations
        teach the tu register, che fai di bello, da quanto tempo, the coffee
        ritual, alla romana (splitting), wedding news formulas. Perform it,
        then improvise your own reunion."""),
    how_it_works=textwrap.dedent("""\
        This record teaches friendly conversation by the reunion method: two
        learners perform the 20 lines, then improvise meeting a friend they
        have not seen in years - Come stai? Che fai di bello? Da quanto
        tempo? - with true personal news. The coffee invitation is drilled as
        the engine of Italian social life: every reunion runs on Hai tempo
        per un caffe?"""),
    key_points=[
        "20-line bilingual reunion dialogue with annotations.",
        "Che fai di bello? - the what-are-you-up-to formula.",
        "Da quanto tempo? - asking how long, answered with Da due anni.",
        "Alla romana - splitting the bill, Roman style.",
        "Perform it, then improvise your own reunion with true news.",
    ],
    requirements=[
        "Learners should perform the dialogue in pairs.",
        "Improvise a reunion using true personal news.",
    ],
    standards=[
        "Standard Italian conversational usage per the Accademia della Crusca.",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
    ],
    sig_lens=("Through the Signature lens, the reunion is the contract's "
              "renewal between friends - old signatures recognized, new "
              "chapters witnessed. This Signature reading treats the coffee "
              "together as the seal warmed and pressed again."),
)


E(
    key="italian_dialogue_problem", name="Italian Conversation: Solving a Problem",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue solving a problem, annotated. 1.
        Turista: Mi scusi, mi sono perso. (Excuse me, I am lost - mi scusi
        opens with the formal apology.) 2. Passante: Non si preoccupi. Dove
        deve andare? (Do not worry - formal si. Where do you need to go?) 3.
        Turista: Cerco il Museo Nazionale. (I am looking for the National
        Museum.) 4. Passante: E vicino. Vada sempre dritto. (It is near. Keep
        going straight - vada is the formal imperative.) 5. Turista: Dritto
        fino in fondo? (Straight to the end?) 6. Passante: Si, poi giri a
        sinistra al semaforo. (Yes, then turn left at the traffic light.) 7.
        Turista: A sinistra, ho capito. E lontano? (Left, understood. Is it
        far?) 8. Passante: No, cinque minuti a piedi. (No, five minutes on
        foot.) 9. Turista: C'e un ingresso laterale? (Is there a side
        entrance?) 10. Passante: Si, ma e chiuso il lunedi. (Yes, but it is
        closed Mondays.) 11. Turista: Oggi e martedi, bene. A che ora chiude?
        (Today is Tuesday, good. What time does it close?) 12. Passante: Alle
        diciotto. (At six p.m. - Italians use 24-hour time officially.) 13.
        Turista: Quanto costa il biglietto? (How much is the ticket?) 14.
        Passante: Dieci euro, ridotto otto. (Ten euros, eight reduced.) 15.
        Turista: Perfetto. E per mangiare qui vicino? (Perfect. And to eat
        nearby?) 16. Passante: C'e una trattoria ottima in via Roma. (There
        is an excellent trattoria on Via Roma.) 17. Turista: La ringrazio
        molto, e stato gentilissimo. (Thank you very much, you have been very
        kind - formal la ringrazio.) 18. Passante: Prego! Buona visita! (You
        are welcome! Enjoy your visit!) 19. Turista: ArrivederLa! (Goodbye -
        formal!) 20. Passante: ArrivederLa! (Goodbye - formal!) Annotations
        teach the formal register throughout (mi scusi, vada, La ringrazio,
        ArrivederLa), direction vocabulary, 24-hour time, museum practical
        phrases. Perform it, then improvise your own lost-tourist rescue."""),
    how_it_works=textwrap.dedent("""\
        This record teaches problem-solving by the rescue method: two learners
        perform the 20 lines in full formal register, then improvise - one is
        lost with a real destination, the other guides them using only
        Italian directions. The formal imperatives (vada, giri) are drilled
        as the polite way to direct a stranger, and the whole exchange proves
        the learner can survive a real problem in Italian."""),
    key_points=[
        "20-line bilingual problem-solving dialogue, full formal register.",
        "Formal imperatives for strangers: vada dritto, giri a sinistra.",
        "Mi sono perso + Dove deve andare - the rescue opening.",
        "24-hour time in official use: Alle diciotto.",
        "Perform it, then improvise your own lost-tourist rescue.",
    ],
    requirements=[
        "Learners should perform the dialogue in full formal register.",
        "Improvise a rescue with a real destination, directions in Italian only.",
    ],
    standards=[
        "Standard Italian formal usage per the Accademia della Crusca.",
    ],
    citations=[
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, the rescue is the contract's "
              "good-faith clause in action - a stranger aided, directions "
              "given as sworn testimony. This Signature reading treats the "
              "thank-you as the receipt signed on the spot."),
)


E(
    key="italian_mastery", name="Italian Mastery Review and Full Reference",
    group="Reference", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        The whole database in one teaching summary: alphabet, 200 core words,
        key grammar, and all phrase tables. ALPHABET: 21 letters (A B C D E
        F G H I L M N O P Q R S T U V Z) + J K W X Y foreign; H silent; grave
        accents a e i o u on final stress; apostrophe for elision. SOUNDS: 7
        vowels; C/G hard before A O U, soft before E I; CH/GH hard; SC+E/I =
        SH; GN = NY; GLI = million-LL; double consonants held; stress
        penultimate unless accented. 200 CORE WORDS (sampled across the
        records): uomo, donna, bambino, famiglia, amico, casa, porta,
        finestra, tavolo, sedia, libro, scuola, lavoro, giorno, notte, tempo,
        acqua, cibo, macchina, strada, citta, paese, mondo, nome, problema,
        essere, avere, fare, andare, dire, vedere, mangiare, bere, parlare,
        scrivere, leggere, dormire, lavorare, studiare, comprare, vendere,
        aprire, chiudere, prendere, dare, venire, sapere, conoscere, pensare,
        amare, bello, buono, grande, piccolo, nuovo, vecchio, alto, basso,
        lungo, corto, felice, triste, caldo, freddo, dolce, rosso, verde,
        bianco, nero, molto, poco, bene, male, sempre, mai, gia, ancora,
        troppo, oggi, ieri, io, tu, lui, lei, noi, voi, loro, mio, tuo, suo,
        nostro, vostro, questo, quello, chi, che, cosa, come, quando, dove,
        perche, quale, uno...cento, primo...decimo, lunedi...domenica,
        gennaio...dicembre, primavera, estate, autunno, inverno, ciao,
        buongiorno, buonasera, grazie, prego, per favore, scusi, arrivederci.
        KEY GRAMMAR: SVO; il/lo/la/l'/i/gli/le, un/uno/una/un'; adjectives
        agree (libro rosso, casa rossa); non + verb negates; questions by
        intonation; c'e/ci sono; passato prossimo ho/sono; imperfetto -avo;
        futuro -ero; condizionale -erei; congiuntivo after che; tu vs Lei.
        PHRASE TABLES: greetings (Buongiorno, Come sta, ArrivederLa),
        restaurant (Vorrei, Il conto, per favore), travel (Dov'e, Quanto
        costa, Un biglietto), health (Mi fa male, Ho la febbre, Dov'e la
        farmacia), shopping (E troppo caro, Puo farmi uno sconto, Lo prendo).
        The ladder in one line: sounds -> words -> grammar -> sentences ->
        tenses -> stories -> idioms -> conversations -> mastery. Test
        yourself: retell all three stories, perform all three dialogues, use
        five idioms in real speech - then the contract is signed: you speak
        Italian."""),
    how_it_works=textwrap.dedent("""\
        This record teaches mastery by the consolidation method: the learner
        reads the full summary, then self-tests against it - covering the 200
        words and recalling each with its article, rebuilding the grammar
        rules from the one-line forms, and performing the phrase tables from
        memory. The final exam is performance: retell the three stories,
        perform the three dialogues, deploy five idioms in real conversation.
        Whatever fails goes back down the ladder to its record for repair."""),
    key_points=[
        "Full alphabet, sound rules, and stress rules in one table.",
        "200 core words sampled across all records - with articles.",
        "Key grammar compressed to one-line forms: articles, agreement, negation, tenses, tu/Lei.",
        "Phrase tables: greetings, restaurant, travel, health, shopping.",
        "Final exam: 3 stories retold, 3 dialogues performed, 5 idioms deployed.",
    ],
    requirements=[
        "Learners should self-test on the 200 words with articles.",
        "Pass the performance exam: stories, dialogues, idioms in real speech.",
    ],
    standards=[
        "Consolidated standard Italian per the Accademia della Crusca.",
        "ISO 639-1:1988 (it); ISO 639-2:1998 (ita).",
    ],
    citations=[
        "Accademia della Crusca. Florence; founded 1583.",
        "Serianni L. Grammatica italiana. Italiano comune e lingua letteraria. UTET; 1988.",
    ],
    sig_lens=("Through the Signature lens, the mastery review is the "
              "contract bound and sealed - every record a signed page, every "
              "story a witnessed chapter, the whole ladder one executed "
              "instrument. The learner's voice is the final seal."),
)


SIG_TAIL = ("Signature editions are his original Signature Language Method - "
            "every word a covenant between sound and meaning, every sentence a "
            "signed contract of understanding, the learner's voice the seal. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")
