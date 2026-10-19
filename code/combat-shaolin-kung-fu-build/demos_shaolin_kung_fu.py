#!/usr/bin/env python3
"""Demo programs for the Shaolin Kung Fu Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: stance geometry, strike physics,
drill timing, conditioning ladders. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Entry text numbers are
cross-checked against these demo outputs.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_skf_salute(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the salute in five phases, three rounds at open and close
    phases = [("raise hands", 0.4), ("hold", 0.4), ("bow", 0.7),
              ("hold bow", 0.6), ("rise", 0.4)]
    one = sum(t for _, t in phases)
    total = one * 3
    for label, t in phases:
        print("  %-12s %4.1f s" % (label, t))
    print("one salute: %.1f s" % one)
    print("three salutes: %.1f s" % total)
    assert 2.49 < one < 2.51
    assert 7.49 < total < 7.51
    print("rule: the hands meet in exactly the same place every time")
    print("OK: %s saluted with precision" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_wuji(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # breath cadence: in 4, pause 2, out 6 -> 12 s cycle
    cycle = 4 + 2 + 6
    minutes = 6
    cycles = minutes * 60 // cycle
    tidal_l = 0.5
    volume = cycles * tidal_l
    print("breath cycle: %d s (4 in, 2 pause, 6 out)" % cycle)
    print("cycles in %d minutes: %d" % (minutes, cycles))
    print("air moved: %.1f L" % volume)
    assert cycle == 12
    assert cycles == 30
    assert 14.9 < volume < 15.1
    print("rule: joints stacked, skeleton carries the weight, mind on the count")
    print("OK: %s stood the zero posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_ma_bu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # horse stance geometry: 90-degree knee, thigh parallel to floor
    thigh = 0.45          # m
    knee_deg = 90
    hip_h = thigh * math.sin(math.radians(knee_deg))
    shoulder_w = 0.45     # m
    base = 2 * shoulder_w
    stability = base / hip_h
    print("thigh %.2f m, knee %d deg -> hip height %.3f m" % (thigh, knee_deg, hip_h))
    print("base width %.2f m, stability ratio %.2f" % (base, stability))
    assert 0.449 < hip_h < 0.451
    assert 0.899 < base < 0.901
    assert 1.99 < stability < 2.01
    # hold ladder: 30 s + 15 s/week
    holds = [30 + 15 * w for w in range(8)]
    print("hold ladder (8 weeks): %s s" % holds)
    assert holds[-1] == 135
    print("rule: thighs parallel, knees over toes, back straight")
    print("OK: %s rooted the horse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_gong_bu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bow stance weight split: 70/30 of 70 kg
    mass = 70.0
    front = mass * 0.70
    back = mass * 0.30
    g = 9.81
    print("front leg: %.0f kg -> %.1f N" % (front, front * g))
    print("back leg:  %.0f kg -> %.1f N" % (back, back * g))
    assert 480.6 < front * g < 480.8
    assert 205.9 < back * g < 206.2
    assert abs((front + back) - mass) < 1e-9
    print("rule: back heel down, knee over ankle, drive from the floor")
    print("OK: %s drew the bow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_xu_bu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # empty stance weight split: 90/10 of 70 kg
    mass = 70.0
    back = mass * 0.90
    front = mass * 0.10
    g = 9.81
    print("back leg: %.0f kg -> %.2f N" % (back, back * g))
    print("front foot: %.0f kg -> %.2f N" % (front, front * g))
    assert 618.02 < back * g < 618.05
    assert 68.66 < front * g < 68.69
    # readiness: the front foot must lift with zero sway
    print("readiness test: front knee lifts with no torso sway")
    print("rule: the empty leg is a kick waiting to happen")
    print("OK: %s coiled the cat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_pu_bu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crouch stance drops the center of mass
    com_stand = 1.00
    com_pu = 0.45
    drop = com_stand - com_pu
    pct = drop / com_stand * 100.0
    print("center of mass: %.2f m standing -> %.2f m in pu bu" % (com_stand, com_pu))
    print("descent: %.2f m (%.0f %%)" % (drop, pct))
    assert 0.549 < drop < 0.551
    assert 54.9 < pct < 55.1
    print("rule: sink low, torso upright, folded knee over its toes")
    print("OK: %s loaded the spring" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_xie_bu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross stance footprint vs horse stance footprint
    xie_w, depth = 0.30, 0.40
    ma_w = 0.90
    xie_area = xie_w * depth
    ma_area = ma_w * depth
    print("xie bu footprint: %.2f x %.2f m = %.3f m^2" % (xie_w, depth, xie_area))
    print("ma bu footprint:  %.2f x %.2f m = %.3f m^2" % (ma_w, depth, ma_area))
    print("compactness ratio: %.3f" % (xie_area / ma_area))
    assert 0.119 < xie_area < 0.121
    assert 0.359 < ma_area < 0.361
    assert 0.332 < xie_area / ma_area < 0.335
    print("rule: knees follow their own toes, even crossed")
    print("OK: %s wound the screw" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_duli_bu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight-week balance ladder: doubles every two weeks, daily practice
    ladder = [(1, 10), (3, 20), (5, 40), (7, 80)]
    total_per_leg = 0
    for start_wk, secs in ladder:
        block = 14 * secs
        total_per_leg += block
        print("weeks %d-%d: %d s/day x 14 days = %d s" % (start_wk, start_wk + 1, secs, block))
    print("total hold time per leg over 8 weeks: %d s (%.1f min)" % (total_per_leg, total_per_leg / 60))
    assert total_per_leg == 2100
    assert abs(total_per_leg / 60 - 35.0) < 0.01
    print("rule: ankle adjusts, torso stays tall, no toe-gripping")
    print("OK: %s stood the crane leg" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_chong_quan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # punch kinetic energy: effective mass 4 kg at 8 m/s
    m, v = 4.0, 8.0
    ke = 0.5 * m * v ** 2
    print("fist speed %.0f m/s, effective mass %.0f kg" % (v, m))
    print("kinetic energy: %.1f J" % ke)
    assert 127.9 < ke < 128.1
    # rotation: 180 degrees over the extension
    print("fist rotation in flight: 180 degrees, palm-up to palm-down")
    print("rule: hip turns first, fist delivers last, snap back twice as fast")
    print("OK: %s threw the straight line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_tui_zhang(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same force, different tools: palm vs fist pressure
    f = 1500.0
    palm_area, fist_area = 0.012, 0.004  # m^2
    p_palm = f / palm_area
    p_fist = f / fist_area
    print("force: %.0f N" % f)
    print("palm (%.0f cm^2): %.0f Pa" % (palm_area * 1e4, p_palm))
    print("fist (%.0f cm^2): %.0f Pa" % (fist_area * 1e4, p_fist))
    assert 124999 < p_palm < 125001
    assert 374999 < p_fist < 375001
    assert 2.99 < p_fist / p_palm < 3.01
    print("rule: palm pushes the mass, fist penetrates it")
    print("OK: %s pushed the door" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_shang_jia(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 45-degree deflection splits an 800 N downward strike
    f = 800.0
    ang = math.radians(45)
    along = f * math.cos(ang)   # slides off along the forearm
    into = f * math.sin(ang)    # presses into the block
    print("incoming: %.0f N straight down" % f)
    print("deflected along forearm: %.1f N" % along)
    print("absorbed by block:       %.1f N" % into)
    assert 565.6 < along < 565.8
    assert 565.6 < into < 565.8
    print("rule: never meet force head-on; the angle does the work")
    print("OK: %s raised the roof" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_deng_tui(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front snap kick energy: 12 kg leg at 9 m/s
    m, v = 12.0, 9.0
    ke = 0.5 * m * v ** 2
    print("leg mass %.0f kg, foot speed %.0f m/s" % (m, v))
    print("kick energy: %.0f J" % ke)
    assert 485.9 < ke < 486.1
    # chamber check: thigh must reach parallel before extension
    print("chamber: thigh parallel, then heel-first snap")
    print("rule: no chamber, no snap - a low knee makes a push")
    print("OK: %s stamped the pedal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_ce_chuai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # side kick reach: 0.92 m leg, training target at 80% of reach
    leg = 0.92
    target = 0.80 * leg
    print("full extension reach: %.2f m" % leg)
    print("training target (80%%): %.3f m" % target)
    assert 0.735 < target < 0.737
    # pivot check: support heel must point at the target
    print("pivot: support heel to target opens the hip")
    print("rule: no pivot, no hip, no power")
    print("OK: %s thrust sideways" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_huan_bu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # footwork cadence ladder: 60 / 90 / 120 steps per minute, 0.6 m steps
    step = 0.6
    minutes = 3
    for cadence in (60, 90, 120):
        dist = cadence * step * minutes
        print("%d steps/min x %.1f m x %d min = %.0f m" % (cadence, step, minutes, dist))
    d90 = 90 * step * minutes
    assert 161.9 < d90 < 162.1
    assert abs(60 * step * minutes - 108.0) < 0.01
    assert abs(120 * step * minutes - 216.0) < 0.01
    print("rule: head level like a bowl of water, hands never drop")
    print("OK: %s wrote the cursive" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_wu_bu_quan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Five Stance Fist: 40 movements at three tempos
    moves = 40
    for label, tempo in (("beginner", 1.5), ("crisp", 1.0), ("sharp", 0.75)):
        total = moves * tempo
        print("%-8s %d moves x %.2f s = %.0f s" % (label, moves, tempo, total))
    assert abs(moves * 1.5 - 60.0) < 0.01
    assert abs(moves * 1.0 - 40.0) < 0.01
    assert abs(moves * 0.75 - 30.0) < 0.01
    print("rule: stances stay deep at every tempo")
    print("OK: %s wrote the first form" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_tan_tui(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twelve roads: height ladder +5 cm per road from 90 cm
    base, step = 0.90, 0.05
    heights = [base + step * i for i in range(12)]
    print("road  1 target: %.2f m" % heights[0])
    print("road  6 target: %.2f m" % heights[5])
    print("road 12 target: %.2f m" % heights[11])
    assert 0.899 < heights[0] < 0.901
    assert 1.149 < heights[5] < 1.151
    assert 1.449 < heights[11] < 1.451
    full = 12 * 20
    print("full twelve roads at 20 s each: %d s (%d min)" % (full, full // 60))
    assert full == 240
    print("rule: chamber, snap, re-chamber - never swing")
    print("OK: %s wound the twelve springs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_hu_zhao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tiger claw rake: 0.19 m hand sweeping 120 degrees
    r = 0.19
    theta = math.radians(120)
    arc = r * theta
    print("claw reach %.2f m, rake arc 120 deg" % r)
    print("raking path: %.3f m" % arc)
    assert 0.397 < arc < 0.399
    # conditioning set
    per_hand, hands = 20, 2
    print("rice-bag set: %d per hand x %d hands = %d rakes" % (per_hand, hands, per_hand * hands))
    assert per_hand * hands == 40
    print("rule: hooked talons from a deep horse, hip drives the rake")
    print("OK: %s filed the first seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_she_quan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # snake dart: 0.60 m extension in 0.12 s
    dist, t = 0.60, 0.12
    v = dist / t
    print("dart distance %.2f m in %.2f s" % (dist, t))
    print("fingertip speed: %.1f m/s" % v)
    assert 4.99 < v < 5.01
    # conditioning: sand pressing sets
    daily = 50
    print("daily sand pressing: %d presses" % daily)
    print("rule: the snake never leaves its head out - snap back instantly")
    print("OK: %s filed the second seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_he_zui(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crane beak pressure: 400 N through 2 cm^2
    f = 400.0
    area = 2e-4  # m^2
    p = f / area
    print("peck force %.0f N, beak tip %.0f cm^2" % (f, area * 1e4))
    print("pressure: %.0f Pa (%.1f MPa)" % (p, p / 1e6))
    assert 1999999 < p < 2000001
    # formation drilling
    print("daily beak formations: 100, then 20 pecks per hand")
    print("rule: tight beak, locked wrist, tall crane leg")
    print("OK: %s filed the third seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_bao_quan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # leopard ridge vs full fist at 1200 N
    f = 1200.0
    ridge, full = 3e-4, 25e-4  # m^2
    p_ridge = f / ridge
    p_full = f / full
    ratio = p_ridge / p_full
    print("leopard ridge (3 cm^2): %.0f Pa" % p_ridge)
    print("full fist (25 cm^2):   %.0f Pa" % p_full)
    print("pressure multiplier: %.2f x" % ratio)
    assert 3999999 < p_ridge < 4000001
    assert 479999 < p_full < 480001
    assert 8.32 < ratio < 8.34
    print("rule: the leopard never throws one strike alone - chains of three and four")
    print("OK: %s filed the fourth seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_long_xing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dragon waist: 180 degrees in 0.5 s drives the hand
    theta = math.pi
    t = 0.5
    omega = theta / t
    r = 0.65
    v = omega * r
    print("waist turn: 180 deg in %.1f s -> %.2f rad/s" % (t, omega))
    print("hand at %.2f m from spine: %.2f m/s from the turn alone" % (r, v))
    assert 6.28 < omega < 6.29
    assert 4.083 < v < 4.086
    print("rule: the waist turns first; the arm only delivers")
    print("OK: %s filed the fifth seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_hei_hu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # black tiger chains: 3 strikes per 0.75 s, 10 combinations
    per_combo, combos = 3, 10
    combo_t = 0.75
    strikes = per_combo * combos
    impact_t = combos * combo_t
    print("%d strikes per combo x %d combos = %d strikes" % (per_combo, combos, strikes))
    print("impact time: %.1f s" % impact_t)
    assert strikes == 30
    assert 7.49 < impact_t < 7.51
    print("metronome: 4 beats/s - strike, strike, strike, step")
    print("rule: forward pressure, no step back, no pauses inside the chain")
    print("OK: %s ran with the black tiger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_xiao_hong_quan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Small Flood Fist: 48 movements, training 1.25 s, performance 0.8 s
    moves = 48
    t_train = moves * 1.25
    t_perf = moves * 0.8
    print("sections: 4 x 12 = %d movements" % moves)
    print("training tempo:  %.0f s" % t_train)
    print("performance:     %.1f s" % t_perf)
    assert moves == 48
    assert 59.9 < t_train < 60.1
    assert 38.3 < t_perf < 38.5
    print("rule: learned one section at a time, performed as one flood")
    print("OK: %s passed the entrance exam" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_sao_tui(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep coverage: 0.90 m leg over 180 degrees
    r = 0.90
    area = math.pi * r ** 2 / 2
    print("sweep radius %.2f m, arc 180 deg" % r)
    print("floor covered: %.3f m^2" % area)
    assert 1.271 < area < 1.274
    # solo spin drilling
    per_side = 10
    print("solo spins: %d per side = %d total" % (per_side, per_side * 2))
    print("rule: ankle height, shin contact, stay low through the spin")
    print("OK: %s swept the floor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_da_hong_quan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Big Flood Fist: 96 movements at 1 s each, ~60 J per movement
    moves = 96
    tempo = 1.0
    total_t = moves * tempo
    work = moves * 60.0
    print("movements: %d at %.1f s each -> %.0f s" % (moves, tempo, total_t))
    print("estimated work: %d moves x 60 J = %.0f J" % (moves, work))
    assert 95.9 < total_t < 96.1
    assert 5759 < work < 5761
    # sections
    print("sections: 6 x 16 movements")
    print("rule: full power, full depth, full speed - no rest inside")
    print("OK: %s survived the flood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_gun_fa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # staff tip speed: 2 m staff spun at 3 rev/s, hands 1 m from tip
    rev = 3.0
    r = 1.0
    v = 2 * math.pi * rev * r
    print("staff length 2.0 m, spin %.0f rev/s" % rev)
    print("tip speed: %.2f m/s" % v)
    assert 18.84 < v < 18.86
    # basics count
    basics = ["thrust", "sweep", "overhead block", "wrapping parry", "spinning strike"]
    print("five basics: %s" % ", ".join(basics))
    assert len(basics) == 5
    print("rule: control first - a 2 m lever at 19 m/s forgives nothing")
    print("OK: %s spun the long signature" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_tong_zi_gong(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twelve-week split ladder: 120 cm + 5 cm/week
    start, step = 120, 5
    weeks = [start + step * w for w in range(1, 13)]
    print("week  1 split: %d cm" % weeks[0])
    print("week  6 split: %d cm" % weeks[5])
    print("week 12 split: %d cm" % weeks[11])
    assert weeks[0] == 125
    assert weeks[5] == 150
    assert weeks[11] == 180
    # daily session budget
    session = 10 + 15 + 5
    print("daily session: 10 warmup + 15 stretch + 5 kick = %d min" % session)
    assert session == 30
    print("rule: breathed into, never forced - torn tissue costs months")
    print("OK: %s grew the child skill" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_tie_bu_shan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight-week iron shirt ladder: 20/side + 10/week, 3 sessions/week
    sessions = 3
    total = 0
    for wk in range(1, 9):
        per_side = 20 + 10 * (wk - 1)
        wk_total = per_side * 2 * sessions
        total += wk_total
        if wk in (1, 8):
            print("week %d: %d per side/session -> %d strikes that week" % (wk, per_side, wk_total))
    print("eight-week total: %d strikes" % total)
    assert total == 2640
    # week-8 load check
    assert 20 + 10 * 7 == 90
    print("rule: exhale and harden at the instant of impact, relax between")
    print("OK: %s wore the iron cloth" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_pao_quan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cannon shot: 2000 N over 0.60 m in 0.15 s
    f, d, t = 2000.0, 0.60, 0.15
    power = f * d / t
    print("force %.0f N, distance %.2f m, time %.2f s" % (f, d, t))
    print("striking power: %.0f W" % power)
    assert 7999 < power < 8001
    # bag sets
    per_side = 10
    print("bag sets: %d per side" % per_side)
    print("rule: stillness, detonation, stillness - the pause is part of the shot")
    print("OK: %s fired the cannon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_luo_han_quan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Arhat Fist: 18 hands x 4 movements = 72
    hands, per = 18, 4
    moves = hands * per
    t_train = moves * 1.25
    t_sharp = moves * 0.8
    print("eighteen hands x %d = %d movements" % (per, moves))
    print("training tempo: %.0f s" % t_train)
    print("sharp tempo:    %.1f s" % t_sharp)
    assert moves == 72
    assert 89.9 < t_train < 90.1
    assert 57.5 < t_sharp < 57.7
    print("rule: every hand a complete technique - entry, execution, finish")
    print("OK: %s sealed the eighteen hands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_mei_hua_quan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # plum blossom poles: 1 m square, corner-to-center diagonal
    side = 1.0
    diag = math.sqrt(2) * side
    print("pole square: %.1f m sides, center pole" % side)
    print("corner-to-center diagonal: %.5f m" % diag)
    assert 1.4141 < diag < 1.4143
    poles = 5
    print("poles: %d in the blossom pattern, ~1 m high" % poles)
    assert poles == 5
    print("rule: gaze forward, every step centered - the poles punish imprecision")
    print("OK: %s walked the blossom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_tie_sha_zhang(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # iron sand palm: 3 phases x 100 days x 100 strikes
    phases = [("mung beans", 100), ("coarse sand", 100), ("iron filings", 100)]
    per_session = 100
    total = 0
    for label, days in phases:
        phase_total = days * per_session
        total += phase_total
        print("%-12s %d days x %d = %d strikes" % (label, days, per_session, phase_total))
    print("three-hundred-day total: %d strikes" % total)
    assert total == 30000
    print("rule: hand care after every session; never through pain; never unsupervised")
    print("OK: %s signed in iron" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_yi_zhi_chan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one finger: 30% of 70 kg on 1.5 cm^2
    mass, frac = 70.0, 0.30
    load_n = mass * frac * 9.81
    area = 1.5e-4  # m^2
    p = load_n / area
    print("load: %.0f kg x %.0f%% = %.1f N" % (mass, frac * 100, load_n))
    print("fingertip pressure: %.0f Pa (%.2f MPa)" % (p, p / 1e6))
    assert 206.0 < load_n < 206.1
    assert 1373300 < p < 1373500
    # finger reduction stages
    stages = [5, 4, 3, 2, 1]
    print("stages: %s fingers, 2+ painless months each" % stages)
    print("rule: the stillness is the exercise - never through pain, never unsupervised")
    print("OK: %s balanced the single point" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_skf_wu_xing_he_yi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five animals: ordered transitions and 3-chains
    n = 5
    transitions = n * (n - 1)
    chains = 1
    for k in range(3):
        chains *= (n - k)  # P(5,3)
    animals = ["dragon", "tiger", "crane", "leopard", "snake"]
    print("animals: %s" % ", ".join(animals))
    print("ordered transitions: %d x %d = %d" % (n, n - 1, transitions))
    print("possible 3-animal chains P(5,3) = %d" % chains)
    assert transitions == 20
    assert chains == 60
    print("rule: each animal fully itself while it lasts - no blending, no hesitation")
    print("OK: %s signed with all five hands" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "salute": demo_skf_salute,
    "wuji": demo_skf_wuji,
    "ma_bu": demo_skf_ma_bu,
    "gong_bu": demo_skf_gong_bu,
    "xu_bu": demo_skf_xu_bu,
    "pu_bu": demo_skf_pu_bu,
    "xie_bu": demo_skf_xie_bu,
    "duli_bu": demo_skf_duli_bu,
    "chong_quan": demo_skf_chong_quan,
    "tui_zhang": demo_skf_tui_zhang,
    "shang_jia": demo_skf_shang_jia,
    "deng_tui": demo_skf_deng_tui,
    "ce_chuai": demo_skf_ce_chuai,
    "huan_bu": demo_skf_huan_bu,
    "wu_bu_quan": demo_skf_wu_bu_quan,
    "tan_tui": demo_skf_tan_tui,
    "hu_zhao": demo_skf_hu_zhao,
    "she_quan": demo_skf_she_quan,
    "he_zui": demo_skf_he_zui,
    "bao_quan": demo_skf_bao_quan,
    "long_xing": demo_skf_long_xing,
    "hei_hu": demo_skf_hei_hu,
    "xiao_hong_quan": demo_skf_xiao_hong_quan,
    "sao_tui": demo_skf_sao_tui,
    "da_hong_quan": demo_skf_da_hong_quan,
    "gun_fa": demo_skf_gun_fa,
    "tong_zi_gong": demo_skf_tong_zi_gong,
    "tie_bu_shan": demo_skf_tie_bu_shan,
    "pao_quan": demo_skf_pao_quan,
    "luo_han_quan": demo_skf_luo_han_quan,
    "mei_hua_quan": demo_skf_mei_hua_quan,
    "tie_sha_zhang": demo_skf_tie_sha_zhang,
    "yi_zhi_chan": demo_skf_yi_zhi_chan,
    "wu_xing_he_yi": demo_skf_wu_xing_he_yi,
}
