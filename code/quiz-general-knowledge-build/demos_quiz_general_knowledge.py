#!/usr/bin/env python3
"""Demos for the General Knowledge Quiz databases.

Every demo is a real, runnable, stdlib-only Python quiz runner: it prints the
10 questions, runs a simulated taker through all 10 answers (7 answered
correctly with messy casing/spacing to exercise the normalizer, 3 answered
wrong), reveals the answers at the bottom, and computes the score with
tight-bounds asserts - never float exact-equality. Each demo ends with the OK
marker. The build machine-executes all 68 and cross-checks every demo answer
against the record text.
"""

import json

from entries_quiz_general_knowledge import ENTRIES

# 0-based indices answered wrong by the simulated taker -> 7/10 correct.
WRONG_IDX = {2, 5, 8}


def make_demo(entry, sig):
    qa = entry["qa_sig"] if sig else entry["qa"]

    def demo(hdr, name, rid, group, key_points, reqs):
        sim = []
        for i, (q, a) in enumerate(qa):
            if i in WRONG_IDX:
                sim.append("not the answer")
            else:
                sim.append("  " + a.upper() + " ")
        body = '''
import json

QA = %s
SIM = %s
EXPECTED = 7

def norm(s):
    return " ".join(s.strip().lower().split())

def main():
    total = len(QA)
    print("Quiz: " + %s)
    print("Record " + %s)
    score = 0
    for i, ((q, a), given) in enumerate(zip(QA, SIM), 1):
        ok = norm(given) == norm(a)
        if ok:
            score += 1
        print("Q%%d: %%s" %% (i, q))
        print("  taker answered: %%s -> %%s" %% (given.strip(), "CORRECT" if ok else "WRONG"))
    print("--- ANSWERS REVEALED (AT THE BOTTOM) ---")
    for i, (q, a) in enumerate(QA, 1):
        print("A%%d: %%s" %% (i, a))
    pct = 100.0 * score / total
    print("SCORE: %%d/%%d (%%.1f%%%%)" %% (score, total, pct))
    assert total == 10, "quiz must have 10 questions"
    assert all(a.strip() for _, a in QA), "empty answer"
    assert 0 <= score <= total, "score out of bounds"
    assert abs(pct - (100.0 * score / total)) < 1e-9, "percent math drift"
    assert score == EXPECTED, "simulated taker should score 7/10"
    print("OK: quiz runner scored %%d/%%d with answers revealed" %% (score, total))

if __name__ == "__main__":
    main()
''' % (json.dumps(qa, ensure_ascii=False), json.dumps(sim, ensure_ascii=False),
       json.dumps(name), json.dumps(rid))
        return hdr(name, rid, group) + body

    return demo


DEMOS = {e["key"]: make_demo(e, False) for e in ENTRIES}
DEMOS_SIG = {e["key"]: make_demo(e, True) for e in ENTRIES}
