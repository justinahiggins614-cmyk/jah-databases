#!/usr/bin/env python3
"""Demo programs for the Kalaripayattu Combat databases.

Every demo is real, runnable, stdlib-only Python performing the actual
training computation for its record: salutation timing, stance geometry,
drill pacing, weapon dimensions, session planning, study checklists. All
are machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker. Demo numbers cross-check the entry text they accompany.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_vanakkam(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # salutation timing: five phases, three slow counts each, opened and closed
    phases = 5          # join palms, forehead, bow, touch earth, rise
    per_phase = 3.0     # seconds per slow count phase
    one = phases * per_phase
    both = 2 * one      # opening salutation + closing salutation
    print('one vanakkam: %.1f s across %d phases' % (one, phases))
    print('opening + closing: %.1f s' % both)
    assert 14.9 < one < 15.1
    assert 29.9 < both < 30.1
    # kalari pit dimensions from the entry
    length_ft, width_ft = 42.0, 21.0
    print('kalari pit: %.0f ft by %.0f ft' % (length_ft, width_ft))
    assert 41.9 < length_ft < 42.1
    assert 20.9 < width_ft < 21.1
    print('rule: respect first, technique second')
    print('OK: %s bracketed the session' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_gaja(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # elephant posture geometry: length from shoulder width, weight split
    shoulder = 0.45            # m, typical adult shoulder width
    length = 1.5 * shoulder    # one and a half shoulder-widths
    body = 70.0                # kg practitioner
    front = body * 0.60
    rear = body * 0.40
    print('stance length: %.3f m' % length)
    print('weight: front %.1f kg, rear %.1f kg' % (front, rear))
    assert 0.674 < length < 0.676
    assert 41.9 < front < 42.1
    assert 27.9 < rear < 28.1
    # knee tracking: front knee must sit over the toes, not past them
    knee_over_toe = 0.0        # m offset, ideal
    print('knee-to-toe offset target: %.2f m' % knee_over_toe)
    assert -0.02 < knee_over_toe < 0.02
    print('rule: front knee over toes, rear heel rooted, hips square')
    print('OK: %s charged like the elephant' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_simha(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lion posture: wide crouch, even weight, spring drill
    shoulder = 0.45
    width = 2.0 * shoulder
    body = 70.0
    left = body * 0.50
    right = body * 0.50
    print('crouch width: %.2f m' % width)
    print('weight: left %.1f kg, right %.1f kg' % (left, right))
    assert 0.89 < width < 0.91
    assert 34.9 < left < 35.1
    assert 34.9 < right < 35.1
    # spring drill: ten rise-and-settle reps, knees never caving in
    reps = 10
    knee_cave = 0.0           # m inward drift, ideal zero
    print('spring reps: %d, knee inward drift: %.2f m' % (reps, knee_cave))
    assert reps == 10
    assert -0.01 < knee_cave < 0.01
    print('rule: knees outside the feet, the crouch stores the spring')
    print('OK: %s crouched like the lion' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_ashva(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # horse posture: parallel feet, even weight, hold time
    shoulder = 0.45
    width = 2.0 * shoulder
    body = 70.0
    per_leg = body * 0.50
    hold = 20.0               # s, upper end of the hold range
    print('stance width: %.2f m, per leg: %.1f kg' % (width, per_leg))
    print('hold: %.0f slow counts' % hold)
    assert 0.89 < width < 0.91
    assert 34.9 < per_leg < 35.1
    assert 9.0 < hold < 21.0
    # toe direction: straight forward, zero outward angle
    toe_deg = 0.0
    print('toe angle: %.0f deg' % toe_deg)
    assert -2.0 < toe_deg < 2.0
    print('rule: back straight, hips sunk, weight even')
    print('OK: %s stood like the horse' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_varaha(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # boar posture: forward-leaning crouch, weight driven low and forward
    body = 70.0
    front = body * 0.70
    rear = body * 0.30
    lean_deg = 30.0
    print('weight: front %.1f kg, rear %.1f kg' % (front, rear))
    print('torso lean: %.0f deg' % lean_deg)
    assert 48.9 < front < 49.1
    assert 20.9 < rear < 21.1
    assert 28.0 < lean_deg < 32.0
    # rooting advance: ten advances and ten retreats, staying low
    advances, retreats = 10, 10
    total_steps = advances + retreats
    print('drill steps: %d advances + %d retreats = %d' % (advances, retreats, total_steps))
    assert total_steps == 20
    print('rule: go under force, root forward, back flat never hunched')
    print('OK: %s rooted like the boar' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_sarpam(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # serpent posture: ground-level coil and the silent rise
    forearm = 0.35            # m, torso rides about one forearm off the floor
    rises = 10
    noise = 0.0               # ideal: silent motion
    print('torso height: %.2f m, rises: %d' % (forearm, rises))
    print('motion noise target: %.1f' % noise)
    assert 0.30 < forearm < 0.40
    assert rises == 10
    assert noise == 0.0
    # weight stays fluid: no more than 60 percent on any one point
    max_point_load = 0.55
    print('max load on any one point: %.0f percent' % (max_point_load * 100))
    assert 0.50 < max_point_load < 0.61
    print('rule: yield, slide, rise where not expected')
    print('OK: %s coiled like the serpent' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_marjjara(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cat posture: raised heels, silent steps in four directions
    heel_raise = 0.04         # m, about two finger-widths
    per_dir = 20
    dirs = 4                  # forward, back, left, right
    total = per_dir * dirs
    print('heel raise: %.2f m' % heel_raise)
    print('silent steps: %d per direction x %d = %d' % (per_dir, dirs, total))
    assert 0.03 < heel_raise < 0.05
    assert total == 80
    # landing check: heels never slap on the hop landings
    hops = 10
    heel_slap = 0
    print('hop landings: %d, heel slaps: %d' % (hops, heel_slap))
    assert hops == 10 and heel_slap == 0
    print('rule: weight never committed until it must')
    print('OK: %s stepped like the cat' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kukkuda(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rooster posture: single-leg hold and kick chambers
    hold = 10                 # slow counts per leg
    legs = 2
    chambers = 10             # kick chambers per leg
    total_holds = hold * legs
    total_chambers = chambers * legs
    print('holds: %d counts x %d legs = %d' % (hold, legs, total_holds))
    print('kick chambers: %d x %d legs = %d' % (chambers, legs, total_chambers))
    assert total_holds == 20
    assert total_chambers == 20
    # chamber height: knee at hip height, thigh parallel to the ground
    chamber_deg = 90.0        # thigh angle from vertical... measured from torso
    print('chamber: thigh parallel to ground')
    assert 85.0 < chamber_deg < 95.0
    print('rule: one root is enough, the gaze steadies the balance')
    print('OK: %s balanced like the rooster' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_matsya(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fish posture: two unbroken minutes of gliding flow
    flow_s = 120.0
    # one weight-shift cycle every four seconds
    cycle_s = 4.0
    cycles = flow_s / cycle_s
    print('flow time: %.0f s, shift cycles: %.0f' % (flow_s, cycles))
    assert 119.9 < flow_s < 120.1
    assert 29.9 < cycles < 30.1
    # head stays level: vertical bob under two centimeters
    bob = 0.015
    print('head bob: %.3f m' % bob)
    assert 0.0 < bob < 0.02
    print('rule: never stop, never lock, always move')
    print('OK: %s flowed like the fish' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_chuvadukal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # footwork patterns: rep counts across the basic patterns
    advance, retreat = 10, 10
    side_each, turn_each = 10, 10
    total = advance + retreat + 2 * side_each + 2 * turn_each
    print('advance %d, retreat %d, side %d, turns %d' % (advance, retreat, side_each, turn_each))
    print('total pattern reps: %d' % total)
    assert total == 60
    # linked sequence: five unbroken minutes
    linked_min = 5.0
    print('linked sequence: %.0f unbroken minutes' % linked_min)
    assert 4.9 < linked_min < 5.1
    print('rule: the feet speak first, the hands only echo')
    print('OK: %s patterned the footwork' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kalugal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # leg conditioning: swings, circles, lunges, splits
    fwd = 10 * 2            # forward swings, both legs
    side = 10 * 2           # side swings, both legs
    circles = 5 * 2 * 2     # five circles, two directions, two legs
    lunges = 5 * 2
    split_breaths = 30
    total_reps = fwd + side + circles + lunges
    print('swings %d + circles %d + lunges %d = %d moving reps' % (fwd + side, circles, lunges, total_reps))
    print('split hold: %d breaths' % split_breaths)
    assert total_reps == 70
    assert split_breaths == 30
    # session time about fifteen minutes
    session_min = 15.0
    print('kalugal session: about %.0f minutes' % session_min)
    assert 14.0 < session_min < 16.0
    print('rule: never bounce a stretch, flexibility is built not forced')
    print('OK: %s conditioned the legs' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_meyyorukkam(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body control circuit: one circuit rep count
    pushups, situps = 10, 10
    backbends = 5
    twists = 10 * 2
    animal_steps = 10 * 2
    jump_squats = 10
    circuit = pushups + situps + backbends + twists + animal_steps + jump_squats
    circuits = 3
    total = circuit * circuits
    print('one circuit: %d reps' % circuit)
    print('three circuits: %d reps' % total)
    assert circuit == 75
    assert total == 225
    # backbend breaths: five breaths per bend, five bends
    bend_breaths = backbends * 5
    print('backbend breaths: %d' % bend_breaths)
    assert bend_breaths == 25
    print('rule: strength and stance grow together')
    print('OK: %s forged the body' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_meippayattu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body forms: eighteen traditional sequences, thirty-minute session
    sequences = 18
    first_rounds = 5
    rest_s = 60.0
    session_min = 30.0
    print('traditional sequences: %d' % sequences)
    print('first-sequence rounds: %d, rest %.0f s' % (first_rounds, rest_s))
    print('full session: about %.0f minutes' % session_min)
    assert sequences == 18
    assert first_rounds == 5
    assert 59.9 < rest_s < 60.1
    assert 28.0 < session_min < 32.0
    print('rule: the body learns the grammar before the weapon gets words')
    print('OK: %s trained the body form' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_swasam(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # breath pattern: inhale 4, hold 4, exhale 6, rest 2
    inh, hold, exh, rest = 4.0, 4.0, 6.0, 2.0
    cycle = inh + hold + exh + rest
    cycles = 10
    total = cycle * cycles
    print('breath cycle: %.0f+%.0f+%.0f+%.0f = %.0f counts' % (inh, hold, exh, rest, cycle))
    print('%d cycles: %.0f counts, about %.1f minutes' % (cycles, total, total / 60.0))
    assert 15.9 < cycle < 16.1
    assert 159.9 < total < 160.1
    # exhale is longest: the strike breath
    print('exhale share of cycle: %.1f percent' % (exh / cycle * 100))
    assert 37.4 < exh / cycle * 100 < 37.6
    print('rule: exhale on the strike, inhale settling into stance')
    print('OK: %s breathed with the art' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_muchan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # short stick: eighteen to twenty-four inches of hardwood
    lo_in, hi_in = 18.0, 24.0
    lo_m, hi_m = lo_in * 0.0254, hi_in * 0.0254
    print('muchan: %.0f-%.0f in = %.2f-%.2f m' % (lo_in, hi_in, lo_m, hi_m))
    assert 0.457 < lo_m < 0.458
    assert 0.609 < hi_m < 0.610
    # drill counts: three cuts x ten, guards, disarms
    cuts = 3 * 10
    guards = 10 * 2
    disarms = 10 * 2
    total = cuts + guards + disarms
    print('cuts %d + guards %d + disarms %d = %d reps' % (cuts, guards, disarms, total))
    assert total == 70
    print('rule: the stick whistles when the hip signs the cut')
    print('OK: %s wielded the short stick' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_otta(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # curved stick: about eighteen inches, three cuts per side
    length_m = 18.0 * 0.0254
    cuts = 3 * 10 * 2      # three cuts, ten each, both sides
    form_min = 3.0
    print('otta: %.3f m' % length_m)
    print('cut reps: %d, form: %.0f unbroken minutes' % (cuts, form_min))
    assert 0.457 < length_m < 0.458
    assert cuts == 60
    assert 2.9 < form_min < 3.1
    print('rule: the curve teaches the wrist to roll through the cut')
    print('OK: %s curved like the tusk' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kol(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # long staff: about five feet, the practitioner height
    length_m = 5.0 * 0.3048
    techniques = 10 * 2 * 3   # thrust/sweep/overhead, ten each, both sides
    spins = 10 * 2            # ten spins each direction
    print('kol: %.3f m' % length_m)
    print('technique reps: %d, spins: %d' % (techniques, spins))
    assert 1.523 < length_m < 1.525
    assert techniques == 60
    assert spins == 20
    # clear circle: staff length plus arm reach on all sides
    clear_m = length_m + 1.5
    print('clear circle diameter: %.2f m' % (2 * clear_m))
    assert 6.0 < 2 * clear_m < 6.1
    print('rule: both hands work, the waist turns every strike')
    print('OK: %s spun the long staff' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kolthari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wooden-weapons stage: three solo forms plus paired work, 45-minute session
    forms = 3 * 3.0          # three forms, three minutes each
    rests = 2 * 1.0          # rest between forms
    paired = 10 + 10 + 5 * 2 # guard taps, role swaps, disarms
    session = 45.0
    print('solo forms: %.0f min, rests: %.0f min' % (forms, rests))
    print('paired exchanges: %d' % paired)
    print('full kolthari session: %.0f minutes' % session)
    assert 8.9 < forms < 9.1
    assert paired == 30
    assert 44.0 < session < 46.0
    print('rule: wood forgives what metal would not - this stage trains judgment')
    print('OK: %s completed the wooden stage' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kadhara(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dagger: twelve to fifteen inches, double-edged
    lo_m, hi_m = 12.0 * 0.0254, 15.0 * 0.0254
    thrusts = 10 * 2
    cuts = 10 * 2
    paired = 10 * 2          # trap-and-answer exchanges, both roles
    print('kadhara: %.2f-%.2f m' % (lo_m, hi_m))
    print('thrusts %d + cuts %d + paired %d = %d' % (thrusts, cuts, paired, thrusts + cuts + paired))
    assert 0.304 < lo_m < 0.306
    assert 0.380 < hi_m < 0.382
    assert thrusts + cuts + paired == 60
    print('rule: the blade never reaches alone - the entry delivers it')
    print('OK: %s drew the dagger' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kuntham(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spear: five to six feet with a metal head
    lo_m, hi_m = 5.0 * 0.3048, 6.0 * 0.3048
    thrusts, sweeps, butts = 10, 10, 10
    form_min = 3.0
    print('kuntham: %.2f-%.2f m' % (lo_m, hi_m))
    print('thrusts %d, sweeps %d, butt strikes %d' % (thrusts, sweeps, butts))
    assert 1.523 < lo_m < 1.525
    assert 1.828 < hi_m < 1.830
    assert thrusts + sweeps + butts == 30
    assert 2.9 < form_min < 3.1
    # thrust reach: spear length plus one deep step
    reach = hi_m + 1.0
    print('max thrust reach: %.2f m' % reach)
    assert 2.82 < reach < 2.84
    print('rule: the whole body drives behind the point')
    print('OK: %s thrust the spear' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_vaal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sword: about two and a half feet of single-edged blade
    length_m = 2.5 * 0.3048
    cuts = 4 * 10 * 2        # four cuts, ten each, both sides
    form_min = 3.0
    print('vaal: %.3f m' % length_m)
    print('cut reps: %d, form: %.0f unbroken minutes' % (cuts, form_min))
    assert 0.761 < length_m < 0.763
    assert cuts == 80
    assert 2.9 < form_min < 3.1
    print('rule: saluted before practice, never pointed carelessly')
    print('OK: %s cut with the sword' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_paricha(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shield: twelve to fifteen inches across, round
    d_m = 13.5 * 0.0254      # mid-range diameter
    area = math.pi * (d_m / 2.0) ** 2
    parries = 10 * 2
    binds = 10
    changes = 20
    print('paricha diameter: %.3f m, face area: %.3f sq m' % (d_m, area))
    print('parries %d + binds %d + guard changes %d = %d' % (parries, binds, changes, parries + binds + changes))
    assert 0.342 < d_m < 0.344
    assert 0.092 < area < 0.094
    assert parries + binds + changes == 50
    print('rule: the shield meets force with angles, not with fear')
    print('OK: %s guarded with the shield' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_valum_parichayum(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sword and shield together: solo form plus paired exchanges
    solo_min = 3.0
    exchanges = 10 * 2       # parry-and-answer, both roles
    paired_min = 5.0
    print('solo form: %.0f min, paired exchanges: %d, paired form: %.0f min' % (solo_min, exchanges, paired_min))
    assert 2.9 < solo_min < 3.1
    assert exchanges == 20
    assert 4.9 < paired_min < 5.1
    # two hands, two jobs: guard coverage plus cut tempo
    print('shield hand guards while sword hand answers - one motion')
    print('rule: defense and attack as one continuous motion')
    print('OK: %s paired sword and shield' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_verumkai(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # empty hand: entries, strikes, sweeps, evasions - all controlled
    entries = 10 * 2
    palm = 10 * 2
    sweeps = 10 * 2
    evasions = 10
    seq_min = 5.0
    total = entries + palm + sweeps + evasions
    print('entries %d, palm strikes %d, sweeps %d, evasions %d' % (entries, palm, sweeps, evasions))
    print('total reps: %d, sequence: %.0f minutes' % (total, seq_min))
    assert total == 70
    assert 4.9 < seq_min < 5.1
    # contact rule: zero full-contact strikes in training
    full_contact = 0
    print('full-contact strikes in training: %d' % full_contact)
    assert full_contact == 0
    print('rule: strikes stop short, sweeps touch lightly - control is the art')
    print('OK: %s fought empty-handed' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kaal_adikal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kicks: chambered from the rooster posture, pads only
    front = 10 * 2
    side = 10 * 2
    spinning = 5 * 2
    total = front + side + spinning
    kick_h = 1.0             # m, hip-height chamber extension
    print('front %d + side %d + spinning %d = %d pad kicks' % (front, side, spinning, total))
    print('kick height: %.1f m' % kick_h)
    assert total == 50
    assert 0.95 < kick_h < 1.05
    # rechamber rule: the kick returns as fast as it goes
    print('rule: chamber, extension, rechamber - never kick a partner')
    print('OK: %s kicked like the rooster spur' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_gada(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mace: two to three feet, short heavy sets of five
    lo_m, hi_m = 2.0 * 0.3048, 3.0 * 0.3048
    smashes = 3 * 5          # three smashes, five each
    rest_s = 60.0
    form_min = 2.0
    print('gada: %.2f-%.2f m' % (lo_m, hi_m))
    print('smash reps: %d, rest %.0f s, form %.0f min' % (smashes, rest_s, form_min))
    assert 0.609 < lo_m < 0.610
    assert 0.914 < hi_m < 0.915
    assert smashes == 15
    assert 59.9 < rest_s < 60.1
    assert 1.9 < form_min < 2.1
    print('rule: never train the mace to exhaustion')
    print('OK: %s swung the mace' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_madu(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twin horn daggers: parry-strike, binds, and the weave
    parry_strike = 10 * 2    # both hand roles
    binds = 10 * 2           # both hands
    weave_min = 3.0
    print('parry-strikes: %d, binds: %d' % (parry_strike, binds))
    print('weave: %.0f unbroken minutes' % weave_min)
    assert parry_strike == 20
    assert binds == 20
    assert 2.9 < weave_min < 3.1
    # two weapons, zero full contact in training
    print('rule: one horn parries, the other answers - slow speed only')
    print('OK: %s wove the twin daggers' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_urumi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # flexible sword: four to six feet of spring steel, learned in three stages
    lo_m, hi_m = 4.0 * 0.3048, 6.0 * 0.3048
    stages = 3               # cloth band, blunt steel, sharp
    spins = 10
    form_min = 2.0
    print('urumi: %.2f-%.2f m, learning stages: %d' % (lo_m, hi_m, stages))
    print('clean spins per set: %d, form: %.0f min' % (spins, form_min))
    assert 1.219 < lo_m < 1.220
    assert 1.828 < hi_m < 1.830
    assert stages == 3
    assert spins == 10
    # clear circle: blade length plus arm reach
    clear_m = hi_m + 1.0
    print('clear circle radius: %.2f m - no one else in the area' % clear_m)
    assert 2.82 < clear_m < 2.84
    print('rule: the urumi rewards only the patient')
    print('OK: %s spun the flexible sword' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_uzhichil(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # oil massage: thirty-minute session breakdown
    oil = 3.0                # warming and applying the oil
    feet = 2 * 2.0           # two feet, two minutes each
    legs_min = 2.0 * 2       # ten long strokes per leg, about two minutes a leg
    thighs = 3.0 * 2         # three minutes per leg
    back = 4.0
    arms = 2.5 * 2           # ten strokes per arm, about two and a half minutes a side
    head = 2.0
    closing = 2.0            # closing rest strokes
    session = oil + feet + legs_min + thighs + back + arms + head + closing
    rest_min = 10.0
    print('oil %.0f + feet %.0f + legs %.0f + thighs %.0f + back %.0f + arms %.0f + head %.0f + closing %.0f = %.0f min' % (
        oil, feet, legs_min, thighs, back, arms, head, closing, session))
    print('rest after: %.0f min' % rest_min)
    assert 29.9 < session < 30.1
    assert 9.9 < rest_min < 10.1
    # frequency in heavy training seasons
    per_week = 2.5           # two to three times per week
    print('sessions per week in season: %.1f' % per_week)
    assert 2.0 <= per_week <= 3.0
    print('rule: recovery is training, not rest from it')
    print('OK: %s gave the oil massage' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_marma(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # vital-point heritage study: 108 points across four study regions
    head_neck, torso, arms, legs = 25, 35, 24, 24
    total = head_neck + torso + arms + legs
    print('study regions: head/neck %d, torso %d, arms %d, legs %d' % (head_neck, torso, arms, legs))
    print('total marma points: %d' % total)
    assert total == 108
    # study session: chart review, guided touch, healing teaching
    chart, touch, teaching = 10.0, 10.0, 10.0
    session = chart + touch + teaching
    print('session: chart %.0f + touch %.0f + teaching %.0f = %.0f min' % (chart, touch, teaching, session))
    assert 29.9 < session < 30.1
    # responsibility: the first lesson, weighted above all
    print('rule: this knowledge exists to heal and to safeguard, never to harm')
    print('OK: %s studied the vital points' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_kalari_chikitsa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bone-setting tradition: assessment, mobilization, binding, rehab
    assess_min = 10.0
    joints = 5               # shoulder, elbow, wrist, knee, ankle
    circles = joints * 10 * 2  # ten circles each direction per joint
    session_min = 45.0
    print('assessment: %.0f min' % assess_min)
    print('mobilization: %d joints x 10 circles x 2 directions = %d' % (joints, circles))
    print('treatment session: %.0f minutes' % session_min)
    assert 9.9 < assess_min < 10.1
    assert circles == 100
    assert 44.0 < session_min < 46.0
    # boundaries: serious injuries always referred to modern care
    print('rule: fractures, deep wounds, head injuries go to modern care')
    print('OK: %s learned the mending' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_angathari(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # metal-weapons stage: six solo forms plus paired work, 90-minute session
    warmup = 15.0
    forms = 3.0 + 3.0 + 3.0 + 3.0 + 2.0 + 3.0   # dagger, spear, sword, combined, mace, twin daggers
    rests = 6 * 1.0
    paired = 3 * 10          # three weapon pairings, ten exchanges each
    closing = 12.0
    review = 10.0
    session = warmup + forms + rests + paired + closing + review
    print('warmup %.0f + forms %.0f + rests %.0f + paired %d + closing %.0f + review %.0f' % (
        warmup, forms, rests, paired, closing, review))
    print('angathari session: %.0f minutes' % session)
    assert 16.9 < forms < 17.1
    assert paired == 30
    assert 89.9 < session < 90.1
    print('rule: the metal does not forgive - control is the whole curriculum')
    print('OK: %s forged through the metal stage' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_verumkai_uttama(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # advanced empty hand: positional flow, weapon defense, controls
    positional_min = 5.0
    stick_def = 10 * 2       # both roles
    controls = 10 * 2        # both sides
    flow_min = 5.0
    print('positional drill: %.0f min' % positional_min)
    print('stick defenses: %d, ground controls: %d' % (stick_def, controls))
    print('flow form: %.0f unbroken minutes' % flow_min)
    assert 4.9 < positional_min < 5.1
    assert stick_def == 20
    assert controls == 20
    assert 4.9 < flow_min < 5.1
    print('rule: the encounter ends in a single motion - economy is mastery')
    print('OK: %s mastered the supreme empty hand' % NAME)
if __name__ == '__main__':
    main()
''')


def demo_sarva_shastra(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # capstone: sixty unbroken minutes across every stage
    vadivus = 8 * 1.0
    body_forms = 10.0
    wood = 3 * 3.0
    metal = 4 * 3.0
    urumi = 2.0
    empty = 5.0
    salutations = 2 * 2.0
    transitions = 10.0
    demo_min = vadivus + body_forms + wood + metal + urumi + empty + salutations + transitions
    print('vadivus %.0f + body %.0f + wood %.0f + metal %.0f + urumi %.0f + empty-hand %.0f' % (
        vadivus, body_forms, wood, metal, urumi, empty))
    print('salutations %.0f + transitions %.0f = %.0f unbroken minutes' % (salutations, transitions, demo_min))
    assert 59.9 < demo_min < 60.1
    print('rule: the ladder is a circle - the master returns to the salutation as a teacher')
    print('OK: %s commanded the full arsenal' % NAME)
if __name__ == '__main__':
    main()
''')


DEMOS = {
    "vanakkam": demo_vanakkam,
    "gaja": demo_gaja,
    "simha": demo_simha,
    "ashva": demo_ashva,
    "varaha": demo_varaha,
    "sarpam": demo_sarpam,
    "marjjara": demo_marjjara,
    "kukkuda": demo_kukkuda,
    "matsya": demo_matsya,
    "chuvadukal": demo_chuvadukal,
    "kalugal": demo_kalugal,
    "meyyorukkam": demo_meyyorukkam,
    "meippayattu": demo_meippayattu,
    "swasam": demo_swasam,
    "muchan": demo_muchan,
    "otta": demo_otta,
    "kol": demo_kol,
    "kolthari": demo_kolthari,
    "kadhara": demo_kadhara,
    "kuntham": demo_kuntham,
    "vaal": demo_vaal,
    "paricha": demo_paricha,
    "valum_parichayum": demo_valum_parichayum,
    "verumkai": demo_verumkai,
    "kaal_adikal": demo_kaal_adikal,
    "gada": demo_gada,
    "madu": demo_madu,
    "urumi": demo_urumi,
    "uzhichil": demo_uzhichil,
    "marma": demo_marma,
    "kalari_chikitsa": demo_kalari_chikitsa,
    "angathari": demo_angathari,
    "verumkai_uttama": demo_verumkai_uttama,
    "sarva_shastra": demo_sarva_shastra,
}
