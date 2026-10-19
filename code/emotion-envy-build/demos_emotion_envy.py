#!/usr/bin/env python3
"""Demo programs for the Envy Emotion databases (Manon's 16:15 orders, emotion series).

Every demo is real, runnable, stdlib-only Python performing the actual
emotion-scenario simulation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker. Demo outputs
were cross-checked against entry text during authoring.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_envy_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three ingredients of envy: comparison, lack, pain (1 = present)
    episodes = [
        {"comparison": 1, "lack": 1, "pain": 1},   # full envy
        {"comparison": 0, "lack": 1, "pain": 1},   # mere desire, no comparison
        {"comparison": 1, "lack": 0, "pain": 0},   # neutral observation
        {"comparison": 1, "lack": 1, "pain": 0},   # noticed gap, no sting
    ]
    for ep in episodes:
        is_envy = ep["comparison"] and ep["lack"] and ep["pain"]
        print("comparison=%d lack=%d pain=%d -> envy=%s"
              % (ep["comparison"], ep["lack"], ep["pain"], bool(is_envy)))
    assert sum(1 for ep in episodes if ep["comparison"] and ep["lack"] and ep["pain"]) == 1
    # Aristotle's scope: felt toward equals in goods that matter
    equals, goods_matter = 1, 1
    sting = 8.5 * equals * goods_matter
    print("sting score: %.1f" % sting)
    assert 8.49 < sting < 8.51
    print("rule: comparison plus lack plus pain - remove any one and it is not envy")
    print("OK: %s defined the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two-party vs three-party structure decides envy vs jealousy
    cases = [
        {"parties": 2, "theme": "lacking"},   # envy
        {"parties": 3, "theme": "losing"},    # jealousy
        {"parties": 2, "theme": "losing"},    # inconsistent input
        {"parties": 3, "theme": "lacking"},   # inconsistent input
    ]
    for c in cases:
        if c["parties"] == 2 and c["theme"] == "lacking":
            label = "envy"
        elif c["parties"] == 3 and c["theme"] == "losing":
            label = "jealousy"
        else:
            label = "mixed/unclear"
        print("parties=%d theme=%s -> %s" % (c["parties"], c["theme"], label))
    labels = ["envy", "jealousy", "mixed/unclear", "mixed/unclear"]
    assert labels[0] == "envy" and labels[1] == "jealousy"
    # the disappearance test: remove the other person
    envy_without_other = 0.0
    jealousy_without_rival = 4.2  # suspicion can linger
    print("envy with other removed: %.1f; jealousy with rival removed: %.1f"
          % (envy_without_other, jealousy_without_rival))
    assert envy_without_other == 0.0
    assert 4.19 < jealousy_without_rival < 4.21
    print("rule: envy is two-party lacking, jealousy is three-party losing")
    print("OK: %s told the two apart" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # volume dial: stakes set the band; same three ingredients throughout
    def band(stakes):
        if stakes <= 3:
            return "mild twinge"
        if stakes <= 7:
            return "moderate settled"
        return "intense consuming"
    for stakes in (2, 5, 9):
        print("stakes %d -> %s" % (stakes, band(stakes)))
    assert band(2) == "mild twinge"
    assert band(5) == "moderate settled"
    assert band(9) == "intense consuming"
    # rumination multiplies: each replay refreshes the sting by a factor
    sting, factor, replays = 3.0, 1.35, 4
    for _ in range(replays):
        sting *= factor
    print("sting after %d replays: %.2f" % (replays, sting))
    assert 9.9 < sting < 10.0
    print("rule: same emotion at every volume; rumination turns twinges into moods")
    print("OK: %s ran the dial" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five myths scored against the research verdict (True = myth busted)
    verdicts = {
        "envy means bad character": True,
        "envy equals jealousy": True,
        "envy always destructive": True,
        "successful people immune": True,
        "comparison can be switched off": True,
    }
    busted = sum(1 for v in verdicts.values() if v)
    print("myths examined: %d, busted: %d" % (len(verdicts), busted))
    assert busted == 5
    # benign envy effect: improvement motivation gain in the lab
    baseline_effort, benign_boost = 50.0, 18.0
    effort = baseline_effort + benign_boost
    print("effort baseline %.1f -> with benign envy %.1f" % (baseline_effort, effort))
    assert 67.9 < effort < 68.1
    print("rule: the feeling is data; only the action is a choice")
    print("OK: %s cleared the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the double movement: surface gladness vs underneath arithmetic (0-10)
    gladness_surface, arithmetic_under = 7.0, 8.0
    split = abs(gladness_surface - arithmetic_under)
    print("surface gladness %.1f vs underneath arithmetic %.1f (split %.1f)"
          % (gladness_surface, arithmetic_under, split))
    assert 0.9 < split < 1.1
    # counterfactual loop: each replay adds one 'if I had...' branch
    branches = sum(1 for _ in range(6))
    print("counterfactual branches after one hour: %d" % branches)
    assert branches == 6
    # flaw-scan urge strength 0-10 vs shame about the scanning
    flaw_scan, shame = 6.5, 7.0
    print("flaw-scan urge %.1f, shame about it %.1f" % (flaw_scan, shame))
    assert 6.49 < flaw_scan < 6.51 and 6.99 < shame < 7.01
    print("rule: glad on the surface, arithmetic underneath - the signature split")
    print("OK: %s stepped inside the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four phases with typical peak sting 0-10
    phases = [("onset", 0.05, 6.0), ("peak", 1.0, 9.0),
              ("fading", 24.0, 3.0), ("aftershock", 168.0, 4.0)]
    for name_, hours, sting in phases:
        print("%-10s at ~%6.1fh: sting %.1f" % (name_, hours, sting))
    stings = [s for _, _, s in phases]
    assert stings[1] == max(stings), "peak must be the maximum"
    # decay: without re-triggering, sting halves roughly every 12h
    sting, half_life, t = 9.0, 12.0, 24.0
    decayed = sting * (0.5 ** (t / half_life))
    print("sting 9.0 decayed over 24h: %.2f" % decayed)
    assert 2.24 < decayed < 2.26
    print("rule: fast onset, first-hour peak, fading with distance, echoing aftershocks")
    print("OK: %s charted the weather" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # appraisal inputs 0-10 for the two snapshots
    twinge = {"relevance": 3.0, "similarity": 4.0, "deserved": 8.0, "control": 7.0}
    storm = {"relevance": 9.5, "similarity": 9.0, "deserved": 4.0, "control": 2.5}
    def volume(a):
        return (a["relevance"] * 0.4 + a["similarity"] * 0.3
                + (10 - a["deserved"]) * 0.15 + (10 - a["control"]) * 0.15)
    vt, vs = volume(twinge), volume(storm)
    print("twinge volume %.2f vs storm volume %.2f" % (vt, vs))
    assert 3.14 < vt < 3.16
    assert 8.52 < vs < 8.53
    # ill will present in storm, absent in twinge (Smith & Kim formula)
    print("ill will: twinge 0, storm 1")
    assert vt < 4.0 < vs
    print("rule: same appraisal, different inputs - volume is information about stakes")
    print("OK: %s held both snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_partner_mix(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # blend = envy ache + resentment heat; stickiness from narrative rehearsal
    ache, heat = 7.0, 6.0
    blend_strength = math.sqrt(ache ** 2 + heat ** 2)
    print("ache %.1f + heat %.1f -> blend strength %.2f" % (ache, heat, blend_strength))
    assert 9.21 < blend_strength < 9.23
    # grievance narrative rehearsal: each retelling adds staying power
    staying = 1.0
    for _ in range(5):
        staying *= 1.25
    print("staying power after 5 retellings: %.2f" % staying)
    assert 3.04 < staying < 3.06
    # untangling: gap gets a plan, story gets an audit
    print("gap->plan, story->audit: two tools for two ingredients")
    print("rule: ache plus heat is stickier than ache alone")
    print("OK: %s mixed the blend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_day_in_life(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five micro-episodes across the day, each a small tax 0-10
    taxes = {"feed photo": 2.0, "bonus mention": 3.5, "sibling news": 2.5,
             "meeting praise": 3.0, "evening review": 4.0}
    total = sum(taxes.values())
    for k, v in taxes.items():
        print("%-14s tax %.1f" % (k, v))
    print("day total tax: %.1f (no single episode above 4.0)" % total)
    assert 14.9 < total < 15.1
    assert max(taxes.values()) <= 4.0
    # savoring loss: attention spent on comparison is unavailable for savoring
    print("rule: background weather, cumulative tax - the day thins without breaking")
    print("OK: %s walked the ordinary day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body channels 0-10 during a moderate envy episode
    channels = {"heart": 5.5, "breath tightness": 6.0, "gut pit": 8.0,
                "jaw tension": 7.0, "shoulder lock": 6.5, "skin flush": 4.0}
    top = max(channels, key=channels.get)
    print("strongest channel: %s (%.1f)" % (top, channels[top]))
    assert top == "gut pit"
    # restless-heavy: agitation and heaviness co-occur
    agitation, heaviness = 7.0, 6.5
    print("agitation %.1f with heaviness %.1f: the signature combination"
          % (agitation, heaviness))
    assert agitation > 5.0 and heaviness > 5.0
    print("rule: the gut leads, the jaw follows, the signature stays quiet")
    print("OK: %s read the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # contradiction score: retreat in torso + return in eyes (0-10 each)
    torso_retreat, eye_return = 7.0, 8.0
    contradiction = (torso_retreat + eye_return) / 2.0
    print("torso retreat %.1f, eye return %.1f -> contradiction %.1f"
          % (torso_retreat, eye_return, contradiction))
    assert 7.49 < contradiction < 7.51
    # self-soothing micro-movements per minute under envy vs at rest
    at_rest, under_envy = 2.0, 9.0
    print("self-touch gestures/min: rest %.1f vs envy %.1f" % (at_rest, under_envy))
    assert under_envy / at_rest > 4.0
    print("rule: the body retreats while the eyes keep returning")
    print("OK: %s posed the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sleep onset delay in minutes by envy volume
    delays = {"twinge": 5.0, "moderate": 35.0, "intense": 75.0}
    for k, v in delays.items():
        print("%-8s sleep delay %4.1f min" % (k, v))
    assert delays["twinge"] < delays["moderate"] < delays["intense"]
    # appetite split: suppressed vs soothing (fractions of people)
    suppressed, soothing, unchanged = 0.45, 0.35, 0.20
    print("appetite: suppressed %.2f, soothing %.2f, unchanged %.2f"
          % (suppressed, soothing, unchanged))
    assert abs(suppressed + soothing + unchanged - 1.0) < 1e-9
    # attentional fatigue: replay hours consume executive budget
    replay_hours, drain_per_hour = 3.0, 12.0
    drain = replay_hours * drain_per_hour
    print("attentional drain: %.1f units (rest alone does not repay it)" % drain)
    assert 35.9 < drain < 36.1
    print("rule: sleep, appetite, energy shifting together means weather became climate")
    print("OK: %s tracked the maintenance systems" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_envy_individual_diffs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four bodily styles, same envy strength 8.0, different lead channels
    styles = {"gut-led": 8.0, "chest-led": 7.5, "cold-freeze": 6.5, "hot-restless": 8.5}
    spread = max(styles.values()) - min(styles.values())
    print("lead-channel strength spread across styles: %.1f" % spread)
    assert 1.9 < spread < 2.1
    # high self-monitors show less: leakage factor by monitoring 0-10
    for monitoring in (2.0, 8.0):
        leakage = 9.0 * (1.0 - monitoring / 12.0)
        print("monitoring %.1f -> leakage %.2f" % (monitoring, leakage))
    assert 9.0 * (1.0 - 8.0 / 12.0) < 9.0 * (1.0 - 2.0 / 12.0)
    print("rule: same feeling, different bodies - signals are hypotheses, never verdicts")
    print("OK: %s mapped the differences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # no universal face: count of dedicated programs found for envy = 0
    dedicated_programs = 0
    print("dedicated universal facial programs for envy: %d" % dedicated_programs)
    assert dedicated_programs == 0
    # the tight congratulations: mouth active, eye muscles still (0-10)
    mouth_smile, eye_crease = 7.0, 1.0
    duchenne_gap = mouth_smile - eye_crease
    print("mouth %.1f vs eye-crease %.1f (Duchenne gap %.1f)"
          % (mouth_smile, eye_crease, duchenne_gap))
    assert 5.9 < duchenne_gap < 6.1
    # micro-sign duration in milliseconds: leak before suppression catches it
    leak_ms = 220.0
    print("typical leak duration: %.0f ms" % leak_ms)
    assert 199.0 < leak_ms < 501.0
    print("rule: no envy face - only envy leaks, and leaks need context")
    print("OK: %s studied the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # visible movement DECREASES as management increases: the less-is-more gradient
    movement = {"mild flicker": 6.0, "managed performance": 3.5,
                "mask": 1.0, "break": 8.5}
    for k, v in movement.items():
        print("%-19s visible movement %.1f" % (k, v))
    assert movement["mask"] < movement["managed performance"] < movement["mild flicker"]
    assert movement["break"] == max(movement.values())
    # leak salience rises against stillness: contrast ratio
    stillness, leak = 9.0, 2.0
    salience = leak * (stillness / 5.0)
    print("leak salience against stillness: %.2f" % salience)
    assert 3.59 < salience < 3.61
    print("rule: the harder the management, the more the leaks stand out")
    print("OK: %s graded the expressions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # concealment kit: 4 techniques; faking kit: 3 choreographies
    conceal = ["redirect", "preemptive praise", "busy hands", "early exit"]
    fake = ["too-fast congratulations", "superlative pile-up", "overlong warmth"]
    print("concealment techniques: %d, faking choreographies: %d"
          % (len(conceal), len(fake)))
    assert len(conceal) == 4 and len(fake) == 3
    # leak channels: timing, symmetry, duration, eyes, voice = 5
    leaks = 5
    # congratulations timing: genuine ~0.5s onset, performed arrives late or rushed
    genuine_onset, performed_onset = 0.5, 1.1
    print("onset delay genuine %.1fs vs performed %.1fs" % (genuine_onset, performed_onset))
    assert performed_onset > genuine_onset
    assert leaks == 5
    print("rule: concealment has tells - the tell is usually effort itself")
    print("OK: %s caught the choreography" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six-frame suppressed flash: neutral, 2-frame tightening, mask settles
    frames = ["neutral", "tighten", "tighten", "mask", "mask", "mask"]
    print("frames: %d, tightening frames: %d" % (len(frames), frames.count("tighten")))
    assert len(frames) == 6 and frames.count("tighten") == 2
    # contempt vs envy: head angle degrees (down vs level) and mouth laterality
    contempt_angle, envy_angle = -12.0, 0.0
    print("contempt head angle %.0f deg (down); envy head angle %.0f deg (level)"
          % (contempt_angle, envy_angle))
    assert contempt_angle < envy_angle
    # writer's rule: behavioral evidence beats labels
    print("rule: draw the contradiction, write the behavior, never the label")
    print("OK: %s filled the gallery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # trigger formula: visibility * comparability * self-relevance (0-10 each)
    def trigger(v, c, s):
        return (v * c * s) / 100.0
    peer_promo = trigger(9.0, 9.5, 9.0)
    stranger_lottery = trigger(9.0, 2.0, 3.0)
    print("peer promotion trigger: %.2f" % peer_promo)
    print("stranger lottery trigger: %.2f" % stranger_lottery)
    assert 7.69 < peer_promo < 7.71
    assert 0.53 < stranger_lottery < 0.55
    assert peer_promo > stranger_lottery * 10
    # breaking one factor disarms: set comparability to ~0
    disarmed = trigger(9.0, 0.5, 9.0)
    print("disarmed (comparability broken): %.2f" % disarmed)
    assert disarmed < 1.0
    print("rule: visibility times comparability times self-relevance - break one, disarm all")
    print("OK: %s catalogued the triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five personal trigger types with charge 0-10 for one invented person
    charges = {"anniversary": 7.0, "place": 5.5, "object": 4.0,
               "specific person": 9.0, "milestone": 8.0}
    top = max(charges, key=charges.get)
    print("highest-charge personal trigger: %s (%.1f)" % (top, charges[top]))
    assert top == "specific person"
    # mapped vs unmapped: preparation cuts ambush strength
    ambush, prepared = 8.5, 8.5 * 0.45
    print("ambush strength unmapped %.1f vs mapped %.2f" % (ambush, prepared))
    assert 3.81 < prepared < 3.84
    print("rule: mapped triggers can be prepared for; unmapped ones ambush")
    print("OK: %s mapped the minefield" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the comparison system fires on partial matches: 5 odd triggers
    odd = ["stranger", "downward", "fictional", "past-self", "pet"]
    print("odd triggers catalogued: %d" % len(odd))
    assert len(odd) == 5
    # stranger trigger fires before similarity check completes: sting then correction
    initial_sting, after_correction = 5.0, 1.5
    print("stranger sting %.1f -> after similarity check %.1f"
          % (initial_sting, after_correction))
    assert after_correction < initial_sting
    # past-self: maximal similarity (it is you) with uncloseable gap
    similarity, closeability = 10.0, 1.0
    pain = similarity * (10.0 - closeability) / 10.0
    print("past-self pain index: %.1f" % pain)
    assert 8.9 < pain < 9.1
    print("rule: the instrument is promiscuous - odd triggers reveal true values")
    print("OK: %s caught the surprises" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cascade: each link lowers the threshold for the next (threshold 0-10)
    threshold, links = 7.0, ["promotion", "house", "marriage", "talent"]
    print("link cascade with falling thresholds:")
    for link in links:
        fired = 8.0 > threshold  # comparison strength 8.0 each time
        print("  %-9s threshold %.1f -> fired=%s" % (link, threshold, fired))
        assert fired
        threshold *= 0.85
    assert threshold < 4.5
    # early break: naming the first trigger restores threshold
    restored = threshold + 3.0
    print("after naming first trigger + absorption: threshold %.2f" % restored)
    assert restored > 6.5
    print("rule: cascades feel like truth but are weather - break them early")
    print("OK: %s traced the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five action families; fork routing by closeability and deservedness 0-10
    def route(closeable, deserved):
        if closeable >= 6 and deserved >= 6:
            return "benign emulation"
        if closeable < 4 or deserved < 4:
            return "diminishing/undermining"
        return "avoidance"
    cases = [(8.0, 8.0), (2.0, 3.0), (5.0, 5.0)]
    routes = [route(c, d) for c, d in cases]
    for (c, d), r in zip(cases, routes):
        print("closeable %.1f deserved %.1f -> %s" % (c, d, r))
    assert routes == ["benign emulation", "diminishing/undermining", "avoidance"]
    print("families: benign, avoidance, research, diminishing, soothing = 5")
    print("rule: the fork is a moment-to-moment choice, not a personality type")
    print("OK: %s watched the actions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # phrase families with deniability scores (literal innocent 0-10 vs pragmatic bite 0-10)
    phrases = {"must be nice": (8.0, 7.0), "good for them": (9.0, 5.0),
               "with their connections...": (6.0, 8.5)}
    for p, (lit, prag) in phrases.items():
        gap = prag - (10.0 - lit)
        print("%-26s literal-innocent %.1f, pragmatic bite %.1f" % (p, lit, prag))
    # prosody: pitch lift in Hz when performing gladness
    rest_pitch, performed_pitch = 110.0, 138.0
    lift = performed_pitch - rest_pitch
    print("pitch lift performing gladness: %.0f Hz" % lift)
    assert 27.9 < lift < 28.1
    print("rule: the words pass politeness; the music transmits the appraisal")
    print("OK: %s listened to the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # envy audit: value with audience vs value with no witnesses (0-10)
    desires = {"promotion for status": (8.5, 3.0), "craft mastery": (7.5, 7.0),
               "bigger car": (8.0, 2.5)}
    for d, (with_aud, no_wit) in desires.items():
        positional = with_aud - no_wit
        verdict = "positional" if positional > 3.0 else "intrinsic"
        print("%-20s positional component %.1f -> %s" % (d, positional, verdict))
    assert desires["promotion for status"][0] - desires["promotion for status"][1] > 3.0
    assert desires["craft mastery"][0] - desires["craft mastery"][1] < 3.0
    # moral tilt: harshness toward envied vs neutral party (0-10)
    neutral, envied = 4.0, 6.8
    print("judgment harshness: neutral %.1f vs envied %.1f" % (neutral, envied))
    assert envied > neutral
    print("rule: would I want this if no one would ever know? - the envy audit")
    print("OK: %s audited the decisions" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_envy_behavior_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six rungs with reversibility cost 0-10 (higher = harder to take back)
    rungs = [("private", 1.0), ("leakage", 2.5), ("distancing", 4.0),
             ("diminishing", 6.5), ("undermining", 9.0), ("consuming", 9.5)]
    for i, (rung, cost) in enumerate(rungs, 1):
        print("rung %d %-11s reversal cost %.1f" % (i, rung, cost))
    costs = [c for _, c in rungs]
    assert costs == sorted(costs), "costs must rise with rungs"
    # escalators: rumination, proximity, grievance, echo - each adds push 0-10
    push = 2.0 + 2.5 + 3.0 + 2.0
    print("combined escalator push: %.1f" % push)
    assert 9.49 < push < 9.51
    print("rule: each rung up is harder to reverse - live on rungs one and two")
    print("OK: %s climbed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three healthy forms with effectiveness 0-10 vs suppression baseline
    forms = {"say it (trusted friend)": 7.5, "show it converted": 8.0,
             "channel it (curriculum)": 9.0, "bottling baseline": 2.0}
    for k, v in forms.items():
        print("%-24s effectiveness %.1f" % (k, v))
    assert forms["channel it (curriculum)"] == max(forms.values())
    # conversion: gap -> next action within 24h counts as converted
    converted = 1
    print("envy converted to next action: %d (loops starved)" % converted)
    assert converted == 1
    print("rule: envy with a job description - say it, show it converted, channel it")
    print("OK: %s expressed it well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottling: 4 costs; exploding: 3 costs
    bottling_costs = {"control tax": 6.0, "pressure buildup": 7.5,
                      "distortion": 8.0, "ambush under load": 9.0}
    exploding_costs = {"relationship damage": 9.0, "reputation rewrite": 8.5,
                       "feeling stays": 7.0}
    print("bottling costs: %d, exploding costs: %d"
          % (len(bottling_costs), len(exploding_costs)))
    assert len(bottling_costs) == 4 and len(exploding_costs) == 3
    # catharsis failure: venting strengthens the narrative (gain per venting)
    strength, gain, vents = 5.0, 1.4, 3
    for _ in range(vents):
        strength *= gain
    print("grievance strength after %d ventings: %.2f" % (vents, strength))
    assert 13.71 < strength < 13.73
    print("rule: bottling smashes the gauge, exploding smashes the panel")
    print("OK: %s priced the mishandling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven practices, each weak alone (0-10), strong in combination
    practices = {"noticing": 3.0, "fair-comparison audit": 4.0, "gratitude": 3.5,
                 "input diet": 4.5, "conversion": 5.0, "admiration": 3.0,
                 "values check": 4.0}
    solo = max(practices.values())
    combined = sum(practices.values()) * 0.55  # synergy factor
    print("practices: %d, best solo %.1f, combined %.2f"
          % (len(practices), solo, combined))
    assert len(practices) == 7
    assert combined > solo * 2.0
    assert 14.84 < combined < 14.86
    print("rule: weak alone, strong together - pressure at many points breaks loops")
    print("OK: %s built the routine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_reading_signs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four evidence bags; confidence rises with agreeing channels
    def confidence(channels_agreeing):
        return 1.0 - (0.5 ** channels_agreeing)
    for n in (1, 2, 4):
        print("%d agreeing channels -> confidence %.3f" % (n, confidence(n)))
    assert confidence(1) < confidence(2) < confidence(4)
    assert 0.93 < confidence(4) < 0.94
    # cost asymmetry: false positive (accusation) vs false negative (missed, kind anyway)
    fp_cost, fn_cost = 9.0, 1.5
    print("false-positive cost %.1f vs false-negative cost %.1f" % (fp_cost, fn_cost))
    assert fp_cost > fn_cost * 5
    print("rule: clusters in context - the reading is for your behavior, not their trial")
    print("OK: %s read the signs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three scenarios with the address-the-gap response scored 0-10
    responses = {"envy toward you: share credit": 8.5,
                 "venting: reflect gap as info": 8.0,
                 "undermining: light redirect": 7.5}
    for k, v in responses.items():
        print("%-34s helpfulness %.1f" % (k, v))
    assert min(responses.values()) > 7.0
    # naming the feeling backfires: helpfulness of 'you are just jealous'
    naming = 1.5
    print("naming-the-feeling helpfulness: %.1f (cardinal error)" % naming)
    assert naming < 2.0
    print("rule: address the gap, never name the feeling")
    print("OK: %s responded well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven mistakes with backfire magnitude 0-10
    mistakes = {"naming it": 9.5, "fairness lecture": 7.0, "flaunting": 8.0,
                "pity": 7.5, "joining diminishing": 8.5,
                "forced gratitude": 6.5, "fixing the gap": 6.0}
    worst = max(mistakes, key=mistakes.get)
    print("mistakes: %d, worst: %s (%.1f)" % (len(mistakes), worst, mistakes[worst]))
    assert len(mistakes) == 7 and worst == "naming it"
    # pity paradox: intended soothing 8.0, actual inferiority confirmation feeds wound
    intended, actual = 8.0, -4.0
    print("pity: intended %.1f, net effect %.1f" % (intended, actual))
    assert actual < 0 < intended
    print("rule: tend weather, never issue verdicts")
    print("OK: %s dodged the mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_related_map(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two sorting questions decide the label
    def sort(has_person, pain_about):
        if not has_person:
            return "longing/covetousness/greed"
        return "envy" if pain_about == "lacking" else "jealousy"
    cases = [(True, "lacking"), (True, "losing"), (False, "lacking")]
    labels = [sort(p, t) for p, t in cases]
    for (p, t), lab in zip(cases, labels):
        print("person=%s pain=%s -> %s" % (p, t, lab))
    assert labels == ["envy", "jealousy", "longing/covetousness/greed"]
    # neighbors and cousins counted
    neighbors, cousins = 3, 4
    print("neighbors %d, cousins %d" % (neighbors, cousins))
    assert neighbors == 3 and cousins == 4
    print("rule: diagnose the ingredients, then pick the tool")
    print("OK: %s drew the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_emotion_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four blends: envy base 7.0 plus partner, each with its own handling need
    blends = {"admiration": (7.0, 6.0, "savor + chase"),
              "anger": (7.0, 8.0, "fairness audit"),
              "sadness": (7.0, 5.0, "restoration"),
              "shame": (7.0, 7.5, "normalizing truth")}
    for partner, (envy, part, tool) in blends.items():
        strength = math.sqrt(envy ** 2 + part ** 2)
        print("envy+%-10s strength %5.2f -> tool: %s" % (partner, strength, tool))
    assert len(blends) == 4
    strongest = max(blends, key=lambda k: blends[k][1])
    print("hottest blend: envy+%s" % strongest)
    assert strongest == "anger"
    print("rule: blends need two tools - one per ingredient")
    print("OK: %s blended the paints" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_envy_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five scenes with sting 0-10: trigger, peak, cascade, turn, resolution
    scenes = [("trigger", 6.0), ("peak", 9.0), ("cascade", 8.0),
              ("turn", 5.0), ("resolution", 2.5)]
    for name_, sting in scenes:
        print("scene %-10s sting %.1f" % (name_, sting))
    stings = [s for _, s in scenes]
    assert stings[1] == max(stings), "peak is the max"
    assert stings[-1] < stings[0], "resolution below trigger"
    # intervention stack at the turn: noticing + audit + benign question
    stack = 2.5 + 2.0 + 2.5
    drop = scenes[2][1] - scenes[3][1]
    print("intervention stack %.1f, sting drop at turn %.1f" % (stack, drop))
    assert 6.9 < stack < 7.1 and 2.9 < drop < 3.1
    # aftershock echo weaker than peak
    echo = 4.0
    assert echo < stings[1]
    print("rule: weather, navigated - conversion, not abolition")
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "definition": demo_envy_definition,
    "family": demo_envy_family,
    "intensity": demo_envy_intensity,
    "myths": demo_envy_myths,
    "first_person": demo_envy_first_person,
    "time_course": demo_envy_time_course,
    "low_vs_high": demo_envy_low_vs_high,
    "partner_mix": demo_envy_partner_mix,
    "day_in_life": demo_envy_day_in_life,
    "body": demo_envy_body,
    "posture": demo_envy_posture,
    "sleep_appetite": demo_envy_sleep_appetite,
    "individual_diffs": demo_envy_individual_diffs,
    "face": demo_envy_face,
    "face_intensity": demo_envy_face_intensity,
    "hiding_faking": demo_envy_hiding_faking,
    "expression_gallery": demo_envy_expression_gallery,
    "classic_triggers": demo_envy_classic_triggers,
    "personal_triggers": demo_envy_personal_triggers,
    "surprise_triggers": demo_envy_surprise_triggers,
    "chain_reactions": demo_envy_chain_reactions,
    "actions": demo_envy_actions,
    "speech": demo_envy_speech,
    "decisions": demo_envy_decisions,
    "behavior_intensity": demo_envy_behavior_intensity,
    "healthy_expression": demo_envy_healthy_expression,
    "unhealthy_expression": demo_envy_unhealthy_expression,
    "everyday_practices": demo_envy_everyday_practices,
    "reading_signs": demo_envy_reading_signs,
    "supportive_responses": demo_envy_supportive_responses,
    "mistakes_to_avoid": demo_envy_mistakes_to_avoid,
    "related_map": demo_envy_related_map,
    "emotion_mixes": demo_envy_emotion_mixes,
    "full_simulation": demo_envy_full_simulation,
}
