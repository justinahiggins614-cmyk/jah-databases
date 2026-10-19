"""Content: generator items batch B (sg-wave2-build). Property of Justin Addam Higgins (JAH)."""

ITEMS = {}

ITEMS["gen-personal-motto"] = {
  "record_kind": "motto", "record_kind_plural": "mottos",
  "ai_short": "Personal Motto",
  "tag_pub": "The Personal Motto generator — words to live by, composed fresh from value, action, and resolve.",
  "tag_sig": "The Signature treatment: an expanded motto generator with creed-level banks.",
  "about": "A generator database: the page carries a real working personal-motto generator, and the archive holds 34 full sample mottos.",
  "search_ph": "Search 34 sample mottos…", "chat_ph": "Ask for a custom motto…",
  "gen_blurb": "Composes personal mottos — a value, an action, and the resolve to carry it, in one line.",
  "blueprint": {
    "kind": "motto", "kind_plural": "mottos",
    "blurb": "A personal motto: the line you live by, composed from a value and an action.",
    "how": ("The generator draws a core value, a daily action, and a closing resolve from three banks, then composes "
            "the motto with the seeded PRNG."),
    "labels": {"v": "Core value", "a": "Daily action", "e": "Resolve"},
    "pools": {
      "v": [
        "Kindness", "Courage", "Curiosity", "Patience", "Joy",
        "Honesty", "Grit", "Wonder", "Loyalty", "Calm",
      ],
      "a": [
        "show up", "begin anyway", "ask better questions", "rest without guilt",
        "laugh loudly", "help first", "learn one thing", "keep going",
      ],
      "e": [
        "every single day.", "especially on hard days.", "and mean it.",
        "one step at a time.", "with a full heart.", "no exceptions.",
      ],
    },
    "steps": [
      {"do": "pick", "bank": "v", "var": "v"},
      {"do": "pick", "bank": "a", "var": "a"},
      {"do": "pick", "bank": "e", "var": "e"},
    ],
    "artifact": "{v}: {a} {e}",
  },
  "sig_extra_pools": {
    "v": ["Audacity", "Grace", "Mischief (kind)", "Resolve", "Radiance", "Steadfastness"],
    "a": ["dance through it", "build the thing", "write it down", "say yes"],
    "e": ["and sign your name to it.", "like you mean forever.", "out loud."],
  },
}

ITEMS["gen-signature-catchphrase"] = {
  "record_kind": "catchphrase", "record_kind_plural": "catchphrases",
  "ai_short": "Signature Catchphrase",
  "tag_pub": "The Signature Catchphrase generator — your say-it-everywhere line, composed fresh.",
  "tag_sig": "The Signature treatment: an expanded catchphrase generator with legend-tier banks.",
  "about": "A generator database: the page carries a real working catchphrase generator, and the archive holds 34 full sample catchphrases.",
  "search_ph": "Search 34 sample catchphrases…", "chat_ph": "Ask for a custom catchphrase…",
  "gen_blurb": "Composes signature catchphrases — an opener with a punch that sticks in the memory.",
  "blueprint": {
    "kind": "catchphrase", "kind_plural": "catchphrases",
    "blurb": "A signature catchphrase: the line people quote back to you.",
    "how": ("The generator pairs a memorable opener with a sticky punchline from two banks using the seeded PRNG."),
    "labels": {"op": "Opener", "pu": "Punchline"},
    "pools": {
      "op": [
        "Watch this", "Plot twist", "Hold my lemonade",
        "New rule", "Breaking news", "Fun fact",
        "Life hack", "Pro tip", "Hot take", "Real talk",
      ],
      "pu": [
        "legends nap first.", "snacks solve most problems.",
        "the group chat was right.", "kindness is the flex.",
        "every day is episode one.", "confidence is a costume — wear it.",
        "the playlist never lies.", "rest is a strategy.",
        "weird is a superpower.", "joy is the assignment.",
      ],
    },
    "steps": [
      {"do": "pick", "bank": "op", "var": "op"},
      {"do": "pick", "bank": "pu", "var": "pu"},
    ],
    "artifact": "{op}: {pu}",
  },
  "sig_extra_pools": {
    "op": ["Signature move", "Ancient wisdom", "Director's note", "Captain's log", "Field report", "Official decree"],
    "pu": [
      "greatness loves company.", "the sequel is always better.",
      "bring snacks, change lives.", "history remembers the kind.",
    ],
  },
}

ITEMS["gen-main-character-energy"] = {
  "record_kind": "main-character profile", "record_kind_plural": "main-character profiles",
  "ai_short": "Main Character Energy",
  "tag_pub": "Main Character Energy — generates your starring-role profile: title, scene, and soundtrack.",
  "tag_sig": "The Signature treatment: an expanded main-character generator with blockbuster banks.",
  "about": "A generator database: the page carries a real working main-character-energy generator, and the archive holds 34 full sample profiles.",
  "search_ph": "Search 34 sample profiles…", "chat_ph": "Ask for a custom profile…",
  "gen_blurb": "Generates main-character profiles — your movie title, your signature scene, your soundtrack cue.",
  "blueprint": {
    "kind": "main-character profile", "kind_plural": "main-character profiles",
    "blurb": "Your starring-role snapshot: the movie title of your life right now.",
    "how": ("The generator draws a movie title, a signature scene, and a soundtrack cue from three banks with the "
            "seeded PRNG."),
    "labels": {"title": "Movie title", "scene": "Signature scene", "song": "Soundtrack cue"},
    "pools": {
      "title": [
        "The Late Bloomer", "Ctrl+Alt+Defy", "Main Street Miracle",
        "The Comeback Tour", "Neon Horizons", "The Plot Thickens",
        "Second Act Energy", "The Wild Card", "Golden Hour",
        "The Underdog Uprising", "Paper Planes", "Static & Stardust",
        "The Slow Climb",
        "Electric Daydream",
        "The Kind Rebellion",
        "Chasing Daylight",
        "The Standing Start",
        "Velvet Revolution",
        "The Lucky Break",
        "Analog Heart",
        "The Great Pivot",
        "Sunrise Industry",
        "The Bold Hello",
        "Miracle on Main Street",
        "The Encore Kid",
        "Static Bloom",
        "The Grand Gesture",
        "Paper Moon Rising",
        "The Joyride",
        "Halftime Hero",
        "The Plot Armor",
        "Golden Reel",
        "The Silver Lining Tour",
        "Day One Energy",
        "The Comeback Trail",
        "Neon Roots",
      ],
      "scene": [
        "walking away from an explosion in slow motion (of confetti)",
        "a montage of small wins set to your favorite song",
        "the training sequence, but for parallel parking",
        "a dramatic airport run — for a flight you are early for",
        "the makeover scene, but it is just a great haircut",
        "rallying the group chat for a spontaneous adventure",
      ],
      "song": [
        "an 80s power ballad", "a lo-fi victory lap", "orchestral swells",
        "a pop anthem at full volume", "acoustic guitar sunrise",
        "synthwave at midnight",
      ],
    },
    "steps": [
      {"do": "pick", "bank": "title", "var": "title"},
      {"do": "pick", "bank": "scene", "var": "scene"},
      {"do": "pick", "bank": "song", "var": "song"},
    ],
    "artifact": "{title}",
  },
  "sig_extra_pools": {
    "title": [
      "The Signature Cut", "Director's Cut: You", "Opening Weekend",
      "The Standing Ovation", "Encore Energy", "The Legend Builds",
    ],
    "scene": [
      "the one-take hallway walk with the perfect song",
      "the rooftop speech that changes everything",
    ],
    "song": ["a choir-backed finale", "your own theme song (hummed)"],
  },
}

ITEMS["gen-personal-theme-song"] = {
  "record_kind": "theme song", "record_kind_plural": "theme songs",
  "ai_short": "Personal Theme Song",
  "tag_pub": "The Personal Theme Song generator — your song title, genre, tempo, and mood, composed fresh.",
  "tag_sig": "The Signature treatment: an expanded theme-song generator with anthem-level banks.",
  "about": "A generator database: the page carries a real working theme-song generator, and the archive holds 34 full sample songs.",
  "search_ph": "Search 34 sample songs…", "chat_ph": "Ask for a custom theme song…",
  "gen_blurb": "Composes personal theme songs — title, genre, tempo, and mood in one anthem snapshot.",
  "blueprint": {
    "kind": "theme song", "kind_plural": "theme songs",
    "blurb": "Your personal theme song: the track that plays when you enter the room.",
    "how": ("The generator draws a song title, genre, tempo, and mood from four banks with the seeded PRNG."),
    "labels": {"t": "Song title", "g": "Genre", "te": "Tempo", "m": "Mood"},
    "pools": {
      "t": [
        "Running Toward Sunrise", "The Confetti Protocol", "Louder Than Mondays",
        "Golden Static", "The Long Way Home", "Neon Umbrella",
        "Halfway to Legendary", "The Snack Run Anthem", "Paper Crown",
        "Thunder in Sneakers", "The Comeback Kid", "Velvet Horizon",
        "The Morning After Midnight",
        "Chasing the Chorus",
        "Static & Honey",
        "The Long Encore",
        "Velvet Static Bloom",
        "Halfway to Stardom",
        "The Golden Mixtape",
        "Thunder & Tonic",
        "Paper Airplanes",
        "The Neon Confessional",
        "Sunrise Over Static",
        "The Happy Accident",
        "Gilded Youth",
        "The Anthem We Deserve",
        "Midnight in Technicolor",
        "The Joy Bomb",
        "Copper & Chrome",
        "The Wildflower Waltz",
        "Electric Picnic",
        "The Grand Refrain",
        "Honeyed Thunder",
        "The Lucky Chord",
        "Velvet Sunrise",
        "Encore for One",
      ],
      "g": [
        "indie pop", "synthwave", "acoustic folk", "funk",
        "orchestral pop", "lo-fi hip-hop", "disco revival", "alt rock",
      ],
      "te": [
        "128 BPM, full sprint", "96 BPM, confident stride",
        "72 BPM, slow burn", "140 BPM, pure adrenaline",
      ],
      "m": [
        "triumphant", "cozy", "electric", "dreamy", "defiant", "joyful",
      ],
    },
    "steps": [
      {"do": "pick", "bank": "t", "var": "t"},
      {"do": "pick", "bank": "g", "var": "g"},
      {"do": "pick", "bank": "te", "var": "te"},
      {"do": "pick", "bank": "m", "var": "m"},
    ],
    "artifact": "{t}",
  },
  "sig_extra_pools": {
    "t": [
      "The Signature Overture", "Encore at Midnight", "The Roaring Ovation",
      "Main Character March", "The Legend Mix", "Anthem for the Bold",
    ],
    "g": ["stadium rock", "cinematic soul"],
    "te": ["110 BPM, main-character walk"],
    "m": ["legendary", "unstoppable"],
  },
}

ITEMS["gen-personal-brand-playground"] = {
  "record_kind": "brand concept", "record_kind_plural": "brand concepts",
  "ai_short": "Personal Brand Playground",
  "tag_pub": "The Personal Brand Playground — generates brand names, taglines, and audiences to play with.",
  "tag_sig": "The Signature treatment: an expanded brand generator with empire-level banks.",
  "about": "A generator database: the page carries a real working personal-brand generator, and the archive holds 34 full sample brands.",
  "search_ph": "Search 34 sample brands…", "chat_ph": "Ask for a custom brand…",
  "gen_blurb": "Generates personal brand concepts — name, tagline, and audience in one playful snapshot.",
  "blueprint": {
    "kind": "brand concept", "kind_plural": "brand concepts",
    "blurb": "A personal brand concept: the name, the line, and who it is for.",
    "how": ("The generator draws a brand name, a tagline, and a target audience from three banks with the seeded "
            "PRNG."),
    "labels": {"b": "Brand name", "tag": "Tagline", "aud": "Audience"},
    "pools": {
      "b": [
        "The Cozy Hustle", "Golden Hour Goods", "The Kind Rebel",
        "Slow Bloom Studio", "The Joy Audit", "Main Street Magic",
        "The Snack Scholar", "Bright Side Bureau", "The Calm Collective",
        "Wonder & Wren", "The Everyday Epic", "Sunbeam Supply",
        "The Daring Daydream",
        "Kindling & Co.",
        "The Brave Ordinary",
        "Golden State of Mind",
        "The Joyful Hustle",
        "Wren & Willow",
        "The Sunny Side",
        "Foxglove Studio",
        "The Good Mischief",
        "Maple & Main",
        "The Bright Ordinary",
        "Copperfield Creative",
        "The Happy Medium",
        "Juniper & Jade",
        "The Cozy Ambitious",
        "Wildflower Works",
        "The Gentle Giant",
        "Sunbeam & Sons",
        "The Kindred Spirit",
        "Marigold & Moon",
        "The Brave Little Brand",
        "Honey & Oak",
        "The Joy Merchant",
        "Lumen & Lark",
      ],
      "tag": [
        "small joys, done well", "kindness as a strategy",
        "make it cozy, make it count", "boldly gentle",
        "joy is the product", "slow down, shine bright",
        "ordinary days, epic standards", "bring the sunshine",
      ],
      "aud": [
        "tired creatives", "joyful minimalists", "weekend adventurers",
        "cozy homebodies", "ambitious kind hearts", "nostalgia collectors",
      ],
    },
    "steps": [
      {"do": "pick", "bank": "b", "var": "b"},
      {"do": "pick", "bank": "tag", "var": "tag"},
      {"do": "pick", "bank": "aud", "var": "aud"},
    ],
    "artifact": "{b}",
  },
  "sig_extra_pools": {
    "b": [
      "The Signature Standard", "Legend & Lore Co.", "The Bold Gentle",
      "Evergreen Empire", "The Radiant Route", "Kindred & Co.",
    ],
    "tag": ["signed, sealed, legendary", "the gold standard of kind"],
    "aud": ["future legends", "kind rebels everywhere"],
  },
}

ITEMS["gen-nickname-genius"] = {
  "record_kind": "nickname", "record_kind_plural": "nicknames",
  "ai_short": "Nickname Genius",
  "tag_pub": "The Nickname Genius — generates nicknames from real first names and playful patterns.",
  "tag_sig": "The Signature treatment: an expanded nickname generator with legend-tier banks.",
  "about": "A generator database: the page carries a real working nickname generator, and the archive holds 34 full sample nicknames.",
  "search_ph": "Search 34 sample nicknames…", "chat_ph": "Ask for a custom nickname…",
  "gen_blurb": "Generates nicknames — a real first name run through playful nickname patterns.",
  "blueprint": {
    "kind": "nickname", "kind_plural": "nicknames",
    "blurb": "A nickname with the base name and pattern that built it.",
    "how": ("The generator draws a first name and a nickname pattern, then applies the pattern to the name with the "
            "seeded PRNG. Patterns use {b} for the base name."),
    "labels": {"b": "Base name", "pat": "Pattern"},
    "pools": {
      "b": [
        "Alex", "Sam", "Jordan", "Casey", "Riley",
        "Taylor", "Morgan", "Avery", "Quinn", "Hayden",
        "Charlie", "Finley", "Emerson", "Rowan", "Skyler",
      ],
      "pat": [
        "{b}y", "{b}ster", "Lil {b}", "{b} the Great",
        "Captain {b}", "{b}-inator", "Big {b}", "{b} 2.0",
        "Sir {b}", "{b}cakes",
      ],
    },
    "steps": [
      {"do": "pick", "bank": "b", "var": "b"},
      {"do": "pick", "bank": "pat", "var": "pat"},
    ],
    "artifact": "{pat}",
    "nested": True,
  },
  "sig_extra_pools": {
    "b": ["Jules", "Remy", "Noa", "Ellis", "Marlow", "Indigo"],
    "pat": ["The Legendary {b}", "{b} Supreme", "Doctor {b}", "{b} of Legend"],
  },
}

ITEMS["gen-username-universe"] = {
  "record_kind": "username", "record_kind_plural": "usernames",
  "ai_short": "Username Universe",
  "tag_pub": "The Username Universe — generates clean, available-style usernames from word alchemy.",
  "tag_sig": "The Signature treatment: an expanded username generator with rare-word banks.",
  "about": "A generator database: the page carries a real working username generator, and the archive holds 34 full sample usernames.",
  "search_ph": "Search 34 sample usernames…", "chat_ph": "Ask for a custom username…",
  "gen_blurb": "Generates usernames — style word plus core word plus number tag, always clean and readable.",
  "blueprint": {
    "kind": "username", "kind_plural": "usernames",
    "blurb": "A generated username: memorable, clean, and ready to claim.",
    "how": ("The generator draws a style word and a core word, capitalizes both, and appends a two-digit tag using "
            "the seeded PRNG. Every combination is checked against the content gate."),
    "labels": {"a": "Style word", "n": "Core word", "num": "Number tag"},
    "pools": {
      "a": [
        "cosmic", "velvet", "thunder", "pixel", "golden",
        "midnight", "neon", "ember", "frosty", "solar",
        "quiet", "rapid", "clever", "brave", "jolly",
        "mystic", "turbo", "cosy", "vivid", "witty",
      ],
      "n": [
        "fox", "panda", "comet", "waffle", "tiger",
        "otter", "falcon", "muffin", "dragon", "koala",
        "ninja", "wizard", "pirate", "astronaut", "badger",
        "squirrel", "llama", "penguin", "raccoon", "taco",
      ],
    },
    "steps": [
      {"do": "pick", "bank": "a", "var": "a", "cap": True},
      {"do": "pick", "bank": "n", "var": "n", "cap": True},
      {"do": "int", "var": "num", "min": 10, "max": 99},
    ],
    "artifact": "{a}{n}{num}",
  },
  "sig_extra_pools": {
    "a": ["legendary", "radiant", "stealthy", "jovial", "prime", "ultra", "mega", "hyper"],
    "n": ["phoenix", "kraken", "yeti", "griffin", "sphinx", "wombat", "axolotl", "quokka"],
  },
}

ITEMS["gen-personal-flag-creator"] = {
  "record_kind": "flag", "record_kind_plural": "flags",
  "ai_short": "Personal Flag Creator",
  "tag_pub": "The Personal Flag Creator — designs personal flags: colors, emblem, and layout.",
  "tag_sig": "The Signature treatment: an expanded flag creator with heraldic banks.",
  "about": "A generator database: the page carries a real working personal-flag generator, and the archive holds 34 full sample flags.",
  "search_ph": "Search 34 sample flags…", "chat_ph": "Ask for a custom flag…",
  "gen_blurb": "Designs personal flags — colors, emblem, and layout composed into a flag worth flying.",
  "blueprint": {
    "kind": "flag", "kind_plural": "flags",
    "blurb": "A personal flag design: colors, emblem, and layout, ready to sketch or sew.",
    "how": ("The generator draws two colors, an emblem, and a layout from four banks with the seeded PRNG, then "
            "names the flag."),
    "labels": {"c1": "Primary color", "c2": "Secondary color", "em": "Emblem", "lay": "Layout"},
    "pools": {
      "c1": [
        "crimson", "navy", "forest green", "goldenrod", "teal",
        "plum", "burnt orange", "slate blue",
      ],
      "c2": [
        "cream", "charcoal", "sky blue", "rose", "sand",
        "mint", "lavender", "copper",
      ],
      "em": [
        "a rising sun", "a fox", "an oak tree", "a compass star",
        "a wave", "a mountain peak", "a key", "a lantern",
      ],
      "lay": [
        "horizontal bicolor", "vertical tricolor", "diagonal split",
        "centered emblem on solid", "canton with stripes", "chevron field",
      ],
    },
    "steps": [
      {"do": "pick", "bank": "c1", "var": "c1", "cap": True},
      {"do": "pick", "bank": "c2", "var": "c2"},
      {"do": "pick", "bank": "em", "var": "em"},
      {"do": "pick", "bank": "lay", "var": "lay"},
    ],
    "artifact": "{c1} {em} {lay}",
  },
  "sig_extra_pools": {
    "c1": ["imperial purple", "midnight black", "ember red", "glacier white"],
    "c2": ["antique gold", "silver", "ivory", "bronze"],
    "em": ["a phoenix", "a lighthouse", "a dragon", "a laurel crown"],
    "lay": ["quarterly heraldic", "nordic cross", "saltire field"],
  },
}
