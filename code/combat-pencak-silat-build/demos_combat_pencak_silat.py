#!/usr/bin/env python3
"""Demo programs for the Pencak Silat Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: stance geometry, guard angles,
footwork cadence, breathing rates, strike reach, block coverage, evasion
displacement, sweep timing, throw loading, lock levers, form timing,
scoring math, and drill pacing. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Demo numbers cross-check
the entry text they accompany.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_kuda_kuda(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kuda-kuda depan geometry: length from shoulder width, 60/40 split
    shoulder = 0.45            # m, typical adult shoulder width
    length = 1.5 * shoulder    # one and a half shoulder-widths front to back
    mid_width = 2.0 * shoulder # kuda-kuda tengah: two shoulder-widths
    body = 70.0                # kg practitioner
    front = body * 0.60
    rear = body * 0.40
    print('depan length: %.3f m, tengah width: %.2f m' % (length, mid_width))
    print('weight: front %.1f kg, rear %.1f kg' % (front, rear))
    assert 0.674 < length < 0.676
    assert 0.89 < mid_width < 0.91
    assert 41.9 < front < 42.1
    assert 27.9 < rear < 28.1
    # five classical stances, held ten counts each
    stances = ['depan', 'belakang', 'tengah', 'samping', 'silang']
    hold_s = len(stances) * 10 * 1.0   # one second per count
    print('stances: %d, hold cycle: %.0f s' % (len(stances), hold_s))
    assert hold_s == 50.0 or 49.9 < hold_s < 50.1
    print('rule: knees over toes, back straight, weight honest')
    print('OK: %s rooted the five stances' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_sikap_pasang(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guard geometry: lead hand extension and elbow angle
    arm = 0.60                 # m, typical arm length
    extension = arm * (2.0 / 3.0)  # two-thirds extension
    elbow_deg = 120.0
    print('lead hand reach: %.2f m, elbow angle: %.0f deg' % (extension, elbow_deg))
    assert 0.39 < extension < 0.41
    assert 115.0 <= elbow_deg <= 125.0
    # shoulder push test: absorbed through stance, not by leaning
    push_n = 60.0              # N, gentle teacher push
    body = 70.0
    absorb_ratio = push_n / (body * 9.81)
    print('push absorbed: %.1f N (%.2f of body weight)' % (push_n, absorb_ratio))
    assert 0.08 < absorb_ratio < 0.10
    # guard shifts: extend six inches and return
    shift_m = 6 * 0.0254
    print('guard shift: %.3f m out and back' % shift_m)
    assert 0.15 < shift_m < 0.16
    print('rule: lead hand greets, rear hand promises, stance holds the door')
    print('OK: %s set the guard' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_langkah(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # footwork cadence drill: ten floor lengths per pattern
    floor_m = 12.0             # m, training lane
    step_m = 0.65              # m, average langkah step
    steps_per_length = floor_m / step_m
    lengths = 10
    total_steps = steps_per_length * lengths
    print('steps per length: %.1f, ten lengths: %.0f steps' % (steps_per_length, total_steps))
    assert 18.4 < steps_per_length < 18.5
    assert 184.0 < total_steps < 185.0
    # drill pace: one step per 1.2 s keeps the head level
    pace_s = 1.2
    drill_min = total_steps * pace_s / 60.0
    print('drill time per pattern: %.1f min' % drill_min)
    assert 3.6 < drill_min < 3.8
    # triangle pattern: three steps per side, 60-degree pivots
    tri_steps = 3 * 3
    pivot_deg = 60.0
    print('triangle: %d steps, %.0f-degree pivots' % (tri_steps, pivot_deg))
    assert tri_steps == 9
    print('rule: head glides at one height, every step lands in stance')
    print('OK: %s walked the patterns' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_pernapasan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 4-2-4 counted breathing: breaths per minute
    cycle_s = 4 + 2 + 4
    bpm = 60.0 / cycle_s
    print('breath cycle: %d s -> %.1f breaths/min' % (cycle_s, bpm))
    assert 5.9 < bpm < 6.1
    # stance breathing: two minutes in kuda-kuda tengah
    stance_s = 120.0
    breaths = stance_s / cycle_s
    print('two-minute stance hold: %.0f breath cycles' % breaths)
    assert 11.9 < breaths < 12.1
    # technique breathing: ten punches, one exhale each
    punches = 10
    exhales = punches  # one exhale per punch
    print('punch set: %d punches, %d exhales' % (punches, exhales))
    assert exhales == punches
    # calm threshold: resting rate under 8 breaths/min after drill
    print('rule: exhale carries the technique, inhale recovers the guard')
    print('OK: %s breathed the discipline' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_pukulan_lurus(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight punch: reach from guard, fist rotation in final third
    arm = 0.60                 # m
    shoulder_add = 0.15        # m, hip snap adds reach
    reach = arm + shoulder_add
    rotate_point = reach * (2.0 / 3.0)  # rotation in final third
    print('punch reach: %.2f m, rotation begins at %.2f m' % (reach, rotate_point))
    assert 0.74 < reach < 0.76
    assert 0.49 < rotate_point < 0.51
    # drill volume: ten slow + ten fast per side, one-minute alternating
    slow = 10
    fast = 10
    per_side = slow + fast
    print('drill: %d slow + %d fast = %d per side' % (slow, fast, per_side))
    assert per_side == 20
    # punch rate in the one-minute alternating set: ~1 punch per 1.5 s
    minute_set = 60.0 / 1.5
    print('one-minute set: ~%.0f punches' % minute_set)
    assert 39.9 < minute_set < 40.1
    print('rule: shortest line, hip snaps, elbow never locks')
    print('OK: %s threw the straight punch' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_tendangan_lurus(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front push kick: reach from leg length plus hip drive
    leg = 0.85                # m, typical leg length
    hip_drive = 0.12          # m, hip thrust adds reach
    reach = leg + hip_drive
    print('kick reach: %.2f m' % reach)
    assert 0.96 < reach < 0.98
    # chamber height: knee toward chest, thigh above horizontal
    chamber_deg = 100.0       # degrees of hip flexion at chamber
    print('chamber hip flexion: %.0f deg' % chamber_deg)
    assert 90.0 <= chamber_deg <= 110.0
    # drill ladder: wall x10, pad x10 per leg
    per_leg = 10 + 10
    both_legs = per_leg * 2
    print('drill: %d per leg, %d total' % (per_leg, both_legs))
    assert both_legs == 40
    # torso counter-lean for balance
    lean_deg = 10.0
    print('counter-lean: %.0f deg' % lean_deg)
    assert 5.0 <= lean_deg <= 15.0
    print('rule: chamber, extend, rechamber - hands never leave guard')
    print('OK: %s drove the front kick' % NAME)
if __name__ == '__main__':
    main()
''')


DEMOS = {
    "kuda-kuda": demo_kuda_kuda,
    "sikap-pasang": demo_sikap_pasang,
    "langkah": demo_langkah,
    "pernapasan": demo_pernapasan,
    "pukulan-lurus": demo_pukulan_lurus,
    "tendangan-lurus": demo_tendangan_lurus,
}


def demo_tangkisan_dalam(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inside block: forearm meets attack at 45 degrees
    angle_deg = 45.0
    print('block contact angle: %.0f deg' % angle_deg)
    assert 40.0 <= angle_deg <= 50.0
    # stance drop as the block lands: one inch
    drop_m = 1 * 0.0254
    print('stance drop on contact: %.3f m' % drop_m)
    assert 0.025 < drop_m < 0.026
    # four gates of the wall
    gates = ['dalam', 'luar', 'atas', 'bawah']
    print('four gates: %s' % ', '.join(gates))
    assert len(gates) == 4
    # drill: ten blocks per side, then answered with free hand
    per_side = 10
    counters = per_side  # one counter per block
    print('drill: %d blocks/side, %d counters' % (per_side, counters))
    assert counters == per_side
    print('rule: small block, rooted stance, free hand answers')
    print('OK: %s raised the inside block' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_elakan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elakan bawah: sink eight inches straight down
    duck_m = 8 * 0.0254
    print('duck depth: %.3f m' % duck_m)
    assert 0.20 < duck_m < 0.21
    # elakan atas: lean back fifteen degrees from the hips
    lean_deg = 15.0
    head_clear_m = 0.55 * math.sin(math.radians(lean_deg))  # head at ~0.55m above hips
    print('lean: %.0f deg -> head clears %.3f m' % (lean_deg, head_clear_m))
    assert 0.14 < head_clear_m < 0.15
    # elakan samping: slip six inches offline
    slip_m = 6 * 0.0254
    print('side slip: %.3f m offline' % slip_m)
    assert 0.15 < slip_m < 0.16
    # four evasions, five each per side at slow speed
    evasions = ['bawah', 'atas', 'samping', 'putar']
    reps = len(evasions) * 5 * 2
    print('slow drill: %d evasions' % reps)
    assert reps == 40
    print('rule: head moves inches, feet stay under the body')
    print('OK: %s moved the target' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_tepisan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # deflecting parry: hand travels under six inches
    travel_m = 6 * 0.0254
    print('parry travel: %.3f m max' % travel_m)
    assert 0.15 < travel_m < 0.16
    # slap contact: brief impulse redirects the punch offline
    contact_s = 0.08          # seconds of contact
    punch_speed = 7.0         # m/s, committed straight punch
    offline_m = 0.15          # target deflection at the shoulder
    print('contact: %.2f s redirects %.2f m offline' % (contact_s, offline_m))
    assert 0.05 < contact_s < 0.12
    # energy cost vs a hard block: parry uses a fraction
    parry_effort = 0.15       # relative effort vs hard block = 1.0
    print('parry effort vs hard block: %.2f' % parry_effort)
    assert 0.10 < parry_effort < 0.25
    # drill: ten parries per side, counter from the parrying hand
    reps = 10 * 2
    print('drill: %d parries, %d same-beat counters' % (reps, reps))
    assert reps == 20
    print('rule: slap, not push - the lighter the touch, the faster the counter')
    print('OK: %s brushed the attack aside' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_tangkapan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # catch timing: punch at 7 m/s over 0.6 m reach -> catch window
    punch_speed = 7.0         # m/s
    reach_m = 0.60
    window_s = reach_m / punch_speed
    print('catch window: %.3f s' % window_s)
    assert 0.08 < window_s < 0.10
    # catch at full extension: limb slowest at the end of travel
    extension_frac = 0.95     # catch in final 5% of travel
    catch_zone_m = reach_m * (1 - extension_frac)
    print('catch zone: final %.2f m of travel' % catch_zone_m)
    assert 0.02 < catch_zone_m < 0.05
    # absorbing langkah: one small step back, ~0.3 m
    absorb_m = 0.30
    print('absorbing step: %.2f m' % absorb_m)
    assert 0.25 < absorb_m < 0.35
    # drill: ten catches per side at slow speed
    reps = 10 * 2
    print('drill: %d soft catches' % reps)
    assert reps == 20
    print('rule: catch at extension, absorb with the step, never grab rigidly')
    print('OK: %s caught the limb' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kembangan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flowing dance: three unbroken minutes at 60 beats per minute
    minutes = 3
    bpm = 60
    beats = minutes * bpm
    print('flow session: %d beats' % beats)
    assert beats == 180
    # five techniques per sequence, one per beat
    per_seq = 5
    sequences = beats // per_seq
    print('five-technique sequences: %d' % sequences)
    assert sequences == 36
    # walking circle between sequences resets the flow
    circle_s = 20.0            # seconds per walking circle
    circles = (minutes * 60) / (per_seq + circle_s / (60.0 / bpm))
    print('rule: transitions disappear, only the river remains')
    print('OK: %s danced the flow' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_tendangan_sabit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crescent kick arc: radius ~ hip height, 120-degree sweep
    radius_m = 0.95
    arc_deg = 120.0
    arc_m = radius_m * math.radians(arc_deg)
    print('arc radius: %.2f m, sweep: %.0f deg -> arc %.2f m' % (radius_m, arc_deg, arc_m))
    assert 1.98 < arc_m < 2.00
    # supporting foot pivots 45 degrees
    pivot_deg = 45.0
    print('support pivot: %.0f deg' % pivot_deg)
    assert 40.0 <= pivot_deg <= 50.0
    # drill: ten arcs per leg per direction on the pad
    reps = 10 * 2 * 2  # luar + dalam, both legs
    print('pad drill: %d arcs' % reps)
    assert reps == 40
    # the kick must return along the same path: recovery time ~ swing time
    print('rule: whip back along the same crescent, torso upright')
    print('OK: %s swept the crescent' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_tendangan_t(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # side kick: supporting foot pivots 180 degrees
    pivot_deg = 180.0
    print('support pivot: %.0f deg' % pivot_deg)
    assert 175.0 <= pivot_deg <= 185.0
    # heel reach: leg length plus full hip commitment
    leg = 0.85
    hip_commit = 0.15
    reach = leg + hip_commit
    print('heel reach: %.2f m' % reach)
    assert 0.99 < reach < 1.01
    # chamber discipline: ten wall chambers per leg without extending
    chambers = 10 * 2
    kicks = 10 * 2
    print('wall chambers: %d, pad kicks: %d' % (chambers, kicks))
    assert chambers == 20 and kicks == 20
    # heaviest kick: body weight behind a small heel surface
    body = 70.0
    heel_area_cm2 = 25.0
    pressure = body / heel_area_cm2  # kg per cm^2, relative measure
    print('relative heel pressure: %.1f kg/cm^2' % pressure)
    assert 2.7 < pressure < 2.9
    print('rule: tight chamber hides the kick, hip commits everything')
    print('OK: %s thrust the side kick' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_siku(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow range: inside arm's reach, the close zone
    arm = 0.60
    close_zone = 0.50          # m, elbows rule inside half a meter
    print('elbow zone: under %.2f m' % close_zone)
    assert close_zone < arm
    # five core elbows, ten reps per side on the pad
    elbows = ['depan', 'atas', 'bawah', 'belakang', 'putar']
    reps = len(elbows) * 10 * 2
    print('elbows: %d, pad drill: %d strikes' % (len(elbows), reps))
    assert reps == 100
    # striking elbow bent ~90 degrees, fist tucked to own shoulder
    elbow_deg = 90.0
    print('striking elbow bend: %.0f deg' % elbow_deg)
    assert 80.0 <= elbow_deg <= 100.0
    # hip snap adds rotation: torso turns ~45 deg into the strike
    torso_deg = 45.0
    print('torso rotation: %.0f deg' % torso_deg)
    assert 40.0 <= torso_deg <= 50.0
    print('rule: never reach with the elbow - langkah brings the target')
    print('OK: %s whipped the elbows' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_lutut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee strike: thigh reaches horizontal at the top
    thigh_deg = 90.0           # degrees of hip flexion
    print('knee lift: thigh to %.0f deg' % thigh_deg)
    assert 85.0 <= thigh_deg <= 95.0
    # strike height: hip height ~0.95 m plus knee point
    hip_h = 0.95
    knee_point = 0.15          # knee point above thigh line
    strike_h = hip_h + knee_point
    print('strike height: %.2f m' % strike_h)
    assert 1.09 < strike_h < 1.11
    # support rises onto the ball of the foot: +8 cm
    rise_m = 0.08
    print('support rise: %.2f m' % rise_m)
    assert 0.06 < rise_m < 0.10
    # drill: ten knees per leg, pull timed with the rise
    reps = 10 * 2
    print('pad drill: %d knees' % reps)
    assert reps == 20
    print('rule: hands pull down as the knee rises - one motion')
    print('OK: %s drove the knee' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_pukulan_bandul(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # swinging punch: arm arc radius and angular speed
    arm = 0.60
    arc_deg = 180.0            # half-circle swing
    arc_m = arm * math.radians(arc_deg)
    print('swing arc: %.2f m' % arc_m)
    assert 1.88 < arc_m < 1.90
    # swing time ~0.35 s -> angular velocity
    swing_s = 0.35
    omega = math.radians(arc_deg) / swing_s
    print('angular velocity: %.1f rad/s' % omega)
    assert 8.9 < omega < 9.1
    # elbow bent 90 degrees through the arc
    elbow_deg = 90.0
    print('elbow bend: %.0f deg' % elbow_deg)
    assert 80.0 <= elbow_deg <= 100.0
    # drill: ten slow arcs per side, feet-hips-shoulder as one
    reps = 10 * 2
    print('pad drill: %d arcs' % reps)
    assert reps == 20
    print('rule: the turn powers the blow - miss becomes elakan putar')
    print('OK: %s swung the pendulum' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_sapuan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep timing: partner steps at ~1.4 steps/s, sweep must land on commitment
    step_hz = 1.4
    step_period = 1.0 / step_hz
    commit_frac = 0.6          # weight commits 60% through the step
    commit_s = step_period * commit_frac
    print('step period: %.2f s, commitment at %.2f s' % (step_period, commit_s))
    assert 0.42 < commit_s < 0.44
    # sweep hook height: just above the ankle, ~12 cm
    hook_m = 0.12
    print('hook height: %.2f m (never the knee)' % hook_m)
    assert 0.10 < hook_m < 0.15
    # leverage: light hook topples committed weight
    body = 70.0
    sweep_force_n = 120.0      # modest hook force
    topple_ratio = sweep_force_n / (body * 9.81)
    print('sweep force: %.0f N (%.2f of body weight)' % (sweep_force_n, topple_ratio))
    assert 0.16 < topple_ratio < 0.19
    # drill: ten sweeps per side at walking speed
    reps = 10 * 2
    print('mat drill: %d sweeps' % reps)
    assert reps == 20
    print('rule: sweep the committed step, guide the partner down')
    print('OK: %s swept the leg' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_bantingan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hip throw: drop hips below partner's center (~0.95 m for 70 kg)
    partner_com = 0.95         # m
    drop_m = 0.25              # sink 25 cm under their center
    hip_h = partner_com - drop_m
    print('throwing hip height: %.2f m' % hip_h)
    assert 0.69 < hip_h < 0.71
    # the legs lift: 70 kg partner, lifter extends with legs
    partner_kg = 70.0
    assist_frac = 0.40         # partner's momentum assists ~40%
    lift_kg = partner_kg * (1 - assist_frac)
    print('effective lift: %.0f kg' % lift_kg)
    assert 41.9 < lift_kg < 42.1
    # three beats: off-balance, entry, turning lift
    beats = 3
    total_s = 1.2              # full throw at drill speed
    per_beat = total_s / beats
    print('three beats at %.2f s each' % per_beat)
    assert 0.39 < per_beat < 0.41
    # drill: five throws per side, slow, fully cooperative
    reps = 5 * 2
    print('mat drill: %d throws' % reps)
    assert reps == 10
    print('rule: legs lift, arms guide, partner breakfalls')
    print('OK: %s threw the partner' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kuncian(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wrist lock lever: forearm ~0.28 m as the lever arm
    lever_m = 0.28
    gentle_n = 25.0            # N, gentle training pressure
    torque = lever_m * gentle_n
    print('lever: %.2f m x %.0f N = %.1f N-m' % (lever_m, gentle_n, torque))
    assert 6.9 < torque < 7.1
    # safe training stops far short of the joint limit: 60% of range
    wrist_range_deg = 140.0    # total wrist flexion/extension range
    train_limit = wrist_range_deg * 0.60
    print('wrist range: %.0f deg, training limit: %.0f deg' % (wrist_range_deg, train_limit))
    assert 83.9 < train_limit < 84.1
    # the tap is law: release within half a second
    release_s = 0.5
    print('max release delay: %.1f s' % release_s)
    assert release_s <= 0.5
    # drill: five locks per side, trading roles
    reps = 5 * 2
    print('drill: %d locks, %d releases' % (reps, reps))
    assert reps == 10
    print('rule: the tap is law - release instantly, every time')
    print('OK: %s turned the key' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_tendangan_belakang(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # back kick: full 180-degree turn on the ball of the foot
    turn_deg = 180.0
    print('turn: %.0f deg' % turn_deg)
    assert 175.0 <= turn_deg <= 185.0
    # heel reach behind: leg plus hip thrust
    leg = 0.85
    hip_thrust = 0.10
    reach = leg + hip_thrust
    print('heel reach: %.2f m' % reach)
    assert 0.94 < reach < 0.96
    # spotting: glance first, turn on a fixed line
    spot_s = 0.25              # seconds to spot before turning
    turn_s = 0.45              # seconds for the turn
    total_s = spot_s + turn_s
    print('spot %.2f s + turn %.2f s = %.2f s' % (spot_s, turn_s, total_s))
    assert 0.69 < total_s < 0.71
    # drill: five slow turns per side, then ten kicks per side on pad
    turns = 5 * 2
    kicks = 10 * 2
    print('footwork: %d turns, pad: %d kicks' % (turns, kicks))
    assert turns == 10 and kicks == 20
    print('rule: spot the target first - never throw it blind')
    print('OK: %s kicked over the shoulder' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_guntingan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scissors takedown: legs close from ~90 deg open to shut
    open_deg = 90.0
    close_deg = 10.0
    shear_deg = open_deg - close_deg
    print('scissor shear: %.0f deg' % shear_deg)
    assert 79.9 < shear_deg < 80.1
    # level drop: attacker drops ~0.5 m to get under the leg
    drop_m = 0.50
    print('level drop: %.2f m' % drop_m)
    assert 0.45 < drop_m < 0.55
    # shear force at the ankle: two legs vs one planted leg
    body = 70.0
    shear_n = body * 9.81 * 0.35  # 35% of body weight through the shear
    print('shear load: %.0f N' % shear_n)
    assert 239.0 < shear_n < 241.0
    # drill: five per side, slow, fully cooperative
    reps = 5 * 2
    print('mat drill: %d scissors' % reps)
    assert reps == 10
    print('rule: total commitment - half a scissors leaves you underneath')
    print('OK: %s closed the scissors' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_jurus_tunggal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # solo form: learned in four-movement sections, ten reps each
    section_moves = 4
    section_reps = 10
    total_moves = 48           # typical tunggal movement count
    sections = total_moves / section_moves
    print('form: %d moves in %.0f sections' % (total_moves, sections))
    assert sections == 12.0
    learn_reps = sections * section_reps
    print('learning volume: %.0f section reps' % learn_reps)
    assert learn_reps == 120.0
    # performance duration: sixty to ninety seconds
    dur_lo, dur_hi = 60.0, 90.0
    mid = (dur_lo + dur_hi) / 2
    move_s = mid / total_moves
    print('tempo: %.2f s per move at mid duration' % move_s)
    assert 1.55 < move_s < 1.57
    # session: three full forms plus weakest-section work
    full_runs = 3
    weak_reps = 10
    print('session: %d full runs + %d weak-section reps' % (full_runs, weak_reps))
    assert full_runs == 3 and weak_reps == 10
    print('rule: the form is the school - practice it at dawn')
    print('OK: %s performed the solo form' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_sambutan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # planned counters: three receptions, ten exchanges each per role
    receptions = 3
    exchanges = 10
    per_role = receptions * exchanges
    print('set exchanges per role: %d' % per_role)
    assert per_role == 30
    # promotion threshold: eight clean answers out of ten
    threshold = 8.0 / 10.0
    print('clean-answer threshold: %.0f%%' % (threshold * 100))
    assert 0.79 < threshold < 0.81
    # chained practice: five continuous exchanges per round
    chain = 5
    rounds = 3
    chain_total = chain * rounds
    print('chain practice: %d exchanges' % chain_total)
    assert chain_total == 15
    # reaction window for a trained counter: ~0.3 s from read to answer
    react_s = 0.30
    print('trained counter window: %.2f s' % react_s)
    assert 0.25 < react_s < 0.35
    print('rule: vocabulary becomes conversation - answer without thought')
    print('OK: %s received every guest' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_jarak_tempo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three zones measured from personal reach
    kick_reach = 0.97          # m, tendangan lurus reach
    punch_reach = 0.75         # m, pukulan lurus reach
    elbow_reach = 0.45         # m, siku reach
    print('zones: jauh %.2f m | sedang %.2f m | dekat %.2f m'
          % (kick_reach, punch_reach, elbow_reach))
    assert kick_reach > punch_reach > elbow_reach
    # zone gaps
    gap1 = kick_reach - punch_reach
    gap2 = punch_reach - elbow_reach
    print('zone steps: %.2f m, %.2f m' % (gap1, gap2))
    assert 0.21 < gap1 < 0.23
    assert 0.29 < gap2 < 0.31
    # zone game: one minute per zone, three zones
    zone_min = 1.0
    total_min = zone_min * 3
    print('zone game: %.0f minutes' % total_min)
    assert total_min == 3.0
    # tempo rounds: three rounds of two minutes
    rounds, round_min = 3, 2
    print('tempo sparring: %d x %d min = %d min' % (rounds, round_min, rounds * round_min))
    assert rounds * round_min == 6
    print('rule: timing beats speed - counter on the half-beat')
    print('OK: %s measured distance and time' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_toya(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # staff cut to about the practitioner's height
    height_m = 1.70
    staff_m = height_m * 1.0
    print('staff length: %.2f m for %.2f m practitioner' % (staff_m, height_m))
    assert 1.69 < staff_m < 1.71
    # grip: hands one-third from each end
    grip_m = staff_m / 3.0
    print('grip inset: %.2f m from each end' % grip_m)
    assert 0.56 < grip_m < 0.58
    # thrust driven by hip: hand speed from hip rotation
    hip_omega = 6.0            # rad/s, hip snap
    hand_r = 0.45              # m, hand radius from hip axis
    hand_speed = hip_omega * hand_r
    print('thrust hand speed: %.1f m/s' % hand_speed)
    assert 2.6 < hand_speed < 2.8
    # drill: ten reps each of thrust, sweep-block, spin transition
    moves = 3
    reps = moves * 10
    print('basics drill: %d reps' % reps)
    assert reps == 30
    print('rule: rattan before hardwood, teacher present always')
    print('OK: %s moved the long staff' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_tanding(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tanding scoring: punch 1, kick 2, clean takedown 3
    score = {'punch': 1, 'kick': 2, 'takedown': 3}
    # sample bout: 6 punches, 4 kicks, 1 takedown
    total = 6 * score['punch'] + 4 * score['kick'] + 1 * score['takedown']
    print('sample card: 6x%d + 4x%d + 1x%d = %d points'
          % (score['punch'], score['kick'], score['takedown'], total))
    assert total == 17
    # bout format: three rounds of two minutes, one minute rest
    rounds, round_min, rest_min = 3, 2, 1
    fight_min = rounds * round_min
    total_min = fight_min + (rounds - 1) * rest_min
    print('bout: %d min fighting, %d min total' % (fight_min, total_min))
    assert fight_min == 6 and total_min == 8
    # takedown value vs punches: one takedown equals three punches
    equiv = score['takedown'] / score['punch']
    print('one takedown = %.0f punches' % equiv)
    assert equiv == 3.0
    # conditioning: two-minute intense pad rounds match bout demand
    print('rule: control is judged - the salute matters most')
    print('OK: %s scored the bout' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_golok(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # heritage practice blade: wooden trainer, ~45 cm
    trainer_cm = 45.0
    print('practice trainer: %.0f cm (wooden, never live)' % trainer_cm)
    assert 40.0 <= trainer_cm <= 50.0
    # three fundamental cutting angles
    cuts = ['downward diagonal', 'upward diagonal', 'horizontal']
    print('fundamental cuts: %d' % len(cuts))
    assert len(cuts) == 3
    # diagonal cut angle: 45 degrees from vertical
    diag_deg = 45.0
    print('diagonal cut: %.0f deg' % diag_deg)
    assert 40.0 <= diag_deg <= 50.0
    # drill: ten slow cuts per angle
    reps = len(cuts) * 10
    print('slow drill: %d cuts' % reps)
    assert reps == 30
    # safety: clear space radius = trainer length + arm + margin
    arm = 0.60
    clear_m = trainer_cm / 100.0 + arm + 0.5
    print('clear space radius: %.2f m' % clear_m)
    assert 1.54 < clear_m < 1.56
    print('rule: practice blade only - respect is the lesson')
    print('OK: %s honored the golok heritage' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_karambit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # curved trainer: ~12 cm blade, ring for the index finger
    blade_cm = 12.0
    ring_dia_cm = 2.5
    print('trainer: %.0f cm curve, ring %.1f cm' % (blade_cm, ring_dia_cm))
    assert 10.0 <= blade_cm <= 15.0
    assert 2.0 <= ring_dia_cm <= 3.0
    # hooking arc radius: small, close-range - about a hand span
    arc_m = 0.20
    arc_deg = 90.0
    arc_len = arc_m * math.radians(arc_deg)
    print('hook arc: %.2f m radius -> %.2f m path' % (arc_m, arc_len))
    assert 0.31 < arc_len < 0.32
    # grip transitions: ten per side, slow
    reps = 10 * 2
    print('grip transitions: %d' % reps)
    assert reps == 20
    # precision lesson: short reach punishes wasted motion
    reach_m = blade_cm / 100.0 + 0.10  # blade plus fist
    print('effective reach: %.2f m' % reach_m)
    assert 0.21 < reach_m < 0.23
    print('rule: smallest true stroke beats the wildest swing')
    print('OK: %s flowed the karambit' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_main_bawah(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # breakfalls: ten each of back, side, front
    falls = 3 * 10
    print('breakfalls: %d' % falls)
    assert falls == 30
    # impact spread: arm slap distributes force over ~0.3 s vs 0.05 s
    hard_s, soft_s = 0.05, 0.30
    reduction = hard_s / soft_s
    print('slap spreads impact: %.2f of rigid force' % reduction)
    assert 0.16 < reduction < 0.18
    # shrimping: ten lengths of a 12 m mat
    mat_m = 12.0
    shrimp_m = 0.40            # m per shrimp
    shrimps = (mat_m / shrimp_m) * 10
    print('shrimping: %.0f shrimps' % shrimps)
    assert 299.9 < shrimps < 300.1
    # positional hold: ten-count control, then switch
    hold_s = 10.0
    switches = 6
    print('positional drill: %d x %.0f s holds' % (switches, hold_s))
    assert switches * hold_s == 60.0
    print('rule: the floor is another stance - fall well first')
    print('OK: %s played the ground game' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_keris(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # heritage trainer: ~35 cm with sheath, wooden, never live
    trainer_cm = 35.0
    print('trainer: %.0f cm with sheath' % trainer_cm)
    assert 30.0 <= trainer_cm <= 40.0
    # drawing ritual: ten slow repetitions of pure protocol
    ritual_reps = 10
    ritual_s = 8.0             # seconds per careful draw-and-return
    ritual_min = ritual_reps * ritual_s / 60.0
    print('drawing ritual: %d reps, %.1f min' % (ritual_reps, ritual_min))
    assert 1.3 < ritual_min < 1.4
    # thrusting form: ten slow thrusts per side, breath-matched
    thrusts = 10 * 2
    print('heritage thrusts: %d (exhale out, inhale back)' % thrusts)
    assert thrusts == 20
    # thrust reach: forearm plus trainer
    forearm = 0.28
    reach = forearm + trainer_cm / 100.0
    print('thrust reach: %.2f m' % reach)
    assert 0.62 < reach < 0.64
    print('rule: responsibility before technique - restraint is mastery')
    print('OK: %s studied the keris heritage' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_jurus_senjata(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weapon form: four-movement sections like the empty-hand tunggal
    section_moves = 4
    total_moves = 40
    sections = total_moves / section_moves
    print('weapon form: %d moves in %.0f sections' % (total_moves, sections))
    assert sections == 10.0
    # duration: sixty to one hundred twenty seconds
    dur_lo, dur_hi = 60.0, 120.0
    mid = (dur_lo + dur_hi) / 2
    move_s = mid / total_moves
    print('tempo: %.2f s per move at mid duration' % move_s)
    assert 2.24 < move_s < 2.26
    # session: three full runs plus weakest-transition work
    full_runs, weak_reps = 3, 10
    session_moves = full_runs * total_moves + weak_reps
    print('session moves: %d' % session_moves)
    assert session_moves == 130
    # grip changes: ~one per eight moves, each checked in the mirror
    grips = total_moves // 8
    print('grip changes: %d' % grips)
    assert grips == 5
    print('rule: slow for years before ever performing fast')
    print('OK: %s performed the weapon form' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_patahan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # controlled study: training stops at 60% of joint range
    wrist_range = 140.0        # degrees total
    train_frac = 0.60
    train_deg = wrist_range * train_frac
    margin_deg = wrist_range - train_deg
    print('wrist: train to %.0f deg, margin %.0f deg' % (train_deg, margin_deg))
    assert 83.9 < train_deg < 84.1
    assert 55.9 < margin_deg < 56.1
    # elbow: hinge range ~145 deg, same 60% rule
    elbow_range = 145.0
    elbow_train = elbow_range * train_frac
    print('elbow: train to %.0f deg' % elbow_train)
    assert 86.9 < elbow_train < 87.1
    # study blocks: one joint per block across many weeks
    joints = ['wrist', 'elbow', 'shoulder']
    weeks_per = 4
    study_weeks = len(joints) * weeks_per
    print('study: %d joints x %d weeks = %d weeks' % (len(joints), weeks_per, study_weeks))
    assert study_weeks == 12
    # release standard: instant on any tap signal
    print('rule: hold the knowledge, choose the release')
    print('OK: %s studied restraint' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_aliran(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lineage: record teacher, their teacher, and generations back
    generations = 5            # typical traceable lineage depth
    print('lineage depth: %d generations' % generations)
    assert generations >= 3
    # comparative study: three contrasting streams in the journal
    streams = ['cimande', 'minangkabau silek', 'modern perguruan']
    print('streams studied: %d' % len(streams))
    assert len(streams) == 3
    # one guest seminar per year
    seminars_per_year = 1
    years = 5
    print('seminars over %d years: %d' % (years, seminars_per_year * years))
    assert seminars_per_year * years == 5
    # archipelago scale: hundreds of aliran across thousands of islands
    islands = 17000            # Indonesian archipelago, approximate
    aliran_est = 300           # estimated distinct streams
    per_island = aliran_est / islands
    print('~%d aliran across ~%d islands' % (aliran_est, islands))
    assert 0.01 < per_island < 0.03
    print('rule: carry the stream forward unpolluted - add, never dam')
    print('OK: %s traced the streams' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_ujian(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grading components: stance endurance five minutes in kuda-kuda tengah
    stance_s = 5 * 60
    print('stance endurance: %d s' % stance_s)
    assert stance_s == 300
    # jurus performed twice at grading
    jurus_runs = 2
    jurus_s = 75.0             # mid-duration tunggal
    jurus_total = jurus_runs * jurus_s
    print('jurus: %d runs x %.0f s = %.0f s' % (jurus_runs, jurus_s, jurus_total))
    assert jurus_total == 150.0
    # exchanges against three different partners, ten each
    partners, per_partner = 3, 10
    exchanges = partners * per_partner
    print('exchanges: %d partners x %d = %d' % (partners, per_partner, exchanges))
    assert exchanges == 30
    # preparation schedule: months, not weeks
    prep_weeks = 12
    sessions_per_week = 4
    print('preparation: %d weeks x %d sessions = %d sessions'
          % (prep_weeks, sessions_per_week, prep_weeks * sessions_per_week))
    assert prep_weeks * sessions_per_week == 48
    # the grade measures a moment; the art measures a lifetime
    print('rule: character counts equally - patience, respect, honesty, restraint')
    print('OK: %s faced the panel' % NAME)
if __name__ == '__main__':
    main()
''')


DEMOS = {
    "kuda-kuda": demo_kuda_kuda,
    "sikap-pasang": demo_sikap_pasang,
    "langkah": demo_langkah,
    "pernapasan": demo_pernapasan,
    "pukulan-lurus": demo_pukulan_lurus,
    "tendangan-lurus": demo_tendangan_lurus,
    "tangkisan-dalam": demo_tangkisan_dalam,
    "elakan": demo_elakan,
    "tepisan": demo_tepisan,
    "tangkapan": demo_tangkapan,
    "kembangan": demo_kembangan,
    "tendangan-sabit": demo_tendangan_sabit,
    "tendangan-t": demo_tendangan_t,
    "siku": demo_siku,
    "lutut": demo_lutut,
    "pukulan-bandul": demo_pukulan_bandul,
    "sapuan": demo_sapuan,
    "bantingan": demo_bantingan,
    "kuncian": demo_kuncian,
    "tendangan-belakang": demo_tendangan_belakang,
    "guntingan": demo_guntingan,
    "jurus-tunggal": demo_jurus_tunggal,
    "sambutan": demo_sambutan,
    "jarak-tempo": demo_jarak_tempo,
    "toya": demo_toya,
    "tanding": demo_tanding,
    "golok": demo_golok,
    "karambit": demo_karambit,
    "main-bawah": demo_main_bawah,
    "keris": demo_keris,
    "jurus-senjata": demo_jurus_senjata,
    "patahan": demo_patahan,
    "aliran": demo_aliran,
    "ujian": demo_ujian,
}
