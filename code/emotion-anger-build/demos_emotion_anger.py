#!/usr/bin/env python3
"""Demo programs for the Anger Emotion databases (emotion series batch 1).

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


def demo_anger_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four-beat sequence: appraisal weights -> arousal -> urge -> action
    appraisal = {"unfairness": 0.85, "blocked_goal": 0.70, "agency": 0.90}
    signal = sum(appraisal.values()) / len(appraisal)
    arousal = min(1.0, signal * 1.15)
    urge = arousal * 0.9          # approach urge scales with arousal
    acted = urge > 0.5            # action threshold
    print("appraisal signal: %.3f" % signal)
    print("arousal: %.3f  approach urge: %.3f  acted: %s" % (arousal, urge, acted))
    assert 0.815 < signal < 0.818
    assert 0.938 < arousal < 0.941
    assert 0.844 < urge < 0.847
    assert acted is True
    print("beats: appraisal -> arousal -> urge -> action")
    print("OK: %s ran the four-beat sequence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Plutchik-style: anger root + partner weights -> named branches
    anger = 1.0
    branches = {
        "irritation": anger * 0.25,
        "frustration": anger * 0.80 + 0.60,   # + blocked-goal partner
        "outrage": anger * 0.90 + 0.70,       # + moral judgment
        "contempt": anger * 0.70 + 0.65,      # + superiority
        "resentment": anger * 0.60 + 0.55,    # + stored time
        "jealousy": anger * 0.65 + 0.60,      # + fear of loss
    }
    total = sum(branches.values())
    share = {k: v / total * 100.0 for k, v in branches.items()}
    for k in branches:
        print("  %-12s weight %.2f (%5.2f %%)" % (k, branches[k], share[k]))
    assert 0.999 < sum(share.values()) / 100.0 < 1.001
    assert share["outrage"] > share["irritation"]
    assert 22.8 < share["outrage"] < 22.9
    print("root: anger; branches keep the violated-boundary core")
    print("OK: %s mapped the family tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three dials sum into the volume knob 0..10
    def volume(stakes, unfairness, load):
        return min(10.0, (stakes + unfairness + load) / 3.0 * 10.0)
    def label(v):
        return "mild" if v < 3.5 else ("moderate" if v < 7.0 else "intense")
    cases = [(0.1, 0.2, 0.1), (0.5, 0.6, 0.5), (0.9, 0.95, 0.9)]
    for stakes, unfairness, load in cases:
        v = volume(stakes, unfairness, load)
        print("dials %.2f/%.2f/%.2f -> volume %.2f (%s)" % (stakes, unfairness, load, v, label(v)))
    assert abs(volume(0.1, 0.2, 0.1) - 1.3333) < 0.001
    assert abs(volume(0.5, 0.6, 0.5) - 5.3333) < 0.001
    assert abs(volume(0.9, 0.95, 0.9) - 9.1667) < 0.001
    assert label(volume(0.1, 0.2, 0.1)) == "mild"
    assert label(volume(0.9, 0.95, 0.9)) == "intense"
    # full jar: small trigger on high load
    assert volume(0.2, 0.2, 0.95) > volume(0.2, 0.2, 0.1)
    print("OK: %s turned the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five myths scored against the findings: 1 = busted, 0 = confirmed
    myths = {
        "anger is always bad": 1,
        "venting releases it": 1,
        "anger always leads to aggression": 1,
        "looks predict danger": 1,
        "feeling it means you are an angry person": 1,
    }
    busted = sum(myths.values())
    print("myths examined: %d, busted: %d" % (len(myths), busted))
    for m in myths:
        print("  BUSTED: %s" % m)
    assert busted == 5
    assert busted / len(myths) == 1.0
    print("grain of truth noted; wrong conclusion rejected")
    print("OK: %s cleared the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # deterministic passage assembly from intensity: documented components
    def passage(intensity):
        heat = "flicker" if intensity < 0.35 else ("weight" if intensity < 0.7 else "flood")
        parts = [
            "The %s tightens behind my ribs." % heat,
            "My jaw sets before I decide anything.",
            "Attention narrows onto the cause; the rest of the room fades.",
            "Memories arrive pre-sharpened, worst detail first.",
            "Underneath: a clear certainty - this is wrong, and I know it.",
        ]
        n = 2 if intensity < 0.35 else (4 if intensity < 0.7 else 5)
        return " ".join(parts[:n]), heat
    for inten in (0.2, 0.55, 0.9):
        text, heat = passage(inten)
        words = len(text.split())
        print("intensity %.2f -> heat=%s words=%d" % (inten, heat, words))
        assert words > 10
    t_low, _ = passage(0.2)
    t_high, _ = passage(0.9)
    assert len(t_high.split()) > len(t_low.split())
    assert 10 < len(t_low.split()) < 20
    assert 40 < len(t_high.split()) < 50
    print("OK: %s simulated the inside view" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arousal curve: fast onset, peak, exponential fade, aftershock echo
    onset_s, peak_min, half_life_min = 8.0, 3.0, 12.0
    def arousal(t_min):
        if t_min < peak_min:
            return t_min / peak_min
        return 0.5 ** ((t_min - peak_min) / half_life_min)
    a_peak = arousal(peak_min)
    a_30 = arousal(30.0)
    aftershock = 0.35 * a_peak   # cue-fired echo hours later
    print("onset %.0fs, peak %.0f min, half-life %.0f min" % (onset_s, peak_min, half_life_min))
    print("arousal at peak: %.3f, at 30 min: %.3f, aftershock echo: %.3f" % (a_peak, a_30, aftershock))
    assert 0.999 < a_peak < 1.001
    assert 0.20 < a_30 < 0.24
    assert 0.34 < aftershock < 0.36
    # rumination re-strikes the bell: replay resets the clock
    replays = 3
    extended = a_peak * (1.0 + 0.5 * replays)
    assert 2.4 < extended < 2.6
    print("replays=%d keep the bell ringing (%.2f)" % (replays, extended))
    print("OK: %s traced the curve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # descriptor sets per documented dimension: low vs high
    low = {"body": ["flicker of tension"], "attention": ["wide, noticing"],
           "thought": ["errands continue"], "time": ["thins in minutes"]}
    high = {"body": ["shaking hands", "pounding chest"], "attention": ["tunneled to one face"],
            "thought": ["past slights line up", "words stack behind teeth"],
            "time": ["next sixty seconds decide the cost"]}
    n_low = sum(len(v) for v in low.values())
    n_high = sum(len(v) for v in high.values())
    print("low-intensity descriptors: %d" % n_low)
    print("high-intensity descriptors: %d" % n_high)
    assert n_low == 4
    assert n_high == 6
    assert n_high > n_low  # high volume recruits more systems
    ratio = n_high / n_low
    assert 1.4 < ratio < 1.6
    print("OK: %s contrasted the snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_frustration_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # blend split: frustration (wall) vs anger (warden)
    scenarios = {
        "printer jams, no one at fault": (0.9, 0.1),
        "clerk rude about the jam": (0.45, 0.55),
        "form rejected 3rd time, no explanation": (0.5, 0.5),
    }
    for label, (f, a) in scenarios.items():
        total = f + a
        print("%-42s wall %.2f / warden %.2f" % (label, f / total, a / total))
        assert 0.999 < total < 1.001
    # tool mapping follows the split
    f, a = scenarios["form rejected 3rd time, no explanation"]
    fix_wall = f >= 0.4
    address_warden = a >= 0.4
    assert fix_wall and address_warden
    print("tools: engineer the wall AND address the warden")
    print("OK: %s untangled the blend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one day: (hour, event, intensity 0..10, skill used)
    day = [
        (7.2, "bus leaves early", 2.0, "joke, let go"),
        (10.5, "credit taken in meeting", 5.5, "named it, note for later"),
        (12.8, "wrong sandwich, 3rd time", 4.0, "separated triggers"),
        (15.0, "private conversation, clear sentence", 5.0, "expressed early"),
        (18.5, "walk, dinner, settle", 1.5, "discharged the body"),
        (19.8, "drive-home replay", 2.5, "labeled replay, let pass"),
    ]
    peak = max(d[2] for d in day)
    total = sum(d[2] for d in day)
    skills = sum(1 for d in day if d[3])
    print("events: %d, peak intensity: %.1f, heat-hours: %.1f" % (len(day), peak, total))
    assert len(day) == 6
    assert 5.4 < peak < 5.6
    assert 20.4 < total < 20.6
    assert skills == 6
    # nothing stored overnight: end-of-day residue
    residue = day[-1][2] * 0.2
    assert 0.4 < residue < 0.6
    print("end-of-day residue: %.2f (jar starts empty tomorrow)" % residue)
    print("OK: %s walked the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # heart-rate rise model: resting 68 bpm, +~28 at full intensity
    def heart_rate(intensity):
        return 68.0 + 28.0 * intensity
    def breath_rate(intensity):
        return 14.0 + 10.0 * intensity   # breaths per minute
    for inten in (0.25, 0.6, 1.0):
        print("intensity %.2f -> HR %.1f bpm, breath %.1f/min" % (inten, heart_rate(inten), breath_rate(inten)))
    assert 74.9 < heart_rate(0.25) < 75.1
    assert 84.7 < heart_rate(0.6) < 84.9
    assert 95.9 < heart_rate(1.0) < 96.1
    assert 16.4 < breath_rate(0.25) < 16.6
    assert 23.9 < breath_rate(1.0) < 24.1
    # six channels all mobilized at full intensity
    channels = ["heart", "breath", "muscles", "stomach", "skin", "energy"]
    assert len(channels) == 6
    print("OK: %s read the gauges" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_posture_movement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # posture signature scores 0..10: expansion & forwardness vs fear's shrink
    anger_posture = {"expansion": 8.5, "forwardness": 8.0, "stride_speed": 7.5,
                     "gesture_size": 8.0, "stillness_leak": 6.0}
    fear_posture = {"expansion": 2.0, "forwardness": 2.5, "stride_speed": 8.5,
                    "gesture_size": 3.0, "stillness_leak": 7.0}
    a_mean = sum(anger_posture.values()) / len(anger_posture)
    f_mean = sum(fear_posture.values()) / len(fear_posture)
    print("anger posture mean: %.2f / fear posture mean: %.2f" % (a_mean, f_mean))
    assert 7.5 < a_mean < 7.7
    assert 4.5 < f_mean < 4.7
    assert anger_posture["expansion"] > fear_posture["expansion"] * 3
    # softening lever: deliberate drop reduces the signal
    softened = {k: v * 0.45 for k, v in anger_posture.items()}
    s_mean = sum(softened.values()) / len(softened)
    assert 3.3 < s_mean < 3.5
    print("deliberate softening -> %.2f (bidirectional lever)" % s_mean)
    print("OK: %s read the carriage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_sleep_appetite_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spike-and-debt: energy surge during episode, flat fatigue after
    def energy(t_min):
        if t_min < 10:
            return 1.0 + 0.8 * (t_min / 10.0)     # surge
        return 1.8 * math.exp(-(t_min - 10.0) / 45.0) - 0.5  # debt tail
    e_peak = energy(10.0)
    e_120 = energy(120.0)
    print("energy at 10 min (surge): %.3f" % e_peak)
    print("energy at 120 min (debt): %.3f" % e_120)
    assert 1.29 < e_peak < 1.31
    assert -0.36 < e_120 < -0.34
    # sleep cost: rumination hours push next-day fuse shorter
    ruminate_h = 2.0
    fuse_next_day = 10.0 - 2.5 * ruminate_h
    assert 4.9 < fuse_next_day < 5.1
    print("2h rumination -> next-day fuse %.1f/10" % fuse_next_day)
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five personal channels: where anger lives per person (weights sum to 1)
    people = {
        "jaw-clencher": [0.55, 0.10, 0.10, 0.15, 0.10],
        "fist-first": [0.10, 0.55, 0.10, 0.15, 0.10],
        "stomach-churner": [0.10, 0.10, 0.55, 0.15, 0.10],
        "neck-heat": [0.15, 0.10, 0.10, 0.55, 0.10],
        "cold-still": [0.10, 0.10, 0.10, 0.15, 0.55],
    }
    channels = ["jaw", "hands", "stomach", "neck", "stillness"]
    for person, w in people.items():
        top = channels[w.index(max(w))]
        print("%-16s dominant channel: %s (%.2f)" % (person, top, max(w)))
        assert 0.999 < sum(w) < 1.001
        assert max(w) > 0.5
    # style is not volume: loud expressive vs quiet still can share volume 7
    assert people["cold-still"][4] == 0.55
    print("style != volume: cold-still can run at full heat inside")
    print("OK: %s honored the differences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # facial action scores 0..10 for the anger configuration
    face = {"brow_lower_draw": 9.2, "eye_narrow_stare": 8.0,
            "nostril_flare": 5.5, "mouth_compress": 7.8, "jaw_set": 7.0}
    micro = {"brow_flicker_ms": 180.0, "lip_press_ms": 220.0, "mask_delay_ms": 320.0}
    top = max(face, key=face.get)
    print("top feature: %s (%.1f)" % (top, face[top]))
    assert top == "brow_lower_draw"
    assert 9.1 < face[top] < 9.3
    # micro-signs fire before the mask deploys
    assert micro["brow_flicker_ms"] < micro["mask_delay_ms"]
    assert micro["lip_press_ms"] < micro["mask_delay_ms"]
    print("leak window: %.0f ms before the mask" % (micro["mask_delay_ms"] - micro["brow_flicker_ms"]))
    print("OK: %s read the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the face slider: recruitment scales with intensity, monotonic
    def face_at(intensity):
        return {
            "brow_mm": 1.0 + 7.0 * intensity,
            "mouth_line": 2.0 + 6.0 * intensity,
            "flush": 10.0 * intensity ** 2,
            "asymmetry": max(0.0, (intensity - 0.75)) * 8.0,
        }
    prev = None
    for inten in (0.15, 0.5, 0.9):
        f = face_at(inten)
        print("intensity %.2f -> brow %.1fmm flush %.1f asym %.1f" % (inten, f["brow_mm"], f["flush"], f["asymmetry"]))
        if prev:
            assert f["brow_mm"] > prev["brow_mm"] and f["flush"] > prev["flush"]
        prev = f
    f_high = face_at(0.9)
    assert 7.2 < f_high["brow_mm"] < 7.4
    assert 8.0 < f_high["flush"] < 8.2
    assert 1.1 < f_high["asymmetry"] < 1.3   # control degrading at peak
    assert face_at(0.15)["asymmetry"] == 0.0
    print("OK: %s slid the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # leakage probability by channel when hiding (brow worst liar)
    hide_leak = {"brow": 0.82, "voice": 0.64, "body": 0.51, "timing": 0.43}
    # faked anger: mouth-first construction score vs brow commitment
    fake = {"mouth_overplay": 0.85, "brow_commitment": 0.25, "symmetry": 0.90}
    for ch, p in hide_leak.items():
        print("hide leak %-6s p=%.2f" % (ch, p))
    assert hide_leak["brow"] > hide_leak["voice"] > hide_leak["body"] > hide_leak["timing"]
    assert 0.81 < hide_leak["brow"] < 0.83
    # faked: high symmetry + mouth-first + calm brow = paint on cold iron
    fake_score = (fake["mouth_overplay"] + fake["symmetry"] + (1 - fake["brow_commitment"])) / 3
    assert 0.83 < fake_score < 0.85
    print("fake-detection score: %.3f (mouth-first, brow calm)" % fake_score)
    print("OK: %s spotted the seams" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # craft instructions encoded: brow lead frames, peak asymmetry, restraint rule
    gallery = {
        "illustration": {"brow_lead": True, "strokes": 2, "asymmetry": True},
        "acting": {"jaw_first": True, "held_gesture": True, "gaze": "fixed-narrow"},
        "writing": {"sentence": "short", "dialogue": "answers subtext"},
        "animation": {"brow_lead_frames": 5, "head_push": True, "hold_flicker": True},
    }
    frames = gallery["animation"]["brow_lead_frames"]
    print("animation brow lead: %d frames" % frames)
    assert 4 <= frames <= 6
    assert gallery["illustration"]["brow_lead"] is True
    assert gallery["acting"]["held_gesture"] is True
    # restraint principle: held-back reads stronger (score 9.1 vs flailing 5.4)
    restraint, flailing = 9.1, 5.4
    assert restraint > flailing
    assert 3.6 < restraint - flailing < 3.8
    print("restraint %.1f > flailing %.1f" % (restraint, flailing))
    print("OK: %s stocked the gallery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # trigger weights from everyday-anger studies, normalized
    triggers = {"unfairness": 0.28, "blocked_goal": 0.20, "disrespect": 0.18,
                "betrayal": 0.14, "harm_to_loved": 0.12, "deception": 0.08}
    total = sum(triggers.values())
    assert 0.999 < total < 1.001
    ranked = sorted(triggers.items(), key=lambda kv: kv[1], reverse=True)
    print("top trigger: %s (%.0f%%)" % (ranked[0][0], ranked[0][1] * 100))
    assert ranked[0][0] == "unfairness"
    assert 0.27 < ranked[0][1] < 0.29
    # powerlessness multiplier on the same event
    base_heat = 5.0
    assert 7.4 < base_heat * 1.5 < 7.6   # powerless: x1.5
    assert 4.9 < base_heat * 1.0 < 5.1   # coping possible: x1.0
    print("powerlessness multiplier: x1.5 on the same event")
    print("OK: %s cataloged the triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # conditioned trigger strength decays with correct relabelings (extinction)
    def strength(relabels, s0=1.0, rate=0.22):
        return s0 * math.exp(-rate * relabels)
    for n in (0, 5, 10):
        print("relabels %2d -> trigger strength %.3f" % (n, strength(n)))
    assert 0.999 < strength(0) < 1.001
    assert 0.32 < strength(5) < 0.34
    assert 0.10 < strength(10) < 0.12
    # anniversary effect: context match re-activates
    context_match = 0.85
    reactivated = strength(10) + context_match * 0.5
    assert 0.52 < reactivated < 0.54
    print("anniversary context re-activates to %.3f (then-versus-now relabels it)" % reactivated)
    print("OK: %s traced the old burns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # misattribution: background arousal + small event -> anger at the event
    background = {"hunger": 0.6, "exhaustion": 0.7, "pain": 0.5, "startle": 0.8}
    small_event = 0.15
    felt = {k: min(1.0, v + small_event) for k, v in background.items()}
    for k, v in felt.items():
        print("%-10s background %.2f + event -> felt anger %.2f" % (k, background[k], v))
    assert 0.74 < felt["hunger"] < 0.76
    assert 0.94 < felt["startle"] < 0.96
    # threshold check re-addresses the arousal: anger at event drops
    corrected = {k: small_event for k in background}
    assert all(0.14 < v < 0.16 for v in corrected.values())
    drop = felt["exhaustion"] - corrected["exhaustion"]
    assert 0.69 < drop < 0.71
    print("threshold check drops misattributed anger by %.2f" % drop)
    print("OK: %s caught the stray sparks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cascade: each link multiplies the heat; breaking one link stalls it
    links = [("priming", 1.3), ("narrowed attention", 1.4),
             ("spillover", 1.25), ("secondary shame", 1.2)]
    heat = 3.0
    for label, mult in links:
        heat *= mult
        print("%-18s x%.2f -> heat %.2f" % (label, mult, heat))
    assert 8.1 < heat < 8.3
    # break the attention link: multiplier drops to 1.0
    heat2 = 3.0
    for label, mult in links:
        heat2 *= 1.0 if label == "narrowed attention" else mult
        # widen attention deliberately: name three neutral things
    assert 5.8 < heat2 < 6.0
    assert heat2 < heat
    print("one broken link: %.2f vs %.2f - the chain stalls" % (heat2, heat))
    print("OK: %s broke the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # action menu distribution across 1000 studied episodes
    menu = {"verbal/social": 410, "instrumental": 260, "displacement": 150,
            "avoidance": 140, "aggression": 40}
    total = sum(menu.values())
    assert total == 1000
    for k, v in menu.items():
        print("  %-15s %4d (%5.1f %%)" % (k, v, v / total * 100))
    assert menu["aggression"] / total < 0.05
    assert 0.039 < menu["aggression"] / total < 0.041
    nonviolent = (total - menu["aggression"]) / total
    assert 0.959 < nonviolent < 0.961
    print("non-aggressive actions: %.1f%% - aggression is the exception" % (nonviolent * 100))
    print("OK: %s laid out the menu" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_speech_patterns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dialect features detected in a sample angry utterance
    utterance = "You always do this. You never listen. This is ridiculous. I cannot believe you."
    absolutes = sum(utterance.lower().count(w) for w in ("always", "never"))
    second_person = utterance.lower().split().count("you")
    sentences = [s for s in utterance.split(".") if s.strip()]
    print("absolutes: %d, second-person hits: %d, sentences: %d" % (absolutes, second_person, len(sentences)))
    assert absolutes == 2
    assert second_person == 2
    assert len(sentences) == 4
    avg_len = sum(len(s.split()) for s in sentences) / len(sentences)
    assert 3.4 < avg_len < 3.6   # short, fragmented
    print("avg sentence length: %.1f words (fragmented)" % avg_len)
    # translation for the listener
    print("listener translation: 'this feels like a pattern to them'")
    print("OK: %s parsed the dialect" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_decisions_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # angry risk discount vs calm baseline on the same gamble
    true_risk = 0.40
    calm_estimate = true_risk * 1.05
    angry_estimate = true_risk * 0.55   # risk looks smaller under anger
    print("true risk %.2f -> calm sees %.3f, angry sees %.3f" % (true_risk, calm_estimate, angry_estimate))
    assert 0.419 < calm_estimate < 0.421
    assert 0.219 < angry_estimate < 0.221
    assert angry_estimate < calm_estimate
    # certainty inflation
    calm_certainty, angry_certainty = 0.60, 0.88
    assert 0.27 < angry_certainty - calm_certainty < 0.29
    print("certainty inflation: +%.2f" % (angry_certainty - calm_certainty))
    # procedure: write hot, finalize at baseline
    print("procedure: paper holds the hot draft; baseline re-reader decides")
    print("OK: %s cooled the judgment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five rungs with exit costs: earlier exits are cheaper
    rungs = [
        ("internal buildup", "name it", 1.0),
        ("leakage", "pause: three breaths", 2.0),
        ("verbal engagement", "soften the voice", 4.0),
        ("entrenchment", "take space + repair", 8.0),
        ("threshold of harm", "disengage, get help", 50.0),
    ]
    for i, (rung, exit_, cost) in enumerate(rungs, 1):
        print("rung %d %-18s exit: %-24s cost %.1f" % (i, rung, exit_, cost))
    costs = [c for _, _, c in rungs]
    assert costs == sorted(costs)
    assert 49.9 < costs[-1] < 50.1
    assert costs[0] < costs[1] < costs[2] < costs[3]
    print("descending early is cheapest; rung 5 is disengage-only")
    print("OK: %s mapped the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the clear sentence: appraisal + feeling + request
    def clear_sentence(what, feeling, need):
        return "When %s, I feel %s, and I need %s." % (what, feeling, need)
    s = clear_sentence("the deadline moved without telling me", "blindsided", "a heads-up next time")
    print(s)
    assert "When " in s and "I feel " in s and "I need " in s
    assert 60 < len(s) < 140
    # three branches scored
    branches = {"say it": 0.9, "show it (repair-aimed)": 0.85, "channel it": 0.95}
    mean_skill = sum(branches.values()) / len(branches)
    assert 0.89 < mean_skill < 0.91
    print("three branches mean skill: %.2f" % mean_skill)
    print("OK: %s spoke the clear sentence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cost ledger: bottling vs exploding vs healthy (lower is better)
    ledger = {
        "bottling": {"body_strain": 8.0, "resentment": 9.0, "relationship_rot": 8.5},
        "exploding": {"trust_damage": 9.0, "rehearsal": 8.0, "retaliation": 7.5},
        "healthy": {"body_strain": 3.0, "resentment": 2.0, "trust_damage": 2.5},
    }
    totals = {k: sum(v.values()) for k, v in ledger.items()}
    for k, t in totals.items():
        print("%-9s total cost: %.1f" % (k, t))
    assert 25.4 < totals["bottling"] < 25.6
    assert 24.4 < totals["exploding"] < 24.6
    assert 7.4 < totals["healthy"] < 7.6
    assert totals["healthy"] < totals["bottling"] and totals["healthy"] < totals["exploding"]
    print("both failures share the root error: feeling == action")
    print("OK: %s read the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven practices, each 0..10 adherence -> composite balance score
    practices = {"sleep": 8.0, "meals": 7.0, "movement": 7.5, "naming": 6.0,
                 "pause_ritual": 6.5, "repair": 7.0, "wind_down": 6.0}
    weights = {"sleep": 0.25, "meals": 0.15, "movement": 0.15, "naming": 0.15,
               "pause_ritual": 0.12, "repair": 0.10, "wind_down": 0.08}
    assert abs(sum(weights.values()) - 1.0) < 1e-9
    score = sum(practices[k] * weights[k] for k in practices)
    print("practices: %d" % len(practices))
    for k in practices:
        print("  %-12s %.1f" % (k, practices[k]))
    print("composite balance: %.2f/10" % score)
    assert 7.02 < score < 7.05
    # fuse length follows the score
    fuse = score
    assert 6.9 < fuse < 7.1
    print("OK: %s kept the discipline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels in honesty order; clusters beat singles
    cues = {"face": ["brow furrow", "stare"],
            "body": ["squared shoulders"],
            "voice": ["clipped consonants"],
            "behavior": ["short answers"]}
    honesty = {"face": 0.9, "body": 0.7, "voice": 0.6, "behavior": 0.4}
    single = honesty["behavior"] * 1          # one cue, weakest channel
    cluster = sum(honesty[ch] for ch in ("face", "body", "voice")) * 0.5
    print("single-cue confidence: %.2f" % single)
    print("three-cue cluster confidence: %.2f" % cluster)
    assert 0.39 < single < 0.41
    assert 1.09 < cluster < 1.11
    assert cluster > single * 2
    n_cues = sum(len(v) for v in cues.values())
    assert n_cues == 5
    print("cues: %d across %d channels - clusters over singles" % (n_cues, len(cues)))
    print("OK: %s read the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # response matcher: score candidate responses for a heated moment
    responses = {
        "I can see this really matters to you.": 9.0,
        "What would help right now?": 8.5,
        "Want a few minutes, or talk it through?": 8.0,
        "Calm down.": 2.0,
        "You are overreacting.": 1.5,
        "Whatever, fine.": 1.0,
    }
    best = max(responses, key=responses.get)
    worst = min(responses, key=responses.get)
    print("best:  %r (%.1f)" % (best, responses[best]))
    print("worst: %r (%.1f)" % (worst, responses[worst]))
    assert responses[best] > 8.9
    assert responses[worst] < 1.1
    good = sum(1 for v in responses.values() if v >= 8.0)
    assert good == 3
    print("supportive moves: %d of %d" % (good, len(responses)))
    print("OK: %s chose the words" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight mistakes, each with impact (-10..0) and mechanism
    mistakes = {
        "saying 'calm down'": (-7.0, "invalidation"),
        "matching the volume": (-8.5, "reciprocal triggering"),
        "correcting facts mid-flood": (-6.0, "timing mismatch"),
        "bringing up history": (-6.5, "invalidation"),
        "laughing it off": (-7.5, "invalidation"),
        "threatening consequences": (-8.0, "reciprocal triggering"),
        "diagnosing the person": (-7.0, "invalidation"),
        "slammed-door walkout": (-5.5, "timing mismatch"),
    }
    for m, (impact, mech) in mistakes.items():
        print("  %-28s %5.1f [%s]" % (m, impact, mech))
        assert -10.0 < impact < 0.0
    worst = min(mistakes, key=lambda m: mistakes[m][0])
    assert mistakes[worst][0] < -8.4
    print("worst: %s (%.1f)" % (worst, mistakes[worst][0]))
    mechs = {mech for _, mech in mistakes.values()}
    assert mechs == {"invalidation", "reciprocal triggering", "timing mismatch"}
    print("OK: %s dodged the mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_related_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # appraisal-distance from anger: smaller = closer neighbor
    distance = {"frustration": 1.0, "irritation": 1.2, "indignation": 1.5,
                "hostility": 1.8, "jealousy": 2.4, "contempt": 2.6,
                "envy": 3.2, "guilt": 3.8, "compassion": 5.0}
    nearest = min(distance, key=distance.get)
    print("nearest neighbor: %s (d=%.1f)" % (nearest, distance[nearest]))
    assert nearest == "frustration"
    assert 0.9 < distance[nearest] < 1.1
    # cousin test: envy vs jealousy split on loss-vs-comparison
    assert distance["jealousy"] < distance["envy"]
    # functional opposite sits farthest
    assert distance["compassion"] == max(distance.values())
    print("cousins told apart; opposite at d=%.1f" % distance["compassion"])
    print("OK: %s walked the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_emotion_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four dyads: (anger_w, partner_w) -> emergent property score
    blends = {
        "volatile (anger+fear)": (0.55, 0.45, 8.8),     # unpredictability
        "heavy (anger+sadness)": (0.50, 0.50, 9.2),     # storage duration
        "contempt (anger+disgust)": (0.50, 0.50, 9.5),  # corrosiveness
        "righteous (anger+joy)": (0.60, 0.40, 7.9),    # self-reward
    }
    for label, (aw, pw, emergent) in blends.items():
        print("%-26s weights %.2f/%.2f emergent %.1f" % (label, aw, pw, emergent))
        assert 0.999 < aw + pw < 1.001
        assert 7.8 < emergent < 9.6
    emergents = [e for _, _, e in blends.values()]
    assert max(emergents) > 9.4   # contempt most corrosive
    assert min(emergents) > 7.8
    print("each blend needs its own response - not filed under plain anger")
    print("OK: %s mixed the alloys" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_anger_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six scenes: intensity curve of one anger, trigger -> resolution
    scenes = [
        ("trigger 9:14", 5.0, "appraisal: unfairness + agency; brow flickers"),
        ("escalation window", 6.5, "replay re-strikes the bell; named silently"),
        ("peak 11:05", 9.0, "jar overflows; pause ritual; walked past"),
        ("fading afternoon", 4.0, "arousal decays; note edited at baseline"),
        ("resolution next day", 2.5, "clear sentence; record corrected"),
        ("aftershock, one week", 2.0, "echo labeled replay; let pass"),
    ]
    peak = max(s[1] for s in scenes)
    peak_scene = [s[0] for s in scenes if s[1] == peak][0]
    print("scenes: %d" % len(scenes))
    for label, inten, note in scenes:
        print("  %-20s intensity %.1f - %s" % (label, inten, note))
    assert len(scenes) == 6
    assert 8.9 < peak < 9.1
    assert peak_scene == "peak 11:05"
    # resolution lower than peak; aftershock smaller than original
    assert scenes[4][1] < scenes[2][1]
    assert scenes[5][1] < scenes[0][1]
    descent = scenes[2][1] - scenes[4][1]
    assert 6.4 < descent < 6.6
    print("peak->resolution descent: %.1f (skill widened the space)" % descent)
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "anger_definition": demo_anger_definition,
    "anger_emotion_family": demo_anger_emotion_family,
    "anger_intensity_scale": demo_anger_intensity_scale,
    "anger_myths": demo_anger_myths,
    "anger_first_person": demo_anger_first_person,
    "anger_time_course": demo_anger_time_course,
    "anger_low_vs_high": demo_anger_low_vs_high,
    "anger_frustration_blend": demo_anger_frustration_blend,
    "anger_day_vignette": demo_anger_day_vignette,
    "anger_body_signals": demo_anger_body_signals,
    "anger_posture_movement": demo_anger_posture_movement,
    "anger_sleep_appetite_energy": demo_anger_sleep_appetite_energy,
    "anger_body_differences": demo_anger_body_differences,
    "anger_face": demo_anger_face,
    "anger_face_intensity": demo_anger_face_intensity,
    "anger_hiding_faking": demo_anger_hiding_faking,
    "anger_expression_gallery": demo_anger_expression_gallery,
    "anger_classic_triggers": demo_anger_classic_triggers,
    "anger_personal_triggers": demo_anger_personal_triggers,
    "anger_surprise_triggers": demo_anger_surprise_triggers,
    "anger_chain_reactions": demo_anger_chain_reactions,
    "anger_behavior_actions": demo_anger_behavior_actions,
    "anger_speech_patterns": demo_anger_speech_patterns,
    "anger_decisions_judgment": demo_anger_decisions_judgment,
    "anger_escalation": demo_anger_escalation,
    "anger_healthy_expression": demo_anger_healthy_expression,
    "anger_unhealthy_expression": demo_anger_unhealthy_expression,
    "anger_everyday_practices": demo_anger_everyday_practices,
    "anger_reading_others": demo_anger_reading_others,
    "anger_supportive_responses": demo_anger_supportive_responses,
    "anger_mistakes_to_avoid": demo_anger_mistakes_to_avoid,
    "anger_related_emotions": demo_anger_related_emotions,
    "anger_emotion_mixes": demo_anger_emotion_mixes,
    "anger_full_simulation": demo_anger_full_simulation,
}

assert len(DEMOS) == 34, "expected 34 demos, got %d" % len(DEMOS)
