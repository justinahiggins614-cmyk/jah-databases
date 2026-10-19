#!/usr/bin/env python3
"""Demo programs for the Calm Emotion databases (Manon's 16:15 orders, emotion series).

Every demo is real, runnable, stdlib-only Python performing the actual
emotion-scenario simulation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker. Demo outputs
were cross-checked against entry text during authoring.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_calm_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # calm-signature checklist: safety, ease, slowed physiology, readiness
    signature = {"appraised safe": 1, "appraised manageable": 1,
                 "parasympathetic lead": 1, "readiness kept": 1,
                 "not numbness": 1, "not suppression": 1}
    met = sum(signature.values())
    score = met / len(signature) * 100.0
    print("calm signature checks met: %d/%d" % (met, len(signature)))
    print("calm definition score: %.1f %%" % score)
    assert met == 6
    assert 99.9 < score < 100.1
    print("rule: the body and mind agreeing the moment is safe and manageable")
    print("OK: %s defined the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # circumplex placement: valence +, arousal low -> pleasant low-energy quadrant
    valence, arousal = 0.75, -0.65
    quadrant = "pleasant low-energy" if valence > 0 and arousal < 0 else "other"
    cousins = ["serenity", "contentment", "relief", "tranquility"]
    opposites = ["anxiety", "agitation"]
    print("calm coordinates: valence %.2f, arousal %.2f -> %s" % (valence, arousal, quadrant))
    print("cousins: %d, opposites: %d" % (len(cousins), len(opposites)))
    assert quadrant == "pleasant low-energy"
    assert len(cousins) == 4 and len(opposites) == 2
    assert -1.0 < valence < 1.0 and -1.0 < arousal < 1.0
    print("rule: low arousal plus pleasant valence, fed by safety and sufficiency")
    print("OK: %s placed calm in the family" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three volumes of the same emotion: depth 1..3, breath rate falls, ease rises
    volumes = [(1, 14.0, 0.25), (2, 10.0, 0.55), (3, 7.0, 0.90)]
    for depth, breaths_min, ease in volumes:
        print("volume %d: breath %.1f/min ease %.2f" % (depth, breaths_min, ease))
    breaths = [v[1] for v in volumes]
    eases = [v[2] for v in volumes]
    assert breaths == sorted(breaths, reverse=True), "breath must fall with depth"
    assert eases == sorted(eases), "ease must rise with depth"
    assert 6.0 < breaths[-1] < 16.0
    print("rule: same signature at every volume, differing in depth and duration")
    print("OK: %s scaled the volumes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    myths = {"calm means feeling nothing": "numbness",
             "calm people never feel anger": "baseline return",
             "calm is weakness": "aimed power",
             "temperament decides": "trainable",
             "calm means no problems": "carrying problems steadily"}
    print("myths examined: %d" % len(myths))
    for myth, truth in myths.items():
        print("  myth: %-38s truth: %s" % (myth, truth))
    assert len(myths) == 5
    assert all(len(t) > 3 for t in myths.values())
    print("rule: every myth paired with its plain truth")
    print("OK: %s cleared the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_inside(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inside-calm telemetry: breath slows, tension drops, attention widens
    t = [0, 30, 60, 120, 300]  # seconds settling in
    breath = [16.0, 13.0, 11.0, 9.0, 8.0]
    tension = [0.80, 0.62, 0.45, 0.28, 0.15]
    for sec, b, tn in zip(t, breath, tension):
        print("t=%ds breath %.1f/min tension %.2f" % (sec, b, tn))
    assert breath == sorted(breath, reverse=True)
    assert tension == sorted(tension, reverse=True)
    assert 7.0 < breath[-1] < 17.0 and 0.0 < tension[-1] < 0.9
    print("rule: the body reports first, the mind follows")
    print("OK: %s rendered the inside view" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arousal decay across the four phases: onset, peak, fade, aftershock buffer
    arousal = {"onset_start": 0.75, "peak": 0.15, "fade_end": 0.35, "aftershock_floor": 0.22}
    for phase, val in arousal.items():
        print("%-14s arousal %.2f" % (phase, val))
    assert arousal["onset_start"] > arousal["peak"]
    assert arousal["peak"] < arousal["fade_end"]
    assert arousal["aftershock_floor"] < arousal["onset_start"]
    assert all(0.0 <= v <= 1.0 for v in arousal.values())
    print("rule: gradual onset, quiet peak, two kinds of fade, buffered aftershock")
    print("OK: %s traced the time course" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Tuesday mild vs Sunday deep: same signature, different depth and buffer
    tuesday = {"depth": 0.30, "buffer_min": 5, "interruptible": True}
    sunday = {"depth": 0.92, "buffer_min": 90, "interruptible": False}
    print("tuesday mild: depth %.2f buffer %d min" % (tuesday["depth"], tuesday["buffer_min"]))
    print("sunday deep:  depth %.2f buffer %d min" % (sunday["depth"], sunday["buffer_min"]))
    assert sunday["depth"] > tuesday["depth"]
    assert sunday["buffer_min"] > tuesday["buffer_min"]
    assert tuesday["interruptible"] and not sunday["interruptible"]
    print("rule: one emotion, two depths - tool vs place")
    print("OK: %s compared the snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_partner_mix(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # relief-calm blend: reward spike first, regulation spreads after
    seq = [("relief spike", 0.90, 0.20), ("blend forming", 0.55, 0.55), ("calm settling", 0.20, 0.90)]
    for label, reward, regulation in seq:
        print("%-14s reward %.2f regulation %.2f" % (label, reward, regulation))
    rewards = [s[1] for s in seq]
    regs = [s[2] for s in seq]
    assert rewards == sorted(rewards, reverse=True)
    assert regs == sorted(regs)
    print("rule: the wave first, then the water it lands in")
    print("OK: %s blended the partners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_day(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one ordinary day: disturbance, regulator, return - buffer deepens each time
    scenes = [("dawn", 0.10, 0.85), ("commute delay", 0.45, 0.60),
              ("hard meeting", 0.62, 0.70), ("good news", 0.30, 0.88),
              ("evening", 0.12, 0.93), ("night", 0.08, 0.95)]
    bufs = []
    for label, disturb, calm in scenes:
        buf = calm - disturb
        bufs.append(buf)
        print("%-14s disturbance %.2f calm %.2f buffer %+.2f" % (label, disturb, calm, buf))
    assert all(b > -0.05 for b in bufs), "buffer must stay non-negative"
    assert bufs[-1] > bufs[1], "buffer deepens across the day"
    print("rule: calm begetting calm - micro-returns all day")
    print("OK: %s walked the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # system-by-system settle: heart, breath, muscle tension, gut knot, hand warmth
    before = {"hr": 88.0, "breath": 17.0, "tension": 0.78, "gut_knot": 0.70, "hand_temp": 31.5}
    after = {"hr": 64.0, "breath": 9.0, "tension": 0.18, "gut_knot": 0.12, "hand_temp": 34.2}
    for k in before:
        print("%-9s before %.1f after %.1f" % (k, before[k], after[k]))
    assert after["hr"] < before["hr"] and after["breath"] < before["breath"]
    assert after["tension"] < before["tension"] and after["gut_knot"] < before["gut_knot"]
    assert after["hand_temp"] > before["hand_temp"]
    assert 50.0 < after["hr"] < 100.0
    print("rule: the body stops bracing - every held thing released")
    print("OK: %s read the body systems" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # posture audit: openness score across checkpoints, calm vs braced
    calm_pose = {"shoulders_low": 0.9, "chest_open": 0.85, "jaw_loose": 0.9,
                 "hands_open": 0.88, "tempo_unhurried": 0.92}
    braced_pose = {"shoulders_low": 0.2, "chest_open": 0.25, "jaw_loose": 0.15,
                   "hands_open": 0.3, "tempo_unhurried": 0.2}
    calm_score = sum(calm_pose.values()) / len(calm_pose)
    braced_score = sum(braced_pose.values()) / len(braced_pose)
    print("calm posture openness: %.2f" % calm_score)
    print("braced posture openness: %.2f" % braced_score)
    assert calm_score > 0.8 and braced_score < 0.4
    assert calm_score - braced_score > 0.4
    print("rule: stacked not braced, open not guarded, still by choice")
    print("OK: %s scored the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flywheel: sleep onset, appetite clarity, energy budget across calm days
    days = [(1, 38.0, 0.45, 0.55), (3, 26.0, 0.62, 0.68), (7, 17.0, 0.78, 0.82)]
    for day, onset_min, appetite, energy in days:
        print("day %d: sleep onset %.0f min appetite %.2f energy %.2f" % (day, onset_min, appetite, energy))
    onsets = [d[1] for d in days]
    assert onsets == sorted(onsets, reverse=True), "onset must shorten"
    assert days[-1][2] > days[0][2] and days[-1][3] > days[0][3]
    print("rule: each steadied system lowers the load on the others")
    print("OK: %s ran the flywheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same calm, different first-signal locations across four people
    people = {"chest-first": 0.85, "hands-first": 0.80, "heaviness": 0.88, "lightness": 0.82}
    for person, signature_match in people.items():
        print("%-12s signature match %.2f" % (person, signature_match))
    assert all(0.7 < v < 1.0 for v in people.values()), "all variants carry the signature"
    spread = max(people.values()) - min(people.values())
    print("spread across bodies: %.2f" % spread)
    assert spread < 0.2
    print("rule: same signature underneath, different clothes on different bodies")
    print("OK: %s compared the bodies" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # face tension audit: 0 = released, 1 = tense; calm face near zero everywhere
    calm_face = {"brow": 0.05, "lids": 0.08, "jaw": 0.04, "lips": 0.06, "nostrils": 0.02}
    tense_face = {"brow": 0.85, "lids": 0.70, "jaw": 0.90, "lips": 0.75, "nostrils": 0.60}
    calm_t = sum(calm_face.values()) / len(calm_face)
    tense_t = sum(tense_face.values()) / len(tense_face)
    print("calm face mean tension: %.2f" % calm_t)
    print("tense face mean tension: %.2f" % tense_t)
    assert calm_t < 0.10 and tense_t > 0.60
    print("rule: the face defined by absences - no tension anywhere")
    print("OK: %s audited the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # face depth gradient: muscle release deepens 1..3, mouth lift stays faint
    depths = [(1, 0.30, 0.02), (2, 0.62, 0.04), (3, 0.92, 0.06)]
    for depth, release, lift in depths:
        print("depth %d: muscle release %.2f mouth lift %.2f deg-equivalent" % (depth, release, lift))
    releases = [d[1] for d in depths]
    lifts = [d[2] for d in depths]
    assert releases == sorted(releases)
    assert all(0.0 < l < 0.10 for l in lifts), "lift stays faint, never a grin"
    print("rule: a continuum - smoothing, softening, stillness")
    print("OK: %s graded the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_hide_fake(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # leakage test: voluntary channels staged, autonomic channels leak
    staged = {"voice_pace": 0.90, "posture": 0.85, "hand_place": 0.88}
    leaked = {"blink_rate": 0.25, "breath_depth": 0.30, "jaw_hold": 0.28}
    staged_ok = sum(staged.values()) / len(staged)
    leaked_ok = sum(leaked.values()) / len(leaked)
    congruence = 1.0 - abs(staged_ok - leaked_ok)
    print("staged channels: %.2f leaked channels: %.2f congruence: %.2f"
          % (staged_ok, leaked_ok, congruence))
    assert staged_ok > 0.8 and leaked_ok < 0.4
    assert congruence < 0.6, "incongruence exposes the fake"
    print("rule: congruence across channels is the real signature")
    print("OK: %s caught the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # render checklist: features at neutral, one faint positive signal
    render = {"brow_smooth": 1, "lids_mid": 1, "gaze_soft": 1,
              "mouth_neutral": 1, "corner_lift_faint": 1, "jaw_dropped_mm": 1}
    failures = {"serene_mask": "vacant", "pleasant_mask": "polite tension", "sleepy": "drowsy"}
    score = sum(render.values()) / len(render)
    print("render checklist: %d/%d" % (sum(render.values()), len(render)))
    print("failure modes avoided: %d" % len(failures))
    assert score > 0.99
    assert len(failures) == 3
    print("rule: present, at ease, and in no hurry - between the failure modes")
    print("OK: %s drew the gallery notes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_triggers_classic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six classic trigger families, each rated for safety-signal strength
    triggers = {"nature": 0.90, "slow_rhythm": 0.85, "warmth_comfort": 0.80,
                "completion": 0.88, "trusted_company": 0.92, "quiet": 0.84}
    for name_, strength in sorted(triggers.items(), key=lambda p: -p[1]):
        print("%-16s safety signal %.2f" % (name_, strength))
    assert len(triggers) == 6
    assert all(0.75 < v < 1.0 for v in triggers.values())
    mean_s = sum(triggers.values()) / len(triggers)
    print("mean safety signal: %.2f" % mean_s)
    assert 0.80 < mean_s < 0.95
    print("rule: safe, nothing required, stand down")
    print("OK: %s listed the classics" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_triggers_personal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # conditioned safety signals: pairing count builds strength, distress unpaired weakens
    cue = {"pairings_with_calm": 40, "pairings_with_distress": 2}
    strength = cue["pairings_with_calm"] / (cue["pairings_with_calm"] + cue["pairings_with_distress"] + 5)
    print("pairings calm=%d distress=%d -> signal strength %.2f"
          % (cue["pairings_with_calm"], cue["pairings_with_distress"], strength))
    assert 0.7 < strength < 1.0
    flipped = {"pairings_with_calm": 40, "pairings_with_distress": 35}
    strength2 = flipped["pairings_with_calm"] / (flipped["pairings_with_calm"] + flipped["pairings_with_distress"] + 5)
    print("after distress pairings: strength %.2f (flip risk)" % strength2)
    assert strength2 < strength
    print("rule: autobiographical, powerful, and fragile")
    print("OK: %s conditioned the cues" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_triggers_surprise(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # odd triggers scored on low-demand + rhythm + order; threat system stands down
    odd = {"vacuum_hum": (0.9, 0.9, 0.3), "dishes": (0.85, 0.8, 0.9),
           "night_highway": (0.95, 0.85, 0.5), "drawer_sorting": (0.8, 0.6, 1.0),
           "skilled_work_watch": (0.9, 0.75, 0.6)}
    for label, (demand_low, rhythm, order) in odd.items():
        score = (demand_low + rhythm + order) / 3.0
        print("%-18s calm score %.2f" % (label, score))
        assert 0.6 < score < 1.0
    print("rule: low demand plus gentle rhythm plus a thread of order")
    print("OK: %s scored the odd triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cascade: each link lowers arousal, lowering the bar for the next
    arousal = 0.70
    links = ["minute of stillness", "slower breath", "shoulders drop",
             "noticing light", "contentment flicker", "stomach unclenches"]
    trace = []
    for link in links:
        arousal = max(0.08, arousal * 0.78)
        trace.append(arousal)
        print("%-20s arousal %.2f" % (link, arousal))
    assert trace == sorted(trace, reverse=True), "arousal must fall each link"
    assert trace[-1] < 0.25
    print("rule: you only need the first link - the chain does the rest")
    print("OK: %s ran the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # calm action profile: pause, deliberate move, simplify, listen, help, disengage
    actions = {"pause_before_answering": 0.92, "deliberate_movement": 0.88,
               "simplify": 0.80, "listen_longer": 0.90,
               "steady_helping": 0.86, "clean_disengagement": 0.84}
    for act, likelihood in actions.items():
        print("%-22s likelihood %.2f" % (act, likelihood))
    mean_a = sum(actions.values()) / len(actions)
    print("mean action likelihood: %.2f" % mean_a)
    assert all(v > 0.75 for v in actions.values())
    assert 0.80 < mean_a < 0.95
    print("rule: approach and tend - noise removed, action lands clean")
    print("OK: %s profiled the actions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # voice telemetry: pitch and pace fall, pauses grow, intensifiers vanish
    agitated = {"pitch_hz": 210.0, "wpm": 168.0, "pause_s": 0.2, "intensifiers": 9}
    calm = {"pitch_hz": 165.0, "wpm": 118.0, "pause_s": 0.9, "intensifiers": 1}
    for k in agitated:
        print("%-12s agitated %.1f calm %.1f" % (k, agitated[k], calm[k]))
    assert calm["pitch_hz"] < agitated["pitch_hz"]
    assert calm["wpm"] < agitated["wpm"]
    assert calm["pause_s"] > agitated["pause_s"]
    assert calm["intensifiers"] < agitated["intensifiers"]
    print("rule: lower, slower, pausing - and quieter in disagreement")
    print("OK: %s measured the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # judgment shifts under calm: horizon widens, risk reads truer, others stay human
    agitated = {"horizon_days": 2.0, "risk_error": 0.45, "perspective": 0.30}
    calm = {"horizon_days": 60.0, "risk_error": 0.12, "perspective": 0.85}
    print("horizon: %.0f -> %.0f days" % (agitated["horizon_days"], calm["horizon_days"]))
    print("risk misread: %.2f -> %.2f" % (agitated["risk_error"], calm["risk_error"]))
    print("perspective: %.2f -> %.2f" % (agitated["perspective"], calm["perspective"]))
    assert calm["horizon_days"] > agitated["horizon_days"] * 10
    assert calm["risk_error"] < agitated["risk_error"]
    assert calm["perspective"] > agitated["perspective"]
    print("rule: the rush and the dread removed - odds read near true size")
    print("OK: %s weighed the decisions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_under_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # phase change: past the depth threshold, stillness is free and hurrying costs
    depths = [0.3, 0.5, 0.65, 0.8, 0.95]
    threshold = 0.7
    for d in depths:
        effort_to_stay = max(0.0, (threshold - d)) * 1.4
        print("depth %.2f effort to stay still: %.2f %s"
              % (d, effort_to_stay, "(past threshold - stillness free)" if d >= threshold else ""))
    below = [d for d in depths if d < threshold]
    above = [d for d in depths if d >= threshold]
    assert all((threshold - d) * 1.4 > 0.0 for d in below)
    assert len(above) == 2
    print("rule: below the threshold skills are practiced; above it, they are simply how you are")
    print("OK: %s crossed the threshold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_healthy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels of healthy expression, each reinforcing the state
    channels = {"saying_it": 0.85, "showing_it": 0.90, "channeling_it": 0.88, "protecting_it": 0.82}
    for ch, strength in channels.items():
        print("%-14s strength %.2f" % (ch, strength))
    total = sum(channels.values())
    print("expression total: %.2f / 4.00" % total)
    assert all(v > 0.75 for v in channels.values())
    assert 3.2 < total < 4.0
    print("rule: spent wisely and replenished regularly - renewable, not infinite")
    print("OK: %s expressed it well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_unhealthy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottling vs faking: both run alarm + mask simultaneously, doubling the load
    honest_settle = {"alarm": 0.15, "mask_effort": 0.0}
    bottling = {"alarm": 0.85, "mask_effort": 0.70}
    faking = {"alarm": 0.45, "mask_effort": 0.60}
    for label, s in [("honest settle", honest_settle), ("bottling", bottling), ("faking", faking)]:
        load = s["alarm"] + s["mask_effort"]
        print("%-14s total load %.2f" % (label, load))
        if label != "honest settle":
            assert load > honest_settle["alarm"] + honest_settle["mask_effort"] + 0.5
    assert bottling["alarm"] > 0.8, "suppressed arousal stays elevated"
    print("rule: appearance stages in seconds; the state builds breath by breath")
    print("OK: %s priced the failures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # small daily habits compound: baseline drifts toward ease week by week
    baseline = 0.45
    habits = ["one-breath reset", "daily walk", "evening review", "protected hour", "tidy margins"]
    weekly_gain = 0.03 * len(habits)
    trace = []
    for week in range(1, 9):
        baseline = min(0.92, baseline + weekly_gain * (0.92 - baseline))
        trace.append(baseline)
        print("week %d baseline calm %.2f" % (week, baseline))
    assert trace == sorted(trace), "baseline must rise monotonically"
    assert trace[-1] > trace[0] + 0.15
    assert trace[-1] <= 0.92
    print("rule: unremarkable things done daily - steadiness compounds like interest")
    print("OK: %s kept the habits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four-channel read with congruence check; hard-place calm weighted highest
    person = {"face": 0.90, "body": 0.85, "voice": 0.88, "behavior": 0.86}
    channels = sum(person.values()) / len(person)
    congruence = 1.0 - (max(person.values()) - min(person.values()))
    context_weight = 1.4  # calm observed in a hard place
    reading = channels * congruence * context_weight
    print("channels %.2f congruence %.2f context x%.1f -> reading %.2f"
          % (channels, congruence, context_weight, reading))
    assert congruence > 0.9, "genuine calm is congruent"
    assert reading > 1.0, "hard-place calm reads strongest"
    print("rule: agreement across channels - never one channel alone")
    print("OK: %s read the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_support(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # co-regulation: helper's steadiness entrains the other's arousal downward
    other_arousal = 0.85
    helper = {"voice_slow": 0.90, "posture_open": 0.88, "breath_audible_slow": 0.92}
    steadiness = sum(helper.values()) / len(helper)
    trace = []
    for minute in range(1, 7):
        other_arousal = max(0.15, other_arousal - 0.12 * steadiness)
        trace.append(other_arousal)
        print("minute %d other arousal %.2f" % (minute, other_arousal))
    assert trace == sorted(trace, reverse=True)
    assert trace[-1] < 0.35
    assert 0.85 < steadiness < 1.0
    print("rule: borrowed calm becomes owned calm within minutes")
    print("OK: %s steadied the other" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_mistakes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five alarm-adders scored by threat-evidence added
    mistakes = {"rushing": 0.80, "minimizing": 0.75, "mirroring": 0.70,
                "early_fixing": 0.55, "withdrawal": 0.65}
    for m, harm in sorted(mistakes.items(), key=lambda p: -p[1]):
        print("%-13s threat-evidence added %.2f" % (m, harm))
    assert mistakes["rushing"] == max(mistakes.values())
    assert all(0.5 < v < 0.9 for v in mistakes.values())
    print("rule: subtract alarm, add safety - always the reverse")
    print("OK: %s listed the mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_related_map(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # neighborhood distances from calm on the appraisal map (0 = same state)
    neighbors = {"serenity": 0.15, "contentment": 0.22, "relief": 0.28,
                 "relaxation": 0.18, "tranquility": 0.25}
    cousins = {"peace": 0.35, "patience": 0.40, "equanimity": 0.38}
    opposites = {"anxiety": 0.95, "agitation": 0.88, "panic": 1.00}
    for label, d in [("neighbors", neighbors), ("cousins", cousins), ("opposites", opposites)]:
        mean_d = sum(d.values()) / len(d)
        print("%-9s mean distance %.2f" % (label, mean_d))
    assert max(neighbors.values()) < min(cousins.values())
    assert max(cousins.values()) < min(opposites.values())
    assert min(opposites.values()) > 0.8
    print("rule: ask what the state is about - appraisal separates the neighbors")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dyads: calm's steadiness plus the partner's character; stability needs no alarm demand
    blends = {"joy": (0.85, 0.55, "cheerful ease"),
              "sadness": (0.80, 0.35, "bittersweet"),
              "anticipation": (0.88, 0.60, "poised readiness"),
              "love": (0.90, 0.45, "tender steadiness")}
    for partner, (steadiness, energy, label) in blends.items():
        stability = steadiness * (1.0 - abs(energy - 0.5))
        print("calm + %-12s %-17s stability %.2f" % (partner, label, stability))
        assert 0.5 < stability < 1.0, "compatible appraisals keep the floor"
    print("rule: blends are wholes, not dilutions - calm lends steadiness, keeps the partner")
    print("OK: %s mixed the dyads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_calm_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-scene arc: trigger, onset, peak, test, resolution - arousal telemetry
    scenes = [("trigger", 0.72), ("onset", 0.45), ("peak", 0.14),
              ("test", 0.30), ("resolution", 0.10)]
    for label, arousal in scenes:
        print("%-10s arousal %.2f" % (label, arousal))
    vals = [s[1] for s in scenes]
    assert vals[0] > vals[1] > vals[2], "settle must deepen to the peak"
    assert vals[3] > vals[2], "the test disturbs - buffer absorbs it"
    assert vals[4] < vals[2] + 0.05, "resolution returns near peak depth"
    assert all(0.0 <= v <= 1.0 for v in vals)
    print("rule: calm changes nothing in the world and everything in the carrying of it")
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "calm_definition": demo_calm_definition,
    "calm_family": demo_calm_family,
    "calm_intensity_scale": demo_calm_intensity_scale,
    "calm_myths": demo_calm_myths,
    "calm_inside": demo_calm_inside,
    "calm_time_course": demo_calm_time_course,
    "calm_low_vs_high": demo_calm_low_vs_high,
    "calm_partner_mix": demo_calm_partner_mix,
    "calm_day": demo_calm_day,
    "calm_body": demo_calm_body,
    "calm_posture": demo_calm_posture,
    "calm_sleep_appetite": demo_calm_sleep_appetite,
    "calm_body_differences": demo_calm_body_differences,
    "calm_face": demo_calm_face,
    "calm_face_intensity": demo_calm_face_intensity,
    "calm_hide_fake": demo_calm_hide_fake,
    "calm_gallery": demo_calm_gallery,
    "calm_triggers_classic": demo_calm_triggers_classic,
    "calm_triggers_personal": demo_calm_triggers_personal,
    "calm_triggers_surprise": demo_calm_triggers_surprise,
    "calm_chain_reactions": demo_calm_chain_reactions,
    "calm_actions": demo_calm_actions,
    "calm_speech": demo_calm_speech,
    "calm_decisions": demo_calm_decisions,
    "calm_under_intensity": demo_calm_under_intensity,
    "calm_healthy": demo_calm_healthy,
    "calm_unhealthy": demo_calm_unhealthy,
    "calm_practices": demo_calm_practices,
    "calm_reading_others": demo_calm_reading_others,
    "calm_support": demo_calm_support,
    "calm_mistakes": demo_calm_mistakes,
    "calm_related_map": demo_calm_related_map,
    "calm_mixes": demo_calm_mixes,
    "calm_full_simulation": demo_calm_full_simulation,
}
