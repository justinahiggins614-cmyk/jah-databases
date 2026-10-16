#!/usr/bin/env python3
"""PHASE D — Everything databases, entries part B: engineering, medicine &
health, earth science, astronomy & space, economics & finance.
(key, group, title, desc, points, requirements, standards, citations, demo_kind, src)
"""

ENTRIES_B = [
# ============================== ENGINEERING ==============================
("statics", "Mechanical",
 "Statics: Forces in Equilibrium",
 "Statics studies bodies at rest or in uniform motion — systems where forces balance exactly. A force is a "
 "vector: magnitude plus direction, resolved into components for analysis. Equilibrium demands two conditions: "
 "the vector sum of forces is zero (no translation) and the sum of moments about any point is zero (no "
 "rotation). Free-body diagrams isolate each part and expose every force acting on it. Trusses, frames, and "
 "bridges are designed in statics first: if it cannot stand still, it cannot stand at all.",
 ["Forces as vectors: magnitude plus direction",
  "Equilibrium: zero net force, zero net moment",
  "Free-body diagrams expose every acting force",
  "Trusses analyzed joint by joint, member by member",
  "The prerequisite of all structural design"],
 "Vector basics and basic trigonometry.",
 ["SI units; standard engineering notation"],
 "Standard engineering literature (statics textbooks).",
 "eng", "public-harvest"),
("mechanics-materials", "Mechanical",
 "Mechanics of Materials: Stress, Strain, and Elasticity",
 "Mechanics of materials asks what forces do inside a solid. Stress is force per unit area; strain is the "
 "resulting deformation per unit length. Hooke's law links them linearly in the elastic region — remove the "
 "load and the material springs back; exceed yield and deformation becomes permanent. The stress-strain curve "
 "maps the whole story: elastic region, yield point, strain hardening, fracture. Beam bending, torsion in "
 "shafts, and column buckling all follow from these relations, letting engineers size members so structures "
 "carry their loads with known safety margins.",
 ["Stress: force per unit area; strain: deformation per length",
  "Hooke's law in the elastic region",
  "Yield, strain hardening, fracture on the stress-strain curve",
  "Beam bending and torsion from the same relations",
  "Safety factors size members for known margins"],
 "Statics basics.",
 ["SI units; standard engineering notation"],
 "Standard engineering literature (mechanics of materials textbooks).",
 "eng", "public-harvest"),
("circuit-analysis", "Electrical",
 "Circuit Analysis: Ohm, Kirchhoff, and Power",
 "Circuit analysis reduces networks of components to solvable equations. Ohm's law (V = IR) relates voltage, "
 "current, and resistance in every resistor. Kirchhoff's current law: currents entering a node sum to zero. "
 "Kirchhoff's voltage law: voltages around any loop sum to zero. Together they yield the node and mesh "
 "equations that solve any linear circuit. Power — VI, or I^2 R — tracks energy conversion and heating, the "
 "practical limit of every design. Thevenin equivalents compress whole networks into one source and one "
 "resistor as seen from any port.",
 ["Ohm's law: V = IR in every resistor",
  "Kirchhoff's current law at nodes",
  "Kirchhoff's voltage law around loops",
  "Node and mesh analysis solve any linear circuit",
  "Power as VI; heating as the practical limit"],
 "Basic algebra and physics concepts.",
 ["SI units; IEC schematic conventions"],
 "Standard engineering literature (circuit analysis textbooks).",
 "eng", "public-harvest"),
("digital-logic", "Electrical",
 "Digital Logic: Boolean Algebra and Gates",
 "Digital logic builds computation from true and false. Boolean algebra — AND, OR, NOT with De Morgan's laws — "
 "is the mathematics; logic gates are the hardware. Combinational circuits compute pure functions of their "
 "inputs: adders, multiplexers, decoders. Sequential circuits add memory through flip-flops, creating state "
 "machines that step through time — the basis of processors. Karnaugh maps and algebraic minimization shrink "
 "circuits to their essentials. Every computer is, at bottom, an enormous precisely-arranged collection of "
 "these gates switching billions of times per second.",
 ["Boolean algebra: AND, OR, NOT, De Morgan's laws",
  "Gates as the hardware realization",
  "Combinational circuits: pure functions of inputs",
  "Sequential circuits: flip-flops and state machines",
  "Minimization shrinks circuits to essentials"],
 "Basic algebra and binary numbers.",
 ["IEEE logic symbols; SI units"],
 "Standard engineering literature (digital design textbooks).",
 "eng", "public-harvest"),
("control-systems", "Electrical",
 "Control Systems: Feedback and Stability",
 "Control systems make machines behave. Open-loop control issues commands blindly; closed-loop feedback "
 "measures the output, compares it to the target, and corrects the error — the thermostat principle. PID "
 "controllers combine proportional, integral, and derivative responses to kill error fast without overshoot. "
 "Stability analysis (poles in the left half-plane, gain and phase margins) guarantees corrections do not "
 "become oscillations. From cruise control to aircraft autopilots to chemical plants, feedback is the "
 "difference between a machine that acts and a machine that achieves.",
 ["Open-loop commands versus closed-loop feedback",
  "Error measurement and correction as the core loop",
  "PID: proportional, integral, derivative responses",
  "Stability analysis prevents corrective oscillation",
  "Applications: cruise control, autopilots, process plants"],
 "Differential equations intuition helpful; algebra required.",
 ["SI units; standard control notation"],
 "Standard engineering literature (control systems textbooks).",
 "eng", "public-harvest"),
("structural-engineering", "Civil",
 "Structural Engineering: Beams, Columns, and Loads",
 "Structural engineering keeps buildings and bridges standing. Loads divide into dead (the structure's own "
 "weight), live (occupants, traffic, stored goods), wind, and seismic — combined by code-specified factors. "
 "Beams carry transverse loads in bending; columns carry axial loads and must be checked against buckling, "
 "which can fail a slender column far below its crushing strength. Connections — bolts, welds — must develop "
 "the full member forces. Codes like ACI and AISC codify a century of lessons, many written after failures "
 "taught what analysis alone had missed.",
 ["Dead, live, wind, and seismic load categories",
  "Beams in bending; columns checked for buckling",
  "Connections must develop full member forces",
  "Load combinations per building codes",
  "Codes codify lessons learned from failures"],
 "Statics and mechanics of materials.",
 ["ACI 318; AISC 360; SI units"],
 "Standard engineering literature (structural design references).",
 "eng", "public-harvest"),
("fluid-mechanics-eng", "Civil",
 "Fluid Mechanics for Engineers",
 "Engineers meet fluids in pipes, pumps, dams, and drainage. Hydrostatics gives pressure as rho-g-h — "
 "pressure growing linearly with depth, acting normal to every surface. Bernoulli's equation trades pressure, "
 "velocity, and elevation along a streamline, sizing pipes and predicting flow. The Darcy-Weisbach relation "
 "quantifies friction loss in pipes; Moody charts read it from roughness and Reynolds number. Pumps add head, "
 "turbines extract it. Open-channel flow — rivers, sewers, spillways — runs on the same principles with a "
 "free surface.",
 ["Hydrostatic pressure as rho-g-h",
  "Bernoulli: pressure, velocity, elevation trade-offs",
  "Pipe friction via Darcy-Weisbach and Moody charts",
  "Pumps add head; turbines extract it",
  "Open-channel flow for rivers and drainage"],
 "Calculus basics; statics helpful.",
 ["SI units; standard fluid notation"],
 "Standard engineering literature (fluid mechanics textbooks).",
 "eng", "public-harvest"),
("engineering-drawing", "Design & Practice",
 "Engineering Drawing: Tolerances and Fits",
 "Engineering drawings are the contract between designer and machinist. Orthographic projection shows the "
 "part in true-shape views; sections reveal interiors; dimensions locate every feature. Tolerances state how "
 "much variation is allowed — no part is ever made exactly — and fits (clearance, transition, interference) "
 "define how mating parts assemble. Geometric dimensioning and tolerancing (GD&T) controls form, orientation, "
 "and position with symbolic precision. A complete drawing package lets any competent shop build the part "
 "without asking a single question.",
 ["Orthographic views and sections describe the part",
  "Dimensions locate every feature exactly",
  "Tolerances state allowable variation",
  "Fits define how mating parts assemble",
  "GD&T controls form and position symbolically"],
 "Basic geometry and spatial visualization.",
 ["ASME Y14.5 (GD&T); ISO 2768; SI units"],
 "Standard engineering literature (drafting references).",
 "eng", "public-harvest"),
("sig-load-path", "Signature Engineering",
 "Signature Load Path Geometry",
 "A Signature original design that traces structural loads as visible geometric paths: every force enters at "
 "a load point and flows through members to the supports, drawn as a continuous Signature load network. "
 "Bottlenecks — members carrying disproportionate flow — stand out geometrically before any number is "
 "computed. The design preserves statics exactly while giving the engineer a canonical load-flow record that "
 "is deterministic and inspectable. A Signature treatment of structures where you see the forces before you "
 "calculate them.",
 ["Loads traced as continuous geometric paths",
  "Force flow from load points to supports",
  "Bottlenecks visible before computation",
  "Statics preserved exactly in geometric form",
  "Canonical deterministic load-flow records"],
 "Statics basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard engineering literature.",
 "eng", "signature"),
("sig-circuit-harmonizer", "Signature Engineering",
 "Signature Circuit Harmonizer",
 "A Signature original instrument that lays circuits out as harmonic networks: voltages as levels, currents "
 "as flows, components as verified transformations between them. Kirchhoff's laws become geometric closure "
 "conditions — what flows in must flow out, visibly. The harmonizer checks consistency of any network "
 "deterministically and flags the exact node or loop where an inconsistency lives. A Signature treatment of "
 "circuit analysis as verifiable network geometry.",
 ["Circuits as harmonic networks: levels and flows",
  "Kirchhoff's laws as geometric closure conditions",
  "Deterministic consistency checking of any network",
  "Faults localized to the exact node or loop",
  "Circuit analysis as verifiable geometry"],
 "Circuit analysis basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard engineering literature.",
 "eng", "signature"),
("sig-tolerance-engine", "Signature Engineering",
 "Signature Tolerance Engine",
 "A Signature original engine that treats tolerances as computable geometry: every dimension carries its "
 "allowable variation as a bounded region, and assemblies are verified by proving the regions always mate — "
 "worst-case stack-ups computed exactly, not estimated. The engine flags tolerance conflicts at design time "
 "and suggests the minimal loosening that resolves them. A Signature treatment of manufacturing precision as "
 "deterministic geometric proof.",
 ["Tolerances as bounded geometric regions",
  "Assembly verified by worst-case proof, not estimate",
  "Stack-ups computed exactly",
  "Conflicts flagged at design time",
  "Minimal corrections suggested deterministically"],
 "Engineering drawing basics.",
 ["Signature system conventions; ASME Y14.5 concepts"],
 "Original Signature design; classical facts per standard engineering literature.",
 "eng", "signature"),
("sig-machine-workability", "Signature Engineering",
 "Signature Workability Proofs for Machines",
 "A Signature original framework that certifies a machine design workable before it is built: every mechanism "
 "gets a proof record covering range of motion, force transmission, interference clearance, and failure modes. "
 "Linkages, gears, and actuators are verified as geometric constructions with stated operating envelopes. A "
 "design is workable only when its proof record is complete and checkable — the Signature standard that "
 "nothing ships on hope. A Signature treatment of mechanical design as certified construction.",
 ["Machine designs certified before building",
  "Proof records: motion, forces, clearance, failure modes",
  "Mechanisms as verified geometric constructions",
  "Operating envelopes stated explicitly",
  "Nothing ships on hope: proof-gated design"],
 "Mechanical engineering basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard engineering literature.",
 "eng", "signature"),
# ============================== MEDICINE & HEALTH ==============================
("human-anatomy-ref", "Anatomy",
 "Human Anatomy: A Systems Reference",
 "This educational reference maps the body's major systems and their principal structures. The skeletal "
 "system (206 bones) frames and protects; skeletal muscle moves it under nervous command; the heart drives "
 "the cardiovascular loop; lungs exchange gases across alveolar membranes; the digestive tract processes "
 "nutrients from mouth to colon; kidneys filter blood into urine; the brain and spinal cord integrate "
 "signaling. Surface landmarks, organ positions, and tissue types are described factually as the shared "
 "vocabulary of medicine. Educational reference only — not a substitute for clinical training.",
 ["Skeletal, muscular, nervous: frame, motion, command",
  "Cardiovascular and respiratory: transport and exchange",
  "Digestive and urinary: processing and filtration",
  "Endocrine and immune: signaling and defense",
  "Shared anatomical vocabulary of medicine"],
 "Basic biology vocabulary.",
 ["Terminologia Anatomica"],
 "Standard medical literature (anatomy references). Educational content.",
 "med", "public-harvest"),
("cardiovascular", "Physiology",
 "The Cardiovascular System",
 "The cardiovascular system delivers oxygen and nutrients while removing wastes. The heart — two atria, two "
 "ventricles, four valves — pumps in a double loop: pulmonary to the lungs, systemic to the body. Arteries "
 "carry blood away under pressure; capillaries exchange across thin walls; veins return it. Blood pressure "
 "(systolic over diastolic), heart rate, and cardiac output quantify performance. Atherosclerosis — plaque "
 "narrowing arteries — underlies heart attacks and strokes, the world's leading killers, and is driven by "
 "modifiable risks: smoking, hypertension, cholesterol, diabetes, inactivity. Educational reference only.",
 ["Double-loop pump: pulmonary and systemic circuits",
  "Arteries, capillaries, veins: delivery, exchange, return",
  "Blood pressure, heart rate, cardiac output as metrics",
  "Atherosclerosis underlies heart attacks and strokes",
  "Major risks are modifiable: smoking, pressure, cholesterol"],
 "Human anatomy basics.",
 ["Standard medical terminology"],
 "Standard medical literature (physiology references). Educational content.",
 "med", "public-harvest"),
("infectious-disease", "Clinical",
 "Infectious Disease: Pathogens and Immunity",
 "Infectious diseases come from pathogens: bacteria, viruses, fungi, parasites. Transmission routes — "
 "airborne droplets, contaminated water or food, vectors like mosquitoes, direct contact — determine control "
 "measures. The immune system answers in layers: innate barriers and inflammation first, then adaptive "
 "antibodies and T-cells with memory. Vaccines train adaptive immunity without the disease, one of "
 "medicine's greatest triumphs — smallpox eradicated, polio nearly so. Hygiene, clean water, and vaccination "
 "remain the highest-leverage interventions in global health. Educational reference only.",
 ["Pathogen classes: bacteria, viruses, fungi, parasites",
  "Transmission routes determine control measures",
  "Innate then adaptive immunity, with memory",
  "Vaccines train immunity without disease",
  "Sanitation and vaccines as highest-leverage interventions"],
 "Microbiology basics helpful.",
 ["Standard medical terminology"],
 "Standard medical literature (infectious disease references). Educational content.",
 "med", "public-harvest"),
("pharmacology", "Clinical",
 "Pharmacology: Drug Classes and Action",
 "Pharmacology studies how drugs act on the body. Drugs bind targets — usually receptors or enzymes — as "
 "agonists (activating) or antagonists (blocking). Pharmacokinetics tracks absorption, distribution, "
 "metabolism, and excretion: what the body does to the drug. Pharmacodynamics tracks the drug's effect: what "
 "the drug does to the body, summarized in dose-response curves. Major classes — antibiotics, antihypertensives, "
 "analgesics, insulin and antidiabetics — each address a physiological lever. Interactions and side effects "
 "are inseparable from benefits at therapeutic doses. Educational reference only — never a prescribing guide.",
 ["Targets: receptors and enzymes; agonists vs antagonists",
  "Pharmacokinetics: the body acts on the drug",
  "Pharmacodynamics: the drug acts on the body",
  "Dose-response curves summarize effect versus dose",
  "Benefits inseparable from interactions and side effects"],
 "Chemistry and physiology basics.",
 ["Standard medical terminology"],
 "Standard medical literature (pharmacology references). Educational content.",
 "med", "public-harvest"),
("nutrition-science", "Wellness",
 "Nutrition Science: Macronutrients and Micronutrients",
 "Nutrition science studies how food sustains the body. Macronutrients — carbohydrates and fats for energy, "
 "protein for building and repair — supply calories; fiber, though indigestible, supports gut health. "
 "Micronutrients — vitamins and minerals — enable metabolism in milligram and microgram amounts; deficiencies "
 "cause specific diseases (scurvy, rickets, anemia). Energy balance governs weight: sustained surplus stores "
 "fat, sustained deficit burns it. Dietary patterns rich in vegetables, whole grains, and legumes are "
 "consistently associated with better outcomes across populations. Educational reference only.",
 ["Macros: carbs and fats for energy, protein for structure",
  "Fiber supports gut health though indigestible",
  "Micronutrients enable metabolism in tiny amounts",
  "Deficiencies cause specific diseases",
  "Energy balance governs weight change"],
 "Basic biology and chemistry intuition.",
 ["Standard nutritional terminology"],
 "Standard nutrition literature (dietary references). Educational content.",
 "med", "public-harvest"),
("exercise-physiology", "Wellness",
 "Exercise Physiology: Training the Body",
 "Exercise physiology studies the body's response to physical work. Aerobic exercise trains the "
 "cardiovascular system — stroke volume rises, resting heart rate falls, mitochondria multiply. Resistance "
 "training builds muscle through progressive overload: stress, recover, adapt. The FITT principle organizes "
 "training: frequency, intensity, time, and type. Recovery — sleep, nutrition, rest days — is when adaptation "
 "happens; training without it is just damage. Regular moderate activity is among the strongest predictors of "
 "healthy lifespan in the epidemiological literature. Educational reference only.",
 ["Aerobic training adapts heart, vessels, mitochondria",
  "Resistance training via progressive overload",
  "FITT: frequency, intensity, time, type",
  "Recovery is when adaptation occurs",
  "Regular activity predicts healthy lifespan"],
 "Basic physiology intuition.",
 ["Standard exercise terminology"],
 "Standard sports-medicine literature. Educational content.",
 "med", "public-harvest"),
("mental-wellness", "Wellness",
 "Mental Wellness: Stress and Resilience Concepts",
 "Mental wellness concepts describe how minds handle pressure. Stress is the body's mobilization for demand — "
 "useful short-term, harmful when chronic, raising cardiovascular and immune risks. Sleep consolidates memory "
 "and regulates emotion; chronic short sleep degrades both. Evidence-supported resilience practices include "
 "regular physical activity, consistent sleep schedules, social connection, and structured problem-solving. "
 "Cognitive-behavioral approaches teach identifying and testing unhelpful thought patterns. This is "
 "educational information about general wellness concepts — not diagnosis or treatment, and not a substitute "
 "for professional care.",
 ["Stress: useful acutely, harmful chronically",
  "Sleep consolidates memory and regulates emotion",
  "Activity, sleep routine, connection support resilience",
  "Cognitive-behavioral concepts: testing thought patterns",
  "Educational information, not clinical care"],
 "None — written for a general reader.",
 ["Standard psychological terminology"],
 "Standard behavioral-health literature. Educational content; not clinical advice.",
 "med", "public-harvest"),
("public-health", "Public Health",
 "Public Health and Epidemiology",
 "Public health protects populations rather than treating individuals. Epidemiology measures disease in "
 "populations: incidence (new cases), prevalence (existing cases), and risk ratios comparing groups. Study "
 "designs — cohort, case-control, randomized trials — trade feasibility against rigor. Surveillance systems "
 "detect outbreaks early; contact tracing and quarantine break transmission chains. Clean water, sanitation, "
 "tobacco control, and vaccination are the field's historic victories, each saving millions of lives through "
 "prevention rather than cure.",
 ["Incidence, prevalence, and risk ratios",
  "Study designs: cohort, case-control, trials",
  "Surveillance detects outbreaks early",
  "Tracing and quarantine break transmission",
  "Prevention's historic victories: water, tobacco, vaccines"],
 "Basic statistics intuition helpful.",
 ["Standard epidemiological terminology"],
 "Standard public-health literature (epidemiology references).",
 "med", "public-harvest"),
("sig-health-metrics", "Signature Health",
 "Signature Health Metrics Engine",
 "A Signature original engine that computes standard wellness metrics — BMI, heart-rate zones, energy "
 "balance, training load — as deterministic records from stated inputs, with every formula shown and every "
 "result reproducible. The engine labels every output as an educational reference metric, never a diagnosis, "
 "and carries the applicable population caveats (athletes, pregnancy, age) as part of each record. A "
 "Signature treatment of health math: transparent formulas, honest limits, reproducible numbers.",
 ["Standard metrics as deterministic reproducible records",
  "Every formula shown with its inputs",
  "Population caveats carried in each record",
  "Educational metrics, never diagnoses",
  "Transparent formulas with honest limits"],
 "Basic arithmetic.",
 ["Signature system conventions"],
 "Original Signature design; formulas per standard references. Educational content.",
 "med", "signature"),
("sig-dosage-geometry", "Signature Health",
 "Signature Dosage Geometry",
 "A Signature original framework that treats dosing schedules as geometric records: dose amounts as heights, "
 "intervals as spacing, blood-level curves as the resulting terrain. The design computes coverage windows and "
 "flags gaps or overlaps deterministically from the schedule alone. It is an educational instrument for "
 "understanding how schedules relate to levels — it never prescribes, adjusts, or recommends any real "
 "medication regimen. A Signature treatment of schedule mathematics with patient-safety labeling throughout.",
 ["Schedules as geometric records: amounts, intervals, curves",
  "Coverage windows computed deterministically",
  "Gaps and overlaps flagged from the schedule",
  "Educational instrument; never a prescribing guide",
  "Safety labeling carried in every record"],
 "Basic algebra.",
 ["Signature system conventions"],
 "Original Signature design. Educational content; not medical advice.",
 "med", "signature"),
("sig-wellness-planner", "Signature Health",
 "Signature Wellness Planner",
 "A Signature original planner that builds weekly wellness schedules — activity, sleep windows, meal rhythm — "
 "as deterministic plans from stated goals and constraints. Plans adapt by rule, not by opaque judgment: "
 "missed sessions reschedule by stated policy, progression follows the overload-and-recover principle. Every "
 "plan carries its assumptions openly and labels itself an educational planning aid. A Signature treatment of "
 "wellness planning as transparent, reproducible scheduling.",
 ["Weekly plans from stated goals and constraints",
  "Rule-based adaptation, openly stated",
  "Overload-and-recover progression built in",
  "Assumptions carried openly in each plan",
  "Educational planning aid, reproducibly generated"],
 "Basic arithmetic.",
 ["Signature system conventions"],
 "Original Signature design. Educational content; not medical advice.",
 "med", "signature"),
("sig-epi-mapper", "Signature Health",
 "Signature Epidemiology Mapper",
 "A Signature original instrument that maps population health data as geographic Signature records: case "
 "counts aggregated by region and time, incidence and prevalence computed deterministically, trends rendered "
 "as readable change maps. The design works on public aggregate statistics — never individual records — and "
 "labels every figure with its source period and population. A Signature treatment of population health "
 "numbers as transparent, auditable geographic records.",
 ["Aggregate population data as geographic records",
  "Incidence and prevalence computed deterministically",
  "Trends as readable change maps",
  "Aggregate statistics only; no individual records",
  "Every figure labeled with period and population"],
 "Basic statistics intuition.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard epidemiology literature.",
 "med", "signature"),
# ============================== EARTH SCIENCE ==============================
("plate-tectonics", "Geology",
 "Plate Tectonics: The Moving Earth",
 "Earth's outer shell is broken into tectonic plates that creep centimeters per year over the ductile mantle. "
 "At divergent boundaries plates pull apart and new crust forms — the Mid-Atlantic Ridge. At convergent "
 "boundaries they collide: ocean plates subduct, melting into magma that feeds volcanoes, while continental "
 "collisions raise mountain ranges like the Himalayas. Transform boundaries grind sideways, storing the "
 "stress released as earthquakes along faults like San Andreas. Plate tectonics unified geology by explaining "
 "continents, oceans, volcanoes, and quakes as one moving system.",
 ["Lithospheric plates creep over the ductile mantle",
  "Divergent boundaries create new crust",
  "Convergent boundaries subduct plates and build mountains",
  "Transform boundaries store earthquake stress",
  "One theory unifying continents, oceans, volcanoes, quakes"],
 "Basic physics intuition.",
 ["Standard geological terminology"],
 "Standard earth-science literature (geology textbooks).",
 "earth", "public-harvest"),
("rock-cycle", "Geology",
 "The Rock Cycle: Igneous, Sedimentary, Metamorphic",
 "Rocks transform continuously through the rock cycle. Magma cooling into solid forms igneous rock — granite "
 "from slow underground cooling, basalt from fast surface flows. Weathering and erosion break rock into "
 "sediment; compaction and cementation lithify it into sedimentary rock, often in revealing layers. Heat and "
 "pressure without melting recrystallize any rock into metamorphic forms like marble from limestone. Melting "
 "completes the loop. The cycle has no beginning or end — Earth's crust is endlessly remade.",
 ["Igneous: magma cooled to solid",
  "Sedimentary: compacted and cemented sediment",
  "Metamorphic: heat and pressure recrystallization",
  "Weathering, erosion, melting drive the transitions",
  "Crust endlessly remade; no start or end"],
 "Basic chemistry intuition helpful.",
 ["Standard geological terminology"],
 "Standard earth-science literature (geology textbooks).",
 "earth", "public-harvest"),
("weather", "Meteorology",
 "Weather: The Atmosphere in Motion",
 "Weather is the atmosphere's short-term state, driven by uneven solar heating. Warm air rises at the equator, "
 "cool air sinks at the poles, and Earth's rotation bends the flows into prevailing winds and jet streams. "
 "High-pressure systems bring fair skies; low-pressure systems bring clouds and storms as air converges and "
 "rises. Fronts — boundaries between air masses — trigger much mid-latitude weather. Humidity, measured as "
 "relative or absolute, decides whether rising air forms clouds and rain. Forecasting models solve fluid "
 "equations on supercomputers, skillful for days, chaotic beyond two weeks.",
 ["Uneven solar heating drives circulation",
  "Rotation bends flows into winds and jet streams",
  "High pressure: fair; low pressure: storms",
  "Fronts as boundaries between air masses",
  "Humidity decides cloud and rain formation"],
 "Basic physics intuition.",
 ["WMO terminology; SI units"],
 "Standard earth-science literature (meteorology textbooks).",
 "earth", "public-harvest"),
("climate-systems", "Meteorology",
 "Climate Systems and Zones",
 "Climate is weather averaged over decades — the long-term pattern a region can expect. Latitude sets the "
 "master template: tropical wet near the equator, arid belts near 30 degrees, temperate mid-latitudes, polar "
 "beyond 60. Oceans moderate coastal climates; mountains wring out rain on windward slopes and cast rain "
 "shadows leeward; altitude cools with height. The Koppen classification maps these into coded zones from "
 "tropical rainforest (Af) to ice cap (EF). Climate change — the current human-driven shift — is measured "
 "against this baseline of natural zones.",
 ["Climate: weather averaged over decades",
  "Latitude template: tropical, arid, temperate, polar",
  "Oceans moderate; mountains shape rainfall",
  "Koppen classification codes the zones",
  "Human-driven change measured against natural baselines"],
 "Weather basics.",
 ["WMO terminology; SI units"],
 "Standard earth-science literature (climatology references).",
 "earth", "public-harvest"),
("water-cycle", "Hydrology",
 "The Water Cycle and Hydrology",
 "Water cycles endlessly: evaporation from oceans and transpiration from plants lift vapor skyward; "
 "condensation forms clouds; precipitation returns it as rain and snow; runoff and groundwater flow carry it "
 "back to the sea. Residence times vary wildly — days in the atmosphere, millennia in deep aquifers and ice "
 "sheets. Hydrology manages the usable fraction: watersheds collect it, aquifers store it, wells and "
 "reservoirs withdraw it. Only about 2.5 percent of Earth's water is fresh, and most of that is locked in ice.",
 ["Evaporation, condensation, precipitation, runoff",
  "Residence times: days to millennia",
  "Watersheds collect; aquifers store",
  "2.5 percent of Earth's water is fresh",
  "Groundwater as a slow, finite savings account"],
 "Basic physics and chemistry intuition.",
 ["Standard hydrological terminology; SI units"],
 "Standard earth-science literature (hydrology textbooks).",
 "earth", "public-harvest"),
("oceanography", "Oceanography",
 "Oceanography: Currents, Tides, and Seafloor",
 "Oceans cover 71 percent of Earth's surface and drive its climate. Surface currents — wind-driven gyres — "
 "redistribute heat from equator to poles; the Gulf Stream warms Western Europe far beyond its latitude. Deep "
 "thermohaline circulation creeps on century timescales, sinking cold salty water at the poles. Tides rise "
 "from the Moon's (and lesser, the Sun's) gravitational pull, cycling roughly twice daily. The seafloor "
 "spreads at mid-ocean ridges and plunges at trenches — plate tectonics written in bathymetry.",
 ["Oceans cover 71 percent of the surface",
  "Wind-driven gyres redistribute heat",
  "Thermohaline circulation on century timescales",
  "Tides from lunar and solar gravity",
  "Seafloor spreading records plate motion"],
 "Basic physics intuition.",
 ["Standard oceanographic terminology; SI units"],
 "Standard earth-science literature (oceanography textbooks).",
 "earth", "public-harvest"),
("soil-science", "Geology",
 "Soil Science: Formation and Classification",
 "Soil is weathered rock plus organic matter, air, and water — the living skin of the continents. The five "
 "forming factors (parent material, climate, organisms, topography, time) produce horizons: topsoil rich in "
 "organic matter over subsoil over weathered parent material. Texture — the sand-silt-clay ratio — controls "
 "drainage and workability; structure and pH control fertility. Soil taxonomy classifies the world's soils "
 "into twelve orders, from fertile Mollisols of the grasslands to ancient Oxisols of the tropics. A centimeter "
 "of topsoil can take centuries to form and a single storm to lose.",
 ["Five forming factors produce soil horizons",
  "Texture: sand-silt-clay ratios control drainage",
  "pH and organic matter control fertility",
  "Twelve soil orders in global taxonomy",
  "Topsoil forms over centuries, erodes in storms"],
 "Basic chemistry intuition helpful.",
 ["USDA soil taxonomy"],
 "Standard earth-science literature (soil science references).",
 "earth", "public-harvest"),
("natural-hazards", "Hazards",
 "Natural Hazards: Earthquakes and Volcanoes",
 "Earthquakes release stored tectonic stress as seismic waves; magnitude (energy released) differs from "
 "intensity (shaking felt). The Ring of Fire — the Pacific's plate boundaries — hosts most major quakes and "
 "volcanoes. Volcanoes erupt where magma reaches the surface: runny basaltic lava builds shield volcanoes, "
 "sticky silica-rich magma explodes into stratovolcanoes. Hazards are assessed by mapping faults, monitoring "
 "deformation and gas, and modeling inundation — then mitigated by building codes, early warning, and "
 "evacuation planning, because the events cannot be prevented, only prepared for.",
 ["Magnitude measures energy; intensity measures shaking",
  "Ring of Fire hosts most quakes and volcanoes",
  "Lava chemistry decides eruption style",
  "Monitoring: deformation, gas, seismicity",
  "Mitigation through codes, warning, evacuation"],
 "Plate tectonics basics.",
 ["USGS terminology; moment magnitude scale"],
 "Standard earth-science literature (hazards references).",
 "earth", "public-harvest"),
("sig-terrain-geometry", "Signature Earth Science",
 "Signature Terrain Geometry",
 "A Signature original treatment that models terrain as exact geometric records: elevation as a deterministic "
 "surface, watersheds as bounded drainage regions, slopes and aspects as computed surface properties. "
 "Erosion patterns, viewsheds, and flood extents are derived as verifiable geometric operations on the "
 "surface rather than opaque simulations. A Signature treatment of landforms where the shape of the ground "
 "is a computable, auditable record.",
 ["Terrain as exact deterministic surfaces",
  "Watersheds as bounded drainage regions",
  "Slope, aspect, viewshed as computed properties",
  "Erosion and flood extents as geometric operations",
  "Auditable landform records"],
 "Basic geometry intuition.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard earth-science literature.",
 "earth", "signature"),
("sig-climate-pattern", "Signature Earth Science",
 "Signature Climate Pattern Engine",
 "A Signature original engine that organizes climate observations as deterministic pattern records on a "
 "Signature lattice: temperature and precipitation series become comparable geometric signatures, anomalies "
 "stand out as measurable deviations, and zone classifications are computed reproducibly from the data. "
 "The engine separates observed patterns from projections, labeling each clearly. A Signature treatment of "
 "climate data as transparent, reproducible pattern records.",
 ["Climate series as comparable geometric signatures",
  "Anomalies as measurable deviations",
  "Reproducible zone classification from data",
  "Observations separated from projections, labeled clearly",
  "Transparent pattern records"],
 "Climate basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard earth-science literature.",
 "earth", "signature"),
("sig-seismic-analyzer", "Signature Earth Science",
 "Signature Seismic Wave Analyzer",
 "A Signature original instrument that treats seismograms as deterministic signal records: P, S, and surface "
 "waves identified by arrival geometry, epicenters located by multi-station triangulation computed exactly. "
 "Magnitude-energy relationships are applied as verified formulas with stated scales. Built as an educational "
 "instrument for understanding how earthquake location and size are actually determined from wave arrivals.",
 ["Seismograms as deterministic signal records",
  "P, S, surface waves by arrival geometry",
  "Epicenter triangulation computed exactly",
  "Magnitude-energy as verified formulas",
  "Educational instrument for real location methods"],
 "Wave physics basics helpful.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard earth-science literature.",
 "earth", "signature"),
("sig-watershed-mapper", "Signature Earth Science",
 "Signature Watershed Mapper",
 "A Signature original instrument that delineates watersheds as exact bounded regions on Signature terrain: "
 "every drop's drainage path computed deterministically to its outlet, stream networks ordered by hierarchy, "
 "catchment areas measured exactly. Water budgets — precipitation in, evapotranspiration and runoff out — are "
 "kept as balanced accounts. A Signature treatment of hydrology where drainage is provable geometry.",
 ["Watersheds as exact bounded regions",
  "Deterministic drainage paths to outlets",
  "Stream networks ordered by hierarchy",
  "Water budgets as balanced accounts",
  "Drainage as provable geometry"],
 "Water cycle basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard earth-science literature.",
 "earth", "signature"),
# ============================== ASTRONOMY & SPACE ==============================
("solar-system", "Solar System",
 "The Solar System: Planets and Small Bodies",
 "Our solar system formed 4.6 billion years ago from a collapsing cloud of gas and dust. Four rocky inner "
 "planets — Mercury, Venus, Earth, Mars — orbit close to the Sun; four giants — Jupiter, Saturn, Uranus, "
 "Neptune — rule the outer reaches, Jupiter alone outweighing all the others combined. The asteroid belt "
 "sits between Mars and Jupiter; the Kuiper belt and Oort cloud harbor icy leftovers including Pluto and "
 "the comets. Every planet's year and day, atmosphere, and moons follow from where it formed and what it "
 "captured.",
 ["4.6-billion-year formation from a collapsing cloud",
  "Rocky inner planets; giant outer planets",
  "Asteroid belt, Kuiper belt, Oort cloud as leftover reservoirs",
  "Pluto as a Kuiper belt dwarf planet",
  "Planetary traits follow from formation location"],
 "Basic physics intuition.",
 ["IAU nomenclature"],
 "Standard astronomy literature (planetary science references).",
 "astro", "public-harvest"),
("stars", "Stellar Astronomy",
 "Stars: Birth, Life, and Death",
 "Stars are fusion furnaces: gravity compresses gas until cores ignite hydrogen into helium, and the "
 "outward radiation pressure balances the inward crush for billions of years. Mass decides fate: Sun-like "
 "stars swell into red giants and fade as white dwarfs; massive stars explode as supernovae, forging heavy "
 "elements and leaving neutron stars or black holes. The Hertzsprung-Russell diagram — luminosity versus "
 "temperature — maps stellar life stages at a glance. Every atom heavier than helium in your body was forged "
 "in a star or its explosive death.",
 ["Fusion: hydrogen to helium under gravitational compression",
  "Mass decides stellar fate",
  "Red giants, white dwarfs, supernovae, neutron stars, black holes",
  "Hertzsprung-Russell diagram maps life stages",
  "Heavy elements forged in stars and supernovae"],
 "Basic physics intuition.",
 ["IAU nomenclature"],
 "Standard astronomy literature (astrophysics textbooks).",
 "astro", "public-harvest"),
("galaxies-cosmology", "Cosmology",
 "Galaxies and the Expanding Universe",
 "Galaxies are island universes of billions of stars: spirals like the Milky Way, ellipticals, and "
 "irregulars shaped by collision. In the 1920s Hubble found galaxies receding with speeds proportional to "
 "distance — the universe is expanding. Run the expansion backward and everything converges about 13.8 "
 "billion years ago: the Big Bang. The cosmic microwave background — the cooled afterglow — and the "
 "abundances of light elements confirm the hot early picture. Dark matter and dark energy, though unseen, "
 "dominate the cosmic budget and drive current research.",
 ["Galaxy types: spiral, elliptical, irregular",
  "Hubble's law: recession speed proportional to distance",
  "13.8-billion-year age from expansion reversal",
  "Microwave background confirms the hot early universe",
  "Dark matter and dark energy dominate the budget"],
 "Basic physics intuition.",
 ["IAU nomenclature"],
 "Standard astronomy literature (cosmology references).",
 "astro", "public-harvest"),
("orbital-mechanics", "Spaceflight",
 "Orbital Mechanics: Kepler and Newton",
 "Kepler's three laws describe orbits: ellipses with the Sun at one focus; equal areas swept in equal times; "
 "period squared proportional to semi-major axis cubed. Newton derived them from universal gravitation plus "
 "his laws of motion, unifying celestial and terrestrial physics. Orbits are energy states: raise the energy "
 "and the ellipse grows; reach escape velocity and it never closes. Hohmann transfers — the fuel-efficient "
 "ellipse tangent to both orbits — are the workhorse of interplanetary travel, timing included.",
 ["Kepler's three laws of planetary motion",
  "Newton's derivation from gravitation",
  "Orbits as energy states; escape velocity",
  "Hohmann transfers for efficient travel",
  "Timing and phasing for rendezvous"],
 "Algebra and basic physics.",
 ["Standard astrodynamics terminology; SI units"],
 "Standard astronomy literature (orbital mechanics textbooks).",
 "astro", "public-harvest"),
("telescopes", "Observation",
 "Telescopes: How We Observe the Sky",
 "Telescopes gather light: refractors bend it through lenses, reflectors bounce it off mirrors — the design "
 "that dominates modern astronomy. Aperture decides light-gathering power and resolution; adaptive optics "
 "corrects atmospheric shimmer in real time. Radio dishes, space telescopes above the atmosphere, and "
 "interferometers linking dishes across continents extend vision across the spectrum. Spectroscopy splits "
 "captured light into fingerprints revealing composition, temperature, and motion through redshift. Every "
 "image is a time machine: distant light shows the universe as it was.",
 ["Light-gathering power grows with aperture",
  "Reflectors dominate modern astronomy",
  "Adaptive optics defeats atmospheric shimmer",
  "Spectroscopy reads composition and redshift",
  "Distant light is a look into the past"],
 "Basic physics intuition.",
 ["Standard astronomical terminology"],
 "Standard astronomy literature (observational references).",
 "astro", "public-harvest"),
("moon", "Solar System",
 "The Moon: Phases, Tides, and Exploration",
 "The Moon — likely born from a giant impact early in Earth's history — is our nearest celestial neighbor at "
 "about 384,400 km. Its phases are geometry: we see the sunlit portion from changing angles through the "
 "month. Tides rise mainly from the Moon's gravity pulling Earth's oceans into bulges. Tidal locking keeps "
 "the same face toward us; the far side is simply the face we never see, not a dark one. Twelve Apollo "
 "astronauts walked its surface between 1969 and 1972, and robotic and crewed missions are returning.",
 ["Likely formed by a giant impact",
  "Phases as changing sunlit geometry",
  "Tides from lunar gravitational pull",
  "Tidal locking keeps one face Earthward",
  "Apollo landings 1969-1972; new missions underway"],
 "Basic physics intuition.",
 ["IAU nomenclature"],
 "Standard astronomy literature (lunar references).",
 "astro", "public-harvest"),
("exoplanets", "Stellar Astronomy",
 "Exoplanets: Worlds Around Other Stars",
 "Over five thousand exoplanets are now confirmed. The transit method catches the tiny dip as a planet "
 "crosses its star; radial velocity senses the star's gravitational wobble; direct imaging photographs a "
 "few. Hot Jupiters hug their stars; super-Earths have no solar-system analog; the habitable zone marks where "
 "liquid water could exist. Kepler's census showed planets are common — most stars have them — and current "
 "telescopes are beginning to sniff the atmospheres of rocky worlds for biosignatures.",
 ["5,000+ confirmed exoplanets and counting",
  "Transit, radial velocity, direct imaging methods",
  "Hot Jupiters, super-Earths, habitable zones",
  "Planets are common: most stars have them",
  "Atmospheric biosignature searches underway"],
 "Basic physics intuition.",
 ["IAU nomenclature"],
 "Standard astronomy literature (exoplanet references).",
 "astro", "public-harvest"),
("spaceflight", "Spaceflight",
 "Spaceflight: Rockets, Orbits, and Delta-V",
 "Rockets work by reaction: expelling mass backward pushes the vehicle forward, per Newton's third law — and "
 "the Tsiolkovsky rocket equation prices every maneuver in propellant. Delta-v, the total velocity change a "
 "vehicle can produce, is the currency of spaceflight: reaching orbit costs about 9.4 km/s from Earth's "
 "surface. Staging drops empty tanks to shed dead weight; gravity assists steal momentum from planets. "
 "Reusable boosters, pioneered at scale in the 2010s, collapsed launch costs and opened the current era of "
 "high flight rates.",
 ["Reaction propulsion per Newton's third law",
  "Tsiolkovsky equation prices maneuvers in propellant",
  "Delta-v as the currency of spaceflight",
  "Staging sheds dead weight; gravity assists steal momentum",
  "Reusability collapsed launch costs"],
 "Basic physics intuition.",
 ["Standard astronautical terminology; SI units"],
 "Standard astronautics literature (spaceflight references).",
 "astro", "public-harvest"),
("sig-orbital-geometry", "Signature Astronomy",
 "Signature Orbital Geometry",
 "A Signature original treatment that renders orbits as exact geometric records: Keplerian elements carried "
 "precisely, transfers drawn as verifiable constructions, rendezvous phasing computed deterministically. "
 "Every maneuver becomes a geometric operation with stated delta-v cost and checkable result — the "
 "Tsiolkovsky equation preserved as the accounting rule. A Signature treatment of astrodynamics where "
 "trajectories are provable geometry before they are flown.",
 ["Orbits as exact geometric records",
  "Transfers as verifiable constructions",
  "Rendezvous phasing computed deterministically",
  "Delta-v costs stated and checkable",
  "Trajectories as provable geometry"],
 "Orbital mechanics basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard astronomy literature.",
 "astro", "signature"),
("sig-star-catalog", "Signature Astronomy",
 "Signature Star Catalog Engine",
 "A Signature original engine that organizes stellar data as a deterministic catalog: positions, magnitudes, "
 "spectral types, and distances carried as exact records with stated uncertainties. Queries — cone searches, "
 "magnitude cuts, spectral selections — execute reproducibly on the Signature lattice. Cross-matching between "
 "catalogs is performed as verified record linkage with confidence scores. A Signature treatment of the sky's "
 "inventory as a rigorous, queryable archive.",
 ["Stellar data as deterministic catalog records",
  "Positions, magnitudes, spectra with stated uncertainties",
  "Reproducible cone searches and selections",
  "Verified cross-catalog record linkage",
  "The sky's inventory as a rigorous archive"],
 "Basic astronomy concepts.",
 ["Signature system conventions; IAU nomenclature"],
 "Original Signature design; classical facts per standard astronomy literature.",
 "astro", "signature"),
("sig-deepspace-mapper", "Signature Astronomy",
 "Signature Deep-Space Mapper",
 "A Signature original instrument that charts deep-sky structure as layered Signature geometry: galaxies, "
 "clusters, and large-scale filaments positioned by redshift-derived distances with uncertainties carried "
 "openly. The mapper keeps observed positions separate from inferred cosmology, labeling each layer. Zoom "
 "levels from solar neighborhood to cosmic web are deterministic views of one underlying record. A Signature "
 "treatment of cosmic cartography with honest uncertainty at every scale.",
 ["Deep-sky structure as layered geometry",
  "Redshift distances with open uncertainties",
  "Observed positions separated from inferred cosmology",
  "Deterministic zoom from local to cosmic web",
  "Honest uncertainty at every scale"],
 "Galaxies and cosmology basics.",
 ["Signature system conventions; IAU nomenclature"],
 "Original Signature design; classical facts per standard astronomy literature.",
 "astro", "signature"),
("sig-mission-planner", "Signature Astronomy",
 "Signature Mission Planner",
 "A Signature original planner that designs space missions as deterministic sequences: launch windows from "
 "planetary phasing, transfer arcs with stated delta-v budgets, arrival conditions computed exactly. Every "
 "plan carries its assumptions — propulsion performance, mass margins, timing tolerance — as checkable "
 "records. Trade studies compare architectures side by side on identical grounds. A Signature treatment of "
 "mission design as transparent, reproducible planning.",
 ["Missions as deterministic event sequences",
  "Launch windows from planetary phasing",
  "Delta-v budgets stated and checkable",
  "Assumptions carried as checkable records",
  "Architecture trade studies on identical grounds"],
 "Orbital mechanics and spaceflight basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard astronautics literature.",
 "astro", "signature"),
# ============================== ECONOMICS & FINANCE ==============================
("microeconomics", "Economics",
 "Microeconomics: Supply, Demand, and Markets",
 "Microeconomics studies individual decisions and their aggregation. The supply-and-demand model: quantity "
 "supplied rises with price, quantity demanded falls, and the market clears where they meet — the equilibrium "
 "price. Elasticity measures responsiveness: how much quantity moves when price moves. Shifts in the curves — "
 "income changes, input costs, tastes — move equilibrium predictably. Market structures range from perfect "
 "competition through monopoly, each with different pricing power and efficiency properties. Externalities, "
 "where costs or benefits fall on third parties, are the classic case for intervention.",
 ["Supply rises with price; demand falls",
  "Equilibrium where the curves cross",
  "Elasticity measures price responsiveness",
  "Curve shifts move equilibrium predictably",
  "Externalities as the classic intervention case"],
 "Basic algebra and graph reading.",
 ["Standard economic terminology"],
 "Standard economics literature (microeconomics textbooks).",
 "econ", "public-harvest"),
("macroeconomics", "Economics",
 "Macroeconomics: GDP, Inflation, Unemployment",
 "Macroeconomics studies whole economies. GDP — the market value of final goods and services produced — is "
 "the headline measure of output. Inflation, tracked by price indexes like the CPI, erodes purchasing power; "
 "central banks typically target around 2 percent. Unemployment counts those seeking work without finding it, "
 "with frictional, structural, and cyclical varieties. The business cycle alternates expansions and "
 "recessions; fiscal policy (government spending and taxes) and monetary policy (interest rates) are the "
 "standard stabilization tools.",
 ["GDP as the headline output measure",
  "Inflation tracked by price indexes; ~2% the usual target",
  "Unemployment: frictional, structural, cyclical",
  "Business cycles alternate expansion and recession",
  "Fiscal and monetary policy as stabilizers"],
 "Microeconomics basics helpful.",
 ["Standard economic terminology"],
 "Standard economics literature (macroeconomics textbooks).",
 "econ", "public-harvest"),
("personal-finance", "Finance",
 "Personal Finance: Budgeting and Saving",
 "Personal finance is applied arithmetic with discipline. A budget assigns every dollar a job — the zero-based "
 "method popularized by practitioners leaves nothing unassigned. Pay yourself first: automate savings before "
 "spending what's left. Emergency funds (typically 3-6 months of expenses) absorb shocks without debt. "
 "Compound interest rewards early saving enormously and punishes carried balances symmetrically. Net worth — "
 "assets minus liabilities, tracked over time — is the scoreboard that matters, not income alone. "
 "Educational information, not financial advice.",
 ["Zero-based budgeting assigns every dollar",
  "Automate savings before spending",
  "Emergency funds absorb shocks without debt",
  "Compound interest rewards early, punishes late",
  "Net worth tracked over time is the scoreboard"],
 "Basic arithmetic.",
 ["Standard financial terminology"],
 "Standard personal-finance literature. Educational content; not financial advice.",
 "econ", "public-harvest"),
("investing", "Finance",
 "Investing: Stocks, Bonds, Diversification",
 "Investing trades present money for larger future money, bearing risk. Stocks are ownership shares with "
 "residual claims on profits; bonds are loans paying contracted interest. Expected return rises with risk — "
 "the risk premium compensates bearing uncertainty. Diversification spreads holdings so single failures "
 "cannot sink the portfolio; broad index funds implement this cheaply. Time horizon dominates strategy: "
 "long horizons tolerate equity volatility, short ones demand safety. Fees compound against you exactly as "
 "returns compound for you. Educational information, not financial advice.",
 ["Stocks: ownership; bonds: contracted loans",
  "Expected return rises with risk",
  "Diversification limits single-failure damage",
  "Time horizon dominates strategy choice",
  "Fees compound against the investor"],
 "Personal finance basics.",
 ["Standard financial terminology"],
 "Standard investing literature. Educational content; not financial advice.",
 "econ", "public-harvest"),
("banking", "Finance",
 "Banking: Interest and Credit",
 "Banks intermediate between savers and borrowers, earning the spread. Interest prices time and risk: the "
 "borrower pays for early use of money, more when default risk is higher. Fractional-reserve banking multiplies "
 "base money into broader money supply through lending. Credit scores summarize repayment history into a "
 "number lenders trust; utilization, history length, and on-time payment drive it. Central banks set policy "
 "rates that ripple through every loan in the economy. Deposit insurance backstops the system against runs. "
 "Educational information, not financial advice.",
 ["Banks earn the spread between savers and borrowers",
  "Interest prices time and default risk",
  "Fractional reserves multiply base money",
  "Credit scores summarize repayment history",
  "Central bank rates ripple through all lending"],
 "Basic algebra.",
 ["Standard financial terminology"],
 "Standard banking literature. Educational content; not financial advice.",
 "econ", "public-harvest"),
("intl-trade", "Economics",
 "International Trade and Exchange Rates",
 "Countries trade on comparative advantage: each specializes where its opportunity cost is lowest, and both "
 "gain — Ricardo's insight that survives two centuries of scrutiny. Exchange rates price currencies against "
 "each other, floating on supply and demand or fixed by policy. A weaker currency cheapens exports and "
 "dearborns imports; the reverse strengthens purchasing power abroad. Tariffs tax imports to protect domestic "
 "producers, at consumers' expense. Balance of payments accounts track every cross-border flow, and must — by "
 "accounting identity — balance.",
 ["Comparative advantage: specialize by lowest opportunity cost",
  "Exchange rates price currencies relatively",
  "Weak currency: cheap exports, dear imports",
  "Tariffs protect producers at consumers' expense",
  "Balance of payments balances by identity"],
 "Microeconomics basics.",
 ["Standard economic terminology"],
 "Standard economics literature (trade textbooks).",
 "econ", "public-harvest"),
("behavioral-econ", "Economics",
 "Behavioral Economics: Decisions and Biases",
 "Behavioral economics studies how people actually decide, biases included. Loss aversion: losses hurt roughly "
 "twice as much as equal gains please, warping risk choices. Present bias discounts the future hyperbolically, "
 "undermining saving and health plans. Anchoring lets irrelevant numbers drag estimates; framing changes "
 "choices without changing options. Nudges — choice architecture preserving freedom — apply these findings: "
 "automatic enrollment, default options, simplified forms. The field disciplines policy with how humans "
 "behave, not how models wish they would.",
 ["Loss aversion warps risk choices",
  "Present bias undermines long-term plans",
  "Anchoring and framing shift decisions",
  "Nudges apply findings while preserving choice",
  "Policy disciplined by actual behavior"],
 "Microeconomics basics helpful.",
 ["Standard economic terminology"],
 "Standard economics literature (behavioral references).",
 "econ", "public-harvest"),
("accounting", "Finance",
 "Accounting: The Balance Sheet Equation",
 "Accounting is the language of business, and its founding sentence is Assets = Liabilities + Equity: what "
 "the firm owns equals what it owes plus what owners claim. Double-entry bookkeeping records every "
 "transaction twice — debit and credit — so the books must balance; imbalance means error. The income "
 "statement reports profit over a period; the cash-flow statement tracks actual money movement, which profit "
 "can obscure. Accrual accounting matches revenues and expenses to their period, not to cash timing. Audits "
 "test whether statements fairly present reality. Educational information, not professional advice.",
 ["Assets = Liabilities + Equity, always",
  "Double-entry: every transaction twice",
  "Income statement: profit over a period",
  "Cash-flow statement: actual money movement",
  "Accrual matches activity to its period"],
 "Basic arithmetic.",
 ["GAAP/IFRS concepts"],
 "Standard accounting literature. Educational content; not professional advice.",
 "econ", "public-harvest"),
("sig-value-geometry", "Signature Economics",
 "Signature Value Geometry",
 "A Signature original treatment that models value flows as geometric records: transactions as directed edges "
 "between account nodes, balances as node states, budgets as bounded regions that flows must respect. "
 "Double-entry becomes geometric closure — every flow accounted at both ends. The design makes cash-flow "
 "statements, budgets, and ledgers three views of one deterministic record. A Signature treatment of money "
 "in motion as verifiable geometry.",
 ["Transactions as directed edges between accounts",
  "Balances as node states; budgets as bounded regions",
  "Double-entry as geometric closure",
  "Ledger, budget, cash flow as one record's views",
  "Verifiable money-in-motion geometry"],
 "Accounting basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard economics literature.",
 "econ", "signature"),
("sig-market-pattern", "Signature Economics",
 "Signature Market Pattern Engine",
 "A Signature original engine that reads market price series as deterministic pattern records on a Signature "
 "lattice: trends as sustained slopes, volatility as measured dispersion, support and resistance as tested "
 "levels with hit counts. Every pattern carries its statistical footing — sample size, time frame, base "
 "rates — so signals are never presented without their evidence. The engine is an educational instrument for "
 "understanding price history; it predicts nothing and labels itself accordingly.",
 ["Price series as deterministic pattern records",
  "Trends, volatility, levels as measured features",
  "Every pattern carries its statistical footing",
  "Educational instrument; predicts nothing",
  "Signals never presented without evidence"],
 "Statistics basics.",
 ["Signature system conventions"],
 "Original Signature design. Educational content; not financial advice.",
 "econ", "signature"),
("sig-budget-harmonizer", "Signature Economics",
 "Signature Budget Harmonizer",
 "A Signature original planner that builds household and project budgets as deterministic Signature records: "
 "income as inflow, categories as bounded allocations, actuals reconciled against plan each period. "
 "Variances are flagged with causes where stated; forecasts extend the plan by rule, not by opaque judgment. "
 "The design keeps the zero-based discipline — every dollar assigned — as a verifiable property of the "
 "record. A Signature treatment of budgeting as reproducible arithmetic.",
 ["Budgets as deterministic allocation records",
  "Inflows, categories, actuals reconciled per period",
  "Variances flagged with stated causes",
  "Forecasts by rule, openly stated",
  "Zero-based discipline as a verifiable property"],
 "Basic arithmetic.",
 ["Signature system conventions"],
 "Original Signature design. Educational content; not financial advice.",
 "econ", "signature"),
("sig-trade-mapper", "Signature Economics",
 "Signature Trade Flow Mapper",
 "A Signature original instrument that maps trade as flow geometry: goods and payments as directed streams "
 "between economies, comparative advantage as measurable opportunity-cost gradients, balances as net flow "
 "records. Tariff scenarios recompute deterministically from stated rates; supply-chain dependencies appear "
 "as visible concentrations. A Signature treatment of international commerce as auditable flow records.",
 ["Trade as directed flow geometry",
  "Comparative advantage as measurable gradients",
  "Tariff scenarios recomputed deterministically",
  "Dependencies visible as concentrations",
  "Auditable commerce records"],
 "International trade basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard economics literature.",
 "econ", "signature"),
]
