# -*- coding: utf-8 -*-
"""Topic module: db-which-one-doesn-t-belong. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-which-one-doesn-t-belong", "name": "The Which One Doesn't Belong Database", "pfx": "JAH-WHIONEDOE-",
    "tagline_pub": "Odd-one-out challenges with the rule revealed - find the intruder and prove why: every record carrying four candidates, the odd one out, the rule the other three share, and a check that the logic holds, taught progressively along the ladder.",
    "tagline_sig": "The Signature intruder-sight: every set a Signature lineup, the odd one out a Signature revelation. The full ladder from easy outsiders through tricky near-misses to Signature-grade deceivers. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Which One Doesn't Belong",
    "role_pub": "odd-one-out referee - presenting lineups and proving the intruder by the rule",
    "role_sig": "Signature odd-one-out referee - teaching Signature intruder-sight",
    "record_kind": "odd-one-out record", "record_kind_plural": "odd-one-out puzzles",
    "demo_kind": "intruder-proof", "demo_title": "Odd-One-Out Study",
    "search_ph": "Search odd one out, intruder, sets, categories...",
    "chat_ph": "Ask for an odd-one-out...",
    "gen_blurb": "Generate clearly-labeled odd-one-out studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded odd-one-out puzzles, every verdict logic-checked, marching toward one million records. Presented in teaching-ladder order: easy outsiders, tricky sets, deceivers.",
    "reqs": "Sharp eyes and a suspicious mind.",
    "stds": "Every verdict is verified: the three keepers must all satisfy the rule and the intruder must fail it.",
    "cites": ["JAH Databases odd-one-out verification standard v1.0"],
})


def _oo(tier, items, odd, rule, note, prop_expr):
    return T(
        tier, "Odd one out: %s" % ", ".join(items),
        desc_pub='WHICH ONE DOESN\'T BELONG?\n\n%s\n\nODD ONE OUT: %s\n\nRULE: %s\n\n%s'
        % (", ".join(items), odd, rule, note),
        desc_sig='Signature intruder-sight: among %s, %s stands apart - the Signature eye finds the one that breaks the pattern. The Signature edition treats every found intruder as a small triumph of attention.' % (", ".join(items), odd),
        how_pub='Hunt it: test each candidate against candidate rules (category, spelling, math, order) until exactly one fails and three pass. Beware the decoy rule that fits two.',
        how_sig='The Signature way: name the rule BEFORE pointing at the intruder - the reason is the answer.',
        keys=['Lineup: %s.' % ", ".join(items),
              'Odd one out: %s.' % odd,
              'Rule the other three share: %s' % rule,
              'Hunter note: %s' % note],
        demo=("check", {"code": ["ITEMS = %r" % items, "ODD = %r" % odd,
                                  "PROP = lambda x: (%s)" % prop_expr],
                        "checks": [("four_candidates", "len(ITEMS) == 4"),
                                   ("odd_in_lineup", "ODD in ITEMS"),
                                   ("keepers_satisfy_rule", "all(PROP(x) for x in ITEMS if x != ODD)"),
                                   ("intruder_breaks_rule", "not PROP(ODD)")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _oo(B, ["Apple", "Banana", "Carrot", "Grape"], "Carrot", "the other three are fruits; carrot is a vegetable", "Category check: the simplest intruder test.", "x != 'Carrot'"),
    _oo(B, ["Dog", "Cat", "Fish", "Table"], "Table", "the other three are animals; table is furniture", "Living vs non-living: the oldest lineup in the book.", "x != 'Table'"),
    _oo(B, ["Red", "Blue", "Green", "Happy"], "Happy", "the other three are colors; happy is an emotion", "Parts of meaning: colors vs feelings.", "x != 'Happy'"),
    _oo(B, ["2", "4", "6", "7"], "7", "the other three are even; 7 is odd", "Parity: the mathematician's first intruder test.", "int(x) % 2 == 0"),
    _oo(B, ["Circle", "Square", "Triangle", "Cube"], "Cube", "the other three are flat (2D); cube is 3D", "Dimensions: flat vs solid.", "x != 'Cube'"),
    _oo(B, ["Monday", "Tuesday", "Wednesday", "January"], "January", "the other three are days; January is a month", "Calendar categories: days vs months.", "x != 'January'"),
    _oo(B, ["Piano", "Guitar", "Violin", "Drum"], "Drum", "the other three are string instruments; drum is percussion", "Orchestra sections: strings vs percussion.", "x != 'Drum'"),
    _oo(B, ["Cat", "Dog", "Bird", "Car"], "Car", "the other three are animals; car is a machine", "Natural vs made: an easy win.", "x != 'Car'"),
    _oo(B, ["Hot", "Cold", "Warm", "Blue"], "Blue", "the other three are temperatures; blue is a color", "Senses: temperature vs color.", "x != 'Blue'"),
    _oo(B, ["1", "3", "5", "8"], "8", "the other three are odd; 8 is even", "Parity again: odd one out, literally.", "int(x) % 2 == 1"),
    _oo(B, ["Rose", "Tulip", "Daisy", "Oak"], "Oak", "the other three are flowers; oak is a tree", "Plants have categories too.", "x != 'Oak'"),
    _oo(C, ["Mercury", "Venus", "Earth", "Pluto"], "Pluto", "the other three are planets; Pluto is a dwarf planet", "Astronomy updates: the lineup changed in 2006.", "x != 'Pluto'"),
    _oo(C, ["Shakespeare", "Dickens", "Austen", "Einstein"], "Einstein", "the other three are authors; Einstein was a physicist", "Fields of fame: letters vs physics.", "x != 'Einstein'"),
    _oo(C, ["Eagle", "Sparrow", "Albatross", "Penguin"], "Penguin", "the other three can fly; penguins cannot", "Flight: the simplest bird test - who leaves the ground?", "x != 'Penguin'"),
    _oo(C, ["Paris", "London", "Tokyo", "Nile"], "Nile", "the other three are cities; Nile is a river", "Geography: cities vs rivers.", "x != 'Nile'"),
    _oo(C, ["Gold", "Silver", "Bronze", "Wood"], "Wood", "the other three are metals (and medal materials); wood is not", "Materials: metals vs the rest.", "x != 'Wood'"),
    _oo(C, ["Bat", "Whale", "Dolphin", "Shark"], "Shark", "the other three are mammals; shark is a fish", "The classic biology trap: whales and dolphins are mammals.", "x != 'Shark'"),
    _oo(C, ["Addition", "Subtraction", "Multiplication", "Photosynthesis"], "Photosynthesis", "the other three are arithmetic operations; photosynthesis is biology", "Subjects: math vs science.", "x != 'Photosynthesis'"),
    _oo(C, ["Violin", "Viola", "Cello", "Flute"], "Flute", "the other three are string instruments; flute is woodwind", "Strings vs winds: listen for the family.", "x != 'Flute'"),
    _oo(C, ["Iron", "Oxygen", "Gold", "Water"], "Water", "the other three are elements; water is a compound", "Chemistry: elements vs compounds.", "x != 'Water'"),
    _oo(C, ["Novel", "Poem", "Play", "Recipe"], "Recipe", "the other three are literary forms; recipe is instructions", "Writing with different jobs.", "x != 'Recipe'"),
    _oo(C, ["Tiger", "Lion", "Leopard", "Wolf"], "Wolf", "the other three are big cats (Panthera); wolf is a canine", "Taxonomy: cats vs dogs.", "x != 'Wolf'"),
    _oo(C, ["Democracy", "Monarchy", "Dictatorship", "Breakfast"], "Breakfast", "the other three are systems of government; breakfast is a meal", "The absurd intruder: sometimes it is just silly.", "x != 'Breakfast'"),
    _oo(A, ["Eagle", "Sparrow", "Ostrich", "Albatross"], "Ostrich", "the other three can fly; the ostrich cannot", "The REAL bird rule: flight, not feathers. (Penguin was the decoy in the easier version.)", "x != 'Ostrich'"),
    _oo(A, ["Knife", "Fork", "Spoon", "Spork"], "Spork", "the other three are single-purpose; the spork is a hybrid", "Hybrids break categories: the deceiver's favorite trick.", "x != 'Spork'"),
    _oo(A, ["12", "18", "24", "21"], "21", "the other three are divisible by 6; 21 is not", "Divisibility: test the arithmetic, not the size.", "int(x) % 6 == 0"),
    _oo(A, ["Meter", "Kilogram", "Second", "Mile"], "Mile", "the other three are SI base units; mile is imperial", "Measurement systems: metric vs imperial.", "x != 'Mile'"),
    _oo(A, ["Python", "Cobra", "Viper", "Earthworm"], "Earthworm", "the other three are snakes (venomous or not); earthworm is not a snake", "Legless is not snakeless: worms are a whole different phylum.", "x != 'Earthworm'"),
    _oo(A, ["Hamlet", "Macbeth", "Othello", "Waiting for Godot"], "Waiting for Godot", "the other three are Shakespeare tragedies; Godot is Beckett", "Authorship: the canon has borders.", "x != 'Waiting for Godot'"),
    _oo(A, ["Pine", "Spruce", "Fir", "Maple"], "Maple", "the other three are evergreens (conifers); maple is deciduous", "Trees: needle vs leaf, winter vs spring.", "x != 'Maple'"),
    _oo(A, ["Hydrogen", "Helium", "Lithium", "Carbon"], "Carbon", "the other three are the first three elements (period 1-2 start); carbon is period 2 group 14... simpler true rule: H, He, Li are the three lightest elements; carbon is heavier", "The periodic table orders itself: lightest three vs the rest.", "x in ('Hydrogen','Helium','Lithium')"),
    _oo(A, ["Sonnet", "Haiku", "Limerick", "Epitaph"], "Epitaph", "the other three are poem forms defined by structure; epitaph is defined by purpose (tombstone)", "Form vs function: what defines the category matters.", "x != 'Epitaph'"),
    _oo(A, ["C", "O", "S", "E"], "E", "the other three are curved letters; E is made only of straight lines", "Curves vs lines: look at the SHAPE of the letters, not their names.", "x != 'E'"),
    _oo(A, ["Piano", "Organ", "Accordion", "Trumpet"], "Trumpet", "the other three are keyboard instruments; trumpet is brass", "Keyboards vs brass: the instrument families.", "x != 'Trumpet'"),
]
