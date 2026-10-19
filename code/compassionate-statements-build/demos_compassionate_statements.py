#!/usr/bin/env python3
"""Demo programs for the Compassionate Statements databases.

Every demo is real, runnable, stdlib-only Python performing an actual
comfort-craft computation for its record: statement pickers, situation
matchers, minimizing-language scanners, warmth/specificity/continuity
metrics, follow-up cadence models, readability scoring. All are
machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker.

Each demo analyzes its own record's statement text verbatim (the
__STMT__ placeholder), so entry text and demo outputs are cross-checked
by build.py.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body, stmt):
    return (hdr_fn(name, rid, group) + _PREAMBLE
            + body.replace("__STMT__", __import__("json").dumps(stmt))
                  .replace("NAME", __import__("json").dumps(name)))


def demo_simple_presence(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # statement picker: score 3 candidate openers for a shock situation
    candidates = {
        "presence": "I am here with you. You do not have to go through this alone.",
        "fixing": "Do not worry, everything will work out fine, just stay positive.",
        "absent": "Let me know if you need anything sometime.",
    }
    minimizing = ["just", "everything will work out", "stay positive", "let me know if"]
    def score(s):
        low = s.lower()
        hits = sum(1 for p in minimizing if p in low)
        presence = sum(1 for w in ["here", "with you", "alone"] if w in low)
        return presence * 10 - hits * 25 + len(s.split())
    scores = {k: score(v) for k, v in candidates.items()}
    for k in sorted(scores):
        print("  %-9s score %d" % (k, scores[k]))
    best = max(scores, key=scores.get)
    print("picker recommends: %s" % best)
    assert best == "presence"
    assert scores["presence"] == 44
    assert scores["fixing"] == -64
    assert scores["absent"] == -17
    words = __STMT__.split()
    print("record statement words: %d" % len(words))
    assert len(words) == 14
    print("OK: %s picked presence over platitude" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_naming_what_you_see(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # specificity scorer: concrete observation words in the statement
    stmt = __STMT__
    concrete = ["looks", "hard", "see", "weight", "carrying"]
    low = stmt.lower()
    hits = [w for w in concrete if w in low]
    words = stmt.split()
    print("concrete observation words: %d (%s)" % (len(hits), ", ".join(hits)))
    assert len(hits) == 5
    spec = len(hits) / len(words) * 100.0
    print("specificity: %.2f %%" % spec)
    assert 38.46 < spec < 38.47
    assert len(words) == 13
    print("OK: %s named the weight plainly" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_permission_to_feel(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # minimizing-language scanner: the statement must contain zero
    stmt = __STMT__
    minimizing = ["at least", "just ", "get over", "move on",
                  "everything happens", "be strong", "calm down",
                  "you should", "stop crying", "too sensitive"]
    low = " " + stmt.lower() + " "
    hits = [p for p in minimizing if p in low]
    print("minimizing phrases found: %d" % len(hits))
    assert len(hits) == 0
    affirm = sum(1 for w in ["okay", "no wrong", "feel"] if w in low)
    print("permission words present: %d" % affirm)
    assert affirm == 3
    print("OK: %s granted permission with zero minimizing" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_honest_admission(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # honesty/commitment pairing check: both halves must be present
    low = __STMT__.lower()
    admission = 1 if "i do not know what to say" in low else 0
    commitment = 1 if "not going anywhere" in low else 0
    print("honesty admission: %d, staying commitment: %d" % (admission, commitment))
    assert admission == 1 and commitment == 1
    assert commitment - admission == 0
    print("pairing complete: honesty about words, certainty about presence")
    print("OK: %s admitted and stayed" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_listening_first(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # other-focus metric: the sentence should center them, not the speaker
    words = __STMT__.lower().split()
    you_n = words.count("you")
    me_n = words.count("me")
    i_n = words.count("i")
    print("you: %d, me: %d, i: %d (total %d words)" % (you_n, me_n, i_n, len(words)))
    assert you_n == 1 and me_n == 1 and i_n == 1
    focus = (you_n + me_n) / len(words) * 100.0
    print("other-focus words: %.2f %%" % focus)
    assert 15.38 < focus < 15.39
    assert you_n >= i_n
    print("OK: %s centered the teller" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_hard_day(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # proportion check: short statement, 2 sentences, plain sympathy
    stmt = __STMT__
    words = stmt.split()
    sentences = [s for s in stmt.split(". ") if s]
    print("words: %d, sentences: %d" % (len(words), len(sentences)))
    assert len(words) == 16
    assert len(sentences) == 2
    avg = len(words) / len(sentences)
    print("avg words per sentence: %.1f" % avg)
    assert 7.99 < avg < 8.01
    warm = sum(1 for w in ["sorry"] if w in stmt.lower())
    print("warmth words: %d" % warm)
    assert warm == 1
    print("OK: %s met the day at its size" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_honoring_effort(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # witness/validation density: effort must be specifically named
    low = __STMT__.lower()
    words = __STMT__.split()
    witness = sum(1 for w in ["saw"] if w in low)
    effort = sum(1 for w in ["hard", "worked", "effort"] if w in low)
    print("witness verbs: %d, effort nouns: %d" % (witness, effort))
    assert witness == 1 and effort == 3
    density = (witness + effort) / len(words) * 100.0
    print("validation density: %.2f %%" % density)
    assert 30.76 < density < 30.78
    print("OK: %s honored the work" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_disappointment(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # validation density: the hope and the hurt both named
    low = __STMT__.lower()
    words = __STMT__.split()
    valid = sum(1 for w in ["sense", "hurts", "hoped", "real"] if w in low)
    print("validation words: %d of %d" % (valid, len(words)))
    assert valid == 4 and len(words) == 11
    v = valid / len(words) * 100.0
    print("validation density: %.2f %%" % v)
    assert 36.36 < v < 36.37
    print("OK: %s legitimized the hurt" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_visiting_sick(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pressure scan: a sick visit must demand nothing of the patient
    stmt = __STMT__
    pressure = ["you should", "at least", "cheer up", "stay positive",
                "get well soon", "how are you feeling"]
    low = stmt.lower()
    hits = [p for p in pressure if p in low]
    print("pressure phrases found: %d" % len(hits))
    assert len(hits) == 0
    permission = sum(1 for w in ["no need", "unless you want"] if w in low)
    print("permission phrases: %d" % permission)
    assert permission == 2
    assert len(stmt.split()) == 17
    print("OK: %s asked nothing of the patient" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_after_mistake(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # continuity metric + shame-language scan
    low = __STMT__.lower()
    words = __STMT__.split()
    continuity = sum(1 for w in ["still", "here", "same", "before"] if w in low)
    print("continuity words: %d of %d" % (continuity, len(words)))
    assert continuity == 4 and len(words) == 15
    c = continuity / len(words) * 100.0
    print("continuity density: %.2f %%" % c)
    assert 26.66 < c < 26.68
    shame = ["ashamed", "disappointed in you", "unforgivable", "i told you so"]
    hits = [p for p in shame if p in low]
    print("shame phrases found: %d" % len(hits))
    assert len(hits) == 0
    print("OK: %s separated act from identity" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_fear(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pacing check: short sentences shrink the horizon
    stmt = __STMT__
    words = stmt.split()
    sentences = [s for s in stmt.split(". ") if s]
    avg = len(words) / len(sentences)
    print("words: %d, sentences: %d, avg: %.1f" % (len(words), len(sentences), avg))
    assert len(words) == 15 and len(sentences) == 2
    assert 7.49 < avg < 7.51
    plan = sum(1 for w in ["step"] if w in stmt.lower())
    print("next-step words: %d" % plan)
    assert plan == 1
    plural = 1 if " we " in " " + stmt.lower() + " " else 0
    print("'we' present (company for the steps): %d" % plural)
    assert plural == 1
    print("OK: %s shrank the horizon" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_exhaustion(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reframe ratio: repair language must outweigh quitting language
    low = __STMT__.lower()
    repair = sum(1 for w in ["rest", "repair"] if w in low)
    quitw = sum(1 for w in ["quitting"] if w in low)
    print("repair words: %d, quitting words: %d" % (repair, quitw))
    assert repair == 2 and quitw == 1
    ratio = repair / quitw
    print("reframe ratio: %.1f" % ratio)
    assert 1.99 < ratio < 2.01
    assert len(__STMT__.split()) == 13
    print("OK: %s prescribed repair, not surrender" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_pain_no_fix(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # false-promise scan: unfixable pain must carry zero false solutions
    low = __STMT__.lower()
    false_promises = ["i can fix", "will fix", "everything will be",
                      "it will get better", "promise it", "have you tried"]
    hits = [p for p in false_promises if p in low]
    print("false promises found: %d" % len(hits))
    assert len(hits) == 0
    honesty = sum(1 for w in ["cannot fix", "will not pretend"] if w in low)
    presence = sum(1 for w in ["stay with you"] if w in low)
    print("honesty markers: %d, presence markers: %d" % (honesty, presence))
    assert honesty == 2 and presence == 1
    print("OK: %s refused false rescue" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_loneliness(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mattering density: being specifically seen, by a specific person
    low = __STMT__.lower()
    words = __STMT__.split()
    mattering = sum(1 for w in ["matter", "notice", "invisible"] if w in low)
    print("mattering words: %d of %d" % (mattering, len(words)))
    assert mattering == 3 and len(words) == 13
    m = mattering / len(words) * 100.0
    print("mattering density: %.2f %%" % m)
    assert 23.07 < m < 23.09
    first_person = 1 if "i notice you" in low else 0
    print("first-person witness ('I notice you'): %d" % first_person)
    assert first_person == 1
    print("OK: %s made them visible" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_caregiver(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reciprocity balance: giving named, receiving offered, ledger at zero
    low = __STMT__.lower()
    words = __STMT__.split()
    given = low.count("give")
    offered = low.count("for you")
    print("giving named: %d, receiving offered: %d" % (given, offered))
    assert given == 1 and offered == 1
    assert offered - given == 0
    care_n = low.count("care")
    print("'care' appears %d times (given and received)" % care_n)
    assert care_n == 2
    assert len(words) == 17
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_plans_fall_apart(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # future-grief density: the unlived future named as grieve-worthy
    low = __STMT__.lower()
    words = __STMT__.split()
    future = sum(1 for w in ["plans", "hope", "future", "pictured"] if w in low)
    print("future-grief words: %d of %d" % (future, len(words)))
    assert future == 4 and len(words) == 16
    f = future / len(words) * 100.0
    print("future-grief density: %.2f %%" % f)
    assert 24.99 < f < 25.01
    fatalism = sum(1 for p in ["meant to be", "door closes", "move on"] if p in low)
    print("fatalism phrases: %d" % fatalism)
    assert fatalism == 0
    print("OK: %s grieved the pictured future" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_grief_first_hours(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # first-hours protocol model: message budget shrinks as shock deepens
    # recommended words = max(10, 40 - 2 * hours_since_news)
    schedule = [(0, 40), (2, 36), (6, 28), (12, 16)]
    for hours, expect in schedule:
        rec = max(10, 40 - 2 * hours)
        print("  %2d h since news -> budget %d words" % (hours, rec))
        assert rec == expect
    n = len(__STMT__.split())
    print("record statement: %d words (fits the first-hour budget)" % n)
    assert n == 16
    assert n <= 40
    debt = 1 if "do not need to say anything back" in __STMT__.lower() else 0
    print("response-debt cancellation: %d" % debt)
    assert debt == 1
    print("OK: %s kept the first hours brief and kind" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_job_loss(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dignity density: worth and belief named against the verdict
    low = __STMT__.lower()
    words = __STMT__.split()
    dignity = sum(1 for w in ["worth", "believe", "bring"] if w in low)
    print("dignity words: %d of %d" % (dignity, len(words)))
    assert dignity == 3 and len(words) == 14
    d = dignity / len(words) * 100.0
    print("dignity density: %.2f %%" % d)
    assert 21.42 < d < 21.44
    blessing = sum(1 for p in ["blessing in disguise", "meant to be"] if p in low)
    assert blessing == 0
    print("OK: %s filed the dissenting opinion" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_diagnosis(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gravity + accompaniment: face the fear, promise the walk
    low = __STMT__.lower()
    words = __STMT__.split()
    gravity = sum(1 for w in ["frightening", "fear", "valid"] if w in low)
    accompany = sum(1 for w in ["walk", "with you"] if w in low)
    print("gravity words: %d, accompaniment words: %d" % (gravity, accompany))
    assert gravity == 3 and accompany == 2
    assert len(words) == 16
    v = gravity / len(words) * 100.0
    print("gravity density: %.2f %%" % v)
    assert 18.74 < v < 18.76
    reassure = sum(1 for p in ["you will be fine", "beat this"] if p in low)
    print("premature reassurance phrases: %d" % reassure)
    assert reassure == 0
    print("OK: %s faced the gravity and promised the walk" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_separation(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # situation matcher: route a disclosure to the right comfort category
    situations = {
        "separation": ["ending", "divorce", "breakup", "footing", "split"],
        "grief": ["died", "funeral", "burial"],
        "illness": ["diagnosis", "hospital", "treatment"],
    }
    text = "after the divorce she is finding her footing again since the split"
    scores = {}
    for cat, keywords in situations.items():
        scores[cat] = sum(1 for w in keywords if w in text)
    for cat in sorted(scores):
        print("  %-10s match %d" % (cat, scores[cat]))
    best = max(scores, key=scores.get)
    print("matcher routes to: %s" % best)
    assert best == "separation"
    assert scores["separation"] == 3
    assert scores["grief"] == 0 and scores["illness"] == 0
    n = len(__STMT__.split())
    print("record statement words: %d" % n)
    assert n == 14
    print("OK: %s matched the situation" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_grief_returns(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grief wave model: intensity(t) = base + A * e^(-t/tau) * |sin(2*pi*t/365)|
    base, A, tau = 20.0, 60.0, 180.0
    def intensity(t):
        return base + A * math.exp(-t / tau) * abs(math.sin(2 * math.pi * t / 365.0))
    i0 = intensity(0.0)
    i_wave = intensity(91.25)   # quarter-year: the sine peaks
    i_far = intensity(730.0)    # two years: the amplitude decays
    print("day 0:    %.2f" % i0)
    print("day 91:   %.2f (wave returns)" % i_wave)
    print("day 730:  %.2f (amplitude decays)" % i_far)
    assert 19.99 < i0 < 20.01
    assert 56.10 < i_wave < 56.20
    assert i_wave > i0, "waves return - grief comes back"
    assert i_far < i_wave, "but the amplitude decays over years"
    assert 19.99 < i_far < 60.0
    n = len(__STMT__.split())
    print("record statement words: %d" % n)
    assert n == 16
    print("OK: %s modeled the tide, not the staircase" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_child_loss(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # readability: a child's comfort must read easy (high Flesch score)
    def syl(w):
        w = w.lower().strip(".,")
        vowels = "aeiouy"
        n = 0
        prev = False
        for ch in w:
            v = ch in vowels
            if v and not prev:
                n += 1
            prev = v
        if w.endswith("e"):
            n -= 1
        return max(1, n)
    stmt = __STMT__
    words = stmt.split()
    sentences = [s for s in stmt.split(". ") if s]
    syllables = sum(syl(w) for w in words)
    flesch = 206.835 - 1.015 * (len(words) / len(sentences)) - 84.6 * (syllables / len(words))
    print("words: %d, sentences: %d, syllables: %d" % (len(words), len(sentences), syllables))
    print("Flesch reading ease: %.1f" % flesch)
    assert len(words) == 20 and len(sentences) == 2
    assert flesch > 90.0, "child comfort must read very easy"
    assert 95.1 < flesch < 95.3
    print("OK: %s spoke at eye level" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_financial(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shame scan + step plan: kill shame first, then sequence the work
    low = __STMT__.lower()
    shame = ["your fault", "irresponsible", "should have", "bad with money"]
    hits = [p for p in shame if p in low]
    print("shame phrases found: %d" % len(hits))
    assert len(hits) == 0
    steps = sum(1 for w in ["together", "one step"] if w in low)
    print("company+sequence words: %d" % steps)
    assert steps == 2
    assert len(__STMT__.split()) == 18
    print("OK: %s de-moralized the ledger" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_chronic_illness(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # continuity density: the promise must span the whole cycle
    low = __STMT__.lower()
    words = __STMT__.split()
    continuity = sum(1 for w in ["keep", "not going anywhere", "good days", "bad ones"] if w in low)
    print("continuity words: %d of %d" % (continuity, len(words)))
    assert continuity == 4 and len(words) == 20
    c = continuity / len(words) * 100.0
    print("continuity density: %.2f %%" % c)
    assert 19.99 < c < 20.01
    cure = sum(1 for p in ["get better", "you will heal"] if p in low)
    print("false recovery promises: %d" % cure)
    assert cure == 0
    print("OK: %s promised the whole cycle" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_anger_grief(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # permission density for the exiled emotion + suppression scan
    low = __STMT__.lower()
    words = __STMT__.split()
    permission = sum(1 for w in ["part of", "do not have to apologize", "here"] if w in low)
    print("permission words: %d of %d" % (permission, len(words)))
    assert permission == 3 and len(words) == 17
    p = permission / len(words) * 100.0
    print("permission density: %.2f %%" % p)
    assert 17.64 < p < 17.66
    suppress = ["calm down", "let it go", "anger issues"]
    hits = [x for x in suppress if x in low]
    print("suppression phrases: %d" % len(hits))
    assert len(hits) == 0
    print("OK: %s granted anger citizenship" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_regret(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fairness density: the past judged with the past's evidence
    low = __STMT__.lower()
    words = __STMT__.split()
    fairness = sum(1 for w in ["best", "knew how", "what you had", "still counts"] if w in low)
    print("fairness words: %d of %d" % (fairness, len(words)))
    assert fairness == 4 and len(words) == 15
    f = fairness / len(words) * 100.0
    print("fairness density: %.2f %%" % f)
    assert 26.66 < f < 26.68
    fatalism = sum(1 for x in ["meant to be", "for a reason"] if x in low)
    assert fatalism == 0
    print("OK: %s demanded a fair trial" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_unworthy(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # unconditional density: kindness with no application process
    low = __STMT__.lower()
    words = __STMT__.split()
    uncond = sum(1 for w in ["do not have to earn", "already yours", "no application"] if w in low)
    print("unconditional words: %d of %d" % (uncond, len(words)))
    assert uncond == 3 and len(words) == 14
    u = uncond / len(words) * 100.0
    print("unconditional density: %.2f %%" % u)
    assert 21.42 < u < 21.44
    ledger = sum(1 for x in ["deserve", "earn it", "pay back"] if x in low)
    print("transactional words: %d" % ledger)
    assert ledger == 0
    print("OK: %s cancelled the application" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_long_goodbye(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # duration density: the vow must name the long road
    low = __STMT__.lower()
    words = __STMT__.split()
    duration = sum(1 for w in ["however long", "keep showing up", "not go through this alone"] if w in low)
    print("duration words: %d of %d" % (duration, len(words)))
    assert duration == 3 and len(words) == 16
    d = duration / len(words) * 100.0
    print("duration density: %.2f %%" % d)
    assert 18.74 < d < 18.76
    print("OK: %s vowed the long road" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_sudden_loss(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shock acknowledgment vs anchor: admit the scale, become steady
    low = __STMT__.lower()
    words = __STMT__.split()
    ack = sum(1 for w in ["no words", "shock"] if w in low)
    anchor = sum(1 for w in ["here", "staying"] if w in low)
    print("acknowledgment: %d, anchor: %d (of %d words)" % (ack, anchor, len(words)))
    assert ack == 2 and anchor == 2 and len(words) == 18
    ratio = anchor / ack
    print("anchor-to-acknowledgment ratio: %.1f" % ratio)
    assert 0.99 < ratio < 1.01
    sense = sum(1 for x in ["at least", "for a reason", "make sense"] if x in low)
    print("sense-making phrases: %d" % sense)
    assert sense == 0
    print("OK: %s became the steady object" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_survivor(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # belief triad: all three sentences present, in order
    low = __STMT__.lower()
    triad = ["i believe you", "not your fault", "on your side"]
    positions = [low.find(t) for t in triad]
    print("triad positions: %s" % positions)
    assert all(p >= 0 for p in positions), "every part of the triad must be present"
    assert positions == sorted(positions), "belief first, absolution second, alliance third"
    assert len(__STMT__.split()) == 15
    blame = ["are you sure", "what were you wearing", "why did you"]
    hits = [x for x in blame if x in low]
    print("blame-shift questions: %d" % len(hits))
    assert len(hits) == 0
    print("OK: %s believed first" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_parent_child_loss(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # permanence density: love inscribed, not ended
    low = __STMT__.lower()
    words = __STMT__.split()
    permanence = sum(1 for w in ["love", "written", "everything"] if w in low)
    print("permanence words: %d of %d" % (permanence, len(words)))
    assert permanence == 3 and len(words) == 15
    c = permanence / len(words) * 100.0
    print("permanence density: %.2f %%" % c)
    assert 19.99 < c < 20.01
    replace = ["another", "replace", "move on"]
    hits = [x for x in replace if x in low]
    print("replacement language: %d" % len(hits))
    assert len(hits) == 0
    print("OK: %s inscribed the love" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_complicated_grief(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # judgment scan: tangled grief must meet zero editing
    low = __STMT__.lower()
    words = __STMT__.split()
    judgment = ["should not feel", "wrong to", "disloyal", "move on", "good times"]
    hits = [x for x in judgment if x in low]
    print("judgment phrases found: %d" % len(hits))
    assert len(hits) == 0
    permission = sum(1 for w in ["does not require", "every feeling", "allowed"] if w in low)
    print("total-permission words: %d of %d" % (permission, len(words)))
    assert permission == 3 and len(words) == 15
    print("OK: %s refused to edit the grief" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_words_run_out(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # presence model: few words, long staying - comfort per word
    words = __STMT__.split()
    print("statement words: %d" % len(words))
    assert len(words) == 3
    minutes, calm = 60.0, 0.9
    comfort = minutes * calm / len(words)
    print("60 quiet minutes at calm 0.9 over %d words: %.2f presence-units/word"
          % (len(words), comfort))
    assert 17.99 < comfort < 18.01
    tax = sum(1 for x in ["because", "therefore", "you should"] if x in __STMT__.lower())
    print("explanation tax words: %d" % tax)
    assert tax == 0
    print("OK: %s let silence carry it" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


def demo_long_companion(hdr, name, rid, group, points, req, stmt):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # follow-up cadence: check-ins across two years, gaps widening honestly
    days = [1, 3, 7, 14, 30, 90, 180, 365, 730]
    total = sum(days)
    gaps = [b - a for a, b in zip(days, days[1:])]
    print("check-in days: %s" % days)
    print("gaps: %s" % gaps)
    print("touchpoints over 2 years: %d" % len(days))
    assert total == 1420
    assert gaps == [2, 4, 7, 16, 60, 90, 185, 365]
    assert all(b >= a for a, b in zip(gaps, gaps[1:])), "gaps widen, never vanish"
    years = sum(1 for w in ["years", "still remember", "still ask"] if w in __STMT__.lower())
    print("long-vow words: %d" % years)
    assert years == 3
    print("OK: %s kept the calendar" % NAME)
if __name__ == "__main__":
    main()
''', stmt)


DEMOS = {
    "simple_presence": demo_simple_presence,
    "naming_what_you_see": demo_naming_what_you_see,
    "permission_to_feel": demo_permission_to_feel,
    "honest_admission": demo_honest_admission,
    "listening_first": demo_listening_first,
    "hard_day": demo_hard_day,
    "honoring_effort": demo_honoring_effort,
    "disappointment": demo_disappointment,
    "visiting_sick": demo_visiting_sick,
    "after_mistake": demo_after_mistake,
    "fear": demo_fear,
    "exhaustion": demo_exhaustion,
    "pain_no_fix": demo_pain_no_fix,
    "loneliness": demo_loneliness,
    "caregiver": demo_caregiver,
    "plans_fall_apart": demo_plans_fall_apart,
    "grief_first_hours": demo_grief_first_hours,
    "job_loss": demo_job_loss,
    "diagnosis": demo_diagnosis,
    "separation": demo_separation,
    "grief_returns": demo_grief_returns,
    "child_loss": demo_child_loss,
    "financial": demo_financial,
    "chronic_illness": demo_chronic_illness,
    "anger_grief": demo_anger_grief,
    "regret": demo_regret,
    "unworthy": demo_unworthy,
    "long_goodbye": demo_long_goodbye,
    "sudden_loss": demo_sudden_loss,
    "survivor": demo_survivor,
    "parent_child_loss": demo_parent_child_loss,
    "complicated_grief": demo_complicated_grief,
    "words_run_out": demo_words_run_out,
    "long_companion": demo_long_companion,
}
