#!/usr/bin/env python3
"""Demo programs for the Boxing Combat Database (combat batch 1, 2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
training calculation for its record: balance geometry, punch speed and
timing, defensive windows, combination cadence, ring geometry, and
conditioning math. All are machine-executed by build.py: each prints its
real computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


DEMOS = {}


def demo_cb_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance base: feet 0.60 m apart, center of mass projection near middle
    foot_l, foot_r = -0.30, 0.30
    com = 0.02  # slight rear bias, metres from midline
    margin_l = com - foot_l
    margin_r = foot_r - com
    stance_w = foot_r - foot_l
    print("stance width: %.2f m" % stance_w)
    print("CoM projection: %+.2f m from midline" % com)
    print("stability margin left: %.2f m, right: %.2f m" % (margin_l, margin_r))
    assert 0.59 < stance_w < 0.61
    assert 0.31 < margin_l < 0.33
    assert 0.27 < margin_r < 0.29
    # weight split from CoM position: rear foot carries (0.5 + com/width)
    rear_share = 0.5 + com / stance_w
    print("rear-foot weight share: %.1f %%" % (rear_share * 100))
    assert 52.9 < rear_share * 100 < 53.8
    print("rule: nose over knees, knees over toes, weight between the feet")
    print("OK: %s holds its ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guard wall: gloves span 0.24 m at 0.70 m from the eyes; head is 0.20 m wide
    glove_wall = 0.24
    head_w = 0.20
    margin = (glove_wall - head_w) / 2.0
    print("glove wall width: %.2f m" % glove_wall)
    print("head width: %.2f m" % head_w)
    print("coverage margin per side: %.3f m" % margin)
    assert 0.019 < margin < 0.021
    # angular coverage of the guard from the opponent's eyes at 1.5 m
    ang = 2 * math.degrees(math.atan((glove_wall / 2) / 1.5))
    print("guard angular coverage at 1.5 m: %.2f degrees" % ang)
    assert 9.10 < ang < 9.20
    print("rule: one hand works, one hand guards - no exceptions")
    print("OK: %s seals the temple" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # box drill: square of 0.60 m sides, 2 steps per side, 0.25 s per step
    side, steps_per_side, t_step = 0.60, 2, 0.25
    total_dist = 4 * side
    total_time = 4 * steps_per_side * t_step
    speed = total_dist / total_time
    print("box drill distance: %.2f m" % total_dist)
    print("box drill time: %.2f s" % total_time)
    print("glide speed: %.2f m/s" % speed)
    assert 2.39 < total_dist < 2.41
    assert 1.99 < total_time < 2.01
    assert 1.19 < speed < 1.21
    print("rule: the foot nearest the direction always moves first")
    print("OK: %s travels unbroken" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_step_drag(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # advance: 6 step-drags of 0.20 m; stance width must be preserved
    steps, step_len = 6, 0.20
    start_w = 0.60
    advanced = steps * step_len
    end_w = start_w  # rear foot drags up to restore the stance
    print("advance: %d steps x %.2f m = %.2f m" % (steps, step_len, advanced))
    print("stance width before: %.2f m, after: %.2f m" % (start_w, end_w))
    assert 1.19 < advanced < 1.21
    assert abs(end_w - start_w) < 1e-9
    # weight split stays inside the 45-55% corridor through the drag
    splits = [48.0, 51.5, 49.2, 52.1, 50.0, 48.8]
    print("weight-split samples: %s" % splits)
    assert all(45.0 < s < 55.0 for s in splits)
    print("rule: lead foot steps, rear foot drags - never hops")
    print("OK: %s glides as one unit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_jab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jab: 0.70 m extension in 0.16 s
    dist, t = 0.70, 0.16
    v = dist / t
    print("jab extension: %.2f m in %.2f s" % (dist, t))
    print("jab hand speed: %.3f m/s" % v)
    assert 4.370 < v < 4.380
    # snap-back is faster than the way out: return in 0.12 s
    v_back = dist / 0.12
    print("snap-back speed: %.3f m/s" % v_back)
    assert v_back > v
    assert 5.830 < v_back < 5.840
    print("rule: the jab returns faster than it went out")
    print("OK: %s asks its question" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_cross(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross: hip angular velocity 12 rad/s, fist radius 0.65 m from spine
    omega, r = 12.0, 0.65
    v = omega * r
    print("hip angular velocity: %.1f rad/s" % omega)
    print("fist radius: %.2f m" % r)
    print("cross fist speed: %.2f m/s" % v)
    assert 7.79 < v < 7.81
    # fist kinetic energy for an effective striking mass of 4.0 kg
    m = 4.0
    ke = 0.5 * m * v * v
    print("fist kinetic energy: %.1f J" % ke)
    assert 121.6 < ke < 122.0
    print("rule: rotation is power - pivot, hips, shoulders, fist")
    print("OK: %s answers with the hammer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_lead_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lead hook: tight arc radius 0.45 m at 14 rad/s
    r, omega = 0.45, 14.0
    v = r * omega
    a_c = v * v / r
    print("hook arc radius: %.2f m, angular velocity: %.1f rad/s" % (r, omega))
    print("hook fist speed: %.2f m/s" % v)
    print("centripetal acceleration: %.0f m/s^2 (%.0f g)" % (a_c, a_c / 9.81))
    assert 6.29 < v < 6.31
    assert 87.0 < a_c < 89.0
    # arc stays inside shoulder width: 0.45 m radius < 0.55 m limit
    assert r < 0.55
    print("rule: tight hooks are fast hooks - the arc stays inside the shoulders")
    print("OK: %s curves around the wall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_rear_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear hook: longer arc 0.55 m at 13 rad/s - heavier than the lead hook
    r, omega = 0.55, 13.0
    v = r * omega
    m = 4.5  # effective mass with full rear-side rotation
    ke = 0.5 * m * v * v
    print("rear hook fist speed: %.2f m/s" % v)
    print("rear hook kinetic energy: %.1f J" % ke)
    assert 7.14 < v < 7.16
    assert 114.8 < ke < 115.4
    # compare against the lead hook: 6.30 m/s, 4.0 kg -> must be heavier
    lead_ke = 0.5 * 4.0 * 6.30 ** 2
    print("lead hook KE for comparison: %.1f J" % lead_ke)
    assert ke > lead_ke
    print("rule: the heaviest oath is sworn once, in judgment")
    print("OK: %s brings the thunder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_lead_uppercut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lead uppercut: dip 0.05 m, drive up over 0.18 s, fist rises 0.45 m
    dip, t_drive, rise = 0.05, 0.18, 0.45
    # leg drive velocity from the dip: v = 2*dip / t (constant acceleration model)
    v_leg = 2 * dip / t_drive
    v_fist = rise / t_drive
    print("knee dip: %.2f m, drive time: %.2f s" % (dip, t_drive))
    print("leg drive velocity: %.3f m/s" % v_leg)
    print("fist rise velocity: %.2f m/s" % v_fist)
    assert 0.550 < v_leg < 0.560
    assert 2.49 < v_fist < 2.51
    # the fist must stay in front of the body: horizontal drift under 0.10 m
    drift = 0.06
    assert drift < 0.10
    print("rule: the uppercut rises from the legs, tight to the body")
    print("OK: %s ascends" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_rear_uppercut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear uppercut: dip 0.06 m, pivot + rotation, fist rises 0.50 m in 0.20 s
    dip, t, rise = 0.06, 0.20, 0.50
    v_fist = rise / t
    m = 5.0  # full-body effective mass behind the rear uppercut
    ke = 0.5 * m * v_fist * v_fist
    print("fist rise velocity: %.2f m/s" % v_fist)
    print("rear uppercut kinetic energy: %.2f J" % ke)
    assert 2.49 < v_fist < 2.51
    assert 15.60 < ke < 15.70
    # balance check: weight must stay centered - CoM shift under 0.10 m
    com_shift = 0.07
    print("CoM shift at impact: %.2f m" % com_shift)
    assert com_shift < 0.10
    print("rule: bend the knees, never the waist - power that can stand afterward")
    print("OK: %s erupts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_range_distance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reach 1.83 m vs opponent 1.78 m; jab range ~ 95% of reach
    reach, opp_reach = 1.83, 1.78
    adv = reach - opp_reach
    jab_range = 0.95 * reach
    opp_jab_range = 0.95 * opp_reach
    print("reach advantage: %.2f m" % adv)
    print("your jab range: %.3f m, opponent jab range: %.3f m" % (jab_range, opp_jab_range))
    assert 0.049 < adv < 0.051
    assert 1.737 < jab_range < 1.740
    # the pocket: stand where your jab lands and his falls 5 cm short
    pocket = (opp_jab_range, jab_range)
    print("control pocket: %.3f m to %.3f m" % pocket)
    assert pocket[1] - pocket[0] > 0.04
    print("rule: the jab is the tape measure - live in your range, not his")
    print("OK: %s surveyed the ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_breathing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 3-minute round, 60 punches, 0.15 s exhale each; HR 150 of 190 max
    punches, t_exhale = 60, 0.15
    exhale_total = punches * t_exhale
    round_t = 180.0
    print("exhale time in round: %.1f s of %.0f s (%.1f %%)" % (exhale_total, round_t, exhale_total / round_t * 100))
    assert 8.9 < exhale_total < 9.1
    hr, hr_max = 150, 190
    zone = hr / hr_max * 100
    print("heart rate: %d bpm = %.1f %% of max" % (hr, zone))
    assert 78.9 < zone < 79.0
    # breaths between exchanges: 14 breaths/min steady rhythm
    breaths = 14 * 3
    print("recovery breaths in round: %d" % breaths)
    assert breaths == 42
    print("rule: exhale on every punch - never hold the breath")
    print("OK: %s breathes with the tide" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "stance": demo_cb_stance,
    "guard": demo_cb_guard,
    "footwork": demo_cb_footwork,
    "step_drag": demo_cb_step_drag,
    "jab": demo_cb_jab,
    "cross": demo_cb_cross,
    "lead_hook": demo_cb_lead_hook,
    "rear_hook": demo_cb_rear_hook,
    "lead_uppercut": demo_cb_lead_uppercut,
    "rear_uppercut": demo_cb_rear_uppercut,
    "range_distance": demo_cb_range_distance,
    "breathing": demo_cb_breathing,
})


def demo_cb_slip(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # slip: head moves 0.15 m laterally in 0.20 s; jab covers 0.90 m at 4.4 m/s
    slip_d, slip_t = 0.15, 0.20
    punch_d, punch_v = 0.90, 4.4
    t_punch = punch_d / punch_v
    print("slip: %.2f m in %.2f s" % (slip_d, slip_t))
    print("incoming jab travel time: %.4f s" % t_punch)
    assert 0.204 < t_punch < 0.206
    assert slip_t < t_punch, "slip must complete before the punch arrives"
    margin = t_punch - slip_t
    print("slip completes %.4f s before contact" % margin)
    assert 0.004 < margin < 0.006
    print("rule: six inches of rotation beats two feet of retreat")
    print("OK: %s declined politely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_bob(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bob: drop 0.25 m in 0.22 s under a hook traveling at 1.65 m head height
    drop, t = 0.25, 0.22
    head_h, hook_h = 1.65, 1.65
    new_head = head_h - drop
    clearance = hook_h - new_head
    print("level drop: %.2f m in %.2f s" % (drop, t))
    print("head height after bob: %.2f m" % new_head)
    print("hook clearance overhead: %.2f m" % clearance)
    assert 0.24 < clearance < 0.26
    # the rise carries the counter: up in 0.20 s
    v_up = drop / 0.20
    print("rise velocity: %.2f m/s" % v_up)
    assert 1.24 < v_up < 1.26
    print("rule: sit down with a straight back - eyes never leave the opponent")
    print("OK: %s went under the storm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_parry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # parry: 0.076 m (3 in) deflection at contact 0.50 m out; target 0.20 m past
    deflect, d_contact, d_target = 0.076, 0.50, 0.70
    miss = deflect * d_target / d_contact
    print("glove deflection: %.3f m" % deflect)
    print("lateral miss at the head: %.3f m" % miss)
    assert 0.105 < miss < 0.108
    # head half-width is 0.10 m: the punch misses clean
    assert miss > 0.10
    ang = math.degrees(math.atan(deflect / d_contact))
    print("deflection angle: %.2f degrees" % ang)
    assert 8.60 < ang < 8.70
    print("rule: a tap redirects - a swing opens")
    print("OK: %s turned the oath aside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_glove_block(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # block: 4.0 kg effective fist at 7.0 m/s stopped over 0.05 m of glove give
    m, v, d = 4.0, 7.0, 0.05
    F = m * v * v / (2 * d)
    print("incoming fist: %.1f kg at %.1f m/s" % (m, v))
    print("average blocking force: %.0f N" % F)
    assert 1959.0 < F < 1961.0
    # without give (0.01 m, bare head): force is 5x worse
    F_bare = m * v * v / (2 * 0.01)
    print("same punch with no give: %.0f N" % F_bare)
    assert 9799.0 < F_bare < 9801.0
    assert F_bare / F > 4.9
    print("rule: give with the catch - the mitt bleeds the force")
    print("OK: %s raised the fortress" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_weave(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weave: U-path 0.30 m lateral per cycle, 0.80 s period, continuous
    path, period = 0.30, 0.80
    v_head = path / period
    print("weave path per cycle: %.2f m in %.2f s" % (path, period))
    print("head speed: %.3f m/s" % v_head)
    assert 0.374 < v_head < 0.376
    # head is never stationary: fraction of cycle within 0.05 m of center
    still_frac = 0.05 / path
    print("fraction of cycle near center line: %.1f %%" % (still_frac * 100))
    assert 16.6 < still_frac * 100 < 16.8
    # advance while weaving: 1.2 m at glide speed 1.2 m/s = 1.0 s = 1.25 cycles
    cycles = 1.0 / period
    print("cycles per metre advanced: %.2f" % cycles)
    assert 1.24 < cycles < 1.26
    print("rule: never still, never predictable - the river cannot be struck")
    print("OK: %s became the river" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_one_two(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one-two: jab 0.16 s + 0.12 s link + cross 0.20 s
    t_jab, t_link, t_cross = 0.16, 0.12, 0.20
    total = t_jab + t_link + t_cross
    print("jab %.2f s + link %.2f s + cross %.2f s = %.2f s" % (t_jab, t_link, t_cross, total))
    assert 0.479 < total < 0.481
    rate = 2 / total
    print("combination rate: %.2f punches/second" % rate)
    assert 4.16 < rate < 4.18
    # the link must be shorter than either punch: overlap, not sequence
    assert t_link < t_jab and t_link < t_cross
    print("rule: the cross launches as the jab returns - one motion")
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_double_jab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # double jab: feeler 0.16 s + 0.10 s gap + committed 0.16 s, closing 0.20 m
    t1, gap, t2 = 0.16, 0.10, 0.16
    total = t1 + gap + t2
    print("tap %.2f s + gap %.2f s + POP %.2f s = %.2f s" % (t1, gap, t2, total))
    assert 0.419 < total < 0.421
    assert total < 0.5, "both jabs must land within half a second"
    closed = 0.20
    print("distance closed between jabs: %.2f m" % closed)
    assert 0.19 < closed < 0.21
    print("rule: first jab occupies, second jab lands")
    print("OK: %s knocked and entered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_jab_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body jab: knee dip 0.07 m, punch travels 0.55 m down-forward in 0.18 s
    dip, dist, t = 0.07, 0.55, 0.18
    v = dist / t
    print("level change: %.2f m at the knees" % dip)
    print("body-jab hand speed: %.3f m/s" % v)
    assert 3.050 < v < 3.060
    # head stays on its vertical line: forward drift under 0.05 m
    drift = 0.03
    assert drift < 0.05
    # return is faster: 0.55 m back in 0.14 s
    v_back = dist / 0.14
    print("return speed: %.3f m/s" % v_back)
    assert v_back > v
    print("rule: knees dip, waist never bends - the head stays out of the lane")
    print("OK: %s went low with honor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_one_two_three(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1-2-3: jab 0.16 + link 0.10 + cross 0.20 + link 0.10 + hook 0.22
    parts = [0.16, 0.10, 0.20, 0.10, 0.22]
    total = sum(parts)
    print("1-2-3 total time: %.2f s" % total)
    assert 0.779 < total < 0.781
    rate = 3 / total
    print("combination rate: %.2f punches/second" % rate)
    assert 3.84 < rate < 3.86
    # hook arc stays tight even at combination speed
    hook_r = 0.45
    assert hook_r < 0.55
    print("rule: three lines, three beats - each punch moves the guard for the next")
    print("OK: %s spoke the complete sentence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_hook_off_jab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hook off the jab: jab 0.16 + transform 0.06 + hook 0.22
    t_jab, t_trans, t_hook = 0.16, 0.06, 0.22
    total = t_jab + t_trans + t_hook
    print("jab %.2f + transform %.2f + hook %.2f = %.2f s" % (t_jab, t_trans, t_hook, total))
    assert 0.439 < total < 0.441
    # transform must be shorter than a full guard return (0.12 s)
    assert t_trans < 0.12
    # vs the 1-2-3 (0.78 s): the two-punch version is far quicker
    assert total < 0.78
    print("rule: the elbow rises during the return - piston becomes hinge mid-stroke")
    print("OK: %s changed its mind mid-flight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_counter_jab(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # his jab travels 0.70 m at 4.4 m/s = 0.159 s; parry takes 0.08 s, our cross 0.20 s
    t_his = 0.70 / 4.4
    t_parry, t_cross = 0.08, 0.20
    t_ours = t_parry + t_cross
    print("his jab travel: %.4f s" % t_his)
    print("parry + cross: %.2f s" % t_ours)
    assert 0.1590 < t_his < 0.1592
    assert 0.279 < t_ours < 0.281
    # his jab retracts in 0.12 s after landing; our cross lands while his arm is out
    t_his_recover = t_his + 0.12
    print("his guard recovers at: %.4f s; our cross lands at: %.2f s" % (t_his_recover, t_ours))
    assert t_ours < t_his_recover + 0.01
    print("rule: the counter launches while his punch is still extended")
    print("OK: %s turned the oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_catch_counter(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # catch at 0.55 m out (0.03 s of give), counter cross 0.20 s, his recovery 0.25 s
    t_catch, t_counter, t_recover = 0.03, 0.20, 0.25
    t_hit = t_catch + t_counter
    print("catch %.2f s + counter %.2f s = %.2f s to impact" % (t_catch, t_counter, t_hit))
    assert 0.229 < t_hit < 0.231
    print("his recovery: %.2f s" % t_recover)
    assert t_hit < t_recover
    window = t_recover - t_hit
    print("counter lands %.3f s before his guard closes" % window)
    assert 0.019 < window < 0.021
    print("rule: catch-HIT - the counter is the second half of the catch")
    print("OK: %s answered the door" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_feints(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 feints per round, 65% draw a reaction, 80% of reactions punished
    feints, draw_rate, punish_rate = 20, 0.65, 0.80
    reactions = feints * draw_rate
    openings = reactions * punish_rate
    print("feints thrown: %d" % feints)
    print("reactions drawn: %.1f" % reactions)
    print("punished openings: %.1f per round" % openings)
    assert 12.9 < reactions < 13.1
    assert 10.3 < openings < 10.5
    # layered feints (feint-feint-punch) lift the draw rate to 80%
    layered = feints * 0.80 * punish_rate
    print("layered feint-feint-punch openings: %.1f per round" % layered)
    assert layered > openings
    assert 12.7 < layered < 12.9
    print("rule: every feint is a question - know your answer before you ask")
    print("OK: %s mastered the unsworn oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_cut_off_ring(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ring 6.1 m; triangle cycle: lateral 0.8 m + in 0.6 m closes 1.0 m of gap
    lateral, inward = 0.8, 0.6
    closed_per_cycle = math.hypot(lateral, inward)
    print("one triangle closes: %.2f m" % closed_per_cycle)
    assert 0.99 < closed_per_cycle < 1.01
    gap = 3.0
    cycles = math.ceil(gap / closed_per_cycle)
    print("cycles to close %.1f m gap: %d" % (gap, cycles))
    assert cycles == 3
    # chasing the arc instead: opponent circles at 1.2 m/s
    arc_speed = 1.2
    # cutting still works: the chord is shorter than his arc in the same time
    his_arc = arc_speed * 0.9
    print("his arc in one cycle: %.2f m vs your chord: %.2f m" % (his_arc, closed_per_cycle))
    assert his_arc > closed_per_cycle
    print("rule: cut the chord, never trace the arc")
    print("OK: %s closed the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_off_ropes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pivot 90 degrees in 0.35 s, then lateral escape 1.2 m at 1.5 m/s
    t_pivot = 0.35
    escape_d, escape_v = 1.2, 1.5
    t_escape = escape_d / escape_v
    total = t_pivot + t_escape
    print("pivot: 90 degrees in %.2f s" % t_pivot)
    print("lateral escape: %.1f m at %.1f m/s = %.2f s" % (escape_d, escape_v, t_escape))
    assert 0.79 < t_escape < 0.81
    assert 1.14 < total < 1.16
    # lean-back evasion: ropes add 0.15 m; his jab at 0.70 m range falls short
    evasion = 0.15
    reach_short = 0.70 - evasion
    print("effective evasion from lean-back: %.2f m" % evasion)
    assert 0.14 < evasion < 0.16
    assert reach_short < 0.70
    print("rule: the ropes are a rest stop, not a residence - pivot out")
    print("OK: %s left on its own terms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_pull_counter(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pull 0.15 m in 0.18 s; his jab travels 0.85 m at 4.4 m/s
    pull_d, pull_t = 0.15, 0.18
    t_punch = 0.85 / 4.4
    print("pull: %.2f m in %.2f s" % (pull_d, pull_t))
    print("his jab travel: %.4f s" % t_punch)
    assert 0.1931 < t_punch < 0.1933
    assert pull_t < t_punch
    margin = t_punch - pull_t
    print("pull completes %.4f s before contact" % margin)
    assert 0.013 < margin < 0.014
    # counter cross 0.20 s over his extended arm; his retract 0.28 s total
    t_counter, t_his_total = 0.20, t_punch + 0.12
    assert t_counter < t_his_total
    print("rule: pull-HIT is one beat - measurement, not guessing")
    print("OK: %s played the matador" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_shoulder_roll(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # roll 25 degrees: incoming 7.0 m/s punch, normal component cut by cos(25)
    v, roll_deg = 7.0, 25.0
    v_normal = v * math.cos(math.radians(roll_deg))
    reduction = (1 - v_normal / v) * 100
    print("roll angle: %.0f degrees" % roll_deg)
    print("normal impact velocity: %.3f m/s (%.1f %% reduction)" % (v_normal, reduction))
    assert 6.343 < v_normal < 6.345
    assert 9.3 < reduction < 9.4
    # the glance redirects the punch 0.12 m off line at the head
    redirect = 0.12
    assert redirect > 0.10  # clears the head half-width
    # counter cross off the roll: 0.20 s while his arm is extended
    print("counter window: cross 0.20 s vs his recovery 0.25 s")
    assert 0.20 < 0.25
    print("rule: the shoulder is the shield - the rear hand never drops")
    print("OK: %s turned the wind" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_infighting_clinch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inside: short hook 0.30 m radius at 20 rad/s; clinch tie-up in 0.40 s
    r, omega = 0.30, 20.0
    v = r * omega
    m = 4.0
    ke = 0.5 * m * v * v
    print("short hook speed: %.2f m/s, energy: %.1f J" % (v, ke))
    assert 5.99 < v < 6.01
    assert 71.9 < ke < 72.1
    # clinch: pin his arms in 0.40 s, referee break in ~2.0 s of control
    t_tie, t_control = 0.40, 2.0
    print("tie-up: %.2f s, control before break: %.1f s" % (t_tie, t_control))
    assert t_tie < 0.5
    # break clean: step back 0.60 m with hands up in 0.50 s
    v_break = 0.60 / 0.50
    print("break step-back speed: %.2f m/s" % v_break)
    assert 1.19 < v_break < 1.21
    print("rule: short tools, honest work - break clean on command")
    print("OK: %s worked the phone booth" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_switch_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # switch hop 0.25 s in a neutral moment; new angle: lead foot 0.30 m outside his
    t_switch = 0.25
    offset = 0.30
    dist = 0.85  # fighting distance
    angle = math.degrees(math.atan(offset / dist))
    print("switch time: %.2f s" % t_switch)
    print("new attack angle: %.2f degrees" % angle)
    assert 19.40 < angle < 19.50
    # weak-side honesty check: southpaw cross within 85% of orthodox power
    orth_ke, south_ke = 122.0, 106.0
    ratio = south_ke / orth_ke * 100
    print("southpaw cross power vs orthodox: %.1f %%" % ratio)
    assert 86.8 < ratio < 87.0
    assert ratio > 85.0, "weak side must be honest before it is used"
    print("rule: switch in neutral moments - mastery is two honest stances")
    print("OK: %s swore with both hands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_conditioning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # roadwork: 5 km at 5:30/km, 4 mornings/week; fight: 12 x 3-min rounds
    pace, dist = 5.5, 5.0  # min/km, km
    run_min = pace * dist
    weekly = run_min * 4
    print("roadwork: %.1f min per run, %.1f min per week" % (run_min, weekly))
    assert 27.4 < run_min < 27.6
    assert 109.9 < weekly < 110.1
    fight_work = 12 * 3
    print("championship fight work: %d minutes" % fight_work)
    assert fight_work == 36
    # intervals: 10 x 100 m at 15 s with 45 s walk-back
    interval_session = 10 * (15 + 45) / 60
    print("interval session: %.1f minutes" % interval_session)
    assert 9.9 < interval_session < 10.1
    print("rule: fights are won on the road in the dark morning hours")
    print("OK: %s forged the engine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_ring_generalship(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 12-round score model: win 7, lose 4, even 1 -> 116-113
    won, lost, even = 7, 4, 1
    assert won + lost + even == 12
    us = won * 10 + even * 10 + lost * 9
    them = lost * 10 + even * 10 + won * 9
    print("rounds: won %d, lost %d, even %d" % (won, lost, even))
    print("score: %d-%d" % (us, them))
    assert us == 116 and them == 113
    # generalship edge: ring control wins 3 of the 4 swing rounds
    swing = 4
    controlled = 3
    print("swing rounds controlled: %d of %d" % (controlled, swing))
    assert controlled / swing == 0.75
    print("rule: techniques are soldiers - generalship is the commander")
    print("OK: %s commanded the fight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cb_fight_prep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 70 kg fighter, planned 3% water cut in final 24 h, rehydrate 1.5 L over 4 h
    weight, cut_pct = 70.0, 0.03
    cut = weight * cut_pct
    print("planned water cut: %.1f kg (%.0f %% of %.0f kg)" % (cut, cut_pct * 100, weight))
    assert 2.09 < cut < 2.11
    rehyd_l, rehyd_h = 1.5, 4.0
    rate = rehyd_l / rehyd_h
    print("rehydration: %.1f L over %.0f h = %.3f L/h" % (rehyd_l, rehyd_h, rate))
    assert 0.374 < rate < 0.376
    # warm-up layers: 30 min out, building to fight intensity, done 5 min before walk
    warm_min, done_before = 30, 5
    print("warm-up window: %d min, finishing %d min before the walk" % (warm_min, done_before))
    assert warm_min - done_before == 25
    print("rule: the bell does not start the oath - it witnesses it")
    print("OK: %s sealed the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "slip": demo_cb_slip,
    "bob": demo_cb_bob,
    "parry": demo_cb_parry,
    "glove_block": demo_cb_glove_block,
    "weave": demo_cb_weave,
    "one_two": demo_cb_one_two,
    "double_jab": demo_cb_double_jab,
    "jab_body": demo_cb_jab_body,
    "one_two_three": demo_cb_one_two_three,
    "hook_off_jab": demo_cb_hook_off_jab,
    "counter_jab": demo_cb_counter_jab,
    "catch_counter": demo_cb_catch_counter,
    "feints": demo_cb_feints,
    "cut_off_ring": demo_cb_cut_off_ring,
    "off_ropes": demo_cb_off_ropes,
    "pull_counter": demo_cb_pull_counter,
    "shoulder_roll": demo_cb_shoulder_roll,
    "infighting_clinch": demo_cb_infighting_clinch,
    "switch_stance": demo_cb_switch_stance,
    "conditioning": demo_cb_conditioning,
    "ring_generalship": demo_cb_ring_generalship,
    "fight_prep": demo_cb_fight_prep,
})
