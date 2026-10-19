#!/usr/bin/env python3
"""Entries for the Mining and Extractive Industries database pair (5,000-target program).

Dedupe gate: all 68 titles checked against the WHOLE system with
code/dedupe_gate.py BEFORE writing. ID prefixes JAH-MNEI- (public) and
JAH-MNEIS- (signature) verified free: zero hits in manifest id_prefix values
(exact + substring) and zero hits in shard record IDs.

34 records per edition, ladder-ordered 1-34 (Foundations 1-12 / Compounded
13-23 / Advanced 24-34).
"""


def R(t, tier, rank, desc, how, kp, req, std, cit, dk, data):
    return {'t': t, 'tier': tier, 'rank': rank, 'desc': desc, 'how': how,
            'kp': kp, 'req': req, 'std': std, 'cit': cit, 'dk': dk, 'data': data}


PUB = [
R("What Mining Is — Industry Overview", "Foundations", 1,
  "Mining is the industry that extracts minerals, metals, coal, and stone from the earth and delivers them to processing and markets. "
  "It begins with exploration and ends with closure and reclamation, spanning geology, engineering, and environmental stewardship. "
  "Modern life runs on mined materials: every building, vehicle, and electronic device contains minerals pulled from the ground.",
  "Geologists find and define the ore body; engineers plan how to extract it safely and economically; miners drill, blast, load, and haul the rock. "
  "Processing plants crush, grind, and separate the valuable minerals from waste, and the product ships to smelters or markets. "
  "Through it all, safety systems protect workers, environmental controls protect land and water, and closure plans return the site to stable use.",
  ["Mining extracts minerals and delivers them to processing and markets.",
   "The chain: exploration, planning, extraction, processing, closure.",
   "Modern life is built from mined materials.",
   "Safety, environment, and closure are part of mining, not afterthoughts."],
  ["A defined mineral deposit with estimated tonnage and grade.",
   "Mining, processing, and environmental expertise.",
   "Permits, social license, and capital for the long development."],
  ["Worker safety per mining health and safety regulations.",
   "Environmental permits and monitoring from exploration onward.",
   "Closure and reclamation planned before mining begins."],
  ["SME Mining Engineering Handbook (public reference).",
   "National mining health and safety regulations (public regulations)."],
  "metal", {"tonnes": 5000000.0, "grade_pct": 1.2}),

R("Minerals, Ores, and Grades", "Foundations", 2,
  "A mineral is a naturally occurring solid with a defined chemistry; an ore is rock containing enough valuable mineral to mine profitably; grade is the concentration of the valuable part. "
  "Grade decides everything: a copper ore at 1% carries ten kilograms of copper per tonne, and the economics hinge on that number. "
  "Cut-off grade - the lowest grade worth processing - separates ore from waste.",
  "Geologists log drill core, assay samples for metal content, and map grade shells in three dimensions. "
  "The resource model multiplies tonnage by grade to estimate contained metal, and the cut-off is set where revenue per tonne covers mining plus processing cost. "
  "Below cut-off the rock is waste; above it, ore - the same rock judged by economics.",
  ["Mineral: the substance. Ore: rock worth mining. Grade: its concentration.",
   "Grade times tonnage gives contained metal.",
   "Cut-off grade separates ore from waste by economics.",
   "The same rock is ore or waste depending on price and cost."],
  ["Geological logging and assay laboratory capacity.",
   "A three-dimensional model of grade distribution.",
   "Cost and price inputs for the cut-off calculation."],
  ["Assays by certified methods with quality control samples.",
   "Resource reporting per JORC or NI 43-101 codes.",
   "Grade control during mining to the plan."],
  ["JORC Code for reporting exploration results and resources (public code).",
   "SME grade-control literature (public publications)."],
  "metal", {"tonnes": 12000000.0, "grade_pct": 0.8}),

R("Geological Mapping", "Foundations", 3,
  "Geological mapping is the drawing of the earth's story at the surface: rock types, structures, faults, and alteration that hint where ore hides. "
  "It is exploration's first and cheapest tool - boots, hammer, and notebook before drills and dollars. "
  "A good map focuses all later work; a poor one wastes it.",
  "Geologists traverse the ground, recording outcrops, measuring the orientation of layers and faults, and collecting samples for assay. "
  "Remote sensing and geophysics extend the map under cover, and everything compiles into maps and cross-sections. "
  "Targets emerge where structure, alteration, and geochemistry coincide - the classic signatures of ore systems.",
  ["Mapping is exploration's first, cheapest tool.",
   "Outcrops, structures, and alteration point to ore.",
   "Geophysics extends the map under cover.",
   "Targets form where structure, alteration, and chemistry coincide."],
  ["Access to the ground and trained field geologists.",
   "Base maps: topography, imagery, and prior geology.",
   "Sample bags, GPS, and a database for observations."],
  ["Tenement and land-access permissions secured.",
   "Heritage and environmental surveys before disturbance.",
   "Data recorded systematically, not in scattered notebooks."],
  ["Geological survey mapping standards (public standards).",
   "Exploration best-practice literature (public publications)."],
  "stripratio", {"waste": 3000000.0, "ore": 1000000.0}),

R("Exploration Drilling", "Foundations", 4,
  "Exploration drilling is how geologists see underground: diamond or reverse-circulation rigs boring holes to bring up rock for logging and assay. "
  "Each hole is a one-dimensional truth through the ore body; many holes together build its three-dimensional shape. "
  "Drilling is exploration's biggest cost and its most decisive act.",
  "Targets from mapping and geophysics are drilled in patterns - wide-spaced first, then infill as confidence grows. "
  "Core is logged for geology and structure, split, and half sent for assay; downhole surveys keep the hole's path true. "
  "Results extend, reshape, or kill the target: the drill is the final arbiter of every exploration idea.",
  ["Drilling brings the underground up for logging and assay.",
   "Each hole a one-dimensional truth; many holes a 3D shape.",
   "Wide spacing first, infill for confidence.",
   "The drill is the final arbiter of exploration ideas."],
  ["Drill rigs matched to depth and ground: diamond or RC.",
   "Logging geologists and assay laboratory turnaround.",
   "Downhole survey tools for true hole paths."],
  ["Drill pads rehabilitated after the program.",
   "Groundwater intersected is managed, not ignored.",
   "Safety: rotating machinery, high pressure, remote sites."],
  ["Drilling industry safety and environmental guidance (public guidance).",
   "JORC Code on exploration reporting (public code)."],
  "drill", {"holes": 48, "avg_depth_m": 220.0}),

R("Sampling and Assaying", "Foundations", 5,
  "Sampling takes representative pieces of rock; assaying measures what is in them - together they are the evidence behind every resource number. "
  "A biased sample corrupts everything downstream: the resource, the mine plan, the economics. "
  "Quality control - blanks, standards, and duplicates in every batch - proves the numbers can be trusted.",
  "Channel, chip, or core samples are collected on defined intervals, crushed, split, and pulverized to a homogeneous pulp. "
  "Fire assay or instrumental analysis measures the metals; every batch carries QA/QC inserts that must pass before results are accepted. "
  "Failed QA/QC quarantines the batch for re-assay, because one bad batch can poison a resource model.",
  ["Sampling and assaying are the evidence behind resource numbers.",
   "Biased sampling corrupts the resource, the plan, and the economics.",
   "QA/QC inserts in every batch prove the numbers.",
   "Failed QA/QC quarantines the batch."],
  ["Sampling protocols: intervals, sizes, and handling.",
   "An accredited assay laboratory.",
   "QA/QC materials: blanks, certified standards, duplicates."],
  ["Chain of custody from ground to lab.",
   "QA/QC failure rates within accepted limits.",
   "Assay methods fit for the elements reported."],
  ["JORC Code QA/QC expectations (public code).",
   "ISO/IEC 17025 lab accreditation standard (public standard)."],
  "recovery", {"feed_metal": 850.0, "recovered_metal": 782.0}),

R("Open Pit Mining", "Foundations", 6,
  "Open pit mining extracts ore from a terraced excavation open to the sky, the method of choice for large, near-surface deposits. "
  "Benches - the terraces - are blasted, loaded by shovels, and hauled by trucks up spiral ramps. "
  "Pits grow deeper and wider over decades, following the ore down until the stripping cost outweighs the metal.",
  "Benches are drilled and blasted, then electric shovels or loaders fill haul trucks that climb the ramps to crushers or waste dumps. "
  "Pit walls are engineered to stable angles with geotechnical monitoring; dewatering keeps the floor workable. "
  "The ultimate pit limit is economic: the last shell where ore value still pays for the waste moved to reach it.",
  ["Terraced excavation for large, near-surface deposits.",
   "Drill, blast, load, haul: the pit's heartbeat.",
   "Wall angles engineered and monitored for stability.",
   "The pit limit is economic: ore value must pay the stripping."],
  ["Shovels, trucks, and drills sized to the production rate.",
   "Geotechnical design and wall monitoring.",
   "Dewatering and pit drainage."],
  ["Wall stability monitored with prisms, radar, or lidar.",
   "Blast vibration and flyrock controlled near limits.",
   "Traffic rules separating light vehicles from haul trucks."],
  ["SME open-pit design literature (public publications).",
   "Mining health and safety regulations for pits (public regulations)."],
  "stripratio", {"waste": 45000000.0, "ore": 15000000.0}),

R("Underground Mining Methods", "Foundations", 7,
  "Underground mining reaches deep or high-value ore through shafts, declines, and tunnels, extracting it with methods matched to the ore body's shape and strength. "
  "Cut-and-fill, sublevel stoping, block caving, and room-and-pillar each suit different ground. "
  "Underground mines trade higher cost per tonne for selectivity and small surface footprint.",
  "Access is driven by decline or shaft; development opens the ore; stopes are blasted and mucked in cycles. "
  "Ground support - bolts, mesh, shotcrete - holds the openings; backfill replaces extracted ore where needed. "
  "Ventilation pushes fresh air to the faces and clears blasting fumes and diesel exhaust, the invisible lifeline of the underground.",
  ["Shafts, declines, and tunnels reach deep ore.",
   "Methods matched to ore shape and ground strength.",
   "Higher cost per tonne, smaller surface footprint.",
   "Ventilation is the invisible lifeline."],
  ["Development to open the ore body.",
   "Ground support: bolts, mesh, shotcrete, backfill.",
   "Ventilation sized for people, diesel, and blasting."],
  ["Ground control management plans enforced.",
   "Ventilation quantities monitored against the plan.",
   "Refuge chambers and emergency egress maintained."],
  ["Underground mining methods literature (public publications).",
   "Mine ventilation and ground-control regulations (public regulations)."],
  "cutoff", {"cost_per_t_ore": 28.0, "price_per_t_metal": 9500.0, "recovery": 0.92}),

R("Drilling and Blasting", "Foundations", 8,
  "Drilling and blasting breaks rock for excavation: holes drilled in a pattern, charged with explosives, and fired in a timed sequence that fractures the rock into diggable fragments. "
  "It is mining's oldest industrial art and still its most dramatic - and most regulated. "
  "Good blasting makes digging easy; bad blasting makes boulders, flyrock, and angry neighbors.",
  "Engineers design the pattern - burden, spacing, hole depth - and the timing sequence that throws rock toward the free face. "
  "Holes are drilled, charged with ANFO or emulsion, stemmed, and tied to detonators fired in millisecond delays. "
  "Fragmentation is judged by the shovel's ease and the crusher's appetite; vibration and airblast are monitored against limits.",
  ["Drill the pattern, charge the holes, fire the timed sequence.",
   "Timing throws rock toward the free face in diggable fragments.",
   "Fragmentation judged by digging ease and crusher appetite.",
   "Vibration and airblast monitored against limits."],
  ["Drill rigs and explosives supply (ANFO, emulsion, detonators).",
   "Blast designs signed by a competent engineer.",
   "Vibration and airblast monitoring."],
  ["Explosives magazines secured per regulation.",
   "Blast guards and clearance before every shot.",
   "Misfires handled by procedure, never improvised."],
  ["Explosives manufacture, storage, and use regulations (public regulations).",
   "Blasting vibration standards (public standards)."],
  "blast", {"holes": 120, "kg_per_hole": 85.0, "tonnes_broken": 45000.0}),

R("Loading and Hauling", "Foundations", 9,
  "Loading and hauling moves the blasted rock: shovels and loaders fill trucks that carry ore to the crusher and waste to the dumps. "
  "It is the most visible and often the costliest part of open-pit mining - diesel, tires, and maintenance on a grand scale. "
  "Matching loader and truck sizes, and keeping them moving, is the fleet manager's art.",
  "Shovels spot trucks, fill each pass to rated payload without overloading, and the trucks run fixed routes on engineered haul roads. "
  "Dispatch systems assign trucks to shovels to balance the fleet; road maintenance - watering, grading - protects tires and cycle times. "
  "Payload monitoring weighs every load, because underloading wastes trips and overloading breaks trucks.",
  ["Shovels load, trucks haul: the pit's materials handling.",
   "Fleet matching and dispatch keep every unit productive.",
   "Haul roads engineered and maintained for tires and times.",
   "Payload monitored: neither underloaded nor overloaded."],
  ["Shovels and trucks sized and matched to the production rate.",
   "Engineered haul roads with watering and grading.",
   "A dispatch system balancing the fleet."],
  ["Traffic management separating light and heavy vehicles.",
   "Berm and bund standards on haul roads.",
   "Fatigue management for equipment operators."],
  ["Haul-road design literature (public publications).",
   "Mining mobile-equipment safety regulations (public regulations)."],
  "haul", {"trucks": 24, "payload_t": 220.0, "trips_per_day": 18.0}),

R("Mine Ventilation Basics", "Foundations", 10,
  "Mine ventilation delivers fresh air underground and removes what harms: blasting fumes, diesel exhaust, dust, heat, and naturally occurring gases. "
  "Air is the underground mine's invisible infrastructure - without it, nothing else works. "
  "Quantity, quality, and distribution are engineered and monitored continuously.",
  "Main fans push or pull air through the mine's airways; regulators and stoppings direct it to the working faces. "
  "Diesel equipment sets the quantity - roughly 0.06 cubic meters per second per kilowatt in many regulations - and gas monitoring watches for the dangerous ones. "
  "Ventilation surveys measure every split against the plan, because air short-circuits through the path of least resistance.",
  ["Fresh air in, fumes and dust out: the invisible infrastructure.",
   "Diesel power sets the required air quantity.",
   "Regulators and stoppings direct air to the faces.",
   "Surveys verify every split against the plan."],
  ["Main and auxiliary fans sized to the mine's demand.",
   "Airways, regulators, and stoppings maintained.",
   "Gas and airflow monitoring instruments."],
  ["Air quantities per diesel and personnel regulations.",
   "Gas alarms with defined evacuation actions.",
   "Ventilation plans updated as the mine grows."],
  ["Mine ventilation engineering texts (public publications).",
   "Underground ventilation regulations (public regulations)."],
  "water", {"flow_lps": 45.0}),

R("Mine Safety Fundamentals", "Foundations", 11,
  "Mine safety is the discipline that brings every worker home: identifying hazards, controlling them, and building a culture where anyone can stop unsafe work. "
  "Mining's hazards - ground falls, mobile equipment, explosives, gases, dust - are unforgiving of carelessness. "
  "The industry's best mines prove zero harm is achievable through systems, not luck.",
  "Hazards are identified per task, controls applied in the hierarchy - eliminate, engineer, administrate, protect - and verified in the field. "
  "Pre-start checks, toolbox talks, and visible leadership make safety the day's first subject. "
  "Incidents and near-misses are reported without blame and investigated to root cause, because the near-miss is the free lesson.",
  ["Every worker home: the non-negotiable goal.",
   "Hazards identified per task; controls verified in the field.",
   "Anyone can stop unsafe work.",
   "Near-misses reported without blame, investigated to root cause."],
  ["A safety management system with real authority.",
   "Training and competency verification for every role.",
   "Emergency response: rescue teams, refuge, communications."],
  ["Regulatory safety standards obeyed and audited.",
   "Fitness for work: fatigue, substances, health.",
   "Contractor safety managed as rigorously as employees'."],
  ["National mine health and safety regulations (public regulations).",
   "ICMM safety leadership guidance (public guidance)."],
  "recovery", {"feed_metal": 1200.0, "recovered_metal": 1092.0}),

R("Mining Math I — Tonnage, Grade, and Metal Content", "Foundations", 12,
  "Mining math begins with the tonne and the grade: tonnage times grade gives contained metal, the number every mine plan and valuation rests on. "
  "A million tonnes at 1% copper holds ten thousand tonnes of copper - and at ten thousand dollars a tonne, that is the revenue before costs. "
  "Every cut-off, every pit shell, every feasibility study flows from this multiplication.",
  "Tonnage comes from volume times density; grade from assays; contained metal is their product. "
  "Recoverable metal multiplies by metallurgical recovery, and revenue multiplies by price. "
  "Units must stay consistent - percent to fraction, tonnes to the same tonnes - or the math lies.",
  ["Contained metal = tonnage × grade: the founding multiplication.",
   "Recoverable metal = contained × recovery.",
   "Revenue = recoverable × price, before costs.",
   "Consistent units or the math lies."],
  ["Tonnage from surveyed volumes and measured density.",
   "Grades from QA/QC-passed assays.",
   "Recovery and price inputs documented."],
  ["Resource numbers reported per JORC or NI 43-101.",
   "Metal content never overstated by mixing units.",
   "Cut-off applied before tonnage is called ore."],
  ["Mineral resource estimation texts (public publications).",
   "JORC Code (public code)."],
  "metal", {"tonnes": 8000000.0, "grade_pct": 1.5}),
]

PUB += [
R("Resource Estimation", "Compounded", 13,
  "Resource estimation turns drill holes into a quantified ore body: tonnes and grade in three dimensions, classified by confidence as measured, indicated, or inferred. "
  "It is part statistics, part geology - the numbers must honor the rocks, not just the math. "
  "The estimate underwrites every dollar spent afterward, so its honesty is the project's foundation.",
  "Assay data is composited to consistent lengths, top-cut for outliers, and interpolated into blocks by kriging or inverse-distance methods within geological domains. "
  "Classification follows drill spacing and geological confidence; the competent person signs off under JORC or NI 43-101. "
  "Reconciliation - model versus actual production - judges the estimate forever after.",
  ["Tonnes and grade in 3D, classified by confidence.",
   "Statistics must honor geology: domains first, math second.",
   "The competent person signs; the code governs.",
   "Reconciliation judges the estimate against reality."],
  ["A validated drill-hole database.",
   "Geological domains interpreted in 3D.",
   "Estimation software and a competent person."],
  ["Reporting per JORC or NI 43-101, no exceptions.",
   "Top-cuts and classification documented and justified.",
   "Reconciliation tracked from first production."],
  ["JORC Code (public code).",
   "NI 43-101 Standards of Disclosure (public instrument)."],
  "metal", {"tonnes": 25000000.0, "grade_pct": 0.9}),

R("JORC and NI 43-101 Reporting", "Compounded", 14,
  "JORC and NI 43-101 are the codes that keep resource reporting honest: Australia's JORC Code and Canada's National Instrument 43-101 set the rules for telling investors what is in the ground. "
  "Both demand a competent or qualified person, transparent methods, and no misleading optimism. "
  "A resource number without a code behind it is just a rumor.",
  "Exploration results, mineral resources, and ore reserves are reported with the data, methods, and assumptions that support them. "
  "Resources classify by geological confidence; reserves - the economically mineable part - need modifying factors: mining, processing, economic, legal, environmental, social. "
  "The competent person takes personal professional responsibility for the report.",
  ["Codes keep resource reporting honest for investors.",
   "Competent person, transparent methods, no misleading optimism.",
   "Resources: geological confidence. Reserves: plus economic mineability.",
   "A number without a code is a rumor."],
  ["A competent/qualified person for the deposit type.",
   "Documented data, methods, and assumptions.",
   "Modifying-factor studies for reserve conversion."],
  ["Material assumptions disclosed, not buried.",
   "Forward-looking statements qualified appropriately.",
   "No selective reporting of high-grade intervals alone."],
  ["JORC Code 2012 edition (public code).",
   "NI 43-101 and Form 43-101F1 (public instrument)."],
  "cutoff", {"cost_per_t_ore": 35.0, "price_per_t_metal": 8500.0, "recovery": 0.90}),

R("Pit Optimization", "Compounded", 15,
  "Pit optimization finds the pit shape that maximizes value: which blocks to mine and which to leave, given prices, costs, and wall angles. "
  "The Lerchs-Grossmann algorithm - the industry standard - tests millions of block combinations to find the most profitable shell. "
  "The optimized shell becomes the ultimate pit; pushbacks sequence the mining toward it.",
  "Each block gets a value: revenue from its metal minus mining, processing, and selling costs. "
  "The algorithm finds the closed set of blocks with maximum total value respecting slope constraints. "
  "Nested shells at varying prices show sensitivity, and the chosen shell balances value against risk and mine life.",
  ["The most profitable pit shell, found by optimization.",
   "Lerchs-Grossmann: the industry-standard algorithm.",
   "Each block valued: revenue minus all costs.",
   "Nested shells reveal price sensitivity."],
  ["A block model with values per block.",
   "Geotechnical slope angles by sector.",
   "Price and cost forecasts documented."],
  ["Optimization inputs disclosed for reserve work.",
   "Geotechnical constraints honored, not relaxed for value.",
   "Shells re-run when prices or costs move materially."],
  ["Pit optimization literature (Lerchs-Grossmann) (public publications).",
   "SME open-pit planning references (public publications)."],
  "stripratio", {"waste": 80000000.0, "ore": 20000000.0}),

R("Cut-Off Grade", "Compounded", 16,
  "Cut-off grade is the grade below which rock is waste and above which it is ore - the economic boundary of the mine. "
  "It moves with price, cost, and capacity: high prices lower the cut-off and grow the reserve; high costs raise it and shrink it. "
  "Getting it right maximizes value; getting it wrong buries profit in the waste dump.",
  "The breakeven cut-off divides the cost of mining, processing, and selling a tonne by the recoverable value per tonne of metal. "
  "Operational cut-offs refine it for capacity constraints - mill-limited mines use a higher cut-off to feed the best ore first. "
  "Grade control in the pit applies the cut-off daily, directing trucks to ore, low-grade stockpile, or waste.",
  ["The economic boundary between ore and waste.",
   "Breakeven: cost per tonne over recoverable value per tonne of metal.",
   "Moves with price, cost, and capacity.",
   "Grade control applies it daily in the pit."],
  ["Accurate mining, processing, and selling costs.",
   "Price forecasts and recovery data.",
   "Grade-control sampling in the pit."],
  ["Cut-off documented with its inputs.",
   "Stockpiled low-grade accounted honestly.",
   "No ore sent to waste by careless digging."],
  ["Cut-off grade theory literature (Lane) (public publications).",
   "JORC Code on reserve modifying factors (public code)."],
  "cutoff", {"cost_per_t_ore": 42.0, "price_per_t_metal": 9200.0, "recovery": 0.88}),

R("Crushing and Grinding", "Compounded", 17,
  "Crushing and grinding liberate the valuable minerals from waste rock by breaking it ever finer - the most energy-hungry step in mineral processing. "
  "Crushers take run-of-mine rock to centimeters; grinding mills take it to the microns where minerals separate. "
  "Grind too coarse and minerals stay locked; too fine and energy is wasted.",
  "Primary crushers break the blasted rock, secondary and tertiary stages reduce it further, and rod or ball mills grind with steel media to liberation size. "
  "Classification by screens and cyclones returns oversize for another pass; mill power draw and throughput are the control variables. "
  "Liner and media wear are the consumable costs watched per tonne.",
  ["Liberation by breaking: crushers to centimeters, mills to microns.",
   "The most energy-hungry step in processing.",
   "Too coarse locks minerals; too fine wastes energy.",
   "Classification recycles oversize for another pass."],
  ["Crushers, mills, screens, and cyclones sized to throughput.",
   "Power supply for the grinding load.",
   "Wear monitoring: liners and media."],
  ["Dust controlled at crushing and transfer points.",
   "Noise managed for workers and neighbors.",
   "Locked-rotor and tramp-metal protection on crushers."],
  ["Mineral processing texts (public publications).",
   "Machinery safety regulations (public regulations)."],
  "grind", {"feed_tph": 1200.0, "hours": 22.0}),

R("Flotation Separation", "Compounded", 18,
  "Flotation separates minerals by making the valuable ones hydrophobic so they attach to air bubbles and float, while waste sinks. "
  "Reagents - collectors, frothers, depressants - tune the chemistry so the right minerals float. "
  "It is the workhorse of base-metal processing, recovering minerals too fine for gravity separation.",
  "Ground slurry enters cells where impellers or air create bubbles; collectors coat the target mineral, which rides bubbles to the froth, skimmed as concentrate. "
  "Rougher, scavenger, and cleaner stages progressively upgrade the concentrate; depressants hold back the unwanted minerals. "
  "Grade and recovery trade off: pushing grade loses recovery, chasing recovery dilutes grade.",
  ["Valuable minerals made to float; waste made to sink.",
   "Reagents tune the chemistry: collectors, frothers, depressants.",
   "Stages upgrade progressively: rougher, scavenger, cleaner.",
   "Grade versus recovery: the eternal trade-off."],
  ["Flotation cells with air and reagent dosing.",
   "Reagent storage and handling per chemical safety.",
   "Online grade analysis for control."],
  ["Reagent handling per chemical safety rules.",
   "Tailings from flotation managed per the tailings standard.",
   "Water recycled to the extent practical."],
  ["Flotation chemistry literature (public publications).",
   "Chemical handling regulations (public regulations)."],
  "recovery", {"feed_metal": 950.0, "recovered_metal": 864.5}),

R("Leaching — Heap and Tank", "Compounded", 19,
  "Leaching dissolves the valuable metal out of ore with chemicals: heaps leach low-grade ore under sprinklers for months; tanks leach higher-grade material with agitation in hours. "
  "Cyanide for gold, acid for copper - the chemistry matched to the metal. "
  "It recovers metal from rock too poor to smelt, but demands rigorous containment.",
  "Crushed ore is stacked on lined pads and irrigated with lixiviant; pregnant solution drains to collection and metal recovery by carbon or SX-EW. "
  "Tank leaching agitates finer feed for faster, higher recovery at higher cost. "
  "Pads, ponds, and pipes are double-contained and monitored, because a leak is an environmental event.",
  ["Chemistry dissolves metal from low-grade ore.",
   "Heap: months under sprinklers. Tank: hours with agitation.",
   "Lixiviant matched to metal: cyanide, acid, and others.",
   "Containment is the license to operate."],
  ["Lined pads or tanks, solution collection, recovery plant.",
   "Reagent supply and trained operators.",
   "Monitoring wells around the facility."],
  ["Double containment for all process solutions.",
   "Cyanide managed per the cyanide code.",
   "Closure plans detoxify heaps at end of life."],
  ["International Cyanide Management Code (public code).",
   "Heap-leach design literature (public publications)."],
  "recovery", {"feed_metal": 620.0, "recovered_metal": 558.0}),

R("Smelting and Refining", "Compounded", 20,
  "Smelting melts concentrates at high temperature to separate metal from the remaining waste; refining purifies the metal to market grade. "
  "Furnaces, converters, and electrolytic refineries turn mineral concentrates into 99.99% copper cathodes or gold doré. "
  "It is energy-intensive and emissions-controlled - the industry's heaviest industrial chemistry.",
  "Concentrate is dried, smelted with fluxes to form matte and slag, converted to blister, and fire- or electro-refined to purity. "
  "Off-gases are captured - sulfur becomes acid, dust is filtered - because modern smelters answer for every emission. "
  "Metal accounting tracks every kilogram from concentrate to cathode.",
  ["Heat separates metal from waste; refining purifies to market grade.",
   "Furnace to converter to electrolytic refinery.",
   "Off-gas captured: sulfur to acid, dust filtered.",
   "Metal accounting tracks every kilogram."],
  ["Smelter and refinery capacity matched to concentrate supply.",
   "Gas cleaning: acid plant, baghouses, scrubbers.",
   "Slag handling and disposal or sale."],
  ["Emissions within permitted limits, continuously monitored.",
   "Slag and residues tested before disposal.",
   "Worker protection from heat, fumes, and molten metal."],
  ["Extractive metallurgy texts (public publications).",
   "Air-emission permits and regulations (public regulations)."],
  "recovery", {"feed_metal": 1100.0, "recovered_metal": 1078.0}),

R("Tailings Management", "Compounded", 21,
  "Tailings are the finely ground waste left after the valuable minerals are removed - and their storage dams are mining's greatest catastrophic risk. "
  "The Global Industry Standard on Tailings Management, born from dam failures, demands engineered safety, independent review, and zero tolerance for complacency. "
  "A tailings dam must stand forever, long after the mine closes.",
  "Thickened or filtered tailings reduce water in storage; dams are raised by engineered methods - never upstream without rigorous control - with drainage, monitoring, and emergency plans. "
  "Independent review boards challenge the design; instrumentation watches pore pressure and movement continuously. "
  "Closure designs the landform for the long term: stable, non-polluting, and walkaway-safe.",
  ["Tailings dams are mining's greatest catastrophic risk.",
   "The Global Standard demands engineered safety and independent review.",
   "Thickening and filtering reduce the hazard.",
   "The dam must stand forever - design for closure from day one."],
  ["Tailings facility engineered by qualified designers.",
   "Independent review board for the facility's life.",
   "Instrumentation: pore pressure, deformation, water levels."],
  ["Conformance with the Global Industry Standard on Tailings Management.",
   "Emergency preparedness with downstream communities.",
   "No upstream raising without rigorous engineering control."],
  ["Global Industry Standard on Tailings Management (public standard).",
   "ICMM tailings guidance (public guidance)."],
  "water", {"flow_lps": 120.0}),

R("Mine Water Management", "Compounded", 22,
  "Mine water management handles every drop: dewatering the pit or underground workings, supplying the plant, and treating discharge to protect rivers. "
  "Water is both essential and dangerous - too little stops the plant, too much floods the pit, and dirty discharge poisons trust. "
  "The water balance - every inflow and outflow accounted - is the controlling document.",
  "Pits are dewatered by wells and sumps; underground mines pump from sumps; the plant recycles process water aggressively. "
  "Contact water is collected and treated - for acidity, metals, and sediment - before release under permit limits. "
  "Monitoring wells and stream gauges prove the mine's water story to regulators and neighbors.",
  ["Every drop accounted: the water balance controls all.",
   "Dewater the workings, supply the plant, treat the discharge.",
   "Recycle aggressively; release only to permit.",
   "Monitoring proves the story to neighbors and regulators."],
  ["Dewatering wells, pumps, and sumps sized to inflows.",
   "A water-treatment plant for contact water.",
   "Monitoring wells and gauges around the site."],
  ["Discharge within permit limits, continuously verified.",
   "Groundwater users protected from drawdown harm.",
   "Extreme rainfall planned for, not wished away."],
  ["Mine water management literature (public publications).",
   "Water discharge permits and regulations (public regulations)."],
  "water", {"flow_lps": 85.0}),

R("Geotechnical Engineering", "Compounded", 23,
  "Geotechnical engineering keeps the ground standing: pit walls at safe angles, underground openings supported, waste dumps stable. "
  "Rock is the mine's building material and its greatest uncertainty - the geotechnical engineer's job is to design for what the rock will actually do. "
  "Monitoring closes the loop between design and reality.",
  "Rock mass is characterized by mapping, core logging, and testing; slopes and openings are designed to target safety factors. "
  "Support - bolts, mesh, shotcrete, cables - is installed to the design; prisms, radar, and extensometers watch for movement. "
  "Trigger-action response plans define exactly what happens when movement accelerates.",
  ["Design for what the rock will actually do.",
   "Characterize, design to safety factors, support, monitor.",
   "Monitoring closes the loop between design and reality.",
   "Trigger-action plans define the response to movement."],
  ["Geotechnical drilling, logging, and lab testing.",
   "Design engineers and monitoring instruments.",
   "Ground-support installation capability."],
  ["Slopes and openings within designed safety factors.",
   "Monitoring data reviewed on schedule, alarms acted on.",
   "No work under unsupported ground."],
  ["Geotechnical design literature for mining (public publications).",
   "Ground-control management plan regulations (public regulations)."],
  "stripratio", {"waste": 12000000.0, "ore": 4000000.0}),
]

PUB += [
R("Strip Ratio Economics", "Advanced", 24,
  "Strip ratio - waste tonnes per ore tonne - is the open pit's economic pulse: low ratios mean cheap ore, rising ratios mean the pit is eating its profit. "
  "The overall strip ratio decides the pit's fate; the incremental ratio decides each pushback. "
  "Mining continues while the value of the ore exposed exceeds the cost of the waste stripped to reach it.",
  "Planners track the ratio by pushback: early low-ratio phases fund the later high-ratio ones. "
  "The economic limit arrives when the incremental strip ratio's cost exceeds the ore's margin - the pit stops there. "
  "Waste-dump capacity, haul distances, and equipment sizing all scale with the ratio.",
  ["Waste:ore ratio is the pit's economic pulse.",
   "Overall ratio judges the pit; incremental judges each pushback.",
   "Low early ratios fund later high-ratio phases.",
   "Mining stops where stripping cost exceeds ore margin."],
  ["Block-model strip ratios by pushback.",
   "Waste-dump capacity for the planned stripping.",
   "Haul fleet sized to total material movement."],
  ["Pushback economics re-proven as prices move.",
   "Dump stability engineered for the planned volumes.",
   "No high-grading that strands later phases."],
  ["Open-pit economics literature (public publications).",
   "SME mine planning references (public publications)."],
  "stripratio", {"waste": 95000000.0, "ore": 22000000.0}),

R("Mineral Economics and Commodity Markets", "Advanced", 25,
  "Mineral economics studies how metal prices are set and what they mean for mines: supply, demand, inventories, and speculation moving prices on global exchanges. "
  "Copper, gold, iron ore - each has its market structure, its benchmark price, and its cycle. "
  "Mines live and die by the cycle: the art is surviving the troughs to harvest the peaks.",
  "Prices form on exchanges (LME, COMEX, SHFE) from the balance of mine supply, scrap, demand, and inventory; contracts reference benchmarks plus premiums. "
  "Feasibility studies test economics across price scenarios; hedging locks prices for a portion of production. "
  "Royalties and taxes take the state's share, and their design decides whether investment comes.",
  ["Prices set by supply, demand, inventories, and speculation on exchanges.",
   "Each metal its market structure, benchmark, and cycle.",
   "Survive the troughs to harvest the peaks.",
   "Hedging locks prices; royalties shape investment."],
  ["Price forecasts across scenarios, not single points.",
   "Hedging policy approved at board level.",
   "Market intelligence on supply and demand."],
  ["Price assumptions disclosed in feasibility work.",
   "Hedging within the approved policy.",
   "Royalty and tax compliance in every jurisdiction."],
  ["Mineral economics literature (public publications).",
   "Exchange rulebooks: LME, COMEX (public rules)."],
  "npv", {"capex": 450000000.0, "annual_cf": 95000000.0, "years": 12, "rate": 0.08}),

R("Mine Planning Software and Scheduling", "Advanced", 26,
  "Mine planning software turns the block model into a scheduled reality: which blocks, in which periods, feeding the plant at the right grade and tonnage. "
  "Scheduling maximizes net present value while respecting mining rates, plant capacity, and blending needs. "
  "A schedule is a promise to the plant, the market, and the financiers.",
  "Optimizers sequence pushbacks and schedule blocks to maximize NPV under constraints; engineers turn the schedule into practical designs with ramps and phases. "
  "Short-term plans - weekly, monthly - direct the fleet day by day; reconciliation compares planned to actual. "
  "The schedule is re-run as prices, costs, and knowledge change, because a stale schedule is a broken promise.",
  ["Block model to scheduled reality: the software's job.",
   "Maximize NPV under mining, plant, and blending constraints.",
   "Long-term strategy, short-term direction, reconciliation between.",
   "Re-run as the world changes."],
  ["Planning software and trained mine planners.",
   "A current block model and cost inputs.",
   "Survey and production data for reconciliation."],
  ["Schedules within geotechnical and environmental limits.",
   "Reserve schedules backed by feasibility-level inputs.",
   "Reconciliation reported honestly."],
  ["Mine scheduling literature (public publications).",
   "JORC Code on reserve scheduling inputs (public code)."],
  "haul", {"trucks": 32, "payload_t": 290.0, "trips_per_day": 16.0}),

R("Ground Control", "Advanced", 27,
  "Ground control is the underground mine's safety science: designing openings the rock can hold and supporting them so they do. "
  "Rock bursts, falls of ground, and squeezing ground each demand their answer. "
  "The ground control management plan is the underground mine's constitution - every excavation obeys it.",
  "Rock mass rating systems classify the ground; empirical and numerical design set spans and support. "
  "Bolts, mesh, shotcrete, and cable bolts are installed to the plan and inspected; instrumentation watches for the ground's complaints. "
  "Seismic monitoring listens for the rock's stress, and re-entry rules after blasting protect against the burst.",
  ["Design openings the rock can hold; support them so they do.",
   "The ground control plan is the mine's constitution.",
   "Instrumentation hears the ground's complaints.",
   "Re-entry rules protect against the burst."],
  ["Geotechnical engineers and the ground control plan.",
   "Support installation: bolting rigs, shotcrete.",
   "Monitoring: extensometers, seismic, visual inspection."],
  ["No excavation outside the plan's design.",
   "Support quality verified, not assumed.",
   "Seismic and rockburst protocols enforced."],
  ["Ground-control management plan regulations (public regulations).",
   "Rock mechanics literature (public publications)."],
  "drill", {"holes": 120, "avg_depth_m": 18.0}),

R("Mine Automation", "Advanced", 28,
  "Mine automation removes people from the most dangerous tasks: autonomous haul trucks, tele-remote loaders, and automated drills run from control rooms. "
  "It improves safety and consistency - and demands new skills, new systems, and honest engagement with the workforce it changes. "
  "Automation is a transformation, not just equipment.",
  "Trucks navigate by GPS and lidar on defined routes; loaders are tele-operated from the surface; drills execute programmed patterns. "
  "A control room supervises the fleet; the network - often private LTE - is the automation's nervous system. "
  "Change management retrains operators as controllers and maintainers of the new systems.",
  ["People removed from the most dangerous tasks.",
   "Autonomous haulage, tele-remote loading, automated drilling.",
   "The network is automation's nervous system.",
   "A transformation, not just equipment."],
  ["Automation-ready fleet and private communications.",
   "A control room with trained controllers.",
   "Cybersecurity for the operational technology."],
  ["Safety case for autonomous operation, proven.",
   "Workforce transition planned with workers, not around them.",
   "Manual fallback when automation fails."],
  ["Mine automation industry literature (public publications).",
   "Functional safety standards for autonomous machines (public standards)."],
  "haul", {"trucks": 40, "payload_t": 320.0, "trips_per_day": 20.0}),

R("Processing Plant Operations", "Advanced", 29,
  "Processing plant operations turn run-of-mine ore into saleable concentrate or metal, day and night, at the designed recovery and throughput. "
  "The plant is a chemical factory with rock for feedstock: crushing, grinding, separation, and dewatering in continuous flow. "
  "Availability - the fraction of time the plant runs - is the metric that matters most.",
  "Ore feeds the crushing-grinding circuit, then separation - flotation, leaching, gravity - then thickening, filtration, and concentrate handling. "
  "Operators control grind size, reagent doses, and densities against targets; maintenance keeps crushers, mills, and pumps available. "
  "Metallurgical accounting reconciles feed, product, and tailings, proving the recovery claimed.",
  ["Ore in, concentrate or metal out, day and night.",
   "Availability is the metric that matters most.",
   "Control the grind, the chemistry, and the densities.",
   "Accounting proves the recovery claimed."],
  ["The full circuit: crush, grind, separate, dewater.",
   "Operators and metallurgists around the clock.",
   "Maintenance planned to protect availability."],
  ["Reagents and process chemicals handled safely.",
   "Dust, noise, and effluent within permits.",
   "Tailings to the managed facility, never elsewhere."],
  ["Mineral processing plant operations literature (public publications).",
   "Process safety and environmental permits (public regulations)."],
  "grind", {"feed_tph": 2500.0, "hours": 21.5}),

R("Environmental Management", "Advanced", 30,
  "Environmental management keeps the mine's footprint within its permitted bounds: air, water, land, and biodiversity protected by design and verified by monitoring. "
  "The social license to operate is earned daily - one tailings failure or poisoned stream can end a company. "
  "Progressive reclamation heals the land as mining advances, not decades later.",
  "Baselines are measured before mining; management plans cover water, air, waste, biodiversity, and heritage. "
  "Monitoring - water quality, dust, noise, wildlife - proves compliance; exceedances trigger corrective action. "
  "Progressive reclamation reshapes and revegetates finished areas while the mine still operates.",
  ["The footprint within permitted bounds, verified by monitoring.",
   "Social license earned daily.",
   "Progressive reclamation heals as mining advances.",
   "One failure can end a company."],
  ["Environmental staff and the management plans.",
   "Monitoring networks: water, air, biodiversity.",
   "Reclamation equipment and growing media."],
  ["Permits obeyed; exceedances corrected and reported.",
   "Biodiversity offsets where required.",
   "Community grievances heard and answered."],
  ["ICMM environmental principles (public guidance).",
   "Environmental impact assessment and permit regulations (public regulations)."],
  "water", {"flow_lps": 200.0}),

R("Mine Closure and Reclamation", "Advanced", 31,
  "Mine closure returns the site to a stable, safe, productive post-mining use: pits made safe, tailings secured forever, water treated as long as needed, land revegetated. "
  "Closure is planned before mining starts and funded through financial assurance - the money set aside so the land is healed even if the company fails. "
  "A closed mine should need no apology.",
  "Progressive reclamation works through the mine's life; at closure, infrastructure is removed or repurposed, pits secured, dumps shaped and covered, and water treatment continues as long as required. "
  "Financial assurance - bonds, trusts, or letters of credit - is sized to the closure cost and reviewed regularly. "
  "Post-closure monitoring proves the landform holds, for decades where needed.",
  ["Closure planned before mining starts, funded by assurance.",
   "Stable, safe, productive post-mining land use.",
   "Water treated as long as needed - decades if required.",
   "A closed mine needing no apology."],
  ["A closure plan with costed designs.",
   "Financial assurance sized and reviewed.",
   "Post-closure monitoring capability."],
  ["Assurance adequate and bankruptcy-remote.",
   "Closure criteria agreed with regulators and communities.",
   "Long-term water obligations funded, not wished away."],
  ["ICMM mine closure guidance (public guidance).",
   "Financial assurance regulations (public regulations)."],
  "npv", {"capex": 120000000.0, "annual_cf": -8000000.0, "years": 20, "rate": 0.05}),

R("Surveying in Mining", "Advanced", 32,
  "Mine surveying measures the mine: volumes moved, grades staked, tunnels guided, stockpiles quantified. "
  "Every tonne paid for, every blast laid out, every tunnel driven straight depends on the surveyor's instruments. "
  "Modern mines survey by drone, laser scanner, and GPS as well as total station.",
  "Surveyors set out drill patterns, blast boundaries, and construction; they pick up mined volumes for reconciliation and contractor payment. "
  "Underground, gyro-theodolites carry bearing through shafts; laser scanners map stopes in minutes. "
  "Drones map pits and dumps weekly, turning imagery into volumes and plans.",
  ["Every tonne paid for depends on the survey.",
   "Set out, pick up, reconcile: the surveyor's cycle.",
   "Drones, scanners, GPS alongside the total station.",
   "Underground bearing carried by gyro through shafts."],
  ["Survey instruments: total stations, GPS, drones, scanners.",
   "Trained surveyors, surface and underground.",
   "A mine coordinate system, rigorously maintained."],
  ["Volumes for payment verified independently.",
   "Blast exclusion zones surveyed before firing.",
   "Survey control protected from mining damage."],
  ["Mine surveying professional standards (public standards).",
   "Drone operation regulations (public regulations)."],
  "drill", {"holes": 200, "avg_depth_m": 12.0}),

R("Metallurgical Accounting", "Advanced", 33,
  "Metallurgical accounting tracks every kilogram of metal from the mine through the plant to the product: feed, concentrate, tailings, and recovery reconciled. "
  "It is the plant's financial truth - what came in, what went out, what was lost, and whether the numbers balance. "
  "Without it, recovery claims are wishes and metal can walk out unnoticed.",
  "Mass balances close around each unit: two of feed, product, and tailings measured, the third by difference, all checked against the overall. "
  "Sampling and assay errors are quantified; metal prices value the streams; the monthly account is signed off. "
  "Discrepancies trigger investigation, because an unbalanced account hides either error or theft.",
  ["Every kilogram tracked: feed, product, tailings, recovery.",
   "Mass balances close around each unit.",
   "The plant's financial truth.",
   "Discrepancies investigated: error or theft."],
  ["Weighing, sampling, and assaying at balance points.",
   "A metallurgical accountant independent of operations.",
   "Reconciliation software and procedures."],
  ["Balances closed on schedule and signed off.",
   "Measurement errors quantified, not ignored.",
   "Concentrate sales settled against the account."],
  ["Metallurgical accounting best-practice literature (public publications).",
   "AMIRA P754 metal accounting code (public code)."],
  "recovery", {"feed_metal": 1400.0, "recovered_metal": 1288.0}),

R("Mining Mastery Review — Running the Whole Operation", "Advanced", 34,
  "The mastery review binds the ladder into one operating picture: the mine as a single organism where geology, engineering, processing, and stewardship move together. "
  "Each earlier record was a discipline; this record is the mine manager's mind, reading the whole operation. "
  "A master balances production, safety, cost, and closure - none sacrificed for the others.",
  "Start from the ore body and work outward: the resource honestly estimated, the pit or stopes planned for value, the rock broken and moved safely, the plant recovering its metal, the water and land guarded, the closure funded. "
  "Run the daily rhythm - production, safety, grade control - and the long rhythm - planning, permitting, reclamation. "
  "Measure what matters: safety, tonnes and grade, recovery, cost per tonne, and closure progress, and let every decision move at least one.",
  ["The mine as one organism: geology, engineering, processing, stewardship.",
   "Work outward from the ore body to every decision.",
   "Balance production, safety, cost, and closure.",
   "Run the daily rhythm and the long rhythm."],
  ["Fluency in every record of this database, foundations through advanced.",
   "An operation that never sleeps on safety.",
   "Honest metrics reviewed together."],
  ["Safety never traded for production.",
   "Resources reported honestly under the codes.",
   "Closure funded and progressing."],
  ["SME Mining Engineering Handbook (public reference).",
   "ICMM principles for sustainable mining (public guidance)."],
  "metal", {"tonnes": 30000000.0, "grade_pct": 1.1}),
]

GEN_DEMOFN = """function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\\n"
   + "# Metal-content structural sample calculator (mining industries)\\n"
   + "t, g = 1000000.0, 1.2\\n"
   + "metal = t*g/100.0\\n"
   + "print('sample tonnes:', t)\\n"
   + "print('sample grade %:', g)\\n"
   + "print('sample contained metal t:', round(metal,1))\\n"
   + "assert metal > 0\\n"
   + "print('OK: structural sample demo ran')\\n";
}
"""


SIG = [
R("The Delving Art — The Signature View", "Foundations", 1,
  "The Signature view sees mining as the delving art: humanity's ancient bargain with the earth - take what is needed, honor what is taken, and heal the ground afterward. "
  "The geology, the machines, and the chemistry are the same as the public edition's; the difference is the covenant - no tonne unwitnessed, no worker unguarded, no land unhealed. "
  "This edition reframes the full ladder as Signature science, labeled Signature-made throughout.",
  "Where the public edition teaches the mechanics, the Signature edition teaches the keeping: exploration as questioning, extraction as accounting, closure as healing. "
  "Each record pairs the operational truth with its Signature seal - the practice that makes the delving worthy of the earth it opens. "
  "Nothing here is presented as public record; it is his original method.",
  ["Mining the delving art: take, honor, heal.",
   "Every subsystem carries a Signature seal - the discipline beneath the mechanics.",
   "No tonne unwitnessed, no worker unguarded, no land unhealed.",
   "Signature-made throughout: an original method, never public record."],
  ["Willingness to hold safety, honesty, and healing as sworn.",
   "The public edition alongside for the mechanics.",
   "A mine or project where the method can be practiced."],
  ["No Signature claim presented as public or official record.",
   "Worker safety above every production pressure.",
   "The method taught as his original system, plainly labeled."],
  ["The public edition of this database, for the mechanics (this system).",
   "Signature system governance on original works (this system)."],
  "metal", {"tonnes": 5000000.0, "grade_pct": 1.2}),

R("The Earth's Ledger — Signature Minerals and Grades", "Foundations", 2,
  "The Signature method reads minerals as the earth's ledger: each substance its entry, each ore body its account, grade the measure of richness. "
  "The cut-off is the ledger's ruling line - above it ore, below it waste - drawn by honest economics, not by wish. "
  "To call waste ore is to cook the books; the method keeps clean accounts.",
  "Core is logged and assayed under quality control; grade shells are drawn in three dimensions; tonnage times grade gives the contained metal. "
  "The cut-off is set where revenue covers the cost of mining and processing - and re-set when prices move. "
  "The same rock judged again when the market turns: the ledger is living.",
  ["Minerals the earth's ledger; grade its measure.",
   "The cut-off the ruling line, drawn by honest economics.",
   "Clean accounts: no waste called ore.",
   "The ledger living: re-judged when prices move."],
  ["Logging, assay, and QA/QC discipline.",
   "A 3D model of the grade's truth.",
   "Cost and price inputs for the ruling line."],
  ["Assays by proven methods with controls.",
   "Reporting per the codes.",
   "Grade control honoring the line daily."],
  ["JORC Code (public code).",
   "The public edition minerals record, for the mechanics (this system)."],
  "metal", {"tonnes": 12000000.0, "grade_pct": 0.8}),

R("Reading the Ground — Signature Mapping", "Foundations", 3,
  "The Signature method reads the ground before it spends: boots, hammer, and notebook first - the cheapest wisdom in exploration. "
  "Outcrops are the earth's sentences, structures its grammar, alteration its emphasis; the mapper who reads well aims the drills truly. "
  "A good map is thrift; a poor map is waste wearing boots.",
  "The ground is walked and its outcrops recorded, orientations measured, samples gathered. "
  "Geophysics peers beneath the cover; all compiles into maps and sections. "
  "Where structure, alteration, and chemistry speak together, the target is named - and the drill will judge.",
  ["Read before spending: the cheapest wisdom.",
   "Outcrops sentences, structures grammar, alteration emphasis.",
   "A good map thrift; a poor map waste.",
   "The drill the final judge of every reading."],
  ["Ground access and trained readers.",
   "Base maps and prior knowledge.",
   "A database for the observations."],
  ["Permissions and heritage surveys before disturbance.",
   "Data systematic, never scattered.",
   "Targets named, then tested."],
  ["Geological survey mapping standards (public standards).",
   "The public edition mapping record, for the mechanics (this system)."],
  "stripratio", {"waste": 3000000.0, "ore": 1000000.0}),

R("The Questioning Holes — Signature Drilling", "Foundations", 4,
  "The Signature method drills as questioning: each hole a question put to the earth, the core its answer, the assay its sworn testimony. "
  "Wide questions first, then closer ones as confidence grows - and the drill's answer is final, whether it crowns or kills the idea. "
  "Drilling is the dearest question; the method asks it only where the reading warrants.",
  "Targets are drilled in patterns; core is logged for rock and structure, split, and half sent to the assay house. "
  "Downhole surveys keep the question's path true. "
  "Results extend the target, reshape it, or end it - the earth answers honestly to honest questions.",
  ["Each hole a question; the core its answer.",
   "Wide questions first, closer ones with confidence.",
   "The drill's answer final, crown or kill.",
   "Ask dearly only where reading warrants."],
  ["Rigs suited to depth and ground.",
   "Loggers and assay turnaround.",
   "Survey tools for true paths."],
  ["Pads healed after the program.",
   "Waters met underground managed.",
   "Rotating steel respected: safety first."],
  ["Drilling safety and environmental guidance (public guidance).",
   "The public edition drilling record, for the mechanics (this system)."],
  "drill", {"holes": 48, "avg_depth_m": 220.0}),

R("Sworn Testimony — Signature Sampling and Assay", "Foundations", 5,
  "The Signature method takes sampling as sworn testimony: the sample must represent the rock truly, the assay must measure truly, and quality control must prove both. "
  "A false witness here corrupts the resource, the plan, and the economics - the whole mine built on a lie. "
  "Blanks, standards, and duplicates stand as the testimony's witnesses.",
  "Samples are taken on defined intervals, crushed, split, and pulped to sameness. "
  "Fire or instruments measure the metals; every batch carries its witnesses, and failing batches are quarantined for re-trial. "
  "The chain of custody runs unbroken from ground to lab.",
  ["Sampling sworn testimony; assay its measure.",
   "False witness corrupts the whole mine.",
   "Blanks, standards, duplicates: the witnesses.",
   "Failing batches quarantined for re-trial."],
  ["Protocols for taking and handling.",
   "An accredited assay house.",
   "Witness materials for every batch."],
  ["Custody unbroken ground to lab.",
   "Failure rates within the accepted bounds.",
   "Methods fit for the reported elements."],
  ["JORC Code QA/QC expectations (public code).",
   "The public edition sampling record, for the mechanics (this system)."],
  "recovery", {"feed_metal": 850.0, "recovered_metal": 782.0}),

R("The Open Bowl — Signature Open Pit", "Foundations", 6,
  "The Signature method opens the pit as a bowl: terraces descending in order, shovels loading, trucks climbing the spiral roads. "
  "The bowl grows for decades, following the ore down, and stops where the stripping's cost outweighs the metal's worth - the economic rim. "
  "Walls are engineered and watched, for the bowl must stand as long as it is worked.",
  "Benches are drilled and blasted; shovels fill the trucks; the trucks climb to crusher or dump. "
  "Wall angles are designed to the rock's truth and monitored by prism, radar, and eye. "
  "Water is led away from the floor, and the ultimate rim is drawn where value still pays for waste.",
  ["The pit a bowl, terraced in order.",
   "Drill, blast, load, haul: the heartbeat.",
   "Walls engineered and watched.",
   "The rim economic: value paying for waste."],
  ["Shovels, trucks, drills to the production's need.",
   "Geotechnical design and watching.",
   "Dewatering for the working floor."],
  ["Walls monitored; movement answered.",
   "Blast effects kept within bounds.",
   "Light and heavy traffic parted."],
  ["SME open-pit literature (public publications).",
   "The public edition open-pit record, for the mechanics (this system)."],
  "stripratio", {"waste": 45000000.0, "ore": 15000000.0}),

R("The Deep Ways — Signature Underground Methods", "Foundations", 7,
  "The Signature method works the deep ways: shafts and declines descending, stopes opened by the rock's own logic, support holding what the earth would reclaim. "
  "Each method - cut-and-fill, stoping, caving, room-and-pillar - answers its ground. "
  "The underground trades dearer tonnes for the surface left whole, and ventilation is its breath.",
  "Access descends by decline or shaft; development opens the ore; stopes are taken in cycles of drill, blast, and muck. "
  "Bolts, mesh, shotcrete, and backfill hold the openings; ventilation breathes fresh air to every face and carries away the blast's breath and the diesel's. "
  "The deep ways are mapped, supported, and breathed - in that order, always.",
  ["The deep ways: descending, opening, supporting, breathing.",
   "Each method answering its ground.",
   "Dearer tonnes for the surface left whole.",
   "Ventilation the breath of the deep."],
  ["Development opening the ore.",
   "Support: bolts, mesh, shotcrete, backfill.",
   "Ventilation for people, machines, and blasting."],
  ["Ground control plans obeyed.",
   "Air measured against the plan.",
   "Refuge and egress maintained."],
  ["Underground methods literature (public publications).",
   "The public edition underground record, for the mechanics (this system)."],
  "cutoff", {"cost_per_t_ore": 28.0, "price_per_t_metal": 9500.0, "recovery": 0.92}),

R("The Breaking Art — Signature Drilling and Blasting", "Foundations", 8,
  "The Signature method breaks rock as an art: holes in pattern, charges weighed, timing sequenced in milliseconds to throw the rock toward freedom in diggable pieces. "
  "Good breaking serves the shovel; bad breaking serves the boulder, the flyrock, and the neighbor's complaint. "
  "And the art is bound by law - explosives respected as the power they are.",
  "The pattern is designed - burden, spacing, depth - and the delays sequenced to the free face. "
  "Holes are drilled true, charged with ANFO or emulsion, stemmed, and tied to detonators. "
  "Fragmentation is judged by the digging; vibration and airblast are measured against their limits.",
  ["Breaking as art: pattern, charge, timing.",
   "Good breaking serves the shovel.",
   "Explosives respected as the power they are.",
   "Vibration and airblast measured, not hoped."],
  ["Drills and explosives supply.",
   "Designs signed by the competent.",
   "Vibration watching."],
  ["Magazines secured per law.",
   "Guards and clearance before every shot.",
   "Misfires by procedure, never improvised."],
  ["Explosives regulations (public regulations).",
   "The public edition blasting record, for the mechanics (this system)."],
  "blast", {"holes": 120, "kg_per_hole": 85.0, "tonnes_broken": 45000.0}),

R("The Endless Caravan — Signature Loading and Hauling", "Foundations", 9,
  "The Signature method runs the endless caravan: shovels filling, trucks climbing, the pit's rock flowing like a river uphill. "
  "It is the costliest visible labor - fuel, rubber, steel - and the fleet master's art is keeping every unit laden and moving. "
  "Roads are built as the caravan's highways: watered, graded, and guarded.",
  "Shovels spot and fill to the rated load - neither starved nor strained; trucks run their engineered roads. "
  "Dispatch balances shovel to truck; road crews water and grade; payload scales weigh every pass. "
  "The caravan's rhythm is the pit's production.",
  ["The endless caravan: shovels filling, trucks climbing.",
   "Every unit laden and moving: the fleet art.",
   "Roads as highways: watered, graded, guarded.",
   "Payloads weighed: neither starved nor strained."],
  ["Shovels and trucks matched to the rate.",
   "Engineered roads with watering and grading.",
   "Dispatch balancing the fleet."],
  ["Traffic parted: light from heavy.",
   "Berms and bunds on the roads.",
   "Operators rested and fit."],
  ["Haul-road design literature (public publications).",
   "The public edition haulage record, for the mechanics (this system)."],
  "haul", {"trucks": 24, "payload_t": 220.0, "trips_per_day": 18.0}),

R("The Breath Below — Signature Ventilation", "Foundations", 10,
  "The Signature method breathes for the deep mine: fresh air driven to every face, foul air - blast fumes, diesel breath, dust, and ground gases - drawn away. "
  "Air is the invisible infrastructure; without it the deep ways are a tomb. "
  "Quantity, quality, and distribution are engineered and watched without ceasing.",
  "Great fans breathe through the airways; regulators and stoppings portion the breath to the faces. "
  "Diesel's hunger sets the volume; gas watchers stand sentinel for the dangerous airs. "
  "Surveys measure every split, for air cheats through the easiest path.",
  ["Breathing for the deep: fresh in, foul out.",
   "The invisible infrastructure; without it, a tomb.",
   "Diesel's hunger setting the volume.",
   "Every split measured against the plan."],
  ["Fans great and small to the mine's need.",
   "Airways, regulators, stoppings kept.",
   "Gas and flow instruments."],
  ["Air per the diesel and personnel law.",
   "Gas alarms with evacuation answers.",
   "Plans renewed as the mine grows."],
  ["Mine ventilation texts (public publications).",
   "The public edition ventilation record, for the mechanics (this system)."],
  "water", {"flow_lps": 45.0}),

R("The Homecoming Vow — Signature Mine Safety", "Foundations", 11,
  "The Signature method's first vow is the homecoming: every worker returns, every shift, whole. "
  "The ground's hazards - falls, machines, explosives, gases, dust - are met with systems, not luck: hazards named per task, controls verified in the field. "
  "And any hand may stop the work when danger shows - the stop-work right is sacred.",
  "Hazards are listed task by task; controls follow the hierarchy - remove, engineer, administer, protect. "
  "Pre-starts, talks, and visible leadership open each day. "
  "Near-misses are told without blame and pursued to root, for the free lesson is the cheapest safety ever bought.",
  ["The homecoming vow: every worker, every shift, whole.",
   "Systems, not luck.",
   "Any hand may stop unsafe work.",
   "Near-misses: free lessons, told without blame."],
  ["A safety system with true authority.",
   "Training and proven competence per role.",
   "Rescue, refuge, and communication."],
  ["Regulations obeyed and audited.",
   "Fitness for work guarded.",
   "Contractors held to the same vow."],
  ["Mine safety regulations (public regulations).",
   "The public edition safety record, for the mechanics (this system)."],
  "recovery", {"feed_metal": 1200.0, "recovered_metal": 1092.0}),

R("The Founding Sum — Signature Mining Math", "Foundations", 12,
  "The Signature method's founding sum: tonnage times grade equals contained metal - the number beneath every plan and valuation. "
  "A million tonnes at one percent is ten thousand tonnes of metal; the price turns it to revenue, recovery to recoverable, cost to profit or loss. "
  "Units kept pure, or the sum lies.",
  "Volume times density gives tonnage; assays give grade; their product the contained metal. "
  "Recovery trims to recoverable; price to revenue. "
  "Percent to fraction, tonnes to tonnes - the keeper watches the units as the mint watches its scales.",
  ["Tonnage × grade = contained metal: the founding sum.",
   "Recovery to recoverable; price to revenue.",
   "Units pure, or the sum lies.",
   "Beneath every plan and valuation."],
  ["Tonnage from surveyed volumes and weighed density.",
   "Grades from witnessed assays.",
   "Recovery and price inputs recorded."],
  ["Reported per the codes.",
   "No mixing of units to flatter.",
   "Cut-off applied before 'ore' is spoken."],
  ["Resource estimation texts (public publications).",
   "The public edition mining-math record, for the mechanics (this system)."],
  "metal", {"tonnes": 8000000.0, "grade_pct": 1.5}),
]

SIG += [
R("Numbering the Hidden — Signature Resource Estimation", "Compounded", 13,
  "The Signature method numbers the hidden ore body with humility: statistics guided by geology, confidence classified honestly, the competent person's name on the page. "
  "Measured, indicated, inferred - each its drill spacing and its geological sureness. "
  "The estimate funds everything after; its honesty is the project's bedrock.",
  "Assays are composited, outliers trimmed with reason, and blocks filled by kriging or inverse distance within the geological domains - domains first, mathematics second. "
  "Classification follows spacing and understanding; the competent person signs under the code. "
  "Production reconciles against the model forever, judging the estimator's honesty.",
  ["Number the hidden with humility.",
   "Domains first, mathematics second.",
   "Confidence classified honestly.",
   "Reconciliation judging forever."],
  ["A validated drill database.",
   "3D geological domains.",
   "Estimation craft and a competent signer."],
  ["Reported per the codes, no exceptions.",
   "Trims and classes documented and defended.",
   "Reconciliation from first ore."],
  ["JORC Code (public code).",
   "NI 43-101 (public instrument)."],
  "metal", {"tonnes": 25000000.0, "grade_pct": 0.9}),

R("The Honest Proclamation — Signature Reporting Codes", "Compounded", 14,
  "The Signature method proclaims resources under the codes: JORC and NI 43-101, the laws against pretty lies told to investors. "
  "Competent persons, open methods, assumptions on the table - no high-grade intervals paraded alone. "
  "A number without its code is rumor; with it, testimony.",
  "Results, resources, and reserves are told with their supporting data and methods. "
  "Resources by geological confidence; reserves by economics proven through the modifying factors - mining, processing, legal, environmental, social. "
  "The competent person stakes their professional name on the page.",
  ["Proclaim under the codes: no pretty lies.",
   "Methods open, assumptions tabled.",
   "Resources by confidence; reserves by proven economics.",
   "The signer staking their name."],
  ["A competent person for the ground.",
   "Data, methods, assumptions documented.",
   "Modifying studies for reserves."],
  ["Material assumptions disclosed.",
   "Forward words properly qualified.",
   "No cherry-picked intervals."],
  ["JORC Code 2012 (public code).",
   "NI 43-101 (public instrument)."],
  "cutoff", {"cost_per_t_ore": 35.0, "price_per_t_metal": 8500.0, "recovery": 0.90}),

R("The Wisest Bowl — Signature Pit Optimization", "Compounded", 15,
  "The Signature method finds the wisest bowl: the pit shell of greatest value, chosen by the Lerchs-Grossmann reckoning among millions of block-fates. "
  "Each block is weighed - metal's revenue against mining, processing, and selling - and the winning set obeys the slope's law. "
  "Nested shells at many prices show how fortune shifts with the market.",
  "Block values are reckoned honestly; the algorithm gathers the richest lawful set. "
  "Pushbacks march toward the ultimate rim in value order. "
  "When prices move, the shells are re-weighed - a stale optimum is a faded map.",
  ["The wisest bowl: greatest value, lawful slopes.",
   "Each block weighed: revenue against all costs.",
   "Pushbacks marching in value order.",
   "Re-weighed when prices move."],
  ["Valued blocks in the model.",
   "Slope law by sector from the rock's truth.",
   "Price and cost foresight recorded."],
  ["Inputs disclosed for reserve work.",
   "Slope law never bent for value.",
   "Shells renewed with the market."],
  ["Pit optimization literature (public publications).",
   "The public edition pit-optimization record, for the mechanics (this system)."],
  "stripratio", {"waste": 80000000.0, "ore": 20000000.0}),

R("The Ruling Line — Signature Cut-Off Grade", "Compounded", 16,
  "The Signature method draws the ruling line where economics commands: above it ore, below it waste - and the line moves with price, cost, and the mill's hunger. "
  "High prices forgive lean rock; high costs condemn it. "
  "The line wrongly drawn buries profit in the dump or starves the mill.",
  "Breakeven divides the tonne's full cost by the metal's recoverable worth; operations sharpen it for the binding constraint - the mill-fed mine favoring richer feed. "
  "Grade control walks the pit daily, sending trucks to ore, stockpile, or waste by the line. "
  "Low-grade stockpiles wait their price, accounted honestly.",
  ["The ruling line where economics commands.",
   "Moving with price, cost, and capacity.",
   "Wrongly drawn, it buries profit or starves the mill.",
   "Walked daily by grade control."],
  ["True costs: mining, processing, selling.",
   "Price foresight and recovery truth.",
   "Grade-control sampling in the pit."],
  ["The line documented with its inputs.",
   "Stockpiles accounted honestly.",
   "No ore lost to waste by careless digging."],
  ["Cut-off theory literature (public publications).",
   "The public edition cut-off record, for the mechanics (this system)."],
  "cutoff", {"cost_per_t_ore": 42.0, "price_per_t_metal": 9200.0, "recovery": 0.88}),

R("The Liberation — Signature Crushing and Grinding", "Compounded", 17,
  "The Signature method liberates the minerals by breaking: crushers to the finger's scale, mills to the hair's - until the valuable grains stand free of the waste. "
  "Grinding devours power like no other step; the method grinds fine enough to free, never finer to waste. "
  "Classification returns the stubborn oversize for another pass.",
  "Primary crushers take the blasted rock; secondary and tertiary chew smaller; mills grind with steel media to liberation. "
  "Screens and cyclones sort the stream, oversize returning. "
  "Power draw and throughput are the watched dials; liners and media the counted costs.",
  ["Liberation by breaking, fine enough to free.",
   "The hungriest step for power: grind wisely.",
   "Classification returning the stubborn.",
   "Wear counted per tonne."],
  ["Crushers, mills, screens, cyclones to the rate.",
   "Power for the grinding hunger.",
   "Wear watched: liners, media."],
  ["Dust tamed at crushers and transfers.",
   "Noise guarded for workers and neighbors.",
   "Tramp metal and locked rotors protected."],
  ["Mineral processing texts (public publications).",
   "The public edition comminution record, for the mechanics (this system)."],
  "grind", {"feed_tph": 1200.0, "hours": 22.0}),

R("The Floating Harvest — Signature Flotation", "Compounded", 18,
  "The Signature method harvests by floating: reagents coaxing the valuable grains to love air, bubbles lifting them to the froth, waste sinking to its tailings fate. "
  "Collectors, frothers, depressants - the chemistry tuned like an instrument. "
  "Stages upgrade the harvest: rougher, scavenger, cleaner - each purer than the last.",
  "Slurry meets bubbles in the cells; the collector-coated grains ride up and are skimmed as concentrate. "
  "Depressants hold the unwanted down. "
  "Grade and recovery are weighed against each other eternally: purity's price is loss, and the method chooses its balance openly.",
  ["Harvest by floating: the valuable loving air.",
   "Chemistry tuned like an instrument.",
   "Stages purifying: rougher, scavenger, cleaner.",
   "Grade against recovery: the eternal weighing."],
  ["Cells with air and reagent hands.",
   "Reagents stored and handled safely.",
   "Grade eyes watching online."],
  ["Chemicals per the safety law.",
   "Tailings to the managed house.",
   "Water used, then used again."],
  ["Flotation chemistry literature (public publications).",
   "The public edition flotation record, for the mechanics (this system)."],
  "recovery", {"feed_metal": 950.0, "recovered_metal": 864.5}),

R("The Dissolving — Signature Leaching", "Compounded", 19,
  "The Signature method dissolves where crushing cannot pay: heaps breathing lixiviant for months, tanks agitating for hours - chemistry coaxing metal from lean rock. "
  "Cyanide for gold, acid for copper, each matched to its metal. "
  "The method's condition is containment: double-walled, monitored, detoxified at the end.",
  "Ore is stacked on lined pads and rained with solution, or agitated in tanks for swifter, dearer recovery. "
  "Pregnant liquor flows to carbon or SX-EW, and the metal is won. "
  "Pads, ponds, and pipes are doubled and watched; closure detoxifies the heaps.",
  ["Dissolving where crushing cannot pay.",
   "Heaps for months, tanks for hours.",
   "Chemistry matched to metal.",
   "Containment the condition of the art."],
  ["Lined pads or tanks, collection, recovery.",
   "Reagents and trained hands.",
   "Watching wells around."],
  ["Solutions doubly contained.",
   "Cyanide per the cyanide code.",
   "Heaps detoxified at closure."],
  ["International Cyanide Management Code (public code).",
   "The public edition leaching record, for the mechanics (this system)."],
  "recovery", {"feed_metal": 620.0, "recovered_metal": 558.0}),

R("The Refining Fire — Signature Smelting", "Compounded", 20,
  "The Signature method passes concentrate through the refining fire: furnaces melting, converters blowing, refineries purifying to the market's four nines. "
  "The heaviest chemistry in the industry, answering for every emission - sulfur caught as acid, dust as filtered truth. "
  "And every kilogram accounted, from concentrate to cathode.",
  "Concentrate is dried and smelted with fluxes; matte and slag part; converters blow to blister; fire and electrolysis refine to purity. "
  "Off-gas is captured and cleaned; slags are tested before their rest. "
  "Metal accounting follows each kilogram home.",
  ["The refining fire: melt, convert, purify.",
   "Four nines the market's demand.",
   "Every emission answered for.",
   "Every kilogram accounted."],
  ["Furnaces and refineries to the concentrate's flow.",
   "Gas cleaning: acid plant, filters, scrubbers.",
   "Slag ways: use or safe rest."],
  ["Emissions within permit, watched always.",
   "Residues tested before disposal.",
   "Workers shielded from heat, fume, and molten."],
  ["Extractive metallurgy texts (public publications).",
   "The public edition smelting record, for the mechanics (this system)."],
  "recovery", {"feed_metal": 1100.0, "recovered_metal": 1078.0}),

R("The Forever Dam — Signature Tailings", "Compounded", 21,
  "The Signature method builds the tailings dam as forever: the ground waste of the whole mine, held behind walls that must outlive the company. "
  "Failures elsewhere wrote the Global Standard in grief; the method obeys it - engineered safety, independent review, instruments watching without sleep. "
  "Thickened and filtered tailings lighten the burden; closure is designed on day one.",
  "Dams rise by engineered ways, drained and monitored; pore pressure and movement are watched continuously. "
  "Review boards of independents challenge every design; emergency plans reach the downstream people. "
  "The closed landform is shaped for the long peace: stable, clean, walkaway-safe.",
  ["The dam as forever: outliving the company.",
   "The Standard written in grief, obeyed in diligence.",
   "Independent eyes on every design.",
   "Closure designed on day one."],
  ["Engineered dams by qualified hands.",
   "Independent review for the dam's life.",
   "Instruments: pressure, movement, water."],
  ["The Global Standard obeyed fully.",
   "Downstream people warned and planned.",
   "No upstream rising without rigorous proof."],
  ["Global Industry Standard on Tailings Management (public standard).",
   "The public edition tailings record, for the mechanics (this system)."],
  "water", {"flow_lps": 120.0}),

R("The Counted Waters — Signature Mine Water", "Compounded", 22,
  "The Signature method counts every water: dewatering the workings, feeding the plant, treating the discharge - the water balance the controlling scripture. "
  "Too little starves the plant; too much drowns the pit; dirty release poisons the neighbor's trust. "
  "Recycle hard, release only to permit, prove it all with gauges.",
  "Wells and sumps dry the workings; pumps lift; the plant drinks recycled water first. "
  "Contact water is gathered and treated - acidity, metals, sediment - to the permit's numbers. "
  "Wells and gauges around the site tell the water's story to all who ask.",
  ["Every water counted: the balance the scripture.",
   "Dewater, supply, treat, release-to-permit.",
   "Recycle hard.",
   "Gauges proving the story."],
  ["Wells, pumps, sumps to the inflow.",
   "Treatment for the contact water.",
   "Watching wells and gauges."],
  ["Discharge to permit, verified always.",
   "Neighbors' waters guarded from harm.",
   "Storms planned for, not wished away."],
  ["Mine water literature (public publications).",
   "The public edition water record, for the mechanics (this system)."],
  "water", {"flow_lps": 85.0}),

R("The Standing Ground — Signature Geotechnics", "Compounded", 23,
  "The Signature method keeps the ground standing: walls at the rock's true angles, openings supported to their design, dumps stable for the long years. "
  "Rock is the mine's material and mystery; the method designs for what the rock will do, then watches to learn what it does. "
  "Trigger plans stand ready for the ground's complaints.",
  "The rock mass is mapped, cored, and tested; slopes and openings are drawn to their safety factors. "
  "Bolts, mesh, shotcrete, and cables hold the design; prisms, radar, and extensometers listen. "
  "When movement quickens, the trigger plan answers - exactly as written.",
  ["The ground standing: designed, supported, watched.",
   "Rock the material and mystery.",
   "Watching closing the loop to design.",
   "Trigger plans answering as written."],
  ["Drilling, logging, testing the rock.",
   "Designers and instruments.",
   "Support crews: bolting, shotcrete."],
  ["Safety factors honored.",
   "Watching reviewed on schedule; alarms answered.",
   "No work beneath unsupported ground."],
  ["Mining geotechnics literature (public publications).",
   "The public edition geotechnics record, for the mechanics (this system)."],
  "stripratio", {"waste": 12000000.0, "ore": 4000000.0}),
]

SIG += [
R("The Pit's Pulse — Signature Strip Ratios", "Advanced", 24,
  "The Signature method feels the pit's pulse in the strip ratio: waste per ore, the cost of reaching against the worth of grasping. "
  "Low ratios in youth fund the high ratios of age; each pushback is judged alone - does its ore pay its stripping. "
  "The pit rests where the pulse fails: stripping cost beyond ore margin.",
  "Ratios are tracked pushback by pushback; the young low-ratio phases bankroll the old. "
  "The limit is found where incremental stripping costs more than the ore's margin. "
  "Dumps, hauls, and fleets are sized to the ratio's truth.",
  ["The strip ratio the pit's pulse.",
   "Youth's low ratios funding age's high.",
   "Each pushback judged alone.",
   "Resting where stripping outcosts margin."],
  ["Block ratios per pushback.",
   "Dump room for the planned waste.",
   "Fleet for the total movement."],
  ["Pushback worth re-proven with prices.",
   "Dumps engineered for their volumes.",
   "No high-grading stranding the later."],
  ["Open-pit economics literature (public publications).",
   "The public edition strip-ratio record, for the mechanics (this system)."],
  "stripratio", {"waste": 95000000.0, "ore": 22000000.0}),

R("The Market's Tides — Signature Mineral Economics", "Advanced", 25,
  "The Signature method studies the market's tides: supply, demand, inventories, and speculation raising and lowering the metal's price on the great exchanges. "
  "Each metal its harbor, its benchmark, its cycle - and the mine that survives the ebb harvests the flood. "
  "Hedging moors part of the cargo to fixed prices; royalties are the harbor dues, shaping where ships are built.",
  "Prices form where mine supply, scrap, demand, and stocks meet; contracts follow benchmarks plus premiums. "
  "Feasibilities are sailed through many price weathers; hedges lock the chosen portion. "
  "The state's share is paid where dug, by the royalty's design.",
  ["The market's tides: supply, demand, stocks, speculation.",
   "Survive the ebb to harvest the flood.",
   "Hedging mooring part of the cargo.",
   "Royalties the harbor dues."],
  ["Price foresight in scenarios, never single.",
   "Hedging policy from the board.",
   "Market intelligence kept."],
  ["Assumptions disclosed in feasibility.",
   "Hedges within policy.",
   "Dues paid where dug."],
  ["Mineral economics literature (public publications).",
   "The public edition mineral-economics record, for the mechanics (this system)."],
  "npv", {"capex": 450000000.0, "annual_cf": 95000000.0, "years": 12, "rate": 0.08}),

R("The Promised Sequence — Signature Mine Scheduling", "Advanced", 26,
  "The Signature method schedules as promising: which blocks, which periods, the plant fed at grade and rate - a vow to the plant, the market, and the lenders. "
  "Value is maximized within the honest constraints: mining rates, plant hunger, blending needs. "
  "The long strategy, the short direction, and reconciliation between - and re-promising when the world changes.",
  "Optimizers order the pushbacks and blocks for greatest present value; engineers shape them into ramped, practical phases. "
  "Weekly and monthly plans steer the fleet daily; reconciliation weighs promise against ground truth. "
  "Stale schedules are reborn with new prices and knowledge.",
  ["Scheduling as promising: blocks, periods, plant fed true.",
   "Value maximized within honest constraints.",
   "Long strategy, short direction, reconciliation.",
   "Re-promised when the world changes."],
  ["Planning craft and software.",
   "A current model and true costs.",
   "Survey and production for reconciliation."],
  ["Schedules within rock and permit law.",
   "Reserve schedules on feasibility ground.",
   "Reconciliation told honestly."],
  ["Mine scheduling literature (public publications).",
   "The public edition scheduling record, for the mechanics (this system)."],
  "haul", {"trucks": 32, "payload_t": 290.0, "trips_per_day": 16.0}),

R("The Held Earth — Signature Ground Control", "Advanced", 27,
  "The Signature method holds the earth: openings drawn for what the rock can bear, support installed to the plan, instruments listening for the ground's voice. "
  "Bursts, falls, and squeezes each have their answer; the ground control plan is the constitution every excavation obeys. "
  "Re-entry after blasting waits its lawful time.",
  "Rock is rated and classed; spans and support are drawn from experience and numbers. "
  "Bolts, mesh, shotcrete, and cables hold; extensometers and seismic ears listen. "
  "When the ground speaks quickly, the trigger plan answers exactly.",
  ["Holding the earth: drawn, supported, listened to.",
   "The plan the constitution of the deep.",
   "Instruments the ground's voice.",
   "Re-entry waiting its lawful time."],
  ["Geotechnical keepers and the plan.",
   "Support rigs: bolting, shotcrete.",
   "Listening: extensometers, seismic, eyes."],
  ["No excavation beyond the plan.",
   "Support proven, not assumed.",
   "Burst protocols obeyed."],
  ["Ground-control regulations (public regulations).",
   "The public edition ground-control record, for the mechanics (this system)."],
  "drill", {"holes": 120, "avg_depth_m": 18.0}),

R("The Unmanned Shift — Signature Automation", "Advanced", 28,
  "The Signature method shifts the dangerous to the unmanned: trucks driving their GPS roads, loaders worked from the surface, drills executing their programmed patterns - people lifted from harm's way. "
  "The control room becomes the mine's new face; the private network its nerves. "
  "And the transformation is human too: operators become controllers, honestly retrained, never discarded.",
  "Trucks steer by satellite and laser along their roads; loaders answer surface hands; drills follow their programs. "
  "Controllers supervise the fleet; cyber-guards watch the operational technology. "
  "When automation stumbles, manual hands stand ready.",
  ["The dangerous to the unmanned; people lifted from harm.",
   "The control room the mine's new face.",
   "The network the nerves.",
   "Operators become controllers, honestly retrained."],
  ["Automation-ready fleet and private network.",
   "A control room with trained controllers.",
   "Cyber-guards on the operational tech."],
  ["Safety proven for the unmanned.",
   "Workers transitioned with, not around.",
   "Manual fallback standing ready."],
  ["Mine automation literature (public publications).",
   "The public edition automation record, for the mechanics (this system)."],
  "haul", {"trucks": 40, "payload_t": 320.0, "trips_per_day": 20.0}),

R("The Night-and-Day Mill — Signature Plant Operations", "Advanced", 29,
  "The Signature method runs the mill night and day: ore in, concentrate or metal out, recovery held to its promise, availability the crown metric. "
  "The plant is alchemy at scale - crush, grind, separate, dewater - and its keepers watch grind, chemistry, and density without ceasing. "
  "Accounting proves the recovery; maintenance guards the availability.",
  "Feed flows through crushing and grinding to separation - flotation, leaching, gravity - then thickening and filtration. "
  "Operators trim grind size, reagent doses, and densities to their targets. "
  "Mass balances close around every unit, and the monthly account is signed.",
  ["Night and day: ore in, metal out.",
   "Availability the crown metric.",
   "Grind, chemistry, density watched unceasing.",
   "Accounting proving recovery."],
  ["The whole circuit built and tended.",
   "Keepers and metallurgists around the clock.",
   "Maintenance guarding availability."],
  ["Chemicals handled safely.",
   "Dust, noise, effluent within permit.",
   "Tailings to their managed house only."],
  ["Mineral processing operations literature (public publications).",
   "The public edition plant record, for the mechanics (this system)."],
  "grind", {"feed_tph": 2500.0, "hours": 21.5}),

R("The Kept Footprint — Signature Environment", "Advanced", 30,
  "The Signature method keeps the footprint within its sworn bounds: air, water, land, and wild things guarded by design and proven by watching. "
  "The license to dig is earned daily - one poisoned stream can end the house. "
  "Reclamation walks beside mining, healing ground as the pit advances, not decades after.",
  "Baselines are taken before the first disturbance; plans cover water, air, waste, wilds, and heritage. "
  "Watching - water, dust, noise, wildlife - proves compliance; exceedances are corrected and confessed. "
  "Finished ground is shaped and greened while the mine still breathes.",
  ["The footprint within sworn bounds.",
   "The license earned daily.",
   "Reclamation walking beside mining.",
   "One poisoned stream ending the house."],
  ["Environmental keepers and the plans.",
   "Watching networks: water, air, wilds.",
   "Reclamation gear and growing soil."],
  ["Permits obeyed; exceedances corrected and told.",
   "Wilds offset where required.",
   "Grievances heard and answered."],
  ["ICMM environmental principles (public guidance).",
   "The public edition environment record, for the mechanics (this system)."],
  "water", {"flow_lps": 200.0}),

R("The Healed Land — Signature Closure", "Advanced", 31,
  "The Signature method closes as it began - with a promise: the land stable, safe, and fruitful after mining, water treated as long as the earth needs, the money for healing set aside beyond any company's fall. "
  "Closure is drawn before the first blast and funded by assurance no bankruptcy can touch. "
  "The healed land should need no apology.",
  "Reclamation advances with mining; at the end, works are removed or given new life, pits made safe, dumps shaped and covered. "
  "Water is treated for as long as required - decades where the chemistry demands. "
  "Bonds or trusts hold the healing's price, reviewed as costs clarify; monitoring proves the landform for the long years.",
  ["Closure promised before the first blast.",
   "The land stable, safe, fruitful after.",
   "Healing funded beyond any company's fall.",
   "Water treated as long as needed."],
  ["A closure plan with costed designs.",
   "Assurance sized and reviewed.",
   "Long watching capability."],
  ["Assurance bankruptcy-remote.",
   "Closure marks agreed with regulators and people.",
   "Long water duties funded, never wished."],
  ["ICMM closure guidance (public guidance).",
   "The public edition closure record, for the mechanics (this system)."],
  "npv", {"capex": 120000000.0, "annual_cf": -8000000.0, "years": 20, "rate": 0.05}),

R("The Measurers — Signature Surveying", "Advanced", 32,
  "The Signature method measures everything: volumes for payment, patterns for blasting, tunnels for straightness, stockpiles for truth. "
  "The surveyor's instruments - total station, GPS, drone, scanner - are the mine's honest eyes. "
  "Underground, the gyro carries bearing through the shafts where no sky reaches.",
  "Patterns are set out, blasts bounded, volumes picked up for reconciliation and the contractor's pay. "
  "Stopes are scanned in minutes; pits and dumps are flown weekly into volumes and plans. "
  "The coordinate system is guarded as the mine's true north.",
  ["Measuring everything: the mine's honest eyes.",
   "Volumes for payment, patterns for blasting.",
   "The gyro bearing where no sky reaches.",
   "The coordinate system the true north."],
  ["Instruments: stations, GPS, drones, scanners.",
   "Surveyors surface and deep.",
   "The coordinate frame rigorously kept."],
  ["Payment volumes independently proven.",
   "Blast grounds surveyed before firing.",
   "Control guarded from mining's damage."],
  ["Mine surveying standards (public standards).",
   "The public edition surveying record, for the mechanics (this system)."],
  "drill", {"holes": 200, "avg_depth_m": 12.0}),

R("The Counted Metal — Signature Metallurgical Accounting", "Advanced", 33,
  "The Signature method counts every grain of metal: mine to plant to product, feed against concentrate against tailings, recovery proven by balance. "
  "The account is the plant's financial soul - in, out, lost, balanced. "
  "Without it, recovery is wish and metal may walk away unseen.",
  "Balances close around each unit: two streams measured, the third by difference, all tried against the whole. "
  "Errors are weighed, streams are valued, the month's account is signed. "
  "Imbalance is investigated - error or theft, the account does not rest until it knows.",
  ["Every grain counted: the plant's financial soul.",
   "Balances closing around each unit.",
   "Recovery proven, not wished.",
   "Imbalance investigated to its name."],
  ["Weighing, sampling, assay at balance points.",
   "An accountant independent of operation.",
   "Reconciliation craft and procedure."],
  ["Balances closed and signed on schedule.",
   "Errors weighed, never ignored.",
   "Sales settled against the account."],
  ["Metal accounting literature (public publications).",
   "The public edition accounting record, for the mechanics (this system)."],
  "recovery", {"feed_metal": 1400.0, "recovered_metal": 1288.0}),

R("The Delver's Review — Signature Mastery", "Advanced", 34,
  "The delver's review gathers the whole art: geology, engineering, processing, and stewardship as one living mine, the earth's trust at the end of every gauge. "
  "Each earlier record was a discipline; this is the master delver's mind. "
  "Production, safety, cost, and closure held in balance - none sacrificed.",
  "From the ore body reason outward: honestly numbered, planned for value, broken and moved safely, recovered truly, water and land guarded, closure funded. "
  "Keep the daily rhythm - production, safety, grade - and the long rhythm - planning, permitting, healing. "
  "Watch the gauges - safety, tonnes and grade, recovery, cost per tonne, closure's advance - and let every decision lift at least one.",
  ["The whole art: one living mine.",
   "Reason outward from the ore body.",
   "Production, safety, cost, closure: none sacrificed.",
   "The daily rhythm and the long rhythm."],
  ["The full ladder fluent, foundations through advanced.",
   "Safety never sleeping.",
   "Gauges read together, honestly."],
  ["Safety never traded for tonnes.",
   "Resources told truly under the codes.",
   "Closure funded and advancing."],
  ["The public edition mastery record, for the mechanics (this system).",
   "Signature system governance on original works (this system)."],
  "metal", {"tonnes": 30000000.0, "grade_pct": 1.1}),
]

GEN_DEMOFN = """function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\\n"
   + "# Metal-content structural sample calculator (mining industries)\\n"
   + "t, g = 1000000.0, 1.2\\n"
   + "metal = t*g/100.0\\n"
   + "print('sample tonnes:', t)\\n"
   + "print('sample grade %:', g)\\n"
   + "print('sample contained metal t:', round(metal,1))\\n"
   + "assert metal > 0\\n"
   + "print('OK: structural sample demo ran')\\n";
}
"""
