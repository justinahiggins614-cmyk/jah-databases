#!/usr/bin/env python3
"""Demo programs for the Capoeira Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record (cadence calculators, drill timers,
biomechanics estimates). All are machine-executed by build.py before
commit: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cc_ginga(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ginga cadence: berimbau toque at 96 bpm, one full sway cycle per 2 beats
    bpm = 96.0
    beats_per_cycle = 2.0
    cycles_per_min = bpm / beats_per_cycle
    session_min = 5.0
    cycles = cycles_per_min * session_min
    steps = cycles * 2.0  # two weight shifts per cycle
    print("tempo: %.0f bpm -> %.1f sway cycles/min" % (bpm, cycles_per_min))
    print("5-minute session: %.0f cycles, %.0f weight shifts" % (cycles, steps))
    assert 47.9 < cycles_per_min < 48.1
    assert 239.9 < cycles < 240.1
    assert 479.9 < steps < 480.1
    # swap interval: how long each guard side holds
    swap_s = 60.0 / cycles_per_min
    print("guard swap every %.2f s" % swap_s)
    assert 1.24 < swap_s < 1.26
    print("rule: the sway never stops - stillness is the one forbidden position")
    print("OK: %s drilled the pulse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guard coverage: forearm 0.45 m held vertical at 0.35 m from face
    forearm = 0.45
    dist = 0.35
    cover_rad = math.atan(forearm / 2.0 / dist)
    cover_deg = math.degrees(cover_rad) * 2.0
    print("forearm %.2f m at %.2f m covers %.1f degrees of head arc" % (forearm, dist, cover_deg))
    assert 64.0 < cover_deg < 66.0
    # two-minute round at 48 cycles/min: guard swaps per round
    swaps = 48.0 * 2.0
    print("2-minute round: %.0f guard swaps" % swaps)
    assert 95.9 < swaps < 96.1
    # late swap exposure: 0.2 s late at kick speed 8 m/s
    exposed_m = 8.0 * 0.2
    print("0.2 s late swap exposes %.1f m of travel to the kick" % exposed_m)
    assert 1.59 < exposed_m < 1.61
    print("rule: the guard swaps on the weight shift - never late")
    print("OK: %s sealed the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_balanco(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 70 kg fighter, 60/40 loading through the sway
    mass = 70.0
    g = 9.81
    front = mass * 0.60 * g
    back = mass * 0.40 * g
    print("70 kg fighter: front leg %.0f N, back leg %.0f N" % (front, back))
    assert 411.9 < front < 412.1
    assert 274.6 < back < 274.8
    # transfer: shifting 20%% of body weight across in 0.6 s (half cycle)
    shift_kg = mass * 0.20
    shift_rate = shift_kg / 0.6
    print("weight transfer rate: %.1f kg/s" % shift_rate)
    assert 23.32 < shift_rate < 23.34
    # silent transfer test: foot pressure noise threshold ~5 N variation
    print("loaded leg stays the weapon leg; light leg stays the escape leg")
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_cocorinha(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # drop: head from 1.60 m standing to 0.90 m in the squat
    g = 9.81
    drop = 1.60 - 0.90
    t_fall = math.sqrt(2.0 * drop / g)
    print("head drop %.2f m in %.3f s (free-fall)" % (drop, t_fall))
    assert 0.699 < drop < 0.701
    assert 0.377 < t_fall < 0.379
    # high kick at 8 m/s needs 0.25 s to cross the last 2 m:
    # the dodge is slower, so it must start on the read, not the launch
    kick_time = 2.0 / 8.0
    head_start = t_fall - kick_time
    print("kick crosses 2 m in %.3f s; dodge needs %.3f s head start" % (kick_time, head_start))
    assert 0.127 < head_start < 0.129
    print("read beats reaction: start the drop on the hip tell")
    # ten reps per side drill volume
    print("drill: 10 reps/side, guard arm up every rep")
    print("OK: %s ducked the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_esquiva_lateral(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # head must clear 0.25 m off the center line in 0.30 s
    clear = 0.25
    t = 0.30
    v = clear / t
    print("lateral head speed needed: %.2f m/s" % v)
    assert 0.83 < v < 0.84
    # lean angle for a 1.70 m fighter leaning from the hips
    height = 1.70
    ang = math.degrees(math.asin(clear / height))
    print("hip-initiated lean angle: %.1f degrees" % ang)
    assert 8.4 < ang < 8.6
    # three-attack drill without moving the feet
    print("drill: slip 3 straight attacks, feet planted, eyes locked")
    print("rule: lean from the hips with coiled legs, never from the neck")
    print("OK: %s slipped the lane" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_esquiva_baixa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # diagonal drop: center of mass falls 0.80 m to hand-touch depth
    g = 9.81
    drop = 0.80
    t = math.sqrt(2.0 * drop / g)
    print("drop %.2f m in %.3f s" % (drop, t))
    assert 0.403 < t < 0.405
    # three exits drilled 5 times per side
    exits = 3 * 5 * 2
    print("exit drill volume: %d reps (rise, roll, negativa x sides)" % exits)
    assert exits == 30  # int count
    # hand load: 70 kg fighter, hand takes ~25%% at the bottom instant
    hand_n = 70.0 * g * 0.25
    print("floor hand peak load ~%.0f N" % hand_n)
    assert 171.6 < hand_n < 171.8
    print("rule: choose the exit on the way down, not after landing")
    print("OK: %s took the low road" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_meia_lua_frente(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crescent arc: leg radius 0.90 m sweeping 120 degrees
    r = 0.90
    arc = r * math.radians(120.0)
    print("kick arc length: %.3f m" % arc)
    assert 1.884 < arc < 1.886
    # delivered in 0.25 s -> foot speed
    v = arc / 0.25
    print("foot speed: %.2f m/s" % v)
    assert 7.53 < v < 7.55
    # return arc doubles the threat: total path per kick
    total = arc * 2.0
    print("out-and-back path: %.3f m of threat per kick" % total)
    assert 3.768 < total < 3.772
    # ten slow technical reps per leg before speed
    print("drill: 10 slow arcs/leg (hip turnover), then 10 at speed on the bag")
    print("rule: power from hip turnover, never from a knee flick")
    print("OK: %s drew the crescent" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_pisao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stomp: leg+body drop 0.40 m driving the sole down
    g = 9.81
    drop = 0.40
    v = math.sqrt(2.0 * g * drop)
    print("sole impact speed: %.2f m/s" % v)
    assert 2.799 < v < 2.803
    # effective striking mass ~35 kg (leg + committed torso)
    m = 35.0
    momentum = m * v
    print("momentum: %.1f kg m/s" % momentum)
    assert 97.9 < momentum < 98.2
    # stopped in 0.10 s on the bag -> average force
    force = momentum / 0.10
    print("average force over 0.10 s: %.0f N" % force)
    assert 979.0 < force < 982.0
    print("rule: stamp THROUGH the target, rechamber instantly")
    print("OK: %s drove the stamp" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_bloqueio(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crossed X meets a 500 N kick at 30 degrees off square
    incoming = 500.0
    ang = math.radians(30.0)
    absorbed = incoming * math.cos(ang)
    deflected = incoming * math.sin(ang)
    print("500 N kick at 30 deg: %.0f N into the X, %.0f N deflected offline" % (absorbed, deflected))
    assert 432.9 < absorbed < 433.1
    assert 249.9 < deflected < 250.1
    # offline step of 0.30 m at 45 degrees bleeds more
    print("pair every block with an offline step - the block redirects, never walls")
    # conditioning: 10 light taps/session, +10%%/week for 8 weeks
    taps = 10.0 * (1.10 ** 8)
    print("8-week progression reaches %.0f taps/session equivalent" % taps)
    assert 21.3 < taps < 21.5
    print("OK: %s crossed the arms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_bencao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # push kick: sole drives 0.50 m through the target in 0.20 s
    dist = 0.50
    t = 0.20
    v = dist / t
    print("push speed: %.1f m/s" % v)
    assert 2.49 < v < 2.51
    # 70 kg partner displaced: impulse from 40 kg effective mass
    m = 40.0
    impulse = m * v
    print("impulse: %.0f N s" % impulse)
    assert 99.9 < impulse < 100.1
    # partner slides back: v_partner = impulse / 70
    vp = impulse / 70.0
    print("70 kg partner pushed back at %.2f m/s" % vp)
    assert 1.42 < vp < 1.44
    print("rule: full hip extension - shove the door, do not snap at it")
    print("OK: %s gave the blessing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_ponteira(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shin whip: knee extends at 12 rad/s, shin 0.45 m
    omega = 12.0
    shin = 0.45
    v = omega * shin
    print("foot speed from shin whip: %.1f m/s" % v)
    assert 5.39 < v < 5.41
    # snap-back must match: 90-degree extension and return in 0.15 s total
    total_ang = math.radians(180.0)
    t = 0.15
    avg_omega = total_ang / t
    print("out-and-back average angular speed: %.1f rad/s" % avg_omega)
    assert 20.93 < avg_omega < 20.95
    # ten snap cycles per leg, thigh still
    print("drill: 10 chamber-extend-rechamber cycles/leg, thigh frozen")
    print("rule: the thigh stays, the shin flies, the foot comes home")
    print("OK: %s snapped the point" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_joelhada(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee rises 0.50 m in 0.25 s driven by the hips
    rise = 0.50
    t = 0.25
    v = rise / t
    print("knee rise speed: %.1f m/s" % v)
    assert 1.99 < v < 2.01
    # hip drive: 25 kg effective mass behind the knee
    m = 25.0
    ke = 0.5 * m * v * v
    print("knee kinetic energy: %.1f J" % ke)
    assert 49.9 < ke < 50.1
    # ten knees per side on the bag
    print("drill: 10/side on the bag, hand-pull plus knee as one motion")
    print("rule: stand tall into it - the hips deliver, the knee is the point")
    print("OK: %s drove the knee" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "ginga": demo_cc_ginga,
    "guard": demo_cc_guard,
    "balanco": demo_cc_balanco,
    "cocorinha": demo_cc_cocorinha,
    "esquiva_lateral": demo_cc_esquiva_lateral,
    "esquiva_baixa": demo_cc_esquiva_baixa,
    "meia_lua_frente": demo_cc_meia_lua_frente,
    "pisao": demo_cc_pisao,
    "bloqueio_cruzado": demo_cc_bloqueio,
    "bencao": demo_cc_bencao,
    "ponteira": demo_cc_ponteira,
    "joelhada": demo_cc_joelhada,
}


def demo_cc_queixada(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross-step 0.60 m, then leg arc: radius 0.95 m through 200 degrees
    step = 0.60
    arc = 0.95 * math.radians(200.0)
    path = step + arc
    print("cross-step %.2f m + arc %.2f m = %.2f m of travel" % (step, arc, path))
    assert 3.315 < arc < 3.317
    assert 3.915 < path < 3.917
    # full commitment: spin-through in 0.70 s
    spin_t = 0.70
    omega = math.radians(360.0) / spin_t
    print("spin rate: %.2f rad/s" % omega)
    assert 8.97 < omega < 8.98
    # ten slow rotations per side before bag contact
    print("drill: 10 slow cross-step rotations/side, then 10 on the bag")
    print("rule: the step disguises, the rotation delivers - commit or do not throw")
    print("OK: %s crossed and spun" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_armada(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full 360 spin delivered in 0.60 s
    spin_t = 0.60
    omega = math.radians(360.0) / spin_t
    print("spin rate: %.2f rad/s" % omega)
    assert 10.47 < omega < 10.48
    # leg tip at 0.95 m radius
    v = omega * 0.95
    print("foot speed at 0.95 m radius: %.2f m/s" % v)
    assert 9.94 < v < 9.96
    # head spot: head completes its turn in the first 0.25 s
    head_omega = math.radians(360.0) / 0.25
    print("head spot rate: %.1f rad/s - the head finds the target first" % head_omega)
    assert 25.12 < head_omega < 25.14
    # ten spotting pivots per direction before adding the kick
    print("drill: 10 spotting pivots/direction, then 10 armadas/side on the bag")
    print("rule: head spots first, arms drive, leg whips last")
    print("OK: %s spun the inside crescent" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_martelo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # leg (~10 kg) raised 1.80 m: potential energy becomes the hammer
    g = 9.81
    m_leg = 10.0
    h = 1.80
    pe = m_leg * g * h
    print("hammer energy at full chamber: %.1f J" % pe)
    assert 176.5 < pe < 176.7
    # drop speed at contact
    v = math.sqrt(2.0 * g * h)
    print("heel drop speed: %.2f m/s" % v)
    assert 5.941 < v < 5.945
    # plus hip drive adds ~30%% more
    total = pe * 1.30
    print("with hip drive: ~%.0f J through the target" % total)
    assert 229.4 < total < 229.7
    print("drill: 10 slow raise-and-drop reps/leg, then 10 driving reps on the bag")
    print("rule: gravity is the engine - raise high, drop everything")
    print("OK: %s brought the hammer down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_rabo_de_arraia(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low spin: heel circle radius 1.00 m, full rotation in 0.80 s
    r = 1.00
    circ = 2.0 * math.pi * r
    spin_t = 0.80
    v = circ / spin_t
    print("heel sweep circle %.2f m in %.2f s -> %.2f m/s" % (circ, spin_t, v))
    assert 6.282 < circ < 6.284
    assert 7.853 < v < 7.855
    # sweep zone: annulus between 0.70 m and 1.00 m radius
    zone = math.pi * (1.00 ** 2 - 0.70 ** 2)
    print("sweep danger zone: %.2f square meters at ankle height" % zone)
    assert 1.601 < zone < 1.603
    # ten no-contact low spins per direction first
    print("drill: 10 low spins/direction (leg relaxed), then low-pad contact")
    print("rule: the spin whips the tail - tension kills it")
    print("OK: %s flicked the stingray tail" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_au(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cartwheel: hands plant 0.50 m apart, full rotation in 1.20 s
    hand_gap = 0.50
    rot_t = 1.20
    omega = math.radians(360.0) / rot_t
    print("rotation rate: %.2f rad/s" % omega)
    assert 5.235 < omega < 5.237
    # lateral travel: 1.60 m per au
    travel = 1.60
    print("lateral escape distance: %.1f m per au" % travel)
    assert 1.599 < travel < 1.601
    # eyes-on-partner check: head turns to track through the rotation
    print("drill: 10/side open floor, then kick out of the landing (meia-lua)")
    # kick-out window: legs pass the top between 0.45 and 0.75 s
    window = 0.75 - 0.45
    print("kick-out window mid-rotation: %.2f s" % window)
    assert 0.299 < window < 0.301
    print("rule: combat cartwheel - dodge, watch, land ready to kick")
    print("OK: %s turned the cartwheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_role(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low spin: 360 degrees in 1.00 s around the planted hand
    spin_t = 1.00
    omega = math.radians(360.0) / spin_t
    print("ground spin rate: %.3f rad/s" % omega)
    assert 6.282 < omega < 6.284
    # chained: 5 roles without standing = 5.0 s of continuous low flow
    chain = 5 * spin_t
    print("5 chained roles: %.1f s of unbroken ground flow" % chain)
    assert 4.99 < chain < 5.01
    # circling: each role advances ~0.80 m around the partner
    circle = 5 * 0.80
    print("5 roles circle %.1f m around the partner" % circle)
    assert 3.99 < circle < 4.01
    # ten singles per direction before chaining
    print("drill: 10 singles/direction, then 10 chained pairs")
    print("rule: the hand is the axle, the hips commit, the spin never stalls")
    print("OK: %s spun the low wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_negativa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hold progression: 30 s holds, adding 10 s/week for 8 weeks
    start = 30.0
    prog = [start + 10.0 * w for w in range(9)]
    print("8-week hold progression: %.0f s -> %.0f s" % (prog[0], prog[-1]))
    assert 29.99 < prog[0] < 30.01
    assert 109.99 < prog[-1] < 110.01
    # weekly volume: 3 sessions x 2 sides x hold
    vol_w1 = 3 * 2 * prog[0]
    vol_w8 = 3 * 2 * prog[-1]
    print("weekly hold volume: %.0f s (wk1) -> %.0f s (wk8)" % (vol_w1, vol_w8))
    assert 179.99 < vol_w1 < 180.01
    assert 659.99 < vol_w8 < 660.01
    # three launches x 5 reps x 2 sides
    launches = 3 * 5 * 2
    print("launch drill: %d reps (sweep, kick, rise)" % launches)
    assert launches == 30  # int count
    print("rule: coil, never collapse - the fortress is loaded")
    print("OK: %s held the fortress" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_cabecada(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # short clinch drive: head+neck mass ~6 kg at 3.0 m/s
    m = 6.0
    v = 3.0
    momentum = m * v
    print("headbutt momentum: %.1f kg m/s" % momentum)
    assert 17.99 < momentum < 18.01
    # absorbed over 0.05 s on the shield
    force = momentum / 0.05
    print("average force over 0.05 s: %.0f N" % force)
    assert 359.9 < force < 360.1
    # crown vs face: crown bone ~2x thicker - the tuck is the safety
    print("contact zone: forehead crown only, chin tucked, neck never snaps")
    # ten touch-contact drives per session on the shield
    print("drill: 10 touch drives/session on the body shield - bags for power")
    print("rule: strictest safety in the database - tuck, crown, shield only")
    print("OK: %s headed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_bananeira(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inverted balance: 70 kg stacked over hands, finger correction torque
    mass = 70.0
    g = 9.81
    weight = mass * g
    print("handstand load: %.0f N over two hands" % weight)
    assert 686.6 < weight < 686.8
    # 2 cm drift corrected by fingertip pressure over 0.10 s
    drift = 0.02
    t_correct = 0.10
    print("finger correction: %.2f m drift fixed in %.2f s" % (drift, t_correct))
    # hold progression: 5 s wall-assisted to 60 s freestanding over 12 weeks
    start, end, weeks = 5.0, 60.0, 12.0
    weekly_gain = (end - start) / weeks
    print("hold progression: %.0f s -> %.0f s (+%.2f s/week)" % (start, end, weekly_gain))
    assert 4.58 < weekly_gain < 4.59
    # five wall kick-ups per session
    print("drill: 5 wall kick-ups/session, then freestanding attempts")
    print("rule: stack straight, steer with the fingers")
    print("OK: %s grew the banana tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_vingativa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lever: hook at ankle (0.10 m) vs body push at hip (0.90 m)
    hook_h = 0.10
    push_h = 0.90
    advantage = push_h / hook_h
    print("lever advantage: %.0f to 1" % advantage)
    assert 8.99 < advantage < 9.01
    # 70 kg partner: toppling needs their center past the hooked foot
    # push force to tip: weight * (base 0.15 m / push height 0.90 m)
    mass = 70.0
    g = 9.81
    tip_force = mass * g * (0.15 / 0.90)
    print("force to tip 70 kg partner: %.1f N" % tip_force)
    assert 114.4 < tip_force < 114.6
    # with the hook removing the base, far less suffices - leverage, not muscle
    print("the hook removes the support; the lever does the rest")
    # ten walk-throughs per side before speed
    print("drill: 10 walk-throughs/side, guide every fall")
    print("rule: position beats strength - hook, lever, guide")
    print("OK: %s turned the tables" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_chapa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # side thrust: leg extends 0.95 m laterally in 0.22 s
    ext = 0.95
    t = 0.22
    v = ext / t
    print("lateral foot speed: %.2f m/s" % v)
    assert 4.317 < v < 4.319
    # support pivot: 90 degrees during the thrust
    pivot = math.radians(90.0) / t
    print("support-foot pivot rate: %.2f rad/s" % pivot)
    assert 7.139 < pivot < 7.141
    # thrust work: 30 kg effective leg mass
    m = 30.0
    ke = 0.5 * m * v * v
    print("thrust energy: %.1f J" % ke)
    assert 279.69 < ke < 279.71
    # ten slow reps per side, then ten driving reps on the bag
    print("drill: 10 slow chamber-pivot-thrust/side, then 10 driving")
    print("rule: pivot turns the body side-on - no pivot, half power")
    print("OK: %s pressed the slab" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_macaquinho(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one-hand plant supports the body for 0.30 s of the 0.90 s flip
    flip_t = 0.90
    support_t = 0.30
    share = support_t / flip_t
    print("single hand carries the flip for %.0f%% of the rotation" % (share * 100.0))
    assert 33.32 < share * 100.0 < 33.34
    # 70 kg on one hand at peak: full body weight through the wrist
    peak_n = 70.0 * 9.81
    print("peak single-hand load: %.0f N" % peak_n)
    assert 686.6 < peak_n < 686.8
    # tight tuck vs au spread: rotation radius 0.60 m vs 0.90 m
    print("compact radius 0.60 m spins faster than the au spread 0.90 m")
    ratio = (0.90 / 0.60) ** 2
    print("tuck spins %.2fx faster (angular momentum)" % ratio)
    assert 2.249 < ratio < 2.251
    # ten per side on mats before open floor
    print("drill: 10/side on mats - plant timing is everything")
    print("rule: plant late and you clip; plant early and you stall")
    print("OK: %s flipped the monkey" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "queixada": demo_cc_queixada,
    "armada": demo_cc_armada,
    "martelo": demo_cc_martelo,
    "rabo_de_arraia": demo_cc_rabo_de_arraia,
    "au": demo_cc_au,
    "role": demo_cc_role,
    "negativa": demo_cc_negativa,
    "cabecada": demo_cc_cabecada,
    "bananeira": demo_cc_bananeira,
    "vingativa": demo_cc_vingativa,
    "chapa": demo_cc_chapa,
    "macaquinho": demo_cc_macaquinho,
})


def demo_cc_meia_lua_compasso(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # compass: heel draws a full circle, radius 1.00 m, in 1.00 s
    r = 1.00
    circ = 2.0 * math.pi * r
    t = 1.00
    v = circ / t
    print("heel circle %.3f m in %.2f s -> %.3f m/s" % (circ, t, v))
    assert 6.282 < circ < 6.284
    assert 6.282 < v < 6.284
    # whole-body rotation behind the heel: 70 kg at heel speed
    ke = 0.5 * 12.0 * v * v  # ~12 kg effective leg mass
    print("heel kinetic energy: %.1f J" % ke)
    assert 236.8 < ke < 237.1
    # danger radius: 1.00 m heel + 0.30 m body = clear 1.30 m
    clear = r + 0.30
    print("keep partners outside %.1f m radius" % clear)
    assert 1.299 < clear < 1.301
    # ten slow arcs per side before bag contact
    print("drill: 10 slow arcs/side, hands planted solid, head tucked")
    print("rule: the hands are the pivot - the heel draws the circle")
    print("OK: %s drew the compass" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_s_dobrado(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # S-fold shrinks the body profile: 1.70 m standing to 0.90 m folded
    tall = 1.70
    folded = 0.90
    reduction = (tall - folded) / tall * 100.0
    print("profile reduction: %.1f%%" % reduction)
    assert 47.05 < reduction < 47.07
    # thread through a 0.40 m gap at 0.50 m/s fold speed
    gap = 0.40
    v = 0.50
    t = gap / v
    print("thread %.2f m gap in %.2f s" % (gap, t))
    assert 0.799 < t < 0.801
    # one breath, one motion: exhale 4.0 s covers fold+thread+unfold
    print("one breath (%.1f s) carries the whole escape" % 4.0)
    # ten S-folds per side on open floor before pressure drilling
    print("drill: 10 S-folds/side, then thread out under light pressure")
    print("rule: lead with the hips, head last - fold, thread, emerge moving")
    print("OK: %s folded the S" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_parafuso(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jump 0.50 m -> airtime for the full 360
    g = 9.81
    h = 0.50
    airtime = 2.0 * math.sqrt(2.0 * h / g)
    print("jump %.2f m gives %.3f s of airtime" % (h, airtime))
    assert 0.638 < airtime < 0.640
    # required spin rate for 360 degrees in that airtime
    omega = math.radians(360.0) / airtime
    print("required spin rate: %.2f rad/s" % omega)
    assert 9.82 < omega < 9.84
    # tight tuck halves the moment of inertia vs extended
    print("tuck tight: the spin only completes tucked")
    # kick extends at the 3/4 mark
    kick_t = airtime * 0.75
    print("kick extends at %.3f s into the jump" % kick_t)
    assert 0.478 < kick_t < 0.480
    # ten jump-tuck spins without the kick first
    print("drill: 10 jump-tuck spins, then add the extension on a high pad")
    print("rule: height first, tuck second, kick last")
    print("OK: %s drove the corkscrew" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_mortal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jump 0.60 m -> airtime for the backward rotation
    g = 9.81
    h = 0.60
    airtime = 2.0 * math.sqrt(2.0 * h / g)
    print("jump %.2f m gives %.3f s of airtime" % (h, airtime))
    assert 0.699 < airtime < 0.701
    # violent tuck: rotation rate needed for the full flip
    omega = math.radians(360.0) / airtime
    print("tuck rotation rate: %.2f rad/s" % omega)
    assert 8.98 < omega < 9.00
    # four stages, ten clean reps each = 40 gated reps before solo
    gated = 4 * 10
    print("gated progression: %d clean reps before solo on mats" % gated)
    assert gated == 40  # int count
    # landing absorption: knees bend 0.35 m to absorb the drop
    print("land soft: 0.35 m of knee bend absorbs the return")
    print("rule: jump UP not back, tuck violently, never tired, never cold, never unspotted")
    print("OK: %s completed the mortal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_au_sem_mao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lateral leap 1.50 m carrying the full airborne rotation in 0.90 s
    dist = 1.50
    t = 0.90
    v = dist / t
    print("takeoff drive: %.2f m/s lateral" % v)
    assert 1.666 < v < 1.668
    # rotation rate matches the grounded au: 360 deg in 0.90 s
    omega = math.radians(360.0) / t
    print("airborne rotation rate: %.3f rad/s" % omega)
    assert 6.981 < omega < 6.983
    # rigid split: body holds a 1.70 m star for the whole flight
    print("hold the star: any fold mid-air collapses the arc")
    # progression stages: au -> one-hand -> delayed-touch -> no-hands
    stages = 4
    reps = stages * 10
    print("progression: %d stages x 10 reps = %d gated reps" % (stages, reps))
    assert reps == 40  # int count
    print("rule: drive hard, hold the split rigid, land running")
    print("OK: %s flew without hands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_chamada(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the slow approach: 3.0 m at 0.50 m/s of deliberate walking
    dist = 3.0
    v = 0.50
    t = dist / v
    print("ritual approach: %.1f s of composure" % t)
    assert 5.99 < t < 6.01
    # the break: explode from stillness - 0 to kick in 0.40 s
    break_t = 0.40
    print("the break: stillness to attack in %.2f s" % break_t)
    assert 0.399 < break_t < 0.401
    # tension ratio: 6 s of waiting per 0.4 s of action = 15:1
    ratio = t / break_t
    print("waiting-to-action ratio: %.0f to 1 - the wait IS the technique" % ratio)
    assert 14.9 < ratio < 15.1
    # ten slow call-and-answer approaches before practicing the break
    print("drill: 10 slow approaches, composure unbroken, then clean breaks")
    print("rule: answer every call; break decisively; never flinch")
    print("OK: %s answered the call" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_malicia(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two-beat trap: show the weakness twice, punish on the third
    # partner takes the bait 70%% of the time after two shows
    p_bait = 0.70
    # over 10 traps, expected successes
    traps = 10
    expected = traps * p_bait
    print("10 two-beat traps at 70%% bait rate: %.1f expected successes" % expected)
    assert 6.99 < expected < 7.01
    # feint economy: 3 feints per real attack keeps the partner guessing
    feints = 3
    attacks = 1
    total = feints + attacks
    real_rate = attacks / total
    print("feint-to-attack %d:%d - only %.0f%% of motions are real" % (feints, attacks, real_rate * 100.0))
    assert 24.9 < real_rate * 100.0 < 25.1
    # pattern-breaking: change the follow-up every 4th exchange
    print("break your own pattern every 4th exchange - unpredictability starts at home")
    # ten feint-then-real reps where the feint must draw a reaction
    print("drill: 10 feint-then-real combos, feint indistinguishable until the branch")
    print("rule: the feint must be real until it is not")
    print("OK: %s played the cunning game" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_jogo_angola(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # slow game: 10-minute round at half tempo, ~6 exchanges/minute
    minutes = 10.0
    exch_per_min = 6.0
    exchanges = minutes * exch_per_min
    print("10-minute Angola round: %.0f patient exchanges" % exchanges)
    assert 59.9 < exchanges < 60.1
    # one explosion per round: the punctuation ratio
    explosions = 1.0
    print("explosions per round: %.0f - punctuation, not tempo" % explosions)
    # low time: ~80%% of the round spent at crouch depth or lower
    low_share = 0.80
    low_min = minutes * low_share
    print("time spent low: %.1f minutes of %.0f" % (low_min, minutes))
    assert 7.99 < low_min < 8.01
    # waiting discipline: the opening comes on average at minute 7
    print("the true opening arrives when impatience would have quit")
    print("drill: 10-minute slow rounds, half tempo, rushing forbidden")
    print("rule: patience defeats speed - wait longest, win")
    print("OK: %s played the slow game" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_jogo_regional(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fast game: 3-minute round, one combination every 4 seconds
    round_s = 180.0
    combo_every = 4.0
    combos = round_s / combo_every
    print("3-minute Regional round: %.0f combinations" % combos)
    assert 44.9 < combos < 45.1
    # 2.5 kicks per combination on average
    kicks = combos * 2.5
    print("kicks thrown: %.0f per round" % kicks)
    assert 112.4 < kicks < 112.6
    # three rounds per session
    session_kicks = kicks * 3.0
    print("3-round session: %.0f kicks" % session_kicks)
    assert 337.4 < session_kicks < 337.6
    # pace check: round 3 output must stay within 90%% of round 1
    print("conditioning standard: round 3 within 90%% of round 1 output")
    print("drill: Bimba sequences to reflex, then 3 full-tempo rounds")
    print("rule: combinations, not singles - the system is the sequence")
    print("OK: %s played the fast game" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cc_sequencia_bimba(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight sequences x 10 reps x 2 roles = the curriculum volume
    seqs = 8
    reps = 10
    roles = 2
    total = seqs * reps * roles
    print("curriculum volume: %d sequences x %d reps x %d roles = %d" % (seqs, reps, roles, total))
    assert total == 160  # int count
    # at 30 s per attack-defense rep, one full pass:
    minutes = total * 30.0 / 60.0
    print("one full precision pass: %.0f minutes" % minutes)
    assert 79.9 < minutes < 80.1
    # weekly: 3 passes = 240 minutes of sequence work
    weekly = minutes * 3.0
    print("weekly sequence work (3 passes): %.0f minutes" % weekly)
    assert 239.9 < weekly < 240.1
    # graduation: all eight clean at speed from either role
    print("graduation standard: 8/8 clean at speed, both roles")
    print("rule: precision before speed - sloppy forms teach sloppy reflexes")
    print("OK: %s completed the eight sequences" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "meia_lua_compasso": demo_cc_meia_lua_compasso,
    "s_dobrado": demo_cc_s_dobrado,
    "parafuso": demo_cc_parafuso,
    "mortal": demo_cc_mortal,
    "au_sem_mao": demo_cc_au_sem_mao,
    "chamada": demo_cc_chamada,
    "malicia": demo_cc_malicia,
    "jogo_angola": demo_cc_jogo_angola,
    "jogo_regional": demo_cc_jogo_regional,
    "sequencia_bimba": demo_cc_sequencia_bimba,
})

# (build.py asserts the DEMOS/ENTRIES key match at import time)
