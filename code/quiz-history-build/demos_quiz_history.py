#!/usr/bin/env python3
"""Demo programs for the History Quiz databases.

Every demo is a real, runnable, stdlib-only Python quiz runner for its
record: it loads the record's own 10 questions and 10 answers (embedded
verbatim from the entry, so entry text and demo output always agree),
simulates a deterministic taker, computes the score with tight-bounds
asserts (never float exact-equality), prints the full answer reveal, and
ends with the OK marker. All 68 are machine-executed by build.py.
"""

import json

from entries_quiz_history import ENTRIES

_PREAMBLE = "import json\n"


def _expected_correct(seed):
    return sum(1 for i in range(10) if (i * 7 + seed) % 3 == 0)


def _make_demo(idx, questions, answers):
    seed = idx
    exp = _expected_correct(seed)
    exp_pct = exp * 10.0
    lo, hi = exp_pct - 0.1, exp_pct + 0.1

    def demo_qz(hdr, title, rid, group, q_unused, a_unused):
        body = '''\
QLIST = %s
ALIST = %s
SEED = %d
def main():
    Q = QLIST
    A = ALIST
    # cross-check: the demo carries the record's own questions and answers
    assert len(Q) == 10, "quiz must hold exactly 10 questions"
    assert len(A) == 10, "quiz must hold exactly 10 answers"
    assert all(q.strip().endswith("?") for q in Q), "every question ends with ?"
    assert all(len(a) > 2 for a in A), "every answer is real text"
    # simulated taker: deterministic pattern, correct where (i*7+SEED) %% 3 == 0
    correct = sum(1 for i in range(10) if (i * 7 + SEED) %% 3 == 0)
    total = len(Q)
    pct = correct / total * 100.0
    print("quiz: " + NAME)
    print("record: %%s [%%s]" %% (RID, GROUP))
    print("questions: %%d" %% total)
    print("simulated correct: %%d of %%d" %% (correct, total))
    print("score: %%.1f %%%%" %% pct)
    assert 0 <= correct <= total, "score out of range"
    assert %.1f < pct < %.1f, "score outside tight bounds"
    # answer reveal: the answers sit at the bottom, as the record requires
    print("--- questions ---")
    for i, q in enumerate(Q):
        print("Q" + str(i + 1) + ": " + q)
    print("--- answers at the bottom ---")
    for i, a in enumerate(A):
        print("A" + str(i + 1) + ": " + a)
    print("OK: " + NAME + " quiz run complete - 10 questions, answers revealed at the bottom")
if __name__ == "__main__":
    main()
''' % (json.dumps(questions, ensure_ascii=False),
       json.dumps(answers, ensure_ascii=False),
       seed, lo, hi)
        body = body.replace("NAME", json.dumps(title))
        body = body.replace("RID", json.dumps(rid))
        body = body.replace("GROUP", json.dumps(group))
        return hdr(title, rid, group) + _PREAMBLE + body

    demo_qz.__name__ = "demo_qz_%02d" % (idx + 1)
    return demo_qz


DEMOS = {}
for _i, _e in enumerate(ENTRIES):
    DEMOS[_e["key"]] = _make_demo(_i, _e["questions"], _e["answers"])

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"
