#!/usr/bin/env python3
"""Demo programs for the Mathematics Quiz databases.

Every demo is real, runnable, stdlib-only Python: a quiz runner that prints
each question, reveals the stored answer, RECOMPUTES the answer from the
question's own numbers (tight-bounds asserts - Fraction-exact, then float
with tolerance, then case-insensitive string - never float exact-equality),
prints the scoring bands, and ends with the OK marker.

Two quizzes carry independent brute-force solvers that derive the answers
from the puzzle statements themselves (not from the stored answers):
  - qz_truth: knights-and-knaves case analysis over all type assignments.
  - qz_grid:  three-house logic grid solved by exhaustive elimination.
All 68 demos are machine-executed by build.py; every stored answer is also
cross-checked against the record text by the build.
"""

import json

_BODY = '''\
import json, math, itertools
from fractions import Fraction

TITLE = __TITLE__
RID = __RID__
QUESTIONS = json.loads(__QDATA__)

def _match(got, want, tol):
    gs, ws = str(got).strip(), str(want).strip()
    try:
        if Fraction(gs) == Fraction(ws):
            return True
    except Exception:
        pass
    try:
        if abs(float(gs) - float(ws)) <= tol:
            return True
    except Exception:
        pass
    return gs.lower() == ws.lower()

def qroots(a, b, c):
    d = math.sqrt(b * b - 4 * a * c)
    return [(-b + d) / (2 * a), (-b - d) / (2 * a)]

def _env():
    return {"math": math, "Fraction": Fraction, "qroots": qroots,
            "abs": abs, "round": round, "sorted": sorted, "tuple": tuple,
            "range": range, "all": all, "any": any, "len": len,
            "itertools": itertools}

__SOLVER__

def main():
    print("QUIZ: %s [%s]" % (TITLE, RID))
    solver_checks()
    score = 0
    for i, (q, want, check, tol) in enumerate(QUESTIONS, 1):
        got = eval(check, {"__builtins__": {}}, _env())
        good = _match(got, want, tol)
        print("Q%d: %s" % (i, q))
        print("    answer revealed: %s   (recomputed: %s)  %s"
              % (want, got, "PASS" if good else "FAIL"))
        assert good, "Q%d mismatch: want %r, recomputed %r" % (i, want, got)
        score += 10
    print("perfect-paper score: %d/100" % score)
    print("bands: 90-100 Quizmaster; 70-89 Sharp; 50-69 Warming up; below 50 climb again")
    assert score == 100
    print("OK: %s - %s - 10/10 answers verified" % (RID, TITLE))

if __name__ == "__main__":
    main()
'''

_SOLVER_NONE = '''\
def solver_checks():
    pass
'''

_SOLVER_TRUTH = '''\
def solver_checks():
    # knights tell truth, knaves lie: a[person] True == knight.
    def sols(names, stmts):
        out = []
        for bits in itertools.product([False, True], repeat=len(names)):
            a = dict(zip(names, bits))
            if all(a[sp] == fn(a) for sp, fn in stmts):
                out.append(a)
        return out
    # Q1: A says "B and I are both knaves."
    s = sols(['A', 'B'], [('A', lambda a: (not a['A']) and (not a['B']))])
    assert len(s) == 1 and s[0]['A'] is False, s
    assert QUESTIONS[0][1] == 'knave', QUESTIONS[0][1]
    # Q2: A says "B is a knave"; B says "A and I are opposite types."
    s = sols(['A', 'B'], [('A', lambda a: not a['B']),
                          ('B', lambda a: a['A'] != a['B'])])
    assert len(s) == 1 and s[0]['A'] is False, s
    assert QUESTIONS[1][1] == 'knave', QUESTIONS[1][1]
    # Q3: A says "I am a knave." -> impossible, zero solutions.
    s = sols(['A'], [('A', lambda a: not a['A'])])
    assert len(s) == 0, s
    assert QUESTIONS[2][1] == 'impossible', QUESTIONS[2][1]
    # Q4: A says "All three of us are knaves." -> A knave in every solution.
    s = sols(['A', 'B', 'C'],
             [('A', lambda a: (not a['A']) and (not a['B']) and (not a['C']))])
    assert s and all(x['A'] is False for x in s), s
    assert QUESTIONS[3][1] == 'knave', QUESTIONS[3][1]
    # Q5: A says "At least one of us is a knave."
    s = sols(['A', 'B'], [('A', lambda a: (not a['A']) or (not a['B']))])
    assert len(s) == 1 and s[0] == {'A': True, 'B': False}, s
    assert QUESTIONS[4][1] == 'A is a knight and B is a knave', QUESTIONS[4][1]
    # Q6: B says "A is a knight." -> a knave-B solution exists.
    s = sols(['A', 'B'], [('B', lambda a: a['A'])])
    assert any(x['B'] is False for x in s), s
    assert QUESTIONS[5][1] == 'yes', QUESTIONS[5][1]
    # Q7: A says "If I am a knight then B is a knave."
    s = sols(['A', 'B'], [('A', lambda a: (not a['A']) or (not a['B']))])
    assert len(s) == 1 and s[0] == {'A': True, 'B': False}, s
    assert QUESTIONS[6][1] == 'knave', QUESTIONS[6][1]
    # Q8: A says "Exactly one of us is a knight"; B says "A is lying."
    s = sols(['A', 'B'], [('A', lambda a: (a['A'] + a['B']) == 1),
                          ('B', lambda a: not a['A'])])
    assert len(s) == 1 and s[0] == {'A': True, 'B': False}, s
    assert QUESTIONS[7][1] == 'knave', QUESTIONS[7][1]
    # Q9: A says "B is a knave"; B says "C is a knave"; C says "A and B are knaves."
    s = sols(['A', 'B', 'C'],
             [('A', lambda a: not a['B']),
              ('B', lambda a: not a['C']),
              ('C', lambda a: (not a['A']) and (not a['B']))])
    assert len(s) == 1, s
    assert sum(s[0].values()) == 1, s
    assert QUESTIONS[8][1] == '1', QUESTIONS[8][1]
    print("truth solver: 9/9 puzzle statements independently derived from cases")
'''

_SOLVER_GRID = '''\
def solver_checks():
    houses = [1, 2, 3]
    sols = []
    for cp in itertools.permutations(['red', 'green', 'blue']):
        for pp in itertools.permutations(['cats', 'dogs', 'birds']):
            for op in itertools.permutations(['Amy', 'Brad', 'Cara']):
                color = dict(zip(houses, cp))
                pet = dict(zip(houses, pp))
                owner = dict(zip(houses, op))
                if owner[1] != 'Amy':
                    continue                      # clue 1
                if color[2] != 'red':
                    continue                      # clue 2
                h_brad = [h for h in houses if owner[h] == 'Brad'][0]
                if pet[h_brad] != 'dogs':
                    continue                      # clue 3
                h_green = [h for h in houses if color[h] == 'green'][0]
                if pet[h_green] != 'birds':
                    continue                      # clue 4
                h_cara = [h for h in houses if owner[h] == 'Cara'][0]
                if color[h_cara] != 'blue':
                    continue                      # clue 5
                sols.append((color, pet, owner))
    assert len(sols) == 1, "grid not unique: %d" % len(sols)
    color, pet, owner = sols[0]
    house_of = lambda pred: [h for h in houses if pred(h)][0]
    derived = [
        owner[1],
        color[2],
        owner[house_of(lambda h: pet[h] == 'dogs')],
        pet[house_of(lambda h: color[h] == 'green')],
        owner[house_of(lambda h: color[h] == 'blue')],
        color[house_of(lambda h: owner[h] == 'Amy')],
        owner[house_of(lambda h: pet[h] == 'cats')],
        color[house_of(lambda h: owner[h] == 'Brad')],
        'house %d' % house_of(lambda h: pet[h] == 'birds'),
        owner[3],
    ]
    for i, d in enumerate(derived):
        assert QUESTIONS[i][1] == d, (i, QUESTIONS[i][1], d)
    print("grid solver: unique solution confirmed, 10/10 answers derived from the 5 clues")
'''


def _build(hdr_fn, title, rid, group, entry, solver):
    qdata = json.dumps([[q["q"], q["a"], q["check"], q["tol"]]
                        for q in entry["questions"]])
    prog = _BODY.replace("__TITLE__", json.dumps(title))
    prog = prog.replace("__RID__", json.dumps(rid))
    prog = prog.replace("__QDATA__", "r'''%s'''" % qdata)
    prog = prog.replace("__SOLVER__", solver)
    return hdr_fn(title, rid, group) + prog


def demo_quiz(hdr, title, rid, group, entry):
    return _build(hdr, title, rid, group, entry, _SOLVER_NONE)


def demo_quiz_truth(hdr, title, rid, group, entry):
    return _build(hdr, title, rid, group, entry, _SOLVER_TRUTH)


def demo_quiz_grid(hdr, title, rid, group, entry):
    return _build(hdr, title, rid, group, entry, _SOLVER_GRID)


DEMOS = {}


import entries_quiz_mathematics as _E

for _e in _E.ENTRIES:
    if _e["key"] == "qz_truth":
        DEMOS[_e["key"]] = demo_quiz_truth
    elif _e["key"] == "qz_grid":
        DEMOS[_e["key"]] = demo_quiz_grid
    else:
        DEMOS[_e["key"]] = demo_quiz
del _e, _E
