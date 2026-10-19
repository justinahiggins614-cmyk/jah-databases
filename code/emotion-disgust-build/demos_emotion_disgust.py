#!/usr/bin/env python3
"""Demo programs for the Disgust Emotion databases (Manon's 2026-10-17 16:15
emotion-series order, batch 1).

Every demo is real, runnable, stdlib-only Python performing the actual
emotion-scenario simulation for its record: scenario simulators, mix
blenders, recognition trainers, and intensity/arc models. All are
machine-executed by build.py before commit: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker. Descriptive/educational only - no diagnosing real people.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the nine classic trigger domains and their representative weights
    domains = {"food": 22.0, "animals": 12.0, "body products": 11.0,
               "body envelope violations": 9.0, "death and decay": 8.0,
               "hygiene": 10.0, "interpersonal contact": 8.0,
               "sexual": 7.0, "moral violations": 13.0}
    total = sum(domains.values())
    print("classic trigger domains: %d" % len(domains))
    for k, v in sorted(domains.items(), key=lambda p: -p[1]):
        print("  %-26s %5.1f %%" % (k, v))
    print("domain weights sum: %.1f %%" % total)
    assert 99.9 < total < 100.1
    top = max(domains, key=domains.get)
    print("largest domain: %s" % top)
    assert top == "food"
    assert 21.9 < domains["food"] < 22.1
    print("rule: one rejection circuit, nine sectors - same alarm, nine watch sectors")
    print("OK: %s mapped the nine sectors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # basic emotions and their distance from disgust on the family map
    # distance 0 = itself; larger = further (0-10 scale)
    dist = {"disgust": 0.0, "contempt": 1.5, "anger": 3.0, "fear": 3.5,
            "sadness": 4.0, "shame": 4.5, "joy": 8.5, "trust": 9.0}
    print("neighbors of disgust on the family map:")
    for k in sorted(dist, key=dist.get):
        print("  %-10s distance %.1f" % (k, dist[k]))
    nearest = min([k for k in dist if k != "disgust"], key=dist.get)
    print("nearest neighbor: %s" % nearest)
    assert nearest == "contempt"
    assert 1.4 < dist["contempt"] < 1.6
    # opposite on the map: trust/acceptance
    opp = max(dist, key=dist.get)
    print("opposite pole: %s" % opp)
    assert opp == "trust"
    # blend check: disgust + anger -> outrage sits between them
    outrage = (dist["disgust"] + dist["anger"]) / 2.0
    print("outrage blend midpoint: %.2f" % outrage)
    assert 1.4 < outrage < 1.6
    print("rule: urge plus body equals name, name equals protocol")
    print("OK: %s charted the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the volume knob: level 0-10 -> body systems recruited
    def systems(level):
        n = 0
        if level >= 1: n += 1   # face
        if level >= 4: n += 1   # throat
        if level >= 6: n += 1   # stomach
        if level >= 8: n += 1   # full posture + attention capture
        return n
    print("volume knob: level -> systems recruited")
    for lv in (1, 3, 5, 7, 9):
        print("  level %d -> %d systems" % (lv, systems(lv)))
    assert systems(1) == 1
    assert systems(5) == 2
    assert systems(7) == 3
    assert systems(9) == 4
    # duration of aftermath scales roughly with the square of the level
    def aftermath_hours(level):
        return 0.05 * level * level
    for lv in (2, 5, 9):
        print("  level %d aftermath ~%.2f h" % (lv, aftermath_hours(lv)))
    assert 0.19 < aftermath_hours(2) < 0.21
    assert 1.24 < aftermath_hours(5) < 1.26
    assert 4.04 < aftermath_hours(9) < 4.06
    print("rule: match the response to the level - whispers get adjustments, screams get distance")
    print("OK: %s calibrated the knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six myths, each scored: 0 = believed, 1 = corrected
    myths = ["only about food", "only weak feel it", "reason erases it",
             "always a problem", "same triggers for all", "feeling = judgmental"]
    answers = [1, 1, 1, 0, 1, 1]  # sample run: five corrected, one missed
    score = sum(answers)
    pct = score / len(myths) * 100.0
    print("myth quiz: %d statements" % len(myths))
    for m, a in zip(myths, answers):
        print("  [%s] %s" % ("corrected" if a else "believed ", m))
    print("score: %d/%d (%.1f %%)" % (score, len(myths), pct))
    assert score == 5
    assert 83.3 < pct < 83.4
    missed = [m for m, a in zip(myths, answers) if not a]
    print("still to clear: %s" % missed[0])
    assert missed == ["always a problem"]
    print("rule: the signal is never broken - widen the frame and the myths fall")
    print("OK: %s cleared the fog" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the inside sequence: phase timestamps in seconds from trigger
    seq = [("sensory hit", 0.0), ("face moves on its own", 0.4),
           ("stomach drops", 0.9), ("label arrives: oh no", 1.4),
           ("urge: get it away", 1.8), ("head turns, hand pulls back", 2.3),
           ("words: no. ugh.", 3.0), ("residue replays", 300.0)]
    print("inside the feeling - phase timeline (seconds):")
    prev = -1.0
    for label, t in seq:
        print("  t=%7.1fs  %s" % (t, label))
        assert t > prev, "phases must run forward in time"
        prev = t
    # the label arrives late: gap between body and words
    gap = seq[3][1] - seq[1][1]
    print("body-to-label gap: %.1f s (the face knows first)" % gap)
    assert 0.9 < gap < 1.1
    span = seq[-1][1] - seq[0][1]
    print("full arc span modeled: %.0f s" % span)
    assert 299.9 < span < 300.1
    print("rule: this is the gate log from the watchtower floor - ground truth, not verdict")
    print("OK: %s walked the inside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_arc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arc model: instant rise, plateau while exposed, exponential decay,
    # plus a smaller echo bump from the contamination tag
    def wave(t):
        # t in seconds; exposure ends at t=120
        if t < 2.0:
            return 10.0 * t / 2.0
        if t < 120.0:
            return 10.0
        d = t - 120.0
        base = 10.0 * math.exp(-d / 90.0)
        echo = 2.5 * math.exp(-((d - 600.0) ** 2) / (2 * 120.0 ** 2))
        return base + echo
    print("arc samples (intensity 0-10):")
    for t in (1.0, 2.0, 60.0, 120.0, 210.0, 720.0):
        print("  t=%6.0fs -> %.2f" % (t, wave(t)))
    assert 4.9 < wave(1.0) < 5.1
    assert 9.9 < wave(60.0) < 10.1
    assert 3.67 < wave(210.0) < 3.69   # one time-constant down
    assert 2.4 < wave(720.0) < 2.7     # echo bump region
    # half-life of the decay phase
    half = 90.0 * math.log(2.0)
    print("decay half-life: %.1f s" % half)
    assert 62.3 < half < 62.5
    print("rule: judge the feeling in the fading, not the peak - and plan for echoes")
    print("OK: %s traced the arc" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # signal strengths (0-10) for the two snapshots in the record
    low = {"face": 2.0, "throat": 0.5, "stomach": 0.0, "posture": 1.0,
           "attention": 1.5, "memory_tag": 1.0}
    high = {"face": 9.5, "throat": 8.5, "stomach": 9.0, "posture": 8.0,
            "attention": 9.0, "memory_tag": 8.5}
    print("snapshot comparison (0-10 signal strength):")
    for k in low:
        print("  %-11s low %4.1f   high %4.1f" % (k, low[k], high[k]))
        assert high[k] > low[k]
    tl, th = sum(low.values()), sum(high.values())
    print("total load: low %.1f vs high %.1f (ratio %.1f)" % (tl, th, th / tl))
    assert 5.9 < tl < 6.1
    assert 52.4 < th < 52.6
    assert 8.7 < th / tl < 8.8
    # words available collapse as volume rises
    words = {2: 40, 9: 3}
    print("words available: level 2 -> %d, level 9 -> %d" % (words[2], words[9]))
    assert words[9] < words[2]
    print("rule: two snapshots, one alarm - calibrate, then respond to the level")
    print("OK: %s held both snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mixed_anger(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # blend mixer: disgust + anger, weights sum to 1
    def blend(w_disgust):
        w_anger = 1.0 - w_disgust
        urges = {"distance": 9.0 * w_disgust + 1.0 * w_anger,
                 "confront": 1.0 * w_disgust + 9.0 * w_anger,
                 "nausea": 8.0 * w_disgust + 0.5 * w_anger,
                 "heat": 1.5 * w_disgust + 8.0 * w_anger}
        return urges
    print("blend: 60% disgust / 40% anger (classic outrage):")
    b = blend(0.6)
    for k, v in b.items():
        print("  %-9s %.2f" % (k, v))
    assert 5.7 < b["distance"] < 5.9
    assert 4.1 < b["confront"] < 4.3
    assert 4.9 < b["nausea"] < 5.1
    assert 4.0 < b["heat"] < 4.2
    # pure ends for reference
    pd, pa = blend(1.0), blend(0.0)
    assert 8.9 < pd["distance"] < 9.1 and 0.9 < pd["confront"] < 1.1
    assert 0.9 < pa["distance"] < 1.1 and 8.9 < pa["confront"] < 9.1
    print("naming check: 'disgusted AND angry' keeps both urges honest")
    print("rule: name both ingredients - distance for disgust, words for anger")
    print("OK: %s mixed the weather" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_day_in_life(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six scenes from the record: (time, domain, cost_seconds, resolved)
    scenes = [("07:10", "hygiene", 5, True),
              ("08:40", "interpersonal", 240, True),
              ("12:15", "food", 90, True),
              ("15:30", "moral", 45, True),
              ("18:00", "food", 150, True),
              ("21:20", "visual", 20, True)]
    total_cost = sum(s[2] for s in scenes)
    resolved = sum(1 for s in scenes if s[3])
    print("patrol log - small corrections:")
    for t, d, c, r in scenes:
        print("  %s  %-14s cost %3ds  %s" % (t, d, c, "resolved" if r else "OPEN"))
    print("corrections: %d, all resolved: %s" % (len(scenes), resolved == len(scenes)))
    print("total daily cost: %d s (%.1f min)" % (total_cost, total_cost / 60.0))
    assert len(scenes) == 6
    assert resolved == 6
    assert total_cost == 550
    assert 9.1 < total_cost / 60.0 < 9.2
    domains_hit = len(set(s[1] for s in scenes))
    print("domains served: %d" % domains_hit)
    assert domains_hit == 5
    print("rule: a territory stays clean by a hundred tiny adjustments nobody applauds")
    print("OK: %s walked the patrol" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what-is": demo_what_is,
    "family": demo_family,
    "intensity": demo_intensity,
    "myths": demo_myths,
    "first-person": demo_first_person,
    "arc": demo_arc,
    "low-vs-high": demo_low_vs_high,
    "mixed-anger": demo_mixed_anger,
    "day-in-life": demo_day_in_life,
}


def demo_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # staged rejection program: onset times (s) and peak strengths (0-10)
    stages = [("face narrows", 0.4, 8.5), ("throat tightens", 0.9, 7.5),
              ("stomach churns", 1.6, 9.0), ("heart slows (brake)", 2.5, 6.0),
              ("skin pales/cools", 3.0, 5.5)]
    print("rejection program - stages in order:")
    prev = -1.0
    for label, t, s in stages:
        print("  t=%4.1fs  strength %4.1f  %s" % (t, s, label))
        assert t > prev
        prev = t
    # unusual signature: heart SLOWS under strong disgust (parasympathetic brake)
    hr_rest, hr_disgust = 72.0, 58.0
    drop = hr_rest - hr_disgust
    print("heart rate: rest %.0f -> disgust %.0f (drop %.0f bpm)" % (hr_rest, hr_disgust, drop))
    assert 13.9 < drop < 14.1
    peak = max(stages, key=lambda p: p[2])
    print("strongest stage: %s" % peak[0])
    assert peak[0] == "stomach churns"
    print("rule: the body keeps its own score - the words catch up later")
    print("OK: %s ran the program" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # movement signature: distances in cm, angles in degrees
    lean_back = 14.0        # torso retreat at moderate intensity
    head_turn = 35.0        # degrees away from trigger
    arc_radius = 90.0       # wide berth around a floor trigger
    straight_line = 60.0    # direct path that was avoided
    extra = arc_radius - straight_line
    print("posture measurements:")
    print("  lean-back: %.1f cm" % lean_back)
    print("  head turn: %.0f deg" % head_turn)
    print("  path arc: %.0f cm vs direct %.0f cm (extra %.0f cm)" % (arc_radius, straight_line, extra))
    assert 13.9 < lean_back < 14.1
    assert 34.9 < head_turn < 35.1
    assert 29.9 < extra < 30.1
    # freeze before retreat: half-second assessment
    freeze = 0.5
    retreat_speed = lean_back / 1.2  # cm per second over the retreat
    print("  freeze: %.1f s, retreat speed: %.1f cm/s" % (freeze, retreat_speed))
    assert 11.6 < retreat_speed < 11.7
    print("rule: fear crouches, anger advances, disgust retreats - in refusal, not panic")
    print("OK: %s read the ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # appetite recovery after a strong wave: fraction of normal appetite
    def appetite(t_hours):
        return 1.0 - 0.85 * math.exp(-t_hours / 3.0)
    print("appetite recovery (fraction of normal):")
    for t in (0.0, 3.0, 6.0, 12.0):
        print("  t=%5.1fh -> %.3f" % (t, appetite(t)))
    assert 0.149 < appetite(0.0) < 0.151
    assert 0.686 < appetite(3.0) < 0.688
    assert 0.884 < appetite(6.0) < 0.886
    assert 0.984 < appetite(12.0) < 0.986
    # sleep cost: replay loops before bed
    loops, per_loop_min = 4, 12
    sleep_delay = loops * per_loop_min
    print("bedtime replay: %d loops x %d min = %d min delay" % (loops, per_loop_min, sleep_delay))
    assert sleep_delay == 48
    # energy: heavy drain, not wired - next-day capacity
    capacity = 100.0 - 25.0 * math.exp(-1.0)
    print("next-morning capacity after a big wave: %.1f %%" % capacity)
    assert 90.7 < capacity < 90.9
    print("rule: do not rush recovery - forcing a meal adds a second problem to the first")
    print("OK: %s honored the schedule" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bodies_differ(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # synthetic sensitivity distribution (disgust-scale style, 0-100)
    sample = [18, 25, 31, 34, 38, 42, 45, 47, 49, 52, 55, 57, 60, 63,
              66, 69, 72, 75, 78, 82, 88, 94]
    n = len(sample)
    mean = sum(sample) / n
    var = sum((x - mean) ** 2 for x in sample) / n
    sd = math.sqrt(var)
    print("sensitivity sample: n=%d" % n)
    print("  mean %.2f, sd %.2f, range %d-%d" % (mean, sd, min(sample), max(sample)))
    assert 56.35 < mean < 56.38
    assert 19.9 < sd < 20.1
    assert min(sample) == 18 and max(sample) == 94
    # spread check: widest in emotion psychology
    spread = max(sample) - min(sample)
    print("  spread: %d points - one of the widest in emotion psychology" % spread)
    assert spread == 76
    # channels: share of people per dominant channel
    channels = {"stomach-first": 46.0, "throat-first": 31.0, "skin-first": 23.0}
    ctot = sum(channels.values())
    print("dominant channels: %s (sum %.0f %%)" % (channels, ctot))
    assert 99.9 < ctot < 100.1
    print("rule: never judge another alarm by your own dial")
    print("OK: %s measured the dials" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # facial action unit intensities (0-5) for the canonical disgust face
    au = {"AU9 nose wrinkle": 4.5, "AU10 upper lip raise": 4.0,
          "AU25 lips part": 2.5, "AU26 jaw drop": 2.0,
          "AU4 brow lower": 3.0, "AU7 lid tighten": 2.5}
    print("disgust face - action unit intensities (0-5):")
    for k in sorted(au, key=au.get, reverse=True):
        print("  %-20s %.1f" % (k, au[k]))
    top2 = sorted(au, key=au.get, reverse=True)[:2]
    print("dominant pair: %s" % top2)
    assert top2 == ["AU9 nose wrinkle", "AU10 upper lip raise"]
    # symmetry check: bilateral (disgust) vs unilateral (contempt)
    left, right = 4.4, 4.6
    asym = abs(left - right)
    print("bilateral symmetry: L=%.1f R=%.1f asymmetry %.1f" % (left, right, asym))
    assert 0.19 < asym < 0.21
    assert asym < 1.0, "true disgust stays near-symmetric"
    print("rule: the gates closing, the exits opening - readable on any face on earth")
    print("OK: %s mapped the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # AU9+AU10 combined intensity across the slider (0-10 alarm level)
    def face_level(alarm):
        return min(5.0, 0.55 * alarm)
    print("slider: alarm level -> face intensity (0-5):")
    prev = -1.0
    for a in (1, 3, 5, 7, 9, 10):
        f = face_level(a)
        print("  alarm %2d -> face %.2f" % (a, f))
        assert f > prev  # monotonic
        prev = f
    assert 0.54 < face_level(1) < 0.56
    assert 2.74 < face_level(5) < 2.76
    assert 4.94 < face_level(9) < 4.96
    # voluntary control fails at the top: suppression success %
    def suppress_ok(alarm):
        return max(0.0, 100.0 - 11.0 * alarm)
    print("suppression success: alarm 3 -> %.0f %%, alarm 9 -> %.0f %%" %
          (suppress_ok(3), suppress_ok(9)))
    assert 66.9 < suppress_ok(3) < 67.1
    assert 0.9 < suppress_ok(9) < 1.1
    print("rule: the nose tells the truth - the upper face is harder to fake than the mouth")
    print("OK: %s ran the slider" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hide_fake(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # leakage probabilities per channel when SUPPRESSING real disgust
    leak = {"nose wrinkle": 0.72, "hard swallow": 0.58, "lean-back": 0.81,
            "distancing hands": 0.64, "voice tightening": 0.49}
    print("suppression leaks (probability the channel betrays):")
    for k in sorted(leak, key=leak.get, reverse=True):
        print("  %-17s %.2f" % (k, leak[k]))
    worst = max(leak, key=leak.get)
    print("hardest to hide: %s" % worst)
    assert worst == "lean-back"
    assert 0.80 < leak["lean-back"] < 0.82
    # faking tells: timing/symmetry errors when PERFORMING disgust
    fake = {"holds too long": 0.77, "asymmetric lip-curl": 0.68,
            "late ugh": 0.61}
    print("faking tells (probability the performance overshoots):")
    for k in sorted(fake, key=fake.get, reverse=True):
        print("  %-19s %.2f" % (k, fake[k]))
    assert 0.76 < fake["holds too long"] < 0.78
    # the managed face: honest interior, softened broadcast
    managed = 1.0 - (leak["nose wrinkle"] * 0.3)
    print("managed-face broadcast reduction factor: %.2f" % managed)
    assert 0.78 < managed < 0.79
    print("rule: read leaks gently - they usually mean someone working hard to be polite")
    print("OK: %s watched the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_drawing_guide(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # buildable geometry: proportions relative to face width = 100 units
    nose_crease_angle = 38.0     # degrees from vertical, the tent collapse
    nostril_lift = 6.0          # units upward from rest
    eye_open = 66.0             # percent of rest opening
    cheek_pouch = 4.5           # units of bunching under each eye
    lip_raise = 7.0             # units of central upper-lip lift
    head_turn = 12.0            # degrees away from trigger
    print("disgust face geometry (face width = 100 units):")
    print("  nose crease angle: %.0f deg from vertical" % nose_crease_angle)
    print("  nostril lift: %.1f units" % nostril_lift)
    print("  eye opening: %.0f %% of rest" % eye_open)
    print("  cheek pouch: %.1f units under each eye" % cheek_pouch)
    print("  upper-lip raise: %.1f units, central" % lip_raise)
    print("  head turn: %.0f deg away" % head_turn)
    assert 37.9 < nose_crease_angle < 38.1
    assert 65.9 < eye_open < 66.1
    assert 6.9 < lip_raise < 7.1
    # silhouette check: inward-up crumple index
    crumple = (nostril_lift + lip_raise + cheek_pouch) / 3.0
    print("crumple index: %.2f (everything draws inward and up)" % crumple)
    assert 5.82 < crumple < 5.84
    print("rule: build in layers - nose, eyes, cheeks, mouth, head angle")
    print("OK: %s drafted the portcullis" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "body-signals": demo_body_signals,
    "posture": demo_posture,
    "sleep-appetite": demo_sleep_appetite,
    "bodies-differ": demo_bodies_differ,
    "face": demo_face,
    "face-intensity": demo_face_intensity,
    "hide-fake": demo_hide_fake,
    "drawing-guide": demo_drawing_guide,
})


def demo_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # prevalence ranking: % of people rating each domain strongly triggering
    prev = {"food": 78.0, "body products": 71.0, "death and decay": 69.0,
            "body envelope violations": 66.0, "hygiene": 58.0,
            "animals": 54.0, "interpersonal contact": 47.0,
            "moral violations": 44.0, "sexual": 39.0}
    print("trigger domains by prevalence (%% strongly triggered):")
    ranked = sorted(prev, key=prev.get, reverse=True)
    for k in ranked:
        print("  %-26s %4.1f %%" % (k, prev[k]))
    assert ranked[0] == "food"
    assert 77.9 < prev["food"] < 78.1
    assert 38.9 < prev["sexual"] < 39.1
    # sorting drill: three sample triggers -> domains
    drill = {"moldy sandwich": "food", "wound photo": "body envelope violations",
             "cheating scandal": "moral violations"}
    hits = sum(1 for v in drill.values() if v in prev)
    print("sorting drill: %d/%d sorted correctly" % (hits, len(drill)))
    assert hits == 3
    print("rule: sort the trigger first - spit-it-out fits domain one, speak-up fits domain nine")
    print("OK: %s posted the nine sectors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # learned tag strength decays only with new SAFE exposures
    def tag_strength(years_since, safe_exposures):
        base = 10.0 * math.exp(-years_since / 12.0)   # slow natural fade
        return max(0.5, base - 0.35 * safe_exposures)   # each safe meal rewrites
    print("tag strength after food poisoning (0-10):")
    for yrs, exp in ((0, 0), (2, 0), (2, 10), (5, 20)):
        print("  %d yrs, %2d safe exposures -> %.2f" % (yrs, exp, tag_strength(yrs, exp)))
    assert 9.9 < tag_strength(0, 0) < 10.1
    assert 8.45 < tag_strength(2, 0) < 8.47
    assert 4.95 < tag_strength(2, 10) < 4.97
    assert 0.49 < tag_strength(5, 20) < 0.51
    # generalization: tag spreads to similar stimuli at a fraction
    general = tag_strength(2, 0) * 0.45
    print("generalized tag (similar smells): %.2f" % general)
    assert 3.80 < general < 3.82
    print("rule: the map is real, it just may be out of date - update with patrols, not arguments")
    print("OK: %s annotated the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ambush multiplier: wave = base * (1 + surprise)
    def wave(base, surprise):
        return base * (1.0 + surprise)
    cases = [("expected bad smell", 6.0, 0.1), ("texture betrayal", 5.0, 0.8),
             ("hidden discovery", 7.0, 0.9), ("delayed realization", 4.0, 1.0)]
    print("ambush waves (base intensity 0-10, surprise 0-1):")
    for label, b, s in cases:
        print("  %-20s base %.1f surprise %.1f -> wave %.2f" % (label, b, s, wave(b, s)))
    assert 6.59 < wave(6.0, 0.1) < 6.61
    assert 8.99 < wave(5.0, 0.8) < 9.01
    assert 13.29 < wave(7.0, 0.9) < 13.31
    assert 7.99 < wave(4.0, 1.0) < 8.01
    # expectation hygiene: a 10-second check removes the surprise half
    saved = wave(7.0, 0.9) - wave(7.0, 0.0)
    print("a sniff-check saves %.2f wave points" % saved)
    assert 6.29 < saved < 6.31
    print("rule: name the second alarm - part of this wave is the surprise, not the thing")
    print("OK: %s defused the ambushes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cascade transition probabilities from disgust to each follower
    trans = {"anger": 0.38, "shame": 0.16, "fear": 0.27, "sadness": 0.12,
             "stands alone": 0.07}
    tot = sum(trans.values())
    print("from disgust, the cascade goes to:")
    for k in sorted(trans, key=trans.get, reverse=True):
        print("  %-12s p=%.2f" % (k, trans[k]))
    print("transition sum: %.2f" % tot)
    assert 0.99 < tot < 1.01
    top = max(trans, key=trans.get)
    print("most likely follower: %s" % top)
    assert top == "anger"
    # chain-tracing: treating the first link deflates followers
    before = sum(v for k, v in trans.items() if k != "stands alone")
    after = before * 0.25
    print("follower load before tracing: %.2f, after: %.2f" % (before, after))
    assert 0.92 < before < 0.94
    assert 0.23 < after < 0.24
    print("rule: find the first flame - crews at the fourth tower chase smoke")
    print("OK: %s traced the chains" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # action-family likelihoods (0-1) at three alarm levels
    fams = ["avoidance", "expulsion", "cleansing", "barriers", "protest"]
    table = {2: [0.85, 0.10, 0.25, 0.30, 0.02],
             5: [0.95, 0.45, 0.70, 0.65, 0.20],
             9: [1.00, 0.90, 0.95, 0.90, 0.75]}
    print("action likelihoods by alarm level:")
    print("  level | " + " ".join("%-10s" % f[:10] for f in fams))
    for lv in (2, 5, 9):
        print("  %5d | " % lv + " ".join("%-10.2f" % v for v in table[lv]))
    assert table[2][0] > table[2][4]   # mild: avoidance dominates protest
    assert table[9][1] > table[5][1]   # expulsion rises with level
    assert table[9][4] > table[2][4]   # protest emerges at high/moral levels
    # circuit completion: action taken -> alarm stands down
    before, after_action = 9.0, 9.0 * 0.18
    print("alarm 9.0 -> after completing action: %.2f" % after_action)
    assert 1.61 < after_action < 1.63
    print("rule: healthy disgust acts, then rests - the circuit completes")
    print("OK: %s drilled the five families" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_behavior_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # voice shifts with alarm level: pitch rise (%), speech rate change (%)
    def voice(alarm):
        return {"pitch_up": 2.5 * alarm, "rate_up": 3.0 * alarm,
                "words_per_burst": max(2, int(14 - 1.3 * alarm))}
    print("voice at three alarm levels:")
    for a in (2, 5, 9):
        v = voice(a)
        print("  alarm %d: pitch +%4.1f %%, rate +%4.1f %%, words/burst %d" %
              (a, v["pitch_up"], v["rate_up"], v["words_per_burst"]))
    assert 4.9 < voice(2)["pitch_up"] < 5.1
    assert 26.9 < voice(9)["rate_up"] < 27.1
    assert voice(9)["words_per_burst"] == 2
    assert voice(2)["words_per_burst"] == 11
    # distancing grammar: share of demonstrative "that" vs naming the thing
    that_share = {2: 0.25, 5: 0.55, 9: 0.85}
    print("share of 'that' (vs naming): %s" % that_share)
    assert that_share[9] > that_share[5] > that_share[2]
    print("rule: the press release always says one thing - distance wanted")
    print("OK: %s read the flags" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_behavior_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # contamination premium: % refusing a sterilized but once-tainted object
    refuse = {"juice (brief roach contact, sterilized)": 68.0,
              "sweater (disliked owner, laundered)": 54.0,
              "coin (morgue tray, disinfected)": 47.0}
    print("refusal rates for sterilized objects (%% refusing):")
    for k in sorted(refuse, key=refuse.get, reverse=True):
        print("  %-42s %4.1f %%" % (k, refuse[k]))
    assert 67.9 < refuse["juice (brief roach contact, sterilized)"] < 68.1
    # moral spillover: harshness uplift in foul-smelling rooms
    base_harsh, foul_harsh = 5.2, 6.4
    uplift = (foul_harsh - base_harsh) / base_harsh * 100.0
    print("moral harshness: clean room %.1f -> foul room %.1f (+%.1f %%)" %
          (base_harsh, foul_harsh, uplift))
    assert 23.0 < uplift < 23.1
    # pause-and-source discount
    discounted = foul_harsh - 0.8 * (foul_harsh - base_harsh)
    print("after pause-and-source check: %.2f (near baseline)" % discounted)
    assert 5.43 < discounted < 5.45
    print("rule: never silence the consultant - check its brief")
    print("OK: %s audited the verdicts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_behavior_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five rungs: probability of reaching each rung at peak alarm
    rungs = ["private avoidance", "visible avoidance", "expulsion/cleansing",
             "vocal condemnation", "person-tagging (DANGER)"]
    p = [1.00, 0.72, 0.45, 0.28, 0.06]
    print("escalation ladder - P(reaching rung) at peak alarm:")
    for r, q in zip(rungs, p):
        print("  rung %d  p=%.2f  %s" % (rungs.index(r) + 1, q, r))
    assert p[0] == 1.00
    assert 0.71 < p[1] < 0.73
    assert 0.05 < p[4] < 0.07
    # expected rung reached
    exp_rung = sum((i + 1) * (p[i] - (p[i + 1] if i + 1 < 5 else 0)) for i in range(5))
    print("expected rung reached: %.2f" % exp_rung)
    assert 2.50 < exp_rung < 2.52
    # off-ramp effect: stepping off at rung 2
    stopped = 1.0 - p[1]
    print("share never passing rung 1 with early off-ramp: %.0f %%" % (stopped * 100))
    assert 27.9 < stopped * 100 < 28.1
    print("rule: the alarm serves the territory - servants that redraw the map get relieved")
    print("OK: %s climbed down the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "classic-triggers": demo_classic_triggers,
    "personal-triggers": demo_personal_triggers,
    "surprise-triggers": demo_surprise_triggers,
    "chain-reactions": demo_chain_reactions,
    "behavior-actions": demo_behavior_actions,
    "behavior-speech": demo_behavior_speech,
    "behavior-decisions": demo_behavior_decisions,
    "behavior-escalation": demo_behavior_escalation,
})


def demo_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels: effectiveness scores (0-10) for completing the circuit
    channels = {"naming early": 7.5, "proportionate action": 9.0,
                "non-weaponized showing": 8.0, "channeling to craft": 8.5}
    print("healthy channels - circuit-completion effectiveness:")
    for k in sorted(channels, key=channels.get, reverse=True):
        print("  %-22s %.1f" % (k, channels[k]))
    best = max(channels, key=channels.get)
    print("strongest channel: %s" % best)
    assert best == "proportionate action"
    # combined outlet vs loop test: aftermath alarm after 60 min
    outlet = 9.0 * 0.15
    loop = 9.0 * 0.85
    print("alarm after 60 min - outlet: %.2f, loop: %.2f" % (outlet, loop))
    assert 1.34 < outlet < 1.36
    assert 7.64 < loop < 7.66
    composite = sum(channels.values()) / len(channels)
    print("composite health score: %.2f" % composite)
    assert 8.24 < composite < 8.26
    print("rule: the aftermath test - outlets settle, loops rehearse")
    print("OK: %s opened the outlets" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 30-day cost model: bottling vs exploding (arbitrary cost units)
    def cost_bottle(day):
        return 2.0 * day + 0.35 * day * day   # fermenting: grows quadratically
    def cost_explode(day):
        return 8.0 * day + 0.02 * day * day   # relational price, steadier
    print("cumulative cost over 30 days:")
    for d in (7, 14, 30):
        print("  day %2d: bottling %7.1f, exploding %7.1f" %
              (d, cost_bottle(d), cost_explode(d)))
    assert 31.1 < cost_bottle(7) < 31.2
    assert 374.9 < cost_bottle(30) < 375.1
    assert 56.9 < cost_explode(7) < 57.1
    assert 257.9 < cost_explode(30) < 258.1
    # crossover: bottling is cheaper early, worse late
    print("bottling cheaper at day 7: %s; at day 30: %s" %
          (cost_bottle(7) < cost_explode(7), cost_bottle(30) < cost_explode(30)))
    assert cost_bottle(7) < cost_explode(7)
    assert cost_bottle(30) > cost_explode(30)
    # repair value: small honest outlets cut bottling cost
    repaired = cost_bottle(30) * 0.25
    print("bottling cost with daily small outlets: %.1f (was %.1f)" %
          (repaired, cost_bottle(30)))
    assert 93.7 < repaired < 93.8
    print("rule: health here is beautifully boring - name it, act small, complete the circuit")
    print("OK: %s priced both failures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven practices: weekly impact on baseline sensitivity (points, 0-100 scale)
    impact = {"trigger journal": 3.2, "verification habit": 4.1,
              "breath-through": 2.8, "proportionate cleansing": 3.6,
              "gentle exposure diet": 5.4, "moral check": 4.8,
              "recovery respect": 3.0}
    print("weekly practice impact (sensitivity points reduced):")
    for k in sorted(impact, key=impact.get, reverse=True):
        print("  %-23s %.1f" % (k, impact[k]))
    total = sum(impact.values())
    print("combined weekly effect: %.1f points" % total)
    assert 26.8 < total < 27.0
    best = max(impact, key=impact.get)
    print("highest leverage: %s" % best)
    assert best == "gentle exposure diet"
    # eight weeks of practice on a baseline of 62 (floored at healthy 28)
    baseline, weeks = 62.0, 8
    raw = baseline - total * weeks * 0.35
    final = max(28.0, raw)
    print("baseline %.0f -> after %d weeks: %.1f (floor 28)" % (baseline, weeks, final))
    assert 27.9 < final < 28.1
    print("rule: maintained gates never have to shout")
    print("OK: %s oiled the hinges" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # recognition trainer: 6 described scenarios, cues per channel
    scenarios = [
        ("break-room smell", ["nose wrinkle", "lean-back", "thin 'interesting'"], True),
        ("deep concentration", ["nose wrinkle"], False),
        ("rejected dish", ["lip curl", "pushed plate", "ugh", "early exit"], True),
        ("tired lean", ["lean-back"], False),
        ("wound story", ["averted gaze", "swallow", "clipped bursts"], True),
        ("thinking hard", ["averted gaze"], False),
    ]
    # read rule: 2+ converging channels (beyond baseline) = disgust
    def read(cues):
        return len(cues) >= 2
    correct = sum(1 for _, cues, truth in scenarios if read(cues) == truth)
    print("recognition trainer - 6 scenarios:")
    for label, cues, truth in scenarios:
        call = read(cues)
        mark = "OK" if call == truth else "MISS"
        print("  [%s] %-16s cues=%d -> %s (truth %s)" %
              (mark, label, len(cues), "disgust" if call else "other",
               "disgust" if truth else "other"))
    print("trainer score: %d/%d" % (correct, len(scenarios)))
    assert correct == 6
    acc = correct / len(scenarios) * 100.0
    print("accuracy: %.1f %%" % acc)
    assert 99.9 < acc < 100.1
    print("rule: converge before concluding - and read quietly, adjust kindly")
    print("OK: %s ran the trainer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_supportive_response(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five support steps: relief contributed (0-10 each)
    steps = {"reduce trigger": 3.2, "validate briefly": 2.1,
             "physical comfort": 1.8, "give time": 1.5, "believe the feeling": 1.9}
    print("support steps - relief contributed:")
    for k in sorted(steps, key=steps.get, reverse=True):
        print("  %-19s %.1f" % (k, steps[k]))
    total = sum(steps.values())
    print("combined relief: %.1f / 10" % total)
    assert 10.4 < total < 10.6
    # the dismissal penalty: 'it is not that bad' subtracts
    penalty = 3.5
    net = total - penalty
    print("with a minimizing remark (-%.1f): net %.1f" % (penalty, net))
    assert 6.9 < net < 7.1
    # moral-disgust translation keeps 90% of the effect
    translated = total * 0.9
    print("translated to moral disgust: %.2f" % translated)
    assert 9.44 < translated < 9.46
    print("rule: notice, reduce, validate, comfort, wait - no speeches")
    print("OK: %s held the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_what_not_to_do(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six mistakes ranked by damage (0-10)
    damage = {"mockery": 9.2, "forced exposure": 8.8, "minimizing": 7.4,
              "mid-wave lecture": 6.1, "self-centering": 5.3, "pity face": 4.6}
    print("mistakes by damage (0-10):")
    ranked = sorted(damage, key=damage.get, reverse=True)
    for k in ranked:
        print("  %-17s %.1f" % (k, damage[k]))
    assert ranked[0] == "mockery"
    assert ranked[-1] == "pity face"
    assert 9.1 < damage["mockery"] < 9.3
    # repair: plain naming + non-repetition recovers most trust
    trust_before, repair = 3.0, 5.8
    trust_after = min(10.0, trust_before + repair)
    print("trust: %.1f -> after plain repair: %.1f" % (trust_before, trust_after))
    assert 8.79 < trust_after < 8.81
    avg_damage = sum(damage.values()) / len(damage)
    print("average mistake damage: %.2f" % avg_damage)
    assert 6.89 < avg_damage < 6.91
    print("rule: get out of the spotlight, get into the support steps")
    print("OK: %s posted the prohibitions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_neighbors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # distance matrix from disgust (0-10), two axes: urge + body signature
    neigh = {"contempt": 1.5, "anger": 3.0, "fear": 3.5, "shame": 4.5,
             "hatred": 6.0, "envy": 7.5}
    print("neighbor distances from disgust:")
    for k in sorted(neigh, key=neigh.get):
        print("  %-9s %.1f" % (k, neigh[k]))
    assert min(neigh, key=neigh.get) == "contempt"
    assert 1.4 < neigh["contempt"] < 1.6
    # triage drill: map each neighbor to its protocol
    proto = {"contempt": "humility work", "anger": "boundaries and words",
             "fear": "safety", "shame": "self-compassion and repair",
             "hatred": "interruption", "envy": "gratitude work"}
    print("triage: neighbor -> protocol")
    for k in sorted(neigh, key=neigh.get):
        print("  %-9s -> %s" % (k, proto[k]))
    assert proto["anger"] == "boundaries and words"
    assert len(proto) == 6
    print("rule: similar faces, different medicines - keep the pharmacy straight")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four great blends: disgust weight vs partner weight
    blends = {"horror": (0.55, "fear"), "outrage": (0.50, "anger"),
              "grief at decay": (0.45, "sadness"),
              "shock-revulsion": (0.60, "surprise")}
    print("the four great blends (disgust share / partner):")
    for name_b, (w, partner) in blends.items():
        print("  %-16s disgust %.2f + %s %.2f" % (name_b, w, partner, 1.0 - w))
        assert 0.99 < w + (1.0 - w) < 1.01
    # signature intensity of each blend at full alarm (0-10)
    sig = {"horror": 9.4, "outrage": 9.1, "grief at decay": 7.2,
           "shock-revulsion": 8.6}
    hottest = max(sig, key=sig.get)
    print("hottest blend at full alarm: %s (%.1f)" % (hottest, sig[hottest]))
    assert hottest == "horror"
    assert 9.39 < sig["horror"] < 9.41
    # response sequencing: answer loudest ingredient first
    order = {"horror": "safety, then cleansing", "outrage": "distance, then words",
             "grief at decay": "comfort, then cleanup",
             "shock-revulsion": "ride the wave, then verify once"}
    for b in blends:
        print("  %-16s -> %s" % (b, order[b]))
    assert order["outrage"] == "distance, then words"
    print("rule: name both ingredients, honor both urges, sequence the response")
    print("OK: %s blended the weather" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five scenes: (scene, minute, jonas_alarm, mara_alarm, circuit_open)
    scenes = [("trigger", 0, 9.0, 1.0, True),
              ("peak + ripple", 4, 8.0, 4.5, True),
              ("cascade traced", 12, 5.0, 5.5, True),
              ("repair", 25, 2.0, 2.5, False),
              ("aftershock filed", 260, 1.2, 0.8, False)]
    print("full simulation - alarm levels (0-10):")
    prev_open = True
    for label, minute, ja, ma, open_ in scenes:
        print("  t=%3d min  %-16s jonas %4.1f  mara %4.1f  circuit %s" %
              (minute, label, ja, ma, "OPEN" if open_ else "closed"))
    # jonas alarm strictly decreases after the peak scene
    alarms = [s[2] for s in scenes[1:]]
    assert alarms == sorted(alarms, reverse=True)
    assert 8.9 < scenes[0][2] < 9.1
    # resolution check: both under 1.5 by the final scene
    assert scenes[-1][2] < 1.5 and scenes[-1][3] < 1.5
    # cost accounting: one dish lost, zero friendships lost
    dishes_lost, friendships_lost = 1, 0
    print("cost: %d dish lost, %d friendships lost" % (dishes_lost, friendships_lost))
    assert dishes_lost == 1 and friendships_lost == 0
    # skills demonstrated across the five scenes
    skills = ["onset read", "peak ridden", "cascade traced", "circuit completed",
              "repair without mockery", "echo starved"]
    print("skills in play: %d" % len(skills))
    assert len(skills) == 6
    print("rule: alarm sounded, wave ridden, cascade traced, circuit completed, echo starved")
    print("OK: %s ran the training film" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "healthy-expression": demo_healthy_expression,
    "unhealthy-expression": demo_unhealthy_expression,
    "everyday-practices": demo_everyday_practices,
    "reading-others": demo_reading_others,
    "supportive-response": demo_supportive_response,
    "what-not-to-do": demo_what_not_to_do,
    "neighbors": demo_neighbors,
    "mixes": demo_mixes,
    "full-simulation": demo_full_simulation,
})

assert set(DEMOS) == {e["key"] for e in
                      __import__("entries_emotion_disgust").ENTRIES}, "demo map misses entries"
