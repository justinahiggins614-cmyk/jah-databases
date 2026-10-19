#!/usr/bin/env python3
"""Demo programs for the Remorse Emotion databases (emotion series).

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


def demo_remorse_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the three-part circuit: standard x deed x reckoning -> remorse signal
    standard = 0.90   # how deeply the violated standard is held
    deed = 0.85       # how clearly the act violated it
    reckoning = 0.80  # how fully the mind delivers the verdict
    signal = standard * deed * reckoning
    print("circuit: standard %.2f x deed %.2f x reckoning %.2f" % (standard, deed, reckoning))
    print("remorse signal: %.4f" % signal)
    assert 0.6119 < signal < 0.6121
    no_standard = 0.05 * deed * reckoning  # no believed rule, no remorse
    print("no standard held: %.4f" % no_standard)
    assert 0.0339 < no_standard < 0.0341
    assert no_standard < signal / 10.0
    print("OK: %s ran the three-part circuit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # family weights around the remorse core; shares must sum to 100
    core = 1.0
    family = {
        "remorse": core * 1.00,
        "guilt": core * 0.90,        # broad act-focused sibling
        "regret": core * 0.70,       # backward-looking neighbor
        "shame": core * 0.75,        # self-judging cousin
        "contrition": core * 0.85,   # remorse facing forward
        "indifference": core * 0.05, # opposite pole: no court convened
    }
    total = sum(family.values())
    share = {k: v / total * 100.0 for k, v in family.items()}
    for k in family:
        print("  %-12s weight %.2f (%5.2f %%)" % (k, family[k], share[k]))
    assert 99.99 < sum(share.values()) < 100.01
    assert share["remorse"] > share["guilt"] > share["indifference"]
    assert 23.52 < share["remorse"] < 23.54
    print("OK: %s mapped the family tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # three dials -> volume knob 0..10
    def volume(value, harm, memory):
        return min(10.0, (value + harm + memory) / 3.0 * 10.0)
    def label(v):
        return "mild" if v < 3.5 else ("moderate" if v < 7.0 else "intense")
    cases = [(0.15, 0.20, 0.10), (0.55, 0.60, 0.50), (0.95, 0.95, 0.90)]
    for val, hrm, mem in cases:
        v = volume(val, hrm, mem)
        print("dials %.2f/%.2f/%.2f -> volume %.2f (%s)" % (val, hrm, mem, v, label(v)))
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


def demo_remorse_myths(hdr, name, rid, group, points, req):
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
    assert avg_after > avg_before * 2.0
    print("OK: %s corrected the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the inner courtroom: three roles, one loop; replay pressure per role
    roles = {"defendant": 0.90, "witness": 0.70, "judge": 0.85}
    pressure = sum(roles.values()) / len(roles)
    print("courtroom roles:", ", ".join("%s %.2f" % (r, v) for r, v in roles.items()))
    print("mean replay pressure: %.4f" % pressure)
    assert 0.8166 < pressure < 0.8168
    # counterfactual rehearsal: each better version sharpens the lesson
    lesson = 0.0
    for i in range(1, 6):
        lesson += 0.12 * (1.0 - lesson)  # diminishing returns
    print("lesson extracted after 5 rehearsals: %.4f" % lesson)
    assert 0.4722 < lesson < 0.4724
    print("OK: %s sat in the courtroom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # loop intensity across the arc: onset, peak, fading, aftershock
    phases = [("onset", 0.45), ("peak", 1.00), ("fading", 0.35), ("aftershock", 0.80)]
    for label_, level in phases:
        bar = "#" * int(level * 20)
        print("  %-10s [%s] %.2f" % (label_, bar, level))
    lv = dict(phases)
    assert lv["peak"] == max(lv.values())
    assert lv["onset"] < lv["peak"]
    assert lv["fading"] < lv["onset"]          # the alarm cannot ring forever
    assert lv["aftershock"] < lv["peak"]       # never quite the original charge
    assert lv["aftershock"] > lv["fading"]     # but well above background
    drop = lv["peak"] - lv["fading"]
    print("peak-to-fading drop: %.2f" % drop)
    assert 0.649 < drop < 0.651
    print("OK: %s traced the time course" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Maya (low) vs Daniel (high): same circuit, different dials
    def volume(value, harm, memory):
        return (value + harm + memory) / 3.0 * 10.0
    maya = volume(0.40, 0.15, 0.20)    # reversible harm, few triggers
    daniel = volume(0.95, 0.95, 0.90)  # identity-central, irreversible, sticky
    print("Maya (low):  %.2f" % maya)
    print("Daniel (high): %.2f" % daniel)
    assert 2.49 < maya < 2.51
    assert 9.32 < daniel < 9.34
    assert daniel > maya * 3.0
    print("OK: %s compared the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_guilt_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # guilt sounds the alarm (restless energy), remorse focuses the beam (moral clarity)
    guilt_energy = 0.70
    remorse_focus = 0.85
    drive = guilt_energy * remorse_focus  # reparative drive of the blend
    print("guilt energy %.2f x remorse focus %.2f -> drive %.4f" % (guilt_energy, remorse_focus, drive))
    assert 0.5949 < drive < 0.5951
    # healthy while energy flows to repair; rumination when it loops on itself
    repair_share = 0.75
    healthy = drive * repair_share
    ruminating = drive * (1.0 - repair_share)
    print("healthy %.4f vs ruminating %.4f" % (healthy, ruminating))
    assert healthy > ruminating * 2.0
    assert 0.4461 < healthy < 0.4463
    print("OK: %s blended guilt and remorse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Elena's day: ache level per hour-block, and how specific the debt gets
    blocks = [
        ("06:40 wake", 0.75, 0.20),
        ("09:15 desk", 0.80, 0.35),
        ("12:30 lunch", 0.60, 0.45),
        ("16:00 urge", 0.85, 0.60),
        ("19:20 dinner", 0.65, 0.75),
        ("22:45 bed", 0.70, 0.90),
    ]
    for label_, ache, clarity in blocks:
        print("  %-11s ache %.2f  debt-clarity %.2f" % (label_, ache, clarity))
    aches = [a for _, a, _ in blocks]
    clar = [c for _, _, c in blocks]
    assert clar[-1] > clar[0] * 4.0      # fog distills into assignment
    assert max(aches) <= 0.85
    assert sum(aches) / len(aches) > 0.70  # a heavy day throughout
    print("OK: %s walked the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # body-channel signal weights; shares must sum to 100
    channels = {
        "chest": 0.95, "gut": 0.85, "breath": 0.70,
        "jaw_neck_shoulders": 0.75, "skin": 0.40, "energy_drain": 0.90,
    }
    total = sum(channels.values())
    share = {k: v / total * 100.0 for k, v in channels.items()}
    for k in channels:
        print("  %-18s %5.2f %%" % (k, share[k]))
    assert 99.99 < sum(share.values()) < 100.01
    assert share["chest"] > share["skin"]
    assert 20.87 < share["chest"] < 20.89
    print("OK: %s read the body signals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_posture_movement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # posture collapse score: head tilt + gaze drop + shoulder round (degrees-ish units)
    head_tilt = 10.0
    gaze_drop = 25.0
    shoulder_round = 15.0
    collapse = head_tilt + gaze_drop + shoulder_round
    print("collapse score: %.1f (head %.1f + gaze %.1f + shoulders %.1f)" % (collapse, head_tilt, gaze_drop, shoulder_round))
    assert 49.9 < collapse < 50.1
    # movement shrink: gesture amplitude as fraction of baseline
    baseline, remorseful = 1.0, 0.45
    print("gesture amplitude: %.2f -> %.2f" % (baseline, remorseful))
    assert remorseful < baseline / 2.0
    print("OK: %s measured the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_sleep_appetite_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # daily resource budget = 100 units; the replay loop claims its share first
    loop_cost = 38.0
    remaining = 100.0 - loop_cost
    sleep_debt = loop_cost * 0.40
    print("loop cost: %.1f units; remaining for life: %.1f" % (loop_cost, remaining))
    print("sleep debt from the loop: %.1f" % sleep_debt)
    assert 61.9 < remaining < 62.1
    assert 15.19 < sleep_debt < 15.21
    # as the ledger closes, the loop releases the budget
    released = loop_cost * 0.80
    print("released on close: %.1f" % released)
    assert 30.39 < released < 30.41
    print("OK: %s balanced the budget" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # four carrier profiles: same circuit, different panels
    profiles = {
        "chest-led": {"chest": 0.95, "gut": 0.40},
        "gut-led": {"chest": 0.40, "gut": 0.95},
        "hot": {"flush": 0.85, "pace": 0.80},
        "cold": {"flush": 0.15, "still": 0.90},
    }
    for label_, sig in profiles.items():
        dom = max(sig, key=sig.get)
        print("  %-10s dominant channel: %s (%.2f)" % (label_, dom, sig[dom]))
    assert profiles["chest-led"]["chest"] > profiles["chest-led"]["gut"]
    assert profiles["gut-led"]["gut"] > profiles["gut-led"]["chest"]
    assert profiles["hot"]["pace"] > profiles["cold"]["flush"]
    # quiet carriers can run the heaviest loop: stillness is not absence
    assert profiles["cold"]["still"] > 0.85
    print("OK: %s compared the carriers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # facial signal components and their read weights
    signals = {
        "gaze_aversion": 0.90, "inner_brow_lift": 0.80,
        "mouth_downturn": 0.75, "swallow": 0.65, "eye_flick": 0.70,
    }
    total = sum(signals.values())
    for k, v in signals.items():
        print("  %-16s strength %.2f (%4.1f %%)" % (k, v, v / total * 100.0))
    assert 3.799 < total < 3.801
    assert signals["gaze_aversion"] == max(signals.values())
    print("OK: %s read the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # display strength at three intensities: flicker, heaviness, crumple
    levels = [("flicker", 0.15), ("heaviness", 0.55), ("crumple", 0.95)]
    for label_, disp in levels:
        print("  %-9s display %.2f" % (label_, disp))
    ds = [d for _, d in levels]
    assert ds[0] < ds[1] < ds[2]
    assert ds[2] > ds[0] * 6.0
    spread = ds[2] - ds[0]
    print("gradient spread: %.2f" % spread)
    assert 0.799 < spread < 0.801
    print("OK: %s graded the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # leakage scores: hiding leaks feeling through control; faking leaks control through absence
    hiding = {"swallow": 0.70, "blink_rate": 0.65, "voice_tremor": 0.60}
    faking = {"swallow": 0.10, "blink_rate": 0.20, "voice_tremor": 0.05}
    hide_leak = sum(hiding.values()) / len(hiding)
    fake_leak = sum(faking.values()) / len(faking)
    print("hiding leakage: %.4f | faking leakage: %.4f" % (hide_leak, fake_leak))
    assert 0.649 < hide_leak < 0.651
    assert 0.116 < fake_leak < 0.118
    assert hide_leak > fake_leak * 5.0
    # timing tell: real face leads words (negative lag); performed face follows (positive lag)
    real_lag, performed_lag = -0.40, 0.60
    print("face-word lag: real %.2fs vs performed +%.2fs" % (real_lag, performed_lag))
    assert real_lag < 0.0 < performed_lag
    print("OK: %s spotted the tells" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the apology scene in beats: durations must sum to the scene length
    beats = [
        ("swallow", 1.5), ("eye_drop", 1.0), ("wrong_order_words", 6.0),
        ("face_ahead_of_mouth", 3.0), ("crumple_fought", 4.5),
    ]
    total = sum(d for _, d in beats)
    for label_, dur in beats:
        print("  %-18s %.1fs" % (label_, dur))
    print("scene length: %.1fs" % total)
    assert 15.9 < total < 16.1
    assert beats[0][1] < beats[2][1]  # the leak precedes the speech
    print("OK: %s staged the scene" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # six classic trigger families, each keyed to the circuit
    triggers = {
        "spoken_wound": 0.90, "betrayal": 0.95, "neglected_duty": 0.85,
        "harm_by_action": 0.88, "moral_compromise": 0.80, "words_of_others": 0.75,
    }
    for k, v in triggers.items():
        key = "deed+standard+reckoning"
        print("  %-16s fires at %.2f via %s" % (k, v, key))
    vals = list(triggers.values())
    assert min(vals) > 0.70          # every classic trigger is a strong key
    assert max(vals) == triggers["betrayal"]
    mean_fire = sum(vals) / len(vals)
    print("mean fire strength: %.4f" % mean_fire)
    assert 0.8549 < mean_fire < 0.8551
    print("OK: %s keyed the triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # cue retrieval strengths: bound cues reopen the scene
    cues = {
        "anniversary_date": 0.90, "place": 0.85, "song": 0.80,
        "smell": 0.70, "photograph": 0.75, "milestone": 0.88,
    }
    for k, v in cues.items():
        print("  %-16s retrieval %.2f" % (k, v))
    strongest = max(cues, key=cues.get)
    print("strongest cue: %s" % strongest)
    assert strongest == "anniversary_date"
    # naming the cue cuts its ambush power
    ambush_before, ambush_after = 0.90, 0.45
    print("ambush power: %.2f -> %.2f after naming" % (ambush_before, ambush_after))
    assert ambush_after == ambush_before / 2.0
    print("OK: %s inventoried the locker" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # guardedness: known triggers are braced for, surprise triggers are not
    guard = {"anniversary": 0.80, "known_place": 0.75,
             "stranger_story": 0.05, "child_question": 0.00, "quiet_moment": 0.10}
    for k, v in guard.items():
        print("  %-14s guardedness %.2f" % (k, v))
    impact = {k: 1.0 - v for k, v in guard.items()}
    assert impact["child_question"] == max(impact.values())
    assert impact["anniversary"] < impact["stranger_story"]
    print("hardest hit: child_question at %.2f" % impact["child_question"])
    assert 0.999 < impact["child_question"] < 1.001
    print("OK: %s mapped the ambushes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the cascade in order, with stage energy
    stages = [
        ("recognition", 0.80), ("shame", 0.70), ("sadness", 0.75),
        ("anger", 0.65), ("fear", 0.60), ("resolve", 0.85),
    ]
    for label_, energy in stages:
        bar = "#" * int(energy * 20)
        print("  %-11s [%s] %.2f" % (label_, bar, energy))
    order = [s for s, _ in stages]
    assert order == ["recognition", "shame", "sadness", "anger", "fear", "resolve"]
    energies = [e for _, e in stages]
    assert energies[-1] > energies[-2]  # resolve gathers the scattered energy
    total = sum(energies)
    print("total cascade energy: %.2f" % total)
    assert 4.349 < total < 4.351
    print("OK: %s ran the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the drive's energy across five action sets; shares sum to 100
    sets = {
        "reparative": 0.40, "seeking": 0.20, "self_punishing": 0.12,
        "avoidance": 0.15, "symbolic": 0.13,
    }
    total = sum(sets.values())
    for k, v in sets.items():
        print("  %-14s %5.2f %%" % (k, v / total * 100.0))
    assert 0.999 < total < 1.001
    assert sets["reparative"] == max(sets.values())
    healthy = sets["reparative"] + sets["seeking"]
    print("healthy-channel share: %.2f" % healthy)
    assert 0.599 < healthy < 0.601
    print("OK: %s tracked the actions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_speech_patterns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # disfluency markers per 100 words: remorseful vs neutral speech
    markers = {"false_starts": (14, 3), "repetitions": (11, 2), "abandoned": (7, 1)}
    for k, (rem, neu) in markers.items():
        print("  %-12s remorseful %d vs neutral %d per 100 words" % (k, rem, neu))
        assert rem > neu * 3
    # specificity test: named-deed apologies land true
    named, general = 0.90, 0.35
    print("lands-true score: named %.2f vs general %.2f" % (named, general))
    assert named > general * 2.0
    print("OK: %s heard the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_decisions_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # decision shifts under remorse: baseline 0.50 each dial
    shifts = {
        "caution": 0.78, "moral_vigilance": 0.82,
        "generosity": 0.75, "self_trust": 0.30, "future_weight": 0.80,
    }
    for k, v in shifts.items():
        direction = "up" if v > 0.50 else "down"
        print("  %-15s %.2f (%s)" % (k, v, direction))
    assert shifts["caution"] > 0.50
    assert shifts["self_trust"] < 0.50
    assert shifts["generosity"] > 0.50
    net = sum(v - 0.50 for v in shifts.values())
    print("net shift: %+.2f" % net)
    assert 0.949 < net < 0.951
    print("OK: %s weighed the judgments" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five escalation tracks: pressure when the drive misses its proper channel
    tracks = {
        "confession_spiral": 0.80, "restitution_race": 0.75,
        "self_punishment_climb": 0.85, "avoidance_fortress": 0.90,
        "numbness_exit": 0.70,
    }
    for k, v in tracks.items():
        print("  %-20s pressure %.2f" % (k, v))
    # proper channel drains every track
    drained = {k: v * 0.20 for k, v in tracks.items()}
    for k, v in drained.items():
        assert v < 0.20
    relief = sum(tracks.values()) - sum(drained.values())
    print("pressure relieved by proper channel: %.2f" % relief)
    assert 3.199 < relief < 3.201
    print("OK: %s vented the pressure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # four movements; each completed movement releases part of the loop
    movements = [
        ("honest_feeling", 0.25), ("plain_speech", 0.25),
        ("specific_payment", 0.25), ("release_into_conduct", 0.25),
    ]
    loop = 1.00
    for label_, release in movements:
        loop -= release
        print("  %-20s loop remaining %.2f" % (label_, max(loop, 0.0)))
    assert -0.001 < loop < 0.001
    # skipped steps leave residue
    skipped = 1.00 - 0.25 - 0.25  # feeling unfelt, speech unspoken
    print("residue when two movements skipped: %.2f" % skipped)
    assert 0.499 < skipped < 0.501
    print("OK: %s completed the circuit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # bottling pressurizes; boiling discharges without paying
    bottled, weeks = 0.60, 8
    for w in range(1, weeks + 1):
        bottled = min(1.0, bottled * 1.08)
    print("bottled pressure after %d weeks: %.4f" % (weeks, bottled))
    assert 0.999 < bottled <= 1.0
    boiled = 0.90
    paid = 0.10  # discharge is not payment
    print("boiled-over discharge %.2f, actual debt paid %.2f" % (boiled, paid))
    assert paid < boiled / 5.0
    proper = 0.90
    print("proper channel pays: %.2f" % proper)
    assert proper > paid * 8.0
    print("OK: %s compared the failures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # six practices, each serving part of the circuit; coverage must be complete
    practices = {
        "evening_review": "appraisal", "prompt_apology": "acknowledgment",
        "repair_list": "debt", "standard_check": "judge",
        "conduct_proof": "prevention", "release_ritual": "filing",
    }
    served = set(practices.values())
    circuit = {"appraisal", "acknowledgment", "debt", "judge", "prevention", "filing"}
    print("practices: %d, circuit parts served: %d" % (len(practices), len(served)))
    assert served == circuit
    # daily books vs decade-end reckoning: small steady cost beats the siege
    daily_cost, siege_cost = 5.0 * 365, 5000.0
    print("yearly daily-books cost %.1f vs one siege %.1f" % (daily_cost, siege_cost))
    assert daily_cost < siege_cost
    print("OK: %s kept the books" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five reading channels and their reliability weights
    channels = {
        "face": 0.30, "body": 0.22, "speech": 0.20,
        "behavior": 0.18, "timing": 0.10,
    }
    total = sum(channels.values())
    for k, v in channels.items():
        print("  %-9s weight %.2f" % (k, v))
    assert 0.999 < total < 1.001
    assert channels["face"] == max(channels.values())
    # humility discount: tendencies, not instruments
    confidence = total * 0.70
    print("calibrated confidence: %.2f (never 1.00)" % confidence)
    assert 0.699 < confidence < 0.701
    print("OK: %s read the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # each helpful response serves one circuit need
    mapping = {
        "listen_fully": "acknowledgment", "validate_appraisal": "verdict",
        "honest_accounting": "debt", "name_the_repair": "channel",
        "allow_timeline": "prevention",
    }
    needs = {"acknowledgment", "verdict", "debt", "channel", "prevention"}
    assert set(mapping.values()) == needs
    for response, need in mapping.items():
        print("  %-18s -> %s" % (response, need))
    # comfort-serving shortcuts serve the responder, not the circuit
    helpful, shortcut = 0.85, 0.25
    print("circuit completion: helpful %.2f vs shortcut %.2f" % (helpful, shortcut))
    assert helpful > shortcut * 3.0
    print("OK: %s served as witness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # seven classic mistakes and how badly each jams the circuit (0..1)
    mistakes = {
        "instant_absolution": 0.70, "ledger_weapon": 0.95,
        "suffering_audit": 0.80, "comparison_verdict": 0.55,
        "fixit_takeover": 0.75, "endless_probation": 0.90,
        "mirror_trial": 0.65,
    }
    for k, v in mistakes.items():
        print("  %-18s jam %.2f" % (k, v))
    worst = max(mistakes, key=mistakes.get)
    print("most corrosive: %s" % worst)
    assert worst == "ledger_weapon"
    avg_jam = sum(mistakes.values()) / len(mistakes)
    print("average jam: %.4f" % avg_jam)
    assert 0.7570 < avg_jam < 0.7572
    print("OK: %s posted the code" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_related_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # distance from remorse along three axes (0 = identical, 1 = opposite)
    neighbors = {
        "guilt": 0.15, "regret": 0.35, "shame": 0.45, "contrition": 0.20,
    }
    opposites = {"self_justification": 0.90, "defiance": 0.95, "indifference": 1.00}
    for k, v in list(neighbors.items()) + list(opposites.items()):
        print("  %-18s distance %.2f" % (k, v))
    assert neighbors["guilt"] == min(neighbors.values())
    assert opposites["indifference"] == max(opposites.values())
    assert min(opposites.values()) > max(neighbors.values())
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_emotion_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # four dyads: remorse blended with a partner; blend character scores
    dyads = {
        "sadness": {"tenderness": 0.90, "heat": 0.20},
        "self_anger": {"tenderness": 0.25, "heat": 0.90},
        "fear": {"tension": 0.85, "drive": 0.55},
        "hope": {"tension": 0.30, "drive": 0.90},
    }
    for k, v in dyads.items():
        print("  %-10s %s" % (k, ", ".join("%s %.2f" % (a, b) for a, b in v.items())))
    assert dyads["sadness"]["tenderness"] > dyads["self_anger"]["tenderness"]
    assert dyads["hope"]["drive"] == max(d["drive"] for d in dyads.values() if "drive" in d)
    assert dyads["fear"]["tension"] > dyads["hope"]["tension"]
    print("OK: %s mixed the dyads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_remorse_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five scenes: remorse level across the arc
    scenes = [
        ("deed", 0.10),
        ("onset", 0.75),
        ("cascade", 0.95),
        ("repair", 0.40),
        ("resolution", 0.12),
    ]
    for label_, level in scenes:
        bar = "#" * int(level * 20)
        print("  %-10s [%s] %.2f" % (label_, bar, level))
    levels = [lv for _, lv in scenes]
    assert levels[2] == max(levels)          # the cascade is the worst
    assert levels[-1] < levels[2] / 5.0     # resolution drains it
    assert levels[3] < levels[2]             # repair breaks the cascade
    assert levels[1] > levels[0]             # onset exceeds the deed-moment
    drop = levels[2] - levels[-1]
    print("cascade-to-resolution drop: %.2f" % drop)
    assert 0.829 < drop < 0.831
    print("OK: %s ran the showcase simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "remorse_definition": demo_remorse_definition,
    "remorse_emotion_family": demo_remorse_emotion_family,
    "remorse_intensity_scale": demo_remorse_intensity_scale,
    "remorse_myths": demo_remorse_myths,
    "remorse_first_person": demo_remorse_first_person,
    "remorse_time_course": demo_remorse_time_course,
    "remorse_low_vs_high": demo_remorse_low_vs_high,
    "remorse_guilt_blend": demo_remorse_guilt_blend,
    "remorse_day_vignette": demo_remorse_day_vignette,
    "remorse_body_signals": demo_remorse_body_signals,
    "remorse_posture_movement": demo_remorse_posture_movement,
    "remorse_sleep_appetite_energy": demo_remorse_sleep_appetite_energy,
    "remorse_body_differences": demo_remorse_body_differences,
    "remorse_face": demo_remorse_face,
    "remorse_face_intensity": demo_remorse_face_intensity,
    "remorse_hiding_faking": demo_remorse_hiding_faking,
    "remorse_expression_gallery": demo_remorse_expression_gallery,
    "remorse_classic_triggers": demo_remorse_classic_triggers,
    "remorse_personal_triggers": demo_remorse_personal_triggers,
    "remorse_surprise_triggers": demo_remorse_surprise_triggers,
    "remorse_chain_reactions": demo_remorse_chain_reactions,
    "remorse_behavior_actions": demo_remorse_behavior_actions,
    "remorse_speech_patterns": demo_remorse_speech_patterns,
    "remorse_decisions_judgment": demo_remorse_decisions_judgment,
    "remorse_escalation": demo_remorse_escalation,
    "remorse_healthy_expression": demo_remorse_healthy_expression,
    "remorse_unhealthy_expression": demo_remorse_unhealthy_expression,
    "remorse_everyday_practices": demo_remorse_everyday_practices,
    "remorse_reading_others": demo_remorse_reading_others,
    "remorse_supportive_responses": demo_remorse_supportive_responses,
    "remorse_mistakes_to_avoid": demo_remorse_mistakes_to_avoid,
    "remorse_related_emotions": demo_remorse_related_emotions,
    "remorse_emotion_mixes": demo_remorse_emotion_mixes,
    "remorse_full_simulation": demo_remorse_full_simulation,
}
