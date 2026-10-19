#!/usr/bin/env python3
"""Entries for the Municipal Services databases (2026-10-17).

34 municipal service topics, ladder-ordered 1-34
(foundations 1-12 / compounded 13-24 / advanced 25-34).
Public = real, fact-checked domain data. Signature = Signature civic
interpretation, titles suffixed " (Signature Edition)".
No website references. No Facebook.
"""


def E(name, group, rank, tier, description, how, key_points, requirements,
      standards, citations, sig_lens, demo_data, demo_key="service"):
    return {"name": name, "group": group, "ladder_rank": rank,
            "ladder_tier": tier, "description": description,
            "how_it_works": how, "key_points": key_points,
            "requirements": requirements, "standards": standards,
            "citations": citations, "sig_lens": sig_lens,
            "demo_key": demo_key, "demo_data": demo_data}


ENTRIES = [

# ---------------- FOUNDATIONS 1-12 ----------------

E("Building Permits", "Foundations", 1, "foundations",
  "A building permit is the city's written permission to build, "
  "alter, or repair a structure — the front door of the construction "
  "regulatory system. Permits ensure work meets the building code: "
  "structural safety, fire protection, energy, and accessibility. "
  "Most jurisdictions require permits for new construction, "
  "additions, structural changes, and major mechanical, electrical, "
  "and plumbing work, while exempting minor repairs like painting. "
  "The permit process — application, plan review, issuance, "
  "inspections, final approval — creates the public record that a "
  "building was built right. Unpermitted work can stall sales, void "
  "insurance, and trigger stop-work orders.",
  "The applicant submits plans showing code compliance; plan "
  "reviewers check structure, fire, energy, and accessibility. Fees "
  "are based on valuation or area. The permit issues with approved "
  "plans and an inspection card. Inspectors visit at stages — "
  "foundation, framing, mechanical rough-in, final — and sign off "
  "each. The certificate of occupancy or final inspection closes "
  "the permit. Online portals now accept applications, route "
  "reviews, schedule inspections, and issue permits digitally.",
  ["Written permission to build, alter, or repair structures.",
   "Ensures compliance with building, fire, energy, accessibility codes.",
   "Process: application, plan review, issuance, inspections, final.",
   "Unpermitted work risks stop-work orders, insurance, and sales."],
  ["Applications need code-compliant plans and valuation.",
   "Work must match the approved plans.",
   "Inspections must be passed at each required stage."],
  ["International Building Code (adopted locally).",
   "Local permit ordinances and fee schedules."],
  ["International Code Council - building codes.",
   "Local building department permit guides."],
  "In the Signature civic system a building permit is a sworn "
  "license to raise walls: the plans a covenant of safety, each "
  "inspection a witness, the final approval a seal on the structure.",
  {"fee": 850, "days": 14, "annual_volume": 4200}),

E("Occupancy Permits", "Foundations", 2, "foundations",
  "An occupancy permit — the certificate of occupancy — is the "
  "document that says a building may legally be used. Issued after "
  "final inspections pass, it certifies the structure complies with "
  "codes and is approved for its stated occupancy: residential, "
  "commercial, assembly, or industrial. Lenders, insurers, and "
  "buyers demand it; occupying without one can bring fines and "
  "eviction orders. Change the use — turning a warehouse into a "
  "restaurant — and a new certificate is required, because the "
  "code's demands change with the use.",
  "After all final inspections pass, the building official issues "
  "the certificate listing the approved occupancy classification, "
  "occupant load, and any conditions. Temporary certificates allow "
  "partial occupancy during finishing work. Change-of-use "
  "applications trigger review of the new occupancy's fire, "
  "accessibility, and structural requirements. The certificate is "
  "recorded against the property and produced at sale, lease, and "
  "financing.",
  ["Certifies a building may legally be occupied.",
   "Issued after final inspections; lists occupancy classification.",
   "Required by lenders, insurers, and buyers.",
   "Change of use requires a new certificate."],
  ["All final inspections must pass first.",
   "Occupancy classification must match actual use.",
   "Temporary occupancy needs conditions and time limits."],
  ["International Building Code (occupancy classifications).",
   "Local certificate-of-occupancy ordinances."],
  ["International Code Council - building code occupancy chapters.",
   "Local building department procedures."],
  "In the Signature civic system the certificate of occupancy is a "
  "sworn welcome: the building inspected and true, the use named "
  "and lawful, the doors opened by the city's seal.",
  {"fee": 150, "days": 5, "annual_volume": 3800}),

E("Electrical Permits", "Foundations", 3, "foundations",
  "Electrical permits govern the wiring that powers buildings — "
  "new services, panel upgrades, rewiring, and additions to "
  "circuits. Electricity kills and burns when installed wrong, so "
  "the National Electrical Code, adopted nearly everywhere, sets "
  "the rules, and licensed electricians do the work in most "
  "jurisdictions. Permits trigger inspections of rough-in wiring "
  "before drywall and of the finished installation. Homeowners doing "
  "their own work usually need permits too, with the same "
  "inspections. Unpermitted electrical work is a leading cause of "
  "house fires discovered after the fact.",
  "The applicant — usually the licensed electrical contractor — "
  "files the scope: service size, circuits, loads. Review checks "
  "load calculations and code compliance. Rough-in inspection "
  "verifies wiring, boxes, and grounding before concealment; final "
  "inspection checks devices, panels, and labeling. The utility "
  "connects or upgrades service after approval. Inspectors can "
  "require corrections with re-inspection before sign-off.",
  ["Govern wiring: services, panels, circuits, rewiring.",
   "National Electrical Code sets the rules nearly everywhere.",
   "Licensed electricians; inspections at rough-in and final.",
   "Unpermitted electrical work is a leading fire cause."],
  ["Work must follow the adopted National Electrical Code.",
   "Most jurisdictions require licensed contractors.",
   "Rough-in must be inspected before concealment."],
  ["National Electrical Code (NFPA 70).",
   "Local electrical ordinances and licensing rules."],
  ["National Fire Protection Association - NEC.",
   "Local electrical inspection procedures."],
  "In the Signature civic system an electrical permit is a sworn "
  "guardianship of current: every inspected connection a covenant "
  "against fire, every labeled panel a promise of order in the "
  "wires.",
  {"fee": 200, "days": 3, "annual_volume": 6500}),

E("Plumbing Permits", "Foundations", 4, "foundations",
  "Plumbing permits cover the pipes that carry water in and waste "
  "out: new installations, repiping, water heaters, sewer "
  "connections, and gas piping in many jurisdictions. Plumbing "
  "codes — the International Plumbing Code, the Uniform Plumbing "
  "Code, or state variants — dictate pipe sizing, venting, "
  "backflow prevention, and fixture standards that protect drinking "
  "water from contamination. Permits bring inspections of rough-in "
  "piping and pressure tests before walls close, and of fixtures "
  "at completion. Cross-connections and sewer gas are the silent "
  "hazards the code guards against.",
  "The licensed plumbing contractor files the fixture count, pipe "
  "materials, and isometric drawings. Review verifies sizing, "
  "venting, and backflow protection. Rough-in inspection checks "
  "pipe, slope, supports, and pressure tests; the top-out and "
  "final inspections verify vents through the roof and working "
  "fixtures. Water heaters need temperature-pressure relief and "
  "proper venting. Sewer taps need right-of-way and utility "
  "coordination.",
  ["Cover water, waste, gas piping, water heaters, sewer taps.",
   "Codes dictate sizing, venting, backflow prevention.",
   "Inspections at rough-in, pressure test, and final.",
   "Protect drinking water from contamination."],
  ["Work must follow the adopted plumbing code.",
   "Backflow preventers required where hazards exist.",
   "Pressure tests must pass before concealment."],
  ["International Plumbing Code or Uniform Plumbing Code.",
   "Local plumbing ordinances and licensing."],
  ["International Code Council / IAPMO - plumbing codes.",
   "Local plumbing inspection procedures."],
  "In the Signature civic system a plumbing permit is a sworn "
  "stewardship of water: every vented trap a covenant of clean "
  "air, every backflow preventer a promise that drinking water "
  "stays pure.",
  {"fee": 180, "days": 3, "annual_volume": 5800}),

E("Mechanical and HVAC Permits", "Foundations", 5, "foundations",
  "Mechanical permits govern heating, ventilation, air conditioning, "
  "and refrigeration — the systems that keep buildings breathable, "
  "warm, and cool. The International Mechanical Code and the "
  "International Energy Conservation Code set requirements for "
  "equipment sizing, ductwork, ventilation rates, combustion safety, "
  "and refrigerant handling. Permits cover new systems, replacements, "
  "and duct modifications; inspections verify proper installation, "
  "venting of combustion appliances, and refrigerant line integrity. "
  "Oversized or unvented equipment wastes energy and can poison air — "
  "the permit is the checkpoint.",
  "The contractor files equipment specifications, load calculations "
  "(Manual J or equivalent), and duct layouts. Review checks sizing, "
  "ventilation rates, and energy compliance. Rough-in inspection "
  "covers ducts, flues, and gas piping; final inspection verifies "
  "operation, clearances, and carbon-monoxide safety. Refrigerant "
  "work requires EPA-certified technicians. Changeouts of like-for-"
  "like equipment may qualify for streamlined permits.",
  ["Govern HVAC and refrigeration installations.",
   "Codes set sizing, ventilation, combustion, refrigerant rules.",
   "Inspections verify ducts, venting, and safe operation.",
   "Load calculations prevent wasteful oversizing."],
  ["Equipment must be sized by approved load calculations.",
   "Combustion appliances need proper venting and clearances.",
   "Refrigerant handling requires EPA certification."],
  ["International Mechanical Code.",
   "International Energy Conservation Code."],
  ["International Code Council - mechanical and energy codes.",
   "Air Conditioning Contractors of America - Manual J."],
  "In the Signature civic system a mechanical permit is a sworn "
  "regulation of breath: every sized system a covenant of comfort, "
  "every vented flue a promise of safe air.",
  {"fee": 220, "days": 4, "annual_volume": 4900}),

E("Demolition Permits", "Foundations", 6, "foundations",
  "Demolition permits authorize tearing buildings down — work as "
  "regulated as construction, because collapse, dust, asbestos, and "
  "utility strikes endanger neighbors. Applicants submit the "
  "structure's details, demolition method, dust and noise controls, "
  "pedestrian protection, and utility disconnection proofs. Asbestos "
  "and lead surveys are mandatory for older buildings; abatement "
  "precedes demolition. Rodent baiting, historic review, and "
  "neighbor notification round out the requirements. The permit "
  "sets the rules for a safe disappearance.",
  "The applicant files surveys for asbestos, lead, and hazardous "
  "materials, plus engineering for the demolition method. Review "
  "checks utility disconnects, protection plans, and historic "
  "status. Abatement contractors remove hazards first under "
  "environmental rules. During demolition, inspectors verify dust "
  "control, site fencing, and structural sequencing. Debris goes to "
  "licensed facilities with manifests; the site is graded and "
  "secured at completion.",
  ["Authorize building demolition with safety controls.",
   "Asbestos and lead surveys mandatory for older buildings.",
   "Require utility disconnects, dust control, pedestrian protection.",
   "Historic review and neighbor notification included."],
  ["Hazard surveys must precede demolition.",
   "Utilities must be disconnected and verified.",
   "Debris must go to licensed facilities."],
  ["OSHA demolition standards (29 CFR 1926 Subpart T).",
   "EPA NESHAP asbestos rules; local demolition ordinances."],
  ["Occupational Safety and Health Administration - demolition.",
   "U.S. Environmental Protection Agency - asbestos NESHAP."],
  "In the Signature civic system a demolition permit is a sworn "
  "unbuilding: every survey a covenant that hazards are known, "
  "every controlled collapse a promise that neighbors stay safe.",
  {"fee": 400, "days": 10, "annual_volume": 700}),

E("Zoning Permits", "Foundations", 7, "foundations",
  "Zoning permits — often called zoning clearances or certificates — "
  "verify that a proposed use and structure comply with the zoning "
  "ordinance before building permits issue. Staff check the use "
  "against the district's allowed list, measure setbacks, height, "
  "lot coverage, and parking against the code, and confirm the lot "
  "is legal. Fences, sheds, home additions, and new businesses all "
  "typically need zoning clearance. It is the gatekeeper that keeps "
  "a factory out of a neighborhood and a house off the setback "
  "line.",
  "The applicant submits a site plan showing the structure's "
  "location, dimensions, and use. Zoning staff verify district, "
  "use permissions, dimensional standards, parking, landscaping, "
  "and overlay rules like floodplain or historic districts. "
  "Compliant projects get clearance and proceed to building "
  "permit; noncompliant ones are denied with appeal rights to the "
  "board of adjustment. Records of clearances build the "
  "property's zoning history.",
  ["Verify use and structure comply with zoning before building.",
   "Check district, setbacks, height, coverage, parking.",
   "Gatekeeper against incompatible uses.",
   "Denials carry appeal rights."],
  ["Site plans must show location, dimensions, and use.",
   "Uses must be permitted or conditionally permitted in the district.",
   "Overlays (floodplain, historic) must also be satisfied."],
  ["Local zoning ordinance.",
   "State zoning enabling acts."],
  ["Local zoning ordinances and permit guides.",
   "American Planning Association - zoning practice."],
  "In the Signature civic system a zoning permit is a sworn fitting: "
  "every setback a covenant of neighborly distance, every allowed "
  "use a promise that the district's character holds.",
  {"fee": 100, "days": 7, "annual_volume": 9000}),

E("Sign Permits", "Foundations", 8, "foundations",
  "Sign permits regulate the signs that speak from buildings and "
  "lots: their size, height, illumination, placement, and "
  "structural safety. Sign codes balance business visibility "
  "against traffic safety and community appearance, distinguishing "
  "wall signs, monument signs, pole signs, and electronic message "
  "centers with different rules. Structural review ensures signs "
  "survive wind; electrical review covers illumination; historic "
  "districts add design review. Content-based distinctions must "
  "respect the First Amendment — the Supreme Court's Reed v. Town "
  "of Gilbert (2015) reshaped how codes classify signs.",
  "The applicant submits sign drawings with dimensions, materials, "
  "structural calculations, and electrical details. Staff check "
  "size, height, setback, and illumination against the sign code. "
  "Engineered signs need sealed structural calcs; illuminated "
  "signs need electrical permits. Installation is inspected for "
  "structural and electrical compliance. Temporary signs — banners, "
  "grand-opening displays — get short-term permits with removal "
  "dates.",
  ["Regulate sign size, height, illumination, placement, structure.",
   "Balance business visibility, traffic safety, appearance.",
   "Structural and electrical review included.",
   "Content rules must respect First Amendment limits."],
  ["Signs must meet dimensional and placement standards.",
   "Structural signs need engineering; illuminated need electrical permits.",
   "Historic districts add design review."],
  ["Local sign codes.",
   "Reed v. Town of Gilbert, 576 U.S. 155 (2015)."],
  ["Local sign ordinances.",
   "Reed v. Town of Gilbert, 576 U.S. 155 (2015)."],
  "In the Signature civic system a sign permit is a sworn voice: "
  "every measured sign a covenant of fair visibility, every "
  "structural check a promise the message stands safely.",
  {"fee": 120, "days": 5, "annual_volume": 2500}),

E("Special Event Permits", "Foundations", 9, "foundations",
  "Special event permits let streets, parks, and plazas become "
  "festivals, parades, races, and concerts — temporarily and safely. "
  "Applications detail the event plan: dates, attendance, street "
  "closures, tents, stages, food vendors, alcohol, amplified sound, "
  "and sanitation. Fire marshals review occupant loads and tent "
  "safety; police plan traffic and security; health departments "
  "license food vendors; public works arranges barricades and "
  "cleanup. Insurance and indemnification protect the city. The "
  "permit is the choreography that lets thousands gather without "
  "chaos.",
  "Organizers apply weeks or months ahead with site plans, "
  "schedules, and vendor lists. Departments review concurrently: "
  "fire for life safety, police for security and traffic, health "
  "for food, parks for grounds protection. Conditions set hours, "
  "sound limits, and cleanup duties; fees cover city costs. "
  "Large events need emergency plans and command posts. After the "
  "event, inspections verify restoration and bills settle.",
  ["Authorize festivals, parades, races, concerts on public space.",
   "Coordinate fire, police, health, public works review.",
   "Require insurance, sanitation, traffic, and security plans.",
   "Set hours, sound, and cleanup conditions."],
  ["Applications must precede the event by the required lead time.",
   "Life-safety and emergency plans required for large events.",
   "Insurance and indemnification must protect the city."],
  ["Local special event ordinances.",
   "NFPA 101/102 life safety provisions for events."],
  ["Local special event permit guides.",
   "National Fire Protection Association - event safety."],
  "In the Signature civic system a special event permit is a sworn "
  "celebration: every barricaded street a covenant of safe joy, "
  "every inspected tent a promise that the gathering ends in "
  "smiles.",
  {"fee": 300, "days": 30, "annual_volume": 600}),

E("Home Occupation Permits", "Foundations", 10, "foundations",
  "Home occupation permits let residents run businesses from home — "
  "within limits that keep neighborhoods residential. Zoning codes "
  "allow quiet, low-impact work (offices, studios, crafts) while "
  "restricting customer traffic, employees, signage, outdoor storage, "
  "and hazardous materials. The permit registers the business, "
  "confirms the use fits the home-occupation rules, and gives "
  "neighbors a standard to hold. It is the compromise between "
  "enterprise and tranquility: earn a living, don't change the "
  "street.",
  "The resident applies describing the business, hours, employees, "
  "visitors, and equipment. Zoning staff check the home-occupation "
  "standards: no retail storefronts, limited signage, no outdoor "
  "storage, parking adequacy. Some jurisdictions notify neighbors "
  "or require conditional approval for higher-impact occupations. "
  "The permit issues with conditions; violations — too many "
  "customers, commercial vehicles everywhere — bring enforcement.",
  ["Allow home businesses within neighborhood-protecting limits.",
   "Restrict traffic, employees, signage, storage, hazards.",
   "Registers the business with zoning.",
   "Compromise between enterprise and tranquility."],
  ["Business must meet home-occupation performance standards.",
   "No change to residential character permitted.",
   "Violations subject to enforcement and revocation."],
  ["Local zoning ordinance home-occupation provisions.",
   "Local business license requirements."],
  ["Local zoning ordinances.",
   "American Planning Association - home occupation guidance."],
  "In the Signature civic system a home occupation permit is a "
  "sworn balance: every quiet enterprise a covenant of livelihood, "
  "every observed limit a promise that home remains home.",
  {"fee": 75, "days": 7, "annual_volume": 1800}),

E("Right-of-Way Permits", "Foundations", 11, "foundations",
  "Right-of-way permits govern work in the public street and "
  "sidewalk corridor: utility cuts, driveway approaches, sidewalk "
  "repairs, scaffolding, and crane swings over the sidewalk. The "
  "right-of-way belongs to the public, and the permit sets the "
  "terms of its temporary private use — traffic control, "
  "restoration standards, insurance, and time limits. Pavement "
  "cuts must be restored to city standards; botched patches become "
  "the potholes of next year. Fees often include degradation "
  "charges recognizing that cuts shorten pavement life.",
  "The applicant submits plans showing the work zone, traffic "
  "control per MUTCD, and restoration details. Review checks "
  "conflicts with other utilities and city projects. The permit "
  "sets hours, lane-closure rules, and restoration specs — base, "
  "pavement, markings. Inspectors check traffic control setup and "
  "final restoration; bonds guarantee it. Emergency utility work "
  "proceeds immediately with after-the-fact permits.",
  ["Govern work in streets and sidewalks: cuts, driveways, scaffolding.",
   "Set traffic control, restoration, insurance, time limits.",
   "Pavement cuts restored to city standards.",
   "Degradation fees recognize shortened pavement life."],
  ["Traffic control must follow the MUTCD.",
   "Restoration must meet city pavement standards.",
   "Bonds or insurance must guarantee the work."],
  ["Local right-of-way ordinances.",
   "Manual on Uniform Traffic Control Devices."],
  ["Federal Highway Administration - MUTCD.",
   "Local right-of-way permit manuals."],
  "In the Signature civic system a right-of-way permit is a sworn "
  "borrowing: every barricaded lane a covenant of safe passage, "
  "every restored patch a promise that the street is returned "
  "whole.",
  {"fee": 250, "days": 5, "annual_volume": 7200}),

E("Grading Permits", "Foundations", 12, "foundations",
  "Grading permits regulate moving earth: cuts, fills, retaining "
  "walls, and drainage changes that reshape lots and slopes. "
  "Uncontrolled grading causes erosion, landslides, flooding of "
  "neighbors, and sediment choking streams — so codes require "
  "engineered plans, erosion controls, and inspections. Hillside "
  "areas face stricter rules on slope, setbacks, and geotechnical "
  "review. The permit ensures water still drains where it should "
  "and slopes stand where they are built.",
  "The applicant submits grading plans with existing and proposed "
  "contours, quantities, retaining walls, and drainage. Engineers "
  "review slope stability, erosion control, and downstream "
  "impacts; geotechnical reports are required on steep or suspect "
  "soils. Silt fence, inlet protection, and stabilized entrances "
  "go in before earth moves. Inspectors check compaction, wall "
  "construction, and final drainage. As-builts confirm the finished "
  "grades.",
  ["Regulate earthwork: cuts, fills, walls, drainage changes.",
   "Prevent erosion, landslides, neighbor flooding.",
   "Require engineered plans and erosion controls.",
   "Hillsides face stricter geotechnical review."],
  ["Plans must show contours, quantities, walls, drainage.",
   "Erosion controls must precede earthmoving.",
   "Geotechnical reports required on steep or suspect soils."],
  ["Local grading ordinances.",
   "State erosion and sediment control laws."],
  ["Local grading manuals.",
   "State erosion control handbooks."],
  "In the Signature civic system a grading permit is a sworn "
  "reshaping: every engineered slope a covenant of stability, "
  "every silt fence a promise that the stream stays clear.",
  {"fee": 350, "days": 12, "annual_volume": 1500}),

# ---------------- COMPOUNDED 13-24 ----------------

E("Curbside Waste Collection", "Compounded", 13, "compounded",
  "Curbside waste collection is the weekly ritual of municipal "
  "service: trucks emptying trash, recycling, and organics carts "
  "from millions of curbs. Cities run it with their own crews or "
  "contract haulers, on routes optimized for density and "
  "turnaround. Automated side-loaders with cart tippers dominate "
  "modern fleets; fees fund the system through bills or taxes. "
  "Missed pickups, the eternal complaint, are tracked as the "
  "service's vital sign. Collection is also the front line of "
  "diversion — what gets sorted at the curb decides what the "
  "landfill receives.",
  "Route planners design daily routes balancing stops, tonnage, "
  "and drive time; GPS and onboard systems track completion. "
  "Crews follow set-out rules — cart placement, lids closed, no "
  "hazardous waste — and tag violations for education. Transfer "
  "stations receive the loads; tipping fees price disposal. "
  "Customer service logs missed pickups and dispatches returns. "
  "Contract cities bid hauling franchises on cycles, scoring "
  "price, diversion, and service.",
  ["Weekly collection of trash, recycling, organics at the curb.",
   "City crews or contracted haulers on optimized routes.",
   "Fees fund the system; missed pickups are the vital sign.",
   "Front line of waste diversion."],
  ["Set-out rules must be published and enforced fairly.",
   "Hauler contracts need performance standards.",
   "Hazardous waste must be excluded from carts."],
  ["Local solid waste ordinances and franchise agreements.",
   "State diversion mandates (where adopted)."],
  ["Solid Waste Association of North America - collection guidance.",
   "Local hauler franchise agreements."],
  "In the Signature civic system curbside collection is a sworn "
  "circuit: every emptied cart a covenant of cleanliness, every "
  "completed route a promise that the week's leavings are gone.",
  {"fee": 28, "days": 1, "annual_volume": 2600000}),

E("Recycling Programs", "Compounded", 14, "compounded",
  "Recycling programs turn discards into feedstock: paper, "
  "cardboard, glass, metal, and plastic sorted at the curb or "
  "drop-off and sold to mills and manufacturers. Single-stream "
  "collection — everything in one cart — boosted participation "
  "but contaminated loads; programs now battle wish-cycling with "
  "education on what truly recycles. Materials recovery facilities "
  "sort the stream with screens, magnets, optical sorters, and "
  "human hands. Markets decide the economics: cardboard and "
  "aluminum pay, mixed plastics often cost. State bottle bills and "
  "recycled-content mandates shape the system.",
  "Cities contract collection and processing, set accepted-"
  "materials lists, and educate residents on proper sorting. "
  "MRFs process single-stream loads under contracts sharing "
  "commodity revenue and residue costs. Contamination audits "
  "measure load quality; tag-and-leave programs correct "
  "offenders. Programs report diversion rates to the state. "
  "Extended producer responsibility laws, spreading across states, "
  "shift packaging costs to producers.",
  ["Turn discards into manufacturing feedstock.",
   "Single-stream boosted participation, raised contamination.",
   "MRFs sort with screens, magnets, optical sorters.",
   "Markets decide economics; education fights wish-cycling."],
  ["Accepted-materials lists must reflect real markets.",
   "Contamination must be measured and addressed.",
   "Diversion must be reported to the state."],
  ["State recycling and diversion mandates.",
   "Local franchise and processing contracts."],
  ["U.S. Environmental Protection Agency - recycling data.",
   "State recycling agency reports."],
  "In the Signature civic system recycling is a sworn return: "
  "every sorted bottle a covenant of second life, every clean "
  "load a promise that discards become resources.",
  {"fee": 8, "days": 14, "annual_volume": 1200000}),

E("Yard Waste and Composting", "Compounded", 15, "compounded",
  "Yard waste programs collect leaves, grass, and branches — and "
  "increasingly food scraps — turning them into compost instead "
  "of landfill. Many states ban yard waste from landfills, making "
  "collection mandatory. Curbside programs use carts or bags on "
  "weekly or seasonal schedules; drop-off sites take brush and "
  "stumps. Composting facilities windrow or vessel-compost the "
  "material into soil amendment sold or given to residents. Food-"
  "scrap collection, the growing frontier, needs airtight carts "
  "and weekly pickup to stay clean.",
  "Cities schedule seasonal leaf collection and year-round yard "
  "waste routes, contracting or operating compost sites. "
  "Facilities manage windrows for temperature, moisture, and "
  "turning to kill pathogens and weed seeds, testing finished "
  "compost to standards. Contamination — plastic bags, trash — "
  "is screened out. Programs educate on what composts; food-scrap "
  "pilots measure participation and diversion. Finished compost "
  "returns to parks, gardens, and farms.",
  ["Collect leaves, grass, branches — increasingly food scraps.",
   "Many states ban yard waste from landfills.",
   "Compost facilities turn organics into soil amendment.",
   "Food-scrap collection is the growing frontier."],
  ["Facilities need permits with operating standards.",
   "Compost must meet pathogen and maturity standards.",
   "Contamination must be screened and managed."],
  ["State composting facility permits.",
   "U.S. Composting Council Seal of Testing Assurance."],
  ["U.S. Composting Council - standards.",
   "State organics diversion laws."],
  "In the Signature civic system composting is a sworn cycle: "
  "every collected leaf a covenant of return, every finished "
  "windrow a promise that the earth is fed back.",
  {"fee": 5, "days": 7, "annual_volume": 800000}),

E("Bulk Waste Pickup", "Compounded", 16, "compounded",
  "Bulk waste pickup hauls the big stuff — furniture, mattresses, "
  "appliances — that doesn't fit the cart. Programs run on "
  "scheduled routes, on-call appointments, or annual cleanups; "
  "some charge per item, others include a yearly allowance. "
  "Appliances with refrigerants need certified recovery before "
  "scrapping. Mattresses, increasingly banned from landfills by "
  "state stewardship laws, go to recyclers who strip springs and "
  "foam. Electronics ride along in many programs under e-waste "
  "rules. The service keeps alleys clear and illegal dumping "
  "down.",
  "Residents schedule pickups online or by phone, placing items "
  "at the curb by the set time. Crews sort on the truck: metal "
  "to scrap, mattresses to recyclers, the rest to transfer. "
  "Refrigerant technicians evacuate appliances per EPA rules. "
  "Programs track items, costs, and diversion. Illegal dumping "
  "crews handle what the program misses. Fees or tax funding "
  "cover the heavy lifting.",
  ["Haul furniture, mattresses, appliances that don't fit carts.",
   "Scheduled routes, on-call, or annual cleanups.",
   "Refrigerants recovered; mattresses increasingly recycled.",
   "Keeps alleys clear and dumping down."],
  ["Refrigerant recovery must follow EPA rules.",
   "E-waste must go to certified recyclers.",
   "Set-out rules must be published."],
  ["EPA refrigerant recovery rules (Section 608).",
   "State e-waste and mattress stewardship laws."],
  ["U.S. Environmental Protection Agency - appliance disposal.",
   "State stewardship program rules."],
  "In the Signature civic system bulk pickup is a sworn clearing: "
  "every hauled sofa a covenant of clean alleys, every recovered "
  "refrigerant a promise that the heavy things leave lightly.",
  {"fee": 35, "days": 10, "annual_volume": 95000}),

E("Household Hazardous Waste", "Compounded", 17, "compounded",
  "Household hazardous waste programs collect the poisons of "
  "modern homes — paints, solvents, pesticides, batteries, "
  "fluorescent lamps, motor oil — keeping them out of trash, "
  "drains, and landfills. Permanent drop-off facilities and "
  "periodic collection events staffed by trained crews sort, "
  "pack, and ship wastes to licensed treatment and disposal. "
  "Paint stewardship programs recycle latex into new paint; "
  "used oil becomes re-refined lubricant or fuel; batteries go "
  "to smelters. The service is free to residents and priced "
  "into the solid waste system.",
  "Residents bring wastes in original containers to staffed "
  "facilities; crews screen, sort by hazard class, and pack "
  "per DOT rules. Licensed haulers manifest shipments to "
  "permitted treatment, storage, and disposal facilities. "
  "Programs track pounds collected by category and report to "
  "the state. Swap shops reuse good paint and cleaners. "
  "Education steers buyers toward less-toxic alternatives.",
  ["Collect paints, solvents, pesticides, batteries, oil, lamps.",
   "Staffed facilities sort, pack, ship to licensed disposal.",
   "Paint, oil, batteries recycled into new products.",
   "Free to residents; keeps poisons out of trash and drains."],
  ["Facilities need hazardous waste permits or exemptions.",
   "Shipments require manifests to permitted facilities.",
   "Staff must be trained in hazard handling."],
  ["State household hazardous waste program rules.",
   "DOT hazardous materials transport rules."],
  ["State environmental agency HHW guidance.",
   "Product Stewardship Institute - paint and battery programs."],
  "In the Signature civic system hazardous waste collection is "
  "a sworn detox: every surrendered solvent a covenant of safe "
  "keeping, every manifested drum a promise the poisons are "
  "caged.",
  {"fee": 0, "days": 30, "annual_volume": 45000}),

E("Water Service", "Compounded", 18, "compounded",
  "Water service delivers drinking water to every tap through the "
  "distribution network: mains, valves, hydrants, storage tanks, "
  "and service lines. Utilities pump treated water into the grid, "
  "maintain pressure for firefighting and upstairs showers alike, "
  "and guard quality from plant to tap with sampling and flushing. "
  "Meters measure use for billing; rates are set to cover "
  "operations, debt, and capital. Main breaks are the dramatic "
  "failures — crews repair around the clock while boil-water "
  "notices protect customers. Lead service line replacement is the "
  "national priority of the decade.",
  "Operators run pumps and tanks to hold pressure zones, flush "
  "mains, and sample per Safe Drinking Water Act schedules. "
  "Leak detection crews find hidden losses; valve crews exercise "
  "valves so they work in emergencies. Engineering models the "
  "network, sizes replacements, and plans lead-line inventory and "
  "removal. Meter readers or AMI systems feed billing; customer "
  "service handles high bills and shutoff protections. Capital "
  "programs replace a target mileage of main yearly.",
  ["Deliver drinking water through mains, tanks, hydrants, services.",
   "Maintain pressure for firefighting and daily use.",
   "Guard quality plant-to-tap with sampling.",
   "Lead service line replacement is the national priority."],
  ["Water quality must meet Safe Drinking Water Act standards.",
   "Lead lines must be inventoried and replaced per rule.",
   "Shutoffs must follow notice and protection rules."],
  ["Safe Drinking Water Act; Lead and Copper Rule Revisions.",
   "State public utility commission rate rules."],
  ["U.S. Environmental Protection Agency - drinking water rules.",
   "American Water Works Association - distribution standards."],
  "In the Signature civic system water service is a sworn flow: "
  "every pressurized main a covenant of readiness, every sample "
  "a witness to purity, every replaced lead line a promise to "
  "children.",
  {"fee": 45, "days": 2, "annual_volume": 480000}),

E("Sewer Service", "Compounded", 19, "compounded",
  "Sewer service carries wastewater away through the collection "
  "system to treatment: gravity mains, force mains, lift "
  "stations, and manholes — mostly invisible until it fails. "
  "Utilities clean and inspect pipes on cycles, using cameras to "
  "find cracks, roots, and grease, then rehabilitate by lining "
  "or replace by digging. Sewer use ordinances ban what harms "
  "the system — grease, wipes, industrial slugs — and set rates "
  "that fund the buried network. Overflows, whether from "
  "blockages or storms, trigger reporting and rapid response.",
  "Collection crews jet-clean lines, televise condition, and "
  "score defects per NASSCO standards. Engineers prioritize "
  "rehabilitation — cured-in-place lining renews pipes without "
  "digging — and upsize bottlenecks. Lift stations get redundant "
  "pumps and backup power. FOG (fats, oils, grease) programs "
  "inspect restaurants. Flow monitoring finds infiltration of "
  "groundwater that steals capacity. Capital plans target a "
  "mileage of renewal yearly.",
  ["Carry wastewater through buried collection networks.",
   "Clean, camera-inspect, and rehabilitate on cycles.",
   "Sewer use ordinances ban grease, wipes, harmful discharges.",
   "Overflows trigger reporting and rapid response."],
  ["Overflows must be reported to regulators.",
   "Rehabilitation should follow condition assessment.",
   "Industrial discharges need pretreatment permits."],
  ["Clean Water Act collection system expectations.",
   "NASSCO PACP inspection standards."],
  ["U.S. Environmental Protection Agency - collection systems.",
   "NASSCO - inspection and rehabilitation standards."],
  "In the Signature civic system sewer service is a sworn "
  "undercurrent: every jetted mile a covenant of flow, every "
  "lined pipe a promise renewed underground, every rapid "
  "response a vow that failures are faced.",
  {"fee": 38, "days": 2, "annual_volume": 460000}),

E("Stormwater Utility Service", "Compounded", 20, "compounded",
  "Stormwater utility service manages rain as a utility: "
  "collecting fees based on impervious area and spending them on "
  "drains, basins, street sweeping, and water-quality programs. "
  "The fee model — pioneered widely since the 1990s — gives "
  "drainage a dedicated revenue instead of competing for general "
  "taxes. Bills go to every parcel with hard surface, with credits "
  "for rain gardens and detention that reduce runoff. The utility "
  "maintains the gray system, builds green infrastructure, and "
  "meets MS4 permit duties. It turns every rooftop into a "
  "ratepayer and every storm into a managed event.",
  "The utility calculates impervious area per parcel from aerial "
  "imagery, bills quarterly or with water bills, and adjudicates "
  "appeals and credit applications. Crews maintain inlets, pipes, "
  "and basins; engineers model flooding and design capital "
  "projects. MS4 compliance — illicit discharge detection, "
  "construction oversight, public education — is funded and "
  "tracked. Green infrastructure grants help property owners "
  "install rain gardens for credits.",
  ["Manage rain as a fee-funded utility.",
   "Fees based on impervious area; credits for runoff reduction.",
   "Maintain drains, build green infrastructure, meet MS4 duties.",
   "Dedicated revenue instead of competing for taxes."],
  ["Fees must reflect cost of service with appeal rights.",
   "MS4 minimum measures must be implemented.",
   "Credits need verification of installed controls."],
  ["Clean Water Act MS4 regulations.",
   "Local stormwater utility ordinances."],
  ["U.S. Environmental Protection Agency - stormwater.",
   "Water Environment Federation - utility guidance."],
  "In the Signature civic system stormwater service is a sworn "
  "taming of rain: every fee a covenant of shared drainage, every "
  "rain garden a promise of patience, every clean outfall a "
  "witness.",
  {"fee": 12, "days": 1, "annual_volume": 500000}),

E("Snow Removal", "Compounded", 21, "compounded",
  "Snow removal is winter's municipal war: plows, salt, and brine "
  "deployed against the storm on priority routes. Cities classify "
  "streets — arterials and hills first, then collectors, then "
  "residentials — and publish the plow order so residents know "
  "where they stand. Anti-icing brine before the storm prevents "
  "bonding; plowing and deicing during it keeps arterials passable; "
  "cleanup widens afterward. Salt damages concrete, cars, and "
  "waterways, so calibration and alternatives matter. Sidewalk "
  "clearing usually falls to property owners by ordinance, on "
  "deadlines measured in hours.",
  "Public works tracks forecasts, pre-treats with brine, and "
  "dispatches plows by priority as snow accumulates. GPS tracks "
  "every truck; supervisors redeploy to drifting areas. Salt "
  "spreaders are calibrated to apply minimum effective rates. "
  "Crews clear downtown cores, bus routes, and hills first, then "
  "residentials. After the storm, widening and hauling clear "
  "intersections and parking. Costs — overtime, salt, equipment "
  "wear — are tracked per storm for budgeting.",
  ["Plows, salt, brine deployed on priority routes.",
   "Anti-ice before, plow during, widen after.",
   "Arterials and hills first; residentials after.",
   "Sidewalks usually owners' duty by ordinance."],
  ["Priority routes must be published.",
   "Salt application should be calibrated to minimum effective rates.",
   "Sidewalk ordinances need clear deadlines and enforcement."],
  ["Local snow emergency ordinances.",
   "State DOT winter maintenance guidance (for state routes)."],
  ["American Public Works Association - winter maintenance.",
   "State DOT snow and ice control manuals."],
  "In the Signature civic system snow removal is a sworn winter "
  "watch: every brined bridge a covenant against ice, every plowed "
  "arterial a promise of passage, every calibrated spreader a vow "
  "of restraint.",
  {"fee": 0, "days": 1, "annual_volume": 25}),

E("Street Sweeping", "Compounded", 22, "compounded",
  "Street sweeping keeps gutters clean, storm drains clear, and "
  "pollutants out of waterways — the humble service with "
  "environmental teeth. Mechanical brooms, vacuum sweepers, and "
  "regenerative-air machines run scheduled routes, collecting "
  "leaves, litter, and the fine sediment that carries metals and "
  "oils to streams. MS4 permits count sweeping as a pollution "
  "control, with frequencies tied to land use. Parking restrictions "
  "on sweeping days — the familiar alternate-side rules — let "
  "sweepers reach the curb. The collected tons are weighed, "
  "tested, and disposed or composted.",
  "Sweeping supervisors schedule routes by land use and leaf "
  "season, posting no-parking signs where needed. Operators run "
  "overlapping passes at effective speeds; dumps are weighed and "
  "logged. Maintenance shops service brooms, vacuums, and water "
  "systems. MS4 reporting credits the pollutant removal. Leaf "
  "season brings extra passes and collection. Costs per curb-mile "
  "are tracked against sweeping's water-quality benefits.",
  ["Clean gutters, clear drains, cut water pollution.",
   "Mechanical, vacuum, regenerative-air machines on routes.",
   "MS4 permits credit sweeping as pollution control.",
   "Alternate-side parking lets sweepers reach curbs."],
  ["Routes must meet MS4 frequency commitments.",
   "Sweepings must be disposed or composted properly.",
   "No-parking rules need signage and notice."],
  ["Clean Water Act MS4 expectations.",
   "Local parking and sweeping ordinances."],
  ["U.S. Environmental Protection Agency - MS4 guidance.",
   "American Public Works Association - sweeping practice."],
  "In the Signature civic system street sweeping is a sworn "
  "tidying: every swept gutter a covenant of clear drains, every "
  "collected ton a promise the stream runs cleaner.",
  {"fee": 0, "days": 30, "annual_volume": 18000}),

E("Pothole Repair", "Compounded", 23, "compounded",
  "Pothole repair is the most visible public works: crews cutting, "
  "cleaning, tacking, filling, and compacting the craters that "
  "freeze-thaw and traffic carve into pavement. Winter patching "
  "uses cold mix for speed; permanent repair waits for warm "
  "weather and hot mix. Throw-and-go fills the hole today; "
  "mill-and-fill renews the section for years. Response-time "
  "standards — 24 to 72 hours for reported arterials — are the "
  "service promise, tracked in 311 systems. Claims for vehicle "
  "damage follow notice rules: cities generally must have known "
  "about the hole.",
  "Crews patrol and respond to 311 reports, prioritizing by "
  "road class and hazard. Cold-mix patches hold through winter; "
  "spring brings hot-mix permanent repairs with proper cut, "
  "clean, tack, fill, and compaction. Quality is checked by "
  "revisit rates — patches that fail get redone. Pavement "
  "managers track pothole counts by street as a condition "
  "signal feeding resurfacing priorities. Damage claims are "
  "investigated against notice records.",
  ["Cut, clean, tack, fill, compact — the visible public works.",
   "Cold mix for winter speed; hot mix for permanent repair.",
   "Response standards of 24-72 hours tracked in 311.",
   "Damage claims turn on whether the city had notice."],
  ["Repairs should follow cut-and-patch standards.",
   "Response times must be tracked and reported.",
   "Claims need investigation against notice records."],
  ["Local street maintenance standards.",
   "State notice-of-claim statutes."],
  ["American Public Works Association - pavement maintenance.",
   "Local 311 service standards."],
  "In the Signature civic system pothole repair is a sworn "
  "mending: every compacted patch a covenant of smooth passage, "
  "every met response time a promise that reports are answered.",
  {"fee": 0, "days": 2, "annual_volume": 60000}),

E("Urban Forestry and Tree Trimming", "Compounded", 24, "compounded",
  "Urban forestry manages the city's living infrastructure: "
  "street and park trees that shade, cool, clean air, and raise "
  "property values — and that fall, heave sidewalks, and tangle "
  "wires when neglected. Certified arborists inventory every "
  "public tree, prune on cycles for structure and clearance, "
  "plant diverse species to resist pests, and remove hazards. "
  "Tree ordinances protect public trees and regulate private "
  "removals; permits govern pruning and planting in rights-of-"
  "way. Storm response clears fallen trees around the clock. A "
  "mature canopy is a decades-long investment paying annual "
  "dividends.",
  "Arborists inventory species, size, and condition in the tree "
  "management system, scheduling pruning by cycle and risk. "
  "Planting programs choose climate-adapted, diverse species "
  "with proper spacing and soil volume. Crews clear sidewalk "
  "conflicts by root pruning or panel replacement. Storm crews "
  "triage blockages and hazards first. Outreach gives residents "
  "trees and care guidance. Canopy assessments from aerial "
  "imagery track the city's green wealth.",
  ["Manage street and park trees as living infrastructure.",
   "Inventory, prune, plant diverse species, remove hazards.",
   "Tree ordinances protect public trees; permits govern work.",
   "Mature canopy pays decades of dividends."],
  ["Pruning must follow ANSI A300 standards.",
   "Removals need documented hazard assessment.",
   "Planting should favor diversity and climate adaptation."],
  ["ANSI A300 (tree care operations).",
   "Local tree ordinances."],
  ["International Society of Arboriculture - best practices.",
   "Arbor Day Foundation - Tree City USA standards."],
  "In the Signature civic system urban forestry is a sworn "
  "tending: every pruned limb a covenant of safety, every "
  "planted tree a promise to a future summer, every saved "
  "canopy a vow kept in green.",
  {"fee": 0, "days": 45, "annual_volume": 12000}),

# ---------------- ADVANCED 25-34 ----------------

E("311 Service Request Systems", "Advanced", 25, "advanced",
  "311 systems are the city's front door for non-emergency "
  "service: one number, one app, one web portal for potholes, "
  "missed trash, broken lights, and graffiti. Born in Baltimore "
  "in 1996 and spread nationwide, 311 takes the request, routes "
  "it to the right department, tracks it to completion, and "
  "reports performance. The data is management gold — heat maps "
  "of complaints reveal failing assets and inequitable service. "
  "Service-level agreements set response targets by request type; "
  "dashboards publish them. 311 keeps 911 lines free for "
  "emergencies while making every request countable.",
  "Call takers and digital channels intake requests with "
  "location, category, and contact. The system routes work orders "
  "to departments, which update status through completion. "
  "Supervisors monitor aging queues against SLAs. Analysts map "
  "request density to target proactive work. Public dashboards "
  "show volumes and response times by neighborhood. Integration "
  "with work management closes the loop from complaint to "
  "completed repair.",
  ["One front door for non-emergency city service.",
   "Routes requests, tracks completion, reports performance.",
   "Complaint heat maps reveal failing assets and inequity.",
   "Keeps 911 free for emergencies."],
  ["Requests need categories, locations, and SLAs.",
   "Departments must update status through completion.",
   "Performance should be published by neighborhood."],
  ["Local 311 service standards.",
   "Accessibility requirements for government communications."],
  ["Bloomberg Philanthropies - 311 and city data guidance.",
   "Local 311 performance reports."],
  "In the Signature civic system 311 is a sworn listening: every "
  "logged request a covenant of attention, every closed ticket a "
  "promise fulfilled, every published dashboard an open account.",
  {"fee": 0, "days": 1, "annual_volume": 1500000}),

E("Zoning Variances", "Advanced", 26, "advanced",
  "A zoning variance is permission to break a dimensional rule — "
  "a smaller setback, a taller fence — when the land's shape or "
  "condition creates a hardship the code never imagined. Boards "
  "of adjustment grant them after public hearings, applying legal "
  "tests: unnecessary hardship, unique conditions, no harm to "
  "neighbors, spirit of the ordinance observed. Variances run "
  "with the land, not the owner. They are the safety valve of "
  "zoning — but overuse signals the code itself needs rewriting. "
  "Use variances (allowing a forbidden use) are barred in many "
  "states.",
  "The owner applies with surveys and hardship evidence; staff "
  "write findings for or against. Neighbors are notified and may "
  "testify at the hearing. The board applies the statutory tests "
  "and grants, conditions, or denies with written findings. "
  "Approvals may expire if unbuilt. Denials can be appealed to "
  "court, which reviews for legal error, not wisdom. Records of "
  "variances build precedent staff cite for years.",
  ["Permission to break dimensional rules on hardship grounds.",
   "Granted by boards of adjustment after public hearings.",
   "Tests: hardship, uniqueness, no neighbor harm, ordinance spirit.",
   "Run with the land; overuse signals code needs rewriting."],
  ["Hardship must be shown under the statutory tests.",
   "Hearings require notice to neighbors.",
   "Findings must be written and supported."],
  ["State zoning enabling acts (variance provisions).",
   "Local board of adjustment rules."],
  ["State variance statutes and case law.",
   "American Planning Association - variance guidance."],
  "In the Signature civic system a variance is a sworn exception: "
  "every granted relief a covenant of measured mercy, every "
  "written finding a promise that exceptions stay exceptional.",
  {"fee": 500, "days": 45, "annual_volume": 900}),

E("Conditional Use Permits", "Advanced", 27, "advanced",
  "Conditional use permits authorize uses the zoning code lists as "
  "acceptable only with review — churches in residential zones, "
  "daycares, drive-throughs, cell towers. The planning commission "
  "holds a hearing, finds the use compatible, and attaches "
  "conditions: hours, landscaping, traffic, noise. Unlike "
  "variances, the use is contemplated by the code; the question "
  "is fit, not exception. Conditions run with the land and are "
  "enforced like law. Revocation follows violations. The permit "
  "is zoning's way of saying yes, carefully.",
  "The applicant files site plans, studies (traffic, noise), and "
  "operations descriptions. Staff analyze compatibility and draft "
  "conditions. The commission hears neighbors and the applicant, "
  "then approves, conditions, or denies with findings. Conditions "
  "— screening walls, limited hours, traffic improvements — are "
  "recorded and inspected. Expansions need amendments. Violations "
  "bring enforcement and possible revocation hearings.",
  ["Authorize code-listed uses only after compatibility review.",
   "Conditions on hours, traffic, noise, landscaping.",
   "Run with the land; enforced like law.",
   "Zoning's way of saying yes, carefully."],
  ["Uses must be listed as conditional in the district.",
   "Findings of compatibility required.",
   "Conditions must be enforceable and monitored."],
  ["Local zoning ordinance (conditional use provisions).",
   "State enabling acts."],
  ["Local conditional use procedures.",
   "American Planning Association - conditional use guidance."],
  "In the Signature civic system a conditional use permit is a "
  "sworn fitting-in: every condition a covenant of good "
  "neighborhood, every hearing a promise that fit is judged "
  "openly.",
  {"fee": 1200, "days": 60, "annual_volume": 400}),

E("Subdivision Review", "Advanced", 28, "advanced",
  "Subdivision review is the city's examination of proposals to "
  "divide land into lots: the planning commission's verdict on "
  "whether the new neighborhood works. Staff check the plat "
  "against the subdivision ordinance — lot sizes, street design, "
  "utilities, drainage, open space, school and park impacts — and "
  "against the comprehensive plan. Public hearings let neighbors "
  "weigh in. Approval comes with conditions and improvement "
  "agreements: the developer builds the streets, sidewalks, and "
  "sewers to city standards, bonded until accepted. Recording "
  "the plat creates the lots.",
  "The developer submits tentative maps, then final plats with "
  "engineering. Departments review concurrently: planning for "
  "design, engineering for streets and drainage, utilities for "
  "service, fire for access. The commission approves, conditions, "
  "or denies with findings. Improvement agreements and bonds "
  "secure the infrastructure; inspectors verify construction. "
  "Final plat recording dedicates streets and creates lots. "
  "Vesting rules protect approved projects from later code "
  "changes.",
  ["City's examination of proposals to divide land.",
   "Checks lots, streets, utilities, drainage, open space.",
   "Developers build infrastructure to city standards, bonded.",
   "Recording the plat creates the lots."],
  ["Plats must meet subdivision ordinance standards.",
   "Improvements need agreements, bonds, and inspection.",
   "Hearings require notice and findings."],
  ["State subdivision map acts.",
   "Local subdivision ordinances."],
  ["American Planning Association - subdivision regulation.",
   "State map acts."],
  "In the Signature civic system subdivision review is a sworn "
  "founding: every approved plat a covenant of a working "
  "neighborhood, every bonded street a promise built before the "
  "first family arrives.",
  {"fee": 2500, "days": 90, "annual_volume": 250}),

E("Site Plan Review", "Advanced", 29, "advanced",
  "Site plan review examines the details of development on a "
  "single lot: building placement, parking, landscaping, lighting, "
  "drainage, and access. Less than a rezoning, more than a "
  "building permit, it is where the city shapes how a project "
  "meets the street. Staff or commissions check compliance with "
  "design standards, then approve with conditions — move the "
  "dumpster, add the sidewalk, shield the lights. Approved plans "
  "bind construction; inspectors verify the site matches the "
  "plan. Good site review prevents a generation of regrets.",
  "The applicant files engineered site plans, landscapes, "
  "lighting photometrics, and traffic details. Staff circulate "
  "to engineering, fire, utilities, and planning. Review checks "
  "setbacks, parking counts, landscaping percentages, lighting "
  "levels, and stormwater. The decision-maker approves, "
  "conditions, or denies with findings. Conditions are bonded "
  "or inspected; as-builts confirm compliance. Amendments handle "
  "field changes.",
  ["Examine development details on a single lot.",
   "Shape placement, parking, landscape, lighting, drainage, access.",
   "Approved plans bind construction.",
   "Prevent a generation of regrets."],
  ["Plans must meet site design standards.",
   "Conditions must be bonded or inspected.",
   "Construction must match the approved plan."],
  ["Local site plan ordinances.",
   "State enabling acts."],
  ["Local site plan manuals.",
   "American Planning Association - site design guidance."],
  "In the Signature civic system site plan review is a sworn "
  "shaping: every approved detail a covenant of good fit, every "
  "conditioned improvement a promise the project serves its "
  "street.",
  {"fee": 1800, "days": 45, "annual_volume": 800}),

E("Code Enforcement", "Advanced", 30, "advanced",
  "Code enforcement keeps neighborhoods from sliding: officers "
  "investigate complaints about junk, weeds, abandoned buildings, "
  "illegal occupancy, and unpermitted work, and bring properties "
  "into compliance. The process runs notice, hearing, orders, and "
  "fines — with liens securing unpaid penalties against the "
  "property. Proactive programs target vacant buildings and "
  "chronic offenders. The best enforcement is educational first: "
  "many violations come from ignorance, not defiance. But the "
  "teeth must be real, or the worst properties never change.",
  "Officers inspect on complaint or proactively, document "
  "violations with photos, and issue notices giving time to "
  "comply. Reinspection verifies; continued violation brings "
  "citations, administrative hearings, and fines. Liens attach "
  "unpaid penalties. Abatement crews can clean dangerous lots "
  "and bill the owner. Receivership and demolition address the "
  "worst buildings. Data targets hot spots and measures "
  "compliance rates.",
  ["Investigate and correct property violations.",
   "Process: notice, hearing, orders, fines, liens.",
   "Education first; real teeth for chronic offenders.",
   "Targets junk, weeds, vacant buildings, illegal work."],
  ["Notice and hearing rights must be honored.",
   "Fines must follow adopted schedules.",
   "Liens require proper recording."],
  ["Local property maintenance codes.",
   "State administrative hearing procedures."],
  ["International Property Maintenance Code.",
   "Local code enforcement manuals."],
  "In the Signature civic system code enforcement is a sworn "
  "keeping: every notice a covenant of fair warning, every "
  "complied property a promise renewed, every lien a vow that "
  "neglect has a price.",
  {"fee": 0, "days": 30, "annual_volume": 22000}),

E("Animal Control", "Advanced", 31, "advanced",
  "Animal control protects people from animals and animals from "
  "people: officers respond to bites, strays, cruelty, and "
  "dangerous dogs, operating shelters that house, reunite, and "
  "rehome. Licensing and rabies vaccination rules create the "
  "paper trail of responsible ownership. Dangerous-dog hearings "
  "can restrict or remove animals after due process. Cruelty "
  "investigations build criminal cases. Modern programs push "
  "live-release rates through adoption, foster, and trap-neuter-"
  "return for community cats. Bite quarantines protect public "
  "health.",
  "Officers patrol, answer calls, and enforce licensing, leash, "
  "and nuisance ordinances. Shelters intake strays and surrenders, "
  "scan for chips, hold for owner reclaim, then adopt out. "
  "Veterinarians spay, neuter, and vaccinate. Cruelty officers "
  "investigate and refer prosecutions. Dangerous-dog cases get "
  "hearings with appeal rights. Bite reports trigger ten-day "
  "quarantines and rabies follow-up.",
  ["Protect people from animals and animals from people.",
   "Respond to bites, strays, cruelty, dangerous dogs.",
   "Operate shelters: house, reunite, rehome.",
   "Licensing and rabies rules track responsible ownership."],
  ["Seizures must follow ordinance and due process.",
   "Dangerous-dog findings need hearings with appeals.",
   "Bite quarantines must follow health rules."],
  ["Local animal control ordinances.",
   "State rabies control laws."],
  ["National Animal Care and Control Association - guidelines.",
   "State public health rabies manuals."],
  "In the Signature civic system animal control is a sworn "
  "guardianship: every reunited pet a covenant of care, every "
  "cruelty case a promise of justice, every adopted animal a vow "
  "of second chances.",
  {"fee": 25, "days": 3, "annual_volume": 30000}),

E("Parking Enforcement", "Advanced", 32, "advanced",
  "Parking enforcement keeps the curb working: officers patrol "
  "for expired meters, illegal parking, blocked hydrants and "
  "driveways, and street-cleaning violations, issuing citations "
  "that turn over spaces and fund the system. Beyond tickets, "
  "enforcement clears fire lanes, bus stops, and accessible "
  "spaces — the violations that endanger. License-plate "
  "recognition automates scofflaw detection; boots and tows "
  "handle the chronic. Appeals go through administrative "
  "hearings. Fair, consistent enforcement is the difference "
  "between a managed curb and a free-for-all.",
  "Officers patrol beats on schedules tied to demand, marking "
  "and citing violations with handhelds that photograph evidence. "
  "Supervisors review contested tickets; hearings officers decide "
  "appeals. Scofflaw programs boot or tow after threshold unpaid "
  "tickets. Accessible-space violations carry the highest fines "
  "by law. Data on citation locations guides deployment and "
  "pricing decisions.",
  ["Keep the curb working through fair enforcement.",
   "Clear fire lanes, bus stops, accessible spaces.",
   "LPR automates scofflaw detection; boots and tows handle chronic.",
   "Appeals through administrative hearings."],
  ["Citations need documented evidence.",
   "Appeals require hearings with notice.",
   "Accessible-space fines follow statutory minimums."],
  ["Local parking ordinances.",
   "State vehicle code parking provisions."],
  ["International Parking and Mobility Institute - enforcement guidance.",
   "Local parking enforcement manuals."],
  "In the Signature civic system parking enforcement is a sworn "
  "ordering of the curb: every fair ticket a covenant of "
  "turnover, every cleared hydrant a promise of safety, every "
  "heard appeal a vow of fairness.",
  {"fee": 45, "days": 1, "annual_volume": 400000}),

E("Public Health Inspections", "Advanced", 33, "advanced",
  "Public health inspections guard what people eat, drink, and "
  "touch: sanitarians inspect restaurants, food trucks, pools, "
  "tattoo shops, and lodging on risk-based schedules. The FDA "
  "Food Code, adopted by states, sets the standards — temperatures, "
  "handwashing, pest control, certified managers. Inspections "
  "score violations; critical ones demand immediate correction "
  "or closure. Reports go public online, and grades in windows "
  "let diners vote with their feet. Outbreak investigations trace "
  "illness to its source and stop it.",
  "Sanitarians schedule by risk category, inspect unannounced, "
  "and document violations with temperatures and photos. "
  "Critical violations trigger reinspection or closure; "
  "operators correct and verify. Scores and reports publish "
  "online. Foodborne-illness complaints trigger investigations "
  "with lab coordination and traceback. Plan review approves new "
  "facilities before opening. Certified food-manager rules put "
  "trained eyes in every kitchen.",
  ["Inspect restaurants, food trucks, pools, lodging on risk schedules.",
   "FDA Food Code sets the standards.",
   "Critical violations demand immediate correction or closure.",
   "Reports public; grades let diners choose."],
  ["Inspections must follow risk-based frequencies.",
   "Closures need documented imminent health hazards.",
   "Reports must be public."],
  ["FDA Food Code (adopted by states).",
   "State food and pool codes."],
  ["U.S. Food and Drug Administration - Food Code.",
   "State environmental health manuals."],
  "In the Signature civic system health inspection is a sworn "
  "watch over the table: every thermometer reading a covenant "
  "of safety, every posted grade a promise of honesty, every "
  "stopped outbreak a vow kept.",
  {"fee": 350, "days": 14, "annual_volume": 18000}),

E("Fire Inspections", "Advanced", 34, "advanced",
  "Fire inspections prevent the fire before the alarm: inspectors "
  "walk businesses, apartments, and assembly occupancies checking "
  "exits, alarms, sprinklers, extinguishers, storage, and hazards. "
  "The International Fire Code, adopted locally, sets the rules; "
  "high-hazard occupancies get annual visits, low-risk less often. "
  "Violations bring correction orders and reinspection; imminent "
  "dangers bring immediate action. Plan review of new construction "
  "and events extends prevention to the drawing board. Every "
  "corrected violation is a fire that may never happen.",
  "Inspectors schedule by occupancy risk, walk the premises "
  "against code checklists, and document violations with orders "
  "and deadlines. Reinspection verifies correction; chronic "
  "violations bring citations and fines. Operational permits — "
  "for hazmats, tents, fireworks — get pre-event inspection. "
  "New construction plans are reviewed for fire protection "
  "systems before permits issue. Public education multiplies "
  "every inspection's reach.",
  ["Prevent fires through occupancy inspections.",
   "Check exits, alarms, sprinklers, extinguishers, hazards.",
   "Risk-based frequencies; imminent dangers get immediate action.",
   "Plan review extends prevention to new construction."],
  ["Inspections must follow adopted fire code.",
   "Violations need orders, deadlines, reinspection.",
   "Imminent hazards authorize immediate action."],
  ["International Fire Code.",
   "NFPA 1 and inspection standards."],
  ["International Code Council - fire code.",
   "National Fire Protection Association - standards."],
  "In the Signature civic system fire inspection is a sworn "
  "prevention: every clear exit a covenant of escape, every "
  "tested sprinkler a promise of water, every corrected hazard "
  "a fire that never was.",
  {"fee": 200, "days": 10, "annual_volume": 25000}),
]
