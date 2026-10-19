#!/usr/bin/env python3
"""Building blueprint archetypes: offices, warehouses, apartments, barns."""

OFFICES = [
 dict(name="Open-Plan Office", group="Corporate", style="Open Office",
  history=("The open-plan office was formalized in 1950s Germany as Burolandschaft - office "
   "landscape - and reached America through 1960s action offices. The 1968 Herman Miller Action "
   "Office II invented the cubicle; the 2000s tore the cubicles back down into benching. The "
   "pendulum keeps swinging, but the engineering - lighting, acoustics, air - stays the same."),
  layout=("Benching clusters of 4 to 8 desks on a planning grid, usually 5 or 6 feet; enclosed "
   "meeting rooms and phone booths ring the core; break and copy zones anchor the columns. "
   "Circulation runs on a clear loop so no desk is more than a short walk from egress."),
  structure=("Tenant fit-out inside a core-and-shell building: demountable or drywall partitions, "
   "raised access floor or overhead distribution. The base building provides the structure - "
   "typically steel or concrete frame with 30-foot bays."),
  systems=("VAV air distribution with one zone per 4 to 6 workstations; lighting at 30 to 50 "
   "foot-candles with daylight dimming at the perimeter. Acoustics are the make-or-break system: "
   "masking, absorptive ceilings, and enclosed rooms for focused work."),
  spaces=[("Workstations",60,30),("Meeting Room A",16,12),("Meeting Room B",12,10),("Phone Booths",8,8),
   ("Break Room",16,12),("Copy/Print",10,8),("Reception",14,10),("Storage",10,8),("Restrooms",14,10)],
  materials=["Demountable partitions","Benching workstations","Acoustic ceiling tile",
   "Sound masking system","Raised access floor","LED troffers with dimming","Carpet tile"],
  codes=["IBC business occupancy","IBC egress Chapter 10","ADA work areas","ASHRAE 90.1"],
  sheets=["A-101 Floor Plan","A-801 Interior Elevations","M-101 HVAC Zones","E-101 Lighting Plan"]),
 dict(name="Executive Suite", group="Corporate", style="Executive Office Suite",
  history=("The executive suite - private offices along the window line, assistants outside - "
   "descends from the 19th-century counting house and the mid-century corporate headquarters. "
   "Law firms and banks kept the form longest; even as open plans spread, the corner office "
   "remains the symbol of arrival."),
  layout=("Private offices line the perimeter glazing; assistants and open workstations sit "
   "inboard. A boardroom anchors one corner with video-conference capability; the reception "
   "sequence - waiting, reception desk, coat closet - manages the arrival ritual."),
  structure=("Full-height drywall or demountable partitions with acoustic ratings of STC 45-plus "
   "for confidential offices. Sidelights and transoms borrow daylight into the interior; doors "
   "get sound seals."),
  systems=("Dedicated HVAC zones per office for individual control; lighting scenes from focused "
   "task to presentation. Boardroom AV - cameras, microphones, displays - is engineered like a "
   "small studio."),
  spaces=[("Corner Office",16,14),("Private Office A",14,12),("Private Office B",14,12),
   ("Assistant Zone",20,12),("Boardroom",24,16),("Reception",14,12),("Waiting",12,10),
   ("File Room",10,8),("Pantry",10,8)],
  materials=["STC-45 partitions","Wood veneer doors","Demountable glass fronts",
   "Boardroom AV system","Task lighting","Stone reception desk","Carpet and wood floors"],
  codes=["IBC business occupancy","ASTM E90 acoustics","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-801 Interior Elevations","AV-101 Audiovisual Plan"]),
 dict(name="Co-Working Hub", group="Corporate", style="Co-Working Space",
  history=("Co-working grew from 1990s hackerspaces and the first San Francisco co-working space "
   "of 2005 into a global industry. The architecture sells flexibility: hot desks by day, event "
   "space by night, and enough phone booths to keep the open floor civilized."),
  layout=("Hot-desk floor in the center with day lockers; dedicated desks along one wall; private "
   "offices and team suites at the perimeter. Phone booths scattered at a ratio of about one per "
   "15 members; event space near the entry doubles as lounge."),
  structure=("High-impact fit-out: durable finishes, abundant power (floor boxes on a tight grid), "
   "and robust Wi-Fi with wired backup. Partitions favor glass for borrowed light and community "
   "visibility."),
  systems=("Dense occupancy drives ventilation - design for 15 to 20 cfm per person, not the office "
   "default. Booking systems for rooms; access control per member tier; commercial-grade coffee "
   "and kitchen equipment."),
  spaces=[("Hot Desk Floor",50,30),("Dedicated Desks",30,15),("Private Offices",20,12),
   ("Phone Booths",10,8),("Event Lounge",25,18),("Kitchen",14,10),("Print Bar",8,8),("Lockers",12,6)],
  materials=["Durable LVT flooring","Glass office fronts","Floor power boxes",
   "Enterprise Wi-Fi","Booking displays","Commercial coffee bar","Acoustic clouds"],
  codes=["IBC business/assembly","IBC occupant load","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","T-101 Technology Plan","E-101 Power Plan"]),
 dict(name="Law Firm Office", group="Professional", style="Law Office",
  history=("Law offices kept the cellular plan long after others went open: confidentiality is the "
   "practice. The classic layout - partner offices on glass, associates inside, library at the "
   "core - comes from the early-1900s skyscraper firms and survives because privilege demands "
   "closed doors."),
  layout=("Uniform partner offices (often 10x15) on the perimeter; associate offices inboard or on "
   "a second tier of windows; secretarial stations outside office doors. Library/conference center "
   "at the core; file rooms secured with limited access."),
  structure=("STC 50 partitions for partner offices; solid-core doors with seals. The law library's "
   "compact shelving needs 150-plus psf floor capacity - verify the base building slab."),
  systems=("After-hours HVAC per office for the late-night deal; lighting scenes for focus and "
   "client meetings. Document security: shredding rooms, secure print, and access-controlled "
   "file areas."),
  spaces=[("Partner Office",12,15),("Partner Office B",12,15),("Associate Office",10,12),
   ("Secretarial Bay",24,10),("Conference Center",30,18),("Law Library",25,18),
   ("File Room",15,12),("Reception",16,12),("Pantry",10,8)],
  materials=["STC-50 partitions","Wood office fronts","Compact library shelving",
   "Conference AV","Secure file room","Stone and wood finishes","Task lighting"],
  codes=["IBC business occupancy","ASTM E90 acoustics","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-801 Interior Elevations","AV-101 Audiovisual Plan"]),
 dict(name="Medical Office", group="Medical", style="Physician Office / Clinic",
  history=("The modern medical office descends from the 19th-century doctor's surgery: waiting room, "
   "consulting room, and dispensary. The exam-room module - standardized rooms off a staff "
   "corridor - was perfected in mid-century clinics and remains the template for primary care."),
  layout=("Patient flow separates from staff flow: waiting and reception at entry, exam rooms along "
   "a patient corridor, staff workroom and provider offices behind. Procedure rooms cluster near "
   "support (lab, sterilization); checkout exits past scheduling."),
  structure=("Exam rooms need acoustic privacy (STC 45) and hand-wash sinks; procedure rooms need "
   "medical gas rough-ins and higher lighting levels. Floors take imaging equipment point loads."),
  systems=("Exam rooms on individual temperature control; medical vacuum and oxygen to procedure "
   "rooms; negative-pressure isolation where required. HIPAA drives the IT and the sight-line "
   "design together."),
  spaces=[("Waiting",20,15),("Reception",12,10),("Exam Room A",10,12),("Exam Room B",10,12),
   ("Exam Room C",10,12),("Procedure Room",14,12),("Provider Office",12,10),("Nurse Station",14,10),
   ("Lab",10,10),("Sterilization",8,8),("Checkout",10,8)],
  materials=["STC-45 exam partitions","Medical-grade flooring","Hands-free sinks",
   "Medical gas outlets","Procedure lighting","Casework with solid surfaces","Privacy glazing"],
  codes=["IBC business occupancy","FGI clinic guidelines","HIPAA privacy","ADA healthcare"],
  sheets=["A-101 Floor Plan","M-101 Medical Gas Plan","P-101 Plumbing Plan"]),
 dict(name="Dental Clinic", group="Medical", style="Dental Office",
  history=("Dental offices standardized around the operatory bay in the mid-1900s: the chair, "
   "delivery unit, and assistant's stool in a fixed triangle, repeated 4 to 8 times. Open-bay "
   "hygiene and enclosed surgical operatories split the modern clinic."),
  layout=("Operatories line the perimeter for daylight and plumbing-wall efficiency; sterilization "
   "sits central with dirty-to-clean flow; lab and pano imaging anchor one end. Reception and "
   "business office guard the entry; consult room for treatment planning."),
  structure=("Operatories need 10-by-12-foot minimum bays with chair, units, and cabinetry; "
   "plumbing walls carry water, air, vacuum, and suction to each chair. Lead-lined walls at the "
   "panoramic X-ray room."),
  systems=("Dental vacuum and compressed air are the specialty utilities - sized per chair count. "
   "Sterilization needs steam and RO water; nitrous oxide piping to sedation rooms with scavenging."),
  spaces=[("Reception/Waiting",18,14),("Operatory A",10,12),("Operatory B",10,12),("Operatory C",10,12),
   ("Hygiene Bay",20,12),("Sterilization",10,10),("Lab",10,8),("Pano Room",8,8),
   ("Consult Room",10,10),("Business Office",10,8)],
  materials=["Dental delivery units","Operatory cabinetry","Lead-lined X-ray walls",
   "Dental vacuum system","Medical air compressor","Sterilization center","Acoustic privacy panels"],
  codes=["IBC business occupancy","NCRP X-ray shielding","ADA healthcare","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","M-101 Dental Utilities","D-101 Operatory Details"]),
 dict(name="Call Center", group="Corporate", style="Contact Center",
  history=("Call centers scaled up with 1980s toll-free marketing and 1990s airline reservations. "
   "The architecture is density engineering: hundreds of agents, acoustic survival, and "
   "supervisor sight-lines - closer to a trading floor than an office."),
  layout=("Agent pods of 6 to 12 on a tight grid with low panels for sight-lines; supervisor "
   "stations elevated or at pod ends; training rooms and break areas sized for shift changes. "
   "Acoustic zoning separates inbound, outbound, and chat teams."),
  structure=("High-density fit-out: 60 to 80 square feet per agent including circulation. Raised "
   "floor or overhead cable tray for the massive data drops; panels at 42 to 48 inches balance "
   "supervision and speech privacy."),
  systems=("Ventilation for dense occupancy; sound masking tuned aggressively; redundant data and "
   "power - a call center outage is revenue lost. Shift operations need 24-hour HVAC capability."),
  spaces=[("Agent Floor",80,50),("Supervisor Row",30,8),("Training Room",24,16),("Break Room",24,16),
   ("Quiet Room",12,10),("Server/Telecom",12,10),("Reception",12,10),("Lockers",16,8)],
  materials=["Low acoustic panels","Sound masking","Raised access floor",
   "High-density data drops","24-hr HVAC","LED high-efficiency lighting","Durable carpet tile"],
  codes=["IBC business occupancy","IBC occupant load","ADA accessibility","TIA-942 telecom"],
  sheets=["A-101 Floor Plan","T-101 Technology Plan","M-101 HVAC Plan"]),
 dict(name="Government Office", group="Professional", style="Public Agency Office",
  history=("Government offices descend from 19th-century courthouses and federal buildings: the "
   "public counter, the secured back office, and records rooms built like vaults. Modern versions "
   "add the security screening vestibule and the public meeting room required by open-meeting laws."),
  layout=("Public lobby with service counters and queuing at entry; secured staff zone behind "
   "controlled doors; records vault central; public meeting room near entry for after-hours "
   "access. Elected-official suites get the perimeter."),
  structure=("Records vaults need reinforced structure for compact shelving loads; the screening "
   "vestibule needs ballistic and blast considerations per agency standard. Durable, "
   "vandal-resistant public finishes."),
  systems=("Separate public and staff HVAC zones for after-hours meetings; robust access control "
   "with audit trails; public-address and assistive listening in meeting rooms."),
  spaces=[("Public Lobby",30,20),("Service Counters",25,8),("Staff Offices",40,25),("Records Vault",20,15),
   ("Meeting Room",24,16),("Screening Vestibule",12,10),("Break Room",14,10),("Restrooms",14,10)],
  materials=["Ballistic screening glazing","Records vault door","Compact records shelving",
   "Access control system","Assistive listening","Durable public finishes","Flag and seal displays"],
  codes=["IBC business occupancy","GSA security criteria","ADA public facilities","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-701 Security Plan","E-101 Access Control Plan"]),
 dict(name="Creative Studio Office", group="Professional", style="Design Studio",
  history=("The creative studio - architects, ad agencies, software teams - rejected the corporate "
   "office in the 1960s and never looked back: warehouse lofts, pin-up walls, and the big communal "
   "table. The architecture performs creativity for clients and recruits alike."),
  layout=("Open studio floor with project tables, not assigned desks; pin-up/crit walls everywhere; "
   "model shop or maker corner; material library; client presentation room with the good light. "
   "Kitchen as social hub."),
  structure=("Loft bones preferred: high ceilings, exposed structure, big windows. Pin-up walls need "
   "continuous tackable or magnetic surfaces; the model shop needs dust collection and power."),
  systems=("Lighting tuned for color-critical work (high CRI, 5000K in review areas); robust power "
   "and data for workstations and plotters; acoustic treatment so the open floor stays workable."),
  spaces=[("Studio Floor",60,35),("Crit Wall",30,6),("Model Shop",20,15),("Material Library",15,12),
   ("Presentation Room",20,14),("Kitchen Hub",16,12),("Phone Booths",10,8),("Storage",12,10)],
  materials=["Exposed structure","Pin-up wall surfacing","Color-critical lighting",
   "Model shop dust collection","Material library shelving","Large-format plotter","Concrete floors"],
  codes=["IBC business occupancy","IECC lighting power","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-801 Interior Elevations","E-101 Lighting Plan"]),
 dict(name="Bank Branch", group="Service", style="Retail Bank Branch",
  history=("Bank branches evolved from 19th-century banking halls - marble, columns, the teller "
   "line as altar - to mid-century drive-through modernism to today's advice-centered pods. The "
   "vault remains the structural and symbolic core."),
  layout=("Teller line or pods facing entry; private offices and a conference room for lending; the "
   "vault and safe-deposit area secured at the rear; drive-through lanes on the side with pneumatic "
   "tubes or video teller. ATM vestibule accessible after hours."),
  structure=("The vault is a structure within the structure: reinforced concrete walls, floor, and "
   "ceiling with a UL-rated door. Teller counters need ballistic glazing per bank standard; "
   "drive-through canopy on its own foundations."),
  systems=("Vault ventilation and dehumidification; alarm, camera, and access systems integrated; "
   "pneumatic tube or ITM video-teller infrastructure; night-deposit with lighting and cameras."),
  spaces=[("Banking Hall",40,25),("Teller Line",25,8),("Private Offices",12,12),
   ("Conference Room",16,12),("Vault",12,12),("Safe Deposit",12,10),("Drive-Through",40,15),
   ("ATM Vestibule",10,8)],
  materials=["UL-rated vault door","Ballistic teller glazing","Pneumatic tube system",
   "Alarm and camera integration","Stone banking hall finishes","Drive-through canopy"],
  codes=["IBC business occupancy","UL 608 vault standards","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-701 Security Plan","S-101 Vault Details"]),
 dict(name="Insurance Office", group="Service", style="Insurance Agency Office",
  history=("Insurance agencies grew from 19th-century fire-insurance offices into neighborhood "
   "storefronts: the agent's desk up front, files in back. Modern agencies blend walk-in retail "
   "with back-office underwriting - part shop, part office."),
  layout=("Storefront reception with waiting; agent offices or pods for consultations; claims "
   "intake area with document scanning; secure file room; break room. Signage and visibility "
   "from the street drive the plan."),
  structure=("Standard retail-office fit-out; the file room needs fire-rated construction and "
   "possibly compact shelving capacity. Storefront glazing with security film."),
  systems=("Standard office HVAC and lighting; document scanners and secure network for policy "
   "systems; after-hours drop box with lighting and camera."),
  spaces=[("Reception",16,12),("Agent Office A",12,10),("Agent Office B",12,10),("Consult Pods",20,10),
   ("Claims Intake",14,10),("File Room",12,10),("Break Room",12,10),("Restroom",8,6)],
  materials=["Storefront glazing","Consultation pods","Fire-rated file room",
   "Document scanning station","Security film","LED lighting","Carpet tile"],
  codes=["IBC business occupancy","NFPA records protection","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-201 Storefront Elevation"]),
 dict(name="Real Estate Office", group="Service", style="Brokerage Office",
  history=("Real estate brokerages moved from downtown offices to high-visibility suburban "
   "storefronts after World War II, following the subdivisions they sold. The window display of "
   "listings - now screens - remains the architectural signature."),
  layout=("Listing display wall facing the sidewalk; agent bullpen with unassigned desks; private "
   "closing rooms for contracts; a marketing/production room for signs and flyers; broker's "
   "office overlooking the floor."),
  structure=("Retail-office fit-out with prominent storefront; closing rooms need acoustic privacy. "
   "Display wall needs power and data for digital listing screens."),
  systems=("Standard office systems; digital signage and video walls on dedicated circuits; "
   "conference-room AV for virtual tours and closings."),
  spaces=[("Listing Wall",20,6),("Agent Bullpen",40,20),("Closing Room A",12,10),("Closing Room B",12,10),
   ("Marketing Room",12,10),("Broker Office",12,10),("Reception",12,10),("Break Room",10,8)],
  materials=["Digital listing displays","Closing room AV","Agent workstations",
   "Storefront glazing","Marketing production equipment","LED lighting"],
  codes=["IBC business occupancy","ADA accessibility","NEC 2023 commercial","Local sign codes"],
  sheets=["A-101 Floor Plan","A-201 Storefront Elevation","AV-101 Audiovisual Plan"]),
]

WAREHOUSES = [
 dict(name="Distribution Center", group="Distribution", style="Regional Distribution Center",
  history=("The modern distribution center descends from railroad freight houses and Sears' great "
   "mail-order plants. The 1980s big-box DC - 500,000-plus square feet, 32-foot clear, "
   "cross-docked - became the physical internet: every online order passes through buildings "
   "like this."),
  layout=("Dock doors on two or four sides with staging lanes inside; narrow-aisle rack storage in "
   "the middle; value-added services (kitting, labeling) in a mezzanine or corner; offices at one "
   "corner near the main entry. Trailer courts sized for the door count."),
  structure=("Tilt-up concrete walls, steel frame with 50-by-50-foot bays, 32-to-40-foot clear "
   "height. Floor is the machine: 6-to-8-inch concrete, flat to tight tolerances (F-numbers) for "
   "narrow-aisle lifts. Dock levelers and seals at every door."),
  systems=("ESFR sprinklers for high-piled storage; high-bay LED with motion sensing; minimal heat "
   "(often 55F) with massive ventilation. Warehouse management systems drive the lighting and "
   "door logic."),
  spaces=[("Rack Storage",300,200),("Staging",100,40),("Shipping Office",20,15),("Value-Added",40,30),
   ("Battery Charging",20,15),("Offices",30,20),("Break Room",20,15),("Restrooms",15,12),("Dock Court",300,120)],
  materials=["Tilt-up concrete panels","Structural steel frame","ESFR sprinkler system",
   "High-bay LED fixtures","Dock levelers and seals","Wire-guided racking","Superflat concrete slab"],
  codes=["IBC storage S-1","NFPA 13 high-piled storage","FM Global data sheets","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan","FP-101 Sprinkler Plan"]),
 dict(name="Cold Storage Warehouse", group="Specialized", style="Refrigerated Warehouse",
  history=("Mechanical refrigeration warehouses date to the 1870s Chicago meatpackers; the modern "
   "frozen-food DC - minus 20 degrees Fahrenheit, 100-foot tall - is among the most energy-intense "
   "buildings on earth. Ammonia refrigeration, perfected for ice rinks and food plants, still "
   "dominates large facilities."),
  layout=("Freezer box within the building: insulated metal panel envelope, often 40-plus feet tall "
   "with automated cranes. Blast-freeze cells near receiving; tempering rooms between freezer and "
   "dock; offices and battery charging outside the envelope."),
  structure=("The envelope is the structure: insulated metal panels on steel frame with careful "
   "vapor barriers - any air leak becomes ice. Heated slabs or glycol loops under freezer floors "
   "prevent frost heave. Roof must carry refrigeration equipment."),
  systems=("Ammonia or CO2 refrigeration with engine room, leak detection, and emergency ventilation "
   "per code. LED lighting rated for minus 20F; doors are high-speed insulated with heated frames."),
  spaces=[("Freezer Storage",150,100),("Blast Freeze",40,25),("Tempering",30,20),("Dock",60,20),
   ("Engine Room",25,20),("Offices",25,15),("Battery Charging",15,12),("Restrooms",12,10)],
  materials=["Insulated metal panels","Ammonia refrigeration plant","Heated freezer slab",
   "High-speed freezer doors","Low-temp LED lighting","Vapor barrier detailing","CO2 backup"],
  codes=["IIAR ammonia standards","ASHRAE 15 refrigeration","IBC storage","OSHA PSM"],
  sheets=["A-101 Floor Plan","M-101 Refrigeration Plan","D-101 Envelope Details"]),
 dict(name="Fulfillment Warehouse", group="Distribution", style="E-Commerce Fulfillment Center",
  history=("E-commerce fulfillment centers are the 21st-century factory: the 1990s dot-com "
   "warehouses grew into million-square-foot buildings where robots and people pick millions of "
   "items a day. The architecture serves the algorithm - every aisle dimension answers to the "
   "pick path."),
  layout=("Inbound docks and decant at one end; pick modules - multi-level shelving with conveyors "
   "- in the center; pack stations and sortation at the other end; outbound docks beyond. Robotics "
   "zones (AMR floors) need ultra-flat slabs and no obstructions."),
  structure=("Clear heights of 36 to 40 feet for multi-level pick modules; 50-by-52-foot bays; "
   "floors flat to robotic tolerances. Mezzanines are structural steel with their own egress and "
   "sprinkler protection."),
  systems=("Miles of conveyor and sortation with distributed controls; AMR fleet charging; "
   "fire protection for multi-level modules (in-rack sprinklers); data infrastructure as "
   "critical as power."),
  spaces=[("Pick Modules",200,120),("Decant",60,30),("Pack Stations",80,30),("Sortation",60,40),
   ("Robotics Zone",80,60),("Outbound Staging",60,30),("Offices",30,20),("Break Room",25,18)],
  materials=["Multi-level pick modules","Conveyor and sortation","AMR robotics floor",
   "In-rack sprinklers","High-bay LED","Structural mezzanines","WMS integration"],
  codes=["IBC storage S-1","NFPA 13 in-rack protection","IBC mezzanines","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","M-101 Conveyor Plan","FP-101 Sprinkler Plan"]),
 dict(name="Bulk Storage Shed", group="Storage", style="Bulk Commodity Shed",
  history=("Bulk storage sheds - for salt, sand, grain, fertilizer - descend from 19th-century "
   "railroad commodity houses. The modern version is a clear-span arch or rigid frame with a "
   "push wall: front loaders work inside against concrete walls while the roof keeps weather off."),
  layout=("One big clear volume with push walls (concrete, 8 to 12 feet tall) around the perimeter; "
   "loader doors at the gable ends; a small office and scale house at the entry. Drainage keeps "
   "the commodity dry."),
  structure=("Clear-span rigid frame or arch to 100-plus feet - no interior columns for loaders to "
   "hit. Push walls designed for lateral commodity pressure (like a retaining wall). Ventilation "
   "along the ridge for dust and fumes."),
  systems=("Dust control and explosion venting where the commodity requires it; minimal heat; "
   "truck scale with office. Fire protection per commodity hazard classification."),
  spaces=[("Storage Volume",120,80),("Push Walls",120,4),("Office",12,10),("Scale House",10,8),
   ("Equipment Bay",20,15)],
  materials=["Clear-span rigid frame","Concrete push walls","Corrugated metal cladding",
   "Truck scale","Ridge ventilation","Dust collection (as required)","Gravel apron"],
  codes=["IBC storage S-1/S-2","NFPA combustible dust","IBC retaining walls","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan","C-101 Grading Plan"]),
 dict(name="Cross-Dock Terminal", group="Distribution", style="Cross-Dock Freight Terminal",
  history=("Cross-docking - freight moves from inbound trailer to outbound trailer without "
   "storage - was perfected by 1980s LTL carriers and retailers like Walmart. The building is a "
   "long, narrow machine: doors on both long sides, freight flowing straight through."),
  layout=("Doors on both long sides (often 100-plus total) with a narrow 60-to-80-foot building "
   "depth; powered conveyor or forklift lanes run the length; small offices at one end. The "
   "apron needs full tractor-trailer circulation on both sides."),
  structure=("Light steel frame with minimal interior columns; dock height 48 to 52 inches with "
   "levelers; canopy or seals at every door. Pavement design carries constant truck traffic."),
  systems=("Dock equipment power and controls; yard management systems; high-mast yard lighting; "
   "minimal heating - the building is a covered work platform."),
  spaces=[("Dock Floor",300,70),("Offices",25,15),("Driver Lounge",15,12),("Maintenance",20,15),
   ("West Apron",300,120),("East Apron",300,120)],
  materials=["Light steel frame","Dock levelers","Dock seals and shelters",
   "High-mast yard lighting","Heavy-duty pavement","Metal panel walls"],
  codes=["IBC storage S-1","IBC egress Chapter 10","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","C-101 Paving Plan","E-101 Yard Lighting"]),
 dict(name="Self-Storage Facility", group="Storage", style="Self-Storage",
  history=("Modern self-storage was born in 1960s Texas - the first facilities in Odessa and "
   "Midland - and grew into a 50,000-facility American industry. The architecture is a matrix of "
   "roll-up doors: unit mix engineering (more small units, fewer large) drives the plan."),
  layout=("Single-story drive-up buildings with exterior unit doors, or multi-story with interior "
   "corridors and freight elevators; climate-controlled units in the conditioned core; office and "
   "retail (boxes, locks) at the entry; wide drive aisles for truck maneuvering."),
  structure=("Light steel or wood frame with corrugated partitions between units; multi-story "
   "versions use steel or concrete frame. Unit doors are the facade - hundreds of roll-ups on a "
   "planning module."),
  systems=("Climate-controlled buildings need full HVAC and insulation; drive-up buildings are "
   "unconditioned. Gate access control, cameras, and individual door alarms are the security "
   "system."),
  spaces=[("Unit Block A",100,25),("Unit Block B",100,25),("Climate Building",80,40),
   ("Office/Retail",15,12),("Freight Elevator",8,8),("Drive Aisles",200,25)],
  materials=["Roll-up unit doors","Corrugated partitions","Access gate system",
   "Camera network","Climate HVAC","LED corridor lighting","Asphalt drive aisles"],
  codes=["IBC storage S-1","IBC egress Chapter 10","ADA units","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-201 Elevations","E-101 Security Plan"]),
 dict(name="Hazmat Warehouse", group="Specialized", style="Hazardous Materials Storage",
  history=("Dedicated hazmat warehouses grew from 1970s environmental law - RCRA, SARA, and the "
   "fire codes' hazardous materials chapters. The building is containment engineering: every "
   "detail assumes a spill, a fire, or both."),
  layout=("Segregated storage rooms by hazard class with 2-hour separations; spill containment "
   "curbs and sloped floors to sumps in every room; separate receiving with its own containment; "
   "control room and emergency equipment at the entry."),
  structure=("Noncombustible construction; floors sloped to contained sumps; explosion venting "
   "panels where required. Secondary containment sized for the largest vessel plus fire water."),
  systems=("Hazard-class ventilation (explosion-proof where required); gas detection; foam or "
   "special suppression per commodity; emergency eyewash and showers; lightning protection."),
  spaces=[("Flammables Room",40,25),("Corrosives Room",30,20),("Oxidizers Room",25,18),
   ("General Hazmat",40,25),("Receiving",25,18),("Control Room",12,10),("Emergency Equip",10,8)],
  materials=["2-hr fire separations","Spill containment curbs","Explosion-proof electrical",
   "Gas detection system","Foam suppression","Acid-resistant flooring","Emergency ventilation"],
  codes=["IFC hazardous materials","NFPA 30/400","EPA SPCC","OSHA PSM"],
  sheets=["A-101 Floor Plan","FP-101 Suppression Plan","D-101 Containment Details"]),
 dict(name="Grain Silo Complex", group="Storage", style="Grain Elevator and Silos",
  history=("Grain elevators - the prairie sentinels - were revolutionized by Joseph Dart's 1842 "
   "Buffalo steam elevator. Concrete slip-formed silos replaced timber cribs in the early 1900s; "
   "modern complexes pair battery silos with a headhouse containing the legs, distributors, and "
   "dryers."),
  layout=("Silo batteries in rows (each 20 to 30 feet diameter, 80 to 120 feet tall); headhouse at "
   "one end with receiving pits, legs, and distributor; dryer and loadout at the rail or truck "
   "side; office and scale near entry."),
  structure=("Slip-formed reinforced concrete silos - continuous pour, no joints; headhouse of "
   "concrete or steel. Foundations carry enormous concentrated loads; grain pressure designs the "
   "walls (Janssen's formula country)."),
  systems=("Dust explosion protection dominates: venting, suppression, and housekeeping per NFPA "
   "61. Aeration floors in silos; grain monitoring (temperature cables); dryer heat with fire "
   "safeguards."),
  spaces=[("Silo Battery",120,60),("Headhouse",30,25),("Receiving Pit",20,12),("Dryer Building",25,20),
   ("Loadout",30,15),("Office",12,10),("Scale",10,30)],
  materials=["Slip-formed concrete silos","Bucket elevator legs","Grain distributor",
   "Aeration flooring","Dust explosion venting","Temperature monitoring","Truck/rail loadout"],
  codes=["NFPA 61 grain facilities","NFPA 68 explosion venting","IBC storage","OSHA grain handling"],
  sheets=["A-101 Site Plan","S-101 Silo Sections","M-101 Dust Control Plan"]),
 dict(name="Light Manufacturing Warehouse", group="Distribution", style="Flex / Light Industrial",
  history=("Flex buildings - part office, part warehouse, divisible into small bays - were the "
   "1980s answer to small manufacturers and contractors who needed both a showroom and a shop. "
   "The 20-to-30-foot bay with its own dock door and office front became the small-business "
   "workhorse."),
  layout=("Divisible bays, each with office/showroom at the front, shop in the middle, and dock or "
   "drive-in door at the rear; demising walls relocate as tenants change. Shared truck court "
   "serves all bays."),
  structure=("Steel frame with 24-to-30-foot bays; 16-to-20-foot clear height; dock-high and "
   "drive-in doors mixed. Office fronts get storefront glazing; shops get the structure."),
  systems=("Each bay separately metered for power (often 400-plus amps for shops); unit heaters or "
   "packaged rooftop per bay; compressed air and welding ventilation rough-ins in shop zones."),
  spaces=[("Bay A Office",25,20),("Bay A Shop",40,30),("Bay B Office",25,20),("Bay B Shop",40,30),
   ("Bay C Office",25,20),("Bay C Shop",40,30),("Truck Court",150,60)],
  materials=["Steel frame","Demising partitions","Storefront office fronts",
   "400A electrical services","Unit heaters","Compressed air piping","Dock and drive-in doors"],
  codes=["IBC factory F-1/business","NFPA 13","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","E-101 Power Plan"]),
 dict(name="Records Archive Warehouse", group="Specialized", style="High-Density Records Archive",
  history=("Records archives - for paper that must survive decades - descend from 19th-century "
   "registry offices. Modern versions are windowless boxes with mobile shelving at 90 percent "
   "space efficiency, FM-200 or water-mist protection, and climate held tight for preservation."),
  layout=("High-bay mobile shelving ranges with a single moving aisle; intake/processing room for "
   "boxing and barcoding; small office and reading room near entry; the whole storage volume "
   "conditioned as one zone."),
  structure=("Floors designed for 300-plus psf under compact shelving; windowless insulated envelope; "
   "roof hardened against leaks (the enemy of paper). Raised floor or sealed slab against moisture."),
  systems=("Tight climate control: 65-68F, 30-40 percent RH with N+1 redundancy; very-early-warning "
   "smoke detection (VESDA); clean-agent or mist suppression; pest management detailing."),
  spaces=[("Compact Shelving",100,60),("Intake/Processing",30,20),("Office",15,12),
   ("Reading Room",15,12),("Mechanical",20,15)],
  materials=["Mobile compact shelving","VESDA detection","Clean-agent suppression",
   "Redundant HVAC","Vapor-sealed envelope","Barcoding system","Pest-proof detailing"],
  codes=["NFPA records protection","NARA storage standards","IBC storage S-1","ASHRAE preservation"],
  sheets=["A-101 Floor Plan","M-101 Climate Plan","FP-101 Suppression Plan"]),
 dict(name="Retail Back-Stock Warehouse", group="Storage", style="Store Support Warehouse",
  history=("Every big-box store hides a back-stock warehouse behind the sales floor - the "
   "replenishment engine that keeps shelves full. Modern versions are flow-through: receiving on "
   "one side, the sales floor on the other, with forward-pick locations sized to the store's "
   "velocity."),
  layout=("Receiving docks at the rear; bulk reserve storage above and behind; forward-pick aisles "
   "feeding directly to the sales floor through stockroom doors; compactor and baler area for "
   "cardboard; manager's office overlooking receiving."),
  structure=("Same bones as the store: steel frame, 24-foot clear, shared roof. The stockroom needs "
   "the same flat slab as the sales floor for pallet jacks; mezzanine for seasonal overflow."),
  systems=("Shared building HVAC with stockroom ventilation; compactor power and hydraulics; "
   "security separation between public sales and the stockroom (alarmed doors, cameras)."),
  spaces=[("Reserve Storage",80,50),("Forward Pick",60,20),("Receiving",40,20),("Compactor Area",20,15),
   ("Manager Office",12,10),("Seasonal Mezzanine",60,20)],
  materials=["Steel frame","Pallet racking","Dock levelers","Cardboard baler",
   "Security doors and cameras","Shared rooftop HVAC","Mezzanine deck"],
  codes=["IBC storage S-1","NFPA 13","IBC egress Chapter 10","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan"]),
 dict(name="Intermodal Yard Office", group="Distribution", style="Container Yard Operations Building",
  history=("Intermodal yards - where containers jump between ship, rail, and truck - grew with "
   "containerization after Malcom McLean's 1956 maiden voyage. The operations building is the "
   "yard's brain: gate, dispatch, and driver services overlooking acres of stacked boxes."),
  layout=("Gate canopy with inspection lanes and kiosks; operations floor with dispatch overlooking "
   "the yard; driver lounge with restrooms and vending; maintenance shop for chassis and reefers; "
   "fuel island and wash rack at the yard edge."),
  structure=("Operations building: conventional steel frame with full-height glazing toward the "
   "yard. Gate canopy: long-span steel on columns clear of truck lanes; foundations for kiosk "
   "equipment and barriers."),
  systems=("Gate operating system with OCR portals; yard lighting on high masts; reefer racks with "
   "480V power for refrigerated containers; fuel and wash-water reclaim systems."),
  spaces=[("Operations Floor",40,25),("Gate Canopy",100,30),("Driver Lounge",20,15),
   ("Maintenance Shop",40,25),("Fuel Island",30,15),("Reefer Racks",60,20)],
  materials=["Gate OCR portals","High-mast yard lighting","Reefer power racks",
   "Operations glazing","Fuel island","Wash-water reclaim","Heavy pavement"],
  codes=["IBC business/storage","IFC fuel dispensing","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","C-101 Yard Plan","E-101 Yard Lighting"]),
]

APARTMENTS = [
 dict(name="Studio Apartment", group="Studio / 1BR", style="Studio Unit",
  history=("The studio apartment descends from 19th-century Parisian artist ateliers - one big "
   "room for living and working. Postwar American versions shrank it into the efficiency: "
   "kitchenette along one wall, sleeping alcove, and a bath. Good studios borrow space with "
   "glass, mirrors, and built-ins."),
  layout=("Single open room zoned by furniture: sleeping area near the window, living zone central, "
   "kitchenette along the entry wall. Bath and closet buffer the corridor. Every inch is planned - "
   "there is no hallway to waste."),
  structure=("Part of a larger multifamily frame: studios stack in the building's structural grid. "
   "Demising walls rated per code; the unit needs no interior bearing - partitions are light."),
  systems=("Individual heat pump or PTAC; 100-amp panel; bath exhaust on timer. Acoustic separation "
   "from neighbors matters most in small units - every sound is close."),
  spaces=[("Living/Sleeping",18,14),("Kitchenette",10,8),("Bath",8,6),("Closet",6,4),("Entry",5,5)],
  materials=["Space-saving built-ins","Murphy or platform bed zone","Kitchenette appliances",
   "PTAC or mini-split","Acoustic demising walls","LVT flooring","LED lighting"],
  codes=["IBC residential R-2","IRC/IBC dwelling unit","ADA Type B units","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","A-801 Interior Elevations"]),
 dict(name="One-Bedroom Apartment", group="Studio / 1BR", style="One-Bedroom Unit",
  history=("The one-bedroom is the workhorse of rental housing: a real bedroom with a door, a "
   "living room that can host, and a kitchen that can cook. The postwar garden-apartment boom "
   "standardized it, and the dimensions have barely changed in 70 years because they work."),
  layout=("Entry into living room; kitchen adjacent (galley or L); bedroom wing with bath and "
   "closets; balcony or patio off the living room. The bedroom door is the whole point - "
   "separation of rest from living."),
  structure=("Stacked in wood, steel, or concrete multifamily construction; demising walls and "
   "floor-ceiling assemblies rated for fire and sound. Balconies need waterproofing and "
   "thermal-break detailing."),
  systems=("Individual HVAC per unit for submetering; plumbing stacked vertically to serve kitchens "
   "and baths in line. Balcony doors and windows sized for egress where required."),
  spaces=[("Living Room",14,12),("Kitchen",10,9),("Bedroom",12,11),("Bath",8,6),
   ("Closet",6,5),("Balcony",10,6),("Entry",5,6)],
  materials=["Demising wall assemblies","Mini-split or PTAC","Kitchen appliance package",
   "Balcony waterproofing","Acoustic floor underlayment","LVT or carpet","LED lighting"],
  codes=["IBC residential R-2","IBC sound transmission","ADA Type B units","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","A-801 Interior Elevations"]),
 dict(name="Two-Bedroom Apartment", group="2BR", style="Two-Bedroom Unit",
  history=("The two-bedroom serves roommates, small families, and home offices - the most flexible "
   "unit in the building. Split-bedroom plans (primary one side, second bedroom the other) became "
   "popular in the 1990s for roommate privacy."),
  layout=("Living, dining, and kitchen share an open core; primary suite on one side with full bath "
   "and walk-in closet; second bedroom and hall bath on the other (split plan) or adjacent. "
   "In-unit laundry near the bedrooms."),
  structure=("Same multifamily systems as smaller units; the larger span may need an interior bearing "
   "line or deeper joists. Split plans need longer corridor or careful adjacency planning."),
  systems=("Larger units may need two HVAC heads or a ducted mini-split; in-unit washer/dryer needs "
   "drain pans and shutoffs. Two baths stack over the unit below."),
  spaces=[("Living/Dining",18,14),("Kitchen",11,10),("Primary Bedroom",13,12),("Primary Bath",9,7),
   ("Bedroom 2",11,10),("Hall Bath",8,6),("Laundry",6,6),("Balcony",12,6)],
  materials=["Ducted mini-split","In-unit laundry","Walk-in closet systems",
   "Demising assemblies","Balcony waterproofing","Quartz counters","LED lighting"],
  codes=["IBC residential R-2","IBC sound transmission","ADA Type B units","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","A-801 Interior Elevations"]),
 dict(name="Three-Bedroom Apartment", group="3BR+", style="Three-Bedroom Unit",
  history=("Three-bedroom apartments house growing families in the city - the urban alternative to "
   "the suburban house. Many cities now require family-sized units in new developments, reversing "
   "decades of studio-heavy construction."),
  layout=("Generous living core; primary suite with bath; two secondary bedrooms sharing a hall "
   "bath; kitchen sized for real cooking; dining that fits a full table. Storage - the family "
   "unit's scarcest resource - gets dedicated closets."),
  structure=("Larger units often sit at building corners or ends where spans allow; corridors serve "
   "fewer doors. Structure identical to smaller units, just more of it."),
  systems=("Two-zone HVAC common; double vanity and extra bath exhaust; in-unit laundry standard. "
   "Sound control between bedrooms matters with kids."),
  spaces=[("Living/Dining",20,15),("Kitchen",12,10),("Primary Bedroom",14,12),("Primary Bath",9,7),
   ("Bedroom 2",11,10),("Bedroom 3",11,10),("Hall Bath",8,6),("Laundry",6,6),("Storage",6,8)],
  materials=["Two-zone HVAC","Double-vanity baths","In-unit laundry",
   "Generous closet systems","Demising assemblies","Durable flooring","LED lighting"],
  codes=["IBC residential R-2","Family-unit requirements (local)","ADA Type B units","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","A-801 Interior Elevations"]),
 dict(name="Garden Apartment", group="2BR", style="Garden Apartment Unit",
  history=("Garden apartments - two or three stories around landscaped courtyards - were the 1940s "
   "to 1960s answer to humane density: no elevators, every unit with a patio or balcony, parking "
   "at the edges. Radburn, New Jersey (1929) pioneered the superblock idea behind them."),
  layout=("Ground-floor units open directly to patios and gardens; upper units get balconies and "
   "stair access. Buildings angle for sun and privacy; parking sits in courts, not in front of "
   "doors. The landscape is part of the floor plan."),
  structure=("Wood-frame walk-ups: simple, economical, and easy to maintain. Stairs are exterior or "
   "in open breezeways; no elevators means strict height limits (usually 3 stories)."),
  systems=("Individual HVAC per unit; simple plumbing stacks; site lighting and landscape irrigation "
   "are building systems. Breezeway stairs need weather protection and lighting."),
  spaces=[("Living Room",15,13),("Kitchen",11,9),("Bedroom 1",12,11),("Bedroom 2",11,10),
   ("Bath",8,6),("Patio",12,10),("Storage",6,5)],
  materials=["Wood-frame construction","Patio slabs","Breezeway stairs",
   "Individual HVAC","Landscape irrigation","Site lighting","Wood or fiber-cement siding"],
  codes=["IBC residential R-2","IBC exterior stairs","ADA site accessibility","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","L-101 Landscape Plan"]),
 dict(name="Loft Apartment", group="Specialty", style="Industrial Loft Conversion",
  history=("Loft living began illegally in 1960s SoHo, where artists occupied cast-iron warehouses. "
   "Cities legalized it in the 1970s-80s (New York's Loft Law, 1982), and developers learned to "
   "build new 'lofts' with the old DNA: high ceilings, big windows, open floors."),
  layout=("One big open volume: sleeping zone screened by partial walls or mezzanine; kitchen along "
   "one wall; bath core central. The windows are the architecture - furniture stays low to keep "
   "sight-lines open."),
  structure=("In conversions, the existing heavy timber or concrete frame is the structure - new "
   "work is all fit-out. Mezzanines need their own structure and egress; the open floor needs no "
   "interior bearing."),
  systems=("High volumes need zoned HVAC or ceiling fans with heat pumps; the big windows need "
   "shading and low-E retrofit. Sprinklers and fire separation bring old warehouses to code."),
  spaces=[("Open Living",30,22),("Kitchen Wall",16,8),("Sleeping Zone",14,12),("Bath Core",10,8),
   ("Mezzanine",16,12),("Entry",8,8)],
  materials=["Existing heavy timber/concrete","Mezzanine steel","Industrial windows",
   "Polished concrete floors","Exposed ductwork","Track lighting","Freestanding kitchen"],
  codes=["IBC change of occupancy","Loft Law (local)","IBC mezzanines","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","A-301 Sections"]),
 dict(name="Penthouse", group="Specialty", style="Penthouse Unit",
  history=("Penthouses were born on 1920s New York rooftops - setback towers created terraces, and "
   "the wealthy claimed the top. The modern penthouse is a house in the sky: private elevator "
   "landing, wraparound terrace, and services no lower floor gets."),
  layout=("Private elevator vestibule; great room with 10-plus-foot ceilings opening to terraces on "
   "two or three sides; primary suite wing; guest suites; catering kitchen plus show kitchen. "
   "Outdoor rooms - kitchen, fireplace, spa - extend the living area."),
  structure=("Top-floor unit in a high-rise frame; terraces need structural capacity for planters, "
   "spas, and outdoor kitchens (saturated soil is heavy). Wind and waterproofing details are "
   "critical at the roof."),
  systems=("Dedicated high-capacity HVAC; smart-home infrastructure; private elevator control; "
   "terrace gas, water, and drainage. Redundant systems - penthouse buyers expect no outages."),
  spaces=[("Great Room",28,20),("Show Kitchen",16,12),("Catering Kitchen",12,10),("Primary Suite",18,14),
   ("Guest Suite",14,12),("Guest Suite 2",13,11),("Terrace",40,20),("Elevator Vestibule",10,8)],
  materials=["Private elevator","Terrace outdoor kitchen","Spa and planters",
   "Smart-home system","Stone and hardwood finishes","10-ft glazing","Redundant HVAC"],
  codes=["IBC residential R-2 high-rise","IBC terrace guards","ADA Type B units","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","A-301 Terrace Details"]),
 dict(name="Micro-Apartment", group="Studio / 1BR", style="Micro-Unit",
  history=("Micro-apartments - 250 to 400 square feet - revived the 19th-century boarding house for "
   "the 21st-century city. After New York's 2013 adAPT competition proved the market, cities "
   "rewrote minimum-size rules. The design secret: shared amenity spaces replace private rooms."),
  layout=("Transformable core: bed that folds or slides, table that expands, kitchenette compressed "
   "to one wall. The bath is a wet-room pod. Generous windows and 9-foot ceilings keep the small "
   "plan from feeling small; building lounges and roof decks supply the missing living room."),
  structure=("Standard multifamily construction; the innovation is all in the fit-out - "
   "prefabricated bath pods and transformable millwork installed like furniture."),
  systems=("Individual mini-split; bath pod with integrated exhaust; building amenity spaces carry "
   "the social load. Storage cages in the basement supplement the tiny closets."),
  spaces=[("Transformable Room",16,13),("Kitchenette",8,6),("Bath Pod",7,6),("Entry",4,5)],
  materials=["Transformable millwork","Prefab bath pod","Fold-down bed system",
   "Mini-split HVAC","Tall windows","Amenity-level finishes","Bike storage"],
  codes=["IBC residential R-2","Local minimum-size rules","ADA Type B units","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","D-101 Millwork Details"]),
 dict(name="Senior Living Unit", group="Specialty", style="Independent Senior Living",
  history=("Senior housing evolved from 19th-century almshouses to today's continuum of care. The "
   "independent-living apartment - fully accessible, service-connected, community-rich - became the "
   "standard in the 1980s as the industry professionalized around aging in place."),
  layout=("Single-level, step-free throughout: wide doors and halls, roll-in shower, kitchen with "
   "seated work zones, emergency call in bath and bedroom. Units cluster near dining, activity, "
   "and wellness rooms - the community spaces are the point."),
  structure=("Standard multifamily; accessibility is the structure of the plan - turning circles, "
   "grab-bar blocking in every bath wall, lever hardware everywhere. No thresholds anywhere."),
  systems=("Emergency call system in every unit; wander-management at entries; commercial kitchen "
   "serving the dining room; higher lighting levels for aging eyes."),
  spaces=[("Living Room",14,12),("Kitchen",10,9),("Bedroom",12,11),("Roll-in Bath",9,7),
   ("Entry",6,6),("Dining Hall",40,25),("Activity Room",25,18)],
  materials=["Grab-bar blocking","Roll-in shower","Lever hardware",
   "Emergency call system","Non-slip flooring","Higher lighting levels","Step-free thresholds"],
  codes=["IBC residential R-2","ADA/FHA accessibility","NFPA 101 residential board","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","A-701 Accessibility Details"]),
 dict(name="Student Housing Unit", group="Specialty", style="Student Apartment",
  history=("Purpose-built student housing - the bed-bath parity suite - replaced dormitories near "
   "growing universities in the 2000s. Each resident gets a private bedroom and bath with shared "
   "living/kitchen: the floor plan of roommate harmony."),
  layout=("Four private bedroom-bath suites lock off a shared living-kitchen core; each bedroom has "
   "its own bath (no sharing, no fights). Study lounges, fitness, and courtyard amenities fill the "
   "building; leasing office at entry."),
  structure=("Wood or steel-frame mid-rise; the repeated suite module makes construction efficient. "
   "Bedroom demising walls rated for privacy; robust finishes for student wear."),
  systems=("Individual bedroom HVAC control (roommates disagree); high-density Wi-Fi; access control "
   "per bedroom; amenity spaces with extended hours."),
  spaces=[("Suite A Bed/Bath",12,11),("Suite B Bed/Bath",12,11),("Suite C Bed/Bath",12,11),
   ("Suite D Bed/Bath",12,11),("Shared Living",16,13),("Shared Kitchen",12,10),("Study Lounge",20,14)],
  materials=["Bed-bath suite modules","Individual HVAC controls","High-density Wi-Fi",
   "Per-bedroom access control","Durable finishes","Study lounge furnishings"],
  codes=["IBC residential R-2","IBC occupant load","ADA Type B units","NEC 2023 dwelling"],
  sheets=["A-101 Unit Plan","T-101 Technology Plan"]),
 dict(name="Duplex Apartment", group="2BR", style="Stacked Duplex Unit",
  history=("The stacked duplex - one unit over another in a two-family house - is the classic "
   "owner-occupant investment from streetcar suburbs. Each unit lives like a small house with its "
   "own entry, porch, and yard rights."),
  layout=("Two full floors, one unit each: entry porches front and rear, living-kitchen open core, "
   "two or three bedrooms, full bath. Basement shared for laundry, storage, and mechanicals."),
  structure=("Wood frame two-family; the floor between units needs fire and sound separation "
   "(1-hour, STC 50). Separate entries mean separate stairs or a shared vestibule with rated "
   "separation."),
  systems=("Separate HVAC, electrical, and water heating per unit for clean cost-splitting; shared "
   "sewer and water service with sub-metering where required."),
  spaces=[("Unit 1 Living",15,13),("Unit 1 Kitchen",11,9),("Unit 1 Bed 1",12,11),("Unit 1 Bed 2",11,10),
   ("Unit 1 Bath",8,6),("Unit 2 Living",15,13),("Unit 2 Kitchen",11,9),("Unit 2 Bed 1",12,11),
   ("Unit 2 Bed 2",11,10),("Unit 2 Bath",8,6),("Shared Basement",30,20)],
  materials=["1-hr floor separation","Separate utility services","Two entry porches",
   "Individual HVAC per unit","Sound-rated assembly","Wood frame construction"],
  codes=["IRC/IBC two-family","R302 fire separation","NEC two services","IECC energy code"],
  sheets=["A-101 First Floor Plan","A-102 Second Floor Plan"]),
 dict(name="Courtyard Apartment Block", group="3BR+", style="Courtyard Housing Block",
  history=("Courtyard housing - apartments wrapped around a shared garden court - descends from "
   "European perimeter blocks and was perfected in 1920s Vienna (the Karl-Marx-Hof) and Los "
   "Angeles courtyard apartments. The court gives every unit light, air, and a front door onto "
   "green."),
  layout=("Units line all four sides of a landscaped court; entries face the court, not the street. "
   "Ground units get patios; upper units get balconies overlooking the green. Parking tucks under "
   "or behind, never in the court."),
  structure=("Wood-frame walk-ups or elevator mid-rise around the court; the court itself needs "
   "drainage, lighting, and landscape structure. Bridges or breezeways connect wings."),
  systems=("Individual unit HVAC; court lighting and irrigation on building systems; stormwater "
   "managed in the court landscape. Security: the court is defensible space with controlled "
   "entries."),
  spaces=[("Court Garden",60,40),("Unit A Living",15,13),("Unit A Kitchen",11,9),("Unit A Beds",24,11),
   ("Unit B Living",15,13),("Unit B Kitchen",11,9),("Unit B Beds",24,11),("Breezeway",20,8)],
  materials=["Courtyard landscape","Patio and balcony slabs","Breezeway construction",
   "Court lighting","Irrigation system","Wood-frame units","Controlled entries"],
  codes=["IBC residential R-2","IBC courtyard provisions","ADA site accessibility","NEC 2023 dwelling"],
  sheets=["A-101 Site Plan","L-101 Landscape Plan"]),
]

BARNS = [
 dict(name="Dairy Barn", group="Livestock", style="Dairy Stanchion Barn",
  history=("Dairy barns standardized in the late 1800s around the stanchion: rows of cows facing a "
   "central feed alley, milked twice daily. The 20th-century milking parlor moved milking out of "
   "the barn, but the bank-barn dairy with its haymow above remains the iconic form."),
  layout=("Central drive/feed alley with stanchion rows on both sides; milk house attached at one "
   "end (separate, sanitary); haymow above for feed storage; calf pens and maternity area at the "
   "far end. Manure handling at the rear - gutter cleaners to spreader."),
  structure=("Timber frame or pole construction with gambrel or gable roof for maximum haymow volume. "
   "Concrete floors with gutters sloped to manure handling; walls washable to 4 feet."),
  systems=("Ventilation is critical: ridge vents plus eave inlets, or mechanical tunnel ventilation. "
   "Milk house needs hot water, cooling, and sanitary drains; barn wiring is dust- and "
   "moisture-rated."),
  spaces=[("Stanchion Rows",80,30),("Feed Alley",80,10),("Milk House",20,15),("Haymow",80,30),
   ("Calf Pens",25,20),("Maternity",20,15),("Office",10,8)],
  materials=["Timber frame bents","Gambrel roof","Concrete floors with gutters",
   "Milk house stainless","Ridge ventilation","Washable wall panels","Manure gutter cleaner"],
  codes=["IBC utility/agricultural","FDA milk sanitation","NEC agricultural buildings","Local ag setbacks"],
  sheets=["A-101 Floor Plan","A-201 Elevations","S-101 Framing Plan"]),
 dict(name="Horse Stable", group="Livestock", style="Horse Barn",
  history=("Horse barns evolved from 18th-century carriage houses into the center-aisle stable: box "
   "stalls on both sides, tack room, and wash rack. The monitor or raised-center-aisle roof - "
   "clerestory windows over the aisle - is the classic horse-barn signature, venting heat and "
   "bringing light."),
  layout=("Center aisle 12 to 14 feet wide with 10x10 or 12x12 box stalls each side; tack room near "
   "entry; wash/grooming bay with hot water; feed room rodent-proofed; hay storage above or in a "
   "separate bay. Office with arena view in show barns."),
  structure=("Pole or timber frame; monitor roof for ventilation and light. Stall fronts of hardwood "
   "or steel mesh over wood; aisle floors of pavers or sealed concrete with drainage."),
  systems=("Dust control is the system: ventilation sized for ammonia and dust, no exposed "
   "insulation horses can chew, and fire separation for hay storage. Wash racks need hot water and "
   "drainage."),
  spaces=[("Center Aisle",80,14),("Box Stalls",80,24),("Tack Room",12,12),("Wash Bay",12,10),
   ("Feed Room",10,10),("Hay Storage",25,20),("Office",10,10)],
  materials=["Box stall fronts","Monitor roof glazing","Paver aisle floor",
   "Rodent-proof feed bins","Wash bay heater","Fire-rated hay separation","Dutch doors"],
  codes=["IBC utility/agricultural","NFPA 150 fire safety","NEC agricultural buildings","Local ag setbacks"],
  sheets=["A-101 Floor Plan","A-201 Elevations","D-101 Stall Details"]),
 dict(name="Hay Barn", group="Crop Storage", style="Hay Storage Barn",
  history=("Hay barns exist to keep the winter feed dry: the Pennsylvania Dutch bank barn stored hay "
   "in the great mow above the threshing floor. Modern hay barns are clear-span sheds - maximum "
   "volume, minimum structure - sized to the baler and the wagon."),
  layout=("One clear volume with big doors at both gable ends for drive-through loading; hay stacked "
   "in bays; a small equipment corner. Ventilation gaps at the eaves keep condensation off the hay."),
  structure=("Pole barn or rigid frame clear-span to 60-plus feet; metal cladding; roof vented at "
   "ridge. Floors of gravel or concrete - hay needs air under the bottom bales."),
  systems=("Minimal: natural ventilation, no heat, basic lighting. Fire separation from other farm "
   "buildings - hay fires are the classic farm disaster."),
  spaces=[("Hay Storage",60,40),("Equipment Corner",20,15),("Drive Aisle",60,12)],
  materials=["Pole or rigid frame","Metal roof and siding","Ridge vent",
   "Gravel floor","Big sliding doors","Lightning protection"],
  codes=["IBC utility/agricultural","NFPA hay storage","NEC agricultural buildings","Local ag setbacks"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan"]),
 dict(name="Tobacco Barn", group="Crop Storage", style="Air-Cure Tobacco Barn",
  history=("Tobacco barns are curing machines: tall, narrow, with adjustable siding vents. Kentucky "
   "and Tennessee air-cure barns hang burley tobacco on tiered rails for 6 to 8 weeks while vents "
   "modulate humidity. The form - tall gable, vented sides - is pure function."),
  layout=("Open interior with tier poles at 4-foot vertical spacing; hanging rails span bent to bent; "
   "drive floor for wagons; stripping room at one end for grading after cure."),
  structure=("Tall timber bents, 3 to 4 tiers high; siding of vertical boards on hinges or sliders "
   "for vent adjustment. The tall narrow form sheds wind and stacks heat for curing."),
  systems=("No mechanical systems historically - the vents are the system. Modern barns add fans for "
   "still-air nights and humidity monitoring."),
  spaces=[("Curing Tiers",40,24),("Drive Floor",40,12),("Stripping Room",20,15)],
  materials=["Timber bents","Hinged vent siding","Tier poles and rails",
   "Tall gable roof","Humidity monitors","Drive-through doors"],
  codes=["IBC utility/agricultural","NEC agricultural buildings","Local ag setbacks"],
  sheets=["A-101 Floor Plan","A-301 Sections"]),
 dict(name="Bank Barn", group="Livestock", style="Pennsylvania Bank Barn",
  history=("The Pennsylvania bank barn - built into a hillside so wagons drive into the upper mow "
   "while stock enters below - is the great American barn form, brought by German settlers in the "
   "1700s. The forebay overhang on the eave side is its signature."),
  layout=("Upper level: threshing floor and haymow with wagon access from the bank; lower level: "
   "stables and pens with the forebay sheltering the stock doors. Stone ramp or earthen bank "
   "serves the upper door."),
  structure=("Massive timber frame with forebay cantilever; stone lower walls, timber upper. The "
   "bank itself retains the hillside - drainage behind the wall is the critical detail."),
  systems=("Gravity does the work: hay drops from mow to stock below. Ventilation via the forebay "
   "and gable vents; modern versions add water and electric to both levels."),
  spaces=[("Threshing Floor",50,30),("Haymow",50,20),("Stable Level",50,30),("Forebay",50,10)],
  materials=["Heavy timber frame","Stone lower walls","Forebay cantilever",
   "Bank ramp","Wood threshing floor","Gable vents","Slate or metal roof"],
  codes=["IBC utility/agricultural","Historic preservation (where listed)","NEC agricultural buildings"],
  sheets=["A-101 Upper Plan","A-102 Lower Plan","A-301 Sections"]),
 dict(name="Round Barn", group="Specialty", style="Round Barn",
  history=("Round barns were promoted around 1900 - the Indiana experiment station built famous "
   "examples - on the theory that a circle encloses maximum volume with minimum wall and lets one "
   "worker feed all stock from the center silo. Few were built, but survivors are landmarks."),
  layout=("Circular plan: central silo, stanchions or stalls radiating around it, drive alley ring. "
   "Haymow in the conical roof volume; cupola vent at the peak."),
  structure=("Circular timber or balloon frame; conical or gambrel-cone roof; central silo of stave "
   "or concrete. The geometry is the structure - every rafter identical, meeting at the cupola."),
  systems=("Center feed distribution by gravity from the silo; cupola ventilation; the round form "
   "sheds wind from every direction."),
  spaces=[("Stall Ring",60,60),("Central Silo",16,16),("Haymow",60,60),("Drive Alley",60,8)],
  materials=["Radial timber framing","Conical roof","Central stave silo",
   "Cupola vent","Circular siding","Concrete grade floor"],
  codes=["IBC utility/agricultural","Historic preservation (where listed)","NEC agricultural buildings"],
  sheets=["A-101 Floor Plan","A-301 Sections"]),
 dict(name="Pole Barn", group="Equipment", style="Post-Frame Building",
  history=("Post-frame - the pole barn - was systematized after World War II: pressure-treated posts "
   "in the ground, trusses spanning post to post, metal skin. It cut farm building costs in half "
   "and became the default for equipment storage, shops, and arenas."),
  layout=("Clear-span bays between post lines; sliding doors sized to the equipment; optional lean-to "
   "bays on the eaves for open storage. Interior divisions are non-structural - rearrange freely."),
  structure=("Laminated or solid posts embedded 4-plus feet (or on piers); trusses bear directly on "
   "posts - no separate frame. Diaphragm action of the metal skin braces the building; engineers "
   "size the posts for the lateral loads."),
  systems=("Usually unconditioned: natural ventilation, basic lighting, minimal electric. Condensate "
   "control under the metal roof (drip barrier) protects equipment."),
  spaces=[("Equipment Bays",80,50),("Shop Corner",25,20),("Lean-To",80,12)],
  materials=["Pressure-treated posts","Roof trusses","Corrugated metal skin",
   "Sliding equipment doors","Gravel or concrete floor","Drip barrier"],
  codes=["IBC utility/agricultural","NFBA post-frame standards","NEC agricultural buildings"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan"]),
 dict(name="Equipment Shed", group="Equipment", style="Machinery Storage Shed",
  history=("Machinery sheds protect the farm's most expensive assets from weather - a roof over the "
   "tractors pays for itself in equipment life. The modern version adds a heated shop bay, because "
   "winter maintenance happens indoors."),
  layout=("Open equipment bays with tall doors; enclosed heated shop with workbench and tool storage; "
   "parts room; small office. Wash pad outside with oil-water separation."),
  structure=("Pole or steel frame; shop bay insulated and lined; equipment bays open or enclosed. "
   "Doors 14 to 16 feet tall for combines and sprayers."),
  systems=("Shop heating (radiant tube or unit heaters); compressed air throughout; welding "
   "ventilation; wash-pad drainage to separator. Good lighting - maintenance is detail work."),
  spaces=[("Equipment Bays",60,40),("Shop",30,25),("Parts Room",12,10),("Office",10,8),("Wash Pad",20,15)],
  materials=["Steel or post frame","Insulated shop bay","14-ft equipment doors",
   "Radiant shop heat","Compressed air piping","Welding ventilation","Wash-water separator"],
  codes=["IBC utility/agricultural","IFC repair garages","NEC agricultural buildings"],
  sheets=["A-101 Floor Plan","M-101 Shop Plan"]),
 dict(name="Sheep Barn", group="Livestock", style="Sheep / Wool Barn",
  history=("Sheep barns center on the shearing floor: a clean, well-lit space where shearers work "
   "down a line of sheep. The form - lambing pens, shearing floor, wool room - was standardized "
   "in 19th-century Australia and New Zealand and copied worldwide."),
  layout=("Lambing/jug pens along one wall; shearing floor central with catching pens feeding it; "
   "wool room with press and skirting table at the end; open loafing area for the flock."),
  structure=("Pole or timber frame; shearing floor of wood (kinder to sheep and shearers); good "
   "natural light over the shearing boards - shearers need to see."),
  systems=("Ventilation for the flock; shearing plant power (overhead or portable); wool press; "
   "water for the pens."),
  spaces=[("Shearing Floor",40,25),("Catching Pens",25,15),("Lambing Jugs",30,15),("Wool Room",20,15),
   ("Loafing Area",40,30)],
  materials=["Wood shearing floor","Catching pen gates","Wool press",
   "Skirting table","Overhead shearing plant","Natural lighting","Ventilation"],
  codes=["IBC utility/agricultural","NEC agricultural buildings","Local ag setbacks"],
  sheets=["A-101 Floor Plan"]),
 dict(name="Granary", group="Crop Storage", style="Grain Storage Barn",
  history=("Granaries - tight, rat-proof grain houses - are among the oldest farm buildings. The "
   "American crib granary with its slatted sides dried ear corn by airflow; modern versions are "
   "sealed bins with aeration floors, but the farm granary building persists for bagged and "
   "specialty grain."),
  layout=("Raised bins or rooms with tight floors; loading auger or leg serving the bins; bagging "
   "area; office with scale tickets. Everything elevated or sealed against rodents and moisture."),
  structure=("Tight wood or steel construction on raised piers; bins designed for grain pressure; "
   "aeration ducts in bin floors. The building must be mouse-tight: metal flashing at every joint."),
  systems=("Aeration fans per bin; grain temperature monitoring; dust control at the leg and "
   "distributor."),
  spaces=[("Grain Bins",40,25),("Bagging Area",20,15),("Auger Alley",40,8),("Office",10,8)],
  materials=["Raised bin construction","Aeration flooring","Grain legs and augers",
   "Temperature cables","Rodent-proof detailing","Sealed concrete or wood floors"],
  codes=["NFPA 61","IBC utility/agricultural","NEC agricultural buildings"],
  sheets=["A-101 Floor Plan","S-101 Bin Sections"]),
 dict(name="Calving Barn", group="Livestock", style="Maternity / Calving Barn",
  history=("Dedicated calving barns grew with larger dairy and beef operations: a clean, warm, "
   "observable space for the highest-risk hours of the production cycle. Cameras and close pens "
   "replaced the old pasture check."),
  layout=("Individual calving pens (12x12 minimum) with gates that swing to a handling alley; "
   "observation corridor or camera room; warming area for calves with heat lamps; vet supply room "
   "with hot water."),
  structure=("Pole or timber frame; pen walls of steel panels or wood; floors of sealed concrete "
   "with drainage - calving barns get washed down constantly."),
  systems=("Heating for winter calving (radiant or forced air); cameras to the house or office; hot "
   "water for sanitation; ventilation that keeps air fresh without chilling newborns."),
  spaces=[("Calving Pens",50,25),("Handling Alley",50,8),("Calf Warming",15,12),("Vet Room",12,10),
   ("Observation",10,8)],
  materials=["Steel pen panels","Sealed concrete floors","Radiant heating",
   "Calving cameras","Hot water system","Wash-down drainage","Heat lamps"],
  codes=["IBC utility/agricultural","NEC agricultural buildings","Local ag setbacks"],
  sheets=["A-101 Floor Plan"]),
 dict(name="Multi-Purpose Farm Barn", group="Specialty", style="Combination Barn",
  history=("The combination barn - shop, storage, and livestock under one roof - is the modern "
   "farm's headquarters building. As farms consolidated, one well-built multi-purpose barn "
   "replaced the scattered outbuildings of the old farmstead."),
  layout=("Zoned under one roof: heated shop with office; cold equipment storage; livestock wing "
   "with pens; feed and tack. Fire separation between shop (hot work) and hay/livestock areas."),
  structure=("Post-frame or steel clear-span; the shop bay gets insulation, liner, and a concrete "
   "floor; livestock wing gets ventilation and washable surfaces. One building, three "
   "environments."),
  systems=("Shop: heat, air, welding ventilation. Livestock: ventilation and water. All: good "
   "lighting, and fire separation between the zones that need it."),
  spaces=[("Shop",40,30),("Office",12,10),("Equipment Storage",40,30),("Livestock Wing",40,25),
   ("Feed/Tack",15,12),("Hay Bay",25,20)],
  materials=["Post-frame structure","Insulated shop bay","Fire separation walls",
   "Welding ventilation","Livestock ventilation","Sealed concrete floors"],
  codes=["IBC utility/mixed","NFPA 150","IFC repair garages","NEC agricultural buildings"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan"]),
]
