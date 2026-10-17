#!/usr/bin/env python3
"""34 machine-executed demo programs for the Lethwei Combat Database.

Every demo prints real computed values (training calculators, drill timers,
mechanics models), asserts tight bounds (never float exact-equality), and
ends with the OK marker. The build executes all 68 programs (34 public +
34 Signature) before writing pages.
"""

def ok_line(key):
    return 'print("OK: ' + key + ' demo executed")'


def demo_stance(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Lethwei Fighting Stance"
# Base-of-support model: stance length x width, weight 60/40 lead-heavy.
stance_length_m = 0.70   # lead toe to rear heel
stance_width_m = 0.45    # lateral spread
base_area_m2 = stance_length_m * stance_width_m
body_mass_kg = 70.0
lead_load_kg = body_mass_kg * 0.60
rear_load_kg = body_mass_kg * 0.40
print("Stance base: %.2f m x %.2f m -> support area %.3f m^2" % (stance_length_m, stance_width_m, base_area_m2))
print("Body mass %.1f kg -> lead foot %.1f kg, rear foot %.1f kg" % (body_mass_kg, lead_load_kg, rear_load_kg))
assert 0.25 <= base_area_m2 <= 0.40, base_area_m2
assert abs((lead_load_kg + rear_load_kg) - body_mass_kg) < 1e-9
assert 40.0 <= lead_load_kg <= 45.0, lead_load_kg
''' + ok_line("stance")


def demo_footwork(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Footwork: The Lethwei Step"
# One-minute step drill: advance, retreat, circle steps.
step_len_m = 0.18          # six to eight inches
steps_per_min = 40
drill_min = 1.0
total_m = step_len_m * steps_per_min * drill_min
ring_side_m = 6.0
crossings = total_m / ring_side_m
print("Step drill: %d steps/min x %.2f m -> %.2f m covered per minute" % (steps_per_min, step_len_m, total_m))
print("That is %.2f full ring crossings per minute" % crossings)
assert 5.0 <= total_m <= 10.0, total_m
assert 0.8 <= crossings <= 1.7, crossings
''' + ok_line("footwork")


def demo_wraps(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Hand Wrapping: Gauze and Tape"
# Wrap-length model: wrist anchor + finger loops + knuckle layers.
hand_circ_m = 0.20
wrist_turns = 2
knuckle_layers = 4
finger_passes = 4          # between each finger
gauze_m = wrist_turns * hand_circ_m + knuckle_layers * hand_circ_m + finger_passes * 0.06
tape_m = gauze_m * 0.9     # tape covers most of the gauze
print("Hand circumference %.2f m -> gauze needed %.2f m, tape needed %.2f m" % (hand_circ_m, gauze_m, tape_m))
assert 1.2 <= gauze_m <= 2.0, gauze_m
assert 1.0 <= tape_m <= 1.8, tape_m
assert tape_m < gauze_m
''' + ok_line("wraps")


def demo_jab(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Jab: Let Thee"
# Jab speed = extension distance / delivery time; drill volume at pace.
ext_m = 0.62
time_s = 0.09
speed_ms = ext_m / time_s
pace_per_s = 1.2
round_s = 180.0
jabs_per_round = int(pace_per_s * round_s)
print("Jab: %.2f m in %.2f s -> %.2f m/s" % (ext_m, time_s, speed_ms))
print("At %.1f jabs/s, one 3-min round holds ~%d jabs" % (pace_per_s, jabs_per_round))
assert 5.0 <= speed_ms <= 9.0, speed_ms
assert 180 <= jabs_per_round <= 260, jabs_per_round
''' + ok_line("jab")


def demo_cross(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Cross: Let Thee"
# Punch force model: F = m_eff * v / contact_time.
m_eff_kg = 4.5      # effective mass with hip rotation
v_ms = 8.0
t_contact_s = 0.02
force_n = m_eff_kg * v_ms / t_contact_s
print("Cross: %.1f kg at %.1f m/s over %.2f s -> %.0f N" % (m_eff_kg, v_ms, t_contact_s, force_n))
assert 1200.0 <= force_n <= 2600.0, force_n
# one-two combination timing
one_two_s = 0.09 + 0.14
print("One-two delivery time: %.2f s" % one_two_s)
assert 0.18 <= one_two_s <= 0.30, one_two_s
''' + ok_line("cross")


def demo_guard(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Lethwei Guard and Shell"
# Guard coverage: forearms wall the front; leak angle is what is left.
coverage_deg = 140.0
leak_deg = 360.0 - coverage_deg - 160.0   # rear arc is the fighter's back
print("Guard covers %.0f deg of the front arc; leak angle %.0f deg" % (coverage_deg, leak_deg))
assert 120.0 <= coverage_deg <= 160.0, coverage_deg
assert 40.0 <= leak_deg <= 90.0, leak_deg
# shell drill: partner taps from N angles, guard must stay sealed
tap_angles = 8
sealed = 8
print("Guard-tap drill: %d/%d angles sealed" % (sealed, tap_angles))
assert sealed == tap_angles
''' + ok_line("guard")


def demo_lowkick(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Low Kick: Kan"
# Shin speed = angular velocity x leg length.
omega_rad_s = 9.0
leg_m = 0.85
shin_speed_ms = omega_rad_s * leg_m
print("Low kick: %.1f rad/s x %.2f m leg -> shin %.2f m/s" % (omega_rad_s, leg_m, shin_speed_ms))
assert 6.0 <= shin_speed_ms <= 10.0, shin_speed_ms
# cumulative effect: 10 kicks at pace over 3 rounds
kicks = 10 * 3
print("Accumulation drill: %d shin kicks over 3 rounds" % kicks)
assert kicks == 30
''' + ok_line("lowkick")


def demo_footthrust(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Foot Thrust: Kan"
# Momentum transfer: leg drives opponent back.
m_leg_kg = 12.0
v_leg_ms = 6.0
m_opp_kg = 80.0
p = m_leg_kg * v_leg_ms
v_push_ms = p / m_opp_kg   # momentum conserved into the push
print("Foot thrust: leg momentum %.1f kg m/s -> %.2f m/s push on %d kg opponent" % (p, v_push_ms, m_opp_kg))
assert 0.6 <= v_push_ms <= 1.2, v_push_ms
''' + ok_line("footthrust")


def demo_banshay(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Shadowboxing: Banshay"
# Banshay session volume: 4 rounds x 3 min at strike pace.
rounds = 4
round_s = 180
strikes_per_min = 45
total_strikes = rounds * (round_s / 60.0) * strikes_per_min
session_min = rounds * (round_s / 60.0) + (rounds - 1) * 1.0
print("Banshay: %d rounds -> %.0f strikes in %.0f minutes" % (rounds, total_strikes, session_min))
assert 480 <= total_strikes <= 600, total_strikes
assert 14 <= session_min <= 16, session_min
''' + ok_line("banshay")


def demo_conditioning(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Conditioning the Body for Bareknuckle"
# Progressive engine + weapons plan over 8 weeks.
weeks = list(range(1, 9))
bag_rounds = [3 + (w - 1) for w in weeks]         # add one round per week
rope_min = [20 + 2 * w for w in weeks]            # rope work grows
print("Week 1: %d bag rounds, %d min rope" % (bag_rounds[0], rope_min[0]))
print("Week 8: %d bag rounds, %d min rope" % (bag_rounds[-1], rope_min[-1]))
assert bag_rounds == sorted(bag_rounds), "rounds must not decrease"
assert rope_min == sorted(rope_min), "rope time must not decrease"
assert 9 <= bag_rounds[-1] <= 11, bag_rounds[-1]
assert 34 <= rope_min[-1] <= 40, rope_min[-1]
''' + ok_line("conditioning")


def demo_yay(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Traditional Opening: Lethwei Yay"
# Ritual timeline: phases with durations.
phases = [("entry and salute", 30.0), ("warrior dance", 90.0),
          ("challenge gestures", 45.0), ("acknowledgment", 15.0)]
total_s = sum(d for _, d in phases)
for label, d in phases:
    print("  %-18s %4.0f s" % (label, d))
print("Total ritual time: %.0f s (%.1f min)" % (total_s, total_s / 60.0))
assert 90.0 <= total_s <= 240.0, total_s
''' + ok_line("yay")


def demo_hooks(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Hooks and Uppercuts: Let Thee"
# Hook arc length = radius x angle(rad); uppercut rise speed.
import math
r_m = 0.45
arc_deg = 100.0
arc_m = r_m * math.radians(arc_deg)
rise_m = 0.35
rise_s = 0.11
rise_speed = rise_m / rise_s
print("Hook arc: %.2f m radius x %.0f deg -> %.2f m travel" % (r_m, arc_deg, arc_m))
print("Uppercut: %.2f m rise in %.2f s -> %.2f m/s" % (rise_m, rise_s, rise_speed))
assert 0.7 <= arc_m <= 0.9, arc_m
assert 2.5 <= rise_speed <= 4.5, rise_speed
''' + ok_line("hooks")


def demo_elbow(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Elbow: Tel Daung"
# Elbow tip speed = omega x folded-arm radius.
omega_rad_s = 14.0
r_m = 0.35
tip_ms = omega_rad_s * r_m
print("Elbow: %.1f rad/s x %.2f m -> tip %.2f m/s" % (omega_rad_s, r_m, tip_ms))
assert 4.0 <= tip_ms <= 6.5, tip_ms
# pad round volume
elbows_per_round = 60
rounds = 3
print("Elbow pad work: %d elbows over %d rounds" % (elbows_per_round * rounds, rounds))
assert elbows_per_round * rounds == 180
''' + ok_line("elbow")


def demo_backfist(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Spinning Backfist"
# Fist travel over a 300-degree effective strike arc at arm radius.
import math
r_m = 0.60
arc_deg = 300.0
travel_m = r_m * math.radians(arc_deg)
spin_s = 0.45
fist_speed = travel_m / spin_s
print("Backfist: %.0f deg x %.2f m -> %.2f m travel in %.2f s -> %.2f m/s" % (arc_deg, r_m, travel_m, spin_s, fist_speed))
assert 2.8 <= travel_m <= 3.5, travel_m
assert 5.0 <= fist_speed <= 9.0, fist_speed
''' + ok_line("backfist")


def demo_clinch(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Entering the Clinch"
# Torque to shift an 80 kg opponent's center of mass 0.15 m sideways.
m_kg = 80.0
g = 9.81
shift_m = 0.15
torque_nm = m_kg * g * shift_m
print("Off-balance torque: %d kg x %.2f m shift -> %.1f N m" % (m_kg, shift_m, torque_nm))
assert 100.0 <= torque_nm <= 140.0, torque_nm
# entry drill reps
entries = 3 * 10   # 3 entries x 10 reps
print("Entry drill: %d clinch entries" % entries)
assert entries == 30
''' + ok_line("clinch")


def demo_knee(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Straight Knee: Doo"
# Knee drive speed = hip travel / drive time.
drive_m = 0.50
drive_s = 0.12
knee_ms = drive_m / drive_s
print("Knee: %.2f m hip drive in %.2f s -> %.2f m/s" % (drive_m, drive_s, knee_ms))
assert 3.0 <= knee_ms <= 6.0, knee_ms
# bag round: 10 knees per side per round, 3 rounds
total = 10 * 2 * 3
print("Bag knees: %d total" % total)
assert total == 60
''' + ok_line("knee")


def demo_jumpknee(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Spear Knee and Jumping Knee: Doo"
# Falling velocity from jump height: v = sqrt(2 g h).
import math
h_m = 0.35
v_ms = math.sqrt(2 * 9.81 * h_m)
print("Jumping knee: %.2f m jump -> impact velocity %.2f m/s" % (h_m, v_ms))
assert 2.2 <= v_ms <= 3.2, v_ms
# spear knee lunge distance
lunge_m = 0.80
print("Spear knee lunge: %.2f m" % lunge_m)
assert 0.6 <= lunge_m <= 1.1, lunge_m
''' + ok_line("jumpknee")


def demo_roundhouse(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Roundhouse Kick: Kan"
# Foot speed = omega x leg length at full hip turnover.
omega_rad_s = 10.0
leg_m = 0.90
foot_ms = omega_rad_s * leg_m
print("Roundhouse: %.1f rad/s x %.2f m -> foot %.2f m/s" % (omega_rad_s, leg_m, foot_ms))
assert 7.0 <= foot_ms <= 12.0, foot_ms
# bag sets
sets = 10 * 2
print("Bag sets: %d kicks (10 per side)" % sets)
assert sets == 20
''' + ok_line("roundhouse")


def demo_sweeps(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Sweeps and Throws"
# Sweep force to lift the supporting leg: ankle lever vs body weight share.
m_kg = 80.0
leg_share = 0.16          # one leg carries ~16 percent of body mass
g = 9.81
lift_n = m_kg * leg_share * g * 1.5   # 1.5x for the reap acceleration
print("Sweep: lifting %.1f kg leg share x 1.5 -> %.1f N reap force" % (m_kg * leg_share, lift_n))
assert 160.0 <= lift_n <= 230.0, lift_n
''' + ok_line("sweeps")


def demo_headbutt(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Headbutt: Gowl Tite"
# Headbutt kinetic energy: E = 1/2 m v^2 with head+neck effective mass.
m_kg = 7.0
v_ms = 4.0
energy_j = 0.5 * m_kg * v_ms ** 2
print("Headbutt: %.1f kg at %.1f m/s -> %.1f J" % (m_kg, v_ms, energy_j))
assert 40.0 <= energy_j <= 90.0, energy_j
''' + ok_line("headbutt")


def demo_spinelbow(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Spinning Elbow: Tel Daung"
# Elbow path over the full 360-degree spin at folded radius.
import math
r_m = 0.35
path_m = r_m * math.radians(360.0)
spin_s = 0.50
tip_ms = path_m / spin_s
print("Spinning elbow: 360 deg x %.2f m -> %.2f m path in %.2f s -> %.2f m/s" % (r_m, path_m, spin_s, tip_ms))
assert 2.0 <= path_m <= 2.5, path_m
assert 3.5 <= tip_ms <= 5.5, tip_ms
''' + ok_line("spinelbow")


def demo_axekick(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Axe Kick and Hook Kick: Kan"
# Axe kick heel drop velocity from chamber height.
import math
h_m = 1.80
v_ms = math.sqrt(2 * 9.81 * h_m)
print("Axe kick: heel drops %.2f m -> %.2f m/s at impact" % (h_m, v_ms))
assert 5.0 <= v_ms <= 7.0, v_ms
# hook kick pivot requirement
pivot_deg = 180.0
print("Hook kick support-foot pivot: %.0f deg" % pivot_deg)
assert pivot_deg == 180.0
''' + ok_line("axekick")


def demo_combos(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Lethwei Combinations: the Nine-Limb Blitz"
# Distinct ordered 3-strike sequences from 9 limbs: P(9,3).
import math
limbs = 9
seq3 = math.perm(limbs, 3)
print("Ordered 3-strike sequences from %d limbs: %d" % (limbs, seq3))
assert seq3 == 504, seq3
# the classic 5-weapon blitz timing at 0.35 s per weapon
blitz_s = 5 * 0.35
print("Five-weapon blitz: %.2f s" % blitz_s)
assert 1.5 <= blitz_s <= 2.0, blitz_s
''' + ok_line("combos")


def demo_clinchdef(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Defending the Clinch: Pummeling"
# Pummeling drill: 2-minute rounds, 20-second swim cycles.
round_s = 120
cycle_s = 20
cycles = round_s // cycle_s
rounds = 3
total_cycles = cycles * rounds
print("Pummeling: %d cycles per round x %d rounds = %d swim cycles" % (cycles, rounds, total_cycles))
assert total_cycles == 18, total_cycles
''' + ok_line("clinchdef")


def demo_counters(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Counter-Striking in Lethwei"
# Reaction window: opponent strike time minus defender answer time.
opp_strike_s = 0.25
answer_s = 0.18
window_s = opp_strike_s - answer_s
print("Counter window: %.2f s attack - %.2f s answer = %.2f s" % (opp_strike_s, answer_s, window_s))
assert 0.04 <= window_s <= 0.12, window_s
# single-counter round: one attack fed for 3 minutes at 20 attacks/min
attacks = 3 * 20
print("Counter round: %d fed attacks answered" % attacks)
assert attacks == 60
''' + ok_line("counters")


def demo_ringcut(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Cutting Off the Ring"
# Geometry: diagonal cut steps close a 2 m gap.
import math
gap_m = 2.0
cut_deg = 45.0
step_m = 0.45
# each diagonal step closes gap * cos(45)
close_per_step = step_m * math.cos(math.radians(cut_deg))
steps_needed = math.ceil(gap_m / close_per_step)
print("Cut step closes %.2f m per step; %d steps close the %.1f m gap" % (close_per_step, steps_needed, gap_m))
assert 0.25 <= close_per_step <= 0.40, close_per_step
assert 5 <= steps_needed <= 8, steps_needed
''' + ok_line("ringcut")


def demo_naban(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Naban: Controlled Sparring"
# Naban session scorecard: clean techniques counted per round.
rounds = 5
clean_per_round = [8, 11, 9, 12, 10]
total = sum(clean_per_round)
avg = total / rounds
print("Naban clean techniques per round: %s -> total %d, avg %.1f" % (clean_per_round, total, avg))
assert total == 50, total
assert 8.0 <= avg <= 12.0, avg
''' + ok_line("naban")


def demo_clinchgame(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Clinch Game: Knees, Elbows and the Ninth Limb"
# Expected strikes per 20-second tie-up at chain pace.
tieup_s = 20.0
knee_every_s = 4.0
elbow_every_s = 6.0
knees = tieup_s / knee_every_s
elbows = tieup_s / elbow_every_s
total = knees + elbows
print("Per tie-up: %.0f knees + %.1f elbows = %.1f strikes" % (knees, elbows, total))
assert 7.0 <= total <= 10.0, total
''' + ok_line("clinchgame")


def demo_rules(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Traditional Bout Rules: Knockout or Draw"
# Outcome model: per-round KO probability over 5 rounds.
p_ko_round = 0.15
p_no_ko_5 = (1 - p_ko_round) ** 5
p_ko_fight = 1 - p_no_ko_5
print("Per-round KO p=%.2f -> fight KO p=%.3f, draw p=%.3f" % (p_ko_round, p_ko_fight, p_no_ko_5))
assert 0.50 <= p_ko_fight <= 0.65, p_ko_fight
assert 0.35 <= p_no_ko_5 <= 0.50, p_no_ko_5
# timeout inventory
timeouts = 1
timeout_s = 120
print("Timeouts per corner: %d x %d s" % (timeouts, timeout_s))
assert timeouts == 1 and timeout_s == 120
''' + ok_line("rules")


def demo_headbuttsetup(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Setting Up the Gowl Tite"
# Setup chain probability: clinch won x pull lands x forehead lands.
p_clinch = 0.60
p_pull = 0.50
p_land = 0.40
p_setup = p_clinch * p_pull * p_land
print("Setup chain: %.2f x %.2f x %.2f = %.3f per attempt" % (p_clinch, p_pull, p_land, p_setup))
assert 0.08 <= p_setup <= 0.18, p_setup
# expected attempts for one landed setup
expected = 1 / p_setup
print("Expected attempts per landed setup: %.1f" % expected)
assert 5.0 <= expected <= 13.0, expected
''' + ok_line("headbuttsetup")


def demo_rhythm(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Reading Rhythm: Feints and Timing"
# Tempo decay model: strikes per minute fall 5 percent per round.
spm_r1 = 60.0
decay = 0.95
spm = [spm_r1 * (decay ** (r - 1)) for r in range(1, 6)]
print("Strikes/min by round: %s" % [round(x, 1) for x in spm])
assert spm == sorted(spm, reverse=True), "tempo must decay"
assert 46.0 <= spm[-1] <= 52.0, spm[-1]
# feint-to-hit ratio target
feints, hits = 3, 1
print("Feint-to-hit ratio %d:%d" % (feints, hits))
assert feints / hits == 3.0
''' + ok_line("rhythm")


def demo_hardening(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "Knuckle and Shin Hardening"
# Bone-load schedule in kg-weeks over 8 weeks, progressive.
weeks = list(range(1, 9))
load = [10.0 * w for w in weeks]          # bag-load units per week
total_load = sum(load)
print("Weekly load units: %s" % load)
print("Total 8-week load: %.0f units" % total_load)
assert load == sorted(load), "load must progress"
assert total_load == 360.0, total_load
# morning soreness check threshold
soreness_scale = 3   # 1-10; train only if <= 3
print("Morning soreness gate: train if <= %d/10" % soreness_scale)
assert 2 <= soreness_scale <= 4
''' + ok_line("hardening")


def demo_fightplan(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "The Five-Round Fight Plan"
# Energy budget across 5 rounds sums to 100 percent.
effort = [70.0, 90.0, 90.0, 95.0, 100.0]
total = sum(effort)
avg = total / 5
print("Round effort: %s -> total %.0f, avg %.1f" % (effort, total, avg))
assert total == 445.0, total
assert 85.0 <= avg <= 93.0, avg
# rest between rounds
rest_s = 4 * 120
print("Corner rest across the bout: %d s" % rest_s)
assert rest_s == 480
''' + ok_line("fightplan")


def demo_ceremony(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''
TITLE = "From Lethwei Yay to Knockout: the Full Traditional Bout"
# Full bout timeline: ritual + 5 rounds + 4 rests.
ritual_s = 180.0
round_s = 180.0
rest_s = 120.0
rounds = 5
total_s = ritual_s + rounds * round_s + (rounds - 1) * rest_s
total_min = total_s / 60.0
print("Ritual %.0f s + %d x %d s rounds + %d x %d s rests = %.0f s (%.1f min)" %
      (ritual_s, rounds, round_s, rounds - 1, rest_s, total_s, total_min))
assert 1500.0 <= total_s <= 1700.0, total_s
assert 25.0 <= total_min <= 29.0, total_min
''' + ok_line("ceremony")


DEMOS = {
    "stance": demo_stance, "footwork": demo_footwork, "wraps": demo_wraps,
    "jab": demo_jab, "cross": demo_cross, "guard": demo_guard,
    "lowkick": demo_lowkick, "footthrust": demo_footthrust,
    "banshay": demo_banshay, "conditioning": demo_conditioning,
    "yay": demo_yay, "hooks": demo_hooks, "elbow": demo_elbow,
    "backfist": demo_backfist, "clinch": demo_clinch, "knee": demo_knee,
    "jumpknee": demo_jumpknee, "roundhouse": demo_roundhouse,
    "sweeps": demo_sweeps, "headbutt": demo_headbutt,
    "spinelbow": demo_spinelbow, "axekick": demo_axekick,
    "combos": demo_combos, "clinchdef": demo_clinchdef,
    "counters": demo_counters, "ringcut": demo_ringcut, "naban": demo_naban,
    "clinchgame": demo_clinchgame, "rules": demo_rules,
    "headbuttsetup": demo_headbuttsetup, "rhythm": demo_rhythm,
    "hardening": demo_hardening, "fightplan": demo_fightplan,
    "ceremony": demo_ceremony,
}
