#!/usr/bin/env python3
"""Entries for the Public Infrastructure Assets databases (2026-10-17).

34 infrastructure asset topics, ladder-ordered 1-34
(foundations 1-12 / compounded 13-24 / advanced 25-34).
Public = real, fact-checked domain data. Signature = Signature
infrastructure interpretation, titles suffixed " (Signature Edition)".
No website references. No Facebook.
"""


def E(name, group, rank, tier, description, how, key_points, requirements,
      standards, citations, sig_lens, demo_data, demo_key="asset"):
    return {"name": name, "group": group, "ladder_rank": rank,
            "ladder_tier": tier, "description": description,
            "how_it_works": how, "key_points": key_points,
            "requirements": requirements, "standards": standards,
            "citations": citations, "sig_lens": sig_lens,
            "demo_key": demo_key, "demo_data": demo_data}


ENTRIES = [

# ---------------- FOUNDATIONS 1-12 ----------------

E("Road Networks: Arterials, Collectors, and Local Streets", "Foundations", 1,
  "foundations",
  "Public roads are organized by function: arterials carry long-distance "
  "traffic at higher speeds, collectors gather traffic from neighborhoods "
  "and feed the arterials, and local streets provide direct access to "
  "homes and businesses. This functional classification, used by the "
  "Federal Highway Administration, decides which roads get federal aid, "
  "what design standards apply, and how they are maintained. America "
  "has over 4 million miles of public road, the vast majority owned by "
  "states, counties, and cities. Pavement types range from asphalt and "
  "concrete to gravel on rural routes, and each mile carries a "
  "maintenance liability measured in decades.",
  "Transportation agencies classify every road segment by function, "
  "then design, build, and maintain to matching standards. Arterials "
  "get wider lanes, controlled access, and signal coordination; "
  "collectors balance movement and access; local streets prioritize "
  "access and neighborhood livability. Pavement management systems "
  "inspect condition on cycles, schedule preventive treatments like "
  "crack sealing and overlays, and reconstruct when the pavement "
  "fails. Funding flows from fuel taxes, vehicle fees, and federal aid "
  "apportioned by classification and use.",
  ["Arterials move traffic; collectors gather it; locals provide access.",
   "Classification decides federal aid eligibility and design standards.",
   "Over 4 million miles of public road in the United States.",
   "Each mile carries a decades-long maintenance liability."],
  ["Classification must follow FHWA functional classification guidance.",
   "Design must meet AASHTO geometric standards for the class.",
   "Federal-aid routes require state maintenance commitments."],
  ["FHWA Functional Classification Guidelines.",
   "AASHTO Policy on Geometric Design of Highways and Streets."],
  ["Federal Highway Administration - functional classification guidance.",
   "AASHTO Green Book (geometric design policy)."],
  "In the Signature infrastructure system roads are sworn arteries: "
  "the arterial a covenant of swift passage, the collector a gathering "
  "promise, the local street a sworn welcome to every door.",
  {"repl_value_m": 2.5, "condition": 3, "age_y": 18, "design_life_y": 30}),

E("Highway Bridges", "Foundations", 2, "foundations",
  "Bridges are the most critical links in the road network — and its "
  "most closely watched assets. The United States has more than 600,000 "
  "highway bridges, most owned by states and counties. Every public "
  "bridge over 20 feet long must be inspected at least every 24 months "
  "under the National Bridge Inspection Standards, with ratings for "
  "deck, superstructure, substructure, and culvert on a 0–9 scale. "
  "Bridges rated 4 or below on key components are classified "
  "structurally deficient and prioritized for repair or replacement. "
  "Types range from simple slab spans to suspension and cable-stayed "
  "landmarks, each with its own inspection demands.",
  "Inspectors examine every element on cycle — visually, with "
  "hands-on access to fracture-critical members, and with underwater "
  "inspection where needed. Ratings feed the National Bridge Inventory, "
  "which Congress and states use to allocate replacement funds. "
  "Load ratings determine legal truck weights; posting signs restrict "
  "heavy vehicles on weak bridges. Deterioration models forecast "
  "condition decline, scheduling rehabilitation before failure. "
  "Emergency closures follow when inspections find critical risk.",
  ["600,000+ highway bridges, mostly state and county owned.",
   "Inspected at least every 24 months under NBIS.",
   "Rated 0-9 on deck, superstructure, substructure, culvert.",
   "Structurally deficient bridges prioritized for repair."],
  ["Inspections must follow the National Bridge Inspection Standards.",
   "Fracture-critical members need hands-on inspection.",
   "Load postings must reflect the rated capacity."],
  ["National Bridge Inspection Standards (23 CFR 650).",
   "AASHTO Manual for Bridge Evaluation."],
  ["Federal Highway Administration - National Bridge Inventory.",
   "National Bridge Inspection Standards, 23 CFR 650 Subpart C."],
  "In the Signature infrastructure system a bridge is a sworn span: "
  "every inspection a covenant of vigilance, every rating an honest "
  "measure of strength, every repair a promise kept to travelers.",
  {"repl_value_m": 8.0, "condition": 3, "age_y": 42, "design_life_y": 75}),

E("Water Treatment Plants", "Foundations", 3, "foundations",
  "Water treatment plants turn raw water from rivers, lakes, and wells "
  "into safe drinking water. The conventional train — coagulation and "
  "flocculation, sedimentation, filtration, and disinfection — removes "
  "particles, pathogens, and contaminants to meet the Safe Drinking "
  "Water Act's standards for some 90 contaminants. America operates "
  "tens of thousands of community water systems, most publicly owned. "
  "Plants range from small package units serving villages to giant "
  "facilities treating hundreds of millions of gallons a day. "
  "Operators must be licensed, and systems test water continuously and "
  "report to the public in annual consumer confidence reports.",
  "Raw water enters, chemicals coagulate suspended particles into floc, "
  "sedimentation basins settle it out, filters polish the water, and "
  "disinfectants — chlorine, chloramine, ozone, or ultraviolet light — "
  "kill pathogens. Laboratories test for bacteria, turbidity, lead, "
  "disinfection byproducts, and more on strict schedules. SCADA systems "
  "control pumps, chemical feeds, and flows around the clock. When "
  "tests fail, the system issues public notice and fixes the problem "
  "under state enforcement.",
  ["Convert raw water to safe drinking water.",
   "Conventional train: coagulation, sedimentation, filtration, disinfection.",
   "Must meet Safe Drinking Water Act standards for ~90 contaminants.",
   "Operators licensed; results reported in consumer confidence reports."],
  ["Treatment must achieve required pathogen removal and disinfection.",
   "Monitoring must follow the mandated contaminant schedules.",
   "Public notice is required for violations."],
  ["Safe Drinking Water Act National Primary Drinking Water Regulations.",
   "AWWA treatment and operation standards."],
  ["U.S. Environmental Protection Agency - drinking water standards.",
   "American Water Works Association - treatment standards."],
  "In the Signature infrastructure system a treatment plant is the "
  "sworn purifier: every filter a covenant of clarity, every test a "
  "witness to safety, every gallon delivered a promise of life.",
  {"repl_value_m": 45.0, "condition": 3, "age_y": 28, "design_life_y": 50}),

E("Wastewater Collection and Treatment", "Foundations", 4, "foundations",
  "Wastewater systems collect used water from homes and businesses "
  "through sewer networks and clean it at treatment plants before "
  "returning it to rivers or reusing it. Treatment progresses from "
  "preliminary screening through primary settling, secondary "
  "biological treatment, and often tertiary filtration and "
  "disinfection. Discharge permits under the Clean Water Act's NPDES "
  "program set strict pollutant limits. Combined sewers in older "
  "cities carry stormwater too, overflowing in heavy rain — a "
  "multibillion-dollar correction underway nationwide. Biosolids, the "
  "treated solids, are recycled as fertilizer or disposed under "
  "regulation.",
  "Sewers flow by gravity to lift stations and interceptors feeding "
  "the plant. Operators manage biological processes — activated "
  "sludge, trickling filters, or membrane bioreactors — where "
  "microbes consume pollutants. Laboratories test effluent against "
  "permit limits for oxygen demand, solids, nutrients, and bacteria. "
  "SCADA controls flows and chemical feeds. Collection crews clean, "
  "inspect with cameras, and rehabilitate aging pipes by lining or "
  "replacement. Pretreatment programs keep industries from poisoning "
  "the biology.",
  ["Collect sewage and clean it before discharge or reuse.",
   "Treatment stages: preliminary, primary, secondary, tertiary.",
   "NPDES permits set strict pollutant limits.",
   "Combined-sewer overflows are a national correction priority."],
  ["Discharges require NPDES permits with enforceable limits.",
   "Operators must be licensed; labs must meet QA standards.",
   "Biosolids use and disposal follow Part 503 rules."],
  ["Clean Water Act NPDES regulations (40 CFR 122).",
   "EPA biosolids standards (40 CFR Part 503)."],
  ["U.S. Environmental Protection Agency - wastewater and NPDES.",
   "Water Environment Federation - operation standards."],
  "In the Signature infrastructure system a treatment plant is the "
  "sworn renewer: what the city used returns clean, every permit "
  "limit a covenant with the river, every microbe an unseen keeper "
  "of the promise.",
  {"repl_value_m": 60.0, "condition": 2, "age_y": 35, "design_life_y": 50}),

E("Stormwater Drainage Systems", "Foundations", 5, "foundations",
  "Stormwater systems carry rain away from streets and buildings "
  "through inlets, pipes, ditches, detention basins, and outfalls. "
  "They are a distinct utility in many cities, funded by stormwater "
  "fees based on impervious area. Under the Clean Water Act's MS4 "
  "program, cities must manage runoff quality as well as quantity, "
  "controlling pollutants that wash off pavement. Green "
  "infrastructure — rain gardens, permeable pavement, bioswales — "
  "now complements gray pipes, soaking water in where it falls. "
  "Undersized or clogged systems flood streets and basements, making "
  "drainage one of the most complaint-driven public works.",
  "Engineers size pipes and basins for design storms using hydrologic "
  "models. Crews clean inlets and pipes, inspect outfalls, and "
  "maintain basins. MS4 permittees run illicit-discharge detection, "
  "construction-site controls, and public education. Asset "
  "inventories map every inlet and pipe; condition assessment "
  "prioritizes rehabilitation. Capital projects upsize bottlenecks "
  "and add storage where development increased runoff.",
  ["Carry rain away via inlets, pipes, basins, and outfalls.",
   "Often a fee-funded utility based on impervious area.",
   "MS4 permits require runoff quality management.",
   "Green infrastructure complements gray pipes."],
  ["MS4 permittees must implement minimum control measures.",
   "Design must handle adopted design storms.",
   "Illicit discharges must be detected and eliminated."],
  ["Clean Water Act MS4 regulations (40 CFR 122.26).",
   "State stormwater design manuals."],
  ["U.S. Environmental Protection Agency - stormwater program.",
   "State MS4 general permits."],
  "In the Signature infrastructure system drainage is the sworn "
  "channel: every inlet a covenant that rain will find its way, "
  "every basin a promise of patience, every clean outfall a witness "
  "to the city's care.",
  {"repl_value_m": 18.0, "condition": 3, "age_y": 25, "design_life_y": 50}),

E("Public Buildings", "Foundations", 6, "foundations",
  "Public buildings — city halls, courthouses, libraries, community "
  "centers, maintenance yards — are the physical home of government "
  "services. A city's building portfolio can number in the hundreds, "
  "each with roofs, HVAC, electrical, plumbing, and life-safety "
  "systems aging on different clocks. Facility condition assessments "
  "score each building and system, feeding capital plans that "
  "prioritize roofs before they leak and boilers before they fail. "
  "Energy benchmarking and retrofits cut operating costs, and "
  "accessibility upgrades keep buildings open to all under the ADA.",
  "Facility managers inventory every building and major system, "
  "assess condition on cycles, and estimate deferred maintenance — "
  "the backlog of needed work. Work-order systems dispatch preventive "
  "maintenance and repairs. Capital planning ranks projects by "
  "condition, criticality, and energy impact. Design and construction "
  "follow public procurement and building codes. Commissioning "
  "verifies new systems perform; energy management systems track "
  "consumption against benchmarks.",
  ["City halls, courthouses, libraries, yards — the home of services.",
   "Each building's systems age on different clocks.",
   "Condition assessments feed capital prioritization.",
   "ADA and energy rules shape upgrades."],
  ["Assessments must cover all major building systems.",
   "Construction must follow public procurement law.",
   "Facilities must meet building codes and ADA."],
  ["State building codes.",
   "Americans with Disabilities Act accessibility standards."],
  ["International Code Council - building codes.",
   "U.S. Access Board - ADA standards."],
  "In the Signature infrastructure system a public building is a "
  "sworn house of service: every roof a covenant of shelter, every "
  "accessible entrance a promise that government opens its doors to "
  "all.",
  {"repl_value_m": 12.0, "condition": 3, "age_y": 40, "design_life_y": 60}),

E("Parks and Recreation Facilities", "Foundations", 7, "foundations",
  "Parks are the green infrastructure of public life: playgrounds, "
  "sports fields, trails, pools, and open space that cities hold in "
  "trust for recreation and health. A parks department manages land, "
  "turf, trees, irrigation, restrooms, and play equipment — each with "
  "safety and maintenance demands. Playgrounds must meet consumer "
  "safety standards and be inspected for hazards. Sports turf needs "
  "mowing, aeration, and rest. Pools need certified operators and "
  "water chemistry control. Urban forestry programs plant and prune "
  "the street and park trees that shade the city.",
  "Park planners acquire land, design facilities with public input, "
  "and build to safety standards. Maintenance crews follow turf, "
  "tree, and equipment schedules; inspectors check playgrounds for "
  "entrapment, falls, and wear. Aquatics staff test water chemistry "
  "multiple times daily. Arborists prune on cycles and remove "
  "hazardous trees. Programming staff run leagues, classes, and "
  "events. Master plans set levels of service — acres and facilities "
  "per thousand residents — guiding acquisition and development.",
  ["Playgrounds, fields, trails, pools, open space held in public trust.",
   "Playgrounds inspected to safety standards; pools need certified operators.",
   "Urban forestry plants and prunes the city's trees.",
   "Master plans set acres and facilities per capita."],
  ["Playgrounds must meet CPSC and ASTM safety standards.",
   "Pools must meet health codes with certified operators.",
   "Tree work must follow arboricultural safety practices."],
  ["CPSC Public Playground Safety Handbook; ASTM F1487.",
   "State and local pool health codes."],
  ["U.S. Consumer Product Safety Commission - playground safety.",
   "National Recreation and Park Association - standards."],
  "In the Signature infrastructure system a park is sworn common "
  "ground: every playground a covenant of safe play, every tree a "
  "promise of shade, every trail an open invitation to all.",
  {"repl_value_m": 6.0, "condition": 3, "age_y": 20, "design_life_y": 40}),

E("Street Lighting", "Foundations", 8, "foundations",
  "Street lighting makes roads safe after dark: poles, mast arms, "
  "luminaires, and the circuits feeding them, now overwhelmingly LED. "
  "The LED conversion — one of the great municipal upgrades of the "
  "2010s and 2020s — cut energy use roughly in half and slashed "
  "maintenance, since LEDs last far longer than old sodium lamps. "
  "Lighting levels follow IES standards by road class, balancing "
  "safety, glare, and light pollution. Smart controls add dimming and "
  "outage reporting. Dark-sky ordinances in many communities limit "
  "spill and color temperature to protect the night.",
  "Engineers design lighting to IES recommended levels for the road "
  "class, spacing poles and sizing luminaires by photometric "
  "calculation. Crews install, relamp, and repair knockdowns; many "
  "cities contract maintenance to the electric utility. Asset "
  "inventories track every pole and fixture. LED retrofits are "
  "financed by energy savings. Outage management systems dispatch "
  "repairs from citizen reports and smart-controller alarms.",
  ["Poles, luminaires, and circuits — now overwhelmingly LED.",
   "LED conversion cut energy roughly in half.",
   "Levels follow IES standards by road class.",
   "Smart controls add dimming and outage reporting."],
  ["Design must meet IES illuminance recommendations.",
   "Electrical work must meet the National Electrical Code.",
   "Dark-sky ordinances may limit spill and color temperature."],
  ["IES recommended practices for roadway lighting.",
   "National Electrical Code (NFPA 70)."],
  ["Illuminating Engineering Society - roadway lighting practice.",
   "International Dark-Sky Association - guidance."],
  "In the Signature infrastructure system streetlights are sworn "
  "lanterns: every lit intersection a covenant of safe passage, "
  "every repaired outage a promise that the dark will not win.",
  {"repl_value_m": 4.0, "condition": 4, "age_y": 8, "design_life_y": 25}),

E("Traffic Signals", "Foundations", 9, "foundations",
  "Traffic signals are the choreography of intersections: controllers, "
  "signal heads, detectors, poles, and the timing plans that decide "
  "who moves when. A single city's signals can number in the hundreds, "
  "each a small computer running phases and intervals tuned to traffic "
  "patterns. Retiming — adjusting cycle lengths, splits, and offsets — "
  "is among the cheapest capacity improvements available, cutting "
  "delay and emissions. Detection by loops, cameras, or radar lets "
  "signals respond to actual demand. Malfunctioning signals are "
  "treated as four-way stops by law, and signal technicians are on "
  "call around the clock.",
  "Engineers warrant signals by traffic-volume, crash, and pedestrian "
  "criteria, then design phasing and timing. Technicians install, "
  "maintain, and retime on cycles — typically every few years or when "
  "patterns change. Central systems monitor operation and push timing "
  "updates; adaptive systems adjust in real time. Preventive "
  "maintenance covers conflict monitors, batteries, and detection. "
  "Crash and delay data justify upgrades and new installations.",
  ["Controllers, heads, detectors, and timing plans at each intersection.",
   "Retiming is among the cheapest capacity improvements.",
   "Detection lets signals respond to real demand.",
   "Failed signals legally become four-way stops."],
  ["Signal warrants must follow the MUTCD.",
   "Timing must provide safe clearance intervals.",
   "Maintenance must keep conflict monitors functional."],
  ["Manual on Uniform Traffic Control Devices (MUTCD).",
   "ITE signal timing and design guidance."],
  ["Federal Highway Administration - MUTCD.",
   "Institute of Transportation Engineers - signal guidance."],
  "In the Signature infrastructure system a signal is a sworn "
  "conductor: every green a covenant of orderly movement, every "
  "retiming a promise that the city's rhythm serves its people.",
  {"repl_value_m": 0.35, "condition": 3, "age_y": 12, "design_life_y": 20}),

E("Sidewalks and Curb Ramps", "Foundations", 10, "foundations",
  "Sidewalks and curb ramps are the pedestrian network — and a civil "
  "rights obligation. The ADA requires accessible pedestrian routes: "
  "curb ramps with detectable warnings at crossings, adequate width, "
  "and manageable slopes. Cities inventory every sidewalk segment and "
  "ramp, rate trip hazards and deterioration, and grind, replace, or "
  "rebuild on priority. In many places abutting property owners share "
  "repair responsibility by ordinance. Transition plans schedule the "
  "retrofit of noncompliant ramps. A walkable city is built one ramp "
  "at a time.",
  "Public works inventories sidewalks by segment, rating cracking, "
  "uplift, and ponding. Crews grind trip hazards, replace panels, and "
  "rebuild ramps to ADA slopes and detectable-warning standards. "
  "Capital programs target corridors near schools, transit, and senior "
  "centers first. Inspectors enforce obstructions and construction "
  "detours. ADA transition plans document barriers and schedule "
  "correction with public input. Costs are tracked per linear foot "
  "for budgeting.",
  ["The pedestrian network and a civil rights obligation.",
   "ADA requires ramps, detectable warnings, width, and slopes.",
   "Cities inventory, rate, and repair on priority.",
   "Transition plans schedule noncompliant ramp retrofits."],
  ["New and altered facilities must meet ADA standards.",
   "Curb ramps require detectable warnings.",
   "Transition plans must schedule barrier removal."],
  ["ADA Standards for Accessible Design.",
   "Public Rights-of-Way Accessibility Guidelines (PROWAG)."],
  ["U.S. Access Board - ADA and PROWAG.",
   "Federal Highway Administration - pedestrian guidance."],
  "In the Signature infrastructure system a curb ramp is a sworn "
  "threshold: every smooth transition a covenant that the street "
  "belongs to everyone, every repaired slab a promise of safe steps.",
  {"repl_value_m": 1.2, "condition": 2, "age_y": 30, "design_life_y": 40}),

E("Public Parking Facilities", "Foundations", 11, "foundations",
  "Public parking — garages, lots, and metered streets — is a priced "
  "utility managing the scarcest urban land. Structures are expensive "
  "concrete assets with decks, ramps, lighting, ventilation, and "
  "payment systems, inspected for structural condition and "
  "waterproofing. Pricing follows demand: the best-performing systems "
  "adjust meter rates by block and hour to keep one or two spaces open "
  "per block, cutting cruising traffic. Revenue funds maintenance, "
  "debt, and often streetscape improvements. Electric-vehicle charging "
  "and accessible spaces are now standard provisions.",
  "Parking managers inventory every space and asset, set rates by "
  "occupancy studies, and enforce time limits. Engineers inspect "
  "garages for deck deterioration, post-tensioning, and drainage; "
  "repairs are staged to keep capacity open. Payment systems — meters, "
  "pay stations, apps — feed revenue and occupancy data. Demand-based "
  "pricing pilots adjust rates periodically. Capital plans schedule "
  "membrane replacement, lighting upgrades, and EV infrastructure.",
  ["Garages, lots, and meters managing scarce urban land.",
   "Structures need deck, drainage, and safety inspection.",
   "Demand-based pricing keeps spaces available and cuts cruising.",
   "Revenue funds maintenance and improvements."],
  ["Structures must meet building and fire codes.",
   "Accessible spaces must meet ADA counts and dimensions.",
   "Rate-setting should follow adopted parking policy."],
  ["State building codes; NFPA parking structure provisions.",
   "ADA Standards (accessible parking)."],
  ["International Parking and Mobility Institute - guidance.",
   "National Academies - parking research."],
  "In the Signature infrastructure system public parking is a sworn "
  "stewardship of scarcity: every priced space a covenant of fair "
  "turnover, every maintained deck a promise of safe return.",
  {"repl_value_m": 15.0, "condition": 3, "age_y": 25, "design_life_y": 50}),

E("Solid Waste and Landfill Facilities", "Foundations", 12, "foundations",
  "Solid waste systems collect trash, recyclables, and organics and "
  "manage their final disposition. Modern landfills are engineered "
  "facilities — composite liners, leachate collection, gas capture, "
  "daily cover, groundwater monitoring — regulated under Subtitle D of "
  "RCRA. Transfer stations consolidate collection trucks into long-"
  "haul trailers. Materials recovery facilities sort recyclables. "
  "Composting and anaerobic digestion divert organics. Landfill gas "
  "is captured for energy or flared. Closure and 30-year post-closure "
  "care are priced into tipping fees from day one.",
  "Collection routes run on weekly cycles; transfer stations and "
  "MRFs process the streams. Landfill operators place waste in cells, "
  "compact, cover daily, and manage leachate and gas systems. "
  "Engineers monitor groundwater wells and gas probes on schedule, "
  "reporting to the state. Permits set design, operating, and closure "
  "standards; financial assurance guarantees closure funds. Diversion "
  "programs — recycling, organics, household hazardous waste events — "
  "extend landfill life.",
  ["Engineered landfills with liners, leachate, and gas systems.",
   "Transfer stations, MRFs, composting complete the system.",
   "Regulated under RCRA Subtitle D with 30-year post-closure care.",
   "Closure costs priced into tipping fees."],
  ["Landfills require state permits with design and operating standards.",
   "Groundwater monitoring and financial assurance are mandatory.",
   "Diversion programs must meet state mandates where adopted."],
  ["RCRA Subtitle D (40 CFR Part 258).",
   "State solid waste facility permits."],
  ["U.S. Environmental Protection Agency - solid waste regulation.",
   "Solid Waste Association of North America - standards."],
  "In the Signature infrastructure system a landfill is a sworn "
  "repository: every liner a covenant against contamination, every "
  "captured gas molecule a promise of responsibility, every closed "
  "cell a sealed chapter.",
  {"repl_value_m": 40.0, "condition": 3, "age_y": 22, "design_life_y": 40}),

# ---------------- COMPOUNDED 13-24 ----------------

E("Public Dams", "Compounded", 13, "compounded",
  "Dams impound water for supply, flood control, power, and recreation — "
  "and demand uncompromising safety. The United States has over 90,000 "
  "dams, most privately or locally owned, with states regulating "
  "non-federal dams and FERC licensing hydroelectric ones. High-hazard "
  "dams — those whose failure would likely kill — require emergency "
  "action plans, regular inspections, and inundation mapping. The "
  "Association of State Dam Safety Officials estimates thousands need "
  "rehabilitation. Spillways, embankments, and gates are the critical "
  "elements; their failure modes are studied relentlessly because the "
  "consequence of being wrong is catastrophic.",
  "Owners inspect routinely, engineers inspect comprehensively on "
  "cycles, and regulators audit. Instrumentation — piezometers, "
  "monuments, weirs — watches seepage and movement. Emergency action "
  "plans name who calls whom and map inundation zones for evacuation. "
  "Rehabilitation raises spillway capacity, armors embankments, and "
  "replaces aging gates. FERC relicensing reviews safety, environment, "
  "and recreation. State programs classify hazard potential and order "
  "repairs, with enforcement up to breach orders for dangerous dams.",
  ["90,000+ dams; most state-regulated or FERC-licensed.",
   "High-hazard dams need emergency action plans and inundation maps.",
   "Spillways, embankments, and gates are the critical elements.",
   "Thousands need rehabilitation."],
  ["High-hazard dams must have emergency action plans.",
   "Inspections must follow state and FERC schedules.",
   "Unsafe dams can be ordered repaired or breached."],
  ["FERC dam safety regulations (18 CFR Part 12).",
   "State dam safety statutes and rules."],
  ["Federal Energy Regulatory Commission - dam safety.",
   "Association of State Dam Safety Officials - guidance."],
  "In the Signature infrastructure system a dam is a sworn wall: "
  "every inspection a covenant against the flood, every spillway a "
  "promise of controlled power, every emergency plan a vow to the "
  "valley below.",
  {"repl_value_m": 120.0, "condition": 3, "age_y": 60, "design_life_y": 100}),

E("Levees and Flood Control Structures", "Compounded", 14, "compounded",
  "Levees are earthen embankments — with floodwalls, gates, and pump "
  "stations — that hold rivers back from communities. The U.S. Army "
  "Corps of Engineers built many and inspects them; local sponsors "
  "maintain them. The National Levee Database inventories thousands of "
  "miles. Levees are rated for the flood they are designed to hold, "
  "and accreditation by FEMA decides whether land behind them is "
  "mapped as protected for flood insurance. The cruel lesson of "
  "Katrina: levees reduce risk, they do not remove it, and failure "
  "behind a levee is catastrophic precisely because people felt safe.",
  "Sponsors mow, inspect, and repair levees; the Corps inspects "
  "federally authorized systems and rates them acceptable, minimally "
  "acceptable, or unacceptable. Engineers analyze seepage, stability, "
  "and overtopping risk. Accreditation requires certified data proving "
  "the 100-year standard. Risk communication tells residents behind "
  "levees to carry flood insurance anyway. Rehabilitation raises, "
  "armors, or sets back levees; nonstructural measures — buyouts, "
  "elevation — complement the walls.",
  ["Earthen embankments plus walls, gates, and pumps.",
   "Corps-built; locally maintained; inventoried nationally.",
   "FEMA accreditation decides flood-insurance mapping.",
   "Levees reduce risk — they do not remove it."],
  ["Sponsors must maintain to Corps standards.",
   "Accreditation requires certified 100-year protection data.",
   "Emergency plans must cover breach scenarios."],
  ["USACE levee inspection and rehabilitation authorities.",
   "FEMA floodplain mapping standards (44 CFR)."],
  ["U.S. Army Corps of Engineers - National Levee Database.",
   "FEMA - levee accreditation guidance."],
  "In the Signature infrastructure system a levee is a sworn embankment: "
  "every inspection a covenant of vigilance, every accreditation an "
  "honest measure of protection, every warning a promise that safety "
  "is never assumed.",
  {"repl_value_m": 85.0, "condition": 3, "age_y": 55, "design_life_y": 80}),

E("Public Airports", "Compounded", 15, "compounded",
  "Public airports — from general-aviation fields to international hubs — "
  "are city or authority-owned infrastructure operating under FAA "
  "oversight. Commercial-service airports need FAA Part 139 "
  "certification: standards for runways, safety areas, rescue and fire "
  "fighting, and wildlife hazard management. The Airport Improvement "
  "Program funds airfield projects from aviation trust fund dollars. "
  "Airports balance airlines, passengers, cargo, neighbors, and the "
  "environment — noise compatibility programs and deicing management "
  "among the eternal negotiations. They are economic engines and "
  "emergency lifelines in one.",
  "Airport operators maintain pavements, lighting, navigational aids, "
  "and terminals; ARFF crews stand ready; operations staff manage "
  "wildlife, snow, and security perimeters. Capital planning follows "
  "FAA-approved master plans and airport layout plans. AIP grants fund "
  "safety and capacity projects with local matches. Part 139 "
  "inspections audit compliance; self-inspection programs run daily. "
  "Noise programs insulate homes and buy easements where jets pass "
  "low.",
  ["City or authority owned; FAA regulated.",
   "Commercial airports need Part 139 certification.",
   "AIP funds airfield projects from aviation trust dollars.",
   "Balance airlines, passengers, cargo, neighbors, environment."],
  ["Part 139 airports must meet certification standards.",
   "Projects need FAA-approved layout plans.",
   "Wildlife hazard assessments are mandatory where required."],
  ["FAA Part 139 (14 CFR Part 139).",
   "FAA Advisory Circulars (design standards)."],
  ["Federal Aviation Administration - airport compliance and AIP.",
   "FAA Advisory Circular 150 series."],
  "In the Signature infrastructure system an airport is a sworn "
  "gateway: every runway a covenant of safe departure and return, "
  "every inspection a promise kept to passengers, every noise program "
  "a vow to neighbors.",
  {"repl_value_m": 500.0, "condition": 3, "age_y": 45, "design_life_y": 60}),

E("Seaports and Harbors", "Compounded", 16, "compounded",
  "Seaports are the nation's trade gates: publicly owned port "
  "authorities operating terminals, channels, cranes, and intermodal "
  "yards where ships meet trucks and trains. The Corps of Engineers "
  "maintains federal navigation channels by dredging; ports maintain "
  "berths and cargo facilities. Harbor Maintenance Tax funds channel "
  "work. Ports compete for cargo with deeper channels, bigger cranes, "
  "and faster turnarounds, while managing environmental duties — "
  "stormwater, air emissions, dredged-material disposal — and security "
  "under Coast Guard and CBP regimes. They anchor regional economies.",
  "Port authorities plan terminals, lease to terminal operators, and "
  "invest in cranes, pavement, and rail. The Corps dredges channels "
  "to authorized depths on cycles. Environmental permits govern "
  "dredging windows and disposal. Security plans control access and "
  "screen cargo per federal rules. Capital programs deepen channels, "
  "raise bridges, and expand yards; tariff schedules set the rates. "
  "Community mitigation addresses truck traffic and emissions.",
  ["Public port authorities operating trade terminals.",
   "Corps maintains federal channels by dredging.",
   "Harbor Maintenance Tax funds channel work.",
   "Balance cargo growth, environment, and security."],
  ["Channel work needs Corps authorization and permits.",
   "Security must meet Coast Guard facility rules.",
   "Dredging requires environmental permits and windows."],
  ["Rivers and Harbors Act authorities.",
   "Maritime Transportation Security Act of 2002."],
  ["U.S. Army Corps of Engineers - navigation program.",
   "American Association of Port Authorities - data."],
  "In the Signature infrastructure system a seaport is a sworn harbor: "
  "every dredged channel a covenant of open trade, every crane a "
  "promise of work, every secure berth a vow of safe passage.",
  {"repl_value_m": 800.0, "condition": 3, "age_y": 50, "design_life_y": 75}),

E("Public Transit: Bus Systems", "Compounded", 17, "compounded",
  "Bus systems are the workhorses of American transit: flexible, "
  "affordable, and everywhere. Transit agencies operate fixed routes, "
  "paratransit for riders with disabilities (required by the ADA), and "
  "often bus rapid transit with dedicated lanes and station-like stops. "
  "The Federal Transit Administration funds capital projects and "
  "oversees safety through state programs. Buses carry the majority "
  "of U.S. transit trips. Fleet electrification — battery buses "
  "replacing diesel — is the industry's great capital transition, "
  "with depots rewired for charging.",
  "Agencies plan routes by ridership and equity, schedule operators, "
  "and maintain fleets on mileage cycles. Dispatchers manage daily "
  "service; maintenance shops handle preventive work and overhauls. "
  "FTA grants fund buses and facilities with local matches; the "
  "Transit Asset Management rule requires condition reporting and "
  "investment prioritization. Paratransit eligibility and scheduling "
  "follow ADA rules. Electrification plans sequence bus purchases, "
  "charger installation, and workforce training.",
  ["Flexible backbone of American transit; majority of trips.",
   "ADA paratransit required alongside fixed routes.",
   "FTA funds capital; safety overseen by state programs.",
   "Fleet electrification is the great capital transition."],
  ["Paratransit must meet ADA complementary-service rules.",
   "Agencies must maintain transit asset management plans.",
   "Procurements follow Buy America requirements."],
  ["FTA Transit Asset Management rule (49 CFR 625).",
   "ADA transportation provisions (49 CFR Parts 37, 38)."],
  ["Federal Transit Administration - guidance and data.",
   "American Public Transportation Association - statistics."],
  "In the Signature infrastructure system a bus network is a sworn "
  "circulation: every route a covenant of access, every paratransit "
  "trip a promise that no rider is left behind.",
  {"repl_value_m": 120.0, "condition": 3, "age_y": 8, "design_life_y": 14}),

E("Public Transit: Rail Systems", "Compounded", 18, "compounded",
  "Rail transit — heavy rail subways, light rail, commuter rail, "
  "streetcars — moves masses on fixed guideways with unmatched "
  "capacity per corridor. Building it costs billions per mile for "
  "subways, far less for surface light rail; operating it demands "
  "track, signal, power, and vehicle maintenance at railroad "
  "discipline. The FTA's Capital Investment Grants program funds "
  "major expansions through rigorous project development. Safety is "
  "overseen by state safety agencies under FTA's state safety "
  "oversight rule, and commuter rail follows Federal Railroad "
  "Administration rules including positive train control.",
  "Agencies maintain track geometry, signals, traction power, and "
  "vehicles on strict cycles; deferred maintenance shows up as "
  "slow orders and breakdowns. Operations control centers dispatch "
  "trains and manage disruptions. Capital programs extend lines and "
  "renew systems under FTA grant agreements. Safety management "
  "systems identify hazards and track corrective actions. Positive "
  "train control enforces speed and separation on commuter rail. "
  "Ridership, reliability, and state of good repair are the reported "
  "vital signs.",
  ["Subways, light rail, commuter rail, streetcars.",
   "Highest capacity per corridor; highest capital cost.",
   "FTA Capital Investment Grants fund major expansions.",
   "Safety via state oversight; PTC on commuter rail."],
  ["Projects must complete FTA project development phases.",
   "State safety oversight programs are mandatory.",
   "Commuter rail must operate positive train control."],
  ["FTA State Safety Oversight rule (49 CFR 674).",
   "FRA positive train control rules (49 CFR 236)."],
  ["Federal Transit Administration - capital investment guidance.",
   "Federal Railroad Administration - safety rules."],
  "In the Signature infrastructure system rail is a sworn steel "
  "promise: every maintained mile a covenant of reliability, every "
  "signal a guardian of lives, every on-time arrival a kept vow.",
  {"repl_value_m": 2500.0, "condition": 3, "age_y": 35, "design_life_y": 60}),

E("Municipal Electric Distribution", "Compounded", 19, "compounded",
  "Municipal electric utilities — about 2,000 public power systems "
  "nationwide — own the poles, wires, transformers, and substations "
  "that deliver electricity within their cities. As distribution "
  "utilities they buy wholesale power and deliver it retail, or "
  "generate some themselves. Public power is locally governed, "
  "not-for-profit, and often delivers lower rates with high "
  "reliability. The assets age like all infrastructure: poles rot, "
  "transformers fail, and underground cable degrades. Storm "
  "hardening, vegetation management, and grid modernization — smart "
  "meters, automation, battery storage — define the capital program.",
  "Line crews build and maintain overhead and underground systems; "
  "substation technicians service breakers and transformers. "
  "Engineers plan capacity, protection, and reliability improvements. "
  "Vegetation crews trim on cycles to prevent outages. Outage "
  "management systems dispatch restoration by priority — hospitals "
  "and critical loads first. Rates are set by the local governing "
  "board to cover costs and fund capital. Reliability is tracked in "
  "SAIDI and SAIFI indices reported to regulators or boards.",
  ["~2,000 public power systems; locally governed, not-for-profit.",
   "Own poles, wires, transformers, substations.",
   "Often lower rates with high reliability.",
   "Capital focus: hardening, vegetation, grid modernization."],
  ["Construction must meet the National Electrical Safety Code.",
   "Rates must cover costs under local charter authority.",
   "Reliability indices should be tracked and reported."],
  ["National Electrical Safety Code (IEEE C2).",
   "State utility commission rules (where applicable)."],
  ["American Public Power Association - data and standards.",
   "Institute of Electrical and Electronics Engineers - NESC."],
  "In the Signature infrastructure system public power is a sworn "
  "current: every maintained feeder a covenant of light, every "
  "trimmed tree a promise against the storm, every restored outage "
  "a vow kept in the dark.",
  {"repl_value_m": 200.0, "condition": 3, "age_y": 30, "design_life_y": 45}),

E("Natural Gas Distribution Systems", "Compounded", 20, "compounded",
  "Natural gas distribution systems deliver gas from transmission "
  "pipelines to homes and businesses through networks of mains and "
  "service lines, most operated by investor-owned or municipal "
  "utilities under strict federal safety rules. The Pipeline and "
  "Hazardous Materials Safety Administration sets the standards; "
  "state commissions enforce them. Cast-iron and bare-steel mains — "
  "the legacy materials — are being replaced with plastic and "
  "protected steel nationwide, a multibillion-dollar safety program. "
  "Operators patrol for leaks, maintain cathodic protection against "
  "corrosion, and respond to odor calls as emergencies.",
  "Operators map every main and service, survey for leaks on "
  "cycles, and grade leaks for repair urgency. Corrosion crews "
  "maintain cathodic protection and coatings. Damage prevention — "
  "the 811 call-before-you-dig system — is the front line against "
  "third-party strikes. Integrity management programs assess high-"
  "consequence areas. Replacement programs prioritize leak-prone "
  "pipe. Emergency plans drill for major incidents; regulators "
  "audit compliance and can levy penalties.",
  ["Deliver gas from transmission pipelines to customers.",
   "Regulated by PHMSA; enforced by state commissions.",
   "Legacy cast-iron and bare-steel mains being replaced.",
   "Leak surveys, cathodic protection, 811 damage prevention."],
  ["Must comply with 49 CFR Part 192 pipeline safety rules.",
   "Integrity management required for covered segments.",
   "Replacement programs must target leak-prone materials."],
  ["Pipeline safety regulations (49 CFR Part 192).",
   "State public utility commission safety rules."],
  ["Pipeline and Hazardous Materials Safety Administration - rules.",
   "American Gas Association - safety guidance."],
  "In the Signature infrastructure system gas distribution is a "
  "sworn flame kept safe: every surveyed mile a covenant against "
  "leaks, every replaced main a promise of modern safety, every 811 "
  "ticket a vow to dig with care.",
  {"repl_value_m": 150.0, "condition": 3, "age_y": 40, "design_life_y": 60}),

E("Broadband and Fiber Networks", "Compounded", 21, "compounded",
  "Broadband networks are the newest public infrastructure: fiber "
  "optic cables delivering gigabit speeds to homes, schools, and "
  "businesses. Hundreds of cities, counties, and cooperatives have "
  "built municipal or open-access fiber networks where private "
  "providers would not, treating connectivity as a utility. Federal "
  "programs — BEAD, ReConnect, E-Rate — fund expansion to unserved "
  "areas. Fiber lasts decades once buried or hung, with electronics "
  "upgraded as speeds grow. The digital divide is the policy driver: "
  "work, school, and medicine now assume a connection.",
  "Network builders design fiber routes, hang or bury cable, splice "
  "fibers, and light the network with optical terminals. Open-access "
  "models lease fiber to competing providers; municipal retail "
  "models sell service directly. Take-rate — the share of passed "
  "homes subscribing — decides financial success. Grant programs "
  "require buildout milestones and speed commitments. Operations "
  "monitor uptime, repair cuts, and upgrade electronics as standards "
  "advance from gigabit to multi-gigabit.",
  ["Fiber networks delivering gigabit public connectivity.",
   "Hundreds of municipal, county, and cooperative builders.",
   "Federal BEAD and ReConnect funds target unserved areas.",
   "Fiber plant lasts decades; electronics upgrade with speeds."],
  ["Grant builds must meet program speed and milestone commitments.",
   "Pole attachments and rights-of-way need agreements.",
   "Networks should publish coverage and performance."],
  ["FCC broadband deployment program rules.",
   "State broadband office grant requirements."],
  ["Federal Communications Commission - broadband data.",
   "National Telecommunications and Information Administration - BEAD."],
  "In the Signature infrastructure system fiber is a sworn thread of "
  "light: every spliced strand a covenant of connection, every lit "
  "home a promise that distance from opportunity is closed.",
  {"repl_value_m": 35.0, "condition": 4, "age_y": 6, "design_life_y": 30}),

E("Fire Stations", "Compounded", 22, "compounded",
  "Fire stations are the ready-rooms of public safety: apparatus bays, "
  "living quarters, dispatch, and decontamination, positioned so crews "
  "reach emergencies within adopted response-time standards — often "
  "four to six minutes for first-due. Station location studies use "
  "travel-time modeling to place houses where the risk is. Modern "
  "stations add diesel exhaust capture, PFAS-aware gear cleaning, and "
  "gender-inclusive facilities. The building must survive the "
  "disasters it responds to: seismic and wind design exceed normal "
  "commercial standards. Apparatus — engines, ladders, rescues — are "
  "capital assets with 15-to-25-year lives.",
  "Fire departments plan station networks against standards of cover, "
  "build to essential-facility codes, and staff around the clock. "
  "Apparatus is specified, purchased, and maintained on rigorous "
  "preventive cycles; pump and aerial testing is annual. Stations "
  "need exhaust systems, gear extractors, and alerting tied to "
  "dispatch. Capital plans replace stations at 50-plus years and "
  "apparatus on schedule. Accreditation through CPSE validates "
  "operations against industry benchmarks.",
  ["Apparatus bays, quarters, dispatch — positioned for response times.",
   "Sited by travel-time modeling against standards of cover.",
   "Built as essential facilities to survive disasters.",
   "Apparatus are 15-to-25-year capital assets."],
  ["Location must meet adopted response-time standards.",
   "Construction must meet essential-facility seismic and wind codes.",
   "Apparatus must pass annual pump and aerial testing."],
  ["NFPA 1710/1720 (deployment standards).",
   "NFPA 1901 (apparatus standards)."],
  ["National Fire Protection Association - standards.",
   "Center for Public Safety Excellence - accreditation."],
  "In the Signature infrastructure system a fire station is a sworn "
  "watchpost: every bay door a covenant of readiness, every tested "
  "pump a promise of water under pressure, every crew a vow kept at "
  "3 a.m.",
  {"repl_value_m": 9.0, "condition": 3, "age_y": 35, "design_life_y": 60}),

E("Police Stations", "Compounded", 23, "compounded",
  "Police stations house patrol, investigations, dispatch, records, "
  "and holding — the operational core of law enforcement. Facilities "
  "must secure evidence rooms to chain-of-custody standards, protect "
  "dispatch centers as critical communications, and provide safe "
  "interview and detention areas. Many departments are consolidating "
  "into modern public safety buildings with 911 centers and emergency "
  "operations. Security design balances public access — lobbies must "
  "welcome — with hardened operations areas. Fleet, radio, and IT "
  "systems are the station's nervous system, refreshed on technology "
  "cycles.",
  "Police planners size facilities by staffing and function, design "
  "secure evidence and communications areas, and build to public-"
  "safety standards. Evidence custodians log every item under "
  "chain-of-custody rules. Dispatch centers need redundant power, "
  "communications, and staffing for peak loads. Fleet managers cycle "
  "patrol vehicles on mileage. IT maintains records systems under "
  "criminal-justice security policies. Accreditation through CALEA "
  "validates policy and practice.",
  ["House patrol, investigations, dispatch, records, holding.",
   "Evidence rooms held to chain-of-custody standards.",
   "Dispatch centers built as critical communications.",
   "Balance public welcome with operational security."],
  ["Evidence handling must meet chain-of-custody law.",
   "Detention areas must meet constitutional and code standards.",
   "Criminal-justice IT must meet CJIS security policy."],
  ["CALEA accreditation standards.",
   "FBI CJIS Security Policy."],
  ["Commission on Accreditation for Law Enforcement Agencies.",
   "Federal Bureau of Investigation - CJIS Security Policy."],
  "In the Signature infrastructure system a police station is a "
  "sworn precinct of order: every secured evidence locker a covenant "
  "of truth, every staffed dispatch console a promise of answer, "
  "every open lobby a vow of public trust.",
  {"repl_value_m": 14.0, "condition": 3, "age_y": 30, "design_life_y": 60}),

E("Public Hospitals", "Compounded", 24, "compounded",
  "Public hospitals — county, city, and district-owned — are the safety "
  "net of American medicine: trauma centers, burn units, and emergency "
  "departments that treat all comers regardless of ability to pay. "
  "They carry the heaviest uncompensated-care loads and often the "
  "most complex cases. As buildings they are among the most demanding "
  "assets: medical gas, emergency power, infection-control ventilation, "
  "and seismic resilience for essential facilities. Accreditation by "
  "The Joint Commission and CMS certification decide their survival; "
  "capital never stops, because medicine never stops advancing.",
  "Hospital operators maintain life-safety and clinical systems on "
  "relentless preventive schedules — generators tested monthly, "
  "medical gas verified, HVAC keeping pressure relationships that "
  "contain infection. Facility guidelines (FGI) govern design of new "
  "and renovated space. Capital planning prioritizes imaging, "
  "surgical suites, and bed towers. Emergency management plans cover "
  "surge, evacuation, and utility failure. Funding blends patient "
  "revenue, tax support, and federal disproportionate-share payments.",
  ["Safety-net medicine: trauma, burn, emergency care for all.",
   "Most demanding buildings: med gas, emergency power, infection control.",
   "Joint Commission accreditation and CMS certification required.",
   "Capital never stops; medicine never stops advancing."],
  ["Must meet CMS conditions of participation.",
   "Life-safety systems require NFPA 99 and 110 compliance.",
   "Construction must follow FGI design guidelines."],
  ["CMS Conditions of Participation (42 CFR 482).",
   "NFPA 99 (health care facilities)."],
  ["Centers for Medicare and Medicaid Services - hospital rules.",
   "Facility Guidelines Institute - design guidelines."],
  "In the Signature infrastructure system a public hospital is a "
  "sworn house of healing: every generator test a covenant of "
  "unbroken care, every trauma bay a promise of readiness, every "
  "treated patient a vow that no one is turned away.",
  {"repl_value_m": 400.0, "condition": 3, "age_y": 38, "design_life_y": 60}),

# ---------------- ADVANCED 25-34 ----------------

E("Public Schools as Infrastructure", "Advanced", 25, "advanced",
  "Public school buildings are among the largest public asset "
  "portfolios: tens of thousands of schools housing 50 million "
  "students, with roofs, HVAC, and safety systems on relentless "
  "clocks. The average American school building is decades old; "
  "national estimates of needed repairs run into the hundreds of "
  "billions. Districts plan by enrollment projections, assess "
  "facility condition, and fund construction through bonds voters "
  "approve. Healthy, safe buildings — ventilation, lead-free water, "
  "secure entries — are increasingly understood as learning "
  "conditions, not just maintenance.",
  "Districts inventory buildings and systems, assess condition, and "
  "project enrollment by attendance zone. Bond programs fund new "
  "construction and major renovation after voter approval; operating "
  "budgets handle maintenance. Design follows state school facility "
  "standards and codes, with security vestibules and storm "
  "shelters where required. Indoor air quality, water testing, and "
  "playground safety run on schedules. Long-range facility plans "
  "align buildings with demography for decades.",
  ["Tens of thousands of schools; ~50 million students.",
   "Average building decades old; repair needs in the hundreds of billions.",
   "Funded largely by voter-approved bonds.",
   "Healthy buildings understood as learning conditions."],
  ["Construction must meet state school facility standards.",
   "Bonds require voter approval and disclosed project lists.",
   "Water, air, and safety testing must follow schedules."],
  ["State school facility program standards.",
   "State building and fire codes for educational occupancies."],
  ["National Council on School Facilities - data.",
   "U.S. Government Accountability Office - school facilities reports."],
  "In the Signature infrastructure system a school is a sworn house "
  "of learning: every sound roof a covenant of shelter for young "
  "minds, every clean air system a promise of clear thought, every "
  "bond a vow the community makes to its children.",
  {"repl_value_m": 35.0, "condition": 2, "age_y": 55, "design_life_y": 60}),

E("Public Libraries", "Advanced", 26, "advanced",
  "Public libraries are the most used civic buildings in America: "
  "books, internet access, children's programs, job help, and "
  "refuge — visited hundreds of millions of times a year. As "
  "assets they blend historic Carnegie buildings with modern "
  "branches: collections space, meeting rooms, makerspaces, and "
  "the technology commons. Capital needs run to HVAC for "
  "preservation, accessibility retrofits, and the endless refresh "
  "of public computers. Libraries are funded by local taxes, "
  "often with dedicated levies voters renew, and increasingly "
  "serve as cooling centers, polling places, and disaster "
  "information hubs.",
  "Library directors plan branches by service area, assess "
  "facility condition, and program capital for renovation and "
  "replacement. Collections are weeded and refreshed; technology "
  "is replaced on cycles. Meeting rooms and makerspaces need "
  "flexible design. Accessibility upgrades follow ADA transition "
  "plans. Funding campaigns pair tax levies with foundation "
  "gifts. Usage statistics — visits, circulation, program "
  "attendance, computer sessions — justify every dollar.",
  ["Most used civic buildings: books, internet, programs, refuge.",
   "Blend historic and modern branches.",
   "Capital needs: HVAC, accessibility, technology refresh.",
   "Serve as cooling centers, polling places, disaster hubs."],
  ["Facilities must meet ADA and building codes.",
   "Collections need preservation environments.",
   "Levies require voter approval with accountability."],
  ["State library construction standards (where adopted).",
   "ADA Standards for Accessible Design."],
  ["American Library Association - data and standards.",
   "Institute of Museum and Library Services - statistics."],
  "In the Signature infrastructure system a library is a sworn house of open "
  "knowledge: every shelf a covenant of free learning, every "
  "computer a promise of connection, every open door a vow to all.",
  {"repl_value_m": 10.0, "condition": 3, "age_y": 45, "design_life_y": 60}),

E("Courthouses and Civic Buildings", "Advanced", 27, "advanced",
  "Courthouses are where the justice system lives: courtrooms, "
  "jury facilities, judges' chambers, clerk offices, and holding — "
  "designed for dignity, security, and the separation of judges, "
  "juries, the public, and the accused. The U.S. Courts Design "
  "Guide sets federal standards; states publish their own. Historic "
  "courthouses anchor town squares while straining under modern "
  "security and technology demands. Civic buildings — city halls "
  "and administration centers — carry the parallel duty of housing "
  "democracy's daily work visibly and accessibly.",
  "Court administrators program space by caseload, design "
  "circulation separating participant groups, and build to "
  "security standards with screening, holding, and duress systems. "
  "Historic courthouses are renovated under preservation standards "
  "while adding accessibility and technology. Capital planning "
  "prioritizes life safety, security, and courtroom adequacy. "
  "Operations maintain the buildings' dignity — because a "
  "courtroom's condition speaks to the justice within.",
  ["Courtrooms, chambers, clerk, holding — designed for dignity and security.",
   "Separate circulation for judges, juries, public, accused.",
   "Federal design guided by the U.S. Courts Design Guide.",
   "Historic courthouses anchor civic life."],
  ["Design must meet court security standards.",
   "Historic renovations follow preservation standards.",
   "Facilities must be accessible under the ADA."],
  ["U.S. Courts Design Guide.",
   "Secretary of the Interior's Standards for Rehabilitation."],
  ["Administrative Office of the U.S. Courts - design guide.",
   "National Center for State Courts - facilities guidance."],
  "In the Signature infrastructure system a courthouse is a sworn "
  "hall of justice: every courtroom a covenant of fair hearing, "
  "every secure corridor a promise of safety, every preserved "
  "facade a vow that law endures.",
  {"repl_value_m": 60.0, "condition": 3, "age_y": 70, "design_life_y": 100}),

E("ISO 55000 Asset Management", "Advanced", 28, "advanced",
  "ISO 55000 is the international standard for managing physical "
  "assets: the disciplined system by which organizations extract "
  "maximum value from infrastructure across its life. It requires "
  "an asset management policy, strategic asset management plan, "
  "defined roles, risk-based decision-making, and continual "
  "improvement — the plan-do-check-act cycle applied to bridges, "
  "pipes, and buildings. Utilities, transit agencies, and cities "
  "adopt it to defend budgets with data, align maintenance with "
  "service levels, and prove stewardship to boards and bond "
  "holders. Certification audits test whether the system is real "
  "or paper.",
  "The organization inventories assets, assesses condition and "
  "criticality, defines levels of service, and models lifecycle "
  "costs and risks. The strategic plan sets objectives; asset "
  "management plans detail interventions by asset class. "
  "Decision-making balances cost, risk, and performance. "
  "Information systems hold the data; competence programs train "
  "the people. Internal audits and management review drive "
  "improvement. Certification bodies audit against ISO 55001's "
  "requirements.",
  ["International standard for physical asset management.",
   "Requires policy, strategic plan, risk-based decisions, improvement.",
   "Applies plan-do-check-act to infrastructure.",
   "Certification audits test whether the system is real."],
  ["Asset registers must be complete and current.",
   "Decisions must balance cost, risk, and performance.",
   "Continual improvement must be demonstrated."],
  ["ISO 55000:2014 (overview and principles).",
   "ISO 55001:2014 (requirements).",
   "ISO 55002:2018 (guidelines)."],
  ["International Organization for Standardization - ISO 55000 series.",
   "Institute of Asset Management - guidance."],
  "In the Signature infrastructure system ISO 55000 is the sworn "
  "discipline of stewardship: every inventoried asset a named "
  "charge, every risk-based decision a covenant of wisdom, every "
  "audit a promise that stewardship is real.",
  {"repl_value_m": 0.5, "condition": 4, "age_y": 5, "design_life_y": 20}),

E("Pavement Condition Rating (PASER)", "Advanced", 29, "advanced",
  "PASER — Pavement Surface Evaluation and Rating — is the visual "
  "rating system that lets a trained eye score a road's condition "
  "from 10 (excellent) to 1 (failed). Developed by the University "
  "of Wisconsin's Transportation Information Center, it is the "
  "lingua franca of local road management: raters walk or drive "
  "each segment, note distresses — cracking, rutting, raveling, "
  "patches — and assign the number that triggers the right "
  "treatment. Tens of thousands of local officials have been "
  "trained in it. The rating feeds pavement management systems "
  "that schedule seals, overlays, and reconstruction at the "
  "cheapest point in the deterioration curve.",
  "Certified raters survey the network on cycles, recording "
  "distress types and severity per PASER manuals for asphalt, "
  "concrete, and gravel. Ratings enter the pavement management "
  "database with segment history. Engineers set treatment "
  "triggers — 8s get crack seal, 5s get overlay, 2s get "
  "reconstruction — and model network condition under budget "
  "scenarios. Quality control re-rates samples for consistency. "
  "The data justifies budgets to councils with maps anyone can "
  "read.",
  ["Visual 10-to-1 rating of pavement condition.",
   "Developed by UW-Madison Transportation Information Center.",
   "Lingua franca of local road management.",
   "Triggers the right treatment at the cheapest point."],
  ["Raters should be trained and certified.",
   "Networks should be rated on regular cycles.",
   "Ratings must feed treatment decisions, not sit in files."],
  ["PASER manuals (asphalt, concrete, gravel).",
   "ASTM D6433 (Pavement Condition Index, related practice)."],
  ["University of Wisconsin Transportation Information Center - PASER.",
   "ASTM D6433."],
  "In the Signature infrastructure system PASER is the sworn eye "
  "on the road: every rating an honest number, every treatment "
  "trigger a covenant of timely care, every resurfaced mile a "
  "promise renewed.",
  {"repl_value_m": 3.0, "condition": 3, "age_y": 12, "design_life_y": 25}),

E("National Bridge Inspection Standards (NBIS)", "Advanced", 30, "advanced",
  "The National Bridge Inspection Standards are the federal rules "
  "that keep America's bridges watched: qualifications for "
  "inspectors, inspection intervals, and the 0–9 condition ratings "
  "that feed the National Bridge Inventory. Born after the 1967 "
  "Silver Bridge collapse killed 46 people, the standards require "
  "routine inspection at least every 24 months, with fracture-"
  "critical, underwater, and damage inspections on their own "
  "schedules. States report to the FHWA; the data drives billions "
  "in federal bridge funding. The standards were substantially "
  "updated in 2022 to modernize risk-based inspection.",
  "Program managers qualify team leaders, schedule inspections by "
  "interval and risk, and ensure hands-on access to fracture-"
  "critical members and underwater elements. Inspectors rate deck, "
  "superstructure, substructure, and culvert; code appraisal and "
  "load ratings; and flag critical findings for immediate action. "
  "States submit inventory data annually. Risk-based intervals now "
  "let the best bridges go longer and focus effort on the worst. "
  "FHWA reviews state programs for compliance.",
  ["Federal rules for bridge inspection since the 1967 Silver Bridge collapse.",
   "Routine inspection at least every 24 months; 0-9 ratings.",
   "Feeds the National Bridge Inventory and federal funding.",
   "2022 update modernized risk-based intervals."],
  ["Inspectors must meet NBIS qualification requirements.",
   "Critical findings require immediate action and reporting.",
   "States must submit inventory data annually."],
  ["National Bridge Inspection Standards (23 CFR 650 Subpart C).",
   "FHWA Bridge Inspector's Reference Manual."],
  ["Federal Highway Administration - NBIS.",
   "23 CFR 650 Subpart C (2022 update)."],
  "In the Signature infrastructure system NBIS is the sworn watch "
  "over every span: every inspection a covenant born of tragedy, "
  "every rating an honest measure, every critical finding an alarm "
  "that must be answered.",
  {"repl_value_m": 8.0, "condition": 3, "age_y": 42, "design_life_y": 75}),

E("Lifecycle Cost Analysis", "Advanced", 31, "advanced",
  "Lifecycle cost analysis counts the whole price of infrastructure: "
  "design, construction, operation, maintenance, rehabilitation, and "
  "disposal — discounted to today's dollars. It is how engineers "
  "prove that the cheaper bid can be the expensive choice: a pavement "
  "that costs more to build but needs no overlay for 20 years often "
  "wins on lifecycle cost. FHWA requires it for major highway "
  "projects; transit and water utilities use it to compare "
  "alternatives. The analysis forces honesty about maintenance — "
  "the costs politicians prefer to ignore — by putting them in the "
  "decision.",
  "Analysts define alternatives, estimate agency and user costs over "
  "the analysis period, apply discount rates, and model deterioration "
  "and maintenance timing. Probabilistic analysis handles "
  "uncertainty in costs and lives. User costs — delay, crashes, "
  "vehicle wear — often dominate. Results compare net present values; "
  "sensitivity tests show which assumptions matter. Decision-makers "
  "choose the alternative with the lowest lifecycle cost that meets "
  "performance needs, and the analysis becomes part of the project "
  "record.",
  ["Counts design through disposal, discounted to present value.",
   "Proves the cheaper bid can be the expensive choice.",
   "Required by FHWA for major highway projects.",
   "Forces honesty about future maintenance costs."],
  ["Alternatives must be compared over a common analysis period.",
   "Costs must include agency, user, and maintenance streams.",
   "Assumptions must be documented and sensitivity-tested."],
  ["FHWA Life-Cycle Cost Analysis guidance.",
   "ASTM E917 (lifecycle costing practice)."],
  ["Federal Highway Administration - LCCA primer.",
   "ASTM E917."],
  "In the Signature infrastructure system lifecycle costing is the "
  "sworn arithmetic of honesty: every future maintenance dollar "
  "counted today, every cheap bid weighed against its true price, "
  "every decision a covenant with the taxpayers of tomorrow.",
  {"repl_value_m": 0.2, "condition": 4, "age_y": 3, "design_life_y": 15}),

E("Capital Improvement Planning", "Advanced", 32, "advanced",
  "Capital improvement planning is how governments schedule big "
  "investments: the multi-year program — typically five or six years — "
  "listing every major project, its cost, its funding, and its year. "
  "The CIP translates master plans and condition assessments into a "
  "funded queue: this year's water main replacements, next year's "
  "fire station, the road program's rolling horizon. It forces the "
  "hard conversation — needs always exceed money — into public view, "
  "ranked by criteria councils adopt. Bond issues, grants, and rates "
  "are sized to the plan, not to wishes.",
  "Departments submit project requests with scopes, costs, and "
  "justifications. Finance and engineering score them against "
  "adopted criteria — condition, safety, growth, mandates — and "
  "build the funded program within revenue forecasts. The council "
  "adopts the CIP after public hearings; the first year becomes the "
  "capital budget. Project managers deliver, reporting cost and "
  "schedule. Annual updates roll the horizon forward, adjusting for "
  "completed work, new needs, and changed revenues.",
  ["Multi-year program of major projects, costs, funding, timing.",
   "Translates plans and assessments into a funded queue.",
   "Forces needs-vs-money into public view.",
   "Bond issues and rates sized to the plan."],
  ["Projects need scopes, cost estimates, and funding sources.",
   "Adoption requires public hearings.",
   "Annual updates must roll the horizon forward."],
  ["GFOA capital planning best practices.",
   "State local-government budget laws."],
  ["Government Finance Officers Association - capital planning guidance.",
   "State municipal budget statutes."],
  "In the Signature infrastructure system the CIP is the sworn "
  "promise of building: every listed project a covenant of intent, "
  "every funded year a vow kept, every public hearing an open "
  "accounting of what will rise and when.",
  {"repl_value_m": 250.0, "condition": 4, "age_y": 2, "design_life_y": 10}),

E("GIS Asset Inventories", "Advanced", 33, "advanced",
  "GIS asset inventories are the digital twin of everything a "
  "government owns in the ground and on it: every hydrant, valve, "
  "manhole, sign, pole, and pipe drawn as a feature with attributes "
  "— material, size, install date, condition, maintenance history. "
  "Built from as-builts, field GPS, and records research, the "
  "inventory feeds work-order systems, capital planning, and "
  "emergency response: the fire crew sees the hydrants, the engineer "
  "sees the pipe ages, the finance director sees the replacement "
  "liability. Data quality — completeness, accuracy, currency — is "
  "the eternal battle, won by field verification and disciplined "
  "as-built submittals.",
  "GIS staff build the inventory from record drawings and field "
  "collection, snapping features to control and attributing from "
  "records. Mobile apps let crews update condition and add assets "
  "in the field. Integration with work management ties every work "
  "order to the asset. Data stewards run completeness and accuracy "
  "audits; contractors submit as-builts in GIS-ready formats. "
  "Dashboards report inventory health; capital models consume age "
  "and condition to forecast renewal needs.",
  ["Digital twin of every owned asset with attributes.",
   "Feeds work orders, capital planning, emergency response.",
   "Built from as-builts, field GPS, records research.",
   "Data quality is the eternal battle."],
  ["Inventories must be complete, accurate, and current.",
   "Contractors must submit GIS-ready as-builts.",
   "Integration with work management is required."],
  ["FGDC metadata and data standards.",
   "NASSCO PACP/MACP/LACP (pipe assessment coding)."],
  ["Federal Geographic Data Committee - standards.",
   "NASSCO - pipeline assessment standards."],
  "In the Signature infrastructure system the asset inventory is "
  "the sworn census of works: every hydrant named, every pipe "
  "aged honestly, every work order a covenant recorded against "
  "its asset.",
  {"repl_value_m": 2.0, "condition": 4, "age_y": 4, "design_life_y": 20}),

E("Infrastructure Resilience and Climate Adaptation", "Advanced", 34, "advanced",
  "Infrastructure resilience is the capacity to take a hit and keep "
  "serving: to resist, absorb, recover from, and adapt to floods, "
  "heat, fire, and storms that are growing more severe. Adaptation "
  "hardens assets — elevating substations, upsizing culverts, "
  "burying lines, cooling shelters — and redesigns systems for the "
  "future climate, not the past's. Federal programs from FEMA's "
  "BRIC grants to DOT's PROTECT fund resilience projects; rating "
  "systems like Envision certify sustainable infrastructure. The "
  "cheapest resilience is built in at design; the most expensive is "
  "rebuilt after failure.",
  "Planners assess vulnerability: which assets face which hazards "
  "at what probability and consequence. Engineers design to future "
  "conditions — higher flood elevations, hotter temperatures — using "
  "downscaled climate projections. Benefit-cost analysis, with FEMA "
  "methodologies, justifies mitigation grants. Operations write "
  "continuity plans: backup power, alternate routes, mutual aid. "
  "After events, build-back-better policies upgrade rather than "
  "merely replace. Performance is measured in avoided losses and "
  "recovery time.",
  ["Capacity to resist, absorb, recover, and adapt.",
   "Hardens assets and redesigns for future climate.",
   "Federal BRIC and PROTECT programs fund projects.",
   "Cheapest resilience is built in at design."],
  ["Vulnerability assessments must use best-available climate science.",
   "Mitigation grants require benefit-cost justification.",
   "Critical facilities need continuity and recovery plans."],
  ["FEMA BRIC program requirements.",
   "Envision sustainable infrastructure framework."],
  ["Federal Emergency Management Agency - BRIC guidance.",
   "Institute for Sustainable Infrastructure - Envision."],
  "In the Signature infrastructure system resilience is the sworn "
  "readiness: every hardened asset a covenant with the future, "
  "every adaptation a promise that the storm will find the city "
  "prepared, every recovery a vow to build back better.",
  {"repl_value_m": 90.0, "condition": 3, "age_y": 15, "design_life_y": 50}),
]
