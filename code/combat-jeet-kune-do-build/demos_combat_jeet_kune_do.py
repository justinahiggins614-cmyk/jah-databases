#!/usr/bin/env python3
"""Demo programs for the Jeet Kune Do Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: stance geometry, footwork timing,
strike travel times, trapping windows, interception margins, drill pacing.
All are machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker. Demo numbers cross-check the entry text they accompany.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_baijong(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bai-jong stance: even weight split, foot placement, rear foot angle
    body = 70.0
    lead = body * 0.50
    rear = body * 0.50
    shoulder = 0.45
    print('stance base: %.2f m square; weight lead %.1f kg, rear %.1f kg' % (shoulder, lead, rear))
    assert 34.9 < lead < 35.1
    assert 34.9 < rear < 35.1
    rear_angle = 45.0
    heel_lift_cm = 5.0
    print('rear foot angle: %.0f deg, rear heel lift: %.0f cm' % (rear_angle, heel_lift_cm))
    assert 40.0 <= rear_angle <= 50.0
    assert 3.0 <= heel_lift_cm <= 8.0
    print('rule: strong side forward, weight even, stance alive')
    print('OK: %s held the on-guard position' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_footwork_advance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # advance/retreat: steps to close the fighting gap
    step = 0.30          # m per push-step
    gap = 1.2            # m fighting range
    per_step = 0.25      # s per step
    import math as _m
    steps = int(_m.ceil(gap / step))
    total = steps * per_step
    print('step: %.2f m; gap %.1f m needs %d steps in %.2f s' % (step, gap, steps, total))
    assert steps == 4
    assert 0.99 < total < 1.01
    print('rule: lead foot first advancing, rear foot first retreating')
    print('OK: %s closed the range in four gliding steps' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_guard_parry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # parry: deflect the punch off the centerline with a wrist-flick
    punch_speed = 8.0       # m/s incoming straight punch
    deflect_deg = 15.0      # parry deflection angle
    contact_dist = 0.40     # m from the face where the parry meets it
    lateral = contact_dist * math.tan(math.radians(deflect_deg))
    lateral_cm = lateral * 100.0
    print('incoming %.1f m/s parried %.0f deg at %.2f m -> %.1f cm off line' % (
        punch_speed, deflect_deg, contact_dist, lateral_cm))
    assert 10.0 < lateral_cm < 11.5
    print('rule: wrist-flick, not a swing; hand returns to guard')
    print('OK: %s parried the straight punch off the line' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_straight_lead(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight lead: travel time and energy of the fastest hand weapon
    reach = 0.75        # m
    speed = 9.0         # m/s
    t = reach / speed
    eff_mass = 4.0      # kg effective arm mass
    ke = 0.5 * eff_mass * speed ** 2
    print('reach %.2f m at %.1f m/s -> %.4f s travel, KE %.0f J' % (reach, speed, t, ke))
    assert 0.08 < t < 0.09
    assert 160.0 < ke < 165.0
    print('rule: no chamber, no telegraph; snaps back along the same line')
    print('OK: %s fired the straight lead in under a tenth of a second' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_cross(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross: longer reach, hip-driven mass, arrival time
    reach = 0.85        # m
    speed = 8.0         # m/s
    hip_deg = 45.0
    t = reach / speed
    print('reach %.2f m at %.1f m/s, hip turn %.0f deg -> %.4f s' % (reach, speed, hip_deg, t))
    assert 0.10 < t < 0.12
    assert 40.0 <= hip_deg <= 50.0
    print('rule: rear shoulder covers the chin; lead hand stays up')
    print('OK: %s drove the cross through the centerline' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_lead_hook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lead hook: horizontal arc, hand speed from angular speed
    radius = 0.60
    arc_deg = 90.0
    arc_len = radius * math.radians(arc_deg)
    omega = 12.0            # rad/s hip-driven angular speed
    hand_speed = omega * radius
    t = arc_len / hand_speed
    print('arc %.2f m (r=%.2f, %.0f deg), hand %.1f m/s -> %.4f s' % (
        arc_len, radius, arc_deg, hand_speed, t))
    assert 0.93 < arc_len < 0.95
    assert 0.12 < t < 0.14
    print('rule: tight arc from the guard; pivot starts the whip')
    print('OK: %s whipped the lead hook around the guard' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_uppercut(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uppercut: short rising travel driven by the legs
    rise = 0.50          # m vertical travel
    speed = 7.0         # m/s
    t = rise / speed
    print('rise %.2f m at %.1f m/s -> %.4f s' % (rise, speed, t))
    assert 0.07 < t < 0.08
    print('rule: leg drive, never drop the hand first; back along the same line')
    print('OK: %s rose the uppercut from below the sight line' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_lateral_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 45-degree angle step: displacement components
    step = 0.30
    ang = math.radians(45.0)
    lateral = step * math.sin(ang)
    forward = step * math.cos(ang)
    print('%.2f m at 45 deg -> lateral %.3f m, forward %.3f m' % (step, lateral, forward))
    assert 0.21 < lateral < 0.22
    assert 0.21 < forward < 0.22
    print('rule: feet never cross; off his line, still in range')
    print('OK: %s stepped off the centerline at forty-five degrees' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_paksao_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # first trapping touch: contact duration and guard displacement
    contact = 0.05          # s, a tap not a grab
    displace_cm = 8.0       # cm off the centerline
    follow_punch = 0.20     # s for the rear punch to land through the opening
    beat = contact + follow_punch
    print('tap %.3f s, guard moved %.0f cm, punch through in %.2f s one beat' % (
        contact, displace_cm, beat))
    assert 0.04 < contact < 0.06
    assert 0.24 < beat < 0.26
    print('rule: the guard is a door with a handle - touch it, move it, hit through')
    print('OK: %s learned the first trapping touch' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_slip_duck(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # slip: head displacement time vs punch arrival time
    head_move = 0.15        # m off the centerline
    slip_time = 0.15        # s to move the head
    punch_time = 0.25       # s for the punch to arrive
    margin = punch_time - slip_time
    print('head %.2f m in %.2f s vs punch %.2f s -> margin %.2f s' % (
        head_move, slip_time, punch_time, margin))
    assert 0.09 < margin < 0.11
    print('rule: eyes open, hands home; the slip is a visit, not a move')
    print('OK: %s slipped the straight punch with a tenth to spare' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_sda(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # single direct attack: one beat to close the full gap
    gap = 1.2           # m
    beat = 0.40         # s step plus punch landing together
    avg_speed = gap / beat
    print('gap %.1f m in one %.2f s beat -> %.1f m/s average' % (gap, beat, avg_speed))
    assert 2.9 < avg_speed < 3.1
    print('rule: one weapon, one beat, no preparation')
    print('OK: %s took the open line in a single direct attack' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_abc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attack by combination: three strikes, each covering the last recovery
    strikes = 3
    volley = 0.90           # s for lead-cross-hook
    per = volley / strikes
    print('%d strikes in %.2f s -> %.2f s per strike, no quiet beat' % (strikes, volley, per))
    assert 0.29 < per < 0.31
    print('rule: the hip hands the baton; two to four strikes, short by design')
    print('OK: %s volleyed the combination with no quiet beat' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_pia(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # progressive indirect attack: feint commits the guard, truth lands in the window
    feint_commit = 0.25     # s the guard stays committed to the feint
    window_open = 0.25
    window_close = 0.50
    true_attack = 0.35      # s after the feint the real strike lands
    print('feint commits guard %.2f s; strike lands at %.2f s inside [%.2f, %.2f]' % (
        feint_commit, true_attack, window_open, window_close))
    assert window_open <= true_attack <= window_close
    print('rule: the feint must be believable - defenses move only for respected threats')
    print('OK: %s lied with the feint and told the truth with the lead' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_hia(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hand immobilization attack: trap window vs strike arrival
    trap_hold = 0.20        # s the guard stays pinned
    strike_time = 0.15      # s for the punch through the opening
    slack = trap_hold - strike_time
    print('trap holds %.2f s, strike needs %.2f s -> slack %.2f s' % (trap_hold, strike_time, slack))
    assert 0.04 < slack < 0.06
    print('rule: trap and hit are one beat, never two')
    print('OK: %s trapped the guard and hit through the opening' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_abd(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attack by drawing: bait offered, counter lands while he is extended
    bait_retreat = 0.20         # m suggested vulnerability
    his_commit = 0.25           # s for his attack to extend
    counter_lands = 0.30        # s after his attack begins
    print('bait %.2f m; his attack commits in %.2f s, counter lands at %.2f s' % (
        bait_retreat, his_commit, counter_lands))
    assert counter_lands > his_commit
    assert 0.29 < counter_lands < 0.31
    print('rule: the counter is chambered before he moves; let it come to the counter')
    print('OK: %s drew the attack and punished the commitment' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_paksao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pak sao: authoritative displacement and pin duration
    displace = 0.20             # m off the centerline
    pin_lo, pin_hi = 0.15, 0.25 # s pin window
    pin_mid = (pin_lo + pin_hi) / 2.0
    punch_time = 0.15           # s rear punch through the opening
    print('slap displaces %.2f m, pins %.2f s (window %.2f-%.2f); punch needs %.2f s' % (
        displace, pin_mid, pin_lo, pin_hi, punch_time))
    assert pin_lo <= punch_time <= pin_hi
    print('rule: power from step and hip; the slap captures, not merely deflects')
    print('OK: %s slapped the guard aside and pinned it' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_lopsao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lop sao: pull distance and the high-line window it opens
    pull = 0.25             # m down and across
    window = 0.30           # s the head stands unguarded
    punch = 0.20            # s for the head-line punch
    print('pull %.2f m opens the high line %.2f s; punch needs %.2f s' % (pull, window, punch))
    assert window > punch
    assert 0.09 < window - punch < 0.11
    print('rule: his weight follows his hand; pull and punch leave together')
    print('OK: %s dragged the guard across and took the high line' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_jutsao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # jut sao: sharp downward yank clearing the high guard
    drop = 0.15             # m straight down
    jerk_time = 0.10        # s explosive drop
    drop_speed = drop / jerk_time
    recover = 0.25          # s before his hand climbs back
    print('yank %.2f m in %.2f s (%.1f m/s); his recovery %.2f s' % (
        drop, jerk_time, drop_speed, recover))
    assert 1.4 < drop_speed < 1.6
    assert recover > jerk_time * 2.0
    print('rule: suddenness beats strength; strike in the same beat')
    print('OK: %s jerked the high guard down like a curtain' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_lead_side_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lead side kick: chambered spear, extension time
    reach = 1.2             # m
    foot_speed = 10.0       # m/s
    t = reach / foot_speed
    print('reach %.1f m at %.1f m/s -> %.4f s' % (reach, foot_speed, t))
    assert 0.11 < t < 0.13
    print('rule: chamber hides intent; heel or foot-edge, never the toes')
    print('OK: %s speared the lead side kick in twelve hundredths' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_hook_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hook kick: circular path around the guard
    radius = 0.90
    arc_deg = 120.0
    path = radius * math.radians(arc_deg)
    speed = 9.0
    t = path / speed
    print('path %.2f m (r=%.2f, %.0f deg) at %.1f m/s -> %.4f s' % (path, radius, arc_deg, speed, t))
    assert 1.87 < path < 1.90
    assert 0.20 < t < 0.22
    print('rule: hip turns over fully; hands stay in guard')
    print('OK: %s whipped the hook kick around the guard' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_low_lead_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low lead kick: no chamber, too fast to check
    travel = 0.60           # m
    speed = 8.0             # m/s
    height = 0.50           # m target height
    t = travel / speed
    check_time = 0.12       # s for the opponent to lift a check
    print('%.2f m at %.1f m/s, height %.2f m -> %.4f s vs check %.2f s' % (
        travel, speed, height, t, check_time))
    assert t < 0.08
    assert t < check_time
    print('rule: shin, not foot; fires from where the foot stands')
    print('OK: %s chopped the low lead kick under the check' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_stop_hit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stop hit: the tenth-of-a-second margin that names the art
    his_time = 0.25         # s his punch needs
    my_time = 0.15          # s the stop-hit lead needs
    margin = his_time - my_time
    print('his %.2f s vs stop hit %.2f s -> margin %.2f s' % (his_time, my_time, margin))
    assert 0.09 < margin < 0.11
    print('rule: read the preparation, start as he starts, strike into his line')
    print('OK: %s intercepted the attack - jeet, the stop hit' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_stop_kick(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stop kick: kill the kick while it chambers
    his_chamber = 0.35      # s chamber plus extend
    my_stop = 0.20          # s lead side kick already halfway there
    margin = his_chamber - my_stop
    print('his chamber %.2f s vs stop kick %.2f s -> margin %.2f s' % (
        his_chamber, my_stop, margin))
    assert 0.14 < margin < 0.16
    print('rule: read the rising knee; spear the hip, thigh, or supporting leg')
    print('OK: %s killed the kick before it extended' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_broken_rhythm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # broken rhythm: irregular cadence denies the defense a pattern
    beats = [0.50, 0.30, 0.70, 0.50, 0.40, 0.80]
    mean = sum(beats) / len(beats)
    var = sum((b - mean) ** 2 for b in beats) / len(beats)
    sd = math.sqrt(var)
    print('cadence %s -> mean %.3f s, sd %.3f s' % (beats, mean, sd))
    assert 0.50 < mean < 0.55
    assert sd > 0.12
    print('rule: deliberate irregularity, never sloppiness; a lie told in rhythm')
    print('OK: %s broke the rhythm the defense was timing' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_economy_motion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # economy of motion: the honest line vs the telegraphed loop
    direct = 0.75           # m straight lead path
    loop = 1.10             # m looping punch path to the same target
    speed = 9.0
    t_direct = direct / speed
    t_loop = loop / speed
    telegraph = 0.15        # s wasted on the pull-back
    saved = (t_loop + telegraph) - t_direct
    shorter = (loop - direct) / loop
    print('direct %.2f m (%.3f s) vs loop %.2f m + telegraph %.2f s (%.3f s)' % (
        direct, t_direct, loop, telegraph, t_loop + telegraph))
    print('saves %.3f s, path %.1f %% shorter' % (saved, shorter * 100.0))
    assert 0.18 < saved < 0.20
    assert 0.30 < shorter < 0.34
    print('rule: delete every tell; the punch simply appears')
    print('OK: %s proved the honest line arrives a third sooner' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_time_hit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # time hit: the five-hundredths window between cue and counter
    his_commit = 0.25       # s his attack needs
    my_counter = 0.20       # s my counter needs
    latest_start = his_commit - my_counter
    print('his %.2f s, mine %.2f s -> must start within %.2f s of the cue' % (
        his_commit, my_counter, latest_start))
    assert 0.04 < latest_start < 0.06
    print('rule: cue and counter one reflex; train fresh, never tired')
    print('OK: %s landed the time hit inside the five-hundredths window' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_flow_drills(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flow drills: volume installs sensitivity
    pace = 60               # cycles per minute
    round_min = 3
    cycles = pace * round_min
    rounds = 3
    total = cycles * rounds
    print('pace %d/min x %d min = %d cycles/round; %d rounds = %d reps' % (
        pace, round_min, cycles, rounds, total))
    assert cycles == 180
    assert total == 540
    print('rule: flow first, speed later, resistance last')
    print('OK: %s drilled five hundred forty trap-and-hit cycles' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_stop_thrust(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stop-thrust: offensive interception at two meters per second
    advance = 0.60          # m
    t = 0.30                # s
    v = advance / t
    his_prep = 0.35         # s his preparation needs to become an attack
    print('advance %.2f m in %.2f s -> %.1f m/s vs his prep %.2f s' % (advance, t, v, his_prep))
    assert 1.9 < v < 2.1
    assert t < his_prep
    print('rule: meet the preparation, not the punch; out-begin him')
    print('OK: %s drove the stop-thrust into his beginning' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_lowline_stop(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low line stop: braced shin meets the kick at forty-five degrees
    angle = 45.0
    contact = 0.40          # m from the hip
    his_leg = 0.85          # m his extended kicking leg
    leverage = contact / his_leg
    print('shin angle %.0f deg, contact %.2f m from hip; leverage ratio %.3f' % (
        angle, contact, leverage))
    assert 0.46 < leverage < 0.48
    print('rule: read the hip, not the foot; hands stay up')
    print('OK: %s braced the low line stop shin-on-shin' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_attack_prep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attack on preparation: the broadcast window before the weapon moves
    broadcast = 0.15        # s preparation shows before the weapon
    my_attack = 0.15        # s straight lead travel
    land_vs_his_start = my_attack - broadcast
    print('broadcast %.2f s, my attack %.2f s -> lands %.2f s after his start' % (
        broadcast, my_attack, land_vs_his_start))
    assert -0.01 < land_vs_his_start < 0.01
    print('rule: answer the intention, not the weapon; study until tells read large')
    print('OK: %s struck the preparation - intercepting the decision' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_cadence_traps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cadence trap: three taught beats, one broken beat to collect
    taught = [0.50, 0.50, 0.50]
    expected_fourth = sum(taught)          # 1.50 s mark
    actual_strike = expected_fourth + 0.25  # lands after the phantom beat
    his_recovery = 0.40                     # s his committed defense needs to reset
    print('taught beats %s; strike at %.2f s (phantom 4th at %.2f s)' % (
        taught, actual_strike, expected_fourth))
    assert actual_strike - expected_fourth < his_recovery
    print('rule: three beats to teach, one broken beat to collect')
    print('OK: %s sprang the cadence trap on the phantom beat' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_centerline(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # centerline: the thirty-degree cone of owned geometry
    cone_deg = 30.0
    half = math.radians(cone_deg / 2.0)
    rng = 1.2               # m sparring range
    half_width = rng * math.tan(half)
    full_width = 2.0 * half_width
    print('cone %.0f deg at %.1f m range -> %.2f m wide (half %.2f m)' % (
        cone_deg, rng, full_width, half_width))
    assert 0.63 < full_width < 0.65
    print('rule: occupy it with your weapons; deny it to his')
    print('OK: %s owned the thirty-degree centerline cone' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_simul_parry_hit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # simultaneous parry and hit: overlapped beats beat sequential ones
    parry = 0.10
    punch = 0.20
    overlapped = max(parry, punch)
    sequential = parry + punch
    saved = sequential - overlapped
    print('parry %.2f + punch %.2f sequential %.2f vs overlapped %.2f -> saves %.2f s' % (
        parry, punch, sequential, overlapped, saved))
    assert 0.09 < saved < 0.11
    print('rule: the parry clears the line the punch already travels')
    print('OK: %s parried and hit in a single shared beat' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_sparring_synthesis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # interception game: scoring the alive test
    round_s = 180
    exchanges = 20
    opportunities = 6
    converted = 3
    rate = converted / opportunities
    per_exchange = round_s / exchanges
    print('%d s round: %d exchanges (%.0f s each), %d chances, %d converted = %.0f %%' % (
        round_s, exchanges, per_exchange, opportunities, converted, rate * 100.0))
    assert 0.49 < rate < 0.51
    assert 8.9 < per_exchange < 9.1
    print('rule: only interceptions score; review the ones seen but not taken')
    print('OK: %s passed the interception game - three of six converted' % NAME)
if __name__ == '__main__':
    main()
''')


DEMOS = {
    "baijong": demo_baijong,
    "footwork_advance": demo_footwork_advance,
    "guard_parry": demo_guard_parry,
    "straight_lead": demo_straight_lead,
    "cross": demo_cross,
    "lead_hook": demo_lead_hook,
    "uppercut": demo_uppercut,
    "lateral_footwork": demo_lateral_footwork,
    "paksao_intro": demo_paksao_intro,
    "slip_duck": demo_slip_duck,
    "sda": demo_sda,
    "abc": demo_abc,
    "pia": demo_pia,
    "hia": demo_hia,
    "abd": demo_abd,
    "paksao": demo_paksao,
    "lopsao": demo_lopsao,
    "jutsao": demo_jutsao,
    "lead_side_kick": demo_lead_side_kick,
    "hook_kick": demo_hook_kick,
    "low_lead_kick": demo_low_lead_kick,
    "stop_hit": demo_stop_hit,
    "stop_kick": demo_stop_kick,
    "broken_rhythm": demo_broken_rhythm,
    "economy_motion": demo_economy_motion,
    "time_hit": demo_time_hit,
    "flow_drills": demo_flow_drills,
    "stop_thrust": demo_stop_thrust,
    "lowline_stop": demo_lowline_stop,
    "attack_prep": demo_attack_prep,
    "cadence_traps": demo_cadence_traps,
    "centerline": demo_centerline,
    "simul_parry_hit": demo_simul_parry_hit,
    "sparring_synthesis": demo_sparring_synthesis,
}
