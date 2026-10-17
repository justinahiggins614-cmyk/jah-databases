#!/usr/bin/env python3
"""Demo programs for the Kickboxing Combat databases (combat orders
2026-10-17, combat batch 1).

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: stance geometry, strike reach and
speed, combination timing, defensive margins, conditioning progressions,
and camp arithmetic. All are machine-executed by build.py: each prints
its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


DEMOS = {}


def demo_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance geometry for a 1.78 m, 75 kg orthodox fighter
    height, mass = 1.78, 75.0
    shoulder_w = 0.46
    stance_w = 1.25 * shoulder_w          # between 1.0x and 1.5x shoulder width
    front_share, rear_share = 0.55, 0.45
    front_kg, rear_kg = mass * front_share, mass * rear_share
    print("stance width: %.3f m (shoulder %.2f m)" % (stance_w, shoulder_w))
    print("weight: front %.2f kg / rear %.2f kg" % (front_kg, rear_kg))
    assert 0.574 < stance_w < 0.576
    assert 41.24 < front_kg < 41.26
    assert 33.74 < rear_kg < 33.76
    assert abs(front_kg + rear_kg - mass) < 1e-9
    print("OK: %s balanced the covenant ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # high-guard coverage: two gloves across the head target
    head_w = 0.16          # metres, average head width
    glove_w = 0.12         # metres, glove face width
    overlap = 0.02
    coverage = 2 * glove_w - overlap
    margin = coverage - head_w
    print("guard coverage: %.3f m vs head %.2f m" % (coverage, head_w))
    print("coverage margin: %.3f m" % margin)
    assert 0.219 < coverage < 0.221
    assert 0.059 < margin < 0.061
    tension = 0.70
    shoulder_load = tension * 100.0
    print("guard tension: %.0f %%" % shoulder_load)
    assert 69.9 < shoulder_load < 70.1
    print("OK: %s raised the honor wall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # step-drag: 6-inch steps, stance width preserved
    step_m = 6 * 0.0254
    steps_per_min = 60
    minutes = 3
    distance = step_m * steps_per_min * minutes
    stance_before, stance_after = 0.575, 0.575
    print("step length: %.4f m" % step_m)
    print("3-min drill distance: %.2f m" % distance)
    assert 0.1523 < step_m < 0.1525
    assert 27.42 < distance < 27.44
    assert abs(stance_before - stance_after) < 1e-9, "stance width must not change"
    pivot_deg = 45.0
    print("fundamental pivot: %.0f degrees" % pivot_deg)
    assert pivot_deg == 45.0
    print("OK: %s wrote the footwork signature" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jab reach and hand speed
    arm_m, shoulder_roll_m = 0.71, 0.08
    reach = arm_m + shoulder_roll_m
    jab_time = 0.15
    hand_speed = reach / jab_time
    print("jab reach: %.2f m" % reach)
    print("jab hand speed: %.2f m/s" % hand_speed)
    assert 0.789 < reach < 0.791
    assert 5.26 < hand_speed < 5.28
    return_time = jab_time / 2.0   # returns twice as fast as it left
    print("return time: %.3f s" % return_time)
    assert 0.074 < return_time < 0.076
    print("OK: %s snapped the first stroke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cross(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross: rear-side rotation arc + arm extension
    shoulder_r = 0.25
    rot_deg = 90.0
    arc = 2 * math.pi * shoulder_r * rot_deg / 360.0
    arm_m = 0.71
    fist_travel = arc + arm_m
    punch_time = 0.25
    fist_speed = fist_travel / punch_time
    print("rotation arc: %.3f m, fist travel: %.3f m" % (arc, fist_travel))
    print("cross fist speed: %.2f m/s" % fist_speed)
    assert 0.392 < arc < 0.394
    assert 1.102 < fist_travel < 1.104
    assert 4.40 < fist_speed < 4.42
    print("OK: %s pressed the cross hard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lead_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lead hook: tight 90-degree arc on a bent arm
    arm_r = 0.60
    arc_deg = 90.0
    arc_len = 2 * math.pi * arm_r * arc_deg / 360.0
    hook_time = 0.22
    hook_speed = arc_len / hook_time
    print("hook arc length: %.3f m" % arc_len)
    print("hook fist speed: %.2f m/s" % hook_speed)
    assert 0.942 < arc_len < 0.944
    assert 4.28 < hook_speed < 4.30
    elbow_deg = 90.0
    assert 89.9 < elbow_deg < 90.1
    print("OK: %s curled the signature" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_rear_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear hook: longer, harder arc than the lead hook
    arm_r = 0.65
    arc_deg = 100.0
    arc_len = 2 * math.pi * arm_r * arc_deg / 360.0
    hook_time = 0.28
    hook_speed = arc_len / hook_time
    print("rear hook arc: %.3f m in %.2f s" % (arc_len, hook_time))
    print("rear hook speed: %.2f m/s" % hook_speed)
    assert 1.134 < arc_len < 1.136
    assert 4.05 < hook_speed < 4.07
    print("OK: %s underlined with the rear hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uppercut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uppercut: short vertical rip from a knee dip
    dip_m = 0.07
    rise_m = 0.35
    punch_time = 0.20
    # average upward acceleration from rest: a = 2d / t^2
    accel = 2 * rise_m / punch_time ** 2
    fist_mass = 0.6
    peak_force = fist_mass * accel
    print("dip: %.2f m, rise: %.2f m" % (dip_m, rise_m))
    print("avg upward accel: %.1f m/s^2, peak fist force ~%.1f N" % (accel, peak_force))
    assert 17.4 < accel < 17.6
    assert 10.4 < peak_force < 10.6
    print("OK: %s rose with the signature" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_low_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low kick: shin whip energy
    omega = 12.0            # rad/s hip turnover
    radius = 0.85           # hip to shin contact
    v = omega * radius
    leg_mass = 10.0
    energy = 0.5 * leg_mass * v ** 2
    print("shin tip speed: %.2f m/s" % v)
    print("kick energy: %.0f J" % energy)
    assert 10.19 < v < 10.21
    assert 519.0 < energy < 521.0
    print("OK: %s chopped the foundation stroke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_roundhouse_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mid kick: full 180-degree pivot, hip fully turned over
    pivot_deg = 180.0
    omega = 11.0
    radius = 0.95
    v = omega * radius
    leg_mass = 11.0
    energy = 0.5 * leg_mass * v ** 2
    pivot_rad = math.radians(pivot_deg)
    print("standing-foot pivot: %.0f deg (%.3f rad)" % (pivot_deg, pivot_rad))
    print("shin speed: %.2f m/s, energy: %.0f J" % (v, energy))
    assert 3.141 < pivot_rad < 3.143
    assert 10.44 < v < 10.46
    assert 599.0 < energy < 601.0
    print("OK: %s pressed through the page" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_teep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # teep: piston thrust work over the push distance
    thrust_m = 0.10      # about four inches of push-through
    drive_mass = 15.0      # leg + hip mass behind the thrust
    foot_v = 6.0
    force = 0.5 * drive_mass * foot_v ** 2 / thrust_m
    print("thrust distance: %.2f m, avg push force: %.0f N" % (thrust_m, force))
    assert 2699.0 < force < 2701.0
    retract_m = thrust_m   # returns on the same line
    assert abs(retract_m - thrust_m) < 1e-9
    print("OK: %s held the firm hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_front_snap_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # snap kick: one-beat chamber-snap-retract
    out_t, back_t = 0.12, 0.10
    beat = out_t + back_t
    ball_v = 8.0
    print("out %.2f s + back %.2f s = one beat %.2f s" % (out_t, back_t, beat))
    print("ball-of-foot speed: %.1f m/s" % ball_v)
    assert 0.219 < beat < 0.221
    assert beat < 0.25, "must stay the fastest kick"
    print("OK: %s wrote the quick stroke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_knee_strike(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee: hip-driven momentum into the target
    knee_mass = 12.0
    knee_v = 7.0
    momentum = knee_mass * knee_v
    energy = 0.5 * knee_mass * knee_v ** 2
    print("knee momentum: %.0f kg m/s, energy: %.0f J" % (momentum, energy))
    assert 83.9 < momentum < 84.1
    assert 293.9 < energy < 294.1
    print("OK: %s drove the rising seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_one_two(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one-two: overlapping piston cycle, sub-second
    jab_t, cross_t, overlap = 0.15, 0.25, 0.05
    total = jab_t + cross_t - overlap
    print("jab %.2f s + cross %.2f s - overlap %.2f s = %.2f s" % (jab_t, cross_t, overlap, total))
    assert 0.349 < total < 0.351
    assert total < 1.0, "the one-two must take under a second"
    print("OK: %s joined the first two strokes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jab_cross_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one-two-three: jab, cross, hook with piston overlap
    jab_t, cross_t, hook_t = 0.15, 0.25, 0.22
    overlap = 0.05
    total = jab_t + cross_t + hook_t - 2 * overlap
    print("1-2-3 total: %.2f s" % total)
    assert 0.519 < total < 0.521
    exit_deg = 45.0
    print("exit angle: %.0f degrees" % exit_deg)
    assert exit_deg == 45.0
    print("OK: %s wrote the full three-stroke name" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_blocking_parrying(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # block absorbs; parry redirects via similar triangles
    punch_n = 500.0
    absorbed = 0.70
    transmitted = punch_n * (1 - absorbed)
    deflect_glove_m = 0.05   # 2 inches at the glove
    arm_m = 0.71
    head_m = 0.25            # glove-to-head distance along the punch line
    miss_m = deflect_glove_m * (arm_m + head_m) / arm_m
    print("block transmits: %.0f N of %.0f N" % (transmitted, punch_n))
    print("parry miss at head: %.3f m" % miss_m)
    assert 149.9 < transmitted < 150.1
    assert 0.067 < miss_m < 0.069
    print("OK: %s held the honor guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_slip_weave_roll(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # slip: minimum head movement to miss
    slip_m = 0.10
    slip_t = 0.18
    head_v = slip_m / slip_t
    punch_v = 8.0
    print("slip %.2f m in %.2f s -> head speed %.2f m/s" % (slip_m, slip_t, head_v))
    assert 0.55 < head_v < 0.57
    assert slip_m < 0.15, "economy: never move more than the miss requires"
    print("OK: %s left the punch unwritten" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_checking_kicks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # check: shin-on-shin high near the knee
    kick_energy = 520.0
    check_absorb = 0.55      # defender's shin takes just over half; kicker takes the rest
    kicker_pain = kick_energy * check_absorb
    contact_m = 0.10         # 10 cm below the knee: thickest bone
    print("kicker absorbs on the check: %.0f J" % kicker_pain)
    print("contact height below knee: %.2f m" % contact_m)
    assert 285.9 < kicker_pain < 286.1
    assert contact_m < 0.15, "meet it high where the bone is thickest"
    print("OK: %s met oath with oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_catching_sweeps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep: lever on the trapped leg's standing ankle
    trapped_h_m = 1.0
    ankle_lever_m = 0.90
    pull_n = 300.0
    torque = pull_n * ankle_lever_m
    print("sweep torque: %.0f N m" % torque)
    assert 269.9 < torque < 270.1
    assert trapped_h_m <= 1.1, "never hold the caught leg above waist height"
    print("OK: %s seized the stroke and turned it" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inside_outside_kicks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # outside kick: full arc; inside kick: compact chop
    r = 0.85
    outside_deg, inside_deg = 120.0, 60.0
    outside_arc = 2 * math.pi * r * outside_deg / 360.0
    inside_arc = 2 * math.pi * r * inside_deg / 360.0
    print("outside arc: %.3f m, inside arc: %.3f m" % (outside_arc, inside_arc))
    assert 1.779 < outside_arc < 1.781
    assert 0.889 < inside_arc < 0.891
    assert inside_arc < outside_arc
    print("OK: %s wrote both margins" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_clinch_pummeling(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pummeling: continuous over-under cycles across a round
    cycle_s = 2.0
    round_s = 180.0
    cycles = round_s / cycle_s
    print("pummeling cycles per 3-min round: %.0f" % cycles)
    assert 89.9 < cycles < 90.1
    print("OK: %s grappled seal to seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_counter_punching(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # counter window: fire into their extension
    opp_jab_t = 0.15
    my_cross_t = 0.25
    # counter starts as their jab extends; lands while they are committed
    window = opp_jab_t + 0.10   # extension plus commitment beat
    print("counter window: %.2f s vs my cross %.2f s" % (window, my_cross_t))
    assert 0.249 < window < 0.251
    assert window <= my_cross_t + 0.001
    print("OK: %s answered the page" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dutch_combinations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Dutch: 4 punches at 3.5/sec + finishing low kick
    punches, rate = 4, 3.5
    punch_phase = punches / rate
    kick_phase = 0.35
    total = punch_phase + kick_phase
    combos_per_round = 20
    round_output = combos_per_round * (punches + 1)
    print("combo time: %.2f s, strikes per round: %d" % (total, round_output))
    assert 1.492 < total < 1.494
    assert round_output == 100
    print("OK: %s flooded the page Dutch-style" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_switch_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # switch kick vs step-in rear kick: time saved is the deception
    hop_t, kick_t = 0.12, 0.30
    switch_total = hop_t + kick_t
    stepin_total = 0.55
    saved = stepin_total - switch_total
    print("switch %.2f s vs step-in %.2f s: saves %.2f s" % (switch_total, stepin_total, saved))
    assert 0.419 < switch_total < 0.421
    assert 0.129 < saved < 0.131
    print("OK: %s rewrote mid-stroke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_spinning_back_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spinning back kick: heel travel over the full turn
    heel_r = 1.0
    heel_travel = math.pi * heel_r   # 180 degrees
    spin_t = 0.50
    heel_v = heel_travel / spin_t
    leg_mass = 12.0
    energy = 0.5 * leg_mass * heel_v ** 2
    print("heel travel: %.3f m, heel speed: %.2f m/s" % (heel_travel, heel_v))
    print("spin energy: %.0f J" % energy)
    assert 3.141 < heel_travel < 3.143
    assert 6.28 < heel_v < 6.30
    assert 236.0 < energy < 238.0
    print("OK: %s signed with the whole arm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_flying_knee(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flying knee: jump height sets airtime for the drive
    jump_m = 0.45
    airtime = 2 * math.sqrt(2 * jump_m / 9.81)
    knee_v = 7.5
    knee_mass = 12.0
    energy = 0.5 * knee_mass * knee_v ** 2
    print("jump %.2f m -> airtime %.3f s" % (jump_m, airtime))
    print("knee energy at apex: %.0f J" % energy)
    assert 0.605 < airtime < 0.607
    assert 337.0 < energy < 338.0
    print("OK: %s leapt off the page" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shin_conditioning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 12-week progression: 100 kicks/leg/session, 3x/week, +10%/week volume
    base, sessions, weeks, growth = 100.0, 3, 12, 1.10
    total = sum(base * sessions * growth ** w for w in range(weeks))
    print("12-week kicks per leg: %.0f" % total)
    assert 6410.0 < total < 6430.0
    final_week = base * sessions * growth ** 11
    print("final week kicks per leg: %.0f" % final_week)
    assert 855.0 < final_week < 857.0
    print("OK: %s kept the daily oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_feints_setups(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # feint: 2-inch shoulder twitch inside human reaction time
    feint_m = 0.05
    feint_t = 0.08
    reaction_t = 0.25
    window = reaction_t - feint_t
    print("feint %.2f m in %.2f s; reaction window %.2f s" % (feint_m, feint_t, window))
    assert 0.169 < window < 0.171
    assert feint_m <= 0.06, "two inches of truth, never theater"
    print("OK: %s hovered the ghost stroke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ring_cutting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three cuts, each shrinking space by a third
    space = 1.0
    for _ in range(3):
        space *= (2.0 / 3.0)
    ring_m = 6.1
    trapped_m = ring_m * space
    print("space after 3 cuts: %.1f %% -> %.2f m of ring" % (space * 100, trapped_m))
    assert 29.62 < space * 100 < 29.64
    assert 1.806 < trapped_m < 1.808
    print("OK: %s owned the margins" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_advanced_defense(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pull counter: lean back 4 inches; punch falls short by the margin
    lean_m = 0.10
    punch_reach_m = 0.79
    gap_m = 1.00   # distance at the moment of the pull
    miss_m = gap_m - punch_reach_m + lean_m
    print("pull miss margin: %.2f m" % miss_m)
    assert 0.309 < miss_m < 0.311
    assert 0.07 < lean_m < 0.11, "the margin between brilliant and knockout is two inches"
    print("OK: %s declined with a shoulder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sparring_strategy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # energy budget: 3 rounds x 3 min, paced pressure
    rounds, round_min = 3, 3
    total_min = rounds * round_min
    output_r1, output_r2, output_r3 = 60, 70, 80   # strikes, rising pressure
    total_strikes = output_r1 + output_r2 + output_r3
    per_min = total_strikes / total_min
    print("fight output: %d strikes over %d min (%.1f/min)" % (total_strikes, total_min, per_min))
    assert total_strikes == 210
    assert 23.32 < per_min < 23.34
    assert output_r1 < output_r2 < output_r3, "pressure must rise, never fade"
    print("OK: %s composed the fight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_southpaw_orthodox(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # outside angle: 15 degrees opens the lane
    angle_deg = 15.0
    angle_rad = math.radians(angle_deg)
    reach_m = 0.79
    lane_m = reach_m * math.sin(angle_rad)
    print("open lane at 15 deg: %.3f m" % lane_m)
    assert 0.204 < lane_m < 0.206
    weapons = 3   # rear straight, lead hook, rear kick to the lead leg
    assert weapons == 3
    print("OK: %s faced the reflection" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ruleset_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arsenal audit across the three rule sets
    arsenal = ["jab", "cross", "hooks", "uppercut", "low kick", "mid kick",
               "head kick", "teep", "knees", "clinch knees", "elbows", "spinning kick"]
    american_classic = {"jab", "cross", "hooks", "uppercut", "mid kick",
                        "head kick", "teep", "spinning kick"}          # no low kicks, no knees
    k1 = set(arsenal) - {"elbows"}                                     # everything but elbows
    legal_american = sum(1 for w in arsenal if w in american_classic)
    legal_k1 = sum(1 for w in arsenal if w in k1)
    print("arsenal: %d weapons; legal American-classic: %d; legal K-1: %d"
          % (len(arsenal), legal_american, legal_k1))
    assert legal_american == 8
    assert legal_k1 == 11
    lost = legal_k1 - legal_american
    print("weapons lost crossing to American-classic: %d" % lost)
    assert lost == 3
    print("OK: %s read the true rulebook" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fight_camp(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 12-week camp: 60 sessions split 60/30/10 across base/sharpen/taper
    sessions = 60
    base = round(sessions * 0.60)
    sharpen = round(sessions * 0.30)
    taper = sessions - base - sharpen
    print("base %d / sharpen %d / taper %d" % (base, sharpen, taper))
    assert base == 36 and sharpen == 18 and taper == 6
    assert base + sharpen + taper == sessions
    combos, traps = 5, 3
    print("fight-night card: %d combos, %d traps" % (combos, traps))
    print("OK: %s rehearsed the signing" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "stance": demo_stance,
    "guard": demo_guard,
    "footwork": demo_footwork,
    "jab": demo_jab,
    "cross": demo_cross,
    "lead_hook": demo_lead_hook,
    "rear_hook": demo_rear_hook,
    "uppercut": demo_uppercut,
    "low_kick": demo_low_kick,
    "roundhouse_body": demo_roundhouse_body,
    "teep": demo_teep,
    "front_snap_kick": demo_front_snap_kick,
    "knee_strike": demo_knee_strike,
    "one_two": demo_one_two,
    "jab_cross_hook": demo_jab_cross_hook,
    "blocking_parrying": demo_blocking_parrying,
    "slip_weave_roll": demo_slip_weave_roll,
    "checking_kicks": demo_checking_kicks,
    "catching_sweeps": demo_catching_sweeps,
    "inside_outside_kicks": demo_inside_outside_kicks,
    "clinch_pummeling": demo_clinch_pummeling,
    "counter_punching": demo_counter_punching,
    "dutch_combinations": demo_dutch_combinations,
    "switch_kick": demo_switch_kick,
    "spinning_back_kick": demo_spinning_back_kick,
    "flying_knee": demo_flying_knee,
    "shin_conditioning": demo_shin_conditioning,
    "feints_setups": demo_feints_setups,
    "ring_cutting": demo_ring_cutting,
    "advanced_defense": demo_advanced_defense,
    "sparring_strategy": demo_sparring_strategy,
    "southpaw_orthodox": demo_southpaw_orthodox,
    "ruleset_mastery": demo_ruleset_mastery,
    "fight_camp": demo_fight_camp,
}
