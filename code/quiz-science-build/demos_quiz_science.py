#!/usr/bin/env python3
"""Demos for the Science Quiz databases (Manon's 2026-10-17 16:15 order).

Every demo is a working quiz runner: it prints the record's 10 questions,
reveals the answer key AT THE BOTTOM, then runs a simulated graded attempt
and asserts tight bounds on the score (never float exact-equality). All
questions and answers are embedded from the same ENTRIES source as the
records, so entry text and demo output can never drift apart.

Real computed values: question count, answer count, correct count, score.
"""

from entries_quiz_science import ENTRIES


def _make_demo(entry):
    quiz_repr = repr([(q, a) for (q, a) in entry["questions"]])

    def fn(hdr_fn, name, rid, group, points, req):
        title = name.replace("'", "")
        return hdr_fn(name, rid, group) + ('''
QUIZ = %s

def _grade(simulated):
    """Score a simulated attempt against the answer key."""
    got = 0
    for (q, a), s in zip(QUIZ, simulated):
        if s.strip().lower() == a.strip().lower():
            got += 1
    return got

def main():
    print("QUIZ: %%s" %% %s)
    print("Record %s [%s] - 10 questions - answer key at the bottom")
    for i, (q, a) in enumerate(QUIZ, 1):
        print("Q%%d: %%s" %% (i, q))
    print("")
    print("ANSWER KEY (at the bottom):")
    for i, (q, a) in enumerate(QUIZ, 1):
        print("A%%d: %%s" %% (i, a))
    print("")
    n = len(QUIZ)
    assert n == 10, "quiz must have 10 questions, got %%d" %% n
    assert all(q and a for q, a in QUIZ), "every question and answer must be non-empty"
    assert all(isinstance(a, str) and len(a) > 1 for q, a in QUIZ), "answers must be real text"
    # simulated graded attempt: first 7 answers exactly right, last 3 wrong
    simulated = [a for q, a in QUIZ[:7]] + ["NOT THE ANSWER"] * 3
    correct = _grade(simulated)
    score = correct / n
    assert correct == 7, "expected 7 correct, got %%d" %% correct
    assert abs(score - 0.70) < 0.011, "score out of tight bounds: %%r" %% score
    assert 0.0 <= score <= 1.0, "score out of range"
    print("Simulated attempt graded: %%d/%%d correct (%%.0f%%%%)" %% (correct, n, score * 100))
    print("OK: quiz runner verified - 10 questions, answer key at bottom, scoring exact")

if __name__ == "__main__":
    main()
''' % (quiz_repr, repr(title), rid, group))

    return fn


DEMOS = {e["key"]: _make_demo(e) for e in ENTRIES}
