#!/usr/bin/env python3
"""Demo programs for the Language Arts Quiz databases.

Every demo is a real, runnable, stdlib-only Python quiz runner built from the
same QA data as its record: it prints the ten questions, grades a simulated
run, prints the real computed score, asserts tight bounds (never float
exact-equality), prints the answer key at the bottom, and ends with the OK
marker. Build.py machine-executes all 68 demos and cross-checks demo stdout
against entry text (Q1 and A1 must appear verbatim).

This module imports ENTRIES (one direction only - entries never imports
demos), so DEMOS stays in sync with the authored quizzes by construction.
"""

import json

from entries_quiz_language_arts import ENTRIES

_BODY = '''\\
import json

def main():
    qa = json.loads(PAYLOAD)
    print("QUIZ RUNNER: " + NAME)
    print("questions: %d" % len(qa))
    for i, item in enumerate(qa, 1):
        print("Q%d: %s" % (i, item[0]))
    # simulated test-taker: answers the odd-numbered questions correctly
    pattern = [(i % 2 == 0) for i in range(len(qa))]
    given = [a if ok else "no answer given"
             for (q, a), ok in zip(qa, pattern)]
    def norm(s):
        return " ".join(s.strip().lower().split())
    correct = sum(1 for (q, a), g in zip(qa, given) if norm(g) == norm(a))
    expected = sum(1 for ok in pattern if ok)
    pct = 100.0 * correct / len(qa)
    print("simulated run: %d of %d correct" % (correct, len(qa)))
    print("score: %.1f percent" % pct)
    assert len(qa) == 10, "a quiz holds ten questions"
    assert all(q.strip() and a.strip() for q, a in qa), "no blank questions or answers"
    assert correct == expected, "grader miscounted"
    assert 49.99 < pct < 50.01, "score out of tight bounds"
    print("ANSWER KEY - at the bottom, as ordered:")
    for i, item in enumerate(qa, 1):
        print("A%d: %s" % (i, item[1]))
    print("OK: " + NAME + " ran the full quiz")
if __name__ == "__main__":
    main()
'''


def make_quiz_demo(entry):
    def demo_fn(hdr, name, rid, group, points, req):
        payload = json.dumps(json.dumps([[q, a] for q, a, _x in entry["qa"]]))
        body = _BODY.replace("PAYLOAD", payload).replace("NAME", json.dumps(entry["name"]))
        return hdr(name, rid, group) + body
    return demo_fn


DEMOS = {e["key"]: make_quiz_demo(e) for e in ENTRIES}
assert len(DEMOS) == 34
