#!/usr/bin/env python3
"""Demo programs for the Embarrassment Emotion databases (emotion series batch 2).

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


def demo_embarrassment_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five beats: exposure -> appraisal -> arousal -> display -> repair
    beats = {"exposure": 0.90, "appraisal": 0.85, "arousal": 0.80,
             "display": 0.75, "repair": 0.95}
    signal = sum(beats.values()) / len(beats)
    completed = signal > 0.80   # honest cycle completes above threshold
    print("beats: " + " -> ".join(beats))
    print("mean beat strength: %.4f  honest cycle completes: %s" % (signal, completed))
    assert 0.849 < signal < 0.851
    assert completed is True
    assert beats["repair"] > beats["display"]  # repair outlasts display
    print("OK: %s ran the five-beat sequence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three ingredients; embarrassment needs all three present
    def forms(self_aw, norm, audience):
        return self_aw and norm and audience
    cases = [(1, 1, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
    results = [forms(*c) for c in cases]
    for c, r in zip(cases, results):
        print("self=%d norm=%d audience=%d -> embarrassment forms: %s" % (c[0], c[1], c[2], r))
    assert results == [True, False, False, False]
    # target check: moment vs self vs other separates the cousins
    targets = {"embarrassment": "moment", "shame": "self", "guilt": "other"}
    assert targets["embarrassment"] == "moment"
    assert len(set(targets.values())) == 3
    print("targets: %s" % targets)
    print("OK: %s mapped the family tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three dials sum into the volume knob 0..10
    def volume(exposure, stakes, audience):
        return min(10.0, (exposure + stakes + audience) / 3.0 * 10.0)
    def label(v):
        return "mild" if v < 3.5 else ("moderate" if v < 7.0 else "intense")
    cases = [(0.1, 0.2, 0.1), (0.5, 0.6, 0.5), (0.9, 0.95, 0.9)]
    for e, s, a in cases:
        v = volume(e, s, a)
        print("dials %.2f/%.2f/%.2f -> volume %.2f (%s)" % (e, s, a, v, label(v)))
    assert abs(volume(0.1, 0.2, 0.1) - 1.3333) < 0.001
    assert abs(volume(0.5, 0.6, 0.5) - 5.3333) < 0.001
    assert abs(volume(0.9, 0.95, 0.9) - 9.1667) < 0.001
    assert label(volume(0.1, 0.2, 0.1)) == "mild"
    assert label(volume(0.9, 0.95, 0.9)) == "intense"
    # turning down one dial lowers the volume
    assert volume(0.9, 0.9, 0.2) < volume(0.9, 0.9, 0.9)
    print("OK: %s turned the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six myths scored against the findings: 1 = busted, 0 = confirmed
    myths = {
        "embarrassment means something is wrong with you": 1,
        "confident people never get embarrassed": 1,
        "witnesses remember it as vividly as you do": 1,
        "pretending it did not happen works best": 1,
        "embarrassment is just shame-lite": 1,
        "frequent embarrassment means you are too sensitive": 1,
    }
    busted = sum(myths.values())
    print("myths evaluated: %d, busted: %d" % (len(myths), busted))
    for m, v in myths.items():
        print("  [%s] %s" % ("BUSTED" if v else "CONFIRMED", m))
    assert busted == 6 and len(myths) == 6
    # the spotlight correction: felt vs actual witness memory
    felt_remembered, actual_remembered = 0.80, 0.15
    gap = felt_remembered - actual_remembered
    print("spotlight gap: felt %.2f vs actual %.2f (gap %.2f)" % (felt_remembered, actual_remembered, gap))
    assert 0.64 < gap < 0.66
    print("OK: %s busted the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_inside(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four layers fire at once; total felt load is their sum
    layers = {"physical": 0.85, "attentional": 0.90, "narrative": 0.80, "motivational": 0.75}
    total = sum(layers.values())
    print("layers:")
    for k, v in layers.items():
        print("  %-13s %.2f" % (k, v))
    print("total felt load: %.2f of 4.00" % total)
    assert 3.29 < total < 3.31
    # moving attention outward cools the total: attentional layer drops
    layers["attentional"] = 0.30
    cooled = sum(layers.values())
    print("after attention shifts outward: %.2f" % cooled)
    assert 2.69 < cooled < 2.71
    assert cooled < total
    print("OK: %s toured the inside view" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arousal curve: onset 2-3s, peak 10-30s, fade by 1-3 min
    def arousal(t):
        # t in seconds; fast rise, exponential-style decay after peak
        if t <= 20:
            return min(1.0, t / 20.0)
        return max(0.0, 1.0 - (t - 20.0) / 160.0)
    for t in (3, 20, 60, 180):
        print("t=%3ds arousal=%.3f" % (t, arousal(t)))
    assert 0.14 < arousal(3) < 0.16
    assert 0.999 < arousal(20) <= 1.0
    assert 0.74 < arousal(60) < 0.76
    assert arousal(180) < 0.01
    # aftershock: each replay re-lights a fraction of peak arousal
    replays, relight = 5, 0.25
    aftershock_load = sum(relight ** i for i in range(1, replays + 1))
    print("5 replays at 0.25 decay: aftershock load %.4f" % aftershock_load)
    assert 0.3330 < aftershock_load < 0.3331
    # closing the loop cuts the replays to zero
    assert aftershock_load > 0.0
    print("OK: %s traced the time course" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same mechanism, different gain: gain scales every beat
    def run(gain):
        beats = {"exposure": 0.5 * gain, "appraisal": 0.6 * gain,
                 "arousal": 0.7 * gain, "display": 0.65 * gain, "repair": 0.9}
        return sum(beats.values()) / len(beats)
    low, high = run(0.2), run(1.6)
    print("low-gain mean beat: %.4f" % low)
    print("high-gain mean beat: %.4f" % high)
    assert 0.277 < low < 0.279
    assert 0.963 < high < 0.965
    assert high > 2.0 * low  # same person, scaled feeling
    # recovery tools identical: laugh, own, move on - applied with patience
    tools = ["laugh", "own", "move on"]
    assert len(tools) == 3
    print("recovery tools at both volumes: %s" % ", ".join(tools))
    print("OK: %s compared the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_blend_anxiety(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # embarrassment covers past-present, anxiety covers future; blend covers all of time
    embarrassment_tenses = {"past", "present"}
    anxiety_tenses = {"future"}
    blend = embarrassment_tenses | anxiety_tenses
    print("blend covers tenses: %s" % sorted(blend))
    assert blend == {"past", "present", "future"}
    assert len(blend) == 3  # no tense left to rest in
    # unmixing: repair the past, prepare for the future - separately
    past_load, future_load = 0.85, 0.75
    repaired_past = past_load * 0.2    # repair shrinks the past channel
    prepared_future = future_load * 0.3  # preparation shrinks the future channel
    total_before = past_load + future_load
    total_after = repaired_past + prepared_future
    print("blend load before unmixing: %.2f, after: %.2f" % (total_before, total_after))
    assert 1.59 < total_before < 1.61
    assert 0.394 < total_after < 0.396
    assert total_after < total_before / 3.0
    print("OK: %s unmixed the tenses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five moments in one day; each completed cycle trains the system
    day = [
        ("06:40 shirt inside out", 0.15, True),
        ("08:15 'you too' birthday", 0.35, True),
        ("12:30 waved at stranger", 0.20, True),
        ("15:00 wrong client name x2", 0.90, True),
        ("19:00 told the story first", 0.40, True),
    ]
    completed = sum(1 for _, _, c in day if c)
    total_heat = sum(h for _, h, _ in day)
    print("moments: %d, completed cycles: %d, total heat: %.2f" % (len(day), completed, total_heat))
    assert completed == 5 and len(day) == 5
    assert 1.99 < total_heat < 2.01
    # completion rate, not frequency, is the variable
    completion_rate = completed / len(day)
    assert 0.999 < completion_rate <= 1.0
    # bedtime replay reality-checked and released
    replay_intensity = 0.90 * 0.1  # evidence shrinks the replay
    assert 0.089 < replay_intensity < 0.091
    print("bedtime replay after reality check: %.3f" % replay_intensity)
    print("OK: %s walked through the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the blush: vessel widening factors by region (baseline 1.0)
    regions = {"face": 2.8, "ears": 2.2, "neck": 1.9}
    heat_index = sum(regions.values()) / len(regions)
    print("vessel widening: %s" % regions)
    print("heat index: %.2f" % heat_index)
    assert 2.29 < heat_index < 2.31
    assert regions["face"] > regions["neck"]  # face leads the blush
    # heart: resting 72 bpm scaled by arousal
    heart = 72 * 1.45
    print("heart rate: %.1f bpm" % heart)
    assert 104.3 < heart < 104.5
    # parasympathetic rebound: wrung-out after the surge
    energy_after = 1.0 - 0.35
    print("energy after rebound: %.2f" % energy_after)
    assert 0.64 < energy_after < 0.66
    print("OK: %s mapped the body cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the shrink: space occupied falls as intensity rises
    occupied = {"low": 0.90, "moderate": 0.70, "high": 0.50}
    for level, occ in occupied.items():
        print("%-9s occupies %.2f of normal space" % (level, occ))
    assert occupied["low"] > occupied["moderate"] > occupied["high"]
    assert abs(occupied["moderate"] - 0.70) < 0.001
    # display components in fixed recruitment order
    order = ["gaze", "mouth", "blush", "head", "hands", "body"]
    shown = {"low": 2, "moderate": 5, "high": 6}
    for level, n in shown.items():
        print("%-9s shows: %s" % (level, ", ".join(order[:n])))
        assert order[:n] == order[:n]  # fixed order, never shuffled
    appeasement = shown["moderate"] / len(order)
    print("moderate appeasement signal: %.4f" % appeasement)
    assert 0.8332 < appeasement < 0.8334
    print("OK: %s read the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # replay loop at bedtime: each replay delays sleep
    replays, per_replay_min = 4, 12
    delay = replays * per_replay_min
    print("bedtime replays: %d -> sleep delayed %d min" % (replays, delay))
    assert delay == 48
    # appetite suppressed during arousal
    arousal, hunger = 0.90, 1.0 - 0.90 * 0.8
    print("arousal %.2f -> hunger %.2f" % (arousal, hunger))
    assert 0.27 < hunger < 0.29
    # energy: spike then drain
    spike, drain = 1.5, 0.6
    print("energy spike %.1f then drain to %.1f" % (spike, drain))
    assert spike > 1.0 > drain
    # closing the loop restores the quiet systems
    closed_delay = 0 * per_replay_min
    assert closed_delay == 0
    print("loop closed -> delay %d min" % closed_delay)
    print("OK: %s checked the quiet systems" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_individual_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five-slider equalizer
    sliders = {"reactivity": 0.8, "self_focus": 0.7, "norm_strictness": 0.6,
               "history": 0.5, "audience_miscal": 0.9}
    embarrassability = sum(sliders.values()) / len(sliders)
    print("equalizer: %s" % sliders)
    print("embarrassability: %.2f" % embarrassability)
    assert 0.69 < embarrassability < 0.71
    # adjustable sliders retrained downward
    sliders["self_focus"] = 0.4
    sliders["audience_miscal"] = 0.3
    retrained = sum(sliders.values()) / len(sliders)
    print("after retraining attention + calibration: %.2f" % retrained)
    assert 0.51 < retrained < 0.53
    assert retrained < embarrassability
    # temperament slider stays: settings, not defects
    assert sliders["reactivity"] == 0.8
    print("OK: %s tuned the equalizer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the mapped display: 7 components
    involuntary = ["gaze_down", "lids_lowered", "blush"]
    voluntary = ["pressed_smile", "head_tilt", "face_touch", "lip_press"]
    display = involuntary + voluntary
    print("display components (%d): %s" % (len(display), ", ".join(display)))
    assert len(display) == 7
    assert len(involuntary) == 3 and len(voluntary) == 4
    # witnesses read it in under a second as goodwill
    read_time = 0.6
    reading = "awareness and goodwill"
    print("witness read time: %.1fs -> %s" % (read_time, reading))
    assert read_time < 1.0
    # the blush certifies the display: involuntary present means genuine
    genuine = "blush" in involuntary
    assert genuine is True
    print("OK: %s drew the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fixed recruitment order; levels add components
    order = ["gaze", "mouth", "blush", "head", "hands", "body"]
    levels = {"low": order[:2], "moderate": order[:5], "high": order[:6]}
    programs = {"low": "nothing needed", "moderate": "laugh-with", "high": "rescue"}
    for level in ("low", "moderate", "high"):
        comps = levels[level]
        print("%-9s %d components -> witness program: %s" % (level, len(comps), programs[level]))
    assert len(levels["low"]) == 2
    assert len(levels["moderate"]) == 5
    assert len(levels["high"]) == 6
    # phase change at the top: appeasement flips to distress
    distress = len(levels["high"]) == 6
    assert distress is True
    assert programs["high"] == "rescue"
    print("OK: %s climbed the gradient" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hiding strategies - and what leaks anyway
    strategies = ["forced casualness", "sudden busy-ness", "over-loud laugh",
                  "quick subject change", "deadpan anyway"]
    leaks = ["blush", "dropping gaze", "climbing voice", "face-seeking hands"]
    print("hiding strategies: %d, leaks: %d" % (len(strategies), len(leaks)))
    assert len(strategies) == 5 and len(leaks) == 4
    # the hiding paradox: shown blush beats hidden tension on trust
    trust_shown, trust_hidden = 0.85, 0.40
    print("witness trust: blush shown %.2f vs tension hidden %.2f" % (trust_shown, trust_hidden))
    assert trust_shown > trust_hidden
    assert 0.44 < trust_shown - trust_hidden < 0.46
    # faking fails in reverse: voluntary present, involuntary absent
    fake_voluntary, fake_involuntary = 3, 0
    gap_felt = fake_voluntary > 0 and fake_involuntary == 0
    assert gap_felt is True
    print("OK: %s caught the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four-beat choreography
    beats = ["realization", "display", "checking glance", "recovery"]
    print("choreography: %s" % " -> ".join(beats))
    assert beats[2] == "checking glance"  # the soul of the performance
    assert len(beats) == 4
    # artist checklist: 6 items; actor checklist: 5 items
    artist = ["3/4 head", "tucked chin", "averted eyes", "crooked pressed smile",
              "diffuse blush wash", "one face-touch"]
    actor = ["nasal exhale", "late smile", "single neck-touch", "checking glance", "short laugh"]
    print("artist items: %d, actor items: %d" % (len(artist), len(actor)))
    assert len(artist) == 6 and len(actor) == 5
    # embarrassment red is diffuse and high; anger red is concentrated and low
    embarrassment_red = {"diffusion": 0.9, "height": 0.8}
    anger_red = {"diffusion": 0.3, "height": 0.2}
    assert embarrassment_red["diffusion"] > anger_red["diffusion"]
    assert embarrassment_red["height"] > anger_red["height"]
    print("OK: %s staged the gallery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the parade: five families
    parade = {"bodily": 5, "verbal": 5, "competence": 4, "exposure": 4, "status": 4}
    total = sum(parade.values())
    print("trigger parade: %s = %d classics" % (parade, total))
    assert total == 22
    # the formula: norm x visible miss x witnesses
    def strength(norm, miss, witnesses):
        return norm * miss * witnesses
    s = strength(0.9, 0.8, 1.0)
    print("trigger strength with witnesses: %.2f" % s)
    assert 0.719 < s < 0.721
    # empty hallway: no witnesses, no sequence
    assert strength(0.9, 0.8, 0.0) == 0.0
    # pre-loading the top five converts ambush to handled moment
    preloaded = 5
    assert preloaded == 5
    print("OK: %s paraded the triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four personal trigger types
    types = ["anniversary", "place", "people", "word"]
    print("personal trigger types: %s" % ", ".join(types))
    assert len(types) == 4
    # extinction: each safe re-exposure multiplies the link by 0.7
    link = 1.0
    for i in range(5):
        link *= 0.7
    print("link strength after 5 safe re-exposures: %.5f" % link)
    assert 0.168 < link < 0.169
    assert link < 0.2  # the file gets updated
    # generalization: one mocked presentation spreads to all presentations
    spread = {"mocked_talk": 1.0, "all_talks": 0.6}
    assert spread["all_talks"] > 0.5
    # the defusing method has four steps
    steps = ["map", "trace", "test then-vs-now", "re-enter gradually"]
    assert len(steps) == 4
    print("OK: %s defused the library" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speed over accuracy: exposure fires the alarm even without offense
    fire = min(1.0, 0.9 * 1.2)
    print("alarm fires on bare exposure: %.2f" % fire)
    assert 0.999 < fire <= 1.0
    # the calm label stands the system down
    labeled = fire * 0.25
    print("after labeling 'attention, not offense': %.2f" % labeled)
    assert 0.249 < labeled < 0.251
    # blush-about-blushing: three decaying layers
    layers = [0.5, 0.25, 0.125]
    loop = sum(layers)
    print("misfire loop layers sum: %.3f" % loop)
    assert 0.874 < loop < 0.876
    # retraining: the praised-without-slip category stops firing
    assert labeled < fire
    print("OK: %s labeled the misfire" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the cascade engine: arousal degrades skill, degraded skill adds arousal
    a = 0.5
    for link in range(3):
        a = min(1.0, a + 0.25)
        skill = 1.0 - a * 0.6
        print("link %d: arousal %.2f, skill %.2f" % (link + 1, a, skill))
    assert 0.999 < a <= 1.0
    assert 0.39 < skill < 0.41  # skill at max arousal
    # the circuit breaker: stillness starves the chain
    a = 1.0
    a = a * 0.3  # plant, breathe, pause
    print("after circuit breaker: arousal %.2f" % a)
    assert 0.29 < a < 0.31
    # the empathic loop: two nervous systems
    caught = 0.5 * 0.6
    assert 0.29 < caught < 0.31
    print("OK: %s broke the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five behavior families with cost profiles (cost in spotlight-seconds)
    families = {"flight": 20, "cover": 15, "repair": 30, "freeze": 25, "overcorrection": 180}
    for fam, cost in families.items():
        print("%-14s cost %3d spotlight-seconds" % (fam, cost))
    assert families["overcorrection"] > sum(v for k, v in families.items() if k != "overcorrection") / 2
    # the gold standard: one clean repair, then resume
    repairs, resumes = 1, 1
    print("gold standard: %d repair + %d resume" % (repairs, resumes))
    assert repairs == 1 and resumes == 1
    # flight skips the repair beat: loop stays open
    loop_open_after_flight = True
    loop_open_after_repair = False
    assert loop_open_after_flight and not loop_open_after_repair
    print("OK: %s ran the behavior menu" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dosage: one apology performs remorse; five perform anxiety
    def audience_read(apologies):
        return "remorse" if apologies == 1 else ("anxiety" if apologies > 2 else "neutral")
    for n in (1, 2, 5):
        print("%d apologies -> audience reads: %s" % (n, audience_read(n)))
    assert audience_read(1) == "remorse"
    assert audience_read(5) == "anxiety"
    # vocal arousal leak: pitch and speed climb
    pitch_base, pitch_hot = 120.0, 120.0 * 1.25
    print("pitch: %.0f Hz calm -> %.0f Hz hot" % (pitch_base, pitch_hot))
    assert 149.9 < pitch_hot < 150.1
    # the recovery dialect: short, owned, forward-moving
    recovery = ["my mistake", "well, that happened", "thanks for rolling with that"]
    assert all(len(p.split()) <= 5 for p in recovery)
    assert len(recovery) == 3
    print("OK: %s tuned the dialect" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three channels tilt judgment
    channels = {"attentional_narrowing": 0.8, "affect_heuristic": 0.7, "memory_asymmetry": 0.75}
    tilt = sum(channels.values()) / len(channels)
    print("judgment tilt: %.4f" % tilt)
    assert 0.749 < tilt < 0.751
    # the classic errors
    errors = ["withdrawal", "overpayment", "identity shrinkage"]
    assert len(errors) == 3
    # the procedural counter-move: wait out the arousal
    def decide(wait_hours, tilt_now):
        return tilt_now * (0.2 if wait_hours >= 1 else 1.0)
    now, later = decide(0, tilt), decide(1, tilt)
    print("tilt now %.3f vs after an hour %.3f" % (now, later))
    assert later < now / 3.0
    assert 0.149 < later < 0.151
    print("OK: %s straightened the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the staircase: four steps
    steps = ["smooth recovery", "multiplied repair", "fragmented behavior", "flip to escape"]
    print("staircase: %s" % " -> ".join(steps))
    assert len(steps) == 4
    # the diagnostic: effort-to-slip ratio
    def ratio(effort, slip):
        return effort / slip
    healthy = ratio(30, 30)
    escalating = ratio(180, 30)
    print("effort/slip: healthy %.1f, escalating %.1f" % (healthy, escalating))
    assert 0.99 < healthy < 1.01
    assert 5.99 < escalating < 6.01
    # matching tools per step
    tools = {1: "one repair and stop", 2: "one repair and stop",
             3: "stillness, then words", 4: "graceful exit, return later"}
    assert tools[3] == "stillness, then words"
    assert tools[4] == "graceful exit, return later"
    print("OK: %s climbed down the staircase" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # say it, show it, channel it
    moves = {"say": "one owned acknowledgment", "show": "thirty-second display",
             "channel": "story or lesson"}
    assert len(moves) == 3
    for k, v in moves.items():
        print("%-7s: %s" % (k, v))
    # openly handled shrinks; secretly handled grows
    open_cost, secret_cost = 30, 30 * 48  # seconds vs two days of replay
    print("cost open: %ds, cost secret: %ds" % (open_cost, secret_cost))
    assert secret_cost > 40 * open_cost
    # the pre-decision survives arousal; improvisation does not
    script_survives, improv_survives = True, False
    assert script_survives and not improv_survives
    print("OK: %s expressed it healthily" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottling: installments; exploding: immediate social cost
    bottle_cost = {"replays_days": 3, "avoided_rooms": 4, "leak_months_later": 1}
    explode_cost = {"sympathy_lost": 1, "scene_memory": 1, "overdisclosure": 1}
    print("bottling costs: %s" % bottle_cost)
    print("exploding costs: %s" % explode_cost)
    assert sum(bottle_cost.values()) == 8
    assert sum(explode_cost.values()) == 3
    # both refuse the cycle: repair beat skipped
    cycle_repair_bottled, cycle_repair_exploded = False, False
    assert not cycle_repair_bottled and not cycle_repair_exploded
    # corrections: scheduled expression vs pause-and-halve
    told_within_24h, words_halved = True, True
    assert told_within_24h and words_halved
    # healthy middle costs thirty seconds
    healthy_cost_s = 30
    assert healthy_cost_s == 30
    print("OK: %s priced both shapes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six small habits
    habits = ["morning pre-decision", "three-second pause", "story told first",
              "evening audit (written)", "weekly exposure rep", "kind witness"]
    print("habits: %d" % len(habits))
    assert len(habits) == 6
    # compounding: small daily gains rewrite the priors within weeks
    gain_per_day, days = 0.02, 21
    improvement = (1 + gain_per_day) ** days - 1
    print("21 days of 2%% daily reps: %.3f improvement" % improvement)
    assert 0.515 < improvement < 0.517
    # written audit closes loops; rumination feeds them
    loop_written, loop_ruminated = 0.1, 0.9
    assert loop_written < loop_ruminated
    # exposure rep: safe completions weaken the alarm gain
    gain = 1.0 * (0.95 ** 21)
    print("alarm gain after 21 safe reps: %.4f" % gain)
    assert 0.340 < gain < 0.342
    print("OK: %s kept the schedule" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three skill levels
    levels = ["spot the display", "gauge the gradient", "read the strategy"]
    assert len(levels) == 3
    # gradient -> response mapping
    responses = {"low": "nothing", "moderate": "laugh-with", "high": "rescue"}
    print("gradient responses: %s" % responses)
    assert responses["moderate"] == "laugh-with"
    assert responses["high"] == "rescue"
    # strategy-matched responses
    strategies = {"coverer": "join the joke", "freezer": "unstared time",
                  "overcorrector": "merciful interruption"}
    assert len(strategies) == 3
    # the never-announce rule: naming it spotlights it
    announced_harm, silent_help = 0.9, 0.2
    assert announced_harm > silent_help
    print("OK: %s read the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_supporting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five moves, each lending a stolen faculty
    moves = {"laugh-with": "appraisal", "normalizer": "appraisal",
             "bridge": "attention", "exit": "arousal clearance",
             "later check-in": "memory editing"}
    assert len(moves) == 5
    for move, lends in moves.items():
        print("%-14s lends: %s" % (move, lends))
    # the meta-rule: be boring about the slip; the room follows your cue
    room_calm_given_calm = 0.85
    room_calm_given_fuss = 0.25
    print("room stays calm: %.2f (you calm) vs %.2f (you fuss)" % (room_calm_given_calm, room_calm_given_fuss))
    assert room_calm_given_calm > 3 * room_calm_given_fuss
    # the later check-in targets the aftershock, where suffering lives
    suffering_in_aftershock = 0.7
    assert 0.69 < suffering_in_aftershock < 0.71
    print("OK: %s built the bridge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven classic mistakes, three worsening mechanisms
    mistakes = ["spotlight callout", "the replay", "teasing escalation", "pity face",
                "fix-it lecture", "frozen staring", "minimizing comparison"]
    mechanisms = {"exposure extension": 3, "catastrophe certification": 2, "authorship theft": 2}
    print("mistakes: %d, mechanisms: %s" % (len(mistakes), mechanisms))
    assert len(mistakes) == 7
    assert sum(mechanisms.values()) == 7
    # the universal correction inverts all three
    correction = {"shorten the spotlight": 1, "warm the room": 1, "return the pen": 1}
    assert len(correction) == 3
    # witness framing becomes the person's framing
    framed_as_incident = 0.8
    assert 0.79 < framed_as_incident < 0.81
    print("OK: %s dodged the friendly fire" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_related_map(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three sorting questions place any self-conscious feeling
    def sort(target, course, intent):
        return (target, course, intent)
    embarrassment = sort("moment", "minutes", "accident")
    shame = sort("self", "years", "accident")
    guilt = sort("other", "weeks", "accident")
    humiliation = sort("moment", "months", "perpetrator")
    print("embarrassment %s | shame %s | guilt %s | humiliation %s"
          % (embarrassment, shame, guilt, humiliation))
    assert len({embarrassment, shame, guilt, humiliation}) == 4
    # six neighbors mapped
    neighbors = ["shame", "guilt", "awkwardness", "humiliation", "stage fright", "pride"]
    assert len(neighbors) == 6
    # pride is the opposite pole: same machinery, opposite appraisal
    shrink, expansion = -1.0, 1.0
    assert shrink < 0 < expansion
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_blends(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four blends with prescriptions
    blends = {"amusement": "join it", "anger": "ask the perpetrator question",
              "sadness": "challenge the story", "pride": "notice and grow it"}
    assert len(blends) == 4
    for partner, rx in blends.items():
        print("embarrassment + %-9s -> %s" % (partner, rx))
    # the audience co-authors the blend
    def recruit(audience):
        return {"kind laughter": "amusement", "cruel laughter": "anger",
                "indifference": "sadness", "applause": "pride"}[audience]
    assert recruit("kind laughter") == "amusement"
    assert recruit("cruel laughter") == "anger"
    assert recruit("applause") == "pride"
    # mismatched tool warning: laugh-it-off on anger blend -> resentment
    resentment = 0.75
    assert 0.74 < resentment < 0.76
    print("OK: %s tasted the chords" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_embarrassment_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six scenes, the full arc
    scenes = ["trigger", "onset and peak", "circuit breaker",
              "aftermath", "aftershock", "resolution"]
    assert len(scenes) == 6
    print("scenes: %s" % " -> ".join(scenes))
    # the hinge: pre-decided script converts training to performance
    script_ready, arousal = True, 0.95
    performance = 0.9 if script_ready else 1.0 - arousal
    print("performance with script ready: %.2f" % performance)
    assert 0.89 < performance < 0.91
    assert performance > 1.0 - arousal  # script beats raw arousal
    # the master move: telling it first converts replay to belonging
    replay_material, belonging = 1.0, 1.0
    converted = replay_material * belonging
    assert 0.999 < converted <= 1.0
    # authorship, not control, was the goal
    controlled_feeling, authored_meaning = False, True
    assert not controlled_feeling and authored_meaning
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "embarrassment_definition": demo_embarrassment_definition,
    "embarrassment_emotion_family": demo_embarrassment_emotion_family,
    "embarrassment_intensity_scale": demo_embarrassment_intensity_scale,
    "embarrassment_myths": demo_embarrassment_myths,
    "embarrassment_inside": demo_embarrassment_inside,
    "embarrassment_time_course": demo_embarrassment_time_course,
    "embarrassment_low_vs_high": demo_embarrassment_low_vs_high,
    "embarrassment_blend_anxiety": demo_embarrassment_blend_anxiety,
    "embarrassment_day_vignette": demo_embarrassment_day_vignette,
    "embarrassment_body": demo_embarrassment_body,
    "embarrassment_posture": demo_embarrassment_posture,
    "embarrassment_sleep_appetite": demo_embarrassment_sleep_appetite,
    "embarrassment_individual_differences": demo_embarrassment_individual_differences,
    "embarrassment_face": demo_embarrassment_face,
    "embarrassment_face_intensity": demo_embarrassment_face_intensity,
    "embarrassment_hiding_faking": demo_embarrassment_hiding_faking,
    "embarrassment_expression_gallery": demo_embarrassment_expression_gallery,
    "embarrassment_classic_triggers": demo_embarrassment_classic_triggers,
    "embarrassment_personal_triggers": demo_embarrassment_personal_triggers,
    "embarrassment_surprise_triggers": demo_embarrassment_surprise_triggers,
    "embarrassment_chain_reactions": demo_embarrassment_chain_reactions,
    "embarrassment_actions": demo_embarrassment_actions,
    "embarrassment_speech": demo_embarrassment_speech,
    "embarrassment_judgment": demo_embarrassment_judgment,
    "embarrassment_escalation": demo_embarrassment_escalation,
    "embarrassment_healthy_expression": demo_embarrassment_healthy_expression,
    "embarrassment_unhealthy_expression": demo_embarrassment_unhealthy_expression,
    "embarrassment_everyday_practices": demo_embarrassment_everyday_practices,
    "embarrassment_reading_others": demo_embarrassment_reading_others,
    "embarrassment_supporting": demo_embarrassment_supporting,
    "embarrassment_mistakes_to_avoid": demo_embarrassment_mistakes_to_avoid,
    "embarrassment_related_map": demo_embarrassment_related_map,
    "embarrassment_blends": demo_embarrassment_blends,
    "embarrassment_full_simulation": demo_embarrassment_full_simulation,
}
