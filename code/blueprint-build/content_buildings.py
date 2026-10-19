#!/usr/bin/env python3
"""Building blueprint archetype families: houses, stores, offices, warehouses."""
# Each archetype: name, group, style, history, layout, structure, systems,
# spaces [(name,w,d) in feet], materials, codes, sheets, variants.

HOUSES = [
 dict(name="Ranch House", group="Single-Story", style="Mid-Century Ranch",
  history=("The ranch house rose with postwar suburban America after 1945. Builders working "
   "on concrete slabs proved a long, low single-story home could be mass-produced quickly, and "
   "millions of ranches went up across the United States through the 1960s. Its DNA traces to "
   "Spanish colonial haciendas and Frank Lloyd Wright's Prairie houses: horizontal lines, deep "
   "eaves, and living space that opens to the yard."),
  layout=("All rooms sit on one level along a central hall or open core. Public rooms cluster at "
   "the front near the entry; bedrooms retreat to the quiet wing. The attached garage anchors one "
   "end of the long rectangle, giving the classic rambling silhouette."),
  structure=("Platform-framed 2x4 or 2x6 exterior walls on a monolithic concrete slab or crawlspace. "
   "Low-pitched gable or hip roof with pre-engineered trusses spanning the full width, so interior "
   "walls carry no roof load and floor plans stay flexible."),
  systems=("Forced-air furnace with ductwork in the attic or crawlspace; 200-amp electrical service; "
   "plumbing wet-wall shared between kitchen and baths. Simple systems keep first cost and "
   "maintenance low."),
  spaces=[("Living Room",16,14),("Kitchen",12,10),("Dining",12,10),("Primary Bedroom",14,12),
   ("Bedroom 2",12,11),("Bedroom 3",11,10),("Bath",8,6),("Hall Bath",8,6),("Utility",8,8),("Garage",20,20)],
  materials=["2x4/2x6 SPF wall framing","Engineered roof trusses","Concrete slab foundation",
   "Brick veneer or fiber-cement siding","Asphalt shingle roof","Double-pane vinyl windows",
   "Fiberglass batt insulation R-13/R-38","3/4 in. subfloor with finish flooring"],
  codes=["IRC R301 design criteria","IRC R602 wall framing","IRC R802 roof framing","NEC 2023 dwelling requirements"],
  sheets=["A-101 Floor Plan","A-201 Elevations","A-301 Sections","S-101 Foundation Plan","E-101 Electrical Plan"]),
 dict(name="Cape Cod Cottage", group="Single-Story", style="Cape Cod Colonial",
  history=("The Cape Cod cottage descends from 17th-century English cottages built by New England "
   "colonists: a steep roof to shed snow, a massive central chimney, and shutters against Atlantic "
   "storms. Revival builders in the 1930s to 1950s made it America's starter home - small, "
   "symmetrical, and easy to expand upward into the unfinished attic."),
  layout=("A compact rectangle with the front door centered between two multi-pane windows. Living "
   "room and kitchen share the ground floor; steep roof slopes leave a half-story above for two "
   "dormered bedrooms. The central chimney serves fireplace and furnace flue together."),
  structure=("Balloon or platform framing with 2x8 or 2x10 roof rafters on a steep 10:12 to 12:12 "
   "pitch. Full basement or crawlspace foundation of poured concrete or block. Knee walls and "
   "collar ties shape the upstairs rooms."),
  systems=("Hot-water baseboard or forced air from a basement furnace; chimney flue sized for the "
   "heating appliance plus fireplace. Dormer windows bring light and egress to the half-story."),
  spaces=[("Living Room",15,13),("Kitchen",11,10),("Dining Nook",9,8),("Bedroom Down",12,10),
   ("Bedroom Up 1",12,10),("Bedroom Up 2",11,9),("Bath",8,6),("Hall Bath",7,6),("Entry",6,6)],
  materials=["2x6 wall framing","2x10 roof rafters","Cedar shingle or clapboard siding",
   "Poured concrete foundation","Asphalt shingle roof","Wood double-hung windows",
   "Central masonry chimney","Hardwood floors"],
  codes=["IRC R301 design criteria","IRC R802 roof framing","IRC R310 emergency escape windows","NEC 2023 dwelling requirements"],
  sheets=["A-101 First Floor Plan","A-102 Second Floor Plan","A-201 Elevations","S-101 Foundation Plan"]),
 dict(name="Colonial Two-Story", group="Two-Story", style="Georgian Colonial Revival",
  history=("The two-story colonial descends from Georgian houses of the 1700s: strict symmetry, a "
   "center hall, and evenly spaced double-hung windows. The Colonial Revival wave of 1890 to 1940 "
   "made it the default respectable American house, and it remains the best-selling two-story "
   "form because it stacks bedrooms efficiently over living space."),
  layout=("Center-hall plan: entry opens to a stair hall with living room left and dining room right. "
   "Kitchen sits rear with family space beyond; four bedrooms and baths fill the second floor. "
   "Perfect symmetry keeps the structure simple and the facade formal."),
  structure=("Platform framing floor by floor; second-floor joists bear on the first-floor wall plates. "
   "Gable roof at 8:12 pitch with ridge beam or trusses. Full basement foundation carries two "
   "stories of load - footing widths sized for the doubled bearing."),
  systems=("Zoned forced air (one system per floor) or two separate units; plumbing stacks grouped "
   "back-to-back between floors to shorten runs. Stair hall doubles as a return-air chase."),
  spaces=[("Living Room",15,13),("Dining Room",14,12),("Kitchen",13,11),("Family Room",16,13),
   ("Foyer",8,10),("Primary Bedroom",15,13),("Bedroom 2",12,11),("Bedroom 3",12,10),("Bedroom 4",11,10),
   ("Primary Bath",10,8),("Hall Bath",8,6),("Laundry",8,6)],
  materials=["2x6 exterior wall framing","2x10 floor joists","Poured concrete basement walls",
   "Brick or siding veneer","Asphalt shingle roof","Double-hung windows with shutters",
   "Hardwood stair with oak rail","Fiberglass insulation R-19/R-38"],
  codes=["IRC R301 design criteria","IRC R502 floor framing","IRC R311 stairways","NEC 2023 dwelling requirements"],
  sheets=["A-101 First Floor Plan","A-102 Second Floor Plan","A-201 Elevations","S-101 Foundation Plan","M-101 HVAC Plan"]),
 dict(name="Craftsman Bungalow", group="Single-Story", style="Arts and Crafts Bungalow",
  history=("The Craftsman bungalow grew from the Arts and Crafts movement and the pattern books of "
   "Greene and Greene in Pasadena around 1905. Gustav Stickley's magazine 'The Craftsman' spread "
   "the gospel of honest joinery, exposed structure, and the deep front porch. Sears and Aladdin "
   "sold thousands as kit houses by mail order in the 1910s and 1920s."),
  layout=("A wide front porch spans the facade under the main gable. Inside, living and dining rooms "
   "flow together around a central fireplace; a short hall leads to two or three bedrooms and one "
   "or two baths. Built-ins - window seats, colonnades, bookcases - replace freestanding furniture."),
  structure=("Low 1.5-story massing with exposed rafter tails and knee braces at the eaves. Front "
   "porch carried on tapered square columns over stone or brick piers. Roof pitches of 6:12 to "
   "8:12 with clipped or jerkinhead gables on many examples."),
  systems=("Originally coal furnace with gravity octopus ductwork; modern retrofits use high-velocity "
   "mini-ducts or ductless heat pumps that thread through the low attic. Porch and deep eaves shade "
   "summer sun while admitting winter light."),
  spaces=[("Front Porch",20,8),("Living Room",15,13),("Dining Room",13,11),("Kitchen",12,10),
   ("Primary Bedroom",13,12),("Bedroom 2",11,10),("Bedroom 3",10,9),("Bath",8,6),("Hall Bath",7,5),("Nook",8,8)],
  materials=["Exposed rafter tails","Tapered porch columns","Stone or brick porch piers",
   "Wood clapboard and shingle siding","Built-in cabinetry","Oak trim and floors",
   "Asphalt or cedar shingle roof","Poured concrete foundation"],
  codes=["IRC R301 design criteria","IRC R802 roof framing","IRC R311 porches and guards","NEC 2023 dwelling requirements"],
  sheets=["A-101 Floor Plan","A-201 Elevations","A-301 Sections","D-101 Millwork Details"]),
 dict(name="Farmhouse", group="Single-Story", style="Vernacular Farmhouse",
  history=("The American farmhouse is vernacular building at its purest: a simple gabled box, a "
   "full-width porch for shade and work, and additions tacked on as families and fortunes grew. "
   "From the 1800s through the Depression, farm families built with local lumber and their own "
   "labor, which is why the form varies by region but always reads as honest shelter."),
  layout=("The porch is an outdoor room - often 8 to 10 feet deep - running the full front. Behind "
   "it, a central living space with the kitchen at the rear near the old summer kitchen or mudroom. "
   "Bedrooms stack simply; many farmhouses grew a rear ell for the kitchen and a second stair."),
  structure=("Heavy timber or balloon framing with board sheathing; tall 9:12 to 12:12 gable roofs "
   "shed snow and hold a vented attic. Porch roofs framed as shed extensions of the main roof, "
   "carried on simple turned or square posts."),
  systems=("Wood stove or boiler heat historically; modern builds use heat pumps with the vented "
   "attic as a buffer. Deep porches and high ceilings drive passive cooling - the original "
   "climate control."),
  spaces=[("Wraparound Porch",30,9),("Living Room",16,14),("Kitchen",14,12),("Dining",13,11),
   ("Mudroom",10,8),("Primary Bedroom",14,12),("Bedroom 2",12,11),("Bedroom 3",11,10),
   ("Bath",8,6),("Pantry",6,8)],
  materials=["Board-and-batten or clapboard siding","Standing-seam metal roof","Turned wood porch posts",
   "Heavy timber or 2x framing","Stone pier or concrete foundation","Wood plank floors",
   "Masonry chimney","Screened porch panels"],
  codes=["IRC R301 design criteria","IRC R802 roof framing","USDA rural housing guidance","NEC 2023 dwelling requirements"],
  sheets=["A-101 Floor Plan","A-201 Elevations","A-301 Sections","S-101 Foundation Plan"]),
 dict(name="Split-Level", group="Multi-Level", style="Mid-Century Split-Level",
  history=("The split-level answered the 1950s builder's dilemma: give buyers three living levels on "
   "a small lot without the cost of a full two-story. Staggering the floor by half a story cut "
   "stair runs in half and let the garage tuck under the bedroom wing. Millions were built from "
   "about 1955 to 1975, and the form still defines postwar suburbs."),
  layout=("Entry lands mid-flight: half a flight up to the bedroom level, half a flight down to the "
   "family room. Living room, dining, and kitchen share the main level. The garage sits under the "
   "bedrooms, and the lower level opens to the backyard at grade."),
  structure=("Three staggered platform-framed boxes sharing foundation walls; the mid-level slab or "
   "joists bear on the lower walls. Short stair runs of 6 to 7 risers connect levels. Retaining "
   "details matter where the lower level meets grade."),
  systems=("One forced-air system struggles with three levels, so good designs zone by level or use "
   "two units. The below-grade family room needs careful waterproofing and a sump or daylight drain."),
  spaces=[("Living Room",15,13),("Dining",12,10),("Kitchen",12,10),("Family Room",16,14),
   ("Primary Bedroom",14,12),("Bedroom 2",12,10),("Bedroom 3",11,10),("Bath",8,6),
   ("Hall Bath",8,6),("Garage",20,20),("Entry Foyer",8,8)],
  materials=["2x4/2x6 wall framing","Brick veneer front","Aluminum or vinyl siding",
   "Concrete block lower walls","Asphalt shingle roof","Sliding glass doors to patio",
   "Wrought-iron stair rail","Fiberglass insulation"],
  codes=["IRC R301 design criteria","IRC R311 stairways","IRC R406 foundation waterproofing","NEC 2023 dwelling requirements"],
  sheets=["A-101 Lower Level Plan","A-102 Main Level Plan","A-103 Upper Level Plan","A-201 Elevations"]),
 dict(name="Townhouse", group="Multi-Unit", style="Urban Row Townhouse",
  history=("The townhouse descends from London terraces and the rowhouses of Philadelphia, "
   "Baltimore, and Brooklyn: narrow lots, shared party walls, and three or four stacked floors. "
   "The form returned in force after 1980 as cities re-densified - one narrow footprint, no side "
   "yards, and a garage or patio at the rear."),
  layout=("Typically 16 to 22 feet wide and three stories: garage and entry at grade, open living "
   "and kitchen on the second floor, bedrooms on the third. Party walls are shared with neighbors, "
   "so windows live only front and rear - the stair becomes the light well."),
  structure=("Party walls of masonry or double-stud fire-rated framing with a 2-hour rating between "
   "units. Floor joists or trusses span the narrow width with no interior bearing. Front and rear "
   "walls carry all lateral load - shear detailing at the open garage level is critical."),
  systems=("Stacked plumbing keeps runs short; each unit needs its own HVAC and electrical service. "
   "Sprinklers are commonly required by local amendment for attached dwellings."),
  spaces=[("Garage",18,20),("Entry",8,10),("Living Room",16,14),("Kitchen",12,10),("Dining",11,9),
   ("Primary Bedroom",14,12),("Bedroom 2",12,10),("Bedroom 3",11,10),("Primary Bath",9,7),("Hall Bath",8,6),
   ("Roof Deck",16,10)],
  materials=["Fire-rated party wall assembly","2x6 exterior framing","Brick or fiber-cement facade",
   "Concrete slab garage level","Asphalt or membrane roof","Steel stair stringers",
   "Sprinkler system","Double-pane windows"],
  codes=["IRC R302 fire separation","IRC R302.2 townhouse separation","IBC occupancy R-2/R-3","NEC 2023 dwelling requirements"],
  sheets=["A-101 Ground Floor Plan","A-102 Second Floor Plan","A-103 Third Floor Plan","S-101 Framing Plans"]),
 dict(name="Log Cabin", group="Small / Cabin", style="Horizontal Log Construction",
  history=("Horizontal log construction came to America with Swedish and Finnish settlers in the "
   "1600s and became the frontier shelter of the Appalachian and western expansion. Interlocking "
   "notched corners need no nails; chinking of clay, moss, or mortar seals the gaps. The 1930s "
   "Civilian Conservation Corps built thousands of log park structures that still stand."),
  layout=("The classic single-pen cabin is one room deep with a sleeping loft above. Dogtrot and "
   "saddlebag plans add a second pen across a breezeway. Modern log homes keep the great room with "
   "its massive fireplace as the heart and stack bedrooms in the loft under the ridge."),
  structure=("Full-scribe or milled log walls 8 to 12 inches thick; corners joined by saddle, dovetail, "
   "or butt-and-pass notches. Logs shrink as they dry - slip joints at doors, windows, and the "
   "ridge let the roof settle without racking openings."),
  systems=("Log walls are thermal mass, not insulation - R-values run about R-1.25 per inch, so "
   "roof insulation carries the envelope. Wood stoves pair naturally; wiring runs in chases or "
   "surface-mounted to avoid drilling logs."),
  spaces=[("Great Room",20,16),("Kitchen",12,10),("Dining",12,10),("Primary Bedroom",14,12),
   ("Bedroom 2",12,10),("Loft",20,12),("Bath",8,6),("Mudroom",8,8),("Porch",20,8)],
  materials=["8-12 in. pine or cedar logs","Saddle-notch corners","Chinking and sealant",
   "Stone fireplace and chimney","Standing-seam metal roof","Poured concrete foundation",
   "Heavy timber loft joists","Boric-acid log treatment"],
  codes=["ICC 400 log construction standard","IRC R301 design criteria","IRC R1001 chimneys","NEC 2023 dwelling requirements"],
  sheets=["A-101 Floor Plan","A-102 Loft Plan","A-201 Elevations","D-101 Log Corner Details"]),
 dict(name="Modern Flat-Roof House", group="Two-Story", style="Contemporary Modern",
  history=("The flat-roof modern house descends from the International Style of the 1920s - Le "
   "Corbusier, Mies van der Rohe, and the Bauhaus - filtered through California Case Study Houses "
   "after the war. Cantilevered volumes, walls of glass, and honest structure replaced applied "
   "ornament. Today's versions add high-performance envelopes behind the crisp lines."),
  layout=("Open plan: kitchen, dining, and living share one flowing space with glass walls to the "
   "yard. Private rooms stack or wing off; the roof becomes a terrace. Circulation is minimal - "
   "rooms connect directly, and the stair is a sculptural element, not a hallway."),
  structure=("Steel moment frames or engineered lumber allow long cantilevers and corner glass with "
   "no posts. Flat or single-slope roofs framed with tapered insulation for drainage at 1/4 inch "
   "per foot. Parapets hide the roof edge and mechanical equipment."),
  systems=("Heat pumps with ductless heads suit the open plan; polished concrete floors carry "
   "radiant loops. Deep overhangs and low-E glass manage solar gain - the glass box only works "
   "with a tuned envelope."),
  spaces=[("Great Room",24,18),("Kitchen",14,12),("Dining",14,10),("Primary Suite",16,14),
   ("Bedroom 2",13,11),("Bedroom 3",12,10),("Bath",9,7),("Hall Bath",8,6),("Study",10,10),("Roof Terrace",24,12)],
  materials=["Steel moment frame","Engineered lumber beams","Floor-to-ceiling low-E glazing",
   "TPO or EPDM membrane roof","Polished concrete floors","Cedar or metal rainscreen siding",
   "Tapered roof insulation","Ductless heat pump system"],
  codes=["IRC R301 design criteria","IBC structural provisions","IECC energy code","NEC 2023 dwelling requirements"],
  sheets=["A-101 Floor Plan","A-102 Upper Floor Plan","A-201 Elevations","S-101 Structural Plans"]),
 dict(name="Accessory Dwelling Unit", group="Small / Cabin", style="ADU / Granny Flat",
  history=("Accessory dwelling units - granny flats, in-law suites, backyard cottages - are among "
   "the oldest housing forms, but modern ADU law is new: California's 2017-2020 reforms and "
   "similar laws nationwide made small second homes legal by right on most residential lots. They "
   "add gentle density without changing neighborhood character."),
  layout=("Everything within 400 to 1,200 square feet: an open living-kitchen core, one or two "
   "bedrooms, a full bath, and stacked laundry. Detached units face the alley or garden; attached "
   "units share a wall with the main house but need their own entry."),
  structure=("Light platform framing identical to small-house construction; slab or raised foundation. "
   "Because spans are short, framing is simple - 2x8 joists and 2x4 walls handle most ADUs. Fire "
   "separation from the main house follows local ADU ordinance."),
  systems=("A single ductless mini-split heats and cools the whole unit; a 100-amp subpanel usually "
   "suffices. Tankless water heater and compact appliances fit the small wet wall."),
  spaces=[("Living/Kitchen",18,14),("Bedroom",12,11),("Bedroom 2",10,10),("Bath",8,6),("Entry",6,6),("Laundry",5,5)],
  materials=["2x4/2x6 wall framing","Engineered floor trusses","Fiber-cement siding",
   "Asphalt shingle or metal roof","Mini-split heat pump","Tankless water heater",
   "Compact appliances","Double-pane windows"],
  codes=["IRC R301 design criteria","Local ADU ordinance","IRC R302 fire separation","NEC 2023 dwelling requirements"],
  sheets=["A-101 Floor Plan","A-201 Elevations","S-101 Foundation Plan"]),
 dict(name="Duplex", group="Multi-Unit", style="Side-by-Side Duplex",
  history=("The side-by-side duplex - two mirror-image homes under one roof - boomed in streetcar "
   "suburbs from 1900 to 1930 and again after 1970 as an owner-occupant investment: live in one "
   "side, rent the other. The shared wall halves construction cost per unit while each side keeps "
   "its own front door and yard."),
  layout=("Mirror plan around a central fire-rated party wall: each unit gets its own entry, living "
   "room, kitchen, two or three bedrooms, and bath. Many duplexes stack a second floor over each "
   "side; garages sit at the rear or in the basement."),
  structure=("The party wall is the structural spine - masonry or double-stud with two layers of "
   "5/8-inch Type X drywall each side for the 1-hour (or 2-hour) rating. Floor systems frame "
   "independently per unit so sound and fire stay separated."),
  systems=("Completely separate services per unit: two electrical meters, two HVAC systems, two water "
   "heaters. Sound-rated assemblies at the party wall and staggered outlets keep neighbor noise down."),
  spaces=[("Unit A Living",14,12),("Unit A Kitchen",11,10),("Unit A Bed 1",12,11),("Unit A Bed 2",11,10),
   ("Unit A Bath",8,6),("Unit B Living",14,12),("Unit B Kitchen",11,10),("Unit B Bed 1",12,11),
   ("Unit B Bed 2",11,10),("Unit B Bath",8,6),("Shared Wall",40,1)],
  materials=["Fire-rated party wall","2x6 exterior framing","Separate electrical services",
   "Two HVAC systems","Brick or siding veneer","Asphalt shingle roof",
   "Sound-rated floor assembly","Concrete foundation"],
  codes=["IRC R302 fire separation","IRC R302.3 two-family separation","NEC 2023 two services","IECC energy code"],
  sheets=["A-101 Unit A Plan","A-102 Unit B Plan","A-201 Elevations","S-101 Framing Plans"]),
 dict(name="Storybook Cottage", group="Small / Cabin", style="Storybook / English Cottage",
  history=("The storybook cottage grew from the English Cotswold vernacular and the 1920s Hollywood "
   "romance with thatched, crooked charm - rolled eaves, arched doors, and diamond-pane windows. "
   "Builders in Los Angeles and the Pacific Northwest turned the fairy-tale into small, "
   "affordable homes with hand-made character."),
  layout=("An irregular, cozy plan: a tiny entry vestibule, an inglenook living room with fireplace, "
   "a galley kitchen, and two small bedrooms tucked under steep eaves. No hallway is wasted - rooms "
   "open directly off each other around the hearth."),
  structure=("Steep 12:12 to 16:12 roofs with rolled eaves formed by layered shingles over curved "
   "framing. Thick stucco or stone walls, arched openings with brick or timber lintels, and small "
   "dormers for upstairs light."),
  systems=("Small volumes heat easily - a single stove or mini-split often suffices. Deep reveals and "
   "small windows are historic, not efficient; modern versions use replica steel windows with "
   "insulated glass."),
  spaces=[("Inglenook Living",14,12),("Kitchen",10,9),("Bedroom 1",11,10),("Bedroom 2",10,9),
   ("Bath",7,6),("Entry Vestibule",6,6),("Nook",7,7)],
  materials=["Stucco over frame or stone walls","Rolled shingle eaves","Arched wood entry door",
   "Diamond-pane replica windows","Brick or stone fireplace","Steep shingle roof",
   "Hand-troweled plaster interior","Poured concrete foundation"],
  codes=["IRC R301 design criteria","IRC R802 roof framing","IRC R310 egress windows","NEC 2023 dwelling requirements"],
  sheets=["A-101 Floor Plan","A-201 Elevations","D-101 Eave Details"]),
]

STORES = [
 dict(name="General Store", group="General Retail", style="Country General Store",
  history=("The country general store was the commercial and social heart of rural America from the "
   "1700s through the early 1900s: one room selling dry goods, hardware, and groceries, with a "
   "potbelly stove and cracker barrel for gathering. Sears catalogs and then chain stores ended "
   "its reign, but the form survives in farm supply and dollar stores."),
  layout=("Open sales floor with perimeter shelving and a central checkout counter near the entry. "
   "The stove corner becomes a seating nook in modern versions. Stockroom and office sit at the "
   "rear with a loading door to the alley."),
  structure=("Simple rectangular box: wood or steel frame, gable or flat roof, storefront glazing "
   "across the front. Clear spans of 20 to 30 feet keep the sales floor column-free."),
  systems=("Rooftop packaged HVAC units; high-bay LED lighting over aisles; point-of-sale and "
   "security wiring in a ceiling raceway. Floors must take rolling loads from stock carts."),
  spaces=[("Sales Floor",40,30),("Checkout",12,8),("Stockroom",20,15),("Office",10,10),
   ("Restroom",8,6),("Entry Vestibule",8,8),("Loading",12,10)],
  materials=["Steel or wood frame","Storefront aluminum glazing","Concrete slab floor",
   "Metal panel or brick facade","Membrane roof","High-bay LED fixtures","Slatwall shelving"],
  codes=["IBC mercantile occupancy","IBC egress Chapter 10","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-201 Storefront Elevation","M-101 HVAC Plan"]),
 dict(name="Supermarket", group="Food Retail", style="Modern Supermarket",
  history=("The supermarket was born in 1930 when Michael Cullen opened King Kullen in Queens with "
   "self-service aisles and low margins. Clarence Saunders' Piggly Wiggly had pioneered self-service "
   "in 1916. The postwar version added produce, meat, dairy, and frozen departments under one "
   "40,000-square-foot roof - the template every grocery still follows."),
  layout=("Racetrack perimeter: produce at entry, then meat, deli, dairy, and frozen along the walls; "
   "dry grocery aisles fill the center. Checkout lanes face the exit vestibule; carts stage outside. "
   "Back-of-house - prep, coolers, loading - runs the full rear wall."),
  structure=("Steel frame with bar-joist roof spanning 30 to 40 feet; tilt-up concrete or metal panel "
   "walls. Roof must carry heavy refrigeration and HVAC tonnage - structural allowances are "
   "generous. Slab designed for cooler footings and floor drains."),
  systems=("Parallel-rack refrigeration is the heart of the building - often a third of energy use. "
   "Rooftop HVAC with economizers, heat reclaim from refrigeration to hot water, and emergency power "
   "for coolers. Floor drains and hose stations throughout prep areas."),
  spaces=[("Sales Floor",120,80),("Produce",30,20),("Meat Prep",25,20),("Deli/Bakery",25,20),
   ("Dairy Cooler",20,15),("Frozen Aisles",40,12),("Checkout Lanes",40,15),("Stockroom",40,25),
   ("Loading Dock",30,15),("Office",12,10),("Restrooms",12,10)],
  materials=["Structural steel frame","Bar-joist roof deck","Tilt-up concrete walls",
   "Refrigeration rack system","Quarry tile prep floors","Polished concrete sales floor",
   "LED high-bay lighting","Insulated metal panel coolers"],
  codes=["IBC mercantile occupancy","FDA Food Code","ASHRAE 90.1","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-102 Reflected Ceiling","M-101 HVAC Plan","R-101 Refrigeration Plan"]),
 dict(name="Convenience Store", group="Food Retail", style="Convenience / C-Store",
  history=("The convenience store descends from Dallas's Southland Ice Company docks, which began "
   "selling milk and eggs in 1927 - the first 7-Eleven. The formula - small footprint, long hours, "
   "high-margin grab-and-go - now pairs with fuel islands, making the c-store one of the most "
   "engineered small buildings in retail."),
  layout=("Compact sales floor wrapped by cooler doors on two walls; coffee and foodservice anchor "
   "one corner, checkout faces the fuel islands through full glazing. Restrooms and a small office "
   "tuck behind the coolers; canopy columns align clear of drive lanes."),
  structure=("Steel frame box, typically 2,500 to 4,000 square feet, with a separate fuel canopy on "
   "its own columns and foundations. Canopy must clear 16-plus feet for trucks and carry signage "
   "and lighting loads."),
  systems=("Walk-in coolers and freezers dominate the electrical load; LED canopy lighting on "
   "photocells. Fuel systems need leak detection, emergency shutoffs, and classified-area wiring "
   "per fire code."),
  spaces=[("Sales Floor",40,25),("Cooler Line",30,8),("Foodservice",15,12),("Checkout",10,8),
   ("Restrooms",10,8),("Office",8,8),("Stockroom",12,10),("Fuel Canopy",80,30)],
  materials=["Steel frame","Aluminum storefront glazing","Fuel canopy steel","Walk-in cooler panels",
   "Slip-resistant tile","LED canopy lights","EMV fuel dispensers","Membrane roof"],
  codes=["IBC mercantile occupancy","IFC motor fuel dispensing","EPA UST regulations","ADA accessibility"],
  sheets=["A-101 Floor Plan","A-201 Canopy Details","E-101 Fuel System Plan"]),
 dict(name="Clothing Boutique", group="Specialty Retail", style="Boutique Retail",
  history=("The boutique broke from department stores in 1960s London - Mary Quant's Bazaar on King's "
   "Road being the icon - selling a curated point of view instead of everything. The architecture "
   "followed: small rooms, dramatic lighting, and the fitting room as the true sales floor."),
  layout=("A sequence of intimate rooms rather than open aisles: entry gallery, main salon, fitting "
   "suite at the rear with flattering light, and a stockroom hidden behind. Circulation loops so "
   "shoppers pass displays twice."),
  structure=("Usually a tenant fit-out inside a larger shell: demising walls, new storefront, and "
   "interior partitions. Track and accent lighting on ceiling grids; fitting rooms need solid "
   "partitions to the deck for privacy and security."),
  systems=("High-CRI accent lighting (90-plus) is the product - lighting power density is the design "
   "driver. Small packaged HVAC with quiet grilles; security tagging and camera coverage at entry "
   "and fitting rooms."),
  spaces=[("Entry Gallery",15,12),("Main Salon",30,20),("Fitting Suite",15,12),("Cash Wrap",8,8),
   ("Stockroom",15,12),("Office",8,8),("Restroom",7,6)],
  materials=["High-CRI track lighting","Plaster feature walls","Wood or stone flooring",
   "Custom millwork displays","Designer storefront","Acoustic ceiling panels","Security system"],
  codes=["IBC mercantile occupancy","IECC lighting power","ADA fitting rooms","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-801 Interior Elevations","E-101 Lighting Plan"]),
 dict(name="Bookstore", group="Specialty Retail", style="Independent Bookstore",
  history=("The modern independent bookstore descends from 18th-century print shops and the great "
   "19th-century booksellers. After chain superstores peaked in the 1990s, independents survived "
   "by becoming community rooms - readings, cafes, and deep curation. The architecture is shelving: "
   "walls of books need real structure."),
  layout=("Perimeter and spine shelving in 3-to-4-foot aisles; a reading nook or cafe near the front "
   "windows; children's section with low shelving at the rear; event space that converts from "
   "stacks. Receiving and office hide behind the children's area."),
  structure=("Book stacks are heavy - 150 pounds per linear foot of full shelving is the rule of "
   "thumb. Floors need 100-plus psf live load capacity; many bookstores occupy old buildings "
   "whose timber floors were already built stout."),
  systems=("Quiet HVAC matters more than in most retail - readings and browsing need low background "
   "noise. Warm 3000K lighting at shelf faces; daylight control to protect stock from UV."),
  spaces=[("Sales Floor",50,35),("Cafe Nook",15,12),("Children's Area",20,15),("Event Space",20,15),
   ("Receiving",12,10),("Office",10,8),("Restroom",8,6)],
  materials=["Heavy-duty bookshelving","100 psf floor structure","Warm LED shelf lighting",
   "Wood floors","Acoustic ceiling","Cafe millwork","UV-filtering glazing"],
  codes=["IBC mercantile occupancy","IBC floor loads Table 1607.1","ADA accessibility","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-601 Shelving Sections","E-101 Lighting Plan"]),
 dict(name="Hardware Store", group="General Retail", style="Hardware / Home Center",
  history=("The hardware store is among America's oldest retail forms - the village ironmonger "
   "scaled up. Postwar home centers like the first Home Depot (1978, Atlanta) turned it into "
   "warehouse retail: 100,000 square feet of lumber, fasteners, and paint under one roof with "
   "forklift-wide aisles."),
  layout=("Wide main aisles for carts and forklifts; departments in zones - lumber and building "
   "materials along one wall with drive-through pickup, paint and tools in the center, garden at "
   "the rear with outdoor yard. Contractor desk near the pro entrance."),
  structure=("Warehouse bones: steel frame, 25-to-30-foot bays, 20-plus-foot clear height for "
   "rack storage. Floors take forklift wheel loads; the lumber yard needs a covered but open-air "
   "shed with its own drainage."),
  systems=("High-bay lighting over 12-foot racks; dust collection at the key-cutting and lumber "
   "areas; large makeup-air units because the garden center doors stand open. Sprinkler design "
   "follows high-piled storage rules."),
  spaces=[("Sales Floor",150,100),("Lumber Yard",80,40),("Garden Center",60,40),("Paint Dept",30,20),
   ("Tool Corral",25,20),("Contractor Desk",15,10),("Receiving",30,20),("Office",12,10)],
  materials=["Structural steel frame","High-bay racking","Forklift-rated slab",
   "Metal panel walls","Skylights over aisles","Dust collection ducting","ESFR sprinklers"],
  codes=["IBC mercantile + storage","NFPA 13 high-piled storage","IBC egress Chapter 10","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","S-101 Framing Plan","FP-101 Sprinkler Plan"]),
 dict(name="Bakery", group="Food Retail", style="Retail Bakery",
  history=("The retail bakery pairs a production kitchen with a shop front - a form as old as "
   "Pompeii's bakeries, where mills, ovens, and counters shared one building. Modern versions "
   "add the theater of visible ovens: customers buy more when they see and smell the bake."),
  layout=("Production kitchen at the rear with ovens along the wall, makeup tables central, and "
   "proofers and coolers flanking. Retail counter and display cases face the street; a small cafe "
   "corner with a few tables. Flour storage and office tuck beside the kitchen."),
  structure=("Masonry or steel frame; the oven zone needs a dedicated exhaust hood, gas service, and "
   "a slab that takes oven point loads. Display area gets the storefront glazing and the inviting "
   "entry."),
  systems=("Commercial ovens drive the design: Type I hoods, makeup air, and gas sizing dominate. "
   "Flour dust is combustible - electrical in the mixing area follows dust-ignition-proof practice. "
   "Grease and flour waste need interceptors on drains."),
  spaces=[("Retail/Display",25,18),("Cafe Corner",12,10),("Production Kitchen",30,20),
   ("Oven Line",20,8),("Flour Storage",10,8),("Office",8,8),("Restroom",7,6)],
  materials=["Commercial deck ovens","Type I exhaust hood","Stainless prep tables",
   "Quarry tile kitchen floor","Display cases","Storefront glazing","Flour silo or bins"],
  codes=["IMC commercial cooking","NFPA 96 ventilation","FDA Food Code","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","M-101 Hood Plan","P-101 Plumbing Plan"]),
 dict(name="Pharmacy", group="Specialty Retail", style="Retail Pharmacy",
  history=("The pharmacy counter - raised, professional, slightly set apart - descends from the "
   "apothecary shops of the 1700s. Modern retail pharmacy splits the building: a convenience front "
   "end and a secured, regulated dispensary at the back with its own workflow, counseling room, "
   "and records storage."),
  layout=("Front-end retail with aisles and checkout near entry; the pharmacy counter runs along "
   "the rear with a drop-off/pickup window, counseling room beside it, and the dispensary workroom "
   "behind locked doors. Drive-through window on the side wall where the site allows."),
  structure=("Standard retail box; the dispensary adds security layers - solid partitions, limited "
   "openings, and a lockable Dutch door or sliding transaction window. Drive-through needs canopy "
   "and lane grading."),
  systems=("The dispensary needs stable temperature and humidity for drug storage - dedicated HVAC "
   "zone with monitoring. HIPAA-compliant counseling privacy; robust data and power for pharmacy "
   "systems with backup for refrigeration of vaccines."),
  spaces=[("Front End",40,30),("Checkout",12,8),("Dispensary",20,15),("Counseling Room",10,8),
   ("Drive-Through",25,12),("Stockroom",15,12),("Office",10,8),("Restroom",8,6)],
  materials=["Secure dispensary partitions","Transaction window","Pharmacy shelving",
   "Vaccine refrigeration","Counseling room acoustic treatment","Retail gondola shelving",
   "Drive-through canopy","Data infrastructure"],
  codes=["IBC mercantile occupancy","State pharmacy board rules","HIPAA privacy","ADA accessibility"],
  sheets=["A-101 Floor Plan","A-701 Security Details","E-101 Data Plan"]),
 dict(name="Furniture Showroom", group="General Retail", style="Furniture Showroom",
  history=("Furniture showrooms grew from cabinetmaker workshops into room-scene galleries: instead "
   "of rows of chairs, shoppers walk through fully staged living rooms and bedrooms. The modern "
   "version - pioneered by Scandinavian and American chains - needs huge clear floor plates and "
   "ceiling heights that flatter full room vignettes."),
  layout=("Vignette bays - each a staged room 12 to 16 feet square - line a looping path; "
   "clearance and mattress departments anchor the rear. A design center with fabric library sits "
   "near the middle; warehouse and pickup at the back with tall dock doors."),
  structure=("Long-span steel with 40-to-60-foot bays and 16-to-20-foot ceilings for two-story "
   "vignettes and tall displays. Floors take concentrated loads from pianos, stone tables, and "
   "stacked inventory."),
  systems=("Track and adjustable accent lighting per vignette - furniture is sold by how it looks "
   "under light. Zoned HVAC for the big volume; freight elevator or ramp to any mezzanine."),
  spaces=[("Vignette Floor",100,70),("Clearance",40,25),("Design Center",20,15),("Warehouse",60,40),
   ("Pickup",25,15),("Office",12,10),("Restrooms",12,8)],
  materials=["Long-span steel frame","Polished concrete or wood floors","Adjustable track lighting",
   "Movable vignette walls","High-bay warehouse racking","Loading dock levelers"],
  codes=["IBC mercantile occupancy","IBC egress Chapter 10","IECC lighting power","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","A-801 Vignette Details","E-101 Lighting Plan"]),
 dict(name="Mall Kiosk Court", group="Specialty Retail", style="Kiosk / Cart Court",
  history=("The mall kiosk - the RMU, or retail merchandising unit - was perfected in the 1980s and "
   "1990s as malls learned to monetize their corridors. A 10-by-10-foot cart with lockable storage "
   "needs only power and proximity to foot traffic, making it the lowest-cost entry into retail."),
  layout=("Kiosks sit in the common-area corridor on a grid that preserves required egress widths - "
   "typically 10 feet clear minimum each side. Each unit has selling faces on three or four sides, "
   "lockable base cabinets, and a small back bar. Seating courts and planters break the run."),
  structure=("Kiosks are furniture, not buildings: aluminum and laminate cases on lockable casters, "
   "anchored against tipping. The mall provides power floor boxes on a grid and the fire "
   "sprinkler coverage over the common area."),
  systems=("Each kiosk draws one or two 20-amp circuits from floor boxes; data via mall Wi-Fi or "
   "hardline. Kiosk lighting is self-contained LED; the mall's HVAC and sprinklers serve the court."),
  spaces=[("Kiosk A",10,10),("Kiosk B",10,10),("Kiosk C",10,10),("Kiosk D",10,10),
   ("Seating Court",20,15),("Corridor North",60,10),("Corridor South",60,10)],
  materials=["Aluminum kiosk framing","Lockable laminate cases","LED display lighting",
   "Floor power boxes","Mall common-area finishes","Egress signage"],
  codes=["IBC mall provisions 402","IFC kiosk regulations","ADA corridor widths","NEC 2023 commercial"],
  sheets=["A-101 Kiosk Layout","E-101 Power Plan"]),
 dict(name="Auto Parts Store", group="Specialty Retail", style="Auto Parts Retail",
  history=("Auto parts stores grew with the automobile itself - from dealership parts counters to "
   "the first dedicated chains in the 1930s. The modern store pairs retail shelving with a "
   "warehouse: thousands of SKUs in the back, a knowledgeable counter, and often a loaner-tool "
   "program and battery testing up front."),
  layout=("Retail floor with parts aisles and a long service counter; the warehouse - often half "
   "the building - holds bulk stock on pallet rack with a forklift aisle. Battery and fluids zone "
   "near the rear door with spill containment; machine shop (rotor turning) in larger stores."),
  structure=("Steel frame with 14-to-16-foot ceilings for rack; slab designed for rack post loads "
   "and forklift traffic. The battery room needs acid-resistant flooring and ventilation."),
  systems=("Warehouse lighting and ventilation; battery charging area with hydrogen ventilation per "
   "code; used-oil and fluid collection with secondary containment. Point-of-sale tied to "
   "catalog inventory systems."),
  spaces=[("Retail Floor",50,35),("Service Counter",20,8),("Warehouse",50,30),("Battery Room",12,10),
   ("Machine Shop",15,12),("Office",10,8),("Restroom",8,6),("Receiving",15,12)],
  materials=["Pallet racking","Forklift-rated slab","Acid-resistant battery flooring",
   "Parts shelving","Service counter millwork","Warehouse LED high-bays","Oil containment"],
  codes=["IBC mercantile + storage S-1","IFC battery storage","NFPA 13","NEC 2023 commercial"],
  sheets=["A-101 Floor Plan","S-101 Slab Plan","M-101 Ventilation Plan"]),
 dict(name="Garden Center", group="Specialty Retail", style="Garden Center / Nursery",
  history=("Garden centers grew from 19th-century nurseries into retail theater in the postwar "
   "suburban boom: greenhouses for growing, shade structures for display, and open yards for bulk "
   "goods. The building is half architecture, half horticulture - light, water, and drainage "
   "design the plan as much as walls do."),
  layout=("Greenhouse ranges for tropicals and starts; open-air shade houses for shrubs; bulk yard "
   "for soil, mulch, and stone with loader access; covered retail for tools, pots, and chemicals. "
   "Checkout sits where all paths converge, near the parking."),
  structure=("Greenhouses: aluminum or steel frames with polycarbonate or glass glazing, gutters "
   "collecting rainwater. Shade houses: simple post-and-cable with shade cloth. Retail building: "
   "conventional steel frame with big overhangs."),
  systems=("Irrigation is the utility: zones, misting, and drainage to a retention system. "
   "Greenhouse heating (unit heaters or radiant) and venting; chemical storage in a locked, "
   "ventilated room per fire code."),
  spaces=[("Greenhouse",60,30),("Shade House",50,30),("Retail Building",40,25),("Bulk Yard",60,40),
   ("Checkout",15,12),("Chemical Storage",10,8),("Office",10,8),("Restroom",8,6)],
  materials=["Aluminum greenhouse frame","Polycarbonate glazing","Shade cloth structures",
   "Irrigation zoning","Bulk bins and loaders","Pesticide storage cabinet","Gravel drainage beds"],
  codes=["IBC mercantile + greenhouse","IFC hazardous materials","EPA pesticide storage","ADA accessibility"],
  sheets=["A-101 Site Plan","A-101 Floor Plan","P-101 Irrigation Plan"]),
]
