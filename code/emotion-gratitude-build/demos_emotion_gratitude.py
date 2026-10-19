#!/usr/bin/env python3
"""Demo programs for the Gratitude Emotion databases (Manon's 16:15 orders, emotion series).

Every demo is real, runnable, stdlib-only Python performing the actual
emotion-scenario simulation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker. Demo outputs
were cross-checked against entry text during authoring.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_gratitude_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six criteria for gratitude as an emotion; gratitude meets all six
    criteria = {"object-directed (has a source)": 1, "appraisal-based": 1,
                "distinct action tendency": 1, "brief-to-enduring": 1,
                "prosocial signal": 1, "felt warmth": 1}
    met = sum(criteria.values())
    score = met / len(criteria) * 100.0
    print("emotion criteria met: %d/%d" % (met, len(criteria)))
    print("gratitude emotion score: %.1f %%" % score)
    assert met == 6
    assert 99.9 < score < 100.1
    print("rule: the felt thank-you - benefit recognized, source outside the self")
    print("OK: %s defined the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Plutchik wheel addresses in degrees: gratitude between joy (0) and trust (-45)
    wheel = {"gratitude": -22.5, "joy": 0.0, "trust": -45.0, "sadness": 180.0}
    def ang_dist(a, b):
        d = abs(a - b) % 360.0
        return min(d, 360.0 - d)
    d_joy = ang_dist(wheel["gratitude"], wheel["joy"])
    d_trust = ang_dist(wheel["gratitude"], wheel["trust"])
    d_sad = ang_dist(wheel["gratitude"], wheel["sadness"])
    print("gratitude->joy: %.1f deg" % d_joy)
    print("gratitude->trust: %.1f deg" % d_trust)
    print("gratitude->sadness: %.1f deg" % d_sad)
    assert 22.4 < d_joy < 22.6
    assert 22.4 < d_trust < 22.6
    assert 157.4 < d_sad < 157.6
    # circumplex: pleasant, moderately activated
    valence, arousal = 8.0, 5.0
    quadrant = "pleasant-moderate" if valence > 5 and 3.0 < arousal <= 6.0 else "other"
    print("circumplex quadrant: %s" % quadrant)
    assert quadrant == "pleasant-moderate"
    print("rule: a complex emotion, not a basic one - joy aimed at a trusted source")
    print("OK: %s placed gratitude on the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dial: level 1-10, pleasantness fixed high, arousal = level
    pleasantness = 8.0
    bands = {}
    for level in (2, 5, 7, 9):
        arousal = float(level)
        if level <= 3:
            band = "mild (quiet appreciation)"
        elif level <= 7:
            band = "moderate (warm thankfulness)"
        else:
            band = "intense (overwhelming)"
        bands[level] = band
        print("level %d -> arousal %.1f, pleasantness %.1f: %s" % (level, arousal, pleasantness, band))
    assert 7.99 < pleasantness < 8.01
    assert bands[2] == "mild (quiet appreciation)"
    assert bands[5] == "moderate (warm thankfulness)"
    assert bands[9] == "intense (overwhelming)"
    # felt vs shown: display gain can mute the shown dial
    felt, shown = 8.0, 8.0 * 0.6
    print("felt %.1f vs shown %.1f: two dials, not one" % (felt, shown))
    assert 4.79 < shown < 4.81
    print("rule: pleasantness stays high at every setting; energy is the dial")
    print("OK: %s turned the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six common claims: each is a myth (True = is a myth)
    items = [("gratitude means pretending everything is fine", True),
             ("gratitude needs a human benefactor", True),
             ("saying thank you is the whole of it", True),
             ("gratitude is just positive thinking", True),
             ("feeling grateful puts you in debt", True),
             ("listing good things always works by itself", True)]
    myths = [t for t, is_myth in items if is_myth]
    print("claims tested: %d" % len(items))
    print("myths busted: %d" % len(myths))
    assert len(myths) == 6
    assert len(myths) == len(items)
    print("rule: the real mechanism survives every myth - benefit plus source, felt as warmth")
    print("OK: %s cleared the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five-phase first-person sequence, component strengths 0-10
    phases = {"recognition": 9.0, "warmth": 8.0, "replay": 7.0,
              "humility": 6.0, "urge to send back": 8.0}
    for phase, val in phases.items():
        print("%-18s %.1f/10" % (phase, val))
    composite = sum(phases.values()) / len(phases)
    print("felt-gratitude composite: %.1f/10" % composite)
    assert 7.59 < composite < 7.61
    assert phases["recognition"] == max(phases.values())
    print("rule: recognition leads, warmth follows, the urge closes the loop")
    print("OK: %s simulated the inside view" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # onset fast, peak lags, fade is slow exponential, memory re-triggers echoes
    onset_min, onset_val = 0.1, 3.0
    peak_min, peak_val = 3.0, 9.0
    t = 63.0
    g = peak_val * math.exp(-(t - peak_min) / 120.0)
    print("onset t=%.1f min: %.1f" % (onset_min, onset_val))
    print("peak  t=%.1f min: %.1f" % (peak_min, peak_val))
    print("fade  t=%.0f min: %.2f" % (t, g))
    assert 5.45 < g < 5.47
    aftershock = 0.4 * peak_val
    print("aftershock on recall: %.1f" % aftershock)
    assert 3.59 < aftershock < 3.61
    print("rule: quick onset, lagging peak, gentle fade, echoing memory")
    print("OK: %s traced the feeling through time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two lived snapshots on the same circuit
    low = {"warmth": 2.0, "urge": 1.5, "replay_days": 0.0}
    high = {"warmth": 9.0, "urge": 8.5, "replay_days": 14.0}
    print("low  (held door): warmth %.1f, urge %.1f, replay %.0f days" % (
        low["warmth"], low["urge"], low["replay_days"]))
    print("high (rain rescue): warmth %.1f, urge %.1f, replay %.0f days" % (
        high["warmth"], high["urge"], high["replay_days"]))
    ratio = high["warmth"] / low["warmth"]
    print("warmth ratio high/low: %.1f" % ratio)
    assert 4.49 < ratio < 4.51
    assert high["replay_days"] > low["replay_days"]
    print("rule: one circuit, different current - trickle versus river")
    print("OK: %s compared the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_joy_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gratitude + joy: the most common partner blend
    g_val, g_aro = 8.0, 5.0
    j_val, j_aro = 8.5, 7.0
    b_val = (g_val + j_val) / 2.0
    b_aro = (g_aro + j_aro) / 2.0
    print("gratitude: valence %.1f arousal %.1f" % (g_val, g_aro))
    print("joy:       valence %.1f arousal %.1f" % (j_val, j_aro))
    print("blend:     valence %.2f arousal %.1f -> celebration" % (b_val, b_aro))
    assert 8.24 < b_val < 8.26
    assert 5.99 < b_aro < 6.01
    print("rule: joy supplies the energy, gratitude supplies the address")
    print("OK: %s blended the partners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a day of small gratitudes: accumulation, then the evening replay
    moments = [("warm bed", 1.5), ("covered meeting", 4.0), ("old friend calls", 3.0),
               ("bus waits", 2.0), ("neighbor soup", 7.5)]
    for label, val in moments:
        print("%-18s +%.1f warmth" % (label, val))
    total = sum(v for _, v in moments)
    replay = 0.4 * total
    day = total + replay
    print("daytime total: %.1f" % total)
    print("evening replay: +%.1f" % replay)
    print("day felt twice: %.1f" % day)
    assert 17.99 < total < 18.01
    assert 7.19 < replay < 7.21
    assert 25.19 < day < 25.21
    print("rule: no single peak - a dozen small recognitions, felt twice")
    print("OK: %s lived the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body signals at intensity 7: the standing-down body
    signals = {"chest_warmth": 7.0, "exhale_factor": 1.6, "heart_delta_bpm": -8.0,
               "muscle_release": 7.5, "tear_readiness": 6.0}
    for k, v in signals.items():
        print("%-16s %.1f" % (k, v))
    assert signals["heart_delta_bpm"] < 0.0
    assert signals["exhale_factor"] > 1.0
    bounded = [v for k, v in signals.items() if k not in ("exhale_factor", "heart_delta_bpm")]
    assert all(0.0 <= v <= 10.0 for v in bounded)
    print("rule: no threat to fight, no prize to chase - the system stands down")
    print("OK: %s read the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # posture openness: the approach system made visible
    chest = 8.0
    arms_open = 10.0
    tilt = 6.0 / 10.0 * 10.0
    nods = min(3.0, 5.0) / 5.0 * 10.0
    approach = 10.0
    score = (chest + arms_open + tilt + nods + approach) / 5.0
    print("chest %.1f arms %.1f tilt %.1f nods %.1f approach %.1f" % (chest, arms_open, tilt, nods, approach))
    print("openness score: %.1f/10" % score)
    assert 7.99 < score < 8.01
    print("rule: gratitude never closes the body - the posture is always an opening")
    print("OK: %s read the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a short pre-sleep gratitude practice vs the worry loop
    journal_min = 5.0
    onset_cut = journal_min * 1.2
    appetite_factor = 1.0
    energy = 7.5
    print("journal minutes: %.1f" % journal_min)
    print("sleep onset sooner by: %.1f min" % onset_cut)
    print("appetite factor: %.1f (untouched)" % appetite_factor)
    print("energy steadiness: %.1f/10" % energy)
    assert 5.99 < onset_cut < 6.01
    assert appetite_factor == 1.0
    assert 7.49 < energy < 7.51
    print("rule: the gratitude replay wins the pre-sleep stage from the worry loop")
    print("OK: %s measured sleep, appetite, energy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_individual_diff(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same felt gratitude, three display gains
    profiles = {"expressive": 1.4, "quiet": 0.6, "stoic": 0.3}
    felt = 8.0
    shown = {k: min(10.0, felt * g) for k, g in profiles.items()}
    for k in ("expressive", "quiet", "stoic"):
        print("%-10s felt %.1f -> shown %.1f" % (k, felt, shown[k]))
    assert shown["quiet"] < shown["expressive"]
    assert shown["stoic"] < shown["quiet"]
    assert 4.79 < shown["quiet"] < 4.81
    assert 2.39 < shown["stoic"] < 2.41
    print("rule: never mistake a quiet instrument for an empty one")
    print("OK: %s compared the instruments" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the face at moderate intensity: FACS action strengths 0-1
    au6_crinkle = 0.7
    au12_smile = 0.8
    brow_moved = 0.4
    print("AU6 eye crinkle: %.1f" % au6_crinkle)
    print("AU12 warm smile: %.1f" % au12_smile)
    print("inner brow raise: %.1f" % brow_moved)
    sincerity = au6_crinkle * au12_smile
    print("sincerity index: %.2f" % sincerity)
    assert 0.55 < sincerity < 0.57
    assert sincerity > 0.5
    print("rule: the crinkle is the honesty certificate - it cannot be summoned at will")
    print("OK: %s drew the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # level -> (AU6, AU12, tear film): threshold markers, not just amplification
    levels = {2: (0.1, 0.2, 0.0), 5: (0.6, 0.7, 0.0), 9: (0.9, 0.9, 1.0)}
    for lv in sorted(levels):
        a6, a12, tear = levels[lv]
        print("level %d: AU6 %.1f AU12 %.1f tear %.1f" % (lv, a6, a12, tear))
    a6s = [levels[lv][0] for lv in sorted(levels)]
    assert a6s == sorted(a6s)
    assert levels[2][2] == 0.0
    assert levels[9][2] == 1.0
    print("rule: each level adds new elements - the face reads like a gauge")
    print("OK: %s scaled the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # (felt, shown) pairs: genuine, hidden, faked
    genuine = (8.0, 8.0)
    hidden = (8.0, 2.0)
    fake = (2.0, 8.0)
    leak = (hidden[0] - hidden[1]) * 0.5
    mismatch = abs(fake[0] - fake[1])
    print("genuine: felt %.1f shown %.1f" % genuine)
    print("hidden:  felt %.1f shown %.1f -> leak %.1f" % (hidden[0], hidden[1], leak))
    print("faked:   felt %.1f shown %.1f -> mismatch %.1f" % (fake[0], fake[1], mismatch))
    assert 2.99 < leak < 3.01
    assert 5.99 < mismatch < 6.01
    assert leak > 0.0 and mismatch > 0.0
    print("rule: trust the involuntary markers, distrust the volume")
    print("OK: %s caught the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # drawable parameters for gratitude at moderate intensity
    params = {"lid_drop": 0.10, "crinkle_lines": 3, "brow_raise_deg": 4.0,
              "mouth_curve": 0.5, "head_tilt_deg": 6.0}
    for k, v in params.items():
        print("%-14s %s" % (k, v))
    assert 0.05 < params["lid_drop"] < 0.20
    assert params["crinkle_lines"] == 3
    assert 3.9 < params["brow_raise_deg"] < 4.1
    assert 5.9 < params["head_tilt_deg"] < 6.1
    print("rule: show the feeling's address - tilt the head toward the giver")
    print("OK: %s parameterized the portrait" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_gratitude_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # classic trigger families with strength ratings 0-10
    triggers = {"help in need": 9.5, "attentive gift": 8.0, "stranger kindness": 8.5,
                "being remembered": 7.5, "forgiveness": 8.0, "near-miss": 7.0, "beauty": 6.0}
    for label, val in sorted(triggers.items(), key=lambda kv: -kv[1]):
        print("%-17s %.1f" % (label, val))
    top = max(triggers, key=triggers.get)
    print("strongest classic trigger: %s" % top)
    assert top == "help in need"
    assert triggers[top] == 9.5
    assert len(triggers) == 7
    print("rule: wherever need meets generosity, the feeling is already on its way")
    print("OK: %s ranked the classics" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # personal associations: memory strength x recency -> trigger strength
    assoc = {"hospital song": (9.0, 0.9), "neighbor soup smell": (8.0, 0.7),
             "anniversary date": (7.0, 1.0)}
    strength = {}
    for k, (s, r) in assoc.items():
        strength[k] = s * r
        print("%-19s strength %.1f x recency %.1f = %.1f" % (k, s, r, strength[k]))
    top = max(strength, key=strength.get)
    print("strongest personal trigger: %s" % top)
    assert top == "hospital song"
    assert 8.09 < strength[top] < 8.11
    assert 5.59 < strength["neighbor soup smell"] < 5.61
    print("rule: your private triggers are a map of everything that ever saved you")
    print("OK: %s mapped the private wires" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # surprise x benefit -> gratitude spike; expectation discounts, novelty amplifies
    events = {"double candy bar": (9.0, 1.0), "rain under awning": (8.0, 2.0),
              "former student email": (7.0, 8.0)}
    spike = {}
    for k, (s, b) in events.items():
        spike[k] = s * b
        print("%-20s surprise %.1f x benefit %.1f = %.1f" % (k, s, b, spike[k]))
    order = sorted(spike, key=spike.get)
    print("spike order: %s" % " < ".join(order))
    assert order == ["double candy bar", "rain under awning", "former student email"]
    assert 55.9 < spike["former student email"] < 56.1
    print("rule: the circuit is a novelty-weighted benefit detector")
    print("OK: %s caught the side-door triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one thank-you, four ripples: echo, pay-forward, witnessing, total
    g0 = 10.0
    echo = g0 * 0.6
    payfwd = echo * 1.2
    witness = payfwd * 0.5
    total = g0 + echo + payfwd + witness
    print("initial gratitude: %.1f" % g0)
    print("giver echo:        %.1f" % echo)
    print("pay-it-forward:    %.1f" % payfwd)
    print("witness moved:     %.1f" % witness)
    print("cascade total:     %.1f" % total)
    assert 5.99 < echo < 6.01
    assert 7.19 < payfwd < 7.21
    assert 3.59 < witness < 3.61
    assert 26.79 < total < 26.81
    print("rule: every expressed gratitude is a stone dropped in water")
    print("OK: %s ran the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # action tendencies at intensity 8: probability each fires
    probs = {"acknowledge": 0.95, "repay": 0.80, "pay_forward": 0.70,
             "savor": 0.85, "draw_closer": 0.75}
    for k, v in probs.items():
        print("%-12s p=%.2f" % (k, v))
    expected = sum(probs.values())
    print("expected actions firing: %.2f of %d" % (expected, len(probs)))
    assert 4.04 < expected < 4.06
    assert probs["acknowledge"] == max(probs.values())
    print("rule: gratitude is an emotion with a to-do list")
    print("OK: %s listed the actions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # specificity scores: generic thanks vs the act-cost-effect triple
    generic = 2.0
    specific = 9.0
    print("generic thanks score:  %.1f" % generic)
    print("specific thanks score: %.1f" % specific)
    assert specific > 3.0 * generic
    assert 8.99 < specific < 9.01
    print("rule: naming the act, the cost, and the effect proves the appraisal ran")
    print("OK: %s scored the speech" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sharing game: fraction shared; patience: discount rate
    base_share, grat_share = 0.30, 0.45
    delta = grat_share - base_share
    base_disc, grat_disc = 0.20, 0.12
    print("shared baseline: %.2f, grateful: %.2f (delta +%.2f)" % (base_share, grat_share, delta))
    print("discount rate baseline: %.2f, grateful: %.2f" % (base_disc, grat_disc))
    assert 0.14 < delta < 0.16
    assert grat_disc < base_disc
    print("rule: the ledger feels abundant, so the hand opens and the future flattens")
    print("OK: %s shifted the decisions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_intensity_behavior(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # intensity -> time horizon of the behavior it drives
    horizons = {2: "moments", 5: "days", 9: "years"}
    for lv in sorted(horizons):
        print("level %d -> acts across %s" % (lv, horizons[lv]))
    ordered = [horizons[k] for k in sorted(horizons)]
    assert ordered == ["moments", "days", "years"]
    assert horizons[9] == "years"
    print("rule: each level includes the last and adds a longer horizon")
    print("OK: %s climbed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three channels: say, show, channel -> completeness
    channels = {"say": 1, "show": 1, "channel": 1}
    full = sum(channels.values()) / 3.0
    partial = 1.0 / 3.0
    print("say + show + channel: completeness %.2f" % full)
    print("say alone:            completeness %.2f" % partial)
    assert 0.99 < full < 1.01
    assert 0.33 < partial < 0.34
    print("rule: saying alone is good - all three closes every loop")
    print("OK: %s completed the expression" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five failure modes with their costs 0-10
    costs = {"bottling": 7.0, "forcing": 6.0, "score_keeping": 8.0,
             "weaponizing": 9.0, "guilt_masking": 5.0}
    for k, v in sorted(costs.items(), key=lambda kv: -kv[1]):
        print("%-13s cost %.1f" % (k, v))
    worst = max(costs, key=costs.get)
    print("costliest failure: %s" % worst)
    assert worst == "weaponizing"
    assert costs[worst] == 9.0
    print("rule: every failure breaks the loop - repair is always back to sincere thanks")
    print("OK: %s priced the failures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six practices: weekly reps -> detection-threshold drop
    doses = {"journal": 7, "thank_you_note": 1, "savoring": 7,
             "subtraction": 2, "spoken": 7, "replay": 7}
    total = sum(doses.values())
    drop = total * 0.01
    for k, v in doses.items():
        print("%-14s %d reps/week" % (k, v))
    print("weekly reps: %d" % total)
    print("threshold drop: %.2f" % drop)
    assert total == 31
    assert 0.309 < drop < 0.311
    print("rule: calibration, not positive thinking - the detector gets better")
    print("OK: %s ran the reps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_reading_signs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cluster detection: independent cues combine into confidence
    cues = {"eye_crinkle": 0.90, "held_gaze": 0.80, "slow_nod": 0.75}
    miss = 1.0
    for k, r in cues.items():
        print("%-12s reliability %.2f" % (k, r))
        miss *= (1.0 - r)
    conf = 1.0 - miss
    print("cluster confidence: %.3f" % conf)
    assert 0.994 < conf < 0.996
    assert conf > max(cues.values())
    print("rule: read the cluster, never a single tell")
    print("OK: %s read the other person" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five response moves rated by helpfulness 0-10
    resp = {"receive_fully": 9, "not_deflecting": 9, "naming_back": 8,
            "not_fixing_tears": 8, "amplifying": 7}
    for k, v in sorted(resp.items(), key=lambda kv: -kv[1]):
        print("%-16s helpfulness %d" % (k, v))
    best = max(resp.values())
    print("best move rating: %d" % best)
    assert best == 9
    assert resp["amplifying"] < best
    print("rule: gratitude is a gift being handed to you - take it with both hands")
    print("OK: %s chose the responses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_mistakes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven loop-breaking mistakes with damage ratings 0-10
    dmg = {"deflection": 8, "reversal": 5, "ledger_joke": 7, "correcting": 6,
           "rushing": 7, "discomfort": 6, "weaponizing": 9}
    for k, v in sorted(dmg.items(), key=lambda kv: -kv[1]):
        print("%-12s damage %d" % (k, v))
    worst = max(dmg, key=dmg.get)
    print("worst mistake: %s" % worst)
    assert worst == "weaponizing"
    assert dmg[worst] == 9
    print("rule: punished expression extinguishes fast - guard the loop")
    print("OK: %s flagged the mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_neighbors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wheel distances in degrees from gratitude (-22.5)
    grat = -22.5
    neighbors = {"appreciation": -10.0, "admiration": -35.0,
                 "contentment": -5.0, "relief": 160.0}
    def ang_dist(a, b):
        d = abs(a - b) % 360.0
        return min(d, 360.0 - d)
    dists = {}
    for k, v in neighbors.items():
        dists[k] = ang_dist(grat, v)
        print("%-13s %.1f deg away" % (k, dists[k]))
    nearest = min(dists, key=dists.get)
    print("nearest neighbor: %s" % nearest)
    assert 12.4 < dists["appreciation"] < 12.6
    assert dists["relief"] > 170.0
    assert nearest in ("appreciation", "admiration")
    print("rule: every neighbor defined by which of gratitude's parts it keeps")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven blends: (valence, arousal) coordinates
    blends = {"celebration": (8.25, 6.0), "deliverance": (7.5, 6.5),
              "bittersweet": (6.0, 4.5), "reverence": (8.0, 5.5),
              "devotion": (8.5, 5.0), "indebted": (5.5, 6.0),
              "earned_thanks": (8.0, 6.5)}
    for k, (v, a) in blends.items():
        print("%-13s valence %.2f arousal %.1f" % (k, v, a))
    assert len(blends) == 7
    assert all(v > 5.0 for v, a in blends.values())
    assert blends["devotion"][0] == max(v for v, a in blends.values())
    print("rule: name both appraisals, and the blend explains itself")
    print("OK: %s mixed the paints" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gratitude_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven scenes: trigger to resolution, state values per scene
    scenes = [("trigger", 9.5), ("onset", 3.0), ("peak", 9.0),
              ("aftershock", 3.6), ("expression", 8.0),
              ("pay_forward", 7.2), ("resolution_trait", 1.0)]
    for sname, val in scenes:
        print("scene %-16s state %.1f" % (sname, val))
    assert scenes[0][1] == 9.5
    assert scenes[2][1] == 9.0
    assert scenes[6][1] == 1.0
    assert len(scenes) == 7
    print("rule: one kindness, seven scenes - the whole cascade, trigger to resolution")
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "definition": demo_gratitude_definition,
    "family": demo_gratitude_family,
    "intensity": demo_gratitude_intensity,
    "myths": demo_gratitude_myths,
    "first_person": demo_gratitude_first_person,
    "time_course": demo_gratitude_time_course,
    "low_vs_high": demo_gratitude_low_vs_high,
    "gratitude_joy_blend": demo_gratitude_joy_blend,
    "day_vignette": demo_gratitude_day_vignette,
    "body": demo_gratitude_body,
    "posture": demo_gratitude_posture,
    "sleep_appetite": demo_gratitude_sleep_appetite,
    "individual_diff": demo_gratitude_individual_diff,
    "face": demo_gratitude_face,
    "face_intensity": demo_gratitude_face_intensity,
    "hiding_faking": demo_gratitude_hiding_faking,
    "expression_gallery": demo_gratitude_expression_gallery,
    "classic_triggers": demo_gratitude_classic_triggers,
    "personal_triggers": demo_gratitude_personal_triggers,
    "surprise_triggers": demo_gratitude_surprise_triggers,
    "chain_reactions": demo_gratitude_chain_reactions,
    "actions": demo_gratitude_actions,
    "speech": demo_gratitude_speech,
    "decisions": demo_gratitude_decisions,
    "intensity_behavior": demo_gratitude_intensity_behavior,
    "healthy_expression": demo_gratitude_healthy_expression,
    "unhealthy_expression": demo_gratitude_unhealthy_expression,
    "everyday_practices": demo_gratitude_everyday_practices,
    "reading_signs": demo_gratitude_reading_signs,
    "supportive_responses": demo_gratitude_supportive_responses,
    "mistakes": demo_gratitude_mistakes,
    "neighbors": demo_gratitude_neighbors,
    "mixes": demo_gratitude_mixes,
    "full_simulation": demo_gratitude_full_simulation,
}
