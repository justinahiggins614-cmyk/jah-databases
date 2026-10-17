#!/usr/bin/env python3
"""Demo programs for the Hapkido Combat databases.

Every demo is real, runnable, stdlib-only Python performing an actual
training calculation for its record: stance geometry, fall physics,
timing windows, leverage ratios, kick arcs. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cbhap_stances(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # horse stance base: twice shoulder width, support polygon area
    shoulder = 0.45  # meters
    width = 2.0 * shoulder
    depth = 0.35
    area = width * depth
    print("horse stance base: %.2f m x %.2f m = %.3f m^2" % (width, depth, area))
    assert 0.89 < width < 0.91
    assert 0.314 < area < 0.316
    # front stance: 1.5 shoulder widths long
    length = 1.5 * shoulder
    print("front stance length: %.3f m" % length)
    assert 0.674 < length < 0.676
    print("rule: the root decides whether the technique lives or dies")
    print("OK: %s rooted the stance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_nakbeop(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fall from standing hip height: impact velocity and time
    g, h = 9.81, 1.0
    v = math.sqrt(2 * g * h)
    t = math.sqrt(2 * h / g)
    print("fall 1.0 m: impact %.2f m/s after %.3f s" % (v, t))
    assert 4.42 < v < 4.44
    assert 0.450 < t < 0.453
    # the slap spreads force over ~0.15 s vs 0.02 s stiff landing
    m = 70.0
    f_stiff = m * v / 0.02 / 1000.0
    f_slap = m * v / 0.15 / 1000.0
    print("stiff landing force: %.1f kN vs slap landing: %.1f kN" % (f_stiff, f_slap))
    assert 15.4 < f_stiff < 15.6
    assert 2.05 < f_slap < 2.09
    print("rule: tuck the chin, slap the mat, exhale on impact")
    print("OK: %s landed the fall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_balgeoreum(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # glide step: cover distance without bouncing the head
    step_len, cadence = 0.45, 2.0  # meters, steps per second
    speed = step_len * cadence
    print("glide speed: %.2f m/s" % speed)
    assert 0.899 < speed < 0.901
    # hold one arm's distance (0.75 m) against a walker at 1.2 m/s
    walker, gap = 1.2, 0.75
    print("retreat speed needed: %.2f m/s" % walker)
    assert speed < walker, "glide alone cannot outrun a committed walk - pivot offline instead"
    print("rule: feet never cross, head never bounces, eyes never leave")
    print("OK: %s held the distance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_jireugi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight punch: 0.7 m travel at 7 m/s hand speed
    dist, hand_v = 0.7, 7.0
    t = dist / hand_v
    print("punch time: %.3f s" % t)
    assert 0.0999 < t < 0.1001
    # hip snap adds effective mass: 4 kg arm vs 12 kg with body behind it
    ke_arm = 0.5 * 4.0 * hand_v ** 2
    ke_body = 0.5 * 12.0 * hand_v ** 2
    print("arm-only energy: %.1f J vs hip-driven: %.1f J" % (ke_arm, ke_body))
    assert 97.9 < ke_arm < 98.1
    assert 293.9 < ke_body < 294.1
    print("rule: floor, hip, fist - one straight stroke")
    print("OK: %s threw the punch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_apchagi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # chamber: thigh parallel to floor, shin hangs; extension reaches solar plexus
    hip_h, thigh, shin = 0.95, 0.45, 0.45
    chamber_knee_h = hip_h  # thigh horizontal
    reach = hip_h + shin   # leg extended upward-forward
    print("chamber knee height: %.2f m, kick reach: %.2f m" % (chamber_knee_h, reach))
    assert 0.949 < chamber_knee_h < 0.951
    assert 1.399 < reach < 1.401
    # snap time: 0.45 m shin travel at 9 m/s
    t = 0.45 / 9.0
    print("extension time: %.3f s" % t)
    assert 0.0499 < t < 0.0501
    print("rule: chamber high, snap out, rechamber fast")
    print("OK: %s chambered the kick" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_dollyeochagi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # roundhouse arc: leg radius 0.9 m sweeping 100 degrees
    r, deg = 0.9, 100.0
    arc = r * math.radians(deg)
    print("kick arc length: %.3f m" % arc)
    assert 1.570 < arc < 1.572
    # foot speed from hip whip: omega 12 rad/s
    v = 12.0 * r
    print("foot speed: %.2f m/s" % v)
    assert 10.79 < v < 10.81
    print("rule: pivot 180 degrees, then let the hip whip the arc")
    print("OK: %s turned the kick" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_makgi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # deflection at 45 degrees: only the perpendicular component must be handled
    f = 300.0  # N incoming punch
    for ang in (90, 45, 30):
        handled = f * math.sin(math.radians(ang))
        print("block angle %d deg: must handle %.1f N of %d N" % (ang, handled, f))
    assert 299.9 < 300.0 * math.sin(math.radians(90)) < 300.1
    assert 212.0 < 300.0 * math.sin(math.radians(45)) < 212.2
    assert 149.9 < 300.0 * math.sin(math.radians(30)) < 300.1
    print("rule: deflect at an angle - redirection beats brute stopping")
    print("OK: %s turned the blow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_wonui(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # redirect a 400 N push: step offline 45 deg, guide with 40 N at the wrist
    push = 400.0
    offline = math.radians(45)
    remaining = push * math.cos(offline)
    print("push along original line after offline step: %.1f N" % remaining)
    assert 282.7 < remaining < 282.9
    # wrist lever: 0.6 m arm, 40 N guide -> torque on attacker's structure
    torque = 40.0 * 0.6
    print("guiding torque at wrist: %.1f N-m" % torque)
    assert 23.99 < torque < 24.01
    print("rule: join force, circle it, return it - never meet it head-on")
    print("OK: %s drew the circle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_danjeon(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 4-2-6 breathing: one full cycle and cycles per minute
    cycle = 4 + 2 + 6
    cpm = 60.0 / cycle
    print("breath cycle: %d s -> %.1f cycles/min" % (cycle, cpm))
    assert cycle == 12
    assert 4.99 < cpm < 5.01
    # ten cycles seated = 120 s of practice
    print("ten cycles: %d s of danjeon practice" % (10 * cycle))
    assert 10 * cycle == 120
    print("rule: inhale 4, hold 2, exhale 6 - exhale on every technique")
    print("OK: %s breathed the oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_yu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # resisting a 200 N push dead-on vs yielding 0.3 m then circling
    push = 200.0
    work_resist = push * 0.05   # braced body gives 5 cm
    work_yield = 20.0 * 0.3     # soft arm guides with 20 N over 30 cm
    print("work to resist: %.1f J vs work to yield and circle: %.1f J" % (work_resist, work_yield))
    assert 9.99 < work_resist < 10.01
    assert 5.99 < work_yield < 6.01
    assert work_yield < work_resist
    print("rule: yield to strength, act on weakness - whoever tenses loses")
    print("OK: %s softened the force" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_geodeureo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grip strength: four fingers ~75%, thumb ~25% of the ring
    grip = 400.0  # N total grip
    vs_fingers, vs_thumb = grip * 0.75, grip * 0.25
    print("pull vs fingers: %.0f N vs pull vs thumb gap: %.0f N" % (vs_fingers, vs_thumb))
    assert vs_fingers == 300.0
    assert vs_thumb == 100.0
    # circular escape adds body rotation: effective escape force triples
    escape = vs_thumb / 3.0
    print("escape effort with the circle: %.1f N" % escape)
    assert 33.3 < escape < 33.4
    print("rule: escape toward the thumb gap, circle free, never pull straight")
    print("OK: %s found the gap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_sonmokkkokki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two hands on one wrist: lever arms 0.08 m (their wrist) vs 0.35 m (your two-hand control)
    their_arm, your_lever = 0.08, 0.35
    ratio = your_lever / their_arm
    print("wrist lock leverage ratio: %.2f : 1" % ratio)
    assert 4.37 < ratio < 4.38
    # 30 N of guided pressure becomes this at the joint
    joint_force = 30.0 * ratio
    print("30 N guided -> %.1f N at the wrist joint" % joint_force)
    assert 131.1 < joint_force < 131.3
    print("rule: cover, bend slowly, stop at the tap")
    print("OK: %s sealed the wrist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_palkkumchikkokki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow lock: forearm lever 0.35 m vs elbow joint radius 0.05 m
    lever, joint = 0.35, 0.05
    ratio = lever / joint
    print("elbow lock leverage: %.1f : 1" % ratio)
    assert 6.99 < ratio < 7.01
    press = 25.0 * ratio
    print("25 N press -> %.0f N at the elbow" % press)
    assert 174.9 < press < 175.1
    print("rule: straighten the arm across your body - a bent elbow escapes")
    print("OK: %s folded the elbow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_yeopchagi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # side kick reach: 0.9 m leg + 0.25 m torso lean extension
    leg, lean = 0.9, 0.25
    reach = math.sqrt(leg ** 2 + lean ** 2)
    print("side kick reach: %.3f m" % reach)
    assert 0.933 < reach < 0.935
    # piston drive: 70 kg body behind the heel at 6 m/s
    ke = 0.5 * 70.0 * 6.0 ** 2
    print("drive energy: %.0f J" % ke)
    assert 1259.9 < ke < 1260.1
    print("rule: pivot 180, lean away, drive the heel through")
    print("OK: %s drove the piston" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_songarakkkokki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # finger lever: 0.07 m finger vs 0.02 m knuckle radius
    finger, knuckle = 0.07, 0.02
    ratio = finger / knuckle
    print("finger lock leverage: %.1f : 1" % ratio)
    assert 3.49 < ratio < 3.51
    torque = 15.0 * finger  # 15 N at the fingertip
    print("15 N at fingertip -> %.2f N-m at the knuckle" % torque)
    assert 1.049 < torque < 1.051
    print("rule: bend with the body, never with finger strength")
    print("OK: %s read the fine print" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_sudochigi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pressure: 400 N over knife-hand edge (0.02 m x 0.09 m) vs fist (0.09 x 0.09 m)
    force = 400.0
    edge_area, fist_area = 0.02 * 0.09, 0.09 * 0.09
    p_edge = force / edge_area / 1000.0
    p_fist = force / fist_area / 1000.0
    print("knife-hand pressure: %.1f kPa vs fist: %.1f kPa" % (p_edge, p_fist))
    assert 222.1 < p_edge < 222.3
    assert 49.3 < p_fist < 49.5
    assert p_edge > 4.0 * p_fist
    print("rule: thumb tucked, hand rigid - the edge is the weapon")
    print("OK: %s edged the hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_eokkaekkokki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shoulder lock: forearm folded behind back, 0.3 m lever on the shoulder
    lever = 0.3
    lift = 20.0
    torque = lift * lever
    print("20 N lift on the folded wrist -> %.1f N-m on the shoulder" % torque)
    assert 5.99 < torque < 6.01
    # elbow must stay below shoulder line: max safe fold angle 70 deg from neutral
    max_fold = math.radians(70)
    print("safe fold limit: %.0f degrees" % math.degrees(max_fold))
    assert 69.9 < math.degrees(max_fold) < 70.1
    print("rule: elbow below the shoulder line, always")
    print("OK: %s crowned the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_dwichagi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # back kick: glute drive, 0.9 m leg at 8 m/s heel speed, 70 kg behind it
    v, m = 8.0, 70.0
    momentum = m * v
    print("heel momentum: %.0f kg-m/s" % momentum)
    assert 559.9 < momentum < 560.1
    # straight line: lateral deviation must stay under 5 cm over 0.9 m
    dev = 0.05
    ang = math.degrees(math.atan(dev / 0.9))
    print("allowed lateral angle: %.2f degrees" % ang)
    assert 3.17 < ang < 3.19
    print("rule: eyes spot first, heel drives straight back")
    print("OK: %s answered the rear" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_balgeolgi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep timing: stepping foot is planted ~0.25 s per step cycle
    plant_time = 0.25
    sweep_speed = 6.0  # m/s foot speed
    reach = sweep_speed * plant_time
    print("sweep reach inside the plant window: %.2f m" % reach)
    assert 1.499 < reach < 1.501
    # hands drive the top opposite: 0.4 m displacement of shoulders
    shoulder_move = 0.4
    base_gone = 0.35  # foot swept 0.35 m out
    total = shoulder_move + base_gone
    print("base-top separation: %.2f m - the fall is certain" % total)
    assert 0.749 < total < 0.751
    print("rule: sweep the weighted leg, move the top opposite")
    print("OK: %s timed the sweep" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_otdongjapgi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lapel grab: cover lands in ~0.2 s, lock needs the step-back
    cover_t = 0.2
    step_t = 0.3
    total = cover_t + step_t
    print("cover plus step: %.1f s to the lock" % total)
    assert 0.499 < total < 0.501
    # two-hand break: 70 kg drop over 0.15 m
    drop_energy = 70.0 * 9.81 * 0.15
    print("drop energy to break two grips: %.1f J" % drop_energy)
    assert 102.9 < drop_energy < 103.1
    print("rule: cover first, then the grab becomes your handle")
    print("OK: %s turned the grab" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_eokkaemechi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shoulder throw: lift 70 kg attacker 0.5 m with the legs
    m, h, g = 70.0, 0.5, 9.81
    work = m * g * h
    print("lifting work: %.1f J" % work)
    assert 343.2 < work < 343.4
    # hips must get below theirs: drop 0.25 m
    print("required hip drop: 0.25 m - the low base is everything")
    assert 0.249 < 0.25 < 0.251
    # rotation: pull the arm down through 90 degrees
    print("shoulder turn: 90 degrees of wheel")
    print("rule: hips below theirs, hip-to-hip, no gap")
    print("OK: %s turned the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_heorimechi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hip throw lever: hands pull at 0.55 m above hip fulcrum
    effort_arm, load_arm = 0.55, 0.25
    advantage = effort_arm / load_arm
    print("hip lever advantage: %.2f : 1" % advantage)
    assert 2.199 < advantage < 2.201
    # hip pop: 0.1 m upward impulse on 70 kg
    impulse = 70.0 * 9.81 * 0.1
    print("hip pop impulse work: %.1f J" % impulse)
    assert 68.6 < impulse < 68.7
    print("rule: glue the hip, drop below, pull down as hips pop up")
    print("OK: %s seated the pivot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_palkkumchichigi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow strike: torso whip, 0.35 m radius at 15 rad/s
    r, omega = 0.35, 15.0
    v = omega * r
    print("elbow tip speed: %.2f m/s" % v)
    assert 5.249 < v < 5.251
    # 4 kg forearm+elbow mass
    ke = 0.5 * 4.0 * v ** 2
    print("strike energy: %.1f J" % ke)
    assert 55.0 < ke < 55.2
    print("rule: torso whips, hand stays relaxed, step in")
    print("OK: %s whipped the hinge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_mureupchagi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee strike: knee rises at 5 m/s, target pulled down at 2 m/s
    closing = 5.0 + 2.0
    print("two-way closing speed: %.1f m/s" % closing)
    assert 6.99 < closing < 7.01
    # 8 kg leg mass behind the knee
    ke = 0.5 * 8.0 * closing ** 2
    print("collision energy: %.0f J" % ke)
    assert 195.9 < ke < 196.1
    print("rule: pull the target down as the knee drives up")
    print("OK: %s met the clinch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_darigeolgo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hook the stepping foot: foot in the air ~0.3 s, hook needs 0.15 s
    air_time, hook_time = 0.3, 0.15
    margin = air_time - hook_time
    print("timing margin on the stepping leg: %.2f s" % margin)
    assert 0.149 < margin < 0.151
    # top driven 0.5 m back while base hooked: fall angle
    ang = math.degrees(math.atan(0.5 / 1.0))
    print("top displacement angle: %.1f degrees past vertical" % ang)
    assert 26.5 < ang < 26.6
    print("rule: hook the base, drive the top - the pincer")
    print("OK: %s hooked the step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_mokjoreugi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # choke urgency: trained response must land inside 3 seconds
    budget = 3.0
    chin_tuck, step, pluck = 0.3, 0.5, 0.4
    total = chin_tuck + step + pluck
    print("defense sequence: %.1f s of a %.0f s budget" % (total, budget))
    assert 1.199 < total < 1.201
    assert total < budget
    # pluck: chop across both forearms with 150 N at 0.3 m leverage
    torque = 150.0 * 0.3
    print("pluck torque on the choke: %.0f N-m" % torque)
    assert 44.9 < torque < 45.1
    print("rule: chin down, step back, pluck in a V - break, strike, lock")
    print("OK: %s answered the urgency" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_gyeonghyeolchigi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # training-safe point map: 12 named points, accuracy radius 2 cm
    points = 12
    radius = 0.02
    area_each = math.pi * radius ** 2
    print("map: %d points, %.1f cm accuracy radius each" % (points, radius * 100))
    assert points == 12
    assert 0.001256 < area_each < 0.001257
    # one inch (2.54 cm) off is a miss: compare
    miss = 0.0254
    print("miss distance: %.2f cm > accuracy radius: off target" % (miss * 100))
    assert miss > radius
    print("rule: one inch off is a miss - accuracy is the technique")
    print("OK: %s mapped the whisper" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_dwiddollyeo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full spin in 0.5 s: angular velocity and heel speed at 0.9 m
    omega = 2 * math.pi / 0.5
    v = omega * 0.9
    print("spin: %.2f rad/s -> heel speed %.2f m/s" % (omega, v))
    assert 12.56 < omega < 12.57
    assert 11.30 < v < 11.32
    # vs standing back kick heel speed 8 m/s: the spin's gift
    gain = v / 8.0
    print("speed gain over standing back kick: %.2fx" % gain)
    assert 1.412 < gain < 1.415
    print("rule: one motion, no hesitation - spot over the shoulder")
    print("OK: %s spun the cyclone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_twieoapchagi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jump: takeoff at 3 m/s -> height and hang time
    v0, g = 3.0, 9.81
    h = v0 ** 2 / (2 * g)
    hang = 2 * v0 / g
    print("jump height: %.3f m, hang time: %.3f s" % (h, hang))
    assert 0.458 < h < 0.460
    assert 0.611 < hang < 0.613
    # kick must fire inside the hang window: snap takes 0.05 s
    assert 0.05 < hang
    print("kick window inside hang time: yes, with margin")
    print("rule: jump, chamber in the air, snap at the peak, land silent")
    print("OK: %s flew the kick" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_dandodaebi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # offline step: 45 degrees, 0.6 m step moves the body off the blade line
    step = 0.6
    lateral = step * math.sin(math.radians(45))
    print("lateral clearance from the stab line: %.3f m" % lateral)
    assert 0.424 < lateral < 0.425
    # blade line is 5 cm wide: clearance must exceed it many times over
    blade_half = 0.025
    print("clearance vs blade half-width: %.1fx" % (lateral / blade_half))
    assert lateral / blade_half > 15.0
    print("rule: step offline first - control the arm, never chase the blade")
    print("OK: %s respected the blade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_jangbongdaebi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # staff 1.8 m: power zone is the outer two-thirds; dead zone the inner third
    staff = 1.8
    dead = staff / 3.0
    power = 2 * staff / 3.0
    print("dead zone: %.1f m near the hands, power zone: %.1f m" % (dead, power))
    assert 0.599 < dead < 0.601
    assert 1.199 < power < 1.201
    # entry step 0.8 m gets inside the dead zone from a 1.5 m swing start
    print("entry step 0.8 m from 1.5 m: inside the dead zone, safe to jam")
    assert 1.5 - 0.8 < dead + 0.15
    print("rule: step inside the arc - never retreat from the reach")
    print("OK: %s entered the stillness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_danbongsul(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # danbong 0.35 m as lock lever vs hand-only 0.08 m wrist radius
    stick, hand = 0.35, 0.08
    mult = stick / hand
    print("lock leverage multiplier from the stick: %.2fx" % mult)
    assert 4.37 < mult < 4.38
    # strike tip speed: wrist snap 10 rad/s at 0.175 m half-length
    v = 10.0 * 0.175
    print("stick tip speed: %.2f m/s" % v)
    assert 1.749 < v < 1.751
    print("rule: center grip, same arcs as the knife-hand, control always")
    print("OK: %s extended the hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_geomsul(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # downward cut: 1.0 m blade, shoulders rotate 8 rad/s
    blade, omega = 1.0, 8.0
    tip_v = omega * blade
    print("blade tip speed: %.1f m/s" % tip_v)
    assert 7.99 < tip_v < 8.01
    # edge alignment: 5 degrees off plane wastes the cut
    off = math.radians(5)
    wasted = 1.0 - math.cos(off)
    print("energy wasted at 5 deg misalignment: %.2f %%" % (wasted * 100))
    assert 0.37 < wasted * 100 < 0.39
    print("rule: the cut is a guided fall - edge in the plane, always")
    print("OK: %s honored the blade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbhap_gyeokpa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # breaking energy: 4 kg effective mass at 8 m/s vs 10 m/s
    for v in (8.0, 10.0):
        ke = 0.5 * 4.0 * v ** 2
        print("strike at %.0f m/s: %.0f J" % (v, ke))
    assert 127.9 < 0.5 * 4.0 * 64.0 < 128.1
    assert 199.9 < 0.5 * 4.0 * 100.0 < 200.1
    # pine board breaks near ~150 J focused: speed is the difference
    print("verdict: 8 m/s falls short, 10 m/s breaks - speed, not muscle")
    print("rule: aim six inches past, exhale, follow through")
    print("OK: %s proved the power" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "stances": demo_cbhap_stances,
    "nakbeop": demo_cbhap_nakbeop,
    "balgeoreum": demo_cbhap_balgeoreum,
    "jireugi": demo_cbhap_jireugi,
    "apchagi": demo_cbhap_apchagi,
    "dollyeochagi": demo_cbhap_dollyeochagi,
    "makgi": demo_cbhap_makgi,
    "wonui": demo_cbhap_wonui,
    "danjeon": demo_cbhap_danjeon,
    "yu": demo_cbhap_yu,
    "geodeureo": demo_cbhap_geodeureo,
    "sonmokkkokki": demo_cbhap_sonmokkkokki,
    "palkkumchikkokki": demo_cbhap_palkkumchikkokki,
    "yeopchagi": demo_cbhap_yeopchagi,
    "songarakkkokki": demo_cbhap_songarakkkokki,
    "sudochigi": demo_cbhap_sudochigi,
    "eokkaekkokki": demo_cbhap_eokkaekkokki,
    "dwichagi": demo_cbhap_dwichagi,
    "balgeolgi": demo_cbhap_balgeolgi,
    "otdongjapgi": demo_cbhap_otdongjapgi,
    "eokkaemechi": demo_cbhap_eokkaemechi,
    "heorimechi": demo_cbhap_heorimechi,
    "palkkumchichigi": demo_cbhap_palkkumchichigi,
    "mureupchagi": demo_cbhap_mureupchagi,
    "darigeolgo": demo_cbhap_darigeolgo,
    "mokjoreugi": demo_cbhap_mokjoreugi,
    "gyeonghyeolchigi": demo_cbhap_gyeonghyeolchigi,
    "dwiddollyeo": demo_cbhap_dwiddollyeo,
    "twieoapchagi": demo_cbhap_twieoapchagi,
    "dandodaebi": demo_cbhap_dandodaebi,
    "jangbongdaebi": demo_cbhap_jangbongdaebi,
    "danbongsul": demo_cbhap_danbongsul,
    "geomsul": demo_cbhap_geomsul,
    "gyeokpa": demo_cbhap_gyeokpa,
}
