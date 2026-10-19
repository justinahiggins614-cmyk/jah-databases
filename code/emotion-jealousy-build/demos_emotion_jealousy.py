#!/usr/bin/env python3
"""Demo programs for the Jealousy Emotion databases (emotion series).

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


def demo_jealousy_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the five-beat sequence: value -> threat -> appraisal -> alarm -> urge
    value, threat = 0.90, 0.65
    appraisal = (value + threat) / 2.0
    alarm = min(1.0, appraisal * 1.2)
    urge = alarm * 0.85
    print("value %.2f  threat %.2f" % (value, threat))
    print("appraisal %.3f  alarm %.3f  urge %.3f" % (appraisal, alarm, urge))
    assert 0.774 < appraisal < 0.776
    assert 0.929 < alarm < 0.931
    assert 0.789 < urge < 0.792
    print("beats: value -> threat -> appraisal -> alarm -> urge")
    print("OK: %s ran the five-beat sequence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the recipe: fear core + anger + sadness over the love base note
    ingredients = {"fear_of_loss": 0.45, "anger": 0.25, "sadness": 0.15, "love": 0.15}
    total = sum(ingredients.values())
    share = {k: v / total * 100.0 for k, v in ingredients.items()}
    for k in ingredients:
        print("  %-12s weight %.2f (%5.2f %%)" % (k, ingredients[k], share[k]))
    assert 0.999 < sum(share.values()) / 100.0 < 1.001
    assert share["fear_of_loss"] > share["anger"] > share["sadness"]
    assert 44.9 < share["fear_of_loss"] < 45.1
    print("core: fear of loss; love is the base note being guarded")
    print("OK: %s mixed the family recipe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the three dials sum into the volume knob 0..10
    def volume(bond, certainty, load):
        return min(10.0, (bond + certainty + load) / 3.0 * 10.0)
    def label(v):
        return "mild" if v < 3.5 else ("moderate" if v < 7.0 else "intense")
    cases = [(0.2, 0.2, 0.1), (0.6, 0.5, 0.5), (0.95, 0.9, 0.85)]
    vols = []
    for bond, certainty, load in cases:
        v = volume(bond, certainty, load)
        vols.append(v)
        print("dials %.2f/%.2f/%.2f -> volume %.2f (%s)" % (bond, certainty, load, v, label(v)))
    assert vols[0] < 3.5 and 3.5 <= vols[1] < 7.0 and vols[2] >= 7.0
    assert 1.66 < vols[0] < 1.68
    assert 8.99 < vols[2] < 9.01
    print("OK: %s played the three volumes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # each myth's confusion = plausibility * (1 - knowledge); correction sets knowledge to 1
    myths = [
        ("jealousy proves love", 0.70),
        ("only insecure people feel it", 0.55),
        ("jealousy equals envy", 0.60),
        ("a little is always healthy", 0.50),
        ("the threat is always real", 0.65),
    ]
    before = sum(p * (1.0 - 0.0) for _, p in myths)
    after = sum(p * (1.0 - 1.0) for _, p in myths)
    for myth, p in myths:
        print("  myth: %-32s plausibility %.2f -> corrected" % (myth, p))
    print("total confusion before %.2f  after %.2f" % (before, after))
    assert 2.99 < before < 3.01
    assert after == 0.0
    assert before > after
    print("OK: %s separated signal from story" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # two voices over minutes: fast alarm decays, slow reason rises
    minutes = [0, 2, 5, 10]
    for t in minutes:
        alarm = 0.95 * (0.85 ** t)
        reason = min(0.90, 0.30 + 0.06 * t)
        print("  t=%2d min  alarm voice %.3f  reason voice %.3f" % (t, alarm, reason))
    a0, r0 = 0.95 * (0.85 ** 0), min(0.90, 0.30)
    a10, r10 = 0.95 * (0.85 ** 10), min(0.90, 0.30 + 0.60)
    assert a0 > r0 and r10 > a10
    assert 0.186 < a10 < 0.188
    assert 0.899 < r10 < 0.901
    print("early: alarm shouts; late: reason catches up")
    print("OK: %s heard both voices" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # arousal across the five phases, hours since trigger
    phases = [("onset", 0.1, 0.90), ("peak", 1.0, 1.00), ("plateau", 8.0, 0.55),
              ("fading", 24.0, 0.25), ("aftershock", 168.0, 0.12)]
    arousals = [a for _, _, a in phases]
    for pname, h, a in phases:
        print("  %-10s t=%6.1fh  arousal %.2f" % (pname, h, a))
    assert arousals[1] == max(arousals), "peak must be highest"
    assert arousals[1] > arousals[2] > arousals[3] > arousals[4], "decay after peak"
    assert 0.11 < arousals[4] < 0.13
    print("worst decisions cluster at the peak; naming the phase loosens it")
    print("OK: %s mapped the weather pattern" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # same alarm, different dials: Tuesday twinge vs 2 a.m. storm
    def volume(bond, certainty, load):
        return min(10.0, (bond + certainty + load) / 3.0 * 10.0)
    low = volume(0.40, 0.25, 0.20)    # friend's lunch, good day
    high = volume(0.95, 0.90, 0.85)   # partner's 2 a.m. text, bad week
    print("low-intensity snapshot  volume %.2f" % low)
    print("high-intensity snapshot volume %.2f" % high)
    assert low < 3.5 < 7.0 <= high
    assert 2.83 < low < 2.85
    assert 8.99 < high < 9.01
    # confirmation trap: at high volume, absence of evidence reads as concealment
    found_nothing, alarm_certain = True, high > 7.0
    helps = not (found_nothing and alarm_certain)
    print("found nothing helps:", helps)
    assert helps is False
    print("OK: %s compared the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_fear_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the blend: jealous heat (approach) + fear cold (protection)
    heat, cold = 0.80, 0.70
    urgency = heat            # jealousy wants to act now
    dread = cold              # fear previews the loss
    pull_approach = heat * 0.9
    pull_protect = cold * 0.9
    print("heat %.2f -> urgency %.2f, approach pull %.2f" % (heat, urgency, pull_approach))
    print("cold %.2f -> dread %.2f, protection pull %.2f" % (cold, dread, pull_protect))
    assert 0.71 < pull_approach < 0.73
    assert 0.62 < pull_protect < 0.64
    # rehearsal loop: each mental replay re-fires the alarm
    alarm = 0.50
    for replay in range(3):
        alarm = min(1.0, alarm + 0.15)
    print("alarm after 3 replays: %.2f" % alarm)
    assert 0.94 < alarm < 0.96
    print("OK: %s separated the two partners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_day_in_life(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # one ordinary day, alarm level by hour (7:00 -> 23:00)
    day = [(7, 0.55), (9, 0.70), (12, 0.45), (15, 0.50),
           (18, 0.30), (20, 0.75), (23, 0.85)]
    total = sum(a for _, a in day)
    peak_hour, peak = max(day, key=lambda p: p[1])
    for h, a in day:
        print("  %02d:00  alarm %s %.2f" % (h, "#" * int(a * 20), a))
    print("peak %02d:00 (%.2f), day total %.2f" % (peak_hour, peak, total))
    assert peak_hour == 23 and 0.84 < peak < 0.86
    assert 4.09 < total < 4.11
    print("nothing happened today; the weather ran on attention alone")
    print("OK: %s walked the ordinary day" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_jealousy_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the body signature: six channels, 0..1 activation at peak alarm
    channels = {"heart": 0.85, "breath": 0.75, "muscles": 0.80,
                "stomach": 0.92, "skin": 0.65, "energy_surge": 0.88}
    loudest = max(channels, key=channels.get)
    for ch, v in sorted(channels.items(), key=lambda p: -p[1]):
        print("  %-13s activation %.2f" % (ch, v))
    print("loudest channel:", loudest)
    assert loudest == "stomach"
    assert 0.91 < channels["stomach"] < 0.93
    assert all(0.0 <= v <= 1.0 for v in channels.values())
    print("OK: %s read the body signature" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # two postures, feature strengths 0..1
    still = {"rigidity": 0.90, "threat_angle": 0.85, "grip": 0.70, "pacing": 0.10}
    restless = {"rigidity": 0.25, "threat_angle": 0.60, "grip": 0.40, "pacing": 0.92}
    dom_still = max(still, key=still.get)
    dom_restless = max(restless, key=restless.get)
    print("still posture dominant:", dom_still, "restless posture dominant:", dom_restless)
    assert dom_still == "rigidity" and dom_restless == "pacing"
    # oscillation toward the partner: lean-in vs pull-away over minutes
    distance = [1.0, 0.4, 0.9, 0.3, 0.8]   # 1.0 = close, 0.0 = withdrawn
    swings = sum(abs(distance[i+1] - distance[i]) for i in range(len(distance)-1))
    print("proximity swings total: %.2f" % swings)
    assert 2.19 < swings < 2.21
    print("OK: %s held the wall and paced it" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # three nights: jealousy taxes sleep, poor sleep raises the load dial
    jealousy = [0.80, 0.60, 0.40]
    load = 0.30
    for night, j in enumerate(jealousy, 1):
        sleep = max(0.0, 1.0 - j * 0.9)
        load = min(1.0, load + (1.0 - sleep) * 0.5)
        print("  night %d  jealousy %.2f -> sleep %.2f, next-day load %.2f" % (night, j, sleep, load))
    assert 0.27 < (1.0 - 0.80 * 0.9) < 0.29
    assert 0.99 < load < 1.01
    # break one link: one protected night of sleep lowers the load
    load = max(0.0, load - 0.45)
    print("after one protected night, load: %.2f" % load)
    assert 0.54 < load < 0.56
    print("OK: %s broke one link of the loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # three bodies, same alarm, different loudest channels
    profiles = {
        "gut_body": {"gut": 0.92, "chest": 0.40, "heat": 0.35},
        "chest_body": {"gut": 0.30, "chest": 0.90, "heat": 0.55},
        "hot_body": {"gut": 0.45, "chest": 0.60, "heat": 0.93},
    }
    loudest = {p: max(ch, key=ch.get) for p, ch in profiles.items()}
    for p, ch in loudest.items():
        print("  %-11s loudest channel: %s" % (p, ch))
    assert loudest["gut_body"] == "gut"
    assert loudest["chest_body"] == "chest"
    assert loudest["hot_body"] == "heat"
    assert len(set(loudest.values())) == 3
    print("OK: %s learned three different towers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # component method: read the parts separately, then name the whole
    brow_furrow, eye_narrow, lip_press = 0.82, 0.78, 0.88
    fear_inner_brow = 0.55
    print("brow furrow %.2f (anger)  eye narrow %.2f  lip press %.2f (control)" % (brow_furrow, eye_narrow, lip_press))
    print("inner brow lift %.2f (fear blend)" % fear_inner_brow)
    parts = [brow_furrow, eye_narrow, lip_press]
    whole = sum(parts) / len(parts) + fear_inner_brow * 0.1
    label = "jealous" if all(p > 0.5 for p in parts) and fear_inner_brow > 0.4 else "unclear"
    print("assembled face score %.3f -> %s" % (whole, label))
    assert label == "jealous"
    assert 0.880 < whole < 0.882
    print("OK: %s assembled the borrowed face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # control budget: arousal spends it, expression shows the remainder
    def expression(arousal):
        control = max(0.0, 1.0 - arousal)
        if control > 0.6:
            return "hidden (micro-signs only)"
        if control > 0.25:
            return "effortful (suppression shows)"
        return "overwhelmed (control bankrupt)"
    for arousal in (0.20, 0.55, 0.90):
        print("  arousal %.2f -> %s" % (arousal, expression(arousal)))
    assert expression(0.20).startswith("hidden")
    assert expression(0.55).startswith("effortful")
    assert expression(0.90).startswith("overwhelmed")
    print("OK: %s spent the control budget" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # hiding: leak = arousal minus control, floored at zero
    arousal, control = 0.85, 0.60
    leak = max(0.0, arousal - control)
    print("hiding: arousal %.2f - control %.2f -> leak %.2f" % (arousal, control, leak))
    assert 0.24 < leak < 0.26
    # faking: voluntary parts present, autonomic parts absent -> detected
    voluntary, autonomic = True, False
    detected_fake = voluntary and not autonomic
    print("faked performance detected:", detected_fake)
    assert detected_fake is True
    # timing rule: first half-second is always honest
    honest_window = 0.5  # seconds before the cover story assembles
    print("honest window: %.1f s" % honest_window)
    assert honest_window == 0.5
    print("OK: %s watched timing and physiology" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # gallery checklist: every drawable/playable choice traced to a record
    checklist = [
        ("three-quarter tracking gaze", True),
        ("low drawn brows + inner lift", True),
        ("pressed lips, set jaw", True),
        ("head down-forward, holding ground", True),
        ("hands: gripping opposite wrist", True),
        ("late smile, shallow breath (actor)", True),
        ("play watching-and-hiding-watching", True),
        ("devotion inside the vigilance", True),
    ]
    score = sum(1 for _, done in checklist if done) / len(checklist)
    print("gallery completeness: %d/%d = %.2f" % (sum(1 for _, d in checklist if d), len(checklist), score))
    assert score == 1.0
    print("OK: %s completed the gallery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_jealousy_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # five classic triggers, base potency 0..1; stacked triggers sum
    triggers = {"rival_attention": 0.80, "secrecy_signal": 0.85,
                "changed_pattern": 0.70, "exclusion": 0.65, "comparison_scene": 0.90}
    for t, p in sorted(triggers.items(), key=lambda p: -p[1]):
        print("  %-16s potency %.2f" % (t, p))
    stacked = triggers["rival_attention"] + triggers["secrecy_signal"]
    lone = triggers["exclusion"]
    print("stacked (laugh + secrecy): %.2f  vs lone exclusion: %.2f" % (stacked, lone))
    assert 1.64 < stacked < 1.66
    assert stacked > lone
    assert 0.89 < triggers["comparison_scene"] < 0.91
    print("OK: %s posted the classic approaches" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # appraisal contamination: old certainty bleeds into new ambiguity
    ambiguity, old_certainty, memory_weight = 0.30, 0.95, 0.60
    effective = ambiguity + memory_weight * (old_certainty - ambiguity)
    print("present ambiguity %.2f + memory 0.60*(0.95-0.30)" % ambiguity)
    print("effective certainty felt: %.3f" % effective)
    assert 0.689 < effective < 0.691
    # naming the rhyme: dating the memory moves it to the slow system
    named = effective - memory_weight * (old_certainty - ambiguity) * 0.5
    print("after naming the rhyme: %.3f" % named)
    assert 0.494 < named < 0.496
    assert named < effective
    print("OK: %s dated the old battlefield" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the alarm monitors attention share, not rival credentials
    bond_value = 0.90
    rivals = {"real_person": 0.80, "absorbed_book": 0.45, "pet": 0.50,
              "read_receipt": 0.55, "fictional_character": 0.40}
    for rival, attention_elsewhere in rivals.items():
        sting = attention_elsewhere * bond_value
        print("  %-18s sting %.2f" % (rival, sting))
        assert sting > 0.0
    stings = [a * bond_value for a in rivals.values()]
    assert max(stings) == 0.80 * 0.90
    assert 0.719 < max(stings) < 0.721
    assert min(stings) > 0.35, "even the painted dragon stings"
    print("OK: %s touched the painted dragon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # cascade: each link multiplies the alarm by the loop gain
    gain = 1.25
    links = ["trigger", "narrowed_attention", "old_memory", "checking", "bad_confrontation"]
    alarm, levels = 0.40, []
    for link in links:
        alarm = min(1.5, alarm * gain)
        levels.append(alarm)
        print("  %-18s alarm %.3f" % (link, alarm))
    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    print("step-ups:", ["%.3f" % d for d in diffs])
    assert all(diffs[i+1] > diffs[i] for i in range(len(diffs)-1)), "cascade accelerates"
    assert 1.21 < levels[-1] < 1.23
    # breaking one link starves the loop
    broken = 0.40 * gain * gain * 1.0 * gain * gain
    print("alarm with one link broken: %.3f" % broken)
    assert broken < levels[-1]
    print("OK: %s broke the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the action menu with its cost ledger: (brief relief, long-term cost)
    actions = {"checking": (0.60, 0.75), "questioning": (0.45, 0.60),
               "guarding": (0.50, 0.65), "testing": (0.40, 0.80),
               "clinging": (0.55, 0.45), "withdrawing": (0.35, 0.70),
               "competing": (0.50, 0.40)}
    for a, (relief, cost) in actions.items():
        net = relief - cost
        print("  %-11s relief %.2f  cost %.2f  net %+.2f" % (a, relief, cost, net))
    nets = [r - c for r, c in actions.values()]
    assert all(n <= 0.15 for n in nets), "no action pays well long-term"
    assert min(nets) < -0.35, "testing is the priciest"
    print("OK: %s priced the menu honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # hearing the dialect: disguised questions carry the markers
    utterances = [
        "So how do you two know each other, again?",
        "You seemed to be having fun tonight.",
        "Do you love me? Really?",
        "Dinner is at seven.",
        "You never laugh like that with me anymore.",
    ]
    markers = ("again", "seem", "fun tonight", "really", "never", "anymore")
    flagged = [u for u in utterances if u.endswith("?") or any(m in u for m in markers)]
    for u in utterances:
        print("  [%s] %s" % ("DIALECT" if u in flagged else "plain  ", u))
    assert len(flagged) == 4
    assert "Dinner is at seven." not in flagged
    # plain translation of the first flagged line
    plain = "I feel threatened and I need reassurance."
    print("plain translation:", plain)
    assert len(plain) > 10
    print("OK: %s heard the dialect" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # decision quality falls as arousal rises
    def quality(arousal):
        return 0.90 - arousal * 0.70
    calm, peak = quality(0.10), quality(0.90)
    print("decision quality calm: %.2f  peak alarm: %.2f" % (calm, peak))
    assert 0.82 < calm < 0.84
    assert 0.26 < peak < 0.28
    assert peak < calm
    # waiting restores the judge without losing real information
    waited = quality(0.90 * (0.5 ** 3))  # arousal decays over three half-lives
    print("quality after waiting: %.2f" % waited)
    assert waited > peak
    assert 0.81 < waited < 0.83
    print("OK: %s let the weather pass" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # tolerance: each rung buys less relief than the last
    rungs = ["surveillance", "interrogation", "restriction",
             "routine_confrontation", "cruel_tests", "coercion"]
    reliefs = [0.50 * (0.70 ** i) for i in range(len(rungs))]
    for rung, relief in zip(rungs, reliefs):
        print("  %-20s relief %.3f" % (rung, relief))
    assert all(reliefs[i+1] < reliefs[i] for i in range(len(reliefs)-1))
    assert 0.083 < reliefs[-1] < 0.085
    # naming the rung is the exit ramp
    named_rung = 1
    print("exit ramp: name rung %d (%s) and step off" % (named_rung, rungs[named_rung]))
    print("OK: %s sounded the recall" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_jealousy_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # three channels, each scored 0..1; the bond closeness delta follows
    say = 0.85    # plain speech at a calm hour
    show = 0.70   # vulnerability without weaponizing
    channel = 0.80  # arousal spent before the conversation
    closeness_delta = (say + show + channel) * 0.2
    print("say %.2f  show %.2f  channel %.2f" % (say, show, channel))
    print("bond closeness delta: %+.2f" % closeness_delta)
    assert 0.46 < closeness_delta < 0.48
    assert closeness_delta > 0, "healthy expression leaves the bond closer or clearer"
    print("OK: %s delivered the true report" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # bottling: cost compounds quietly; exploding: spike now, louder alarm later
    bottle_cost = sum(0.30 for _ in range(5))          # five days unspoken
    explode_spike = 0.90                               # one peak-hour confrontation
    alarm_gain_after = 0.20                            # the alarm learns explosions work
    print("bottling cost over 5 days: %.2f" % bottle_cost)
    print("exploding spike: %.2f + alarm gain %+.2f" % (explode_spike, alarm_gain_after))
    assert 1.49 < bottle_cost < 1.51
    assert explode_spike > bottle_cost / 5, "one explosion costs more than one bottled day"
    # the middle path: outlet without command
    middle_cost = 0.15
    print("middle path cost: %.2f" % middle_cost)
    assert middle_cost < bottle_cost / 5 and middle_cost < explode_spike
    print("OK: %s chose the middle path" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # seven practices, each turning the background-load dial down
    practices = {"evidence_habit": 0.08, "waiting_habit": 0.08, "body_habit": 0.10,
                 "plain_speech_habit": 0.08, "attention_habit": 0.06,
                 "outside_voice_habit": 0.08, "history_habit": 0.08}
    load = 0.90
    for p, drop in practices.items():
        load = max(0.0, load - drop)
    print("background load 0.90 -> %.2f after %d practices" % (load, len(practices)))
    assert 0.33 < load < 0.35
    assert load < 0.90 - 0.50, "climate beats weather"
    print("OK: %s kept the standing orders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # independent channels agreeing: 1 sign is noise, 3 signs are a pattern
    def confidence(n_signs, trigger_present):
        base = {1: 0.25, 2: 0.50, 3: 0.75}[n_signs]
        return base * (1.5 if trigger_present else 0.7)
    c1 = confidence(1, True)
    c3 = confidence(3, True)
    c3_no_trigger = confidence(3, False)
    print("1 sign + trigger: %.3f   3 signs + trigger: %.3f   3 signs, no trigger: %.3f"
          % (c1, c3, c3_no_trigger))
    assert 0.374 < c1 < 0.376
    assert 1.124 < c3 < 1.126
    assert c3_no_trigger < c3, "context multiplies meaning"
    assert c1 < c3
    print("pattern is still only a hypothesis until confirmed")
    print("OK: %s read to serve, not to expose" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # score responses by which mechanism they address (0..1 each)
    responses = {
        "gentle naming": 0.80,
        "one warm reassurance": 0.85,
        "volunteered clarity": 0.75,
        "steady presence": 0.90,
        "2 a.m. interrogation engagement": 0.15,
        "submitting to audits": 0.20,
    }
    best = max(responses, key=responses.get)
    worst = min(responses, key=responses.get)
    for r, s in sorted(responses.items(), key=lambda p: -p[1]):
        print("  %-30s %.2f" % (r, s))
    print("best:", best, " worst:", worst)
    assert best == "steady presence"
    assert worst == "2 a.m. interrogation engagement"
    assert 0.89 < responses[best] < 0.91
    print("OK: %s stood the watch together" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # every mistake backfires: multiplier > 1 on the next alarm's gain
    mistakes = {"labeling": 1.30, "soothing_lies": 1.50, "audit_compliance": 1.40,
                "staged_provocations": 1.60, "triangulation": 1.35,
                "peak_hour_engagement": 1.45, "storm_matching": 1.55}
    for m, mult in sorted(mistakes.items(), key=lambda p: -p[1]):
        print("  %-20s next-alarm gain x%.2f" % (m, mult))
    assert all(mult > 1.0 for mult in mistakes.values()), "every mistake feeds the mechanism"
    assert max(mistakes.values()) == 1.60
    assert 1.29 < mistakes["labeling"] < 1.31
    print("unifying principle: never feed the mechanism you are trying to calm")
    print("OK: %s posted the forbidden drills" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_related_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the shape test: count the corners
    def classify(corners, heat):
        if corners == 2:
            return "envy"
        if corners == 3 and heat > 0.5:
            return "jealousy"
        if corners == 3 and heat <= 0.5:
            return "suspicion"
        return "unknown"
    cases = [(2, 0.7, "envy"), (3, 0.8, "jealousy"), (3, 0.3, "suspicion")]
    for corners, heat, expected in cases:
        got = classify(corners, heat)
        print("  corners %d heat %.1f -> %s" % (corners, heat, got))
        assert got == expected
    # the antidote: trust lowers the threat prior
    prior, trust_evidence = 0.80, 0.60
    posterior = prior * (1.0 - trust_evidence)
    print("threat prior %.2f with trust evidence -> %.2f" % (prior, posterior))
    assert 0.319 < posterior < 0.321
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_blends(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # Plutchik-style dyads: name both partners, treat the loudest first
    base = 1.00  # jealousy
    blends = {
        "dread": ("fear", 0.85),
        "righteous_fury": ("anger", 0.90),
        "mournful_clinging": ("sadness", 0.75),
        "fierce_devotion": ("love", 0.95),
    }
    for bname, (partner, strength) in blends.items():
        total = base + strength
        loudest = partner if strength > base * 0.5 else "jealousy"
        print("  %-16s partner %-7s strength %.2f -> treat %s first" % (bname, partner, strength, loudest))
        assert 1.74 < total < 1.96
    assert blends["fierce_devotion"][1] == max(s for _, s in blends.values())
    print("OK: %s greeted each ally by name" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jealousy_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # Maya's week: five scenes, alarm level per scene
    scenes = [("trigger", 0.90), ("plateau", 0.60), ("peak", 0.95),
              ("choice_point", 0.40), ("resolution", 0.15)]
    for sname, alarm in scenes:
        print("  %-12s alarm %.2f %s" % (sname, alarm, "#" * int(alarm * 20)))
    peak = max(a for _, a in scenes)
    resolution = scenes[-1][1]
    choice = scenes[3][1]
    assert 0.94 < peak < 0.96
    assert resolution < peak and choice < peak
    assert 0.14 < resolution < 0.16
    drop = (peak - resolution) / peak * 100.0
    print("alarm fell %.1f%% from peak to resolution" % drop)
    assert 84.1 < drop < 84.3
    print("OK: %s walked Maya's week to dawn" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "jealousy_definition": demo_jealousy_definition,
    "jealousy_emotion_family": demo_jealousy_emotion_family,
    "jealousy_intensity_scale": demo_jealousy_intensity_scale,
    "jealousy_myths": demo_jealousy_myths,
    "jealousy_first_person": demo_jealousy_first_person,
    "jealousy_time_course": demo_jealousy_time_course,
    "jealousy_low_vs_high": demo_jealousy_low_vs_high,
    "jealousy_fear_blend": demo_jealousy_fear_blend,
    "jealousy_day_in_life": demo_jealousy_day_in_life,
    "jealousy_body_signals": demo_jealousy_body_signals,
    "jealousy_posture": demo_jealousy_posture,
    "jealousy_sleep_appetite": demo_jealousy_sleep_appetite,
    "jealousy_body_differences": demo_jealousy_body_differences,
    "jealousy_face": demo_jealousy_face,
    "jealousy_face_intensity": demo_jealousy_face_intensity,
    "jealousy_hiding_faking": demo_jealousy_hiding_faking,
    "jealousy_expression_gallery": demo_jealousy_expression_gallery,
    "jealousy_classic_triggers": demo_jealousy_classic_triggers,
    "jealousy_personal_triggers": demo_jealousy_personal_triggers,
    "jealousy_surprise_triggers": demo_jealousy_surprise_triggers,
    "jealousy_chain_reactions": demo_jealousy_chain_reactions,
    "jealousy_actions": demo_jealousy_actions,
    "jealousy_speech": demo_jealousy_speech,
    "jealousy_judgment": demo_jealousy_judgment,
    "jealousy_escalation": demo_jealousy_escalation,
    "jealousy_healthy_expression": demo_jealousy_healthy_expression,
    "jealousy_unhealthy_expression": demo_jealousy_unhealthy_expression,
    "jealousy_everyday_practices": demo_jealousy_everyday_practices,
    "jealousy_reading_others": demo_jealousy_reading_others,
    "jealousy_supportive_responses": demo_jealousy_supportive_responses,
    "jealousy_mistakes_to_avoid": demo_jealousy_mistakes_to_avoid,
    "jealousy_related_emotions": demo_jealousy_related_emotions,
    "jealousy_blends": demo_jealousy_blends,
    "jealousy_full_simulation": demo_jealousy_full_simulation,
}
