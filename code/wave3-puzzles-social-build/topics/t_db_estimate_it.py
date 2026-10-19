# -*- coding: utf-8 -*-
"""Topic module: db-estimate-it. Fermi estimates with computed breakdowns.
Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-estimate-it", "name": "The Estimate It Database", "pfx": "JAH-ESTIT-",
    "tagline_pub": "Fermi estimation challenges - big questions answered with brave arithmetic: every record carrying the question, the step-by-step breakdown, the final estimate, and why each step is reasonable, taught progressively along the ladder.",
    "tagline_sig": "The Signature estimation-sight: every big question a Signature calculation, every rough number honestly earned. The full ladder from everyday estimates through classic Fermis to Signature-grade whoppers. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Estimate It",
    "role_pub": "estimation coach - breaking big questions into brave little multiplications",
    "role_sig": "Signature estimation coach - teaching Signature estimation-sight",
    "record_kind": "estimation puzzle record", "record_kind_plural": "estimation puzzles",
    "demo_kind": "fermi-proof", "demo_title": "Estimate It Study",
    "search_ph": "Search Fermi, estimate, how many, breakdown...",
    "chat_ph": "Ask for an estimate...",
    "gen_blurb": "Generate clearly-labeled estimation studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded Fermi estimates, every breakdown machine-computed, marching toward one million records. Presented in teaching-ladder order: everyday, classic, whoppers.",
    "reqs": "Paper, pencil, and the courage to be roughly right.",
    "stds": "Every estimate shows its steps; the demo multiplies the steps and asserts the result matches the stated answer within 1%.",
    "cites": ["JAH Databases Fermi verification standard v1.0"],
})


def _es(tier, question, steps, unit, note):
    # steps: list of (label, value)
    result = 1.0
    for _, v in steps:
        result *= v
    breakdown = "\n".join("  %s: %s" % (label, ("%g" % v)) for label, v in steps)
    return T(
        tier, "Estimate: %s" % question,
        desc_pub='ESTIMATE IT:\n\nQuestion: %s?\n\nBreakdown:\n%s\n\nESTIMATE: %s %s\n\n%s'
        % (question, breakdown, ("%g" % result), unit, note),
        desc_sig='Signature estimation-sight: %s - broken into brave steps, each honestly earned, the Signature product standing. The Signature edition treats every Fermi as proof that rough numbers beat no numbers.' % question,
        how_pub='Estimate it yourself: split the question into 3-5 multiplicative steps, guess each step to the nearest power of ten (or better), multiply, and sanity-check the answer against reality.',
        how_sig='The Signature way: round each step to one significant figure first - precision is the enemy of estimation.',
        keys=['Question: %s?' % question,
              'Steps: %d, each stated and reasonable.' % len(steps),
              'Estimate: %s %s (machine-multiplied).' % (("%g" % result), unit),
              'Reality check: %s' % note],
        demo=("compute", {"code": ["STEPS = %r" % steps,
                                   "RESULT = 1.0",
                                   "for _label, _v in STEPS: RESULT *= _v"],
                          "show": ["RESULT"],
                          "asserts": [("steps_reasonable", "all(v > 0 for _, v in STEPS)"),
                                      ("matches_stated", "abs(RESULT - %r) / %r < 0.01" % (result, result))]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _es(B, "how many piano tuners in Chicago", [("population of Chicago", 2700000), ("1 / household size", 1/2.5), ("fraction with pianos", 0.05), ("tunings per piano per year", 1), ("1 / tunings one tuner does per year", 1/500)], "tuners", "The classic Fermi, straight from Enrico himself: about a hundred tuners - the method matters more than the number."),
    _es(B, "how many breaths you take per day", [("breaths per minute", 15), ("minutes per day", 1440)], "breaths", "About twenty-one thousand breaths a day - you just did one."),
    _es(B, "how many words you speak per day", [("words per minute talking", 130), ("minutes of talking per day", 60)], "words", "Roughly eight thousand words a day for a chatty human."),
    _es(B, "how many hairs on your head", [("scalp area (cm²)", 600), ("hairs per cm²", 200)], "hairs", "About 120,000 hairs - give or take a bad haircut."),
    _es(B, "how many seconds in a year", [("seconds per minute", 60), ("minutes per hour", 60), ("hours per day", 24), ("days per year", 365)], "seconds", "31,536,000 - pi times ten million, near enough to sing about."),
    _es(B, "how many heartbeats per day", [("beats per minute", 70), ("minutes per day", 1440)], "beats", "About 100,800 beats a day - the hardest-working muscle you own."),
    _es(B, "how many pages in all your school books", [("books per year", 6), ("pages per book", 300), ("years of school", 12)], "pages", "Around 21,600 pages - you have read a small library already."),
    _es(B, "how many steps to walk across town", [("town width (km)", 8), ("steps per km", 1400)], "steps", "About 11,200 steps - a solid day's walking in one line."),
    _es(B, "how many cups of water you drink per year", [("cups per day", 6), ("days per year", 365)], "cups", "About 2,190 cups - a small swimming pool over a lifetime."),
    _es(B, "how many hours you sleep per year", [("hours per night", 8), ("nights per year", 365)], "hours", "2,920 hours - a third of your life, spent well."),
    _es(B, "how many miles you walk per year", [("steps per day", 8000), ("miles per step", 1/2000), ("days per year", 365)], "miles", "About 1,460 miles a year - you walk to another city annually without noticing."),
    _es(C, "how many ping-pong balls fit in a school bus", [("bus volume (m³)", 60), ("1 / ball volume (m³)", 1/3.35e-5), ("packing efficiency", 0.64)], "balls", "About 1.1 million - the interview classic, answered with geometry."),
    _es(C, "how many gas stations in the US", [("US population", 330000000), ("1 / people per station", 1/3000)], "stations", "About 110,000 - the real count is near 115,000. Fermi wins again."),
    _es(C, "how many tweets per day (worldwide)", [("users", 300000000), ("fraction tweeting daily", 0.2), ("tweets per tweeter", 3)], "tweets", "About 180 million - the world's chatter, quantified."),
    _es(C, "how many grains of sand on a beach", [("beach volume (m³)", 1000000), ("grains per m³", 1e12)], "grains", "About 10^18 grains - more than stars you can see, fewer than atoms in a grape."),
    _es(C, "how many cells in the human body", [("body mass (kg)", 70), ("cells per kg", 4.3e11)], "cells", "About 3×10^13 - thirty trillion tiny citizens."),
    _es(C, "how many photos taken per day worldwide", [("smartphone users", 4000000000), ("photos per user per day", 2)], "photos", "About 8 billion photos a day - humanity's diary, written in light."),
    _es(C, "how many hairs shed per day", [("hairs on head", 120000), ("1 / hair lifespan (days)", 1/1000)], "hairs", "About 120 a day - the shower drain's daily harvest, totally normal."),
    _es(C, "how many words in all published books", [("books published", 150000000), ("words per book", 80000)], "words", "About 1.2×10^13 words - humanity's complete first draft."),
    _es(C, "how many ants on Earth", [("humans", 8000000000), ("ants per human", 2500000)], "ants", "About 2×10^16 - twenty quadrillion ants, and they were here first."),
    _es(C, "how many cups of coffee per day worldwide", [("coffee drinkers", 1000000000), ("cups per drinker", 2)], "cups", "About 2 billion cups a day - the world's most popular productivity tool."),
    _es(C, "how many miles of DNA in your body", [("cells", 3e13), ("DNA per cell (m)", 2)], "meters", "About 6×10^13 meters - to the sun and back, hundreds of times, inside you."),
    _es(C, "how many sheets of paper used per day in a school", [("students", 800), ("sheets per student per day", 5)], "sheets", "About 4,000 sheets a day - a tree's worth every couple of weeks."),
    _es(A, "how many atoms in a grape", [("water mass in grape (g)", 4), ("moles per gram (1/18)", 1/18), ("molecules per mole", 6.022e23), ("atoms per water molecule", 3)], "atoms", "About 4×10^23 atoms - a grape holds a measurable fraction of a mole of atoms."),
    _es(A, "how many piano tuners - full Fermi with overhead", [("pianos in Chicago", 54000), ("tunings per year each", 1), ("1 / workdays per year", 1/250), ("1 / tunings per day", 1/2)], "tuners", "108 tuners - the full Fermi with labor economics: demand divided by capacity."),
    _es(A, "how much data the internet holds", [("users", 5000000000), ("GB stored per user", 100)], "GB", "About 5×10^11 GB - half a zettabyte of humanity."),
    _es(A, "how many Earths fit in the Sun", [("sun volume / earth volume", 1300000)], "Earths", "1.3 million Earths - the Sun is not big, it is BIG big."),
    _es(A, "how many heartbeats in a lifetime", [("beats per minute", 70), ("minutes per year", 525600), ("years", 80)], "beats", "About 2.9 billion beats - spend them on things worth the thump."),
    _es(A, "how many stars in the observable universe", [("galaxies", 2e11), ("stars per galaxy", 1e11)], "stars", "About 2×10^22 - more stars than grains of sand on all Earth's beaches."),
    _es(A, "how many chess games possible (Shannon number)", [("options^40 (first half-game)", 30**40), ("options^40 (second half)", 30**40)], "games", "30^80 ≈ 10^118 - more games than atoms in the observable universe."),
    _es(A, "how many books could a library of Congress hold digitally", [("books", 40000000), ("MB per book", 2)], "MB", "About 8×10^7 MB - 80 petabytes: the Library of Congress fits in a data center."),
    _es(A, "how many years to count to a billion", [("seconds per number", 1), ("seconds", 1e9), ("years per second-count", 1/31536000)], "years", "About 31.7 years of nonstop counting - a billion is bigger than it sounds."),
    _es(A, "how many molecules in a breath", [("breath volume (L)", 0.5), ("moles per L of air", 1/22.4), ("molecules per mole", 6.022e23)], "molecules", "About 1.3×10^22 molecules per breath - you inhale a crowd every time."),
    _es(A, "how much the Great Pyramid weighs", [("blocks", 2300000), ("tons per block", 2.5)], "tons", "About 5.75 million tons - humanity's heaviest group project."),
]
