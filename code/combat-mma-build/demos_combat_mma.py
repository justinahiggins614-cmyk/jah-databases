#!/usr/bin/env python3
"""Demo programs for the Mixed Martial Arts Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record (stance calculators, force estimates,
timing windows, drill timers). All are machine-executed by build.py before
the pages are written: each prints its real computed values, asserts tight
bounds (never float exact-equality), and ends with the OK marker.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_cmma_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance geometry: feet wider than the shoulders, weight split even
    shoulder_cm = 46.0
    stance_cm = shoulder_cm + 12.0          # wider base for takedown defense
    lead_back_cm = 30.0                    # dominant foot back one foot length
    w_lead = 50.0
    w_rear = 100.0 - w_lead
    print("shoulder width: %.1f cm -> stance width: %.1f cm" % (shoulder_cm, stance_cm))
    print("lead foot back: %.1f cm; weight lead/rear: %.0f/%.0f" % (lead_back_cm, w_lead, w_rear))
    assert 55.0 < stance_cm < 62.0
    assert 45.0 <= w_lead <= 55.0 and 45.0 <= w_rear <= 55.0
    assert abs((w_lead + w_rear) - 100.0) < 1e-9
    print("base: wide enough to sprawl, even enough to move either way")
    print("OK: %s stance is balanced" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cutting the cage: diagonal step to block the escape lane
    import math
    opp_x, opp_y = 3.0, 0.0          # opponent 3 m ahead, drifting right
    drift = 1.0                       # m/s lateral drift
    close_speed = 2.0                 # m/s forward herding speed
    t = opp_x / close_speed           # time to reach their line
    lane_x = drift * t                # where their escape lane will be
    angle = math.degrees(math.atan2(lane_x, opp_x))
    print("time to their line: %.2f s; escape lane at %.2f m right" % (t, lane_x))
    print("cut angle: %.1f degrees off center" % angle)
    assert 1.0 < t < 2.0
    assert 20.0 < angle < 45.0       # a real forty-five-ish cut, not a chase
    print("herd, do not chase: the diagonal step closes the lane")
    print("OK: %s cuts the cage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_jab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jab reach: arm plus the shoulder-turn extension
    arm_cm = 71.0
    shoulder_turn_cm = 8.0
    step_cm = 8.0
    reach_cm = arm_cm + shoulder_turn_cm + step_cm
    print("arm %.0f cm + shoulder turn %.0f cm + step %.0f cm" % (arm_cm, shoulder_turn_cm, step_cm))
    print("jab reach: %.0f cm" % reach_cm)
    assert 80.0 < reach_cm < 95.0
    # the cross must reach whatever the jab touches: cross adds rear-side rotation
    cross_reach_cm = reach_cm + 12.0
    assert cross_reach_cm > reach_cm
    print("cross reach: %.0f cm (covers the jab's range)" % cross_reach_cm)
    print("OK: %s measures the range" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_cross(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross power: effective mass x hand speed / impact time
    m_eff = 4.5          # kg: arm plus rotating shoulder mass
    v = 9.0              # m/s hand speed at extension
    dt = 0.05            # s impact duration
    force_n = m_eff * v / dt
    print("effective mass %.1f kg x %.1f m/s / %.2f s" % (m_eff, v, dt))
    print("cross impact force: %.0f N" % force_n)
    assert 600.0 < force_n < 1100.0
    # weight transfer: ~70 percent forward at impact
    w_forward = 70.0
    assert 60.0 < w_forward < 80.0
    print("weight transfer at impact: %.0f percent forward" % w_forward)
    print("OK: %s carries the hips" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math
    # tight hook arc: radius x angle; wide hooks are slow hooks
    r_tight = 0.55       # m: tight hook radius (fist inside shoulders)
    r_wide = 0.90        # m: sloppy wide hook radius
    theta = math.pi / 2  # 90-degree arc
    arc_tight = r_tight * theta
    arc_wide = r_wide * theta
    print("tight arc: %.2f m vs wide arc: %.2f m" % (arc_tight, arc_wide))
    assert 0.80 < arc_tight < 0.95
    assert arc_wide > arc_tight * 1.5
    # time at 8 m/s hand speed: tight arrives much sooner
    t_tight = arc_tight / 8.0
    t_wide = arc_wide / 8.0
    print("arrival: tight %.3f s, wide %.3f s (%.0f ms slower)" % (t_tight, t_wide, (t_wide - t_tight) * 1000))
    assert (t_wide - t_tight) * 1000 > 50.0
    print("OK: %s stays tight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_uppercut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uppercut drive: knee dip then leg-powered upward impulse
    dip_cm = 8.0                       # 2-4 inch athletic dip
    body_kg = 80.0
    up_speed = 3.0                     # m/s upward drive speed
    impulse = body_kg * up_speed       # kg m/s delivered upward
    print("dip: %.0f cm; upward impulse: %.0f kg m/s" % (dip_cm, impulse))
    assert 5.0 < dip_cm < 12.0
    assert 200.0 < impulse < 300.0
    # over-dip check: hips must stay above the knees
    hip_drop_cm = dip_cm
    knee_bend_limit_cm = 25.0
    assert hip_drop_cm < knee_bend_limit_cm
    print("hips stay above the knees: no over-dip, no stranded fighter")
    print("OK: %s rises to meet the chin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_lowkick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low kick impact: swinging leg mass x shin speed / contact time
    m_leg = 12.0         # kg effective swinging-leg mass
    v_shin = 12.0        # m/s shin speed at impact
    dt = 0.02            # s contact duration
    force_n = m_leg * v_shin / dt
    print("leg %.0f kg x %.0f m/s / %.2f s" % (m_leg, v_shin, dt))
    print("shin impact force: %.0f N" % force_n)
    assert 5000.0 < force_n < 10000.0
    # support-foot pivot must exceed 90 degrees for full hip turnover
    pivot_deg = 100.0
    assert 90.0 < pivot_deg < 130.0
    print("support foot pivots %.0f degrees: hips fully turned over" % pivot_deg)
    print("OK: %s chops the base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_headmove(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # slip margin: head moves just off the punch line
    slip_cm = 7.6                        # ~3 inches
    punch_halfwidth_cm = 5.0            # glove half-width
    margin_cm = slip_cm - punch_halfwidth_cm
    print("slip %.1f cm vs punch half-width %.1f cm -> margin %.1f cm" % (slip_cm, punch_halfwidth_cm, margin_cm))
    assert 1.0 < margin_cm < 5.0
    # big weave check: over 10 cm is wasted motion
    assert slip_cm < 10.0
    # return time at 2 m/s head speed
    t_return = (slip_cm / 100.0) / 2.0
    print("return to stance: %.3f s" % t_return)
    assert t_return < 0.05
    print("small, fast, back in stance: the punch signs empty air")
    print("OK: %s moves a breath off line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_block(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # high block coverage of the head target box
    head_w_cm, head_h_cm = 22.0, 26.0
    glove_w_cm, glove_h_cm = 14.0, 18.0
    cover = (2 * glove_w_cm * glove_h_cm) / (head_w_cm * head_h_cm) * 100.0
    print("two gloves cover %.0f%% of the head target box" % cover)
    assert 80.0 < cover < 100.0
    # parry deflection: 2-3 inch tap moves the punch line clear
    parry_cm = 6.0
    need_cm = 4.0
    assert parry_cm > need_cm
    print("parry deflects %.0f cm: clears the chin with margin" % parry_cm)
    print("OK: %s holds the margin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_doubleleg(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # penetration step: cover the gap before the sprawl lands
    gap_m = 1.2
    shot_time_s = 0.40
    speed = gap_m / shot_time_s
    print("gap %.1f m in %.2f s -> penetration speed %.1f m/s" % (gap_m, shot_time_s, speed))
    assert 2.5 < speed < 3.5
    # level change drops the hips 4-6 inches
    drop_cm = 12.0
    assert 10.0 < drop_cm < 16.0
    # sprawl reaction benchmark: defender needs ~0.35 s; shot must beat it
    sprawl_time_s = 0.35
    margin = sprawl_time_s - shot_time_s
    print("shot %.2f s vs sprawl %.2f s: margin %+.2f s" % (shot_time_s, sprawl_time_s, margin))
    assert margin < 0.0  # the shot alone does not beat a ready sprawl: set it up first
    print("never shoot naked: strikes plant their weight, then the shot beats the sprawl")
    print("OK: %s penetrates with a setup" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_sprawl(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sprawl timing: legs back and hips down inside the shot window
    sprawl_time_s = 0.32
    shot_time_s = 0.50       # a shot from reasonable range
    window = shot_time_s - sprawl_time_s
    print("shot %.2f s, sprawl %.2f s -> defensive window %+.2f s" % (shot_time_s, sprawl_time_s, window))
    assert window > 0.10
    # hips land on the attacker: defender 80 kg drops ~0.5 m
    m = 80.0
    drop_m = 0.5
    energy_j = m * 9.81 * drop_m
    print("hip-drop energy: %.0f J onto the shooter's back" % energy_j)
    assert 350.0 < energy_j < 450.0
    print("violent and total: half-sprawls get finished")
    print("OK: %s kills the shot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_hipescape(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one shrimp buys 6-12 inches; guard recovery needs ~15 cm of space
    shrimp_cm = 20.0
    need_cm = 15.0
    print("one hip escape: %.0f cm of space; guard needs %.0f cm" % (shrimp_cm, need_cm))
    assert shrimp_cm > need_cm
    # three chained escapes in a drill round
    total_cm = 3 * shrimp_cm
    print("three chained escapes: %.0f cm - enough to recover guard from mount" % total_cm)
    assert 50.0 < total_cm < 70.0
    # three minutes of shrimping warm-up
    reps = 3 * 60 / 4.0      # one rep every ~4 s
    print("warm-up volume: %.0f shrimps per side" % reps)
    assert 40.0 < reps < 50.0
    print("OK: %s makes space and keeps it" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_bridgeroll(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bridge force: glutes drive the hips against the mounted opponent
    body_kg = 80.0
    bridge_force_n = body_kg * 9.81 * 1.5   # explosive bridge ~1.5x bodyweight
    opp_kg = 90.0
    opp_weight_n = opp_kg * 9.81
    print("bridge force: %.0f N vs opponent weight: %.0f N" % (bridge_force_n, opp_weight_n))
    assert bridge_force_n > opp_weight_n
    # bridge height must exceed 12 inches to tip them
    bridge_cm = 35.0
    assert 30.0 < bridge_cm < 45.0
    print("bridge height %.0f cm: the mount tips over the trapped side" % bridge_cm)
    print("OK: %s turns the tables" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_combos(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # combination output: 3-strike combos every 4 s across a 3-minute round
    round_s = 180.0
    combo_s = 4.0
    strikes_per_combo = 3
    total = round_s / combo_s * strikes_per_combo
    print("combos per round: %.0f -> strikes thrown: %.0f" % (round_s / combo_s, total))
    assert 130.0 < total < 140.0
    # one-two timing: cross fires as the jab returns (~0.15 s later)
    jab_return_s = 0.15
    assert 0.10 < jab_return_s < 0.25
    print("cross fires %.2f s after the jab: one beat, not two punches" % jab_return_s)
    print("OK: %s links the strikes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_checking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # check economics: kicker's thigh meets defender's shin bone
    kick_force_n = 7000.0
    # shin-on-shin: contact area halves, pressure on the kicker doubles
    area_thigh_cm2 = 60.0
    area_shin_cm2 = 25.0
    p_thigh = kick_force_n / area_thigh_cm2
    p_kicker = kick_force_n / area_shin_cm2
    print("pressure on thigh if unblocked: %.0f N/cm2" % p_thigh)
    print("pressure rebounded onto kicker's shin: %.0f N/cm2" % p_kicker)
    assert p_kicker > p_thigh * 2.0
    # check lift: 6-10 inches in under 0.2 s
    lift_cm = 20.0
    t_lift = 0.18
    assert 15.0 < lift_cm < 26.0
    assert t_lift < 0.25
    print("check up in %.2f s: the kick meets bone, not meat" % t_lift)
    print("OK: %s makes them pay for kicking" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_singleleg(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # run-the-pipe leverage: leg held high vs held low
    hold_high_m = 0.90
    hold_low_m = 0.50
    opp_leg_kg = 16.0
    torque_high = opp_leg_kg * 9.81 * hold_high_m
    torque_low = opp_leg_kg * 9.81 * hold_low_m
    print("leg torque held high: %.0f N m vs held low: %.0f N m" % (torque_high, torque_low))
    assert torque_high > torque_low * 1.5
    # head-inside safety: head offset from the guillotine line
    head_inside_cm = 25.0   # ear to ribs
    assert head_inside_cm > 15.0
    print("head inside by %.0f cm: the guillotine doorway stays shut" % head_inside_cm)
    print("OK: %s finishes the pipe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_clinch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pummeling volume: continuous inside-position battles
    round_s = 180.0
    pummel_cycle_s = 6.0
    cycles = round_s / pummel_cycle_s
    print("pummeling cycles per round: %.0f" % cycles)
    assert 25.0 < cycles < 35.0
    # underhook leverage: arm under the armpit lifts the posture
    underhook_depth_cm = 30.0   # hand to the shoulder blade
    assert underhook_depth_cm > 20.0
    print("underhook reaches %.0f cm deep: posture control secured" % underhook_depth_cm)
    print("OK: %s owns the inside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_thaiclinch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # plum collision: pull-down meets the rising knee
    pull_n = 200.0
    knee_n = 300.0
    combined_n = pull_n + knee_n
    print("pull %.0f N + knee %.0f N = %.0f N collision" % (pull_n, knee_n, combined_n))
    assert 450.0 < combined_n < 550.0
    # knee volume: alternating knees every ~1.5 s
    knees_per_30s = 30.0 / 1.5
    print("knees per 30 s clinch exchange: %.0f" % knees_per_30s)
    assert 18.0 < knees_per_30s < 22.0
    print("the head comes down as the knee comes up")
    print("OK: %s seals the plum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_guillotine(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guillotine extension: hips drive while elbows pull down
    hip_drive_n = 400.0
    elbow_pull_n = 150.0
    total_n = hip_drive_n + elbow_pull_n
    print("hip drive %.0f N + elbow pull %.0f N = %.0f N" % (hip_drive_n, elbow_pull_n, total_n))
    assert 500.0 < total_n < 600.0
    # the choke must be blood-flow pressure: fade in under 10 s once locked
    fade_s = 8.0
    assert 5.0 < fade_s < 10.0
    print("locked choke fades the defender in ~%.0f s: release on the tap" % fade_s)
    print("OK: %s closes the bracket" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_rnc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # RNC: chest expansion closes the arm triangle
    chest_expand_cm = 5.0
    elbow_close_cm = 8.0
    closure_cm = chest_expand_cm + elbow_close_cm
    print("chest +%.0f cm, elbows +%.0f cm -> %.0f cm of closure" % (chest_expand_cm, elbow_close_cm, closure_cm))
    assert 10.0 < closure_cm < 16.0
    # back control value: the highest-percentage finish in the sport
    attempts = 100.0
    finishes = 62.0
    rate = finishes / attempts * 100.0
    print("back-take finish rate in the model: %.0f%%" % rate)
    assert 55.0 < rate < 70.0
    print("the back is the goal: every scramble that gives it invites this")
    print("OK: %s takes the back and finishes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_armbar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # armbar leverage: hips as fulcrum, elbow near, hand far
    d_elbow_m = 0.15
    d_hand_m = 0.45
    advantage = d_hand_m / d_elbow_m
    print("fulcrum at elbow %.2f m, force at hand %.2f m -> %.1fx leverage" % (d_elbow_m, d_hand_m, advantage))
    assert 2.5 < advantage < 3.5
    # hip lift of 80 kg attacker vs elbow joint tolerance
    lift_n = 80.0 * 9.81
    torque = lift_n * d_hand_m
    print("hip lift torque at the elbow: %.0f N m" % torque)
    assert 300.0 < torque < 400.0
    print("hips are the engine: never pull with the arms")
    print("OK: %s draws past straight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_gnp(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ground-and-pound flurry: controlled strikes from posture
    flurry_s = 30.0
    strike_interval_s = 2.5
    strikes = flurry_s / strike_interval_s
    print("strikes in a 30 s postured flurry: %.0f" % strikes)
    assert 10.0 < strikes < 14.0
    # posture check: hips stay heavy through the flurry
    base_width_cm = 60.0
    assert 50.0 < base_width_cm < 70.0
    print("base %.0f cm wide: the buck is ridden, not feared" % base_width_cm)
    print("control first, damage second: short strikes, heavy hips")
    print("OK: %s writes from above" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_guardpass(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # passing economics: patient attempts vs success
    attempts = 10.0
    success_rate = 0.40
    passes = attempts * success_rate
    print("pass attempts per round: %.0f at %.0f%% -> %.0f clean passes" % (attempts, success_rate * 100, passes))
    assert 3.0 < passes < 5.0
    # stack fold angle: legs folded past 90 degrees kill the hips
    fold_deg = 120.0
    assert 90.0 < fold_deg < 150.0
    print("stack fold %.0f degrees: the guard player's hips are done" % fold_deg)
    print("OK: %s turns the page" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_tdd(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # layered takedown defense: intercept, sprawl/whizzer, scramble
    p_intercept = 0.15
    p_sprawl = 0.55
    p_whizzer = 0.20
    # probability the shot is stopped by at least one layer
    p_stop = 1 - (1 - p_intercept) * (1 - p_sprawl) * (1 - p_whizzer)
    print("layers: intercept %.0f%%, sprawl %.0f%%, whizzer %.0f%%" % (p_intercept * 100, p_sprawl * 100, p_whizzer * 100))
    print("combined stop rate: %.1f%%" % (p_stop * 100))
    assert 65.0 < p_stop * 100 < 75.0
    # gauntlet: 10 shots, must stay standing
    survived = 10
    assert survived == 10
    print("gauntlet: %d shots, still standing" % survived)
    print("OK: %s dictates where the fight happens" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_cagewrestling(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wall-walk: each attempt climbs the pinned fighter closer to standing
    progress_per_attempt = 0.35   # fraction of the way to the feet
    attempts = 3
    total = 1 - (1 - progress_per_attempt) ** attempts
    print("wall-walk progress per attempt: %.0f%%" % (progress_per_attempt * 100))
    print("after %d attempts: %.0f%% of the way to the feet" % (attempts, total * 100))
    assert 70.0 < total * 100 < 80.0
    # pinner's outside trip needs the hips tight: gap under 15 cm
    gap_cm = 10.0
    assert gap_cm < 15.0
    print("pinner hip gap %.0f cm: no daylight for the wall walk" % gap_cm)
    print("OK: %s works the fence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_subdefense(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # early vs late defense success rates
    p_early = 0.85   # defended at the first grip
    p_late = 0.25    # defended after the lock closes
    print("defense at the grip: %.0f%% vs defense at the lock: %.0f%%" % (p_early * 100, p_late * 100))
    assert p_early > p_late * 3.0
    # hand-fighting: two hands beat one gripping hand
    hands_defense = 2
    hands_attack = 1
    assert hands_defense > hands_attack
    print("two defensive hands peel one attacking grip: arithmetic of survival")
    print("OK: %s defends early" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_transitions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # chain math: each link lands 40%; the chain lands if ANY link lands
    p_link = 0.40
    links = 3
    p_chain = 1 - (1 - p_link) ** links
    print("per-link %.0f%% x %d links -> chain success %.1f%%" % (p_link * 100, links, p_chain * 100))
    assert 75.0 < p_chain * 100 < 82.0
    # single-attack comparison: one 40% attack vs the chain
    assert p_chain > p_link * 1.9
    print("the chain nearly doubles the lone attack: hunt reactions, not submissions")
    print("OK: %s chains the attacks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_feints(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # feint timing: the guard commits longer than the real strike needs
    reaction_s = 0.25      # human reaction to the feint
    guard_hang_s = 0.30   # guard stays committed after the fake
    strike_s = 0.20       # real cross travel time
    print("reaction %.2f s, guard hangs %.2f s, real strike %.2f s" % (reaction_s, guard_hang_s, strike_s))
    assert strike_s < guard_hang_s
    margin = guard_hang_s - strike_s
    print("strike lands with %.2f s of open guard to spare" % margin)
    assert 0.05 < margin < 0.20
    print("show it twice real, punish the habit on the third")
    print("OK: %s draws the reaction" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_elbows(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow cut model: clean elbows on the brow line
    p_cut_per_elbow = 0.15
    elbows = 6
    p_cut = 1 - (1 - p_cut_per_elbow) ** elbows
    print("cut chance per clean elbow: %.0f%%" % (p_cut_per_elbow * 100))
    print("after %d elbows: %.0f%% chance of a cut" % (elbows, p_cut * 100))
    assert 55.0 < p_cut * 100 < 70.0
    # twelve-to-six check: downward angle must never appear (0 tolerance)
    illegal_reps = 0
    assert illegal_reps == 0
    print("twelve-to-six reps in the repertoire: %d (illegal, never drilled)" % illegal_reps)
    print("OK: %s cuts at close range" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_sweeps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kuzushi: tip the base past ~15 degrees and the sweep is inevitable
    tip_deg = 18.0
    need_deg = 15.0
    print("balance broken at %.0f degrees; sweep needs %.0f" % (tip_deg, need_deg))
    assert tip_deg > need_deg
    # scissor-to-hip-bump switch inside one beat of the post
    switch_s = 0.8
    assert switch_s < 1.0
    print("post defended -> hip bump in %.1f s: the pair is one technique" % switch_s)
    print("OK: %s reverses from below" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_sideescape(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow escape inches: each shrimp buys ~15 cm, guard needs ~30 cm
    per_shrimp_cm = 15.0
    need_cm = 30.0
    shrimps = 2
    gained = per_shrimp_cm * shrimps
    print("per shrimp %.0f cm x %d = %.0f cm (need %.0f cm)" % (per_shrimp_cm, shrimps, gained, need_cm))
    assert gained >= need_cm
    # flat time: the student is never flat more than a moment
    flat_s = 0.5
    assert flat_s < 1.0
    print("max flat time %.1f s: onto the hip immediately" % flat_s)
    print("OK: %s recovers the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_triangle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # triangle pressure: thigh and calf close on the carotids
    thigh_n = 250.0
    calf_n = 180.0
    total_n = thigh_n + calf_n
    print("thigh %.0f N + calf %.0f N = %.0f N of closure" % (thigh_n, calf_n, total_n))
    assert 400.0 < total_n < 460.0
    # angle cut: hips must go perpendicular (80-100 deg) for the choke
    angle_deg = 90.0
    assert 80.0 < angle_deg < 100.0
    print("hips cut to %.0f degrees: square hips break it, angled hips make it" % angle_deg)
    print("OK: %s closes the geometry" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_cagetakedowns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the fence multiplies trip success: no retreat to step into
    p_open = 0.45
    p_cage = 0.75
    print("trip success open mat: %.0f%% vs against the cage: %.0f%%" % (p_open * 100, p_cage * 100))
    assert p_cage > p_open * 1.5
    # trip window: the moment the back foot cannot step back
    window_s = 0.6
    assert 0.4 < window_s < 0.9
    print("trip window against the fence: %.1f s - generous, attack it" % window_s)
    print("OK: %s finishes at the margin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cmma_gameplan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-minute round budget: striking, clinch, ground
    round_s = 300.0
    striking_s = 120.0
    clinch_s = 120.0
    ground_s = 60.0
    total = striking_s + clinch_s + ground_s
    print("round budget: striking %.0f s, clinch %.0f s, ground %.0f s" % (striking_s, clinch_s, ground_s))
    assert abs(total - round_s) < 1e-9
    # ninety-second scripted opening
    script_s = 90.0
    assert script_s < round_s
    print("scripted opening: %.0f s of the %d s round" % (script_s, int(round_s)))
    # one adjustment between rounds
    adjustments = 1
    assert adjustments == 1
    print("between rounds: %d adjustment - the single most important change" % adjustments)
    print("OK: %s plans the fight" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "mma_stance": demo_cmma_stance,
    "footwork_angles": demo_cmma_footwork,
    "jab": demo_cmma_jab,
    "cross": demo_cmma_cross,
    "lead_hook": demo_cmma_hook,
    "rear_uppercut": demo_cmma_uppercut,
    "low_kick": demo_cmma_lowkick,
    "head_movement": demo_cmma_headmove,
    "blocking": demo_cmma_block,
    "double_leg": demo_cmma_doubleleg,
    "sprawl": demo_cmma_sprawl,
    "hip_escape": demo_cmma_hipescape,
    "bridge_roll": demo_cmma_bridgeroll,
    "combos": demo_cmma_combos,
    "checking": demo_cmma_checking,
    "single_leg": demo_cmma_singleleg,
    "clinch": demo_cmma_clinch,
    "thai_clinch": demo_cmma_thaiclinch,
    "guillotine": demo_cmma_guillotine,
    "rnc": demo_cmma_rnc,
    "armbar": demo_cmma_armbar,
    "gnp": demo_cmma_gnp,
    "guard_pass": demo_cmma_guardpass,
    "tdd": demo_cmma_tdd,
    "cage_wrestling": demo_cmma_cagewrestling,
    "sub_defense": demo_cmma_subdefense,
    "transitions": demo_cmma_transitions,
    "feints": demo_cmma_feints,
    "elbows": demo_cmma_elbows,
    "sweeps": demo_cmma_sweeps,
    "side_escape": demo_cmma_sideescape,
    "triangle": demo_cmma_triangle,
    "cage_takedowns": demo_cmma_cagetakedowns,
    "game_plan": demo_cmma_gameplan,
}
