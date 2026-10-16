#!/usr/bin/env python3
"""PHASE M — crash-data-databases (public) seed entries.

Public crash investigation records: NTSB-style documentation — aircraft/vehicle,
cause findings, safety outcomes, recommendations. Scholarly tone; aggregate
casualty figures only; no victim names; no graphic detail.

Tuple: (key, group, title, desc, points, req, standards, citations, demo_kind, verification)
verification is None here (crash DB); the accidents DB carries it as a record field.
"""

ENTRIES = [
# ============================ AVIATION (30) ============================
("tenerife-1977", "aviation-investigations",
 "Tenerife Airport Disaster — 1977",
 "On March 27, 1977, KLM Flight 4805 and Pan Am Flight 1736, both Boeing 747s, "
 "collided on the runway at Los Rodeos Airport, Tenerife, Canary Islands, during "
 "takeoff in dense fog. All 248 people aboard the KLM aircraft and 335 of the 396 "
 "aboard the Pan Am aircraft were killed, for a total of 583 fatalities — the "
 "deadliest accident in aviation history. The Spanish investigation found that the "
 "KLM captain began the takeoff roll without takeoff clearance, amid "
 "miscommunications between the crews and air traffic control compounded by fog "
 "and radio interference.",
 ("Probable cause: KLM takeoff without clearance; contributing: fog, ambiguous ATC phraseology, radio congestion",
  "583 fatalities — the highest toll of any aviation accident",
  "Aircraft: KLM Boeing 747-206B and Pan Am Boeing 747-121",
  "Safety outcomes: ICAO standardized phraseology ('takeoff' reserved for clearance); crew resource management programs",
  "Safety outcomes: ground radar (ASDE) requirements; sterile cockpit emphasis",
  "Investigating body: Spanish Civil Aviation Accident Investigation Commission (CIAIAC), with Dutch and U.S. participation"),
 "A complete investigation record requires: occurrence date and location; both aircraft identifications; "
 "meteorological conditions; ATC transcript summary; factual sequence; analysis of communications; "
 "probable-cause determination; safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "ICAO standardized radiotelephony phraseology"),
 "Spanish Civil Aviation Accident Investigation Commission (CIAIAC) — public final report (public record); "
 "ICAO circular documentation of the occurrence.",
 "investigation", None),

("jal123-1985", "aviation-investigations",
 "Japan Air Lines Flight 123 — 1985",
 "On August 12, 1985, Japan Air Lines Flight 123, a Boeing 747SR flying from Tokyo "
 "to Osaka, suffered an explosive decompression 12 minutes after takeoff when the "
 "aft pressure bulkhead failed. The failure severed all four hydraulic systems and "
 "tore away the vertical stabilizer, leaving the crew with essentially no flight "
 "controls. The aircraft remained airborne for about 32 minutes before striking "
 "Mount Takamagahara; 520 of the 524 people aboard were killed — the deadliest "
 "single-aircraft accident in history. The Japanese investigation traced the "
 "bulkhead failure to an improper repair performed seven years earlier after a "
 "tailstrike.",
 ("Probable cause: improper repair of the aft pressure bulkhead leading to fatigue cracking and in-flight failure",
  "520 fatalities of 524 occupants — deadliest single-aircraft accident",
  "Aircraft: Boeing 747-146SR, registration JA8119",
  "Crew controlled the aircraft for 32 minutes using differential engine thrust alone",
  "Safety outcomes: strengthened oversight of structural repairs; aging-aircraft inspection programs",
  "Investigating body: Japan Aircraft Accident Investigation Commission (AAIC)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification and maintenance "
 "history; structural failure sequence; crew actions; probable-cause determination; "
 "safety recommendations on repair oversight; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "Boeing structural repair manual standards (as referenced by the investigation)"),
 "Japan Aircraft Accident Investigation Commission (AAIC) — public final report (public record).",
 "causetree", None),

("af447-2009", "aviation-investigations",
 "Air France Flight 447 — 2009",
 "On June 1, 2009, Air France Flight 447, an Airbus A330 flying from Rio de Janeiro "
 "to Paris, was lost over the Atlantic Ocean with all 228 people aboard. The "
 "aircraft's pitot tubes iced over in a thunderstorm, causing autopilot disconnect "
 "and inconsistent airspeed readings; the crew's control inputs led to an "
 "aerodynamic stall from which the aircraft did not recover. Wreckage and flight "
 "recorders were recovered from the ocean floor nearly two years later. The French "
 "BEA investigation issued 41 safety recommendations.",
 ("Probable cause: crew handling following loss of airspeed indications — failure to recognize and recover from a sustained stall",
  "228 fatalities; wreckage located on the ocean floor in 2011",
  "Aircraft: Airbus A330-203",
  "Contributing: pitot-tube icing in convective weather; startle and mode awareness in manual flight",
  "Safety outcomes: fleet-wide pitot-tube replacement; upset-recovery and high-altitude stall training mandates",
  "Investigating body: French Bureau of Enquiry and Analysis for Civil Aviation Safety (BEA)"),
 "A complete investigation record requires: occurrence date and route; aircraft and crew information; "
 "flight-recorder data summary; meteorological analysis; human-factors analysis; "
 "probable-cause determination; numbered safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "EASA certification standards for airspeed sensing"),
 "French Bureau of Enquiry and Analysis for Civil Aviation Safety (BEA) — public final report (public record).",
 "timeline", None),

("mh370-2014", "aviation-investigations",
 "Malaysia Airlines Flight 370 — 2014",
 "On March 8, 2014, Malaysia Airlines Flight 370, a Boeing 777 flying from Kuala "
 "Lumpur to Beijing with 239 people aboard, deviated from its planned route and "
 "disappeared. Satellite communications data indicated the aircraft flew on for "
 "hours over the Indian Ocean; only scattered debris has been recovered. The "
 "Malaysian ICAO Annex 13 safety investigation team released its final report in "
 "2018 without determining the cause of the disappearance — a documented instance "
 "of an investigation concluding with cause undetermined. The occurrence drove "
 "global adoption of enhanced aircraft tracking standards.",
 ("Cause: undetermined — the investigation's final report states the cause of the disappearance could not be established",
  "239 people aboard; aircraft not recovered",
  "Aircraft: Boeing 777-200ER",
  "Evidence basis: satellite handshake data, radar traces, recovered debris",
  "Safety outcomes: ICAO Global Aeronautical Distress and Safety System (GADSS) — 15-minute normal tracking and autonomous distress tracking standards",
  "Investigating body: Malaysian ICAO Annex 13 Safety Investigation Team for MH370"),
 "A complete investigation record requires: occurrence date and last known position; aircraft identification; "
 "all evidence streams (radar, satellite, debris); analysis of each hypothesis; "
 "explicit statement where cause is undetermined; safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "ICAO GADSS concept of operations"),
 "Malaysian ICAO Annex 13 Safety Investigation Team for MH370 — public final report (public record).",
 "investigation", None),

("twa800-1996", "aviation-investigations",
 "TWA Flight 800 — 1996",
 "On July 17, 1996, TWA Flight 800, a Boeing 747 flying from New York to Paris, "
 "broke apart over the Atlantic Ocean off Long Island shortly after takeoff, "
 "killing all 230 people aboard. After a four-year investigation, the NTSB "
 "determined the probable cause was an explosion of the center wing fuel tank, "
 "most likely from ignition of flammable fuel/air vapors, with the ignition "
 "source undetermined. The investigation ruled out a missile or bomb through "
 "extensive wreckage reconstruction. The central safety outcome was the FAA "
 "requirement for fuel-tank inerting on transport aircraft.",
 ("Probable cause: explosion of the center wing fuel tank from ignition of flammable vapors; ignition source not determined",
  "230 fatalities; wreckage recovered and reconstructed",
  "Aircraft: Boeing 747-131",
  "Investigation duration: four years; missile/bomb hypotheses excluded by evidence",
  "Safety outcomes: FAA fuel-tank inerting rule; wiring inspection programs for aging aircraft",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "wreckage reconstruction findings; exclusion analysis of alternative hypotheses; "
 "probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA fuel-tank system safety standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "reclog", None),

("swissair111-1998", "aviation-investigations",
 "Swissair Flight 111 — 1998",
 "On September 2, 1998, Swissair Flight 111, a McDonnell Douglas MD-11 flying from "
 "New York to Geneva, crashed into the Atlantic off Nova Scotia, killing all 229 "
 "people aboard. The crew had reported smoke in the cockpit and diverted toward "
 "Halifax; an in-flight fire above the cockpit ceiling progressed beyond control. "
 "The Transportation Safety Board of Canada found the fire most likely started "
 "from an electrical arcing event involving in-flight entertainment wiring and was "
 "propagated by flammable thermal/acoustic insulation material. The investigation "
 "led to worldwide changes in aircraft material flammability standards.",
 ("Probable cause: in-flight fire initiated by electrical arcing, propagated by flammable insulation (MPET-covered material)",
  "229 fatalities",
  "Aircraft: McDonnell Douglas MD-11",
  "Crew declared emergency and diverted; fire spread above the cockpit ceiling",
  "Safety outcomes: removal of MPET insulation from aircraft; improved flammability test standards; enhanced fire detection",
  "Investigating body: Transportation Safety Board of Canada (TSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "fire-origin analysis; material flammability findings; crew-action timeline; "
 "probable-cause determination; safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "FAA flammability test standards for cabin materials"),
 "Transportation Safety Board of Canada (TSB) — public aviation investigation report (public record).",
 "causetree", None),

("valujet592-1996", "aviation-investigations",
 "ValuJet Flight 592 — 1996",
 "On May 11, 1996, ValuJet Flight 592, a McDonnell Douglas DC-9 flying from Miami "
 "to Atlanta, crashed into the Florida Everglades, killing all 110 people aboard. "
 "Expired chemical oxygen generators had been improperly prepared, packaged, and "
 "loaded as cargo in the forward hold; they activated and started a fire that "
 "the crew could not control. The NTSB found the probable cause was a fire from "
 "the oxygen generators, with contributing failures by the contract maintenance "
 "facility, the airline's oversight, and the FAA's oversight of the carrier. The "
 "accident reshaped hazardous-materials rules and FAA surveillance of airlines.",
 ("Probable cause: in-flight fire from improperly prepared oxygen generators carried as cargo",
  "110 fatalities",
  "Aircraft: McDonnell Douglas DC-9-32",
  "Contributing: maintenance contractor errors; airline and FAA oversight failures",
  "Safety outcomes: smoke detection and fire suppression required in Class D cargo holds; hazmat handling rules tightened",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft and cargo documentation; "
 "maintenance-contractor chain; oversight analysis; probable-cause determination; "
 "safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA hazardous materials carriage rules"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "investigation", None),

("alaska261-2000", "aviation-investigations",
 "Alaska Airlines Flight 261 — 2000",
 "On January 31, 2000, Alaska Airlines Flight 261, a McDonnell Douglas MD-83 "
 "flying from Puerto Vallarta to San Francisco via Seattle, crashed into the "
 "Pacific Ocean off California, killing all 88 people aboard. The horizontal "
 "stabilizer jackscrew assembly failed from excessive wear caused by insufficient "
 "lubrication; when the crew attempted to troubleshoot the jammed stabilizer, the "
 "assembly failed completely and the aircraft became uncontrollable. The NTSB "
 "found the probable cause was the loss of pitch control from the jackscrew "
 "failure, stemming from extended lubrication intervals and the FAA-approved "
 "extension of maintenance check intervals.",
 ("Probable cause: loss of pitch control from failure of the horizontal stabilizer jackscrew — excessive wear from insufficient lubrication",
  "88 fatalities",
  "Aircraft: McDonnell Douglas MD-83",
  "Contributing: extended maintenance intervals; inadequate lubrication procedures and oversight",
  "Safety outcomes: FAA review of maintenance interval escalation; jackscrew inspection mandates",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft maintenance history; "
 "component failure analysis; maintenance-interval documentation; probable-cause determination; "
 "safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA airworthiness directive process"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "timeline", None),

("aa587-2001", "aviation-investigations",
 "American Airlines Flight 587 — 2001",
 "On November 12, 2001, American Airlines Flight 587, an Airbus A300 flying from "
 "New York to Santo Domingo, crashed in Queens, New York, shortly after takeoff, "
 "killing all 260 people aboard and 5 people on the ground. The aircraft's "
 "vertical stabilizer separated in flight following the first officer's "
 "alternating rudder inputs in response to wake turbulence. The NTSB found the "
 "probable cause was the in-flight separation of the vertical stabilizer as a "
 "result of loads beyond ultimate design created by the pilot's unnecessary and "
 "excessive rudder pedal inputs, with contributing factors including the "
 "aircraft's rudder system characteristics and elements of the airline's training "
 "program.",
 ("Probable cause: vertical stabilizer separation from excessive rudder inputs beyond design loads",
  "265 total fatalities (260 aboard, 5 on the ground)",
  "Aircraft: Airbus A300-605R",
  "Trigger: wake turbulence encounter after takeoff; pilot rudder inputs",
  "Safety outcomes: revised upset-recovery and rudder-use training; review of composite structure certification",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "structural failure analysis; flight-data recorder analysis; training-program review; "
 "probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA aircraft structural certification standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "causetree", None),

("colgan3407-2009", "aviation-investigations",
 "Colgan Air Flight 3407 — 2009",
 "On February 12, 2009, Colgan Air Flight 3407, a Bombardier Q400 operating as "
 "Continental Connection, crashed into a house near Buffalo, New York, on approach, "
 "killing all 49 people aboard and one person on the ground. The aircraft slowed "
 "to stall speed on approach; the captain's response to the stick shaker — "
 "pulling back instead of pushing forward — aggravated the stall. The NTSB cited "
 "the crew's failure to manage airspeed and recover from the stall, with "
 "contributing factors including crew fatigue, sterile-cockpit violations, and "
 "inadequate training. The accident directly drove the Airline Safety and FAA "
 "Extension Act of 2010.",
 ("Probable cause: captain's inappropriate response to the stall warning; failure to manage airspeed on approach",
  "50 fatalities (49 aboard, 1 on the ground)",
  "Aircraft: Bombardier DHC-8-400 (Q400)",
  "Contributing: crew fatigue; inadequate stall-recovery training; monitoring failures",
  "Safety outcomes: 1,500-hour ATP rule for first officers; new flight/duty-time rest rules; stall-training reform",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft and crew records; "
 "cockpit voice recorder analysis; fatigue analysis; training records review; "
 "probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA pilot qualification and rest requirements"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "verify", None),

("asiana214-2013", "aviation-investigations",
 "Asiana Airlines Flight 214 — 2013",
 "On July 6, 2013, Asiana Airlines Flight 214, a Boeing 777 flying from Seoul to "
 "San Francisco, struck the seawall short of the runway during a visual approach, "
 "killing 3 of the 307 people aboard and injuring many others. The aircraft came "
 "in low and slow; the crew did not recognize the decaying airspeed and the "
 "autothrottle's inactive state until too late. The NTSB found the probable cause "
 "was the flight crew's mismanagement of the approach and inadequate monitoring "
 "of airspeed, with contributing issues in automation mode awareness and crew "
 "resource management. The accident became a landmark case in automation "
 "dependency training.",
 ("Probable cause: crew mismanagement of a visual approach — failure to monitor and maintain airspeed",
  "3 fatalities of 307 occupants; aircraft destroyed by impact and fire",
  "Aircraft: Boeing 777-200ER",
  "Contributing: autothrottle mode confusion; inadequate go-around decision-making",
  "Safety outcomes: enhanced manual-flying and automation-management training; approach-stabilization emphasis",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft and crew records; "
 "approach-parameter analysis; automation-mode analysis; human-factors analysis; "
 "probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA stabilized-approach criteria"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "investigation", None),

("lion610-2018", "aviation-investigations",
 "Lion Air Flight 610 — 2018",
 "On October 29, 2018, Lion Air Flight 610, a Boeing 737 MAX 8 flying from Jakarta, "
 "crashed into the Java Sea minutes after takeoff, killing all 189 people aboard. "
 "Erroneous angle-of-attack data triggered the Maneuvering Characteristics "
 "Augmentation System (MCAS) to repeatedly command nose-down stabilizer trim; the "
 "crew could not counter the repeated commands. The Indonesian KNKT investigation "
 "cited MCAS design, the single-sensor dependency, inadequate crew procedures and "
 "training, and maintenance issues with the accident aircraft. The accident — "
 "followed by Ethiopian Airlines Flight 302 — led to the worldwide grounding of "
 "the 737 MAX.",
 ("Cause findings: MCAS activation on erroneous sensor data; design relied on a single angle-of-attack sensor",
  "189 fatalities",
  "Aircraft: Boeing 737 MAX 8",
  "Contributing: inadequate flight-crew procedures and training for MCAS; maintenance actions on the accident aircraft",
  "Safety outcomes: global 737 MAX grounding; MCAS redesign with dual-sensor input; certification-process reforms",
  "Investigating body: Indonesian National Transportation Safety Committee (KNKT)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "flight-data analysis of automated trim commands; system-design review; maintenance history; "
 "cause findings; safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "FAA/EASA system safety assessment standards"),
 "Indonesian National Transportation Safety Committee (KNKT) — public final report (public record).",
 "causetree", None),

("et302-2019", "aviation-investigations",
 "Ethiopian Airlines Flight 302 — 2019",
 "On March 10, 2019, Ethiopian Airlines Flight 302, a Boeing 737 MAX 8 flying "
 "from Addis Ababa to Nairobi, crashed minutes after takeoff, killing all 157 "
 "people aboard. As with Lion Air Flight 610, erroneous angle-of-attack data "
 "triggered repeated MCAS nose-down trim commands the crew could not overcome. "
 "The Ethiopian investigation's interim findings pointed to the aircraft's "
 "systems rather than crew action. Together with Flight 610, the accident "
 "prompted the worldwide grounding of the 737 MAX fleet and a fundamental "
 "reassessment of flight-control certification.",
 ("Cause findings: uncommanded MCAS stabilizer inputs following faulty angle-of-attack data",
  "157 fatalities",
  "Aircraft: Boeing 737 MAX 8",
  "Pattern: second MCAS-related loss of control within five months",
  "Safety outcomes: fleet grounding; MCAS redesign; enhanced certification scrutiny of flight-control software",
  "Investigating body: Ethiopian Aircraft Accident Investigation Bureau"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "flight-recorder analysis; comparison with prior similar occurrences; system-design review; "
 "cause findings; safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "FAA/EASA flight-control certification standards"),
 "Ethiopian Aircraft Accident Investigation Bureau — public interim report (public record).",
 "timeline", None),

("germanwings9525-2015", "aviation-investigations",
 "Germanwings Flight 9525 — 2015",
 "On March 24, 2015, Germanwings Flight 9525, an Airbus A320 flying from "
 "Barcelona to Düsseldorf, descended into the French Alps, killing all 150 people "
 "aboard. The French BEA investigation found that the co-pilot, alone on the "
 "flight deck, deliberately initiated the descent while the captain was locked "
 "out. Cockpit voice recorder evidence established the deliberate nature of the "
 "act; the investigation documented the co-pilot's concealed medical history. "
 "The occurrence prompted worldwide review of cockpit-access procedures and pilot "
 "medical fitness reporting.",
 ("Cause finding: deliberate descent initiated by the co-pilot; captain locked out of the flight deck",
  "150 fatalities",
  "Aircraft: Airbus A320-211",
  "Evidence: cockpit voice recorder; medical-history documentation",
  "Safety outcomes: review of two-person flight-deck policies; strengthened psychological fitness assessment and reporting",
  "Investigating body: French Bureau of Enquiry and Analysis for Civil Aviation Safety (BEA)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "recorder evidence analysis; medical-fitness documentation; procedural review; "
 "cause findings; safety recommendations; source citations. Tone remains factual and non-sensational.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "EASA pilot medical fitness standards"),
 "French Bureau of Enquiry and Analysis for Civil Aviation Safety (BEA) — public final report (public record).",
 "investigation", None),

("airasia8501-2014", "aviation-investigations",
 "Indonesia AirAsia Flight 8501 — 2014",
 "On December 28, 2014, Indonesia AirAsia Flight 8501, an Airbus A320 flying from "
 "Surabaya to Singapore, was lost in the Java Sea with all 162 people aboard. "
 "The Indonesian KNKT investigation found that a cracked solder joint in the "
 "rudder travel limiter system caused repeated faults; the crew's response — "
 "including resetting circuit breakers and subsequent handling — led to a stall "
 "from which recovery was not made. Contributing factors included maintenance "
 "practices and crew coordination. The investigation issued recommendations on "
 "maintenance, upset recovery training, and emergency locator transmitters.",
 ("Cause findings: rudder limiter system fault; crew actions leading to an unrecovered stall",
  "162 fatalities",
  "Aircraft: Airbus A320-216",
  "Contributing: recurring maintenance fault; crew coordination during the upset",
  "Safety outcomes: maintenance procedure review; upset-prevention training emphasis",
  "Investigating body: Indonesian National Transportation Safety Committee (KNKT)"),
 "A complete investigation record requires: occurrence date and location; aircraft maintenance history; "
 "system-fault analysis; crew-action analysis; cause findings; safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "Airbus system maintenance standards (as referenced by the investigation)"),
 "Indonesian National Transportation Safety Committee (KNKT) — public final report (public record).",
 "verify", None),

("tam3054-2007", "aviation-investigations",
 "TAM Airlines Flight 3054 — 2007",
 "On July 17, 2007, TAM Airlines Flight 3054, an Airbus A320 landing at São Paulo's "
 "Congonhas Airport in rain, overran the runway, crossed a road, and struck a "
 "cargo building, killing all 187 people aboard and 12 on the ground. The "
 "Brazilian CENIPA investigation found that one thrust reverser had been "
 "deactivated for maintenance and the crew did not correctly set the thrust "
 "levers for landing, leaving one engine producing forward thrust during the "
 "landing roll on a wet, grooved runway. The accident drove major runway-safety "
 "reforms in Brazil.",
 ("Cause findings: incorrect thrust-lever positioning with one reverser deactivated; loss of deceleration on a wet runway",
  "199 total fatalities (187 aboard, 12 on the ground)",
  "Aircraft: Airbus A320-233; runway: Congonhas, São Paulo",
  "Contributing: wet runway conditions; operational procedures for reverser-deferred dispatch",
  "Safety outcomes: Congonhas runway resurfacing and grooving; runway safety area improvements; operational procedure changes",
  "Investigating body: Brazilian Aeronautical Accident Investigation and Prevention Center (CENIPA)"),
 "A complete investigation record requires: occurrence date and location; aircraft configuration; "
 "runway-condition analysis; crew-procedure analysis; cause findings; safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "ICAO runway safety standards"),
 "Brazilian Aeronautical Accident Investigation and Prevention Center (CENIPA) — public final report (public record).",
 "timeline", None),

("spanair5022-2008", "aviation-investigations",
 "Spanair Flight 5022 — 2008",
 "On August 20, 2008, Spanair Flight 5022, a McDonnell Douglas MD-82 taking off "
 "from Madrid-Barajas Airport, crashed just beyond the runway, killing 154 of the "
 "172 people aboard. The crew attempted takeoff without deploying flaps and slats, "
 "and the takeoff warning system did not alert them. The Spanish CIAIAC "
 "investigation found the probable cause was the crew's omission in configuring "
 "the aircraft, with the inoperative warning system as a contributing factor, "
 "alongside maintenance and procedural issues. The accident reinforced checklist "
 "discipline and warning-system integrity worldwide.",
 ("Probable cause: takeoff attempted without flaps/slats; takeoff warning system failed to alert",
  "154 fatalities of 172 occupants",
  "Aircraft: McDonnell Douglas MD-82",
  "Contributing: maintenance actions on the warning system; checklist execution",
  "Safety outcomes: reinforced sterile-cockpit and checklist discipline; warning-system reliability review",
  "Investigating body: Spanish Civil Aviation Accident Investigation Commission (CIAIAC)"),
 "A complete investigation record requires: occurrence date and location; aircraft configuration evidence; "
 "warning-system analysis; checklist-procedure review; probable-cause determination; "
 "safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "Takeoff configuration warning system certification standards"),
 "Spanish Civil Aviation Accident Investigation Commission (CIAIAC) — public final report (public record).",
 "causetree", None),

("us1549-2009", "aviation-investigations",
 "US Airways Flight 1549 — 2009",
 "On January 15, 2009, US Airways Flight 1549, an Airbus A320 departing New York's "
 "LaGuardia Airport, struck a flock of Canada geese minutes after takeoff, "
 "losing thrust in both engines. Unable to reach an airport, the crew ditched "
 "the aircraft in the Hudson River; all 155 people aboard survived and were "
 "rescued. The NTSB investigation credited the crew's decision-making and "
 "crew-resource management, and examined engine bird-ingestion certification, "
 "ditching procedures, and wildlife management. The ditching is studied "
 "worldwide as a successful emergency outcome.",
 ("Outcome: successful ditching — all 155 occupants survived",
  "Cause: dual engine thrust loss from bird strikes shortly after takeoff",
  "Aircraft: Airbus A320-214; location: Hudson River, New York",
  "Crew actions: rejected airport-return options as unachievable; executed controlled ditching",
  "Safety outcomes: review of engine bird-ingestion standards; ditching-procedure guidance; airport wildlife-hazard management",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "bird-strike evidence; decision-analysis of landing options; crew-performance analysis; "
 "findings; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA engine bird-ingestion certification standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "investigation", None),

("ua232-1989", "aviation-investigations",
 "United Airlines Flight 232 — 1989",
 "On July 19, 1989, United Airlines Flight 232, a McDonnell Douglas DC-10 flying "
 "from Denver to Chicago, suffered an uncontained failure of the tail-mounted "
 "engine that severed all three hydraulic systems. With no flight controls, the "
 "crew — assisted by a deadheading training captain — controlled the aircraft "
 "using differential thrust from the two remaining engines and crash-landed at "
 "Sioux City, Iowa. Of the 296 people aboard, 112 were killed and 184 survived. "
 "The NTSB traced the engine failure to a fatigue crack in the fan disk that "
 "originated in a metallurgical defect. The accident is a landmark in crew "
 "resource management and engine-inspection practice.",
 ("Probable cause: uncontained engine failure from a fan-disk fatigue crack; total loss of hydraulics",
  "112 fatalities of 296 occupants; 184 survived",
  "Aircraft: McDonnell Douglas DC-10-10",
  "Crew used differential engine thrust for limited control — a CRM landmark",
  "Safety outcomes: enhanced engine-disk inspection; CRM training mandates; hydraulic-system redundancy review",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft and engine history; "
 "metallurgical failure analysis; crew-performance analysis; probable-cause determination; "
 "safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA engine-rotor integrity standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "stats", None),
("aloha243-1988", "aviation-investigations",
 "Aloha Airlines Flight 243 — 1988",
 "On April 28, 1988, Aloha Airlines Flight 243, a Boeing 737 flying between "
 "Hawaiian islands, suffered an explosive decompression when a section of the "
 "forward fuselage separated at 24,000 feet. One flight attendant was killed; the "
 "remaining 94 people aboard survived as the crew landed the damaged aircraft at "
 "Kahului, Maui. The NTSB found the probable cause was the failure of the "
 "airline's maintenance program to detect disbonding and fatigue damage in the "
 "fuselage lap joints — a watershed finding that created the FAA's Aging "
 "Aircraft program.",
 ("Probable cause: fuselage structural failure from undetected fatigue and disbonding in lap joints",
  "1 fatality of 95 occupants; crew landed the damaged aircraft",
  "Aircraft: Boeing 737-297",
  "Contributing: maintenance-program deficiencies in detecting structural fatigue",
  "Safety outcomes: FAA Aging Aircraft program; widespread structural inspection mandates; damage-tolerance research",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft maintenance and inspection history; "
 "structural failure analysis; maintenance-program review; probable-cause determination; "
 "safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA aging-aircraft structural inspection standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "investigation", None),

("eastern401-1972", "aviation-investigations",
 "Eastern Air Lines Flight 401 — 1972",
 "On December 29, 1972, Eastern Air Lines Flight 401, a Lockheed L-1011 "
 "approaching Miami, crashed into the Florida Everglades, killing 101 of the 176 "
 "people aboard. The crew became distracted troubleshooting a landing-gear "
 "indicator light and did not notice the autopilot had disengaged; the aircraft "
 "gradually descended into the terrain. The NTSB found the probable cause was the "
 "crew's failure to monitor the flight instruments during the distraction. The "
 "accident is regarded as a founding case of crew resource management: it showed "
 "that technically competent crews could still lose an airworthy aircraft to "
 "distraction.",
 ("Probable cause: crew distraction by a landing-gear indicator; failure to monitor instruments",
  "101 fatalities of 176 occupants",
  "Aircraft: Lockheed L-1011-385-1 TriStar",
  "Mechanism: unnoticed autopilot disengagement during troubleshooting",
  "Safety outcomes: crew resource management (CRM) development; altitude-alert systems; sterile-cockpit rule",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "cockpit voice recorder analysis; autopilot-system analysis; human-factors analysis; "
 "probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA crew resource management advisory standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "verify", None),

("delta191-1985", "aviation-investigations",
 "Delta Air Lines Flight 191 — 1985",
 "On August 2, 1985, Delta Air Lines Flight 191, a Lockheed L-1011 approaching "
 "Dallas/Fort Worth International Airport, encountered a microburst — a violent "
 "downdraft — on final approach and crashed short of the runway, killing 136 of "
 "the 163 people aboard and one person on the ground, for 137 total fatalities. "
 "The NTSB found the probable cause was the crew's decision to continue the "
 "approach into a thunderstorm and the lack of procedures, training, and "
 "technology for microburst avoidance and escape. The accident drove the "
 "deployment of Terminal Doppler Weather Radar and mandatory windshear training.",
 ("Probable cause: encounter with microburst-induced windshear; decision to continue approach into a thunderstorm",
  "137 total fatalities (136 aboard, 1 on the ground)",
  "Aircraft: Lockheed L-1011-385-1 TriStar",
  "Contributing: absence of windshear detection technology and escape procedures in 1985",
  "Safety outcomes: Terminal Doppler Weather Radar at major airports; windshear training and on-board detection requirements",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "meteorological reconstruction; flight-data analysis; training and procedures review; "
 "probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA windshear training and detection standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "timeline", None),

("usair427-1994", "aviation-investigations",
 "USAir Flight 427 — 1994",
 "On September 8, 1994, USAir Flight 427, a Boeing 737-300 approaching Pittsburgh, "
 "entered an uncontrolled descent and crashed, killing all 132 people aboard. The "
 "NTSB's four-and-a-half-year investigation determined the probable cause was a "
 "loss of control from the rudder surface deflecting opposite to the pilots' "
 "commands — caused by a jam of the main rudder power control unit's servo valve. "
 "The finding resolved two earlier unexplained 737 upsets (United Flight 585 and "
 "Eastwind Flight 517) and led to a redesign of the 737 rudder system and "
 "retrofit of the worldwide fleet.",
 ("Probable cause: rudder reversal from a jammed rudder power control unit servo valve",
  "132 fatalities",
  "Aircraft: Boeing 737-3B7",
  "Investigation linked the accident to two prior 737 rudder upsets",
  "Safety outcomes: redesigned rudder control system; fleet-wide retrofit; enhanced flight-data recorder requirements",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "component-level failure analysis; comparison with prior similar occurrences; "
 "probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA flight-control system certification standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "causetree", None),

("ae4184-1994", "aviation-investigations",
 "American Eagle Flight 4184 — 1994",
 "On October 31, 1994, American Eagle Flight 4184, an ATR 72 holding near "
 "Roselawn, Indiana, crashed after ice accumulated on the wings in freezing "
 "drizzle, killing all 68 people aboard. The NTSB found the probable cause was "
 "aileron hinge-moment reversal caused by ice ridges forming aft of the "
 "de-icing boots — a hazard the aircraft's certification had not addressed. "
 "Contributing factors included inadequate guidance on flight in freezing rain "
 "and drizzle. The accident transformed icing certification standards and "
 "operating guidance for turboprop aircraft.",
 ("Probable cause: loss of control from ice-induced aileron hinge-moment reversal in freezing drizzle",
  "68 fatalities",
  "Aircraft: ATR 72-212",
  "Contributing: inadequate certification standards for supercooled-droplet icing; crew guidance gaps",
  "Safety outcomes: revised icing certification envelopes; freezing-drizzle operating guidance; de-icing boot procedures",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "meteorological analysis; aerodynamic failure analysis; certification review; "
 "probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA aircraft icing certification standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "investigation", None),

("af358-2005", "aviation-investigations",
 "Air France Flight 358 — 2005",
 "On August 2, 2005, Air France Flight 358, an Airbus A340 landing at Toronto "
 "Pearson International Airport in a thunderstorm, overran the runway and came "
 "to rest in a ravine, where the aircraft caught fire. All 309 people aboard "
 "evacuated; there were no fatalities, though injuries occurred. The "
 "Transportation Safety Board of Canada found the crew continued an approach "
 "into deteriorating weather and touched down far along the wet runway, leaving "
 "insufficient distance to stop. The accident became a key case for runway "
 "safety areas and timely evacuation.",
 ("Outcome: runway overrun — all 309 occupants survived the evacuation",
  "Cause findings: long touchdown on a wet runway in a thunderstorm; continued approach into deteriorating weather",
  "Aircraft: Airbus A340-313X; runway: Toronto Pearson",
  "Evacuation completed before fire engulfed the aircraft",
  "Safety outcomes: ICAO runway end safety area guidance; thunderstorm-approach policy review",
  "Investigating body: Transportation Safety Board of Canada (TSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "landing-performance analysis; weather analysis; evacuation analysis; cause findings; "
 "safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "ICAO runway end safety area standards"),
 "Transportation Safety Board of Canada (TSB) — public aviation investigation report (public record).",
 "timeline", None),

("ba38-2008", "aviation-investigations",
 "British Airways Flight 38 — 2008",
 "On January 17, 2008, British Airways Flight 38, a Boeing 777 flying from "
 "Beijing to London, lost thrust in both engines on final approach to Heathrow "
 "and landed short of the runway. All 152 people aboard survived; the aircraft "
 "was substantially damaged. The UK Air Accidents Investigation Branch found "
 "that ice had accreted in the fuel system during the long cold-soak cruise and "
 "was released during approach, restricting fuel flow to both engines. The "
 "investigation prompted worldwide fuel-system icing research and procedural "
 "changes for long cold-soak operations.",
 ("Cause finding: fuel-flow restriction from ice accreted in the fuel system during cruise",
  "0 fatalities of 152 occupants",
  "Aircraft: Boeing 777-236ER",
  "Mechanism: ice release on approach blocked fuel-oil heat exchangers",
  "Safety outcomes: fuel-system icing research programs; revised cold-soak operating procedures",
  "Investigating body: UK Air Accidents Investigation Branch (AAIB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "fuel-system analysis; flight-profile thermal analysis; cause findings; safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "EASA fuel-system icing certification guidance"),
 "UK Air Accidents Investigation Branch (AAIB) — public final report (public record).",
 "stats", None),

("qf32-2010", "aviation-investigations",
 "Qantas Flight 32 — 2010",
 "On November 4, 2010, Qantas Flight 32, an Airbus A380 departing Singapore, "
 "suffered an uncontained failure of the number-two engine that damaged the wing, "
 "fuel, hydraulic, and control systems. The crew managed cascading system "
 "failures for nearly two hours and landed safely with all 469 people aboard. "
 "The Australian Transport Safety Bureau traced the failure to a misaligned "
 "oil-feed pipe that caused an oil fire and turbine-disc failure. The "
 "investigation is widely studied for exemplary crew resource management under "
 "extreme workload.",
 ("Cause finding: uncontained engine failure from a mis-manufactured oil-feed pipe",
  "0 fatalities of 469 occupants; safe landing after cascading failures",
  "Aircraft: Airbus A380-842",
  "Crew managed dozens of system warnings over nearly two hours",
  "Safety outcomes: Rolls-Royce Trent 900 inspection program; CRM case study adopted worldwide",
  "Investigating body: Australian Transport Safety Bureau (ATSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft and engine identification; "
 "component failure analysis; crew-workload analysis; cause findings; safety recommendations; source citations.",
 ("ICAO Annex 13 — Aircraft Accident and Incident Investigation",
  "Engine-rotor manufacturing quality standards"),
 "Australian Transport Safety Bureau (ATSB) — public investigation report (public record).",
 "reclog", None),

("psa182-1978", "aviation-investigations",
 "PSA Flight 182 — 1978",
 "On September 25, 1978, PSA Flight 182, a Boeing 727 approaching San Diego, "
 "collided in mid-air with a Cessna 172 and crashed into a residential "
 "neighborhood, killing all 135 people aboard the airliner, the 2 people in the "
 "Cessna, and 7 people on the ground — 144 total fatalities. The NTSB found the "
 "probable cause was the 727 crew's failure to maintain separation from the "
 "Cessna after reporting it in sight, with air traffic control procedures as a "
 "contributing factor. The disaster accelerated the development of the Traffic "
 "Alert and Collision Avoidance System (TCAS) and stricter terminal airspace "
 "rules.",
 ("Probable cause: failure to maintain visual separation from the Cessna; ATC procedural factors",
  "144 total fatalities (135 aboard the 727, 2 in the Cessna, 7 on the ground)",
  "Aircraft: Boeing 727-214 and Cessna 172",
  "Location: San Diego, California — see-and-avoid limitations demonstrated",
  "Safety outcomes: TCAS development and mandate; Class B airspace redesign; transponder requirements",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; both aircraft identifications; "
 "ATC transcript analysis; see-and-avoid analysis; probable-cause determination; "
 "safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA terminal airspace and TCAS standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "causetree", None),

("ac797-1983", "aviation-investigations",
 "Air Canada Flight 797 — 1983",
 "On June 2, 1983, Air Canada Flight 797, a McDonnell Douglas DC-9 flying from "
 "Dallas to Toronto via Montreal, developed an in-flight fire that began in or "
 "around the aft lavatory. The crew diverted to Cincinnati; during evacuation "
 "after landing, a flash fire swept the cabin and 23 of the 46 people aboard "
 "were killed. The NTSB could not determine the fire's ignition source but found "
 "the probable cause of the fatalities was the in-flight fire and the crew's "
 "delayed recognition of its severity. The accident produced sweeping cabin-fire "
 "safety reforms.",
 ("Probable cause of fatalities: in-flight cabin fire; ignition source undetermined",
  "23 fatalities of 46 occupants",
  "Aircraft: McDonnell Douglas DC-9-32",
  "Contributing: delayed fire recognition; lavatory smoke detection absent",
  "Safety outcomes: lavatory smoke detectors mandated; fire-blocking seat materials; floor-level emergency lighting",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft identification; "
 "fire-origin analysis; crew-timeline analysis; evacuation analysis; probable-cause determination; "
 "safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA cabin fire-protection standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "investigation", None),

("sou242-1977", "aviation-investigations",
 "Southern Airways Flight 242 — 1977",
 "On April 4, 1977, Southern Airways Flight 242, a McDonnell Douglas DC-9 flying "
 "from Huntsville to Atlanta, flew into a severe thunderstorm with hail that "
 "flamed out both engines. With no thrust and no reachable airport, the crew "
 "attempted an emergency landing on a highway near New Hope, Georgia; the "
 "aircraft struck obstructions and broke apart. Of the 85 people aboard, 63 "
 "were killed, along with 9 people on the ground — 72 total fatalities. The NTSB "
 "found the probable cause was the engines' ingestion of massive water and hail, "
 "with the crew's continued flight into severe weather and inadequate weather "
 "information as factors. The accident improved airborne weather-radar "
 "procedures and engine rain-ingestion standards.",
 ("Probable cause: dual engine flameout from hail and water ingestion in a severe thunderstorm",
  "72 total fatalities (63 aboard, 9 on the ground)",
  "Aircraft: McDonnell Douglas DC-9-31",
  "Crew attempted a highway landing after total thrust loss",
  "Safety outcomes: engine water-ingestion certification standards; weather-avoidance procedures; ATC weather-information improvements",
  "Investigating body: U.S. National Transportation Safety Board (NTSB)"),
 "A complete investigation record requires: occurrence date and location; aircraft and engine identification; "
 "meteorological analysis; engine-ingestion analysis; crew decision analysis; "
 "probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "FAA engine precipitation-ingestion standards"),
 "U.S. National Transportation Safety Board (NTSB) — public aircraft accident report (public record).",
 "timeline", None),

# ========================= MOTOR VEHICLE (20) =========================
("ford-pinto-cases", "motor-vehicle-crash-data",
 "Ford Pinto Fuel-System Safety Cases — 1970s",
 "In the 1970s, the Ford Pinto's fuel-tank placement behind the rear axle made "
 "it vulnerable to rupture and fire in rear-impact collisions. NHTSA "
 "investigations and public crash testing documented the hazard; Ford recalled "
 "1.5 million Pintos and Bobcats in 1978 to install fuel-tank shields. The cases "
 "became the landmark study of cost-benefit analysis in safety regulation after "
 "an internal Ford memo weighing recall costs against projected casualty costs "
 "became public. The regulatory outcome was the upgrade of Federal Motor Vehicle "
 "Safety Standard 301 on fuel-system integrity.",
 ("Hazard: rear-impact fuel-tank rupture and fire",
  "Regulatory action: 1978 recall of 1.5 million vehicles; FMVSS 301 upgraded",
  "Evidence: NHTSA investigations; crash-test documentation; civil litigation record",
  "Safety outcomes: fuel-system integrity standards; cost-benefit transparency in rulemaking",
  "Landmark: Grimshaw v. Ford — punitive damages in the civil record",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: vehicle identification; crash-test and field data; regulatory correspondence; "
 "recall documentation; standard changes; civil-litigation outcomes; source citations.",
 ("FMVSS 301 — Fuel System Integrity",
  "NHTSA defect investigation procedures"),
 "National Highway Traffic Safety Administration (NHTSA) — public investigation and recall records (public record).",
 "investigation", None),

("takata-airbag-recalls", "motor-vehicle-crash-data",
 "Takata Airbag Inflator Recalls — 2008–present",
 "Beginning in 2008, defective Takata airbag inflators — which could rupture on "
 "deployment and spray metal fragments — triggered the largest automotive recall "
 "in U.S. history, covering tens of millions of vehicles across many "
 "manufacturers. The inflators were linked to dozens of deaths and hundreds of "
 "injuries worldwide. NHTSA coordinated the recalls, issued consent orders, and "
 "levied record civil penalties; Takata entered bankruptcy in 2017. The "
 "long-running recall campaign became the model for phased, risk-prioritized "
 "recall management of a systemic supplier defect.",
 ("Defect: ammonium-nitrate inflators prone to rupture; metal-fragment injuries",
  "Scale: largest U.S. auto recall — tens of millions of vehicles",
  "Linked in public reports to dozens of deaths and hundreds of injuries worldwide",
  "Regulatory action: NHTSA coordinated recalls; consent orders; record civil penalties",
  "Safety outcomes: phased risk-prioritized recall model; propellant-chemistry scrutiny",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: defect description; affected vehicle population; injury data; "
 "recall phasing documentation; regulatory orders; manufacturer responses; source citations.",
 ("FMVSS 208 — Occupant Crash Protection",
  "NHTSA recall and consent-order procedures"),
 "National Highway Traffic Safety Administration (NHTSA) — public recall and enforcement records (public record).",
 "reclog", None),

("gm-ignition-switch", "motor-vehicle-crash-data",
 "General Motors Ignition-Switch Cases — 2014",
 "General Motors' delayed recall of vehicles with ignition switches that could "
 "slip from 'run' to 'accessory' — disabling power steering, power brakes, and "
 "airbags — became one of the largest U.S. auto-safety scandals. An independent "
 "compensation administrator approved 124 death claims linked to the defect. GM "
 "entered a deferred-prosecution agreement with the U.S. Department of Justice, "
 "recalling millions of vehicles. The cases prompted reforms in automaker "
 "early-warning reporting and internal safety culture.",
 ("Defect: ignition switch slipping to accessory — airbags and power assists disabled",
  "Independent compensation program approved 124 death claims",
  "Regulatory action: DOJ deferred-prosecution agreement; congressional hearings",
  "Safety outcomes: strengthened TREAD Act early-warning reporting; safety-culture reforms",
  "Documenting body: NHTSA; U.S. Department of Justice; independent compensation administrator"),
 "A complete record requires: defect description; timeline of internal knowledge; recall documentation; "
 "compensation-program statistics; enforcement outcomes; reforms adopted; source citations.",
 ("TREAD Act — early-warning reporting requirements",
  "NHTSA defect investigation procedures"),
 "National Highway Traffic Safety Administration (NHTSA) and U.S. Department of Justice — public records (public record).",
 "verify", None),

("toyota-unintended-acceleration", "motor-vehicle-crash-data",
 "Toyota Unintended-Acceleration Investigations — 2009–2011",
 "A wave of complaints about sudden unintended acceleration in Toyota vehicles "
 "prompted congressional hearings, NHTSA investigations, and an independent "
 "study by NASA engineers. The investigations found no electronic-throttle "
 "defect; identified causes were sticky accelerator pedals, floor-mat "
 "entrapment, and driver pedal misapplication. Toyota recalled millions of "
 "vehicles and paid a $1.2 billion Department of Justice settlement in 2014. "
 "The episode established brake-throttle override systems and event data "
 "recorders as industry safety baselines.",
 ("Findings: pedal entrapment and sticky pedals; NASA/NHTSA found no electronic-throttle defect",
  "Regulatory action: recalls; $1.2 billion DOJ settlement (2014)",
  "Safety outcomes: brake-throttle override systems; event data recorder requirements",
  "Documenting bodies: NHTSA; NASA Engineering and Safety Center; U.S. Department of Justice"),
 "A complete record requires: complaint data; engineering analysis; independent study findings; "
 "recall documentation; settlement terms; adopted countermeasures; source citations.",
 ("FMVSS 124 — Accelerator Control Systems",
  "NHTSA event data recorder requirements"),
 "NHTSA and NASA Engineering and Safety Center — public investigation reports (public record).",
 "investigation", None),

("tesla-autopilot-williston-2016", "motor-vehicle-crash-data",
 "Tesla Autopilot Fatal Crash, Williston, Florida — 2016",
 "On May 7, 2016, a Tesla Model S operating with Autopilot engaged collided "
 "with a tractor-trailer crossing the highway near Williston, Florida, killing "
 "the Tesla driver. Both NHTSA and the NTSB investigated — the first fatal crash "
 "involving a partially automated driving system to receive full federal "
 "investigation. The NTSB found the probable cause was the driver's inattention "
 "and overreliance on automation, combined with the system's operational design "
 "allowing engagement outside its intended conditions. The case set the template "
 "for automated-driving crash investigation.",
 ("Probable cause: driver inattention and overreliance on automation; system allowed use outside its operational design domain",
  "1 fatality; first fully investigated fatal crash of a partially automated vehicle",
  "Investigating bodies: NTSB and NHTSA",
  "Safety outcomes: driver-monitoring expectations; operational-design-domain enforcement; automated-vehicle investigation protocols",
  "Landmark: template for investigating automation-related crashes"),
 "A complete record requires: occurrence date and location; vehicle and system state data; "
 "driver-attention evidence; system-design analysis; probable-cause determination; "
 "safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "NHTSA automated driving system guidance"),
 "U.S. National Transportation Safety Board (NTSB) — public highway accident report (public record).",
 "causetree", None),

("uber-atg-tempe-2018", "motor-vehicle-crash-data",
 "Uber ATG Test Vehicle Crash, Tempe, Arizona — 2018",
 "On March 18, 2018, an Uber Advanced Technologies Group self-driving test "
 "vehicle struck and killed a pedestrian crossing a road in Tempe, Arizona — the "
 "first pedestrian fatality involving an autonomous test vehicle. The NTSB "
 "investigation found the vehicle's system detected the pedestrian but did not "
 "correctly classify or brake in time; the safety operator was distracted. The "
 "probable cause cited the inadequate safety culture at Uber ATG, the "
 "operator's inattention, and the victim crossing outside a crosswalk. Arizona "
 "suspended Uber's testing; the case reshaped autonomous-vehicle testing "
 "practices nationwide.",
 ("Probable cause: inadequate safety culture; operator inattention; system classification failure",
  "1 pedestrian fatality — first involving an autonomous test vehicle",
  "Investigating body: NTSB",
  "Safety outcomes: safety-driver attention requirements; testing-transparency expectations; state testing-permit reforms",
  "Regulatory response: Arizona testing suspension; industry safety-practice reviews"),
 "A complete record requires: occurrence date and location; system perception logs; operator-attention evidence; "
 "safety-culture assessment; probable-cause determination; safety recommendations; source citations.",
 ("NTSB investigation procedures (49 CFR Part 831)",
  "NHTSA automated driving system testing guidance"),
 "U.S. National Transportation Safety Board (NTSB) — public highway accident report (public record).",
 "verify", None),

("firestone-ford-explorer-2000", "motor-vehicle-crash-data",
 "Firestone Tire / Ford Explorer Cases — 2000",
 "In 2000, tread separations on Firestone tires fitted to Ford Explorers — "
 "linked in public reports to hundreds of deaths — triggered massive recalls, "
 "congressional hearings, and the Transportation Recall Enhancement, "
 "Accountability and Documentation (TREAD) Act. Investigations found tire "
 "manufacturing issues compounded by recommended inflation pressures and vehicle "
 "handling after blowouts. The TREAD Act created early-warning reporting, "
 "requiring manufacturers to report warranty claims, injuries, and deaths to "
 "NHTSA quarterly — the backbone of modern U.S. auto-defect surveillance.",
 ("Defect: tire tread separation; rollover risk after blowout",
  "Regulatory outcome: the TREAD Act (2000) — early-warning reporting mandates",
  "Safety outcomes: tire pressure monitoring systems (TPMS) required; tire-aging guidance",
  "Documenting body: NHTSA; U.S. Congress"),
 "A complete record requires: defect description; injury and fatality data; recall documentation; "
 "legislative history; adopted standards; surveillance-system description; source citations.",
 ("TREAD Act — early-warning reporting",
  "FMVSS 138 — Tire Pressure Monitoring Systems"),
 "NHTSA — public investigation and recall records; U.S. Congress legislative record (public record).",
 "stats", None),

("fars-roadway-trends", "motor-vehicle-crash-data",
 "U.S. Roadway Fatality Trends — FARS Public Data",
 "The Fatality Analysis Reporting System (FARS), maintained by NHTSA since 1975, "
 "is the census of fatal motor-vehicle crashes on U.S. public roads. Annual FARS "
 "data show roughly 36,000–43,000 roadway deaths per year in recent decades, "
 "with notable declines from safety advances and spikes linked to behavioral "
 "factors. FARS underpins virtually all U.S. road-safety policy: speed "
 "management, impaired-driving enforcement, occupant-protection laws, and vehicle "
 "standards are all evaluated against this public dataset.",
 ("Dataset: census of fatal U.S. roadway crashes since 1975",
  "Recent annual toll: roughly 36,000–43,000 deaths per year",
  "Uses: policy evaluation; countermeasure research; state safety planning",
  "Public access: annual reports and query systems published by NHTSA",
  "Safety outcomes: data-driven speed, impairment, and protection countermeasures",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: dataset description and coverage; annual trend figures; "
 "methodology notes; policy uses; access information; source citations.",
 ("FARS coding and analysis manual",
  "Model Minimum Uniform Crash Criteria (MMUCC)"),
 "NHTSA Fatality Analysis Reporting System — public annual reports and data (public record).",
 "stats", None),

("seatbelt-effectiveness", "motor-vehicle-crash-data",
 "Seat-Belt Effectiveness — NHTSA Public Findings",
 "NHTSA research consistently finds that lap-and-shoulder seat belts reduce the "
 "risk of fatal injury to front-seat passenger-vehicle occupants by about 45 "
 "percent and the risk of moderate-to-critical injury by about 50 percent. "
 "Observational surveys track national belt use, which rose from under 15 "
 "percent in the early 1980s to about 90 percent today following primary "
 "enforcement laws and 'Click It or Ticket' campaigns. Seat belts remain the "
 "single most effective occupant-protection countermeasure in the public record.",
 ("Effectiveness: about 45% reduction in fatal-injury risk for front-seat occupants",
  "National use rose from under 15% (early 1980s) to about 90% today",
  "Evidence: NHTSA observational surveys; crash-data effectiveness studies",
  "Safety outcomes: primary-enforcement belt laws; high-visibility enforcement campaigns",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: effectiveness estimates with methodology; use-rate trends; "
 "law and enforcement history; lives-saved estimation methods; source citations.",
 ("FMVSS 208 — Occupant Crash Protection",
  "FMVSS 209/210 — Seat Belt Assemblies and Anchorages"),
 "NHTSA — public effectiveness studies and observational surveys (public record).",
 "stats", None),

("alcohol-impaired-trends", "motor-vehicle-crash-data",
 "Alcohol-Impaired Driving Trends — Public Data",
 "Alcohol-impaired driving remains one of the largest contributors to U.S. "
 "roadway deaths, accounting for roughly three in ten crash fatalities in "
 "public FARS data across recent decades. The adoption of 0.08 blood-alcohol "
 "concentration as the national per se standard, minimum-21 drinking-age laws, "
 "sobriety checkpoints, and ignition-interlock programs are all documented in "
 "the public record as countermeasures. NHTSA publishes annual impaired-driving "
 "statistics tracking long-term declines and recent plateaus.",
 ("Share: roughly 3 in 10 U.S. crash fatalities involve an alcohol-impaired driver",
  "Countermeasures: 0.08 BAC standard; minimum-21 laws; checkpoints; ignition interlocks",
  "Evidence: FARS annual data; NHTSA impaired-driving reports",
  "Safety outcomes: documented long-term decline from 1980s peaks",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: fatality-share trends; countermeasure history; "
 "enforcement data; evaluation studies; source citations.",
 ("Model Minimum Uniform Crash Criteria (MMUCC)",
  "NHTSA impaired-driving program guidance"),
 "NHTSA — public FARS data and impaired-driving reports (public record).",
 "stats", None),

("distracted-driving-research", "motor-vehicle-crash-data",
 "Distracted-Driving Research — Public Findings",
 "NHTSA's naturalistic driving studies — instrumenting volunteer drivers' "
 "vehicles with cameras and sensors — documented that visual-manual tasks like "
 "texting substantially increase crash risk, with eyes-off-road time the key "
 "mechanism. Public reports estimate thousands of deaths per year involve "
 "distracted drivers. The research base supported state texting-while-driving "
 "bans, NHTSA distraction guidelines for in-vehicle devices, and ongoing study "
 "of hands-free versus handheld cognitive distraction.",
 ("Mechanism: eyes-off-road time during visual-manual tasks drives crash risk",
  "Scale: thousands of U.S. deaths per year involve distraction (public estimates)",
  "Evidence: naturalistic driving studies; FARS distraction coding",
  "Safety outcomes: state texting bans; NHTSA in-vehicle device guidelines",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: study designs and risk estimates; annual fatality estimates; "
 "law and guideline history; ongoing research questions; source citations.",
 ("NHTSA visual-manual distraction guidelines",
  "Model Minimum Uniform Crash Criteria (MMUCC)"),
 "NHTSA — public naturalistic driving studies and reports (public record).",
 "investigation", None),

("motorcycle-helmet-effectiveness", "motor-vehicle-crash-data",
 "Motorcycle Helmet Effectiveness — Public Data",
 "NHTSA public research finds that helmets reduce the risk of head injury and "
 "are about 37 percent effective in preventing fatal injuries to motorcycle "
 "riders. States with universal helmet laws show markedly higher helmet use and "
 "lower fatality rates in public data comparisons. The helmet record is one of "
 "the most studied occupant-protection topics in the crash literature, with "
 "decades of consistent findings supporting helmet use as a proven "
 "countermeasure.",
 ("Effectiveness: helmets about 37% effective in preventing rider fatalities",
  "Universal-law states show higher use and lower fatality rates",
  "Evidence: NHTSA crash-data studies; state law comparisons",
  "Safety outcomes: state universal helmet laws; helmet standards (DOT FMVSS 218)",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: effectiveness estimates; state law comparisons; use-rate data; "
 "standard specifications; source citations.",
 ("FMVSS 218 — Motorcycle Helmets",
  "NHTSA motorcycle safety program data"),
 "NHTSA — public motorcycle safety studies (public record).",
 "stats", None),

("child-passenger-safety", "motor-vehicle-crash-data",
 "Child Passenger Safety — Public Record",
 "Motor-vehicle crashes are a leading cause of death for U.S. children, and the "
 "public record documents dramatic risk reductions from proper restraints: "
 "child safety seats reduce fatal injury risk for infants and toddlers by the "
 "majority compared with seat belts alone, and booster seats similarly protect "
 "older children. NHTSA's record covers the LATCH anchor standard, rear-facing "
 "guidance, and state child-restraint laws. Observational surveys track misuse "
 "rates — a persistent finding is that most seats have at least one installation "
 "error, driving inspection-station programs.",
 ("Protection: child seats reduce fatal-injury risk by the majority for infants and toddlers",
  "Standards: LATCH anchors; state restraint laws; rear-facing guidance",
  "Persistent finding: most installed seats have at least one misuse error",
  "Safety outcomes: inspection-station programs; ease-of-use ratings",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: effectiveness estimates by restraint type; misuse survey data; "
 "standard and law history; program descriptions; source citations.",
 ("FMVSS 213 — Child Restraint Systems",
  "FMVSS 225 — Child Restraint Anchorage Systems (LATCH)"),
 "NHTSA — public child passenger safety research (public record).",
 "verify", None),

("airbag-effectiveness-record", "motor-vehicle-crash-data",
 "Frontal Airbag Effectiveness and Risks — Public Record",
 "Frontal airbags, required in U.S. passenger vehicles, are documented in "
 "NHTSA public research as reducing driver fatal-injury risk by about 29 "
 "percent in frontal crashes when combined with seat belts. The early "
 "high-powered airbags also caused injuries to children and small adults, "
 "leading to 'depowered' airbags and then advanced airbags that adjust "
 "deployment to occupant size and crash severity. The airbag record illustrates "
 "how a countermeasure's risks are measured and engineered down in public.",
 ("Effectiveness: about 29% driver fatality-risk reduction in frontal crashes (with belts)",
  "Risk history: early high-powered deployments injured children and small adults",
  "Engineering response: depowered airbags; advanced occupant-sensing airbags",
  "Safety outcomes: FMVSS 208 advanced-airbag requirements; back-seat guidance for children",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: effectiveness estimates; injury-risk findings; design evolution; "
 "regulatory milestones; source citations.",
 ("FMVSS 208 — Occupant Crash Protection (advanced airbags)",
  "NHTSA special crash investigations (SCI)"),
 "NHTSA — public airbag research and rulemaking records (public record).",
 "investigation", None),

("esc-effectiveness", "motor-vehicle-crash-data",
 "Electronic Stability Control Effectiveness — Public Record",
 "NHTSA research found electronic stability control (ESC) reduces fatal "
 "single-vehicle crashes by about half and fatal single-vehicle rollovers by "
 "even more, making it one of the most effective crash-avoidance technologies "
 "in the public record. Based on this evidence, NHTSA required ESC on all new "
 "U.S. passenger vehicles under FMVSS 126, phased in from 2008 to 2012. "
 "International regulators followed with equivalent mandates, and ESC became a "
 "foundation technology for later driver-assistance systems.",
 ("Effectiveness: about 50% reduction in fatal single-vehicle crashes",
  "Mandate: FMVSS 126 — ESC required on new U.S. passenger vehicles",
  "Evidence: NHTSA crash-data effectiveness studies",
  "Safety outcomes: global ESC mandates; foundation for later assistance systems",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: effectiveness estimates; rulemaking history; phase-in schedule; "
 "international adoption; source citations.",
 ("FMVSS 126 — Electronic Stability Control Systems",
  "UN Regulation No. 140 (international equivalent)"),
 "NHTSA — public ESC research and FMVSS 126 rulemaking (public record).",
 "stats", None),

("rear-visibility-rule", "motor-vehicle-crash-data",
 "Rear Visibility Rule, FMVSS 111 — 2014",
 "After years of advocacy following backover tragedies involving children, "
 "NHTSA issued the rear-visibility rule in 2014 requiring rearview cameras on "
 "new vehicles — phased in fully by 2018. Public rulemaking data documented "
 "hundreds of backover deaths and thousands of injuries per year, many involving "
 "small children, with large blind zones behind high-profile vehicles. The rule "
 "is a landmark case of a visibility countermeasure moving from advocacy to "
 "federal mandate on the strength of public crash data.",
 ("Rule: rearview cameras required on new vehicles (FMVSS 111, 2014)",
  "Problem documented: hundreds of backover deaths per year; large rear blind zones",
  "Phase-in: full compliance by May 2018",
  "Safety outcomes: standard backup cameras; ongoing study of sensor-based aids",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: problem-size data; rulemaking history; phase-in schedule; "
 "effectiveness monitoring; source citations.",
 ("FMVSS 111 — Rear Visibility",
  "NHTSA backover crash data reports"),
 "NHTSA — public FMVSS 111 rulemaking record (public record).",
 "reclog", None),

("school-bus-safety", "motor-vehicle-crash-data",
 "School Bus Occupant Safety — Public Record",
 "Large school buses are among the safest vehicles on U.S. roads: NHTSA public "
 "data show school-bus-related fatalities are a small fraction of roadway "
 "deaths, with most victims being pedestrians or occupants of other vehicles. "
 "The safety strategy is 'compartmentalization' — closely spaced, high-backed, "
 "energy-absorbing seats — codified in FMVSS 222, rather than seat belts on "
 "large buses (a long-debated topic in the public record). NHTSA continues to "
 "study belt-equipped buses while the data support compartmentalization's "
 "strong record.",
 ("Record: school buses among the safest U.S. road vehicles by fatality rate",
  "Strategy: compartmentalization (FMVSS 222) — high-backed energy-absorbing seats",
  "Most school-bus-related victims are pedestrians or other-vehicle occupants",
  "Ongoing: NHTSA study of seat belts on large buses",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: fatality statistics; compartmentalization description; "
 "belt debate summary; standard history; source citations.",
 ("FMVSS 222 — School Bus Passenger Seating and Crash Protection",
  "NHTSA school bus safety research"),
 "NHTSA — public school bus safety data (public record).",
 "verify", None),

("ltccs-truck-study", "motor-vehicle-crash-data",
 "Large Truck Crash Causation Study — FMCSA",
 "The Large Truck Crash Causation Study, conducted jointly by FMCSA and NHTSA, "
 "examined a national sample of serious truck crashes to assign critical "
 "reasons — the last failure in the causal chain. Public findings showed driver "
 "factors dominating: decision errors, recognition failures, and non-performance "
 "(such as fatigue) far outweighed vehicle or environmental critical reasons. "
 "The study underpins hours-of-service rules, speed management, and "
 "driver-assistance priorities for heavy trucks.",
 ("Method: national sample of serious truck crashes; critical-reason assignment",
  "Finding: driver decision, recognition, and non-performance errors dominate critical reasons",
  "Uses: hours-of-service rules; truck safety technology priorities",
  "Documenting bodies: FMCSA and NHTSA"),
 "A complete record requires: study design; critical-reason distributions; "
 "policy applications; limitations; source citations.",
 ("FMCSA hours-of-service regulations",
  "LTCCS public report methodology"),
 "FMCSA/NHTSA — public Large Truck Crash Causation Study report (public record).",
 "investigation", None),

("pedestrian-safety-data", "motor-vehicle-crash-data",
 "Pedestrian Crash Data — Public Record",
 "NHTSA public data document thousands of U.S. pedestrian deaths per year — "
 "roughly one in six roadway fatalities — with a rising trend over the past "
 "decade concentrated in urban areas, at night, and away from intersections. "
 "The data record covers vehicle front-end design, speed effects on survivability, "
 "and the evaluation of automatic emergency braking with pedestrian detection. "
 "Pedestrian safety is a major input to New Car Assessment Program updates and "
 "urban speed-management policy.",
 ("Scale: thousands of U.S. pedestrian deaths per year; rising trend",
  "Risk factors: darkness; urban arterials; higher vehicle speeds and front-end profiles",
  "Countermeasures: pedestrian-detecting automatic emergency braking; speed management",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: fatality trends; risk-factor analysis; countermeasure evaluations; "
 "program updates; source citations.",
 ("FMVSS pedestrian-protection research program",
  "NHTSA pedestrian crash data reports"),
 "NHTSA — public pedestrian safety data (public record).",
 "stats", None),

("ncap-program", "motor-vehicle-crash-data",
 "New Car Assessment Program — Public Ratings",
 "NHTSA's New Car Assessment Program, launched in 1978, crash-tests new "
 "vehicles and publishes 5-star safety ratings that consumers use when buying "
 "cars. The public program — later joined by the Insurance Institute for "
 "Highway Safety's ratings — is credited with accelerating the adoption of "
 "airbags, stronger structures, and electronic stability control, as "
 "manufacturers design for the tests. NCAP's evolution from belted-dummy "
 "frontal tests to rollover, side-impact, and driver-assistance assessments "
 "mirrors the history of vehicle safety itself.",
 ("Program: 5-star crash-test ratings published for consumers since 1978",
  "Effect: manufacturers design to the tests — accelerated airbags, structures, ESC",
  "Evolution: frontal to rollover, side, and driver-assistance assessments",
  "Companion: Insurance Institute for Highway Safety ratings (independent, public)",
  "Documenting body: National Highway Traffic Safety Administration (NHTSA)"),
 "A complete record requires: program history; test protocols; rating methodology; "
 "documented safety effects; source citations.",
 ("NCAP test protocols (public)",
  "FMVSS compliance testing procedures"),
 "NHTSA — public New Car Assessment Program records (public record).",
 "timeline", None),
]
