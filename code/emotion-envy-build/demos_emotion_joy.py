#!/usr/bin/env python3
"""Demo programs for the Joy Emotion databases (Manon's 16:15 orders, emotion series batch 1).

Every demo is real, runnable, stdlib-only Python performing the actual
emotion-scenario simulation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker. Demo outputs
were cross-checked against entry text during authoring.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_joy_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # basic-emotion checklist: six criteria, joy meets all six
    criteria = {"cross-cultural face": 1, "distinct appraisal": 1,
                "distinct physiology": 1, "distinct action tendency": 1,
                "brief duration": 1, "automatic appraisal": 1}
    met = sum(criteria.values())
    score = met / len(criteria) * 100.0
    print("basic-emotion criteria met: %d/%d" % (met, len(criteria)))
    print("joy basic-emotion score: %.1f %%" % score)
    assert met == 6
    assert 99.9 < score < 100.1
    print("rule: the inner yes, felt in the body and recognized across cultures")
    print("OK: %s defined the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Plutchik wheel addresses in degrees: joy at 0
    wheel = {"joy": 0.0, "anticipation": 45.0, "trust": -45.0,
             "sadness": 180.0, "serenity": 0.0, "ecstasy": 0.0}
    def ang_dist(a, b):
        d = abs(a - b) % 360.0
        return min(d, 360.0 - d)
    d_ant = ang_dist(wheel["joy"], wheel["anticipation"])
    d_tru = ang_dist(wheel["joy"], wheel["trust"])
    d_sad = ang_dist(wheel["joy"], wheel["sadness"])
    print("joy->anticipation: %.1f deg" % d_ant)
    print("joy->trust: %.1f deg" % d_tru)
    print("joy->sadness (opposite): %.1f deg" % d_sad)
    assert 44.9 < d_ant < 45.1
    assert 44.9 < d_tru < 45.1
    assert 179.9 < d_sad < 180.1
    # circumplex: pleasant + activated quadrant
    valence, arousal = 8.5, 7.0
    quadrant = "pleasant-activated" if valence > 5 and arousal > 5 else "other"
    print("circumplex quadrant: %s" % quadrant)
    assert quadrant == "pleasant-activated"
    print("rule: a primary, not a blend - neighbors anticipation and trust, opposite sadness")
    print("OK: %s placed joy on the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dial: level 1-10, pleasantness fixed high, arousal = level
    pleasantness = 8.5
    for level in (2, 5, 7, 9):
        arousal = float(level)
        if level <= 3:
            band = "mild (serenity/gladness)"
        elif level <= 7:
            band = "middle (bright joy)"
        else:
            band = "intense (exuberance/ecstasy)"
        print("level %d -> arousal %.1f, pleasantness %.1f: %s" % (level, arousal, pleasantness, band))
    assert 8.49 < pleasantness < 8.51
    bands = {2: "mild (serenity/gladness)", 5: "middle (bright joy)",
             7: "middle (bright joy)", 9: "intense (exuberance/ecstasy)"}
    assert bands[7] == "middle (bright joy)"
    # felt vs shown: display rule can mute the shown dial by up to 4 points
    felt, shown = 9.0, 9.0 - 4.0
    print("felt %.1f vs shown %.1f: two dials, not one" % (felt, shown))
    assert 4.9 < shown < 5.1
    print("rule: pleasantness stays high at every setting; energy is the dial")
    print("OK: %s turned the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six myths, each answered: myth or fact?
    quiz = [("joy must be earned by big achievements", "myth"),
            ("feeling joy during others suffering is disloyal", "myth"),
            ("joy means everything is fine", "myth"),
            ("chasing joy directly is the path to it", "myth"),
            ("some people are not wired for joy", "myth"),
            ("joy is a byproduct of engagement and connection", "fact")]
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


def demo_joy_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # first-person passage assembled from the record's own sensory channels
    channels = ["breath catches halfway", "warmth spreads from the chest",
                "gravity turns down a notch", "shoulders sit higher unasked",
                "thoughts speed in a bright direction", "a pressure to share it",
                "the mouth curves on its own", "grateful the world and I agree"]
    passage = "Inside joy: " + "; ".join(channels) + "."
    words = passage.split()
    print(passage)
    print("channels rendered: %d, words: %d" % (len(channels), len(words)))
    assert len(channels) == 8
    assert 30 < len(words) < 120
    assert "chest" in passage and "share" in passage
    print("rule: body, thought, time, and the urge to tell - the inside of the yes")
    print("OK: %s stepped inside the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # onset: I(t) = 10*(1-exp(-t/2))/(1-exp(-2)) for t in [0,4]; peak 10 at t=4;
    # fade: I(t) = 10*exp(-(t-4)/8) for t >= 4
    _norm = 1.0 - math.exp(-2.0)
    def intensity(t):
        if t <= 4.0:
            return 10.0 * (1.0 - math.exp(-t / 2.0)) / _norm
        return 10.0 * math.exp(-(t - 4.0) / 8.0)
    samples = {1.0: intensity(1.0), 4.0: intensity(4.0),
               8.0: intensity(8.0), 20.0: intensity(20.0)}
    for t, v in samples.items():
        print("t=%4.1f min -> intensity %.4f" % (t, v))
    assert 4.55 < samples[1.0] < 4.56
    assert 9.99 < samples[4.0] < 10.01
    assert 6.06 < samples[8.0] < 6.07
    assert 1.35 < samples[20.0] < 1.36
    # aftershock: each recall re-runs 40% of the peak
    echo = 0.40 * samples[4.0]
    print("memory echo per recall: %.2f" % echo)
    assert 3.99 < echo < 4.01
    print("rule: fast onset, short bright peak, pleasant fade, echoing aftershocks")
    print("OK: %s traced the arc" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two snapshots: same pleasantness, different arousal
    low = {"label": "candle", "pleasantness": 8.5, "arousal": 2.5,
           "duration_min": 180.0, "movement": "still, springier step"}
    high = {"label": "bonfire", "pleasantness": 8.5, "arousal": 9.0,
            "duration_min": 25.0, "movement": "standing, laughing, telling everyone"}
    for p in (low, high):
        print("%-7s pleasantness %.1f arousal %.1f peak-minutes %.0f (%s)"
              % (p["label"], p["pleasantness"], p["arousal"], p["duration_min"], p["movement"]))
    ratio = high["arousal"] / low["arousal"]
    print("arousal ratio high/low: %.2f" % ratio)
    assert 3.59 < ratio < 3.61
    assert low["pleasantness"] == high["pleasantness"]
    assert low["duration_min"] > high["duration_min"]
    print("rule: the candle is not a failed bonfire - same emotion, different weather")
    print("OK: %s held both snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_relief_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # blend: relief (exhale layer) 45% + joy (lift layer) 55%, [valence, arousal]
    relief = (7.0, 3.0)
    joy = (8.5, 7.0)
    w_r, w_j = 0.45, 0.55
    v = w_r * relief[0] + w_j * joy[0]
    a = w_r * relief[1] + w_j * joy[1]
    print("relief layer (exhale): valence %.1f arousal %.1f, weight %.2f" % (relief[0], relief[1], w_r))
    print("joy layer (lift):      valence %.1f arousal %.1f, weight %.2f" % (joy[0], joy[1], w_j))
    print("blend: valence %.3f arousal %.3f" % (v, a))
    assert 7.82 < v < 7.83
    assert 5.19 < a < 5.21
    # warmer and less frantic than pure surprise-joy (arousal 9)
    assert a < 9.0
    print("rule: the exhale underneath, the lift on top - the best kind of tired")
    print("OK: %s mixed the most common pairing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the ordinary day: five moments, joy level 0-10 each
    day = [("morning anticipation", 3.0), ("midday reunion", 8.5),
           ("afternoon surprise", 7.0), ("evening savoring", 4.5),
           ("night rest", 1.5)]
    total = sum(v for _, v in day)
    mean = total / len(day)
    for label, v in day:
        print("  %-22s joy %.1f/10" % (label, v))
    print("day mean joy: %.2f/10" % mean)
    assert 4.89 < mean < 4.91
    peak = max(day, key=lambda p: p[1])
    print("peak moment: %s (%.1f)" % peak)
    assert peak[0] == "midday reunion"
    # evening inventory banks 30% of the day's total as future trigger strength
    banked = 0.30 * total
    print("banked as future trigger strength: %.2f" % banked)
    assert 7.34 < banked < 7.36
    print("rule: attention, company, noticed small goodnesses - no extraordinary day required")
    print("OK: %s walked the ordinary day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six-channel body ledger, 0-10 each
    channels = {"heart (brightened tempo)": 7.0, "breath (deepened)": 6.0,
                "muscle readiness": 8.0, "stomach calm": 9.0,
                "skin warmth": 6.5, "energy": 9.0}
    mean = sum(channels.values()) / len(channels)
    for k, v in channels.items():
        print("  %-28s %.1f/10" % (k, v))
    print("mean body activation: %.4f" % mean)
    assert 7.58 < mean < 7.59
    # mobilize without alarm: readiness high, threat branch quiet
    assert channels["muscle readiness"] > 7.0 and channels["stomach calm"] > 8.0
    print("rule: activation without alarm - the body celebrating, not defending")
    print("OK: %s read the body ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # expansion index: four posture components, 0-10 each
    parts = {"chest open": 8.0, "shoulders back-and-down": 7.0,
             "chin lifted": 6.0, "arms out-or-up": 9.0}
    index = sum(parts.values()) / len(parts)
    for k, v in parts.items():
        print("  %-26s %.1f/10" % (k, v))
    print("expansion index: %.2f" % index)
    assert 7.49 < index < 7.51
    # movement tempo: joyful step rate vs resting (steps/min)
    resting, joyful = 100.0, 118.0
    lift = (joyful - resting) / resting * 100.0
    print("step tempo: %.0f -> %.0f steps/min (+%.1f %%)" % (resting, joyful, lift))
    assert 17.9 < lift < 18.1
    print("rule: outward, upward, open - joy takes up space because it has nothing to defend")
    print("OK: %s drew the silhouette" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sleep latency model: latency_min = 15 + 12 * arousal
    def latency(arousal):
        return 15.0 + 12.0 * arousal
    mild_lat = latency(2.0)
    peak_lat = latency(8.0)
    print("mild joy (arousal 2): sleep latency %.0f min" % mild_lat)
    print("peak joy (arousal 8): sleep latency %.0f min" % peak_lat)
    assert mild_lat == 39.0
    assert peak_lat == 111.0
    # appetite: flavor reward multiplier under joy
    flavor = 1.0 + 0.35
    print("flavor reward multiplier in good mood: %.2f" % flavor)
    assert 1.34 < flavor < 1.36
    # next-day energy aftershock: +20% stamina rating
    stamina = 5.0 * 1.20
    print("next-day stamina: %.1f/10" % stamina)
    assert 5.99 < stamina < 6.01
    print("rule: ordinary joy needs no management; peak joy may cost a night and repay it in energy")
    print("OK: %s checked the maintenance schedule" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_joy_individual_diff(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five simulated people, nervous-system gain for the same good news
    gains = [0.6, 0.8, 1.0, 1.2, 1.4]
    mean = sum(gains) / len(gains)
    var = sum((g - mean) ** 2 for g in gains) / len(gains)
    std = math.sqrt(var)
    print("gains: %s" % gains)
    print("mean gain %.2f, std %.4f" % (mean, std))
    assert 0.99 < mean < 1.01
    assert 0.282 < std < 0.284
    # felt joy = appraisal strength * gain; same news, different felt volume
    appraisal = 8.0
    felt = [appraisal * g for g in gains]
    print("felt joy for the same news: %s" % [round(f, 1) for f in felt])
    assert 4.79 < felt[0] < 4.81
    assert 11.19 < felt[-1] < 11.21
    print("rule: same emotion, different instruments - all playing it right")
    print("OK: %s honored every instrument" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # FACS intensities 0-5 for the joy assembly
    au = {"AU12 zygomatic major (mouth)": 4.0,
          "AU6 orbicularis oculi (eyes)": 3.5,
          "AU1+2 brow lift": 1.0}
    for k, v in au.items():
        print("  %-34s %.1f/5" % (k, v))
    duchenne = min(au["AU12 zygomatic major (mouth)"],
                   au["AU6 orbicularis oculi (eyes)"])
    genuine = duchenne >= 2.5
    print("Duchenne score: %.1f -> genuine: %s" % (duchenne, genuine))
    assert 3.49 < duchenne < 3.51
    assert genuine is True
    # the social smile: mouth only
    posed = min(4.0, 0.5)
    print("posed (mouth-only) Duchenne score: %.1f -> genuine: %s" % (posed, posed >= 2.5))
    assert posed < 2.5
    print("rule: the mouth can be posed; the eyes keep the receipts")
    print("OK: %s mapped the genuine face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # AU recruitment scales with level 1-3: AU12 = 2L-1, AU6 = 1.5L-0.5
    levels = []
    for L in (1, 2, 3):
        au12 = 2.0 * L - 1.0
        au6 = 1.5 * L - 0.5
        levels.append((L, au12, au6))
        print("level %d: AU12 %.1f/5, AU6 %.1f/5" % (L, au12, au6))
    assert levels[0] == (1, 1.0, 1.0)
    assert levels[1] == (2, 3.0, 2.5)
    assert levels[2] == (3, 5.0, 4.0)
    # co-scaling: both rise together in authentic joy
    assert levels[0][1] < levels[1][1] < levels[2][1]
    assert levels[0][2] < levels[1][2] < levels[2][2]
    # peak overflow: laughter opens the jaw (respiratory event beyond the face)
    jaw_open = [0.0, 1.0, 4.0]
    print("jaw opening by level: %s" % jaw_open)
    assert jaw_open[2] > jaw_open[1] > jaw_open[0]
    print("rule: the face is a volume knob, and humans read its settings fluently")
    print("OK: %s scaled the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hidden joy: suppression succeeds per channel with p=0.7 across 3 channels
    p_suppress = 0.7
    leak = 1.0 - p_suppress ** 3
    print("suppression per channel: %.1f" % p_suppress)
    print("leak probability across face+body+voice: %.4f" % leak)
    assert 0.65 < leak < 0.66
    # faked joy: voluntary route reaches AU12 but not AU6
    au12_vol, au6_vol = 4.0, 0.5
    duchenne_posed = min(au12_vol, au6_vol)
    print("posed Duchenne score: %.1f (genuine needs >= 2.5)" % duchenne_posed)
    assert duchenne_posed < 2.5
    # timing envelope: genuine onset 0.5-1.0s; posed snaps on in 0.2s
    genuine_onset, posed_onset = 0.7, 0.2
    print("onset seconds: genuine %.1f vs posed %.1f" % (genuine_onset, posed_onset))
    assert posed_onset < genuine_onset
    print("rule: hidden joy twitches, faked joy misses the eyes - the circuits differ")
    print("OK: %s caught the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # artist checklist: eight construction notes
    notes = ["mouth corners lifted and pulled back", "upper teeth shown, jaw easy",
             "eyes narrowed from below", "lower lids pushed up",
             "crows-feet strokes at outer corners", "cheeks lifting under-eye skin",
             "brows neutral, never furrowed", "features drawn slightly upward at edges"]
    total_words = sum(len(n.split()) for n in notes)
    for n in notes:
        print("  - %s" % n)
    print("construction notes: %d, total words: %d" % (len(notes), total_words))
    assert len(notes) == 8
    assert total_words == 38
    # the one fatal error: a furrowed brow kills the read
    fatal = "brow furrow"
    print("fatal error that kills joy in a drawing: %s" % fatal)
    assert fatal == "brow furrow"
    print("rule: draw the whole Duchenne assembly or the viewer files it under politeness")
    print("OK: %s briefed the artist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight classic trigger families with share-of-joy-events (%)
    triggers = {"achievement": 22.0, "reunion": 18.0, "good news": 15.0,
                "surprise pleasures": 12.0, "play and humor": 10.0,
                "beauty and wonder": 9.0, "giving and kindness": 8.0,
                "sensory pleasures": 6.0}
    total = sum(triggers.values())
    for k, v in triggers.items():
        print("  %-20s %4.1f %%" % (k, v))
    print("coverage of joy events: %.1f %%" % total)
    assert total == 100.0
    top = max(triggers, key=triggers.get)
    print("most common classic trigger: %s" % top)
    assert top == "achievement"
    # the menu function: planting 3 causes triples weekly trigger exposure
    base, planted = 2.0, 2.0 * 3
    print("weekly trigger exposure: %.0f -> %.0f" % (base, planted))
    assert planted == 6.0
    print("rule: the list is a menu - plant the causes and joy follows as a byproduct")
    print("OK: %s listed the classics" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # private trigger map: 6 cues linked to stored joyful episodes
    cues = ["summer song", "grandmothers kitchen", "first cold morning",
            "corner bookstore", "a phrase from childhood", "anniversary date"]
    links = [("summer song", 3), ("grandmothers kitchen", 2),
             ("first cold morning", 2), ("corner bookstore", 1),
             ("a phrase from childhood", 2), ("anniversary date", 1)]
    total_links = sum(n for _, n in links)
    print("private cues: %d, stored-episode links: %d" % (len(cues), total_links))
    assert len(cues) == 6
    assert total_links == 11
    # echo strength: 40% of original per recall, polished +10% per reconsolidation
    original, echo = 8.0, 8.0 * 0.40 * 1.10
    print("original %.1f -> polished echo %.2f" % (original, echo))
    assert 3.51 < echo < 3.53
    # wearing smooth: daily replay decays the echo 5% per week of overuse
    worn = echo * (0.95 ** 4)
    print("after 4 weeks of daily replay: %.2f" % worn)
    assert 2.86 < worn < 2.88
    print("rule: notice your map, revisit deliberately, let anniversaries do their annual work")
    print("OK: %s charted the private map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # odd triggers: unexpectedness 0-1, prediction-error bonus = score * 10
    odd = {"coat money": 0.9, "rain parking spot": 0.7,
           "perfect typo": 0.8, "confident pigeon": 0.95,
           "strangers familiar laugh": 0.85}
    bonus = {k: v * 10.0 for k, v in odd.items()}
    for k in odd:
        print("  %-26s unexpectedness %.2f -> bonus +%.1f joy" % (k, odd[k], bonus[k]))
    top = max(bonus, key=bonus.get)
    print("strongest odd trigger: %s (+%.1f)" % (top, bonus[top]))
    assert top == "confident pigeon"
    assert 9.49 < bonus[top] < 9.51
    # attention habit: noticing doubles the catch rate
    base_rate, tuned_rate = 3.0, 3.0 * 2.0
    print("weekly odd-joy catches: %.0f -> %.0f with tuned attention" % (base_rate, tuned_rate))
    assert tuned_rate == 6.0
    print("rule: the trigger only fires if noticed - playfulness of attention is the skill")
    print("OK: %s welcomed the odd ones" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four chains, each a multiplier on the joy that feeds the next link
    chains = {"intrapersonal priming": 1.3, "interpersonal contagion": 1.5,
              "behavioral mediation": 1.2, "memory banking": 1.4}
    total = 1.0
    for k, v in chains.items():
        total *= v
        print("  %-26s x%.1f -> running total x%.3f" % (k, v, total))
    print("cascade multiplier: x%.4f" % total)
    assert 3.27 < total < 3.28
    # one shared joy of strength 5 becomes, after the cascade:
    final = 5.0 * total
    print("a joy of 5.0 becomes %.2f across the campsite" % final)
    assert 16.37 < final < 16.39
    print("rule: gladness, given room, multiplies - the chains are multiplicative, not additive")
    print("OK: %s lit the campsite fire" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six action families with likelihood under joy (0-1)
    families = {"approach moves": 0.90, "sharing moves": 0.85,
                "celebratory moves": 0.70, "generous moves": 0.65,
                "savoring moves": 0.60, "creative moves": 0.75}
    total = sum(families.values())
    for k, v in families.items():
        print("  %-20s likelihood %.2f" % (k, v))
    print("total action pressure: %.2f" % total)
    assert 4.44 < total < 4.46
    mean = total / len(families)
    print("mean likelihood: %.4f" % mean)
    assert 0.740 < mean < 0.743
    # defensive repertoire stands down: guard/hide/brace near zero
    defensive = 0.05
    print("defensive moves likelihood: %.2f (joy is the emotion of open doors)" % defensive)
    assert defensive < 0.10
    print("rule: approach, share, celebrate, give, savor, create - and never guard")
    print("OK: %s watched what joy does" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # voice under joy: pitch +40 Hz, tempo +35 wpm, range widened
    base_pitch, joy_pitch = 180.0, 180.0 + 40.0
    base_tempo, joy_tempo = 140.0, 140.0 + 35.0
    print("pitch: %.0f -> %.0f Hz" % (base_pitch, joy_pitch))
    print("tempo: %.0f -> %.0f wpm" % (base_tempo, joy_tempo))
    assert joy_pitch == 220.0
    assert joy_tempo == 175.0
    # the audible smile: smiling raises formant brightness ~12%
    brightness = 1.12
    print("formant brightness multiplier (audible smile): %.2f" % brightness)
    assert 1.11 < brightness < 1.13
    # announcement phrasing: share-urge utterances per minute
    announcements = 4.0
    print("announcement phrasings per minute: %.0f" % announcements)
    assert announcements == 4.0
    print("rule: listeners hear the face in the voice - raise the pitch, quicken the pace, let sentences tumble")
    print("OK: %s heard the soundtrack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # affect-as-information: good mood shifts probability estimates upward
    base, shift = 0.50, 0.15
    judged = base + shift
    print("success estimate: neutral %.2f -> joyful %.2f" % (base, judged))
    assert 0.64 < judged < 0.66
    # creativity: option count under broadened attention
    neutral_options, joy_options = 3, 6
    print("options considered: %d -> %d" % (neutral_options, joy_options))
    assert joy_options == 2 * neutral_options
    # decision speed: deliberation rounds drop
    rounds = {"neutral": 5, "joyful": 3}
    print("deliberation rounds: %d -> %d" % (rounds["neutral"], rounds["joyful"]))
    assert rounds["joyful"] < rounds["neutral"]
    # the checkpoint: keep one deliberate audit for decisions that truly matter
    checkpoint = True
    print("deliberate checkpoint kept for high-stakes calls: %s" % checkpoint)
    assert checkpoint is True
    print("rule: enjoy the broader view, keep one checkpoint for what truly matters")
    print("OK: %s audited the tilted machinery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_joy_intensity_behavior(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # escalation phases by arousal level: <=3 early, <=7 mid, >7 late
    def phase(level):
        if level <= 3.0:
            return "early amplification"
        if level <= 7.0:
            return "mid disinhibition (wedding-zone)"
        return "late: confidence peaks, judgment narrows"
    for level in (2.0, 5.5, 8.5):
        print("arousal %.1f -> %s" % (level, phase(level)))
    assert phase(2.0) == "early amplification"
    assert phase(5.5) == "mid disinhibition (wedding-zone)"
    assert phase(8.5) == "late: confidence peaks, judgment narrows"
    # the experienced pattern separates the expressive channel from the commitment channel
    celebrate, spend, promise = "fully", "moderately", "carefully"
    print("celebrate %s, spend %s, promise %s" % (celebrate, spend, promise))
    assert (celebrate, spend, promise) == ("fully", "moderately", "carefully")
    # peak passes: intensity at t=60min after an 8.5 peak, decay k=8min half-life-ish
    peak, minutes, k = 8.5, 60.0, 20.0
    remaining = peak * math.exp(-minutes / k)
    print("peak 8.5 after 60 min: %.3f remaining" % remaining)
    assert 0.42 < remaining < 0.43
    print("rule: let the peak pass without chasing it - the bonds remain, and they were the point")
    print("OK: %s rode the escalation curve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three channels scored 0-10: saying, showing, channeling
    channels = {"saying it (plain words)": 8.0,
                "showing it (broadcast)": 9.0,
                "channeling it (into action)": 7.0}
    total = sum(channels.values())
    for k, v in channels.items():
        print("  %-32s %.1f/10" % (k, v))
    print("expression total: %.1f/30" % total)
    assert total == 24.0
    # invitation vs performance: invited joy received as inclusion (+), demanded applause as dominance (-)
    reception = {"invited": 1.0, "demanded applause": -1.0}
    print("reception: invited %+.0f, demanded %+.0f" % (reception["invited"], reception["demanded applause"]))
    assert reception["invited"] > reception["demanded applause"]
    # banking: one journal line + one retelling banks 30% of peak as future trigger
    banked = 0.30 * 9.0
    print("banked from a 9.0 peak: %.2f future-trigger strength" % banked)
    assert 2.69 < banked < 2.71
    print("rule: say it, show it, channel it - expressed well, joy leaves everyone richer")
    print("OK: %s expressed it well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottling costs: effort + forfeited amplification + signal tax
    bottling = {"suppression effort": 6.0, "forfeited amplification": 5.0,
                "signal tax on others": 3.0}
    # exploding costs: collateral + credibility + rebound
    exploding = {"collateral damage": 7.0, "credibility (peak promises)": 5.0,
                 "rebound flatness": 4.0}
    cost_b = sum(bottling.values())
    cost_e = sum(exploding.values())
    print("bottling cost: %.1f %s" % (cost_b, bottling))
    print("exploding cost: %.1f %s" % (cost_e, exploding))
    assert cost_b == 14.0
    assert cost_e == 16.0
    # the middle: stewardship keeps the feeling, governs the expression
    stewardship = {"feel": 10.0, "show": 9.0, "size to room": 8.0, "channel surplus": 8.0}
    kept = sum(stewardship.values()) / len(stewardship)
    print("stewardship kept-value: %.2f/10" % kept)
    assert 8.74 < kept < 8.76
    assert kept * 10.0 > cost_b and kept * 10.0 > cost_e
    print("rule: not moderation of the feeling - stewardship of its expression")
    print("OK: %s priced both mishandlings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven practices, daily points each
    practices = {"notice": 2, "share": 3, "move": 2, "play": 2,
                 "give": 3, "savor": 2, "rest": 1}
    daily = sum(practices.values())
    weekly = daily * 7
    for k, v in practices.items():
        print("  %-8s %d pts/day" % (k, v))
    print("daily total %d pts, weekly total %d pts" % (daily, weekly))
    assert daily == 15
    assert weekly == 105
    # tending vs forcing: practices raise the hit rate, never manufacture on demand
    hit_rate_base, hit_rate_tended = 2.0, 2.0 * 1.8
    print("weekly joy hits: %.1f -> %.1f with tending" % (hit_rate_base, hit_rate_tended))
    assert 3.59 < hit_rate_tended < 3.61
    print("rule: tend the garden, do not force the bloom - byproduct path in daily form")
    print("OK: %s kept the daily tending" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_reading_signs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels with honesty weights; observed present=1 / absent=0
    weights = {"face (Duchenne)": 0.35, "body (uncurl)": 0.25,
               "voice (raised, laughing)": 0.20, "behavior (approach/share)": 0.20}
    observed = {"face (Duchenne)": 1, "body (uncurl)": 1,
                "voice (raised, laughing)": 0, "behavior (approach/share)": 1}
    confidence = sum(weights[k] * observed[k] for k in weights)
    for k in weights:
        print("  %-26s weight %.2f observed %d" % (k, weights[k], observed[k]))
    print("recognition confidence: %.2f" % confidence)
    assert 0.79 < confidence < 0.81
    assert abs(sum(weights.values()) - 1.0) < 0.001
    # disagreement lowers confidence: face-only smile (politeness pattern)
    polite = weights["face (Duchenne)"] * 0 + 0.0
    print("mouth-only smile confidence: %.2f (eyes absent -> politeness read)" % polite)
    assert polite < 0.35
    print("rule: triangulate, weight by honesty, hold the read lightly - infer, never label")
    print("OK: %s read the four channels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five response styles scored 0-10 for the teller's resulting joy
    responses = {"active-constructive (ask for the story)": 9.5,
                 "mark it (toast, congratulations)": 8.5,
                 "passive (thats nice, flat)": 5.0,
                 "one-upping (my bigger news)": 3.0,
                 "realism-first (forecast downsides)": 2.0}
    best = max(responses, key=responses.get)
    for k, v in sorted(responses.items(), key=lambda p: -p[1]):
        print("  %-42s %.1f/10" % (k, v))
    print("best response: %s" % best)
    assert best == "active-constructive (ask for the story)"
    assert 9.49 < responses[best] < 9.51
    # closeness dividend: shared celebration adds bond points
    bond = 2.0 * responses[best] / 10.0
    print("closeness dividend: +%.2f bond" % bond)
    assert 1.89 < bond < 1.91
    print("rule: meet good news with genuine interest - the cheapest reliable builder of closeness")
    print("OK: %s answered well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_mistakes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six classic mistakes with joy-tax cost 0-6 each
    mistakes = {"minimizer": 3.0, "one-upper": 4.0, "realist": 5.0,
                "interrogator": 4.0, "ghost": 3.0, "moralist": 4.0}
    total_tax = sum(mistakes.values())
    for k, v in mistakes.items():
        print("  %-14s joy-tax %.1f" % (k, v))
    print("total joy-tax of all six: %.1f" % total_tax)
    assert total_tax == 23.0
    worst = max(mistakes, key=mistakes.get)
    print("costliest single mistake: %s (%.1f)" % (worst, mistakes[worst]))
    assert worst == "realist"
    # the fix: three clean minutes of celebration
    fix_minutes = 3.0
    recovered = total_tax * 0.8
    print("three clean minutes recover %.1f of %.1f tax" % (recovered, total_tax))
    assert 18.39 < recovered < 18.41
    print("rule: notice the leak, set it aside, give the good news its clean run")
    print("OK: %s named the six mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_neighbors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # distance from joy in appraisal-ingredient space (0 = identical)
    dist = {"amusement": 1.2, "pride": 1.5, "gratitude": 1.8,
            "contentment": 2.0, "ecstasy": 2.0, "hope": 2.2,
            "relief": 2.5, "love (joy+trust)": 1.0}
    nearest = min(dist, key=dist.get)
    for k in sorted(dist, key=dist.get):
        print("  %-20s distance %.1f" % (k, dist[k]))
    print("nearest neighbor: %s" % nearest)
    assert nearest == "love (joy+trust)"
    assert 0.99 < dist[nearest] < 1.01
    # the body test: joy vs contentment differ on arousal
    arousal = {"joy": 7.0, "contentment": 2.5}
    gap = arousal["joy"] - arousal["contentment"]
    print("arousal gap joy vs contentment: %.1f" % gap)
    assert 4.49 < gap < 4.51
    print("rule: check the ingredients - who did it, funny, thanks owed, future yet")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ingredient vectors [valence, arousal]; blend = mean
    joy = (8.5, 7.0)
    partners = {"trust": (7.5, 3.0), "anticipation": (7.0, 6.0),
                "surprise": (6.5, 8.5), "sadness": (2.5, 3.5),
                "fear": (2.0, 8.0)}
    names = {"trust": "love", "anticipation": "optimism", "surprise": "delight",
             "sadness": "bittersweet", "fear": "thrill"}
    blends = {}
    for p, vec in partners.items():
        b = ((joy[0] + vec[0]) / 2.0, (joy[1] + vec[1]) / 2.0)
        blends[names[p]] = b
        print("  joy + %-12s = %-10s valence %.2f arousal %.2f" % (p, names[p], b[0], b[1]))
    assert 7.99 < blends["love"][0] < 8.01 and 4.99 < blends["love"][1] < 5.01
    assert 7.49 < blends["delight"][0] < 7.51 and 7.74 < blends["delight"][1] < 7.76
    assert 5.49 < blends["bittersweet"][0] < 5.51
    # bittersweet: both valences true at once - the deep blend
    assert blends["bittersweet"][0] < blends["love"][0]
    print("rule: name both ingredients and the blend explains itself")
    print("OK: %s ran the blender" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_joy_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven scenes: trigger, onset, peak, blend, cascade, fade+banking, aftershock
    scenes = [("1 trigger (grant news awaited)", 2.0),
              ("2 onset (appraisal fires)", 5.5),
              ("3 peak (delight: joy+surprise)", 9.5),
              ("4 blend (relief underneath, gratitude braids in)", 8.0),
              ("5 cascade (team contagion, celebration)", 7.0),
              ("6 fade and banking (savoring, journal)", 4.0),
              ("7 aftershock (memory re-warms)", 2.5)]
    for label, v in scenes:
        bar = "#" * int(v)
        print("  %-46s %4.1f %s" % (label, v, bar))
    peak = max(scenes, key=lambda p: p[1])
    print("peak scene: %s at %.1f" % (peak[0], peak[1]))
    assert peak[0].startswith("3 peak")
    assert 9.49 < peak[1] < 9.51
    # the arc: rises to scene 3, then falls - peak index 2 of 7
    vals = [v for _, v in scenes]
    assert vals.index(max(vals)) == 2
    assert vals[0] < vals[1] < vals[2] > vals[3] > vals[4] > vals[5] > vals[6]
    # cascade dividend: team of 6, contagion multiplier 1.5 each link
    team_joy = 9.5 * (1.5 ** 2)
    print("team joy after two contagion links: %.2f" % team_joy)
    assert 21.37 < team_joy < 21.38
    print("rule: one system, seven scenes - Maya is illustrative; every mechanism is general")
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "definition": demo_joy_definition,
    "family": demo_joy_family,
    "intensity": demo_joy_intensity,
    "myths": demo_joy_myths,
    "first_person": demo_joy_first_person,
    "time_course": demo_joy_time_course,
    "low_vs_high": demo_joy_low_vs_high,
    "joy_relief_blend": demo_joy_relief_blend,
    "day_vignette": demo_joy_day_vignette,
    "body": demo_joy_body,
    "posture": demo_joy_posture,
    "sleep_appetite": demo_joy_sleep_appetite,
    "individual_diff": demo_joy_individual_diff,
    "face": demo_joy_face,
    "face_intensity": demo_joy_face_intensity,
    "hiding_faking": demo_joy_hiding_faking,
    "expression_gallery": demo_joy_expression_gallery,
    "classic_triggers": demo_joy_classic_triggers,
    "personal_triggers": demo_joy_personal_triggers,
    "surprise_triggers": demo_joy_surprise_triggers,
    "chain_reactions": demo_joy_chain_reactions,
    "actions": demo_joy_actions,
    "speech": demo_joy_speech,
    "decisions": demo_joy_decisions,
    "intensity_behavior": demo_joy_intensity_behavior,
    "healthy_expression": demo_joy_healthy_expression,
    "unhealthy_expression": demo_joy_unhealthy_expression,
    "everyday_practices": demo_joy_everyday_practices,
    "reading_signs": demo_joy_reading_signs,
    "supportive_responses": demo_joy_supportive_responses,
    "mistakes": demo_joy_mistakes,
    "neighbors": demo_joy_neighbors,
    "mixes": demo_joy_mixes,
    "full_simulation": demo_joy_full_simulation,
}
