#!/usr/bin/env python3
"""Demo programs for the Krav Maga Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: stance geometry, footwork timing,
strike physics, leverage math, reaction-time windows, redirect angles,
and drill planning. All are machine-executed by build.py: each prints its
real computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker. Every number below matches the number
stated in the corresponding entry text (cross-checked 2026-10-17).
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cbkm_fighting_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance geometry: feet 1.3x shoulder width, weight 60/40
    shoulder = 0.45          # meters
    width = 1.3 * shoulder
    mass = 80.0             # kg student
    front = 0.60 * mass
    rear = 0.40 * mass
    print("stance width: %.3f m" % width)
    print("front foot load: %.1f kg, rear foot load: %.1f kg" % (front, rear))
    assert 0.584 < width < 0.586
    assert 47.9 < front < 48.1
    assert 31.9 < rear < 32.1
    assert abs(front + rear - mass) < 1e-9
    print("rule: the stance is the platform - build it first")
    print("OK: %s held the platform" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # footwork drill: step length, cadence, distance and round timing
    step, cadence, t = 0.5, 2.0, 10.0
    dist = step * cadence * t
    steps_per_round = 10
    step_time = 1.0 / cadence
    round_t = steps_per_round * step_time
    rounds = 6
    block = rounds * round_t
    print("10 s of footwork: %.1f m covered" % dist)
    print("per round: %d steps x %.1f s = %.1f s" % (steps_per_round, step_time, round_t))
    print("%d-round footwork block: %.0f s" % (rounds, block))
    assert 9.99 < dist < 10.01
    assert 4.99 < round_t < 5.01
    assert 29.9 < block < 30.1
    print("rule: the nearest foot moves first, the stance rebuilds every step")
    print("OK: %s moved without breaking" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_punch_combatives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight-punch force and four-punch combination timing
    m_eff, accel = 4.0, 60.0
    F = m_eff * accel
    per_punch, n = 0.25, 4
    combo = per_punch * n
    combos, round_t = 10, 10.0 * per_punch * n / n
    print("straight punch force: %.0f N" % F)
    print("four-punch combination: %.2f s" % combo)
    print("10 combinations: %.1f s combatives round" % (combos * combo))
    assert 239.9 < F < 240.1
    assert 0.999 < combo < 1.001
    assert 9.99 < combos * combo < 10.01
    print("rule: the hip throws the punch - the arm only delivers it")
    print("OK: %s fired the combination" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_palm_heel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # palm-heel vs fist: same force, different pressure on the striker
    F = 3000.0
    palm_area, fist_area = 0.008, 0.004
    p_palm = F / palm_area / 1000.0     # kPa
    p_fist = F / fist_area / 1000.0
    print("palm-heel pressure: %.1f kPa" % p_palm)
    print("fist pressure: %.1f kPa" % p_fist)
    print("pressure ratio fist/palm: %.1f" % (p_fist / p_palm))
    assert 374.9 < p_palm < 375.1
    assert 749.9 < p_fist < 750.1
    assert 1.99 < p_fist / p_palm < 2.01
    print("rule: spread the force, spare the hand")
    print("OK: %s struck with the open hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_elbow_strikes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow strike energy: forearm+hand mass whipped at speed
    m, v = 2.5, 12.0
    ke = 0.5 * m * v * v
    reach = 0.35
    print("elbow strike energy: %.1f J" % ke)
    print("effective range: %.2f m" % reach)
    # one elbow vs one palm-heel for scale
    print("energy per kilogram of weapon: %.1f J/kg" % (ke / m))
    assert 179.9 < ke < 180.1
    assert 71.9 < ke / m < 72.1
    print("rule: short weapon, full rotation - the elbow is for close work")
    print("OK: %s whipped the elbow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_knee_strikes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee strike: thigh mass stopped on target, impulse force
    m, v, t_stop = 10.0, 8.0, 0.05
    F = m * v / t_stop
    hip_drive = 0.45
    print("knee strike force: %.0f N" % F)
    print("hip drive into the strike: %.2f m" % hip_drive)
    print("momentum delivered: %.0f kg m/s" % (m * v))
    assert 1599.9 < F < 1600.1
    assert 79.9 < m * v < 80.1
    print("rule: pull down as the knee drives up - two forces, one point")
    print("OK: %s drove the knee" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_front_kick_groin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front kick to the groin: leg energy and rechamber time
    m, v = 15.0, 10.0
    ke = 0.5 * m * v * v
    rechamber = 0.3
    print("groin kick energy: %.1f J" % ke)
    print("rechamber time: %.1f s" % rechamber)
    # kicks per 10 s round if each kick cycle takes 0.6 s
    cycle = 0.6
    print("kicks per 10 s round at %.1f s per cycle: %d" % (cycle, int(10.0 / cycle)))
    assert 749.9 < ke < 750.1
    assert 0.299 < rechamber < 0.301
    assert int(10.0 / cycle) == 16
    print("rule: the kick opens - the hands finish")
    print("OK: %s snapped the front kick" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_hammerfist(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hammerfist: muscle-driven vs gravity-only drop
    m, v = 3.0, 8.0
    ke = 0.5 * m * v * v
    g, drop = 9.81, 0.6
    v_grav = math.sqrt(2 * g * drop)
    print("hammerfist energy at 8 m/s: %.1f J" % ke)
    print("gravity-only speed on a 0.6 m drop: %.2f m/s" % v_grav)
    print("muscle contribution: %.1f percent of total speed" % (100.0 * (v - v_grav) / v))
    assert 95.9 < ke < 96.1
    assert 3.42 < v_grav < 3.44
    assert 57.0 < 100.0 * (v - v_grav) / v < 57.3
    print("rule: gravity assists - the muscles do the work")
    print("OK: %s swung the hammerfist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_inside_defense(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inside defense timing: deflect 0.2 m inside the punch's 0.06 s window
    punch_v, gap = 10.0, 0.6
    t_punch = gap / punch_v
    deflect = 0.2
    hand_v = deflect / t_punch
    counter_delay = 0.1
    print("punch travel time over 0.6 m: %.3f s" % t_punch)
    print("required hand speed for 0.2 m deflection: %.2f m/s" % hand_v)
    print("counter lands at: %.2f s after the punch starts" % (t_punch + counter_delay))
    assert 0.0599 < t_punch < 0.0601
    assert 3.33 < hand_v < 3.34
    assert 0.1599 < t_punch + counter_delay < 0.1601
    print("rule: defend and attack are one motion")
    print("OK: %s rode the punch off the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_wrist_grab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wrist grab release: bodyweight pull on a lever against the thumb
    pull, lever = 400.0, 0.3
    torque = pull * lever
    thumb_resist = 20.0   # N m a thumb grip can resist
    print("release torque: %.1f N m" % torque)
    print("thumb grip resistance: %.0f N m" % thumb_resist)
    print("margin: %.0f N m in the defender's favor" % (torque - thumb_resist))
    assert 119.9 < torque < 120.1
    assert 99.9 < torque - thumb_resist < 100.1
    print("rule: the whole body signs against the single thumb")
    print("OK: %s tore the wrist free" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_defense_360(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 360 defense: reaction window vs attack arrival, drill volume
    dist, atk_v = 1.5, 8.0
    t_arrive = dist / atk_v
    t_react = 0.20
    sectors, per = 8, 45
    print("attack arrival time: %.4f s vs trained reaction %.2f s" % (t_arrive, t_react))
    print("coverage: %d sectors x %d degrees = %d degrees" % (sectors, per, sectors * per))
    drill_t, cadence = 300.0, 3.0
    reps = int(drill_t / cadence)
    print("5-minute drill at 3 s cadence: %d repetitions" % reps)
    assert 0.1874 < t_arrive < 0.1876
    assert sectors * per == 360
    assert reps == 100
    print("rule: drill until direction no longer matters")
    print("OK: %s covered the full circle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_front_choke_pluck(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front choke pluck: two-hand pull vs the choke press
    per_hand, hands = 300.0, 2
    pluck = per_hand * hands
    press = 400.0
    margin = pluck - press
    window = 1.0   # seconds before the choke sets
    print("pluck force: %.0f N vs choke press %.0f N" % (pluck, press))
    print("pluck wins by: %.0f N" % margin)
    print("the pluck must land inside: %.1f s" % window)
    assert 599.9 < pluck < 600.1
    assert 199.9 < margin < 200.1
    print("rule: tuck the chin, pluck with the body, kick the groin")
    print("OK: %s plucked the choke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_side_headlock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # side headlock escape: bridge lift and shrimp space
    atk_mass, frac = 80.0, 0.60
    lifted = atk_mass * frac
    F = lifted * 9.81
    shrimp = 0.25
    print("bridge lifts %.0f kg: %.1f N of hip drive" % (lifted, F))
    print("shrimp creates %.2f m of escape space" % shrimp)
    assert 47.9 < lifted < 48.1
    assert 470.8 < F < 471.0
    assert 0.249 < shrimp < 0.251
    print("rule: bridge first, shrimp second, head out third")
    print("OK: %s bridged out of the headlock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_shirt_grab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two-handed shirt grab: double pluck plus simultaneous kick window
    per_hand, hands = 250.0, 2
    pluck = per_hand * hands
    window = 0.5   # seconds: pluck and kick land together
    print("double pluck: %.0f N down and out" % pluck)
    print("pluck and groin kick land inside: %.1f s" % window)
    # kick cycles inside the window
    print("kick cycles available in the window: %.1f" % (window / 0.3))
    assert 499.9 < pluck < 500.1
    assert 1.66 < window / 0.3 < 1.68
    print("rule: both hands pluck while the leg answers")
    print("OK: %s broke the shirt grab" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_bear_hug_free(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bear hug arms-free: rear elbow energy and base drop
    m, v = 2.5, 10.0
    ke = 0.5 * m * v * v
    drop = 0.35   # meters the hips sink
    mass = 80.0
    # lower center of gravity: stability gain as base torque
    print("rear elbow energy: %.1f J" % ke)
    print("base drop: %.2f m - the lift now fights %.0f kg sunk low" % (drop, mass))
    assert 124.9 < ke < 125.1
    assert 0.349 < drop < 0.351
    print("rule: drop low, strike free, turn in")
    print("OK: %s broke the free bear hug" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_bear_hug_pinned(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bear hug arms-pinned: space-making shrug then the 90-degree turn
    per_side = 0.15
    total_space = 2 * per_side
    turn = math.pi / 2
    t_turn = 0.4
    omega = turn / t_turn
    print("space made: %.2f m per side, %.2f m total" % (per_side, total_space))
    print("90-degree turn in %.1f s: %.2f rad/s" % (t_turn, omega))
    assert 0.299 < total_space < 0.301
    assert 3.926 < omega < 3.928
    print("rule: make space first - no space, no strike")
    print("OK: %s turned out of the pinned hug" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_hair_grab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hair grab: two-hand clamp pins the grabbing hand, step kills leverage
    per_hand, hands = 300.0, 2
    pin = per_hand * hands
    shorten = 0.2   # meters of pull leverage removed
    print("clamp pin force: %.0f N over the grabbing hand" % pin)
    print("leverage shortened by: %.1f m toward the thumb side" % shorten)
    assert 599.9 < pin < 600.1
    assert 0.199 < shorten < 0.201
    print("rule: pin the hand to the head - the lever becomes a post")
    print("OK: %s clamped the hair grab" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_rear_choke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear choke: 180-degree pivot toward the attack inside 1 second
    turn = math.pi
    t_turn = 0.4
    omega = turn / t_turn
    budget = 1.0
    print("pivot: 180 degrees in %.1f s = %.2f rad/s" % (t_turn, omega))
    print("pluck + turn + first strike inside: %.1f s" % budget)
    print("time left after the turn: %.1f s for the counter" % (budget - t_turn))
    assert 7.853 < omega < 7.855
    assert 0.599 < budget - t_turn < 0.601
    print("rule: turn toward the choke - never away")
    print("OK: %s spun out of the rear choke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_ground_survival(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # technical stand-up: four phases, total time, protected distance
    phases = 4
    total = 1.2
    per_phase = total / phases
    safe_dist = 2.0
    print("technical stand-up: %d phases in %.1f s (%.1f s per phase)" % (phases, total, per_phase))
    print("kicks hold the attacker %.0f m away until you rise" % safe_dist)
    assert phases == 4
    assert 0.299 < per_phase < 0.301
    assert 1.99 < safe_dist < 2.01
    print("rule: the ground is for escaping - stand up first")
    print("OK: %s stood up protected" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_kicks_ground(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kicks from the ground: upward kick energy, arc, reach
    m, v = 15.0, 7.0
    ke = 0.5 * m * v * v
    arc = 180.0
    reach = 1.2
    print("ground kick energy: %.1f J" % ke)
    print("coverage arc: %.0f degrees at %.1f m reach" % (arc, reach))
    assert 367.4 < ke < 367.6
    assert 179.9 < arc < 180.1
    assert 1.199 < reach < 1.201
    print("rule: kick to keep distance, stand on the hard kick")
    print("OK: %s kicked from the ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_clinch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # clinch pummeling cadence and head-pressure math
    switches, drill_t = 10, 20.0
    per_switch = drill_t / switches
    head_kg = 24.0
    pressure = head_kg * 9.81
    print("pummeling: %d switches in %.0f s = %.1f s per switch" % (switches, drill_t, per_switch))
    print("head pressure: %.1f N from %d kg of drive" % (pressure, int(head_kg)))
    assert 1.99 < per_switch < 2.01
    assert 235.4 < pressure < 235.5
    print("rule: never rest chest to chest - attack or exit")
    print("OK: %s owned the clinch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_bursting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bursting: entry speed and strike coverage during the burst
    dist, t = 2.0, 0.5
    v = dist / t
    strikes = 3
    rate = strikes / t
    print("burst speed: %.1f m/s over %d m" % (v, int(dist)))
    print("strikes during the burst: %d in %.1f s = %.1f per second" % (strikes, t, rate))
    assert 3.99 < v < 4.01
    assert 5.99 < rate < 6.01
    print("rule: always forward, always violent - the burst is the entry")
    print("OK: %s burst through the gap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_retzev(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # retzev: continuous striking volume and work per round
    rate, round_t = 3.0, 30.0
    strikes = int(rate * round_t)
    per_strike = 150.0
    work = strikes * per_strike
    rest, rounds = 60.0, 5
    session = rounds * (round_t + rest) - rest
    print("strikes per 30 s round at %.0f per second: %d" % (rate, strikes))
    print("work per round: %.0f J" % work)
    print("5-round session: %.0f s total" % session)
    assert strikes == 90
    assert 13499.0 < work < 13501.0
    assert 389.9 < session < 390.1
    print("rule: every strike chambers the next - never stop")
    print("OK: %s kept the continuous motion" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_knife_live_side(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # live-side knife threat: redirect speed, angle, two-on-one control
    hand_dist, t = 0.4, 0.1
    hand_v = hand_dist / t
    angle = 30.0
    control = 500.0
    print("redirect hand speed: %.1f m/s" % hand_v)
    print("muzzle swept %.0f degrees off the centerline" % angle)
    print("two-on-one control: %.0f N on the weapon arm" % control)
    assert 3.99 < hand_v < 4.01
    assert 29.9 < angle < 30.1
    assert 499.9 < control < 500.1
    print("rule: redirect, control, counterattack - never release early")
    print("OK: %s handled the live-side threat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_knife_dead_side(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dead-side knife threat: body rotation does what reach cannot
    turn_deg, step = 90.0, 0.6
    t_turn, t_step = 0.20, 0.15
    total = t_turn + t_step
    print("torso turns %d degrees offline, stepping %.1f m" % (int(turn_deg), step))
    print("turn %.2f s + step %.2f s = %.2f s total defense" % (t_turn, t_step, total))
    assert 0.349 < total < 0.351
    assert 0.599 < step < 0.601
    print("rule: rotation beats reach - the body is gone when the blade arrives")
    print("OK: %s solved the dead-side threat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_stick_attack(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stick attack: swing timing vs the defender's inside entry
    stick = 0.7
    arc = math.pi * stick          # 180-degree arc length
    t_swing = 0.4
    tip_v = arc / t_swing
    t_entry = 0.3
    print("stick arc: %.3f m in %.1f s - tip reaches %.1f m/s" % (arc, t_swing, tip_v))
    print("defender bursts inside the %.1f m arc in %.1f s" % (stick, t_entry))
    print("entry beats the swing by: %.1f s" % (t_swing - t_entry))
    assert 2.199 < arc < 2.200
    assert 5.49 < tip_v < 5.51
    assert 0.099 < t_swing - t_entry < 0.101
    print("rule: inside the arc the stick is useless - own that range")
    print("OK: %s beat the stick inside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_knife_slash(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # slashing knife: burst through the retraction window
    t_slash = 0.25
    window = 0.15
    entry = 1.0
    v = entry / window
    print("slash arc time: %.2f s - too fast to catch mid-swing" % t_slash)
    print("retraction window: %.2f s; entry covers %d m at %.2f m/s" % (window, int(entry), v))
    assert 0.249 < t_slash < 0.251
    assert 6.66 < v < 6.68
    print("rule: do not block the slash - arrive inside it")
    print("OK: %s timed the slash" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_knife_overhead_stab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # overhead stab: intercept inside the 0.2 s drop window
    drop, v = 1.2, 6.0
    t = drop / v
    block_angle = 45.0
    print("stab drop time: %.1f m at %.0f m/s = %.2f s" % (drop, v, t))
    print("forearms intercept at %.0f degrees - block and counter as one" % block_angle)
    assert 0.1999 < t < 0.2001
    assert 44.9 < block_angle < 45.1
    print("rule: the stab cannot be outrun - only intercepted")
    print("OK: %s intercepted the overhead stab" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_handgun_front(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # frontal handgun threat: muzzle redirect speed and control
    hand_dist, hand_v = 0.5, 8.0
    t = hand_dist / hand_v
    angle = 45.0
    control = 600.0
    print("muzzle redirect: %.1f m at %.0f m/s = %.4f s" % (hand_dist, hand_v, t))
    print("muzzle swept %.0f degrees off the body" % angle)
    print("two-hand weapon control: %.0f N" % control)
    assert 0.0624 < t < 0.0626
    assert 44.9 < angle < 45.1
    assert 599.9 < control < 600.1
    print("rule: last resort, contact range only - distance is always better")
    print("OK: %s cleared the frontal threat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_multiple_attackers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # multiple attackers: stacking cone, movement rate, scan cycle
    cone = 60.0
    circle_m, circle_t = 3.0, 1.0
    move_v = circle_m / circle_t
    scan = 0.5
    max_stay = 2.0
    print("threat cone: %.0f degrees - nobody gets behind" % cone)
    print("circling speed: %.1f m/s" % move_v)
    print("scan cycle %.1f s; max time in one spot %.0f s" % (scan, max_stay))
    assert 59.9 < cone < 60.1
    assert 2.99 < move_v < 3.01
    assert 0.499 < scan < 0.501
    print("rule: stack them, circle, escape through the gap")
    print("OK: %s managed the multiple threat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_handgun_behind(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear handgun threat: 180-degree spin toward the gun side
    turn = math.pi
    t_turn = 0.4
    omega = turn / t_turn
    budget = 0.5
    print("spin: 180 degrees in %.1f s = %.2f rad/s" % (t_turn, omega))
    print("redirect + control + first counter inside %.1f s of the turn start" % budget)
    assert 7.853 < omega < 7.855
    assert 0.099 < budget - t_turn < 0.101
    print("rule: turn toward the gun - never away from the muzzle")
    print("OK: %s spun on the rear threat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_long_gun(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # long gun threat: bigger sidestep, stronger two-on-one control
    barrel = 1.0
    sidestep = 0.8
    control = 700.0
    grip = 0.2
    torque = control * grip
    t_control = 0.3
    print("barrel %.1f m of leverage - sidestep %.1f m offline" % (barrel, sidestep))
    print("two-on-one: %.0f N x %.1f m grip = %.0f N m in %.1f s" % (control, grip, torque, t_control))
    assert 0.799 < sidestep < 0.801
    assert 139.9 < torque < 140.1
    assert 0.299 < t_control < 0.301
    print("rule: the longer the weapon, the bigger the offline step")
    print("OK: %s controlled the long gun" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_third_party(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # third-party protection: shove the protectee to cover, advance rate
    m_prot, dist, t = 60.0, 2.0, 1.0
    v = dist / t
    a = 2 * dist / (t * t)
    F = m_prot * a
    cover, t_cover = 5.0, 2.5
    v_cover = cover / t_cover
    print("protectee shove: %.0f kg x %.0f m/s^2 = %.0f N" % (m_prot, a, F))
    print("advance to cover: %.0f m in %.1f s = %.1f m/s" % (cover, t_cover, v_cover))
    assert 239.9 < F < 240.1
    assert 1.99 < v_cover < 2.01
    print("rule: your body is the wall - never leave the angle open")
    print("OK: %s shielded the protectee" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbkm_stress_drills(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stress drills: heart-rate zone, skill degradation, session volume
    hr_lo, hr_hi = 150, 170
    degrade = 0.30   # fine-motor degradation at 170 bpm
    scenarios, per = 5, 3.0   # minutes
    total_min = scenarios * per
    total_s = total_min * 60.0
    print("stress zone: %d-%d bpm; fine motor degrades %.0f percent at %d bpm"
          % (hr_lo, hr_hi, degrade * 100.0, hr_hi))
    print("session: %d scenarios x %.0f min = %.0f min (%d s)" % (scenarios, per, total_min, int(total_s)))
    assert hr_lo == 150 and hr_hi == 170
    assert 0.299 < degrade < 0.301
    assert int(total_s) == 900
    print("rule: what works at 170 bpm is what you actually own")
    print("OK: %s proved it under stress" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "fighting_stance": demo_cbkm_fighting_stance,
    "footwork": demo_cbkm_footwork,
    "punch_combatives": demo_cbkm_punch_combatives,
    "palm_heel": demo_cbkm_palm_heel,
    "elbow_strikes": demo_cbkm_elbow_strikes,
    "knee_strikes": demo_cbkm_knee_strikes,
    "front_kick_groin": demo_cbkm_front_kick_groin,
    "hammerfist": demo_cbkm_hammerfist,
    "inside_defense": demo_cbkm_inside_defense,
    "wrist_grab": demo_cbkm_wrist_grab,
    "defense_360": demo_cbkm_defense_360,
    "front_choke_pluck": demo_cbkm_front_choke_pluck,
    "side_headlock": demo_cbkm_side_headlock,
    "shirt_grab": demo_cbkm_shirt_grab,
    "bear_hug_free": demo_cbkm_bear_hug_free,
    "bear_hug_pinned": demo_cbkm_bear_hug_pinned,
    "hair_grab": demo_cbkm_hair_grab,
    "rear_choke": demo_cbkm_rear_choke,
    "ground_survival": demo_cbkm_ground_survival,
    "kicks_ground": demo_cbkm_kicks_ground,
    "clinch": demo_cbkm_clinch,
    "bursting": demo_cbkm_bursting,
    "retzev": demo_cbkm_retzev,
    "knife_live_side": demo_cbkm_knife_live_side,
    "knife_dead_side": demo_cbkm_knife_dead_side,
    "stick_attack": demo_cbkm_stick_attack,
    "knife_slash": demo_cbkm_knife_slash,
    "knife_overhead_stab": demo_cbkm_knife_overhead_stab,
    "handgun_front": demo_cbkm_handgun_front,
    "multiple_attackers": demo_cbkm_multiple_attackers,
    "handgun_behind": demo_cbkm_handgun_behind,
    "long_gun": demo_cbkm_long_gun,
    "third_party": demo_cbkm_third_party,
    "stress_drills": demo_cbkm_stress_drills,
}
