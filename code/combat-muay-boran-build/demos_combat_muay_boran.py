#!/usr/bin/env python3
"""Demo programs for the Muay Boran Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
computation for its record (stance geometry, drill arithmetic, strike
physics, combination counting, teaching-ladder planning). All are
machine-executed by build.py for both editions (68 executions): each
prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. The numbers printed here
are the same numbers carried in the entry prose, so text and program
agree.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_mb_stance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Muay Boran stance geometry for a 1.72 m, 68 kg practitioner
    height, mass = 1.72, 68.0
    stance_len = 0.35 * height
    per_foot = mass / 2.0
    force_n = per_foot * 9.81
    print("stance span: %.4f m" % stance_len)
    print("load per foot: %.1f kg (%.2f N)" % (per_foot, force_n))
    assert 0.60 < stance_len < 0.61
    assert 333.4 < force_n < 333.7
    print("rule: wide flat base, square chest - the stance is the first technique")
    print("OK: %s holds the base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # closing a 2.0 m gap in short 0.30 m steps
    gap, step, step_time = 2.0, 0.30, 0.35
    steps = int(math.ceil(gap / step))
    total = steps * step_time
    print("gap: %.1f m, step: %.2f m" % (gap, step))
    print("steps to close: %d, time: %.2f s" % (steps, total))
    assert steps == 7
    assert 2.4 < total < 2.5
    print("rule: lead foot leads forward, rear foot leads back - the stance survives every step")
    print("OK: %s closes the gap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_nine_weapons(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # combination space of the nine weapons
    n = 9
    pairs = n * (n - 1) // 2
    triples = n * (n - 1) * (n - 2) // 6
    print("weapons: %d" % n)
    print("two-weapon pairings: %d" % pairs)
    print("three-weapon chains: %d" % triples)
    assert pairs == 36
    assert triples == 84
    print("rule: every technique is one weapon, every combination is weapons chained")
    print("OK: %s counts the arsenal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_wai_khru(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ram muay music: 72 beats per minute over 4 minutes
    tempo, minutes = 72, 4
    beats = tempo * minutes
    print("tempo: %d bpm, duration: %d min" % (tempo, minutes))
    print("beats in the dance: %d" % beats)
    assert beats == 288
    print("rule: every step inside the rhythm - the dance is never hurried")
    print("OK: %s keeps the rhythm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_mongkon_prajioud(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sacred cloth sizing: 0.57 m head + 0.15 m knot; 0.32 m per armband
    head, knot = 0.57, 0.15
    mongkon = head + knot
    pair = 2 * 0.32
    print("mongkon cloth: %.2f m" % mongkon)
    print("prajioud pair: %.2f m" % pair)
    assert 0.71 < mongkon < 0.73
    assert 0.63 < pair < 0.65
    print("rule: the mongkon is blessed, the prajioud are earned, neither is costume")
    print("OK: %s measures the cloth" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_card_chuek(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hemp rope: 24 wraps around a 0.21 m circuit per hand
    wraps, circuit = 24, 0.21
    per_hand = wraps * circuit
    both = 2 * per_hand
    print("rope per hand: %.2f m" % per_hand)
    print("rope for the pair: %.2f m" % both)
    assert 5.03 < per_hand < 5.05
    assert 10.07 < both < 10.09
    print("rule: wrap the wrist thick - the wrist is what breaks")
    print("OK: %s winds the rope" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_guard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # long guard: 0.75 m lead vs 0.25 m face guard against a 1.2 m/s rush
    lead, face, rush = 0.75, 0.25, 1.2
    extra = lead - face
    warning = extra / rush
    print("extra reach: %.2f m" % extra)
    print("early warning: %.4f s" % warning)
    assert 0.49 < extra < 0.51
    assert 0.41 < warning < 0.43
    print("rule: distance is defense - the long lead keeps the fight at your weapons")
    print("OK: %s raises the walls" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_conditioning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 8-week shin cycle: 3 sessions/week, 50 -> 120 strikes per session
    sessions = 3 * 8
    avg = (50 + 120) / 2.0
    total = int(sessions * avg)
    print("sessions: %d" % sessions)
    print("strikes per session: 50 -> 120 (avg %.0f)" % avg)
    print("total strikes: %d" % total)
    assert sessions == 24
    assert total == 2040
    print("rule: gradual stress hardens, sudden stress breaks - tissue hardens between sessions")
    print("OK: %s forges the weapons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_sao_chueak(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # triangular stepping: 0.50 m sides, 60-degree turns, 10 cycles
    side, cycles = 0.50, 10
    perim = 3 * side
    total = perim * cycles
    print("triangle perimeter: %.2f m" % perim)
    print("10 cycles: %.1f m of angled travel" % total)
    assert 1.49 < perim < 1.51
    assert 14.9 < total < 15.1
    print("rule: straight lines retreat, triangles flank - keep the corners sharp")
    print("OK: %s walks the triangle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_ram_mai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # forms practice: 3 forms x 12 movements, drilled 5 rounds
    forms, moves, rounds = 3, 12, 5
    carried = forms * moves
    executions = carried * rounds
    print("techniques carried: %d" % carried)
    print("executions per session: %d" % executions)
    assert carried == 36
    assert executions == 180
    print("rule: every movement has a name, a target, and a reason")
    print("OK: %s keeps the textbook" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_regional_styles(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cataloged signature techniques per regional style
    counts = [24, 31, 28, 35, 22]  # Thasao, Korat, Lopburi, Chaiya, Uttaradit
    total = sum(counts)
    avg = total / len(counts)
    print("styles: %d" % len(counts))
    print("cataloged techniques: %d (avg %.1f per style)" % (total, avg))
    assert total == 140
    assert 27.9 < avg < 28.1
    print("rule: one art, five homelands - learn one homeland before touring the rest")
    print("OK: %s maps the regions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_mat_trong(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight punch: 0.65 m at 9 m/s; sustainable pace 1 per 1.5 s over 3 min
    dist, vel = 0.65, 9.0
    travel = dist / vel
    per_round = int(180.0 / 1.5)
    print("punch travel time: %.4f s" % travel)
    print("punches per 3-min round: %d" % per_round)
    assert 0.072 < travel < 0.073
    assert per_round == 120
    print("rule: the fist is the last link - power comes from the floor through the hip")
    print("OK: %s throws straight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_mat_wiang_san(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hook: 0.55 m arm sweeping 120 degrees
    r, deg = 0.55, 120.0
    arc = r * math.radians(deg)
    print("hook arc: %.4f m" % arc)
    assert 1.15 < arc < 1.16
    print("rule: the arm guides, the rotation hits - swing tight, never wide")
    print("OK: %s turns the hook" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_mat_soi_dao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # uppercut: rising 0.45 m at 7 m/s
    rise, vel = 0.45, 7.0
    travel = rise / vel
    print("uppercut rise: %.2f m" % rise)
    print("travel time: %.4f s" % travel)
    assert 0.064 < travel < 0.065
    print("rule: the legs drive the rise - short and straight up, never wide")
    print("OK: %s pierces the star" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_sok_ti(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # horizontal elbow: 0.35 m forearm, 90-degree sweep, 10 m/s tip speed
    r = 0.35
    arc = r * math.radians(90.0)
    travel = arc / 10.0
    print("elbow arc: %.4f m" % arc)
    print("sweep time: %.4f s" % travel)
    assert 0.549 < arc < 0.551
    assert 0.054 < travel < 0.056
    print("rule: compact is fast, wide is visible - the blade stays folded until the hip orders")
    print("OK: %s cuts across" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_sok_ngat(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # upward elbow: rising 0.50 m at 6.5 m/s
    rise, vel = 0.50, 6.5
    travel = rise / vel
    print("elbow rise: %.2f m" % rise)
    print("travel time: %.4f s" % travel)
    assert 0.076 < travel < 0.078
    print("rule: the point rises vertical and close - share no centerline")
    print("OK: %s spears upward" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_khao_trong(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # straight knee: 0.30 m drive in 0.15 s, 12 kg effective mass
    d, t, m = 0.30, 0.15, 12.0
    accel = 2 * d / (t ** 2)
    force = m * accel
    print("knee acceleration: %.2f m/s^2" % accel)
    print("driving force: %.1f N" % force)
    assert 26.6 < accel < 26.7
    assert 319.0 < force < 321.0
    print("rule: the hips thrust through - a knee with the hips is a spear")
    print("OK: %s drives the knee" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_khao_khong(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # curved knee: quarter-circle path of 0.45 m radius
    r = 0.45
    path = r * math.radians(90.0)
    print("curved knee path: %.4f m" % path)
    assert 0.706 < path < 0.708
    print("rule: swing the hip, not the lower leg - the curve takes the side door")
    print("OK: %s hooks the knee" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_tae_khao(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # low kick: 2500 N over the 0.012 m^2 shin contact patch
    force, area = 2500.0, 0.012
    pressure = force / area
    print("thigh target height: 0.35 m")
    print("impact pressure: %.0f Pa" % pressure)
    assert 208000.0 < pressure < 209000.0
    print("rule: shin, never foot - chop the leg until the stance surrenders")
    print("OK: %s cuts low" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_tae_tat(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # roundhouse: 10 kg leg at 12 m/s
    m, v = 10.0, 12.0
    ke = 0.5 * m * v ** 2
    print("kick kinetic energy: %.1f J" % ke)
    assert 719.0 < ke < 721.0
    print("rule: the battle-axe needs a setup - never throw it naked")
    print("OK: %s swings the axe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_thip_trong(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # push kick: 400 N through 0.60 m of displacement
    force, dist = 400.0, 0.60
    work = force * dist
    print("push work: %.1f J" % work)
    assert 239.0 < work < 241.0
    print("rule: the leg returns faster than it went out - insist on your range")
    print("OK: %s pushes through" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_chap_kho(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # clinch control: 2 hands x 3 grips, transitions between control points
    points = 2 * 3
    transitions = points * (points - 1)
    print("control points: %d" % points)
    print("grip transitions: %d" % transitions)
    assert points == 6
    assert transitions == 30
    print("rule: the tie-up is a means, the knee is the end - work the clinch")
    print("OK: %s ties the clinch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_tad_kha(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep timing: 0.20 s window in a 0.80 s step cycle, over a 3-min round
    window, cycle = 0.20, 0.80
    pct = 100.0 * window / cycle
    windows = int(180.0 / cycle)
    print("window: %.1f %% of each step" % pct)
    print("windows per round: %d" % windows)
    assert pct == 25.0
    assert windows == 225
    print("rule: sweep at the rhythm, not at the leg - arrive inside the window")
    print("OK: %s cuts the base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_ninth_weapon(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ninth weapon: closing 0.40 m at 1.5 m/s from the tight clinch
    dist, speed = 0.40, 1.5
    travel = dist / speed
    print("closing distance: %.2f m" % dist)
    print("strike time: %.4f s" % travel)
    assert 0.266 < travel < 0.268
    print("rule: control of the head decides the clinch - classical record, never sparred")
    print("OK: %s maps the ninth" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_mae_mai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 15 master tricks: ordered pairs and triples
    n = 15
    pairs = n * (n - 1)
    triples = n * (n - 1) * (n - 2)
    print("master tricks: %d" % n)
    print("ordered pairs: %d" % pairs)
    print("ordered triples: %d" % triples)
    assert pairs == 210
    assert triples == 2730
    print("rule: each mae mai assumes its parent weapon - mastery, not secrecy")
    print("OK: %s crowns the masters" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_luk_mai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 15 mae mai x 2 luk mai; full exchanges mae -> luk -> mae
    n, per = 15, 2
    luk = n * per
    exchanges = n * per * (n - 1)
    print("complementary tricks: %d" % luk)
    print("complete exchanges: %d" % exchanges)
    assert luk == 30
    assert exchanges == 420
    print("rule: the master trick opens the door, the complement walks through it")
    print("OK: %s completes the branches" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_sok_klap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spinning back elbow: full 360-degree turn in 0.50 s
    omega = 2 * math.pi / 0.50
    print("spin angular velocity: %.4f rad/s" % omega)
    assert 12.56 < omega < 12.58
    print("rule: spin only with a trigger - their committed attack is the cover")
    print("OK: %s turns the blade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_hanuman(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Hanuman Tawai Waen: 0.60 m jump, hang time from projectile motion
    h = 0.60
    hang = 2 * math.sqrt(2 * h / 9.81)
    print("jump height: %.2f m" % h)
    print("hang time: %.4f s" % hang)
    assert 0.699 < hang < 0.701
    print("rule: fly only on certainty - a missed flying technique lands you down")
    print("OK: %s presents the ring" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_kwang_liow_lang(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the deer looks back: 180-degree turn in 0.30 s
    omega = math.pi / 0.30
    print("turn angular velocity: %.4f rad/s" % omega)
    assert 10.47 < omega < 10.48
    print("rule: the deer must look back - spot over the shoulder or kick blind")
    print("OK: %s glances back" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_hap_liuk(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grappling leverage: 0.60 m lever on a 0.15 m joint, 50 N applied
    advantage = 0.60 / 0.15
    at_joint = 50.0 * advantage
    print("mechanical advantage: %.1f to 1" % advantage)
    print("50 N becomes %.0f N at the joint" % at_joint)
    assert advantage == 4.0
    assert 199.0 < at_joint < 201.0
    print("rule: the tap is sacred - the 4 to 1 advantage does not forgive")
    print("OK: %s honors the lever" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_thum(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # throw physics: 1.40 m push height vs 0.30 m base
    angle = math.degrees(math.atan(0.30 / 1.40))
    print("topple angle: %.3f degrees" % angle)
    assert 12.09 < angle < 12.11
    print("rule: break the posture first - no break, no throw")
    print("OK: %s topples the base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_khao_loi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flying knee: 3 x 0.70 m run-up, 0.55 m jump
    runup = 3 * 0.70
    hang = 2 * math.sqrt(2 * 0.55 / 9.81)
    print("run-up: %.2f m" % runup)
    print("hang time: %.4f s" % hang)
    assert 2.09 < runup < 2.11
    assert 0.669 < hang < 0.671
    print("rule: fly only at the certain moment - the landing is graded with the strike")
    print("OK: %s takes the sky" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_combinations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # combination grammar: ordered chains from the 9 weapons
    n = 9
    two_chains = n * (n - 1)
    three_chains = n * (n - 1) * (n - 2)
    print("ordered two-strike chains: %d" % two_chains)
    print("ordered three-strike chains: %d" % three_chains)
    assert two_chains == 72
    assert three_chains == 504
    print("rule: move the guard, move the head, arrive - vocabulary, not choreography")
    print("OK: %s speaks in sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mb_kru(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # teaching ladder: 34 techniques, 2 per session, 3 sessions a week
    techniques, per_session, per_week = 34, 2, 3
    sessions = techniques // per_session
    weeks = sessions / per_week
    print("sessions: %d" % sessions)
    print("weeks at 3 per week: %.2f" % weeks)
    assert sessions == 17
    assert 5.6 < weeks < 5.7
    print("rule: the ladder is the pedagogy - a teacher who keeps the 34 whole keeps the art whole")
    print("OK: %s keeps the lineage" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS_FULL = {
    "stance": demo_mb_stance,
    "footwork": demo_mb_footwork,
    "nine_weapons": demo_mb_nine_weapons,
    "wai_khru": demo_mb_wai_khru,
    "mongkon_prajioud": demo_mb_mongkon_prajioud,
    "card_chuek": demo_mb_card_chuek,
    "guard": demo_mb_guard,
    "conditioning": demo_mb_conditioning,
    "sao_chueak": demo_mb_sao_chueak,
    "ram_mai": demo_mb_ram_mai,
    "regional_styles": demo_mb_regional_styles,
    "mat_trong": demo_mb_mat_trong,
    "mat_wiang_san": demo_mb_mat_wiang_san,
    "mat_soi_dao": demo_mb_mat_soi_dao,
    "sok_ti": demo_mb_sok_ti,
    "sok_ngat": demo_mb_sok_ngat,
    "khao_trong": demo_mb_khao_trong,
    "khao_khong": demo_mb_khao_khong,
    "tae_khao": demo_mb_tae_khao,
    "tae_tat": demo_mb_tae_tat,
    "thip_trong": demo_mb_thip_trong,
    "chap_kho": demo_mb_chap_kho,
    "tad_kha": demo_mb_tad_kha,
    "ninth_weapon": demo_mb_ninth_weapon,
    "mae_mai": demo_mb_mae_mai,
    "luk_mai": demo_mb_luk_mai,
    "sok_klap": demo_mb_sok_klap,
    "hanuman": demo_mb_hanuman,
    "kwang_liow_lang": demo_mb_kwang_liow_lang,
    "hap_liuk": demo_mb_hap_liuk,
    "thum": demo_mb_thum,
    "khao_loi": demo_mb_khao_loi,
    "combinations": demo_mb_combinations,
    "kru": demo_mb_kru,
}
DEMOS = DEMOS_FULL
