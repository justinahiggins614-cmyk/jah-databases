#!/usr/bin/env python3
"""Entries for the Railway Systems database pair (5,000-target program).

Dedupe gate: all 68 titles checked against the WHOLE system with
code/dedupe_gate.py BEFORE writing. ID prefixes JAH-RLSY- (public) and
JAH-RLSYS- (signature) verified free: zero hits in manifest id_prefix values
(exact + substring) and zero hits in shard record IDs.

34 records per edition, ladder-ordered 1-34 (Foundations 1-12 / Compounded
13-23 / Advanced 24-34).
"""


def R(t, tier, rank, desc, how, kp, req, std, cit, dk, data):
    return {'t': t, 'tier': tier, 'rank': rank, 'desc': desc, 'how': how,
            'kp': kp, 'req': req, 'std': std, 'cit': cit, 'dk': dk, 'data': data}


PUB = [
R("What Railway Systems Are — Industry Overview", "Foundations", 1,
  "Railway systems are the networks that move people and freight on steel rails: track, trains, signals, stations, and the organizations that run them. "
  "Rail is the most energy-efficient way to move heavy goods over land and a backbone of passenger transport in much of the world. "
  "Every railway, from a mountain narrow-gauge line to a high-speed main line, runs on the same fundamentals: a guided path, powered vehicles, safe separation of trains, and a timetable.",
  "Steel wheels roll on steel rails with very low friction, so one locomotive can pull thousands of tonnes; flanges on the wheels keep them guided on the track. "
  "Signals and interlockings keep trains separated, timetables schedule their paths, and crews operate and maintain the whole system. "
  "Freight railroads earn by the tonne-kilometer, passenger railways by the seat filled, and both live or die on reliability and safety.",
  ["Steel wheel on steel rail: low friction moves heavy loads efficiently.",
   "Guidance by flange keeps trains on the path without steering.",
   "Signals keep trains separated; timetables schedule their paths.",
   "Freight earns by tonne-kilometer, passengers by seats filled."],
  ["A defined network of track with compatible gauge and loading gauge.",
   "Rolling stock matched to the track and the traffic.",
   "Signaling, timetabling, and trained crews."],
  ["Trains separated by signaled blocks or equivalent protection.",
   "Track inspected and maintained to standard.",
   "Crews qualified on the routes they operate."],
  ["UIC (International Union of Railways) leaflets on railway operations (public standards).",
   "Railway engineering textbooks on track and vehicle fundamentals (public publications)."],
  "braking", {"v_kmh": 100.0, "decel": 0.9}),

R("Track — Rails, Sleepers, and Ballast", "Foundations", 2,
  "Railway track is the engineered path trains run on: two steel rails held at exact gauge by sleepers (ties), sitting in ballast stone that spreads the load and drains water. "
  "The rail's profile - its cross-section shape - carries the wheel, resists wear, and guides the flange. "
  "Track is a structure as surely as a bridge: it must hold tonnes at speed, thousands of times a day, for decades.",
  "Rails are rolled in long lengths and welded into continuous strings, fastened to sleepers with clips that hold gauge under load. "
  "Sleepers of concrete, wood, or steel space the rails and pass loads into the ballast, a deep bed of crushed stone that is tamped to level and lined to alignment. "
  "Geometry cars measure gauge, level, and alignment; tamping machines lift and pack the ballast back to spec where it has settled.",
  ["Rails carry and guide; sleepers hold gauge; ballast spreads load and drains.",
   "Continuous welded rail eliminates joints and the pounding they cause.",
   "Track geometry - gauge, level, alignment - is measured and maintained.",
   "Ballast is tamped and lined back to spec as it settles."],
  ["Rails, fastenings, sleepers, and ballast to specification.",
   "A formation (earthworks) that drains and stays stable.",
   "Tamping and geometry measurement capability."],
  ["Gauge, cant, and alignment within tolerance for the line speed.",
   "Rail defects inspected by ultrasonic or visual regimes.",
   "Drainage maintained so the formation never softens."],
  ["UIC leaflets on track construction and maintenance (public standards).",
   "AREMA Manual for Railway Engineering, track chapter (public industry guidance)."],
  "cant", {"v_kmh": 120.0, "radius_m": 800.0}),

R("Track Gauge", "Foundations", 3,
  "Track gauge is the distance between the inner faces of the two rails, and it decides which trains can run on a line. "
  "Standard gauge - 1435 mm - dominates the world, but broad and narrow gauges persist where history or terrain chose them. "
  "Gauge is destiny: a train built for one gauge cannot run on another without special variable-gauge equipment or a bogie change.",
  "The gauge is set when the track is built and held by the sleepers and fastenings; gauge-widening on sharp curves eases the wheelsets around. "
  "Break-of-gauge stations transfer passengers or freight between gauges - by changing bogies, using variable-gauge axles, or transloading the cargo. "
  "New lines choose gauge deliberately: standard for interoperability, narrow for tight mountain curves, broad for stability and capacity.",
  ["Gauge is the rail-to-rail distance; it decides which trains fit.",
   "Standard gauge (1435 mm) dominates; broad and narrow persist regionally.",
   "Break-of-gauge needs bogie exchange, variable gauge, or transloading.",
   "Curves may widen gauge slightly to ease wheelsets around."],
  ["A gauge decision matched to terrain, traffic, and neighbors.",
   "Rolling stock built or adapted to the chosen gauge.",
   "Break-of-gauge facilities where gauges meet."],
  ["Gauge held within tolerance at all speeds operated.",
   "Loading gauge (vehicle size) coordinated with structure gauge.",
   "Variable-gauge equipment certified before service."],
  ["UIC leaflets on track gauges and loading gauges (public standards).",
   "National track standards for gauge tolerances (public regulations)."],
  "curve", {"cant_mm": 150.0, "radius_m": 800.0}),

R("Wheels and the Wheel-Rail Interface", "Foundations", 4,
  "The wheel-rail interface is where the whole railway meets the ground: a steel wheel's tread rolls on the rail head while its flange guards against derailment. "
  "The contact patch is astonishingly small - about the size of a coin - yet carries tonnes, because steel on steel deforms only microscopically. "
  "Managing that interface - profiles, lubrication, and wear - is one of railroading's central arts.",
  "Wheel treads are coned so the wheelset self-centers on straight track; on curves the outer wheel rides a larger rolling radius, easing the turn. "
  "Flangeway clearance at switches and crossings is kept exact, rail head lubrication cuts curve wear and noise, and worn profiles are re-turned on wheel lathes. "
  "Hollow wear, flats from locked brakes, and cracks are found by inspection and measurement before they become failures.",
  ["Contact patch the size of a coin carries tonnes on steel.",
   "Coned treads self-center; flanges guard at switches.",
   "Profiles wear and are re-turned; lubrication cuts curve wear.",
   "Flats, hollow wear, and cracks are found before they fail."],
  ["Wheel profiles and rail profiles matched by design.",
   "Wheel lathes and profile measurement.",
   "Curve lubrication where wear and noise demand it."],
  ["Wheel and rail defect limits enforced by measurement.",
   "Flangeway clearances held at switches and crossings.",
   "Lubricants kept off the rail head where braking needs friction."],
  ["UIC leaflets on wheel and rail profiles (public standards).",
   "Railway tribology literature on the wheel-rail interface (public publications)."],
  "axle", {"wagon_t": 80.0, "axles": 4}),

R("Couplers — Joining Cars", "Foundations", 5,
  "Couplers are the mechanical joints that link cars into trains, transmitting the pulling and pushing forces of the locomotive through the whole consist. "
  "The Janney knuckle coupler dominates North America, buffers-and-chain persist in parts of Europe, and Scharfenberg couplers join multiple units. "
  "A coupler failure at speed can part a train, so their strength and inspection matter enormously.",
  "Knuckle couplers lock automatically when cars are pushed together and release by a lever; draft gear behind each coupler absorbs the shock of slack run-in and run-out. "
  "Air brake hoses and, on passenger trains, electrical and heating connections are coupled alongside the mechanical joint. "
  "Crews inspect knuckles, pins, and draft gear for cracks and wear, and broken knuckles are replaced before the car moves again.",
  ["Couplers transmit traction and braking forces through the train.",
   "Knuckle couplers lock on push-together; draft gear absorbs slack shocks.",
   "Air hoses couple with the mechanical joint; passenger trains add electrical links.",
   "A failed coupler can part a train - inspection is critical."],
  ["Couplers of compatible type and rating across the fleet.",
   "Draft gear maintained to absorb buff and draft forces.",
   "Spare knuckles and the tools to change them."],
  ["Coupler inspections on a defined cycle, cracks condemned.",
   "Mixed coupler types only with approved adapters.",
   "Air hoses tested with the brake test before departure."],
  ["AAR standards for couplers and draft gear (public industry standards).",
   "UIC leaflets on buffers, drawgear, and couplers (public standards)."],
  "energy", {"mass_t": 2000.0, "v_kmh": 80.0}),

R("Braking Systems", "Foundations", 6,
  "Train brakes must stop thousands of tonnes reliably, and they do it with air: the automatic air brake applies on every car when pressure drops, so a parted hose stops the train instead of dooming it. "
  "That fail-safe principle - loss of pressure means brakes on - has protected railways for over 150 years. "
  "Modern additions include dynamic braking, which turns traction motors into generators, and electronic controlled pneumatic brakes for instant, uniform application.",
  "The locomotive's compressor charges the brake pipe running the train's length; each car has a reservoir and a triple valve that applies its brakes when pipe pressure falls. "
  "The engineer reduces pipe pressure to apply and recharges to release; graduated release and dynamic blending refine control. "
  "Brake tests before departure verify every car applies and releases, because one dead car lengthens the stopping distance for all.",
  ["Fail-safe by design: pressure loss applies the brakes.",
   "One brake pipe commands every car in the train.",
   "Dynamic braking saves friction brakes on long descents.",
   "Departure brake tests verify every car before moving."],
  ["Air compressors, reservoirs, and triple valves maintained.",
   "Brake shoes or pads and discs within wear limits.",
   "Dynamic brake grids where grades demand them."],
  ["Brake tests before every departure, documented.",
   "Piston travel and shoe thickness within limits.",
   "Handbrakes applied on parked cuts per the rules."],
  ["AAR and UIC brake system standards (public industry standards).",
   "National brake-test regulations (public regulations)."],
  "braking", {"v_kmh": 80.0, "decel": 0.7}),

R("Diesel Locomotives", "Foundations", 7,
  "Diesel locomotives are self-powered workhorses: a diesel engine drives a generator or alternator, and electric traction motors turn that power into pulling force at the wheels. "
  "This diesel-electric arrangement lets the engine run at efficient speeds while the motors deliver huge starting torque. "
  "Freight railroads run thousands of them, often coupled in multiples for heavy trains.",
  "Fuel feeds the prime mover; its crankshaft spins the main generator producing electricity for the traction motors on each axle. "
  "Dynamic braking reverses the motors into generators, dumping energy into resistor grids on long downgrades. "
  "Multiple-unit control lets one crew run several locomotives as one, and distributed power places units mid-train or at the rear for long, heavy consists.",
  ["Diesel-electric: engine makes electricity, motors pull.",
   "Huge starting torque from electric traction motors.",
   "Dynamic braking turns motors into generators on descents.",
   "Multiple-unit and distributed power multiply pulling force."],
  ["Fuel, lube oil, and cooling capacity for the duty cycle.",
   "Traction motors, generators, and control electronics maintained.",
   "Sand for adhesion in slippery conditions."],
  ["Emissions per applicable locomotive standards.",
   "Daily inspections: fluids, brakes, safety devices.",
   "Event recorders ('black boxes') functional."],
  ["AAR locomotive standards (public industry standards).",
   "EPA locomotive emission regulations (public regulations)."],
  "energy", {"mass_t": 4000.0, "v_kmh": 65.0}),

R("Electric Locomotives and Catenary", "Foundations", 8,
  "Electric locomotives draw power from overhead catenary wire or third rail instead of carrying fuel, giving instant high power, clean operation, and regenerative braking that feeds energy back to the grid. "
  "The catenary - the zigzag overhead wire system - is the locomotive's fuel line, held at precise height and tension. "
  "Electrification costs heavily up front but pays back on busy lines through lower energy and maintenance costs.",
  "The pantograph presses against the contact wire, drawing high-voltage AC or DC to transformers and traction converters feeding the motors. "
  "Regenerative braking returns energy to the wire for other trains to use; phase breaks and neutral sections separate electrical sections. "
  "Catenary is tensioned to stay level across temperatures, with overlaps and section insulators letting maintenance isolate parts of the line.",
  ["Power from the wire: high power, no fuel carried, regenerative braking.",
   "The pantograph-contact wire interface is the critical contact.",
   "Catenary tensioned and leveled across temperatures.",
   "High build cost, low running cost: electrify the busy lines."],
  ["Catenary or third rail built and maintained to spec.",
   "Substations feeding the sections with protection.",
   "Locomotives with pantographs, transformers, converters."],
  ["Electrical clearances and isolation procedures for worker safety.",
   "Pantograph and wire wear monitored; dewirement prevented.",
   "Regenerative energy managed so the grid accepts it."],
  ["UIC leaflets on electrification systems (public standards).",
   "Electrical safety regulations for railways (public regulations)."],
  "energy", {"mass_t": 1500.0, "v_kmh": 160.0}),

R("Passenger Cars", "Foundations", 9,
  "Passenger cars are the railway's hotels on wheels: coaches for seating, sleepers for nights, diners for meals, all riding on bogies that smooth the track's imperfections. "
  "Modern cars are crashworthy shells with climate control, retention toilets, accessibility features, and information systems. "
  "Comfort is the product; the timetable is the promise; safety is the non-negotiable foundation.",
  "Bodies of steel or aluminum ride on two bogies each, with suspension isolating passengers from track irregularities. "
  "Heating, ventilation, and air conditioning hold the climate; doors with sensitive edges and interlocks protect boarding; retention tanks keep waste off the track. "
  "Accessible cars offer wheelchair spaces, accessible toilets, and boarding aids, and the whole train's systems answer to the crew's controls.",
  ["Comfort is the product; the timetable the promise; safety the foundation.",
   "Bogies and suspension isolate passengers from the track.",
   "Crashworthy bodies, climate control, and interlocked doors.",
   "Accessibility built in: spaces, toilets, boarding aids."],
  ["Cars maintained to the maintenance plan: bogies, brakes, doors, HVAC.",
   "Cleaning and servicing between trips.",
   "Onboard crew trained in service and emergency duties."],
  ["Door interlocks and sensitive edges functional.",
   "Emergency exits, lighting, and communication working.",
   "Accessibility features per applicable regulations."],
  ["UIC and AAR passenger car standards (public industry standards).",
   "Accessibility regulations for rail vehicles (public regulations)."],
  "capacity", {"cars": 8, "seats": 72}),

R("Freight Wagons", "Foundations", 10,
  "Freight wagons are the railway's muscle specialized by cargo: boxcars for general goods, flatcars for machinery, tank cars for liquids, hoppers for bulk, autoracks for vehicles. "
  "Each type maximizes its payload within the axle-load and loading-gauge limits while protecting the cargo. "
  "The wagon fleet is the freight railroad's factory floor - its utilization decides profitability.",
  "Bodies matched to cargo ride on two bogies with the specified axle load; brakes, couplers, and bearings are standardized for interchange between railroads. "
  "Loading follows the rules: weight distributed, securement verified, placarded hazmat declared and placed per regulation. "
  "Wagons cycle through loading, hauling, unloading, and maintenance, and dwell time - idle hours - is the enemy of utilization.",
  ["Wagon types specialized by cargo: box, flat, tank, hopper, autorack.",
   "Payload maximized within axle-load and gauge limits.",
   "Interchange standards let wagons run across railroads.",
   "Dwell time is the enemy: keep wagons moving."],
  ["Wagons of the right type, maintained to interchange rules.",
   "Loading and securement per the loading rules.",
   "Hazmat placarding and placement per regulation."],
  ["Brake, bearing, and wheel defect limits enforced.",
   "Overloading prohibited - weigh where required.",
   "Hazmat handled per dangerous-goods regulations."],
  ["AAR interchange rules for freight wagons (public industry rules).",
   "RID/ADR dangerous-goods rail regulations (public regulations)."],
  "axle", {"wagon_t": 100.0, "axles": 4}),

R("Railway Stations", "Foundations", 11,
  "Stations are where the railway meets the people: platforms for boarding, concourses for waiting, and the backstage of crew rooms, signaling, and servicing. "
  "A great station moves thousands per hour without crush or confusion; a poor one turns every departure into a scramble. "
  "Stations are also the railway's shopfronts - their quality shapes the decision to ride.",
  "Platforms are sized for peak crowds with clear markings for train positions and safe yellow lines; concourses separate arriving and departing flows. "
  "Information - departure boards, announcements, mobile updates - tells passengers where to be and when; ticketing, retail, and accessibility services complete the offer. "
  "Behind the scenes, stations host crew sign-on points, stabling for trains, and the signaling that routes them.",
  ["Stations move crowds without crush or confusion.",
   "Platforms sized for peaks, marked for train positions.",
   "Information tells every passenger where to be and when.",
   "The station is the railway's shopfront."],
  ["Platforms, concourses, and vertical circulation for peak flows.",
   "Passenger information and announcement systems.",
   "Ticketing, accessibility, and safety staffing."],
  ["Platform-train interface safe: lighting, markings, staff where needed.",
   "Crowd management plans for peaks and disruptions.",
   "Accessibility: step-free routes, tactile paving, assistance."],
  ["Station design guidance (public industry publications).",
   "Accessibility regulations for stations (public regulations)."],
  "headway", {"speed_kmh": 80.0, "block_km": 2.0}),

R("Railway Math I — Braking Distance and Speed", "Foundations", 12,
  "Railway math begins with the stop: braking distance grows with the square of speed, so doubling speed quadruples the distance needed. "
  "The formula is distance = v squared over 2a, where v is speed and a is the deceleration the brakes can sustain. "
  "Every signal spacing, every speed limit, every timetable margin bows to this square law.",
  "Convert speed to meters per second, square it, and divide by twice the deceleration: a train at 100 km/h (27.8 m/s) braking at 0.9 m/s² needs about 430 meters. "
  "Add the driver's reaction and the brake system's build-up time, plus a safety margin, to get the true signal spacing. "
  "Adhesion limits deceleration - wet leaves on the rail can halve it - which is why autumn timetables carry extra margin.",
  ["Braking distance grows with the square of speed.",
   "d = v²/2a, plus reaction, build-up, and margin.",
   "Adhesion limits deceleration; wet rail demands respect.",
   "Signal spacing is braking distance made physical."],
  ["Known deceleration rates per train type and condition.",
   "Speeds in consistent units before squaring.",
   "Margins for reaction, build-up, and low adhesion."],
  ["Signal spacings proven against worst-case braking.",
   "Speed limits set from the braking math, not from hope.",
   "Low-adhesion seasons carry extra margin."],
  ["Railway braking and signaling engineering texts (public publications).",
   "National signal-spacing standards (public regulations)."],
  "braking", {"v_kmh": 120.0, "decel": 0.9}),
]

PUB += [
R("Block Signaling", "Compounded", 13,
  "Block signaling divides the line into sections - blocks - and allows only one train in a block at a time, enforced by signals the driver must obey. "
  "It is the fundamental safety system of railways: space between trains guaranteed by the infrastructure, not by hope. "
  "Track circuits or axle counters detect each block's occupancy and hold the protecting signal at danger until the block clears.",
  "Each block's entrance has a signal; detection proves the block clear before the signal clears. "
  "Distant signals warn of the stop ahead at braking distance, and overlaps - extra protected track beyond the signal - forgive slight overruns. "
  "Two-aspect, three-aspect, and four-aspect systems trade block length against capacity: more aspects mean shorter blocks and more trains per hour.",
  ["One train per block: separation guaranteed by infrastructure.",
   "Detection (track circuit or axle counter) proves blocks clear.",
   "Distant signals warn at braking distance; overlaps forgive overruns.",
   "More aspects allow shorter blocks and higher capacity."],
  ["Signals, detection, and power supplies per the signaling plan.",
   "Block lengths matched to braking distances at line speed.",
   "Signal sighting verified from the driver's position."],
  ["Signals obeyed absolutely; passed-at-danger events investigated.",
   "Detection failures treated as occupied until proven clear.",
   "Signal maintenance on a defined cycle."],
  ["National signaling principles and standards (public regulations).",
   "UIC leaflets on signaling (public standards)."],
  "headway", {"speed_kmh": 120.0, "block_km": 3.0}),

R("Interlocking", "Compounded", 14,
  "Interlocking is the logic that prevents signals from clearing for conflicting routes: points and signals locked together so no two trains are ever invited into the same space. "
  "It is the railway's referee, once built of levers and rods, now of software and relays. "
  "Every junction, station throat, and crossing is governed by it.",
  "The interlocking holds a model of the track: which routes are set, which points are locked, which blocks are occupied. "
  "A route request is granted only if every element is free and locked; the protecting signals clear, and nothing conflicting can clear until the route releases. "
  "Modern electronic interlockings prove their logic formally, because a software error here could route two trains together.",
  ["Points and signals locked together: no conflicting routes cleared.",
   "The interlocking models the track and grants only safe routes.",
   "Release comes only when the train has passed.",
   "Software interlockings are formally proven safe."],
  ["Interlocking equipment covering every junction and station throat.",
   "Point machines, detection, and signal control wired through it.",
   "Formal safety case for the logic."],
  ["No signal cleared without the interlocking's permission.",
   "Point failures detected and signaled before trains approach.",
   "Software changes re-proven before commissioning."],
  ["National interlocking safety standards (public regulations).",
   "CENELEC railway software safety standards (public standards)."],
  "headway", {"speed_kmh": 60.0, "block_km": 1.5}),

R("Timetables and Scheduling", "Compounded", 15,
  "The timetable is the railway's master plan: every train's path through time and space, scheduled so they meet, pass, and arrive without conflict. "
  "Building one is a vast puzzle of running times, dwell times, connections, and single-track meets. "
  "A good timetable is robust - small delays absorbed, not amplified into network-wide chaos.",
  "Planners compute running times from the physics - acceleration, line speed, braking - add dwell for boarding and meets on single track, and thread the paths through junctions. "
  "Buffer times at key points absorb small delays; connections are protected where the timetable promises them. "
  "Periodic timetables repeat the pattern hourly, making the service memorable, while freight paths are threaded around the passenger pattern.",
  ["Every train's path through time and space, conflict-free by design.",
   "Running times from physics; dwell and meets from operations.",
   "Buffers absorb small delays; robustness is designed in.",
   "Periodic patterns make service memorable."],
  ["Running-time calculations per train type and route.",
   "A scheduling system that detects conflicts.",
   "Timetable margins tuned to actual performance."],
  ["Published times kept or honestly revised.",
   "Connections promised are connections protected.",
   "Safety margins never traded for journey time."],
  ["Timetable planning literature (public publications).",
   "Passenger rights on delays (public regulations)."],
  "runtime", {"dist_km": 240.0, "avg_kmh": 110.0, "stops": 6, "dwell_min": 2.0}),

R("Dispatching and Train Control", "Compounded", 16,
  "Dispatching is the real-time command of the railway: dispatchers route trains, resolve conflicts, and recover from disruption as the day unfolds. "
  "The timetable is the plan; dispatching is the adaptation when reality - a late train, a failed signal, a storm - breaks the plan. "
  "Good dispatchers keep the network fluid; poor ones let one delay cascade into dozens.",
  "The dispatcher watches the whole area on a live diagram, sets routes through the interlockings, and holds or advances trains to protect connections and capacity. "
  "When disruption strikes, they replan: single-line working around a failure, revised passing orders, bus bridges for blocked lines. "
  "Decisions are logged, because the dispatcher carries legal responsibility for the safety of every move authorized.",
  ["The timetable is the plan; dispatching is the adaptation.",
   "Dispatchers route, prioritize, and replan in real time.",
   "Disruption replanned: single-line working, revised meets, alternatives.",
   "Every authorized move logged; the dispatcher answers for safety."],
  ["A control center with a live view of the whole area.",
   "Authority over routes, held and released by rule.",
   "Contingency plans for common failures."],
  ["No unsafe move authorized under pressure.",
   "Fatigue management for safety-critical dispatchers.",
   "Communications recorded and retrievable."],
  ["Railway operations control literature (public publications).",
   "National train-control and dispatcher rules (public regulations)."],
  "headway", {"speed_kmh": 100.0, "block_km": 2.5}),

R("Freight Operations and Yards", "Compounded", 17,
  "Freight yards are where trains are built: cars sorted by destination, assembled into outbound trains, and dispatched to the network. "
  "Hump yards push cars over a crest and let gravity roll them into classification tracks, retarded to coupling speed. "
  "Yard efficiency decides freight transit times more than line speed does - a car spends most of its life waiting in yards.",
  "Inbound trains are inspected, then switched - car by car or cut by cut - into classification tracks per destination. "
  "Outbound trains are assembled, air-tested, crewed, and dispatched; intermodal terminals transfer containers between train and truck. "
  "Yardmasters balance the work: switching capacity, track space, and crew availability against the inbound flow.",
  ["Yards build trains: sort by destination, assemble, dispatch.",
   "Hump yards use gravity; flat yards use switch engines.",
   "Yard time dominates car transit - efficiency here is everything.",
   "Intermodal terminals bridge rail and road."],
  ["Classification tracks, leads, and switching power.",
   "Retarders or skilled crews for safe coupling speeds.",
   "Terminal equipment for containers and trailers."],
  ["Switching speeds and coupling impacts within limits.",
   "Hazmat cars switched and placed per regulation.",
   "Blue-flag protection for workers between cars."],
  ["AAR yard operating practices (public industry guidance).",
   "Hazmat switching and handling regulations (public regulations)."],
  "capacity", {"cars": 60, "seats": 100}),

R("Multiple Units — EMU and DMU", "Compounded", 18,
  "Multiple units are self-propelled trainsets - EMUs electric, DMUs diesel - with driving cabs at both ends and motors distributed along the train. "
  "No locomotive to run around: the driver walks to the other end and drives back, which makes them perfect for frequent suburban and regional services. "
  "Distributed traction also means superb acceleration, cutting station-to-station times.",
  "Each car or pair carries traction equipment - transformers and converters on EMUs, engines and transmissions on DMUs - feeding motors on the bogies. "
  "Units couple together in multiples for peak trains and split for off-peak, matching capacity to demand. "
  "Regenerative or dynamic braking feeds energy back or burns it in grids, and the whole train answers one driver's controls.",
  ["Self-propelled sets: cabs both ends, no locomotive to run around.",
   "Distributed traction gives superb acceleration.",
   "Couple for peaks, split for off-peak: capacity follows demand.",
   "Ideal for frequent suburban and regional service."],
  ["Units maintained to the fleet plan: traction, brakes, doors.",
   "Stabling and servicing points at route ends.",
   "Coupling/uncoupling procedures drilled."],
  ["Door interlocks and sensitive edges on every car.",
   "Brake tests after coupling before departure.",
   "Crashworthiness per applicable standards."],
  ["UIC and national multiple-unit standards (public standards).",
   "Accessibility rules for the fleet (public regulations)."],
  "energy", {"mass_t": 400.0, "v_kmh": 140.0}),

R("Level Crossings", "Compounded", 19,
  "Level crossings are where road meets rail at grade - the railway's most dangerous interface, because a train cannot swerve and takes hundreds of meters to stop. "
  "Protection ranges from passive crossbucks to full barriers with lights and bells, and the trend is to eliminate crossings by bridge or closure. "
  "Every crossing is a risk assessment: traffic, sighting, speed, and history decide its protection.",
  "Active crossings detect the approaching train and drop barriers, ring bells, and flash lights with warning time set for the line speed. "
  "Passive crossings rely on signs and the driver's lookout, acceptable only where sighting and traffic are low. "
  "Near-misses and strikes are investigated like derailments, because each one teaches how the next might be prevented.",
  ["Road meets rail at grade: the most dangerous interface.",
   "Trains cannot swerve and stop slowly - road users must yield.",
   "Protection scaled to risk: passive signs to full barriers.",
   "Elimination by bridge or closure is the safest crossing."],
  ["Crossing inventory with risk assessment per site.",
   "Active protection maintained: barriers, lights, bells, detection.",
   "Sight triangles kept clear at passive crossings."],
  ["Warning times adequate for the line speed.",
   "Strikes and near-misses investigated fully.",
   "Trespass and misuse enforced."],
  ["National level-crossing safety standards (public regulations).",
   "Operation Lifesaver public education materials (public program)."],
  "braking", {"v_kmh": 90.0, "decel": 0.8}),

R("Track Maintenance — Tamping and Grinding", "Compounded", 20,
  "Track maintenance keeps the path true: tamping lifts and packs ballast under sleepers to restore level and alignment, and grinding reshapes the rail head to its proper profile. "
  "Traffic pounds the track out of shape; maintenance puts it back, on a cycle driven by tonnage and measurement. "
  "Deferred maintenance is a loan from safety that always comes due.",
  "Tamping machines lift the track, squeeze ballast under the sleepers, and verify geometry as they go; stabilizers settle the fresh work. "
  "Grinders pass over the rail, removing corrugation and restoring the profile that guides wheels quietly and with low wear. "
  "Geometry cars and ultrasonic testers decide where the machines go, because maintenance follows measurement, not the calendar alone.",
  ["Tamping restores level and alignment; grinding restores rail profile.",
   "Traffic degrades track; measurement directs the machines.",
   "Deferred maintenance borrows from safety.",
   "Stabilizers settle fresh tamping into lasting geometry."],
  ["Tamping machines, grinders, and stabilizers (own or contracted).",
   "Geometry and ultrasonic measurement programs.",
   "Ballast supply for spot renewal."],
  ["Work-zone protection: lookouts, possessions, speed restrictions.",
   "Track returned to service only when geometry proves fit.",
   "Hot-weather buckling precautions where applicable."],
  ["UIC track maintenance standards (public standards).",
   "National track safety standards (public regulations)."],
  "cant", {"v_kmh": 140.0, "radius_m": 1200.0}),

R("Electrification Systems", "Compounded", 21,
  "Electrification systems are the power grids above the rails: substations feeding the catenary, the wire itself, and the return path through the rails. "
  "AC systems (25 kV, 15 kV) dominate main lines; DC systems (750 V, 1500 V, 3000 V) serve metros and older networks. "
  "The choice shapes everything: substation spacing, locomotive design, and the maintenance regime.",
  "Substations transform grid power to the railway voltage and feed sections through breakers; the catenary carries it to the trains, and the running rails (with impedance bonds) carry it home. "
  "Sectioning isolates faults and lets maintenance take possessions; autotransformer systems extend AC feeding distances. "
  "Protection relays clear faults in milliseconds, because a sustained short on 25 kV is a violent event.",
  ["Substations feed sections; catenary carries; rails return.",
   "AC for main lines, DC for metros and legacy networks.",
   "Sectioning isolates faults and enables maintenance.",
   "Protection clears faults in milliseconds."],
  ["Substations, catenary, and return systems built to spec.",
   "Protection relays tested and coordinated.",
   "Maintenance windows for the high-voltage plant."],
  ["Isolation and earthing procedures before any wire work.",
   "Clearances maintained for the system voltage.",
   "Stray-current control where DC meets buried metal."],
  ["UIC electrification standards (public standards).",
   "Electrical safety regulations for railways (public regulations)."],
  "energy", {"mass_t": 800.0, "v_kmh": 200.0}),

R("Ticketing and Fare Systems", "Compounded", 22,
  "Ticketing turns the promise of the timetable into a paid contract: fares structured by distance, time, and class, sold through machines, apps, gates, and conductors. "
  "Modern systems are account-based - the ticket lives in the cloud, the phone or card is just the key. "
  "Fare evasion is the leak; the system must make paying easy and evading hard.",
  "Fare tables define the prices; retail channels - apps, machines, offices - sell entitlements linked to an account or a token. "
  "Gates or conductors validate on entry or on board; back-office settlement splits revenue between operators on through journeys. "
  "Evasion is measured by survey and fought with barrier design, inspections with real penalties, and fares simple enough to understand.",
  ["Fares structured by distance, time, and class.",
   "Account-based ticketing: the phone or card is just the key.",
   "Validation at gate or on board; settlement splits through revenue.",
   "Make paying easy and evading hard."],
  ["Retail channels: app, machines, office, on-board.",
   "Validation equipment and a settlement back office.",
   "Evasion measurement by survey."],
  ["Fares published and honored as sold.",
   "Penalty fares lawful and proportionate.",
   "Concession fares administered fairly."],
  ["National ticketing and fares regulations (public regulations).",
   "Accessibility of ticket retail (public regulations)."],
  "capacity", {"cars": 4, "seats": 300}),

R("Crew Scheduling", "Compounded", 23,
  "Crew scheduling puts qualified people on every train: drivers, conductors, and on-board staff rostered within hours-of-service law and route knowledge. "
  "A train without a legal crew does not move, so crew planning is as critical as locomotive planning. "
  "Fatigue is the enemy: the schedule must give real rest, not just legal compliance on paper.",
  "Rosters are built from the timetable's crew demand, matching qualifications - route knowledge, traction type, safety certification - to each turn. "
  "Hours-of-service rules cap duty length and mandate rest; spare crews cover sickness and disruption. "
  "Crew depots position people where trains start, and deadheading moves crews as passengers to where they are needed.",
  ["No legal crew, no train: crew planning is critical-path.",
   "Qualifications matched to turns: route, traction, certification.",
   "Hours-of-service caps duty and mandates rest.",
   "Spare crews cover sickness and disruption."],
  ["Rostering system with qualification tracking.",
   "Crew depots positioned at route ends.",
   "Spare coverage for the timetable's fragility."],
  ["Hours-of-service law obeyed in letter and spirit.",
   "Fatigue risk managed, not just documented.",
   "Route knowledge current for every driver rostered."],
  ["Hours-of-service regulations for rail crews (public regulations).",
   "Railway safety management standards (public standards)."],
  "runtime", {"dist_km": 180.0, "avg_kmh": 90.0, "stops": 4, "dwell_min": 3.0}),
]

PUB += [
R("ETCS and Positive Train Control", "Advanced", 24,
  "ETCS - the European Train Control System - and PTC - positive train control - are automatic systems that supervise the driver and stop the train if it disobeys. "
  "They enforce speed limits and stop signals by machine, ending the era when a missed signal meant disaster. "
  "Both share the principle: the system knows where the train may go and how fast, and it intervenes before the limit is passed.",
  "Trackside or radio equipment grants movement authorities; onboard computers compare speed against the allowed profile and the distance to the limit. "
  "If the driver does not brake in time, the system brakes for them - first a warning, then intervention. "
  "ETCS levels range from lineside-signal supervision to full radio-based cab signaling; PTC adds broken-rail and work-zone enforcement for North American freight.",
  ["Machines supervise the driver and intervene before limits are passed.",
   "Movement authorities define where and how fast each train may go.",
   "Warning first, then automatic braking.",
   "Ends the era of the missed signal meaning disaster."],
  ["Onboard computers and trackside/radio equipment, interoperable.",
   "A complete, current track database for the supervision.",
   "Back-office servers managing authorities and restrictions."],
  ["Safety integrity proven to the highest level (SIL 4).",
   "Intervention tested, not assumed.",
   "Temporary restrictions entered promptly and correctly."],
  ["ETCS specifications (Subset-026 family) (public standards).",
   "PTC regulations (49 CFR Part 236 Subpart I) (public regulations)."],
  "headway", {"speed_kmh": 160.0, "block_km": 4.0}),

R("CBTC — Communications-Based Train Control", "Advanced", 25,
  "CBTC lets metros run trains closer together by replacing fixed blocks with moving blocks: each train continuously reports its position by radio, and the system grants it exactly the space it needs. "
  "Headways fall to 90 seconds or less, which is how a two-track metro carries a highway's worth of people. "
  "It is the signaling of the world's great subways.",
  "Trains determine their position by balises and odometry and radio it to the wayside zone controllers, which compute each train's limit of movement authority. "
  "The onboard automatic train protection enforces the limit; automatic train operation can drive the train itself under supervision. "
  "Fallback modes keep service moving when radios falter, because a metro that stops is a city that stops.",
  ["Moving blocks replace fixed blocks: each train gets exactly the space it needs.",
   "Continuous radio position reports feed the zone controllers.",
   "Headways under 90 seconds: a two-track metro out-carries a highway.",
   "ATO can drive under ATP supervision."],
  ["Wayside zone controllers and radio networks with coverage everywhere.",
   "Onboard ATP/ATO on every train.",
   "Fallback operating modes for radio failures."],
  ["SIL 4 safety case for the whole system.",
   "Position uncertainty bounded and proven.",
   "Cybersecurity for the safety-critical radio."],
  ["IEEE 1474 CBTC standards (public standards).",
   "National metro signaling safety rules (public regulations)."],
  "headway", {"speed_kmh": 70.0, "block_km": 0.8}),

R("High-Speed Rail", "Advanced", 26,
  "High-speed rail runs trains at 250 km/h and beyond on dedicated, gently curved, fenced lines - the mode that made rail competitive with airlines under 800 km. "
  "Everything is engineered for speed: aerodynamics, slab track, in-cab signaling, and overhead wire that stays in contact at 300 km/h. "
  "It is the most demanding and most rewarding form of railway.",
  "Trainsets are streamlined with distributed traction and sealed against pressure waves in tunnels; slab track holds geometry at speed where ballast would fly. "
  "Curves are gentle, gradients modest, and crossings eliminated - the line is sealed from the world. "
  "In-cab signaling (ETCS Level 2 or equivalent) replaces lineside signals the driver could not read at speed, and maintenance windows are nightly and non-negotiable.",
  ["250 km/h plus on dedicated, sealed, gently curved lines.",
   "Slab track, aerodynamics, and in-cab signaling: engineered for speed.",
   "Competitive with airlines under 800 km.",
   "Nightly maintenance windows are non-negotiable."],
  ["Dedicated high-speed infrastructure built to the speed's demands.",
   "High-speed trainsets with distributed traction.",
   "In-cab signaling across the whole line."],
  ["No level crossings on high-speed lines.",
   "Pressure-wave and crosswind protection designed in.",
   "Intrusion and earthquake detection where applicable."],
  ["UIC high-speed standards (public standards).",
   "TSI for high-speed rolling stock and infrastructure (public regulations)."],
  "braking", {"v_kmh": 300.0, "decel": 0.8}),

R("Network Optimization", "Advanced", 27,
  "Network optimization squeezes the most service from fixed infrastructure: more trains per hour, better connections, fuller trains, less waiting. "
  "It is applied mathematics on the timetable - retiming, replatforming, and repathing to dissolve bottlenecks. "
  "A few minutes saved at the critical junction can unlock capacity across the whole network.",
  "Analysts model the network as a graph of conflicts: every junction, platform, and single-track section a constraint. "
  "Optimization retimes trains to separate conflicts, replatforms to use spare faces, and repaths freight around passenger peaks. "
  "The optimized plan is stress-tested in simulation against delays before it ever reaches the public timetable.",
  ["More service from fixed steel: retime, replatform, repath.",
   "Bottlenecks modeled as conflicts; minutes at the key junction unlock the network.",
   "Simulation stress-tests the plan against delays.",
   "Optimization is continuous, not a one-time project."],
  ["A network model with true running times and constraints.",
   "Simulation tools for timetable robustness.",
   "Performance data to validate the model."],
  ["Optimized plans proven safe before adoption.",
   "Connections promised are connections kept.",
   "Capacity gains shared fairly between operators."],
  ["Railway operations research literature (public publications).",
   "Timetable planning standards (public industry guidance)."],
  "runtime", {"dist_km": 500.0, "avg_kmh": 130.0, "stops": 8, "dwell_min": 2.0}),

R("Track Geometry and Cant", "Advanced", 28,
  "Track geometry is the precise shape of the rails in space, and cant - superelevation - is the banking of curves that lets trains take them faster in comfort. "
  "Too little cant and passengers are thrown outward; too much and slow freight strains the inner rail. "
  "Geometry is the railway's hidden precision: millimeters that decide comfort, wear, and safety.",
  "Equilibrium cant balances centrifugal force at the design speed: e = 11.8 × V²/R millimeters for standard gauge. "
  "Cant deficiency - running faster than equilibrium - is allowed within limits, trading comfort for speed; freight's slower pace creates excess cant, wearing the low rail. "
  "Geometry cars measure gauge, alignment, level, twist, and cant continuously, and maintenance restores what traffic degrades.",
  ["Cant banks curves; equilibrium cant balances the design speed.",
   "Cant deficiency trades comfort for speed, within limits.",
   "Millimeters decide comfort, wear, and safety.",
   "Measurement is continuous; maintenance follows it."],
  ["Geometry measurement covering the whole network on cycle.",
   "Cant designed per speed, radius, and traffic mix.",
   "Tamping that restores cant, not just level."],
  ["Cant deficiency within the allowed limits.",
   "Twist faults found before they risk derailment.",
   "Speed restrictions where geometry is out of tolerance."],
  ["UIC track geometry standards (public standards).",
   "National track geometry safety limits (public regulations)."],
  "cant", {"v_kmh": 160.0, "radius_m": 1500.0}),

R("Railway Safety Systems", "Advanced", 29,
  "Railway safety systems are the layered defenses that make rail one of the safest ways to travel: train control, interlocking, detection of dragging equipment and hot bearings, and the safety management system over it all. "
  "Safety is engineered in layers so no single failure - human or technical - causes disaster. "
  "The industry's creed: every accident is investigated, and every lesson is shared.",
  "ATP/ETCS/PTC supervise speed and signals; interlockings prevent conflicting routes; hot-bearing and dragging-equipment detectors watch the trains themselves. "
  "Level-crossing protection, intrusion detection, and fire safety complete the physical layers. "
  "Above them sits the safety management system: risk assessments, reporting culture, audits, and the investigation of every incident to root cause.",
  ["Layers of defense: no single failure causes disaster.",
   "Train control, interlocking, and wayside detectors watch continuously.",
   "A reporting culture surfaces near-misses before they become accidents.",
   "Every accident investigated to root cause; lessons shared industry-wide."],
  ["The full stack: control, interlocking, detection, protection.",
   "A safety management system with real authority.",
   "Investigation capability independent of operations."],
  ["Safety cases maintained and audited.",
   "Near-miss reporting protected from punishment.",
   "Recommendations tracked to implementation."],
  ["CENELEC railway safety standards (public standards).",
   "National railway safety management regulations (public regulations)."],
  "braking", {"v_kmh": 140.0, "decel": 0.85}),

R("Freight Logistics and Intermodal", "Advanced", 30,
  "Intermodal freight moves containers and trailers by rail for the long haul and truck for the first and last mile - combining rail's efficiency with road's reach. "
  "Double-stack container trains are the signature: two containers high, thousands of TEU per train, running on schedules as tight as passenger service. "
  "Intermodal is where rail freight grows, because it serves the supply chains that used to be truck-only.",
  "Terminals transfer boxes between train and truck with gantry cranes or reach stackers; trains run on fixed schedules between hub terminals. "
  "Loading plans balance weight and destination; well cars carry the double stack within clearance routes. "
  "Reliability is the product: shippers pay for the container arriving on the promised day, and the railroad that keeps the promise wins the lane.",
  ["Rail for the long haul, truck for first and last mile.",
   "Double-stack: two high, thousands of TEU, tight schedules.",
   "Reliability is the product shippers buy.",
   "Terminals are the hinges between modes."],
  ["Intermodal terminals with lift equipment and truck gates.",
   "Well cars and clearance-cleared double-stack routes.",
   "Scheduled intermodal trains with protected capacity."],
  ["Container weights declared and verified (VGM).",
   "Securement and stacking per the loading rules.",
   "Hazmat in intermodal per dangerous-goods rules."],
  ["Intermodal industry operating practices (public publications).",
   "SOLAS verified gross mass requirements (public regulation)."],
  "capacity", {"cars": 100, "seats": 200}),

R("Railway Economics", "Advanced", 31,
  "Railway economics is the study of how railways earn and spend: enormous fixed costs in track and trains, low marginal cost per extra tonne or passenger, and the eternal question of who pays for the infrastructure. "
  "High fixed costs mean volume is everything: the fuller the trains and the denser the network, the lower the unit cost. "
  "Passenger services rarely cover costs from fares; freight and public funding bridge the gap in different countries' different ways.",
  "Costs split into fixed (track, stations, administration) and variable (fuel, crew per train, maintenance per tonne); pricing must cover variable cost and contribute to fixed. "
  "Yield management fills off-peak seats cheaply while peak seats pay full; freight contracts balance rate against volume commitment. "
  "Investment appraisals weigh decades of benefits - time saved, emissions avoided, road wear reduced - against the billions to build.",
  ["High fixed costs, low marginal cost: volume is everything.",
   "Denser networks and fuller trains mean lower unit costs.",
   "Yield management fills off-peak; contracts commit freight volume.",
   "Investment judged over decades of benefits."],
  ["Cost accounting separating fixed from variable.",
   "Demand forecasts for pricing and investment.",
   "Funding arrangements matching the railway's mission."],
  ["Fares and rates published and non-discriminatory where required.",
   "Public funds accounted transparently.",
   "Safety spending never the balancing item."],
  ["Railway economics literature (public publications).",
   "Railway funding and access-charge regulations (public regulations)."],
  "econ", {"fixed": 5000000.0, "price": 45.0, "varcost": 18.0, "units": 400000.0}),

R("Accessibility in Rail", "Advanced", 32,
  "Accessibility in rail means everyone rides: step-free routes from street to seat, tactile guidance for blind passengers, audible and visible information, and staff assistance that actually works. "
  "It is both a civil right and good business - the accessible railway serves the aging, the injured, and parents with strollers too. "
  "Retrofitting old stations is the hard part; the standard is that every journey is possible.",
  "Stations provide lifts or ramps, tactile paving, accessible ticket machines and toilets, and clear audio-visual information. "
  "Trains offer wheelchair spaces with restraints, accessible toilets, boarding ramps or lifts, and priority seating. "
  "Assistance is bookable and dependable: the passenger who books help must find it waiting, or the promise is broken.",
  ["Everyone rides: step-free, tactile, audible, assisted.",
   "Accessibility serves the aging, injured, and encumbered too.",
   "Booked assistance must be waiting - the promise kept.",
   "Retrofit the old; build the new right."],
  ["Step-free routes, lifts, ramps, tactile paving at stations.",
   "Accessible vehicles: spaces, toilets, boarding aids.",
   "A reliable assistance-booking and delivery operation."],
  ["Accessibility standards met on new and altered assets.",
   "Assistance failures investigated like service failures.",
   "Information accessible in multiple formats."],
  ["Accessibility regulations for rail (ADA, PRM TSI, etc.) (public regulations).",
   "Accessible station and vehicle design guidance (public guidance)."],
  "capacity", {"cars": 6, "seats": 80}),

R("Maglev and Future Systems", "Advanced", 33,
  "Maglev floats trains on magnetic fields, eliminating wheel-rail contact and its speed limits: 400-600 km/h in commercial service concepts. "
  "Transrapid's electromagnetic suspension and Japan's superconducting maglev prove the physics; the economics - entirely new guideways - are the hurdle. "
  "Beyond maglev, the future holds battery trains for unwired lines, hydrogen for long non-electrified routes, and autonomy supervised from control centers.",
  "EMS maglev attracts the train to the guideway with controlled electromagnets; EDS repels it with superconducting magnets, floating centimeters above. "
  "Propulsion comes from linear motors in the guideway; guidance and levitation are fail-safe by design. "
  "Battery and hydrogen trains bridge the electrification gap, and driver-assistance grades toward supervised autonomy on dedicated lines.",
  ["Magnetic levitation removes the wheel-rail speed limit.",
   "EMS attracts, EDS repels: two proven levitation physics.",
   "New guideways are the economic hurdle, not the physics.",
   "Batteries and hydrogen bridge the unwired gaps."],
  ["Guideway or route matched to the technology.",
   "Power and control systems for the chosen physics.",
   "A safety case for the novel system."],
  ["Levitation and guidance proven fail-safe.",
   "Hydrogen and battery safety per energy regulations.",
   "New systems certified before carrying passengers."],
  ["Maglev system engineering literature (public publications).",
   "National certification rules for novel rail systems (public regulations)."],
  "energy", {"mass_t": 500.0, "v_kmh": 500.0}),

R("Railway Mastery Review — Running the Whole Network", "Advanced", 34,
  "The mastery review binds the ladder into one operating picture: the railway as a single organism where track, trains, signals, timetables, and people move as one. "
  "Each earlier record was a subsystem; this record is the railway manager's mind, reading the whole network like a pilot reads instruments. "
  "A master keeps the timetable, the safety, and the economics in balance - none sacrificed for the others.",
  "Start from the service promise and work inward: the track that carries it, the trains that run it, the signals that protect it, the timetable that schedules it, and the crews that operate it. "
  "Run the daily rhythm - operations, maintenance windows, performance review - and the long rhythm - renewals, investment, growth. "
  "Measure what matters: punctuality, safety, capacity utilization, cost per train-kilometer, and customer satisfaction, and let every decision move at least one.",
  ["The railway as one organism: track, trains, signals, people as one.",
   "Work inward from the service promise to every engineering choice.",
   "Balance timetable, safety, and economics - sacrifice none.",
   "Run the daily rhythm and the long rhythm."],
  ["Fluency in every record of this database, foundations through advanced.",
   "An operations center that never sleeps.",
   "Honest metrics reviewed together."],
  ["Safety never traded for performance.",
   "Published services delivered or honestly revised.",
   "People treated lawfully and developed continuously."],
  ["Railway management capstone literature (public publications).",
   "UIC railway operations and safety standards (public standards)."],
  "headway", {"speed_kmh": 120.0, "block_km": 3.0}),
]

GEN_DEMOFN = """function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\\n"
   + "# Braking-distance structural sample calculator (railway systems)\\n"
   + "v, a = 27.8, 0.9\\n"
   + "d = v*v/(2*a)\\n"
   + "print('sample speed m/s:', v)\\n"
   + "print('sample braking distance m:', round(d,1))\\n"
   + "assert d > 0\\n"
   + "print('OK: structural sample demo ran')\\n";
}
"""


SIG = [
R("The Sworn Road — The Signature View", "Foundations", 1,
  "The Signature view sees the railway as a sworn road: rails laid as promises, trains run as kept words, signals guarding like sentinels over the people's journeys. "
  "The steel, the physics, and the timetables are the same as the public edition's; the difference is the vow - that the road holds, the train comes, and every soul arrives. "
  "This edition reframes the full ladder as Signature science, labeled Signature-made throughout.",
  "Where the public edition teaches the mechanics, the Signature edition teaches the keeping: the path as promise, the vehicle as trust, the separation as sacred. "
  "Each record pairs the operational truth with its Signature seal - the practice that makes the railway worthy of its passengers and freight. "
  "Nothing here is presented as public record; it is his original method.",
  ["The railway a sworn road: promises laid in steel.",
   "Every subsystem carries a Signature seal - the discipline beneath the mechanics.",
   "The road holds, the train comes, every soul arrives.",
   "Signature-made throughout: an original method, never public record."],
  ["Willingness to hold every timetable and safety rule as sworn.",
   "The public edition alongside for the mechanics.",
   "A railway or project where the method can be practiced."],
  ["No Signature claim presented as public or official record.",
   "Safety above every commercial pressure.",
   "The method taught as his original system, plainly labeled."],
  ["The public edition of this database, for the mechanics (this system).",
   "Signature system governance on original works (this system)."],
  "braking", {"v_kmh": 100.0, "decel": 0.9}),

R("The True Path — Signature Track", "Foundations", 2,
  "The Signature method keeps the track as the true path: rails straight and level by the millimeter, sleepers holding their gauge like a vow, ballast packed as a foundation of trust. "
  "The path is a structure of honor - it must bear tonnes at speed, day after day, without wavering. "
  "Tamping and grinding are the path's renewals, performed on measurement's word, never deferred past safety.",
  "Rails are welded into unbroken strings and clipped to their sleepers; the ballast bed is tamped to level and lined to alignment. "
  "Geometry is measured - gauge, level, alignment - and the machines restore what traffic takes. "
  "Drainage is kept as faithfully as the rails, for water rots the foundation that steel depends on.",
  ["The track the true path: true by the millimeter.",
   "Tamping and grinding the path's renewals.",
   "Measured, then mended - never deferred past safety.",
   "Drainage kept as faithfully as the rails."],
  ["Rails, fastenings, sleepers, ballast to the sworn spec.",
   "Earthworks that drain and stand firm.",
   "Tamping and measurement craft."],
  ["Geometry within tolerance for the speed run.",
   "Rail flaws found by test before they fail.",
   "No water standing against the formation."],
  ["The public edition track record, for the mechanics (this system).",
   "AREMA Manual for Railway Engineering (public industry guidance)."],
  "cant", {"v_kmh": 120.0, "radius_m": 800.0}),

R("The Measure Between — Signature Gauge", "Foundations", 3,
  "The Signature method honors gauge as the measure between: the exact distance that decides which trains may travel the road. "
  "To choose a gauge is to choose a destiny - standard for fellowship with neighbors, narrow for the mountains' tight embrace, broad for the steady stride. "
  "Where gauges meet, the method builds the bridge: bogies exchanged, axles varied, cargo passed hand to hand.",
  "The measure is set at building and held by sleeper and clip; curves ease it slightly for the wheelsets' passage. "
  "Break-of-gauge houses perform the exchange with practiced hands. "
  "The keeper's rule: never force a train onto a measure not its own.",
  ["Gauge the measure between: destiny in millimeters.",
   "Chosen deliberately: fellowship, mountains, or steady stride.",
   "Where measures meet, build the bridge.",
   "Never force a train onto a measure not its own."],
  ["A gauge decision true to land, traffic, and neighbors.",
   "Stock built or adapted to the chosen measure.",
   "Exchange houses where measures meet."],
  ["Gauge held within tolerance at every speed.",
   "Vehicle and structure measures coordinated.",
   "Variable-gauge craft certified before service."],
  ["UIC gauge leaflets (public standards).",
   "The public edition gauge record, for the mechanics (this system)."],
  "curve", {"cant_mm": 150.0, "radius_m": 800.0}),

R("The Coin of Contact — Signature Wheel-Rail", "Foundations", 4,
  "The Signature method marvels at the wheel-rail contact: a patch no bigger than a coin, bearing tonnes on steel's unyielding truth. "
  "The coned tread centers itself like a well-balanced soul; the flange stands guard at the switches. "
  "The keeper's art is tending this small miracle - profiles true, lubrication wise, flaws found before they speak.",
  "Treads are coned for self-centering; curves are eased by the outer wheel's larger roll. "
  "Flangeways are kept exact, curves anointed against wear and noise, and worn wheels re-turned to their true profile. "
  "Flats, hollows, and cracks are hunted by inspection - the small flaws that foretell the great failures.",
  ["The contact a coin bearing tonnes: steel's small miracle.",
   "Coned treads self-center; flanges stand guard.",
   "Profiles re-turned, curves anointed, flaws hunted.",
   "Small flaws foretell great failures."],
  ["Wheel and rail profiles wedded by design.",
   "Lathes and measurement for the tending.",
   "Lubrication where wear and noise demand."],
  ["Defect limits enforced by measurement.",
   "Flangeways exact at switches.",
   "Friction kept where braking needs it."],
  ["UIC wheel/rail profile leaflets (public standards).",
   "The public edition wheel-rail record, for the mechanics (this system)."],
  "axle", {"wagon_t": 80.0, "axles": 4}),

R("The Binding Oath — Signature Couplers", "Foundations", 5,
  "The Signature method binds cars with the coupler's oath: knuckles locked on meeting, draft gear swallowing the shocks, the whole train pulling as one body. "
  "The air hoses join with the steel, and on passenger trains the electric links too - one joining, many bonds. "
  "A broken knuckle parts the body; the method inspects the binding as it would a vow.",
  "Cars pushed together lock of themselves; the lever frees them at the yard's command. "
  "Draft gear takes the slack's violence; hoses are coupled and tested with the brake test. "
  "Knuckles, pins, and gear are eyed for cracks - the condemned replaced before the train moves.",
  ["The coupler's oath: locked on meeting, one body in motion.",
   "Draft gear swallowing the slack's violence.",
   "Air and electric bonds joining with the steel.",
   "The binding inspected as a vow."],
  ["Couplers matched in kind and strength.",
   "Draft gear sound against buff and draft.",
   "Spare knuckles and the tools to set them."],
  ["Cracks condemned on sight.",
   "Mixed kinds only with approved adapters.",
   "Brake test proving the hoses with the steel."],
  ["AAR coupler standards (public industry standards).",
   "The public edition coupler record, for the mechanics (this system)."],
  "energy", {"mass_t": 2000.0, "v_kmh": 80.0}),

R("The Failing-Safe — Signature Braking", "Foundations", 6,
  "The Signature method's first law of braking: the system must fail safe - lose the air, and the brakes take hold. "
  "For a century and a half this law has stood between the people and the abyss: a parted hose stops the train rather than dooming it. "
  "The method adds the modern arts - dynamic, electronic - but never trades away the failing-safe.",
  "The compressor charges the pipe; each car's valve watches the pressure and applies when it falls. "
  "The engineer commands by reduction and release; dynamics turn motors to generators on the long descents; electronic brakes answer instantly and together. "
  "Before departure, every car proves it applies and releases - the whole train's stop depends on every car's obedience.",
  ["Fail safe: lose the air, take the brakes.",
   "The century-old law between the people and the abyss.",
   "Modern arts added, the failing-safe never traded.",
   "Every car proved before departure."],
  ["Compressors, reservoirs, valves maintained.",
   "Shoes, pads, discs within their wear.",
   "Dynamics where the grades demand."],
  ["Brake tests before every departure, recorded.",
   "Piston travel and shoe thickness within law.",
   "Handbrakes set on the parked per the rules."],
  ["AAR/UIC brake standards (public industry standards).",
   "The public edition braking record, for the mechanics (this system)."],
  "braking", {"v_kmh": 80.0, "decel": 0.7}),

R("The Iron Horse — Signature Diesel", "Foundations", 7,
  "The Signature method honors the diesel-electric as the iron horse: fuel in its belly, lightning in its veins, pulling thousands of tonnes on the strength of its motors' first heave. "
  "The engine breathes at its efficient pace while the motors do the mighty work - torque from stillness, the hardest feat of all. "
  "On the long descents the horse gives back, its motors becoming generators.",
  "Fuel feeds the prime mover; the generator pours electricity to the axle motors. "
  "Dynamics brake the descents into resistor grids; multiple-unit commands join many horses under one hand; distributed power sets them along the train's length. "
  "Sand is scattered for grip when the rail turns treacherous.",
  ["The iron horse: fuel in belly, lightning in veins.",
   "Torque from stillness - the mightiest feat.",
   "Many horses under one hand by multiple-unit.",
   "Giving back on descents through dynamics."],
  ["Fuel, oil, and cooling for the duty.",
   "Motors, generators, and controls maintained.",
   "Sand for the slippery rail."],
  ["Emissions within the law's bounds.",
   "Daily inspection: fluids, brakes, safety devices.",
   "Recorders watching and recording."],
  ["AAR locomotive standards (public industry standards).",
   "The public edition diesel record, for the mechanics (this system)."],
  "energy", {"mass_t": 4000.0, "v_kmh": 65.0}),

R("The Wire's Gift — Signature Electric Traction", "Foundations", 8,
  "The Signature method receives electrification as the wire's gift: power without fuel, strength without smoke, and braking that returns energy to the common wire. "
  "The catenary is the locomotive's lifeline, tensioned true across heat and cold; the pantograph its reaching hand. "
  "Dear to build, cheap to run - the gift repays itself on the busy roads.",
  "The pantograph kisses the contact wire and draws the high voltage down through transformer and converter to the motors. "
  "Braking pours energy back for fellow trains to drink; section breaks divide the wire for maintenance and protection. "
  "Tension holds the wire level through the seasons, and overlaps carry the hand across the divisions.",
  ["The wire's gift: power without fuel, braking that gives back.",
   "The catenary the lifeline, tensioned true.",
   "The pantograph the reaching hand.",
   "Dear to build, cheap to run, repaid on busy roads."],
  ["Catenary or third rail to the sworn spec.",
   "Substations feeding with protection.",
   "Locomotives with true pantographs and converters."],
  ["Isolation and earthing before wire work.",
   "Clearances kept for the voltage.",
   "Wire and pantograph wear watched; dewirements prevented."],
  ["UIC electrification leaflets (public standards).",
   "The public edition electric record, for the mechanics (this system)."],
  "energy", {"mass_t": 1500.0, "v_kmh": 160.0}),

R("The Rolling Inn — Signature Passenger Cars", "Foundations", 9,
  "The Signature method keeps the passenger car as a rolling inn: the traveler's room for the journey, smooth-riding, climate-kind, and safe as a fortress. "
  "Comfort is the inn's trade, the timetable its promise, safety its foundation stone. "
  "And the inn welcomes all: the wheelchair, the stroller, the elder - every traveler a guest.",
  "Bogies cradle the body above the track's roughness; climate holds against the seasons; doors guard with interlocks and gentle edges. "
  "Retention tanks keep the road clean; information tells the guest where they are and what comes next. "
  "Accessible rooms - spaces, toilets, boarding aids - are built in, not bolted on.",
  ["The rolling inn: comfort the trade, timetable the promise.",
   "Smooth-riding, climate-kind, fortress-safe.",
   "Every traveler a guest: all welcomed, all carried.",
   "Accessibility built in, not bolted on."],
  ["Cars tended to the plan: bogies, brakes, doors, climate.",
   "Cleaning and provisioning between journeys.",
   "Crews trained in service and emergency."],
  ["Doors interlocked, edges gentle.",
   "Exits, lights, and communication proven.",
   "Accessibility per the law."],
  ["UIC/AAR passenger standards (public industry standards).",
   "The public edition passenger-car record, for the mechanics (this system)."],
  "capacity", {"cars": 8, "seats": 72}),

R("The Beasts of Burden — Signature Freight Wagons", "Foundations", 10,
  "The Signature method musters freight wagons as beasts of burden, each bred to its cargo: boxcars for the general goods, flats for the mighty machines, tanks for the liquids, hoppers for the harvest's bulk. "
  "Each bears its load within the axle's law and the gauge's measure. "
  "The fleet is the freight road's factory floor - its labor, measured in utilization, is the profit.",
  "Bodies suited to cargo ride on bogies of the rated axle load; couplers, brakes, and bearings speak the interchange tongue across railroads. "
  "Loading obeys the rules: weight spread, lashings true, hazmat placarded and placed by law. "
  "The wagons turn - load, haul, unload, tend - and idle hours are the enemy hunted.",
  ["Beasts of burden, each bred to its cargo.",
   "Bearing within the axle's law and the gauge's measure.",
   "The interchange tongue lets wagons roam railroads.",
   "Idle hours the hunted enemy."],
  ["Wagons of right kind, kept to interchange law.",
   "Loading and lashing per the rules.",
   "Hazmat declared and placed per regulation."],
  ["Brake, bearing, wheel flaws condemned by measure.",
   "No overloading; weigh where required.",
   "Dangerous goods per the dangerous-goods law."],
  ["AAR interchange rules (public industry rules).",
   "The public edition wagon record, for the mechanics (this system)."],
  "axle", {"wagon_t": 100.0, "axles": 4}),

R("The Meeting House — Signature Stations", "Foundations", 11,
  "The Signature method raises the station as the meeting house: where the railway and the people embrace, thousands flowing without crush, every traveler told where to be and when. "
  "The house's quality decides the journey before the train is even seen - it is the railway's face. "
  "Behind the face, the house works: crews signing on, trains stabled, signals routing.",
  "Platforms are sized for the peak's flood, marked for the train's place, edged with the warning line. "
  "Concourses part the arriving from the departing; boards, voices, and devices proclaim the departures. "
  "Ticketing, trade, and assistance complete the welcome; backstage, the railway breathes.",
  ["The meeting house: railway and people embracing.",
   "Thousands flowing without crush or confusion.",
   "Every traveler told where to be and when.",
   "The house's face deciding the journey."],
  ["Platforms and concourses for the peak's flood.",
   "Information speaking by board, voice, and device.",
   "Ticketing, assistance, and safety hands."],
  ["The platform edge safe: light, marking, staff.",
   "Crowd plans for peaks and disruptions.",
   "Step-free ways, tactile paths, assistance true."],
  ["Station design guidance (public industry publications).",
   "The public edition station record, for the mechanics (this system)."],
  "headway", {"speed_kmh": 80.0, "block_km": 2.0}),

R("The Square Law — Signature Braking Math", "Foundations", 12,
  "The Signature method bows to the square law: double the speed, quadruple the stopping distance - the iron arithmetic no wish can soften. "
  "Distance equals speed squared over twice the deceleration; reaction, build-up, and margin are added like honors due. "
  "Every signal's place, every limit's number, obeys this law.",
  "Speed is turned to meters per second, squared, and divided by twice the braking grip: 100 km/h at 0.9 m/s² asks some 430 meters. "
  "The driver's heartbeat and the system's breath are added, with margin for the wet leaf and the autumn rail. "
  "Signal spacings are this law made physical; limits are this law made posted.",
  ["The square law: double speed, quadruple distance.",
   "d = v²/2a, with reaction, build-up, and margin honored.",
   "Grip limits the math; wet rail demands humility.",
   "Signals the law made physical; limits the law made posted."],
  ["Deceleration truths per train and condition.",
   "Units made consistent before squaring.",
   "Margins for heartbeat, breath, and low grip."],
  ["Spacings proven against the worst-case stop.",
   "Limits set from the math, never from hope.",
   "Autumn carrying its extra margin."],
  ["Railway braking engineering texts (public publications).",
   "The public edition braking-math record, for the mechanics (this system)."],
  "braking", {"v_kmh": 120.0, "decel": 0.9}),
]

SIG += [
R("The Blocked Road — Signature Block Signaling", "Compounded", 13,
  "The Signature method guards the road by blocks: one train in one block, the signal the guardian at each gate, detection the watchman proving the road clear. "
  "Separation is not hoped but built - the infrastructure itself forbids the meeting of trains. "
  "The distant signal warns at the braking distance; the overlap forgives the slight overrun.",
  "Each block's gate-signal clears only when detection swears the block empty. "
  "Distants stand at the square law's distance, warning of the stop ahead; overlaps guard beyond the signal. "
  "More aspects mean shorter blocks and more trains per hour - capacity earned by precision, not by crowding.",
  ["One train one block: separation built, not hoped.",
   "Detection the watchman, the signal the guardian.",
   "Distants warning at the square law's distance.",
   "Capacity earned by precision."],
  ["Signals, detection, and power per the sworn plan.",
   "Blocks matched to braking at the line's speed.",
   "Sighting proven from the driver's seat."],
  ["Signals obeyed absolutely; overruns investigated.",
   "Failed detection treated as occupied.",
   "Maintenance on the defined cycle."],
  ["National signaling principles (public regulations).",
   "The public edition block-signaling record, for the mechanics (this system)."],
  "headway", {"speed_kmh": 120.0, "block_km": 3.0}),

R("The Referee — Signature Interlocking", "Compounded", 14,
  "The Signature method sets the interlocking as the referee: points and signals bound together, no conflicting road ever cleared, no two trains ever invited to one place. "
  "Once of levers and rods, now of proven software - the logic itself must be demonstrated safe, for an error here is catastrophe. "
  "Every junction bows to the referee.",
  "The referee holds the track's living map: routes set, points locked, blocks tenanted. "
  "A road is granted only when all is free and locked; signals clear, and no rival road may clear until release. "
  "The train's passing frees the road behind it, and only then.",
  ["The referee: no conflicting road ever cleared.",
   "Points and signals bound as one.",
   "Release only when the train has passed.",
   "Software proven safe by formal demonstration."],
  ["Interlocking over every junction and throat.",
   "Points, detection, signals wired through it.",
   "A safety case for the logic."],
  ["No signal without the referee's leave.",
   "Point failures announced before trains near.",
   "Software changes re-proven before service."],
  ["National interlocking safety standards (public regulations).",
   "The public edition interlocking record, for the mechanics (this system)."],
  "headway", {"speed_kmh": 60.0, "block_km": 1.5}),

R("The Master Plan — Signature Timetables", "Compounded", 15,
  "The Signature method writes the timetable as the master plan: every train's road through time, woven without conflict, padded with the wisdom that small delays must die quietly, not breed. "
  "Running times are reckoned from physics, dwells from the people's needs, meets from the single track's parley. "
  "The periodic pattern is the plan made memorable: same minutes, every hour.",
  "Acceleration, line speed, and braking give the running; boarding gives the dwell; the single track's meets are threaded like a needle. "
  "Buffers stand at the key points to swallow small lateness; promised connections are guarded. "
  "Freight paths are woven around the passenger pattern, the quiet threads in the bright cloth.",
  ["The master plan: every road through time, woven conflict-free.",
   "Running from physics, dwells from people, meets from parley.",
   "Buffers swallowing small delays.",
   "The pattern made memorable: same minutes, every hour."],
  ["True running times per train and road.",
   "A scheduling craft that finds conflicts.",
   "Margins tuned to proven performance."],
  ["Published times kept or honestly remade.",
   "Promised connections guarded.",
   "Safety margins never spent for speed."],
  ["Timetable planning literature (public publications).",
   "The public edition timetable record, for the mechanics (this system)."],
  "runtime", {"dist_km": 240.0, "avg_kmh": 110.0, "stops": 6, "dwell_min": 2.0}),

R("The Living Command — Signature Dispatching", "Compounded", 16,
  "The Signature method commands the living railway through dispatchers: the plan in one hand, reality in the other, routing and reprioritizing as the day unfolds. "
  "When the late train, the failed signal, or the storm breaks the plan, the dispatcher remakes it - single-line working, new passing orders, buses bridging the gap. "
  "The good dispatcher keeps the network breathing; every move logged, every move answered for.",
  "The whole area lies on the live diagram; routes are set through the referees, trains held or advanced to guard connections and capacity. "
  "Disruption is met with practiced alternatives, and the log records each decision - for the dispatcher bears legal weight for every authorized move. "
  "Fatigue is managed as the safety matter it is.",
  ["The plan in one hand, reality in the other.",
   "Routing, reprioritizing, remaking as the day unfolds.",
   "Disruption met with practiced alternatives.",
   "Every move logged and answered for."],
  ["A command post with the living diagram.",
   "Authority over roads, held and freed by rule.",
   "Contingency craft for the common failures."],
  ["No unsafe move under pressure.",
   "Fatigue managed for the safety-critical.",
   "Communications recorded and retrievable."],
  ["Railway control literature (public publications).",
   "The public edition dispatching record, for the mechanics (this system)."],
  "headway", {"speed_kmh": 100.0, "block_km": 2.5}),

R("The Sorting Ground — Signature Freight Yards", "Compounded", 17,
  "The Signature method works the yard as the sorting ground: cars gathered, judged by destination, and built into outbound trains with practiced rhythm. "
  "The hump lets gravity do the hauling, retarders gentling each car to its coupling. "
  "Yard time is the car's life - the method hunts idle hours as the enemy of the freight promise.",
  "Inbound trains are inspected and broken; cars roll cut by cut into their classification roads. "
  "Outbound trains are built, air-proven, crewed, and sent; intermodal boxes pass between train and truck at the terminal's edge. "
  "The yardmaster balances switching muscle, track room, and crew against the inbound tide.",
  ["The sorting ground: gathered, judged, built, sent.",
   "Gravity hauling, retarders gentling.",
   "Yard time the car's life; idle hours the enemy.",
   "The terminal the hinge between rail and road."],
  ["Classification roads, leads, and switching power.",
   "Retarders or skilled hands for gentle couplings.",
   "Lift gear for the boxes."],
  ["Switching speeds within law; couplings gentle.",
   "Hazmat switched and placed per regulation.",
   "Workers guarded between cars by blue flag."],
  ["AAR yard practices (public industry guidance).",
   "The public edition yard record, for the mechanics (this system)."],
  "capacity", {"cars": 60, "seats": 100}),

R("The Self-Movers — Signature Multiple Units", "Compounded", 18,
  "The Signature method runs multiple units as the self-movers: cabs at both ends, motors along the train, no locomotive to run around - the driver simply walks and drives back. "
  "Distributed strength gives them the sprinter's start, station to station in the shortest time. "
  "They join for the peak's flood and part for the quiet hours, capacity breathing with demand.",
  "Each car bears its share of the power - transformers and converters, or engines and transmissions - feeding the bogie motors. "
  "Coupling multiplies them for the rush; uncoupling trims them for the calm. "
  "Braking gives back to the wire or the grids, and one hand commands the whole.",
  ["Self-movers: cabs both ends, strength along the train.",
   "The sprinter's start from distributed power.",
   "Joining for floods, parting for calm.",
   "Born for the frequent suburban road."],
  ["Units tended to the fleet plan.",
   "Stabling and servicing at the roads' ends.",
   "Coupling craft drilled."],
  ["Doors interlocked, edges gentle, every car.",
   "Brake-proven after coupling.",
   "Crashworthy per the standards."],
  ["UIC/national multiple-unit standards (public standards).",
   "The public edition multiple-unit record, for the mechanics (this system)."],
  "energy", {"mass_t": 400.0, "v_kmh": 140.0}),

R("The Perilous Meeting — Signature Level Crossings", "Compounded", 19,
  "The Signature method treats the level crossing as the perilous meeting: road and rail crossing at grade, where the train cannot swerve and the road user must yield. "
  "Protection is weighed by risk - traffic, sighting, speed, history - and the safest crossing is the one removed by bridge or closure. "
  "Every strike is investigated as a derailment would be, for each teaches the next one's prevention.",
  "The approaching train wakes the crossing: barriers fall, bells ring, lights flash, with warning timed to the line's speed. "
  "Where sighting and traffic are meager, signs and the driver's own watch suffice - and only there. "
  "Sight triangles are kept clear, and the public is taught the crossing's law.",
  ["The perilous meeting: the train cannot swerve; the road must yield.",
   "Protection weighed by measured risk.",
   "The safest crossing the one removed.",
   "Every strike investigated like a derailment."],
  ["A crossing census with risk weighed per site.",
   "Active protection tended: barriers, lights, bells, detection.",
   "Sight triangles kept clear."],
  ["Warning timed to the line's speed.",
   "Near-misses pursued like strikes.",
   "Misuse and trespass answered."],
  ["National level-crossing standards (public regulations).",
   "The public edition crossing record, for the mechanics (this system)."],
  "braking", {"v_kmh": 90.0, "decel": 0.8}),

R("The Path's Renewal — Signature Track Maintenance", "Compounded", 20,
  "The Signature method renews the path as traffic wears it: tamping lifting and packing the ballast back to true, grinding reshaping the rail's crown to its proper curve. "
  "The pounding of tonnes is relentless; the renewal is rhythmic, driven by measurement rather than the calendar's whim. "
  "Deferred renewal is a debt to safety, and safety always collects.",
  "Tampers lift, squeeze, and verify; stabilizers settle the fresh work into lasting truth. "
  "Grinders erase the corrugation and restore the guiding profile, quieting the ride and sparing the wheels. "
  "Geometry cars and ultrasonic eyes say where the machines must go.",
  ["Renewal rhythmic: tamping for truth, grinding for profile.",
   "Measurement commands; the calendar merely suggests.",
   "Deferred renewal a debt safety collects.",
   "Stabilizers settling fresh work into lasting truth."],
  ["Tampers, grinders, stabilizers - owned or hired.",
   "Geometry and ultrasonic watch programs.",
   "Ballast at hand for renewal."],
  ["Work zones guarded: lookouts, possessions, restrictions.",
   "Track returned only when geometry proves fit.",
   "Heat precautions against buckling."],
  ["UIC maintenance standards (public standards).",
   "The public edition maintenance record, for the mechanics (this system)."],
  "cant", {"v_kmh": 140.0, "radius_m": 1200.0}),

R("The High Grid — Signature Electrification", "Compounded", 21,
  "The Signature method raises the high grid above the rails: substations feeding the wire, the wire feeding the trains, the rails carrying the current home. "
  "AC for the main roads, DC for the metros and the old networks - each chosen for its ground. "
  "Protection clears the fault in a heartbeat, for 25,000 volts unforgiving demands reverence.",
  "Substations transform the grid's power to the railway's voltage and feed the sections through breakers. "
  "Sectioning lets faults be isolated and maintenance take its possessions; autotransformers stretch the AC feeding. "
  "Impedance bonds guide the return through the rails, and relays watch without sleeping.",
  ["The high grid: substations feeding, wire carrying, rails returning.",
   "AC for mains, DC for metros - each to its ground.",
   "Sectioning for faults and possessions.",
   "Protection swifter than the fault's violence."],
  ["Substations, wire, and return to the sworn spec.",
   "Relays tested and coordinated.",
   "Windows for tending the high plant."],
  ["Isolation and earthing before wire work.",
   "Clearances kept for the voltage.",
   "Stray currents watched where DC meets buried metal."],
  ["UIC electrification leaflets (public standards).",
   "The public edition electrification record, for the mechanics (this system)."],
  "energy", {"mass_t": 800.0, "v_kmh": 200.0}),

R("The Paid Promise — Signature Ticketing", "Compounded", 22,
  "The Signature method sells the journey as a paid promise: fares reckoned by distance, time, and class, sold through every channel, honored at gate and on board. "
  "The account holds the ticket in the cloud; the phone or card is merely the key. "
  "Paying is made easy and evading made hard - the honest majority must never subsidize the dodging few.",
  "Fare tables speak the prices; channels - app, machine, office, conductor - sell entitlements to account or token. "
  "Gates and conductors validate; the back office divides through-revenue between the roads that carried. "
  "Evasion is measured by survey and met with barrier sense, honest inspection, and fares plain enough to understand.",
  ["The journey a paid promise, honored at gate and board.",
   "The ticket in the cloud; the card merely the key.",
   "Paying easy, evading hard.",
   "Through-revenue divided between the carrying roads."],
  ["Channels: app, machines, office, on-board.",
   "Validation gear and a settlement house.",
   "Evasion measured by survey."],
  ["Fares published and honored as sold.",
   "Penalties lawful and proportionate.",
   "Concessions administered fairly."],
  ["National ticketing regulations (public regulations).",
   "The public edition ticketing record, for the mechanics (this system)."],
  "capacity", {"cars": 4, "seats": 300}),

R("The Rested Crew — Signature Crew Scheduling", "Compounded", 23,
  "The Signature method rosters crews as it would guard treasure: qualified hands on every train, hours within the law, rest that truly restores. "
  "No legal crew, no train - the roster is critical path. "
  "Fatigue is the silent enemy; the schedule must give real sleep, not paper compliance.",
  "Turns are built from the timetable's demand, matched to qualifications - road knowledge, traction, certification. "
  "Duty is capped and rest mandated by law; spare crews stand ready for sickness and disruption. "
  "Depots hold crews where trains are born; deadheading carries them as travelers to where they are needed.",
  ["Qualified hands on every train; rest that truly restores.",
   "No legal crew, no train.",
   "Fatigue the silent enemy; real sleep the defense.",
   "Spare crews for sickness and storm."],
  ["Rostering with qualification truth.",
   "Depots where the trains are born.",
   "Spare cover for the fragile timetable."],
  ["Hours law obeyed in spirit, not just letter.",
   "Fatigue managed, never merely filed.",
   "Road knowledge current for every driver."],
  ["Hours-of-service regulations (public regulations).",
   "The public edition crew record, for the mechanics (this system)."],
  "runtime", {"dist_km": 180.0, "avg_kmh": 90.0, "stops": 4, "dwell_min": 3.0}),
]

SIG += [
R("The Unsleeping Guardian — Signature Train Control", "Advanced", 24,
  "The Signature method sets the automatic guardian above the driver: ETCS and PTC watching speed and signals, warning first, then braking where the human falters. "
  "The system knows each train's granted road and its allowed swiftness, and intervenes before the limit is passed. "
  "The age when a missed signal meant disaster is ended by this vigilance.",
  "Movement is granted by trackside or radio; the onboard mind weighs speed against the allowed profile and the distance to the bound. "
  "The driver is warned; if the warning goes unheeded, the machine brakes. "
  "From lineside supervision to full radio cab-signaling, the guardian scales - and every intervention is proven, not assumed.",
  ["The unsleeping guardian above the driver.",
   "Warning first, then the machine's braking.",
   "Each train's road and swiftness known and bounded.",
   "The missed signal no longer meaning disaster."],
  ["Onboard minds and trackside/radio grantors, speaking together.",
   "A track truth complete and current.",
   "Back-office grantors of authorities and restrictions."],
  ["Safety proven to the highest integrity.",
   "Intervention tested in truth.",
   "Temporary bounds entered promptly and rightly."],
  ["ETCS specifications (public standards).",
   "The public edition train-control record, for the mechanics (this system)."],
  "headway", {"speed_kmh": 160.0, "block_km": 4.0}),

R("The Moving Rooms — Signature CBTC", "Advanced", 25,
  "The Signature method grants each metro train a moving room: no fixed blocks, but exactly the space it needs, reported by radio breath by breath. "
  "Headways shrink below ninety seconds, and the two-track tunnel out-carries the highway above. "
  "The zone minds compute each train's limit; the onboard guardian enforces it; the automatic driver may drive beneath the guardian's eye.",
  "Trains fix their place by balise and odometry and radio it unceasingly; zone controllers reckon each limit of authority. "
  "Protection enforces; operation may drive. "
  "And when the radios falter, fallback modes keep the city moving - for the metro stopped is the city stopped.",
  ["Each train a moving room, exactly its needed space.",
   "Radio breath reporting place unceasingly.",
   "Ninety-second headways: the tunnel out-carrying the highway.",
   "Fallback modes when the radios falter."],
  ["Zone minds and radio covering every meter.",
   "Onboard guardianship on every train.",
   "Fallback crafts for radio failure."],
  ["Safety case whole and proven.",
   "Place-uncertainty bounded and demonstrated.",
   "The safety radio guarded against cyber ill."],
  ["IEEE 1474 CBTC standards (public standards).",
   "The public edition CBTC record, for the mechanics (this system)."],
  "headway", {"speed_kmh": 70.0, "block_km": 0.8}),

R("The Swift Road — Signature High-Speed", "Advanced", 26,
  "The Signature method runs the swift road at 250 km/h and beyond: dedicated, sealed, gently curving - the train that outruns the short-haul jet. "
  "Aerodynamics cheat the wind, slab track holds its truth at speed, in-cab signals speak where lineside eyes would blur. "
  "The most demanding road, and the most rewarding: cities joined as neighborhoods.",
  "Streamlined sets with strength along their length seal against tunnel pressure; slab track keeps geometry where ballast would take flight. "
  "Curves are gentle, crossings banished, the road fenced from the world. "
  "The cab signals carry the authority, and the night belongs to maintenance - non-negotiable, for speed forgives nothing.",
  ["The swift road: 250 km/h and beyond, sealed and gentle.",
   "Aerodynamics, slab track, cab signals: built for swiftness.",
   "Outrunning the short-haul jet under 800 km.",
   "The night belonging to maintenance."],
  ["Dedicated road built to swiftness's demands.",
   "Sets with distributed strength.",
   "Cab signaling along the whole."],
  ["No grade crossings on the swift road.",
   "Pressure and crosswind armored.",
   "Intrusion and quake watched where the land demands."],
  ["UIC high-speed standards (public standards).",
   "The public edition high-speed record, for the mechanics (this system)."],
  "braking", {"v_kmh": 300.0, "decel": 0.8}),

R("The Loom of Time — Signature Network Optimization", "Advanced", 27,
  "The Signature method weaves the network as a loom weaves cloth: retiming, replatforming, repathing, until the fixed steel yields its utmost service. "
  "Minutes saved at the binding junction free the whole web; conflicts are the knots, and the optimizer's art is untying them. "
  "The plan is proven in simulation against delay before it ever meets the public.",
  "The network is drawn as a graph of conflicts - junctions, platforms, single roads. "
  "Trains are retimed to part the conflicts, platforms reassigned to the spare faces, freight repathed around the passenger flood. "
  "Simulation storms the plan with delays, and only the robust is published.",
  ["The network a loom; the optimizer its weaver.",
   "Minutes at the binding junction freeing the web.",
   "Conflicts the knots; retiming the untying.",
   "Proven in simulation before publication."],
  ["A network model with true times and bindings.",
   "Simulation craft for robustness.",
   "Performance truth to school the model."],
  ["Plans proven safe before adoption.",
   "Promised connections kept.",
   "Capacity shared fairly between roads."],
  ["Railway operations research literature (public publications).",
   "The public edition optimization record, for the mechanics (this system)."],
  "runtime", {"dist_km": 500.0, "avg_kmh": 130.0, "stops": 8, "dwell_min": 2.0}),

R("The Banking of Curves — Signature Geometry", "Advanced", 28,
  "The Signature method banks the curves as a rider leans: cant - superelevation - set so the design speed rides in balance, neither thrown outward nor grinding the low rail. "
  "Millimeters decide comfort, wear, and safety; the geometry car reads them unceasingly. "
  "Deficiency is borrowed speed, permitted within law; excess is the slow freight's tax on the low rail.",
  "Equilibrium cant answers the formula: 11.8 × V²/R millimeters on the standard measure. "
  "Faster than equilibrium borrows against comfort; slower pays in low-rail wear. "
  "Gauge, alignment, level, twist, and cant are measured in one pass, and tamping restores what the tonnes take.",
  ["Banking the curves as a rider leans.",
   "Millimeters deciding comfort, wear, safety.",
   "Deficiency borrowed speed; excess the slow tax.",
   "Measured unceasingly, restored rhythmically."],
  ["Geometry watch over the whole network.",
   "Cant designed for speed, curve, and traffic's mix.",
   "Tamping that restores cant, not merely level."],
  ["Deficiency within the law's leave.",
   "Twist faults found before they threaten.",
   "Restrictions where geometry fails tolerance."],
  ["UIC geometry standards (public standards).",
   "The public edition geometry record, for the mechanics (this system)."],
  "cant", {"v_kmh": 160.0, "radius_m": 1500.0}),

R("The Layered Shield — Signature Railway Safety", "Advanced", 29,
  "The Signature method shields the railway in layers: train control above the driver, interlocking at the junctions, detectors watching the rolling stock, and over all the safety management system with its reporting, audits, and root-cause hunts. "
  "No single failure - of human or machine - may reach through every layer. "
  "The creed: every accident taught, every lesson shared across the industry.",
  "Guardians supervise speed and signals; referees forbid conflicting roads; hot-box and dragging-gear eyes watch the trains themselves. "
  "Crossings are guarded, intrusions detected, fires answered. "
  "Above all, the management system: risks weighed, near-misses welcomed without punishment, every incident pursued to its root.",
  ["The layered shield: no single failure reaching through.",
   "Guardians, referees, and watchful detectors.",
   "Near-misses welcomed, never punished.",
   "Every accident taught; every lesson shared."],
  ["The whole stack: control, interlocking, detection, guarding.",
   "A safety management with true authority.",
   "Investigation independent of operation."],
  ["Safety cases kept and audited.",
   "Reporting sheltered from retribution.",
   "Recommendations tracked to done."],
  ["CENELEC railway safety standards (public standards).",
   "The public edition safety record, for the mechanics (this system)."],
  "braking", {"v_kmh": 140.0, "decel": 0.85}),

R("The Two-Mode Road — Signature Intermodal", "Advanced", 30,
  "The Signature method joins the modes: rail for the long road's efficiency, truck for the first and last mile's reach - the container the handshake between them. "
  "Double-stack trains run like clockwork between the hubs, and reliability is the cargo: the box arriving on the promised day. "
  "The terminal is the hinge where the modes embrace.",
  "Cranes and stackers pass boxes between train and truck; scheduled trains run hub to hub on protected capacity. "
  "Loading plans balance weight and destination; well cars bear the double stack beneath the cleared bridges. "
  "The shipper buys the promise of the day; the railroad that keeps it owns the lane.",
  ["Rail the long road, truck the last mile, the box the handshake.",
   "Double-stack clockwork between hubs.",
   "Reliability the cargo; the promised day the product.",
   "The terminal the hinge of modes."],
  ["Terminals with lift gear and truck gates.",
   "Well cars and cleared double-stack roads.",
   "Scheduled trains with guarded capacity."],
  ["Weights declared and proven.",
   "Stacking and securement per the rules.",
   "Hazmat per the dangerous-goods law."],
  ["Intermodal operating practices (public publications).",
   "The public edition intermodal record, for the mechanics (this system)."],
  "capacity", {"cars": 100, "seats": 200}),

R("The Ledger of the Road — Signature Railway Economics", "Advanced", 31,
  "The Signature method reckons the railway's ledger honestly: great fixed costs in road and rolling stock, small marginal cost per added tonne or traveler - so fullness is fortune and emptiness is ruin. "
  "Pricing must cover the variable and tithe to the fixed; yield fills the quiet hours cheaply while the peak pays full. "
  "The decades-long view judges the building: time saved, smoke spared, roads unworn.",
  "Fixed and variable are parted truthfully; rates are set to cover the moving cost and feed the standing. "
  "Off-peak seats go cheaply to fill, peak seats dearly to pay; freight contracts wed rate to volume sworn. "
  "Appraisals count the long benefits against the billions of building.",
  ["Fullness fortune, emptiness ruin: the fixed-cost law.",
   "Pricing covering the variable, tithing to the fixed.",
   "Yield filling the quiet, charging the peak.",
   "The decades judging the building."],
  ["Cost truth parted: fixed from variable.",
   "Demand foresight for pricing and building.",
   "Funding fitted to the mission."],
  ["Rates published, none favored unlawfully.",
   "Public coin accounted openly.",
   "Safety never the balancing item."],
  ["Railway economics literature (public publications).",
   "The public edition economics record, for the mechanics (this system)."],
  "econ", {"fixed": 5000000.0, "price": 45.0, "varcost": 18.0, "units": 400000.0}),

R("The Open Door — Signature Accessibility", "Advanced", 32,
  "The Signature method holds the door open for all: step-free from street to seat, tactile paths for the blind, voices and signs for the deaf, and assistance that keeps its appointment. "
  "The accessible road serves the elder, the injured, the parent with the stroller - all the people the stairs would turn away. "
  "The booked helper must be waiting; the promise broken is trust broken.",
  "Lifts and ramps, tactile paving, accessible machines and toilets, information in sight and sound. "
  "Wheelchair rooms with restraints, accessible toilets, boarding aids, priority seats. "
  "Assistance booked and delivered - the traveler's appointment with the railway, kept.",
  ["The door open for all: step-free, tactile, voiced, assisted.",
   "Serving all the stairs would turn away.",
   "The booked helper waiting: promise kept.",
   "The old retrofitted, the new built right."],
  ["Step-free ways, lifts, ramps, tactile paths.",
   "Accessible vehicles: rooms, toilets, boarding.",
   "Assistance booked and truly delivered."],
  ["Standards met on new and altered works.",
   "Assistance failures pursued like service failures.",
   "Information in many forms."],
  ["Accessibility regulations for rail (public regulations).",
   "The public edition accessibility record, for the mechanics (this system)."],
  "capacity", {"cars": 6, "seats": 80}),

R("The Floating Future — Signature Maglev and Beyond", "Advanced", 33,
  "The Signature method dreams forward: maglev floating on magnetic will, freed from wheel and rail's limits, running 400 to 600 km/h; batteries bridging the unwired valleys; hydrogen for the long diesel roads. "
  "The physics is proven - attraction and repulsion both fly; the guideway's cost is the trial. "
  "And autonomy approaches, supervised from the control centers, on roads set apart.",
  "Electromagnets draw the train to the guideway, or superconducting magnets repel it to float - linear motors driving, guidance failing safe. "
  "Battery trains cross the gaps between wires; hydrogen carries the long unwired journeys. "
  "New systems earn their passengers by certification, not by promise.",
  ["Floating on magnetic will, freed from contact's limits.",
   "Physics proven; the guideway's cost the trial.",
   "Batteries bridging valleys, hydrogen the long roads.",
   "Certification before passengers, always."],
  ["Guideway or road fitted to the art.",
   "Power and control for the chosen physics.",
   "A safety case for the novel."],
  ["Levitation and guidance failing safe.",
   "Hydrogen and battery per the energy laws.",
   "No passengers before certification."],
  ["Maglev engineering literature (public publications).",
   "The public edition future-systems record, for the mechanics (this system)."],
  "energy", {"mass_t": 500.0, "v_kmh": 500.0}),

R("The Keeper of the Road — Signature Mastery", "Advanced", 34,
  "The keeper of the road holds the whole railway as one living vow: track, trains, signals, timetables, and people moving as one body, the traveler at the end of every gauge. "
  "Each earlier record was a single art; this is the art of arts - reading the network as the pilot reads the sky. "
  "The master balances timetable, safety, and ledger, sacrificing none.",
  "From the service promise reason inward: the track bearing it, the trains running it, the signals guarding it, the timetable scheduling it, the crews working it. "
  "Keep the daily rhythm - operations, windows, review - and the long rhythm - renewals, investment, growth. "
  "Watch the gauges - punctuality, safety, fullness, cost per train-kilometer, the people's contentment - and let every decision lift at least one.",
  ["The whole railway one living vow.",
   "Reason inward from the promise.",
   "Timetable, safety, ledger: none sacrificed.",
   "The daily rhythm and the long rhythm kept."],
  ["The full ladder fluent, foundations through advanced.",
   "A command that never sleeps.",
   "Gauges read together, honestly."],
  ["Safety never traded for performance.",
   "Published services delivered or honestly remade.",
   "People treated lawfully, grown continually."],
  ["The public edition mastery record, for the mechanics (this system).",
   "Signature system governance on original works (this system)."],
  "headway", {"speed_kmh": 120.0, "block_km": 3.0}),
]

GEN_DEMOFN = """function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\\n"
   + "# Braking-distance structural sample calculator (railway systems)\\n"
   + "v, a = 27.8, 0.9\\n"
   + "d = v*v/(2*a)\\n"
   + "print('sample speed m/s:', v)\\n"
   + "print('sample braking distance m:', round(d,1))\\n"
   + "assert d > 0\\n"
   + "print('OK: structural sample demo ran')\\n";
}
"""
