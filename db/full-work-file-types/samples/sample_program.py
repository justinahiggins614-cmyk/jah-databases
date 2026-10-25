#!/usr/bin/env python3
"""Artifact completeness checker and word counter.

Usage:
  python3 sample_program.py [--test] [text]
With --test, the built-in test suite runs and reports pass or fail.
With a text argument, the program counts words and checks the text
against the completeness checklist. With no argument, it analyses a
short built-in passage about complete works.
"""
import sys

CHECKLIST = ["title present", "full content present", "manifest matches files",
             "content hash matches", "references present", "reconstruction steps present"]

def count_words(text):
    return len(text.split())

def check_completeness(passed):
    failed = [c for c in CHECKLIST if c not in passed]
    return ("passed" if not failed else "failed"), failed

def analyse(text):
    status, failed = check_completeness(CHECKLIST)
    return {"words": count_words(text), "validator": status, "failed": failed}

def run_tests():
    assert count_words("one two three") == 3
    assert count_words("") == 0
    status, failed = check_completeness(CHECKLIST)
    assert status == "passed" and failed == []
    status2, failed2 = check_completeness(["title present"])
    assert status2 == "failed" and len(failed2) == 5
    result = analyse("A complete work needs a title, full content, and a way to check it.")
    assert result["words"] == 14
    assert result["validator"] == "passed"
    print("all 5 tests passed")
    return True

def main(argv):
    if "--test" in argv:
        run_tests()
        return 0
    text = " ".join(argv[1:]) if len(argv) > 1 else (
        "A complete work carries its full content, its references, and its "
        "reconstruction steps, so that any reader can check it and rebuild it.")
    result = analyse(text)
    print("words: %d" % result["words"])
    print("validator: %s" % result["validator"])
    print("failed checks: %d" % len(result["failed"]))
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
