#!/usr/bin/env python3
"""Demo programs for the Eskrima Kali Arnis Combat Database.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record (angle geometry, triangle footwork,
strike energy, drill rep math, leverage, timing windows). All are
machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker. Demo text is cross-checked against entry text: every number a
demo computes appears in its record's prose.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_eka_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three names of the art and the ladder schedule behind them
    names = {"eskrima": 7, "kali": 4, "arnis": 5}
    for n, ln in names.items():
        print("name %-8s letters %d" % (n, ln))
        assert ln == len(n)
    # training schedule: weeks per tier, 3 sessions of 60 minutes
    tiers = {"foundations": 12, "compounded": 16, "advanced": 24}
    total_min = sum(w * 3 * 60 for w in tiers.values())
    print("tier weeks:", tiers)
    print("total practice minutes to walk the ladder: %d" % total_min)
    assert total_min == 52 * 180
    assert 9359 < total_min < 9361
    print("rule: weapon, angle, triangle, drill - in that order")
    print("OK: %s framed the art" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_the_stick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stick lengths in inches converted to centimeters, plus reach
    arm_cm = 71.0  # ~28 inch arm
    for inches, expect_lo, expect_hi in ((26, 66.03, 66.05), (28, 71.11, 71.13), (30, 76.19, 76.21)):
        cm = inches * 2.54
        reach = arm_cm + cm
        print("stick %d in = %.2f cm, reach %.1f cm" % (inches, cm, reach))
        assert expect_lo < cm < expect_hi
    cm28 = 28 * 2.54
    reach_ft = (arm_cm + cm28) / 30.48
    print("28-inch stick reach: %.2f feet" % reach_ft)
    assert 4.65 < reach_ft < 4.67
    print("rule: the stick is the sword in disguise")
    print("OK: %s measured the weapon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_the_grip(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wrist snap tip speed: v = omega * L
    mass = 0.35      # kg, rattan stick
    length = 0.71    # m, 28 inches
    omega = 15.0     # rad/s wrist snap
    tip_speed = omega * length
    print("tip speed: %.2f m/s" % tip_speed)
    assert 10.64 < tip_speed < 10.66
    # kinetic energy at the tip
    ke = 0.5 * mass * tip_speed ** 2
    print("strike energy: %.2f J" % ke)
    assert 19.80 < ke < 19.90
    print("rule: loose on the travel, tight at impact")
    print("OK: %s timed the clutch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_stance_handa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weight distribution in handa: 60% rear, 40% lead
    body_kg = 75.0
    rear = body_kg * 0.60
    lead = body_kg * 0.40
    print("rear leg: %.1f kg, lead leg: %.1f kg" % (rear, lead))
    assert 44.99 < rear < 45.01
    assert 29.99 < lead < 30.01
    assert abs((rear + lead) - body_kg) < 0.01
    base_m = 0.45  # stance width in meters
    print("base width: %.2f m" % base_m)
    print("rule: sink an inch, blade the body, bring the live hand home")
    print("OK: %s held the stance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_angles_1_5(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # angle 1 geometry: diagonal at 45 degrees, stick length L
    L = 0.71
    ang = math.radians(45.0)
    dx = L * math.cos(ang)
    dy = L * math.sin(ang)
    print("angle-1 diagonal components: dx=%.4f m dy=%.4f m" % (dx, dy))
    assert 0.5019 < dx < 0.5021
    assert 0.5019 < dy < 0.5021
    # five angles cover four quadrants plus the centerline thrust
    print("angles 1-5: four quadrants plus the centerline")
    assert dx > 0 and dy > 0
    print("rule: every angle is both an attack and a defense")
    print("OK: %s drew the alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_angles_6_12(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twelve angles divide the circle around the target
    sector = 360.0 / 12.0
    print("twelve-angle sector: %.2f degrees" % sector)
    assert 29.99 < sector < 30.01
    # upper angles: rising cuts (6,7), verticals (8,9), low line (10,11), overhead (12)
    upper = {6: "rising backhand", 7: "rising forehand", 8: "vertical backhand",
             9: "vertical forehand", 10: "low forehand", 11: "low backhand",
             12: "overhead"}
    assert len(upper) == 7
    total = 5 + len(upper)
    print("full numerado: %d angles" % total)
    assert total == 12
    print("rule: confirm numbering with any new partner")
    print("OK: %s completed the circle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_footwork_sulong(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # forward triangle: equilateral, side 0.6 m; step base corner -> front point
    side = 0.6
    height = side * math.sqrt(3.0) / 2.0
    print("triangle height: %.4f m" % height)
    assert 0.5195 < height < 0.5197
    # two steps to close: base corner to side point to front point
    closed = 2 * side
    print("two-step advance covers: %.1f m" % closed)
    assert 1.19 < closed < 1.21
    print("rule: the feet deliver the weapon")
    print("OK: %s walked the triangle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_labtik(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full-power strike: kinetic chain energy at the tip
    mass = 0.35
    tip_speed = 10.65  # m/s from the grip demo chain
    ke = 0.5 * mass * tip_speed ** 2
    print("labtik strike energy: %.2f J" % ke)
    assert 19.80 < ke < 19.90
    # defang the snake: the weapon hand is ~0.15 m wide; accuracy window
    hand_m = 0.15
    print("defang target width: %.2f m" % hand_m)
    assert 0.149 < hand_m < 0.151
    # follow-through: six inches past the contact line
    follow_m = 6 * 0.0254
    print("follow-through: %.3f m past contact" % follow_m)
    assert 0.1523 < follow_m < 0.1525
    print("rule: strike through the target, not at it")
    print("OK: %s threw with the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_footwork_atras(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # retreat triangle: three retreat steps create distance while offline
    side = 0.6
    steps = 3
    distance = steps * side
    print("three retreat triangles: %.1f m of angled distance" % distance)
    assert 1.79 < distance < 1.81
    # angled vs straight: lateral offset after 3 steps (60-degree triangle legs)
    lateral = steps * side * math.sin(math.radians(60.0))
    print("lateral offset off the power line: %.3f m" % lateral)
    assert 1.558 < lateral < 1.560
    print("rule: never back straight up")
    print("OK: %s reloaded on the retreat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_defensa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # deflection: incoming force F met at 45 degrees; deflected component
    F = 200.0  # N incoming strike force
    meet_deg = 45.0
    slid = F * math.cos(math.radians(meet_deg))
    thru = F * math.sin(math.radians(meet_deg))
    print("incoming %.0f N -> slid offline %.1f N, through %.1f N" % (F, slid, thru))
    assert 141.41 < slid < 141.43
    assert 141.41 < thru < 141.43
    # four defenses answer four angle families
    defenses = ["outside block", "inside block", "roof block (payong)", "cross-block"]
    print("defenses: %d" % len(defenses))
    assert len(defenses) == 4
    print("rule: deflect, do not catch")
    print("OK: %s raised the shield" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_abaniko(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fan strike: wrist rotates 120-degree arc, radius 0.15 m, in 0.1 s
    arc_deg = 120.0
    radius = 0.15
    t = 0.1
    arc_len = radius * math.radians(arc_deg)
    speed = arc_len / t
    print("abaniko tip speed: %.2f m/s" % speed)
    assert 3.13 < speed < 3.15
    # back-and-forth: strikes per second at this pace
    sps = 1.0 / t
    print("fan rate: %.0f direction changes per second" % sps)
    assert 9.99 < sps < 10.01
    print("rule: the wrist is the last weapon to tire")
    print("OK: %s fanned the arc" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_solo_drills(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # session math: 12 angles x 10 reps x 3 sets, 2 strikes per second
    strikes = 12 * 10 * 3
    rate = 2.0
    minutes = strikes / rate / 60.0
    print("session strikes: %d" % strikes)
    assert strikes == 360
    print("session time at 2 strikes/s: %.1f minutes" % minutes)
    assert 2.99 < minutes < 3.01
    # slow finish: 3 perfect slow strikes per angle
    slow = 12 * 3
    print("slow finish strikes: %d" % slow)
    assert slow == 36
    print("rule: ten focused minutes daily beats one sloppy hour weekly")
    print("OK: %s shadowed honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_sinawali(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six-count weave: alternating hands and heights
    pattern = [("R", 1), ("L", 2), ("R", 3), ("L", 3), ("R", 2), ("L", 1)]
    assert len(pattern) == 6
    rights = sum(1 for h, _ in pattern if h == "R")
    lefts = sum(1 for h, _ in pattern if h == "L")
    print("six-count: %d right-hand + %d left-hand strikes" % (rights, lefts))
    assert rights == 3 and lefts == 3
    cycles = 60
    total = cycles * len(pattern)
    print("%d cycles = %d strikes, both hands equal" % (cycles, total))
    assert total == 360
    print("rule: sticks strike the partner's stick, never the partner")
    print("OK: %s wove the pattern" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_heaven_six(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # heaven six at tempo: 120 bpm, one strike per beat, six-count cycles
    bpm = 120.0
    per_beat = 1.0
    strikes_per_min = bpm * per_beat
    cycles_per_min = strikes_per_min / 6.0
    print("strikes per minute: %.0f" % strikes_per_min)
    assert 119.99 < strikes_per_min < 120.01
    print("six-count cycles per minute: %.1f" % cycles_per_min)
    assert 19.99 < cycles_per_min < 20.01
    print("rule: relaxed shoulders, steady breath")
    print("OK: %s kept the roof" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_redonda(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # circular strike: one revolution per 0.5 s, radius 0.71 m
    period = 0.5
    omega = 2 * math.pi / period
    print("redonda angular velocity: %.2f rad/s" % omega)
    assert 12.56 < omega < 12.57
    r = 0.71
    centripetal = omega ** 2 * r
    print("tip centripetal acceleration: %.1f m/s^2" % centripetal)
    assert 111.9 < centripetal < 112.3
    print("rule: tight and fast beats wide and slow")
    print("OK: %s turned the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_hubud(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hubud cycle: feed, parry, tie, untie - 4 beats at 1.5 s per cycle
    beats = 4
    cycle_s = 1.5
    session_min = 10.0
    cycles = session_min * 60.0 / cycle_s
    reps = cycles * beats
    print("hubud cycles in 10 minutes: %.0f" % cycles)
    assert 399.99 < cycles < 400.01
    print("technique beats practiced: %.0f" % reps)
    assert 1599.99 < reps < 1600.01
    print("rule: practice soft - rushing builds arm-wrestling, not sensitivity")
    print("OK: %s tied and untied" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_sombrada(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # counter-for-counter chain: 4 exchanges, 2 choices each -> 16 paths
    exchanges = 4
    choices = 2
    paths = choices ** exchanges
    print("four-exchange chain paths: %d" % paths)
    assert paths == 16
    # decision window: perceive, block, counter under 0.5 s
    window = 0.5
    chains_per_session = 200.0
    print("decision window: %.1f s, chains per session: %.0f" % (window, chains_per_session))
    assert 0.49 < window < 0.51
    print("rule: counters stop at the touch")
    print("OK: %s answered every answer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_tapi_tapi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tap window: strike takes 0.25 s; tap must land between 0.10 and 0.20 s
    flight = 0.25
    win_open = 0.10
    win_close = 0.20
    window = win_close - win_open
    print("tap window: %.2f s of %.2f s flight" % (window, flight))
    assert 0.099 < window < 0.101
    # at 60 fps, the window is this many frames
    frames = window * 60.0
    print("window at 60 fps: %.0f frames" % frames)
    assert 5.99 < frames < 6.01
    print("rule: tap-strike is one beat, not two")
    print("OK: %s tapped the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_espada_y_daga(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two weapons x twelve angles = 144 combined attack lines
    angles = 12
    combos = angles * angles
    print("espada y daga attack combinations: %d" % combos)
    assert combos == 144
    # coordination rule: weapons never do the same job at the same time
    jobs = {"stick": "long range", "dagger": "close range"}
    assert len(jobs) == 2
    print("stick: %s, dagger: %s" % (jobs["stick"], jobs["dagger"]))
    print("rule: the weapons never do the same job at the same time")
    print("OK: %s paired the weapons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_footwork_iii(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sidestep: 0.5 m lateral over 1.0 m of forward distance
    lateral = 0.5
    forward = 1.0
    evade_deg = math.degrees(math.atan(lateral / forward))
    print("evasion angle: %.2f degrees" % evade_deg)
    assert 26.56 < evade_deg < 26.58
    # dead side: stepping outside the weapon shoulder (~0.45 m) at 1 m range
    dead_deg = math.degrees(math.atan(0.45 / 1.0))
    print("dead-side angle at 1 m: %.2f degrees" % dead_deg)
    assert 24.22 < dead_deg < 24.24
    print("rule: step to the dead side")
    print("OK: %s owned the angle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_panantukan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # translation: 12 stick angles become 12 empty-hand strikes
    angles = 12
    print("translated strikes: %d" % angles)
    assert angles == 12
    # hand vs stick: same wrist omega, hand radius 0.6 m vs stick tip 1.4 m
    omega = 15.0
    v_hand = omega * 0.6
    v_tip = omega * 1.4
    ratio = v_tip / v_hand
    print("hand speed %.1f m/s vs stick tip %.1f m/s, ratio %.2f" % (v_hand, v_tip, ratio))
    assert 2.32 < ratio < 2.34
    print("rule: every combination must trace back to an angle")
    print("OK: %s translated the weapon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_gunting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scissor wedge: 20-degree wedge -> mechanical advantage 1/tan(10 deg)
    wedge_deg = 20.0
    advantage = 1.0 / math.tan(math.radians(wedge_deg / 2.0))
    print("gunting wedge mechanical advantage: %.2f to one" % advantage)
    assert 5.66 < advantage < 5.68
    # 40 N of arm pressure becomes clamping force
    arm_n = 40.0
    clamp_n = arm_n * advantage
    print("40 N of pressure clamps at %.1f N" % clamp_n)
    assert 226.5 < clamp_n < 227.5
    print("rule: drill it as pressure, never as a jerk")
    print("OK: %s closed the scissors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_daga_i(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three grips, twelve angles each
    grips = ["hammer", "pakal (icepick)", "fencer"]
    angles = 12
    print("grips: %d" % len(grips))
    assert len(grips) == 3
    combos = len(grips) * angles
    print("grip-angle combinations: %d" % combos)
    assert combos == 36
    # arc length for a 1.2 rad wrist cut with a 0.25 m blade
    blade_m = 0.25
    arc = blade_m * 1.2
    print("blade arc for 1.2 rad wrist cut: %.2f m" % arc)
    assert 0.299 < arc < 0.301
    print("rule: deflect the weapon arm, never catch the edge")
    print("OK: %s honored the edge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_agaw_i(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # snaking leverage: 0.6 m lever vs 0.05 m wrist radius
    lever = 0.6
    wrist_r = 0.05
    advantage = lever / wrist_r
    print("snaking leverage: %.0f to one" % advantage)
    assert 11.99 < advantage < 12.01
    # opponent grips at 200 N; the snake needs only this much
    grip_n = 200.0
    need_n = grip_n / advantage
    print("200 N grip defeated by %.2f N of snake" % need_n)
    assert 16.65 < need_n < 16.68
    print("rule: a disarm is an opportunity, never a wrestling match")
    print("OK: %s snaked the weapon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_agaw_ii(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # punyo strike: short lever 0.15 m at 15 rad/s
    omega = 15.0
    lever = 0.15
    v = omega * lever
    mass = 0.35
    ke = 0.5 * mass * v ** 2
    print("punyo strike speed: %.2f m/s, energy: %.3f J" % (v, ke))
    assert 2.249 < v < 2.251
    assert 0.885 < ke < 0.888
    # then the strip: grab near the tip, twist toward the thumb side
    print("rule: punyo first, strip second")
    print("OK: %s loosened and took" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_daga_ii(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # thrust crosses arm's length (0.71 m) in 0.2 s
    dist = 0.71
    t = 0.2
    speed = dist / t
    print("knife thrust speed: %.2f m/s" % speed)
    assert 3.54 < speed < 3.56
    # human reaction 0.25 s: distance covered before you can react
    reaction = 0.25
    covered = speed * reaction
    print("distance covered in one reaction time: %.3f m" % covered)
    assert 0.886 < covered < 0.889
    print("rule: the defense must be pre-positioned, not launched on sight")
    print("OK: %s respected the blade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_cadena(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five core moves chain into ordered three-move sequences
    moves = 5
    chains = moves * (moves - 1) * (moves - 2)
    print("ordered three-move chains from five core moves: %d" % chains)
    assert chains == 60
    # continuous minute test: 3-move chains at 2 s each
    minute_chains = 60.0 / 2.0
    print("chains in the continuous minute: %.0f" % minute_chains)
    assert 29.99 < minute_chains < 30.01
    print("rule: every motion ends in the next motion's chamber")
    print("OK: %s chained the hands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_dumog(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hip throw: lift 75 kg opponent's center 0.3 m
    m = 75.0
    g = 9.81
    h = 0.3
    work = m * g * h
    print("hip throw work: %.1f J" % work)
    assert 220.6 < work < 220.9
    # the hips do the lifting: thrower's effort is a fraction via leverage
    print("rule: control the head, control the spine")
    print("OK: %s threw with the hips" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_live_hand(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # check timing: hand intercepts across 0.3 m in 0.1 s
    dist = 0.3
    t = 0.1
    speed = dist / t
    print("live-hand check speed: %.1f m/s" % speed)
    assert 2.99 < speed < 3.01
    # the check buys the beat: opponent strike flight 0.25 s
    flight = 0.25
    beats = flight / t
    print("one check buys %.1f beats of the strike flight" % beats)
    assert 2.49 < beats < 2.51
    print("rule: check the weapon arm, not the weapon")
    print("OK: %s woke the live hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_espada_y_daga_ii(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two weapons x three ranges = six range-weapon cells
    cells = 2 * 3
    print("range-weapon cells: %d" % cells)
    assert cells == 6
    # passing circuit: dagger receives, stick traps, dagger finishes
    circuit = ["dagger receives", "stick traps", "dagger finishes"]
    assert len(circuit) == 3
    # high-low clearing: guard covers one line strongly; two lines threatened
    lines = 2
    covered = 1
    print("lines threatened: %d, lines strongly covered: %d" % (lines, covered))
    assert lines - covered == 1
    print("rule: keep the dagger hand relaxed")
    print("OK: %s passed and cleared" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_laban_laro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # round structure: 3 x 2 min rounds + 2 x 1 min rests
    rounds = 3
    round_min = 2.0
    rests = 2
    rest_min = 1.0
    total = rounds * round_min + rests * rest_min
    print("sparring session: %.0f minutes" % total)
    assert 7.99 < total < 8.01
    # 30 strikes per minute per round
    per_round = 30.0 * round_min
    total_strikes = per_round * rounds
    print("strikes thrown: %.0f" % total_strikes)
    assert 179.99 < total_strikes < 180.01
    print("rule: one correction between rounds")
    print("OK: %s played the fight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_free_flow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three ranges, six transitions (each pair both directions)
    ranges = ["largo", "medio", "corto"]
    transitions = len(ranges) * (len(ranges) - 1)
    print("range transitions: %d" % transitions)
    assert transitions == 6
    # called-range game: new range every 10 s in a 2-minute round
    calls = 120.0 / 10.0
    print("range calls per round: %.0f" % calls)
    assert 11.99 < calls < 12.01
    print("rule: range is a decision, not an accident")
    print("OK: %s switched everything" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_multiple(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stacking: two attackers 3 m apart; narrow their angle under 20 degrees
    sep = 3.0
    max_deg = 20.0
    need_dist = sep / (2.0 * math.tan(math.radians(max_deg / 2.0)))
    print("distance needed to stack under 20 degrees: %.2f m" % need_dist)
    assert 8.50 < need_dist < 8.53
    # drill finish: defender ten meters away
    exit_m = 10.0
    print("drill exit distance: %.0f m" % exit_m)
    assert 9.99 < exit_m < 10.01
    print("rule: the win is the exit")
    print("OK: %s moved the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_eka_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # foundation math: 34 techniques x 1000 honest repetitions
    techniques = 34
    reps_each = 1000
    total = techniques * reps_each
    print("foundation repetitions: %d" % total)
    assert total == 34000
    # at 200 reps per day
    per_day = 200
    days = total / per_day
    print("days at 200 reps/day: %.0f" % days)
    assert 169.99 < days < 170.01
    print("rule: the practice never ends")
    print("OK: %s kept the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    'what_is': demo_eka_what_is,
    'the_stick': demo_eka_the_stick,
    'the_grip': demo_eka_the_grip,
    'stance_handa': demo_eka_stance_handa,
    'angles_1_5': demo_eka_angles_1_5,
    'angles_6_12': demo_eka_angles_6_12,
    'footwork_sulong': demo_eka_footwork_sulong,
    'labtik': demo_eka_labtik,
    'footwork_atras': demo_eka_footwork_atras,
    'defensa': demo_eka_defensa,
    'abaniko': demo_eka_abaniko,
    'solo_drills': demo_eka_solo_drills,
    'sinawali': demo_eka_sinawali,
    'heaven_six': demo_eka_heaven_six,
    'redonda': demo_eka_redonda,
    'hubud': demo_eka_hubud,
    'sombrada': demo_eka_sombrada,
    'tapi_tapi': demo_eka_tapi_tapi,
    'espada_y_daga': demo_eka_espada_y_daga,
    'footwork_iii': demo_eka_footwork_iii,
    'panantukan': demo_eka_panantukan,
    'gunting': demo_eka_gunting,
    'daga_i': demo_eka_daga_i,
    'agaw_i': demo_eka_agaw_i,
    'agaw_ii': demo_eka_agaw_ii,
    'daga_ii': demo_eka_daga_ii,
    'cadena': demo_eka_cadena,
    'dumog': demo_eka_dumog,
    'live_hand': demo_eka_live_hand,
    'espada_y_daga_ii': demo_eka_espada_y_daga_ii,
    'laban_laro': demo_eka_laban_laro,
    'free_flow': demo_eka_free_flow,
    'multiple': demo_eka_multiple,
    'mastery': demo_eka_mastery,
}
