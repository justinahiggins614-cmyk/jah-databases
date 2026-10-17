#!/usr/bin/env python3
"""Demo programs for the Muay Thai Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
computation for its record (training calculators, drill timers, strike
physics, camp volume). All are machine-executed by build.py before commit:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_mt_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance geometry for a 1.75 m, 70 kg fighter
    height, mass = 1.75, 70.0
    stance_len = 0.35 * height          # shoulder-width-plus stance
    per_foot = mass / 2.0               # near-even weight split
    force_n = per_foot * 9.81
    print("stance length: %.4f m" % stance_len)
    print("weight per foot: %.1f kg (%.2f N)" % (per_foot, force_n))
    assert 0.61 < stance_len < 0.62
    assert 343.3 < force_n < 343.4
    print("rule: low center of gravity between the feet - the stance is the first technique")
    print("OK: %s holds the base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crossing a 6.1 m ring in gliding steps
    ring, step, step_time = 6.1, 0.25, 0.4
    steps = int(math.ceil(ring / step))
    total = steps * step_time
    print("ring width: %.1f m, step: %.2f m" % (ring, step))
    print("steps to cross: %d, time: %.1f s" % (steps, total))
    assert steps == 25
    assert 9.9 < total < 10.1
    print("rule: lead foot leads forward, rear foot leads back - the stance survives every step")
    print("OK: %s crosses the ring" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # high-guard coverage vs face width
    glove_w, face_w = 0.12, 0.16
    coverage = 2 * glove_w
    margin = coverage - face_w
    print("glove coverage: %.2f m vs face %.2f m" % (coverage, face_w))
    print("coverage margin: %.3f m" % margin)
    assert 0.079 < margin < 0.081
    print("rule: fist-width gap to the face - the guard absorbs, it does not press")
    print("OK: %s seals the temple" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_jab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jab timing: travel time and sustainable rate
    dist, vel = 0.6, 8.0
    travel = dist / vel
    per_min = int(60.0 / 1.2)           # one jab every 1.2 s
    print("jab travel time: %.4f s" % travel)
    print("sustainable jabs per minute: %d" % per_min)
    assert 0.074 < travel < 0.076
    assert per_min == 50
    print("rule: speed and return beat power - the scout always comes home")
    print("OK: %s measures the range" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_parry_slip(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # slip geometry: head speed needed to clear a punch
    displacement, time = 0.15, 0.10
    head_speed = displacement / time
    punch_w = 0.12
    clearance = displacement - punch_w / 2.0
    print("head speed for slip: %.2f m/s" % head_speed)
    print("clearance past punch edge: %.3f m" % clearance)
    assert 1.49 < head_speed < 1.51
    assert 0.089 < clearance < 0.091
    print("rule: inches beat feet - the smallest move that works is the best move")
    print("OK: %s was never there" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_shadowboxing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shadowboxing session volume: 5 x (3 min work / 1 min rest)
    rounds, work, rest = 5, 3.0, 1.0
    work_min = rounds * work
    total_min = work_min + (rounds - 1) * rest
    strikes = work_min * 60.0 * 1.5     # 1.5 strikes per second
    print("work: %.0f min, session: %.0f min" % (work_min, total_min))
    print("strikes thrown: %.0f" % strikes)
    assert total_min == 19
    assert 1349.0 < strikes < 1351.0
    print("rule: full speed, full intent, zero impact - the mirror is the coach")
    print("OK: %s boxes the wind" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_cross(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross power: rotational energy of the hip/torso turn
    torso_m, radius, omega = 30.0, 0.15, 8.0
    inertia = torso_m * radius ** 2
    ke = 0.5 * inertia * omega ** 2
    print("torso inertia: %.4f kg m^2" % inertia)
    print("rotational energy: %.2f J" % ke)
    assert 21.5 < ke < 21.7
    print("rule: the cross is a hip punch that happens to use the hand")
    print("OK: %s answers the thunder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_roundhouse(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # roundhouse shin speed and energy
    omega, leg_len, leg_m = 10.0, 0.85, 4.0
    v = omega * leg_len
    ke = 0.5 * leg_m * v ** 2
    print("shin speed: %.2f m/s" % v)
    print("impact energy: %.1f J" % ke)
    assert 8.49 < v < 8.51
    assert 144.4 < ke < 144.6
    print("rule: the pivot is the kick - no pivot, no hips, no power")
    print("OK: %s swings the broadsword" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_teep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # teep impulse: stopping a rushing 80 kg opponent
    force, contact = 300.0, 0.25
    impulse = force * contact
    dv = impulse / 80.0
    print("teep impulse: %.1f N s" % impulse)
    print("opponent velocity change: %.4f m/s" % dv)
    assert 74.9 < impulse < 75.1
    assert 0.93 < dv < 0.95
    print("rule: the gatekeeper decides who enters - distance is decided by the teep")
    print("OK: %s holds the gate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_check(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # check timing window: kick travel vs shin lift
    kick_travel, lift = 0.15, 0.12
    margin = kick_travel - lift
    print("kick travel: %.2f s, check lift: %.2f s" % (kick_travel, lift))
    print("timing margin: %.3f s" % margin)
    assert 0.029 < margin < 0.031
    print("rule: read the hip - waiting for the shin means waiting too long")
    print("OK: %s raises the shield" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_heavy_bag(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weekly bag volume: 5 rounds/day, 5 days, 1.2 strikes/s
    per_round = int(1.2 * 180)
    weekly = per_round * 5 * 5
    print("strikes per 3-min round: %d" % per_round)
    print("weekly bag volume: %d strikes" % weekly)
    assert per_round == 216
    assert weekly == 5400
    print("rule: the bag is the truth-teller - only hip-driven strikes move it")
    print("OK: %s works the anvil" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_conditioning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shin conditioning progression: +10%/week for 6 weeks from 60 kicks
    start, weeks, rate = 60.0, 6, 0.10
    final = start * (1.0 + rate) ** (weeks - 1)
    total = sum(start * (1.0 + rate) ** w for w in range(weeks))
    print("week 1: %.0f kicks/session, week %d: %.2f" % (start, weeks, final))
    print("six-week total: %.0f kicks" % total)
    assert 96.6 < final < 96.7
    assert 462.0 < total < 464.0
    print("rule: months, not days - progressive overload with real technique")
    print("OK: %s tempers the steel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hook arc: tight 90-degree-elbow arc at 0.6 m radius
    theta, r, fist_v = 1.9, 0.6, 7.0
    arc = theta * r
    t = arc / fist_v
    print("hook arc length: %.3f m" % arc)
    print("fist travel time: %.4f s" % t)
    assert 1.13 < arc < 1.15
    assert 0.162 < t < 0.164
    print("rule: short and tight beats long and loopy - the arc is the weapon")
    print("OK: %s finds the seam" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_uppercut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uppercut launch: velocity to rise 0.35 m against gravity
    h = 0.35
    v = math.sqrt(2.0 * 9.81 * h)
    print("vertical rise: %.2f m" % h)
    print("launch velocity needed: %.4f m/s" % v)
    assert 2.62 < v < 2.63
    print("rule: the punch is the top of a squat - leg drive, not arm lift")
    print("OK: %s raises the geyser" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_elbow_horizontal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pocket entry: punch range vs elbow range
    punch_range, elbow_range = 0.75, 0.45
    step_in = punch_range - elbow_range
    print("punch range: %.2f m, elbow range: %.2f m" % (punch_range, elbow_range))
    print("step-in to elbow range: %.2f m" % step_in)
    assert 0.299 < step_in < 0.301
    print("rule: inches, not feet - the blade is drawn only at arm's length")
    print("OK: %s draws the dagger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_knee_straight(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight-knee impact force: 70 kg dropping 0.1 m, stopped in 0.05 m
    m, h, d = 70.0, 0.10, 0.05
    force = m * 9.81 * (1.0 + h / d)
    print("knee impact force: %.1f N" % force)
    assert 2059.0 < force < 2061.0
    print("rule: hips thrust up, arms pull down - the target is caught between")
    print("OK: %s swings the ram" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_elbow_updiag(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # diagonal elbow cut path: brow 0.20 m above the shoulder at 45 degrees
    rise, angle = 0.20, math.radians(45.0)
    path = rise / math.sin(angle)
    print("cut path length: %.4f m" % path)
    assert 0.282 < path < 0.284
    print("rule: the diagonal shears - rise from the earth, fall from the sky")
    print("OK: %s learns every angle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_knee_curved(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # curved knee arc: 1.2 rad sweep at 0.4 m radius
    theta, r, v = 1.2, 0.4, 5.0
    arc = theta * r
    t = arc / v
    print("curved knee arc: %.3f m" % arc)
    print("arc travel time: %.4f s" % t)
    assert 0.479 < arc < 0.481
    assert 0.095 < t < 0.097
    print("rule: when the gate holds, go around the wall - curve the knee")
    print("OK: %s swings the scythe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_clinch_entry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # clinch entry: steps to collapse from 1.2 m to 0.2 m at 0.5 m/step
    outside, inside, step = 1.2, 0.2, 0.5
    steps = int(math.ceil((outside - inside) / step))
    print("distance to collapse: %.1f m" % (outside - inside))
    print("entry steps: %d" % steps)
    assert steps == 2
    print("rule: never enter naked - a setup strike buys the step inside")
    print("OK: %s takes the neck" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_low_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low-kick target band on a 0.9 m leg
    leg, lo, hi = 0.9, 0.15, 0.35
    band, frac = hi - lo, (hi - lo) / leg
    print("target band: %.2f m (%.1f%% of the leg)" % (band, frac * 100.0))
    assert 0.22 < frac < 0.23
    print("rule: chop down through the thigh - the leg always falls in the end")
    print("OK: %s swings the axe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_switch_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # switch kick vs guard reset: 0.18 s switch + 0.22 s kick
    total = 0.18 + 0.22
    reset = 0.45
    advantage = reset - total
    print("switch plus kick: %.2f s, guard reset: %.2f s" % (total, reset))
    print("timing advantage: %.3f s" % advantage)
    assert 0.399 < total < 0.401
    assert 0.049 < advantage < 0.051
    print("rule: low and quick - a hopping switch is a telegraphed switch")
    print("OK: %s wears the mask" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_clinch_control(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pummeling cycles in a 30 s clinch exchange
    clinch_t, cycle = 30.0, 0.8
    cycles = int(clinch_t / cycle)
    print("clinch time: %.0f s, pummel cycle: %.1f s" % (clinch_t, cycle))
    print("inside-position battles: %d" % cycles)
    assert cycles == 37
    print("rule: inside position is rented by the second, never owned")
    print("OK: %s wrestles the storm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_catch_dump(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # catch window: kick travel 0.18 s vs hand clamp 0.12 s
    travel, clamp = 0.18, 0.12
    margin = travel - clamp
    print("kick travel: %.2f s, clamp time: %.2f s" % (travel, clamp))
    print("catch margin: %.3f s" % margin)
    assert 0.059 < margin < 0.061
    print("rule: the catch is a hug, not a reach - pin it to the body")
    print("OK: %s springs the trapdoor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_shell_counter(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shell coverage: 270 of 360 degrees sealed
    covered, total = 270.0, 360.0
    pct = covered / total * 100.0
    print("shell coverage: %.1f%%" % pct)
    assert 74.9 < pct < 75.1
    print("rule: the shell buys time, the counter spends it - watch through the guard")
    print("OK: %s answers through the slit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_spin_elbow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spinning elbow: full 360-degree turn in 0.45 s
    omega = 2.0 * math.pi / 0.45
    print("spin angular velocity: %.2f rad/s" % omega)
    assert 13.9 < omega < 14.0
    print("rule: spot over the shoulder - blind spins miss, and a miss must re-face")
    print("OK: %s becomes the cyclone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_flying_knee(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flying knee: jump from 2.5 m/s takeoff, knee chambered at 1.0 m
    v0 = 2.5
    h = v0 ** 2 / (2.0 * 9.81)
    reach = 1.0 + h
    print("jump height: %.4f m" % h)
    print("knee reach at peak: %.4f m" % reach)
    assert 0.318 < h < 0.320
    assert 1.318 < reach < 1.320
    print("rule: hands pull down as the knee drives up - the collision is the knockout")
    print("OK: %s strikes from the sky" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_spin_heel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spinning heel kick: 360 degrees in 0.5 s, heel at 1.0 m
    omega = 2.0 * math.pi / 0.5
    heel_v = omega * 1.0
    print("heel speed: %.3f m/s" % heel_v)
    assert 12.56 < heel_v < 12.58
    print("rule: full commitment or nothing - the last 90 degrees hold the power")
    print("OK: %s swings the whirlwind scythe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_pocket_elbows(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # range bands: elbow 0.30-0.45 m, punch 0.60-0.80 m, kick 0.90-1.20 m
    bands = {"elbow": (0.30, 0.45), "punch": (0.60, 0.80), "kick": (0.90, 1.20)}
    pocket_w = bands["elbow"][1] - bands["elbow"][0]
    print("pocket band width: %.2f m" % pocket_w)
    for k, (lo, hi) in bands.items():
        print("  %-6s %.2f-%.2f m" % (k, lo, hi))
    assert 0.149 < pocket_w < 0.151
    print("rule: at forearm distance long weapons jam and short blades rule")
    print("OK: %s owns the forge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_clinch_throws(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # throw geometry: base 0.4 m wide, CoM pulled 0.25 m past center
    base, pull = 0.4, 0.25
    edge = base / 2.0
    margin = pull - edge
    print("base half-width: %.2f m, pull: %.2f m" % (edge, pull))
    print("topple margin: %.3f m" % margin)
    assert 0.049 < margin < 0.051
    print("rule: balance breaks before the body falls - move the mass, remove the base")
    print("OK: %s reaps the harvest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_sweeps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep leverage: 12 kg leg, CoM at 0.45 m, sweep at the 0.9 m ankle
    m, com, ankle = 12.0, 0.45, 0.9
    torque = m * 9.81 * com
    force = torque / ankle
    print("leg torque: %.2f N m" % torque)
    print("sweep force at ankle: %.2f N" % force)
    assert 58.8 < force < 58.9
    print("rule: leverage, not strength - the ankle is the longest lever")
    print("OK: %s calls the tide" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_counter_timing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # counter window: 0.15 s attack vs 0.10 s interception launch
    attack, launch = 0.15, 0.10
    window = attack - launch
    print("attack time: %.2f s, counter launch: %.2f s" % (attack, launch))
    print("counter window: %.3f s" % window)
    assert 0.049 < window < 0.051
    print("rule: timing beats speed - the counter starts later and lands first")
    print("OK: %s answers before the question" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_combinations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # combination branching: 8 strikes, 3 deep
    strikes, depth = 8, 3
    combos = strikes ** depth
    print("strike library: %d, combination depth: %d" % (strikes, depth))
    print("possible 3-strike flows: %d" % combos)
    assert combos == 512
    print("rule: combinations are decision trees, not scripts - read and branch")
    print("OK: %s speaks in sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_ringcraft(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ring geometry: 6.1 m square, diagonal escape line, 45-degree cut
    side = 6.1
    diag = side * math.sqrt(2.0)
    cut_angle = 45.0
    print("ring diagonal: %.4f m" % diag)
    print("cut angle: %.0f degrees" % cut_angle)
    assert 8.62 < diag < 8.63
    print("rule: do not chase - herd; cut the escape and let the ropes trap")
    print("OK: %s draws the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mt_fight_camp(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # camp week volume: 2 sessions/day x 10 rounds x 6 days, 60 strikes/round
    rounds = 2 * 10 * 6
    strikes = rounds * 60
    print("rounds per week: %d" % rounds)
    print("strikes per week: %d" % strikes)
    assert rounds == 120
    assert strikes == 7200
    print("rule: build volume, sharpen intensity, taper to freshness - in that order")
    print("OK: %s signs the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "stance": demo_mt_stance,
    "footwork": demo_mt_footwork,
    "guard": demo_mt_guard,
    "jab": demo_mt_jab,
    "parry_slip": demo_mt_parry_slip,
    "shadowboxing": demo_mt_shadowboxing,
    "cross": demo_mt_cross,
    "roundhouse": demo_mt_roundhouse,
    "teep": demo_mt_teep,
    "check": demo_mt_check,
    "heavy_bag": demo_mt_heavy_bag,
    "conditioning": demo_mt_conditioning,
    "hook": demo_mt_hook,
    "uppercut": demo_mt_uppercut,
    "elbow_horizontal": demo_mt_elbow_horizontal,
    "knee_straight": demo_mt_knee_straight,
    "elbow_updiag": demo_mt_elbow_updiag,
    "knee_curved": demo_mt_knee_curved,
    "clinch_entry": demo_mt_clinch_entry,
    "low_kick": demo_mt_low_kick,
    "switch_kick": demo_mt_switch_kick,
    "clinch_control": demo_mt_clinch_control,
    "catch_dump": demo_mt_catch_dump,
    "shell_counter": demo_mt_shell_counter,
    "spin_elbow": demo_mt_spin_elbow,
    "flying_knee": demo_mt_flying_knee,
    "spin_heel": demo_mt_spin_heel,
    "pocket_elbows": demo_mt_pocket_elbows,
    "clinch_throws": demo_mt_clinch_throws,
    "sweeps": demo_mt_sweeps,
    "counter_timing": demo_mt_counter_timing,
    "combinations": demo_mt_combinations,
    "ringcraft": demo_mt_ringcraft,
    "fight_camp": demo_mt_fight_camp,
}
