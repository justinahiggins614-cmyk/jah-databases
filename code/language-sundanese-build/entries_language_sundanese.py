#!/usr/bin/env python3
"""Entries for the Sundanese to English databases (Manon's language project,
2026-10-17, language batch 4, rank 36/100).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,750 databases):
zero 'sundanese' hits, zero id_prefix values containing 'LSUN'; zgrep over
all shard index.jsonl.gz files in jah-databases-data-1: zero 'sundanese'
file hits, zero 'JAH-LSUN' ID hits. ID prefixes JAH-LSUN- (public) and
JAH-LSUNS- (signature) verified free across manifest id_prefix values AND
all shard index IDs. Pre-authoring whole-system dedupe-gate check over all
68 planned titles (34 records + 34 Signature Edition titles): zero
collisions, zero refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-sundanese              - The Sundanese to English Database
                                    (public-harvest: real, fact-checked
                                    Sundanese (Basa Sunda) - overview, the
                                    Aksara Sunda writing system, phonology,
                                    core vocabulary with sentences,
                                    grammar essentials, themed sentence
                                    sets, verb tense/aspect, questions and
                                    answers, commands, descriptions,
                                    stories, idioms, registers, complex
                                    sentences, conversations, mastery
                                    reference; standard references Adelaar
                                    2005, Ethnologue 28th ed. (2025),
                                    Palanggeran Ejahan Basa Sunda 2008,
                                    ISO 639-3 sun)
  language-sundanese-signature    - The Sundanese to English Signature Database
                                    (his original Signature Language Method:
                                    the undak usuk basa as a stairway of
                                    honor, every word choosing its height,
                                    every sentence climbing toward respect;
                                    src signature, titles suffixed
                                    " (Signature Edition)", clearly labeled
                                    Signature-made, never presented as
                                    authentic public record)

34 records each, ladder-ranked 1-34 (simple -> compounded -> most complex),
ladder_tier foundations (1-3) / compounded (4-20) / advanced (21-34); the
shard index is written in ladder order so pages present simple -> complex.

Every record carries Sundanese content + English translation + example
sentences. Sentences are required in EVERY record - no vocabulary-list-only
records. Sundanese is written in Latin script in this database (modern
standard orthography); the Aksara Sunda record shows the traditional
script alongside.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_sundanese.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "the undak usuk basa is a stairway of honor, every word "
            "choosing its height, every sentence climbing toward respect. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_ETH = ("Ethnologue: Languages of the World, 28th edition (2025). "
           "Sundanese [sun]: approximately 40 million first-language "
           "speakers; Austronesian, Malayo-Polynesian.")
CIT_ADL = ("Adelaar K.A. 'Sundanese.' In Adelaar K.A., Himmelmann N.P. "
           "(eds.), The Austronesian Languages of Asia and Madagascar. "
           "Routledge; 2005. (Phonology, morphology, speech levels.)")
CIT_ISO = ("ISO 639-3 code sun (Sundanese); ISO 639-1 code su.")
CIT_UNI = ("The Unicode Standard. Sundanese block U+1B80-U+1BBF "
           "(Aksara Sunda, added in Unicode 5.1).")
CIT_EJA = ("Palanggeran Ejahan Basa Sunda. Universitas Pendidikan "
           "Indonesia; 2008. (Official Sundanese spelling rules.)")
CIT_PAR = ("Paribasa (Sundanese proverbs) and Babasan (Sundanese idioms), "
           "Sundanese-language reference collections; forms verified "
           "against documented usage.")
CIT_SPEAKERS = ("Speaker figures are best-available estimates, rounded, "
                "per the roster note: about 40 million native speakers, "
                "the second-largest mother-tongue community in Indonesia "
                "after Javanese.")


def _num_lines(items):
    """Numbered Sundanese -> English sentence lines for descriptions."""
    out = []
    for i, (su, en) in enumerate(items, 1):
        out.append("%d. %s - %s" % (i, su, en))
    return "\n".join(out)


# ------------------------------------------------------------------ drills

OVERVIEW_SENTS = [
    ("Abdi urang Sunda.", "I am Sundanese."),
    ("Basa Sunda teh basa indung kuring.", "Sundanese is my mother tongue."),
]

NOUNS25 = [
    ("jalma", "person"), ("budak", "child"), ("lalaki", "man"),
    ("awewe", "woman"), ("imah", "house"), ("panto", "door"),
    ("jandela", "window"), ("meja", "table"), ("korsi", "chair"),
    ("cai", "water"), ("sangu", "cooked rice"), ("lauk", "fish"),
    ("buah", "fruit"), ("tangkal", "tree"), ("kembang", "flower"),
    ("panonpoe", "sun"), ("bulan", "moon"), ("bentang", "star"),
    ("langit", "sky"), ("taneuh", "earth / soil"), ("jalan", "road"),
    ("pasar", "market"), ("kota", "city"), ("lembur", "village"),
    ("nagara", "country"),
]
VERBS25 = [
    ("dahar", "eat"), ("nginum", "drink"), ("sare", "sleep"),
    ("hudang", "wake up"), ("leumpang", "walk"), ("lumpat", "run"),
    ("diuk", "sit"), ("nangtung", "stand"), ("nyarita", "speak"),
    ("nanya", "ask"), ("maca", "read"), ("nulis", "write"),
    ("meuli", "buy"), ("ngajual", "sell"), ("nyieun", "make"),
    ("ibak", "bathe"), ("seuri", "laugh"), ("ceurik", "cry"),
    ("indit", "go"), ("datang", "come"), ("balik", "go home / return"),
    ("gawe", "work"), ("diajar", "study"), ("ulin", "play"),
    ("nempo", "see / watch"),
]
ADJ25 = [
    ("alus", "good"), ("goreng", "bad"), ("gede", "big"),
    ("leutik", "small"), ("panjang", "long"), ("pondok", "short"),
    ("jangkung", "tall"), ("handap", "low"), ("anyar", "new"),
    ("kolot", "old"), ("ngora", "young"), ("geulis", "beautiful"),
    ("pinter", "smart"), ("beunghar", "rich"), ("miskin", "poor"),
    ("panas", "hot"), ("tiis", "cold"), ("amis", "sweet"),
    ("pait", "bitter"), ("asin", "salty"), ("lada", "spicy"),
    ("beurat", "heavy"), ("hampang", "light"), ("gancang", "fast"),
    ("kuat", "strong"),
]
ADV15 = [
    ("pisan", "very"), ("leuwih", "more"), ("geus", "already"),
    ("acan", "not yet"), ("keur", "currently"), ("rek", "about to"),
    ("tangtu", "certainly"), ("meureun", "maybe"), ("saban", "every"),
    ("ayeuna", "now"), ("kamari", "yesterday"), ("isukan", "tomorrow"),
    ("lalaunan", "slowly"), ("oge", "also / too"), ("bae", "just / only"),
]
NUMBERS = [
    (1, "hiji"), (2, "dua"), (3, "tilu"), (4, "opat"), (5, "lima"),
    (6, "genep"), (7, "tujuh"), (8, "dalapan"), (9, "salapan"),
    (10, "sapuluh"), (11, "sabelas"), (12, "dua belas"),
    (20, "dua puluh"), (21, "dua puluh hiji"), (25, "dua puluh lima"),
    (30, "tilu puluh"), (50, "lima puluh"),
    (100, "saratus"), (1000, "sarebu"), (1000000, "sajuta"),
]
ORDINALS = [("kahiji", "first"), ("kadua", "second"), ("katilu", "third")]
DAYS = ["Senen", "Salasa", "Rebo", "Kemis", "Jumaah", "Saptu", "Minggu"]
MONTHS = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
          "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

GREET30 = [
    ("Sampurasun.", "Traditional Sundanese greeting (reply: rampes)."),
    ("Rampes.", "The reply to sampurasun."),
    ("Wilujeng enjing.", "Good morning."),
    ("Wilujeng siang.", "Good midday."),
    ("Wilujeng sonten.", "Good afternoon."),
    ("Wilujeng wengi.", "Good evening."),
    ("Wilujeng sumping.", "Welcome."),
    ("Hatur nuhun.", "Thank you."),
    ("Hatur nuhun pisan.", "Thank you very much."),
    ("Sami-sami.", "You are welcome."),
    ("Punten.", "Excuse me (asking permission)."),
    ("Hampura.", "Forgive me / sorry."),
    ("Mangga.", "Please, go ahead / come in."),
    ("Kumaha damang?", "How are you?"),
    ("Pangestu, alhamdulillah.", "I am well, thank God (reply)."),
    ("Atos tuang?", "Have you eaten?"),
    ("Atos, hatur nuhun.", "Yes, I have, thank you (reply)."),
    ("Wilujeng angkat.", "Safe travels (farewell)."),
    ("Sing ati-ati.", "Be careful."),
    ("Wilujeng kulem.", "Good night (sleep well)."),
    ("Wilujeng tepang taun.", "Happy birthday."),
    ("Wilujeng boboran.", "Happy Eid (Lebaran greeting)."),
    ("Sumuhun.", "Yes (polite)."),
    ("Muhun.", "Yes (casual polite)."),
    ("Henteu.", "No."),
    ("Teu sawios.", "It is nothing / no problem."),
    ("Punten, bade tumaros.", "Excuse me, may I ask something?"),
    ("Wilujeng wengi, wilujeng kulem.", "Good evening, sleep well."),
    ("Abdi bade angkat heula.", "I will take my leave first."),
    ("Mugia salamet dugi ka tujuan.", "May you arrive safely at your destination."),
]

PRONOUNS = [
    ("abdi", "I (humble, polite)"), ("sim kuring", "I (formal polite)"),
    ("kuring", "I (neutral)"), ("aing", "I (very informal)"),
    ("anjeun", "you (polite)"), ("salira", "you (refined)"),
    ("sia", "you (coarse)"), ("maneh", "you (informal)"),
    ("manehna", "he / she (neutral)"), ("maranehna", "they (neutral)"),
    ("urang", "we (inclusive; colloquial I)"), ("aranjeun", "you (plural, polite)"),
    ("maraneh", "you (plural, informal)"), ("kami", "we (exclusive)"),
    ("ieu", "this"), ("eta", "that"),
]

IDIOMS20 = [
    ("Caina herang laukna beunang.",
     "Literal: the water stays clear, the fish is caught. Meaning: solve a matter the good way so nobody is hurt.",
     "Urang kudu musyawarah sangkan caina herang laukna beunang. - We must deliberate so the water stays clear and the fish is caught."),
    ("Cikaracak ninggang batu, laun-laun jadi legok.",
     "Literal: dripping water strikes stone, slowly it hollows. Meaning: steady persistence finishes even the hardest work.",
     "Diajar unggal poe, cikaracak ninggang batu, laun-laun jadi legok. - Study every day; dripping water hollows stone in time."),
    ("Tong kosong nyaring bunyina.",
     "Literal: the empty drum sounds the loudest. Meaning: those who know least boast most.",
     "Ulah kawas tong kosong nyaring bunyina. - Do not be like the empty drum that sounds loudest."),
    ("Kawas cai dina daun taleus.",
     "Literal: like water on a taro leaf. Meaning: a fickle person, leaving no trace, impossible to hold.",
     "Jangjina kawas cai dina daun taleus. - His promises are like water on a taro leaf."),
    ("Buruk-buruk papan jati.",
     "Literal: however rotten, still teak. Meaning: family still helps family, whatever the faults.",
     "Buruk-buruk papan jati, dulur mah tetep nulungan. - Rotten or not it is teak: family still helps."),
    ("Cul dogdog tinggal igel.",
     "Literal: throwing away the drum, keeping only the dance. Meaning: abandoning sure work for an uncertain venture.",
     "Ulah cul dogdog tinggal igel. - Do not throw away the drum and keep only the dance."),
    ("Bentik curuk balas nunjuk.",
     "Literal: the finger bends only to point. Meaning: someone who only likes ordering others around.",
     "Anjeunna mah bentik curuk balas nunjuk. - He just bends his finger to point at others."),
    ("Silih asah, silih asih, silih asuh.",
     "Literal: sharpen one another, love one another, nurture one another. Meaning: the Sundanese ethic of mutual support.",
     "Hirup kudu silih asah, silih asih, silih asuh. - Life must be mutual sharpening, loving, and nurturing."),
    ("Mun teu ngakal moal ngakeul.",
     "Literal: if you do not work you cannot eat. Meaning: no work, no food; diligence feeds you.",
     "Mun teu ngakal moal ngakeul, sing getol gawe. - If you do not work you cannot eat, so work hard."),
    ("Elmu tungtut dunya siar.",
     "Literal: pursue knowledge, seek the world. Meaning: never stop learning, wherever you go.",
     "Elmu tungtut dunya siar, ulah eureun diajar. - Pursue knowledge and seek the world; never stop learning."),
    ("Kacang poho ka lanjaran.",
     "Literal: the bean forgets its trellis. Meaning: someone who forgets their origins after succeeding.",
     "Ulah kacang poho ka lanjaran. - Do not be the bean that forgets its trellis."),
    ("Bobot pangayon timbang taraju.",
     "Literal: weigh on the scale, balance on the balance. Meaning: judge fairly only after thinking it through.",
     "Bobot pangayon timbang taraju samemeh mutuskeun. - Weigh and balance before you decide."),
    ("Batok bulu eusi madu.",
     "Literal: a hairy coconut shell filled with honey. Meaning: rough outside, good-hearted inside.",
     "Tong ditilik tina rupana, batok bulu eusi madu. - Do not judge by looks; the hairy shell holds honey."),
    ("Agul ku payung butut.",
     "Literal: proud of a tattered umbrella. Meaning: boasting about one's family line or borrowed finery.",
     "Ulah agul ku payung butut. - Do not be proud of a tattered umbrella."),
    ("Adat kakurung ku iga.",
     "Literal: habit caged by the ribs. Meaning: bad habits are very hard to change.",
     "Adat kakurung ku iga, hese dirobahna. - Habit caged by the ribs is hard to change."),
    ("Kurung batok.",
     "Literal: (a frog) under a coconut shell. Meaning: narrow-minded, never traveling far.",
     "Ulah kurung batok, kudu loba pangalaman. - Do not be a frog under a shell; gather experience."),
    ("Gede hulu.",
     "Literal: big head. Meaning: arrogant.",
     "Anjeunna teh gede hulu. - He is big-headed."),
    ("Panjang leungeun.",
     "Literal: long arm. Meaning: a thief; thieving.",
     "Awas, manehna mah panjang leungeun. - Careful, he is long-armed."),
    ("Kawas anjing tutung buntut.",
     "Literal: like a dog with a burnt tail. Meaning: restless, unable to sit still.",
     "Budak teh kawas anjing tutung buntut. - The child is like a dog with a burnt tail."),
    ("Cileuncang mande sagara.",
     "Literal: a ripple wanting to rival the ocean. Meaning: trying to surpass those far above one's station.",
     "Ulah cileuncang mande sagara. - Do not be a ripple trying to rival the ocean."),
]

PARTICLES24 = [
    "deui", "wae", "keneh", "sih", "atuh", "bade", "henteu", "teu",
    "moal", "ulah", "sok", "mah", "teh", "nu", "anu", "jeung",
    "atawa", "tapi", "sabab", "lamun", "mun", "supaya", "dina", "ka",
]

GRAMMAR10 = [
    ("Word order is subject-verb-object, like English.",
     "Abdi dahar sangu.", "I eat rice."),
    ("No grammatical gender: one pronoun covers he, she, and it.",
     "Manehna guru.", "He/she is a teacher."),
    ("No case marking: nouns never change form for subject or object.",
     "Budak nempo budak.", "The child sees the child."),
    ("No verb conjugation for person: one form serves all subjects.",
     "Abdi indit. Anjeun indit. Maranehna indit.",
     "I go. You go. They go."),
    ("Plurals use reduplication or the -ar- infix: budak becomes barudak.",
     "Barudak keur ulin.", "The children are playing."),
    ("Negation: henteu/teu (not), moal (will not), ulah (do not!).",
     "Abdi henteu terang. Ulah ribut!", "I do not know. Do not be noisy!"),
    ("Questions need no particle: an interrogative word plus rising intonation.",
     "Saha nami anjeun?", "What is your name?"),
    ("Passive voice takes di-: dibaca (is read), dituang (is eaten).",
     "Buku dibaca ku murid.", "The book is read by the student."),
    ("Active verbs take the nasal prefix N-: tulis becomes nulis.",
     "Abdi nulis surat.", "I write a letter."),
    ("Time is marked by words, not verb endings: geus, keur, rek/bade.",
     "Abdi geus dahar. Abdi keur dahar. Abdi rek dahar.",
     "I have eaten. I am eating. I am about to eat."),
]

TENSE_SETS = [
    ("Past and completed - geus (already)",
     [("Abdi geus dahar.", "I have already eaten."),
      ("Manehna geus balik kamari.", "He/she went home yesterday."),
      ("Kami geus meuli beas.", "We have bought rice."),
      ("Barudak geus sarare.", "The children have fallen asleep."),
      ("Anjeun geus nulis?", "Have you written?")]),
    ("Present and ongoing - keur (currently)",
     [("Abdi keur diajar.", "I am studying."),
      ("Manehna keur masak di dapur.", "She is cooking in the kitchen."),
      ("Urang keur ngadagoan beus.", "We are waiting for the bus."),
      ("Bapa keur maca koran.", "Father is reading the newspaper."),
      ("Ibu keur nyieun kueh.", "Mother is making cake.")]),
    ("Future - rek / bade (about to / will)",
     [("Abdi rek indit isukan.", "I will go tomorrow."),
      ("Manehna bade sumping enjing.", "He will come in the morning."),
      ("Urang rek ulin ka pantai.", "We are going to play at the beach."),
      ("Bapa bade angkat ka Bandung.", "Father will depart for Bandung."),
      ("Abdi rek meuli buku anyar.", "I am going to buy a new book.")]),
    ("Habitual - sok (usually / often)",
     [("Abdi sok hudang jam lima.", "I usually wake at five."),
      ("Manehna sok ulin bal.", "He often plays ball."),
      ("Urang sok dahar babarengan.", "We usually eat together."),
      ("Bapa sok maca peuting.", "Father usually reads at night."),
      ("Barudak sok ribut isuk-isuk.", "The children are often noisy in the morning.")]),
    ("Negative future - moal (will not)",
     [("Abdi moal indit.", "I will not go."),
      ("Manehna moal datang.", "He/she will not come."),
      ("Urang moal hilap.", "We will not forget."),
      ("Hujan moal turun.", "It will not rain."),
      ("Abdi moal beuki.", "I will not buy it.")]),
]

QA20 = [
    ("Saha nami anjeun?", "Abdi teh Ujang.", "What is your name?", "My name is Ujang."),
    ("Naon ieu?", "Ieu teh buku.", "What is this?", "This is a book."),
    ("Anjeun timana?", "Abdi ti Bandung.", "Where are you from?", "I am from Bandung."),
    ("Imah anjeun dimana?", "Imah abdi di lembur.", "Where is your house?", "My house is in the village."),
    ("Iraha anjeun datang?", "Abdi datang kamari.", "When did you arrive?", "I arrived yesterday."),
    ("Naha anjeun ceurik?", "Abdi ceurik sabab sedih.", "Why are you crying?", "I cry because I am sad."),
    ("Kumaha damang?", "Pangestu, alhamdulillah.", "How are you?", "I am well, thank God."),
    ("Kumaha carana ka pasar?", "Leumpang terus ka kenca.", "How do I get to the market?", "Walk straight, then left."),
    ("Sabaraha hargana?", "Hargana lima rebu.", "How much is it?", "It costs five thousand."),
    ("Nu mana buku anjeun?", "Nu beureum.", "Which one is your book?", "The red one."),
    ("Saha nu sumping?", "Bapa nu sumping.", "Who came?", "Father came."),
    ("Naon anu didahar?", "Sangu jeung lauk.", "What is being eaten?", "Rice and fish."),
    ("Kunaon anjeun telat?", "Sabab macet.", "Why are you late?", "Because of the traffic jam."),
    ("Aya naon di dapur?", "Aya sangu haneut.", "What is in the kitchen?", "There is warm rice."),
    ("Iraha urang angkat?", "Isukan isuk.", "When do we leave?", "Tomorrow morning."),
    ("Naha hujan?", "Sabab usum hujan.", "Why is it raining?", "Because it is the rainy season."),
    ("Kumaha rasana?", "Amis pisan.", "How does it taste?", "Very sweet."),
    ("Sabaraha budakna?", "Aya tilu.", "How many children?", "There are three."),
    ("Timana cai ieu?", "Ti sumur.", "Where is this water from?", "From the well."),
    ("Naha anjeun henteu sarare?", "Sabab masih gawe.", "Why are you not asleep?", "Because I am still working."),
]

COMMANDS20 = [
    ("Diuk!", "Sit!", "informal"),
    ("Mangga calik.", "Please sit.", "polite"),
    ("Dahar!", "Eat!", "informal"),
    ("Mangga tuang.", "Please eat.", "polite"),
    ("Indit ayeuna!", "Go now!", "informal"),
    ("Mangga angkat.", "Please go ahead.", "polite"),
    ("Ulah ribut!", "Do not be noisy!", "informal"),
    ("Punten, ulah ribut.", "Excuse me, please keep quiet.", "polite"),
    ("Buka pantona!", "Open the door!", "informal"),
    ("Punten, buka pantona.", "Excuse me, open the door.", "polite"),
    ("Tutup jandelana!", "Close the window!", "informal"),
    ("Punten, tutup jandelana.", "Excuse me, close the window.", "polite"),
    ("Hudang!", "Wake up!", "informal"),
    ("Mangga hudang.", "Please wake up.", "polite"),
    ("Asup!", "Come in!", "informal"),
    ("Mangga lebet.", "Please come in.", "polite"),
    ("Cicing!", "Be quiet!", "informal"),
    ("Punten, cicing heula.", "Excuse me, be quiet a moment.", "polite"),
    ("Balik!", "Go home!", "informal"),
    ("Mangga, wangsul.", "Please, go home.", "polite"),
]

REGISTER15 = [
    ("kuring", "abdi", "I - neutral becomes humble-polite"),
    ("maneh", "anjeun", "you - informal becomes polite"),
    ("anjeun", "salira", "you - polite becomes refined"),
    ("indit", "angkat", "go - neutral becomes polite"),
    ("dahar", "tuang", "eat - neutral becomes polite (for self)"),
    ("dahar", "neda", "eat - neutral becomes honorific (for others)"),
    ("sare", "kulem", "sleep - neutral becomes very polite"),
    ("diuk", "calik", "sit - neutral becomes polite"),
    ("hayang", "hoyong", "want - neutral becomes polite"),
    ("datang", "sumping", "come - neutral becomes honorific"),
    ("nanya", "tumaros", "ask - neutral becomes polite"),
    ("imah", "bumi", "house - neutral becomes polite"),
    ("peuting", "wengi", "night - neutral becomes polite"),
    ("isuk", "enjing", "morning - neutral becomes polite"),
    ("budak", "murangkalih", "child - neutral becomes polite"),
]

CONV_MARKET = [
    ("A", "Wilujeng enjing, Bu.", "Good morning, ma'am."),
    ("B", "Wilujeng enjing. Bade meser naon?", "Good morning. What would you like to buy?"),
    ("A", "Aya cau?", "Do you have bananas?"),
    ("B", "Aya, seger pisan. Sabaraha kilo?", "Yes, very fresh. How many kilos?"),
    ("A", "Dua kilo we. Sabaraha?", "Two kilos. How much?"),
    ("B", "Dua puluh rebu.", "Twenty thousand."),
    ("A", "Mirah teuing? Lima belas rebu we.", "A bit pricey? Fifteen thousand, then."),
    ("B", "Henteu tiasa, dalapan belas rebu.", "I cannot; eighteen thousand."),
    ("A", "Mangga, dalapan belas rebu.", "Fine, eighteen thousand."),
    ("B", "Aya deui?", "Anything else?"),
    ("A", "Laukna seger?", "Is the fish fresh?"),
    ("B", "Seger pisan, nembe dongkap.", "Very fresh, just arrived."),
    ("A", "Sabaraha sakilona?", "How much per kilo?"),
    ("B", "Tilu puluh lima rebu.", "Thirty-five thousand."),
    ("A", "Mangga, satengah kilo.", "Fine, half a kilo."),
    ("B", "Ieu totalna tilu puluh genep rebu.", "This totals thirty-six thousand."),
    ("A", "Ieu artosna. Hatur nuhun.", "Here is the money. Thank you."),
    ("B", "Sami-sami. Mangga, sing laris.", "You are welcome. Come again."),
    ("A", "Wilujeng angkat, Bu.", "Goodbye, ma'am."),
    ("B", "Wilujeng angkat.", "Goodbye."),
]
CONV_FRIEND = [
    ("A", "Sampurasun!", "Sampurasun! (traditional greeting)"),
    ("B", "Rampes! Kumaha damang?", "Rampes! How are you?"),
    ("A", "Pangestu, alhamdulillah. Anjeun kumaha?", "I am well, thank God. And you?"),
    ("B", "Sehat. Geus lila teu tepang.", "Healthy. Long time no see."),
    ("A", "Enya, ti iraha anjeun di dieu?", "Yes, since when have you been here?"),
    ("B", "Ti sataun kamari. Gawe di kota.", "Since last year. Working in the city."),
    ("A", "Atos tuang?", "Have you eaten?"),
    ("B", "Atos. Urang ngopi yuk.", "Yes. Let us have coffee."),
    ("A", "Mangga. Di warung hareup we.", "Sure. At the shop ahead."),
    ("B", "Kumaha kulawarga di lembur?", "How is the family in the village?"),
    ("A", "Sehat sadayana. Ibu nanyakeun anjeun.", "All healthy. Mother asks about you."),
    ("B", "Salam ka ibu. Iraha urang ulin ka lembur?", "Give her my regards. When shall we visit the village?"),
    ("A", "Isukan kumaha? Poe Minggu.", "How about tomorrow? Sunday."),
    ("B", "Mangga, abdi bade milu.", "Sure, I will join."),
    ("A", "Urang angkat isuk-isuk jam tujuh.", "We leave early at seven."),
    ("B", "Sapuk. Ulah telat nya.", "Agreed. Do not be late."),
    ("A", "Moal. Dugi ka tepang isukan.", "I won't. See you tomorrow."),
    ("B", "Mugia salamet.", "Stay safe."),
    ("A", "Hatur nuhun.", "Thank you."),
    ("B", "Sami-sami.", "You are welcome."),
]
CONV_PROBLEM = [
    ("A", "Aduh, lampuna pareum!", "Oh no, the lights are out!"),
    ("B", "Enya, sakabupaten pareum sigana.", "Yes, probably the whole district is out."),
    ("A", "Kumaha atuh? Budak sieun poek.", "What now? The child is afraid of the dark."),
    ("B", "Ulah panik. Aya lilin?", "Don't panic. Are there candles?"),
    ("A", "Aya di lomari dapur.", "There are some in the kitchen cupboard."),
    ("B", "Mangga candak. Abdi neangan senter.", "Go get them. I'll look for the flashlight."),
    ("A", "Senterna batrena beak.", "The flashlight batteries are dead."),
    ("B", "Teu sawios, lilin we cekap.", "No problem, candles are enough."),
    ("A", "Telepon PLN ka saha?", "Whom do we call at the power company?"),
    ("B", "Ka call center, ieu nomerna.", "The call center; here is the number."),
    ("A", "Dijawab, cenah sejam deui hurung.", "They answered; power back in an hour, they say."),
    ("B", "Syukur. Urang ngadagoan we.", "Thank goodness. Let's just wait."),
    ("A", "Sangu di magic com masih haneut?", "Is the rice in the cooker still warm?"),
    ("B", "Masih. Urang dahar heula.", "Still warm. Let's eat first."),
    ("A", "Mangga tuang.", "Please eat."),
    ("B", "Hatur nuhun. Amis sangu haneut.", "Thank you. Warm rice is sweet."),
    ("A", "Tuh, lampuna hurung deui!", "Look, the lights are back on!"),
    ("B", "Alhamdulillah. Masalah rengse.", "Thank God. Problem solved."),
    ("A", "Hatur nuhun tos ngabantos.", "Thank you for helping."),
    ("B", "Sami-sami, dulur mah kudu nulungan.", "You're welcome; family must help."),
]

STORY1 = [
    ("Ujang budak leutik ti lembur Cibeureum.", "Ujang is a little boy from Cibeureum village."),
    ("Unggal isuk manehna hudang jam lima.", "Every morning he wakes at five."),
    ("Manehna ibak tuluy dahar sangu haneut.", "He bathes, then eats warm rice."),
    ("Sanggeus dahar, manehna indit ka sawah.", "After eating, he goes to the rice field."),
    ("Bapana geus ngadagoan di galengan.", "His father is already waiting on the dike."),
    ("Maranéhna melak paré babarengan.", "They plant rice together."),
    ("Panonpoe bersinar, angin niis seger.", "The sun shines, the breeze blows fresh."),
    ("Ujang seuri bari diajar melak.", "Ujang laughs while learning to plant."),
    ("Beurang manehna balik ka imah.", "At midday he returns home."),
    ("Indungna ngahaturanan sangu jeung lauk.", "His mother serves rice and fish."),
]
STORY2 = [
    ("Kamari embe Si Ujang leungit.", "Yesterday Ujang's goat went missing."),
    ("Isuk-isuk kandangna geus kosong.", "In the morning its pen was already empty."),
    ("Ujang ceurik, indungna ngahibur.", "Ujang cried; his mother comforted him."),
    ("Bapana indit neangan ka leuweung.", "His father went to search in the woods."),
    ("Di jalan manehna papanggih jeung tatangga.", "On the way he met a neighbor."),
    ("Tatangga teh nempo embe di sisi walungan.", "The neighbor had seen the goat by the river."),
    ("Bapa lumpat gancang ka walungan.", "Father ran quickly to the river."),
    ("Embe teh keur nginum cai.", "The goat was drinking water."),
    ("Bapa nangkep embe tuluy dibawa balik.", "Father caught the goat and brought it home."),
    ("Ujang seuri deui, hatena bungah.", "Ujang laughed again, his heart happy."),
]
STORY3 = [
    ("Isukan Ujang rek indit ka Bandung.", "Tomorrow Ujang will go to Bandung."),
    ("Manehna bade numpak kareta api.", "He will ride the train."),
    ("Indungna geus nyiapkeun bekal.", "His mother has prepared provisions."),
    ("Bapana mere sangu beas ka anjeunna.", "His father gives him travel money."),
    ("Maranéhna bade angkat jam tujuh isuk.", "They will depart at seven in the morning."),
    ("Di Bandung Ujang rek tepang jeung dulurna.", "In Bandung Ujang will meet his cousin."),
    ("Dulurna bade ngajak ulin ka kota.", "His cousin will take him around the city."),
    ("Maranéhna rek nempo museum jeung kebon binatang.", "They will see the museum and the zoo."),
    ("Sontenna maranéhna bade balik ka lembur.", "In the afternoon they will return to the village."),
    ("Ujang moal hilap kana poe eta.", "Ujang will never forget that day."),
]

COMPLEX15 = [
    ("Abdi dahar sangu sabab abdi lapar pisan.",
     "I eat rice because I am very hungry. - causal clause with sabab"),
    ("Sanajan hujan, bapa tetep angkat ka sawah.",
     "Although it rains, father still goes to the field. - concessive with sanajan"),
    ("Buku anu dibaca ku Ujang teh kandel pisan.",
     "The book that Ujang reads is very thick. - relative clause with anu"),
    ("Lamun anjeun datang isuk, urang dahar babarengan.",
     "If you come early, we eat together. - conditional with lamun"),
    ("Manehna ceurik sabab embena leungit kamari.",
     "He cries because his goat went missing yesterday. - past causal"),
    ("Ibu masak sangu bari bapa maca koran.",
     "Mother cooks rice while father reads the newspaper. - simultaneous with bari"),
    ("Barudak ulin di buruan sanggeus rengse diajar.",
     "The children play in the yard after finishing study. - temporal with sanggeus"),
    ("Abdi henteu terang saha nu nyokot konci.",
     "I do not know who took the key. - embedded question"),
    ("Jalma anu getol gawe tangtu bakal suksés.",
     "A person who works hard will surely succeed. - relative + future"),
    ("Ulah indit samemeh hujan eureun.",
     "Do not leave before the rain stops. - temporal with samemeh"),
    ("Manehna datang ka sakola mawa buku anyar.",
     "He comes to school bringing a new book. - participial"),
    ("Najan cape, indung tetep seuri ka barudakna.",
     "However tired, mother still smiles at her children. - concessive with najan"),
    ("Urang kudu diajar sangkan pinter.",
     "We must study so that we become smart. - purpose with sangkan"),
    ("Eta imah gedé téh milik kulawarga anu beunghar.",
     "That big house belongs to a rich family. - identification + relative"),
    ("Mun anjeun hoyong suksés, sing getol ti ayeuna.",
     "If you want to succeed, be diligent from now on. - conditional + imperative"),
]

DESCRIBE20 = [
    ("Ujang budakna jangkung tur pinter.", "Ujang is a tall and smart boy."),
    ("Bu Guru geulis tur someah.", "The teacher is beautiful and friendly."),
    ("Imah kami gedé, aya lima kamar.", "Our house is big; it has five rooms."),
    ("Kota Bandung tiis tur rame.", "Bandung city is cool and lively."),
    ("Sawah bapa lega, parena hejo.", "Father's rice field is wide; the rice is green."),
    ("Anjing hideung eta galak pisan.", "That black dog is very fierce."),
    ("Kembang beureum di buruan seungit.", "The red flowers in the yard are fragrant."),
    ("Gunung Tangkuban Parahu jangkung tur endah.", "Mount Tangkuban Parahu is tall and beautiful."),
    ("Cai walungan herang tur tiis.", "The river water is clear and cold."),
    ("Nenek geus kolot, buluna bodas.", "Grandmother is old; her hair is white."),
    ("Mobil beureum eta gancang pisan.", "That red car is very fast."),
    ("Pasar isuk rame ku jalma.", "The morning market is crowded with people."),
    ("Dapur indung beresih tur rapih.", "Mother's kitchen is clean and tidy."),
    ("Tangkal mangga di tukang imah jangkung.", "The mango tree behind the house is tall."),
    ("Langit peuting pinuh ku bentang.", "The night sky is full of stars."),
    ("Jalan ka lembur heureut tur nanjak.", "The road to the village is narrow and climbing."),
    ("Sangu haneut amis tur pulen.", "Warm rice is sweet and fluffy."),
    ("Aki someah, sok dongeng ka incu.", "Grandfather is kind; he often tells stories to his grandchildren."),
    ("Tas kulit eta beurat tur awis.", "That leather bag is heavy and expensive."),
    ("Pantai Pangandaran endah, ombakna gedé.", "Pangandaran beach is beautiful; its waves are big."),
]

HOME20 = [
    ("Imah abdi aya di lembur.", "My house is in the village."),
    ("Imahna gedé tur beresih.", "The house is big and clean."),
    ("Aya opat kamar di imah.", "There are four rooms in the house."),
    ("Kamar sare abdi di luhur.", "My bedroom is upstairs."),
    ("Dapur aya di tukang.", "The kitchen is at the back."),
    ("Panto hareup warnana hejo.", "The front door is green."),
    ("Jandela kamar dibuka isuk-isuk.", "The bedroom window is opened in the morning."),
    ("Meja dahar di tengah imah.", "The dining table is in the middle of the house."),
    ("Bapa keur diuk di korsi.", "Father is sitting on the chair."),
    ("Indung keur masak di dapur.", "Mother is cooking in the kitchen."),
    ("Aki jeung nini cicing di lembur.", "Grandfather and grandmother live in the village."),
    ("Dulur abdi aya tilu.", "I have three siblings."),
    ("Adina masih sakola SD.", "My younger sibling still attends elementary school."),
    ("Lanceukna geus gawe di kota.", "My older sibling already works in the city."),
    ("Buruan hareup lega pisan.", "The front yard is very spacious."),
    ("Aya tangkal mangga di buruan.", "There is a mango tree in the yard."),
    ("Ucing sare di handapeun meja.", "The cat sleeps under the table."),
    ("Lampu kamar hurung peuting.", "The room lamp is lit at night."),
    ("Urang kudu ngaberesihan imah.", "We must clean the house."),
    ("Imah teh tempat pangbalikan.", "Home is the place of return."),
]

FOOD20 = [
    ("Abdi lapar pisan.", "I am very hungry."),
    ("Indung keur masak sangu.", "Mother is cooking rice."),
    ("Sangu geus asak.", "The rice is cooked."),
    ("Lauk goreng amis pisan.", "The fried fish is very tasty."),
    ("Sambelna lada teuing.", "The chili sauce is too spicy."),
    ("Mangga tuang.", "Please eat."),
    ("Abdi tuang sangu jeung lauk.", "I eat rice with fish."),
    ("Sayurna seger.", "The vegetables are fresh."),
    ("Caina haneut.", "The water is warm."),
    ("Buahna amis.", "The fruit is sweet."),
    ("Warung hareup ngajual lotek.", "The shop ahead sells lotek (vegetable salad)."),
    ("Sabaraha saporsi?", "How much for one portion?"),
    ("Saporsina sapuluh rebu.", "One portion is ten thousand."),
    ("Abdi mesen dua porsi.", "I order two portions."),
    ("Tong hilap sambelna.", "Don't forget the chili sauce."),
    ("Dahar nu cukup, ulah kaleuleuwihi.", "Eat enough, do not overdo it."),
    ("Sanggeus dahar, nginum cai haneut.", "After eating, drink warm water."),
    ("Kueh ieu amis teuing.", "This cake is too sweet."),
    ("Beasna beak, kudu meuli deui.", "The uncooked rice is gone; we must buy more."),
    ("Hatur nuhun kana tuangna.", "Thank you for the meal."),
]

TRAVEL20 = [
    ("Abdi bade angkat ka Bandung.", "I will depart for Bandung."),
    ("Kareta angkat jam tujuh.", "The train departs at seven."),
    ("Sabaraha ongkosna?", "How much is the fare?"),
    ("Ongkosna dua puluh rebu.", "The fare is twenty thousand."),
    ("Mangga, ieu tiketna.", "Here is the ticket."),
    ("Beusna pinuh pisan.", "The bus is very full."),
    ("Urang diuk di hareup.", "We sit in the front."),
    ("Sabaraha lami ka ditu?", "How long to get there?"),
    ("Kira-kira dua jam.", "About two hours."),
    ("Punten, jalan ka stasion dimana?", "Excuse me, where is the road to the station?"),
    ("Leumpang terus, tuluy belok ka kenca.", "Walk straight, then turn left."),
    ("Hotelna deukeut ti dieu?", "Is the hotel near here?"),
    ("Deukeut, lima menit leumpang.", "Near, five minutes on foot."),
    ("Kamarna beresih tur nyaman.", "The room is clean and comfortable."),
    ("Aya cai haneut?", "Is there hot water?"),
    ("Aya, di kamar mandi.", "Yes, in the bathroom."),
    ("Urang ulin ka pantai isukan.", "We will visit the beach tomorrow."),
    ("Jalanna macet pisan.", "The road is very jammed."),
    ("Supirna someah.", "The driver is friendly."),
    ("Wilujeng angkat, sing salamet.", "Safe travels, be safe."),
]

WORK20 = [
    ("Bapa gawe di kantor.", "Father works at an office."),
    ("Indung guru di sakola.", "Mother is a teacher at a school."),
    ("Abdi diajar basa Sunda.", "I study Sundanese."),
    ("Muridna pinter-pinter.", "The students are smart."),
    ("Guruna someah pisan.", "The teacher is very kind."),
    ("Pelajaran dimimitian jam tujuh.", "Lessons start at seven."),
    ("Urang diajar maca jeung nulis.", "We learn to read and write."),
    ("PRna kudu dikumpulkeun isukan.", "The homework must be submitted tomorrow."),
    ("Kantor buka jam dalapan.", "The office opens at eight."),
    ("Rapat dimimitian jam salapan.", "The meeting starts at nine."),
    ("Bosna tegas tapi adil.", "The boss is firm but fair."),
    ("Gajihna cekap keur kulawarga.", "The salary suffices for the family."),
    ("Dulur abdi dokter di rumah sakit.", "My sibling is a doctor at the hospital."),
    ("Petani melak pare di sawah.", "The farmer plants rice in the field."),
    ("Padagang ngajual di pasar.", "The trader sells at the market."),
    ("Montir ngalereskeun motor.", "The mechanic repairs the motorcycle."),
    ("Koki masak di restoran.", "The cook cooks at the restaurant."),
    ("Supir nganteur panumpang.", "The driver takes the passengers."),
    ("Gawe nu getol sangkan suksés.", "Work hard so you succeed."),
    ("Istirahat heula, ulah cape teuing.", "Rest first, do not overtire."),
]

HEALTH20 = [
    ("Abdi teu damang.", "I am not well."),
    ("Sirah abdi nyeri.", "My head aches."),
    ("Awak abdi panas.", "My body is hot (feverish)."),
    ("Beuteung abdi nyeri.", "My stomach hurts."),
    ("Huntu abdi nyeri.", "My tooth hurts."),
    ("Abdi batuk ti kamari.", "I have coughed since yesterday."),
    ("Panonna beureum.", "His eyes are red."),
    ("Sukuna tiis.", "Her feet are cold."),
    ("Leungeunna tatu.", "His hand is wounded."),
    ("Manehna muriang.", "He has a fever."),
    ("Kudu ka dokter.", "Must go to the doctor."),
    ("Dokterna someah.", "The doctor is kind."),
    ("Dokter mere obat.", "The doctor gives medicine."),
    ("Inum obatna tilu kali sapoe.", "Take the medicine three times a day."),
    ("Ulah hilap inum cai nu loba.", "Do not forget to drink lots of water."),
    ("Istirahat nu cukup.", "Rest enough."),
    ("Apotekna buka nepi ka peuting.", "The pharmacy is open until night."),
    ("Sabaraha hargana obat?", "How much is the medicine?"),
    ("Mugia enggal damang.", "Get well soon."),
    ("Hatur nuhun, dokter.", "Thank you, doctor."),
]

EMOTION20 = [
    ("Abdi bungah pisan.", "I am very happy."),
    ("Manehna seuri wae.", "She just keeps laughing."),
    ("Hatena pinuh ku kabungah.", "His heart is full of joy."),
    ("Abdi sedih.", "I am sad."),
    ("Manehna ceurik.", "She cries."),
    ("Cimata murag.", "Tears fall."),
    ("Abdi ambek.", "I am angry."),
    ("Ulah ambek-ambek.", "Do not be angry."),
    ("Beungeutna beureum ku ambek.", "His face is red with anger."),
    ("Abdi sieun.", "I am afraid."),
    ("Budak sieun poek.", "The child fears the dark."),
    ("Ulah sieun, aya abdi.", "Do not be afraid, I am here."),
    ("Abdi bogoh ka anjeun.", "I love you."),
    ("Kanyaah indung taya watesna.", "A mother's love knows no bounds."),
    ("Manehna kaget ngadenge sora.", "He was startled hearing the sound."),
    ("Hadeuh, reuwas pisan!", "Oh, so startled!"),
    ("Abdi isin.", "I am shy."),
    ("Beungeutna beureum ku isin.", "Her face reddens with shyness."),
    ("Sing sabar.", "Be patient."),
    ("Hate nu tenang, awak nu sehat.", "A calm heart, a healthy body."),
]

NATURE20 = [
    ("Panonpoe bersinar.", "The sun shines."),
    ("Bulan pinuh peuting ieu.", "The moon is full tonight."),
    ("Bentang loba di langit.", "Many stars in the sky."),
    ("Hujan turun.", "Rain falls."),
    ("Angin niis gancang.", "The wind blows fast."),
    ("Halimun kandel isuk-isuk.", "Fog is thick in the morning."),
    ("Tangkal jangkung di leuweung.", "Tall trees in the forest."),
    ("Kembang mekar di buruan.", "Flowers bloom in the yard."),
    ("Anjing ngagonggong.", "The dog barks."),
    ("Ucing keur sare.", "The cat is sleeping."),
    ("Manuk hiber di langit.", "Birds fly in the sky."),
    ("Lauk ngojay di walungan.", "Fish swim in the river."),
    ("Embe dahar jukut.", "The goat eats grass."),
    ("Munding ngojay di balong.", "The buffalo wallows in the pond."),
    ("Hayam kongkorongok isuk-isuk.", "The rooster crows in the morning."),
    ("Orangutan? Henteu, monyet di tangkal.", "Not an orangutan; a monkey in the tree."),
    ("Usum hujan geus datang.", "The rainy season has come."),
    ("Usum halodo panas pisan.", "The dry season is very hot."),
    ("Taneuhna subur.", "The soil is fertile."),
    ("Alam Sunda endah pisan.", "Sundanese nature is very beautiful."),
]

SHOP20 = [
    ("Urang balanja ka pasar.", "We shop at the market."),
    ("Pasarna rame pisan.", "The market is very crowded."),
    ("Sabaraha hargana?", "How much is the price?"),
    ("Ieu lima rebu.", "This is five thousand."),
    ("Awis teuing!", "Too expensive!"),
    ("Mirah pisan.", "Very cheap."),
    ("Bisa kurang?", "Can it be less?"),
    ("Henteu tiasa, tos mirah.", "Cannot; already cheap."),
    ("Mangga, abdi beuli.", "Fine, I will buy it."),
    ("Aya kembalian?", "Is there change?"),
    ("Ieu kembalianana.", "Here is the change."),
    ("Abdi mesen tilu kilo beas.", "I order three kilos of rice."),
    ("Timbanganana pas?", "Is the scale accurate?"),
    ("Pas, mangga tingali.", "Accurate, please check."),
    ("Warungna buka isuk-isuk.", "The stall opens early morning."),
    ("Tutup jam salapan peuting.", "It closes at nine at night."),
    ("Mayar tunai atanapi transfer?", "Pay cash or transfer?"),
    ("Tunai we.", "Cash, please."),
    ("Hatur nuhun, mangga mampir deui.", "Thank you, please come again."),
    ("Sami-sami.", "You are welcome."),
]

FRIEND20 = [
    ("Anjeun sobat abdi.", "You are my friend."),
    ("Urang tepang di sakola.", "We met at school."),
    ("Wilujeng tepang.", "Nice to meet you."),
    ("Mangga calik.", "Please sit."),
    ("Ngopi heula.", "Have coffee first."),
    ("Kumaha kabarna?", "How have you been?"),
    ("Alhamdulillah sae.", "Thank God, fine."),
    ("Iraha urang ulin deui?", "When shall we hang out again?"),
    ("Isukan sore kumaha?", "How about tomorrow afternoon?"),
    ("Mangga, abdi bade milu.", "Sure, I will join."),
    ("Urang ulin ka puncak.", "We will go to the peak."),
    ("Bawa bekal masing-masing.", "Bring your own provisions."),
    ("Ulang taun abdi poe Minggu.", "My birthday is Sunday."),
    ("Mangga dongkap ka imah.", "Please come to my house."),
    ("Aya acara syukuran.", "There is a thanksgiving gathering."),
    ("Hatur nuhun tos dongkap.", "Thank you for coming."),
    ("Mugia urang sehat sadayana.", "May we all stay healthy."),
    ("Dulur saati, sobat sajati.", "One-hearted kin, true friends."),
    ("Dugi ka tepang deui.", "Until we meet again."),
    ("Sing ati-ati di jalan.", "Be careful on the road."),
]

TECH20 = [
    ("Abdi gaduh telepon.", "I have a telephone."),
    ("Nomor teleponna sabaraha?", "What is the phone number?"),
    ("Telepon abdi pareum.", "My phone is off."),
    ("Cas heula teleponna.", "Charge the phone first."),
    ("Aya sinyal?", "Is there signal?"),
    ("Sinyalna kuat.", "The signal is strong."),
    ("Kirim pesen ka abdi.", "Send me a message."),
    ("Pesenna geus dugi.", "The message has arrived."),
    ("Telepon ka indung.", "Call mother."),
    ("Abdi keur online.", "I am online."),
    ("Internétna gancang.", "The internet is fast."),
    ("Buka aplikasina.", "Open the application."),
    ("Klik tombol beureum.", "Click the red button."),
    ("Potona sae pisan.", "The photo is very good."),
    ("Kirim potona ka abdi.", "Send me the photo."),
    ("Komputerna anyar.", "The computer is new."),
    ("Ketik alamatna di dieu.", "Type the address here."),
    ("Simpen datana.", "Save the data."),
    ("Pareuman heula.", "Turn it off first."),
    ("Hurungkeun deui.", "Turn it on again."),
]

ENTRIES = [
    {
        "key": "overview",
        "name": "Sundanese Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Sundanese (Basa Sunda) is the Austronesian language of the "
            "Malayo-Polynesian branch (Malayo-Sumbawan subgroup) spoken as "
            "a mother tongue by about 40 million people, the second-largest "
            "native-speaker community in Indonesia after Javanese. With "
            "second-language users the total passes 44 million. It is the "
            "first language of West Java, Banten, and Jakarta's hinterland, "
            "with speaker communities in Lampung and southern Sumatra "
            "(transmigrants). The prestige standard is the Priangan "
            "dialect of Bandung; other major dialects are Banten, Bogor, "
            "and Cirebon.\n"
            "Indonesian is the national official language; Sundanese is the "
            "language of home, market, ceremony, and literature across the "
            "Sundanese highlands, taught in West Java schools and used in "
            "regional media and local government.\n"
            "Key facts a learner should hold from day one: (1) Sundanese "
            "has speech levels - undak usuk basa - and choosing the right "
            "level is choosing the right respect; the 1988 language "
            "congress simplified the old six levels to basa hormat "
            "(respectful) and basa loma (ordinary); (2) the language "
            "builds words with affixes (di-, N-, -an, -keun, -ar-) around "
            "a root; (3) there is no grammatical gender, no case, and no "
            "verb conjugation for person - one verb form serves all "
            "subjects; (4) the basic sentence order is subject-verb-object, "
            "like English. Example: " +
            _num_lines(OVERVIEW_SENTS)
        ),
        "how_it_works": (
            "Sundanese works as a root-and-affix system inside a "
            "respect-ranked vocabulary. The root carries the core idea - "
            "for example dahar (eat) - and affixes steer it: didahar "
            "(eaten, passive), kadaharan (food, the thing eaten). Parallel "
            "to this, nearly every everyday word has a level twin: dahar "
            "(loma) vs tuang (lemes) for \"eat\", kuring (neutral) vs abdi "
            "(humble) for \"I\". A speaker runs two gears at once - affixes "
            "for grammar, levels for respect. Learn the root families and "
            "the level pairs together and the whole language starts to "
            "unfold."
        ),
        "key_points": [
            "Sundanese (Basa Sunda): Austronesian family, Malayo-Polynesian branch, Malayo-Sumbawan subgroup.",
            "About 40 million native speakers; over 44 million total - the second-largest mother tongue in Indonesia.",
            "First language of West Java, Banten, and Jakarta's hinterland; transmigrant communities in Sumatra.",
            "Indonesian is the national official language; Sundanese rules home, market, ceremony, and literature.",
            "Prestige standard: Priangan (Bandung); Banten, Bogor, Cirebon dialects.",
            "Speech levels (undak usuk basa): 1988 congress simplified six levels to basa hormat and basa loma.",
            "Affix system (di-, N-, -an, -keun, -ar-) around a stable root.",
            "No gender, no case, no person conjugation; subject-verb-object order.",
        ],
        "requirements": [
            "No prior knowledge of Sundanese is assumed; the writing system record comes next.",
            "Accept that one idea has two words - the level, not the meaning, decides.",
            "Learn roots and affixes, not just whole words.",
        ],
        "standards": [
            "ISO 639-1 code su; ISO 639-3 code sun.",
            "Romanization in this database follows modern Indonesian-based Sundanese orthography.",
            "Speaker figures are best-available estimates, rounded, per the roster note.",
        ],
        "citations": [CIT_ETH, CIT_ADL, CIT_ISO, CIT_SPEAKERS],
        "sig_lens": (
            "The Signature read: Sundanese is the Language of the Stairway "
            "of Honor - a system where every word climbs or descends "
            "according to rank. The Signature Language Method learns "
            "Sundanese the way the highlands teach it: level first, word "
            "second, sentence last. Every vowel a gate of courtesy, every "
            "affix a family bond, every sentence a climb toward respect "
            "between speaker and listener."
        ),
        "drill": {
            "native_m": 40, "total_m": 44, "dialects": 6,
            "levels_old": 6, "levels_new": 2, "scripts": 3, "vowels": 7,
        },
        "must_contain": ["40", "Austronesian", "Basa Sunda", "undak usuk basa"],
    },
    {
        "key": "writing",
        "name": "The Sundanese Writing System",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Sundanese is written today mainly in the Latin alphabet with "
            "Indonesian-based spelling, standardized by the Palanggeran "
            "Ejahan Basa Sunda (2008). Alongside it lives the traditional "
            "Aksara Sunda, the standardized Sundanese script, encoded in "
            "Unicode 5.1 in the block U+1B80-U+1BBF and taught in West "
            "Java schools. The old Sundanese script (Aksara Sunda Kuno) "
            "appears on palm-leaf manuscripts such as the Bujangga Manik; "
            "religious texts historically used Pegon, the Arabic-based "
            "script.\n"
            "The script holds 18 basic letters (aksara ngalagena) in the "
            "traditional kaganga order: ka ga nga / ca ja nya / ta da na / "
            "pa ba ma / ya ra la / wa sa ha. Each consonant carries an "
            "inherent a, changed by rarangkén diacritics: panghulu (-i), "
            "panyuku (-u), paneuleung (-eu), paneleung (-é), pamepet (-e), "
            "panolong (-o), panyecek (-ng), panglayar (-r), pamingkal (-ya), "
            "panyakra (-ra), panyiku (-la), pangwisad (-h), and pamaeh, the "
            "vowel killer.\n"
            "Seven independent vowels: a, é, i, o, u, e, eu. The script "
            "has its own digits 0-9. Direction is left to right.\n"
            "Example lines: " +
            _num_lines([
                ("Aksara Sunda mibanda 18 aksara ngalagena.",
                 "The Sundanese script has 18 basic letters."),
                ("Rarangkén ngarobah sora vokal.", "Diacritics change the vowel sound."),
            ])
        ),
        "how_it_works": (
            "Read the script as consonant-plus-vowel beats: each ngalagena "
            "is read with a unless a rarangkén says otherwise, and pamaeh "
            "silences the vowel for closed syllables. Learn the kaganga "
            "order (ka ga nga, ca ja nya, ta da na, pa ba ma, ya ra la, wa "
            "sa ha) the way children chant it, then add the seven vowel "
            "signs one per day. The digits run 0-9 in their own shapes. "
            "In this database the running text uses Latin spelling; the "
            "script appears wherever the traditional form matters."
        ),
        "key_points": [
            "Three scripts in history: Latin (modern standard), Aksara Sunda, Pegon (religious).",
            "Aksara Sunda standardized in Unicode 5.1, block U+1B80-U+1BBF.",
            "18 aksara ngalagena in kaganga order: ka ga nga / ca ja nya / ta da na / pa ba ma / ya ra la / wa sa ha.",
            "13 rarangkén: vowel signs, -ng, -r, -ya, -ra, -la, -h, and pamaeh (vowel killer).",
            "Seven independent vowels: a, é, i, o, u, e, eu.",
            "Own digits 0-9; direction left to right.",
            "Modern spelling follows Palanggeran Ejahan Basa Sunda (2008).",
        ],
        "requirements": [
            "Chant the kaganga order until the 18 letters come in sequence.",
            "Write your name in Latin Sundanese spelling first, then in Aksara Sunda.",
            "Learn one rarangkén per day with three example syllables.",
        ],
        "standards": [
            "Aksara Sunda shapes and code points follow the Unicode Sundanese block (U+1B80-U+1BBF).",
            "Latin transliteration follows the 2008 Palanggeran spelling.",
            "Simplified running text writes é as e except where the é/e contrast is taught.",
        ],
        "citations": [CIT_UNI, CIT_EJA, CIT_ISO],
        "sig_lens": (
            "The Signature read: the script is the carved stairway - 18 "
            "stone steps in kaganga order, each rarangkén a handrail "
            "guiding the vowel upward. The Signature Language Method climbs "
            "the script the way the highlands climb: one step chanted, one "
            "sign mastered, until the whole mountain of letters stands "
            "open."
        ),
        "drill": {
            "ngalagena": 18,
            "order": ["ka", "ga", "nga", "ca", "ja", "nya", "ta", "da",
                      "na", "pa", "ba", "ma", "ya", "ra", "la", "wa",
                      "sa", "ha"],
            "vowels": 7, "digits": 10, "rarangken": 13,
        },
        "must_contain": ["Aksara Sunda", "ngalagena", "pamaeh", "kaganga"],
    },
    {
        "key": "phonology",
        "name": "Sundanese Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Sundanese has 7 vowels and 18 consonants. The vowels: a, i, u, "
            "é (/e/), o, e (/e/ pepet, the schwa), eu (/ɤ/, the high-mid "
            "back unrounded vowel that gives Sundanese its signature "
            "sound). Unlike Indonesian, Sundanese keeps é and e (pepet) "
            "apart: béas (uncooked rice) vs beas (tax, in loans). The 18 "
            "consonants: b, c (/tʃ/), d, g, h, j (/dʒ/), k, l, m, n, ny "
            "(/ɲ/), ng (/ŋ/), p, r, s, t, w, y. There are no native "
            "fricatives beyond s and h; loans add f, v, z, kh, sy. There "
            "is no dental/alveolar distinction as in Javanese.\n"
            "Stress falls on the penultimate syllable; questions rise in "
            "intonation at the end. A Sundanese signature: glides slip "
            "between vowels - kuéh is heard /kuwéh/, béar as /béjar/, "
            "miang as /mijang/.\n"
            "Spoken examples: " +
            _num_lines([
                ("cai", "water - the ai glides"),
                ("imah", "house"),
                ("dahar", "eat"),
                ("panonpoe", "sun - the oe glides"),
                ("bentang", "star"),
                ("peuting", "night - hear the eu"),
                ("isuk", "morning"),
                ("beas", "uncooked rice - hear the é"),
                ("bener", "true - hear the pepet e"),
                ("hujan", "rain"),
                ("seuri", "laugh"),
                ("meunang", "get - hear the eu twice"),
            ])
        ),
        "how_it_works": (
            "Train the ear on the two sounds Indonesian lacks: the pepet "
            "e (schwa) and the eu (/ɤ/). Minimal pairs drill the é/e split "
            "(béas vs beas). Stress the next-to-last syllable and let the "
            "glides (w, y) appear naturally between vowels - never force "
            "them. The 18 consonants match Indonesian spelling, so "
            "Indonesian speakers only add the vowels. Read the 12 example "
            "words aloud daily until eu stops feeling foreign."
        ),
        "key_points": [
            "7 vowels: a, i, u, é (/e/), o, e (pepet /ə/), eu (/ɤ/).",
            "18 consonants: b c d g h j k l m n ny ng p r s t w y.",
            "No native fricatives beyond s and h; loans add f, v, z, kh, sy.",
            "Stress on the penultimate syllable; rising intonation for questions.",
            "Glide insertion: kuéh -> /kuwéh/, béar -> /béjar/, miang -> /mijang/.",
            "12 spoken example words with English meanings.",
        ],
        "requirements": [
            "Say the 7 vowels in order until eu is steady.",
            "Drill é/e minimal pairs aloud.",
            "Read the 12 example words daily for a week.",
        ],
        "standards": [
            "Phoneme counts follow Adelaar (2005) and standard Sundanese grammars.",
            "IPA values: eu = /ɤ/, e (pepet) = /ə/, é = /e/.",
        ],
        "citations": [CIT_ADL, CIT_ETH],
        "sig_lens": (
            "The Signature read: the seven vowels are seven gates of "
            "courtesy - and eu, the sound no neighbor owns, is the "
            "innermost gate. The Signature Language Method tunes the ear "
            "gate by gate: master eu and the stairway of honor opens, "
            "because respect in Sundanese is first a sound, then a word."
        ),
        "drill": {
            "vowels": 7, "consonants": 18, "examples": 12,
            "loan_consonants": ["f", "v", "z", "kh", "sy"],
            "glides": [("kueh", "kuweh"), ("bear", "bejar"), ("miang", "mijang")],
        },
        "must_contain": ["pepet", "eu", "penultimate", "kuéh"],
    },
    {
        "key": "nouns1",
        "name": "Core Sundanese Nouns I",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "25 essential Sundanese nouns - person, place, thing - each "
            "with English and one example sentence, translated. Plurals "
            "come later; learn the singular forms cold.\n" +
            _num_lines([
                ("jalma - person", "Jalma éta someah. - That person is friendly."),
                ("budak - child", "Budak keur ulin. - The child is playing."),
                ("lalaki - man", "Lalaki éta petani. - That man is a farmer."),
                ("awewe - woman", "Awewe éta guru. - That woman is a teacher."),
                ("imah - house", "Imah abdi gedé. - My house is big."),
                ("panto - door", "Panto dibuka. - The door is opened."),
                ("jandela - window", "Jandela ditutup. - The window is closed."),
                ("meja - table", "Buku di luhur meja. - The book is on the table."),
                ("korsi - chair", "Diuk dina korsi. - Sit on the chair."),
                ("cai - water", "Cai herang. - The water is clear."),
                ("sangu - cooked rice", "Sangu geus asak. - The rice is cooked."),
                ("lauk - fish", "Laukna seger. - The fish is fresh."),
                ("buah - fruit", "Buahna amis. - The fruit is sweet."),
                ("tangkal - tree", "Tangkalna jangkung. - The tree is tall."),
                ("kembang - flower", "Kembangna seungit. - The flower is fragrant."),
                ("panonpoe - sun", "Panonpoe bersinar. - The sun shines."),
                ("bulan - moon", "Bulan pinuh. - The moon is full."),
                ("bentang - star", "Bentang loba. - The stars are many."),
                ("langit - sky", "Langit biru. - The sky is blue."),
                ("taneuh - earth / soil", "Taneuhna subur. - The soil is fertile."),
                ("jalan - road", "Jalanna lega. - The road is wide."),
                ("pasar - market", "Pasar rame. - The market is crowded."),
                ("kota - city", "Kotana gedé. - The city is big."),
                ("lembur - village", "Lemburna asri. - The village is lovely."),
                ("nagara - country", "Nagara urang endah. - Our country is beautiful."),
            ])
        ),
        "how_it_works": (
            "Nouns never change form - no gender, no case, no plural "
            "ending. The suffix -na marks possession or definiteness "
            "(imahna: his house / the house). Point at objects and name "
            "them: imah, panto, jandela. Build the sentence frame "
            "[noun] + [adjective] and the 25 nouns become 25 sentences."
        ),
        "key_points": [
            "25 essential nouns with English and a translated example sentence each.",
            "Nouns are invariable: no gender, no case, no plural suffix.",
            "The -na suffix marks possession or definiteness.",
            "Sentence frame: noun + adjective.",
        ],
        "requirements": [
            "Name 10 household objects in Sundanese from memory.",
            "Use each noun once in a noun + adjective sentence.",
        ],
        "standards": [
            "Vocabulary follows standard Priangan Sundanese usage.",
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL, CIT_EJA],
        "sig_lens": (
            "The Signature read: nouns are the stones of the stairway - "
            "jalma, imah, cai - each one set solid before the climb. The "
            "Signature Language Method lays 25 stones first, because no "
            "sentence climbs without footing."
        ),
        "drill": {"nouns": [n for n, _ in NOUNS25]},
        "must_contain": ["jalma", "panonpoe", "taneuh", "25"],
    },
    {
        "key": "verbs1",
        "name": "Core Sundanese Verbs I",
        "group": "Core Vocabulary",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "25 essential Sundanese verbs - each with English and one "
            "example sentence, translated. One form serves every subject; "
            "time is marked by separate words (geus, keur, rek), covered "
            "in the tenses record.\n" +
            _num_lines([
                ("dahar - eat", "Abdi dahar sangu. - I eat rice."),
                ("nginum - drink", "Manehna nginum cai. - He drinks water."),
                ("sare - sleep", "Budak sare. - The child sleeps."),
                ("hudang - wake up", "Abdi hudang jam lima. - I wake at five."),
                ("leumpang - walk", "Urang leumpang ka pasar. - We walk to the market."),
                ("lumpat - run", "Budak lumpat gancang. - The child runs fast."),
                ("diuk - sit", "Mangga diuk. - Please sit."),
                ("nangtung - stand", "Manehna nangtung. - He stands."),
                ("nyarita - speak", "Anjeun nyarita basa Sunda. - You speak Sundanese."),
                ("nanya - ask", "Abdi nanya ka guru. - I ask the teacher."),
                ("maca - read", "Manehna maca buku. - She reads a book."),
                ("nulis - write", "Abdi nulis surat. - I write a letter."),
                ("meuli - buy", "Indung meuli beas. - Mother buys rice."),
                ("ngajual - sell", "Bapa ngajual lauk. - Father sells fish."),
                ("nyieun - make", "Ibu nyieun kueh. - Mother makes cake."),
                ("ibak - bathe", "Budak ibak isuk-isuk. - The child bathes in the morning."),
                ("seuri - laugh", "Barudak seuri. - The children laugh."),
                ("ceurik - cry", "Orok ceurik. - The baby cries."),
                ("indit - go", "Abdi indit ka sakola. - I go to school."),
                ("datang - come", "Tamu datang. - The guest comes."),
                ("balik - go home / return", "Urang balik sonten. - We go home in the afternoon."),
                ("gawe - work", "Bapa gawe di kantor. - Father works at an office."),
                ("diajar - study", "Murid diajar. - The student studies."),
                ("ulin - play", "Barudak ulin bal. - The children play ball."),
                ("nempo - see / watch", "Abdi nempo pilem. - I watch a film."),
            ])
        ),
        "how_it_works": (
            "Verbs do not conjugate: dahar stays dahar for I, you, he, "
            "they. Bolt on time words - geus dahar (have eaten), keur "
            "dahar (am eating), rek dahar (will eat). The nasal prefix "
            "N- builds active verbs from roots (tulis -> nulis). Practice "
            "by swapping subjects under one verb: Abdi indit, anjeun "
            "indit, maranehna indit."
        ),
        "key_points": [
            "25 essential verbs with English and a translated example sentence each.",
            "No conjugation for person or number.",
            "Time is marked by geus (already), keur (currently), rek (about to).",
            "Active verbs often carry the nasal prefix N- (tulis -> nulis).",
        ],
        "requirements": [
            "Conjugate nothing: say each verb with three different subjects.",
            "Add geus, keur, and rek to five verbs.",
        ],
        "standards": [
            "Verb forms follow standard Priangan Sundanese usage.",
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL, CIT_EJA],
        "sig_lens": (
            "The Signature read: verbs are the climbers on the stairway - "
            "dahar, indit, diajar - each step taken the same by every "
            "foot. The Signature Language Method marches the verbs in "
            "place: one form, all climbers, no stragglers."
        ),
        "drill": {"verbs": [v for v, _ in VERBS25]},
        "must_contain": ["dahar", "geus", "rek", "25"],
    },
    {
        "key": "adjadv",
        "name": "Sundanese Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "25 adjectives and 15 adverbs - each with English and a "
            "translated example sentence. Adjectives follow the noun "
            "(imah gedé, a big house) and never change form; intensity "
            "comes from pisan (very), leuwih (more), and pang- (most).\n" +
            _num_lines([
                ("alus - good", "Jalma alus. - A good person."),
                ("goreng - bad", "Kalakuan goreng. - Bad behavior."),
                ("gede - big", "Imah gede. - A big house."),
                ("leutik - small", "Budak leutik. - A small child."),
                ("panjang - long", "Jalan panjang. - A long road."),
                ("pondok - short", "Carita pondok. - A short story."),
                ("jangkung - tall", "Tangkal jangkung. - A tall tree."),
                ("handap - low", "Sora handap. - A low voice."),
                ("anyar - new", "Buku anyar. - A new book."),
                ("kolot - old", "Imah kolot. - An old house."),
                ("ngora - young", "Guru ngora. - A young teacher."),
                ("geulis - beautiful", "Awewe geulis. - A beautiful woman."),
                ("pinter - smart", "Murid pinter. - A smart student."),
                ("beunghar - rich", "Jalma beunghar. - A rich person."),
                ("miskin - poor", "Kulawarga miskin. - A poor family."),
                ("panas - hot", "Cai panas. - Hot water."),
                ("tiis - cold", "Angin tiis. - Cold wind."),
                ("amis - sweet", "Buah amis. - Sweet fruit."),
                ("pait - bitter", "Ubar pait. - Bitter medicine."),
                ("asin - salty", "Lauk asin. - Salty fish."),
                ("lada - spicy", "Sambel lada. - Spicy chili sauce."),
                ("beurat - heavy", "Tas beurat. - A heavy bag."),
                ("hampang - light", "Koper hampang. - A light suitcase."),
                ("gancang - fast", "Mobil gancang. - A fast car."),
                ("kuat - strong", "Lalaki kuat. - A strong man."),
                ("pisan - very", "Alus pisan. - Very good."),
                ("leuwih - more", "Leuwih gede. - Bigger."),
                ("geus - already", "Geus rengse. - Already finished."),
                ("acan - not yet", "Acan dahar. - Not eaten yet."),
                ("keur - currently", "Keur diajar. - Currently studying."),
                ("rek - about to", "Rek indit. - About to go."),
                ("tangtu - certainly", "Tangtu datang. - Will certainly come."),
                ("meureun - maybe", "Meureun hujan. - Maybe it will rain."),
                ("saban - every", "Saban poe. - Every day."),
                ("ayeuna - now", "Dahar ayeuna. - Eat now."),
                ("kamari - yesterday", "Kamari hujan. - Yesterday it rained."),
                ("isukan - tomorrow", "Isukan libur. - Tomorrow is a holiday."),
                ("lalaunan - slowly", "Leumpang lalaunan. - Walk slowly."),
                ("oge - also / too", "Abdi oge. - Me too."),
                ("bae - just / only", "Sakedik bae. - Just a little."),
            ])
        ),
        "how_it_works": (
            "Adjectives sit after the noun and never inflect: imah gedé, "
            "imah-imah gedé. Compare with leuwih (leuwih alus, better), "
            "go superlative with pang- (pangalusna, the best), and "
            "intensify with pisan (alus pisan, very good). Adverbs of time "
            "(ayeuna, kamari, isukan) float to the front or back of the "
            "sentence. Drill: take one noun through all 25 adjectives."
        ),
        "key_points": [
            "25 adjectives + 15 adverbs = 40 modifiers, each with a translated sentence.",
            "Adjectives follow the noun and never change form.",
            "Comparison: leuwih (more), pang- (most); intensity: pisan (very).",
            "Time adverbs (ayeuna, kamari, isukan) mark tense instead of verb endings.",
        ],
        "requirements": [
            "Describe five objects using noun + adjective.",
            "Compare three things with leuwih and pang-.",
            "Place ayeuna, kamari, and isukan in sentences.",
        ],
        "standards": [
            "Modifier forms follow standard Priangan Sundanese usage.",
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL, CIT_EJA],
        "sig_lens": (
            "The Signature read: adjectives are the colors painted on the "
            "stairway stones, adverbs the pace of the climb - pisan the "
            "steep step, lalaunan the gentle one. The Signature Language "
            "Method paints every stone before climbing higher."
        ),
        "drill": {"adjectives": [a for a, _ in ADJ25],
                  "adverbs": [a for a, _ in ADV15]},
        "must_contain": ["pisan", "leuwih", "pang-", "40"],
    },
    {
        "key": "pronouns",
        "name": "Sundanese Pronouns",
        "group": "Core Vocabulary",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Personal, possessive, demonstrative, and interrogative "
            "pronouns - full paradigms with example sentences. Sundanese "
            "pronouns carry no gender; they carry rank. First person: abdi "
            "(humble polite), sim kuring (formal), kuring (neutral), aing "
            "(very informal). Second person: anjeun (polite), salira "
            "(refined), maneh (informal), sia (coarse). Third person: "
            "manehna (he/she, neutral), maranehna (they). We: urang "
            "(inclusive), kami (exclusive). Possession uses the noun plus "
            "pronoun (buku abdi, my book) or the -na suffix (bukuna, "
            "his/her book). Demonstratives: ieu (this), eta (that).\n" +
            _num_lines([
                ("Abdi teh urang Sunda.", "I am Sundanese."),
                ("Kuring indit ka pasar.", "I (neutral) go to the market."),
                ("Anjeun timana?", "Where are you from?"),
                ("Salira bade tuang?", "Will you (refined) eat?"),
                ("Manehna guru.", "He/she is a teacher."),
                ("Maranehna murid.", "They are students."),
                ("Urang dahar babarengan.", "We (inclusive) eat together."),
                ("Kami geus rengse.", "We (exclusive) have finished."),
                ("Buku abdi anyar.", "My book is new."),
                ("Imahna gedé.", "His/her house is big."),
                ("Ieu buku abdi.", "This is my book."),
                ("Eta imah bapa.", "That is father's house."),
                ("Saha nami anjeun?", "What is your name?"),
                ("Naon ieu?", "What is this?"),
                ("Dimana imah anjeun?", "Where is your house?"),
                ("Iraha anjeun datang?", "When did you arrive?"),
                ("Naha anjeun ceurik?", "Why are you crying?"),
                ("Kumaha damang?", "How are you?"),
                ("Sabaraha hargana?", "How much is it?"),
                ("Nu mana?", "Which one?"),
            ])
        ),
        "how_it_works": (
            "Choose the pronoun by rank first, meaning second: abdi to "
            "elders, kuring to friends, aing never outside close peers. "
            "Possession needs no 'of': buku abdi (my book), imah anjeun "
            "(your house); -na clings to the noun for his/her/its. "
            "Interrogatives (saha, naon, dimana, iraha, naha, kumaha, "
            "sabaraha) open questions with rising intonation. Drill pairs: "
            "ask and answer every interrogative daily."
        ),
        "key_points": [
            "No gender in any pronoun; rank decides the form.",
            "I: abdi / sim kuring / kuring / aing across four ranks.",
            "You: salira / anjeun / maneh / sia across four ranks.",
            "Possession: pronoun after noun (buku abdi) or -na suffix (bukuna).",
            "Demonstratives: ieu (this), eta (that).",
            "Eight interrogatives: saha, naon, dimana, iraha, naha, kumaha, sabaraha, nu mana.",
            "20 paradigm sentences, fully translated.",
        ],
        "requirements": [
            "Address an elder with abdi and a friend with kuring in roleplay.",
            "Form possessives both ways for five nouns.",
            "Ask and answer all eight interrogatives.",
        ],
        "standards": [
            "Pronoun ranks follow documented undak usuk basa usage.",
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL, CIT_EJA],
        "sig_lens": (
            "The Signature read: pronouns are the bows exchanged on the "
            "stairway - abdi bows low, kuring stands level, aing never "
            "bows at all. The Signature Language Method teaches the bow "
            "before the word, because in Sundanese the rank arrives before "
            "the meaning."
        ),
        "drill": {"pronouns": [p for p, _ in PRONOUNS],
                  "interrogatives": ["saha", "naon", "dimana", "iraha",
                                     "naha", "kumaha", "sabaraha", "nu mana"]},
        "must_contain": ["abdi", "manehna", "-na", "ieu"],
    },
    {
        "key": "numbers",
        "name": "Sundanese Numbers and Time",
        "group": "Core Vocabulary",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Sundanese numbers run base-10: hiji (1) through sapuluh (10), "
            "then compounds - dua puluh (20), saratus (100), sarebu "
            "(1000), sajuta (1,000,000). Teens add belas (sabelas 11, dua "
            "belas 12). Ordinals take ka-: kahiji (first), kadua (second), "
            "katilu (third).\n"
            "Days: Senen, Salasa, Rebo, Kemis, Jumaah, Saptu, Minggu. "
            "Months use the Gregorian names: Januari through Desember. "
            "Clock time: jam hiji (1 o'clock), jam satengah tujuh (half "
            "past six), jam dalapan kurang saparapat (quarter to eight).\n"
            "20 number-and-time sentences: " +
            _num_lines([
                ("Abdi gaduh anak dua.", "I have two children."),
                ("Hargana sarebu rupiah.", "The price is a thousand rupiah."),
                ("Poe Senen abdi gawe.", "On Monday I work."),
                ("Isukan poe Salasa.", "Tomorrow is Tuesday."),
                ("Ayeuna jam tujuh.", "Now it is seven o'clock."),
                ("Abdi dongkap jam satengah dalapan.", "I arrived at half past seven."),
                ("Bulan Januari geus datang.", "The month of January has come."),
                ("Ulang taun abdi kaping tilu.", "My birthday is the third."),
                ("Abdi meuli tilu.", "I buy three."),
                ("Umurna lima puluh taun.", "His age is fifty years."),
                ("Sakolana saratus meter.", "The school is a hundred meters away."),
                ("Poe Jumaah libur.", "Friday is a holiday."),
                ("Kamari poe Kemis.", "Yesterday was Thursday."),
                ("Isukan isuk jam genep.", "Tomorrow morning at six o'clock."),
                ("Abdi dahar tilu kali sapoe.", "I eat three times a day."),
                ("Budak opat keur ulin.", "Four children are playing."),
                ("Kareta datang jam dalapan.", "The train comes at eight."),
                ("Taun ieu taun hareup?", "This year or next year?"),
                ("Jam sabaraha ayeuna?", "What time is it now?"),
                ("Jam dua belas kurang saparapat.", "A quarter to twelve."),
            ])
        ),
        "how_it_works": (
            "Numbers stack by place with no connecting words: saratus lima "
            "puluh (150). Teens are root + belas; tens are root + puluh. "
            "Time phrases bolt onto jam (o'clock), poe (day), bulan "
            "(month), taun (year): jam tujuh isuk (7 in the morning), poe "
            "Senen (Monday). Ordinals prefix ka-. Count objects aloud to "
            "twenty daily until dua puluh hiji comes without thought."
        ),
        "key_points": [
            "Base-10 cardinals: hiji through sapuluh, then compounds.",
            "Teens: root + belas (sabelas, dua belas).",
            "Tens: root + puluh; hundreds saratus; thousands sarebu.",
            "Ordinals: ka- prefix (kahiji, kadua, katilu).",
            "Seven weekday names; Gregorian month names.",
            "Clock time uses jam + number; satengah and saparapat phrases.",
            "20 number-and-time sentences, fully translated.",
        ],
        "requirements": [
            "Count 1-20 aloud, then by tens to 100.",
            "Say today's weekday and date from memory.",
            "Tell the time for five different hours.",
        ],
        "standards": [
            "Number forms follow standard Sundanese usage.",
            "Weekday and month names follow current West Java usage.",
        ],
        "citations": [CIT_ADL, CIT_EJA],
        "sig_lens": (
            "The Signature read: numbers are the counted steps of the "
            "stairway - hiji the first stone, sarebu the thousandth, each "
            "one true. The Signature Language Method drills counting as a "
            "covenant march: one to twenty, no stragglers, until the days "
            "of the week fall in line behind."
        ),
        "drill": {"numbers": [n for n, _ in NUMBERS],
                  "days": DAYS, "months": MONTHS,
                  "ordinals": [o for o, _ in ORDINALS]},
        "must_contain": ["hiji", "sapuluh", "sarebu", "kahiji"],
    },
    {
        "key": "greetings",
        "name": "Sundanese Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "30 greetings, farewells, and politeness phrases - each with "
            "English meaning and a usage note. The crown greeting is "
            "sampurasun, answered by rampes; time-of-day greetings use "
            "wilujeng (enjing, siang, sonten, wengi).\n" +
            _num_lines([(s, e) for s, e in GREET30])
        ),
        "how_it_works": (
            "Greet by the sun: wilujeng enjing before midday, wilujeng "
            "siang at midday, wilujeng sonten in the afternoon, wilujeng "
            "wengi at night. Answer sampurasun with rampes - the pair is "
            "a ritual, never half of it. Thank with hatur nuhun, excuse "
            "yourself with punten, ask forgiveness with hampura, and open "
            "every request with mangga. Part with wilujeng angkat and the "
            "blessing mugia salamet."
        ),
        "key_points": [
            "30 greetings and politeness phrases with usage notes.",
            "Sampurasun is answered by rampes - always the pair.",
            "Wilujeng + time of day covers all daytime greetings.",
            "Hatur nuhun (thanks), punten (excuse me), hampura (sorry), mangga (please).",
            "Kumaha damang? is answered pangestu, alhamdulillah.",
        ],
        "requirements": [
            "Greet by time of day without checking notes.",
            "Perform the sampurasun/rampes exchange in roleplay.",
            "Thank, excuse, and apologize in three scenarios.",
        ],
        "standards": [
            "Greeting forms follow standard polite Sundanese usage.",
        ],
        "citations": [CIT_ADL, CIT_EJA],
        "sig_lens": (
            "The Signature read: greetings are the handrails of the "
            "stairway - sampurasun the first rail every climber touches. "
            "The Signature Language Method teaches the greeting before the "
            "grammar, because the handrail is grasped before the first "
            "step."
        ),
        "drill": {"greetings": [g for g, _ in GREET30]},
        "must_contain": ["Sampurasun", "rampes", "Wilujeng", "Hatur nuhun"],
    },
    {
        "key": "grammar",
        "name": "Sundanese Grammar Essentials",
        "group": "Grammar Essentials",
        "ladder_rank": 10,
        "ladder_tier": "compounded",
        "description": (
            "The ten load-bearing rules of Sundanese grammar - each rule "
            "with translated example sentences. Master these ten and the "
            "whole language stands.\n" +
            _num_lines([(r, "%s - %s" % (s, e)) for r, s, e in GRAMMAR10])
        ),
        "how_it_works": (
            "Sundanese grammar is spare: SVO order, no gender, no case, "
            "no conjugation. Meaning rides on word choice and small "
            "helper words: -na for possession, di- for passive, N- for "
            "active, geus/keur/rek for time, henteu/teu/moal/ulah for "
            "negation. Plurals repeat or infix -ar-. Questions rise in "
            "tone. Learn the ten rules as ten tools; every later record "
            "is these tools at work."
        ),
        "key_points": [
            "SVO word order; no gender, no case, no person conjugation.",
            "Plural via reduplication and the -ar- infix (budak -> barudak).",
            "Negation: henteu/teu (not), moal (will not), ulah (do not).",
            "Questions: interrogative word + rising intonation, no particle.",
            "Passive di-, active nasal N-, possessive -na.",
            "Time words geus/keur/rek replace tense endings.",
            "Adjectives follow nouns; pisan/leuwih/pang- grade them.",
            "10 rules, each with translated example sentences.",
        ],
        "requirements": [
            "Build one sentence per rule from scratch.",
            "Convert five active sentences to passive with di-.",
            "Negate five sentences three ways (teu, moal, ulah).",
        ],
        "standards": [
            "Grammar rules follow Adelaar (2005) and standard Sundanese grammars.",
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL, CIT_EJA],
        "sig_lens": (
            "The Signature read: the ten rules are the ten commandments "
            "of the stairway - short, load-bearing, unbreakable. The "
            "Signature Language Method carves them in order: climb one "
            "rule, master it, then the next; no climber skips a step."
        ),
        "drill": {"rules": 10},
        "must_contain": ["subject-verb-object", "barudak", "di-", "geus"],
    },
    {
        "key": "home",
        "name": "Sundanese Home and Family Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 11,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: house, rooms, furniture, family members.\n" +
            _num_lines(HOME20)
        ),
        "how_it_works": (
            "Home sentences teach location words (di, di luhur, di "
            "tukang, di hareup) and family terms (bapa, indung, aki, "
            "nini, dulur, lanceuk, adi). Possession runs through -na and "
            "pronouns: imah abdi, kamar sare abdi. Describe your own "
            "house room by room in Sundanese; the vocabulary sticks "
            "because the rooms are yours."
        ),
        "key_points": [
            "20 home-and-family sentences, fully translated.",
            "Location words: di, di luhur, di tukang, di hareup.",
            "Family terms: bapa, indung, aki, nini, dulur, lanceuk, adi.",
            "Possession via pronouns and -na.",
        ],
        "requirements": [
            "Describe your own home room by room in Sundanese.",
            "Name all family members with the right terms.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: home is the foot of the stairway - every "
            "climb begins at the panto and every return ends there. The "
            "Signature Language Method names the rooms first, because the "
            "climber must know where the stairway stands."
        ),
        "drill": {"sentences": 20, "rooms": ["kamar", "dapur", "buruan"]},
        "must_contain": ["imah", "Indung", "buruan", "20"],
    },
    {
        "key": "food",
        "name": "Sundanese Food and Cooking Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 12,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: meals, ingredients, cooking actions, "
            "restaurant. Note the rice words: paré (the plant), béas "
            "(uncooked rice), sangu (cooked rice).\n" +
            _num_lines(FOOD20)
        ),
        "how_it_works": (
            "Food sentences drill the three rice words (paré, béas, "
            "sangu) - mixing them marks a beginner instantly. Cooking "
            "verbs (masak, goreng) pair with taste adjectives (amis, "
            "pait, asin, lada). Restaurant phrases run on sabaraha and "
            "saporsi. Order a full meal in roleplay: greeting, order, "
            "price, thanks."
        ),
        "key_points": [
            "20 food-and-cooking sentences, fully translated.",
            "Three rice words: paré (plant), béas (uncooked), sangu (cooked).",
            "Taste adjectives: amis, pait, asin, lada.",
            "Restaurant pattern: sabaraha + saporsi + hatur nuhun.",
        ],
        "requirements": [
            "Use paré, béas, and sangu each in a correct sentence.",
            "Order a two-course meal in roleplay.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: food is the fuel of the climb - sangu "
            "the staple stone every climber carries. The Signature "
            "Language Method feeds the student first: no one climbs the "
            "stairway of honor hungry."
        ),
        "drill": {"sentences": 20, "rice_words": ["pare", "beas", "sangu"]},
        "must_contain": ["sangu", "Beas", "saporsi", "20"],
    },
    {
        "key": "travel",
        "name": "Sundanese Travel and Directions Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: transport, asking directions, tickets, "
            "lodging.\n" +
            _num_lines(TRAVEL20)
        ),
        "how_it_works": (
            "Travel sentences run on direction words (terus, kenca, "
            "katuhu, hareup, tukang) and the polite opener punten. Fares "
            "and times use the number record: dua puluh rebu, jam tujuh. "
            "Lodging questions use aya (is there): aya cai haneut? "
            "Practice by giving directions from your door to the market "
            "without notes."
        ),
        "key_points": [
            "20 travel-and-direction sentences, fully translated.",
            "Direction words: terus, kenca, katuhu, hareup, tukang.",
            "Polite opener punten for every stranger question.",
            "Fares and times reuse the number record.",
        ],
        "requirements": [
            "Give directions from your door to the market.",
            "Buy a ticket and book a room in roleplay.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: travel is the stairway extended - every "
            "jalan a continuation of the climb, every traveler a fellow "
            "climber. The Signature Language Method sends the student "
            "out: the stairway of honor is walked, not memorized."
        ),
        "drill": {"sentences": 20,
                  "directions": ["terus", "kenca", "katuhu", "hareup", "tukang"]},
        "must_contain": ["Kareta", "tiket", "Punten", "20"],
    },
    {
        "key": "work",
        "name": "Sundanese Work and School Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: jobs, office, classroom, learning.\n" +
            _num_lines(WORK20)
        ),
        "how_it_works": (
            "Work sentences name professions (guru, dokter, petani, "
            "padagang, montir, koki, supir) and school life (murid, "
            "pelajaran, PR). Time discipline runs on jam: jam tujuh, jam "
            "dalapan. The ethic sentence - gawe nu getol sangkan suksés - "
            "carries the culture: diligence is praised openly. Describe "
            "your own job or studies in ten sentences."
        ),
        "key_points": [
            "20 work-and-school sentences, fully translated.",
            "Profession vocabulary: guru, dokter, petani, padagang, montir, koki, supir.",
            "School vocabulary: murid, pelajaran, PR, sakola.",
            "Time discipline: jam + number.",
        ],
        "requirements": [
            "Describe your job or studies in ten Sundanese sentences.",
            "Name seven professions from memory.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: work is the daily climbing - gawe the "
            "verb that lifts the stone each morning. The Signature "
            "Language Method honors the worker's vocabulary first, "
            "because the stairway of honor was built by working hands."
        ),
        "drill": {"sentences": 20,
                  "professions": ["guru", "dokter", "petani", "padagang",
                                  "montir", "koki", "supir"]},
        "must_contain": ["gawe", "sakola", "Murid", "20"],
    },
    {
        "key": "health",
        "name": "Sundanese Health and Body Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: body parts, symptoms, doctor visit, pharmacy.\n" +
            _num_lines(HEALTH20)
        ),
        "how_it_works": (
            "Health sentences center the body (sirah, awak, beuteung, "
            "huntu, panon, suku, leungeun) plus the symptom verb nyeri "
            "(aches) and the state muriang (feverish). The doctor visit "
            "runs: complaint, examination, obat, dosage (tilu kali "
            "sapoe). Learn these before you need them - this record is "
            "the one you will use in an emergency."
        ),
        "key_points": [
            "20 health-and-body sentences, fully translated.",
            "Body parts: sirah, awak, beuteung, huntu, panon, suku, leungeun.",
            "Symptom words: nyeri (aches), muriang (feverish), batuk (cough).",
            "Doctor-visit pattern: complaint, obat, dosage.",
        ],
        "requirements": [
            "Name ten body parts from memory.",
            "Describe three symptoms to a doctor in roleplay.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
            "Health phrases are language study, not medical advice.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: the body is the climber - sirah the "
            "lookout, suku the stepper, hate the engine. The Signature "
            "Language Method teaches the climber's own parts first, "
            "because no stairway is climbed without them."
        ),
        "drill": {"sentences": 20,
                  "body": ["sirah", "awak", "beuteung", "huntu", "panon",
                           "suku", "leungeun"]},
        "must_contain": ["nyeri", "dokter", "obat", "20"],
    },
    {
        "key": "emotions",
        "name": "Sundanese Emotions and Feelings Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: happy, sad, angry, afraid, love, surprise.\n" +
            _num_lines(EMOTION20)
        ),
        "how_it_works": (
            "Emotion sentences pair the feeling word (bungah, sedih, "
            "ambek, sieun, bogoh, kaget, isin) with the body that shows "
            "it: beungeut beureum (red face), cimata murag (tears fall). "
            "Comfort phrases (ulah sieun, sing sabar) are social tools - "
            "use them on others, not just yourself. Say each feeling "
            "with its face: the intonation teaches the word."
        ),
        "key_points": [
            "20 emotion sentences, fully translated.",
            "Core feelings: bungah, sedih, ambek, sieun, bogoh, kaget, isin.",
            "Body-linked expressions: beungeut beureum, cimata murag.",
            "Comfort phrases: ulah sieun, sing sabar.",
        ],
        "requirements": [
            "Express seven feelings with face and intonation.",
            "Comfort a sad friend in roleplay.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: feelings are the weather on the stairway "
            "- bungah the sunrise, sedih the rain, ambek the storm every "
            "climber learns to walk through. The Signature Language "
            "Method names the weather so the climber is never caught "
            "without words."
        ),
        "drill": {"sentences": 20,
                  "feelings": ["bungah", "sedih", "ambek", "sieun",
                               "bogoh", "kaget", "isin"]},
        "must_contain": ["bungah", "ambek", "bogoh", "20"],
    },
    {
        "key": "nature",
        "name": "Sundanese Nature and Weather Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: animals, plants, seasons, weather talk. The "
            "highland climate gives two seasons: usum hujan (rainy) and "
            "usum halodo (dry).\n" +
            _num_lines(NATURE20)
        ),
        "how_it_works": (
            "Nature sentences stock the landscape: panonpoe, bulan, "
            "bentang, hujan, angin, halimun, tangkal, kembang, walungan, "
            "gunung. Animal verbs are vivid: ngagonggong (bark), hiber "
            "(fly), ngojay (swim), kongkorongok (crow). Weather talk "
            "opens conversations - master hujan turun and usum hujan "
            "geus datang as small talk. Walk outside and name ten things "
            "you see."
        ),
        "key_points": [
            "20 nature-and-weather sentences, fully translated.",
            "Two seasons: usum hujan (rainy), usum halodo (dry).",
            "Landscape words: walungan, gunung, leuweung, balong.",
            "Vivid animal verbs: ngagonggong, hiber, ngojay, kongkorongok.",
        ],
        "requirements": [
            "Name ten natural things seen on a walk.",
            "Make weather small talk for both seasons.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: nature is the mountain the stairway "
            "climbs - every panonpoe a lamp, every hujan a blessing on "
            "the steps. The Signature Language Method walks the student "
            "outside: the stairway of honor stands in real weather."
        ),
        "drill": {"sentences": 20, "seasons": ["usum hujan", "usum halodo"]},
        "must_contain": ["usum hujan", "walungan", "Bentang", "20"],
    },
    {
        "key": "shopping",
        "name": "Sundanese Shopping and Money Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: market, prices, bargaining, paying.\n" +
            _num_lines(SHOP20)
        ),
        "how_it_works": (
            "Market sentences run the bargaining dance: sabaraha hargana "
            "(how much), awis teuing (too expensive), bisa kurang (can "
            "it be less), mirah pisan (very cheap). Prices count in rebu "
            "(thousands). Pay with tunai or transfer; always confirm the "
            "timbangan (scale). Bargain a full purchase in roleplay from "
            "greeting to sami-sami."
        ),
        "key_points": [
            "20 shopping-and-money sentences, fully translated.",
            "Bargaining arc: sabaraha -> awis teuing -> bisa kurang -> deal.",
            "Prices in rebu (thousands).",
            "Payment: tunai (cash) or transfer; check the timbangan.",
        ],
        "requirements": [
            "Bargain a purchase start to finish in roleplay.",
            "State five prices in rebu without hesitation.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: the market is the stairway's landing - "
            "where climbers meet, bargain, and part as neighbors. The "
            "Signature Language Method teaches the honest bargain: "
            "sabaraha asked fairly, hatur nuhun given freely."
        ),
        "drill": {"sentences": 20},
        "must_contain": ["Sabaraha", "rebu", "Timbangan", "20"],
    },
    {
        "key": "friendship",
        "name": "Sundanese Friendship and Social Life Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: meeting people, invitations, celebrations.\n" +
            _num_lines(FRIEND20)
        ),
        "how_it_works": (
            "Friendship sentences open with wilujeng tepang (nice to "
            "meet you) and run on invitations: mangga dongkap (please "
            "come), bawa bekal masing-masing (bring your own provisions). "
            "Celebrations use syukuran (thanksgiving gathering). The "
            "closing ethic - dulur saati, sobat sajati - says friendship "
            "is kinship chosen. Invite a friend somewhere real this week."
        ),
        "key_points": [
            "20 friendship sentences, fully translated.",
            "Meeting: wilujeng tepang; invitation: mangga dongkap.",
            "Celebration: syukuran (thanksgiving gathering).",
            "Ethic: dulur saati, sobat sajati (kin of one heart, true friends).",
        ],
        "requirements": [
            "Introduce yourself to a stranger in roleplay.",
            "Extend and accept an invitation.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: friendship is climbing together - dulur "
            "saati, one heart on the stairway. The Signature Language "
            "Method never climbs alone: invite, share bekal, and the "
            "steps grow easier."
        ),
        "drill": {"sentences": 20},
        "must_contain": ["sobat", "syukuran", "tepang", "20"],
    },
    {
        "key": "technology",
        "name": "Sundanese Technology and Communication Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences: phone, internet, computer, messaging.\n" +
            _num_lines(TECH20)
        ),
        "how_it_works": (
            "Technology sentences borrow freely: telepon, internét, "
            "komputer, aplikasi, sinyal, online - international words in "
            "Sundanese mouths. Core verbs stay native: kirim (send), "
            "cas (charge), klik (click), ketik (type), simpen (save), "
            "hurungkeun/pareuman (turn on/off). Troubleshoot a dead "
            "phone in Sundanese: pareum, cas, hurungkeun deui."
        ),
        "key_points": [
            "20 technology sentences, fully translated.",
            "Loanwords: telepon, internét, komputer, aplikasi, sinyal.",
            "Native verbs: kirim, cas, klik, ketik, simpen.",
            "On/off: hurungkeun / pareuman.",
        ],
        "requirements": [
            "Troubleshoot a dead phone in Sundanese.",
            "Send a message and make a call in roleplay.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: technology is the new wing of the "
            "stairway - telepon the talking drum, internét the road "
            "without end. The Signature Language Method climbs it too: "
            "the stairway of honor reaches wherever the signal reaches."
        ),
        "drill": {"sentences": 20},
        "must_contain": ["telepon", "sinyal", "Kirim", "20"],
    },
    {
        "key": "tenses",
        "name": "Sundanese Verb Tenses in Sentences",
        "group": "Grammar in Action",
        "ladder_rank": 21,
        "ladder_tier": "advanced",
        "description": (
            "Sundanese verbs never change for time; time words do the "
            "work. Five gears, five translated sentences each - 25 "
            "sentences total.\n" +
            "\n".join(
                "GEAR: %s\n%s" % (g, _num_lines(ss))
                for g, ss in TENSE_SETS
            )
        ),
        "how_it_works": (
            "Think in gears, not tenses: geus looks backward (completed), "
            "keur holds the present (ongoing), rek/bade lean forward "
            "(about to), sok repeats (habitual), moal refuses the future "
            "(will not). The verb never moves - only the gear word "
            "changes. Convert one sentence through all five gears: Abdi "
            "geus dahar / keur dahar / rek dahar / sok dahar / moal dahar."
        ),
        "key_points": [
            "Five time gears: geus, keur, rek/bade, sok, moal.",
            "The verb form never changes; only the marker changes.",
            "25 sentences: five per gear, fully translated.",
            "Bade is the polite twin of rek.",
        ],
        "requirements": [
            "Run ten verbs through all five gears.",
            "Narrate yesterday, today, and tomorrow in three paragraphs.",
        ],
        "standards": [
            "Time markers follow standard Sundanese usage.",
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: time is the stairway seen from above - "
            "geus the steps behind, keur the step underfoot, rek the "
            "steps ahead. The Signature Language Method climbs all three "
            "at once: the honorable climber remembers, stands, and "
            "advances."
        ),
        "drill": {"gears": [g for g, _ in TENSE_SETS],
                  "per_gear": 5},
        "must_contain": ["geus", "keur", "moal", "sok"],
    },
    {
        "key": "qa",
        "name": "Sundanese Questions and Answers",
        "group": "Grammar in Action",
        "ladder_rank": 22,
        "ladder_tier": "advanced",
        "description": (
            "20 question-and-answer pairs covering who, what, where, "
            "when, why, and how - every question in Sundanese with its "
            "answer, both translated.\n" +
            _num_lines([("%s -> %s" % (q, a), "%s -> %s" % (qe, ae))
                        for q, a, qe, ae in QA20])
        ),
        "how_it_works": (
            "Questions open with the interrogative (saha, naon, dimana, "
            "iraha, naha, kumaha, sabaraha) and rise in intonation - no "
            "particle needed. Answers mirror the question's words: "
            "Dimana imah anjeun? -> Imah abdi di lembur. Drill as "
            "pairs with a partner: one asks, one answers, then swap. "
            "Speed matters more than perfection here."
        ),
        "key_points": [
            "20 Q&A pairs across who/what/where/when/why/how.",
            "Interrogative-first order with rising intonation.",
            "Answers mirror the question's vocabulary.",
            "Both question and answer fully translated.",
        ],
        "requirements": [
            "Ask and answer all 20 pairs with a partner.",
            "Invent five new pairs using the same interrogatives.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: questions are the lanterns on the "
            "stairway - saha who climbs, naha why, kumaha how. The "
            "Signature Language Method lights every step: the honorable "
            "climber asks before assuming."
        ),
        "drill": {"pairs": 20},
        "must_contain": ["Saha", "Kumaha", "Sabaraha", "20"],
    },
    {
        "key": "commands",
        "name": "Sundanese Commands and Requests",
        "group": "Grammar in Action",
        "ladder_rank": 23,
        "ladder_tier": "advanced",
        "description": (
            "20 imperative and polite-request sentences - informal "
            "commands beside their polite twins. The bare verb commands "
            "(Diuk!); politeness adds mangga, punten, and the lemes "
            "verb (Mangga calik.).\n" +
            _num_lines([("%s [%s]" % (s, r), e) for s, e, r in COMMANDS20])
        ),
        "how_it_works": (
            "The informal imperative is the bare verb: Diuk! Dahar! The "
            "polite request wraps it: mangga + lemes verb (Mangga calik, "
            "Mangga tuang), or punten + verb (Punten, ulah ribut). "
            "Prohibitions use ulah (do not) and tong (don't, coarse). "
            "Never command an elder with a bare verb - climb the "
            "register, not just the sentence."
        ),
        "key_points": [
            "20 commands and requests, informal vs polite, fully translated.",
            "Bare verb = informal command; mangga/punten + lemes verb = polite.",
            "Prohibition: ulah (do not).",
            "Register climbs with the sentence: calik, tuang, lebet.",
        ],
        "requirements": [
            "Give five orders informally, then rephrase each politely.",
            "Forbid three actions with ulah.",
        ],
        "standards": [
            "Command forms follow documented undak usuk basa usage.",
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: commands are the hand on the stairway "
            "rail - the bare verb grips hard, mangga guides gently. The "
            "Signature Language Method teaches the gentle grip first: "
            "honor climbs, it never shoves."
        ),
        "drill": {"commands": 20, "registers": ["informal", "polite"]},
        "must_contain": ["Mangga", "Ulah", "calik", "20"],
    },
    {
        "key": "descriptions",
        "name": "Sundanese Descriptions of People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "description": (
            "20 sentences describing people, places, and things in "
            "detail - the portrait record. Stack adjectives after the "
            "noun and add pisan, teuing, or clauses for color.\n" +
            _num_lines(DESCRIBE20)
        ),
        "how_it_works": (
            "Describe outward-in: size, color, character (jangkung tur "
            "pinter). Places get atmosphere: rame, asri, endah. Chain "
            "with tur (and) and commas; intensify with pisan. The -na "
            "suffix points: tangkalna (the tree in question). Write a "
            "ten-sentence portrait of someone you know - then of your "
            "village."
        ),
        "key_points": [
            "20 descriptive sentences, fully translated.",
            "Portrait order: size, color, character.",
            "Chaining with tur; intensifiers pisan, teuing.",
            "Place atmosphere: rame, asri, endah.",
        ],
        "requirements": [
            "Write a ten-sentence portrait of a person.",
            "Write a ten-sentence portrait of a place.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: description is the carving on the "
            "stairway - each adjective a chisel stroke revealing the "
            "stone's figure. The Signature Language Method carves "
            "slowly: one true detail outranks ten vague ones."
        ),
        "drill": {"sentences": 20},
        "must_contain": ["geulis", "Tangkuban Parahu", "pisan", "20"],
    },
    {
        "key": "story1",
        "name": "Sundanese Story I: The Little Rice Farmer",
        "group": "Stories and Idioms",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "description": (
            "A 10-sentence simple story in Sundanese - present and simple "
            "time - with line-by-line English translation. Read it "
            "aloud; then retell it without looking.\n" +
            _num_lines(STORY1)
        ),
        "how_it_works": (
            "Stories fuse every earlier record: nouns, verbs, time "
            "words, -na, greetings. Read line by line, covering the "
            "English; uncover to check. Then retell the story in your "
            "own Sundanese - changed details are fine, the arc must "
            "hold. This story uses simple present time: hudang, ibak, "
            "dahar, indit, melak, balik."
        ),
        "key_points": [
            "10-sentence story with line-by-line English translation.",
            "Simple present-time narration.",
            "Fuses nouns, verbs, time words, -na, and family terms.",
            "Retell practice: same arc, your own words.",
        ],
        "requirements": [
            "Read the story aloud twice without stumbling.",
            "Retell it from memory in Sundanese.",
        ],
        "standards": [
            "The story is an original teaching construction of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: the first story is the first full "
            "climb - ten steps in one breath, from hudang to balik. The "
            "Signature Language Method celebrates it: the climber who "
            "retells the tale owns the stairway."
        ),
        "drill": {"lines": 10},
        "must_contain": ["Ujang", "sawah", "paré", "10"],
    },
    {
        "key": "story2",
        "name": "Sundanese Story II: The Runaway Goat",
        "group": "Stories and Idioms",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "description": (
            "A 10-sentence story in past time - geus, kamari, and "
            "completed action - with line-by-line English translation.\n" +
            _num_lines(STORY2)
        ),
        "how_it_works": (
            "Past narration leans on geus (already) and time anchors "
            "(kamari, isuk-isuk): Kamari embe leungit. Sequence with "
            "tuluy (then) and sanggeus (after). Feel the arc: loss "
            "(leungit), search (neangan), finding (kapanggih), joy "
            "(bungah). Retell it starting from the finding and working "
            "backward - the grammar must still hold."
        ),
        "key_points": [
            "10-sentence past-time story with line-by-line translation.",
            "Past markers: geus, kamari, and completed verbs.",
            "Sequencers: tuluy (then), sanggeus (after).",
            "Emotional arc: loss, search, finding, joy.",
        ],
        "requirements": [
            "Retell the story forward, then backward.",
            "Rewrite three lines with different past markers.",
        ],
        "standards": [
            "The story is an original teaching construction of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: the second story looks down the "
            "stairway - geus the steps already climbed, each one kept. "
            "The Signature Language Method teaches memory as honor: "
            "what is climbed is not forgotten."
        ),
        "drill": {"lines": 10},
        "must_contain": ["embe", "leungit", "walungan", "10"],
    },
    {
        "key": "story3",
        "name": "Sundanese Story III: The Journey to Bandung",
        "group": "Stories and Idioms",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "description": (
            "A 10-sentence story in future time - rek, bade, isukan, "
            "and moal - with line-by-line English translation.\n" +
            _num_lines(STORY3)
        ),
        "how_it_works": (
            "Future narration plans with rek/bade and isukan: Isukan "
            "Ujang rek indit. Promises use moal hilap (will never "
            "forget). Itineraries chain departures and arrivals: angkat "
            "jam tujuh, sumping, balik sonten. Plan your own real "
            "tomorrow in ten Sundanese sentences - the story becomes "
            "your day."
        ),
        "key_points": [
            "10-sentence future-time story with line-by-line translation.",
            "Future markers: rek, bade, isukan.",
            "Promise form: moal hilap.",
            "Itinerary chaining: angkat, sumping, balik.",
        ],
        "requirements": [
            "Plan your real tomorrow in ten Sundanese sentences.",
            "Make three promises with moal.",
        ],
        "standards": [
            "The story is an original teaching construction of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: the third story looks up the stairway - "
            "rek the steps not yet climbed, each one promised. The "
            "Signature Language Method teaches the climber to vow: moal "
            "hilap, the honorable never forgets the climb."
        ),
        "drill": {"lines": 10},
        "must_contain": ["Bandung", "isukan", "moal hilap", "10"],
    },
    {
        "key": "idioms",
        "name": "Sundanese Idioms and Proverbs",
        "group": "Stories and Idioms",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "description": (
            "20 Sundanese paribasa (proverbs) and babasan (idioms) - "
            "each with literal translation, real meaning, and an "
            "example sentence. These are documented sayings, not "
            "inventions.\n" +
            "\n".join(
                "%d. %s\n   Literal and meaning: %s\n   Example: %s" % (i, s, m, e)
                for i, (s, m, e) in enumerate(IDIOMS20, 1)
            )
        ),
        "how_it_works": (
            "Proverbs are compressed culture: learn the image first "
            "(dripping water, the bean's trellis), then the meaning, "
            "then drop one into conversation at the right moment - a "
            "single paribasa can end a debate. Babasan (gedé hulu, "
            "panjang leungeun, kurung batok) color everyday speech. Use "
            "one per day; never force two into one sentence."
        ),
        "key_points": [
            "20 documented paribasa and babasan with literal translation, meaning, and example.",
            "Paribasa: proverbs (compressed wisdom). Babasan: idioms (colorful expressions).",
            "Images: water, stone, beans, drums, shells, animals.",
            "One per day in real conversation.",
        ],
        "requirements": [
            "Explain five proverbs in your own words.",
            "Use three idioms correctly in conversation.",
        ],
        "standards": [
            "Proverb and idiom forms verified against documented Sundanese usage.",
        ],
        "citations": [CIT_PAR, CIT_ADL],
        "sig_lens": (
            "The Signature read: proverbs are the inscriptions carved "
            "into the stairway landings - cikaracak ninggang batu, the "
            "drip that hollows stone, is the Method itself. The "
            "Signature Language Method carves one inscription per day: "
            "slow water, deep hollow."
        ),
        "drill": {"idioms": 20},
        "must_contain": ["paribasa", "babasan", "Cikaracak", "Silih asah"],
    },
    {
        "key": "registers",
        "name": "Sundanese Formal and Polite Registers",
        "group": "Conversation and Registers",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "description": (
            "15 formal-vs-informal word pairs (loma vs lemes) for "
            "letters, business, and elders - each pair with English and "
            "a usage line. Climb the register: the word changes, the "
            "meaning stays.\n" +
            _num_lines([
                ("%s -> %s" % (l, h),
                 "%s. %s." % (e, u))
                for l, h, e, u in [
                    ("kuring", "abdi", "I",
                     "Kuring indit becomes Abdi angkat to an elder"),
                    ("maneh", "anjeun", "you",
                     "Maneh timana becomes Anjeun timana politely"),
                    ("anjeun", "salira", "you",
                     "Anjeun becomes Salira to the highly respected"),
                    ("indit", "angkat", "go",
                     "Abdi indit becomes Abdi angkat"),
                    ("dahar", "tuang", "eat",
                     "Abdi dahar becomes Abdi tuang"),
                    ("dahar", "neda", "eat (honorific)",
                     "Mangga neda for the honored guest"),
                    ("sare", "kulem", "sleep",
                     "Manehna sare becomes Anjeunna kulem"),
                    ("diuk", "calik", "sit",
                     "Diuk becomes Mangga calik"),
                    ("hayang", "hoyong", "want",
                     "Abdi hayang becomes Abdi hoyong"),
                    ("datang", "sumping", "come",
                     "Manehna datang becomes Anjeunna sumping"),
                    ("nanya", "tumaros", "ask",
                     "Abdi nanya becomes Abdi tumaros"),
                    ("imah", "bumi", "house",
                     "Imah abdi becomes Bumi abdi"),
                    ("peuting", "wengi", "night",
                     "Peuting becomes Wengi to elders"),
                    ("isuk", "enjing", "morning",
                     "Isuk becomes Enjing to elders"),
                    ("budak", "murangkalih", "child",
                     "Budak becomes Murangkalih politely"),
                ]
            ])
        ),
        "how_it_works": (
            "Registers swap vocabulary, not grammar: the sentence frame "
            "stays, the words climb. Master the direction: loma words "
            "for self among peers, lemes words upward to elders and "
            "outward to strangers; honorific words (neda, sumping) "
            "describe the respected other, humble words (abdi, tuang) "
            "describe yourself. Rewrite five loma sentences fully into "
            "lemes."
        ),
        "key_points": [
            "15 loma-to-lemes pairs with usage lines.",
            "Humble words for self (abdi, tuang); honorific words for others (neda, sumping).",
            "Grammar never changes - only vocabulary climbs.",
            "Wrong register to an elder is the costliest error.",
        ],
        "requirements": [
            "Rewrite five loma sentences fully into lemes.",
            "Hold a two-minute polite conversation without slipping.",
        ],
        "standards": [
            "Register pairs follow documented undak usuk basa usage.",
        ],
        "citations": [CIT_ADL, CIT_EJA],
        "sig_lens": (
            "The Signature read: registers are the stairway itself - "
            "loma the lower steps, lemes the upper, and every pair a "
            "single step climbed. The Signature Language Method drills "
            "the climb until it is reflex: respect first, words follow."
        ),
        "drill": {"pairs": 15},
        "must_contain": ["lemes", "loma", "murangkalih", "tumaros"],
    },
    {
        "key": "complex",
        "name": "Sundanese Compound and Complex Sentences",
        "group": "Conversation and Registers",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "description": (
            "15 long sentences with clauses, connectors, and relative "
            "clauses - parsed and translated. The connectors: sabab "
            "(because), sanajan/najan (although), anu (who/which), lamun/"
            "mun (if), bari (while), sanggeus (after), samemeh (before), "
            "sangkan (so that).\n" +
            "\n".join(
                "%d. %s\n   %s" % (i, s, p)
                for i, (s, p) in enumerate(COMPLEX15, 1)
            )
        ),
        "how_it_works": (
            "Complex sentences chain simple ones with connectors: take "
            "two known sentences and join them with sabab, lamun, or "
            "bari. Relative clauses hang on anu: buku anu dibaca ku "
            "Ujang. Purpose closes with sangkan. Build each of the 15 "
            "from its two halves first, then say it whole - the halves "
            "are already in your earlier records."
        ),
        "key_points": [
            "15 complex sentences, parsed and translated.",
            "Connectors: sabab, sanajan, najan, anu, lamun, mun, bari, sanggeus, samemeh, sangkan.",
            "Relative clauses with anu.",
            "Build from halves, then say whole.",
        ],
        "requirements": [
            "Join ten sentence pairs with connectors.",
            "Write five relative clauses with anu.",
        ],
        "standards": [
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: complex sentences are the long flights "
            "of the stairway - sabab the landing where reasons rest, "
            "anu the turn where clauses join. The Signature Language "
            "Method climbs them in halves: no flight is too long when "
            "each step is known."
        ),
        "drill": {"sentences": 15,
                  "connectors": ["sabab", "sanajan", "najan", "anu",
                                 "lamun", "mun", "bari", "sanggeus",
                                 "samemeh", "sangkan"]},
        "must_contain": ["sabab", "sangkan", "anu", "15"],
    },
    {
        "key": "convmarket",
        "name": "Sundanese Conversation: At the Market",
        "group": "Conversation and Registers",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual market dialogue (Sundanese + English), "
            "annotated - greeting, browsing, bargaining, paying, "
            "parting. A = buyer, B = seller.\n" +
            "\n".join(
                "%s: %s\n   %s" % (sp, s, e)
                for sp, s, e in CONV_MARKET
            )
        ),
        "how_it_works": (
            "Dialogues are performed, not read: take a role and speak "
            "it. The market arc runs greeting (wilujeng enjing), request "
            "(aya cau?), bargaining (mirah teuing / henteu tiasa), "
            "payment (ieu artosna), thanks (hatur nuhun), farewell "
            "(wilujeng angkat). Swap roles and run it again faster. "
            "Then improvise the same arc with different goods."
        ),
        "key_points": [
            "20-line bilingual dialogue, annotated.",
            "Market arc: greet, request, bargain, pay, thank, part.",
            "Bargaining moves: mirah teuing, bisa kurang, henteu tiasa.",
            "Perform both roles; then improvise new goods.",
        ],
        "requirements": [
            "Perform the dialogue twice, both roles.",
            "Improvise a market dialogue for different goods.",
        ],
        "standards": [
            "The dialogue is an original teaching construction of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: the market dialogue is the stairway's "
            "busiest landing performed aloud - every bargain an honorable "
            "exchange. The Signature Language Method stages it: speak "
            "both climbers, buyer and seller, until the landing feels "
            "like home."
        ),
        "drill": {"lines": 20, "speakers": ["A", "B"]},
        "must_contain": ["market", "rebu", "Mirah", "20"],
    },
    {
        "key": "convfriend",
        "name": "Sundanese Conversation: Meeting a Friend",
        "group": "Conversation and Registers",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual reunion dialogue (Sundanese + English), "
            "annotated - greeting, catching up, invitation, plan, "
            "farewell. A and B are old friends.\n" +
            "\n".join(
                "%s: %s\n   %s" % (sp, s, e)
                for sp, s, e in CONV_FRIEND
            )
        ),
        "how_it_works": (
            "Friendship dialogues open with the ritual pair "
            "sampurasun/rampes, then trade news with kumaha and atos. "
            "Invitations are specific: isukan sore, jam tujuh, bawa "
            "bekal. Promises close it: moal telat, dugi ka tepang "
            "isukan. Perform it, swap roles, then hold the same "
            "conversation about your own real plans."
        ),
        "key_points": [
            "20-line bilingual dialogue, annotated.",
            "Reunion arc: ritual greeting, news, invitation, plan, farewell.",
            "Specific invitations: time, place, what to bring.",
            "Perform, swap, then personalize.",
        ],
        "requirements": [
            "Perform the dialogue twice, both roles.",
            "Make a real plan with a friend in Sundanese.",
        ],
        "standards": [
            "The dialogue is an original teaching construction of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: the reunion dialogue is two climbers "
            "meeting on the stairway - sampurasun the embrace, the plan "
            "the promise to climb together. The Signature Language "
            "Method rejoices in it: honor shared is honor doubled."
        ),
        "drill": {"lines": 20, "speakers": ["A", "B"]},
        "must_contain": ["Sampurasun", "Rampes", "ngopi", "20"],
    },
    {
        "key": "convproblem",
        "name": "Sundanese Conversation: Solving a Problem",
        "group": "Conversation and Registers",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual problem-solving dialogue (Sundanese + "
            "English), annotated - the lights go out, and two neighbors "
            "solve it step by step. A and B are neighbors.\n" +
            "\n".join(
                "%s: %s\n   %s" % (sp, s, e)
                for sp, s, e in CONV_PROBLEM
            )
        ),
        "how_it_works": (
            "Problem dialogues run the fix arc: alarm (aduh!), "
            "assessment (kumaha atuh?), resources (aya lilin?), action "
            "(mangkok? mangga candak), authority (telepon PLN), "
            "resolution (hurung deui), thanks (hatur nuhun). Notice the "
            "calm register: ulah panik, teu sawios. Perform it, then "
            "improvise a new problem - a flat tire, a lost key - on the "
            "same arc."
        ),
        "key_points": [
            "20-line bilingual dialogue, annotated.",
            "Fix arc: alarm, assessment, resources, action, authority, resolution, thanks.",
            "Calm register: ulah panik, teu sawios.",
            "Improvise new problems on the same arc.",
        ],
        "requirements": [
            "Perform the dialogue twice, both roles.",
            "Improvise a new problem dialogue on the same arc.",
        ],
        "standards": [
            "The dialogue is an original teaching construction of this database.",
        ],
        "citations": [CIT_ADL],
        "sig_lens": (
            "The Signature read: the blackout dialogue is the stairway "
            "in the dark - ulah panik the lantern, gotong royong the "
            "shared hand. The Signature Language Method teaches the "
            "dark too: honor holds steady when the lights go out."
        ),
        "drill": {"lines": 20, "speakers": ["A", "B"]},
        "must_contain": ["pareum", "lilin", "Hatur nuhun", "20"],
    },
    {
        "key": "mastery",
        "name": "Sundanese Mastery Review and Full Reference",
        "group": "Mastery Reference",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary: the alphabet "
            "and script, 200 core words, the ten grammar rules, and all "
            "phrase tables - foundations through conversation. Use it as "
            "the daily drill sheet and the final exam.\n"
            "ALPHABET: the Latin alphabet a-z (26 letters) plus the "
            "Aksara Sunda 18 ngalagena (ka ga nga ca ja nya ta da na pa "
            "ba ma ya ra la wa sa ha) and 7 independent vowels (a é i o "
            "u e eu).\n"
            "200 CORE WORDS: 25 nouns (jalma, budak, lalaki, awewe, "
            "imah, panto, jandela, meja, korsi, cai, sangu, lauk, buah, "
            "tangkal, kembang, panonpoe, bulan, bentang, langit, taneuh, "
            "jalan, pasar, kota, lembur, nagara), 25 verbs (dahar, "
            "nginum, sare, hudang, leumpang, lumpat, diuk, nangtung, "
            "nyarita, nanya, maca, nulis, meuli, ngajual, nyieun, ibak, "
            "seuri, ceurik, indit, datang, balik, gawe, diajar, ulin, "
            "nempo), 25 adjectives (alus, goreng, gede, leutik, panjang, "
            "pondok, jangkung, handap, anyar, kolot, ngora, geulis, "
            "pinter, beunghar, miskin, panas, tiis, amis, pait, asin, "
            "lada, beurat, hampang, gancang, kuat), 15 adverbs (pisan, "
            "leuwih, geus, acan, keur, rek, tangtu, meureun, saban, "
            "ayeuna, kamari, isukan, lalaunan, oge, bae), 30 greetings "
            "(sampurasun through mugia salamet dugi ka tujuan), 20 "
            "numbers and ordinals (hiji through sajuta, kahiji, kadua), "
            "20 proverbs and idioms (caina herang through cileuncang "
            "mande sagara), 16 pronouns and demonstratives (abdi through "
            "eta), 24 particles and connectors (deui through ka).\n"
            "TEN GRAMMAR RULES: SVO order; no gender/case/conjugation; "
            "plural by reduplication and -ar-; negation "
            "henteu/teu/moal/ulah; questions by interrogative + "
            "intonation; passive di-; active nasal N-; time words "
            "geus/keur/rek; possessive -na; adjectives after nouns.\n"
            "PHRASE TABLES: 30 greetings, 20 themed sentence sets "
            "(home, food, travel, work, health, emotions, nature, "
            "shopping, friendship, technology), 25 tense sentences, 20 "
            "Q&A pairs, 20 commands, 20 descriptions, 3 ten-line "
            "stories, 20 idioms, 15 register pairs, 15 complex "
            "sentences, 3 twenty-line conversations.\n"
            "Final drill: " +
            _num_lines([
                ("Sebutkeun 7 vokal basa Sunda.", "Name the 7 Sundanese vowels."),
                ("Sebutkeun 18 konsonan.", "Name the 18 consonants."),
                ("Kumaha carana nanyakeun harga?", "How do you ask the price?"),
                ("Naon bedana dahar jeung tuang?", "What is the difference between dahar and tuang?"),
                ("Jelaskeun 5 gear waktu.", "Explain the 5 time gears."),
            ])
        ),
        "how_it_works": (
            "The mastery record is the exam and the cheat sheet in one. "
            "Work it backward: start from the conversations and prove "
            "you can still climb down to the alphabet. The 200 core "
            "words are drawn verbatim from the records that taught "
            "them - count them, say them, write them. Pass mark: name "
            "all 200, explain all ten rules, perform one dialogue, "
            "retell one story."
        ),
        "key_points": [
            "Full-database summary: alphabet, 200 core words, 10 grammar rules, all phrase tables.",
            "200 core words drawn verbatim from their teaching records.",
            "Daily drill sheet and final exam in one.",
            "Pass mark: 200 words, 10 rules, 1 dialogue, 1 story.",
        ],
        "requirements": [
            "Recite all 200 core words grouped by record.",
            "Explain the ten grammar rules without notes.",
            "Perform one dialogue and retell one story.",
        ],
        "standards": [
            "Core-word lists are verbatim from their teaching records.",
            "Practice sentences are original teaching constructions of this database.",
        ],
        "citations": [CIT_ADL, CIT_EJA, CIT_ISO, CIT_UNI],
        "sig_lens": (
            "The Signature read: the mastery record is the view from "
            "the top of the stairway - 200 stones counted, 10 "
            "commandments kept, every landing visited. The Signature "
            "Language Method ends where it began: level first, word "
            "second, sentence last - now the climber's own."
        ),
        "drill": {
            "core_words": (
                [n for n, _ in NOUNS25] + [v for v, _ in VERBS25] +
                [a for a, _ in ADJ25] + [a for a, _ in ADV15] +
                [g for g, _ in GREET30] +
                ["hiji", "dua", "tilu", "opat", "lima", "genep", "tujuh",
                 "dalapan", "salapan", "sapuluh", "sabelas", "dua belas",
                 "dua puluh", "tilu puluh", "lima puluh", "saratus",
                 "sarebu", "sajuta", "kahiji", "kadua"] +
                ["herang", "cikaracak", "tong", "taleus", "jati", "igel",
                 "curuk", "silih", "ngakal", "elmu", "lanjaran", "taraju",
                 "madu", "payung", "iga", "batok", "hulu", "leungeun",
                 "buntut", "sagara"] +
                [p for p, _ in PRONOUNS] + PARTICLES24
            ),
            "grammar_rules": 10, "stories": 3, "conversations": 3,
            "phrase_tables": 9,
        },
        "must_contain": ["200", "Aksara Sunda", "TEN GRAMMAR RULES", "PHRASE TABLES"],
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
assert [e["ladder_rank"] for e in ENTRIES] == list(range(1, 35)), "ladder ranks broken"
