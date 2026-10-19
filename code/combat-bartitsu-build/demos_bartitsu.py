#!/usr/bin/env python3
"""Demo programs for the Bartitsu Combat databases (Manon's combat orders
2026-10-17, combat batch 3).

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: stance geometry, footwork timing,
cane leverage, fall physics, strike energetics, throw mechanics, drill
timers, and combination counters. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_bart_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Bartitsu timeline: founding to academy years to today
    founding, academy_open, academy_close, today = 1898, 1899, 1902, 2026
    age = today - founding
    academy_years = academy_close - academy_open
    pillars = ["pugilism", "savate", "jujutsu", "cane (Vigny)"]
    share = 100.0 / len(pillars)
    print("founded: %d; academy years: %d; age in %d: %d years" % (founding, academy_years, today, age))
    for p in pillars:
        print("  pillar: %-14s %5.2f %%" % (p, share))
    print("pillars: %d" % len(pillars))
    assert age == 128
    assert academy_years == 3
    assert 24.99 < share < 25.01
    print("rule: four arts, one system - the cane, the kick, the blow, the throw")
    print("OK: %s framed the art" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_guard_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance base triangle: fore-aft separation x lateral width
    fore_aft, lateral = 0.55, 0.30
    base_area = 0.5 * fore_aft * lateral
    mass = 70.0
    on_balls = mass * 0.60
    force_balls = on_balls * 9.81
    print("base triangle: %.2f m x %.2f m -> area %.4f m^2" % (fore_aft, lateral, base_area))
    print("mass on balls of feet: %.1f kg (%.1f N)" % (on_balls, force_balls))
    assert 0.0824 < base_area < 0.0826
    assert 41.99 < on_balls < 42.01
    assert 411.9 < force_balls < 412.2
    print("rule: front foot leads the advance, rear foot leads the retreat")
    print("OK: %s held the platform" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three-minute footwork round: step rate and ground covered
    round_s, step_rate = 180.0, 2.0
    steps = round_s * step_rate
    step_len = 0.45
    distance = steps * step_len
    box_sides = 4
    print("round: %.0f s at %.1f steps/s -> %.0f steps" % (round_s, step_rate, steps))
    print("step length %.2f m -> distance %.1f m" % (step_len, distance))
    print("box pattern sides: %d" % box_sides)
    assert steps == 360.0
    assert 161.9 < distance < 162.1
    print("rule: never cross the feet, never let them meet, head level")
    print("OK: %s drilled the engine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_cane_grip(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cane leverage: grip 0.10 m from head, 0.91 m cane -> 0.81 m to tip
    cane_len, grip_inset = 0.91, 0.10
    lever_tip = cane_len - grip_inset
    force = 50.0
    torque_tip = force * lever_tip
    # parry: attacker force at his foible (0.81 m) vs defender forte (0.20 m)
    mech_adv = lever_tip / 0.20
    print("lever to tip: %.2f m; torque at %.0f N: %.2f N m" % (lever_tip, force, torque_tip))
    print("parry mechanical advantage (forte vs foible): %.2f" % mech_adv)
    assert 0.809 < lever_tip < 0.811
    assert 40.49 < torque_tip < 40.51
    assert 4.04 < mech_adv < 4.06
    print("rule: strike with the foible, parry with the forte, steer with the wrist")
    print("OK: %s took the grip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_ukemi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # back breakfall from shoulder height: hard stop vs roll-out
    h, g = 1.40, 9.81
    v = math.sqrt(2 * g * h)
    hard_stop, roll_out = 0.05, 1.20
    decel_hard = v * v / (2 * hard_stop) / g
    decel_roll = v * v / (2 * roll_out) / g
    print("impact velocity from %.2f m: %.2f m/s" % (h, v))
    print("hard stop over %.2f m: %.1f g" % (hard_stop, decel_hard))
    print("roll over %.2f m: %.2f g" % (roll_out, decel_roll))
    assert 5.23 < v < 5.25
    assert 27.9 < decel_hard < 28.1
    assert 1.16 < decel_roll < 1.18
    print("rule: slap, tuck the chin, never post a straight arm")
    print("OK: %s learned to fall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_straight_blow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight blow: effective mass and fist velocity -> energy and power
    m_eff, v = 4.0, 9.0
    momentum = m_eff * v
    ke = 0.5 * m_eff * v * v
    t_extend = 0.12
    power = ke / t_extend
    print("effective mass %.1f kg at %.1f m/s" % (m_eff, v))
    print("momentum: %.1f kg m/s; kinetic energy: %.1f J" % (momentum, ke))
    print("extension time %.2f s -> power %.0f W" % (t_extend, power))
    assert 35.99 < momentum < 36.01
    assert 161.9 < ke < 162.1
    assert 1349.0 < power < 1351.0
    print("rule: hit through the target, breathe out, guard returns")
    print("OK: %s threw the straight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_front_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # savate front kick: shod foot mass and piston velocity
    m_foot, v = 4.5, 11.0
    ke = 0.5 * m_foot * v * v
    leg_len, hip_drive = 0.95, 0.15
    reach = leg_len + hip_drive
    print("shod foot %.1f kg at %.1f m/s -> KE %.2f J" % (m_foot, v, ke))
    print("reach: leg %.2f m + hip drive %.2f m = %.2f m" % (leg_len, hip_drive, reach))
    assert 272.24 < ke < 272.26
    assert 1.099 < reach < 1.101
    print("rule: chamber, piston, rechamber - the hips drive, the shoe delivers")
    print("OK: %s kicked the measure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_cane_guards(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tierce + quarte coverage of the 180-degree high line
    tierce_arc, quarte_arc, overlap = 100.0, 100.0, 20.0
    coverage = tierce_arc + quarte_arc - overlap
    high_line = 180.0
    uncovered = high_line - coverage
    print("tierce %.0f deg + quarte %.0f deg - overlap %.0f deg = %.0f deg covered" % (
        tierce_arc, quarte_arc, overlap, coverage))
    print("uncovered high line: %.1f %%" % (uncovered / high_line * 100.0))
    assert coverage == 180.0
    assert uncovered == 0.0
    print("rule: a guard is a chambered riposte, not a wall")
    print("OK: %s raised the guards" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_distance_timing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # measures and the reaction gap: safe long measure
    long_m, mid_m, close_m = 1.60, 1.10, 0.60
    reaction, advance_speed = 0.25, 1.80
    gap_closed = reaction * advance_speed
    safe_long = long_m + gap_closed
    print("measures: long %.2f m, middle %.2f m, close %.2f m" % (long_m, mid_m, close_m))
    print("reaction %.2f s at advance %.1f m/s closes %.2f m" % (reaction, advance_speed, gap_closed))
    print("safe long measure: %.2f m" % safe_long)
    assert 0.449 < gap_closed < 0.451
    assert 2.049 < safe_long < 2.051
    print("rule: perfect technique at the wrong measure is a missed technique")
    print("OK: %s read the measure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_cane_parries(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # beat parry: lateral tap grows into a clean miss by the body
    point_speed, parry_dist = 6.0, 0.60
    time_left = parry_dist / point_speed
    lateral_v = 1.0
    miss = lateral_v * time_left
    print("point at %.1f m/s, parried %.2f m out -> %.3f s to arrival" % (point_speed, parry_dist, time_left))
    print("lateral %.1f m/s over that time -> miss distance %.3f m" % (lateral_v, miss))
    assert 0.0999 < time_left < 0.1001
    assert 0.0999 < miss < 0.1001
    print("rule: parry with the forte, move the cane not the body, answer at once")
    print("OK: %s turned the point" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_overhead_cut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # overhead cut: wrist snap multiplies tip speed at the foible
    radius, omega = 0.75, 14.0
    tip_speed = radius * omega
    rev_per_s = omega / (2 * math.pi)
    print("foible radius %.2f m at %.1f rad/s -> tip speed %.2f m/s" % (radius, omega, tip_speed))
    print("rotation rate: %.2f rev/s" % rev_per_s)
    assert 10.49 < tip_speed < 10.51
    assert 2.227 < rev_per_s < 2.229
    print("rule: cut through the target, finish in guard")
    print("OK: %s brought the cut down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_moulinet(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # figure-of-eight: tip path per cycle and rotation rate
    r_loop = 0.45
    loop_path = 2 * math.pi * r_loop
    cycle_path = 2 * loop_path
    freq = 2.5
    tip_speed = cycle_path * freq
    cycles_min = freq * 60.0
    print("loop path %.3f m; figure-of-eight cycle %.3f m" % (loop_path, cycle_path))
    print("at %.1f Hz: tip speed %.2f m/s, %.0f cycles/min" % (freq, tip_speed, cycles_min))
    assert 2.826 < loop_path < 2.828
    assert 5.654 < cycle_path < 5.656
    assert 14.13 < tip_speed < 14.15
    assert cycles_min == 150.0
    print("rule: the wrist works, the arm guides - the wall that bites")
    print("OK: %s turned the eight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_o_goshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # o goshi lever: hip fulcrum, effort arm vs load arm
    opp_mass = 80.0
    effort_arm, load_arm = 0.60, 0.25
    mech_adv = effort_arm / load_arm
    force_needed = opp_mass * 9.81 / mech_adv
    print("effort arm %.2f m / load arm %.2f m -> advantage %.2f" % (effort_arm, load_arm, mech_adv))
    print("force to throw %d kg opponent: %.1f N" % (opp_mass, force_needed))
    assert 2.399 < mech_adv < 2.401
    assert 326.9 < force_needed < 327.1
    print("rule: kuzushi first, the hip is a fulcrum, leverage beats strength")
    print("OK: %s loaded the hip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_hook_punch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hook: bent-arm arc, body rotation -> tangential fist speed
    radius, omega = 0.55, 16.0
    v = radius * omega
    m_fist = 0.6
    ke = 0.5 * m_fist * v * v
    print("arc radius %.2f m at %.1f rad/s -> fist %.2f m/s" % (radius, omega, v))
    print("fist %.1f kg -> KE %.2f J" % (m_fist, ke))
    assert 8.79 < v < 8.81
    assert 23.22 < ke < 23.26
    print("rule: pivot the foot, whip the body, elbow high")
    print("OK: %s hooked around the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_low_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # coup de pied bas: lower-leg swing -> impact force
    m_leg, v = 3.5, 9.0
    ke = 0.5 * m_leg * v * v
    momentum = m_leg * v
    contact_t = 0.02
    force = momentum / contact_t
    print("lower leg %.1f kg at %.1f m/s -> KE %.2f J, momentum %.1f" % (m_leg, v, ke, momentum))
    print("contact %.2f s -> impact force %.0f N" % (contact_t, force))
    assert 141.74 < ke < 141.76
    assert 1574.0 < force < 1576.0
    print("rule: kick the leg till he guards low, then take the exposed line")
    print("OK: %s swept the foundation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_cane_thrust(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # thrust: lunge mass behind the point -> piercing pressure
    body, lunge_v = 75.0, 2.2
    momentum = body * lunge_v
    force = 800.0
    point_area = 0.0002
    pressure = force / point_area
    print("lunge: %.0f kg at %.1f m/s -> momentum %.1f kg m/s" % (body, lunge_v, momentum))
    print("force %.0f N on %.1f cm^2 -> pressure %.2f MPa" % (force, point_area * 1e4, pressure / 1e6))
    assert 164.99 < momentum < 165.01
    assert 3.999 < pressure / 1e6 < 4.001
    print("rule: shortest line, lunge behind it, recover at once")
    print("OK: %s drove the point" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_kotegaeshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kotegaeshi: torque at the wrist vs body-drop energy behind the spiral
    hand_lever = 0.19
    torque_lock = 15.0
    force_hand = torque_lock / hand_lever
    body, drop = 70.0, 0.10
    energy = body * 9.81 * drop
    print("lock torque %.1f N m at hand lever %.2f m -> hand force %.1f N" % (torque_lock, hand_lever, force_hand))
    print("body drop %.2f m of %d kg -> %.1f J behind the spiral" % (drop, body, energy))
    assert 78.94 < force_hand < 78.96
    assert 68.66 < energy < 68.68
    print("rule: the body turns the spiral, never the arms alone")
    print("OK: %s turned the wrist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_chasse(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # chasse: driving column reach and momentum
    leg_len, hip_commit = 0.95, 0.25
    reach = leg_len + hip_commit
    m_eff, v = 12.0, 7.0
    momentum = m_eff * v
    print("reach: leg %.2f m + hip %.2f m = %.2f m" % (leg_len, hip_commit, reach))
    print("driving mass %.0f kg at %.1f m/s -> momentum %.1f kg m/s" % (m_eff, v, momentum))
    assert 1.199 < reach < 1.201
    assert 83.99 < momentum < 84.01
    print("rule: turn the hip over, drive like a battering ram, rechamber")
    print("OK: %s drove the side kick" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_uppercut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uppercut: leg drive work and rising fist speed
    body, dip = 75.0, 0.25
    work = body * 9.81 * dip
    rise, t = 0.50, 0.15
    v_up = rise / t
    print("leg drive: %d kg through %.2f m dip -> %.1f J" % (body, dip, work))
    print("fist rises %.2f m in %.2f s -> %.2f m/s upward" % (rise, t, v_up))
    assert 183.9 < work < 184.0
    assert 3.32 < v_up < 3.34
    print("rule: thrown from the knees up - standing tall throws only the arm")
    print("OK: %s rose from the floor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_cane_disarm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crook disarm: twist torque vs grip resistance torque
    crook_r, twist_force = 0.06, 60.0
    torque_twist = crook_r * twist_force
    grip_r, grip_force = 0.04, 40.0
    torque_grip = grip_r * grip_force
    wins = torque_twist > torque_grip
    print("crook twist: %.2f m x %.0f N = %.2f N m" % (crook_r, twist_force, torque_twist))
    print("grip resists: %.2f m x %.0f N = %.2f N m" % (grip_r, grip_force, torque_grip))
    print("disarm wins: %s" % wins)
    assert 3.599 < torque_twist < 3.601
    assert 1.599 < torque_grip < 1.601
    assert wins
    print("rule: the twist attacks the grip's weak axis - a straight pull fails")
    print("OK: %s stripped the weapon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_cane_hip_throw(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cane assist lengthens the throwing lever: 0.60 m arm -> 1.00 m with cane
    opp_mass = 80.0
    load_arm = 0.25
    ma_plain = 0.60 / load_arm
    ma_cane = 1.00 / load_arm
    f_plain = opp_mass * 9.81 / ma_plain
    f_cane = opp_mass * 9.81 / ma_cane
    reduction = (f_plain - f_cane) / f_plain * 100.0
    print("plain hip throw: MA %.2f -> %.1f N" % (ma_plain, f_plain))
    print("cane assisted:  MA %.2f -> %.1f N" % (ma_cane, f_cane))
    print("force reduction: %.1f %%" % reduction)
    assert 2.399 < ma_plain < 2.401
    assert 3.999 < ma_cane < 4.001
    assert 196.19 < f_cane < 196.21
    assert 39.9 < reduction < 40.1
    print("rule: the cane supplies the handle the street does not")
    print("OK: %s stacked the levers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_combinations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # combination counting: techniques ^ links, and session volume
    techs, links = 8, 3
    combos = techs ** links
    rounds, round_s, per_combo_s = 5, 180.0, 4.0
    per_round = round_s / per_combo_s
    session = per_round * rounds
    print("%d techniques in %d-link chains -> %d combinations" % (techs, links, combos))
    print("%d rounds x %.0f combos/round = %.0f combos per session" % (rounds, per_round, session))
    assert combos == 512
    assert per_round == 45.0
    assert session == 225.0
    print("rule: guard returns between links - a combination is not flailing")
    print("OK: %s chained the weapons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_seoi_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seoi nage: loading the opponent onto the shoulder axle
    opp_mass, lift = 80.0, 0.35
    work = opp_mass * 9.81 * lift
    t_throw = 0.50
    power = work / t_throw
    print("loading %d kg up %.2f m -> %.1f J" % (opp_mass, lift, work))
    print("throw time %.2f s -> power %.0f W" % (t_throw, power))
    assert 274.67 < work < 274.69
    assert 549.3 < power < 549.5
    print("rule: the shoulder is the axle - drop it under his center")
    print("OK: %s turned the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_balayage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # balayage timing window: weight transfer vs sweep arrival
    transfer_t = 0.28
    sweep_dist, sweep_v = 0.50, 4.0
    sweep_t = sweep_dist / sweep_v
    margin = transfer_t - sweep_t
    print("weight transfer window: %.2f s" % transfer_t)
    print("sweep %.2f m at %.1f m/s -> %.3f s; margin %.3f s" % (sweep_dist, sweep_v, sweep_t, margin))
    assert 0.124 < sweep_t < 0.126
    assert 0.154 < margin < 0.156
    assert margin > 0, "sweep must fit inside the transfer window"
    print("rule: too early passes harmless, too late bounces off - the instant is everything")
    print("OK: %s swept the step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_juji_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # juji gatame lever model: wrist force -> elbow torque (illustrative)
    forearm = 0.30
    force_wrist = 100.0
    torque_elbow = forearm * force_wrist
    control_threshold = 25.0
    print("wrist force %.0f N on %.2f m forearm -> elbow torque %.1f N m" % (force_wrist, forearm, torque_elbow))
    print("control threshold %.1f N m; margin %.1f N m" % (control_threshold, torque_elbow - control_threshold))
    assert 29.99 < torque_elbow < 30.01
    assert torque_elbow > control_threshold
    print("rule: position before submission - the hips feel the resistance")
    print("OK: %s set the armlock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_knife_defense(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knife geometry: lunge reach vs cane barrier, and why escape outranks both
    lunge_reach = 1.50
    cane_barrier = 1.60
    margin = cane_barrier - lunge_reach
    lunge_speed = 3.0
    lunge_time = lunge_reach / lunge_speed
    react, step_off = 0.25, 0.30
    print("lunge reach %.2f m in %.2f s; cane barrier %.2f m -> margin %.2f m" % (
        lunge_reach, lunge_time, cane_barrier, margin))
    print("reaction %.2f s + offline step %.2f s = %.2f s (must be < lunge time to evade clean)" % (
        react, step_off, react + step_off))
    assert 0.099 < margin < 0.101
    assert 0.499 < lunge_time < 0.501
    print("rule: escape first, barrier second, arm control third - never grab the blade")
    print("OK: %s held the measure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_flying_mare(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flying mare: borrowed pull velocity -> peak height and flight time
    pull_v = 2.0
    shoulder_h = 1.00
    peak = shoulder_h + pull_v * pull_v / (2 * 9.81)
    fall_t = math.sqrt(2 * peak / 9.81)
    print("pull velocity %.1f m/s over shoulder height %.2f m -> peak %.3f m" % (pull_v, shoulder_h, peak))
    print("fall time from peak: %.3f s" % fall_t)
    assert 1.203 < peak < 1.205
    assert 0.494 < fall_t < 0.496
    print("rule: his pull is the engine - hips under, grip the arm, bend decisive")
    print("OK: %s flew the mare" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_counters(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # counter window in frames at 60 fps: slip inside his execution+recovery
    fps = 60.0
    exec_frames, recover_frames = 12.0, 9.0
    window_s = (exec_frames + recover_frames) / fps
    slip_frames = 6.0
    slip_s = slip_frames / fps
    margin = window_s - slip_s
    print("his committed window: %.0f frames -> %.2f s" % (exec_frames + recover_frames, window_s))
    print("your slip: %.0f frames -> %.2f s; counter margin %.2f s" % (slip_frames, slip_s, margin))
    assert 0.349 < window_s < 0.351
    assert 0.099 < slip_s < 0.101
    assert 0.249 < margin < 0.251
    print("rule: defense small, answer immediate - steal his tempo")
    print("OK: %s answered in the same breath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_multiple_opponents(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shield geometry: circle so the near attacker blocks the far one
    a_deg, b_deg = 0.0, 90.0
    step_to = -45.0
    sep_a = abs(a_deg - step_to)
    sep_b = abs(b_deg - step_to)
    block_cone = 30.0
    b_blocked = sep_b - sep_a > block_cone
    print("attackers at %.0f and %.0f deg; you circle to %.0f deg" % (a_deg, b_deg, step_to))
    print("separations: %.0f deg and %.0f deg; far attacker blocked: %s" % (sep_a, sep_b, b_blocked))
    assert sep_a == 45.0
    assert sep_b == 135.0
    assert b_blocked
    print("rule: never ground, always circle, the exit is the win condition")
    print("OK: %s worked the geometry" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_cane_trap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two-handed trap: clamp force vs the trapped arm's pull
    hands = 2
    force_each = 150.0
    clamp = hands * force_each
    arm_pull = 200.0
    held = clamp > arm_pull
    print("clamp: %d hands x %.0f N = %.0f N vs arm pull %.0f N" % (hands, force_each, clamp, arm_pull))
    print("trap holds: %s" % held)
    assert clamp == 300.0
    assert held
    print("rule: at clinch range the cane grapples - one hand guides, one drives")
    print("OK: %s closed the frame" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_hadaka_jime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # safe choke drill timing + illustrative contact pressure model
    hold_s, rest_s, reps = 3.0, 10.0, 5
    session = reps * (hold_s + rest_s)
    force, area = 120.0, 0.004
    pressure_kpa = force / area / 1000.0
    print("drill: %d reps x (%.0f s hold + %.0f s rest) = %.0f s" % (reps, hold_s, rest_s, session))
    print("model pressure: %.0f N on %.4f m^2 -> %.1f kPa (illustrative)" % (force, area, pressure_kpa))
    assert session == 65.0
    assert 29.99 < pressure_kpa < 30.01
    print("rule: chin tucks, two hands pull, turn in - release on tap, instantly")
    print("OK: %s drilled the defense chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_randori(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # randori session timer: rounds, rest, volume
    round_s, rest_s, rounds = 180.0, 60.0, 5
    total = rounds * round_s + (rounds - 1) * rest_s
    ratio = round_s / rest_s
    per_combo_s = 4.0
    techniques = (round_s / per_combo_s) * rounds
    print("%d rounds x %.0f s + rests -> total %.0f s (%.1f min)" % (rounds, round_s, total, total / 60.0))
    print("work/rest %.0f:1; techniques at one per %.0f s: %.0f" % (ratio, per_combo_s, techniques))
    assert total == 1140.0
    assert ratio == 3.0
    assert techniques == 225.0
    print("rule: agreed, guided, contest - conventions keep students training tomorrow")
    print("OK: %s timed the rounds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_grand_combination(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grand combination: seven links, cumulative time and energy ledger
    links = [("thrust", 0.40, 165.0), ("overhead cut", 0.50, 120.0),
             ("one-two", 0.90, 324.0), ("low kick", 0.50, 141.8),
             ("cane trap", 0.80, 60.0), ("hip throw", 1.20, 274.7),
             ("juji gatame", 1.00, 40.0)]
    total_t = sum(t for _, t, _ in links)
    total_e = sum(e for _, _, e in links)
    print("links: %d" % len(links))
    for nm, t, e in links:
        print("  %-13s %4.2f s  %6.1f J" % (nm, t, e))
    print("sequence: %.2f s, %.1f J total" % (total_t, total_e))
    assert len(links) == 7
    assert 5.29 < total_t < 5.31
    assert 1125.4 < total_e < 1125.6
    print("rule: the capstone is seamlessness - one decision, seven links")
    print("OK: %s signed the whole name" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bart_teaching(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # teaching ladder planner: hours per tier for one full cycle
    tiers = [("foundations", 12, 3.0), ("compounded", 24, 3.0), ("advanced", 48, 3.0)]
    total = 0.0
    for nm, weeks, hrs in tiers:
        tier_h = weeks * hrs
        total += tier_h
        print("  %-12s %2d weeks x %.1f h = %5.1f h" % (nm, weeks, hrs, tier_h))
    class_size = 12
    print("full ladder cycle: %.1f h over %d weeks" % (total, sum(w for _, w, _ in tiers)))
    assert total == 252.0
    assert sum(w for _, w, _ in tiers) == 84
    print("rule: demonstrate, drill, correct - one fault at a time, safety first")
    print("OK: %s planned the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_bart_what_is,
    "guard_stance": demo_bart_guard_stance,
    "footwork": demo_bart_footwork,
    "cane_grip": demo_bart_cane_grip,
    "ukemi": demo_bart_ukemi,
    "straight_blow": demo_bart_straight_blow,
    "front_kick": demo_bart_front_kick,
    "cane_guards": demo_bart_cane_guards,
    "distance_timing": demo_bart_distance_timing,
    "cane_parries": demo_bart_cane_parries,
    "overhead_cut": demo_bart_overhead_cut,
    "moulinet": demo_bart_moulinet,
    "o_goshi": demo_bart_o_goshi,
    "hook_punch": demo_bart_hook_punch,
    "low_kick": demo_bart_low_kick,
    "cane_thrust": demo_bart_cane_thrust,
    "kotegaeshi": demo_bart_kotegaeshi,
    "chasse": demo_bart_chasse,
    "uppercut": demo_bart_uppercut,
    "cane_disarm": demo_bart_cane_disarm,
    "cane_hip_throw": demo_bart_cane_hip_throw,
    "combinations": demo_bart_combinations,
    "seoi_nage": demo_bart_seoi_nage,
    "balayage": demo_bart_balayage,
    "juji_gatame": demo_bart_juji_gatame,
    "knife_defense": demo_bart_knife_defense,
    "flying_mare": demo_bart_flying_mare,
    "counters": demo_bart_counters,
    "multiple_opponents": demo_bart_multiple_opponents,
    "cane_trap": demo_bart_cane_trap,
    "hadaka_jime": demo_bart_hadaka_jime,
    "randori": demo_bart_randori,
    "grand_combination": demo_bart_grand_combination,
    "teaching": demo_bart_teaching,
}
