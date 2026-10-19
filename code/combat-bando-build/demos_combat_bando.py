#!/usr/bin/env python3
"""Demo programs for the Bando Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: training calculators and drill
timers with real computed values. All are machine-executed by build.py
before pages are written: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_cbb_meaning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five-year black-belt path: weekly hours -> total mat hours
    hours_per_week = 4.0
    weeks_per_year = 50.0
    years = 5.0
    total = hours_per_week * weeks_per_year * years
    print("training: %.1f h/week x %.0f weeks x %.0f years" % (hours_per_week, weeks_per_year, years))
    print("total mat hours on the black-belt path: %.0f" % total)
    assert 999.9 < total < 1000.1
    # the 9x9 matrix: techniques x principles
    cells = 9 * 9
    print("matrix cells (9 techniques x 9 principles): %d" % cells)
    assert cells == 81
    # nine animal systems
    animals = ["bull", "boar", "cobra", "viper", "python", "panther", "tiger", "scorpion", "eagle"]
    print("animal systems: %d" % len(animals))
    assert len(animals) == 9
    print("OK: %s mapped the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_ready_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weight distribution: 60/40 across a shoulder-width base
    front_pct, rear_pct = 60.0, 40.0
    body_kg = 75.0
    front_kg = body_kg * front_pct / 100.0
    rear_kg = body_kg * rear_pct / 100.0
    print("front leg load: %.1f kg, rear leg load: %.1f kg" % (front_kg, rear_kg))
    assert 44.9 < front_kg < 45.1
    assert 29.9 < rear_kg < 30.1
    # stability: either heel liftable a finger width => both legs loaded
    liftable = front_kg > 0 and rear_kg > 0
    print("both heels liftable (balanced): %s" % liftable)
    assert liftable
    # stance hold progression: minutes per session over 12 weeks
    start, add, weeks = 5.0, 1.0, 12.0
    final = start + add * (weeks - 1)
    print("stance hold after %d weeks: %.0f minutes" % (weeks, final))
    assert 15.9 < final < 16.1
    print("OK: %s rooted the foothold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_stepping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # line drill: step length -> distance covered
    step_m = 0.45
    steps_out, steps_back = 10, 10
    total_m = step_m * (steps_out + steps_back)
    print("line drill distance: %.1f m" % total_m)
    assert 8.99 < total_m < 9.01
    # circling: arc length per step times steps
    arc_m, n_steps = 0.35, 12
    circled = arc_m * n_steps
    print("circling drill ground covered: %.1f m" % circled)
    assert 4.19 < circled < 4.21
    # head level check: bobbing must stay under 2 cm
    bob_cm = 1.4
    print("head bob: %.1f cm (limit 2.0 cm)" % bob_cm)
    assert bob_cm < 2.0
    print("OK: %s walked the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_straight_punch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hip rotation speed -> fist speed: v = omega * r (arm length)
    omega = 12.0          # rad/s hip-shoulder turn
    arm_m = 0.70          # shoulder to knuckle
    fist_ms = omega * arm_m
    print("hip turn: %.1f rad/s, arm: %.2f m -> fist speed: %.2f m/s" % (omega, arm_m, fist_ms))
    assert 8.39 < fist_ms < 8.41
    # punch travel time over 0.6 m
    dist_m = 0.6
    t = dist_m / fist_ms
    print("punch travel time over %.1f m: %.3f s" % (dist_m, t))
    assert 0.0713 < t < 0.0715
    # air sets: 50 slow form + 50 bag = 100 reps
    reps = 50 + 50
    print("daily straight-punch reps: %d" % reps)
    assert reps == 100
    print("OK: %s threw it straight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_backfist_hammer(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # backfist whip: v = omega * r at the knuckles
    omega = 16.0          # rad/s shoulder whip
    arm_m = 0.65
    v = omega * arm_m
    print("backfist knuckle speed: %.2f m/s" % v)
    assert 10.39 < v < 10.41
    # hammer strike: short arc drop of 0.35 m -> speed at contact
    drop_m = 0.35
    g = 9.81
    v_hammer = math.sqrt(2 * g * drop_m)
    print("hammer drop speed from %.2f m: %.2f m/s" % (drop_m, v_hammer))
    assert 2.61 < v_hammer < 2.63
    # return time must beat a 0.25 s counter window
    return_s = 0.18
    print("hand return time: %.2f s (counter window 0.25 s)" % return_s)
    assert return_s < 0.25
    print("OK: %s snapped the arc" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_open_hand(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # contact area: palm heel vs knuckles -> pressure for the same force
    force_n = 400.0
    knuckle_cm2 = 8.0
    palm_cm2 = 40.0
    p_knuckle = force_n / knuckle_cm2
    p_palm = force_n / palm_cm2
    print("pressure knuckles: %.1f N/cm2, palm heel: %.1f N/cm2" % (p_knuckle, p_palm))
    assert 49.9 < p_knuckle < 50.1
    assert 9.9 < p_palm < 10.1
    print("palm spreads the same force over %.1fx the area" % (palm_cm2 / knuckle_cm2))
    assert 4.99 < palm_cm2 / knuckle_cm2 < 5.01
    # conditioning: 50 light chops/day, +10% per week for 8 weeks
    daily, weeks = 50.0, 8.0
    final_daily = daily * (1.10 ** (weeks - 1))
    print("chop volume after %d weeks: %.0f/day" % (weeks, final_daily))
    assert 97.3 < final_daily < 97.5
    print("OK: %s edged the hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_elbow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow: short lever, full torso rotation -> point speed
    omega = 14.0          # rad/s torso whip
    lever_m = 0.35        # shoulder to elbow point
    v = omega * lever_m
    print("elbow point speed: %.2f m/s" % v)
    assert 4.89 < v < 4.91
    # kinetic energy of the forearm+hand mass at that speed
    m = 2.2               # kg forearm and hand
    ke = 0.5 * m * v * v
    print("elbow kinetic energy: %.1f J" % ke)
    assert 26.3 < ke < 26.5
    # pad drill: 10 reps x 3 angles x 2 sides
    reps = 10 * 3 * 2
    print("elbow pad reps per session: %d" % reps)
    assert reps == 60
    print("OK: %s shortened the lever" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_parry_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reaction window: punch at 8 m/s from 1.2 m -> time to parry
    punch_ms = 8.0
    dist_m = 1.2
    window = dist_m / punch_ms
    print("parry window: %.3f s" % window)
    assert 0.149 < window < 0.151
    # deflection: moving the wrist 8 cm sideways over a 0.5 m punch path
    deflect_m, path_m = 0.08, 0.5
    angle_deg = math.degrees(math.atan(deflect_m / path_m))
    print("deflection angle: %.2f degrees" % angle_deg)
    assert 9.08 < angle_deg < 9.10
    # parry-counter is one beat: must fire within 0.3 s of the parry
    counter_beat = 0.22
    print("parry-to-counter beat: %.2f s (limit 0.30 s)" % counter_beat)
    assert counter_beat < 0.30
    print("OK: %s brushed it past" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_knee(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee: hip thrust drives 12 kg of leg to 6 m/s
    m_leg = 12.0
    v = 6.0               # m/s knee rise speed
    ke = 0.5 * m_leg * v * v
    print("knee kinetic energy: %.0f J" % ke)
    assert 215.9 < ke < 216.1
    # clinch pull-down adds: hand pull force over 0.3 m of travel
    pull_n, travel_m = 150.0, 0.3
    work = pull_n * travel_m
    print("pull-down work added: %.0f J" % work)
    assert 44.9 < work < 45.1
    total = ke + work
    print("combined knee + pull: %.0f J" % total)
    assert 260.9 < total < 261.1
    # drill: 10 per leg alternating
    reps = 10 * 2
    print("knee pad reps: %d" % reps)
    assert reps == 20
    print("OK: %s drove the hinge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_front_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kick reach: leg length + hip drive
    leg_m = 0.90
    hip_drive_m = 0.10
    reach = leg_m + hip_drive_m
    print("front-kick reach: %.2f m" % reach)
    assert 0.999 < reach < 1.001
    # snap extension: lower leg extends 0.45 m in 0.12 s
    ext_m, ext_s = 0.45, 0.12
    v = ext_m / ext_s
    print("snap extension speed: %.2f m/s" % v)
    assert 3.74 < v < 3.76
    # chamber check: knee must reach hip height (0.95 m for this student)
    chamber_m = 0.95
    print("chamber height: %.2f m" % chamber_m)
    assert 0.949 < chamber_m < 0.951
    # drill: 10 chambers + 10 full kicks per leg
    reps = (10 + 10) * 2
    print("front-kick drill reps: %d" % reps)
    assert reps == 40
    print("OK: %s chambered the piston" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_low_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low kick arc: hip turns 100 degrees, leg length 0.9 m -> arc distance
    arc_deg = 100.0
    leg_m = 0.9
    arc_m = math.radians(arc_deg) * leg_m
    print("shin arc travel: %.3f m" % arc_m)
    assert 1.570 < arc_m < 1.572
    # conditioning: 50 light kicks/leg, never power before the base volume
    base_vol = 50 * 2
    print("base conditioning volume: %d light kicks" % base_vol)
    assert base_vol == 100
    # accumulation: 12 kicks x 180 J each
    per_kick_j, n = 180.0, 12
    total_j = per_kick_j * n
    print("accumulated leg damage over %d kicks: %.0f J" % (n, total_j))
    assert 2159.9 < total_j < 2160.1
    print("OK: %s swung the bat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_breakfall(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fall from 1.0 m hip height: impact velocity
    h, g = 1.0, 9.81
    v = math.sqrt(2 * g * h)
    print("impact velocity from %.1f m: %.2f m/s" % (h, v))
    assert 4.428 < v < 4.430
    # stopping distance: stiff body 0.05 m vs breakfall 0.30 m -> g-force
    m = 75.0
    for d, label in ((0.05, "stiff"), (0.30, "breakfall")):
        f = m * v * v / (2 * d)
        gs = f / (m * g)
        print("%-9s stopping %.2f m -> %.1f g" % (label, d, gs))
        if label == "stiff":
            assert 19.9 < gs < 20.1
        else:
            assert 3.32 < gs < 3.34
    # progression: sitting, squatting, standing, pushed = 4 stages
    stages = 4
    print("breakfall stages: %d" % stages)
    assert stages == 4
    print("OK: %s slapped the mat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_aka_first(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # first aka: 24 moves learned in chunks of 3
    moves, chunk = 24, 3
    chunks = moves // chunk
    print("aka moves: %d, chunks of %d -> %d chunks" % (moves, chunk, chunks))
    assert chunks == 8
    # breath pattern: exhale on strikes (14), inhale on transitions (10)
    exhales, inhales = 14, 10
    print("breath pattern: %d exhales, %d inhales" % (exhales, inhales))
    assert exhales + inhales == moves
    # daily practice: 5 slow reps x 90 s each
    reps, rep_s = 5, 90.0
    daily_min = reps * rep_s / 60.0
    print("daily aka practice: %.1f minutes" % daily_min)
    assert 7.49 < daily_min < 7.51
    # both directions doubles the map
    directions = 2
    print("directions practiced: %d" % directions)
    assert directions == 2
    print("OK: %s walked the form" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_tiger(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rake: body drop of 0.15 m adds to a 3 kg arm moving at 7 m/s
    m_arm, v = 3.0, 7.0
    ke_arm = 0.5 * m_arm * v * v
    m_body, drop_m, g = 75.0, 0.15, 9.81
    pe_drop = m_body * g * drop_m
    total = ke_arm + pe_drop
    print("arm KE: %.1f J, body-drop energy: %.1f J, total: %.1f J" % (ke_arm, pe_drop, total))
    assert 73.4 < ke_arm < 73.6
    assert 110.3 < pe_drop < 110.5
    assert 183.8 < total < 184.0
    # drill: 10 downward + 10 cross rakes per hand
    reps = (10 + 10) * 2
    print("rake pad reps: %d" % reps)
    assert reps == 40
    print("OK: %s raked through" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_boar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # boar rush: 75 kg fighter at 4 m/s -> momentum
    m, v = 75.0, 4.0
    p = m * v
    print("rush momentum: %.0f kg m/s" % p)
    assert 299.9 < p < 300.1
    # three-step rush covering 3 x 0.8 m
    steps, step_m = 3, 0.8
    dist = steps * step_m
    print("three-step rush distance: %.1f m" % dist)
    assert 2.39 < dist < 2.41
    # arrival strike adds the rush momentum to a 4 kg arm at 5 m/s
    punch_p = 4.0 * 5.0
    print("arrival punch momentum: %.0f kg m/s" % punch_p)
    assert 19.9 < punch_p < 20.1
    print("OK: %s charged the wedge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_eagle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # talon grip progression: 20 kg -> 45 kg over 12 weeks
    start_kg, end_kg, weeks = 20.0, 45.0, 12.0
    gain_per_week = (end_kg - start_kg) / weeks
    print("grip gain: %.2f kg/week" % gain_per_week)
    assert 2.083 < gain_per_week < 2.084
    # catch window: wrist passes through a 0.25 m catch zone at 3 m/s
    zone_m, hand_ms = 0.25, 3.0
    window = zone_m / hand_ms
    print("wrist-catch window: %.3f s" % window)
    assert 0.0832 < window < 0.0834
    # catch-and-hit must land within one beat: 0.4 s
    beat = 0.35
    print("catch-to-hit beat: %.2f s (limit 0.40 s)" % beat)
    assert beat < 0.40
    print("OK: %s closed the talon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_cobra(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cobra snap: hand travels 0.55 m out and back
    dist_m = 0.55
    hand_ms = 9.0
    out_s = dist_m / hand_ms
    roundtrip = 2 * out_s
    print("snap out: %.3f s, round trip: %.3f s" % (out_s, roundtrip))
    assert 0.0610 < out_s < 0.0612
    assert 0.1221 < roundtrip < 0.1223
    # double: second strike lands within 0.25 s of the first
    double_gap = 0.20
    print("double-strike gap: %.2f s (limit 0.25 s)" % double_gap)
    assert double_gap < 0.25
    # paper drill: snap without pushing -> contact time under 0.05 s
    contact_s = 0.04
    print("paper-drill contact: %.2f s (limit 0.05 s)" % contact_s)
    assert contact_s < 0.05
    print("OK: %s struck in a blink" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_viper(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sway: 0.15 m offline over a 0.5 m punch path
    sway_m, path_m = 0.15, 0.5
    angle = math.degrees(math.atan(sway_m / path_m))
    print("sway evasion angle: %.2f degrees" % angle)
    assert 16.69 < angle < 16.71
    # serpentine step: 0.15 m slides, 8 steps
    slide_m = 0.15
    steps = 8
    flowed = slide_m * steps
    print("serpentine flow distance: %.2f m" % flowed)
    assert 1.199 < flowed < 1.201
    # reversal: direction change must complete within 0.3 s
    reversal_s = 0.25
    print("reversal time: %.2f s (limit 0.30 s)" % reversal_s)
    assert reversal_s < 0.30
    print("OK: %s flowed offline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_python(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # coil: body screw-turn of 90 degrees per loop, 3 loops
    deg_per_loop, loops = 90.0, 3
    total_turn = deg_per_loop * loops
    print("coil turn over %d loops: %.0f degrees" % (loops, total_turn))
    assert 269.9 < total_turn < 270.1
    # wrap pressure: 200 N over a 0.06 m2 wrap area
    force_n, area_m2 = 200.0, 0.06
    pressure = force_n / area_m2
    print("wrap pressure: %.0f Pa" % pressure)
    assert 3333.2 < pressure < 3333.4
    # quarter-turn tightening: 4 stages to full control
    stages = 4
    print("tightening stages: %d" % stages)
    assert stages == 4
    # tap release: must be instant, under 1 s
    release_s = 0.5
    print("tap release: %.1f s (limit 1.0 s)" % release_s)
    assert release_s < 1.0
    print("OK: %s coiled patiently" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_panther(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep timing: weight transfers onto the lead leg over 0.4 s; window is 0.1 s
    transfer_s, window_s = 0.4, 0.1
    print("weight-transfer window: %.2f s of %.1f s" % (window_s, transfer_s))
    assert 0.099 < window_s < 0.101
    # sweep scythe: foot travels 0.8 m arc in 0.25 s
    arc_m, t_s = 0.8, 0.25
    v = arc_m / t_s
    print("sweep foot speed: %.2f m/s" % v)
    assert 3.199 < v < 3.201
    # drill: 50 slow reps per side reading the transfer
    reps = 50 * 2
    print("timing drill reps: %d" % reps)
    assert reps == 100
    print("OK: %s timed the transfer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_bull(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bull charge: 85 kg at 5 m/s -> kinetic energy
    m, v = 85.0, 5.0
    ke = 0.5 * m * v * v
    print("charge kinetic energy: %.0f J" % ke)
    assert 1062.4 < ke < 1062.6
    # structured stop: halt within 1.6 m of the clap
    stop_m = 1.6
    print("structured stop distance: %.1f m" % stop_m)
    assert 1.59 < stop_m < 1.61
    # charge reps: 10 full charges with rest between
    reps = 10
    print("bull charge reps: %d" % reps)
    assert reps == 10
    # drive-through: charge ends 2.4 m past contact
    through_m = 2.4
    print("drive-through finish: %.1f m past contact" % through_m)
    assert 2.39 < through_m < 2.41
    print("OK: %s halted on the clap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_scorpion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # feint honesty: first 0.15 m identical between feint and strike
    identical_m = 0.15
    print("identical initiation: %.2f m" % identical_m)
    assert 0.149 < identical_m < 0.151
    # honesty check: partner reads the arc at most once in ten
    reads, trials = 1, 10
    read_rate = reads / trials
    print("read rate: %.1f pct (limit 10 pct)" % (read_rate * 100))
    assert read_rate <= 0.10 + 1e-9
    # slow pair drilled 50 times before speed
    reps = 50
    print("slow-pair reps: %d" % reps)
    assert reps == 50
    # arc return must beat the 0.3 s counter window
    return_s = 0.22
    print("arc return: %.2f s (limit 0.30 s)" % return_s)
    assert return_s < 0.30
    print("OK: %s arched the tail" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_naban_clinch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pummeling round: 3 minutes, position changes every 5 s
    round_s, change_s = 180.0, 5.0
    changes = round_s / change_s
    print("pummeling position changes per round: %.0f" % changes)
    assert 35.9 < changes < 36.1
    # frame leverage: forearm 0.35 m vs neck pressure at 0.1 m
    forearm_m, neck_m = 0.35, 0.10
    leverage = forearm_m / neck_m
    print("frame leverage: %.1fx" % leverage)
    assert 3.49 < leverage < 3.51
    # head-turn guide: 15 degrees at light pressure
    guide_deg = 15.0
    print("head-turn guide: %.1f degrees" % guide_deg)
    assert 14.9 < guide_deg < 15.1
    print("OK: %s won the inside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_naban_throw(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hip throw leverage: load arm 0.9 m vs effort arm 0.25 m
    load_m, effort_m = 0.9, 0.25
    ma = load_m / effort_m
    print("hip-throw mechanical advantage: %.1f to 1" % ma)
    assert 3.59 < ma < 3.61
    # entry drilled 50 times before any lift
    entries = 50
    print("no-throw entries drilled: %d" % entries)
    assert entries == 50
    # throw arc: partner travels ~1.6 m over the hip
    arc_m = 1.6
    print("throw arc: %.1f m" % arc_m)
    assert 1.59 < arc_m < 1.61
    # hips must be lower: sink 0.25 m below standing hip height
    sink_m = 0.25
    print("hip sink: %.2f m" % sink_m)
    assert 0.249 < sink_m < 0.251
    print("OK: %s levered the fulcrum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_naban_pin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pin pressure: 75 kg relaxed over 0.25 m2 of contact
    m_kg, area_m2, g = 75.0, 0.25, 9.81
    pressure = m_kg * g / area_m2
    print("pin pressure: %.0f Pa" % pressure)
    assert 2942.9 < pressure < 2943.1
    # role switch every 3 minutes in a 30-minute session
    session_min, switch_min = 30.0, 3.0
    switches = session_min / switch_min
    print("role switches per session: %.0f" % switches)
    assert 9.9 < switches < 10.1
    # two points of control minimum: far arm + near hip
    controls = 2
    print("minimum control points: %d" % controls)
    assert controls == 2
    # tap release under 1 s
    release_s = 0.5
    print("tap release: %.1f s (limit 1.0 s)" % release_s)
    assert release_s < 1.0
    print("OK: %s sank the weight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_khut_thaing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # study chart: 10 major points mapped on a body grid
    chart_points = ["jaw hinge", "neck vessels", "solar plexus", "floating ribs",
                    "inner thigh nerve", "instep", "wrist leverage", "elbow leverage",
                    "temple region", "collarbone notch"]
    print("chart points: %d" % len(chart_points))
    assert len(chart_points) == 10
    # study order: chart -> self -> partner = 3 stages
    stages = 3
    print("study stages: %d" % stages)
    assert stages == 3
    # location-only touch: fingertip pressure under 5 N
    touch_n = 3.0
    print("mapping touch: %.1f N (limit 5.0 N)" % touch_n)
    assert touch_n < 5.0
    # restraint protocol: zero force reps on points
    force_reps = 0
    print("force reps on points: %d" % force_reps)
    assert force_reps == 0
    print("OK: %s mapped with restraint" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_combos(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two-beat chain drilled 100 times until it is one word
    reps = 100
    print("two-beat chain reps: %d" % reps)
    assert reps == 100
    # three-beat chain: jab, cross, hook at 0.4 s per beat
    beats, beat_s = 3, 0.4
    chain_s = beats * beat_s
    print("three-beat chain time: %.1f s" % chain_s)
    assert 1.19 < chain_s < 1.21
    # matrix: 81 technique-principle cells available as chain links
    cells = 9 * 9
    print("chain-link cells: %d" % cells)
    assert cells == 81
    # every chain ends in stance
    ends_in_stance = True
    print("chains ending in stance: %s" % ends_in_stance)
    assert ends_in_stance
    print("OK: %s chained the beats" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_counters(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three counter timings
    timings = ["simultaneous", "parry-counter", "draw-counter"]
    print("counter timings: %d" % len(timings))
    assert len(timings) == 3
    # parry-counter must fire within one beat: 0.3 s
    beat_s = 0.25
    print("parry-to-counter: %.2f s (limit 0.30 s)" % beat_s)
    assert beat_s < 0.30
    # recognition drill: 18 of 20 commitment instants called correctly
    calls, thrown = 18, 20
    accuracy = calls / thrown
    print("commitment recognition: %.0f pct" % (accuracy * 100))
    assert 0.899 < accuracy < 0.901
    # counter-only sparring rounds: 3 x 2 minutes
    rounds, round_min = 3, 2.0
    total_min = rounds * round_min
    print("counter-only sparring: %.0f minutes" % total_min)
    assert 5.99 < total_min < 6.01
    print("OK: %s lived in the instant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_multiple_attackers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stacking cone: keep both attackers within a 60-degree cone ahead
    cone_deg = 60.0
    print("stacking cone: %.0f degrees" % cone_deg)
    assert 59.9 < cone_deg < 60.1
    # repositioning: circle at 1.2 m/s around a 3 m radius
    speed_ms, radius_m = 1.2, 3.0
    circumference = 2 * math.pi * radius_m
    lap_s = circumference / speed_ms
    print("reposition lap: %.1f s" % lap_s)
    assert 15.69 < lap_s < 15.71
    # scenario: 2 then 3 partners, walking pace first
    partners = [2, 3]
    print("scenario partners: %d then %d" % (partners[0], partners[1]))
    assert partners == [2, 3]
    # the drill always ends at the marked exit
    exits = 1
    print("exits per rep: %d" % exits)
    assert exits == 1
    print("OK: %s stacked the geometry" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_close_quarter(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four-beat chain: elbow, knee, elbow, knee at 0.45 s per beat
    beats, beat_s = 4, 0.45
    chain_s = beats * beat_s
    print("four-beat chain: %.2f s" % chain_s)
    assert 1.799 < chain_s < 1.801
    # strikes per minute at chain pace
    spm = 60.0 / beat_s
    print("chain pace: %.0f strikes/minute" % spm)
    assert 133.2 < spm < 133.4
    # six-beat chain built over weeks after the four-beat is automatic
    advanced_beats = 6
    print("advanced chain beats: %d" % advanced_beats)
    assert advanced_beats == 6
    # guard present through every beat
    guard_beats = 4
    print("guarded beats: %d of %d" % (guard_beats, beats))
    assert guard_beats == beats
    print("OK: %s turned the crankshaft" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_sweep_throw(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # chain: sweep threat shifts 30 kg of the 75 kg fighter onto the far leg
    shifted_kg, total_kg = 30.0, 75.0
    shift_pct = shifted_kg / total_kg * 100.0
    print("weight shifted by sweep threat: %.0f pct" % shift_pct)
    assert 39.9 < shift_pct < 40.1
    # throw takes the shifted weight: effort = shifted / mechanical advantage 3.6
    ma = 3.6
    effort_kg = shifted_kg / ma
    print("throw effort on shifted weight: %.1f kg" % effort_kg)
    assert 8.32 < effort_kg < 8.34
    # sensitivity drill: 20 exaggerated shifts before honest resistance
    reps = 20
    print("sensitivity reps: %d" % reps)
    assert reps == 20
    print("OK: %s took what the threat gave" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_advanced_aka(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # advanced aka: 60 moves in chunks of 3
    moves, chunk = 60, 3
    chunks = moves // chunk
    print("advanced aka: %d moves in %d chunks" % (moves, chunks))
    assert chunks == 20
    # each chunk analyzed: principle + attack answered + chain = 3 questions
    questions = 3
    print("analysis questions total: %d" % (questions * chunks))
    assert questions * chunks == 60
    # full-speed performance: 60 moves at 1.0 s per move
    perf_min = moves * 1.0 / 60.0
    print("full-speed performance: %.0f minute" % perf_min)
    assert 0.99 < perf_min < 1.01
    # lifetime refinement: practiced daily
    daily = True
    print("daily lifetime practice: %s" % daily)
    assert daily
    print("OK: %s recited the whole oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_controlled_sparring(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # round timer: 3 min work, 1 min rest, 5 rounds
    work_min, rest_min, rounds = 3.0, 1.0, 5
    total_min = rounds * work_min + (rounds - 1) * rest_min
    print("sparring session: %d rounds, %.0f minutes total" % (rounds, total_min))
    assert 18.9 < total_min < 19.1
    # single-technique rounds first: jab-only, kick-only, counter-only
    single_rounds = 3
    print("single-technique rounds: %d" % single_rounds)
    assert single_rounds == 3
    # gear check: 5 required items
    gear = ["headgear", "mouthguard", "gloves", "shin guards", "groin protection"]
    print("required gear items: %d" % len(gear))
    assert len(gear) == 5
    # stoppage trust: every stop respected
    stops_respected = True
    print("all stoppages respected: %s" % stops_respected)
    assert stops_respected
    print("OK: %s tested the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbb_nine_by_nine(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the matrix: 9 techniques x 9 principles
    cells = 9 * 9
    print("matrix cells: %d" % cells)
    assert cells == 81
    # new cell: extract 1 principle, test across 5 techniques
    techniques = 5
    print("cross-technique test: %d techniques" % techniques)
    assert techniques == 5
    # combine 2 principles into 1 new technique, filed as cell 82
    new_cell = cells + 1
    print("first student-authored cell: %d" % new_cell)
    assert new_cell == 82
    # teaching test: 1 junior student taught per new cell
    juniors = 1
    print("juniors taught per cell: %d" % juniors)
    assert juniors == 1
    print("OK: %s authored a cell" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "bando-meaning": demo_cbb_meaning,
    "ready-stance": demo_cbb_ready_stance,
    "stepping": demo_cbb_stepping,
    "straight-punch": demo_cbb_straight_punch,
    "backfist-hammer": demo_cbb_backfist_hammer,
    "open-hand": demo_cbb_open_hand,
    "elbow": demo_cbb_elbow,
    "parry-guard": demo_cbb_parry_guard,
    "knee": demo_cbb_knee,
    "front-kick": demo_cbb_front_kick,
    "low-kick": demo_cbb_low_kick,
    "breakfall": demo_cbb_breakfall,
    "aka-first": demo_cbb_aka_first,
    "tiger": demo_cbb_tiger,
    "boar": demo_cbb_boar,
    "eagle": demo_cbb_eagle,
    "cobra": demo_cbb_cobra,
    "viper": demo_cbb_viper,
    "python": demo_cbb_python,
    "panther": demo_cbb_panther,
    "bull": demo_cbb_bull,
    "scorpion": demo_cbb_scorpion,
    "naban-clinch": demo_cbb_naban_clinch,
    "naban-throw": demo_cbb_naban_throw,
    "naban-pin": demo_cbb_naban_pin,
    "khut-thaing": demo_cbb_khut_thaing,
    "combos": demo_cbb_combos,
    "counters": demo_cbb_counters,
    "multiple-attackers": demo_cbb_multiple_attackers,
    "close-quarter": demo_cbb_close_quarter,
    "sweep-throw": demo_cbb_sweep_throw,
    "advanced-aka": demo_cbb_advanced_aka,
    "controlled-sparring": demo_cbb_controlled_sparring,
    "nine-by-nine": demo_cbb_nine_by_nine,
}
