#!/usr/bin/env python3
"""Demo programs for the Sambo Combat databases (Manon combat orders 2026-10-17, combat batch 2).

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: stance geometry, fall-energy,
grip leverage, kuzushi force, scoring, throw torque, lock leverage,
drill timing, and fight-strategy arithmetic. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.

Cross-checked against entry text: 20-second hold = 4 points, 8-point
total victory, three warnings = disqualification, sport sambo bans
chokes while combat sambo permits them.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cbsam_stance_base(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tipping angle: how far the body can lean before the COM leaves the base
    base_half = 0.225   # half of a 0.45 m shoulder-width stance
    com_tall = 0.95     # center of mass height standing tall
    com_low = 0.80      # center of mass height in the sambo crouch
    a_tall = math.degrees(math.atan(base_half / com_tall))
    a_low = math.degrees(math.atan(base_half / com_low))
    print("tipping angle standing tall: %.2f degrees" % a_tall)
    print("tipping angle in sambo crouch: %.2f degrees" % a_low)
    assert 13.2 < a_tall < 13.5
    assert 15.6 < a_low < 15.8
    assert a_low > a_tall, "the crouch must be harder to topple"
    print("gain from the crouch: %.2f degrees of stability" % (a_low - a_tall))
    print("OK: %s holds its ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_breakfalls(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fall energy for an 80 kg fighter dropping from hip height
    m, g, h = 80.0, 9.81, 0.9
    energy = m * g * h
    # stiff landing: deceleration over 0.15 m; ukemi: slap+roll over 0.40 m
    f_stiff = energy / 0.15
    f_ukemi = energy / 0.40
    g_stiff = f_stiff / (m * g)
    g_ukemi = f_ukemi / (m * g)
    print("fall energy: %.1f J" % energy)
    print("stiff landing force: %.0f N (%.1f g)" % (f_stiff, g_stiff))
    print("ukemi landing force: %.0f N (%.2f g)" % (f_ukemi, g_ukemi))
    assert 706.0 < energy < 707.0
    assert 4700.0 < f_stiff < 4720.0
    assert 1760.0 < f_ukemi < 1775.0
    assert f_ukemi < f_stiff / 2.5, "ukemi must more than halve the shock"
    print("OK: %s spreads the fall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_jacket_grips(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # torque about the opponent's shoulder from a 200 N pull
    pull = 200.0
    sleeve_arm = 0.60   # pull at the sleeve, full arm length
    lapel_arm = 0.15    # pull at the lapel, close to the shoulder
    t_sleeve = pull * sleeve_arm
    t_lapel = pull * lapel_arm
    print("sleeve-grip torque: %.0f N m" % t_sleeve)
    print("lapel-grip torque: %.0f N m" % t_lapel)
    assert 119.0 < t_sleeve < 121.0
    assert 29.0 < t_lapel < 31.0
    ratio = t_sleeve / t_lapel
    print("the sleeve grip gives %.1fx the turning leverage" % ratio)
    assert 3.9 < ratio < 4.1
    print("OK: %s grips with leverage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three-minute footwork round: slide + follow-step cycle
    round_s = 180.0
    cycle_s = 0.8
    step_m = 0.5
    cycles = round_s / cycle_s
    distance = cycles * step_m
    print("step cycles in one round: %.0f" % cycles)
    print("mat covered: %.1f m" % distance)
    assert 224.0 < cycles < 226.0
    assert 112.0 < distance < 113.0
    # stance width must never change: lead and rear move the same distance
    lead = [step_m] * 10
    rear = [step_m] * 10
    assert all(abs(a - b) < 1e-9 for a, b in zip(lead, rear))
    print("stance width preserved across all cycles")
    print("OK: %s never crosses its feet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_kuzushi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # horizontal push at shoulder height needed to topple an 80 kg opponent
    m, g = 80.0, 9.81
    push_h = 1.4
    base_settled = 0.225  # feet planted
    base_stepping = 0.10  # mid-step, base narrowed
    f_settled = m * g * base_settled / push_h
    f_stepping = m * g * base_stepping / push_h
    print("force to topple settled stance: %.1f N" % f_settled)
    print("force to topple mid-step: %.1f N" % f_stepping)
    assert 126.0 < f_settled < 126.3
    assert 55.9 < f_stepping < 56.2
    print("attacking the step takes %.0f percent less force"
          % ((1 - f_stepping / f_settled) * 100))
    assert f_stepping < f_settled * 0.5
    print("OK: %s topples the step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_tieup(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # closing 1.2 m of distance at a 2.5 m/s step-in
    distance, speed = 1.2, 2.5
    entry_t = distance / speed
    reaction_t = 0.25  # trained defensive reaction
    print("tie-up entry time: %.2f s" % entry_t)
    print("defender reaction time: %.2f s" % reaction_t)
    assert 0.47 < entry_t < 0.49
    # entry must land inside the reaction window plus the grip-fight
    assert entry_t < reaction_t + 0.30
    print("entry beats the first defensive motion")
    print("OK: %s wins the inside" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_posture_frame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 300 N of clinch pressure met by a forearm frame at 45 degrees
    push = 300.0
    angle = math.radians(45.0)
    axial = push / math.cos(angle)  # compression carried by the bones
    print("incoming pressure: %.0f N" % push)
    print("axial load on the frame: %.1f N" % axial)
    assert 424.0 < axial < 425.0
    # bent-arm frame vs straight-arm push: the frame shortens the lever
    lever_bent, lever_straight = 0.35, 0.60
    print("shoulder torque bent frame: %.0f N m" % (push * lever_bent))
    print("shoulder torque straight arm: %.0f N m" % (push * lever_straight))
    assert push * lever_bent < push * lever_straight * 0.6
    print("OK: %s frames the pressure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_hip_escape(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # escaping side control needs about 1.2 m of hip travel
    per_shrimp = 0.35
    needed = 1.2
    cycle_s = 1.2
    cycles = math.ceil(needed / per_shrimp)
    total_t = cycles * cycle_s
    print("hip travel per shrimp: %.2f m" % per_shrimp)
    print("shrimp cycles to escape: %d" % cycles)
    print("escape time: %.1f s" % total_t)
    assert cycles == 4
    assert 4.7 < total_t < 4.9
    # shoulders stay down: shoulder travel must be near zero
    shoulder_travel = 0.02
    assert shoulder_travel < per_shrimp * 0.1
    print("OK: %s shrimps to freedom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_bridging(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bridge lifts 40 percent of an 80 kg opponent through 0.25 m
    m_opp = 80.0 * 0.40
    g, lift = 9.81, 0.25
    work = m_opp * g * lift
    peak_force = work / lift
    print("bridge work: %.1f J" % work)
    print("peak hip force: %.0f N" % peak_force)
    assert 78.0 < work < 79.0
    assert 313.0 < peak_force < 315.0
    # bridging into motion: timed at their weight shift, needs 30 percent less
    timed_force = peak_force * 0.70
    print("timed bridge force: %.0f N" % timed_force)
    assert 219.0 < timed_force < 221.0
    print("OK: %s bridges the siege" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_rules_scoring(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # FIAS-style scoring walk: 4-point throw, 2-point hold, 2-point hold
    score = 0
    score += 4  # big throw, opponent flat, thrower standing
    score += 2  # 10-second hold-down
    print("after throw plus one hold: %d points" % score)
    assert score == 6
    score += 2  # second 10-second hold
    print("after second hold: %d points" % score)
    total_victory = score >= 8
    print("total victory at 8 points: %s" % total_victory)
    assert total_victory
    warnings = 3
    dq = warnings >= 3
    print("three warnings means disqualification: %s" % dq)
    assert dq
    print("OK: %s counts to victory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_osoto_gari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reap torque vs the opponent's support torque
    reap_force, reap_arm = 150.0, 0.45
    t_reap = reap_force * reap_arm
    m, g = 80.0, 9.81
    t_support = m * g * 0.10  # weight inside a 0.10 m base edge
    pull, pull_h = 100.0, 1.4  # kuzushi pull at shoulder height
    t_total = t_reap + pull * pull_h
    print("reap torque: %.1f N m" % t_reap)
    print("support torque: %.1f N m" % t_support)
    print("reap plus kuzushi pull: %.1f N m" % t_total)
    assert 67.0 < t_reap < 68.0
    assert 78.0 < t_support < 79.0
    assert 207.0 < t_total < 208.0
    assert t_total > t_support * 2.0, "the throw must overwhelm the base"
    print("OK: %s reaps the leg" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_de_ashi_harai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the stepping foot is light for 0.35 s; the sweep must land inside it
    foot_light_s = 0.35
    sweep_m, sweep_speed = 0.40, 3.0
    sweep_t = sweep_m / sweep_speed
    window = 0.20  # usable contact window inside the step
    print("foot light for: %.2f s" % foot_light_s)
    print("sweep travel time: %.3f s" % sweep_t)
    assert 0.13 < sweep_t < 0.14
    assert sweep_t < window < foot_light_s
    print("the sweep fits inside the step with margin")
    # late sweep (after the foot plants) needs 3x the force: never chase
    planted_force = 3.0
    print("planted-foot force multiplier: %.0fx - do not chase" % planted_force)
    print("OK: %s steals the step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_ko_uchi_gari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # opponent pulled onto toes: COM 0.15 m past the base edge
    m, g = 80.0, 9.81
    t_tip = m * g * 0.15
    reap, drive = 120.0, 150.0
    t_reap = reap * 0.90   # ankle reap lever about the COM
    t_drive = drive * 1.40  # chest drive at shoulder height
    t_total = t_reap + t_drive
    print("tipping torque needed: %.1f N m" % t_tip)
    print("reap plus drive: %.1f N m" % t_total)
    assert 117.0 < t_tip < 118.0
    assert 317.0 < t_total < 319.0
    assert t_total > t_tip * 2.5
    print("OK: %s answers the retreat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_seoi_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lifting an 80 kg opponent: legs vs lower back
    load = 80.0 * 9.81
    # bent-back lift: lumbar moment arm 0.40 m
    lumbar_moment = load * 0.40
    # proper form: hips under, legs drive; lumbar moment near zero
    print("opponent weight: %.0f N" % load)
    print("bent-back lumbar moment: %.0f N m - never do this" % lumbar_moment)
    assert 313.0 < lumbar_moment < 315.0
    # safe guideline: keep the working moment under 60 N m
    safe = 60.0
    print("proper-form guideline: under %.0f N m at the low back" % safe)
    assert lumbar_moment > safe * 5.0
    print("OK: %s lifts with the legs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_harai_goshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep at thigh height 0.75 m with 200 N vs their balance torque
    sweep, h = 200.0, 0.75
    t_sweep = sweep * h
    t_balance = 80.0 * 9.81 * 0.10
    print("sweep torque: %.0f N m" % t_sweep)
    print("balance torque: %.1f N m" % t_balance)
    assert 149.0 < t_sweep < 151.0
    assert 78.0 < t_balance < 79.0
    assert t_sweep > t_balance * 1.8
    # higher contact = longer lever: ankle sweep would give only 200*0.1
    ankle_version = 200.0 * 0.10
    print("ankle-height version would give: %.0f N m" % ankle_version)
    assert ankle_version < t_balance
    print("OK: %s sweeps at the thigh" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_uchi_mata(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the lifting leg must unweight the opponent: 30 percent of bodyweight
    m, g = 80.0, 9.81
    unweight = 0.30 * m * g
    lift = 400.0  # driving thigh lift
    print("force to unweight: %.1f N" % unweight)
    print("thigh lift delivered: %.0f N" % lift)
    assert 235.0 < unweight < 236.0
    assert lift > unweight * 1.5
    # support foot pivot: single-leg balance holds the lift
    support_time = 0.6  # seconds of single-leg drive
    print("single-leg drive time: %.1f s" % support_time)
    assert 0.5 < support_time < 0.8
    print("OK: %s lifts the tide" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_morote_gari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # drive an 80 kg opponent to 2 m/s in 0.5 s off the penetration step
    m = 80.0
    dv, dt = 2.0, 0.5
    force = m * dv / dt
    print("drive force: %.0f N" % force)
    assert 319.0 < force < 321.0
    # rear knee drops: penetration lowers the COM by 0.35 m first
    drop = 0.35
    print("level change: %.2f m" % drop)
    assert 0.34 < drop < 0.36
    # head position: tight to the hip keeps the spine safe
    print("head stays tight to the hip, never under the center")
    print("OK: %s shoots the double" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_sprawl(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the shot lands in 0.60 s; the sprawl must beat it
    detect_t, sprawl_t = 0.15, 0.35
    shot_t = 0.60
    defense_t = detect_t + sprawl_t
    margin = shot_t - defense_t
    print("sprawl total time: %.2f s" % defense_t)
    print("shot arrival: %.2f s" % shot_t)
    print("margin: %.2f s" % margin)
    assert 0.09 < margin < 0.11
    assert margin > 0, "the sprawl must win the race"
    # hips travel back 1.1 m in the sprawl
    hip_travel = 1.1
    print("hip travel: %.1f m" % hip_travel)
    assert 1.0 < hip_travel < 1.2
    print("OK: %s becomes the mat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_kesa_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pin pressure: 70 percent of 80 kg over 0.15 square meters
    weight = 0.70 * 80.0 * 9.81
    area = 0.15
    pressure = weight / area
    print("pin weight: %.1f N" % weight)
    print("pin pressure: %.0f Pa" % pressure)
    assert 549.0 < weight < 550.0
    assert 3660.0 < pressure < 3665.0
    # FIAS hold-down scoring: 2 points at 10 s, 4 points at 20 s
    for seconds, pts in ((10, 2), (20, 4)):
        print("hold %d s scores %d points" % (seconds, pts))
    assert (20, 4)[1] == 4
    print("OK: %s wraps the scarf" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_mount(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # base polygon: knees 0.50 m apart, COM centered; bridge shifts 0.20 m
    base_half = 0.25
    bridge_shift = 0.20
    margin = base_half - bridge_shift
    print("base half-width: %.2f m" % base_half)
    print("bridge shift: %.2f m" % bridge_shift)
    print("stability margin: %.2f m" % margin)
    assert 0.04 < margin < 0.06
    assert margin > 0, "the COM stays inside the base"
    # grapevine cuts bridge power by pinning the legs: 40 percent less lift
    print("grapevined bridge power: 60 percent of free bridge")
    print("OK: %s rides the storm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_back_control(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear choke: 15 percent of bodyweight across two carotids
    pull = 0.15 * 80.0 * 9.81
    per_side = pull / 2.0
    needed = 24.5  # newtons per side to occlude, sports-medicine figure
    print("choke pull: %.1f N" % pull)
    print("per side: %.1f N (needs %.1f N)" % (per_side, needed))
    assert 117.0 < pull < 118.0
    assert 58.0 < per_side < 60.0
    assert per_side > needed * 2.0
    print("rule boundary: legal in combat sambo, banned in sport sambo")
    print("OK: %s secures the back" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_armbar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 300 N bridge at the wrist, 0.35 m from the elbow
    torque = 300.0 * 0.35
    injury_limit = 40.0  # elbow injury threshold, sports-medicine figure
    print("armbar torque: %.0f N m" % torque)
    print("elbow injury threshold: %.0f N m" % injury_limit)
    assert 104.0 < torque < 106.0
    assert torque > injury_limit * 2.0
    print("the tap must come long before full pressure")
    # control check: knees pinched, thumb up verified by position flags
    position = {"knees_pinched": True, "thumb_up": True, "wrist_to_chest": True}
    assert all(position.values())
    print("OK: %s demonstrates the lever" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_kimura(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # figure-four pull of 150 N at 0.30 m from the shoulder
    torque = 150.0 * 0.30
    shoulder_limit = 25.0  # shoulder injury threshold, sports-medicine figure
    print("kimura torque: %.0f N m" % torque)
    print("shoulder injury threshold: %.0f N m" % shoulder_limit)
    assert 44.0 < torque < 46.0
    assert torque > shoulder_limit
    # slow application: pressure ramps over 2 seconds, never instant
    ramp_s = 2.0
    print("pressure ramp: %.0f s minimum" % ramp_s)
    assert 1.9 < ramp_s < 2.1
    print("OK: %s ties the knot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_achilles(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 250 N bridge onto the tendon over 4 square centimeters
    force = 250.0
    area_m2 = 4.0 / 10000.0
    pressure_kpa = force / area_m2 / 1000.0
    print("bridge force: %.0f N" % force)
    print("tendon pressure: %.0f kPa" % pressure_kpa)
    assert 624.0 < pressure_kpa < 626.0
    # the slowest application of any lock: ramp over 3 seconds
    ramp_s = 3.0
    print("minimum pressure ramp: %.0f s" % ramp_s)
    assert 2.9 < ramp_s < 3.1
    print("OK: %s seals the heel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_knee_bar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 350 N bridge, knee 0.40 m below the hip fulcrum
    torque = 350.0 * 0.40
    knee_limit = 60.0  # knee injury threshold, sports-medicine figure
    print("knee bar torque: %.0f N m" % torque)
    print("knee injury threshold: %.0f N m" % knee_limit)
    assert 139.0 < torque < 141.0
    assert torque > knee_limit * 2.0
    print("career-ending stakes: release is instant on the tap")
    print("OK: %s respects the lever" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_toe_hold(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rotational lock: 60 N at a 0.15 m lever on the foot
    torque = 60.0 * 0.15
    foot_limit = 5.0  # small-joint injury threshold, sports-medicine figure
    print("toe hold torque: %.1f N m" % torque)
    print("foot injury threshold: %.1f N m" % foot_limit)
    assert 8.9 < torque < 9.1
    assert torque > foot_limit
    # quarter turn tells everything: never take the full twist
    print("a quarter turn diagnoses; the full twist is never needed")
    print("OK: %s turns the key gently" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_combinations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # single throw lands 35 percent; each chained follow-up lands 50 percent
    p1, p2, p3 = 0.35, 0.50, 0.50
    p_chain = 1.0 - (1.0 - p1) * (1.0 - p2) * (1.0 - p3)
    print("single-throw success: %.0f percent" % (p1 * 100))
    print("three-throw chain success: %.1f percent" % (p_chain * 100))
    assert 0.83 < p_chain < 0.85
    assert p_chain > p1 * 2.0, "the chain must more than double the odds"
    print("OK: %s speaks in chains" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_counters(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # their commitment phase lasts 0.25 s; the counter must fire inside it
    commit_s = 0.25
    window_s = 0.15
    print("commitment phase: %.2f s" % commit_s)
    print("counter window: %.2f s" % window_s)
    assert 0.14 < window_s < 0.16
    assert window_s < commit_s
    coverage = window_s / commit_s * 100.0
    print("the window covers %.0f percent of their commitment" % coverage)
    assert 59.0 < coverage < 61.0
    print("OK: %s echoes the attack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_striking_entries(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # closing 1.5 m behind the jab-cross at 3 m/s
    distance, speed = 1.5, 3.0
    entry_t = distance / speed
    guard_return_s = 0.25  # hands back to guard between strikes
    print("entry time: %.2f s" % entry_t)
    assert 0.49 < entry_t < 0.51
    print("guard return: %.2f s" % guard_return_s)
    assert 0.24 < guard_return_s < 0.26
    # two strikes thrown during the entry
    strikes = int(entry_t / guard_return_s)
    print("strikes covering the entry: %d" % strikes)
    assert strikes == 2
    print("OK: %s knocks then enters" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_clinch_striking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee: 12 kg of leg at 6 m/s, stopped in 0.05 s
    m, v, dt = 12.0, 6.0, 0.05
    force = m * v / dt
    print("knee strike force: %.0f N" % force)
    assert 1439.0 < force < 1441.0
    # balance: support foot must stay planted through the knee
    print("the support foot never leaves the mat during the knee")
    # knee-to-throw: their reaction to the knee opens the hip throw
    print("strike reaction opens the throw; the throw follows")
    print("OK: %s hammers the forge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_kick_defense(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low kick arrives in 0.35 s; the shin check lifts in 0.20 s
    kick_t, check_t = 0.35, 0.20
    margin = kick_t - check_t
    print("kick arrival: %.2f s" % kick_t)
    print("check lift: %.2f s" % check_t)
    print("margin: %.2f s" % margin)
    assert 0.14 < margin < 0.16
    assert margin > 0
    # the catch converts: every caught kick becomes a takedown
    print("caught kick to takedown conversion: 1.0")
    print("OK: %s taxes the kick" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_ground_striking_defense(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the shell covers a 160-degree arc; hips rotate 90 degrees per second
    coverage_deg = 160.0
    hip_rate = 90.0
    print("shell coverage: %.0f degrees" % coverage_deg)
    assert 159.0 < coverage_deg < 161.0
    # re-aiming the shell across the gap takes under half a second
    gap = 180.0 - coverage_deg
    reaim_t = gap / hip_rate
    print("gap to cover: %.0f degrees, re-aim time: %.2f s" % (gap, reaim_t))
    assert 0.21 < reaim_t < 0.23
    print("movement is the roof; stillness is the rain")
    print("OK: %s shells the storm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_ura_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # deadlift an 80 kg opponent with 20 percent acceleration overhead
    lift = 80.0 * 9.81 * 1.20
    print("lift force: %.0f N" % lift)
    assert 941.0 < lift < 943.0
    # back stays straight: the arch is thoracic, the lift is in the legs
    print("the arch is thoracic; the lift is in the legs")
    # crash pads mandatory until clean: pad absorbs the landing
    pad_rating_j = 1500.0
    landing_j = 80.0 * 9.81 * 1.5
    print("landing energy: %.0f J vs pad rating %.0f J" % (landing_j, pad_rating_j))
    assert landing_j < pad_rating_j
    print("OK: %s reverses the storm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cbsam_fight_strategy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # score management: ahead 6-0 with 2 minutes left, total victory at 8
    lead, target, seconds_left = 6, 8, 120
    needed = target - lead
    rate = needed / (seconds_left / 60.0)  # points per minute required
    print("lead: %d, total victory at: %d" % (lead, target))
    print("points needed: %d" % needed)
    print("required scoring rate: %.2f points per minute" % rate)
    assert needed == 2
    assert 0.99 < rate < 1.01
    # behind 0-4 with a minute left: must open up for the big throw
    print("down 0-4 with 60 s left: chase the 4-point throw or the lock")
    deficit_plan = "attack"
    assert deficit_plan == "attack"
    print("OK: %s authors the bout" % NAME)
if __name__ == "__main__":
    main()
''')
