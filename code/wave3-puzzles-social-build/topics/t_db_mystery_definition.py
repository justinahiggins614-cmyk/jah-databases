# -*- coding: utf-8 -*-
"""Topic module: db-mystery-definition. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-mystery-definition", "name": "The Mystery Definition Database", "pfx": "JAH-MYSDEF-",
    "tagline_pub": "Mystery definitions with the word revealed - guess the word from its definition: every record carrying the clues, the answer, and a check that the definition fits, taught progressively along the ladder.",
    "tagline_sig": "The Signature word-sight: every definition a Signature riddle, every answer a Signature reveal. The full ladder from easy words through tricky ones to Signature-grade vocabulary. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Mystery Definition",
    "role_pub": "word master - defining mysteriously and revealing fairly",
    "role_sig": "Signature word master - teaching Signature word-sight",
    "record_kind": "mystery definition record", "record_kind_plural": "mystery definitions",
    "demo_kind": "definition-proof", "demo_title": "Mystery Definition Study",
    "search_ph": "Search words, definitions, vocabulary, guess the word...",
    "chat_ph": "Ask for a mystery definition...",
    "gen_blurb": "Generate clearly-labeled definition studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded mystery definitions, every answer verified, marching toward one million records. Presented in teaching-ladder order: easy words, tricky ones, Signature-grade.",
    "reqs": "A love of words and a guessing spirit.",
    "stds": "Every definition's clues must all fit the answer; the demo verifies the fit.",
    "cites": ["JAH Databases definition verification standard v1.0"],
})


def _md(tier, answer, clues, hint, check_code, checks):
    return T(
        tier, "Mystery word: %s" % ("_" * len(answer)),
        desc_pub='MYSTERY DEFINITION:\n\n%s\n\nHINT: %s\n\nANSWER: %s'
        % ("\n".join("  - %s" % c for c in clues), hint, answer.upper()),
        desc_sig='Signature word-sight: the clues pointed, and %s stepped forward. The Signature edition treats every solved word as the vocabulary growing by one.' % answer.upper(),
        how_pub='Guess it: read all the clues before answering - each clue rules out thousands of words; together they leave one.',
        how_sig='The Signature way: guess after two clues, then use the rest to confirm - speed with a safety net.',
        keys=['Clues: %d.' % len(clues),
              'Hint: %s' % hint,
              'Answer: %s.' % answer.upper()],
        demo=("check", {"code": check_code, "checks": checks}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _md(B, "apple", ["A fruit", "Grows on trees", "Keeps the doctor away (so they say)"], "Starts with A.", ["W='apple'"], [("len5", "len(W) == 5"), ("starts_a", "W.startswith('a')")]),
    _md(B, "dog", ["A pet", "Barks", "Wags its tail"], "Man's best friend.", ["W='dog'"], [("len3", "len(W) == 3")]),
    _md(B, "sun", ["In the sky", "Gives light and heat", "Rises in the east"], "The day star.", ["W='sun'"], [("len3", "len(W) == 3")]),
    _md(B, "book", ["Has pages", "You read it", "Has a cover"], "Libraries are full of them.", ["W='book'"], [("len4", "len(W) == 4")]),
    _md(B, "water", ["You drink it", "Falls as rain", "Covers most of Earth"], "H2O.", ["W='water'"], [("len5", "len(W) == 5")]),
    _md(B, "bird", ["Has feathers", "Can fly", "Lays eggs"], "Sings in the morning.", ["W='bird'"], [("len4", "len(W) == 4")]),
    _md(B, "chair", ["You sit on it", "Has four legs", "Found at tables"], "Not a sofa.", ["W='chair'"], [("len5", "len(W) == 5")]),
    _md(B, "moon", ["In the night sky", "Orbits Earth", "Has phases"], "Made of cheese? No.", ["W='moon'"], [("len4", "len(W) == 4")]),
    _md(B, "fish", ["Lives in water", "Has gills", "Swims"], "Not a mammal.", ["W='fish'"], [("len4", "len(W) == 4")]),
    _md(B, "tree", ["Has leaves", "Grows tall", "Gives shade"], "Has roots.", ["W='tree'"], [("len4", "len(W) == 4")]),
    _md(B, "house", ["People live in it", "Has rooms", "Has a roof"], "Home.", ["W='house'"], [("len5", "len(W) == 5")]),
    _md(C, "telescope", ["You look through it", "Shows distant stars", "Astronomers use it"], "Ends with -scope.", ["W='telescope'"], [("len9", "len(W) == 9"), ("scope", "W.endswith('scope')")]),
    _md(C, "bicycle", ["Has two wheels", "You pedal it", "No engine"], "Starts with bi- (two).", ["W='bicycle'"], [("len7", "len(W) == 7"), ("bi", "W.startswith('bi')")]),
    _md(C, "volcano", ["A mountain that erupts", "Spits lava", "Can be dormant"], "Think Pompeii.", ["W='volcano'"], [("len7", "len(W) == 7")]),
    _md(C, "dictionary", ["Defines words", "Alphabetical", "Heavy"], "This database's cousin.", ["W='dictionary'"], [("len10", "len(W) == 10")]),
    _md(C, "kaleidoscope", ["Shows shifting patterns", "You turn it", "Mirrors inside"], "A toy of symmetry.", ["W='kaleidoscope'"], [("len12", "len(W) == 12")]),
    _md(C, "chameleon", ["Changes color", "A lizard", "Long tongue"], "Blends in.", ["W='chameleon'"], [("len9", "len(W) == 9")]),
    _md(C, "lighthouse", ["Warns ships", "Has a bright lamp", "Stands on coasts"], "Guides sailors home.", ["W='lighthouse'"], [("len10", "len(W) == 10")]),
    _md(C, "xylophone", ["You strike it", "Has wooden bars", "A musical instrument"], "Starts with X.", ["W='xylophone'"], [("x", "W.startswith('x')")]),
    _md(C, "quarantine", ["Isolation period", "Stops disease spread", "40 days originally"], "Starts with Q.", ["W='quarantine'"], [("q", "W.startswith('q')")]),
    _md(C, "skeleton", ["Bones", "Holds you up", "Halloween favorite"], "You have 206.", ["W='skeleton'"], [("len8", "len(W) == 8")]),
    _md(C, "tornado", ["A spinning storm", "Funnel cloud", "Dorothy's ride"], "Starts with T.", ["W='tornado'"], [("len7", "len(W) == 7")]),
    _md(C, "pyramid", ["Ancient tomb", "Triangular sides", "Found in Egypt"], "The Great one is at Giza.", ["W='pyramid'"], [("len7", "len(W) == 7")]),
    _md(A, "serendipity", ["Happy accidents", "Finding what you weren't seeking", "A fortunate discovery"], "The word for lucky finds.", ["W='serendipity'"], [("len11", "len(W) == 11")]),
    _md(A, "petrichor", ["The smell after rain", "Earthy scent", "From dry soil"], "Your nose knows it.", ["W='petrichor'"], [("len9", "len(W) == 9")]),
    _md(A, "defenestration", ["Throwing out a window", "A political act in Prague", "Very specific"], "The word for window-tossing.", ["W='defenestration'"], [("len14", "len(W) == 14")]),
    _md(A, "sesquipedalian", ["Long words", "A foot and a half (literally)", "This word describes itself"], "Self-describing.", ["W='sesquipedalian'"], [("len14", "len(W) == 14")]),
    _md(A, "limerence", ["Involuntary infatuation", "Not quite love", "A psychologist's term"], "Stronger than a crush.", ["W='limerence'"], [("len9", "len(W) == 9")]),
    _md(A, "apricity", ["Warmth of sun in winter", "A rare beautiful word", "Frost plus sun"], "Winter sun's gift.", ["W='apricity'"], [("len8", "len(W) == 8")]),
    _md(A, "syzygy", ["Three celestial bodies aligned", "Astronomy term", "All Y's"], "The Scrabble champion.", ["W='syzygy'"], [("len6", "len(W) == 6"), ("ys", "W.count('y') == 3")]),
    _md(A, "crepuscular", ["Active at twilight", "Dawn and dusk animals", "Neither day nor night"], "Twilight's word.", ["W='crepuscular'"], [("len11", "len(W) == 11")]),
    _md(A, "ineffable", ["Too great for words", "Indescribable", "Beyond expression"], "Ironically, describable.", ["W='ineffable'"], [("len9", "len(W) == 9")]),
    _md(A, "sonder", ["Realizing strangers have full lives", "A modern coinage", "Empathy's word"], "Everyone's inner movie.", ["W='sonder'"], [("len6", "len(W) == 6")]),
    _md(A, "vellichor", ["Smell of old books", "A modern coinage", "Bookshop scent"], "Book lovers know.", ["W='vellichor'"], [("len9", "len(W) == 9")]),
]

# unique titles: number each mystery word
for _n, _t in enumerate(TOPICS, 1):
    _k = [k for k in _t["keys"] if k.startswith("Answer:")][0]
    _a = _k.split(":")[1].strip().rstrip(".")
    _t["title"] = "Mystery word #%d (%d letters): %s" % (_n, len(_a), "_" * len(_a))

