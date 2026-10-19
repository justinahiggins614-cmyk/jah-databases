#!/usr/bin/env python3
"""Makable-category blueprint archetypes: machines, tools, devices, vehicles, infrastructure.
For these families, 'spaces' are components/bays/zones with nominal sizes."""

MACHINES = [
 dict(name="Steam Engine", group="Power", style="Stationary Steam Engine",
  history=("The stationary steam engine - Newcomen's 1712 atmospheric engine, Watt's 1776 separate "
   "condenser - powered the Industrial Revolution. Corliss valve gear (1849) made it efficient "
   "enough to run factories and mills; thousands still survive in museums and heritage sites."),
  layout=("Boiler house separate from the engine room (safety); engine on a massive foundation with "
   "flywheel; line shafting distributing power to the mill. The engineer's station overlooks the "
   "whole machine."),
  structure=("Engine foundations of mass concrete isolated from the building; the engine house is a "
   "durable masonry or steel shell with a traveling crane for maintenance. Chimney sized to the "
   "boiler."),
  systems=("Boiler feedwater treatment; condensate return; lubrication (mechanical lubricators); "
   "governor and valve gear; exhaust to condenser or atmosphere. Safety valves and water columns "
   "per the boiler code."),
  spaces=[("Boiler",12,8),("Engine Bed",16,10),("Flywheel",10,10),("Line Shafting",40,4),
   ("Coal Bunker",12,10),("Feedwater",10,8),("Engineer Station",8,8)],
  materials=["Cast-iron engine frame","Steel boiler","Mass concrete foundations",
   "Babbitt bearings","Mechanical lubricators","Line shafting and belting","Brick chimney"],
  codes=["ASME BPVC Section I","ASME B31.1 power piping","NBIC inspection","Local boiler laws"],
  sheets=["M-101 General Arrangement","M-201 Foundation Plan","P-101 Steam Piping"]),
 dict(name="Wind Turbine", group="Power", style="Utility Wind Turbine",
  history=("Modern wind turbines descend from 1970s-80s Danish three-blade designs, scaled from "
   "kilowatts to 15-plus megawatts. The architecture is the same at every size: rotor, nacelle, "
   "tower, foundation - just bigger, with the largest rotors now wider than a football field is long."),
  layout=("Rotor and nacelle atop a tubular tower; foundation (spread footing or monopile offshore) "
   "below; access road and crane pad beside; substation and collection lines at the project edge. "
   "Spacing: 3 to 5 rotor diameters between turbines."),
  structure=("Tubular steel tower in sections; foundation designed for the overturning moment - the "
   "governing load case. Blades of fiberglass/carbon composite; nacelle bedplate carries the "
   "drivetrain."),
  systems=("Pitch and yaw control; converter and transformer in or beside the nacelle; SCADA "
   "monitoring; lightning protection (blades are lightning rods); aviation lighting per FAA."),
  spaces=[("Rotor Diameter",400,400),("Nacelle",30,12),("Tower",300,15),("Foundation",60,60),
   ("Crane Pad",60,40),("Substation",40,30)],
  materials=["Composite blades","Tubular steel tower","Permanent-magnet generator",
   "Pitch/yaw drives","Mass concrete foundation","SCADA system","Lightning protection"],
  codes=["IEC 61400","ASCE 7 wind","FAA obstruction lighting","NEC 2023"],
  sheets=["M-101 General Arrangement","S-101 Foundation Plan","E-101 Collection System"]),
 dict(name="Industrial Press", group="Processing", style="Hydraulic Press",
  history=("Hydraulic presses descend from Joseph Bramah's 1795 hydraulic press. The H-frame shop "
   "press and the C-frame production press stamp, bend, and form metal in every fabrication shop; "
   "forging presses scale the same principle to thousands of tons."),
  layout=("Press centered in its cell with die storage adjacent; material infeed from one side, "
   "parts outfeed to the other; hydraulic power unit behind guarding; operator station with "
   "two-hand controls at the front."),
  structure=("Press frame of welded steel plate; foundation sized for the tonnage plus impact; "
   "bolster and ram precision-ground. Guarding per OSHA - the danger zone is fully enclosed."),
  systems=("Hydraulic power unit (pump, reservoir, valving); tonnage monitoring; light curtains or "
   "two-hand control; die heating/cooling where the process needs it."),
  spaces=[("Press Cell",16,12),("Die Storage",12,10),("Infeed",10,8),("Outfeed",10,8),
   ("Hydraulic Unit",8,6),("Operator Station",6,4)],
  materials=["Welded steel frame","Hydraulic cylinders","Precision bolster",
   "Light curtains","Tonnage monitor","Die sets","Guarding"],
  codes=["ANSI B11.2 hydraulic presses","OSHA 1910.217","NFPA 79","NEC 2023 industrial"],
  sheets=["M-101 General Arrangement","H-101 Hydraulic Schematic"]),
 dict(name="Conveyor System", group="Material Handling", style="Belt Conveyor Line",
  history=("Belt conveyors mechanized bulk handling in the late 1800s - Thomas Robins' 1892 "
   "conveyor for coal and ore set the pattern. The modern troughed-belt conveyor moves thousands "
   "of tons per hour in mines, ports, and plants."),
  layout=("Tail section with take-up; inclined or horizontal carries on idler frames; head section "
   "with drive and discharge; transfer chutes between conveyors; walkway alongside the full "
   "length with crossovers."),
  structure=("Truss or beam gallery on bents; idler frames at spacing per belt tension; head/tail "
   "pulleys on plummer blocks. The gallery encloses the belt in cold climates."),
  systems=("Drive motors with soft starts or VFDs; belt scales; dust control at transfers; "
   "pull-cord emergency stops along the walkway; fire detection in enclosed galleries."),
  spaces=[("Tail Section",20,8),("Carry Run",200,6),("Head Section",20,10),("Drive House",15,12),
   ("Transfer Chute",10,8),("Walkway",220,4)],
  materials=["Troughed belt","Idler frames","Drive pulleys",
   "Truss gallery","Take-up assembly","Belt scale","Pull-cord switches"],
  codes=["CEMA conveyor standards","ASME B20.1","MSHA/OSHA","NEC 2023 industrial"],
  sheets=["M-101 Profile","M-201 Gallery Sections"]),
 dict(name="Water Pump Station", group="Processing", style="Municipal Pump Station",
  history=("Municipal pump stations - water and wastewater - are the hidden infrastructure of every "
   "city: Roman aqueducts used gravity, but modern cities pump. The dry-pit/wet-pit station with "
   "centrifugal pumps is the standard form worldwide."),
  layout=("Wet well receiving inflow; dry pit with pump row beside it; valve and meter vault; "
   "electrical room; standby generator outside; odor control at the wet well. All-weather access "
   "for maintenance trucks."),
  structure=("Wet well of watertight concrete below grade; dry pit with pump foundations isolated "
   "for vibration; the superstructure is a durable utility building with crane or monorail for "
   "pump removal."),
  systems=("Pumps on VFDs for flow matching; level control; standby power (full station load); "
   "odor control (biofilter or carbon); SCADA to the utility's control center."),
  spaces=[("Wet Well",20,15),("Dry Pit",30,15),("Valve Vault",15,10),("Electrical Room",15,12),
   ("Generator",12,10),("Odor Control",12,10)],
  materials=["Centrifugal pumps","VFD drives","Watertight concrete",
   "Pump control SCADA","Standby generator","Odor biofilter","Crane/monorail"],
  codes=["Ten States Standards","NFPA 820","NEC 2023","Local utility standards"],
  sheets=["M-101 General Arrangement","P-101 Piping Plan","E-101 Power Plan"]),
 dict(name="Air Compressor Station", group="Processing", style="Industrial Air Compressor",
  history=("Compressed air - the fourth utility - has powered industry since 19th-century mines "
   "ran pneumatic drills. The modern rotary-screw compressor with refrigerated dryer delivers "
   "clean, dry air to the whole plant from one station."),
  layout=("Compressor row with service clearances; receiver tanks; dryer and filter train; "
   "distribution header leaving the room; electrical and controls along one wall. Cool, clean "
   "intake air location matters."),
  structure=("Equipment on housekeeping pads; the room needs ventilation for compressor heat "
   "(or ducted heat recovery); receivers are pressure vessels on their own supports."),
  systems=("Sequencing controls stage compressors to demand; dryers hold the pressure dew point; "
   "leak management (a quarter of air is typically lost to leaks); heat recovery to the building."),
  spaces=[("Compressor Row",30,12),("Receivers",15,10),("Dryer Train",15,8),("Electrical",12,10),
   ("Controls",8,6)],
  materials=["Rotary-screw compressors","Air receivers","Refrigerated dryers",
   "Coalescing filters","Sequencing controls","Distribution header","Heat recovery"],
  codes=["ASME BPVC Section VIII","OSHA 1910.169","CAGI standards","NEC 2023 industrial"],
  sheets=["M-101 General Arrangement","P-101 Air Piping"]),
 dict(name="CNC Mill", group="Processing", style="3-Axis CNC Machining Center",
  history=("CNC milling descends from John Parsons' 1940s punched-card mill controls and MIT's "
   "1952 Servomechanisms Lab machine. The vertical machining center - tool changer, enclosure, "
   "flood coolant - became the universal machine shop tool in the 1980s."),
  layout=("Machine centered with operator door facing the aisle; chip conveyor to the side or rear; "
   "coolant tank beneath; tool presetter and workholding storage nearby; stock rack at the cell "
   "entry."),
  structure=("Cast-iron or polymer-concrete machine base on a level pad; the enclosure contains "
   "coolant and chips. Leveling and anchoring per the builder's foundation drawing."),
  systems=("Flood or through-spindle coolant with filtration; compressed air for tool change; "
   "mist collection; CNC control with its programs and probing."),
  spaces=[("Machine Envelope",10,8),("Operator Zone",8,6),("Chip Conveyor",6,4),
   ("Stock Rack",8,4),("Tool Storage",6,4)],
  materials=["Cast machine base","Automatic tool changer","Flood coolant system",
   "Chip conveyor","Mist collector","CNC control","Workholding vises"],
  codes=["ANSI B11.8 machining centers","NFPA 79","OSHA machine guarding","NEC 2023 industrial"],
  sheets=["M-101 General Arrangement","F-101 Foundation Detail"]),
 dict(name="Industrial 3D Printer", group="Processing", style="Large-Format Additive Machine",
  history=("Additive manufacturing grew from Chuck Hull's 1984 stereolithography patent. "
   "Large-format machines now print end-use parts in engineering polymers and metals - the "
   "blueprint is the product, built layer by layer."),
  layout=("Machine cell with the printer centered; material storage (dry, controlled) adjacent; "
   "post-processing station (support removal, curing); ventilation enclosure around polymer "
   "machines; operator console outside the enclosure."),
  structure=("Printer on a rigid, level base - vibration kills print quality; the enclosure "
   "contains heat and fumes. Material storage needs the dryness the filament manufacturer "
   "specifies."),
  systems=("Enclosure ventilation with filtration (UFPs and VOCs); heated chamber control; dry-box "
   "filament feed; power conditioning - a mid-print outage ruins the part."),
  spaces=[("Printer Cell",12,10),("Material Storage",8,6),("Post-Processing",10,8),
   ("Ventilation",6,4),("Operator Console",6,4)],
  materials=["Motion gantry","Heated chamber","Filament dry boxes",
   "Ventilation filtration","Post-processing station","UPS power","Build plates"],
  codes=["ASTM F42 additive","UL 3400 (draft)","OSHA ventilation","NEC 2023 industrial"],
  sheets=["M-101 General Arrangement","M-101 Ventilation Plan"]),
 dict(name="Farm Tractor", group="Material Handling", style="Row-Crop Tractor",
  history=("Tractors replaced the horse between 1920 and 1950: Fordson's 1917 mass-produced tractor, "
   "then the Farmall Regular (1924) with its tricycle front for cultivating rows. Diesel, "
   "hydraulics (Ferguson's 1930s three-point hitch), and cabs followed."),
  layout=("Engine forward, clutch and transmission central, rear axle and PTO at the back; operator "
   "station with ROPS cab above; three-point hitch and drawbar at the rear; front weights and "
   "optional loader."),
  structure=("The drivetrain is the frame: engine, clutch housing, transmission, and rear axle bolt "
   "into one structural spine. ROPS cab certified to the overturn standard."),
  systems=("Diesel with emissions aftertreatment; hydraulics (steering, hitch, remotes); PTO "
   "(540/1000 rpm); electrical for lights and precision-ag displays."),
  spaces=[("Engine Bay",6,4),("Operator Cab",5,5),("Rear Axle/PTO",5,4),("Hitch Zone",4,4)],
  materials=["Diesel engine","ROPS cab","Three-point hitch",
   "Hydraulic system","PTO driveline","Precision-ag display","Ballast weights"],
  codes=["OSHA ROPS 1928.51","ASABE standards","EPA Tier 4","SAE J2194"],
  sheets=["M-101 General Arrangement","H-101 Hydraulic Schematic"]),
 dict(name="Excavator", group="Material Handling", style="Hydraulic Excavator",
  history=("Hydraulic excavators replaced cable shovels in the 1950s-60s: the French Poclain and "
   "German Demag machines proved hydraulics could dig. The tracked 360-degree excavator is now "
   "the universal earthmoving machine."),
  layout=("Undercarriage (tracks, carbody) below; swing bearing and upper structure above; boom, "
   "stick, and bucket forward; counterweight and engine at the rear; cab on the left with full "
   "visibility of the digging."),
  structure=("X-frame carbody; swing bearing as the critical joint; boom and stick of welded "
   "box-section steel. Stability - tipping load - governs the operating envelope."),
  systems=("Hydraulic pumps, valves, and cylinders (boom, stick, bucket, swing, travel); diesel "
   "power; the control pattern (ISO/SAE) selectable; telematics standard."),
  spaces=[("Undercarriage",14,10),("Upper Structure",12,9),("Boom/Stick/Bucket",20,4),
   ("Counterweight",8,6),("Cab",5,5)],
  materials=["Welded boom and stick","Swing bearing","Hydraulic cylinders",
   "Track frames","Diesel engine","ROPS/FOPS cab","Telematics"],
  codes=["ISO 6165","SAE J1177","OSHA 1926.602","EPA Tier 4"],
  sheets=["M-101 General Arrangement","H-101 Hydraulic Schematic"]),
 dict(name="Lathe", group="Processing", style="Engine Lathe",
  history=("The engine lathe - Maudslay's 1800 screw-cutting lathe - is the mother of machine tools: "
   "it can make its own parts. The modern geared-head engine lathe keeps the same layout: "
   "headstock, bed, carriage, tailstock."),
  layout=("Headstock (spindle, gears) at the left; bed with precision ways; carriage and cross-slide "
   "traveling the bed; tailstock at the right; chip pan beneath; motor and drive in the cabinet "
   "base."),
  structure=("Cast-iron bed with hardened ways - the machine's accuracy lives in the bed; leveled on "
   "the shop floor and anchored. Headstock spindle on precision bearings."),
  systems=("Spindle drive (geared or VFD); carriage feed and threading gearbox; coolant; chuck "
   "guarding with interlock."),
  spaces=[("Bed/Work Zone",8,3),("Headstock",3,3),("Tailstock",2,3),("Cabinet Base",8,3)],
  materials=["Cast-iron bed","Precision spindle","Geared headstock",
   "Quick-change toolpost","Chuck guard","Coolant system","Leveling mounts"],
  codes=["ANSI B11.6 lathes","NFPA 79","OSHA machine guarding","NEC 2023 industrial"],
  sheets=["M-101 General Arrangement"]),
 dict(name="Generator Set", group="Power", style="Standby Generator",
  history=("Standby generators became standard for critical facilities after the 1965 Northeast "
   "blackout proved the grid could fail widely. The modern diesel or gas genset - engine, "
   "alternator, transfer switch - starts automatically in seconds."),
  layout=("Genset on its pad or in its enclosure; automatic transfer switch beside the service "
   "entrance; fuel storage (sub-base tank or remote) with containment; exhaust routed safely; "
   "battery charger and block heater for reliable starting."),
  structure=("Genset on vibration isolators on a concrete pad; enclosure for weather and sound "
   "(critical in urban sites); fuel tank double-walled with leak detection."),
  systems=("Automatic transfer switch with engine start; load bank testing provisions; remote "
   "monitoring and alarming; exhaust aftertreatment per emissions rules."),
  spaces=[("Genset",12,6),("Transfer Switch",4,3),("Fuel Storage",10,6),("Exhaust Zone",6,4)],
  materials=["Diesel/gas engine","Alternator","Automatic transfer switch",
   "Double-wall fuel tank","Sound enclosure","Battery system","Remote monitor"],
  codes=["NFPA 110","NFPA 37","EPA emissions","NEC 700/701"],
  sheets=["M-101 General Arrangement","E-101 One-Line Diagram"]),
]

TOOLS = [
 dict(name="Claw Hammer", group="Hand Tools", style="Framing Claw Hammer",
  history=("The claw hammer's form is ancient - Roman blacksmiths forged them - but the modern "
   "American pattern with its curved claw was standardized in the 1800s. The 16-ounce smooth-face "
   "framer remains the carpenter's signature tool."),
  layout=("Head: striking face, cheek, and claw; eye joining head to handle; handle of hickory, "
   "steel, or fiberglass with a gripped end. Balance point just below the head."),
  structure=("Head of forged, heat-treated steel; handle wedged and epoxied into the eye; the claw "
   "split and beveled for nail pulling. Faces are chamfered to reduce glancing marks."),
  systems=("No systems - the tool is pure mechanics. Maintenance: keep the face clean, the handle "
   "tight, and never strike hardened steel with the face."),
  spaces=[("Head",4.5,1.2),("Claw",2.5,1.0),("Handle",11,1.1),("Grip",4.5,1.3)],
  materials=["Forged steel head","Hickory handle","Steel wedge and epoxy",
   "Rubber grip","Heat-treated face"],
  codes=["ASME B107 hand tools","OSHA hand tool safety"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Handsaw", group="Hand Tools", style="Western Panel Saw",
  history=("Western handsaws - teeth that cut on the push stroke - were perfected by 19th-century "
   "American makers like Disston of Philadelphia. Taper grinding (thinner at the back) keeps the "
   "blade from binding; the modern hardpoint saw made sharpening disposable."),
  layout=("Blade with toe, heel, tooth line, and back; handle (D-handle or pistol grip) at the "
   "heel; teeth sized by points-per-inch for rip vs. crosscut."),
  structure=("Spring-steel blade, taper-ground; teeth set alternately for kerf clearance; handle "
   "bolted through the heel with saw nuts. Blade tension comes from the handle bolts."),
  systems=("Maintenance system: keep teeth sharp, the blade clean and lightly oiled, and store hung "
   "or sheathed - a kinked saw is a ruined saw."),
  spaces=[("Blade",26,5),("Tooth Line",26,0.5),("Handle",6,4)],
  materials=["Spring-steel blade","Hardwood handle","Saw nuts",
   "Hardpoint teeth (disposable)","Blade oil"],
  codes=["ASME B107","OSHA hand tool safety"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Cordless Drill", group="Power Tools", style="Cordless Drill/Driver",
  history=("Cordless drills grew from 1960s NASA-Black & Decker work (the cordless tools for "
   "Apollo) into the 18-volt lithium-ion platform that now runs the jobsite. The drill/driver - "
   "clutch, gearbox, chuck - is the first tool in every kit."),
  layout=("Motor and gearbox in the barrel; chuck at the nose; trigger with forward/reverse; "
   "clutch ring behind the chuck; battery sliding into the base of the pistol grip."),
  structure=("Clamshell housing of glass-filled nylon; metal gearbox and chuck; brushless motor in "
   "modern tools. The battery is the structural base - it sets the tool's balance."),
  systems=("Lithium-ion battery platform (the real product - one battery runs dozens of tools); "
   "electronic clutch; LED work light; battery management preventing over-discharge."),
  spaces=[("Barrel/Motor",7,3),("Chuck",2.5,2),("Grip",4.5,2.5),("Battery",4,3.5)],
  materials=["Brushless motor","Metal gearbox","1/2-in. chuck",
   "Li-ion battery pack","Glass-filled nylon housing","LED work light"],
  codes=["UL 62841","OSHA power tools","UN 38.3 batteries"],
  sheets=["D-101 Detail Drawing","E-101 Battery Platform"]),
 dict(name="Table Saw", group="Power Tools", style="Contractor Table Saw",
  history=("The table saw - circular blade rising through a table - was refined in the early 1900s "
   "and made safe-ish by the riving knife and blade guard. It remains the heart of the woodshop: "
   "rip, crosscut, dado, bevel."),
  layout=("Cast-iron table with miter slots; blade arbor beneath with tilt mechanism; rip fence on "
   "rails; outfeed support behind; dust port below; switch and overload on the front rail."),
  structure=("Trunnion assembly carrying the arbor - cabinet saws mount it to the cabinet, "
   "contractor saws to the table. The fence must lock parallel to the blade every time."),
  systems=("Dust collection (the saw makes mountains of it); riving knife and guard; anti-kickback "
   "pawls; flesh-sensing brake on modern safety saws."),
  spaces=[("Table",27,20),("Blade Zone",10,0.13),("Rip Fence",30,3),("Outfeed",27,12),("Motor Cabinet",20,18)],
  materials=["Cast-iron table","Trunnion assembly","Riving knife",
   "Rip fence system","Dust port","Safety brake cartridge","Miter gauge"],
  codes=["UL 62841-3-1","OSHA 1910.213","NFPA 664 dust"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Adjustable Wrench", group="Hand Tools", style="Crescent Wrench",
  history=("The adjustable wrench - Johansson's 1891 Swedish patent, popularized by the Crescent "
   "Tool Company of Jamestown, New York - put a toolbox in one tool. The knurled worm gear moving "
   "the jaw is the whole invention."),
  layout=("Fixed jaw and head; movable jaw on the slide; knurled adjusting worm; handle with "
   "hanging hole. Jaws angled 15 degrees to the handle for knuckle clearance."),
  structure=("Drop-forged alloy steel, heat-treated; the worm and rack teeth are the precision "
   "parts - slop here is what rounds fasteners. Chrome or black-oxide finish."),
  systems=("Maintenance: keep the worm clean and lightly oiled; never use a cheater bar - the "
   "wrench is not a lever for pipes."),
  spaces=[("Head/Jaws",3,1.5),("Worm Gear",1.5,1),("Handle",7,1)],
  materials=["Drop-forged alloy steel","Knurled worm","Heat-treated jaws","Chrome finish"],
  codes=["ASME B107.8","OSHA hand tool safety"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Screwdriver Set", group="Hand Tools", style="Screwdriver Set",
  history=("Screwdrivers follow the screw: slotted drivers are centuries old; Phillips (1930s) "
   "matched the new cross-head screws for assembly lines; Torx and square drives followed for "
   "better torque transfer. The set - not the single driver - is the tool."),
  layout=("Tip (the drive profile), shank, bolster (on heavy drivers), handle with flutes or "
   "cushion grip, and striking cap on demolition drivers. Sets span Phillips, slotted, Torx, "
   "square, and precision sizes."),
  structure=("Shank of hardened chrome-vanadium steel; tip precision-ground to the drive standard; "
   "handle molded over the shank's tang. Insulated drivers add 1000V-rated sheathing."),
  systems=("Organization is the system: indexed case or roll so the right tip is found, not "
   "improvised. Magnetized tips hold the screw."),
  spaces=[("Tip",1,0.4),("Shank",5,0.35),("Handle",4,1.2),("Case",12,8)],
  materials=["Chrome-vanadium shanks","Precision-ground tips","Cushion grips",
   "Indexed storage case","Insulated options"],
  codes=["ASME B107.600","IEC 60900 insulated","OSHA hand tool safety"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Carpenter's Square", group="Hand Tools", style="Framing Square",
  history=("The steel framing square - 16 by 24 inches - is the carpenter's computer: its rafter "
   "tables (printed on the face since the 1800s) lay out stairs, rafters, and polygons. The "
   "Stanley 19th-century squares taught generations from their printed tables."),
  layout=("Long blade (body) 24 inches; tongue 16 inches; the heel where they meet; rafter tables, "
   "brace tables, and scales stamped on both faces."),
  structure=("Hardened spring steel, true to a few thousandths; the inside corner is the reference. "
   "A dropped square must be checked - the tool's truth is its squareness."),
  systems=("The printed tables are the system: rafter lengths per foot of run, brace measurements, "
   "octagon scales. Learn the tables and the square replaces math."),
  spaces=[("Blade",24,2),("Tongue",16,2),("Heel",2,2)],
  materials=["Hardened steel","Stamped rafter tables","Protective finish"],
  codes=["ASME B107","OSHA hand tool safety"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Chisel Set", group="Hand Tools", style="Bench Chisel Set",
  history=("Chisels are Stone Age tools refined: the socket or tang bench chisel with its "
   "25-degree bevel has cut mortises for millennia. Japanese laminated chisels and Western "
   "socket chisels represent the two great traditions."),
  layout=("Cutting edge with bevel; blade; bolster or shoulder; socket or tang; handle (wood or "
   "composite) with ferrule and leather washer. Sets run 1/4 to 1-1/2 inches."),
  structure=("Blade of high-carbon or laminated steel, hardened at the edge and softer at the "
   "shank; the socket must fit the handle's tenon perfectly - a loose chisel is dangerous."),
  systems=("Sharpening is the tool: hollow-grind, hone, strop. A sharp chisel is safe; a dull one "
   "needs force and slips."),
  spaces=[("Edge/Bevel",1,1),("Blade",5,1),("Handle",5,1.2)],
  materials=["High-carbon steel","Hardwood handles","Leather washers","Honing guides","Strops"],
  codes=["ASME B107","OSHA hand tool safety"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Bench Vise", group="Workshop", style="Machinist's Bench Vise",
  history=("The bench vise - the third hand of the shop - was refined in the 1800s with the "
   "swivel base and anvil. The machinist's vise with its 360-degree swivel and pipe jaws holds "
   "anything the shop needs to work on."),
  layout=("Fixed jaw and slide; movable jaw on the screw; swivel base with locking handles; anvil "
   "flat behind the fixed jaw; pipe jaws below the main jaws."),
  structure=("Cast-iron or ductile-iron body; hardened steel jaw faces (replaceable, serrated); "
   "Acme screw with thrust bearing. Bolted through the bench with the fixed jaw just past the "
   "edge."),
  systems=("Mounting is the system: through-bolted to a bench that doesn't move. Jaw protectors "
   "(copper, aluminum) for finished work."),
  spaces=[("Jaws",6,4),("Slide",8,3),("Swivel Base",8,8),("Anvil",4,3)],
  materials=["Ductile-iron body","Hardened jaw faces","Acme screw",
   "Swivel base","Pipe jaws","Bench bolts"],
  codes=["ASME B107","OSHA 1910.212"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Angle Grinder", group="Power Tools", style="Angle Grinder",
  history=("Angle grinders grew from 1950s German metalworking (Ackermann + Schmitt, later Flex) "
   "into the universal cutting and grinding tool. The 4-1/2-inch grinder - cutting, grinding, "
   "flap discs - is the most versatile and most dangerous handheld power tool."),
  layout=("Motor body in-line; bevel gear head turning the spindle 90 degrees; disc guarded on the "
   "top half; side handle threading into the gear head; paddle or slide switch."),
  structure=("Spiral bevel gears in the head; spindle lock for disc changes; guard adjustable "
   "without tools on modern designs. The disc is the consumable - rated speed must exceed the "
   "grinder's RPM."),
  systems=("Disc selection is the system: cutting, grinding, flap, wire - each with its max RPM. "
   "Dust extraction shrouds for concrete work; never remove the guard."),
  spaces=[("Motor Body",12,3),("Gear Head",4,3.5),("Disc",4.5,0.25),("Side Handle",5,1.2)],
  materials=["Bevel gear head","Spindle lock","Adjustable guard",
   "Cutting/grinding discs","Side handle","Dust shroud"],
  codes=["UL 62841-2-3","ANSI B7.1 abrasives","OSHA 1910.243"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Tape Measure", group="Hand Tools", style="Power-Lock Tape",
  history=("The steel tape measure - Stanley's 1868 patent for the PowerLock return spring - put "
   "25 feet in a pocket. Blade standout (how far it extends unsupported) and the end-hook's "
   "riveted slip (exactly one hook thickness) are the engineering."),
  layout=("Case with belt clip; blade coiled on the return spring; end hook riveted with calibrated "
   "slip; blade lock; standout markings. Widths from 1/2 to 1-1/4 inches."),
  structure=("Concave-curved spring-steel blade - the curve is the stiffness; the case protects the "
   "coil; the hook slides exactly its own thickness for inside/outside accuracy."),
  systems=("Reading is the skill: 16-inch stud marks (red), 19.2-inch marks (black diamond) for "
   "engineered layouts. Keep the blade clean; a kinked tape lies."),
  spaces=[("Case",3.5,3),("Blade Extended",300,1),("End Hook",1.5,1)],
  materials=["Spring-steel blade","Polycarbonate case","Return spring",
   "Sliding end hook","Blade lock","Belt clip"],
  codes=["NIST Handbook 44","OSHA hand tool safety"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Workbench", group="Workshop", style="Woodworking Workbench",
  history=("The workbench - heavy, flat, with vises - is the woodworker's foundation tool. The "
   "Roubo bench (18th-century French) with its leg vise and the Scandinavian cabinetmaker's bench "
   "are the two classics; modern versions add the MFT hole grid."),
  layout=("Top (the reference surface) at knuckle height; front vise and tail/end vise; tool well "
   "or not (purists skip it); stretchers and shelf below; dog holes in the top for holdfasts."),
  structure=("Mass is the structure: 150-plus pounds so hand-planing doesn't move it. Top of "
   "laminated maple 3-plus inches thick, flattened true; legs and stretchers mortised."),
  systems=("Workholding is the system: vises, dogs, holdfasts - the bench holds the work so both "
   "hands are free. Flatness maintained with periodic re-flattening."),
  spaces=[("Top",72,30),("Front Vise",10,8),("Tail Vise",12,8),("Shelf",60,24)],
  materials=["Laminated maple top","Leg vise hardware","Tail vise",
   "Bench dogs and holdfasts","Mortised base","Finish (oil/wax)"],
  codes=["OSHA 1910.212"],
  sheets=["D-101 Detail Drawing"]),
]

DEVICES = [
 dict(name="Refrigerator", group="Kitchen", style="French-Door Refrigerator",
  history=("Mechanical refrigeration for homes arrived in the 1920s-30s (Frigidaire, Kelvinator); "
   "the frost-free top-freezer of the 1950s and the French-door of the 2000s refined it. The vapor- "
   "compression cycle - compressor, condenser, expansion, evaporator - hasn't changed, only "
   "improved."),
  layout=("Refrigerator compartment up top with French doors; freezer drawer below; through-door "
   "ice and water; compressor and condenser at the back bottom; door bins and crispers inside."),
  structure=("Steel cabinet with foamed-in-place polyurethane insulation; inner liner of ABS; door "
   "gaskets magnetic. Leveling and door alignment are the installation."),
  systems=("Vapor-compression refrigeration with variable-speed compressor; defrost control; ice "
   "maker with water filtration; door alarms. Energy Star ratings drive the engineering."),
  spaces=[("Fresh Food",36,28),("Freezer Drawer",36,20),("Doors Open Swing",36,30),("Mechanical",36,10)],
  materials=["Steel cabinet","Polyurethane insulation","Variable-speed compressor",
   "Ice/water system","LED interior lighting","Magnetic gaskets"],
  codes=["UL 60335-2-24","DOE energy standards","ASHRAE 15 (charge limits)","EPA SNAP refrigerants"],
  sheets=["D-101 Detail Drawing","R-101 Refrigeration Diagram"]),
 dict(name="Washing Machine", group="Kitchen", style="Front-Load Washer",
  history=("Electric washing machines arrived in the 1900s-10s; the front-loader - gentler, more "
   "efficient - conquered the world after 1990s energy rules. The horizontal-axis drum uses "
   "gravity and a fraction of the water of top-loaders."),
  layout=("Drum horizontal on bearings; door (with bellows gasket) at front; detergent drawer top "
   "left; control panel top; pump and drain at bottom rear; counterweights (concrete!) around the "
   "tub."),
  structure=("Outer cabinet; suspended tub on springs and dampers - the spin cycle's 1,200-plus RPM "
   "needs the suspension; concrete counterweights. Leveled precisely or it walks."),
  systems=("Direct-drive or belt motor with imbalance sensing; water valves and level sensing; drain "
   "pump; heater for sanitizing cycles. Vibration control is the engineering."),
  spaces=[("Cabinet",27,27),("Door Swing",27,24),("Drum",22,20),("Top Panel",27,6)],
  materials=["Stainless drum","Suspension springs/dampers","Concrete counterweights",
   "Direct-drive motor","Bellows gasket","Control board"],
  codes=["UL 2157","DOE energy/water standards","IEC 60456"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Microwave Oven", group="Kitchen", style="Countertop Microwave",
  history=("The microwave oven grew from Raytheon's 1945 radar magnetron accident (Percy Spencer's "
   "melting candy bar) to the 1967 countertop Radarange. The cavity magnetron, waveguide, and "
   "turntable are still the design."),
  layout=("Cooking cavity with turntable; magnetron and waveguide feeding from the side; control "
   "panel and door with choke seal at front; cooling fan and power supply at rear."),
  structure=("Steel cavity (the Faraday cage); door with RF choke seal and mesh screen; the cabinet "
   "is a vented shell. Door interlocks are triple-redundant by law."),
  systems=("Magnetron generating 2.45 GHz; waveguide and mode stirrer distributing energy; "
   "turntable evening the field; inverter power supplies in modern units for true variable power."),
  spaces=[("Cavity",16,14),("Turntable",13,13),("Control Panel",4,14),("Magnetron Bay",8,10)],
  materials=["Steel cavity","Magnetron","Waveguide",
   "RF choke door","Turntable motor","Inverter supply"],
  codes=["UL 923","FDA 21 CFR 1030.10","IEC 60705"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Television", group="Home", style="Flat-Panel Smart TV",
  history=("TVs shrank from 1950s consoles to 2000s flat panels: plasma, then LCD-LED, now OLED and "
   "Mini-LED. The display went from furniture to a millimeter-thin panel; the smarts moved into "
   "the set itself."),
  layout=("Panel with backlight/display layers; main board, power supply, and speakers behind; "
   "wall-mount VESA pattern or stand; bezel minimal. Viewing distance: 1.5 to 2.5 times the "
   "diagonal."),
  structure=("Panel glass or film stack in a rigid chassis; VESA mount pattern standardized; the "
   "stand or wall mount carries the (now light) load."),
  systems=("Display driver electronics; smart-TV SoC with streaming apps; HDMI 2.1 inputs; audio "
   "(often supplemented by soundbar); ambient light sensing for picture adjustment."),
  spaces=[("Panel 55in",48,28),("Wall Mount Zone",16,16),("Stand Footprint",36,12)],
  materials=["LCD/OLED panel","LED backlight","Main board SoC",
   "Power supply","VESA mount","Speakers"],
  codes=["UL 60065/62368","FCC Part 15","DOE energy standards","HDMI/HDCP"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Desktop Computer", group="Computing", style="Tower Workstation",
  history=("Desktop computers standardized in the 1980s around the AT/ATX tower: motherboard, "
   "expansion slots, drive bays. The modern tower keeps the form while cooling kilowatts of "
   "silicon."),
  layout=("Motherboard tray with CPU, RAM, expansion slots; power supply at bottom or top rear; "
   "drive bays front; fans front-to-back airflow path; cable routing behind the tray."),
  structure=("Steel chassis with motherboard standoffs; the ATX standard fixes mounting points so "
   "parts interchange. Airflow path is the thermal design."),
  systems=("Power supply (80 Plus rated); cooling (air or liquid); front-panel I/O; the thermal "
   "envelope (TDP) sizes everything."),
  spaces=[("Chassis",18,8),("Motherboard Zone",12,10),("PSU Bay",6,6),("Drive Bays",6,6)],
  materials=["ATX chassis","Motherboard","CPU and cooler",
   "Power supply","Memory and storage","Case fans"],
  codes=["UL 62368","FCC Part 15","80 Plus","ATX specification"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Laptop", group="Computing", style="Clamshell Laptop",
  history=("Laptops shrank from 1980s luggables (Osborne 1, 24 pounds) to today's 3-pound "
   "ultrabooks. The clamshell - screen hinged to keyboard base - won by 1990 and never lost."),
  layout=("Display assembly (panel, webcam, antennas in the lid); base with keyboard, trackpad, "
   "battery, and mainboard; hinge joining them; ports along the sides."),
  structure=("Unibody aluminum or magnesium; the hinge is the wear item; the battery often fills "
   "the base. Thinness fights thermals - heat pipes and fans in millimeters."),
  systems=("Battery with charge management; thermal system (heat pipes, fans); Wi-Fi/Bluetooth "
   "antennas in the lid; power delivery over USB-C."),
  spaces=[("Base",13,9),("Display Open",13,9),("Hinge Zone",13,1)],
  materials=["Unibody chassis","Display panel","Battery pack",
   "Heat-pipe cooling","Keyboard/trackpad","Hinge assembly"],
  codes=["UL 62368","FCC Part 15","UN 38.3 batteries","USB-C PD"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Smartphone", group="Computing", style="Slab Smartphone",
  history=("Smartphones converged in 2007: the slab with a touchscreen, radios for everything, and "
   "an app store. The engineering is density - a supercomputer, six radios, and cameras in 7 "
   "millimeters."),
  layout=("Display stack front; mainboard, battery, and cameras in the midframe; antennas at the "
   "edges (they can't be shielded); SIM/USB at the bottom edge."),
  structure=("Glass front and back (or metal) on a rigid midframe; waterproof gaskets (IP68); the "
   "battery glued in. Drop survival is structural engineering."),
  systems=("SoC with modem; multi-band antennas (cellular, Wi-Fi, BT, GPS, NFC, UWB); battery "
   "management; camera modules with OIS."),
  spaces=[("Body",6.3,3),("Display",6.1,2.9),("Camera Array",1.5,1.5)],
  materials=["Glass/metal body","OLED display","SoC",
   "Battery cell","Camera modules","Antenna array"],
  codes=["UL 62368","FCC Part 15/22/24","IP68","USB-C"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Air Conditioner", group="Climate", style="Split-System AC",
  history=("Modern air conditioning began with Carrier's 1902 humidity control for a Brooklyn print "
   "shop. The residential split system - noisy parts outside, quiet coil inside - became the "
   "global standard after 1960s Japanese mini-split refinements."),
  layout=("Outdoor condenser unit on pad or brackets; indoor evaporator coil (in furnace/air "
   "handler or wall cassette); refrigerant lines and condensate drain between; thermostat inside."),
  structure=("Condenser on a level pad with service clearances; line set routed and insulated; the "
   "indoor unit mounted for condensate drainage (the silent killer of installations)."),
  systems=("Vapor-compression with variable-speed compressor; refrigerant charge critical; "
   "condensate management; SEER2 ratings; smart thermostat control."),
  spaces=[("Condenser",36,36),("Air Handler",24,20),("Line Set Run",240,4)],
  materials=["Condenser unit","Evaporator coil","Line set",
   "Thermostat","Condensate pump","Refrigerant"],
  codes=["UL 1995","DOE SEER2 standards","ASHRAE 15","EPA 608"],
  sheets=["D-101 Detail Drawing","R-101 Refrigeration Diagram"]),
 dict(name="Ceiling Fan", group="Climate", style="Ceiling Fan",
  history=("Ceiling fans cooled 19th-century America before air conditioning - the 1882 "
   "Schuyler Wheeler electric fan and Philip Diehl's 1887 sewing-machine-motor fan. The form "
   "hasn't changed: motor, downrod, blades."),
  layout=("Mounting bracket at the ceiling box; downrod (length per ceiling height); motor housing; "
   "blades (4-5) at 7-plus feet above the floor; wall or remote control."),
  structure=("The ceiling box must be fan-rated (it holds 50-plus pounds of wobbling load); "
   "downrod sized so blades clear 7 feet; blade pitch (12-15 degrees) moves the air."),
  systems=("Motor (AC or DC - DC is quieter and more efficient); reverse switch for winter "
   "(clockwise, low speed, redistributes warm air); remote/wall control."),
  spaces=[("Blade Sweep",52,52),("Downrod",12,2),("Motor",10,8)],
  materials=["Fan-rated box","Downrod","Motor",
   "Balanced blades","Remote control","Light kit (optional)"],
  codes=["UL 507","NEC 314.27 fan boxes","ENERGY STAR"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Toaster Oven", group="Kitchen", style="Countertop Toaster Oven",
  history=("Toaster ovens brought broiling to the countertop in the 1960s-70s: quartz or calrod "
   "elements top and bottom, a small insulated cavity, and convection fans in modern versions. "
   "The air-fryer era is just a toaster oven with better marketing."),
  layout=("Insulated cavity with rack positions; heating elements top and bottom; control panel "
   "front; crumb tray below; convection fan at rear in better models."),
  structure=("Double-wall insulated shell; door with tempered glass; the cavity small enough that "
   "elements heat it fast. Countertop clearances for the hot shell."),
  systems=("Element control (often electronic now); convection fan; timer with auto-shutoff; the "
   "safety system is the thermal cutoff."),
  spaces=[("Cavity",16,12),("Footprint",18,14),("Door Open",18,12)],
  materials=["Quartz/calrod elements","Insulated shell","Tempered glass door",
   "Convection fan","Electronic controls","Crumb tray"],
  codes=["UL 1026","DOE standards"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="Vacuum Cleaner", group="Home", style="Upright/Canister Vacuum",
  history=("Vacuums went from 1901 Booth's horse-drawn 'Puffing Billy' to Hoover's 1908 upright "
   "to Dyson's 1990s bagless cyclone. The physics never changed: move air fast through a "
   "cleaning head, separate the dirt."),
  layout=("Cleaning head with brushroll; dirt path (bag or cyclonic bin); motor and fan; filters "
   "(HEPA in good ones); handle and controls. Cordless sticks put the motor in the hand."),
  structure=("The air path is the structure - every joint sealed or suction dies; the brushroll "
   "bearings are the wear item."),
  systems=("Motor/fan creating sealed suction (inches of water); cyclonic or bag separation; HEPA "
   "filtration; brushroll drive. Battery management in cordless models."),
  spaces=[("Cleaning Head",12,10),("Body",16,12),("Handle",36,4)],
  materials=["Motor/fan","Cyclonic bin","HEPA filter",
   "Brushroll","Sealed air path","Battery (cordless)"],
  codes=["UL 1017","IEC 60312","CARB (cordless)"],
  sheets=["D-101 Detail Drawing"]),
 dict(name="LED Lamp", group="Home", style="LED Desk/Floor Lamp",
  history=("LED lighting - Nakamura's 1990s blue LED completing the set - replaced a century of "
   "hot filaments with cool diodes. The lamp became a thermal and optical device: heatsink, "
   "driver, diffuser."),
  layout=("Base with driver; articulated arm or fixed stem; head with LED array, heatsink, and "
   "diffuser; switch or touch control on head or base."),
  structure=("The heatsink is the structure - LED life is temperature; the arm needs joints that "
   "hold position; the base must not tip with the arm extended."),
  systems=("Constant-current driver (flicker-free in good ones); dimming (beware incompatible "
   "dimmers); color temperature selection in modern lamps."),
  spaces=[("Base",8,8),("Arm Reach",24,4),("Head",8,5)],
  materials=["LED array","Heatsink","Constant-current driver",
   "Diffuser","Articulated arm","Touch controls"],
  codes=["UL 153","FCC Part 15","DOE lighting standards","Title 24 JA8"],
  sheets=["D-101 Detail Drawing"]),
]

VEHICLES = [
 dict(name="Sedan", group="Road", style="Midsize Sedan",
  history=("The sedan - enclosed, four doors, separate trunk - became the default car in 1920s "
   "America as closed bodies got cheap. Unibody construction (Budd's work, 1930s-60s) replaced "
   "body-on-frame for cars, making the body the structure."),
  layout=("Engine bay forward; passenger cabin with two rows; trunk aft; fuel tank under the rear "
   "seat; crumple zones front and rear around the rigid safety cell."),
  structure=("Unibody: stamped steel panels welded into a structural shell; the safety cell around "
   "passengers with crumple zones fore and aft. Crash-tested to federal standards."),
  systems=("Powertrain (ICE, hybrid, or EV); suspension and steering; braking with ABS/stability "
   "control; HVAC; the ADAS sensor suite in modern cars."),
  spaces=[("Overall",190,72),("Cabin",100,60),("Trunk",40,50),("Engine Bay",40,55)],
  materials=["Unibody steel","Powertrain","Suspension",
   "Safety cell","ADAS sensors","HVAC"],
  codes=["FMVSS","EPA emissions/fuel economy","IIHS ratings","SAE standards"],
  sheets=["M-101 General Arrangement"]),
 dict(name="Pickup Truck", group="Road", style="Full-Size Pickup",
  history=("Pickups grew from 1920s Model T conversions to America's best-selling vehicles. "
   "Body-on-frame survived in trucks because the frame carries the load - the bed, the trailer, "
   "the work."),
  layout=("Cab (regular, extended, or crew) forward; bed aft with wheelhouses; frame rails full "
   "length; fuel tank amidships; tow hitch at the rear."),
  structure=("Ladder frame of boxed steel - the truck's backbone; cab and bed bolt on. Payload and "
   "tow ratings are structural ratings."),
  systems=("V8/diesel/EV powertrain options; 4WD transfer case; trailer brake controller and tow "
   "package; bed and tailgate utility systems."),
  spaces=[("Overall",230,80),("Crew Cab",70,70),("Bed 5.5ft",67,60),("Frame Rails",200,36)],
  materials=["Boxed ladder frame","Cab and bed","Tow package",
   "4WD system","Bed liner","Trailer brake controller"],
  codes=["FMVSS","EPA","SAE J2807 towing"],
  sheets=["M-101 General Arrangement"]),
 dict(name="Box Truck", group="Work", style="Box Truck / Step Van",
  history=("Box trucks - cab plus rectangular cargo box - are the workhorses of local delivery, "
   "descended from 1920s panel trucks. The step van (bread-truck form) optimized the driver's "
   "in-and-out all day."),
  layout=("Cab forward with walk-through to the box; box with roll-up rear door and curbside door; "
   "chassis rails beneath; fuel and DEF tanks amidships."),
  structure=("Chassis cab plus separate box - the box is non-structural cargo volume on a truck "
   "frame. Box of aluminum or FRP panels on steel posts."),
  systems=("Diesel or gas powertrain; liftgate options; cargo lighting and tie-downs; telematics "
   "for fleets."),
  spaces=[("Overall",260,96),("Box 16ft",192,96),("Cab",80,90),("Chassis",240,36)],
  materials=["Truck chassis","Aluminum/FRP box","Roll-up door",
   "Liftgate","Cargo tie-downs","Telematics"],
  codes=["FMVSS","DOT commercial","NEC n/a"],
  sheets=["M-101 General Arrangement"]),
 dict(name="City Bus", group="Road", style="Transit Bus",
  history=("City buses replaced streetcars in mid-1900s America; the GM 'old-look' and 'New Look' "
   "buses defined the form. Low-floor buses (1990s) and now battery-electric buses continue the "
   "evolution."),
  layout=("Driver station forward left; entry doors (front, sometimes middle/rear); passenger cabin "
   "with priority seating; wheelchair positions with securement; engine or battery bay at rear."),
  structure=("Integral or body-on-chassis; low-floor designs drop the floor between the wheels. "
   "The bus is a rolling public building - durability is structural."),
  systems=("Diesel/CNG/hybrid/battery-electric drivetrains; kneeling suspension; stop-request and "
   "annunciation; fare collection; wheelchair ramp or lift."),
  spaces=[("Overall",480,102),("Cabin",400,96),("Driver Station",40,40),("Wheelchair Bays",60,50)],
  materials=["Bus body structure","Low-floor chassis","Drivetrain",
   "Fare system","Accessibility equipment","Telematics"],
  codes=["FMVSS","ADA transit","FTA Buy America"," Altoona testing"],
  sheets=["M-101 General Arrangement"]),
 dict(name="Sailboat", group="Water", style="Cruising Sailboat",
  history=("Sailboats are humanity's oldest vehicles - Egyptian reed boats, Viking longships. The "
   "modern cruising sloop (masthead rig, fin keel, spade rudder) was refined in the 1960s-70s "
   "fiberglass revolution."),
  layout=("Bow with anchor locker; foredeck; cabin trunk with V-berth forward, salon amidships, "
   "galley and head; cockpit aft with helm; engine under the companionway; keel below, rudder aft."),
  structure=("Fiberglass (or wood/steel/aluminum) hull as a monocoque; keel bolted through the "
   "hull grid; rigging loads carried to chainplates tied into the structure. The hull is the "
   "frame."),
  systems=("Standing and running rigging; auxiliary diesel with shaft or saildrive; DC/AC "
   "electrical with charging; plumbing (head, galley, bilge); navigation electronics."),
  spaces=[("Hull 35ft",420,132),("Cabin",240,110),("Cockpit",96,90),("Keel",72,12)],
  materials=["Fiberglass hull","Lead/iron keel","Aluminum mast",
   "Standing rigging","Auxiliary diesel","Navigation electronics"],
  codes=["ABYC standards","USCG requirements","CE marking","ISO 12215"],
  sheets=["M-101 General Arrangement","S-101 Sail Plan"]),
 dict(name="Motorboat", group="Water", style="Center-Console Motorboat",
  history=("Motorboats went mainstream with 1950s fiberglass and the outboard motor (Ole Evinrude's "
   "1909 detachable rowboat motor). The center console - helm amidships, walkaround decks - became "
   "the versatile fishing/family form."),
  layout=("Bow deck with seating/storage; center console with helm; cockpit aft; outboard(s) on "
   "the transom; fuel tank under the deck amidships; livewell and fish boxes in fishing versions."),
  structure=("Fiberglass V-hull with stringers and transom built for outboard loads; foam flotation "
   "for level flotation; the transom is the structural heart."),
  systems=("Outboard(s) with remote controls; fuel system with water separation; bilge pumps; "
   "12V electrical with battery management; livewell aeration."),
  spaces=[("Hull 25ft",300,102),("Console",48,36),("Cockpit",96,90),("Bow Deck",96,90)],
  materials=["Fiberglass V-hull","Outboard engine(s)","Fuel system",
   "Bilge pumps","12V electrical","Livewell system"],
  codes=["ABYC standards","USCG flotation","EPA marine engines","NMMA certification"],
  sheets=["M-101 General Arrangement"]),
 dict(name="Small Aircraft", group="Air", style="Four-Seat Piston Single",
  history=("The four-seat piston single - Piper Cherokee (1960), Cessna 172 (1956, still in "
   "production) - taught the world to fly. High-wing or low-wing, fixed gear, 160 horsepower: "
   "the Volkswagen Beetle of the sky."),
  layout=("Engine forward of the firewall; cabin with two rows; wing (high or low) carrying fuel; "
   "empennage aft; fixed tricycle gear. Weight and balance envelope governs loading."),
  structure=("Aluminum semi-monocoque fuselage; wing spar as the structural spine; the type "
   "certificate defines the structure - every rivet is regulated."),
  systems=("Piston engine with propeller; fuel system (gravity or pumped); 12/24V electrical; "
   "avionics (now glass panels); pitot-static instruments."),
  spaces=[("Fuselage 27ft",324,48),("Wingspan 36ft",120,432),("Cabin",96,44),("Engine Bay",48,44)],
  materials=["Aluminum airframe","Piston engine","Propeller",
   "Glass avionics","Fuel system","Fixed landing gear"],
  codes=["14 CFR Part 23","FAA type certificate","ASTM (LSA)"],
  sheets=["M-101 General Arrangement"]),
 dict(name="Tractor-Trailer", group="Work", style="Semi Tractor-Trailer",
  history=("Semi-trucks - tractor plus articulated trailer - scaled with the Interstate Highway "
   "System after 1956. The fifth wheel coupling (invented 1915, perfected 1920s) made the "
   "combination flexible and standard."),
  layout=("Tractor: engine forward, cab with sleeper, fifth wheel over the drive axles; trailer: "
   "53-foot box (dry van, reefer, flatbed) pinned to the fifth wheel; landing gear forward when "
   "unhitched."),
  structure=("Tractor ladder frame; trailer as a stressed box or frame-plus-panels; the fifth wheel "
   "is the joint - kingpin and jaws carrying the trailer's front."),
  systems=("Diesel powertrain (moving to electric); air brakes (the standard); reefer units with "
   "own engines; ELD/telematics mandated."),
  spaces=[("Tractor",240,96),("Trailer 53ft",636,102),("Fifth Wheel Zone",48,60),("Combination",876,102)],
  materials=["Tractor frame","Fifth wheel","53-ft trailer",
   "Air brake system","Reefer unit","ELD/telematics"],
  codes=["FMVSS","DOT hours of service","EPA SmartWay","ELD mandate"],
  sheets=["M-101 General Arrangement"]),
 dict(name="Motorcycle", group="Road", style="Standard Motorcycle",
  history=("Motorcycles - bicycle plus engine - standardized by the 1920s: Harley-Davidson and "
   "Indian in America, Triumph/Norton in Britain, Honda's 1960s CB series globalizing it. The "
   "diamond frame with the engine as a stressed member is the classic layout."),
  layout=("Front fork and wheel; fuel tank over the frame spine; engine central (often structural); "
   "seat; rear swingarm and wheel; handlebars with all controls at hand."),
  structure=("Steel or aluminum frame (or engine-as-frame); suspension front (telescopic fork) and "
   "rear (swingarm with shock); the rider is part of the dynamics."),
  systems=("Engine (now often with rider aids: ABS, traction control, ride modes); chain/belt/shaft "
   "final drive; lighting and instruments."),
  spaces=[("Overall 84in",84,32),("Wheelbase",58,8),("Engine Zone",24,18)],
  materials=["Frame","Engine","Suspension",
   "Final drive","Rider aids (ABS/TC)","Lighting"],
  codes=["FMVSS motorcycle","EPA","DOT helmet (rider)"],
  sheets=["M-101 General Arrangement"]),
 dict(name="Bicycle", group="Road", style="Road/Hybrid Bicycle",
  history=("The safety bicycle - equal wheels, chain drive, diamond frame (1885 Rover) - is the "
   "most efficient vehicle ever made. The modern road/hybrid bike refines it: derailleur gears "
   "(1930s), aluminum/carbon frames, disc brakes."),
  layout=("Diamond frame: top tube, down tube, seat tube, stays; fork and front wheel; handlebar "
   "and stem; saddle on seatpost; wheels with quick-releases; drivetrain (chainrings, chain, "
   "cassette, derailleurs)."),
  structure=("The diamond frame is a truss - every tube in tension or compression; that's why "
   "bicycles are so light and strong. Frame materials: steel, aluminum, carbon, titanium."),
  systems=("Derailleur gearing; rim or disc brakes; the rider is the engine - fit (saddle height, "
   "reach) is the ergonomics."),
  spaces=[("Wheelbase 40in",40,4),("Frame Triangle",24,20),("Wheels 700c",28,28)],
  materials=["Frame (Al/carbon/steel)","Wheels","Drivetrain",
   "Brakes","Saddle and cockpit","Tires and tubes"],
  codes=["CPSC 16 CFR 1512","ISO 4210","EN standards"],
  sheets=["M-101 General Arrangement"]),
 dict(name="RV Camper", group="Work", style="Class C Motorhome",
  history=("RVs grew from 1920s auto-camping trailers to the motorhome industry centered in Elkhart, "
   "Indiana. The Class C - van cab with overcab bunk and box body - is the versatile family "
   "form."),
  layout=("Driver cab forward; overcab bunk; living/dinette amidships; galley; bath; rear bedroom; "
   "basement storage below the floor; utilities (water, waste, propane, electric) in compartments."),
  structure=("Cutaway van chassis plus house body (aluminum/wood frame, fiberglass or metal skin); "
   "the house must flex with the chassis - sealants are structural."),
  systems=("12V DC and 120V AC (shore/generator/solar); propane for cooking/heat/fridge; fresh/gray/"
   "black water; slide-outs in larger units; leveling."),
  spaces=[("Overall 28ft",336,96),("Living",120,90),("Overcab Bunk",80,60),("Bath",48,40)],
  materials=["Van chassis","House body","Slide-out mechanisms",
   "12V/120V electrical","Propane system","Water systems","Leveling jacks"],
  codes=["NFPA 1192","ANSI A119.5","FMVSS (chassis)"],
  sheets=["M-101 General Arrangement"]),
 dict(name="Fire Truck", group="Work", style="Pumper Fire Apparatus",
  history=("Motorized fire apparatus replaced horse-drawn steamers in the 1910s-20s. The pumper - "
   "pump, water, hose, ladders - standardized around the mid-century American LaFrance and Seagrave "
   "designs; NFPA 1901 now governs every detail."),
  layout=("Cab (crew of 4-6) forward; pump panel amidships; water tank central; hose bed top rear; "
   "compartments for tools, ladders, and medical gear; aerial device on ladder trucks."),
  structure=("Commercial or custom chassis; the body is a tool cabinet on wheels - every compartment "
   "sized to its equipment. Pump and tank are structural loads."),
  systems=("Fire pump (1,000-plus GPM) with PTO; water tank (500-plus gallons); foam system; "
   "emergency lighting and sirens; scene lighting; radio and data."),
  spaces=[("Overall 32ft",384,100),("Cab",96,96),("Pump Module",72,96),("Hose Bed",120,90)],
  materials=["Custom/commercial chassis","Fire pump","Water tank",
   "Compartment body","Emergency lighting","Aerial (ladder trucks)","Foam system"],
  codes=["NFPA 1901","FMVSS","CA Title 13 (where applicable)"],
  sheets=["M-101 General Arrangement"]),
]

INFRASTRUCTURE = [
 dict(name="Suspension Bridge", group="Crossings", style="Suspension Bridge",
  history=("Suspension bridges matured with John Roebling's Niagara (1855) and Brooklyn (1883) "
   "bridges; the Golden Gate (1937) proved the long span. The form - main cables, suspenders, "
   "stiffening truss - now spans nearly 2 miles at the Canakkale 1915 bridge (2022)."),
  layout=("Two towers with anchorages beyond; main cables draped over tower saddles; suspenders "
   "hanging the deck; stiffening truss or box girder deck; approach spans to the abutments."),
  structure=("Main cables of parallel steel wire (spun in place); towers of steel or concrete; "
   "anchorages holding the cable pull (often massive concrete); the deck stiffened against wind - "
   "the Tacoma Narrows lesson (1940)."),
  systems=("Deck dehumidification (cable preservation); wind monitoring; traveler/cable inspection "
   "systems; lighting and de-icing where needed."),
  spaces=[("Main Span",4200,90),("Tower",700,60),("Anchorage",150,120),("Approach",1500,90)],
  materials=["Main cables (steel wire)","Steel/concrete towers","Suspenders",
   "Stiffening truss","Anchorages","Dehumidification"],
  codes=["AASHTO LRFD","FHWA bridge standards","Wind engineering practice"],
  sheets=["S-101 General Arrangement","S-201 Tower Details"]),
 dict(name="Concrete Dam", group="Water", style="Concrete Gravity Dam",
  history=("Concrete gravity dams - Hoover (1936), Grand Coulee (1942) - hold water by sheer mass. "
   "The arch dam (thinner, pushing into canyon walls) and buttress variants suit narrower sites; "
   "gravity suits wide valleys."),
  layout=("Crest with roadway; upstream face vertical or battered; downstream face sloped; spillway "
   "(gated or uncontrolled) in or beside the dam; powerhouse at the toe; galleries inside for "
   "inspection and drainage."),
  structure=("Mass concrete in lifts with cooling (Hoover's cooling pipes are famous); the dam's "
   "weight resists the water's push - stability against overturning and sliding governs. "
   "Foundation grouting seals seepage."),
  systems=("Spillway gates and controls; powerhouse with turbines; drainage galleries with weirs "
   "monitoring seepage; instrumentation (plumb lines, piezometers) watching the dam forever."),
  spaces=[("Dam Axis",1244,45),("Crest",1244,30),("Spillway",500,80),("Powerhouse",400,120)],
  materials=["Mass concrete","Foundation grouting","Spillway gates",
   "Turbines and generators","Instrumentation","Drainage galleries"],
  codes=["USBR design standards","FERC dam safety","USACE EM 1110"],
  sheets=["S-101 General Arrangement","S-301 Sections"]),
 dict(name="Highway Interchange", group="Transport", style="Freeway Interchange",
  history=("Interchanges - the cloverleaf (1929, Woodbridge NJ), then directional and stack designs "
   "- are where freeways meet. The four-level stack is the ultimate form: every movement on its "
   "own bridge, no weaving."),
  layout=("Mainline freeways crossing; ramps for each turning movement; bridges carrying ramps over "
   "the mainlines; the footprint often a quarter-mile square. Design speed of ramps sets the "
   "curves."),
  structure=("Bridges: prestressed concrete or steel girders on single or bent piers; retaining "
   "walls where ramps climb; the whole interchange is a bridge project more than a road."),
  systems=("Drainage (interchanges are all pavement); lighting (high-mast); signage structures; "
   "ramp metering signals; ITS sensors and cameras."),
  spaces=[("Mainline A",2000,120),("Mainline B",2000,120),("Ramp Bridges",800,40),("Footprint",1400,1400)],
  materials=["Bridge girders","Piers and bents","Retaining walls",
   "High-mast lighting","Sign structures","Ramp meters"],
  codes=["AASHTO Green Book","AASHTO LRFD bridges","MUTCD"],
  sheets=["C-101 Geometric Plan","S-101 Bridge Plans"]),
 dict(name="Railway Tunnel", group="Crossings", style="Bored Rail Tunnel",
  history=("Rail tunnels - the 1826 Wapping Tunnel, then Alpine bores like the Gotthard (1882, "
   "2016 base tunnel) - conquered mountains and water. TBMs (tunnel boring machines) made "
   "long bores routine; the Channel Tunnel (1994) proved undersea rail."),
  layout=("Twin bores (one track each) with cross-passages every few hundred meters; portals with "
   "cut-and-cover approaches; ventilation and emergency egress shafts; the TBM launch site."),
  structure=("Segmental concrete lining erected by the TBM; cross-passages mined; portals of "
   "retained cut. Ground support matched to geology - the tunnel is designed from the borehole "
   "data."),
  systems=("Ventilation (piston effect plus fans); emergency walkways and cross-passages; fire "
   "detection and suppression; traction power; signaling and communications; drainage pumping."),
  spaces=[("Bore A",20000,30),("Bore B",20000,30),("Cross-Passages",30,15),("Portal Works",500,200)],
  materials=["TBM","Segmental lining","Cross-passage structures",
   "Ventilation","Traction power","Fire/life safety"],
  codes=["NFPA 130","AREMA","FTA guidelines"],
  sheets=["C-101 Alignment Plan","S-101 Tunnel Sections"]),
 dict(name="Water Treatment Plant", group="Water", style="Surface Water Treatment Plant",
  history=("Modern water treatment - coagulation, sedimentation, filtration, disinfection - "
   "crystallized in the early 1900s and ended waterborne disease in cities. The conventional "
   "plant layout hasn't changed in a century, only refined."),
  layout=("Intake and raw-water pumping; rapid mix and flocculation basins; sedimentation basins; "
   "filters; clearwell and disinfection; chemical storage and feed; residuals handling; "
   "administration and lab."),
  structure=("Basins of watertight reinforced concrete below and above grade; the filter building "
   "and chemical areas need corrosion-resistant detailing; clearwell as a buried reservoir."),
  systems=("Chemical feed (coagulant, chlorine, fluoride); filter backwash; SCADA control of the "
   "whole train; lab for compliance testing; standby power for the high-service pumps."),
  spaces=[("Floc/Sed Basins",120,60),("Filters",80,40),("Clearwell",100,60),("Chemical Building",60,30),
   ("Lab/Admin",40,25),("Residuals",60,30)],
  materials=["Concrete basins","Filter media","Chemical feed systems",
   "SCADA","Lab equipment","Standby power"],
  codes=["Ten States Standards","SDWA","AWWA standards","NEC 2023"],
  sheets=["P-101 Process Flow","C-101 Site Plan"]),
 dict(name="Electrical Substation", group="Energy", style="Air-Insulated Substation",
  history=("Substations - where high voltage is transformed and switched - grew with the AC grid "
   "after 1890s. The air-insulated switchyard (busbars, breakers, transformers on gravel) is the "
   "classic form; gas-insulated switchgear shrinks it for cities."),
  layout=("Incoming lines on dead-end structures; busbars; breakers and disconnects per bay; power "
   "transformers with fire walls and oil containment; control house; the yard fenced with "
   "clearances per voltage."),
  structure=("Steel take-off structures; transformer foundations with oil containment pits; control "
   "house (often blast/EM-shielded); the ground grid under everything - safety is buried copper."),
  systems=("Protective relaying (the substation's brain); SCADA; station battery and DC system; "
   "fire protection for transformers; security (fences, cameras) per NERC."),
  spaces=[("Switchyard",200,150),("Transformers",60,40),("Control House",30,20),("Busbars",180,30)],
  materials=["Power transformers","Circuit breakers","Busbar structures",
   "Protective relays","Ground grid","Oil containment","Security fencing"],
  codes=["IEEE C37","NESC","NERC CIP","NEC 2023 Art 490"],
  sheets=["E-101 One-Line","E-201 Yard Plan"]),
 dict(name="Airport Terminal", group="Transport", style="Airport Passenger Terminal",
  history=("Airport terminals evolved from 1930s art-deco halls to today's processors: curbside, "
   "check-in, security, concourse, gates. The unit terminal with piers (1950s-60s) and the "
   "transporter/midfield concepts all serve the same flow."),
  layout=("Landside: curbs, check-in hall, security checkpoint; airside: concourse with gates, "
   "holdrooms, concessions; baggage systems below or behind; apron and taxiways beyond. "
   "Passenger flow never crosses baggage flow."),
  structure=("Long-span terminal roof (often the architectural signature); the concourse as a "
   "bridge-like structure; baggage handling in the undercroft. Seismic and blast design per "
   "airport standards."),
  systems=("Baggage handling (miles of conveyors); security screening; flight information; "
   "jet bridges; apron fueling and services; the terminal is a small city of systems."),
  spaces=[("Check-in Hall",300,80),("Concourse",600,60),("Holdrooms",200,40),("Baggage Hall",200,60),
   ("Curbside",400,40)],
  materials=["Long-span roof","Curtain wall","Baggage handling system",
   "Jet bridges","Security equipment","Flight displays"],
  codes=["IBC assembly","FAA AC 150","NFPA 415","ADA airports"],
  sheets=["A-101 Floor Plan","S-101 Roof Structure"]),
 dict(name="Cell Tower", group="Energy", style="Monopole Communications Tower",
  history=("Cell towers - the visible network - multiplied with cellular telephony from the 1980s. "
   "The monopole (single tapered steel pole) replaced lattice towers in most suburban sites; "
   "macro sites now share with small cells and DAS."),
  layout=("Tower with antenna arrays at the top (sectors); equipment shelter or cabinets at the "
   "base; generator; fenced compound with access road. Fall zone and setbacks govern siting."),
  structure=("Tapered steel monopole on a drilled pier or spread footing; antennas on mounts with "
   "wind and ice loading per TIA-222; the foundation resists the overturning moment."),
  systems=("Radios (often at the tower top now); fiber backhaul; backup power (battery plus "
   "generator); FAA lighting where required; remote monitoring."),
  spaces=[("Tower 150ft",8,8),("Compound",50,50),("Shelter",12,20),("Generator",8,6)],
  materials=["Tapered monopole","Antenna mounts","Radios and antennas",
   "Equipment shelter","Backup power","Fiber backhaul"],
  codes=["ANSI/TIA-222","FAA lighting","NEC 2023","Local zoning"],
  sheets=["S-101 Tower Details","E-101 Power Plan"]),
 dict(name="Sewer Lift Station", group="Water", style="Wastewater Lift Station",
  history=("Lift stations pump sewage uphill where gravity can't - every hilly city's hidden "
   "infrastructure. The wet-well/dry-well and the submersible (wet-well only) stations are the "
   "two standard forms."),
  layout=("Wet well receiving gravity sewers; pumps (dry-pit beside or submersible within); valve "
   "vault; control panel; standby generator; odor control; all-weather access for pump trucks."),
  structure=("Wet well of watertight concrete; valve vault; the superstructure minimal - often just "
   "a control building. Buoyancy design for the buried structures."),
  systems=("Duplex or triplex pumps with alternation; level control; standby power (full load); "
   "SCADA alarming to the utility; odor control (carbon or biofilter)."),
  spaces=[("Wet Well",15,12),("Valve Vault",12,10),("Controls",8,8),("Generator",10,8)],
  materials=["Wastewater pumps","Level controls","Watertight concrete",
   "Standby generator","Odor control","SCADA alarming"],
  codes=["Ten States Standards","NFPA 820","NEC 2023 Class I Div 2 (wet well)"],
  sheets=["M-101 General Arrangement","P-101 Piping Plan"]),
 dict(name="Solar Farm Array", group="Energy", style="Utility Solar Farm",
  history=("Utility solar farms scaled from 1980s California SEGS plants to today's gigawatt "
   "deserts: rows of PV on single-axis trackers, inverters, and transformers feeding the grid. "
   "The layout is pure geometry - sun angles and row spacing."),
  layout=("PV blocks on trackers or fixed tilt; inverter stations central to blocks; collection "
   "lines to the substation; access roads on a grid; fencing and gates; O&M building at entry."),
  structure=("Driven piles or ground screws per geotech; tracker torque tubes on posts; the "
   "modules are the weather surface. Wind (uplift) governs the foundation design."),
  systems=("Inverters (string or central); transformers; SCADA monitoring per string; vegetation "
   "management (often sheep!); the substation interconnect."),
  spaces=[("PV Block",800,400),("Inverter Station",20,12),("Substation",60,40),("O&M Building",30,20)],
  materials=["PV modules","Single-axis trackers","Driven piles",
   "Inverters","Transformers","SCADA","Fencing"],
  codes=["NEC 690 solar","IEEE 1547 interconnection","UL 2703 racking","Local grading"],
  sheets=["E-101 Array Plan","C-101 Grading Plan"]),
 dict(name="Wind Farm", group="Energy", style="Onshore Wind Farm",
  history=("Wind farms - dozens to hundreds of turbines - grew from 1980s California passes "
   "(Altamont, Tehachapi) to the Great Plains giants. The farm is a power plant spread over "
   "miles: turbines, roads, and collection lines."),
  layout=("Turbines on ridges or grid spacing; access roads to each pad; collection system "
   "(underground) to the substation; O&M building; met towers. Spacing: 3-5 diameters "
   "crosswind, 5-10 downwind."),
  structure=("Each turbine as in the single-turbine record; the farm adds roads (crane-worthy), "
   "collection trenching, and the substation. Foundations per turbine geotech."),
  systems=("Collection system to substation; SCADA for the fleet; curtailment and grid compliance; "
   "bat/bird monitoring and mitigation."),
  spaces=[("Turbine Pad",80,60),("Access Roads",5000,20),("Substation",80,50),("O&M Building",40,25)],
  materials=["Turbines","Collection system","Access roads",
   "Substation","SCADA","Met towers"],
  codes=["IEC 61400","IEEE 1547","FAA","Wildlife guidelines"],
  sheets=["C-101 Layout Plan","E-101 Collection Plan"]),
 dict(name="Canal Lock", group="Water", style="Navigation Lock",
  history=("Locks - the pound lock perfected in 14th-century Europe, scaled by 19th-century "
   "canals - lift boats over elevation. The Panama Canal's 1914 locks and the 2016 neo-Panamax "
   "locks are the masterpieces of the form."),
  layout=("Lock chamber with miter gates at each end; approach walls guiding vessels; culverts and "
   "valves filling/emptying the chamber; control house overlooking; the dam or weir holding the "
   "upper pool beside it."),
  structure=("Chamber walls of mass concrete (or sheet pile in soft ground); miter gates of steel; "
   "the chamber floor and culverts as one watertight structure. Gates are the moving machinery."),
  systems=("Gate and valve machinery (hydraulic); filling/emptying hydraulics designed to not "
   "turbulence the vessel; controls and signaling; dewatering for maintenance."),
  spaces=[("Chamber 600ft",600,110),("Gates",40,110),("Approach Walls",400,60),("Control House",20,15)],
  materials=["Mass concrete chamber","Miter gates","Gate machinery",
   "Culvert valves","Controls","Dewatering system"],
  codes=["USACE EM 1110 locks","PIANC guidelines"],
  sheets=["S-101 General Arrangement","M-101 Gate Details"]),
]
