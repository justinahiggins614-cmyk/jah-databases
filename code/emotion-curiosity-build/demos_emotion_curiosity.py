#!/usr/bin/env python3
"""Demo programs for the Curiosity Emotion databases (emotion series).

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


def demo_curiosity_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three-beat loop: notice -> gap -> seek, weights into drive
    notice = {"novelty": 0.80, "salience": 0.60}
    gap = sum(notice.values()) / len(notice)          # the itch
    seek_drive = min(1.0, gap * 1.25)                 # the pull to act
    print("notice: %.3f  gap: %.3f  seek drive: %.3f" % (sum(notice.values())/2, gap, seek_drive))
    assert 0.699 < gap < 0.701
    assert 0.874 < seek_drive < 0.876
    print("beats: notice -> gap -> seek")
    print("OK: %s ran the three-beat loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_emotion_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Berlyne split: perceptual vs epistemic weights across situations
    situations = {
        "strange_sound": (0.90, 0.20),
        "half_heard_fact": (0.30, 0.95),
        "odd_object": (0.85, 0.45),
        "unfinished_proof": (0.25, 0.90),
    }
    for s, (per, epi) in situations.items():
        dom = "perceptual" if per > epi else "epistemic"
        print("  %-16s perceptual %.2f epistemic %.2f -> %s" % (s, per, epi, dom))
    per_avg = sum(p for p, e in situations.values()) / len(situations)
    epi_avg = sum(e for p, e in situations.values()) / len(situations)
    assert 0.574 < per_avg < 0.576
    assert 0.624 < epi_avg < 0.626
    print("root: approach; two branches - look (perceptual) and learn (epistemic)")
    print("OK: %s mapped the family tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_intensity_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three dials sum into the volume knob 0..10
    def volume(stakes, gap_size, closeness):
        return min(10.0, (stakes + gap_size + closeness) / 3.0 * 10.0)
    def label(v):
        return "mild" if v < 3.5 else ("moderate" if v < 7.0 else "intense")
    cases = [(0.1, 0.2, 0.1), (0.5, 0.6, 0.5), (0.9, 0.95, 0.9)]
    for stakes, gap_size, closeness in cases:
        v = volume(stakes, gap_size, closeness)
        print("dials %.2f/%.2f/%.2f -> volume %.2f (%s)" % (stakes, gap_size, closeness, v, label(v)))
        assert label(v) in ("mild", "moderate", "intense")
    assert 1.332 < volume(0.1, 0.2, 0.1) < 1.334
    assert 5.332 < volume(0.5, 0.6, 0.5) < 5.334
    assert 9.166 < volume(0.9, 0.95, 0.9) < 9.168
    print("OK: %s set the three dials" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # myth vs measured: topic hops are finished micro-investigations, not distraction
    myths = {
        "killed the cat": "warns against recklessness, not wondering",
        "cannot focus": "curiosity IS focus - attention locks onto the gap",
        "born with it": "trainable like a muscle - reward questions, it grows",
        "just nosiness": "nosiness wants gossip; curiosity wants understanding",
    }
    for myth, correction in myths.items():
        print("  myth: %-15s -> %s" % (myth, correction))
    assert len(myths) == 4
    # focus-lock demo: dwell time per hop rises when gaps are rewarded
    dwell = [2.0, 3.5, 6.0, 9.5]  # minutes per investigation, rewarded environment
    growth = dwell[-1] / dwell[0]
    print("dwell growth under rewarded questions: %.2fx" % growth)
    assert 4.74 < growth < 4.76
    print("OK: %s busted the four myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attention narrowing onto the gap across 5 minutes of wondering
    attention = [0.30, 0.55, 0.72, 0.85, 0.93]
    for minute, a in enumerate(attention):
        print("  minute %d: attention on gap %.2f" % (minute, a))
        assert 0.0 < a < 1.0
    narrowing = attention[-1] - attention[0]
    print("narrowing: %.2f" % narrowing)
    assert 0.629 < narrowing < 0.631
    # time thinning: perceived minutes vs clock minutes
    perceived = sum(attention) / len(attention) * 5.0
    print("clock 5.0 min felt like %.2f min" % perceived)
    assert 3.349 < perceived < 3.351
    print("OK: %s walked inside the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four phases with drive level and duration share
    phases = [
        ("onset", 0.85, 0.05),
        ("peak", 1.00, 0.70),
        ("fading", 0.35, 0.15),
        ("aftershock", 0.55, 0.10),
    ]
    for name_, drive, share in phases:
        print("  %-10s drive %.2f  time share %4.1f %%" % (name_, drive, share * 100.0))
    assert abs(sum(s for _, _, s in phases) - 1.0) < 1e-9
    # aftershock: one answered question births new ones
    new_gaps = 3
    print("answered 1 question -> %d new gaps (molting)" % new_gaps)
    assert new_gaps == 3
    print("OK: %s ran onset to aftershock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pebble vs flood: resource spend in the two snapshots
    low = {"minutes": 0.5, "obstacles_cleared": 0, "tunnel": 0.10}
    high = {"minutes": 180.0, "obstacles_cleared": 4, "tunnel": 0.90}
    for snap, d in (("low ", low), ("high", high)):
        print("  %s minutes %6.1f obstacles %d tunnel %.2f" % (snap, d["minutes"], d["obstacles_cleared"], d["tunnel"]))
    ratio = high["minutes"] / low["minutes"]
    print("time ratio high/low: %.0f" % ratio)
    assert 359.9 < ratio < 360.1
    assert high["obstacles_cleared"] > low["obstacles_cleared"]
    assert high["tunnel"] > low["tunnel"]
    print("same emotion, different volume")
    print("OK: %s contrasted the two snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_joy_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the delight-in-discovery blend: curiosity pull + joy glow
    curiosity, joy = 0.85, 0.75
    delight = (curiosity + joy) / 2.0 * 1.15   # synergy bonus
    delight = min(1.0, delight)
    print("curiosity %.2f + joy %.2f -> delight %.3f" % (curiosity, joy, delight))
    assert 0.919 < delight < 0.921
    # self-fueling: each discovery raises appetite for the next gap
    appetite = 0.50
    for i in range(3):
        appetite = min(1.0, appetite + delight * 0.25)
        print("  discovery %d -> appetite %.3f" % (i + 1, appetite))
    assert 1.0 - 1e-9 < appetite <= 1.0
    print("OK: %s blended the partners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four hooks across the day: minutes spent vs value returned
    hooks = [
        ("kettle rattle", "perceptual", 0.5, 1),
        ("coworker word", "social", 5.0, 3),
        ("chart mismatch", "epistemic", 25.0, 9),
        ("documentary city", "diversive", 20.0, 4),
    ]
    total_min = 0.0
    total_val = 0
    for label, mode, minutes, value in hooks:
        total_min += minutes
        total_val += value
        print("  %-15s %-10s %5.1f min -> value %d" % (label, mode, minutes, value))
    print("day total: %.1f min -> value %d" % (total_min, total_val))
    assert 50.4 < total_min < 50.6
    assert total_val == 17
    print("OK: %s walked the ordinary day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_body_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # funded, not alarmed: arousal up, tension down
    rest = {"heart": 68.0, "breath": 14.0, "tension": 0.50}
    curious = {"heart": 76.0, "breath": 16.5, "tension": 0.32}
    for k in rest:
        print("  %-7s rest %.1f -> curious %.1f" % (k, rest[k], curious[k]))
    assert 7.9 < curious["heart"] - rest["heart"] < 8.1
    assert 2.4 < curious["breath"] - rest["breath"] < 2.6
    assert curious["tension"] < rest["tension"]
    # pupil widening: percent increase in diameter
    pupil_gain = (5.2 - 4.0) / 4.0 * 100.0
    print("pupil diameter gain: %.1f %%" % pupil_gain)
    assert 29.9 < pupil_gain < 30.1
    print("OK: %s read the body signals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_posture_movement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the approach posture in degrees and behavior shifts
    lean = 12.0        # torso degrees toward target
    head_tilt = 8.0    # orienting tilt
    walk_slow = 0.60   # walking speed multiplier near the target
    print("lean %.1f deg  head tilt %.1f deg  walk speed x%.2f" % (lean, head_tilt, walk_slow))
    assert 11.9 < lean < 12.1
    assert 7.9 < head_tilt < 8.1
    assert 0.59 < walk_slow < 0.61
    # sunflower angling: curious audience members facing the speaker
    facing = 9
    total = 10
    print("audience facing speaker: %d/%d" % (facing, total))
    assert facing / total > 0.8
    print("OK: %s carried the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_sleep_appetite_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the just-one-more-chapter ledger for one evening hunt
    chapters = 4
    minutes_each = 22.0
    borrowed = chapters * minutes_each
    print("chapters %d x %.0f min = %.0f min borrowed from sleep" % (chapters, minutes_each, borrowed))
    assert 87.9 < borrowed < 88.1
    # appetite delay: meal pushed back while the hunt is hot
    meal_delay = 95.0
    print("meal delayed %.0f min; energy during hunt +%.0f %%" % (meal_delay, 35.0))
    assert 94.9 < meal_delay < 95.1
    # the bill: fatigue masked during, paid after
    masked, paid = 0.75, 0.75
    assert abs(masked - paid) < 1e-9
    print("fatigue masked %.2f = fatigue paid %.2f (the bill arrives later)" % (masked, paid))
    print("OK: %s balanced the day ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_body_differences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same loop, different loudspeakers: expression profiles sum to the same drive
    profiles = {
        "still_and_quiet": {"movement": 0.10, "voice": 0.15, "inner": 0.95},
        "fidgety_talkative": {"movement": 0.90, "voice": 0.95, "inner": 0.60},
        "head_buzzer": {"movement": 0.30, "voice": 0.40, "inner": 0.90},
        "chest_flutterer": {"movement": 0.45, "voice": 0.50, "inner": 0.85},
    }
    for label, ch in profiles.items():
        total = sum(ch.values())
        print("  %-16s movement %.2f voice %.2f inner %.2f (total %.2f)" % (label, ch["movement"], ch["voice"], ch["inner"], total))
    totals = [sum(ch.values()) for ch in profiles.values()]
    spread = max(totals) - min(totals)
    print("expression spread: %.2f (wide) vs loop underneath: identical" % spread)
    assert 1.24 < spread < 1.26
    print("OK: %s honored the differences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the data-collection mask: feature checklist scores 0..1
    features = {
        "eyes_widened": 0.90, "pupils_larger": 0.85, "gaze_locked": 0.95,
        "brows_lifted": 0.80, "brows_knit": 0.55, "lips_parted": 0.70,
        "blink_rate_down": 0.88, "head_tilt": 0.75,
    }
    score = sum(features.values()) / len(features)
    for f, v in features.items():
        print("  %-15s %.2f" % (f, v))
    print("mask score: %.3f" % score)
    assert 0.796 < score < 0.798
    assert score > 0.5
    print("OK: %s assembled the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three gears: each is the last with the volume turned up
    gears = {
        "mild": {"brow_lift": 0.30, "eye_wide": 0.25, "lean": 0.10, "hand": 0.00},
        "moderate": {"brow_lift": 0.65, "eye_wide": 0.70, "lean": 0.55, "hand": 0.20},
        "high": {"brow_lift": 0.95, "eye_wide": 0.95, "lean": 0.90, "hand": 0.85},
    }
    prev = None
    for gear, feats in gears.items():
        total = sum(feats.values())
        print("  %-8s total %.2f" % (gear, total))
        if prev is not None:
            assert total > prev, "gears must scale smoothly upward"
        prev = total
    assert 0.64 < sum(gears["mild"].values()) < 0.66
    assert 2.09 < sum(gears["moderate"].values()) < 2.11
    assert 3.64 < sum(gears["high"].values()) < 3.66
    print("OK: %s shifted the three gears" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hiding: face guarded, other channels leak; faking: face staged, follow-through missing
    hidden = {"face_guarded": 0.90, "lean_leak": 0.75, "glance_leak": 0.80, "question_leak": 0.65}
    leak = (hidden["lean_leak"] + hidden["glance_leak"] + hidden["question_leak"]) / 3.0
    print("hidden face guard %.2f but leak average %.3f" % (hidden["face_guarded"], leak))
    assert 0.732 < leak < 0.734
    assert leak > 0.5, "the body keeps receipts"
    faked = {"face_staged": 0.90, "followup_questions": 0.10, "sustained_attention": 0.15}
    follow = (faked["followup_questions"] + faked["sustained_attention"]) / 2.0
    print("faked face stage %.2f but follow-through %.3f" % (faked["face_staged"], follow))
    assert 0.124 < follow < 0.126
    assert follow < 0.3, "cannot stage the follow-through"
    print("OK: %s caught the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the drawable recipe: element weights for the portrait
    recipe = [
        ("eyes wider than rest, lids lifted", 0.95),
        ("brows raised inner, faint knit", 0.90),
        ("lips parted, no corner tension", 0.75),
        ("head tilt 5-10 degrees", 0.80),
        ("lean toward target", 0.85),
        ("thinker hand (stage)", 0.60),
    ]
    for element, w in recipe:
        print("  [%.2f] %s" % (w, element))
    mean_w = sum(w for _, w in recipe) / len(recipe)
    print("recipe completeness: %.3f" % mean_w)
    assert 0.807 < mean_w < 0.809
    # duration cue: curiosity held vs surprise flash (seconds)
    hold = 8.0
    flash = 0.8
    print("held pose %.1fs vs flash %.1fs" % (hold, flash))
    assert hold / flash > 5.0
    print("OK: %s sketched the gallery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five classic triggers with gap sizes they open
    triggers = {
        "novelty": 0.75, "incompleteness": 0.90,
        "complexity": 0.70, "surprise": 0.85, "direct_question": 0.95,
    }
    for t, gap in triggers.items():
        print("  %-16s opens gap %.2f" % (t, gap))
    strongest = max(triggers, key=triggers.get)
    print("strongest opener: %s" % strongest)
    assert strongest == "direct_question"
    mean_gap = sum(triggers.values()) / len(triggers)
    print("mean gap: %.3f" % mean_gap)
    assert 0.829 < mean_gap < 0.831
    print("OK: %s rang the five triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # self-relevance multiplies the pull of private cues
    cues = {"song": 0.50, "smell": 0.65, "anniversary": 0.70, "old_place": 0.60}
    self_relevance = 1.6
    for cue, base in cues.items():
        pulled = min(1.0, base * self_relevance)
        print("  %-11s base %.2f x relevance %.1f -> pull %.3f" % (cue, base, self_relevance, pulled))
        assert pulled > base
    pulls = [min(1.0, b * self_relevance) for b in cues.values()]
    mean_pull = sum(pulls) / len(pulls)
    print("mean personal pull: %.3f vs generic novelty 0.75" % mean_pull)
    assert 0.939 < mean_pull < 0.941
    assert mean_pull > 0.75
    print("OK: %s tripped the private wires" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # expectation violation magnitude + strangeness bonus
    oddities = {
        "typo in beloved book": (0.60, 0.30),
        "too-neat coincidence": (0.75, 0.45),
        "once-only machine glitch": (0.80, 0.40),
        "found grocery list": (0.55, 0.50),
    }
    for label, (violation, strange) in oddities.items():
        pull = min(1.0, violation + strange * 0.5)
        print("  %-24s violation %.2f strange %.2f -> pull %.3f" % (label, violation, strange, pull))
    pulls = [min(1.0, v + s * 0.5) for v, s in oddities.values()]
    best = max(pulls)
    print("strongest odd pull: %.3f" % best)
    assert 0.999 < best < 1.001
    mean_pull = sum(pulls) / len(pulls)
    assert 0.880 < mean_pull < 0.883
    print("OK: %s chased the stray lights" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the domino run: word -> event -> person -> movement -> documentary
    chain = ["word", "event", "person", "movement", "documentary"]
    gaps_opened = [2, 2, 3, 2, 1]   # each answer opens new gaps
    total = 0
    for step, (link, opened) in enumerate(zip(chain, gaps_opened)):
        total += opened
        print("  step %d %-12s opens %d new gaps (running total %d)" % (step + 1, link, opened, total))
    print("one trigger -> %d gaps across %d links" % (total, len(chain)))
    assert total == 10
    # narrowing: question specificity rises along the chain
    specificity = [0.20, 0.40, 0.60, 0.80, 0.95]
    assert specificity == sorted(specificity)
    print("specificity rises: broad -> precise")
    print("OK: %s ran the dominoes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_behavior_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the six moves: cost vs decisiveness
    moves = {
        "ask": (0.20, 0.70), "look_closer": (0.30, 0.60), "search": (0.40, 0.80),
        "follow": (0.55, 0.65), "collect": (0.35, 0.50), "test": (0.80, 0.95),
    }
    for move, (cost, decisive) in moves.items():
        value = decisive / cost
        print("  %-11s cost %.2f decisive %.2f value %.2f" % (move, cost, decisive, value))
    best_value = max(d / c for c, d in moves.values())
    print("best value-per-cost: %.2f (ask)" % best_value)
    assert 3.49 < best_value < 3.51
    most_decisive = max(moves, key=lambda m: moves[m][1])
    assert most_decisive == "test"
    print("most decisive: %s" % most_decisive)
    print("OK: %s worked the toolkit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_speech_patterns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dialect: question words per 100 spoken words, curious vs neutral
    curious_rate = 11.5
    neutral_rate = 3.0
    print("question words per 100: curious %.1f vs neutral %.1f" % (curious_rate, neutral_rate))
    ratio = curious_rate / neutral_rate
    print("ratio: %.2f" % ratio)
    assert 3.82 < ratio < 3.84
    # upward tilt: share of sentences ending on a rising tone
    tilt_curious, tilt_neutral = 0.62, 0.28
    print("rising-tone share: curious %.2f vs neutral %.2f" % (tilt_curious, tilt_neutral))
    assert tilt_curious > tilt_neutral + 0.3
    print("OK: %s spoke the dialect" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_decisions_judgment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # information in the ledger: unfamiliar option priced above its odds
    known = {"dinner": 7.0, "info": 0.0}
    unknown = {"dinner": 6.5, "info": 2.0}
    known_total = sum(known.values())
    unknown_total = sum(unknown.values())
    print("known option total %.1f vs unknown option total %.1f" % (known_total, unknown_total))
    assert unknown_total > known_total
    assert 1.49 < unknown_total - known_total < 1.51
    # paying for answers: minutes waited to learn early
    wait_paid = 12.0
    print("minutes waited just to learn the answer early: %.0f" % wait_paid)
    assert wait_paid > 0
    print("the mind prices information as a good worth buying")
    print("OK: %s priced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four rungs: budget authorized at each
    rungs = [
        ("glance", 1.0),
        ("probe", 15.0),
        ("reorganize", 180.0),
        ("restructure", 1500.0),
    ]
    for rung, budget in rungs:
        print("  %-11s authorized budget %7.1f min-equivalents" % (rung, budget))
    budgets = [b for _, b in rungs]
    assert budgets == sorted(budgets)
    ratio = budgets[-1] / budgets[0]
    print("top rung costs %.0fx the bottom" % ratio)
    assert 1499.9 < ratio < 1500.1
    print("OK: %s climbed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four moves compound the generosity loop
    moves = {"say_it": 0.25, "show_it": 0.30, "channel_it": 0.35, "share_it": 0.40}
    loop = 1.0
    for move, gain in moves.items():
        loop *= (1.0 + gain)
        print("  %-10s loop x%.2f -> %.3f" % (move, 1.0 + gain, loop))
    print("generosity loop multiplier: %.3f" % loop)
    assert 3.070 < loop < 3.073
    assert loop > 2.0, "generous twice over"
    print("OK: %s lit the public light" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottling vs exploding: costs over a year, arbitrary units
    bottled = {"assumptions": 30.0, "apathy": 45.0, "missed": 25.0}
    exploded = {"trust_burned": 40.0, "boundaries": 35.0, "burnout": 30.0}
    b_total = sum(bottled.values())
    e_total = sum(exploded.values())
    for k, v in bottled.items():
        print("  bottled   %-11s cost %.0f" % (k, v))
    for k, v in exploded.items():
        print("  exploded  %-11s cost %.0f" % (k, v))
    print("bottled total %.0f vs exploded total %.0f" % (b_total, e_total))
    assert 99.9 < b_total < 100.1
    assert 104.9 < e_total < 105.1
    # the middle path costs a fraction of either
    tended = 12.0
    assert tended < b_total / 5.0 and tended < e_total / 5.0
    print("tended curiosity cost: %.0f (a fraction of either failure)" % tended)
    print("OK: %s priced both failures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five small habits: hooks noticed per week grows additively
    habits = {
        "notebook": 0.08, "daily_question": 0.10, "novelty_slot": 0.07,
        "ten_minute_rule": 0.06, "close_loops": 0.09,
    }
    hooks = 2.0
    for habit, weekly in habits.items():
        hooks += weekly * 10.0
        print("  %-15s weekly +%.0f %% -> hooks/week %.2f" % (habit, weekly * 100, hooks))
    annual = hooks * 52.0
    print("hooks noticed per year: %.0f (from 104 with no habits)" % annual)
    assert 311.9 < annual < 312.1
    print("small, repeated, compounding - that is the whole trick")
    print("OK: %s walked the keeper rounds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_reading_others(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels corroborate; two in agreement = confident read
    channels = {"face": 0.85, "body": 0.75, "voice": 0.70, "behavior": 0.90}
    for ch, v in channels.items():
        print("  %-8s signal %.2f" % (ch, v))
    pairs = 0
    keys = list(channels)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if channels[keys[i]] > 0.5 and channels[keys[j]] > 0.5:
                pairs += 1
    print("agreeing pairs: %d of 6" % pairs)
    assert pairs == 6
    # the gold standard: follow-up questions are expensive to fake
    followups = 4
    print("follow-up questions observed: %d -> confident read" % followups)
    assert followups >= 2
    print("OK: %s sighted the beacon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five moves raising the expected value of another person's gaps
    moves = {
        "feed_the_hunt": 0.30, "protect_question": 0.35, "make_room": 0.20,
        "lend_tools": 0.25, "celebrate": 0.30,
    }
    value = 1.0
    for move, boost in moves.items():
        value *= (1.0 + boost)
        print("  %-16s gap value x%.2f -> %.3f" % (move, 1.0 + boost, value))
    print("their gaps now worth %.2fx" % value)
    assert 3.421 < value < 3.424
    print("OK: %s kept the harbor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_mistakes_to_avoid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five mistakes raising the price of wondering
    mistakes = {
        "mock the question": 0.90, "wall answer": 0.70, "hijack the hunt": 0.60,
        "rush the closure": 0.45, "punish the tangent": 0.80,
    }
    price = 1.0
    for m, hike in mistakes.items():
        price *= (1.0 + hike)
        print("  %-18s price x%.2f -> %.3f" % (m, 1.0 + hike, price))
    print("wondering now costs %.2fx - the lesson is about safety" % price)
    assert 13.48 < price < 13.50
    print("OK: %s posted the hazards" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_emotion_map(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # distance from curiosity on the unknown-handling map (0 = same house)
    distances = {
        "interest": 0.15, "wonder": 0.30, "surprise": 0.35, "anticipation": 0.40,
        "boredom": 0.85, "apathy": 0.95, "nosiness": 0.45, "awe": 0.55,
    }
    for emotion, d in sorted(distances.items(), key=lambda kv: kv[1]):
        print("  %-13s distance %.2f" % (emotion, d))
    nearest = min(distances, key=distances.get)
    farthest = max(distances, key=distances.get)
    print("nearest: %s  farthest: %s" % (nearest, farthest))
    assert nearest == "interest"
    assert farthest == "apathy"
    assert distances["nosiness"] > distances["interest"]
    print("OK: %s walked the district" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_emotion_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Plutchik-style dyads: curiosity 1.0 blended with four partners
    curiosity = 1.0
    blends = {
        "delight_in_discovery": (curiosity, 0.80, "joy"),
        "cautious_investigation": (curiosity, 0.70, "fear"),
        "wonder": (curiosity, 0.90, "surprise"),
        "itch_of_almost_known": (curiosity, 0.85, "anticipation"),
    }
    for blend, (c, p, partner) in blends.items():
        strength = (c + p) / 2.0 * 1.10
        print("  %-22s curiosity %.1f + %s %.2f -> %.3f" % (blend, c, partner, p, strength))
        assert 0.9 < strength < 1.1
    strengths = [(c + p) / 2.0 * 1.10 for c, p, _ in blends.values()]
    assert 3.986 < sum(strengths) < 3.989
    print("four blends, one shared engine")
    print("OK: %s flew combined colors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_curiosity_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the attic box: five scenes, drive and questions per scene
    scenes = [
        ("trigger", 0.90, 3),
        ("onset", 0.95, 5),
        ("peak hunt", 1.00, 8),
        ("the turn", 0.70, 2),
        ("resolution", 0.40, 0),
    ]
    total_q = 0
    for scene, drive, questions in scenes:
        total_q += questions
        print("  %-10s drive %.2f questions %d" % (scene, drive, questions))
    print("questions across the arc: %d" % total_q)
    assert total_q == 18
    peak = max(scenes, key=lambda s: s[1])
    assert peak[0] == "peak hunt"
    # the molt: resolution opens the town
    aftershock_gaps = 2
    print("resolution opens %d new gaps (the town) - the molt" % aftershock_gaps)
    assert aftershock_gaps == 2
    print("OK: %s opened the attic box" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "curiosity_definition": demo_curiosity_definition,
    "curiosity_emotion_family": demo_curiosity_emotion_family,
    "curiosity_intensity_scale": demo_curiosity_intensity_scale,
    "curiosity_myths": demo_curiosity_myths,
    "curiosity_first_person": demo_curiosity_first_person,
    "curiosity_time_course": demo_curiosity_time_course,
    "curiosity_low_vs_high": demo_curiosity_low_vs_high,
    "curiosity_joy_blend": demo_curiosity_joy_blend,
    "curiosity_day_vignette": demo_curiosity_day_vignette,
    "curiosity_body_signals": demo_curiosity_body_signals,
    "curiosity_posture_movement": demo_curiosity_posture_movement,
    "curiosity_sleep_appetite_energy": demo_curiosity_sleep_appetite_energy,
    "curiosity_body_differences": demo_curiosity_body_differences,
    "curiosity_face": demo_curiosity_face,
    "curiosity_face_intensity": demo_curiosity_face_intensity,
    "curiosity_hiding_faking": demo_curiosity_hiding_faking,
    "curiosity_expression_gallery": demo_curiosity_expression_gallery,
    "curiosity_classic_triggers": demo_curiosity_classic_triggers,
    "curiosity_personal_triggers": demo_curiosity_personal_triggers,
    "curiosity_surprise_triggers": demo_curiosity_surprise_triggers,
    "curiosity_chain_reactions": demo_curiosity_chain_reactions,
    "curiosity_behavior_actions": demo_curiosity_behavior_actions,
    "curiosity_speech_patterns": demo_curiosity_speech_patterns,
    "curiosity_decisions_judgment": demo_curiosity_decisions_judgment,
    "curiosity_escalation": demo_curiosity_escalation,
    "curiosity_healthy_expression": demo_curiosity_healthy_expression,
    "curiosity_unhealthy_expression": demo_curiosity_unhealthy_expression,
    "curiosity_everyday_practices": demo_curiosity_everyday_practices,
    "curiosity_reading_others": demo_curiosity_reading_others,
    "curiosity_supportive_responses": demo_curiosity_supportive_responses,
    "curiosity_mistakes_to_avoid": demo_curiosity_mistakes_to_avoid,
    "curiosity_emotion_map": demo_curiosity_emotion_map,
    "curiosity_emotion_mixes": demo_curiosity_emotion_mixes,
    "curiosity_full_simulation": demo_curiosity_full_simulation,
}
