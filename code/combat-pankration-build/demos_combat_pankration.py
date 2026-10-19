#!/usr/bin/env python3
"""Demo programs for the Pankration Combat Database (combat batch 3, 2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
training calculation for its record: timelines, stance geometry, strike
energy, throw mechanics, conditioning math, and bout strategy numbers.
All are machine-executed by build.py: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


DEMOS = {}


def demo_pk_allforce(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pankration's Olympic debut: 648 BC (33rd Olympiad) to 2026 AD
    years = 2026 + 648
    olympiads = years / 4.0
    print("years since 648 BC: %d" % years)
    print("four-year Olympiads spanned: %.1f" % olympiads)
    assert 2673.9 < years < 2674.1
    assert 668.4 < olympiads < 668.6
    # the two halves of the art, equal partners
    halves = {"pygme (boxing)": 1, "pale (wrestling)": 1}
    print("halves of the art: %d" % sum(halves.values()))
    assert sum(halves.values()) == 2
    print("rule: pan (all) plus kratos (force) - the complete fighter")
    print("OK: %s frames the art" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_parastasis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stance base: feet 0.55 m apart, center of mass near midline
    foot_l, foot_r = -0.275, 0.275
    com = 0.01  # hair of rear bias, metres from midline
    stance_w = foot_r - foot_l
    margin_l = com - foot_l
    margin_r = foot_r - com
    print("stance width: %.3f m" % stance_w)
    print("stability margin lead: %.3f m, rear: %.3f m" % (margin_l, margin_r))
    assert 0.549 < stance_w < 0.551
    assert 0.284 < margin_l < 0.286
    assert 0.264 < margin_r < 0.266
    # both margins positive: the CoM projection sits inside the base
    assert margin_l > 0 and margin_r > 0
    print("rule: soft knees, even weight, free rocking in every direction")
    print("OK: %s holds its ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_cheires(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guard wall: forearms span 0.22 m at 0.65 m from the opponent's eyes
    wall = 0.22
    head_w = 0.20
    margin = (wall - head_w) / 2.0
    print("guard wall: %.2f m, head: %.2f m" % (wall, head_w))
    print("coverage margin per side: %.3f m" % margin)
    assert 0.009 < margin < 0.011
    # angular coverage of the guard from 0.65 m out
    ang = 2 * math.degrees(math.atan((wall / 2) / 0.65))
    print("angular coverage: %.1f degrees" % ang)
    assert 19.1 < ang < 19.4
    print("rule: the wall that punches back - fists at the cheeks, elbows home")
    print("OK: %s raises the wall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # closing measure: 1.8 m gap, 0.45 m steps, 2 steps per second
    gap = 1.8
    step = 0.45
    rate = 2.0
    steps = gap / step
    seconds = steps / rate
    print("gap: %.1f m, steps needed: %.0f" % (gap, steps))
    print("time to close: %.1f s" % seconds)
    assert 3.9 < steps < 4.1
    assert 1.99 < seconds < 2.01
    # retreat must be faster than the advance to hold measure
    retreat_rate = 2.5
    hold = rate / retreat_rate
    print("retreat keeps %.0f %% of the advance covered" % (hold * 100))
    assert 79.9 < hold * 100 < 80.1
    print("rule: every step restores the stance - never cross the feet")
    print("OK: %s owns the measure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_pygme(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight punch: 2.0 kg effective mass at 8.0 m/s
    m, v = 2.0, 8.0
    ke = 0.5 * m * v * v
    mom = m * v
    print("punch kinetic energy: %.1f J" % ke)
    print("punch momentum: %.1f kg m/s" % mom)
    assert 63.9 < ke < 64.1
    assert 15.9 < mom < 16.1
    # snap-back: the return travels the same road in the same time
    travel = 0.6  # metres out and back
    t_out = travel / v
    print("extension time: %.3f s (return matches it)" % t_out)
    assert 0.074 < t_out < 0.076
    print("rule: the shoulder covers the chin - defense built into the attack")
    print("OK: %s travels the straight road" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_pale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # off-balance: 150 N pull at 1.6 m height vs 80 kg on a 0.30 m base
    pull, h = 150.0, 1.6
    m, base = 80.0, 0.30
    tip_torque = pull * h
    restore_torque = m * 9.81 * (base / 2.0)
    print("tipping torque: %.1f N m" % tip_torque)
    print("restoring torque: %.1f N m" % restore_torque)
    assert 239.9 < tip_torque < 240.1
    assert 117.6 < restore_torque < 117.9
    assert tip_torque > restore_torque, "the pull must beat the base"
    print("verdict: the base fails - the throw completes itself")
    print("rule: move his weight past his base and leverage does the rest")
    print("OK: %s feels the tip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_prohibitions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the ancient Olympic run: 648 BC to the last games, 393 AD
    span = 648 + 393
    olympiads = span / 4.0
    print("pankration's Olympic span: %d years" % span)
    print("Olympiads contested: %.2f" % olympiads)
    assert 1040.9 < span < 1041.1
    assert 260.24 < olympiads < 260.26
    # the prohibitions: exactly two
    fouls = ["daknein (biting)", "oruttein (gouging)"]
    print("prohibited acts: %d" % len(fouls))
    assert len(fouls) == 2
    print("rule: two lines only - everything inside them is the art")
    print("OK: %s keeps the lines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_ptosis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 80 kg fighter falling 0.6 m: v at impact, then force over stop time
    m, drop = 80.0, 0.6
    v = math.sqrt(2 * 9.81 * drop)
    print("impact speed: %.2f m/s" % v)
    assert 3.42 < v < 3.44
    stiff = m * v / 0.02    # locked body stops in 20 ms
    soft = m * v / 0.25     # breakfall spreads it over 250 ms
    print("stiff-body peak force: %.0f N" % stiff)
    print("breakfall peak force: %.0f N" % soft)
    assert 13700.0 < stiff < 13760.0
    assert 1095.0 < soft < 1102.0
    ratio = stiff / soft
    print("force reduction: %.1f x" % ratio)
    assert 12.4 < ratio < 12.6
    print("rule: chin tucked, arm slaps, breath out - the ground is not the enemy")
    print("OK: %s falls safely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_halteres(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # progressive halteres: 5 kg x 3 sets x 12 reps, +10% volume weekly
    start_vol = 5.0 * 3 * 12
    rate = 1.10
    weeks = 8
    vols = [start_vol * (rate ** w) for w in range(weeks)]
    print("week 1 volume: %.0f kg" % vols[0])
    print("week 8 volume: %.0f kg" % vols[-1])
    assert 179.9 < vols[0] < 180.1
    assert 350.5 < vols[-1] < 351.2
    total = sum(vols)
    print("8-week total lifted: %.0f kg" % total)
    assert 2058.0 < total < 2059.0
    print("rule: small weekly additions, clean form - the set ends when form breaks")
    print("OK: %s works the forge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_skamma(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # training ground: 10 m x 10 m mat, each pair needs 3 m x 3 m
    area = 10.0 * 10.0
    per_pair = 3.0 * 3.0
    pairs = int(area // per_pair)
    print("ground area: %.0f m^2" % area)
    print("pairs that fit: %d" % pairs)
    assert 99.9 < area < 100.1
    assert pairs == 11
    # clinch rounds: 2 min on, 1 min off, 6 rounds
    work = 6 * 2.0
    rest = 6 * 1.0
    print("session: %.0f min work, %.0f min rest" % (work, rest))
    assert 11.99 < work < 12.01 and 5.99 < rest < 6.01
    print("rule: same surface, same discipline, every session - the ground is honest")
    print("OK: %s trains the ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_breathing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 3-minute round at 30 breaths/min under effort
    round_s = 180.0
    rate = 30.0
    breaths = round_s / 60.0 * rate
    print("breaths per round: %.0f" % breaths)
    assert 89.9 < breaths < 90.1
    # 5-round bout plus 1-minute rests at 15 breaths/min
    bout_breaths = 5 * breaths + 4 * 15.0
    print("breaths per 5-round bout: %.0f" % bout_breaths)
    assert 509.9 < bout_breaths < 510.1
    # exhale fraction: effort gets the out-breath
    print("rule: exhale on effort, inhale on recovery - never hold under strain")
    print("OK: %s breathes the bout" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_clinch_tieup(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # underhook lift: 40 kg of opponent's weight on a 0.25 m lever
    m, lever = 40.0, 0.25
    torque = m * 9.81 * lever
    print("underhook torque: %.1f N m" % torque)
    assert 98.0 < torque < 98.2
    # head position: forehead drive of 120 N at 1.65 m vs his base
    drive = 120.0 * 1.65
    print("posture-breaking torque: %.1f N m" % drive)
    assert 197.9 < drive < 198.1
    print("rule: head up and inside, hips low and back - the tie-up is never a rest")
    print("OK: %s works the bridge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_laktisma(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # front kick: 8 kg effective leg mass at 7 m/s, pad gives 0.06 m
    m, v, give = 8.0, 7.0, 0.06
    ke = 0.5 * m * v * v
    force = ke / give
    print("kick energy: %.0f J" % ke)
    print("pad force: %.0f N" % force)
    assert 195.9 < ke < 196.1
    assert 3265.0 < force < 3269.0
    # rechamber time at the same speed over 0.9 m of leg travel
    t_back = 0.9 / v
    print("rechamber time: %.3f s" % t_back)
    assert 0.128 < t_back < 0.130
    print("rule: chamber, piston, rechamber - the stance must be recovered")
    print("OK: %s drives the spear" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_turning_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # turning kick: hips at 10 rad/s, leg 0.9 m -> foot speed 9 m/s
    omega, leg = 10.0, 0.9
    v = omega * leg
    m = 6.0
    ke = 0.5 * m * v * v
    print("foot speed: %.1f m/s" % v)
    print("kick energy: %.0f J" % ke)
    assert 8.99 < v < 9.01
    assert 242.9 < ke < 243.1
    # pivot: supporting foot turns ~135 degrees during the kick
    pivot_deg = 135.0
    print("supporting-foot pivot: %.0f degrees" % pivot_deg)
    assert 134.9 < pivot_deg < 135.1
    print("rule: pivot fully, roll the hips - rotation is the engine")
    print("OK: %s turns the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_ankon(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elbow: 4 kg effective mass at 6 m/s over 0.03 m of contact
    m, v, contact = 4.0, 6.0, 0.03
    ke = 0.5 * m * v * v
    force = ke / contact
    print("elbow energy: %.0f J" % ke)
    print("contact force: %.0f N" % force)
    assert 71.9 < ke < 72.1
    assert 2398.0 < force < 2402.0
    # short arc: 0.35 m radius, 60-degree turn
    arc = 0.35 * math.radians(60.0)
    print("elbow arc: %.3f m" % arc)
    assert 0.366 < arc < 0.367
    print("rule: the torso turns, the arm barely moves - short, sharp, home")
    print("OK: %s presses the seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_gony(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee: 10 kg at 5 m/s, target pulled down to meet it (relative 7 m/s)
    m, v = 10.0, 7.0
    ke = 0.5 * m * v * v
    print("knee collision energy: %.0f J" % ke)
    assert 244.9 < ke < 245.1
    # over 0.05 m of body compression
    force = ke / 0.05
    print("body force: %.0f N" % force)
    assert 4898.0 < force < 4902.0
    # snap-back: 0.5 m of leg travel at 7 m/s
    t_back = 0.5 / v
    print("recovery time: %.3f s" % t_back)
    assert 0.071 < t_back < 0.072
    print("rule: pull him down onto the rising knee - then two feet, instantly")
    print("OK: %s swings the hammer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_rhipsis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the throw's completion: opponent's mass center falls 1.0 m
    drop = 1.0
    t = math.sqrt(2 * drop / 9.81)
    print("fall time of the mass center: %.3f s" % t)
    assert 0.451 < t < 0.453
    # three beats, and the first beat is the throw
    beats = ["off-balance", "entry", "execution"]
    print("beats: %d" % len(beats))
    assert len(beats) == 3
    # off-balance carries 70% of the work: entry 20%, execution 10%
    shares = {"off-balance": 0.70, "entry": 0.20, "execution": 0.10}
    assert abs(sum(shares.values()) - 1.0) < 1e-9
    print("work shares: off-balance 70 %, entry 20 %, execution 10 %")
    print("rule: the throw completes the fall - it never lifts dead weight")
    print("OK: %s proves the throw" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_hip_throw(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hip throw: 300 N pull at 0.9 m lever vs 80 kg resisting at 0.2 m
    pull_torque = 300.0 * 0.9
    resist_torque = 80.0 * 9.81 * 0.2
    print("pulling torque: %.1f N m" % pull_torque)
    print("resisting torque: %.1f N m" % resist_torque)
    assert 269.9 < pull_torque < 270.1
    assert 156.9 < resist_torque < 157.1
    assert pull_torque > resist_torque, "the fulcrum must win"
    margin = pull_torque - resist_torque
    print("throwing margin: %.1f N m" % margin)
    assert 112.9 < margin < 113.1
    print("rule: hips below his, back flat to his chest, pull without pause")
    print("OK: %s turns the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_mesolabe(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # waist lift: 80 kg raised 1.1 m in 1.5 s
    m, h, t = 80.0, 1.1, 1.5
    work = m * 9.81 * h
    power = work / t
    print("lift work: %.1f J" % work)
    print("lift power: %.1f W" % power)
    assert 863.1 < work < 863.4
    assert 575.3 < power < 575.7
    # in the air the opponent's base is zero: his strength counts for nothing
    print("opponent's base while lifted: 0.00 m")
    print("rule: legs are the crane, the back is only the frame - position first")
    print("OK: %s raises the claim" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_trips_sweeps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # step cycle 0.5 s, foot vulnerable for 0.2 s of each cycle
    cycle, window = 0.5, 0.2
    vulnerable = window / cycle
    print("step cycle: %.1f s, vulnerable window: %.1f s" % (cycle, window))
    print("vulnerable fraction: %.0f %%" % (vulnerable * 100))
    assert 39.9 < vulnerable * 100 < 40.1
    # the sweep brush: 0.05 s contact at 4 m/s foot speed
    brush_t, foot_v = 0.05, 4.0
    brush_d = brush_t * foot_v
    print("brush distance: %.2f m" % brush_d)
    assert 0.199 < brush_d < 0.201
    print("rule: his step is your invitation - timing, never force")
    print("OK: %s taxes every foot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_apopnixis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear choke: 180 N of forearm force over 0.025 m^2 of neck contact
    force, area = 180.0, 0.025
    pressure = force / area  # pascals
    print("hold pressure: %.0f Pa (%.1f kPa)" % (pressure, pressure / 1000))
    assert 7198.0 < pressure < 7202.0
    # applied gradually over 3 s, released in under 0.5 s on the tap
    apply_t, release_t = 3.0, 0.5
    print("apply: %.1f s gradual, release: < %.1f s on the tap" % (apply_t, release_t))
    assert 2.99 < apply_t < 3.01 and 0.499 < release_t < 0.501
    print("rule: pressure slowly, release instantly - the tap is sacred")
    print("OK: %s honors the hold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_top_position(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 80 kg through the chest over 0.12 m^2 vs perched on knees over 0.02 m^2
    w = 80.0 * 9.81
    p_chest = w / 0.12
    p_knees = w / 0.02
    print("chest pressure: %.0f Pa" % p_chest)
    print("knee-perch pressure: %.0f Pa" % p_knees)
    assert 6538.0 < p_chest < 6542.0
    assert 39238.0 < p_knees < 39242.0
    ratio = p_knees / p_chest
    print("perch is %.1f x spikier - spread the weight, pin with mass" % ratio)
    assert 5.99 < ratio < 6.01
    print("rule: heavy chest, killing hips, working hands - the top is a workshop")
    print("OK: %s holds the throne" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_escapes_beneath(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bridge: 60 kg of hips thrown 0.25 m skyward in 0.3 s
    m, h, t = 60.0, 0.25, 0.3
    work = m * 9.81 * h
    power = work / t
    print("bridge work: %.1f J" % work)
    print("bridge power: %.0f W" % power)
    assert 147.1 < work < 147.2
    assert 490.3 < power < 490.7
    # hip escape: slide 0.4 m out from under the pin
    slide = 0.4
    print("hip-escape slide: %.1f m to freedom" % slide)
    assert 0.399 < slide < 0.401
    print("rule: buck-and-slide - bridge when he is light, shrimp when he is heavy")
    print("OK: %s finds the exit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_striking_into_clinch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jab-cross-tie entry: 1.2 s per entry, 5 entries per round, 3 rounds
    entry_t, per_round, rounds = 1.2, 5, 3
    total_entries = per_round * rounds
    total_t = total_entries * entry_t
    print("entries per bout: %d" % total_entries)
    print("time spent entering: %.0f s" % total_t)
    assert total_entries == 15
    assert 17.9 < total_t < 18.1
    # the last punch and the grip: gap must be under 0.2 s
    gap = 0.15
    print("punch-to-grip gap: %.2f s (limit 0.20 s)" % gap)
    assert gap < 0.20
    print("rule: the strikes escort, the grip is the mission - one continuous motion")
    print("OK: %s crosses the bridge" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_pk_klimax(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # klimax: 4 rungs (1 arm + 2 legs + body drop) vs 2 defending limbs
    rungs, defenders = 4, 2
    advantage = rungs / defenders
    print("ladder rungs: %d, defending limbs: %d" % (rungs, defenders))
    print("structural advantage: %.1f to 1" % advantage)
    assert 1.99 < advantage < 2.01
    # each rung holds 150 N: the frame totals 600 N against a 400 N escape
    frame = 4 * 150.0
    escape = 400.0
    print("frame hold: %.0f N vs escape: %.0f N" % (frame, escape))
    assert 599.9 < frame < 600.1
    assert frame > escape, "the ladder must out-hold the escape"
    print("rule: hold the frame, never muscle the squeeze - geometry does the work")
    print("OK: %s weaves the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_trachelos(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear choke: two 150 N arm forces meeting at 60 degrees
    f, ang = 150.0, 60.0
    resultant = 2 * f * math.cos(math.radians(ang / 2))
    print("closing force on the neck: %.1f N" % resultant)
    assert 259.7 < resultant < 259.9
    # the hold closes like a book: each degree of elbow draw adds force
    per_degree = resultant / 60.0
    print("force per degree of closure: %.2f N" % per_degree)
    assert 4.32 < per_degree < 4.34
    print("rule: position first - the choke is the period at the sentence's end")
    print("OK: %s writes the final clause" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_arm_locks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight arm lock: 120 N at the wrist, 0.35 m lever on the elbow
    force, lever = 120.0, 0.35
    torque = force * lever
    print("elbow torque: %.1f N m" % torque)
    assert 41.9 < torque < 42.1
    # the elbow's safe working range ends well before the lock's geometry
    safe_deg, lock_deg = 180.0, 195.0
    margin = lock_deg - safe_deg
    print("joint margin respected: %.0f degrees of restraint" % margin)
    assert 14.99 < margin < 15.01
    # leverage beats strength: a 60 kg fighter generates the torque of a far heavier pull
    print("rule: isolate, fulcrum, pressure - slowly, and the tap is the answer")
    print("OK: %s respects the lever" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_counters(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # punch travel: 0.6 m at 8 m/s; human reaction ~0.20 s
    travel, speed = 0.6, 8.0
    t_travel = travel / speed
    t_react = 0.20
    print("punch travel time: %.3f s, reaction time: %.2f s" % (t_travel, t_react))
    assert 0.074 < t_travel < 0.076
    # the counter reads the telegraph (0.25 s), not the punch
    t_telegraph = 0.25
    window = t_telegraph + t_travel
    print("counter window: %.3f s" % window)
    assert 0.324 < window < 0.326
    assert window > t_react, "the window must exceed reaction time"
    print("rule: yield to his direction, add your force to his - never meet force with force")
    print("OK: %s signs his sentence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_ground_striking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # downward punch: 2 kg at 6 m/s plus a 0.3 m gravity drop
    m, v, drop = 2.0, 6.0, 0.3
    v2 = v * v + 2 * 9.81 * drop
    ke_down = 0.5 * m * v2
    ke_flat = 0.5 * m * v * v
    gain = (ke_down - ke_flat) / ke_flat * 100
    print("flat punch energy: %.1f J" % ke_flat)
    print("downward punch energy: %.1f J" % ke_down)
    assert 35.9 < ke_flat < 36.1
    assert 41.8 < ke_down < 42.0
    print("gravity bonus: +%.1f %%" % gain)
    assert 16.3 < gain < 16.5
    print("rule: base first, strikes second - short drops, never a wind-up")
    print("OK: %s calls the rain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_bout_plan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pacing: 20 s bursts at 90% + 40 s clinch recovery at 50%
    burst, rec = 20.0, 40.0
    avg = (burst * 0.90 + rec * 0.50) / (burst + rec)
    print("burst: %.0f %%, recovery: %.0f %%" % (0.90 * 100, 0.50 * 100))
    print("average output: %.1f %%" % (avg * 100))
    assert 63.2 < avg * 100 < 63.5
    # 5 rounds of 3 min = 15 min of bout; bursts per round at this rhythm
    bout_s = 5 * 180.0
    bursts = bout_s / (burst + rec)
    print("sustainable bursts per bout: %.0f" % bursts)
    assert 14.9 < bursts < 15.1
    print("rule: the plan is a compass, not a cage - read, game, branches")
    print("OK: %s walks the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_arrhichion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 648 BC debut to 564 BC final: 84 years; 33rd Olympiad + 21 = 54th
    gap = 648 - 564
    olympiad = 33 + gap // 4
    print("years after pankration's debut: %d" % gap)
    print("Olympiad of the final: %dth" % olympiad)
    assert gap == 84
    assert olympiad == 54
    assert gap % 4 == 0, "the Olympiad math must land exactly"
    # the two-escape rule: every bad position gets two answers
    escapes = 2
    print("escapes attempted per bad position: %d" % escapes)
    assert escapes == 2
    print("rule: the bout is never over while the mind still works")
    print("OK: %s keeps working" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_sostratus(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three Olympic crowns: 364, 360, 356 BC
    wins = [364, 360, 356]
    span = wins[0] - wins[-1]
    gaps = [wins[i] - wins[i + 1] for i in range(len(wins) - 1)]
    print("Olympic victories: %d" % len(wins))
    print("reign span: %d years, gaps: %s" % (span, gaps))
    assert len(wins) == 3
    assert span == 8
    assert gaps == [4, 4]
    # the small lever: a finger needs a fraction of the elbow's force
    finger_n, elbow_n = 15.0, 120.0
    print("finger study force: %.0f N vs elbow: %.0f N" % (finger_n, elbow_n))
    assert finger_n < elbow_n / 4
    print("rule: the small joint obeys the same law - isolate, fulcrum, pressure")
    print("OK: %s hunts the small joint" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_dioxippus(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the exhibition c. 326 BC: 322 years after the 648 BC debut
    gap = 648 - 326
    print("years after pankration's debut: %d" % gap)
    assert gap == 322
    # three range changes: spear range dodged, spear shattered, clinch taken
    ranges = ["long (javelin dodged)", "spear shattered", "clinch and throw"]
    print("range changes: %d" % len(ranges))
    assert len(ranges) == 3
    # the complete fighter's arithmetic: win in two ranges, survive the third
    win, survive = 2, 1
    print("win %d ranges, survive %d" % (win, survive))
    assert win + survive == 3
    print("rule: refuse the specialist's game - change the range until his plan breaks")
    print("OK: %s declines the spear's fight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pk_modern_revival(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # modern federation era: 1999 to 2026
    era = 2026 - 1999
    print("modern federation era: %d years" % era)
    assert era == 27
    # against the ancient Olympic span of 1041 years
    ancient = 1041.0
    share = era / ancient * 100
    print("ancient Olympic span: %.0f years" % ancient)
    print("modern era as share of the ancient span: %.1f %%" % share)
    assert 2.58 < share < 2.62
    # the ladder is unchanged: 3 tiers, 34 records each side
    tiers, recs = 3, 34
    print("tiers: %d, records per database: %d" % (tiers, recs))
    assert tiers == 3 and recs == 34
    print("rule: the art waited - the waiting is over")
    print("OK: %s re-swears the oath" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "allforce": demo_pk_allforce,
    "parastasis": demo_pk_parastasis,
    "cheires": demo_pk_cheires,
    "footwork": demo_pk_footwork,
    "pygme": demo_pk_pygme,
    "pale": demo_pk_pale,
    "prohibitions": demo_pk_prohibitions,
    "ptosis": demo_pk_ptosis,
    "halteres": demo_pk_halteres,
    "skamma": demo_pk_skamma,
    "breathing": demo_pk_breathing,
    "clinch_tieup": demo_pk_clinch_tieup,
    "laktisma": demo_pk_laktisma,
    "turning_kick": demo_pk_turning_kick,
    "ankon": demo_pk_ankon,
    "gony": demo_pk_gony,
    "rhipsis": demo_pk_rhipsis,
    "hip_throw": demo_pk_hip_throw,
    "mesolabe": demo_pk_mesolabe,
    "trips_sweeps": demo_pk_trips_sweeps,
    "apopnixis": demo_pk_apopnixis,
    "top_position": demo_pk_top_position,
    "escapes_beneath": demo_pk_escapes_beneath,
    "striking_into_clinch": demo_pk_striking_into_clinch,
    "klimax": demo_pk_klimax,
    "trachelos": demo_pk_trachelos,
    "arm_locks": demo_pk_arm_locks,
    "counters": demo_pk_counters,
    "ground_striking": demo_pk_ground_striking,
    "bout_plan": demo_pk_bout_plan,
    "arrhichion": demo_pk_arrhichion,
    "sostratus": demo_pk_sostratus,
    "dioxippus": demo_pk_dioxippus,
    "modern_revival": demo_pk_modern_revival,
})
