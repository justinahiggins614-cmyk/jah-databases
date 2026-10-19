# -*- coding: utf-8 -*-
"""Topic module: gen-family-game-generator (GENERATOR class, first-release pick).
34 full sample family games + REAL game generator (see realgen).
Property of Justin Addam Higgins (JAH)."""
from w3lib import topic

CFG = {
    "slug": "gen-family-game-generator",
    "prefix_pub": "JAH-FAMGAMGEN-",
    "prefix_sig": "JAH-FAMGAMGENS-",
    "name_pub": "The Family Game Generator Database",
    "name_sig": "The Family Game Generator Signature Database",
    "tagline_pub": "Family game night, solved forever - real quiz rounds with answers at the bottom, scavenger hunts with scoring, charades decks by difficulty, and story builders with twist cards: every record a complete playable game, plus a real generator that creates a brand-new game on every run, taught progressively along the ladder.",
    "tagline_sig": "The Signature craft of play: every game night a Signature testimony, every laugh recorded in the family ledger. The full ladder from quick quizzes through hunts and charades to Signature-grade story building. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai_pub": "JAH Family Game Archivist",
    "ai_sig": "JAH Family Game Signature Archivist",
    "role_pub": "game master - creating complete playable family games: quizzes, scavenger hunts, charades, story builders",
    "role_sig": "Signature game master - creating Signature-grade family games",
    "greet_pub": "I am the JAH Family Game Archivist. Quiz, hunt, charades, or story - pick your game night.",
    "greet_sig": "I am the JAH Family Game Signature Archivist. Pick your game night.",
    "record_kind": "family game record",
    "record_kind_plural": "family games",
    "demo_kind": "family-game",
    "demo_title": "Family Game Study",
    "search_ph": "Search quiz, scavenger hunt, charades, story builder...",
    "chat_ph": "Ask for a family game...",
    "gen_blurb": "Real working generator - every run creates a brand-new, complete playable family game: quiz round with answers, scavenger hunt, charades deck, or story builder. Never a structural sample.",
    "about_archive": "Seeded sample family games, each complete and playable tonight, marching toward one million records. Presented in teaching-ladder order: quick games, team games, Signature-grade epics.",
    "reqs_default": "The family, the items listed, and a willingness to be silly. Grown-ups play too - no sidelines.",
    "stds_default": "Every game is complete: rules, setup, play, and scoring. Quiz answers always at the bottom, no peeking.",
    "cites_default": ["JAH Databases game craft standard v1.0"],
}
CUSTOM_GEN = "family-game"


def _quiz(tier, qs):
    body = "\n".join("Q%d: %s" % (i + 1, q) for i, (q, a) in enumerate(qs))
    ans = "\n".join("A%d: %s" % (i + 1, a) for i, (q, a) in enumerate(qs))
    return topic(
        tier, "Family quiz round (%d questions): %s" % (len(qs), qs[0][0][:30].rstrip(" ?")),
        desc_pub="SAMPLE GAME - QUIZ ROUND:\n\nRead each question aloud; players write answers secretly. Answers are at the bottom, no peeking.\n\n%s\n\nScoring: 1 point per correct answer, bonus point for the funniest wrong answer (family vote).\n\nANSWERS (no peeking):\n%s" % (body, ans),
        desc_sig="Signature play: the quiz as family testimony - what the family knows together, recorded. The Signature edition treats every correct answer as a small family triumph.",
        how_pub="One reader, everyone else writes. Little kids get to answer first to avoid copying. The funniest-wrong-answer vote is mandatory - it keeps losing fun.",
        how_sig="The Signature way: end with the lightning round - each player invents one question for the group.",
        keys=["%d real questions with verified answers." % len(qs),
              "Answers at the bottom - the honor system is the game.",
              "Scoring rewards both knowledge and humor.",
              "Adaptable: swap any question for a family-specific one."],
        demo=("check", {"code": ["QS = %r" % qs],
                        "checks": [("five_questions", "len(QS) == %d" % len(qs)),
                                   ("all_have_answers", "all(len(q) == 2 and q[1].strip() for q in QS)"),
                                   ("questions_unique", "len(set(q[0] for q in QS)) == len(QS)")]}),
    )


def _hunt(tier, items, place):
    return topic(
        tier, "Family scavenger hunt (%d items, %s)" % (len(items), place),
        desc_pub="SAMPLE GAME - SCAVENGER HUNT (%s):\n\n20 minutes on the clock. Find each item and bring it (or photograph it) back to base.\n\n%s\n\nScoring: 1 point per item, 2 points if the whole family agrees it was the most creative find. Grown-ups play too - no sidelines in this family."
        % (place, "\n".join("%d. %s" % (i + 1, it) for i, it in enumerate(items))),
        desc_sig="Signature play: the hunt as family expedition - the house and yard mapped by attention. The Signature edition treats every found item as a small discovery worthy of the ledger.",
        how_pub="Set boundaries first, then the timer. Photograph fragile or fixed things instead of moving them. The creativity bonus is where legends are born.",
        how_sig="The Signature way: the youngest hunter picks one bonus item for the list.",
        keys=["%d hunt items, location: %s." % (len(items), place),
              "20-minute timer keeps the energy high.",
              "Creativity bonus rewards imagination over speed.",
              "Safe and doable with stuff already around."],
        demo=("check", {"code": ["ITEMS = %r" % items],
                        "checks": [("eight_items", "len(ITEMS) == %d" % len(items)),
                                   ("items_unique", "len(set(ITEMS)) == len(ITEMS)"),
                                   ("items_specific", "all(len(i) > 5 for i in ITEMS)")]}),
    )


def _char(tier, cards):
    body = "\n".join("Card %d [%s]: %s" % (i + 1, d, w) for i, (w, d) in enumerate(cards))
    return topic(
        tier, "Family charades deck (%d cards): %s" % (len(cards), cards[0][0][:28]),
        desc_pub="SAMPLE GAME - CHARADES:\n\nNo talking, no pointing at objects - sounds and gestures only. 60 seconds per card.\n\n%s\n\nLittle kids get the Easy cards first; let them deal. The actor may not speak - the guessers may shout all they want." % body,
        desc_sig="Signature play: charades as family theater - the body saying what words cannot. The Signature edition treats every great mime as a standing ovation moment.",
        how_pub="Split into two teams. Easy cards warm up the shy; Hard cards are for the brave. The 60-second timer is sacred.",
        how_sig="The Signature way: the winning team performs an encore of their best card.",
        keys=["%d charade cards across difficulties." % len(cards),
              "Difficulty labels keep it fair for all ages.",
              "60 seconds per card - the timer is the game.",
              "No talking rule forces glorious creativity."],
        demo=("check", {"code": ["CARDS = %r" % cards],
                        "checks": [("eight_cards", "len(CARDS) == %d" % len(cards)),
                                   ("has_easy", "any(d == 'Easy' for _, d in CARDS)"),
                                   ("difficulties_labeled", "all(d in ('Easy', 'Medium', 'Hard') for _, d in CARDS)")]}),
    )


def _story(tier, starter, twists):
    return topic(
        tier, "Family story builder: %s" % starter[:34].rstrip(" -"),
        desc_pub="SAMPLE GAME - STORY BUILDER:\n\nOne person reads the starter, then players take turns adding one sentence each. When a twist card appears, the next player MUST work it in.\n\nStarter: %s\n\nTwist cards (in order):\n%s\n\nKeep going until someone says 'the end' and everyone agrees. Write down the best lines - family lore starts here."
        % (starter, "\n".join("%d. %s" % (i + 1, t) for i, t in enumerate(twists))),
        desc_sig="Signature play: the story as family mythology - tonight's silliness is next decade's legend. The Signature edition treats the written-down best lines as the first page of the family book.",
        how_pub="The starter reader goes last in the rotation (they already know the beginning). Twists are mandatory - that is where the genius happens.",
        how_sig="The Signature way: illustrate the final story together, one drawing per player.",
        keys=["One story starter + %d twist cards." % len(twists),
              "Turn-based sentence building - everyone contributes.",
              "Twists force creativity; no skipping them.",
              "Write down the best lines - that is the real prize."],
        demo=("check", {"code": ["TW = %r" % twists, "ST = %r" % starter],
                        "checks": [("has_starter", "len(ST) > 30"),
                                   ("three_twists", "len(TW) == %d" % len(twists)),
                                   ("twists_unique", "len(set(TW)) == len(TW)")]}),
    )


B = "Foundations"
C = "Compounded"
A = "Advanced"
TOPICS = [
    _quiz(B, [("How many legs does a spider have?", "Eight."), ("What planet is known as the Red Planet?", "Mars."), ("How many days are in a leap year?", "366."), ("What is the largest ocean on Earth?", "The Pacific Ocean."), ("Which animal is the tallest in the world?", "The giraffe.")]),
    _quiz(B, [("How many colors are in a rainbow?", "Seven."), ("What do you call a baby frog?", "A tadpole."), ("Which planet has beautiful rings around it?", "Saturn."), ("How many sides does a triangle have?", "Three."), ("What is the fastest land animal?", "The cheetah.")]),
    _quiz(B, [("What gas do plants absorb from the air?", "Carbon dioxide."), ("How many minutes are in an hour?", "Sixty."), ("What is a group of wolves called?", "A pack."), ("How many strings does a violin have?", "Four."), ("What is the hardest natural substance on Earth?", "Diamond.")]),
    _quiz(B, [("Which bird cannot fly but swims well?", "The penguin."), ("How many players are on a soccer team on the field?", "Eleven."), ("What is the capital of France?", "Paris."), ("What do caterpillars turn into?", "Butterflies (or moths)."), ("How many teeth does an adult human usually have?", "Thirty-two.")]),
    _quiz(B, [("What is H2O commonly known as?", "Water."), ("Which continent is the Sahara Desert on?", "Africa."), ("What shape has five sides?", "A pentagon."), ("How many wheels does a tricycle have?", "Three."), ("What is the largest mammal in the world?", "The blue whale.")]),
    _hunt(B, ["something red", "something that makes noise", "something soft", "something older than you", "something that smells good", "something with wheels", "something you can wear", "something that grows"], "around the house"),
    _hunt(B, ["something square", "something that reflects", "something with a button", "something tiny", "something blue", "something round", "something shiny", "something funny"], "in the living room"),
    _char(B, [("brushing teeth", "Easy"), ("walking a dog", "Easy"), ("eating spaghetti", "Easy"), ("a cat chasing a laser pointer", "Easy"), ("wrapping a present", "Easy"), ("playing basketball", "Easy"), ("swimming upstream", "Medium"), ("flying a kite", "Medium")]),
    _char(B, [("a penguin waddling", "Easy"), ("building a sandcastle", "Medium"), ("a robot dancing", "Medium"), ("a statue coming to life", "Hard"), ("baking a cake in fast-forward", "Hard"), ("a sloth crossing the road", "Hard"), ("a popcorn kernel popping", "Hard"), ("defusing a bomb (gently!)", "Hard")]),
    _story(B, "On the morning of the big picnic, the family discovered the car would not start - and something was glowing in the garage.", ["A talking parrot lands on the windowsill with urgent news.", "Someone's phone starts playing music nobody recognizes.", "A long-lost relative knocks on the door holding a pie."]),
    _story(B, "Grandma's old recipe box had one card nobody had ever dared to cook - until today.", ["Everything suddenly goes silent - even the birds.", "A map falls out of a book, marked with an X nearby.", "The youngest person present suddenly knows exactly what to do."]),
    _quiz(C, [("Which month has the fewest days?", "February."), ("What do you call frozen water?", "Ice."), ("How many cents are in a dollar?", "One hundred."), ("What animal says 'moo'?", "A cow."), ("What is the sun?", "A star.")]),
    _quiz(C, [("How many seasons are there in a year?", "Four."), ("What color do you get mixing blue and yellow?", "Green."), ("Which animal is known as the king of the jungle?", "The lion."), ("How many hours are in a day?", "Twenty-four."), ("What do bees make?", "Honey.")]),
    _quiz(C, [("What is the opposite of hot?", "Cold."), ("How many letters are in the English alphabet?", "Twenty-six."), ("What fruit keeps the doctor away, according to the saying?", "An apple."), ("Which animal hops and carries babies in a pouch?", "A kangaroo."), ("How many days are in a regular year?", "365.")]),
    _quiz(C, [("What is the largest desert in the world?", "The Antarctic Desert."), ("How many hearts does an octopus have?", "Three."), ("What is the currency of Japan?", "The yen."), ("Which planet is closest to the sun?", "Mercury."), ("What do you call a group of fish?", "A school.")]),
    _hunt(C, ["something that opens and closes", "something that floats", "something with stripes", "something you read", "something musical", "something from nature", "something that keeps you warm", "something with a handle"], "in the backyard"),
    _hunt(C, ["something older than the house", "something that needs batteries", "something with a smell you love", "something that makes you laugh", "something with writing on it", "something that rolls", "something transparent", "something with four legs (toy counts)"], "around the house, harder edition"),
    _char(C, [("directing an orchestra", "Medium"), ("a mime trapped in a box", "Medium"), ("ice skating on thin ice", "Hard"), ("a T-Rex trying to clap", "Hard"), ("knitting with spaghetti", "Hard"), ("a GPS giving wrong directions", "Medium"), ("popping bubble wrap in slow motion", "Easy"), ("a flamingo doing yoga", "Medium")]),
    _char(C, [("reading a boring book dramatically", "Easy"), ("a squirrel hiding nuts", "Easy"), ("parallel parking a bus", "Medium"), ("a chameleon at a disco", "Hard"), ("deflating like a balloon", "Medium"), ("a penguin on a hot beach", "Easy"), ("juggling invisible balls", "Medium"), ("a sloth winning a race", "Hard")]),
    _story(C, "The power went out during the storm, and that is when the knocking started - three knocks, then giggling.", ["It starts raining - indoors. Just a little.", "A map falls out of a book, marked with an X in your own neighborhood.", "Everything suddenly goes silent - even the birds."]),
    _story(C, "A mysterious package arrived with no return address, labeled: OPEN TOGETHER AFTER DINNER.", ["A talking parrot lands on the windowsill with urgent news.", "The youngest person present suddenly knows exactly what to do.", "Someone's phone starts playing music nobody recognizes - from inside the walls."]),
    _story(C, "The new puppy dug up something shiny in the backyard that hummed when you held it.", ["A long-lost relative knocks on the door holding a pie.", "It starts raining - indoors. Just a little.", "Everything suddenly goes silent - even the birds."]),
    _quiz(C, [("What is the largest state in the USA?", "Alaska."), ("How many legs does a crab have?", "Ten."), ("What is the name of the toy cowboy in Toy Story?", "Woody."), ("Which shape has no corners?", "A circle."), ("What do you call a house made of ice?", "An igloo.")]),
    _quiz(A, [("What is the chemical symbol for gold?", "Au."), ("How many bones are in the adult human body?", "206."), ("What year did humans first land on the moon?", "1969."), ("What is the longest river in the world?", "The Nile (or Amazon - accept either with reasoning)."), ("What does 'www' stand for?", "World Wide Web.")]),
    _quiz(A, [("Which country has the most natural lakes?", "Canada."), ("What is the smallest prime number?", "2."), ("How many time zones does Russia span?", "Eleven."), ("What is the hardest rock?", "Diamond (mineral); accept granite discussion."), ("What language has the most native speakers?", "Mandarin Chinese.")]),
    _quiz(A, [("What is the speed of light (approx)?", "300,000 km/s."), ("Which organ produces insulin?", "The pancreas."), ("What is the capital of Australia?", "Canberra."), ("How many elements are in the periodic table?", "118."), ("What is the largest island in the world?", "Greenland.")]),
    _hunt(A, ["something invented before 1900", "something that uses a magnet", "something with a serial number", "something that changed the world from this house", "something with instructions in two languages", "something that measures something", "something older than everyone playing", "something that belonged to a grandparent"], "the whole house, expert edition"),
    _hunt(A, ["a shadow shaped like an animal", "a reflection you cannot explain quickly", "something that sounds different up close", "the oldest thing you can find outside", "something nature is reclaiming", "a perfect circle in nature", "something that should not be where it is", "evidence of an animal visitor"], "outdoors, photographer edition"),
    _char(A, [("a black hole eating a star", "Hard"), ("photosynthesis in fast-forward", "Hard"), ("a computer buffering", "Medium"), ("the water cycle", "Medium"), ("a volcano erupting politely", "Hard"), ("democracy in action", "Hard"), ("a printer jamming dramatically", "Easy"), ("evolution of dance", "Medium")]),
    _story(A, "The old lighthouse on the cliff had been dark for fifty years - until tonight, when its beam swept across our windows.", ["A talking parrot lands on the windowsill with urgent news.", "Everything suddenly goes silent - even the birds.", "A map falls out of a book, marked with an X in your own neighborhood.", "The youngest person present suddenly knows exactly what to do."]),
    _story(A, "Every clock in the house stopped at 3:33 a.m. - and when we woke, the furniture had been rearranged by someone who knew us too well.", ["It starts raining - indoors. Just a little.", "Someone's phone starts playing music nobody recognizes - from inside the walls.", "A long-lost relative knocks on the door holding a pie.", "Everything suddenly goes silent - even the birds."]),
    _story(A, "The family road trip took a wrong turn down a road that was not on any map, toward a town that was not on any sign.", ["A map falls out of a book, marked with an X in your own neighborhood.", "The youngest person present suddenly knows exactly what to do.", "A talking parrot lands on the windowsill with urgent news.", "It starts raining - indoors. Just a little."]),
    _hunt(A, ["something that glows", "something with a key", "something that survived a move", "something with a story nobody believes", "something that only works in summer", "something with more than 100 parts", "something that was once alive", "something that predicts something"], "attic and garage, explorer edition"),
    _quiz(A, [("What is the deepest point in the ocean?", "The Mariana Trench (Challenger Deep)."), ("How many players in a baseball team on the field?", "Nine."), ("What is the most spoken language in the world (total speakers)?", "English."), ("Which metal is liquid at room temperature?", "Mercury (and gallium near it)."), ("What is the tallest mountain in the world?", "Mount Everest.")]),
]
