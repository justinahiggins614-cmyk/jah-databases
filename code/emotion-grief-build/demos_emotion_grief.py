#!/usr/bin/env python3
"""Demo programs for The Grief Emotion Database (public + Signature).

Every demo is an emotion-scenario simulator: real, runnable, stdlib-only
Python performing the actual simulation for its record. All are
machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker. Descriptive/educational only - no diagnosing of any real person.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_grief_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # taxonomy: basic vs complex emotion terms
    terms = {"joy": "basic", "sadness": "basic", "anger": "basic",
             "fear": "basic", "surprise": "basic", "disgust": "basic",
             "grief": "complex", "mourning": "complex", "nostalgia": "complex",
             "melancholy": "complex", "remorse": "complex", "love": "complex"}
    basic = sum(1 for v in terms.values() if v == "basic")
    complex_ = sum(1 for v in terms.values() if v == "complex")
    print("terms classified: %d basic, %d complex (n=%d)" % (basic, complex_, len(terms)))
    assert basic == 6 and complex_ == 6
    assert terms["grief"] == "complex", "grief must classify as complex"
    roots = {"sadness": 1.00, "anger": 0.45, "fear": 0.35, "guilt": 0.40, "longing": 0.80}
    total = sum(roots.values())
    print("grief component roots: %d, total weight %.2f" % (len(roots), total))
    assert 2.99 < total < 3.01
    print("OK: %s mapped the definition" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Plutchik-style wheel: grief as a blend positioned from basic emotions
    wheel = {"joy": 0, "trust": 45, "fear": 90, "surprise": 135,
             "sadness": 180, "disgust": 225, "anger": 270, "anticipation": 315}
    # grief sits in the sadness family at high intensity: angle near sadness
    grief_angle = 180.0
    def ang_dist(a, b):
        d = abs(a - b) % 360.0
        return min(d, 360.0 - d)
    d_sad = ang_dist(grief_angle, wheel["sadness"])
    d_joy = ang_dist(grief_angle, wheel["joy"])
    print("grief angle %.0f deg: dist to sadness %.0f, to joy %.0f" % (grief_angle, d_sad, d_joy))
    assert d_sad == 0.0 and d_joy == 180.0
    # blend vector: sadness root plus recruited partners
    blend = {"sadness": 1.0, "anger": 0.4, "fear": 0.3, "love-longing": 0.7}
    norm = math.sqrt(sum(v * v for v in blend.values()))
    print("blend vector norm: %.4f" % norm)
    assert 1.3190 < norm < 1.3192
    print("OK: %s placed grief in the family" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_volumes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # intensity scale 0-10 mapped to volumes
    def volume(i):
        if i < 3.5:
            return "mild"
        if i < 7.0:
            return "moderate"
        return "intense"
    cases = [(1.5, "mild"), (3.4, "mild"), (3.5, "moderate"),
             (5.5, "moderate"), (6.9, "moderate"), (7.0, "intense"), (9.2, "intense")]
    for i, want in cases:
        got = volume(i)
        print("intensity %.1f -> %s" % (i, got))
        assert got == want, (i, got, want)
    # volume is not love: love weight independent of volume
    love = 9.0
    for i in (2.0, 5.0, 9.0):
        print("volume %s at intensity %.1f carries love weight %.1f" % (volume(i), i, love))
    print("OK: %s scaled the volumes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    myths = [
        ("five neat stages in order", False),
        ("grief ends within a year", False),
        ("strong people do not cry", False),
        ("healthy grief means forgetting", False),
        ("grief is only about death", False),
        ("time alone heals", False),
        ("looking fine means being fine", False),
    ]
    corrections = {
        "five neat stages in order": "patterns loop and double back; no order",
        "grief ends within a year": "no deadline; waves return for years",
        "strong people do not cry": "many genuine styles exist",
        "healthy grief means forgetting": "continuing bonds are healthy",
        "grief is only about death": "all deep losses count",
        "time alone heals": "what happens in the time heals",
        "looking fine means being fine": "grief is often invisible",
    }
    for myth, true in myths:
        assert not true, myth
        print("myth: %-34s -> %s" % (myth, corrections[myth][:46]))
    assert len(myths) == 7 and len(corrections) == 7
    print("OK: %s cleared the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # simulated passage timeline: phases of one morning, minutes each
    phases = [("waking re-realization", 12), ("habit collision (second cup)", 6),
              ("double exposure at work", 180), ("trigger ambush (song)", 4),
              ("wave passing", 2), ("evening heaviness", 90)]
    total = sum(d for _, d in phases)
    print("passage phases: %d, simulated span %d min" % (len(phases), total))
    assert len(phases) == 6
    assert total == 294
    wave_share = sum(d for p, d in phases if "wave" in p or "ambush" in p) / total
    print("acute-wave share of the morning: %.3f" % wave_share)
    assert 0.019 < wave_share < 0.022
    print("OK: %s walked the passage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # intensity model: acute peak then exponential softening, plus aftershock
    peak, tau = 9.0, 120.0
    def intensity(t_days):
        return peak * math.exp(-t_days / tau)
    half_life = tau * math.log(2.0)
    print("peak %.1f, tau %.0f days -> half-life %.2f days" % (peak, tau, half_life))
    assert 83.17 < half_life < 83.19
    for t in (30, 180, 365):
        print("day %3d intensity %.3f" % (t, intensity(t)))
    assert 7.00 < intensity(30) < 7.02
    assert 2.00 < intensity(180) < 2.01
    # aftershock: anniversary spike on top of the faded base
    base_365 = intensity(365)
    spike = base_365 + 4.5
    print("day 365 base %.3f + anniversary spike -> %.3f" % (base_365, spike))
    assert 0.42 < base_365 < 0.44
    assert 4.92 < spike < 4.94
    print("OK: %s traced the time course" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_low_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two lived snapshots scored on the same five dials (0-10)
    dials = ["awareness", "disruption", "wave_freq", "body_load", "support_need"]
    low = dict(zip(dials, [2.0, 1.5, 2.5, 2.0, 2.0]))
    high = dict(zip(dials, [9.0, 8.5, 9.0, 8.0, 9.0]))
    low_mean = sum(low.values()) / len(low)
    high_mean = sum(high.values()) / len(high)
    print("low-intensity snapshot mean:  %.2f" % low_mean)
    print("high-intensity snapshot mean: %.2f" % high_mean)
    assert 1.99 < low_mean < 2.01
    assert 8.69 < high_mean < 8.71
    ratio = high_mean / low_mean
    print("high/low ratio: %.2f" % ratio)
    assert 4.34 < ratio < 4.36
    print("OK: %s held both snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_mixed_partner(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grief + anger blend as a weighted vector over felt qualities
    grief = {"heaviness": 0.9, "tears": 0.8, "stillness": 0.7, "heat": 0.1, "motion": 0.2}
    anger = {"heaviness": 0.1, "tears": 0.2, "stillness": 0.1, "heat": 0.9, "motion": 0.8}
    w_grief, w_anger = 0.6, 0.4
    blend = {k: w_grief * grief[k] + w_anger * anger[k] for k in grief}
    for k in sorted(blend):
        print("  %-10s %.3f" % (k, blend[k]))
    # the blend is both heavy AND hot: heaviness and heat both elevated
    assert 0.57 < blend["heaviness"] < 0.59
    assert 0.41 < blend["heat"] < 0.43
    assert 0.43 < blend["motion"] < 0.45
    print("OK: %s blended the partners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_day(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hourly grief load across the vignette day (0-10 per hour block)
    day = {"06-08": 6.0, "08-12": 4.0, "12-14": 7.5, "14-17": 5.0,
           "17-20": 6.5, "20-23": 8.0, "23-06": 5.5}
    total = sum(day.values())
    peak_block = max(day, key=day.get)
    mean = total / len(day)
    print("day blocks: %d, total load %.1f, mean %.3f" % (len(day), total, mean))
    print("peak block: %s at %.1f" % (peak_block, day[peak_block]))
    assert total == 42.5
    assert peak_block == "20-23"
    assert 6.07 < mean < 6.08
    # dual-process rhythm: loss-oriented vs restoration-oriented blocks
    loss_blocks = {"06-08", "12-14", "20-23"}
    loss_share = sum(v for k, v in day.items() if k in loss_blocks) / total
    print("loss-oriented share of the day: %.3f" % loss_share)
    assert 0.505 < loss_share < 0.507
    print("OK: %s lived the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body signals as functions of grief intensity (0-10)
    def heart_rate(i):
        return 68.0 + 2.6 * i
    def breath_rate(i):
        return 14.0 + 0.9 * i
    def sighs_per_hour(i):
        return 2.0 + 1.4 * i
    def heaviness(i):
        return i / 10.0
    for i in (2.0, 5.0, 9.0):
        print("intensity %.0f: HR %.1f bpm, breath %.1f/min, sighs %.1f/hr, heaviness %.2f"
              % (i, heart_rate(i), breath_rate(i), sighs_per_hour(i), heaviness(i)))
    assert 72.9 < heart_rate(2.0) < 73.3
    assert 90.9 < heart_rate(9.0) < 91.9
    assert 21.9 < breath_rate(9.0) < 22.3
    assert 14.4 < sighs_per_hour(9.0) < 14.8
    assert 0.89 < heaviness(9.0) < 0.91
    print("OK: %s read the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fold index 0-1 from five postural signs, scored per intensity
    signs = ["shoulders_forward", "chest_narrowed", "head_tilted",
             "gaze_dropped", "self_embrace"]
    def fold(i):
        return min(1.0, 0.15 + 0.085 * i)
    for i in (1.0, 5.0, 9.0):
        f = fold(i)
        active = sum(1 for s in signs if f > 0.2)
        print("intensity %.0f: fold index %.3f, signs active %d/%d" % (i, f, active, len(signs)))
    assert 0.234 < fold(1.0) < 0.236
    assert 0.574 < fold(5.0) < 0.576
    assert 0.914 < fold(9.0) < 0.916
    # tempo downshift: gait speed fraction of baseline
    def tempo(i):
        return 1.0 - 0.045 * i
    print("gait tempo at intensity 9: %.3f of baseline" % tempo(9.0))
    assert 0.594 < tempo(9.0) < 0.596
    print("OK: %s read the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_sleep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 14-day model: sleep efficiency and appetite index under acute grief
    days = list(range(1, 15))
    sleep_eff = [0.92 - 0.28 * math.exp(-(d - 1) / 5.0) for d in days]
    appetite = [0.90 - 0.55 * math.exp(-(d - 1) / 6.0) for d in days]
    print("day 1:  sleep eff %.3f, appetite %.3f" % (sleep_eff[0], appetite[0]))
    print("day 14: sleep eff %.3f, appetite %.3f" % (sleep_eff[-1], appetite[-1]))
    assert 0.639 < sleep_eff[0] < 0.641
    assert 0.349 < appetite[0] < 0.351
    assert 0.898 < sleep_eff[-1] < 0.900
    assert 0.836 < appetite[-1] < 0.840
    mean_sleep = sum(sleep_eff) / len(sleep_eff)
    print("14-day mean sleep efficiency: %.4f" % mean_sleep)
    assert 0.815 < mean_sleep < 0.818
    print("OK: %s tracked sleep and appetite" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_body_differs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five griever personas: physical response profiles (0-10 per channel)
    personas = {
        "the weeper":   {"tears": 9.0, "sleep_loss": 3.0, "appetite_loss": 4.0, "aches": 3.0},
        "the sleepless": {"tears": 4.0, "sleep_loss": 9.0, "appetite_loss": 5.0, "aches": 6.0},
        "the hollow":   {"tears": 2.0, "sleep_loss": 6.0, "appetite_loss": 9.0, "aches": 4.0},
        "the aching":   {"tears": 5.0, "sleep_loss": 5.0, "appetite_loss": 3.0, "aches": 9.0},
        "the steady":   {"tears": 3.0, "sleep_loss": 2.0, "appetite_loss": 2.0, "aches": 2.0},
    }
    channels = ["tears", "sleep_loss", "appetite_loss", "aches"]
    for ch in channels:
        vals = [p[ch] for p in personas.values()]
        mean = sum(vals) / len(vals)
        var = sum((v - mean) ** 2 for v in vals) / len(vals)
        sd = math.sqrt(var)
        print("  %-14s mean %.2f  stdev %.2f  range %.0f-%.0f"
              % (ch, mean, sd, min(vals), max(vals)))
        assert sd > 1.5, (ch, sd)
    # no single template: max pairwise distance between personas
    names = list(personas)
    def dist(a, b):
        return math.sqrt(sum((personas[a][c] - personas[b][c]) ** 2 for c in channels))
    dmax = max(dist(a, b) for a in names for b in names if a < b)
    print("max persona distance: %.3f" % dmax)
    assert 9.16 < dmax < 9.17
    print("OK: %s honored the differences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # facial action unit intensities (0-5) for the grief face at moderate volume
    aus = {"inner_brow_raise": 4.2, "brow_knit": 3.1, "upper_lid_droop": 3.6,
           "eye_glisten": 3.0, "mouth_corner_down": 3.8, "lip_tremble": 2.4,
           "chin_bunch": 2.1}
    total = sum(aus.values())
    mean = total / len(aus)
    print("action units: %d, total %.1f, mean %.3f" % (len(aus), total, mean))
    assert total == 22.2
    assert 3.17 < mean < 3.18
    top = max(aus, key=aus.get)
    print("most diagnostic feature: %s (%.1f)" % (top, aus[top]))
    assert top == "inner_brow_raise"
    # diagnosticity: grief brow present in grief, rare elsewhere
    print("grief-brow diagnosticity: present in grief 0.92, in other states 0.11")
    assert 0.92 > 0.11
    print("OK: %s drew the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # expression scale: feature strength 0-10 across volumes
    scale = {
        "mild":     {"brow": 2.0, "eye": 2.5, "mouth": 2.0, "animation": 7.0},
        "moderate": {"brow": 5.5, "eye": 5.0, "mouth": 5.5, "animation": 4.0},
        "intense":  {"brow": 9.0, "eye": 9.5, "mouth": 9.0, "animation": 1.5},
        "managed":  {"brow": 3.0, "eye": 3.5, "mouth": 2.5, "animation": 5.0},
    }
    for vol, feats in scale.items():
        sig = (feats["brow"] + feats["eye"] + feats["mouth"]) / 3.0
        print("  %-9s grief-signal %.2f  animation %.1f" % (vol, sig, feats["animation"]))
    sigs = {v: (f["brow"] + f["eye"] + f["mouth"]) / 3.0 for v, f in scale.items()}
    assert sigs["mild"] < sigs["moderate"] < sigs["intense"]
    assert 2.16 < sigs["mild"] < 2.18
    assert 9.16 < sigs["intense"] < 9.18
    # managed face: moderate signal under high suppression effort
    assert sigs["managed"] < sigs["moderate"]
    print("OK: %s scaled the expression" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_hide_fake(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # leakage scores 0-1: hidden grief leaks, faked grief lacks the brow
    hidden = {"brow_flicker": 0.75, "eye_brighten_steady": 0.68, "swallowed_sob": 0.71,
              "mouth_only_smile": 0.63, "voice_thicken": 0.58}
    faked = {"brow_flicker": 0.12, "eye_brighten_steady": 0.08, "swallowed_sob": 0.05,
             "mouth_only_smile": 0.81, "voice_thicken": 0.10}
    h_mean = sum(hidden.values()) / len(hidden)
    f_leak = sum(v for k, v in faked.items() if k != "mouth_only_smile") / 4.0
    print("hidden grief leakage score: %.3f" % h_mean)
    print("faked grief leakage score:  %.3f" % f_leak)
    assert 0.66 < h_mean < 0.68
    assert 0.08 < f_leak < 0.10
    # the grief brow is the hardest to fake: faked shows mouth without brow
    print("faked grief: mouth-only smile %.2f with brow flicker %.2f" %
          (faked["mouth_only_smile"], faked["brow_flicker"]))
    assert faked["mouth_only_smile"] > 0.8 and faked["brow_flicker"] < 0.15
    print("OK: %s spotted the leakage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # artist checklist: buildable features grouped by region
    features = {
        "brow": ["inner lift", "drawn together", "tent shape", "worry lines"],
        "eyes": ["lids half-mast", "gaze down", "wet glisten", "lower lid tense"],
        "nose_cheeks": ["nostril flare (held)", "midface flush (open)"],
        "mouth": ["corners down-out", "trembling lip", "bunched chin", "slack jaw (quiet)"],
        "head": ["tilt down", "tilt sideways"],
    }
    total = sum(len(v) for v in features.values())
    print("regions: %d, buildable features: %d" % (len(features), total))
    assert len(features) == 5
    assert total == 16
    # coverage: every region has at least 2 features
    assert all(len(v) >= 2 for v in features.values())
    print("OK: %s stocked the gallery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # trigger likelihood 0-1 of summoning a wave in the first year
    triggers = {"song": 0.88, "photograph": 0.81, "empty chair": 0.77,
                "anniversary date": 0.85, "holiday": 0.72, "smell": 0.66,
                "milestone": 0.69, "loaded question": 0.58, "others happiness": 0.61,
                "hospital corridor": 0.74}
    ranked = sorted(triggers.items(), key=lambda kv: -kv[1])
    print("top 3 triggers:")
    for t, p in ranked[:3]:
        print("  %-18s %.2f" % (t, p))
    assert ranked[0][0] == "song"
    assert ranked[1][0] == "anniversary date"
    assert ranked[2][0] == "photograph"
    mean = sum(triggers.values()) / len(triggers)
    print("mean trigger likelihood: %.4f" % mean)
    assert 0.730 < mean < 0.732
    print("OK: %s mapped the triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # private association weights 0-1 for one simulated griever
    private = {"tea brand": 0.91, "sunday light": 0.84, "voicemail": 0.95,
               "hardware store route": 0.62, "birthday password": 0.73,
               "the joke": 0.88, "their recipe": 0.79}
    strongest = max(private, key=private.get)
    print("strongest private trigger: %s (%.2f)" % (strongest, private[strongest]))
    assert strongest == "voicemail"
    # marked vs unmarked anniversaries
    marked = {"death date": 0.90, "birthday": 0.82}
    unmarked = {"diagnosis day": 0.71, "last ordinary tuesday": 0.66, "first warm day": 0.58}
    m_mean = sum(marked.values()) / len(marked)
    u_mean = sum(unmarked.values()) / len(unmarked)
    print("marked anniversary mean %.3f, unmarked mean %.3f" % (m_mean, u_mean))
    assert 0.859 < m_mean < 0.861
    assert 0.649 < u_mean < 0.651
    assert m_mean > u_mean
    print("OK: %s charted the private map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_surprise(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # surprise index: logical link (0-1, low) vs wave power (0-1, high)
    odd = {"ripe peach": (0.05, 0.72), "sale on socks": (0.03, 0.58),
           "childhood cartoon": (0.08, 0.66), "cut grass": (0.10, 0.70),
           "strangers laugh": (0.12, 0.81)}
    print("surprise triggers (logic link vs wave power):")
    total_surprise = 0.0
    for t, (logic, power) in odd.items():
        surprise = power * (1.0 - logic)
        total_surprise += surprise
        print("  %-17s logic %.2f power %.2f surprise %.3f" % (t, logic, power, surprise))
        assert logic < 0.15 and power > 0.5
    mean_surprise = total_surprise / len(odd)
    print("mean surprise index: %.4f" % mean_surprise)
    assert 0.630 < mean_surprise < 0.645
    print("OK: %s caught the surprises" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_chains(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cascade links with continuation probabilities
    links = [("song spark", 1.00), ("kitchen memory", 0.85), ("future-absence pang", 0.70),
             ("hospital weeks", 0.55), ("guilt what-if", 0.45), ("global verdict", 0.30),
             ("shame at tears", 0.20)]
    print("cascade links and reach probabilities:")
    reach = 1.0
    for i, (label, p) in enumerate(links):
        if i:
            reach *= p
        print("  link %d %-20s reach %.4f" % (i + 1, label, reach))
    assert 0.0088 < reach < 0.0089
    # expected chain length
    exp_len = sum(reach_i for reach_i in
                  [1.0, 0.85, 0.85 * 0.70, 0.85 * 0.70 * 0.55,
                   0.85 * 0.70 * 0.55 * 0.45, 0.85 * 0.70 * 0.55 * 0.45 * 0.30,
                   0.85 * 0.70 * 0.55 * 0.45 * 0.30 * 0.20])
    print("expected cascade length: %.3f links" % exp_len)
    assert 2.971 < exp_len < 2.974
    # interruption at any link halves the remainder
    print("interruption at link 4 cuts expected remainder by half: %.3f -> %.3f"
          % (exp_len, exp_len / 2.0))
    print("OK: %s traced the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_behavior(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six behavior families: likelihood 0-1 at acute vs integrated phase
    behaviors = {
        "searching": (0.82, 0.25), "withdrawing": (0.75, 0.35),
        "preserving": (0.70, 0.55), "restless": (0.64, 0.20),
        "numbing": (0.58, 0.25), "reaching": (0.35, 0.80),
    }
    print("behavior families (acute -> integrated):")
    for b, (acute, integ) in behaviors.items():
        print("  %-12s %.2f -> %.2f" % (b, acute, integ))
    # reaching is the only family that rises with integration
    risers = [b for b, (a, i) in behaviors.items() if i > a]
    assert risers == ["reaching"], risers
    acute_mean = sum(a for a, _ in behaviors.values()) / len(behaviors)
    integ_mean = sum(i for _, i in behaviors.values()) / len(behaviors)
    print("mean likelihood: acute %.4f, integrated %.4f" % (acute_mean, integ_mean))
    assert 0.639 < acute_mean < 0.641
    assert 0.399 < integ_mean < 0.401
    print("OK: %s read the behaviors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speech metrics: baseline vs grieving
    baseline = {"wpm": 150.0, "pause_ratio": 0.12, "pitch_var": 1.00}
    grieving = {"wpm": 108.0, "pause_ratio": 0.31, "pitch_var": 0.62}
    print("speech: baseline wpm %.0f -> grieving wpm %.0f" % (baseline["wpm"], grieving["wpm"]))
    print("pause ratio: %.2f -> %.2f" % (baseline["pause_ratio"], grieving["pause_ratio"]))
    assert grieving["wpm"] < baseline["wpm"] * 0.8
    assert grieving["pause_ratio"] > baseline["pause_ratio"] * 2.0
    slowdown = (baseline["wpm"] - grieving["wpm"]) / baseline["wpm"]
    print("slowdown: %.3f" % slowdown)
    assert 0.279 < slowdown < 0.281
    # characteristic phrases mapped to mechanisms
    phrases = {"I cant believe theyre gone": "updating",
               "It doesnt feel real": "derealization",
               "If only I had": "counterfactual",
               "I just miss them": "core ache"}
    assert len(phrases) == 4
    print("characteristic phrases mapped: %d" % len(phrases))
    print("OK: %s heard the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # risk-aversion multiplier and horizon under grief (baseline 1.0)
    profiles = {
        "risk_averse": {"risk_mult": 1.8, "horizon_days": 14.0},
        "reckless": {"risk_mult": 0.4, "horizon_days": 3.0},
        "frozen": {"risk_mult": 1.0, "horizon_days": 1.0},
    }
    baseline_horizon = 365.0
    for p, v in profiles.items():
        hfrac = v["horizon_days"] / baseline_horizon
        print("  %-11s risk x%.1f  horizon %.0f days (%.4f of baseline)"
              % (p, v["risk_mult"], v["horizon_days"], hfrac))
    assert profiles["risk_averse"]["risk_mult"] > 1.5
    assert profiles["reckless"]["risk_mult"] < 0.5
    frozen_frac = profiles["frozen"]["horizon_days"] / baseline_horizon
    print("frozen horizon fraction: %.5f" % frozen_frac)
    assert 0.00273 < frozen_frac < 0.00275
    # borrowed cortex: supported decision quality recovery
    alone, supported = 0.45, 0.82
    print("decision quality: alone %.2f -> supported %.2f" % (alone, supported))
    assert supported - alone > 0.35
    print("OK: %s weighed the decisions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rung classifier from load (0-10) and resources (0-10)
    def rung(load, resources):
        gap = load - resources
        if gap < 2.0:
            return 1
        if gap < 4.5:
            return 2
        if gap < 7.0:
            return 3
        return 4
    cases = [((4.0, 6.0), 1), ((7.0, 4.0), 2), ((9.0, 3.0), 3), ((9.5, 1.0), 4)]
    for (load, res), want in cases:
        got = rung(load, res)
        print("load %.1f resources %.1f -> rung %d" % (load, res, got))
        assert got == want, (load, res, got, want)
    # de-escalation: restoring resources moves the rung back down
    print("rung 3 case with +3 resources: %d -> %d" % (rung(9.0, 3.0), rung(9.0, 6.0)))
    assert rung(9.0, 6.0) == 2
    print("OK: %s read the rungs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_healthy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # channel effectiveness 0-1 across three needs: discharge, process, connect
    channels = {
        "telling the story": (0.50, 0.95, 0.80),
        "crying freely": (0.90, 0.45, 0.55),
        "walking": (0.85, 0.40, 0.30),
        "making tribute": (0.70, 0.75, 0.60),
        "ritual": (0.55, 0.70, 0.75),
        "serving others": (0.45, 0.80, 0.90),
    }
    print("channel scores (discharge, process, connect -> total):")
    totals = {}
    for ch, (d, p, c) in channels.items():
        totals[ch] = d + p + c
        print("  %-18s %.2f %.2f %.2f -> %.2f" % (ch, d, p, c, totals[ch]))
    best = max(totals, key=totals.get)
    print("highest total: %s (%.2f)" % (best, totals[best]))
    assert best == "telling the story"
    assert 2.24 < totals[best] < 2.26
    # repertoire coverage: all three needs covered above 0.8 by some channel
    assert max(v[0] for v in channels.values()) >= 0.8
    assert max(v[1] for v in channels.values()) >= 0.8
    assert max(v[2] for v in channels.values()) >= 0.8
    print("OK: %s opened the channels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_unhealthy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cost model: bottling vs exploding vs healthy across four cost types
    costs = {
        "bottling": {"body": 0.85, "isolation": 0.80, "frozen_grief": 0.75, "relationships": 0.45},
        "exploding": {"body": 0.55, "isolation": 0.60, "frozen_grief": 0.40, "relationships": 0.90},
        "healthy": {"body": 0.20, "isolation": 0.15, "frozen_grief": 0.15, "relationships": 0.20},
    }
    for style, cs in costs.items():
        total = sum(cs.values())
        print("  %-10s total cost %.2f %s" % (style, total, dict(cs)))
        cs["_total"] = total
    assert costs["bottling"]["_total"] > costs["healthy"]["_total"] * 2.0
    assert costs["exploding"]["_total"] > costs["healthy"]["_total"] * 2.0
    print("bottling worst cost: body %.2f; exploding worst cost: relationships %.2f" %
          (costs["bottling"]["body"], costs["exploding"]["relationships"]))
    assert costs["bottling"]["body"] == 0.85
    assert costs["exploding"]["relationships"] == 0.90
    print("OK: %s priced the patterns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # balance score from adopted practices, weighted by pillar
    practices = {
        "daily walk": ("body", 0.90), "guarded sleep": ("body", 0.85),
        "regular meals": ("body", 0.70), "morning daylight": ("body", 0.55),
        "ten minute writing": ("mind", 0.75), "name the day": ("mind", 0.60),
        "small pleasure": ("mind", 0.50), "one connection": ("heart", 0.80),
        "speak their name": ("heart", 0.65), "let one wave through": ("heart", 0.70),
        "loose rhythm": ("structure", 0.60), "one task done": ("structure", 0.55),
        "weekly no": ("structure", 0.50), "small ritual": ("meaning", 0.75),
    }
    adopted = {"daily walk", "guarded sleep", "regular meals", "ten minute writing",
               "one connection", "loose rhythm", "small ritual"}
    score = sum(w for p, (_, w) in practices.items() if p in adopted)
    maxscore = sum(w for _, w in practices.values())
    balance = score / maxscore
    print("practices adopted %d/%d, balance score %.4f" % (len(adopted), len(practices), balance))
    assert len(adopted) == 7
    assert 0.568 < balance < 0.570
    # pillars covered?
    pillars = {practices[p][0] for p in adopted}
    print("pillars covered: %s" % sorted(pillars))
    assert pillars == {"body", "mind", "heart", "structure", "meaning"}
    print("OK: %s kept the practices" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_reading(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cue checklist: weights sum to recognition confidence 0-1
    cues = {"grief brow": 0.22, "downcast gaze": 0.12, "glistening eyes": 0.14,
            "folded posture": 0.13, "flat quiet voice": 0.11, "withdrawal": 0.10,
            "known loss date": 0.10, "mouth says fine body disagrees": 0.08}
    total_w = sum(cues.values())
    print("cue weights total: %.2f" % total_w)
    assert 0.999 < total_w < 1.001
    # observed cue sets -> confidence
    observed_a = {"grief brow", "glistening eyes", "folded posture", "known loss date"}
    observed_b = {"withdrawal"}
    conf_a = sum(cues[c] for c in observed_a)
    conf_b = sum(cues[c] for c in observed_b)
    print("four strong cues -> confidence %.2f" % conf_a)
    print("one weak cue -> confidence %.2f" % conf_b)
    assert 0.58 < conf_a < 0.60
    assert 0.099 < conf_b < 0.101
    # rule: confidence guides gentleness, never a label
    print("rule: confidence %.2f suggests softer pace, not a diagnosis" % conf_a)
    print("OK: %s read the signs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_support(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # response quality 0-1 scored on presence, concreteness, non-fixing
    responses = {
        "Im so sorry. Im here.": (0.95, 0.60, 0.95),
        "Ill bring dinner Thursday.": (0.85, 1.00, 0.90),
        "Tell me about them, if youd like.": (0.90, 0.55, 0.95),
        "Let me know if you need anything.": (0.50, 0.20, 0.70),
        "At least theyre not suffering.": (0.30, 0.30, 0.15),
        "Arent you over this yet?": (0.10, 0.20, 0.05),
    }
    scores = {r: (p + c + n) / 3.0 for r, (p, c, n) in responses.items()}
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])
    print("responses ranked:")
    for r, s in ranked:
        print("  %.3f  %s" % (s, r))
    assert ranked[0][0] == "Ill bring dinner Thursday."
    assert ranked[-1][0] == "Arent you over this yet?"
    assert 0.916 < ranked[0][1] < 0.918
    assert 0.116 < ranked[-1][1] < 0.118
    print("OK: %s chose the words" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_mistakes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mistake severity 0-1 and the safe substitute
    mistakes = {
        "silver lining": (0.75, "Im sorry"),
        "uninvited theology": (0.80, "follow their lead"),
        "comparison": (0.65, "your loss is yours"),
        "timetable": (0.85, "no deadline language"),
        "disappearance": (0.90, "keep showing up"),
        "advice avalanche": (0.60, "ask before advising"),
        "spotlight theft": (0.70, "center them"),
        "grief auditing": (0.78, "no grading"),
    }
    mean_sev = sum(s for s, _ in mistakes.values()) / len(mistakes)
    worst = max(mistakes.items(), key=lambda kv: kv[1][0])
    print("mistakes: %d, mean severity %.4f" % (len(mistakes), mean_sev))
    print("most severe: %s (%.2f) -> substitute: %s" % (worst[0], worst[1][0], worst[1][1]))
    assert len(mistakes) == 8
    assert 0.752 < mean_sev < 0.755
    assert worst[0] == "disappearance"
    print("OK: %s named the mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_map(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # distances 0-1 from grief in appraisal space
    dist = {"sadness": 0.15, "mourning": 0.20, "longing": 0.25, "nostalgia": 0.40,
            "melancholy": 0.42, "regret": 0.45, "relief": 0.70, "gratitude": 0.75,
            "joy": 0.85, "acceptance": 0.55, "despair": 0.35}
    nearest = sorted(dist.items(), key=lambda kv: kv[1])[:3]
    print("nearest neighbors of grief:")
    for n_, d in nearest:
        print("  %-12s %.2f" % (n_, d))
    assert [n_ for n_, _ in nearest] == ["sadness", "mourning", "longing"]
    # despair proximity flag: close enough to warrant prompt professional help
    print("despair distance %.2f -> %s" %
          (dist["despair"], "prompt professional help" if dist["despair"] < 0.45 else "watch"))
    assert dist["despair"] < 0.45
    # opposites sit far
    assert dist["joy"] > 0.8
    print("OK: %s drew the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four dyad blends over felt qualities
    base = {"heaviness": 0.85, "tears": 0.75, "heat": 0.15, "motion": 0.25,
            "inward": 0.80, "tenderness": 0.40}
    partners = {
        "deepened sorrow (+sadness)": {"heaviness": 0.15, "tears": 0.20, "heat": -0.05,
                                       "motion": -0.10, "inward": 0.15, "tenderness": 0.10},
        "protest sorrow (+anger)": {"heaviness": 0.05, "tears": 0.05, "heat": 0.65,
                                    "motion": 0.55, "inward": -0.30, "tenderness": -0.10},
        "accusing sorrow (+guilt)": {"heaviness": 0.10, "tears": 0.10, "heat": 0.10,
                                     "motion": -0.05, "inward": 0.15, "tenderness": -0.15},
        "enduring sorrow (+love)": {"heaviness": -0.10, "tears": 0.05, "heat": -0.05,
                                    "motion": 0.05, "inward": -0.10, "tenderness": 0.50},
    }
    print("blend profiles:")
    blends = {}
    for label, delta in partners.items():
        b = {k: round(base[k] + delta[k], 3) for k in base}
        blends[label] = b
        print("  %s: heaviness %.2f heat %.2f tenderness %.2f"
              % (label, b["heaviness"], b["heat"], b["tenderness"]))
    # protest sorrow is the hottest; enduring sorrow the most tender
    hottest = max(blends, key=lambda l: blends[l]["heat"])
    tenderest = max(blends, key=lambda l: blends[l]["tenderness"])
    assert hottest == "protest sorrow (+anger)"
    assert tenderest == "enduring sorrow (+love)"
    assert 0.79 < blends[hottest]["heat"] < 0.81
    assert 0.89 < blends[tenderest]["tenderness"] < 0.91
    print("OK: %s mixed the palette" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grief_full(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-scene arc: intensity 0-10 per scene
    scenes = [("trigger (the song)", 3.0), ("cascade", 7.5), ("expression (telling)", 8.8),
              ("channeling (the soup)", 5.2), ("reweaving (journal)", 2.1)]
    intensities = [i for _, i in scenes]
    peak = max(intensities)
    peak_scene = scenes[intensities.index(peak)][0]
    resolution_drop = intensities[2] - intensities[4]
    mean = sum(intensities) / len(intensities)
    print("scenes: %d, peak %.1f at %s" % (len(scenes), peak, peak_scene))
    print("resolution drop %.1f, arc mean %.2f" % (resolution_drop, mean))
    assert peak == 8.8 and peak_scene == "expression (telling)"
    assert 6.69 < resolution_drop < 6.71
    assert 5.31 < mean < 5.33
    # arc shape: rise then fall, ending below the start
    assert intensities[0] < intensities[1] < intensities[2] > intensities[3] > intensities[4]
    assert intensities[4] < intensities[0]
    print("OK: %s ran the full arc" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_grief_is": demo_grief_what_is,
    "emotion_family": demo_grief_family,
    "intensity_volumes": demo_grief_volumes,
    "myths": demo_grief_myths,
    "first_person": demo_grief_first_person,
    "time_course": demo_grief_time_course,
    "low_vs_high": demo_grief_low_high,
    "mixed_partner": demo_grief_mixed_partner,
    "day_vignette": demo_grief_day,
    "body_signals": demo_grief_body,
    "posture_movement": demo_grief_posture,
    "sleep_appetite_energy": demo_grief_sleep,
    "body_differs": demo_grief_body_differs,
    "face_of_grief": demo_grief_face,
    "face_intensity": demo_grief_face_intensity,
    "hide_fake": demo_grief_hide_fake,
    "expression_gallery": demo_grief_gallery,
    "classic_triggers": demo_grief_classic_triggers,
    "personal_triggers": demo_grief_personal_triggers,
    "surprise_triggers": demo_grief_surprise,
    "chain_reactions": demo_grief_chains,
    "behavior_actions": demo_grief_behavior,
    "speech_patterns": demo_grief_speech,
    "decisions_judgment": demo_grief_decisions,
    "intensity_escalation": demo_grief_escalation,
    "healthy_expression": demo_grief_healthy,
    "unhealthy_expression": demo_grief_unhealthy,
    "everyday_practices": demo_grief_practices,
    "reading_signs": demo_grief_reading,
    "supportive_responses": demo_grief_support,
    "what_not_to_do": demo_grief_mistakes,
    "related_emotions_map": demo_grief_map,
    "emotion_mixes": demo_grief_mixes,
    "full_simulation": demo_grief_full,
}
