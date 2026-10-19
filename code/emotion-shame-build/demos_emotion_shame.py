#!/usr/bin/env python3
"""Demo programs for the Shame Emotion databases (emotion series).

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


def demo_shame_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the three-part circuit: standard x exposure x audience -> shame signal
    standard = 0.90   # how central the breached standard is
    exposure = 0.80   # how unveiled the failure feels
    audience = 0.85   # how weighty the watching eyes feel
    signal = standard * exposure * audience
    print("circuit: standard %.2f x exposure %.2f x audience %.2f" % (standard, exposure, audience))
    print("shame signal: %.4f" % signal)
    assert 0.6119 < signal < 0.6121
    alone = standard * exposure * 0.15   # imagined audience still fires, weaker
    print("alone (imagined audience): %.4f" % alone)
    assert 0.1079 < alone < 0.1081
    assert alone > 0.0  # the audience lives inside the mind
    print("OK: %s ran the three-part circuit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # family weights around the shame core; shares must sum to 100
    core = 1.0
    family = {
        "shame": core * 1.00,
        "guilt": core * 0.85,        # act-focused sibling
        "embarrassment": core * 0.55, # brief situational cousin
        "humiliation": core * 0.95,   # shame + perpetrator
        "shyness": core * 0.45,       # anticipated shame
        "pride": core * 0.70,         # opposite pole, same machinery
    }
    total = sum(family.values())
    share = {k: v / total * 100.0 for k, v in family.items()}
    for k in family:
        print("  %-14s weight %.2f (%5.2f %%)" % (k, family[k], share[k]))
    assert 99.99 < sum(share.values()) < 100.01
    assert share["shame"] > share["embarrassment"]
    assert 22.21 < share["shame"] < 22.23
    print("OK: %s mapped the family tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # three dials -> volume knob 0..10
    def volume(identity, audience, permanence):
        return min(10.0, (identity + audience + permanence) / 3.0 * 10.0)
    def label(v):
        return "mild" if v < 3.5 else ("moderate" if v < 7.0 else "intense")
    cases = [(0.15, 0.20, 0.10), (0.55, 0.60, 0.50), (0.95, 0.95, 0.90)]
    for ident, aud, perm in cases:
        v = volume(ident, aud, perm)
        print("dials %.2f/%.2f/%.2f -> volume %.2f (%s)" % (ident, aud, perm, v, label(v)))
    assert label(volume(*cases[0])) == "mild"
    assert label(volume(*cases[1])) == "moderate"
    assert label(volume(*cases[2])) == "intense"
    assert 1.49 < volume(*cases[0]) < 1.51
    assert 5.49 < volume(*cases[1]) < 5.51
    assert 9.32 < volume(*cases[2]) < 9.34
    print("OK: %s set the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # belief accuracy before vs after myth correction (5 myths)
    before = [0.30, 0.45, 0.25, 0.50, 0.35]  # folk accuracy per myth
    correction = [0.55, 0.40, 0.60, 0.35, 0.50]  # gain from the factual account
    after = [min(1.0, b + c) for b, c in zip(before, correction)]
    avg_before = sum(before) / len(before)
    avg_after = sum(after) / len(after)
    print("myth accuracy: before %.3f -> after %.3f" % (avg_before, avg_after))
    assert 0.369 < avg_before < 0.371
    assert 0.849 < avg_after < 0.851
    assert avg_after > avg_before
    print("myths cleared: shame!=guilt, mild shame useful, innocents feel it,")
    print("  shamelessness!=strength, secrecy feeds it")
    print("OK: %s cleared the fog on the mirror" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # attention budget: outward vs inward share across the episode
    steps = ["calm", "onset", "peak", "fading"]
    inward = [0.20, 0.65, 0.90, 0.45]  # share of attention aimed at the self
    for s, w in zip(steps, inward):
        print("  %-7s attention inward: %4.0f%% outward: %4.0f%%" % (s, w * 100, (1 - w) * 100))
    assert inward[2] > inward[1] > inward[0]
    assert inward[3] < inward[2]  # the spotlight swings back out
    assert 0.899 < inward[2] < 0.901
    print("OK: %s traced the spotlight reversal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # arousal curve: onset spike, peak, exponential fade, aftershock echoes
    peak = 1.0
    decay = 0.55  # per-hour decay factor after the peak
    hours = [0.05, 0.5, 2.0, 6.0, 24.0]
    levels = [peak * (decay ** h) for h in hours]
    for h, lv in zip(hours, levels):
        print("  t=+%5.2fh  arousal %.4f" % (h, lv))
    for a, b in zip(levels, levels[1:]):
        assert a > b  # strictly decaying after the peak
    assert 0.970 < levels[0] < 0.972
    assert 0.741 < levels[1] < 0.743
    # aftershock: a reminder re-fires at a fraction of the original
    echo = levels[3] * 4.0
    print("  reminder echo at +6h: %.4f (fraction of peak)" % echo)
    assert 0.10 < echo < 0.12
    print("OK: %s charted onset, peak, fading, aftershock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # two snapshots on the same three dials
    def volume(identity, audience, permanence):
        return min(10.0, (identity + audience + permanence) / 3.0 * 10.0)
    low = volume(0.15, 0.25, 0.10)    # mispronounced name at dinner
    high = volume(0.95, 0.90, 0.95)   # public dismantling by a respected figure
    print("low snapshot volume:  %.2f -> the tap on the shoulder" % low)
    print("high snapshot volume: %.2f -> the hand pressing down" % high)
    assert 1.66 < low < 1.68
    assert 9.32 < high < 9.34
    assert high > 5.0 * low  # different universe, same machinery
    print("OK: %s compared the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_guilt_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # two tracks: guilt pushes approach+repair, shame pushes withdraw+hide
    guilt = {"approach": 0.80, "repair": 0.85, "withdraw": 0.10}
    shame = {"approach": 0.10, "repair": 0.15, "withdraw": 0.85}
    # attention decides the blend: focus on harmed party vs watching eyes
    for focus, w_guilt, w_shame in [("harmed party", 0.7, 0.3), ("watching eyes", 0.3, 0.7)]:
        approach = w_guilt * guilt["approach"] + w_shame * shame["approach"]
        withdraw = w_guilt * guilt["withdraw"] + w_shame * shame["withdraw"]
        net = approach - withdraw
        print("focus %-13s approach %.3f withdraw %.3f net %+.3f" % (focus, approach, withdraw, net))
        if focus == "harmed party":
            assert net > 0.0  # guilt leads -> repair
            assert 0.264 < net < 0.266
        else:
            assert net < 0.0  # shame leads -> hiding
            assert -0.316 < net < -0.314
    print("OK: %s untangled the knot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the three daily taxes: anticipation, attention, discounted reward
    anticipation = 0.30  # outfit, seat, silence pre-shaped
    attention = 0.35     # working memory eaten by the replay loop
    reward = 0.25        # praise sliding off the rewritten self-model
    tax = anticipation + attention + reward
    hours = 16.0
    lost = tax * hours
    print("taxes: anticipation %.2f + attention %.2f + reward %.2f = %.2f" % (
        anticipation, attention, reward, tax))
    print("of a 16h day, %.1f hours effectively taxed" % lost)
    assert 0.899 < tax < 0.901
    assert 14.39 < lost < 14.41
    # the metacognitive crack: naming cuts the attention tax
    attention_named = attention * 0.40
    tax_named = anticipation + attention_named + reward
    print("after naming the operator: tax %.2f (saved %.2f)" % (tax_named, tax - tax_named))
    assert tax_named < tax
    print("OK: %s ledgered Mara's day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # six body channels, normalized shares of the shame response
    channels = {
        "skin (blush)": 0.95,
        "heart": 0.70,
        "breath (shallow)": 0.75,
        "muscles (slump)": 0.85,
        "stomach (knot)": 0.65,
        "energy (drain)": 0.80,
    }
    total = sum(channels.values())
    share = {k: v / total * 100.0 for k, v in channels.items()}
    for k in channels:
        print("  %-17s raw %.2f (%5.2f %%)" % (k, channels[k], share[k]))
    assert 99.99 < sum(share.values()) < 100.01
    assert share["skin (blush)"] > share["stomach (knot)"]
    assert 20.20 < share["skin (blush)"] < 20.22
    print("OK: %s read the body's ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_posture_movement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # shrink index 0..100 from postural components (degrees / factors)
    head_tilt = 18.0      # degrees forward
    shoulder_roll = 0.80  # 0..1 inward roll
    chest_narrow = 0.75   # 0..1 narrowing
    height_loss = 0.06    # fraction of stature resigned
    shrink = (head_tilt / 30.0 * 25.0 + shoulder_roll * 25.0 +
              chest_narrow * 25.0 + height_loss / 0.10 * 25.0)
    print("components: head %.0f deg, shoulders %.2f, chest %.2f, height -%.0f%%" % (
        head_tilt, shoulder_roll, chest_narrow, height_loss * 100))
    print("shrink index: %.2f / 100" % shrink)
    assert 68.74 < shrink < 68.76
    pride = 100.0 - shrink  # the photographic negative
    print("pride's negative would read: %.2f" % pride)
    assert 31.24 < pride < 31.26
    print("OK: %s measured the geometry of shame" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_sleep_appetite_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # maintenance budget: share of normal function under calm vs shame alarm
    systems = {"appetite": (1.00, 0.35), "sleep": (1.00, 0.55), "energy": (1.00, 0.45)}
    for name_, (calm, alarm) in systems.items():
        drop = (calm - alarm) * 100.0
        print("  %-8s calm %4.0f%% -> alarm %4.0f%% (drop %4.0f%%)" % (
            name_, calm * 100, alarm * 100, drop))
    avg_drop = sum((c - a) for c, a in systems.values()) / len(systems) * 100.0
    print("average maintenance drop: %.2f%%" % avg_drop)
    assert 54.99 < avg_drop < 55.01
    # recovery: systems re-budget as the threat passes
    recovered = {"appetite": 0.95, "sleep": 0.90, "energy": 0.92}
    for name_, r in recovered.items():
        assert r > systems[name_][1]
    print("OK: %s tracked the garrison's rations" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # three body profiles run the same program on different hardware
    profiles = {
        "blusher": {"blush": 0.95, "voice": 0.40, "gut": 0.45},
        "freezer": {"blush": 0.25, "voice": 0.90, "gut": 0.55},
        "gut-first": {"blush": 0.35, "voice": 0.45, "gut": 0.95},
    }
    for pname, ch in profiles.items():
        total = sum(ch.values())
        dom = max(ch, key=ch.get)
        print("  %-9s total %.2f dominant channel: %s" % (pname, total, dom))
        assert 1.69 < total < 1.81  # same program, redistributed
    assert profiles["blusher"]["blush"] > profiles["freezer"]["blush"]
    assert profiles["gut-first"]["gut"] > profiles["blusher"]["gut"]
    # absence of a blush is not absence of shame
    assert profiles["freezer"]["voice"] + profiles["freezer"]["gut"] > 1.0
    print("OK: %s calibrated the different gauges" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # face channels recruited at moderate intensity (1 = fully recruited)
    channels = {
        "gaze aversion": 1.0,
        "head down-turn": 0.9,
        "lip compression": 0.85,
        "brow lower": 0.6,
        "hand barrier": 0.7,
        "blush": 0.9,
    }
    recruited = sum(1 for v in channels.values() if v >= 0.6)
    strength = sum(channels.values()) / len(channels)
    print("channels recruited: %d of %d" % (recruited, len(channels)))
    print("mean display strength: %.4f" % strength)
    for k, v in channels.items():
        print("  %-16s %4.0f%%" % (k, v * 100))
    assert recruited == 6
    assert 0.824 < strength < 0.826
    print("OK: %s read the shamed face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the dimmer: recruitment rises, coordination peaks then fragments
    settings = {
        "low": {"recruit": 0.25, "coord": 0.90},
        "moderate": {"recruit": 0.85, "coord": 0.95},
        "high": {"recruit": 1.00, "coord": 0.45},
        "overload": {"recruit": 1.00, "coord": 0.15},
    }
    for s, d in settings.items():
        legibility = d["recruit"] * d["coord"]
        print("  %-9s recruit %.2f coord %.2f legibility %.3f" % (s, d["recruit"], d["coord"], legibility))
    leg = {s: d["recruit"] * d["coord"] for s, d in settings.items()}
    assert leg["moderate"] > leg["low"]      # the classic readable face
    assert leg["moderate"] > leg["high"]     # fragmentation costs legibility
    assert leg["overload"] < leg["low"]      # the blank is least legible
    assert 0.807 < leg["moderate"] < 0.809
    print("OK: %s worked the dimmer switch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # voluntary channels can be suppressed; involuntary ones leak
    voluntary = {"head angle": 0.80, "mouth": 0.75, "hands": 0.70}   # suppression effort
    involuntary = {"blush": 0.95, "gaze break": 0.85, "blink rate": 0.60, "pitch": 0.55}
    shown_voluntary = {k: max(0.0, 1.0 - v) for k, v in voluntary.items()}
    leak = sum(involuntary.values()) / len(involuntary)
    cover = sum(shown_voluntary.values()) / len(shown_voluntary)
    print("voluntary display remaining after cover: %.3f" % cover)
    print("involuntary leak score: %.3f" % leak)
    assert 0.249 < cover < 0.251
    assert 0.736 < leak < 0.738
    assert leak > cover * 2.0  # the leaks betray the cover
    # suppression monitoring feeds the feeling: effort sustains arousal
    effort = sum(voluntary.values()) / len(voluntary)
    sustained = 0.50 + effort * 0.40
    print("arousal sustained by monitoring effort: %.3f" % sustained)
    assert 0.799 < sustained < 0.801
    print("OK: %s caught the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # artist checklist: components and their coverage weight
    components = {
        "head tilt 15-20 deg": 0.20,
        "quarter-turn away": 0.15,
        "lowered eyeline": 0.20,
        "compressed mouth": 0.15,
        "blush wash": 0.15,
        "shoulder roll": 0.10,
        "hand barrier": 0.05,
    }
    coverage = sum(components.values())
    print("checklist items: %d  coverage: %.2f" % (len(components), coverage))
    for k, v in components.items():
        print("  %-20s weight %.2f" % (k, v))
    assert len(components) == 7
    assert 0.999 < coverage < 1.001
    # the classic error: playing sadness instead of shame
    sadness_overlap = 0.35  # shared brow/mouth features
    distinct = 1.0 - sadness_overlap
    print("distinct from sadness: %.0f%% (play the refusal, not the tears)" % (distinct * 100))
    assert 0.649 < distinct < 0.651
    print("OK: %s filled the sketchbook" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # six classic triggers scored on the circuit: standard x exposure x audience
    triggers = {
        "public failure": (0.90, 0.95, 0.90),
        "hidden exposure": (0.85, 1.00, 0.80),
        "public criticism": (0.80, 0.85, 0.95),
        "rejection": (0.95, 0.70, 0.85),
        "bodily exposure": (0.75, 0.90, 0.85),
        "moral tripwire": (0.95, 0.90, 0.75),
    }
    scored = {k: s * e * a for k, (s, e, a) in triggers.items()}
    for k in sorted(scored, key=scored.get, reverse=True):
        print("  %-17s potential %.4f" % (k, scored[k]))
    top = max(scored, key=scored.get)
    print("strongest: %s" % top)
    assert top == "public failure"
    assert 0.7694 < scored["public failure"] < 0.7696
    assert all(0.50 < v < 0.80 for v in scored.values())
    print("OK: %s filed the trigger repertoire" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # single-trial conditioning: cue strength after pairings, then extinction
    strength = 1.0  # bound in one trial at the original scene
    print("cue strength after original scene: %.2f" % strength)
    # safe re-encounters without consequence: extinction
    decay = 0.80
    for i in range(1, 6):
        strength *= decay
        print("  safe encounter %d -> strength %.4f" % (i, strength))
    assert 0.3276 < strength < 0.3278
    # avoidance preserves the minefield: no encounters, no decay
    avoided = 1.0
    print("with total avoidance, strength stays: %.2f" % avoided)
    assert avoided == 1.0
    print("OK: %s mapped the minefield" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the circuit monitors visibility, not valence: visibility scores
    surprises = {
        "public praise": (0.85, 0.90),    # (visibility, positivity)
        "public help": (0.70, 0.80),
        "success spotlight": (0.90, 0.95),
        "intimacy": (0.75, 0.85),
        "nearby laughter": (0.60, 0.30),
        "quiet rest": (0.40, 0.50),
    }
    for k, (vis, pos) in surprises.items():
        risk = vis * (1.0 - pos * 0.30)  # positivity only partly offsets
        print("  %-18s visibility %.2f positivity %.2f -> shame-risk %.3f" % (k, vis, pos, risk))
        assert risk > 0.25  # every surprise input carries real risk
    risks = {k: vis * (1.0 - pos * 0.30) for k, (vis, pos) in surprises.items()}
    assert max(risks, key=risks.get) == "success spotlight"
    assert 0.643 < risks["success spotlight"] < 0.645
    print("OK: %s posted sentries on the unexpected roads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # four amplifiers multiply the original trigger
    trigger = 1.0
    amplifiers = {
        "meta-shame": 1.40,
        "archive replay": 1.60,
        "overgeneralization": 1.50,
        "dread forecast": 1.30,
    }
    level = trigger
    for k, amp in amplifiers.items():
        level *= amp
        print("  after %-16s level %.3f" % (k, level))
    assert 4.367 < level < 4.369  # one fumbled answer becomes a season
    # cutting the earliest fuse collapses the chain
    cut = trigger * 1.0  # meta-shame named and contained
    print("with the first fuse cut: level %.2f" % cut)
    assert cut < level / 4.0
    print("OK: %s cut the fuse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five moves: short-term relief vs long-term interest charged
    moves = {
        "withdrawal": (0.80, 0.70),
        "concealment": (0.65, 0.60),
        "deflection": (0.55, 0.65),
        "overcompensation": (0.50, 0.85),
        "inverted aggression": (0.60, 0.90),
    }
    for k, (relief, cost) in moves.items():
        net = relief - cost
        print("  %-19s relief %.2f cost %.2f net %+.2f" % (k, relief, cost, net))
        assert net < 0.15  # every move charges interest
    nets = {k: r - c for k, (r, c) in moves.items()}
    assert min(nets, key=nets.get) == "overcompensation"
    assert -0.351 < nets["overcompensation"] < -0.349
    print("OK: %s costed the five retreats" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_speech_patterns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # arousal reshapes the voice: volume down, pitch up, pace splits
    arousal = 0.75
    volume = 1.0 - arousal * 0.45   # acoustic footprint shrinks
    pitch = 1.0 + arousal * 0.25    # cords tighten
    print("arousal %.2f -> volume %.3f pitch %.3f" % (arousal, volume, pitch))
    assert 0.6624 < volume < 0.6626
    assert 1.1874 < pitch < 1.1876
    # minimizer density per 100 words, calm vs shamed
    calm_min, shamed_min = 2.0, 14.0
    print("minimizers per 100 words: calm %.0f -> shamed %.0f" % (calm_min, shamed_min))
    assert shamed_min > 5.0 * calm_min
    # the discounting laugh deletes the sentence it follows
    print("OK: %s heard the accent" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_decisions_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # expected value with shame-inflated downside vs true downside
    gain, p_success = 100.0, 0.60
    true_loss, p_fail = 20.0, 0.40
    ev_true = p_success * gain - p_fail * true_loss
    inflated_loss = true_loss * 4.0  # "everyone will see me fail"
    ev_shamed = p_success * gain - p_fail * inflated_loss
    print("true EV: %+.1f   shame-priced EV: %+.1f" % (ev_true, ev_shamed))
    assert 51.9 < ev_true < 52.1
    assert 27.9 < ev_shamed < 28.1
    decide_true = ev_true > 0
    decide_shamed = ev_shamed > 0
    print("decide: true-logic %s, shame-logic %s" % (decide_true, decide_shamed))
    # at higher inflation the veto flips the decision
    ev_severe = p_success * gain - p_fail * (true_loss * 8.0)
    assert ev_severe < 0.0  # the smaller life, chosen as if by preference
    print("OK: %s audited the quiet legislator" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the staircase: cumulative cost of each funded step
    steps = [
        ("freeze", 0.0),
        ("flight", 10.0),
        ("cover-up campaign", 40.0),
        ("counterattack", 120.0),
        ("self-erasure", 400.0),
    ]
    cumulative = 0.0
    for name_, cost in steps:
        cumulative += cost
        print("  %-18s step cost %6.1f cumulative %6.1f" % (name_, cost, cumulative))
    assert 569.9 < cumulative < 570.1
    # early intervention at the freeze costs a fraction
    early = 5.0
    print("meeting it at the freeze: %.1f vs staircase %.1f" % (early, cumulative))
    assert early < cumulative / 100.0
    print("OK: %s priced the staircase" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the three arts close the circuit: residual shame after each step
    residual = 1.0
    print("initial residual: %.2f" % residual)
    for art, cut in [("disclose", 0.35), ("display briefly", 0.20), ("act on the standard", 0.35)]:
        residual *= (1.0 - cut)
        print("  after %-20s residual %.4f" % (art, residual))
    assert 0.337 < residual < 0.339
    # skipping disclosure leaves secrecy feeding the loop
    skipped = 1.0 * (1.0 - 0.20) * (1.0 - 0.35)
    print("skipping disclosure: residual %.3f (secrecy keeps feeding it)" % skipped)
    assert skipped > residual * 1.5
    print("OK: %s closed the circuit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # bottling: arousal stays high while display drops; melting: flood then seal
    days = range(1, 8)
    bottled_arousal = [0.70 + 0.03 * d for d in days]   # accrues
    bottled_display = [max(0.05, 0.40 - 0.05 * d) for d in days]  # the seal holds
    print("bottling over 7 days: arousal %.2f -> %.2f, display %.2f -> %.2f" % (
        bottled_arousal[0], bottled_arousal[-1], bottled_display[0], bottled_display[-1]))
    assert bottled_arousal[-1] > bottled_arousal[0]  # the audience is fooled, the body is not
    assert bottled_display[-1] < bottled_display[0]
    assert 0.909 < bottled_arousal[-1] < 0.911
    # meltdown then tighter seal: the alternating cycle
    flood, seal = 1.0, 0.95
    print("meltdown flood %.1f -> next seal %.2f (tighter than before)" % (flood, seal))
    assert seal > 0.90
    print("OK: %s walked both costly roads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # six practices, each targeting one dial; combined multiplicative effect
    practices = {
        "naming": 0.15,
        "audience audit": 0.20,
        "standard check": 0.25,
        "exposure budget": 0.20,
        "repair reflex": 0.15,
        "body practice": 0.10,
    }
    level = 1.0
    for k, cut in practices.items():
        level *= (1.0 - cut)
        print("  %-16s level %.4f" % (k, level))
    assert 0.311 < level < 0.313  # maintenance compounds quietly
    print("single heroic intervention (one 40%% cut): %.2f" % 0.60)
    assert level < 0.60  # hygiene beats heroics
    print("OK: %s kept the daily orders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # cluster score: cues x context; single cue vs cluster vs cluster+context
    cues = {"gaze drop": 0.7, "mouth press": 0.6, "blush": 0.8, "stillness": 0.5}
    single = max(cues.values())
    cluster = sum(cues.values()) / len(cues)
    context_boost = 1.6  # right after an exposure moment
    reading = min(0.99, cluster * context_boost)
    print("cues: %s" % ", ".join("%s %.1f" % (k, v) for k, v in cues.items()))
    print("single best cue: %.2f  cluster: %.3f  with context: %.3f" % (single, cluster, reading))
    assert 0.649 < cluster < 0.651
    assert reading > single  # context beats the best lone cue
    assert 0.98 < reading < 1.0
    # without context the same cluster reads weaker
    print("same cluster, no exposure context: %.3f" % cluster)
    assert cluster < 0.70
    print("OK: %s read the cluster" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five moves, each lowering one dial of the circuit
    moves = {
        "normalize (audience)": 0.25,
        "ordinary face (threat)": 0.15,
        "specific counter-evidence (verdict)": 0.20,
        "graceful role (belonging)": 0.20,
        "protected exit (trap)": 0.10,
    }
    load = 1.0
    for k, cut in moves.items():
        load *= (1.0 - cut)
        print("  %-32s load %.4f" % (k, load))
    assert 0.367 < load < 0.369
    print("the bond reads intact at load %.2f" % load)
    # the quiet burial: unrehearsed scenes fade faster
    rehearsed, buried = 0.80, 0.30
    assert buried < rehearsed / 2.0
    print("OK: %s walked beside the traveler" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # seven mistakes, each inflating one dial; the cost of good intentions
    mistakes = {
        "spotlighting": ("audience", 1.50),
        "pep-talk overcorrection": ("verdict", 1.30),
        "fix-it rush": ("verdict", 1.25),
        "teasing it light": ("exposure", 1.40),
        "tribunal of concern": ("audience", 1.60),
        "mask mistaken for person": ("verdict", 1.35),
        "keeping score": ("exposure", 1.45),
    }
    dials = {"audience": 1.0, "exposure": 1.0, "verdict": 1.0}
    for m, (dial, mult) in mistakes.items():
        dials[dial] *= mult
        print("  %-24s %s x%.2f -> %.3f" % (m, dial, mult, dials[dial]))
    total = dials["audience"] * dials["exposure"] * dials["verdict"]
    print("combined inflation: %.3f" % total)
    assert 2.399 < dials["audience"] < 2.401
    assert 2.029 < dials["exposure"] < 2.031
    assert 2.193 < dials["verdict"] < 2.195
    assert 10.67 < total < 10.69
    print("OK: %s marked the seven traps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_related_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # classify an event on three axes -> nearest neighbor
    # axes: object (0=act, 1=self), agency (0=self-caused, 1=other-inflicted), tendency
    neighbors = {
        "guilt": (0.15, 0.10, "repair"),
        "shame": (0.90, 0.20, "hide"),
        "embarrassment": (0.55, 0.15, "laugh-off"),
        "humiliation": (0.85, 0.90, "retaliate"),
        "pride": (0.80, 0.30, "expand"),
    }
    event = (0.88, 0.18)  # self judged, self revealed: the classic shame coordinates
    def dist(a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    ranked = sorted(neighbors, key=lambda k: dist(event, neighbors[k][:2]))
    for k in ranked:
        print("  %-14s distance %.3f tendency: %s" % (k, dist(event, neighbors[k][:2]), neighbors[k][2]))
    assert ranked[0] == "shame"
    assert 0.027 < dist(event, neighbors["shame"][:2]) < 0.029
    assert ranked[1] == "pride"  # nearest border: same channels, opposite pole
    print("OK: %s surveyed the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_emotion_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # appraisal fusion: shame core + partner tendency
    shame_core = {"self_under_eyes": 1.0}
    partners = {
        "anger": {"tendency": "attack", "energy": 0.85},
        "fear": {"tendency": "avoid", "energy": 0.75},
        "sadness": {"tendency": "withdraw", "energy": 0.60},
        "disgust": {"tendency": "expel", "energy": 0.70},
        "joy": {"tendency": "approach", "energy": 0.65},
    }
    names = {
        "anger": "humiliated fury", "fear": "anticipatory dread",
        "sadness": "heavy withdraw", "disgust": "self-contamination",
        "joy": "bittersweet wince",
    }
    for p, d in partners.items():
        blend = shame_core["self_under_eyes"] * d["energy"]
        print("  shame + %-7s = %-19s tendency %-8s strength %.3f" % (p, names[p], d["tendency"], blend))
        assert 0.59 < blend < 0.86
    blends = {p: d["energy"] for p, d in partners.items()}
    assert max(blends, key=blends.get) == "anger"  # the hottest alloy
    print("OK: %s assayed the alloys" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shame_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five scenes: shame level across Dev's arc
    scenes = [
        ("trigger", 0.75),
        ("peak", 1.00),
        ("cascade", 0.95),
        ("turn", 0.45),
        ("resolution", 0.15),
    ]
    for name_, level in scenes:
        bar = "#" * int(level * 20)
        print("  %-11s [%s] %.2f" % (name_, bar, level))
    levels = [lv for _, lv in scenes]
    assert levels[1] == max(levels)          # the peak is the worst
    assert levels[-1] < levels[1] / 5.0       # resolution drains it
    assert levels[2] > levels[3]              # the turn breaks the cascade
    drop = levels[1] - levels[-1]
    print("peak-to-resolution drop: %.2f" % drop)
    assert 0.849 < drop < 0.851
    print("OK: %s ran the showcase simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "shame_definition": demo_shame_definition,
    "shame_emotion_family": demo_shame_emotion_family,
    "shame_intensity_scale": demo_shame_intensity_scale,
    "shame_myths": demo_shame_myths,
    "shame_first_person": demo_shame_first_person,
    "shame_time_course": demo_shame_time_course,
    "shame_low_vs_high": demo_shame_low_vs_high,
    "shame_guilt_blend": demo_shame_guilt_blend,
    "shame_day_vignette": demo_shame_day_vignette,
    "shame_body_signals": demo_shame_body_signals,
    "shame_posture_movement": demo_shame_posture_movement,
    "shame_sleep_appetite_energy": demo_shame_sleep_appetite_energy,
    "shame_body_differences": demo_shame_body_differences,
    "shame_face": demo_shame_face,
    "shame_face_intensity": demo_shame_face_intensity,
    "shame_hiding_faking": demo_shame_hiding_faking,
    "shame_expression_gallery": demo_shame_expression_gallery,
    "shame_classic_triggers": demo_shame_classic_triggers,
    "shame_personal_triggers": demo_shame_personal_triggers,
    "shame_surprise_triggers": demo_shame_surprise_triggers,
    "shame_chain_reactions": demo_shame_chain_reactions,
    "shame_behavior_actions": demo_shame_behavior_actions,
    "shame_speech_patterns": demo_shame_speech_patterns,
    "shame_decisions_judgment": demo_shame_decisions_judgment,
    "shame_escalation": demo_shame_escalation,
    "shame_healthy_expression": demo_shame_healthy_expression,
    "shame_unhealthy_expression": demo_shame_unhealthy_expression,
    "shame_everyday_practices": demo_shame_everyday_practices,
    "shame_reading_others": demo_shame_reading_others,
    "shame_supportive_responses": demo_shame_supportive_responses,
    "shame_mistakes_to_avoid": demo_shame_mistakes_to_avoid,
    "shame_related_emotions": demo_shame_related_emotions,
    "shame_emotion_mixes": demo_shame_emotion_mixes,
    "shame_full_simulation": demo_shame_full_simulation,
}
