#!/usr/bin/env python3
"""Demo programs for the Guilt Emotion databases (emotion series - RESPAWN;
rebuilt fully from scratch, 2026-10-17).

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
    # three-beat appraisal: standard active, breach judged, responsibility assigned
    standard, breach, responsibility = 1.0, 0.8, 0.9
    guilt = standard * 0.2 + breach * 0.4 + responsibility * 0.4
    print("beats: standard=%.2f breach=%.2f responsibility=%.2f" % (standard, breach, responsibility))
    print("guilt signal: %.3f" % guilt)
    assert 0.879 < guilt < 0.881
    # no responsibility -> sorrow, not guilt
    guilt2 = standard * 0.2 + breach * 0.4 + 0.05 * 0.4
    print("without responsibility: %.3f (sorrow, not guilt)" % guilt2)
    assert 0.539 < guilt2 < 0.541
    print("OK: %s ran the three-beat appraisal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # self-conscious gate: self-awareness x standards x self-evaluation must all be present
    self_awareness, standards, evaluation = 0.9, 0.85, 0.8
    gate = self_awareness * standards * evaluation
    print("self-conscious gate: %.3f" % gate)
    assert 0.611 < gate < 0.613
    # moral-emotion feeders: self-evaluation machinery + care for others
    feeders = {"self_evaluation": 0.9, "care_for_others": 0.85}
    bond_value = sum(feeders.values()) / len(feeders)
    print("bond-maintenance value: %.3f" % bond_value)
    assert 0.874 < bond_value < 0.876
    print("OK: %s mapped the family tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def volume(harm, closeness, responsibility, irreversibility):
        return (harm + closeness + responsibility + irreversibility) / 4.0
    def label(v):
        return "mild" if v < 0.35 else ("moderate" if v < 0.65 else "intense")
    mild = volume(0.2, 0.3, 0.3, 0.1)
    moderate = volume(0.6, 0.7, 0.6, 0.4)
    intense = volume(0.9, 0.95, 1.0, 0.9)
    for v in (mild, moderate, intense):
        print("volume %.3f -> %s" % (v, label(v)))
    assert 0.224 < mild < 0.226 and label(mild) == "mild"
    assert 0.574 < moderate < 0.576 and label(moderate) == "moderate"
    assert 0.936 < intense < 0.938 and label(intense) == "intense"
    print("OK: %s ran the three volumes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six myths; correct answers: belief-not-proof, cousins-not-twins,
    # signal-not-enemy, ache-not-report-card, repair-takes-time, replay-is-a-loop
    myths = [
        ("guilt proves wrongdoing", False),
        ("guilt and shame are identical", False),
        ("all guilt should be eliminated", False),
        ("feeling guilty makes you good", False),
        ("one apology always settles it", False),
        ("thinking harder resolves guilt", False),
    ]
    # the healthy stance: turn each myth into a question (True = questioned)
    questioned = [True, True, True, True, True, False]
    score = sum(questioned) / len(myths)
    print("myths questioned: %d/%d  score: %.3f" % (sum(questioned), len(myths), score))
    assert 0.832 < score < 0.834
    print("OK: %s cleared the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four moving parts of the inner passage, each 0..1 right now
    parts = {"chest_catch": 0.7, "replay_loop": 0.85, "heaviness": 0.6, "self_thought": 0.75}
    total = sum(parts.values())
    print("inner parts: " + ", ".join("%s=%.2f" % kv for kv in parts.items()))
    print("total felt load: %.3f" % total)
    assert 2.899 < total < 2.901
    # the replay stops when repair happens, not when thinking stops
    repaired = True
    replay_after = 0.85 * (0.1 if repaired else 1.0)
    print("replay after repair: %.3f" % replay_after)
    assert 0.084 < replay_after < 0.086
    print("OK: %s simulated the inner passage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guilt over hours: onset spike, peak, fading after repair at hour 6
    def level(h):
        if h < 1: return 0.3 + 0.6 * h          # onset climb
        if h < 6: return 0.9 - 0.02 * (h - 1)    # peak plateau, slow burn
        return max(0.05, 0.8 - 0.25 * (h - 6))   # fading after repair
    for h in (0, 1, 6, 9):
        print("hour %d: %.3f" % (h, level(h)))
    assert 0.299 < level(0) < 0.301
    assert 0.899 < level(1) < 0.901
    assert 0.799 < level(6) < 0.801
    assert 0.049 < level(9) < 0.051
    # aftershock: brief echo at 0.25 of peak, weaker each time
    aftershock = 0.9 * 0.25
    print("aftershock echo: %.3f" % aftershock)
    assert 0.224 < aftershock < 0.226
    print("OK: %s ran the time course" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def volume(harm, closeness, responsibility, irreversibility):
        return (harm + closeness + responsibility + irreversibility) / 4.0
    low = volume(0.2, 0.4, 0.3, 0.1)    # forgotten text message
    high = volume(0.9, 0.95, 1.0, 0.85) # harsh words to a loved one
    print("low-intensity snapshot: %.3f" % low)
    print("high-intensity snapshot: %.3f" % high)
    assert 0.249 < low < 0.251
    assert 0.924 < high < 0.926
    # second-layer guilt: high intensity leaks into new situations
    leak = high * 0.3
    print("second-layer leak: %.3f" % leak)
    assert 0.277 < leak < 0.279
    print("OK: %s ran the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_shame_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attention focus decides the output: act-focus -> guilt, self-focus -> shame
    act_focus, self_focus = 0.55, 0.45
    guilt_part = act_focus
    shame_part = self_focus
    blend = guilt_part + shame_part
    print("guilt part %.2f + shame part %.2f = blend %.2f" % (guilt_part, shame_part, blend))
    assert 0.999 < blend < 1.001
    # untangling: settle attention on one focus; repair addresses the act half
    repaired_act = guilt_part * 0.1   # 90% of guilt resolved by repair
    remaining = repaired_act + shame_part
    print("after repairing the act, remaining: %.3f (shame half needs perspective)" % remaining)
    assert 0.504 < remaining < 0.506
    print("OK: %s untangled the blend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dread hours vs repair minutes across the vignette day
    dread_hours = 9.5   # morning replay through afternoon leak
    repair_minutes = 9.0
    ratio = (dread_hours * 60.0) / repair_minutes
    print("dread minutes: %.1f  repair minutes: %.1f  ratio: %.2f" % (dread_hours * 60, repair_minutes, ratio))
    assert 63.32 < ratio < 63.34
    # loop starvation: replay finds no open breach after the call
    open_breach_before, open_breach_after = 1.0, 0.0
    replay_before = 0.85 * open_breach_before
    replay_after = 0.85 * open_breach_after
    print("replay before repair: %.2f  after: %.2f" % (replay_before, replay_after))
    assert 0.849 < replay_before < 0.851
    assert replay_after == 0.0
    print("OK: %s ran the day vignette" % NAME)
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
}


def demo_guilt_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the guilt cluster: six channels firing together
    cluster = {"chest_weight": 0.8, "stomach_knot": 0.75, "face_heat": 0.7,
               "restless_hands": 0.65, "shallow_breath": 0.6, "weighted_fatigue": 0.7}
    total = sum(cluster.values())
    print("cluster channels: %d  total signal: %.3f" % (len(cluster), total))
    assert 4.199 < total < 4.201
    # single channel alone is ambiguous; the cluster is the signature
    single = cluster["face_heat"]
    print("single channel (face heat): %.2f - ambiguous alone" % single)
    assert 0.699 < single < 0.701
    print("OK: %s mapped the body signals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_posture_movement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # appeasement posture score: smaller + averted + self-soothing
    smaller, averted, self_soothing = 0.8, 0.75, 0.7
    appeasement = (smaller + averted + self_soothing) / 3.0
    print("appeasement posture score: %.3f" % appeasement)
    assert 0.749 < appeasement < 0.751
    # lean-back then lean-in during confession: withdrawal then approach
    lean_back, lean_in = -0.3, 0.5
    net = lean_back + lean_in
    print("confession lean: back %.1f then in %.1f, net %.1f (approach wins)" % (lean_back, lean_in, net))
    assert 0.199 < net < 0.201
    print("OK: %s ran the posture program" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_sleep_appetite_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sleep onset: replay arousal holds the mind above the sleep threshold
    replay_arousal, sleep_threshold = 0.85, 0.4
    latency_factor = replay_arousal / sleep_threshold
    print("sleep latency factor: %.3f (over 1.0 = lying awake)" % latency_factor)
    assert 2.124 < latency_factor < 2.126
    # working-memory crowding: replay occupies the shared workspace
    workspace, replay_load = 1.0, 0.55
    available = workspace - replay_load
    print("working memory available for the day: %.2f" % available)
    assert 0.449 < available < 0.451
    print("OK: %s ran the sleep-appetite-energy model" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three profiles, same guilt, different channels
    profiles = {
        "gut_person": {"gut": 0.9, "chest": 0.2, "heat": 0.3},
        "chest_person": {"gut": 0.2, "chest": 0.9, "heat": 0.3},
        "hot_responder": {"gut": 0.3, "chest": 0.2, "heat": 0.9},
    }
    for pname, ch in profiles.items():
        total = sum(ch.values())
        print("%s dominant channel total: %.2f" % (pname, total))
        assert 1.399 < total < 1.401
    # display rules reroute: suppressed blush becomes stomach knot
    blush_suppressed = 0.7
    rerouted_knot = blush_suppressed * 0.8
    print("rerouted stomach knot: %.3f" % rerouted_knot)
    assert 0.559 < rerouted_knot < 0.561
    print("OK: %s compared the body differences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_facial_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the confession sequence: gaze drop, brow lift, lip press, blush, swallow
    sequence = [("gaze_drop", 0.85), ("brow_lift", 0.6), ("lip_press", 0.75),
                ("blush", 0.8), ("swallow", 0.7)]
    present = sum(1 for _, v in sequence if v > 0.5)
    print("sequence steps present: %d/%d" % (present, len(sequence)))
    assert present == 5
    mean_signal = sum(v for _, v in sequence) / len(sequence)
    print("mean facial signal: %.3f" % mean_signal)
    assert 0.739 < mean_signal < 0.741
    print("OK: %s read the guilty face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_expression_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dimmer switch: readable at moderate, flat at high (overload shutdown)
    def show(intensity):
        if intensity < 0.35: return 0.2   # fleeting flashes
        if intensity < 0.7: return 0.85   # sustained, readable
        return 0.1                        # flat: overload shutdown
    low, mod, high = show(0.2), show(0.5), show(0.9)
    print("low %.2f  moderate %.2f  high %.2f (flat = overload, not indifference)" % (low, mod, high))
    assert 0.199 < low < 0.201
    assert 0.849 < mod < 0.851
    assert 0.099 < high < 0.101
    print("OK: %s ran the expression dimmer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # multi-channel control: the face is managed, the other channels leak
    managed = {"face": 0.9}
    leaked = {"hands": 0.75, "voice_pitch": 0.7, "timing": 0.65, "blush": 0.8}
    leak_total = sum(leaked.values()) / len(leaked)
    print("managed channels: %d  mean leakage elsewhere: %.3f" % (len(managed), leak_total))
    assert 0.724 < leak_total < 0.726
    # faked guilt is too smooth: real guilt disrupts fluency
    real_disfluency, faked_disfluency = 0.7, 0.1
    print("disfluency real %.1f vs faked %.1f" % (real_disfluency, faked_disfluency))
    assert real_disfluency > faked_disfluency + 0.5
    print("OK: %s caught the leakage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gallery checklist: three studies x directions each
    studies = {
        "quiet_admission": ["head tilt 10 deg", "inner brow lift", "faint blush"],
        "confession": ["hand to mouth", "flickering gaze", "shoulders forward"],
        "heavy_carrying": ["head in hands", "flat mouth", "elbows on knees"],
    }
    total = sum(len(v) for v in studies.values())
    print("studies: %d  directions: %d" % (len(studies), total))
    assert total == 9
    # the authenticity rule: guilt never performs itself
    polish, believability = 0.9, 0.2
    print("polish %.1f -> believability %.1f (polished guilt reads false)" % (polish, believability))
    assert believability < 0.3
    print("OK: %s opened the expression gallery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven classic triggers scored on standard-clarity x breach-obviousness x responsibility
    triggers = {
        "harming": (1.0, 0.9, 0.9), "promise_breaking": (1.0, 0.85, 0.95),
        "lying": (0.9, 0.8, 0.9), "neglect": (0.85, 0.7, 0.8),
        "taking_more": (0.9, 0.75, 0.85), "code_violation": (0.95, 0.9, 1.0),
        "benefiting_from_loss": (0.8, 0.7, 0.6),
    }
    scores = {k: (a + b + c) / 3.0 for k, (a, b, c) in triggers.items()}
    top = max(scores, key=scores.get)
    print("triggers scored: %d  strongest: %s (%.3f)" % (len(scores), top, scores[top]))
    assert 0.949 < scores[top] < 0.951
    weakest = min(scores, key=scores.get)
    print("weakest (most ambiguous): %s (%.3f)" % (weakest, scores[weakest]))
    assert 0.699 < scores[weakest] < 0.701
    print("OK: %s fired the classic triggers" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
    "guilt_body_signals": demo_guilt_body_signals,
    "guilt_posture_movement": demo_guilt_posture_movement,
    "guilt_sleep_appetite_energy": demo_guilt_sleep_appetite_energy,
    "guilt_body_differences": demo_guilt_body_differences,
    "guilt_facial_expression": demo_guilt_facial_expression,
    "guilt_expression_intensity": demo_guilt_expression_intensity,
    "guilt_hiding_faking": demo_guilt_hiding_faking,
    "guilt_expression_gallery": demo_guilt_expression_gallery,
    "guilt_classic_triggers": demo_guilt_classic_triggers,
})


def demo_guilt_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # personal trigger map: cue strength x unresolved appraisal
    triggers = {"song": (0.8, 0.9), "anniversary_date": (0.85, 0.85),
                "place": (0.7, 0.8), "object": (0.6, 0.75), "phrase": (0.75, 0.9)}
    fired = {k: a * b for k, (a, b) in triggers.items()}
    strongest = max(fired, key=fired.get)
    print("personal triggers: %d  strongest: %s (%.3f)" % (len(fired), strongest, fired[strongest]))
    assert 0.721 < fired[strongest] < 0.724
    # naming a trigger turns ambush into forecast
    ambush, forecast = 0.9, 0.4
    print("ambush %.1f -> forecast %.1f after writing it down" % (ambush, forecast))
    assert forecast < ambush - 0.4
    print("OK: %s mapped the personal triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hidden rules revealed by surprise triggers; audit each
    rules = {"rest must be earned": 0.8, "good fortune must be even": 0.7,
             "growth is betrayal": 0.75, "joy is disloyal in hard times": 0.65}
    # the audit: would I impose this rule on someone I love?
    kept = {r: v for r, v in rules.items() if v > 0.75}
    print("hidden rules found: %d  surviving audit: %d" % (len(rules), len(kept)))
    assert len(kept) == 1
    survivor = list(kept)[0]
    print("survivor: %s" % survivor)
    assert survivor == "rest must be earned"
    print("OK: %s audited the surprise triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the cascade: each domino adds its load to the weather system
    cascade = [("guilt", 0.7), ("shame", 0.6), ("anxiety", 0.55),
               ("anger", 0.5), ("sadness", 0.45), ("withdrawal", 0.4)]
    total = sum(v for _, v in cascade)
    print("cascade dominoes: %d  total weather: %.3f" % (len(cascade), total))
    assert 3.199 < total < 3.201
    # settling the first domino starves the chain
    root_settled = 0.7 * 0.1
    remaining = total - 0.7 + root_settled
    print("after settling the root breach, remaining: %.3f" % remaining)
    assert 2.569 < remaining < 2.571
    print("OK: %s traced the chain reaction" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # behavior menu scored on fit: does it reach the harmed account?
    behaviors = {"direct_repair": 0.95, "proxy_repair": 0.4, "avoidance": 0.05,
                 "excessive_confession": 0.3, "self_punishment": 0.2, "people_pleasing": 0.35}
    best = max(behaviors, key=behaviors.get)
    print("behaviors: %d  best fit: %s (%.2f)" % (len(behaviors), best, behaviors[best]))
    assert best == "direct_repair"
    # proxy repair needs repeating: relief decays without settling
    relief = 0.5
    for i in range(3):
        relief *= 0.7
    print("proxy relief after 3 rounds: %.3f (keeps needing repeats)" % relief)
    assert 0.171 < relief < 0.173
    print("OK: %s chose the guilty behaviors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_behavior_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the guilt dialect: count the markers in a sample apology
    sample = ("I am so sorry, I feel terrible about this, it is all my fault, "
              "I did not mean to, I swear, can I make it up to you, "
              "you must think I am awful, I am sorry, I am really sorry")
    markers = ["sorry", "terrible", "my fault", "did not mean", "make it up", "awful"]
    hits = sum(sample.lower().count(m) for m in markers)
    print("guilt-speech markers in sample: %d" % hits)
    assert hits == 8
    # repeated apology past function: bids beyond the first have shrinking returns
    returns = [1.0, 0.5, 0.25, 0.1]
    print("apology returns by repetition: %s" % returns)
    assert sum(returns) < 2.0
    print("OK: %s spoke the guilty dialect" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_decisions_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guilt votes: risk down, generosity up, self-punishment up, standards stricter
    baseline = {"risk": 0.5, "generosity": 0.5, "self_punish": 0.1, "strictness": 0.5}
    guilty = {"risk": 0.25, "generosity": 0.8, "self_punish": 0.6, "strictness": 0.75}
    shifts = {k: guilty[k] - baseline[k] for k in baseline}
    print("shifts: " + ", ".join("%s=%+.2f" % kv for kv in shifts.items()))
    assert -0.26 < shifts["risk"] < -0.24
    assert 0.29 < shifts["generosity"] < 0.31
    assert 0.49 < shifts["self_punish"] < 0.51
    # the second look: decide with the lesson, not the ache
    lesson_kept = 1.0
    ache_faded = 0.2
    print("lesson kept %.1f, ache faded to %.1f - re-decide now" % (lesson_kept, ache_faded))
    assert ache_faded < 0.3
    print("OK: %s voted with guilt" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # escalation: as feeling grows, the target gets vaguer (act -> relationship -> self)
    levels = [("low", 0.3, "act"), ("moderate", 0.6, "relationship"), ("high", 0.9, "self")]
    for label, intensity, target in levels:
        print("%s intensity %.1f -> target: %s" % (label, intensity, target))
    # cost-vs-settlement confusion: costly self-punishment, zero settlement
    cost, settlement = 0.9, 0.05
    print("self-punishment cost %.2f, settlement %.2f (the confusion)" % (cost, settlement))
    assert cost > settlement + 0.8
    # re-aiming: bring the target back to the act
    reaimed = 0.3
    print("re-aimed target intensity: %.1f (back at the act)" % reaimed)
    assert 0.299 < reaimed < 0.301
    print("OK: %s climbed the escalation ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the working apology: four components, each present
    apology = {"name_the_act": 1.0, "own_it": 1.0, "acknowledge_impact": 1.0, "concrete_repair": 1.0}
    # penalties: hedging, groveling, excuses each deduct
    penalties = {"hedging": 0.0, "groveling": 0.0, "excuses": 0.0}
    score = sum(apology.values()) / 4.0 - sum(penalties.values())
    print("apology components: %d/4  penalties: %.1f  score: %.3f" % (sum(apology.values()), sum(penalties.values()), score))
    assert 0.999 < score < 1.001
    # proportion test: breach smaller and relationship steadier afterward
    breach_before, breach_after = 0.8, 0.2
    print("breach %.1f -> %.1f after healthy expression" % (breach_before, breach_after))
    assert breach_after < breach_before - 0.5
    print("OK: %s expressed it healthily" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
    "guilt_personal_triggers": demo_guilt_personal_triggers,
    "guilt_surprise_triggers": demo_guilt_surprise_triggers,
    "guilt_chain_reactions": demo_guilt_chain_reactions,
    "guilt_behavior_actions": demo_guilt_behavior_actions,
    "guilt_behavior_speech": demo_guilt_behavior_speech,
    "guilt_decisions_judgment": demo_guilt_decisions_judgment,
    "guilt_escalation": demo_guilt_escalation,
    "guilt_healthy_expression": demo_guilt_healthy_expression,
})


def demo_guilt_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottling: suppression keeps arousal while hiding expression
    arousal, expressed = 0.85, 0.1
    bottled_cost = arousal * (1.0 - expressed) * 10.0  # years of underground loop
    print("bottled: arousal %.2f expressed %.2f -> cost %.2f" % (arousal, expressed, bottled_cost))
    assert 7.649 < bottled_cost < 7.651
    # exploding: catharsis for the confessor, second breach for the other
    confessor_relief, other_harm = 0.8, 0.7
    net = confessor_relief - other_harm - 0.5  # minus the new breach
    print("explosion net value: %.2f (negative = served the wrong person)" % net)
    assert -0.41 < net < -0.39
    print("OK: %s priced the unhealthy patterns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six daily practices; each prevents its failure mode
    practices = {"repair_promptly": 0.9, "promises_small": 0.85, "evening_review": 0.9,
                 "proportion_check": 0.85, "separate_layers": 0.8, "forgive_outward": 0.75}
    coverage = sum(practices.values()) / len(practices)
    print("practices: %d  mean coverage: %.3f" % (len(practices), coverage))
    assert 0.840 < coverage < 0.842
    # the evening review: written capture releases the 2 a.m. rehearsal
    rehearsal_before, rehearsal_after = 0.9, 0.2
    print("2 a.m. rehearsal %.1f -> %.1f after writing it down" % (rehearsal_before, rehearsal_after))
    assert rehearsal_after < rehearsal_before - 0.6
    print("OK: %s ran the daily practices" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cluster convergence: four channels firing together near the topic
    channels = {"gaze": 0.8, "lips": 0.75, "hands": 0.7, "speech": 0.85}
    topic_near, topic_far = 1.0, 0.2
    signal_near = sum(channels.values()) / len(channels) * topic_near
    signal_far = sum(channels.values()) / len(channels) * topic_far
    print("signal near topic: %.3f  far from topic: %.3f" % (signal_near, signal_far))
    assert 0.774 < signal_near < 0.776
    assert 0.154 < signal_far < 0.156
    # topic-bound = guilt; free-floating = anxiety
    print("topic-bound pattern -> guilt read (not free-floating anxiety)")
    assert signal_near > signal_far + 0.5
    print("OK: %s read the signs in others" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six supportive moves, each rated on help delivered
    moves = {"listen_fully": 0.9, "validate_standard": 0.85, "proportion_help": 0.8,
             "concrete_repair": 0.9, "no_false_absolution": 0.75, "stay_after": 0.85}
    total_help = sum(moves.values())
    print("supportive moves: %d  total help: %.3f" % (len(moves), total_help))
    assert 5.049 < total_help < 5.051
    # the role-reversal question: borrow their fairer other-mind
    self_dial, other_dial = 1.0, 0.6
    print("responsibility dial: self %.1f vs as-judge-of-other %.1f" % (self_dial, other_dial))
    assert other_dial < self_dial - 0.3
    print("OK: %s supported well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven mistakes, each scored on damage done
    mistakes = {"dont_feel_guilty": 0.6, "instant_absolution": 0.55, "shame_upgrade": 0.9,
                "weaponizing": 0.95, "guilt_competition": 0.5, "forced_cheer": 0.45,
                "endless_inquest": 0.7}
    worst = max(mistakes, key=mistakes.get)
    print("mistakes: %d  most damaging: %s (%.2f)" % (len(mistakes), worst, mistakes[worst]))
    assert worst == "weaponizing"
    total_damage = sum(mistakes.values())
    print("total damage if all committed: %.3f" % total_damage)
    assert 4.649 < total_damage < 4.651
    print("OK: %s dodged the mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_related_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the neighborhood on two axes: focus (act=0/self=1) x direction (inward=0/outward=1)
    coords = {"guilt": (0.1, 0.1), "shame": (0.9, 0.1), "remorse": (0.15, 0.1),
              "regret": (0.9, 0.7), "embarrassment": (0.8, 0.2), "moral_disgust": (0.1, 0.9)}
    def dist(a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    d_shame = dist(coords["guilt"], coords["shame"])
    d_disgust = dist(coords["guilt"], coords["moral_disgust"])
    print("neighbors mapped: %d" % len(coords))
    print("guilt-shame distance: %.3f (closest cousin)" % d_shame)
    print("guilt-moral_disgust distance: %.3f" % d_disgust)
    assert 0.799 < d_shame < 0.801
    assert 0.799 < d_disgust < 0.801
    assert d_shame < dist(coords["guilt"], coords["regret"])
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_emotion_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four canonical blends: guilt base 0.6 plus each partner
    base = 0.6
    blends = {"shame": 0.5, "self_anger": 0.45, "anxiety": 0.55, "sadness": 0.4}
    for partner, w in blends.items():
        total = base + w
        print("guilt + %s: %.2f" % (partner, total))
    heaviest = max(blends, key=blends.get)
    print("heaviest blend: guilt + %s" % heaviest)
    assert heaviest == "anxiety"
    # driver diagnostic: name the secondary appraisal first
    drivers = {"shame": "perspective", "self_anger": "name the punishment",
               "anxiety": "face consequences", "sadness": "rest and refuel"}
    print("drivers diagnosed: %d" % len(drivers))
    assert len(drivers) == 4
    print("OK: %s blended the emotions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guilt_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six scenes with guilt levels: trigger, peak, leak, turn, repair, release
    scenes = [("trigger", 0.4), ("peak", 0.9), ("leak", 0.75),
              ("turn", 0.5), ("repair", 0.25), ("release", 0.05)]
    for label, level in scenes:
        print("scene %-8s guilt %.2f" % (label, level))
    peak = max(v for _, v in scenes)
    final = scenes[-1][1]
    print("peak %.2f -> release %.2f" % (peak, final))
    assert 0.899 < peak < 0.901
    assert 0.049 < final < 0.051
    # the thesis in numbers: dread scales with avoidance, not breach size
    dread_hours, repair_minutes = 20.0, 9.0
    ratio = (dread_hours * 60.0) / repair_minutes
    print("dread-to-repair ratio: %.2f" % ratio)
    assert 133.32 < ratio < 133.34
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
    "guilt_unhealthy_expression": demo_guilt_unhealthy_expression,
    "guilt_everyday_practices": demo_guilt_everyday_practices,
    "guilt_reading_others": demo_guilt_reading_others,
    "guilt_supportive_responses": demo_guilt_supportive_responses,
    "guilt_mistakes_to_avoid": demo_guilt_mistakes_to_avoid,
    "guilt_related_emotions": demo_guilt_related_emotions,
    "guilt_emotion_mixes": demo_guilt_emotion_mixes,
    "guilt_full_simulation": demo_guilt_full_simulation,
})
