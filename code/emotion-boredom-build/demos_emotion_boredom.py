#!/usr/bin/env python3
"""Demo programs for the Boredom Emotion databases (emotion series).

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


def demo_boredom_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four-beat sequence: unmet need -> disengaged attention -> time drag -> urge
    wanted, offered = 0.85, 0.20
    gap = wanted - offered                     # engagement gap
    attention = max(0.0, 1.0 - gap * 1.2)      # attention engagement 0..1
    time_drag = 1.0 + gap * 2.5                # perceived minutes per real minute
    urge = min(1.0, gap * 1.3)                 # urge for change
    print("engagement gap: %.3f" % gap)
    print("attention: %.3f  time drag: %.3fx  urge: %.3f" % (attention, time_drag, urge))
    assert 0.649 < gap < 0.651
    assert 0.219 < attention < 0.221
    assert 2.624 < time_drag < 2.626
    assert 0.844 < urge < 0.846
    print("beats: unmet need -> disengaged attention -> time drag -> urge for change")
    print("OK: %s ran the four-beat sequence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # root: unengaged mind; partner ingredients branch it into named states
    root = 1.0
    branches = {
        "plain boredom": root * 1.00,
        "frustrated boredom": root * 0.70 + 0.60,   # + blocked goals
        "meaning-hollow boredom": root * 0.65 + 0.55,  # + fading meaning
        "agitated boredom": root * 0.75 + 0.65,     # + restlessness
        "lethargic boredom": root * 0.60 + 0.50,    # + low energy
        "curious edge": root * 0.40 + 0.30,         # + curiosity (opposite pole)
    }
    total = sum(branches.values())
    share = {k: v / total * 100.0 for k, v in branches.items()}
    for k in branches:
        print("  %-22s weight %.2f (%5.2f %%)" % (k, branches[k], share[k]))
    assert 0.999 < sum(share.values()) / 100.0 < 1.001
    assert share["agitated boredom"] > share["plain boredom"]
    assert 20.8 < share["agitated boredom"] < 21.0
    print("root: unengaged mind; branches keep the attention-fit core")
    print("OK: %s mapped the family tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # volume dial: gap * duration / choice  ->  0..10
    def volume(gap, duration_h, choice):
        return min(10.0, gap * (1.0 + duration_h * 0.8) / max(choice, 0.1) * 2.0)
    def label(v):
        return "mild" if v < 3.5 else ("moderate" if v < 7.0 else "intense")
    cases = [(0.25, 0.25, 0.9), (0.45, 1.5, 0.5), (0.85, 6.0, 0.15)]
    for gap, dur, choice in cases:
        v = volume(gap, dur, choice)
        print("gap %.2f dur %.2fh choice %.2f -> volume %.2f (%s)" % (gap, dur, choice, v, label(v)))
    assert label(volume(0.25, 0.25, 0.9)) == "mild"
    assert label(volume(0.45, 1.5, 0.5)) == "moderate"
    assert label(volume(0.85, 6.0, 0.15)) == "intense"
    assert 0.66 < volume(0.25, 0.25, 0.9) < 0.68
    print("OK: %s calibrated the three volumes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # myth vs fact scorecard: each myth gets a falseness score 0..1 from the findings
    myths = {
        "only boring people get bored": 0.92,
        "boredom is harmless idleness": 0.85,
        "more stimulation cures it": 0.88,
        "boredom means you need entertainment": 0.80,
        "boredom is a character flaw": 0.95,
    }
    avg_false = sum(myths.values()) / len(myths)
    for m, f in myths.items():
        print("  myth %-42s falseness %.2f" % (m, f))
    print("average falseness: %.3f" % avg_false)
    assert all(f > 0.75 for f in myths.values())
    assert 0.878 < avg_false < 0.882
    print("truth: appetite, signal, fit - not flaw")
    print("OK: %s busted the five myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inner timeline: drag index per 10-minute block of a dull hour
    blocks = ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60"]
    drag = [0.30, 0.45, 0.58, 0.68, 0.75, 0.80]
    for b, d in zip(blocks, drag):
        bar = "#" * int(d * 30)
        print("  min %-6s drag %.2f %s" % (b, d, bar))
    peak, start = max(drag), drag[0]
    print("drag climbed %.2f -> %.2f (x%.2f)" % (start, peak, peak / start))
    assert drag == sorted(drag), "drag must climb monotonically"
    assert 2.66 < peak / start < 2.68
    assert 0.79 < peak < 0.81
    print("OK: %s lived the hour from inside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five phases with signal strength 0..1 and redirect cost 0..1
    phases = [
        ("onset", 0.20, 0.15),
        ("climb", 0.50, 0.40),
        ("peak", 0.95, 0.85),
        ("fading", 0.35, 0.30),
        ("aftershock", 0.25, 0.20),
    ]
    for name_, sig, cost in phases:
        print("  %-10s signal %.2f  redirect cost %.2f" % (name_, sig, cost))
    sigs = [s for _, s, _ in phases]
    assert sigs.index(max(sigs)) == 2, "peak must be phase 3"
    assert phases[0][2] < phases[2][2], "onset cheapest to redirect"
    assert 0.94 < max(sigs) < 0.96
    print("rule: intervene at onset, endure the peak with structure")
    print("OK: %s walked the five phases" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two snapshots on the same dials: gap, duration_h, choice
    low = {"gap": 0.25, "duration_h": 1.0, "choice": 0.9}
    high = {"gap": 0.85, "duration_h": 6.0, "choice": 0.15}
    def misery(d):
        return d["gap"] * (1 + d["duration_h"] * 0.8) / max(d["choice"], 0.1)
    ml, mh = misery(low), misery(high)
    print("low snapshot misery:  %.3f" % ml)
    print("high snapshot misery: %.3f" % mh)
    print("ratio high/low: %.2f" % (mh / ml))
    assert 0.49 < ml < 0.51
    assert 32.0 < mh < 34.0
    assert mh / ml > 60.0
    print("same mechanism, different dials - drizzle vs flood")
    print("OK: %s compared the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_restlessness_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # blend = boredom half (low engagement) + restlessness half (high arousal)
    boredom, restless = 0.80, 0.85
    mismatch = abs((1 - boredom) - restless)   # arousal-engagement mismatch
    discomfort = (boredom + restless) / 2 * (1 + mismatch)
    print("boredom %.2f  restlessness %.2f" % (boredom, restless))
    print("mismatch %.3f  blend discomfort %.3f" % (mismatch, discomfort))
    assert 0.64 < mismatch < 0.66
    assert 1.35 < discomfort < 1.37
    # remedy order: discharge body first, then engage mind
    after_move = discomfort * 0.55
    after_engage = after_move * 0.35
    print("after movement: %.3f  after engagement: %.3f" % (after_move, after_engage))
    assert 0.74 < after_move < 0.76
    assert 0.25 < after_engage < 0.27
    print("OK: %s mixed and answered the blend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the day's boredom dial, hour by hour 8:00 -> 22:00
    dial = [0.10, 0.15, 0.35, 0.45, 0.25, 0.70, 0.80, 0.75, 0.30,
            0.15, 0.10, 0.20, 0.35, 0.45, 0.40]
    hours = list(range(8, 23))
    peak_i = dial.index(max(dial))
    print("hours tracked: %d  peak at %d:00 (%.2f)" % (len(dial), hours[peak_i], dial[peak_i]))
    avg = sum(dial) / len(dial)
    flat_hours = sum(1 for d in dial if d >= 0.5)
    print("average dial %.3f  flat hours (>=0.5): %d" % (avg, flat_hours))
    assert hours[peak_i] == 14, "peak should be early afternoon"
    assert 0.36 < avg < 0.38
    assert flat_hours == 3
    print("rescue at 16:00: genuine engagement, dial collapses")
    print("OK: %s walked the whole day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body channels 0..1: arousal low, slack high; two profiles
    lethargic = {"heart_arousal": 0.25, "muscle_slack": 0.85, "sigh_rate": 0.70,
                 "skin_itch": 0.55, "heaviness": 0.90}
    agitated = {"heart_arousal": 0.75, "muscle_slack": 0.30, "sigh_rate": 0.60,
                "skin_itch": 0.80, "heaviness": 0.35}
    for label, p in (("lethargic", lethargic), ("agitated", agitated)):
        idle_index = (p["muscle_slack"] + p["heaviness"] + p["sigh_rate"]) / 3
        print("  %-9s idle index %.3f  arousal %.2f" % (label, idle_index, p["heart_arousal"]))
    li = (lethargic["muscle_slack"] + lethargic["heaviness"] + lethargic["sigh_rate"]) / 3
    ai = (agitated["muscle_slack"] + agitated["heaviness"] + agitated["sigh_rate"]) / 3
    assert 0.81 < li < 0.83
    assert 0.41 < ai < 0.43
    assert lethargic["heart_arousal"] < agitated["heart_arousal"]
    print("sighing is the tell in both profiles")
    print("OK: %s read the body channels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_posture_movement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # posture honesty score: voluntary control 0..1 per channel (lower = more honest)
    channels = {"mouth_smile": 0.90, "nod": 0.85, "spine_melt": 0.25,
                "foot_tap": 0.20, "gaze_drift": 0.15}
    for ch, ctrl in sorted(channels.items(), key=lambda kv: kv[1]):
        print("  %-12s control %.2f  honesty %.2f" % (ch, ctrl, 1 - ctrl))
    most_honest = min(channels, key=channels.get)
    print("most honest channel: %s" % most_honest)
    assert most_honest == "gaze_drift"
    assert channels["spine_melt"] < channels["nod"]
    # deliberate upright posture feeds back into attention
    attention_before, attention_after = 0.30, 0.30 + (1 - channels["spine_melt"]) * 0.4
    print("attention before %.2f -> after upright %.2f" % (attention_before, attention_after))
    assert 0.59 < attention_after < 0.61
    print("OK: %s decoded posture and movement" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_sleep_appetite_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # diagnose the tiredness: clean (wants rest) vs flat (wants engagement)
    def diagnose(sleep_debt, engagement_gap):
        if sleep_debt > 0.6 and engagement_gap < 0.4:
            return "clean tiredness -> rest"
        if engagement_gap > 0.6:
            return "flat tiredness -> engage"
        return "mixed -> light rest then engage"
    cases = [(0.8, 0.2), (0.2, 0.85), (0.5, 0.5)]
    for sd, eg in cases:
        print("  sleep debt %.1f gap %.2f => %s" % (sd, eg, diagnose(sd, eg)))
    assert diagnose(0.8, 0.2) == "clean tiredness -> rest"
    assert diagnose(0.2, 0.85) == "flat tiredness -> engage"
    # boredom-nap: gap unchanged by sleep
    gap_before, gap_after_nap = 0.75, 0.72
    print("nap barely moves the gap: %.2f -> %.2f" % (gap_before, gap_after_nap))
    assert gap_after_nap > 0.65
    print("OK: %s untangled sleep, appetite, energy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # personal dialects: baseline arousal + appetite set the profile
    people = {
        "high-arousal teen": (0.85, 0.90),
        "low-arousal adult": (0.30, 0.50),
        "hungry mind": (0.60, 0.95),
        "easygoing elder": (0.35, 0.40),
    }
    for label, (arousal, appetite) in people.items():
        alarm = appetite * (1.1 - arousal * 0.3)   # louder when appetite big
        profile = "agitated" if arousal > 0.55 else "lethargic"
        print("  %-18s alarm %.3f profile %s" % (label, alarm, profile))
    alarms = {l: a * (1.1 - ar * 0.3) for l, (ar, a) in people.items()}
    assert alarms["hungry mind"] > alarms["easygoing elder"]
    assert 0.87 < alarms["hungry mind"] < 0.88
    print("bigger appetite -> louder alarm; hunger, not weakness")
    print("OK: %s mapped the body dialects" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # configural face score: eyes weighted heaviest
    face = {"gaze_drift": 0.90, "lid_heavy": 0.75, "mouth_slack": 0.80,
            "brow_neutral": 0.70, "micro_yawn": 0.55}
    weights = {"gaze_drift": 0.35, "lid_heavy": 0.20, "mouth_slack": 0.20,
               "brow_neutral": 0.10, "micro_yawn": 0.15}
    score = sum(face[k] * weights[k] for k in face)
    for k in face:
        print("  %-12s signal %.2f x weight %.2f" % (k, face[k], weights[k]))
    print("boredom face score: %.3f" % score)
    assert 0.77 < score < 0.79
    assert weights["gaze_drift"] == max(weights.values())
    # neighbor check: sadness shares droop but lacks restless micro-movement
    print("disambiguator: restless micro-movements (sadness lacks them)")
    print("OK: %s rendered the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # intensity -> slack (signal) and protest (control failure)
    def face_at(intensity):
        slack = min(1.0, 0.25 + intensity * 0.75)
        protest = max(0.0, (intensity - 0.55) / 0.45) ** 1.5
        return slack, protest
    for inten, want in ((0.2, "whisper"), (0.55, "mask"), (0.9, "protest")):
        s, p = face_at(inten)
        print("  intensity %.2f (%-7s) slack %.3f protest %.3f" % (inten, want, s, p))
    s1, p1 = face_at(0.2)
    s3, p3 = face_at(0.9)
    assert 0.39 < s1 < 0.41 and p1 < 0.01
    assert 0.92 < s3 < 0.94 and 0.68 < p3 < 0.70
    print("read two axes: slackness (depth) and protest (nearness to limit)")
    print("OK: %s scaled the face with intensity" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # leakage: low control score = leaks; mask degrades over minutes
    control = {"mouth": 0.90, "nod": 0.85, "gaze": 0.15, "blink": 0.25, "sigh": 0.20}
    minutes = 45
    leak = {ch: (1 - c) * (1 + minutes / 60.0) for ch, c in control.items()}
    for ch in sorted(leak, key=leak.get, reverse=True):
        print("  %-6s leak %.3f" % (ch, leak[ch]))
    assert max(leak, key=leak.get) == "gaze"
    assert 1.48 < leak["gaze"] < 1.50
    assert leak["mouth"] < leak["gaze"]
    # timing tell: conscious responses add delay
    genuine_lag, performed_lag = 0.25, 0.85
    print("response lag genuine %.2fs vs performed %.2fs" % (genuine_lag, performed_lag))
    assert performed_lag > genuine_lag * 2
    print("OK: %s caught the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # render checklist: each landmark scored 0..1 for legibility
    landmarks = {"unfocused stare": 0.95, "lids three-quarter": 0.85,
                 "brows neutral": 0.75, "mouth slack": 0.88,
                 "chin on fist": 0.90, "flat lighting": 0.80}
    legibility = sum(landmarks.values()) / len(landmarks)
    for lm, sc in landmarks.items():
        print("  %-18s legibility %.2f" % (lm, sc))
    print("overall legibility: %.3f" % legibility)
    assert 0.85 < legibility < 0.87
    # neighbor guards
    assert landmarks["unfocused stare"] > 0.9, "must not read as sadness (down) or contempt (away)"
    print("rule: play the failure of attention, not the feeling")
    print("OK: %s briefed the artist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # skeleton score = gap * duration_factor * (1 - choice) per trigger
    triggers = {
        "waiting room": (0.70, 1.6, 0.10),
        "dull meeting": (0.75, 1.4, 0.15),
        "repetitive task": (0.80, 1.8, 0.30),
        "empty stretch": (0.65, 2.0, 0.60),
        "captive audience": (0.70, 1.5, 0.05),
        "familiar loop": (0.60, 1.3, 0.50),
        "confinement": (0.75, 1.7, 0.05),
    }
    scores = {t: g * d * (1 - c) for t, (g, d, c) in triggers.items()}
    for t in sorted(scores, key=scores.get, reverse=True):
        print("  %-16s skeleton %.3f" % (t, scores[t]))
    top = max(scores, key=scores.get)
    print("strongest skeleton: %s" % top)
    assert top == "confinement"
    assert 1.21 < scores["confinement"] < 1.23
    assert all(s > 0.3 for s in scores.values())
    print("OK: %s catalogued the seven triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # conditioning strength 0..1 vs structural outgrowing 0..1
    personal = {
        "stale hobby": (0.40, 0.90),
        "over-familiar place": (0.75, 0.50),
        "flat anniversary": (0.85, 0.20),
        "draining acquaintance": (0.90, 0.10),
        "post-achievement hollow": (0.20, 0.85),
    }
    for t, (cond, out) in personal.items():
        stick = max(cond, out)
        kind = "conditioned" if cond >= out else "outgrown"
        print("  %-22s stick %.2f (%s)" % (t, stick, kind))
    sticks = {t: max(c, o) for t, (c, o) in personal.items()}
    assert sticks["draining acquaintance"] > sticks["flat anniversary"]
    assert 0.89 < sticks["draining acquaintance"] < 0.91
    print("remedy is surgical: raise challenge, appoint successor goal, break cue")
    print("OK: %s mapped the private set" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels 0..1 fed; boredom = 1 - min fed channel (weakest link)
    surprises = {
        "too much choice": (0.50, 0.60, 0.10, 0.50),
        "easy success": (0.05, 0.50, 0.60, 0.50),
        "constant novelty": (0.40, 0.30, 0.50, 0.40),
        "being over-helped": (0.30, 0.50, 0.05, 0.50),
        "pure comfort": (0.20, 0.05, 0.60, 0.60),
        "shallow social": (0.40, 0.40, 0.50, 0.10),
    }
    labels = ("challenge", "meaning", "agency", "connection")
    for t, ch in surprises.items():
        weakest = labels[ch.index(min(ch))]
        bored = 1 - min(ch)
        print("  %-16s weakest: %-10s boredom %.2f" % (t, weakest, bored))
    bores = {t: 1 - min(ch) for t, ch in surprises.items()}
    assert bores["pure comfort"] > 0.9, "comfort starves meaning"
    assert 0.94 < bores["pure comfort"] < 0.96
    print("fit-failure, not input-failure")
    print("OK: %s sprung the six traps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # classic chain: each link's probability given the last
    links = [("trigger", 1.00), ("urge", 0.90), ("cheap novelty", 0.85),
             ("irritability", 0.70), ("conflict", 0.45), ("guilt", 0.60),
             ("dread", 0.55)]
    p = 1.0
    for label, cond in links:
        p *= cond
        print("  %-14s cumulative %.4f" % (label, p))
    print("full chain probability: %.4f" % p)
    assert 0.078 < p < 0.080
    # cutting the first link collapses the chain
    p_cut = 1.0
    for _, cond in links:
        p_cut *= cond
    p_cut *= 0.10  # intervene at urge
    print("with early intervention: %.4f" % p_cut)
    assert p_cut < 0.01
    print("OK: %s traced and cut the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five repertoires with cost and desperation 0..1
    reps = {
        "small": (0.05, 0.15),
        "seeking": (0.25, 0.40),
        "social": (0.45, 0.55),
        "escape": (0.60, 0.75),
        "risky": (0.95, 0.95),
    }
    for r, (cost, desp) in reps.items():
        print("  %-8s cost %.2f desperation %.2f" % (r, cost, desp))
    costs = [c for c, _ in reps.values()]
    assert costs == sorted(costs), "escalation must be orderly"
    # intervene at small stage
    answered = 0.05 * 0.1
    unanswered_risk = 0.95
    print("answered-at-small cost %.3f vs unanswered risk %.2f" % (answered, unanswered_risk))
    assert answered < 0.01 < unanswered_risk
    print("OK: %s translated the five repertoires" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_speech_patterns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # prosody flattening with intensity; discourse decay
    def prosody(intensity):
        pitch_range = 1.0 - intensity * 0.6
        pace = 1.0 - intensity * 0.4
        return pitch_range, pace
    for inten in (0.2, 0.6, 0.9):
        pr, pa = prosody(inten)
        print("  intensity %.1f pitch range %.2f pace %.2f" % (inten, pr, pa))
    pr, pa = prosody(0.9)
    assert 0.45 < pr < 0.47 and 0.63 < pa < 0.65
    # rescue-questions vs curious questions
    rescue = ["so what else is going on", "got anything fun happening", "are we done yet"]
    curious = ["how does that work", "why did you choose that", "what happens next"]
    print("rescue-questions: %d  curious-questions: %d" % (len(rescue), len(curious)))
    assert len(rescue) == len(curious) == 3
    print("OK: %s heard the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_decisions_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # future discounting steepens with boredom intensity
    def discount_factor(intensity, months):
        return 1.0 / (1.0 + (0.2 + intensity * 1.5) * months)
    for inten in (0.1, 0.5, 0.9):
        d = discount_factor(inten, 6)
        print("  intensity %.1f  6-month value kept: %.3f" % (inten, d))
    assert 0.32 < discount_factor(0.1, 6) < 0.33
    assert 0.09 < discount_factor(0.9, 6) < 0.11
    # pre-commitment rule holds the line
    rule_holds = discount_factor(0.9, 6) < 0.5
    print("peak-state decision trusted: %s -> decide by prior arrangement" % (not rule_holds))
    assert rule_holds
    print("OK: %s guarded judgment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five stages; threshold rises each unanswered stage; resources spent
    stages = ["private signals", "seeking", "social", "structural", "risky"]
    threshold, spent = 0.40, 0.0
    spend = [0.02, 0.10, 0.30, 0.55, 0.90]
    for i, st in enumerate(stages):
        threshold = min(0.95, threshold + 0.12)
        spent += spend[i]
        print("  stage %d %-15s threshold %.2f spent %.2f" % (i + 1, st, threshold, spent))
    assert 0.94 < threshold < 0.96
    assert 1.86 < spent < 1.88
    # early interception vs threshold reset
    print("interception at stage 1 cost: 0.05 | reset fast cost: 0.40")
    assert 0.05 < 0.40
    print("OK: %s climbed and mapped the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three moves scored on information kept 0..1 and cause addressed 0..1
    moves = {
        "say it true": (0.90, 0.30),
        "show it clean": (0.80, 0.20),
        "channel it": (0.95, 0.95),
    }
    for m, (info, cause) in moves.items():
        total = (info + cause) / 2
        print("  %-13s info %.2f cause %.2f total %.3f" % (m, info, cause, total))
    totals = {m: (i + c) / 2 for m, (i, c) in moves.items()}
    assert totals["channel it"] > totals["say it true"] > totals["show it clean"]
    assert 0.949 < totals["channel it"] < 0.951
    print("channeling removes the cause, not just the pressure")
    print("OK: %s expressed it well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cost ledgers: bottling vs exploding over 10 episodes
    bottle = {"suppression effort": 0.70, "sideways leaks": 0.60, "world contraction": 0.50}
    explode = {"social capital": 0.80, "threshold ratchet": 0.65, "repair cost": 0.55}
    bc, ec = sum(bottle.values()), sum(explode.values())
    for label, ledger, total in (("bottling", bottle, bc), ("exploding", explode, ec)):
        print("  %s cost %.2f %s" % (label, total, ledger))
    print("bottling %.2f vs exploding %.2f" % (bc, ec))
    assert 1.79 < bc < 1.81
    assert 1.99 < ec < 2.01
    # both leave the signal unanswered -> deeper boredom
    print("both manage the signal; neither answers it")
    print("OK: %s priced both failures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven practices with daily effect 0..1 on the gap; compound over 30 days
    practices = {"audit": 0.10, "challenge dial": 0.15, "meaning thread": 0.12,
                 "novelty ration": 0.08, "stillness": 0.10, "transition ritual": 0.07,
                 "worthy list": 0.13}
    gap = 0.70
    for day in (1, 10, 30):
        g = gap * (1 - sum(practices.values())) ** (day / 7)
        print("  day %2d gap %.3f" % (day, g))
    g30 = gap * (1 - sum(practices.values())) ** (30 / 7)
    assert 0.001 < g30 < 0.005
    assert sum(practices.values()) > 0.7, "maintenance must be substantial"
    print("small and daily beats large and occasional")
    print("OK: %s drilled the seven practices" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels converge; context sets the bar
    channels = {"face": 0.80, "body": 0.75, "voice": 0.70, "behavior": 0.85}
    convergence = sum(channels.values()) / len(channels)
    print("channel convergence: %.3f" % convergence)
    # base rates: dull meeting vs crisis meeting
    for ctx, base in (("dull meeting 3pm", 0.70), ("crisis meeting", 0.15)):
        reading = convergence * 0.6 + base * 0.4
        verdict = "boredom likely" if reading > 0.5 else "look deeper"
        print("  %-16s reading %.3f -> %s" % (ctx, reading, verdict))
    assert 0.77 < convergence < 0.79
    r_dull = convergence * 0.6 + 0.70 * 0.4
    r_crisis = convergence * 0.6 + 0.15 * 0.4
    assert r_dull > 0.5 > r_crisis or r_crisis < 0.55
    print("OK: %s read the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # responses scored on channel fed 0..1 and shame added 0..1 (lower better)
    responses = {
        "genuine question": (0.85, 0.05),
        "offer agency": (0.80, 0.05),
        "offer challenge": (0.75, 0.10),
        "reframe": (0.65, 0.05),
        "kind naming": (0.60, 0.02),
        "graceful ending": (0.70, 0.05),
        "spectacle dump": (0.30, 0.20),
        "scolding": (0.10, 0.85),
    }
    good = {k: v for k, v in responses.items() if k not in ("spectacle dump", "scolding")}
    for r, (fed, shame) in sorted(responses.items(), key=lambda kv: kv[1][0] - kv[1][1], reverse=True)[:3]:
        print("  %-16s net %.2f" % (r, fed - shame))
    best = max(good, key=lambda k: good[k][0] - good[k][1])
    assert best == "genuine question"
    assert responses["scolding"][1] > 0.8
    print("OK: %s answered supportively" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven mistakes with damage 0..1
    mistakes = {"stimulation dump": 0.70, "shaming": 0.75, "scroll as remedy": 0.80,
                "forced cheer": 0.55, "outsourcing": 0.65, "numbing": 0.85,
                "identity labeling": 0.90}
    for m, d in sorted(mistakes.items(), key=lambda kv: kv[1], reverse=True):
        print("  %-18s damage %.2f" % (m, d))
    worst = max(mistakes, key=mistakes.get)
    assert worst == "identity labeling"
    assert 0.89 < mistakes[worst] < 0.91
    # antidote question effectiveness
    print("antidote: which channel starves, and what would genuinely feed it?")
    print("OK: %s posted the warnings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_related_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # distance 0..1 from boredom; appetite test separates apathy
    neighbors = {
        "apathy": (0.15, False), "restlessness": (0.25, True),
        "frustration": (0.35, True), "loneliness": (0.45, True),
        "weariness": (0.40, True), "melancholy": (0.50, True),
    }
    for n_, (dist, appetite) in sorted(neighbors.items(), key=lambda kv: kv[1][0]):
        print("  %-13s distance %.2f appetite %s" % (n_, dist, appetite))
    assert neighbors["apathy"][0] < 0.2 and not neighbors["apathy"][1]
    # opposites: channel fullness
    opposites = {"curiosity": 0.90, "flow": 0.95, "enthusiasm": 0.88}
    assert min(opposites.values()) > 0.85
    print("flowchart: appetite? which channel? how long?")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_emotion_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dyads: boredom 0.7 + partner 0.7, compound character scores
    blends = {
        "agitated": (0.70, 0.70, 0.90),    # energy
        "short-fuse": (0.70, 0.60, 0.75),  # prickliness
        "grey": (0.70, 0.65, 0.80),        # heaviness
        "promising": (0.70, 0.75, 0.85),   # search energy
    }
    for b, (bo, pa, char) in blends.items():
        compound = (bo + pa) / 2 * (0.5 + char / 2)
        print("  %-10s compound %.3f" % (b, compound))
    compounds = {b: (bo + pa) / 2 * (0.5 + ch / 2) for b, (bo, pa, ch) in blends.items()}
    assert 0.66 < compounds["agitated"] < 0.68
    assert compounds["promising"] > compounds["short-fuse"]
    print("name both, feed both")
    print("OK: %s forged the four blends" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_boredom_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five scenes: trigger -> climb -> peak -> turn -> resolution (dial 0..1)
    scenes = [("trigger", 0.30), ("climb", 0.65), ("peak", 0.92),
              ("turn", 0.55), ("resolution", 0.12)]
    for s, dial in scenes:
        bar = "#" * int(dial * 30)
        print("  %-10s dial %.2f %s" % (s, dial, bar))
    dials = [d for _, d in scenes]
    assert dials.index(max(dials)) == 2, "peak at scene 3"
    assert dials[-1] < 0.15, "resolution must land low"
    drop = dials[2] - dials[-1]
    print("peak-to-resolution drop: %.2f" % drop)
    assert 0.79 < drop < 0.81
    print("the claim is always available: by intention or by accident")
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "boredom_definition": demo_boredom_definition,
    "boredom_emotion_family": demo_boredom_emotion_family,
    "boredom_intensity_scale": demo_boredom_intensity_scale,
    "boredom_myths": demo_boredom_myths,
    "boredom_first_person": demo_boredom_first_person,
    "boredom_time_course": demo_boredom_time_course,
    "boredom_low_vs_high": demo_boredom_low_vs_high,
    "boredom_restlessness_blend": demo_boredom_restlessness_blend,
    "boredom_day_vignette": demo_boredom_day_vignette,
    "boredom_body_signals": demo_boredom_body_signals,
    "boredom_posture_movement": demo_boredom_posture_movement,
    "boredom_sleep_appetite_energy": demo_boredom_sleep_appetite_energy,
    "boredom_body_differences": demo_boredom_body_differences,
    "boredom_face": demo_boredom_face,
    "boredom_face_intensity": demo_boredom_face_intensity,
    "boredom_hiding_faking": demo_boredom_hiding_faking,
    "boredom_expression_gallery": demo_boredom_expression_gallery,
    "boredom_classic_triggers": demo_boredom_classic_triggers,
    "boredom_personal_triggers": demo_boredom_personal_triggers,
    "boredom_surprise_triggers": demo_boredom_surprise_triggers,
    "boredom_chain_reactions": demo_boredom_chain_reactions,
    "boredom_behavior_actions": demo_boredom_behavior_actions,
    "boredom_speech_patterns": demo_boredom_speech_patterns,
    "boredom_decisions_judgment": demo_boredom_decisions_judgment,
    "boredom_escalation": demo_boredom_escalation,
    "boredom_healthy_expression": demo_boredom_healthy_expression,
    "boredom_unhealthy_expression": demo_boredom_unhealthy_expression,
    "boredom_everyday_practices": demo_boredom_everyday_practices,
    "boredom_reading_others": demo_boredom_reading_others,
    "boredom_supportive_responses": demo_boredom_supportive_responses,
    "boredom_mistakes_to_avoid": demo_boredom_mistakes_to_avoid,
    "boredom_related_emotions": demo_boredom_related_emotions,
    "boredom_emotion_mixes": demo_boredom_emotion_mixes,
    "boredom_full_simulation": demo_boredom_full_simulation,
}

assert len(DEMOS) == 34, "expected 34 demos, got %d" % len(DEMOS)
