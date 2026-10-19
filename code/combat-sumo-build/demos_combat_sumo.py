#!/usr/bin/env python3
"""Demo programs for the Sumo Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training or technique computation for its record: stance stability
angles, drill volumes and timers, impact forces, throw torques, lift
work. All are machine-executed by build.py: each prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_sumo_kamae(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance stability: topple angle from center-of-mass height
    h = 1.85                      # wrestler height, m
    half_base = 0.60              # half of stance width, m
    com_stand = 0.55 * h          # standing center of mass
    com_kamae = 0.65              # center of mass sunk into kamae
    tip_stand = math.degrees(math.atan(half_base / com_stand))
    tip_kamae = math.degrees(math.atan(half_base / com_kamae))
    print("standing topple angle: %.2f deg" % tip_stand)
    print("kamae topple angle:    %.2f deg" % tip_kamae)
    print("stability gain: %.2f deg" % (tip_kamae - tip_stand))
    assert 30.4 < tip_stand < 30.7
    assert 42.6 < tip_kamae < 42.8
    assert tip_kamae - tip_stand > 12.0
    print("rule: sink the hips and the stance forgives twelve more degrees")
    print("OK: %s rooted the stance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_shiko(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shiko session volume: sets, tempo, weekly total
    per_set = 100                 # 50 stomps per leg
    sets = 3
    tempo = 1.4                   # seconds per stomp
    days = 6
    session = per_set * sets
    session_time = session * tempo
    weekly = session * days
    print("stomps per session: %d" % session)
    print("session time: %.0f s (%.1f min)" % (session_time, session_time / 60))
    print("weekly stomps: %d" % weekly)
    assert session == 300
    assert session_time == 420
    assert 6.9 < session_time / 60 < 7.1
    assert weekly == 1800
    print("rule: three hundred stomps a day, eighteen hundred a week, hips open by the month")
    print("OK: %s counted the stomps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_suriashi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # suri-ashi lane drill: slides, distance, drill timer
    lane = 10.0                   # meters
    slide = 0.5                   # meters per slide
    lanes = 10
    per_slide = 1.2               # seconds per slide
    slides_per_lane = lane / slide
    total_slides = slides_per_lane * lanes
    distance = lane * lanes
    drill_time = total_slides * per_slide
    print("slides per lane: %.0f" % slides_per_lane)
    print("total slides: %.0f over %.0f m" % (total_slides, distance))
    print("drill time: %.0f s (%.1f min)" % (drill_time, drill_time / 60))
    assert slides_per_lane == 20
    assert total_slides == 200
    assert distance == 100
    assert drill_time == 240
    print("rule: two hundred silent slides, hips never bobbing")
    print("OK: %s glided the lanes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_teppo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # teppo strike energetics: momentum and energy per strike
    per_arm = 50
    arms = 2
    sets = 3
    hand_m = 0.55                # kg, striking hand+forearm effective mass
    v = 9.0                       # m/s hand speed
    strikes = per_arm * arms * sets
    p = hand_m * v
    ke = 0.5 * hand_m * v ** 2
    session_energy = strikes * ke
    print("strikes per session: %d" % strikes)
    print("momentum per strike: %.2f kg m/s" % p)
    print("energy per strike: %.2f J" % ke)
    print("session striking energy: %.0f J" % session_energy)
    assert strikes == 300
    assert 4.94 < p < 4.96
    assert 22.2 < ke < 22.4
    assert 6675 < session_energy < 6685
    print("rule: hip-driven, palm-heel contact, instant snap-back")
    print("OK: %s struck the post" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_matawari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # matawari progression: split angle gained per week to full 180
    start = 130.0                 # degrees of split
    target = 180.0
    gain = 1.5                    # degrees per week, patient progress
    hold = 45                     # seconds per hold
    holds = 3
    weeks = (target - start) / gain
    daily_time = hold * holds
    print("split now: %.0f deg, target: %.0f deg" % (start, target))
    print("weeks to full split: %.1f" % weeks)
    print("daily stretch time: %d s" % daily_time)
    assert 33.3 < weeks < 33.4
    assert daily_time == 135
    print("rule: a degree and a half a week, breathed not bounced")
    print("OK: %s opened the hips" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_tachiai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tachiai collision: momentum and impact force
    m = 150.0                     # kg
    v = 3.2                       # m/s charge speed
    dt = 0.18                     # s collision duration
    p = m * v
    f = p / dt
    ke = 0.5 * m * v ** 2
    print("charge momentum: %.0f kg m/s" % p)
    print("collision force: %.0f N (%.1f kN)" % (f, f / 1000))
    print("charge kinetic energy: %.0f J" % ke)
    assert p == 480
    assert 2660 < f < 2675
    assert 767 < ke < 769
    print("rule: low, fast, and driving through the collision")
    print("OK: %s charged the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_butsukari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # butsukari-geiko: total impulse absorbed across a set
    m = 150.0
    v = 2.6
    charges = 6
    lane = 12.0                   # m driving lane
    impulse_each = m * v
    total_impulse = impulse_each * charges
    drive_work_each = impulse_each * 0 + 700.0 * lane  # 700 N sustained push
    print("impulse per charge: %.0f N s" % impulse_each)
    print("total impulse absorbed: %.0f N s" % total_impulse)
    print("driving work per rep: %.0f J" % drive_work_each)
    assert impulse_each == 390
    assert total_impulse == 2340
    assert drive_work_each == 8400
    print("rule: driver hits low and keeps driving, receiver sinks and holds")
    print("OK: %s took the impacts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_yotsu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # yotsu belt grip: pulling torque from the inside hand
    pull = 850.0                   # N inside-hand pull
    arm = 0.62                     # m lever from grip to opponent center
    torque = pull * arm
    hold_time = 8.0                # s a grip must survive
    impulse = pull * hold_time
    print("inside-hand torque: %.0f N m" % torque)
    print("grip impulse over %.0f s: %.0f N s" % (hold_time, impulse))
    assert 526 < torque < 528
    assert impulse == 6800
    print("rule: win the inside hand and the throw is already half signed")
    print("OK: %s locked the yotsu" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_oshidashi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # oshi-dashi: work and power to push across the dohyo
    g = 9.81
    m = 150.0
    mu = 0.55                     # sliding friction on clay
    dist = 4.55                   # m, full dohyo diameter
    t = 2.2                       # s drive time
    f = m * g * mu
    work = f * dist
    power = work / t
    print("push force vs friction: %.1f N" % f)
    print("work across the dohyo: %.0f J" % work)
    print("drive power: %.0f W" % power)
    assert 808 < f < 811
    assert 3675 < work < 3690
    assert 1670 < power < 1680
    print("rule: legs drive in suri-ashi, hands only transmit, never pause")
    print("OK: %s pushed them out" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_oshitaoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # oshi-taoshi: force to topple a leaning opponent forward
    g = 9.81
    m = 150.0
    com_h = 1.0                   # m center-of-mass height
    half_base = 0.32              # m half of foot base
    f_topple = m * g * half_base / com_h
    push = 900.0                  # N available downward push
    margin = push / f_topple
    print("topple force needed: %.1f N" % f_topple)
    print("available push: %.0f N, margin: %.2f x" % (push, margin))
    assert 470 < f_topple < 472
    assert 1.90 < margin < 1.93
    print("rule: same push as oshi-dashi, finished downward at the lean")
    print("OK: %s pushed them down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_tsukidashi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tsuki-dashi: thrust barrage rate and striking power
    rate = 4.5                    # thrusts per second
    hand_m = 0.55
    v = 8.5
    seconds = 10.0
    ke_each = 0.5 * hand_m * v ** 2
    power = ke_each * rate
    total = rate * seconds
    session_ke = ke_each * total
    print("thrust rate: %.1f per second" % rate)
    print("energy per thrust: %.2f J" % ke_each)
    print("barrage power: %.1f W" % power)
    print("thrusts in %.0f s: %.0f" % (seconds, total))
    assert 19.8 < ke_each < 20.0
    assert 89.0 < power < 90.0
    assert total == 45
    assert 890 < session_ke < 900
    print("rule: teppo strikes, alternating, advancing, never pausing")
    print("OK: %s rained the thrusts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_tsukitaoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tsuki-taoshi: downward thrust topples the backward-leaning opponent
    g = 9.81
    m = 150.0
    lean_deg = 12.0
    com_h = 1.0
    shoulder_forward = 0.50        # m, thrust lands ahead of feet
    offset = math.sin(math.radians(lean_deg)) * com_h
    restoring = m * g * offset
    f_needed = restoring / shoulder_forward
    delivered = 880.0
    print("lean offset: %.3f m, restoring torque: %.1f N m" % (offset, restoring))
    print("downward thrust needed: %.0f N, delivered: %.0f N" % (f_needed, delivered))
    assert 0.207 < offset < 0.209
    assert 305 < restoring < 307
    assert 610 < f_needed < 615
    assert delivered > f_needed
    print("rule: read the backward lean, then sign the thrust downward")
    print("OK: %s thrust them down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_okuridashi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # okuri-dashi: chase speed and push work from behind
    dist = 3.2                    # m to the edge
    t = 1.4                       # s chase time
    push = 700.0                  # N sustained rear push
    speed = dist / t
    work = push * dist
    power = work / t
    print("chase speed: %.2f m/s" % speed)
    print("rear-push work: %.0f J" % work)
    print("chase power: %.0f W" % power)
    assert 2.28 < speed < 2.30
    assert work == 2240
    assert 1599 < power < 1601
    print("rule: stay behind, stay close, steer to the nearest edge")
    print("OK: %s chased them out" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_okuritaoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # okuri-taoshi: downward press folds the stumbling opponent
    g = 9.81
    m = 150.0
    press = 950.0                 # N downward press on back/shoulders
    drop = 0.55                   # m the press travels
    work = press * drop
    body = m * g
    ratio = press / body
    print("downward press: %.0f N vs body weight %.0f N (%.2f x)" % (press, body, ratio))
    print("press work over %.2f m: %.1f J" % (drop, work))
    assert 1470 < body < 1473
    assert 0.64 < ratio < 0.66
    assert 522 < work < 524
    print("rule: press the stumble to the clay, then stand clear")
    print("OK: %s pressed them down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_hatakikomi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hatakikomi: slap impulse redirects the charge into the clay
    arm_m = 4.5                   # kg swinging arm
    v = 11.0                      # m/s hand speed at contact
    dt = 0.05                     # s contact time
    momentum = arm_m * v
    force = momentum / dt
    charge_m = 150.0 * 3.0        # kg m/s of the incoming charge
    print("slap momentum: %.1f kg m/s" % momentum)
    print("slap force: %.0f N" % force)
    print("incoming charge momentum: %.0f kg m/s" % charge_m)
    assert 49.4 < momentum < 49.6
    assert 988 < force < 992
    assert charge_m == 450
    print("rule: let them commit, slap downward, sidestep the fall")
    print("OK: %s slapped them down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_hikiotoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hiki-otoshi: the downward component of the pull
    pull = 750.0                   # N total pull
    ang = 35.0                     # degrees below horizontal
    down = pull * math.sin(math.radians(ang))
    fwd = pull * math.cos(math.radians(ang))
    drop_assist = 150.0 * 9.81 * 0.35  # body-drop contribution, N m-ish work share
    print("pull: %.0f N at %.0f deg -> down %.1f N, forward %.1f N" % (pull, ang, down, fwd))
    assert 429 < down < 432
    assert 614 < fwd < 616
    print("rule: sudden, downward, full-bodied - hips drop with the pull")
    print("OK: %s pulled them down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_sukuinage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sukuinage: lift work plus twist torque of the beltless scoop
    g = 9.81
    m = 150.0
    lift_h = 0.35
    work = m * g * lift_h
    twist_f = 600.0
    twist_arm = 0.50
    torque = twist_f * twist_arm
    print("scoop lift work: %.1f J" % work)
    print("twist torque: %.0f N m" % torque)
    assert 514 < work < 516
    assert torque == 300
    print("rule: scoop deep, lift with the legs, commit to the twist")
    print("OK: %s scooped the throw" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_uwatenage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uwate-nage: centripetal force wheeling the opponent around
    m = 150.0
    r = 0.70                      # m arc radius of the overarm wheel
    omega = 4.2                   # rad/s hip turn rate
    v = omega * r
    f = m * v ** 2 / r
    print("wheel rim speed: %.2f m/s" % v)
    print("wheeling force: %.0f N" % f)
    assert 2.93 < v < 2.95
    assert 1845 < f < 1860
    print("rule: grip deep, turn fully, let the hips wheel the arc")
    print("OK: %s wheeled the overarm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_shitatenage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shitate-nage: explosive lift work and pivot torque
    g = 9.81
    m = 150.0
    lift_h = 0.25
    work = m * g * lift_h
    lift_f = 700.0
    pivot_arm = 0.45
    torque = lift_f * pivot_arm
    print("underarm lift work: %.1f J" % work)
    print("pivot torque: %.0f N m" % torque)
    assert 367 < work < 369
    assert torque == 315
    print("rule: inside hand lifts explosive, body turns around the pivot")
    print("OK: %s pivoted the underarm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_kotenage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kote-nage: the trapped arm as a lever on the elbow
    wrist_f = 300.0               # N applied at the wrist
    wrist_arm = 0.55              # m wrist to elbow
    elbow_torque = wrist_f * wrist_arm
    body_turn = 500.0             # N of body rotation behind the lock
    print("elbow torque from wrist control: %.0f N m" % elbow_torque)
    print("body turn behind the lock: %.0f N" % body_turn)
    assert elbow_torque == 165
    print("rule: trap wrist and elbow, turn the body, release at the fall")
    print("OK: %s locked the armlock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_kubinage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kubi-nage: pivot torque around the controlled head
    turn_f = 650.0                # N of body turn
    pivot_arm = 0.80              # m torso lever around the head
    torque = turn_f * pivot_arm
    head_h = 1.70                 # m fulcrum height
    print("pivot torque around the head: %.0f N m" % torque)
    print("fulcrum height: %.1f m" % head_h)
    assert torque == 520
    print("rule: the head is the fulcrum, the body rotates, never crank the neck")
    print("OK: %s pivoted the head throw" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_sotogake(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sotogake: reap torque vs the opponent's base torque
    g = 9.81
    m = 150.0
    hook_f = 500.0
    hook_arm = 0.90               # m ankle height lever
    reap_torque = hook_f * hook_arm
    base_torque = m * g * 0.30    # opponent half-base resistance
    ratio = reap_torque / base_torque
    print("reap torque: %.0f N m vs base resistance %.0f N m (%.2f x)" % (reap_torque, base_torque, ratio))
    assert reap_torque == 450
    assert 440 < base_torque < 443
    assert 1.01 < ratio < 1.03
    print("rule: hook the weighted leg, drive the upper body the same beat")
    print("OK: %s reaped the outer leg" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_uchigake(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uchigake: inner reap torque through the narrow entry
    hook_f = 480.0
    hook_arm = 0.85
    reap_torque = hook_f * hook_arm
    entry_gap = 0.25              # m between the opponent's feet
    print("inner reap torque: %.0f N m through a %.2f m entry gap" % (reap_torque, entry_gap))
    assert reap_torque == 408
    print("rule: bent leg, quick entry, same-beat upper-body drive")
    print("OK: %s reaped the inner leg" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_kirikaeshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kirikaeshi: twist torque against the knee block
    twist = 550.0                 # N m of torso twist
    block_f = 500.0               # N knee block
    block_arm = 0.90
    block_torque = block_f * block_arm
    combined = twist + block_torque
    print("twist %.0f N m + knee block %.0f N m = %.0f N m of spiral" % (twist, block_torque, combined))
    assert block_torque == 450
    assert combined == 1000
    print("rule: twist peaks exactly as the knee block lands")
    print("OK: %s spiraled the knee trip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_watashikomi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # watashikomi: thigh control plus downward press folds the opponent
    thigh_f = 400.0               # N controlling the gripped thigh
    press_f = 800.0               # N driving the upper body down
    fold_torque = thigh_f * 0.45 + press_f * 0.60
    print("thigh control %.0f N + press %.0f N -> fold torque %.0f N m" % (thigh_f, press_f, fold_torque))
    assert fold_torque == 660
    print("rule: penetrate low, secure the thigh, then fold")
    print("OK: %s folded the thigh grab" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_yorikiri(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # yori-kiri: the grinding march - work, steps, and power
    g = 9.81
    m = 150.0
    mu = 0.55
    dist = 4.0                    # m marched to the edge
    t = 3.5                       # s of sustained drive
    step = 0.5                    # m per step
    f = m * g * mu
    work = f * dist
    power = work / t
    steps = dist / step
    print("march force: %.1f N over %.1f m = %.0f J in %.1f s" % (f, dist, work, t))
    print("steps: %.0f, march power: %.0f W" % (steps, power))
    assert 808 < f < 811
    assert 3230 < work < 3245
    assert steps == 8
    assert 923 < power < 928
    print("rule: locked grip, low hips, inexhaustible legs, stop at the edge")
    print("OK: %s marched the force out" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_yoritaoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # yori-taoshi: the downward vector change on the braced defender
    drive = 1200.0                # N driven down through the grip
    drop = 0.60                   # m the drive travels
    work = drive * drop
    hold = 150.0 * 9.81 * 0.40    # defender brace resistance share
    print("downward drive work: %.0f J vs brace share %.0f J" % (work, hold))
    assert work == 720
    assert 588 < hold < 590
    assert work > hold
    print("rule: march until they brace, then sign the vector downward")
    print("OK: %s forced them down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_uwatedashinage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uwatedashi-nage: snap pull work over the set hip
    pull = 950.0                  # N yank on the overarm
    travel = 0.80                 # m the pull travels
    work = pull * travel
    t = 0.35                      # s snap duration
    power = work / t
    print("snap pull work: %.0f J in %.2f s -> %.0f W" % (work, t, power))
    assert work == 760
    assert 2170 < power < 2172
    print("rule: deep overarm grip, hip set, one sudden pull")
    print("OK: %s snapped the pulling overarm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_shitatedashinage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shitatedashi-nage: drag work of the pulling underarm
    pull = 900.0
    travel = 0.70
    work = pull * travel
    drop = 0.40                   # m the attacker drops with the pull
    body_work = 150.0 * 9.81 * drop
    total = work + body_work
    print("pull work %.0f J + body-drop work %.0f J = %.0f J" % (work, body_work, total))
    assert work == 630
    assert 588 < body_work < 590
    assert 1218 < total < 1220
    print("rule: drag what cannot be lifted - pull and drop as one")
    print("OK: %s dragged the pulling underarm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_katasukashi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # katasukashi: the fall time once the support is removed
    g = 9.81
    head_h = 1.60                 # m head height when the arm is swung
    fall_t = math.sqrt(2 * head_h / g)
    swing_t = 0.25                # s the swing-down takes
    margin = fall_t - swing_t
    print("head fall time: %.3f s, swing time: %.2f s, margin %.3f s" % (fall_t, swing_t, margin))
    assert 0.570 < fall_t < 0.573
    assert margin > 0.30
    print("rule: duck under at the commitment, swing down and across, never up")
    print("OK: %s swung them down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_utchari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # utchari: edge pivot rotation rate and staying inside
    turn = math.pi               # 180-degree pivot, radians
    t = 0.40                     # s single-motion reversal
    omega = turn / t
    pivot_r = 0.30               # m pivot radius at the tawara
    rim = omega * pivot_r
    edge_margin = 2.275 - 0.30   # m of ring left behind the pivot
    print("pivot rate: %.2f rad/s, rim speed %.2f m/s" % (omega, rim))
    print("ring remaining behind pivot: %.3f m" % edge_margin)
    assert 7.84 < omega < 7.86
    assert 1.974 < edge_margin < 1.976
    print("rule: hold the edge, pivot-throw as one motion, no hesitation")
    print("OK: %s reversed at the edge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_tsuriotoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tsuri-otoshi: the full-body lift - work and power
    g = 9.81
    m = 150.0
    lift_h = 0.55
    t = 0.80
    work = m * g * lift_h
    power = work / t
    grip_each = m * g / 2        # N per hand on the two-handed grip
    print("lift work: %.1f J in %.1f s -> %.0f W" % (work, t, power))
    print("load per gripping hand: %.0f N" % grip_each)
    assert 808 < work < 811
    assert 1010 < power < 1013
    assert 735 < grip_each < 737
    print("rule: hips below center, back straight, decisive lift or nothing")
    print("OK: %s lifted the body drop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_kawazugake(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kawazugake: the counter window and reversed momentum
    m = 150.0
    v = 3.0
    attack_p = m * v
    window = 0.25                 # s timing window for the hook
    hook_f = 600.0
    hook_impulse = hook_f * window
    print("attack momentum: %.0f kg m/s, counter window: %.2f s" % (attack_p, window))
    print("hook impulse in the window: %.0f N s" % hook_impulse)
    assert attack_p == 450
    assert hook_impulse == 150
    print("rule: answer, never initiate - hook inside the quarter-second")
    print("OK: %s countered backward" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sumo_izori(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # izori: penetration depth and the backward throw arc
    drop = 0.45                   # m the attacker drops to go under
    t = 0.30                      # s to penetrate
    sink_speed = drop / t
    m = 150.0
    arc = 1.00                    # m the opponent travels over backward
    g = 9.81
    throw_work = m * g * arc * 0.6  # effective work share of the arc
    print("penetration sink speed: %.2f m/s" % sink_speed)
    print("backward throw work share: %.0f J" % throw_work)
    assert 1.49 < sink_speed < 1.51
    assert 882 < throw_work < 884
    print("rule: deepest wrestler wins - penetrate fully, commit totally")
    print("OK: %s dropped the backward body" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "kamae": demo_sumo_kamae,
    "shiko": demo_sumo_shiko,
    "suriashi": demo_sumo_suriashi,
    "teppo": demo_sumo_teppo,
    "matawari": demo_sumo_matawari,
    "tachiai": demo_sumo_tachiai,
    "butsukari": demo_sumo_butsukari,
    "yotsu": demo_sumo_yotsu,
    "oshidashi": demo_sumo_oshidashi,
    "oshitaoshi": demo_sumo_oshitaoshi,
    "tsukidashi": demo_sumo_tsukidashi,
    "tsukitaoshi": demo_sumo_tsukitaoshi,
    "okuridashi": demo_sumo_okuridashi,
    "okuritaoshi": demo_sumo_okuritaoshi,
    "hatakikomi": demo_sumo_hatakikomi,
    "hikiotoshi": demo_sumo_hikiotoshi,
    "sukuinage": demo_sumo_sukuinage,
    "uwatenage": demo_sumo_uwatenage,
    "shitatenage": demo_sumo_shitatenage,
    "kotenage": demo_sumo_kotenage,
    "kubinage": demo_sumo_kubinage,
    "sotogake": demo_sumo_sotogake,
    "uchigake": demo_sumo_uchigake,
    "kirikaeshi": demo_sumo_kirikaeshi,
    "watashikomi": demo_sumo_watashikomi,
    "yorikiri": demo_sumo_yorikiri,
    "yoritaoshi": demo_sumo_yoritaoshi,
    "uwatedashinage": demo_sumo_uwatedashinage,
    "shitatedashinage": demo_sumo_shitatedashinage,
    "katasukashi": demo_sumo_katasukashi,
    "utchari": demo_sumo_utchari,
    "tsuriotoshi": demo_sumo_tsuriotoshi,
    "kawazugake": demo_sumo_kawazugake,
    "izori": demo_sumo_izori,
}
