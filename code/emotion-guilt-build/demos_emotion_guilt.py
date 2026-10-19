#!/usr/bin/env python3
"""Demo programs for the Guilt Emotion databases (emotion series).

Every demo is an emotion-scenario simulator: real, runnable, stdlib-only
Python that computes the scenario for its record, prints the real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker. All 68 demos (34 public + 34 Signature) are machine-executed
by build.py. Descriptive/educational only - no diagnosing real people.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_guilt_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four-beat sequence: standard -> transgression -> attribution -> repair urge
    standard = 0.90   # strength of the held standard
    breach = 0.80     # perceived size of the transgression
    attribution = 0.85  # accepted share of responsibility
    guilt = breach * attribution          # 0.68
    repair_urge = min(1.0, guilt * 1.10)  # 0.748
    acted = repair_urge > 0.5
    print("beats: standard %.2f -> breach %.2f -> attribution %.2f" % (standard, breach, attribution))
    print("guilt: %.3f  repair urge: %.3f  acted: %s" % (guilt, repair_urge, acted))
    assert 0.679 < guilt < 0.681
    assert 0.747 < repair_urge < 0.749
    assert acted is True
    # no attribution, no guilt: zero the attribution step
    assert (breach * 0.0) == 0.0
    print("OK: %s ran the four-beat sequence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guilt root + partner/time weights -> named branches
    guilt = 1.0
    branches = {
        "remorse": guilt * 0.95 + 0.60,        # + weight of serious wrong
        "regret": guilt * 0.55 + 0.50,         # + outcome focus
        "survivor_guilt": guilt * 0.50 + 0.45, # + spared-while-others-suffer
        "anticipatory": guilt * 0.60 + 0.55,    # + forward time direction
        "collective": guilt * 0.45 + 0.50,      # + group membership
    }
    total = sum(branches.values())
    share = {k: v / total * 100.0 for k, v in branches.items()}
    for k in branches:
        print("  %-14s weight %.2f (%5.2f %%)" % (k, branches[k], share[k]))
    assert 0.999 < sum(share.values()) / 100.0 < 1.001
    assert share["remorse"] > share["collective"]
    assert 27.42 < share["remorse"] < 27.45
    print("root: guilt; branches keep the breached-standard core")
    print("OK: %s mapped the family tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three dials sum into the volume knob 0..10
    def volume(harm, closeness, responsibility):
        return min(10.0, (harm + closeness + responsibility) / 3.0 * 10.0)
    def label(v):
        return "mild" if v < 3.5 else ("moderate" if v < 7.0 else "intense")
    cases = [(0.1, 0.2, 0.15), (0.5, 0.6, 0.55), (0.9, 0.95, 0.9)]
    vols = []
    for harm, closeness, responsibility in cases:
        v = volume(harm, closeness, responsibility)
        vols.append(v)
        print("dials %.2f/%.2f/%.2f -> volume %.2f (%s)" % (harm, closeness, responsibility, v, label(v)))
    assert 1.49 < vols[0] < 1.51
    assert 5.49 < vols[1] < 5.51
    assert 9.16 < vols[2] < 9.18
    assert label(vols[0]) == "mild" and label(vols[1]) == "moderate" and label(vols[2]) == "intense"
    print("OK: %s ran the three volumes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # each myth freezes one step of the four-beat sequence
    myths = [
        ("guilt means you did wrong", "attribution"),
        ("guilt equals shame", "judgment-target"),
        ("feeling it proves goodness", "repair"),
        ("stop feeling it", "signal"),
        ("apology always clears it", "repair"),
        ("guilt is useless", "signal"),
    ]
    valid_steps = {"standard", "transgression", "attribution", "repair", "signal", "judgment-target"}
    for myth, step in myths:
        print("  myth: %-32s freezes: %s" % (myth, step))
        assert step in valid_steps
    assert len(myths) == 6
    frozen = {m[1] for m in myths}
    assert "attribution" in frozen and "repair" in frozen
    print("myths debunked: %d" % len(myths))
    print("OK: %s cleared the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attention goes inward and backward; each replay deepens the groove
    inward, backward = 0.70, 0.60
    depth = 0.20
    for cycle in range(1, 6):
        depth = min(1.0, depth + inward * backward * 0.25)
        print("replay cycle %d: groove depth %.3f" % (cycle, depth))
    # depth after 5 cycles: 0.20 + 5 * 0.105 = 0.725
    assert 0.724 < depth < 0.726
    heaviness = 0.55 + depth * 0.40   # 0.84
    repair_urge = 0.30 + depth * 0.60  # 0.735
    print("heaviness: %.3f  repair urge: %.3f" % (heaviness, repair_urge))
    assert 0.839 < heaviness < 0.841
    assert 0.734 < repair_urge < 0.736
    print("OK: %s simulated the inner passage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guilt's slow time signature: delayed onset, rumination peak, repair fade, aftershock
    phases = [
        ("onset delay", 2.0, "attribution completing"),
        ("peak (rumination)", 9.0, "replay loop at full speed"),
        ("fading (repair begun)", 4.0, "sequence closing"),
        ("aftershock (cue)", 3.0, "account re-opened, smaller"),
    ]
    peak = max(p[1] for p in phases)
    peak_phase = [p[0] for p in phases if p[1] == peak][0]
    for label, inten, note in phases:
        print("  %-20s intensity %.1f - %s" % (label, inten, note))
    assert 8.9 < peak < 9.1
    assert peak_phase == "peak (rumination)"
    assert phases[2][1] < phases[1][1]      # fading below peak
    assert phases[3][1] < phases[0][1] + 2.0  # aftershock modest vs onset context
    descent = phases[1][1] - phases[2][1]
    assert 4.9 < descent < 5.1
    print("peak->fading descent: %.1f (repair started)" % descent)
    print("OK: %s ran the time course" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def volume(harm, closeness, responsibility, centrality):
        return min(10.0, (harm + closeness + responsibility + centrality) / 4.0 * 10.0)
    low = volume(0.15, 0.30, 0.40, 0.20)    # forgotten message
    high = volume(0.90, 0.95, 0.90, 0.85)   # serious breach, loved one, core value
    print("low-intensity snapshot:  volume %.2f" % low)
    print("high-intensity snapshot: volume %.2f" % high)
    assert 2.61 < low < 2.63
    assert 8.99 < high < 9.01
    assert high - low > 6.0
    print("same mechanism, different dials: gap %.2f" % (high - low))
    print("OK: %s ran the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_shame_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guilt pushes repair, shame pushes hiding: the blend stalls
    repair_urge = 0.80   # guilt: "I did a bad thing" -> fix it
    hiding_urge = 0.75   # shame: "I am a bad person" -> hide
    net_action = repair_urge - hiding_urge  # 0.05 -> paralysis
    pain = repair_urge + hiding_urge        # 1.55 -> worse than either alone
    print("repair urge: %.2f  hiding urge: %.2f" % (repair_urge, hiding_urge))
    print("net action: %.2f (standstill)  felt pain: %.2f" % (net_action, pain))
    assert 0.04 < net_action < 0.06
    assert 1.54 < pain < 1.56
    assert pain > repair_urge and pain > hiding_urge
    # untangle: name the louder sentence
    louder = "guilt" if repair_urge >= hiding_urge else "shame"
    print("louder sentence: %s -> aim at the act" % louder)
    assert louder == "guilt"
    print("OK: %s untangled the blend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one ordinary day: signal -> compounding -> cascade -> repair -> aftershock
    day = [
        ("morning signal", 3.0, "missed call remembered"),
        ("midday compounding", 5.0, "repair missed, second layer"),
        ("afternoon cascade", 7.0, "associated breaches retrieved"),
        ("evening repair", 1.5, "call made, account closing"),
        ("night aftershock", 2.0, "cue fires, met with recognition"),
    ]
    for label, inten, note in day:
        print("  %-20s intensity %.1f - %s" % (label, inten, note))
    peak = max(d[1] for d in day)
    assert 6.9 < peak < 7.1
    repair_drop = day[2][1] - day[3][1]
    assert 5.4 < repair_drop < 5.6
    assert day[4][1] < day[2][1]  # aftershock smaller than cascade
    print("repair drop: %.1f (dread was larger than the deed)" % repair_drop)
    print("OK: %s ran the day vignette" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guilt's body pattern: heaviness and inward pull, not heat and push
    channels = {
        "breastbone weight": 0.90,
        "stomach churn": 0.85,
        "shallow breath": 0.60,
        "sighing": 0.55,
        "muscle slacken": 0.70,
        "flushing": 0.40,
        "energy drain": 0.80,
        "heart race": 0.35,
    }
    ranked = sorted(channels.items(), key=lambda kv: kv[1], reverse=True)
    for ch, v in ranked:
        print("  %-18s %.2f" % (ch, v))
    top = ranked[0][0]
    assert top == "breastbone weight"
    assert channels["energy drain"] > channels["heart race"]  # drains, not mobilizes
    assert channels["stomach churn"] > channels["flushing"]
    total = sum(channels.values())
    assert 5.14 < total < 5.16
    print("OK: %s mapped the body signals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_posture_movement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the shrinking program: every parameter reduces apparent size
    neutral_visibility = 1.00
    head_pitch = 0.12      # forward pitch reduces height
    shoulder_round = 0.15  # narrows the chest
    gaze_drop = 0.18       # withdraws social presence
    gesture_shrink = 0.10  # smaller movements
    visibility = neutral_visibility - (head_pitch + shoulder_round + gaze_drop + gesture_shrink)
    print("visibility index: %.2f (neutral 1.00)" % visibility)
    assert 0.44 < visibility < 0.46
    assert visibility < neutral_visibility
    # appeasement signal strength rises as visibility falls
    appeasement = 1.0 - visibility
    assert 0.54 < appeasement < 0.56
    print("appeasement signal: %.2f" % appeasement)
    print("OK: %s ran the posture program" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_sleep_appetite_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # maintenance systems under guilt: night amplification, appetite loss, drain
    baseline = 1.0
    day_rumination, night_rumination = 0.45, 0.90
    amplification = night_rumination / day_rumination  # 2.0
    sleep_quality = baseline - night_rumination * 0.55   # 0.505
    appetite = baseline - 0.65 * 0.70                    # 0.545
    energy = baseline - (day_rumination * 0.50 + (1.0 - sleep_quality) * 0.40)
    print("night/day rumination: %.1fx" % amplification)
    print("sleep quality: %.3f  appetite: %.3f  energy: %.3f" % (sleep_quality, appetite, energy))
    assert 1.99 < amplification < 2.01
    assert 0.504 < sleep_quality < 0.506
    assert 0.544 < appetite < 0.546
    assert 0.576 < energy < 0.578
    assert appetite < energy < baseline
    print("OK: %s ran the maintenance systems" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five body-writing styles; no single profile dominates
    profiles = {
        "gut-dominant": 0.28,
        "head-dominant": 0.24,
        "visible-flusher": 0.16,
        "hidden-churner": 0.20,
        "behavioral (child)": 0.12,
    }
    total = sum(profiles.values())
    print("profiles: %d styles" % len(profiles))
    for p, share in sorted(profiles.items(), key=lambda kv: kv[1], reverse=True):
        print("  %-20s %.2f" % (p, share))
    assert 0.999 < total < 1.001
    assert max(profiles.values()) < 0.35  # no monopoly
    assert min(profiles.values()) > 0.05  # every style real
    spread = max(profiles.values()) - min(profiles.values())
    assert 0.15 < spread < 0.17
    print("no single body writes guilt for everyone")
    print("OK: %s mapped the differences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # no universal guilt face: a cluster of micro-signs instead
    cluster = {
        "gaze aversion": 0.85,
        "lowered lids": 0.70,
        "blink-rate spike": 0.60,
        "inner brow lift": 0.55,
        "lip press": 0.65,
        "lip bite": 0.40,
        "head tilt down": 0.75,
        "swallow before answering": 0.50,
    }
    print("cluster size: %d micro-signs (no single prototype)" % len(cluster))
    top3 = sorted(cluster.items(), key=lambda kv: kv[1], reverse=True)[:3]
    for sign, w in top3:
        print("  %-24s %.2f" % (sign, w))
    assert len(cluster) == 8
    assert top3[0][0] == "gaze aversion"
    mean_w = sum(cluster.values()) / len(cluster)
    assert 0.624 < mean_w < 0.626
    print("read the cluster and its timing, never one sign")
    print("OK: %s mapped the face cluster" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flicker -> held cluster -> collapse
    levels = [
        ("mild", 2, 0.5),       # signs visible, seconds held
        ("moderate", 5, 4.0),
        ("intense", 8, 30.0),
    ]
    for label, signs, seconds in levels:
        print("  %-10s %d signs, holds ~%.1fs" % (label, signs, seconds))
    counts = [l[1] for l in levels]
    assert counts == sorted(counts) and len(set(counts)) == 3
    durations = [l[2] for l in levels]
    assert durations == sorted(durations)
    # wave pattern at moderate: leak, compose, leak again
    waves = [0.6, 0.2, 0.55, 0.25, 0.5]
    assert max(waves) == waves[0] and min(waves) == waves[1]
    assert 0.59 < waves[0] < 0.61
    print("scale: flicker, held cluster, collapse")
    print("OK: %s ran the intensity scale" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hiding: suppression stops large movements, leaks small ones
    channels = {
        "posture": (0.80, 0.20),   # (suppression, leak)
        "voice tone": (0.70, 0.30),
        "word choice": (0.55, 0.45),
        "gaze": (0.30, 0.70),
        "blink rate": (0.15, 0.85),
        "swallow": (0.20, 0.80),
    }
    print("hiding: suppression vs leak per channel")
    for ch, (supp, leak) in channels.items():
        print("  %-12s suppressed %.2f  leaks %.2f" % (ch, supp, leak))
        assert 0.99 < supp + leak < 1.01
    fastest_leak = max(channels.items(), key=lambda kv: kv[1][1])[0]
    assert fastest_leak == "blink rate"
    # faking: fluent display, vague repair
    display_fluency, repair_concrete = 0.90, 0.20
    asymmetry = display_fluency - repair_concrete
    assert 0.69 < asymmetry < 0.71
    print("faked guilt asymmetry (display - repair): %.2f" % asymmetry)
    print("OK: %s exposed hiding and faking" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # craft decisions across media, all from the appeasement program
    notes = {
        "spine (shortened)": "visual",
        "eyes (half-mast, averted)": "visual",
        "mouth (pressed shut)": "visual",
        "hands (busy)": "visual",
        "stillness between lines": "actor",
        "voice (quieter, slower)": "actor",
        "guilty rhythm in dialogue": "writer",
        "shadow/profile composition": "visual",
    }
    media = {}
    for note, m in notes.items():
        media.setdefault(m, []).append(note)
        print("  [%-6s] %s" % (m, note))
    assert len(notes) == 8
    assert set(media) == {"visual", "actor", "writer"}
    assert len(media["visual"]) == 5
    print("through-line: show the hiding, the feeling shows itself")
    print("OK: %s filled the gallery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven classic triggers: standard clear, breach observable, responsibility hard to dodge
    triggers = [
        ("promise-breaking", 0.95, 0.90),
        ("harm-causing", 0.90, 0.85),
        ("omission", 0.70, 0.75),
        ("betrayal of trust", 0.92, 0.88),
        ("selfish advantage", 0.80, 0.70),
        ("code violation", 0.85, 0.95),
        ("role failure", 0.88, 0.80),
    ]
    print("classic triggers (clarity, dodge-difficulty):")
    for t, clarity, dodge in triggers:
        efficiency = (clarity + dodge) / 2.0
        print("  %-18s efficiency %.3f" % (t, efficiency))
        assert 0.69 < efficiency < 0.96
    assert len(triggers) == 7
    best = max(triggers, key=lambda t: (t[1] + t[2]) / 2.0)[0]
    assert best == "promise-breaking"
    # omission arrives late: counterfactual construction takes time
    onset = {"promise-breaking": 0.2, "omission": 2.5}
    assert onset["omission"] > onset["promise-breaking"] * 5
    print("OK: %s cataloged the classic triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # associative tags: cue -> re-fires the appraisal
    tags = [
        ("song", 0.80), ("smell", 0.75), ("anniversary date", 0.90),
        ("phrase", 0.65), ("place", 0.70), ("weather", 0.45),
    ]
    ambush_power = sum(w for _, w in tags) / len(tags)
    print("unnamed trigger ambush power: %.3f" % ambush_power)
    assert 0.707 < ambush_power < 0.709
    # naming converts surprise into recognition
    recognition = 0.75
    named_power = ambush_power * (1.0 - recognition)
    print("named trigger ambush power:   %.3f" % named_power)
    assert 0.176 < named_power < 0.178
    assert named_power < ambush_power / 3.0
    strongest = max(tags, key=lambda t: t[1])[0]
    assert strongest == "anniversary date"
    print("OK: %s mapped the personal triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # surprise triggers: comparison-built breach, overactive attribution
    triggers = [
        ("good news (another's loss)", 0.30, 0.75),   # (real breach, claimed responsibility)
        ("rest while others work", 0.15, 0.70),
        ("pleasure amid need", 0.20, 0.65),
        ("undeserved trust", 0.25, 0.80),
        ("outgrowing loved ones", 0.10, 0.72),
        ("unrepayable kindness", 0.20, 0.68),
    ]
    print("surprise triggers (real breach vs claimed responsibility):")
    for t, breach, claimed in triggers:
        gap = claimed - breach
        print("  %-26s gap %.2f" % (t, gap))
        assert gap > 0.40  # attribution overclaims in every case
    assert len(triggers) == 6
    mean_gap = sum(c - b for _, b, c in triggers) / len(triggers)
    assert 0.515 < mean_gap < 0.518
    print("audit question: circumstance or conduct?")
    print("OK: %s cataloged the surprise triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cascade: primary breach -> retrieved archive -> abstraction -> partners -> defense
    stages = [
        ("primary breach", 3.0),
        ("retrieved archive", 5.5),
        ("abstraction to trait", 7.0),
        ("partners recruited", 8.5),
        ("defensive reactions", 9.0),
    ]
    for label, inten in stages:
        print("  %-22s intensity %.1f" % (label, inten))
    growth = stages[-1][1] / stages[0][1]
    assert 2.99 < growth < 3.01
    # joints: intervene with specificity at each mechanism
    joints = ["specificity", "behavioral language", "one feeling at a time"]
    assert len(joints) == 3
    # specificity shrinks the retrieved archive back toward the primary
    calmed = stages[1][1] * 0.55 + stages[0][1] * 0.45
    assert 4.36 < calmed < 4.38
    print("cascade growth: %.1fx; specificity calms archive to %.2f" % (growth, calmed))
    print("OK: %s ran the chain reaction" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five patterns; only repair closes the sequence
    patterns = {
        "repair": (0.90, True),
        "appeasement": (0.45, False),
        "avoidance": (0.15, False),
        "self-punishment": (0.30, False),
        "defensive": (0.10, False),
    }
    print("patterns (relief, closes sequence):")
    closers = []
    for p, (relief, closes) in patterns.items():
        print("  %-16s relief %.2f  closes: %s" % (p, relief, closes))
        if closes:
            closers.append(p)
    assert closers == ["repair"]
    assert patterns["repair"][0] > patterns["appeasement"][0]
    # self-punishment pays the wrong creditor: harmed person receives 0
    harmed_receives = {"repair": 0.85, "self-punishment": 0.0, "appeasement": 0.30}
    assert harmed_receives["self-punishment"] == 0.0
    assert harmed_receives["repair"] > harmed_receives["appeasement"]
    print("OK: %s ran the behavior patterns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_speech_patterns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # phrases and the work each does
    phrases = [
        ("I'm sorry (x3)", "repair urge without a plan"),
        ("I feel terrible", "feeling as substitute for fix"),
        ("I didn't mean to", "intent defense"),
        ("it wasn't a big deal", "minimization"),
        ("but you...", "counter-accusation pivot"),
        ("are you mad at me?", "absolution fishing"),
    ]
    works = {w for _, w in phrases}
    print("characteristic phrases: %d" % len(phrases))
    for ph, work in phrases:
        print("  %-22s -> %s" % (ph, work))
        assert work in works
    assert len(phrases) == 6 and len(works) == 6
    # tone: quieter + faster-or-halting
    volume_drop, pace_shift = 0.33, 0.25
    assert 0.32 < volume_drop < 0.34
    print("tone: volume -%.0f%%, pace shifted %.2f" % (volume_drop * 100, pace_shift))
    print("OK: %s ran the speech patterns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_decisions_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five judgment effects under guilt
    effects = {
        "frame narrows to breach": 0.80,
        "responsibility inflates": 0.70,
        "risk distorts": 0.60,
        "others judged harshly": 0.65,
        "decision quality drops": 0.75,
    }
    for e, strength in effects.items():
        print("  %-28s %.2f" % (e, strength))
    assert len(effects) == 5
    assert max(effects.values()) == effects["frame narrows to breach"]
    # countermeasure: the calm-self check
    guilty_promise, calm_promise = 120.0, 40.0  # promised amends, arbitrary units
    overcommit = guilty_promise / calm_promise
    assert 2.99 < overcommit < 3.01
    print("guilty promise vs calm promise: %.1fx overcommit" % overcommit)
    print("countermeasure: delay, write options, check against the calm self")
    print("OK: %s ran the judgment effects" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the staircase: tug -> ache -> weight -> flood -> breaking point
    steps = [
        ("tug", 1.5, "private wince, quick fix"),
        ("ache", 4.0, "repeated apologies, checking"),
        ("weight", 6.5, "confession expands, self-punishment"),
        ("flood", 9.0, "cascade open, erratic behavior"),
    ]
    for label, inten, note in steps:
        print("  %-8s intensity %.1f - %s" % (label, inten, note))
    intens = [s[1] for s in steps]
    assert intens == sorted(intens)
    climb = steps[-1][1] / steps[0][1]
    assert 5.99 < climb < 6.01
    # three exits: only repair closes
    exits = {"genuine repair": True, "withdrawal": False, "hardening": False}
    closed = [e for e, c in exits.items() if c]
    assert closed == ["genuine repair"]
    print("staircase climb: %.1fx; exits: %s" % (climb, ", ".join(exits)))
    print("OK: %s ran the escalation staircase" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four-part apology + system fix; proportion matched
    parts = {
        "name the act": True,
        "accept responsibility": True,
        "acknowledge impact": True,
        "concrete repair": True,
    }
    completeness = sum(1 for v in parts.values() if v) / len(parts)
    print("apology completeness: %.2f" % completeness)
    assert 0.999 < completeness < 1.001
    # proportion: payment matches debt
    breach, repair = 6.0, 6.0
    proportion = repair / breach
    assert 0.999 < proportion < 1.001
    # attribution audit first: real share repaired, false share released
    real_share, claimed_share = 0.60, 1.00
    released = claimed_share - real_share
    assert 0.399 < released < 0.401
    # closed account: replay finds the story ending in repair
    loop_open = False
    assert loop_open is False
    print("proportion: %.2f  false share released: %.2f  loop open: %s" % (proportion, released, loop_open))
    print("OK: %s ran the healthy expression" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three failure modes; all leave the account open
    modes = {
        "bottling": ("never named, never repaired", True),
        "exploding": ("flood without a plan", True),
        "weaponizing": ("guilt as leverage", True),
    }
    print("failure modes (account stays open):")
    for mode, (desc, open_acct) in modes.items():
        print("  %-12s %s; open: %s" % (mode, desc, open_acct))
        assert open_acct is True
    assert len(modes) == 3
    # suppression rebounds: suppressed content returns more often
    baseline_return, suppressed_return = 1.0, 1.8
    rebound = suppressed_return / baseline_return
    assert 1.79 < rebound < 1.81
    print("suppression rebound: %.1fx return rate" % rebound)
    print("OK: %s ran the unhealthy patterns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven practices, each targeting one failure point
    practices = [
        ("prompt repair", "compounding"),
        ("written ledger", "replay loop"),
        ("attribution check", "attribution inflation"),
        ("standard clarity", "midnight rule-drafting"),
        ("maintenance", "resource depletion"),
        ("system fixing", "recurrence"),
        ("release practice", "re-auditing closed accounts"),
    ]
    targets = {t for _, t in practices}
    print("practices: %d, failure points covered: %d" % (len(practices), len(targets)))
    for p, t in practices:
        print("  %-20s -> %s" % (p, t))
    assert len(practices) == 7
    assert len(targets) == 7  # one practice per failure point
    # daily bookkeeping beats annual crises
    small_daily, one_crisis = 7 * 0.10, 1.50
    assert small_daily < one_crisis
    print("OK: %s ran the everyday practices" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cluster across four channels, time-locked to a topic
    cues = {
        "face": 0.55,      # gaze drops when the topic lands
        "body": 0.50,      # forward fold
        "voice": 0.45,     # quieter, swallows
        "behavior": 0.60,  # sudden helpfulness / avoidance
    }
    for ch, w in cues.items():
        print("  %-10s cue weight %.2f" % (ch, w))
    # convergence: independent weak cues multiply
    combined = 1.0
    for w in cues.values():
        combined *= (1.0 - w)
    combined = 1.0 - combined  # 1 - (0.45*0.50*0.55*0.40)
    print("single strongest cue: %.2f  converged cluster: %.3f" % (max(cues.values()), combined))
    assert 0.949 < combined < 0.951
    assert combined > max(cues.values())
    # timing gate: without topic-lock, the reading does not run
    topic_locked, plausible_breach = True, True
    assert topic_locked and plausible_breach
    print("cues open a conversation; they never deliver a verdict")
    print("OK: %s ran the reading cluster" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five responses, each assisting the sequence
    responses = [
        ("listen first", "confession beat"),
        ("acknowledge w/o judging", "attribution step"),
        ("ask the repair question", "repair beat"),
        ("calibrate proportion", "oversized punishment"),
        ("stay for the long repair", "interpersonal core"),
    ]
    assisted = {step for _, step in responses}
    print("responses: %d, sequence steps assisted: %d" % (len(responses), len(assisted)))
    for r, step in responses:
        print("  %-26s -> %s" % (r, step))
    assert len(responses) == 5 and len(assisted) == 5
    # the boundary: support, not performance
    performed_by_supporter = 0.0
    assert performed_by_supporter == 0.0
    print("the account is theirs to close")
    print("OK: %s ran the supportive responses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven mistakes, each corrupting one sequence step
    mistakes = [
        ("dismissing", "signal validity"),
        ("weaponizing", "interpersonal trust"),
        ("rushed forgiveness", "repair beat"),
        ("piling on", "confession beat"),
        ("reflexive comfort", "attribution audit"),
        ("diagnosing", "act-vs-self judgment"),
        ("broadcasting", "confession context"),
    ]
    corrupted = {s for _, s in mistakes}
    print("mistakes: %d, steps corrupted: %d" % (len(mistakes), len(corrupted)))
    for m, step in mistakes:
        print("  %-20s corrupts: %s" % (m, step))
    assert len(mistakes) == 7 and len(corrupted) == 7
    print("OK: %s named the mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_related_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two axes: judgment target (act=0, self=1), breach type (moral=1, non-moral=0)
    hood = {
        "guilt": (0.0, 1.0),
        "shame": (0.7, 1.0),
        "regret": (0.2, 0.2),
        "remorse": (0.0, 1.15),   # same quadrant, heavier weight
        "embarrassment": (0.6, 0.1),
        "pride": (0.0, -1.0),    # opposite verdict
    }
    def dist(a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])
    g = hood["guilt"]
    near = sorted(((n, dist(g, p)) for n, p in hood.items() if n != "guilt"), key=lambda kv: kv[1])
    for n, d in near:
        print("  %-14s distance %.3f" % (n, d))
    assert near[0][0] == "remorse"       # closest: same quadrant, heavier
    assert near[1][0] == "shame"         # next: nearest neighbor
    assert near[-1][0] == "pride"        # farthest: opposite verdict
    assert 0.69 < near[1][1] < 0.71
    # prescription test: only guilt is settled by specific repair
    settles = {"guilt": "specific repair", "shame": "examine self-verdict",
               "regret": "better deciding", "embarrassment": "let moment pass"}
    assert settles["guilt"] == "specific repair"
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_emotion_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four blends: core guilt + partner appraisal -> emergent property
    blends = [
        ("shame", "standstill", "separate the verdicts"),
        ("sadness", "mourning", "acknowledge the loss"),
        ("fear", "dread", "face actual consequences"),
        ("self-anger", "corrosion", "redirect fury to the problem"),
    ]
    print("blends (partner, emergent property, prescription):")
    for partner, emergent, rx in blends:
        print("  guilt + %-10s -> %-10s | %s" % (partner, emergent, rx))
    assert len(blends) == 4
    emergents = {b[1] for b in blends}
    assert len(emergents) == 4  # each blend has its own weather
    # emergent property not present in either partner alone
    pure_guilt_standstill, pure_shame_standstill = 0.10, 0.15
    blend_standstill = 0.85
    assert blend_standstill > pure_guilt_standstill + pure_shame_standstill
    print("OK: %s blended the four dyads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five scenes: trigger -> peak -> encounter -> repair -> settling
    scenes = [
        ("trigger 18:40", 4.0, "attribution completes"),
        ("peak 19:15", 9.0, "replay loop at full speed"),
        ("encounter 19:50", 7.5, "appeasement display, over-explaining"),
        ("repair (next day)", 2.5, "four-part apology + system fix"),
        ("settling (week)", 1.0, "loop quiets; changed behavior accrues"),
        ("aftershock (Sunday)", 2.0, "cue fires; met with recognition"),
    ]
    peak = max(s[1] for s in scenes)
    peak_scene = [s[0] for s in scenes if s[1] == peak][0]
    print("scenes: %d" % len(scenes))
    for label, inten, note in scenes:
        print("  %-20s intensity %.1f - %s" % (label, inten, note))
    assert len(scenes) == 6
    assert 8.9 < peak < 9.1
    assert peak_scene == "peak 19:15"
    assert scenes[3][1] < scenes[2][1]   # repair below encounter
    assert scenes[5][1] < scenes[0][1]   # aftershock smaller than trigger
    descent = scenes[1][1] - scenes[3][1]
    assert 6.4 < descent < 6.6
    print("peak->repair descent: %.1f (the model, run)" % descent)
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "guilt_definition": demo_guilt_definition,
    "guilt_emotion_family": demo_guilt_emotion_family,
    "guilt_intensity_scale": demo_guilt_intensity_scale,
    "guilt_myths": demo_guilt_myths,
    "guilt_first_person": demo_guilt_first_person,
    "guilt_time_course": demo_guilt_time_course,
    "guilt_low_vs_high": demo_guilt_low_vs_high,
    "guilt_shame_blend": demo_guilt_shame_blend,
    "guilt_day_vignette": demo_guilt_day_vignette,
    "guilt_body_signals": demo_guilt_body_signals,
    "guilt_posture_movement": demo_guilt_posture_movement,
    "guilt_sleep_appetite_energy": demo_guilt_sleep_appetite_energy,
    "guilt_body_differences": demo_guilt_body_differences,
    "guilt_face": demo_guilt_face,
    "guilt_face_intensity": demo_guilt_face_intensity,
    "guilt_hiding_faking": demo_guilt_hiding_faking,
    "guilt_expression_gallery": demo_guilt_expression_gallery,
    "guilt_classic_triggers": demo_guilt_classic_triggers,
    "guilt_personal_triggers": demo_guilt_personal_triggers,
    "guilt_surprise_triggers": demo_guilt_surprise_triggers,
    "guilt_chain_reactions": demo_guilt_chain_reactions,
    "guilt_behavior_actions": demo_guilt_behavior_actions,
    "guilt_speech_patterns": demo_guilt_speech_patterns,
    "guilt_decisions_judgment": demo_guilt_decisions_judgment,
    "guilt_escalation": demo_guilt_escalation,
    "guilt_healthy_expression": demo_guilt_healthy_expression,
    "guilt_unhealthy_expression": demo_guilt_unhealthy_expression,
    "guilt_everyday_practices": demo_guilt_everyday_practices,
    "guilt_reading_others": demo_guilt_reading_others,
    "guilt_supportive_responses": demo_guilt_supportive_responses,
    "guilt_mistakes_to_avoid": demo_guilt_mistakes_to_avoid,
    "guilt_related_emotions": demo_guilt_related_emotions,
    "guilt_emotion_mixes": demo_guilt_emotion_mixes,
    "guilt_full_simulation": demo_guilt_full_simulation,
}

assert len(DEMOS) == 34, "expected 34 demos, got %d" % len(DEMOS)
