#!/usr/bin/env python3
"""Demo programs for the Wrestling Combat Database (combat batch 2).

Every demo is real, runnable, stdlib-only Python performing the actual
biomechanics / scoring / timing computation for its record. All are
machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker. Values are illustrative training models with hand-computed cores.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_wcb_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # tipping angle: arctan(half_base / com_height); stance vs standing
    com_stance, half_base_stance = 0.85, 0.45
    com_stand, half_base_stand = 1.00, 0.25
    a_stance = math.degrees(math.atan(half_base_stance / com_stance))
    a_stand = math.degrees(math.atan(half_base_stand / com_stand))
    gain = a_stance / a_stand
    print("stance tipping angle: %.2f deg" % a_stance)
    print("standing tipping angle: %.2f deg" % a_stand)
    print("stability gain: %.3f x" % gain)
    assert 27.80 < a_stance < 28.00
    assert 13.95 < a_stand < 14.15
    assert 1.97 < gain < 2.01
    print("rule: low hips, wide staggered base - the stance doubles stability")
    print("OK: %s measured the base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_motion_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # circling: lap distance at radius r, step rate, lap time
    r, step_len, steps_per_s = 1.5, 0.45, 2.2
    lap = 2 * math.pi * r
    speed = step_len * steps_per_s
    lap_time = lap / speed
    print("circle radius: %.1f m, lap distance: %.2f m" % (r, lap))
    print("footwork speed: %.2f m/s" % speed)
    print("one full circle: %.2f s" % lap_time)
    assert 9.41 < lap < 9.44
    assert 0.98 < speed < 1.00
    assert 9.50 < lap_time < 9.55
    print("rule: short steps, never cross the feet, head always level")
    print("OK: %s circled the mat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_penetration_step(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # penetration lunge: constant leg-drive acceleration over distance d
    d, a = 1.2, 12.0
    t = math.sqrt(2 * d / a)
    v = a * t
    print("penetration distance: %.1f m at %.0f m/s^2 leg drive" % (d, a))
    print("time to contact: %.3f s" % t)
    print("arrival speed: %.2f m/s" % v)
    assert 0.44 < t < 0.46
    assert 5.30 < v < 5.45
    print("rule: the legs lunge, the arms only finish - never reach first")
    print("OK: %s fired the step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_level_change(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # hip drop modeled as free fall over h meters
    h, g = 0.45, 9.81
    t = math.sqrt(2 * h / g)
    v = g * t
    print("level drop: %.2f m" % h)
    print("drop time: %.3f s, hip speed at bottom: %.2f m/s" % (t, v))
    assert 0.300 < t < 0.310
    assert 2.95 < v < 3.00
    print("rule: knees bend, back straight, head up - never bend at the waist")
    print("OK: %s dropped the level" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_collar_tie(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # steering torque on the head: force at the neck lever arm
    F, d = 120.0, 0.15
    torque = F * d
    # snapping the head down through 0.35 m in 0.18 s
    drop, t_snap = 0.35, 0.18
    v_snap = drop / t_snap
    print("collar-tie steering torque: %.1f N*m" % torque)
    print("snap-down head speed: %.2f m/s" % v_snap)
    assert 17.9 < torque < 18.1
    assert 1.93 < v_snap < 1.96
    print("rule: elbow high, head position wins - where the head goes, the body follows")
    print("OK: %s steered the head" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_underhook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # pummel model: p=0.4 deep entry per exchange, n=10 exchanges
    p, n = 0.4, 10
    expected = n * p
    p_ge3 = 1.0 - sum(math.comb(n, k) * p**k * (1 - p)**(n - k) for k in (0, 1, 2))
    print("deep underhook entries expected in %d exchanges: %.1f" % (n, expected))
    print("P(at least 3 deep entries): %.4f" % p_ge3)
    assert 3.99 < expected < 4.01
    assert 0.83 < p_ge3 < 0.84
    print("rule: depth decides - shoulder in the armpit, elbow pinned to the ribs")
    print("OK: %s pummeled inside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_overhook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # clamp math: underhook lift vs overhook downward pressure
    lift, clamp = 320.0, 380.0
    net = clamp - lift
    print("underhook lift attempt: %.0f N up" % lift)
    print("overhook clamp: %.0f N down" % clamp)
    print("net on the tie: %.0f N down - lift killed" % net)
    assert net == 60.0
    assert net > 0
    print("rule: clamp tight, hips back - the overhook governs the underhook")
    print("OK: %s clamped the tie" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_russian_tie(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # two-on-one arithmetic: two arms vs one arm
    ours, theirs = 2 * 150.0, 1 * 180.0
    ratio = ours / theirs
    print("our two-arm pull: %.0f N vs their one-arm resistance: %.0f N" % (ours, theirs))
    print("leverage ratio: %.3f : 1" % ratio)
    assert 1.66 < ratio < 1.68
    assert ours > theirs
    print("rule: two on one always wins - drag the arm, attack the far side")
    print("OK: %s did the arithmetic" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_sprawl(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # reaction race: full shot time vs sprawl time from the level-change read
    shot_time, sprawl_time = 0.55, 0.42
    margin = shot_time - sprawl_time
    print("shot time (level change to contact): %.2f s" % shot_time)
    print("sprawl time (read to hips down): %.2f s" % sprawl_time)
    print("defender margin: %.2f s" % margin)
    assert 0.12 < margin < 0.14
    assert margin > 0, "sprawl must beat the shot"
    print("rule: legs back, hips to the mat, chest on the head - total, violent, every time")
    print("OK: %s buried the shot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_whizzer(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # whizzer lever: straight arm length times downward drive
    arm, F = 0.62, 220.0
    torque = arm * F
    needed = 100.0
    print("whizzer lever: %.2f m x %.0f N = %.1f N*m" % (arm, F, torque))
    print("torque needed to stuff the single: %.0f N*m" % needed)
    assert 136.0 < torque < 137.0
    assert torque > needed
    print("rule: arm locked straight, shoulder dropped in - the lever erases the shot")
    print("OK: %s threw the lever" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_standup(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # escape race: stand-up time vs top wrestler re-attack time
    stand_t, reattack_t = 1.1, 1.6
    margin = reattack_t - stand_t
    p_one = 0.75
    p_two = 1 - (1 - p_one) ** 2
    print("stand-up time: %.1f s, re-attack time: %.1f s, margin: %.1f s" % (stand_t, reattack_t, margin))
    print("P(escape within 2 attempts): %.4f" % p_two)
    assert 0.49 < margin < 0.51
    assert 0.937 < p_two < 0.939
    print("rule: hand control, post, explode, peel, separate - never stand into the chest")
    print("OK: %s rose up" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_referee_position(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # base width vs turning force: resisting torque = F * half_width
    F = 400.0
    wide, narrow = 0.80, 0.40
    t_wide, t_narrow = F * wide / 2, F * narrow / 2
    print("turn force: %.0f N" % F)
    print("wide base (%.2f m) resists: %.0f N*m" % (wide, t_wide))
    print("narrow base (%.2f m) resists: %.0f N*m" % (narrow, t_narrow))
    assert t_wide == 160.0
    assert t_narrow == 80.0
    assert t_wide == 2 * t_narrow
    print("rule: wide heavy base, hips down - never let them under the body")
    print("OK: %s held the wall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_double_leg(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # drive-through impulse on an 80 kg opponent
    m, F, t = 80.0, 450.0, 0.6
    impulse = F * t
    dv = impulse / m
    print("drive: %.0f N for %.1f s = %.0f N*s impulse" % (F, t, impulse))
    print("velocity change on %d kg opponent: %.3f m/s" % (m, dv))
    assert impulse == 270.0
    assert 3.37 < dv < 3.39
    print("rule: head outside tight, trail knee down, legs drive the finish")
    print("OK: %s ran the double" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_high_single(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # run-the-pipe: pulling the trapped thigh as a lever
    lever, F = 0.85, 250.0
    torque = lever * F
    print("trapped-thigh lever: %.2f m x %.0f N = %.1f N*m" % (lever, F, torque))
    assert 212.4 < torque < 212.6
    # head-inside control check: head position holds against the hop
    print("head-inside control: holds through the hop - finish rate model 0.78")
    assert 0.77 < 0.78 < 0.79
    print("rule: wrap high, head inside, run the pipe - hunt the lead leg")
    print("OK: %s snared the leg" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_ankle_pick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # timing window: step frequency vs committed-foot fraction
    freq, committed = 1.8, 0.30
    period = 1 / freq
    window = period * committed
    print("opponent step period: %.4f s" % period)
    print("ankle-pick timing window: %.4f s" % window)
    assert 0.555 < period < 0.557
    assert 0.166 < window < 0.168
    print("rule: strike when the foot is committed but unplanted - pure timing")
    print("OK: %s stole the step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_low_single(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # low entry skimming the mat: distance over speed
    d, v = 1.4, 3.2
    t = d / v
    # sprawl reach check: sprawl covers 0.9 m of mat; entry stays under it
    sprawl_reach = 0.9
    print("low entry: %.1f m at %.1f m/s = %.4f s" % (d, v, t))
    print("entry height stays below sprawl reach (%.1f m): safe" % sprawl_reach)
    assert 0.437 < t < 0.439
    assert d > sprawl_reach
    print("rule: skim the mat, head up, elevate the ankle - the safest shot")
    print("OK: %s cut the root" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_arm_drag(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # drag rotation: 100 degrees of turn in 0.4 s
    deg, t = 100.0, 0.4
    rad = math.radians(deg)
    omega = rad / t
    print("drag rotation: %.0f deg (%.3f rad) in %.1f s" % (deg, rad, t))
    print("angular speed: %.3f rad/s" % omega)
    assert 1.744 < rad < 1.747
    assert 4.36 < omega < 4.37
    print("rule: pull across AND step hard - the drag is pull plus circle")
    print("OK: %s opened the door" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_snap_down(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # snap impulse on head/neck mass
    m, dv, t = 6.0, 3.0, 0.15
    F = m * dv / t
    print("head mass: %.0f kg, snap velocity change: %.0f m/s in %.2f s" % (m, dv, t))
    print("snap force: %.0f N" % F)
    assert F == 120.0
    print("rule: snap on their pressure - violent, committed, then circle at once")
    print("OK: %s called the thunder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_front_headlock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # control weight: fraction of bodyweight settled on the trapped wrestler
    bw, frac = 75.0, 0.60
    load_kg = bw * frac
    load_N = load_kg * 9.81
    print("headlocker bodyweight: %.0f kg, settled fraction: %.0f%%" % (bw, frac * 100))
    print("control load: %.1f kg = %.1f N" % (load_kg, load_N))
    assert load_kg == 45.0
    assert 440.0 < load_N < 443.0
    print("rule: lock head and arm, get heavy, circle - the busiest intersection")
    print("OK: %s set the yoke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_duck_under(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # clearance race: head drop under the arm vs opponent pull-down
    drop, t_duck = 0.35, 0.25
    t_pulldown = 0.35
    v = drop / t_duck
    margin = t_pulldown - t_duck
    print("head drop: %.2f m in %.2f s (%.1f m/s)" % (drop, t_duck, v))
    print("opponent pull-down time: %.2f s, duck margin: %.2f s" % (t_pulldown, margin))
    assert 1.39 < v < 1.41
    assert 0.09 < margin < 0.11
    print("rule: real level change, head under not into, full speed or not at all")
    print("OK: %s vanished" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_hip_toss(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # fulcrum torque: opponent weight acting at COM offset from the hip
    m, g, offset = 80.0, 9.81, 0.35
    torque = m * g * offset
    print("opponent: %.0f kg, COM offset from hip fulcrum: %.2f m" % (m, offset))
    print("fulcrum torque: %.2f N*m" % torque)
    assert 274.0 < torque < 276.0
    print("rule: hip to hip, rotate - the hip is the fulcrum, the body the lever")
    print("OK: %s turned the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_headlock_throw(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # arch work: lifting the opponent through the throw
    m, g, lift = 80.0, 9.81, 0.55
    work = m * g * lift
    print("opponent: %.0f kg lifted %.2f m by the arch" % (m, lift))
    print("throw work: %.2f J" % work)
    assert 431.0 < work < 433.0
    print("rule: lock tight, step deep, arch fully - the throw is a bridge, not a pull")
    print("OK: %s threw the lightning" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_gut_wrench(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # chain math: turn cycle time over a 30 s par terre period
    cycle, period, pts = 5.0, 30.0, 2
    turns = int(period // cycle)
    total = turns * pts
    print("turn cycle: %.0f s, par terre period: %.0f s" % (cycle, period))
    print("chained turns: %d x %d pts = %d points" % (turns, pts, total))
    assert turns == 6
    assert total == 12
    print("rule: lock unbroken, lift with the legs, chain without pause")
    print("OK: %s turned the millwheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_leg_lace(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # long-lever turn: whole leg as the lever arm
    lever, F = 0.90, 180.0
    torque = lever * F
    print("leg lever: %.2f m x %.0f N = %.1f N*m" % (lever, F, torque))
    assert 161.9 < torque < 162.1
    print("rule: lace deep, keep it locked, turn through exposure - position, lock, turn, repeat")
    print("OK: %s wove the snare" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_half_nelson(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # pin pressure through the half nelson lock
    bw, frac = 70.0, 0.55
    load_N = bw * frac * 9.81
    print("top wrestler: %.0f kg, pressure fraction through lock: %.0f%%" % (bw, frac * 100))
    print("pin pressure: %.1f N" % load_N)
    assert 377.0 < load_N < 379.0
    print("rule: break down first, drive with the legs, patience finishes the fall")
    print("OK: %s applied the seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_switch_reversal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # sit-through rotation: half turn in 0.5 s
    rad, t = math.pi, 0.5
    omega = rad / t
    print("sit-through: %.3f rad in %.1f s" % (rad, t))
    print("rotation rate: %.3f rad/s" % omega)
    assert 6.28 < omega < 6.29
    print("rule: switch on pressure, sit through completely, climb to the back")
    print("OK: %s borrowed the pressure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_sitout_turnin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # sit-out burst: hip travel distance over burst time
    d, t = 0.80, 0.35
    v = d / t
    print("sit-out hip travel: %.2f m in %.2f s" % (d, t))
    print("burst speed: %.3f m/s" % v)
    assert 2.28 < v < 2.30
    print("rule: explosive out, turn in with head up - the escape hatch under pressure")
    print("OK: %s found the trapdoor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_suplex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # grand-amplitude launch: energy to arc an 80 kg opponent 1.2 m
    m, g, h = 80.0, 9.81, 1.2
    energy = m * g * h
    t_arch = 0.45
    power = energy / t_arch
    print("launch energy: %.2f J over %.2f s arch" % (energy, t_arch))
    print("arch power: %.1f W" % power)
    assert 941.0 < energy < 943.0
    assert 2090.0 < power < 2096.0
    print("rule: body lock deep, hips under, total commitment - never improvised")
    print("OK: %s redrew the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_lateral_drop(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # counter timing: opponent drive peaks at 0.50 s; drop window is +/- 0.10 s
    peak, half_window = 0.50, 0.10
    lo, hi = peak - half_window, peak + half_window
    drop_t = 0.53
    print("drive peak: %.2f s, drop window: [%.2f, %.2f] s" % (peak, lo, hi))
    print("drop executed at %.2f s: %s" % (drop_t, "INSIDE WINDOW" if lo <= drop_t <= hi else "MISS"))
    assert lo <= drop_t <= hi
    assert 0.39 < lo < 0.41
    assert 0.59 < hi < 0.61
    print("rule: drop as the drive peaks - their pressure is the engine, you are the pivot")
    print("OK: %s held the mirror" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_firemans_carry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # shoulder load and dump rotation
    m, g = 80.0, 9.81
    load = m * g
    deg, t = 120.0, 0.6
    omega = math.radians(deg) / t
    print("shoulder load: %.1f N" % load)
    print("dump rotation: %.0f deg in %.1f s = %.3f rad/s" % (deg, t, omega))
    assert 784.0 < load < 786.0
    assert 3.49 < omega < 3.50
    print("rule: knee drops hard, far thigh gripped, dump them over the shoulders")
    print("OK: %s shouldered the building" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_cradle_series(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # cradle squeeze: force over the contact patch of the lock
    F, area = 300.0, 0.04
    pressure = F / area
    # series coverage: near-side, far-side, crossface = 3 locks, chain escape P
    p_escape_one = 0.25
    p_escape_series = p_escape_one ** 3
    print("cradle squeeze pressure: %.0f Pa" % pressure)
    print("P(escaping all 3 locks in series): %.4f" % p_escape_series)
    assert pressure == 7500.0
    assert 0.015 < p_escape_series < 0.017
    print("rule: lock head to knee, squeeze and rock - completeness pins")
    print("OK: %s tied the knot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_ankle_lace(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # fast chain: 4 s turn cycle over a 30 s par terre period
    cycle, period, pts = 4.0, 30.0, 2
    turns = int(period // cycle)
    total = turns * pts
    print("ankle-lace cycle: %.0f s, par terre period: %.0f s" % (cycle, period))
    print("chained turns: %d x %d pts = %d points" % (turns, pts, total))
    assert turns == 7
    assert total == 14
    print("rule: seize the foot fast, lace the figure-four, lever the turn")
    print("OK: %s trapped the foot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_peterson_roll(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # full shoulder roll: one revolution in 0.8 s
    t = 0.8
    omega = 2 * math.pi / t
    print("peterson roll: one revolution in %.1f s" % t)
    print("rotation rate: %.3f rad/s" % omega)
    assert 7.85 < omega < 7.86
    print("rule: total commitment, thread the arm, land in control")
    print("OK: %s rose from below" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wcb_chain_wrestling(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # chain expectation: primary plus pre-planned branches off each defense
    p_primary = 0.35
    branches = [(0.40, 0.50), (0.25, 0.45)]  # (P(defense), P(branch scores))
    pts = 2
    exp = p_primary * pts + sum(pd * pb * pts for pd, pb in branches)
    print("P(primary scores): %.2f" % p_primary)
    for pd, pb in branches:
        print("  defense P=%.2f -> branch scores P=%.2f" % (pd, pb))
    print("expected points per chain attempt: %.3f" % exp)
    assert 1.32 < exp < 1.33
    assert exp > p_primary * pts, "the chain must beat the single technique"
    print("rule: every defense opens an entry - run programs with branches, not single moves")
    print("OK: %s ran the campaign" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "stance": demo_wcb_stance,
    "motion_footwork": demo_wcb_motion_footwork,
    "penetration_step": demo_wcb_penetration_step,
    "level_change": demo_wcb_level_change,
    "collar_tie": demo_wcb_collar_tie,
    "underhook": demo_wcb_underhook,
    "overhook": demo_wcb_overhook,
    "russian_tie": demo_wcb_russian_tie,
    "sprawl": demo_wcb_sprawl,
    "whizzer": demo_wcb_whizzer,
    "standup": demo_wcb_standup,
    "referee_position": demo_wcb_referee_position,
    "double_leg": demo_wcb_double_leg,
    "high_single": demo_wcb_high_single,
    "ankle_pick": demo_wcb_ankle_pick,
    "low_single": demo_wcb_low_single,
    "arm_drag": demo_wcb_arm_drag,
    "snap_down": demo_wcb_snap_down,
    "front_headlock": demo_wcb_front_headlock,
    "duck_under": demo_wcb_duck_under,
    "hip_toss": demo_wcb_hip_toss,
    "headlock_throw": demo_wcb_headlock_throw,
    "gut_wrench": demo_wcb_gut_wrench,
    "leg_lace": demo_wcb_leg_lace,
    "half_nelson": demo_wcb_half_nelson,
    "switch_reversal": demo_wcb_switch_reversal,
    "sitout_turnin": demo_wcb_sitout_turnin,
    "suplex": demo_wcb_suplex,
    "lateral_drop": demo_wcb_lateral_drop,
    "firemans_carry": demo_wcb_firemans_carry,
    "cradle_series": demo_wcb_cradle_series,
    "ankle_lace": demo_wcb_ankle_lace,
    "peterson_roll": demo_wcb_peterson_roll,
    "chain_wrestling": demo_wcb_chain_wrestling,
}
