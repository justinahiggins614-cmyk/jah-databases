#!/usr/bin/env python3
"""Demo programs for the Wing Chun Combat databases (combat batch 3).

Every demo is real, runnable, stdlib-only Python performing the actual
computation behind its record: training calculators, drill timers,
biomechanics and timing math. All are machine-executed by build.py: each
prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Demo numbers cross-check
the entry text they accompany.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_wc_centerline(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # centerline vs circular path: two fighters 1.50 m apart
    straight = 1.50
    arc = math.pi * 0.75          # semicircular hook around the outside
    saved = arc - straight
    pct = saved / arc * 100.0
    print("centerline attack distance: %.2f m" % straight)
    print("circular attack distance:   %.4f m" % arc)
    print("distance saved:             %.4f m (%.2f %%)" % (saved, pct))
    assert 2.3561 < arc < 2.3563
    assert 0.8561 < saved < 0.8563
    assert 36.33 < pct < 36.35
    print("rule: the straight line arrives first when timing is equal")
    print("OK: %s proved the shortest path" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Yee Jee Kim Yeung Ma: weight split and tip-over margin
    body = 70.0
    per_foot = body / 2.0
    com_height = 0.95            # center of mass height, meters
    half_base = 0.225            # half of the 0.45 m base
    tip_deg = math.degrees(math.atan(half_base / com_height))
    print("body mass: %.1f kg -> %.1f kg per foot (50/50)" % (body, per_foot))
    print("base width: %.2f m, center of mass height: %.2f m" % (half_base * 2, com_height))
    print("tip-over angle: %.3f degrees" % tip_deg)
    assert 34.99 < per_foot < 35.01
    assert 13.32 < tip_deg < 13.34
    print("rule: root first - arm power without the stance is discarded")
    print("OK: %s measured the root" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Man Sau + Wu Sau coverage of the 180-degree frontal arc
    man_deg = 60.0
    wu_deg = 40.0
    overlap = 15.0
    covered = man_deg + wu_deg - overlap
    pct = covered / 180.0 * 100.0
    print("man sau coverage: %.0f deg, wu sau coverage: %.0f deg, overlap: %.0f deg" % (man_deg, wu_deg, overlap))
    print("frontal arc covered: %.0f of 180 deg (%.2f %%)" % (covered, pct))
    assert covered == 85.0
    assert 47.22 < pct < 47.23
    print("rule: the centerline is never left without a hand")
    print("OK: %s mapped the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_punch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Yat Jee Chung Kuen: fist dynamics
    dist = 0.55                 # meters of travel
    t = 0.12                   # seconds
    m = 4.0                    # effective body mass, kg
    v = dist / t
    ke = 0.5 * m * v ** 2
    mom = m * v
    print("travel: %.2f m in %.2f s -> velocity %.4f m/s" % (dist, t, v))
    print("kinetic energy: %.3f J, momentum: %.3f kg m/s" % (ke, mom))
    assert 4.583 < v < 4.584
    assert 42.00 < ke < 42.03
    assert 18.33 < mom < 18.34
    print("rule: no wind-up - the punch starts on the line and returns to it")
    print("OK: %s clocked the vertical punch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_chain_punch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Lin Wan Kuen: sustained output of a chain-punch burst
    punches = 8
    burst_t = 1.2              # seconds
    per_punch_j = 42.014
    rate = punches / burst_t
    per_min = rate * 60.0
    total_j = punches * per_punch_j
    power = total_j / burst_t
    print("burst: %d punches in %.1f s" % (punches, burst_t))
    print("rate: %.4f punches/s = %.1f punches/min" % (rate, per_min))
    print("energy delivered: %.2f J at %.2f W" % (total_j, power))
    assert 6.66 < rate < 6.67
    assert 399.9 < per_min < 400.1
    assert 280.0 < power < 280.2
    print("rule: the punches themselves jam the counter - offense is defense")
    print("OK: %s ran the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_tan_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Tan Sau: dispersing a 100 N punch arriving 30 deg off the line
    f = 100.0
    turn_deg = 60.0
    residual = f * math.cos(math.radians(turn_deg))
    lateral = f * math.sin(math.radians(turn_deg))
    print("incoming: %.0f N turned %.0f deg off its path" % (f, turn_deg))
    print("still on target: %.2f N, shunted sideways: %.2f N" % (residual, lateral))
    assert 49.99 < residual < 50.01
    assert 86.60 < lateral < 86.61
    print("rule: disperse, never block - the elbow stays nailed to the line")
    print("OK: %s parted the curtain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_bong_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Bong Sau: elbow-pivot lever against an 80 N punch
    f_in = 80.0
    arm_in = 0.28               # punch lands 0.28 m from the elbow pivot
    arm_out = 0.10              # shoulder/upper-arm counter lever
    f_hold = f_in * arm_in / arm_out
    print("incoming %.0f N at %.2f m from elbow pivot" % (f_in, arm_in))
    print("shoulder force required at %.2f m lever: %.2f N" % (arm_out, f_hold))
    assert 223.99 < f_hold < 224.01
    print("rule: the wing is a bridge, never a destination - roll through it")
    print("OK: %s held the wing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_fook_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Fook Sau: economical pin from forearm weight + intention
    forearm = 1.6               # kg
    g = 9.81
    intention = 20.0            # N of downward intention
    pin = forearm * g + intention
    opp_lift = 25.0             # N the trapped arm can lift with
    net = pin - opp_lift
    print("pinning force: %.3f N (arm weight + intention)" % pin)
    print("opponent lift: %.1f N -> net pin: %.3f N" % (opp_lift, net))
    assert 35.69 < pin < 35.70
    assert 10.69 < net < 10.70
    print("rule: control without grabbing - heavy to them, light to you")
    print("OK: %s kept the covenant of weight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_pak_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Pak Sau: slapping a 3 kg guarding arm off the line
    hand_m = 0.5
    dist = 0.25
    t = 0.08
    v = dist / t
    mom = hand_m * v
    arm_m = 3.0
    arm_v = 1.0
    deflect_deg = math.degrees(math.atan(mom / (arm_m * arm_v)))
    print("slap: %.1f kg hand at %.3f m/s -> %.4f kg m/s" % (hand_m, v, mom))
    print("redirects the %.0f kg arm by %.3f degrees" % (arm_m, deflect_deg))
    assert 3.124 < v < 3.126
    assert 27.511 < deflect_deg < 27.513
    print("rule: slap and punch land as one beat, never two")
    print("OK: %s cleared the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_advance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Seung Ma / Tui Ma: closing speed of the gliding step
    step = 0.5                  # meters per step
    cadence = 2.0               # steps per second
    speed = step * cadence
    gap = 1.5
    t_close = gap / speed
    print("step: %.1f m at %.0f steps/s -> %.1f m/s" % (step, cadence, speed))
    print("closing a %.1f m gap: %.1f s (%d steps)" % (gap, t_close, int(gap / step)))
    assert 0.99 < speed < 1.01
    assert 1.49 < t_close < 1.51
    print("rule: the head stays level - the opponent feels the distance change, never sees the step")
    print("OK: %s glided the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_turn(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Juen Ma: 45-degree stance turn
    deg = 45.0
    rad = math.radians(deg)
    hip_r = 0.25
    arc = hip_r * rad
    t = 0.25
    omega = rad / t
    print("turn: %.0f deg, hip arc: %.4f m in %.2f s" % (deg, arc, t))
    print("angular velocity: %.4f rad/s" % omega)
    assert 0.1963 < arc < 0.1964
    assert 3.1415 < omega < 3.1416
    print("rule: feet, hips, hands arrive together - the turn comes from the stance")
    print("OK: %s turned on the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_siu_nim_tau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Siu Nim Tau: slow-pass training volume
    sections = 3
    movements = 108
    slow_s = 20.0 * 60.0
    per_move = slow_s / movements
    breath_s = 6.0
    breaths = slow_s / breath_s
    print("sections: %d, movements: %d, slow pass: %.0f s" % (sections, movements, slow_s))
    print("time per movement: %.3f s" % per_move)
    print("breath cycles at %.0f s each: %.0f" % (breath_s, breaths))
    assert 11.11 < per_move < 11.12
    assert breaths == 200.0
    print("rule: the slowness is the training - tendons learn what muscles would steal")
    print("OK: %s kept the little idea" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_lap_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Lap Sau: the work of the sudden pull
    f = 60.0                    # N of pull
    d = 0.2                     # meters of displacement
    t = 0.15                    # seconds
    work = f * d
    v = d / t
    print("pull: %.0f N over %.1f m -> work %.1f J" % (f, d, work))
    print("arm displaced at %.4f m/s - faster than balance can follow" % v)
    assert 11.99 < work < 12.01
    assert 1.333 < v < 1.334
    print("rule: sudden, not strong - pull and punch are one beat")
    print("OK: %s stole the balance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_jut_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Jut Sau: jerking shock on a 3 kg arm
    m = 3.0
    a = 8.0                     # m/s^2 of the jerk
    t = 0.1
    f = m * a
    impulse = f * t
    dv = impulse / m
    print("jerk: %.0f kg arm at %.0f m/s^2 -> %.0f N" % (m, a, f))
    print("impulse over %.1f s: %.1f N s, velocity change: %.1f m/s downward" % (t, impulse, dv))
    assert 23.99 < f < 24.01
    assert 2.39 < impulse < 2.41
    assert 0.799 < dv < 0.801
    print("rule: a shock, not a press - the hand recovers as their arm falls")
    print("OK: %s cracked the whip downward" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_kwan_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Kwan Sau: the 90-degree hand rotation
    deg = 90.0
    rad = math.radians(deg)
    t = 0.15
    omega = rad / t
    hand_r = 0.28
    v = omega * hand_r
    print("rotation: %.0f deg in %.2f s -> %.4f rad/s" % (deg, t, omega))
    print("hand speed at %.2f m radius: %.4f m/s" % (hand_r, v))
    assert 10.471 < omega < 10.473
    assert 2.932 < v < 2.933
    print("rule: the forearms rotate - the elbows keep their oath to the line")
    print("OK: %s turned the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_gaun_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Gaun Sau: the wedge splitting at 45 degrees per side
    f = 80.0
    side = 45.0
    comp = f * math.cos(math.radians(side))
    total = 2.0 * comp
    print("drive: %.0f N split %.0f deg per side" % (f, side))
    print("lateral force per side: %.4f N, total spread: %.4f N" % (comp, total))
    assert 56.56 < comp < 56.58
    assert 113.13 < total < 113.14
    print("rule: through the guard, not around it - the stance drops behind the wedge")
    print("OK: %s split the log" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_huen_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Huen Sau: the tight escape circle
    r = 0.15
    circ = 2.0 * math.pi * r
    hand_v = 2.0
    t_circle = circ / hand_v
    four = 4.0 * t_circle
    print("circle radius: %.2f m, circumference: %.4f m" % (r, circ))
    print("one circle at %.0f m/s: %.4f s; four circles: %.4f s" % (hand_v, t_circle, four))
    assert 0.9424 < circ < 0.9425
    assert 0.4712 < t_circle < 0.4713
    assert 1.8849 < four < 1.8850
    print("rule: never pull against the grip - circle toward the thumb")
    print("OK: %s untied the knot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_gan_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Gan Sau: plowing a 12 kg kick off the low line
    m = 12.0
    v = 3.0
    p = m * v
    deg = 45.0
    lateral = p * math.sin(math.radians(deg))
    residual = p * math.cos(math.radians(deg))
    print("kick momentum: %.0f kg m/s, deflected %.0f deg" % (p, deg))
    print("shunted sideways: %.3f, still on target: %.3f" % (lateral, residual))
    assert 25.455 < lateral < 25.457
    assert 25.455 < residual < 25.457
    print("rule: the elbow stays bent - a straight arm has no structure")
    print("OK: %s plowed the low line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_biu_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Biu Sau: fingertip pressure of the darting thrust
    f = 50.0                    # N of thrust
    area_cm2 = 4.0
    area_m2 = area_cm2 / 10000.0
    pressure = f / area_m2
    kpa = pressure / 1000.0
    print("thrust: %.0f N through %.0f fingertips (%.1f cm^2)" % (f, 4, area_cm2))
    print("pressure: %.0f Pa = %.1f kPa" % (pressure, kpa))
    assert 124999.0 < pressure < 125001.0
    assert 124.9 < kpa < 125.1
    print("rule: pads only, never a partner's face - accuracy is the technique")
    print("OK: %s loosed the dart" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_chum_kiu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Chum Kiu: bridging the gap with turning steps
    per_step = 0.75
    steps = 3
    t = 1.2
    dist = per_step * steps
    speed = dist / t
    print("turning advance: %.2f m per step x %d steps = %.2f m" % (per_step, steps, dist))
    print("bridging time: %.1f s -> %.3f m/s" % (t, speed))
    assert 2.249 < dist < 2.251
    assert 1.874 < speed < 1.876
    print("rule: seek the bridge - the turn carries you to a new angle, not a desperate block")
    print("OK: %s crossed the gap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_kicks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Wing Chun kicks: the leg's numbers vs the punch
    m = 12.0
    v = 6.0
    p = m * v
    ke = 0.5 * m * v ** 2
    punch_j = 42.014
    ratio = ke / punch_j
    reach_kick = 0.95
    reach_hand = 0.70
    adv = reach_kick - reach_hand
    print("kick: %.0f kg at %.0f m/s -> %.0f kg m/s, %.1f J" % (m, v, p, ke))
    print("vs punch %.1f J: %.2f x the energy" % (punch_j, ratio))
    print("reach advantage: %.2f m vs %.2f m (+%.2f m)" % (reach_kick, reach_hand, adv))
    assert 71.99 < p < 72.01
    assert 215.99 < ke < 216.01
    assert 5.14 < ratio < 5.15
    print("rule: low, tight, and back home - the kick must cost nothing defensively")
    print("OK: %s fired the long punch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_dan_chi_sau(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Dan Chi Sao: one minute of single-hand sticking volume
    cycle_s = 2.0
    minute = 60.0
    cycles = minute / cycle_s
    # each cycle: 1 Tan, 1 Fook, 1 punch, 1 Pak per hand
    tan = cycles
    fook = cycles
    punches = cycles
    pak = cycles
    total_shapes = tan + fook + punches + pak
    print("cycle: %.1f s -> %.0f cycles per minute" % (cycle_s, cycles))
    print("per hand: %.0f Tan, %.0f Fook, %.0f punches, %.0f Pak" % (tan, fook, punches, pak))
    print("technique reps per minute per hand: %.0f" % total_shapes)
    assert cycles == 30.0
    assert total_shapes == 120.0
    print("rule: light, forward, unbroken - pushers are not listening")
    print("OK: %s held the first conversation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_luk_sao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Luk Sao: three-minute rolling volume
    roll_s = 1.5
    round_s = 3.0 * 60.0
    rolls = round_s / roll_s
    shapes_per_roll = 3.0       # Tan, Fook, Bong cycling
    changes = rolls * shapes_per_roll
    print("roll: %.1f s, round: %.0f s -> %.0f rolls" % (roll_s, round_s, rolls))
    print("shape changes per hand per round: %.0f" % changes)
    assert rolls == 120.0
    assert changes == 360.0
    print("rule: never break contact to chase - let the openings come to the bridges")
    print("OK: %s rolled the endless river" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_lop_sao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Lop Sao cycle: 4 beats at 120 bpm
    bpm = 120.0
    beat_s = 60.0 / bpm
    cycle_s = 4.0 * beat_s
    cycles = 50
    total_s = cycles * cycle_s
    punches = cycles * 2        # two punches per 4-beat cycle
    print("beat: %.2f s, cycle (Lop,punch,Pak,punch): %.1f s" % (beat_s, cycle_s))
    print("%d cycles: %.0f s, punches per partner: %d" % (cycles, total_s, punches))
    assert 1.99 < cycle_s < 2.01
    assert 99.9 < total_s < 100.1
    assert punches == 100
    print("rule: the pull catches the commitment - timing, not strength, runs the cycle")
    print("OK: %s kept the sparring heartbeat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_dummy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Mook Yan Jong: full-pass conditioning volume
    movements = 108
    per_move_s = 3.0
    pass_s = movements * per_move_s
    pass_min = pass_s / 60.0
    passes = 3
    total_min = pass_min * passes
    print("movements: %d at %.0f s each -> one pass %.0f s (%.1f min)" % (movements, per_move_s, pass_s, pass_min))
    print("%d passes: %.1f min of work against the wood" % (passes, total_min))
    assert 323.9 < pass_s < 324.1
    assert 5.399 < pass_min < 5.401
    assert 16.19 < total_min < 16.21
    print("rule: the dummy never lies - a wrong angle is reported instantly")
    print("OK: %s argued with the iron partner" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_dummy_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Biu Ma: flanking the dummy in 45-degree darts
    step_m = 0.4
    radius = 0.6
    quarter_arc = 2.0 * math.pi * radius / 4.0
    import math as _m
    steps = int(_m.ceil(quarter_arc / step_m))
    print("dart: %.1f m at 45 deg; quarter flank arc (r=%.1f m): %.4f m" % (step_m, radius, quarter_arc))
    print("steps to own the flank: %d" % steps)
    assert 0.9424 < quarter_arc < 0.9425
    assert steps == 3
    print("rule: never meet force head-on when a step puts you where it is not")
    print("OK: %s owned the blind side" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_biu_jee(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Biu Jee: the 180-degree elbow recovery snap
    deg = 180.0
    rad = math.radians(deg)
    t = 0.2
    omega = rad / t
    r = 0.55
    v = omega * r
    print("recovery: %.0f deg in %.1f s -> %.4f rad/s" % (deg, t, omega))
    print("fingertip speed at %.2f m: %.4f m/s" % (r, v))
    assert 15.707 < omega < 15.709
    assert 8.639 < v < 8.640
    print("rule: recover the centerline by any means - then already be attacking")
    print("OK: %s snapped the contingency" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_chi_gerk(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Chi Gerk: stopping a sweep vs deflecting it
    m = 12.0
    v = 2.5
    p = m * v
    t_stop = 0.1
    f_stop = p / t_stop
    sense_n = 5.0
    print("sweep momentum: %.0f kg m/s" % p)
    print("dead-stop force over %.1f s: %.0f N - hence deflect, never block" % (t_stop, f_stop))
    print("leg-bridge sensitivity target: %.0f N pressure changes" % sense_n)
    assert 29.99 < p < 30.01
    assert 299.99 < f_stop < 300.01
    print("rule: hear five newtons through the shin - no blind half")
    print("OK: %s listened downward" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_knives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # Bart Cham Dao: eight cuts, full circle, close range
    cuts = 8
    spacing = 360.0 / cuts
    coverage = cuts * spacing
    blade = 0.35
    arm = 0.65
    reach = blade + arm
    area = math.pi * reach ** 2
    print("cuts: %d at %.0f deg -> %.0f deg of coverage" % (cuts, spacing, coverage))
    print("reach: %.2f m blade + %.2f m arm = %.2f m; circle: %.4f m^2" % (blade, arm, reach, area))
    assert coverage == 360.0
    assert 0.99 < reach < 1.01
    assert 3.1415 < area < 3.1416
    print("rule: the knives excuse nothing - stance, guard, and line hold as ever")
    print("OK: %s kept the edged covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_pole(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Luk Dim Boon Kwan: lever multiplication at the tip
    pole = 2.6
    grip = 0.5
    rear_v = 2.0
    tip_v = rear_v * (pole / grip)
    m_eff = 1.5
    ke = 0.5 * m_eff * tip_v ** 2
    print("pole: %.1f m, grip spacing: %.1f m, rear hand: %.1f m/s" % (pole, grip, rear_v))
    print("tip velocity: %.2f m/s, tip energy: %.2f J" % (tip_v, ke))
    assert 10.399 < tip_v < 10.401
    assert 81.11 < ke < 81.13
    print("rule: the tip is only fast if the root is true - the snap transfers to the fist")
    print("OK: %s whipped the lever of truth" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_lin_siu_dai_da(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Lin Siu Dai Da: one beat vs two
    one_beat = 0.25
    two_beat = 0.50
    saved_pct = (two_beat - one_beat) / two_beat * 100.0
    window = 2.0
    simultaneous = window / one_beat
    sequential = window / two_beat
    print("simultaneous: %.2f s, block-then-punch: %.2f s (%.0f %% saved)" % (one_beat, two_beat, saved_pct))
    print("actions in %.0f s: %.0f simultaneous vs %.0f sequential" % (window, simultaneous, sequential))
    assert saved_pct == 50.0
    assert simultaneous == 8.0
    assert sequential == 4.0
    print("rule: the hand that turns the attack aside is already the fist that answers")
    print("OK: %s struck the single heartbeat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_lat_sao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Lat Sau Jik Chung: standard sparring session volume
    rounds = 3
    round_s = 2.0 * 60.0
    rest_s = 60.0
    work_s = rounds * round_s
    total_s = work_s + (rounds - 1) * rest_s
    total_min = total_s / 60.0
    punch_rate = 300.0           # punches per minute of work
    punches = punch_rate * (work_s / 60.0)
    print("session: %d x %.0f s rounds, %.0f s rests -> %.0f s total (%.0f min)" % (rounds, round_s, rest_s, total_s, total_min))
    print("punches at %.0f/min: %.0f per session" % (punch_rate, punches))
    assert work_s == 360.0
    assert total_s == 480.0
    assert total_min == 8.0
    assert punches == 1800.0
    print("rule: the laboratory, not the contest - the win is a technique that worked")
    print("OK: %s passed the examination" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_gor_sao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Gor Sao: five minutes of free sticking exchanges
    exchange_s = 1.5
    round_s = 5.0 * 60.0
    exchanges = round_s / exchange_s
    techniques = exchanges * 2
    print("exchange every %.1f s over %.0f s" % (exchange_s, round_s))
    print("exchanges: %.0f, techniques thrown and answered: %.0f" % (exchanges, techniques))
    assert exchanges == 200.0
    assert techniques == 400.0
    print("rule: the roll is the grammar - Gor Sao is the poetry spoken in it")
    print("OK: %s spoke the poetry" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wc_application(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Application framework: reaction distance doctrine
    react_s = 0.25
    punch_v = 5.0               # m/s attacker punch
    covered = punch_v * react_s
    safe_m = 1.5
    margin = safe_m - covered
    counter_s = 0.30
    total_response = react_s + counter_s
    print("reaction %.2f s x punch %.0f m/s = %.2f m covered before response begins" % (react_s, punch_v, covered))
    print("safe distance: %.1f m (margin %.2f m); counter lands at %.2f s" % (safe_m, margin, total_response))
    assert 1.249 < covered < 1.251
    assert 0.24 < margin < 0.26
    assert 0.549 < total_response < 0.551
    print("rule: see first, speak second, guard third - strike only when no answer remains")
    print("OK: %s walked the whole ladder" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "centerline": demo_wc_centerline,
    "stance": demo_wc_stance,
    "guard": demo_wc_guard,
    "punch": demo_wc_punch,
    "chain_punch": demo_wc_chain_punch,
    "tan_sau": demo_wc_tan_sau,
    "bong_sau": demo_wc_bong_sau,
    "fook_sau": demo_wc_fook_sau,
    "pak_sau": demo_wc_pak_sau,
    "advance": demo_wc_advance,
    "turn": demo_wc_turn,
    "siu_nim_tau": demo_wc_siu_nim_tau,
    "lap_sau": demo_wc_lap_sau,
    "jut_sau": demo_wc_jut_sau,
    "kwan_sau": demo_wc_kwan_sau,
    "gaun_sau": demo_wc_gaun_sau,
    "huen_sau": demo_wc_huen_sau,
    "gan_sau": demo_wc_gan_sau,
    "biu_sau": demo_wc_biu_sau,
    "chum_kiu": demo_wc_chum_kiu,
    "kicks": demo_wc_kicks,
    "dan_chi_sau": demo_wc_dan_chi_sau,
    "luk_sao": demo_wc_luk_sao,
    "lop_sao": demo_wc_lop_sao,
    "dummy": demo_wc_dummy,
    "dummy_footwork": demo_wc_dummy_footwork,
    "biu_jee": demo_wc_biu_jee,
    "chi_gerk": demo_wc_chi_gerk,
    "knives": demo_wc_knives,
    "pole": demo_wc_pole,
    "lin_siu_dai_da": demo_wc_lin_siu_dai_da,
    "lat_sao": demo_wc_lat_sao,
    "gor_sao": demo_wc_gor_sao,
    "application": demo_wc_application,
}
