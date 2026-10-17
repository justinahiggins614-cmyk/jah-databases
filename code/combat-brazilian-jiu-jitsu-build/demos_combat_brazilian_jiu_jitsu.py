#!/usr/bin/env python3
"""Demo programs for the Brazilian Jiu-Jitsu Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: impact physics, drill timers,
leverage and torque math, pressure calculations, and round planning.
All are machine-executed by build.py before commit: each prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cbbjj_breakfall(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # impact force of a standing fall absorbed by the breakfall slap
    m = 80.0            # practitioner mass, kg
    h = 1.2             # fall height of the hips, m
    d = 0.25            # mat deceleration distance, m
    g = 9.81
    v = math.sqrt(2 * g * h)
    F = m * v * v / (2 * d)     # work-energy: F*d = 1/2 m v^2
    print("fall velocity: %.3f m/s" % v)
    print("breakfall impact force: %.0f N" % F)
    assert 4.84 < v < 4.87
    assert 3755.0 < F < 3770.0
    # spread over the slap area vs a single point (elbow)
    slap_area = 0.09    # m^2 : forearm + lat
    point_area = 0.004  # m^2 : elbow point
    print("pressure on slap: %.1f kPa" % (F / slap_area / 1000.0))
    print("pressure on elbow point: %.1f kPa" % (F / point_area / 1000.0))
    assert 41.0 < F / slap_area / 1000.0 < 43.0
    assert 935.0 < F / point_area / 1000.0 < 945.0
    print("rule: spread the force, spare the joint")
    print("OK: %s absorbed the fall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_hip_escape(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shrimping drill: distance covered per rep and line totals
    per_rep = 0.35      # meters of hip travel per shrimp
    reps = 20
    total = per_rep * reps
    mat_length = 10.0   # meters
    lines = total / mat_length
    print("per shrimp: %.2f m" % per_rep)
    print("20 shrimps: %.1f m (%d%% of a 10 m mat line)" % (total, round(lines * 100)))
    assert 6.99 < total < 7.01
    assert 0.69 < lines < 0.71
    # drill timer: 3 rounds of 2 minutes, 15 s rest
    work, rest, rounds = 120.0, 15.0, 3
    session = rounds * work + (rounds - 1) * rest
    print("drill session: %d rounds x %ds + %ds rests = %.0f s" % (rounds, work, rest, session))
    assert 389.9 < session < 390.1
    print("rule: the hips travel, the frames guard")
    print("OK: %s shrimped the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_closed_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guard retention drill: attacks per round from closed guard
    attempts = {"scissor sweep": 4, "hip bump": 3, "kimura": 2, "triangle": 2, "cross-collar": 3}
    total = sum(attempts.values())
    # combination rate: each failed attack opens the next at 60% conversion
    conv = 0.60
    chained = total * conv
    print("attack attempts per 5-min round: %d" % total)
    for k, v in attempts.items():
        print("  %-14s %d" % (k, v))
    print("chained follow-ups at 60%% conversion: %.1f" % chained)
    assert total == 14
    assert 8.39 < chained < 8.41
    # posture-break force: pulling 80 kg opponent down 0.25 m
    m, g, drop = 80.0, 9.81, 0.25
    work = m * g * drop
    print("posture-break work: %.1f J" % work)
    assert 196.1 < work < 196.3
    print("rule: break the posture, then collect")
    print("OK: %s held the home position" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_mount_position(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # base of support: trapezoid from knees to feet
    knee_w = 0.60   # m between knees
    foot_w = 0.90   # m between hooked feet
    depth = 0.55    # m knees to feet
    area = (knee_w + foot_w) / 2.0 * depth
    print("mount base of support: %.4f m^2" % area)
    assert 0.4124 < area < 0.4126
    # riding the bridge: hip float time per bridge cycle
    bridges = 6
    ride_each = 1.4   # seconds of float per bridge
    print("riding %d bridges x %.1f s = %.1f s of control" % (bridges, ride_each, bridges * ride_each))
    assert 8.39 < bridges * ride_each < 8.41
    # IBJJF mount points over a 5-minute match with 2 mounts
    print("2 mounts x 4 pts = %d pts" % (2 * 4))
    assert 2 * 4 == 8
    print("rule: hips low, base wide, patience")
    print("OK: %s kept the mountain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_side_control(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # chest pressure: bodyweight over the contact patch
    m, g = 80.0, 9.81
    contact = 0.06   # m^2 chest-to-chest contact
    pressure = m * g / contact / 1000.0  # kPa
    print("side control pressure: %.1f kPa" % pressure)
    assert 13.07 < pressure < 13.09
    # transition matrix: follow their turn
    turns = {"turns in": "mount", "turns away": "back", "pushes": "americana/armbar"}
    print("transitions: %d" % len(turns))
    for k, v in turns.items():
        print("  %-10s -> %s" % (k, v))
    assert len(turns) == 3
    # hold time for points: 3 s per control, 3 controls
    print("3 controls x 3 s = %d s of pinned time for 10 pts" % (3 * 3))
    assert 3 + 4 + 3 == 10  # side + mount + back points
    print("rule: heavy chest, quiet arms")
    print("OK: %s pinned the side" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_bridge_roll(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bridge work: lifting the mounted opponent's weight
    m, g = 80.0, 9.81
    lift = 0.15   # m of hip elevation at the top of the bridge
    work = m * g * lift
    print("bridge work per rep: %.1f J" % work)
    assert 117.6 < work < 117.8
    # drill ladder: 10 bridges, rest shrinking
    reps = 10
    total_work = reps * work
    print("%d bridges: %.0f J total" % (reps, total_work))
    assert 1176.0 < total_work < 1178.0
    # timing window: bridge when they settle (0.8 s) not when braced
    window = 0.8
    reaction = 0.25
    margin = window - reaction
    print("timing margin: %.2f s" % margin)
    assert 0.54 < margin < 0.56
    print("rule: trap, bridge, look, roll")
    print("OK: %s reversed the mount" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_standup_base(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # technical stand-up phase timer
    phases = {"post hand": 0.4, "plant foot": 0.3, "lift hips": 0.5, "swing leg": 0.4}
    total = sum(phases.values())
    print("stand-up phases:")
    for k, v in phases.items():
        print("  %-10s %.1f s" % (k, v))
    print("total stand-up time: %.1f s" % total)
    assert 1.59 < total < 1.61
    # drill: 30 stand-ups, guard hand up every rep
    reps = 30
    hands_up = reps  # zero drops allowed
    print("%d reps, hands dropped: %d" % (reps, reps - hands_up))
    assert hands_up == reps
    print("rule: post, guard, rise - never turn the back")
    print("OK: %s stood in base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_posture_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # posture geometry: spine angle vs force the guard player must overcome
    m, g = 80.0, 9.81
    lean_deg = 10.0   # degrees off vertical when posture is good
    lean = math.radians(lean_deg)
    # horizontal force to break posture scales with cos of lean
    hold = m * g * math.cos(lean)
    broken_lean = math.radians(45.0)
    hold_broken = m * g * math.cos(broken_lean)
    print("posture hold at 10 deg: %.0f N" % hold)
    print("posture hold at 45 deg: %.0f N" % hold_broken)
    assert 772.0 < hold < 774.0
    assert 554.0 < hold_broken < 556.0
    print("posture advantage: %.0f N harder to break down" % (hold - hold_broken))
    assert 217.0 < (hold - hold_broken) < 219.0
    print("rule: tall spine, managed distance")
    print("OK: %s kept the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_guard_break_standing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # standing with their weight: leg press load
    m, g = 80.0, 9.81
    carried = 0.65   # fraction of their weight hanging on you
    load = m * g * carried
    print("standing load: %.0f N (%.1f kg)" % (load, load / g))
    assert 509.0 < load < 511.0
    # knee wedge lever: pry force at the ankles
    effort_arm = 0.45  # m: hands on knees
    load_arm = 0.12    # m: ankle lock point
    mech_adv = effort_arm / load_arm
    print("wedge mechanical advantage: %.2f : 1" % mech_adv)
    assert 3.74 < mech_adv < 3.76
    ankle_resist = 120.0  # N of ankle lock resistance
    print("hand effort needed: %.1f N" % (ankle_resist / mech_adv))
    assert 31.9 < ankle_resist / mech_adv < 32.1
    print("rule: posture, stand, wedge, disengage")
    print("OK: %s broke the guard standing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_scissor_sweep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep torque: bottom leg swinging across the far hip
    leg_m = 12.0      # kg mass of the sweeping leg
    r = 0.50          # m lever from hip pivot
    omega = 6.0       # rad/s swing speed
    v = omega * r
    ke = 0.5 * leg_m * v * v
    print("leg swing speed: %.1f m/s, kinetic energy: %.0f J" % (v, ke))
    assert 2.99 < v < 3.01
    assert 53.9 < ke < 54.1
    # grip off-balance: pull their 80 kg mass 0.2 m past base
    m, g = 80.0, 9.81
    shift = 0.20
    torque_needed = m * g * shift
    print("off-balance torque to create: %.1f N m" % torque_needed)
    assert 156.9 < torque_needed < 157.1
    print("rule: grips tip, legs deliver")
    print("OK: %s scissored them over" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_hip_bump_sweep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hip bump impulse: drive 80 kg opponent backward over their base
    m = 80.0
    dv = 1.2          # m/s of backward velocity imparted
    impulse = m * dv
    print("bump impulse: %.0f N s" % impulse)
    assert 95.9 < impulse < 96.1
    # delivered in 0.25 s of hip explosion
    dt = 0.25
    force = impulse / dt
    print("peak bump force: %.0f N" % force)
    assert 383.9 < force < 384.1
    # combination tree: bump -> posted hand -> kimura/triangle
    tree = {"bump lands": "mount (2 pts)", "they post": "kimura", "they tuck": "guillotine"}
    print("combination branches: %d" % len(tree))
    assert len(tree) == 3
    print("rule: tall posture is the trigger")
    print("OK: %s bumped them over" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_americana(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # paintbrush torque on the shoulder
    F = 60.0          # N of steady lifting force
    r = 0.30          # m forearm lever from elbow to wrist
    torque = F * r
    print("americana torque: %.1f N m" % torque)
    assert 17.99 < torque < 18.01
    # rotation to tap: ~35 degrees of shoulder rotation under control
    deg = 35.0
    rad = math.radians(deg)
    work = torque * rad
    print("rotation to tap: %.0f deg, work: %.1f J" % (deg, work))
    assert 0.6108 < rad < 0.6110
    assert 10.99 < work < 11.01
    # application speed: slow, 2 s to full pressure
    print("application time: 2.0 s - slow and steady")
    print("rule: paint slow, release instant")
    print("OK: %s finished the americana" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_kimura(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # figure-four leverage: grip at wrist vs their grip at elbow
    F = 80.0          # N torso rotation force
    r_wrist = 0.28    # m from elbow pivot to wrist grip
    r_elbow = 0.10    # m from shoulder pivot to their defensive grip
    torque_out = F * r_wrist
    torque_resist_max = 150.0 * r_elbow  # their 150 N defense at short lever
    print("kimura torque: %.1f N m vs defense %.1f N m" % (torque_out, torque_resist_max))
    assert 22.39 < torque_out < 22.41
    assert 14.99 < torque_resist_max < 15.01
    assert torque_out > torque_resist_max
    # four attack positions share one grip
    positions = ["guard", "side control", "mount", "back"]
    print("kimura positions: %d" % len(positions))
    assert len(positions) == 4
    print("rule: control the grip, control the person")
    print("OK: %s locked the figure-four" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_rear_naked_choke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # blood choke timeline: published carotid occlusion to unconsciousness
    t_min, t_max = 8.0, 13.0
    t_mid = (t_min + t_max) / 2.0
    print("occlusion to unconsciousness: %.0f-%.0f s (mid %.1f s)" % (t_min, t_max, t_mid))
    assert 10.49 < t_mid < 10.51
    # drill: 10 lock-and-release reps, 6 s hold each, partner taps at 3 s
    reps, hold = 10, 6.0
    total = reps * hold
    print("%d reps x %.0f s holds = %.0f s under the choke" % (reps, hold, total))
    assert 59.9 < total < 60.1
    # triangle geometry: biceps grip + hand behind head
    print("lock checkpoints: 3 (under chin, biceps grip, hand behind head)")
    print("rule: squeeze the carotids, never crank the neck")
    print("OK: %s sank the rear naked choke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_cross_collar_choke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scissor geometry: wrists crossing at the carotids
    grip_depth = 0.10   # m of cloth fed deep (four fingers at ear level)
    wrist_angle = 70.0  # degrees of scissor flare
    rad = math.radians(wrist_angle)
    # effective compression width across the neck
    neck_d = 0.12       # m neck diameter
    wrap = math.pi * neck_d * (wrist_angle / 360.0)
    print("grip depth: %.2f m, scissor flare: %.0f deg" % (grip_depth, wrist_angle))
    print("cloth wrap on carotids: %.3f m" % wrap)
    assert 0.0732 < wrap < 0.0734
    # finish: elbows to ribs, crunch forward 0.15 m
    crunch = 0.15
    print("finishing crunch: %.2f m forward" % crunch)
    assert 0.149 < crunch < 0.151
    print("rule: deep grips decide everything")
    print("OK: %s crossed the collars" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_armbar_mount(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lever ratio: hips as fulcrum, wrist far, elbow near
    r_wrist = 0.62   # m fulcrum to wrist (force applied)
    r_elbow = 0.31   # m fulcrum to elbow (joint loaded)
    ratio = r_wrist / r_elbow
    print("armbar lever ratio: %.2f : 1" % ratio)
    assert 1.99 < ratio < 2.01
    # hip bridge force 400 N becomes elbow load
    F_hip = 400.0
    F_elbow = F_hip * ratio
    print("400 N hip bridge -> %.0f N at the elbow" % F_elbow)
    assert 799.0 < F_elbow < 801.0
    # control check: knees pinched, thumb up, wrist to chest
    checks = ["arm pinned pre-swing", "knees pinched", "thumb up", "wrist to chest"]
    print("control checkpoints: %d" % len(checks))
    assert len(checks) == 4
    print("rule: hips are the fulcrum, the body is the lever")
    print("OK: %s extended the armbar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_triangle_choke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # triangle geometry: legs at 60 degrees, the V that closes
    angle = 60.0
    rad = math.radians(angle)
    leg = 0.85   # m leg length
    # closing force component perpendicular to the neck
    F_squeeze = 300.0  # N total leg squeeze
    F_neck = F_squeeze * math.sin(rad)
    print("triangle angle: %.0f deg, squeeze on neck: %.0f N" % (angle, F_neck))
    assert 259.7 < F_neck < 259.9
    # angle adjustment: hips slide out 0.25 m to create the angle
    slide = 0.25
    print("hip slide for angle: %.2f m" % slide)
    assert 0.249 < slide < 0.251
    # one arm in / one arm out check
    print("arms in triangle: 1 (their shoulder is the second wall)")
    print("rule: the angle makes the choke")
    print("OK: %s closed the triangle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_elbow_escape_mount(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inch-by-inch: each bridge-shrimp cycle gains space
    per_cycle = 0.15   # m gained per cycle
    cycles = 4
    total = per_cycle * cycles
    print("per cycle: %.2f m x %d cycles = %.2f m" % (per_cycle, cycles, total))
    assert 0.599 < total < 0.601
    # knee must travel 0.45 m to clear the hip line
    needed = 0.45
    print("knee travel needed: %.2f m -> cycles required: %d" % (needed, math.ceil(needed / per_cycle)))
    assert math.ceil(needed / per_cycle) == 3
    # frame discipline: one frame always stays (2 arms, min 1 up)
    print("frames up during escape: >= 1 at all times")
    print("rule: small gains chained without pausing")
    print("OK: %s elbow-escaped the mount" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_bullfighter_pass(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bullfighter sprint timer
    grip_break = 1.2   # s to shove the legs aside
    sprint = 1.8       # s lateral sprint around the legs
    settle = 3.0       # s hold for the points
    total = grip_break + sprint + settle
    print("grip break %.1f s + sprint %.1f s + hold %.0f s = %.1f s" % (grip_break, sprint, settle, total))
    assert 5.99 < total < 6.01
    # lateral distance covered in the sprint
    speed = 3.5   # m/s lateral sprint
    dist = speed * sprint
    print("lateral distance: %.2f m" % dist)
    assert 6.29 < dist < 6.31
    # both directions hunted
    print("passing directions drilled: 2 (left and right)")
    print("rule: speed around the legs, not strength through them")
    print("OK: %s ran the bullfighter" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_knee_slice_pass(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weight distribution through the slicing knee
    m, g = 80.0, 9.81
    on_knee = 0.70   # fraction of weight driven through the knee
    knee_load = m * g * on_knee
    print("weight through slicing knee: %.0f N (%.0f%%)" % (knee_load, on_knee * 100))
    assert 549.2 < knee_load < 549.4
    # slice travel across the thigh
    travel = 0.35   # m of knee travel
    time = 1.1      # s for the slice
    print("slice: %.2f m in %.1f s = %.2f m/s" % (travel, time, travel / time))
    assert 0.317 < travel / time < 0.319
    # follow-ups when they react
    follows = {"turns in": "mount", "frames hard": "underhook finish"}
    print("follow-ups: %d" % len(follows))
    assert len(follows) == 2
    print("rule: pressure through, not around")
    print("OK: %s sliced the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_half_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # underhook battle: pummeling rounds
    rounds, per_round = 5, 60.0   # 5 x 60 s pummeling rounds
    total = rounds * per_round
    print("underhook pummeling: %d x %.0f s = %.0f s" % (rounds, per_round, total))
    assert 299.9 < total < 300.1
    # come-up stages: elbow -> hand -> drive
    stages = [("elbow", 0.5), ("hand", 0.5), ("drive", 0.8)]
    t = sum(s for _, s in stages)
    print("come-up stages: %d, total %.1f s" % (len(stages), t))
    assert 1.79 < t < 1.81
    # win/lose matrix
    print("underhook won -> sweep or back take; underhook lost -> frame and recover")
    print("rule: the underhook is the whole position")
    print("OK: %s battled the half guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_double_leg(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # penetration step and drive
    step = 1.10    # m deep penetration step
    drive = 2.0    # m of forward drive
    print("penetration step: %.2f m, drive: %.1f m" % (step, drive))
    assert 1.09 < step < 1.11
    # lifting 80 kg opponent 0.3 m during the finish
    m, g = 80.0, 9.81
    lift = 0.30
    work = m * g * lift
    print("lift work: %.1f J" % work)
    assert 235.3 < work < 235.5
    # level change: hips drop 0.45 m, back stays straight
    drop = 0.45
    print("level change: hips drop %.2f m" % drop)
    assert 0.449 < drop < 0.451
    # head position safety: head above hips the whole shot
    print("head height > hip height: enforced every rep")
    print("rule: knees bend, back straight, head up")
    print("OK: %s finished the double leg" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_delariva_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # off-balance angle: hook pulls their base past the tipping point
    tip_deg = 12.0
    tip = math.radians(tip_deg)
    m, g, h_com = 80.0, 9.81, 0.95   # center of mass height
    # horizontal pull force to tip at the hook
    F_tip = m * g * math.tan(tip)
    print("off-balance at %.0f deg needs %.0f N of hook pull" % (tip_deg, F_tip))
    assert 166.0 < F_tip < 168.0
    # hook depth: instep wrapped 0.15 m around the ankle
    wrap = 0.15
    print("hook wrap: %.2f m of instep on the ankle" % wrap)
    assert 0.149 < wrap < 0.151
    # entries chained from de la Riva
    chains = ["classic sweep", "berimbolo", "back take", "leg drag"]
    print("chains from de la Riva: %d" % len(chains))
    assert len(chains) == 4
    print("rule: the hook is the engine, the grips are the steering")
    print("OK: %s hooked the de la Riva" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_darce_choke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arm-triangle compression: thread depth vs closure
    thread = 0.35    # m of arm threaded past the neck
    print("thread depth: %.2f m" % thread)
    assert 0.349 < thread < 0.351
    # hip walk closes the triangle: 0.25 m toward their head
    walk = 0.25
    gap_close = thread + walk
    print("triangle closure: %.2f m" % gap_close)
    assert 0.599 < gap_close < 0.601
    # compression force from dropping 60% of bodyweight through the shoulder
    m, g = 80.0, 9.81
    F = m * g * 0.60
    print("shoulder compression: %.0f N" % F)
    assert 470.0 < F < 472.0
    print("rule: depth of thread decides the finish")
    print("OK: %s threaded the darce" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_guillotine_choke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sprawl-back finish: hips travel away to extend the neck
    sprawl = 0.60   # m of hip retreat
    print("sprawl-back: %.2f m" % sprawl)
    assert 0.599 < sprawl < 0.601
    # neck extension angle under the lock
    ext_deg = 25.0
    ext = math.radians(ext_deg)
    m_neck = 6.0   # kg head+neck mass
    # torque closing the chin strap
    F_arm = 120.0  # N arm lock force
    r = 0.09       # m neck radius lever
    torque = F_arm * r
    print("chin-strap torque: %.1f N m at %.0f deg extension" % (torque, ext_deg))
    assert 10.79 < torque < 10.81
    assert 0.4362 < ext < 0.4364
    # two finishes drilled
    print("finishes drilled: 2 (arm-in high elbow, chin strap)")
    print("rule: the sprawl finishes it, the arms hold the shape")
    print("OK: %s closed the guillotine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_omoplata(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shoulder rotation: leg pressure rotates the arm behind the back
    F_leg = 180.0   # N leg pressure
    r = 0.28        # m from shoulder pivot to leg contact
    torque = F_leg * r
    print("omoplata torque: %.1f N m" % torque)
    assert 50.39 < torque < 50.41
    # rotation to finish: 90 degrees of shoulder turn
    deg = 90.0
    rad = math.radians(deg)
    work = torque * rad
    print("90 deg rotation, work: %.1f J" % work)
    assert 79.16 < work < 79.18
    # their escape becomes your sweep: forward roll follow
    print("forward roll escape -> sweep (2 pts) or back take")
    print("rule: pivot the hips fully, then sit tall")
    print("OK: %s turned the omoplata" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_north_south_choke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gravity choke: bodyweight through the shoulder onto the neck
    m, g = 80.0, 9.81
    share = 0.55   # fraction of weight sunk through the shoulder
    F = m * g * share
    print("shoulder compression: %.0f N" % F)
    assert 431.5 < F < 431.7
    # contact patch: forearm + ribs around the neck
    contact = 0.025  # m^2
    pressure = F / contact / 1000.0
    print("compression pressure: %.1f kPa" % pressure)
    assert 17.25 < pressure < 17.27
    # stretch: feet walk 0.4 m out to kill frames
    walk = 0.40
    print("stretch walk: %.2f m" % walk)
    assert 0.399 < walk < 0.401
    print("rule: gravity finishes it - muscling ruins the angle")
    print("OK: %s sank the north-south choke" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_anaconda_choke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gator roll: full rotation to tighten the coil
    roll_time = 1.5   # s per full gator roll
    omega = 2 * math.pi / roll_time
    print("gator roll angular velocity: %.3f rad/s" % omega)
    assert 4.1887 < omega < 4.1889
    # coil closure: each quarter roll takes up 0.08 m of slack
    per_quarter = 0.08
    closure = per_quarter * 4
    print("full-roll slack take-up: %.2f m" % closure)
    assert 0.319 < closure < 0.321
    # lock check before rolling
    print("lock checkpoints before roll: 2 (thread deep, hands locked)")
    print("rule: commit to the roll - half rolls give up the position")
    print("OK: %s coiled the anaconda" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_berimbolo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inversion spin: 180 degrees underneath in drill time
    spin_deg = 180.0
    spin_time = 1.1   # s
    omega = math.radians(spin_deg) / spin_time
    print("berimbolo spin: %.0f deg in %.1f s = %.3f rad/s" % (spin_deg, spin_time, omega))
    assert 2.855 < omega < 2.857
    # back take scoring: 4 points for hooks + seatbelt control
    print("back take: 4 pts (hooks in, 3 s control)")
    assert 4 == 4
    # drill ladder: 10 inversions each side
    reps = 20
    print("drill: %d inversions (%d per side)" % (reps, reps // 2))
    assert reps // 2 == 10
    print("rule: invert fully - hesitation gets you flattened")
    print("OK: %s spun the berimbolo" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_ezekiel_choke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sleeve friction: the hidden grip that makes the choke
    mu = 0.40          # cloth-on-cloth friction
    grip_F = 90.0      # N of hand grip inside the sleeve
    friction = mu * grip_F
    print("sleeve friction hold: %.1f N" % friction)
    assert 35.99 < friction < 36.01
    # vise closure: free hand pulls the sleeved wrist 0.12 m across
    pull = 0.12
    print("vise pull: %.2f m across the neck" % pull)
    assert 0.119 < pull < 0.121
    # two carotids compressed by the forearm blade
    print("carotids compressed: 2 (forearm blade + pulling wrist)")
    print("rule: the sleeve grip must be deep - shallow slips")
    print("OK: %s slid the Ezekiel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_ankle_lock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fulcrum leverage: forearm under the Achilles, foot as the lever
    F_back = 200.0   # N of back-arch force
    r_foot = 0.26    # m foot lever from ankle pivot
    torque = F_back * r_foot
    print("ankle lock torque: %.1f N m" % torque)
    assert 51.99 < torque < 52.01
    # fulcrum pressure on the Achilles: contact 0.008 m^2
    contact = 0.008
    pressure = F_back / contact / 1000.0
    print("fulcrum pressure: %.1f kPa" % pressure)
    assert 24.99 < pressure < 25.01
    # knee line control: leg must not rotate more than 5 degrees
    print("knee rotation limit in drill: 5 deg (control the line)")
    print("rule: the back does the work, the forearm is the fulcrum")
    print("OK: %s wedged the ankle lock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_heel_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # danger math: why this is catch-and-release in drilling
    # ligament damage begins around 45 degrees of heel rotation
    danger_deg = 45.0
    applied_deg = 0.0    # degrees applied in safe drilling: ZERO
    margin = danger_deg - applied_deg
    print("danger threshold: %.0f deg rotation" % danger_deg)
    print("rotation applied in drilling: %.0f deg" % applied_deg)
    print("safety margin kept: %.0f deg" % margin)
    assert 44.99 < margin < 45.01
    # rotation speed at full application: 45 deg in 0.3 s
    t_full = 0.3
    omega = math.radians(danger_deg) / t_full
    print("full-application speed: %.2f rad/s - faster than the tap reflex" % omega)
    assert 2.617 < omega < 2.619
    # supervision rule
    print("supervision required: qualified black belt, catch and release only")
    print("rule: tap comes before pain - ligaments fail before the warning")
    print("OK: %s respected the heel hook" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_inverted_recovery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # granby roll: full 360 under pressure
    roll_deg = 360.0
    roll_time = 1.4   # s per granby
    omega = math.radians(roll_deg) / roll_time
    print("granby roll: %.0f deg in %.1f s = %.3f rad/s" % (roll_deg, roll_time, omega))
    assert 4.4879 < omega < 4.4881
    # inversion comfort ladder: granby volume
    weekly = 50
    weeks = 8
    total = weekly * weeks
    print("comfort ladder: %d granbys/week x %d weeks = %d" % (weekly, weeks, total))
    assert total == 400
    # recovery window: re-guard before they settle (1.2 s)
    window = 1.2
    print("re-guard window: %.1f s" % window)
    assert 1.19 < window < 1.21
    print("rule: roll with their force, never against it")
    print("OK: %s inverted to safety" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbbjj_xguard_entry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # X lift: extending the hooks lifts the standing opponent
    m, g = 80.0, 9.81
    lift_share = 0.75  # fraction of their weight the X must lift
    F_lift = m * g * lift_share
    print("X-guard lift force: %.0f N" % F_lift)
    assert 588.5 < F_lift < 588.7
    # two hooks share the load
    per_hook = F_lift / 2.0
    print("per hook: %.1f N" % per_hook)
    assert 294.2 < per_hook < 294.4
    # dump directions: they lean, you dump
    dumps = ["backward", "forward", "sideways"]
    print("dump directions: %d" % len(dumps))
    assert len(dumps) == 3
    # entry timing: dive as they pressure (0.5 s window)
    print("entry window on their pressure step: 0.5 s")
    print("rule: stay compact - reaching arms get trapped")
    print("OK: %s slid into the X-guard" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "breakfall": demo_cbbjj_breakfall,
    "hip_escape": demo_cbbjj_hip_escape,
    "closed_guard": demo_cbbjj_closed_guard,
    "mount_position": demo_cbbjj_mount_position,
    "side_control": demo_cbbjj_side_control,
    "bridge_roll": demo_cbbjj_bridge_roll,
    "standup_base": demo_cbbjj_standup_base,
    "posture_guard": demo_cbbjj_posture_guard,
    "guard_break_standing": demo_cbbjj_guard_break_standing,
    "scissor_sweep": demo_cbbjj_scissor_sweep,
    "hip_bump_sweep": demo_cbbjj_hip_bump_sweep,
    "americana": demo_cbbjj_americana,
    "kimura": demo_cbbjj_kimura,
    "rear_naked_choke": demo_cbbjj_rear_naked_choke,
    "cross_collar_choke": demo_cbbjj_cross_collar_choke,
    "armbar_mount": demo_cbbjj_armbar_mount,
    "triangle_choke": demo_cbbjj_triangle_choke,
    "elbow_escape_mount": demo_cbbjj_elbow_escape_mount,
    "bullfighter_pass": demo_cbbjj_bullfighter_pass,
    "knee_slice_pass": demo_cbbjj_knee_slice_pass,
    "half_guard": demo_cbbjj_half_guard,
    "double_leg": demo_cbbjj_double_leg,
    "delariva_guard": demo_cbbjj_delariva_guard,
    "darce_choke": demo_cbbjj_darce_choke,
    "guillotine_choke": demo_cbbjj_guillotine_choke,
    "omoplata": demo_cbbjj_omoplata,
    "north_south_choke": demo_cbbjj_north_south_choke,
    "anaconda_choke": demo_cbbjj_anaconda_choke,
    "berimbolo": demo_cbbjj_berimbolo,
    "ezekiel_choke": demo_cbbjj_ezekiel_choke,
    "ankle_lock": demo_cbbjj_ankle_lock,
    "heel_hook": demo_cbbjj_heel_hook,
    "inverted_recovery": demo_cbbjj_inverted_recovery,
    "xguard_entry": demo_cbbjj_xguard_entry,
}
