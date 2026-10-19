#!/usr/bin/env python3
"""Demo programs for the Pride Emotion databases (emotion series).

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


def demo_pride_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # three-beat appraisal: achievement, ownership, self-worth -> pride
    appraisal = {"achievement": 0.90, "ownership": 0.85, "self_worth": 0.80}
    signal = sum(appraisal.values()) / len(appraisal)
    authentic = min(1.0, signal * 1.10)          # effort-based attribution
    hubristic = min(1.0, signal * 0.60 + 0.35)   # superiority-based attribution
    print("appraisal signal: %.3f" % signal)
    print("authentic pride: %.3f  hubristic pride: %.3f" % (authentic, hubristic))
    assert 0.849 < signal < 0.852
    assert 0.934 < authentic < 0.937
    assert authentic > hubristic > 0.80
    print("beats: achievement -> ownership -> self-worth")
    print("OK: %s ran the three-beat appraisal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # self-conscious family: pride branches by appraisal type
    pride = 1.0
    branches = {
        "authentic": pride * 0.85 + 0.70,    # effort-specific appraisal
        "hubristic": pride * 0.75 + 0.55,    # global superiority appraisal
        "joy_rider": pride * 0.60 + 0.50,    # pleasure current partner
        "contentment": pride * 0.45 + 0.40,  # settled background partner
    }
    total = sum(branches.values())
    share = {k: v / total * 100.0 for k, v in branches.items()}
    for k in branches:
        print("  %-12s weight %.2f (%5.2f %%)" % (k, branches[k], share[k]))
    assert 0.999 < sum(share.values()) / 100.0 < 1.001
    assert share["authentic"] > share["hubristic"] > share["contentment"]
    print("OK: %s branched the self-conscious family" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_volumes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # volume dials: stakes, ownership, audience -> intensity
    volumes = {
        "glow":  {"stakes": 0.20, "ownership": 1.00, "audience": 0.10},
        "swell": {"stakes": 0.60, "ownership": 1.00, "audience": 0.50},
        "blaze": {"stakes": 1.00, "ownership": 1.00, "audience": 1.00},
    }
    out = {}
    for v, d in volumes.items():
        intensity = (d["stakes"] * 0.45 + d["ownership"] * 0.35 + d["audience"] * 0.20)
        out[v] = intensity
        print("  %-6s intensity %.3f" % (v, intensity))
    assert out["glow"] < out["swell"] < out["blaze"]
    assert 0.45 < out["glow"] < 0.47
    assert 0.71 < out["swell"] < 0.73
    assert 0.99 < out["blaze"] < 1.01
    print("OK: %s scaled the three volumes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five myths, each scored against the two-face evidence: 1 = busted
    myths = {
        "pride is always bad": 1,
        "pride equals arrogance": 1,
        "pride cannot coexist with humility": 1,
        "pride needs an audience": 1,
        "proud means better than everyone": 1,
    }
    busted = sum(myths.values())
    rate = busted / len(myths)
    for m, b in myths.items():
        print("  myth busted: %-38s %s" % (m, bool(b)))
    print("myth-bust rate: %.2f" % rate)
    assert busted == 5
    assert 0.999 < rate < 1.001
    print("OK: %s cleared the five myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # six beats of the first-person passage: inner voltage over time
    beats = ["disbelief", "evidence", "warmth", "release", "replay", "generosity"]
    voltage = [0.30, 0.55, 0.80, 0.85, 1.00, 0.95]
    for b, v in zip(beats, voltage):
        print("  %-12s voltage %.2f" % (b, v))
    peak = max(voltage)
    assert voltage[:5] == sorted(voltage[:5])  # rise to the replay peak
    assert 0.99 < peak < 1.01
    assert voltage[-1] > 0.90  # generosity plateau stays high
    print("peak voltage: %.2f at '%s'" % (peak, beats[voltage.index(peak)]))
    print("OK: %s walked the six beats" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # onset fast, peak delayed (ownership accounting), graceful fade, aftershock echo
    t_onset, t_peak = 0.2, 1.5          # hours after the event
    peak = 1.0
    half_life = 36.0                    # hours: authentic pride fades slowly
    t = 72.0
    faded = peak * 0.5 ** (t / half_life)
    aftershock = 0.35 * peak            # reminder-triggered echo
    hubris_drop = peak * 0.5 ** (t / 4.0)  # hubristic: applause rented, fades fast
    print("onset %.1fh  peak %.1fh  faded@72h %.3f" % (t_onset, t_peak, faded))
    print("aftershock echo %.2f  hubristic remainder %.4f" % (aftershock, hubris_drop))
    assert t_peak > t_onset
    assert 0.24 < faded < 0.26
    assert aftershock < peak
    assert hubris_drop < 0.001
    assert faded > hubris_drop * 100
    print("OK: %s traced onset-peak-fade-aftershock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # same appraisal, different dial settings: the shelf vs the stage
    low = {"stakes": 0.15, "ownership": 1.0, "audience": 0.05, "label": "shelf"}
    high = {"stakes": 1.00, "ownership": 1.0, "audience": 1.00, "label": "stage"}
    def intensity(d):
        return d["stakes"] * 0.45 + d["ownership"] * 0.35 + d["audience"] * 0.20
    il, ih = intensity(low), intensity(high)
    print("  shelf intensity %.3f  stage intensity %.3f" % (il, ih))
    print("  ratio stage/shelf: %.1fx" % (ih / il))
    assert ih > il
    assert 2.3 < ih / il < 2.4
    assert 0.42 < il < 0.44
    assert 0.99 < ih < 1.01
    print("OK: %s compared low vs high intensity" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_triumph_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # triumph = pride ownership structure + joy pleasure current
    pride, joy = 0.90, 0.85
    triumph = 0.55 * pride + 0.45 * joy + 0.10 * pride * joy  # synergy term
    print("pride %.2f  joy %.2f  triumph %.3f" % (pride, joy, triumph))
    assert triumph > pride and triumph > joy
    assert 0.94 < triumph < 0.96
    synergy = 0.10 * pride * joy
    assert 0.076 < synergy < 0.078
    print("synergy bonus: %.3f" % synergy)
    print("OK: %s blended pride and joy into triumph" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_day_in_life(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # hourly pride trace across an ordinary day (6:00-22:00)
    trace = [0.05, 0.10, 0.35, 0.30, 0.25, 0.55, 0.60, 0.50,
             0.40, 0.45, 0.65, 0.55, 0.40, 0.35, 0.30, 0.45, 0.50]
    hours = len(trace)
    pride_minutes = sum(trace) * 60.0
    peak = max(trace)
    avg = sum(trace) / hours
    print("hours tracked: %d  peak %.2f  avg %.3f" % (hours, peak, avg))
    print("total pride-minutes: %.1f" % pride_minutes)
    assert hours == 17
    assert 0.64 < peak < 0.66
    assert 400.0 < pride_minutes < 430.0
    assert avg > 0.35  # an ordinary good day, well stocked
    print("OK: %s integrated a day of pride" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # body channel activations during authentic pride (0-1 scale)
    channels = {
        "chest_expansion": 0.90,
        "heart_warm_lift": 0.55,
        "breath_depth": 0.75,
        "shoulder_release": 0.80,
        "skin_flush": 0.30,
        "gut_churn": 0.05,
        "clean_energy": 0.85,
    }
    for c, v in channels.items():
        print("  %-16s %.2f" % (c, v))
    top = max(channels, key=channels.get)
    assert top == "chest_expansion"
    assert channels["gut_churn"] < 0.10  # pride is not a gut-churning emotion
    assert channels["clean_energy"] > 0.80
    mean_up = sum(v for k, v in channels.items() if k != "gut_churn") / 6
    assert 0.69 < mean_up < 0.71
    print("OK: %s mapped the body on pride" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # posture parameters -> pride display score
    spine_tall = 0.90      # 0 slouch .. 1 full height
    chest_open = 0.85
    head_tilt_deg = 4.0    # diagnostic range 3-5
    arms_away = 0.70
    stride_gain = 0.60
    score = (0.30 * spine_tall + 0.25 * chest_open +
             0.20 * (1.0 - abs(head_tilt_deg - 4.0) / 4.0) +
             0.15 * arms_away + 0.10 * stride_gain)
    print("head tilt %.1f deg  display score %.3f" % (head_tilt_deg, score))
    assert 3.0 <= head_tilt_deg <= 5.0
    assert 0.84 < score < 0.86
    # shame posture mirror: invert spine and tilt
    shame_score = (0.30 * (1 - spine_tall) + 0.25 * (1 - chest_open))
    assert shame_score < 0.15
    print("OK: %s scored the pride posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_sleep_appetite_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # maintenance ledger: authentic surplus vs hubristic borrowed energy
    authentic = {"sleep_ease": 0.80, "appetite_steady": 0.90, "energy_next_day": 0.75}
    hubristic = {"sleep_ease": 0.45, "appetite_steady": 0.70, "energy_next_day": -0.40}
    a_total = sum(authentic.values())
    h_total = sum(hubristic.values())
    print("authentic maintenance %.2f  hubristic maintenance %.2f" % (a_total, h_total))
    assert a_total > 2.40
    assert authentic["energy_next_day"] > 0 > hubristic["energy_next_day"]
    assert h_total < a_total / 2
    # the motivational aftereffect: next effort feels cheaper
    effort_cost = 1.0 - 0.5 * authentic["energy_next_day"]
    assert 0.61 < effort_cost < 0.64
    print("next-effort perceived cost: %.2f" % effort_cost)
    print("OK: %s balanced sleep, appetite, and energy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_bodies_differ(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five people, same feeling, different display gain
    people = {
        "expressive": 1.00,
        "open": 0.80,
        "balanced": 0.60,
        "reserved": 0.35,
        "quiet": 0.20,
    }
    base_signal = 0.85  # the shared inner pride
    shown = {p: base_signal * g for p, g in people.items()}
    for p, v in shown.items():
        print("  %-10s shown %.3f" % (p, v))
    assert all(v > 0 for v in shown.values())
    assert shown["expressive"] > shown["quiet"] * 4
    # calibration: divide by gain to recover the true signal
    recovered = {p: v / people[p] for p, v in shown.items()}
    assert all(abs(v - base_signal) < 0.001 for v in recovered.values())
    print("calibrated true signal: %.2f for all five" % base_signal)
    print("OK: %s calibrated five different bodies" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # facial action recipe for pride: quiet face + lifted head
    face = {
        "lip_press": 0.70,
        "corner_lift_mm": 1.5,
        "gaze_direct": 0.90,
        "brow_furrow": 0.00,
        "head_tilt_deg": 4.0,
        "cheek_lift": 0.40,
    }
    for k, v in face.items():
        print("  %-16s %s" % (k, v))
    assert face["brow_furrow"] == 0.00  # pride never knits the brow
    assert 3.0 <= face["head_tilt_deg"] <= 5.0
    assert face["gaze_direct"] > 0.85  # willing to be seen
    recognition = 0.45 * face["gaze_direct"] + 0.35 * (face["head_tilt_deg"] / 5.0) + 0.20 * face["lip_press"]
    assert 0.82 < recognition < 0.84
    print("face-only recognition: %.3f (full signal with torso is higher)" % recognition)
    print("OK: %s composed the face of pride" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # ordered progression: lip press -> smile -> grin; level -> tilt -> open lift
    stages = {
        "low":      {"smile": 0.15, "tilt": 0.0, "grin": 0.00},
        "moderate": {"smile": 0.60, "tilt": 3.5, "grin": 0.00},
        "high":     {"smile": 1.00, "tilt": 6.0, "grin": 0.85},
    }
    for s, f in stages.items():
        print("  %-8s smile %.2f  tilt %.1f  grin %.2f" % (s, f["smile"], f["tilt"], f["grin"]))
    assert stages["low"]["smile"] < stages["moderate"]["smile"] < stages["high"]["smile"]
    assert stages["low"]["tilt"] < stages["moderate"]["tilt"] < stages["high"]["tilt"]
    assert stages["high"]["grin"] > 0.80  # containment threshold crossed
    assert stages["moderate"]["grin"] == 0.00  # still containable
    print("OK: %s scaled the face across intensities" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # suppression races expression: the leak is the head start
    expression_onset_ms = 120.0
    suppression_onset_ms = 420.0
    leak_window_ms = suppression_onset_ms - expression_onset_ms
    leak_prob = min(1.0, leak_window_ms / 500.0)
    # faked pride: overshoot gain + stiffness
    real_gain, fake_gain = 1.00, 1.45
    real_ease, fake_ease = 0.90, 0.35
    print("leak window %.0f ms  leak probability %.2f" % (leak_window_ms, leak_prob))
    print("real gain %.2f ease %.2f | fake gain %.2f ease %.2f" % (real_gain, real_ease, fake_gain, fake_ease))
    assert leak_window_ms > 200.0
    assert 0.59 < leak_prob < 0.61
    assert fake_gain > real_gain * 1.3  # the overshoot tell
    assert fake_ease < real_ease / 2     # the stiffness tell
    print("OK: %s caught the leaks and the fakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # tilt calibration for the artist: neutral <3, pride 3-5, arrogance drift >5
    def zone(tilt):
        if tilt < 3.0:
            return "neutral"
        if tilt <= 5.0:
            return "pride"
        return "arrogance-drift"
    tests = {1.5: "neutral", 4.0: "pride", 8.0: "arrogance-drift"}
    for tilt, want in tests.items():
        got = zone(tilt)
        print("  tilt %4.1f deg -> %s" % (tilt, got))
        assert got == want
    print("OK: %s calibrated the gallery tilt" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # six classic triggers: strength = achievement * ownership * self-worth
    triggers = {
        "personal accomplishment": (0.95, 1.00, 0.85),
        "recognition": (0.80, 0.85, 1.00),
        "mastery moment": (0.90, 1.00, 0.80),
        "helping others succeed": (0.85, 0.80, 0.90),
        "group win": (0.90, 0.70, 0.85),
        "living up to a standard": (0.80, 1.00, 0.95),
    }
    strengths = {}
    for t, (a, o, s) in triggers.items():
        strengths[t] = a * o * s
        print("  %-24s strength %.3f" % (t, strengths[t]))
    top = max(strengths, key=strengths.get)
    assert top == "personal accomplishment"
    assert 0.80 < strengths[top] < 0.82
    # remove ownership: pride shrinks even when achievement stays
    shrunk = 0.95 * 0.20 * 0.85
    assert shrunk < strengths[top] / 3
    print("ownership removed: strength %.3f (collapsed)" % shrunk)
    print("OK: %s fired the six classic triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # resonance = cue_strength * memory_clarity * years_held
    cues = {
        "grandparent workshop": (0.95, 0.90, 30.0),
        "quit-day anniversary": (0.80, 0.85, 5.0),
        "old notebook": (0.70, 0.75, 12.0),
        "generic trophy": (0.50, 0.60, 8.0),
    }
    resonance = {}
    for c, (cue, clarity, years) in cues.items():
        resonance[c] = cue * clarity * math.log1p(years)
        print("  %-22s resonance %.3f" % (c, resonance[c]))
    top = max(resonance, key=resonance.get)
    assert top == "grandparent workshop"
    assert resonance[top] > resonance["generic trophy"] * 2
    assert 2.9 < resonance[top] < 3.0
    print("OK: %s resonated the personal triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # surprise model: appraisal * (1 - expectation) -- unexpected lands whole
    base_appraisal = 0.85
    events = {
        "expected annual praise": 0.90,
        "rival compliment": 0.05,
        "stranger thanks": 0.10,
        "child imitation": 0.02,
    }
    felt = {}
    for e, exp in events.items():
        felt[e] = base_appraisal * (1.0 - exp)
        print("  %-24s felt %.3f" % (e, felt[e]))
    assert felt["child imitation"] > felt["expected annual praise"] * 8
    assert 0.83 < felt["child imitation"] < 0.84
    assert 0.084 < felt["expected annual praise"] < 0.086
    print("OK: %s amplified the surprises" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # iterate appraisals: output becomes the next round's prior
    def run(attribution, rounds=4):
        standing, history = 0.50, []
        for _ in range(rounds):
            if attribution == "effort":
                standing = standing + 0.12 * standing   # calibrated growth
            else:
                standing = standing + 0.25 * standing   # superiority overreach
            history.append(standing)
        return history
    healthy = run("effort")
    fragile = run("superiority")
    for i, (h, f) in enumerate(zip(healthy, fragile)):
        print("  round %d  healthy %.3f  fragile %.3f" % (i + 1, h, f))
    assert healthy[-1] < fragile[-1]          # fragile overshoots...
    assert healthy[-1] < 1.00                # ...but healthy stays calibrated
    assert fragile[-1] > 1.10                # fragile leaves the evidence behind
    print("OK: %s ran the chain reactions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_behavior(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # action urge strengths under authentic pride
    actions = {
        "share the news": 0.90,
        "take up space": 0.70,
        "repeat winning behavior": 0.85,
        "mentor someone": 0.75,
        "display the evidence": 0.60,
        "raise the bar": 0.80,
        "diminish others": 0.05,
    }
    for a, u in actions.items():
        print("  %-22s urge %.2f" % (a, u))
    top = max(actions, key=actions.get)
    assert top == "share the news"
    assert actions["diminish others"] < 0.10  # the hubristic tell, absent here
    generous = actions["mentor someone"] + actions["share the news"]
    assert 1.64 < generous < 1.66
    print("OK: %s moved through the pride actions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # effort-words vs self-words in the first thirty seconds
    authentic_utterance = ("we pulled it off after those early mornings, "
                           "the third attempt finally held, priya's data saved us")
    hubristic_utterance = ("i am just built different, nobody else could have, "
                           "i carried the whole thing")
    effort_words = {"mornings", "attempt", "held", "data", "early", "pulled"}
    self_words = {"i", "built", "different", "nobody", "carried"}
    def count(words, text):
        toks = text.lower().split()
        return sum(1 for t in toks if t.strip(",.") in words)
    ae, ase = count(effort_words, authentic_utterance), count(self_words, authentic_utterance)
    he, hse = count(effort_words, hubristic_utterance), count(self_words, hubristic_utterance)
    print("authentic: effort-words %d  self-words %d" % (ae, ase))
    print("hubristic: effort-words %d  self-words %d" % (he, hse))
    assert ae > ase and hse > he
    ratio = ae / max(1, ase)
    assert ratio >= 2.0
    print("OK: %s heard which face was speaking" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # expected value with the pride-updated self-model
    def choose(p, payoff, cost):
        return p * payoff - cost
    # authentic: calibrated update from a real win; hubristic overprices by identity
    va = choose(0.65, 110.0, 35.0)    # ambitious: hard worthwhile challenge
    vs = choose(0.95, 45.0, 10.0)     # safe: easy safe option
    vg_auth = choose(0.65, 130.0, 60.0)  # gamble priced with evidence
    vg_hub = choose(0.95, 130.0, 60.0)   # same gamble, mispriced by identity
    print("authentic: ambitious %.1f  safe %.1f  gamble %.1f" % (va, vs, vg_auth))
    print("hubristic gamble (mispriced): %.1f" % vg_hub)
    assert va > vs > 0            # authentic picks the ambitious path
    assert vg_auth < va           # correctly prices the long shot down
    assert vg_hub > va            # hubristic mispricing flips the choice
    print("OK: %s repriced the decisions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five stages: glow, swell, blaze, the split, the terminus
    stages = ["glow", "swell", "blaze"]
    gain = {"glow": 0.25, "swell": 0.55, "blaze": 0.90}
    for s in stages:
        print("  %-6s gain %.2f" % (s, gain[s]))
    assert gain["glow"] < gain["swell"] < gain["blaze"]
    # stage four: attribution decides the branch
    authentic_t4 = {"mentoring": 0.85, "building": 0.80, "dominating": 0.05}
    hubristic_t4 = {"mentoring": 0.10, "building": 0.15, "dominating": 0.90}
    a_gen = authentic_t4["mentoring"] + authentic_t4["building"]
    h_dom = hubristic_t4["dominating"]
    print("authentic stage-4 generosity %.2f  hubristic stage-4 dominance %.2f" % (a_gen, h_dom))
    assert a_gen > 1.60 and h_dom > 0.85
    print("OK: %s climbed the escalation stages" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # own it, share it, spread it -> expression health score
    own = 0.90    # the win said out loud, effort included
    share = 0.85  # told to people who understand
    spread = 0.80 # helpers credited, others celebrated
    calibrate = 0.88  # broadcast matched to the win
    health = 0.30 * own + 0.30 * share + 0.25 * spread + 0.15 * calibrate
    print("own %.2f  share %.2f  spread %.2f  calibrate %.2f" % (own, share, spread, calibrate))
    print("expression health: %.3f" % health)
    assert 0.85 < health < 0.87
    assert health > 0.80  # the healthy threshold
    print("OK: %s expressed pride healthily" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # cost over 30 days: bottling ferments, exploding spends socially
    days = 30
    bottle_cost = sum(0.05 * d for d in range(1, days + 1))      # resentment accrues
    explode_cost = sum(0.08 * (days - d + 1) for d in range(1, days + 1))  # goodwill burns
    healthy_cost = 0.5  # small friction of honest expression
    print("30-day cost: bottling %.1f  exploding %.1f  healthy %.1f" % (bottle_cost, explode_cost, healthy_cost))
    assert 23.0 < bottle_cost < 23.5
    assert 37.0 < explode_cost < 37.5
    assert healthy_cost < bottle_cost / 10
    assert healthy_cost < explode_cost / 10
    print("OK: %s priced bottling and exploding" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # seven practices, each a daily balance contribution
    practices = {
        "evening ledger": 0.30,
        "credit audit": 0.25,
        "bar check": 0.15,
        "witness practice": 0.20,
        "modesty calibration": 0.15,
        "effort journal": 0.20,
        "mentor hour": 0.25,
    }
    balance = sum(practices.values())
    for p, v in practices.items():
        print("  %-20s +%.2f" % (p, v))
    print("daily balance: %.2f" % balance)
    assert 1.49 < balance < 1.51
    assert all(v > 0 for v in practices.values())
    # a week of practice compounds
    week = balance * 7
    assert 10.4 < week < 10.6
    print("weekly compound: %.2f" % week)
    print("OK: %s kept the seven practices" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # three channels + context -> recognition score
    body = 0.90    # torso expansion, head tilt
    face = 0.65    # small pressed smile, direct gaze
    voice = 0.70   # lifted pitch, effort-words
    context = 0.85 # a known recent win in the background
    score = 0.35 * body + 0.25 * face + 0.20 * voice + 0.20 * context
    print("body %.2f  face %.2f  voice %.2f  context %.2f" % (body, face, voice, context))
    print("recognition score: %.3f" % score)
    assert 0.78 < score < 0.80
    assert score > 0.70  # the recognition threshold
    assert body > face   # body is the most reliable channel
    print("OK: %s read pride in another person" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five candidate responses scored on witness, specify, join
    responses = {
        "tell me everything - those early mornings paid off": (1.0, 1.0, 0.9),
        "amazing!": (0.5, 0.1, 0.5),
        "nice": (0.2, 0.0, 0.2),
        "that reminds me of when I won": (0.1, 0.2, 0.0),
        "it was just luck, the test was easy": (0.1, 0.0, 0.1),
    }
    scores = {}
    for r, (w, s, j) in responses.items():
        scores[r] = 0.4 * w + 0.35 * s + 0.25 * j
        print("  %-52s %.3f" % (r, scores[r]))
    best = max(scores, key=scores.get)
    worst = min(scores, key=scores.get)
    assert best.startswith("tell me everything")
    assert worst.startswith("it was just luck")
    assert 0.96 < scores[best] < 0.98
    assert scores[worst] < 0.10
    print("OK: %s chose the supportive response" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_mistakes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five mistakes, each a backfire multiplier on the moment (>1 = damage)
    mistakes = {
        "deflation": 2.2,
        "hijack": 2.8,
        "mid-glow audit": 2.5,
        "flatline": 1.8,
        "the moral warning": 3.0,
    }
    for m, b in mistakes.items():
        print("  %-18s backfire x%.1f" % (m, b))
    assert all(b > 1.0 for b in mistakes.values())
    worst = max(mistakes, key=mistakes.get)
    assert worst == "the moral warning"
    total = sum(mistakes.values())
    assert 12.2 < total < 12.4
    print("OK: %s listed the five mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_related_map(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 2D map: x = valence, y = self-focus; pride at origin-adjacent
    coords = {
        "pride": (0.8, 0.7),
        "arrogance": (0.75, 0.80),
        "vanity": (0.6, 0.85),
        "conceit": (0.65, 0.90),
        "self-esteem": (0.7, 0.4),
        "confidence": (0.75, 0.5),
        "humility": (0.5, 0.3),
        "shame": (-0.8, 0.7),
    }
    def dist(a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])
    d = {k: dist(v, coords["pride"]) for k, v in coords.items() if k != "pride"}
    for k in sorted(d, key=d.get):
        print("  %-12s distance %.3f" % (k, d[k]))
    nearest = min(d, key=d.get)
    farthest = max(d, key=d.get)
    assert nearest == "arrogance"
    assert farthest == "shame"
    assert 0.10 < d["arrogance"] < 0.13
    assert 1.59 < d["shame"] < 1.61
    print("OK: %s mapped the pride neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_blends(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # four dyads: pride blended with joy, gratitude, anger, fear
    pride = 0.90
    blends = {
        "triumph (joy)": (0.85, 0.55, 0.45),
        "humble pride (gratitude)": (0.80, 0.50, 0.50),
        "righteous defiance (anger)": (0.75, 0.60, 0.40),
        "fragile pride (fear)": (0.70, 0.65, 0.35),
    }
    out = {}
    for b, (partner, wp, wq) in blends.items():
        val = wp * pride + wq * partner + 0.08 * pride * partner
        out[b] = val
        print("  %-28s %.3f" % (b, val))
    assert all(0.85 < v < 1.00 for v in out.values())
    assert out["triumph (joy)"] > out["fragile pride (fear)"]
    print("OK: %s blended the four dyads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pride_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five scenes: trigger, onset, peak, wobble, resolution
    scenes = {
        "trigger": 0.85,     # the council vote lands
        "onset": 0.70,       # disbelief, then the warmth
        "peak": 1.00,        # the calls, the credit audit, the glow
        "wobble": 0.55,      # the 11 PM doubts, ownership holds
        "resolution": 0.40,  # settled residue + mentoring + aftershock
    }
    for s, v in scenes.items():
        print("  %-10s intensity %.2f" % (s, v))
    vals = list(scenes.values())
    assert vals[2] == max(vals)          # the peak is the peak
    assert vals[1] < vals[2] > vals[3]   # arc shape
    assert scenes["resolution"] > 0.30   # residue funds the next effort
    assert scenes["wobble"] > 0.50       # well-evidenced ownership holds
    arc_energy = sum(vals)
    assert 3.49 < arc_energy < 3.51
    print("total arc energy: %.2f" % arc_energy)
    print("OK: %s simulated one pride end to end" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "pride_definition": demo_pride_definition,
    "pride_emotion_family": demo_pride_emotion_family,
    "pride_volumes": demo_pride_volumes,
    "pride_myths": demo_pride_myths,
    "pride_first_person": demo_pride_first_person,
    "pride_time_course": demo_pride_time_course,
    "pride_low_vs_high": demo_pride_low_vs_high,
    "pride_triumph_blend": demo_pride_triumph_blend,
    "pride_day_in_life": demo_pride_day_in_life,
    "pride_body_signals": demo_pride_body_signals,
    "pride_posture": demo_pride_posture,
    "pride_sleep_appetite_energy": demo_pride_sleep_appetite_energy,
    "pride_bodies_differ": demo_pride_bodies_differ,
    "pride_face": demo_pride_face,
    "pride_face_intensity": demo_pride_face_intensity,
    "pride_hiding_faking": demo_pride_hiding_faking,
    "pride_expression_gallery": demo_pride_expression_gallery,
    "pride_classic_triggers": demo_pride_classic_triggers,
    "pride_personal_triggers": demo_pride_personal_triggers,
    "pride_surprise_triggers": demo_pride_surprise_triggers,
    "pride_chain_reactions": demo_pride_chain_reactions,
    "pride_behavior": demo_pride_behavior,
    "pride_speech": demo_pride_speech,
    "pride_decisions": demo_pride_decisions,
    "pride_escalation": demo_pride_escalation,
    "pride_healthy_expression": demo_pride_healthy_expression,
    "pride_unhealthy_expression": demo_pride_unhealthy_expression,
    "pride_everyday_practices": demo_pride_everyday_practices,
    "pride_reading_others": demo_pride_reading_others,
    "pride_supportive_responses": demo_pride_supportive_responses,
    "pride_mistakes": demo_pride_mistakes,
    "pride_related_map": demo_pride_related_map,
    "pride_blends": demo_pride_blends,
    "pride_full_simulation": demo_pride_full_simulation,
}

assert set(DEMOS) == {"pride_definition", "pride_emotion_family", "pride_volumes",
                      "pride_myths", "pride_first_person", "pride_time_course",
                      "pride_low_vs_high", "pride_triumph_blend", "pride_day_in_life",
                      "pride_body_signals", "pride_posture", "pride_sleep_appetite_energy",
                      "pride_bodies_differ", "pride_face", "pride_face_intensity",
                      "pride_hiding_faking", "pride_expression_gallery",
                      "pride_classic_triggers", "pride_personal_triggers",
                      "pride_surprise_triggers", "pride_chain_reactions", "pride_behavior",
                      "pride_speech", "pride_decisions", "pride_escalation",
                      "pride_healthy_expression", "pride_unhealthy_expression",
                      "pride_everyday_practices", "pride_reading_others",
                      "pride_supportive_responses", "pride_mistakes",
                      "pride_related_map", "pride_blends", "pride_full_simulation"}
