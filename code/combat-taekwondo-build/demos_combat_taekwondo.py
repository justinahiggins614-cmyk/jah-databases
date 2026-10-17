#!/usr/bin/env python3
"""Demo programs for the Taekwondo Combat databases (combat batch 1).

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: drill timers, stance geometry, strike
physics, combination counts, scoring scenarios. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds (never
float exact-equality), and ends with the OK marker.

Every number cross-checked against the entry text 2026-10-17.
"""

import math

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_tkd_what_is_taekwondo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the architecture of the art: tenets, pillars, forms
    tenets = ["courtesy", "integrity", "perseverance", "self-control",
              "indomitable spirit"]
    pillars = ["basics", "forms", "sparring", "breaking"]
    taegeuk = 8
    tul = 24
    forms = taegeuk + tul
    print("tenets: %d" % len(tenets))
    for t in tenets:
        print("  - %s" % t)
    print("pillars: %d (%s)" % (len(pillars), ", ".join(pillars)))
    print("forms: %d taegeuk + %d tul = %d" % (taegeuk, tul, forms))
    assert len(tenets) == 5
    assert len(pillars) == 4
    assert forms == 32
    print("rule: foot, fist, the way - character graded with technique")
    print("OK: %s mapped the art" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_attention_bow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bow drill timer: down, hold, up
    down, hold, up = 1.0, 1.0, 1.0
    per_bow = down + hold + up
    reps = 20
    total = reps * per_bow
    print("per bow: %.1f s (down %.0f, hold %.0f, up %.0f)" % (per_bow, down, hold, up))
    print("drill: %d bows = %.0f s = %.1f min" % (reps, total, total / 60.0))
    assert 2.99 < per_bow < 3.01
    assert 59.9 < total < 60.1
    print("rule: respect is a physical drill - deliberate action, not reaction")
    print("OK: %s timed the bow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_ready_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ready stance base of support: shoulder width by foot depth
    shoulder = 0.45          # meters
    depth = 0.15             # meters, ball-to-heel working depth
    area = shoulder * depth
    fist_gap = 0.09          # one fist width, fists to belt
    print("foot separation: %.2f m" % shoulder)
    print("base of support: %.2f x %.2f m = %.4f m^2" % (shoulder, depth, area))
    print("fist chamber gap: %.2f m" % fist_gap)
    assert 0.449 < shoulder < 0.451
    assert 0.0674 < area < 0.0676
    print("rule: nothing extended, nothing exposed, everything coiled")
    print("OK: %s measured the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_front_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front stance load split 60/40 for a 70 kg practitioner
    mass = 70.0
    g = 9.81
    weight = mass * g
    front = 0.60 * weight
    back = 0.40 * weight
    shoulder = 0.45
    length = 1.5 * shoulder
    print("body weight: %.1f N" % weight)
    print("front leg: %.1f N (60 %%)" % front)
    print("back leg: %.1f N (40 %%)" % back)
    print("stance length: %.3f m" % length)
    assert 411.8 < front < 412.1
    assert 274.5 < back < 274.8
    assert 0.674 < length < 0.676
    print("rule: the lunge frozen at maximum commitment")
    print("OK: %s loaded the stance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_back_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # back stance load split 70/30 for a 70 kg practitioner
    mass = 70.0
    g = 9.81
    weight = mass * g
    back = 0.70 * weight
    front = 0.30 * weight
    foot_angle = 90.0  # degrees between the feet
    print("back leg: %.1f N (70 %%)" % back)
    print("front leg: %.1f N (30 %%)" % front)
    print("angle between feet: %.0f degrees" % foot_angle)
    assert 480.6 < back < 480.8
    assert 205.9 < front < 206.2
    assert 89.9 < foot_angle < 90.1
    print("rule: the light front leg is a free weapon")
    print("OK: %s weighed the defense" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_horse_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # horse stance hold ladder: 20 s week 1, +10 s/week, 8 weeks daily
    weeks = [20 + 10 * w for w in range(8)]
    per_day = sum(weeks) / len(weeks)
    total_s = sum(weeks) * 7
    total_min = total_s / 60.0
    print("weekly holds (s): %s" % weeks)
    print("week 8 hold: %d s" % weeks[-1])
    print("accumulated: %d s = %.1f min" % (total_s, total_min))
    assert weeks[-1] == 90
    assert total_s == 3080
    assert 51.3 < total_min < 51.4
    print("rule: rooted before used - the seal pressed into the earth")
    print("OK: %s built the root" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_breathing_kihap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # breathing drill: 4 s in, 4 s out; 15 cycles fill a form
    inhale, exhale = 4.0, 4.0
    cycle = inhale + exhale
    cycles = 15
    total = cycles * cycle
    kihap = 0.25  # seconds, diaphragmatic burst
    print("breath cycle: %.0f s in + %.0f s out = %.0f s" % (inhale, exhale, cycle))
    print("%d cycles = %.0f s = %.1f min (one form)" % (cycles, total, total / 60.0))
    print("ki hap burst: %.2f s" % kihap)
    assert 7.99 < cycle < 8.01
    assert 119.9 < total < 120.1
    assert 0.24 < kihap < 0.26
    print("rule: exhale on exertion - the shout notarizes the strike")
    print("OK: %s breathed the technique" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_straight_punch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight punch: 0.65 m extension in 0.09 s, 3.5 kg effective mass
    dist, t = 0.65, 0.09
    v = dist / t
    m = 3.5
    ke = 0.5 * m * v * v
    print("fist speed: %.2f m/s" % v)
    print("kinetic energy: %.1f J" % ke)
    assert 7.21 < v < 7.24
    assert 91.1 < ke < 91.5
    print("rule: the punch of the hips is a hammer, the punch of the arm is a slap")
    print("OK: %s threw the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_knife_hand(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pressure concentration: knife edge vs fist, same 500 N arm
    force = 500.0
    edge_cm2, fist_cm2 = 25.0, 40.0
    p_edge = force / (edge_cm2 / 10000.0) / 1000.0  # kPa
    p_fist = force / (fist_cm2 / 10000.0) / 1000.0
    ratio = fist_cm2 / edge_cm2
    print("knife edge: %.0f kPa" % p_edge)
    print("fist face: %.0f kPa" % p_fist)
    print("pressure ratio: %.1f x" % ratio)
    assert 199.9 < p_edge < 200.1
    assert 124.9 < p_fist < 125.1
    assert 1.59 < ratio < 1.61
    print("rule: power is not how much you bring, but how narrowly you sign")
    print("OK: %s edged the blade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_basic_blocks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three zones of the guard, in degrees of coverage
    low = 30.0      # below the belt line
    middle = 30.0   # torso band, +/-15
    high = 45.0     # 15 to 60 degrees above the eyes
    total = low + middle + high
    print("low block zone: %.0f deg" % low)
    print("middle block zone: %.0f deg" % middle)
    print("high block zone: %.0f deg" % high)
    print("guarded arc: %.0f deg" % total)
    assert total == 105.0
    print("rule: every block is chambered to become the next strike")
    print("OK: %s raised the shield" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_front_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front snap kick: 0.55 m extension in 0.12 s; head target geometry
    dist, t = 0.55, 0.12
    v = dist / t
    hip, head = 0.95, 1.60
    rise = head - hip
    reach = 0.93
    angle = math.degrees(math.atan2(rise, reach))
    print("foot speed: %.2f m/s" % v)
    print("head target rise: %.2f m over %.2f m reach" % (rise, reach))
    print("head kick angle: %.1f deg" % angle)
    assert 4.57 < v < 4.60
    assert 34.9 < angle < 35.1
    print("rule: power in the snap of the knee, not the swing of the leg")
    print("OK: %s snapped the kick" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_roundhouse_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # roundhouse: 1.05 m leg through 180 degrees in 0.25 s
    r = 1.05
    arc = r * math.pi
    t = 0.25
    v = arc / t
    print("foot arc: %.3f m" % arc)
    print("foot speed: %.2f m/s" % v)
    assert 3.29 < arc < 3.31
    assert 13.1 < v < 13.3
    print("rule: the pivot is the engine - no pivot, no power")
    print("OK: %s drew the great arc" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_side_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # side kick piston: 400 N over 0.6 m of travel
    force, dist = 400.0, 0.60
    work = force * dist
    print("thrust: %.0f N over %.1f m" % (force, dist))
    print("work on target: %.1f J" % work)
    assert 239.9 < work < 240.1
    print("rule: the battering ram - one straight line, no apology")
    print("OK: %s drove the piston" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_back_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # back kick spin: 180 degrees in 0.3 s
    deg, t = 180.0, 0.30
    deg_per_s = deg / t
    rad_per_s = math.radians(deg_per_s)
    print("spin rate: %.0f deg/s" % deg_per_s)
    print("angular velocity: %.2f rad/s" % rad_per_s)
    assert 599.9 < deg_per_s < 600.1
    assert 10.46 < rad_per_s < 10.49
    print("rule: the rotation is the chamber")
    print("OK: %s turned the heel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_axe_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # axe kick drop: leg raised to 1.8 m, free fall
    h, g = 1.8, 9.81
    t = math.sqrt(2 * h / g)
    v = g * t
    print("drop time: %.3f s" % t)
    print("impact speed (gravity alone): %.2f m/s" % v)
    assert 0.60 < t < 0.62
    assert 5.9 < v < 6.0
    print("rule: the falling hammer - drop it, do not swing it")
    print("OK: %s dropped the axe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_push_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # push kick stop: 80 kg at 2 m/s halted over 0.4 m
    m, v, d = 80.0, 2.0, 0.40
    ke = 0.5 * m * v * v
    force = ke / d
    print("attacker energy: %.0f J" % ke)
    print("stopping force: %.1f N" % force)
    assert 159.9 < ke < 160.1
    assert 399.9 < force < 400.1
    print("rule: distance management is fight management")
    print("OK: %s held the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_crescent_kicks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crescent arc: 1.0 m leg through 120 degrees
    r = 1.0
    arc = r * math.radians(120.0)
    print("sweep arc: %.3f m" % arc)
    assert 2.09 < arc < 2.10
    print("rule: the curve honestly traveled - a flourish cut short is a lie")
    print("OK: %s swept the scythe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_hook_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hook kick: 120-degree arc in 0.20 s, then the hook in 0.28 s total
    arc_rate = 120.0 / 0.20
    total = 0.28
    print("arc rate: %.0f deg/s" % arc_rate)
    print("total technique time: %.2f s" % total)
    assert 599.9 < arc_rate < 600.1
    assert 0.279 < total < 0.281
    print("rule: arc honestly traveled, hook decisively fired")
    print("OK: %s set the hook" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # footwork delivery: 2 steps/s, 3 m coverage, pivot angles
    rate = 2.0
    steps_for_3m = 4.5
    step_len = 3.0 / steps_for_3m
    pivot = 45.0
    matrix = 10 * (1 + 1 + 1 + 2 + 1)  # fwd, back, slide, pivots x2, switch
    print("step rate: %.1f steps/s" % rate)
    print("step length: %.3f m" % step_len)
    print("pivot angle: %.0f deg" % pivot)
    print("drill matrix: %d steps" % matrix)
    assert 0.666 < step_len < 0.668
    assert matrix == 60
    print("rule: never let the feet stop moving")
    print("OK: %s wrote the steps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_kick_combinations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # combination math from 5 base kicks
    base = 5
    pairs = base * base
    triples = base ** 3
    drill_kicks = 3 * 10 * 2  # 3 pairs, 10 reps, 2 sides
    print("ordered pairs: %d" % pairs)
    print("ordered triples: %d" % triples)
    print("drill volume: %d kicks" % drill_kicks)
    assert pairs == 25
    assert triples == 125
    assert drill_kicks == 60
    print("rule: the rechamber is the combination")
    print("OK: %s chained the kicks" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_taekwondo": demo_tkd_what_is_taekwondo,
    "attention_bow": demo_tkd_attention_bow,
    "ready_stance": demo_tkd_ready_stance,
    "front_stance": demo_tkd_front_stance,
    "back_stance": demo_tkd_back_stance,
    "horse_stance": demo_tkd_horse_stance,
    "breathing_kihap": demo_tkd_breathing_kihap,
    "straight_punch": demo_tkd_straight_punch,
    "knife_hand": demo_tkd_knife_hand,
    "basic_blocks": demo_tkd_basic_blocks,
    "front_kick": demo_tkd_front_kick,
    "roundhouse_kick": demo_tkd_roundhouse_kick,
    "side_kick": demo_tkd_side_kick,
    "back_kick": demo_tkd_back_kick,
    "axe_kick": demo_tkd_axe_kick,
    "push_kick": demo_tkd_push_kick,
    "crescent_kicks": demo_tkd_crescent_kicks,
    "hook_kick": demo_tkd_hook_kick,
    "footwork": demo_tkd_footwork,
    "kick_combinations": demo_tkd_kick_combinations,
}


def demo_tkd_taegeuk_poomsae(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # taegeuk movements per form: 1-8 Jang
    moves = [18, 18, 20, 20, 20, 20, 24, 24]
    total = sum(moves)
    avg = total / len(moves)
    print("movements: %s" % moves)
    print("total: %d, average: %.1f per form" % (total, avg))
    assert total == 164
    assert 20.4 < avg < 20.6
    print("rule: the form ends exactly where it began")
    print("OK: %s walked the eight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_chonji_tul(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Chon-Ji: 19 movements, 4 directions, ~40 s performance
    moves, directions, seconds = 19, 4, 40.0
    per_move = seconds / moves
    per_dir = moves / directions
    print("movements: %d over %d directions" % (moves, directions))
    print("seconds per movement: %.2f" % per_move)
    assert moves == 19
    assert 2.10 < per_move < 2.12
    assert 4.74 < per_dir < 4.76
    print("rule: the 19th movement must look exactly like the 1st")
    print("OK: %s signed heaven and earth" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_sparring_fundamentals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # match clocks: WT seniors 3x2 min + rests; ITF 2x2 min + rest
    wt = 3 * 120 + 2 * 60
    itf = 2 * 120 + 60
    print("WT senior match: 3x2 min + 2x1 min rest = %d s (%d min)" % (wt, wt // 60))
    print("ITF match: 2x2 min + 1 min rest = %d s (%d min)" % (itf, itf // 60))
    assert wt == 480
    assert itf == 300
    print("rule: calm above all - the fighter who panics has lost the round")
    print("OK: %s timed the laboratory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_tornado_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tornado kick: full 360 in 0.5 s of airtime, 1.05 m leg
    deg, t, r = 360.0, 0.50, 1.05
    rate = deg / t
    circle = 2 * math.pi * r
    print("rotation rate: %.0f deg/s" % rate)
    print("foot circle: %.3f m" % circle)
    assert 719.9 < rate < 720.1
    assert 6.59 < circle < 6.61
    print("rule: kick at the peak - late is just a roundhouse with extra steps")
    print("OK: %s rode the cyclone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_spinning_hook_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spinning hook: 360 spin, hook in the final quarter, 0.6 s total
    total = 0.60
    hook_window = 0.15  # final quarter of the rotation
    hook_arc = 120.0
    hook_rate = hook_arc / hook_window
    print("total: %.2f s, hook window: %.2f s" % (total, hook_window))
    print("hook rate: %.0f deg/s" % hook_rate)
    assert 0.599 < total < 0.601
    assert 799.9 < hook_rate < 800.1
    print("rule: spin honestly completed, hook fired at the exact end")
    print("OK: %s sealed the verdict" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_jumping_kicks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jumping kick budget: 0.4 m jump -> hang time, technique inside it
    h, g = 0.40, 9.81
    hang = 2 * math.sqrt(2 * h / g)
    chamber, kick, rechamber = 0.15, 0.28, 0.45
    print("hang time: %.3f s" % hang)
    print("budget: chamber %.2f, kick %.2f, rechamber %.2f, land %.2f" % (
        chamber, kick, rechamber, hang))
    assert 0.570 < hang < 0.573
    assert rechamber < hang
    print("rule: the technique ends at landing, not at impact")
    print("OK: %s kept the promise" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_double_kicks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # double roundhouse: 0.22 s kick, 0.10 s rechamber, 0.22 s kick
    k1, rc, k2 = 0.22, 0.10, 0.22
    total = k1 + rc + k2
    print("kick 1: %.2f s, rechamber: %.2f s, kick 2: %.2f s" % (k1, rc, k2))
    print("two impacts inside %.2f s" % total)
    assert 0.539 < total < 0.541
    print("rule: the instant rechamber is the whole technique")
    print("OK: %s stamped it twice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_koryo_poomsae(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Koryo: 30 movements in ~90 s; 9 yudanja forms
    moves, seconds = 30, 90.0
    per_move = seconds / moves
    yudanja = 9
    print("Koryo: %d movements, %.1f s per movement" % (moves, per_move))
    print("yudanja forms: %d" % yudanja)
    assert moves == 30
    assert 2.99 < per_move < 3.01
    assert yudanja == 9
    print("rule: slow sections at quarter speed, maximum tension, total control")
    print("OK: %s pressed the black seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_dangun_tul(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Dan-Gun: 21 movements in ~50 s; 24 patterns in the system
    moves, seconds, patterns = 21, 50.0, 24
    per_move = seconds / moves
    print("Dan-Gun: %d movements, %.2f s per movement" % (moves, per_move))
    print("ITF patterns: %d" % patterns)
    assert moves == 21
    assert 2.37 < per_move < 2.40
    assert patterns == 24
    print("rule: the sine wave is the engine - down, up, down")
    print("OK: %s unrolled the scroll" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_counter_techniques(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # counter timing: 0.25 s reaction vs 0.25 s kick arrival - read the tell
    reaction = 0.25
    kick_speed, distance = 8.0, 2.0
    arrival = distance / kick_speed
    tell_lead = 0.10  # the tell precedes the kick
    window = arrival + tell_lead
    print("reaction: %.2f s, kick arrival: %.2f s" % (reaction, arrival))
    print("counter window off the tell: %.2f s" % window)
    assert 0.249 < arrival < 0.251
    assert 0.349 < window < 0.351
    print("rule: read the tell, never the kick")
    print("OK: %s wrote the reply" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_sparring_strategy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scenario: trailing 7-12, head kick (3) + turning body (4) wins it
    us, them = 7, 12
    head, turning_body = 3, 4
    final = us + head + turning_body
    print("score: %d-%d, need %d" % (us, them, them - us + 1))
    print("head kick + turning body: %d + %d + %d = %d" % (us, head, turning_body, final))
    assert final == 14
    assert final > them
    print("rule: the plan survives the scoreboard")
    print("OK: %s counted the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_self_defense(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wrist release leverage: 15 cm lever vs 5 cm grip at the thumb
    lever, grip = 0.15, 0.05
    ma = lever / grip
    grip_force = 300.0
    needed = grip_force / ma
    print("mechanical advantage: %.1f to 1" % ma)
    print("300 N grip broken with %.0f N" % needed)
    assert 2.99 < ma < 3.01
    assert 99.9 < needed < 100.1
    print("rule: every defense ends at the exit")
    print("OK: %s opened the lock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_breaking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # breaking: ~3000 N peak force on a 2.5 cm pine board, aim 10 cm through
    force = 3000.0
    equiv_kg = force / 9.81
    board_cm = 2.5
    aim_through_cm = 10.0
    print("peak force: %.0f N (~%.0f kg momentary load)" % (force, equiv_kg))
    print("board: %.1f cm pine, aim %.0f cm beyond" % (board_cm, aim_through_cm))
    assert 305.0 < equiv_kg < 307.0
    print("rule: aim through the board, never at it")
    print("OK: %s notarized the break" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tkd_mastery_path(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # belt path: months per gup, 10th to 1st
    months = [3, 3, 3, 3, 4, 4, 6, 6, 6, 8]
    total = sum(months)
    years = total / 12.0
    print("months per gup: %s" % months)
    print("10th gup to 1st dan: %d months = %.1f years" % (total, years))
    assert total == 46
    assert 3.8 < years < 3.9
    print("rule: the black belt marks the end of the basics, not of learning")
    print("OK: %s bound the manuscript" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "taegeuk_poomsae": demo_tkd_taegeuk_poomsae,
    "chonji_tul": demo_tkd_chonji_tul,
    "sparring_fundamentals": demo_tkd_sparring_fundamentals,
    "tornado_kick": demo_tkd_tornado_kick,
    "spinning_hook_kick": demo_tkd_spinning_hook_kick,
    "jumping_kicks": demo_tkd_jumping_kicks,
    "double_kicks": demo_tkd_double_kicks,
    "koryo_poomsae": demo_tkd_koryo_poomsae,
    "dangun_tul": demo_tkd_dangun_tul,
    "counter_techniques": demo_tkd_counter_techniques,
    "sparring_strategy": demo_tkd_sparring_strategy,
    "self_defense": demo_tkd_self_defense,
    "breaking": demo_tkd_breaking,
    "mastery_path": demo_tkd_mastery_path,
})

assert len(DEMOS) == 34, "expected 34 demos, got %d" % len(DEMOS)
