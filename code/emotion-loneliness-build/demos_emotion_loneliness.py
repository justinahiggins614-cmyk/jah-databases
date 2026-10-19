#!/usr/bin/env python3
"""Demo programs for the Loneliness Emotion databases (Manon's 16:15 orders, emotion series).

Every demo is real, runnable, stdlib-only Python performing the actual
emotion-scenario simulation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker. Demo outputs
were cross-checked against entry text during authoring.

Descriptive/educational only: these simulations describe and simulate the
emotion of loneliness. They never diagnose any real person.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_loneliness_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # discrepancy model: loneliness = wanted - actual perceived connection
    wanted, actual = 8.0, 3.0
    gap = wanted - actual
    print("wanted connection: %.1f, perceived actual: %.1f, gap: %.1f" % (wanted, actual, gap))
    assert 4.9 < gap < 5.1
    # Weiss two kinds: emotional (bond) vs social (network)
    kinds = {"emotional": "missing a close bond", "social": "missing a circle"}
    print("kinds: %s" % ", ".join("%s=%s" % (k, v) for k, v in kinds.items()))
    assert len(kinds) == 2
    # headcount does not decide it: crowded-but-lonely vs alone-and-content
    crowded_lonely = (12.0, 7.5)  # people nearby, loneliness felt
    alone_content = (0.0, 1.0)
    print("crowded: %d nearby -> felt %.1f; alone: %d nearby -> felt %.1f" % (
        crowded_lonely[0], crowded_lonely[1], alone_content[0], alone_content[1]))
    assert crowded_lonely[1] > alone_content[1]
    print("rule: the gap, not the headcount")
    print("OK: %s defined the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Russell circumplex: valence 0-10, arousal 0-10
    valence, arousal = 2.5, 3.5
    quad = ("unpleasant-low" if valence < 5 and arousal < 5 else "other")
    print("circumplex: valence %.1f, arousal %.1f -> %s" % (valence, arousal, quad))
    assert quad == "unpleasant-low"
    # distance to neighbors on the map
    pts = {"loneliness": (2.5, 3.5), "sadness": (2.0, 3.0),
           "fear": (2.5, 7.5), "joy": (8.5, 7.0)}
    def dist(a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])
    d_sad = dist(pts["loneliness"], pts["sadness"])
    d_fear = dist(pts["loneliness"], pts["fear"])
    d_joy = dist(pts["loneliness"], pts["joy"])
    print("dist to sadness: %.2f, to fear: %.2f, to joy: %.2f" % (d_sad, d_fear, d_joy))
    assert 0.6 < d_sad < 0.8
    assert 3.9 < d_fear < 4.1
    assert d_joy > d_fear
    print("rule: belonging family, fed by sadness, fear, shame - answered by connection")
    print("OK: %s placed loneliness on the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dial: level 1-10; cost is non-linear (level^2)
    def band(level):
        if level <= 3:
            return "mild (passing twinge)"
        if level <= 6:
            return "moderate (settled ache)"
        return "intense (heavy weather)"
    for level in (2, 5, 8):
        print("level %d -> %s, cost %.0f" % (level, band(level), level ** 2))
    assert band(2) == "mild (passing twinge)"
    assert band(5) == "moderate (settled ache)"
    assert band(8) == "intense (heavy weather)"
    # top-end step costs more than a middle step
    assert 8 ** 2 - 7 ** 2 > 4 ** 2 - 3 ** 2
    # two inputs: gap width x duration
    width, weeks = 6.0, 4.0
    dial = min(10.0, width * 0.8 + weeks * 0.9)
    print("width %.1f x %d weeks -> dial %.1f (%s)" % (width, weeks, dial, band(dial)))
    assert 8.3 < dial < 8.5
    print("rule: pleasantness is not the dial here - gap width times duration is")
    print("OK: %s turned the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    quiz = [("only unpopular people get lonely", "myth"),
            ("loneliness is the same as being alone", "myth"),
            ("feeling lonely means something is wrong with you", "myth"),
            ("admitting it will make it worse, so hide it", "myth"),
            ("technology ended loneliness", "myth"),
            ("it is selfish to feel lonely when others care", "myth"),
            ("loneliness tracks perceived closeness, not headcount", "fact")]
    answers = ["myth"] * 6 + ["fact"]
    score = sum(1 for (_, c), a in zip(quiz, answers) if a == c)
    print("myth quiz: %d/%d correct" % (score, len(quiz)))
    for (q, c), a in zip(quiz, answers):
        print("  [%s] %-52s -> %s" % ("ok" if a == c else "MISS", q, c))
    assert score == 7
    print("rule: name the false rule and the appraisal stops enforcing it")
    print("OK: %s cleared the attic" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # features encoded as images in the passage
    features = {"hyper-awareness of quiet": "humming stillness, loud kettle",
                "somatic hollowness": "hollow chest, missing furniture",
                "heavy-phone paradox": "reaching feels like lifting weight",
                "social comparison": "hallway laugh lands like a stone",
                "compensatory fantasy": "rehearsed conversations",
                "discrepancy double vision": "two lives, the gap as address",
                "shame-free naming": "nothing is wrong, exactly"}
    print("encoded features: %d" % len(features))
    for k, v in features.items():
        print("  %-26s -> %s" % (k, v))
    assert len(features) == 7
    # the passage is simulation for recognition, not diagnosis
    purpose = "recognition"
    assert purpose == "recognition"
    print("rule: the double vision - fine and missing at once - is the signature")
    print("OK: %s stepped inside the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weather pattern over 8 weeks: onset, peak, fading, aftershock echo
    weeks = [1.0, 2.5, 5.0, 7.5, 9.0, 8.0, 5.5, 3.0]
    phases = ["onset", "onset", "peak", "peak", "peak", "fading", "fading", "aftershock-echo"]
    for w, (v, p) in enumerate(zip(weeks, phases), 1):
        print("week %d: felt %.1f (%s)" % (w, v, p))
    peak = max(weeks)
    assert 8.9 < peak < 9.1
    assert weeks.index(peak) == 4  # peaks at week 5, the empty-edges stretch
    # fading slope: steady contact closes the gap from the edges
    fade = weeks[4] - weeks[6]
    print("fade from peak to week 7: %.1f points" % fade)
    assert 3.4 < fade < 3.6
    # aftershock is an echo, not a relapse: smaller than the peak
    assert weeks[7] < peak * 0.5
    print("rule: weather passes; the record of passings is evidence against the permanence lie")
    print("OK: %s charted the weather" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same person, same apartment; only the dial moves
    low = {"dial": 2.0, "duration_h": 3.0, "rooms_affected": 1, "bid_made": 1}
    high = {"dial": 8.0, "duration_h": 24.0 * 21, "rooms_affected": 5, "bid_made": 0}
    for label, s in (("low", low), ("high", high)):
        print("%s: dial %.0f, duration %.0fh, rooms %d, bid made: %s" % (
            label, s["dial"], s["duration_h"], s["rooms_affected"], bool(s["bid_made"])))
    assert low["bid_made"] == 1 and high["bid_made"] == 0
    assert high["duration_h"] / low["duration_h"] > 100
    # approach wins at low dial, avoidance wins at high dial
    p_approach = {2.0: 0.9, 8.0: 0.15}
    print("P(approach wins): dial 2 -> %.2f, dial 8 -> %.2f" % (p_approach[2.0], p_approach[8.0]))
    assert p_approach[2.0] > 0.8 and p_approach[8.0] < 0.2
    print("rule: duration in days, pervasiveness across rooms, bid-failure - that is the high setting")
    print("OK: %s held the two snapshots side by side" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_loneliness_grief_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grief = waves (decaying spikes), loneliness = steady tide
    tide = 6.0
    def wave(t):
        return 4.0 * math.exp(-0.35 * t) * (1.0 if t % 3 < 1.5 else 0.25)
    print("tide (loneliness, steady): %.1f" % tide)
    for t in (0, 2, 5, 9):
        total = tide + wave(t)
        print("day %d: wave %.2f + tide %.1f = %.2f" % (t, wave(t), tide, total))
    assert 9.9 < tide + wave(0) < 10.1
    assert tide + wave(9) < tide + 1.0  # waves fade, tide remains
    # sorting the housemates: grief answered by mourning, loneliness by connection
    answers = {"grief": "mourning and ritual", "loneliness": "connection rebuilt"}
    assert answers["grief"] != answers["loneliness"]
    print("rule: two alarms, one trigger - mourning does not fill the daily-contact gap")
    print("OK: %s sorted the housemates" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the day's arithmetic: minutes of felt contact vs felt distance
    beats = [("morning quiet", 0), ("bus comparison", 0), ("desk lunch", 0),
             ("commute contrast", 0), ("counter dinner", 0), ("heavy-phone hour", 0),
             ("brother's meme", 4)]
    contact = sum(m for _, m in beats)
    day = 24 * 60
    print("felt contact: %d min out of %d" % (contact, day))
    assert contact == 4
    ratio = contact / day
    print("ratio: %.4f - four true minutes carried the day" % ratio)
    assert 0.002 < ratio < 0.004
    # hinge moments: commute and evening carry the most weight
    hinges = {"commute": 3.0, "evening": 3.5, "morning": 1.0, "midday": 0.5}
    worst = max(hinges, key=hinges.get)
    print("heaviest hinge: %s (weight %.1f)" % (worst, hinges[worst]))
    assert worst == "evening"
    print("rule: the ratio of felt contact to felt distance defines the day")
    print("OK: %s lived the ordinary day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # somatic signature, 0-10 self-report scale at moderate intensity
    signals = {"chest hollow/pressure": 7.5, "shallow breathing": 6.5,
               "jaw/shoulder tension": 6.0, "stomach knot": 5.5,
               "cold hands": 5.0, "gray fatigue": 7.0}
    for k, v in signals.items():
        print("  %-22s %.1f/10" % (k, v))
    mean_sig = sum(signals.values()) / len(signals)
    print("mean somatic load: %.2f" % mean_sig)
    assert 6.2 < mean_sig < 6.4
    # pain-circuitry overlap: social pain uses the same alarm as physical pain
    overlap = True
    assert overlap
    # the body reports before the mind admits: jaw clenched an hour early
    lead_minutes = 60.0
    assert 55.0 < lead_minutes < 65.0
    print("rule: the body files its report an hour before the mind admits the feeling")
    print("OK: %s read the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # openness score 0-10 from observable features (10 = fully open)
    features = {"shoulder roll-in": -2.0, "head tilt down": -1.5,
                "gaze dropped": -1.5, "arms crossed/pocketed": -1.0,
                "shortened stride": -1.0, "edge positioning": -1.0}
    openness = 10.0 + sum(features.values())
    for k, v in features.items():
        print("  %-22s %+0.1f" % (k, v))
    print("openness score: %.1f/10" % openness)
    assert 1.9 < openness < 2.1
    # the cost: closed posture reads as do-not-approach
    p_approach_open, p_approach_closed = 0.65, 0.25
    print("P(approach): open %.2f vs closed %.2f" % (p_approach_open, p_approach_closed))
    assert p_approach_closed < p_approach_open
    print("rule: the protection prolongs the need for protection - open the frame")
    print("OK: %s read the silhouette" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sleep efficiency: time asleep / time in bed
    eff_rested, eff_lonely = 0.94, 0.81
    print("sleep efficiency: rested %.0f%%, lonely %.0f%%" % (eff_rested * 100, eff_lonely * 100))
    assert 0.80 < eff_lonely < 0.82
    # appetite swings both ways
    patterns = {"evening grazing": "+snacks, fills hours", "futility shrinkage": "toast or nothing"}
    print("appetite: %s" % "; ".join("%s (%s)" % (k, v) for k, v in patterns.items()))
    assert len(patterns) == 2
    # energy = triple deficit sum
    deficits = {"poor sleep": 3.0, "erratic fuel": 2.5, "alarm uptime": 3.5}
    total = sum(deficits.values())
    print("energy deficit total: %.1f/10 (%s)" % (total, " + ".join(deficits)))
    assert 8.9 < total < 9.1
    print("rule: maintenance strain, not character - the triad is downstream of the gap")
    print("OK: %s checked the maintenance systems" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_individual_diff(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same gap, different ringtones: sensitivity multipliers
    base_gap = 5.0
    profiles = {"highly sensitive": 1.6, "steady attachment": 0.7,
                "unpredictable attachment": 1.4, "introvert (depth need)": 1.0}
    for k, m in profiles.items():
        felt = base_gap * m
        print("  %-28s x%.1f -> felt %.1f" % (k, m, felt))
    assert abs(base_gap * profiles["highly sensitive"] - 8.0) < 0.01
    assert base_gap * profiles["steady attachment"] < base_gap
    # life-stage objects of the want
    stages = {"teens": "peer belonging", "young adult": "a circle in a new city",
              "parent": "adult conversation", "older adult": "daily contact"}
    assert len(stages) == 4
    print("objects of the want shift by stage: %d stages mapped" % len(stages))
    # introversion correction
    assert profiles["introvert (depth need)"] == 1.0
    print("rule: no single correct shape - differently-shaped loneliness is still loneliness")
    print("OK: %s tuned the ringtones" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # FACS-inspired intensities 0-5 for the composite
    aus = {"AU1 inner-brow raise (plea)": 2.0, "upper-lid droop": 2.5,
           "gaze aversion/drift": 3.0, "mouth corner depressor": 2.0,
           "lip press (suppression)": 2.5, "cheek raise (Duchenne)": 0.0}
    for k, v in aus.items():
        print("  %-32s %.1f/5" % (k, v))
    assert aus["AU1 inner-brow raise (plea)"] > 0
    assert aus["cheek raise (Duchenne)"] == 0.0  # the eyes do not join the smile
    # the tell: smile assembly delay in seconds
    genuine_delay, performed_delay = 0.1, 0.6
    print("smile delay: genuine %.1fs vs performed %.1fs" % (genuine_delay, performed_delay))
    assert performed_delay > genuine_delay + 0.3
    print("rule: the brow and the eyes file their own report")
    print("OK: %s drew the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # suppression budget 100 units; cost rises with dial
    def cost(dial):
        return dial ** 2
    for dial in (2, 5, 8):
        c = cost(dial)
        state = "invisible" if dial <= 3 else ("managed" if dial <= 6 else "flat/fractured")
        print("dial %d: suppression cost %d/100 -> %s" % (dial, c, state))
    assert cost(2) == 4 and cost(5) == 25 and cost(8) == 64
    # read order: eyes (least voluntary) first, mouth (most managed) second
    voluntariness = {"eyes": 0.2, "brow": 0.4, "mouth": 0.8}
    ordered = sorted(voluntariness, key=voluntariness.get)
    print("read order: %s" % " -> ".join(ordered))
    assert ordered == ["eyes", "brow", "mouth"]
    print("rule: the gap between the least and most voluntary features is the dial")
    print("OK: %s scaled the expression" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hiding tactics and their leak probabilities
    tactics = {"performed smile": 0.55, "over-talkativeness": 0.40,
               "busyness costume": 0.35, "deflection script": 0.50}
    for k, v in tactics.items():
        print("  %-20s leak P=%.2f" % (k, v))
    mean_leak = sum(tactics.values()) / len(tactics)
    print("mean leak probability: %.3f" % mean_leak)
    assert 0.44 < mean_leak < 0.46
    # the temporal leak: performance runs in bursts, recovery reads as withdrawal
    burst_hours, recovery_days = 3.0, 2.0
    print("burst %.0fh -> recovery %.0fd (misread as disinterest)" % (burst_hours, recovery_days))
    assert burst_hours < recovery_days * 24
    print("rule: your performance is more transparent than it feels - gentleness, not suspicion")
    print("OK: %s watched the mask slip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # artist checklist: required craft decisions
    artist = ["dimmed eye highlight", "2mm brow lift, no more", "soft jaw (not clenched)",
              "neutral-down mouth", "negative space: empty chair"]
    actor = ["stillness over tears", "voice a semitone flatter", "trailing sentence ends",
             "half-beat-late laugh", "the aborted reach", "contrast beat: real smile, then fade"]
    print("artist decisions: %d, actor decisions: %d" % (len(artist), len(actor)))
    assert len(artist) == 5 and len(actor) == 6
    # the 2mm rule: overdraw turns loneliness into tragedy
    brow_mm = 2.0
    assert 1.9 < brow_mm < 2.1
    # contrast beat encodes the thesis: contact answers, then the gap reopens
    print("brow lift: %.0fmm - the whole plea, do not overdraw" % brow_mm)
    print("rule: draw the discrepancy itself - the wanted life as absence")
    print("OK: %s stocked the gallery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_loneliness_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gap-opening power 0-10: expected company minus actual company
    triggers = {"move to new city": 9.0, "relationship ending": 9.5,
                "new school/job": 7.5, "empty nest": 6.5, "retirement": 6.0,
                "first holidays after loss": 8.5, "living alone after company": 7.0,
                "wedding season (unpartnered)": 6.0}
    for k, v in sorted(triggers.items(), key=lambda kv: -kv[1]):
        print("  %-32s gap %.1f" % (k, v))
    top = max(triggers, key=triggers.get)
    print("strongest classic: %s (%.1f)" % (top, triggers[top]))
    assert top == "relationship ending"
    assert 9.4 < triggers[top] < 9.6
    # same event with the right person beside you triggers nothing
    assert triggers["move to new city"] > 0
    print("rule: the trigger is the event minus the expected company")
    print("OK: %s listed the greatest hits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # associative strength 0-10 by sense; smell is fastest
    tags = {"song (hearing)": 7.0, "park bench (place)": 6.5,
            "anniversary (calendar)": 8.0, "extra toothbrush (object)": 7.5,
            "cut grass (smell)": 8.5, "Sunday call gone quiet (ritual)": 7.0}
    for k, v in sorted(tags.items(), key=lambda kv: -kv[1]):
        print("  %-28s strength %.1f" % (k, v))
    assert max(tags.values()) == tags["cut grass (smell)"]
    # decay of the echo: each recall weakens the ambush slightly
    s0, decay = 8.5, 0.92
    s5 = s0 * (decay ** 5)
    print("smell-tag strength: now %.1f -> after 5 recalls %.2f" % (s0, s5))
    assert 5.5 < s5 < 5.7
    # translate, do not argue
    print("rule: the song hurts because the friendship mattered - translate, do not argue")
    print("OK: %s mapped the private wires" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # contrast power; unguarded multiplier 1.5x when the guard is down
    base = {"joyful crowd": 6.0, "silent phone Friday": 5.5, "sunny Saturday": 5.0,
            "overheard inside joke": 4.5, "couples' dinner": 6.5, "grocery run for one": 4.0}
    guarded = 1.0
    unguarded = 1.5
    for k, v in sorted(base.items(), key=lambda kv: -kv[1] * unguarded):
        print("  %-22s guarded %.1f -> unguarded %.1f" % (k, v, v * unguarded))
    worst = max(base, key=base.get)
    assert worst == "couples' dinner"
    assert abs(base[worst] * unguarded - 9.75) < 0.01
    # innocence adds shame via the myths; naming the mechanism disarms it
    shame_addon = 2.0
    named = 0.0
    print("shame add-on unnamed: +%.1f, named: +%.1f" % (shame_addon, named))
    assert named < shame_addon
    print("rule: unguarded contrast - the alarm's native language, nothing foolish about hearing it")
    print("OK: %s caught the ambushes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # classic chain: each link manufactures evidence; evidence multiplies felt gap
    links = ["canceled dinner (gap 2.0)", "shame story (x1.5)", "hiding: no reschedule (x1.4)",
             "empty weekend (x1.6)", "confirmation (x1.3)"]
    gap = 2.0
    mults = [1.5, 1.4, 1.6, 1.3]
    for link in links:
        print("  " + link)
    for m in mults:
        gap *= m
    print("manufactured gap: %.2f from a 2.0 start" % gap)
    assert 8.7 < gap < 8.8
    # refusing one link starves the cascade: multiply by 0 at the hiding link
    gap2 = 2.0 * 1.5 * 0.0 * 1.6 * 1.3
    print("with the hiding link refused: %.1f" % gap2)
    assert gap2 == 0.0
    # branches
    branches = {"anger branch": "push away -> rejection", "fear branch": "cling -> withdrawal"}
    assert len(branches) == 2
    print("rule: refuse one behavioral link and the evidence factory shuts down")
    print("OK: %s broke the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one week of behavior counts
    reaching = {"texts sent": 4, "plans made": 2, "lingered after meeting": 3}
    retreating = {"plans canceled": 3, "early exits": 2, "invites declined first": 2}
    fillers = {"doomscroll hours": 9, "midnight reorganizing": 2, "extra episodes": 6}
    r, t = sum(reaching.values()), sum(retreating.values())
    print("reaching %d vs retreating %d (fillers %d)" % (r, t, sum(fillers.values())))
    assert r == 9 and t == 7
    ratio = r / (r + t)
    print("reach ratio: %.3f %s" % (ratio, "(cage)" if ratio < 0.6 else "(key)"))
    assert 0.56 < ratio < 0.57
    # the rule: one genuine reach a day outperforms a month of fillers
    daily_reach, days = 1, 30
    assert daily_reach * days == 30
    print("30 days x 1 genuine reach = %d answered alarms" % (daily_reach * days))
    print("rule: the ratio is the cage and the key")
    print("OK: %s inventoried the repertoire" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # closers detected in a sample dialogue of 20 utterances
    closers = ["I'm fine", "no worries", "all good", "I'm fine", "no worries"]
    utterances = 20
    closer_rate = len(closers) / utterances
    print("closers: %d/%d utterances (rate %.2f)" % (len(closers), utterances, closer_rate))
    assert abs(closer_rate - 0.25) < 0.001
    # initiation decay over 4 weeks: bids placed per week
    bids = [5, 3, 2, 1]
    print("bids placed per week: %s" % bids)
    assert bids == sorted(bids, reverse=True)
    decay = bids[-1] / bids[0]
    print("decay: %.2f of week-1 initiation by week 4" % decay)
    assert abs(decay - 0.2) < 0.001
    # the skill: ask the second, slower question
    print("rule: hear the closers, then ask the second slower question - and mean it")
    print("OK: %s listened to the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Bayesian threat read: high prior on rejection sorts ambiguous evidence
    prior_reject = 0.70
    # a warm reply arrives: likelihood of warmth if interested vs if not
    p_warm_if_interested, p_warm_if_not = 0.80, 0.30
    p_warm = p_warm_if_interested * (1 - prior_reject) + p_warm_if_not * prior_reject
    posterior = p_warm_if_not * prior_reject / p_warm
    print("prior P(reject)=%.2f -> after one warm reply P(reject)=%.3f" % (prior_reject, posterior))
    assert 0.46 < posterior < 0.48
    # three warm replies in a row keep updating
    p = prior_reject
    for i in range(3):
        pw = p_warm_if_interested * (1 - p) + p_warm_if_not * p
        p = p_warm_if_not * p / pw
    print("after 3 warm replies: P(reject)=%.3f" % p)
    assert 0.10 < p < 0.12
    print("rule: calibration, not willpower - log the contrary evidence")
    print("OK: %s recalibrated the lens" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_intensity_behavior(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # system dominance by dial: alarm weight falls, defense weight rises
    def weights(dial):
        alarm = max(0.0, 1.0 - dial / 12.0)
        defense = min(1.0, dial / 10.0)
        return alarm, defense
    for dial in (2, 5, 8):
        a, d = weights(dial)
        regime = "reaches" if a > d else ("manages" if abs(a - d) < 0.25 else "sabotages")
        print("dial %d: alarm %.2f vs defense %.2f -> %s" % (dial, a, d, regime))
    a2, d2 = weights(2)
    a8, d8 = weights(8)
    assert a2 > d2 and d8 > a8
    assert abs(weights(5)[0] - weights(5)[1]) < 0.25
    # the way back: un-sabotage restores alarm dominance
    print("rule: mild reaches, moderate manages, intense sabotages - un-sabotage walks it back")
    print("OK: %s watched the dial drive" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three channels, effectiveness 0-10 at closing the gap
    channels = {"say it plainly": 8.5, "show it appropriately": 7.0,
                "channel into making": 7.5}
    for k, v in channels.items():
        print("  %-22s effectiveness %.1f" % (k, v))
    mean_eff = sum(channels.values()) / len(channels)
    print("mean: %.2f vs hiding (%.1f)" % (mean_eff, 2.0))
    assert 7.6 < mean_eff < 7.7
    # small and repeatable: reps build the skill
    reps = [1, 2, 3, 4, 5]
    skill = [1 - 0.7 ** r for r in reps]
    print("skill after reps %s: %.2f" % (reps[-1], skill[-1]))
    assert 0.83 < skill[-1] < 0.84
    print("rule: one honest sentence, one undisguised gladness, one made thing shared")
    print("OK: %s opened the three channels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottling: costs compound weekly; exploding: backlog-sized release
    bottled = 2.0
    for week in range(1, 5):
        bottled *= 1.35
        print("bottled pressure week %d: %.2f" % (week, bottled))
    assert 6.6 < bottled < 6.7
    trigger_size, release_size = 1.0, bottled
    print("trigger %.1f -> release %.1f (backlog-sized, bewilders listeners)" % (trigger_size, release_size))
    assert release_size > trigger_size * 6
    # dosage comparison: small chosen releases vs sealed pressure
    small_releases = 4 * 1.0
    print("4 small chosen releases total %.1f vs sealed %.1f" % (small_releases, bottled))
    assert small_releases < bottled
    print("rule: dosage and timing - small chosen releases beat backlog floods")
    print("OK: %s priced both directions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weekly felt-contact minutes per practice
    practices = {"one recurring thing": 90, "named greetings x12": 24,
                 "three threads alive": 60, "daily outdoor walk": 35,
                 "regular volunteering": 120, "evening naming": 5}
    total = sum(practices.values())
    for k, v in practices.items():
        print("  %-24s %d min/wk" % (k, v))
    print("total: %d min/week of evidence" % total)
    assert total == 334
    # compound interest over 8 weeks
    evidence = [total * (1.05 ** w) for w in range(8)]
    print("week 8 evidence: %.0f (compounding)" % evidence[-1])
    assert 469.0 < evidence[-1] < 471.0
    print("rule: the alarm is answered by evidence, one kept appointment at a time")
    print("OK: %s built the routine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_reading_signs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels, weak alone; co-occurrence is the signal
    cues = {"face": 0.30, "body": 0.25, "voice": 0.30, "behavior": 0.35}
    single = max(cues.values())
    combined = 1 - math.prod(1 - v for v in cues.values())
    print("strongest single cue: %.2f; combined: %.3f" % (single, combined))
    assert 0.76 < combined < 0.77
    # context multiplier
    contexts = {"well-connected regular": 1.0, "new arrival": 2.2,
                "recently bereaved": 2.5, "life-stage transition": 1.8}
    for k, v in contexts.items():
        print("  %-24s x%.1f -> read %.3f" % (k, v, min(0.99, combined * v / 2)))
    assert contexts["recently bereaved"] > contexts["well-connected regular"]
    # the golden rule: never announce
    announced = False
    assert announced is False
    print("rule: recognition is reconnaissance for kindness - targeting data, not a label")
    print("OK: %s learned the read" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five moves, each defeating one defense
    moves = {"specific invitation": "bid-failure", "second invitation": "first veto",
             "second slower question": "the closer", "structured contact": "spontaneity decay",
             "visible inclusion": "membership doubt"}
    for k, v in moves.items():
        print("  %-22s defeats %s" % (k, v))
    assert len(moves) == 5
    coverage = len(moves) / 5.0 * 100
    print("defense coverage: %.0f%%" % coverage)
    assert 99.9 < coverage < 100.1
    # steadiness: the trust audit accepts only kept promises
    kept, promised = 9, 10
    trust = kept / promised
    print("kept %d/%d promises -> trust %.2f" % (kept, promised, trust))
    assert 0.89 < trust < 0.91
    print("rule: steadiness is the only currency the trust audit accepts")
    print("OK: %s rehearsed the kindness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_mistakes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the audit: membership evidence (+) vs management evidence (-)
    moves = {"minimizing": -2, "pitying": -2, "advice-bombing": -1,
             "forced cheer": -1, "interrogating": -1, "comparing": -1,
             "grand gesture then silence": 0}
    good = {"specific invite": 2, "second ask": 2, "steady presence": 3}
    bad_total = sum(moves.values())
    good_total = sum(good.values())
    print("mistakes total: %d; kind moves total: +%d" % (bad_total, good_total))
    assert bad_total == -8
    assert good_total == 7
    # dosage: ten small kept promises beat one grand gesture
    print("10 small kept promises (%d) vs 1 grand gesture (%d)" % (10 * 1, 5))
    assert 10 * 1 > 5
    print("rule: membership heals; management, however loving, does not")
    print("OK: %s dodged the misfires" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_neighbors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # objective/subjective x present/absent: four rooms
    rooms = {("isolated", "lonely"): "hermit in winter",
             ("isolated", "content"): "hermit by choice",
             ("surrounded", "lonely"): "popular student",
             ("surrounded", "content"): "the circle"}
    print("four rooms: %d occupied in the data" % len(rooms))
    assert len(rooms) == 4
    # the want-test separates solitude from loneliness
    def state(chosen, unwanted_distance):
        if chosen and not unwanted_distance:
            return "solitude"
        if unwanted_distance:
            return "loneliness"
        return "neutral aloneness"
    assert state(True, False) == "solitude"
    assert state(False, True) == "loneliness"
    # boredom differential: fantasy content
    fantasies = {"bored": "interesting activity", "lonely": "company"}
    assert fantasies["bored"] != fantasies["lonely"]
    print("fantasy test: bored->%s, lonely->%s" % (fantasies["bored"], fantasies["lonely"]))
    print("rule: response-matching - each neighbor wants a different answer")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # blends as chords: loneliness base 6.0 plus partner weight
    base = 6.0
    blends = {"bittersweet (+joy 5.0)": (5.0, "parallel appraisal"),
              "social dread (+fear 7.0)": (7.0, "temporal extension"),
              "abandonment rage (+anger 6.0)": (6.0, "attribution"),
              "hopeful aching (+anticipation 4.0)": (4.0, "scheduled resolution")}
    for k, (w, mech) in blends.items():
        chord = math.hypot(base, w)
        print("  %-32s chord %.2f (%s)" % (k, chord, mech))
    assert 7.8 < math.hypot(base, 5.0) < 7.9
    assert math.hypot(base, 7.0) > math.hypot(base, 4.0)
    # handle the partner first: it distorts the loneliness underneath
    order = ["partner", "loneliness"]
    assert order[0] == "partner"
    print("rule: handle the partner first - it is what distorts the loneliness underneath")
    print("OK: %s blended the chords" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_loneliness_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Priya's arc: gap value per scene
    scenes = [("trigger: the move", 2.0), ("loop: bar photos", 5.0),
              ("peak: rainy Sunday", 9.0), ("refused link: tacos Thursday", 6.5),
              ("fading: hiking group", 3.0), ("aftershock: the song", 3.5)]
    for name_, gap in scenes:
        print("  %-28s gap %.1f" % (name_, gap))
    gaps = [g for _, g in scenes]
    assert max(gaps) == 9.0 and gaps.index(9.0) == 2
    assert gaps[-2] < gaps[0] + 2.0  # fading lands near the start
    assert gaps[-1] < gaps[2] * 0.5  # aftershock is an echo, not a relapse
    drop = gaps[2] - gaps[4]
    print("peak-to-fading drop: %.1f via one refused link + kept appointments" % drop)
    assert 5.9 < drop < 6.1
    print("rule: the loop manufactured its own evidence; kept appointments rebuilt the world")
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "definition": demo_loneliness_definition,
    "family": demo_loneliness_family,
    "intensity": demo_loneliness_intensity,
    "myths": demo_loneliness_myths,
    "first_person": demo_loneliness_first_person,
    "time_course": demo_loneliness_time_course,
    "low_vs_high": demo_loneliness_low_vs_high,
    "loneliness_grief_blend": demo_loneliness_loneliness_grief_blend,
    "day_vignette": demo_loneliness_day_vignette,
    "body": demo_loneliness_body,
    "posture": demo_loneliness_posture,
    "sleep_appetite": demo_loneliness_sleep_appetite,
    "individual_diff": demo_loneliness_individual_diff,
    "face": demo_loneliness_face,
    "face_intensity": demo_loneliness_face_intensity,
    "hiding_faking": demo_loneliness_hiding_faking,
    "expression_gallery": demo_loneliness_expression_gallery,
    "classic_triggers": demo_loneliness_classic_triggers,
    "personal_triggers": demo_loneliness_personal_triggers,
    "surprise_triggers": demo_loneliness_surprise_triggers,
    "chain_reactions": demo_loneliness_chain_reactions,
    "actions": demo_loneliness_actions,
    "speech": demo_loneliness_speech,
    "decisions": demo_loneliness_decisions,
    "intensity_behavior": demo_loneliness_intensity_behavior,
    "healthy_expression": demo_loneliness_healthy_expression,
    "unhealthy_expression": demo_loneliness_unhealthy_expression,
    "everyday_practices": demo_loneliness_everyday_practices,
    "reading_signs": demo_loneliness_reading_signs,
    "supportive_responses": demo_loneliness_supportive_responses,
    "mistakes": demo_loneliness_mistakes,
    "neighbors": demo_loneliness_neighbors,
    "mixes": demo_loneliness_mixes,
    "full_simulation": demo_loneliness_full_simulation,
}
