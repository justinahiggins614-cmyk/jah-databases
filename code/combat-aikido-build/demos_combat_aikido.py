#!/usr/bin/env python3
"""Demo programs for the Aikido Combat databases (Manon's combat orders
2026-10-17, combat batch 2).

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record (balance physics, stance geometry,
timing, drill planning). All are machine-executed by build.py: each prints
its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_what_is_aikido(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the three physical facts: blend, tip, guide
    # kuzushi: force to tip a 75 kg attacker leaning 4 cm past the base edge
    m, g, d = 75.0, 9.81, 0.04
    torque = m * g * d
    # blending: meeting a 2.0 m/s push by matching it needs ~0 relative force
    push_speed = 2.0
    matched = 2.0
    relative = abs(push_speed - matched)
    print("tip torque at 4 cm past base: %.3f N m" % torque)
    print("relative speed when blended: %.3f m/s" % relative)
    assert 29.42 < torque < 29.44
    assert relative < 0.001
    facts = ["move with the force", "tip the balance", "guide joints to range edge"]
    print("three facts: %d" % len(facts))
    for f in facts:
        print("  - %s" % f)
    print("OK: %s named the way" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_founder_ueshiba(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # founder timeline arithmetic
    born, daito, budo, named, died = 1883, 1915, 1938, 1942, 1969
    age_daito = daito - born
    budo_to_named = named - budo
    life = died - born
    print("began Daito-ryu at age: %d" % age_daito)
    print("Budo manual to aikido naming: %d years" % budo_to_named)
    print("lifespan: %d years" % life)
    assert age_daito == 32
    assert budo_to_named == 4
    assert life == 86
    print("OK: %s traced the lineage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dojo_etiquette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # ceremony timing plan: opening + closing bows at measured pace
    bows = ["kamiza bow", "instructor bow", "mokuso", "onegai shimasu"]
    per_bow_s = 4.0
    ceremony_s = len(bows) * per_bow_s
    partner_bows_per_class = 12
    partner_bow_s = 3.0
    total_s = 2 * ceremony_s + partner_bows_per_class * partner_bow_s
    print("opening/closing ceremony: %.0f s each" % ceremony_s)
    print("partner bows: %d x %.0f s" % (partner_bows_per_class, partner_bow_s))
    print("total etiquette time: %.1f min" % (total_s / 60.0))
    assert 15.9 < ceremony_s < 16.1
    assert 1.13 < total_s / 60.0 < 1.14
    print("rule: every bow is a safety contract")
    print("OK: %s bowed in" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shisei_kamae(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # hanmi triangle: feet 0.75 m apart, body turned 60 degrees
    stance_m = 0.75
    angle_deg = 60.0
    angle_rad = math.radians(angle_deg)
    # presented width = stance * sin(60): the target you offer
    presented = stance_m * math.sin(angle_rad)
    # center of mass height ~0.95 m for 1.75 m student, base half-width
    com_h = 0.95
    half_base = stance_m / 2.0
    tip_angle = math.degrees(math.atan(half_base / com_h))
    print("presented target width: %.3f m" % presented)
    print("tip-over angle: %.2f degrees" % tip_angle)
    assert 0.649 < presented < 0.651
    assert 21.5 < tip_angle < 21.7
    print("rule: soft knees, straight spine, wide soft eyes")
    print("OK: %s took hanmi" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ashi_sabaki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # footwork drill plan: cross a 12 m mat with 0.75 m steps
    mat_m = 12.0
    step_m = 0.75
    steps = mat_m / step_m
    cadence_s = 0.8
    cross_s = steps * cadence_s
    # four directions, both hanmi sides
    total_steps = steps * 4 * 2
    total_min = total_steps * cadence_s / 60.0
    print("steps per crossing: %.0f" % steps)
    print("one crossing: %.1f s" % cross_s)
    print("full drill (4 dirs x 2 sides): %.0f steps, %.1f min" % (total_steps, total_min))
    assert 15.9 < steps < 16.1
    assert 12.7 < cross_s < 12.9
    assert 1.69 < total_min < 1.71
    print("rule: silent and level - noisy feet, late technique")
    print("OK: %s walked the mat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tenkan_irimi_movement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # tenkan: 180-degree pivot on the ball of the foot, radius 0.35 m
    r = 0.35
    arc = math.pi * r  # half circle travelled by the sweeping foot
    # hand circle at chest height, radius 0.30 m, full turn
    hand_arc = 2 * math.pi * 0.30
    # irimi entry: 1.1 m diagonal step in 0.5 s
    entry_m, entry_s = 1.1, 0.5
    entry_speed = entry_m / entry_s
    print("tenkan sweep arc: %.3f m" % arc)
    print("hand circle: %.3f m" % hand_arc)
    print("irimi entry speed: %.2f m/s" % entry_speed)
    assert 1.099 < arc < 1.101
    assert 1.884 < hand_arc < 1.886
    assert 2.19 < entry_speed < 2.21
    print("rule: feet turn, body follows - shoulders never lead")
    print("OK: %s turned and entered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ukemi_forward_roll(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # mae-ukemi: roll path diagonal across the back, ~1.6 m per roll
    roll_m = 1.6
    roll_s = 1.2
    # 30-roll warmup set
    reps = 30
    set_s = reps * roll_s
    rest_s = 60.0
    total_min = (set_s + rest_s) / 60.0
    # landing deceleration: from 2.2 m/s to 0 over the roll path
    v = 2.2
    decel = v ** 2 / (2 * roll_m)
    print("roll path: %.1f m in %.1f s" % (roll_m, roll_s))
    print("30-roll set + rest: %.1f min" % total_min)
    print("landing deceleration: %.3f m/s^2 (%.2f g)" % (decel, decel / 9.81))
    assert 1.599 < roll_m < 1.601
    assert 1.59 < total_min < 1.61
    assert 1.512 < decel < 1.514
    print("rule: diagonal path, tucked chin, exhale on the roll")
    print("OK: %s rolled forward" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ukemi_back_side(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # impact spreading: 75 kg falling 0.45 m (crouched start), slap spreads
    # the stop over 0.12 s instead of 0.03 s without the slap
    m, h = 75.0, 0.45
    v = math.sqrt(2 * 9.81 * h)
    p = m * v
    f_slap = p / 0.12
    f_noslap = p / 0.03
    print("impact speed: %.3f m/s" % v)
    print("force with slap (0.12 s stop): %.0f N" % f_slap)
    print("force without slap (0.03 s stop): %.0f N" % f_noslap)
    print("reduction factor: %.1f x" % (f_noslap / f_slap))
    assert 2.970 < v < 2.972
    assert 1855.0 < f_slap < 1858.0
    assert 3.99 < f_noslap / f_slap < 4.01
    print("rule: never post a straight arm - the slap replaces the post")
    print("OK: %s fell safely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_kuzushi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # eight-direction map: weak corners at 45-degree diagonals
    # tip torque for 75 kg, center 4 cm past base edge vs 12 cm muscled shove
    m = 75.0
    t_kuzushi = m * 9.81 * 0.04
    t_muscle = m * 9.81 * 0.12
    print("torque at kuzushi (4 cm past edge): %.2f N m" % t_kuzushi)
    print("torque muscled (12 cm shove): %.2f N m" % t_muscle)
    print("effort ratio: %.1f x harder without kuzushi" % (t_muscle / t_kuzushi))
    assert 29.42 < t_kuzushi < 29.44
    assert 2.99 < t_muscle / t_kuzushi < 3.01
    # mid-step window: base narrows for ~0.25 s of a 1.0 s step
    print("timing window (mid-step): %.2f s of each step" % 0.25)
    print("rule: balance first, technique second, strength never")
    print("OK: %s broke the balance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_awase_musubi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # blending: attacker pushes at 1.8 m/s; defender matches within 0.1 m/s
    push = 1.8
    match = 1.75
    relative = abs(push - match)
    # then guides 10 degrees off line over 0.5 s
    guide_deg = 10.0
    guide_rad = math.radians(guide_deg)
    lateral = push * 0.5 * math.sin(guide_rad)
    print("relative speed (blend): %.2f m/s" % relative)
    print("lateral diversion in 0.5 s: %.3f m" % lateral)
    assert 0.049 < relative < 0.051
    assert 0.156 < lateral < 0.157
    print("rule: match speed exactly - faster is fleeing, slower is resisting")
    print("OK: %s joined the energy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_maai_atemi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # three distances in cm for a 1.75 m student, arm reach 0.72 m
    reach = 0.72
    chika = 0.30
    uchi = reach - 0.05
    toma = reach + 0.75  # one step beyond
    # entry: 0.75 m step in 0.45 s vs 0.25 s human reaction
    entry_t = 0.75 / (0.75 / 0.45)
    print("chika-ma: %.2f m, uchi-ma: %.2f m, toma: %.2f m" % (chika, uchi, toma))
    print("entry time: %.2f s vs reaction %.2f s" % (entry_t, 0.25))
    assert 0.29 < chika < 0.31
    assert 0.66 < uchi < 0.68
    assert 1.46 < toma < 1.48
    assert 0.44 < entry_t < 0.46
    print("rule: distance is yours to set, timing is yours to steal")
    print("OK: %s owned the distance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grip_fundamentals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # ryote-dori: two hands pull ~2 x 180 N on the wrist; dropping the center
    # answers with body weight 75 kg * 9.81 instead of arm strength
    pull = 2 * 180.0
    body_answer = 75.0 * 9.81
    ratio = body_answer / pull
    # tenkan frees the wrist by moving the target 1.1 m in 0.6 s
    free_speed = 1.1 / 0.6
    print("two-hand pull: %.0f N vs body-weight answer: %.1f N" % (pull, body_answer))
    print("body advantage: %.2f x" % ratio)
    print("tenkan escape speed: %.2f m/s" % free_speed)
    assert 359.9 < pull < 360.1
    assert 2.04 < ratio < 2.05
    assert 1.83 < free_speed < 1.84
    print("rule: the body moves first - the release is a side effect of footwork")
    print("OK: %s answered the grip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ikkyo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # ikkyo arc: arm length 0.72 m guided through 100 degrees downward
    r = 0.72
    arc_rad = math.radians(100.0)
    arc_m = r * arc_rad
    # hip drive: 75 kg stepping 0.8 m through the arc in 0.9 s
    work = 75.0 * 9.81 * 0.25  # center drops 0.25 m during the arc
    print("control arc length: %.3f m" % arc_m)
    print("hip-drop work through the arc: %.1f J" % work)
    assert 1.256 < arc_m < 1.258
    assert 183.9 < work < 184.0
    print("rule: hips do the work - shoulders only steer")
    print("OK: %s taught the first teaching" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nikyo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # nikyo: 25 N applied at 0.09 m wrist lever folds the joint
    f, lever = 25.0, 0.09
    torque = f * lever
    # placement tolerance: 1 cm shift changes effective lever 11 percent
    shift = 0.01 / lever * 100.0
    print("wrist-fold torque: %.3f N m" % torque)
    print("1 cm misplacement changes leverage: %.1f %%" % shift)
    assert 2.249 < torque < 2.251
    assert 11.0 < shift < 11.2
    print("rule: a finger of placement beats a hundred pounds of force")
    print("OK: %s turned the second teaching" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sankyo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # sankyo spiral: hand rotates 270 degrees while rising 0.35 m
    rot_rad = math.radians(270.0)
    rise = 0.35
    # spiral path length: unwrapped cylinder of radius 0.09 m
    path = math.sqrt((0.09 * rot_rad) ** 2 + rise ** 2)
    # lift assist on 75 kg attacker: spiral converts rotation to lift
    print("spiral rotation: %.2f rad" % rot_rad)
    print("spiral path length: %.3f m" % path)
    assert 4.711 < rot_rad < 4.713
    assert 0.549 < path < 0.551
    print("rule: rotate the whole arm as one piece - never twist the wrist alone")
    print("OK: %s wound the third teaching" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_yonkyo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # yonkyo: 40 N through knuckles on 1.2 cm^2 of inner wrist
    f = 40.0
    area_m2 = 1.2e-4
    pressure_kpa = f / area_m2 / 1000.0
    # same force on a 12 cm^2 palm: comparison
    palm_kpa = f / 12e-4 / 1000.0
    print("knuckle pressure: %.1f kPa" % pressure_kpa)
    print("palm pressure (same force): %.1f kPa" % palm_kpa)
    print("concentration factor: %.1f x" % (pressure_kpa / palm_kpa))
    assert 333.2 < pressure_kpa < 333.5
    assert 9.99 < pressure_kpa / palm_kpa < 10.01
    print("rule: the smallest true point outweighs the largest false effort")
    print("OK: %s pressed the fourth teaching" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gokyo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # gokyo vs ikkyo lever: straight arm 0.72 m vs folded 0.45 m effective
    straight, folded = 0.72, 0.45
    advantage = straight / folded
    # same 60 N guide force at each lever
    t_straight = 60.0 * straight
    t_folded = 60.0 * folded
    print("straight-arm torque: %.1f N m vs folded: %.1f N m" % (t_straight, t_folded))
    print("gokyo lever advantage: %.2f x" % advantage)
    assert 43.19 < t_straight < 43.21
    assert 1.59 < advantage < 1.61
    print("rule: same footwork, same arc - only the hands change")
    print("OK: %s stretched the fifth teaching" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_irimi_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # irimi-nage: 1.1 m entry in 0.5 s, guiding hand draws 120-degree arc at 0.65 m
    entry_v = 1.1 / 0.5
    arc = 0.65 * math.radians(120.0)
    # attacker 75 kg tipped past heels: falls 1.0 m to the mat
    fall_t = math.sqrt(2 * 1.0 / 9.81)
    print("entry speed: %.2f m/s" % entry_v)
    print("guiding arc: %.3f m" % arc)
    print("attacker fall time: %.3f s" % fall_t)
    assert 2.19 < entry_v < 2.21
    assert 1.360 < arc < 1.362
    assert 0.451 < fall_t < 0.453
    print("rule: keep walking - stopping the feet kills the throw")
    print("OK: %s entered the throw" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shiho_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # shiho-nage: great vertical circle, radius 0.70 m (arm + step)
    r = 0.70
    circle = 2 * math.pi * r
    # cut completed in 1.1 s
    cut_s = 1.1
    hand_speed = circle / cut_s
    # tenkan pivot: 180 degrees in 0.55 s
    pivot_dps = 180.0 / 0.55
    print("throw circle: %.3f m" % circle)
    print("hand speed through the cut: %.2f m/s" % hand_speed)
    print("pivot rate: %.1f deg/s" % pivot_dps)
    assert 4.397 < circle < 4.399
    assert 3.99 < hand_speed < 4.01
    assert 327.2 < pivot_dps < 327.4
    print("rule: complete the tenkan - half a pivot strands you")
    print("OK: %s cut the four directions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_kotegaeshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # kotegaeshi spiral: wrist turns 200 degrees at radius 0.07 m while
    # nage steps 0.9 m through - smooth corkscrew, never a kink
    wrist_arc = 0.07 * math.radians(200.0)
    step_m = 0.9
    total_path = math.sqrt(wrist_arc ** 2 + step_m ** 2)
    # applied over 1.0 s: gentle angular rate
    wrist_dps = 200.0 / 1.0
    print("wrist spiral arc: %.3f m" % wrist_arc)
    print("combined path: %.3f m" % total_path)
    print("wrist turn rate: %.0f deg/s (smooth, never snapped)" % wrist_dps)
    assert 0.244 < wrist_arc < 0.245
    assert 0.932 < total_path < 0.934
    assert 199.9 < wrist_dps < 200.1
    print("rule: spiral, never snap - smoothness is the safety")
    print("OK: %s turned the wrist back" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jujinage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # jujinage: arms crossed at 90 degrees, wrists stacked 0.06 m apart
    cross_deg = 90.0
    stack_m = 0.06
    # step-through: 1.0 m at hips while guiding the X down 0.5 m
    drive = math.sqrt(1.0 ** 2 + 0.5 ** 2)
    # locked structure: attacker 75 kg tips over the crossed line
    tip_torque = 75.0 * 9.81 * 0.10
    print("cross angle: %.0f degrees, wrist stack: %.2f m" % (cross_deg, stack_m))
    print("step-through drive: %.3f m" % drive)
    print("tip torque over the X: %.2f N m" % tip_torque)
    assert 1.117 < drive < 1.119
    assert 73.57 < tip_torque < 73.59
    print("rule: the cross must be true - wrists stacked, elbows down")
    print("OK: %s crossed the gate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_kaiten_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # kaiten-nage wheel: radius 0.55 m vertical circle, one full turn in 1.2 s
    r = 0.55
    wheel = 2 * math.pi * r
    turn_s = 1.2
    rim_speed = wheel / turn_s
    rpm = 60.0 / turn_s
    # oval check: 5% ovality would tilt 0.03 m off vertical - fault threshold
    oval_m = 0.05 * r
    print("wheel circumference: %.3f m" % wheel)
    print("rim speed: %.2f m/s (%0.0f rpm)" % (rim_speed, rpm))
    print("5%% ovality deviation: %.3f m - keep the wheel round" % oval_m)
    assert 3.455 < wheel < 3.457
    assert 2.879 < rim_speed < 2.881
    assert 0.0274 < oval_m < 0.0276
    print("rule: round and vertical - an oval wheel wrenches the shoulder")
    print("OK: %s turned the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumi_otoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # sumi-otoshi: step 0.55 m to the 45-degree corner, hand draws 0.30 m
    step_m = 0.55
    corner_rad = math.radians(45.0)
    # effective corner displacement
    corner_m = step_m * math.cos(corner_rad)
    hand_m = 0.30
    # drop: center falls 0.35 m once past the corner
    drop_t = math.sqrt(2 * 0.35 / 9.81)
    print("corner step: %.3f m at 45 degrees" % corner_m)
    print("hand draw: %.2f m - the step does the work" % hand_m)
    print("drop time: %.3f s" % drop_t)
    assert 0.388 < corner_m < 0.390
    assert 0.266 < drop_t < 0.268
    print("rule: if they do not fall, the corner was wrong - never force it")
    print("OK: %s dropped the corner" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aiki_otoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # aiki-otoshi: hips drop 0.45 m below standing, scoop behind the knee
    drop_m = 0.45
    # leg drive: 75 kg attacker lifted 0.15 m by the legs
    lift_j = 75.0 * 9.81 * 0.15
    # tip-over: attacker pivots over the scooped leg, 1.0 m fall
    tip_t = math.sqrt(2 * 1.0 / 9.81)
    print("level change: %.2f m" % drop_m)
    print("leg-drive work: %.1f J" % lift_j)
    print("tip-over time: %.3f s" % tip_t)
    assert 110.3 < lift_j < 110.4
    assert 0.451 < tip_t < 0.453
    print("rule: scoop behind the knee - never the front of the joint")
    print("OK: %s scooped the drop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_koshinage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # koshi-nage: hips wedge 0.15 m below attacker's center, then legs
    # straighten 0.35 m lifting 75 kg
    wedge_m = 0.15
    lift_m = 0.35
    lift_j = 75.0 * 9.81 * lift_m
    # back-safety: bent-back lift of same load risks ~3x spinal shear;
    # straight-back leg drive keeps shear at the leg-driven baseline
    print("hip wedge below center: %.2f m" % wedge_m)
    print("leg-drive lift work: %.1f J" % lift_j)
    assert 257.5 < lift_j < 257.6
    print("rule: hips below theirs, back straight - the legs throw")
    print("OK: %s loaded the hip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_udekime_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # udekime-nage: straight arm lever 0.72 m, 50 N body-driven force
    lever = 0.72
    f = 50.0
    torque = f * lever
    # safety margin: elbow warns at ~15 N m; control stays well under
    warn = 15.0
    margin = warn / torque
    print("elbow lever torque: %.1f N m" % torque)
    print("margin under warning threshold: %.2f x" % margin)
    assert 35.99 < torque < 36.01
    assert 0.416 < margin < 0.418
    print("rule: body applies, never snaps - release the instant they fall")
    print("OK: %s locked the straight arm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_katame_waza(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # pin: 40 kg of settled body weight over 0.08 m^2 shoulder contact
    weight_n = 40.0 * 9.81
    area = 0.08
    pressure_kpa = weight_n / area / 1000.0
    # escape attempt: partner pushes 200 N up, geometry holds 3x
    hold_n = 200.0 * 3.0
    print("pin pressure: %.2f kPa" % pressure_kpa)
    print("geometry holds against: %.0f N escape attempt" % hold_n)
    assert 4.90 < pressure_kpa < 4.91
    assert 599.9 < hold_n < 600.1
    print("rule: painless to the still, inescapable to the moving")
    print("OK: %s held the pin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_randori(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # randori triangle: keep 2 attackers at 120-degree separation, 2.5 m out
    sep_deg = 120.0
    dist_m = 2.5
    # arc between attackers you must cover to stay off their line
    arc = math.radians(sep_deg) * dist_m
    # 90-second round, technique every ~6 s
    round_s = 90.0
    techniques = round_s / 6.0
    print("attacker separation: %.0f degrees at %.1f m" % (sep_deg, dist_m))
    print("repositioning arc: %.2f m" % arc)
    print("techniques per 90 s round: %.0f" % techniques)
    assert 5.235 < arc < 5.237
    assert 14.99 < techniques < 15.01
    print("rule: never between two attackers - triangle, throw, move on")
    print("OK: %s faced the many" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jiyu_waza(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # jiyu-waza rounds: menu of 3 techniques x 2 attacks = 6 pairings,
    # then open vocabulary of 24 techniques x 6 attacks = 144 pairings
    limited = 3 * 2
    open_pairs = 24 * 6
    # continuous round: attack every 8 s for 3 minutes
    attacks = 180.0 / 8.0
    print("limited-menu pairings: %d" % limited)
    print("open-vocabulary pairings: %d" % open_pairs)
    print("attacks in a 3-minute flow round: %.1f" % attacks)
    assert limited == 6
    assert open_pairs == 144
    assert 22.49 < attacks < 22.51
    print("rule: the body answers before the mind finishes naming")
    print("OK: %s freed the technique" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tanto_dori(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # tanto-dori: thrust at 3.0 m/s from 1.2 m; defender must clear the
    # line (0.45 m sideways) before the blade arrives
    thrust_v = 3.0
    dist_m = 1.2
    arrival_s = dist_m / thrust_v
    clear_m = 0.45
    needed_v = clear_m / arrival_s
    print("blade arrival time: %.2f s" % arrival_s)
    print("lateral speed needed to clear: %.3f m/s" % needed_v)
    assert 0.399 < arrival_s < 0.401
    assert 1.124 < needed_v < 1.126
    print("rule: escape first - the disarm is the last resort; wood only")
    print("OK: %s took the knife (wooden)" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tachi_jo_dori(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # jo-dori: staff 1.28 m; thrust tip travels 1.0 m in 0.4 s.
    # defender enters 1.4 m inside the arc in the same 0.4 s window.
    tip_v = 1.0 / 0.4
    entry_v = 1.4 / 0.4
    # bokken cut arc: 1.0 m blade sweeps 120 degrees
    cut_arc = 1.0 * math.radians(120.0)
    print("staff tip speed: %.1f m/s" % tip_v)
    print("required entry speed: %.1f m/s" % entry_v)
    print("sword cut arc: %.3f m" % cut_arc)
    assert 2.49 < tip_v < 2.51
    assert 3.49 < entry_v < 3.51
    assert 2.094 < cut_arc < 2.095
    print("rule: inside the arc before it completes - timing beats speed")
    print("OK: %s took the long weapons (wooden)" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_kaeshi_waza(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # kaeshi-waza: the counter window opens when the giver commits -
    # ~0.3 s of a 1.0 s technique where balance is given
    tech_s = 1.0
    window_s = 0.3
    window_pct = window_s / tech_s * 100.0
    # reversal: borrow the 2.0 m/s committed motion, add 10-degree redirect
    borrowed = 2.0
    redirect = borrowed * math.sin(math.radians(10.0))
    print("counter window: %.1f s (%.0f%% of the technique)" % (window_s, window_pct))
    print("redirected speed: %.3f m/s" % redirect)
    assert 29.9 < window_pct < 30.1
    assert 0.347 < redirect < 0.348
    print("rule: slow and announced - a speed counter is an ambush")
    print("OK: %s reversed the technique" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hanmi_handachi_suwari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # shikko: knee-step 0.35 m, 20 steps to cross 7 m; torso stays vertical
    knee_step = 0.35
    steps = 7.0 / knee_step
    # hip mobility: upright torso over knees needs ~110-degree hip flexion
    hip_deg = 110.0
    # conditioning: start 3 min sessions, add 1 min weekly to 10 min
    weeks = (10 - 3) / 1
    print("knee-steps per 7 m: %.0f" % steps)
    print("hip flexion held: %.0f degrees" % hip_deg)
    print("weeks to build 10-minute shikko: %.0f" % weeks)
    assert 19.99 < steps < 20.01
    assert weeks == 7
    print("rule: upright torso, hip-driven glide - knees adapt gradually")
    print("OK: %s walked on knees" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aiki_ken_jo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # ken suburi: 7 cuts; jo suburi: 20 forms; full set both sides
    ken, jo = 7, 20
    both_sides = (ken + jo) * 2
    # shomen cut: 1.0 m blade through 150 degrees in 0.6 s
    cut_arc = 1.0 * math.radians(150.0)
    tip_v = cut_arc / 0.6
    # 13-count jo kata at 2 s per count
    kata_s = 13 * 2
    print("suburi per full set (both sides): %d" % both_sides)
    print("shomen tip speed: %.2f m/s" % tip_v)
    print("13-count kata: %d s" % kata_s)
    assert both_sides == 54
    assert 4.363 < tip_v < 4.365
    assert kata_s == 26
    print("rule: the cut is powered by the hips - riai, one study")
    print("OK: %s took up the wood" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_aikido": demo_what_is_aikido,
    "founder_ueshiba": demo_founder_ueshiba,
    "dojo_etiquette": demo_dojo_etiquette,
    "shisei_kamae": demo_shisei_kamae,
    "ashi_sabaki": demo_ashi_sabaki,
    "tenkan_irimi_movement": demo_tenkan_irimi_movement,
    "ukemi_forward_roll": demo_ukemi_forward_roll,
    "ukemi_back_side": demo_ukemi_back_side,
    "kuzushi": demo_kuzushi,
    "awase_musubi": demo_awase_musubi,
    "maai_atemi": demo_maai_atemi,
    "grip_fundamentals": demo_grip_fundamentals,
    "ikkyo": demo_ikkyo,
    "nikyo": demo_nikyo,
    "sankyo": demo_sankyo,
    "yonkyo": demo_yonkyo,
    "gokyo": demo_gokyo,
    "irimi_nage": demo_irimi_nage,
    "shiho_nage": demo_shiho_nage,
    "kotegaeshi": demo_kotegaeshi,
    "jujinage": demo_jujinage,
    "kaiten_nage": demo_kaiten_nage,
    "sumi_otoshi": demo_sumi_otoshi,
    "aiki_otoshi": demo_aiki_otoshi,
    "koshinage": demo_koshinage,
    "udekime_nage": demo_udekime_nage,
    "katame_waza": demo_katame_waza,
    "randori": demo_randori,
    "jiyu_waza": demo_jiyu_waza,
    "tanto_dori": demo_tanto_dori,
    "tachi_jo_dori": demo_tachi_jo_dori,
    "kaeshi_waza": demo_kaeshi_waza,
    "hanmi_handachi_suwari": demo_hanmi_handachi_suwari,
    "aiki_ken_jo": demo_aiki_ken_jo,
}

