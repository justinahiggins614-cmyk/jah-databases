#!/usr/bin/env python3
"""Building blueprint archetypes: schools, factories."""

SCHOOLS = [
 dict(name="One-Room Schoolhouse", group="Classroom Buildings", style="One-Room School",
  history=("The one-room schoolhouse educated rural America from the 1700s to the mid-1900s: one "
   "teacher, eight grades, one stove. Thousands were built from pattern books; survivors are "
   "museums now, but the form - gabled box, belfry, banks of windows on one side - is pure "
   "functional beauty."),
  layout=("Single classroom with the teacher's desk at the front, recitation bench, and rows of "
   "desks facing the blackboard wall; entry vestibule with cloakrooms; privies or restrooms "
   "outside or in a rear addition. Windows line the left wall (right-handed light)."),
  structure=("Wood frame, gable roof, often with a small belfry; raised on piers or a stone "
   "foundation. The blackboard wall is load-bearing and windowless; the window wall carries the "
   "daylight."),
  systems=("Wood or coal stove (later oil furnace) with the flue through the roof; daylighting is "
   "the lighting system - tall windows, high ceilings. Modern restorations add discreet HVAC and "
   "accessible restrooms."),
  spaces=[("Classroom",28,22),("Entry Vestibule",10,8),("Cloakroom",10,6),("Teacher Corner",8,8)],
  materials=["Wood frame and siding","Gabled shingle roof","Belfry",
   "Slate blackboards","Tall double-hung windows","Wood stove or furnace","Pine floors"],
  codes=["IBC educational (historic)","Historic preservation standards","ADA (restorations)","NEC 2023"],
  sheets=["A-101 Floor Plan","A-201 Elevations"]),
 dict(name="Elementary School", group="Classroom Buildings", style="Elementary School",
  history=("Elementary schools standardized after World War II into the finger plan - classroom "
   "wings extending from a central core - and later the pod plan around shared commons. The "
   "classroom module (about 900 square feet for 25 students) has been stable for 70 years."),
  layout=("Classroom wings of 4 to 6 rooms each with shared project areas; administration at the "
   "entry with secure vestibule; cafeteria/gymnatorium multipurpose room; library media center "
   "central; art and music rooms with acoustic separation; playground beyond."),
  structure=("Single-story steel or masonry bearing-wall with bar joists; classroom wings repeat a "
   "structural module. Secure vestibule with ballistic glazing at entry is now standard."),
  systems=("HVAC per classroom for individual control and ventilation (high outdoor air for kids); "
   "low background noise targets (35 dBA); daylighting with glare control. Kitchen serving the "
   "cafeteria needs full commercial equipment."),
  spaces=[("Classroom A",30,30),("Classroom B",30,30),("Classroom C",30,30),("Classroom D",30,30),
   ("Admin Suite",25,18),("Library",40,30),("Cafeteria/Gym",60,40),("Art Room",30,25),
   ("Music Room",30,25),("Kitchen",25,20),("Secure Vestibule",12,10)],
  materials=["Masonry/steel frame","Secure entry vestibule","Classroom casework",
   "Acoustic ceilings (NRC 0.70+)","Daylighting controls","Commercial kitchen","Playground equipment"],
  codes=["IBC educational E","IBC egress Chapter 10","ADA schools","ASHRAE 62.1 ventilation"],
  sheets=["A-101 Floor Plan","A-201 Elevations","M-101 HVAC Plan"]),
 dict(name="Middle School", group="Classroom Buildings", style="Middle School",
  history=("Middle schools (grades 6-8) emerged in the 1960s-70s between elementary and high school, "
   "and their architecture followed the team model: interdisciplinary teams of 100-150 students "
   "sharing a wing with team commons. The building teaches collaboration by layout."),
  layout=("Team wings with 4 to 5 classrooms around a team commons; science labs with prep rooms; "
   "electives wing (art, music, tech); gymnasium with locker rooms; cafeteria; library. Admin "
   "suite with secure entry at the front."),
  structure=("Steel frame with masonry or metal panel; gymnasium as a separate long-span structure. "
   "Science labs need acid-resistant casework and emergency fixtures."),
  systems=("Zoned HVAC per team wing; lab ventilation and gas; gym HVAC for high occupancy; "
   "building-wide PA, clocks, and security. Science prep rooms need chemical storage."),
  spaces=[("Team Wing A",80,40),("Team Commons",30,25),("Science Lab",30,25),("Science Prep",12,10),
   ("Gymnasium",84,50),("Locker Rooms",30,20),("Cafeteria",50,35),("Library",40,30),
   ("Art Room",30,25),("Music Room",35,25),("Admin Suite",25,18)],
  materials=["Steel frame","Gymnasium long-span","Science casework",
   "Team commons furniture","Acoustic treatment","Security vestibule","Athletic flooring"],
  codes=["IBC educational E","IFC science labs","ADA schools","ASHRAE 62.1"],
  sheets=["A-101 Floor Plan","M-101 HVAC Plan","L-101 Lab Details"]),
 dict(name="High School", group="Classroom Buildings", style="Comprehensive High School",
  history=("The comprehensive high school - academics, career-tech, athletics, arts under one roof - "
   "was the 20th century's great educational building project. The modern version organizes "
   "1,000-plus students into small learning communities to recover the human scale."),
  layout=("Academic wings by department; career-tech wing with shops and labs; science wing; "
   "performing arts (auditorium, band, choir); athletics (gym, field house, stadium); cafeteria "
   "commons; library media center as the academic heart. Main entry with event access separate "
   "from academic entries."),
  structure=("Steel frame campus or single large building; long-span structures for gym and "
   "auditorium; shops need heavy floors and high bays. Phased construction is common - design "
   "for expansion joints."),
  systems=("Complex zoning: shops need dust collection and welding ventilation; labs need gas and "
   "fume hoods; auditorium needs theatrical systems; kitchens serve 1,000-plus. Building "
   "automation ties it together."),
  spaces=[("Academic Wing",120,50),("Science Wing",80,40),("CTE Shops",80,50),("Auditorium",70,50),
   ("Gymnasium",94,55),("Cafeteria Commons",70,45),("Library",60,40),("Admin",30,20),
   ("Band/Choir",40,30),("Kitchen",30,25)],
  materials=["Steel frame campus","Long-span gym/auditorium","CTE shop equipment",
   "Theatrical systems","Commercial kitchen","Athletic facilities","Building automation"],
  codes=["IBC educational E","IBC assembly A","IFC shops and labs","ADA schools"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan","M-101 HVAC Zones"]),
 dict(name="Science Wing", group="Specialty Facilities", style="School Science Wing",
  history=("School science wings evolved from the 19th-century demonstration lecture hall to the "
   "modern lab-classroom: every student at a lab station, prep rooms behind, and safety systems "
   "throughout. The 1990s added the shared prep model - one prep room serving four labs."),
  layout=("Lab-classrooms in a row sharing a central prep room; chemical storage in a dedicated "
   "fire-rated room; fume hoods on exterior walls; greenhouse or outdoor lab adjacent. Teacher "
   "prep with sight-lines into labs."),
  structure=("Lab floors need chemical-resistant finishes and floor drains; casework anchored for "
   "seismic where required; the chemical storage room is 2-hour rated with spill containment."),
  systems=("Lab ventilation with fume-hood exhaust; emergency gas shutoffs; eyewash and safety "
   "showers within 10 seconds of every station; acid waste piping to neutralization."),
  spaces=[("Lab-Classroom A",32,28),("Lab-Classroom B",32,28),("Prep Room",20,15),
   ("Chemical Storage",12,10),("Greenhouse",20,15),("Teacher Prep",12,10)],
  materials=["Lab casework","Fume hoods","Chemical storage cabinets",
   "Acid-resistant flooring","Emergency fixtures","Acid waste piping","Lab gas systems"],
  codes=["IFC laboratories","NFPA 45","IBC educational E","ANSI Z9.5 ventilation"],
  sheets=["A-101 Floor Plan","L-101 Lab Details","M-101 Lab Ventilation"]),
 dict(name="Gymnasium", group="Specialty Facilities", style="School Gymnasium",
  history=("School gymnasiums descend from 19th-century German Turnhallen; the American version "
   "added basketball (invented 1891) and bleachers. The modern gym is a community asset - "
   "daytime PE, evening leagues - engineered for 1,000-plus occupants."),
  layout=("Main court with cross courts; bleachers on one or both sides; lobby with concessions and "
   "ticketing; locker rooms with showers; training room; equipment storage; officials' room. "
   "Dividing curtain splits the floor for simultaneous classes."),
  structure=("Long-span steel (90-plus feet clear) with acoustic deck; bleachers need their own "
   "structure and egress; the floor is the famous maple system - sleepers, subfloor, and finish "
   "with precise resilience."),
  systems=("High-bay HVAC for big volumes and crowds; sports lighting at 50-plus foot-candles; "
   "sound system for events; scoreboards and shot clocks. Locker rooms need heavy ventilation."),
  spaces=[("Main Court",94,55),("Bleachers",60,20),("Lobby",30,20),("Locker Room A",30,20),
   ("Locker Room B",30,20),("Training Room",20,15),("Storage",20,15),("Concessions",15,10)],
  materials=["Long-span steel","Maple sports floor","Retractable bleachers",
   "Acoustic wall panels","Sports lighting","Dividing curtain","Scoreboard system"],
  codes=["IBC assembly A-3/A-4","IBC bleachers 1029","ADA assembly seating","NEC 2023"],
  sheets=["A-101 Floor Plan","S-101 Long-Span Details","E-101 Sports Lighting"]),
 dict(name="Library Media Center", group="Specialty Facilities", style="School Library",
  history=("School libraries grew from book rooms into media centers in the 1970s and into learning "
   "commons today: fewer stacks, more collaboration zones, a makerspace corner, and the librarian "
   "as technology teacher. Daylight and quiet remain the constants."),
  layout=("Open reading room with varied seating zones; collaboration rooms with writable walls; "
   "stacks reduced to a core collection; makerspace with 3D printers; production room for video; "
   "librarian office with sight-lines over the floor."),
  structure=("Open floor plate with minimal columns; the makerspace needs power and ventilation for "
   "equipment; stacks (where they remain) need 150 psf capacity."),
  systems=("Quiet HVAC (35 dBA target); tunable lighting for reading vs. screen work; robust Wi-Fi "
   "and device charging everywhere; the makerspace needs dust collection and fume extraction."),
  spaces=[("Reading Room",50,35),("Collaboration Rooms",20,15),("Stacks Core",30,20),
   ("Makerspace",25,20),("Production Room",15,12),("Librarian Office",12,10)],
  materials=["Varied seating zones","Writable wall surfaces","Makerspace equipment",
   "Tunable LED lighting","Acoustic clouds","Robust Wi-Fi","Reduced stacks"],
  codes=["IBC educational E","IBC stack loads","ADA libraries","NEC 2023"],
  sheets=["A-101 Floor Plan","T-101 Technology Plan"]),
 dict(name="Cafeteria Hall", group="Support", style="School Cafeteria",
  history=("School cafeterias scaled up with the National School Lunch Program (1946): the "
   "servery line, the tray rail, and seating for hundreds in 20-minute shifts. Modern versions "
   "add food-court variety and the commons model - one big student union space."),
  layout=("Servery with multiple stations facing the dining hall; tray return and dish room behind; "
   "kitchen with dry, cooler, and freezer storage; dining hall with varied seating; outdoor "
   "terrace where climate allows. Flow: enter, serve, eat, return, exit - no crossing streams."),
  structure=("Big open dining volume (often double-height) with the kitchen as a separate "
   "fire-rated zone; the servery wall carries plumbing, gas, and power to every station."),
  systems=("Commercial kitchen: Type I hoods, grease interceptors, walk-in coolers; dining hall "
   "HVAC for 500-plus occupants; tray conveyor or return windows; waste and recycling stations."),
  spaces=[("Dining Hall",70,45),("Servery",40,15),("Kitchen",40,25),("Dry Storage",15,12),
   ("Cooler/Freezer",15,12),("Dish Room",15,12),("Tray Return",15,8)],
  materials=["Commercial kitchen line","Type I hoods","Servery counters",
   "Walk-in coolers","Dining furniture","Acoustic treatment","Tray return system"],
  codes=["IMC commercial cooking","NFPA 96","FDA Food Code","IBC assembly"],
  sheets=["A-101 Floor Plan","M-101 Hood Plan","K-101 Kitchen Details"]),
 dict(name="Vocational Workshop", group="Specialty Facilities", style="CTE / Shop Building",
  history=("Vocational shops - wood, metal, auto - descend from the manual training high schools of "
   "the 1890s. Today's career-tech shops teach robotics, welding, and automotive diagnostics in "
   "spaces closer to industry than to classrooms."),
  layout=("High-bay shop floor with equipment zones; tool crib; classroom adjacent with windows "
   "into the shop; finishing room separated and ventilated; outdoor project yard. Auto shops add "
   "lifts and alignment bays."),
  structure=("High-bay steel frame (16-plus feet); floors for equipment point loads; the finishing "
   "room is fire-separated; welding areas need spark separation."),
  systems=("Dust collection at every woodworking station; welding fume extraction; compressed air "
   "throughout; auto shops need vehicle exhaust extraction and fluid handling. Eye wash and "
   "first aid central."),
  spaces=[("Shop Floor",80,50),("Tool Crib",15,12),("Classroom",30,25),("Finishing Room",20,15),
   ("Auto Bays",50,30),("Project Yard",60,40)],
  materials=["Shop machinery","Dust collection","Welding ventilation",
   "Auto lifts","Compressed air","Fire-separated finishing","Eye wash stations"],
  codes=["IFC shops","NFPA 51B hot work","IBC educational E","OSHA training"],
  sheets=["A-101 Floor Plan","M-101 Dust/Exhaust Plan"]),
 dict(name="Art School Studio", group="Specialty Facilities", style="Art Studio Building",
  history=("Art school studios need the north light of 19th-century Parisian ateliers: big "
   "windows, high ceilings, and floors that survive everything. The modern studio building adds "
   "kilns, darkrooms (now digital labs), and gallery space for critique."),
  layout=("Studios with 12-plus-foot ceilings and north glazing; critique wall in each; kiln room "
   "fire-separated; printmaking with ventilation; digital lab; gallery at entry for shows; "
   "material storage and spray booth."),
  structure=("High-bay frame with the great north windows; kiln room of masonry with its own "
   "ventilation; spray booth fire-rated. Floors: sealed concrete that cleans."),
  systems=("Kiln ventilation and power (kilns are huge electrical loads); spray booth exhaust and "
   "fire suppression; printmaking ventilation; gallery track lighting."),
  spaces=[("Studio A",40,30),("Studio B",40,30),("Kiln Room",15,12),("Printmaking",25,20),
   ("Digital Lab",25,20),("Gallery",40,25),("Spray Booth",12,10),("Storage",15,12)],
  materials=["North-light glazing","Kilns","Spray booth",
   "Printmaking presses","Gallery track lighting","Sealed concrete floors","Crit walls"],
  codes=["IFC kilns and booths","NFPA 33 spray","IBC educational E","NEC 2023"],
  sheets=["A-101 Floor Plan","M-101 Ventilation Plan"]),
 dict(name="Auditorium Building", group="Specialty Facilities", style="School Auditorium",
  history=("School auditoriums are the community's theater: daytime assembly, evening concerts and "
   "plays. The form - fan or shoebox hall, fly tower optional, balcony - comes from 19th-century "
   "opera houses scaled to school budgets."),
  layout=("Auditorium with stage, orchestra pit (optional), and balcony; lobby with concessions; "
   "backstage: dressing rooms, green room, scene shop, costume storage; control booth at rear. "
   "Music rooms adjacent for warm-up."),
  structure=("Long-span roof over the hall; stage house (fly tower) of masonry where full rigging "
   "is provided; balcony structure with its own egress; acoustic shaping in walls and ceiling."),
  systems=("Theatrical: dimming, stage lighting positions, sound, rigging, curtains. HVAC must be "
   "silent (25 dBA target) - the audience hears everything. Assisted listening throughout."),
  spaces=[("Auditorium",70,55),("Stage",40,30),("Lobby",40,25),("Dressing Rooms",20,15),
   ("Scene Shop",30,20),("Control Booth",12,8),("Balcony",40,20)],
  materials=["Long-span structure","Theatrical rigging","Stage lighting and dimming",
   "Acoustic shaping","Silent HVAC","Assisted listening","Scene shop tools"],
  codes=["IBC assembly A-1","IBC stage provisions","ADA assembly","NFPA 101"],
  sheets=["A-101 Floor Plan","A-301 Sections","T-101 Theatrical Plan"]),
 dict(name="Administration Building", group="Support", style="School Administration",
  history=("School administration buildings - the district office - centralize what schools share: "
   "superintendent, business, HR, curriculum, and the board room where the public watches "
   "decisions happen. The board room is the democratic heart."),
  layout=("Public entry to board room and reception; departmental office wings; records vault; "
   "conference and training rooms; print/mail center. The board room needs public seating, dais, "
   "and broadcast capability."),
  structure=("Conventional office construction; the records vault needs fire-rated, high-load "
   "construction; board room needs acoustic treatment and AV infrastructure."),
  systems=("Standard office HVAC with after-hours capability for board meetings; board room AV with "
   "recording and streaming; records vault climate control."),
  spaces=[("Board Room",40,30),("Reception",20,15),("Office Wing",60,30),("Records Vault",20,15),
   ("Conference",20,15),("Training Room",30,20),("Print/Mail",15,12)],
  materials=["Board room AV","Dais and public seating","Records vault",
   "Office systems furniture","Broadcast streaming","Conference AV"],
  codes=["IBC business occupancy","Open meetings law provisions","ADA public facilities","NEC 2023"],
  sheets=["A-101 Floor Plan","AV-101 Board Room Plan"]),
]

FACTORIES = [
 dict(name="Assembly Plant", group="Heavy Industry", style="General Assembly Plant",
  history=("Assembly plants descend from Ford's Highland Park (1910) and River Rouge (1928): the "
   "moving line, parts fed from the sides, finished product out the end. Modern plants add "
   "robotics and the andon system - but the long, clear building is still the machine."),
  layout=("Assembly line down the center with workstations on both sides; subassembly feeders "
   "along the walls; parts supermarkets at line-side; shipping at one end, receiving at the "
   "other; offices and cafeteria in a corner annex."),
  structure=("Steel frame with 30-by-60-foot bays, 24-to-32-foot clear height; crane bays where "
   "heavy lifts occur; floors for point loads and anchor bolts everywhere - the line gets "
   "reconfigured."),
  systems=("Process power (often 480V, thousands of amps); compressed air as a utility; paint or "
   "process exhaust where applicable; andon and MES data networks; fire protection for the "
   "commodity."),
  spaces=[("Assembly Line",300,60),("Subassembly",100,40),("Parts Supermarket",80,30),
   ("Receiving",60,30),("Shipping",60,30),("Offices",40,25),("Cafeteria",30,20),("Maintenance",30,20)],
  materials=["Structural steel frame","Crane runway beams","Compressed air grid",
   "ESFR sprinklers","High-bay LED","Epoxy floors","Andon/MES network"],
  codes=["IBC factory F-1","NFPA 13","OSHA manufacturing","NEC 2023 industrial"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan","M-101 Process Utilities"]),
 dict(name="Textile Mill", group="Light Industry", style="Textile Mill",
  history=("Textile mills drove the Industrial Revolution - Lowell's Massachusetts mills of the "
   "1820s were America's first great factories. The sawtooth roof with north-facing glazing gave "
   "weavers perfect diffuse light; modern mills use the same daylighting logic with new machines."),
  layout=("Weaving or knitting floor in the big open volume; yarn preparation (winding, warping) "
   "upstream; dyeing and finishing in a wet-process wing; warehouse for cones and rolls; offices "
   "at the entry."),
  structure=("Heavy floors for looms (vibration!); sawtooth or monitor roofs for daylight; the dye "
   "house needs corrosion-resistant construction and floor drains everywhere."),
  systems=("Humidification - textile processes need 65-75 percent RH; dust and lint collection; dye "
   "house steam, water treatment, and effluent handling; compressed air for air-jet looms."),
  spaces=[("Weaving Floor",150,100),("Yarn Prep",60,30),("Dye House",60,40),("Finishing",50,30),
   ("Warehouse",60,40),("Offices",30,20),("Boiler Room",25,20)],
  materials=["Heavy loom floors","Sawtooth daylighting","Humidification system",
   "Lint collection","Dye vats and ranges","Water treatment","Effluent handling"],
  codes=["IBC factory F-1","IFC dye operations","EPA effluent","OSHA textiles"],
  sheets=["A-101 Floor Plan","M-101 Humidification Plan"]),
 dict(name="Food Processing Plant", group="Food / Beverage", style="Food Processing Facility",
  history=("Food processing plants industrialized the kitchen: canneries in the 1800s, frozen-food "
   "plants after Clarence Birdseye's 1920s quick-freeze patents. Sanitary design - smooth, "
   "washable, sloped-to-drain - is the entire architecture."),
  layout=("Raw receiving and storage; processing hall with equipment lines; packaging hall; cooler "
   "and freezer; dry storage; shipping. Personnel flow: entry, locker rooms, hand-wash, then the "
   "floor - no cross-contamination paths."),
  structure=("Insulated metal panel or tilt-up with washable interiors; floors sloped to drains with "
   "chemical-resistant coatings; the freezer box within the building envelope."),
  systems=("Refrigeration (ammonia common); steam for cooking and sanitation; compressed air "
   "(food-grade); washdown water and wastewater pretreatment; pest-proof detailing everywhere."),
  spaces=[("Processing Hall",120,80),("Packaging Hall",80,40),("Raw Storage",40,30),
   ("Cooler",40,30),("Freezer",40,25),("Dry Storage",40,25),("Shipping",40,20),
   ("Locker Rooms",25,18),("QA Lab",15,12)],
  materials=["Washable wall panels","Sloped chemical floors","Ammonia refrigeration",
   "Steam system","Food-grade air","Wastewater pretreatment","Pest-proof detailing"],
  codes=["FDA FSMA","USDA (meat/poultry)","IBC factory F-1","3-A sanitary standards"],
  sheets=["A-101 Floor Plan","M-101 Refrigeration Plan","P-101 Sanitary Drainage"]),
 dict(name="Steel Fabrication Shop", group="Heavy Industry", style="Structural Steel Shop",
  history=("Steel fabrication shops cut, fit, and weld the skeletons of buildings and bridges. The "
   "form - long bays with overhead cranes, fitting beds, and blast/paint at the end - was set by "
   "early-1900s bridge shops and hasn't fundamentally changed."),
  layout=("Receiving and material storage at one end; cutting (saw, plasma, coping); fitting beds; "
   "welding stations; blast and paint booths; finished storage and loadout at the other end. "
   "Crane runway serves the full length."),
  structure=("Heavy steel frame with crane runway girders (often 10-to-20-ton cranes); 30-foot-plus "
   "clear height; floors for extreme point loads; the blast/paint area is fire-separated."),
  systems=("Welding fume extraction; compressed air; overhead cranes; blast dust collection; paint "
   "booth ventilation and fire suppression; massive electrical service for welders."),
  spaces=[("Fab Bays",200,60),("Cutting",60,30),("Fitting Beds",80,30),("Welding",60,30),
   ("Blast Booth",30,20),("Paint Booth",30,20),("Material Storage",60,30),("Offices",25,15)],
  materials=["Crane runway girders","Overhead bridge cranes","Welding stations",
   "Plasma cutting tables","Blast/paint booths","Fume extraction","Heavy-duty floors"],
  codes=["IBC factory F-1","AWS welding","NFPA 33 spray","OSHA steel"],
  sheets=["A-101 Floor Plan","S-101 Crane Details","M-101 Ventilation Plan"]),
 dict(name="Electronics Assembly Plant", group="Light Industry", style="Electronics Manufacturing",
  history=("Electronics assembly moved from 1960s hand-soldering lines to surface-mount technology "
   "(SMT) lines: pick-and-place machines, reflow ovens, and automated test. Cleanliness and ESD "
   "control define the building more than heavy structure."),
  layout=("SMT lines in the ESD-controlled production hall; through-hole and hand-assembly areas; "
   "test and burn-in; warehouse for components (dry storage for moisture-sensitive parts); "
   "offices and engineering labs adjacent."),
  structure=("Light, clean construction: sealed floors, smooth walls, minimal dust generation. "
   "Vibration control for pick-and-place precision; the building is a clean box, not a heavy one."),
  systems=("ESD flooring and controls throughout; tight temperature/humidity control; nitrogen for "
   "reflow; fume extraction at soldering; UPS and clean power for test."),
  spaces=[("SMT Hall",100,60),("Assembly",60,30),("Test/Burn-In",40,25),("Component Warehouse",50,30),
   ("Dry Storage",20,15),("Engineering Lab",30,20),("Offices",30,20)],
  materials=["ESD flooring","SMT pick-and-place lines","Reflow ovens",
   "Nitrogen system","Fume extraction","Clean power/UPS","Moisture dry cabinets"],
  codes=["IBC factory F-1","ANSI/ESD S20.20","IPC standards","NEC 2023 industrial"],
  sheets=["A-101 Floor Plan","E-101 ESD Plan","M-101 Process Plan"]),
 dict(name="Brewery", group="Food / Beverage", style="Craft/Production Brewery",
  history=("Breweries are among the oldest factories - Mesopotamian beer predates writing. The "
   "modern craft brewery pairs a working brewhouse with a taproom: production as theater, a form "
   "that revived with American craft brewing after 1980."),
  layout=("Brewhouse with kettles and mash tuns; fermentation cellar with tank farm; packaging "
   "(canning/bottling) line; cold storage; taproom and retail at the front with views into "
   "production; grain handling and spent-grain loadout at the rear."),
  structure=("Brewhouse needs height for the kettle stack and steam venting; floors sloped to drains "
   "with chemical-resistant coatings; the tank farm needs floor capacity for full vessels."),
  systems=("Steam boiler; glycol chilling for fermentation; compressed air and CO2; CIP (clean-in- "
   "place) chemical handling; wastewater with high BOD - pretreatment often required."),
  spaces=[("Brewhouse",50,35),("Fermentation Cellar",50,30),("Packaging",40,25),("Cold Storage",30,20),
   ("Taproom",40,25),("Grain Handling",20,15),("Boiler/Chiller",25,20)],
  materials=["Brew kettles and tuns","Fermentation tanks","Glycol chilling",
   "Steam boiler","Canning line","Sloped chemical floors","Taproom millwork"],
  codes=["IBC factory F-2","TTB brewery regulations","FDA food safety","IFC CO2 storage"],
  sheets=["A-101 Floor Plan","M-101 Process Plan","P-101 Drainage Plan"]),
 dict(name="Paper Mill", group="Heavy Industry", style="Paper Mill",
  history=("Paper mills mechanized in the early 1800s with the Fourdrinier machine - a continuous "
   "wire forming the sheet. Modern mills are among the largest single machines on earth: a paper "
   "machine can be 500 feet long, and the building is literally wrapped around it."),
  layout=("Pulp preparation (or recycled fiber plant); the paper machine hall - one enormous room; "
   "finishing (winders, sheeters); roll warehouse; chemical storage; power/boiler house; water "
   "treatment. The machine hall dominates everything."),
  structure=("The machine hall is a special structure: heavy foundations for the machine (vibration "
   "isolation), high bays with crane service, and corrosion-resistant construction in the wet end."),
  systems=("Enormous steam, water, and power demands - mills often cogenerate; white-water recycling; "
   "effluent treatment; hood ventilation over the machine (heat and humidity)."),
  spaces=[("Machine Hall",400,80),("Pulp Prep",100,50),("Finishing",80,40),("Roll Warehouse",100,50),
   ("Chemical Storage",40,25),("Boiler House",50,30),("Water Treatment",60,40)],
  materials=["Paper machine","Machine foundations","Corrosion-resistant wet end",
   "Cogeneration plant","White-water system","Effluent treatment","Overhead cranes"],
  codes=["IBC factory F-1","EPA effluent","TAPPI standards","OSHA paper"],
  sheets=["A-101 Floor Plan","S-101 Machine Foundations","M-101 Utilities Plan"]),
 dict(name="Auto Assembly Plant", group="Heavy Industry", style="Automotive Assembly",
  history=("Auto assembly plants are the cathedrals of mass production: Ford's River Rouge (1928) "
   "took in raw materials and shipped finished cars. Modern plants add the body shop's robot "
   "armies and the paint shop's clean-room conditions."),
  layout=("Stamping at one end (or nearby); body shop with welding robots; paint shop (sealed, "
   "conditioned); general assembly - trim and final - in the longest hall; quality gates; "
   "shipping yard beyond. Conveyors link the buildings."),
  structure=("Massive steel frame; body shop floors for robot anchoring; paint shop as a clean "
   "building-within-a-building; general assembly needs 30-foot clear with conveyor steel "
   "throughout."),
  systems=("Paint shop: huge conditioned air, water treatment, and fire protection; body shop: "
   "welding power and fume control; general assembly: compressed air, andon, and MES networks; "
   "the whole plant on redundant power."),
  spaces=[("Body Shop",300,120),("Paint Shop",250,100),("General Assembly",400,120),
   ("Stamping",200,100),("Quality Gates",60,30),("Offices",50,30),("Shipping Yard",400,200)],
  materials=["Welding robot lines","Paint booths and ovens","Conveyor systems",
   "Stamping presses","Andon/MES network","Redundant power","ESFR sprinklers"],
  codes=["IBC factory F-1","NFPA 33 paint","OSHA auto","NEC 2023 industrial"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan","M-101 Process Utilities"]),
 dict(name="Chemical Processing Plant", group="Heavy Industry", style="Chemical Process Facility",
  history=("Chemical plants grew from 19th-century alkali works into today's integrated complexes: "
   "reactor trains, distillation columns, and tank farms in carefully zoned plots. Inherently "
   "safer design - smaller inventories, milder conditions - is the modern discipline."),
  layout=("Process units in zoned blocks with spacing per code; tank farm with secondary "
   "containment; control building (blast-resistant) central; utilities (boiler, cooling, air, "
   "nitrogen); warehouse; rail/truck loading; flare at the safe distance."),
  structure=("Open steel process structures (pipe racks and equipment modules); blast-resistant "
   "control building; tank foundations with containment dikes; pipe bridges between units."),
  systems=("Process control (DCS) everywhere; fire and gas detection; emergency shutdown systems; "
   "flare and relief systems; scrubbers and treatment for emissions; lightning and grounding "
   "grids."),
  spaces=[("Process Block A",120,80),("Process Block B",100,60),("Tank Farm",150,100),
   ("Control Building",40,25),("Utilities",60,40),("Warehouse",60,30),("Loading",80,40)],
  materials=["Process vessels and columns","Pipe racks","DCS control system",
   "Blast-resistant control room","Secondary containment","Fire/gas detection","Flare system"],
  codes=["OSHA PSM","EPA RMP","NFPA 30","API standards"],
  sheets=["A-101 Plot Plan","P-101 P&ID Index","E-101 Hazardous Area Plan"]),
 dict(name="Furniture Factory", group="Light Industry", style="Furniture Manufacturing",
  history=("Furniture factories mechanized cabinetmaking in the late 1800s - Grand Rapids, "
   "Michigan became Furniture City. The modern plant runs a flow: rough mill, machining (CNC), "
   "assembly, finishing, upholstery, warehouse."),
  layout=("Rough mill and dry kilns at receiving; CNC machining center; assembly floor; finishing "
   "(spray booths, drying); upholstery wing; finished-goods warehouse; showroom at the office "
   "entry."),
  structure=("Steel frame with high bays; the rough mill needs dust explosion protection; finishing "
   "is fire-separated; warehouse racking for finished goods."),
  systems=("Dust collection throughout the wood areas; spray booth ventilation and suppression; "
   "compressed air; dry kiln heat; finishing ovens. Wood waste often fuels the boiler."),
  spaces=[("Rough Mill",80,50),("CNC Center",60,40),("Assembly",80,50),("Finishing",60,30),
   ("Upholstery",50,30),("Warehouse",80,50),("Showroom",30,20),("Kilns",40,25)],
  materials=["CNC machining centers","Dust collection","Spray booths",
   "Dry kilns","Upholstery lines","Warehouse racking","Wood-waste boiler"],
  codes=["IBC factory F-1","NFPA 664 woodworking","NFPA 33 spray","OSHA woodworking"],
  sheets=["A-101 Floor Plan","M-101 Dust Collection","FP-101 Suppression Plan"]),
 dict(name="Print Shop Factory", group="Light Industry", style="Commercial Printing Plant",
  history=("Commercial printing plants grew from Gutenberg's press through the 19th-century rotary "
   "press to offset lithography's 20th-century dominance. Digital presses now share the floor, "
   "but the big offset press - 100 feet of steel - still anchors large plants."),
  layout=("Press hall with the big presses in a row; prepress and platemaking; bindery "
   "(cutters, folders, stitchers); paper warehouse (climate-controlled); shipping; customer "
   "service offices at entry."),
  structure=("Press foundations are special: massive, vibration-isolated, and precisely level - the "
   "press manufacturer specifies them. Paper warehouse needs 55-65F and 45-55 percent RH."),
  systems=("Compressed air for presses; ink and solvent handling with ventilation; paper dust "
   "collection; the warehouse HVAC holds tight climate for paper stability."),
  spaces=[("Press Hall",150,60),("Prepress",40,25),("Bindery",60,40),("Paper Warehouse",60,40),
   ("Shipping",40,25),("Offices",30,20)],
  materials=["Offset presses","Press foundations","Bindery equipment",
   "Climate-controlled warehouse","Ink handling","Paper dust collection","Compressed air"],
  codes=["IBC factory F-1","IFC solvent storage","NEC 2023 industrial","OSHA printing"],
  sheets=["A-101 Floor Plan","S-101 Press Foundations","M-101 Ventilation Plan"]),
 dict(name="Packaging Plant", group="Light Industry", style="Packaging Manufacturing",
  history=("Packaging plants - corrugated boxes, folding cartons, flexible film - grew with "
   "consumer goods in the 1900s. The corrugator, a 300-foot machine turning liner and fluting "
   "into board, is the heart of the box plant."),
  layout=("Corrugator line down the center; converting (die-cutters, gluers) downstream; "
   "finished-goods warehouse; roll-stock storage for liner; ink room; offices at entry."),
  structure=("Long clear building for the corrugator; roll storage needs heavy floors (paper rolls "
   "weigh tons); the ink room is fire-separated."),
  systems=("Steam for the corrugator; compressed air; dust collection at converting; starch "
   "adhesive handling; warehouse fire protection for the paper commodity."),
  spaces=[("Corrugator Line",300,40),("Converting",120,60),("Finished Warehouse",100,60),
   ("Roll Storage",80,40),("Ink Room",20,15),("Offices",30,20)],
  materials=["Corrugator","Die-cutters and gluers","Steam system",
   "Roll handling","Starch system","Warehouse racking","Dust collection"],
  codes=["IBC factory F-1","NFPA 13 paper storage","IFC ink storage","OSHA packaging"],
  sheets=["A-101 Floor Plan","M-101 Steam Plan"]),
]
