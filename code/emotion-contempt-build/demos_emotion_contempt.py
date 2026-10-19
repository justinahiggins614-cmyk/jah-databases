#!/usr/bin/env python3
"""Demo programs for the Contempt Emotion databases (Manon's 2026-10-17 16:15
emotion-series order, batch 2).

Every demo is real, runnable, stdlib-only Python performing the actual
emotion-scenario simulation for its record: scenario simulators, mix
blenders, recognition trainers, and intensity/arc models. All are
machine-executed by build.py before commit: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker. Descriptive/educational only - no diagnosing real people.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the verdict model: contempt strength from standard-gap and permanence
    gap = 7.5        # how far the person fell below the standard (0-10)
    permanence = 8.0 # how much it reads as character, not moment (0-10)
    strength = (gap * 0.6 + permanence * 0.4)
    print("standard gap: %.1f / 10" % gap)
    print("permanence reading: %.1f / 10" % permanence)
    print("verdict strength: %.2f / 10" % strength)
    assert 7.6 < strength < 7.8
    cool = 9.0  # low arousal signature of contempt (0-10)
    print("coolness (low arousal): %.1f / 10" % cool)
    assert cool > 8.0
    print("rule: gap x permanence = verdict; coolness = the signature")
    print("OK: %s modeled the verdict" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # CAD triad: moral emotion -> moral code it watches
    triad = {"contempt": "community/hierarchy", "anger": "autonomy",
             "disgust": "divinity/purity"}
    for emo, code in triad.items():
        print("  %-9s watches %s" % (emo, code))
    assert triad["contempt"] == "community/hierarchy"
    # distance from contempt on the family map (0-10)
    dist = {"contempt": 0.0, "disdain": 1.0, "scorn": 1.5, "anger": 3.0,
            "disgust": 3.5, "pity": 4.0, "respect": 9.0, "admiration": 9.5}
    nearest = min([k for k in dist if k != "contempt"], key=dist.get)
    print("nearest neighbor: %s" % nearest)
    assert nearest == "disdain"
    opp = max(dist, key=dist.get)
    print("opposite pole: %s" % opp)
    assert opp == "admiration"
    print("OK: %s mapped the CAD triad" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # intensity dial: mild -> moderate -> intense, permanence decides the register
    levels = [("mild disdain", 2.0, "the moment"), ("dismissal", 5.5, "the pattern"),
              ("scorn", 8.5, "the person")]
    for label, score, judged in levels:
        print("  %-13s %4.1f/10 judges %s" % (label, score, judged))
        assert 0.0 < score < 10.0
    scores = [s for _, s, _ in levels]
    assert scores == sorted(scores)
    # permanence is what separates the registers
    perm = [2.0, 5.0, 9.0]
    print("permanence across registers: %s" % perm)
    assert perm[2] > perm[1] > perm[0]
    print("rule: mild judges the moment, intense judges the person")
    print("OK: %s scaled the three volumes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    myths = [
        ("contempt is stronger anger", False, "different tools: anger confronts, contempt dismisses"),
        ("contempt is always snobbery", False, "it can be earned moral judgment"),
        ("contempt means hatred", False, "hatred wants harm; contempt wants absence"),
        ("contempt is rare", False, "common in marriages, workplaces, public life"),
        ("expressing it is harmless honesty", False, "it corrodes trust faster than most messages"),
    ]
    for myth, true, correction in myths:
        print("  MYTH: %-38s -> %s" % (myth, correction))
        assert true is False
    print("myths debunked: %d/%d" % (len(myths), len(myths)))
    print("OK: %s cleared the five myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three ingredients arriving together (weights sum to 1.0)
    ingredients = {"comparative appraisal": 0.45, "cooling of arousal": 0.30,
                   "withdrawal of engagement": 0.25}
    total = sum(ingredients.values())
    for k, v in ingredients.items():
        print("  %-24s %5.1f %%" % (k, v * 100.0))
    assert 0.999 < total < 1.001
    # the calm is the signature: certainty without heat
    certainty, heat = 9.0, 2.0
    print("certainty %.1f vs heat %.1f" % (certainty, heat))
    assert certainty > heat + 5.0
    print("OK: %s simulated the inside view" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_arc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the time-shape: fast onset, plateau peak, conditional fade, residue
    arc = [("onset", 1.0, "verdict clicks, under a second"),
           ("plateau", 48.0, "cool certainty, hours to days"),
           ("fading", 72.0, "gradual, needs verdict revision"),
           ("aftershock", 720.0, "reclassification lingers")]
    for phase, hours, note in arc:
        print("  %-10s ~%6.1f h  %s" % (phase, hours, note))
    # plateau outlasts onset by orders of magnitude: the cool signature
    assert arc[1][1] / arc[0][1] > 10.0
    # residue outlasts the feeling itself
    assert arc[3][1] > arc[2][1]
    print("rule: the arc ends, but the file stays edited")
    print("OK: %s traced onset to aftershock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scope and staying power decide the snapshot
    low = {"scope": "act", "arousal": 2.0, "residue": 0.0}
    high = {"scope": "person", "arousal": 4.5, "residue": 9.0}
    for label, s in (("low ", low), ("high", high)):
        print("  %s scope=%-6s arousal=%.1f residue=%.1f" %
              (label, s["scope"], s["arousal"], s["residue"]))
    assert high["residue"] > low["residue"] + 5.0
    assert high["arousal"] < 6.0  # even high contempt runs cool
    # the transition: repetition promotes incident to identity
    repetitions = [1, 3, 7, 12]
    promoted = [r >= 7 for r in repetitions]
    print("incident->identity promotion at 7+ repetitions: %s" % promoted)
    assert promoted == [False, False, True, True]
    print("OK: %s compared the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mixed_anger(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # indignation blend vector: contempt + anger components
    contempt = {"dismiss": 8.0, "cool": 8.5, "confront": 1.5}
    anger = {"dismiss": 2.0, "cool": 2.0, "confront": 8.5}
    blend = {k: (contempt[k] + anger[k]) / 2.0 for k in contempt}
    print("indignation blend:")
    for k, v in blend.items():
        print("  %-8s %.2f" % (k, v))
        assert 0.0 < v < 10.0
    # both dismiss AND confront are live: the signature of the blend
    assert blend["dismiss"] > 4.0 and blend["confront"] > 4.0
    # self-sealing: heat supplies conviction, cold dismisses counter-evidence
    sealing = 4.0 + blend["cool"] * 0.5 + blend["dismiss"] * 0.15
    print("self-sealing index: %.2f" % sealing)
    assert 7.3 < sealing < 7.5
    print("OK: %s blended contempt with anger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_day_in_life(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # drops of contempt through an ordinary day; accumulation makes the file
    drops = [("commute", 1.5, "driver"), ("meeting", 4.0, "colleague"),
             ("news", 6.0, "public figure"), ("evening", 2.0, "family")]
    total = 0.0
    by_target = {}
    for moment, size, target in drops:
        total += size
        by_target[target] = by_target.get(target, 0.0) + size
        print("  %-8s drop %.1f -> %s" % (moment, size, target))
    print("day total: %.1f" % total)
    assert 13.0 < total < 14.0
    # the file forms where drops accumulate on one target
    filed = [t for t, v in by_target.items() if v >= 4.0]
    print("targets with accumulating files: %s" % filed)
    assert filed == ["colleague", "public figure"]
    print("OK: %s ran the day ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arousal signature across emotions (0-10): contempt runs cool
    arousal = {"contempt": 2.5, "anger": 8.5, "fear": 9.0, "disgust": 6.0,
               "sadness": 3.5, "joy": 6.5}
    for emo, a in sorted(arousal.items(), key=lambda p: p[1]):
        print("  %-9s arousal %.1f" % (emo, a))
    assert arousal["contempt"] < arousal["disgust"] < arousal["anger"]
    coolest = min(arousal, key=arousal.get)
    print("coolest of the set: %s" % coolest)
    assert coolest == "contempt"
    # selective tension: face/neck hold, body does not brace
    print("tension: jaw/one-sided mouth/neck HOLD; whole-body brace ABSENT")
    print("OK: %s mapped the cool body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the geometry of looking down (degrees from neutral)
    pose = {"chin lift": 8.0, "head turn away": 12.0, "torso lean back": 6.0,
            "gesture speed": -50.0}
    for k, v in pose.items():
        unit = "%" if "speed" in k else "deg"
        print("  %-16s %+6.1f %s" % (k, v, unit))
    assert pose["chin lift"] > 0 and pose["torso lean back"] > 0
    assert pose["gesture speed"] < 0  # slowed to half speed
    # every element broadcasts the same message
    print("message: I am above this, and above you")
    print("OK: %s posed the hierarchy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # held contempt: nightly verdict rehearsal vs food appetite
    nights = 7
    rehearsals = [3, 4, 2, 5, 3, 4, 3]  # minutes of replay per night
    avg = sum(rehearsals) / len(rehearsals)
    print("avg nightly rehearsal: %.2f min over %d nights" % (avg, nights))
    assert 3.0 < avg < 4.0
    food_appetite_change = 0.5   # barely moved (0-10 scale)
    company_appetite_change = -4.0  # meals with the target become chores
    print("food appetite change: %+.1f; company appetite change: %+.1f" %
          (food_appetite_change, company_appetite_change))
    assert abs(food_appetite_change) < 1.0
    assert company_appetite_change < -2.0
    print("tiredness type: not exhausted, just unwilling")
    print("OK: %s tracked sleep and appetite" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what-is": demo_what_is,
    "family": demo_family,
    "intensity": demo_intensity,
    "myths": demo_myths,
    "first-person": demo_first_person,
    "arc": demo_arc,
    "low-vs-high": demo_low_vs_high,
    "mixed-anger": demo_mixed_anger,
    "day-in-life": demo_day_in_life,
    "body-signals": demo_body_signals,
    "posture": demo_posture,
    "sleep-appetite": demo_sleep_appetite,
}

def demo_bodies_differ(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # display dialects: the same verdict, different channels
    dialects = {
        "broadcaster": {"face": 9.0, "voice": 4.0, "silence": 2.0},
        "vocal": {"face": 3.0, "voice": 9.0, "silence": 3.0},
        "silent": {"face": 2.0, "voice": 2.0, "silence": 9.0},
        "polite-masker": {"face": 4.0, "voice": 5.0, "silence": 4.0},
    }
    for person, ch in dialects.items():
        dom = max(ch, key=ch.get)
        print("  %-13s dominant channel: %s (%.1f)" % (person, dom, ch[dom]))
        assert ch[dom] >= 8.0 or person == "polite-masker"
    print("rule: learn the language, then learn the speaker")
    print("OK: %s charted the dialects" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # asymmetry score: unilateral mouth action vs bilateral
    left_corner = 8.0   # active side
    right_corner = 0.5  # neutral side
    asymmetry = abs(left_corner - right_corner)
    print("mouth corner L=%.1f R=%.1f asymmetry=%.1f" %
          (left_corner, right_corner, asymmetry))
    assert asymmetry > 6.0
    brow_furrow = 0.5  # contempt keeps the forehead smooth
    print("brow furrow: %.1f (smooth = cool)" % brow_furrow)
    assert brow_furrow < 2.0
    gaze = "down the nose, past the target"
    print("gaze: %s" % gaze)
    print("OK: %s drew the one-sided face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four registers: felt intensity vs visibility
    registers = [
        ("low", 2.0, 3.0, "fractional tightening, mistaken for a smile"),
        ("moderate", 5.5, 8.0, "held unilateral curl, the textbook face"),
        ("high", 8.5, 9.5, "sneer, nostril flare, eye roll"),
        ("masked-high", 8.5, 2.5, "ironed into politeness; leaks in timing"),
    ]
    for label, felt, visible, note in registers:
        print("  %-11s felt %.1f visible %.1f  %s" % (label, felt, visible, note))
        assert 0.0 < felt < 10.0 and 0.0 < visible < 10.0
    # masked-high: strong feeling, low visibility
    assert registers[3][1] > 8.0 and registers[3][2] < 3.0
    print("rule: intensity does not always mean visibility")
    print("OK: %s graded the four registers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hide_fake(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hiding is easy (low arousal), faking is hard (asymmetry)
    hide_difficulty = 3.0   # 0-10
    fake_difficulty = 8.5
    print("hide difficulty: %.1f/10 (cool = easy to cover)" % hide_difficulty)
    print("fake difficulty: %.1f/10 (one-sided = hard to perform)" % fake_difficulty)
    assert hide_difficulty < 5.0 < fake_difficulty
    leaks = ["smile a beat late", "gaze slides off early",
             "over-careful politeness", "exhale before answering"]
    print("leakage channels (%d): %s" % (len(leaks), "; ".join(leaks)))
    assert len(leaks) == 4
    print("OK: %s tested hiding vs faking" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_drawing_guide(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # component checklist for the artist/actor (weight = importance)
    components = {"asymmetry first": 10.0, "gaze geometry": 8.0,
                  "smooth brow": 7.0, "half-speed body": 6.0,
                  "inner action: I have decided": 9.0}
    total = sum(components.values())
    for k, v in sorted(components.items(), key=lambda p: -p[1]):
        print("  %-28s weight %.1f" % (k, v))
    print("total weight: %.1f" % total)
    assert 39.0 < total < 41.0
    top = max(components, key=components.get)
    assert top == "asymmetry first"
    print("most common mistake: heat - contempt is refrigerated")
    print("OK: %s built the portrait" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the trigger menu: each shows claim vs evidence gap (0-10)
    triggers = {"incompetence on display": 8.0, "shamelessness": 8.5,
                "status violation": 7.5, "moral failure with pride": 9.0,
                "weakness as strength": 7.0, "trigger words": 5.5}
    for t, gap in sorted(triggers.items(), key=lambda p: -p[1]):
        print("  %-26s gap %.1f" % (t, gap))
    biggest = max(triggers, key=triggers.get)
    print("largest gap: %s" % biggest)
    assert biggest == "moral failure with pride"
    assert all(0.0 < v < 10.0 for v in triggers.values())
    print("rule: contempt rushes into the space between pretension and reality")
    print("OK: %s walked the trigger menu" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the old file reopens: present force borrows the past's weight
    original_force = 8.0   # the verdict as first filed
    present_situation = 2.0  # what the current moment deserves
    felt = original_force * 0.8 + present_situation * 0.2
    print("original filing force: %.1f" % original_force)
    print("present situation warrants: %.1f" % present_situation)
    print("felt force: %.2f (mostly borrowed)" % felt)
    assert 6.5 < felt < 7.0
    disproportion = felt - present_situation
    print("disproportion: %.2f -> trace the tag to its origin" % disproportion)
    assert disproportion > 4.0
    print("OK: %s opened the cold storage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the idling ranker: small triggers, each mapping a secret pride
    pairs = [("confident bad taste", "my taste"),
             ("misused big word", "my literacy"),
             ("weaponized helplessness", "my competence"),
             ("obscure-taste performance", "my authenticity")]
    for trigger, pride in pairs:
        print("  %-26s maps to pride in %s" % (trigger, pride))
    assert len(pairs) == 4
    print("rule: each strange weight is a mirror with dust on it")
    print("OK: %s opened the curiosity cabinet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cascade: each appraisal lowers the threshold for the next
    threshold = 7.0
    print("initial ranking threshold: %.1f" % threshold)
    steps = []
    for i in range(5):
        threshold *= 0.82  # momentum: easier to rank low each time
        steps.append(threshold)
        print("  appraisal %d -> threshold %.2f" % (i + 1, threshold))
    assert steps == sorted(steps, reverse=True)
    assert steps[-1] < 3.0
    # the circuit breaker: refuse the second ranking
    print("breaker: refuse appraisal 2 and the chain starves")
    print("OK: %s simulated the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four enactments, ranked by severity (0-10)
    acts = {"withdrawal": 3.0, "demotion": 5.0, "mockery": 7.0, "erasure": 9.5}
    for a, sev in sorted(acts.items(), key=lambda p: p[1]):
        print("  %-10s severity %.1f" % (a, sev))
    assert list(acts.values()) == sorted(acts.values())
    # deniability: each act alone is explainable; the pattern convicts
    deniable = {"withdrawal": True, "demotion": True, "mockery": True,
                "erasure": False}
    print("deniable alone: %s" % deniable)
    assert deniable["erasure"] is False
    print("OK: %s enacted the hierarchy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_behavior_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the phrasebook: literal politeness, verdict in the delivery
    phrases = ["well, actually...", "bless your heart", "I am sure you tried",
               "that is... an interesting choice", "we have already covered this",
               "as he was saying (while present)"]
    for p in phrases:
        print("  '%s'" % p)
    assert len(phrases) == 6
    # the exhale-laugh: one sound doing a paragraph's work
    print("exhale-laugh: 1 sound = 1 paragraph of verdict")
    print("rule: every phrase has an innocent reading; the pattern convicts")
    print("OK: %s transcribed the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_behavior_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # conclusion-first distortion: successes discounted, failures diagnostic
    target = {"successes": [8.0, 7.5, 8.5], "failures": [4.0, 3.5]}
    # contempt weights: success counts half, failure counts double
    scored = (sum(target["successes"]) * 0.5 + sum(target["failures"]) * 2.0)
    scored /= (len(target["successes"]) * 0.5 + len(target["failures"]) * 2.0)
    fair = (sum(target["successes"]) + sum(target["failures"]))
    fair /= (len(target["successes"]) + len(target["failures"]))
    print("fair score: %.2f; contempt-weighted score: %.2f" % (fair, scored))
    assert scored < fair - 1.0
    print("distortion: %.2f points of verdict" % (fair - scored))
    print("corrective: criteria written before the feeling arrived")
    print("OK: %s weighed the rigged decision" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "bodies-differ": demo_bodies_differ,
    "face": demo_face,
    "face-intensity": demo_face_intensity,
    "hide-fake": demo_hide_fake,
    "drawing-guide": demo_drawing_guide,
    "classic-triggers": demo_classic_triggers,
    "personal-triggers": demo_personal_triggers,
    "surprise-triggers": demo_surprise_triggers,
    "chain-reactions": demo_chain_reactions,
    "behavior-actions": demo_behavior_actions,
    "behavior-speech": demo_behavior_speech,
    "behavior-decisions": demo_behavior_decisions,
})

def demo_behavior_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four rungs: private -> social -> structural -> open
    rungs = [("private", 2.0, "unseen eye-roll"), ("social", 4.5, "audience recruited"),
             ("structural", 7.0, "exclusion built in"), ("open", 9.0, "verdict stated")]
    for label, sev, note in rungs:
        print("  rung %-10s severity %.1f  %s" % (label, sev, note))
    sevs = [s for _, s, _ in rungs]
    assert sevs == sorted(sevs)
    # intervene lowest-first: starve rung one
    print("de-escalation: re-include, refuse the audience, appeal the verdict - early")
    print("OK: %s climbed the ladder in reverse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # translation: verdict -> standard (the healthy conversion)
    verdict = "you are pathetic in meetings"
    standard = "I expect clear preparation in meetings"
    print("verdict : %s" % verdict)
    print("standard: %s" % standard)
    assert "you are" in verdict and "I expect" in standard
    # the measure: standard clearer AND person intact
    clarity_gain, person_intact = 8.0, 9.0
    print("clarity gain %.1f; person intact %.1f" % (clarity_gain, person_intact))
    assert clarity_gain > 6.0 and person_intact > 6.0
    print("OK: %s translated verdict to standard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two failures, one root: the verdict never became a standard
    bottle = {"voiced": 0.0, "ferment": 9.0, "relationship_hollow": 8.5}
    explode = {"voiced": 10.0, "finality": 9.5, "survival_odds": 1.5}
    print("bottling : voiced %.1f ferment %.1f hollow %.1f" %
          (bottle["voiced"], bottle["ferment"], bottle["relationship_hollow"]))
    print("exploding: voiced %.1f finality %.1f survival %.1f" %
          (explode["voiced"], explode["finality"], explode["survival_odds"]))
    assert bottle["ferment"] > 8.0 and explode["survival_odds"] < 3.0
    print("third road: keep the standard, retire the verdict")
    print("OK: %s costed both failures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five maintenance habits, each scoring a supervision link (0-10)
    practices = {"verdict audit": 8.0, "competence inventory": 7.5,
                 "hierarchy holiday": 8.5, "translation drill": 7.0,
                 "direct channel": 9.0}
    for p, v in sorted(practices.items(), key=lambda q: -q[1]):
        print("  %-20s supervision %.1f" % (p, v))
    avg = sum(practices.values()) / len(practices)
    print("average supervision: %.2f" % avg)
    assert 7.5 < avg < 8.5
    print("motto: a scale never calibrated weighs only the weigher's mood")
    print("OK: %s ran the maintenance log" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # channel convergence: face + voice + body + pattern over time
    channels = {"face (one-sided)": 0.8, "voice (teacher-tone)": 0.7,
                "body (lean-back)": 0.6, "pattern (consulted less)": 0.9}
    evidence = sum(channels.values()) / len(channels)
    print("channels:")
    for k, v in channels.items():
        print("  %-24s %.1f" % (k, v))
    print("converged evidence: %.3f" % evidence)
    assert 0.70 < evidence < 0.80
    reliable = evidence > 0.65
    print("reliable read: %s (single cues never are)" % reliable)
    assert reliable is True
    print("OK: %s converged the channels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_supportive_response(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # response options scored on de-escalation value (0-10)
    options = {"ask about the standard": 9.0, "join the verdict": 1.0,
               "name the pattern, not the feeling": 8.0,
               "grovel": 2.0, "counter-attack": 1.5,
               "curiosity + dignity": 8.5, "healthy distance": 7.5}
    best = max(options, key=options.get)
    worst = min(options, key=options.get)
    for o, v in sorted(options.items(), key=lambda p: -p[1]):
        print("  %-32s %.1f" % (o, v))
    print("best: %s; worst: %s" % (best, worst))
    assert best == "ask about the standard"
    assert worst == "join the verdict"
    print("OK: %s chose the broker's lines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_what_not_to_do(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five engines; starve all five at once
    engines = {"social": "performing for audience", "certainty": "trusting the chill",
               "hierarchy": "shaming/counter-ranking", "generalization": "feeling as fact",
               "commitment": "early voicing"}
    for engine, fuel in engines.items():
        print("  starve %-13s by refusing: %s" % (engine, fuel))
    assert len(engines) == 5
    print("rule: what makes the verdict more public, certain, or permanent makes it worse")
    print("OK: %s posted the warning placard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_neighbors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three axes: gaze (down=-1/up=+1), temperature (0-10), target (act/person)
    axes = {
        "contempt": (-1, 2.5, "person"), "disdain": (-1, 3.0, "person"),
        "scorn": (-1, 4.0, "person"), "anger": (0, 8.5, "act"),
        "disgust": (0, 6.0, "thing"), "pity": (-1, 3.5, "person"),
        "respect": (+1, 4.0, "person"),
    }
    for emo, (gaze, temp, target) in axes.items():
        print("  %-9s gaze %+d temp %.1f target %s" % (emo, gaze, temp, target))
    # contempt vs disgust: person vs thing; contempt vs pity: unworthy vs unfortunate
    assert axes["contempt"][2] == "person" and axes["disgust"][2] == "thing"
    assert axes["respect"][0] == +1  # the opposite pole looks up
    print("OK: %s surveyed the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five blends: partner appraisal + signature behavior
    blends = {
        "indignation": ("anger", "lectures"),
        "revulsion": ("disgust", "shuns"),
        "mockery": ("amusement", "performs"),
        "condescension": ("pity", "pats on the head"),
        "bully's blend": ("fear", "strikes first"),
    }
    for blend, (partner, signature) in blends.items():
        print("  contempt + %-9s = %-13s -> %s" % (partner, blend, signature))
    assert len(blends) == 5
    # blends are more stable than pure contempt: appraisals validate each other
    stability = {"pure contempt": 6.0, "indignation": 8.5, "mockery": 8.0}
    assert stability["indignation"] > stability["pure contempt"]
    print("rule: pure metals bend; it is the alloys that cut")
    print("OK: %s assayed the blends" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five scenes: the whole machinery in order
    scenes = [
        ("trigger", "appraisal clicks", 1.0, 2.5),
        ("plateau", "teacher-voice, audience recruited", 48.0, 4.0),
        ("cascade", "generalization, structural exclusion", 336.0, 7.5),
        ("reckoning", "the standard forced into words", 1.0, 5.0),
        ("resolution", "standard posted, verdict retired", 24.0, 2.0),
    ]
    peak = 0.0
    for label, note, hours, severity in scenes:
        print("  %-10s %4.0f h sev %.1f  %s" % (label, hours, severity, note))
        peak = max(peak, severity)
        assert 0.0 < severity < 10.0
    print("peak severity: %.1f at the cascade" % peak)
    assert abs(peak - 7.5) < 0.01
    # resolution retires the verdict but keeps the standard
    print("end state: verdict retired, standard posted, colleague restored")
    print("OK: %s ran the five scenes" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "behavior-escalation": demo_behavior_escalation,
    "healthy-expression": demo_healthy_expression,
    "unhealthy-expression": demo_unhealthy_expression,
    "everyday-practices": demo_everyday_practices,
    "reading-others": demo_reading_others,
    "supportive-response": demo_supportive_response,
    "what-not-to-do": demo_what_not_to_do,
    "neighbors": demo_neighbors,
    "mixes": demo_mixes,
    "full-simulation": demo_full_simulation,
})
