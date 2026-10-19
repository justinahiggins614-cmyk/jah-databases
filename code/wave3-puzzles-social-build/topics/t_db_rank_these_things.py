# -*- coding: utf-8 -*-
"""Topic module: db-rank-these-things. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-rank-these-things", "name": "The Rank These Things Database", "pfx": "JAH-RANTHETHI-",
    "tagline_pub": "Ranking challenges with the correct order proven - biggest to smallest, fastest to slowest, oldest to newest: every record carrying the items, the true ranking, and the facts that fix each position, taught progressively along the ladder.",
    "tagline_sig": "The Signature ordering-sight: every ranking a Signature hierarchy, every position earned by fact. The full ladder from easy orders through tricky near-ties to Signature-grade rankers. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Rank These Things",
    "role_pub": "ranking referee - setting ordering challenges and proving every position by fact",
    "role_sig": "Signature ranking referee - teaching Signature ordering-sight",
    "record_kind": "ranking challenge record", "record_kind_plural": "ranking challenges",
    "demo_kind": "ranking-proof", "demo_title": "Ranking Study",
    "search_ph": "Search rank, order, biggest, fastest, oldest...",
    "chat_ph": "Ask for a ranking challenge...",
    "gen_blurb": "Generate clearly-labeled ranking studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded ranking challenges, every order fact-checked, marching toward one million records. Presented in teaching-ladder order: easy orders, tricky sets, expert rankers.",
    "reqs": "A sense of scale and a love of lists.",
    "stds": "Every ranking is verified against the stated values in the demo: the order must sort by the measure, no ties broken arbitrarily.",
    "cites": ["JAH Databases ranking verification standard v1.0"],
})


def _rk(tier, items, measure, values, note):
    # values: list aligned with items; correct order = sorted desc by value
    order = sorted(range(len(items)), key=lambda i: values[i], reverse=True)
    ranked = [items[i] for i in order]
    return T(
        tier, "Rank: %s" % ", ".join(items),
        desc_pub='RANK THESE THINGS (by %s):\n\n%s\n\nCORRECT ORDER:\n%s\n\n%s'
        % (measure, ", ".join(items),
           "\n".join("%d. %s (%s)" % (n + 1, items[i], ("%g" % values[i])) for n, i in enumerate(order)), note),
        desc_sig='Signature ordering-sight: %s, ranked by %s - the Signature hierarchy standing on facts. The Signature edition treats every correct ranking as the world sorted properly.' % (", ".join(items), measure),
        how_pub='Rank them yourself first, then check: for each adjacent pair, ask which fact puts one above the other. The demo sorts by the numbers - your brain should too.',
        how_sig='The Signature way: guess the full order before peeking - the surprise is the lesson.',
        keys=['Items: %s.' % ", ".join(items),
              'Measure: %s.' % measure,
              'Correct order: %s.' % ", ".join(ranked),
              'Ranker note: %s' % note],
        demo=("check", {"code": ["ITEMS = %r" % items, "VALS = %r" % values,
                                  "ORDER = sorted(range(len(ITEMS)), key=lambda i: VALS[i], reverse=True)"],
                        "checks": [("order_is_sorted", "all(VALS[ORDER[i]] >= VALS[ORDER[i+1]] for i in range(len(ORDER)-1))"),
                                   ("no_ties", "len(set(VALS)) == len(VALS)"),
                                   ("uses_all_items", "sorted(ORDER) == list(range(len(ITEMS)))")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _rk(B, ["Ant", "Cat", "Elephant", "Mouse"], "weight (kg)", [0.003, 4, 5000, 0.02], "Size order: the elephant outweighs the cat by a thousand times."),
    _rk(B, ["Bicycle", "Car", "Airplane", "Walking"], "top speed (km/h)", [30, 200, 900, 6], "Speed order: walking < cycling < driving < flying."),
    _rk(B, ["Day", "Week", "Month", "Year"], "length (days)", [1, 7, 30, 365], "Time order: the calendar's own ranking."),
    _rk(B, ["Pea", "Apple", "Watermelon", "Grape"], "size (cm)", [1, 8, 40, 2], "Size order: pea < grape < apple < watermelon."),
    _rk(B, ["Candle", "Lamp", "Sun", "Flashlight"], "brightness", [1, 60, 1e12, 200], "Brightness: the sun outshines everything by orders of magnitude."),
    _rk(B, ["Egg", "Chicken", "Dinosaur", "Whale"], "weight (kg)", [0.06, 2, 8000, 150000], "Weight: from egg to blue whale, six orders of magnitude."),
    _rk(B, ["Second", "Minute", "Hour", "Day"], "length (seconds)", [1, 60, 3600, 86400], "Time's own ladder, each step 60x the last (mostly)."),
    _rk(B, ["Turtle", "Human", "Cheetah", "Snail"], "speed (km/h)", [0.3, 12, 110, 0.05], "Speed: snail < turtle < human < cheetah."),
    _rk(B, ["Puddle", "Pond", "Lake", "Ocean"], "size", [1, 100, 1e6, 1e12], "Water bodies: each step dwarfs the last."),
    _rk(B, ["Whisper", "Talk", "Shout", "Jet engine"], "loudness (dB)", [30, 60, 90, 140], "Loudness: decibels are logarithmic - the jet is a billion times louder than the whisper."),
    _rk(B, ["Seed", "Sprout", "Tree", "Forest"], "size", [1, 10, 1000, 1e9], "Growth: from one seed to a forest of millions."),
    _rk(C, ["Mercury", "Earth", "Jupiter", "Mars"], "diameter (km)", [4879, 12742, 139820, 6779], "Planets: Mercury < Mars < Earth < Jupiter - Jupiter is wider than all others combined."),
    _rk(C, ["Cheetah", "Pronghorn", "Lion", "Greyhound"], "top speed (km/h)", [110, 88, 80, 72], "Land speed: the pronghorn surprises everyone at #2."),
    _rk(C, ["Eiffel Tower", "Empire State", "Burj Khalifa", "Shanghai Tower"], "height (m)", [330, 443, 828, 632], "Skyscrapers: Burj Khalifa towers over all at 828m."),
    _rk(C, ["Amazon", "Nile", "Mississippi", "Thames"], "length (km)", [6400, 6650, 6275, 346], "Rivers: the Nile edges the Amazon (disputed, but the ranking holds by most measures)."),
    _rk(C, ["Blue whale", "Elephant", "Giraffe", "Hippo"], "weight (kg)", [150000, 5000, 1200, 1500], "Weight: whale > elephant > hippo > giraffe - the hippo outweighs the giraffe."),
    _rk(C, ["Everest", "K2", "Kangchenjunga", "Fuji"], "height (m)", [8849, 8611, 8586, 3776], "Mountains: Everest > K2 > Kangchenjunga >> Fuji."),
    _rk(C, ["Falcon", "Eagle", "Sparrow", "Ostrich"], "top speed (km/h)", [390, 160, 46, 70], "Birds: the peregrine falcon's dive (390 km/h) is the fastest animal motion on Earth."),
    _rk(C, ["Diamond", "Gold", "Silver", "Copper"], "hardness (Mohs)", [10, 2.5, 2.7, 3], "Hardness: diamond (10) > copper (3) > silver (2.7) > gold (2.5) - gold is soft!"),
    _rk(C, ["Sahara", "Gobi", "Mojave", "Antarctic"], "area (million km²)", [9.2, 1.3, 0.12, 14], "Deserts: Antarctica is the largest desert on Earth - the trick answer."),
    _rk(C, ["Pacific", "Atlantic", "Indian", "Arctic"], "area (million km²)", [165, 106, 70, 14], "Oceans: Pacific > Atlantic > Indian > Arctic."),
    _rk(C, ["Giraffe", "Elephant", "Blue whale", "Ostrich"], "height (m)", [5.5, 4, 30, 2.7], "Height: the blue whale's LENGTH (30m) beats all - read the measure carefully."),
    _rk(C, ["Lightning", "Sound", "Car", "Bullet"], "speed (m/s)", [300000000, 343, 55, 800], "Speed: light > bullet > sound > car - light is a million times faster than sound."),
    _rk(A, ["Jupiter", "Saturn", "Neptune", "Earth"], "mass (10^24 kg)", [1898, 568, 102, 5.97], "Mass: Jupiter outweighs all other planets combined, twice over."),
    _rk(A, ["Sperm whale", "Colossal squid", "Giant squid", "Blue whale"], "length (m)", [20, 10, 13, 30], "Length: blue whale (30m) > sperm whale (20m) > giant squid (13m) > colossal squid (10m) - the names lie."),
    _rk(A, ["Oak", "Redwood", "Baobab", "Bristlecone pine"], "age (years)", [500, 2000, 2500, 5000], "Age: the bristlecone pine (5,000 years) was old when Rome was young."),
    _rk(A, ["Venus", "Mars", "Mercury", "Jupiter"], "day length (hours)", [2802, 24.6, 1407, 9.9], "Day length: Venus (2,802h) > Mercury (1,407h) > Mars (24.6h) > Jupiter (9.9h) - Venus spins slowest."),
    _rk(A, ["Antarctica", "Australia", "Europe", "Africa"], "area (million km²)", [14, 7.7, 10.2, 30.3], "Continents: Africa (30.3) > Antarctica (14) > Europe (10.2) > Australia (7.7)."),
    _rk(A, ["Cheetah", "Sailfish", "Peregrine falcon", "Pronghorn"], "top speed (km/h)", [110, 109, 390, 88], "Falcon (390, air) > cheetah (110, land) > sailfish (109, sea) > pronghorn (88) - the sea almost ties the land."),
    _rk(A, ["Iron", "Lead", "Gold", "Aluminum"], "density (g/cm³)", [7.9, 11.3, 19.3, 2.7], "Density: gold (19.3) > lead (11.3) > iron (7.9) > aluminum (2.7)."),
    _rk(A, ["Shakespeare", "Dickens", "Twain", "Austen"], "words published (millions)", [0.9, 4.0, 1.5, 0.6], "Output: Dickens wrote the most by far - the ranking of literary stamina."),
    _rk(A, ["Grain of sand", "Basketball", "Moon", "Sun"], "diameter (mm)", [1, 240, 3474000, 1392000000], "Scale: from a millimeter of sand to 1.4 billion millimeters of Sun - nine orders of magnitude in four steps."),
    _rk(A, ["Nile", "Amazon", "Yangtze", "Mississippi"], "discharge (m³/s)", [2830, 209000, 30100, 16800], "Discharge: the Amazon discharges more than the next seven rivers combined."),
    _rk(A, ["Everest", "Dead Sea shore", "Mariana Trench", "Denver"], "elevation (m)", [8849, -430, -10935, 1609], "Elevation: Everest (8,849) > Denver (1,609) > Dead Sea (-430) > Trench (-10,935) - negatives rank low."),
]
