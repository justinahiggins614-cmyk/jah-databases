#!/usr/bin/env python3
"""Demo programs for the Compliments databases.

Every demo is real, runnable, stdlib-only Python performing the actual
compliment-craft computation for its record: the compliment-of-the-day
picker, the occasion matcher, sincerity scorers, recognition-gap
arithmetic, tribute word budgets, legacy trees, and ripple estimates.
All are machine-executed by build.py before the pages are written: each
prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Demo scenarios mirror
their entries; entry text is cross-checked against demo outputs.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cmpl_thank_you(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sincerity scorer: concrete-detail words over total words
    note = ("thank you for staying late Tuesday to fix the report in the "
            "rain you gave me a ride home and I walked into the meeting "
            "calm instead of scrambling over the deadline I am genuinely "
            "grateful for the extra hour at midnight")
    words = note.split()
    specifics = {"tuesday", "rain", "ride", "home", "report", "midnight",
                 "extra", "hour", "deadline", "calm", "meeting", "late"}
    hits = sum(1 for w in words if w.strip(",.") in specifics)
    score = hits / len(words) * 100.0
    print("words: %d, concrete details: %d" % (len(words), hits))
    print("specificity score: %.2f %%" % score)
    assert len(words) == 42
    assert hits == 11
    assert 26.1 < score < 26.2
    verdict = "SINCERE" if score >= 15.0 else "VAGUE"
    print("verdict: %s (threshold 15 %%)" % verdict)
    assert verdict == "SINCERE"
    print("OK: %s scored the thank-you" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_small_efforts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # daily scan: small efforts logged across a week, noticed or missed
    efforts = [("mon", "wiped counters", True), ("mon", "took bins out", True),
               ("tue", "answered email midnight", True), ("tue", "made tea", False),
               ("wed", "fixed squeaky door", True), ("thu", "extra practice", True),
               ("thu", "watered plants", True), ("fri", "ironed shirts", False),
               ("sat", "drove grandma", True), ("sat", "cleaned porch", True),
               ("sun", "prepped lunches", True)]
    total = len(efforts)
    noticed = sum(1 for _, _, n in efforts if n)
    coverage = noticed / total * 100.0
    print("efforts logged: %d, noticed: %d" % (total, noticed))
    print("recognition coverage: %.2f %%" % coverage)
    assert total == 11
    assert noticed == 9
    assert 81.8 < coverage < 81.82
    missed = [d for _, d, n in efforts if not n]
    print("missed (name next time): %s" % ", ".join(missed))
    print("OK: %s ran the daily scan" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_kind(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kindness ledger: weighted kind acts over two weeks
    acts = [3, 2, 4, 1, 5, 2, 3, 4, 2, 1, 5, 3, 2, 4]
    total = sum(acts)
    weeks = 2
    per_week = total / weeks
    print("kind acts: %d, kindness points: %d" % (len(acts), total))
    print("points per week: %.2f" % per_week)
    assert len(acts) == 14
    assert total == 41
    assert 20.49 < per_week < 20.51
    biggest = max(acts)
    print("most generous single act weight: %d" % biggest)
    assert biggest == 5
    print("OK: %s balanced the kindness ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_name(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # name-use counter: how often the greeting names the person
    transcript = ["Morning, Marcus, how was the weekend?",
                  "Good thanks, and you?",
                  "Busy but good, Marcus. Did the report land?",
                  "It did, sent it last night.",
                  "Appreciate it, Marcus.",
                  "No problem at all.",
                  "Hey Marcus, coffee later?",
                  "Sure, sounds good.",
                  "Great, see you at three, Marcus.",
                  "See you then.",
                  "Marcus, one more thing - the client called.",
                  "Oh? What did they say?",
                  "They loved the draft, Marcus.",
                  "That is a relief.",
                  "You earned it.",
                  "Thanks, Marcus, that means a lot.",
                  "Anytime.",
                  "Alright, back to it, Marcus.",
                  "Back to it.",
                  "Talk soon, Marcus."]
    uses = sum(1 for s in transcript if "Marcus" in s)
    pct = uses / len(transcript) * 100.0
    print("exchanges: %d, name uses: %d" % (len(transcript), uses))
    print("recognition rate: %.1f %%" % pct)
    assert len(transcript) == 20
    assert uses == 10
    assert 49.9 < pct < 50.1
    print("OK: %s counted the name-greetings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_punctuality(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # punctuality record: minutes early (+) across ten arrivals
    arrivals = [5, 3, 7, 0, 4, 6, 2, 8, 1, 5]
    on_time = sum(1 for a in arrivals if a >= 0)
    streak = on_time  # all on time: streak equals the run
    avg_early = sum(arrivals) / len(arrivals)
    print("arrivals: %d, on time: %d" % (len(arrivals), on_time))
    print("on-time streak: %d" % streak)
    print("average minutes early: %.2f" % avg_early)
    assert on_time == 10
    assert streak == 10
    assert 4.09 < avg_early < 4.11
    print("pattern verdict: RELIABLE")
    print("OK: %s read the punctuality record" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_question(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # question-quality rater: specificity + open-endedness + relevance
    q = "how did the timing assumption break when the client load doubled"
    specific_nouns = {"timing", "assumption", "client", "load"}
    found = sum(1 for n in specific_nouns if n in q)
    spec_pts = 3 if found >= 4 else found
    open_pts = 3 if q.split()[0] in {"how", "why", "what"} else 0
    rel_pts = 2 if "client" in q and "load" in q else 0
    score = spec_pts + open_pts + rel_pts
    print("question: %s" % q)
    print("specificity %d/3 + open-ended %d/3 + relevance %d/2" % (spec_pts, open_pts, rel_pts))
    print("quality score: %d/10" % score)
    assert found == 4
    assert score == 8
    print("OK: %s rated the question" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_progress(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # in-progress acknowledgment: milestones across 120 tasks
    total_tasks = 120
    done = 67
    progress = done / total_tasks * 100.0
    milestones = [30, 60, 90, 120]
    next_m = min(m for m in milestones if m > done)
    remaining = next_m - done
    print("tasks done: %d/%d" % (done, total_tasks))
    print("progress: %.2f %%" % progress)
    print("next praise milestone: %d (remaining %d)" % (next_m, remaining))
    assert 55.8 < progress < 55.9
    assert next_m == 90
    assert remaining == 23
    print("OK: %s honored the work in progress" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_calm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # calm-under-pressure analyzer: calm markers in a crisis exchange
    lines = ["server is down", "client is watching", "stay with me, we have a plan",
             "checking logs now", "do not panic, one step at a time",
             "found it, bad deploy", "rolling back calmly",
             "rollback started", "breathe, almost there",
             "service restoring", "steady, verify first",
             "verified, all green", "well handled everyone", "thank you"]
    calm_words = {"stay", "plan", "calmly", "breathe", "steady", "verify",
                  "do not panic", "one step"}
    calm = sum(1 for l in lines for w in calm_words if w in l)
    ratio = calm / len(lines) * 100.0
    print("exchange lines: %d, calm markers: %d" % (len(lines), calm))
    print("steadiness ratio: %.2f %%" % ratio)
    assert len(lines) == 14
    assert calm == 8
    assert 57.1 < ratio < 57.2
    print("OK: %s measured the calm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_public_thanks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # public thanks reach: audience times sincerity multiplier
    audience = 40
    sincerity = 0.9
    reach = audience * sincerity
    impact = reach * 2.5  # witnesses carry it onward
    print("audience: %d, sincerity: %.1f" % (audience, sincerity))
    print("recognition reach: %.1f" % reach)
    print("estimated impact: %.1f" % impact)
    assert 35.9 < reach < 36.1
    assert 89.9 < impact < 90.1
    print("OK: %s projected the public thanks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_consistency(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # consistency streaks over a 30-day log
    log = [1]*12 + [0] + [1]*8 + [0] + [1]*5 + [0]*3
    assert len(log) == 30
    longest, cur = 0, 0
    for d in log:
        cur = cur + 1 if d else 0
        longest = max(longest, cur)
    rate = sum(log) / len(log) * 100.0
    print("days logged: %d, kept: %d" % (len(log), sum(log)))
    print("longest streak: %d days" % longest)
    print("consistency rate: %.1f %%" % rate)
    assert longest == 12
    assert 83.3 < rate < 83.4
    print("OK: %s traced the consistency" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_listening(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # listening markers: reflective phrases across 24 dialogue turns
    turns = ["it sounds like the deadline crushed you",
             "yeah, completely",
             "what I hear is you need backup",
             "exactly",
             "so the real issue is the handoff",
             "right",
             "tell me more about Tuesday",
             "it was chaos",
             "sounds like chaos with no support",
             "that is it",
             "ok",
             "hmm",
             "what helped last time",
             "the checklist",
             "so a checklist would steady this",
             "yes",
             "noted",
             "right",
             "anything else weighing on you",
             "the client call",
             "the call felt unfair, is that right",
             "very",
             "I hear you",
             "thanks"]
    starters = ("it sounds like", "what i hear", "so ", "tell me more",
                "sounds like", "what helped", "anything else", "is that right",
                "i hear you")
    reflective = sum(1 for t in turns if t.lower().startswith(starters))
    pct = reflective / len(turns) * 100.0
    print("dialogue turns: %d, reflective: %d" % (len(turns), reflective))
    print("listening rate: %.1f %%" % pct)
    assert len(turns) == 24
    assert reflective == 9
    assert 37.4 < pct < 37.6
    print("OK: %s heard the listening" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_time(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # time-gift ledger: minutes given across five gifts of time
    gifts = [("tue call", 45), ("thu review", 30), ("sat drive", 60),
             ("sun chat", 20), ("mon mentoring", 90)]
    total_min = sum(m for _, m in gifts)
    hours = total_min / 60.0
    print("gifts of time: %d" % len(gifts))
    for label, m in gifts:
        print("  %-14s %3d min" % (label, m))
    print("total: %d minutes (%.2f hours)" % (total_min, hours))
    assert total_min == 245
    assert 4.08 < hours < 4.09
    print("OK: %s totaled the time given" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_craft(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # craftsmanship: defects per thousand before and after the standard held
    before, after = 34, 6
    improvement = (before - after) / before * 100.0
    print("defects per 1000 before: %d, after: %d" % (before, after))
    print("improvement: %.2f %%" % improvement)
    assert 82.35 < improvement < 82.36
    print("standard verdict: REFUSES TO SHIP ALMOST-RIGHT")
    print("OK: %s inspected the craftsmanship" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_meeting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # well-run meeting: agenda completion and time efficiency
    items, decided, minutes = 8, 8, 45
    completion = decided / items * 100.0
    per_item = minutes / items
    print("agenda items: %d, decided: %d" % (items, decided))
    print("completion: %.0f %%" % completion)
    print("minutes per item: %.3f" % per_item)
    assert completion == 100.0
    assert 5.62 < per_item < 5.63
    print("OK: %s clocked the well-run meeting" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_courage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # everyday courage inventory: acts weighted by stakes
    acts = [("spoke up in meeting", 3, 3), ("started over at forty", 1, 4),
            ("told the hard truth", 2, 5), ("walked into the new room", 2, 2)]
    total = sum(n * w for _, n, w in acts)
    count = sum(n for _, n, _ in acts)
    print("brave acts: %d across %d kinds" % (count, len(acts)))
    for label, n, w in acts:
        print("  %-24s %d x weight %d = %d" % (label, n, w, n * w))
    print("courage score: %d" % total)
    assert count == 8
    assert total == 27
    print("OK: %s inventoried the courage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # clarity scorer: Flesch reading ease on a sample sentence
    text = "The quick brown fox jumps over the lazy dog near the river bank."
    words = text.replace(".", "").split()
    vowels = set("aeiouy")

    def syllables(w):
        w = w.lower()
        n, prev = 0, False
        for ch in w:
            v = ch in vowels
            if v and not prev:
                n += 1
            prev = v
        if w.endswith("e"):
            n -= 1
        return max(1, n)

    syl = sum(syllables(w) for w in words)
    sentences = 1
    ease = 206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syl / len(words))
    print("words: %d, syllables: %d" % (len(words), syl))
    print("Flesch reading ease: %.2f" % ease)
    assert len(words) == 13
    assert syl == 16
    assert 89.5 < ease < 89.6
    print("verdict: PLAIN AND CLEAR")
    print("OK: %s scored the clarity" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_patience(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # patience log: trying waits endured without a flicker
    waits = [("support hold", 12), ("traffic jam", 8), ("delayed flight", 25),
             ("slow checkout", 5)]
    total = sum(m for _, m in waits)
    print("trying waits: %d" % len(waits))
    for label, m in waits:
        print("  %-14s %2d min, calm throughout" % (label, m))
    print("total patience: %d minutes" % total)
    assert total == 50
    assert len(waits) == 4
    print("OK: %s logged the patience" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_appearance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tastefulness checker: choice-words pass, body-words fail
    red_flags = {"figure", "body", "weight", "sexy", "tight", "thighs",
                 "chest", "curves", "skinny", "fat"}
    drafts = [("That jacket is a great color on you.", "PASS"),
              ("You look great in that tight dress, it shows your figure.", "FAIL")]
    for text, expected in drafts:
        lowered = text.lower()
        hits = sorted(w for w in red_flags if w in lowered)
        verdict = "FAIL" if hits else "PASS"
        print("draft: %s" % text)
        print("  flags: %s -> %s" % (hits if hits else "none", verdict))
        assert verdict == expected, text
    print("rule: compliment the choice, never the body")
    print("OK: %s ran the tastefulness check" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_mentor(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mentor impact: mentees times years times sessions per year
    mentees, years, sessions_per_year = 6, 3, 12
    sessions = mentees * years * sessions_per_year
    impact = sessions * 1.5
    print("mentees: %d, years each: %d, sessions/year: %d" % (mentees, years, sessions_per_year))
    print("guidance sessions: %d" % sessions)
    print("impact score: %.0f" % impact)
    assert sessions == 216
    assert impact == 324.0
    print("OK: %s measured the mentorship" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_integrity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # integrity ledger: promises kept over promises made
    made, kept = 48, 46
    ratio = kept / made * 100.0
    print("promises made: %d, kept: %d" % (made, kept))
    print("integrity ratio: %.2f %%" % ratio)
    assert 95.83 < ratio < 95.84
    print("verdict: THE HARD RIGHT THING, REPEATEDLY")
    print("OK: %s balanced the integrity ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_unseen(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # visibility map: seen versus unseen tasks behind one smooth event
    tasks = ["room set", "materials ready", "follow-ups sent", "sound check",
             "chairs arranged", "signage hung", "catering confirmed",
             "backup slides", "name tags", "cleanup crew",
             "transport booked", "rehearsal run", "lighting tuned",
             "program printed", "usher briefed", "parking arranged",
             "first aid kit", "wifi tested", "timeline synced", "thank-yous drafted"]
    seen = {"room set", "materials ready", "signage hung", "catering confirmed",
            "name tags", "program printed"}
    unseen = [t for t in tasks if t not in seen]
    visibility = len(seen) / len(tasks) * 100.0
    print("tasks: %d, seen: %d, unseen: %d" % (len(tasks), len(seen), len(unseen)))
    print("visibility: %.1f %%" % visibility)
    assert len(unseen) == 14
    assert 29.9 < visibility < 30.1
    print("recognition gap: %d tasks" % len(unseen))
    print("OK: %s mapped the unseen work" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # problem-solving path: nine steps from stuck to solved
    steps = ["reproduce", "narrow", "isolate timing", "hypothesize",
             "test one variable", "confirm", "fix", "regression-test", "document"]
    hours = 3.5
    rate = len(steps) / hours
    print("steps from stuck to solved: %d" % len(steps))
    print("hours: %.1f, steps per hour: %.3f" % (hours, rate))
    assert len(steps) == 9
    assert 2.57 < rate < 2.58
    print("method honored: isolate, test, confirm")
    print("OK: %s traced the solution path" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_humor(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # humor lift meter: room mood before and after the well-timed joke
    before, after = 4.2, 7.8
    lift = after - before
    print("room mood before: %.1f/10, after: %.1f/10" % (before, after))
    print("lift: %.2f points" % lift)
    assert 3.59 < lift < 3.61
    print("verdict: TENSION BROKEN, THINKING RESTORED")
    print("OK: %s measured the lift" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_comeback(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # comeback timeline: setback to recovery, lessons counted
    setback_day, recovery_day = 0, 47
    lessons = ["owned it same day", "fixed the root cause", "told the team plainly",
               "built the checklist", "helped the next person avoid it"]
    days = recovery_day - setback_day
    rate = len(lessons) / days
    print("days from setback to recovery: %d" % days)
    print("lessons banked: %d" % len(lessons))
    print("lessons per day: %.4f" % rate)
    assert days == 47
    assert len(lessons) == 5
    assert 0.106 < rate < 0.107
    print("OK: %s charted the comeback" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_character(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # whole-character profile: virtue tallies across twenty years
    virtues = {"honesty": 9, "generosity": 7, "steadiness": 8,
               "courage": 6, "kindness": 8}
    total = sum(virtues.values())
    print("virtues witnessed:")
    for v, n in virtues.items():
        print("  %-10s %d" % (v, n))
    print("character weight: %d" % total)
    assert total == 38
    assert min(virtues.values()) >= 6
    print("OK: %s weighed the character" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_lifetime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lifetime achievement arc: milestones by decade
    decades = {"20s": 3, "30s": 7, "40s": 9, "50s": 6, "60s": 4}
    total = sum(decades.values())
    peak = max(decades, key=decades.get)
    print("milestones by decade:")
    for d, n in decades.items():
        print("  %s: %d" % (d, n))
    print("lifetime milestones: %d (peak decade %s)" % (total, peak))
    assert total == 29
    assert peak == "40s"
    print("OK: %s walked the lifetime arc" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_moral(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # moral courage ledger: stands weighted by true cost
    stands = [("spoke against the plan", 9, 3), ("returned the overpayment", 7, 2),
              ("blew the whistle", 10, 4), ("defended the new hire", 6, 2)]
    total = sum(s * w for _, s, w in stands)
    print("stands taken: %d" % len(stands))
    for label, stakes, weight in stands:
        print("  %-26s stakes %2d x %d = %d" % (label, stakes, weight, stakes * weight))
    print("moral courage score: %d" % total)
    assert total == 93
    print("OK: %s weighed the moral courage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_lifework(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # life's work: output across the decades of showing up
    works, years = 120, 35
    per_year = works / years
    print("works: %d, years: %d" % (works, years))
    print("works per year: %.4f" % per_year)
    assert 3.42 < per_year < 3.43
    print("verdict: FORTY YEARS OF SHOWING UP, HONORED")
    print("OK: %s surveyed the life's work" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_tribute(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # living tribute word budget: celebration, not farewell
    sections = [("opening", 150), ("stories", 400), ("qualities", 250),
                ("closing", 200)]
    total = sum(w for _, w in sections)
    stories_share = 400 / total * 100.0
    print("tribute word budget:")
    for label, w in sections:
        print("  %-9s %d words" % (label, w))
    print("total: %d words" % total)
    print("stories share: %.0f %%" % stories_share)
    assert total == 1000
    assert stories_share == 40.0
    print("OK: %s budgeted the living tribute" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_legacy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mentor legacy tree: generations of influence
    generations = [1, 4, 11, 23]
    total = sum(generations)
    depth = len(generations)
    print("legacy tree by generation: %s" % generations)
    print("generations deep: %d" % depth)
    print("lives touched: %d" % total)
    assert depth == 4
    assert total == 39
    print("OK: %s mapped the legacy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_grace(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grace journal: hardships met with grace markers
    hardships = ["loss", "illness", "reversal", "betrayal", "waiting", "goodbye"]
    grace = [3, 4, 2, 5, 3, 4]
    total = sum(grace)
    avg = total / len(hardships)
    print("hardships carried: %d" % len(hardships))
    print("grace markers: %d (average %.1f per hardship)" % (total, avg))
    assert total == 21
    assert 3.49 < avg < 3.51
    print("OK: %s kept the grace journal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_unsung(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # unsung hero finder: contribution minus recognition equals the gap
    people = [("the aide", 95, 20), ("the volunteer", 80, 60),
              ("the fixer", 70, 10), ("the organizer", 88, 45),
              ("the driver", 60, 55)]
    gaps = [(label, c - r) for label, c, r in people]
    hero, gap = max(gaps, key=lambda p: p[1])
    print("recognition gaps:")
    for label, g in gaps:
        print("  %-13s gap %d" % (label, g))
    print("largest gap: %s (%d)" % (hero, gap))
    assert gap == 75
    assert hero == "the aide"
    print("OK: %s found the unsung hero" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_forgive(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # forgiveness ledger: grievances released, none in cold storage
    grievances, released = 9, 7
    freedom = released / grievances * 100.0
    held = grievances - released
    print("grievances: %d, released: %d, still held: %d" % (grievances, released, held))
    print("freedom score: %.2f %%" % freedom)
    assert held == 2
    assert 77.7 < freedom < 77.8
    print("OK: %s closed the forgiveness ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmpl_lifechange(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # life-change ripple: one true compliment branching outward
    # compliment-of-the-day picker: deterministic choice by day-of-year
    import datetime
    compliments = ["You have a real gift for this - do it properly.",
                   "Your voice deserves to be heard.",
                   "You would be a great teacher.",
                   "The way you kept going mattered."]
    day = 290  # fixed day for a reproducible pick
    pick = compliments[day % len(compliments)]
    generations = [1, 3, 6, 12]  # told 3, each told 2, each told 2
    touched = sum(generations)
    print("compliment of the day: %s" % pick)
    print("ripple generations: %s" % generations)
    print("lives touched: %d" % touched)
    assert pick == compliments[2]
    assert touched == 22
    print("OK: %s traced the life-changing ripple" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "thank_you": demo_cmpl_thank_you,
    "small_efforts": demo_cmpl_small_efforts,
    "you_are_kind": demo_cmpl_kind,
    "hello_by_name": demo_cmpl_name,
    "punctuality": demo_cmpl_punctuality,
    "good_question": demo_cmpl_question,
    "work_in_progress": demo_cmpl_progress,
    "calm_under_pressure": demo_cmpl_calm,
    "thank_publicly": demo_cmpl_public_thanks,
    "consistency": demo_cmpl_consistency,
    "listening": demo_cmpl_listening,
    "time_gift": demo_cmpl_time,
    "craftsmanship": demo_cmpl_craft,
    "well_run_meeting": demo_cmpl_meeting,
    "courage": demo_cmpl_courage,
    "clear_writing": demo_cmpl_writing,
    "patience": demo_cmpl_patience,
    "tasteful_appearance": demo_cmpl_appearance,
    "mentorship": demo_cmpl_mentor,
    "integrity": demo_cmpl_integrity,
    "unseen_work": demo_cmpl_unseen,
    "problem_solving": demo_cmpl_problem,
    "humor": demo_cmpl_humor,
    "comeback": demo_cmpl_comeback,
    "whole_character": demo_cmpl_character,
    "lifetime_achievement": demo_cmpl_lifetime,
    "moral_courage": demo_cmpl_moral,
    "lifes_work": demo_cmpl_lifework,
    "living_tribute": demo_cmpl_tribute,
    "mentor_legacy": demo_cmpl_legacy,
    "grace_hard_times": demo_cmpl_grace,
    "unsung_hero": demo_cmpl_unsung,
    "forgiveness": demo_cmpl_forgive,
    "life_changing": demo_cmpl_lifechange,
}
