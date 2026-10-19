#!/usr/bin/env python3
"""Demo programs for the Pickup Lines databases.

Every demo is real, runnable, stdlib-only Python performing the actual
pickup-line computation for its record: the line's word/character counts
and estimated delivery time, a deterministic line-of-the-day picker
(sha256 of the date), and a context matcher scoring all 34 archive lines
by tag overlap. All are machine-executed by build.py: each prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker.
"""

import hashlib as _hashlib
import json as _json

_PREAMBLE = "import hashlib\nimport json\n"

_ROSTER_SRC = None

def _roster_code():
    global _ROSTER_SRC
    if _ROSTER_SRC is None:
        import importlib.util as _iu
        _spec = _iu.spec_from_file_location("ent", __file__.rsplit("/", 1)[0] + "/entries_pickup_lines.py")
        _ent = _iu.module_from_spec(_spec); _spec.loader.exec_module(_ent)
        _roster = [{"key": e["key"], "line": e["line"], "tags": e["tags"],
                    "rank": e["ladder_rank"], "name": e["name"]} for e in _ent.ENTRIES]
        _ROSTER_SRC = "ROSTER = " + repr(_roster) + "\n"
    return _ROSTER_SRC


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + _roster_code() + body.replace(
        "NAME", _json.dumps(name))

def demo_pk_simple_hello(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Hi. I could not walk past without saying hello. I am ___, and you looked like someone worth knowing."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 19
    assert chars == 100
    assert 7.5950 < secs < 7.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "simple_hello" in top))
    assert best == 1
    assert "simple_hello" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_genuine_compliment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "I hope this is okay to say - you have a wonderful laugh. It just made my whole coffee break better."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 21
    assert chars == 99
    assert 8.3950 < secs < 8.4050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "genuine_compliment" in top))
    assert best == 1
    assert "genuine_compliment" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_shared_moment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Did you see that sunset? I needed at least one other person to agree it was spectacular."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 17
    assert chars == 88
    assert 6.7950 < secs < 6.8050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "shared_moment" in top))
    assert best == 1
    assert "shared_moment" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_helpful_question(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "You look like you know this place - what is the one thing here I absolutely should not miss?"
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 19
    assert chars == 92
    assert 7.5950 < secs < 7.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "helpful_question" in top))
    assert best == 1
    assert "helpful_question" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_honest_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "I will be honest - I came over because talking to strangers is how I meet my favorite people. I am ___."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 22
    assert chars == 103
    assert 8.7950 < secs < 8.8050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "honest_intro" in top))
    assert best == 1
    assert "honest_intro" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_bright_smile(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Hi. [smile] I am ___. That is the whole line - the smile was doing most of the work."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 19
    assert chars == 84
    assert 7.5950 < secs < 7.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "bright_smile" in top))
    assert best == 1
    assert "bright_smile" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_kind_observation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "I saw you help that kid pick up his dropped books. That was genuinely lovely to watch."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 17
    assert chars == 86
    assert 6.7950 < secs < 6.8050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "kind_observation" in top))
    assert best == 1
    assert "kind_observation" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_coffee_line(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Can I buy you a coffee? No strings, no pitch - just good conversation with an interesting stranger."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 18
    assert chars == 99
    assert 7.1950 < secs < 7.2050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "coffee_line" in top))
    assert best == 1
    assert "coffee_line" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_bookstore_hello(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Anyone reading that book in public is someone I want to know. What is it about?"
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 16
    assert chars == 79
    assert 6.3950 < secs < 6.4050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "bookstore_hello" in top))
    assert best == 1
    assert "bookstore_hello" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_music_note(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "You have been humming that song for ten minutes and now it is stuck in my head too - in a good way."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 23
    assert chars == 99
    assert 9.1950 < secs < 9.2050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['kind']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "music_note" in top))
    assert best == 1
    assert "music_note" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s opened kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_library_book(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Are you a library book? Because I keep checking you out."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 11
    assert chars == 56
    assert 4.3950 < secs < 4.4050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "library_book" in top))
    assert best == 1
    assert "library_book" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s charmed the stacks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_gatsby_line(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "In my younger and more vulnerable years, my father gave me some advice - go talk to interesting strangers. So here I am."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 23
    assert chars == 120
    assert 9.1950 < secs < 9.2050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "gatsby_line" in top))
    assert best == 1
    assert "gatsby_line" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s charmed the stacks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_plot_twist(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Every good story needs a plot twist. I have a feeling you might be mine."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 15
    assert chars == 72
    assert 5.9950 < secs < 6.0050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "plot_twist" in top))
    assert best == 1
    assert "plot_twist" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s charmed the stacks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_well_read(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "You must read a lot - your eyes have that well-traveled look."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 12
    assert chars == 61
    assert 4.7950 < secs < 4.8050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "well_read" in top))
    assert best == 1
    assert "well_read" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s charmed the stacks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_dogeared_page(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "You are the page I keep coming back to."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 9
    assert chars == 39
    assert 3.5950 < secs < 3.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "dogeared_page" in top))
    assert best == 1
    assert "dogeared_page" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s charmed the stacks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_unfinished_chapter(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "I feel like our story is an unfinished chapter. Want to help me write the next page?"
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 17
    assert chars == 84
    assert 6.7950 < secs < 6.8050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "unfinished_chapter" in top))
    assert best == 1
    assert "unfinished_chapter" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s charmed the stacks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_cute_science(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Are you made of copper and tellurium? Because you are Cu-Te."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 11
    assert chars == 60
    assert 4.3950 < secs < 4.4050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "cute_science" in top))
    assert best == 1
    assert "cute_science" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s ran the experiment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_gravity_line(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "You must be gravity, because I am falling for you."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 10
    assert chars == 50
    assert 3.9950 < secs < 4.0050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "gravity_line" in top))
    assert best == 1
    assert "gravity_line" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s ran the experiment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_photosynthesis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "You must be the sun - everything in my day just started revolving around you."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 15
    assert chars == 77
    assert 5.9950 < secs < 6.0050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "photosynthesis" in top))
    assert best == 1
    assert "photosynthesis" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s ran the experiment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_bunsen_smile(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Is your smile a Bunsen burner? Because it is burning with the steadiest blue flame I have ever seen."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 19
    assert chars == 100
    assert 7.5950 < secs < 7.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "bunsen_smile" in top))
    assert best == 1
    assert "bunsen_smile" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s ran the experiment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_noble_gas(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "You must be a noble gas, because you complete me - no reaction required."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 14
    assert chars == 72
    assert 5.5950 < secs < 5.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "noble_gas" in top))
    assert best == 1
    assert "noble_gas" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s ran the experiment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_hypothesis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "My hypothesis: this conversation will be the best part of my day. Care to help me test it?"
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 18
    assert chars == 90
    assert 7.1950 < secs < 7.2050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "hypothesis" in top))
    assert best == 1
    assert "hypothesis" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s ran the experiment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_dictionary_def(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "I looked up captivating in the dictionary, and it just said your name."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 13
    assert chars == 70
    assert 5.1950 < secs < 5.2050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "dictionary_def" in top))
    assert best == 1
    assert "dictionary_def" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_star_chart(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "If every star is a wish, you must be the whole constellation I wished on."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 15
    assert chars == 73
    assert 5.9950 < secs < 6.0050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "star_chart" in top))
    assert best == 1
    assert "star_chart" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_periodic_serenade(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Roses are red, violets are blue, you are my favorite element, and I have the data to prove it."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 19
    assert chars == 94
    assert 7.5950 < secs < 7.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "periodic_serenade" in top))
    assert best == 1
    assert "periodic_serenade" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_algorithm_us(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "If I wrote an algorithm for the perfect evening, every path would lead to you."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 15
    assert chars == 78
    assert 5.9950 < secs < 6.0050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "algorithm_us" in top))
    assert best == 1
    assert "algorithm_us" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_constellation_map(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Astronomers map constellations by connecting bright points. I just found my brightest one."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 13
    assert chars == 90
    assert 5.1950 < secs < 5.2050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "constellation_map" in top))
    assert best == 1
    assert "constellation_map" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_time_traveler(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "I am not a time traveler, but I can see us laughing about this moment a year from now."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 19
    assert chars == 86
    assert 7.5950 < secs < 7.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "time_traveler" in top))
    assert best == 1
    assert "time_traveler" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_permission_slip(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "I checked with the librarian, and I have official permission to check you out."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 14
    assert chars == 78
    assert 5.5950 < secs < 5.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "permission_slip" in top))
    assert best == 1
    assert "permission_slip" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_chemistry_eq(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "You plus me - I ran the numbers, and it is the most balanced equation I have ever seen."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 19
    assert chars == 87
    assert 7.5950 < secs < 7.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "chemistry_eq" in top))
    assert best == 1
    assert "chemistry_eq" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_odyssey_opener(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "It took Odysseus ten years to get home. It took me one look to know I wanted to talk to you."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 21
    assert chars == 92
    assert 8.3950 < secs < 8.4050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "odyssey_opener" in top))
    assert best == 1
    assert "odyssey_opener" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_astronomers_wish(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "I wished on every star last night, and this morning you were standing here."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 14
    assert chars == 75
    assert 5.5950 < secs < 5.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "astronomers_wish" in top))
    assert best == 1
    assert "astronomers_wish" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_poets_proof(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Poets say the eyes are windows. Yours just showed me a view I never want to leave."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 17
    assert chars == 82
    assert 6.7950 < secs < 6.8050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['bookish']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "poets_proof" in top))
    assert best == 1
    assert "poets_proof" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_kindness_theorem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LINE = "Theorem: kindness is the most attractive quality in the universe. Proof: you, standing here."
    print("line: %s" % LINE)
    words = len(LINE.split())
    chars = len(LINE)
    secs = words / 150.0 * 60.0
    print("words: %d  chars: %d  delivery: %.3f s at 150 wpm" % (words, chars, secs))
    assert words == 14
    assert chars == 92
    assert 5.5950 < secs < 5.6050
    day = "2026-10-17"
    idx = int(hashlib.sha256((day + "|pickup-lines").encode()).hexdigest(), 16) % len(ROSTER)
    pick = ROSTER[idx]
    print("line of the day %s -> #%d %s" % (day, idx, pick["name"]))
    assert idx == 5
    assert pick["key"] == "bright_smile"
    ctx = ['science']
    scores = {r["key"]: len(set(r["tags"]) & set(ctx)) for r in ROSTER}
    best = max(scores.values())
    top = sorted(k for k, v in scores.items() if v == best)
    print("context %s -> best score %d shared by %d line(s); this line in top: %s" % (ctx, best, len(top), "kindness_theorem" in top))
    assert best == 1
    assert "kindness_theorem" in top
    print("rule: clean, kind, respectful - clever opens, kindness keeps")
    print("OK: %s landed the line" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "simple_hello": demo_pk_simple_hello,
    "genuine_compliment": demo_pk_genuine_compliment,
    "shared_moment": demo_pk_shared_moment,
    "helpful_question": demo_pk_helpful_question,
    "honest_intro": demo_pk_honest_intro,
    "bright_smile": demo_pk_bright_smile,
    "kind_observation": demo_pk_kind_observation,
    "coffee_line": demo_pk_coffee_line,
    "bookstore_hello": demo_pk_bookstore_hello,
    "music_note": demo_pk_music_note,
    "library_book": demo_pk_library_book,
    "gatsby_line": demo_pk_gatsby_line,
    "plot_twist": demo_pk_plot_twist,
    "well_read": demo_pk_well_read,
    "dogeared_page": demo_pk_dogeared_page,
    "unfinished_chapter": demo_pk_unfinished_chapter,
    "cute_science": demo_pk_cute_science,
    "gravity_line": demo_pk_gravity_line,
    "photosynthesis": demo_pk_photosynthesis,
    "bunsen_smile": demo_pk_bunsen_smile,
    "noble_gas": demo_pk_noble_gas,
    "hypothesis": demo_pk_hypothesis,
    "dictionary_def": demo_pk_dictionary_def,
    "star_chart": demo_pk_star_chart,
    "periodic_serenade": demo_pk_periodic_serenade,
    "algorithm_us": demo_pk_algorithm_us,
    "constellation_map": demo_pk_constellation_map,
    "time_traveler": demo_pk_time_traveler,
    "permission_slip": demo_pk_permission_slip,
    "chemistry_eq": demo_pk_chemistry_eq,
    "odyssey_opener": demo_pk_odyssey_opener,
    "astronomers_wish": demo_pk_astronomers_wish,
    "poets_proof": demo_pk_poets_proof,
    "kindness_theorem": demo_pk_kindness_theorem,
}
