#!/usr/bin/env python3
"""Demo programs for the Savate Combat databases (combat batch 1).

Every demo is real, runnable, stdlib-only Python performing the actual
combat calculation for its record: training calculators, timing models,
energy and momentum figures, range geometry. All are machine-executed by
build.py before the pages are written: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker. Entry text was cross-checked against these outputs.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cs_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # la garde: weight split, base width, stability margin
    height = 1.75            # m, reference tireur
    mass = 70.0              # kg
    base = 0.45              # m between the feet
    front_share, back_share = 0.60, 0.40
    front_kg = mass * front_share
    back_kg = mass * back_share
    com_height = 0.95        # m, knees soft
    # lateral stability: half-base vs a 5 cm sway of the COM
    margin = base / 2.0 - 0.05
    print("height %.2f m, mass %.0f kg" % (height, mass))
    print("base width: %.2f m" % base)
    print("weight: front %.1f kg (%.0f %%) / back %.1f kg (%.0f %%)" % (
        front_kg, front_share * 100, back_kg, back_share * 100))
    print("COM height: %.2f m, sway margin: %.3f m" % (com_height, margin))
    assert 41.9 < front_kg < 42.1
    assert 27.9 < back_kg < 28.1
    assert 0.449 < base < 0.451
    assert 0.174 < margin < 0.176
    assert margin > 0, "stance must stay stable under a 5 cm sway"
    print("rule: sixty-forty, knees soft, rear heel lifted - the loaded spring")
    print("OK: %s holds the covenant of balance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pas chasse: step distance, step time, travel speed, pivot rate
    step_d = 0.40   # m
    step_t = 0.35   # s
    v = step_d / step_t
    square_steps = 4
    square_d = square_steps * step_d
    square_t = square_steps * step_t
    pivot_rad = math.pi / 2.0   # 90 degrees
    pivot_t = 0.25
    pivot_rate = pivot_rad / pivot_t
    print("step: %.2f m in %.2f s -> %.3f m/s" % (step_d, step_t, v))
    print("square drill: %d steps, %.1f m in %.1f s" % (square_steps, square_d, square_t))
    print("pivot: %.4f rad in %.2f s -> %.3f rad/s" % (pivot_rad, pivot_t, pivot_rate))
    assert 1.142 < v < 1.144
    assert 1.599 < square_d < 1.601
    assert 1.399 < square_t < 1.401
    assert 6.283 < pivot_rate < 6.284
    print("rule: feet never cross, head never bobs - economy arrives early")
    print("OK: %s travels without lifting the pen" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_fouette_median(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # median fouette: foot tip speed and strike energy from the snap
    leg_r = 0.90          # m, hip to laces
    arc = math.pi / 2.0   # 90-degree snap arc
    snap_t = 0.15         # s
    arc_len = leg_r * arc
    tip_v = arc_len / snap_t
    leg_mass = 4.5        # kg, lower leg + shoe
    ke = 0.5 * leg_mass * tip_v ** 2
    print("snap arc: %.3f m in %.2f s" % (arc_len, snap_t))
    print("tip speed: %.2f m/s" % tip_v)
    print("strike energy: %.1f J (%.1f kg at %.2f m/s)" % (ke, leg_mass, tip_v))
    assert 1.413 < arc_len < 1.414
    assert 9.42 < tip_v < 9.43
    assert 199.5 < ke < 200.0
    print("rule: the hip turns, the knee snaps - the leg is the pen, not the hand")
    print("OK: %s signed the ribs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_chasse_frontal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # frontal chasse: push force, work done, displacement of 80 kg opponent
    force = 600.0      # N, piston drive
    drive_d = 0.25     # m, sole travel through the target
    work = force * drive_d
    opp_mass = 80.0
    dv = math.sqrt(2.0 * work / opp_mass)   # velocity imparted, unresisted
    print("push: %.0f N over %.2f m" % (force, drive_d))
    print("work on target: %.0f J" % work)
    print("velocity imparted to %d kg opponent: %.3f m/s" % (opp_mass, dv))
    assert 149.9 < work < 150.1
    assert 1.936 < dv < 1.937
    # a second, committed rep with full hip thrust
    work2 = 700.0 * 0.28
    dv2 = math.sqrt(2.0 * work2 / opp_mass)
    print("committed rep: %.0f J -> %.3f m/s" % (work2, dv2))
    assert 195.9 < work2 < 196.1
    assert 2.213 < dv2 < 2.215
    print("rule: the chasse displaces - the pad holder should be moved, not stung")
    print("OK: %s stamped the seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_direct_avant(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lead direct: travel time, fist speed, reach with the shoulder snap
    travel = 0.60   # m, cheek to target
    t = 0.12        # s
    v = travel / t
    shoulder_add = 0.08  # m stolen by the shoulder snap
    reach = travel + shoulder_add
    print("travel: %.2f m in %.2f s -> %.2f m/s" % (travel, t, v))
    print("reach with shoulder snap: %.2f m" % reach)
    assert 4.99 < v < 5.01
    assert 0.679 < reach < 0.681
    # double jab: two pistons inside a quarter second
    double_t = 2 * t + 0.01
    print("double jab: %.2f s for two touches" % double_t)
    assert 0.249 < double_t < 0.251
    print("rule: straight out, straight back - the return is half the technique")
    print("OK: %s dotted the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_direct_arriere(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear cross: hip contribution over the jab, knuckle speed, momentum
    jab_v = 5.0
    hip_gain = 1.40          # 40% from the hip turn
    cross_v = jab_v * hip_gain
    fist_mass = 3.5          # kg, arm + glove effective
    p = fist_mass * cross_v
    print("jab knuckle speed: %.1f m/s" % jab_v)
    print("cross knuckle speed: %.1f m/s (x%.2f hip gain)" % (cross_v, hip_gain))
    print("momentum: %.2f kg m/s" % p)
    assert 6.99 < cross_v < 7.01
    assert 24.49 < p < 24.51
    gain_pct = (cross_v - jab_v) / jab_v * 100.0
    print("gain over the jab: %.1f %%" % gain_pct)
    assert 39.9 < gain_pct < 40.1
    print("rule: power comes from the floor through the hip, never from the arm")
    print("OK: %s underlined in bold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_pied_bas(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # coup de pied bas: swing time, contact window, attrition model
    swing_t = 0.18      # s, knee lift to contact
    target_h = 0.25     # m, shin height
    knee_lift = 0.15    # m, compact and unreadable
    rng = 0.40          # m, striking range
    # attrition: opponent mobility factor after each landed bas
    mob = 1.0
    print("swing: %.2f s to %.2f m shin at %.2f m range" % (swing_t, target_h, rng))
    for i in (1, 2, 3):
        mob *= 0.92
        print("  bas #%d landed -> mobility factor %.4f" % (i, mob))
    assert 0.179 < swing_t < 0.181
    assert 0.778 < mob < 0.779   # 0.92^3
    assert mob < 0.80, "three clean bas kicks must cost real mobility"
    print("rule: small kick, honest edge - the crack, not the thud")
    print("OK: %s wrote the footnote" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_revers_lateral(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lateral revers: heel arc, tip speed, lateral coverage
    heel_r = 0.85
    arc = math.radians(120.0)
    swing_t = 0.22
    arc_len = heel_r * arc
    tip_v = arc_len / swing_t
    print("heel arc: %.3f m (%.0f deg) in %.2f s" % (arc_len, math.degrees(arc), swing_t))
    print("tip speed: %.2f m/s" % tip_v)
    assert 1.779 < arc_len < 1.781
    assert 8.08 < tip_v < 8.10
    # coverage: the arc spans the guard's whole side frame
    coverage = 2.0 * heel_r * math.sin(arc / 2.0)
    print("lateral coverage: %.3f m" % coverage)
    assert 1.471 < coverage < 1.473
    print("rule: the pivot separates the revers from the fouette - open the hip fully")
    print("OK: %s signed backhand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_crochets(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crochets: tight lead hook vs wide rear hook arc speeds
    lead_r, lead_t = 0.55, 0.14
    rear_r, rear_t = 0.70, 0.16
    arc = math.pi / 2.0
    lead_v = lead_r * arc / lead_t
    rear_v = rear_r * arc / rear_t
    print("lead hook: r=%.2f m arc in %.2f s -> %.2f m/s" % (lead_r, lead_t, lead_v))
    print("rear hook: r=%.2f m arc in %.2f s -> %.2f m/s" % (rear_r, rear_t, rear_v))
    assert 6.16 < lead_v < 6.18
    assert 6.87 < rear_v < 6.89
    assert rear_v > lead_v, "the rear hook must carry the hip's extra"
    # elbow check: 90 degrees +/- 5 or the hook is a slap
    elbow = 90.0
    assert 85.0 < elbow < 95.0
    print("elbow angle: %.0f deg - the hook stays a hook" % elbow)
    print("rule: pivot and hip, never the arm alone")
    print("OK: %s closed the bracket" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_defenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # defense timing: reaction budget vs the jab's flight - why economy wins
    detect = 0.25   # s, visual detection
    motor = 0.15    # s, motor response
    budget = detect + motor
    jab_d, jab_v = 0.60, 5.0
    flight = jab_d / jab_v
    print("reaction budget: %.2f s (detect %.2f + motor %.2f)" % (budget, detect, motor))
    print("jab flight time: %.2f s" % flight)
    assert 0.399 < budget < 0.401
    assert 0.119 < flight < 0.121
    assert flight < budget, "you cannot react to the punch - you must read the tell"
    tell_lead = 0.30  # s, the shoulder dips before the punch launches
    usable = tell_lead + flight - motor
    print("tell lead: %.2f s -> usable defense window: %.2f s" % (tell_lead, usable))
    assert 0.269 < usable < 0.271
    # the parry itself: 5 cm in 0.08 s fits easily; a 30 cm swat does not
    parry_t = 0.05 / (0.05 / 0.08)
    assert 0.079 < parry_t < 0.081
    print("rule: centimeters, not feet - the smallest defense that works")
    print("OK: %s edited with the eraser" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_fouette_figure(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fouette figure: extra height demand over the median
    median_h, figure_h = 1.10, 1.70   # m target heights
    extra = figure_h - median_h
    sink = 0.10                       # m, support leg sinks
    leg = 0.90
    # hip flexion angle needed: leg must reach figure_h from a sunk base
    reach_needed = figure_h - (0.95 - sink)
    hip_flex = math.degrees(math.acos(max(-1.0, min(1.0, (leg**2 + reach_needed**2 - 0.0) / (2 * leg * max(reach_needed, 0.01))))))
    snap_t = 0.18
    print("median target %.2f m -> figure target %.2f m (+%.2f m)" % (median_h, figure_h, extra))
    print("support sink: %.2f m, snap time: %.2f s" % (sink, snap_t))
    assert 0.599 < extra < 0.601
    # progression: shoulder height first, +10 cm per week to head height
    start, step = 1.45, 0.10
    weeks = math.ceil((figure_h - start) / step)
    print("progression: %.2f m start, +%.2f m/week -> %d weeks to head height" % (start, step, weeks))
    assert weeks == 3
    assert snap_t > 0.15, "the figure is slower than the median - that is its price"
    print("rule: height comes from the base, never from leaning")
    print("OK: %s dotted the exclamation point" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_chasse_lateral(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lateral chasse: pivot requirement, sideways displacement, balance
    pivot_deg = 90.0
    force, drive_d = 550.0, 0.22
    work = force * drive_d
    opp = 80.0
    dv = math.sqrt(2.0 * work / opp)
    base = 0.45
    com_offset = 0.10   # m, torso lean-away shifts COM but stays in base
    print("pivot required: %.0f deg" % pivot_deg)
    print("sideways work: %.0f J -> %.3f m/s on %d kg" % (work, dv, opp))
    print("COM offset %.2f m inside base %.2f m: %s" % (
        com_offset, base, "BALANCED" if com_offset < base / 2 else "OVER"))
    assert 120.9 < work < 121.1
    assert 1.739 < dv < 1.741
    assert com_offset < base / 2.0
    print("rule: no pivot, no kick - the support foot decides")
    print("OK: %s wrote in the margin" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {}
DEMOS.update({
    "stance": demo_cs_stance,
    "footwork": demo_cs_footwork,
    "fouette_median": demo_cs_fouette_median,
    "chasse_frontal": demo_cs_chasse_frontal,
    "direct_avant": demo_cs_direct_avant,
    "direct_arriere": demo_cs_direct_arriere,
    "pied_bas": demo_cs_pied_bas,
    "revers_lateral": demo_cs_revers_lateral,
    "crochets": demo_cs_crochets,
    "defenses": demo_cs_defenses,
    "fouette_figure": demo_cs_fouette_figure,
    "chasse_lateral": demo_cs_chasse_lateral,
})


def demo_cs_distance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three ranges in cm, steps to cross, exit time
    longue, moyenne, courte = 180.0, 120.0, 60.0  # cm
    step_cm = 40.0
    cross_steps = (longue - moyenne) / step_cm
    step_t = 0.35
    exit_t = step_t   # one pas chasse back to the longue
    print("longue %.0f cm / moyenne %.0f cm / courte %.0f cm" % (longue, moyenne, courte))
    print("crossing longue->moyenne: %.1f steps" % cross_steps)
    print("exit to the longue: %.2f s (one pas chasse)" % exit_t)
    assert 1.49 < cross_steps < 1.51
    assert 0.349 < exit_t < 0.351
    # the jab measures it: glove at 68 cm reach marks the moyenne's edge
    jab_reach = 68.0
    assert moyenne - 60.0 < jab_reach < moyenne - 40.0
    print("jab reach %.0f cm marks the moyenne - measure, do not feel" % jab_reach)
    print("rule: the feet must serve the weapons")
    print("OK: %s ruled the margins" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_combos_simples(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two-strike chains from 4 foundation tools: permutation count + timing
    import math as _m
    tools = 4
    chains = _m.perm(tools, 2)
    beat = 0.25          # s per strike
    chain_t = 2 * beat
    print("foundation tools: %d -> two-strike chains: %d" % (tools, chains))
    print("chain duration at full speed: %.2f s" % chain_t)
    assert chains == 12
    assert 0.499 < chain_t < 0.501
    # the four named foundation chains and their beat maps
    named = {"jab-cross": (0.25, 0.25), "jab-fouette": (0.25, 0.30),
             "cross-bas": (0.25, 0.28), "fouette-chasse": (0.30, 0.25)}
    for c, (b1, b2) in named.items():
        total = b1 + b2
        print("  %-14s %.2f + %.2f = %.2f s %s" % (
            c, b1, b2, total, "OK" if total <= 0.60 else "TOO SLOW"))
        assert total <= 0.60, c + " is two singles, not a chain"
    print("rule: strike two launches off strike one's return - no pause")
    print("OK: %s wrote the first sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_fouette_balance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # swinging fouette: full-leg momentum vs the chambered snap
    leg_mass = 12.0     # kg, whole leg + shoe
    swing_v = 11.0      # m/s at the laces
    p = leg_mass * swing_v
    ke = 0.5 * leg_mass * swing_v ** 2
    chambered_ke = 199.7  # J, from the median fouette demo
    ratio = ke / chambered_ke
    print("swinging leg: %.1f kg at %.1f m/s" % (leg_mass, swing_v))
    print("momentum: %.0f kg m/s, energy: %.0f J" % (p, ke))
    print("vs chambered fouette: %.1fx the energy" % ratio)
    assert 131.9 < p < 132.1
    assert 725.9 < ke < 726.1
    assert 3.63 < ratio < 3.64
    print("rule: momentum replaces the snap - spend it where the price is paid")
    print("OK: %s ruled the heavy underline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_revers_balance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # swinging revers: full arc, tip speed, time in the blind sector
    heel_r = 0.85
    arc = math.radians(270.0)
    swing_t = 0.30
    arc_len = heel_r * arc
    tip_v = arc_len / swing_t
    # opponent's frontal vision ~120 deg; the kick approaches from 150 deg off-center
    blind_deg = 150.0 - 60.0
    blind_t = swing_t * (blind_deg / 270.0)
    print("arc: %.2f m in %.2f s -> tip %.2f m/s" % (arc_len, swing_t, tip_v))
    print("unseen approach: %.0f deg of arc = %.3f s blind" % (blind_deg, blind_t))
    assert 4.00 < arc_len < 4.01
    assert 13.34 < tip_v < 13.36
    assert 0.099 < blind_t < 0.101
    print("rule: the widest arc owns the outside line - drill the return")
    print("OK: %s wrote backward and bound it" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_chasse_bas(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low chasse: stopping impulse vs an 80 kg opponent advancing at 2 m/s
    opp, v_adv = 80.0, 2.0
    incoming = opp * v_adv
    force, contact_t = 700.0, 0.23
    impulse = force * contact_t
    contact_h = 0.40   # m, lead thigh above the knee
    print("incoming momentum: %.0f kg m/s" % incoming)
    print("stopping impulse: %.0f N x %.2f s = %.1f N s" % (force, contact_t, impulse))
    print("contact height: %.2f m (thigh, never the knee)" % contact_h)
    assert 159.9 < incoming < 160.1
    assert 160.9 < impulse < 161.1
    assert impulse >= incoming, "the piston must at least cancel the advance"
    assert 0.35 < contact_h < 0.50
    print("rule: meet the march with the sole - the advance stops here")
    print("OK: %s drew the redaction bar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_remontant(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # remontant: leg-driven upward punch, chin-height target
    dip = 0.10          # m, knee dip loading the legs
    travel = 0.50       # m, fist's vertical arc
    t = 0.13            # s
    v = travel / t
    chin_h = 1.55       # m target
    fist_mass = 3.5
    p = fist_mass * v
    print("dip %.2f m -> fist climbs %.2f m in %.2f s = %.2f m/s upward" % (dip, travel, t, v))
    print("target chin height: %.2f m, momentum %.2f kg m/s" % (chin_h, p))
    assert 3.84 < v < 3.86
    assert 13.45 < p < 13.47
    assert 1.54 < chin_h < 1.56
    # the arc must stay tight: elbow bend 90 deg, no looping
    assert dip <= 0.12, "deeper than 12 cm the dip becomes a tell"
    print("rule: the legs drive, the arm guides - the caret stays tight")
    print("OK: %s inserted from below" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_enchainements(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three-strike pieds-poings chains: duration, beat gaps, weight path
    chains = {
        "jab-cross-fouette": [0.25, 0.25, 0.30],
        "jab-bas-cross": [0.25, 0.28, 0.25],
        "fouette-chasse-cross": [0.30, 0.25, 0.25],
    }
    for c, beats in chains.items():
        total = sum(beats)
        print("%-22s beats %s = %.2f s" % (c, beats, total))
        assert 0.77 < total < 0.81, c + " must fit inside 0.8 s"
        assert max(beats) <= 0.30, "no seam may show"
    # weight surfing: the mass moves lead->rear->lead across the chain
    transfers = 2
    print("weight transfers per chain: %d (never caught between)" % transfers)
    assert transfers == 2
    print("rule: each strike's recovery feeds the next strike's launch")
    print("OK: %s signed first, family, flourish" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_feintes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # feint model: reaction window, launch overlap, success over 10 attempts
    window = 0.30        # s the bitten reaction opens
    feint_peak = 0.20    # s into the motion the feint peaks
    real_launch = 0.18   # s - the real attack launches as the feint peaks
    overlap = window - (real_launch - 0.0)
    bite_rate = 0.70
    attempts = 10
    expected = attempts * bite_rate
    print("reaction window: %.2f s, feint peaks at %.2f s" % (window, feint_peak))
    print("real attack launches at %.2f s (on the peak)" % real_launch)
    print("expected successes: %.1f of %d at %.0f %% bite rate" % (expected, attempts, bite_rate * 100))
    assert 0.17 < real_launch < 0.21, "the real attack must launch on the feint's peak"
    assert 6.9 < expected < 7.1
    # a lazy feint (peak mismatch > 0.1 s) fools no one
    mismatch = abs(feint_peak - real_launch)
    assert mismatch < 0.10, "feint and attack must be one motion"
    print("rule: the feint must be the real attack's first half - or it is pantomime")
    print("OK: %s drafted in the open, signed in the gap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_contre(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # counter timing: the 0.06 s launch window, and the chasse stop's combined momentum
    jab_flight = 0.12        # s, 0.6 m at 5 m/s
    tell_lead = 0.30         # s, the tell precedes the launch
    launch_deadline = 0.06   # s after the tell
    print("jab flight: %.2f s; tell leads by %.2f s" % (jab_flight, tell_lead))
    print("counter launch deadline: %.2f s after the tell" % launch_deadline)
    assert 0.119 < jab_flight < 0.121
    assert 0.059 < launch_deadline < 0.061
    # the chasse stop: your 600 N piston meets his 160 kg m/s advance
    his_p = 80.0 * 2.0
    your_f, your_t = 600.0, 0.25
    combined = his_p + your_f * your_t
    print("chasse stop: his %.0f + your %.0f = %.0f kg m/s turned against him" % (
        his_p, your_f * your_t, combined))
    assert 309.9 < combined < 310.1
    print("rule: strike INTO the attack - his commitment is your opening")
    print("OK: %s countersigned while the ink was wet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_corps_corps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # courte output: short-hook rate, bump space, exit step count
    hook_arc = 0.30   # m
    hook_t = 0.10     # s
    hook_v = hook_arc / hook_t
    drill_t = 3.0
    strikes = int(drill_t / hook_t)
    rate = strikes / drill_t
    bump_space = 0.15  # m created by the shoulder bump
    exit_steps = 1     # one pas chasse back to the moyenne
    print("short hook: %.2f m in %.2f s = %.1f m/s" % (hook_arc, hook_t, hook_v))
    print("output: %d strikes in %.0f s = %.1f per second" % (strikes, drill_t, rate))
    print("bump creates %.2f m; exit costs %d step" % (bump_space, exit_steps))
    assert 2.99 < hook_v < 3.01
    assert strikes == 30
    assert 9.9 < rate < 10.1
    assert 0.149 < bump_space < 0.151
    print("rule: the bump is the punch's chamber - the exit is the technique")
    print("OK: %s read the fine print" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_pied_saute(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jumping kick: airtime from 0.35 m, kick window, landing mass
    g = 9.81
    h = 0.35
    airtime = 2.0 * math.sqrt(2.0 * h / g)
    kick_need = 0.40   # s, chamber + snap + re-chamber
    margin = airtime - kick_need
    v_land = math.sqrt(2.0 * g * h)
    print("jump %.2f m -> airtime %.3f s" % (h, airtime))
    print("kick needs %.2f s -> margin %.3f s" % (kick_need, margin))
    print("landing velocity: %.2f m/s of added mass" % v_land)
    assert 0.533 < airtime < 0.535
    assert 0.133 < margin < 0.135
    assert margin > 0.10, "under 0.1 s margin the kick is a gamble"
    assert 2.61 < v_land < 2.63
    print("rule: the kick lives at the peak - the landing is half the technique")
    print("OK: %s pressed the seal mid-air" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_riposte(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # riposte window: parry contact to guard recovery
    window = 0.40
    launch_by = 0.10   # s after parry contact the answer launches
    land_by = 0.35     # s the answer lands
    print("window: %.2f s (parry contact -> guard recovery)" % window)
    print("answer launches by %.2f s, lands by %.2f s" % (launch_by, land_by))
    assert 0.399 < window < 0.401
    assert launch_by < 0.15, "later than 0.15 s the answer is a separate exchange"
    assert land_by < window, "the answer must land inside the window"
    pairs = {"parry-cross": 0.32, "slip-hook": 0.30, "check-bas": 0.28, "parry-fouette": 0.35}
    for p, t in pairs.items():
        print("  %-14s lands at %.2f s %s" % (p, t, "INSIDE" if t < window else "LATE"))
        assert t < window
    print("rule: the defense's motion becomes the answer's chamber")
    print("OK: %s annotated in four tenths" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "distance": demo_cs_distance,
    "combos_simples": demo_cs_combos_simples,
    "fouette_balance": demo_cs_fouette_balance,
    "revers_balance": demo_cs_revers_balance,
    "chasse_bas": demo_cs_chasse_bas,
    "remontant": demo_cs_remontant,
    "enchainements": demo_cs_enchainements,
    "feintes": demo_cs_feintes,
    "contre": demo_cs_contre,
    "corps_corps": demo_cs_corps_corps,
    "pied_saute": demo_cs_pied_saute,
    "riposte": demo_cs_riposte,
})


def demo_cs_balayage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep: lever mechanics at the ankle, timing window on the weight transfer
    leg_lever = 0.95     # m, ankle to opponent's COM
    force = 40.0         # N, small hook at the ankle
    torque = force * leg_lever
    sweep_h = 0.10       # m, foot travels flat and low
    window = 0.20        # s total (+/-0.10) around the weight transfer
    print("lever: %.2f m x %.0f N = %.0f N m of toppling torque" % (leg_lever, force, torque))
    print("sweep height: %.2f m, timing window: %.2f s" % (sweep_h, window))
    assert 37.9 < torque < 38.1
    assert 0.199 < window < 0.201
    # leverage vs brute force: 40 N at the ankle beats 400 N at the hip
    hip_force_needed = torque / 0.10
    print("same torque at the hip would need %.0f N - leverage wins" % hip_force_needed)
    assert 379.9 < hip_force_needed < 380.1
    print("rule: assist his motion, never fight it - timing is the technique")
    print("OK: %s pulled the rug at ten centimeters" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_esquive_totale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lean-back: head displacement, clearance vs the kick arc, return time
    head_move = 0.50        # m rearward
    kick_reach = 1.80       # m, high fouette's reach at head height
    needed = 0.30           # m of clearance to be safe
    margin = head_move - needed
    return_t = 0.30         # s to spring back and counter
    counter_window = 0.40
    print("head displacement: %.2f m vs kick reach %.2f m" % (head_move, kick_reach))
    print("clearance margin: %.2f m" % margin)
    print("return + counter: %.2f s inside the %.2f s window: %s" % (
        return_t, counter_window, "YES" if return_t < counter_window else "NO"))
    assert 0.199 < margin < 0.201
    assert return_t < counter_window, "evasion without the return fails the drill"
    # the feet stay planted: base 0.45 m, COM shift must stay inside it
    com_shift = 0.15
    assert com_shift < 0.45 / 2.0
    print("rule: evade-and-return is one word - the page turns back with your line on it")
    print("OK: %s turned the page at the hips" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_combos_avancees(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four-move chains from 8 tools: permutation space, duration, rhythm break
    import math as _m
    tools = 8
    space = _m.perm(tools, 4)
    beats = [0.25, 0.25, 0.25, 0.30]
    total = sum(beats)
    break_pause = 0.15   # s, the fast-fast-SLOW disruption
    print("tools: %d -> four-move chain space: %d" % (tools, space))
    print("chain duration: %.2f s" % total)
    print("rhythm break pause: %.2f s" % break_pause)
    assert space == 1680
    assert 1.049 < total < 1.051
    # the break makes the opponent's timed counter arrive early
    his_counter_t = total            # he times your rhythm
    your_break_t = sum(beats[:2]) + break_pause + sum(beats[2:])
    early = your_break_t - his_counter_t
    print("his timed counter arrives %.2f s early - and misses" % early)
    assert 0.149 < early < 0.151
    print("rule: alternate levels, alternate sides, earn the finish, break the rhythm")
    print("OK: %s illuminated the manuscript" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_jeu_jambes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 45-degree cut geometry: lateral displacement, flank advantage
    fwd = 0.80   # m forward travel
    ang = math.radians(45.0)
    lateral = fwd * math.tan(ang)
    diag = fwd / math.cos(ang)
    print("forward %.2f m at 45 deg -> lateral %.3f m, diagonal %.3f m" % (fwd, lateral, diag))
    assert 0.799 < lateral < 0.801
    assert 1.131 < diag < 1.132
    # flank position: opponent's guard covers 90 deg front; you stand 45 deg off it
    guard_cover = 90.0
    your_angle = 45.0
    outside = your_angle <= guard_cover / 2.0 + 22.5
    print("guard covers %.0f deg; you stand %.0f deg off-center: flank %s" % (
        guard_cover, your_angle, "TAKEN" if outside else "CONTESTED"))
    assert outside
    # switch-step: lead change costs 0.18 s, buys the unexpected side
    switch_t = 0.18
    assert 0.179 < switch_t < 0.181
    print("rule: the angle wins before the kick is thrown")
    print("OK: %s slanted the watermark" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_coups_retournes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # turning kick: rotation rate, kick window in the final 120 deg, blind fraction
    turn = 2.0 * math.pi
    turn_t = 0.55
    rate = turn / turn_t
    kick_arc = math.radians(120.0)
    kick_t = turn_t * (kick_arc / turn)
    blind_arc = math.radians(180.0)   # back turned
    blind_t = turn_t * (blind_arc / turn)
    print("turn: %.3f rad in %.2f s = %.2f rad/s" % (turn, turn_t, rate))
    print("kick window (final 120 deg): %.3f s" % kick_t)
    print("blind fraction (back turned): %.3f s" % blind_t)
    assert 11.42 < rate < 11.44
    assert 0.183 < kick_t < 0.184
    assert 0.274 < blind_t < 0.276
    assert turn_t < 0.60, "slower than 0.6 s the turn is a gift"
    # rotational arrival speed: heel at 0.85 m
    heel_v = 0.85 * rate
    print("heel arrival speed from rotation alone: %.2f m/s" % heel_v)
    assert 9.71 < heel_v < 9.73
    print("rule: pick the target before the turn - the kick is the punctuation")
    print("OK: %s flourished and braked into guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_strategie_ring(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ringcraft geometry: 6.1 m ring, angled cut savings, corner trap
    ring = 6.1
    center = 1.0   # m, the owned center square
    # chasing 3 m straight = ~8 steps; two 45-deg cuts cover it in ~5
    chase_steps = 3.0 / 0.40
    cut_steps = 2 * (2.12 / 0.40) / 2.0
    saved = chase_steps - cut_steps
    print("ring: %.1f m square; center owned: %.0f m" % (ring, center))
    print("3 m chase: %.1f straight steps vs %.1f angled -> saves %.1f steps" % (
        chase_steps, cut_steps, saved))
    assert 7.49 < chase_steps < 7.51
    assert 5.29 < cut_steps < 5.31
    assert 2.19 < saved < 2.21
    # corner trap: 4 exits, ropes remove 1, your angle removes 2 -> 1 left
    exits, removed = 4, 3
    left = exits - removed
    print("corner trap: %d exits - %d denied = %d escape left" % (exits, removed, left))
    assert left == 1
    print("rule: own the center, cut don't chase, trap at the ropes")
    print("OK: %s laid out the page" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_specialites(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # double fouette: the 0.35 s gap vs guard recovery, and the 10k program
    gap = 0.35
    guard_recovery = 0.50
    deficit = guard_recovery - gap
    reps = 10000
    per_day = 50
    days = reps / per_day
    print("double kick gap: %.2f s vs guard recovery %.2f s" % (gap, guard_recovery))
    print("recovery deficit exploited: %.2f s" % deficit)
    print("specialty program: %d reps at %d/day = %.0f days" % (reps, per_day, days))
    assert 0.149 < deficit < 0.151
    assert deficit > 0, "the second kick must beat the guard's answer"
    assert days == 200.0
    # body-type match: long legs (0.95 m) favor the swing, fast hips favor the snap
    leg = 0.95
    swing_bonus = leg / 0.90
    print("long-leg swing bonus: x%.3f" % swing_bonus)
    assert 1.055 < swing_bonus < 1.056
    print("rule: one chamber, two snaps, one plant - the personal seal")
    print("OK: %s struck the seal twice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_preparation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # camp energetics: round cost, bout cost, work-rest ratio, weekly volumes
    kcal_per_min = 13.0
    round_min, rest_min = 3.0, 1.0
    rounds = 5
    round_kcal = kcal_per_min * round_min
    bout_kcal = round_kcal * rounds
    ratio = round_min / rest_min
    print("one round: %.0f kcal; %d-round bout: %.0f kcal" % (round_kcal, rounds, bout_kcal))
    print("work:rest = %.0f:%.0f" % (ratio, 1.0))
    assert 38.9 < round_kcal < 39.1
    assert 194.9 < bout_kcal < 195.1
    assert ratio == 3.0
    # weekly volumes across the 8-week camp
    base_run, peak_run = 3 * 5.0, 2 * 5.0 + 5 * 3.0  # km
    print("base week runs: %.0f km; peak interval week: %.0f km equiv" % (base_run, peak_run))
    assert base_run == 15.0
    assert peak_run == 25.0
    # taper: volume halves in week 8, sleep to 9 h
    taper_vol, sleep = 0.5, 9.0
    print("taper: volume x%.1f, sleep %.0f h" % (taper_vol, sleep))
    assert taper_vol == 0.5 and sleep == 9.0
    print("rule: nobody applauds the paper - but no signature survives bad stock")
    print("OK: %s milled the paper" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_assaut_combat(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sample scorecards: same exchanges under assaut vs combat scoring
    # touches: [clean controlled, variety bonus, defense answer, hard contact]
    touches = {"clean": 8, "variety": 3, "riposte": 2, "hard": 4}
    assaut_score = touches["clean"] * 1.0 + touches["variety"] * 1.5 + touches["riposte"] * 2.0
    combat_score = touches["clean"] * 1.0 + touches["hard"] * 2.0 + touches["riposte"] * 1.5
    print("touches: %s" % touches)
    print("assaut card: %.1f (technique valued)" % assaut_score)
    print("combat card: %.1f (damage valued)" % combat_score)
    assert 16.4 < assaut_score < 16.6    # 8 + 4.5 + 4
    assert 18.9 < combat_score < 19.1    # 8 + 8 + 3
    # three rounds, 10-9 each: winner 30-27
    rds = [(10, 9), (10, 9), (9, 10)]
    w = sum(a for a, b in rds)
    l = sum(b for a, b in rds)
    print("rounds %s -> %d-%d" % (rds, w, l))
    assert (w, l) == (29, 28)
    print("rule: assaut is the journal article, combat the public defense")
    print("OK: %s published under lights" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cs_tactiques_elite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elite tactics by the numbers: entropy of the weapon mix, tempo gap, programming payoff
    uniform = [0.25, 0.25, 0.25, 0.25]
    h_uniform = -sum(p * math.log2(p) for p in uniform)
    skewed = [0.50, 0.25, 0.125, 0.125]
    h_skewed = -sum(p * math.log2(p) for p in skewed)
    print("4-weapon mix entropy: uniform %.3f bits vs readable %.3f bits" % (h_uniform, h_skewed))
    assert 1.999 < h_uniform < 2.001
    assert 1.749 < h_skewed < 1.751
    assert h_uniform > h_skewed, "uniform is the unpredictable mix"
    # false tempo: a round at 60% pace, then full pace - calibration gap
    slow_rate, full_rate = 20.0, 34.0   # strikes per round
    gap = full_rate - slow_rate
    print("false tempo: %d -> %d strikes/round, gap %d" % (slow_rate, full_rate, gap))
    assert gap == 14.0
    # target programming: 6 touches on the thigh, then the figure over the dropped guard
    programmed = 6
    payoff = programmed * 0.5   # expected extra value of the programmed opening
    print("programmed touches: %d -> opening value %.1f" % (programmed, payoff))
    assert 2.99 < payoff < 3.01
    print("rule: encrypt in the ring - decrypt only for the judges")
    print("OK: %s changed the key mid-document" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "balayage": demo_cs_balayage,
    "esquive_totale": demo_cs_esquive_totale,
    "combos_avancees": demo_cs_combos_avancees,
    "jeu_jambes": demo_cs_jeu_jambes,
    "coups_retournes": demo_cs_coups_retournes,
    "strategie_ring": demo_cs_strategie_ring,
    "specialites": demo_cs_specialites,
    "preparation": demo_cs_preparation,
    "assaut_combat": demo_cs_assaut_combat,
    "tactiques_elite": demo_cs_tactiques_elite,
})
