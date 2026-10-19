#!/usr/bin/env python3
"""Entries for the Humanitarian Disaster Relief databases (2026-10-17).

34 relief topics, ladder-ordered 1-34
(foundations 1-12 / compounded 13-24 / advanced 25-34).
Public = real, fact-checked domain data. Signature = Signature relief
interpretation, titles suffixed " (Signature Edition)".
No website references. No Facebook.
"""


def E(name, group, rank, tier, description, how, key_points, requirements,
      standards, citations, sig_lens, demo_data, demo_key="relief"):
    return {"name": name, "group": group, "ladder_rank": rank,
            "ladder_tier": tier, "description": description,
            "how_it_works": how, "key_points": key_points,
            "requirements": requirements, "standards": standards,
            "citations": citations, "sig_lens": sig_lens,
            "demo_key": demo_key, "demo_data": demo_data}


ENTRIES = [

# ---------------- FOUNDATIONS 1-12 ----------------

E("Disaster Declaration Process", "Foundations", 1, "foundations",
  "The disaster declaration process is the formal sequence that "
  "unlocks government aid: local emergency proclamations, state "
  "declarations by the governor, and — for major disasters — a "
  "presidential declaration under the Stafford Act. The governor's "
  "request goes to the President through FEMA, with preliminary "
  "damage assessments documenting unmet needs beyond state and "
  "local capacity. A presidential declaration opens Individual "
  "Assistance for survivors and Public Assistance for governments, "
  "plus hazard mitigation funding. Without the declaration, "
  "federal disaster dollars do not flow — the paperwork is the "
  "gateway to the rescue.",
  "Local officials proclaim emergencies to activate local powers "
  "and mutual aid. The state emergency management agency conducts "
  "preliminary damage assessments with FEMA, documenting impacts "
  "against per-capita and statewide indicators. The governor "
  "requests a declaration specifying the needed programs. The "
  "President declares — or denies — designating affected counties "
  "and assistance types. FEMA then opens application channels: "
  "disaster assistance registration for individuals, applicant "
  "briefings for governments. Denials can be appealed with new "
  "data.",
  ["Local, state, then presidential declarations unlock aid.",
   "Governor requests through FEMA with damage assessments.",
   "Presidential declaration opens Individual and Public Assistance.",
   "No declaration, no federal disaster dollars."],
  ["Requests need documented damage beyond local capacity.",
   "Preliminary assessments must support the request.",
   "Designations specify counties and assistance types."],
  ["Robert T. Stafford Disaster Relief and Emergency Assistance Act.",
   "FEMA declaration regulations (44 CFR Part 206)."],
  ["Federal Emergency Management Agency - declaration guidance.",
   "Stafford Act, 42 U.S.C. 5121."],
  "In the Signature relief system a declaration is a sworn "
  "summons: every assessed damage a covenant of truth, every "
  "designated county a promise that help is officially coming.",
  {"people": 50000, "supply_tons": 1200, "days": 30}),

E("Emergency Operations Centers (EOC)", "Foundations", 2, "foundations",
  "Emergency Operations Centers are the brains of disaster "
  "response: the rooms — physical or virtual — where agencies "
  "coordinate. The EOC does not command field units; it "
  "supports them, gathering information, setting priorities, "
  "allocating resources, and speaking with one voice to the "
  "public. EOCs activate at levels matching the incident, from "
  "a watch desk to full staffing around the clock. Inside, "
  "sections mirror the Incident Command System: operations, "
  "planning, logistics, finance. The EOC's common operating "
  "picture — the shared map of what is happening — is its most "
  "precious product.",
  "Agencies staff the EOC by emergency plans when activation "
  "criteria are met. The planning section builds situation "
  "reports and incident action plans; operations coordinates "
  "missions; logistics orders resources; finance tracks costs "
  "for reimbursement. Information flows in from field units, "
  "dispatch, and the public; decisions and public messages "
  "flow out. Demobilization returns staff as the incident "
  "winds down. After-action reviews capture lessons.",
  ["Coordination hub supporting — not commanding — field response.",
   "Gathers information, sets priorities, allocates resources.",
   "Sections mirror ICS: operations, planning, logistics, finance.",
   "Common operating picture is the most precious product."],
  ["Activation must follow plan criteria.",
   "Staff need ICS training and position credentials.",
   "Costs must be tracked for reimbursement."],
  ["FEMA Emergency Operations Center guidance.",
   "National Incident Management System (NIMS)."],
  ["Federal Emergency Management Agency - EOC guidance.",
   "FEMA National Incident Management System."],
  "In the Signature relief system the EOC is a sworn "
  "watchtower: every situation report a covenant of shared "
  "truth, every allocated resource a promise sent where "
  "needed most.",
  {"people": 200000, "supply_tons": 5000, "days": 14}),

E("Incident Command System (ICS)", "Foundations", 3, "foundations",
  "The Incident Command System is America's standard for running "
  "emergencies: one incident commander, modular sections, "
  "manageable spans of control, and common terminology so "
  "firefighters, police, medics, and volunteers work as one. "
  "Born from California wildfire chaos in the 1970s, ICS is now "
  "required for federal preparedness funding nationwide. It "
  "expands and contracts with the incident — a car crash needs "
  "a commander and a few units; a hurricane needs the full "
  "organization. Unified command lets multiple agencies share "
  "leadership without surrendering authority. ICS is the grammar "
  "of disaster response.",
  "The first responder establishes command, names the incident, "
  "and sets objectives. The command staff — safety, liaison, "
  "public information — supports; the general staff runs "
  "operations, planning, logistics, and finance. Each "
  "operational period produces an incident action plan with "
  "objectives, assignments, and communications. Span of control "
  "stays at three to seven subordinates. Transfer of command "
  "briefs the incoming commander fully. Demobilization releases "
  "resources systematically.",
  ["Standard system: one commander, modular sections, common terms.",
   "Born of 1970s wildfires; required for federal funding.",
   "Expands and contracts with the incident.",
   "Unified command shares leadership across agencies."],
  ["Responders need ICS training (100, 200, 700, 800 series).",
   "Span of control must stay manageable.",
   "Incident action plans required each operational period."],
  ["National Incident Management System.",
   "FEMA ICS training standards."],
  ["Federal Emergency Management Agency - ICS and NIMS.",
   "FIRESCOPE history (California)."],
  "In the Signature relief system ICS is a sworn order of "
  "battle against chaos: every clear objective a covenant of "
  "purpose, every manageable span a promise that no one is "
  "overwhelmed.",
  {"people": 100000, "supply_tons": 2500, "days": 21}),

E("Search and Rescue Operations", "Foundations", 4, "foundations",
  "Search and rescue is the race against time after disaster: "
  "finding the trapped, the lost, and the missing. Urban search "
  "and rescue teams — like FEMA's 28 national task forces — cut "
  "through collapsed buildings with engineers, medics, and "
  "canine teams. Swiftwater teams work floods; wilderness teams "
  "work the backcountry; the Coast Guard works the seas. The "
  "golden hours decide survival: most live rescues happen in "
  "the first day. Operations run on probabilities — searching "
  "the most likely places first — and end only when hope is "
  "mathematically exhausted.",
  "Incident command assigns search sectors by probability; "
  "teams grid them with canines, cameras, listening devices, "
  "and drones. Structural engineers assess collapse stability "
  "before entry. Medics stabilize the found; coroners handle "
  "the lost. Air assets and boats extend reach. Families get "
  "a missing-persons process with dignity. Demobilization "
  "follows when probability of live find drops below "
  "thresholds — the hardest decision in rescue.",
  ["Race against time: most live rescues in the first day.",
   "USAR task forces, swiftwater, wilderness, Coast Guard teams.",
   "Search by probability: most likely places first.",
   "Engineers, medics, canines work as one."],
  ["Teams need typed credentials and training.",
   "Structural assessment must precede collapse entry.",
   "Operations follow incident command."],
  ["FEMA USAR program standards.",
   "National Search and Rescue Plan."],
  ["Federal Emergency Management Agency - USAR.",
   "U.S. Coast Guard search and rescue doctrine."],
  "In the Signature relief system search and rescue is a sworn "
  "hunt for life: every gridded sector a covenant of "
  "thoroughness, every canine alert a promise of hope, every "
  "found survivor a vow fulfilled.",
  {"people": 5000, "supply_tons": 50, "days": 7}),

E("Emergency Sheltering", "Foundations", 5, "foundations",
  "Emergency sheltering gives displaced people a roof tonight: "
  "congregate shelters in schools and gyms, run to Red Cross "
  "standards with cots, meals, medical, and security. Shelters "
  "open by plan when evacuations or damage displace residents, "
  "staffed by trained workers and volunteers. The best "
  "sheltering keeps families together, accommodates disabilities "
  "and medical needs, welcomes pets in co-located areas, and "
  "protects dignity with privacy and quiet hours. Sheltering "
  "is the most human of logistics — a stranger's gym becomes "
  "a neighborhood.",
  "Emergency management designates shelter sites in plans; the "
  "Red Cross or the jurisdiction opens them on trigger. Staff "
  "register residents, assign cots by family, and provide meals, "
  "showers, medical screening, and information. Functional-needs "
  "support — power for devices, accessible cots, sign language "
  "— is built in. Security keeps order; mental-health teams "
  "circulate. Demobilization returns buildings as residents "
  "transition to temporary housing.",
  ["Congregate shelters: cots, meals, medical, security.",
   "Open by plan on evacuation or damage triggers.",
   "Accommodate disabilities, medical needs, pets.",
   "Protect dignity: privacy, quiet hours, family unity."],
  ["Shelters must meet Red Cross shelter standards.",
   "ADA functional-needs support required.",
   "Sites need agreements before disaster."],
  ["American Red Cross shelter standards.",
   "FEMA mass care guidance; ADA requirements."],
  ["American Red Cross - sheltering standards.",
   "Federal Emergency Management Agency - mass care."],
  "In the Signature relief system a shelter is a sworn haven: "
  "every cot a covenant of rest, every hot meal a promise of "
  "care, every kept family together a vow of humanity.",
  {"people": 20000, "supply_tons": 800, "days": 21}),

E("Mass Feeding Operations", "Foundations", 6, "foundations",
  "Mass feeding puts hot meals in survivors' hands when kitchens "
  "are dark: mobile kitchens, fixed feeding sites, and food "
  "distribution, scaled from hundreds to hundreds of thousands "
  "of meals a day. Voluntary organizations — the Red Cross, "
  "Salvation Army, Southern Baptist Disaster Relief — lead "
  "under government coordination, with the Emergency Management "
  "Assistance Compact and federal mission assignments funding "
  "the surge. Feeding sites locate near shelters and damaged "
  "neighborhoods; dietary needs — infant, medical, cultural — "
  "are planned for. A hot meal is logistics, dignity, and morale "
  "in one tray.",
  "Emergency management estimates feeding need from shelter "
  "populations and damage; voluntary agencies deploy kitchens "
  "and canteens. Sites are set with food safety, traffic, and "
  "accessibility in mind. Health departments inspect field "
  "kitchens. Supply chains move bulk food, water, and ice. "
  "Daily counts track meals served against need; demobilization "
  "follows as power and kitchens return.",
  ["Hot meals when home kitchens are dark.",
   "Voluntary agencies lead under government coordination.",
   "Scaled from hundreds to hundreds of thousands daily.",
   "Dietary needs planned: infant, medical, cultural."],
  ["Field kitchens need health department approval.",
   "Food safety standards apply in the field.",
   "Sites must be accessible."],
  ["FEMA mass care feeding guidance.",
   "FDA Food Code (field application); state health rules."],
  ["American Red Cross / Salvation Army feeding doctrine.",
   "Federal Emergency Management Agency - mass care."],
  "In the Signature relief system mass feeding is a sworn "
  "table: every hot tray a covenant of nourishment, every "
  "served dietary need a promise of respect, every counted "
  "meal a vow that no one is forgotten.",
  {"people": 30000, "supply_tons": 1500, "days": 30}),

E("Emergency First Aid Stations", "Foundations", 7, "foundations",
  "Emergency first aid stations treat the walking wounded of "
  "disaster: the cuts, sprains, and crush injuries that flood "
  "in after the shaking stops. Set up near shelters, search "
  "areas, and distribution points, they triage with the "
  "START system — sorting the immediate, delayed, minor, and "
  "expectant — and stabilize for transport to hospitals. "
  "Staffed by EMTs, nurses, and physicians, often volunteers "
  "through Medical Reserve Corps, they keep minor injuries "
  "from becoming emergencies and hospitals from drowning. "
  "Tetanus shots, wound cleaning, and chronic-disease "
  "medication refills are the quiet lifesavers.",
  "Medical planners site stations by casualty estimates; "
  "teams deploy with kits, cots, and communications. Triage "
  "officers sort arrivals; treatment teams stabilize; "
  "transport coordinators move the critical to hospitals. "
  "Pharmacies dispense refills for the displaced chronically "
  "ill. Patient tracking follows the displaced through the "
  "system. Demobilization comes as hospitals and clinics "
  "recover.",
  ["Treat the walking wounded near shelters and search areas.",
   "Triage by START: immediate, delayed, minor, expectant.",
   "Stabilize and transport the critical.",
   "Quiet lifesavers: tetanus, wound care, medication refills."],
  ["Staff need medical credentials and disaster training.",
   "Triage must follow adopted protocols.",
   "Patient tracking required."],
  ["START triage protocol.",
   "State EMS and medical volunteer regulations."],
  ["Medical Reserve Corps guidance.",
   "START triage (Hoag Hospital/Newport Beach)."],
  "In the Signature relief system a first aid station is a "
  "sworn triage: every sorted patient a covenant of order in "
  "chaos, every stabilized wound a promise of onward care.",
  {"people": 15000, "supply_tons": 120, "days": 14}),

E("Evacuation Planning", "Foundations", 8, "foundations",
  "Evacuation planning moves people out of harm's way before "
  "disaster strikes: zones mapped by hazard, routes sized by "
  "population, and triggers tied to forecasts. Hurricane zones "
  "follow storm surge maps; wildfire plans follow fuel and "
  "wind; dam plans follow inundation maps. Plans address the "
  "hard parts — carless households, nursing homes, hospitals, "
  "pets, and contraflow lanes that turn highways one-way "
  "outbound. Public messaging must be early, clear, and "
  "multilingual: the order means go now. Re-entry planning "
  "brings people home safely in phases.",
  "Planners model clearance times — how long the last car "
  "takes to reach safety — and set zone triggers from "
  "forecasts. Transportation departments plan contraflow and "
  "fuel; transit agencies move the carless; health "
  "departments move facilities. Alerts go through IPAWS, "
  "media, and door-knockers. Shelters open ahead of the "
  "order. Law enforcement secures evacuated areas. Re-entry "
  "tiers return residents, then businesses, with damage "
  "assessments guiding the phases.",
  ["Move people out before disaster strikes.",
   "Zones by hazard; routes sized by population.",
   "Address carless, facilities, pets, contraflow.",
   "Orders must be early, clear, multilingual."],
  ["Plans need modeled clearance times.",
   "Functional-needs populations must be planned for.",
   "Re-entry must be phased and communicated."],
  ["FEMA evacuation planning guidance.",
   "State emergency management statutes."],
  ["Federal Emergency Management Agency - evacuation guidance.",
   "Transportation Research Board - evacuation modeling."],
  "In the Signature relief system evacuation is a sworn "
  "exodus: every mapped zone a covenant of foresight, every "
  "contraflow lane a promise of passage, every returned "
  "resident a vow of homecoming.",
  {"people": 250000, "supply_tons": 3000, "days": 5}),

E("Emergency Alert Systems (WEA/IPAWS)", "Foundations", 9, "foundations",
  "The Integrated Public Alert and Warning System is how "
  "America shouts danger: Wireless Emergency Alerts that "
  "buzz every phone in a polygon, the Emergency Alert System "
  "on broadcast, and NOAA Weather Radio — all launched from "
  "one federal gateway by authorized local officials. WEA "
  "messages are 360 characters of imperative: the hazard, "
  "the place, the action. AMBER alerts find missing children; "
  "tornado warnings save lives by minutes. The system's power "
  "demands discipline: over-alerting breeds the cry-wolf "
  "fatigue that kills the next warning's credibility.",
  "Authorized alerting authorities — emergency managers, "
  "weather service, law enforcement — train and certify on "
  "IPAWS. Operators draw polygons, write 360-character "
  "messages with hazard, location, and protective action, "
  "and launch. Carriers deliver WEA to capable phones in "
  "the area; broadcasters relay EAS. Tests — the national "
  "periodic test — verify the chain. After-action reviews "
  "tune thresholds and wording.",
  ["IPAWS: WEA phones, EAS broadcast, NOAA radio — one gateway.",
   "360 characters: hazard, place, action.",
   "Launched by authorized local officials.",
   "Over-alerting breeds fatal cry-wolf fatigue."],
  ["Alerting authorities must be trained and authorized.",
   "Messages must state hazard, location, protective action.",
   "Tests must verify the chain."],
  ["FEMA IPAWS requirements.",
   "FCC WEA rules (47 CFR Part 10)."],
  ["Federal Emergency Management Agency - IPAWS.",
   "Federal Communications Commission - WEA rules."],
  "In the Signature relief system an alert is a sworn alarm: "
  "every polygon a covenant of precision, every 360 "
  "characters a promise of clarity, every restrained "
  "sounding a vow that warnings keep their weight.",
  {"people": 1000000, "supply_tons": 0, "days": 1}),

E("Damage Assessment: Windshield Surveys", "Foundations", 10, "foundations",
  "Damage assessment turns chaos into numbers: rapid "
  "windshield surveys — teams driving street by street — "
  "classify every building as affected, minor, major, or "
  "destroyed, the categories that unlock declarations and "
  "dollars. Preliminary damage assessments pair local "
  "knowledge with FEMA validators; the counts become the "
  "governor's request and the declaration's foundation. "
  "Later, detailed assessments scope Public Assistance "
  "projects down to the repair line-item. Drones and "
  "satellites now accelerate the count, but the trained eye "
  "at the curb remains the standard.",
  "Trained teams — building officials, assessors, FEMA "
  "specialists — canvas zones with standardized forms and "
  "the four damage categories. GPS tags each structure; "
  "photos document. Data aggregates to county and state "
  "totals against per-capita indicators. Detailed "
  "assessments follow for public facilities, scoping repair "
  "versus replacement. Quality review samples for "
  "consistency. The numbers feed declarations, grants, and "
  "recovery planning.",
  ["Classify buildings: affected, minor, major, destroyed.",
   "Rapid surveys unlock declarations and dollars.",
   "Preliminary assessments feed the governor's request.",
   "Drones accelerate; the trained eye remains standard."],
  ["Assessors need training on damage categories.",
   "Data must be georeferenced and documented.",
   "Quality review must sample for consistency."],
  ["FEMA damage assessment operations manual.",
   "Stafford Act damage thresholds."],
  ["Federal Emergency Management Agency - damage assessment.",
   "FEMA preliminary damage assessment guide."],
  "In the Signature relief system damage assessment is a "
  "sworn counting: every classified building a covenant of "
  "honest measure, every validated total a promise that aid "
  "follows fact.",
  {"people": 80000, "supply_tons": 200, "days": 10}),

E("Community Emergency Response Teams (CERT)", "Foundations", 11, "foundations",
  "Community Emergency Response Teams are neighbors trained to "
  "help themselves when professionals are overwhelmed: FEMA's "
  "program teaching disaster preparedness, fire safety, light "
  "search and rescue, medical triage, and team organization in "
  "about 20 hours. CERTs do not replace responders — they "
  "extend them, checking on neighbors, staffing shelters, and "
  "managing spontaneous volunteers until professionals arrive. "
  "Thousands of teams nationwide are the deep bench of "
  "resilience: the people who act in the first minutes, when "
  "minutes matter most.",
  "Fire departments or emergency management agencies sponsor "
  "teams, recruiting residents for the FEMA curriculum taught "
  "by qualified instructors. Graduates drill periodically, "
  "maintain go-kits, and integrate into local plans for "
  "activation. During incidents, CERTs work assigned missions "
  "under supervision — never freelancing. Programs track "
  "membership, training, and activations; refresher training "
  "keeps skills alive.",
  ["Neighbors trained for the first minutes of disaster.",
   "~20-hour FEMA curriculum: preparedness, fire, rescue, triage.",
   "Extend professionals; do not replace them.",
   "Thousands of teams: the deep bench of resilience."],
  ["Training must follow the FEMA CERT curriculum.",
   "Teams work under supervision, never freelancing.",
   "Sponsors must integrate teams into local plans."],
  ["FEMA CERT program guidance.",
   "Local emergency management plans."],
  ["Federal Emergency Management Agency - CERT.",
   "FEMA CERT training materials."],
  "In the Signature relief system CERT is a sworn "
  "neighborhood: every trained resident a covenant of "
  "readiness, every drill a promise practiced, every first-"
  "minute action a vow that neighbors do not wait.",
  {"people": 5000, "supply_tons": 20, "days": 30}),

E("Disaster Recovery Centers", "Foundations", 12, "foundations",
  "Disaster Recovery Centers are FEMA's storefronts after "
  "declaration: one-stop shops where survivors meet FEMA, the "
  "Small Business Administration, state agencies, and voluntary "
  "organizations face to face. Survivors check application "
  "status, appeal decisions, apply for SBA disaster loans, and "
  "get referrals — no appointment needed. DRCs locate in the "
  "hardest-hit areas, in accessible buildings, with multilingual "
  "staff. Mobile DRCs reach rural pockets. The centers stay "
  "until the need fades, then close with notice — the visible "
  "promise that the system comes to the people.",
  "FEMA and the state select sites by damage and access, stand "
  "up the center with partner agencies, and publicize hours "
  "and services. Staff help survivors navigate applications, "
  "appeals, and referrals; SBA officers take loan "
  "applications. Daily reports track visits and issues. "
  "Demobilization follows declining traffic with public "
  "notice; remaining cases transfer to continued case "
  "management.",
  ["One-stop shops for survivors after declaration.",
   "FEMA, SBA, state, voluntary agencies face to face.",
   "No appointment; accessible; multilingual.",
   "Mobile units reach rural pockets."],
  ["Sites must be accessible and in affected areas.",
   "Staff must cover application, appeal, referral needs.",
   "Closure requires public notice."],
  ["FEMA DRC operations guidance.",
   "Stafford Act individual assistance provisions."],
  ["Federal Emergency Management Agency - DRC guidance.",
   "Stafford Act, 42 U.S.C. 5121."],
  "In the Signature relief system a recovery center is a "
  "sworn doorway: every answered question a covenant of "
  "guidance, every appeal heard a promise of fairness, every "
  "open door a vow that the system comes to the people.",
  {"people": 40000, "supply_tons": 100, "days": 60}),

# ---------------- COMPOUNDED 13-24 ----------------

E("Humanitarian Supply Chains", "Compounded", 13, "compounded",
  "Humanitarian supply chains move relief from warehouses to "
  "the suffering: procurement, pre-positioned stockpiles, "
  "transport, and distribution under conditions where markets "
  "have collapsed. FEMA's logistics system, the UN Humanitarian "
  "Response Depots, and NGO supply networks stage commodities "
  "— water, food, tarps, medical kits — near hazard zones. "
  "The chain must surge instantly, track every pallet, and "
  "adapt as roads fail and needs shift. Commercial supply "
  "chains optimize cost; humanitarian chains optimize speed "
  "and equity — getting the right aid to the right people at "
  "the right time, regardless of profit.",
  "Logisticians forecast need from assessments, release "
  "pre-positioned stocks, procure surge supplies, and book "
  "transport — trucks, airlift, sealift. Distribution centers "
  "receive, sort, and push to points of distribution. Tracking "
  "systems follow pallets to final delivery. Partnerships with "
  "commercial carriers and the military extend reach. "
  "Demobilization recovers unused stocks and reconciles every "
  "shipment.",
  ["Move relief where markets have collapsed.",
   "Pre-positioned stockpiles near hazard zones.",
   "Optimize speed and equity, not profit.",
   "Track every pallet to final delivery."],
  ["Stockpiles need rotation and readiness checks.",
   "Distributions must be needs-based and documented.",
   "Partnerships need pre-disaster agreements."],
  ["FEMA logistics doctrine.",
   "UN Humanitarian Response Depot procedures."],
  ["Federal Emergency Management Agency - logistics.",
   "UN Office for the Coordination of Humanitarian Affairs - logistics."],
  "In the Signature relief system the supply chain is a sworn "
  "lifeline: every pre-positioned pallet a covenant of "
  "foresight, every delivered tarp a promise kept at speed, "
  "every tracked shipment a vow of accountability.",
  {"people": 150000, "supply_tons": 9000, "days": 45}),

E("Last-Mile Logistics", "Compounded", 14, "compounded",
  "Last-mile logistics is the hardest hundred yards of relief: "
  "getting supplies from the distribution point into the hands "
  "of the isolated — the flooded street, the mountain village, "
  "the high-rise with dead elevators. Trucks stop where roads "
  "do; the last mile needs boats, ATVs, helicopters, drones, "
  "and above all people carrying boxes. Points of distribution "
  "(PODs) push commodities outward; community groups pull them "
  "inward. Equity lives or dies here: the well-connected get "
  "served first unless the last mile is deliberately planned "
  "for the unreachable.",
  "Planners map isolated populations from census and damage "
  "data, pre-designate POD sites, and contract last-mile "
  "assets — high-water vehicles, boats, aircraft. PODs operate "
  "drive-through or walk-up with traffic control and "
  "security. Community organizations deliver to homebound "
  "residents. Tracking extends to the household where "
  "possible. After-action reviews measure who was reached — "
  "and who was not.",
  ["The hardest hundred yards: road's end to the isolated.",
   "Boats, ATVs, helicopters, drones, and people carrying.",
   "PODs push outward; community groups pull inward.",
   "Equity lives or dies in the last mile."],
  ["Isolated populations must be mapped in advance.",
   "PODs need traffic, security, and accessibility plans.",
   "Reach must be measured by population, not just tonnage."],
  ["FEMA POD operations guidance.",
   "Military last-mile doctrine (where applicable)."],
  ["Federal Emergency Management Agency - POD guidance.",
   "UN logistics cluster guidance."],
  "In the Signature relief system the last mile is a sworn "
  "delivery: every mapped isolate a covenant of being seen, "
  "every carried box a promise that distance does not deny "
  "aid.",
  {"people": 60000, "supply_tons": 1800, "days": 30}),

E("Water, Sanitation, and Hygiene (WASH)", "Compounded", 15, "compounded",
  "WASH — water, sanitation, and hygiene — is survival's "
  "tripod in disaster: safe water to drink, safe disposal of "
  "waste, and the hygiene that stops disease from following "
  "disaster. When systems fail, responders distribute bottled "
  "and bulk water, deploy mobile treatment units, install "
  "latrines and handwashing stations, and promote hygiene in "
  "shelters and camps. The Sphere standards set the minimums: "
  "15 liters per person per day, water points within 500 "
  "meters, one latrine per 20 people. Cholera and dysentery "
  "are the enemies; WASH is the wall.",
  "Assessors measure water access and sanitation gaps; WASH "
  "teams deploy treatment, trucking, and storage. Engineers "
  "site latrines away from water sources; hygiene promoters "
  "teach handwashing and safe storage. Water quality is tested "
  "for pathogens and chlorine residual. Waste is managed to "
  "prevent contamination. Monitoring tracks liters per person "
  "and disease trends.",
  ["Safe water, safe waste disposal, hygiene promotion.",
   "Sphere minimums: 15 L/person/day, points within 500 m.",
   "Stops cholera and dysentery following disaster.",
   "Mobile treatment, trucking, latrines, handwashing."],
  ["Water must be tested for safety.",
   "Latrines sited away from water sources.",
   "Hygiene promotion must accompany hardware."],
  ["Sphere Handbook WASH standards.",
   "WHO drinking water quality guidelines."],
  ["Sphere Association - Sphere Handbook.",
   "World Health Organization - water quality guidelines."],
  "In the Signature relief system WASH is a sworn purity: "
  "every tested liter a covenant of safety, every latrine a "
  "promise of dignity, every taught handwashing a vow against "
  "the second disaster of disease.",
  {"people": 100000, "supply_tons": 4500, "days": 60}),

E("Emergency Medical Teams", "Compounded", 16, "compounded",
  "Emergency Medical Teams are the deployable hospitals of "
  "disaster: self-sufficient units — from mobile clinics to "
  "field surgical hospitals — classified by WHO into types "
  "by capability. National teams like FEMA's Disaster Medical "
  "Assistance Teams and international classified EMTs deploy "
  "to earthquakes, conflicts, and outbreaks, bringing staff, "
  "equipment, pharmaceuticals, and their own support for weeks. "
  "Coordination through health clusters prevents the chaos of "
  "unregistered teams. The standard is simple: do no harm, "
  "meet the need, leave capacity behind.",
  "Health authorities request teams through coordination "
  "mechanisms; classified teams deploy with verified "
  "capabilities. Teams establish at assigned sites, triage "
  "and treat per protocols, and report to health information "
  "systems. Pharmacies manage controlled stocks. Demobilization "
  "hands patients and records to recovering facilities. "
  "After-action reviews feed reclassification. Unregistered "
  "teams are directed to coordinate or stand down.",
  ["Deployable medical units, WHO-classified by capability.",
   "From mobile clinics to field surgical hospitals.",
   "Self-sufficient for weeks.",
   "Standard: do no harm, meet need, leave capacity."],
  ["Teams should meet WHO classification standards.",
   "Deployment needs host-nation and cluster coordination.",
   "Patient records must transfer on demobilization."],
  ["WHO Emergency Medical Team classification standards.",
   "National team program standards."],
  ["World Health Organization - EMT initiative.",
   "FEMA Disaster Medical Assistance Team guidance."],
  "In the Signature relief system a medical team is a sworn "
  "healing expedition: every deployed capability a covenant "
  "of readiness, every treated patient a promise of care, "
  "every capacity left behind a vow of lasting good.",
  {"people": 25000, "supply_tons": 300, "days": 30}),

E("Field Hospitals", "Compounded", 17, "compounded",
  "Field hospitals bring the emergency department to the "
  "disaster: tented or modular facilities with triage, "
  "surgery, wards, pharmacy, lab, and imaging, erected where "
  "hospitals are destroyed or overwhelmed. Military, "
  "government, and NGO field hospitals deploy to "
  "earthquakes, wars, and pandemics — the COVID alternate "
  "care sites were field hospitals at national scale. They "
  "need water, power, waste, security, and supply chains as "
  "much as clinicians. The measure is throughput with "
  "quality: stabilizing the surge so the system survives.",
  "Health authorities site field hospitals by casualty "
  "flow; engineers erect structures with utilities, medical "
  "gas, and waste systems. Clinical teams staff to "
  "capability — emergency, surgical, intensive. Logistics "
  "sustain pharmaceuticals, oxygen, and blood. Information "
  "systems track patients. Security protects staff and "
  "supplies. Demobilization transfers patients and "
  "decommissions the site safely.",
  ["Tented/modular hospitals where facilities are destroyed.",
   "Triage, surgery, wards, pharmacy, lab, imaging.",
   "Need utilities, supply chains, security as much as clinicians.",
   "Measure: throughput with quality."],
  ["Siting must follow casualty flow and access.",
   "Clinical capability must match the need.",
   "Waste and utilities need engineered systems."],
  ["WHO field hospital guidance.",
   "Military field hospital doctrine."],
  ["World Health Organization - emergency medical guidance.",
   "U.S. Army field hospital doctrine."],
  "In the Signature relief system a field hospital is a "
  "sworn bastion of care: every erected ward a covenant of "
  "refuge, every surgery a promise of skill, every "
  "stabilized patient a vow that the surge was met.",
  {"people": 40000, "supply_tons": 600, "days": 45}),

E("Temporary Housing Programs", "Compounded", 18, "compounded",
  "Temporary housing bridges shelter and home: FEMA's "
  "Individuals and Households Program offers rental "
  "assistance, hotel stays through Transitional Sheltering "
  "Assistance, and — where rentals are scarce — manufactured "
  "housing units and direct lease. States and nonprofits add "
  "their own programs. The goal is dignity and momentum: "
  "families stable enough to work, enroll kids, and rebuild. "
  "The failure mode is the trailer park that becomes "
  "permanent — so programs time-limit assistance and connect "
  "to permanent housing case management.",
  "FEMA determines eligibility from registrations and "
  "inspections, then authorizes rental assistance paid to "
  "survivors or hotels. Where housing stock is destroyed, "
  "direct housing missions place units on private or group "
  "sites with utilities and maintenance. Case managers help "
  "households plan permanent housing. Recertification "
  "continues assistance while need lasts, up to statutory "
  "limits. Closeout transitions the last households out.",
  ["Bridge from shelter to home: rental aid, hotels, units.",
   "FEMA IHP plus state and nonprofit programs.",
   "Goal: dignity and momentum toward rebuilding.",
   "Time-limited; connected to permanent housing."],
  ["Eligibility needs registration and inspection.",
   "Assistance must be recertified while need lasts.",
   "Sites need utilities, maintenance, and services."],
  ["Stafford Act housing assistance provisions.",
   "FEMA IHP guidance."],
  ["Federal Emergency Management Agency - IHP guidance.",
   "Stafford Act, 42 U.S.C. 5174."],
  "In the Signature relief system temporary housing is a "
  "sworn bridge: every rental check a covenant of "
  "stability, every placed unit a promise of dignity, every "
  "transitioned family a vow fulfilled.",
  {"people": 30000, "supply_tons": 2000, "days": 180}),

E("Debris Management", "Compounded", 19, "compounded",
  "Debris management clears the aftermath: the millions of "
  "cubic yards of trees, building wreckage, and mud that "
  "block roads, harbor hazards, and stall recovery. FEMA's "
  "Public Assistance reimburses eligible removal — but only "
  "with documented rights-of-entry, environmental and "
  "historic reviews, and proper disposal. Operations run "
  "through temporary debris sites where loads are measured, "
  "sorted, reduced by grinding or burning, and hauled to "
  "final disposal. Segregation matters: vegetative, "
  "construction, hazardous, and electronic streams each have "
  "their rules. Done right, debris becomes mulch and "
  "aggregate; done wrong, it becomes liability.",
  "Jurisdictions activate debris plans with pre-qualified "
  "contractors, establish monitoring with load tickets and "
  "GPS, and open temporary sites with permits. Crews clear "
  "rights-of-way first, then private property with "
  "rights-of-entry. Monitors document every load for "
  "reimbursement. Environmental reviews cover wetlands, "
  "asbestos, and historic properties. Final disposal "
  "follows waste rules; closeout reconciles quantities.",
  ["Clear millions of cubic yards blocking recovery.",
   "FEMA reimburses with documentation and reviews.",
   "Sort: vegetative, construction, hazardous, electronic.",
   "Done right: mulch and aggregate. Done wrong: liability."],
  ["Rights-of-entry required for private property.",
   "Loads need monitored tickets for reimbursement.",
   "Environmental and historic reviews required."],
  ["FEMA debris management guide.",
   "44 CFR debris removal eligibility rules."],
  ["Federal Emergency Management Agency - debris guidance.",
   "U.S. Army Corps of Engineers debris mission guidance."],
  "In the Signature relief system debris management is a "
  "sworn clearing: every ticketed load a covenant of "
  "honest accounting, every sorted stream a promise of "
  "proper rest, every cleared road a vow of return.",
  {"people": 120000, "supply_tons": 500000, "days": 120}),

E("Volunteer Coordination", "Compounded", 20, "compounded",
  "Volunteer coordination turns goodwill into workforce: "
  "affiliated volunteers through VOAD organizations, and the "
  "spontaneous thousands who simply show up. Volunteer "
  "Reception Centers register, credential, and assign the "
  "spontaneous; voluntary agencies manage their trained "
  "members. Unmanaged volunteers become a second disaster — "
  "unfed, untasked, in the way. Managed well, they muck "
  "houses, staff shelters, and sort donations by the "
  "thousand. Liability coverage, safety briefings, and "
  "supervision are non-negotiable.",
  "Emergency management activates volunteer coordination "
  "with voluntary agency liaisons. Reception centers intake "
  "spontaneous volunteers, check skills, and assign to "
  "missions. Agencies supervise work crews with safety "
  "briefings and equipment. Hours are tracked for "
  "reimbursement and recognition. Demobilization releases "
  "volunteers with thanks and records. After-action reviews "
  "improve the next activation.",
  ["Turn goodwill into managed workforce.",
   "Affiliated plus spontaneous volunteers.",
   "Reception centers register and assign.",
   "Unmanaged volunteers become a second disaster."],
  ["Volunteers need safety briefings and supervision.",
   "Liability coverage required.",
   "Hours must be tracked."],
  ["FEMA volunteer coordination guidance.",
   "State VOAD coordination protocols."],
  ["National Voluntary Organizations Active in Disaster.",
   "Federal Emergency Management Agency - donations/volunteer guidance."],
  "In the Signature relief system volunteer coordination is "
  "a sworn mustering: every registered helper a covenant of "
  "organized compassion, every safe assignment a promise of "
  "purpose, every tracked hour a vow of gratitude.",
  {"people": 10000, "supply_tons": 100, "days": 60}),

E("Donations Management", "Compounded", 21, "compounded",
  "Donations management handles the generosity flood: the "
  "unsolicited clothes, canned goods, and bottled water that "
  "arrive faster than they can be sorted — the 'second "
  "disaster' of disaster lore. Best practice: cash first, "
  "because money buys exactly what is needed locally. "
  "Managed programs run warehouses and distribution with "
  "inventory systems; unmanaged piles rot. National Donations "
  "Management Network and state portals match offers to needs. "
  "The rule for donors: give cash, give through trusted "
  "organizations, never self-deploy with a truck of stuff.",
  "Emergency management activates donations plans with "
  "warehouse space and staffing. Offers are logged, vetted "
  "against needs, and accepted or declined. Warehouses sort, "
  "inventory, and distribute through agencies. Cash donations "
  "go to established funds. Public messaging steers generosity "
  "to cash and specific lists. Demobilization donates or "
  "disposes remainders responsibly.",
  ["Handle the generosity flood without drowning in it.",
   "Cash first: buys exactly what is needed.",
   "Unsolicited goods are the 'second disaster.'",
   "Match offers to needs; never self-deploy."],
  ["Donations need warehousing and inventory control.",
   "Public messaging must steer to cash and lists.",
   "Distribution must be needs-based."],
  ["FEMA donations management guidance.",
   "State donations plans."],
  ["Federal Emergency Management Agency - donations guidance.",
   "National Donations Management Network."],
  "In the Signature relief system donations management is a "
  "sworn stewardship of generosity: every vetted offer a "
  "covenant of fit, every distributed good a promise "
  "honored, every cash gift a vow of maximum help.",
  {"people": 80000, "supply_tons": 2500, "days": 45}),

E("Psychological First Aid", "Compounded", 22, "compounded",
  "Psychological first aid is the humane response to trauma's "
  "first hours: not therapy, but practical care — safety, "
  "calm, connection, and hope — delivered by anyone trained "
  "in its principles. Born from disaster mental health "
  "research, PFA teaches responders to listen without "
  "pressuring, meet basic needs, connect survivors to "
  "supports, and link to services. Crisis counseling programs, "
  "funded by FEMA after declarations, bring trained counselors "
  "to shelters and neighborhoods. Most survivors recover with "
  "support; PFA helps the natural recovery along and spots "
  "those who need more.",
  "Trained providers — counselors, trained volunteers, "
  "responders — offer PFA in shelters, assistance centers, "
  "and door-to-door outreach. They assess needs, provide "
  "practical help, teach coping, and connect to resources. "
  "Programs track contacts and referrals. Those showing "
  "persistent distress are referred to professional care. "
  "Responder mental health — defusing and peer support — "
  "runs in parallel.",
  ["Practical care in trauma's first hours: safety, calm, connection.",
   "Not therapy — support for natural recovery.",
   "Listen without pressuring; meet needs; link to services.",
   "FEMA crisis counseling funds post-declaration programs."],
  ["Providers need PFA training.",
   "Referral pathways must exist for persistent distress.",
   "Cultural sensitivity required."],
  ["National Child Traumatic Stress Network PFA guide.",
   "FEMA crisis counseling program guidance."],
  ["National Child Traumatic Stress Network - PFA.",
   "Substance Abuse and Mental Health Services Administration."],
  "In the Signature relief system psychological first aid is "
  "a sworn comfort: every listened-to story a covenant of "
  "witness, every met need a promise of steadiness, every "
  "referral a vow that no one faces the aftermath alone.",
  {"people": 50000, "supply_tons": 10, "days": 90}),

E("Animal Sheltering in Disasters", "Compounded", 23, "compounded",
  "Animal sheltering in disasters keeps families whole: "
  "because people will not evacuate without their pets, "
  "and should not have to. Post-Katrina, the PETS Act of "
  "2006 requires emergency plans to account for household "
  "pets and service animals. Co-located shelters house "
  "animals adjacent to human shelters; standalone emergency "
  "animal shelters take the overflow. Operations need "
  "veterinarians, kennels, food, and reunification systems "
  "— microchip scanning and photo boards that return the "
  "lost. Livestock need separate large-animal sheltering.",
  "Emergency management plans designate animal shelter "
  "sites and staffing — animal control, humane societies, "
  "veterinary teams. Evacuation messaging tells owners to "
  "bring carriers, food, and records. Shelters intake, "
  "identify, house, and care for animals; reunification "
  "teams match strays to owners. Medical teams triage "
  "injuries. Demobilization returns animals or transfers "
  "to adoption.",
  ["Keep families whole: no one should abandon pets to evacuate.",
   "PETS Act (2006) requires pet planning.",
   "Co-located and standalone emergency shelters.",
   "Reunification systems return the lost."],
  ["Plans must address pets and service animals.",
   "Shelters need veterinary oversight.",
   "Reunification records required."],
  ["PETS Act of 2006 (42 U.S.C. 5196 note).",
   "FEMA animal emergency guidance."],
  ["Federal Emergency Management Agency - animal emergencies.",
   "PETS Act, Pub. L. 109-308."],
  "In the Signature relief system animal sheltering is a "
  "sworn keeping of the whole family: every kenneled pet a "
  "covenant of reunion, every scanned chip a promise of "
  "return, every fed animal a vow that no family member is "
  "left behind.",
  {"people": 15000, "supply_tons": 150, "days": 30}),

E("Power Restoration Coordination", "Compounded", 24, "compounded",
  "Power restoration coordination brings the lights back in "
  "order: utilities, mutual-aid crews, and government "
  "coordinating the largest mobilizations in the industry. "
  "Restoration follows priority — transmission first, then "
  "substations, then critical facilities (hospitals, water "
  "plants), then the largest blocks of customers, then "
  "individual services. Mutual assistance agreements move "
  "thousands of lineworkers across the country; the "
  "Department of Energy coordinates federal support. Public "
  "communication — estimated restoration times by area — "
  "is as vital as the wires.",
  "Utilities activate storm plans, pre-stage crews, and "
  "assess damage by patrol and smart-meter data. Incident "
  "command structures manage the restoration with damage "
  "assessment feeding work planning. Mutual-aid crews "
  "integrate under host-utility direction. Government "
  "coordinates fuel, access, and regulatory waivers. "
  "Estimated restoration times publish and update. "
  "After-action reviews improve the next storm.",
  ["Restore in priority order: transmission to individual services.",
   "Mutual aid moves thousands of lineworkers.",
   "Critical facilities prioritized.",
   "Public restoration estimates as vital as wires."],
  ["Restoration must follow safety-first sequencing.",
   "Mutual-aid crews need integration and safety briefings.",
   "Estimates must be updated as known."],
  ["DOE emergency support function guidance.",
   "Industry mutual assistance agreements."],
  ["U.S. Department of Energy - energy emergencies.",
   "Edison Electric Institute - mutual assistance."],
  "In the Signature relief system power restoration is a "
  "sworn relighting: every re-energized feeder a covenant "
  "of return, every prioritized hospital a promise of care, "
  "every honest estimate a vow of straight talk in the dark.",
  {"people": 500000, "supply_tons": 800, "days": 14}),

# ---------------- ADVANCED 25-34 ----------------

E("Post-Disaster Needs Assessment (PDNA)", "Advanced", 25, "advanced",
  "The Post-Disaster Needs Assessment is the international "
  "standard for counting what disaster destroyed and what "
  "recovery costs: a government-led, UN-EU-World Bank "
  "supported methodology assessing damage, loss, needs, and "
  "recovery strategy across sectors — housing, infrastructure, "
  "livelihoods, social sectors. The PDNA produces the "
  "recovery price tag that donors conferences pledge "
  "against, and the strategy that guides years of "
  "reconstruction. Its discipline — one assessment, one "
  "number, one plan — prevents the competing claims that "
  "plague uncoordinated recovery.",
  "The government requests PDNA support; partners deploy "
  "sector teams with government counterparts. Teams assess "
  "physical damage and economic loss, estimate recovery "
  "needs with build-back-better premiums, and draft sector "
  "strategies. Validation workshops align stakeholders. The "
  "consolidated report goes to donors and guides the "
  "recovery framework. Implementation is monitored against "
  "the PDNA's benchmarks.",
  ["International standard for disaster damage and needs.",
   "Government-led, UN-EU-World Bank supported.",
   "One assessment, one number, one recovery plan.",
   "Price tag that donor conferences pledge against."],
  ["Government must lead and own the assessment.",
   "Sectors must use consistent methods.",
   "Recovery strategy must include build-back-better."],
  ["PDNA Guidelines (UN-EU-World Bank).",
   "Sendai Framework for Disaster Risk Reduction."],
  ["Global Facility for Disaster Reduction and Recovery - PDNA.",
   "United Nations Development Programme - recovery guidance."],
  "In the Signature relief system the PDNA is a sworn "
  "reckoning: every counted loss a covenant of honest "
  "measure, every priced need a promise of planned "
  "recovery, every validated strategy a vow of one "
  "direction.",
  {"people": 1000000, "supply_tons": 50000, "days": 365}),

E("The UN Cluster Coordination System", "Advanced", 26, "advanced",
  "The UN cluster system organizes international relief by "
  "sector: eleven clusters — from food security and health "
  "to shelter, WASH, and logistics — each with a designated "
  "lead agency accountable for coordination. Born of the "
  "2005 humanitarian reform after coordination failures, "
  "the system activates in major crises where the "
  "government requests help. Cluster coordinators map who "
  "does what where, fill gaps, and speak for the sector. "
  "National clusters mirror the global ones. The system is "
  "imperfect — meetings multiply — but it ended the era of "
  "nobody-in-charge relief.",
  "The Humanitarian Coordinator activates clusters with "
  "government consent; lead agencies appoint coordinators. "
  "Clusters hold regular coordination meetings, maintain "
  "4W matrices (who, what, where, when), identify gaps, "
  "and advocate. Funding flows through appeals and pooled "
  "funds informed by cluster strategies. Performance is "
  "reviewed; deactivation follows recovery. National "
  "authorities increasingly lead with cluster support.",
  ["Eleven sector clusters with accountable lead agencies.",
   "Born of 2005 reform after coordination failures.",
   "Map who does what where; fill gaps.",
   "Ended the era of nobody-in-charge relief."],
  ["Activation needs government consent.",
   "Lead agencies must staff coordination.",
   "Information must be shared across clusters."],
  ["IASC cluster coordination guidance.",
   "UN General Assembly Resolution 46/182."],
  ["UN Office for the Coordination of Humanitarian Affairs.",
   "Inter-Agency Standing Committee guidance."],
  "In the Signature relief system the clusters are a sworn "
  "division of mercy: every sector a covenant of clear "
  "responsibility, every 4W matrix a promise of no gaps, "
  "every coordinated response a vow against chaos.",
  {"people": 2000000, "supply_tons": 200000, "days": 180}),

E("Sphere Humanitarian Standards", "Advanced", 27, "advanced",
  "The Sphere Handbook is the humanitarian charter: minimum "
  "standards for water, food, shelter, and health in crisis, "
  "plus the Humanitarian Charter's rights and the Core "
  "Humanitarian Standard's quality benchmarks. Written by "
  "practitioners since 1997, Sphere says what 'enough' means "
  "— 15 liters of water, 2,100 kilocalories, 3.5 square "
  "meters of covered shelter space per person. Agencies "
  "pledge to meet them; evaluations measure against them. "
  "Sphere turned good intentions into accountable minimums: "
  "the floor below which no response may fall.",
  "Agencies adopt Sphere in program design, setting "
  "indicators from its minimum standards. Monitoring "
  "measures coverage against the thresholds. Evaluations "
  "judge response quality by them. Training teaches the "
  "handbook's application across contexts. National "
  "adaptations translate standards to local law. The "
  "handbook is revised periodically by global "
  "consultation — the 2018 edition is current.",
  ["Minimum standards for water, food, shelter, health.",
   "Defines 'enough': liters, calories, square meters.",
   "Humanitarian Charter plus Core Humanitarian Standard.",
   "The floor below which no response may fall."],
  ["Programs should be designed to Sphere minimums.",
   "Monitoring must measure against the standards.",
   "Adaptations must respect the Charter's rights."],
  ["Sphere Handbook (2018 edition).",
   "Core Humanitarian Standard on Quality and Accountability."],
  ["Sphere Association - Sphere Handbook.",
   "CHS Alliance - Core Humanitarian Standard."],
  "In the Signature relief system Sphere is a sworn floor: "
  "every liter a covenant of minimum dignity, every "
  "measured standard a promise of accountability, every "
  "met threshold a vow that enough is truly enough.",
  {"people": 500000, "supply_tons": 30000, "days": 120}),

E("Cash and Voucher Assistance", "Advanced", 28, "advanced",
  "Cash and voucher assistance gives survivors money instead "
  "of things: the fastest-growing modality in humanitarian "
  "aid, now a major share of international response. Cash "
  "respects dignity and choice, supports local markets "
  "instead of bypassing them, and costs less to deliver than "
  "shipping goods. Programs use mobile money, cards, or "
  "paper vouchers redeemable at vetted vendors, targeted by "
  "vulnerability and verified by identity systems. FEMA's "
  "own disaster assistance is largely cash. The evidence is "
  "strong: where markets function, cash outperforms "
  "in-kind.",
  "Agencies assess market functionality and beneficiary "
  "preference, set transfer values from minimum expenditure "
  "baskets, and choose delivery mechanisms — mobile money, "
  "prepaid cards, vouchers. Registration and verification "
  "prevent duplication. Vendor networks are contracted and "
  "monitored. Post-distribution monitoring checks spending, "
  "prices, and protection outcomes. Coordination avoids "
  "overlap between agencies.",
  ["Money instead of things: dignity, choice, market support.",
   "Fastest-growing aid modality; FEMA assistance is largely cash.",
   "Mobile money, cards, vouchers via verified identity.",
   "Where markets function, cash outperforms in-kind."],
  ["Markets must be assessed as functional.",
   "Targeting must be vulnerability-based and verified.",
   "Post-distribution monitoring required."],
  ["CALP Network cash guidance.",
   "Donor cash policies (e.g., Grand Bargain commitments)."],
  ["CALP Network - cash and voucher guidance.",
   "Overseas Development Institute - cash evidence."],
  "In the Signature relief system cash assistance is a "
  "sworn trust in people: every transfer a covenant of "
  "dignity, every market purchase a promise of local "
  "recovery, every monitored outcome a vow of wise "
  "giving.",
  {"people": 200000, "supply_tons": 500, "days": 90}),

E("Early Recovery Planning", "Advanced", 29, "advanced",
  "Early recovery starts rebuilding while response still "
  "runs: debris cleared with livelihoods in mind, markets "
  "restarted, governance restored, foundations laid for "
  "long-term recovery. The UN's early recovery cluster — "
  "led by UNDP — coordinates this bridge phase that "
  "traditional response neglects and development arrives "
  "too late for. Cash-for-work clears rubble and pays "
  "survivors; small grants restart businesses; rubble is "
  "recycled into reconstruction. Early recovery is where "
  "relief becomes recovery: the pivot from saving lives "
  "to restoring them.",
  "Coordinators map early recovery needs alongside "
  "humanitarian response, prioritizing livelihoods, "
  "governance, and infrastructure quick wins. Cash-for-work "
  "programs employ survivors in clearance and repair. "
  "Business grants and microfinance restart commerce. "
  "Debris recycling feeds reconstruction material needs. "
  "Planning links to the PDNA and national recovery "
  "frameworks. Transition hands programs to development "
  "actors.",
  ["Rebuild while response still runs.",
   "Bridge phase: relief to long-term recovery.",
   "Cash-for-work, business grants, debris recycling.",
   "The pivot from saving lives to restoring them."],
  ["Planning must start during response, not after.",
   "Programs should build on local capacity.",
   "Transition to development actors required."],
  ["UNDP early recovery guidance.",
   "IASC early recovery policy."],
  ["United Nations Development Programme - early recovery.",
   "UN Cluster guidance."],
  "In the Signature relief system early recovery is a "
  "sworn turning: every cash-for-work day a covenant of "
  "renewed livelihood, every restarted business a promise "
  "of return, every recycled rubble a vow that ruins "
  "become foundations.",
  {"people": 300000, "supply_tons": 20000, "days": 180}),

E("Build Back Better", "Advanced", 30, "advanced",
  "Build Back Better is recovery's highest ambition: not "
  "restoring what was, but building what should be — safer, "
  "greener, fairer. Coined after the 2004 tsunami and "
  "enshrined in the Sendai Framework, it means elevating "
  "homes above the next flood, hardening grids, restoring "
  "mangroves as storm buffers, and fixing the inequities "
  "the disaster exposed. It costs more upfront and pays "
  "back in avoided losses. Every recovery faces the "
  "temptation to rebuild fast and wrong; Build Back Better "
  "is the discipline to rebuild right.",
  "Recovery planners embed resilience standards in "
  "rebuilding: elevated structures, hardened infrastructure, "
  "nature-based defenses. Building codes are updated and "
  "enforced for reconstruction. Land-use plans steer "
  "rebuilding from the most hazardous areas. Equity "
  "assessments direct resources to the most vulnerable. "
  "Funding — from FEMA's 406 mitigation to international "
  "donors — rewards resilient design. Monitoring verifies "
  "the better, not just the rebuilt.",
  ["Recover safer, greener, fairer — not just as before.",
   "Enshrined in the Sendai Framework.",
   "Elevate, harden, restore nature, fix inequities.",
   "Costs more now; pays in avoided losses."],
  ["Reconstruction should meet updated resilience standards.",
   "Equity must guide resource allocation.",
   "Land use should steer from highest hazard."],
  ["Sendai Framework Priority 4.",
   "FEMA Hazard Mitigation Grant Program (406) rules."],
  ["UN Office for Disaster Risk Reduction - Sendai Framework.",
   "World Bank - Build Back Better guidance."],
  "In the Signature relief system Build Back Better is a "
  "sworn improvement: every elevated home a covenant "
  "against the next flood, every hardened grid a promise "
  "of endurance, every corrected inequity a vow of "
  "justice.",
  {"people": 400000, "supply_tons": 80000, "days": 730}),

E("Disaster Risk Reduction", "Advanced", 31, "advanced",
  "Disaster risk reduction prevents the disaster before the "
  "hazard strikes: the Sendai Framework's global agenda to "
  "cut deaths, affected people, and economic loss through "
  "understanding risk, strengthening governance, investing "
  "in resilience, and preparing response. It is codes that "
  "keep buildings standing, wetlands that blunt storm "
  "surge, early warnings that empty the beach, and "
  "insurance that spreads the loss. Every dollar of "
  "mitigation saves about six in recovery, per the National "
  "Institute of Building Sciences. DRR is the cheapest "
  "life insurance a society buys.",
  "Governments assess risk — hazard, exposure, vulnerability "
  "— and write DRR strategies with targets. Building codes "
  "and land-use plans reduce exposure; infrastructure "
  "hardening reduces vulnerability; early warning systems "
  "and drills prepare response. Mitigation grants fund "
  "elevations, buyouts, and retrofits. Progress is reported "
  "against Sendai targets. The private sector is enlisted "
  "through insurance and resilient investment.",
  ["Prevent disaster before hazard strikes.",
   "Sendai Framework: understand risk, govern, invest, prepare.",
   "Codes, wetlands, warnings, insurance.",
   "$1 of mitigation saves ~$6 in recovery."],
  ["Strategies need risk assessments and targets.",
   "Codes and land use must reflect known hazards.",
   "Progress must be monitored against targets."],
  ["Sendai Framework for Disaster Risk Reduction 2015-2030.",
   "National mitigation investment studies."],
  ["UN Office for Disaster Risk Reduction - Sendai.",
   "National Institute of Building Sciences - mitigation saves."],
  "In the Signature relief system risk reduction is a sworn "
  "foresight: every strengthened code a covenant with the "
  "future, every preserved wetland a promise of natural "
  "defense, every prepared community a vow that warning "
  "becomes action.",
  {"people": 1000000, "supply_tons": 10000, "days": 365}),

E("Contingency Stockpiles", "Advanced", 32, "advanced",
  "Contingency stockpiles are readiness in a warehouse: "
  "pre-positioned water, food, tarps, cots, medical kits, "
  "and generators staged near hazard zones for immediate "
  "release. FEMA's distribution centers, state stockpiles, "
  "and the Strategic National Stockpile for medical "
  "countermeasures form the American system; UN depots "
  "serve the world. Stockpiles must rotate — food expires, "
  "batteries die — and match the hazards they serve: "
  "hurricane kits on the Gulf, wildfire supplies in the "
  "West. The stockpile that sits unready is just expensive "
  "storage.",
  "Logisticians size stockpiles from hazard and population "
  "models, procure to specification, and warehouse with "
  "inventory systems tracking lot dates. Rotation schedules "
  "refresh perishables; inspections verify readiness. "
  "Release authorities and triggers are pre-delegated for "
  "speed. Exercises test the drawdown. After use, "
  "replenishment restores readiness. Audits verify the "
  "stockpile exists as claimed.",
  ["Pre-positioned relief near hazard zones.",
   "Water, food, tarps, cots, medical kits, generators.",
   "Must rotate: food expires, batteries die.",
   "Match stockpiles to regional hazards."],
  ["Inventory must be tracked with rotation schedules.",
   "Release authorities must be pre-delegated.",
   "Readiness must be inspected and exercised."],
  ["FEMA logistics and stockpile guidance.",
   "Strategic National Stockpile authorities."],
  ["Federal Emergency Management Agency - logistics.",
   "Administration for Strategic Preparedness and Response."],
  "In the Signature relief system a stockpile is a sworn "
  "readiness: every rotated pallet a covenant against "
  "decay, every pre-delegated release a promise of speed, "
  "every inspected shelf a vow that readiness is real.",
  {"people": 500000, "supply_tons": 25000, "days": 30}),

E("Civil-Military Coordination", "Advanced", 33, "advanced",
  "Civil-military coordination brings armed forces into "
  "disaster relief without militarizing it: the military's "
  "lift, engineering, and medical capacity under civilian "
  "direction. In the US, the National Guard answers to "
  "governors while federal troops need Stafford Act mission "
  "assignments and Posse Comitatus limits; internationally, "
  "the Oslo Guidelines govern foreign military humanitarian "
  "use as a last resort. Coordination runs through defense "
  "coordinating officers embedded with FEMA and civil-"
  "military cells in UN operations. The principle is "
  "constant: civilian lead, military support, humanitarian "
  "space protected.",
  "Governors activate Guard units under state control; "
  "federal requests go through FEMA mission assignments to "
  "designated commands. Defense coordinating officers embed "
  "in FEMA regions to translate needs to capabilities. "
  "Internationally, clusters request military assets only "
  "when civilian capacity is exhausted, per Oslo. After "
  "action, forces demobilize and costs are reimbursed. "
  "Training and exercises build the relationships before "
  "the crisis.",
  ["Military capacity under civilian direction.",
   "Guard to governors; federal troops via mission assignment.",
   "Oslo Guidelines govern international military humanitarian use.",
   "Principle: civilian lead, military support."],
  ["Federal military use needs proper authorization.",
   "Posse Comitatus limits domestic law enforcement roles.",
   "Humanitarian principles must be protected."],
  ["Stafford Act mission assignment authorities.",
   "Oslo Guidelines on military humanitarian assets."],
  ["Federal Emergency Management Agency - military coordination.",
   "UN OCHA - Oslo Guidelines."],
  "In the Signature relief system civil-military "
  "coordination is a sworn alliance: every airlift a "
  "covenant of capacity lent, every civilian lead a "
  "promise of proper order, every protected humanitarian "
  "space a vow of principle.",
  {"people": 750000, "supply_tons": 40000, "days": 60}),

E("Accountability to Affected Populations", "Advanced", 34, "advanced",
  "Accountability to affected populations is the radical "
  "idea that survivors are not beneficiaries but rights-"
  "holders: entitled to information, participation, and "
  "complaint mechanisms in the aid they receive. The Core "
  "Humanitarian Standard and the Grand Bargain enshrine it; "
  "FEMA's equity initiatives pursue it domestically. "
  "Practice means communicating in local languages, "
  "consulting communities on program design, running "
  "feedback hotlines, and publishing what was heard and "
  "changed. Aid that ignores the affected repeats the "
  "colonial pattern; accountability breaks it.",
  "Agencies establish communication channels — radio, SMS, "
  "community meetings — in local languages. Feedback "
  "mechanisms collect complaints and questions; teams "
  "analyze and respond, closing the loop publicly. "
  "Participation shapes program design and targeting. "
  "Protection from sexual exploitation and abuse is "
  "enforced with zero tolerance. Monitoring measures "
  "satisfaction and inclusion, disaggregated by "
  "vulnerability.",
  ["Survivors as rights-holders, not beneficiaries.",
   "Entitled to information, participation, complaint.",
   "Enshrined in CHS and the Grand Bargain.",
   "Feedback loops: hear, respond, show change."],
  ["Communication must be in local languages.",
   "Feedback mechanisms must be safe and accessible.",
   "Responses must be published and tracked."],
  ["Core Humanitarian Standard on Quality and Accountability.",
   "Grand Bargain commitments."],
  ["CHS Alliance - Core Humanitarian Standard.",
   "Inter-Agency Standing Committee - AAP commitments."],
  "In the Signature relief system accountability is a "
  "sworn listening at the highest level: every feedback "
  "hotline a covenant of voice, every published response "
  "a promise of answer, every consulted community a vow "
  "that aid serves, not rules.",
  {"people": 1000000, "supply_tons": 5000, "days": 180}),
]
