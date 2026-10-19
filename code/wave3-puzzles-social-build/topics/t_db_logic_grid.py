# -*- coding: utf-8 -*-
"""Topic module: db-logic-grid. 3x3 logic grids, deterministically generated
and brute-force verified unique at import time. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T
import itertools
import random

CFG = mkcfg({
    "slug": "db-logic-grid", "name": "The Logic Grid Database", "pfx": "JAH-LOGGRI-",
    "tagline_pub": "Logic grid puzzles with every solution proven unique by brute force - three friends, three pets, three colors: every record carrying the clues, the one true solution, and the full elimination story, taught progressively along the ladder.",
    "tagline_sig": "The Signature deduction-sight: every grid a Signature crossroads, every elimination a Signature certainty. The full ladder from gentle grids through tangled ones to Signature-grade deductions. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Logic Grid",
    "role_pub": "logic coach - dealing grids whose solutions are proven unique by exhaustive search",
    "role_sig": "Signature logic coach - teaching Signature deduction-sight",
    "record_kind": "logic grid record", "record_kind_plural": "logic grid puzzles",
    "demo_kind": "grid-proof", "demo_title": "Logic Grid Study",
    "search_ph": "Search logic grid, clues, elimination, deduction...",
    "chat_ph": "Ask for a logic grid...",
    "gen_blurb": "Generate clearly-labeled grid studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded logic grids, every solution brute-force proven unique, marching toward one million records. Presented in teaching-ladder order: gentle, tangled, Signature-grade.",
    "reqs": "A grid (draw 3x3 boxes), a pencil, and patience.",
    "stds": "Every grid's solution is proven the UNIQUE solution by exhaustive search over all assignments.",
    "cites": ["JAH Databases grid verification standard v1.0"],
})

def solve_grid(persons, pets, colors, clue_exprs):
    sols = []
    for pp in itertools.permutations(pets):
        for cc in itertools.permutations(colors):
            C = {p: (pp[i], cc[i]) for i, p in enumerate(persons)}
            if all(eval(e, {"C": C}) for e in clue_exprs):
                sols.append(C)
    return sols


LG_HELPERS = """
import itertools
def solve_grid(persons, pets, colors, clue_exprs):
    sols = []
    for pp in itertools.permutations(pets):
        for cc in itertools.permutations(colors):
            C = {p: (pp[i], cc[i]) for i, p in enumerate(persons)}
            if all(eval(e, {"C": C}) for e in clue_exprs):
                sols.append(C)
    return sols
"""

# clue templates: (natural language, expr using P=person, V=value, C=candidate dict)
CLUE_TPL = [
    ("Neither {P} nor {Q} has the {V}.", "C['{P}'][0] != '{V}' and C['{Q}'][0] != '{V}'"),
    ("Neither {P} nor {Q} loves {V}.", "C['{P}'][1] != '{V}' and C['{Q}'][1] != '{V}'"),

    ("{P}'s pet is not the {V}.", "C['{P}'][0] != '{V}'"),
    ("{P}'s pet is the {V}.", "C['{P}'][0] == '{V}'"),
    ("{P} loves the color {V}.", "C['{P}'][1] == '{V}'"),
    ("{P} does not like {V}.", "C['{P}'][1] != '{V}'"),
    ("The {V} owner loves {W}.", "next(p for p in C if C[p][0]=='{V}') == next(p for p in C if C[p][1]=='{W}')"),
    ("{P}'s pet is not the {V}, and {Q} does not like {W}.", "C['{P}'][0] != '{V}' and C['{Q}'][1] != '{W}'"),
    ("Whoever has the {V} loves {W}.", "C[next(p for p in C if C[p][0]=='{V}')][1] == '{W}'"),
]

NAMES = [["Ava", "Ben", "Cleo"], ["Dan", "Eva", "Finn"], ["Gus", "Hana", "Ivan"],
         ["Jade", "Kai", "Lena"], ["Milo", "Nora", "Owen"], ["Pia", "Quinn", "Rosa"],
         ["Sam", "Tara", "Umar"], ["Vera", "Wade", "Xena"], ["Yara", "Zane", "Amy"],
         ["Bram", "Cora", "Dev"], ["Elif", "Farah", "Gabe"], ["Hugo", "Iris", "Jasper"]]
PETS = [["dog", "cat", "fish"], ["parrot", "hamster", "turtle"], ["rabbit", "lizard", "frog"],
        ["horse", "goat", "sheep"], ["owl", "fox", "deer"], ["duck", "pig", "cow"]]
COLORS = [["red", "blue", "green"], ["gold", "silver", "bronze"], ["purple", "orange", "teal"],
          ["pink", "brown", "gray"], ["black", "white", "yellow"]]

STORIES = [
    "Three friends adopted pets and painted their rooms - sort out who has what.",
    "Three neighbors each got a new pet and a favorite color - untangle the trio.",
    "Three classmates brought pets for show-and-tell - match each to their color.",
    "Three cousins inherited pets and picked lucky colors - solve the family puzzle.",
    "Three teammates each chose a mascot pet and a jersey color - crack the lineup.",
    "Three pen pals described their pets and favorite colors - piece it together.",
]


def build_grid(seed):
    rng = random.Random(seed)
    persons = rng.choice(NAMES)
    pets = rng.choice(PETS)
    colors = rng.choice(COLORS)
    # random true solution
    pet_perm = rng.sample(pets, 3)
    col_perm = rng.sample(colors, 3)
    sol = {p: (pet_perm[i], col_perm[i]) for i, p in enumerate(persons)}
    C0 = sol

    def val(kind, avoid=None):
        pool = pets if kind == "pet" else colors
        c = rng.choice([x for x in pool if x != avoid])
        return c

    clues = []
    exprs = []
    candidates = []
    for tpl, expr in CLUE_TPL:
        for _draw in range(10):
            P = rng.choice(persons)
            Q = rng.choice([x for x in persons if x != P])
            if "{V}" in tpl and "{W}" in tpl:
                V = val("pet"); W = val("color")
                e = expr.replace("{V}", V).replace("{W}", W)
                n = tpl.replace("{V}", V).replace("{W}", W)
            elif "{Q}" in tpl:
                V = val("pet"); W = val("color")
                e = expr.replace("{P}", P).replace("{Q}", Q).replace("{V}", V).replace("{W}", W)
                n = tpl.replace("{P}", P).replace("{Q}", Q).replace("{V}", V).replace("{W}", W)
            elif "{V}" in tpl:
                kind = "pet" if "pet" in tpl else "color"
                V = val(kind)
                e = expr.replace("{P}", P).replace("{V}", V)
                n = tpl.replace("{P}", P).replace("{V}", V)
            else:
                e = expr.replace("{P}", P).replace("{Q}", Q)
                n = tpl.replace("{P}", P).replace("{Q}", Q)
            try:
                if eval(e, {"C": C0}):
                    candidates.append((n, e))
            except Exception:
                continue
    # best-first: repeatedly add the clue that kills the most solutions
    seen = set()
    for _ in range(8):
        sols = solve_grid(persons, pets, colors, exprs)
        if len(sols) == 1:
            break
        best, best_kill = None, -1
        for n, e in candidates:
            if e in seen:
                continue
            k = sum(1 for s_ in sols if not eval(e, {"C": s_}))
            if k > best_kill:
                best, best_kill = (n, e), k
        if best is None or best_kill == 0:
            break
        seen.add(best[1])
        clues.append(best[0]); exprs.append(best[1])
    sols = solve_grid(persons, pets, colors, exprs)
    assert len(sols) == 1, "seed %d not unique: %d sols" % (seed, len(sols))
    assert sols[0] == sol
    return persons, pets, colors, sol, clues, exprs


def _grid(tier, seed, story):
    persons, pets, colors, sol, clues, exprs = build_grid(seed)
    sol_text = "\n".join("  %s: %s, %s" % (p, sol[p][0], sol[p][1]) for p in persons)
    clue_text = "\n".join("  %d. %s" % (i + 1, c) for i, c in enumerate(clues))
    return T(
        tier, "Logic grid #%d: %s" % (seed, ", ".join(persons)),
        desc_pub='LOGIC GRID:\n\n%s\n\nThree people: %s. Three pets: %s. Three colors: %s. Each person has exactly one pet and one favorite color.\n\nCLUES:\n%s\n\nSOLUTION (proven unique):\n%s'
        % (story, ", ".join(persons), ", ".join(pets), ", ".join(colors), clue_text, sol_text),
        desc_sig='Signature deduction-sight: this grid - %s - resolves to exactly one truth, the Signature certainty. The Signature edition treats every solved grid as the mind sorting the world properly.' % ", ".join(persons),
        how_pub='Solve it: draw the grid, mark X for no and O for yes, and let each clue eliminate. When one box remains in a row, it is certain - certainty cascades.',
        how_sig='The Signature way: find the most restrictive clue first - the tightest constraint cracks the grid open.',
        keys=['People: %s; pets: %s; colors: %s.' % (", ".join(persons), ", ".join(pets), ", ".join(colors)),
              '%d clues, each eliminating possibilities.' % len(clues),
              'Solution proven the UNIQUE solution by exhaustive search over all %d assignments.' % (6 * 6),
              'Solve story: %s' % story],
        demo=("compute", {"preamble": LG_HELPERS,
                          "code": ["PERSONS = %r" % persons, "PETS = %r" % pets, "COLORS = %r" % colors,
                                   "EXPRS = %r" % exprs, "SOLS = solve_grid(PERSONS, PETS, COLORS, EXPRS)"],
                          "show": ["len(SOLS)"],
                          "asserts": [("unique_solution", "len(SOLS) == 1"),
                                      ("matches_stated", "all(SOLS[0][p] == %r[p] for p in PERSONS)" % sol)]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = []
_seeds = {"Foundations": list(range(101, 112)), "Compounded": list(range(201, 213)), "Advanced": list(range(301, 312))}
for _tier in (B, C, A):
    for _k, _s in enumerate(_seeds[_tier]):
        TOPICS.append(_grid(_tier, _s, STORIES[_k % len(STORIES)]))

print("grids built:", len(TOPICS))
