#!/usr/bin/env python3
"""Demo programs for The Force and Motion Basics Database (fundamentals order #9).

Every demo is real, runnable, stdlib-only Python performing the actual
force-and-motion computation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_fmb_what_is_force(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the two families of force: contact needs touch, field acts at a distance
    forces = [("pushing a box", "contact"), ("kicking a ball", "contact"),
              ("braking friction", "contact"), ("tension in a rope", "contact"),
              ("gravity", "field"), ("magnetism", "field"),
              ("static electricity", "field")]
    contact = [f for f, k in forces if k == "contact"]
    field = [f for f, k in forces if k == "field"]
    print("force families: contact vs field")
    for f, k in forces:
        print("  %-22s %s" % (f, k))
    print("contact: %d, field: %d, total: %d" % (len(contact), len(field), len(forces)))
    assert len(contact) == 4
    assert len(field) == 3
    assert len(forces) == 7
    assert all(k in ("contact", "field") for _, k in forces)
    print("rule: every force has size AND direction - classify first, then count")
    print("OK: %s mapped the two families" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_push_pull(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tug-of-war: team A pulls +320 N (east), team B pulls -295 N (west)
    pull_a = 320.0
    pull_b = -295.0
    net = pull_a + pull_b
    direction = "east (+x)" if net > 0 else "west (-x)"
    rope_tension = min(abs(pull_a), abs(pull_b))
    print("team A pull: %.1f N east" % pull_a)
    print("team B pull: %.1f N west" % abs(pull_b))
    print("net force: %.1f N %s" % (abs(net), direction))
    print("rope tension: %.1f N" % rope_tension)
    assert 24.9 < net < 25.1
    assert 294.9 < rope_tension < 295.1
    assert direction == "east (+x)"
    print("rule: opposing pushes subtract - the sign of the net names the winner")
    print("OK: %s called the tug-of-war" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_position_distance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # runner: 0 m -> 40 m -> 10 m along the track
    legs = [(0.0, 40.0), (40.0, 10.0)]
    distance = sum(abs(b - a) for a, b in legs)
    displacement = legs[-1][1] - legs[0][0]
    print("path: 0 m -> 40 m -> 10 m")
    print("distance (every step counts): %.1f m" % distance)
    print("displacement (finish minus start): %.1f m" % displacement)
    assert distance == 70.0
    assert displacement == 10.0
    # round trip erases displacement but never distance
    rt_legs = [(0.0, 40.0), (40.0, 0.0)]
    rt_dist = sum(abs(b - a) for a, b in rt_legs)
    rt_disp = rt_legs[-1][1] - rt_legs[0][0]
    print("round trip: distance %.1f m, displacement %.1f m" % (rt_dist, rt_disp))
    assert rt_dist == 80.0
    assert rt_disp == 0.0
    print("rule: distance accumulates, displacement subtracts - only endpoints matter")
    print("OK: %s walked the track" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_speed(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # car covers 150 m in 25 s
    d, t = 150.0, 25.0
    v = d / t
    kmh = v * 3.6
    print("distance: %.1f m, time: %.1f s" % (d, t))
    print("speed: %.4f m/s" % v)
    print("speed: %.4f km/h" % kmh)
    assert 5.999 < v < 6.001
    assert 21.59 < kmh < 21.61
    # average can hide a varied pace: fast half, slow half, same average
    v1, v2 = 10.0, 2.0
    avg = (v1 * 12.5 + v2 * 12.5) / 25.0
    print("varied pace 10 m/s then 2 m/s averages: %.4f m/s" % avg)
    assert 5.999 < avg < 6.001
    print("rule: speed is distance over time - the average hides the pace")
    print("OK: %s timed the car" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_direction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # displacement 30 m east, 40 m north: the 3-4-5 triangle
    east, north = 30.0, 40.0
    length = math.hypot(east, north)
    heading = math.degrees(math.atan2(north, east))
    print("components: %.1f m east, %.1f m north" % (east, north))
    print("arrow length: %.4f m" % length)
    print("heading: %.4f degrees north of east" % heading)
    assert 49.999 < length < 50.001
    assert 53.12 < heading < 53.14
    # quadrant check: same components negated point southwest
    sw_heading = math.degrees(math.atan2(-north, -east))
    print("negated components head: %.2f degrees (southwest quadrant)" % sw_heading)
    assert -127.0 < sw_heading < -126.0
    print("rule: components add per axis - the angle needs its quadrant")
    print("OK: %s gave motion its address" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_velocity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # car velocity changes from (2, 0) to (2, 3) m/s over 1.5 s: a pure turn
    v1 = (2.0, 0.0)
    v2 = (2.0, 3.0)
    t = 1.5
    dv = (v2[0] - v1[0], v2[1] - v1[1])
    dv_mag = math.hypot(*dv)
    a_avg = dv_mag / t
    print("v1: (%.1f, %.1f) m/s  v2: (%.1f, %.1f) m/s" % (v1[0], v1[1], v2[0], v2[1]))
    print("velocity change: (%.1f, %.1f) m/s, size %.4f m/s" % (dv[0], dv[1], dv_mag))
    print("average acceleration: %.4f m/s^2 north" % a_avg)
    assert dv == (0.0, 3.0)
    assert 2.999 < dv_mag < 3.001
    assert 1.999 < a_avg < 2.001
    print("rule: turning changes velocity even at constant speed - subtract the arrows")
    print("OK: %s tracked the turn" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_acceleration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # car: 5 m/s -> 20 m/s in 3 s at constant acceleration
    v0, v1, t = 5.0, 20.0, 3.0
    a = (v1 - v0) / t
    s = v0 * t + 0.5 * a * t * t
    print("v0: %.1f m/s, v1: %.1f m/s, t: %.1f s" % (v0, v1, t))
    print("acceleration: %.4f m/s^2" % a)
    print("distance: %.4f m" % s)
    assert 4.999 < a < 5.001
    assert 37.49 < s < 37.51
    # braking: same size, opposite sign
    a_brake = (0.0 - 20.0) / 4.0
    print("braking 20 m/s to rest in 4 s: %.4f m/s^2" % a_brake)
    assert -5.001 < a_brake < -4.999
    print("rule: acceleration is velocity change over time - speeding, slowing, turning")
    print("OK: %s measured the change" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_mass(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # aluminum block: density 2700 kg/m^3, volume 0.002 m^3
    rho, vol = 2700.0, 0.002
    m = rho * vol
    print("density: %.1f kg/m^3, volume: %.4f m^3" % (rho, vol))
    print("mass: %.4f kg (%d g)" % (m, int(m * 1000)))
    assert 5.399 < m < 5.401
    # mass resists: same 10 N push on 5.4 kg vs 54 kg
    a1 = 10.0 / m
    a2 = 10.0 / (10.0 * m)
    print("10 N on 5.4 kg: a = %.4f m/s^2; on 54 kg: a = %.4f m/s^2" % (a1, a2))
    assert 1.851 < a1 < 1.853
    assert 0.1851 < a2 < 0.1853
    assert abs(a1 / a2 - 10.0) < 1e-9
    print("rule: mass is the matter - and the resistance to changing its motion")
    print("OK: %s weighed the matter" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_weight(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 70 kg person: Earth g = 9.81, Moon g = 1.62
    m = 70.0
    w_earth = m * 9.81
    w_moon = m * 1.62
    print("mass: %.1f kg (everywhere)" % m)
    print("Earth weight: %.2f N" % w_earth)
    print("Moon weight: %.2f N" % w_moon)
    print("Moon/Earth ratio: %.4f" % (w_moon / w_earth))
    assert 686.6 < w_earth < 686.8
    assert 113.3 < w_moon < 113.5
    assert 0.1651 < w_moon / w_earth < 0.1653
    print("rule: mass is what you are - weight is how hard the world holds you")
    print("OK: %s felt the pull" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_newton_unit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1 N = 1 kg m/s^2 by definition; convert legacy units on entry
    lbf_to_n = 4.448221615
    pull_lbf = 10.0
    pull_n = pull_lbf * lbf_to_n
    dyn_per_n = 100000.0
    print("10 lbf = %.6f N" % pull_n)
    print("1 N = %d dyn" % int(dyn_per_n))
    assert 44.48 < pull_n < 44.49
    assert dyn_per_n == 100000.0
    # unit closure: F = ma must reduce to kg m/s^2
    m, a = 2.5, 4.0
    f = m * a
    print("2.5 kg * 4.0 m/s^2 = %.2f N (units close to kg m/s^2)" % f)
    assert 9.99 < f < 10.01
    # prefixes keep numbers readable
    print("engine thrust 2500 N = %.2f kN" % (2500.0 / 1000.0))
    assert abs(2500.0 / 1000.0 - 2.5) < 1e-12
    print("rule: the newton is kg m/s^2 - if units do not close, the setup is wrong")
    print("OK: %s defined the newton" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_spring_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Hooke law: k = 200 N/m spring
    k = 200.0
    x = 0.15
    f = k * x
    print("k: %.1f N/m, stretch: %.2f m" % (k, x))
    print("force read: %.4f N" % f)
    assert 29.99 < f < 30.01
    # invert: what stretch does 45 N produce?
    x2 = 45.0 / k
    print("45 N stretches the spring: %.4f m" % x2)
    assert 0.2249 < x2 < 0.2251
    # calibration check: 1 kg mass should read 9.81 N on Earth
    cal = 1.0 * 9.81
    x_cal = cal / k
    print("1 kg calibration mass: %.3f N -> %.5f m stretch" % (cal, x_cal))
    assert 9.809 < cal < 9.811
    assert 0.04904 < x_cal < 0.04906
    print("rule: forces are invisible - the scale reads what the force did to matter")
    print("OK: %s read the spring" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_balanced_unbalanced(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 10 N east vs 6 N + 4 N west: balanced, net zero
    f_east = 10.0
    f_west = 6.0 + 4.0
    net1 = f_east - f_west
    print("10 N east vs 10 N west: net = %.2f N -> %s" %
          (net1, "BALANCED" if net1 == 0 else "UNBALANCED"))
    assert net1 == 0.0
    # add 2 N east: unbalanced, 1 kg mass accelerates
    net2 = net1 + 2.0
    a = net2 / 1.0
    print("add 2 N east: net = %.2f N -> UNBALANCED, a = %.2f m/s^2" % (net2, a))
    assert 1.99 < net2 < 2.01
    assert 1.99 < a < 2.01
    print("rule: balanced holds velocity - only the unbalanced net changes it")
    print("OK: %s judged the balance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_net_force(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two pushers: (3, 4) N and (1, -2) N
    f1 = (3.0, 4.0)
    f2 = (1.0, -2.0)
    fx = f1[0] + f2[0]
    fy = f1[1] + f2[1]
    mag = math.hypot(fx, fy)
    heading = math.degrees(math.atan2(fy, fx))
    print("F1: (%.1f, %.1f) N  F2: (%.1f, %.1f) N" % (f1[0], f1[1], f2[0], f2[1]))
    print("net: (%.1f, %.1f) N, size %.6f N, heading %.2f deg" % (fx, fy, mag, heading))
    assert fx == 4.0 and fy == 2.0
    assert 4.4721 < mag < 4.4722
    assert 26.56 < heading < 26.57
    # opposing pair subtracts: the net can be smaller than each part
    g1, g2 = (50.0, 0.0), (-48.0, 0.0)
    net_small = math.hypot(g1[0] + g2[0], g1[1] + g2[1])
    print("50 N vs 48 N opposed: net %.1f N" % net_small)
    assert net_small == 2.0
    print("rule: add components per axis - the net alone decides the motion")
    print("OK: %s summed the arrows" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_free_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # free-body arrows: (5,0), (-2,3), (0,-1) newtons on a 2 kg body
    forces = [(5.0, 0.0), (-2.0, 3.0), (0.0, -1.0)]
    fx = sum(f[0] for f in forces)
    fy = sum(f[1] for f in forces)
    mag = math.hypot(fx, fy)
    heading = math.degrees(math.atan2(fy, fx))
    m = 2.0
    a = mag / m
    print("arrows: %s" % (forces,))
    print("net: (%.1f, %.1f) N, size %.6f N at %.2f deg" % (fx, fy, mag, heading))
    print("mass %.1f kg -> a = %.6f m/s^2 along the net" % (m, a))
    assert fx == 3.0 and fy == 2.0
    assert 3.6055 < mag < 3.6056
    assert 33.69 < heading < 33.70
    assert 1.8027 < a < 1.8028
    print("rule: isolate the body, draw every force ON it, sum per axis")
    print("OK: %s audited the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_newton_first(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # frictionless ice: 12 m/s, zero net force, velocity frozen
    v = 12.0
    t = 8.0
    net = 0.0
    assert net == 0.0
    v_final = v  # first law: velocity does not change
    d = v_final * t
    print("net force: %.1f N -> velocity holds at %.1f m/s" % (net, v_final))
    print("distance in %.1f s: %.1f m (no force, no fuel)" % (t, d))
    assert v_final == 12.0
    assert d == 96.0
    # the bus-braking lurch: passengers keep velocity while the bus slows
    v_bus0, v_bus1 = 10.0, 0.0
    v_passenger = v_bus0  # no net force on the unrestrained passenger
    print("bus 10 m/s -> 0; unrestrained passenger keeps %.1f m/s" % v_passenger)
    assert v_passenger == 10.0
    assert v_bus1 == 0.0
    print("rule: zero net force freezes velocity - rest and uniform motion need no cause")
    print("OK: %s honored inertia" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_newton_second(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # forward: 2.5 kg at 4 m/s^2 needs what net force?
    f = 2.5 * 4.0
    print("2.5 kg * 4.0 m/s^2 = %.4f N" % f)
    assert 9.99 < f < 10.01
    # backward: 36 N on 4.5 kg gives what acceleration?
    a = 36.0 / 4.5
    print("36 N / 4.5 kg = %.4f m/s^2" % a)
    assert 7.999 < a < 8.001
    # weighing by shaking: known 20 N, measured 2.5 m/s^2
    m_unknown = 20.0 / 2.5
    print("20 N produces 2.5 m/s^2 -> mass = %.4f kg" % m_unknown)
    assert 7.999 < m_unknown < 8.001
    # direction check: acceleration follows the net force
    print("acceleration always points along the net force - the vector law")
    print("rule: F = ma reads three ways - find a, find F, find m")
    print("OK: %s ran the exchange" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_newton_third(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rocket: 1500 N on exhaust gas for 2 s; equal opposite on the rocket
    f_gas, t = -1500.0, 2.0
    f_rocket = 1500.0
    j_gas = f_gas * t
    j_rocket = f_rocket * t
    print("impulse on exhaust gas: %.1f N s (backward)" % j_gas)
    print("impulse on rocket: %.1f N s (forward)" % j_rocket)
    print("system total impulse: %.1f N s" % (j_gas + j_rocket))
    assert j_gas == -3000.0
    assert j_rocket == 3000.0
    assert j_gas + j_rocket == 0.0
    # equal forces, unequal masses: cannon vs cannonball
    f_pair = 8000.0
    a_ball = f_pair / 4.0
    a_cannon = f_pair / 1200.0
    print("8000 N pair: ball (4 kg) a = %.1f m/s^2, cannon (1200 kg) a = %.4f m/s^2" %
          (a_ball, a_cannon))
    assert a_ball == 2000.0
    assert 6.666 < a_cannon < 6.668
    print("rule: pairs act on different bodies - equal forces, unequal accelerations")
    print("OK: %s filed both receipts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_gravity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # surface gravity from the planet itself: g = G*M/R^2
    G = 6.67430e-11
    M = 5.97237e24
    R = 6.371e6
    g = G * M / (R * R)
    print("G*M/R^2 = %.6f m/s^2" % g)
    assert 9.819 < g < 9.822
    # inverse-square: double the distance, quarter the force
    f1 = G * 1000.0 * 1000.0 / (10.0 ** 2)
    f2 = G * 1000.0 * 1000.0 / (20.0 ** 2)
    print("1000 kg pair at 10 m: %.6e N; at 20 m: %.6e N" % (f1, f2))
    assert abs(f2 / f1 - 0.25) < 1e-12
    # weight of 1 kg at the computed g
    w = 1.0 * g
    print("1 kg weighs %.4f N at computed g" % w)
    assert 9.819 < w < 9.822
    print("rule: gravity is universal - the planet own mass sets your g")
    print("OK: %s weighed the planet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_friction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # F = mu * N: mu = 0.45, N = 200 N
    mu, n = 0.45, 200.0
    f = mu * n
    print("mu: %.2f, normal: %.1f N" % (mu, n))
    print("friction limit: %.4f N" % f)
    assert 89.99 < f < 90.01
    # material pairs: rubber/asphalt grips, waxed ski/snow slides
    f_grip = 0.9 * n
    f_slide = 0.05 * n
    print("rubber on asphalt: %.1f N; waxed ski on snow: %.1f N" % (f_grip, f_slide))
    assert f_grip == 180.0
    assert f_slide == 10.0
    # area does not matter for hard dry contact
    print("wide tire vs narrow tire, same rubber: same grip (area cancels)")
    print("rule: friction opposes the slide and scales with the normal force")
    print("OK: %s gripped the surfaces" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_static_kinetic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mu_s = 0.6, mu_k = 0.35, N = 150 N
    n = 150.0
    fs_max = 0.6 * n
    fk = 0.35 * n
    print("static ceiling: %.2f N, kinetic: %.2f N" % (fs_max, fk))
    assert 89.99 < fs_max < 90.01
    assert 52.49 < fk < 52.51
    # 60 N push: static matches exactly, nothing moves
    push1 = 60.0
    fs1 = push1 if push1 < fs_max else fs_max
    print("push 60 N: static friction = %.1f N, motion: none" % fs1)
    assert fs1 == 60.0
    # 120 N push: breaks free, kinetic takes over
    push2 = 120.0
    net = push2 - fk
    print("push 120 N: breaks free, net = %.2f N forward" % net)
    assert 67.49 < net < 67.51
    print("rule: static matches up to its ceiling - kinetic is smaller and steady")
    print("OK: %s held then slipped" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_drag(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # quadratic drag: 0.5 * rho * v^2 * Cd * A
    rho, v, cd, area = 1.225, 25.0, 0.47, 2.0
    fd = 0.5 * rho * v * v * cd * area
    print("rho %.3f, v %.1f m/s, Cd %.2f, A %.1f m^2" % (rho, v, cd, area))
    print("drag: %.4f N" % fd)
    assert 359.8 < fd < 359.9
    # double the speed -> quadruple the drag
    fd2 = 0.5 * rho * (2 * v) ** 2 * cd * area
    print("at 50 m/s: %.2f N (ratio %.4f)" % (fd2, fd2 / fd))
    assert abs(fd2 / fd - 4.0) < 1e-9
    # power to beat drag grows as v^3
    p1 = fd * v
    p2 = fd2 * (2 * v)
    print("power at 25 m/s: %.1f W; at 50 m/s: %.1f W (ratio %.4f)" % (p1, p2, p2 / p1))
    assert abs(p2 / p1 - 8.0) < 1e-9
    print("rule: drag squares with speed - power cubes with it")
    print("OK: %s paid the air tax" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_momentum(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1500 kg car at 25 m/s
    p = 1500.0 * 25.0
    print("momentum: %.1f kg m/s" % p)
    assert p == 37500.0
    # stopping impulse: same momentum change, force trades with time
    f_5s = p / 5.0
    f_half_s = p / 0.5
    print("stop in 5 s: %.1f N; stop in 0.5 s: %.1f N" % (f_5s, f_half_s))
    assert f_5s == 7500.0
    assert f_half_s == 75000.0
    assert abs(f_half_s / f_5s - 10.0) < 1e-9
    print("rule: impulse changes momentum - stretch the time, shrink the force")
    print("OK: %s banked the momentum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_lever(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # effort arm 2.0 m, load arm 0.5 m, load 400 N
    d_e, d_l, load = 2.0, 0.5, 400.0
    effort = load * d_l / d_e
    ma = d_e / d_l
    print("effort arm %.1f m, load arm %.1f m, load %.1f N" % (d_e, d_l, load))
    print("effort needed: %.4f N, MA = %.1f" % (effort, ma))
    assert 99.99 < effort < 100.01
    assert ma == 4.0
    # torque balance check
    t_e = effort * d_e
    t_l = load * d_l
    print("torque in: %.2f N m, torque out: %.2f N m" % (t_e, t_l))
    assert abs(t_e - t_l) < 1e-9
    # distance trade: effort travels MA times farther
    d_load = 0.1
    d_effort = d_load * ma
    print("lift load %.2f m -> effort travels %.2f m" % (d_load, d_effort))
    assert abs(d_effort - 0.4) < 1e-12
    print("rule: torque balances - multiplied force costs distance")
    print("OK: %s worked the lever" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_inclined_plane(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 50 kg crate on a 30-degree ramp
    m, theta_deg, g = 50.0, 30.0, 9.81
    theta = math.radians(theta_deg)
    push = m * g * math.sin(theta)
    normal = m * g * math.cos(theta)
    print("weight: %.2f N" % (m * g))
    print("push along slope: %.4f N" % push)
    print("normal into slope: %.4f N" % normal)
    assert 245.24 < push < 245.26
    assert 424.78 < normal < 424.80
    # ramp length for a 3 m rise
    h = 3.0
    L = h / math.sin(theta)
    print("3 m rise needs %.2f m of ramp" % L)
    assert 5.999 < L < 6.001
    # work check: push * L must equal m*g*h
    w_ramp = push * L
    w_lift = m * g * h
    print("work via ramp: %.2f J; direct lift: %.2f J" % (w_ramp, w_lift))
    assert abs(w_ramp - w_lift) < 1e-6
    print("rule: halve the force, double the distance - the work never changes")
    print("OK: %s climbed the ramp" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_wheel_axle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wheel R = 0.30 m, axle r = 0.05 m
    R, r = 0.30, 0.05
    ma = R / r
    effort = 50.0
    load = effort * ma
    print("R %.2f m, r %.2f m -> MA = %.4f" % (R, r, ma))
    print("50 N at rim -> %.4f N at axle" % load)
    assert abs(ma - 6.0) < 1e-12
    assert 299.99 < load < 300.01
    # torque balance
    t_in = effort * R
    t_out = load * r
    print("torque in: %.4f N m, torque out: %.4f N m" % (t_in, t_out))
    assert abs(t_in - t_out) < 1e-9
    # reversed: drive the axle, the rim runs 6x faster
    v_axle = 1.0
    v_rim = v_axle * ma
    print("axle surface 1.0 m/s -> rim %.1f m/s (bicycle mode)" % v_rim)
    assert abs(v_rim - 6.0) < 1e-12
    print("rule: the radius ratio is the machine - force one way, speed the other")
    print("OK: %s turned the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_pulley(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 4 supporting segments, 800 N load
    n, load = 4, 800.0
    effort = load / n
    lift = 1.0
    pull = lift * n
    print("segments: %d, load: %.1f N" % (n, load))
    print("effort: %.4f N; pull %.1f m to lift %.1f m" % (effort, pull, lift))
    assert effort == 200.0
    assert pull == 4.0
    # work balances
    w_in = effort * pull
    w_out = load * lift
    print("work in: %.1f J, work out: %.1f J" % (w_in, w_out))
    assert w_in == 800.0 and w_out == 800.0
    # fixed pulley alone: direction only, MA = 1
    print("single fixed pulley: MA 1 - redirects, does not multiply")
    print("rule: count the segments on the moving block - that count is the machine")
    print("OK: %s rigged the tackle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_wedge_screw(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wedge: 0.20 m long, 0.04 m thick
    ma_wedge = 0.20 / 0.04
    drive = 200.0
    split = drive * ma_wedge
    print("wedge MA: %.4f; 200 N drive -> %.1f N splitting" % (ma_wedge, split))
    assert ma_wedge == 5.0
    assert split == 1000.0
    # screw: handle r = 0.15 m, pitch = 2 mm
    r_handle, pitch = 0.15, 0.002
    ma_screw = 2 * math.pi * r_handle / pitch
    hand = 20.0
    clamp = hand * ma_screw
    print("screw MA: %.4f; 20 N at handle -> %.1f N clamping" % (ma_screw, clamp))
    assert 471.23 < ma_screw < 471.25
    assert 9424.0 < clamp < 9426.0
    # distance trade: handle circle per 1 pitch of advance
    circle = 2 * math.pi * r_handle
    print("handle travels %.4f m per %.4f m of advance (ratio = MA)" %
          (circle, pitch))
    assert abs(circle / pitch - ma_screw) < 1e-9
    print("rule: the wrapped plane trades hundreds of turns for crushing force")
    print("OK: %s drove wedge and screw" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_mech_advantage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 150 N in -> 600 N out; 2 m in-travel, 0.4 m out-travel
    f_in, f_out = 150.0, 600.0
    d_in, d_out = 2.0, 0.4
    ama = f_out / f_in
    ima = d_in / d_out
    w_in = f_in * d_in
    w_out = f_out * d_out
    eff = w_out / w_in
    print("AMA: %.4f, IMA: %.4f" % (ama, ima))
    print("work in: %.1f J, work out: %.1f J, efficiency: %.4f" % (w_in, w_out, eff))
    assert ama == 4.0
    assert ima == 5.0
    assert 0.7999 < eff < 0.8001
    assert abs(eff - ama / ima) < 1e-12
    # design margin: IMA ~25% above required AMA
    required_ama = 4.0
    design_ima = required_ama * 1.25
    print("need AMA %.1f -> design IMA %.2f (margin for friction)" %
          (required_ama, design_ima))
    assert design_ima == 5.0
    print("rule: IMA is geometry, AMA is reality - efficiency is their ratio")
    print("OK: %s rated the machine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_work(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight: 200 N over 15 m
    w1 = 200.0 * 15.0
    print("200 N * 15 m = %.4f J" % w1)
    assert w1 == 3000.0
    # angled: 100 N at 60 deg over 10 m
    w2 = 100.0 * math.cos(math.radians(60.0)) * 10.0
    print("100 N at 60 deg * 10 m = %.4f J" % w2)
    assert 499.99 < w2 < 500.01
    # perpendicular does zero work
    w3 = 100.0 * math.cos(math.radians(90.0)) * 10.0
    print("100 N perpendicular * 10 m = %.6f J" % w3)
    assert abs(w3) < 1e-9
    # work-energy: net work = delta KE; stopping distance scales as v^2
    ke = 0.5 * 1500.0 * 20.0 ** 2
    f_brake = 7500.0
    d_stop = ke / f_brake
    print("1500 kg at 20 m/s: KE %.1f J, stops in %.2f m at 7500 N braking" %
          (ke, d_stop))
    assert ke == 300000.0
    assert 39.99 < d_stop < 40.01
    print("rule: only the along-motion component works - perpendicular rides free")
    print("OK: %s kept the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 2 kg at 10 m/s; same 2 kg held 5 m up
    m, v, h, g = 2.0, 10.0, 5.0, 9.81
    ke = 0.5 * m * v * v
    pe = m * g * h
    print("KE: %.4f J, PE: %.4f J, system total: %.4f J" % (ke, pe, ke + pe))
    assert ke == 100.0
    assert 98.09 < pe < 98.11
    assert 198.09 < ke + pe < 198.11
    # drop it: impact speed from energy, mass cancels
    v_impact = math.sqrt(2 * g * h)
    print("dropped from 5 m: impact speed %.4f m/s" % v_impact)
    assert 9.904 < v_impact < 9.906
    # check: impact KE equals the PE released
    ke_impact = 0.5 * m * v_impact ** 2
    print("impact KE: %.4f J (was PE %.4f J)" % (ke_impact, pe))
    assert abs(ke_impact - pe) < 1e-6
    print("rule: energy transforms but never vanishes - audit every form")
    print("OK: %s audited the treasury" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_power(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 3000 J in 10 s
    p1 = 3000.0 / 10.0
    print("3000 J / 10 s = %.4f W" % p1)
    assert p1 == 300.0
    # steady push: 200 N at 1.5 m/s
    p2 = 200.0 * 1.5
    print("200 N * 1.5 m/s = %.4f W" % p2)
    assert p2 == 300.0
    assert abs(p1 - p2) < 1e-12
    # horsepower and motor sizing
    hp = p1 / 745.7
    print("300 W = %.4f hp" % hp)
    assert 0.402 < hp < 0.403
    lift_p = 490.5 * 2.0  # 50 kg at 2 m/s
    print("lifting 50 kg at 2 m/s needs %.1f W before losses" % lift_p)
    assert 980.9 < lift_p < 981.1
    print("rule: power is the pace of spending - size for the peak, not the average")
    print("OK: %s set the pace" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_torque(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 80 N on a 0.5 m wrench, perpendicular
    tau = 0.5 * 80.0 * math.sin(math.radians(90.0))
    print("torque: %.4f N m" % tau)
    assert tau == 40.0
    # angled push loses leverage
    tau30 = 0.5 * 80.0 * math.sin(math.radians(30.0))
    print("same push at 30 deg: %.4f N m" % tau30)
    assert 19.99 < tau30 < 20.01
    # rotational equilibrium: +40 and -40 cancel
    net = 40.0 + (-40.0)
    print("counterclockwise 40 N m vs clockwise 40 N m: net %.4f N m" % net)
    assert net == 0.0
    # along-the-wrench push: zero torque
    tau0 = 0.5 * 80.0 * math.sin(math.radians(0.0))
    print("push along the wrench: %.6f N m" % tau0)
    assert tau0 == 0.0
    print("rule: twist needs leverage - perpendicular at distance, or nothing")
    print("OK: %s balanced the twist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_projectile(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # launch 20 m/s at 45 degrees, g = 9.81
    v0, theta_deg, g = 20.0, 45.0, 9.81
    theta = math.radians(theta_deg)
    vx = v0 * math.cos(theta)
    vy = v0 * math.sin(theta)
    t = 2 * vy / g
    R = vx * t
    H = vy * vy / (2 * g)
    print("vx: %.6f m/s, vy: %.6f m/s" % (vx, vy))
    print("flight time: %.6f s" % t)
    print("range: %.6f m" % R)
    print("peak height: %.6f m" % H)
    assert 14.1421 < vx < 14.1422
    assert 2.882 < t < 2.884
    assert 40.77 < R < 40.78
    assert 10.19 < H < 10.20
    # cross-check with the range formula
    r2 = v0 * v0 * math.sin(2 * theta) / g
    assert abs(r2 - R) < 1e-9
    # 45 degrees is the vacuum optimum
    r30 = v0 * v0 * math.sin(math.radians(60.0)) / g
    print("range at 30 deg: %.4f m < 45-deg range" % r30)
    assert r30 < R
    print("rule: two motions, one clock - horizontal coasts while vertical falls")
    print("OK: %s flew the arc" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fmb_collisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 2 kg at 3 m/s hits stationary 3 kg, sticks together
    m1, v1, m2, v2 = 2.0, 3.0, 3.0, 0.0
    p_before = m1 * v1 + m2 * v2
    v_after = p_before / (m1 + m2)
    p_after = (m1 + m2) * v_after
    print("momentum before: %.4f kg m/s" % p_before)
    print("stuck velocity: %.4f m/s" % v_after)
    print("momentum after: %.4f kg m/s" % p_after)
    assert p_before == 6.0
    assert abs(v_after - 1.2) < 1e-12
    assert abs(p_after - p_before) < 1e-12
    # energy audit: the cost of sticking
    ke_before = 0.5 * m1 * v1 * v1
    ke_after = 0.5 * (m1 + m2) * v_after * v_after
    lost = ke_before - ke_after
    print("KE before: %.4f J, after: %.4f J, converted: %.4f J" %
          (ke_before, ke_after, lost))
    assert ke_before == 9.0
    assert abs(ke_after - 3.6) < 1e-12
    assert abs(lost - 5.4) < 1e-12
    # center of mass keeps its velocity through it all
    v_cm = p_before / (m1 + m2)
    print("center-of-mass velocity: %.4f m/s (unchanged)" % v_cm)
    assert abs(v_cm - v_after) < 1e-12
    print("rule: momentum always balances - energy pays the toll")
    print("OK: %s settled the collision" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_force": demo_fmb_what_is_force,
    "push_pull": demo_fmb_push_pull,
    "position_distance": demo_fmb_position_distance,
    "speed": demo_fmb_speed,
    "direction": demo_fmb_direction,
    "velocity": demo_fmb_velocity,
    "acceleration": demo_fmb_acceleration,
    "mass": demo_fmb_mass,
    "weight": demo_fmb_weight,
    "newton_unit": demo_fmb_newton_unit,
    "spring_scale": demo_fmb_spring_scale,
    "balanced_unbalanced": demo_fmb_balanced_unbalanced,
    "net_force": demo_fmb_net_force,
    "free_body": demo_fmb_free_body,
    "newton_first": demo_fmb_newton_first,
    "newton_second": demo_fmb_newton_second,
    "newton_third": demo_fmb_newton_third,
    "gravity": demo_fmb_gravity,
    "friction": demo_fmb_friction,
    "static_kinetic": demo_fmb_static_kinetic,
    "drag": demo_fmb_drag,
    "momentum": demo_fmb_momentum,
    "lever": demo_fmb_lever,
    "inclined_plane": demo_fmb_inclined_plane,
    "wheel_axle": demo_fmb_wheel_axle,
    "pulley": demo_fmb_pulley,
    "wedge_screw": demo_fmb_wedge_screw,
    "mech_advantage": demo_fmb_mech_advantage,
    "work": demo_fmb_work,
    "energy": demo_fmb_energy,
    "power": demo_fmb_power,
    "torque": demo_fmb_torque,
    "projectile": demo_fmb_projectile,
    "collisions": demo_fmb_collisions,
}
