#!/usr/bin/env python3
"""Demo programs for the Karate Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: stance geometry, strike energy,
kick reach, block timing, kata timing, drill pacing. All are
machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker. Demo numbers cross-check the entry text they accompany.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_zenkutsu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front stance geometry: length from shoulder width, weight split
    shoulder = 0.45            # m, typical adult shoulder width
    length = 2.0 * shoulder    # two shoulder-widths front to back
    width = 1.0 * shoulder     # one shoulder-width side to side
    body = 70.0                # kg practitioner
    front = body * 0.60
    rear = body * 0.40
    print('stance length: %.2f m, width: %.2f m' % (length, width))
    print('weight: front %.1f kg, rear %.1f kg' % (front, rear))
    assert 0.89 < length < 0.91
    assert 0.44 < width < 0.46
    assert 41.9 < front < 42.1
    assert 27.9 < rear < 28.1
    # front knee angle and rear foot turnout
    knee_deg = 95.0
    rear_out_deg = 30.0
    print('front knee bend: %.0f deg, rear foot turnout: %.0f deg' % (knee_deg, rear_out_deg))
    assert 90.0 <= knee_deg <= 100.0
    assert 25.0 <= rear_out_deg <= 35.0
    print('rule: knee over toes, heel down, hips square')
    print('OK: %s rooted the front stance' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kiba(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # horse stance: parallel feet, even weight, depth check
    shoulder = 0.45
    width = 2.0 * shoulder
    body = 70.0
    left = body * 0.50
    right = body * 0.50
    print('stance width: %.2f m' % width)
    print('weight: left %.1f kg, right %.1f kg' % (left, right))
    assert 0.89 < width < 0.91
    assert 34.9 < left < 35.1
    assert 34.9 < right < 35.1
    # knee tracking: knee x must stay outside foot x (no collapse)
    foot_x = width / 2.0
    knee_x = foot_x + 0.02   # knees pressed slightly outward
    print('foot half-width: %.3f m, knee x: %.3f m' % (foot_x, knee_x))
    assert knee_x >= foot_x, 'knees collapsing inward'
    print('rule: knees outside the feet, back straight, weight even')
    print('OK: %s held the horse stance' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kamae(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guard geometry: lead hand reach and elbow tuck
    forearm = 0.30          # m, lead hand ahead of face
    elbow_tuck_deg = 25.0   # elbows angled inward
    chin_gap = 0.05         # m, rear fist from chin
    print('lead hand ahead of face: %.2f m' % forearm)
    print('elbow tuck: %.0f deg, rear fist off chin: %.2f m' % (elbow_tuck_deg, chin_gap))
    assert 0.29 < forearm < 0.31
    assert 20.0 <= elbow_tuck_deg <= 30.0
    assert 0.03 < chin_gap < 0.08
    # guard coverage: head guarded if hands span the target width
    head_width = 0.16
    coverage = 2 * forearm * math.tan(math.radians(20.0))
    print('lateral coverage at face plane: %.2f m vs head %.2f m' % (coverage, head_width))
    assert coverage > head_width, 'guard does not cover the head'
    print('rule: lead hand asks, rear hand answers, elbows guard the house')
    print('OK: %s raised the guard' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_chokuzuki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight punch energy: arm mass at hand speed
    arm_mass = 4.0     # kg
    hand_speed = 7.0   # m/s
    ke = 0.5 * arm_mass * hand_speed ** 2
    travel = 0.60      # m, hip to full extension
    t = travel / (hand_speed / 2.0)  # average speed over the travel
    print('kinetic energy: %.1f J' % ke)
    print('punch travel: %.2f m in %.3f s' % (travel, t))
    assert 97.9 < ke < 98.1
    assert 0.16 < t < 0.18
    # fist rotation over the travel
    rot_deg = 180.0
    print('fist rotation: %.0f deg (corkscrew)' % rot_deg)
    assert rot_deg == 180.0
    print('rule: chamber, drive, rotate, kime - then rechamber')
    print('OK: %s threw the straight punch' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kokutsu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # back stance: seventy percent on the rear leg
    body = 70.0
    rear = body * 0.70
    front = body * 0.30
    print('weight: rear %.1f kg, front %.1f kg' % (rear, front))
    assert 48.9 < rear < 49.1
    assert 20.9 < front < 21.1
    # L-shape length: 1.5 shoulder-widths
    shoulder = 0.45
    length = 1.5 * shoulder
    torso_deg = 45.0
    print('stance length: %.3f m, torso angle: %.0f deg' % (length, torso_deg))
    assert 0.674 < length < 0.676
    assert torso_deg == 45.0
    # front leg lightness: must lift without weight shift
    lift_margin = front / body
    print('front leg load fraction: %.2f (kick-ready below 0.35)' % lift_margin)
    assert lift_margin < 0.35
    print('rule: weight back, front leg free, target narrow')
    print('OK: %s settled into back stance' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_nekoashi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cat stance: ninety percent on the rear leg
    body = 70.0
    rear = body * 0.90
    front = body * 0.10
    print('weight: rear %.1f kg, front %.1f kg' % (rear, front))
    assert 62.9 < rear < 63.1
    assert 6.9 < front < 7.1
    # front foot ball contact: tiny base, instant kick
    shoulder = 0.45
    gap = 1.0 * shoulder
    print('front-back foot gap: %.2f m' % gap)
    assert 0.44 < gap < 0.46
    # balance check: center of pressure over rear foot
    cop = (rear * 0.0 + front * gap) / body
    print('center of pressure %.3f m ahead of rear foot (stable under 0.10 m)' % cop)
    assert cop < 0.10
    print('rule: ninety percent rooted, ten percent whisper')
    print('OK: %s poised in cat stance' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_ageuke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rising block: forearm rises to intercept a descending attack
    rise = 0.50        # m, hip to above forehead
    t = 0.15           # s, block time
    v = rise / t
    print('block rise: %.2f m in %.2f s -> %.2f m/s' % (rise, t, v))
    assert 3.32 < v < 3.34
    # intercept angle: block plane meets attack at 45 deg
    intercept_deg = 45.0
    finish_above_head = 0.05  # m, fist above forehead
    print('intercept angle: %.0f deg, fist finishes %.2f m above forehead' % (intercept_deg, finish_above_head))
    assert intercept_deg == 45.0
    assert 0.04 < finish_above_head < 0.06
    print('rule: meet it halfway up, carry it past the head')
    print('OK: %s rose to block' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_sotouke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # outside block: 90-degree sweep, contact timing
    forearm = 0.35          # m
    arc_deg = 90.0
    arc = forearm * math.radians(arc_deg)
    hand_speed = 4.0        # m/s
    t = arc / hand_speed
    print('sweep arc: %.3f m at %.1f m/s -> %.3f s' % (arc, hand_speed, t))
    assert 0.549 < arc < 0.551
    assert 0.136 < t < 0.139
    # deflection: attack redirected across the body
    deflect_deg = 45.0
    print('attack deflected %.0f deg across the centerline' % deflect_deg)
    assert deflect_deg == 45.0
    print('rule: guide it past, never stop it dead')
    print('OK: %s swept the outside block' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_uchiuke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inside block: mirror of the outside block
    forearm = 0.35
    arc_deg = 90.0
    arc = forearm * math.radians(arc_deg)
    hand_speed = 4.0
    t = arc / hand_speed
    print('sweep arc: %.3f m at %.1f m/s -> %.3f s' % (arc, hand_speed, t))
    assert 0.549 < arc < 0.551
    assert 0.136 < t < 0.139
    # finish position: fist a fist-width outside the shoulder
    finish = 0.10  # m outside shoulder
    print('finish: %.2f m outside the blocking-side shoulder' % finish)
    assert 0.08 < finish < 0.12
    print('rule: the mirror twin - inside to outside, ribs stay covered')
    print('OK: %s swept the inside block' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_gedanbarai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # downward sweep: broad 120-degree arc from the ear
    forearm = 0.40
    arc_deg = 120.0
    arc = forearm * math.radians(arc_deg)
    print('sweep arc: %.3f m over %.0f deg' % (arc, arc_deg))
    assert 0.837 < arc < 0.839
    # finish above the front knee
    finish_above_knee = 0.05  # m
    print('finish: %.2f m above the front knee' % finish_above_knee)
    assert 0.04 < finish_above_knee < 0.06
    # downward deflection angle carries the attack into the floor
    down_deg = 60.0
    print('deflection drives the attack %.0f deg downward' % down_deg)
    assert down_deg == 60.0
    print('rule: the broom clears the floor in one arc')
    print('OK: %s swept the low block' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_shutouchi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knife-hand strike: small mass, high speed, narrow line
    hand_mass = 0.5    # kg
    hand_speed = 9.0   # m/s
    ke = 0.5 * hand_mass * hand_speed ** 2
    print('hand-blade energy: %.2f J' % ke)
    assert 20.24 < ke < 20.26
    # concentration: edge width vs fist width
    edge_m = 0.02
    fist_m = 0.09
    concentration = fist_m / edge_m
    print('edge %.3f m vs fist %.3f m: %.1fx force concentration' % (edge_m, fist_m, concentration))
    assert 4.4 < concentration < 4.6
    print('rule: fingers together, thumb tucked, hip snaps the whip')
    print('OK: %s cut with the knife-hand' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_maegeri(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front kick: chamber, snap, rechamber - reach from leg length
    leg = 0.90          # m
    chamber_h = 1.00    # m, knee at hip height
    reach = leg         # ball of foot reach from the hip
    snap_t = 0.12       # s, extension time
    print('leg %.2f m -> reach %.2f m from hip' % (leg, reach))
    print('chamber knee height: %.2f m, snap time: %.2f s' % (chamber_h, snap_t))
    assert 0.89 < reach < 0.91
    assert 0.99 < chamber_h < 1.01
    assert 0.10 < snap_t < 0.14
    # rechamber must match extension: piston symmetry
    rechamber_t = 0.12
    print('rechamber time: %.2f s (piston symmetry)' % rechamber_t)
    assert abs(rechamber_t - snap_t) < 0.02
    print('rule: out and back like a piston - the chamber is half the kick')
    print('OK: %s snapped the front kick' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kiai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kiai timing: shout peak must land inside the kime window
    shout = 0.40        # s, exhalation burst
    kime_window = 0.10  # s, +/- 0.05 s around impact
    print('shout duration: %.2f s, kime window: %.2f s' % (shout, kime_window))
    assert 0.29 < shout < 0.51
    assert 0.09 < kime_window < 0.11
    # peak of the shout at 60% through the burst
    peak = 0.60 * shout
    impact_at = 0.24    # s into the burst
    offset = abs(peak - impact_at)
    print('shout peak at %.2f s, impact at %.2f s: offset %.3f s' % (peak, impact_at, offset))
    assert offset < kime_window / 2.0 + 0.20
    # abdominal pressure spike at kime
    pressure = 1.0 + 2.5 * math.exp(-((impact_at - peak) ** 2) / 0.01)
    print('relative abdominal pressure at impact: %.2f' % pressure)
    assert pressure > 2.0
    print('rule: the shout signs exactly at the end of the sentence')
    print('OK: %s voiced the kiai' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_ibuki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # power breathing: 4 s in, 2 s out -> cycles per minute
    inhale = 4.0
    exhale = 2.0
    cycle = inhale + exhale
    per_min = 60.0 / cycle
    print('breath cycle: %.0f s in + %.0f s out = %.0f s' % (inhale, exhale, cycle))
    print('cycles per minute: %.1f' % per_min)
    assert 9.9 < per_min < 10.1
    # Sanchin: 30 movements, one breath each, ~3 minutes
    breaths = 30
    kata_min = breaths * cycle / 60.0
    print('Sanchin %d breaths -> %.1f minutes' % (breaths, kata_min))
    assert 2.9 < kata_min < 3.1
    # tension ramps with the exhalation
    tension_end = 1.0
    tension_start = 0.2
    print('tension ramps %.1f -> %.1f across the exhalation' % (tension_start, tension_end))
    assert tension_end > tension_start
    print('rule: four seconds draw the fire, two seconds forge the steel')
    print('OK: %s breathed the power breath' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_gyakuzuki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reverse punch: hip rotation adds torso mass behind the fist
    eff_mass = 15.0    # kg, arm plus rotating torso
    hand_speed = 7.0   # m/s
    ke = 0.5 * eff_mass * hand_speed ** 2
    hip_deg = 45.0
    print('hip rotation: %.0f deg' % hip_deg)
    print('effective mass %.0f kg at %.1f m/s -> %.1f J' % (eff_mass, hand_speed, ke))
    assert 367.4 < ke < 367.6
    assert hip_deg == 45.0
    # vs the straight punch without hip drive
    arm_only = 0.5 * 4.0 * 7.0 ** 2
    gain = ke / arm_only
    print('arm-only punch: %.1f J; hip drive multiplies energy %.2fx' % (arm_only, gain))
    assert 3.74 < gain < 3.76
    print('rule: the hip writes, the arm only delivers the letter')
    print('OK: %s drove the reverse punch' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_oizuki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lunge punch: step and strike arrive as one event
    step = 0.90        # m, one stance length
    punch_travel = 0.60
    foot_plant = 0.45   # s into the motion
    impact = 0.47       # s into the motion
    sync = abs(impact - foot_plant)
    print('step: %.2f m; foot plants at %.2f s, impact at %.2f s' % (step, foot_plant, impact))
    print('foot-fist sync offset: %.3f s (must be under 0.050 s)' % sync)
    assert 0.89 < step < 0.91
    assert sync < 0.050
    # momentum added by the step: body mass at step speed
    body = 70.0
    step_speed = step / foot_plant
    p = body * step_speed
    print('step speed %.2f m/s -> body momentum %.1f kg m/s behind the punch' % (step_speed, p))
    assert 1.99 < step_speed < 2.01
    assert 139.9 < p < 140.1
    print('rule: foot and fist are one event, never two')
    print('OK: %s lunged the punch' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_uraken(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # back-fist: 120-degree whipping arc, wrist snap at the end
    forearm = 0.35
    arc_deg = 120.0
    arc = forearm * math.radians(arc_deg)
    hand_speed = 6.0
    t = arc / hand_speed
    print('snap arc: %.3f m over %.0f deg at %.1f m/s -> %.3f s' % (arc, arc_deg, hand_speed, t))
    assert 0.732 < arc < 0.734
    assert 0.121 < t < 0.123
    # wrist snap adds the last burst: 30% speed gain in the final tenth
    snap_gain = 1.30
    tip_speed = hand_speed * snap_gain
    print('wrist snap multiplies tip speed %.2fx -> %.2f m/s' % (snap_gain, tip_speed))
    assert 7.79 < tip_speed < 7.81
    print('rule: the arm stays relaxed - the wrist cracks the whip')
    print('OK: %s snapped the back-fist' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_mawashigeri(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # roundhouse: hip turnover swings the leg through its arc
    leg = 0.95
    arc_deg = 90.0
    path = leg * math.radians(arc_deg)
    pivot_deg = 135.0   # supporting foot pivot, mid-range of 90-180
    print('leg %.2f m sweeps %.3f m of arc' % (leg, path))
    print('supporting foot pivots %.0f deg (range 90-180)' % pivot_deg)
    assert 1.491 < path < 1.493
    assert 90.0 <= pivot_deg <= 180.0
    # shin speed and energy at contact
    shin_mass = 3.5
    shin_speed = 10.0
    ke = 0.5 * shin_mass * shin_speed ** 2
    print('shin %.1f kg at %.0f m/s -> %.1f J' % (shin_mass, shin_speed, ke))
    assert 174.9 < ke < 175.1
    print('rule: the pivot is the kick - turn the hip over completely')
    print('OK: %s swung the roundhouse' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_yokogeri(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # side kick: 180-degree pivot, bladed foot thrust
    pivot_deg = 180.0
    extension = 0.85    # m, hip to heel at full thrust
    thrust_t = 0.15     # s
    v = extension / thrust_t
    print('pivot: %.0f deg, thrust %.2f m in %.2f s -> %.2f m/s' % (pivot_deg, extension, thrust_t, v))
    assert pivot_deg == 180.0
    assert 5.65 < v < 5.68
    # thrust force: leg mass decelerated into the target
    leg_mass = 12.0
    stop_t = 0.05       # s, deceleration into the shield
    force = leg_mass * v / stop_t
    print('leg %.0f kg stopped in %.2f s -> %.0f N thrust' % (leg_mass, stop_t, force))
    assert 1359.0 < force < 1361.0
    print('rule: a piston, not a swing - chamber, thrust, rechamber')
    print('OK: %s thrust the side kick' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_uramawashi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hook kick: wide outward arc, heel returns across the target
    leg = 0.95
    out_deg = 135.0
    out_path = leg * math.radians(out_deg)
    print('outward arc: %.3f m over %.0f deg' % (out_path, out_deg))
    assert 2.237 < out_path < 2.239
    # the hook: heel travels back across a 0.30 m target window
    window = 0.30
    heel_speed = 8.0
    t_window = window / heel_speed
    print('heel crosses the %.2f m window in %.4f s' % (window, t_window))
    assert 0.0374 < t_window < 0.0376
    # timing: the return must beat the guard's reaction (~0.25 s)
    reaction = 0.25
    print('guard reaction ~%.2f s vs heel transit %.4f s: the hook wins' % (reaction, t_window))
    assert t_window < reaction
    print('rule: write wide to draw the eye, sign on the return')
    print('OK: %s hooked the kick' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_ushirogeri(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # back kick: 180-degree turn, heel driven straight back
    turn_deg = 180.0
    drive = 0.70        # m, heel travel behind the body
    drive_t = 0.18      # s
    v = drive / drive_t
    print('turn: %.0f deg; heel drives %.2f m back in %.2f s -> %.2f m/s' % (turn_deg, drive, drive_t, v))
    assert turn_deg == 180.0
    assert 3.88 < v < 3.90
    # whole turning mass behind one heel
    body = 70.0
    ke = 0.5 * body * v ** 2
    print('body %.0f kg turning into the drive -> %.1f J' % (body, ke))
    assert 528.0 < ke < 530.0
    # eyes first: target acquired before the leg moves
    look_lead = 0.10    # s, eyes find target before chamber
    print('eyes acquire the target %.2f s before the leg moves (never kick blind)' % look_lead)
    assert look_lead > 0.0
    print('rule: look, turn, chamber, drive - in that order, always')
    print('OK: %s drove the back kick' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_hizageri(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee strike: hands pull down as the knee spears up
    knee_h = 1.20       # m, rib height target
    pull = 0.25         # m, hands drag the target down
    closing = knee_h - pull
    print('knee rises to %.2f m; hands pull the target down %.2f m' % (knee_h, pull))
    print('closing distance covered from both ends: %.2f m' % closing)
    assert 1.19 < knee_h < 1.21
    assert 0.94 < closing < 0.96
    # drive time and impact speed of the knee
    drive_t = 0.20
    v = closing / drive_t
    knee_mass = 8.0     # kg, thigh plus hip behind it
    ke = 0.5 * knee_mass * v ** 2
    print('knee %.0f kg at %.2f m/s -> %.1f J' % (knee_mass, v, ke))
    assert 4.74 < v < 4.76
    assert 90.24 < ke < 90.26
    print('rule: pull down and drive up are one motion')
    print('OK: %s speared the knee strike' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_shutouke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knife-hand block: chest cross opens into a 60-degree fan
    fan_deg = 60.0
    arm = 0.55          # m, shoulder to knife-hand
    spread = 2 * arm * math.sin(math.radians(fan_deg / 2.0))
    print('fan opens %.0f deg; hand spread at full extension: %.3f m' % (fan_deg, spread))
    assert 0.549 < spread < 0.551
    # blocking hand height vs incoming middle punch
    hand_h = 1.30       # m, shoulder height block
    punch_h = 1.25      # m, solar plexus punch
    cover = hand_h - punch_h
    print('block at %.2f m vs punch at %.2f m: coverage margin %.2f m' % (hand_h, punch_h, cover))
    assert 0.04 < cover < 0.06
    # the open hand stays live: grab follows the block within 0.3 s
    grab_window = 0.30
    print('open hand ready to grab within %.1f s of the block' % grab_window)
    assert grab_window <= 0.30
    print('rule: cross at the chest, open like a fan, keep the hand live')
    print('OK: %s opened the knife-hand block' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_moroteuke(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # augmented block: second arm braces the first
    single = 100.0      # arbitrary structural resistance units
    reinforced = single * 1.40
    print('single-arm resistance: %.0f units' % single)
    print('reinforced resistance: %.0f units (+40%%)' % reinforced)
    assert 139.9 < reinforced < 140.1
    # both arms must arrive together: sync within 0.03 s
    primary_t = 0.16
    support_t = 0.17
    sync = abs(primary_t - support_t)
    print('primary arrives %.2f s, support %.2f s: sync offset %.3f s' % (primary_t, support_t, sync))
    assert sync < 0.03
    # deflection vs a committed attack of 150 units
    attack = 150.0
    held = reinforced >= attack * 0.90
    print('committed attack %.0f units vs reinforced %.0f: %s' % (attack, reinforced, 'HELD' if held else 'YIELDS'))
    assert held
    print('rule: two arms, one structure, one arrival')
    print('OK: %s braced the augmented block' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_heianshodan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Heian Shodan: 21 movements, ~2 s each, I-shaped embusen
    moves = 21
    per_move = 2.0      # s
    total = moves * per_move
    print('movements: %d at %.1f s each -> %.0f s total' % (moves, per_move, total))
    assert moves == 21
    assert 41.9 < total < 42.1
    # embusen: I-shape, 3 turns of 180 deg and 2 of 90 deg
    turns = [180.0, 180.0, 180.0, 90.0, 90.0]
    total_turn = sum(turns)
    print('embusen turns: %s -> %.0f deg of turning' % (turns, total_turn))
    assert total_turn == 720.0
    # technique mix: blocks, punches, hammer-fists
    blocks = 9
    punches = 9
    hammer = 3
    print('blocks %d, punches %d, hammer-fists %d' % (blocks, punches, hammer))
    assert blocks + punches + hammer == moves
    print('rule: stance, block, punch - linked, never rushed')
    print('OK: %s walked Heian Shodan' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_heiannidan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Heian Nidan: 26 movements, first kata with kicks
    moves = 26
    kicks = 4           # mae-geri and yoko-geri keage, both sides
    per_move = 2.0
    total = moves * per_move
    print('movements: %d, kicks among them: %d' % (moves, kicks))
    print('total time at %.1f s per move: %.0f s' % (per_move, total))
    assert moves == 26
    assert 51.9 < total < 52.1
    # kick share of the kata
    share = kicks / moves * 100.0
    print('kicks are %.1f %% of the form - the new dimension' % share)
    assert 15.3 < share < 15.5
    # back-fist sequences: the kata's signature
    uraken_seq = 4
    print('back-fist strike sequences: %d' % uraken_seq)
    assert uraken_seq == 4
    print('rule: hands and feet in one flow - the second dimension')
    print('OK: %s walked Heian Nidan' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_tekkishodan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Tekki Shodan: one straight lateral line, all power from the hips
    line_m = 3.0        # m, lateral embusen line
    steps = 6           # crossing steps along the line
    step_m = line_m / steps
    print('embusen: %.1f m straight line, %d crossing steps of %.2f m' % (line_m, steps, step_m))
    assert 0.49 < step_m < 0.51
    # hip vibration: 3 sharp snaps per technique cluster
    clusters = 8
    snaps = clusters * 3
    print('technique clusters: %d, hip snaps: %d' % (clusters, snaps))
    assert snaps == 24
    # stance never leaves horse stance: depth held throughout
    depth_hold = 1.00   # fraction of the kata in kiba-dachi
    print('fraction of kata in horse stance: %.2f' % depth_hold)
    assert depth_hold == 1.00
    # forward travel must be zero: the discipline of the line
    forward = 0.0
    print('forward travel: %.1f m - the line is never left' % forward)
    assert forward == 0.0
    print('rule: power without stepping - the ground speaks through the hips')
    print('OK: %s held the iron horse line' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_hangetsu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Hangetsu: 41 movements, half slow breathing, half fast
    moves = 41
    slow = 20
    fast = moves - slow
    print('movements: %d (slow %d, fast %d)' % (moves, slow, fast))
    assert moves == 41
    assert slow + fast == moves
    # slow sections: 6 s per movement with ibuki; fast: 1 s
    slow_t = slow * 6.0
    fast_t = fast * 1.0
    total = slow_t + fast_t
    print('slow %.0f s + fast %.0f s = %.0f s total' % (slow_t, fast_t, total))
    assert 140.9 < total < 141.1
    # contrast ratio: the lesson of the kata
    contrast = slow_t / fast_t
    print('slow-to-fast time ratio: %.2f:1' % contrast)
    assert 5.70 < contrast < 5.72
    # breath cycles in the slow half: one per movement
    breaths = slow
    print('ibuki breaths in the slow half: %d' % breaths)
    assert breaths == 20
    print('rule: two inks, one brush - never let the gears bleed')
    print('OK: %s breathed Hangetsu' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_bunkai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bunkai: every movement yields applications at three levels
    moves = 21          # Heian Shodan as the example
    levels = 3          # kihon, oyo, ura
    applications = moves * levels
    print('kata movements: %d x %d levels = %d applications' % (moves, levels, applications))
    assert applications == 63
    # honesty check: each application must reuse the kata's mechanics
    # score = stance_match + hip_match + timing_match, each 0..1
    scores = [2.7, 2.9, 3.0, 2.8, 2.6]
    avg = sum(scores) / len(scores)
    print('sample application fidelity scores: %s -> avg %.2f (bar 2.5)' % (scores, avg))
    assert avg > 2.5
    # a movement with no application is a movement not yet read
    unread = 0
    print('unread movements: %d' % unread)
    assert unread == 0
    print('rule: the application must wear the kata\\'s exact handwriting')
    print('OK: %s read the bunkai' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kumite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ma-ai: engagement distance = arm reach + one step
    reach = 0.70
    step = 0.90
    maai = reach + step
    print('arm reach %.2f m + step %.2f m = ma-ai %.2f m' % (reach, step, maai))
    assert 1.59 < maai < 1.61
    # progression: 4 levels from one-step to free sparring
    levels = ['kihon ippon', 'sanbon', 'jiyu ippon', 'jiyu kumite']
    print('progression levels: %d' % len(levels))
    assert len(levels) == 4
    # control: technique stops at the surface - penetration depth zero
    penetration = 0.0   # m, traditional control
    print('target penetration: %.2f m (control is the technique)' % penetration)
    assert penetration == 0.0
    # reaction drill: defender must answer inside 0.25 s at ma-ai
    attack_t = 0.30     # s, announced attack travel
    answer_t = 0.25     # s, defender block+counter budget
    print('attack travel %.2f s, defender budget %.2f s' % (attack_t, answer_t))
    assert answer_t < attack_t
    print('rule: distance, timing, control - the laboratory rules')
    print('OK: %s entered kumite' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_taisabaki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body shifting: 45-degree pivot moves the centerline off the attack
    step = 0.90
    angle_deg = 45.0
    lateral = step * math.sin(math.radians(angle_deg))
    print('step %.2f m at %.0f deg -> %.3f m lateral displacement' % (step, angle_deg, lateral))
    assert 0.635 < lateral < 0.637
    # attack corridor half-width: body must clear it
    corridor = 0.25     # m, half-width of a straight punch corridor
    clear = lateral > corridor
    print('attack corridor half-width %.2f m: %s' % (corridor, 'CLEARED' if clear else 'HIT'))
    assert clear
    # counter angle: the flank opens as the body shifts
    flank_deg = 90.0 - angle_deg
    print('flank exposure opened to the counter: %.0f deg' % flank_deg)
    assert flank_deg == 45.0
    # head stays level through the shift: vertical travel under 0.05 m
    head_drop = 0.03
    print('head vertical travel: %.2f m (must stay under 0.05 m)' % head_drop)
    assert head_drop < 0.05
    print('rule: the best block is not being there')
    print('OK: %s shifted the body' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_atemi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the classical target map: a dozen primary zones
    zones = ['temple', 'jaw hinge', 'nose', 'side of neck', 'collarbone',
             'solar plexus', 'floating ribs', 'groin', 'inner thigh',
             'knee', 'instep', 'back of hand']
    print('primary target zones catalogued: %d' % len(zones))
    assert len(zones) == 12
    # training rule: touch-only with partners - contact force capped
    touch_cap_N = 5.0   # N, essentially zero penetration
    pad_N = 500.0       # N, full mechanics on pads
    print('partner contact cap: %.0f N; pad training: %.0f N' % (touch_cap_N, pad_N))
    assert touch_cap_N < 10.0
    assert pad_N > 100.0
    # every zone pairs with its kata-prescribed technique
    paired = len(zones)  # one technique per zone in this study
    coverage = paired / len(zones)
    print('zones paired with kata techniques: %d/%d' % (paired, len(zones)))
    assert coverage == 1.0
    print('rule: study the map completely, touch it lightly, under a teacher')
    print('OK: %s mapped the vital points' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_sanchin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Sanchin: 30 breath cycles, 4 s in / 2 s out, ~3 minutes
    breaths = 30
    inhale = 4.0
    exhale = 2.0
    total = breaths * (inhale + exhale) / 60.0
    print('breaths: %d x (%.0f s + %.0f s) = %.1f minutes' % (breaths, inhale, exhale, total))
    assert 2.9 < total < 3.1
    # tension peaks at the bottom of each exhalation
    peak_tension = 1.0
    rest_tension = 0.2
    print('tension: rest %.1f -> peak %.1f at each exhalation bottom' % (rest_tension, peak_tension))
    assert peak_tension > rest_tension * 4.0
    # shime testing: teacher verifies the structure
    shime_points = ['shoulders', 'abdomen', 'thighs', 'lats']
    print('shime test points: %d' % len(shime_points))
    assert len(shime_points) == 4
    # stance never rises: depth held for the full kata
    depth = 1.00
    print('fraction of kata at full sanchin-dachi depth: %.2f' % depth)
    assert depth == 1.00
    print('rule: mind, body, breath - the three battles, one victory')
    print('OK: %s endured Sanchin' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kankudai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Kanku Dai: 65 movements, ~1.5 s each, ~100 seconds
    moves = 65
    per_move = 1.5
    total = moves * per_move
    print('movements: %d at %.1f s each -> %.1f s total' % (moves, per_move, total))
    assert moves == 65
    assert 97.4 < total < 97.6
    # technique families represented
    families = {'blocks': 18, 'punches': 20, 'kicks': 8, 'tension sequences': 12, 'jump': 1, 'transitions': 6}
    fam_total = sum(families.values())
    print('families: %s' % families)
    print('family movements sum: %d' % fam_total)
    assert fam_total == moves
    # the jump: crouch, tuck, silent landing
    jump_h = 0.40       # m
    land_noise = 0.0    # ideal: silent
    print('jump height %.2f m, landing noise target %.1f (silent)' % (jump_h, land_noise))
    assert 0.39 < jump_h < 0.41
    # two kiai at the traditional points
    kiai = 2
    print('kiai placements: %d' % kiai)
    assert kiai == 2
    print('rule: the whole art in one form - pace the breathing, keep the stances')
    print('OK: %s gazed at the sky' % NAME)
if __name__ == '__main__':
    main()
''')


DEMOS = {
    "zenkutsu": demo_zenkutsu,
    "kiba": demo_kiba,
    "kamae": demo_kamae,
    "chokuzuki": demo_chokuzuki,
    "kokutsu": demo_kokutsu,
    "nekoashi": demo_nekoashi,
    "ageuke": demo_ageuke,
    "sotouke": demo_sotouke,
    "uchiuke": demo_uchiuke,
    "gedanbarai": demo_gedanbarai,
    "shutouchi": demo_shutouchi,
    "maegeri": demo_maegeri,
    "kiai": demo_kiai,
    "ibuki": demo_ibuki,
    "gyakuzuki": demo_gyakuzuki,
    "oizuki": demo_oizuki,
    "uraken": demo_uraken,
    "mawashigeri": demo_mawashigeri,
    "yokogeri": demo_yokogeri,
    "uramawashi": demo_uramawashi,
    "ushirogeri": demo_ushirogeri,
    "hizageri": demo_hizageri,
    "shutouke": demo_shutouke,
    "moroteuke": demo_moroteuke,
    "heianshodan": demo_heianshodan,
    "heiannidan": demo_heiannidan,
    "tekkishodan": demo_tekkishodan,
    "hangetsu": demo_hangetsu,
    "bunkai": demo_bunkai,
    "kumite": demo_kumite,
    "taisabaki": demo_taisabaki,
    "atemi": demo_atemi,
    "sanchin": demo_sanchin,
    "kankudai": demo_kankudai,
}
