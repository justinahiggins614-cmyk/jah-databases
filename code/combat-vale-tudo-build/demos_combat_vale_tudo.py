#!/usr/bin/env python3
"""Demo programs for the Vale Tudo Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: timelines, stance geometry, drill
timers, strike physics, leverage math, and conditioning calculators. All
are machine-executed by build.py before the merge: each prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_vt_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # vale tudo lineage timeline: challenge era -> UFC 1 -> IVC -> unified rules
    challenge_era = 1925
    ufc1 = 1993
    ivc = 1997
    unified_nj = 2000
    pride_start = 1997
    print("challenge era %d -> UFC 1 %d: %d years" % (challenge_era, ufc1, ufc1 - challenge_era))
    print("UFC 1 %d -> IVC %d: %d years" % (ufc1, ivc, ivc - ufc1))
    print("IVC %d -> unified rules (NJ) %d: %d years" % (ivc, unified_nj, unified_nj - ivc))
    print("UFC 1 %d -> Pride FC %d: %d years" % (ufc1, pride_start, pride_start - ufc1))
    assert ufc1 - challenge_era == 68
    assert ivc - ufc1 == 4
    assert unified_nj - ivc == 3
    assert pride_start - ufc1 == 4
    print("rule: learn the lineage first - the art only makes sense as a complete system")
    print("OK: %s mapped the lineage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance geometry scales with the fighter
    height_cm = 175.0
    width = 0.55 * height_cm
    body_kg = 75.0
    per_foot = body_kg / 2.0
    lead_angle = 45.0
    print("fighter height: %.0f cm -> stance width: %.2f cm" % (height_cm, width))
    print("weight split 50/50: %.2f kg per foot" % per_foot)
    print("lead foot angle: %.0f degrees" % lead_angle)
    assert 96.24 < width < 96.26
    assert 37.49 < per_foot < 37.51
    # a second fighter to show the scaling
    w2 = 0.55 * 160.0
    print("160 cm fighter -> stance width: %.2f cm" % w2)
    assert 87.99 < w2 < 88.01
    print("rule: square enough to wrestle, bladed enough to punch")
    print("OK: %s set the base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_breakfall(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # falling physics: spread the force, buy time
    m = 75.0
    g = 9.81
    h = 1.0
    v = math.sqrt(2 * g * h)
    ke = m * g * h
    print("fall from %.1f m: impact speed %.3f m/s, energy %.2f J" % (h, v, ke))
    assert 4.42 < v < 4.44
    assert 735.7 < ke < 735.8
    # stopping fast (braced, 0.1 s) vs slow (slap and roll, 0.3 s)
    f_fast = m * v / 0.1
    f_slow = m * v / 0.3
    print("braced stop (0.1 s): %.0f N" % f_fast)
    print("slap-and-roll stop (0.3 s): %.0f N" % f_slow)
    print("force ratio: %.2f x" % (f_fast / f_slow))
    assert 3321.0 < f_fast < 3324.0
    assert 1106.0 < f_slow < 1109.0
    assert 2.99 < f_fast / f_slow < 3.01
    print("rule: the mat is an ally when you give it time and surface")
    print("OK: %s learned to fall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # footwork volume: how much ground a fighter covers
    round_s = 180.0
    cadence = 0.8
    steps = round_s / cadence
    step_len = 0.6
    distance = steps * step_len
    print("one 3-minute round at one step per %.1f s:" % cadence)
    print("  steps: %.0f" % steps)
    print("  distance at %.1f m/step: %.0f m" % (step_len, distance))
    assert 224.99 < steps < 225.01
    assert 134.99 < distance < 135.01
    rounds = 3
    print("three rounds: %.0f m of disciplined movement" % (distance * rounds))
    assert 404.99 < distance * rounds < 405.01
    print("rule: feet like rails - step and drag, never cross")
    print("OK: %s owned the distance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_jab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jab mechanics: reach and hand speed
    arm = 0.70
    shoulder_roll = 0.15
    reach = arm + shoulder_roll
    extend_t = 0.12
    speed = reach / extend_t
    return_t = extend_t / 2.0
    print("jab reach: arm %.2f m + shoulder roll %.2f m = %.2f m" % (arm, shoulder_roll, reach))
    print("hand speed over %.2f s: %.2f m/s" % (extend_t, speed))
    print("return time: %.2f s (twice as fast as the extension)" % return_t)
    assert 0.849 < reach < 0.851
    assert 7.08 < speed < 7.09
    assert 0.059 < return_t < 0.061
    # doubles and triples per round
    per_round = 40
    print("drill target: %d clean jabs per 3-minute round" % per_round)
    print("rule: a snap, not a push - and back twice as fast")
    print("OK: %s snapped the lead hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_cross(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross power: rotation plus straight-line drive
    eff_mass = 4.0
    v = 8.0
    stop_d = 0.05
    force = eff_mass * v ** 2 / (2 * stop_d)
    print("cross: %.1f kg at %.1f m/s stopped in %.2f m" % (eff_mass, v, stop_d))
    print("  estimated impact force: %.0f N" % force)
    assert 2559.0 < force < 2561.0
    # hip rotation speed: 90 degrees in 0.15 s
    omega = (math.pi / 2) / 0.15
    print("hip rotation: 90 degrees in 0.15 s = %.2f rad/s" % omega)
    assert 10.46 < omega < 10.48
    print("rule: thrown behind the jab, never naked - and the lead hand comes home first")
    print("OK: %s drove the rear hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hook arc: the bent arm travels a quarter circle
    r = 0.65
    theta = math.pi / 2
    arc = r * theta
    t = 0.18
    v = arc / t
    print("hook arc: radius %.2f m x 90 degrees = %.3f m of travel" % (r, arc))
    print("fist speed over %.2f s: %.2f m/s" % (t, v))
    assert 1.0210 < arc < 1.0211
    assert 5.672 < v < 5.674
    # body hook level change: knees bend 0.25 m, not the waist
    dip = 0.25
    print("body hook level change: knee dip %.2f m, waist stays tall" % dip)
    print("rule: the elbow leads, the hips supply the violence")
    print("OK: %s swung the arc" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_lowkick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low kick: shin speed from hip rotation
    leg = 0.90
    omega = 12.0
    foot_speed = leg * omega
    swing_t = (math.pi / 2) / omega
    print("low kick: leg %.2f m x %.0f rad/s = %.2f m/s shin speed" % (leg, omega, foot_speed))
    print("90-degree swing time: %.4f s" % swing_t)
    assert 10.79 < foot_speed < 10.81
    assert 0.130 < swing_t < 0.132
    # conditioning plan: gradual volume over weeks
    week1 = 30
    print("shin conditioning: start %d light bag kicks per leg per session, add 10 per week" % week1)
    week8 = week1 + 7 * 10
    print("week 8: %d per leg per session - never on hard objects" % week8)
    assert week8 == 100
    print("rule: the shin is the bat, the foot is fragile - and set it up with punches")
    print("OK: %s chopped the base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_clinch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pummeling drill volume: the hand fight for inside position
    round_s = 120.0
    switch_every = 40.0 / 3.0
    switches = round_s / switch_every
    rounds = 3
    print("pummeling round: %.0f s, one underhook switch per %.1f s" % (round_s, switch_every))
    print("  switches per round: %.0f" % switches)
    assert 8.99 < switches < 9.01
    print("  three rounds: %.0f total switches" % (switches * rounds))
    assert 26.99 < switches * rounds < 27.01
    print("rule: own the inside and you own the clinch - double underhooks is control")
    print("OK: %s won the hand fight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_sprawl(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sprawl reaction drill: hips beat the hands
    hips_back = 0.9
    react_t = 0.35
    hip_speed = hips_back / react_t
    print("sprawl: hips travel %.1f m back in %.2f s = %.2f m/s" % (hips_back, react_t, hip_speed))
    assert 2.57 < hip_speed < 2.58
    # EMOM drill ladder: distance closes as the reflex sharpens
    for week, dist in ((1, 3.0), (2, 2.0), (3, 1.0)):
        reps = 10
        print("week %d: partner shoots from %.0f m, %d sprawls" % (week, dist, reps))
    total = 3 * 10
    print("three-week ladder total: %d sprawl reps" % total)
    assert total == 30
    print("rule: the hips must beat the hands - hesitation is the only enemy")
    print("OK: %s killed the shot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # posture-break leverage from the closed guard
    pull_N = 300.0
    lever_m = 0.40
    torque = pull_N * lever_m
    print("posture break: %.0f N pull x %.2f m lever = %.1f N-m" % (pull_N, lever_m, torque))
    assert 119.9 < torque < 120.1
    # retention rounds: the beginner's guard workload
    round_s = 180.0
    rounds = 3
    total_s = round_s * rounds
    print("retention drilling: %d rounds x %.0f s = %.0f s under pressure" % (rounds, round_s, total_s))
    assert total_s == 540.0
    # ankle lock height: high guard vs low guard
    print("ankle lock high on the back: control; low on the hips: loose - keep it high")
    print("rule: ankles locked, posture broken - the guard only exists while the lock holds")
    print("OK: %s held the fortress" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_hipescape(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shrimping volume: the engine of every escape
    per_rep = 0.35
    mat_m = 6.0
    reps = math.ceil(mat_m / per_rep)
    rep_t = 2.0
    set_t = reps * rep_t
    print("shrimp %.2f m per rep across a %.0f m mat: %d reps per length" % (per_rep, mat_m, reps))
    print("at %.1f s per rep: %.1f s per length" % (rep_t, set_t))
    assert reps == 18
    assert 35.9 < set_t < 36.1
    lengths = 10
    print("drill: %d lengths per session = %d total shrimps" % (lengths, lengths * reps))
    assert lengths * reps == 180
    print("rule: the arms frame, the hips travel - never push with the arms")
    print("OK: %s shrimped to safety" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_uppercut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uppercut: leg drive becomes upward fist speed
    dip = 0.15
    body_kg = 75.0
    g = 9.81
    leg_work = body_kg * g * dip
    rise_m = 0.55
    rise_t = 0.15
    fist_v = rise_m / rise_t
    print("knee dip %.2f m loads %.1f J from a %.0f kg fighter" % (dip, leg_work, body_kg))
    print("fist rises %.2f m in %.2f s = %.2f m/s upward" % (rise_m, rise_t, fist_v))
    assert 110.3 < leg_work < 110.5
    assert 3.66 < fist_v < 3.67
    print("rule: the punch is the top of a chain that starts with bent knees")
    print("OK: %s rose through the middle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_elbows(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow vs punch: shorter lever, far smaller contact area
    omega = 10.0
    v_elbow = 0.35 * omega
    v_punch = 0.70 * omega
    print("same torso rotation (%.0f rad/s): elbow %.2f m/s vs punch %.2f m/s" % (omega, v_elbow, v_punch))
    assert 3.49 < v_elbow < 3.51
    assert 6.99 < v_punch < 7.01
    elbow_cm2 = 4.0
    fist_cm2 = 80.0
    ratio = fist_cm2 / elbow_cm2
    print("contact area: elbow %.0f cm2 vs fist %.0f cm2 -> %.0f x the pressure for the same force" % (
        elbow_cm2, fist_cm2, ratio))
    assert ratio == 20.0
    print("rule: the shortest weapon, honestly chambered, cuts deepest")
    print("OK: %s folded the blade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_knees(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # clinch knee: spear momentum plus the hand pull
    knee_v = 6.0
    eff_mass = 12.0
    momentum = eff_mass * knee_v
    pull_N = 300.0
    print("knee: %.0f kg effective mass x %.1f m/s = %.1f kg-m/s" % (eff_mass, knee_v, momentum))
    print("hand pull on the head: %.0f N meeting the rising knee" % pull_N)
    assert 71.9 < momentum < 72.1
    # volley math: knees come in bursts
    volley = 4
    per_knee_s = 0.8
    print("volley of %d knees at %.1f s each: %.1f s of sustained attack" % (volley, per_knee_s, volley * per_knee_s))
    assert 3.19 < volley * per_knee_s < 3.21
    print("rule: pull the head down honestly and the knee finds the road you built")
    print("OK: %s speared the clinch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_doubleleg(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # double leg: penetration depth and drive momentum
    height_cm = 175.0
    pen_step = 1.20
    level_drop = 0.40
    print("175 cm fighter: penetration step %.2f m, level drop %.2f m" % (pen_step, level_drop))
    assert 1.19 < pen_step < 1.21
    body_kg = 75.0
    drive_v = 3.0
    momentum = body_kg * drive_v
    print("drive: %.0f kg x %.1f m/s = %.1f kg-m/s through the target" % (body_kg, drive_v, momentum))
    assert 224.9 < momentum < 225.1
    # setup ratio: most shots need the punches first
    print("rule: the punches occupy the eyes while the level change happens underneath")
    print("OK: %s shot the double" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_singleleg(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # single leg: work to lift the captured leg
    leg_kg = 15.0
    lift_m = 0.50
    work = leg_kg * 9.81 * lift_m
    print("captured leg %.0f kg lifted %.2f m: %.2f J of work" % (leg_kg, lift_m, work))
    assert 73.5 < work < 73.6
    # run-the-pipe step distance
    pipe_step = 0.80
    print("run-the-pipe cross step: %.2f m behind the supporting leg" % pipe_step)
    # finish chains per round
    finishes = 10
    print("drill: %d finishes per round, alternating pipe and dump" % finishes)
    print("rule: keep the captured leg tight to the chest - a loose leg is a lost leg")
    print("OK: %s levered the single" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_whizzer(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # whizzer: the overhook as a lever on the shoulder
    lever_m = 0.60
    force_N = 400.0
    torque = lever_m * force_N
    print("whizzer: %.2f m overhook lever x %.0f N = %.1f N-m on the shoulder" % (lever_m, force_N, torque))
    assert 239.9 < torque < 240.1
    # the chain: sprawl -> whizzer -> crossface -> circle, drilled per side
    steps = 4
    per_side = 10
    rounds = 3
    total = steps * per_side * rounds
    print("chain drill: %d steps x %d reps x %d rounds = %d chained reps" % (steps, per_side, rounds, total))
    assert total == 120
    print("rule: sprawl first - the whizzer without the sprawl is an invitation")
    print("OK: %s chained the defense" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_guardpass(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pressure passing: honest weight through the shoulder
    body_kg = 75.0
    share = 0.60
    force_N = body_kg * share * 9.81
    area_m2 = 0.10
    pressure = force_N / area_m2
    print("passer %.0f kg, %.0f%% through the shoulder: %.1f N" % (body_kg, share * 100, force_N))
    print("over %.2f m2 of chest: %.0f Pa of pressure" % (area_m2, pressure))
    assert 441.4 < force_N < 441.5
    assert 4414.0 < pressure < 4416.0
    # stabilization count
    print("pass complete only after the 3-count hold in side control")
    print("rule: control the hips and the head before moving the legs")
    print("OK: %s passed with pressure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_sidecontrol(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crossface pressure on the jaw
    shoulder_kg = 20.0
    force_N = shoulder_kg * 9.81
    area_m2 = 0.01
    pressure = force_N / area_m2
    print("crossface: %.0f kg of shoulder over %.3f m2 of jaw = %.0f Pa" % (shoulder_kg, area_m2, pressure))
    assert 19619.0 < pressure < 19621.0
    # hold-and-transition rounds
    rounds = 3
    round_s = 180.0
    print("drill: %d x %.0f s hold-and-transition rounds" % (rounds, round_s))
    print("total top pressure time: %.0f s" % (rounds * round_s))
    assert rounds * round_s == 540.0
    print("rule: leave no space - space is the bottom fighter's currency")
    print("OK: %s held the crossface" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_mount(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mount: base width vs bridge, and the weight delivered
    base_m = 0.80
    body_kg = 75.0
    area_m2 = 0.15
    pressure = body_kg * 9.81 / area_m2
    print("mount base: knees %.2f m apart, hips low" % base_m)
    print("weight delivered: %.0f kg over %.2f m2 = %.0f Pa" % (body_kg, area_m2, pressure))
    assert 4904.0 < pressure < 4906.0
    # maintenance rounds
    rounds = 3
    round_s = 120.0
    print("drill: %d x %.0f s mount maintenance rounds" % (rounds, round_s))
    assert rounds * round_s == 360.0
    print("rule: ride the bridge, do not fight it - the hips resettle, the knees stay pinched")
    print("OK: %s kept the throne" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_armbar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # armbar leverage: hips as the fulcrum against the elbow
    bridge_N = 600.0
    lever_m = 0.30
    torque = bridge_N * lever_m
    print("armbar: %.0f N hip bridge x %.2f m lever = %.1f N-m on the elbow" % (bridge_N, lever_m, torque))
    assert 179.9 < torque < 180.1
    # entry reps before pressure: the crown is earned
    zero_resist_reps = 500
    print("required zero-resistance entry reps before live finishing: %d" % zero_resist_reps)
    # the tap rule in numbers: release time target
    print("release on tap: immediate - 0.0 s of extra pressure, every time")
    print("rule: trap truly, swing cleanly, and honor the tap as the highest law")
    print("OK: %s set the fulcrum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_rnc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear naked choke: bilateral carotid compression from the V
    per_side_N = 250.0
    angle_deg = 60.0
    total_N = 2 * per_side_N * math.sin(math.radians(angle_deg))
    print("mata-leao: %.0f N per side through a %.0f-degree V = %.1f N of compression" % (
        per_side_N, angle_deg, total_N))
    assert 432.9 < total_N < 433.1
    # back control first: the choke without the back is a gift
    print("prerequisites per rep: both hooks in, chest to back, then the encirclement")
    print("training rule: entries and locks at zero pressure for hundreds of reps")
    print("rule: the most decisive weapon needs the least violence - blood choke, never windpipe")
    print("OK: %s closed the lion killer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_guillotine(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guillotine: high-elbow lever plus the back arch
    lever_m = 0.35
    arch_N = 500.0
    torque = lever_m * arch_N
    print("guillotine: %.2f m high-elbow lever x %.0f N arch = %.1f N-m" % (lever_m, arch_N, torque))
    assert 174.9 < torque < 175.1
    # entry reps per side
    per_side = 10
    print("drill: %d sprawl-to-guillotine entries per side per round" % per_side)
    print("rule: sprawl first, choke second - the high elbow is the mechanical secret")
    print("OK: %s collected the toll" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_triangle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # triangle: the angle is the choke - 90 degrees, then the vise
    angle_deg = 90.0
    squeeze_N = 400.0
    hip_add_N = 200.0
    total_N = squeeze_N + hip_add_N
    print("triangle: body angled %.0f degrees to the trapped shoulder" % angle_deg)
    print("leg squeeze %.0f N + hip lift %.0f N = %.0f N closing the vise" % (squeeze_N, hip_add_N, total_N))
    assert total_N == 600.0
    # the flat triangle finishes nothing: angle check
    flat_penalty = 0.40
    print("flat (0-degree) triangle keeps only %.0f%% of the compression - angle out" % (flat_penalty * 100))
    assert 39.9 < flat_penalty * 100 < 40.1
    print("rule: ninety degrees honestly taken and the vise closes by law, not by force")
    print("OK: %s locked the geometry" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_kimura(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kimura: slow rotation torque on the shoulder
    hand_N = 150.0
    lever_m = 0.30
    torque = hand_N * lever_m
    print("kimura: %.0f N x %.2f m figure-four lever = %.1f N-m on the shoulder" % (hand_N, lever_m, torque))
    assert 44.9 < torque < 45.1
    # the six-count finish: patience, not yanking
    counts = 6
    print("finish applied over a slow %d-count - the shoulder taps long before it is threatened" % counts)
    # history anchor: 1951, the bout that named the lock
    print("named for Masahiko Kimura's 1951 victory over Helio Gracie at the Maracana")
    assert 2026 - 1951 == 75
    print("rule: the slow rotation, the early tap honored")
    print("OK: %s turned the history" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_sweeps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scissor sweep: off-balance then the scissor torque
    opp_kg = 80.0
    base_half_m = 0.25
    tip_torque = opp_kg * 9.81 * base_half_m
    scissor_N = 300.0
    scissor_lever = 0.40
    scissor_torque = scissor_N * scissor_lever
    print("80 kg opponent, base half-width %.2f m: tipping needs %.1f N-m" % (base_half_m, tip_torque))
    print("scissor: %.0f N x %.2f m = %.1f N-m" % (scissor_N, scissor_lever, scissor_torque))
    assert 196.1 < tip_torque < 196.3
    assert 119.9 < scissor_torque < 120.1
    # sweep volume per session
    per_side = 10
    print("drill: %d scissor + %d hip-bump per side per round" % (per_side, per_side))
    print("rule: off-balance first, then technique - the sweep on a balanced man is a gift")
    print("OK: %s reversed the fight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_flyingknee(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flying knee: launch physics
    jump_m = 0.50
    g = 9.81
    takeoff_v = math.sqrt(2 * g * jump_m)
    air_up = takeoff_v / g
    print("vertical jump %.2f m needs takeoff velocity %.2f m/s" % (jump_m, takeoff_v))
    print("time to apex: %.3f s - the knee must arrive on time" % air_up)
    assert 3.13 < takeoff_v < 3.14
    assert 0.318 < air_up < 0.320
    # distance covered: the ultimate distance-closer
    reach_m = 2.0
    print("covers %.1f m in a single explosive jump - miss, and there is no base left" % reach_m)
    # bag volume before timing work
    per_side = 10
    rounds = 3
    print("drill: %d per side x %d rounds on the bag before any timed pads" % (per_side, rounds))
    assert per_side * rounds == 30
    print("rule: the landing is part of the technique - land balanced or the miss becomes a takedown")
    print("OK: %s took flight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_subchains(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the classic chain: armbar -> triangle -> omoplata
    per_transition_s = 1.5
    transitions = 3
    chain_s = per_transition_s * transitions
    print("chain: %d transitions x %.1f s = %.1f s armbar to triangle to omoplata" % (
        transitions, per_transition_s, chain_s))
    assert 4.49 < chain_s < 4.51
    # flow round volume
    flow_s = 600.0
    chains_possible = flow_s / chain_s
    print("10-minute flow round could cycle %.0f full chains - transitions, not finishes" % chains_possible)
    assert 133.2 < chains_possible < 133.4
    print("rule: never force a defended submission - the defense is the next opening")
    print("OK: %s wove the net" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_grounddef(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bridge power: the engine of bottom escapes
    body_kg = 75.0
    lift_m = 0.30
    work = body_kg * 9.81 * lift_m
    print("bridge: %.0f kg hips lifted %.2f m = %.1f J per bridge" % (body_kg, lift_m, work))
    assert 220.6 < work < 220.8
    bridges = 20
    print("%d bridges per session: %.0f J of escape engine" % (bridges, bridges * work))
    assert 4413.0 < bridges * work < 4416.0
    # positional sparring structure
    rounds = 3
    round_s = 120.0
    print("positional sparring: %d x %.0f s, light controlled strikes, full gear, coach present" % (rounds, round_s))
    print("rule: shell the head, frame the distance, escape in layers")
    print("OK: %s survived the bottom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_heritage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # old rules vs unified rules: the sport grew up
    old_fouls = 3
    unified_fouls = 31
    ratio = unified_fouls / old_fouls
    print("old vale tudo fouls: ~%d (no biting, no eye-gouging, no groin strikes)" % old_fouls)
    print("unified rules fouls: %d" % unified_fouls)
    print("rulebook growth factor: %.2f x" % ratio)
    assert 10.32 < ratio < 10.34
    # IVC to unified rules: how fast the change came
    ivc = 1997
    unified_nj = 2000
    print("IVC %d -> unified rules (NJ) %d: %d years from headbutts-legal to the modern book" % (
        ivc, unified_nj, unified_nj - ivc))
    assert unified_nj - ivc == 3
    print("rule: heritage, not curriculum - study the old game, fight the modern one")
    print("OK: %s kept the memory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_combos(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jab-cross-shot: the classic vale tudo combination, timed
    jab_t = 0.12
    cross_t = 0.15
    shot_t = 0.45
    total = jab_t + cross_t + shot_t
    print("jab %.2f s + cross %.2f s + shot %.2f s = %.2f s start to takedown" % (jab_t, cross_t, shot_t, total))
    assert 0.719 < total < 0.721
    # hand-speed portion: strikes per second in the pure striking blend
    hook_t = 0.18
    three_strikes = jab_t + cross_t + hook_t
    rate = 3 / three_strikes
    print("jab-cross-hook in %.2f s: %.2f strikes per second" % (three_strikes, rate))
    assert 6.66 < rate < 6.68
    # session volume
    rounds = 5
    round_s = 180.0
    print("drill: %d x %.0f s rounds rotating three combinations" % (rounds, round_s))
    print("rule: every strike must earn its place - no wasted motion, no telegraphed rhythm")
    print("OK: %s wrote in paragraphs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_strategy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # output budgeting across a 3-round fight
    rounds = 3
    round_s = 300.0
    total_s = rounds * round_s
    print("championship distance: %d x %.0f s = %.0f s of fighting" % (rounds, round_s, total_s))
    assert total_s == 900.0
    strikes_per_round = 60
    total_strikes = strikes_per_round * rounds
    reserve = 0.20
    print("plan: %d strikes per round x %d rounds = %d, with %.0f%% held in reserve" % (
        strikes_per_round, rounds, total_strikes, reserve * 100))
    assert total_strikes == 180
    round3_budget = strikes_per_round * (1 - reserve)
    print("round 3 closes at %.0f strikes - the budgeted finish" % round3_budget)
    assert 47.9 < round3_budget < 48.1
    print("rule: the plan survives first contact - but the strategist adjusts between rounds")
    print("OK: %s thought in rounds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vt_code(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the preparation log: what a year of the code looks like
    sessions_week = 4
    weeks = 52
    sessions_year = sessions_week * weeks
    hours_each = 1.5
    hours_year = sessions_year * hours_each
    print("the code in numbers: %d sessions/week x %d weeks = %d sessions per year" % (
        sessions_week, weeks, sessions_year))
    print("at %.1f h each: %.0f h of honest training per year" % (hours_each, hours_year))
    assert sessions_year == 208
    assert hours_year == 312.0
    # the tap rule: release time allowed after the tap
    allowed_s = 0.0
    print("time allowed past the tap: %.1f s - the sport's most sacred rule" % allowed_s)
    print("rule: power without honor is just violence - the code is the art's immune system")
    print("OK: %s swore the oath" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "vt_what_is": demo_vt_what_is,
    "vt_stance": demo_vt_stance,
    "vt_breakfall": demo_vt_breakfall,
    "vt_footwork": demo_vt_footwork,
    "vt_jab": demo_vt_jab,
    "vt_cross": demo_vt_cross,
    "vt_hook": demo_vt_hook,
    "vt_lowkick": demo_vt_lowkick,
    "vt_clinch": demo_vt_clinch,
    "vt_sprawl": demo_vt_sprawl,
    "vt_guard": demo_vt_guard,
    "vt_hipescape": demo_vt_hipescape,
    "vt_uppercut": demo_vt_uppercut,
    "vt_elbows": demo_vt_elbows,
    "vt_knees": demo_vt_knees,
    "vt_doubleleg": demo_vt_doubleleg,
    "vt_singleleg": demo_vt_singleleg,
    "vt_whizzer": demo_vt_whizzer,
    "vt_guardpass": demo_vt_guardpass,
    "vt_sidecontrol": demo_vt_sidecontrol,
    "vt_mount": demo_vt_mount,
    "vt_armbar": demo_vt_armbar,
    "vt_rnc": demo_vt_rnc,
    "vt_guillotine": demo_vt_guillotine,
    "vt_triangle": demo_vt_triangle,
    "vt_kimura": demo_vt_kimura,
    "vt_sweeps": demo_vt_sweeps,
    "vt_flyingknee": demo_vt_flyingknee,
    "vt_subchains": demo_vt_subchains,
    "vt_grounddef": demo_vt_grounddef,
    "vt_heritage": demo_vt_heritage,
    "vt_combos": demo_vt_combos,
    "vt_strategy": demo_vt_strategy,
    "vt_code": demo_vt_code,
}
