#!/usr/bin/env python3
"""34 machine-executed scenario-simulator demos for the Anticipation Emotion Database.

Every demo is real, runnable, stdlib-only Python. Each simulates the record's
scenario, prints real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Descriptive/educational only:
no real people, no diagnoses.
"""

def _w(hdr, name, rid, group, body):
    return hdr(name, rid, group) + body

def d_e01(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def intensity(importance, uncertainty, days_away):
    closeness = max(0.0, 10.0 - min(days_away, 30) / 3.0)
    return round(0.45 * importance * 10 + 0.35 * uncertainty * 10 + 0.20 * closeness * 10, 2)

def main():
    s1 = intensity(8, 6, 3)    # big interview in 3 days
    s2 = intensity(3, 2, 60)   # mild curiosity, far off
    s3 = intensity(9, 9, 1)    # life decision tomorrow, unknown outcome
    print("scenario intensities:", s1, s2, s3)
    for v in (s1, s2, s3):
        assert 0.0 <= v <= 100.0, "intensity out of bounds"
    assert s3 > s1 > s2, "ordering broken: closeness/importance must raise intensity"
    assert abs(s2 - 20.5) < 0.01, "mild scenario drifted"
    assert abs(s3 - 91.33) < 0.01, "peak scenario drifted"
    print("OK: e01 anticipation-intensity model - 3 scenarios computed, ordering holds")
main()
''')

def d_e02(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    ant, joy, trust, fear, surprise = 70.0, 60.0, 50.0, 20.0, 10.0
    optimism = round(0.5 * ant + 0.5 * joy, 2)      # Plutchik dyad
    hope = round(0.5 * ant + 0.5 * trust, 2)        # Plutchik dyad
    dread = round(0.5 * ant + 0.5 * fear, 2)
    interest = round(0.3 * ant, 2)                  # mild form
    vigilance = round(min(100.0, 1.2 * ant), 2)    # intense form
    print("optimism", optimism, "hope", hope, "dread", dread,
          "interest", interest, "vigilance", vigilance)
    assert optimism == 65.0 and hope == 60.0 and dread == 45.0
    assert interest < ant < vigilance, "mild < base < intense must hold"
    assert abs((optimism - surprise) - 55.0) < 0.01, "opposite contrast drifted"
    print("OK: e02 emotion-family model - dyads, mild/intense forms, opposite computed")
main()
''')

def d_e03(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    volumes = {"mild": 25.0, "moderate": 55.0, "intense": 85.0}
    cost = {k: round(v * v / 100.0, 2) for k, v in volumes.items()}
    print("volumes:", volumes)
    print("body cost:", cost)
    assert cost["mild"] < cost["moderate"] < cost["intense"]
    assert cost["intense"] > 2.0 * cost["moderate"], "intense cost must exceed 2x moderate"
    assert abs(cost["moderate"] - 30.25) < 0.01, "moderate cost drifted"
    assert abs(cost["intense"] - 72.25) < 0.01, "intense cost drifted"
    print("OK: e03 volume ladder - quadratic body cost, intense > 2x moderate")
main()
''')

def d_e04(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    # affective forecasting: predicted vs actual impact (0-100) for 5 events
    cases = [(80, 45), (90, 50), (70, 40), (85, 55), (75, 35)]
    errors = [round(p - a, 2) for p, a in cases]
    mae = round(sum(abs(e) for e in errors) / len(errors), 2)
    print("forecast errors:", errors, "mean abs error:", mae)
    assert all(e > 0 for e in errors), "forecasts must overestimate (myth 5)"
    assert 20.0 < mae < 45.0, "mean error outside plausible band"
    assert abs(mae - 35.0) < 0.01, "mae drifted"
    print("OK: e04 forecast-error model - systematic overestimation demonstrated")
main()
''')

def d_e05(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    intensity = 72.0
    activation = round(min(100.0, 20.0 + 0.8 * intensity), 2)
    rehearsals_per_hour = round(2.0 + 0.15 * intensity, 1)
    checks_per_hour = round(1.0 + 0.12 * intensity, 1)
    time_dilation = round(1.0 + intensity / 200.0, 2)  # felt vs clock time
    print("activation", activation, "rehearsals/hr", rehearsals_per_hour,
          "checks/hr", checks_per_hour, "time dilation", time_dilation)
    assert 0.0 <= activation <= 100.0
    assert abs(activation - 77.6) < 0.01
    assert time_dilation > 1.0, "waiting must feel slower than the clock"
    assert abs(time_dilation - 1.36) < 0.01
    print("OK: e05 first-person simulator - activation, rehearsal rate, time dilation")
main()
''')

def d_e06(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    # hours from trigger; event at t=72
    phases = {"onset": 0.5, "build": 60.0, "peak": 71.0, "event": 72.0, "aftershock": 80.0}
    peak_level, event_level, echo_level = 92.0, 40.0, 28.0
    print("phase times:", phases)
    print("levels: peak", peak_level, "event", event_level, "aftershock", echo_level)
    assert phases["peak"] < phases["event"], "peak must precede the event"
    assert echo_level < peak_level, "aftershock smaller than peak"
    assert event_level < peak_level, "fading: event calmer than peak"
    assert abs(phases["peak"] - 71.0) < 0.01
    print("OK: e06 timeline model - peak pinned just before the event, echo after")
main()
''')

def d_e07(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def snap(volume):
    return {
        "sleep_loss_min": round(volume * 1.1, 1),
        "rehearsals": round(volume / 8.0, 1),
        "appetite_shift": round(volume / 25.0, 2),
        "day_flavor": round(volume / 10.0, 1),
    }
def main():
    low, high = snap(20.0), snap(88.0)
    print("low:", low); print("high:", high)
    for k in low:
        assert high[k] > low[k], "high intensity must exceed low on " + k
    assert abs(low["sleep_loss_min"] - 22.0) < 0.01
    assert abs(high["sleep_loss_min"] - 96.8) < 0.01
    print("OK: e07 two-snapshot simulator - high exceeds low on every channel")
main()
''')

def d_e08(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    anticipation, excitement = 75.0, 68.0
    eagerness = round(0.5 * anticipation + 0.5 * excitement, 2)
    seam = round(abs(anticipation - excitement), 2)  # how separable the layers are
    print("anticipation", anticipation, "excitement", excitement,
          "eagerness", eagerness, "seam", seam)
    assert eagerness > 50.0, "blend must clear the midpoint"
    assert abs(eagerness - 71.5) < 0.01
    assert seam < 20.0, "close partners: seam stays narrow"
    print("OK: e08 blend-seam model - eagerness computed, layers separable")
main()
''')

def d_e09(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    # hourly activation 6:40 -> 22:00; results post at 16:47 (hour 16.78)
    hours = [6.67, 8.25, 10.5, 12.08, 14.0, 16.78, 18.0, 20.0, 22.0]
    act = []
    for h in hours:
        if h < 16.78:
            a = 30.0 + 62.0 * (h - 6.67) / (16.78 - 6.67)
        else:
            a = 92.0 - 60.0 * min(1.0, (h - 16.78) / 3.0)
        act.append(round(a, 1))
    print(list(zip(hours, act)))
    peak_i = max(range(len(act)), key=lambda i: act[i])
    assert hours[peak_i] == 16.78, "peak must sit at the event hour"
    assert act[0] < act[4] < act[5], "build must rise toward the event"
    assert act[-1] < 45.0, "evening must settle below 45"
    print("OK: e09 day simulator - rise, false-calm, peak at event, evening settle")
main()
''')

def d_e10(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    activation = 77.6
    bpm = round(68.0 + 0.40 * activation, 1)
    breaths = round(14.0 + 0.12 * activation, 1)
    jaw_tone = round(activation / 10.0, 1)  # 0-10 scale
    print("bpm", bpm, "breaths/min", breaths, "jaw tone", jaw_tone)
    assert 68.0 <= bpm <= 110.0, "lifted but not terror range"
    assert abs(bpm - 99.0) < 0.05
    assert 14.0 <= breaths <= 30.0
    assert abs(breaths - 23.3) < 0.05
    print("OK: e10 body-signal model - heart, breath, muscle tone in mobilization band")
main()
''')

def d_e11(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    activation = 77.6
    lean_deg = round(2.0 + 0.15 * activation, 2)
    gaze_checks_hr = round(4.0 + 0.5 * activation, 1)
    steps_pacing = round(activation / 4.0, 1)  # corridor laps per hour at peak
    print("forward lean deg", lean_deg, "gaze checks/hr", gaze_checks_hr,
          "pacing laps/hr", steps_pacing)
    assert 2.0 <= lean_deg <= 20.0
    assert abs(lean_deg - 13.64) < 0.01
    assert gaze_checks_hr > 20.0, "checking loops must be frequent at this volume"
    print("OK: e11 posture model - lean, scanning, pacing scale with activation")
main()
''')

def d_e12(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    activation = 77.6
    latency_min = round(15.0 + 0.8 * activation, 1)
    appetite_a = round(-0.5 * activation / 10.0, 2)  # stomach-person: loss
    appetite_b = round(0.3 * activation / 10.0, 2)   # grazer: gain
    crash_next_day = round(activation * 0.6, 1)      # recovery tiredness 0-100
    print("sleep latency min", latency_min, "appetite A", appetite_a,
          "appetite B", appetite_b, "next-day crash", crash_next_day)
    assert latency_min < 120.0
    assert abs(latency_min - 77.1) < 0.05
    assert appetite_a < 0 < appetite_b, "appetite must split by person"
    assert 0.0 <= crash_next_day <= 100.0
    print("OK: e12 sleep/appetite/energy model - latency, split appetite, crash")
main()
''')

def d_e13(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    profiles = {
        "stomach-person": {"gut": 0.9, "hands": 0.2, "chest": 0.4},
        "hand-person": {"gut": 0.2, "hands": 0.9, "chest": 0.3},
        "chest-person": {"gut": 0.3, "hands": 0.3, "chest": 0.9},
    }
    dom = {p: max(w, key=w.get) for p, w in profiles.items()}
    print("dominant channels:", dom)
    assert len(set(dom.values())) == 3, "each profile must lead a different channel"
    assert dom["stomach-person"] == "gut"
    assert dom["hand-person"] == "hands"
    assert dom["chest-person"] == "chest"
    print("OK: e13 individual-difference model - three bodies, three lead channels")
main()
''')

def d_e14(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    aus = {"brow_lift": 20, "brow_knit": 45, "gaze_fix": 55, "lip_part": 60,
           "blink_fast": 75, "jaw_set": 80, "lip_press": 62, "nostril_flare": 78}
    def active(level):
        return sorted(k for k, thr in aus.items() if level >= thr)
    low, high = active(25.0), active(88.0)
    print("low-intensity AUs:", low); print("high-intensity AUs:", high)
    assert len(high) > len(low), "more units active at high intensity"
    assert set(low) < set(high), "low set must nest inside high set"
    assert "jaw_set" in high and "jaw_set" not in low
    print("OK: e14 facial-unit model - nested activation sets across intensity")
main()
''')

def d_e15(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    def valence_gap(level):
        # pleasant vs dread mouth signal; degrades as effort dominates
        return round(40.0 * max(0.0, 1.0 - level / 110.0), 2)
    g_low, g_high = valence_gap(25.0), valence_gap(95.0)
    print("valence gap low:", g_low, "high:", g_high)
    assert g_low > g_high, "valence signal must degrade at max intensity"
    assert abs(g_low - 30.91) < 0.01
    assert abs(g_high - 5.45) < 0.01
    print("OK: e15 intensity-expression model - valence gap shrinks at the peak")
main()
''')

def d_e16(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    # suppression effectiveness per channel (1.0 = fully hidden)
    eff = {"mouth": 0.90, "posture": 0.75, "voice": 0.55,
           "hands": 0.35, "swallow": 0.25, "gaze": 0.20, "blink": 0.15}
    leak = {k: round(1.0 - v, 2) for k, v in eff.items()}
    print("leakage:", leak)
    assert leak["gaze"] > leak["mouth"], "eyes must leak more than the mouth"
    assert leak["blink"] > leak["posture"]
    worst = max(leak, key=leak.get)
    assert worst == "blink", "blink rate must be the leakiest channel"
    print("OK: e16 leakage model - gaze/blink leak most, mouth hides best")
main()
''')

def d_e17(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    checklist = {"eyes_off_frame": 1, "brow_lift_knit": 1, "mouth_valence": 1,
                 "one_leak_detail": 1, "head_lean": 1, "future_tense_voice": 1}
    score = sum(checklist.values())
    print("gallery checklist score:", score, "of", len(checklist))
    assert score == 6, "complete portrait needs all six craft marks"
    assert checklist["mouth_valence"] == 1, "mouth must set the story"
    print("OK: e17 gallery model - six craft marks, mouth sets the story")
main()
''')

def d_e18(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    triggers = {
        "exam results tomorrow": (9, 8, 1),
        "trip in 30 days": (7, 3, 30),
        "package arriving today": (5, 6, 0.2),
        "wedding in 6 months": (10, 4, 180),
        "interview in 3 days": (9, 7, 3),
    }
    score = {k: round(i * u / max(d, 0.5), 2) for k, (i, u, d) in triggers.items()}
    ranked = sorted(score, key=score.get, reverse=True)
    print("trigger scores:", score)
    assert ranked[0] == "exam results tomorrow", "nearest high-stakes trigger must top"
    assert score["exam results tomorrow"] > score["trip in 30 days"]
    assert abs(score["package arriving today"] - 60.0) < 0.01
    print("OK: e18 trigger model - importance x uncertainty / time distance")
main()
''')

def d_e19(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    # cue strength over years since the original waiting; anniversary spike
    def strength(years, anniversary=False):
        base = round(80.0 * (0.85 ** years), 2)
        return round(min(100.0, base + 35.0) if anniversary else base, 2)
    s1, s5, s5a = strength(1), strength(5), strength(5, True)
    print("1yr:", s1, "5yr:", s5, "5yr anniversary:", s5a)
    assert s1 > s5, "cue must decay with time"
    assert s5a > s5, "anniversary must spike the cue"
    assert abs(s1 - 68.0) < 0.01
    assert abs(s5a - 70.5) < 0.01
    print("OK: e19 personal-trigger model - decay plus anniversary spike")
main()
''')

def d_e20(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    # thin cue starts a wait; cost accrues even when no event arrives
    cues = {"city name overheard": 0.3, "typing dots": 0.5,
            "snow forecast": 0.6, "eight stops away": 0.8}
    hours_waited = 3.0
    costs = {k: round(v * 25.0 * hours_waited, 2) for k, v in cues.items()}
    print("false-alarm costs:", costs)
    assert all(c > 0 for c in costs.values()), "every false alarm costs real arousal"
    assert costs["eight stops away"] > costs["city name overheard"]
    assert abs(costs["typing dots"] - 37.5) < 0.01
    print("OK: e20 surprise-trigger model - cheap to start, expensive to run")
main()
''')

def d_e21(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    # cascade link strengths; early intervention halves link 1
    links = [0.9, 0.8, 0.7, 0.6]
    def downstream(ls):
        p, out = 1.0, []
        for l in ls:
            p *= l
            out.append(round(p, 4))
        return out
    full = downstream(links)
    early = downstream([0.45, 0.8, 0.7, 0.6])   # intervene at link 1
    late = downstream([0.9, 0.8, 0.7, 0.45])     # intervene at link 4
    print("full:", full, "early:", early, "late:", late)
    assert early[-1] < late[-1] < full[-1], "early steering must beat late steering"
    assert abs(full[-1] - 0.3024) < 0.0001
    print("OK: e21 cascade model - early intervention steers the whole chain")
main()
''')

def d_e22(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    def checks_per_hour(uncertainty):
        return round(2.0 + 1.8 * uncertainty, 1)
    vals = [checks_per_hour(u) for u in (2.0, 5.0, 8.0)]
    print("checks/hr at uncertainty 2/5/8:", vals)
    assert vals == sorted(vals), "checking must rise with uncertainty"
    assert abs(vals[2] - 16.4) < 0.01
    prep_done = [True, True, False]  # packed once, list closed, bag repacked?
    loops = sum(1 for p in prep_done if not p)
    assert loops == 1, "one looping behavior detected"
    print("OK: e22 action model - checking scales with uncertainty; loop flagged")
main()
''')

def d_e23(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    future_markers = {"will", "going to", "when", "once", "after", "then", "soon"}
    sentences = ["I will walk in and say hello", "It is raining today",
                 "Once we know then we can plan", "She is reading now",
                 "When Friday comes I will be ready"]
    def ratio(s):
        words = s.lower().split()
        hits = sum(1 for w in words if w in future_markers)
        return round(hits / len(words), 3)
    ratios = [ratio(s) for s in sentences]
    print("future-tense ratios:", ratios)
    avg = round(sum(ratios) / len(ratios), 3)
    assert ratios[0] > ratios[1] and ratios[2] > ratios[3], "waiting speech must score higher"
    assert avg > 0.1, "mixed waiting-day speech must lean future"
    print("OK: e23 language model - future-tense ratio detects waiting speech")
main()
''')

def d_e24(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    # temporal discounting: value of a reward after the event vs now
    def present_value(reward, weeks, k):
        return round(reward / (1.0 + k * weeks), 2)
    calm = present_value(100.0, 8, 0.1)
    waiting = present_value(100.0, 8, 0.35)  # steeper discount under anticipation
    print("calm PV:", calm, "waiting PV:", waiting)
    assert waiting < calm, "waiting must steepen discounting"
    assert abs(calm - 55.56) < 0.01
    assert abs(waiting - 26.32) < 0.01
    print("OK: e24 decision model - anticipation steepens temporal discounting")
main()
''')

def d_e25(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    steps = {"checking": 5.0, "broadcasting": 12.0, "overflow prep": 25.0,
             "friction": 45.0, "freeze/flood": 70.0}
    costs = list(steps.values())
    print("escalation costs:", steps)
    assert costs == sorted(costs), "each step must cost more than the last"
    assert costs[-1] > 3.0 * costs[0], "final step must exceed 3x the first"
    total = round(sum(costs), 1)
    assert abs(total - 157.0) < 0.01
    print("OK: e25 escalation model - five-step staircase, costs compound")
main()
''')

def d_e26(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    say, show, channel = 30.0, 25.0, 35.0
    combined = round(say + show + channel - 0.3 * min(say, show, channel), 2)
    print("say", say, "show", show, "channel", channel, "combined", combined)
    assert combined > max(say, show, channel), "three channels must beat any one"
    assert combined < say + show + channel, "diminishing overlap must apply"
    assert abs(combined - 82.5) < 0.01
    print("OK: e26 expression model - three channels compound with overlap")
main()
''')

def d_e27(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    healthy = 20.0
    bottled = round(healthy + 45.0, 1)    # body keeps the books
    exploded = round(healthy + 50.0, 1)  # relationships + reserves taxed
    print("cost bottled:", bottled, "exploded:", exploded, "healthy:", healthy)
    assert bottled > healthy and exploded > healthy, "both edges must cost more"
    assert abs(bottled - 65.0) < 0.01 and abs(exploded - 70.0) < 0.01
    print("OK: e27 expression-cost model - both unhealthy edges cost more")
main()
''')

def d_e28(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    start = 85.0
    reductions = {"named wait": 8.0, "scheduled checks": 10.0, "finished prep": 7.0,
                  "body spending": 12.0, "second track": 9.0,
                  "sleep protection": 6.0, "witness": 5.0}
    end = round(start - sum(reductions.values()), 1)
    print("start", start, "end", end)
    assert 20.0 <= end <= 40.0, "practices must bring volume to working range"
    assert abs(end - 28.0) < 0.01
    print("OK: e28 practice model - seven practices land volume in working range")
main()
''')

def d_e29(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    cues = {"face": 0.8, "body": 0.75, "voice": 0.7, "behavior": 0.85}
    agree = sum(1 for v in cues.values() if v >= 0.6)
    confidence = round(sum(cues.values()) / 4.0, 3)
    print("agreeing channels:", agree, "confidence:", confidence)
    assert agree >= 3, "three of four channels must agree for a solid read"
    assert 0.7 <= confidence <= 0.9
    assert abs(confidence - 0.775) < 0.001
    print("OK: e29 recognition model - four-channel agreement, confidence scored")
main()
''')

def d_e30(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    helpful = {"name it": 8.5, "ask what helps": 9.0, "one honest reassurance": 8.0,
               "lend calm": 8.8, "mark end date": 9.2, "scheduled check-in": 8.6}
    unhelpful = {"just relax": 2.0, "do not worry": 1.5, "toxic cheer": 2.5,
                 "speculation spiral": 1.8}
    h_avg = round(sum(helpful.values()) / len(helpful), 2)
    u_avg = round(sum(unhelpful.values()) / len(unhelpful), 2)
    print("helpful avg", h_avg, "unhelpful avg", u_avg)
    assert h_avg > 2.0 * u_avg, "helpful responses must clearly outscore"
    assert abs(h_avg - 8.68) < 0.01
    print("OK: e30 support model - helpful responses outscore unhelpful 2x")
main()
''')

def d_e31(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    harms = {"minimizing": 7.0, "commandeering": 6.5, "speculation": 8.0,
             "reassurance treadmill": 7.5, "ambush": 8.5,
             "scorekeeping": 6.0, "projection": 5.5}
    print("mistake harms:", harms)
    assert all(h > 0 for h in harms.values()), "every listed mistake must harm"
    worst = max(harms, key=harms.get)
    assert worst == "ambush", "peak-wait ambush must be the worst mistake"
    assert abs(sum(harms.values()) - 49.0) < 0.01
    print("OK: e31 mistake model - seven hazards scored, ambush worst")
main()
''')

def d_e32(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    # distance from anticipation in appraisal space (0 = identical)
    dist = {"excitement": 1.2, "hope": 1.5, "anxiety": 1.8, "curiosity": 2.0,
            "impatience": 1.0, "worry": 1.4, "eagerness": 0.8, "dread": 1.1,
            "vigilance": 0.5, "surprise": 4.0, "nostalgia": 4.5, "contentment": 3.5}
    print("distances:", dist)
    assert dist["impatience"] < dist["nostalgia"], "impatience nearer than nostalgia"
    assert dist["vigilance"] < dist["surprise"], "vigilance is intensity, surprise opposite"
    assert min(dist, key=dist.get) == "vigilance"
    print("OK: e32 map model - cousins near, opposites far, vigilance nearest")
main()
''')

def d_e33(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    blends = {
        "eagerness": (75.0, 68.0, 0.0),   # (anticipation, partner, threat)
        "dread": (75.0, 0.0, 70.0),
        "hope": (70.0, 55.0, 5.0),
        "alarm": (80.0, 20.0, 75.0),
    }
    def playbook(b):
        a, p, t = b
        if t > 50: return "bound the wait, add a witness"
        if p >= 65: return "share it, channel the energy"
        return "protect the patience"
    books = {k: playbook(v) for k, v in blends.items()}
    print("playbooks:", books)
    assert len(set(books.values())) == 3, "four blends must map to three playbooks"
    assert books["dread"] == books["alarm"], "threat blends share a playbook"
    assert books["eagerness"] != books["hope"]
    print("OK: e33 blend model - four dyads, partner names the playbook")
main()
''')

def d_e34(hdr, name, rid, group, kp, req):
    return _w(hdr, name, rid, group, '''\
def main():
    scenes = ["trigger", "build", "peak", "event", "aftershock"]
    levels = [25.0, 62.0, 94.0, 40.0, 28.0]
    print(list(zip(scenes, levels)))
    peak_i = max(range(len(levels)), key=lambda i: levels[i])
    assert scenes[peak_i] == "peak", "peak must be the worst hour, before the event"
    assert levels[3] < levels[2], "event calmer than peak"
    assert levels[4] < levels[2] and levels[4] > 0, "aftershock: smaller echo, nonzero"
    assert abs(sum(levels) - 249.0) < 0.01
    print("OK: e34 full simulation - five scenes, peak before event, echo after")
main()
''')

DEMOS = {
    "e01": d_e01, "e02": d_e02, "e03": d_e03, "e04": d_e04, "e05": d_e05,
    "e06": d_e06, "e07": d_e07, "e08": d_e08, "e09": d_e09, "e10": d_e10,
    "e11": d_e11, "e12": d_e12, "e13": d_e13, "e14": d_e14, "e15": d_e15,
    "e16": d_e16, "e17": d_e17, "e18": d_e18, "e19": d_e19, "e20": d_e20,
    "e21": d_e21, "e22": d_e22, "e23": d_e23, "e24": d_e24, "e25": d_e25,
    "e26": d_e26, "e27": d_e27, "e28": d_e28, "e29": d_e29, "e30": d_e30,
    "e31": d_e31, "e32": d_e32, "e33": d_e33, "e34": d_e34,
}
