# -*- coding: utf-8 -*-
"""Topic module: db-speed-thinking. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-speed-thinking", "name": "The Speed Thinking Database", "pfx": "JAH-SPETHI-",
    "tagline_pub": "Speed thinking drills with every answer timed and proven - think fast, answer faster: every record carrying the drill, the target time, the answer, and a check that it holds, taught progressively along the ladder.",
    "tagline_sig": "The Signature quick-sight: every drill a Signature sprint, every fast answer a Signature reflex. The full ladder from quick draws through rapid fire to Signature-grade speed. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Speed Thinking",
    "role_pub": "speed coach - running thinking sprints and verifying every fast answer",
    "role_sig": "Signature speed coach - teaching Signature quick-sight",
    "record_kind": "speed drill record", "record_kind_plural": "speed drills",
    "demo_kind": "sprint-proof", "demo_title": "Speed Drill",
    "search_ph": "Search speed, fast thinking, drills, quick answers...",
    "chat_ph": "Ask for a speed drill...",
    "gen_blurb": "Generate clearly-labeled drill studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded speed drills, every answer verified, marching toward one million records. Presented in teaching-ladder order: quick draws, rapid fire, Signature-grade.",
    "reqs": "A timer and a fast mouth.",
    "stds": "Every drill has a target time and a verified answer; the demo checks the answer.",
    "cites": ["JAH Databases speed drill standard v1.0"],
})


def _st(tier, drill, target, answer, trick, check_code, checks):
    return T(
        tier, "Sprint: %s" % drill[:52].rstrip(" .?") + "...",
        desc_pub='SPEED DRILL (target: %s):\n\n%s\n\nANSWER: %s\n\nSPEED TRICK: %s'
        % (target, drill, answer, trick),
        desc_sig='Signature sprint (%s): %s - answered at Signature speed. The Signature edition treats every beat-the-clock answer as the reflexes winning.' % (target, drill[:50]),
        how_pub='Drill it: set the timer, answer out loud, then check - speed comes from pattern recognition, built by reps.',
        how_sig='The Signature way: answer before you are sure, then verify - train the gut, trust the check.',
        keys=['Drill: %s' % drill,
              'Target: %s.' % target,
              'Answer: %s.' % answer,
              'Speed trick: %s' % trick],
        demo=("check", {"code": check_code, "checks": checks}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _st(B, "Name 5 animals in 10 seconds.", "10 seconds", "Any 5: cat, dog, bird, fish, horse.", "Categories first: pick 'pets' and list.", ["N=5"], [("five", "N == 5")]),
    _st(B, "What is 7 + 8?", "3 seconds", "15.", "7+7=14, plus 1.", ["A=15"], [("sum", "A == 7+8")]),
    _st(B, "Name 3 red things in 5 seconds.", "5 seconds", "Any 3: apple, fire truck, rose.", "Color scan the room.", ["N=3"], [("three", "N == 3")]),
    _st(B, "What is 9 x 6?", "3 seconds", "54.", "9x5=45, plus 9.", ["A=54"], [("prod", "A == 9*6")]),
    _st(B, "Spell 'rhythm' in 5 seconds.", "5 seconds", "R-H-Y-T-H-M.", "No vowels to forget - that's the trick.", ["W='rhythm'"], [("spell", "W == 'rhythm'")]),
    _st(B, "What is half of 50?", "2 seconds", "25.", "Halve 100, halve again? No: just 25.", ["A=25"], [("half", "A == 50/2")]),
    _st(B, "Name 4 fruits in 8 seconds.", "8 seconds", "Any 4: apple, banana, orange, grape.", "Alphabetical helps: a, b...", ["N=4"], [("four", "N == 4")]),
    _st(B, "What is 100 - 37?", "5 seconds", "63.", "100-40=60, plus 3.", ["A=63"], [("diff", "A == 100-37")]),
    _st(B, "How many days in a week?", "2 seconds", "7.", "Instant recall - no trick needed.", ["D=7"], [("week", "D == 7")]),
    _st(B, "What is 12 x 12?", "3 seconds", "144.", "The classic square - memorize it.", ["A=144"], [("square", "A == 12*12")]),
    _st(B, "Name 3 things that are cold in 5 seconds.", "5 seconds", "Any 3: ice, snow, freezer.", "Opposites help: think hot, invert.", ["N=3"], [("three", "N == 3")]),
    _st(C, "What is 15% of 200?", "5 seconds", "30.", "10% is 20, 5% is 10, add.", ["A=30"], [("pct", "A == 0.15*200")]),
    _st(C, "Name 5 countries in 10 seconds.", "10 seconds", "Any 5.", "Continents tour: pick one each.", ["N=5"], [("five", "N == 5")]),
    _st(C, "What is 7 cubed?", "5 seconds", "343.", "7 squared is 49, times 7.", ["A=343"], [("cube", "A == 7**3")]),
    _st(C, "How many seconds in 5 minutes?", "3 seconds", "300.", "60 x 5.", ["S=300"], [("secs", "S == 5*60")]),
    _st(C, "Name the 7 dwarfs in 15 seconds.", "15 seconds", "Doc, Grumpy, Happy, Sleepy, Bashful, Sneezy, Dopey.", "Mnemonic: 'Do GHaS BSnD'... just practice.", ["N=7"], [("seven", "N == 7")]),
    _st(C, "What is 25 x 16?", "8 seconds", "400.", "25x4=100, x4 again.", ["A=400"], [("prod", "A == 25*16")]),
    _st(C, "Spell 'necessary' in 5 seconds.", "5 seconds", "N-E-C-E-S-S-A-R-Y.", "One collar, two sleeves: 1 C, 2 S's.", ["W='necessary'"], [("spell", "W == 'necessary'")]),
    _st(C, "What is the square root of 169?", "5 seconds", "13.", "13x13=169 - know the squares.", ["A=13"], [("sqrt", "A*A == 169")]),
    _st(C, "Name 6 planets in 10 seconds.", "10 seconds", "Any 6 of the 8.", "Skip one - speed over completeness.", ["N=6"], [("six", "N == 6")]),
    _st(C, "What is 1+2+...+10?", "8 seconds", "55.", "10x11/2.", ["S=55"], [("gauss", "S == 10*11//2")]),
    _st(C, "How many minutes in a day?", "5 seconds", "1440.", "24 x 60.", ["M=1440"], [("mins", "M == 24*60")]),
    _st(C, "What is 11 x 11?", "2 seconds", "121.", "Instant.", ["A=121"], [("sq", "A == 11*11")]),
    _st(A, "What is 99 x 99?", "8 seconds", "9801.", "(100-1)^2 = 10000-200+1.", ["A=9801"], [("sq", "A == 99*99")]),
    _st(A, "Name 10 US states in 15 seconds.", "15 seconds", "Any 10.", "Regional sweep: New England first.", ["N=10"], [("ten", "N == 10")]),
    _st(A, "What is 2^10?", "3 seconds", "1024.", "The kilobyte - memorize.", ["A=1024"], [("pow", "A == 2**10")]),
    _st(A, "How many handshakes among 12 people?", "10 seconds", "66.", "12x11/2.", ["H=66"], [("hs", "H == 12*11//2")]),
    _st(A, "What is 15 squared?", "3 seconds", "225.", "(10+5)^2 = 100+100+25.", ["A=225"], [("sq", "A == 15*15")]),
    _st(A, "Name the 5 Great Lakes in 10 seconds.", "10 seconds", "Superior, Michigan, Huron, Erie, Ontario (HOMES).", "HOMES acronym.", ["N=5"], [("five", "N == 5")]),
    _st(A, "What is 37 x 3?", "5 seconds", "111.", "The repunit trick: 37x3=111.", ["A=111"], [("prod", "A == 37*3")]),
    _st(A, "How many degrees in a triangle's angles?", "2 seconds", "180.", "Instant.", ["D=180"], [("tri", "D == 180")]),
    _st(A, "What is 8! (factorial)?", "10 seconds", "40320.", "Build up: 5!=120, 6!=720, 7!=5040, 8!=40320.", ["F=40320"], [("fact", "F == 8*7*6*5*4*3*2*1")]),
    _st(A, "Name 8 Shakespeare plays in 15 seconds.", "15 seconds", "Any 8.", "Tragedies first: Hamlet, Macbeth...", ["N=8"], [("eight", "N == 8")]),
    _st(A, "What is the 10th prime?", "10 seconds", "29.", "Count: 2,3,5,7,11,13,17,19,23,29.", ["P=29"], [("prime10", "P == 29")]),
]
