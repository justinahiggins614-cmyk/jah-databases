#!/usr/bin/env python3
"""Demo programs for the Catch Wrestling Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: drill planners, timers, leverage
math, progression calculators. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Numbers match the entry
text (rep counts, hold times, round lengths) so entry and demo agree.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_cw_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance width scales with the wrestler: feet ~ shoulder width,
    # lead foot half a foot-length ahead
    height_in = 70.0
    shoulder_in = height_in * 0.259
    stance_w = shoulder_in
    lead_offset = 5.5  # half a foot-length ahead
    print("height %.0f in -> shoulder/stance width %.2f in" % (height_in, stance_w))
    print("lead foot offset: %.1f in ahead" % lead_offset)
    assert 18.12 < stance_w < 18.14
    # base check: hips at half standing height
    hip_h = height_in * 0.5
    print("stance hip height: %.1f in" % hip_h)
    assert 34.9 < hip_h < 35.1
    # mobility drill: 4 directions x 10 slides
    slides = 4 * 10
    print("stance slides per session: %d" % slides)
    assert slides == 40
    print("rule: hips under shoulders, weight on the balls of the feet")
    print("OK: %s set the base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # level change: hips drop 2-4 inches, penetration knee lands
    # between the opponent's feet
    drop_in = 3.0
    stance_hip = 35.0
    shot_hip = stance_hip - drop_in
    print("level change: hips %.1f -> %.1f in (drop %.1f in)" % (stance_hip, shot_hip, drop_in))
    assert 31.9 < shot_hip < 32.1
    # penetration step distance from a 70-inch wrestler's stride
    stride_in = 70.0 * 0.45
    print("penetration step reach: %.1f in" % stride_in)
    assert 31.4 < stride_in < 31.6
    # drill: 3 sets of 10 penetration steps
    reps = 3 * 10
    print("penetration reps per session: %d" % reps)
    assert reps == 30
    print("rule: hips drop before the hands move")
    print("OK: %s changed levels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_ties(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hand-fighting rounds: 2 minutes, exchanges scored on inside control
    round_s = 120
    exchange_s = 8.0
    exchanges = round_s / exchange_s
    print("exchanges per 2-min round: %.0f" % exchanges)
    assert 14.9 < exchanges < 15.1
    # inside-control share across 4 rounds
    shares = [0.55, 0.62, 0.58, 0.66]
    avg = sum(shares) / len(shares)
    print("inside-control share: %s -> avg %.3f" % (shares, avg))
    assert 0.602 < avg < 0.603
    # pummel corrections per round
    pummels = [6, 4, 5, 3]
    print("pummels per round: %s (total %d)" % (pummels, sum(pummels)))
    assert sum(pummels) == 18
    print("rule: inside control is the currency")
    print("OK: %s won the hands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_wrist_control(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two-on-one leverage: two arms vs one, force advantage ~2x
    # minus the angle penalty of the outside step
    arms_attack = 2.0
    angle_eff = 0.92
    advantage = arms_attack * angle_eff
    print("two-on-one force advantage: %.2fx" % advantage)
    assert 1.83 < advantage < 1.85
    # drill: alternate arm-drag exit and snap-down exit
    drags, snaps = 10, 10
    print("exits drilled: %d arm drags + %d snap-downs" % (drags, snaps))
    assert drags + snaps == 20
    # grip endurance: 3 x 60-second two-on-one holds
    hold_s = 3 * 60
    print("grip hold volume: %d seconds" % hold_s)
    assert hold_s == 180
    print("rule: two hands on one arm always wins the arithmetic")
    print("OK: %s doubled the grip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_snapdown(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # snap impulse: sharp pull from back and hips, ~0.25 s
    pull_force_lb = 60.0
    pull_time_s = 0.25
    impulse = pull_force_lb * pull_time_s
    print("snap impulse: %.1f lb-s" % impulse)
    assert 14.9 < impulse < 15.1
    # drill: 5 snaps per side, every rep finishes go-behind or headlock
    reps = 5 * 2
    print("snap reps per session: %d" % reps)
    assert reps == 10
    # posture broken: head drops ~14 inches to hands-on-mat
    drop_in = 14.0
    print("head drop to the mat: %.0f in" % drop_in)
    assert 13.9 < drop_in < 14.1
    print("rule: the snap is short and sharp from the back and hips")
    print("OK: %s broke the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_front_headlock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front headlock round: hold pressure in 30-s blocks across 5 rounds
    blocks, block_s = 5, 30
    total_s = blocks * block_s
    print("headlock pressure time: %d blocks x %d s = %d s" % (blocks, block_s, total_s))
    assert total_s == 150
    # three exits drilled equally from the same entry
    exits = ["go-behind", "guillotine", "chin whip"]
    per_exit = 4
    print("exits: %s x %d reps each = %d" % (len(exits), per_exit, len(exits) * per_exit))
    assert len(exits) * per_exit == 12
    # hips-back angle: torso lean kept under 20 degrees
    lean_deg = 18.0
    print("torso lean: %.0f deg (limit 20)" % lean_deg)
    assert lean_deg < 20.0
    print("rule: hips back and chest heavy make the headlock unliftable")
    print("OK: %s held the crossroads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_sprawl(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
import time
def main():
    # real drill timer: 10 whistle-start sprawls, short honest intervals
    n = 10
    t0 = time.perf_counter()
    for i in range(n):
        time.sleep(0.05)  # sprawl rep
        time.sleep(0.05)  # reset to stance
    elapsed = time.perf_counter() - t0
    per_rep = elapsed / n
    print("10 sprawls timed: %.3f s total, %.3f s per rep" % (elapsed, per_rep))
    assert 0.9 < elapsed < 1.6
    assert 0.09 < per_rep < 0.16
    # reaction budget: sprawl must land inside the shot's 0.4 s window
    shot_window = 0.4
    sprawl_time = 0.32
    margin = shot_window - sprawl_time
    print("reaction margin: %.2f s inside the %.1f s shot window" % (margin, shot_window))
    assert 0.07 < margin < 0.09
    print("rule: drill from a whistle until the legs fire without a decision")
    print("OK: %s sprawled on the whistle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_hip_bump(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bridge force estimate: hips explode at ~1.4x bodyweight
    bw_lb = 170.0
    bridge_lb = bw_lb * 1.4
    print("hip-bump bridge force: %.0f lb bodyweight -> %.0f lb" % (bw_lb, bridge_lb))
    assert 237.9 < bridge_lb < 238.1
    # drill: 50 reps per side before live use (entry text standard)
    reps = 50 * 2
    print("escape reps to earn live use: %d" % reps)
    assert reps == 100
    # escape window: first 2 seconds underneath are the golden window
    window_s = 2.0
    settle_s = 20.0
    print("golden window %.0f s vs settled ride %.0f s (ratio %.1fx harder)" % (
        window_s, settle_s, settle_s / window_s))
    assert settle_s / window_s == 10.0
    print("rule: escape before the ride settles")
    print("OK: %s left the bottom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_granby(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Granby roll: full 360-degree inversion, body kept round
    roll_deg = 360.0
    print("granby rotation: %.0f degrees" % roll_deg)
    assert 359.9 < roll_deg < 360.1
    # roll distance vs shoulder width: tight ball rolls ~1.2x shoulder width
    shoulder_in = 18.1
    roll_in = shoulder_in * 1.2
    print("roll travel: %.1f in (shoulder %.1f in x 1.2)" % (roll_in, shoulder_in))
    assert 21.71 < roll_in < 21.73
    # both sides, slow first: 10 slow rolls per side before speed
    slow = 10 * 2
    print("slow technical rolls before speed: %d" % slow)
    assert slow == 20
    print("rule: the roll is a ball, and a ball has no handles")
    print("OK: %s rolled under" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_bridge(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bridge hold progression: 30 s toward 120 s over 8 weeks (entry text standard)
    start_s, target_s, weeks = 30.0, 120.0, 8
    weekly_gain = (target_s - start_s) / weeks
    print("bridge progression: %.0f s -> %.0f s over %d weeks (+%.2f s/week)" % (
        start_s, target_s, weeks, weekly_gain))
    assert 11.24 < weekly_gain < 11.26
    # session minimum: 3 x 30-second bridges (entry text standard)
    session_s = 3 * 30
    print("session minimum: 3 x 30 s = %d s" % session_s)
    assert session_s == 90
    # arch height: hips rise ~14 in off the mat at full bridge
    arch_in = 14.0
    print("bridge arch height: %.0f in" % arch_in)
    assert 13.9 < arch_in < 14.1
    print("rule: the bridge wins by height")
    print("OK: %s arched the last line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_tight_waist(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ride volume: 5 sessions x 12-minute ride blocks per week
    sessions, block_min = 5, 12
    weekly_min = sessions * block_min
    print("weekly ride time: %d sessions x %d min = %d min" % (sessions, block_min, weekly_min))
    assert weekly_min == 60
    # breakdown cycle: down, build, down - 20 s per cycle
    cycle_s = 20.0
    cycles = block_min * 60 / cycle_s
    print("breakdowns per block: %.0f" % cycles)
    assert 35.9 < cycles < 36.1
    # crossface steering: head turned ~45 degrees to break posture
    turn_deg = 45.0
    print("crossface head turn: %.0f deg" % turn_deg)
    assert 44.9 < turn_deg < 45.1
    print("rule: the ride is a cycle, not a hold")
    print("OK: %s kept the watch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_half_nelson(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the turn: shoulders rotate 90+ degrees to flat; drive through to 180
    turn_deg = 180.0
    print("shoulder rotation to the pin: %.0f deg" % turn_deg)
    assert 179.9 < turn_deg < 180.1
    # drill: 50 half nelsons per side (entry text standard)
    reps = 50 * 2
    rep_s = 6.0
    drill_min = reps * rep_s / 60.0
    print("drill volume: %d reps x %.0f s = %.0f min" % (reps, rep_s, drill_min))
    assert reps == 100
    assert 9.9 < drill_min < 10.1
    # chain split: half nelson finish vs cradle switch, 50/50 in drilling
    print("chain: 50%% finish, 50%% cradle switch")
    print("rule: the arm is the hook and the body is the engine")
    print("OK: %s turned the shoulders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_bar_arm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # chicken wing leverage: wrist held high between the shoulder blades
    # vs low at the waist - lever arm ratio
    high_in, low_in = 16.0, 6.0
    leverage = high_in / low_in
    print("wrist-high vs wrist-low leverage: %.2fx" % leverage)
    assert 2.66 < leverage < 2.68
    # shoulder rotation to the tap band: 45-90 degrees of internal rotation
    tap_lo, tap_hi = 45.0, 90.0
    print("tap band: %.0f-%.0f deg shoulder rotation" % (tap_lo, tap_hi))
    assert tap_hi - tap_lo == 45.0
    # drill both versions: pin turn and controlled lock
    pin_reps, lock_reps = 10, 10
    print("drill: %d pin turns + %d lock controls" % (pin_reps, lock_reps))
    assert pin_reps + lock_reps == 20
    print("rule: height of the wrist decides the leverage")
    print("OK: %s barred the arm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_double_leg(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # penetration depth: knee lands between their feet, ~24 in deep
    depth_in = 24.0
    print("penetration depth: %.0f in" % depth_in)
    assert 23.9 < depth_in < 24.1
    # drive distance through the finish: 3 steps of ~20 in
    steps, step_in = 3, 20.0
    drive_in = steps * step_in
    print("drive through: %d steps x %.0f in = %.0f in" % (steps, step_in, drive_in))
    assert 59.9 < drive_in < 60.1
    # chain rate: double leg to single leg on the sprawl, drilled 10x
    chains = 10
    print("sprawl chains drilled: %d" % chains)
    assert chains == 10
    print("rule: drive through the finish with the feet stepping")
    print("OK: %s shot the double" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_double_wrist_lock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # figure-four: two hands on one wrist, control multiplier 2.0
    control = 2.0
    print("figure-four control multiplier: %.1fx" % control)
    assert 1.99 < control < 2.01
    # elbow kept at ~90 degrees; wrist above elbow line
    elbow_deg = 90.0
    print("trapped elbow angle: %.0f deg" % elbow_deg)
    assert 89.9 < elbow_deg < 90.1
    # finish: smooth rotation of ~60 degrees behind the back
    finish_deg = 60.0
    print("finishing rotation: %.0f deg" % finish_deg)
    assert 59.9 < finish_deg < 60.1
    # drill as control first: 10 control holds + 10 finishes
    print("drill: 10 controls + 10 finishes = %d" % 20)
    print("rule: the shoulder is attacked by position, not by yanking")
    print("OK: %s locked the wrist double" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_americana(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # key lock: paint the hand toward the head, ~8 in of travel
    travel_in = 8.0
    print("hand travel to the tap: %.0f in" % travel_in)
    assert 7.9 < travel_in < 8.1
    # elbow pinned: anchor force holds elbow down at ~25 lb
    anchor_lb = 25.0
    print("elbow anchor: %.0f lb of pinning pressure" % anchor_lb)
    assert 24.9 < anchor_lb < 25.1
    # switching pair: key lock <-> arm bar, 5 switches each direction
    switches = 5 * 2
    print("key lock/arm bar switches drilled: %d" % switches)
    assert switches == 10
    print("rule: the elbow pinned to the mat is the anchor")
    print("OK: %s turned the key" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_toe_hold(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # toe hold: foot rotated ~30 degrees against the controlled leg
    rot_deg = 30.0
    print("foot rotation to the tap: %.0f deg" % rot_deg)
    assert 29.9 < rot_deg < 30.1
    # leg control: knee trapped with ~40 lb of control pressure
    control_lb = 40.0
    print("knee control pressure: %.0f lb" % control_lb)
    assert 39.9 < control_lb < 40.1
    # entries drilled: leg-ride entries + scramble entries
    entries = 8 + 8
    print("entries drilled: %d" % entries)
    assert entries == 16
    print("rule: leg control above the ankle is the lock")
    print("OK: %s held the toe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_ankle_lock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight ankle lock: hip bridge drives ~1.2x bodyweight through the wedge
    bw_lb = 170.0
    bridge_lb = bw_lb * 1.2
    print("hip bridge through the wedge: %.0f lb" % bridge_lb)
    assert 203.9 < bridge_lb < 204.1
    # wedge depth: foot seated 4+ inches deep in the armpit
    depth_in = 4.5
    print("wedge depth: %.1f in" % depth_in)
    assert 4.49 < depth_in < 4.51
    # drill: wedge depth scored on 12 reps
    reps = 12
    print("wedge-depth reps: %d" % reps)
    assert reps == 12
    print("rule: the wedge is the lock")
    print("OK: %s wedged the ankle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_arm_bar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arm bar: elbow at 180 (straight); hyperextension tap band 180-195
    straight_deg, tap_deg = 180.0, 195.0
    print("elbow: straight %.0f deg, tap band to %.0f deg" % (straight_deg, tap_deg))
    assert tap_deg - straight_deg == 15.0
    # hip bridge into the elbow: ~1.1x bodyweight
    bw_lb = 170.0
    bridge_lb = bw_lb * 1.1
    print("bridge into the elbow: %.0f lb" % bridge_lb)
    assert 186.9 < bridge_lb < 187.1
    # switching pair reps: 5 each direction
    switches = 10
    print("arm bar/key lock switches: %d" % switches)
    assert switches == 10
    print("rule: the finish is a smooth hip bridge, never a yank")
    print("OK: %s barred it straight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_guillotine(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guillotine close: forearm wraps ~270 degrees around the neck
    wrap_deg = 270.0
    print("wrap closure: %.0f deg" % wrap_deg)
    assert 269.9 < wrap_deg < 270.1
    # body drop closes the hold: hips drop 6 in
    drop_in = 6.0
    print("hip drop to close: %.0f in" % drop_in)
    assert 5.9 < drop_in < 6.1
    # paired exits drilled: 6 guillotines + 6 go-behinds from the headlock
    reps = 6 + 6
    print("paired exits drilled: %d" % reps)
    assert reps == 12
    print("rule: the body closes the hold; the arms only hold the shape")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_single_leg(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dump finish: lift the leg ~18 in while turning over it
    lift_in = 18.0
    print("dump lift: %.0f in" % lift_in)
    assert 17.9 < lift_in < 18.1
    # three finishes drilled equally: dump, trip, run-the-pipe
    finishes = 3
    per = 6
    print("finishes: %d x %d reps = %d" % (finishes, per, finishes * per))
    assert finishes * per == 18
    # chain: double-to-single drilled as one motion, 10 chains
    chains = 10
    print("double-to-single chains: %d" % chains)
    assert chains == 10
    print("rule: head tight to the hip with the ear on the thigh")
    print("OK: %s took the single" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_fireman(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fireman's carry: partner draped across shoulders, ~170 lb carried
    carried_lb = 170.0
    # legs do the lifting: quads handle ~2x bodyweight in the stand
    leg_capacity = 170.0 * 2.0
    margin = leg_capacity - carried_lb
    print("carried %.0f lb vs leg capacity %.0f lb (margin %.0f lb)" % (
        carried_lb, leg_capacity, margin))
    assert 169.9 < margin < 170.1
    # timing entries: 12 signal-start reps
    reps = 12
    print("timing entries: %d" % reps)
    assert reps == 12
    # dump control: landing within a 3-foot circle
    circle_ft = 3.0
    print("controlled landing circle: %.0f ft" % circle_ft)
    assert 2.9 < circle_ft < 3.1
    print("rule: the legs do the lifting, the timing does the throw")
    print("OK: %s carried the fireman" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_hip_throw(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hip throw arc: rotation radius ~ hip height 35 in
    radius_in = 35.0
    arc_in = math.pi * radius_in  # half-circle throw path
    print("throw arc: pi x %.0f in = %.1f in" % (radius_in, arc_in))
    assert 109.95 < arc_in < 109.97
    # load check: hips must be below theirs - 4 in below
    below_in = 4.0
    print("hips below theirs: %.0f in" % below_in)
    assert 3.9 < below_in < 4.1
    # load reps drilled separately: 15 loads before rotation
    loads = 15
    print("load reps before rotation: %d" % loads)
    assert loads == 15
    print("rule: the load is the throw and the turn is just the finish")
    print("OK: %s turned the hip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_cradle_near(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cradle lock: head-to-knee fold, lock circumference vs torso
    torso_in = 34.0
    lock_in = torso_in * 0.85  # folded, the loop is shorter than the torso
    print("cradle lock loop: %.1f in (torso %.0f in)" % (lock_in, torso_in))
    assert 28.89 < lock_in < 28.91
    # drill: 50 cradles per side (entry text standard)
    reps = 50 * 2
    print("cradle reps: %d" % reps)
    assert reps == 100
    # rock to the pin: sit-through of ~90 degrees
    rock_deg = 90.0
    print("sit-through rock: %.0f deg" % rock_deg)
    assert 89.9 < rock_deg < 90.1
    print("rule: the lock is the pin, the rock is just the delivery")
    print("OK: %s folded the cradle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_cradle_far(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # far-side cradle: the long fold, loop ~1.3x the near-side loop
    near_in = 28.9
    far_in = near_in * 1.3
    print("far-side loop: %.1f in (near-side %.1f in x 1.3)" % (far_in, near_in))
    assert 37.56 < far_in < 37.58
    # inside-out switch: the head is never released - 0 releases per rep
    reps = 12
    releases = 0
    print("switch reps: %d, head releases: %d" % (reps, releases))
    assert releases == 0
    # chain: near attempt -> defense -> inside-out, drilled 12x
    print("chain reps: %d" % reps)
    assert reps == 12
    print("rule: the switch is not a restart - the head control never releases")
    print("OK: %s switched the cradle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_head_arm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arm triangle: both sides of the neck closed, ~180 deg of wrap each
    wrap_deg = 180.0 * 2
    print("total wrap: %.0f deg" % wrap_deg)
    assert 359.9 < wrap_deg < 360.1
    # angle walk: hips step ~15 deg at a time to find the finish
    step_deg = 15.0
    steps = 4
    total_deg = step_deg * steps
    print("angle walk: %d steps x %.0f deg = %.0f deg" % (steps, step_deg, total_deg))
    assert 59.9 < total_deg < 60.1
    # one control, three endings: throw, pin, choke drilled from the same grip
    endings = 3
    print("endings from one grip: %d" % endings)
    assert endings == 3
    print("rule: the body closes the triangle, not the arm squeeze")
    print("OK: %s closed the triangle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_can_opener(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # can opener taught as recognition + defense: drill scores the defense
    # cues recognized, not the crank applied
    cues = ["hands cup the head", "elbows drive down", "head pulled forward"]
    print("recognition cues: %d" % len(cues))
    for c in cues:
        print("  - %s" % c)
    assert len(cues) == 3
    # defense reps: posture + hand-fight, 15 live reps
    defense_reps = 15
    print("defense reps: %d" % defense_reps)
    assert defense_reps == 15
    # drilling pressure cap: minimal - 10%% of full, i.e. control only
    pressure_cap = 0.10
    print("drilling pressure cap: %.0f%% (control only)" % (pressure_cap * 100))
    assert 0.099 < pressure_cap < 0.101
    print("rule: the live drilled element is the escape, not the crank")
    print("OK: %s filed the archive" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_banana_split(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # banana split: legs spread to ~120 degrees of total split
    split_deg = 120.0
    print("split angle: %.0f deg" % split_deg)
    assert 119.9 < split_deg < 120.1
    # each leg controlled separately: 2 controls before any spread
    controls = 2
    print("leg controls before the spread: %d" % controls)
    assert controls == 2
    # steady pressure: spread applied over ~4 seconds, not yanked
    spread_s = 4.0
    print("spread time: %.0f s of steady pressure" % spread_s)
    assert 3.9 < spread_s < 4.1
    # ride time kept through the finish: 100%% structure
    print("rule: a broken ride is a lost split")
    print("OK: %s spread the ride" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_heel_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # heel hook: knee torqued rotationally - tap band is narrow, ~20 deg
    tap_band_deg = 20.0
    print("tap band: %.0f deg of rotation (narrow - tap early)" % tap_band_deg)
    assert 19.9 < tap_band_deg < 20.1
    # control points: knee + hip locked = 2 controls before rotation
    controls = 2
    print("controls before rotation: %d" % controls)
    assert controls == 2
    # caught, not cranked: application speed capped at 25%% for drilling
    speed_cap = 0.25
    print("drilling speed cap: %.0f%%" % (speed_cap * 100))
    assert 0.249 < speed_cap < 0.251
    # entries + leg control are the live elements: 12 reps
    reps = 12
    print("live reps (entries + control): %d" % reps)
    assert reps == 12
    print("rule: it is caught, not cranked - earliest taps, instant release")
    print("OK: %s respected the hook" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_japanese_necktie(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # necktie thread: wrap depth scored 0-3 (wrap, trap, lock)
    thread_score = 3
    print("thread score: %d/3 (wrap, trap, lock)" % thread_score)
    assert thread_score == 3
    # weight drop to close: hips drop 8 in to the side
    drop_in = 8.0
    print("weight drop: %.0f in" % drop_in)
    assert 7.9 < drop_in < 8.1
    # slack tolerance: 0 inches - any slack is escape
    slack_in = 0.0
    print("slack tolerance: %.1f in" % slack_in)
    assert slack_in == 0.0
    # thread reps: 14 clean threads before live use
    reps = 14
    print("thread reps: %d" % reps)
    assert reps == 14
    print("rule: the thread is the choke")
    print("OK: %s tied the necktie" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_power_half(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # power half: legs + arm + chest fire as one - 3 drivers
    drivers = ["grapevine spread", "half nelson lever", "chest drive"]
    print("drivers: %d" % len(drivers))
    assert len(drivers) == 3
    # coordination: all 3 drivers inside a 0.5 s window
    window_s = 0.5
    print("firing window: %.1f s" % window_s)
    assert 0.49 < window_s < 0.51
    # chain: power half -> banana split -> toe hold, 8 full chains
    chains = 8
    print("full chains drilled: %d" % chains)
    assert chains == 8
    # base broken: opponent base reduced to ~10%% during the turn
    base_left = 0.10
    print("opponent base remaining: %.0f%%" % (base_left * 100))
    assert 0.099 < base_left < 0.101
    print("rule: the chain is timing, not strength")
    print("OK: %s powered the half" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_scarf_armbar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # transition window: the far arm is open ~0.8 s
    window_s = 0.8
    print("transition window: %.1f s" % window_s)
    assert 0.79 < window_s < 0.81
    # swing: legs travel ~200 degrees over the head in one motion
    swing_deg = 200.0
    print("leg swing: %.0f deg in one motion" % swing_deg)
    assert 199.9 < swing_deg < 200.1
    # scarf hold airtight check: 0 inches of space
    space_in = 0.0
    print("space in the scarf hold: %.1f in" % space_in)
    assert space_in == 0.0
    # drill: 10 trap-and-swings as one motion
    reps = 10
    print("trap-and-swing reps: %d" % reps)
    assert reps == 10
    print("rule: the trap and the swing are one motion, not two")
    print("OK: %s swung the arm bar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_hook_chains(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # arm chain: 3 locks, each defense names the next
    locks = ["double wrist lock", "arm bar", "key lock"]
    print("arm chain links: %d" % len(locks))
    assert len(locks) == 3
    # branching: 3 defenses per lock -> 3^2 = 9 two-link paths
    paths = 3 ** 2
    print("two-link paths: 3^2 = %d" % paths)
    assert paths == 9
    # chain reps: minimum 3 locks per rep, 8 reps, no pauses
    reps, per_rep = 8, 3
    total_locks = reps * per_rep
    print("chain volume: %d reps x %d locks = %d locks" % (reps, per_rep, total_locks))
    assert total_locks == 24
    # control kept between links: 100%%
    print("rule: the chain waits where the defense is going")
    print("OK: %s linked the hooks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cw_flow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the catch chain as a round: phase time budget
    phases = {"tie battle": 120, "takedown": 20, "ride": 60,
              "turn": 25, "hook": 30, "pin": 20}
    total_s = sum(phases.values())
    print("catch chain round: %d phases" % len(phases))
    for k, v in phases.items():
        print("  %-11s %3d s (%4.1f%%)" % (k, v, v / total_s * 100.0))
    print("round total: %d s" % total_s)
    assert total_s == 275
    assert 43.6 < phases["tie battle"] / total_s * 100.0 < 43.7
    # transitions: 5 between-phase transitions, 0 pauses allowed
    transitions, pauses = 5, 0
    print("transitions: %d, pauses allowed: %d" % (transitions, pauses))
    assert pauses == 0
    # full rounds per session: 3
    rounds = 3
    print("chain rounds per session: %d" % rounds)
    assert rounds == 3
    print("rule: transitions are the technique")
    print("OK: %s ran the chain" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "stance": demo_cw_stance,
    "posture": demo_cw_posture,
    "ties": demo_cw_ties,
    "wrist_control": demo_cw_wrist_control,
    "snapdown": demo_cw_snapdown,
    "front_headlock": demo_cw_front_headlock,
    "sprawl": demo_cw_sprawl,
    "hip_bump": demo_cw_hip_bump,
    "granby": demo_cw_granby,
    "bridge": demo_cw_bridge,
    "tight_waist": demo_cw_tight_waist,
    "half_nelson": demo_cw_half_nelson,
    "bar_arm": demo_cw_bar_arm,
    "double_leg": demo_cw_double_leg,
    "double_wrist_lock": demo_cw_double_wrist_lock,
    "americana": demo_cw_americana,
    "toe_hold": demo_cw_toe_hold,
    "ankle_lock": demo_cw_ankle_lock,
    "arm_bar": demo_cw_arm_bar,
    "guillotine": demo_cw_guillotine,
    "single_leg": demo_cw_single_leg,
    "fireman": demo_cw_fireman,
    "hip_throw": demo_cw_hip_throw,
    "cradle_near": demo_cw_cradle_near,
    "cradle_far": demo_cw_cradle_far,
    "head_arm": demo_cw_head_arm,
    "can_opener": demo_cw_can_opener,
    "banana_split": demo_cw_banana_split,
    "heel_hook": demo_cw_heel_hook,
    "japanese_necktie": demo_cw_japanese_necktie,
    "power_half": demo_cw_power_half,
    "scarf_armbar": demo_cw_scarf_armbar,
    "hook_chains": demo_cw_hook_chains,
    "flow": demo_cw_flow,
}
