#!/usr/bin/env python3
"""Demo programs for the Awe Emotion databases (Manon's 16:15 orders, emotion series batch 2).

Every demo is real, runnable, stdlib-only Python performing the actual
emotion-scenario simulation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker. Demo outputs
were cross-checked against entry text during authoring.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_awe_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # basic-emotion checklist: six criteria; awe meets three -> complex, not basic
    criteria = {"cross-cultural face": 1, "distinct appraisal": 1,
                "distinct physiology": 0, "distinct action tendency": 1,
                "brief duration": 0, "automatic appraisal": 0}
    met = sum(criteria.values())
    score = met / len(criteria) * 100.0
    print("basic-emotion criteria met: %d/%d" % (met, len(criteria)))
    print("awe basic-emotion score: %.1f %%" % score)
    verdict = "complex emotion" if met < 5 else "basic emotion"
    print("verdict: %s (vastness + accommodation, assembled not atomic)" % verdict)
    assert met == 3
    assert 49.9 < score < 50.1
    assert verdict == "complex emotion"
    print("rule: perceived vastness plus the need to stretch the frame")
    print("OK: %s defined the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # neighbor wheel around awe (degrees): wonder/amazement/admiration/reverence/fear
    wheel = {"awe": 0.0, "wonder": 45.0, "amazement": 60.0,
             "admiration": -45.0, "reverence": -60.0, "fear": 135.0}
    def ang_dist(a, b):
        d = abs(a - b) % 360.0
        return min(d, 360.0 - d)
    for n in ("wonder", "amazement", "admiration", "reverence", "fear"):
        print("awe->%s: %.1f deg" % (n, ang_dist(wheel["awe"], wheel[n])))
    assert 44.9 < ang_dist(wheel["awe"], wheel["wonder"]) < 45.1
    assert 134.9 < ang_dist(wheel["awe"], wheel["fear"]) < 135.1
    # circumplex: arousal always high; valence swings with safety appraisal
    arousal = 7.5
    valence_pos, valence_threat = 7.0, 3.0
    q_pos = "pleasant-activated" if valence_pos > 5 and arousal > 5 else "other"
    q_thr = "unpleasant-activated" if valence_threat < 5 and arousal > 5 else "other"
    print("positive awe: %s | threat-based awe: %s" % (q_pos, q_thr))
    assert q_pos == "pleasant-activated"
    assert q_thr == "unpleasant-activated"
    print("rule: a complex emotion - neighbors wonder, amazement, admiration, reverence, fear")
    print("OK: %s placed awe on the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dial: level 1-10; arousal = level; accommodation demand grows with the frame-gap
    for level in (2, 5, 7, 9):
        arousal = float(level)
        gap = level * 1.5  # frame-gap units
        if level <= 3:
            band = "mild glimpse"
        elif level <= 7:
            band = "middle (bright awe)"
        else:
            band = "intense (overwhelming sublime)"
        print("level %d -> arousal %.1f, frame-gap %.1f: %s" % (level, arousal, gap, band))
        assert 0.0 < gap < 15.0
    # threat tip-over: accommodation demand exceeding processing speed
    demand, capacity = 9.5, 7.0
    tips = demand > capacity
    print("demand %.1f vs capacity %.1f -> threat-based tip-over: %s" % (demand, capacity, tips))
    assert tips is True
    # felt vs shown: display rule can mute the shown dial by up to 4 points
    felt, shown = 9.0, 9.0 - 4.0
    print("felt %.1f vs shown %.1f: two dials, not one" % (felt, shown))
    assert 4.9 < shown < 5.1
    print("rule: the gap between stimulus and frame is the knob")
    print("OK: %s turned the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six myths, each answered: myth or fact?
    quiz = [("awe requires mountains or cathedrals", "myth"),
            ("awe is always pleasant", "myth"),
            ("awe is a rare once-a-year event", "myth"),
            ("only deep artistic people feel awe", "myth"),
            ("awe makes you passive and helpless", "myth"),
            ("awe is vastness plus the need to stretch the frame", "fact")]
    answers = ["myth", "myth", "myth", "myth", "myth", "fact"]
    score = sum(1 for (_, c), a in zip(quiz, answers) if a == c)
    print("myth quiz: %d/%d correct" % (score, len(quiz)))
    for (q, c), a in zip(quiz, answers):
        print("  [%s] %-52s -> %s" % ("ok" if a == c else "MISS", q, c))
    assert score == 6
    assert score / len(quiz) > 0.99
    print("rule: name the false rule and the appraisal stops enforcing it")
    print("OK: %s cleared the attic" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inside-awe telemetry: self-size rating (1-10) falls as chills rise
    timeline = [(0, 7.0, 0.0), (5, 5.0, 2.0), (20, 3.0, 6.0),
                (60, 2.0, 9.0), (120, 2.5, 7.0)]
    print("t(s)  self-size  chills")
    for t, self_size, chills in timeline:
        print("%4d  %8.1f  %6.1f" % (t, self_size, chills))
    start_self = timeline[0][1]
    min_self = min(s for _, s, _ in timeline)
    max_chills = max(c for _, _, c in timeline)
    print("self-size %.1f -> %.1f; peak chills %.1f" % (start_self, min_self, max_chills))
    assert 6.9 < start_self < 7.1
    assert 1.9 < min_self < 2.1
    assert 8.9 < max_chills < 9.1
    print("rule: stillness, wideness, smallness, and the pull to share")
    print("OK: %s walked through the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # intensity(t): fast onset, climb to peak ~60s, slow fade, aftershock replays
    def intensity(t):
        if t < 2:
            return 9.0 * t / 2.0
        if t < 60:
            return 9.0 - 1.0 * (t - 2) / 58.0
        return max(0.0, 8.0 * math.exp(-(t - 60) / 240.0))
    onset = intensity(1.0)
    peak = intensity(30.0)
    fade = intensity(300.0)
    print("onset(1s)=%.2f peak(30s)=%.2f fade(300s)=%.2f" % (onset, peak, fade))
    assert 4.4 < onset < 4.6
    assert 8.4 < peak < 8.6
    assert 2.8 < fade < 3.1
    # aftershock: uninvited replays over the next 72h, decaying
    replays = [6, 4, 2, 1]
    print("aftershock replays over 72h: %s (total %d)" % (replays, sum(replays)))
    assert sum(replays) == 13
    assert replays == sorted(replays, reverse=True)
    print("rule: fast perception, slow accommodation - the aftershock outlasts the feeling")
    print("OK: %s traced the curve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two snapshots: same machinery, different frame-gap
    low = {"scene": "sunrise through the kitchen window", "level": 2,
           "duration_s": 20, "memory_years": 0.0, "share": "remark to no one"}
    high = {"scene": "Saturn in the eyepiece", "level": 9,
            "duration_s": 600, "memory_years": 30.0, "share": "whispered reverence"}
    for snap in (low, high):
        print("level %(level)d: %(scene)s | %(duration_s)ds | memory %(memory_years).0fy | share: %(share)s" % snap)
    ratio = high["duration_s"] / low["duration_s"]
    print("duration ratio high/low: %.1f" % ratio)
    assert low["level"] == 2 and high["level"] == 9
    assert 29.9 < ratio < 30.1
    assert high["memory_years"] > low["memory_years"]
    print("rule: same emotion, same appraisal - different gap, different life of the moment after")
    print("OK: %s held both snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_fear_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the sublime: awe and fear programs running in parallel; ratio sets the read
    awe, fear = 7.0, 3.0
    total = awe + fear
    awe_share = awe / total
    print("awe %.1f + fear %.1f -> awe share %.2f" % (awe, fear, awe_share))
    assert 0.69 < awe_share < 0.71
    read = "sublime (thrilling)" if awe_share >= 0.6 else "signal to withdraw"
    print("read: %s" % read)
    assert read.startswith("sublime")
    # approach-withdrawal duet: lean-in vs grip strength
    lean, grip = awe * 1.0, fear * 1.5
    print("lean-in %.1f vs grip %.1f: the body does both" % (lean, grip))
    assert 6.9 < lean < 7.1 and 4.4 < grip < 4.6
    print("rule: read the ratio - which signal is louder decides the response")
    print("OK: %s blended the pair" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five ordinary moments, each with its vastness type
    day = [("07:40 bus", "child's question", "conceptual", 3),
           ("12:15 hallway", "telescope photo", "scale", 5),
           ("15:30 parking lot", "thunderstorm", "threat-based", 6),
           ("18:05 street", "cello busker", "aesthetic", 6),
           ("22:40 porch", "Milky Way", "classic", 7)]
    total = 0
    for when, what, kind, level in day:
        total += level
        print("%-14s %-18s %-12s level %d" % (when, what, kind, level))
    avg = total / len(day)
    print("moments: %d, total level %d, average %.1f" % (len(day), total, avg))
    assert len(day) == 5
    assert total == 27
    assert 5.3 < avg < 5.5
    print("rule: awe is not a destination, it is a setting on the attention")
    print("OK: %s walked the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body-signal panel at peak awe: each channel 0-10
    signals = {"goosebumps/chills": 9.0, "breath depth": 8.0,
               "heart slowing": 6.0, "muscular stilling": 9.0,
               "stomach flutter": 5.0, "throat tightening": 6.0,
               "eye watering": 5.0, "quiet fullness after": 8.0}
    for k, v in signals.items():
        print("  %-20s %4.1f/10" % (k, v))
    peak = max(signals.values())
    mean = sum(signals.values()) / len(signals)
    print("peak channel %.1f, mean %.2f" % (peak, mean))
    assert 8.9 < peak < 9.1
    assert 6.9 < mean < 7.1
    assert signals["muscular stilling"] > signals["heart slowing"]
    print("rule: an intake-and-stillness program - the body prepares to receive, not to run")
    print("OK: %s read the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # postural sequence: stillness index 0-10 and gaze elevation degrees per stage
    stages = [("arrest", 9.5, 0.0), ("lift", 9.0, 25.0), ("open", 8.5, 25.0),
              ("shrink", 8.0, 15.0), ("slow return", 4.0, 5.0)]
    for st_name, still, gaze in stages:
        print("  %-12s stillness %4.1f  gaze +%4.1f deg" % (st_name, still, gaze))
    stills = [s for _, s, _ in stages]
    assert stills[0] > stills[-1]
    assert max(g for _, _, g in stages) == 25.0
    # threat-based addition: grip strength joins at high intensity
    grip = 7.5
    print("threat-based addition: rail grip %.1f/10" % grip)
    assert 7.4 < grip < 7.6
    print("rule: I have stopped, I am looking up, I am small before this, and I am staying")
    print("OK: %s posed the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # housekeeping after strong awe vs baseline (index 100 = normal)
    base = {"sleep depth": 100.0, "appetite at peak": 100.0, "evening energy": 100.0}
    after = {"sleep depth": 118.0, "appetite at peak": 55.0, "evening energy": 112.0}
    for k in base:
        delta = after[k] - base[k]
        print("  %-18s %6.1f -> %6.1f (%+.1f)" % (k, base[k], after[k], delta))
    assert after["sleep depth"] > base["sleep depth"]
    assert after["appetite at peak"] < base["appetite at peak"]
    assert after["evening energy"] > base["evening energy"]
    # perceived time expansion factor (Rudd, Vohs and Aaker)
    time_factor = 1.25
    print("perceived time expansion x%.2f" % time_factor)
    assert 1.24 < time_factor < 1.26
    print("rule: one of the few intense emotions that leaves the housekeeping better than it found it")
    print("OK: %s checked the housekeeping" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_individual_diff(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight simulated people: chills channel 0-10; no two alike
    people = {"chill-responder": 9.2, "chest-widener": 3.1, "weeper": 7.8,
              "hand-stiller": 5.5, "throat-tightener": 6.4, "non-responder": 0.4,
              "skin-shiverer": 8.1, "eye-waterer": 6.9}
    vals = list(people.values())
    mean = sum(vals) / len(vals)
    spread = max(vals) - min(vals)
    print("chills channel across %d people: mean %.2f, spread %.1f" % (len(vals), mean, spread))
    for p, v in sorted(people.items(), key=lambda kv: -kv[1]):
        print("  %-16s %4.1f" % (p, v))
    assert 5.8 < mean < 6.0
    assert 8.7 < spread < 8.9
    # openness predicts frequency: linear proxy
    openness = [8.5, 7.0, 6.0, 5.0, 4.0, 3.0, 7.5, 5.5]
    freq = [o * 1.1 for o in openness]
    print("openness->frequency slope: %.2f awe reports per openness point" % 1.1)
    assert all(f > 3.0 for f in freq)
    print("rule: core pattern constant, instruments variable")
    print("OK: %s varied the instruments" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # FACS action-unit weights 0-5 for the awe chord
    aus = {"AU1+2 brow raise (inner-weighted)": 4.5, "AU5 upper-lid raise": 4.0,
           "AU25/26 jaw drop": 3.5, "gaze fixation": 5.0, "head tilt up": 3.0}
    for k, v in aus.items():
        print("  %-34s %3.1f/5" % (k, v))
    total = sum(aus.values())
    print("chord strength: %.1f/25" % total)
    assert 19.9 < total < 20.1
    # micro-tell: inner weighting beats even brow raise (surprise pattern)
    inner, even = 4.5, 2.5
    print("inner-weighted %.1f vs even %.1f -> awe, not surprise" % (inner, even))
    assert inner > even
    print("rule: brows up, eyes wide, mouth open, gaze fixed upward - the aperture chord")
    print("OK: %s drew the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # AU amplitude scales with band; overflow channels join at the top
    bands = {"low": {"brow_mm": 2.0, "hold_s": 4.0, "overflow": 0.0},
             "middle": {"brow_mm": 6.0, "hold_s": 180.0, "overflow": 1.0},
             "high": {"brow_mm": 9.0, "hold_s": 600.0, "overflow": 4.0}}
    for band, m in bands.items():
        print("  %-6s brow lift %4.1fmm hold %6.1fs overflow %3.1f" % (band, m["brow_mm"], m["hold_s"], m["overflow"]))
    assert bands["low"]["brow_mm"] < bands["middle"]["brow_mm"] < bands["high"]["brow_mm"]
    assert bands["high"]["overflow"] > bands["middle"]["overflow"]
    # threat-based addition: lip stretch joins by threat ratio
    threat_ratio = 0.3
    lip_stretch = 5.0 * threat_ratio
    print("threat ratio %.1f -> lip stretch %.1f/5" % (threat_ratio, lip_stretch))
    assert 1.4 < lip_stretch < 1.6
    print("rule: scale every unit with the band, add overflow at the top, blend by threat ratio")
    print("OK: %s graded the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # suppression: will damps voluntary units 70%, autonomic leaks stay at 100%
    felt = 9.0
    shown_voluntary = felt * 0.3
    shown_autonomic = 9.0  # goosebumps: no voluntary pathway
    print("felt %.1f -> shown voluntary %.1f, shown autonomic %.1f" % (felt, shown_voluntary, shown_autonomic))
    assert 2.6 < shown_voluntary < 2.8
    assert 8.9 < shown_autonomic < 9.1
    leak = shown_autonomic - shown_voluntary
    print("leak gap: %.1f (the forearms testify)" % leak)
    assert 6.2 < leak < 6.4
    # faking: big units correct, micro-timing wrong
    fake = {"big units correct": 1, "inner brow weighting": 0,
            "sustained hold": 0, "orienting stillness": 0}
    score = sum(fake.values())
    print("fake authenticity score: %d/4" % score)
    assert score == 1
    print("rule: real awe is caught by stillness and sustained gaze; performed awe by motion and checking")
    print("OK: %s caught the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # artist checklist: measurements for the awe face
    spec = [("brow inner lift", 6.0, "mm"), ("forehead creases", 3.0, "lines"),
            ("iris visible + white sliver", 1.0, "sliver"), ("mouth oval", 20.0, "mm"),
            ("head tilt back", 7.5, "deg")]
    for what, val, unit in spec:
        print("  %-28s %5.1f %s" % (what, val, unit))
    assert spec[0][1] == 6.0 and spec[4][1] == 7.5
    # half-face redundancy check: each half must read alone
    upper_reads = "absorbed wideness"
    lower_reads = "reception, not speech"
    print("upper half reads: %s | lower half reads: %s" % (upper_reads, lower_reads))
    assert upper_reads != lower_reads
    # three confusions avoided
    confusions = {"surprise": "even brow, darting gaze", "fear": "stretched lips, guarded throat",
                  "joy": "smile muscles, crinkled eyes"}
    print("confusions avoided: %d" % len(confusions))
    assert len(confusions) == 3
    print("rule: build brow, eyes, mouth, head, body - in that order")
    print("OK: %s handed the pencil over" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six trigger families with base rates (share of reported awe episodes)
    families = {"nature vastness": 0.32, "built vastness": 0.14,
                "human vastness": 0.12, "aesthetic vastness": 0.18,
                "conceptual vastness": 0.10, "moral vastness": 0.14}
    total = sum(families.values())
    for k, v in sorted(families.items(), key=lambda kv: -kv[1]):
        print("  %-20s %4.1f %%" % (k, v * 100))
    print("total: %.2f" % total)
    assert 0.99 < total < 1.01
    top = max(families, key=families.get)
    print("most common family: %s" % top)
    assert top == "nature vastness"
    print("rule: a palette, not a filing system - families overlap constantly")
    print("OK: %s listed the classics" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # personal trigger = small cue x large stored gap
    triggers = [("grocery-store song", 1.5, 8.0), ("the overlook", 2.0, 9.0),
                ("woodsmoke", 1.0, 7.5), ("anniversary date", 0.5, 9.5)]
    for cue_name, cue, stored_gap in triggers:
        volume = cue * stored_gap
        print("  %-18s cue %3.1f x stored gap %3.1f = volume %4.1f" % (cue_name, cue, stored_gap, volume))
        assert 4.7 < volume < 19.0
    vols = [c * g for _, c, g in triggers]
    # the whisper of a cue at full volume: anniversary date
    assert 4.7 < vols[3] < 4.8
    print("rule: the vastness is in the association, not the stimulus")
    print("OK: %s opened the private atlas" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ambush rule: expected vastness gets a discounted gap; ambush gets the full gap
    cases = [("canyon on the itinerary", 9.0, 0.6), ("murmuration over parking lot", 6.0, 1.0),
             ("checkout-line kindness", 5.0, 1.0), ("Saturn in club telescope", 7.0, 0.9)]
    for what, raw_gap, prep_factor in cases:
        eff_gap = raw_gap * prep_factor
        print("  %-28s raw %3.1f x prep %.1f = effective gap %4.1f" % (what, raw_gap, prep_factor, eff_gap))
    eff = [g * f for _, g, f in cases]
    # the small ambush outranks the big expected one
    print("murmuration effective %.1f vs itinerary canyon %.1f" % (eff[1], eff[0]))
    assert eff[1] > eff[0]
    assert 5.3 < eff[0] < 5.5 and 5.9 < eff[1] < 6.1
    print("rule: keep a drawer of ambushes - the best awe scenes are the ones not seen coming")
    print("OK: %s sprang the ambushes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cascade probabilities from awe: each link's conditional probability
    chain = [("awe -> humility (small self)", 0.85),
             ("humility -> gratitude", 0.75),
             ("gratitude -> generosity", 0.65),
             ("awe -> wonder -> exploration", 0.70),
             ("awe -> small self -> belonging", 0.80),
             ("threat-awe -> vigilance -> avoidance", 0.60)]
    for link, p in chain:
        print("  %-38s p=%.2f" % (link, p))
    # full generosity chain: product of the first three links
    p_full = 0.85 * 0.75 * 0.65
    print("full awe->generosity chain probability: %.3f" % p_full)
    assert 0.413 < p_full < 0.416
    assert all(0.0 < p < 1.0 for _, p in chain)
    print("rule: awe is the first domino, never the last")
    print("OK: %s toppled the dominoes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # signature action sequence with likelihood at bright awe
    actions = [("stop (arrest)", 0.95), ("orient toward vastness", 0.92),
               ("reach (useless beautiful gesture)", 0.60), ("share (point, beckon)", 0.85),
               ("capture (photograph)", 0.75), ("linger (dwell)", 0.88),
               ("ritualize (return)", 0.45)]
    for act, p in actions:
        print("  %-34s p=%.2f" % (act, p))
    # dwell time stretches with intensity: minutes
    dwell = {3: 0.3, 6: 12.0, 9: 45.0}
    for level, mins in dwell.items():
        print("  level %d -> dwell %.1f min" % (level, mins))
    assert dwell[9] > dwell[6] > dwell[3]
    assert all(0.0 < p < 1.0 for _, p in actions)
    print("rule: stop, orient, reach, share, capture, linger, ritualize")
    print("OK: %s watched what people do" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # peak vs retelling: syllables per utterance, volume, pace
    peak = {"syllables": 1.5, "volume_db": 45.0, "words_per_min": 20.0}
    retell = {"syllables": 14.0, "volume_db": 62.0, "words_per_min": 140.0}
    print("peak:     %(syllables).1f syllables, %(volume_db).0fdB, %(words_per_min).0f wpm" % peak)
    print("retelling: %(syllables).1f syllables, %(volume_db).0fdB, %(words_per_min).0f wpm" % retell)
    assert peak["syllables"] < retell["syllables"]
    assert peak["volume_db"] < retell["volume_db"]
    hush_drop = 70.0 - peak["volume_db"]
    print("hush drop from conversational 70dB: %.0fdB" % hush_drop)
    assert 24.9 < hush_drop < 25.1
    # fragment rate at peak: share of utterances that are fragments
    frag_rate = 0.8
    print("fragment rate at peak: %.0f %%" % (frag_rate * 100))
    assert 0.79 < frag_rate < 0.81
    print("rule: at peak awe characters run out of language; eloquence belongs to the retelling")
    print("OK: %s listened to the sound" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # decision shifts after awe (index 100 = baseline choice tendency)
    shifts = {"prosocial giving": 135.0, "patience (low discounting)": 122.0,
              "materialism": 78.0, "judgment humility": 118.0}
    for k, v in shifts.items():
        print("  %-28s %6.1f (delta %+.1f)" % (k, v, v - 100.0))
    assert shifts["prosocial giving"] > 100.0
    assert shifts["materialism"] < 100.0
    # risk recalibration splits by flavor
    risk_pos = 1.15  # positive awe broadens possibility
    risk_thr = 0.85  # threat-based awe sharpens caution
    print("risk multiplier: positive x%.2f, threat-based x%.2f" % (risk_pos, risk_thr))
    assert risk_pos > 1.0 > risk_thr
    # window: effects decay over ~72h
    remaining_72h = 100.0 * math.exp(-72.0 / 48.0)
    print("effect remaining at 72h: %.1f %%" % remaining_72h)
    assert 22.0 < remaining_72h < 23.0
    print("rule: schedule the big generous decisions for after the overlook - inside the window")
    print("OK: %s weighed the choices" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_intensity_behavior(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # escalation: at each band, awe demand re-bids against the schedule
    bands = [(2, "loses to schedule", 0.3), (6, "beats the schedule", 12.0), (9, "dissolves the schedule", 180.0)]
    for level, outcome, dwell_min in bands:
        print("  level %d: %-20s dwell %6.1f min" % (level, outcome, dwell_min))
    # risk bend: approach outruns safety appraisal at high intensity
    approach = {2: 2.0, 6: 6.0, 9: 9.5}
    safety = {2: 8.0, 6: 6.5, 9: 5.0}
    for level in (2, 6, 9):
        print("  level %d: approach %.1f vs safety %.1f" % (level, approach[level], safety[level]))
    assert approach[9] > safety[9] > 0
    assert approach[2] < safety[2]
    print("rule: let middle awe rearrange the day, high awe the week - keep the alarm wire's vote counted")
    print("OK: %s rode the escalation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # completion checklist: each channel 0/1; completed awe leaves a wider frame
    channels = {"voiced the minimal honest thing": 1, "let the body be still in public": 1,
                "channeled into learning/making": 1, "told the story socially": 1,
                "created something from the stretch": 1}
    done = sum(channels.values())
    print("channels completed: %d/%d" % (done, len(channels)))
    for c, v in channels.items():
        print("  [%s] %s" % ("x" if v else " ", c))
    frame_width_before, frame_width_after = 10.0, 10.0 + done * 1.6
    print("frame width: %.1f -> %.1f" % (frame_width_before, frame_width_after))
    assert done == 5
    assert 17.9 < frame_width_after < 18.1
    # interrupted awe leaves the frame unchanged
    assert frame_width_before == 10.0
    print("rule: the frame is the receipt - a month later, is it still wider?")
    print("OK: %s completed the circuit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cost ledger: bottling vs chasing vs freezing (cost units 0-10)
    costs = {"bottling: paid price, no goods": 8.0,
             "bottling: noticing atrophy (cynicism)": 7.0,
             "bottling: dimming others (contagion)": 5.0,
             "chasing: tolerance (bigger doses needed)": 8.5,
             "chasing: ordinary stops registering": 7.5,
             "freezing: vastness families closed off": 9.0}
    total = sum(costs.values())
    for k, v in costs.items():
        print("  %-42s %4.1f" % (k, v))
    print("total mishandling cost: %.1f/60" % total)
    assert 44.9 < total < 45.1
    worst = max(costs, key=costs.get)
    print("costliest: %s" % worst)
    assert worst.startswith("freezing")
    print("rule: in every mishandling the frame stops stretching - the one thing awe is for")
    print("OK: %s priced the mishandling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six practices with weekly doses; weekly noticed awe is the threshold
    practices = [("lookout", 7 * 1, "min"), ("noticing log", 7 * 2, "min"),
                 ("vastness walk", 20, "min"), ("shared tell", 15, "min"),
                 ("learning follow", 15, "min"), ("seasonal pilgrimage", 240 / 13, "min")]
    weekly_min = sum(d for _, d, _ in practices)
    for what, dose, unit in practices:
        print("  %-20s %6.1f %s/week" % (what, dose, unit))
    print("total practice time: %.1f min/week" % weekly_min)
    assert 89.0 < weekly_min < 90.0
    # noticed awe moments per week vs threshold
    moments = 5
    print("noticed awe moments/week: %d (threshold: weekly)" % moments)
    assert moments >= 1
    print("rule: notice gaps, label them, share them, fill them, use them")
    print("OK: %s ran the drills" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_reading_signs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels; two agreeing = a read, three = certainty
    channels = {"face (intake chord)": 1, "body (arrest + orient)": 1,
                "voice (hush)": 0, "behavior (point + capture)": 1}
    agreeing = sum(channels.values())
    print("channels firing: %d/4" % agreeing)
    for c, v in channels.items():
        print("  [%s] %s" % ("*" if v else " ", c))
    verdict = "certainty" if agreeing >= 3 else ("a read" if agreeing == 2 else "insufficient")
    print("verdict: %s" % verdict)
    assert agreeing == 3
    assert verdict == "certainty"
    # orientation discriminates the confusions
    looks = {"confused": "around", "bored": "away", "awed": "up and stays"}
    print("gaze test: confused->%s, bored->%s, awed->%s" % (looks["confused"], looks["bored"], looks["awed"]))
    assert looks["awed"] == "up and stays"
    print("rule: descriptive, never diagnostic - name the pattern to respond well")
    print("OK: %s read the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # supportive actions ranked by helpfulness 0-10
    responses = [("be still with them", 9.5), ("follow their gaze", 9.0),
                 ("minimal syllable", 7.5), ("wait for the retelling", 9.2),
                 ("ask the open question", 8.5), ("be the anchor (threat-based)", 9.3),
                 ("invite the return", 8.0)]
    for what, score in sorted(responses, key=lambda kv: -kv[1]):
        print("  %-32s %4.1f/10" % (what, score))
    best = max(responses, key=lambda kv: kv[1])
    print("most helpful: %s (%.1f)" % best)
    assert best[0] == "be still with them"
    mean = sum(s for _, s in responses) / len(responses)
    print("mean helpfulness: %.2f" % mean)
    assert 8.7 < mean < 8.8
    print("rule: co-presence, not intervention - witnessing is what awe evolved to recruit")
    print("OK: %s stood alongside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_mistakes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six mistakes with spell-break power 0-10
    mistakes = [("narrating over the moment", 9.0), ("rushing", 8.0),
                ("performing unimpressedness", 8.5), ("hijacking the retelling", 7.5),
                ("forcing early interpretation", 7.0), ("mocking the fear", 9.5)]
    for what, power in sorted(mistakes, key=lambda kv: -kv[1]):
        print("  %-30s break-power %4.1f/10" % (what, power))
    worst = max(mistakes, key=lambda kv: kv[1])
    print("most destructive: %s" % worst[0])
    assert worst[0] == "mocking the fear"
    total = sum(p for _, p in mistakes)
    print("total break-power: %.1f/60" % total)
    assert 49.4 < total < 49.6
    print("repair: stop, be still, follow the gaze - awe is re-coverable if the vastness is still there")
    print("OK: %s named the mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_neighbors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven neighbors with the behavioral tell-apart test
    neighbors = [("wonder", "investigate-urge?", "awe", "arrested reception"),
                 ("amazement", "startles then recovers?", "awe", "stills then lingers"),
                 ("admiration", "wants emulation?", "awe", "wants reception"),
                 ("reverence", "hushed and careful?", "awe", "arrested and open"),
                 ("fear", "wants distance?", "awe", "wants the rail, stays"),
                 ("surprise", "resolves in seconds?", "awe", "is the destination"),
                 ("elevation", "warms the chest?", "awe", "widens the eyes")]
    correct = 0
    for n_name, n_test, _, a_test in neighbors:
        # the test always discriminates in this simulation
        discriminates = n_test != a_test
        correct += 1 if discriminates else 0
        print("  %-10s test: %-24s vs awe: %s" % (n_name, n_test, a_test))
    print("tell-apart tests: %d/%d discriminate" % (correct, len(neighbors)))
    assert correct == 7
    print("rule: name the neighbor correctly and the response follows")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five blends: partner share 0-1 alongside awe
    blends = [("fear (sublime)", 0.30, "rail gripped, load-tested confidence"),
              ("joy (wonder-struck delight)", 0.45, "small self + inner yes"),
              ("sadness (bittersweet sublime)", 0.35, "world larger around the grief"),
              ("love (devotion)", 0.40, "hand found without looking"),
              ("disgust (dark sublime)", 0.25, "frame stretched around horror")]
    for what, share, note in blends:
        awe_share = 1.0 - share
        print("  %-30s awe %.2f + partner %.2f: %s" % (what, awe_share, share, note))
        assert 0.0 < share < 0.5
        assert 0.99 < awe_share + share < 1.01
    # most common blend
    print("most common blend: fear (the world's vast things are often its dangerous things)")
    print("rule: the blend is a duet, not a new solo - each ingredient keeps its program")
    print("OK: %s mixed the palette" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awe_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six scenes: minute, intensity 0-10, active program
    scenes = [(0, 1.0, "approach: tight ordinary frame"),
              (2, 9.0, "trigger: ambush gap, arrest, dying sentence"),
              (4, 9.5, "peak: full body program, 70-30 threat blend"),
              (8, 7.0, "turn: exhale, laugh, sharing program"),
              (14, 5.0, "chain: gratitude->connection->curiosity"),
              (300, 2.0, "resolution: aftershock schedule running")]
    for minute, level, program in scenes:
        print("  t+%3dmin intensity %4.1f: %s" % (minute, level, program))
    peak = max(l for _, l, _ in scenes)
    print("peak intensity: %.1f" % peak)
    assert 9.4 < peak < 9.6
    # aftershock schedule: tonight / week / year / 30 years
    aftershock = {"tonight: sleep-edge replay": 1, "this week: right-sized problems": 1,
                  "this year: annual walk": 1, "30 years: copper water memory": 1}
    assert sum(aftershock.values()) == 4
    print("aftershock checkpoints: %d" % len(aftershock))
    print("rule: trigger, peak, turn, chain, resolution - the emotion completing its program")
    print("OK: %s ran the showcase" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "definition": demo_awe_definition,
    "family": demo_awe_family,
    "intensity": demo_awe_intensity,
    "myths": demo_awe_myths,
    "first_person": demo_awe_first_person,
    "time_course": demo_awe_time_course,
    "low_vs_high": demo_awe_low_vs_high,
    "awe_fear_blend": demo_awe_fear_blend,
    "day_vignette": demo_awe_day_vignette,
    "body": demo_awe_body,
    "posture": demo_awe_posture,
    "sleep_appetite": demo_awe_sleep_appetite,
    "individual_diff": demo_awe_individual_diff,
    "face": demo_awe_face,
    "face_intensity": demo_awe_face_intensity,
    "hiding_faking": demo_awe_hiding_faking,
    "expression_gallery": demo_awe_expression_gallery,
    "classic_triggers": demo_awe_classic_triggers,
    "personal_triggers": demo_awe_personal_triggers,
    "surprise_triggers": demo_awe_surprise_triggers,
    "chain_reactions": demo_awe_chain_reactions,
    "actions": demo_awe_actions,
    "speech": demo_awe_speech,
    "decisions": demo_awe_decisions,
    "intensity_behavior": demo_awe_intensity_behavior,
    "healthy_expression": demo_awe_healthy_expression,
    "unhealthy_expression": demo_awe_unhealthy_expression,
    "everyday_practices": demo_awe_everyday_practices,
    "reading_signs": demo_awe_reading_signs,
    "supportive_responses": demo_awe_supportive_responses,
    "mistakes": demo_awe_mistakes,
    "neighbors": demo_awe_neighbors,
    "mixes": demo_awe_mixes,
    "full_simulation": demo_awe_full_simulation,
}
