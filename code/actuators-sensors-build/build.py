#!/usr/bin/env python3
"""Build the Actuators and Sensors field databases for JAH Databases (field #29, taxonomy order).

Verified 2026-10-17 (see entries_actuators_sensors.py docstring): NO database
covers the general actuators-and-sensors discipline. Manifest search (2358
databases): nearest neighbors are 'cyber-sensor' (268 records of network
security sensors - IDS, honeypots, EDR - NOT physical transducers),
'phone-sensor-fusion' (15 phone-only records), 'electrical-electronic-testing'
(24 test records), 'robotics-autonomous-physical-systems' (32 macro robot
records), 'mechatronics-engineers' (people records), and 'microrobotics'
(32 micro-scale records - explicitly micro-scale only). Whole-system title
sweep over all 760 shard indexes (1,129,453 records): actuator/sensor
discipline terms hit only shallow study-corpus items and incidental uses.
ZERO full-record discipline coverage anywhere.

So this build creates two NEW databases, 32 ladder-ordered records each,
covering ONLY what the system left uncovered (macro/general scale;
micro-scale belongs to field #28):

  actuators-sensors             - The Actuators and Sensors Database
                                  (public-harvest: real, fact-checked
                                  actuator and sensor engineering)
  actuators-sensors-signature   - The Actuators and Sensors Signature Database
                                  (his original Signature interpretation;
                                  src signature, titles suffixed
                                  " (Signature Edition)", never presented as
                                  authentic public record)

32 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Actuator/sensor demos: motor
power chain; energy-family force comparison; DC motor model (stall, no-load,
loaded efficiency); torque-speed sizing; BLDC KV/kt and commutation; stepper
resolution and step rate; thermistor-to-ADC chain; measurement statistics;
PD servo step response; gearbox + ballscrew thrust; solenoid force and L/R;
voice-coil force and excursion; hydraulic cylinder push/pull/speed/power;
pneumatic force, air use, speed; piezo stack displacement and blocked force;
SMA wire force, stroke, heat time; Terfenol-D stretch and blocked force;
encoder counts and velocity; strain bridge and load-cell weight; 4-20 mA
pressure loop and water column; Pt100 Callendar-Van Dusen and thermocouple
EMF; ultrasonic time-of-flight and capacitive proximity; camera field of
view and stereo depth; IMU integration, drift, and tilt; LIDAR timing and
radar Doppler; tactile taxel capacitance and FSR curve; instrumentation-amp
gain and anti-alias corner; ADC LSB, quantization noise, ENOB; I2C/SPI/CAN
throughput; 1-D Kalman convergence and complementary filter; inertia sizing
(peak/RMS torque, safety factor); MTBF reliability and availability.

Subtitle disambiguation (fields #13-28 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "DC Motors: The
Spinning Workhorse of Machines".

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
# Whole-system dedupe gate against the FRESH data/dedupe/exact/ index in the
# main repo (per task). Fields past the gate index were cross-checked
# directly (see docstring) - subtitle disambiguation used throughout.
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_actuators_sensors import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of actuators "
                "and sensors engineering: clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked actuators and sensors engineering: what "
                "actuators and sensors are; the energy families (electric, hydraulic, pneumatic); "
                "DC, brushless, and stepper motors; torque, speed, and power; servos and drives; "
                "gearboxes, leadscrews, and ballscrews; solenoids; voice coils and linear motors; "
                "hydraulic and pneumatic actuators; piezoelectric, shape-memory-alloy, and "
                "magnetostrictive actuators; position encoders and resolvers; force, torque, and "
                "strain sensing; pressure, temperature, proximity, vision, IMU, LIDAR/radar, and "
                "tactile sensors; signal conditioning; ADCs and DACs; I2C, SPI, and CAN buses; "
                "sensor fusion; sizing and selection; failure, safety, and maintenance, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what actuators and "
              "sensors are, the energy families, DC motors, torque/speed/power, what sensors do, "
              "brushless and stepper motors, measurement truth) -> Compounded (servos, "
              "transmissions, solenoids, voice coils and linear motors, hydraulics, pneumatics, "
              "piezoelectric, shape-memory-alloy, and magnetostrictive actuators, encoders, force, "
              "pressure, temperature, proximity, vision, IMU, LIDAR/radar, and tactile sensors) -> "
              "Advanced (signal conditioning, ADCs/DACs, interfacing buses, sensor fusion, sizing "
              "and selection, failure/safety/maintenance).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search servo, encoder, piezoelectric, Kalman, hydraulics, thermocouple, LIDAR...",
        "chat_ph": "Ask about actuators and sensors...",
        "archive_blurb": ("Seeded %s actuators-and-sensors records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled actuators-and-sensors studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about actuators and sensors - from DC, brushless, and stepper motors through torque and power, servos, transmissions, solenoids, voice coils, hydraulic, pneumatic, piezoelectric, shape-memory, and magnetostrictive actuators, encoders, force, pressure, temperature, proximity, vision, IMU, LIDAR, and tactile sensors, signal conditioning, ADCs/DACs, I2C/SPI/CAN, sensor fusion, sizing, and reliability." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "actuators-sensors-study", "gen_demo_kind": "actuators-sensors-demo",
        "source": source,
    }

CIT_PUB = ("Actuators and sensors (standard texts: Bolton 'Mechatronics' 7th ed. 2019; "
           "Fraden 'Handbook of Modern Sensors' 5th ed. 2016; Dunn 'Introduction to "
           "Instrumentation, Sensors, and Process Control' 2006; Nyce 'Linear Position "
           "Sensors' 2004; Johnson 'Process Control Instrumentation Technology' 8th ed. "
           "2006; IEEE Std 176-1987 on piezoelectricity; Bishop (ed.) 'The Mechatronics "
           "Handbook' 2002; Welch & Bishop 'An Introduction to the Kalman Filter' 2006; "
           "Bosch 'CAN Specification 2.0' 1991; NXP 'I2C-bus specification' UM10204; "
           "Lagoudas (ed.) 'Shape Memory Alloys' 2008; Janocha (ed.) 'Adaptronics and "
           "Smart Structures' 1999; Hendershot & Miller 'Design of Brushless "
           "Permanent-Magnet Machines' 2010; Esposito 'Fluid Power with Applications' 7th "
           "ed. 2009; Ogata 'Modern Control Engineering' 5th ed. 2010; Titterton & Weston "
           "'Strapdown Inertial Navigation Technology' 2nd ed. 2004; Szeliski 'Computer "
           "Vision' 2010; Shan & Toth 'Topographic Laser Ranging and Scanning' 2008; "
           "Burns et al. NIST Monograph 175 (ITS-90 thermocouples) 1993; Clark "
           "'Magnetostrictive rare earth-Fe2 compounds' 1980; Kester (ed.) 'Data Conversion "
           "Handbook' 2005; O'Connor & Kleyner 'Practical Reliability Engineering' 5th ed. "
           "2012; Dahiya et al. 'Directions Toward Effective Utilization of Tactile Skin' "
           "2013).")
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["actuators-sensors"] = _cfg(
    "actuators-sensors", "The Actuators and Sensors Database",
    "Real, fact-checked actuator and sensor engineering: from what actuators and sensors are "
    "through the energy families, DC, brushless, and stepper motors, torque/speed/power, servos, "
    "transmissions, solenoids, voice coils, hydraulic, pneumatic, piezoelectric, shape-memory, "
    "and magnetostrictive actuators, encoders, force, pressure, temperature, proximity, vision, "
    "IMU, LIDAR/radar, and tactile sensors to signal conditioning, ADCs/DACs, I2C/SPI/CAN, "
    "sensor fusion, sizing, and reliability - taught progressively along the ladder.",
    "actuators and sensors record", "JAH-ACT-", "JAH Actuators Archivist",
    "actuators and sensors archivist - electric actuators (DC, brushless, stepper, servo), "
    "transmissions, solenoids, voice coils, hydraulic and pneumatic actuators, smart materials "
    "(piezoelectric, shape-memory alloy, magnetostrictive), sensors (position, force, pressure, "
    "temperature, proximity, vision, IMU, LIDAR/radar, tactile), signal conditioning, ADC/DAC, "
    "I2C/SPI/CAN, sensor fusion, sizing and selection, failure and maintenance; teaching "
    "progressively along the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, history, math, how-to - "
    "using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["actuators-sensors-signature"] = _cfg(
    "actuators-sensors-signature", "The Actuators and Sensors Signature Database",
    "His original Signature interpretation of actuators and sensors: the full ladder from what "
    "actuators and sensors are through the energy families, motors, smart materials, every "
    "sensor family, conditioning, conversion, buses, fusion, sizing, and reliability, reframed "
    "as Signature science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "actuators and sensors record", "JAH-ACS-", "JAH Actuators Archivist (Signature)",
    "actuators and sensors archivist - Signature editions: his original Signature "
    "interpretation of actuators and sensors, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, how-to - "
    "using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# actuators-and-sensors computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_as_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the actuator/sensor loop in one motor: electrical power in, shaft power out
    V, I, eta = 12.0, 2.0, 0.75
    P_in = V * I
    P_out = P_in * eta
    rpm = 3000.0
    omega = rpm * 2.0 * math.pi / 60.0
    tau = P_out / omega
    print("electrical in: %.1f W; shaft out: %.1f W (%.0f%% efficient)" % (P_in, P_out, eta * 100))
    print("at %.0f rpm (%.1f rad/s): torque = %.4f N m" % (rpm, omega, tau))
    print("heat lost: %.1f W - the missing power always becomes heat" % (P_in - P_out))
    assert abs(tau - 0.0573) < 5e-4, tau
    assert abs(P_out - 18.0) < 1e-9
    print("sense, decide, act, sense again: the loop every machine runs")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_families(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # one bore, three families: what 50 mm of piston buys in each energy family
    d = 0.050
    A = math.pi * (d / 2.0) ** 2
    F_hyd = 210e5 * A            # 210 bar oil
    F_pneu = 6e5 * A             # 6 bar air
    tau, rpm = 0.5, 3000.0       # electric motor
    P = tau * rpm * 2.0 * math.pi / 60.0
    print("50 mm bore hydraulic at 210 bar: %.1f kN" % (F_hyd / 1000.0))
    print("50 mm bore pneumatic at 6 bar:   %.2f kN" % (F_pneu / 1000.0))
    print("0.5 N m electric motor at 3000 rpm: %.1f W (~%.0f W/kg for a 1 kg motor)" % (P, P / 1.0))
    assert 41000.0 < F_hyd < 41500.0, F_hyd
    assert 1170.0 < F_pneu < 1190.0, F_pneu
    assert abs(P - 157.08) < 0.05, P
    print("rule: pick electric for precision, hydraulic for force density, pneumatic for cheap speed")
    print("OK: %s weighed the families" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_dc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the whole DC motor on two constants: torque from current, speed from voltage
    V, R, kt = 12.0, 1.2, 0.05
    ke = kt                                  # SI units: ke (V s/rad) == kt (N m/A)
    I_stall = V / R
    tau_stall = kt * I_stall
    w_nl = V / ke
    rpm_nl = w_nl * 60.0 / (2.0 * math.pi)
    tau_load, I_load = 0.2, 0.2 / kt
    Vemf = V - I_load * R
    w = Vemf / ke
    rpm = w * 60.0 / (2.0 * math.pi)
    eta = tau_load * w / (V * I_load)
    print("stall: %.1f A -> %.2f N m" % (I_stall, tau_stall))
    print("no-load: %.0f rad/s = %.0f rpm" % (w_nl, rpm_nl))
    print("at 0.2 N m: %.0f rpm, %.0f%% efficient" % (rpm, eta * 100))
    assert abs(I_stall - 10.0) < 1e-9 and abs(tau_stall - 0.5) < 1e-9
    assert abs(w_nl - 240.0) < 1e-9
    assert abs(rpm - 1375.1) < 0.5, rpm
    assert abs(eta - 0.6) < 1e-9, eta
    print("rule: voltage sets speed, current sets torque - read the ammeter, it never lies")
    print("OK: %s spun the workhorse" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_torquespeed(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # sizing arithmetic: match the power, trade torque for speed, budget the losses
    tau_need, rpm_need = 30.0, 60.0
    w_need = rpm_need * 2.0 * math.pi / 60.0
    P_need = tau_need * w_need
    tau_m, rpm_m = 0.3, 6000.0
    P_m = tau_m * rpm_m * 2.0 * math.pi / 60.0
    ratio, eff = 100.0, 0.90
    tau_out = tau_m * ratio * eff
    rpm_out = rpm_m / ratio
    print("load needs: %.1f W (30 N m at 60 rpm)" % P_need)
    print("motor makes: %.1f W (0.3 N m at 6000 rpm) - power matches" % P_m)
    print("through 100:1 at 90%%: %.1f N m at %.0f rpm" % (tau_out, rpm_out))
    print("shortfall: %.1f N m lost to the gearbox - accept it, or oversize honestly" % (tau_need - tau_out))
    assert abs(P_need - 188.50) < 0.05, P_need
    assert abs(P_m - P_need) < 0.01
    assert abs(tau_out - 27.0) < 0.01, tau_out
    print("rule: power is the budget; torque and speed are how you spend it")
    print("OK: %s traded torque for speed" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_bldc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # KV one way, kt the other; pole pairs set the commutation pace
    KV, Vbus = 1000.0, 12.0          # rpm per volt
    rpm_nl = KV * Vbus
    kt = 60.0 / (2.0 * math.pi * KV)  # N m/A
    pole_pairs = 4
    steps_per_rev = 6 * pole_pairs
    rpm_run = 6000.0
    comm_hz = rpm_run / 60.0 * steps_per_rev
    elec_hz = rpm_run / 60.0 * pole_pairs
    print("1000 KV on 12 V: %.0f rpm no-load; kt = %.5f N m/A" % (rpm_nl, kt))
    print("%d commutations per mechanical rev" % steps_per_rev)
    print("at 6000 rpm: %.0f commutations/s, %.0f Hz electrical" % (comm_hz, elec_hz))
    assert rpm_nl == 12000.0
    assert abs(kt - 0.00955) < 1e-5, kt
    assert steps_per_rev == 24 and comm_hz == 2400.0 and elec_hz == 400.0
    print("rule: the controller replaces the brushes - without it the motor is a paperweight")
    print("OK: %s commutated electronically" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_stepper(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # counted motion: pulses in, exact revolutions out
    step_deg = 1.8
    steps = int(360.0 / step_deg)
    micro = 16
    usteps = steps * micro
    lead_mm = 8.0
    res_mm = lead_mm / usteps
    rpm = 600.0
    steps_per_s = rpm * steps / 60.0
    print("%d steps/rev; %dx microstepping -> %d microsteps/rev" % (steps, micro, usteps))
    print("on an 8 mm lead screw: %.4f mm per microstep (%.1f um)" % (res_mm, res_mm * 1000))
    print("600 rpm needs exactly %.0f steps/s - no encoder required" % steps_per_s)
    assert steps == 200 and usteps == 3200
    assert abs(res_mm - 0.0025) < 1e-12
    assert steps_per_s == 2000.0
    print("rule: the stepper obeys perfectly - so a lost step lies perfectly too; keep margin")
    print("OK: %s counted the steps" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_sensors(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the three-step chain: temperature -> resistance -> voltage -> number
    B, R0, T0 = 3950.0, 10000.0, 298.15
    T = 273.15 + 60.0
    R = R0 * math.exp(B * (1.0 / T - 1.0 / T0))
    Vcc, Rpull = 3.3, 10000.0
    V = Vcc * R / (Rpull + R)
    code = int(V / Vcc * 4095)
    print("10 k NTC at 60 C: %.1f ohms" % R)
    print("divider at 3.3 V: %.4f V" % V)
    print("12-bit ADC: %d" % code)
    assert 2470.0 < R < 2500.0, R
    assert abs(V - 0.6571) < 0.002, V
    assert code == 815, code
    print("rule: transduction, conditioning, conversion - the chain is only as good as its weakest step")
    print("OK: %s translated heat into a number" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_measure(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ten readings of a 100.000 mm gauge block: precision, bias, and the calibration fix
    data = [100.02, 99.98, 100.01, 100.00, 99.99, 100.03, 100.00, 99.97, 100.01, 100.02]
    n = len(data)
    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data) / (n - 1)
    std = math.sqrt(var)
    stderr = std / math.sqrt(n)
    bias = mean - 100.0
    print("n=%d  mean=%.3f mm  std=%.4f mm  std-err=%.4f mm" % (n, mean, std, stderr))
    print("bias vs the 100.000 mm block: %+.3f mm -> calibrate it out" % bias)
    assert abs(mean - 100.003) < 1e-9, mean
    assert 0.018 < std < 0.020, std
    print("rule: precision is confident; calibration makes it right")
    print("OK: %s separated precision from accuracy" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_servo(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # a PD servo refuses the error: overdamped, no overshoot, zero steady-state error
    J, b, Kp, Kd = 0.001, 0.02, 5.0, 0.5
    zeta = (Kd + b) / (2.0 * math.sqrt(Kp * J))
    target, dt, th, w, peak = 1.0, 0.001, 0.0, 0.0, 0.0
    for _ in range(2000):
        e = target - th
        u = Kp * e - Kd * w
        w += (u - b * w) / J * dt
        th += w * dt
        peak = max(peak, th)
    print("damping ratio zeta = %.2f (overdamped)" % zeta)
    print("after 2 s: theta = %.5f rad (target 1.0); peak = %.5f (overshoot %.3f%%)" % (th, peak, (peak - 1.0) * 100))
    assert abs(zeta - 3.68) < 0.02, zeta
    assert abs(th - 1.0) < 0.005, th
    assert peak <= 1.001, peak
    print("rule: Kp for response, Kd for calm, Ki for exactness - and never let it lie about following error")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_trans(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # motor -> gearbox -> ballscrew: speed traded down, force traded up, friction paid at each stage
    tau_m, rpm_m = 0.4, 3000.0
    ratio, eff_g = 20.0, 0.85
    tau_g = tau_m * ratio * eff_g
    rpm_g = rpm_m / ratio
    lead, eff_s = 0.005, 0.90
    F = 2.0 * math.pi * tau_g * eff_s / lead
    v = rpm_g * lead / 60.0
    print("gearbox 20:1 at 85%%: %.1f N m at %.0f rpm" % (tau_g, rpm_g))
    print("ballscrew 5 mm lead at 90%%: %.0f N thrust at %.1f mm/s" % (F, v * 1000))
    assert abs(tau_g - 6.8) < 1e-9
    assert 7680.0 < F < 7700.0, F
    assert abs(v * 1000 - 12.5) < 1e-9
    print("rule: count every stage's efficiency in the torque budget")
    print("OK: %s traded speed for force" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_solenoid(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ampere-turns squared over gap squared: violent at the end of the stroke, weak at the start
    mu0 = 4.0 * math.pi * 1e-7
    N, I, gap = 500.0, 2.0, 0.002
    bore = 0.010
    A = math.pi * (bore / 2.0) ** 2
    F = mu0 * (N * I) ** 2 * A / (2.0 * gap ** 2)
    L, R = 0.010, 6.0
    tau = L / R
    print("500 turns x 2 A across 2 mm: F = %.1f N" % F)
    print("L/R time constant: %.2f ms to pull in" % (tau * 1000))
    print("24 W in the coil: fine for a punch, fatal held forever - mind the duty cycle")
    assert 12.2 < F < 12.5, F
    assert abs(tau - 0.001667) < 1e-6
    print("rule: clamp the switch-off spike with a flyback diode or the driver dies")
    print("OK: %s pulled the plunger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_voicecoil(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # F = B l I: current in, newtons out, no translation, no negotiation
    B, l, I = 0.5, 10.0, 2.0
    F = B * l * I
    m, f = 0.020, 50.0
    X = F / (m * (2.0 * math.pi * f) ** 2)
    Kf, Ilin, mstage = 25.0, 3.0, 2.0
    Flin = Kf * Ilin
    a = Flin / mstage
    print("speaker coil: %.1f N; 20 g cone at 50 Hz moves %.2f mm" % (F, X * 1000))
    print("linear motor: %.0f N -> %.1f m/s2 on a 2 kg stage, zero backlash" % (Flin, a))
    assert abs(F - 10.0) < 1e-9
    assert abs(X - 0.005066) < 1e-4, X
    assert abs(a - 37.5) < 1e-9
    print("rule: holding force costs continuous current and heat - voice coils love short strokes")
    print("OK: %s pushed without gears" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_hyd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # pressure x area = force; flow / area = speed; pressure x flow = power
    P = 160e5
    bore, rod = 0.063, 0.036
    A_push = math.pi * (bore / 2.0) ** 2
    A_pull = A_push - math.pi * (rod / 2.0) ** 2
    F_push, F_pull = P * A_push, P * A_pull
    Q = 20.0 / 1000.0 / 60.0
    v = Q / A_push
    power = P * Q
    print("63 mm bore at 160 bar: push %.1f kN, pull %.1f kN" % (F_push / 1000, F_pull / 1000))
    print("20 L/min: %.1f mm/s push; hydraulic power %.2f kW" % (v * 1000, power / 1000))
    assert 49800.0 < F_push < 49950.0, F_push
    assert 33500.0 < F_pull < 33680.0, F_pull
    assert abs(v - 0.1069) < 0.001, v
    print("rule: oil barely compresses - stiff, precise, and deserving of relief valves and respect")
    print("OK: %s pushed five tonnes with one hand" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_pneu(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # cheap, fast, springy: the air bill is the real cost of "free" air
    bore = 0.050
    A = math.pi * (bore / 2.0) ** 2
    F = 6e5 * A
    stroke = 0.100
    std_L_per_side = A * stroke * 7.0 * 1000.0   # 6 bar gauge ~ 7 bar absolute
    cycles = 60.0
    air = 2.0 * std_L_per_side * cycles          # double-acting, normal L/min
    Q = 100.0 / 1000.0 / 60.0                    # 100 Nl/min supply
    v = Q / A
    print("50 mm bore at 6 bar: %.0f N" % F)
    print("100 mm stroke drinks %.2f std L per side; 60 double-acting cycles/min -> %.0f Nl/min" % (std_L_per_side, air))
    print("100 Nl/min through the bore: %.2f m/s - cushion the ends" % v)
    assert 1170.0 < F < 1190.0, F
    assert 163.0 < air < 167.0, air
    assert abs(v - 0.8488) < 0.01, v
    print("rule: between two hard stops nothing beats air; asked for a micrometre it hands you a servo")
    print("OK: %s breathed compressed air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_piezo(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # a whisper of crystal strain amplified by a hundred layers
    d33 = 500e-12
    layers, t_layer, V = 100.0, 0.5e-3, 100.0
    L = layers * t_layer
    E = V / t_layer
    strain = d33 * E
    dL = strain * L
    Astack, Estack = 1e-4, 50e9
    k = Astack * Estack / L
    F_block = k * dL
    print("PZT stack 50 mm, 100 V: free %.1f um, blocked %.0f N" % (dL * 1e6, F_block))
    print("strain %.0f microstrain; hysteresis ~15%% - linearize with charge drive or feedback" % (strain * 1e6))
    assert abs(dL - 5e-6) < 1e-12, dL
    assert abs(F_block - 500.0) < 1e-6, F_block
    print("rule: never bend the crystal brutishly - leverage it, and never pull it in tension")
    print("OK: %s flexed the crystal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_sma(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # heat it and the metal insists on who it was: 200 MPa of remembered shape
    d = 0.5e-3
    A = math.pi * (d / 2.0) ** 2
    F = 200e6 * A
    L = 0.100
    stroke = 0.04 * L
    mass = 6450.0 * A * L
    energy = mass * 500.0 * 50.0
    t_heat = energy / 5.0
    print("0.5 mm nitinol wire: %.1f N recovery, %.1f mm stroke on 100 mm" % (F, stroke * 1000))
    print("5 W heats it through 50 K in %.2f s - cooling is the bottleneck" % t_heat)
    assert 39.0 < F < 39.6, F
    assert abs(stroke - 0.004) < 1e-12
    assert 0.6 < t_heat < 0.7, t_heat
    print("rule: silent solid-state muscle - keep working strain under 2-3% for fatigue life")
    print("OK: %s remembered its shape" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_magneto(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # giant magnetostriction: magnetism stretched into 1600 ppm of motion
    lam = 1600e-6
    L = 0.100
    dL = lam * L
    Arod, Erod = 1e-4, 30e9
    k = Arod * Erod / L
    F_block = k * dL
    print("Terfenol-D rod 100 mm: free %.0f um, blocked %.0f N" % (dL * 1e6, F_block))
    print("needs bias magnets, prestress, and a drive solenoid - brittle, expensive, unmatched")
    assert abs(dL - 1.6e-4) < 1e-12, dL
    assert abs(F_block - 4800.0) < 1e-6, F_block
    print("rule: laminate or slot the rod to beat eddy currents at kilohertz")
    print("OK: %s stretched with magnetism" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_enc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # quadrature counting: direction from phase order, 4x resolution from edges
    lines = 1024
    cpr = lines * 4
    res_deg = 360.0 / cpr
    rpm = 3000.0
    counts_per_s = rpm / 60.0 * cpr
    dt = 0.010
    # velocity the honest way: counts in the window -> revolutions -> rpm
    counts = 4096.0
    revs = counts / cpr
    rpm2 = revs / dt * 60.0
    print("%d-line encoder -> %d counts/rev -> %.4f deg per count" % (lines, cpr, res_deg))
    print("at 3000 rpm the controller swallows %.0f counts/s" % counts_per_s)
    print("%.0f counts in %.0f ms = %.0f rpm exactly" % (counts, dt * 1000, rpm2))
    assert cpr == 4096
    assert abs(res_deg - 0.0879) < 0.0001, res_deg
    assert counts_per_s == 204800.0
    assert abs(rpm2 - 6000.0) < 1e-9, rpm2
    print("rule: resolution is counts; accuracy is how true each count is - datasheets list both")
    print("OK: %s counted the rotation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_force(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the Wheatstone bridge turns a 0.2% resistance whisper into millivolts of truth
    Vex, GF, strain = 5.0, 2.0, 1000e-6
    Vout = Vex * GF * strain / 4.0          # quarter bridge
    sens, Vex2 = 2.0e-3, 5.0                # 2 mV/V load cell
    Vfs = sens * Vex2
    Vread = 8.2e-3
    weight = Vread / Vfs * 100.0            # 100 kg cell
    print("quarter bridge (GF=2, 1000 ue, 5 V): %.1f mV" % (Vout * 1000))
    print("2 mV/V cell on 5 V: full scale %.0f mV; reading %.1f mV -> %.1f kg" % (Vfs * 1000, Vread * 1000, weight))
    assert abs(Vout - 0.0025) < 1e-12, Vout
    assert abs(weight - 82.0) < 1e-9, weight
    print("rule: full bridges quadruple the signal and cancel temperature drift")
    print("OK: %s weighed the world" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_pressure(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 4-20 mA: a current that refuses to be corrupted by long wires
    p, pfs = 6.0, 10.0
    I = 4.0 + 16.0 * (p / pfs)
    V = I / 1000.0 * 250.0
    rho, g, h = 1000.0, 9.81, 10.0
    p_water = rho * g * h / 1e5
    print("0-10 bar transmitter at 6 bar: %.1f mA -> %.2f V on 250 ohms" % (I, V))
    print("0 mA would mean a broken wire, not zero pressure - that is the live zero")
    print("10 m water column: %.3f bar" % p_water)
    assert abs(I - 13.6) < 0.01, I
    assert abs(V - 3.4) < 0.01, V
    assert abs(p_water - 0.981) < 0.001, p_water
    print("rule: gauge vs absolute vs differential - pick wrong and err by a whole atmosphere")
    print("OK: %s felt the push" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_temp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # three witnesses of heat: platinum precision, thermocouple ruggedness
    R0 = 100.0
    T = 100.0
    R = R0 * (1.0 + 3.9083e-3 * T - 5.775e-7 * T ** 2)   # Callendar-Van Dusen
    seebeck = 41e-6
    Vtk = seebeck * 100.0
    print("Pt100 at 100 C: %.2f ohms (Callendar-Van Dusen)" % R)
    print("Type K at 100 C difference: %.1f mV - and it measures difference, so compensate the cold junction" % (Vtk * 1000))
    assert abs(R - 138.5055) < 0.01, R
    assert abs(Vtk - 0.0041) < 1e-9
    print("rule: thermocouples for heat and harshness, RTDs for accuracy, thermistors for cheap sensitivity")
    print("OK: %s took the temperature" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_prox(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # shout and listen: sound timed to 0.17 mm; capacitance felt through walls
    c = 343.0
    d = 2.0
    t = 2.0 * d / c
    dt = 1e-6
    res = c * dt / 2.0
    eps0, A = 8.854e-12, 1e-4
    C1, C2 = eps0 * A / 0.005, eps0 * A / 0.004
    print("ultrasonic 2 m round trip: %.2f ms; 1 us timing -> %.2f mm resolution" % (t * 1000, res * 1000))
    print("capacitive 1 cm2: %.3f pF at 5 mm, %.3f pF at 4 mm - senses through non-conductors" % (C1 * 1e12, C2 * 1e12))
    assert abs(t - 0.01166) < 0.00005, t
    assert abs(res - 1.715e-4) < 1e-6, res
    assert abs(C1 * 1e12 - 0.177) < 0.002 and abs(C2 * 1e12 - 0.221) < 0.002
    print("rule: temperature moves sound 0.18%/C - compensate or accept the error")
    print("OK: %s watched the near field" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_vision(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # a picture becomes a measurement when geometry says what each pixel means
    sensor_w, px = 6.4, 640.0
    um_per_px = sensor_w / px * 1000.0
    f, dist = 8.0, 1000.0
    fov = sensor_w * dist / f
    mm_per_px = fov / px
    B, disp_px = 60.0, 6.0
    disp_mm = disp_px * sensor_w / px
    Z = f * B / disp_mm
    print("pixel pitch: %.1f um; at 1 m the field is %.0f mm wide -> %.2f mm/px" % (um_per_px, fov, mm_per_px))
    print("stereo: 60 mm baseline, 6 px disparity -> %.1f m deep" % (Z / 1000.0))
    assert abs(um_per_px - 10.0) < 1e-9
    assert abs(fov - 800.0) < 1e-9 and abs(mm_per_px - 1.25) < 1e-9
    assert abs(Z / 1000.0 - 8.0) < 1e-9, Z
    print("rule: calibrate on a real target - uncalibrated vision measures fiction")
    print("OK: %s measured with light" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_imu(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the inner ear: fast truth from the gyro, slow fiction from its drift
    rate, dt, n = 10.0, 0.01, 500
    angle = 0.0
    for _ in range(n):
        angle += rate * dt
    bias = 0.1
    drift = bias * 60.0
    tilt = math.degrees(math.asin(4.905 / 9.81))
    print("gyro 10 deg/s for 5 s integrates to %.1f deg turned" % angle)
    print("0.1 deg/s bias -> %.1f deg heading error in one minute" % drift)
    print("4.905 m/s2 on x: %.1f deg of tilt from gravity's components" % tilt)
    assert abs(angle - 50.0) < 0.05, angle
    assert abs(drift - 6.0) < 0.01
    assert abs(tilt - 30.0) < 0.01, tilt
    print("rule: brilliant short-term, hopeless alone long-term - fuse it")
    print("OK: %s felt the motion" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_lidar(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # distance from the speed of light; velocity from the Doppler shift
    c = 3e8
    t = 2.0 * 1.0 / c
    dt = 1e-9
    res = c * dt / 2.0
    pts = 10.0 * 3600.0
    lam = 3.9e-3
    fd = 2.0 * 10.0 / lam
    print("1 m round trip: %.2f ns; 1 ns timing -> %.2f m resolution" % (t * 1e9, res))
    print("10 Hz x 3600 pts/rev = %.0f 3D points/s" % pts)
    print("77 GHz radar: 10 m/s approach -> %.0f Hz Doppler shift, straight through fog" % fd)
    assert abs(t - 6.667e-9) < 1e-11, t
    assert abs(res - 0.15) < 1e-9, res
    assert pts == 36000.0
    assert 5100.0 < fd < 5160.0, fd
    print("rule: light for detail, radio for weather - and intensity is not distance")
    print("OK: %s mapped with light and radio" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_tactile(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # artificial skin: squeeze the gap, watch the picofarads rise
    eps0, A = 8.854e-12, 1e-4
    C0 = eps0 * A / 0.001
    C1 = eps0 * A / 0.0009
    ratio = C1 / C0
    taxels = 8 * 8
    Rfsr = 10000.0 * (5.0 ** -0.8)
    print("taxel: %.3f pF at 1 mm -> %.3f pF at 0.9 mm (%.1f%% signal)" % (C0 * 1e12, C1 * 1e12, (ratio - 1) * 100))
    print("8x8 array: %d taxels imaging pressure like a camera images light" % taxels)
    print("FSR: ~%.0f ohms at 5 N (log-log fall from 10 k at 1 N)" % Rfsr)
    assert abs(ratio - 1.1111) < 0.001, ratio
    assert taxels == 64
    assert 2700.0 < Rfsr < 2820.0, Rfsr
    print("rule: watch vibration or pressure-centroid motion - tighten the grip before the drop")
    print("OK: %s learned to touch" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_signal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # one resistor sets the gain; one RC keeps the aliases out
    Rg = 500.0
    G = 1.0 + 50000.0 / Rg
    Vbridge = 2.5e-3
    Vout = Vbridge * G
    R, C, fs = 1600.0, 0.5e-6, 1000.0
    fc = 1.0 / (2.0 * math.pi * R * C)
    print("instrumentation amp Rg=500: gain %.0f; 2.5 mV -> %.1f mV" % (G, Vout * 1000))
    print("anti-alias RC: %.1f Hz corner for %.0f Hz sampling (Nyquist %.0f Hz)" % (fc, fs, fs / 2))
    assert G == 101.0
    assert abs(Vout - 0.2525) < 1e-9, Vout
    assert 198.0 < fc < 200.0, fc
    print("rule: skip conditioning and the best ADC digitizes garbage with exquisite precision")
    print("OK: %s cleaned the microvolts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_adcdac(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the border toll: 805.7 uV per step, and honesty about how many bits are real
    N, Vref = 12, 3.3
    lsb = Vref / (2 ** N)
    qnoise = lsb / math.sqrt(12.0)
    sinad = 70.0
    enob = (sinad - 1.76) / 6.02
    print("12-bit at 3.3 V: LSB = %.1f uV; quantization noise = %.1f uV rms" % (lsb * 1e6, qnoise * 1e6))
    print("70 dB SINAD -> %.2f effective bits: ENOB is the honest resolution" % enob)
    assert 805.0 < lsb * 1e6 < 806.5, lsb
    assert 11.3 < enob < 11.4, enob
    print("rule: the voltage reference IS the ruler - its drift is the system's drift")
    print("OK: %s crossed the border" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_buses(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # two wires for the patient, four for the hurried, arbitration for the urgent
    i2c_hz = 400e3
    thr = i2c_hz / 9.0
    usable = 128 - 16
    spi_hz = 10e6
    spi_thr = spi_hz / 8.0
    can_hz = 1e6
    bit_us = 1e6 / can_hz
    frame_us = 108.0 * bit_us
    print("I2C 400 kHz: %.1f kB/s; 7-bit bus -> ~%d usable addresses" % (thr / 1000, usable))
    print("SPI 10 MHz: %.2f MB/s full duplex" % (spi_thr / 1e6))
    print("CAN 1 Mbps: %.0f us bits, ~%.0f us per 8-byte frame - most urgent wins undamaged" % (bit_us, frame_us))
    assert 44400.0 < thr < 44500.0, thr
    assert usable == 112
    assert abs(spi_thr - 1.25e6) < 1.0
    print("rule: terminate the bus - even electrons need good manners at the end of the line")
    print("OK: %s talked to the chips" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_fusion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # quantified humility: how much to believe the model vs the measurement
    true, x, P, Q, R = 10.0, 0.0, 100.0, 1e-4, 1.0
    for i in range(50):
        z = true + 0.5 * math.sin(i)
        P = P + Q            # predict: uncertainty grows
        K = P / (P + R)      # gain: weight by uncertainties
        x = x + K * (z - x)  # update: correct by surprise x gain
        P = (1.0 - K) * P
    dt = 0.01
    comp = 0.98 * (0.0 + 10.0 * dt) + 0.02 * 30.0
    print("1-D Kalman after 50 noisy samples: %.3f (truth 10.0)" % x)
    print("complementary one-liner: 98%% gyro + 2%% accel -> %.3f deg" % comp)
    assert abs(x - 10.0) < 0.3, x
    assert abs(comp - 0.698) < 0.001, comp
    print("rule: fusion is not averaging - each sensor testifies only to what it knows")
    print("OK: %s fused the witnesses" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_sizing(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the promise written in arithmetic: peak for the hardest move, RMS for the heat
    J = 0.02
    w = 3000.0 * 2.0 * math.pi / 60.0
    alpha = w / 0.5
    tau_acc = J * alpha
    tau_peak = tau_acc + 1.0
    num = tau_peak ** 2 * 0.5 + 2.0 ** 2 * 2.0 + tau_peak ** 2 * 0.5
    tau_rms = math.sqrt(num / 4.0)
    sf = 1.5
    print("0.02 kg m2 to 3000 rpm in 0.5 s: %.2f N m accel + 1 N m friction = %.2f N m peak" % (tau_acc, tau_peak))
    print("duty RMS: %.2f N m -> shop for >= %.1f N m peak, >= %.1f N m continuous (1.5x)" % (tau_rms, tau_peak * sf, tau_rms * sf))
    assert 13.5 < tau_peak < 13.7, tau_peak
    assert 6.9 < tau_rms < 7.0, tau_rms
    assert 20.3 < tau_peak * sf < 20.5
    print("rule: size on paper so the machine never apologizes in metal")
    print("OK: %s sized the drive" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_as_reliability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the honest machine plans its own ending: exponential, memoryless, budgeted
    mtbf, mttr = 50000.0, 4.0
    lam = 1.0 / mtbf
    R_year = math.exp(-lam * 8760.0)
    avail = mtbf / (mtbf + mttr)
    drift_6mo = 0.1 * 6.0
    print("MTBF 50000 h: %.1f%% survive one year" % (R_year * 100))
    print("MTTR 4 h: availability %.5f" % avail)
    print("0.1%%/month drift -> recalibrate every 6 months to hold %.1f%%" % drift_6mo)
    assert 0.838 < R_year < 0.841, R_year
    assert 0.9999 < avail < 1.0, avail
    print("rule: the predicted failure is a maintenance task; the unpredicted one is an incident")
    print("OK: %s planned for failure" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_as_what, "energy_families": demo_as_families,
    "dc_motors": demo_as_dc, "torque_speed": demo_as_torquespeed,
    "bldc": demo_as_bldc, "steppers": demo_as_stepper,
    "sensors_intro": demo_as_sensors, "measurement_truth": demo_as_measure,
    "servos": demo_as_servo, "transmissions": demo_as_trans,
    "solenoids": demo_as_solenoid, "voice_coils": demo_as_voicecoil,
    "hydraulics": demo_as_hyd, "pneumatics": demo_as_pneu,
    "piezo": demo_as_piezo, "sma": demo_as_sma,
    "magnetostrictive": demo_as_magneto, "encoders": demo_as_enc,
    "force_sensors": demo_as_force, "pressure_sensors": demo_as_pressure,
    "temperature_sensors": demo_as_temp, "proximity": demo_as_prox,
    "vision": demo_as_vision, "imu": demo_as_imu,
    "lidar_radar": demo_as_lidar, "tactile": demo_as_tactile,
    "signal_conditioning": demo_as_signal, "adc_dac": demo_as_adcdac,
    "buses": demo_as_buses, "sensor_fusion": demo_as_fusion,
    "sizing": demo_as_sizing, "reliability": demo_as_reliability,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_actuators_sensors.py).
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        # Whole-system dedupe gate (his standing rule: every record, never a sample).
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    # Ladder order guarantee: ids were assigned in ladder order; re-verify.
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in ("actuators-sensors", "actuators-sensors-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    # sanity: ids unique + prefix + required keys + ALL demo programs compile
    # + banned-content scan + ladder fields present
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) >= 30, "fewer than 30 records in %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # machine-execute EVERY demo (canon: runnable demo, machine-executed OK)
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    entries_m = [base.manifest_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [base.api_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
