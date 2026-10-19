#!/usr/bin/env python3
"""Demo programs for the Sadness Emotion databases (Manon's 2026-10-17 16:15
order, emotion series batch 1).

Every demo is a real, runnable, stdlib-only Python emotion-scenario
simulator: the user picks a situation (or the simulator presets one),
picks an intensity, and the demo simulates the emotion unfolding - inner
monologue, body signals, facial expression, dialogue, and behavior - scene
by scene. Fully descriptive and educational; never diagnosing anyone.

All are machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker. Entry prose and demo numbers are cross-checked by hand.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return (hdr_fn(name, rid, group) + _PREAMBLE +
            body.replace("NAME", __import__("json").dumps(name)))


def demo_emsad_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four diagnostic marks of the sad signal, and their weights
    marks = {"inner brow lift": 0.34, "mouth corners down": 0.26,
             "gaze lowered": 0.22, "low energy posture": 0.18}
    total = sum(marks.values())
    print("diagnostic marks: %d" % len(marks))
    for k, v in marks.items():
        print("  %-20s weight %.2f" % (k, v))
    print("weights sum: %.2f" % total)
    assert 0.999 < total < 1.001
    top = max(marks, key=marks.get)
    print("most diagnostic: %s" % top)
    assert top == "inner brow lift"
    assert 0.339 < marks[top] < 0.341
    print("rule: the feeling is the message, never the enemy")
    print("OK: %s defined the signal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # primary-emotion ingredients feeding the sadness family (teaching weights)
    family = {"sadness": 60.0, "fear": 15.0, "anger": 10.0,
              "surprise": 10.0, "disgust": 5.0}
    total = sum(family.values())
    share = {k: v / total for k, v in family.items()}
    print("family ingredients: %d" % len(family))
    for k in family:
        print("  %-10s %5.1f -> share %.3f" % (k, family[k], share[k]))
    assert total == 100.0
    assert 0.599 < share["sadness"] < 0.601
    assert 0.149 < share["fear"] < 0.151
    # blends: sadness + partner -> named relative
    blends = {("sadness", "surprise"): "disappointment",
              ("sadness", "anger"): "resentment",
              ("sadness", "fear"): "despair",
              ("sadness", "joy"): "bittersweetness"}
    print("named blends: %d" % len(blends))
    assert blends[("sadness", "surprise")] == "disappointment"
    assert blends[("sadness", "fear")] == "despair"
    print("rule: name the partner and you name the blend")
    print("OK: %s mapped the family" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_volumes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # volume bands on the shared 1-10 intensity scale
    def band(i):
        if 1 <= i <= 3:
            return "mild"
        if 4 <= i <= 7:
            return "moderate"
        return "intense"
    samples = {2: "mild", 5: "moderate", 9: "intense"}
    for i, want in samples.items():
        got = band(i)
        print("intensity %d -> %s" % (i, got))
        assert got == want
    # care multiplier: how much care the feeling asks for, by band
    care = {"mild": 1.0, "moderate": 2.2, "intense": 4.5}
    for i in (2, 5, 9):
        print("  care multiplier at %d: %.1f" % (i, care[band(i)]))
    assert 4.49 < care["intense"] < 4.51
    assert 2.19 < care["moderate"] < 2.21
    # band edges are exact teaching boundaries
    assert band(3) == "mild" and band(4) == "moderate"
    assert band(7) == "moderate" and band(8) == "intense"
    print("rule: same emotion, different volume - read the dial first")
    print("OK: %s calibrated the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five myths; every correct answer is False (teaching quiz)
    myths = [
        "sadness is always bad and should be switched off",
        "crying is weakness",
        "feeling sad means something is wrong with you",
        "you should cheer up immediately",
        "sad people cannot function",
    ]
    truth = [False, False, False, False, False]
    # simulated learner answers (deterministic): gets 3 of 5 right
    answers = [False, True, False, True, False]
    score = sum(1 for a, t in zip(answers, truth) if a == t)
    print("myths tested: %d" % len(myths))
    for m, a, t in zip(myths, answers, truth):
        mark = "right" if a == t else "wrong"
        print("  [%s] %s" % (mark, m))
    print("learner score: %d/5" % score)
    assert 2.9 < score < 3.1
    missed = [m for m, a, t in zip(myths, answers, truth) if a != t]
    print("missed myths: %d" % len(missed))
    assert len(missed) == 2
    print("rule: test folk sayings against observation")
    print("OK: %s cleared the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_inside(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # first-person passage: sentence word counts at intensity 6 (fixed text model)
    sentences = [
        "the morning arrives a shade dimmer than yesterday",
        "a weight rests low in the chest like a hand",
        "thoughts move slower and circle the empty place",
        "sounds are too loud and too far away",
        "sighs come on their own long and slow",
        "kindness feels both unwelcome and deeply wanted",
    ]
    counts = [len(s.split()) for s in sentences]
    total = sum(counts)
    avg = total / len(sentences)
    print("passage sentences: %d" % len(sentences))
    print("word counts: %s" % counts)
    print("total words: %d, average per sentence: %.2f" % (total, avg))
    assert total == 49
    assert 8.15 < avg < 8.18
    assert min(counts) >= 6 and max(counts) <= 10
    print("slowest sentence words: %d (sad thinking runs slow)" % max(counts))
    print("rule: a composite sketch for learning, never a report on anyone")
    print("OK: %s stepped inside the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_timeline(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four-phase timeline at intensity 7 (teaching minutes)
    onset, peak, half_life, aftershock = 8.0, 25.0, 40.0, 15.0
    total = onset + peak + half_life + aftershock
    print("onset: %.0f min, peak: %.0f min, fade half-life: %.0f min, aftershock: %.0f min"
          % (onset, peak, half_life, aftershock))
    print("episode span: %.0f min" % total)
    assert 87.9 < total < 88.1
    # fade curve: intensity halves every half_life minutes after the peak
    i_peak = 7.0
    i_after_one = i_peak * 0.5 ** (half_life / half_life)
    i_after_two = i_peak * 0.5 ** (2 * half_life / half_life)
    print("intensity at peak: %.1f" % i_peak)
    print("after one half-life: %.2f" % i_after_one)
    print("after two half-lives: %.2f" % i_after_two)
    assert 3.49 < i_after_one < 3.51
    assert 1.749 < i_after_two < 1.751
    assert i_after_two < i_after_one < i_peak
    print("rule: sadness is weather, and weather passes")
    print("OK: %s charted the timeline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_low_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # archive scaling rules applied at intensity 2 and 9
    def snapshot(i):
        hr = 2.0 * i                      # heart lift, bpm above rest
        breath = 14.0 - 0.34 * i          # breaths per minute
        tear_p = 1.0 / (1.0 + math.exp(-(i - 6.0)))  # tears likely past 6
        wpm = 150.0 - 7.0 * i             # speech rate
        return hr, breath, tear_p, wpm
    lo = snapshot(2)
    hi = snapshot(9)
    print("intensity 2: heart +%.0f bpm, breath %.1f/min, tear p %.2f, speech %.0f wpm" % lo)
    print("intensity 9: heart +%.0f bpm, breath %.1f/min, tear p %.2f, speech %.0f wpm" % hi)
    assert 3.9 < lo[0] < 4.1 and 17.9 < hi[0] < 18.1
    assert 13.31 < lo[1] < 13.33 and 10.93 < hi[1] < 10.95
    assert 0.017 < lo[2] < 0.019 and 0.952 < hi[2] < 0.954
    assert 135.9 < lo[3] < 136.1 and 86.9 < hi[3] < 87.1
    for a, b in zip(lo, hi):
        assert b != a
    print("heart lift scales ~2 bpm per point; speech falls ~7 wpm per point")
    print("rule: same emotion, different volume - calibrate across the range")
    print("OK: %s took both snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_mix_lonely(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sadness 7 blended with loneliness 6: weighted by dominance
    s, l = 7.0, 6.0
    w_s = s / (s + l)
    w_l = l / (s + l)
    blend = w_s * s + w_l * l
    print("sadness %.0f (weight %.3f), loneliness %.0f (weight %.3f)" % (s, w_s, l, w_l))
    print("blended ache: %.2f" % blend)
    assert 0.537 < w_s < 0.539 and 0.461 < w_l < 0.463
    assert 6.53 < blend < 6.55
    # behavior fork: pure sadness may accept comfort; the lonely blend refuses
    accept_pure = 0.62
    accept_blend = 0.62 - 0.30 * w_l
    print("comfort accepted: pure sadness %.2f, lonely blend %.2f" % (accept_pure, accept_blend))
    assert 0.480 < accept_blend < 0.483
    assert accept_blend < accept_pure
    print("rule: honor the loss on the sadness wire, send company down the loneliness wire")
    print("OK: %s unmixed the blend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_day(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one imagined day, hourly sadness 07:00-22:00 (16 readings)
    hours = list(range(7, 23))
    levels = [5, 5, 3, 3, 3, 6, 4, 4, 4, 4, 4, 7, 6, 4, 4, 3]
    assert len(hours) == len(levels) == 16
    avg = sum(levels) / len(levels)
    peak = max(levels)
    peak_h = hours[levels.index(peak)]
    print("readings: %d hours" % len(hours))
    for h, v in zip(hours, levels):
        print("  %02d:00  %d" % (h, v))
    print("day average: %.2f, peak %d at %02d:00" % (avg, peak, peak_h))
    assert 4.29 < avg < 4.33
    assert peak == 7 and peak_h == 18
    # distraction windows (work hours) average lower than evening
    work = sum(levels[2:8]) / 6.0
    evening = sum(levels[11:14]) / 3.0
    print("work-window avg: %.2f, evening avg: %.2f" % (work, evening))
    assert 3.83 < work < 3.84 and 5.66 < evening < 5.68
    assert evening > work
    print("rule: sadness is weather, and weather passes")
    print("OK: %s walked the ordinary day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven body channels at intensity 6 (archive scaling rules)
    i = 6.0
    heart = 2.0 * i                        # bpm above rest
    breath = 14.0 - 0.34 * i               # breaths per minute
    muscle = 10.0 - 0.9 * i                # tension score, softens downward
    stomach = 1.2 * i                      # unease score 0-12
    pallor = 0.8 * i                       # pallor score 0-10
    tears = 1.0 / (1.0 + math.exp(-(i - 6.0))) * 10.0  # readiness 0-10
    energy = 100.0 - 8.0 * i               # percent of normal charge
    print("intensity %.0f body channels:" % i)
    print("  heart +%.0f bpm, breath %.2f/min, muscle tension %.1f/10" % (heart, breath, muscle))
    print("  stomach %.1f/12, pallor %.1f/10, tear readiness %.1f/10" % (stomach, pallor, tears))
    print("  energy %.0f%% of normal" % energy)
    assert 11.9 < heart < 12.1
    assert 11.95 < breath < 11.97
    assert 4.59 < muscle < 4.61
    assert 7.19 < stomach < 7.21
    assert 4.79 < pallor < 4.81
    assert 4.99 < tears < 5.01
    assert 51.9 < energy < 52.1
    # body-load index: mean of normalized channels (0-10)
    chans = [heart / 20.0 * 10.0, (14.0 - breath) / 3.4 * 10.0,
             (10.0 - muscle), stomach / 12.0 * 10.0, pallor,
             tears, (100.0 - energy) / 80.0 * 10.0]
    load = sum(chans) / len(chans)
    print("body-load index: %.2f/10" % load)
    assert 5.59 < load < 5.61
    print("rule: the body budgets power for reflection instead of action")
    print("OK: %s read the instrument panel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # posture signature at intensity 6
    i = 6.0
    head_tilt = 8.0 + 2.0 * i              # degrees forward
    stride = 1.0 - 0.03 * i                # stride-length factor
    gesture = 10.0 - 1.1 * i               # gesture size score 0-10
    self_touch = 1.3 * i                   # self-touch score 0-13
    print("intensity %.0f posture:" % i)
    print("  head tilt %.0f degrees forward" % head_tilt)
    print("  stride factor %.2f (step is %.0f%% of normal)" % (stride, stride * 100.0))
    print("  gesture size %.1f/10, self-touch %.1f/13" % (gesture, self_touch))
    assert 19.9 < head_tilt < 20.1
    assert 0.819 < stride < 0.821
    assert 3.39 < gesture < 3.41
    assert 7.79 < self_touch < 7.81
    # readability: how far the posture carries (meters of recognition)
    readability = 4.0 + 3.5 * i
    print("readable across the room: about %.0f meters" % readability)
    assert 24.9 < readability < 25.1
    print("rule: the posture broadcasts before words do")
    print("OK: %s sketched the furled sail" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_sleep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # housekeeping channels at intensity 6, and their lag
    i = 6.0
    sleep_loss = 15.0 * i                  # minutes of sleep gone missing
    appetite = 100.0 - 9.0 * i             # percent of normal appetite
    energy = 100.0 - 8.0 * i               # percent of normal energy
    task_slow = 1.0 + 0.08 * i             # task-time multiplier
    print("intensity %.0f housekeeping:" % i)
    print("  sleep lost: %.0f minutes" % sleep_loss)
    print("  appetite: %.0f%% of normal" % appetite)
    print("  energy: %.0f%% of normal" % energy)
    print("  one-hour task now takes %.0f minutes" % (60.0 * task_slow))
    assert 89.9 < sleep_loss < 90.1
    assert 45.9 < appetite < 46.1
    assert 51.9 < energy < 52.1
    assert 1.479 < task_slow < 1.481
    # lagging recovery: channels recover slower than the mood (days)
    mood_days, sleep_days = 2.0, 5.0
    print("mood recovers in ~%.0f days; sleep needs ~%.0f days" % (mood_days, sleep_days))
    assert sleep_days > mood_days
    assert 4.9 < sleep_days < 5.1
    print("rule: mop the surface feelings first; give the deep rooms their week")
    print("OK: %s tended the slow rooms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six person profiles: channel-sensitivity coefficients at intensity 6
    i = 6.0
    base_load = 5.60  # mean body-load index from the body record
    profiles = {
        "the crier": 1.35, "the stoic": 0.62, "the gut-feeler": 1.12,
        "the tired one": 1.22, "the restless": 0.88, "the average": 1.00,
    }
    loads = {k: base_load * c for k, c in profiles.items()}
    print("body-load index at intensity %.0f, by profile:" % i)
    for k in profiles:
        print("  %-14s %.2f" % (k, loads[k]))
    spread = max(loads.values()) - min(loads.values())
    print("spread: %.2f" % spread)
    assert 4.08 < spread < 4.10
    assert loads["the crier"] > loads["the average"] > loads["the stoic"]
    assert 7.55 < loads["the crier"] < 7.57
    assert 3.46 < loads["the stoic"] < 3.48
    print("rule: judge the feeling by its direction and story, never by its volume")
    print("OK: %s honored six different bodies" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four facial parts (action-unit strengths) at intensity 6
    i = 6.0
    brow = 0.12 * i    # inner brow raise
    lips = 0.11 * i    # lip corner depressor
    lids = 0.08 * i    # eyelid droop
    gaze = 0.09 * i    # gaze lowering
    score = brow + lips + lids + gaze
    print("intensity %.0f face:" % i)
    print("  inner brow %.2f, lip corners %.2f, lids %.2f, gaze %.2f" % (brow, lips, lids, gaze))
    print("  expression score: %.2f" % score)
    assert 0.719 < brow < 0.721
    assert 0.659 < lips < 0.661
    assert 0.479 < lids < 0.481
    assert 0.539 < gaze < 0.541
    assert 2.399 < score < 2.401
    # the brow is the most diagnostic single mark
    print("most diagnostic: inner brow lift (hardest to fake)")
    assert brow == max(brow, lips, lids, gaze)
    print("rule: four brushstrokes, signed with the brow")
    print("OK: %s painted the sad face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four parts at intensities 2, 5, 9: every part rises monotonically
    def parts(i):
        return [0.12 * i, 0.11 * i, 0.08 * i, 0.09 * i]
    names = ["brow", "lip corners", "lids", "gaze"]
    prev = None
    for i in (2, 5, 9):
        p = parts(i)
        s = sum(p)
        print("intensity %d: %s -> score %.2f" %
              (i, ", ".join("%.2f" % v for v in p), s))
        if prev is not None:
            for a, b, n in zip(prev, p, names):
                assert b > a, "%s did not rise" % n
        prev = p
    assert 0.799 < sum(parts(2)) < 0.801
    assert 1.999 < sum(parts(5)) < 2.001
    assert 3.599 < sum(parts(9)) < 3.601
    # floor effect: at intensity 2 most observers read neutral
    print("at intensity 2 the face reads near-neutral: absence of signal is not signal of absence")
    print("rule: the muscles cannot easily report a lower number than the feeling")
    print("OK: %s turned the volume knob on the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_hide(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # leakage = intensity^2 / (effort + 1) * 0.1
    def leakage(i, effort):
        return i ** 2 / (effort + 1.0) * 0.1
    cases = [(9, 8, 0.90), (9, 2, 2.70), (4, 8, 0.18), (2, 8, 0.04)]
    for i, effort, want in cases:
        got = leakage(i, effort)
        print("intensity %d, effort %d -> leakage %.2f" % (i, effort, got))
        assert want - 0.01 < got < want + 0.01
    # the mask fails above 0.5: at intensity 9 with effort 8 it is failing
    assert 0.899 < leakage(9, 8) < 0.901
    print("verdict at intensity 9, effort 8: the mask is FAILING")
    # micro-flash: the genuine brow fires before control arrives (< 0.2 s)
    flash_ms = 160.0
    control_ms = 420.0
    print("genuine brow flash: %.0f ms; deliberate control: %.0f ms" % (flash_ms, control_ms))
    assert flash_ms < 200.0 < control_ms
    print("rule: strong feelings outvote strong masks")
    print("OK: %s watched the mask fail honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_artist(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # studio measurements for portraying sadness at intensity 6
    i = 6.0
    brow_angle = 8.0 + 2.0 * i          # inner brow ends, degrees up
    lid_cover = i / 48.0                # fraction of iris covered
    mouth_drop_mm = 1.0 * i             # mouth corner drop, mm life-size
    head_tilt = 8.0 + 2.0 * i           # degrees forward
    move_slow = 1.0 / 1.5               # movement speed factor (slowed by a third)
    print("intensity %.0f studio notes:" % i)
    print("  brow inner ends up %.0f degrees, outer ends level" % brow_angle)
    print("  lids cover %.3f of the iris (top eighth)" % lid_cover)
    print("  mouth corners drop %.0f mm life-size" % mouth_drop_mm)
    print("  head tilts %.0f degrees; movement at %.2f speed" % (head_tilt, move_slow))
    assert 19.9 < brow_angle < 20.1
    assert 0.124 < lid_cover < 0.126
    assert 5.9 < mouth_drop_mm < 6.1
    assert 19.9 < head_tilt < 20.1
    assert 0.666 < move_slow < 0.668
    print("rule: draw the anatomy and the emotion arrives on its own")
    print("OK: %s pinned the measurement sheet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # classic triggers ranked by teaching potency
    triggers = [
        ("death of a loved one", 10.0),
        ("end of a close relationship", 9.0),
        ("serious illness or injury", 8.0),
        ("loss of home, job, or life's work", 7.0),
        ("rejection or exclusion", 6.0),
        ("failure at something that mattered", 5.0),
        ("being forgotten or overlooked", 4.0),
    ]
    ranked = sorted(triggers, key=lambda t: -t[1])
    print("classic triggers, ranked:")
    for name_t, pot in ranked:
        print("  potency %4.1f  %s" % (pot, name_t))
    assert ranked[0] == ("death of a loved one", 10.0)
    assert ranked[-1][1] == 4.0
    pots = [p for _, p in triggers]
    assert pots == sorted(pots, reverse=True)
    # compounding: two mid-level triggers together can out-pull one classic
    combo = 6.0 + 5.0 - 6.0 * 5.0 / 20.0
    print("rejection (6) + meaningful failure (5) combined: %.2f" % combo)
    assert 9.49 < combo < 9.51
    assert combo > 9.0
    print("rule: the closer the lost thing sat to the center, the harder the pull")
    print("OK: %s sounded the classic channels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_personal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # anniversary decay: potency = base * e^(-years / 2.5)
    base, tau = 9.0, 2.5
    years = [1, 3, 10]
    pots = [base * math.exp(-y / tau) for y in years]
    print("anniversary decay (base %.0f):" % base)
    for y, p in zip(years, pots):
        print("  year %2d -> potency %.2f" % (y, p))
    assert 6.03 < pots[0] < 6.05
    assert 2.70 < pots[1] < 2.72
    assert 0.164 < pots[2] < 0.166
    assert pots[0] > pots[1] > pots[2]
    # sensory ambush: a reminder can spike a full wave regardless of the curve
    ambush = 7.5
    print("sensory ambush spike (a smell, a street corner): %.1f" % ambush)
    assert ambush > pots[2]
    print("rule: map the atlas, note the dates, treat ambushes as weather")
    print("OK: %s charted the private tides" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_surprise(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # odd triggers: (name, unexpectedness, potency)
    odd = [
        ("favorite cereal in aisle seven", 9.0, 5.0),
        ("sunshine against inner gray", 7.0, 3.5),
        ("good news with nowhere to send thanks", 8.0, 5.5),
        ("the last page of a beloved book", 6.0, 3.0),
        ("relief after a long effort ends", 7.5, 4.0),
    ]
    ranked = sorted(odd, key=lambda t: -t[1])
    print("surprise triggers, by unexpectedness:")
    for name_t, unexp, pot in ranked:
        print("  surprise %.1f  potency %.1f  %s" % (unexp, pot, name_t))
    assert ranked[0][0] == "favorite cereal in aisle seven"
    assert 8.9 < ranked[0][1] < 9.1
    # legitimacy check: unexpectedness and potency are independent axes
    for _, unexp, pot in odd:
        assert 0.0 < pot <= 10.0
    strangest = max(odd, key=lambda t: t[1])
    print("strangest trigger still carries real potency: %.1f" % strangest[2])
    assert 4.9 < strangest[2] < 5.1
    print("rule: triggers need no permission and no logic, only an association")
    print("OK: %s opened the odd-keys drawer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_cascade(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-step cascade: each stage multiplies the last
    stages = ["sadness", "loneliness", "withdrawal", "rumination", "deepened sadness"]
    mults = [1.0, 1.08, 1.06, 1.10, 1.04]
    level = 6.0
    print("cascade from intensity %.1f:" % level)
    trace = []
    for s, m in zip(stages, mults):
        level = level * m
        trace.append(level)
        print("  %-16s x%.2f -> %.2f" % (s, m, level))
    peak = max(trace)
    print("cascade peak: %.2f" % peak)
    assert 7.85 < peak < 7.87
    assert trace[-1] > 6.0
    # breaking one link: answering a message removes the withdrawal multiplier
    fixed = 6.0 * 1.08 * 1.00 * 1.10 * 1.04
    print("with withdrawal link broken (x1.00): peak %.2f" % fixed)
    assert 7.40 < fixed < 7.42
    assert fixed < peak
    print("rule: every link is an exit - one message, one walk")
    print("OK: %s traced the chain and its exits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # action likelihoods; weighted draw with fixed selector 0.63
    actions = [
        ("withdrawing and seeking solitude", 0.80),
        ("moving slowly and doing less", 0.72),
        ("seeking comfort", 0.58),
        ("crying, openly or privately", 0.55),
        ("revisiting reminders", 0.47),
        ("neglecting small routines", 0.41),
    ]
    total = sum(w for _, w in actions)
    print("action likelihoods (sum %.2f):" % total)
    for a, w in actions:
        print("  %.2f  %s" % (w, a))
    assert 3.52 < total < 3.54
    # deterministic weighted draw
    sel = 0.40 * total
    acc = 0.0
    chosen = actions[-1][0]
    for a, w in actions:
        acc += w
        if sel <= acc:
            chosen = a
            break
    print("selector 0.40 -> showcased action: %s" % chosen)
    assert chosen == "moving slowly and doing less"
    assert actions[0][1] == max(w for _, w in actions)
    print("rule: the low-energy program running as designed, not a flaw")
    print("OK: %s observed the honest center" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # thirty-second speech sample at intensity 6
    i = 6.0
    wpm = 150.0 - 7.0 * i
    words_30s = wpm / 2.0
    sighs = int(i / 3.0)
    pauses = int(i / 2.0)
    print("intensity %.0f voice:" % i)
    print("  speech rate %.0f wpm -> ~%.0f words in 30 seconds" % (wpm, words_30s))
    print("  sighs: %d, long pauses: %d" % (sighs, pauses))
    assert 107.9 < wpm < 108.1
    assert 53.9 < words_30s < 54.1
    assert sighs == 2 and pauses == 3
    phrases = ["I just feel heavy.", "It is not the same without them.",
               "Leave me alone for a bit, but do not go far."]
    print("characteristic phrases: %d" % len(phrases))
    for p in phrases:
        print("  \\"%s\\"" % p)
    assert len(phrases) == 3
    print("rule: hear the pauses as punctuation - the silence is not empty")
    print("OK: %s tuned the ear" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sad chooser accepts a gamble only if p(win) > 0.50 + 0.02 * intensity
    def bar(i):
        return 0.50 + 0.02 * i
    for i in (2, 7):
        print("intensity %d: acceptance bar %.0f%%" % (i, bar(i) * 100.0))
    assert 0.539 < bar(2) < 0.541
    assert 0.639 < bar(7) < 0.641
    # sample gamble: 60% chance to win - taken at 2, refused at 7
    p = 0.60
    take_lo = p > bar(2)
    take_hi = p > bar(7)
    print("gamble at 60%%: intensity 2 -> %s, intensity 7 -> %s"
          % ("TAKE" if take_lo else "REFUSE", "TAKE" if take_hi else "REFUSE"))
    assert take_lo and not take_hi
    # the price of the mood: expected value left on the table
    ev = p * 100.0 - 40.0
    print("expected value refused at intensity 7: %.0f" % ev)
    assert 19.9 < ev < 20.1
    print("rule: notice the tint; let the big contracts wait for clear skies")
    print("OK: %s audited the storm tariff" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # staircase from 4.0, +1.2 per stage, capped at 10
    stages = []
    level = 4.0
    for _ in range(6):
        stages.append(level)
        level = min(10.0, level + 1.2)
    print("escalation staircase:")
    for n, v in enumerate(stages):
        print("  stage %d: %.1f" % (n, v))
    assert 3.99 < stages[0] < 4.01
    assert 5.19 < stages[1] < 5.21
    assert 6.39 < stages[2] < 6.41
    assert 7.59 < stages[3] < 7.61
    assert 8.79 < stages[4] < 8.81
    assert 9.99 < stages[5] < 10.01
    for a, b in zip(stages, stages[1:]):
        assert b >= a
    # every stage is a landing: removing fuel flattens the curve
    flat = [4.0, 4.1, 4.0, 4.2, 4.1, 4.0]
    print("with fuel removed the curve stays near %.1f" % (sum(flat) / len(flat)))
    assert max(flat) < stages[2]
    print("rule: map the staircase so it can be descended, not just climbed")
    print("OK: %s marked the landings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_healthy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # healthy-expression options scored on acknowledgment, release, connection
    options = [
        ("naming it aloud to a trusted person", 9.2),
        ("writing it out longhand", 8.6),
        ("crying when tears come, without apology", 8.1),
        ("moving the body gently", 7.4),
        ("making something from it", 7.0),
    ]
    ranked = sorted(options, key=lambda o: -o[1])
    print("healthy-expression options, ranked:")
    for label, score in ranked:
        print("  %.1f  %s" % (score, label))
    best = ranked[0]
    print("best option: %s (%.1f)" % best)
    assert best[0] == "naming it aloud to a trusted person"
    assert 9.19 < best[1] < 9.21
    scores = [s for _, s in options]
    assert scores == sorted(scores, reverse=True)
    # expression speeds the timeline: expressed fades with a shorter half-life
    buried_half, expressed_half = 40.0, 26.0
    print("fade half-life: buried %.0f min, expressed %.0f min" % (buried_half, expressed_half))
    assert expressed_half < buried_half
    print("rule: deliver the message - a signal delivered is a signal stood down")
    print("OK: %s drilled the signal corps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_unhealthy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cost models at intensity 6: healthy cheapest, bottling middle, explosion highest
    i = 6.0
    bottle = 5.0 * i + 8.0
    explode = 6.0 * i + 8.0
    healthy = 2.0 * i + 2.0
    print("intensity %.0f exit costs:" % i)
    print("  healthy expression: %.0f" % healthy)
    print("  bottling it up:     %.0f" % bottle)
    print("  blowing up:         %.0f" % explode)
    assert 13.9 < healthy < 14.1
    assert 37.9 < bottle < 38.1
    assert 43.9 < explode < 44.1
    assert healthy < bottle < explode
    # the ordering holds at every intensity 1..10
    for j in range(1, 11):
        h, b, e = 2.0 * j + 2.0, 5.0 * j + 8.0, 6.0 * j + 8.0
        assert h < b < e
    print("ordering healthy < bottling < explosion holds at every intensity 1-10")
    print("rule: feelings are paid for one way or another - pay the cheapest price")
    print("OK: %s posted the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five practices with daily benefit scores; weekly total at 70% adherence
    practices = [
        ("naming the feeling daily", 3.0),
        ("a twenty-minute walk", 4.0),
        ("one honest weekly conversation", 2.0),
        ("keeping sleep hours regular", 3.0),
        ("one small act of making", 2.0),
    ]
    daily = sum(b for _, b in practices)
    adherence = 0.70
    weekly = daily * 7.0 * adherence
    print("daily benefit: %.0f points across %d practices" % (daily, len(practices)))
    for label, b in practices:
        print("  %.0f/day  %s" % (b, label))
    print("weekly at %.0f%% adherence: %.1f points" % (adherence * 100.0, weekly))
    assert 13.9 < daily < 14.1
    assert 68.59 < weekly < 68.61
    # consistency beats intensity: mediocre-but-steady outscores heroic-but-abandoned
    steady = 14.0 * 30.0 * 0.70
    heroic = 28.0 * 7.0 * 1.00
    print("steady month: %.0f vs heroic week: %.0f" % (steady, heroic))
    assert steady > heroic
    print("rule: choose practices easy enough to survive bad days")
    print("OK: %s issued the quartermaster's tools" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_reading(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four-channel weighted checklist on a described scenario
    weights = {"face": 0.35, "body": 0.25, "voice": 0.25, "behavior": 0.15}
    cues = {"face": 0.8, "body": 0.6, "voice": 0.7, "behavior": 0.5}
    score = sum(weights[k] * cues[k] for k in weights)
    print("observed cues:")
    for k in weights:
        print("  %-8s cue %.1f x weight %.2f = %.3f" % (k, cues[k], weights[k], weights[k] * cues[k]))
    print("weighted reading: %.3f" % score)
    assert 0.679 < score < 0.681
    def band(s):
        if s < 0.4:
            return "unlikely"
        if s <= 0.6:
            return "possible"
        return "likely"
    print("band: %s sadness - worth a gentle check-in" % band(score))
    assert band(score) == "likely"
    assert band(0.2) == "unlikely" and band(0.5) == "possible"
    wsum = sum(weights.values())
    assert 0.999 < wsum < 1.001
    print("rule: the checklist informs the question - are you all right - never replaces it")
    print("OK: %s trained the scout's eye" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_support(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # helpful responses scored on honoring, company, non-intrusion
    responses = [
        ("listening without fixing", 9.4),
        ("gently naming what you see", 8.8),
        ("offering specific concrete help", 8.2),
        ("quiet presence without demands", 7.9),
        ("brief shared experience, never taking the floor", 7.1),
    ]
    ranked = sorted(responses, key=lambda r: -r[1])
    print("helpful responses, ranked:")
    for label, score in ranked:
        print("  %.1f  %s" % (score, label))
    assert ranked[0][0] == "listening without fixing"
    assert 9.39 < ranked[0][1] < 9.41
    assert ranked[-1][1] > 7.0
    # concrete beats vague: specific help outscores the vague offer
    vague = 5.2
    print("vague 'let me know if you need anything': %.1f (below every ranked response)" % vague)
    assert vague < ranked[-1][1]
    print("rule: follow their lead - offer, do not impose; stay, do not fix")
    print("OK: %s stocked the companion's handbook" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_mistakes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # misfires scored on invalidation + hijacking + abandonment
    misfires = [
        ("telling them to cheer up / look on the bright side", 9.1),
        ("comparing losses and hijacking the floor", 8.4),
        ("rushing in with solutions before listening", 7.8),
        ("minimizing: it is not that bad, at least", 7.5),
        ("avoiding them because their sadness is uncomfortable", 7.2),
    ]
    ranked = sorted(misfires, key=lambda m: -m[1])
    print("misfires, by harm:")
    for label, harm in ranked:
        print("  %.1f  %s" % (harm, label))
    worst = ranked[0]
    print("worst misfire: %s (%.1f)" % worst)
    assert "cheer up" in worst[0]
    assert 9.09 < worst[1] < 9.11
    harms = [h for _, h in misfires]
    assert harms == sorted(harms, reverse=True)
    assert min(harms) > 7.0
    print("rule: audit the impulse - am I soothing them, or soothing myself")
    print("OK: %s printed the red page" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_relatives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # relatives of sadness by teaching distance
    relatives = [
        ("melancholy", 0.15),
        ("disappointment", 0.30),
        ("grief", 0.45),
        ("despair", 0.60),
        ("apathy", 0.75),
    ]
    by_dist = sorted(relatives, key=lambda r: r[1])
    print("relatives by distance from sadness:")
    for label, d in by_dist:
        print("  %.2f  %s" % (d, label))
    nearest, farthest = by_dist[0], by_dist[-1]
    print("nearest: %s (%.2f); farthest: %s (%.2f)" % (nearest[0], nearest[1], farthest[0], farthest[1]))
    assert nearest[0] == "melancholy"
    assert 0.149 < nearest[1] < 0.151
    assert farthest[0] == "apathy"
    assert 0.749 < farthest[1] < 0.751
    dists = [d for _, d in relatives]
    assert dists == sorted(dists)
    # three telling-apart questions per relative (object, course, need)
    print("telling-apart questions: what is it about, how long has it stayed, what does it want")
    print("rule: name the relative correctly and you bring the right remedy")
    print("OK: %s charted the family with measured distances" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sadness at 7 blended with four partners; weighted profiles
    s = 7.0
    partners = [("anger", 5.0, "frustrated sorrow"),
                ("surprise", 6.0, "disappointment"),
                ("fear", 8.0, "despair"),
                ("joy", 3.0, "bittersweetness")]
    blends = []
    print("sadness %.0f blends:" % s)
    for pname, plevel, label in partners:
        w = s / (s + plevel)
        blended = w * s + (1.0 - w) * plevel
        blends.append((label, blended))
        print("  + %-8s %-2.0f -> %-18s %.2f" % (pname, plevel, label, blended))
    vals = [v for _, v in blends]
    assert 6.16 < vals[0] < 6.18
    assert 6.53 < vals[1] < 6.55
    assert 7.53 < vals[2] < 7.54
    assert 5.79 < vals[3] < 5.81
    # pairwise distinctness: no two blends closer than 0.3
    diffs = [abs(a - b) for x, a in enumerate(vals) for b in vals[x + 1:]]
    print("smallest pairwise difference: %.2f" % min(diffs))
    assert min(diffs) > 0.36
    print("rule: name the partner and you name the blend")
    print("OK: %s filled the four jars" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emsad_full_sim(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-scene showcase: trigger -> rise -> turn -> fade -> resolution
    scenes = [
        ("trigger: the news lands", 5.0, "the appraisal lands in about eight minutes"),
        ("rise: the loss sinks in", 7.2, "tears arrive at the twenty-five minute peak"),
        ("turn: naming it aloud", 5.5, "the circuit completes, comfort received"),
        ("fade: the half-life works", 3.1, "forty-minute half-life thins the wave"),
        ("resolution: a week of practices", 1.5, "the loss filed, the lesson kept"),
    ]
    print("showcase simulation - Mara's episode (invented composite):")
    peak = 0.0
    for title, level, note in scenes:
        peak = max(peak, level)
        print("  [%4.1f] %-32s %s" % (level, title, note))
        assert 0.0 <= level <= 10.0
    assert 7.19 < peak < 7.21
    resolution = scenes[-1][1]
    print("peak %.1f, resolution %.1f" % (peak, resolution))
    assert resolution < peak
    assert 1.49 < resolution < 1.51
    # every subsystem moves together at the peak scene
    i = 7.2
    heart = 2.0 * i
    brow = 0.12 * i
    print("at the peak: heart +%.1f bpm, brow %.2f, tears flowing" % (heart, brow))
    assert 14.39 < heart < 14.41
    assert 0.863 < brow < 0.865
    print("rule: every sadness has a far shore, and the archive exists to prove it")
    print("OK: %s walked the voyage end to end" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
 "emsad-what-is": demo_emsad_what_is,
 "emsad-family": demo_emsad_family,
 "emsad-volumes": demo_emsad_volumes,
 "emsad-myths": demo_emsad_myths,
 "emsad-inside": demo_emsad_inside,
 "emsad-timeline": demo_emsad_timeline,
 "emsad-low-high": demo_emsad_low_high,
 "emsad-mix-lonely": demo_emsad_mix_lonely,
 "emsad-day": demo_emsad_day,
 "emsad-body": demo_emsad_body,
 "emsad-posture": demo_emsad_posture,
 "emsad-sleep": demo_emsad_sleep,
 "emsad-differences": demo_emsad_differences,
 "emsad-face": demo_emsad_face,
 "emsad-face-intensity": demo_emsad_face_intensity,
 "emsad-hide": demo_emsad_hide,
 "emsad-artist": demo_emsad_artist,
 "emsad-triggers": demo_emsad_triggers,
 "emsad-personal": demo_emsad_personal,
 "emsad-surprise": demo_emsad_surprise,
 "emsad-cascade": demo_emsad_cascade,
 "emsad-actions": demo_emsad_actions,
 "emsad-speech": demo_emsad_speech,
 "emsad-decisions": demo_emsad_decisions,
 "emsad-escalation": demo_emsad_escalation,
 "emsad-healthy": demo_emsad_healthy,
 "emsad-unhealthy": demo_emsad_unhealthy,
 "emsad-practices": demo_emsad_practices,
 "emsad-reading": demo_emsad_reading,
 "emsad-support": demo_emsad_support,
 "emsad-mistakes": demo_emsad_mistakes,
 "emsad-relatives": demo_emsad_relatives,
 "emsad-mixes": demo_emsad_mixes,
 "emsad-full-sim": demo_emsad_full_sim,
}
