#!/usr/bin/env python3
"""PHASE M — accidents-insurance-proven (public) seed entries.

Accident records with verified documentation ONLY. Every record carries an
explicit verification level as a record field:
  official-investigation — formal investigation report by an official body
  insurance-documented  — documented through insurance/compensation claims records
  publicly-reported     — documented through reputable public reporting and public records

Scholarly tone; aggregate figures only; no victim names; no graphic detail.

Tuple: (key, group, title, desc, points, req, standards, citations, demo_kind, verification)
"""

OFFICIAL = "official-investigation"
INSURED = "insurance-documented"
PUBLIC = "publicly-reported"

ENTRIES = [
# ================= OFFICIAL-INVESTIGATION (22) =================
("charkhi-dadri-1996", "official-investigation-records",
 "Charkhi Dadri Mid-Air Collision — 1996",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the formal court of "
 "inquiry report of the Directorate General of Civil Aviation (India). On November "
 "12, 1996, Saudi Arabian Airlines Flight 763 and Kazakhstan Airlines Flight 1907 "
 "collided in mid-air near Charkhi Dadri, India, killing all 349 people aboard "
 "both aircraft — the deadliest mid-air collision in history. The inquiry found "
 "the Kazakh crew descended below its assigned altitude in poor visibility, with "
 "contributing factors including inadequate English proficiency and the absence "
 "of secondary surveillance radar. The accident drove mandatory TCAS equipage "
 "and English-proficiency standards worldwide.",
 ("Verification: formal DGCA court of inquiry report (India)",
  "349 fatalities — deadliest mid-air collision in history",
  "Cause finding: Kazakh aircraft descended below assigned altitude",
  "Contributing: language proficiency; lack of secondary radar",
  "Safety outcomes: worldwide TCAS mandate; ICAO English-proficiency requirements",
  "Civil and military airspace coordination reforms in the region"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "cause findings; safety outcomes; cross-references to related records; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "ICAO English language proficiency requirements"),
 "Directorate General of Civil Aviation (India) — public court of inquiry report (public record).",
 "investigation", OFFICIAL),

("aa191-1979", "official-investigation-records",
 "American Airlines Flight 191 — 1979",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the NTSB public "
 "aircraft accident report. On May 25, 1979, American Airlines Flight 191, a "
 "McDonnell Douglas DC-10 departing Chicago O'Hare, lost its left engine and "
 "pylon on takeoff, then rolled and crashed, killing all 271 people aboard and "
 "2 on the ground. The NTSB found the probable cause was the separation of the "
 "engine pylon from maintenance damage — American's forklift-based engine-change "
 "procedure had cracked the pylon structure — combined with the asymmetric "
 "stall characteristics that followed. The FAA briefly grounded the DC-10 "
 "fleet; maintenance procedures for engine removal were rewritten industry-wide.",
 ("Verification: NTSB public aircraft accident report",
  "273 total fatalities (271 aboard, 2 on the ground)",
  "Probable cause: engine-pylon separation from maintenance-induced damage",
  "Aircraft: McDonnell Douglas DC-10-10",
  "Safety outcomes: DC-10 fleet grounding and review; engine-change procedure reforms",
  "Maintenance-damage inspection requirements strengthened"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "maintenance-procedure analysis; probable-cause determination; safety outcomes; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA maintenance procedure standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "causetree", OFFICIAL),

("turkish981-1974", "official-investigation-records",
 "Turkish Airlines Flight 981 — 1974",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the French BEA "
 "public investigation report. On March 3, 1974, Turkish Airlines Flight 981, "
 "a McDonnell Douglas DC-10 flying from Paris to London, crashed in the "
 "Ermenonville forest after the aft cargo door blew out, collapsing the cabin "
 "floor and severing control cables. All 346 people aboard were killed. The "
 "investigation found the cargo-door latch design allowed the door to appear "
 "locked when it was not, and that a recommended fix had not been mandated. "
 "The accident forced redesign of the DC-10 cargo door and floor venting, and "
 "established the principle that known design defects must be corrected by "
 "airworthiness directive.",
 ("Verification: French BEA public investigation report",
  "346 fatalities",
  "Cause finding: cargo-door blowout from a latch design that could indicate locked when unlatched",
  "Known defect not corrected by mandatory directive before the accident",
  "Safety outcomes: cargo-door redesign; floor-venting requirements; airworthiness-directive reform",
  "Aircraft: McDonnell Douglas DC-10-10"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "design-defect analysis; regulatory-history review; cause findings; safety outcomes; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "FAA airworthiness directive process"),
 "French Bureau of Enquiry and Analysis for Civil Aviation Safety (BEA) — public report (public record).",
 "causetree", OFFICIAL),

("lac-megantic-2013", "official-investigation-records",
 "Lac-Mégantic Rail Disaster — 2013",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the Transportation "
 "Safety Board of Canada public investigation report. On July 6, 2013, an "
 "unattended 73-car freight train carrying crude oil rolled downhill and "
 "derailed in downtown Lac-Mégantic, Quebec; multiple tank cars exploded and "
 "burned, killing 47 people and destroying much of the town center. The TSB "
 "identified 18 causes and contributing factors, centering on inadequate "
 "handbrakes, the lack of a backup safety system, weak regulatory oversight, "
 "and a poor safety culture at the railway. The disaster transformed crude-oil "
 "transport regulation in North America.",
 ("Verification: Transportation Safety Board of Canada public report",
  "47 fatalities; town center destroyed",
  "Causes: unattended train; insufficient handbrakes; no backup safety system; weak oversight",
  "Operator: Montreal, Maine and Atlantic Railway",
  "Safety outcomes: crude-oil tank-car standards (DOT-117); operating-practice reforms",
  "Documented as 18 causes and contributing factors"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "multi-cause analysis; regulatory findings; safety outcomes; source citations.",
 ("Transportation Safety Board of Canada investigation standards",
  "North American tank-car safety standards"),
 "Transportation Safety Board of Canada (TSB) — public investigation report (public record).",
 "investigation", OFFICIAL),

("amtrak188-2015", "official-investigation-records",
 "Amtrak Train 188 Derailment — 2015",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the NTSB public "
 "railroad accident report. On May 12, 2015, Amtrak Northeast Regional Train "
 "188 derailed on a curve in Philadelphia while traveling 106 mph where the "
 "limit was 50 mph, killing 8 people and injuring many of the 250 aboard. The "
 "NTSB found the probable cause was the engineer's acceleration to excessive "
 "speed, likely due to loss of situational awareness after being distracted by "
 "a nearby commuter-train emergency. The probable cause statement explicitly "
 "noted that positive train control, had it been in place, would have "
 "prevented the accident — accelerating PTC implementation nationwide.",
 ("Verification: NTSB public railroad accident report",
  "8 fatalities; train entered a 50-mph curve at 106 mph",
  "Probable cause: excessive speed from loss of situational awareness",
  "NTSB finding: positive train control would have prevented the accident",
  "Safety outcomes: accelerated positive train control implementation",
  "Location: Philadelphia, Pennsylvania"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "speed and signal analysis; human-factors analysis; probable-cause determination; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FRA positive train control requirements"),
 "U.S. National Transportation Safety Board (NTSB) — public railroad accident report (public record).",
 "timeline", OFFICIAL),

("santiago-compostela-2013", "official-investigation-records",
 "Santiago de Compostela Train Derailment — 2013",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the Spanish "
 "railway accident investigation commission (CIAF) public report. On July 24, "
 "2013, an Alvia high-speed train derailed on a sharp curve approaching "
 "Santiago de Compostela station in Spain while traveling far above the "
 "curve's speed limit, killing 79 people. The investigation found the driver "
 "was distracted by a phone call and failed to brake, and that the line "
 "lacked automatic speed supervision at the critical curve. The accident led "
 "to automatic braking installation at the site and a national review of "
 "high-speed line transitions.",
 ("Verification: Spanish CIAF public investigation report",
  "79 fatalities",
  "Cause findings: excessive speed; driver distraction; no automatic speed supervision at the curve",
  "Safety outcomes: automatic braking at the site; national transition-zone review",
  "Location: Santiago de Compostela, Spain"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "speed analysis; supervision-system review; cause findings; safety outcomes; source citations.",
 ("Spanish railway investigation standards",
  "European train control system deployment standards"),
 "Spanish Railway Accident Investigation Commission (CIAF) — public report (public record).",
 "verify", OFFICIAL),

("costa-concordia-2012", "official-investigation-records",
 "Costa Concordia Grounding — 2012",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the Italian "
 "official marine casualty investigation and subsequent court proceedings "
 "(public record). On January 13, 2012, the cruise ship Costa Concordia "
 "struck a reef off Giglio Island, Italy, during an unauthorized close pass to "
 "shore; the ship capsized, killing 32 people among the more than 4,200 aboard. "
 "The investigation found the master deliberately deviated from the planned "
 "route, delayed the abandon-ship order, and left the vessel before evacuation "
 "was complete. The disaster prompted review of voyage planning, bridge "
 "resource management, and muster-drill timing across the cruise industry.",
 ("Verification: Italian official marine casualty investigation and public court record",
  "32 fatalities of more than 4,200 aboard",
  "Cause findings: deliberate route deviation; delayed evacuation order",
  "Safety outcomes: voyage-planning oversight; muster-drill timing reforms",
  "Vessel: Costa Concordia, off Giglio Island, Italy"),
 "A complete record requires: verification level stated; occurrence data; official investigation citation; "
 "bridge-management analysis; evacuation analysis; cause findings; safety outcomes; source citations.",
 ("IMO casualty investigation code",
  "SOLAS voyage-planning requirements"),
 "Italian official marine casualty investigation — public report and court record (public record).",
 "investigation", OFFICIAL),

("sewol-2014", "official-investigation-records",
 "Sewol Ferry Sinking — 2014",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the official "
 "Korean investigation reports and public inquiry records. On April 16, 2014, "
 "the ferry Sewol capsized and sank off South Korea, killing 304 people — most "
 "of them high-school students. Official investigations found the vessel was "
 "overloaded with improperly secured cargo, had reduced ballast, and turned too "
 "sharply; the crew's delayed evacuation order proved fatal. The disaster "
 "prompted sweeping reforms of Korean maritime safety regulation, vessel "
 "loading oversight, and emergency-response coordination.",
 ("Verification: Korean official investigation and inquiry reports",
  "304 fatalities, most of them students",
  "Cause findings: overloading; improper ballast; sharp turn; delayed evacuation order",
  "Safety outcomes: Korean maritime regulatory overhaul; loading oversight reforms",
  "Vessel: Sewol, off the southwest coast of South Korea"),
 "A complete record requires: verification level stated; occurrence data; official report citations; "
 "stability and loading analysis; evacuation analysis; cause findings; safety outcomes; source citations.",
 ("IMO casualty investigation code",
  "SOLAS stability and loading requirements"),
 "Korean official investigation reports — public inquiry record (public record).",
 "timeline", OFFICIAL),

("deepwater-horizon-2010", "official-investigation-records",
 "Deepwater Horizon Explosion — 2010",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in multiple official "
 "reports, including the U.S. Chemical Safety Board investigation and the "
 "National Commission on the BP Deepwater Horizon Oil Spill. On April 20, 2010, "
 "a blowout on the Deepwater Horizon drilling rig in the Gulf of Mexico killed "
 "11 workers and triggered one of the largest marine oil spills in history. "
 "Official findings cited a cascade of failures: a defective cement job, "
 "misread pressure tests, and a blowout preventer that did not function. The "
 "disaster drove offshore drilling safety reforms and the reorganization of "
 "U.S. offshore regulation.",
 ("Verification: U.S. Chemical Safety Board and National Commission public reports",
  "11 workers killed; major marine oil spill",
  "Cause findings: cement failure; misinterpreted well tests; blowout preventer failure",
  "Safety outcomes: offshore drilling safety reforms; U.S. offshore regulatory reorganization",
  "Location: Gulf of Mexico, April 20, 2010"),
 "A complete record requires: verification level stated; occurrence data; official report citations; "
 "well-control analysis; equipment-failure analysis; cause findings; safety outcomes; source citations.",
 ("U.S. Chemical Safety Board investigation standards",
  "Offshore drilling safety regulations"),
 "U.S. Chemical Safety Board and National Commission — public reports (public record).",
 "causetree", OFFICIAL),

("texas-city-2005", "official-investigation-records",
 "Texas City Refinery Explosion — 2005",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the U.S. Chemical "
 "Safety Board public investigation report. On March 23, 2005, a hydrocarbon "
 "vapor cloud exploded at BP's Texas City, Texas, refinery during the startup "
 "of an isomerization unit, killing 15 workers and injuring about 180. The CSB "
 "found organizational and safety deficiencies at all levels: a history of "
 "cost-cutting, inadequate training, and a blowdown drum venting to atmosphere "
 "in a populated area. The Baker Panel review that followed became a landmark "
 "in process-safety culture assessment.",
 ("Verification: U.S. Chemical Safety Board public report",
  "15 fatalities; about 180 injuries",
  "Cause findings: startup procedure failures; atmospheric venting; organizational safety deficiencies",
  "Safety outcomes: Baker Panel safety-culture review; process-safety management reforms",
  "Location: Texas City, Texas"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "process-safety analysis; organizational-culture findings; cause findings; safety outcomes; source citations.",
 ("U.S. Chemical Safety Board investigation standards",
  "OSHA process safety management standard"),
 "U.S. Chemical Safety Board — public investigation report (public record).",
 "verify", OFFICIAL),

("bhopal-1984", "official-investigation-records",
 "Bhopal Gas Tragedy — 1984",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in Indian official "
 "inquiry reports and extensive public judicial records. In December 1984, a "
 "leak of methyl isocyanate gas from the Union Carbide pesticide plant in "
 "Bhopal, India, killed thousands of people in surrounding communities and "
 "injured hundreds of thousands — the world's worst industrial disaster. "
 "Official inquiries found a combination of poor maintenance, disabled safety "
 "systems, inadequate training, and cost-cutting. The tragedy reshaped global "
 "chemical-process safety law, including community right-to-know provisions "
 "worldwide.",
 ("Verification: Indian official inquiry reports; public judicial record",
  "Thousands of fatalities; hundreds of thousands injured — worst industrial disaster on record",
  "Cause findings: disabled safety systems; poor maintenance; inadequate training and oversight",
  "Safety outcomes: global process-safety law; community right-to-know provisions",
  "Location: Bhopal, India, December 1984"),
 "A complete record requires: verification level stated; occurrence data; official inquiry citations; "
 "process-safety analysis; judicial-record summary; cause findings; safety outcomes; source citations.",
 ("Indian official inquiry standards",
  "Global process-safety management principles"),
 "Indian official inquiry reports — public record (public record).",
 "investigation", OFFICIAL),

("herald-free-enterprise-1987", "official-investigation-records",
 "Herald of Free Enterprise Capsizing — 1987",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the UK formal "
 "investigation (Sheen Report), a public record. On March 6, 1987, the roll-on/"
 "roll-off ferry Herald of Free Enterprise capsized moments after leaving "
 "Zeebrugge, Belgium, with its bow doors open, killing 193 people. The Sheen "
 "inquiry found the immediate cause was the failure to close the bow doors, "
 "but its landmark finding was the 'disease of sloppiness' — a corporate "
 "culture in which safety warnings went unheeded from ship to boardroom. The "
 "report's safety-management findings led directly to the International Safety "
 "Management (ISM) Code.",
 ("Verification: UK formal investigation — the Sheen Report (public record)",
  "193 fatalities",
  "Immediate cause: sailing with bow doors open",
  "Landmark finding: corporate 'disease of sloppiness' — safety-management failure",
  "Safety outcomes: International Safety Management (ISM) Code",
  "Vessel: Herald of Free Enterprise, off Zeebrugge, Belgium"),
 "A complete record requires: verification level stated; occurrence data; formal report citation; "
 "immediate-cause analysis; safety-management findings; safety outcomes; source citations.",
 ("UK formal marine investigation standards",
  "IMO International Safety Management Code"),
 "UK Department of Transport formal investigation — Sheen Report (public record).",
 "causetree", OFFICIAL),

("piper-alpha-1988", "official-investigation-records",
 "Piper Alpha Platform Explosion — 1988",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the UK public "
 "inquiry (Cullen Report). On July 6, 1988, explosions and fire destroyed the "
 "Piper Alpha oil platform in the North Sea, killing 167 workers — the "
 "world's worst offshore oil disaster. The Cullen inquiry found that a "
 "condensate pump had been restarted without knowing a safety valve had been "
 "removed for maintenance, and identified fundamental failures in permit-to-work "
 "systems, safety management, and regulatory oversight. Its 106 recommendations "
 "rebuilt the UK offshore safety regime around goal-setting regulation and "
 "safety cases.",
 ("Verification: UK public inquiry — the Cullen Report",
  "167 fatalities — worst offshore oil disaster",
  "Cause findings: permit-to-work failure; removed safety valve; management-system failures",
  "Safety outcomes: UK offshore safety-case regime; goal-setting regulation",
  "Location: North Sea, July 6, 1988"),
 "A complete record requires: verification level stated; occurrence data; public inquiry citation; "
 "permit-system analysis; management findings; recommendations summary; safety outcomes; source citations.",
 ("UK public inquiry standards",
  "UK offshore safety-case regulations"),
 "UK public inquiry — Cullen Report (public record).",
 "reclog", OFFICIAL),

("kings-cross-1987", "official-investigation-records",
 "King's Cross Station Fire — 1987",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the UK public "
 "inquiry (Fennell Report). On November 18, 1987, a fire in the King's Cross "
 "St Pancras Underground station in London — likely started by a discarded "
 "match on a wooden escalator — developed into a flashover that killed 31 "
 "people. The Fennell inquiry's landmark finding was the 'trench effect,' a "
 "previously unrecognized fire phenomenon on escalators, alongside failures in "
 "staff training, emergency procedures, and management. The report transformed "
 "fire safety across underground railways worldwide.",
 ("Verification: UK public inquiry — the Fennell Report",
  "31 fatalities",
  "Landmark finding: the 'trench effect' fire phenomenon on escalators",
  "Cause findings: ignition on wooden escalator; training and procedure failures",
  "Safety outcomes: wooden escalator replacement; underground fire-safety standards",
  "Location: London Underground, November 18, 1987"),
 "A complete record requires: verification level stated; occurrence data; public inquiry citation; "
 "fire-phenomenon findings; management findings; safety outcomes; source citations.",
 ("UK public inquiry standards",
  "Underground railway fire-safety standards"),
 "UK public inquiry — Fennell Report (public record).",
 "investigation", OFFICIAL),

("kegworth-1989", "official-investigation-records",
 "Kegworth Air Disaster (British Midland Flight 92) — 1989",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the UK Air "
 "Accidents Investigation Branch public report. On January 8, 1989, British "
 "Midland Flight 92, a Boeing 737-400 diverting to East Midlands Airport after "
 "an engine problem, crashed short of the runway, killing 47 of the 126 people "
 "aboard. The crew mistakenly shut down the healthy engine instead of the "
 "damaged one — a misidentification compounded by unfamiliarity with the new "
 "737-400 engine instruments and vibration indicators. The accident became a "
 "foundational case in cockpit instrument design and crew training for engine "
 "failure identification.",
 ("Verification: UK AAIB public report",
  "47 fatalities of 126 occupants",
  "Cause finding: wrong-engine shutdown after misidentifying the damaged engine",
  "Contributing: unfamiliar 737-400 instrumentation; vibration-indicator design",
  "Safety outcomes: engine-instrument redesign; failure-identification training",
  "Location: Kegworth, England"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "instrument-design analysis; crew-action analysis; cause findings; safety outcomes; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "Cockpit instrument human-factors standards"),
 "UK Air Accidents Investigation Branch (AAIB) — public report (public record).",
 "verify", OFFICIAL),

("united173-1978", "official-investigation-records",
 "United Airlines Flight 173 — 1978",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the NTSB public "
 "aircraft accident report. On December 28, 1978, United Flight 173, a DC-8 "
 "approaching Portland, Oregon, circled while troubleshooting a landing-gear "
 "problem until it ran out of fuel and crashed, killing 10 of the 189 people "
 "aboard. The NTSB found the probable cause was the crew's failure to monitor "
 "fuel state while preoccupied — the captain's fixation and the crew's "
 "reluctance to challenge him. The accident is credited as the direct catalyst "
 "for United's development of Cockpit Resource Management, the precursor to "
 "modern CRM.",
 ("Verification: NTSB public aircraft accident report",
  "10 fatalities of 189 occupants — fuel exhaustion",
  "Probable cause: failure to monitor fuel during prolonged troubleshooting",
  "Human factors: captain fixation; crew reluctance to challenge",
  "Safety outcomes: birth of Cockpit Resource Management (CRM)",
  "Aircraft: McDonnell Douglas DC-8"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "fuel-state analysis; crew-coordination analysis; probable-cause determination; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA crew resource management standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "timeline", OFFICIAL),

("avianca52-1990", "official-investigation-records",
 "Avianca Flight 52 — 1990",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the NTSB public "
 "aircraft accident report. On January 25, 1990, Avianca Flight 52, a Boeing "
 "707 from Bogotá to New York, ran out of fuel and crashed on Long Island "
 "after extended holding, killing 73 of the 158 people aboard. The NTSB found "
 "the probable cause was the crew's failure to declare a fuel emergency — "
 "language and communication barriers meant controllers never understood the "
 "severity — combined with traffic delays and inadequate fuel planning. The "
 "accident drove reforms in emergency phraseology and fuel-reserve policy.",
 ("Verification: NTSB public aircraft accident report",
  "73 fatalities of 158 occupants — fuel exhaustion",
  "Probable cause: failure to declare a fuel emergency; communication barriers",
  "Contributing: holding delays; fuel planning",
  "Safety outcomes: emergency-phraseology reforms; fuel-reserve policy review",
  "Aircraft: Boeing 707-321B"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "communication analysis; fuel-planning review; probable-cause determination; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "ICAO emergency phraseology standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "causetree", OFFICIAL),

("airinter148-1992", "official-investigation-records",
 "Air Inter Flight 148 — 1992",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the French "
 "investigation commission's public report. On January 20, 1992, Air Inter "
 "Flight 148, an Airbus A320 approaching Strasbourg, descended into the Vosges "
 "mountains, killing 87 of the 96 people aboard. The investigation found the "
 "crew had inadvertently selected vertical-speed mode instead of flight-path-"
 "angle mode on the autopilot — the two modes displayed similarly — causing a "
 "descent rate far steeper than intended. The accident became a landmark in "
 "cockpit automation interface design and led to display changes on Airbus "
 "aircraft.",
 ("Verification: French investigation commission public report",
  "87 fatalities of 96 occupants",
  "Cause finding: wrong autopilot vertical mode selected — similar displays for different modes",
  "Safety outcomes: Airbus display redesign; automation-interface human-factors standards",
  "Aircraft: Airbus A320-111; location: Vosges mountains, France"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "interface-design analysis; crew-action analysis; cause findings; safety outcomes; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "Cockpit automation human-factors standards"),
 "French investigation commission — public report (public record).",
 "investigation", OFFICIAL),

("sanbruno-2010", "official-investigation-records",
 "San Bruno Pipeline Explosion — 2010",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the NTSB public "
 "pipeline accident report. On September 9, 2010, a 30-inch natural gas "
 "transmission pipeline ruptured and exploded in a residential neighborhood of "
 "San Bruno, California, killing 8 people and destroying 38 homes. The NTSB "
 "found the probable cause was a defective pipe segment installed in 1956 with "
 "inadequate welds, combined with PG&E's inadequate integrity-management "
 "program and the California regulator's weak oversight. The accident drove "
 "national pipeline records-verification requirements.",
 ("Verification: NTSB public pipeline accident report",
  "8 fatalities; 38 homes destroyed",
  "Probable cause: defective 1956 pipe segment; inadequate integrity management",
  "Contributing: weak regulatory oversight of records and testing",
  "Safety outcomes: pipeline records verification mandates; integrity-assessment reforms",
  "Location: San Bruno, California"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "pipe-defect analysis; integrity-program review; probable-cause determination; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "PHMSA pipeline integrity management rules"),
 "U.S. National Transportation Safety Board (NTSB) — public pipeline accident report (public record).",
 "verify", OFFICIAL),

("airflorida90-1982", "official-investigation-records",
 "Air Florida Flight 90 — 1982",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the NTSB public "
 "aircraft accident report. On January 13, 1982, Air Florida Flight 90, a "
 "Boeing 737 departing Washington National Airport in a snowstorm, failed to "
 "gain altitude, struck the 14th Street Bridge, and crashed into the Potomac "
 "River, killing 78 people including 4 motorists on the bridge. The NTSB found "
 "the probable cause was the crew's failure to de-ice the aircraft and to "
 "reject the takeoff despite clear signs of icing — including engine "
 "instrument readings the crew misread. The accident transformed winter "
 "operations: de-icing procedures, holdover times, and crew winter training.",
 ("Verification: NTSB public aircraft accident report",
  "78 total fatalities (74 aboard, 4 motorists)",
  "Probable cause: failure to de-ice; failure to reject takeoff with iced wings",
  "Contributing: misread engine instruments; inadequate winter procedures",
  "Safety outcomes: de-icing and anti-icing programs; holdover-time tables; winter crew training",
  "Aircraft: Boeing 737-222; location: Potomac River, Washington"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "icing analysis; crew-decision analysis; probable-cause determination; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA winter-operations and de-icing standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "timeline", OFFICIAL),

("egyptair804-2016", "official-investigation-records",
 "EgyptAir Flight 804 — 2016",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the Egyptian "
 "Aircraft Accident Investigation Administration's public reporting on the "
 "occurrence. On May 19, 2016, EgyptAir Flight 804, an Airbus A320 flying from "
 "Paris to Cairo, was lost over the Mediterranean Sea with all 66 people "
 "aboard. ACARS messages indicated smoke in the avionics bay and lavatory "
 "before the aircraft disappeared from radar; wreckage and recorders were "
 "recovered from the sea. The investigation examined fire scenarios including "
 "an oxygen-mask-related ignition hypothesis reported by investigators. The "
 "occurrence remains a reference case for in-flight fire investigation over "
 "water.",
 ("Verification: Egyptian Aircraft Accident Investigation Administration public reporting",
  "66 fatalities; wreckage recovered from the Mediterranean",
  "Evidence: ACARS smoke warnings; flight-recorder data",
  "Investigation examined fire scenarios; ignition hypotheses reported but contested",
  "Safety outcomes: continued in-flight fire research; recorder recovery capabilities",
  "Aircraft: Airbus A320-232"),
 "A complete record requires: verification level stated; occurrence data; official reporting citation; "
 "fire-scenario analysis; evidence inventory; findings as reported; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "In-flight fire investigation standards"),
 "Egyptian Aircraft Accident Investigation Administration — public reporting (public record).",
 "investigation", OFFICIAL),

# ================= INSURANCE-DOCUMENTED (14) =================
("gm-compensation-fund", "insurance-documented-records",
 "GM Ignition-Switch Compensation Fund Record",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented through the "
 "independent compensation program administered by Kenneth Feinberg for "
 "General Motors, a public claims record. Following GM's delayed recall of "
 "vehicles with defective ignition switches, the company established a "
 "compensation fund that approved 124 death claims and hundreds of injury "
 "claims linked to the defect. The fund's published protocols, eligibility "
 "criteria, and aggregate claim statistics constitute one of the most detailed "
 "public insurance-style documentation sets for an auto defect — showing how "
 "compensation programs verify causation claim by claim.",
 ("Verification: independent compensation administrator's public claims record",
  "124 death claims approved; hundreds of injury claims",
  "Documentation: published protocols, eligibility criteria, aggregate statistics",
  "Causation verified claim by claim against defect criteria",
  "Demonstrates insurance-style documentation of a product defect",
  "Related: GM ignition-switch cases in the crash investigation database"),
 "A complete record requires: verification level stated; fund establishment documents; "
 "protocol and criteria summary; aggregate claim statistics; causation-verification method; source citations.",
 ("Compensation-fund protocol standards (published)",
  "TREAD Act early-warning reporting"),
 "Independent compensation administrator — public fund reports (public record).",
 "verify", INSURED),

("takata-victim-funds", "insurance-documented-records",
 "Takata Airbag Victim Compensation Records",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented through victim "
 "compensation funds and multidistrict litigation records, all public court "
 "records. The defective Takata inflators were linked in public reports to "
 "dozens of deaths and hundreds of injuries worldwide; compensation was "
 "structured through funds established in Takata's bankruptcy and through "
 "automaker settlements. Court filings document the claims process, "
 "eligibility, and aggregate payouts — a public insurance record of how mass "
 "product-defect injuries are compensated across jurisdictions.",
 ("Verification: public court records — bankruptcy funds and multidistrict litigation",
  "Dozens of deaths and hundreds of injuries linked in public reports",
  "Compensation via bankruptcy-established funds and automaker settlements",
  "Claims process, eligibility, and aggregates documented in filings",
  "Cross-jurisdiction compensation model for a global defect"),
 "A complete record requires: verification level stated; fund structures; court-record citations; "
 "aggregate injury data; claims-process description; source citations.",
 ("Bankruptcy claims-administration standards",
  "Multidistrict litigation procedures (public)"),
 "U.S. federal court records — Takata bankruptcy and MDL proceedings (public record).",
 "reclog", INSURED),

("grimshaw-v-ford", "insurance-documented-records",
 "Grimshaw v. Ford — Pinto Litigation Record",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in the published "
 "court opinion and public trial record of Grimshaw v. Ford Motor Co. (1981). "
 "The case arose from a Pinto rear-impact fire; the jury awarded compensatory "
 "damages and $125 million in punitive damages (later reduced), after Ford's "
 "internal cost-benefit memo on the fuel-tank hazard became public evidence. "
 "The published opinion documents the defect evidence, the company's knowledge "
 "timeline, and the legal standard for punitive damages — the foundational "
 "public record linking product-liability litigation to safety regulation.",
 ("Verification: published court opinion and public trial record",
  "Punitive damages initially $125 million (reduced on appeal)",
  "Internal cost-benefit memo entered as public evidence",
  "Documents defect knowledge timeline and corporate decision-making",
  "Foundational product-liability record for auto safety"),
 "A complete record requires: verification level stated; case citation; defect evidence summary; "
 "damages history; legal standards applied; source citations.",
 ("California product-liability law (as applied in the published opinion)",
  "Public trial-record documentation standards"),
 "Grimshaw v. Ford Motor Co. — published court opinion (public record).",
 "investigation", INSURED),

("johns-manville-trust", "insurance-documented-records",
 "Johns-Manville Asbestos Personal Injury Trust",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in the public trust "
 "distribution procedures and annual reports of the Manville Personal Injury "
 "Settlement Trust. After Johns-Manville's bankruptcy over asbestos liabilities, "
 "the trust became the claims mechanism for hundreds of thousands of asbestos "
 "injury claims, with published medical criteria, payment schedules, and audit "
 "procedures. The trust record demonstrates how insurance-style claims "
 "administration documents long-latency occupational injuries at scale — with "
 "disease categories, exposure criteria, and scheduled values all public.",
 ("Verification: public trust distribution procedures and annual reports",
  "Hundreds of thousands of claims administered",
  "Published medical criteria and payment schedules",
  "Documents long-latency occupational injury at scale",
  "Model for mass-toxic-tort claims administration"),
 "A complete record requires: verification level stated; trust establishment summary; "
 "medical criteria; payment schedules; audit procedures; aggregate statistics; source citations.",
 ("Trust distribution procedures (public)",
  "Bankruptcy claims-administration standards"),
 "Manville Personal Injury Settlement Trust — public procedures and reports (public record).",
 "stats", INSURED),

("exxon-valdez-litigation", "insurance-documented-records",
 "Exxon Valdez Civil Litigation and Settlement Record",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in the public court "
 "record of In re Exxon Valdez, including the jury's original $5 billion "
 "punitive award and the decades of appeals ending near $500 million. The 1989 "
 "tanker grounding spilled about 11 million gallons of crude oil into Prince "
 "William Sound, Alaska. The litigation record documents environmental damage "
 "claims, the allocation of compensatory damages to fishermen and communities, "
 "and the legal standards for punitive damages in maritime cases — a complete "
 "public insurance record of a catastrophic spill's civil aftermath.",
 ("Verification: public federal court record",
  "Punitive award: $5 billion reduced through appeals to about $500 million",
  "Spill: about 11 million gallons, Prince William Sound, 1989",
  "Documents environmental and economic damage claims at scale",
  "Maritime punitive-damages standards developed in the record"),
 "A complete record requires: verification level stated; spill facts; case history; "
 "damages allocation; legal standards; source citations.",
 ("Federal maritime damages law (as applied)",
  "Oil Pollution Act claims framework"),
 "U.S. federal court records — Exxon Valdez litigation (public record).",
 "timeline", INSURED),

("gulf-coast-claims-facility", "insurance-documented-records",
 "Gulf Coast Claims Facility — Deepwater Horizon",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in the public reports "
 "of the Gulf Coast Claims Facility and the subsequent court-supervised "
 "settlement program. BP established a $20 billion trust to compensate "
 "individuals and businesses harmed by the 2010 Deepwater Horizon spill; the "
 "facility processed hundreds of thousands of claims with published protocols. "
 "The claims record — eligibility rules, documentation requirements, payment "
 "statistics — is the largest public insurance-style documentation set for an "
 "environmental disaster's economic aftermath.",
 ("Verification: public claims-facility and settlement-program reports",
  "$20 billion trust established",
  "Hundreds of thousands of claims processed",
  "Published eligibility rules and documentation requirements",
  "Largest public claims record for an environmental disaster"),
 "A complete record requires: verification level stated; trust establishment; protocol summary; "
 "claim statistics; documentation requirements; source citations.",
 ("Claims-facility protocol standards (published)",
  "Oil Pollution Act claims framework"),
 "Gulf Coast Claims Facility — public reports (public record).",
 "reclog", INSURED),

("toyota-settlements", "insurance-documented-records",
 "Toyota Unintended-Acceleration Settlement Records",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in the public "
 "Department of Justice deferred-prosecution agreement ($1.2 billion, 2014) "
 "and public civil-settlement records. Beyond the NHTSA/NASA engineering "
 "investigation, the financial-documentation record shows how unintended-"
 "acceleration claims were resolved: the DOJ agreement's statement of facts, "
 "civil class settlements, and individual injury claims. Together they form "
 "the insurance-documented layer of the episode — who paid, under what "
 "admissions, and through what claims process.",
 ("Verification: public DOJ agreement and civil-settlement records",
  "$1.2 billion deferred-prosecution agreement (2014)",
  "Statement of facts published as part of the agreement",
  "Civil class and individual injury settlements documented",
  "Insurance layer of the unintended-acceleration episode"),
 "A complete record requires: verification level stated; agreement terms; statement of facts; "
 "civil settlement summary; claims-process description; source citations.",
 ("DOJ deferred-prosecution standards (public)",
  "Federal class-settlement procedures"),
 "U.S. Department of Justice — public agreement (public record).",
 "verify", INSURED),

("ford-firestone-settlements", "insurance-documented-records",
 "Ford/Firestone Tire Litigation Settlement Records",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in public court "
 "records of the tire tread-separation litigation wave of the early 2000s. "
 "Beyond the recalls and the TREAD Act, hundreds of injury and death claims "
 "from Firestone tire failures on Ford Explorers were resolved through "
 "settlements documented in public filings. The litigation record captures "
 "tire-aging evidence, inflation-pressure disputes, and vehicle-handling "
 "analysis — the insurance-documented complement to the regulatory record of "
 "the defect.",
 ("Verification: public court records of tire-failure litigation",
  "Hundreds of injury and death claims resolved",
  "Documents tire-aging and pressure evidence",
  "Insurance complement to the NHTSA regulatory record",
  "Settlement patterns show claims valuation for rollover injuries"),
 "A complete record requires: verification level stated; defect background; litigation scope; "
 "evidence themes; settlement documentation; source citations.",
 ("State product-liability procedures (public)",
  "TREAD Act claims-reporting framework"),
 "Public court records — tire-failure litigation (public record).",
 "investigation", INSURED),

("september-11-vcf", "insurance-documented-records",
 "September 11th Victim Compensation Fund",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in the public "
 "regulations, protocols, and award statistics of the federal September 11th "
 "Victim Compensation Fund. Created by Congress, the fund provided "
 "compensation to victims and families without litigation, using published "
 "economic-loss formulas, non-economic award schedules, and collateral-offset "
 "rules. Its public record — thousands of claims, published methodology, and "
 "special-master reports — is the definitive documentation of how a no-fault "
 "federal compensation system values catastrophic loss.",
 ("Verification: federal regulations, protocols, and award statistics (public)",
  "No-fault federal compensation — alternative to litigation",
  "Published economic-loss formulas and award schedules",
  "Thousands of claims with special-master reporting",
  "Definitive model of federal catastrophic-loss compensation"),
 "A complete record requires: verification level stated; statutory basis; methodology summary; "
 "claim statistics; special-master reports; source citations.",
 ("VCF regulations and protocols (public)",
  "Federal compensation-fund administration standards"),
 "September 11th Victim Compensation Fund — public regulations and reports (public record).",
 "stats", INSURED),

("mgm-grand-litigation", "insurance-documented-records",
 "MGM Grand Fire Litigation Record — 1980",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in the public court "
 "records of the civil litigation following the November 21, 1980, MGM Grand "
 "hotel fire in Las Vegas, which killed 85 people. The litigation established "
 "the liability of the hotel's owners and contractors for fire-safety "
 "deficiencies and produced settlements distributed to victims and families "
 "through court-supervised processes. The case record documents the fire's "
 "spread through unprotected vertical openings — findings that paralleled the "
 "official fire investigation and drove high-rise fire-code reform.",
 ("Verification: public court records of fire litigation",
  "85 fatalities, November 21, 1980, Las Vegas",
  "Court-supervised settlements to victims and families",
  "Documents fire-spread through unprotected vertical openings",
  "Litigation record paralleled official fire-investigation findings"),
 "A complete record requires: verification level stated; fire facts; case history; "
 "liability findings; settlement documentation; code-reform outcomes; source citations.",
 ("Nevada civil-procedure public records",
  "High-rise fire-code standards (post-fire reforms)"),
 "Public court records — MGM Grand fire litigation (public record).",
 "timeline", INSURED),

("station-nightclub-settlements", "insurance-documented-records",
 "Station Nightclub Fire Settlement Records — 2003",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in public court "
 "records of the civil settlements following the February 20, 2003, Station "
 "nightclub fire in West Warwick, Rhode Island, which killed 100 people. "
 "Settlements from the club owners, the band's management, the town, and "
 "material suppliers totaled well over $100 million, distributed through "
 "court-supervised processes. The litigation record documents pyrotechnic "
 "use, flammable soundproofing foam, overcrowding, and blocked exits — the "
 "insurance-documented layer beneath the criminal and official findings.",
 ("Verification: public court records of civil settlements",
  "100 fatalities, February 20, 2003, West Warwick, Rhode Island",
  "Settlements well over $100 million from multiple defendants",
  "Documents pyrotechnics, flammable foam, overcrowding, exits",
  "Insurance layer beneath criminal and official findings"),
 "A complete record requires: verification level stated; fire facts; defendant scope; "
 "settlement documentation; contributing-factor findings; source citations.",
 ("Rhode Island civil-procedure public records",
  "Nightclub fire-code standards (post-fire reforms)"),
 "Public court records — Station nightclub fire settlements (public record).",
 "verify", INSURED),

("imperial-sugar-claims", "insurance-documented-records",
 "Imperial Sugar Refinery Explosion Claims — 2008",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in workers' "
 "compensation records and public civil-settlement filings following the "
 "February 7, 2008, sugar-dust explosion at the Imperial Sugar refinery in "
 "Port Wentworth, Georgia, which killed 14 workers. The claims record — "
 "workers' compensation awards, third-party settlements, and OSHA penalty "
 "proceedings (public) — documents combustible-dust hazards as an insurable "
 "industrial risk. The explosion also drove OSHA's combustible-dust enforcement "
 "emphasis and renewed rulemaking efforts.",
 ("Verification: workers' compensation records; public settlement filings; OSHA proceedings",
  "14 fatalities, February 7, 2008, Port Wentworth, Georgia",
  "Combustible-dust hazard documented as an insurable industrial risk",
  "Claims record complements the CSB's official investigation",
  "Drove OSHA combustible-dust enforcement emphasis"),
 "A complete record requires: verification level stated; explosion facts; claims documentation; "
 "OSHA proceedings; hazard findings; source citations.",
 ("Workers' compensation claims procedures (public)",
  "OSHA combustible-dust enforcement guidance"),
 "Public claims and OSHA records — Imperial Sugar explosion (public record).",
 "reclog", INSURED),

("lac-megantic-victim-fund", "insurance-documented-records",
 "Lac-Mégantic Victim Compensation Fund",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in the public "
 "settlement-fund records arising from the railway's bankruptcy proceedings. "
 "After the 2013 Lac-Mégantic derailment, the Montreal, Maine and Atlantic "
 "Railway's bankruptcy produced a victim compensation fund of approximately "
 "$460 million Canadian, contributed by the railway, its insurers, and other "
 "settling parties, distributed to victims, families, and the town. The fund "
 "record — allocation formulas, claimant categories, distribution reports — "
 "is the insurance-documented complement to the TSB's official investigation.",
 ("Verification: public bankruptcy settlement-fund records",
  "Fund of approximately $460 million Canadian",
  "Contributors: railway, insurers, and settling parties",
  "Documents allocation formulas and claimant categories",
  "Insurance complement to the TSB official investigation"),
 "A complete record requires: verification level stated; fund establishment; contributor scope; "
 "allocation documentation; distribution reports; source citations.",
 ("Canadian bankruptcy claims procedures (public)",
  "Settlement-fund administration standards"),
 "Public bankruptcy court records — Lac-Mégantic settlement fund (public record).",
 "stats", INSURED),

("aviation-hull-liability-claims", "insurance-documented-records",
 "Aviation Hull and Liability Claims Documentation",
 "VERIFICATION LEVEL: INSURANCE-DOCUMENTED — documented in the public "
 "literature of aviation insurance practice and published claims-handling "
 "standards. Every commercial aircraft crash generates a parallel insurance "
 "record: hull loss adjustment, passenger liability claims under the Montreal "
 "Convention's strict-liability framework, and subrogation among insurers, "
 "manufacturers, and operators. This record documents the claims process "
 "itself — notification, investigation coordination with official bodies, "
 "valuation methods, and settlement patterns — as the insurance layer present "
 "in every major aviation accident.",
 ("Verification: published aviation-insurance practice literature and claims standards",
  "Montreal Convention strict-liability framework for passenger claims",
  "Hull adjustment, liability claims, and subrogation documented as a process",
  "Insurance investigation runs parallel to official investigations",
  "The insurance layer present in every major aviation accident"),
 "A complete record requires: verification level stated; convention framework; claims-process stages; "
 "valuation methods; coordination with official investigations; source citations.",
 ("Montreal Convention (1999) liability framework",
  "Published aviation claims-handling standards"),
 "International aviation insurance practice literature — public standards (public record).",
 "investigation", INSURED),

# ================= PUBLICLY-REPORTED (14) =================
("copiapo-2010", "publicly-reported-records",
 "Copiapó Mining Accident and Rescue — 2010",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented through Chilean "
 "government briefings and extensive reputable international press coverage. "
 "On August 5, 2010, a cave-in at the San José copper-gold mine near Copiapó, "
 "Chile, trapped 33 miners underground; all were rescued after 69 days in an "
 "operation watched worldwide. The public record documents the collapse, the "
 "borehole contact, the rescue shaft drilling, and the miners' survival — "
 "alongside subsequent official Chilean inquiries into mine safety regulation. "
 "The rescue remains the benchmark case for mine emergency response.",
 ("Verification: government briefings; reputable international press coverage",
  "33 miners trapped; all 33 rescued after 69 days",
  "Public record: collapse, contact, rescue drilling, survival",
  "Subsequent Chilean official inquiries into mine regulation",
  "Benchmark case for mine emergency response"),
 "A complete record requires: verification level stated; event timeline from public sources; "
 "rescue-operation documentation; inquiry outcomes; source citations.",
 ("Chilean mine-safety regulations (post-event reforms)",
  "International mine-rescue guidance"),
 "Chilean government briefings; reputable international press archives (public record).",
 "timeline", PUBLIC),

("tham-luang-2018", "publicly-reported-records",
 "Tham Luang Cave Rescue — 2018",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented through Thai government "
 "briefings and extensive reputable international press coverage. In "
 "June-July 2018, 12 boys and their coach were trapped by flooding in the Tham "
 "Luang cave in Thailand; an international dive-rescue operation extracted all "
 "13 over three days. The public record documents the search, the diving "
 "plan, the sedation-and-extraction method, and the multinational cooperation — "
 "a rescue studied worldwide for cave-diving medicine and incident command.",
 ("Verification: Thai government briefings; reputable international press coverage",
  "13 people trapped; all 13 extracted over three days",
  "Public record: search, dive plan, extraction method, cooperation",
  "Studied for cave-diving medicine and incident command",
  "One rescuer fatality documented in the public record"),
 "A complete record requires: verification level stated; event timeline from public sources; "
 "rescue-method documentation; cooperation record; source citations.",
 ("Cave-diving rescue practice (as publicly documented)",
  "Incident-command system principles"),
 "Thai government briefings; reputable international press archives (public record).",
 "investigation", PUBLIC),

("andes-1972", "publicly-reported-records",
 "Andes Flight Disaster — 1972",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented through survivor "
 "accounts, published memoirs, and extensive reputable press coverage, with "
 "Uruguayan Air Force search records as the official backbone. On October 13, "
 "1972, a Uruguayan Air Force charter carrying a rugby team crashed in the "
 "Andes; 16 of the 45 aboard survived 72 days before rescue. The public record "
 "documents the crash, the survivors' ordeal, and the two survivors' trek for "
 "help — one of the most documented survival events in aviation history.",
 ("Verification: survivor accounts and memoirs; reputable press; Uruguayan Air Force search records",
  "16 survivors of 45 aboard; 72 days before rescue",
  "Public record: crash, ordeal, trek for help",
  "Among the most documented survival events in aviation",
  "Search-and-rescue lessons in mountainous terrain"),
 "A complete record requires: verification level stated; event facts from public sources; "
 "survival-account documentation; search-record summary; source citations.",
 ("Mountain search-and-rescue practice (as publicly documented)",
  "Aviation survival literature"),
 "Survivor memoirs; reputable press archives; Uruguayan Air Force search records (public record).",
 "timeline", PUBLIC),

("hindenburg-1937", "publicly-reported-records",
 "Hindenburg Disaster — 1937",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented through contemporary "
 "press coverage, newsreel footage, and the published findings of the U.S. "
 "Commerce Department inquiry, with the historical record carried by public "
 "archives. On May 6, 1937, the airship Hindenburg caught fire while landing "
 "at Lakehurst, New Jersey, killing 36 people. The inquiry could not "
 "definitively establish the ignition source; the hydrogen lifting gas made "
 "the fire unsurvivable for many. The disaster ended the commercial airship "
 "era and remains the iconic case of hydrogen fire risk in public memory.",
 ("Verification: contemporary press; newsreel record; published Commerce Department inquiry findings",
  "36 fatalities, May 6, 1937, Lakehurst, New Jersey",
  "Ignition source never definitively established",
  "Ended the commercial rigid-airship era",
  "Iconic hydrogen fire-risk case"),
 "A complete record requires: verification level stated; event facts; inquiry findings; "
 "historical documentation; source citations.",
 ("U.S. airship operation standards of the era (historical)",
  "Hydrogen safety principles (modern reference)"),
 "U.S. Commerce Department inquiry — published findings; public news archives (public record).",
 "investigation", PUBLIC),

("grand-canyon-1956", "publicly-reported-records",
 "Grand Canyon Mid-Air Collision — 1956",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented through the Civil "
 "Aeronautics Board investigation's published findings and extensive "
 "contemporary press coverage. On June 30, 1956, TWA Flight 2 and United "
 "Flight 718 collided over the Grand Canyon, killing all 128 people aboard "
 "both aircraft. The CAB found the probable cause was the pilots' failure to "
 "see each other in uncontrolled airspace. The disaster directly created the "
 "Federal Aviation Agency (now FAA) and modern positive air-traffic control.",
 ("Verification: CAB published findings; contemporary press coverage",
  "128 fatalities — deadliest U.S. commercial aviation disaster of its era",
  "Probable cause: failure to see and avoid in uncontrolled airspace",
  "Directly created the Federal Aviation Agency and positive ATC",
  "Wreckage unrecovered for years; historical documentation extensive"),
 "A complete record requires: verification level stated; event facts; CAB findings; "
 "regulatory outcomes; source citations.",
 ("CAB investigation standards of the era (historical)",
  "Federal Aviation Act of 1958 (regulatory outcome)"),
 "Civil Aeronautics Board — published findings; public press archives (public record).",
 "causetree", PUBLIC),

("park-slope-1960", "publicly-reported-records",
 "Park Slope Mid-Air Collision — 1960",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented through the Civil "
 "Aeronautics Board investigation's published findings and extensive "
 "contemporary press coverage. On December 16, 1960, United Flight 826 and TWA "
 "Flight 266 collided over New York City; the United aircraft crashed in Park "
 "Slope, Brooklyn, killing all 128 people aboard both aircraft and 6 on the "
 "ground — 134 total. The CAB found the United aircraft had strayed beyond its "
 "clearance limits at excessive speed. The disaster accelerated air-traffic "
 "control modernization and flight-recorder requirements.",
 ("Verification: CAB published findings; contemporary press coverage",
  "134 total fatalities (128 aboard, 6 on the ground)",
  "Cause finding: United aircraft beyond clearance limits at excessive speed",
  "Accelerated ATC modernization and recorder requirements",
  "Location: Brooklyn, New York, December 16, 1960"),
 "A complete record requires: verification level stated; event facts; CAB findings; "
 "regulatory outcomes; source citations.",
 ("CAB investigation standards of the era (historical)",
  "FAA flight-recorder requirements (regulatory outcome)"),
 "Civil Aeronautics Board — published findings; public press archives (public record).",
 "timeline", PUBLIC),

("wire-service-documentation", "publicly-reported-records",
 "Wire-Service Documentation of Breaking Transport Disasters",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — this record documents the "
 "documentation method itself, as practiced by international wire services and "
 "reputable newsrooms. When a transport disaster breaks, wire services build "
 "the first public record through a disciplined pipeline: verified casualty "
 "figures from authorities, official statements clearly attributed, "
 "eyewitness accounts labeled as such, and corrections issued openly. This "
 "record describes the standards — two-source verification, attribution "
 "discipline, and correction practice — that make wire copy the citable public "
 "layer of accident documentation.",
 ("Verification: published newsroom standards and stylebooks",
  "Pipeline: authority figures, attributed statements, labeled eyewitness accounts",
  "Standards: two-source verification; attribution discipline; open corrections",
  "Wire copy as the citable public layer of accident documentation",
  "Applies to aviation, rail, maritime, and industrial disasters alike"),
 "A complete record requires: verification level stated; pipeline description; "
 "standards summary; correction-practice documentation; source citations.",
 ("Published wire-service standards and stylebooks",
  "Press-association reporting guidelines"),
 "International wire-service standards — public stylebooks (public record).",
 "verify", PUBLIC),

("commercial-aviation-rates", "publicly-reported-records",
 "Public Statistical Record: Commercial Aviation Accident Rates",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented in the public "
 "statistical summaries published by Boeing, ICAO, and IATA. These annual "
 "publications track worldwide commercial-jet accident and fatality rates "
 "across decades, showing the long-term decline that makes modern scheduled "
 "aviation the safest transport mode per passenger-mile. The statistical "
 "record — hull-loss rates by generation, fatality trends, regional "
 "comparisons — is the public quantitative backbone against which individual "
 "accidents are understood.",
 ("Verification: public statistical summaries (Boeing, ICAO, IATA)",
  "Tracks worldwide jet accident and fatality rates across decades",
  "Documents the long-term decline in accident rates",
  "Hull-loss rates by aircraft generation; regional comparisons",
  "The quantitative backbone for understanding individual accidents"),
 "A complete record requires: verification level stated; publisher scope; metrics definitions; "
 "trend summary; use in safety analysis; source citations.",
 ("ICAO safety-report methodology (public)",
  "IATA annual safety-report methodology (public)"),
 "Boeing statistical summary; ICAO safety report; IATA annual review (public records).",
 "stats", PUBLIC),

("crowdsourced-video-documentation", "publicly-reported-records",
 "Crowdsourced Video as Accident Documentation",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented in the public "
 "literature on open-source investigation. Dashcam, CCTV, and bystander video "
 "now routinely provide the first visual evidence of crashes — capturing "
 "vehicle speeds, signal states, and sequences that no official sensor "
 "recorded. This record documents the verification method: geolocation, "
 "time-sync, and chain-of-custody practices that let public video serve as "
 "evidence, plus the ethical rules for handling footage involving victims. "
 "Open-source methods have corroborated and occasionally corrected official "
 "timelines.",
 ("Verification: public open-source investigation literature",
  "Sources: dashcam, CCTV, bystander video",
  "Method: geolocation, time-sync, chain of custody",
  "Ethical rules for victim-involving footage",
  "Has corroborated and corrected official timelines"),
 "A complete record requires: verification level stated; source types; verification method; "
 "ethical rules; relationship to official investigations; source citations.",
 ("Open-source investigation verification standards (public)",
  "Video-evidence handling guidelines"),
 "Public open-source investigation literature (public record).",
 "verify", PUBLIC),

("historical-press-archives", "publicly-reported-records",
 "Historical Newspaper Archives as Accident Documentation",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented in the public practice "
 "of historical research. For accidents that predate modern investigation "
 "bodies, digitized newspaper archives are often the primary surviving "
 "record: they preserve casualty lists, contemporary official statements, "
 "inquest findings, and public reaction. This record documents the method — "
 "cross-edition comparison, date verification, and corroboration against "
 "official gazettes — and its limits: early reporting errors, sensationalism, "
 "and gaps. Used rigorously, press archives recover accidents history would "
 "otherwise lose.",
 ("Verification: public historical-research practice",
  "Primary surviving record for pre-modern accidents",
  "Preserves casualty lists, statements, inquest findings",
  "Method: cross-edition comparison; gazette corroboration",
  "Limits: early errors, sensationalism, gaps"),
 "A complete record requires: verification level stated; archive scope; method description; "
 "limits documentation; source citations.",
 ("Historical research methodology (public)",
  "Newspaper digitization and archive standards"),
 "Public historical-research literature and digitized archives (public record).",
 "investigation", PUBLIC),

("asn-public-database", "publicly-reported-records",
 "Aviation Safety Network Public Database",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented in the published "
 "methodology of the Aviation Safety Network (ASN), an independent public "
 "database of aviation accidents. ASN compiles occurrence records from "
 "official reports, press coverage, and contributor submissions, with each "
 "entry showing its sources. With tens of thousands of occurrences indexed, "
 "it is the most-used public reference for accident lookup — demonstrating "
 "how a publicly-reported database achieves reliability through source "
 "transparency rather than official authority.",
 ("Verification: ASN published methodology and sourcing practice",
  "Tens of thousands of occurrences indexed",
  "Each entry shows its sources — transparency as reliability",
  "Most-used public reference for accident lookup",
  "Model: public database without official authority"),
 "A complete record requires: verification level stated; database scope; methodology; "
 "sourcing practice; reliability model; source citations.",
 ("ASN database methodology (public)",
  "Public-database sourcing standards"),
 "Aviation Safety Network — public methodology (public record).",
 "stats", PUBLIC),

("baaa-public-archive", "publicly-reported-records",
 "Bureau of Aircraft Accidents Archives Public Record",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented in the published "
 "operations of the Bureau of Aircraft Accidents Archives (B3A), a public "
 "archive of aircraft accident records maintained in Geneva. The archive "
 "collects official reports, press records, and photographs for tens of "
 "thousands of occurrences, making historical accident documentation "
 "accessible to researchers. This record describes the archive's collection "
 "method, access model, and role as the public memory of aviation accidents — "
 "particularly for occurrences whose official files are incomplete or "
 "inaccessible.",
 ("Verification: B3A published operations and access model",
  "Tens of thousands of occurrences archived",
  "Collects official reports, press, and photographs",
  "Public memory for incomplete official files",
  "Research-access model documented"),
 "A complete record requires: verification level stated; archive scope; collection method; "
 "access model; research role; source citations.",
 ("B3A archive operations (public)",
  "Aviation archive preservation standards"),
 "Bureau of Aircraft Accidents Archives — public operations record (public record).",
 "reclog", PUBLIC),

("foia-accident-documentation", "publicly-reported-records",
 "Public-Records Requests and Accident Documentation",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented in the public "
 "literature on freedom-of-information practice. Public-records requests "
 "(such as FOIA in the United States) routinely surface accident "
 "documentation that would otherwise stay inside agencies: investigation "
 "correspondence, inspection histories, and enforcement files. This record "
 "documents the request method — targeted requests, appeal practice, and "
 "exemption limits — and landmark disclosures that changed the public "
 "understanding of accidents. It is the mechanism by which the public record "
 "grows after the official report is closed.",
 ("Verification: public FOI literature and disclosed records",
  "Surfaces correspondence, inspections, enforcement files",
  "Method: targeted requests; appeals; exemption limits",
  "Landmark disclosures documented",
  "Grows the public record after reports close"),
 "A complete record requires: verification level stated; legal framework; method description; "
 "disclosure examples; limits; source citations.",
 ("FOIA procedures (public law)",
  "Public-records journalism standards"),
 "Public FOI literature and disclosed government records (public record).",
 "verify", PUBLIC),

("memorialization-records", "publicly-reported-records",
 "Memorialization and Public Remembrance Records",
 "VERIFICATION LEVEL: PUBLICLY-REPORTED — documented in the public record "
 "of memorials, anniversaries, and remembrance practices. Societies document "
 "accidents not only in reports but in memorials, museum exhibits, annual "
 "ceremonies, and survivor networks — a public layer that preserves the human "
 "meaning of events the technical record reduces to findings. This record "
 "describes memorialization practice: what gets memorialized, who decides, "
 "and how remembrance records serve victims' families and public learning — "
 "with dignity and without sensationalism.",
 ("Verification: public record of memorials and remembrance practice",
  "Memorials, museums, ceremonies, survivor networks",
  "Preserves human meaning alongside technical findings",
  "Documents what societies choose to remember",
  "Conducted with dignity, without sensationalism"),
 "A complete record requires: verification level stated; memorialization forms; "
 "decision processes; family and learning roles; source citations.",
 ("Memorial design and curation practice (public)",
  "Museum ethics standards (public)"),
 "Public memorial and museum records (public record).",
 "investigation", PUBLIC),
("crossair3597-2001", "official-investigation-records",
 "Crossair Flight 3597 — 2001",
 "VERIFICATION LEVEL: OFFICIAL-INVESTIGATION — documented in the Swiss "
 "Aircraft Accident Investigation Bureau public report. On November 24, 2001, "
 "Crossair Flight 3597, an Avro RJ100 approaching Zurich in poor visibility, "
 "descended below the minimum descent altitude and struck terrain, killing 24 "
 "of the 33 people aboard. The investigation found the crew continued the "
 "approach below minimums without adequate visual reference, with contributing "
 "factors in crew training, airline safety culture, and approach-procedure "
 "design. The accident drove reforms in Swiss aviation oversight and "
 "controlled-flight-into-terrain prevention.",
 ("Verification: Swiss Aircraft Accident Investigation Bureau public report",
  "24 fatalities of 33 occupants",
  "Cause finding: descent below minimum altitude without visual reference",
  "Contributing: training, safety culture, procedure design",
  "Safety outcomes: Swiss oversight reforms; CFIT-prevention emphasis",
  "Aircraft: Avro RJ100; location: near Zurich, Switzerland"),
 "A complete record requires: verification level stated; occurrence data; official report citation; "
 "approach analysis; organizational findings; cause findings; safety outcomes; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "CFIT-prevention approach-procedure standards"),
 "Swiss Aircraft Accident Investigation Bureau — public report (public record).",
 "causetree", OFFICIAL),
]
