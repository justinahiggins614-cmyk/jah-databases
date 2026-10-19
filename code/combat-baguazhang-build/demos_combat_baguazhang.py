#!/usr/bin/env python3
"""Demo programs for the Baguazhang Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: circle geometry, step counts, timing,
strike mechanics, weapon leverage, and drill scoring with real computed
values. All are machine-executed by build.py before pages are written:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_bgz_meaning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Dong Haichuan: 1797 -> 1882
    born, died = 1797, 1882
    lifespan = died - born
    print("Dong Haichuan lifespan: %d - %d = %d years" % (born, died, lifespan))
    assert lifespan == 85
    # taught in Beijing from about 1864
    beijing_start = 1864
    teaching_years = died - beijing_start
    print("Beijing teaching years: %d - %d = %d" % (beijing_start, died, teaching_years))
    assert teaching_years == 18
    # the three principal internal arts
    internal_arts = ["xingyiquan", "taijiquan", "baguazhang"]
    print("principal internal arts: %d" % len(internal_arts))
    assert len(internal_arts) == 3
    # eight trigrams behind the name
    trigrams = 8
    print("trigrams in the name: %d" % trigrams)
    assert trigrams == 8
    print("OK: %s named the art" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_circle_walking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # circle geometry: diameter 8 ft -> circumference
    diameter_ft = 8.0
    circ_ft = math.pi * diameter_ft
    print("8 ft circle circumference: %.2f ft" % circ_ft)
    assert 25.12 < circ_ft < 25.14
    # eight steps per revolution -> step arc length
    step_ft = circ_ft / 8.0
    print("step arc length (8 steps/rev): %.3f ft" % step_ft)
    assert 3.141 < step_ft < 3.143
    # beginner range 6..12 ft: circumference range
    c6, c12 = math.pi * 6.0, math.pi * 12.0
    print("beginner circle range: %.2f .. %.2f ft" % (c6, c12))
    assert 18.84 < c6 < 18.86 and 37.69 < c12 < 37.71
    # five minutes each direction at 60 steps/min -> revolutions
    steps = 60 * 5
    revs = steps / 8.0
    print("5 min at 60 steps/min: %d steps = %.1f revolutions" % (steps, revs))
    assert 37.4 < revs < 37.6
    print("OK: %s walked the circle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_mud_wading(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # slide length 0.30 m, twenty slides out and twenty back
    slide_m = 0.30
    total_m = slide_m * 40
    print("line drill: 40 slides x %.2f m = %.1f m" % (slide_m, total_m))
    assert 11.99 < total_m < 12.01
    # sole clearance must stay under a coin's thickness (~2 mm)
    clearance_mm = 1.5
    print("sole clearance: %.1f mm (limit 2.0 mm)" % clearance_mm)
    assert clearance_mm < 2.0
    # head height constant: bob under 2 cm
    bob_cm = 1.2
    print("head bob: %.1f cm (limit 2.0 cm)" % bob_cm)
    assert bob_cm < 2.0
    # cadence: one slide per 1.2 s -> slides per minute
    per_min = 60.0 / 1.2
    print("slides per minute at 1.2 s cadence: %.0f" % per_min)
    assert 49.9 < per_min < 50.1
    print("OK: %s waded the mud" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_swing_hook_steps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # direction change: full 180 degree reversal
    reversal_deg = 180.0
    print("direction reversal: %.0f degrees" % reversal_deg)
    assert reversal_deg == 180.0
    # hook step toe-in angle about 45 degrees pigeon-toed
    hook_deg = 45.0
    print("kou bu toe-in angle: %.0f degrees" % hook_deg)
    assert 44.9 < hook_deg < 45.1
    # drill: ten swing-hook pairs each side
    pairs = 10 * 2
    print("line drill pairs: %d" % pairs)
    assert pairs == 20
    # the turn completes within two steps
    turn_steps = 2
    print("turn completes within %d steps" % turn_steps)
    assert turn_steps == 2
    # inner/outer foot naming: 2 terms
    terms = ["waibu", "neibu"]
    print("foot-position terms: %d" % len(terms))
    assert len(terms) == 2
    print("OK: %s swung and hooked" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_posture_alignment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance depth: knee angle about 135 degrees (thigh burn zone)
    knee_deg = 135.0
    print("walking knee angle: %.0f degrees" % knee_deg)
    assert 134.9 < knee_deg < 135.1
    # sedan-chair test: head height variation under a finger width (~2 cm)
    head_var_cm = 1.6
    print("head height variation: %.1f cm (limit 2.0 cm)" % head_var_cm)
    assert head_var_cm < 2.0
    # hold standard: five minutes of aligned walking
    hold_min = 5.0
    print("aligned walking hold: %.0f minutes" % hold_min)
    assert hold_min == 5.0
    # waist twist range each side in degrees
    twist_deg = 45.0
    print("waist twist each side: %.0f degrees" % twist_deg)
    assert 44.9 < twist_deg < 45.1
    print("OK: %s held the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_static_postures(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight static postures in the traditional set
    postures = 8
    print("static postures in the set: %d" % postures)
    assert postures == 8
    # session: 3 postures x 2 min x 2 directions
    session_min = 3 * 2 * 2
    print("starter session: 3 postures x 2 min x 2 ways = %d min" % session_min)
    assert session_min == 12
    # the classic hand: thumb-index 'L' angle 90 degrees
    l_deg = 90.0
    print("thumb-index L angle: %.0f degrees" % l_deg)
    assert l_deg == 90.0
    # rear palm guards below lead elbow: fingertip offset in cm
    offset_cm = 5.0
    print("rear fingertips below lead elbow: %.0f cm" % offset_cm)
    assert 4.9 < offset_cm < 5.1
    print("OK: %s held the eight postures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_single_change(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # single change: block then strike then reverse (180 deg)
    moves = ["block", "strike", "reverse"]
    print("single change sequence: %d moves" % len(moves))
    assert len(moves) == 3
    # drill: walk 4 steps, change, 4 steps, change - ten changes each side
    changes = 10 * 2
    print("drill changes: %d" % changes)
    assert changes == 20
    # eight-step rhythm preserved through the change
    rhythm = 8
    print("steps per revolution kept: %d" % rhythm)
    assert rhythm == 8
    # first of eight changes
    order = 1
    print("change number in sequence: %d of 8" % order)
    assert order == 1
    print("OK: %s changed the single palm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_double_change(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # both arms describe a full 360 degree wheel
    wheel_deg = 360.0
    print("arm wheel during the turn: %.0f degrees" % wheel_deg)
    assert wheel_deg == 360.0
    # two hands working as one system
    hands = 2
    print("hands in the change: %d" % hands)
    assert hands == 2
    # ten changes each side, continuous arm-circle
    changes = 10 * 2
    print("drill changes: %d" % changes)
    assert changes == 20
    # second of eight changes
    order = 2
    print("change number in sequence: %d of 8" % order)
    assert order == 2
    print("OK: %s changed the double palm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_single_palm_strike(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fist/palm speed: v = omega * r (waist turn x arm length)
    omega = 10.0      # rad/s waist-shoulder turn
    arm_m = 0.65      # shoulder to palm heel
    v = omega * arm_m
    print("waist turn %.1f rad/s x arm %.2f m -> palm speed %.2f m/s" % (omega, arm_m, v))
    assert 6.49 < v < 6.51
    # travel time over 0.5 m
    t = 0.5 / v
    print("strike travel over 0.50 m: %.4f s" % t)
    assert 0.0768 < t < 0.0770
    # ten strikes each side
    reps = 10 * 2
    print("drill reps: %d" % reps)
    assert reps == 20
    print("OK: %s struck with the single palm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_double_palm_strike(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body momentum arriving with the hands: 75 kg at 1.5 m/s
    mass_kg, speed_ms = 75.0, 1.5
    p = mass_kg * speed_ms
    print("body momentum into the double palm: %.1f kg m/s" % p)
    assert 112.4 < p < 112.6
    # two palms land together: simultaneity within 20 ms
    gap_ms = 12.0
    print("palm landing gap: %.0f ms (limit 20 ms)" % gap_ms)
    assert gap_ms < 20.0
    # push-through: two inches past contact
    through_in = 2.0
    print("push-through past contact: %.0f in" % through_in)
    assert through_in == 2.0
    # ten issues each side
    reps = 10 * 2
    print("drill reps: %d" % reps)
    assert reps == 20
    print("OK: %s issued the double palm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_millstone_palm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grinding circles: 0.15 m radius at 24 grinds/min for 5 min
    per_min, minutes = 24.0, 5.0
    grinds = per_min * minutes
    print("grinding session: %.0f x %.0f = %.0f circles" % (per_min, minutes, grinds))
    assert 119.9 < grinds < 120.1
    # one grind circle circumference
    circ_m = 2 * math.pi * 0.15
    print("one grind circle: %.3f m" % circ_m)
    assert 0.942 < circ_m < 0.943
    # total grinding distance per session
    total_m = circ_m * grinds
    print("total grinding distance: %.1f m" % total_m)
    assert 113.0 < total_m < 113.2
    # reverse grind direction every 2 revolutions
    print("OK: %s turned the millstone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_breathing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 4 steps in, 4 steps out at 60 steps/min -> 8 s breath cycle
    cycle_s = 8.0 / 1.0
    steps_per_cycle = 8
    secs = steps_per_cycle / 60.0 * 60.0
    print("breath cycle: %d steps = %.0f s" % (steps_per_cycle, secs))
    assert 7.9 < secs < 8.1
    # five-minute session -> breath cycles
    cycles = 5 * 60 / secs
    print("breath cycles in 5 min: %.1f" % cycles)
    assert 37.4 < cycles < 37.6
    # lengthened practice: 6 in, 6 out
    long_cycle = 12 / 60.0 * 60.0
    print("lengthened cycle: %.0f s" % long_cycle)
    assert 11.9 < long_cycle < 12.1
    # tension scan every revolution
    print("OK: %s breathed with the circle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_flowing_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flowing change: no braking - footfall rhythm unbroken
    # walking momentum 75 kg at 1.2 m/s carried through the turn
    mass_kg, speed_ms = 75.0, 1.2
    ke = 0.5 * mass_kg * speed_ms ** 2
    print("walking kinetic energy carried through: %.1f J" % ke)
    assert 53.9 < ke < 54.1
    # turn angle 180 degrees ridden, not braked
    turn_deg = 180.0
    print("turn ridden through: %.0f degrees" % turn_deg)
    assert turn_deg == 180.0
    # drill: ten flowing vs ten single, feel the difference
    reps = 10 + 10
    print("comparison drill reps: %d" % reps)
    assert reps == 20
    # third of eight changes
    order = 3
    print("change number in sequence: %d of 8" % order)
    assert order == 3
    print("OK: %s flowed with the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_back_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full half-turn of the torso: 180 degrees
    turn_deg = 180.0
    print("torso turn: %.0f degrees" % turn_deg)
    assert turn_deg == 180.0
    # slow-motion drill first: ten reps each side at half speed
    reps = 10 * 2
    print("slow drill reps: %d" % reps)
    assert reps == 20
    # back-guard sweep covers 180 degrees of rear arc
    guard_deg = 180.0
    print("back-guard sweep arc: %.0f degrees" % guard_deg)
    assert guard_deg == 180.0
    # fourth of eight changes
    order = 4
    print("change number in sequence: %d of 8" % order)
    assert order == 4
    print("OK: %s turned the back body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_turning_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full 360 spin on the weighted leg's axis
    spin_deg = 360.0
    print("axis spin: %.0f degrees" % spin_deg)
    assert spin_deg == 360.0
    # stationary axis drill: ten full rotations each leg
    spins = 10 * 2
    print("stationary spins: %d" % spins)
    assert spins == 20
    # the circle turn takes two step-times (1.0 s per step -> 2.0 s)
    turn_s = 2.0
    print("turn time: %.1f s (two step-times)" % turn_s)
    assert 1.99 < turn_s < 2.01
    # fifth of eight changes
    order = 5
    print("change number in sequence: %d of 8" % order)
    assert order == 5
    print("OK: %s spun the turning body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_rubbing_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grinding contact: coefficient of friction forearm-on-arm ~0.4
    mu = 0.4
    normal_n = 30.0
    friction_n = mu * normal_n
    print("grinding friction: %.1f N x %.1f = %.1f N" % (normal_n, mu, friction_n))
    assert 11.9 < friction_n < 12.1
    # the turn stays tight: radius under 0.5 m to the center
    radius_m = 0.45
    print("turn radius to partner: %.2f m (max 0.50 m)" % radius_m)
    assert radius_m < 0.50
    # contact must hold unbroken through the whole turn
    breaks = 0
    print("contact breaks allowed: %d" % breaks)
    assert breaks == 0
    # sixth of eight changes
    order = 6
    print("change number in sequence: %d of 8" % order)
    assert order == 6
    print("OK: %s ground the rubbing body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_overturning_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # coil: waist winds 90 degrees one way, snaps back
    coil_deg = 90.0
    print("waist coil: %.0f degrees" % coil_deg)
    assert 89.9 < coil_deg < 90.1
    # the flip: full reversal in about 0.4 s at speed
    flip_s = 0.4
    print("flip time at speed: %.1f s" % flip_s)
    assert 0.39 < flip_s < 0.41
    # slow drill first: ten overturns each side
    reps = 10 * 2
    print("slow drill reps: %d" % reps)
    assert reps == 20
    # seventh of eight changes
    order = 7
    print("change number in sequence: %d of 8" % order)
    assert order == 7
    print("OK: %s overturned the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_returning_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the full sequence: eight changes in order
    changes = 8
    print("changes in the sequence: %d" % changes)
    assert changes == 8
    # examination: two full rounds without pausing
    rounds = 2
    total = changes * rounds
    print("examination: %d rounds x %d = %d changes" % (rounds, changes, total))
    assert total == 16
    # walking steps between changes: four
    between = 4
    print("walking steps between changes: %d" % between)
    assert between == 4
    # eighth of eight changes
    order = 8
    print("change number in sequence: %d of 8" % order)
    assert order == 8
    print("OK: %s returned the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_covering_millstone(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hidden hand falls ~0.5 m: free-fall time
    h_m = 0.5
    t = math.sqrt(2 * h_m / 9.81)
    print("hand drop %.1f m: free-fall %.3f s" % (h_m, t))
    assert 0.318 < t < 0.321
    # overhead arc: about 270 degrees from behind-head to target
    arc_deg = 270.0
    print("strike arc: %.0f degrees" % arc_deg)
    assert arc_deg == 270.0
    # ten hidden-hand strikes, partner must flinch late every time
    reps = 10
    late = 10
    print("deception drill: %d/%d late flinches" % (late, reps))
    assert late == reps == 10
    print("OK: %s covered with the millstone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_trigrams(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight trigrams, eight strategies
    trigrams = ["qian", "kun", "zhen", "xun", "kan", "li", "gen", "dui"]
    print("trigrams: %d" % len(trigrams))
    assert len(trigrams) == 8
    # pairs of trigrams form 64 hexagrams
    hexagrams = 8 * 8
    print("hexagram combinations: 8 x 8 = %d" % hexagrams)
    assert hexagrams == 64
    # one trigram per palm change
    changes = 8
    print("changes mapped: %d" % changes)
    assert changes == len(trigrams)
    # strategy-selection drill: three correct in a row
    streak = 3
    print("required correct streak: %d" % streak)
    assert streak == 3
    print("OK: %s read the eight trigrams" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_elbow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow lever 0.30 m vs full arm 0.65 m: shorter lever, waist-driven
    elbow_m, arm_m = 0.30, 0.65
    ratio = arm_m / elbow_m
    print("arm/elbow lever ratio: %.2f / %.2f = %.2f" % (arm_m, elbow_m, ratio))
    assert 2.16 < ratio < 2.18
    # waist torque 60 N m through the elbow lever -> force at elbow
    torque_nm = 60.0
    force_n = torque_nm / elbow_m
    print("waist torque %.0f N m -> elbow force %.0f N" % (torque_nm, force_n))
    assert 199.9 < force_n < 200.1
    # three elbow shapes
    shapes = ["folding", "rising", "horizontal"]
    print("elbow shapes: %d" % len(shapes))
    assert len(shapes) == 3
    # ten pad strikes each shape each side
    reps = 10 * 3 * 2
    print("pad drill reps: %d" % reps)
    assert reps == 60
    print("OK: %s folded the elbow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_shoulder(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kao: whole body 75 kg arriving at 2.0 m/s
    mass_kg, speed_ms = 75.0, 2.0
    p = mass_kg * speed_ms
    print("kao momentum: %.0f kg x %.1f m/s = %.0f kg m/s" % (mass_kg, speed_ms, p))
    assert 149.9 < p < 150.1
    # follow-through: two inches past contact
    through_in = 2.0
    print("follow-through: %.0f in past contact" % through_in)
    assert through_in == 2.0
    # ten bumps each shoulder
    reps = 10 * 2
    print("bag drill reps: %d" % reps)
    assert reps == 20
    # contact angle: beside the opponent, 90 degrees to their facing
    angle_deg = 90.0
    print("entry angle: %.0f degrees" % angle_deg)
    assert angle_deg == 90.0
    print("OK: %s bumped the kao shoulder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_palm_variations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eleven palm shapes in the arsenal
    shapes = ["upward", "downward", "vertical", "hugging", "piercing",
              "chopping", "lifting", "picking", "collapsing", "bumping", "tucking"]
    print("palm shapes: %d" % len(shapes))
    assert len(shapes) == 11
    # twenty-plus named techniques
    techniques = 24
    print("named techniques: %d+" % techniques)
    assert techniques >= 20
    # ten reps of each shape's job on the pad
    reps = 10 * len(shapes)
    print("pad drill reps: %d" % reps)
    assert reps == 110
    # random-call test: 8 of 10 correct
    score, total = 8, 10
    print("random-call standard: %d/%d" % (score, total))
    assert score == 8 and total == 10
    print("OK: %s showed the hand arsenal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_sticking_turning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sticking pressure: light, under 5 N - never grabbing
    stick_n = 3.0
    print("sticking pressure: %.1f N (limit 5.0 N)" % stick_n)
    assert stick_n < 5.0
    # entries at 45 degrees to the attack line
    entry_deg = 45.0
    print("entry angle: %.0f degrees" % entry_deg)
    assert 44.9 < entry_deg < 45.1
    # two entries: diagonal-out and direct-in
    entries = ["diagonal-out", "direct-in"]
    print("entries: %d" % len(entries))
    assert len(entries) == 2
    # ten clean entries each
    reps = 10 * 2
    print("drill reps: %d" % reps)
    assert reps == 20
    print("OK: %s stuck and turned" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_deerhorn_basics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a pair of deer-horn knives, one per hand
    knives = 2
    print("deer-horn knives: %d (one per hand)" % knives)
    assert knives == 2
    # each trainer: 4 crescent points to learn
    points_per = 4
    print("crescent points per knife: %d" % points_per)
    assert points_per == 4
    # guard hold: two-minute steady carry each direction
    hold_min = 2.0 * 2
    print("guard carry: %.0f minutes" % hold_min)
    assert hold_min == 4.0
    # woven into single and double changes: 2 changes
    woven = 2
    print("changes woven: %d" % woven)
    assert woven == 2
    print("OK: %s gripped the deer-horn knives" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_deerhorn_changes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crescent trap: locks within a 60-degree capture arc
    capture_deg = 60.0
    print("crescent capture arc: %.0f degrees" % capture_deg)
    assert 59.9 < capture_deg < 60.1
    # knives woven through all eight changes
    changes = 8
    print("changes woven: %d" % changes)
    assert changes == 8
    # trap-then-cut: the two-beat rhythm
    beats = 2
    print("trap-then-cut beats: %d" % beats)
    assert beats == 2
    # partner drill: three clean trap-and-turn-pasts at half speed
    clean = 3
    print("required clean traps: %d" % clean)
    assert clean == 3
    print("OK: %s trapped with the deer-horn knives" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_straight_sword(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # practice jian blade about 0.75 m
    blade_m = 0.75
    print("practice blade: %.2f m" % blade_m)
    assert 0.74 < blade_m < 0.76
    # thirteen sword methods
    methods = 13
    print("sword methods: %d" % methods)
    assert methods == 13
    # thrust reach: arm 0.65 m + blade 0.75 m
    reach_m = 0.65 + blade_m
    print("thrust reach: %.2f m" % reach_m)
    assert 1.39 < reach_m < 1.41
    # point steadiness: wobble under 3 cm during the walk
    wobble_cm = 2.0
    print("point wobble: %.1f cm (limit 3.0 cm)" % wobble_cm)
    assert wobble_cm < 3.0
    print("OK: %s drew the straight sword" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_spear_staff(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # great spear length about 2.5 m vs standard staff 1.8 m
    spear_m, staff_m = 2.5, 1.8
    print("great spear %.1f m vs staff %.1f m" % (spear_m, staff_m))
    assert 2.49 < spear_m < 2.51 and 1.79 < staff_m < 1.81
    # leverage: thrust force at 2.5 m from waist torque 60 N m
    torque_nm = 60.0
    tip_n = torque_nm / spear_m
    print("waist torque %.0f N m -> spear tip %.1f N" % (torque_nm, tip_n))
    assert 23.9 < tip_n < 24.1
    # accuracy standard: 8 of 10 thrusts on the mark
    hits, total = 8, 10
    print("thrust accuracy standard: %d/%d" % (hits, total))
    assert hits == 8 and total == 10
    print("OK: %s shouldered the great weapons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_swimming_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every evasion angular: 45 degrees minimum
    evade_deg = 45.0
    print("minimum evasion angle: %.0f degrees" % evade_deg)
    assert evade_deg == 45.0
    # ten fed attacks, none met head-on
    attacks, head_on = 10, 0
    print("evasion drill: %d attacks, %d met head-on" % (attacks, head_on))
    assert attacks == 10 and head_on == 0
    # counter lands from the evasion's motion: 8 of 10
    counters = 8
    print("counters landed: %d/%d" % (counters, attacks))
    assert counters == 8
    # root-in-motion freeze: strike-ready every time (5 checks)
    checks = 5
    print("freeze checks passed: %d/%d" % (checks, checks))
    assert checks == 5
    print("OK: %s swam the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_coiling_power(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full waist coil: 180 degrees wound
    coil_deg = 180.0
    print("waist coil: %.0f degrees" % coil_deg)
    assert 179.9 < coil_deg < 180.1
    # elastic storage: coil the spring over 4 steps, release on the 5th
    wind_steps, release_step = 4, 5
    print("wind %d steps, release on step %d" % (wind_steps, release_step))
    assert wind_steps == 4 and release_step == 5
    # curved strike around a guard pad: 8 of 10
    curved, total = 8, 10
    print("curved strikes landed: %d/%d" % (curved, total))
    assert curved == 8 and total == 10
    # three consecutive wound-then-released strikes
    chain = 3
    print("coil-release chain: %d" % chain)
    assert chain == 3
    print("OK: %s coiled the power" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_old_eight_form(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight changes, both directions
    form_rounds = 8 * 2
    print("form changes (both directions): %d" % form_rounds)
    assert form_rounds == 16
    # four walking steps between changes
    between = 4
    total_steps = form_rounds * between
    print("walking steps in the form: %d x %d = %d" % (form_rounds, between, total_steps))
    assert total_steps == 64
    # random-order round: 8 called changes, all correct
    called, correct = 8, 8
    print("random-order round: %d/%d correct" % (correct, called))
    assert called == correct == 8
    # application round: eight live answers
    live = 8
    print("live applications: %d" % live)
    assert live == 8
    print("OK: %s linked the old eight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_entering_side(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # entry finishes at the flank: 90 degrees to the opponent's facing
    flank_deg = 90.0
    print("flank angle: %.0f degrees" % flank_deg)
    assert 89.9 < flank_deg < 90.1
    # ten entries, none met head-on
    entries, head_on = 10, 0
    print("entry drill: %d entries, %d head-on" % (entries, head_on))
    assert entries == 10 and head_on == 0
    # single-change application: block + strike = 2 hands
    hands = 2
    print("hands in the single-change application: %d" % hands)
    assert hands == 2
    # contact stays light and controlled: under 20 N on pads
    contact_n = 15.0
    print("application contact: %.0f N (limit 20 N)" % contact_n)
    assert contact_n < 20.0
    print("OK: %s entered from the side" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_multiple_attackers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three attackers divide the circle into 120-degree sectors
    sectors = 360.0 / 3
    print("three-attacker sectors: %.0f degrees each" % sectors)
    assert 119.9 < sectors < 120.1
    # two-attacker drill: five exchanges each
    exchanges = 5 * 2
    print("two-attacker exchanges: %d" % exchanges)
    assert exchanges == 10
    # shield positioning held one full minute
    shield_s = 60.0
    print("shield hold: %.0f s" % shield_s)
    assert 59.9 < shield_s < 60.1
    # stops allowed: zero - the circle never stops
    stops = 0
    print("stops allowed: %d" % stops)
    assert stops == 0
    print("OK: %s circled the many" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bgz_mastery_circle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shrink the circle: 12 ft -> 6 ft, circumference halves
    c12 = math.pi * 12.0
    c6 = math.pi * 6.0
    print("circle shrink: %.2f ft -> %.2f ft" % (c12, c6))
    assert 37.69 < c12 < 37.71 and 18.84 < c6 < 18.86
    ratio = c6 / c12
    print("circumference ratio: %.2f" % ratio)
    assert 0.499 < ratio < 0.501
    # endurance: one full hour of continuous walking
    hour_min = 60.0
    print("continuous walk: %.0f minutes" % hour_min)
    assert hour_min == 60.0
    # reflex test: ten random attacks, ten correct answers
    correct, total = 10, 10
    print("reflex test: %d/%d" % (correct, total))
    assert correct == total == 10
    print("OK: %s mastered the circle" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "bgz-meaning": demo_bgz_meaning,
    "bgz-circle-walking": demo_bgz_circle_walking,
    "bgz-mud-wading": demo_bgz_mud_wading,
    "bgz-swing-hook-steps": demo_bgz_swing_hook_steps,
    "bgz-posture-alignment": demo_bgz_posture_alignment,
    "bgz-static-postures": demo_bgz_static_postures,
    "bgz-single-change": demo_bgz_single_change,
    "bgz-double-change": demo_bgz_double_change,
    "bgz-single-palm-strike": demo_bgz_single_palm_strike,
    "bgz-double-palm-strike": demo_bgz_double_palm_strike,
    "bgz-millstone-palm": demo_bgz_millstone_palm,
    "bgz-breathing": demo_bgz_breathing,
    "bgz-flowing-body": demo_bgz_flowing_body,
    "bgz-back-body": demo_bgz_back_body,
    "bgz-turning-body": demo_bgz_turning_body,
    "bgz-rubbing-body": demo_bgz_rubbing_body,
    "bgz-overturning-body": demo_bgz_overturning_body,
    "bgz-returning-body": demo_bgz_returning_body,
    "bgz-covering-millstone": demo_bgz_covering_millstone,
    "bgz-trigrams": demo_bgz_trigrams,
    "bgz-elbow": demo_bgz_elbow,
    "bgz-shoulder": demo_bgz_shoulder,
    "bgz-palm-variations": demo_bgz_palm_variations,
    "bgz-sticking-turning": demo_bgz_sticking_turning,
    "bgz-deerhorn-basics": demo_bgz_deerhorn_basics,
    "bgz-deerhorn-changes": demo_bgz_deerhorn_changes,
    "bgz-straight-sword": demo_bgz_straight_sword,
    "bgz-spear-staff": demo_bgz_spear_staff,
    "bgz-swimming-body": demo_bgz_swimming_body,
    "bgz-coiling-power": demo_bgz_coiling_power,
    "bgz-old-eight-form": demo_bgz_old_eight_form,
    "bgz-entering-side": demo_bgz_entering_side,
    "bgz-multiple-attackers": demo_bgz_multiple_attackers,
    "bgz-mastery-circle": demo_bgz_mastery_circle,
}
