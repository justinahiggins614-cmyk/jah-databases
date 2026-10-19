#!/usr/bin/env python3
"""Entries for the Portuguese to English databases (34 ladder-ordered records).

Public records: real, fact-checked Portuguese language teaching - every record
carries Portuguese content with English translation and example sentences,
organized in the Signature system.
"""
import textwrap

ENTRIES = []


def E(**kw):
    ENTRIES.append(kw)
    return kw


E(
    key="portuguese_overview", name="Portuguese Language Overview",
    group="Language overview", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Portuguese (portugues) is a Western Romance language of the Indo-European
        family, born in the northwest of the Iberian Peninsula and carried around
        the world by exploration, trade, and settlement. It is the official
        language of nine countries: Brazil, Portugal, Angola, Mozambique,
        Guinea-Bissau, Cape Verde, Sao Tome and Principe, Equatorial Guinea, and
        Timor-Leste, and it is also used in Macau. Roughly 236 million people
        speak Portuguese as their first language and about 250 million speak it
        in total, making it the sixth most spoken native language in the world
        and the most spoken language in the Southern Hemisphere. Brazil alone
        holds more than 200 million speakers - over 80 percent of all
        Portuguese speakers. The two great written standards are European
        Portuguese (Portugal and Africa) and Brazilian Portuguese, with the 1990
        Orthographic Agreement (Acordo Ortografico) harmonizing spelling across
        the Portuguese-speaking world. Portuguese grew out of Vulgar Latin,
        shares deep roots with Spanish, Galician, Catalan, Italian, and French,
        and borrows everyday words from Arabic, African languages, and the
        Indigenous languages of the Americas. This record is the map of the
        whole database: what Portuguese is, where it lives, and how the ladder
        below carries a learner from a first greeting to full conversation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the overview by anchoring every fact in a sentence
        the learner can say. Each fact - the native name portugues, the ISO
        codes pt and por, the language family path, the speaker numbers, the
        nine official countries, the two main standards - appears with a plain
        English explanation and a Portuguese example sentence. The learner reads
        the facts, then repeats the sentences, so the overview is not memorized
        trivia but spoken language from the first record. Later records climb
        the teaching ladder: foundations (records 1-10: sounds, words, grammar
        basics), compounded (records 11-24: themed sentence sets and verb
        tenses), advanced (records 25-34: stories, idioms, registers, complex
        sentences, conversations, and a full reference)."""),
    key_points=[
        "Native name: portugues; English name: Portuguese; ISO 639-1: pt; ISO 639-3: por.",
        "Family: Indo-European > Italic > Romance > Western > Ibero-Romance > West Iberian.",
        "About 236 million native speakers; about 250 million total speakers worldwide.",
        "Official in nine countries plus Macau; Brazil holds over 80 percent of speakers.",
        "Two main standards: European Portuguese and Brazilian Portuguese; spelling harmonized by the 1990 Acordo Ortografico.",
        "Every record in this database carries Portuguese content, English translation, and example sentences.",
    ],
    requirements=[
        "No prior knowledge of Portuguese is needed; this is the starting record of the ladder.",
        "Learners should read each example sentence aloud to begin training pronunciation from day one.",
    ],
    standards=[
        "ISO 639-1:1988 (pt) and ISO 639-2:1998 (por) language codes.",
        "Acordo Ortografico da Lingua Portuguesa, 1990 - the unified spelling standard.",
    ],
    citations=[
        "Acordo Ortografico da Lingua Portuguesa. 1990. Unifies spelling across the Portuguese-speaking countries.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. The standard reference grammar of contemporary Portuguese.",
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017. The official proficiency framework for Portuguese as a foreign language.",
    ],
    sig_lens=("Through the Signature lens, a language is not a school subject - it is a "
              "living contract between peoples, and Portuguese is one of the great signed "
              "contracts of human history: two hundred and thirty-six million voices keeping "
              "one oath of meaning across four continents. This Signature reading treats the "
              "overview as the first seal of that contract."""),
)

E(
    key="portuguese_writing", name="Portuguese Writing System",
    group="Writing and sound", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Portuguese is written with the Latin alphabet, read left to right, with
        the same 26 letters as English since the 1990 Orthographic Agreement
        formally added K, W, and Y: A B C D E F G H I J K L M N O P Q R S T U
        V W X Y Z. Letters K, W, and Y appear mostly in foreign words, proper
        names, and scientific terms (kilo, website, yoga). The musical sound of
        Portuguese comes from its diacritics: the acute accent (a, e, i, o, u)
        marks an open stressed vowel, the circumflex (a, e, o) marks a closed
        stressed vowel, the tilde (a, o) marks a nasal vowel, the grave accent
        (a) appears only in the contraction a + a (a), and the cedilla (c)
        turns C into the soft sound of S before A, O, or U, as in coracao
        (heart). The trema (u) was abolished by the 1990 Agreement except in a
        few proper names. Question marks and exclamation marks work as in
        English, and the decimal system uses a comma where English uses a
        point: 3,14 for pi. Numerals are the familiar Arabic digits 0-9. Master
        the letters and the five diacritics, and every Portuguese word becomes
        pronounceable on sight."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the writing system by pairing every letter and
        diacritic with a real word, its pronunciation hint, and its English
        translation. The learner copies the alphabet, sounds each letter with
        its example word - A as in amor (love), C cedilla as in coracao
        (heart), the tilde as in pao (bread) - and practices the five diacritic
        marks by writing accented words by hand. Because Portuguese spelling is
        far more regular than English spelling, this one record unlocks reading
        for the entire database."""),
    key_points=[
        "26 letters, left to right; K, W, Y reintroduced by the 1990 Orthographic Agreement for foreign words and names.",
        "Acute (a), circumflex (a), tilde (a), grave (a, only in contractions), cedilla (c) - five marks with clear jobs.",
        "Acute = open stressed vowel; circumflex = closed stressed vowel; tilde = nasal vowel; cedilla = C sounds like S.",
        "Trema (u) abolished by the 1990 Agreement; the old spelling is gone from new books.",
        "Decimal comma: 3,14. Familiar digits 0-9. Portuguese spelling is highly regular - learn the rules once, read everything.",
    ],
    requirements=[
        "Learners should write the alphabet by hand once and say each letter with its example word.",
        "Practice the tilde and cedilla first - they carry the most distinctively Portuguese sounds.",
    ],
    standards=[
        "Acordo Ortografico da Lingua Portuguesa, 1990 - alphabet and diacritic rules.",
        "Instituto Camoes orthography guidelines for Portuguese as a foreign language.",
    ],
    citations=[
        "Acordo Ortografico da Lingua Portuguesa. 1990. Governs the 26-letter alphabet, diacritics, and spelling.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Chapters on spelling and accentuation.",
    ],
    sig_lens=("Through the Signature lens, the alphabet is the first covenant of the "
              "written word: twenty-six signs, five seals of accent, and one simple oath - "
              "what is written is what is spoken. This Signature reading treats the tilde "
              "and the cedilla as the two unmistakable signatures of Portuguese on the page."""),
)

E(
    key="portuguese_phonology", name="Portuguese Pronunciation and Phonology",
    group="Writing and sound", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Portuguese sounds are learned, not guessed, because the spelling tells
        the mouth what to do. The five vowels A, E, I, O, U each have an open
        and a closed sound, and the tilde adds five nasal vowels: a in pao
        (bread), a in ma (hand), o in pao, e in bem (well), i in sim (yes),
        u in um (one). European Portuguese softens unstressed vowels toward a
        whisper - the famous "sh" and swallowed vowels - while Brazilian
        Portuguese keeps vowels fuller and brighter. The letter R is the
        hardest sound for learners: at the start of a word or doubled (RR) it
        is a strong guttural sound, as in rua (street) and carro (car); between
        vowels a single R is a light tap, as in caro (expensive). S between
        vowels sounds like Z (casa = CAH-zah), X is unpredictable and simply
        memorized, and LH and NH are single sounds: LH like the LL in "million"
        (filho = son), NH like the NY in "canyon" (manha = morning). Stress
        falls on the second-to-last syllable by default (cidade), on the last
        syllable when the word ends in a consonant other than S or in a diphthong
        (amor, papel), and anywhere an accent mark points (musica). Ten spoken
        examples to say aloud: pao (bread), mae (mother), coracao (heart),
        cidade (city), agua (water), sol (sun), noite (night), amor (love),
        tempo (time), obrigado (thank you). Say them slowly, then at speaking
        speed, and the music of Portuguese starts to live in your mouth."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronunciation by giving every sound rule a word to
        say, an English approximation to aim for, and a translation to anchor
        the memory. The learner practices the nasal vowels by holding the
        sound through the nose, practices the two R sounds in rua versus caro,
        and learns the three default stress rules so any new word can be
        stressed correctly on first sight. Ten example words - pao, mae,
        coracao, cidade, agua, sol, noite, amor, tempo, obrigado - are the
        daily drill: say each one, translate it, and repeat until the mouth
        moves without thinking."""),
    key_points=[
        "Five oral vowels plus five nasal vowels; the tilde always means nasal.",
        "R is guttural at word start and doubled (rua, carro), a light tap between vowels (caro).",
        "S between vowels sounds like Z (casa); LH = 'million' LL (filho); NH = 'canyon' NY (manha).",
        "Stress: second-to-last syllable by default (cidade); last syllable before most final consonants (amor); accent marks always win (musica).",
        "Brazilian vowels are fuller; European unstressed vowels are softer - both follow the same spelling rules.",
    ],
    requirements=[
        "Say the ten drill words aloud daily; record yourself and compare against a native speaker if possible.",
        "Do not pronounce Portuguese like Spanish - the nasal vowels and the softened unstressed vowels are the giveaway.",
    ],
    standards=[
        "Instituto Camoes Referencial Camoes Portugues Lingua Estrangeira, 2017 - pronunciation targets for learners.",
        "International Phonetic Alphabet (IPA) conventions used for sound description.",
    ],
    citations=[
        "Mateus M H M et al. Gramatica da Lingua Portuguesa. 7th ed. Caminho; 2006. The reference phonology of Portuguese.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013.",
    ],
    sig_lens=("Through the Signature lens, pronunciation is the voice sealing the "
              "contract of meaning: the nasal vowel is the breath made audible, the "
              "guttural R the engine of the street, the tilde the visible mark of "
              "sound passing through the nose. This Signature reading treats every "
              "sound rule as a clause of the spoken covenant."""),
)

E(
    key="portuguese_nouns", name="Portuguese Core Nouns I",
    group="Core vocabulary", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Nouns are the bricks of Portuguese, and every noun is masculine or
        feminine - there is no neutral. The article tells the gender: o homem
        (the man), a mulher (the woman). Learn each noun with its article and
        the gender becomes automatic. Here are twenty-five essential nouns,
        each with an example sentence and translation. O homem trabalha muito.
        (The man works a lot.) A mulher le a revista. (The woman reads the
        magazine.) A crianca brinca no parque. (The child plays in the park.) O
        amigo mora perto daqui. (The friend lives near here.) A familia e
        grande. (The family is big.) A casa tem tres quartos. (The house has
        three bedrooms.) A porta esta aberta. (The door is open.) A janela da
        para o jardim. (The window faces the garden.) A mesa e de madeira.
        (The table is made of wood.) A cadeira e confortavel. (The chair is
        comfortable.) O livro esta na mesa. (The book is on the table.) A
        escola fica longe. (The school is far away.) O trabalho comeca cedo.
        (Work starts early.) O dia esta lindo. (The day is beautiful.) A noite
        cai devagar. (The night falls slowly.) O tempo passa rapido. (Time
        passes quickly.) A agua esta fria. (The water is cold.) A comida cheira
        bem. (The food smells good.) O carro e novo. (The car is new.) A rua e
        estreita. (The street is narrow.) A cidade nunca dorme. (The city never
        sleeps.) O pais e enorme. (The country is huge.) O mundo e redondo.
        (The world is round.) O nome dele e Carlos. (His name is Carlos.) O
        problema tem solucao. (The problem has a solution.) Twenty-five nouns,
        twenty-five sentences, and the skeleton of a thousand conversations."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nouns the way native speakers learn them: never
        alone, always with the article that carries the gender. The learner
        reads each noun, notes whether it takes o or a, studies the example
        sentence, and repeats it aloud with the translation in mind. The
        vocabulary quiz in the demonstration program tests English-to-Portuguese
        recall on exactly these words, so the entry and the demo verify each
        other. Master these twenty-five and the themed sentence records that
        follow will feel like familiar ground."""),
    key_points=[
        "Every noun is masculine or feminine; the article (o/a) reveals the gender - always learn them together.",
        "Endings hint at gender: -o is usually masculine (livro), -a usually feminine (casa), but -ema/-ama words like problema are masculine.",
        "Plurals add -s: casa -> casas, livro -> livros; words ending in -ao take -oes or -aes (mao -> maos).",
        "25 essential nouns with 25 translated example sentences: people, home, objects, time, places.",
    ],
    requirements=[
        "Memorize each noun together with its article; flashcards should show 'o livro', not 'livro'.",
        "Say every example sentence aloud; the quiz in the demo checks recall.",
    ],
    standards=[
        "Acordo Ortografico da Lingua Portuguesa, 1990 - plural and spelling rules.",
        "CEFR A1 vocabulary scope: everyday nouns for people, home, and immediate surroundings.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Noun gender and number.",
        "Dicionario Houaiss da Lingua Portuguesa. Gender and plural entries for all headwords.",
    ],
    sig_lens=("Through the Signature lens, a noun is the name sealed on a thing: to "
              "say 'a casa' is to put the feminine seal on the house itself, and no "
              "house in Portuguese is ever nameless of gender. This Signature reading "
              "treats the article as the signature line under every noun."""),
)

E(
    key="portuguese_verbs", name="Portuguese Core Verbs I",
    group="Core vocabulary", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Verbs are the engines of Portuguese sentences, and they conjugate -
        the ending changes with the speaker. Twenty-five essential verbs, each
        with a sentence: Ser: Ele e medico. (He is a doctor.) Estar: Ela esta
        cansada. (She is tired.) Ter: Eu tenho dois irmaos. (I have two
        brothers.) Fazer: Nos fazemos o almoco. (We make lunch.) Ir: Eles vao
        a praia. (They go to the beach.) Poder: Voce pode ajudar? (Can you
        help?) Querer: Eu quero cafe. (I want coffee.) Saber: Ela sabe nadar.
        (She knows how to swim.) Dar: Eu dou o presente. (I give the gift.)
        Dizer: Ele diz a verdade. (He tells the truth.) Ver: Nos vemos o mar.
        (We see the sea.) Ouvir: Voce ouve a musica? (Do you hear the music?)
        Falar: Eu falo portugues. (I speak Portuguese.) Comer: Eles comem
        arroz. (They eat rice.) Beber: Nos bebemos agua. (We drink water.)
        Dormir: A crianca dorme cedo. (The child sleeps early.) Trabalhar: Eu
        trabalho em casa. (I work from home.) Estudar: Ela estuda medicina.
        (She studies medicine.) Aprender: Nos aprendemos juntos. (We learn
        together.) Ensinar: Ele ensina ingles. (He teaches English.) Comprar:
        Eu compro pao. (I buy bread.) Vender: Eles vendem carros. (They sell
        cars.) Pagar: Voce paga a conta. (You pay the bill.) Abrir: Abra a
        porta! (Open the door!) Fechar: Feche a janela! (Close the window!)
        Note the two verbs for "to be": ser for identity and lasting traits,
        estar for states and locations. Master these twenty-five verbs in the
        present tense and you can say what is, what happens, and what people
        do."""),
    how_it_works=textwrap.dedent("""\
        This record teaches verbs by the three regular families: -ar verbs like
        falar, -er verbs like comer, and -ir verbs like abrir. The learner
        studies each verb with its example sentence, then practices the present
        tense pattern: eu falo, tu falas, ele fala, nos falamos, eles falam.
        The conjugation drill in the demonstration program generates these
        forms from the infinitive and checks them against the forms taught in
        this entry, so the program and the page verify each other. Irregular
        verbs - ser, estar, ter, ir, poder, querer, saber, dar, dizer - are
        learned by heart, one sentence at a time."""),
    key_points=[
        "Three verb families: -ar (falar), -er (comer), -ir (abrir); regular endings follow a fixed pattern per family.",
        "Ser = identity and lasting traits (Ele e medico); estar = states and location (Ela esta cansada).",
        "25 essential verbs with 25 translated sentences; the eight irregulars here must be memorized by heart.",
        "Present tense pattern for -ar: -o, -as, -a, -amos, -am (falo, falas, fala, falamos, falam).",
    ],
    requirements=[
        "Conjugate each regular verb aloud through all six persons before moving to the next.",
        "Memorize the present tense of ser, estar, ter, and ir - they appear in half of all sentences.",
    ],
    standards=[
        "CEFR A1-A2 verb scope: present tense of high-frequency regular and irregular verbs.",
        "Instituto Camoes Referencial: ser/estar distinction taught as a core A1 objective.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Verb conjugation and the ser/estar distinction.",
        "Houaiss A. Dicionario Houaiss da Lingua Portuguesa. Verb entries with full conjugations.",
    ],
    sig_lens=("Through the Signature lens, a verb is the oath in motion: the ending "
              "is the speaker signing who acts - eu falo, tu falas, ele fala - and the "
              "irregular verbs are the old oaths, memorized because they were sworn "
              "long before the rules were written. This Signature reading treats "
              "conjugation as the act of signing the sentence."""),
)

E(
    key="portuguese_adjectives", name="Portuguese Adjectives and Adverbs",
    group="Core vocabulary", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Adjectives in Portuguese agree with the noun: masculine, feminine,
        singular, plural. O carro bonito (the pretty car), a casa bonita (the
        pretty house), os carros bonitos, as casas bonitas. Most adjectives
        follow the noun, and some change meaning with position: um homem grande
        (a big man) versus um grande homem (a great man). Twenty-five
        adjectives with sentences: bonito/bonita (pretty), grande (big), pequeno
        (small), novo (new), velho (old), bom (good), mau (bad), alto (tall),
        baixo (short), rapido (fast), lento (slow), facil (easy), dificil
        (difficult), feliz (happy), triste (sad), quente (hot), frio (cold),
        limpo (clean), sujo (dirty), claro (light/clear), escuro (dark), forte
        (strong), fraco (weak), rico (rich), pobre (poor). Example: A sopa esta
        quente. (The soup is hot.) Ele e um homem forte. (He is a strong man.)
        Adverbs do not change form and usually sit near the verb: muito
        (very/much), pouco (little), bem (well), mal (badly), sempre (always),
        nunca (never), ja (already), ainda (still), aqui (here), la (there),
        hoje (today), amanha (tomorrow), ontem (yesterday), cedo (early),
        tarde (late). Example: Ela fala bem portugues. (She speaks Portuguese
        well.) Nos chegamos cedo. (We arrived early.) Agreement is the heart of
        Portuguese description: the adjective must match its noun, always."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description through the agreement machine. The
        learner takes each adjective and runs it through the four forms -
        masculine singular, feminine singular, masculine plural, feminine
        plural - then attaches it to a noun in a full sentence. The agreement
        drill in the demonstration program computes these four forms from the
        masculine singular and checks them against the forms in this entry.
        Adverbs are practiced in fixed phrases near the verb: fala bem, chega
        cedo, trabalha muito. Twenty-five adjectives and fifteen adverbs, each
        in a sentence, give the learner the full palette of everyday
        description."""),
    key_points=[
        "Adjectives agree in gender and number: bonito, bonita, bonitos, bonitas.",
        "Most adjectives follow the noun; a few (grande, bom, mau) change meaning when placed before it.",
        "Adjectives ending in -e or a consonant (feliz, facil) use one form for both genders.",
        "Adverbs never change: muito, bem, sempre, nunca, ja, ainda, aqui, la, hoje, amanha, ontem, cedo, tarde.",
        "25 adjectives + 15 adverbs, each with a translated example sentence.",
    ],
    requirements=[
        "For each adjective, write all four agreement forms before using it in a sentence.",
        "Learn the position-sensitive adjectives (grande, bom, novo, velho) as pairs: before vs after the noun.",
    ],
    standards=[
        "Acordo Ortografico da Lingua Portuguesa, 1990 - adjective spelling and plural formation.",
        "CEFR A1-A2 scope: agreement of common adjectives; high-frequency adverbs of time, place, and manner.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Adjective agreement and placement.",
        "Mateus M H M et al. Gramatica da Lingua Portuguesa. Caminho; 2006. Adverb classes.",
    ],
    sig_lens=("Through the Signature lens, the adjective is the witness that must "
              "match the noun it testifies for: bonito swears to o carro, bonita "
              "swears to a casa, and a mismatched ending is a broken testimony. This "
              "Signature reading treats agreement as the law of true description."""),
)

E(
    key="portuguese_pronouns", name="Portuguese Pronouns",
    group="Core vocabulary", ladder_rank=4, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Pronouns replace nouns, and Portuguese has a full cabinet of them.
        Personal pronouns: eu (I), tu (you, informal), ele/ela (he/she), nos
        (we), vos (you, formal-plural, rare in Brazil), eles/elas (they). In
        Brazil, voce/voces (you) replaced tu/vos in most speech, and verbs use
        the ele/eles endings with them: voce fala, voces falam. Possessive
        pronouns agree like adjectives: meu/minha (my), teu/tua (your,
        informal), seu/sua (his/her/your formal), nosso/nossa (our),
        vosso/vossa (your, plural), seu/sua (their). O meu livro (my book), a
        nossa casa (our house). Demonstratives mark distance: este/esta (this,
        near me), esse/essa (that, near you), aquele/aquela (that, far from
        both). Este livro e meu. (This book is mine.) Interrogatives ask: quem
        (who), o que (what), qual/quais (which), onde (where), quando (when),
        por que (why), como (how), quanto (how much). Quem e voce? (Who are
        you?) Onde fica o hotel? (Where is the hotel?) Clitic object pronouns
        (me, te, o, a, lhe, nos, vos, os, as, lhes) attach to verbs: Ele me viu.
        (He saw me.) Eu te amo. (I love you.) Learn the personal and possessive
        paradigms cold - they unlock every sentence that follows."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronouns as complete paradigms, not isolated words.
        The learner copies each table - personal, possessive, demonstrative,
        interrogative - and practices one example sentence per pronoun until
        the table can be recited without looking. The paradigm checker in the
        demonstration program verifies the table sizes taught here (six personal
        pronouns plus voce/voces, six possessive pairs, six demonstratives,
        eight interrogatives), so the entry and the program hold each other
        accountable. Brazil-vs-Portugal usage notes keep the learner oriented
        in both standards."""),
    key_points=[
        "Personal: eu, tu, ele/ela, nos, vos, eles/elas - plus voce/voces, the everyday 'you' in Brazil.",
        "Voce/voces take third-person verb endings: voce fala, voces falam.",
        "Possessives agree with the thing owned: meu livro, minha casa, nosso carro, nossa familia.",
        "Demonstratives mark distance: este (near me), esse (near you), aquele (far from both).",
        "Interrogatives: quem, o que, qual, onde, quando, por que, como, quanto - each with an example question.",
    ],
    requirements=[
        "Recite the personal pronoun table aloud until it is automatic; it is the key to all conjugation.",
        "Practice possessives with real objects around you: o meu telefone, a minha mesa.",
    ],
    standards=[
        "Instituto Camoes Referencial: personal and possessive pronouns as A1 core objectives.",
        "Acordo Ortografico da Lingua Portuguesa, 1990 - pronoun spelling (e.g., the hyphenated clitics).",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Pronoun paradigms and clitic placement.",
        "Mateus M H M et al. Gramatica da Lingua Portuguesa. Caminho; 2006.",
    ],
    sig_lens=("Through the Signature lens, pronouns are the masks the speaker wears: "
              "eu signs for the self, voce signs for the other, and the possessive "
              "stamps ownership - meu, tua, nossa - on everything it touches. This "
              "Signature reading treats the paradigm table as the roster of voices."""),
)

E(
    key="portuguese_numbers", name="Portuguese Numbers and Time",
    group="Core vocabulary", ladder_rank=4, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Numbers first, then the clock, then the calendar. Um (1), dois (2),
        tres (3), quatro (4), cinco (5), seis (6), sete (7), oito (8), nove
        (9), dez (10), onze (11), doze (12), treze (13), catorze/quatorze
        (14), quinze (15), dezesseis (16), dezessete (17), dezoito (18),
        dezenove (19), vinte (20), trinta (30), quarenta (40), cinquenta (50),
        sessenta (60), setenta (70), oitenta (80), noventa (90), cem (100;
        cento before other numbers: cento e um). Compound numbers join with e:
        vinte e um (21), trinta e cinco (35). Um changes with gender before
        nouns: uma mulher, um homem; dois/duas: duas casas. Ordinals:
        primeiro, segundo, terceiro, quarto, quinto. Days of the week are
        numbered like no other Romance language: segunda-feira, terca-feira,
        quarta-feira, quinta-feira, sexta-feira (second through sixth market
        days), sabado, domingo. Months: janeiro, fevereiro, marco, abril,
        maio, junho, julho, agosto, setembro, outubro, novembro, dezembro.
        Seasons: primavera, verao, outono, inverno. Time: Que horas sao? Sao
        duas horas. (What time is it? It is two o'clock.) E meio-dia. (It is
        noon.) E meia-noite. (It is midnight.) A aula e as tres e meia. (Class
        is at half past three.) Dates: Hoje e dia dezessete de outubro. (Today
        is October 17th.) Numbers unlock prices, times, dates, and addresses -
        the practical skeleton of daily life."""),
    how_it_works=textwrap.dedent("""\
        This record teaches numbers as a machine with three gears: units,
        tens, hundreds, joined by e. The learner counts aloud 1-20, then by
        tens to 100, then builds compounds like vinte e um and cento e cinco
        until the pattern is reflexive. The number-to-words engine in the
        demonstration program converts any number 0-100 to Portuguese and is
        checked against the forms taught in this entry, so the program proves
        the entry and the entry proves the program. Days, months, and clock
        time are practiced as questions and answers: Que dia e hoje? Hoje e
        sexta-feira. Que horas sao? Sao oito horas."""),
    key_points=[
        "1-20 and the tens are memorized; compounds join with e: vinte e um, trinta e dois.",
        "Cem = 100 alone; cento before more numbers: cento e um (101).",
        "Um/uma and dois/duas change with gender: uma mulher, duas casas.",
        "Weekdays are numbered: segunda-feira through sexta-feira, then sabado, domingo.",
        "Clock: Sao duas horas; E meio-dia / meia-noite; use 'as' for the hour: as tres e meia.",
    ],
    requirements=[
        "Count aloud 1-100 without notes before leaving this record; speed matters in real conversation.",
        "Practice telling time with a real clock: Sao oito e quinze, E meio-dia.",
    ],
    standards=[
        "CEFR A1: numbers 1-100, telling time, days, months, dates.",
        "Acordo Ortografico da Lingua Portuguesa, 1990 - number word spelling (dezesseis, etc.).",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Numerals.",
        "Instituto Camoes Referencial: numbers, time, and calendar as A1 objectives.",
    ],
    sig_lens=("Through the Signature lens, numbers are the measures sealed by "
              "agreement: vinte e um is not two words but one sworn total, the clock "
              "is the day's contract read aloud, and the numbered weekdays are the "
              "week itself signing its days in order. This Signature reading treats "
              "counting as the first exact science of the language."""),
)

E(
    key="portuguese_greetings", name="Portuguese Greetings and Everyday Phrases",
    group="Core vocabulary", ladder_rank=5, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Thirty phrases that open every door. Ola! (Hello!) Bom dia! (Good
        morning!) Boa tarde! (Good afternoon!) Boa noite! (Good evening /
        good night!) Como vai? (How are you?) Tudo bem? (All good?) Tudo otimo,
        obrigado. (Great, thanks.) Prazer em conhece-lo. (Pleased to meet
        you.) Seja bem-vindo! (Welcome!) Obrigado (said by men) / Obrigada
        (said by women) - thank you. De nada. (You are welcome.) Por favor.
        (Please.) Com licenca. (Excuse me - to pass.) Desculpe. (Sorry.)
        Perdao. (Pardon.) Ate logo. (See you later.) Ate amanha. (See you
        tomorrow.) Tchau! (Bye!) Boa sorte! (Good luck!) Parabens!
        (Congratulations!) Saude! (Cheers! / Bless you!) Boa viagem! (Have a
        good trip!) Bom apetite! (Enjoy your meal!) Que pena! (What a pity!)
        Nao tem problema. (No problem.) Com certeza. (Certainly.) Pois nao?
        (May I help you? - Portugal shops.) Fique a vontade. (Make yourself at
        home.) Deus te abencoe is common in speech but kept out of this record
        by the no-religious-talk rule; use Fique bem. (Take care.) instead.
        Obrigado changes with the speaker's gender, not the listener's - a
        woman always says obrigada. Use these thirty phrases daily and no
        conversation ever starts cold."""),
    how_it_works=textwrap.dedent("""\
        This record teaches phrases as social tools with usage notes, not as
        vocabulary to memorize. Each phrase carries when to use it: bom dia
        until noon, boa tarde until evening, boa noite after dark; com licenca
        to pass through a crowd, desculpe to apologize. The learner practices
        the phrases in imagined scenes - entering a shop, meeting a friend,
        leaving a party - until the right phrase arrives without thought. The
        phrase quiz in the demonstration program tests Portuguese-to-English
        recall on all thirty, exactly as taught here."""),
    key_points=[
        "Obrigado (men) / obrigada (women) - the thank-you agrees with the speaker, not the listener.",
        "Bom dia / boa tarde / boa noite follow the time of day; tchau and ate logo close conversations.",
        "Com licenca = excuse me to pass; desculpe = sorry; perdao = pardon.",
        "Por favor, de nada, com certeza, nao tem problema - the oil of polite conversation.",
        "30 greetings, farewells, and politeness phrases with usage notes.",
    ],
    requirements=[
        "Use five of these phrases in a real or imagined conversation every day until all thirty are natural.",
        "Never mix up com licenca and desculpe - one opens a path, the other mends a fault.",
    ],
    standards=[
        "CEFR A1: formulaic greetings, leave-taking, and politeness conventions.",
        "Instituto Camoes Referencial: social formulas as A1 core objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013.",
    ],
    sig_lens=("Through the Signature lens, a greeting is the handshake before the "
              "contract: bom dia signs the morning open, obrigada seals the kindness "
              "received, and tchau closes the meeting with honor. This Signature "
              "reading treats the thirty phrases as the thirty seals of daily "
              "courtesy."""),
)

E(
    key="portuguese_grammar", name="Portuguese Grammar Essentials",
    group="Grammar", ladder_rank=5, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The seven pillars of Portuguese grammar, each with a sentence. Word
        order: subject-verb-object, as in English - Eu como pao. (I eat
        bread.) Questions keep the same order and rise in intonation - Voce
        fala ingles? (Do you speak English?) - or start with a question word:
        Onde voce mora? Gender: every noun is masculine (o) or feminine (a);
        learn the article with the noun. Number: add -s for plurals - o livro,
        os livros; a casa, as casas. Articles: definite o/a/os/as (the),
        indefinite um/uma/uns/umas (a, some) - Eu quero um cafe. (I want a
        coffee.) Negation: put nao before the verb - Eu nao falo frances. (I
        do not speak French.) Nunca (never) and ninguem (nobody) strengthen it:
        Eu nunca vi isso. (I never saw that.) Question formation: intonation
        alone (Voce vem?), question words (Quem? O que? Onde? Quando? Por
        que? Como? Quanto?), or the tag ne? in Brazil - Voce vem, ne? (You are
        coming, right?) Adjective agreement: adjectives match gender and
        number - um carro novo, uma casa nova, carros novos, casas novas.
        Ser vs estar: ser for identity (Eu sou brasileiro), estar for states
        and place (Eu estou cansado; Ele esta em casa). Seven pillars, seven
        sentences each practiced aloud, and the skeleton of Portuguese grammar
        stands complete."""),
    how_it_works=textwrap.dedent("""\
        This record teaches grammar as seven working rules, each demonstrated
        on a real sentence the learner already knows from earlier records. The
        learner transforms sentences through each rule: make it plural, make
        it negative, make it a question, swap ser for estar and feel the
        meaning change. The sentence-order checker in the demonstration
        program verifies subject-verb-object structure on the example sentences
        of this entry, proving the rules on real text. These seven pillars are
        the foundation every later record builds on - nothing advanced works
        without them."""),
    key_points=[
        "Word order is SVO; questions use rising intonation or a question word - no word-order gymnastics needed.",
        "Negation: nao before the verb; nunca/ninguem for never/nobody.",
        "Articles: o/a/os/as (the), um/uma/uns/umas (a/some); gender and number live in the article.",
        "Adjectives agree with the noun in gender and number - always.",
        "Ser = identity and lasting traits; estar = states, conditions, and location.",
        "Seven pillars, each with translated example sentences to transform and practice.",
    ],
    requirements=[
        "Practice the transformations: take each example sentence and make it plural, negative, and a question.",
        "Master ser vs estar with ten personal sentences: Eu sou..., Eu estou...",
    ],
    standards=[
        "CEFR A1-A2 grammar scope: SVO order, negation, articles, agreement, question formation.",
        "Instituto Camoes Referencial: the seven pillars as A1-A2 core objectives.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013.",
        "Mateus M H M et al. Gramatica da Lingua Portuguesa. Caminho; 2006.",
    ],
    sig_lens=("Through the Signature lens, grammar is the law of the contract: the "
              "word order is the procedure, agreement is the witness rule, negation "
              "is the clause that voids, and ser versus estar is the distinction "
              "between what a thing is and how it stands. This Signature reading "
              "treats the seven pillars as the seven articles of the language's "
              "constitution."""),
)


E(
    key="portuguese_home_family", name="Portuguese Home and Family Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the home and the family, the first compounded
        theme. A minha familia mora numa casa grande. (My family lives in a
        big house.) O meu pai trabalha no banco. (My father works at the
        bank.) A minha mae e professora. (My mother is a teacher.) O meu irmao
        mais velho estuda engenharia. (My older brother studies engineering.)
        A minha irma mais nova adora desenhar. (My younger sister loves to
        draw.) Os meus avos moram no campo. (My grandparents live in the
        countryside.) A sala de estar e clara e confortavel. (The living room
        is bright and comfortable.) A cozinha fica ao lado da sala de jantar.
        (The kitchen is next to the dining room.) O meu quarto tem uma janela
        grande. (My bedroom has a big window.) O banheiro precisa de reforma.
        (The bathroom needs renovation.) A mesa da cozinha e redonda. (The
        kitchen table is round.) O sofa novo chegou ontem. (The new sofa
        arrived yesterday.) O meu tio visita-nos todo domingo. (My uncle
        visits us every Sunday.) A minha prima casou-se em junho. (My cousin
        got married in June.) O bebe dorme no berco. (The baby sleeps in the
        crib.) O cachorro late no quintal. (The dog barks in the backyard.) O
        gato dorme no tapete. (The cat sleeps on the rug.) Nos jantamos juntos
        as sete horas. (We have dinner together at seven o'clock.) A casa dos
        meus pais fica perto da praia. (My parents' house is near the beach.)
        Lar e onde o coracao esta. (Home is where the heart is.) Home words:
        pai, mae, irmao, irma, filho, filha, avo, tio, tia, primo, sala,
        cozinha, quarto, banheiro, quintal."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the home theme by surrounding the learner with
        twenty real sentences about family members, rooms, and furniture. Each
        sentence reuses the grammar pillars - possessives (o meu, a minha),
        ser and estar, plurals - so the foundations get drilled inside new
        vocabulary. The learner reads each sentence, translates it, then
        rebuilds three of them with their own family: O meu pai e..., A minha
        casa tem... The scrambled-sentence checker in the demonstration program
        verifies that these sentences reassemble correctly, proving word order
        on real examples."""),
    key_points=[
        "Family: pai, mae, irmao, irma, filho, filha, avo/avo, tio, tia, primo/prima.",
        "Rooms: sala de estar, cozinha, sala de jantar, quarto, banheiro, quintal.",
        "Possessives drill: o meu pai, a minha mae, os meus avos - agreement with the owned thing.",
        "20 full sentences with translations covering house, rooms, furniture, and family members.",
    ],
    requirements=[
        "Rewrite five sentences with your own family members and your own home.",
        "Say the family words with possessives: meu, minha, meus, minhas - until automatic.",
    ],
    standards=[
        "CEFR A1-A2: family members, rooms, furniture, and daily home life.",
        "Acordo Ortografico da Lingua Portuguesa, 1990 - spelling of all vocabulary.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Family and household vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, the home is the first archive: every "
              "family member a record, every room a field, and the sentence 'a minha "
              "familia' the seal of belonging. This Signature reading treats the "
              "household as the learner's first database of meaning."""),
)

E(
    key="portuguese_food_cooking", name="Portuguese Food and Cooking Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the table, the kitchen, and the restaurant. O cafe
        da manha e a refeicao mais importante. (Breakfast is the most
        important meal.) Eu tomo cafe com leite toda manha. (I drink coffee
        with milk every morning.) O almoco e servido ao meio-dia. (Lunch is
        served at noon.) A feijoada e o prato nacional do Brasil. (Feijoada is
        Brazil's national dish.) O bacalhau e tipico de Portugal. (Salt cod is
        typical of Portugal.) Ela corta as cebolas em fatias finas. (She cuts
        the onions into thin slices.) Ele tempera a carne com sal e pimenta.
        (He seasons the meat with salt and pepper.) Nos cozinhamos o arroz em
        fogo baixo. (We cook the rice on low heat.) A sopa precisa de mais sal.
        (The soup needs more salt.) O bolo esta no forno. (The cake is in the
        oven.) O frango assado cheira muito bem. (The roast chicken smells
        very good.) Voce quer sobremesa? (Do you want dessert?) A conta, por
        favor. (The check, please.) O garcom trouxe o cardapio. (The waiter
        brought the menu.) Este restaurante serve comida caseira. (This
        restaurant serves home-style food.) Eu sou alergico a amendoim. (I am
        allergic to peanuts.) A feira tem frutas frescas. (The market has
        fresh fruit.) Compre dois quilos de tomate. (Buy two kilos of
        tomatoes.) O pao quentinho saiu do forno. (The warm bread just came
        out of the oven.) Bom apetite a todos! (Enjoy your meal, everyone!)
        Food words: arroz, feijao, carne, frango, peixe, ovo, leite, queijo,
        pao, manteiga, acucar, sal, pimenta, cebola, alho, tomate, batata,
        fruta, sobremesa, conta."""),
    how_it_works=textwrap.dedent("""\
        This record teaches food language through the day's meals: breakfast,
        market, cooking, restaurant, and the check. Each sentence carries a
        cooking verb - cortar, temperar, cozinhar, assar, servir - or a
        restaurant phrase, so the learner can shop, cook, and eat in
        Portuguese. The learner practices by narrating their own meal in
        Portuguese: Eu tomo..., Eu compro..., O garcom trouxe... The
        demonstration program's sentence checker verifies these twenty
        sentences reassemble correctly, proving the vocabulary works in real
        word order."""),
    key_points=[
        "Meals: cafe da manha, almoco, jantar, lanche, sobremesa.",
        "Cooking verbs: cortar, temperar, cozinhar, assar, ferver, servir.",
        "Restaurant survival: O cardapio, por favor. A conta, por favor. Eu sou alergico a...",
        "Signature dishes: feijoada (Brazil), bacalhau (Portugal) - culture inside vocabulary.",
        "20 full sentences with translations: meals, ingredients, cooking actions, restaurant.",
    ],
    requirements=[
        "Narrate your next real meal in Portuguese, aloud, using at least five sentences from this record.",
        "Learn the allergy sentence by heart if it applies to you: Eu sou alergico a...",
    ],
    standards=[
        "CEFR A1-A2: food, drink, meals, shopping for food, restaurants.",
        "Instituto Camoes Referencial: food and restaurant objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Culinary vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, the meal is the daily covenant renewed: "
              "the cook signs with salt and fire, the table witnesses, and 'bom "
              "apetite' seals the gathering. This Signature reading treats every "
              "recipe as a contract between hunger and care."""),
)

E(
    key="portuguese_travel", name="Portuguese Travel and Directions Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the road, the station, and the hotel. Onde fica a
        estacao de trem? (Where is the train station?) Fica a dois quarteiroes
        daqui. (It is two blocks from here.) Vire a direita na esquina. (Turn
        right at the corner.) Siga em frente ate o semaforo. (Go straight to
        the traffic light.) O onibus para no centro. (The bus stops downtown.)
        Quanto custa a passagem? (How much is the ticket?) Um bilhete de ida e
        volta, por favor. (A round-trip ticket, please.) O voo sai as dez
        horas. (The flight leaves at ten o'clock.) O meu voo atrasou duas
        horas. (My flight was delayed two hours.) Onde posso alugar um carro?
        (Where can I rent a car?) O hotel fica perto da praia? (Is the hotel
        near the beach?) Eu tenho uma reserva para tres noites. (I have a
        reservation for three nights.) O quarto tem vista para o mar. (The
        room has a sea view.) A que horas e o cafe da manha? (What time is
        breakfast?) Pode chamar um taxi? (Can you call a taxi?) Estou perdido;
        pode me ajudar? (I am lost; can you help me?) O museu abre as nove.
        (The museum opens at nine.) A praia e linda nesta epoca. (The beach is
        beautiful at this time of year.) Leve o passaporte sempre. (Always
        carry your passport.) Boa viagem e ate breve! (Have a good trip and
        see you soon!) Travel words: passagem, bilhete, voo, atraso, hotel,
        reserva, quarto, taxi, onibus, trem, mapa, passaporte, praia, museu."""),
    how_it_works=textwrap.dedent("""\
        This record teaches travel as a sequence: asking the way, buying the
        ticket, boarding, checking in, and seeing the sights. Each sentence is
        a tool the learner will actually use, drilled as question-and-answer
        pairs: Onde fica...? Fica a... The learner practices by giving
        directions around their own neighborhood in Portuguese. The
        demonstration program verifies all twenty sentences reassemble in
        correct order, so the travel phrases are proven on real syntax."""),
    key_points=[
        "Asking the way: Onde fica...? Fica a... Vire a direita/esquerda. Siga em frente.",
        "Transport: Quanto custa a passagem? Um bilhete de ida e volta. O voo atrasou.",
        "Hotel: Eu tenho uma reserva. O quarto tem vista para o mar. A que horas e o cafe da manha?",
        "Emergency clarity: Estou perdido; pode me ajudar? - learn it before you need it.",
        "20 full sentences with translations: transport, directions, tickets, lodging.",
    ],
    requirements=[
        "Practice giving directions from your home to three real places, in Portuguese, aloud.",
        "Memorize the lost-and-help sentence; it is the most important one in the record.",
    ],
    standards=[
        "CEFR A1-A2: travel, transport, asking for and giving directions, accommodation.",
        "Instituto Camoes Referencial: travel objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013.",
    ],
    sig_lens=("Through the Signature lens, the journey is the contract in motion: "
              "the ticket is the signed passage, the direction the sworn route, and "
              "'onde fica' the question that opens every road. This Signature reading "
              "treats the traveler as the covenant carried from place to place."""),
)

E(
    key="portuguese_work_school", name="Portuguese Work and School Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the office and the classroom. Eu trabalho como
        engenheiro. (I work as an engineer.) Ela e medica num hospital grande.
        (She is a doctor at a big hospital.) O escritorio abre as oito horas.
        (The office opens at eight o'clock.) Temos uma reuniao as dez. (We
        have a meeting at ten.) O chefe pediu o relatorio ate sexta. (The boss
        asked for the report by Friday.) Meu salario cai no dia cinco. (My
        salary arrives on the fifth.) Preciso de ferias urgentemente. (I
        urgently need a vacation.) A escola fica perto da minha casa. (The
        school is near my house.) As aulas comecam em fevereiro. (Classes
        start in February.) O professor explicou a licao. (The teacher
        explained the lesson.) Os alunos fizeram a prova ontem. (The students
        took the test yesterday.) Eu estudo portugues todas as noites. (I
        study Portuguese every night.) Ela tirou nota dez na prova. (She got a
        perfect score on the test.) A biblioteca fecha as dez da noite. (The
        library closes at ten at night.) Meu colega de trabalho e muito gentil.
        (My coworker is very kind.) Vamos almocar juntos hoje? (Shall we have
        lunch together today?) O projeto novo e desafiador. (The new project
        is challenging.) Entreguei o trabalho no prazo. (I delivered the work
        on time.) Aprender e um trabalho para a vida toda. (Learning is a
        lifelong job.) Work words: emprego, salario, chefe, colega, reuniao,
        relatorio, prazo, ferias; school words: aula, prova, nota, professor,
        aluno, licao, biblioteca."""),
    how_it_works=textwrap.dedent("""\
        This record teaches work and school language through the working day:
        the job title, the meeting, the deadline, the classroom, the test. Each
        sentence carries a profession noun or a school noun in a real context,
        so the learner can introduce their own work: Eu trabalho como... The
        learner practices by describing their own job or studies in five
        Portuguese sentences. The demonstration program checks all twenty
        sentences for correct reassembly, proving the professional vocabulary
        in real word order."""),
    key_points=[
        "Professions: engenheiro, medica, professor, aluno, chefe, colega - learn yours in Portuguese today.",
        "Office verbs: pedir, entregar, marcar (a reuniao), cumprir (o prazo).",
        "School verbs: estudar, explicar, fazer a prova, tirar nota.",
        "Time discipline: ate sexta, no prazo, as dez - deadlines in Portuguese.",
        "20 full sentences with translations: jobs, office, classroom, learning.",
    ],
    requirements=[
        "Write your own job or study description in five Portuguese sentences using this record's patterns.",
        "Learn your profession's Portuguese name by heart - you will say it often.",
    ],
    standards=[
        "CEFR A1-A2: work, professions, workplace, school, and study.",
        "Instituto Camoes Referencial: work and education objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Profession vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, work is the oath kept daily: the deadline "
              "is the promise signed, the report the testimony delivered, and the "
              "classroom the archive where the next generation signs its name. This "
              "Signature reading treats every profession as a covenant of craft."""),
)

E(
    key="portuguese_health_body", name="Portuguese Health and Body Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the body, the doctor, and the pharmacy - the
        record to learn before you need it. Estou com dor de cabeca. (I have a
        headache.) Minha garganta esta doendo. (My throat hurts.) Estou com
        febre desde ontem. (I have had a fever since yesterday.) Preciso de um
        medico. (I need a doctor.) Onde fica o hospital mais proximo? (Where
        is the nearest hospital?) Chame uma ambulancia, por favor. (Call an
        ambulance, please.) O medico receitou um remedio. (The doctor
        prescribed a medicine.) Tome este comprimido duas vezes ao dia. (Take
        this pill twice a day.) A farmacia abre aos domingos? (Is the pharmacy
        open on Sundays?) Estou alergico a penicilina. (I am allergic to
        penicillin.) Meu braco esta inchado. (My arm is swollen.) Ela torceu o
        tornozelo. (She twisted her ankle.) Beba muita agua e descanse. (Drink
        plenty of water and rest.) O coracao bate forte. (The heart beats
        fast.) Respire fundo, por favor. (Breathe deeply, please.) Vou fazer um
        exame de sangue. (I am going to have a blood test.) A consulta e
        amanha as nove. (The appointment is tomorrow at nine.) Estou me
        sentindo melhor hoje. (I am feeling better today.) Cuide da sua saude.
        (Take care of your health.) Saude e o maior tesouro. (Health is the
        greatest treasure.) Body words: cabeca, olho, ouvido, nariz, boca,
        garganta, ombro, braco, mao, dedo, perna, joelho, pe, coracao,
        estomago."""),
    how_it_works=textwrap.dedent("""\
        This record teaches health language in the order of an emergency:
        describing the symptom, asking for the doctor, understanding the
        prescription, and recovering. Each sentence is drilled as a pair -
        symptom and response - so the learner can both report and understand.
        The learner practices by describing their own body in Portuguese and
        rehearsing the three emergency sentences until they are instant. The
        demonstration program verifies all twenty sentences reassemble
        correctly, proving medical phrases in real syntax."""),
    key_points=[
        "Symptoms: dor de cabeca, febre, garganta doendo, inchado, torcido.",
        "Emergency trio: Preciso de um medico. Onde fica o hospital mais proximo? Chame uma ambulancia.",
        "Pharmacy: receitou um remedio, Tome este comprimido, Estou alergico a...",
        "Body parts from cabeca to pe - point and name them aloud.",
        "20 full sentences with translations: body parts, symptoms, doctor visit, pharmacy.",
    ],
    requirements=[
        "Memorize the emergency trio before traveling; rehearse them until instant.",
        "Learn your own allergies and conditions in Portuguese: Estou alergico a...",
    ],
    standards=[
        "CEFR A1-A2: body, health, illness, medical help, pharmacy.",
        "Instituto Camoes Referencial: health objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Anatomy and medical vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, the body is the first and final archive: "
              "every symptom a report filed, every prescription a signed order, and "
              "'cuide da sua saude' the standing oath of self-keeping. This Signature "
              "reading treats health language as the covenant of the body with itself."""),
)

E(
    key="portuguese_emotions", name="Portuguese Emotions and Feelings Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the inner life: joy, sadness, anger, fear, love,
        surprise. Estou muito feliz hoje! (I am very happy today!) Ela riu
        alto com a piada. (She laughed out loud at the joke.) Que alegria te
        ver! (What a joy to see you!) Estou triste com a noticia. (I am sad
        about the news.) Ele chorou de emocao. (He cried with emotion.)
        Sinto sua falta. (I miss you.) Estou com raiva dessa situacao. (I am
        angry about this situation.) Nao fique bravo comigo. (Do not be mad at
        me.) Isso me deixa nervoso. (That makes me nervous.) Estou com medo do
        escuro. (I am afraid of the dark.) Fique calmo, vai dar tudo certo.
        (Stay calm, everything will be fine.) Eu te amo de todo o coracao. (I
        love you with all my heart.) Ela esta apaixonada por ele. (She is in
        love with him.) Que surpresa maravilhosa! (What a wonderful surprise!)
        Nao acredito no que vejo! (I cannot believe what I see!) Estou
        orgulhoso de voce. (I am proud of you.) Tenho vergonha de falar em
        publico. (I am embarrassed to speak in public.) Estou cansado, preciso
        descansar. (I am tired, I need to rest.) Sinto-me em paz aqui. (I feel
        at peace here.) A vida e bela apesar de tudo. (Life is beautiful
        despite everything.) Emotion words: alegria, tristeza, raiva, medo,
        amor, surpresa, orgulho, vergonha, calma, saudade - and saudade, the
        untranslatable Portuguese longing for what is absent, deserves its own
        meditation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches feelings through the estar pattern - emotions are
        states, so they take estar, not ser: estou feliz, estou triste, estou
        com medo. Each sentence pairs the feeling with its cause, so the
        learner practices the full thought: Estou nervoso com a prova. The
        learner practices by naming their own feelings in Portuguese each
        morning. The demonstration program verifies all twenty sentences
        reassemble correctly, and its emotion classifier sorts them by feeling,
        proving the vocabulary in working order."""),
    key_points=[
        "Feelings take estar: estou feliz, estou triste, estou cansado - states, not identity.",
        "Saudade: the deep Portuguese longing for someone or something absent - no single English word.",
        "Sinto sua falta (I miss you) and estou com saudade are the language's emotional signature.",
        "Six families: happy, sad, angry, afraid, love, surprise - each with causes and responses.",
        "20 full sentences with translations covering the whole emotional range.",
    ],
    requirements=[
        "Each morning, say your feeling in Portuguese: Hoje estou... - make it a daily ritual.",
        "Learn saudade deeply; it is the most Portuguese word in the language.",
    ],
    standards=[
        "CEFR A1-A2: feelings, moods, and personal states.",
        "Instituto Camoes Referencial: expressing emotions as A2 objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Emotion vocabulary entries, including saudade.",
    ],
    sig_lens=("Through the Signature lens, feeling is the heart signing its state: "
              "estou feliz seals the joy, sinto sua falta files the absence, and "
              "saudade is the longest oath - love that keeps signing after the beloved "
              "is gone. This Signature reading treats emotion as the inner covenant "
              "made audible."""),
)

E(
    key="portuguese_nature_weather", name="Portuguese Nature and Weather Sentences",
    group="Themed sentences", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for animals, plants, seasons, and weather talk. O ceu
        esta azul hoje. (The sky is blue today.) Esta chovendo muito. (It is
        raining a lot.) Vai fazer sol amanha. (It will be sunny tomorrow.)
        Esta fazendo frio esta semana. (It is cold this week.) Que calor
        insuportavel! (What unbearable heat!) O vento esta forte. (The wind is
        strong.) A previsao diz que vai nevar. (The forecast says it will
        snow.) O arco-iris apareceu depois da chuva. (The rainbow appeared
        after the rain.) As arvores estao floridas na primavera. (The trees
        are in bloom in spring.) As folhas caem no outono. (The leaves fall in
        autumn.) O cachorro corre no parque. (The dog runs in the park.) O
        gato subiu na arvore. (The cat climbed the tree.) O passaro canta de
        manha. (The bird sings in the morning.) Vi uma borboleta no jardim. (I
        saw a butterfly in the garden.) O rio e fundo e perigoso. (The river
        is deep and dangerous.) A montanha esta coberta de neve. (The mountain
        is covered in snow.) A floresta e cheia de vida. (The forest is full
        of life.) O mar estava calmo ontem. (The sea was calm yesterday.)
        Cuidemos da natureza. (Let us take care of nature.) A natureza e a
        nossa casa comum. (Nature is our common home.) Nature words: sol, lua,
        estrela, nuvem, chuva, neve, vento, trovão, rio, mar, montanha,
        floresta, arvore, flor, animal, passaro, peixe."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nature through weather talk - the universal small
        talk - and the living world around it. Weather verbs are impersonal:
        chove, neva, faz sol, faz frio - no subject needed, a pattern the
        learner masters by describing each day's sky. Each sentence pairs an
        observation with its season or cause. The learner practices by
        describing the weather outside their window every morning in
        Portuguese. The demonstration program verifies all twenty sentences
        and checks the impersonal weather pattern against real examples."""),
    key_points=[
        "Weather verbs are impersonal: chove (it rains), faz sol, faz frio - no subject.",
        "Esta + gerund for ongoing weather: Esta chovendo muito.",
        "Seasons: primavera, verao, outono, inverno - with their signature sentences.",
        "Animals and plants in action sentences: O passaro canta, As arvores estao floridas.",
        "20 full sentences with translations: animals, plants, seasons, weather talk.",
    ],
    requirements=[
        "Describe the weather outside your window in Portuguese every morning for a week.",
        "Learn the impersonal pattern cold: chove, neva, faz sol, faz calor, faz frio.",
    ],
    standards=[
        "CEFR A1-A2: weather, seasons, animals, plants, environment.",
        "Instituto Camoes Referencial: nature and weather objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Weather and nature vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, weather is the sky filing its daily "
              "report: chove is the rain's signature, faz sol the sun's seal, and "
              "the changing seasons the year countersigning itself. This Signature "
              "reading treats nature talk as the oldest conversation of all."""),
)

E(
    key="portuguese_shopping", name="Portuguese Shopping and Money Sentences",
    group="Themed sentences", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the market, prices, bargaining, and paying. Quanto
        custa isto? (How much is this?) Custa vinte reais. (It costs twenty
        reais.) Esta muito caro! (That is very expensive!) Tem desconto a
        vista? (Is there a cash discount?) Posso pagar com cartao? (Can I pay
        by card?) Aceitam pix? (Do you accept Pix?) So tenho dinheiro. (I only
        have cash.) Pode embrulhar para presente? (Can you gift-wrap it?) Estou
        so olhando, obrigado. (I am just looking, thanks.) Voce tem um numero
        maior? (Do you have a bigger size?) Onde fica o provador? (Where is
        the fitting room?) Ficou perfeito em voce! (It looks perfect on you!)
        Vou levar este. (I will take this one.) Qual e o preco final? (What is
        the final price?) Faz por quinze? (Will you do it for fifteen?) Fechado!
        (Deal!) O troco esta errado. (The change is wrong.) Preciso da nota
        fiscal. (I need the receipt.) A loja fecha as seis. (The store closes
        at six.) Comprar com sabedoria e uma arte. (Shopping wisely is an
        art.) Money words: preco, desconto, troco, conta, cartao, dinheiro,
        caixa, recibo, oferta, promocao; currencies: real (Brazil), euro
        (Portugal)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches shopping as a negotiation script: ask the price,
        react, bargain, pay, and confirm. Each sentence is drilled in pairs -
        the buyer's line and the seller's line - so the learner can play both
        sides. The learner practices by role-playing a market scene with a
        partner or aloud alone. The demonstration program verifies all twenty
        sentences reassemble correctly and runs a price-bargaining calculator
        that matches the discount language taught here."""),
    key_points=[
        "The price script: Quanto custa? Esta caro! Tem desconto? Faz por quinze? Fechado!",
        "Paying: Posso pagar com cartao? Aceitam pix? So tenho dinheiro.",
        "Sizes and fitting: um numero maior, Onde fica o provador?",
        "Always check: O troco esta errado. Preciso da nota fiscal.",
        "20 full sentences with translations: market, prices, bargaining, paying.",
    ],
    requirements=[
        "Role-play a full purchase in Portuguese: greeting, price, bargain, payment, farewell.",
        "Learn your currency's name and the local payment words (pix in Brazil, multibanco in Portugal).",
    ],
    standards=[
        "CEFR A1-A2: shopping, prices, money, paying.",
        "Instituto Camoes Referencial: shopping objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Commerce vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, the bargain is the oldest negotiation: "
              "the price asked, the price offered, and 'fechado' the moment both "
              "hands sign. This Signature reading treats the market as the place "
              "where value itself is countersigned."""),
)

E(
    key="portuguese_friendship", name="Portuguese Friendship and Social Life Sentences",
    group="Themed sentences", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for meeting people, invitations, and celebrations.
        Prazer em conhece-lo! (Pleased to meet you!) De onde voce e? (Where
        are you from?) Eu sou do Brasil. (I am from Brazil.) Ha quanto tempo
        voce mora aqui? (How long have you lived here?) Voce vem sempre aqui?
        (Do you come here often?) Quer tomar um cafe comigo? (Want to have a
        coffee with me?) Vamos ao cinema sexta-feira? (Shall we go to the
        movies on Friday?) Faco aniversario sabado; venha! (It is my birthday
        Saturday; come!) Traga um amigo! (Bring a friend!) A festa foi
        otima! (The party was great!) Obrigado pelo convite! (Thanks for the
        invitation!) Foi bom te ver! (It was good to see you!) Vamos marcar
        alguma coisa! (Let us plan something!) Me passa seu numero? (Can I
        have your number?) Te ligo amanha! (I will call you tomorrow!) Voce e
        um otimo amigo. (You are a great friend.) Amigos sao a familia que
        escolhemos. (Friends are the family we choose.) Parabens pelo novo
        emprego! (Congratulations on the new job!) Saude e felicidade sempre!
        (Health and happiness always!) Ate a proxima! (Until next time!)
        Friendship words: amigo, convite, festa, aniversario, encontro,
        conversa, risada, abraco."""),
    how_it_works=textwrap.dedent("""\
        This record teaches social life as a chain of invitations: meet, ask,
        invite, celebrate, part, and plan the next meeting. Each sentence is a
        link the learner practices in sequence, building a full social
        encounter from Prazer em conhece-lo to Ate a proxima. The learner
        practices by introducing themselves to an imaginary new friend and
        carrying the conversation through an invitation. The demonstration
        program verifies all twenty sentences and checks the invitation chain
        order, proving social language in its natural sequence."""),
    key_points=[
        "The meeting chain: Prazer! De onde voce e? Ha quanto tempo mora aqui?",
        "Invitations: Quer tomar um cafe? Vamos ao cinema? Faco aniversario; venha!",
        "Celebrations: Parabens! A festa foi otima! Obrigado pelo convite!",
        "Parting warmly: Foi bom te ver! Vamos marcar alguma coisa! Ate a proxima!",
        "20 full sentences with translations: meeting people, invitations, celebrations.",
    ],
    requirements=[
        "Carry a full imaginary encounter aloud: meeting, invitation, farewell, next plan.",
        "Learn the birthday and congratulations phrases; you will use them often.",
    ],
    standards=[
        "CEFR A1-A2: introductions, invitations, social events, congratulations.",
        "Instituto Camoes Referencial: social interaction objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013.",
    ],
    sig_lens=("Through the Signature lens, friendship is the contract signed by "
              "choice: the invitation the offer, the acceptance the seal, and 'ate a "
              "proxima' the clause that keeps the bond open. This Signature reading "
              "treats every celebration as a renewal of the social covenant."""),
)

E(
    key="portuguese_technology", name="Portuguese Technology and Communication Sentences",
    group="Themed sentences", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the phone, the internet, the computer, and
        messaging. Meu celular descarregou. (My phone died.) Qual e a senha do
        wi-fi? (What is the wi-fi password?) A internet esta lenta hoje. (The
        internet is slow today.) Me manda o link, por favor. (Send me the
        link, please.) Vou te ligar mais tarde. (I will call you later.) Nao
        estou conseguindo te ouvir. (I cannot hear you.) A chamada caiu. (The
        call dropped.) Manda mensagem quando chegar. (Text me when you
        arrive.) Vi sua foto no perfil. (I saw your photo on the profile.) O
        computador travou de novo. (The computer froze again.) Preciso
        atualizar o aplicativo. (I need to update the app.) Esqueci minha
        senha. (I forgot my password.) O arquivo nao abriu. (The file did not
        open.) Salve o documento antes de sair. (Save the document before
        leaving.) A bateria esta acabando. (The battery is running out.)
        Coloque para carregar. (Put it on to charge.) O video esta
        carregando. (The video is loading.) Curti sua publicacao! (I liked
        your post!) Nao clique em links suspeitos. (Do not click suspicious
        links.) A tecnologia aproxima quem esta longe. (Technology brings
        together those who are far.) Tech words: celular, computador, tela,
        teclado, senha, aplicativo, arquivo, link, mensagem, chamada, video,
        bateria, carregador."""),
    how_it_works=textwrap.dedent("""\
        This record teaches technology as troubleshooting dialogue: report the
        problem, ask for help, follow the fix. Each sentence is a real line
        from digital life, drilled in problem-solution pairs: A internet esta
        lenta. / Reinicie o roteador. The learner practices by narrating their
        own device use in Portuguese. The demonstration program verifies all
        twenty sentences and runs a tech-support dialogue matcher that pairs
        problems with solutions from this record's vocabulary."""),
    key_points=[
        "Problem lines: descarregou, travou, caiu, esta lenta, esqueci minha senha.",
        "Help lines: Qual e a senha do wi-fi? Me manda o link. Manda mensagem quando chegar.",
        "Safety line: Nao clique em links suspeitos - learn it and live it.",
        "Device verbs: ligar, carregar, atualizar, salvar, clicar, curtir.",
        "20 full sentences with translations: phone, internet, computer, messaging.",
    ],
    requirements=[
        "Narrate your next hour of device use in Portuguese: Vou te ligar, O video esta carregando...",
        "Learn the password and wi-fi phrases; they unlock every cafe in the Portuguese-speaking world.",
    ],
    standards=[
        "CEFR A1-A2: technology, devices, internet, everyday digital communication.",
        "Instituto Camoes Referencial: digital communication objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Technology vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, the message is the voice extended: the "
              "link the bridge signed, the password the seal of the private archive, "
              "and every call the oath that distance will not silence us. This "
              "Signature reading treats technology as the covenant of connection."""),
)


E(
    key="portuguese_tenses", name="Portuguese Verb Tenses in Sentences",
    group="Grammar", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Portuguese verbs live in time: present, past, and future, each with its
        own endings. Present (now): Eu falo portugues. (I speak Portuguese.)
        Ela trabalha aqui. (She works here.) Nos estudamos juntos. (We study
        together.) Voce entende? (Do you understand?) Eles moram longe. (They
        live far away.) Preterite, the completed past: Eu falei com ela ontem.
        (I spoke with her yesterday.) Nos comemos pizza. (We ate pizza.) Ele
        abriu a porta. (He opened the door.) Ela foi ao mercado. (She went to
        the market.) Eles disseram a verdade. (They told the truth.) Imperfect,
        the habitual past: Quando eu era crianca, jogava bola. (When I was a
        child, I used to play ball.) Nos iamos a praia todo verao. (We used
        to go to the beach every summer.) Chovia muito naquela epoca. (It used
        to rain a lot back then.) Future: Eu viajarei em julho. (I will travel
        in July.) Nos nos veremos amanha. (We will see each other tomorrow.)
        Sera um dia lindo. (It will be a beautiful day.) Eles chegarao cedo.
        (They will arrive early.) Voce vai gostar. (You are going to like it -
        the everyday ir + infinitive future.) Conditional (would): Eu gostaria
        de um cafe. (I would like a coffee.) Voce poderia ajudar? (Could you
        help?) Seria otimo te ver. (It would be great to see you.) Key
        irregulars: ser (sou, fui, era, serei), estar (estou, estive, estava,
        estarei), ter (tenho, tive, tinha, terei), ir (vou, fui, ia, irei).
        Regular -ar endings: present -o/-as/-a/-amos/-am; preterite
        -ei/-aste/-ou/-amos/-aram; future -arei/-aras/-ara/-aremos/-arao. Five
        sentences per tense, drilled aloud, and time itself speaks Portuguese."""),
    how_it_works=textwrap.dedent("""\
        This record teaches tenses by conjugation tables plus sentences: the
        learner conjugates falar, comer, and abrir through present, preterite,
        imperfect, and future, then reads five real sentences per tense. The
        irregular verbs ser, estar, ter, and ir get their own tables, learned
        by heart. The tense drill in the demonstration program generates the
        full tables from the infinitive and checks every form against the
        tables taught in this entry - the program and the page verify each
        other, form by form. The everyday future with ir + infinitive (vou
        viajar) is drilled alongside the formal future (viajarei)."""),
    key_points=[
        "Present: -o/-as/-a/-amos/-am for -ar verbs (falo, falas, fala, falamos, falam).",
        "Preterite (completed past): -ei/-aste/-ou/-amos/-aram (falei, falaste, falou, falamos, falaram).",
        "Imperfect (habitual past): -ava/-avas/-ava/-avamos/-avam (falava...).",
        "Future: infinitive + -ei/-as/-a/-emos/-ao (falarei...); everyday speech uses ir + infinitive (vou falar).",
        "Conditional (would): -ia endings (falaria); polite requests live here: gostaria, poderia.",
        "Irregular cores: ser, estar, ter, ir - full tables in this record, memorized by heart.",
    ],
    requirements=[
        "Conjugate one regular verb of each family through all four tenses aloud before moving on.",
        "Write ten personal sentences: five in the preterite (yesterday), five in the future (tomorrow).",
    ],
    standards=[
        "CEFR A2-B1: present, preterite, imperfect, future, and conditional of high-frequency verbs.",
        "Instituto Camoes Referencial: tense objectives across A2 and B1.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Verb tenses and moods.",
        "Mateus M H M et al. Gramatica da Lingua Portuguesa. Caminho; 2006.",
    ],
    sig_lens=("Through the Signature lens, tense is time signing the verb: the "
              "present seals what is, the preterite files what was done, the future "
              "promises what will be, and the conditional drafts what would be. This "
              "Signature reading treats every conjugation as a dated entry in the "
              "archive of action."),
)

E(
    key="portuguese_qa", name="Portuguese Questions and Answers",
    group="Grammar", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty question-and-answer pairs covering who, what, where, when, why,
        and how. Quem e voce? Eu sou a Ana. (Who are you? I am Ana.) O que e
        isso? E um presente. (What is this? It is a gift.) Onde voce mora? Moro
        em Lisboa. (Where do you live? I live in Lisbon.) Quando voce chegou?
        Cheguei ontem. (When did you arrive? I arrived yesterday.) Por que voce
        esta triste? Porque perdi o onibus. (Why are you sad? Because I missed
        the bus.) Como voce vai? Vou bem, obrigado. (How are you? I am well,
        thanks.) Qual e o seu nome? Meu nome e Pedro. (What is your name? My
        name is Pedro.) Quantos anos voce tem? Tenho trinta anos. (How old are
        you? I am thirty.) Quanto custa? Custa cinquenta reais. (How much is
        it? It costs fifty reais.) Que horas sao? Sao tres horas. (What time is
        it? It is three o'clock.) De onde voce e? Sou do Rio. (Where are you
        from? I am from Rio.) Para onde voce vai? Vou para casa. (Where are
        you going? I am going home.) Com quem voce veio? Vim com minha irma.
        (Who did you come with? I came with my sister.) O que voce faz? Sou
        professor. (What do you do? I am a teacher.) Como se diz isso em
        portugues? Diz-se 'obrigado'. (How do you say that in Portuguese? You
        say 'obrigado'.) Qual e o problema? O carro nao liga. (What is the
        problem? The car will not start.) Quando e seu aniversario? E em maio.
        (When is your birthday? It is in May.) Por que nao? Porque nao quero.
        (Why not? Because I do not want to.) Voce entendeu? Entendi tudo.
        (Did you understand? I understood everything.) Pode repetir? Claro:
        quem, o que, onde... (Can you repeat? Of course: who, what, where...)
        The question words: quem, o que, qual, onde, quando, por que, como,
        quanto - eight keys that open every conversation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches questions as pairs: the learner asks, then answers,
        alternating roles aloud. Each of the eight question words gets at
        least two pairs, so the pattern of each - quem asks people, onde asks
        places, por que asks reasons - becomes instinct. The learner practices
        by interviewing an imaginary friend with all twenty questions. The
        question-word classifier in the demonstration program sorts each
        question of this entry by its interrogative, proving the eight keys
        each open the right door."""),
    key_points=[
        "Eight question words: quem (who), o que (what), qual (which), onde (where), quando (when), por que (why), como (how), quanto (how much).",
        "Por que (why) vs porque (because) - the space changes the meaning.",
        "Questions need no word-order change: rising intonation does the work - Voce vem?",
        "Como se diz...? (How do you say...?) is the learner's master key.",
        "20 question/answer pairs with translations covering who/what/where/when/why/how.",
    ],
    requirements=[
        "Practice each pair both ways: ask the question, then answer it, aloud.",
        "Use Como se diz...? on five real objects around you today.",
    ],
    standards=[
        "CEFR A1-A2: asking and answering with all interrogatives.",
        "Instituto Camoes Referencial: question formation objectives.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Interrogatives.",
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
    ],
    sig_lens=("Through the Signature lens, the question is the summons and the "
              "answer the testimony: quem calls the witness, onde fixes the place, "
              "por que demands the cause, and every answered pair closes a case. "
              "This Signature reading treats the twenty pairs as twenty hearings "
              "of the court of conversation."),
)

E(
    key="portuguese_commands", name="Portuguese Commands and Requests",
    group="Grammar", ladder_rank=10, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty imperative and polite-request sentences, formal versus informal.
        Informal (tu, friends and family): Fala mais alto! (Speak louder!)
        Come a salada! (Eat the salad!) Abre a porta! (Open the door!) Nao
        fale assim! (Do not talk like that! - negative uses the subjunctive.)
        Vem ca! (Come here!) Formal (voce, strangers and elders): Fale mais
        alto, por favor. (Speak louder, please.) Coma a salada. (Eat the
        salad.) Abra a porta. (Open the door.) Nao fale assim. (Do not talk
        like that.) Venha ca, por favor. (Come here, please.) Polite requests
        anyone can use: Pode me ajudar? (Can you help me?) Voce poderia repetir?
        (Could you repeat?) Me da um minuto? (Give me a minute? - informal.)
        O senhor poderia me dar uma informacao? (Could you give me some
        information? - very formal.) Com licenca, por favor. (Excuse me,
        please.) Desculpe o incomodo. (Sorry for the bother.) Faca o favor de
        sentar-se. (Please have a seat - formal.) Sente-se aqui. (Sit here -
        informal.) Nao se preocupe. (Do not worry.) Tenha um bom dia! (Have a
        good day! - formal.) The rule: affirmative tu imperative takes the
        ele/ela present form minus nothing - fala, come, abre; formal voce
        imperative takes the subjunctive - fale, coma, abra; negatives always
        take the subjunctive. Politeness in Portuguese is grammar, not just
        manners."""),
    how_it_works=textwrap.dedent("""\
        This record teaches commands as a formality ladder: tu for intimates,
        voce for respect, o senhor/a senhora for high formality, and the
        conditional (poderia, gostaria) for the politest requests. The learner
        converts each command up and down the ladder - Fala! becomes Fale,
        por favor, becomes O senhor poderia falar? - feeling the grammar of
        respect. The imperative drill in the demonstration program generates
        affirmative and negative imperatives from the infinitive and checks
        them against the forms taught here, proving the rule on real verbs."""),
    key_points=[
        "Affirmative tu imperative = ele/ela present form: fala, come, abre.",
        "Voce imperative = present subjunctive: fale, coma, abra - add por favor for politeness.",
        "All negative imperatives use the subjunctive: nao fale, nao coma, nao abra.",
        "Polite requests climb: Pode...? -> Voce poderia...? -> O senhor poderia...?",
        "20 imperative and polite-request sentences, formal vs informal, with translations.",
    ],
    requirements=[
        "Convert five commands from tu to voce form and back, aloud, until the pattern is instant.",
        "Practice the polite request ladder on one request: Pode...? Poderia...? O senhor poderia...?",
    ],
    standards=[
        "CEFR A2: imperative mood, formal vs informal address.",
        "Instituto Camoes Referencial: imperative and politeness objectives.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. The imperative mood.",
        "Mateus M H M et al. Gramatica da Lingua Portuguesa. Caminho; 2006.",
    ],
    sig_lens=("Through the Signature lens, the command is the order signed by "
              "authority and the polite request the petition sealed with respect: "
              "fala commands the friend, fale petitions the stranger, and poderia "
              "bows the lowest. This Signature reading treats formality as the "
              "protocol of the spoken court."),
)

E(
    key="portuguese_descriptions", name="Portuguese Descriptions of People and Places",
    group="Themed sentences", ladder_rank=10, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences describing people, places, and things in detail. Ela
        e alta, magra, de cabelos castanhos e olhos verdes. (She is tall,
        slim, with brown hair and green eyes.) Ele tem barba e usa oculos.
        (He has a beard and wears glasses.) O bebe tem bochechas rosadas.
        (The baby has rosy cheeks.) Minha avo tem cabelos brancos e um sorriso
        doce. (My grandmother has white hair and a sweet smile.) Lisboa e uma
        cidade antiga cheia de charme. (Lisbon is an old city full of charm.)
        O Rio tem praias deslumbrantes e montanhas verdes. (Rio has stunning
        beaches and green mountains.) A casa e ampla, arejada e muito
        iluminada. (The house is spacious, airy, and very bright.) O quarto e
        pequeno mas aconchegante. (The room is small but cozy.) O jardim esta
        cheio de flores coloridas. (The garden is full of colorful flowers.)
        A praia estava deserta ao amanhecer. (The beach was deserted at dawn.)
        O restaurante e elegante e a comida e refinada. (The restaurant is
        elegant and the food is refined.) O mercado e barulhento e cheio de
        cores. (The market is noisy and full of colors.) A montanha e
        imponente e coberta de neve. (The mountain is imposing and covered in
        snow.) O rio e largo e as aguas sao cristalinas. (The river is wide
        and the waters are crystal clear.) O ceu noturno estava estrelado.
        (The night sky was starry.) A festa foi animada e cheia de musica.
        (The party was lively and full of music.) O filme foi emocionante do
        comeco ao fim. (The movie was thrilling from start to finish.) O livro
        e fascinante e facil de ler. (The book is fascinating and easy to
        read.) Descrever bem e pintar com palavras. (To describe well is to
        paint with words.) Description stacks adjectives after the noun, each
        agreeing: uma cidade antiga cheia de charme."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description by stacking: the learner takes a
        person or place and adds adjectives one by one, each agreeing with its
        noun - alta, magra, de cabelos castanhos. Each sentence is a model the
        learner imitates on their own subjects: their street, their friend,
        their room. The agreement checker in the demonstration program verifies
        that every adjective in these twenty sentences matches its noun in
        gender and number, proving the description rules on real text. Detail
        is built, not born: one agreeing adjective at a time."""),
    key_points=[
        "People: ser + adjectives for lasting traits (e alta), ter + nouns for features (tem barba).",
        "Places: ser for character (e antiga), estar for temporary states (estava deserta).",
        "Adjectives stack after the noun, all agreeing: flores coloridas, aguas cristalinas.",
        "De-phrases add detail without agreement: de cabelos castanhos, de neve.",
        "20 detailed descriptive sentences with translations: people, places, things.",
    ],
    requirements=[
        "Describe three real people and three real places in Portuguese, four adjectives each.",
        "Check every adjective agrees; the demo's agreement checker shows the standard.",
    ],
    standards=[
        "CEFR A2-B1: detailed description of people, places, and objects.",
        "Instituto Camoes Referencial: description objectives.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Adjective agreement.",
        "Dicionario Houaiss da Lingua Portuguesa. Descriptive vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, description is the portrait signed in "
              "words: each agreeing adjective a brushstroke, each de-phrase a "
              "shading, and the finished sentence the likeness sealed. This "
              "Signature reading treats the twenty sentences as twenty portraits "
              "in the gallery of the language."),
)

E(
    key="portuguese_story1", name="Portuguese Story I: A New Morning",
    group="Stories", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the present tense, with line-by-line English
        translation - the learner's first full narrative. O sol nasce sobre a
        cidade. (The sun rises over the city.) Ana acorda cedo todos os dias.
        (Ana wakes up early every day.) Ela toma banho e veste a roupa de
        trabalho. (She showers and puts on her work clothes.) O cheiro do cafe
        enche a cozinha. (The smell of coffee fills the kitchen.) Ela come pao
        com manteiga e bebe suco de laranja. (She eats bread with butter and
        drinks orange juice.) O onibus chega as sete e meia. (The bus arrives
        at seven thirty.) Ana cumprimenta o motorista com um sorriso. (Ana
        greets the driver with a smile.) A cidade desperta devagar. (The city
        wakes up slowly.) No escritorio, os colegas ja trabalham. (At the
        office, her colleagues are already working.) Cada manha e uma nova
        chance. (Every morning is a new chance.) Read the Portuguese first,
        guess the meaning, then check the translation - the story teaches
        itself. Every verb is present tense; every sentence is short; every
        line is a small victory."""),
    how_it_works=textwrap.dedent("""\
        This record teaches narrative by immersion: ten connected sentences,
        one morning, present tense throughout. The learner reads the Portuguese
        line, covers the translation, guesses, then uncovers - training the
        eye to trust Portuguese first. Then the learner retells the story
        aloud without looking, and finally writes their own morning in ten
        Portuguese sentences. The story checker in the demonstration program
        verifies ten sentences, counts the words, and confirms the present
        tense pattern taught here, proving the narrative on real text."""),
    key_points=[
        "Ten sentences, one continuous morning, all present tense - the simplest full narrative.",
        "Line-by-line translation trains Portuguese-first reading: guess, then check.",
        "Daily-routine verbs drilled in context: acordar, tomar banho, vestir, comer, chegar, cumprimentar.",
        "Retell the story aloud, then write your own morning in ten sentences.",
    ],
    requirements=[
        "Read the story aloud three times: Portuguese only, then with translations, then Portuguese only again.",
        "Write your own ten-sentence morning story using this story's verbs.",
    ],
    standards=[
        "CEFR A2: understanding and producing simple connected narrative text.",
        "Instituto Camoes Referencial: narrative objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013.",
    ],
    sig_lens=("Through the Signature lens, the story is the day's first filing: ten "
              "sentences, ten entries, each sealing a moment of the morning into the "
              "archive. This Signature reading treats Ana's morning as the template "
              "every learner's own story will follow."),
)

E(
    key="portuguese_story2", name="Portuguese Story II: The Journey",
    group="Stories", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the past tense, with line-by-line English
        translation. No ano passado, Pedro fez uma grande viagem. (Last year,
        Pedro took a great trip.) Ele comprou as passagens com meses de
        antecedencia. (He bought the tickets months in advance.) O aviao
        decolou numa manha de sabado. (The plane took off on a Saturday
        morning.) Pedro olhou pela janela e viu as nuvens. (Pedro looked out
        the window and saw the clouds.) Ele chegou a Lisboa a tarde. (He
        arrived in Lisbon in the afternoon.) Um amigo o esperava no aeroporto.
        (A friend was waiting for him at the airport.) Eles jantaram num
        restaurante tipico. (They had dinner at a typical restaurant.) Pedro
        provou o bacalhau e adorou. (Pedro tried the salt cod and loved it.)
        Nos dias seguintes, ele visitou museus e castelos. (In the following
        days, he visited museums and castles.) Foi a melhor viagem da sua
        vida. (It was the best trip of his life.) Preterite carries the
        completed actions - comprou, decolou, chegou - while the imperfect
        paints the background - esperava. Read, guess, check, retell: the past
        becomes yours."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the past through Pedro's journey: the preterite
        for what happened (comprou, decolou, chegou, provou) and the imperfect
        for the background (esperava). The learner reads each line, notes which
        past each verb uses, and feels the difference: completed action versus
        ongoing scene. Then the learner retells the journey aloud and writes
        their own ten-sentence past story - a real trip they took. The story
        checker in the demonstration program verifies ten sentences and
        confirms the past-tense pattern, proving the narrative on real text."""),
    key_points=[
        "Ten sentences, one completed journey, past tenses throughout.",
        "Preterite = completed actions: comprou, decolou, chegou, provou, foi.",
        "Imperfect = background and habit: esperava, visitava.",
        "Line-by-line translation; retell aloud, then write your own past story in ten sentences.",
    ],
    requirements=[
        "Mark every verb in the story as preterite or imperfect before retelling it.",
        "Write your own ten-sentence past story about a real trip or event.",
    ],
    standards=[
        "CEFR A2-B1: past narration with preterite and imperfect contrast.",
        "Instituto Camoes Referencial: past narrative objectives.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Preterite vs imperfect.",
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
    ],
    sig_lens=("Through the Signature lens, the past-tense story is the archive of "
              "what was done: the preterite files each completed act, the imperfect "
              "keeps the background open, and Pedro's journey becomes a sealed "
              "record. This Signature reading treats memory itself as the testimony "
              "the past signs."),
)

E(
    key="portuguese_story3", name="Portuguese Story III: Tomorrow's Promise",
    group="Stories", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the future and conditional, with line-by-line
        English translation. Amanha, Maria comecara um novo capitulo. (Tomorrow,
        Maria will begin a new chapter.) Ela acordara antes do nascer do sol.
        (She will wake before sunrise.) Tomara cafe com a familia e saira
        cedo. (She will have coffee with her family and leave early.) No
        trabalho, apresentara seu grande projeto. (At work, she will present
        her big project.) Os colegas aplaudirao de pe. (Her colleagues will
        applaud standing.) Depois, ela ligara para a mae. (Afterward, she will
        call her mother.) A noite, jantara com os amigos para comemorar. (At
        night, she will have dinner with friends to celebrate.) Se tudo der
        certo, viajara no verao. (If all goes well, she will travel in the
        summer.) Seria maravilhoso conhecer o mundo. (It would be wonderful to
        see the world.) O futuro pertence a quem se prepara hoje. (The future
        belongs to those who prepare today.) The formal future (-ara, -era,
        -ira) carries the promises; the conditional (seria) carries the dream.
        Read, guess, check, retell - and then promise your own tomorrow in
        ten sentences."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the future through Maria's promised day: the formal
        future endings (-ara, -era, -ira) on every promise, the conditional
        for the dream (seria maravilhoso), and the everyday ir + infinitive
        noted as the spoken alternative. The learner reads, marks each future
        form, and converts three sentences to the spoken vai + infinitive
        form. Then the learner writes their own ten-sentence tomorrow. The
        story checker in the demonstration program verifies ten sentences and
        confirms the future/conditional pattern taught here."""),
    key_points=[
        "Ten sentences, one promised day, future and conditional throughout.",
        "Formal future: infinitive + -ei/-as/-a/-emos/-ao (comecara, apresentara, viajara).",
        "Conditional for dreams and politeness: seria maravilhoso.",
        "Spoken alternative: ir + infinitive (vai comecar) - convert three sentences as drill.",
        "Line-by-line translation; retell, then write your own ten-sentence future.",
    ],
    requirements=[
        "Mark every future and conditional form in the story before retelling it.",
        "Write your own ten-sentence tomorrow: five promises, five dreams.",
    ],
    standards=[
        "CEFR B1: future and conditional in narration.",
        "Instituto Camoes Referencial: future and conditional objectives.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Future and conditional.",
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
    ],
    sig_lens=("Through the Signature lens, the future-tense story is the promise "
              "signed in advance: each -ara a vow, the conditional the dream "
              "clause, and Maria's tomorrow a contract with herself. This Signature "
              "reading treats every future sentence as a promissory note of the "
              "soul."),
)

E(
    key="portuguese_idioms", name="Portuguese Idioms and Proverbs",
    group="Register and style", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty idioms and proverbs with literal translation, real meaning, and
        an example sentence - the soul of the language. Cao que ladra nao
        morde. (Barking dog does not bite - literal.) People who threaten
        rarely act. Example: Nao tenha medo dele; cao que ladra nao morde.
        Em boca fechada nao entra mosca. (A fly does not enter a closed mouth.)
        Silence avoids trouble. A pressa e inimiga da perfeicao. (Haste is the
        enemy of perfection.) Slow down to do well. Quem tem boca vai a Roma.
        (Who has a mouth goes to Rome.) Ask and you will find your way. Agua
        mole em pedra dura tanto bate ate que cansa. (Soft water on hard stone
        hits until it tires.) Persistence wins. Fazer das tripas coracao. (To
        make heart from guts.) To summon courage from fear. Meter a colher.
        (To stick in the spoon.) To meddle. Chutar o balde. (To kick the
        bucket - the Brazilian way.) To give up. Quebrar o gelo. (To break the
        ice.) Custar os olhos da cara. (To cost the eyes of the face.) Very
        expensive. Ter borboletas na barriga. (To have butterflies in the
        belly.) Nervous excitement. Matar dois coelhos com uma cajadada so.
        (To kill two rabbits with one stick.) Two birds, one stone. De grao
        em grao a galinha enche o papo. (Grain by grain the hen fills her
        crop.) Little by little. Em terra de cego quem tem olho e rei. (In
        the land of the blind, who has an eye is king.) O barato sai caro.
        (The cheap comes out expensive.) Antes tarde do que nunca. (Better
        late than never.) Casa de ferreiro, espeto de pau. (In the blacksmith's
        house, a wooden skewer.) The cobbler's children go barefoot. Quem
        semeia vento colhe tempestade. (Who sows wind reaps storm.) Actions
        have consequences. Aprenda um por dia e em vinte dias voce fala como
        um nativo. (Learn one a day and in twenty days you will speak like a
        native.)"""),
    how_it_works=textwrap.dedent("""\
        This record teaches idioms in three layers: the literal translation
        (often funny), the real meaning (always practical), and a sentence
        showing it alive. The learner studies one idiom, says the literal
        version, explains the real meaning in their own words, then uses it in
        a new sentence. The idiom quiz in the demonstration program tests
        literal-to-meaning matching on all twenty, exactly as taught here.
        One idiom a day for twenty days turns a student into a storyteller."""),
    key_points=[
        "Every idiom: literal translation + real meaning + example sentence.",
        "Proverbs teach culture: persistence (agua mole), prudence (em boca fechada), consequence (quem semeia vento).",
        "Brazilian color: chutar o balde, meter a colher, custar os olhos da cara.",
        "Use idioms sparingly in speech - one per conversation is plenty.",
        "20 idioms and proverbs, fully glossed with example sentences.",
    ],
    requirements=[
        "Learn one idiom per day; use each in a real or written sentence the same day.",
        "Never translate idioms word-for-word into English - learn the meaning, not the words.",
    ],
    standards=[
        "CEFR B1-B2: idiomatic expressions and proverbs.",
        "Instituto Camoes Referencial: idiomatic language objectives.",
    ],
    citations=[
        "Dicionario Houaiss da Lingua Portuguesa. Idiom and proverb entries.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013.",
    ],
    sig_lens=("Through the Signature lens, the proverb is the people's sealed "
              "wisdom: short enough to remember, true enough to sign, passed from "
              "mouth to mouth like a contract no one wrote but everyone keeps. This "
              "Signature reading treats the twenty sayings as twenty clauses of the "
              "popular constitution."),
)

E(
    key="portuguese_registers", name="Portuguese Formal and Polite Registers",
    group="Register and style", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen formal-versus-informal pairs for letters, business, and elders.
        Informal: Oi, tudo bem? / Formal: Olá, como vai o senhor? (Hi, all
        good? / Hello, how are you, sir?) Informal: Valeu pela ajuda! /
        Formal: Muito obrigado pela sua ajuda. (Thanks for the help! / Thank
        you very much for your help.) Informal: Me manda isso depois. /
        Formal: Poderia me enviar isso depois? (Send me that later. / Could
        you send me that later?) Informal: Nao entendi. / Formal: Perdao, nao
        compreendi bem. (I did not get it. / Pardon, I did not quite
        understand.) Informal: Que horas voce sai? / Formal: A que horas o
        senhor sai? (What time do you leave? / At what time do you leave,
        sir?) Informal: Fala serio! / Formal: O senhor esta brincando? (No
        way! / Are you joking, sir?) Informal: To sem tempo. / Formal: No
        momento estou sem disponibilidade. (I have no time. / At the moment I
        am unavailable.) Informal: Manda um abraco pra ela. / Formal: Transmita
        os meus cumprimentos a ela. (Give her a hug. / Convey my regards to
        her.) Informal: Foi mal. / Formal: Pec o desculpas. (My bad. / I
        apologize.) Informal: Que legal! / Formal: Que interessante! (How
        cool! / How interesting!) Informal: Tchau, ate mais! / Formal:
        Atenciosamente, ate breve. (Bye, see you! / Sincerely, see you soon.)
        Informal: Preciso disso pra ontem. / Formal: Precisaria disso com a
        maior brevidade possivel. (I need this like yesterday. / I would need
        this as soon as possible.) Informal: Da pra fazer? / Formal: Seria
        possivel fazer? (Can it be done? / Would it be possible?) Informal:
        Beleza, combinado. / Formal: Perfeito, fica assim combinado. (Great,
        agreed. / Perfect, agreed.) Informal: E ai, novidades? / Formal: Como
        tem passado? (Hey, anything new? / How have you been?) Formal writing
        uses o senhor/a senhora, the conditional (poderia, seria), and full
        forms (estou, para) where speech contracts (to, pra). Choose the
        register before you choose the words."""),
    how_it_works=textwrap.dedent("""\
        This record teaches register as a choice with consequences: the learner
        takes each informal sentence and rewrites it formal, noticing the
        three tools of formality - o senhor/a senhora address, the conditional
        mood (poderia, seria, precisaria), and uncontracted forms (estou, para
        instead of to, pra). Business letters, job interviews, and elders get
        the formal; friends get the informal; mixing them is the mark of the
        outsider. The register sorter in the demonstration program classifies
        each pair of this entry as formal or informal, proving the distinction
        on real examples."""),
    key_points=[
        "Three tools of formality: o senhor/a senhora, the conditional (poderia, seria), full uncontracted forms.",
        "Tu/vce informal with friends; o senhor/a senhora with elders, clients, and officials.",
        "Business letters close with Atenciosamente; friends close with Abracos.",
        "Never use slang (to, pra, valeu, foi mal) with officials or in job interviews.",
        "15 formal vs informal pairs with translations: letters, business, elders.",
    ],
    requirements=[
        "Rewrite five informal sentences from your own speech into formal register.",
        "Draft one formal email in Portuguese: greeting, request with poderia, closing with Atenciosamente.",
    ],
    standards=[
        "CEFR B1-B2: sociolinguistic appropriateness and register.",
        "Instituto Camoes Referencial: register objectives.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Forms of address.",
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
    ],
    sig_lens=("Through the Signature lens, register is the dress code of the "
              "contract: the informal signs among friends, the formal seals "
              "before witnesses, and the conditional bows before authority. This "
              "Signature reading treats the fifteen pairs as fifteen protocols of "
              "the court of speech."),
)

E(
    key="portuguese_complex", name="Portuguese Compound and Complex Sentences",
    group="Register and style", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen long sentences with clauses, connectors, and relative clauses -
        parsed and translated. Eu estudo portugues porque quero trabalhar no
        Brasil. (I study Portuguese because I want to work in Brazil -
        cause: porque.) Embora estivesse cansado, ele terminou o relatorio.
        (Although he was tired, he finished the report - concession: embora +
        subjunctive.) Quando cheguei, ela ja tinha saido. (When I arrived, she
        had already left - time: quando.) Se chover, ficaremos em casa. (If it
        rains, we will stay home - condition: se.) O livro que voce me deu e
        otimo. (The book that you gave me is great - relative: que.) A cidade
        onde nasci e pequena. (The city where I was born is small - relative:
        onde.) Ele fala tao rapido que ninguem entende. (He speaks so fast
        that nobody understands - consequence: tao...que.) Ela e nao so
        inteligente mas tambem gentil. (She is not only intelligent but also
        kind - correlation: nao so...mas tambem.) Depois que terminarmos,
        vamos comemorar. (After we finish, we will celebrate - time: depois
        que.) Antes de sair, apague as luzes. (Before leaving, turn off the
        lights - time: antes de + infinitive.) Ele trabalha tanto durante o
        dia que dorme cedo. (He works so much during the day that he sleeps
        early.) Nao sei se ele vem amanha. (I do not know if he is coming
        tomorrow - indirect question: se.) Dizem que o filme e excelente.
        (They say the movie is excellent - reported: que.) Quanto mais estudo,
        mais aprendo. (The more I study, the more I learn - proportion: quanto
        mais...mais.) Faca o que eu digo, nao o que eu faco. (Do what I say,
        not what I do - relative: o que.) Master the connectors - porque,
        embora, quando, se, que, onde, para, depois que, antes de - and long
        sentences assemble themselves."""),
    how_it_works=textwrap.dedent("""\
        This record teaches complex sentences as clause architecture: the
        learner takes each long sentence, finds the connector, and splits the
        sentence into its clauses - main and subordinate - naming the relation:
        cause, concession, time, condition, consequence. Then the learner
        rebuilds the sentence from the clauses, and finally builds their own
        complex sentence with each connector. The clause counter in the
        demonstration program splits these fifteen sentences at their
        connectors and counts the clauses, proving the architecture on real
        text. Fifteen connectors, fifteen sentences, one new power: saying two
        thoughts as one."""),
    key_points=[
        "Connectors and their clauses: porque (cause), embora + subjunctive (concession), quando (time), se (condition).",
        "Relatives: que (that), onde (where), o que (what) - they glue clauses to nouns.",
        "Correlatives: nao so...mas tambem, tao...que, quanto mais...mais.",
        "Antes de + infinitive; depois que + subjunctive - the time pair.",
        "15 long sentences, parsed by clause and connector, with translations.",
    ],
    requirements=[
        "Split five sentences into clauses and name each connector's job before rebuilding them.",
        "Write one complex sentence with each of: porque, embora, se, quando, que.",
    ],
    standards=[
        "CEFR B1-B2: complex sentences, subordination, connectors.",
        "Instituto Camoes Referencial: complex syntax objectives.",
    ],
    citations=[
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013. Subordination.",
        "Mateus M H M et al. Gramatica da Lingua Portuguesa. Caminho; 2006.",
    ],
    sig_lens=("Through the Signature lens, the complex sentence is the contract "
              "with clauses: the main clause the principal agreement, each "
              "subordinate clause a condition, exception, or consequence, and the "
              "connector the article number binding them. This Signature reading "
              "treats subordination as the fine print made beautiful."),
)

E(
    key="portuguese_dialogue_market", name="Portuguese Conversation at the Market",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue at the market, annotated. [Vendor
        greets] Vendedor: Bom dia! O que vai querer hoje? (Good morning! What
        will you have today?) [Customer greets back] Cliente: Bom dia! Quero
        frutas e verduras. (Good morning! I want fruit and vegetables.)
        [Asking price] Vendedor: As macas estao otimas. Quer provar uma? (The
        apples are great. Want to taste one?) [Tasting] Cliente: Hum, docinha!
        Quanto custa o quilo? (Hmm, sweet! How much per kilo?) [Price] Vendedor:
        Oito reais o quilo. (Eight reais per kilo.) [Reacting] Cliente: Esta
        caro. Faz por seis? (That is expensive. Will you do six?) [Bargaining]
        Vendedor: Por seis nao da. Faco por sete. (Six I cannot do. I will do
        seven.) [Agreeing] Cliente: Fechado! Me da dois quilos. (Deal! Give me
        two kilos.) [Adding items] Vendedor: Mais alguma coisa? Os tomates
        estao bonitos. (Anything else? The tomatoes are nice.) [Choosing]
        Cliente: Me da um quilo de tomate tambem. (Give me a kilo of tomatoes
        too.) [Weighing] Vendedor: Pronto. Deu quinze reais no total. (Done.
        Fifteen reais total.) [Paying] Cliente: Posso pagar com cartao? (Can I
        pay by card?) [Confirming] Vendedor: Claro! Aproxime o cartao. (Of
        course! Tap the card.) [Receipt] Cliente: Preciso da nota, por favor.
        (I need the receipt, please.) [Bagging] Vendedor: Aqui esta. Quer
        sacola? (Here it is. Want a bag?) [Thanks] Cliente: Nao, obrigado.
        Trouxe a minha. (No, thanks. I brought mine.) [Farewell] Vendedor:
        Obrigado pela preferencia! Volte sempre! (Thanks for shopping here!
        Come back anytime!) [Leaving] Cliente: Ate sabado que vem! (See you
        next Saturday!) [Aside] Vendedor: Ate logo! (See you!) Every line is a
        tool: greeting, tasting, pricing, bargaining, paying, thanking."""),
    how_it_works=textwrap.dedent("""\
        This record teaches conversation as a script with stage directions:
        each line is tagged with its move - greeting, asking, bargaining,
        paying - so the learner sees the anatomy of a market exchange. The
        learner reads both roles aloud, then plays the scene with a partner,
        then improvises the same scene with different products. The dialogue
        checker in the demonstration program verifies twenty lines with
        alternating speakers and matches each line to its conversational move,
        proving the script on real dialogue."""),
    key_points=[
        "The market script: greet, taste, ask price, bargain, agree, add items, pay, thank, part.",
        "Bargaining core: Esta caro. Faz por seis? Fechado!",
        "Paying: Posso pagar com cartao? Preciso da nota, por favor.",
        "Every line annotated with its conversational move and English translation.",
        "20-line bilingual dialogue; perform it, then improvise it with new products.",
    ],
    requirements=[
        "Perform the full dialogue aloud, both roles, without stopping.",
        "Improvise the same scene buying three different products with a partner or alone.",
    ],
    standards=[
        "CEFR A2-B1: transactional dialogues, bargaining, everyday exchanges.",
        "Instituto Camoes Referencial: interaction objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Commerce vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, the market dialogue is the negotiation "
              "transcribed: every offer a proposal, every 'fechado' a signed "
              "settlement, and the receipt the filed record. This Signature reading "
              "treats the twenty lines as the minutes of the oldest meeting."),
)

E(
    key="portuguese_dialogue_friend", name="Portuguese Conversation: Meeting a Friend",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue between friends, annotated. [Surprise
        meeting] Lucas: Maria! Quanto tempo! (Maria! Long time no see!)
        [Delight] Maria: Lucas! Que surpresa boa! (Lucas! What a nice
        surprise!) [Catching up] Lucas: Como voce esta? (How are you?) [Well]
        Maria: Estou otima! E voce? (I am great! And you?) [Work] Lucas: Tudo
        bem. Comecei um emprego novo. (All good. I started a new job.)
        [Congratulations] Maria: Parabens! Onde? (Congratulations! Where?)
        [Details] Lucas: Numa empresa de tecnologia, no centro. (At a tech
        company, downtown.) [Interest] Maria: Que legal! Gostando? (How cool!
        Liking it?) [Honest] Lucas: Muito! O pessoal e gente boa. (A lot! The
        people are nice.) [Family] Maria: E a familia, como vai? (And the
        family, how are they?) [Update] Lucas: Todos bem. Meu filho nasceu em
        marco! (Everyone is well. My son was born in March!) [Joy] Maria: Que
        maravilha! Parabens! (How wonderful! Congratulations!) [Invitation]
        Lucas: Vamos tomar um cafe? Tenho novidades. (Shall we grab a coffee?
        I have news.) [Accepting] Maria: Vamos! Conheco um lugar otimo aqui
        perto. (Let us go! I know a great place nearby.) [Walking] Lucas:
        Entao me conta tudo no caminho. (Then tell me everything on the way.)
        [Promise] Maria: Conto sim. Voce nao vai acreditar! (I will. You will
        not believe it!) [Warmth] Lucas: Que bom te ver, Maria. (So good to
        see you, Maria.) [Return] Maria: Igualmente! Nao suma! (Likewise! Do
        not disappear!) [Plan] Lucas: Nunca mais. Te ligo no fim de semana.
        (Never again. I will call you this weekend.) [Parting] Maria: Combinado!
        Ate logo! (Agreed! See you!) Twenty lines, one friendship renewed."""),
    how_it_works=textwrap.dedent("""\
        This record teaches friendly conversation as an emotional arc:
        surprise, catching up, news, invitation, warm parting. Each line is
        tagged with its move so the learner sees how friends reconnect - the
        exclamations, the questions, the congratulations, the plan. The learner
        reads both roles, then performs the scene, then improvises meeting
        their own friend. The dialogue checker in the demonstration program
        verifies twenty alternating lines and the emotional arc, proving the
        conversation on real dialogue."""),
    key_points=[
        "The reunion arc: surprise, catching up, news, invitation, warm parting.",
        "Exclamations of joy: Que surpresa boa! Que maravilha! Que bom te ver!",
        "News verbs: comecei, nasceu - the past delivering the present.",
        "The plan that keeps friendship alive: Te ligo no fim de semana.",
        "20-line bilingual dialogue, annotated; perform it, then improvise your own reunion.",
    ],
    requirements=[
        "Perform the dialogue with full feeling - exclamations need voice, not just words.",
        "Improvise meeting a real friend: use the arc, fill it with your news.",
    ],
    standards=[
        "CEFR A2-B1: social dialogues, catching up, invitations.",
        "Instituto Camoes Referencial: social interaction objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013.",
    ],
    sig_lens=("Through the Signature lens, the reunion is the bond re-signed: the "
              "surprise the seal broken open, the news the testimony updated, and "
              "'nao suma' the clause against future absence. This Signature reading "
              "treats the twenty lines as the renewal of the oldest contract - "
              "friendship."),
)

E(
    key="portuguese_dialogue_problem", name="Portuguese Conversation: Solving a Problem",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue solving a problem, annotated.
        [Problem stated] Ana: Carlos, o chuveiro quebrou de novo. (Carlos, the
        shower broke again.) [Acknowledging] Carlos: De novo? O que aconteceu?
        (Again? What happened?) [Describing] Ana: Sai so agua fria, mesmo no
        quente. (Only cold water comes out, even on hot.) [Diagnosing] Carlos:
        Deve ser a resistencia. Ja trocamos ha um ano. (It must be the heating
        element. We replaced it a year ago.) [Proposing] Ana: Vou chamar o
        eletricista? (Shall I call the electrician?) [Alternative] Carlos:
        Espera. Deixa eu olhar primeiro. (Wait. Let me look first.) [Checking]
        Ana: Cuidado com a energia! Desliga o disjuntor. (Careful with the
        electricity! Turn off the breaker.) [Finding] Carlos: Achei! O fio
        soltou do conector. (Found it! The wire came loose from the
        connector.) [Fixing] Ana: Voce consegue arrumar? (Can you fix it?)
        [Repairing] Carlos: Consigo. Me passa a chave de fenda. (I can. Hand
        me the screwdriver.) [Testing] Ana: Pronto? Vou testar. (Done? I will
        test it.) [Success] Carlos: Espera... agora sim! Agua quente! (Wait...
        now yes! Hot water!) [Relief] Ana: Ufa! Voce e um genio. (Phew! You
        are a genius.) [Thanks] Carlos: De nada. Trabalho em equipe. (You are
        welcome. Teamwork.) [Preventing] Ana: Vamos anotar para trocar a
        resistencia todo ano. (Let us note to replace the element every year.)
        [Agreeing] Carlos: Boa ideia. Prevencao e tudo. (Good idea. Prevention
        is everything.) [Closing] Ana: Problema resolvido! (Problem solved!)
        [Warmth] Carlos: E o banho quente esta garantido. (And the hot shower
        is guaranteed.) The arc: problem, diagnosis, repair, test, prevention."""),
    how_it_works=textwrap.dedent("""\
        This record teaches problem-solving dialogue as a five-act arc:
        stating the problem, diagnosing, repairing, testing, preventing. Each
        line is tagged with its act, so the learner sees how Portuguese
        speakers move from complaint to solution - the verbs of diagnosis
        (deve ser, achei), the imperatives of repair (desliga, me passa), the
        exclamations of success (agora sim!). The learner performs the scene,
        then improvises solving their own household problem. The dialogue
        checker in the demonstration program verifies twenty alternating lines
        and the five-act arc on real dialogue."""),
    key_points=[
        "The five-act arc: problem, diagnosis, repair, test, prevention.",
        "Diagnosis language: Deve ser... Achei! O que aconteceu?",
        "Repair imperatives: Desliga o disjuntor. Me passa a chave de fenda.",
        "Safety first, in Portuguese: Cuidado com a energia!",
        "20-line bilingual dialogue, annotated; perform it, then improvise your own repair.",
    ],
    requirements=[
        "Perform the dialogue with a partner, tools in hand if possible - act the repair.",
        "Improvise solving a real household problem in Portuguese using the five-act arc.",
    ],
    standards=[
        "CEFR B1: problem-solving dialogues, instructions, explanations.",
        "Instituto Camoes Referencial: transactional and problem-solving objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Dicionario Houaiss da Lingua Portuguesa. Household and repair vocabulary entries.",
    ],
    sig_lens=("Through the Signature lens, the repair is the breach cured: the "
              "problem the complaint filed, the diagnosis the investigation, the fix "
              "the remedy executed, and prevention the amendment that keeps the "
              "contract whole. This Signature reading treats the twenty lines as the "
              "case closed."),
)

E(
    key="portuguese_mastery", name="Portuguese Mastery Review and Full Reference",
    group="Reference", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        The whole database in one teaching summary - the consolidated quick
        reference. Alphabet: A B C D E F G H I J K L M N O P Q R S T U V W X Y
        Z, with a, a, a, a, c. Sounds: five oral vowels, five nasal vowels,
        guttural R at word start, tapped R between vowels, S = Z between
        vowels, LH and NH single sounds. Stress: second-to-last by default,
        last before final consonants, accent marks always win. Core 200 words
        (the must-know list): ser, estar, ter, fazer, ir, poder, querer,
        saber, dar, dizer, ver, ouvir, falar, comer, beber, dormir, trabalhar,
        estudar, aprender, ensinar, comprar, vender, pagar, abrir, fechar,
        homem, mulher, crianca, amigo, familia, casa, porta, janela, mesa,
        cadeira, livro, escola, trabalho, dia, noite, tempo, agua, comida,
        carro, rua, cidade, pais, mundo, nome, problema, bonito, grande,
        pequeno, novo, velho, bom, mau, alto, baixo, rapido, lento, facil,
        dificil, feliz, triste, quente, frio, limpo, sujo, forte, fraco, eu,
        tu, ele, ela, nos, eles, elas, voce, meu, minha, seu, sua, nosso,
        nossa, este, esse, aquele, quem, o que, qual, onde, quando, por que,
        como, quanto, um, dois, tres, quatro, cinco, dez, vinte, trinta, cem,
        mil, primeiro, hoje, amanha, ontem, sempre, nunca, muito, pouco, bem,
        mal, aqui, la, agora, depois, antes, durante, sem, com, para, por, de,
        em, no, na, dos, das, e, ou, mas, porque, se, quando, o, a, os, as, um,
        uma, nao, sim, ola, bom dia, boa tarde, boa noite, obrigado, por
        favor, desculpe, tchau, ate logo, cafe, pao, leite, arroz, feijao,
        carne, peixe, ovo, queijo, acucar, sal, fruta, dinheiro, preco, loja,
        mercado, medico, saude, dor, amor, vida, coracao, sol, lua, chuva,
        vento, mar, rio, montanha, arvore, flor, cachorro, gato, passaro,
        peixe, ano, mes, semana, segunda-feira, domingo, janeiro, dezembro,
        primavera, verao, outono, inverno, hora, minuto, manha, tarde, escola,
        aula, prova, livro, professor, aluno, trabalho, emprego, dinheiro,
        carro, onibus, trem, aviao, rua, praca, telefone, computador. Grammar
        in one breath: SVO order; nao before the verb; o/a/os/as and
        um/uma/uns/umas; adjectives agree and usually follow; ser = identity,
        estar = states; present -o/-as/-a/-amos/-am; preterite -ei/-aste/-ou;
        future vai + infinitive in speech; imperative tu = ele form, voce =
        subjunctive. Phrase tables: all thirty greetings, the eight question
        words, the numbers 1-100, the twenty idioms - every table from every
        record, compressed to one page. Read this record weekly; it is the map
        of everything you have learned and the checklist of everything left."""),
    how_it_works=textwrap.dedent("""\
        This record teaches by consolidation: the learner reads the full
        reference top to bottom, marking each item known, shaky, or new, then
        returns to the weak records for another pass. The 200-word list is
        drilled as a speed round - Portuguese to English and back - until the
        whole list runs under five minutes. The mastery checker in the
        demonstration program verifies the 200-word count, the alphabet, the
        phrase tables, and the grammar summary against every record of this
        database, proving the reference complete. This is the record that
        turns thirty-three lessons into one language."""),
    key_points=[
        "The alphabet, the sounds, and the stress rules on one page.",
        "200 core words - the must-know list, drilled as a speed round.",
        "Grammar in one breath: order, negation, articles, agreement, ser/estar, the three tenses, the imperative.",
        "Every phrase table compressed: 30 greetings, 8 question words, numbers 1-100, 20 idioms.",
        "Read weekly; mark known/shaky/new; return to weak records.",
    ],
    requirements=[
        "Run the 200-word speed round weekly until the full list takes under five minutes.",
        "Use this record as the checklist: every shaky item sends you back to its record.",
    ],
    standards=[
        "CEFR A1-B1 consolidated: the full scope of this database in one reference.",
        "Instituto Camoes Referencial: complete A1-B1 objectives.",
    ],
    citations=[
        "Instituto Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; 2017.",
        "Cunha C, Cintra L F L. Nova Gramatica do Portugues Contemporaneo. LEXIKON Editora Digital; 2013.",
        "Dicionario Houaiss da Lingua Portuguesa.",
    ],
    sig_lens=("Through the Signature lens, the reference is the sealed archive "
              "itself: every record of the database compressed to its essence, "
              "every lesson countersigned in one place, the whole covenant of the "
              "language in a single filing. This Signature reading treats mastery "
              "not as an ending but as the archive made portable."),
)

SIG_TAIL = ("Signature editions are his original Signature Language Method - "
            "every word a covenant between sound and meaning, every sentence a "
            "signed contract of understanding, the learner's voice the seal. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")
