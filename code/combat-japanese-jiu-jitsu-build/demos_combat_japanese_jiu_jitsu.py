#!/usr/bin/env python3
"""Demo programs for the Japanese Jiu-Jitsu Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: stance geometry, distance/timing math,
fall-impact physics, leverage and torque for locks, drill timers, and
technique chaining schedules. All are machine-executed by build.py before
the merger step: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_jjj_shisei(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jigotai base of support: feet 0.60 m apart, stance depth 0.45 m
    width, depth = 0.60, 0.45
    area = width * depth
    # center of mass 0.05 m forward of center; margin to nearest edge
    margin = min(width / 2.0, depth / 2.0 - 0.05)
    print("base of support: %.2f m x %.2f m = %.4f m^2" % (width, depth, area))
    print("stability margin to nearest edge: %.3f m" % margin)
    assert 0.2699 < area < 0.2701
    assert 0.1749 < margin < 0.1751
    print("rule: the lower body wins - stance is the first covenant")
    print("OK: %s rooted the stance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_maai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # issoku-itto-no-maai: one step, one sword - 1.8 m
    maai = 1.8
    closing_speed = 2.5      # m/s, committed step
    reaction = 0.28          # s, trained response
    time_to_contact = maai / closing_speed
    window = time_to_contact - reaction
    print("distance: %.1f m at %.1f m/s -> contact in %.3f s" % (maai, closing_speed, time_to_contact))
    print("decision window after reaction: %.3f s" % window)
    assert 0.719 < time_to_contact < 0.721
    assert 0.439 < window < 0.441
    assert window > 0.0, "no time to decide at this distance"
    print("rule: maai is space divided by speed - manage the distance, manage the clock")
    print("OK: %s measured the distance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_mushin_zanshin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # breathing on-ramp: 4-2-4 counts = 10 s per breath, 5 minute session
    breath_cycle = 4 + 2 + 4
    session = 5 * 60
    breaths = session // breath_cycle
    # zanshin hold: 2 s after each of 40 techniques
    zanshin_total = 40 * 2
    print("breathing session: %d s / %d s per breath = %d breaths" % (session, breath_cycle, breaths))
    print("zanshin holds: 40 techniques x 2 s = %d s of remaining mind" % zanshin_total)
    assert breaths == 30
    assert zanshin_total == 80
    print("rule: a settled nervous system sticks to nothing")
    print("OK: %s trained the mind states" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_kumiuchi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pummeling round: 90 s, inside position won 7 times, held 3 s each
    round_s, wins, hold_s = 90, 7, 3
    control_s = wins * hold_s
    share = control_s / round_s * 100.0
    print("pummeling round: %d s, inside control %d x %d s = %d s (%.2f %%)" % (
        round_s, wins, hold_s, control_s, share))
    assert control_s == 21
    assert 23.32 < share < 23.34
    print("rule: control the head, control the sleeve, move the hips first")
    print("OK: %s fought the grip fight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_ukemi_hard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 70 kg fighter falls from 1.5 m: energy m*g*h
    m, g, h = 70.0, 9.81, 1.5
    energy = m * g * h
    # rolling fall spreads the stop over 1.2 m; stiff fall over 0.1 m
    f_roll = energy / 1.2
    f_stiff = energy / 0.1
    print("fall energy: %.2f J" % energy)
    print("average force, rolling (1.2 m): %.1f N" % f_roll)
    print("average force, stiff (0.1 m): %.1f N" % f_stiff)
    assert 1030.0 < energy < 1030.1
    assert 858.3 < f_roll < 858.5
    assert 10300.0 < f_stiff < 10301.0
    assert f_roll < f_stiff / 10.0
    print("rule: spread the fall - one-point landings break")
    print("OK: %s received the ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_taihenjutsu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # forward roll: full 360 degrees in 0.9 s, covering 1.6 m
    omega = 2 * math.pi / 0.9
    rolls, dist_each = 10, 1.6
    total_dist = rolls * dist_each
    print("roll angular velocity: %.3f rad/s" % omega)
    print("drill: %d rolls x %.1f m = %.1f m of relocation" % (rolls, dist_each, total_dist))
    assert 6.981 < omega < 6.982
    assert 15.99 < total_dist < 16.01
    print("rule: every roll ends in stance, eyes on the partner")
    print("OK: %s changed the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_kyusho(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
import random
def main():
    points = ["kasumi", "uto", "jinchu", "suigetsu", "denko",
              "inazuma", "myojo", "kote", "hiji", "sokuto",
              "koshin", "ashinoko"]
    rng = random.Random(17)
    rounds = []
    for r in range(3):
        order = points[:]
        rng.shuffle(order)
        rounds.append(order)
    touches = sum(len(r) for r in rounds)
    print("kyusho drill: %d points x 3 rounds = %d touches" % (len(points), touches))
    for i, r in enumerate(rounds):
        assert set(r) == set(points), "round %d misses a point" % i
        print("  round %d: %s ..." % (i + 1, ", ".join(r[:4])))
    assert touches == 36
    print("rule: touch before power - precision under motion")
    print("OK: %s mapped the vital points" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_tehodoki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grip resists with 25 N at wrist radius 0.035 m
    grip_torque = 25.0 * 0.035
    # escape: body turn drives 60 N through 0.35 m of arm
    escape_torque = 60.0 * 0.35
    ratio = escape_torque / grip_torque
    print("grip torque: %.3f N m" % grip_torque)
    print("escape torque: %.1f N m (ratio %.1f:1)" % (escape_torque, ratio))
    assert 0.874 < grip_torque < 0.876
    assert 20.99 < escape_torque < 21.01
    assert 23.9 < ratio < 24.1
    print("rule: rotate through the thumb gap - never pull against the grip")
    print("OK: %s released the wrist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_ryote_mochi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two hands grip: 35 N each at wrist radius 0.045 m
    grip_torque = 2 * 35.0 * 0.045
    # escape: circling body drives 70 N through 0.30 m lever
    escape_torque = 70.0 * 0.30
    print("two-hand grip torque: %.2f N m" % grip_torque)
    print("circling escape torque: %.1f N m" % escape_torque)
    assert 3.149 < grip_torque < 3.151
    assert 20.99 < escape_torque < 21.01
    assert escape_torque > 5 * grip_torque
    print("rule: the turning body collects on the committed grip")
    print("OK: %s broke the two-hand hold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_kata_mochi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # palm pins the grabbing hand with 50 N; body turn levers the wrist
    # at 0.25 m from the pin
    wrist_torque = 50.0 * 0.25
    wrist_limit = 8.0  # N m, training tap threshold
    print("pin force: 50 N at 0.25 m lever -> wrist torque %.1f N m" % wrist_torque)
    print("tap threshold: %.1f N m" % wrist_limit)
    assert 12.49 < wrist_torque < 12.51
    assert wrist_torque > wrist_limit
    print("rule: the grab is a gift - pin the hand, turn the body")
    print("OK: %s answered the lapel grab" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_empi_uchi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow strike: effective mass 4.2 kg (arm + torso), 8.5 m/s
    m, v = 4.2, 8.5
    ke = 0.5 * m * v ** 2
    # momentum for comparison
    p = m * v
    print("elbow strike energy: %.2f J, momentum %.2f kg m/s" % (ke, p))
    assert 151.7 < ke < 151.8
    assert 35.69 < p < 35.71
    print("rule: short path, whole body - the torso is the handle")
    print("OK: %s threw the elbow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_shotei_uchi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # palm-heel: 4.0 kg effective mass at 7.0 m/s, 0.025 s contact
    m, v, t = 4.0, 7.0, 0.025
    force = m * v / t
    print("palm-heel impulse force: %.0f N over %.3f s" % (force, t))
    assert 1119.9 < force < 1120.1
    print("rule: fingers back, wrist locked - the heel alone arrives")
    print("OK: %s struck with the palm heel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_ude_garami(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # figure-four: 55 N lifted through 0.30 m forearm lever
    applied = 55.0 * 0.30
    tap_cap = 12.0  # N m, training dial stops here
    print("shoulder torque applied: %.1f N m (training cap %.0f N m)" % (applied, tap_cap))
    assert 16.49 < applied < 16.51
    assert applied > tap_cap, "dial must exceed the cap before the tap"
    print("rule: the lock is a dial - pressure rises, the tap is honored")
    print("OK: %s wove the entanglement" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_kote_gaeshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wrist turn: 40 N tangential at 0.05 m hand radius
    torque = 40.0 * 0.05
    wrist_limit = 1.2  # N m, small joint
    leverage = torque / wrist_limit
    print("wrist-turn torque: %.1f N m vs %.1f N m limit (%.2fx)" % (torque, wrist_limit, leverage))
    assert 1.999 < torque < 2.001
    assert 1.66 < leverage < 1.67
    print("rule: the smallest joint steers the whole body")
    print("OK: %s turned the wrist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_waki_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 70 kg defender sits back: 60% of weight through the armpit fulcrum
    m, g = 70.0, 9.81
    fulcrum_force = m * g * 0.60
    # elbow lever 0.28 m from fulcrum
    elbow_torque = fulcrum_force * 0.28
    print("armpit fulcrum force: %.1f N" % fulcrum_force)
    print("elbow torque: %.1f N m" % elbow_torque)
    assert 412.0 < fulcrum_force < 412.1
    assert 115.3 < elbow_torque < 115.4
    print("rule: structure holds the lock - sit back, let weight work")
    print("OK: %s closed the armpit vise" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_hiji_kannuki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # forearm presses 120 N, 0.25 m from the elbow hinge
    bolt_torque = 120.0 * 0.25
    print("elbow-bolt torque: %.0f N m" % bolt_torque)
    assert 29.99 < bolt_torque < 30.01
    print("rule: resistance signs the bolt - the pull-back feeds the lock")
    print("OK: %s slid the elbow bolt" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_ashi_garami(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hip bridge 250 N rotating the shin on a 0.30 m lever
    knee_torque = 250.0 * 0.30
    print("leg-entanglement torque: %.0f N m" % knee_torque)
    print("note: knees forgive nothing - drill the entry, barely touch pressure")
    assert 74.99 < knee_torque < 75.01
    print("rule: entry speed is the skill; pressure is barely touched")
    print("OK: %s wove the leg snare" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_kubi_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # neck-guided arc: head travels 1.2 m in 0.6 s
    arc, t = 1.2, 0.6
    head_speed = arc / t
    print("head arc speed: %.1f m/s over %.1f m" % (head_speed, arc))
    assert 1.999 < head_speed < 2.001
    print("rule: control the head and the body follows")
    print("OK: %s threw by the neck" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_tani_otoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # valley drop: center falls 0.45 m -> t = sqrt(2h/g)
    h, g = 0.45, 9.81
    t = math.sqrt(2 * h / g)
    print("drop time for %.2f m: %.3f s" % (h, t))
    assert 0.302 < t < 0.304
    print("rule: the lean that defeats the forward throw feeds the valley")
    print("OK: %s dropped the valley" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_yama_arashi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pull 180 N down-across, sweep 120 N through - perpendicular forces
    pull, sweep = 180.0, 120.0
    resultant = math.sqrt(pull ** 2 + sweep ** 2)
    print("pull %.0f N + sweep %.0f N -> resultant %.2f N" % (pull, sweep, resultant))
    assert 216.32 < resultant < 216.34
    print("rule: the storm is the combination - torn between two forces")
    print("OK: %s raised the mountain storm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_kata_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 70 kg defender, 65% of weight through the chest onto the triangle
    m, g = 70.0, 9.81
    force = m * g * 0.65
    contact = 0.06  # m^2 of the triangle
    pressure = force / contact
    print("pin force: %.1f N over %.2f m^2 = %.0f Pa" % (force, contact, pressure))
    assert 446.3 < force < 446.4
    assert 7438.0 < pressure < 7440.0
    print("rule: weight pins - arms only maintain the loop")
    print("OK: %s built the room with no door" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_yoko_shiho_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 30 s hold against 6 honest escape attempts; weight 70 kg split 60/40
    m, g = 70.0, 9.81
    chest = m * g * 0.60
    legs = m * g * 0.40
    print("hold: 30 s vs 6 escapes - all ridden")
    print("weight split: chest %.1f N / legs %.1f N" % (chest, legs))
    assert 412.0 < chest < 412.1
    assert 274.6 < legs < 274.7
    assert abs((chest + legs) - m * g) < 0.01
    print("rule: the right angle is the lock - ride, never resist")
    print("OK: %s held the side cross" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_tate_shiho_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hold-only round: 120 s on top, 8 bridge attempts ridden low
    hold_s, bridges = 120, 8
    ride_each = hold_s / bridges
    print("mount hold: %d s, %d bridges ridden (%.1f s control per bridge)" % (
        hold_s, bridges, ride_each))
    assert 14.99 < ride_each < 15.01
    print("rule: control flows downward - pour, do not chase")
    print("OK: %s kept the throne" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_okuri_eri_jime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # safety protocol: 6 s application, full release, 10 s recovery; 5 reps
    apply_s, recover_s, reps = 6, 10, 5
    total = reps * (apply_s + recover_s)
    print("strangle safety timer: %d reps x (%d s on + %d s off) = %d s" % (
        reps, apply_s, recover_s, total))
    assert total == 80
    print("rule: the strangle is a dial - depth first, then the smallest pull")
    print("OK: %s timed the sliding strangle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_kata_ha_jime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # thread depth: 4 fingers = 0.08 m past the hand; 10 threads per side
    depth_m, threads = 0.08, 10
    total_thread_m = depth_m * threads * 2
    print("wing drill: %d threads/side x %.2f m depth x 2 sides = %.2f m threaded" % (
        threads, depth_m, total_thread_m))
    assert 1.599 < total_thread_m < 1.601
    print("rule: depth of thread is the technique - a shallow wing is an embrace")
    print("OK: %s threaded the single wing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_gyaku_juji_jime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reverse cross: grip set in 3 s, finish pulls 2 x 90 N out and down
    set_s = 3
    finish = 2 * 90.0
    print("grip set: %d s -> crossed X; finish pull: %.0f N out and down" % (set_s, finish))
    assert set_s == 3
    assert 179.99 < finish < 180.01
    print("rule: elbows out and down - the finish direction is the technique")
    print("OK: %s crossed the reverse X" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_hadaka_jime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # naked strangle drill: pressure in 0.5 s increments, tap expected ~2.5 s
    step, tap_at = 0.5, 2.5
    steps_to_tap = tap_at / step
    print("incremental drill: %.1f s steps, tap expected at %.1f s (%d steps)" % (
        step, tap_at, int(steps_to_tap)))
    assert 4.99 < steps_to_tap < 5.01
    print("rule: a loaded technique - release begins before the tap ends")
    print("OK: %s respected the naked strangle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_sumi_otoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dead corner: 135 degrees from the facing direction, rear diagonal
    corner_deg = 135.0
    corner_rad = math.radians(corner_deg)
    # unit facing vector (1,0); corner direction components
    cx, cy = math.cos(corner_rad), math.sin(corner_rad)
    print("dead corner at %.0f deg: direction (%.4f, %.4f)" % (corner_deg, cx, cy))
    assert -0.7072 < cx < -0.7070
    assert 0.7070 < cy < 0.7072
    print("rule: kuzushi at the perfect angle is the entire technique")
    print("OK: %s found the dead corner" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_uki_otoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee drop 0.5 m vertical: t = sqrt(2h/g); timing window +-0.1 s
    h, g = 0.5, 9.81
    t = math.sqrt(2 * h / g)
    window = 0.1
    print("knee drop: %.3f s; answer window %.3f +- %.1f s" % (t, t, window))
    assert 0.319 < t < 0.320
    print("rule: the drop answers the push - early is wasted, late is run over")
    print("OK: %s floated the drop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_tomoe_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stomach circle: attacker launched at 3.2 m/s, 45 deg -> range v^2/g
    v, g = 3.2, 9.81
    flight_range = v ** 2 / g
    air_time = 2 * v * math.sin(math.pi / 4) / g
    print("tomoe circle: launch %.1f m/s -> range %.3f m, air time %.3f s" % (
        v, flight_range, air_time))
    assert 1.043 < flight_range < 1.045
    assert 0.460 < air_time < 0.462
    print("rule: the foot is the ramp, the fall is the counterweight")
    print("OK: %s drew the stomach circle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_ushiro_ryote_mochi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # instant drop 0.25 m: t = sqrt(2h/g); elbows wedge up with 2 x 60 N
    h, g = 0.25, 9.81
    t = math.sqrt(2 * h / g)
    wedge = 2 * 60.0
    print("drop: %.3f s to steal the pull's space; elbow wedge %.0f N" % (t, wedge))
    assert 0.225 < t < 0.227
    assert 119.99 < wedge < 120.01
    print("rule: never pull forward - drop, wedge, turn inside")
    print("OK: %s escaped the rear hold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_kaeshi_waza(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attack commitment lasts 0.50 s; the counter needs 0.35 s to fire
    commitment, counter_need = 0.50, 0.35
    window = commitment - counter_need
    print("commitment %.2f s - counter %.2f s = window %.2f s" % (
        commitment, counter_need, window))
    assert 0.149 < window < 0.151
    assert window > 0, "no window: the attack was not genuine"
    print("rule: never force the counter - answer the real thing")
    print("OK: %s returned the attack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_renraku_waza(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # chain: technique 1 (0.8 s) + link (0.2 s) + technique 2 (0.7 s)
    t1, link, t2 = 0.8, 0.2, 0.7
    chain = t1 + link + t2
    drill_chains = 10
    drill_total = drill_chains * chain
    print("combination chain: %.1f s; drill %d chains = %.0f s" % (
        chain, drill_chains, drill_total))
    assert 1.699 < chain < 1.701
    assert 16.99 < drill_total < 17.01
    print("rule: the first technique farms the defense the second reaps")
    print("OK: %s chained the harvest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jjj_muto_dori(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wooden-sword cut: tip travels 2.5 m arc in 0.40 s
    arc, t_cut = 2.5, 0.40
    tip_speed = arc / t_cut
    # defender offline step: 0.6 m in 0.35 s, entering the dead angle
    step, t_step = 0.6, 0.35
    step_speed = step / t_step
    print("blade tip: %.2f m/s; offline step: %.2f m/s" % (tip_speed, step_speed))
    assert 6.249 < tip_speed < 6.251
    assert 1.713 < step_speed < 1.715
    assert t_step < t_cut, "the step must beat the cut"
    print("rule: enter the dead angle - never the arc")
    print("OK: %s faced the sword unarmed" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "shisei": demo_jjj_shisei,
    "maai": demo_jjj_maai,
    "mushin_zanshin": demo_jjj_mushin_zanshin,
    "kumiuchi": demo_jjj_kumiuchi,
    "ukemi_hard": demo_jjj_ukemi_hard,
    "taihenjutsu": demo_jjj_taihenjutsu,
    "kyusho": demo_jjj_kyusho,
    "tehodoki": demo_jjj_tehodoki,
    "ryote_mochi": demo_jjj_ryote_mochi,
    "kata_mochi": demo_jjj_kata_mochi,
    "empi_uchi": demo_jjj_empi_uchi,
    "shotei_uchi": demo_jjj_shotei_uchi,
    "ude_garami": demo_jjj_ude_garami,
    "kote_gaeshi": demo_jjj_kote_gaeshi,
    "waki_gatame": demo_jjj_waki_gatame,
    "hiji_kannuki": demo_jjj_hiji_kannuki,
    "ashi_garami": demo_jjj_ashi_garami,
    "kubi_nage": demo_jjj_kubi_nage,
    "tani_otoshi": demo_jjj_tani_otoshi,
    "yama_arashi": demo_jjj_yama_arashi,
    "kata_gatame": demo_jjj_kata_gatame,
    "yoko_shiho_gatame": demo_jjj_yoko_shiho_gatame,
    "tate_shiho_gatame": demo_jjj_tate_shiho_gatame,
    "okuri_eri_jime": demo_jjj_okuri_eri_jime,
    "kata_ha_jime": demo_jjj_kata_ha_jime,
    "gyaku_juji_jime": demo_jjj_gyaku_juji_jime,
    "hadaka_jime": demo_jjj_hadaka_jime,
    "sumi_otoshi": demo_jjj_sumi_otoshi,
    "uki_otoshi": demo_jjj_uki_otoshi,
    "tomoe_nage": demo_jjj_tomoe_nage,
    "ushiro_ryote_mochi": demo_jjj_ushiro_ryote_mochi,
    "kaeshi_waza": demo_jjj_kaeshi_waza,
    "renraku_waza": demo_jjj_renraku_waza,
    "muto_dori": demo_jjj_muto_dori,
}
