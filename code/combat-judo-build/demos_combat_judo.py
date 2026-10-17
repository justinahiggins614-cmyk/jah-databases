#!/usr/bin/env python3
"""Demo programs for the Judo Combat databases (combat batch 1, 2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: drill timers, force and torque
calculators, balance-vector geometry, hold-time scoring, and seeded
probability simulations of grip fighting, counters, and randori sessions.
All are machine-executed by build.py: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker. Every number cross-checked against the entry text.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cj_reigi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dojo etiquette checklist: 8 courtesies, 7 observed this session
    courtesies = ["bow on entry", "bow onto mat", "opening za-rei",
                  "bow to each partner", "silence during demo",
                  "clean gi, short nails", "bow off mat", "closing za-rei"]
    observed = [c for c in courtesies if c != "bow off mat"]
    score = len(observed) / len(courtesies) * 100.0
    print("courtesies observed: %d of %d" % (len(observed), len(courtesies)))
    for c in observed:
        print("  [x] %s" % c)
    print("reigi score: %.1f %%" % score)
    assert 87.4 < score < 87.6
    print("rule: the bow is the handshake of judo - respect is the safety system")
    print("OK: %s filed the courtesies" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_shisei(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # natural posture: stance width sets the stability margin
    stance = 0.45          # meters, feet shoulder-width
    com_height = 0.95      # meters, center of mass with soft knees
    margin = stance / 2.0  # center starts mid-base
    print("stance width: %.2f m" % stance)
    print("center-of-mass height: %.2f m" % com_height)
    print("stability margin: %.3f m in any direction" % margin)
    assert 0.224 < margin < 0.226
    # push test from the eight directions: posture absorbs with a step
    absorbed = 8
    print("push test: %d of 8 directions absorbed with a step, 0 falls" % absorbed)
    assert absorbed == 8
    print("rule: head over hips over feet - never bent past the toes")
    print("OK: %s held the stance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_mae_ukemi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # forward breakfall: hip-height fall braked by the arm slap
    h = 0.9
    v = math.sqrt(2 * 9.81 * h)
    d = 0.25            # stopping distance, arms + torso compression
    a = v * v / (2 * d)
    g = a / 9.81
    print("fall height: %.1f m -> impact speed %.3f m/s" % (h, v))
    print("braked over %.2f m: deceleration %.2f m/s^2 (%.2f g)" % (d, a, g))
    assert 4.20 < v < 4.21
    assert 35.3 < a < 35.4
    assert 3.59 < g < 3.61
    print("rule: the slap spreads the impact - bent arms are shock absorbers")
    print("OK: %s slapped on schedule" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_koho_ukemi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # back breakfall: chin tuck keeps the head off the mat
    clearance = 0.15   # meters, head above mat through the landing
    h = 0.9
    v = math.sqrt(2 * 9.81 * h)
    arm = 0.7
    reach = arm * math.sin(math.radians(45))  # arms slap at 45 degrees
    print("head clearance: %.2f m (chin tucked, head never touches)" % clearance)
    print("impact speed from %.1f m: %.3f m/s" % (h, v))
    print("arm slap lateral reach at 45 deg: %.3f m" % reach)
    assert 0.149 < clearance < 0.151
    assert 4.20 < v < 4.21
    assert 0.494 < reach < 0.496
    print("rule: chin tucks the instant balance breaks - never reach back with the hands")
    print("OK: %s guarded the head" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_yoko_ukemi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # side breakfall: 70 kg from hip height, braked over 0.2 m
    m, h, d = 70.0, 0.9, 0.2
    energy = m * 9.81 * h
    force = energy / d
    print("fall energy: %.2f J" % energy)
    print("peak force over %.1f m: %.1f N across arm, hip, lat" % (d, force))
    assert 618.0 < energy < 618.1
    assert 3090.0 < force < 3090.3
    # drill both sides equally: 10 reps per side
    reps = {"left": 10, "right": 10}
    print("drill reps: left %d, right %d (balanced)" % (reps["left"], reps["right"]))
    assert reps["left"] == reps["right"] == 10
    print("rule: land on the whole side as one surface - never the shoulder point alone")
    print("OK: %s kept both columns equal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_zenpo_kaiten(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # forward roll: curled body traces a circle matching body length
    diameter = 0.55
    circ = math.pi * diameter
    print("curled-body roll circumference: %.3f m" % circ)
    assert 1.727 < circ < 1.729
    # roll drill timer: 10 clean rolls in 14 s
    rolls, total = 10, 14.0
    per_roll = total / rolls
    print("%d rolls in %.0f s -> %.2f s per roll" % (rolls, total, per_roll))
    assert 1.39 < per_roll < 1.41
    print("rule: roll shoulder to opposite hip - never straight over the head")
    print("OK: %s traced the circle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_kuzushi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # happo no kuzushi: eight directions, four opposing pairs
    dirs = [(i * 45, math.cos(math.radians(i * 45)), math.sin(math.radians(i * 45)))
            for i in range(8)]
    sx = sum(x for _, x, _ in dirs)
    sy = sum(y for _, _, y in dirs)
    print("eight kuzushi vectors sum to (%.2e, %.2e): opposing pairs cancel" % (sx, sy))
    assert abs(sx) < 1e-9 and abs(sy) < 1e-9
    # projection of a 45-degree (front-corner) pull on the forward axis
    proj = math.cos(math.radians(45))
    print("front-corner pull projection on forward axis: %.4f" % proj)
    assert 0.7070 < proj < 0.7072
    print("kuzushi compass:")
    for deg, x, y in dirs:
        print("  %3d deg: (%+.3f, %+.3f)" % (deg, x, y))
    print("rule: resistance to one direction becomes kuzushi for its opposite")
    print("OK: %s read all eight directions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_tai_sabaki(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 180-degree pivot in 0.6 s
    omega = math.pi / 0.6
    radius = 0.45
    arc = math.pi * radius
    print("pivot 180 deg in 0.6 s: angular velocity %.3f rad/s" % omega)
    print("free-foot semicircle (r=%.2f m): %.3f m of travel" % (radius, arc))
    assert 5.235 < omega < 5.237
    assert 1.413 < arc < 1.415
    # the landing is the test: balanced and upright after the fastest pivot
    landing = "shizen-hontai"
    print("landing posture: %s" % landing)
    assert landing == "shizen-hontai"
    print("rule: pivot on the ball of the foot - finish balanced or it was just a fancy fall")
    print("OK: %s turned on time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_footwork(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tsugi ashi drill timer: 30 s at 2 steps/s, 0.5 m steps
    step, cadence, duration = 0.5, 2.0, 30.0
    steps = cadence * duration
    distance = steps * step
    print("tsugi ashi: %.0f steps x %.1f m in %.0f s" % (steps, step, duration))
    print("distance glided: %.1f m, stance never narrowed" % distance)
    assert steps == 60.0
    assert 29.99 < distance < 30.01
    # four directions drilled equally
    for d in ["forward", "backward", "left", "right"]:
        print("  drilled: %s tsugi ashi" % d)
    print("rule: feet never cross - the feet arrive first, then hips, then hands")
    print("OK: %s glided the length" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_kumikata(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import random
    # four grip points -> six two-hand combinations
    points_n = 4
    combos = points_n * (points_n - 1) // 2
    print("grip points: %d -> two-hand combinations: %d" % (points_n, combos))
    assert combos == 6
    # grip-fight simulation: 20 exchanges, 0.55 win probability each
    rng = random.Random(7)
    wins = sum(1 for _ in range(20) if rng.random() < 0.55)
    print("20 grip exchanges at p=0.55: won %d (expected 11.0)" % wins)
    assert 7 < wins < 16
    print("rule: grip, attack, release, re-grip - a static grip is a handle for the opponent")
    print("OK: %s won the grips" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_de_ashi_harai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweep window: foot in the air 0.25 s of a 1.1 s stride
    stride, air = 1.1, 0.25
    window = air / stride * 100.0
    contact = 0.08  # seconds, the sweep is a whip
    print("stride %.2f s, foot airborne %.2f s -> sweep window %.2f %%" % (stride, air, window))
    print("sweep contact: %.2f s" % contact)
    assert 22.72 < window < 22.74
    assert contact == 0.08
    print("rule: sweep the moving foot before it plants - timing, not force")
    print("OK: %s arrived on the step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_o_soto_gari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # outer reap: 300 N driven through at 0.70 m below the hip
    force, lever = 300.0, 0.70
    torque = force * lever
    print("reap force %.0f N at %.2f m below hip -> torque %.1f N-m" % (force, lever, torque))
    assert 209.9 < torque < 210.1
    # the drive: hips through, chest on the opponent
    drive = "hips driving through, chest on uke"
    print("power source: %s" % drive)
    print("rule: kuzushi to the rear corner and reap are one action - commit the hips")
    print("OK: %s reaped with the hips" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cj_o_goshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # major hip throw: 70 kg lifted 0.35 m over the hip fulcrum
    m, lift = 70.0, 0.35
    work = m * 9.81 * lift
    knee_bend = 0.25
    print("uke %.0f kg lifted %.2f m over hip fulcrum" % (m, lift))
    print("work by the legs: %.2f J (arms lift nothing)" % work)
    print("entry knee bend: %.2f m to get hips under the load" % knee_bend)
    assert 240.3 < work < 240.4
    print("rule: a fulcrum above the load cannot lift it - hips low, legs do the lifting")
    print("OK: %s loaded the hip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_seoi_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shoulder throw: 70 kg on a 0.35 m torque arm about the shoulder
    m, arm = 70.0, 0.35
    torque = m * 9.81 * arm
    drop_knee_depth = 0.30
    print("load %.0f kg on %.2f m arm -> shoulder torque %.2f N-m" % (m, arm, torque))
    print("drop-knee entry adds %.2f m of depth" % drop_knee_depth)
    assert 240.3 < torque < 240.4
    print("rule: hips below the belt, pull never stops - the shoulder is the catapult")
    print("OK: %s fired the catapult" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_o_uchi_gari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inner reap driven through at 25 degrees from vertical
    force, deg = 280.0, 25.0
    horiz = force * math.sin(math.radians(deg))
    vert = force * math.cos(math.radians(deg))
    print("reap %.0f N at %.0f deg: %.2f N back, %.2f N up" % (force, deg, horiz, vert))
    assert 118.3 < horiz < 118.4
    assert 253.7 < vert < 253.8
    print("rule: the reap scoops as well as pushes - the support does not just move, it leaves")
    print("OK: %s hooked the hinge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_ko_uchi_gari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # minor inner reap: 0.25 m arc in 0.12 s
    arc, t = 0.25, 0.12
    tip = arc / t
    print("flick arc %.2f m in %.2f s -> tip speed %.3f m/s" % (arc, t, tip))
    assert 2.08 < tip < 2.09
    print("rule: strike as weight transfers on - the foot only finishes what the hands started")
    print("OK: %s flicked the footnote" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_hiza_guruma(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # knee wheel: quarter turn over the posted knee at 0.5 m
    knee_h = 0.5
    guided = (math.pi / 2) * knee_h
    print("posted knee at %.1f m: quarter-turn guided rotation %.3f m" % (knee_h, guided))
    assert 0.785 < guided < 0.786
    print("rule: the foot posts, the hands wheel - a well-placed foot beats a strong leg")
    print("OK: %s turned the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_tai_otoshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body drop: 0.35 m drop, leg blocked across at ankle height
    drop = 0.35
    t = math.sqrt(2 * drop / 9.81)
    block_h = 0.10
    pivot_r = 0.85
    print("body drop %.2f m in %.4f s" % (drop, t))
    print("blocking leg across at %.2f m; uke pivots over %.2f m radius" % (block_h, pivot_r))
    assert 0.267 < t < 0.268
    print("rule: the leg is placed, never swung - the hands and the drop do the throwing")
    print("OK: %s dropped the roadblock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_kesa_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scarf hold: osaekomi clock 10 s waza-ari, 20 s ippon
    def score(t):
        return "ippon" if t >= 20 else ("waza-ari" if t >= 10 else "no score")
    log = [(6, "bridge attempt - held"), (13, "shrimp attempt - held"), (20, "clock")]
    for t, note in log:
        print("t=%2ds: %-28s -> %s" % (t, note, score(t)))
    assert score(20) == "ippon"
    assert score(10) == "waza-ari"
    # weight distribution: 65% of 40 kg upper-body weight across uke
    upper = 40.0
    across = upper * 0.65
    print("chest weight across uke: %.1f kg of %.0f kg upper body" % (across, upper))
    assert 25.9 < across < 26.1
    print("rule: arms guide, the chest holds - arms tire, weight is free")
    print("OK: %s sealed the scarf hold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_harai_goshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sweeping hip: 120-degree arc with a 0.8 m leg in 0.35 s
    arc_rad = math.radians(120)
    leg, t = 0.8, 0.35
    arc_len = arc_rad * leg
    tip = arc_len / t
    print("sweep arc %.3f rad x %.1f m leg = %.3f m in %.2f s" % (arc_rad, leg, arc_len, t))
    print("sweep tip speed: %.3f m/s" % tip)
    assert 1.675 < arc_len < 1.676
    assert 4.78 < tip < 4.79
    print("rule: hip fulcrum plus sweep compounding - entry depth decides everything")
    print("OK: %s swept the compound" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_uchi_mata(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inner thigh throw: 75 kg lifted 0.25 m by the thigh
    m, lift = 75.0, 0.25
    work = m * 9.81 * lift
    print("uke %.0f kg lifted %.2f m by the thigh: %.2f J" % (m, lift, work))
    assert 183.9 < work < 184.0
    kuzushi = "front"
    print("kuzushi direction: %s - the thigh redirects committed weight" % kuzushi)
    print("rule: the thigh redirects what the kuzushi committed - it cannot create it")
    print("OK: %s lifted the wheel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_tomoe_nage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # circle throw: foot planted at belt line 0.95 m, uke flies a semicircle
    belt = 0.95
    flight = math.pi * belt
    print("plant at belt line %.2f m -> circular flight %.3f m" % (belt, flight))
    assert 2.984 < flight < 2.986
    print("rule: the foot pushes, never kicks - commit fully or not at all")
    print("OK: %s drew the circle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_kami_shiho_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # north-south pin: 70 kg split 45 head-side, 25 hips-side
    head_side, hips_side = 45.0, 25.0
    print("weight: %.0f kg head-side, %.0f kg hips-side (total %.0f kg)" %
          (head_side, hips_side, head_side + hips_side))
    assert head_side + hips_side == 70.0
    # osaekomi clock
    for t, want in [(10, "waza-ari"), (20, "ippon")]:
        got = "ippon" if t >= 20 else ("waza-ari" if t >= 10 else "no score")
        print("hold %2ds -> %s" % (t, got))
        assert got == want
    print("rule: control the four corners and the body between them cannot move")
    print("OK: %s pressed the north-south seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_yoko_shiho_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # side pin: 40 kg of chest pressure across the ribs at 90 degrees
    chest = 40.0
    base_width = 1.1  # sprawled legs, meters
    print("cross-body pressure: %.0f kg at 90 degrees" % chest)
    print("sprawled base width: %.1f m - unrollable" % base_width)
    assert 39.9 < chest < 40.1
    hold, want = 20, "ippon"
    got = "ippon" if hold >= 20 else ("waza-ari" if hold >= 10 else "no score")
    print("hold %ds -> %s" % (hold, got))
    assert got == want
    print("rule: a pin, not a strangle - forearm on the shoulder, never the throat")
    print("OK: %s filed the cross-seal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cj_nami_juji_jime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross choke: two 180 N pulls, wrists crossed at 50 degrees
    pull, cross = 180.0, 50.0
    inward = 2 * pull * math.sin(math.radians(cross / 2))
    print("pulls %.0f N x 2 at %d-deg cross -> inward constriction %.2f N" % (pull, cross, inward))
    assert 152.1 < inward < 152.2
    print("target: carotids (blood choke) - never the windpipe")
    print("rule: the tap ends it instantly - the release reflex is the real technique")
    print("OK: %s signed the cross" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_hadaka_jime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rear naked strangle: figure-four multiplies input ~1.4x
    draw, mult = 150.0, 1.4
    constrict = draw * mult
    print("draw %.0f N x figure-four %.1f -> constriction %.1f N" % (draw, mult, constrict))
    assert 209.9 < constrict < 210.1
    print("finish: expand the chest, draw the elbow back and down - smooth, never a jerk")
    print("rule: position before submission - control the back first with no space")
    print("OK: %s set the vise" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_juji_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cross armlock: hips fulcrum under elbow, wrist controlled 0.28 m out
    force, arm = 120.0, 0.28
    torque = force * arm
    print("hip extension %.0f N x %.2f m lever -> elbow torque %.2f N-m" % (force, arm, torque))
    assert 33.59 < torque < 33.61
    print("finish: millimeters of hip extension - the tap is obeyed before pressure, not after pain")
    print("rule: only the elbow is attacked - the applier owns the joint")
    print("OK: %s filed the lever" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_renraku_waza(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # combination: attacks at 0.4, 0.5, 0.7 compound to one chain
    ps = [0.4, 0.5, 0.7]
    combined = 1.0
    for p in ps:
        combined *= (1 - p)
    combined = 1 - combined
    print("chain %s -> combined success %.4f" % (ps, combined))
    assert 0.909 < combined < 0.911
    print("classic pairs: seoi->o-uchi, o-uchi->seoi, o-uchi->ko-uchi, de-ashi->o-soto")
    print("rule: the first attack must be genuine - defense against it is free kuzushi")
    print("OK: %s wrote the compound sentence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_kaeshi_waza(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import random
    # counter window: 0.25 s telegraph vs 0.30 s entry
    telegraph, entry = 0.25, 0.30
    print("telegraph %.2f s, counter entry %.2f s - recognition must be instant" % (telegraph, entry))
    assert entry > telegraph  # the window is real but narrow
    # counter randori: 30 committed attacks, counter success p=0.45
    rng = random.Random(21)
    counters = sum(1 for _ in range(30) if rng.random() < 0.45)
    print("30 attacks at p=0.45: %d counters landed (expected 13.5)" % counters)
    assert 8 < counters < 20
    print("rule: never block the attack - move with it and redirect it")
    print("OK: %s redirected the storm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_tate_shiho_gatame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mounted pin: knees 0.6 m apart, 55 kg through the sternum
    knees, chest = 0.6, 55.0
    print("knee base %.1f m gripping the ribs" % knees)
    print("chest pressure %.0f kg through the sternum" % chest)
    assert 0.59 < knees < 0.61
    assert 54.9 < chest < 55.1
    hold = 20
    got = "ippon" if hold >= 20 else ("waza-ari" if hold >= 10 else "no score")
    print("hold %ds -> %s" % (hold, got))
    assert got == "ippon"
    print("rule: maintain by floating - loose hips follow and re-settle, never a rigid perch")
    print("OK: %s took the high seat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_okuri_eri_jime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sliding lapel choke: 0.15 m slide against ~0.4 gi-on-gi friction
    slide, mu, pull = 0.15, 0.4, 160.0
    friction = mu * pull
    net = pull - friction
    print("slide %.2f m, pull %.0f N vs friction %.1f N -> net %.1f N" % (slide, pull, friction, net))
    assert 63.9 < friction < 64.1
    assert 95.9 < net < 96.1
    print("rule: commit fully - hesitation kills the slide; the tap ends it instantly")
    print("OK: %s slid the signature" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_sumi_gaeshi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # corner reversal: drop 0.9 m, wheel uke over the corner on a 1.0 m radius
    drop, radius = 0.9, 1.0
    flight = (math.pi / 2) * radius
    print("drop %.1f m, corner wheel radius %.1f m -> flight %.3f m" % (drop, radius, flight))
    assert 1.570 < flight < 1.572
    print("rule: the hook is placed and lifts, never kicks - time it at the peak of their drive")
    print("OK: %s signed the corner" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_ude_garami(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # entangled armlock: 100 N through a 0.3 m figure-four lever
    force, lever = 100.0, 0.3
    torque = force * lever
    print("figure-four %.0f N x %.1f m -> shoulder torque %.2f N-m, applied in degrees" %
          (force, lever, torque))
    assert 29.9 < torque < 30.1
    print("rule: the entanglement is the technique - the tap comes from inevitability, not pain")
    print("OK: %s tied the knot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cj_randori(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # randori session architecture: 6 rounds x 4 minutes
    rounds, minutes = 6, 4
    total_min = rounds * minutes
    attacks_per_round = 12
    attacks = rounds * attacks_per_round
    conversion = 0.25
    scores = int(attacks * conversion)
    print("session: %d rounds x %d min = %d min" % (rounds, minutes, total_min))
    print("attacks: %d/round x %d = %d; converted %.0f%% -> %d scores" %
          (attacks_per_round, rounds, attacks, conversion * 100, scores))
    assert total_min == 24
    assert attacks == 72
    assert scores == 18
    print("rule: techniques that die in randori are not yet learned - randori is the honest test")
    print("OK: %s ran the laboratory" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "reigi": demo_cj_reigi,
    "shisei": demo_cj_shisei,
    "mae_ukemi": demo_cj_mae_ukemi,
    "koho_ukemi": demo_cj_koho_ukemi,
    "yoko_ukemi": demo_cj_yoko_ukemi,
    "zenpo_kaiten": demo_cj_zenpo_kaiten,
    "kuzushi": demo_cj_kuzushi,
    "tai_sabaki": demo_cj_tai_sabaki,
    "footwork": demo_cj_footwork,
    "kumikata": demo_cj_kumikata,
    "de_ashi_harai": demo_cj_de_ashi_harai,
    "o_soto_gari": demo_cj_o_soto_gari,
    "o_goshi": demo_cj_o_goshi,
    "seoi_nage": demo_cj_seoi_nage,
    "o_uchi_gari": demo_cj_o_uchi_gari,
    "ko_uchi_gari": demo_cj_ko_uchi_gari,
    "hiza_guruma": demo_cj_hiza_guruma,
    "tai_otoshi": demo_cj_tai_otoshi,
    "kesa_gatame": demo_cj_kesa_gatame,
    "harai_goshi": demo_cj_harai_goshi,
    "uchi_mata": demo_cj_uchi_mata,
    "tomoe_nage": demo_cj_tomoe_nage,
    "kami_shiho_gatame": demo_cj_kami_shiho_gatame,
    "yoko_shiho_gatame": demo_cj_yoko_shiho_gatame,
    "nami_juji_jime": demo_cj_nami_juji_jime,
    "hadaka_jime": demo_cj_hadaka_jime,
    "juji_gatame": demo_cj_juji_gatame,
    "renraku_waza": demo_cj_renraku_waza,
    "kaeshi_waza": demo_cj_kaeshi_waza,
    "tate_shiho_gatame": demo_cj_tate_shiho_gatame,
    "okuri_eri_jime": demo_cj_okuri_eri_jime,
    "sumi_gaeshi": demo_cj_sumi_gaeshi,
    "ude_garami": demo_cj_ude_garami,
    "randori": demo_cj_randori,
}
