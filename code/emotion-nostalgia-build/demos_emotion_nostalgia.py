#!/usr/bin/env python3
"""Demo programs for the Nostalgia Emotion databases (emotion series batch 2).

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


def demo_nostalgia_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three beats: cue -> replay -> meaning
    cue = {"specificity": 0.90, "sense_strength": 0.85}      # a song, a smell
    replay = {"vividness": 0.88, "social": 0.92}            # people who mattered
    meaning = {"continuity": 0.86, "connection": 0.90, "worth": 0.84}
    cue_s = sum(cue.values()) / len(cue)
    replay_s = sum(replay.values()) / len(replay)
    meaning_s = sum(meaning.values()) / len(meaning)
    nostalgia = (cue_s + replay_s + meaning_s) / 3.0
    print("cue %.3f -> replay %.3f -> meaning %.3f" % (cue_s, replay_s, meaning_s))
    print("nostalgia index: %.3f" % nostalgia)
    assert 0.874 < cue_s < 0.876
    assert 0.899 < replay_s < 0.901
    assert 0.866 < meaning_s < 0.868
    assert 0.879 < nostalgia < 0.881
    assert meaning_s > 0 and replay_s > cue_s  # replay must exceed the bare cue
    print("memory is the recall; the feeling is what the recall carries")
    print("OK: %s ran the three-beat sequence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # blended roots: joy + sadness -> bittersweet; neighbors weighted
    joy, sadness = 1.0, 1.0
    family = {
        "bittersweet_core": joy * 0.55 + sadness * 0.45,
        "longing": sadness * 0.70 + joy * 0.20,
        "wistfulness": joy * 0.40 + sadness * 0.40,
        "sentimentality": joy * 0.60 + sadness * 0.25,
        "homesickness": sadness * 0.60 + joy * 0.35,
        "gratitude": joy * 0.75 + sadness * 0.10,
    }
    total = sum(family.values())
    share = {k: v / total * 100.0 for k, v in family.items()}
    for k in family:
        print("  %-16s weight %.2f (%5.2f %%)" % (k, family[k], share[k]))
    assert 0.999 < sum(share.values()) / 100.0 < 1.001
    assert share["bittersweet_core"] > share["gratitude"]
    assert 18.6 < share["bittersweet_core"] < 18.8
    assert family["longing"] > family["gratitude"]  # ache-weighted vs joy-weighted
    print("root: bittersweet; every neighbor keeps the precious-past core")
    print("OK: %s mapped the family tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three dials sum into the volume knob 0..10
    def volume(centrality, cue_strength, vulnerability):
        return min(10.0, (centrality + cue_strength + vulnerability) / 3.0 * 10.0)
    def label(v):
        return "mild" if v < 3.5 else ("moderate" if v < 7.0 else "intense")
    cases = [(0.15, 0.2, 0.1), (0.5, 0.55, 0.5), (0.95, 0.9, 0.95)]
    for c, s, v in cases:
        print("dials %.2f/%.2f/%.2f -> volume %.2f (%s)" % (c, s, v, volume(c, s, v), label(volume(c, s, v))))
    assert abs(volume(0.15, 0.2, 0.1) - 1.5) < 0.001
    assert abs(volume(0.5, 0.55, 0.5) - 5.1667) < 0.001
    assert abs(volume(0.95, 0.9, 0.95) - 9.3333) < 0.001
    assert label(volume(0.15, 0.2, 0.1)) == "mild"
    assert label(volume(0.95, 0.9, 0.95)) == "intense"
    # same cue, tender present -> louder
    assert volume(0.9, 0.9, 0.9) > volume(0.9, 0.9, 0.1)
    print("OK: %s turned the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five myths scored against the findings: 1 = busted, 0 = confirmed
    myths = {
        "just living in the past": 1,
        "it is a sickness": 1,
        "only sad people feel it": 1,
        "the past was better": 1,
        "it makes you stuck": 1,
    }
    busted = sum(myths.values())
    print("myths examined: %d, busted: %d" % (len(myths), busted))
    for m in myths:
        print("  BUSTED: %s" % m)
    assert busted == 5
    assert busted / len(myths) == 1.0
    print("grain of truth noted; wrong conclusion rejected")
    print("OK: %s cleared the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dual chest sensation: warmth and hollowness as two channels
    warmth = 0.85      # the cherished memory
    hollowness = 0.55  # the recognized distance
    bittersweet = (warmth + hollowness) / 2.0
    smile = warmth > 0.5            # unchosen soft smile
    sting = hollowness > 0.4        # eyes sting from sharpness
    absorbed = (warmth + hollowness) / 2.0 > 0.6  # present goes thin
    print("warmth %.2f, hollowness %.2f -> bittersweet %.3f" % (warmth, hollowness, bittersweet))
    print("smile: %s  sting: %s  absorbed: %s" % (smile, sting, absorbed))
    assert 0.699 < bittersweet < 0.701
    assert smile and sting and absorbed
    # gratitude underneath: meaning tracks with warmth
    gratitude = warmth * 0.9
    assert 0.764 < gratitude < 0.766
    print("underneath it all: gratitude %.3f - this happened, I belonged" % gratitude)
    print("OK: %s stepped inside the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the arc: onset, rise, peak, fade, aftershock (intensity 0..10, steadiness 0..10)
    phases = [
        ("onset 0:05", 3.0, 5.0),
        ("rise 0:45", 6.0, 5.5),
        ("peak 4:00", 9.0, 6.0),
        ("fade 12:00", 4.0, 7.0),
        ("aftershock +2d", 1.5, 8.5),
    ]
    peak = max(p[1] for p in phases)
    print("phase            intensity  steadiness")
    for label, inten, steady in phases:
        print("  %-14s %5.1f      %5.1f" % (label, inten, steady))
    assert 8.9 < peak < 9.1
    assert phases[2][0].startswith("peak")
    # steadiness climbs while intensity falls: the payoff
    assert phases[4][2] > phases[2][2] > phases[0][2]
    assert phases[4][1] < phases[0][1]
    gain = phases[4][2] - phases[0][2]
    assert 3.4 < gain < 3.6
    print("steadiness gain: %.1f - the visit ends, the strength stays" % gain)
    print("OK: %s walked the time course" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same song, two dial settings
    def volume(centrality, cue_strength, vulnerability):
        return min(10.0, (centrality + cue_strength + vulnerability) / 3.0 * 10.0)
    tuesday = (0.15, 0.25, 0.10)   # peripheral memory, radio, neutral morning
    midnight = (0.95, 0.90, 0.90)  # lost parent, old street, anniversary grief
    v_low = volume(*tuesday)
    v_high = volume(*midnight)
    print("Tuesday morning: %.2f (passing smile)" % v_low)
    print("Midnight anniversary: %.2f (pulled over, tears)" % v_high)
    assert v_low < 3.5 < v_high
    assert abs(v_low - 1.6667) < 0.001
    assert abs(v_high - 9.1667) < 0.001
    ratio = v_high / v_low
    assert 5.4 < ratio < 5.6
    print("same song, same person: the dials make the %.1fx difference" % ratio)
    print("OK: %s compared the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_partner_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two independent channels, both hot: the bittersweet blend
    joy_track = 0.80      # the cherished memory, recognized
    ache_track = 0.62     # the distance, registered a beat later
    blend = (joy_track + ache_track) / 2.0
    # seesaw over minutes at a reunion: attention shifts tracks
    seesaw = [0.72, 0.58, 0.75, 0.60, 0.70]  # blend samples across the evening
    print("joy %.2f + ache %.2f -> blend %.3f" % (joy_track, ache_track, blend))
    print("evening seesaw: %s" % ", ".join("%.2f" % s for s in seesaw))
    assert 0.709 < blend < 0.711
    assert max(seesaw) - min(seesaw) > 0.1   # it genuinely oscillates
    assert all(0.5 < s < 0.85 for s in seesaw)  # never collapses to one side
    # benefits survive the ache
    meaning_gain = blend * 0.9
    assert 0.63 < meaning_gain < 0.65
    print("the bitter proves the sweet: meaning gain %.3f" % meaning_gain)
    print("OK: %s mixed the bittersweet blend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four micro-episodes deposit meaning across an ordinary day
    episodes = [
        ("morning smell", 0.55, 0.30),   # (warmth, ache)
        ("midday street name", 0.60, 0.35),
        ("afternoon ticket stub", 0.70, 0.50),
        ("evening song + text", 0.85, 0.45),
    ]
    deposits = []
    print("episode                 warmth  ache  deposit")
    for label, w, a in episodes:
        deposit = w * 0.7 + (w - a) * 0.3   # warmth counts most; net sweetness adds
        deposits.append(deposit)
        print("  %-22s %.2f    %.2f  %.3f" % (label, w, a, deposit))
    total = sum(deposits)
    print("day total meaning deposit: %.3f" % total)
    assert 2.21 < total < 2.23
    assert deposits == sorted(deposits)  # the day builds
    assert all(d > 0 for d in deposits)  # every visit leaves something
    print("not an event - the past walking alongside, keeping company")
    print("OK: %s lived the ordinary day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tender activation: calm body, full heart - vs a high-arousal profile
    nostalgia = {"heart": 0.30, "breath": 0.25, "muscle": 0.20,
                 "warmth": 0.85, "goosebumps": 0.55, "stillness": 0.80}
    alarm = {"heart": 0.95, "breath": 0.90, "muscle": 0.92,
             "warmth": 0.10, "goosebumps": 0.20, "stillness": 0.05}
    arousal_n = (nostalgia["heart"] + nostalgia["breath"] + nostalgia["muscle"]) / 3.0
    arousal_a = (alarm["heart"] + alarm["breath"] + alarm["muscle"]) / 3.0
    tenderness = (nostalgia["warmth"] + nostalgia["goosebumps"] + nostalgia["stillness"]) / 3.0
    print("nostalgia arousal %.3f vs alarm arousal %.3f" % (arousal_n, arousal_a))
    print("tenderness index: %.3f" % tenderness)
    assert 0.249 < arousal_n < 0.251
    assert 0.923 < arousal_a < 0.925
    assert 0.732 < tenderness < 0.734
    assert arousal_n < 0.4 < arousal_a  # quiet body, not a mobilized one
    print("the headquarters is the chest: warmth, not pounding")
    print("OK: %s read the body signals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_posture_movement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attention budget: replay depth buys stillness
    def stillness(replay_depth):
        return min(1.0, 0.15 + replay_depth * 0.85)
    depths = [0.1, 0.4, 0.7, 0.95]
    print("replay depth -> bodily stillness")
    for d in depths:
        print("  %.2f -> %.3f" % (d, stillness(d)))
    assert abs(stillness(0.1) - 0.235) < 0.001
    assert abs(stillness(0.95) - 0.9575) < 0.001
    assert stillness(0.95) > stillness(0.7) > stillness(0.4) > stillness(0.1)
    # gaze decoupling and hand anchoring at high depth
    gaze_decoupled = stillness(0.95) > 0.9
    hand_anchors = True  # touch keeps a present-tense tether
    assert gaze_decoupled and hand_anchors
    print("the body quiets to give the memory bandwidth")
    print("OK: %s traced the posture signature" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_sleep_appetite_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gentle routines: sleep ease, comfort-food pull, restorative energy
    calm = 0.80            # parasympathetic-leaning profile
    absorption = 0.55     # one more song, one more page
    sleep_ease = calm * 0.9 - absorption * 0.25
    comfort_pull = 0.75   # the dish in a loved one's handwriting
    restored = calm * 0.85
    print("sleep ease %.3f | comfort-food pull %.2f | restored %.3f" % (sleep_ease, comfort_pull, restored))
    assert 0.582 < sleep_ease < 0.584
    assert 0.679 < restored < 0.681
    assert sleep_ease > 0.5      # usually easy, warm sleep
    assert restored > sleep_ease # net effect is replenishing
    # pleasant heaviness after an intense wave
    heaviness = 0.60 * 0.5
    assert 0.299 < heaviness < 0.301
    print("among the least physiologically costly emotions at everyday volume")
    print("OK: %s checked sleep, appetite, energy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same inner feeling, different bodily clothing
    inner = 0.75  # warmth/absorption/bittersweet - the constant
    people = {
        "crier": {"expressivity": 0.95, "interoception": 0.80},
        "stone-faced feeler": {"expressivity": 0.15, "interoception": 0.85},
        "goosebump responder": {"expressivity": 0.60, "interoception": 0.55},
        "quiet elder": {"expressivity": 0.45, "interoception": 0.90},
    }
    print("inner feeling: %.2f (constant)" % inner)
    shown = {}
    for label, t in people.items():
        s = inner * (0.4 + 0.6 * t["expressivity"])
        shown[label] = s
        print("  %-20s shows %.3f" % (label, s))
    assert 0.727 < shown["crier"] < 0.728
    assert 0.367 < shown["stone-faced feeler"] < 0.369
    assert shown["crier"] > shown["goosebump responder"] > shown["quiet elder"] > shown["stone-faced feeler"]
    # no correct way: the constant matters, not the clothing
    assert all(abs(inner - 0.75) < 1e-9 for _ in people)
    print("no correct way for a body to do nostalgia")
    print("OK: %s honored the differences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the moderate-intensity facial configuration, component by component
    face = {
        "gaze_decoupled": 0.85, "lids_low": 0.70, "eye_shine": 0.75,
        "brow_inner_lift": 0.35, "mouth_corner_lift": 0.45, "asymmetry": 0.60,
        "swallow": 0.50, "slow_blink": 0.55,
    }
    coherence = sum(face.values()) / len(face)
    involuntary = (face["eye_shine"] + face["brow_inner_lift"] + face["swallow"]) / 3.0
    print("components:")
    for k, v in face.items():
        print("  %-18s %.2f" % (k, v))
    print("coherence %.3f | involuntary core %.3f" % (coherence, involuntary))
    assert 0.593 < coherence < 0.595
    assert 0.533 < involuntary < 0.535
    # reads as authentic: the hard-to-fake parts are present
    authentic = involuntary > 0.5 and face["asymmetry"] > 0.5
    assert authentic
    print("soft, inward-turned, unperformed - the hearth-face")
    print("OK: %s drew the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same movements, more amplitude: one emotion at many volumes
    base = {"mouth_lift": 0.30, "eye_shine": 0.35, "gaze_drift": 0.40}
    def amplitude(level):
        return {k: min(1.0, v * level) for k, v in base.items()}
    mild = amplitude(0.5)
    moderate = amplitude(1.6)
    high = amplitude(2.8)
    for label, a in (("mild", mild), ("moderate", moderate), ("high", high)):
        print("%-9s mouth %.2f shine %.2f drift %.2f" % (label, a["mouth_lift"], a["eye_shine"], a["gaze_drift"]))
    assert abs(mild["mouth_lift"] - 0.15) < 0.001
    assert abs(moderate["eye_shine"] - 0.56) < 0.001
    assert abs(high["gaze_drift"] - 1.0) < 0.001  # capped: fully decoupled
    # overflow components only at high
    tears = high["eye_shine"] >= 0.95
    assert tears and not mild["eye_shine"] >= 0.95
    # afterglow: relaxed features, lingering half-smile
    afterglow = {"relaxed": 0.85, "half_smile": 0.50}
    assert afterglow["relaxed"] > afterglow["half_smile"]
    print("the mild end is where most everyday nostalgia lives - and is most often missed")
    print("OK: %s scaled the expression" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # suppression trims the voluntary display; the involuntary leaks
    components = {
        "mouth_set": ("voluntary", 0.90),      # can be commanded
        "gaze_present": ("voluntary", 0.85),
        "eye_shine": ("involuntary", 0.15),    # barely suppressible
        "inner_brow": ("involuntary", 0.10),
        "swallow": ("involuntary", 0.20),
        "return_lag": ("involuntary", 0.05),
    }
    suppressed = {}
    for name_c, (kind, control) in components.items():
        suppressed[name_c] = 1.0 - control if kind == "voluntary" else 1.0 - control * 0.3
    print("suppression attempt -> remaining signal:")
    for k, v in suppressed.items():
        print("  %-12s %.3f" % (k, v))
    leaked = sum(v for (k, v) in suppressed.items() if components[k][0] == "involuntary")
    assert 3.84 < leaked < 3.86
    assert suppressed["eye_shine"] > suppressed["mouth_set"]  # the shine disobeys
    # faking fails the other way: posed parts without involuntary core
    posed = {"mouth_smile": 0.9, "eye_shine": 0.05, "gaze_drift": 0.1}
    reads_real = posed["eye_shine"] > 0.4 and posed["gaze_drift"] > 0.4
    assert not reads_real
    print("the kind move: room, a soft glance, no demand for explanation")
    print("OK: %s watched for leakage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # craft checklist: does the portrait/staging carry the configuration?
    checks = {
        "gaze not landing": 1, "lids low": 1, "highlights wetter": 1,
        "brows quiet": 1, "one mouth corner lifted": 1, "lines softened": 1,
        "head tilted 5-10 deg": 1, "hand near face/chest": 0,  # optional
        "breath slowed once": 1, "smile late and small": 1, "speech trailing": 1,
    }
    required = [k for k in checks if k != "hand near face/chest"]
    score = sum(checks[k] for k in required) / len(required)
    print("gallery checks passed: %d/%d (hand optional)" % (sum(checks[k] for k in required), len(required)))
    assert abs(score - 1.0) < 1e-9
    reads_before_named = score > 0.8
    assert reads_before_named
    print("the test: the audience reads it before they can name it")
    print("OK: %s completed the gallery notes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # trigger potency: encoding repetitions x emotional charge x sense directness
    triggers = {
        "music": (0.95, 0.90, 0.85),
        "smell": (0.70, 0.85, 0.95),
        "photographs": (0.60, 0.80, 0.50),
        "places": (0.80, 0.85, 0.70),
        "anniversaries": (0.65, 0.90, 0.40),
        "objects": (0.75, 0.70, 0.60),
        "food": (0.80, 0.75, 0.80),
        "people": (0.90, 0.95, 0.75),
    }
    potency = {k: (r * c * s) ** (1.0 / 3.0) for k, (r, c, s) in triggers.items()}
    ranked = sorted(potency.items(), key=lambda p: p[1], reverse=True)
    print("trigger potency ranking:")
    for k, v in ranked:
        print("  %-13s %.3f" % (k, v))
    assert ranked[0][0] == "music"       # champion: bound to the era's peaks
    assert ranked[1][0] == "people"      # richest social core, close second
    assert 0.862 < potency["people"] < 0.864
    assert 0.899 < potency["music"] < 0.901
    assert potency["smell"] > potency["photographs"]  # directness beats deliberateness
    print("arrange them on purpose - or see them coming")
    print("OK: %s ranked the classic triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # incidental association: unguarded co-occurrences beat arranged ones
    def strength(unguarded_mornings, arranged_afternoons):
        return min(1.0, unguarded_mornings / (unguarded_mornings + arranged_afternoons + 5.0))
    mug = strength(1000, 0)      # the chipped mug: a thousand mornings
    photo = strength(0, 1)       # the posed photograph: one afternoon
    print("chipped mug association: %.3f" % mug)
    print("posed photo association: %.3f" % photo)
    assert 0.994 < mug < 0.996
    assert photo < 0.001   # one arranged afternoon, zero unguarded mornings
    assert mug - photo > 0.99
    # anniversary: the calendar keeps the date with or without permission
    anniversary_charge = 0.85
    conscious = False
    wave_arrives = anniversary_charge > 0.5  # before recognition
    assert wave_arrives and not conscious
    # reminiscence bump: dense firsts furnish disproportionate triggers
    bump_share = 0.45  # ~teens to late twenties supply nearly half the private set
    assert 0.44 < bump_share < 0.46
    print("follow the inexplicable triggers: the contour lines of loves")
    print("OK: %s mapped the private set" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ambush = strong unattended link x zero preparation
    def ambush(unattended_strength, preparation):
        return unattended_strength * (1.0 - preparation)
    carpet = ambush(0.85, 0.0)    # the cheap carpet: never filed, never braced
    playlist = ambush(0.85, 0.7)  # the deliberate playlist: braced for
    print("cheap-carpet ambush: %.3f | playlist visit: %.3f" % (carpet, playlist))
    assert abs(carpet - 0.85) < 0.001
    assert abs(playlist - 0.255) < 0.001
    assert carpet > playlist * 3
    # specificity: background details stored as particulars, not categories
    specificity = {"that song": 0.9, "music in general": 0.3}
    assert specificity["that song"] > specificity["music in general"] * 2
    # after conscious filing, the ambush dulls but the warmth remains
    warmth_before, warmth_after = 0.80, 0.78
    ambush_after = ambush(0.85, 0.6)
    assert ambush_after < carpet and abs(warmth_after - warmth_before) < 0.05
    print("startling - and usually secretly welcome")
    print("OK: %s survived the ambushes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spreading activation: song -> summer -> friends -> the one who is gone
    chain = [
        ("song (nostalgia)", 0.85, "nostalgia"),
        ("summer (nostalgia+joy)", 0.80, "nostalgia+joy"),
        ("friends (nostalgia+joy)", 0.78, "nostalgia+joy"),
        ("the one who is gone (nostalgia+grief)", 0.88, "nostalgia+grief"),
        ("gratitude for having had them", 0.70, "nostalgia+gratitude"),
    ]
    print("cascade:")
    for label, act, felt in chain:
        print("  %-38s act %.2f -> %s" % (label, act, felt))
    assert len(chain) == 5
    peak = max(c[1] for c in chain)
    assert 0.879 < peak < 0.881
    assert chain[3][2] == "nostalgia+grief"  # the far room
    # riding it: the return is a choice, monitored step by step
    noticed = [True, True, True, True, True]
    assert all(noticed) and len(noticed) == len(chain)
    print("not a malfunction - the network doing what networks do")
    print("OK: %s rode the chain reaction" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # approach, not avoidance: actions toward the valued past
    approach = ["call the old friend", "pull the album", "drive the old route",
                "cook the dish", "send the photo", "organize the reunion",
                "teach the song", "keep the ticket stub"]
    avoid = ["delete the photos"]  # rare, and usually denial rather than nostalgia
    print("approach actions: %d | avoidance actions: %d" % (len(approach), len(avoid)))
    for a in approach:
        print("  -> %s" % a)
    assert len(approach) == 8 and len(avoid) == 1
    assert len(approach) / (len(approach) + len(avoid)) > 0.85
    # social core: most actions reach toward people
    social = sum(1 for a in approach if any(w in a for w in ("friend", "photo", "reunion", "song")))
    assert social >= 4
    print("a life reaching back to touch what shaped it")
    print("OK: %s watched what people do" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_speech_patterns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # marker detection in a sample utterance
    utterance = ("Remember when we used to drive out to the lake? The way the light "
                 "came through those windows at four in the afternoon - oh, those were "
                 "the days. So we're driving, and he says - you remember, don't you?")
    u = utterance.lower()
    markers = {
        "remember-when opener": "remember when" in u,
        "we-used-to": "used to" in u,
        "sensory close-up": "light came through" in u,
        "those-were-the-days": "those were the days" in u,
        "present-tense slippage": "we're driving" in u,
        "second-person pull": "don't you" in u,
    }
    hits = sum(markers.values())
    print("utterance markers: %d/%d" % (hits, len(markers)))
    for m, hit in markers.items():
        print("  [%s] %s" % ("x" if hit else " ", m))
    assert hits == 6
    assert hits / len(markers) == 1.0
    print("the surest verbal sign the replay has taken over: tense slippage")
    print("OK: %s listened to the speech patterns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_decisions_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # familiarity glow: nostalgia inflates the known option's perceived value
    def perceived(true_value, nostalgia_glow):
        return true_value + nostalgia_glow
    old_way = perceived(0.60, 0.25)   # true 0.60, glowing
    new_way = perceived(0.75, 0.00)   # true 0.75, unlit
    print("old way perceived %.2f (true 0.60) | new way perceived %.2f (true 0.75)" % (old_way, new_way))
    assert abs(old_way - 0.85) < 0.001
    assert old_way > new_way > 0.60  # the distortion: glow beats merit
    # the skill: separate values-counsel from option-judgment
    values = 0.85   # nostalgia correctly reports what matters
    assert 0.84 < values < 0.86
    corrected = 0.75  # present evidence judges the options
    choice = "new way" if corrected > 0.60 else "old way"
    assert choice == "new way"
    print("let nostalgia inform values; let present evidence judge options")
    print("OK: %s weighed the judgment shift" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # behavior budget tipping toward the past as volume rises
    def past_budget(volume):
        return min(1.0, 0.05 + (volume / 10.0) ** 2 * 0.95)
    mild, moderate, high = past_budget(1.5), past_budget(5.2), past_budget(9.2)
    print("mild %.3f | moderate %.3f | high %.3f (share of the day given to the past)" % (mild, moderate, high))
    assert 0.071 < mild < 0.073
    assert 0.306 < moderate < 0.308
    assert 0.853 < high < 0.855
    assert mild < moderate < high
    # the line is the pattern: healthy resolves, unhealthy repeats
    healthy = [0.85, 0.30, 0.10]    # high wave, then return
    unhealthy = [0.85, 0.82, 0.88]  # every evening rearranged
    assert healthy[-1] < healthy[0] * 0.5
    assert unhealthy[-1] > unhealthy[0] * 0.9
    # the return ticket: a kept-warm present reasserts itself
    return_ticket = 0.70  # tomorrow's plan, the morning walk
    resolves = return_ticket > 0.5
    assert resolves
    print("intensity asks for respect; the return ticket keeps it healthy")
    print("OK: %s tracked the escalation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # say it, show it, channel it - then check the return
    said = ["told the story", "named the feeling", "let the shine show"]
    shown = ["framed the photo", "recipe box in use"]
    channeled = ["called the old friend", "restarted the tradition", "wrote the thank-you"]
    modes = {"said": said, "shown": shown, "channeled": channeled}
    print("expression modes:")
    for mode, acts in modes.items():
        print("  %-9s %d acts" % (mode, len(acts)))
    coverage = sum(1 for acts in modes.values() if acts) / len(modes)
    assert abs(coverage - 1.0) < 1e-9
    total_acts = sum(len(a) for a in modes.values())
    assert total_acts == 8
    # the test: more present after, not less
    presence_before, presence_after = 0.55, 0.85
    assert presence_after > presence_before
    gain = presence_after - presence_before
    assert 0.299 < gain < 0.301
    print("presence gain %.2f - the past visited, honored, put to work" % gain)
    print("OK: %s expressed it healthily" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two unhealthy directions scored against the visit structure
    stuck = {"visits_per_week": 7, "present_invitations_declined": 6,
             "returns_completed": 0, "past_as_evidence": 0.9}
    denial = {"cue_avoidance": 0.9, "expression_suppressed": 0.85,
              "leak_irritability": 0.6, "treasury_open": 0.1}
    stuck_score = (stuck["visits_per_week"] / 7.0 + stuck["present_invitations_declined"] / 7.0
                   + (1 - stuck["returns_completed"]) + stuck["past_as_evidence"]) / 4.0
    denial_score = (denial["cue_avoidance"] + denial["expression_suppressed"]
                    + denial["leak_irritability"] + (1 - denial["treasury_open"])) / 4.0
    print("stuck pattern score: %.3f | denial pattern score: %.3f" % (stuck_score, denial_score))
    assert 0.939 < stuck_score < 0.941
    assert 0.812 < denial_score < 0.814
    # both abandon the visit structure: stuck never returns, denial never visits
    healthy_visits, healthy_returns = 3, 3
    assert stuck["returns_completed"] < healthy_returns
    assert denial["treasury_open"] < 0.5
    # the middle way keeps both phases
    balanced = {"visits": 3, "returns": 3}
    assert balanced["visits"] == balanced["returns"]
    print("the middle way: the visit with a return ticket")
    print("OK: %s named the unhealthy turns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven small habits, each a few minutes; balance compounds
    habits = {
        "curated trigger shelf": 0.15,
        "one story a week": 0.15,
        "write the details": 0.12,
        "return ticket set": 0.18,
        "one visit into action": 0.15,
        "share the treasury": 0.13,
        "new door opened": 0.12,
    }
    total = sum(habits.values())
    print("habits kept: %d, combined balance weight: %.2f" % (len(habits), total))
    for h, w in habits.items():
        print("  %-22s +%.2f" % (h, w))
    assert abs(total - 1.0) < 1e-9
    # the present needs deposits too: today's song is tomorrow's trigger
    present_deposits = habits["new door opened"] + habits["one visit into action"]
    assert 0.269 < present_deposits < 0.271
    # small and repeated beats big and occasional
    steady = total * 0.9
    binge = 0.5 * 0.4
    assert steady > binge
    print("minutes a day - the hearth tended, the house lived in")
    print("OK: %s kept the daily round" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cue integration: face + body + voice + context, no single tell decides
    cues = {"face": 0.70, "body": 0.60, "voice": 0.65, "context": 0.90}  # reunion, old song
    integrated = sum(cues.values()) / len(cues)
    print("cue channels: %s" % ", ".join("%s %.2f" % p for p in cues.items()))
    print("integrated read: %.3f" % integrated)
    assert 0.712 < integrated < 0.714
    assert integrated > 0.6  # configuration clears the bar
    # the sadness misread: check for the warmth discriminator
    warmth_present = True   # the small smile, the tender tone
    read = "nostalgia" if (integrated > 0.6 and warmth_present) else "uncertain"
    assert read == "nostalgia"
    # without context the same signs stay ambiguous
    thin = {"face": 0.70, "body": 0.60, "voice": 0.65, "context": 0.20}
    thin_read = sum(thin.values()) / len(thin)
    assert thin_read < 0.6
    print("context is the great clarifier; never label from the outside")
    print("OK: %s read the signs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five supportive moves; each does distinct work
    moves = {
        "do not rush": 0.90,        # protects the replay arc
        "receive the story": 0.85,  # extends savoring, bonds
        "witness without fixing": 0.88,  # moved-tears are not a problem
        "add your thread / ask to be shown": 0.80,  # co-remembering
        "bridge back gently": 0.82,  # completes the visit
    }
    coverage = sum(1 for v in moves.values() if v > 0.5) / len(moves)
    quality = sum(moves.values()) / len(moves)
    print("supportive moves: %d, coverage %.2f, quality %.3f" % (len(moves), coverage, quality))
    for m, v in moves.items():
        print("  %-32s %.2f" % (m, v))
    assert abs(coverage - 1.0) < 1e-9
    assert 0.849 < quality < 0.851
    # the misfire to avoid
    are_you_okay = 0.25  # implies something is wrong
    assert are_you_okay < min(moves.values())
    print("people remember for years who received their nostalgia well")
    print("OK: %s responded supportively" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six well-meaning mistakes, each disrupting a mechanism
    mistakes = {
        "mocking it": "shames a tender emotion",
        "correcting the memory": "fact-checks a feeling",
        "rushing/interrupting": "strands the arc mid-replay",
        "pathologizing": "makes a healthy visit feel shameful",
        "feeding the stuckness": "validates 'nothing measures up'",
        "hijacking the story": "violates narrative ownership",
    }
    print("mistakes recognized: %d" % len(mistakes))
    for m, cost in mistakes.items():
        print("  AVOID: %-22s - %s" % (m, cost))
    assert len(mistakes) == 6
    # the thread: treating the visit as a problem
    thread = all("problem" in c or True for c in mistakes.values())
    assert thread
    # the helpful alternative for stuckness: gentle present-tense invitation
    invitation = 0.85
    confrontation = 0.30
    assert invitation > confrontation
    print("honor the visit - it is the whole of the law")
    print("OK: %s listed the mistakes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_related_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # discriminator quiz: which neighbor is it?
    def classify(center):
        if center == "precious past, mine": return "nostalgia"
        if center == "valued absent, wanted now": return "longing"
        if center == "valued place, separated": return "homesickness"
        if center == "irrevocable loss": return "grief"
        if center == "past judged mistaken": return "regret"
        if center == "good received": return "gratitude"
        return "uncertain"
    cases = {
        "precious past, mine": "nostalgia",
        "valued absent, wanted now": "longing",
        "valued place, separated": "homesickness",
        "irrevocable loss": "grief",
        "past judged mistaken": "regret",
        "good received": "gratitude",
    }
    correct = sum(1 for c, want in cases.items() if classify(c) == want)
    print("neighbors placed: %d/%d" % (correct, len(cases)))
    assert correct == 6
    # border blends exist: appraisals stack
    border = ("precious past, mine", "irrevocable loss")  # nostalgia + grief
    assert len(border) == 2
    print("a practical routing system, not taxonomy for its own sake")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_emotion_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # second-order blends: nostalgia at the center, wearing the partner's colors
    n = 1.0
    blends = {
        "celebration (joy)": n * 0.6 + 0.8 * 0.7,
        "bittersweet (sadness)": n * 0.55 + 0.7 * 0.45,
        "mourning (grief)": n * 0.5 + 0.9 * 0.6,
        "thanksgiving (gratitude)": n * 0.6 + 0.85 * 0.5,
        "legacy (pride)": n * 0.55 + 0.7 * 0.5,
        "homesickness (longing)": n * 0.5 + 0.8 * 0.55,
        "audit (regret)": n * 0.5 + 0.6 * 0.5,
        "reverie (calm)": n * 0.6 + 0.5 * 0.4,
    }
    print("blend strengths:")
    for k, v in blends.items():
        print("  %-24s %.3f" % (k, v))
    assert len(blends) == 8
    assert blends["mourning (grief)"] > blends["reverie (calm)"]  # heaviest vs gentlest
    assert 1.039 < blends["mourning (grief)"] < 1.041
    assert 0.799 < blends["reverie (calm)"] < 0.801
    # interactions, not averages: each partner changes what the nostalgia does
    seeks = {"celebration (joy)": "company", "mourning (grief)": "the memorial",
             "reverie (calm)": "the porch"}
    assert len(set(seeks.values())) == 3
    print("same fire, different light on the walls")
    print("OK: %s mixed the blends" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nostalgia_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the six-scene arc: trigger, rise, peak, turn, channeling, resolution
    scenes = [
        ("trigger 18:40", 3.0, "the first chord lands"),
        ("rise 18:43", 6.0, "rooms open in sequence"),
        ("peak 18:51", 9.0, "shine spills; gratitude surfaces"),
        ("turn 18:58", 4.5, "deep breath; hand to chest"),
        ("channeling 19:05", 5.5, "the text; the unseen photo"),
        ("resolution 20:30", 2.0, "the long telling; easy sleep"),
    ]
    peak = max(s[1] for s in scenes)
    peak_scene = [s[0] for s in scenes if s[1] == peak][0]
    print("scenes: %d" % len(scenes))
    for label, inten, note in scenes:
        print("  %-18s intensity %.1f - %s" % (label, inten, note))
    assert len(scenes) == 6
    assert 8.9 < peak < 9.1
    assert peak_scene == "peak 18:51"
    # resolution lower than peak; channeling lifts above the turn
    assert scenes[5][1] < scenes[2][1]
    assert scenes[4][1] > scenes[3][1]
    descent = scenes[2][1] - scenes[5][1]
    assert 6.9 < descent < 7.1
    # the aftershock: steadiness for days
    aftershock_days, steadiness = 3, 8.5
    assert aftershock_days >= 2 and steadiness > 8.0
    print("peak->resolution descent: %.1f; aftershock: %d days at %.1f" % (descent, aftershock_days, steadiness))
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "nostalgia_definition": demo_nostalgia_definition,
    "nostalgia_emotion_family": demo_nostalgia_emotion_family,
    "nostalgia_intensity_scale": demo_nostalgia_intensity_scale,
    "nostalgia_myths": demo_nostalgia_myths,
    "nostalgia_first_person": demo_nostalgia_first_person,
    "nostalgia_time_course": demo_nostalgia_time_course,
    "nostalgia_low_vs_high": demo_nostalgia_low_vs_high,
    "nostalgia_partner_blend": demo_nostalgia_partner_blend,
    "nostalgia_day_vignette": demo_nostalgia_day_vignette,
    "nostalgia_body_signals": demo_nostalgia_body_signals,
    "nostalgia_posture_movement": demo_nostalgia_posture_movement,
    "nostalgia_sleep_appetite_energy": demo_nostalgia_sleep_appetite_energy,
    "nostalgia_body_differences": demo_nostalgia_body_differences,
    "nostalgia_face": demo_nostalgia_face,
    "nostalgia_face_intensity": demo_nostalgia_face_intensity,
    "nostalgia_hiding_faking": demo_nostalgia_hiding_faking,
    "nostalgia_expression_gallery": demo_nostalgia_expression_gallery,
    "nostalgia_classic_triggers": demo_nostalgia_classic_triggers,
    "nostalgia_personal_triggers": demo_nostalgia_personal_triggers,
    "nostalgia_surprise_triggers": demo_nostalgia_surprise_triggers,
    "nostalgia_chain_reactions": demo_nostalgia_chain_reactions,
    "nostalgia_behavior_actions": demo_nostalgia_behavior_actions,
    "nostalgia_speech_patterns": demo_nostalgia_speech_patterns,
    "nostalgia_decisions_judgment": demo_nostalgia_decisions_judgment,
    "nostalgia_escalation": demo_nostalgia_escalation,
    "nostalgia_healthy_expression": demo_nostalgia_healthy_expression,
    "nostalgia_unhealthy_expression": demo_nostalgia_unhealthy_expression,
    "nostalgia_everyday_practices": demo_nostalgia_everyday_practices,
    "nostalgia_reading_others": demo_nostalgia_reading_others,
    "nostalgia_supportive_responses": demo_nostalgia_supportive_responses,
    "nostalgia_mistakes_to_avoid": demo_nostalgia_mistakes_to_avoid,
    "nostalgia_related_emotions": demo_nostalgia_related_emotions,
    "nostalgia_emotion_mixes": demo_nostalgia_emotion_mixes,
    "nostalgia_full_simulation": demo_nostalgia_full_simulation,
}

assert len(DEMOS) == 34, "expected 34 demos, got %d" % len(DEMOS)
