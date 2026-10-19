#!/usr/bin/env python3
"""Demo programs for the Snake Kung Fu Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: salute timing, breath cadence,
formation geometry, drill counting, conditioning ladders, form timing,
meridian counts. All are machine-executed by build.py: each prints its
real computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker. Entry text numbers are cross-checked
against these demo outputs.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_snk_salute(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the snake salute in five phases, three rounds at open and close
    phases = [("raise hands", 0.4), ("hold", 0.5), ("bow", 0.7),
              ("hold bow", 0.6), ("rise", 0.4)]
    one = sum(t for _, t in phases)
    total = one * 3
    for label, t in phases:
        print("  %-12s %4.1f s" % (label, t))
    print("one salute: %.1f s" % one)
    print("three salutes: %.1f s" % total)
    assert 2.59 < one < 2.61
    assert 7.79 < total < 7.81
    print("rule: the hands meet in exactly the same place every time")
    print("OK: %s saluted with precision" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_rest(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # breath cadence: in 4, pause 2, out 6 -> 12 s cycle
    cycle = 4 + 2 + 6
    minutes = 5
    cycles = minutes * 60 // cycle
    tidal_l = 0.5
    volume = cycles * tidal_l
    print("breath cycle: %d s (4 in, 2 pause, 6 out)" % cycle)
    print("cycles in %d minutes: %d" % (minutes, cycles))
    print("air moved: %.1f L" % volume)
    assert cycle == 12
    assert cycles == 25
    assert 12.4 < volume < 12.6
    print("rule: stillness is readiness at its most efficient")
    print("OK: %s rested in the coil" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_tongue_hand(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two fingers, ~2 cm each: narrow striking surface, alignment is all
    fingers = 2
    width_cm = 2.0
    surface = fingers * width_cm
    hold_s, holds, hands = 10, 6, 2
    total = hold_s * holds * hands
    print("striking surface: %d fingers x %.1f cm = %.1f cm" % (fingers, width_cm, surface))
    print("formation drill: %ds x %d holds x %d hands = %ds" % (hold_s, holds, hands, total))
    assert 3.9 < surface < 4.1
    assert total == 120
    print("rule: fingers, wrist, forearm - one straight line")
    print("OK: %s formed the tongue hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_head_palm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wrist snap through 45 degrees, 12 snaps per hand
    snap_deg = 45
    per_hand, hands = 12, 2
    total_snaps = per_hand * hands
    total_deg = snap_deg * total_snaps
    print("wrist snap: %d degrees" % snap_deg)
    print("snaps: %d per hand x %d hands = %d" % (per_hand, hands, total_snaps))
    print("total whip: %d degrees" % total_deg)
    assert total_snaps == 24
    assert total_deg == 1080
    print("rule: the arm carries, the wrist delivers")
    print("OK: %s snapped the snake head" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_waist(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # nine rotations each direction, four seconds per circle
    rotations, directions = 9, 2
    total_rot = rotations * directions
    total_deg = total_rot * 360
    secs = total_rot * 4
    print("rotations: %d x %d directions = %d" % (rotations, directions, total_rot))
    print("waist travel: %d degrees" % total_deg)
    print("time: %d s" % secs)
    assert total_rot == 18
    assert total_deg == 6480
    assert secs == 72
    print("rule: the waist leads and the limbs follow")
    print("OK: %s warmed the serpent waist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_finger_cond(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six-week fingertip pushup ladder per hand
    ladder = [5, 8, 10, 12, 15, 20]
    total = sum(ladder)
    for w, reps in enumerate(ladder, 1):
        print("  week %d: %d fingertip pushups per hand" % (w, reps))
    print("total per hand: %d" % total)
    assert ladder == sorted(ladder)
    assert total == 70
    print("rule: dull effort is training, sharp pain is damage")
    print("OK: %s conditioned the fingers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_step(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gliding steps: half a meter each, silent and level
    step_m, steps, seconds = 0.5, 40, 60
    distance = step_m * steps
    speed = distance / seconds
    print("steps: %d x %.1f m = %.1f m" % (steps, step_m, distance))
    print("time: %d s, speed: %.3f m/s" % (seconds, speed))
    assert 19.9 < distance < 20.1
    assert 0.33 < speed < 0.34
    print("rule: the head rides at one height")
    print("OK: %s glided the snake step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_coil_deflect(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ninety-degree attack guided into a thirty-degree miss
    incoming, outgoing = 90, 30
    redirection = incoming - outgoing
    sets, reps = 3, 10
    total = sets * reps
    print("incoming %d deg -> outgoing %d deg: %d deg redirection" % (incoming, outgoing, redirection))
    print("drill: %d sets x %d = %d deflections per side" % (sets, reps, total))
    assert redirection == 60
    assert total == 30
    print("rule: stick, spiral, release - never a hard block")
    print("OK: %s coiled the deflection" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_low_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hold ladder for the low snake stance
    ladder = [30, 45, 60, 90, 120]
    total = sum(ladder)
    for rung in ladder:
        print("  hold rung: %d s" % rung)
    print("total coil time: %d s" % total)
    assert ladder == sorted(ladder)
    assert total == 345
    print("rule: stillness at depth is a weapon")
    print("OK: %s held the low snake stance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_double_tongue(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two strikes per 1.2 s cycle, alternating hands
    cycle_s, per_cycle = 1.2, 2
    seconds = 60
    strikes = int(seconds / cycle_s) * per_cycle
    print("cycle: %.1f s for %d strikes" % (cycle_s, per_cycle))
    print("one minute: %d strikes" % strikes)
    assert strikes == 100
    print("rule: never commit both hands at once")
    print("OK: %s struck the double tongue" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_whips_tail(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 180-degree backfist arc, 20 sweeps per side
    arc, per_side, sides = 180, 20, 2
    total_sweeps = per_side * sides
    total_deg = arc * total_sweeps
    print("arc: %d degrees" % arc)
    print("sweeps: %d per side x %d = %d" % (per_side, sides, total_sweeps))
    print("total arc: %d degrees" % total_deg)
    assert total_sweeps == 40
    assert total_deg == 7200
    print("rule: the waist whips, the arm is the lash")
    print("OK: %s whipped the tail" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_eye_flicks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five shrinking rings, ten clean passes each
    rings_cm = [10, 8, 6, 5, 4]
    per_ring = 10
    total = len(rings_cm) * per_ring
    for r in rings_cm:
        print("  ring %d cm: %d clean passes" % (r, per_ring))
    print("total strikes: %d" % total)
    assert rings_cm == sorted(rings_cm, reverse=True)
    assert total == 50
    print("rule: precision defeats power")
    print("OK: %s flicked with precision" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_coiling_strike(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 270-degree wind, then the coil releases into the strike
    wind_deg = 270
    sets, reps = 3, 8
    total = sets * reps
    print("coil wind: %d degrees" % wind_deg)
    print("drill: %d sets x %d = %d strikes" % (sets, reps, total))
    assert wind_deg == 270
    assert total == 24
    print("rule: a strike without the wind is not this technique")
    print("OK: %s struck from the coil" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_creeps_down(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full height to coil in 1.5 s, ten transitions
    drop_s, reps = 1.5, 10
    total = drop_s * reps
    print("one transition: %.1f s" % drop_s)
    print("ten transitions: %.1f s of controlled dropping" % total)
    assert 14.9 < total < 15.1
    print("rule: the torso stays upright while the floor rushes up")
    print("OK: %s crept down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_darting_head(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1.2 m lunge, hand and body arriving as one event
    lunge_m, reps = 1.2, 12
    distance = lunge_m * reps
    print("lunge: %.1f m" % lunge_m)
    print("%d darts: %.1f m down the floor" % (reps, distance))
    assert 14.3 < distance < 14.5
    print("rule: the strike arrives with the lunge, never after")
    print("OK: %s darted the head strike" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_entwine(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stick, spiral, slide, settle - four moves, five slow reps
    moves, reps = 4, 5
    total = moves * reps
    print("sequence: stick, spiral, slide, settle (%d moves)" % moves)
    print("repetitions: %d -> %d entanglements" % (reps, total))
    assert total == 20
    print("rule: walking speed, zero force, geometry does the work")
    print("OK: %s entwined the branch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_rising(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # coil to full height in 1 s, 1.1 m of ascent
    rise_s, height_m, reps = 1.0, 1.1, 8
    total_s = rise_s * reps
    print("one rise: %.1f s, %.1f m" % (rise_s, height_m))
    print("%d rises: %.1f s of uncoiling" % (reps, total_s))
    assert 7.9 < total_s < 8.1
    assert 1.09 < height_m < 1.11
    print("rule: the legs uncoil the body, the hands never push")
    print("OK: %s rose as the serpent" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_vital1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twelve primary points mapped, ten of twelve to advance
    points_n, questions, needed = 12, 12, 10
    print("primary points mapped: %d" % points_n)
    print("study quiz: %d questions, %d correct to advance" % (questions, needed))
    assert points_n == 12
    assert needed == 10
    print("rule: educational anatomy only - never practiced on people")
    print("OK: %s mapped the twelve points" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_form1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eighteen movements, three seconds each, three rounds
    moves, per_move_s, rounds = 18, 3, 3
    one_round = moves * per_move_s
    total = one_round * rounds
    print("form: %d movements x %ds = %ds per round" % (moves, per_move_s, one_round))
    print("%d rounds: %ds" % (rounds, total))
    assert one_round == 54
    assert total == 162
    print("rule: slow until automatic, then full speed until transitions vanish")
    print("OK: %s performed form one" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_breathing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # in 6, hold 3, out 9 -> 18 s cycle
    cycle = 6 + 3 + 9
    minutes = 10
    cycles = minutes * 60 // cycle
    print("breath cycle: %d s (6 in, 3 hold, 9 out)" % cycle)
    print("cycles in %d minutes: %d" % (minutes, cycles))
    assert cycle == 18
    assert cycles == 33
    print("rule: the nine counts out are the whole lesson")
    print("OK: %s breathed the serpent breath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_coil_evasion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three directions, four reps each, 0.6 m per coil
    directions, reps, disp_m = 3, 4, 0.6
    total_coils = directions * reps
    total_m = total_coils * disp_m
    print("evasions: %d directions x %d = %d coils" % (directions, reps, total_coils))
    print("displacement: %d x %.1f m = %.1f m" % (total_coils, disp_m, total_m))
    assert total_coils == 12
    assert 7.19 < total_m < 7.21
    print("rule: evasion is relocation, not retreat")
    print("OK: %s coiled away" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_double_head(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 25 strike-and-guard pairs in 30 seconds
    pairs, seconds = 25, 30
    per_pair = seconds / pairs
    print("pairs: %d in %d s" % (pairs, seconds))
    print("one pair every %.1f s" % per_pair)
    assert 1.19 < per_pair < 1.21
    print("rule: two serpents instead of one")
    print("OK: %s struck double-headed" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_form2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twenty-four traveling movements, 3.5 s each, two rounds
    moves, per_move_s, rounds = 24, 3.5, 2
    one_round = moves * per_move_s
    total = one_round * rounds
    print("form: %d movements x %.1f s = %.1f s per round" % (moves, per_move_s, one_round))
    print("%d rounds: %.1f s" % (rounds, total))
    assert 83.9 < one_round < 84.1
    assert 167.9 < total < 168.1
    print("rule: the alphabet before the sentence - form one first")
    print("OK: %s crossed the river" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_vital2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twelve meridians, five noted points each
    meridians, per = 12, 5
    total = meridians * per
    print("meridians: %d" % meridians)
    print("points: %d x %d = %d" % (meridians, per, total))
    assert total == 60
    print("rule: book-and-body study only, light self-touch, never hard pressure")
    print("OK: %s charted the meridians" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_vs_crane(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five principles, three slow drills each
    principles, drills = 5, 3
    total = principles * drills
    print("principles: low/high, coil/wings, dart/evasion, guard eyes, never chase")
    print("drills: %d principles x %d = %d" % (principles, drills, total))
    assert total == 15
    print("rule: walking speed, theory not sparring")
    print("OK: %s studied the crane" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_form3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # thirty-six constricting movements, 4 s each, two rounds
    moves, per_move_s, rounds = 36, 4, 2
    one_round = moves * per_move_s
    total = one_round * rounds
    print("form: %d movements x %ds = %ds per round" % (moves, per_move_s, one_round))
    print("%d rounds: %ds" % (rounds, total))
    assert one_round == 144
    assert total == 288
    print("rule: the snake does not only dart, it holds")
    print("OK: %s coiled the python sequence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_iron_finger(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four-week bean-bag thrust ladder per hand
    ladder = [50, 75, 100, 125]
    total = sum(ladder)
    for w, reps in enumerate(ladder, 1):
        print("  week %d: %d thrusts per hand" % (w, reps))
    print("total per hand: %d" % total)
    assert ladder == sorted(ladder)
    assert total == 350
    print("rule: soak, massage, rest - iron is earned in seasons")
    print("OK: %s forged the iron finger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_silk(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 4 s per spiral circle, ten unbroken minutes
    per_circle_s, minutes = 4, 10
    coils = minutes * 60 // per_circle_s
    print("circle: %d s" % per_circle_s)
    print("coils in %d minutes: %d" % (minutes, coils))
    assert coils == 150
    print("rule: the silk must never break")
    print("OK: %s reeled the coiling silk" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_spear(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 100 thrusts a session, depth marked 2-5 cm over the months
    thrusts = 100
    depths_cm = [2, 3, 4, 5]
    print("thrusts per session: %d" % thrusts)
    print("penetration stages (cm): %s" % depths_cm)
    assert thrusts == 100
    assert depths_cm == sorted(depths_cm)
    assert depths_cm[-1] == 5
    print("rule: bag and dummy only - never people, never hard surfaces")
    print("OK: %s drove the spear hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_water(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six phases, two seconds each, five repetitions
    phases, per_s, reps = 6, 2, 5
    one = phases * per_s
    total = one * reps
    print("phases: %d x %ds = %ds per repetition" % (phases, per_s, one))
    print("%d repetitions: %ds of diving serpent" % (reps, total))
    assert one == 12
    assert total == 60
    print("rule: the strike belongs to the breach, not the dive")
    print("OK: %s struck the water" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_vital_drills(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight partner-safe drills, contact flag zero throughout
    drills = 8
    contact_flags = [0] * drills
    print("partner-safe drills: %d" % drills)
    print("contact flags: %s" % contact_flags)
    assert drills == 8
    assert all(f == 0 for f in contact_flags)
    print("rule: the deeper the knowledge, the lighter the hand")
    print("OK: %s drilled with restraint" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_python(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three wraps, two arms, five steps - control as position
    wraps, arms, steps = 3, 2, 5
    control_points = wraps * arms
    print("wraps: %d x %d arms = %d control points" % (wraps, arms, control_points))
    print("sequence steps: %d" % steps)
    assert control_points == 6
    assert steps == 5
    print("rule: control is a position, not a pressure")
    print("OK: %s coiled the python" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_form4(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # nine bends, four movements each, 4 s per movement
    bends, per_bend, per_move_s = 9, 4, 4
    moves = bends * per_bend
    total = moves * per_move_s
    print("form: %d bends x %d = %d movements" % (bends, per_bend, moves))
    print("time: %d x %ds = %ds" % (moves, per_move_s, total))
    assert moves == 36
    assert total == 144
    print("rule: every bend keeps the coil")
    print("OK: %s bent nine times" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_snk_master(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # all four forms in order: 18 + 24 + 36 + 36 movements
    forms = [18, 24, 36, 36]
    total_moves = sum(forms)
    avg_s = 3.5
    total_s = total_moves * avg_s
    print("forms: %s = %d movements" % (forms, total_moves))
    print("performance: %d x %.1f s = %.1f s" % (total_moves, avg_s, total_s))
    assert total_moves == 114
    assert 398.9 < total_s < 399.1
    print("rule: integration, not speed - one serpent, one signature")
    print("OK: %s completed the master sequence" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "salute": demo_snk_salute,
    "rest": demo_snk_rest,
    "tongue-hand": demo_snk_tongue_hand,
    "snake-head-palm": demo_snk_head_palm,
    "waist-coils": demo_snk_waist,
    "finger-conditioning": demo_snk_finger_cond,
    "snake-step": demo_snk_step,
    "coil-deflect": demo_snk_coil_deflect,
    "low-stance": demo_snk_low_stance,
    "double-tongue": demo_snk_double_tongue,
    "whips-tail": demo_snk_whips_tail,
    "eye-flicks": demo_snk_eye_flicks,
    "coiling-strike": demo_snk_coiling_strike,
    "creeps-down": demo_snk_creeps_down,
    "darting-head": demo_snk_darting_head,
    "entwines-branch": demo_snk_entwine,
    "rising-serpent": demo_snk_rising,
    "vital-theory-1": demo_snk_vital1,
    "form-one": demo_snk_form1,
    "snake-breathing": demo_snk_breathing,
    "coiling-evasion": demo_snk_coil_evasion,
    "double-headed": demo_snk_double_head,
    "form-two": demo_snk_form2,
    "vital-theory-2": demo_snk_vital2,
    "snake-vs-crane": demo_snk_vs_crane,
    "form-three": demo_snk_form3,
    "iron-finger": demo_snk_iron_finger,
    "silk-energy": demo_snk_silk,
    "spear-hand": demo_snk_spear,
    "strikes-water": demo_snk_water,
    "vital-applications": demo_snk_vital_drills,
    "python-coils": demo_snk_python,
    "form-four": demo_snk_form4,
    "master-sequence": demo_snk_master,
}
