#!/usr/bin/env python3
"""Entries for the Turbomachinery field databases (field #20, taxonomy order).

Verified 2026-10-17: NO database covers turbomachinery as a discipline.
- Manifest-wide regex search (turbo|turbine|compressor|pump|cavitat|blade|
  cascade|rotordyn|fan): zero database hits across all 2340 databases.
- Fields #11-19 shard indexes (volcanology, climatology,
  atmospheric-science, hydrology, meteorology, calculus, combinatorics,
  econometrics, psychometrics): direct whole-shard title scans - the only
  hits are false positives on the substring "surge" ("Hurricane Forecasting:
  Track Models, the Cone, and Storm Surge" - storm surge; "Pyroclastic Flows
  and Surges" - pyroclastic surge). Neither is compressor surge, and neither
  rises to the discipline: no Euler turbine equation, no velocity triangles,
  no specific speed, no affinity laws, no cascades, no cavitation/NPSH, no
  rotordynamics.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main repo
  rebuilt 2026-10-17 08:04 UTC, covering fields through #10; fields #11-19
  cross-checked directly above): every record checked + admitted at build
  time.

So this build creates two NEW databases, 37 ladder-ordered records each:

  turbomachinery             - The Turbomachinery Database
                               (public-harvest: real, fact-checked
                               turbomachinery; citations Dixon & Hall,
                               Cumpsty, Logan, Japikse & Baines,
                               Saravanamuttoo/Rogers/Cohen, Wilson &
                               Korakianitis, Cengel & Boles, White,
                               Stepanoff, Karassik, Bleier, Hydraulic
                               Institute, API 610, ISO 10816)
  turbomachinery-signature   - The Turbomachinery Signature Database
                               (his original Signature interpretation of the
                               discipline; src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

Subtitle disambiguation (fields #13-19 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "The Euler Turbine
Equation: The One Equation That Rules Every Rotor" and "Velocity Triangles:
The Language Every Blade Speaks".
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "turbomachinery, clearly labeled Signature-made, never presented "
            "as authentic public record.")

C_DIXON = ("Dixon, S. L. and Hall, C. A. 'Fluid Mechanics and Thermodynamics "
           "of Turbomachinery', 7th ed. Butterworth-Heinemann, 2013.")
C_CUMPSTY = ("Cumpsty, N. A. 'Compressor Aerodynamics'. Krieger, 2004 "
             "(orig. Longman, 1989).")
C_LOGAN = ("Logan, Earl Jr. 'Turbomachinery: Basic Theory and Applications', "
           "2nd ed. CRC Press, 1993.")
C_JAPIKSE = ("Japikse, David and Baines, Nicholas C. 'Introduction to "
             "Turbomachinery'. Concepts ETI, 1994.")
C_SARAV = ("Saravanamuttoo, H. I. H., Rogers, G. F. C., and Cohen, H. 'Gas "
           "Turbine Theory', 6th ed. Pearson, 2009.")
C_WILSON = ("Wilson, D. G. and Korakianitis, T. 'The Design of High-Efficiency "
            "Turbomachinery and Gas Turbines', 2nd ed. MIT Press, 2014.")
C_CENGEL = ("Cengel, Yunus A. and Boles, Michael A. 'Thermodynamics: An "
            "Engineering Approach', 9th ed. McGraw-Hill, 2019.")
C_WHITE = ("White, Frank M. 'Fluid Mechanics', 9th ed. McGraw-Hill, 2021.")
C_STEPANOFF = ("Stepanoff, A. J. 'Centrifugal and Axial Flow Pumps: Theory, "
               "Design, and Application', 2nd ed. Krieger, 1993.")
C_KARASSIK = ("Karassik, Igor J., Messina, Joseph P., Cooper, Paul, and Heald, "
              "Charles C. 'Pump Handbook', 4th ed. McGraw-Hill, 2008.")
C_BLEIER = ("Bleier, Frank P. 'Fan Handbook: Selection, Application, and "
            "Design'. McGraw-Hill, 1997.")
C_HI = ("Hydraulic Institute. 'ANSI/HI 9.6.x Standards for Rotodynamic Pumps: "
        "Guideline for NPSH Margin'. Hydraulic Institute, current ed.")
C_API610 = ("American Petroleum Institute. 'API Standard 610: Centrifugal Pumps "
            "for Petroleum, Petrochemical and Natural Gas Industries', 12th ed.")
C_ISO10816 = ("ISO 10816-3:2009. 'Mechanical vibration - Evaluation of machine "
              "vibration by measurements on non-rotating parts', Part 3.")

ENTRIES = [
    {
        "key": "what_is_turbomachinery",
        "name": "What Turbomachinery Is: The Machines That Move Fluids Through Spinning Blades",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Turbomachinery is the engineering discipline of machines that exchange "
            "energy with a continuously flowing fluid through the action of rotating "
            "blades. The family splits two ways. Power-producing machines - steam "
            "turbines, gas turbines, wind turbines, hydraulic turbines - take energy "
            "OUT of the fluid and deliver shaft power. Power-absorbing machines - "
            "compressors, pumps, fans, blowers - take shaft power IN and add energy "
            "TO the fluid, raising its pressure. What unites them is the mechanism: "
            "a rotor carrying blades turns inside a casing, and the fluid's tangential "
            "momentum changes as it passes through the blade rows. That change of "
            "swirl, multiplied by blade speed, is work - the Euler turbine equation, "
            "which governs every member of the family. Turbomachines handle the "
            "world's energy: nearly all electricity is generated by turbines, nearly "
            "all pumped water and compressed air moves through rotodynamic machines, "
            "and every jet engine is a gas turbine with a fan on the front."
        ),
        "how_it_works": (
            "A turbomachine works by controlled deflection of a fluid stream. Fluid "
            "enters the rotor with some absolute velocity; the blades, moving at "
            "tangential speed U, see the fluid arriving at a relative velocity W. The "
            "curved blade passages turn the flow, changing its tangential (swirl) "
            "component C-theta. By Newton's second law applied to angular momentum, "
            "the torque on the fluid equals the mass flow rate times the change in "
            "angular momentum, and power equals torque times rotational speed. In a "
            "turbine the fluid leaves with LESS swirl than it entered with, so the "
            "fluid does work on the blades. In a compressor or pump the rotor ADDS "
            "swirl, so the shaft does work on the fluid. Stators - stationary blade "
            "rows between rotors - redirect the flow and, in turbines, convert "
            "pressure into velocity (nozzles); in compressors, diffusers convert "
            "velocity back into pressure. The whole discipline is the quantitative "
            "management of these velocity triangles."
        ),
        "key_points": [
            "Turbomachines exchange energy with a flowing fluid via rotating blades; the mechanism is change of tangential momentum.",
            "Power machines (turbines) extract energy from the fluid; absorbing machines (compressors, pumps, fans) add energy to it.",
            "The Euler turbine equation - work equals blade speed times change in swirl velocity - governs the entire family.",
            "Rotors add or extract swirl; stators redirect flow and trade pressure for velocity (nozzles) or velocity for pressure (diffusers).",
            "Turbines generate nearly all the world's electricity; compressors, pumps, and fans move nearly all its fluids.",
        ],
        "requirements": [
            "No prior background needed - this is the first rung of the ladder.",
            "Comfort with the idea that a spinning blade can push a fluid, or be pushed by it.",
            "Basic arithmetic; the mathematics builds gently from here.",
        ],
        "standards": [
            "Terminology follows Dixon & Hall: rotor/stator, absolute/relative velocity, stage.",
            "Power-producing vs power-absorbing is the primary classification used throughout.",
        ],
        "citations": [C_DIXON, C_LOGAN, C_JAPIKSE],
        "sig_lens": (
            "Signature take: the blade is the Signature instrument of energy - a "
            "shaped surface that negotiates between spin and stream. His Signature "
            "framing treats every turbomachine as an energy bargain struck in "
            "rotating geometry: the fluid offers momentum, the blade sets the terms."
        ),
    },
    {
        "key": "fluid_mechanics_foundation",
        "name": "The Fluid Mechanics Foundation: Pressure, Velocity, and the Duct",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Before blades can be understood, the fluid itself must be: how pressure "
            "and velocity trade places as a fluid moves through passages. Two ideas "
            "carry the whole load. Continuity: in steady flow, what flows in must flow "
            "out, so mass flow rate rho*A*V is constant along a duct - squeeze the "
            "area and the velocity must rise. Bernoulli (for incompressible, steady, "
            "frictionless flow along a streamline): static pressure plus dynamic "
            "pressure, p + rho*V^2/2, is constant - so when velocity rises, static "
            "pressure falls. A nozzle accelerates flow and drops pressure; a diffuser "
            "decelerates flow and recovers pressure. Every blade passage in every "
            "turbomachine is, at heart, a tiny nozzle or diffuser, and the pressure "
            "fields the blades feel are Bernoulli fields bent around curved walls. "
            "Real flows add friction and compressibility, but continuity plus "
            "Bernoulli is the skeleton everything else hangs on."
        ),
        "how_it_works": (
            "Consider air flowing steadily through a converging duct. Continuity "
            "fixes the velocity ratio: V2 = V1*(A1/A2), so halving the area doubles "
            "the velocity. Bernoulli then fixes the pressure change: p2 = p1 - "
            "rho*(V2^2 - V1^2)/2, so the pressure drops by the gain in dynamic "
            "pressure. In a real machine the same trade happens inside blade "
            "passages: turbine nozzle passages converge, accelerating the flow and "
            "converting pressure energy into kinetic energy that the rotor then "
            "harvests. Compressor and pump diffuser passages diverge, slowing the "
            "flow and converting kinetic energy back into pressure - pressure "
            "recovery. Friction steals a little total pressure along the way (that "
            "is loss), and at high speeds compressibility means density changes too, "
            "but the continuity-Bernoulli skeleton predicts the first-order "
            "behavior of every passage in the machine."
        ),
        "key_points": [
            "Continuity: mass flow rho*A*V is constant along a duct - smaller area means higher velocity.",
            "Bernoulli: p + rho*V^2/2 is constant along a streamline - higher velocity means lower static pressure.",
            "Nozzles trade pressure for velocity; diffusers trade velocity back for pressure.",
            "Every blade passage is a small nozzle or diffuser; blade pressure fields are Bernoulli fields around curved walls.",
            "Friction and compressibility modify the picture but do not replace the skeleton.",
        ],
        "requirements": [
            "Familiarity with pressure, velocity, and density as physical quantities.",
            "High-school algebra: squaring, ratios, rearranging formulas.",
        ],
        "standards": [
            "Incompressible Bernoulli stated with its assumptions: steady, inviscid, along a streamline.",
            "SI units throughout: pressure in pascals, velocity in m/s, density in kg/m^3.",
        ],
        "citations": [C_WHITE, C_DIXON],
        "sig_lens": (
            "Signature take: pressure and velocity are the two currencies of the "
            "fluid economy, and every passage is a money-changer. His Signature "
            "framing reads the duct as the blade's classroom - master the "
            "nozzle-diffuser trade here, and every rotor downstream is just the "
            "same lesson, spinning."
        ),
    },
    {
        "key": "conservation_laws",
        "name": "The Conservation Laws: Mass, Momentum, and Energy Across the Machine",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Turbomachinery analysis rests on three conservation laws applied to a "
            "control volume wrapped around the machine. Conservation of mass: the "
            "mass flow in equals the mass flow out in steady operation - the "
            "accountant's rule that fixes velocities from areas. Conservation of "
            "momentum: the force on the fluid equals the mass flow times the change "
            "in velocity vector - the rule that turns flow turning into blade force, "
            "and blade force into torque. Conservation of energy (the steady-flow "
            "energy equation): heat added minus shaft work equals the mass flow "
            "times the change in stagnation enthalpy plus changes in kinetic and "
            "potential energy. For turbomachines the dominant term is the shaft work "
            "and the stagnation enthalpy change, which is exactly what the Euler "
            "turbine equation computes from the velocity triangles. These three "
            "laws are not approximations - they are the audit that every design "
            "calculation, every CFD result, and every test measurement must pass."
        ),
        "how_it_works": (
            "Wrap an imaginary box around a compressor rotor. Mass conservation "
            "says m_dot_in = m_dot_out = m_dot; with known inlet density and area, "
            "the through-flow velocity is fixed. Momentum conservation in the "
            "tangential direction says the torque on the fluid is m_dot times the "
            "change in (radius times tangential velocity) - r*C-theta - between "
            "outlet and inlet; multiply by shaft speed omega and you have the shaft "
            "power, which is the Euler equation in disguise. Energy conservation "
            "says the shaft work per unit mass equals the rise in stagnation "
            "enthalpy, h02 - h01 (kinetic and potential changes being small by "
            "comparison for most machines). So a compressor designer who wants 150 "
            "kJ/kg of pressure rise knows immediately the shaft must supply 150 "
            "kJ/kg of work - no blade geometry can change that ledger, only how "
            "efficiently the work is converted. The conservation laws set the "
            "budget; the blading decides how much of the budget survives as useful "
            "pressure rise versus loss."
        ),
        "key_points": [
            "Mass: steady m_dot_in = m_dot_out - fixes velocities from areas and density.",
            "Tangential momentum: torque = m_dot * change in (r * C-theta) - flow turning becomes shaft torque.",
            "Energy: shaft work per unit mass = stagnation enthalpy rise (compressor) or drop (turbine).",
            "The conservation laws set an inviolable budget; blade design decides how much survives as useful work.",
            "Every design calculation and test measurement must satisfy all three - they are the audit, not an approximation.",
        ],
        "requirements": [
            "The fluid-mechanics foundation record (pressure-velocity trade).",
            "Comfort with 'per unit mass' quantities (kJ/kg) and mass flow rate (kg/s).",
        ],
        "standards": [
            "Control-volume forms per White; steady-flow energy equation per Cengel & Boles.",
            "Sign convention stated explicitly: work done BY the fluid is positive for turbines.",
        ],
        "citations": [C_WHITE, C_CENGEL, C_DIXON],
        "sig_lens": (
            "Signature take: conservation is the Signature audit - nothing enters "
            "or leaves the ledger uncounted. His Signature framing treats the "
            "control volume as a contract: the fluid signs in mass, momentum, and "
            "energy, and the machine must account for every unit."
        ),
    },
    {
        "key": "euler_turbine_equation",
        "name": "The Euler Turbine Equation: The One Equation That Rules Every Rotor",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The Euler turbine equation is the single most important equation in "
            "turbomachinery: the specific work exchanged between rotor and fluid "
            "equals the blade speed times the change in tangential fluid velocity, "
            "w = U * (C-theta_1 - C-theta_2) for a turbine (work done BY the fluid), "
            "with the signs reversed for a compressor. It comes straight from "
            "conservation of angular momentum: torque is mass flow times change in "
            "angular momentum r*C-theta, and power is torque times angular speed. "
            "Its power is its generality - it cares nothing about blade shape, "
            "losses, or fluid properties. If you know the blade speed and how much "
            "swirl the rotor adds or removes, you know the work, period. Turbine "
            "designers chase large turning (big C-theta change); compressor "
            "designers are limited by how much swirl they can add before the flow "
            "separates. Every performance calculation in the discipline either uses "
            "this equation or answers to it."
        ),
        "how_it_works": (
            "Picture a turbine rotor with blade speed U = 300 m/s at the mean "
            "radius. The nozzle delivers flow with tangential velocity C-theta_1 = "
            "500 m/s; the rotor turns the flow so it leaves with C-theta_2 = 100 "
            "m/s. The Euler equation says each kilogram of fluid gives up "
            "w = 300 * (500 - 100) = 120,000 J/kg = 120 kJ/kg of work. With a mass "
            "flow of 50 kg/s, the shaft power is 6 MW - from one line of arithmetic. "
            "The equation also explains the designer's dilemma: more work wants "
            "more turning, but turning the flow too aggressively makes it separate "
            "from the blade suction surface, and separated flow is loss. So the "
            "whole art of blading is achieving the Euler work with the least "
            "aerodynamic violence. For a compressor the same equation with "
            "reversed sign says the shaft must supply U*(C-theta_2 - C-theta_1) - "
            "and the rise in stagnation enthalpy equals exactly that work."
        ),
        "key_points": [
            "w = U*(C-theta_1 - C-theta_2): specific work equals blade speed times swirl change (turbine sign convention).",
            "Derived from angular momentum conservation - no empiricism, no blade-shape dependence.",
            "Turbines want large flow turning; compressors are limited by separation - the central design tension.",
            "Shaft power = m_dot * w; stagnation enthalpy change = w (adiabatic).",
            "Every performance estimate in turbomachinery either uses Euler or answers to it.",
        ],
        "requirements": [
            "The conservation-laws record (angular momentum).",
            "Understanding of tangential velocity and blade speed U = omega*r.",
        ],
        "standards": [
            "Subscript 1 = rotor inlet, 2 = rotor outlet; C-theta positive in the direction of rotation.",
            "Work positive when done BY the fluid (turbine); state the convention whenever signs are used.",
        ],
        "citations": [C_DIXON, C_LOGAN, C_JAPIKSE],
        "sig_lens": (
            "Signature take: Euler wrote the Signature contract between spin and "
            "swirl in one line. His Signature framing treats the equation as the "
            "discipline's constitution - every blade, from a wind turbine to a jet "
            "engine compressor, governs itself by it."
        ),
    },
    {
        "key": "velocity_triangles",
        "name": "Velocity Triangles: The Language Every Blade Speaks",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Velocity triangles are the working drawings of turbomachinery: at any "
            "point on a blade, three velocity vectors form a triangle - the absolute "
            "fluid velocity C (what a stationary observer sees), the blade speed U "
            "(tangential, known from rpm and radius), and the relative velocity W = "
            "C - U (what the moving blade actually feels). The flow angles follow: "
            "alpha is the absolute flow angle measured from the axial (or radial) "
            "direction, beta the relative flow angle. The blade's inlet metal angle "
            "must roughly match the incoming relative flow angle beta_1, or the flow "
            "strikes the leading edge at incidence and separates. The triangle at "
            "rotor inlet plus the triangle at rotor outlet, drawn together, shows at "
            "a glance how much the flow turned (the Euler work), whether the "
            "relative velocity diffused (compressor) or accelerated (turbine), and "
            "whether the design is sane. Engineers sketch triangles before they draw "
            "blades - the triangle is the design."
        ),
        "how_it_works": (
            "Take an axial turbine stage with blade speed U = 250 m/s and axial "
            "through-flow velocity Cx = 150 m/s (kept roughly constant through the "
            "stage). The nozzle discharges at absolute angle alpha_1 = 70 degrees "
            "from axial, so C-theta_1 = Cx*tan(alpha_1) = 150*2.747 = 412 m/s. The "
            "blade sees relative tangential velocity W-theta_1 = C-theta_1 - U = "
            "162 m/s, arriving at relative angle beta_1 = atan(162/150) = 47.2 "
            "degrees - so the blade leading edge is built near 47 degrees. After "
            "the rotor turns the flow, suppose it leaves with C-theta_2 = 50 m/s; "
            "the Euler work is U*(C-theta_1 - C-theta_2) = 250*362 = 90.5 kJ/kg. "
            "Draw both triangles tip-to-tip on the U vector and the turning is "
            "visible as the horizontal distance between the C vectors. Change any "
            "angle and the work, the blade shape, and the loss all change with it - "
            "which is why the triangle, not the blade, is drawn first."
        ),
        "key_points": [
            "Three vectors: absolute C, blade speed U, relative W = C - U; alpha = absolute angle, beta = relative angle.",
            "The blade feels only W - the inlet metal angle must match the incoming beta_1 to avoid incidence separation.",
            "Inlet and outlet triangles drawn together display flow turning = Euler work at a glance.",
            "Constant axial velocity Cx is the usual first assumption for axial stages; radial machines use radial components.",
            "Engineers sketch triangles before blades: the triangle is the design, the blade is its embodiment.",
        ],
        "requirements": [
            "The Euler turbine equation record.",
            "Basic vector addition/subtraction and trigonometry (tan, atan).",
        ],
        "standards": [
            "Angles measured from the axial direction for axial machines, per Dixon & Hall convention.",
            "Station 1 = rotor inlet, station 2 = rotor outlet, consistently across the database.",
        ],
        "citations": [C_DIXON, C_JAPIKSE, C_LOGAN],
        "sig_lens": (
            "Signature take: the triangle is the Signature sketch - three arrows "
            "that say everything about a blade before a single curve is drawn. His "
            "Signature framing treats velocity triangles as the discipline's "
            "alphabet: learn the letters and every machine becomes readable."
        ),
    },
    {
        "key": "degree_of_reaction",
        "name": "Degree of Reaction: Splitting the Pressure Change Between Rotor and Stator",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Degree of reaction, Lambda, answers a design question: of the stage's "
            "total pressure change, how much happens in the ROTOR versus the "
            "STATOR? Formally it is the static enthalpy change across the rotor "
            "divided by the stage stagnation enthalpy change. Lambda = 0 is an "
            "impulse stage: all the pressure drop happens in the nozzle, the rotor "
            "just turns high-velocity flow at constant relative speed (classic "
            "steam-turbine impulse blading, and the Pelton wheel is the extreme). "
            "Lambda = 0.5 is the 50%-reaction stage: rotor and stator share the "
            "pressure change equally, giving symmetric velocity triangles - the "
            "workhorse of gas turbines and axial compressors. Lambda = 1 would put "
            "everything in the rotor. Reaction shapes everything: blade loading, "
            "efficiency, the pressure the rotor tip seals must hold, and whether "
            "the relative flow accelerates (turbine, kind to boundary layers) or "
            "diffuses (compressor, hostile to boundary layers)."
        ),
        "how_it_works": (
            "For an axial stage with constant axial velocity, reaction has a "
            "triangle-only formula: Lambda = 1 - (C-theta_1 + C-theta_2)/(2*U). "
            "Take U = 250 m/s, C-theta_1 = 200 m/s, C-theta_2 = 50 m/s: Lambda = 1 "
            "- 250/500 = 0.5 - the symmetric 50%-reaction stage, where the inlet "
            "and outlet triangles are mirror images and the rotor and stator do "
            "equal shares of the pressure work. Push C-theta_1 up to 450 with "
            "C-theta_2 = 50: Lambda = 1 - 500/500 = 0 - a pure impulse stage, all "
            "expansion in the nozzle, the rotor merely deflecting the jet. The "
            "choice matters downstream: impulse stages need no pressure-holding "
            "seals at the rotor tip (pressure is constant across the rotor) but "
            "suffer higher kinetic-energy losses; 50%-reaction stages are more "
            "efficient but demand tight tip clearances because pressure falls "
            "across the rotor and wants to leak over the blade tips. Compressor "
            "stages live near 50% reaction for the same symmetry reason, and "
            "because diffusion must be shared to stay attached."
        ),
        "key_points": [
            "Lambda = rotor static enthalpy change / stage stagnation enthalpy change; 0 = impulse, 0.5 = symmetric reaction.",
            "Impulse: all pressure change in the stator/nozzle; rotor only turns flow - simple seals, higher kinetic losses.",
            "50% reaction: equal split, symmetric triangles - the efficient workhorse of gas turbines and axial compressors.",
            "Reaction determines tip-seal duty: pressure drop across the rotor must be sealed or it leaks.",
            "Compressor stages favor ~50% reaction to share the hostile diffusion between blade rows.",
        ],
        "requirements": [
            "The velocity-triangles record.",
            "Static vs stagnation enthalpy distinction.",
        ],
        "standards": [
            "Lambda defined on static-to-stagnation basis per Dixon & Hall.",
            "Impulse/ reaction terminology per steam-turbine convention (Parsons vs de Laval).",
        ],
        "citations": [C_DIXON, C_LOGAN, C_WILSON],
        "sig_lens": (
            "Signature take: reaction is the Signature negotiation - who does the "
            "pressure work, the spinner or the stander? His Signature framing "
            "treats Lambda as the fairness dial of the stage: 0 keeps all the "
            "power with the nozzle, 0.5 splits it blade-and-blade."
        ),
    },
    {
        "key": "turbomachinery_family",
        "name": "The Turbomachinery Family: Turbines, Compressors, Pumps, and Fans",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The family has four great branches, distinguished by what they do to "
            "the fluid and what fluid they handle. Turbines extract work: steam "
            "turbines (power stations), gas turbines (jets, peaking power), wind "
            "turbines (renewables), hydraulic turbines (dams) - all expand a fluid "
            "from high to low pressure and harvest the swirl change. Compressors "
            "absorb work to raise gas pressure: axial compressors (jet engines, "
            "large industrial), centrifugal compressors (turbochargers, process "
            "plants, refrigeration). Pumps absorb work to raise liquid pressure or "
            "lift it: centrifugal and axial-flow (rotodynamic) pumps move water, "
            "oil, chemicals by the megaton; positive-displacement pumps (piston, "
            "gear, screw) force fixed volumes for metering and high pressure. Fans "
            "and blowers move large gas volumes against small pressure rises: "
            "cooling, ventilation, combustion air. Same Euler equation, same "
            "triangles - the branches differ in fluid (compressible gas vs "
            "incompressible liquid), pressure ratio, and whether the machine gives "
            "or takes shaft power."
        ),
        "how_it_works": (
            "The branches are separated by the sign of the Euler work and the "
            "compressibility of the fluid. A steam turbine takes 10 MPa, 500 C "
            "steam, expands it to 10 kPa condenser pressure, and each kilogram "
            "surrenders over a megajoule of enthalpy as shaft work - the fluid "
            "leaves with less swirl and less pressure. An axial compressor does "
            "the reverse: the shaft drives swirl INTO the air, raising its "
            "stagnation pressure stage by stage, pressure ratio 30:1 or more in a "
            "modern jet engine core. A centrifugal water pump adds head - pressure "
            "expressed as a liquid column - typically tens to hundreds of meters, "
            "with water treated as incompressible so density stays put. A fan moves "
            "air at pressure rises of a few kilopascals, where even air is nearly "
            "incompressible. The designer picks the branch by duty: need shaft "
            "power OUT? turbine. Need pressure UP in a gas? compressor. Liquid? "
            "pump. Huge volume, tiny pressure? fan. The velocity triangles then "
            "tell whether the chosen machine is drawn correctly."
        ),
        "key_points": [
            "Turbines extract shaft work by expanding fluid; compressors/pumps/fans absorb shaft work to pressurize fluid.",
            "Compressors handle compressible gases; pumps handle (nearly) incompressible liquids; fans move gas at low pressure rise.",
            "Steam/gas/wind/hydro turbines; axial/centrifugal compressors; rotodynamic vs positive-displacement pumps.",
            "The Euler equation and velocity triangles apply identically to all four branches.",
            "Branch selection follows the duty: power out = turbine, gas pressure up = compressor, liquid pressure up = pump, volume at low pressure = fan.",
        ],
        "requirements": [
            "The 'what is turbomachinery' record.",
            "Rough sense of pressure units (kPa, MPa) and the idea of compressible vs incompressible flow.",
        ],
        "standards": [
            "Rotodynamic vs positive-displacement is the primary pump classification per the Hydraulic Institute.",
            "Turbine types named by working fluid: steam, gas, wind, hydraulic.",
        ],
        "citations": [C_JAPIKSE, C_LOGAN, C_KARASSIK],
        "sig_lens": (
            "Signature take: one family, four temperaments - the harvesters and "
            "the lifters. His Signature framing sees the branches as the same "
            "blade-physics wearing different work clothes: the turbine gathers, "
            "the compressor climbs, the pump heaves, the fan breathes."
        ),
    },
    {
        "key": "flow_geometries",
        "name": "Axial, Radial, and Mixed Flow: Three Geometries, One Physics",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Turbomachines come in three flow geometries, named for the path the "
            "fluid takes through the rotor. Axial machines: the flow enters and "
            "leaves moving mostly parallel to the shaft axis - jet-engine "
            "compressors and turbines, large steam turbines, axial pumps and fans. "
            "They stage easily (row after row along the axis), handle huge volume "
            "flows, and give modest pressure change per stage. Radial (centrifugal) "
            "machines: the flow enters axially and leaves radially outward "
            "(centrifugal compressors and pumps) or enters radially and leaves "
            "axially (radial-inflow turbines like turbocharger turbines). The "
            "radius change itself does work - the U in the Euler equation differs "
            "between inlet and outlet - so a single radial stage achieves a far "
            "larger pressure ratio than an axial stage. Mixed-flow machines split "
            "the difference, leaving at a cone angle between axial and radial. "
            "Geometry choice follows specific speed: low specific speed duties "
            "want radial, high want axial, the middle wants mixed."
        ),
        "how_it_works": (
            "The geometry changes the Euler equation's form. In an axial stage the "
            "blade speed U is nearly the same at inlet and outlet (same radius), so "
            "work is U times the swirl change. In a centrifugal compressor the flow "
            "enters near the shaft at small radius (small U_1) and leaves at the "
            "impeller tip at large radius (large U_2): work = U_2*C-theta_2 - "
            "U_1*C-theta_1, and the radius change contributes directly - a single "
            "impeller with tip speed 500 m/s can deliver a pressure ratio of 4:1 "
            "or more, where an axial stage manages ~1.3:1. That is why turbochargers "
            "and small gas turbines are centrifugal (few stages, compact, rugged) "
            "while large jet engines and power-station steam turbines are axial "
            "(many stages, high efficiency at huge flows). The through-flow path "
            "also sets the mechanical design: axial rotors are long drums or discs "
            "stacked on a shaft; centrifugal impellers are single shrouded or "
            "open wheels that must contain enormous centrifugal stress at the tip."
        ),
        "key_points": [
            "Axial: flow parallel to the shaft; many stages, huge flows, modest pressure ratio per stage.",
            "Radial/centrifugal: flow turns from axial to radial; radius change adds work - high pressure ratio per stage.",
            "Mixed flow: the compromise geometry for the middle of the specific-speed range.",
            "Small machines favor centrifugal (compact, rugged); large machines favor axial (efficient at huge flows).",
            "Geometry follows specific speed - the dimensionless selector covered later on the ladder.",
        ],
        "requirements": [
            "The turbomachinery-family record.",
            "The Euler equation in its general form (U_2*C-theta_2 - U_1*C-theta_1).",
        ],
        "standards": [
            "'Centrifugal' and 'radial' used interchangeably for outward-flow machines per common usage.",
            "Stage pressure ratios quoted as typical ranges, not guarantees: axial 1.15-1.35, centrifugal up to 4+.",
        ],
        "citations": [C_DIXON, C_JAPIKSE, C_WILSON],
        "sig_lens": (
            "Signature take: three roads for the fluid - straight through, flung "
            "outward, or the diagonal between. His Signature framing treats "
            "geometry as the machine's posture: axial stands tall in a line, "
            "radial crouches and hurls, mixed-flow leans into the turn."
        ),
    },
    {
        "key": "dimensionless_performance",
        "name": "Dimensionless Performance: The Flow, Head, and Power Coefficients",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Three dimensionless numbers collapse the performance of all "
            "geometrically similar turbomachines onto single curves. The flow "
            "coefficient phi = Q/(N*D^3) (volume flow scaled by speed and size); "
            "the head coefficient psi = g*H/(N^2*D^2) (pressure rise scaled by the "
            "blade-speed dynamic head); the power coefficient lambda = P/(rho*N^3*"
            "D^5) (power scaled by size and speed). Two machines that are scale "
            "copies of each other, running at the same phi, develop the same psi "
            "and lambda - a laboratory model predicts the full-size prototype, "
            "and a pump catalog curve applies to every size in the family. "
            "Efficiency, being already dimensionless, plots against phi as a single "
            "curve too. These coefficients are why a test on a 30 cm model fan "
            "certifies a 3 m industrial fan: the physics has no preferred size, "
            "only preferred proportions."
        ),
        "how_it_works": (
            "Take a centrifugal pump: D = 0.3 m, N = 1450 rpm = 24.17 rev/s, "
            "delivering Q = 0.05 m^3/s. phi = 0.05/(24.17 * 0.027) = 0.0766. At "
            "its best-efficiency point it makes H = 22 m of head: psi = "
            "9.81*22/(24.17^2 * 0.09) = 215.8/52.6 = 4.10. Now scale the design up "
            "by factor 2 (D = 0.6 m) at the same speed: the same phi demands Q = "
            "0.0766 * 24.17 * 0.216 = 0.40 m^3/s (8x the flow - the cube law), and "
            "the same psi gives H = 4.10 * 52.6 * 0.36/9.81... precisely, H = psi*"
            "N^2*D^2/g = 4.10*584.3*0.36/9.81 = 87.9 m (4x the head - the square "
            "law). The model test predicted the prototype exactly, because "
            "dimensionless performance is scale-invariant. Pump and fan makers "
            "publish one dimensionless curve per impeller family and generate "
            "every catalog size from it - the coefficients are the product line."
        ),
        "key_points": [
            "phi = Q/(N D^3): dimensionless flow; psi = gH/(N^2 D^2): dimensionless head; lambda = P/(rho N^3 D^5): dimensionless power.",
            "Geometrically similar machines at equal phi share psi, lambda, and efficiency - one curve serves the whole size family.",
            "Model tests predict prototypes: scale-invariant physics, no preferred size.",
            "Flow scales with the cube of size, head with the square, power with the fifth - at fixed speed.",
            "Catalog curves for pump/fan families are published dimensionless and scaled per size.",
        ],
        "requirements": [
            "The flow-geometries record.",
            "Dimensional analysis comfort: checking that combinations like Q/(N D^3) are unitless.",
        ],
        "standards": [
            "N in revolutions per second for dimensionless forms; state units whenever dimensional forms appear.",
            "Head H in meters of the pumped fluid; pressure rise = rho*g*H.",
        ],
        "citations": [C_DIXON, C_STEPANOFF, C_LOGAN],
        "sig_lens": (
            "Signature take: the coefficients are the Signature fingerprints - "
            "size washes out, proportion remains. His Signature framing treats "
            "phi, psi, lambda as the machine's true name: call a pump by its "
            "coefficients and you have named every sibling it will ever have."
        ),
    },
    {
        "key": "specific_speed",
        "name": "Specific Speed and Specific Diameter: The Machine Selector's Compass",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Specific speed is the number that picks the machine. In dimensionless "
            "form, Ns = N*sqrt(Q)/(g*H)^(3/4): it combines the duty (flow Q, head H) "
            "with the speed N into a single index that is the same for all "
            "geometrically similar machines. Its power is classificatory: low "
            "specific speed means a radial/centrifugal machine is optimal; high "
            "specific speed means axial; the middle means mixed flow. A duty "
            "requiring high head at small flow (Ns ~ 0.3) wants a centrifugal pump "
            "or compressor; a duty with huge flow at low head (Ns ~ 3) wants an "
            "axial machine. Specific diameter Ds = D*(g*H)^(1/4)/sqrt(Q) is its "
            "twin, fixing the size. The Cordier diagram plots the Ns-Ds pairs of "
            "good designs across the whole industry and finds they fall on one "
            "narrow band - Ns*Ds roughly constant - which is the empirical proof "
            "that specific speed, not habit or tradition, should choose the "
            "geometry. Every turbomachinery selection chart is a specific-speed "
            "chart in disguise."
        ),
        "how_it_works": (
            "A water utility needs Q = 0.1 m^3/s lifted H = 60 m, and the motor "
            "runs at N = 1450 rpm = 24.17 rps. Ns = 24.17*sqrt(0.1)/(9.81*60)^"
            "(3/4) = 24.17*0.3162/119.3 = 0.0641 - deep in radial territory, so a "
            "centrifugal pump is the right choice; an axial pump here would be "
            "grossly off its efficient range. Change the duty to Q = 2 m^3/s at "
            "H = 6 m (flood control): Ns = 24.17*1.414/21.2 = 1.61 - axial "
            "territory, so an axial-flow pump. The twin number sizes it: good "
            "designs sit near Ns*Ds ~ 2.5-3, so Ds ~ 2.75/0.0641 = 42.9 for the "
            "first duty, giving D = 42.9*sqrt(0.1)/(9.81*60)^(1/4) = 42.9*0.3162/"
            "4.94 = 2.75 m - a large slow centrifugal, which matches reality for "
            "this duty. Pump catalogs quote specific speed in dimensional US units "
            "(rpm, gpm, ft): radial below ~4000, mixed 4000-8000, axial above ~8000 "
            "- same physics, different ruler."
        ),
        "key_points": [
            "Ns = N sqrt(Q)/(gH)^(3/4): one dimensionless number combining duty and speed, invariant across similar machines.",
            "Low Ns -> radial/centrifugal geometry; high Ns -> axial; middle -> mixed flow.",
            "Ds = D (gH)^(1/4)/sqrt(Q) fixes the efficient size; good designs cluster near Ns*Ds ~ 2.5-3 (Cordier band).",
            "Dimensional US-unit form (N in rpm, Q in gpm, H in ft): radial < ~4000, mixed 4000-8000, axial > ~8000.",
            "Every selection chart is a specific-speed chart in disguise - compute Ns before choosing anything.",
        ],
        "requirements": [
            "The dimensionless-performance record (phi, psi).",
            "Square roots and fractional exponents.",
        ],
        "standards": [
            "Dimensionless Ns used for theory; dimensional US customary quoted where catalogs use it, with units stated.",
            "Pump Ns uses Q and H; turbine Ns uses power: N*sqrt(P)/H^(5/4) - never mix the two.",
        ],
        "citations": [C_DIXON, C_STEPANOFF, C_JAPIKSE],
        "sig_lens": (
            "Signature take: specific speed is the Signature compass - one number "
            "that points at the right machine before a single blade is sketched. "
            "His Signature framing treats Ns as the duty's fingerprint: read it, "
            "and the geometry chooses itself."
        ),
    },
    {
        "key": "affinity_laws",
        "name": "The Affinity Laws: How Speed Changes Everything, Predictably",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The affinity laws predict exactly what happens when you change a "
            "rotodynamic machine's speed: flow varies directly with speed (Q2/Q1 = "
            "N2/N1), head varies with the square (H2/H1 = (N2/N1)^2), and power "
            "varies with the cube (P2/P1 = (N2/N1)^3) - at the same dimensionless "
            "operating point, i.e., the same phi. They fall straight out of the "
            "dimensionless coefficients: hold phi, psi, lambda constant and the "
            "scaling is algebra. Their practical power is enormous: a pump tested "
            "at 1450 rpm is fully characterized at 2900 rpm without retesting; a "
            "variable-speed drive that trims speed 20% cuts flow 20%, head 36%, "
            "and power nearly 50% - the cubic is why variable-speed pumping saves "
            "so much energy. The laws assume the machine stays at the same point "
            "on its dimensionless curve and that efficiency is unchanged, which "
            "holds well for modest speed changes and incompressible machines; "
            "compressibility and Reynolds-number shifts bend them at the edges."
        ),
        "how_it_works": (
            "A centrifugal pump at N1 = 1450 rpm delivers Q1 = 100 L/s at H1 = 40 "
            "m, absorbing P1 = 50 kW. Speed it up to N2 = 1740 rpm (ratio 1.2) on "
            "a variable-frequency drive. Affinity says: Q2 = 100*1.2 = 120 L/s; "
            "H2 = 40*1.44 = 57.6 m; P2 = 50*1.728 = 86.4 kW. The pump's head "
            "curve, originally H = H0 - k*Q^2, transforms to the new speed by "
            "scaling every (Q, H) point: the whole curve marches up and right, and "
            "the best-efficiency point marches with it. Now reverse it: slow to "
            "1160 rpm (ratio 0.8) and power falls to 50*0.512 = 25.6 kW - nearly "
            "halved for a 20% flow reduction. That cubic is the entire economic "
            "case for variable-speed drives in pumping and fan systems. The "
            "caveat: the laws move you along lines of constant phi through the "
            "origin of the Q-H plane, so the new operating point is where the "
            "scaled curve meets the system curve - recompute the intersection, "
            "never assume the duty point rides along unchanged."
        ),
        "key_points": [
            "Q ~ N, H ~ N^2, P ~ N^3 at constant dimensionless operating point (constant phi).",
            "Derived from the dimensionless coefficients - no new physics, just algebra on phi/psi/lambda.",
            "The cubic power law is the economic case for variable-speed drives: 20% slower ~ 50% less power.",
            "The whole H-Q curve scales: every point moves along a constant-phi ray through the origin.",
            "Recompute the system-curve intersection after scaling; compressibility and Reynolds effects bend the laws at the edges.",
        ],
        "requirements": [
            "The dimensionless-performance record.",
            "The idea of a pump curve and a system curve intersecting at the operating point.",
        ],
        "standards": [
            "Stated for rotodynamic (not positive-displacement) machines; speed ratio applied to shaft speed.",
            "Efficiency assumed constant across the speed change - flag as approximate for large changes.",
        ],
        "citations": [C_STEPANOFF, C_KARASSIK, C_BLEIER],
        "sig_lens": (
            "Signature take: the affinity laws are the Signature throttle - one "
            "knob, three predictable consequences. His Signature framing treats "
            "the cubic as energy's honesty: push a little less fluid and the "
            "universe charges you a lot less power."
        ),
    },
    {
        "key": "losses_efficiency",
        "name": "Losses and Efficiency: Where the Energy Goes",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "No turbomachine achieves its Euler work cleanly; losses eat a share "
            "at every step, and efficiency is the accounting. The loss ledger has "
            "standard line items. Profile loss: friction and separation on the "
            "blade surfaces themselves - the boundary layers' tax. Secondary loss: "
            "the endwall vortices and passage vortices where blades meet hub and "
            "casing - the corners' tax. Tip-clearance loss: fluid leaking over the "
            "unshrouded blade tip from pressure side to suction side instead of "
            "doing work - the gap's tax. Leakage and windage: flow slipping through "
            "seals and the drag of the spinning disc in its cavity. For "
            "compressors, shock loss joins at transonic tip speeds. Efficiencies "
            "are defined against ideal references: isentropic efficiency compares "
            "actual work to the work of an isentropic (lossless, adiabatic) process "
            "between the same pressures; polytropic (small-stage) efficiency "
            "removes the pressure-ratio distortion so multistage machines can be "
            "compared fairly. A modern large axial compressor stage runs ~90-92% "
            "polytropic; a good centrifugal pump ~85-90% at its best point."
        ),
        "how_it_works": (
            "Audit a compressor stage swallowing 100 units of shaft work. Profile "
            "loss takes ~3 units - the blade boundary layers dissipate kinetic "
            "energy as heat. Secondary flows take ~2 - the passage vortex scrubs "
            "the endwalls. Tip clearance takes ~1.5 - leakage over the tip does no "
            "turning. Seal leakage and disc windage take ~1 more. About 92.5 units "
            "emerge as useful pressure rise: the stage isentropic efficiency is "
            "~92.5%. Where the loss goes matters as much as its size: loss inside "
            "a turbine rotor reheats the fluid and is partly recovered in later "
            "stages (reheat), while loss in a compressor is pure waste. Designers "
            "fight each line item with specific weapons: controlled-diffusion "
            "airfoils and low incidence for profile loss, endwall contouring and "
            "lean for secondary loss, tight clearances and shrouds for tip loss, "
            "better seals for leakage. The loss audit turns 'improve efficiency' "
            "from a wish into a work list."
        ),
        "key_points": [
            "Standard loss items: profile, secondary, tip-clearance, leakage/windage, shock (transonic compressors).",
            "Isentropic efficiency = actual work / isentropic work between the same pressures; polytropic efficiency is the pressure-ratio-free comparison.",
            "Compressor loss is pure waste; turbine loss partly reheats and is recovered downstream (reheat effect).",
            "Each loss has a design countermeasure: airfoil shaping, endwall contouring, tight clearances, better seals.",
            "The loss audit converts 'improve efficiency' from a wish into an itemized work list.",
        ],
        "requirements": [
            "The Euler equation record (ideal work) and the fluid-mechanics record (boundary layers mentioned).",
            "Isentropic (lossless adiabatic) as a reference process.",
        ],
        "standards": [
            "Isentropic vs polytropic efficiency distinguished per Dixon & Hall; total-to-total vs total-to-static stated.",
            "Loss breakdown quoted as typical ranges for modern axial stages, not guarantees.",
        ],
        "citations": [C_DIXON, C_CUMPSTY, C_WILSON],
        "sig_lens": (
            "Signature take: loss is the Signature toll - every blade pays the "
            "fluid for passage. His Signature framing treats the loss audit as "
            "the machine's confessional: profile, secondary, clearance, leakage - "
            "each line item a named thief, each with a known countermeasure."
        ),
    },
    {
        "key": "steam_turbines",
        "name": "Steam Turbines: Impulse, Reaction, and the Rankine Workhorse",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The steam turbine is the backbone of civilization's electricity: most "
            "of the world's power - coal, nuclear, gas combined-cycle, solar "
            "thermal, geothermal - is a steam turbine turning a generator. It runs "
            "the Rankine cycle: water is pumped to boiler pressure, boiled and "
            "superheated, expanded through the turbine to condenser pressure, and "
            "condensed back to water. Two blading philosophies share the market. "
            "Impulse stages (de Laval heritage): the full stage pressure drop "
            "happens in fixed nozzles, and the rotor buckets merely deflect the "
            "high-velocity jets at constant pressure - rugged, simple sealing. "
            "Reaction stages (Parsons heritage): pressure drops continuously "
            "across both fixed and moving rows at ~50% reaction - more efficient, "
            "tighter clearances. Real machines are multistage axial giants: "
            "high-pressure, intermediate-pressure, and low-pressure cylinders in "
            "series, with reheat between HP and IP and enormous last-stage blades "
            "handling wet steam at the exhaust. Thermal efficiencies reach ~40% "
            "simple, ~60%+ in combined cycle."
        ),
        "how_it_works": (
            "Follow a kilogram of water around a 10 MPa / 500 C reheat Rankine "
            "cycle. The pump pressurizes liquid water (about 10 kJ/kg of work - "
            "liquids are cheap to pump). The boiler/superheater adds ~3270 kJ/kg, "
            "producing superheated steam at h = 3474 kJ/kg. The turbine expands it "
            "to 10 kPa condenser pressure; ideally (isentropically) it leaves at "
            "h = 2154 kJ/kg, so the turbine extracts 1321 kJ/kg. Net work is "
            "1321 - 10 = 1311 kJ/kg against 3270 kJ/kg of heat in: thermal "
            "efficiency ~40%. The expansion crosses the saturation dome, so the "
            "last stages run in wet steam - droplets erode blades, which is why LP "
            "blades get hardened leading edges (Stellite shields) and moisture "
            "separators sit between stages. Reheat - pulling the steam out after "
            "the HP cylinder, reheating it, and expanding again - raises both "
            "efficiency and exhaust dryness, which is why every large plant uses "
            "it. The condenser closes the loop at the lowest achievable pressure, "
            "because every kilopascal shaved off the back pressure is free turbine "
            "work."
        ),
        "key_points": [
            "The Rankine cycle - pump, boiler/superheater, turbine, condenser - is the steam power loop; most world electricity flows through it.",
            "Impulse blading: pressure drop in nozzles only, rotor deflects jets; reaction blading: continuous drop at ~50% reaction, more efficient.",
            "Real plants: HP/IP/LP cylinders in series with reheat; last-stage blades fight wet-steam erosion.",
            "~40% thermal efficiency simple cycle; ~60%+ in combined cycle with a gas turbine topping it.",
            "Condenser pressure is free work - the colder the cooling water, the better the plant.",
        ],
        "requirements": [
            "The conservation-laws record (steady-flow energy equation).",
            "The degree-of-reaction record (impulse vs reaction).",
            "Saturation, superheat, and steam tables as concepts (values are supplied).",
        ],
        "standards": [
            "Cycle analysis on a per-unit-mass basis (kJ/kg); thermal efficiency = net work / heat added.",
            "Wet-steam region handled per standard Rankine analysis with quality x.",
        ],
        "citations": [C_CENGEL, C_DIXON, C_LOGAN],
        "sig_lens": (
            "Signature take: the steam turbine is the Signature engine of the "
            "grid - fire and water negotiated into spinning steel. His Signature "
            "framing treats the Rankine loop as the original energy bargain: boil "
            "at pressure, expand to vacuum, and keep the difference."
        ),
    },
    {
        "key": "gas_turbines",
        "name": "Gas Turbines: The Brayton Cycle Made of Metal",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The gas turbine - the Brayton cycle in hardware - is a compressor, a "
            "combustor, and a turbine on one shaft: it inhales air, squeezes it, "
            "burns fuel in it at constant pressure, and expands the hot gas "
            "through the turbine, which drives the compressor and delivers net "
            "shaft power (or, with a fan and nozzle, jet thrust). The ideal "
            "thermal efficiency depends on one thing above all: pressure ratio, "
            "eta = 1 - rp^(-(gamma-1)/gamma). Real machines add the second great "
            "lever: turbine inlet temperature (TIT) - hotter gas carries more "
            "work per kilogram, which is why first-stage turbine blades are "
            "single-crystal superalloys with internal cooling passages and film-"
            "cooling holes, surviving gas hotter than their own melting point. "
            "Applications split three ways: aircraft propulsion (thrust), "
            "mechanical drive (pipelines, ships), and power generation - where the "
            "exhaust heat feeds a steam bottoming cycle in combined-cycle plants "
            "hitting 60%+ efficiency. A modern large frame machine passes hundreds "
            "of kg/s of air at pressure ratios above 20:1."
        ),
        "how_it_works": (
            "Air enters at 300 K and the axial compressor raises it to pressure "
            "ratio 12:1; ideally the exit temperature is T2 = 300 * 12^0.2857 = "
            "610 K, and the compressor swallows cp*(610-300) = 312 kJ/kg. Fuel "
            "burns at constant pressure, firing the gas to TIT = 1500 K. The "
            "turbine expands it back to ambient pressure: T4 = 1500/12^0.2857 = "
            "738 K, delivering cp*(1500-738) = 766 kJ/kg. Net work is 766 - 312 = "
            "454 kJ/kg against heat added cp*(1500-610) = 894 kJ/kg: thermal "
            "efficiency 50.8% - exactly 1 - 12^(-0.2857), the ideal Brayton "
            "value. Real machines fall short through component inefficiencies and "
            "cooling-air penalties, landing ~35-40% simple cycle. Raising TIT from "
            "1500 K to 1700 K at the same pressure ratio lifts specific work "
            "sharply while barely moving the ideal efficiency - which is why the "
            "industry's fiercest battle is materials and cooling, not pressure "
            "ratio. In an aircraft engine the same core trades some shaft work "
            "for a propelling nozzle: the leftover enthalpy becomes a high-"
            "velocity jet, and thrust is mass flow times jet velocity change."
        ),
        "key_points": [
            "Compressor + combustor + turbine on one shaft: the Brayton cycle as hardware; net work = turbine work minus compressor work.",
            "Ideal efficiency = 1 - rp^(-(gamma-1)/gamma): pressure ratio is the master lever.",
            "Turbine inlet temperature is the second lever: hotter gas, more work per kg - enabled by cooled superalloy blades.",
            "Applications: jet thrust, mechanical drive, power generation; combined cycle pushes past 60% efficiency.",
            "Real simple-cycle efficiency ~35-40%: component losses and cooling air take their cut.",
        ],
        "requirements": [
            "The conservation-laws record and the Euler equation record.",
            "Ideal-gas relations: cp, gamma, isentropic T-p relation.",
        ],
        "standards": [
            "Brayton analysis per Cengel & Boles; pressure ratio defined as compressor exit/inlet stagnation pressure.",
            "TIT = combustor exit / turbine rotor inlet stagnation temperature (firing temperature).",
        ],
        "citations": [C_SARAV, C_CENGEL, C_WILSON],
        "sig_lens": (
            "Signature take: the gas turbine is the Signature breath - inhale, "
            "squeeze, ignite, exhale power. His Signature framing treats the "
            "Brayton machine as controlled continuous explosion: the combustor "
            "is the furnace, the cooled blade the miracle that stands inside it."
        ),
    },
    {
        "key": "wind_turbines",
        "name": "Wind Turbines: Harvesting the Sky Within the Betz Limit",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The wind turbine is a turbine run in reverse service: instead of a "
            "pressurized fluid expanding, a free stream of air gives up part of "
            "its kinetic energy to the rotor. Actuator-disc theory sets the "
            "absolute ceiling: no turbine can extract more than 16/27 = 59.3% of "
            "the wind's kinetic power - the Betz limit - because the slowed air "
            "must still get out of the way downstream. Real three-bladed "
            "horizontal-axis machines peak near Cp ~ 0.45-0.50 at their design tip-"
            "speed ratio (blade tip speed divided by wind speed, typically 7-9). "
            "Power scales with the cube of wind speed and the square of rotor "
            "diameter - P = rho/2 * A * V^3 * Cp - which is why turbines keep "
            "growing taller (stronger, steadier winds aloft) and wider (a 100 m "
            "rotor sweeps ~7,850 m^2). Below rated wind speed the controller "
            "tracks maximum Cp; above it, blades pitch to shed power and hold "
            "rated output; above cut-out speed the machine parks to survive. The "
            "blades are twisted, tapered airfoils - cascades in the open air, "
            "stall-regulated or pitch-regulated."
        ),
        "how_it_works": (
            "Take a 100 m diameter rotor (swept area 7,854 m^2) in a 12 m/s wind "
            "at sea-level density 1.225 kg/m^3. The wind's raw power is 0.5 * "
            "1.225 * 7854 * 12^3 = 8.32 MW. Betz says at most 59.3% is "
            "extractable: 4.93 MW absolute ceiling. A real rotor at Cp = 0.45 "
            "delivers 3.74 MW electrical-ish (before drivetrain losses). The "
            "optimum comes from slowing the wind to 1/3 of its upstream speed at "
            "the disc (axial induction factor a = 1/3) - slow it less and you "
            "leave energy in the stream; slow it more and the stream chokes, "
            "spilling around the rotor. Blade-element theory then distributes "
            "that extraction along the blade: each annular ring of the disc works "
            "its local velocity triangle, with twist built into the blade so the "
            "local angle of attack stays near optimum from root (slow, high "
            "solidity) to tip (fast, slender). Pitch control above rated wind "
            "rotates the whole blade to spill lift - the same stall physics as an "
            "aircraft wing, used here as a safety valve."
        ),
        "key_points": [
            "Betz limit 16/27 = 59.3%: the absolute ceiling on wind-energy extraction; optimum slows wind to 1/3 at the disc.",
            "P = (rho/2) A V^3 Cp: cubic in wind speed, square in diameter - size and site dominate economics.",
            "Three-bladed horizontal-axis machines peak at Cp ~ 0.45-0.50 near tip-speed ratio 7-9.",
            "Blades are twisted tapered airfoils; pitch regulation sheds power above rated wind, parks above cut-out.",
            "Actuator-disc theory gives the limit; blade-element/momentum theory designs the blade to approach it.",
        ],
        "requirements": [
            "The fluid-mechanics foundation record (dynamic pressure).",
            "The velocity-triangles record (angle of attack idea).",
        ],
        "standards": [
            "Cp defined against the undisturbed upstream wind power through the swept area.",
            "Betz derivation per actuator-disc momentum theory; stated assumptions (inviscid, 1-D, infinite blades).",
        ],
        "citations": [C_DIXON, C_WHITE, C_JAPIKSE],
        "sig_lens": (
            "Signature take: the wind turbine is the Signature sail - it does "
            "not chase the wind, it taxes it. His Signature framing treats Betz "
            "as nature's tariff schedule: 59.3% is all the sky will ever "
            "surrender, and the blade's whole art is collecting it gracefully."
        ),
    },
    {
        "key": "hydraulic_turbines",
        "name": "Hydraulic Turbines: Pelton, Francis, and Kaplan by Head and Flow",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Hydraulic turbines convert the pressure and elevation of water into "
            "shaft power at the world's dams, and the choice among the three great "
            "types is pure specific speed. The Pelton wheel (impulse): a high-"
            "pressure jet from a nozzle strikes double-cup buckets on the wheel "
            "rim at atmospheric pressure - the extreme impulse machine, Lambda = "
            "0, for high head and low flow (hundreds of meters, alpine plants). "
            "The Francis turbine (reaction, mixed-flow): water spirals inward "
            "through guide vanes into a runner that turns radial-inward flow into "
            "axial outflow, with pressure dropping across the runner - the "
            "workhorse for medium heads (tens to hundreds of meters) and the most "
            "common large hydro machine on earth. The Kaplan turbine (reaction, "
            "axial, with adjustable blades): for low head and huge flow (a few "
            "meters to tens of meters), its propeller-like runner with variable-"
            "pitch blades plus adjustable guide vanes holds efficiency across "
            "wildly varying river flows. A draft tube below every reaction "
            "turbine recovers the exit kinetic energy and lets the runner sit "
            "above tailwater without losing head."
        ),
        "how_it_works": (
            "Head and flow pick the runner. An alpine site with H = 500 m and Q = "
            "2 m^3/s: specific speed is low - Pelton territory. The nozzle "
            "converts the full 500 m of head into a jet at V = sqrt(2*g*H) = 99 "
            "m/s; buckets moving at ~0.45*V = 44.6 m/s turn the jet nearly 165 "
            "degrees, and the Euler work per kilogram is U*(C-theta_1 - "
            "C-theta_2) with C-theta_2 nearly -U - almost twice U*C-jet of "
            "energy per unit mass, at ~90% hydraulic efficiency. A valley site "
            "with H = 100 m, Q = 20 m^3/s sits mid-range: Francis, with wicket "
            "gates throttling the spiral case flow and the runner diffusing "
            "pressure as it turns the flow inward and down. A river site with H = "
            "10 m, Q = 100 m^3/s is Kaplan country: the axial runner's blades "
            "pitch flatter as flow rises, keeping incidence clean where a fixed "
            "blade would stall. In all three, the draft tube - a diverging "
            "diffuser below the runner - converts leftover exit kinetic energy "
            "into suction head, effectively adding meters of head for free and "
            "permitting the runner to sit above the tailrace."
        ),
        "key_points": [
            "Pelton (impulse): high head, low flow; jet strikes buckets at atmospheric pressure - the impulse extreme.",
            "Francis (reaction, mixed-flow): medium head and flow; the world's most common large hydro runner.",
            "Kaplan (reaction, axial, adjustable blades): low head, huge flow; holds efficiency across varying river discharge.",
            "Specific speed selects the type: low Ns -> Pelton, mid -> Francis, high -> Kaplan.",
            "The draft tube recovers exit kinetic energy as useful head in every reaction machine.",
        ],
        "requirements": [
            "The flow-geometries record (impulse vs reaction).",
            "The specific-speed record.",
            "Head in meters of water as an energy-per-weight measure.",
        ],
        "standards": [
            "Turbine specific speed Ns = N*sqrt(P)/H^(5/4) - power-based, distinct from the pump form.",
            "Buckets, wicket gates, spiral case, draft tube per standard hydro terminology.",
        ],
        "citations": [C_DIXON, C_LOGAN, C_JAPIKSE],
        "sig_lens": (
            "Signature take: three wheels for three rivers - the jet-hurler, the "
            "spiral-tamer, the pitch-shifter. His Signature framing treats the "
            "hydro family as water's three moods answered: the mountain's fury "
            "gets Pelton cups, the valley's muscle gets Francis, the plain's "
            "flood gets Kaplan's adjustable grin."
        ),
    },
    {
        "key": "axial_compressors",
        "name": "Axial Compressors: Building Pressure Stage by Stage",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The axial compressor is the jet engine's lung: row after row of "
            "rotor-stator stages, each adding a small pressure rise (~1.15-1.35 "
            "per stage), stacking to overall ratios of 30:1 or more in modern "
            "cores. Each stage is a rotor that adds swirl (doing work on the air) "
            "followed by a stator that removes the swirl and diffuses the flow, "
            "converting kinetic energy into pressure. The fundamental difficulty "
            "is that compressors diffuse: the relative flow SLOWS through the "
            "rotor, and boundary layers hate slowing down - push the diffusion "
            "too hard and the flow separates, the stage stalls, and the "
            "compressor can surge. Two design rules guard the diffusion: the de "
            "Haller number (W2/W1 >= ~0.72, the relative velocity may not fall "
            "too far) and the diffusion factor (DF <= ~0.6, a loading limit "
            "combining deceleration and turning). Stages are stacked on one "
            "shaft with interstage bleed, variable stators on the front stages, "
            "and tight tip clearances - a 15-stage machine is fifteen small "
            "aerodynamic miracles in series."
        ),
        "how_it_works": (
            "Design one stage: blade speed U = 350 m/s, axial velocity Cx = 180 "
            "m/s, 50% reaction. Choose flow turning to hold DF = 0.31. The rotor "
            "inlet relative angle and outlet relative angle come from the "
            "triangles; the de Haller check W2/W1 = 0.83 clears 0.72, and DF = "
            "0.31 clears 0.6 - the stage is safely loaded. Euler gives the work: "
            "with C-theta_1 = 160 m/s and C-theta_2 = 230 m/s (compressor sign "
            "convention, swirl added), w = U*(C-theta_2 - C-theta_1) = 350*70 = "
            "24.5 kJ/kg. At T01 = 300 K that is a stage temperature rise of "
            "24.4 K and a stage pressure ratio of 1.28. Fourteen such stages give "
            "1.28^14 ~ 32:1 overall - the arithmetic of the modern core. Off-design, the front stages see high incidence as flow "
            "drops (they drift toward stall) while the rear stages choke - "
            "variable stator vanes on the first stages reschedule the incidence, "
            "and bleed valves dump interstage air at startup. The compressor map "
            "with its surge line is the operating manual for this balancing act."
        ),
        "key_points": [
            "Rotor adds swirl (work in), stator removes swirl and diffuses (pressure up); ~1.15-1.35 pressure ratio per stage.",
            "Diffusion is the enemy: de Haller W2/W1 >= 0.72 and diffusion factor DF <= 0.6 guard against separation.",
            "Multistage stacking multiplies pressure ratios: 14 stages at 1.28 -> ~32:1 overall.",
            "Off-design mismatch: front stages stall, rear stages choke - variable stators and bleed manage it.",
            "The surge line on the compressor map marks the stability boundary of the whole stack.",
        ],
        "requirements": [
            "The velocity-triangles record and the Euler equation record.",
            "The losses record (why diffusion is hostile).",
        ],
        "standards": [
            "De Haller and Lieblein diffusion-factor limits per Cumpsty.",
            "Stage pressure ratio quoted as stagnation (total) pressure ratio.",
        ],
        "citations": [C_CUMPSTY, C_DIXON, C_SARAV],
        "sig_lens": (
            "Signature take: the axial compressor is the Signature staircase - "
            "each step small, the climb enormous. His Signature framing treats "
            "every stage as a negotiation with separation: ask the air to slow "
            "down, but never so rudely that it refuses."
        ),
    },
    {
        "key": "centrifugal_compressors",
        "name": "Centrifugal Compressors: The Impeller, the Slip, and the Diffuser",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The centrifugal compressor does in one impeller what takes many axial "
            "stages: air enters axially at the eye, is flung outward by the "
            "rotating impeller, and leaves at the tip with huge swirl - then a "
            "diffuser (vaneless or vaned) converts that kinetic energy into "
            "pressure. Single-stage pressure ratios of 4:1 to 8:1 are routine, "
            "which is why turbochargers, small gas turbines, process compressors, "
            "and refrigeration machines are centrifugal. Two effects dominate the "
            "design. Slip: the flow never quite follows the blade to full "
            "tangential velocity at the tip - it lags by the slip factor sigma "
            "(Stodola: sigma = 1 - pi*sin(beta_2b)/Z for backswept blades), so "
            "the Euler work uses sigma*U_2, not U_2. Stress: tip speed is capped "
            "around 500-600 m/s by centrifugal stress in the impeller material, "
            "which caps the pressure ratio per stage. The diffuser then faces the "
            "hardest diffusion in turbomachinery - recovering pressure from Mach "
            "~1 swirling flow without stalling - and its design often decides the "
            "machine's range."
        ),
        "how_it_works": (
            "Size a turbocharger compressor: impeller tip diameter 0.1 m spinning "
            "at 150,000 rpm gives U_2 = pi*D*N/60 = 785 m/s - too fast for "
            "aluminum, so either slow down or accept the stress limit; take U_2 = "
            "500 m/s (95,500 rpm). With 17 backswept blades at beta_2b = 90 - 30 "
            "= 60 degrees from tangential (30 degrees backsweep), Stodola slip "
            "sigma = 1 - pi*sin(60)/17 = 1 - 0.160 = 0.84. The Euler work is "
            "sigma*U_2^2 = 0.84*250000 = 210 kJ/kg (zero inlet swirl assumed). At "
            "T01 = 300 K the ideal exit stagnation temperature is 300 + 210/1.005 "
            "= 509 K, giving an ideal pressure ratio (509/300)^3.5 = 6.4:1; with "
            "82% impeller-diffuser efficiency the real ratio lands near 4.9:1. The "
            "vaneless diffuser then trades the tip Mach ~1.1 swirl for pressure "
            "in a widening annulus - simple and wide-ranging but lossy - or vaned "
            "diffusers recover more pressure over a narrower stable range. Back-"
            "sweep (blades leaning away from rotation) trades a little work for a "
            "much wider, more stable map - the standard choice."
        ),
        "key_points": [
            "One impeller + diffuser replaces many axial stages: 4:1 to 8:1 per stage; turbochargers, APUs, process machines.",
            "Slip factor sigma (Stodola) corrects the Euler work: the flow lags the blade, work = sigma*U_2*C-theta_2.",
            "Tip speed capped ~500-600 m/s by centrifugal stress - the material limit sets the pressure-ratio limit.",
            "The diffuser does the hardest pressure recovery in the field; vaneless = wide range, vaned = higher peak recovery.",
            "Backswept blades trade peak work for stability and range - the standard industrial choice.",
        ],
        "requirements": [
            "The Euler equation record (general radial form).",
            "The axial-compressor record (contrast per-stage pressure ratio).",
        ],
        "standards": [
            "Slip per Stodola; backsweep angle measured from the radial/tangential convention stated in the record.",
            "Tip speed limits quoted for common impeller materials (aluminum vs titanium).",
        ],
        "citations": [C_JAPIKSE, C_DIXON, C_CUMPSTY],
        "sig_lens": (
            "Signature take: the centrifugal impeller is the Signature sling - "
            "one wheel, one mighty throw. His Signature framing treats slip as "
            "the honest tax on hurrying: the air cannot quite keep up with the "
            "blade, and the design pays Stodola's toll willingly for the range "
            "backsweep buys."
        ),
    },
    {
        "key": "rotodynamic_pumps",
        "name": "Centrifugal and Axial Pumps: The Rotodynamic Workhorses",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Rotodynamic pumps - centrifugal, mixed-flow, and axial-flow - move "
            "the world's liquids by the same blade physics as compressors, with "
            "water's incompressibility simplifying the math: density is constant, "
            "so volume flow and mass flow differ only by rho. The centrifugal pump "
            "is the archetype: liquid enters the impeller eye axially, is flung "
            "outward, and the volute casing (a spiral collector) gathers the flow "
            "and diffuses it into pressure - head, measured in meters of liquid. "
            "Its head-capacity curve falls with flow (H = H0 - k*Q^2 roughly): "
            "shut the discharge valve and it sits at shutoff head churning safely; "
            "open the valve and flow rises as head falls, until the operating "
            "point where the pump curve crosses the system curve. Axial-flow "
            "pumps (propellers in a tube) serve high-flow, low-head duties - "
            "flood control, irrigation, cooling-water circulation - where a "
            "centrifugal would be absurdly large. Mixed-flow splits the middle. "
            "Every pump has a best-efficiency point (BEP); running far from it "
            "invites recirculation, vibration, and cavitation."
        ),
        "how_it_works": (
            "A centrifugal pump's impeller at 2900 rpm with outlet diameter 0.25 m "
            "has tip speed U_2 = pi*0.25*2900/60 = 38 m/s. The Euler head is "
            "U_2*C-theta_2/g; with radial-ish exit blading the theoretical shutoff "
            "head approaches U_2^2/g = 38^2/9.81 = 147 m - the ceiling no real "
            "pump reaches because slip and losses take their cut; a real machine "
            "might shut off at 120 m and run at BEP near Q = 80 L/s, H = 100 m, "
            "eta = 84%. The system it feeds has its own curve: static lift plus "
            "friction, H_sys = H_static + k*Q^2. The pump settles where the two "
            "curves cross - throttle the discharge valve and k rises, the system "
            "curve steepens, and the operating point slides up-left to lower flow "
            "and higher head. Power is rho*g*Q*H/eta: 1000*9.81*0.08*100/0.84 = "
            "93.4 kW of shaft power. Run at half flow and efficiency sags, "
            "recirculation sets in at the impeller eye, and the bearings feel it - "
            "which is why pump people preach: respect the BEP, and use a VFD "
            "rather than a throttle valve when the duty varies."
        ),
        "key_points": [
            "Rotodynamic pumps = centrifugal, mixed-flow, axial-flow; water's incompressibility makes density constant.",
            "Centrifugal: impeller flings flow outward, volute collects and diffuses; H-Q curve falls with flow (H = H0 - kQ^2).",
            "Operating point = pump curve x system curve intersection; throttling steepens the system curve.",
            "Axial-flow pumps serve high-flow/low-head duties (flood, irrigation, cooling water).",
            "Best-efficiency point is the happy place; far off-BEP operation brings recirculation, vibration, cavitation.",
        ],
        "requirements": [
            "The centrifugal-compressor record (impeller physics carries over).",
            "The affinity-laws record (speed changes).",
            "Head in meters of liquid as energy per unit weight.",
        ],
        "standards": [
            "Head-capacity curve per Hydraulic Institute nomenclature; BEP defined at maximum efficiency.",
            "Shutoff head, runout, and minimum-flow limits stated per API 610 practice.",
        ],
        "citations": [C_STEPANOFF, C_KARASSIK, C_HI],
        "sig_lens": (
            "Signature take: the centrifugal pump is the Signature lifter - the "
            "world's water climbs on its impellers. His Signature framing treats "
            "the H-Q curve as the pump's personality profile: meet it at its BEP "
            "and it serves for decades; drag it off-curve and it complains in "
            "vibration."
        ),
    },
    {
        "key": "positive_displacement_pumps",
        "name": "Positive Displacement Pumps: When Flow Must Be Forced, Not Flung",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Positive-displacement (PD) pumps do not fling fluid - they trap it. "
            "A piston, diaphragm, gear pair, lobe set, or screw captures a fixed "
            "volume each revolution and shoves it into the discharge line, so "
            "flow is nearly proportional to speed and nearly independent of "
            "pressure: Q = V_rev * N * eta_volumetric. That makes PD pumps the "
            "choice for metering (chemical dosing must deliver exactly X mL/min "
            "regardless of back-pressure), high-viscosity fluids (syrups, sludges, "
            "crude that a centrifugal cannot grab), and very high pressures "
            "(hydraulics, waterjet cutting at hundreds of MPa). The price: flow "
            "pulsates with each trapped volume (pulsation dampeners smooth it), "
            "they cannot tolerate closed discharge valves (pressure rises until "
            "something breaks - relief valves are mandatory, not optional), and "
            "solids or dry-running destroy tight clearances fast. Reciprocating "
            "(piston/plunger/diaphragm) versus rotary (gear, lobe, vane, screw, "
            "progressive cavity) is the family split: reciprocating for the "
            "highest pressures, rotary for smooth continuous flow."
        ),
        "how_it_works": (
            "A triplex plunger pump displaces V_rev = 150 mL per revolution "
            "across its three plungers; at N = 300 rpm the theoretical flow is "
            "0.15 L * 300 = 45 L/min. Internal slip past the plunger seals loses "
            "~5%, so volumetric efficiency is 0.95 and actual flow is 42.75 L/min "
            "- and that flow barely changes whether the discharge is at 5 MPa or "
            "35 MPa, because each revolution still traps the same volume. Power "
            "is Q*delta_p/eta: at 35 MPa, 0.0007125 m^3/s * 35e6 Pa / 0.9 = 27.7 "
            "kW. Contrast a centrifugal at the same duty: its flow would collapse "
            "as back-pressure rose. The dark side: close the discharge valve and "
            "the PD pump keeps trapping volumes - pressure spikes toward infinity "
            "in theory, toward burst pipes in practice - so a relief valve set "
            "just above working pressure is piped back to suction on every PD "
            "installation. Pulsation: each plunger stroke is a flow pulse at 3*N "
            "frequency (triplex), so a gas-charged dampener on the discharge "
            "absorbs the peaks and the piping sees near-steady flow."
        ),
        "key_points": [
            "PD pumps trap fixed volumes per revolution: Q = V_rev * N * eta_v - flow set by speed, nearly independent of pressure.",
            "Duties: metering/dosing, high-viscosity fluids, very high pressures (hydraulics, waterjet).",
            "Closed discharge = burst hazard: relief valves are mandatory on every PD installation.",
            "Flow pulsates per trapped volume; dampeners smooth it; reciprocating = highest pressure, rotary = smoothest flow.",
            "Tight clearances hate solids and dry-running - the maintenance contract of PD machines.",
        ],
        "requirements": [
            "The rotodynamic-pumps record (the contrast case).",
            "Volumetric efficiency as actual/theoretical flow.",
        ],
        "standards": [
            "Relief-valve requirement per Hydraulic Institute PD pump standards.",
            "Reciprocating vs rotary classification per standard industry taxonomy.",
        ],
        "citations": [C_KARASSIK, C_HI, C_STEPANOFF],
        "sig_lens": (
            "Signature take: the PD pump is the Signature enforcer - it does not "
            "persuade fluid, it evicts it by the fixed bucketful. His Signature "
            "framing treats trapped volume as a promise kept per revolution: "
            "metering-grade honesty, with a relief valve as the mandatory witness."
        ),
    },
    {
        "key": "fans_blowers",
        "name": "Fans and Blowers: Moving Air at Low Pressure Rise",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Fans and blowers are the low-pressure end of the compression family: "
            "they move large volumes of gas against small pressure rises - a few "
            "hundred pascals for ventilation, a few kilopascals for combustion air "
            "and cooling towers, up to tens of kilopascals for blowers feeding "
            "pneumatic conveying. At these pressure ratios (barely above 1.0) even "
            "air is effectively incompressible, so fan engineering uses the pump "
            "playbook: volume flow, pressure rise, and the fan laws (the affinity "
            "laws renamed). Types: centrifugal fans (squirrel-cage forward-curved "
            "for HVAC, backward-curved for efficiency, radial-tip for dirty air), "
            "axial fans (tube-axial, vane-axial for cooling towers and tunnels), "
            "and mixed-flow. Ratings distinguish total pressure (fan total "
            "pressure = outlet minus inlet stagnation) from static pressure "
            "(total minus outlet dynamic) - a fan exhausting freely to atmosphere "
            "converts its exit dynamic pressure into nothing useful, so static "
            "efficiency is the honest metric. Selection is by the same specific "
            "speed logic as pumps, and noise - blade-pass frequency and broadband "
            "- is a first-class design constraint, not an afterthought."
        ),
        "how_it_works": (
            "A backward-curved centrifugal fan, 0.8 m impeller at 1450 rpm, is "
            "rated Q = 5 m^3/s at 1200 Pa total pressure rise, 78% total "
            "efficiency. Air power is Q*delta_p = 6.0 kW; shaft power 7.7 kW. "
            "Need 20% more airflow for a hot day? The fan laws (affinity) say "
            "speed to 1740 rpm: Q = 6.0 m^3/s, pressure = 1200*1.44 = 1728 Pa, "
            "power = 7.7*1.728 = 13.3 kW - the cubic again, which is why VFDs on "
            "HVAC fans pay for themselves in months. Static vs total: if the fan "
            "discharges through a short duct to atmosphere at 15 m/s exit "
            "velocity, the exit dynamic pressure is rho*V^2/2 = 1.2*225/2 = 135 "
            "Pa - that is 11% of the total rise, wasted as a jet; static pressure "
            "rise is 1065 Pa and static efficiency 69%. Fan curves show the "
            "stall region on the left (like compressors, fans stall at low flow) "
            "- operate right of the stall line, ideally near peak efficiency, and "
            "remember the system curve: filters loading with dust steepen it and "
            "walk the operating point leftward toward trouble."
        ),
        "key_points": [
            "Fans/blowers: large gas volumes at small pressure rises; air treated as incompressible - the pump playbook applies.",
            "Types: centrifugal (forward/backward-curved, radial-tip), axial (tube/vane), mixed-flow - picked by specific speed.",
            "Total vs static pressure: static efficiency is the honest metric when exit kinetic energy is wasted.",
            "Fan laws = affinity laws: Q~N, p~N^2, P~N^3 - VFDs on fans pay back fast.",
            "Stall region on the left of the curve; dirty filters steepen the system curve and walk the point toward it.",
        ],
        "requirements": [
            "The affinity-laws record and the rotodynamic-pumps record.",
            "Total vs static pressure distinction.",
        ],
        "standards": [
            "Fan rating per AMCA 210 test code; total/static pressure per AMCA definitions.",
            "Noise treated as a design constraint: blade-pass frequency = blade count x rpm/60.",
        ],
        "citations": [C_BLEIER, C_STEPANOFF, C_DIXON],
        "sig_lens": (
            "Signature take: the fan is the Signature breath of buildings - "
            "quiet, constant, invisible until it stops. His Signature framing "
            "treats fan selection as respect for the cubic: a small slowdown is "
            "a large saving, and the static pressure tells the truth the total "
            "hides."
        ),
    },
    {
        "key": "performance_maps",
        "name": "Performance Maps: Reading the Compressor and Pump Chart",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The performance map is the operating manual of a turbomachine drawn "
            "as a chart. For a compressor: corrected mass flow on the x-axis "
            "(m_dot*sqrt(T01)/p01 - the flow the machine 'feels' regardless of "
            "inlet weather), pressure ratio on the y-axis, with one speed line "
            "per corrected speed (N/sqrt(T01)). Each speed line runs from choke "
            "(right: maximum flow, the machine cannot swallow more) to surge "
            "(left: minimum stable flow, beyond which violent flow reversal "
            "erupts). The surge line joins the surge points; the operating line "
            "sits right of it with surge margin - typically (PR_surge - PR_op)/"
            "PR_op >= 10-15% at constant flow. Efficiency islands (contours) show "
            "where the machine is happy. For pumps the map is the H-Q curve "
            "family at several speeds with efficiency contours and the NPSH-"
            "required curve rising at high flow. Reading a map answers the three "
            "operational questions: where do we run, how far from trouble, and "
            "how efficiently."
        ),
        "how_it_works": (
            "A jet engine compressor map at 100% corrected speed: the speed line "
            "stretches from choke at corrected flow 105 kg/s, PR = 22, to surge at "
            "62 kg/s, PR = 27.5. The engine's operating line at cruise crosses "
            "this speed line at 80 kg/s, PR = 25. Surge margin = (27.5 - 25)/25 = "
            "10% - acceptable but not generous; a hot-day takeoff with inlet "
            "distortion could eat that margin, which is why the controller "
            "schedules bleed and variable stators to push the operating line "
            "right. On a cold day the corrected speed N/sqrt(T) rises for the "
            "same mechanical rpm (denser air), shifting the whole map - the "
            "machine 'feels' faster than its tachometer says, and the operating "
            "point walks toward the surge line. That is the deep reason maps use "
            "corrected parameters: the aerodynamics answer to Mach numbers, not "
            "to rpm. Pump people read the same story in H-Q form: the duty point "
            "where pump meets system curve, efficiency contours around the BEP, "
            "and the NPSHr curve climbing at high flow warning of cavitation."
        ),
        "key_points": [
            "Compressor map: corrected flow vs pressure ratio, speed lines from choke (right) to surge (left).",
            "Corrected parameters (m_dot sqrt(T)/p, N/sqrt(T)) collapse weather and altitude onto one map.",
            "Surge margin >= 10-15% between operating line and surge line at constant flow - the stability budget.",
            "Efficiency islands show the happy zone; the map answers: where we run, how far from trouble, how efficiently.",
            "Pump maps: H-Q curve families with efficiency contours and NPSHr rising at high flow.",
        ],
        "requirements": [
            "The axial-compressor record (surge concept) and the affinity-laws record.",
            "Corrected flow/speed as Mach-similarity parameters (idea level).",
        ],
        "standards": [
            "Corrected flow = m_dot*sqrt(T01)/p01, corrected speed = N/sqrt(T01), per standard gas-turbine practice.",
            "Surge margin definition per Saravanamuttoo; choke = sonic limitation at the throat.",
        ],
        "citations": [C_SARAV, C_CUMPSTY, C_KARASSIK],
        "sig_lens": (
            "Signature take: the map is the Signature territory chart - choke "
            "cliffs on the right, surge dragons on the left. His Signature "
            "framing treats corrected parameters as the machine's true senses: "
            "it does not feel rpm, it feels Mach - and the map is drawn in what "
            "it feels."
        ),
    },
    {
        "key": "blade_cascades",
        "name": "Blade Cascades and Airfoils: The Two-Dimensional Heart of the Blade",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A cascade is a row of blades unwrapped: imagine cutting a cylindrical "
            "slice through an axial blade row and laying it flat - you get an "
            "infinite straight row of identical airfoils with spacing s and chord "
            "l, flow entering at angle alpha_1 and leaving at alpha_2. Cascade "
            "testing (and cascade CFD) isolates the two-dimensional blade-to-"
            "blade aerodynamics from the three-dimensional machine: it measures "
            "exactly what one blade row does to the flow - turning, loss, and "
            "the outlet angle. The key results: the flow never leaves exactly at "
            "the blade metal angle - it deviates by delta (Carter's rule: delta = "
            "m*theta*sqrt(s/l), m ~ 0.2-0.3 depending on stagger); loss buckets "
            "plot profile loss against incidence, showing the narrow happy range "
            "of inlet angles; and the diffusion factor / de Haller limits measured "
            "in cascades became the design rules of the axial compressor. Every "
            "blade section of a real 3-D blade is designed as a cascade section "
            "first, then stacked with twist, lean, and sweep to make the 3-D "
            "blade."
        ),
        "how_it_works": (
            "Test a compressor cascade: 8 blades, chord 100 mm, spacing 80 mm "
            "(solidity sigma = l/s = 1.25), stagger 35 degrees, camber theta = 30 "
            "degrees. Blow air at inlet angle alpha_1 = 50 degrees. Carter's rule "
            "predicts deviation delta = m*theta*sqrt(s/l) with m = 0.26: delta = "
            "0.26*30*sqrt(0.8) = 6.98 degrees - so the flow leaves at alpha_2 = "
            "metal angle + 7 degrees, not at the metal angle; the designer must "
            "aim the metal 7 degrees 'into' the desired flow. Vary incidence "
            "(alpha_1 minus the design inlet angle) from -8 to +8 degrees and the "
            "measured total-pressure loss traces a bucket: minimum near zero "
            "incidence, rising steeply past +5 (suction-side separation) and past "
            "-6 (pressure-side separation). That bucket IS the stage's tolerance "
            "to off-design operation - a wide bucket means a forgiving compressor. "
            "Controlled-diffusion airfoils reshape the suction-surface velocity "
            "distribution to delay separation, widening the bucket and raising "
            "the allowable diffusion - the quiet revolution that lifted stage "
            "pressure ratios in the 1980s."
        ),
        "key_points": [
            "Cascade = one blade row unwrapped flat: isolates 2-D blade-to-blade aerodynamics (turning, loss, outlet angle).",
            "Deviation (Carter's rule): flow leaves off the metal angle - aim the blade to compensate.",
            "Loss buckets vs incidence define the blade's off-design tolerance; wide bucket = forgiving stage.",
            "De Haller and diffusion-factor limits were born in cascade tunnels.",
            "Real 3-D blades are stacked cascade sections: design in 2-D, then add twist, lean, sweep.",
        ],
        "requirements": [
            "The velocity-triangles record (inlet/outlet angles).",
            "The axial-compressor record (diffusion limits).",
        ],
        "standards": [
            "Cascade nomenclature per Cumpsty: solidity sigma = chord/spacing, stagger, camber theta.",
            "Carter's deviation rule with the stagger-dependent m factor.",
        ],
        "citations": [C_CUMPSTY, C_DIXON, C_WILSON],
        "sig_lens": (
            "Signature take: the cascade is the Signature laboratory - one blade "
            "row, infinite patience, no excuses. His Signature framing treats "
            "deviation as the flow's small rebellion: it never leaves quite "
            "where you aimed it, and the master designer aims with the rebellion "
            "priced in."
        ),
    },
    {
        "key": "cavitation",
        "name": "Cavitation: When Liquid Boils Inside the Pump",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Cavitation is what happens when a pump's inlet pressure falls below "
            "the liquid's vapor pressure: the liquid boils - not from heat but "
            "from low pressure - forming vapor bubbles at the impeller eye. The "
            "bubbles ride into higher-pressure regions downstream and collapse "
            "violently, and that collapse is the damage: microjets and shock "
            "waves pit the impeller metal (it looks sandblasted, then eaten), "
            "noise rises to a gravel-in-the-pump roar, vibration climbs, head "
            "falls off a cliff as vapor chokes the passages, and efficiency dies. "
            "It is governed by the cavitation number sigma = (p_inlet - p_vapor)/"
            "(rho*V^2/2): when the local pressure anywhere dips under vapor "
            "pressure, bubbles are born. Inception starts at the blade suction "
            "side near the leading edge, where local velocities peak and pressures "
            "trough. Cavitation is purely a suction-side phenomenon - the "
            "discharge side, at high pressure, cannot cavitate - which is why "
            "every cure aims at the inlet: raise suction pressure, lower the "
            "pump, cool the liquid, slow the pump, or pick a better inlet design."
        ),
        "how_it_works": (
            "A cooling-water pump draws 80 C water (vapor pressure 47.4 kPa "
            "absolute) with the suction vessel at atmospheric pressure. The "
            "impeller eye accelerates the flow to 12 m/s at the blade leading "
            "edge; the local dynamic depression is roughly rho*V^2/2 = 1000*144/2 "
            "= 72 kPa below the inlet static pressure. If inlet static is 101 "
            "kPa absolute, the blade suction-side pressure dips to ~29 kPa - well "
            "below the 47.4 kPa vapor pressure - so bubbles form. They collapse "
            "a few centimeters downstream where pressure recovers, each collapse "
            "a tiny water-hammer focusing megapascal-scale pulses onto "
            "micrometer spots of metal. Run this for weeks and the impeller eye "
            "looks chewed. The Thoma cavitation parameter sigma_Th = NPSH/H "
            "collapses the condition onto the map: every pump has a critical "
            "sigma below which head falls 3% (the standard inception criterion). "
            "The fix is NPSH margin - more suction head than the pump demands - "
            "covered next on the ladder."
        ),
        "key_points": [
            "Cavitation = low-pressure boiling at the pump inlet: vapor bubbles form, then collapse violently downstream.",
            "Damage signature: pitted impellers, gravel-like noise, vibration, head collapse, efficiency loss.",
            "Inception when local pressure < vapor pressure: cavitation number sigma = (p - p_v)/(rho V^2/2).",
            "Purely a suction-side phenomenon - all cures aim at the inlet (raise suction head, slow down, cool the liquid).",
            "Thoma parameter sigma_Th = NPSH/H; 3% head drop is the standard inception criterion.",
        ],
        "requirements": [
            "The fluid-mechanics foundation record (vapor pressure idea, Bernoulli).",
            "The rotodynamic-pumps record (impeller eye, BEP).",
        ],
        "standards": [
            "Vapor pressure as a pure function of temperature for the pumped liquid.",
            "3% head-drop inception criterion per Hydraulic Institute practice.",
        ],
        "citations": [C_KARASSIK, C_STEPANOFF, C_HI],
        "sig_lens": (
            "Signature take: cavitation is the Signature betrayal - the liquid "
            "turns to vapor exactly where the pump trusted it most. His Signature "
            "framing treats the collapsing bubble as the smallest hammer in "
            "engineering: micrometers wide, megapascals strong, patient enough "
            "to eat steel."
        ),
    },
    {
        "key": "npsh",
        "name": "Net Positive Suction Head: The Guard Against Cavitation",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Net Positive Suction Head (NPSH) is the quantified guard against "
            "cavitation: the margin, in meters of liquid, between the inlet "
            "stagnation pressure and the vapor pressure. Two numbers face off. "
            "NPSH-available is what the SYSTEM offers: (p_suction - p_vapor)/"
            "(rho*g) plus inlet velocity head minus suction-line losses - set by "
            "tank level, suction pressure, liquid temperature, and piping. "
            "NPSH-required is what the PUMP demands: measured by the manufacturer, "
            "rising steeply with flow (roughly with Q^2), marking where head "
            "drops 3%. The iron rule: NPSHa >= NPSHr with margin - the Hydraulic "
            "Institute recommends margin ratios of 1.1 to 1.3+ depending on "
            "service, and critical services want more. Suction specific speed "
            "S = N*sqrt(Q)/NPSHr^(3/4) (US units) judges the inlet design itself: "
            "below ~8,500-11,000 the impeller eye is cavitation-tolerant; above "
            "it, the eye is aggressive and the pump will punish any NPSH "
            "shortfall. Every pump failure investigation starts here."
        ),
        "how_it_works": (
            "A process pump must deliver Q = 0.12 m^3/s. The suction tank sits 3 "
            "m above the pump centerline, the suction line loses 1.2 m of head to "
            "friction, the liquid is 60 C water (vapor pressure 19.9 kPa = 2.03 m "
            "of water), and inlet velocity head is 0.4 m. NPSHa = 3.0 - 1.2 - "
            "2.03 + 0.4 = 0.17... wait, that is the suction head above vapor: "
            "recompute properly - static head 3.0 m plus atmospheric 10.33 m "
            "minus vapor 2.03 m minus losses 1.2 m plus velocity head 0.4 m = "
            "10.5 m available. The pump's NPSHr at this flow is 6.5 m, so the "
            "margin ratio is 10.5/6.5 = 1.62 - comfortable. Now throttle the "
            "suction valve (never do this): losses jump to 5 m, NPSHa falls to "
            "6.9 m, margin ratio 1.06 - the pump growls at the edge. Hot summer "
            "raises the liquid to 90 C (vapor 7.2 m): NPSHa = 5.3 m < NPSHr - "
            "full cavitation, head collapse, impeller damage within weeks. The "
            "ladder lesson: NPSH is a system property first and a pump property "
            "second - the cure for a cavitating pump is usually in the piping, "
            "the tank level, or the temperature, not in the pump."
        ),
        "key_points": [
            "NPSHa (system offers) vs NPSHr (pump demands): the iron rule is NPSHa >= NPSHr with margin (1.1-1.3x+).",
            "NPSHa = static head + atmospheric - vapor head - suction losses + velocity head.",
            "NPSHr rises steeply with flow (~Q^2); margin evaporates at high flow and high temperature.",
            "Suction specific speed S judges inlet aggressiveness: < ~8,500-11,000 (US) is tolerant design.",
            "Cavitation cures live in the system - tank level, piping, temperature - more often than in the pump.",
        ],
        "requirements": [
            "The cavitation record.",
            "Head in meters of liquid; vapor pressure vs temperature.",
        ],
        "standards": [
            "NPSH margin guidance per Hydraulic Institute ANSI/HI 9.6.1.",
            "NPSHr defined at 3% head drop; suction specific speed in US customary units (rpm, gpm, ft).",
        ],
        "citations": [C_HI, C_KARASSIK, C_STEPANOFF],
        "sig_lens": (
            "Signature take: NPSH is the Signature bodyguard - a number that "
            "stands between the pump and the void. His Signature framing treats "
            "the margin ratio as the machine's courage measured in meters: "
            "above 1.3 it sleeps soundly, near 1.0 it dreams of gravel."
        ),
    },
    {
        "key": "surge_stall",
        "name": "Surge and Stall: The Instability Twins of Compression",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Surge and stall are the two faces of compressor instability, and "
            "confusing them is dangerous. Rotating stall is LOCAL: one or more "
            "patches of stalled flow rotate around the annulus at a fraction of "
            "rotor speed while the machine keeps pumping on average - efficiency "
            "drops, blades vibrate (stall flutter can break them), but the system "
            "survives. Surge is SYSTEMIC: the whole compressor can no longer "
            "hold back the downstream pressure, flow reverses violently through "
            "the entire machine, pressure collapses, flow re-establishes, and "
            "the cycle repeats at a few hertz - a deep, booming oscillation that "
            "can destroy bearings, seals, and blades in seconds. Which one you "
            "get is decided by the Greitzer B parameter: B = (U/2a)*sqrt(Vp/"
            "(Ac*Lc)) - the ratio of pressure-rise capability to system "
            "compliance. Large B (big downstream volume, e.g., a pipeline or "
            "large plenum) gives surge; small B gives rotating stall. Control "
            "systems draw the surge line on the map and hold the operating line "
            "clear of it with margin, bleed, and variable geometry."
        ),
        "how_it_works": (
            "An industrial compressor feeds a large process vessel: impeller tip "
            "speed U = 400 m/s, speed of sound a = 340 m/s, plenum volume Vp = 50 "
            "m^3, compressor duct area Ac = 0.5 m^2, duct length Lc = 10 m. "
            "Greitzer B = (400/680)*sqrt(50/(0.5*10)) = 0.588*sqrt(10) = 1.86 - "
            "well above the ~0.8 crossover, so this system surges, not stalls. "
            "Throttle the discharge: the operating point marches left up the "
            "speed line, the slope of the pressure-rise characteristic goes "
            "positive past its peak - the classic static-instability criterion - "
            "and at the surge line the compressor cannot sustain the plenum "
            "pressure. Flow reverses in milliseconds with a bang; the plenum "
            "blows down through the backward compressor; pressure falls until "
            "the compressor can pump forward again; the plenum refills; bang "
            "again - 2-5 Hz of the most violent event in normal machinery "
            "operation. The protection: a surge-control valve that opens on "
            "approach (recycling discharge to suction, moving the operating "
            "point right), plus the 10-15% surge margin baked into the operating "
            "line. Rotating stall, by contrast, would show as a rumbling "
            "asymmetry with mean flow continuing - degrading, not catastrophic."
        ),
        "key_points": [
            "Rotating stall: local stalled patches circling the annulus; mean flow continues; blades vibrate, efficiency drops.",
            "Surge: system-wide violent flow reversal oscillation (Hz range); destroys hardware in seconds.",
            "Greitzer B decides: large downstream volume -> surge; small -> rotating stall; crossover B ~ 0.8.",
            "Static criterion: positive slope of the pressure-rise characteristic past its peak invites instability.",
            "Protection: surge margin, fast-acting recycle/blowoff valves, variable geometry, and never operating left of the line.",
        ],
        "requirements": [
            "The performance-maps record (surge line, operating line).",
            "The axial-compressor record (stall mechanism).",
        ],
        "standards": [
            "Greitzer B parameter per Greitzer (1976); surge-margin definition per Saravanamuttoo.",
            "Distinction stall-vs-surge per Cumpsty's treatment.",
        ],
        "citations": [C_CUMPSTY, C_SARAV, C_DIXON],
        "sig_lens": (
            "Signature take: stall is the Signature stumble, surge the Signature "
            "earthquake - one limps, the other levels the block. His Signature "
            "framing treats the Greitzer B as the prophecy number: compute it "
            "before the first startup, because the machine will obey it whether "
            "you did or not."
        ),
    },
    {
        "key": "rotordynamics",
        "name": "Rotordynamics: Critical Speeds and the Spinning Shaft",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Rotordynamics is the study of the shaft itself as a vibrating "
            "system: every rotor has natural frequencies, and when running speed "
            "coincides with one, you get a critical speed - resonance with "
            "potentially enormous vibration. The Jeffcott rotor (a disc on a "
            "massless flexible shaft) captures the essence: natural frequency "
            "omega_n = sqrt(k/m), critical speed Nc = 60*omega_n/(2*pi) rpm. "
            "Below the critical (subcritical, rigid-rotor operation) the "
            "deflection grows with speed; AT the critical, unbalance drives "
            "large whirl - but with damping the machine can pass through; ABOVE "
            "it (supercritical, flexible-rotor operation) the rotor self-"
            "centers, spinning about its mass center rather than its geometric "
            "center - the physics that lets some machines run smoothly above "
            "their first critical. Real rotors have many modes (bending, "
            "torsional), bearings add stiffness AND damping (and cross-coupled "
            "stiffness that can drive oil-whip instability in fluid-film "
            "bearings), and the Campbell diagram plots natural frequencies vs "
            "running speed to find every crossing. API 610/617 demand separation "
            "margins: operating speed must clear criticals by typically 15-20%+."
        ),
        "how_it_works": (
            "A pump rotor: disc mass m = 40 kg on a shaft of stiffness k = 8e6 "
            "N/m. omega_n = sqrt(8e6/40) = 447 rad/s; Nc = 60*447/(2*pi) = 4270 "
            "rpm. Running at 2950 rpm, the separation is (4270-2950)/4270 = 31% "
            "- comfortably subcritical per API practice. Unbalance response: "
            "with residual unbalance U = 20 g-mm (a small setscrew's worth), the "
            "deflection at speed ratio r = omega/omega_n follows X = (U/m)*r^2/"
            "sqrt((1-r^2)^2 + (2*zeta*r)^2). At r = 0.69 (2950 rpm) with damping "
            "zeta = 0.1, the magnification is modest (~1.9x the static "
            "deflection); at r = 1 it would peak at 1/(2*zeta) = 5x - the "
            "critical's bite, tamed only by damping. Above the critical (r > "
            "1.3), the response falls and the rotor self-centers - which is why "
            "large steam turbines, running supercritical between their first and "
            "second criticals, need exquisite balance AND damping to traverse "
            "the critical on every startup. Cross-coupled bearing stiffness can "
            "add negative damping (oil whip at ~0.42-0.48x running speed) - the "
            "instability that tilts toward tilting-pad bearings in high-duty "
            "machines."
        ),
        "key_points": [
            "Critical speed = running speed coinciding with a rotor natural frequency; resonance with large unbalance response.",
            "Jeffcott model: omega_n = sqrt(k/m); subcritical (rigid) vs supercritical (flexible, self-centering) operation.",
            "Damping is what lets machines traverse criticals; separation margins ~15-20%+ per API.",
            "Campbell diagram finds every natural-frequency crossing across the speed range.",
            "Fluid-film bearings add cross-coupled stiffness -> oil whip/whirl instability; tilting-pad bearings cure it.",
        ],
        "requirements": [
            "The losses/windage-adjacent idea of bearings (next record deepens it).",
            "Resonance: natural frequency, damping ratio, magnification.",
        ],
        "standards": [
            "Critical-speed separation margins per API 610 (pumps) / API 617 (compressors).",
            "Campbell diagram and unbalance-response analysis per standard rotordynamics practice.",
        ],
        "citations": [C_DIXON, C_API610, C_WILSON],
        "sig_lens": (
            "Signature take: the shaft is the Signature spine - stiff enough to "
            "stand, supple enough to survive its own song. His Signature framing "
            "treats the critical speed as the rotor's one forbidden note: know "
            "where it sings, damp the passage, and never linger."
        ),
    },
    {
        "key": "bearings",
        "name": "Bearings: Rolling, Fluid-Film, and Magnetic",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Bearings decide how long a turbomachine lives: they carry the "
            "rotor's weight and thrust while adding the stiffness and damping "
            "the rotordynamics assumed. Three technologies share the work. "
            "Rolling-element bearings (ball, roller): compact, low friction at "
            "all speeds, life rated by L10 - the hours at which 10% fail, L10 = "
            "(C/P)^p million revolutions (p = 3 ball, 10/3 roller) - but "
            "speed-limited by centrifugal loading of the elements themselves and "
            "intolerant of contamination. Fluid-film (journal) bearings: the "
            "shaft rides on a self-generated oil wedge - infinite life in "
            "principle (no metal contact at speed), superb damping, but they "
            "need minimum speed to build the film and can go unstable (oil whip). "
            "Tilting-pad journal bearings - pads that pivot to follow the shaft "
            "- kill the cross-coupled stiffness behind oil whip and dominate "
            "large high-speed machines. Magnetic bearings: active electromagnets "
            "levitate the shaft with position feedback - no contact, no oil, no "
            "wear, but they need power, backup bearings for drop events, and "
            "control electronics. Thrust bearings (tilting-pad Kingsbury/Michell "
            "type) separately absorb the axial push - enormous in multistage "
            "pumps and compressors - with balance drums/pistons trimming the "
            "residual."
        ),
        "how_it_works": (
            "A process pump uses deep-groove ball bearings: dynamic capacity C = "
            "48 kN, equivalent load P = 9 kN. L10 = (48/9)^3 = 152 million "
            "revolutions = at 2950 rpm, 152e6/(2950*60) = 859 hours?? - that "
            "cannot be right for a pump; recompute: 152e6 rev / (2950 rev/min) = "
            "51,525 min = 859 h - indeed too short, which is why real pump "
            "bearings are sized with C/P ~ 5+: take C = 90 kN, P = 9 kN: L10 = "
            "1000 million rev = 5,650 h... still shortish; at P = 6 kN: (15)^3 = "
            "3375 Mrev = 19,000 h - now we are in honest pump territory (API 610 "
            "wants 25,000 h+). The cubic punishes overload brutally: double the "
            "load, life falls 8x. Now the big steam turbine next door: 60 MW on "
            "tilting-pad journals, each pad pivoting on its rocker - the oil "
            "film, ~50 microns thick at speed, carries 20 tonnes per bearing "
            "with zero metal contact, and the pads' freedom to tilt removes the "
            "cross-coupling that would whip a fixed-arc bearing at 3600 rpm. "
            "Thrust: the HP steam turbine's axial steam push (~tens of tonnes) "
            "lands on a Kingsbury thrust bearing - a collar between two rings of "
            "tilting pads - with a balance drum bleeding pressure to trim the "
            "net load to what the pads can take. Three bearing films, three "
            "philosophies: rolling for compactness, fluid-film for heavy "
            "damping, magnetic for the oil-free future."
        ),
        "key_points": [
            "Rolling-element: compact, L10 = (C/P)^p million revs (p=3 ball, 10/3 roller); the cubic punishes overload 8x per doubling.",
            "Fluid-film journal: shaft rides an oil wedge - infinite life at speed, superb damping; needs speed to build film.",
            "Tilting-pad journals kill oil-whip cross-coupling - the standard for large high-speed rotors.",
            "Magnetic bearings: contact-free, oil-free levitation with active control; need backup bearings and power.",
            "Thrust bearings (Kingsbury/Michell pads) plus balance drums handle the huge axial loads of multistage machines.",
        ],
        "requirements": [
            "The rotordynamics record (why bearings supply stiffness and damping).",
            "Load, life, and the idea of a fatigue rating.",
        ],
        "standards": [
            "L10 life per ISO 281; API 610 bearing-life expectations for pumps.",
            "Tilting-pad and oil-whip treatment per standard rotordynamics references.",
        ],
        "citations": [C_API610, C_DIXON, C_KARASSIK],
        "sig_lens": (
            "Signature take: bearings are the Signature cradle - everything "
            "spins, nothing touches. His Signature framing treats the oil wedge "
            "as the quietest miracle in the plant: fifty microns of oil holding "
            "twenty tonnes at sixty revolutions a second, forever."
        ),
    },
    {
        "key": "seals_leakage",
        "name": "Seals and Leakage Control: Labyrinths, Brushes, and Dry Gas Seals",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Wherever pressure differs across a rotating gap, fluid leaks - over "
            "blade tips, through interstage gaps, along the shaft to atmosphere - "
            "and seals are the art of throttling that leakage without touching. "
            "The labyrinth seal is the classic: a series of thin teeth with tight "
            "clearance, each tooth throttling the flow and each cavity "
            "dissipating its kinetic energy, so leakage falls roughly with the "
            "number of teeth (Martin's formula quantifies it). It never touches - "
            "so it never wears - but clearance opens with thermal transients and "
            "rubs. Brush seals: a dense pack of fine metallic bristles that DO "
            "touch lightly, cutting leakage to a fraction of a labyrinth's - the "
            "upgrade for turbine interstage and compressor discharge sealing. Dry "
            "gas seals: for process compressors handling hydrocarbons, a pair of "
            "faces with spiral micro-grooves pump a thin gas film between them - "
            "non-contacting, near-zero leakage, but intolerant of dirt and "
            "needing clean seal gas. And the abradable: the casing side coated "
            "soft so the blade tip can rub in its own minimum clearance - the "
            "tip-clearance record's best friend. Sealing is efficiency: every "
            "kilogram that bypasses the blades is Euler work thrown away."
        ),
        "how_it_works": (
            "A steam turbine interstage labyrinth: 8 teeth, clearance 0.4 mm, "
            "diameter 0.5 m, pressure ratio 0.7 across it. Martin's formula for "
            "the leakage mass flow: m_dot = (A * p1 / sqrt(R*T1)) * sqrt((1 - "
            "(p2/p1)^2) / sqrt(n - ln(p2/p1))), with flow area A = pi*D*clearance "
            "= pi*0.5*0.0004 = 6.28e-4 m^2. For steam at p1 = 2 MPa, T1 = 600 K "
            "(R = 461.5 J/kg-K): m_dot = (6.28e-4 * 2e6 / sqrt(461.5*600)) * "
            "sqrt(1-0.49)/sqrt(8 - ln 0.7) = (1256/526.3) * 0.714/2.89 = 2.387 * "
            "0.247 = 0.59 kg/s per seal. Against a 100 kg/s main flow that is "
            "0.6% - times a dozen such seals, real money, which is why brush "
            "seals (cutting this by 3-5x) pay back fast in retrofits. The teeth "
            "work by repeated throttling: each tooth drops pressure nearly "
            "isentropically, each chamber kills the jet's kinetic energy in "
            "turbulence - the seal is a tiny multi-stage turbine run in reverse "
            "as a pure dissipator. Rubs during thermal transients open the "
            "clearance permanently (labyrinths don't heal), so abradable coatings "
            "and spring-backed brush bristles exist to forgive the rub."
        ),
        "key_points": [
            "Labyrinth seals: non-contacting teeth + cavities throttle leakage in stages (Martin's formula); never wear, but rubs open clearance permanently.",
            "Brush seals: lightly-touching bristles cut labyrinth leakage 3-5x - the standard retrofit upgrade.",
            "Dry gas seals: grooved faces ride a pumped gas film - near-zero leakage for process compressors; demand clean seal gas.",
            "Abradable coatings let blade tips rub in their own minimum clearance - sealing meets tip-clearance control.",
            "Leakage is lost Euler work: sealing efficiency IS machine efficiency.",
        ],
        "requirements": [
            "The fluid-mechanics foundation record (throttling, kinetic-energy dissipation).",
            "The tip-clearance record's context (next on the ladder).",
        ],
        "standards": [
            "Martin's labyrinth formula with the Egli carryover perspective noted.",
            "Dry gas seal practice per API 692 (dry gas sealing systems).",
        ],
        "citations": [C_DIXON, C_WILSON, C_API610],
        "sig_lens": (
            "Signature take: the seal is the Signature tollbooth - every gap "
            "charges the flow, and the teeth collect honestly. His Signature "
            "framing treats labyrinths as turbines of pure waste: stage after "
            "stage dedicated to turning pressure into nothing, beautifully."
        ),
    },
    {
        "key": "cooling_materials",
        "name": "Blade Cooling and High-Temperature Materials: Surviving the Furnace",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The gas turbine's hottest blades live in gas hotter than their own "
            "melting point - possible only through the twin technologies of "
            "cooling and materials. Cooling: compressor-discharge air is ducted "
            "inside the hollow blade, snaking through serpentine passages with "
            "turbulators and pin fins, then ejected through film-cooling holes "
            "to blanket the surface - plus thermal barrier coatings (ceramic, "
            "~0.3 mm) that drop the metal temperature another ~100-150 K. "
            "Cooling effectiveness epsilon = (Tg - Tm)/(Tg - Tc) measures the "
            "achievement: epsilon = 0.5 means the cooling closed half the gap "
            "between gas and coolant temperatures. Materials: nickel superalloys, "
            "then directionally solidified, then single-crystal (no grain "
            "boundaries for creep to slide along), each step buying ~50-100 K of "
            "metal capability; oxide-dispersion and ceramic-matrix composites "
            "are the frontier. The price of cooling is real: 15-25% of compressor "
            "air bypasses the combustor to cool, diluting the cycle and costing "
            "efficiency - the designer spends cooling air like money, only where "
            "the temperature demands it."
        ),
        "how_it_works": (
            "A first-stage turbine blade faces Tg = 1700 K gas; the single-"
            "crystal alloy is allowed Tm = 1250 K metal; cooling air arrives at "
            "Tc = 800 K. Required effectiveness epsilon = (1700-1250)/(1700-800) "
            "= 450/900 = 0.5 - an aggressive but achievable design with "
            "serpentine internal cooling plus film rows plus TBC. Without any "
            "cooling (epsilon = 0), TIT would be capped at ~1250 K - and since "
            "specific work scales roughly with TIT, the uncooled engine makes "
            "~25% less power per kilogram of air. The cooling air itself costs: "
            "suppose 20% of compressor flow cools the turbine; that air did "
            "compressor work but skips the combustor's full heat addition, "
            "trimming cycle efficiency by ~2-3 points - the eternal trade. "
            "Thermal barrier coating: a yttria-stabilized zirconia ceramic layer "
            "~0.3 mm thick with terrible thermal conductivity; the 150 K drop "
            "across it is 'free' (no air spent), which is why every hot blade "
            "wears one. Creep - slow deformation under stress at temperature - "
            "is the life limiter: single-crystal blades align the crystal to "
            "eliminate transverse grain boundaries, doubling creep life per "
            "alloy generation."
        ),
        "key_points": [
            "Cooled blades survive gas hotter than their melting point: internal serpentine + film cooling + thermal barrier coatings.",
            "Cooling effectiveness epsilon = (Tg-Tm)/(Tg-Tc): 0.5 is aggressive modern practice.",
            "Materials ladder: nickel superalloy -> directional -> single-crystal -> CMC frontier; each step buys temperature.",
            "Cooling air costs 15-25% of compressor flow and ~2-3 efficiency points - spent like money, only where needed.",
            "TBC gives ~100-150 K 'free'; creep at temperature is the life limiter single-crystal defeats.",
        ],
        "requirements": [
            "The gas-turbine record (TIT as the performance lever).",
            "Heat transfer idea: conduction through a coating, convection to coolant.",
        ],
        "standards": [
            "Effectiveness definition per standard turbine-cooling literature.",
            "Creep-life framing per superalloy metallurgy practice.",
        ],
        "citations": [C_SARAV, C_WILSON, C_DIXON],
        "sig_lens": (
            "Signature take: the cooled blade is the Signature salamander - it "
            "lives in fire by sweating air. His Signature framing treats "
            "cooling effectiveness as the bravest number in engineering: how "
            "close to melting dare you run, and how much air will you spend for "
            "the privilege."
        ),
    },
    {
        "key": "tip_clearance",
        "name": "Tip Clearance and Secondary Flows: The Efficiency Thieves",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The gap between a blade tip and the casing - often under a "
            "millimeter - is where some of the worst losses in turbomachinery "
            "are born. Pressure is higher on the blade's pressure side than its "
            "suction side, so fluid jets through the tip gap instead of turning "
            "through the passage: no Euler work from that fluid, plus a tip-"
            "leakage vortex that scrambles the passage flow downstream. The rule "
            "of thumb: each 1% of tip clearance relative to blade height costs "
            "~1-2 points of stage efficiency in compressors, ~1 point in "
            "turbines. Shrouded blades (a band joining the tips) nearly eliminate "
            "it - standard in steam turbines, rare in aircraft compressors where "
            "weight and stress forbid. Secondary flows are the accomplices: where "
            "blades meet endwalls, the boundary layers roll into passage "
            "vortices that sweep low-energy fluid across the passage - the "
            "'secondary loss' line item. Designers fight back with endwall "
            "contouring, blade lean and sweep (shifting the loading away from "
            "the endwalls), and casing treatments (grooves over compressor rotor "
            "tips that extend the stall margin). Clearance control is a machine-"
            "system problem: the gap breathes with thermal transients, "
            "centrifugal growth, and maneuver loads."
        ),
        "how_it_works": (
            "An axial compressor stage: blade height h = 60 mm, running tip "
            "clearance tau = 0.6 mm - tau/h = 1%. Efficiency debit ~1.5 points: "
            "a stage that would be 91% with zero clearance delivers ~89.5%. "
            "Across a 14-stage core that is real fuel burn. During a hot restart "
            "the casing (thin, fast-heating) grows before the rotor (heavy, "
            "slow) - clearance opens to 1.2 mm and the debit doubles; at cold "
            "cruise the rotor's centrifugal growth (proportional to rpm^2) "
            "closes it back. Active clearance control manages the breathing: "
            "thermal (cooling/heating the casing with compressor air), or "
            "mechanical. The leakage jet itself: driven by the blade pressure "
            "difference delta_p across the tip, its velocity scales with "
            "sqrt(2*delta_p/rho) - tens of m/s - and it rolls into a vortex "
            "whose core is a total-pressure deficit convecting downstream, "
            "raising mixing loss in the next blade row. Casing treatment - "
            "axial grooves or honeycomb over the rotor tip - bleeds the vortex "
            "energy and can buy 5-10% more stall margin: the grooves are ugly, "
            "the stability is beautiful."
        ),
        "key_points": [
            "Tip leakage: pressure-side to suction-side jet through the tip gap - no work, plus a downstream-scrambling vortex.",
            "Rule of thumb: ~1-2 efficiency points per 1% clearance/height (compressors), ~1 point (turbines).",
            "Shrouds eliminate it where weight/stress allow; abradables let tips rub in minimum clearance.",
            "Secondary (passage) vortices at the endwalls are the accomplices - fought with lean, sweep, endwall contouring.",
            "Clearance breathes with thermals and rpm; active clearance control + casing treatment manage it.",
        ],
        "requirements": [
            "The losses record (tip-clearance and secondary line items).",
            "The seals record (abradables).",
        ],
        "standards": [
            "Clearance debit rules quoted as industry rules of thumb with the compressor/turbine distinction.",
            "Casing-treatment stall-margin benefit per Cumpsty's treatment.",
        ],
        "citations": [C_CUMPSTY, C_DIXON, C_WILSON],
        "sig_lens": (
            "Signature take: the tip gap is the Signature keyhole - a millimeter "
            "of nothing that steals percentages. His Signature framing treats "
            "clearance as the machine's breathing: inhale on the hot restart, "
            "exhale at cruise, and the design must tailor the clothes to fit "
            "every breath."
        ),
    },
    {
        "key": "multistage_matching",
        "name": "Multi-Stage Matching and Off-Design Operation",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A multistage machine is a team, and off-design is when the team "
            "quarrels. At the design point every stage sits at its happy "
            "incidence - but stages are stacked on one shaft at one speed, "
            "passing one mass flow, while density rises through a compressor "
            "(so rear stages need smaller annulus area) or falls through a "
            "turbine. Drop the speed or the flow and the stages mismatch: in a "
            "compressor at low corrected speed, the front stages see too little "
            "flow for their blade angles (high positive incidence - toward "
            "stall) while the rear stages, sized for denser air, see too much "
            "flow (toward choke). The machine's operating line is the locus of "
            "points where all stages agree - found by stage-stacking: each "
            "stage's characteristic composed in series, iterated until the "
            "pressures and flows match. Turbines are kinder: accelerating flow "
            "through the stages is stable, so multistage turbines tolerate off-"
            "design gracefully - which is why the matching problem is "
            "compressor folklore. Remedies: variable stators reschedule front-"
            "stage incidence, interstage bleed dumps excess front-stage flow at "
            "startup, and multi-spool shafts let the spools find their own "
            "speeds."
        ),
        "how_it_works": (
            "Stack three identical compressor stages, each with characteristic "
            "PR_i(m_dot_corrected). At design, each passes 10 kg/s corrected at "
            "PR 1.3 - overall 2.197. Now run at 80% corrected speed: the front "
            "stage, seeing the full inlet flow, operates at higher "
            "flow-coefficient than its design (toward choke is wrong - think "
            "again: at fixed geometry, lower speed means the blades meet the "
            "flow at higher incidence because U fell while Cx tried to hold). "
            "Stage-stacking iterates: guess the interstage pressures, look up "
            "each stage's flow at its pressure ratio and the common corrected "
            "speed, enforce continuity - the stages negotiate to a common "
            "corrected flow where all three characteristics intersect the "
            "continuity constraint. The result: front stage near stall "
            "(incidence +6 deg), rear stage toward choke, overall PR collapsed. "
            "Open the interstage bleed between stage 1 and 2: the front "
            "stage's effective flow rises (bleed dumps overboard), its incidence "
            "falls back to +1 deg, and the machine starts cleanly. Close the "
            "bleed as speed rises and the stages reconverge on the design match. "
            "Multi-spool engines dodge the whole quarrel: HP and LP spools each "
            "find the speed where their stages agree."
        ),
        "key_points": [
            "Stages on one shaft share speed and mass flow but want different flows off-design: front stages stall, rear stages choke (compressors).",
            "Stage-stacking composes single-stage characteristics in series with continuity to find the operating line.",
            "Turbines tolerate off-design (accelerating flow is stable); compressors are the matching problem.",
            "Remedies: variable stators, interstage bleed, multi-spool shafts.",
            "The operating line on the map is the stages' negotiated agreement, not a single stage's wish.",
        ],
        "requirements": [
            "The axial-compressor record and the performance-maps record.",
            "Incidence and stall from the cascade record.",
        ],
        "standards": [
            "Stage-stacking method per standard compressor performance literature.",
            "Off-design incidence sign conventions consistent with the cascade record.",
        ],
        "citations": [C_CUMPSTY, C_SARAV, C_DIXON],
        "sig_lens": (
            "Signature take: the stage stack is the Signature crew - fourteen "
            "rowers, one oar-speed, and the river keeps changing. His Signature "
            "framing treats matching as diplomacy: bleed valves and variable "
            "vanes are the negotiators that keep every stage rowing without "
            "catching a crab."
        ),
    },
    {
        "key": "variable_geometry",
        "name": "Variable Geometry: Inlet Guide Vanes and Variable Stators",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Variable geometry lets the blading change its mind with operating "
            "condition. Inlet guide vanes (IGVs): the stationary row ahead of the "
            "first rotor, whose stagger angle rotates - closing the IGVs "
            "pre-swirls the flow and throttles the mass flow at nearly constant "
            "pressure ratio, unloading the machine for part-load with far less "
            "waste than a throttle valve. Variable stator vanes (VSVs): the "
            "front stators of a multistage axial compressor rotate in unison on "
            "their spindles, rescheduling incidence stage by stage as corrected "
            "speed changes - the direct cure for the front-stage stall of "
            "off-design operation. The control law schedules vane angle against "
            "corrected speed (and sometimes inlet temperature): at 70% speed the "
            "first stators may close 20+ degrees, handing each downstream rotor "
            "the incidence it wants. Turbines use it too: variable-area turbine "
            "nozzles (common in turbochargers - VGT) change the nozzle throat to "
            "match the turbine to the engine across the drive cycle, and "
            "variable-pitch Kaplan runners are variable geometry in hydro "
            "service. The cost is mechanical: spindles, bushings, unison rings, "
            "actuators - and the aerodynamic cost of the leakage around every "
            "movable vane's spindle."
        ),
        "how_it_works": (
            "A 10-stage industrial compressor must start without surging. At 80% "
            "corrected speed the VSV schedule closes the front stators, "
            "throttling the axial velocity back to the design flow coefficient. "
            "The front-stage incidence that would have been +13 deg (deep toward "
            "stall) returns to ~0 deg - the velocity triangle is restored, and "
            "the machine starts cleanly. As the machine accelerates to full "
            "speed, the schedule opens every vane to its design stagger in a "
            "choreographed sweep, and the operating line tracks safely right of "
            "the surge line the whole way up. In a turbocharger VGT, the same idea shrinks the turbine nozzle "
            "at low engine speed - raising exhaust back-pressure and turbine "
            "power to spin the compressor harder, killing turbo lag - and opens "
            "it at high speed to avoid choking. One mechanism, two miracles: "
            "stability for the compressor, responsiveness for the turbocharger."
        ),
        "key_points": [
            "IGVs throttle mass flow by pre-swirl at near-constant pressure ratio - part-load without throttle waste.",
            "VSVs reschedule front-stage incidence vs corrected speed - the cure for off-design front-stage stall.",
            "Control schedules vane angle against corrected speed: closed at low speed, design stagger at full speed.",
            "Turbine side: variable-area nozzles (VGT turbochargers) match turbine power to demand, killing lag.",
            "Costs: spindle/bushing/actuator mechanics plus spindle leakage - complexity traded for range and stability.",
        ],
        "requirements": [
            "The multistage-matching record (the problem VSVs solve).",
            "The performance-maps record (operating line vs surge line).",
        ],
        "standards": [
            "VSV schedule expressed against corrected speed per standard industrial practice.",
            "VGT (variable-geometry turbocharger) terminology per automotive practice.",
        ],
        "citations": [C_SARAV, C_CUMPSTY, C_DIXON],
        "sig_lens": (
            "Signature take: variable geometry is the Signature shapeshifter - "
            "blades that pivot to meet the moment. His Signature framing treats "
            "the vane schedule as choreography: every speed has its stance, and "
            "the unison ring conducts the whole front of the machine like an "
            "orchestra."
        ),
    },
    {
        "key": "combined_cycle",
        "name": "Combined Cycles and Cogeneration: Squeezing Every Joule",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The combined cycle refuses to waste the gas turbine's exhaust: at "
            "500-650 C it still holds most of the fuel's energy, so a heat-"
            "recovery steam generator (HRSG) raises steam and a Rankine "
            "bottoming cycle converts it - the gas turbine tops, the steam "
            "turbine bottoms, and the plant efficiency is eta_cc = eta_GT + "
            "eta_ST - eta_GT*eta_ST, routinely 60-64% LHV, the highest of any "
            "heat engine in commercial service. The HRSG is a counterflow "
            "boiler with no furnace: exhaust gas on one side, feedwater/steam on "
            "the other, arranged in superheater, evaporator, and economizer "
            "sections at two or three pressure levels to pinch the temperature "
            "profiles together. Cogeneration (CHP) goes further: instead of "
            "condensing the steam for maximum power, it extracts steam (or hot "
            "water) for district heating or industrial process - total fuel "
            "utilization 80-90%, at the cost of some electrical output. The "
            "design tension is the pinch point: closer gas/steam temperature "
            "approach recovers more heat but needs exponentially more HRSG "
            "surface - economics, not thermodynamics, sizes the boiler."
        ),
        "how_it_works": (
            "A 400 MW-class gas turbine at eta_GT = 0.38 exhausts 62% of its fuel "
            "heat at 600 C. The triple-pressure HRSG recovers it into steam at "
            "12 MPa/565 C (HP), 3 MPa (IP), 0.5 MPa (LP); the steam turbine "
            "converts 30% of the exhaust heat into shaft power (eta_ST = 0.30 on "
            "the bottoming heat). Combined efficiency: 0.38 + 0.30*(1-0.38) = "
            "0.38 + 0.186 = 0.566 - 56.6%, a 49% relative improvement over the "
            "gas turbine alone, with no new fuel burned. Push the gas turbine to "
            "0.40 and the bottoming to 0.32 and eta_cc = 0.592; the record "
            "machines with 1700 C-class TIT and advanced HRSGs touch 64%. The "
            "pinch analysis: at the evaporator, gas at 300 C meets saturated "
            "water at 280 C - a 20 K pinch; halving the pinch to 10 K would "
            "recover ~1% more heat but roughly double the evaporator surface - "
            "so the HRSG is optimized on cost per recovered megawatt, not on "
            "thermodynamics alone. In CHP mode, extracting 100 MW of 150 C "
            "process steam drops electrical output ~25 MW but the total useful "
            "energy (power + heat) reaches 85% of fuel - the right answer where "
            "heat has value."
        ),
        "key_points": [
            "Combined cycle: gas turbine topping + steam Rankine bottoming via HRSG; eta_cc = eta_GT + eta_ST - eta_GT*eta_ST.",
            "60-64% LHV: the most efficient commercial heat engine; ~50% relative gain over the gas turbine alone, no extra fuel.",
            "HRSG: unfired counterflow boiler (superheater/evaporator/economizer, multi-pressure) - pinch point sets the economics.",
            "Cogeneration extracts useful heat too: 80-90% total fuel utilization where heat has value.",
            "HRSG surface is cost-optimized, not thermodynamically maximized - economics sizes the boiler.",
        ],
        "requirements": [
            "The gas-turbine record and the steam-turbine record (the two cycles combined).",
            "Heat-exchanger pinch concept (idea level).",
        ],
        "standards": [
            "Efficiencies quoted LHV basis for gas-turbine plants per industry convention.",
            "HRSG sections and multi-pressure levels per standard combined-cycle practice.",
        ],
        "citations": [C_SARAV, C_CENGEL, C_WILSON],
        "sig_lens": (
            "Signature take: the combined cycle is the Signature second harvest "
            "- the exhaust becomes the fuel. His Signature framing treats the "
            "HRSG as the plant's conscience: it refuses to let 600-degree heat "
            "walk out the stack, and turns waste into the world's most efficient "
            "megawatts."
        ),
    },
    {
        "key": "condition_monitoring",
        "name": "Condition Monitoring and Failure Modes: Listening to the Machine",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Turbomachines telegraph their troubles in vibration, temperature, "
            "pressure, and oil - and condition monitoring is the discipline of "
            "reading the telegrams before the failure. Vibration is the richest "
            "signal: ISO 10816 zones A (new-machine good) through D (damage "
            "imminent) grade overall velocity; the spectrum diagnoses - 1x "
            "running speed is unbalance, 2x is misalignment or looseness, blade-"
            "pass frequency (blade count x rpm) with sidebands is rotor-stator "
            "rub or blade damage, ~0.42-0.48x is oil whip, sub-synchronous "
            "rumbles mark rotating stall. Performance monitoring watches the "
            "map: a compressor drifting left at constant corrected speed is "
            "fouling; rising vibration with falling efficiency is erosion; "
            "sudden thrust-bearing temperature excursion is the alarm that "
            "precedes a wipe. The classic failure modes each have a signature: "
            "fatigue (high-cycle blade failure from resonant excitation - the "
            "Campbell diagram's revenge), creep (hot-section life consumed by "
            "temperature), erosion (wet steam, dust, droplets), foreign-object "
            "damage (the dropped bolt), surge (the deep bang), and cavitation "
            "(the gravel roar). Monitoring turns random catastrophe into "
            "scheduled maintenance."
        ),
        "how_it_works": (
            "A 50 MW compressor train's vibration trend: baseline 2.1 mm/s RMS "
            "(Zone A/B boundary per ISO 10816-3 for this machine class). Over "
            "six weeks it creeps to 4.8 mm/s (Zone C - unsatisfactory for long-"
            "term operation) with the spectrum showing growth at 1x running speed "
            "(180 Hz at 10,800 rpm... 1x = 180 Hz) plus a new 0.45x component at "
            "81 Hz. Diagnosis: the 1x growth is unbalance - likely fouling "
            "deposit shedding unevenly or a blade erosion patch; the 0.45x is "
            "the early signature of oil whirl in a journal bearing, the "
            "precursor of whip. Action: schedule a wash (compressor fouling "
            "washes off with detergent + water while running), check bearing "
            "temperatures and oil condition, plan a borescope at the next outage "
            "- and set the trip at Zone D (7.1+ mm/s). Meanwhile performance: "
            "discharge pressure at constant corrected flow has sagged 2% - "
            "consistent with fouling, which also explains the unbalance. Two "
            "independent signals, one story: the machine is dirty, not dying. "
            "That is monitoring done right - the data converges before the "
            "wrench turns."
        ),
        "key_points": [
            "Vibration spectrum diagnoses: 1x = unbalance, 2x = misalignment, blade-pass = rub/damage, ~0.45x = oil whip, sub-sync = stall.",
            "ISO 10816 zones A-D grade severity; trends matter more than snapshots.",
            "Performance drift on the map (fouling walks left, erosion drops efficiency) corroborates vibration.",
            "Classic failure modes: fatigue, creep, erosion, FOD, surge, cavitation - each with a signature.",
            "Monitoring converts random catastrophe into scheduled maintenance: converge the signals before turning the wrench.",
        ],
        "requirements": [
            "The performance-maps record and the rotordynamics record.",
            "The surge/stall and cavitation records (failure signatures).",
        ],
        "standards": [
            "Vibration zones per ISO 10816-3; frequency analysis per standard machinery-diagnostics practice.",
            "Alarm/trip philosophy: alert in C, act before D.",
        ],
        "citations": [C_ISO10816, C_SARAV, C_API610],
        "sig_lens": (
            "Signature take: monitoring is the Signature stethoscope - the "
            "machine tells you everything if you learn its frequencies. His "
            "Signature framing treats the spectrum as the machine's confession: "
            "1x admits imbalance, blade-pass admits a rub, and 0.45x whispers "
            "that the oil film is plotting."
        ),
    },
    {
        "key": "design_workflow",
        "name": "The Design Workflow: From Duty Point to Manufactured Blade",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Designing a turbomachine is a disciplined descent from the duty "
            "point to metal, and it follows the ladder of this database in "
            "order. One: the duty (Q, H or pressure ratio, fluid, speed "
            "constraints) gives specific speed, which picks the geometry "
            "(radial/mixed/axial) and the specific diameter, which sizes it. "
            "Two: the dimensionless coefficients (phi, psi at the BEP) fix the "
            "velocity triangles - flow angles, blade speed, turning, Euler work. "
            "Three: degree of reaction splits the work between rotor and "
            "stator; de Haller and diffusion-factor limits check the "
            "aerodynamic loading; the blade count follows from solidity and the "
            "deviation rule. Four: the 2-D cascade sections are designed (camber, "
            "stagger, thickness) and stacked into 3-D blades with twist, lean, "
            "and sweep; tip clearance and seals are budgeted. Five: the "
            "structure is checked - centrifugal stress, creep life, critical "
            "speeds, bearing loads. Six: the map is predicted (stage-stacking), "
            "surge margin verified, control schedules (VSV, bleed) defined. "
            "Seven: CFD and rig tests validate, the design iterates, and only "
            "then is metal cut. Every step answers to the conservation laws, "
            "and the whole workflow is why the ladder teaches in this order."
        ),
        "how_it_works": (
            "Design a process pump: duty Q = 0.1 m^3/s, H = 60 m, water, motor "
            "1450 rpm. Step 1: Ns = 24.17*sqrt(0.1)/(9.81*60)^0.75 = 0.064 - "
            "radial; Ds ~ 43 from the Cordier band gives D ~ 0.42 m - wait, "
            "recheck with the earlier worked example's proportions: D ~ 0.42 m "
            "impeller at 1450 rpm gives U_2 = pi*0.42*1450/60 = 31.9 m/s, Euler "
            "head U_2^2/g ~ 104 m theoretical - plenty above the 60 m duty, "
            "leaving room for slip and losses. Step 2: pick phi = 0.08 at BEP: "
            "D = (Q/(phi*N))^(1/3) = 0.373 m, U_2 = 28.3 m/s, theoretical Euler "
            "head 81.6 m - headroom above the 60 m duty. Step 3: choose outlet "
            "blade angle 25 degrees backsweep, Z = 9 blades; Stodola slip sigma "
            "= 0.68; Euler head with slip ~ 56 m - within trim range of the "
            "duty, so the designer nudges D slightly and re-runs the loop. Step 4: volute sized for "
            "constant angular momentum, tongue gap set, NPSHr estimated from "
            "suction specific speed. Step 5: shaft sized for the critical-speed "
            "margin, bearings picked for 25,000 h L10. Step 6: predicted H-Q "
            "curve, BEP at the duty, surge... (pumps don't surge) - recirculation "
            "margin checked at low flow. Metal gets cut only after the map, the "
            "stresses, and the NPSH all agree."
        ),
        "key_points": [
            "Seven descents: duty -> Ns/Ds (geometry+size) -> triangles (work) -> reaction/loading (blading) -> 3-D stacking -> structures/rotordynamics -> map/controls.",
            "Each step uses the ladder's tools in ladder order: specific speed, coefficients, Euler, reaction, cascades, seals, critical speeds.",
            "Slip, deviation, and loss budgets connect the ideal triangles to the real metal.",
            "Validation (CFD, rig test) iterates the design; metal is cut last.",
            "The workflow is the ladder made practical: this database teaches in design order.",
        ],
        "requirements": [
            "Every record on the ladder - this is the capstone that uses them all.",
            "Iterative thinking: design is a loop, not a straight line.",
        ],
        "standards": [
            "Meanline-design methodology per Dixon & Hall / Wilson & Korakianitis.",
            "Validation hierarchy: meanline -> throughflow -> CFD -> rig test -> engine test.",
        ],
        "citations": [C_DIXON, C_WILSON, C_JAPIKSE],
        "sig_lens": (
            "Signature take: the workflow is the Signature pilgrimage - from a "
            "duty point written on paper to a blade that outlives its designer. "
            "His Signature framing treats each descent as an oath: the triangles "
            "swear to Euler, the metal swears to the triangles, and the test "
            "rig absolves them all."
        ),
    },
    {
        "key": "frontier",
        "name": "The Frontier: Hydrogen Turbines and Supercritical Carbon Dioxide",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Two frontiers are rewriting turbomachinery now. Hydrogen combustion: "
            "burning H2 in a gas turbine emits no CO2 - only water - but hydrogen "
            "burns ~8x faster than methane (flame speed ~2.9 vs ~0.4 m/s), with a "
            "far wider flammability range and a tiny quenching distance: the "
            "flame wants to flash back into the premixer. Combustors are being "
            "reinvented around it - micromix (hundreds of tiny diffusion flames), "
            "axial-staged, and sequential combustion - while the turbine itself "
            "barely changes (hot gas is hot gas) except for the higher water "
            "content of the exhaust. Supercritical CO2 (sCO2) power cycles: CO2 "
            "above its critical point (31 C, 7.38 MPa) is dense like a liquid "
            "but flows like a gas; compressing it near the critical point takes "
            "a fraction of the work of compressing a gas, so a recuperated "
            "Brayton cycle on sCO2 promises 45-50% efficiency at 550-700 C turbine "
            "inlet - steam-Rankine territory at gas-turbine simplicity - in a "
            "turbomachine set the size of a desk for tens of megawatts. The "
            "challenges are the flip side of the promise: near-critical property "
            "swings punish off-design, printed-circuit heat exchangers must "
            "contain 20-30 MPa, and dry gas seals must seal a dense supercritical "
            "fluid. Both frontiers obey the same ladder - Euler, triangles, "
            "maps - with new fluids and new flames."
        ),
        "how_it_works": (
            "An sCO2 recompression Brayton cycle: compressor inlet at 32 C, 7.5 "
            "MPa - just above critical. Density there is ~600 kg/m^3 (vs ~70 "
            "for the hot gas), so the compressor work per kilogram is tiny: "
            "compressing to 25 MPa takes roughly cp*T*ln(rp)-ish ~ 30 kJ/kg "
            "against a turbine output of ~130 kJ/kg at TIT 650 C - a back-work "
            "ratio near 0.23, versus ~0.5 for air Brayton. Cycle efficiency "
            "lands ~47% with recuperation effectiveness 0.95. The turbomachinery "
            "is startling: a 10 MW sCO2 turbine is ~0.3 m in diameter - the "
            "power density of the dense fluid shrinks everything, which makes "
            "tip clearance (still ~0.3 mm absolute) a crueler fraction of blade "
            "height and rotordynamics fiercer (100,000+ rpm concepts exist). On "
            "the hydrogen side: a micromix combustor splits the fuel into 1,600 "
            "tiny jets, each burning as a small diffusion flame with residence "
            "time under a millisecond - too fast for thermal NOx to form and too "
            "distributed to flash back. The turbine downstream sees ~1600 K gas "
            "with 15%+ water vapor: slightly higher heat transfer, slightly "
            "different expansion - the ladder's tools handle it, with updated "
            "gas properties. New fluids, new flames, same Euler."
        ),
        "key_points": [
            "Hydrogen turbines: zero-CO2 combustion; 8x flame speed and wide flammability demand new combustors (micromix, staged, sequential).",
            "Flashback is the hydrogen hazard; tiny distributed flames and sub-millisecond residence times defeat it and thermal NOx.",
            "sCO2 cycles: near-critical compression slashes back-work ratio (~0.23 vs ~0.5 air); 45-50% efficiency at 550-700 C TIT.",
            "sCO2 turbomachinery is desk-sized for tens of MW - but clearance fractions and rotordynamics get fiercer as blades shrink.",
            "Both frontiers run on the ladder's physics - Euler, triangles, maps - with new fluid properties and new flames.",
        ],
        "requirements": [
            "The gas-turbine record and the design-workflow record.",
            "Critical point concept; flame speed idea.",
        ],
        "standards": [
            "sCO2 critical point 31.1 C / 7.38 MPa; cycle layouts per current sCO2 literature.",
            "Hydrogen flame properties per standard combustion references.",
        ],
        "citations": [C_SARAV, C_CENGEL, C_WILSON],
        "sig_lens": (
            "Signature take: the frontier is the Signature horizon - hydrogen "
            "fire and a fluid that cannot decide if it is liquid or gas. His "
            "Signature framing treats both as the ladder's final exam: the "
            "physics you climbed still holds, and the only new answers are "
            "written in hotter flames and denser fluids."
        ),
    },
]
