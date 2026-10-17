#!/usr/bin/env python3
"""Entries for the Microrobotics field databases (field #28, taxonomy order).

Verified 2026-10-17: NO database covers microrobotics as a discipline
(micro-scale robots: MEMS bodies, micro-actuation - electrostatic,
piezoelectric, thermal, magnetic; micro-sensors; microfabrication;
scaling laws; micro-locomotion; swarm microrobots; medical microrobots;
micro-assembly; microfluidic integration; wireless/chemical/biological
powering; micro-scale control; inspection, surgical, and drug-delivery
applications).
- Manifest search (2356 databases): no 'microrobot' database exists. Nearest
  neighbors: 'robots' (37,000 macro-robot records), 'robotics-autonomous-
  physical-systems' (32 macro records), 'microsystems-engineers' (people
  records), 'microfabrication labs/facilities' (cleanroom facility records,
  title-only). None teach the micro-scale robotics discipline.
- Whole-system title sweep over all 758 shard indexes ('microrobot',
  'micro-robot', 'micro robot', 'nanorobot', 'microbot', 'microgripper',
  'microactuator', 'microassembly', 'microswimmer', 'micro-locomotion',
  'comb drive', 'thermal microactuator', 'piezoelectric microactuator',
  'electrostatic microactuator', 'microfluidic robot'): ZERO hits across
  1,129,379 records.
- Full-text sweep over all chunk files: only incidental mentions
  ('Microfabrication Facilities/Labs' cleanroom records, 'Scaling laws for
  teams' management records, passing mentions in hypersonics/petrophysics).
  ZERO full-record discipline coverage anywhere.
- Per the task rule, bare formula cards do NOT count as discipline coverage.

So this build creates two NEW databases, 32 ladder-ordered records each,
covering ONLY what the system left uncovered:

  microrobotics             - The Microrobotics Database (public-harvest:
                             real, fact-checked micro/nano-scale robotics;
                             citations Madou 2011, Maluf & Williams 2004,
                             Senturia 2001, Kovacs 1998, Gad-el-Hak 2006,
                             Sitti 2017, Nelson/Kaliakatsos/Abbott 2010,
                             Purcell 1977, Feynman 1959, Judy 2001,
                             Diller & Sitti 2013, Howell 2001, Pister 1992,
                             Ma et al. 2013, Whitesides & Grzybowski 2002,
                             Rubenstein et al. 2014, Kummer et al. 2010)
  microrobotics-signature  - The Microrobotics Signature Database (his original
                             Signature interpretation; src signature, titles
                             suffixed " (Signature Edition)", never presented
                             as authentic public record)

32 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Subtitle disambiguation (fields #13-27 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Scaling Laws at
Small Sizes: Why Surface Beats Volume".

Numerical cores (all hand-verified 2026-10-17):
- 1 mm silicon cube: mass 2.33 mg, weight 22.9 uN, surface/volume 6000 /m.
- Re: 1 mm robot at 1 mm/s in water -> Re = 1; 10 um at 10 um/s -> Re = 1e-4;
  human swimmer -> Re ~ 2e6.
- Capillary length of water: 2.7 mm (below ~mm, surface tension beats gravity).
- Brownian: 1 um particle in water diffuses ~0.66 um rms in 1 s.
- Si cantilever 500x50x2 um: k = 0.135 N/m, f0 = 5.4 kHz, self-weight sag 8.5 nm.
- 150 mm wafer, 5x5 mm dies -> ~700 dies; DRIE 10 um/min -> 50 min through 500 um.
- Al-on-Si thermal stress, dT=100 K -> 143 MPa.
- Comb drive (N=100, h=10 um, g=2 um, V=50 V) -> 11.1 uN.
- Parallel-plate pull-in (A=1 mm2, g0=5 um, k=10 N/m) -> 6.5 V.
- PZT bimorph (L=2 mm, t=0.2 mm) -> 27 nm/V; 1.35 um at 50 V.
- Chevron (L=500 um, 5 deg, dT=300 K) -> 4.5 um amplified from 0.39 um.
- 100 um NdFeB cube in 10 mT -> torque 1e-8 N m; 1 T/m gradient -> 1 uN (~14x weight).
- Capacitive accel (A=1 mm2, g=2 um, m=1 ug, k=1 N/m): C0 = 4.43 pF, 1 g -> 9.8 nm -> dC 21.7 fF; f0 = 5.0 kHz.
- 1 mm3 battery ~1 J -> 1 mW robot runs ~18 min; 1 mF @ 3 V -> 4.5 s.
- 13.56 MHz inductive: L=1 uH resonates with 138 pF.
- Stokes drag on 1 mm sphere at 1 mm/s in water -> 9.4 nN.
- Microchannel 100x50 um, 1 cm, 1 kPa -> 0.104 uL/s, 20.8 mm/s, Re = 1.4.
- Capillary adhesion on 10 um sphere -> 2.3 uN (beats typical grip forces).
- Fixed-guided Si flexure 200x20x5 um: k = 13.2 N/m; 10 um -> 132 uN, 317 MPa.
- 10 E. coli pushing 10 um cargo -> 53 um/s (Stokes).
- Optical trap k=10 pN/um; 100 mW in 1 um spot -> 1.3e11 W/m2.
- 1e9 robots x 1 pL -> 1 mL total dose; 1% targeting -> 10 uL local.
- Per-hinge 99% over 50 hinges -> 60.5% assembly yield; need 99.9% for 95%.
- Stiction: water meniscus on 100 um plate -> 57.6 uN vs ~10 uN restore.
- Weibull (beta=2, eta=1e7): 1e6 cycles -> 1.0% failed.
- Microscope diffraction limit (550 nm, NA 0.9) -> 0.37 um.
- Learning curve 80%: 10k units @ $100 -> 10M units @ $10.82.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "microrobotics, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_MADOU = ("Madou, Marc J. 'Fundamentals of Microfabrication and "
           "Nanotechnology'. 3rd ed. CRC Press, 2011.")
C_MALUF = ("Maluf, Nadim and Williams, Kirt. 'An Introduction to "
           "Microelectromechanical Systems Engineering'. 2nd ed. Artech "
           "House, 2004.")
C_SENTURIA = ("Senturia, Stephen D. 'Microsystem Design'. Kluwer Academic "
              "Publishers, 2001.")
C_KOVACS = ("Kovacs, Gregory T. A. 'Micromachined Transducers Sourcebook'. "
            "McGraw-Hill, 1998.")
C_MEMSHB = ("Gad-el-Hak, Mohamed (ed.). 'The MEMS Handbook'. 2nd ed. CRC "
            "Press, 2006.")
C_SITTI = ("Sitti, Metin. 'Mobile Microrobotics'. MIT Press, 2017.")
C_NELSON = ("Nelson, Bradley J., Kaliakatsos, Ioannis K., and Abbott, Jake J. "
            "'Microrobots for Minimally Invasive Medicine'. Annual Review of "
            "Biomedical Engineering, Vol. 12, 2010.")
C_PURCELL = ("Purcell, Edward M. 'Life at Low Reynolds Number'. American "
             "Journal of Physics, Vol. 45, No. 1, 1977.")
C_FEYNMAN = ("Feynman, Richard P. 'There\\u2019s Plenty of Room at the "
             "Bottom'. Lecture at the California Institute of Technology, "
             "December 29, 1959.")
C_JUDY = ("Judy, Jack W. 'Microelectromechanical Systems (MEMS): "
          "Fabrication, Design and Applications'. Smart Materials and "
          "Structures, Vol. 10, No. 6, 2001.")
C_DILLER = ("Diller, Eric and Sitti, Metin. 'Micro-Scale Mobile Robotics'. "
            "Foundations and Trends in Robotics, Vol. 2, No. 3, 2013.")
C_HOWELL = ("Howell, Larry L. 'Compliant Mechanisms'. Wiley, 2001.")
C_PISTER = ("Pister, Kristofer S. J., Judy, Michael W., Burgett, Stephen R., "
            "and Fearing, Ronald S. 'Microfabricated Hinges'. Sensors and "
            "Actuators A, Vol. 33, No. 3, 1992.")
C_WOOD = ("Ma, Kevin Y., Chirarattananon, Pakpong, Fuller, Sawyer B., and "
          "Wood, Robert J. 'Controlled Flight of a Biologically Inspired, "
          "Insect-Scale Robot'. Science, Vol. 340, No. 6132, 2013.")
C_WHITESIDES = ("Whitesides, George M. and Grzybowski, Bartosz. "
                "'Self-Assembly at All Scales'. Science, Vol. 295, No. 5564, "
                "2002.")
C_RUBENSTEIN = ("Rubenstein, Michael, Cornejo, Alejandro, and Nagpal, "
                "Radhika. 'Programmable Self-Assembly in a Thousand-Robot "
                "Swarm'. Science, Vol. 345, No. 6198, 2014.")
C_KUMMER = ("Kummer, Michael P., Abbott, Jake J., Kratochvil, Bradley E., "
            "Borer, Reinoud, Sengul, Ali, and Nelson, Bradley J. 'OctoMag: An "
            "Electromagnetic System for 5-DOF Wireless Micromanipulation'. "
            "IEEE Transactions on Robotics, Vol. 26, No. 6, 2010.")
C_ISO13485 = ("ISO 13485: Medical devices - Quality management systems for "
              "regulatory purposes.")
C_IEEE2700 = ("IEEE 2700-2017: Standard for Sensor Performance Parameter "
              "Definitions.")
C_SEMI = ("SEMI Standards: process, materials, and handling specifications "
          "for microfabrication.")
C_ISO8373 = ("ISO 8373: Robotics - Vocabulary.")

ENTRIES = [
{
"key": "what_is_microrobotics",
"name": "What Is Microrobotics: Robots Smaller Than a Grain of Sand",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Microrobotics is the discipline of designing, building, and controlling "
"robots whose characteristic size runs from about a centimetre down to a "
"micrometre - machines you can lose on your fingertip. A 1-millimetre cube "
"of silicon weighs just 2.33 milligrams and feels a gravitational pull of "
"only about 23 micronewtons, yet its surface-to-volume ratio is 6,000 per "
"metre - a thousand times that of a 1-metre cube. That single fact rewrites "
"the rules: surface forces (electrostatics, surface tension, adhesion, "
"viscous drag) dominate, while weight and inertia fade into the background. "
"Microrobotics draws its bodies from micro-electro-mechanical systems "
"(MEMS), its muscles from electrostatic, piezoelectric, thermal, magnetic, "
"chemical, and biological actuators, its senses from micro-sensors, and its "
"factories from semiconductor microfabrication. Its applications run from "
"drug-delivering swimmers inside the bloodstream to insect-scale flying "
"robots, pipeline inspectors, and self-assembling micro-factories. This "
"database teaches the discipline from that first scaling insight through "
"actuation, sensing, power, locomotion, control, and the medical, "
"industrial, and scientific applications that justify the field."),
"how_it_works": (
"A microrobot is a complete robot shrunk until physics changes its mind. "
"The body is usually etched or deposited from silicon, polymers, or thin "
"films using the same lithography and etching tools that make computer "
"chips. Because the machine is tiny, its actuators exploit forces that are "
"negligible at human scale: a voltage across a micrometre gap pulls with "
"micronewtons (electrostatic), a magnetic field gradient drags a "
"micrometre magnet harder than gravity pulls it (magnetic), a catalyst "
"coating turns fuel into bubbles that push (chemical), and living cells "
"can be harnessed as engines (biohybrid). Sensing is done with "
"micro-machined capacitors, piezoresistors, and optics, and control "
"happens either on board (for the larger millibots) or from outside - "
"magnetic fields, light, ultrasound, or chemical gradients steering robots "
"too small to carry a computer. Every record in this database is one piece "
"of that shrunken machine: one scaling law, one actuator, one sensor, one "
"power strategy, one way of moving, one application."),
"key_points": [
"Microrobotics spans roughly 10 mm down to 1 um; below that lies nanorobotics.",
"A 1 mm silicon cube weighs 2.33 mg and feels 22.9 uN of gravity - surface forces rule.",
"Surface-to-volume ratio at 1 mm is 6,000 per metre, 1,000x that of a 1 m cube.",
"Bodies come from MEMS; muscles from electrostatic, piezoelectric, thermal, magnetic, chemical, and biological actuation.",
"Control is often external (fields, light, ultrasound) because onboard computers do not fit.",
"Applications: medicine (drug delivery, surgery), inspection, micro-assembly, environmental sensing, science.",
],
"requirements": [
"No prerequisites - this record introduces the discipline.",
"A calculator for the scaling exercises in the demo.",
"Familiarity with basic physics units (newtons, metres, kilograms).",
],
"standards": [
"ISO 8373 (robotics vocabulary) frames what counts as a robot at any scale.",
"SEMI standards govern the microfabrication processes microrobot bodies are built with.",
"IEEE 2700-2017 defines how micro-sensor performance is specified.",
],
"citations": [C_SITTI, C_DILLER, C_FEYNMAN],
"sig_lens": (
"Signature take: the microrobot is the Signature machine in miniature - "
"proof that intelligence is not size but organization. Where big robots "
"fight gravity with motors, the Signature microrobot recruits the forces "
"the big world ignores: the cling of surfaces, the push of fields, the "
"swim of chemistry. Small is not a limitation to overcome; it is a "
"different physics to befriend."),
},
{
"key": "scale_map",
"name": "The Micro-Scale Map: From Millibots to Nanobots",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"The micro-scale is not one place but a ladder of regimes, and each rung "
"has its own physics. Millibots (roughly 1 to 10 mm) still carry batteries, "
"motors, and microcontrollers - they are conventional robots, just small. "
"Microrobots (roughly 100 um to 1 mm) sit at the crossover: too small for "
"ordinary motors, large enough for MEMS actuators, and dominated by "
"surface forces. Below about 100 um, viscous forces crush inertia - a "
"10-micrometre swimmer moving at 10 um/s in water operates at a Reynolds "
"number of 0.0001, four orders of magnitude below a 1 mm robot at 1 mm/s "
"(Re = 1), and ten orders below a human swimmer (Re ~ 2,000,000). At that "
"point the fluid feels like thick honey and coasting is impossible: stop "
"pushing and you stop instantly. Nanorobots (below about 1 um) live where "
"Brownian motion - the random shove of molecules - is a design load, not "
"noise. This record maps the ladder so every later record can name which "
"rung it stands on."),
"how_it_works": (
"The map is drawn with dimensionless numbers. The Reynolds number "
"Re = density x speed x size / viscosity tells whether inertia or viscosity "
"rules the fluid around the robot: above Re ~ 1,000 the robot can coast and "
"glide; below Re ~ 1, every motion must be continuously powered and "
"reciprocal motions (like a scallop opening and closing) produce zero net "
"travel. The Bond number compares gravity to surface tension, and the "
"capillary length of water - 2.7 mm - marks where droplets stop sagging and "
"start clinging. The Peclet number weighs directed motion against diffusion: "
"when it falls below 1, the robot wanders randomly faster than it swims "
"purposefully. Engineers read these numbers the way sailors read charts - "
"they say which propulsion works, which sensing is possible, and whether "
"the robot may carry its own power or must be fed from outside."),
"key_points": [
"Millibots (1-10 mm): conventional robots, carry batteries and computers.",
"Microrobots (100 um-1 mm): MEMS actuators, surface forces dominate.",
"Re = 1 for a 1 mm robot at 1 mm/s in water; Re = 0.0001 for a 10 um swimmer.",
"Human swimmer Re ~ 2,000,000 - ten orders of magnitude above the micro-swimmer.",
"Below Re ~ 1 there is no coasting; below Pe ~ 1 diffusion beats swimming.",
"Nanorobots (<1 um) must treat Brownian motion as a design load.",
],
"requirements": [
"The 'What Is Microrobotics' record (the discipline overview).",
"Basic fluid concepts: density, viscosity.",
"A calculator for the Reynolds-number exercises.",
],
"standards": [
"ISO 8373 (robotics vocabulary) applies across all size rungs.",
"Standard fluid-property tables (water: density 1000 kg/m3, viscosity 1 mPa s).",
],
"citations": [C_PURCELL, C_SITTI, C_DILLER],
"sig_lens": (
"Signature take: the scale map is a ladder of worlds, and the Signature "
"engineer climbs it the way a mountaineer reads weather - each altitude has "
"its own air. The Signature microrobot never fights the rung it stands on; "
"it is designed for exactly one rung, the way a fish is designed for water "
"and not for air."),
},
{
"key": "scaling_laws",
"name": "Scaling Laws at Small Sizes: Why Surface Beats Volume",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Scaling laws are the master equations of microrobotics: they predict how "
"every force, speed, and energy changes when a design shrinks. Volume "
"forces - weight, inertia, stored chemical energy - scale with the cube of "
"size (L^3). Surface forces - muscle-like actuator force, friction, viscous "
"drag, surface tension, electrostatic pull - scale with the square (L^2). "
"Their ratio therefore scales as 1/L: shrink by 1,000 and surface forces "
"become 1,000 times more important relative to weight. That is why an ant "
"lifts many times its body weight while an elephant cannot, and why a "
"microrobot can be yanked around by a magnet yet barely notices gravity. "
"Time scales too: a smaller resonator rings faster (frequency ~ 1/L), heat "
"escapes faster (cooling time ~ L^2), and diffusion crosses the robot sooner "
"(time ~ L^2). A 1-micrometre particle in water wanders about 0.66 um in one "
"second by Brownian motion alone - comparable to its own size, a random walk "
"no macro engineer ever budgets for. Learn the exponents and the whole "
"discipline becomes predictable."),
"how_it_works": (
"Write any quantity as a power of the characteristic length L and the "
"design trade-offs appear. Actuator force from muscles or electrostatics "
"grows as L^2 while the mass it must move grows as L^3, so acceleration "
"capability (force/mass) grows as 1/L - small robots are violently agile. "
"But stored energy grows as L^3 while power-hungry tasks like radio "
"transmission scale worse, so endurance collapses with size. Surface "
"tension forces (~ L) beat weight (~ L^3) below the capillary length of "
"2.7 mm for water, which is why micro-parts cling instead of falling. "
"Electrostatic force per unit area is scale-invariant (it depends on field, "
"not size), so shrinking the gap multiplies force density - the reason "
"electrostatic comb drives are the workhorse micro-actuator. The demo "
"computes these crossovers numerically: the capillary length, the Brownian "
"wander, and the force-ratio flip."),
"key_points": [
"Volume quantities scale as L^3; surface quantities as L^2; their ratio as 1/L.",
"Below the 2.7 mm capillary length of water, surface tension beats gravity.",
"Electrostatic force density is scale-invariant - shrinking the gap multiplies force.",
"Agility (force/mass) grows as 1/L: small robots accelerate harder.",
"Endurance collapses with size: stored energy falls as L^3.",
"A 1 um particle wanders ~0.66 um per second by Brownian motion alone.",
],
"requirements": [
"The micro-scale map (which rung each law applies to).",
"Algebra with powers and scientific notation.",
"A calculator for the crossover exercises.",
],
"standards": [
"Standard physical constants (surface tension of water 0.072 N/m, Boltzmann constant).",
"Scaling analysis follows Buckingham-Pi dimensional practice.",
],
"citations": [C_SENTURIA, C_PURCELL, C_FEYNMAN],
"sig_lens": (
"Signature take: scaling laws are the Signature engineer's oracle - ask "
"what happens at a tenth the size and the exponents answer before any "
"prototype is built. Signature design begins with the exponent, not the "
"drawing: choose the physics that gets stronger as you shrink, and refuse "
"the physics that gets weaker."),
},
{
"key": "mems_body",
"name": "MEMS: The Micro-Electro-Mechanical Body of the Microrobot",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"MEMS - micro-electro-mechanical systems - are the bodies microrobots are "
"built from: mechanical structures (beams, membranes, gears, mirrors) "
"etched into silicon at the micrometre scale, with electronics integrated "
"on the same chip. A silicon cantilever 500 um long, 50 um wide, and 2 um "
"thick has a stiffness of only 0.135 N/m - soft as a spider's thread - yet "
"rings at 5.4 kHz and sags just 8.5 nanometres under its own weight. That "
"combination (soft, fast, weightless-feeling) is the MEMS signature. The "
"same processes make accelerometers (the airbag sensor in cars), pressure "
"sensors, micromirrors (in projectors), and the comb-drive actuators that "
"move microrobot limbs. Silicon is the structural material of choice: "
"single-crystal silicon has a yield strength near 7 GPa - stronger per "
"weight than steel - and at the micro-scale it is nearly perfect, with no "
"room for the dislocations that weaken large crystals. This record is the "
"anatomy lesson: beams, springs, masses, and hinges in silicon."),
"how_it_works": (
"A MEMS body starts as a silicon wafer and is sculpted by adding thin "
"films (deposition) and removing material (etching) through patterned masks "
"(lithography). A cantilever beam bends with stiffness k = 3EI/L^3, where E "
"is Young's modulus (169 GPa for silicon), I the second moment of area, and "
"L the length; its mass m = density x volume sets the resonant frequency "
"f = (1/2pi) sqrt(k/m). Designers tune L, width, and thickness to place "
"stiffness, frequency, and travel where the robot needs them: soft springs "
"for sensitive accelerometers, stiff beams for fast mirrors. Moving parts "
"are freed by etching away a sacrificial layer beneath them (surface "
"micromachining) or by etching deep trenches from the back (bulk "
"micromachining). Electrical signals reach the mechanics through doped "
"silicon or metal traces, so sensing and actuation live on the same chip as "
"the structure they serve."),
"key_points": [
"MEMS = micrometre-scale mechanical structures integrated with electronics on silicon.",
"A 500x50x2 um silicon cantilever: k = 0.135 N/m, f0 = 5.4 kHz, self-sag 8.5 nm.",
"Single-crystal silicon yields near 7 GPa - stronger per weight than steel.",
"Surface micromachining frees parts by removing a sacrificial layer; bulk etches deep shapes.",
"Same technology family: airbag accelerometers, projector micromirrors, pressure sensors.",
"Stiffness scales as 1/L^3: halving length stiffens a beam eightfold.",
],
"requirements": [
"Scaling laws (why small beams are stiff and fast).",
"Basic beam-bending concepts (stiffness, resonance).",
"A calculator for the cantilever exercises.",
],
"standards": [
"SEMI standards for wafer dimensions, flatness, and handling.",
"IEEE 2700-2017 for reporting MEMS sensor performance.",
"Silicon material data per standard references (E = 169 GPa, density 2330 kg/m3).",
],
"citations": [C_MALUF, C_SENTURIA, C_KOVACS, C_JUDY],
"sig_lens": (
"Signature take: the MEMS body is the Signature skeleton - silicon carved "
"with the patience of a chipmaker and the intent of a watchmaker. "
"Signature MEMS treats the wafer as a block of marble and the etch as a "
"chisel: the robot was always inside the silicon, and fabrication is the "
"art of freeing it without breaking its spirit."),
},
{
"key": "microfabrication",
"name": "Microfabrication: Lithography, Etching, and Building Tiny Machines",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Microfabrication is the manufacturing discipline behind every microrobot: "
"the set of processes that patterns, deposits, and etches materials with "
"micrometre precision. Photolithography projects a mask pattern onto "
"light-sensitive photoresist; with 365 nm ultraviolet light and a 0.5 "
"numerical-aperture lens, features as small as 0.45 um resolve - finer than "
"a bacterium. Etching then transfers the pattern into the material: wet "
"etching dissolves, dry (plasma) etching bombards, and deep reactive-ion "
"etching (DRIE) carves trenches hundreds of micrometres deep at about 10 um "
"per minute - a 500 um wafer etches through in roughly 50 minutes. "
"Deposition adds films (metals, oxides, piezoelectrics) atom by atom. LIGA "
"(lithography, electroplating, molding) builds tall metal microstructures, "
"and soft lithography stamps patterns in rubber-like PDMS for microfluidics. "
"Economics favour the batch: one 150 mm wafer holds roughly 700 dice of "
"5x5 mm, so a thousand robots can be born in a single etch run. This record "
"covers the process flow from bare wafer to freed microrobot."),
"how_it_works": (
"A typical surface-micromachining flow runs like this: grow or deposit a "
"sacrificial layer (often silicon dioxide), deposit the structural layer "
"(polysilicon), pattern it with lithography, etch the pattern, repeat for "
"multiple mechanical layers, then dissolve the sacrificial oxide in "
"hydrofluoric acid to free the moving parts - the microrobot equivalent of "
"removing scaffolding. Bulk micromachining instead etches the wafer itself, "
"using potassium hydroxide (which stops on crystal planes, making perfect "
"V-grooves and pyramids) or DRIE (which makes vertical walls of any shape). "
"Each lithography step aligns to the last within a fraction of a micrometre; "
"misalignment stacks into tolerance budgets the designer must respect. "
"After release, parts are dried supercritically or with anti-stiction "
"coatings so surface tension does not glue them down - at this scale, a "
"drying droplet is a wrecking ball."),
"key_points": [
"Photolithography at 365 nm resolves ~0.45 um features - finer than a bacterium.",
"DRIE etches ~10 um/min: a 500 um wafer etches through in ~50 min.",
"One 150 mm wafer yields ~700 dice of 5x5 mm - batch economics favour microrobots.",
"Sacrificial-layer release frees moving parts; supercritical drying defeats stiction.",
"KOH etches silicon along crystal planes; DRIE makes arbitrary vertical walls.",
"LIGA builds tall metal microstructures; soft lithography patterns PDMS microfluidics.",
],
"requirements": [
"MEMS bodies (what the processes are building).",
"Basic chemistry ideas: acids dissolve, plasmas bombard.",
"A calculator for the wafer-yield and etch-time exercises.",
],
"standards": [
"SEMI standards for photoresist, etchants, and wafer specifications.",
"Cleanroom classifications (ISO 14644) for fabrication environments.",
],
"citations": [C_MADOU, C_MALUF, C_MEMSHB],
"sig_lens": (
"Signature take: microfabrication is Signature manufacturing - a thousand "
"robots per wafer, each identical, each perfect, born in parallel. The "
"Signature fab does not assemble robots; it grows them the way a crystal "
"grows, layer by layer, and releases them like fledglings when the "
"scaffolding dissolves."),
},
{
"key": "micro_materials",
"name": "Materials at the Micro-Scale: Silicon, Polymers, and Smart Films",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"The materials of microrobotics are chosen for what they do, not just what "
"they are. Single-crystal silicon is the structural workhorse: stiff "
"(169 GPa), light (2330 kg/m3), and nearly flawless at small sizes, with a "
"yield strength approaching 7 GPa. Polysilicon adds patternable mechanical "
"layers; silicon nitride makes hard masks and membranes; silicon dioxide is "
"the sacrificial layer that disappears on command. Polymers bring "
"compliance: SU-8 photoresist builds tall, stiff microstructures directly "
"from lithography, while PDMS (silicone rubber) makes soft microfluidic "
"channels and flexible skins. Smart films add function: piezoelectric films "
"(PZT, AlN, ZnO) turn voltage into motion, shape-memory alloys (nitinol) "
"remember a shape and snap back when heated, and magnetic films (NiFe, "
"NdFeB) let external fields grab the robot. The catch is mismatch: an "
"aluminium film on silicon, heated 100 K, develops about 143 MPa of thermal "
"stress from the expansion difference - enough to curl a beam into a "
"potato chip. Material selection in microrobotics is stress management as "
"much as property shopping."),
"how_it_works": (
"Each material earns its place by a transduction or structural job. "
"Piezoelectric films strain when voltage is applied (the direct route to "
"micro-muscles); the strain is small (fractions of a percent) but the force "
"is large and the response is fast (kilohertz to megahertz). Shape-memory "
"alloy films deliver huge work per volume by a heat-triggered crystal phase "
"change - slow, but enormously strong for their size. Magnetic films couple "
"to external fields with no wires at all. Polymers trade stiffness for "
"toughness and biocompatibility: a PDMS channel will not crack where "
"silicon would shatter, and SU-8 structures survive handling that kills "
"bare silicon. The designer stacks these as thin films, and every interface "
"is a potential failure: thermal-expansion mismatch bends stacks, residual "
"deposition stress curls released beams, and galvanic pairs corrode in "
"bodily fluids. Choosing materials means choosing which stresses you can "
"live with."),
"key_points": [
"Single-crystal silicon: 169 GPa stiff, ~7 GPa strong, nearly flawless at micro-scale.",
"SU-8 builds tall polymer microstructures; PDMS makes soft, biocompatible microfluidics.",
"Piezoelectric films (PZT/AlN) turn voltage into fast, forceful micro-motion.",
"Nitinol shape-memory films deliver huge work density via heat-triggered phase change.",
"Magnetic films (NdFeB) allow completely wireless force coupling.",
"Al on Si heated 100 K -> ~143 MPa thermal stress: mismatch management is mandatory.",
],
"requirements": [
"Microfabrication (how films are deposited and patterned).",
"Basic ideas of stress, strain, and thermal expansion.",
"A calculator for the thermal-stress exercise.",
],
"standards": [
"SEMI materials specifications for electronic-grade silicon and thin films.",
"ASTM thin-film mechanical testing practices.",
],
"citations": [C_MADOU, C_KOVACS, C_MEMSHB],
"sig_lens": (
"Signature take: materials are the Signature alphabet - silicon the "
"consonants, polymers the vowels, smart films the punctuation that makes "
"the structure speak. The Signature material stack is chosen the way a "
"poet chooses words: each film must earn its place, and the stresses "
"between them must resolve into harmony, not war."),
},
{
"key": "electrostatic_actuation",
"name": "Electrostatic Actuation: Comb Drives and the Pull-In Limit",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"Electrostatic actuation is the workhorse muscle of microrobotics: it moves "
"parts with the attraction between charged plates, needs no coils or "
"magnets, and is built with the same lithography as the structure itself. "
"A comb drive - two interleaved rows of micrometre fingers - pulls with a "
"force F = N x epsilon0 x h x V^2 / g: with 100 fingers, 10 um finger "
"height, a 2 um gap, and 50 volts, that is 11.1 micronewtons, enough to "
"drive shutters, mirrors, grippers, and micro-engines. The force density "
"grows as the gap shrinks, which is exactly why electrostatics loves the "
"micro-scale. The price is voltage (tens to hundreds of volts for useful "
"force) and the pull-in instability: a parallel-plate actuator pulled past "
"one-third of its gap snaps shut uncontrollably. For plates of 1 mm2 area, "
"a 5 um gap, and a 10 N/m suspension, pull-in strikes at just 6.5 volts - "
"the designer must either stay below it or exploit the snap as a digital "
"switch. This record covers comb drives, parallel plates, scratch drives, "
"and the stability math that keeps them honest."),
"how_it_works": (
"Apply a voltage V across a gap g and the plates attract with a force "
"proportional to V^2 - double the voltage, quadruple the force. In a "
"lateral comb drive the capacitance changes linearly with engagement, so "
"the force is constant with displacement: ideal for smooth, controllable "
"motion over tens of micrometres. In a parallel-plate (gap-closing) "
"actuator the force grows as 1/g^2, so as the plate moves the pull "
"strengthens - past the one-third-gap point the spring can no longer hold "
"back and the plate slams shut (pull-in). Engineers dodge this with "
"leveraged bending, shaped electrodes, or charge (rather than voltage) "
"control. Scratch drives and inchworm motors chain many small electrostatic "
"steps into long travel, the way an inchworm chains small bends into a "
"journey. All of it runs on electric fields alone: no current, almost no "
"heat, just voltage and geometry."),
"key_points": [
"Comb drive: F = N*eps0*h*V^2/g; 100 fingers at 50 V -> 11.1 uN.",
"Force density grows as the gap shrinks - electrostatics favours the micro-scale.",
"Pull-in: a parallel plate snaps shut past one-third of its gap (6.5 V in the worked example).",
"Comb drives give constant force vs displacement; gap-closing gives 1/g^2 force.",
"Price: tens to hundreds of volts; benefit: no current, no heat, lithography-compatible.",
"Scratch drives and inchworms chain small steps into long travel.",
],
"requirements": [
"MEMS bodies (the suspensions the actuators pull against).",
"Capacitance basics: C = eps0*A/g.",
"A calculator for the force and pull-in exercises.",
],
"standards": [
"High-voltage handling practice for >50 V MEMS drive (isolation, creepage).",
"IEEE 2700-2017 for specifying actuator displacement performance.",
],
"citations": [C_SENTURIA, C_MALUF, C_KOVACS],
"sig_lens": (
"Signature take: the comb drive is the Signature handshake - a hundred "
"tiny fingers interlacing, pulling with pure voltage, never touching. "
"Signature electrostatic design treats the air gap as sacred: the smaller "
"the gap, the stronger the grip, and pull-in is not a failure but a promise "
"kept too eagerly - the plates simply could not resist each other."),
},
{
"key": "piezoelectric_actuation",
"name": "Piezoelectric Actuation: Bending Tiny Muscles with Voltage",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"Piezoelectric actuation turns voltage directly into strain: apply a field "
"to a PZT or aluminium-nitride film and the crystal lattice shears by a "
"fraction of a percent, fast (kilohertz to megahertz) and forceful. The "
"strain is small, so microrobots amplify it with bimorphs - two active "
"layers bonded back to back, one expanding while the other contracts, "
"curling like a bimetallic strip. A 2 mm long, 0.2 mm thick PZT bimorph "
"deflects about 27 nanometres per volt, so 50 volts buys 1.35 um of tip "
"motion - enough for micro-grippers, scanning mirrors, and the wing hinges "
"of insect-scale flying robots. Piezoelectrics also work in reverse: bend "
"them and they generate voltage, which makes them sensors as well as "
"muscles (the same film can drive and listen). Compared with "
"electrostatics they need lower voltage and deliver higher force density, "
"but the travel is short and the ceramics are brittle - design around "
"amplification levers and compliant hinges, never around brute bending of "
"the crystal itself."),
"how_it_works": (
"The piezoelectric coefficients (d31 for in-plane strain from a through-"
"thickness field, d33 for through-thickness) convert electric field to "
"mechanical strain: strain = d x field. In a bimorph the differential "
"strain between layers becomes curvature, and curvature integrated over "
"length becomes tip deflection: deflection ~ (3/2) x d31 x (L/t)^2 x V, so "
"long thin bimorphs move far. Stack actuators trade travel for force "
"(many thin layers in series electrically, in parallel mechanically), "
"tube scanners bend in two axes for microscope positioning, and ultrasonic "
"motors rectify microscopic piezo vibrations into continuous rotation. "
"Drive is capacitive - current flows only while the voltage changes - so "
"holding a position costs almost no power. Hysteresis and creep (the "
"ceramic remembers its past) are tamed with charge control or closed-loop "
"sensing, often using the piezo element itself as the sensor."),
"key_points": [
"PZT bimorph 2 mm x 0.2 mm: ~27 nm/V; 50 V -> 1.35 um tip deflection.",
"Fast (kHz-MHz), forceful, low holding power - but short travel and brittle.",
"Deflection scales as (L/t)^2: long thin bimorphs move far.",
"Reversible: the same film senses (bend -> voltage) and actuates.",
"Stacks trade travel for force; tubes scan in two axes.",
"Hysteresis and creep tamed by charge control or closed-loop feedback.",
],
"requirements": [
"Micro-scale materials (PZT/AlN films and their brittleness).",
"Basic ideas of strain, curvature, and capacitors.",
"A calculator for the bimorph deflection exercise.",
],
"standards": [
"IEEE 176 (piezoelectricity standard) for coefficients and measurement.",
"High-voltage practice for piezo drive waveforms.",
],
"citations": [C_KOVACS, C_MEMSHB, C_WOOD],
"sig_lens": (
"Signature take: the piezo film is the Signature muscle that never tires "
"of holding still - voltage in, shape out, and holding the pose costs "
"nothing. Signature piezo design is leverage thinking: the crystal gives a "
"whisper of strain and the bimorph geometry turns it into a shout of "
"motion."),
},
{
"key": "thermal_actuation",
"name": "Thermal Actuation: Heat as a Micro-Muscle",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"Thermal actuation is the simplest micro-muscle: run current through a "
"beam, it heats, expands, and pushes. A chevron (bent-beam) actuator turns "
"that tiny expansion into useful motion with geometry - two beams meeting "
"at a shallow 5-degree angle convert 0.39 um of thermal expansion (a 500 um "
"silicon beam heated 300 K) into 4.5 um of apex displacement, an "
"amplification of more than 11 times, with millinewton forces behind it. "
"Thermal actuators are the strongmen of MEMS: large force, large "
"displacement, trivially fabricated from a single layer - at the price of "
"power (about 0.125 W for a 5 V, 200-ohm heater) and speed (milliseconds to "
"heat and cool, versus microseconds for electrostatics). They also run hot, "
"which rules them out near living tissue or temperature-sensitive cargo. "
"Use them where force matters more than efficiency: micro-relays, optical "
"switches, grippers that must hold hard, and one-shot deployment mechanisms "
"that fire once and latch."),
"how_it_works": (
"Joule heating (P = V^2/R) raises the beam temperature; thermal expansion "
"(delta-L = alpha x L x delta-T) lengthens it; the chevron geometry resolves "
"that lengthening mostly into sideways motion at the apex, amplified by "
"1/tan(angle). Hot-arm/cold-arm (U-shaped) actuators bend instead: one arm "
"heats and expands while the other stays cool, curling the tip sideways. "
"Bimorph thermal actuators pair materials with different expansion "
"coefficients for out-of-plane curling. The thermal time constant - set by "
"the beam's heat capacity and its conduction paths - fixes the speed limit: "
"thin beams in good thermal contact cycle in milliseconds; the same physics "
"that makes them slow makes them strong, because the whole beam volume "
"works as muscle. Designers pulse the drive (short hot bursts, long cool "
"rests) to manage average power, and add heat sinks or isolation trenches "
"where neighbours must stay cool."),
"key_points": [
"Chevron (500 um, 5 deg, dT=300 K): 0.39 um expansion -> 4.5 um motion, ~11x amplification.",
"Millinewton forces from a single lithography layer - the strongman actuator.",
"Price: ~0.1 W power draw and millisecond speed (heat/cool cycles).",
"Runs hot: unsuitable near tissue or temperature-sensitive cargo.",
"Hot-arm/cold-arm bends; bimorphs curl out of plane.",
"Pulse the drive and isolate neighbours thermally.",
],
"requirements": [
"Micro-scale materials (thermal expansion coefficients).",
"Joule heating and basic heat-transfer ideas.",
"A calculator for the chevron amplification exercise.",
],
"standards": [
"Thermal management practice for packaged MEMS (derating, heat paths).",
"SEMI packaging standards for power dissipation.",
],
"citations": [C_MALUF, C_MEMSHB, C_JUDY],
"sig_lens": (
"Signature take: the thermal actuator is the Signature strongman - slow, "
"hungry, and honest, turning electricity into heat into push with no "
"pretense of elegance. Signature thermal design respects the fire: give it "
"room to breathe, pulse it like a heartbeat, and never ask it to work "
"beside anything that fears warmth."),
},
{
"key": "magnetic_actuation",
"name": "Magnetic Actuation: Steering Untethered Microrobots with Fields",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Magnetic actuation is how microrobots move with no wires, no batteries, "
"and no onboard motors: an external field grabs a magnetic body and steers "
"it from across the room - or across the body. A 100 um cube of NdFeB "
"magnet (magnetization ~1e6 A/m) carries a magnetic moment of 1e-6 A m2; "
"in a 10 mT field it feels a torque of 1e-8 N m, and in a 1 T/m gradient a "
"pull of 1 micronewton - about 14 times its own weight. Torque (moment "
"cross field) rotates the robot; gradient force (moment dot field-gradient) "
"translates it. Systems like the OctoMag use eight electromagnets to steer "
"a microrobot with five degrees of freedom inside the eye or the "
"bloodstream. Because fields penetrate tissue harmlessly, magnetic drive is "
"the leading choice for medical microrobots. The trade-offs: the workspace "
"needs the coil array, control must invert the field-to-motion map in real "
"time, and ferromagnetic surroundings distort the field - steer in a steel "
"pipe and the pipe steers back."),
"how_it_works": (
"A uniform field aligns the robot's magnetization like a compass needle - "
"that gives orientation control (3 rotational degrees). A field gradient "
"pulls the magnet toward stronger field - that gives position control. "
"Combine rotating uniform fields with a helical robot body and the helix "
"swims like a corkscrew (the bacterial flagellum trick); oscillate the "
"field and a flexible tail beats. The controller computes the currents for "
"each coil from the desired field and gradient at the robot's position "
"(the actuation matrix inverse), updates at tens of hertz from camera "
"feedback, and closes the loop. Scaling favours magnets: torque scales "
"with volume (L^3) while viscous drag torque scales roughly with L^3 as "
"well, so magnetic swimmers keep working down to the micrometre scale - "
"unlike motors, which die of friction long before."),
"key_points": [
"100 um NdFeB cube: 1e-8 N m torque in 10 mT; 1 uN pull in 1 T/m (~14x its weight).",
"Uniform field -> orientation; gradient -> translation; rotating field + helix -> swimming.",
"OctoMag-style coil arrays give 5-DOF wireless manipulation (Kummer et al. 2010).",
"Fields penetrate tissue: the leading drive for medical microrobots.",
"Magnetic scaling survives to micrometres where motors die of friction.",
"Steel surroundings distort fields - the workspace must be magnetically clean.",
],
"requirements": [
"Scaling laws (why magnets beat motors at small size).",
"Basic magnetism: torque = moment cross field.",
"A calculator for the torque/force exercises.",
],
"standards": [
"IEC 60601 for magnetic-field medical device safety (exposure limits).",
"Electromagnetic compatibility practice for coil-drive electronics.",
],
"citations": [C_KUMMER, C_NELSON, C_SITTI],
"sig_lens": (
"Signature take: magnetic drive is Signature telekinesis - the hand never "
"touches the puppet, yet the puppet dances. The Signature magnetic "
"microrobot carries nothing but a speck of magnet and a clever shape; all "
"the intelligence lives in the field outside, conducting an orchestra it "
"never joins."),
},
{
"key": "micro_sensors",
"name": "Micro-Sensors: How Microrobots Feel the World",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"A microrobot that cannot sense is just a projectile, so micro-sensors are "
"its eyes, ears, and fingertips. The capacitive accelerometer is the "
"classic: a micromachined proof mass on springs shifts between fixed "
"plates, and the capacitance change reports acceleration. With 1 mm2 "
"plates, a 2 um gap (C0 = 4.43 pF), a 1-microgram mass, and 1 N/m springs, "
"one g of acceleration moves the mass 9.8 nm and changes the capacitance by "
"21.7 femtofarads - a signal modern electronics reads easily - while the "
"structure resonates at 5.0 kHz, far above the motion it measures. "
"Piezoresistive sensors read strain as resistance change (pressure sensors, "
"force-sensing gripper jaws); piezoelectric films read vibration; thermal "
"sensors read flow; and micro-optics plus cameras give vision. The "
"fundamental limit is Brownian noise: the air molecules battering the proof "
"mass set a floor no amplifier can beat, so the quietest sensors work in "
"vacuum packages. This record covers transduction principles, noise floors, "
"and what a microrobot can actually perceive."),
"how_it_works": (
"Every micro-sensor is a transduction chain: physical quantity -> "
"mechanical response -> electrical signal. Capacitive sensing converts "
"displacement to capacitance (delta-C/C = displacement/gap) and is read "
"with bridge or switched-capacitor circuits that reject drift. "
"Piezoresistors (doped silicon, gauge factor ~100) turn strain into "
"resistance for pressure diaphragms and force probes. Resonant sensors "
"watch a frequency shift instead of an amplitude: a mass landing on a "
"resonating beam detunes it, giving exquisite sensitivity for chemical and "
"biological detection. The mechanical-thermal noise floor comes from the "
"damping that also limits the quality factor - less damping means less "
"noise but slower response, the eternal sensor trade. Calibration trims "
"offset and scale factor; temperature compensation trims the drift; and "
"packaging (often vacuum) sets the final noise floor the robot must live "
"with."),
"key_points": [
"Capacitive accel example: 4.43 pF, 1 g -> 9.8 nm -> 21.7 fF; f0 = 5.0 kHz.",
"Transduction chain: physical -> mechanical -> electrical.",
"Piezoresistive (strain->resistance), piezoelectric (vibration), resonant (frequency-shift) sensing.",
"Brownian noise sets the fundamental floor; vacuum packaging lowers it.",
"Trade: less damping = less noise but slower response.",
"Calibration trims offset/scale; temperature compensation trims drift.",
],
"requirements": [
"MEMS bodies (springs, masses, resonators).",
"Capacitance and resistance basics.",
"A calculator for the accelerometer exercise.",
],
"standards": [
"IEEE 2700-2017: the standard language for sensor performance parameters.",
"Calibration traceability per ISO/IEC 17025 practice.",
],
"citations": [C_KOVACS, C_MALUF, C_SENTURIA],
"sig_lens": (
"Signature take: the micro-sensor is the Signature sense organ - a "
"proof mass that feels the world the way an inner ear does, a capacitor "
"that listens for nanometres. Signature sensing never shouts over noise; "
"it quiets the room (vacuum packaging, careful electronics) until the "
"whisper of the signal is the loudest thing left."),
},
{
"key": "micro_power",
"name": "Powering Micro-Robots: Batteries, Capacitors, and the Energy Problem",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Power is the cruellest scaling law in microrobotics: energy storage "
"shrinks with volume (L^3) while the jobs stay hungry. A 1-cubic-millimetre "
"thin-film battery holds roughly 1 joule - enough to run a 1-milliwatt "
"microrobot for about 18 minutes. A 1-millifarad capacitor at 3 volts holds "
"just 4.5 millijoules: 4.5 seconds at the same draw. And the power "
"electronics (voltage converters, regulators) refuse to shrink as fast as "
"the load, eating a growing share of the budget. This is why the field "
"splits: millibots carry real batteries and run real missions, while true "
"microrobots usually take power from outside - magnetic fields, light, "
"ultrasound, or chemical fuel in the environment. Energy harvesting (solar, "
"vibration, thermal gradients, RF) can trickle-charge the smallest robots, "
"but the harvested microwatts suit sensing and occasional bursts, not "
"continuous locomotion. This record does the energy bookkeeping every "
"microrobot design must survive."),
"how_it_works": (
"Bookkeep in joules and watts. Chemical batteries (thin-film lithium) pack "
"the most energy per volume (~100 Wh/kg at micro-scale, less than "
"macroscopic cells because packaging dominates); capacitors deliver power "
"fast but store little; fuel cells and micro-combustors promise more but "
"add plumbing. The robot's average power sets endurance: 1 mW for 18 min "
"from the 1 mm3 battery above, or indefinitely if the 1 mW arrives "
"wirelessly. Peak power (a jump, a radio burst) can exceed the average by "
"100x, so designers add a capacitor as a sprint reservoir charged slowly "
"from the battery or harvester. Duty cycling is the universal trick: sleep "
"at nanowatts, wake for milliseconds of work, sleep again - the average, "
"not the peak, is what the battery feels. The demo runs the full budget: "
"storage, draw, endurance, and the wireless-vs-battery crossover."),
"key_points": [
"1 mm3 battery ~1 J -> 1 mW robot runs ~18 min; 1 mF @ 3 V -> 4.5 s.",
"Energy scales as L^3; power electronics shrink slower than the load.",
"Millibots carry batteries; true microrobots usually take power from outside.",
"Capacitors are sprint reservoirs, not fuel tanks.",
"Duty cycling (sleep at nW, burst at mW) stretches any budget 100x.",
"Harvesters suit sensing and bursts, not continuous locomotion.",
],
"requirements": [
"Scaling laws (the L^3 energy trap).",
"Energy vs power: joules, watts, and duty cycle.",
"A calculator for the endurance exercises.",
],
"standards": [
"Battery safety practice (UN 38.3 transport testing logic for lithium cells).",
"IEEE 1625/1725 design guidance for rechargeable cells (concepts apply at micro-scale).",
],
"citations": [C_SITTI, C_DILLER, C_MEMSHB],
"sig_lens": (
"Signature take: power is where Signature honesty lives - no robot is "
"promised more joules than its volume can hold. The Signature power "
"budget is drawn before the first beam is etched: storage, draw, duty "
"cycle, and the honest admission of when the robot must be fed from "
"outside. A robot that cannot pay its energy bills is a sculpture, not a "
"machine."),
},
{
"key": "wireless_power",
"name": "Wireless Power and Communication: Feeding Robots Without Wires",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"When batteries cannot fit, power arrives as a field. Inductive coupling - "
"the phone-charger principle shrunk to millimetres - transfers watts "
"across short gaps: a 1 uH receive coil resonates at 13.56 MHz with just "
"138 pF of capacitance, a capacitor smaller than a grain of salt. Resonant "
"coupling stretches the range; capacitive coupling works through thin "
"insulators; RF far-field follows the Friis equation but at 13.56 MHz the "
"22-metre wavelength makes every microrobot deeply near-field, so "
"far-field radio is the wrong tool and near-field induction is the right "
"one. Light powers through photovoltaics (a laser can feed a robot no "
"battery could), and ultrasound penetrates tissue where light cannot - the "
"preferred channel for medical microrobots. Communication rides the same "
"channels: backscatter (modulating the reflected field, like RFID), load "
"modulation on the power carrier, or optical blinking. This record covers "
"link budgets, resonance, and why the power channel and the command channel "
"are usually the same wire that isn't there."),
"how_it_works": (
"Resonance is the whole trick: transmitter and receiver coils tuned to the "
"same frequency exchange energy efficiently even with weak coupling "
"(coupling coefficients of 0.01 are typical at micro-scale gaps). Received "
"power scales with k^2 x Q_tx x Q_rx - high quality factors rescue weak "
"coupling, so coils are wound (or patterned) for maximum Q and the "
"capacitor is trimmed to exact resonance. The AC is rectified on the robot "
"(Schottky diodes or active rectifiers in CMOS) and regulated to the logic "
"and actuator rails. For communication, the robot modulates its load - "
"tiny impedance changes the transmitter detects as backscatter - achieving "
"kilobits per second with no transmitter on the robot at all. Ultrasound "
"power uses piezoelectric receivers (the same films as the actuators) at "
"hundreds of kilohertz to megahertz; optical power uses photovoltaic cells "
"tuned to the laser wavelength. Every scheme is sized by the link budget: "
"power in, coupling, rectification loss, power out."),
"key_points": [
"1 uH coil + 138 pF resonates at 13.56 MHz - the workhorse wireless band.",
"Received power ~ k^2*Q_tx*Q_rx: high Q rescues weak micro-scale coupling.",
"At 13.56 MHz (22 m wavelength) microrobots are deeply near-field: induction, not radio.",
"Ultrasound penetrates tissue: the medical microrobot's power channel.",
"Backscatter communication needs no transmitter on the robot.",
"Power and command usually share one channel - the wire that isn't there.",
],
"requirements": [
"Powering micro-robots (the energy budget that forces wireless).",
"Resonance basics: f = 1/(2 pi sqrt(LC)).",
"A calculator for the resonance and link exercises.",
],
"standards": [
"ISM band allocations (13.56 MHz, etc.) for wireless power.",
"IEC 60601 exposure limits for medical wireless power.",
],
"citations": [C_SITTI, C_KOVACS, C_NELSON],
"sig_lens": (
"Signature take: wireless power is Signature hospitality - the robot is a "
"guest that never carries its own food because the room itself is the "
"feast. Signature wireless design tunes the room and the guest to the same "
"note, and the energy crosses the gap the way a hum crosses a hall: "
"without touching anything."),
},
{
"key": "micro_locomotion",
"name": "Micro-Locomotion: Legs, Crawlers, and Swimming at Low Reynolds Number",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Moving at the micro-scale means fighting - or befriending - viscosity. "
"Legged microrobots stride: a 1 mm robot with 100 um strides at 100 Hz "
"covers 10 mm/s, ten body lengths per second, a respectable sprint. But "
"legs need joints, bearings, and friction control that barely exist below "
"a millimetre, so many microrobots crawl (inchworm gaits on electrostatic "
"scratch drives), roll (magnetically torqued spheres), or swim. Swimming "
"obeys Purcell's scallop theorem: at low Reynolds number, reciprocal "
"motion - open and close like a scallop - produces exactly zero net travel, "
"because the fluid has no memory. Nature's answer is the corkscrew: a "
"rotating helix (bacterial flagellum, magnetic micro-helix) screws through "
"the fluid non-reciprocally and swims. The drag is pure Stokes: a 1 mm "
"sphere moving at 1 mm/s in water feels just 9.4 nanonewtons of drag - "
"tiny, but so is every force available to fight it. This record covers "
"gaits, the scallop theorem, helical swimming, and the drag math."
),
"how_it_works": (
"Pick the regime from the Reynolds number. Above Re ~ 1 (millibots in air "
"or large microrobots in water), legs and wheels still work: electrostatic "
"or piezoelectric legs step at hundreds of hertz, and the square-cube law "
"makes the robot absurdly strong for its weight. Below Re ~ 1, switch to "
"non-reciprocal swimming: rotate a helix with a magnetic field (torque "
"from outside, thrust from the shape), beat an elastic tail with an "
"oscillating field, or catalyze bubbles asymmetrically for chemical "
"thrust. Speed scales with actuation frequency times size: double the "
"spin, double the swim - until viscous heating or actuator limits cap the "
"frequency. Steering comes from biasing the field direction (magnetic), "
"modulating the chemistry (catalytic), or differential leg strides "
"(walkers). Odometry is nearly impossible - no wheel encoders survive the "
"shrink - so position comes from external cameras or from the field "
"controller's model of where the robot should be."),
"key_points": [
"1 mm walker, 100 um strides at 100 Hz -> 10 mm/s = 10 body lengths/s.",
"Scallop theorem: reciprocal motion gives zero net travel at low Re.",
"Helical (corkscrew) swimming beats the scallop theorem - the bacterial trick.",
"Stokes drag on 1 mm sphere at 1 mm/s in water: 9.4 nN.",
"Speed ~ frequency x size; steering via field bias or differential strides.",
"No onboard odometry: position comes from external cameras or field models.",
],
"requirements": [
"The micro-scale map (Reynolds regimes).",
"Magnetic actuation (the usual swimmer drive).",
"A calculator for the speed and drag exercises.",
],
"standards": [
"Swimming performance reported as body lengths per second (field convention).",
"ISO 8373 vocabulary for locomotion terms.",
],
"citations": [C_PURCELL, C_SITTI, C_DILLER, C_KUMMER],
"sig_lens": (
"Signature take: micro-locomotion is Signature travel writing - every "
"journey is through honey, and the wise traveller stops kicking and "
"starts screwing. The Signature swimmer does not fight viscosity; it "
"threads itself through the fluid the way a screw threads wood, turning "
"the enemy medium into the road."),
},
{
"key": "microfluidics",
"name": "Microfluidic Integration: Robots That Swim in Labs-on-Chips",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Microfluidics - plumbing at the micrometre scale - is the native habitat "
"of many microrobots and the laboratory they work in. A channel 100 um "
"wide, 50 um tall, and 1 cm long pushes water at 0.104 microlitres per "
"second under just 1 kPa of pressure; the mean flow speed is 20.8 mm/s and "
"the Reynolds number is 1.4 - deeply laminar, so streams flow side by side "
"without mixing except by diffusion. That laminarity is a superpower: "
"reagents can be layered, gradients held steady for chemotaxis studies, "
"and single cells parked in traps for a robot to operate on. Microrobots "
"swim these channels to sort cells, assemble micro-tissues, deliver drugs "
"to precise channel addresses, and stir where stirring is otherwise "
"impossible. Valves (pneumatic PDMS membranes), pumps (peristaltic, "
"electroosmotic), and droplet generators give the chip its circulation, "
"and the robot is the mobile toolhead the fixed plumbing cannot be. This "
"record covers channel flow, laminar tricks, and the robot-as-toolhead "
"partnership."),
"how_it_works": (
"Pressure-driven flow follows Poiseuille's law: flow rate = pressure drop / "
"hydraulic resistance, with resistance ~ viscosity x length / (width x "
"height^3) - halving the channel height multiplies resistance sixteenfold, "
"which is why microfluidic pumps work hard. Electroosmotic flow instead "
"drags the fluid with an electric field along charged channel walls: no "
"moving parts, flat velocity profile, easy electronic control. Droplets "
"(water in oil) become isolated test tubes, each a microreactor a robot "
"can visit. The microrobot navigates by the same fields as elsewhere - "
"magnetic gradients steer it along channels, acoustic fields park it at "
"nodes - while the chip supplies the chemistry: reagents, cells, gradients, "
"waste removal. Vision through the transparent PDMS closes the loop. "
"Design rule: the robot handles what must move (tools, cargo, cells); the "
"chip handles what must flow (fluids, reagents, waste)."),
"key_points": [
"100x50 um channel, 1 cm, 1 kPa -> 0.104 uL/s, 20.8 mm/s, Re = 1.4 (laminar).",
"Laminar flow: streams layer without mixing; gradients stay put.",
"Halving channel height multiplies hydraulic resistance 16x.",
"Droplets are isolated microreactors the robot can visit.",
"Electroosmotic pumping: no moving parts, electronic flow control.",
"Division of labour: robot moves tools/cargo; chip moves fluids.",
],
"requirements": [
"Micro-locomotion (how robots swim the channels).",
"Microfabrication (soft lithography for PDMS chips).",
"A calculator for the flow-rate exercise.",
],
"standards": [
"Microfluidic interfacing conventions (chip-to-world connections).",
"Biocompatibility practice for cell-handling chips (ISO 10993 concepts).",
],
"citations": [C_MADOU, C_SITTI, C_WHITESIDES],
"sig_lens": (
"Signature take: the lab-on-a-chip is the Signature aquarium - glass "
"rivers that never mix, droplet islands, and one small swimmer with a job "
"to do. Signature microfluidics never asks the robot to be the plumbing; "
"the chip is the river system and the robot is the boat, and each is "
"designed for exactly its half of the partnership."),
},
{
"key": "micro_grippers",
"name": "Micro-Grippers and End Effectors: Hands for the Invisible",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"A gripper at the micro-scale faces an inverted problem: picking up is "
"easy, letting go is hard. Adhesion rules the small world - a 10 um sphere "
"touched to a surface feels about 0.5 uN of van der Waals attraction and "
"2.3 uN of capillary pull from a water meniscus, forces comparable to or "
"bigger than the gripper's own 10-uN electrostatic grip. Release the part "
"and it stays glued to the jaw. Micro-grippers therefore design the "
"release as carefully as the grasp: two-jaw tweezers driven by comb drives "
"or thermal chevrons, vacuum micro-nozzles that hold by suction and release "
"by a puff, compliant jaws that peel rather than pull, and active release "
"tricks (a sharp tap, a voltage pulse, a bubble). Force sensing in the "
"jaws - piezoresistive or capacitive - keeps the grip below the crush load "
"of a living cell (nanonewtons) while above the adhesion that would steal "
"the part. This record covers jaw designs, the adhesion enemy, and release "
"strategies."),
"how_it_works": (
"Two-jaw grippers open and close with the standard actuators: comb drives "
"for smooth proportional motion, thermal chevrons for strong holding "
"force, piezo bimorphs for fast delicate touch. The jaw tips are shaped to "
"the cargo - flat for chips, cupped for cells, needle-like for fibres - and "
"often coated to tune adhesion (hydrophobic coatings shed water menisci). "
"Vacuum grippers skip jaws entirely: a micro-nozzle sips the part with "
"suction and a pressure pulse spits it out, dodging the adhesion problem "
"by never making dry contact. Release strategies include mechanical "
"ejection (a third finger flicks the part), inertial release (a fast jerk "
"overcomes adhesion with acceleration), and environmental release "
"(submerge in fluid so capillary forces vanish). Closed-loop force sensing "
"watches the jaw strain so the controller knows grasped vs released vs "
"crushed - at these scales the difference is nanonewtons."),
"key_points": [
"Release is harder than grasp: capillary pull (2.3 uN on 10 um sphere) beats grip forces.",
"Comb-drive tweezers, thermal chevron jaws, piezo fingers: the standard hands.",
"Vacuum micro-nozzles dodge adhesion by avoiding dry contact.",
"Release tricks: ejector finger, inertial jerk, fluid submersion.",
"Jaw force sensing (piezoresistive/capacitive) distinguishes grasped/released/crushed.",
"Coatings tune adhesion: hydrophobic sheds the meniscus.",
],
"requirements": [
"Electrostatic and thermal actuation (the jaw muscles).",
"Scaling laws (why adhesion dominates).",
"A calculator for the adhesion-force exercise.",
],
"standards": [
"Cell-handling force limits per biomanipulation practice (nN-scale).",
"IEEE 2700-2017 for force-sensor performance reporting.",
],
"citations": [C_SITTI, C_DILLER, C_MALUF],
"sig_lens": (
"Signature take: the micro-gripper is the Signature hand that learned "
"humility - strong enough to hold a cell, gentle enough not to bruise it, "
"and wise enough to know the real skill is letting go. Signature gripper "
"design spends half its genius on the release, because at the micro-scale "
"everything wants to be held forever."),
},
{
"key": "micro_assembly",
"name": "Micro-Assembly: Building Things One Micron at a Time",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"Micro-assembly is manufacturing with microrobots as the workforce: "
"picking up micrometre parts and placing them with micrometre accuracy to "
"build sensors, optics, and machines no human hand could assemble. A "
"serial pick-and-place robot managing 10 seconds per part places 360 parts "
"per hour - a 1,000-part microassembly takes nearly 3 hours, which is why "
"the field dreams in parallel (self-assembly, massively parallel "
"micro-handlers). The enemies are the familiar small-world gang: adhesion "
"steals parts from grippers, vibration (a footstep is an earthquake at "
"this scale) ruins alignment, thermal drift walks the stage by microns, "
"and electrostatic discharge welds or repels parts unpredictably. "
"Alignment tolerance stacks brutally: placing a part within +-1 um over a "
"10 mm stage travel demands 1e-4 relative precision from every axis. "
"Strategies include compliant alignment (let chamfers and flexures seat "
"the part), visual servoing (cameras close the loop), and designing parts "
"that assemble themselves (see self-assembly). This record covers the "
"process, the enemies, and the throughput math."),
"how_it_works": (
"A micro-assembly cell pairs precision stages (piezo or voice-coil, "
"nanometre resolution, millimetre travel) with micro-grippers and "
"machine vision. The cycle: locate the part (template matching on the "
"camera), pick (gripper closes, force sensor confirms), transport (stage "
"moves, vibration isolation holds still), align (visual servoing trims the "
"last microns), place (controlled release - the hard part), verify "
"(measure, accept or rework). Throughput multiplies with parallelism: "
"arrays of grippers, wafer-scale batch transfer (place a whole wafer of "
"parts at once), and self-assembly where parts find their own seats via "
"surface tension or shape matching. Process control tracks the yield "
"killers - particle contamination (a 1 um dust mote is a boulder), humidity "
"(capillary stiction), and operator tremor (automate everything). The demo "
"computes serial throughput, alignment budgets, and the parallel speedup."),
"key_points": [
"Serial pick-place at 10 s/part -> 360 parts/hour; 1,000 parts ~ 3 hours.",
"+-1 um placement over 10 mm travel = 1e-4 relative precision per axis.",
"Enemies: adhesion, vibration, thermal drift, electrostatic discharge.",
"Compliant alignment and visual servoing close the precision loop.",
"Parallelism wins: gripper arrays, wafer-scale transfer, self-assembly.",
"Contamination control: a 1 um dust mote is a boulder.",
],
"requirements": [
"Micro-grippers (the hands doing the placing).",
"Testing and characterization (how placement is verified).",
"A calculator for the throughput exercise.",
],
"standards": [
"Cleanroom practice (ISO 14644) for assembly environments.",
"ESD control (ANSI/ESD S20.20 concepts) for micro-part handling.",
],
"citations": [C_SITTI, C_DILLER, C_WHITESIDES],
"sig_lens": (
"Signature take: micro-assembly is Signature watchmaking - a thousand "
"invisible parts, each placed with a patience no human hand possesses. "
"The Signature assembly cell is a monastery of stillness: vibration "
"isolated, temperature held, humidity tamed, so the only thing moving is "
"the part finding its home."),
},
{
"key": "micro_control",
"name": "Control at the Micro-Scale: Steering Without Seeing Clearly",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"Controlling a microrobot means steering a machine you can barely see, "
"with actuators you cannot fully model, through disturbances you cannot "
"measure. The numbers are unforgiving: a camera at 30 frames per second "
"watching a robot moving 1 mm/s sees it jump 33 um between frames - 33 "
"times a 1 um precision target. Open-loop dead reckoning drifts as "
"Brownian motion and unmodelled drag accumulate; closed-loop vision "
"feedback is limited by frame rate, latency, and the diffraction limit "
"(~0.37 um for a good microscope). The field's answers: slow down near "
"the target, use predictive models (Kalman filters fusing the field "
"controller's commands with sparse camera updates), exploit the physics "
"(magnetic fields are precisely known, so model-based feedforward does "
"most of the work), and design the task to need less precision (funnels, "
"traps, and compliant guides that forgive error). Millibots carry "
"microcontrollers and run PID loops onboard; true microrobots are "
"controlled from outside, the loop closed through a microscope. This "
"record covers feedback limits, state estimation, and the art of "
"controlling the barely visible."),
"how_it_works": (
"The control loop is: sense (camera frame, maybe 30-1000 Hz with a fast "
"camera), estimate (filter the noisy pixel measurements into position and "
"velocity - a Kalman filter weighs the model prediction against the "
"measurement by their relative trustworthiness), decide (PID or "
"model-predictive control computes the field or voltage command), actuate "
"(coils, electrodes, or laser update). Latency is the enemy: every "
"millisecond of delay at 1 mm/s is a micron of overshoot. Feedforward "
"helps enormously for magnetic systems because the field map is known "
"exactly - the controller pre-computes most of the command and uses "
"feedback only for correction. For swimmers, the controller plans in "
"velocity space (the fluid has no inertia to fight). And when precision "
"demands exceed sensing, the task is redesigned: drive the robot into a "
"funnel, let a trap catch it, use a docking station - precision by "
"mechanics, not by feedback."),
"key_points": [
"30 fps camera + 1 mm/s robot = 33 um jumps between frames vs 1 um targets.",
"Brownian motion and unmodelled drag kill open-loop dead reckoning.",
"Kalman filters fuse sparse camera data with the field model's predictions.",
"Magnetic feedforward works because the field map is known exactly.",
"Latency at 1 mm/s: 1 ms delay = 1 um overshoot.",
"When sensing falls short, redesign the task: funnels, traps, docking stations.",
],
"requirements": [
"Micro-locomotion (what is being steered).",
"Magnetic actuation or wireless power (the command channel).",
"A calculator for the frame-jump and latency exercises.",
],
"standards": [
"Control performance specified per IEEE 2700-style sensor/actuator parameters.",
"Vision calibration practice (pixel-to-micron mapping, distortion).",
],
"citations": [C_SITTI, C_DILLER, C_KUMMER],
"sig_lens": (
"Signature take: micro-control is Signature piloting in fog - the pilot "
"cannot see the ship clearly, so he learns the currents instead. The "
"Signature controller trusts its model of the field the way a sailor "
"trusts the chart, and spends its precious camera frames only on "
"correcting the drift the chart could not predict."),
},
{
"key": "swarm_micro",
"name": "Swarm Microrobots: Many Tiny Robots, One Big Job",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"One microrobot is a curiosity; ten thousand are a material. Swarm "
"microrobotics coordinates masses of tiny robots to do jobs no single "
"one can: cover a square metre for inspection (10,000 robots on a 10 mm "
"grid), assemble structures in parallel, map a chemical plume by "
"distributed sampling, or form shapes on command (a thousand-robot swarm "
"spelling out structures, as demonstrated at the centimetre scale). The "
"math of swarms is the math of scaling twice: capability grows with n, "
"but naive all-to-all communication grows with n^2 - so real swarms use "
"local rules (talk only to neighbours within a few millimetres) and "
"stigmergy (communicate through the environment: leave a chemical trail, "
"modify a shared structure). Global commands broadcast from outside "
"(a light pattern, a field gradient) steer the collective without "
"addressing individuals. Fault tolerance is free: lose 10% of a "
"10,000-robot swarm and the job still completes. This record covers local "
"rules, communication scaling, and programming the collective."),
"how_it_works": (
"Each robot runs the same tiny program: sense neighbours (short-range IR, "
"capacitive, or optical), sense the environment (chemical, light, field), "
"apply the local rule (move toward the gradient, keep 5 mm from "
"neighbours, deposit material where the template says), repeat. Global "
"behaviour - aggregation, pattern formation, collective transport - emerges "
"without any robot understanding the plan, the way ant colonies build "
"without architects. The operator programs the swarm by programming the "
"rule and the environment: project the target shape in light and the "
"phototactic robots fill it; set a chemical source and the chemotactic "
"robots map its plume. Task allocation is market-based or threshold-based "
"(robots take jobs they are near or suited for). The demo computes coverage "
"(robots per square metre), the n^2 communication trap, and the fault-"
"tolerance arithmetic that makes swarms robust."),
"key_points": [
"10,000 robots on a 10 mm grid cover 1 m2 for inspection.",
"All-to-all communication scales as n^2: real swarms use local neighbour rules.",
"Stigmergy: communicate through the environment (trails, shared structures).",
"Global steering via broadcast (light patterns, field gradients) - no individual addressing.",
"Fault tolerance is free: losing 10% of 10,000 barely matters.",
"Program the rule + the environment; the collective behaviour emerges.",
],
"requirements": [
"Micro-locomotion (how individuals move).",
"Control at the micro-scale (the sensing limits swarms inherit).",
"A calculator for the coverage and scaling exercises.",
],
"standards": [
"Swarm performance metrics per emerging multi-robot systems practice.",
"Communication protocol discipline (local broadcast, no global addressing).",
],
"citations": [C_RUBENSTEIN, C_SITTI, C_DILLER],
"sig_lens": (
"Signature take: the swarm is the Signature choir - ten thousand tiny "
"voices, none singing the whole song, all singing it together. The "
"Signature swarm programmer does not conduct individuals; he writes the "
"hymn (the local rule) and lights the cathedral (the environment), and "
"the music assembles itself."),
},
{
"key": "compliant_mech",
"name": "Compliant Mechanisms: Hinges Made of Bending, Not Pins",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"At the micro-scale, pin joints are a nightmare - no room for bearings, "
"friction welds the pins, assembly is impossible - so microrobots hinge "
"by bending instead: compliant mechanisms get their motion from the "
"elastic deflection of the material itself. A fixed-guided silicon beam "
"200 um long, 20 um wide, and 5 um thick bends with a stiffness of "
"13.2 N/m; push its tip 10 um sideways and it answers with 132 uN while "
"the peak stress reaches only 317 MPa - far below silicon's ~7 GPa limit, "
"so it can flex millions of times. No sliding, no wear, no lubrication, "
"no assembly: the hinge is etched as part of the body. The pseudo-rigid-"
"body model lets designers treat each flexure as a rigid link with a "
"torsional spring, so textbook mechanism synthesis (four-bars, sliders, "
"grippers) ports straight to the micro-world. Bistable compliant designs "
"snap between two positions and stay there with no power - mechanical "
"memory. This record covers flexure design, stress limits, and the "
"mechanisms that bend instead of turning."),
"how_it_works": (
"Replace every pin joint with a thin flexure sized so its bending gives "
"the needed rotation at acceptable stress: stress ~ 6 x force x length / "
"(width x thickness^2), so long thin flexures rotate far at low stress. "
"The pseudo-rigid-body model places a virtual pivot at the flexure's "
"characteristic radius with a torsional spring constant derived from beam "
"theory, letting the designer synthesize linkages with ordinary kinematics "
"and then convert each pivot back to a flexure. Notch hinges (thin "
"waists) concentrate rotation for precision stages; distributed-compliance "
"designs spread bending for large motion; bistable beams (pre-curved past "
"their buckling point) snap through and latch. Fatigue is managed by "
"keeping stress well under the endurance limit and avoiding sharp corners "
"(fillet everything - a corner is a crack waiting to happen). Damping is "
"low, so flexure mechanisms ring; add viscoelastic coatings or operate "
"below resonance where ringing matters."),
"key_points": [
"Si flexure 200x20x5 um: k = 13.2 N/m; 10 um deflection -> 132 uN at 317 MPa stress.",
"No pins, no wear, no lubrication, no assembly - the hinge is etched in.",
"Pseudo-rigid-body model: design with linkages, build with flexures.",
"Bistable designs latch with zero holding power - mechanical memory.",
"Stress ~ 6FL/(wt^2): long thin flexures rotate far at low stress.",
"Fillet every corner: sharp corners are cracks waiting to happen.",
],
"requirements": [
"MEMS bodies (beam theory: stiffness, resonance).",
"Micro-scale materials (silicon's strength and fatigue).",
"A calculator for the flexure stress exercise.",
],
"standards": [
"Howell 'Compliant Mechanisms' design methodology (field-standard reference).",
"Fatigue design practice for silicon microstructures.",
],
"citations": [C_HOWELL, C_SENTURIA, C_PISTER],
"sig_lens": (
"Signature take: the compliant mechanism is the Signature joint that "
"refused to be assembled - no pin, no bearing, no wear, just silicon "
"choosing to bend. Signature flexure design is origami thinking: the "
"motion was always in the material, and the etch merely gave it "
"permission to move."),
},
{
"key": "chemical_propulsion",
"name": "Chemical Propulsion: Catalytic Motors and Janus Particles",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Chemical propulsion lets microrobots swim on fuel dissolved in their "
"environment - no wires, no fields, no batteries. The classic is the "
"Janus particle: a 2 um silica sphere half-coated with platinum. In "
"hydrogen-peroxide solution the platinum catalyzes 2H2O2 -> 2H2O + O2; "
"the asymmetric reaction (and the bubbles it makes) pushes the particle "
"at about 10 um/s - five body lengths per second - until the fuel runs "
"out. A 10-minute run covers 6 mm, a respectable voyage for a "
"micrometre machine. Variants use enzyme catalysis (biocompatible fuels "
"like glucose or urea instead of peroxide), diffusiophoresis (motion in "
"a self-generated chemical gradient, no bubbles), and bubble recoil "
"(oxygen jets from tubular microengines). Steering comes from built-in "
"asymmetry plus external bias: magnetic caps let a field aim the "
"particle while chemistry drives it. The limits are honest: fuel "
"depletes, peroxide is toxic to tissue, and the robot cannot be turned "
"off - it swims until chemistry says stop. This record covers the "
"mechanisms, the speeds, and the fuel bookkeeping."),
"how_it_works": (
"Asymmetry is the engine. Coat one hemisphere with catalyst and the "
"reaction runs faster there; the product gradient (or the growing and "
"detaching bubbles) pushes the particle toward or away from the coated "
"side, depending on the mechanism. Self-diffusiophoresis moves particles "
"in the concentration gradients they generate - no bubbles needed, works "
"at lower fuel concentrations. Tubular microjets (rolled-up nanomembranes "
"with catalyst inside) fire oxygen bubbles from one end like tiny rockets, "
"reaching hundreds of body lengths per second in strong fuel. Speed scales "
"with fuel concentration and catalytic area, saturating when diffusion "
"cannot feed the reaction faster. Lifetime is fuel divided by consumption "
"rate: a closed droplet of 1% peroxide feeds a Janus swimmer for minutes; "
"an open reservoir (the bloodstream, a lake) feeds it indefinitely. "
"Enzyme-powered motors trade speed for biocompatibility - slower, but the "
"fuel is already in the body."),
"key_points": [
"Pt Janus particle (2 um) in peroxide: ~10 um/s = 5 body lengths/s.",
"Asymmetry is the engine: catalyst on one side only.",
"Diffusiophoresis swims without bubbles; microjets fire bubble rockets.",
"Speed scales with fuel concentration, saturating at diffusion limits.",
"Enzyme motors use body-safe fuels (glucose, urea) - slower but biocompatible.",
"Limits: fuel depletes, peroxide is toxic, no off switch.",
],
"requirements": [
"Micro-locomotion (the scallop theorem these motors beat).",
"Scaling laws (diffusion vs directed motion).",
"A calculator for the speed/range exercise.",
],
"standards": [
"Chemical safety practice for peroxide and catalytic materials.",
"Biocompatibility screening (ISO 10993 concepts) for medical variants.",
],
"citations": [C_SITTI, C_DILLER, C_NELSON],
"sig_lens": (
"Signature take: the catalytic swimmer is the Signature sailor that "
"drinks the sea - fuel dissolved everywhere, engine painted on half its "
"hull. Signature chemical design accepts the honest bargain: the robot "
"cannot be switched off, so it is given a voyage worth completing before "
"the chemistry runs dry."),
},
{
"key": "biohybrid",
"name": "Biohybrid Microrobots: Living Engines in Synthetic Bodies",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Biohybrid microrobots hire living cells as engines: bacteria, algae, or "
"muscle tissue integrated with synthetic bodies. Ten E. coli bacteria, "
"each pushing with about 0.5 piconewtons of flagellar thrust, drive a "
"10 um cargo at 53 um/s through water - the Stokes drag math balances "
"exactly (5 pN of thrust against 6-pi-mu-a-v drag). The cells bring "
"capabilities no motor matches: they harvest chemical energy from the "
"environment, self-repair, replicate, and - crucially - sense and steer "
"themselves (chemotaxis: bacteria swim up nutrient gradients "
"autonomously). Muscle-powered biobots bend synthetic skeletons with "
"real contractile force; sperm-hybrid micromotors tow drug cargo with "
"the strongest micro-swimmers nature built. The costs are biological: "
"cells need the right temperature, pH, and nutrients; they die; and a "
"medical biohybrid must be immunologically invisible or the body attacks "
"the engine. This record covers the cell-machine interface, thrust "
"budgets, and keeping the living half alive."),
"how_it_works": (
"Attach motile cells to a synthetic chassis - bacteria to a microbead, "
"cardiomyocytes to a flexible PDMS skeleton - and the cells' native "
"machinery becomes the drivetrain. Bacterial flagellar motors spin at "
"~100 Hz, each delivering ~0.5 pN; the thrust sums (imperfectly - "
"coordination is statistical) and Stokes drag sets the speed. Steering "
"uses the cells' own taxes: chemotaxis follows chemical gradients, "
"magnetotactic bacteria follow field lines, phototactic algae follow "
"light - the operator steers by shaping the environment, not the robot. "
"Muscle biobots pace contraction with electrical or optical stimulation "
"(optogenetics: light-gated ion channels make muscle fire on command). "
"Encapsulation (alginate, PEG hydrogels) shields cells from immune attack "
"while passing nutrients. Lifetime is measured in hours to days - the "
"cells' lifespan, not the chassis's - so biohybrids are single-mission "
"machines by nature."),
"key_points": [
"10 E. coli x 0.5 pN -> 5 pN thrust drives 10 um cargo at 53 um/s (Stokes balance).",
"Cells self-fuel, self-repair, and steer themselves (chemotaxis).",
"Flagellar motors spin ~100 Hz - nature's rotary engine, free with every bacterium.",
"Steering via taxes: shape the environment (gradients, light, fields), not the robot.",
"Optogenetic muscle fires on light command for biobot actuation.",
"Limits: cells need life support; medical use demands immune invisibility.",
],
"requirements": [
"Chemical propulsion (the synthetic counterpart).",
"Micro-locomotion (Stokes drag and low-Re swimming).",
"A calculator for the thrust/speed exercise.",
],
"standards": [
"Biosafety practice (BSL-1/2) for engineered cell-machine systems.",
"ISO 10993 biocompatibility concepts for medical biohybrids.",
],
"citations": [C_SITTI, C_NELSON, C_DILLER],
"sig_lens": (
"Signature take: the biohybrid is the Signature partnership - the "
"machine provides the mission and the cell provides the miracle. "
"Signature biohybrid design is diplomacy between kingdoms: keep the "
"living half fed, warm, and unthreatened, and it will lend you an engine "
"three billion years in the perfecting."),
},
{
"key": "optical_control",
"name": "Optical Control: Tweezers and Light-Driven Microrobots",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Light is the most precise hand in microrobotics: focused to a "
"micrometre spot, a 100 mW laser reaches an intensity of 1.3e11 W/m2, "
"and the photon momentum becomes a usable tool. Optical tweezers trap "
"a micrometre particle in the focus with a spring-like stiffness around "
"10 pN/um - displace the particle 1 um and the light pulls back with "
"10 piconewtons, enough to hold a cell, stretch DNA, or assemble "
"micro-parts without contact. Holographic tweezers split one beam into "
"hundreds of independently steerable traps: a full micro-assembly crew "
"made of light. Beyond trapping, light drives: photothermal actuators "
"bend where the laser heats, liquid-crystal elastomers crawl toward "
"illumination, and photocatalytic swimmers chase light gradients. "
"Optogenetics lets light fire biohybrid muscle on command. The limits: "
"light needs line of sight (useless deep in tissue without fibre "
"delivery), high intensities cook biology, and the apparatus (laser, "
"microscope, spatial light modulator) dwarfs the robot. This record "
"covers trapping, holographic control, and light as fuel."),
"how_it_works": (
"A tightly focused laser creates an intensity gradient; a transparent "
"particle is pulled toward the brightest point (gradient force) while "
"photon scattering pushes it downstream - with a high-numerical-aperture "
"objective the gradient wins and the particle is trapped in 3D. Move the "
"focus (steering mirrors, acousto-optic deflectors, holograms) and the "
"particle follows: calibrated tweezers are also force sensors, reading "
"piconewtons from the particle's displacement in the known trap stiffness. "
"Holographic optical tweezers compute a phase hologram that sculpts the "
"beam into arbitrary trap arrays, updated at video rates. Light-driven "
"robots skip the trap: azobenzene polymers bend under UV, thermophoretic "
"swimmers ride laser-heated gradients, and photovoltaic robots convert "
"the beam directly to electricity. Control closes through the same "
"microscope that delivers the light - sense and actuate through one "
"objective."),
"key_points": [
"Optical trap stiffness ~10 pN/um: 1 um displacement -> 10 pN restoring force.",
"100 mW in a 1 um spot = 1.3e11 W/m2 - photon momentum becomes a tool.",
"Holographic tweezers: hundreds of independently steerable light-traps.",
"Calibrated tweezers double as piconewton force sensors.",
"Light drives directly: photothermal bending, thermophoretic swimming, photovoltaics.",
"Limits: needs line of sight; high intensity cooks biology; big apparatus, tiny robot.",
],
"requirements": [
"Micro-grippers (contact manipulation, the optical alternative).",
"Wireless power (optical power delivery).",
"A calculator for the trap-force and intensity exercises.",
],
"standards": [
"Laser safety (ANSI Z136) for trapping beam powers.",
"Microscope calibration practice for force measurement.",
],
"citations": [C_SITTI, C_DILLER, C_WHITESIDES],
"sig_lens": (
"Signature take: the optical tweezer is the Signature touch that never "
"touches - a finger made of focused starlight, gentle enough for a cell "
"and precise enough for a chromosome. Signature optical design wields "
"light the way a conductor wields a baton: the beam never plays a note "
"itself, but every particle in the hall moves to it."),
},
{
"key": "medical_microbots",
"name": "Medical Microrobots: Drug Delivery Inside the Body",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Medical microrobots aim to replace systemic treatment with targeted "
"delivery: instead of flooding the body with drugs, send the drug to the "
"disease. The arithmetic is compelling - a billion microrobots each "
"carrying 1 picolitre deliver 1 millilitre of drug in total, and if just "
"1% reach the target, 10 microlitres arrive exactly where needed versus "
"millilitres washing through healthy tissue. Magnetic swimmers steer "
"through the bloodstream under external fields (fields pass through "
"tissue harmlessly); catalytic and biohybrid swimmers exploit local "
"chemistry; ultrasound imaging tracks them in real time. The gauntlet "
"they must run: immune clearance (macrophages eat intruders), the "
"bloodstream's shear and branching flow, targeting (finding a tumour "
"among healthy tissue), controlled release (drug out only at the "
"address), and safe degradation or excretion afterwards. Biodegradable "
"bodies (magnesium, PLGA polymers) dissolve after the mission. This "
"record covers the delivery concept, the physiological gauntlet, and the "
"dose arithmetic."),
"how_it_works": (
"The mission profile: inject (intravenous or local), navigate (magnetic "
"gradients steer swimmers against flow; chemotaxis or flow-following "
"handles the fine approach), target (ligands on the robot surface bind "
"tissue markers - antibodies, peptides - for molecular addressing), "
"release (pH, temperature, enzyme, ultrasound, or light triggers open the "
"cargo bay only at the target), degrade (the body dissolves or the kidneys "
"clear the remains). Propulsion choices trade control for autonomy: "
"magnetic drive is fully steerable from outside but needs the coil array "
"and imaging; chemical/biohybrid swimmers navigate themselves but cannot "
"be recalled. Imaging closes the loop - ultrasound, photoacoustic, and "
"magnetic particle imaging each see different robot materials at depth. "
"Safety is designed in layers: biocompatible/biodegradable materials, "
"dose limits from the arithmetic above, and fail-safe degradation if "
"control is lost."),
"key_points": [
"1e9 robots x 1 pL = 1 mL total dose; 1% targeting -> 10 uL delivered locally.",
"Magnetic steering penetrates tissue; ultrasound tracks at depth.",
"Targeting via surface ligands (antibodies, peptides) for molecular addressing.",
"Release triggers: pH, temperature, enzymes, ultrasound, light - only at the address.",
"Biodegradable bodies (Mg, PLGA) dissolve after the mission.",
"Gauntlet: immune clearance, blood flow, targeting, release, safe excretion.",
],
"requirements": [
"Magnetic actuation (the leading medical drive).",
"Biohybrid microrobots (the living-engine alternative).",
"A calculator for the dose-arithmetic exercise.",
],
"standards": [
"ISO 13485 quality management for medical devices.",
"ISO 10993 biocompatibility evaluation concepts.",
"IEC 60601 for field/imaging equipment safety.",
],
"citations": [C_NELSON, C_SITTI, C_KUMMER],
"sig_lens": (
"Signature take: the medical microrobot is the Signature physician's "
"smallest envoy - a courier that carries medicine through the bloodstream "
"and knocks only on the diseased door. Signature medical design holds "
"itself to the physician's oath at the micrometre scale: first, do no "
"harm - then dissolve without a trace when the errand is done."),
},
{
"key": "microsurgery",
"name": "Microsurgery Tools: Operating at the Cellular Scale",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Microsurgery tools extend the surgeon's hands below the tremor limit: "
"human hand tremor shakes at roughly 100 um amplitude around 10 Hz, so "
"any tool working inside a 100 um retinal vein - with walls to spare, "
"meaning tools under 30 um - must filter the surgeon out of the loop. "
"Microrobotic surgical tools do exactly that: magnetically steered "
"micro-grippers and cutters inside the eye, untethered drills for the "
"inner ear, cell-scale injectors that pierce one cell without disturbing "
"its neighbours, and retinal-vein cannulation robots that hold station "
"against the pulse of blood flow. Force sensing at the nanonewton scale "
"tells the controller (and the surgeon) the difference between touching, "
"grasping, and tearing - information a human hand could never feel. "
"Tremor filtering, motion scaling (surgeon moves 1 mm, tool moves 10 um), "
"and virtual fixtures (software walls the tool cannot cross) make the "
"impossible routine. This record covers the tools, the tremor problem, "
"and the safety architecture of surgery at cellular scale."),
"how_it_works": (
"The system splits the surgeon from the tool: the surgeon commands at "
"human scale through a master console while the microrobot executes at "
"cellular scale inside the patient. Magnetic fields or tethered "
"micro-actuators drive the tool; cameras (often OCT - optical coherence "
"tomography - for depth) track it; force sensors in the tool report "
"contact. Tremor filtering removes the 8-12 Hz physiological shake in "
"software; motion scaling divides the surgeon's hand motion by 10-100x; "
"virtual fixtures forbid the tool from entering no-go anatomy even if "
"commanded. For untethered intraocular robots, the OctoMag-style coil "
"array steers from outside the eye while the surgeon watches through the "
"surgical microscope. Safety layers: redundant position sensing, force "
"limits that halt on excess contact, and tools designed to fail soft "
"(flexures bend, nothing snaps into shrapnel)."),
"key_points": [
"Hand tremor ~100 um at ~10 Hz: tools for 100 um vessels must be <30 um and tremor-filtered.",
"Motion scaling 10-100x: surgeon moves millimetres, tool moves microns.",
"Virtual fixtures: software walls the tool cannot cross.",
"nN force sensing distinguishes touch, grasp, and tear.",
"OCT imaging gives depth tracking inside tissue.",
"Safety: redundant sensing, force-limited halt, fail-soft flexure tools.",
],
"requirements": [
"Medical microrobots (the delivery cousins of surgical tools).",
"Micro-grippers (the hands at the tool tip).",
"A calculator for the tremor/scaling exercise.",
],
"standards": [
"ISO 13485 and IEC 60601 for surgical device safety.",
"Surgical robotics risk management per ISO 14971 concepts.",
],
"citations": [C_NELSON, C_SITTI, C_KUMMER],
"sig_lens": (
"Signature take: the microsurgery tool is the Signature hand steadied "
"beyond human steadiness - the tremor filtered out, the motion divided a "
"hundredfold, the surgeon's intent preserved and the surgeon's shake "
"discarded. Signature surgical design honours the surgeon's skill by "
"removing only the noise, never the judgment."),
},
{
"key": "micro_flight",
"name": "Insect-Scale Flight: The Hardest Actuation Problem",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Insect-scale flight is microrobotics' hardest actuation problem: the "
"robot must beat its wings over 100 times per second while carrying its "
"own power, and the aerodynamics are unsteady in ways no textbook "
"propeller equation covers. The RoboBee (Harvard, 2013) proved it "
"possible: an 80 mg robot with a 3 cm wingspan, flapping at 120 Hz on "
"piezoelectric bimorph muscles, generating 785 uN of lift - exactly its "
"weight - and achieving controlled hover. The tricks: piezoelectric "
"actuators (the only muscles fast and light enough), compliant wing "
"hinges (flexures, not bearings), and resonance (drive the wing at its "
"natural frequency so each beat costs minimal energy). Power remains "
"tethered - no battery flies at 80 mg yet - so control flies offboard "
"while the robot flies on a wire leash. Scaling says smaller flies "
"faster: wingbeat frequency rises roughly as 1/size. This record covers "
"the lift math, the actuator choice, and why flight is the final exam of "
"micro-actuation."),
"how_it_works": (
"Lift comes from flapping, not spinning: each half-stroke accelerates "
"air downward (leading-edge vortices add extra lift at this scale - the "
"insect trick). The wing is a resonant system - hinge stiffness and wing "
"inertia set a natural frequency, and the piezo muscle drives it there, "
"so the wing stores and returns energy like a tuning fork. Thrust "
"vectoring steers: differential wing amplitude rolls and pitches the "
"body, the way insects modulate stroke. The controller (offboard, for "
"now) reads body attitude from external cameras or onboard gyros and "
"modulates the two wing drives at kilohertz rates. Power budget: the "
"piezo wings of an 80 mg robot draw tens of milliwatts - within a wire "
"tether's delivery but an order of magnitude beyond what an 80 mg "
"battery could sustain, which is why free flight awaits better power "
"density, not better aerodynamics."),
"key_points": [
"RoboBee: 80 mg, 3 cm wingspan, 120 Hz, 785 uN lift = its own weight (Ma et al. 2013).",
"Piezo bimorphs: the only flight muscles fast and light enough.",
"Resonant wings: drive at natural frequency, beat almost for free.",
"Leading-edge vortices: the insect unsteady-aerodynamics trick.",
"Power is tethered: tens of mW needed, no 80 mg battery can sustain it.",
"Frequency scales ~1/size: smaller fliers beat faster.",
],
"requirements": [
"Piezoelectric actuation (the flight muscles).",
"Compliant mechanisms (the wing hinges).",
"A calculator for the lift/weight exercise.",
],
"standards": [
"Flight-test reporting per micro air vehicle research conventions.",
"Piezo drive safety practice (high-voltage, high-frequency).",
],
"citations": [C_WOOD, C_SITTI, C_HOWELL],
"sig_lens": (
"Signature take: the flying microrobot is the Signature final exam - "
"every actuation lesson distilled into 80 milligrams that refuses to "
"fall. Signature flight design does not fight the air; it joins the "
"insects' ancient conspiracy with vortices, resonance, and wings that "
"remember every beat."),
},
{
"key": "inspection_env",
"name": "Inspection Microrobots: Pipelines, Engines, and the Environment",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Inspection is microrobotics' most near-term industrial job: send small "
"robots where humans and big machines cannot go. A 1 km pipeline of 10 cm "
"diameter takes one 10 mm/s crawler 27.8 hours to traverse - but ten "
"crawlers do it in 2.8 hours, and none of them needs the pipeline shut "
"down or cut open. Jet-engine inspectors crawl turbine blades looking for "
"cracks; bridge-cable robots ride strands checking for corrosion; "
"environmental micro-swimmers sample water for pollutants, mapping plumes "
"by distributed sensing the way a swarm maps a chemical gradient. The "
"payloads are micro-sensors: cameras, eddy-current probes, ultrasonic "
"transducers, chemical sniffers - the sensing records of this database, "
"mounted on the locomotion records. The business case writes itself: "
"inspection without disassembly, without shutdown, without scaffolding. "
"The engineering challenges are locomotion on real surfaces (rust, slime, "
"curvature), communication through metal (no radio inside a steel pipe - "
"use acoustic or tethered links), and retrieval (the robot must come "
"home). This record covers platforms, payloads, and the coverage math."),
"how_it_works": (
"The platform matches the venue: magnetic crawlers cling to steel pipes "
"and climb vertically; inchworm robots brace inside tubes; swimming "
"inspectors ride flow in water mains; flying millibots survey from above. "
"Navigation fuses dead reckoning (poor, but the pipe constrains the "
"geometry) with landmarks (welds, flanges, known features) and external "
"tracking where available. Data muling solves the communication problem: "
"the robot records everything and dumps it at a dock, because streaming "
"video through metres of steel is fantasy. Power is usually carried "
"(millibots with batteries run hour-long missions) or tethered for "
"unlimited endurance where the tether can follow. The inspection plan is "
"coverage arithmetic: speed times swath width times robots, divided by "
"area - the demo works a pipeline and a bridge cable. Findings feed "
"predictive maintenance: the robot does not just see the crack, it "
"schedules the repair."),
"key_points": [
"1 km of 10 cm pipe: one 10 mm/s crawler = 27.8 h; ten crawlers = 2.8 h.",
"Inspection without disassembly, shutdown, or scaffolding: the business case.",
"Payloads: micro-cameras, eddy-current, ultrasound, chemical sniffers.",
"No radio inside steel pipe: use acoustic links, tethers, or data muling.",
"Navigation by constrained geometry + landmarks (welds, flanges).",
"Findings feed predictive maintenance: see the crack, schedule the repair.",
],
"requirements": [
"Micro-locomotion (crawling and swimming platforms).",
"Micro-sensors (the inspection payloads).",
"A calculator for the coverage-arithmetic exercise.",
],
"standards": [
"Non-destructive testing practice (ASNT concepts) for inspection payloads.",
"Pipeline inspection reporting conventions (anomaly classification).",
],
"citations": [C_SITTI, C_DILLER, C_JUDY],
"sig_lens": (
"Signature take: the inspection microrobot is the Signature watchman - "
"patient, small, and welcome where giants cannot go. It does not break "
"the pipe to see inside it; it knocks politely, crawls the darkness with "
"a lantern of sensors, and returns with the truth about every weld."),
},
{
"key": "self_assembly",
"name": "Self-Assembly and Micro-Origami: Robots That Fold Themselves",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Self-assembly solves micro-assembly's hardest problem - handling - by "
"eliminating handling: parts are fabricated flat and fold themselves into "
"3D robots. Stressed thin films curl on release (the stress that curls an "
"Al-on-Si beam becomes a hinge that folds to a designed angle); solder "
"hinges melt and surface tension pulls flaps upright; hydrogels swell and "
"fold on a chemical trigger; magnetic panels snap to programmed "
"orientations. Micro-origami has folded grippers, containers, and walking "
"robots from flat precursors. The yield math is sobering: with 99% "
"per-hinge success across 50 hinges, only 60.5% of robots fold correctly - "
"so production demands 99.9% per-hinge reliability to reach 95% assembly "
"yield. Design rules follow: minimize hinge count, make hinges "
"self-correcting (folds that guide themselves home), and test the fold "
"sequence on sacrificial runs. Combined with swarm thinking, self-assembly "
"scales: a wafer of flat precursors becomes a wafer of robots in one "
"trigger step. This record covers fold mechanisms, yield math, and "
"design for self-assembly."),
"how_it_works": (
"Program the flat pattern with fold information: hinge lines are "
"thinned, stressed, or coated so each knows its fold angle and direction. "
"Release the trigger - etch the sacrificial layer, raise the temperature, "
"change the pH - and the stored energy (film stress, surface tension, "
"swelling pressure) drives each hinge to its angle in a designed sequence "
"(order matters: fold the inner flaps before the outer shell closes). "
"Self-correction comes from geometry: V-groove hinges seat at exactly "
"the designed angle; magnetic latches click panels into their final "
"pose; capillary bridges pull misaligned flaps home. The designer "
"simulates the fold path to catch collisions (two flaps trying to occupy "
"one space) and sequences the triggers so the structure cannot trap "
"itself half-folded. Yield is verified statistically - fold a hundred, "
"count the good ones - and the hinge process is tuned until the binomial "
"math from the demo clears the production target."),
"key_points": [
"Flat precursors fold into 3D robots: stress hinges, solder surface tension, hydrogels, magnets.",
"99% per-hinge x 50 hinges = 60.5% yield; need 99.9% per hinge for 95%.",
"Fold sequence matters: inner flaps before the outer shell closes.",
"Self-correcting hinges: V-grooves seat exactly; capillary bridges pull flaps home.",
"Minimize hinge count; simulate the fold path to catch collisions.",
"One trigger step turns a wafer of flat patterns into a wafer of robots.",
],
"requirements": [
"Micro-assembly (the serial process self-assembly replaces).",
"Micro-scale materials (stressed films and their curl).",
"A calculator for the yield-math exercise.",
],
"standards": [
"Origami fold-pattern conventions (mountain/valley assignment).",
"Statistical process control for hinge-yield qualification.",
],
"citations": [C_WHITESIDES, C_PISTER, C_SITTI],
"sig_lens": (
"Signature take: self-assembly is Signature origami - the robot folded "
"into the wafer like a letter folded into an envelope, waiting for the "
"trigger to become itself. The Signature folder designs backwards from "
"the finished machine, hiding every hinge's destiny in the flat pattern, "
"and trusts the physics to read the instructions."),
},
{
"key": "reliability",
"name": "Reliability at the Micro-Scale: Stiction, Wear, and Packaging",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Microrobots do not fail the way big machines fail - they fail by "
"sticking, not by breaking. Stiction (static friction plus adhesion) "
"glues moving parts permanently: a water meniscus condensing under a "
"100 um plate pulls with 57.6 uN, overwhelming the ~10 uN the "
"electrostatic actuator can muster to free it - the part never moves "
"again. Wear is different too: silicon has no dislocations to blunt "
"cracks, so a scratched flexure can fail suddenly rather than wearing "
"gracefully. The Weibull statistics still apply: with shape parameter "
"2 and characteristic life 1e7 cycles, 1.0% of a fleet fails by 1e6 "
"cycles - plan spares accordingly. Defences are layered: anti-stiction "
"coatings (self-assembled monolayers), dimpled landing pads (less "
"contact area), hermetic packaging (keep the water out), supercritical "
"drying after release, and design rules (no large flat contacts, "
"filleted corners). Packaging is half the product: the chip-scale "
"package must pass electrical signals, optical paths, and sometimes "
"fluids while keeping the hostile world out. This record covers failure "
"modes, the statistics, and the defences."),
"how_it_works": (
"Design against stiction first: minimize contact area (dimples, bumps), "
"coat surfaces (hydrophobic monolayers cut capillary adhesion), control "
"the environment (hermetic seals, getters absorb stray moisture), and "
"give actuators margin (restoring force well above worst-case adhesion). "
"Design against fracture: fillet every corner, keep flexure stress under "
"a fraction of the 7 GPa silicon limit, proof-test with an overload "
"cycle that breaks the weaklings early. Qualify with accelerated life "
"tests - temperature, humidity, vibration, and cycle count - then fit "
"Weibull parameters and extrapolate to the mission life with margin. "
"Packaging co-design starts on day one: the package defines the "
"mechanical boundary conditions (stress from the seal can warp the "
"device), the thermal path, and the feedthrough count. A microrobot that "
"works on the probe station and dies in the package was never a product - "
"reliability is designed, not inspected in."),
"key_points": [
"Stiction kills more microrobots than fracture: 57.6 uN meniscus vs ~10 uN restore.",
"Anti-stiction: monolayers, dimpled pads, hermetic seals, supercritical drying.",
"Silicon fails suddenly: fillet corners, proof-test, keep stress far under 7 GPa.",
"Weibull (beta=2, eta=1e7 cycles): 1.0% fail by 1e6 cycles - plan spares.",
"Packaging is half the product: signals, optics, fluids in; hostile world out.",
"Reliability is designed in, not inspected in.",
],
"requirements": [
"Microfabrication (release and drying, where stiction strikes).",
"MEMS bodies (the structures being protected).",
"A calculator for the stiction and Weibull exercises.",
],
"standards": [
"SEMI packaging and hermeticity test standards.",
"Weibull analysis per IEC 61649.",
"Moisture sensitivity handling (IPC/JEDEC J-STD-033 concepts).",
],
"citations": [C_MALUF, C_MEMSHB, C_SENTURIA],
"sig_lens": (
"Signature take: reliability is Signature humility - the admission that "
"the invisible enemy (a water meniscus, a sharp corner) defeats more "
"robots than any rival. The Signature reliability engineer is a "
"paranoid guardian: coat everything, seal everything, fillet everything, "
"and never trust a moving part that has not proven it can move a "
"million times."),
},
{
"key": "testing",
"name": "Testing and Characterization: Measuring the Invisible",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"You cannot improve what you cannot measure, and at the micro-scale "
"measurement is its own discipline. Optical microscopes hit the "
"diffraction limit: at 550 nm wavelength and 0.9 numerical aperture, two "
"points closer than 0.37 um blur into one - fine for watching a "
"100 um robot, blind to its nanometre flexures. Scanning electron "
"microscopes see nanometres but need vacuum (no live water, no moving "
"air) and coat insulators in metal. White-light interferometry profiles "
"surface heights to ~1 nm for checking etch depths and released gaps; "
"laser Doppler vibrometry watches a 5.4 kHz cantilever ring without "
"touching it; stroboscopic video freezes kilohertz motion into slow "
"frames. Electrical testing runs on probe stations: needles land on "
"micrometre pads to drive actuators and read sensors before the wafer "
"is diced. The metrology loop closes the design loop: measure the real "
"stiffness, compare to the 0.135 N/m prediction, and tune the process "
"until they agree. This record covers the instruments, their limits, "
"and the measure-compare-tune cycle."),
"how_it_works": (
"Characterize in layers. Geometry first: SEM for lateral dimensions, "
"interferometry or profilometry for heights and depths, cross-sections "
"for layer stacks. Motion second: stroboscopic microscopy for "
"microsecond-scale actuator steps, laser vibrometry for resonant "
"frequencies and mode shapes, high-speed cameras for gaits. Electrical "
"third: probe-station I-V and C-V curves, pull-in voltage measurement "
"(watch for the 6.5 V snap from the actuation record), sensor noise "
"spectra. Environmental fourth: temperature, humidity, and shock "
"chambers for the reliability record's accelerated tests. Every "
"measurement carries uncertainty - the diffraction limit, the probe "
"contact resistance, the calibration of the vibrometer - and honest "
"characterization reports it. The golden rule: measure the quantity the "
"design equation predicts (stiffness, frequency, force), not a proxy, so "
"disagreement points at the model or the process, never at ambiguity."),
"key_points": [
"Diffraction limit (550 nm, NA 0.9): 0.37 um - optical microscopes are blind below it.",
"SEM sees nanometres but needs vacuum; interferometry profiles heights to ~1 nm.",
"Laser vibrometry watches kHz resonators without touching them.",
"Probe stations test actuators/sensors electrically before dicing.",
"Measure what the design equation predicts: disagreement indicts model or process.",
"Report uncertainty honestly: every instrument has limits.",
],
"requirements": [
"MEMS bodies (the structures being measured).",
"Electrostatic actuation (pull-in as a measurable signature).",
"A calculator for the diffraction-limit exercise.",
],
"standards": [
"Measurement uncertainty per the Guide to the Expression of Uncertainty (GUM).",
"Traceable calibration for dimensional metrology.",
],
"citations": [C_MALUF, C_KOVACS, C_SENTURIA],
"sig_lens": (
"Signature take: characterization is Signature truth-seeking - the "
"moment the beautiful equation meets the etched silicon and one of them "
"must confess. The Signature metrologist measures without flinching, "
"reports uncertainty without shame, and tunes the process until the "
"cantilever rings at exactly the frequency the mathematics promised."),
},
{
"key": "energy_limits",
"name": "Energy Scaling Limits: Why Small Robots Can't Carry Big Batteries",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"This record states the field's hardest truth as a theorem: below about "
"a cubic millimetre, carrying energy stops paying and harvesting or "
"receiving it wins. The proof is bookkeeping. Stored energy scales as "
"L^3; the power electronics' overhead does not shrink proportionally; "
"self-discharge and leakage drain small stores faster; and the energy "
"cost of the mission (swim a body length, send a bit) scales weakly "
"with size while the tank collapses with L^3. A 1 mm3 battery's ~1 joule "
"runs a 1 mW robot 18 minutes - a mission, barely. Shrink to 100 um "
"(1e-3 mm3, ~1 mJ) and the same 1 mW lasts about a second: the robot "
"becomes a firework, not a machine. Meanwhile wireless delivery scales "
"with receiver area (L^2) against a load that also shrinks - the link "
"budget in the wireless record stays closable far below the battery "
"crossover. The design consequence is a fork in the road: millibots "
"carry fuel and roam; microrobots take power as a utility (fields, "
"light, ultrasound, chemistry) and the system is designed around the "
"feed, not the tank. This record derives the crossover and maps the "
"fork."),
"how_it_works": (
"Write endurance as stored energy over average power and scale both. "
"E_stored = energy density x L^3; P_avg = duty cycle x P_peak, where "
"P_peak for locomotion scales roughly with drag x speed ~ L^2 x L = L^3 "
"at constant body-lengths-per-second - so endurance looks scale-invariant "
"until the overheads intrude: the regulator's quiescent current, the "
"leakage, the minimum-size package, none of which scale as L^3. Plot "
"endurance versus size and the curve bends down sharply below ~1 mm3 - "
"the demo computes it. Then price the alternatives per the earlier "
"records: wireless inductive at 1 mW continuous (infinite endurance "
"inside the workspace), photovoltaic under a laser (power follows the "
"beam), catalytic from ambient fuel (endurance equals fuel availability). "
"The system architect's decision matrix: mission duration x mobility "
"range x workspace control - pick the power strategy that survives all "
"three, and never let the tank size choose the mission."),
"key_points": [
"Endurance = energy/power: both scale ~L^3, but overheads do not - small loses.",
"1 mm3 battery: 18 min at 1 mW; 100 um robot's share: ~1 second.",
"Wireless delivery scales as L^2 vs an L^3-shrinking load: the link stays closable.",
"Fork: millibots carry fuel and roam; microrobots take power as a utility.",
"Design the system around the feed, not the tank, below ~1 mm3.",
"Mission duration x range x workspace control: the power-strategy decision matrix.",
],
"requirements": [
"Powering micro-robots (the battery budget).",
"Wireless power (the utility alternative).",
"A calculator for the endurance-crossover exercise.",
],
"standards": [
"Energy reporting per watt-hour and power-density conventions.",
"Mission-profile discipline (duration, range, duty cycle specified up front).",
],
"citations": [C_SITTI, C_DILLER, C_PURCELL],
"sig_lens": (
"Signature take: the energy limit is the Signature law of small "
"journeys - no vessel carries more voyage than its hull can hold, and "
"the wise captain refuels from the sea itself. Signature power "
"architecture never apologizes for the feed: a robot drinking from a "
"field is not dependent, it is connected - the way a city is connected "
"to its grid."),
},
{
"key": "economics_roadmap",
"name": "Economics and Roadmap: From Lab Curiosity to Micro-Robot Industry",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Microrobotics becomes an industry when the tenth thousand robot costs "
"less than the value of its work. The cost curve is the semiconductor "
"learning curve: unit cost falls ~20% per doubling of cumulative volume "
"(80% learning rate), so a robot costing $100 at 10,000 units costs about "
"$10.82 at 10 million units - the demo runs the exponent. The fixed "
"costs dominate early: a MEMS mask set runs ~$50,000, amortized to $0.05 "
"per unit at a million units but $50 at a thousand - prototype economics "
"punish small runs, production economics reward commitment. Foundry "
"access (multi-project wafers) lets startups prototype for thousands, "
"not millions. Markets open in order of value density: medical (a "
"targeted-delivery robot earns its cost in one procedure), inspection "
"(a pipeline crawler earns it in one avoided shutdown), then consumer "
"and environmental at high volumes. The roadmap: tethered lab demos "
"today, supervised wireless systems this decade, autonomous swarms when "
"power and control cross their thresholds. This record prices the field "
"and charts the path from bench to industry."),
"how_it_works": (
"Price the robot as: (non-recurring engineering / volume) + (wafer cost / "
"die per wafer / yield) + package + test. At low volume the first term "
"dominates - share it via multi-project wafers. At high volume the "
"second term dominates - improve yield (the self-assembly record's "
"binomial math) and die-per-wafer (the microfabrication record's batch "
"economics). The learning curve compounds: each doubling of cumulative "
"production cuts cost 20% through yield learning, process tuning, and "
"automation. Market entry follows willingness to pay per robot: medical "
"devices tolerate $1,000+ per unit (regulated, high value), industrial "
"inspection $10-100 (payback in avoided downtime), environmental and "
"consumer <$1 (only at tens of millions of units). The roadmap gates are "
"technical: untethered power (the energy record's crossover), closed-loop "
"control without microscopes (the control record's limits), and "
"reliability at scale (the reliability record's Weibull math) - each gate "
"passed unlocks the next market tier."),
"key_points": [
"80% learning curve: $100 at 10k units -> $10.82 at 10M units.",
"$50k mask set: $50/unit at 1k units, $0.05 at 1M - volume rewards commitment.",
"Multi-project wafers let startups prototype for thousands, not millions.",
"Markets open by value density: medical, then inspection, then high-volume.",
"Roadmap gates: untethered power, microscope-free control, reliability at scale.",
"Unit cost = NRE/volume + wafer/die/yield + package + test.",
],
"requirements": [
"Energy scaling limits (the power gate on the roadmap).",
"Reliability at the micro-scale (the quality gate).",
"A calculator for the learning-curve exercise.",
],
"standards": [
"Cost modeling per semiconductor industry practice.",
"Technology readiness level (TRL) discipline for roadmap gating.",
],
"citations": [C_MADOU, C_JUDY, C_NELSON],
"sig_lens": (
"Signature take: the roadmap is the Signature promise kept in stages - "
"no hype, only gates, each opened by physics, not by press release. "
"Signature economics respects the learning curve the way a farmer "
"respects the seasons: plant the mask set, tend the yield, harvest at "
"volume, and never promise the tenth thousand robots before the first "
"hundred have earned their keep."),
},
]

assert len(ENTRIES) == 32, "expected 32 entries, got %d" % len(ENTRIES)
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries not in ladder order"
tiers = [e["ladder_tier"] for e in ENTRIES]
assert tiers == sorted(tiers, key=lambda t: {"foundations": 0, "compounded": 1, "advanced": 2}[t]), "tiers not ordered"
