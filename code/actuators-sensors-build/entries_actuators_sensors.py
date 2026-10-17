#!/usr/bin/env python3
"""Entries for the Actuators and Sensors field databases (field #29, taxonomy order).

Verified 2026-10-17: NO database covers the general actuators-and-sensors
discipline (electric actuators - DC/AC/stepper/servo motors, solenoids, voice
coils; hydraulic and pneumatic actuators; smart materials - piezoelectric,
shape-memory alloy, magnetostrictive; sensors - position/encoders,
force/torque/strain, pressure, temperature, proximity/distance, vision, IMUs,
LIDAR/radar, tactile; signal conditioning; ADC/DAC; interfacing buses
I2C/SPI/CAN; sensor fusion; selection and sizing; failure and maintenance).
- Manifest search (2358 databases): nearest neighbors are the cybersecurity
  'cyber-sensor' database (268 records: network IDS, honeypots, EDR - network
  security sensors, NOT physical transducers), 'phone-sensor-fusion' (15
  phone-only records), 'electrical-electronic-testing' (24 test records),
  'robotics-autonomous-physical-systems' (32 macro robot records),
  'mechatronics-engineers' (people records), and 'microrobotics' (32
  micro-scale records - explicitly micro-scale only). None teaches the
  macro/general actuator-and-sensor discipline.
- Whole-system title sweep over all 760 shard indexes (1,129,453 records):
  actuator/sensor discipline terms hit only study corpora (e.g.
  'electronics-automation-study' 316 shallow textbook-study items with a
  non-canon schema - no description/how-it-works/demo records), incidental
  uses (LiDAR as a mapping tool in earth-sciences records, hall-effect
  keyboard switches, data-format encoders, open-channel hydraulics), and
  application mentions. ZERO full-record discipline coverage anywhere.
- Per the task rule, bare formula cards and study-corpus items do NOT count
  as discipline coverage.

So this build creates two NEW databases, 32 ladder-ordered records each:

  actuators-sensors             - The Actuators and Sensors Database
                                  (public-harvest: real, fact-checked
                                  actuator and sensor engineering)
  actuators-sensors-signature   - The Actuators and Sensors Signature
                                  Database (his original Signature
                                  interpretation; src signature, titles
                                  suffixed " (Signature Edition)", never
                                  presented as authentic public record)

32 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex. Deliberately
macro-scale/general: micro-scale actuation and sensing belong to field #28
(microrobotics) and are not repeated here.

Subtitle disambiguation (fields #13-28 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "DC Motors: The
Spinning Workhorse of Machines".

Numerical cores (all hand-verified 2026-10-17):
- 12 V, 2 A, 75%-efficient motor: 18 W out; 0.0573 N m at 3000 rpm.
- 50 mm bore cylinder: 41.2 kN hydraulic at 210 bar; 1.18 kN pneumatic at 6 bar.
- DC motor (12 V, 1.2 ohm, kt 0.05 N m/A): 10 A stall, 0.5 N m stall torque,
  240 rad/s no-load; 0.2 N m load -> 1375 rpm, 60% efficient.
- 30 N m at 60 rpm = 188.5 W; 0.3 N m at 6000 rpm motor through 100:1 at 90%
  efficiency delivers 27 N m (3 N m lost - oversize honestly).
- BLDC KV 1000 rpm/V on 12 V -> 12000 rpm; kt = 0.00955 N m/A; 4 pole pairs
  -> 24 commutations per rev; 2400 Hz at 6000 rpm.
- Stepper 1.8 deg -> 200 steps/rev; 16x microstepping -> 3200; 8 mm lead
  screw -> 2.5 um per microstep; 600 rpm -> 2000 steps/s.
- 10 k NTC (B=3950) at 60 C -> 2486 ohm; 10 k divider at 3.3 V -> 0.6571 V;
  12-bit ADC reads 815.
- Gauge-block data (n=10): mean 100.003 mm, sample std 0.0189 mm.
- PD servo (J=1e-3, b=0.02, Kp=5, Kd=0.5): overdamped (zeta 3.68), settles to
  1.0 rad within 2 s with zero steady-state error.
- 0.4 N m at 3000 rpm through 20:1 (85%) -> 6.8 N m at 150 rpm; 5 mm
  ballscrew (90%) -> 7.69 kN thrust, 12.5 mm/s.
- Solenoid (500 turns, 2 A, 2 mm gap, 10 mm bore): ~12.3 N; L/R = 1.67 ms.
- Voice coil (B=0.5 T, 10 m wire, 2 A) -> 10 N; 20 g mass at 50 Hz ->
  5.07 mm excursion. Linear motor 25 N/A at 3 A -> 75 N, 37.5 m/s2 on 2 kg.
- Hydraulic cylinder (63 mm bore, 36 mm rod, 160 bar): 49.9 kN push,
  33.6 kN pull; 20 L/min -> 106.9 mm/s push, 5.33 kW.
- Pneumatic (50 mm bore, 6 bar): 1.18 kN; 100 mm stroke uses 1.37 std L per
  side; 60 double-acting cycles/min -> ~165 Nl/min; 100 Nl/min -> 0.85 m/s.
- Piezo stack (d33=500 pm/V, 100 x 0.5 mm layers, 100 V): 5 um free, 500 N
  blocked; ~15% hysteresis.
- Nitinol wire (0.5 mm, 200 MPa recovery): 39.3 N, 4 mm stroke on 100 mm;
  5 W heats it in ~0.63 s.
- Terfenol-D (1600 ppm, 100 mm rod): 160 um free, 4800 N blocked.
- 1024 ppr quadrature encoder -> 4096 counts/rev, 0.0879 deg; 3000 rpm ->
  204800 counts/s; 4096 counts in 10 ms -> 6000 rpm.
- Quarter-bridge strain gauge (GF=2, 1000 ue, 5 V): 2.5 mV; 2 mV/V load cell
  at 5 V reads 8.2 mV -> 82 kg on a 100 kg cell.
- 0-10 bar 4-20 mA transmitter at 6 bar -> 13.6 mA -> 3.4 V on 250 ohm;
  10 m water column = 0.981 bar.
- Pt100 at 100 C (Callendar-Van Dusen) = 138.51 ohm; Type K ~41 uV/C ->
  4.1 mV per 100 C.
- Ultrasonic 2 m round trip -> 11.66 ms; 1 us timing -> 0.17 mm resolution.
- Camera (6.4 mm sensor, 640 px, f=8 mm) at 1 m: 800 mm field, 1.25 mm/px;
  stereo (60 mm baseline, 6 px disparity) -> 8.0 m.
- Gyro 10 deg/s for 5 s -> 50 deg; 0.1 deg/s drift -> 6 deg in a minute;
  4.905 m/s2 on x -> 30 deg tilt.
- LIDAR: 1 m round trip -> 6.67 ns; 1 ns timing -> 0.15 m resolution;
  10 Hz x 3600 pts -> 36000 pts/s; 77 GHz radar, 10 m/s -> 5.13 kHz Doppler.
- Capacitive taxel (1 cm2, 1 mm gap): 0.885 pF; squeezed to 0.9 mm ->
  0.984 pF (11.1% rise); 8x8 array = 64 taxels.
- Instrumentation amp (Rg=500 ohm) -> gain 101; 2.5 mV -> 252.5 mV;
  anti-alias RC (1.6 k, 0.5 uF) -> 198.9 Hz corner for 1 kHz sampling.
- 12-bit ADC at 3.3 V: LSB 805.7 uV, quantization noise 232.6 uV rms;
  70 dB SINAD -> 11.34 effective bits.
- I2C at 400 kHz: 9 clocks/byte -> 44.4 kB/s; 7-bit bus -> ~112 usable
  addresses; SPI at 10 MHz -> 1.25 MB/s full duplex; CAN 1 Mbps -> 1 us bit.
- 1-D Kalman (Q=1e-4, R=1, true 10.0, 50 noisy samples) converges within
  0.3 of truth; complementary filter blends gyro and accel tilt.
- Inertia 0.02 kg m2, 0-3000 rpm in 0.5 s: 12.57 N m accel + 1 N m friction
  -> 13.57 N m peak; RMS over the duty cycle 6.93 N m; size 1.5x -> 20.4/10.4.
- MTBF 50000 h: 1-year reliability 0.839; 4 h MTTR -> 0.99992 availability.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "actuators and sensors, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_BOLTON = ("Bolton, W. 'Mechatronics: Electronic Control Systems in "
            "Mechanical and Electrical Engineering'. 7th ed. Pearson, 2019.")
C_FRADEN = ("Fraden, Jacob. 'Handbook of Modern Sensors: Physics, Designs, "
            "and Applications'. 5th ed. Springer, 2016.")
C_DUNN = ("Dunn, William C. 'Introduction to Instrumentation, Sensors, and "
          "Process Control'. Artech House, 2006.")
C_NYCE = ("Nyce, David S. 'Linear Position Sensors: Theory and Application'. "
          "Wiley-Interscience, 2004.")
C_JOHNSON = ("Johnson, Curtis D. 'Process Control Instrumentation Technology'. "
             "8th ed. Pearson Prentice Hall, 2006.")
C_IEEE176 = ("'IEEE Standard on Piezoelectricity'. ANSI/IEEE Std 176-1987. "
             "IEEE, 1988.")
C_BISHOP = ("Bishop, Robert H. (ed.). 'The Mechatronics Handbook'. CRC Press, "
            "2002.")
C_KALMAN = ("Welch, Greg and Bishop, Gary. 'An Introduction to the Kalman "
            "Filter'. Technical Report TR 95-041, University of North "
            "Carolina at Chapel Hill, 2006.")
C_CAN = ("Robert Bosch GmbH. 'CAN Specification, Version 2.0'. Stuttgart, "
         "1991.")
C_I2C = ("NXP Semiconductors. 'I2C-bus specification and user manual'. "
         "UM10204, Rev. 6, 2014.")
C_LAGOUDAS = ("Lagoudas, Dimitris C. (ed.). 'Shape Memory Alloys: Modeling "
              "and Engineering Applications'. Springer, 2008.")
C_JANOCHA = ("Janocha, Hartmut (ed.). 'Adaptronics and Smart Structures: "
             "Basics, Materials, Design, and Applications'. Springer, 1999.")
C_HENDERSHOT = ("Hendershot, J. R. and Miller, T. J. E. 'Design of Brushless "
                "Permanent-Magnet Machines'. Motor Design Books, 2010.")
C_ESPOSITO = ("Esposito, Anthony. 'Fluid Power with Applications'. 7th ed. "
              "Pearson Prentice Hall, 2009.")
C_OGATA = ("Ogata, Katsuhiko. 'Modern Control Engineering'. 5th ed. Pearson, "
           "2010.")
C_TIT = ("Titterton, D. H. and Weston, J. L. 'Strapdown Inertial Navigation "
         "Technology'. 2nd ed. IET, 2004.")
C_SZE = ("Szeliski, Richard. 'Computer Vision: Algorithms and Applications'. "
         "Springer, 2010.")
C_SHAN = ("Shan, Jie and Toth, Charles K. (eds.). 'Topographic Laser Ranging "
          "and Scanning: Principles and Processing'. CRC Press, 2008.")
C_NIST = ("Burns, G. W. et al. 'Temperature-Electromotive Force Reference "
          "Functions and Tables for the Letter-Designated Thermocouple Types "
          "Based on the ITS-90'. NIST Monograph 175, 1993.")
C_CLARK = ("Clark, A. E. 'Magnetostrictive rare earth-Fe2 compounds'. In "
           "Wohlfarth, E. P. (ed.), 'Ferromagnetic Materials', Vol. 1. "
           "North-Holland, 1980.")
C_ADC = ("Kester, Walt (ed.). 'Data Conversion Handbook'. Analog Devices / "
         "Elsevier, 2005.")
C_OCONNOR = ("O'Connor, Patrick and Kleyner, Andre. 'Practical Reliability "
             "Engineering'. 5th ed. Wiley, 2012.")
C_DAHIYA = ("Dahiya, R. S. et al. 'Directions Toward Effective Utilization "
            "of Tactile Skin: A Review'. IEEE Sensors Journal, Vol. 13, No. "
            "11, 2013.")

ENTRIES = [
{
"key": "what_is",
"name": "What Are Actuators and Sensors: The Muscle and the Senses of Every Machine",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"An actuator turns energy into motion or force; a sensor turns a physical "
"quantity into a signal a controller can read. Together they are the muscle "
"and the senses of every machine, from a washing machine's water valve to a "
"robot arm placing parts. An actuator takes an input - usually electricity, "
"sometimes pressurized oil or air - and produces torque, thrust, pressure, or "
"displacement at its output. A sensor does the reverse: it watches position, "
"force, temperature, light, or motion and reports a voltage, a current, or a "
"stream of digital numbers. The controller sits between them, reading sensors "
"and commanding actuators in a loop. A 12-volt motor drawing 2 amps at "
"75 percent efficiency delivers 18 watts of shaft power - at 3000 rpm that "
"is 0.057 newton-metres of torque. That single chain, electrical power in, "
"mechanical power out, measured power reported back, is the entire subject "
"of this database: how machines push the world, and how they feel what they "
"are doing."),
"how_it_works": (
"Every actuator is an energy converter with an efficiency less than one, and "
"every sensor is a transducer with a transfer function. Start with power: "
"electrical watts in, mechanical watts out, the difference lost as heat. "
"The motor equation links the two worlds: torque times angular speed equals "
"mechanical power, voltage times current equals electrical power, and "
"efficiency is their ratio. A sensor reverses the flow: a physical quantity "
"deforms, heats, or illuminates a transducer element, the element changes a "
"resistance, capacitance, or voltage, and conditioning electronics turn that "
"change into a clean signal. The controller closes the loop - it compares "
"the sensor reading with the desired value and adjusts the actuator command "
"to shrink the difference. Every record in this database is one piece of "
"that loop: one way of pushing, one way of feeling, one way of converting, "
"one way of choosing."),
"key_points": [
"An actuator converts energy into motion or force; a sensor converts a physical quantity into a readable signal.",
"Electrical power in times efficiency equals mechanical power out: P = tau x omega.",
"A 12 V, 2 A motor at 75% efficiency delivers 18 W - 0.057 N m at 3000 rpm.",
"The controller closes the loop: it reads sensors, compares with the goal, and commands actuators.",
"Every machine is the same loop: sense, decide, act, sense again.",
"No actuator is 100% efficient; the missing power always becomes heat.",
],
"requirements": [
"No prerequisites - this record introduces the discipline.",
"A calculator for the power exercises in the demo.",
"Familiarity with watts, volts, amps, and newtons.",
],
"standards": [
"IEC 60050 (International Electrotechnical Vocabulary) defines actuator and sensor terminology.",
"ISO 8373 (robotics vocabulary) frames actuators in robotic systems.",
"IEEE 2700-2017 defines how sensor performance is specified.",
],
"citations": [C_BOLTON, C_FRADEN, C_BISHOP],
"sig_lens": (
"Signature take: the actuator is the Signature hand and the sensor is the "
"Signature eye - no intelligence exists without both. A mind that cannot "
"push and cannot feel is a mind in a box. The Signature machine is built "
"from this loop outward: every capability begins as a muscle that can move "
"and a sense that can report, and everything clever is choreography on top "
"of that honest exchange."),
},
{
"key": "energy_families",
"name": "The Energy Families of Motion: Electric, Hydraulic, and Pneumatic Power",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Almost every actuator belongs to one of three energy families. Electric "
"actuators - motors, solenoids, voice coils - run on current and voltage; "
"they are clean, quiet, precise, and easy to control, which is why they "
"dominate everything from phones to factory robots. Hydraulic actuators run "
"on pressurized oil, typically 100 to 350 bar; oil barely compresses, so a "
"modest 50 mm bore cylinder at 210 bar pushes with 41.2 kilonewtons - the "
"force behind excavators, presses, and aircraft controls. Pneumatic "
"actuators run on compressed air at 4 to 8 bar; air is springy, so they are "
"fast and gentle but less stiff - a 50 mm bore cylinder at 6 bar gives just "
"1.18 kilonewtons, perfect for pick-and-place speed. Choosing a family is "
"the first and biggest actuation decision: electrics for precision and "
"cleanliness, hydraulics for brute force in a small package, pneumatics "
"for cheap speed. A 0.5 newton-metre electric motor spinning at 3000 rpm "
"makes 157 watts - about 157 watts per kilogram for a 1 kg motor - while "
"hydraulics pack ten to a hundred times the power density where the pump "
"and plumbing are acceptable."),
"how_it_works": (
"Each family converts its stored energy the same way: energy in, force or "
"torque out, losses as heat. An electric motor turns current in windings "
"into torque on a rotor through magnetic forces - torque is proportional to "
"current, speed to voltage. A hydraulic cylinder turns oil pressure into "
"thrust: force equals pressure times piston area, so high pressure on a "
"small bore makes enormous force, and flow rate sets the speed. A pneumatic "
"cylinder does the same with air, but because air compresses, the cylinder "
"acts like a spring - fast and compliant rather than rigid. Smart materials "
"form a fourth, smaller family: crystals and alloys that strain directly "
"under voltage, heat, or magnetic fields, covered later in this database. "
"Engineers compare families on force density, speed, stiffness, "
"efficiency, cleanliness, and cost - and then usually pick electric unless "
"the job screams otherwise."),
"key_points": [
"Electric: clean, precise, easy to control; torque proportional to current, speed to voltage.",
"Hydraulic: 100-350 bar oil; 50 mm bore at 210 bar gives 41.2 kN - brute force in a small package.",
"Pneumatic: 4-8 bar air; 50 mm bore at 6 bar gives 1.18 kN - fast and cheap but springy.",
"A 0.5 N m motor at 3000 rpm makes 157 W - roughly 157 W/kg for a 1 kg motor.",
"Force equals pressure times area in fluid power; flow rate sets the speed.",
"Pick electric for precision, hydraulic for force density, pneumatic for cheap speed.",
],
"requirements": [
"The actuator/sensor loop from the previous record.",
"Pressure units: 1 bar = 100,000 pascals.",
"A calculator for the force exercises in the demo.",
],
"standards": [
"ISO 4413 (hydraulic fluid power) and ISO 4414 (pneumatic fluid power) set safety rules.",
"NFPA/T3.6 and CETOP standards govern hydraulic component ratings.",
"IEC 60034 rates rotating electrical machines.",
],
"citations": [C_ESPOSITO, C_BOLTON, C_BISHOP],
"sig_lens": (
"Signature take: the three families are three temperaments of strength. "
"Electricity is the disciplined athlete - precise, tireless, clean. "
"Hydraulics is the strongman - quiet bulk force that never complains. "
"Pneumatics is the sprinter - explosive, cheap, a little wild. The "
"Signature builder does not marry one temperament; the machine gets the "
"muscle its job deserves, and the Signature is in the honesty of the "
"match."),
},
{
"key": "dc_motors",
"name": "DC Motors: The Spinning Workhorse of Machines",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"The brushed DC motor is the simplest useful actuator ever built: apply a "
"voltage and the shaft spins, reverse the voltage and it spins back. Inside "
"are magnets on the outside, wire coils on the spinning rotor, and a "
"mechanical switch - the commutator with its carbon brushes - that flips the "
"coil current twice per revolution so the magnetic push always points the "
"same way around. Two constants describe the whole machine: the torque "
"constant kt says how many newton-metres each ampere buys, and the "
"back-EMF constant ke says how many volts each radian per second generates "
"back - in SI units the two numbers are equal. A 12-volt motor with "
"1.2 ohms of winding resistance and kt of 0.05 N m/A draws 10 amps stalled "
"for 0.5 N m of stall torque, spins 240 rad/s (2292 rpm) with no load, and "
"at a 0.2 N m load settles at 1375 rpm running 60 percent efficient. Speed "
"is set by voltage, torque by current - that clean separation is why DC "
"motors are the first actuator every student meets, and why they still run "
"wipers, windows, toys, and small robots everywhere."),
"how_it_works": (
"Current in a coil inside a magnetic field feels a force - the Lorentz "
"force - and with the coil wound on a rotor that force becomes torque. The "
"commutator reverses the coil connections exactly when the coil passes the "
"magnetic neutral plane, so the torque never reverses even though the coil "
"keeps spinning. As the rotor turns it also acts as a generator: the "
"spinning coils cut the magnetic field and produce a voltage - the back "
"EMF - proportional to speed and opposing the supply. The current that "
"flows is the supply voltage minus the back EMF, divided by the winding "
"resistance. More load means more current; more current means more torque; "
"and the speed droops until torque balances the load. Brushes wear and "
"spark, which is the price of the mechanical commutator - the brushless "
"version keeps the physics and replaces the switch with electronics."),
"key_points": [
"Voltage sets speed, current sets torque - the two knobs are nearly independent.",
"Stall current = V/R; stall torque = kt x stall current; no-load speed = V/ke.",
"A 12 V, 1.2 ohm, 0.05 N m/A motor: 10 A stall, 0.5 N m stall torque, 240 rad/s no-load.",
"At 0.2 N m load it runs 1375 rpm at 60% efficiency.",
"The commutator and brushes flip coil current twice per rev - they wear and spark.",
"Back EMF is the motor acting as a generator; it is why speed droops under load.",
],
"requirements": [
"Torque, speed, and power from the previous records.",
"Ohm's law: V = I x R.",
"A calculator for the motor exercises in the demo.",
],
"standards": [
"IEC 60034-1 rates DC machines (duty types, ratings).",
"NEMA MG 1 covers motor dimensions and performance in North America.",
"IEEE 113-1985 guides DC machine testing.",
],
"citations": [C_BOLTON, C_BISHOP, C_HENDERSHOT],
"sig_lens": (
"Signature take: the DC motor is the honest engine - it tells you exactly "
"what it is doing. Current is effort, voltage is pace, heat is the tax. "
"There is no hiding in a DC motor: ask for too much torque and the "
"ammeter confesses. The Signature builder loves this machine because it "
"teaches the first law of actuation - every push has a price, and the "
"price is always written on the meter."),
},
{
"key": "torque_speed",
"name": "Torque, Speed, and Power: The Three Numbers Every Motor Lives By",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Every rotating actuator is described by three numbers that multiply "
"together: torque in newton-metres, speed in radians per second, and power "
"in watts, with power equal to torque times speed. You cannot have high "
"torque and high speed from a small motor at once - the product is capped "
"by the power the motor can handle. A job needing 30 N m at 60 rpm "
"demands 188.5 watts; a motor making 0.3 N m at 6000 rpm also makes "
"188.5 watts, so a 100:1 gearbox connects them - at 90 percent gearbox "
"efficiency the output is 27 N m, and the honest engineer either accepts "
"27, picks a slightly bigger motor, or finds a more efficient gearbox. "
"This is the sizing equation that governs all of actuation: match the "
"power, trade torque against speed with gears or screws, and budget the "
"losses at every stage. Motors also have two ratings that matter - "
"continuous torque, which the cooling can sustain forever, and peak "
"torque, which the windings survive for seconds. Size for the continuous "
"rating at the worst duty point; check the peak rating for the hardest "
"single move."),
"how_it_works": (
"Mechanical power is force times velocity in a straight line and torque "
"times angular velocity in rotation: P = tau x omega. Convert rpm to "
"rad/s by multiplying by 2 pi and dividing by 60. The power is conserved "
"through a gearbox (minus efficiency), so torque goes up exactly as much "
"as speed goes down: a 100:1 reducer multiplies torque by 100 and divides "
"speed by 100. Plot the motor's torque against speed and you get its "
"operating map: DC motors give a straight line from stall torque to "
"no-load speed, and the power peaks in the middle. The load has its own "
"line - friction, inertia, gravity - and where the two lines cross is "
"where the machine actually runs. Sizing is the art of placing that "
"crossing point in the motor's happy zone: not at stall, not at no-load, "
"and never beyond the continuous rating for longer than the duty allows."),
"key_points": [
"Power = torque x angular velocity; convert rpm to rad/s with 2 pi / 60.",
"30 N m at 60 rpm = 188.5 W; a 0.3 N m, 6000 rpm motor matches it through 100:1 gearing.",
"Gearbox efficiency eats torque: 90% of ideal 30 N m leaves 27 N m - budget honestly.",
"Continuous torque is forever; peak torque is for seconds - size for continuous.",
"The motor curve and the load curve cross at the real operating point.",
"Trade torque for speed with gears, screws, or belts; power is what is conserved.",
],
"requirements": [
"The DC motor record (torque constant, back EMF).",
"Unit conversion between rpm and rad/s.",
"A calculator for the sizing exercises in the demo.",
],
"standards": [
"IEC 60034-1 defines continuous (S1) and short-time (S2) duty ratings.",
"AGMA 2001 rates gear tooth strength for the torque multiplication stage.",
"ISO 3408 rates ballscrews that convert the torque to thrust.",
],
"citations": [C_BOLTON, C_OGATA, C_BISHOP],
"sig_lens": (
"Signature take: torque, speed, and power are the three honest numbers - "
"they cannot be negotiated with, only traded. Want more push? Surrender "
"pace. Want more pace? Surrender push. The Signature engineer writes these "
"three numbers at the top of every design and never lets marketing move "
"them. Power is the budget; torque and speed are how you spend it."),
},
{
"key": "sensors_intro",
"name": "What Sensors Do: Turning the Physical World into Numbers",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"A sensor is a translator: it takes a physical quantity - temperature, "
"force, light, motion - and produces a signal, usually a voltage or a "
"stream of digital numbers, that a controller can use. Inside every sensor "
"is a transducer element whose electrical property changes with the "
"quantity: a thermistor's resistance falls as it warms, a strain gauge's "
"resistance stretches with force, a photodiode's current rises with light. "
"Conditioning electronics amplify and clean that tiny change, and an "
"analog-to-digital converter turns it into numbers. Follow one concrete "
"chain: a 10 k thermistor with a B-value of 3950 ohms reads 2486 ohms at "
"60 C; in a divider with a 10 k resistor at 3.3 volts that is 0.6571 volts; "
"a 12-bit converter turns that into the number 815. Temperature became "
"resistance, resistance became voltage, voltage became a number - that "
"three-step chain, transduction, conditioning, conversion, is inside "
"every sensor you will ever meet, from a ten-cent thermistor to a "
"million-dollar LIDAR."),
"how_it_works": (
"Transduction starts the chain: the sensing element converts the measurand "
"into an electrical change - resistive (thermistor, strain gauge, "
"photoresistor), capacitive (pressure diaphragms, touch), inductive "
"(proximity, LVDT), or self-generating (thermocouple, piezoelectric, "
"photodiode). The raw change is almost always small - millivolts, "
"microamps, fractions of a percent - so conditioning amplifies it, filters "
"noise, and shifts it into the converter's range. The ADC samples the "
"voltage at discrete times and rounds each sample to the nearest of its "
"2^N levels; a 12-bit converter has 4096 levels. Calibration closes the "
"story: the raw number is mapped to engineering units through a curve "
"measured against a known reference, because no two sensing elements are "
"exactly alike. The quality of a sensor is the quality of this whole "
"chain, not just the element."),
"key_points": [
"Every sensor is a three-step chain: transduction, conditioning, conversion to numbers.",
"Transducer elements change resistance, capacitance, inductance, voltage, or current with the quantity.",
"A 10 k NTC thermistor at 60 C: 2486 ohms -> 0.6571 V in a divider -> ADC number 815.",
"Raw sensor signals are tiny; conditioning amplifies, filters, and ranges them.",
"Calibration maps raw numbers to engineering units against a known reference.",
"The chain is only as good as its weakest step.",
],
"requirements": [
"The actuator/sensor loop record.",
"Voltage dividers: Vout = Vin x R2/(R1+R2).",
"A calculator for the thermistor chain in the demo.",
],
"standards": [
"IEEE 2700-2017 standardizes sensor performance specifications.",
"IEC 60751 defines industrial platinum resistance thermometers.",
"ASTM E230 defines thermocouple EMF tables.",
],
"citations": [C_FRADEN, C_DUNN, C_JOHNSON],
"sig_lens": (
"Signature take: the sensor is how the machine touches reality - and "
"reality only speaks through translation. Temperature cannot enter a "
"computer; only numbers can. So the sensor is a diplomat between two "
"worlds, and like every diplomat it can misreport. The Signature builder "
"respects the chain: transducer, conditioning, conversion, calibration - "
"and never trusts a number whose journey is unknown."),
},
{
"key": "bldc",
"name": "Brushless DC Motors: Magnets That Switch Themselves",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"The brushless DC motor keeps everything good about the DC motor and "
"throws away the wearing parts: the magnets move to the spinning rotor and "
"the coils stay still on the stator, so there are no brushes and no "
"commutator to wear out or spark. An electronic controller does the "
"commutating instead - it energizes the stator coils in sequence, chasing "
"the rotor's magnets around, and it knows the rotor's position from Hall "
"sensors or from the back EMF in the unpowered coil. The payoff is "
"dramatic: higher efficiency, higher speed, longer life, and far better "
"power density - this is the motor in drones, e-bikes, power tools, and "
"electric cars. Ratings use KV: a 1000 KV motor spins 1000 rpm per volt "
"with no load, so on 12 volts it reaches 12000 rpm, and its torque "
"constant is 0.00955 N m per amp. With 4 pole pairs the controller makes "
"24 commutations per revolution, switching at 2400 Hz when the motor "
"runs 6000 rpm. The price is complexity: a brushless motor is a paperweight "
"without its electronic drive."),
"how_it_works": (
"Three stator windings form three phases; energizing two at a time creates "
"a magnetic field vector that the rotor's permanent magnets chase. The "
"controller advances the field in six steps per electrical revolution - "
"the classic six-step commutation - and with P pole pairs each mechanical "
"revolution contains P electrical revolutions, hence 6P steps. Position "
"feedback tells the controller when to step: Hall-effect sensors read the "
"rotor magnets directly (sensored), or the controller watches the voltage "
"induced in the floating phase (sensorless back-EMF). KV and kt are two "
"faces of the same constant: kt in N m/A equals 60/(2 pi x KV) with KV in "
"rpm/V. Field-oriented control refines six-step into smooth sinusoidal "
"drive, holding the stator field exactly 90 electrical degrees ahead of "
"the rotor for maximum torque per amp - the same physics, executed with "
"finer timing."),
"key_points": [
"Magnets on the rotor, coils on the stator - no brushes, no commutator, no wear.",
"Electronics commutate: six steps per electrical revolution, 6P steps per mechanical rev.",
"A 1000 KV motor on 12 V reaches 12000 rpm; kt = 0.00955 N m/A.",
"4 pole pairs at 6000 rpm means 2400 commutations per second.",
"Hall sensors or back-EMF sensing tell the controller the rotor position.",
"Needs its electronic drive - without it, a brushless motor does nothing.",
],
"requirements": [
"The DC motor record (torque constant, back EMF).",
"Three-phase sequencing intuition.",
"A calculator for the KV/kt exercises in the demo.",
],
"standards": [
"IEC 60034-30-1 covers efficiency classes of motors including BLDC.",
"NEMA MG 1 Part 31 addresses motors on electronic drives.",
"UL 1004-1 covers safety of rotating electrical machines.",
],
"citations": [C_HENDERSHOT, C_BOLTON, C_BISHOP],
"sig_lens": (
"Signature take: the brushless motor is the DC motor grown up - it traded "
"its mechanical switch for judgment. The brushes were honest but mortal; "
"the controller is tireless but blind without its sensors. So the "
"brushless motor teaches the Signature lesson of the whole field: replace "
"wearing parts with sensing and timing, and the machine stops dying and "
"starts listening."),
},
{
"key": "steppers",
"name": "Stepper Motors: Motion in Counted Steps",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"A stepper motor moves in exact, countable increments - typically 1.8 "
"degrees per step, 200 steps per revolution - and holds its position with "
"magnetic detent even with no power in some designs. Command 200 pulses "
"and the shaft turns exactly once; command them at 2000 pulses per second "
"and it spins 600 rpm. That open-loop precision is the stepper's superpower: "
"no encoder needed for 3D printers, CNC machines, and camera gimbals that "
"trust the count. Microstepping divides each full step - 16x microstepping "
"gives 3200 microsteps per rev - smoothing motion and, with an 8 mm lead "
"screw, delivering 2.5 micrometres of linear resolution per microstep. The "
"limits are real: torque falls as speed rises because the winding "
"inductance resists fast current changes, so a motor holding 0.45 N m "
"standing still may pull out of synchronism above its torque-speed curve; "
"and if the load ever overpowers it, steps are lost silently and the "
"controller's count lies. Size the holding torque with margin, keep speeds "
"on the curve, and the stepper is the most obedient actuator built."),
"how_it_works": (
"Toothed iron rotors and sequenced stator coils: each pulse advances the "
"stator's magnetic field by one step angle, and the rotor's teeth snap to "
"the nearest alignment - the detent torque of the permanent-magnet or "
"hybrid rotor holds it between pulses. A driver chip sequences the two "
"phases (full, half, or microstepping waveforms); microstepping varies the "
"phase currents sinusoidally to park the rotor between detent positions. "
"Torque comes from the magnetic shear between stator and rotor teeth and is "
"maximal at standstill (holding torque); as step rate rises, winding "
"inductance (L/R time constant) prevents current from reaching full value "
"in each step, so torque rolls off - the pull-out curve every datasheet "
"prints. Resonance at certain step rates can make the rotor oscillate and "
"skip; microstepping and mechanical damping tame it. Because position is "
"inferred from the pulse count, any skipped step is an invisible error - "
"closed-loop steppers add an encoder to catch it."),
"key_points": [
"1.8 deg per step = 200 steps/rev; 16x microstepping = 3200 microsteps/rev.",
"With an 8 mm lead screw, each microstep moves 2.5 um.",
"600 rpm needs exactly 2000 steps/s - motion is countable and open-loop.",
"Holding torque (e.g. 0.45 N m) is the standstill rating; torque falls with speed.",
"Lost steps are silent - the controller's count keeps lying after a stall.",
"Resonance at certain rates can skip steps; microstepping damps it.",
],
"requirements": [
"The DC motor and torque/speed records.",
"Pulse-frequency to rpm conversion.",
"A calculator for the resolution exercises in the demo.",
],
"standards": [
"NEMA ICS 16 defines stepper motor/drive terminology and testing.",
"IEC 60034-1 duty ratings apply to thermal sizing.",
"ISO 230-2 tests positioning accuracy of the resulting axes.",
],
"citations": [C_BOLTON, C_BISHOP, C_OGATA],
"sig_lens": (
"Signature take: the stepper is the obedient actuator - it does exactly "
"what it is told, one counted step at a time, and asks for no supervision. "
"That obedience is also its flaw: it cannot report betrayal. The "
"Signature builder counts on the stepper but verifies with a sensor, "
"because trust without verification is how machines quietly ruin work."),
},
{
"key": "measurement_truth",
"name": "Measurement Truth: Accuracy, Precision, Resolution, and Calibration",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Four words govern whether a sensor reading means anything, and engineers "
"use them with surgical precision. Resolution is the smallest change the "
"sensor can report - a ruler marked in millimetres resolves 1 mm. "
"Precision (repeatability) is how tightly repeated readings cluster: ten "
"measurements of a 100.000 mm gauge block reading 99.97 to 100.03 mm with "
"a mean of 100.003 mm and a standard deviation of 0.0189 mm are precise. "
"Accuracy is how close the mean sits to the truth: that same set is "
"accurate to 0.003 mm once the +0.003 mm bias is calibrated out. "
"Calibration is the act of measuring the sensor against a known reference "
"and correcting the bias - without it, precision is just confident "
"wrongness. Then come the fine print: hysteresis (different readings "
"approaching from above vs below), linearity (how straight the response "
"curve is), drift (how the reading wanders with time and temperature), and "
"noise (the random jitter on every reading). A sensor's datasheet is a "
"contract written in these words - read it before trusting a single "
"number."),
"how_it_works": (
"Statistics turn repeated readings into truth claims. The mean estimates "
"the systematic offset; the sample standard deviation estimates the random "
"spread; the standard error of the mean (std divided by root-n) says how "
"well the mean itself is known - with n=10 and std 0.0189 mm, the mean is "
"known to about 0.006 mm. Calibration compares the sensor against a "
"reference standard traceable to national labs and fits a correction - "
"offset, gain, or a full lookup curve - that the system applies to every "
"reading. Hysteresis is measured by approaching the same point from both "
"directions; linearity by fitting a straight line and reporting the worst "
"deviation as percent of full scale; drift by logging the reading over "
"hours and degrees. Uncertainty budgets combine them all, usually as a "
"root-sum-of-squares, so the final claim reads like '100.00 mm plus or "
"minus 0.02 mm at 95 percent confidence' - the only honest way to report a "
"measurement."),
"key_points": [
"Resolution: smallest reportable change. Precision: tightness of repeats. Accuracy: closeness to truth.",
"Ten gauge-block readings: mean 100.003 mm, std 0.0189 mm - precise; calibrate out the 0.003 mm bias to be accurate.",
"Calibration measures the sensor against a known reference and corrects the bias.",
"Hysteresis, linearity, drift, and noise are the fine print on every datasheet.",
"Standard error of the mean = std / sqrt(n) - more readings pin down the mean.",
"Report measurements with uncertainty: value plus-or-minus, with confidence.",
],
"requirements": [
"The sensor introduction record.",
"Mean and standard deviation.",
"A calculator or the demo for the statistics.",
],
"standards": [
"GUM (JCGM 100:2008) is the international guide to measurement uncertainty.",
"ISO 17025 governs calibration laboratory competence.",
"NIST Handbook 150 and traceability chains anchor references to SI units.",
],
"citations": [C_DUNN, C_FRADEN, C_JOHNSON],
"sig_lens": (
"Signature take: measurement is the only honesty a machine has, and "
"honesty has four names. Resolution is what it can see, precision is how "
"steadily it looks, accuracy is whether it tells the truth, and "
"calibration is its conscience - the regular confession against a higher "
"standard. The Signature builder calibrates on schedule, because an "
"uncalibrated sensor is not a sensor at all; it is a rumor with a "
"display."),
},
{
"key": "servos",
"name": "Servo Motors and Drives: Closing the Loop on Motion",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"A servo is not a kind of motor - it is a motor married to a sensor and a "
"controller that refuses to be wrong. An encoder watches the shaft; the "
"drive compares the actual position with the commanded position thousands "
"of times per second and pours current into the motor to erase the error. "
"The result is motion with authority: a servo holds position against "
"disturbance, follows trajectories at speed, and reports exactly where it "
"is. The controller is usually PID - proportional pushes harder the larger "
"the error, integral eliminates the lingering offset, derivative brakes "
"against velocity to prevent overshoot. Take a small servo with inertia "
"0.001 kg m2 and damping 0.02: with Kp=5 and Kd=0.5 the loop is overdamped "
"(damping ratio 3.68), glides to a 1.0-radian command with no overshoot, "
"and settles inside 2 seconds with zero steady-state error. Hobby servos "
"package motor, gears, potentiometer, and driver into one ten-dollar box; "
"industrial servos pair brushless motors with high-resolution encoders and "
"drives that switch tens of amps. Whenever position must be right - robot "
"joints, CNC axes, camera gimbals - the servo is the answer."),
"how_it_works": (
"The loop runs in three repeating steps: measure, compare, correct. The "
"encoder reports shaft angle theta; the controller computes the error "
"e = theta_desired - theta and its derivative; the control law "
"u = Kp e + Ki integral(e) + Kd de/dt produces a current (torque) command; "
"the power stage - an H-bridge or three-phase inverter - delivers it. "
"Proportional gain sets stiffness: double Kp and the servo fights "
"disturbance twice as hard, but too much Kp with too little damping makes "
"it oscillate. Integral gain eats steady-state error from friction and "
"gravity but can wind up during saturation, so drives clamp it. Derivative "
"gain adds electronic damping - it resists velocity, killing overshoot. "
"Tuning is the craft: start with Kp for response, add Kd for calm, add Ki "
"for exactness. Feedforward goes further, commanding the torque the "
"trajectory needs before the error even appears. The drive also protects: "
"current limits guard the windings, following-error limits fault if the "
"encoder and command ever disagree badly - the servo would rather stop "
"than lie."),
"key_points": [
"A servo is motor + position sensor + controller in a fast error-erasing loop.",
"PID: proportional pushes with error, integral kills offset, derivative brakes velocity.",
"A PD servo (J=0.001, Kp=5, Kd=0.5) is overdamped and settles to 1.0 rad with zero steady error.",
"Too much Kp oscillates; integral winds up in saturation; derivative adds damping.",
"Feedforward commands expected torque before error appears.",
"Following-error limits make the servo fault rather than silently lie about position.",
],
"requirements": [
"The DC motor, torque/speed, and encoder records.",
"Basic calculus intuition (derivatives, integrals).",
"A calculator for the loop exercises in the demo.",
],
"standards": [
"IEC 61800 series covers adjustable-speed servo drive safety and EMC.",
"ISO 13849 governs safety-related control parts (safe torque off).",
"NEMA ICS 16 / IEC 60034 apply to the motor itself.",
],
"citations": [C_OGATA, C_BOLTON, C_BISHOP],
"sig_lens": (
"Signature take: the servo is the first actuator with a conscience. An "
"open-loop motor hopes; a servo knows - it watches its own shaft and "
"refuses the gap between command and reality. That refusal, executed "
"thousands of times a second, is the smallest possible unit of "
"responsibility. The Signature machine is built from such refusals, "
"layered until the whole system would rather stop than be wrong."),
},
{
"key": "transmissions",
"name": "Gearboxes, Leadscrews, and Ballscrews: Trading Speed for Force",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"Motors spin fast and weak; machines usually need slow and strong. "
"Mechanical transmissions trade between the two, conserving power minus "
"friction. A gearbox multiplies torque by its ratio and divides speed by "
"the same: a 0.4 N m motor at 3000 rpm through a 20:1 box at 85 percent "
"efficiency delivers 6.8 N m at 150 rpm. A leadscrew or ballscrew then "
"converts rotation into linear thrust: force equals 2 pi times torque "
"times efficiency divided by the lead, so that 6.8 N m through a 5 mm "
"lead ballscrew at 90 percent efficiency pushes with 7.69 kilonewtons "
"while advancing 12.5 mm per second. Ballscrews roll on recirculating "
"balls (90 percent efficient, precise, expensive); plain leadscrews slide "
"(30-50 percent efficient, self-locking, cheap). Gears add backlash - the "
"tiny dead zone when direction reverses - which precision designs kill "
"with preloaded or split gears, harmonic drives, or direct drive. Belts "
"and chains do the same trade over distance. Every transmission is a deal "
"with friction: count its efficiency in the torque budget or the machine "
"will be weaker than the math promised."),
"how_it_works": (
"Power conservation rules every stage: torque out equals torque in times "
"ratio times efficiency, speed out equals speed in divided by ratio. Spur "
"and helical gears mesh teeth; planetary boxes nest gears for high ratio "
"in a small can; worm gears give huge single-stage ratios but waste half "
"the power as heat and usually cannot be back-driven. Harmonic (strain "
"wave) drives flex a thin spline to get 100:1 with near-zero backlash for "
"robot joints. Screws are inclined planes wrapped around a shaft: one "
"turn advances the nut by the lead, so thrust is torque amplified by "
"2 pi / lead - a 5 mm lead turns modest torque into kilonewtons. "
"Efficiency decides reversibility: below 50 percent the screw self-locks "
"and holds load with no power (a feature for lifts, a hazard for "
"back-driving). Backlash - gear tooth clearance plus nut clearance - is "
"measured in arc-minutes or micrometres and compensated in software or "
"eliminated in hardware."),
"key_points": [
"Gearbox: torque x ratio x efficiency; speed / ratio. 0.4 N m at 3000 rpm -> 6.8 N m at 150 rpm through 20:1 at 85%.",
"Ballscrew: F = 2 pi x tau x eff / lead; 6.8 N m, 5 mm lead, 90% -> 7.69 kN at 12.5 mm/s.",
"Ballscrews roll (90% efficient, precise); plain screws slide (30-50%, self-locking, cheap).",
"Backlash is the dead zone on reversal - kill it with preload, harmonic drives, or software.",
"Worm gears give huge ratios but waste power and usually cannot be back-driven.",
"Count every stage's efficiency in the torque budget.",
],
"requirements": [
"The torque/speed/power record.",
"Torque, force, and lead (mm per revolution).",
"A calculator for the transmission exercises in the demo.",
],
"standards": [
"AGMA 2001-D04 rates gear tooth pitting and bending strength.",
"ISO 3408 defines ballscrew accuracy grades and ratings.",
"ISO 1328 classifies gear accuracy (backlash-relevant).",
],
"citations": [C_BISHOP, C_BOLTON, C_OGATA],
"sig_lens": (
"Signature take: the transmission is the negotiator between what the "
"motor wants and what the load needs. The motor wants to spin; the load "
"wants to be shoved. Gears, screws, and belts translate - and every "
"translation takes its fee in friction. The Signature builder pays the "
"fee on paper before paying it in metal, because a machine that is "
"weaker than its math is a promise broken at commissioning."),
},
{
"key": "solenoids",
"name": "Solenoids and Contactors: The Electromagnetic Push and Pull",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"A solenoid is the simplest electric actuator: a coil of wire that becomes "
"a magnet when current flows and yanks an iron plunger into itself. Force "
"rises with the square of the ampere-turns and falls with the square of "
"the air gap - so a 500-turn coil at 2 amps (1000 ampere-turns) across a "
"2 mm gap on a 10 mm bore pulls about 12.3 newtons, but at 4 mm the same "
"coil manages barely a quarter of that. That violent gap dependence is "
"the solenoid's character: huge force at the end of the stroke, weak at "
"the start, and strictly on-or-off - there is no proportional middle. "
"They switch valves, fire dot-matrix pins, lock doors, and throw "
"contactors, usually in milliseconds: a 10 mH coil on 6 ohms reaches full "
"current in about 1.7 milliseconds (the L/R time constant). Relays and "
"contactors are solenoids with electrical contacts attached - small "
"current in the coil switches big current in the load. Mind the heat: "
"24 watts in a small coil is fine for a one-second punch but will cook it "
"if held forever; datasheets rate duty cycle for exactly this reason."),
"how_it_works": (
"Magnetic circuits obey the same math as electric ones: ampere-turns are "
"the voltage, flux is the current, and the air gap is the dominant "
"resistance (reluctance). Closing the gap lowers the reluctance, so the "
"system pulls the plunger in to minimize its magnetic energy - force is "
"the spatial derivative of that energy, giving F proportional to "
"(NI)^2 x area / gap^2. A return spring pushes the plunger back out when "
"the coil de-energizes. The coil is an inductor: current rises as "
"I(t) = V/R x (1 - e^(-tR/L)), so the L/R time constant sets the pull-in "
"speed, and on switch-off the collapsing field generates a voltage spike "
"(L di/dt) that must be clamped with a flyback diode or the driver dies. "
"AC solenoids add a shading ring to stop 50/60 Hz buzz. Proportional "
"solenoids shape the pole piece into a cone so force stays roughly flat "
"over the stroke, giving hydraulic valves their metering control."),
"key_points": [
"Force scales with (ampere-turns)^2 / gap^2: 500 turns at 2 A, 2 mm gap, 10 mm bore -> ~12.3 N.",
"Huge force at end of stroke, weak at start - strictly on/off, no proportional middle.",
"Current rises with time constant L/R: 10 mH on 6 ohms -> ~1.7 ms to pull in.",
"Switch-off generates a voltage spike - clamp it with a flyback diode.",
"Relays and contactors are solenoids with power contacts: small coil current switches big load current.",
"Duty cycle matters: 24 W is fine for a punch, fatal held continuously.",
],
"requirements": [
"The DC motor record (electromagnetism basics).",
"Inductor behavior: current cannot change instantly.",
"A calculator for the force exercises in the demo.",
],
"standards": [
"IEC 60947-4-1 and -5-1 cover contactors and control-circuit devices.",
"UL 508 / CSA C22.2 No. 14 cover industrial control equipment.",
"IEC 61000-4-4 addresses the switching transients solenoids create.",
],
"citations": [C_BOLTON, C_BISHOP, C_ESPOSITO],
"sig_lens": (
"Signature take: the solenoid is the binary soul of actuation - on or "
"off, in or out, no maybes. It does not modulate; it commits. That "
"commitment, squared with the gap, is why solenoids punch far above their "
"size at the end of the stroke. The Signature builder uses the solenoid "
"where decisions are binary and speed is everything - and reaches for a "
"proportional muscle everywhere else."),
},
{
"key": "voice_coils",
"name": "Voice Coils and Linear Motors: Force Without Gears",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Some jobs need pure linear push with no gears, no screws, no backlash - "
"just force, now. The voice coil delivers: a coil of wire sitting in a "
"radial magnetic field feels F = B x l x I, force equals flux density "
"times wire length times current, perfectly linear. A speaker is a voice "
"coil: with B = 0.5 tesla, 10 metres of wire, and 2 amps, the coil pushes "
"with 10 newtons, and on a 20-gram cone at 50 Hz that is 5.07 mm of "
"excursion - sound itself. Scale it up and the voice coil becomes the "
"linear motor: flat or tubular motors that drive pick-and-place heads, "
"wafer stages, and maglev shuttles directly. A linear motor with a force "
"constant of 25 N/A at 3 amps makes 75 newtons and accelerates a 2 kg "
"stage at 37.5 m/s2 - with zero backlash, zero wear, and stiffness set "
"entirely by the servo loop. The price is continuous current: holding "
"force against gravity means heating the coils forever, so voice coils "
"love short strokes and light loads, and linear motors love counterbalance "
"or horizontal axes."),
"how_it_works": (
"The Lorentz force does the work: each metre of current-carrying wire "
"crossing the magnetic field contributes B x I newtons, and the coil sums "
"them. In a speaker the coil is cylindrical in an annular magnet gap; the "
"suspension spring centers it and the cone radiates sound. In a linear "
"motor the rotary motor is conceptually unrolled: magnets form a track, "
"coils form the forcer, and the same three-phase commutation as a brushless "
"motor - now with a linear encoder instead of a rotary one - sequences the "
"phases as the forcer glides. Iron-core versions pull harder but cog "
"against the magnets (cogging force ripple); ironless versions glide "
"perfectly smooth at lower force. Heat is the limit: force needs current, "
"current squared times resistance is heat, and the coils must dump it - "
"water cooling appears on serious stages. Position feedback closes the "
"loop exactly like a rotary servo."),
"key_points": [
"F = B x l x I, perfectly linear: 0.5 T, 10 m wire, 2 A -> 10 N.",
"A 20 g speaker cone at 50 Hz moves 5.07 mm - that motion is sound.",
"Linear motors (25 N/A at 3 A -> 75 N) accelerate a 2 kg stage at 37.5 m/s2 with zero backlash.",
"No gears, no screws, no wear - stiffness comes from the servo loop alone.",
"Iron-core cogs; ironless glides smooth at lower force.",
"Holding force costs continuous current and heat - voice coils love short strokes.",
],
"requirements": [
"The DC motor and servo records (Lorentz force, closed loop).",
"Linear encoders (see the position sensor record).",
"A calculator for the force exercises in the demo.",
],
"standards": [
"IEC 60034 applies to linear motors as rotating-machine derivatives.",
"ISO 230 series tests the resulting linear axes.",
"IEEE 2700-2017 covers the linear encoders that close the loop.",
],
"citations": [C_BISHOP, C_BOLTON, C_NYCE],
"sig_lens": (
"Signature take: the voice coil is the most honest force in the catalog - "
"current in, newtons out, no translation, no negotiation. Where gears "
"bargain and screws compromise, the coil simply pushes in direct "
"proportion. The Signature builder pays for that honesty in copper heat "
"and holds it for the moments that matter: the focus pull, the wafer "
"step, the note."),
},
{
"key": "hydraulics",
"name": "Hydraulic Actuators: Huge Force from Pressurized Oil",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"When the force needed dwarfs what motors can give in the space allowed, "
"engineers reach for oil. A hydraulic cylinder is a piston in a barrel: "
"pump oil into one side at 160 bar and a 63 mm bore pushes with 49.9 "
"kilonewtons - five tonnes - from a cylinder you can lift with one hand. "
"The rod side pulls less because the rod steals area: with a 36 mm rod "
"the same cylinder retracts with 33.6 kN. Speed is set by flow: 20 litres "
"per minute into that bore extends the rod at 106.9 mm/s, and pressure "
"times flow is power - 5.33 kilowatts of it. Oil barely compresses, so "
"hydraulics are stiff and precise under load; the same oil lubricates, "
"cools, and carries away contamination to the filters. The system needs a "
"pump, a reservoir, valves, hoses, and coolers - plumbing with attitude - "
"and it demands respect: 160 bar will inject oil through skin, a burst "
"hose whips, and leaks are both a mess and a fire risk. Excavators, "
"presses, aircraft flight controls, and injection moulders all run on "
"this bargain: accept the plumbing, get force density nothing else "
"touches."),
"how_it_works": (
"Force equals pressure times effective area; speed equals flow divided by "
"area; power equals pressure times flow. A variable-displacement pump sets "
"system pressure (relief valves cap it for safety); proportional or servo "
"valves meter flow to each actuator, giving smooth speed and position "
"control; the cylinder converts it back to force and motion. Double-acting "
"cylinders power both directions; single-acting cylinders push and let "
"gravity or a spring return. Accumulators - gas-charged bottles - store "
"pressure energy to smooth pulsations and survive pump pauses. Because oil "
"is nearly incompressible, a trapped volume is a stiff spring: position "
"holds under load and servo valves achieve remarkable precision. The "
"enemies are contamination (a 10-micron particle scores a servo valve "
"spool, hence fine filtration and ISO cleanliness codes), heat (every "
"watt of loss warms the oil, hence coolers), and air entrainment (bubbles "
"make the stiff oil spongy). Seal friction causes stick-slip at low "
"speed - the classic hydraulic judder."),
"key_points": [
"63 mm bore at 160 bar pushes 49.9 kN; the 36 mm rod side pulls 33.6 kN.",
"20 L/min extends that cylinder at 106.9 mm/s; pressure x flow = 5.33 kW.",
"Oil barely compresses: stiff, precise under load, and self-lubricating.",
"Valves meter flow for speed; relief valves cap pressure for safety.",
"Enemies: contamination (filters, ISO codes), heat (coolers), air bubbles, seal stick-slip.",
"160 bar demands respect: injection injury, burst hoses, leak fire risk.",
],
"requirements": [
"The energy families record (fluid power basics).",
"Pressure x area = force; flow / area = speed.",
"A calculator for the cylinder exercises in the demo.",
],
"standards": [
"ISO 4413 sets hydraulic system safety rules.",
"ISO 4406 codes fluid cleanliness (particles per ml).",
"ISO 6020/6022 standardize cylinder mounting dimensions.",
],
"citations": [C_ESPOSITO, C_BISHOP, C_BOLTON],
"sig_lens": (
"Signature take: hydraulics is strength without apology. Where electric "
"muscle calculates and pneumatic muscle hurries, oil simply does not "
"yield - five tonnes from a hand-sized cylinder, stiff as a held breath. "
"The Signature builder treats hydraulics like heavy weather: harnessed "
"with relief valves, filtration, and respect, it moves mountains; "
"neglected, it reminds you that pressure is stored violence."),
},
{
"key": "pneumatics",
"name": "Pneumatic Actuators: Fast Muscle from Compressed Air",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Compressed air is the cheapest muscle in the factory: a compressor in "
"the corner, plastic tubing everywhere, and cylinders that slam back and "
"forth millions of times. A 50 mm bore cylinder at 6 bar pushes with "
"1.18 kilonewtons - modest next to hydraulics, but plenty for pick-and-"
"place, clamping, sorting, and packaging at blinding speed. Air is free "
"and exhaust is just air, so pneumatics are clean enough for food plants; "
"and because air compresses, cylinders are naturally compliant - they give "
"instead of breaking when they meet resistance. The springiness is also "
"the weakness: precise positioning fights the air spring, so pneumatics "
"rule bang-bang motion between hard stops and cede fine positioning to "
"electrics. Air is not free to make: each 100 mm stroke of that 50 mm "
"cylinder drinks 1.37 standard litres per side, so 60 double-acting "
"cycles a minute consume about 165 normal litres per minute - and the "
"compressor's electricity bill is the real cost of 'free' air. Size the "
"valve and tubing for flow: 100 Nl/min through that bore means 0.85 m/s, "
"fast enough to need cushioning at the ends."),
"how_it_works": (
"Force equals pressure times area, same as hydraulics, but the working "
"fluid is compressible air at 4-8 bar. Directional valves (5/2, 5/3) route "
"air to either side of the piston; flow-control valves (needle "
"restrictions) meter the exhaust to set speed - meter-out control gives "
"the smoothest motion because the exhaust restriction back-pressures the "
"cylinder. End cushioning - adjustable air pockets at stroke ends - "
"decelerates the piston so it does not hammer the end caps at 1 m/s. "
"FRL units (filter, regulator, lubricator) prepare the air: water is "
"drained, pressure is regulated, and a mist of oil keeps seals alive "
"(many modern cylinders run oil-free). Because air compresses, a "
"cylinder mid-stroke is a spring whose stiffness rises with pressure - "
"great for gentle handling, poor for holding position against varying "
"load. Vacuum cups use the same physics in reverse: -0.6 bar under a "
"100 mm cup lifts about 470 N - the gripper of choice for sheets, boxes, "
"and circuit boards."),
"key_points": [
"50 mm bore at 6 bar gives 1.18 kN - fast, cheap, clean, compliant.",
"Air compresses: naturally gentle, but fights precise positioning.",
"100 mm stroke drinks 1.37 std litres per side; 60 double-acting cycles/min -> ~165 Nl/min.",
"100 Nl/min through a 50 mm bore = 0.85 m/s - cushion the stroke ends.",
"Meter-out flow controls give the smoothest speed; FRL units prepare the air.",
"Vacuum cups grip with the same physics in reverse.",
],
"requirements": [
"The energy families and hydraulics records.",
"Standard litres vs actual litres at pressure.",
"A calculator for the air-consumption exercises in the demo.",
],
"standards": [
"ISO 4414 sets pneumatic system safety rules.",
"ISO 6430/6431/15552 standardize cylinder dimensions and mounting.",
"ISO 8573-1 classes compressed-air purity (particles, water, oil).",
],
"citations": [C_ESPOSITO, C_BISHOP, C_BOLTON],
"sig_lens": (
"Signature take: pneumatics is the cheerful muscle - fast, cheap, "
"forgiving, everywhere. It does not pretend to precision; it promises "
"speed and keeps it a million cycles a day. The Signature builder loves "
"air for what it is and never asks it to be what it is not: between two "
"hard stops, nothing beats it; asked to hold a micrometre, it laughs and "
"hands you a servo."),
},
{
"key": "piezo",
"name": "Piezoelectric Actuators: Crystal Precision for Tiny Moves",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Some crystals strain when electrified - squeeze a quartz crystal and it "
"makes voltage; apply voltage and it strains. Piezoelectric actuators "
"exploit the second half: stack a hundred thin ceramic layers, apply "
"100 volts, and the stack grows by 5 micrometres with sub-nanometre "
"repeatability. A 50 mm stack of PZT ceramic (d33 = 500 picometres per "
"volt) with 100 layers of 0.5 mm each strains 100 microstrain at "
"200 kV/m field - 5 um of free motion - and with a stiffness of "
"100 MN/m it pushes 500 newtons blocked. That combination - nanometre "
"resolution, kilonewton-capable force, millisecond response - runs "
"scanning tunnelling microscopes, fuel injectors, adaptive optics, and "
"ultrasonic welders. The limits are honest: 5 um is the whole stroke "
"(levers amplify it at the cost of force), the ceramic is brittle and "
"hates tension, hysteresis loops 10-15 percent (charge control or "
"feedback linearizes it), and heat plus high field depolarize the "
"ceramic. Piezo is the actuator of last resort for small and first "
"resort for precise."),
"how_it_works": (
"Apply an electric field E to a poled ferroelectric ceramic and it strains "
"by S = d x E, where d is the piezoelectric coefficient matrix; the 33 "
"mode (field along the poling axis) gives the biggest strain. Stacking N "
"thin layers multiplies the displacement by N while keeping the drive "
"voltage low - each layer sees the full voltage across a thin gap, so "
"field is high while voltage stays near 100 V. The stack is a very stiff "
"spring: free displacement times stiffness equals blocked force, and any "
"real load gets something in between along the load line. Hysteresis "
"comes from ferroelectric domain-wall motion; driving with charge instead "
"of voltage straightens the curve because charge tracks polarization "
"better than voltage does. Bimorph benders glue two piezo layers to a "
"shim so one side's expansion bends the strip - millimetres of motion at "
"millinewtons of force. Resonance turns the same stack into an ultrasonic "
"motor or a loudspeaker tweeter."),
"key_points": [
"Strain = d33 x field: 500 pm/V at 200 kV/m -> 100 microstrain.",
"100-layer, 50 mm PZT stack at 100 V: 5 um free displacement, 500 N blocked force.",
"Nanometre repeatability, millisecond response - the precision actuator.",
"Stroke is micrometres (lever-amplify at the cost of force); ceramic hates tension.",
"Hysteresis 10-15% - linearize with charge drive or position feedback.",
"Heat and over-field depolarize the ceramic permanently.",
],
"requirements": [
"The smart-materials notion from the energy families record.",
"Electric field = voltage / thickness.",
"A calculator for the stack exercises in the demo.",
],
"standards": [
"ANSI/IEEE Std 176-1987 standardizes piezoelectric terminology and coefficients.",
"IEEE 2700-2017 covers piezo-based sensors built from the same ceramics.",
"Manufacturer derating curves govern field, temperature, and tension limits.",
],
"citations": [C_IEEE176, C_JANOCHA, C_FRADEN],
"sig_lens": (
"Signature take: the piezo crystal is patience made material - it moves "
"five micrometres and means every nanometre of it. Where other actuators "
"shout across millimetres, the crystal whispers and the microscope "
"listens. The Signature builder calls on piezo when the job is too fine "
"for muscle: the mirror that must tilt by light-waves, the probe that "
"must touch one atom. Small, certain, absolute."),
},
{
"key": "sma",
"name": "Shape-Memory Alloys: Metal That Remembers Its Shape",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Heat a bent paperclip of nitinol - nickel-titanium - and it snaps back "
"to its remembered shape with startling force. That is the shape-memory "
"effect: below its transformation temperature the alloy deforms easily in "
"its martensite phase; heated above it, the crystal shifts to austenite "
"and every atom marches back to the memorized geometry, exerting up to "
"200 MPa of recovery stress. A 0.5 mm nitinol wire pulls 39.3 newtons and "
"recovers 4 percent strain - 4 mm on a 100 mm wire - enough to close a "
"valve, deploy an antenna, or straighten a medical stent inside an artery. "
"Heating is fast and easy - run current through the wire itself: 5 watts "
"heats that 100 mm wire through its 50 K transformation in about 0.63 "
"seconds. Cooling is the bottleneck - the wire must shed heat to the air, "
"so cycle rates are hertz at best without forced cooling. Stents, "
"orthodontic wires, eyeglass frames, and deployable space structures all "
"exploit the same trick: enormous work from a silent, solid-state muscle "
"with no gears and no noise, paid for in heat and patience."),
"how_it_works": (
"Two crystal phases do the work. In cool martensite the lattice is soft "
"and twinned - it deforms up to 6-8 percent by detwinning with modest "
"stress. Heat past the austenite-start temperature and the lattice "
"snaps to cubic austenite, recovering the memorized shape and generating "
"recovery stress up to 200-600 MPa if constrained. The temperatures "
"(Mf, Ms, As, Af) are tuned by alloy composition and heat treatment - "
"body-temperature Af makes stents deploy inside arteries. Superelastic "
"nitinol works above Af: stress alone induces martensite, which snaps "
"back when unloaded - the springiness of orthodontic wires and "
"kink-resistant guidewires. Training - repeated thermal cycling under "
"load - teaches two-way memory (both shapes remembered). Fatigue is the "
"design limit: millions of small-strain cycles are fine, thousands of "
"full-strain cycles crack the wire - keep working strain under 2-3 "
"percent for long life."),
"key_points": [
"Nitinol heated past its transformation snaps back to its memorized shape at up to 200 MPa.",
"0.5 mm wire: 39.3 N recovery force, 4% strain = 4 mm on a 100 mm wire.",
"Heat with its own resistance: 5 W transforms it in ~0.63 s; cooling limits cycle rate.",
"Superelastic nitinol (above Af) springs back from stress alone - stents, guidewires, braces.",
"Tune transformation temperatures by alloy and heat treatment.",
"Keep working strain under 2-3% for fatigue life; full-strain cycling cracks it.",
],
"requirements": [
"The smart-materials notion from the energy families record.",
"Stress, strain, and resistive heating.",
"A calculator for the wire exercises in the demo.",
],
"standards": [
"ASTM F2063 covers wrought nickel-titanium for medical devices.",
"ASTM F2005 defines nitinol terminology.",
"ISO 10993 governs biocompatibility of implant applications.",
],
"citations": [C_LAGOUDAS, C_JANOCHA, C_BISHOP],
"sig_lens": (
"Signature take: nitinol is the metal with a memory and a will - bend it "
"cold and it forgives you; warm it and it insists on who it was. No "
"motor, no gears, no noise: just heat, patience, and thirty-nine "
"newtons from a wire thinner than a pencil lead. The Signature builder "
"uses it where silence matters and waiting is allowed - the stent that "
"blooms inside a heart, the antenna that unfolds a million miles from "
"home."),
},
{
"key": "magnetostrictive",
"name": "Magnetostrictive Actuators: Giant Magnetism, Tiny Stretch",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Some materials stretch in a magnetic field - and Terfenol-D, a "
"terbium-iron alloy, stretches more than anything else known: 1600 parts "
"per million. A 100 mm Terfenol-D rod in a solenoid grows 160 micrometres "
"when the field hits saturation - a giant strain for a magnetic effect, "
"hence 'giant magnetostriction'. With a modulus of 30 GPa on a 1 cm2 rod "
"the stiffness is 30 MN/m, so that 160 um of free motion becomes 4800 "
"newtons blocked - piezo-like precision with hydraulic-like force, "
"responding in microseconds to kilohertz. Sonar projectors, active "
"vibration cancellers, fuel injectors, and high-force micropositioners "
"use it. The price: the rod needs a magnetic bias (permanent magnets), a "
"prestress bolt (it performs best squeezed), and a solenoid big enough to "
"drive it - plus Terfenol-D is brittle and eye-wateringly expensive. "
"Magnetostrictive actuators live where the budget allows and nothing else "
"combines this force, this speed, and this resolution."),
"how_it_works": (
"Magnetic domains rotate toward the applied field, and in highly "
"magnetostrictive alloys the crystal lattice distorts with them - strain "
"follows the square of magnetization at low fields, saturating at lambda_s "
"(1600 ppm for Terfenol-D). A solenoid around the rod provides the drive "
"field; permanent magnets add a DC bias so the AC drive works on the "
"steep, linear part of the curve instead of the quadratic bottom (which "
"would double the frequency). A prestress bolt squeezes the rod to ~10-20 "
"MPa, maximizing coupling and keeping the brittle rod in compression "
"where it is strong. The rod pushes a load through the load line like a "
"piezo stack: free strain times stiffness is the blocked force. Eddy "
"currents in the solid rod limit high-frequency response, so rods are "
"laminated or slotted for kilohertz work. Drive electronics are current "
"sources - field follows current - and position feedback linearizes the "
"remaining hysteresis."),
"key_points": [
"Terfenol-D: 1600 ppm giant magnetostriction - a 100 mm rod stretches 160 um.",
"30 GPa modulus on 1 cm2 -> 30 MN/m stiffness -> 4800 N blocked force.",
"Piezo-like precision with hydraulic-like force, responding to kilohertz.",
"Needs magnetic bias (linearizes), prestress (keeps brittle rod in compression), and a drive solenoid.",
"Brittle and expensive - used where nothing else combines force, speed, and resolution.",
"Laminate or slot the rod to beat eddy currents at high frequency.",
],
"requirements": [
"The piezoelectric actuator record (load lines, blocked force).",
"Magnetic field from a solenoid.",
"A calculator for the rod exercises in the demo.",
],
"standards": [
"Manufacturer specifications govern bias, prestress, and drive limits (no single universal standard).",
"IEEE 2700-2017 covers magnetostrictive position sensors (the reciprocal device).",
"ASTM material specs apply to the housing and prestress mechanics.",
],
"citations": [C_CLARK, C_JANOCHA, C_BISHOP],
"sig_lens": (
"Signature take: Terfenol-D is the aristocrat of muscles - rare, "
"expensive, brittle, and utterly unmatched at what it does. Sixteen "
"hundred parts per million of stretch from pure magnetism, four thousand "
"eight hundred newtons from a finger-sized rod. The Signature builder "
"does not spend this muscle casually; it is reserved for the instruments "
"where force, speed, and fineness must arrive together or not at all."),
},
{
"key": "encoders",
"name": "Position Sensors: Encoders and Resolvers That Count Rotation",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"A servo is blind without position feedback, and the encoder is its eyes. "
"An incremental optical encoder shines light through a slotted disk: 1024 "
"slots give 1024 pulses per revolution, and reading both edges of the two "
"quadrature channels multiplies that by four - 4096 counts per rev, "
"0.0879 degrees per count. At 3000 rpm the controller must swallow "
"204800 counts per second, and velocity comes free: 4096 counts in "
"10 milliseconds means exactly one revolution per 10 ms - 6000 rpm. "
"Quadrature also gives direction: channel A leading B means forward, "
"lagging means reverse. Absolute encoders skip the homing dance - a "
"12-bit absolute encoder reports one of 4096 unique positions the instant "
"power returns. Resolvers do the same job in hell: a rotating transformer "
"whose sine/cosine windings report angle through heat, oil, and vibration "
"that would kill glass disks - the feedback of choice for EV motors and "
"aerospace. Linear encoders read glass or steel scales for direct "
"position, immune to screw backlash. Choose incremental for cost, "
"absolute for power-loss safety, resolvers for harshness."),
"how_it_works": (
"Optical encoders pattern a disk with alternating clear and opaque lines; "
"an LED and photodetector pair turns the passing lines into square waves, "
"and two tracks offset by a quarter period give quadrature - direction "
"from phase order, 4x resolution from edge counting. A once-per-rev index "
"pulse marks a home reference. Absolute encoders pattern the disk with a "
"Gray code - each angular position has a unique bit pattern read by an "
"array of detectors, so position is known at power-up with no motion. "
"Magnetic encoders replace optics with Hall sensors reading a multipole "
"magnet ring: tougher, cheaper, slightly less precise. Resolvers are "
"rotating transformers: excite the rotor winding with AC, and the two "
"stator windings output sine and cosine of the shaft angle - a "
"resolver-to-digital converter computes the arctangent. Capacitive and "
"inductive encoders read patterned PCBs for compact, robust feedback. "
"Resolution is counts per rev; accuracy is how true each count is - the "
"two are different numbers and datasheets list both."),
"key_points": [
"1024-line quadrature encoder -> 4096 counts/rev -> 0.0879 deg per count.",
"3000 rpm produces 204800 counts/s; 4096 counts in 10 ms = 6000 rpm exactly.",
"Quadrature phase order gives direction for free.",
"Absolute encoders (12-bit = 4096 unique positions) know position at power-up - no homing.",
"Resolvers are rotating transformers that survive heat, oil, and vibration.",
"Resolution (counts) and accuracy (truth of each count) are different numbers.",
],
"requirements": [
"The servo record (why feedback matters).",
"Frequency = counts per second; rpm conversion.",
"A calculator for the encoder exercises in the demo.",
],
"standards": [
"IEEE 2700-2017 standardizes position sensor performance specs.",
"EnDat, BiSS, and SSI are open absolute-encoder interface protocols.",
"ISO 230-2 tests the positioning accuracy of encoder-guided axes.",
],
"citations": [C_NYCE, C_FRADEN, C_BISHOP],
"sig_lens": (
"Signature take: the encoder is the machine's proprioception - its sense "
"of where its own limbs are. Without it, every servo is a sleepwalker, "
"confident and lost. Four thousand ninety-six counts per revolution is "
"four thousand ninety-six small honesties per turn. The Signature builder "
"never commands motion it cannot witness; the encoder is the witness."),
},
{
"key": "force_sensors",
"name": "Force, Torque, and Strain: Weighing and Feeling the Load",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Force is felt through deformation: stretch a metal, its electrical "
"resistance changes, and the strain gauge turns that whisper into a "
"signal. Bond four gauges into a Wheatstone bridge on a carefully shaped "
"spring element and you have a load cell. The math is small and exact: "
"with a gauge factor of 2.0, a strain of 1000 microstrain changes each "
"350-ohm gauge by 0.2 percent, and a quarter-bridge on 5 volts excitation "
"outputs 2.5 millivolts. A 100 kg load cell with 2 mV/V sensitivity gives "
"10 mV at full scale on 5 V - so a reading of 8.2 mV means 82 kg, "
"linearly, repeatably. Torque sensors do the same on a twisting shaft; "
"multi-axis force/torque sensors stack gauged flexures to report Fx, Fy, "
"Fz and the three moments - the wrists of assembly robots. Piezoelectric "
"force washers catch fast impacts a strain gauge is too slow to see; "
"capacitive and optical load cells serve where gauges cannot go. Every "
"weighing scale, every crash-test dummy, every robot grip that knows not "
"to crush the egg - all strain gauges, all bridges, all millivolts made "
"meaningful by calibration."),
"how_it_works": (
"Stretch a conductor and it gets longer and thinner - resistance rises by "
"gauge factor times strain (GF ~2.0 for foil gauges, ~100+ for "
"semiconductor gauges). The Wheatstone bridge turns that fractional "
"resistance change into a voltage: with one active gauge (quarter "
"bridge) Vout = Vex x GF x strain / 4; four active gauges (full bridge) "
"quadruple the signal and cancel temperature drift, since all four warm "
"together. The spring element - a beam, column, or shear web machined "
"from tool steel or aluminium - concentrates the load's strain exactly "
"where the gauges sit, and its stiffness sets the trade between "
"sensitivity and overload survival. An instrumentation amplifier boosts "
"millivolts to volts; calibration against deadweights maps volts to "
"newtons. Temperature compensation - matched gauges, bridge symmetry, "
"and sometimes a thermistor - keeps the zero from wandering. Torque "
"flanges put gauges at 45 degrees to the shaft axis where torsional shear "
"is maximal."),
"key_points": [
"Strain gauge: resistance changes with stretch; GF ~2.0 for foil, ~100+ for semiconductor.",
"Quarter bridge (GF=2, 1000 ue, 5 V) outputs exactly 2.5 mV.",
"2 mV/V load cell on 5 V: 8.2 mV reading = 82 kg on a 100 kg cell.",
"Full bridges quadruple signal and cancel temperature drift.",
"Multi-axis sensors report 3 forces + 3 moments - the robot's wrist.",
"Piezo washers catch fast impacts; calibration against deadweights makes millivolts honest.",
],
"requirements": [
"The measurement truth record (calibration, accuracy).",
"Wheatstone bridge basics.",
"A calculator for the bridge exercises in the demo.",
],
"standards": [
"ASTM E4 verifies force calibration of testing machines.",
"ISO 376 calibrates force-proving instruments.",
"OIML R60 governs load cells for legal weighing.",
],
"citations": [C_FRADEN, C_DUNN, C_JOHNSON],
"sig_lens": (
"Signature take: the load cell is the machine's sense of effort - the "
"difference between touching and crushing. Eighty-two kilograms read "
"from eight point two millivolts: that is the whole discipline in one "
"sentence, a whisper amplified into certainty. The Signature grip is "
"never stronger than it needs to be, because it always knows exactly "
"how strong it is being."),
},
{
"key": "pressure_sensors",
"name": "Pressure Sensors: Feeling the Push of Fluids",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Pressure is force per area, and the pressure sensor feels it with a "
"diaphragm - a thin membrane that flexes under the fluid and reports the "
"flex. Piezoresistive sensors diffuse strain gauges into a silicon "
"diaphragm: micrometres of bow become millivolts of bridge output, "
"conditioned on-chip into the industrial standard 4-20 mA loop, where "
"4 mA means zero and 20 mA means full scale. A 0-10 bar transmitter at "
"6 bar sources 13.6 mA - drop it across the standard 250-ohm resistor "
"and the controller reads 3.40 volts. The 4 mA live-zero is genius: "
"0 mA means a broken wire, not zero pressure. Capacitive sensors watch "
"the diaphragm bow change a capacitance - superb for low pressures; "
"piezoelectric sensors catch fast pressure spikes in engines. Gauge "
"sensors reference the atmosphere, absolute sensors reference vacuum, "
"differential sensors read the difference - pick wrong and the number "
"lies by a whole atmosphere. Ten metres of water column is 0.981 bar: "
"that is the hydrostatic intuition behind every depth gauge, tank level, "
"and barometer ever built."),
"how_it_works": (
"A diaphragm clamped at its rim bows under pressure; the bow is "
"proportional to pressure at small deflections (plate theory), and "
"strain gauges at the rim's high-stress ring convert bow to resistance "
"change. Silicon piezoresistive diaphragms are etched from wafers with "
"the bridge diffused in - tiny, cheap, and sensitive. The on-chip "
"conditioner amplifies, temperature-compensates, and drives the 4-20 mA "
"current loop: current, not voltage, because current ignores wire "
"resistance over long cable runs. Capacitive versions metalize the "
"diaphragm and a fixed backplate - pressure changes the gap, the gap "
"changes the capacitance, an ASIC reads femtofarads. Overpressure stops "
"and burst diaphragms protect against spikes; snubbers tame water "
"hammer. Calibration is against a deadweight tester - known masses on "
"a known piston - the gold standard of pressure truth."),
"key_points": [
"Diaphragm flex -> strain -> millivolts -> 4-20 mA loop.",
"0-10 bar transmitter at 6 bar: 13.6 mA -> 3.40 V across 250 ohms.",
"4 mA live-zero means 0 mA signals a broken wire, not zero pressure.",
"Current loops ignore cable resistance - voltage would not.",
"Gauge vs absolute vs differential: pick wrong and err by a full atmosphere.",
"10 m of water = 0.981 bar - the hydrostatic intuition behind depth and level.",
],
"requirements": [
"The force/strain record (bridges, diaphragms).",
"Pressure = force / area; hydrostatic p = rho g h.",
"A calculator for the loop exercises in the demo.",
],
"standards": [
"IEC 61298 defines pressure transmitter testing methods.",
"ASME B40.100 covers pressure gauges.",
"IEC 61508 applies where pressure transmitters guard safety functions.",
],
"citations": [C_FRADEN, C_DUNN, C_JOHNSON],
"sig_lens": (
"Signature take: the pressure sensor is the machine's awareness of being "
"squeezed - by water, by steam, by the atmosphere itself. Thirteen point "
"six milliamps for six bar: a current that refuses to be corrupted by "
"long wires, carrying its truth to the control room. The Signature "
"builder trusts the loop because the loop was designed by people who "
"had seen wires break."),
},
{
"key": "temperature_sensors",
"name": "Temperature Sensors: Thermocouples, RTDs, and Thermistors",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"Temperature has three great electrical translators, each with a "
"temperament. Thermocouples join two dissimilar metals: the junction "
"generates a voltage from the Seebeck effect - about 41 microvolts per "
"C for Type K - so 100 C of difference makes 4.1 mV; they are rugged, "
"cheap, and span -200 to 1300 C, but they measure difference, not "
"absolute, so the cold junction must be known. RTDs are platinum "
"resistors whose resistance rises almost linearly: a Pt100 is 100.00 "
"ohms at 0 C and 138.51 ohms at 100 C by the Callendar-Van Dusen "
"equation - accurate to fractions of a degree, the laboratory's choice "
"from -200 to 600 C. Thermistors are ceramic resistors with a violent "
"exponential curve (seen earlier: 10 k at 25 C, 2486 ohms at 60 C) - "
"cheap and exquisitely sensitive over a narrow span. Infrared sensors "
"read temperature without touching, from the thermal radiation every "
"object emits. Pick thermocouples for heat and harshness, RTDs for "
"accuracy, thermistors for cheap sensitivity, IR for distance or moving "
"targets."),
"how_it_works": (
"Seebeck: a temperature gradient along a conductor drives charge carriers "
"to the cold end, building a voltage; join two different metals and the "
"difference of their Seebeck voltages appears at the open ends - "
"proportional to the hot-minus-cold temperature difference. The "
"reference (cold) junction is compensated electronically - historically "
"an ice bath at 0 C, today a thermistor measuring the terminal block. "
"RTD: platinum's resistivity rises with temperature; the Callendar-Van "
"Dusen equation R(T) = R0(1 + AT + BT^2) (+CT^3 terms below zero) maps "
"resistance to ITS-90 temperature; 3- or 4-wire connections cancel lead "
"resistance. Thermistor: R = R0 exp(B(1/T - 1/T0)) - steep, nonlinear, "
"linearized by the Steinhart-Hart equation. Infrared: every surface "
"radiates per Planck's law; a thermopile or microbolometer measures the "
"flux and inverts it to temperature - but emissivity must be known, or "
"the reading is fiction. Self-heating (I^2 R in resistive sensors) is "
"kept negligible with small excitation currents."),
"key_points": [
"Type K thermocouple: ~41 uV/C; 100 C difference -> 4.1 mV; measures difference - compensate the cold junction.",
"Pt100 RTD: 138.51 ohms at 100 C (Callendar-Van Dusen) - the accuracy champion, -200 to 600 C.",
"Thermistor: exponential, cheap, ultra-sensitive over a narrow span; linearize with Steinhart-Hart.",
"Infrared reads thermal radiation without contact - but emissivity must be known.",
"Use 3- or 4-wire RTD connections to cancel lead resistance.",
"Keep excitation current small: self-heating corrupts resistive readings.",
],
"requirements": [
"The sensor introduction record (the thermistor chain).",
"Seebeck effect intuition; resistance vs temperature.",
"A calculator for the RTD exercises in the demo.",
],
"standards": [
"ASTM E230 / IEC 60584 define thermocouple EMF tables and tolerances.",
"IEC 60751 defines Pt100 characteristics and classes.",
"NIST Monograph 175 tabulates ITS-90 thermocouple references.",
],
"citations": [C_NIST, C_FRADEN, C_DUNN],
"sig_lens": (
"Signature take: temperature is the one quantity every machine must "
"respect, and these three are its three witnesses. The thermocouple "
"endures the furnace, the platinum tells the exact truth, the thermistor "
"notices the fever first. The Signature builder asks which witness the "
"job deserves - and remembers that an infrared reading without an "
"emissivity is not a measurement but a guess wearing a number."),
},
{
"key": "proximity",
"name": "Proximity and Distance: Ultrasonic, Infrared, and Capacitive Eyes",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"Before a machine touches something, it should know it is there. "
"Proximity sensors watch the near field without contact. Ultrasonic "
"sensors shout and listen: a 40 kHz ping's echo returns after the sound "
"crosses the gap twice, so a target 2 metres away answers in 11.66 ms "
"(2 x 2 m / 343 m/s); with 1-microsecond timing the resolution is "
"0.17 mm - and it works on any material, in dust and darkness. "
"Infrared sensors triangulate: a beam reflects off the target onto a "
"position-sensitive detector, and the spot's position gives the range - "
"fast and cheap for centimetres to metres, as in every robot vacuum. "
"Capacitive sensors feel the dielectric: a 1 cm2 plate 5 mm from a "
"target is 0.177 pF, closing to 4 mm makes 0.221 pF - they sense "
"non-metals through walls, which is why they guard level and presence. "
"Inductive sensors do the same for metals only, with a coil whose eddy "
"currents damp on approach - the end-of-travel switch in every machine "
"shop. Photoelectric through-beam and reflective sensors watch for "
"broken light. Pick ultrasonic for range on anything, IR for cheap "
"speed, capacitive for stealth through materials, inductive for metal in "
"filth."),
"how_it_works": (
"Ultrasonic: a piezoelectric transducer rings at 40 kHz (some at 200+ "
"kHz for precision), the echo's time-of-flight gives distance = c x t / "
"2 with c ~ 343 m/s in air - temperature-compensate c or accept ~0.18 "
"percent per degree error. The beam spreads (~30-degree cone at 40 kHz), "
"so small or angled targets vanish - and soft materials absorb the ping. "
"IR triangulation: an emitter and a position-sensitive detector sit a "
"baseline apart; near targets shift the reflected spot far, far targets "
"barely shift it - the response is steep up close, flat far away. "
"Capacitive: C = epsilon x A / d; an oscillator's frequency shifts with "
"C, and a threshold declares presence - guard electrodes shape the field. "
"Inductive: a high-frequency coil's field induces eddy currents in "
"nearby metal, damping the oscillator - ferrous metals trip it farthest. "
"Photoelectric: an LED beam to a retroreflector or a receiver; break the "
"beam, detect the object - the fastest presence sensing there is."),
"key_points": [
"Ultrasonic 2 m round trip: 11.66 ms; 1 us timing -> 0.17 mm resolution; works on anything in darkness.",
"IR triangulation: steep and precise up close, flat and vague far away.",
"Capacitive: 1 cm2 at 5 mm = 0.177 pF, at 4 mm = 0.221 pF - senses through non-conductive walls.",
"Inductive: metals only, via eddy-current damping - the machine-shop limit switch.",
"Temperature changes sound speed 0.18%/C - compensate or accept the error.",
"Photoelectric beams are the fastest presence detection.",
],
"requirements": [
"The sensor introduction record.",
"Time-of-flight intuition; capacitance basics.",
"A calculator for the ranging exercises in the demo.",
],
"standards": [
"IEC 60947-5-2 covers proximity switches and their ratings.",
"IEEE 2700-2017 frames their performance specs.",
"Manufacturer beam-pattern charts govern ultrasonic aiming.",
],
"citations": [C_FRADEN, C_DUNN, C_BISHOP],
"sig_lens": (
"Signature take: proximity sensing is manners for machines - knowing "
"where things are before touching them. The shout-and-listen of "
"ultrasound, the quiet watch of the beam: both are courtesies that "
"prevent collisions. The Signature machine never gropes blindly; it "
"extends its senses ahead of its muscles, because a touch should always "
"be a decision, never an accident."),
},
{
"key": "vision",
"name": "Vision Sensors: Cameras That Measure the World",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"A camera is a position sensor with millions of pixels: each pixel "
"reports light, and geometry turns light into measurement. The numbers "
"are friendly: a 6.4 mm wide sensor with 640 pixels has 10-micrometre "
"pixels; with an 8 mm lens, an object 1 metre away fills a field "
"800 mm wide - 1.25 mm per pixel. That is gauging: count pixels across "
"a part, multiply by 1.25, and you have measured it without touching. "
"Add a second camera and you get depth: with a 60 mm baseline, an 8 mm "
"lens, and 6 pixels of disparity, the target sits at 8.0 metres "
"(Z = f x B / disparity). Structured light and time-of-flight cameras "
"do it with one eye - projecting patterns or timing photons. Smart "
"cameras package lens, light, processor, and verdict ('pass/fail') into "
"one industrial box that watches bottles, labels, and solder joints at "
"line speed. Lighting is half the instrument: backlight for silhouettes, "
"diffuse dome for shiny curves, dark-field for scratches. A vision "
"sensor does not see like we do - it measures like we wish we could."),
"how_it_works": (
"The pinhole model rules: a world point projects through the lens centre "
"onto the sensor, so image position encodes ray angle. Calibrate once - "
"focal length, principal point, lens distortion - and pixels become "
"angles, angles become millimetres at a known distance. Telecentric "
"lenses make magnification independent of distance for true gauging. "
"Stereo triangulates: two calibrated views of the same point, disparity "
"inversely proportional to depth. Structured light replaces the second "
"camera with a projector of known patterns; time-of-flight modulates the "
"illumination and measures each pixel's phase lag - distance from the "
"speed of light. Processing runs edge detection, blob analysis, template "
"matching, and now neural networks - but the measurement chain is only "
"as honest as the calibration target it was taught on. Resolution sets "
"the smallest feature; depth of field and motion blur set the practical "
"limits."),
"key_points": [
"6.4 mm sensor, 640 px, 8 mm lens at 1 m: 800 mm field, 1.25 mm per pixel - count pixels, measure parts.",
"Stereo: 60 mm baseline, 6 px disparity -> 8.0 m deep (Z = fB/d).",
"Structured light and time-of-flight give depth with one camera.",
"Smart cameras package lens + light + processor + pass/fail verdict in one box.",
"Lighting is half the instrument: backlight, dome, dark-field for different defects.",
"Calibrate on a real target - uncalibrated vision measures fiction.",
],
"requirements": [
"The proximity record (triangulation intuition).",
"Similar triangles; pixels and fields of view.",
"A calculator for the optics exercises in the demo.",
],
"standards": [
"EMVA 1288 standardizes camera characterization (quantum efficiency, noise).",
"GigE Vision and USB3 Vision standardize industrial camera interfaces.",
"ISO 10360-8 covers optical CMM-style acceptance testing.",
],
"citations": [C_SZE, C_FRADEN, C_BISHOP],
"sig_lens": (
"Signature take: the camera is the only sensor that sees the whole "
"scene at once - millions of measurements in a single glance. But a "
"picture is not a measurement until geometry says what each pixel "
"means. The Signature builder calibrates before admiring: focal "
"length, distortion, baseline - the unglamorous numbers that turn a "
"pretty image into an honest ruler."),
},
{
"key": "imu",
"name": "IMUs: Accelerometers and Gyroscopes That Feel Motion",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"An inertial measurement unit feels motion from the inside: three "
"accelerometers report proper acceleration, three gyroscopes report "
"angular velocity, and together they track orientation and movement with "
"no outside reference - the inner ear of drones, phones, and rockets. "
"Accelerometers are proof masses on springs: tilt the chip and gravity's "
"component along the axis appears - 4.905 m/s2 on the x-axis means "
"exactly 30 degrees of tilt (arcsin 0.5). Gyroscopes - usually vibrating "
"MEMS tuning forks using the Coriolis effect - report rotation rate: "
"integrate 10 deg/s for 5 seconds and you have turned 50 degrees. The "
"catch is drift: a gyro bias of 0.1 deg/s grows to 6 degrees of heading "
"error in a minute, and double-integrating acceleration noise into "
"position diverges faster still. So IMUs are brilliant for short-term "
"motion and hopeless alone for long-term navigation - they are fused "
"with GPS, magnetometers, and vision (see sensor fusion) to get the best "
"of both. Every drone that hovers, every phone that rotates its screen, "
"every rocket that finds its way - all MEMS inertial sensing, all drift "
"managed by fusion."),
"how_it_works": (
"MEMS accelerometers micromachine a proof mass on silicon springs; "
"capacitive fingers measure its deflection - deflection is proportional "
"to acceleration, and at rest the chip reports 1 g upward (it feels the "
"table pushing back against gravity). Tilt sensing inverts this: the "
"gravity vector's components across the three axes give pitch and roll "
"via arcsine/arctangent - but any real acceleration corrupts it. MEMS "
"gyros vibrate a mass and watch the Coriolis force deflect it sideways "
"when the chip rotates - drive and sense modes on one chip, the rate "
"proportional to angular velocity. Integration turns rate into angle, "
"but bias integrates into ramp error and noise into random walk - "
"spec sheets quote bias instability and angle random walk for exactly "
"this reason. Sensor fusion (Kalman or complementary filters) blends "
"the gyro's fast truth with the accelerometer's long-term gravity "
"reference and the magnetometer's compass, each covering the others' "
"weaknesses."),
"key_points": [
"Accelerometer: 4.905 m/s2 on x = 30 deg tilt (arcsin 0.5); it feels gravity's components.",
"Gyro: integrate 10 deg/s x 5 s = 50 deg turned.",
"0.1 deg/s bias -> 6 deg heading error in one minute - drift is the enemy.",
"Double-integrating acceleration to position diverges fast - never navigate on IMU alone.",
"Fuse with GPS, magnetometer, vision: gyros for fast truth, others for long-term reference.",
"Spec-sheet words that matter: bias instability, angle random walk.",
],
"requirements": [
"The sensor introduction and measurement truth records.",
"Integration: angle = rate x time.",
"A calculator for the drift exercises in the demo.",
],
"standards": [
"IEEE 2700-2017 standardizes inertial sensor specs.",
"IEEE Std 952 covers inertial sensor test procedures.",
"RTCA DO-178C / DO-254 apply where IMUs fly safety-critical missions.",
],
"citations": [C_TIT, C_FRADEN, C_BISHOP],
"sig_lens": (
"Signature take: the IMU is the machine's inner ear - it knows it is "
"moving even in the dark, with no landmarks, asking nothing of the "
"world. But the inner ear drifts, in machines as in men: six degrees a "
"minute of quiet lying. The Signature builder trusts the IMU's fast "
"honesty and corrects its slow fiction - with magnets, satellites, and "
"cameras - because no sense should navigate alone."),
},
{
"key": "lidar_radar",
"name": "LIDAR and Radar: Mapping the World with Light and Radio",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"LIDAR maps the world in 3D with timed light: fire a laser pulse, catch "
"the reflection, and distance is the speed of light times half the "
"round-trip time - 1 metre means 6.67 nanoseconds. Timing to 1 ns "
"resolves 0.15 m; spin the beam at 10 Hz with 3600 points per revolution "
"and the sensor paints 36000 3D points per second - the point clouds that "
"drive autonomous vehicles and survey drones. Radar does the same with "
"radio: a 77 GHz automotive radar (3.9 mm wavelength) sees through fog "
"and rain that blind LIDAR, and the Doppler shift measures velocity "
"directly - a target approaching at 10 m/s shifts the echo by 5.13 kHz. "
"Flash LIDAR and phased arrays are killing the spinning mirror; FMCW "
"LIDAR adds Doppler velocity to every point like radar. The trade is "
"physics: light gives centimetre detail but scatters in weather; radio "
"pierces weather but resolves coarsely. Self-driving stacks both, plus "
"cameras, because no single wavelength tells the whole truth."),
"how_it_works": (
"Direct time-of-flight LIDAR: a pulsed laser (often 905 or 1550 nm), a "
"scanning mirror or rotating head, and a fast photodetector with a "
"time-to-digital converter - distance = c x t / 2. Eye safety caps the "
"pulse energy (Class 1), which caps the range; 1550 nm allows more power "
"because the cornea absorbs it. FMCW LIDAR chirps the laser frequency "
"and mixes the echo with the outgoing chirp - the beat frequency gives "
"range, its Doppler shift gives velocity, all coherently. Radar: FMCW at "
"24/77 GHz, antennas on PCB, the same chirp-and-mix math - range from "
"beat frequency, velocity from Doppler, angle from phased-array phase "
"differences. Point clouds accumulate scans into maps; SLAM algorithms "
"localize the sensor inside the map it is building. Reflectivity lies: "
"dark or angled surfaces return little - intensity is not distance, and "
"fusion with cameras disambiguates."),
"key_points": [
"1 m round trip = 6.67 ns; 1 ns timing -> 0.15 m range resolution.",
"10 Hz spin x 3600 pts/rev = 36000 3D points per second.",
"77 GHz radar sees through fog; 10 m/s approach -> 5.13 kHz Doppler shift.",
"FMCW (light or radio) measures range AND velocity coherently.",
"Light: centimetre detail, fails in weather. Radio: pierces weather, coarse detail.",
"Dark/angled surfaces return little - intensity is not distance.",
],
"requirements": [
"The proximity record (time-of-flight).",
"Speed of light c = 3.00e8 m/s; Doppler basics.",
"A calculator for the timing exercises in the demo.",
],
"standards": [
"IEC 60825-1 governs laser eye safety (Class 1 LIDAR).",
"ETSI EN 302 264 / FCC Part 95 regulate automotive radar bands.",
"IEEE 2700-2017 frames ranging-sensor performance specs.",
],
"citations": [C_SHAN, C_FRADEN, C_BISHOP],
"sig_lens": (
"Signature take: LIDAR is the machine's way of touching the world with "
"light - thirty-six thousand touches a second, each timed to a "
"nanosecond. Radar is the same touch in a longer wavelength, patient "
"through fog. The Signature builder pairs them because reality has "
"weather: one wavelength for the clear day, one for the storm, and the "
"map is the agreement between them."),
},
{
"key": "tactile",
"name": "Tactile Sensors: Giving Machines a Sense of Touch",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"Touch is the last sense machines are learning, and it may be the most "
"important for working beside humans. A tactile taxel is a tiny force "
"sensor; an array of them is artificial skin. Capacitive taxels are the "
"workhorse: two plates with a squishy dielectric - a 1 cm2 taxel with a "
"1 mm gap is 0.885 pF, press it to 0.9 mm and it rises to 0.984 pF, an "
"11.1 percent signal for a 0.1 mm squeeze. Tile 8x8 and you have 64 "
"taxels imaging pressure like a camera images light - enough to feel "
"shape, slip, and texture. Resistive FSRs (force-sensing resistors) are "
"cheaper: their resistance falls with force, roughly log-log - 10 k at "
"1 N, about 2.76 k at 5 N - fine for 'how hard' if not for precision. "
"Piezoelectric films feel dynamic touch and vibration; optical waveguides "
"feel deformation as light loss. Robot fingertips use them to grip "
"without crushing, detect slip before the object falls, and tell texture "
"by vibration. Skin is still the hardest sensor to copy: millions of "
"receptors, self-healing, and wired to a brain that cares. We are at "
"64 taxels and proud of it."),
"how_it_works": (
"Capacitive taxels parallel-plate physics: C = epsilon x A / d, so "
"squeezing the gap raises capacitance; each taxel is scanned by a "
"capacitance-to-digital converter, and the array is read row by row like "
"a keyboard matrix. Elastomer dielectrics add compliance and protect the "
"plates. FSRs sandwich a piezoresistive polymer: more force, more "
"conductive paths, lower resistance - simple voltage dividers read them, "
"with log-log calibration curves. Piezoelectric skins (PVDF film) "
"generate charge only while the force changes - perfect for slip and "
"texture vibration, blind to static holding force. Optical tactile "
"sensors (like GelSight) press a gel against the object and photograph "
"the deformation with an internal camera - stunning shape resolution "
"from an ordinary camera. Slip detection watches high-frequency "
"vibration or the centroid of pressure racing across the array - the "
"signal to tighten the grip before the drop."),
"key_points": [
"Capacitive taxel: 1 cm2, 1 mm gap = 0.885 pF; pressed to 0.9 mm = 0.984 pF (11.1% signal).",
"8x8 array = 64 taxels imaging pressure like a camera images light.",
"FSR: resistance falls log-log with force; ~2.76 k at 5 N from 10 k at 1 N.",
"Piezo films feel dynamic touch/vibration only - blind to static force.",
"Optical gel sensors photograph deformation for stunning shape resolution.",
"Slip detection: watch vibration or pressure-centroid motion, tighten before the drop.",
],
"requirements": [
"The force/strain and proximity (capacitive) records.",
"Capacitance vs gap; arrays and scanning.",
"A calculator for the taxel exercises in the demo.",
],
"standards": [
"IEEE 2700-2017 frames tactile sensor performance specs.",
"ISO 13482 covers safety of personal-care robots that touch humans.",
"Manufacturer calibration curves govern FSR log-log behavior.",
],
"citations": [C_DAHIYA, C_FRADEN, C_BISHOP],
"sig_lens": (
"Signature take: touch is the sense that makes a machine gentle. Force "
"without touch is a hammer; force with touch is a hand. Sixty-four "
"taxels feeling an eleven-percent whisper of capacitance - that is the "
"beginning of care in hardware. The Signature grip knows the egg will "
"break before the egg knows it, and that foreknowledge is the whole "
"difference between a tool and a partner."),
},
{
"key": "signal_conditioning",
"name": "Signal Conditioning: From Microvolts to Clean Data",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Between every raw transducer and every converter sits the most "
"underappreciated electronics in the system: signal conditioning. Raw "
"sensor signals are small, high-impedance, noisy, and wrong-ranged - "
"millivolts riding on volts of common-mode, kilohm sources a converter "
"cannot load. The instrumentation amplifier fixes the first two: three "
"op-amps in a classic topology amplify only the difference between its "
"inputs, with gain set by one resistor - G = 1 + 50 k / Rg, so Rg = 500 "
"ohms gives exactly 101, turning a 2.5 mV bridge signal into 252.5 mV. "
"Filters fix the noise: a resistor and capacitor make an anti-alias "
"low-pass - 1.6 k and 0.5 uF corner at 198.9 Hz, safely below the 500 Hz "
"Nyquist limit of a 1 kHz sampler, so high-frequency noise cannot fold "
"back as phantom signals. Then come level shifting (bipolar to "
"single-supply), protection (overvoltage clamps, because sensors live in "
"a rough world), isolation (breaking ground loops between factory floor "
"and controller), and linearization (undoing the thermistor's curve "
"before the converter sees it). Conditioning is where microvolts become "
"trustworthy volts - skip it and the world's best ADC digitizes garbage "
"with exquisite precision."),
"how_it_works": (
"The instrumentation amplifier's three-op-amp structure: two non-"
"inverting buffers present gigohm input impedance (no loading the "
"bridge), their shared gain resistor sets the first-stage gain, and a "
"differential subtractor rejects what is common to both inputs - 50/60 "
"Hz pickup, ground bounce - by 80-120 dB of common-mode rejection. Gain "
"accuracy lives in that one resistor; drift lives in its tempco. "
"Anti-alias filtering obeys Nyquist: sample at fs, and any signal above "
"fs/2 aliases into the band - so a low-pass cornering well below fs/2 "
"(198.9 Hz for fs = 1 kHz) attenuates the alias band by 20 dB per decade "
"(first order) or more. Sallen-Key stages build sharper active filters "
"without inductors. Protection diodes clamp sensor lines to the supply "
"rails; series resistors limit fault current; TVS diodes eat surges. "
"Isolation amplifiers or digital isolators break the galvanic path where "
"ground potentials differ by tens of volts. Cold-junction compensation, "
"bridge completion, and excitation current sources are conditioning too - "
"everything that makes the transducer's raw truth converter-ready."),
"key_points": [
"Instrumentation amp: gigohm inputs, one-resistor gain (Rg=500 -> G=101); 2.5 mV -> 252.5 mV.",
"CMRR of 80-120 dB rejects what is common to both inputs.",
"Anti-alias: RC at 198.9 Hz for 1 kHz sampling; anything above 500 Hz would fold back as lies.",
"Protection (clamps, TVS), isolation (ground loops), level shifting - the unglamorous essentials.",
"Bridge completion, excitation, cold-junction compensation are conditioning too.",
"Skip conditioning and the best ADC digitizes garbage with exquisite precision.",
],
"requirements": [
"The force/strain record (bridges) and ADC record (Nyquist).",
"Op-amp golden rules; RC time constants.",
"A calculator for the gain/filter exercises in the demo.",
],
"standards": [
"IEC 61000-4 series governs the EMC immunity conditioning must survive.",
"IEC 61326 covers EMC requirements for measurement equipment.",
"Manufacturer CMRR/gain-drift specs bound the error budget.",
],
"citations": [C_DUNN, C_JOHNSON, C_ADC],
"sig_lens": (
"Signature take: conditioning is the translator's discipline - the "
"quiet work between the world's whisper and the computer's hearing. "
"Gain, filtering, protection, isolation: none of it glamorous, all of "
"it load-bearing. The Signature builder lavishes care here precisely "
"because no one applauds it - for this is where honesty is manufactured, "
"one rejected common-mode volt at a time."),
},
{
"key": "adc_dac",
"name": "ADCs and DACs: The Border Crossing Between Worlds",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Every sensor's analog truth must cross into digital, and every digital "
"command must cross back out to move an actuator - the ADC and DAC are "
"that border. An N-bit converter slices its reference into 2^N levels: "
"a 12-bit ADC on a 3.3 V reference has steps of 805.7 microvolts (the "
"LSB), and rounding to the nearest step injects quantization noise of "
"LSB / sqrt(12) = 232.6 uV rms - the theoretical floor no 12-bit "
"converter beats. Real converters add their own noise and distortion, "
"summarized as SINAD; a 70 dB SINAD means 11.34 effective bits (ENOB = "
"(SINAD - 1.76)/6.02) - the honest resolution. SAR ADCs convert bit by "
"bit (fast, medium resolution); sigma-delta ADCs oversample and "
"noise-shape (slow, 24-bit precision for weigh scales); pipeline and "
"flash trade power for gigahertz. DACs reverse it: an R-2R ladder or "
"sigma-delta modulator turns numbers back into voltage to drive "
"actuators - with settling time and glitch energy as the fine print. "
"Sample fast enough (Nyquist), reference cleanly (the reference IS the "
"ruler), and never forget: the converter's resolution is a promise the "
"signal chain must keep."),
"how_it_works": (
"SAR: a comparator binary-searches the input against a DAC - N "
"comparisons for N bits, one conversion per N clock cycles, the "
"workhorse of embedded sensing. Sigma-delta: a 1-bit modulator "
"oversamples hugely (64-256x), pushing quantization noise to high "
"frequencies where a digital filter removes it - 24-bit audio and "
"precision weighing from a 1-bit core. Flash: 2^N comparators decide "
"all bits at once - gigahertz for oscilloscopes, power-hungry and "
"coarse. Quantization noise is uniformly distributed over +-LSB/2, "
"hence LSB/sqrt(12) rms; dither (added noise!) decorrelates it from "
"the signal. ENOB folds noise plus distortion into one honest number. "
"DAC: R-2R ladders switch binary-weighted currents; multiplying DACs "
"take an analog reference; glitch impulse (the mid-scale code-change "
"spike) and settling time bound control-loop speed. The voltage "
"reference - bandgap or buried-zener - defines every code's meaning; "
"its drift with temperature and time is the system's drift."),
"key_points": [
"12-bit, 3.3 V: LSB = 805.7 uV; quantization noise = 232.6 uV rms - the unbeatable floor.",
"70 dB SINAD -> 11.34 effective bits: ENOB is the honest resolution.",
"SAR: fast bit-by-bit workhorse. Sigma-delta: slow 24-bit precision. Flash: GHz, power-hungry.",
"DACs reverse the crossing: R-2R ladders, settling time, glitch energy.",
"The voltage reference IS the ruler - its drift is the system's drift.",
"Sample above Nyquist, reference cleanly, and keep the chain's promise.",
],
"requirements": [
"The signal conditioning record (anti-alias, Nyquist).",
"Binary: N bits -> 2^N levels.",
"A calculator for the LSB/ENOB exercises in the demo.",
],
"standards": [
"IEEE Std 1241 defines ADC terminology and test methods.",
"IEEE Std 1658 defines DAC terminology and test methods.",
"IEC 61326 covers EMC for the converter instruments.",
],
"citations": [C_ADC, C_DUNN, C_JOHNSON],
"sig_lens": (
"Signature take: the converter is the border checkpoint between the "
"continuous world and the counted one - and every crossing pays the "
"quantization toll. Eight hundred five microvolts per step: that is the "
"price of admission to digital. The Signature builder pays it gladly "
"but never pretends the toll is zero - for the map is not the territory, "
"and eleven point three honest bits beat sixteen lying ones."),
},
{
"key": "buses",
"name": "Talking to Chips: I2C, SPI, and CAN Buses",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Sensors must talk to controllers, and three buses carry almost all of "
"that conversation. I2C is the two-wire minimalist: SDA and SCL, every "
"chip with a 7-bit address (~112 usable of 128), the controller "
"addressing each sensor in turn. At 400 kHz with 9 clocks per byte "
"(8 bits + ACK), a bus moves about 44.4 kilobytes per second - plenty "
"for temperature, pressure, and IMU registers, on just two wires with "
"pull-up resistors. SPI is the four-wire sprinter: MOSI, MISO, clock, "
"and a chip-select per device - full duplex, no addressing overhead, "
"10 MHz clocks moving 1.25 megabytes per second each way - the choice "
"for fast ADCs, displays, and radios. CAN is the automotive survivor: "
"two wires, differential, multi-master, with bitwise arbitration so the "
"most urgent message always wins the bus without corruption - at 1 Mbps "
"each bit is 1 microsecond and an 8-byte frame takes about 108 "
"microseconds, and it shrugs off the electromagnetic warzone under a "
"hood. Pick I2C for many slow sensors on few pins, SPI for speed, CAN "
"for vehicles and noisy factories where messages must not die."),
"how_it_works": (
"I2C: open-drain lines pulled high; the controller pulls SDA low for a "
"START, clocks out 7 address bits plus read/write, and each byte gets an "
"ACK bit from the receiver - clock stretching lets slow sensors hold "
"SCL low until ready. Addresses collide if two chips share one - "
"address pins or multiplexers fix it. SPI: the controller asserts one "
"chip-select, then clocks shift registers in both directions "
"simultaneously - mode (CPOL/CPHA) sets clock polarity and sampling "
"edge; daisy-chaining is possible but chip-selects are simpler. Speed "
"is limited by signal integrity, not protocol. CAN: dominant/recessive "
"bits on a differential pair; transmitters monitor the bus while "
"sending - a node sending recessive that reads dominant loses "
"arbitration silently, so the lowest ID wins without damage; CRC, ACK "
"slots, and error frames make it brutally reliable, with faulty nodes "
"voted off by error counters. Termination resistors (120 ohms each end) "
"prevent reflections. Higher layers (CANopen, J1939) define what the "
"bytes mean."),
"key_points": [
"I2C: 2 wires, 7-bit addresses (~112 usable), 400 kHz -> ~44.4 kB/s - many slow sensors, few pins.",
"SPI: 4 wires, full duplex, 10 MHz -> 1.25 MB/s each way - fast ADCs, displays, radios.",
"CAN: differential multi-master, arbitration lets the most urgent message win undamaged.",
"CAN at 1 Mbps: 1 us bits, ~108 us per 8-byte frame - built for automotive EMI warzones.",
"I2C needs pull-ups and unique addresses; SPI needs a chip-select per device; CAN needs 120-ohm terminators.",
"CANopen/J1939 define what CAN bytes mean; I2C/SPI leave meaning to datasheets.",
],
"requirements": [
"The ADC record (what the buses carry).",
"Bits, bytes, clocks per byte.",
"A calculator for the throughput exercises in the demo.",
],
"standards": [
"NXP UM10204 defines the I2C bus specification.",
"Motorola/Freescale SPI Block Guide defines SPI signaling.",
"Bosch CAN 2.0 plus ISO 11898 define CAN; ISO 11898-2 the high-speed physical layer.",
],
"citations": [C_I2C, C_CAN, C_BISHOP],
"sig_lens": (
"Signature take: buses are the etiquette of silicon - how a hundred "
"chips share a conversation without shouting over each other. Two wires "
"for the patient, four for the hurried, arbitration for the urgent: "
"each protocol is a social contract written in clocks and volts. The "
"Signature builder chooses the contract that fits the company - and "
"terminates the bus, because even electrons need good manners at the "
"end of the line."),
},
{
"key": "sensor_fusion",
"name": "Sensor Fusion: Kalman and Complementary Filters",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"No single sensor tells the whole truth, so engineers blend them: the "
"gyro is fast but drifts, the accelerometer is absolute but noisy, GPS "
"is absolute but slow - fusion takes each sensor's strength and covers "
"its weakness. The complementary filter is the honest simple version: "
"angle = 0.98 x (angle + gyro x dt) + 0.02 x accel_angle - trust the "
"gyro for 98 percent of the fast motion, nudge 2 percent toward the "
"accelerometer's gravity reference each step, and drift can never "
"accumulate. The Kalman filter is the optimal version: it models the "
"system, predicts the next state, then corrects the prediction with "
"the measurement, weighting each by its uncertainty. A one-dimensional "
"demo tells the story: true value 10.0, noisy measurements swinging "
"with sine-wave disturbance, process noise Q = 1e-4, measurement noise "
"R = 1.0 - after 50 updates the estimate sits within 0.3 of truth, "
"smoother than any single reading. That predict-correct loop, scaled "
"to matrices, flies aircraft, lands rockets, and steadies every drone "
"camera. Fusion is not averaging - it is each sensor testifying only "
"to what it knows."),
"how_it_works": (
"Kalman in two steps, repeated forever. Predict: x_hat = F x + B u, "
"P = F P F' + Q - the model projects the state forward and grows the "
"uncertainty by the process noise. Update: K = P H' / (H P H' + R) - "
"the Kalman gain weighs prediction against measurement by their "
"uncertainties; x = x_hat + K (z - H x_hat) corrects the estimate by "
"the surprise times the gain; P = (1 - K H) P shrinks the uncertainty. "
"Trustworthy sensor (small R) gets high gain - the estimate jumps to "
"the measurement; shaky model (big Q) likewise. The complementary "
"filter is the steady-state Kalman for one special case: a fixed blend "
"of high-passed gyro and low-passed accel, no matrices, nearly as good "
"for tilt. Extended Kalman linearizes nonlinear models each step "
"(the workhorse of navigation); unscented and particle filters handle "
"worse nonlinearity. Tuning is choosing Q and R - the engineer's "
"quantified trust in model versus measurement."),
"key_points": [
"Fuse strengths: gyro fast but drifting, accel absolute but noisy, GPS absolute but slow.",
"Complementary: 98% gyro integration + 2% accel nudge - drift can never accumulate.",
"Kalman predict-correct: gain K weights measurement vs prediction by their uncertainties.",
"1-D demo: true 10.0, Q=1e-4, R=1.0 -> within 0.3 of truth after 50 updates.",
"Small R (trusted sensor) -> high gain; big Q (shaky model) -> trust measurements.",
"Fusion is not averaging - each sensor testifies only to what it knows.",
],
"requirements": [
"The IMU record (why fusion is needed).",
"Weighted averages; basic matrix intuition for the full form.",
"A calculator or the demo for the filter.",
],
"standards": [
"Welch & Bishop TR 95-041 is the canonical Kalman introduction.",
"IEEE Std 952 covers inertial navigation test and fusion practice.",
"RTCA DO-178C applies to airborne fusion software.",
],
"citations": [C_KALMAN, C_TIT, C_BISHOP],
"sig_lens": (
"Signature take: fusion is the wisdom of not trusting any single "
"witness completely - the gyro's quick eyes, the accelerometer's deep "
"memory of down, each corrected by the other. The Kalman gain is "
"quantified humility: how much to believe the model, how much the "
"measurement, updated with every sample. The Signature navigator is "
"never certain and never lost, because certainty was never the goal - "
"convergence was."),
},
{
"key": "sizing",
"name": "Sizing and Selection: Picking the Right Actuator and Sensor",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Choosing hardware is where the whole discipline comes due - and it is "
"arithmetic, not taste. Size the actuator from the load: a 0.02 kg m2 "
"inertia spun from rest to 3000 rpm (314.16 rad/s) in 0.5 seconds needs "
"angular acceleration 628.3 rad/s2, so acceleration torque is 12.57 N m; "
"add 1 N m of friction and the peak demand is 13.57 N m. Then check the "
"duty cycle: 0.5 s accelerating, 2 s running at 2 N m, 0.5 s braking, "
"1 s dwelling - the RMS torque is 6.93 N m, and that is what the motor's "
"continuous rating must beat. Apply a 1.5 safety factor and the shopping "
"list reads: peak at least 20.4 N m, continuous at least 10.4 N m. "
"Sensor selection mirrors it: list the measurand, range, required "
"accuracy, bandwidth, and environment - then pick the simplest sensor "
"that meets all five, because every extra decimal costs money and "
"complexity. Check the ugly realities last: supply voltage available, "
"ambient temperature, washdown, EMI, cable lengths, and what happens at "
"power loss (brakes? absolute encoders? fail-safe valves?). The right "
"choice is the smallest, cheapest combination that meets the numbers "
"with margin - engineering is the art of enough."),
"how_it_works": (
"The sizing workflow never changes. One: define the motion - torque or "
"force vs time, including friction, gravity, and inertia (J = m r^2 for "
"the load reflected through the transmission). Two: compute peak torque "
"(acceleration plus load) and RMS torque over the full duty cycle - "
"thermal reality cares about RMS. Three: divide by transmission "
"efficiency and ratio to get motor-shaft numbers. Four: pick a motor "
"whose continuous rating exceeds RMS torque times safety factor and "
"whose peak rating exceeds peak torque - then verify the speed fits the "
"motor's curve and the voltage is available. Five: size the drive for "
"the peak current, the power supply for the RMS power plus margin, and "
"the feedback (encoder resolution from the positioning tolerance "
"divided by at least 4-10x). Sensor selection: range must cover the "
"worst case with headroom, accuracy one grade better than the process "
"needs, bandwidth 5-10x the fastest signal of interest, and the package "
"must survive the environment. Document every assumption - the next "
"engineer will thank you."),
"key_points": [
"Peak torque: inertia x alpha + friction - 0.02 kg m2 to 3000 rpm in 0.5 s needs 13.57 N m peak.",
"RMS torque over the duty cycle (6.93 N m here) is what the continuous rating must beat.",
"1.5x safety factor -> shop for >= 20.4 N m peak, >= 10.4 N m continuous.",
"Sensor: range, accuracy, bandwidth, environment - simplest that meets all five wins.",
"Encoder resolution: positioning tolerance divided by 4-10x.",
"Check power-loss behavior: brakes, absolute encoders, fail-safe valves.",
],
"requirements": [
"The torque/speed, transmission, servo, and encoder records.",
"RMS: square, mean, root - over the duty cycle.",
"A calculator for the sizing exercises in the demo.",
],
"standards": [
"IEC 60034-1 duty types (S1-S10) frame the thermal sizing.",
"ISO 13849 guides the safety-related selection (PL/SIL).",
"AGMA/ISO gear and ISO 3408 screw standards rate the transmission.",
],
"citations": [C_BOLTON, C_BISHOP, C_OGATA],
"sig_lens": (
"Signature take: sizing is where engineering becomes a promise - the "
"numbers you write are the machine you will get. Thirteen point five "
"seven newton-metres peak, six point nine three RMS: no adjectives, no "
"hope, just the load's honest demand with a fifty-percent margin for "
"the unknown. The Signature builder sizes on paper so the machine never "
"has to apologize in metal."),
},
{
"key": "reliability",
"name": "Failure, Safety, and Maintenance: What Breaks and How to Know",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Everything built eventually fails; the discipline is in knowing when "
"and planning for it. Reliability starts with the failure rate: a "
"component with MTBF 50000 hours has lambda = 2e-5 failures per hour, "
"so its chance of surviving one year (8760 hours) is e^(-0.1752) = "
"83.9 percent - no better, no worse, exponential and honest. With a "
"4-hour mean repair time, availability is 50000/50004 = 99.992 percent. "
"Actuators fail in known ways: motor bearings wear (listen for the "
"whine), brushes wear out (watch the dust), windings cook (watch the "
"temperature), hydraulic seals weep (watch the floor), pneumatic seals "
"leak (listen for the hiss), piezo stacks crack under tension, SMA "
"wires fatigue past 3 percent strain. Sensors fail sneakier: drift - "
"a sensor wandering 0.1 percent per month is 1.2 percent per year, so "
"recalibrate every 6 months to hold 0.6 percent; stuck-at faults that "
"report a plausible constant; and common-cause failures where one "
"environment kills redundant sensors together. Safety answers with "
"layers: safe-torque-off on drives, redundant sensors voting 2-of-3, "
"proof testing on schedule, and FMEDA numbers behind every safety "
"rating. Maintain on condition (vibration, temperature, current "
"signature) where you can, on calendar where you must - and log "
"everything, because the failure you predicted is a maintenance task "
"and the one you did not is an incident."),
"how_it_works": (
"The exponential model: R(t) = e^(-lambda t) for constant failure rate "
"lambda = 1/MTBF - memoryless, the workhorse of electronics "
"reliability; Weibull models wear-out with its shape parameter. "
"Availability = MTBF / (MTBF + MTTR) - reliability is about not "
"failing, availability about being up. FMEA lists every failure mode, "
"its effect, and its detection; FMEDA adds diagnostic coverage numbers "
"for safety certification. Condition monitoring watches the physics: "
"motor current signature analysis sees broken rotor bars as sidebands, "
"vibration spectra see bearing defects at their fault frequencies, "
"thermography sees the hot winding before it shorts, pressure decay "
"sees the leaking seal. Sensor validation watches the sensors "
"themselves: range checks, rate-of-change limits, cross-comparison "
"between redundant channels, and model-based residuals that flag the "
"channel disagreeing with physics. Proof-test intervals come from the "
"target SIL: the more dangerous the failure, the more often you prove "
"the safety function still works. Calibration intervals come from "
"drift specs and the accuracy the process demands."),
"key_points": [
"MTBF 50000 h -> 83.9% survive one year (exponential); 4 h MTTR -> 99.992% availability.",
"Actuator failures: bearings, brushes, cooked windings, weeping seals, hissing leaks, cracked piezos.",
"Sensor failures: drift (0.1%/month -> recalibrate every 6 months), stuck-at, common-cause.",
"Condition monitoring: current signature, vibration spectra, thermography, pressure decay.",
"Safety layers: safe-torque-off, 2-of-3 voting, proof tests, FMEDA numbers.",
"The predicted failure is a maintenance task; the unpredicted one is an incident - log everything.",
],
"requirements": [
"The measurement truth record (drift, calibration).",
"Exponential e^(-x); availability vs reliability.",
"A calculator for the reliability exercises in the demo.",
],
"standards": [
"IEC 61508 / ISO 13849 govern functional safety and SIL/PL ratings.",
"IEEE Std 1413 and IEC 61709 guide reliability prediction.",
"ISO 13374 standardizes condition-monitoring data processing.",
],
"citations": [C_OCONNOR, C_DUNN, C_BISHOP],
"sig_lens": (
"Signature take: the honest machine plans its own ending. Eighty-three "
"point nine percent for the year: not a wish, a number - and the "
"maintenance plan is written from numbers like it. The Signature "
"builder instruments for the failure, schedules for the drift, and logs "
"everything, because a machine that knows how it will die can be trusted "
"with how it lives."),
},
]
