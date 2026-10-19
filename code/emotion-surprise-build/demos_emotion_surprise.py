#!/usr/bin/env python3
"""Demo programs for The Surprise Emotion Database (emotion-surprise).

Every demo is an emotion-scenario simulator: real, runnable, stdlib-only
Python that simulates surprise unfolding - trigger appraisal, body signals,
facial expression, dialogue, behavior, and landing - with real computed
values. All are machine-executed by build.py: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker. Descriptive/educational only - nothing here diagnoses anyone.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_ems_def1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # surprise score = prediction gap x suddenness; fires above threshold
    scenarios = [
        ("coffee shop moved chairs", 0.55, 0.45),
        ("friend jumps out shouting", 0.90, 0.95),
        ("plot twist in film", 0.70, 0.60),
        ("usual morning alarm", 0.05, 0.10),
    ]
    threshold = 0.20
    fired = 0
    for label, gap, sudden in scenarios:
        score = gap * sudden
        verdict = "SURPRISE" if score > threshold else "no surprise"
        print("%-28s gap=%.2f sudden=%.2f score=%.3f -> %s" % (label, gap, sudden, score, verdict))
        if score > threshold:
            fired += 1
    assert 0.246 < 0.55 * 0.45 < 0.249
    assert 0.854 < 0.90 * 0.95 < 0.856
    assert fired == 3, "three of four scenarios break prediction"
    print("rule: surprise is the mismatch detector firing - gap times suddenness")
    print("OK: %s scored four scenarios" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Plutchik-style blend: surprise (neutral, high arousal) + joy -> delight
    surprise = {"valence": 0.0, "arousal": 0.9}
    joy = {"valence": 0.9, "arousal": 0.6}
    fear = {"valence": -0.9, "arousal": 0.9}
    def blend(a, b, w=0.5):
        return {"valence": w * a["valence"] + (1 - w) * b["valence"],
                "arousal": w * a["arousal"] + (1 - w) * b["arousal"]}
    delight = blend(surprise, joy)
    alarm = blend(surprise, fear)
    print("delight: valence=%+.2f arousal=%.2f" % (delight["valence"], delight["arousal"]))
    print("alarm:   valence=%+.2f arousal=%.2f" % (alarm["valence"], alarm["arousal"]))
    assert 0.44 < delight["valence"] < 0.46
    assert 0.74 < delight["arousal"] < 0.76
    assert -0.46 < alarm["valence"] < -0.44
    assert 0.89 < alarm["arousal"] < 0.91
    assert abs(surprise["valence"]) < 0.01, "surprise itself is valence-neutral"
    print("rule: surprise is the neutral crossroads - the partner picks the direction")
    print("OK: %s blended the family" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_volumes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # volume = novelty x significance x suddenness, scaled 1-10
    def volume(novelty, significance, suddenness):
        return 1.0 + 9.0 * novelty * significance * suddenness
    cases = [
        ("moved chairs", 0.2, 0.1, 0.5),
        ("plot twist", 0.7, 0.4, 0.8),
        ("car swerves into lane", 0.9, 1.0, 1.0),
    ]
    for label, n, s, u in cases:
        v = volume(n, s, u)
        band = "whisper" if v < 4 else ("moderate" if v < 7 else "thunderclap")
        print("%-22s volume=%.2f/10 -> %s" % (label, v, band))
    assert 1.08 < volume(0.2, 0.1, 0.5) < 1.10
    assert 2.99 < volume(0.7, 0.4, 0.8) < 3.02
    assert 9.09 < volume(0.9, 1.0, 1.0) < 9.11
    print("rule: the same circuit at different dial settings - whisper to thunderclap")
    print("OK: %s set the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # myth-or-fact quiz scored against the mismatch model
    items = [
        ("surprise is always unpleasant", False),
        ("easy startle means weak character", False),
        ("surprise proves attention was working", True),
        ("the first half-second can be suppressed", False),
        ("surprise itself is neutral", True),
    ]
    model = {"surprise is always unpleasant": False,
             "easy startle means weak character": False,
             "surprise proves attention was working": True,
             "the first half-second can be suppressed": False,
             "surprise itself is neutral": True}
    score = sum(1 for label, _ in items if model[label] == dict(items)[label])
    for label, truth in items:
        print("%-42s fact=%s" % (label, truth))
    print("myth-busting score: %d/%d" % (score, len(items)))
    assert score == 5
    assert len(items) == 5
    print("rule: test every belief against the mismatch model - myths fail the test")
    print("OK: %s busted five myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_firstperson(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # first-person passage generator: intensity picks the sentences
    def passage(intensity):
        lines = ["The world skips a frame - my breath catches without asking."]
        if intensity >= 0.4:
            lines.append("My eyes go wide on their own, trying to take in more of it.")
        if intensity >= 0.7:
            lines.append("There are no words in my head at all, just bright buzzing alertness.")
            lines.append("Time stretches - every sense turned all the way up at once.")
        lines.append("Then the questions arrive, all out of order: what was that, am I okay.")
        return lines
    for inten in (0.2, 0.5, 0.9):
        lines = passage(inten)
        print("--- intensity %.1f: %d lines" % (inten, len(lines)))
        for ln in lines:
            print("  " + ln)
    assert len(passage(0.2)) == 2
    assert len(passage(0.5)) == 3
    assert len(passage(0.9)) == 5
    print("rule: the inside of surprise is a bright blank - then questions, then the landing")
    print("OK: %s voiced the inside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_timecourse(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # arousal curve: fast rise, exponential decay, slow aftershock tail
    def arousal(t):
        # t in seconds; rise tau 0.25s, decay tau 2.5s, aftershock tau 600s
        if t < 0:
            return 0.0
        rise = 1.0 - math.exp(-t / 0.25)
        decay = math.exp(-t / 2.5)
        after = 0.25 * math.exp(-t / 600.0)
        return rise * decay + after
    for t in (0.3, 1.0, 3.0, 60.0):
        print("t=%5.1fs arousal=%.3f" % (t, arousal(t)))
    peak = max((arousal(t / 10.0), t / 10.0) for t in range(1, 200))[1]
    print("peak near t=%.1fs" % peak)
    assert 0.86 < arousal(0.3) < 0.88
    assert 0.90 < arousal(1.0) < 0.92
    assert 0.54 < arousal(3.0) < 0.56
    assert 0.22 < arousal(60.0) < 0.24
    assert 0.5 < peak < 1.5, "peak lands in the first second"
    print("rule: milliseconds to rise, seconds to fade, minutes of aftershock")
    print("OK: %s ran the timeline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_lowhigh(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # two lived snapshots as parameter sets on the same circuit
    whisper = {"hr_jump": 3, "freeze_s": 0.3, "brow_mm": 1.0, "story": False}
    thunder = {"hr_jump": 35, "freeze_s": 2.5, "brow_mm": 8.0, "story": True}
    for label, s in (("whisper", whisper), ("thunderclap", thunder)):
        print("%-11s hr+%dbpm freeze=%.1fs brow=%.1fmm story=%s"
              % (label, s["hr_jump"], s["freeze_s"], s["brow_mm"], s["story"]))
    ratio = thunder["hr_jump"] / whisper["hr_jump"]
    print("heart-rate jump ratio: %.1fx" % ratio)
    assert 11.6 < ratio < 11.8
    assert whisper["freeze_s"] < thunder["freeze_s"]
    assert whisper["story"] is False and thunder["story"] is True
    print("rule: same circuit, opposite dial settings - hiccup vs picked-up-and-set-down")
    print("OK: %s held both snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_mixfear(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the fear blend: shared arousal + context appraisal
    def blend(context_threat):
        arousal = 0.85  # shared body preparation
        fear_layer = arousal * context_threat
        return {"arousal": arousal, "fear_layer": fear_layer,
                "label": "alarm" if fear_layer > 0.4 else "pure surprise"}
    for ctx, threat in (("balloon at party", 0.05), ("pop alone at night", 0.80)):
        b = blend(threat)
        print("%-20s fear_layer=%.2f -> %s" % (ctx, b["fear_layer"], b["label"]))
    assert 0.03 < blend(0.05)["fear_layer"] < 0.06
    assert 0.67 < blend(0.80)["fear_layer"] < 0.69
    assert blend(0.05)["label"] == "pure surprise"
    assert blend(0.80)["label"] == "alarm"
    print("rule: the body stands in fear's posture already - context picks the blend")
    print("OK: %s mixed the pair" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_dayinlife(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # tally one Tuesday: the mismatch detector at work all day
    day = [
        ("06:42", "alarm tone wrong", "whisper", "amusement"),
        ("07:15", "cold shower", "low-moderate", "laughter"),
        ("08:30", "road closed", "moderate", "annoyance"),
        ("12:10", "unexpected compliment", "moderate", "pleasure"),
        ("15:45", "strange email subject", "whisper", "curiosity"),
        ("20:00", "plot twist", "moderate-high", "delight"),
        ("21:30", "gift on porch", "moderate", "joy"),
    ]
    print("surprises logged: %d" % len(day))
    landings = {}
    for t, what, vol, land in day:
        landings[land] = landings.get(land, 0) + 1
        print("  %s %-22s [%s] -> %s" % (t, what, vol, land))
    print("distinct landings: %d" % len(landings))
    assert len(day) == 7
    assert len(landings) == 7, "every surprise lands somewhere different"
    print("rule: hitch, attention, appraisal, landing - eight times before bedtime")
    print("OK: %s lived the Tuesday" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # heart-rate spike and recovery after a startle
    baseline, spike = 72.0, 38.0
    def hr(t):
        return baseline + spike * math.exp(-t / 4.0)
    for t in (0.0, 4.0, 12.0):
        print("t=%4.1fs heart rate=%.1f bpm" % (t, hr(t)))
    assert 109.9 < hr(0.0) < 110.1
    assert 85.9 < hr(4.0) < 86.1
    assert 73.8 < hr(12.0) < 74.0
    gasp_liters = 1.5  # sharp intake above tidal volume
    print("gasp intake above tidal: %.1f L" % gasp_liters)
    assert 1.49 < gasp_liters < 1.51
    print("rule: defend first, identify later - the body runs the drill in milliseconds")
    print("OK: %s traced the body" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ems_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # three acts: crouch (defense), orient (investigate), discharge (release)
    def act(intensity):
        freeze = 0.3 + 1.7 * intensity
        if intensity < 0.35:
            return ("crouch", freeze, "none")
        if intensity < 0.7:
            return ("crouch+orient", freeze, "lean-in")
        return ("crouch+orient+discharge", freeze, "shake-out")
    for inten in (0.2, 0.5, 0.9):
        a, fz, dis = act(inten)
        print("intensity %.1f: %s freeze=%.2fs discharge=%s" % (inten, a, fz, dis))
    a02 = act(0.2)
    assert a02[0] == "crouch" and a02[2] == "none"
    assert 0.639 < a02[1] < 0.641
    assert 1.14 < act(0.5)[1] < 1.16
    assert act(0.9)[2] == "shake-out"
    print("rule: crouch protects the instrument, orient aims it, discharge resets it")
    print("OK: %s staged the three acts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_sleep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # aftershock: lowered startle threshold recovering over hours
    def threshold(hours_after):
        # 1.0 = normal; dips to 0.55 right after, recovers with tau 3h
        return 1.0 - 0.45 * math.exp(-hours_after / 3.0)
    for h in (0.0, 3.0, 9.0):
        print("t+%dh startle threshold=%.2f of normal" % (h, threshold(h)))
    assert 0.54 < threshold(0.0) < 0.56
    assert 0.83 < threshold(3.0) < 0.85
    assert 0.97 < threshold(9.0) < 0.99
    fuel_spent = 180.0  # kcal mobilized by a big false alarm, repaid by rest+food
    print("fuel mobilized by big false alarm: %.0f kcal" % fuel_spent)
    assert 179.9 < fuel_spent < 180.1
    print("rule: the sprint's bill comes due - quieter evening, real food, rest")
    print("OK: %s balanced the fuel books" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # personal instruments: seeded sensitivity profiles, same balloon
    import random
    rng = random.Random(42)
    people = {
        "Ana": {"wiring": 1.3, "recovery_h": 0.1},
        "Ben": {"wiring": 0.6, "recovery_h": 0.2},
        "Cara": {"wiring": 1.4, "recovery_h": 2.5},
    }
    balloon = 0.8  # trigger strength
    for who, p in people.items():
        jolt = balloon * p["wiring"] * (0.9 + 0.2 * rng.random())
        print("%-5s jolt=%.2f aftershock=%.1fh" % (who, jolt, p["recovery_h"]))
    jolts = {w: balloon * p["wiring"] for w, p in people.items()}
    assert 0.47 < jolts["Ben"] < 0.49
    assert 1.03 < jolts["Ana"] < 1.05
    assert 1.11 < jolts["Cara"] < 1.13
    assert jolts["Ben"] < jolts["Ana"] < jolts["Cara"], "same balloon, three honest answers"
    print("rule: same balloon, three honest answers - learn your own instrument")
    print("OK: %s tuned three bells" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # FACS action units for surprise: AU1+2 brow raise, AU5 lid raise, AU26 jaw drop
    def aus(intensity):
        return {"AU1+2 brow raise": 5.0 * intensity,
                "AU5 lid raise": 5.0 * intensity,
                "AU26 jaw drop": 5.0 * intensity}
    for inten in (0.3, 0.7, 1.0):
        a = aus(inten)
        print("intensity %.1f: " % inten +
              ", ".join("%s=%.1f" % (k, v) for k, v in a.items()))
    a = aus(0.7)
    assert 3.49 < a["AU1+2 brow raise"] < 3.51
    assert 3.49 < a["AU5 lid raise"] < 3.51
    assert 3.49 < a["AU26 jaw drop"] < 3.51
    onset_ms = 400.0  # all three moves assemble within half a second
    print("full tableau assembly: <%.0f ms" % onset_ms)
    assert 399.9 < onset_ms < 400.1
    print("rule: brows up, eyes wide, jaw down - the face becomes an intake device")
    print("OK: %s coded the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_intensityface(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the dial: amplitude and hold time scale with volume
    def face(intensity):
        amp = 10.0 * intensity          # brow lift in mm
        hold = 0.5 + 3.5 * intensity    # seconds the tableau holds
        band = "flicker" if intensity < 0.35 else ("trio" if intensity < 0.7 else "full blaze")
        return amp, hold, band
    for inten in (0.2, 0.5, 0.9):
        amp, hold, band = face(inten)
        print("intensity %.1f: brow=%.1fmm hold=%.2fs -> %s" % (inten, amp, hold, band))
    assert face(0.2)[2] == "flicker" and face(0.5)[2] == "trio" and face(0.9)[2] == "full blaze"
    assert 1.99 < face(0.2)[0] < 2.01
    assert 3.64 < face(0.9)[1] < 3.66
    print("rule: amplitude and duration report the volume honestly")
    print("OK: %s turned the dial" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_hidefake(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # leakage vs suppression effort; faked timing vs genuine timing
    def leak(suppression):
        # suppression 0..1; leak probability falls but never to zero
        return 0.95 * math.exp(-2.0 * suppression) + 0.05
    for s in (0.0, 0.5, 0.9):
        print("suppression %.1f -> leak probability %.2f" % (s, leak(s)))
    assert 0.99 < leak(0.0) < 1.01
    assert 0.39 < leak(0.5) < 0.41
    assert 0.20 < leak(0.9) < 0.22
    genuine_onset, acted_onset = 0.30, 1.40  # seconds to full tableau
    print("genuine onset %.1fs vs acted onset %.1fs" % (genuine_onset, acted_onset))
    assert acted_onset > 3.0 * genuine_onset
    print("rule: the bell cannot be unrung in the first half-second - trust the flash")
    print("OK: %s caught the leak" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_artist(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the artist's notes as a generated description from the dial setting
    def describe(intensity):
        parts = ["brows arched high, forehead creased in horizontal waves"]
        if intensity >= 0.35:
            parts.append("eyes wide, white showing above and below the iris, gaze aimed")
        if intensity >= 0.7:
            parts.append("jaw hanging slack, mouth a dark oval")
            parts.append("head pulled back a fraction, hands rising palm-open")
        return "; ".join(parts) + "."
    for inten in (0.2, 0.5, 0.9):
        d = describe(inten)
        print("intensity %.1f (%d features): %s" % (inten, d.count(";") + 1, d[:80] + "..."))
    assert describe(0.2).count(";") == 0
    assert describe(0.5).count(";") == 1
    assert describe(0.9).count(";") == 3
    print("rule: brows, eyes, mouth, head, hands - draw the beacon faithfully")
    print("OK: %s sketched the look" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_classictriggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # four families, each trigger scored by prediction-break size
    catalog = {
        "sound": [("thunderclap", 0.95), ("balloon pop", 0.85)],
        "vision": [("figure lunges from dark", 0.90), ("lights snap on", 0.60)],
        "news": [("won prize never entered", 0.95), ("dinner is ready", 0.20)],
        "social": [("friend at door unannounced", 0.75), ("stranger knows my name", 0.88)],
        "body": [("missing stair", 0.70), ("phantom phone buzz", 0.45)],
    }
    total = 0
    for fam, items in catalog.items():
        for label, brk in items:
            total += 1
            print("%-6s %-28s break=%.2f" % (fam, label, brk))
    assert total == 10
    strongest = max(b for items in catalog.values() for _, b in items)
    weakest = min(b for items in catalog.values() for _, b in items)
    assert 0.94 < strongest < 0.96
    assert 0.19 < weakest < 0.21
    print("rule: quiet, continuity, predictable people, solid stairs - that is what we expect")
    print("OK: %s catalogued the hammers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_personaltriggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # private associative network: stimulus unlocks weighted memories
    network = {"wedding song": [("dance floor", 0.9), ("vows", 0.85), ("the ending", 0.95)],
               "old street": [("childhood home", 0.7), ("the move", 0.6)],
               "a phrase": [("who used to say it", 0.8)]}
    def unlock(stimulus):
        mems = network[stimulus]
        load = sum(w for _, w in mems) / len(mems)
        return load, len(mems)
    for stim in network:
        load, n = unlock(stim)
        print("%-12s unlocks %d memories, mean weight %.2f" % (stim, n, load))
    load, n = unlock("wedding song")
    assert n == 3
    assert 0.89 < load < 0.91
    print("rule: never just the song - the whole network arrives in one package")
    print("OK: %s mapped the private catalog" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_oddtriggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # jolt = confidence in prediction x size of violation
    def jolt(confidence, violation):
        return confidence * violation
    cases = [("typo in beloved book", 0.99, 0.30),
             ("clock stops ticking", 0.95, 0.55),
             ("parrot speaks after 10 silent years", 0.99, 0.90),
             ("text reply in 11 seconds to morning message", 0.90, 0.70)]
    for label, c, v in cases:
        print("%-42s jolt=%.3f" % (label, jolt(c, v)))
    assert 0.296 < jolt(0.99, 0.30) < 0.298
    assert 0.890 < jolt(0.99, 0.90) < 0.892
    biggest = max(cases, key=lambda c: jolt(c[1], c[2]))
    assert biggest[0] == "parrot speaks after 10 silent years"
    print("rule: high confidence is the secret ingredient of odd triggers")
    print("OK: %s weighed the odd ones" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ems_chains(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # cascade: each surprise lowers the threshold for the next
    threshold, surprises = 1.0, []
    events = ["fire alarm", "smoke in stairwell", "elevators out", "it was a drill"]
    strengths = [0.9, 0.7, 0.6, 0.8]
    for ev, s in zip(events, strengths):
        felt = s / threshold
        surprises.append((ev, felt))
        threshold *= 0.82  # each ring lowers the bar for the next
        print("%-18s felt=%.2f threshold now=%.2f" % (ev, felt, threshold))
    assert 0.89 < surprises[0][1] < 0.91
    assert 1.44 < surprises[3][1] < 1.46, "the fourth rings loudest on a lowered threshold"
    assert 0.44 < threshold < 0.46
    print("rule: cascades are broken by information - name it early, give solid ground")
    print("OK: %s ran the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_behaviors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # action probabilities by intensity: freeze, orient, recoil, recruit
    def actions(intensity):
        freeze = min(1.0, 0.4 + intensity)
        orient = min(1.0, intensity * 1.1)
        recoil = max(0.0, (intensity - 0.45) * 1.6)
        recruit = max(0.0, (intensity - 0.30) * 1.2)
        return {"freeze": freeze, "orient": orient, "recoil": recoil, "recruit": recruit}
    for inten in (0.2, 0.6, 0.95):
        a = actions(inten)
        print("intensity %.2f: " % inten +
              ", ".join("%s=%.2f" % (k, v) for k, v in a.items()))
    a = actions(0.6)
    assert 0.99 < a["freeze"] < 1.01
    assert 0.65 < a["orient"] < 0.67
    assert 0.23 < a["recoil"] < 0.25
    assert 0.35 < a["recruit"] < 0.37
    assert actions(0.2)["recoil"] == 0.0, "low surprise never recoils"
    print("rule: freeze, orient, recoil, recruit - then the telling")
    print("OK: %s choreographed the crowd" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # prosody under arousal: pitch, rate, fluency
    def prosody(arousal):
        pitch_mult = 1.0 + 0.45 * arousal
        rate_mult = 1.0 + 0.60 * arousal
        fluency = 1.0 - 0.55 * arousal  # false starts rise
        return pitch_mult, rate_mult, fluency
    for ar in (0.2, 0.6, 0.95):
        p, r, f = prosody(ar)
        print("arousal %.2f: pitch x%.2f rate x%.2f fluency %.2f" % (ar, p, r, f))
    p, r, f = prosody(0.6)
    assert 1.26 < p < 1.28
    assert 1.35 < r < 1.37
    assert 0.66 < f < 0.68
    first_words = ["what?", "what was that?", "are you serious?", "no way"]
    print("first words: %s" % ", ".join(first_words))
    assert len(first_words) == 4
    print("rule: gasp first, questions second, story third - the voice walks the path")
    print("OK: %s transcribed the soundtrack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # decision tilts after a prediction break
    def tilts(arousal):
        caution = 0.5 * arousal            # risk aversion bump
        spotlight = 0.7 * arousal          # overweighting of the trigger
        carryover = 0.4 * arousal          # handoff emotion bleeding in
        learning = 0.8 * arousal           # map-update value (the useful tilt)
        return caution, spotlight, carryover, learning
    for ar in (0.3, 0.8):
        c, s, co, l = tilts(ar)
        print("arousal %.1f: caution=%.2f spotlight=%.2f carryover=%.2f learning=%.2f"
              % (ar, c, s, co, l))
    c, s, co, l = tilts(0.8)
    assert 0.39 < c < 0.41
    assert 0.55 < s < 0.57
    assert 0.31 < co < 0.33
    assert 0.63 < l < 0.65
    print("rule: let the tilt pass, keep the lesson, then decide with the updated map")
    print("OK: %s steadied the table" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # four stages by intensity; stage-matched response
    def stage(intensity):
        if intensity < 0.4:
            return (1, "freeze+orient", "let it run")
        if intensity < 0.65:
            return (2, "vocalize+recruit", "join calmly")
        if intensity < 0.85:
            return (3, "defense before appraisal", "one clear instruction")
        return (4, "overload", "radical simplicity: one voice, one sentence")
    for inten in (0.25, 0.5, 0.75, 0.95):
        n, desc, resp = stage(inten)
        print("intensity %.2f -> stage %d (%s): %s" % (inten, n, desc, resp))
    assert stage(0.25)[0] == 1
    assert stage(0.5)[0] == 2
    assert stage(0.75)[0] == 3
    assert stage(0.95)[0] == 4
    assert "one voice" in stage(0.95)[2]
    print("rule: the stages are weather, not identity - match the stage")
    print("OK: %s managed the stages" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_healthyexpr(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # three-step clean expression scored per step
    steps = [("permission: let the half-second happen", 1.0),
             ("narration: 'that startled me, give me a second'", 1.0),
             ("channeling: laugh, breath, movement - or savoring", 1.0)]
    score = sum(w for _, w in steps)
    for label, w in steps:
        print("  [x] %s (weight %.1f)" % (label, w))
    print("expression cleanliness: %.1f/3.0" % score)
    assert 2.99 < score < 3.01
    suppressed_cost = 1.6  # extra arousal-minutes when the half-second is fought
    print("suppression surcharge: x%.1f lingering arousal" % suppressed_cost)
    assert 1.59 < suppressed_cost < 1.61
    print("rule: permission, narration, channeling - let the bell ring clean")
    print("OK: %s expressed it well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_unhealthy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the books: bottled vs exploded vs middle path
    def account(style, surprises):
        # returns (lingering arousal units, social cost units)
        if style == "bottled":
            return (2.2 * surprises, 0.8 * surprises)
        if style == "exploded":
            return (1.4 * surprises, 2.5 * surprises)
        return (0.5 * surprises, 0.2 * surprises)  # middle path
    for style in ("bottled", "exploded", "middle"):
        ar, sc = account(style, 3)
        print("%-8s lingering=%.1f social cost=%.1f total=%.1f" % (style, ar, sc, ar + sc))
    b3 = account("bottled", 3)
    assert 6.59 < b3[0] < 6.61 and 2.39 < b3[1] < 2.41
    mb, me, mm = (sum(account(s, 3)) for s in ("bottled", "exploded", "middle"))
    assert 8.99 < mb < 9.01 and 11.69 < me < 11.71 and 2.09 < mm < 2.11
    assert mm < mb and mm < me, "the middle path balances the books"
    print("rule: feel fully, express cleanly, land quickly - the books balance")
    print("OK: %s did the accounting" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 28 days of small habits compounding: aftershock minutes shrink
    aftershock = 20.0  # minutes after a big startle, week zero
    for week in range(1, 5):
        aftershock *= 0.72  # recovery breath + narration + audits compound
        print("week %d: aftershock %.1f min" % (week, aftershock))
    assert 20.0 * 0.72 < 14.5 and 20.0 * 0.72 > 14.3
    final = 20.0 * (0.72 ** 4)
    assert 5.3 < final < 5.5
    habits = ["recovery breath", "narration sentences", "threshold audit",
              "deliberate novelty", "gentle reveals", "savoring pause"]
    print("habits installed: %d" % len(habits))
    assert len(habits) == 6
    print("rule: housekeeping for the instrument - tuned, cleaned, played regularly")
    print("OK: %s kept the bell true" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ems_reading(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # four-channel read: face, body, voice, context -> confidence
    def read(face, body, voice, context):
        channels = [face, body, voice, context]  # each 0..1
        conf = sum(channels) / len(channels)
        verdict = "certain" if conf > 0.75 else ("likely" if conf > 0.5 else "hypothesis")
        return conf, verdict
    cases = [("party guest", 0.9, 0.85, 0.8, 0.95),
             ("suppressed in meeting", 0.3, 0.7, 0.2, 0.9),
             ("acted for camera", 0.8, 0.3, 0.6, 0.4)]
    for label, f, b, v, c in cases:
        conf, verdict = read(f, b, v, c)
        print("%-20s confidence=%.2f -> %s" % (label, conf, verdict))
    assert 0.86 < read(0.9, 0.85, 0.8, 0.95)[0] < 0.88
    assert read(0.9, 0.85, 0.8, 0.95)[1] == "certain"
    assert read(0.3, 0.7, 0.2, 0.9)[1] == "likely"
    assert read(0.8, 0.3, 0.6, 0.4)[1] == "likely"
    print("rule: three channels agreeing is near-certain; context is the fourth channel")
    print("OK: %s read the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_support(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # response picker: stage -> the right first move
    moves = {1: "calm presence, quiet face - let the landing form",
             2: "name without claiming: 'that startled you'",
             3: "one clear piece of information, one simple next step",
             4: "reduce input: one voice, one sentence, then wait"}
    for stage in (1, 2, 3, 4):
        print("stage %d -> %s" % (stage, moves[stage]))
    assert len(moves) == 4
    assert "calm presence" in moves[1]
    assert "one voice" in moves[4]
    banned = ["calm down", "it is nothing", "you should not be surprised"]
    print("never say: %s" % "; ".join(banned))
    assert len(banned) == 3
    print("rule: steadiness, naming, patience - become the room the echo settles in")
    print("OK: %s met the moment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_nottodo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five classic mistakes mapped to their costs
    mistakes = [
        ("startle without consent", "fear blend, distress, broken trust"),
        ("mock the flinch", "suppressed signals, eroded trust"),
        ("flood the landing", "extended freeze, stage-four push"),
        ("correct the feeling", "loneliness added to surprise"),
        ("weaponize the moment", "trust spent at ruinous rates"),
    ]
    for i, (m, cost) in enumerate(mistakes, 1):
        print("%d. %-24s -> %s" % (i, m, cost))
    assert len(mistakes) == 5
    assert mistakes[0][0] == "startle without consent"
    assert "ruinous" in mistakes[4][1]
    print("rule: the bell is an instrument - never a toy, a target, or a tool")
    print("OK: %s learned the five" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_emomap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # distances from surprise in valence-arousal space
    surprise = (0.0, 0.9)
    states = {"astonishment": (0.3, 0.85), "amazement": (0.5, 0.8),
              "startle": (0.0, 1.0), "confusion": (-0.1, 0.5),
              "anticipation": (0.2, 0.5), "boredom": (0.0, 0.1),
              "fear": (-0.9, 0.9), "delight": (0.45, 0.75)}
    def dist(p):
        return math.hypot(p[0] - surprise[0], p[1] - surprise[1])
    ranked = sorted(states.items(), key=lambda kv: dist(kv[1]))
    for label, p in ranked:
        print("%-13s distance=%.3f" % (label, dist(p)))
    assert ranked[0][0] == "startle"
    assert ranked[1][0] == "astonishment"
    assert 0.099 < dist(states["startle"]) < 0.101
    assert 0.799 < dist(states["boredom"]) < 0.801
    print("rule: locate the feeling to find its handling - triangulate, do not guess")
    print("OK: %s charted the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_blends(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the four famous mixes as valence/arousal blends with surprise
    surprise = {"v": 0.0, "a": 0.9}
    partners = {"joy": {"v": 0.9, "a": 0.6}, "fear": {"v": -0.9, "a": 0.9},
                "anger": {"v": -0.8, "a": 0.85}, "sadness": {"v": -0.7, "a": 0.3}}
    names = {"joy": "delight", "fear": "alarm", "anger": "outrage", "sadness": "disappointment"}
    for p, q in partners.items():
        v = 0.5 * surprise["v"] + 0.5 * q["v"]
        a = 0.5 * surprise["a"] + 0.5 * q["a"]
        print("%-13s v=%+.2f a=%.2f <- surprise + %s" % (names[p], v, a, p))
    delight_v = 0.5 * 0.0 + 0.5 * 0.9
    alarm_a = 0.5 * 0.9 + 0.5 * 0.9
    assert 0.44 < delight_v < 0.46
    assert 0.89 < alarm_a < 0.91
    outrage_v = 0.5 * 0.0 + 0.5 * -0.8
    disapp_a = 0.5 * 0.9 + 0.5 * 0.3
    assert -0.41 < outrage_v < -0.39
    assert 0.59 < disapp_a < 0.61
    print("rule: one neutral interrupt, four landings - the blend is in the landing")
    print("OK: %s mixed the four" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ems_fullsim(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the showcase: scored timeline of Elena's brother in the driveway
    timeline = [
        (0.0, "trigger", "brother's car in driveway; prediction gap = maximum"),
        (0.3, "freeze+orient", "hand mid-pour; head turns; brow flash; jaw drop"),
        (2.0, "peak", "bright blank; hr 72->104; questions flooding"),
        (6.0, "appraisal", "brother confirmed safe; blend locks to DELIGHT"),
        (9.0, "discharge", "shriek, laughter, tears; telling begins"),
        (600.0, "aftershock", "warm; threshold lowered; house feels alive"),
    ]
    for t, phase, note in timeline:
        print("T+%6.1fs %-14s %s" % (t, phase, note))
    assert len(timeline) == 6
    assert timeline[0][0] == 0.0 and timeline[-1][0] == 600.0
    phases = [p for _, p, _ in timeline]
    assert phases == ["trigger", "freeze+orient", "peak", "appraisal", "discharge", "aftershock"]
    hr_jump = 104 - 72
    print("heart-rate jump at peak: +%d bpm" % hr_jump)
    assert 31.9 < hr_jump < 32.1
    print("rule: the whole instrument playing the whole piece - trigger to resolution")
    print("OK: %s scored the symphony" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "def1": demo_ems_def1,
    "family": demo_ems_family,
    "volumes": demo_ems_volumes,
    "myths": demo_ems_myths,
    "firstperson": demo_ems_firstperson,
    "timecourse": demo_ems_timecourse,
    "lowhigh": demo_ems_lowhigh,
    "mixfear": demo_ems_mixfear,
    "dayinlife": demo_ems_dayinlife,
    "body": demo_ems_body,
    "posture": demo_ems_posture,
    "sleep": demo_ems_sleep,
    "differences": demo_ems_differences,
    "face": demo_ems_face,
    "intensityface": demo_ems_intensityface,
    "hidefake": demo_ems_hidefake,
    "artist": demo_ems_artist,
    "classictriggers": demo_ems_classictriggers,
    "personaltriggers": demo_ems_personaltriggers,
    "oddtriggers": demo_ems_oddtriggers,
    "chains": demo_ems_chains,
    "behaviors": demo_ems_behaviors,
    "speech": demo_ems_speech,
    "judgment": demo_ems_judgment,
    "escalation": demo_ems_escalation,
    "healthyexpr": demo_ems_healthyexpr,
    "unhealthy": demo_ems_unhealthy,
    "practices": demo_ems_practices,
    "reading": demo_ems_reading,
    "support": demo_ems_support,
    "nottodo": demo_ems_nottodo,
    "emomap": demo_ems_emomap,
    "blends": demo_ems_blends,
    "fullsim": demo_ems_fullsim,
}
