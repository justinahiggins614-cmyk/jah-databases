#!/usr/bin/env python3
"""Fill topics for short gadget items. Same spec as gadget files."""
F,C,A="foundations","compounded","advanced"
def T(title,tier,spec): return (title,tier,spec)
TOPICS = {}
def add(slug, lst): TOPICS[slug] = lst

add("db-everyday-object-reinvention", [
T("The Step Stool",A,"reach safely|fold + grip + light|stool|build|10h|advanced|ladder safety|reinvention: the forgotten essential"),
])
add("db-product-that-doesn-t-exist-yet", [
T("The Honest Label Printer",A,"label everything|phone + thermal|printer|build|16h|advanced|none|concept: organization as product"),
])
add("db-pocket-sized-wonder", [
T("Pocket Anemometer",A,"wind where?|tiny fan + readout|meter|build|12h|advanced|none|wonder: drone pilots love"),
])
add("db-giant-gadget", [
T("Giant Abacus (Outdoor)",A,"math playground|2m frame + balls|abacus|build|30h|advanced|secure|wonder: climbable arithmetic"),
])
add("db-transforming-object", [
T("Transformer Table (Dining)",A,"daily vs feast|expanding mechanism|table|build|40h|advanced|pinch|transform: 4 to 12 seats"),
])
add("gen-travel-gadget-studio", [
T("Travel Hammock (Ultralight)",A,"rest anywhere|8oz + straps|hammock|sew|8h|advanced|tree safety|design: straps protect bark"),
])
add("db-desk-gadget", [
T("Desk Treadmill (Under)",A,"walk while working|slim treadmill|treadmill|study|4h|advanced|none|gadget: 2mph max typing"),
])
add("db-smart-everyday-tool", [
T("Smart Pill Organizer",A,"never miss|7-day + alerts|organizer|build|16h|advanced|none|tool: caregiver alerts"),
])
add("db-modular-product", [
T("Modular Tiny House",A,"home grows|modules add rooms|house|study|100h|advanced|pro|modular: start 200sqft"),
])
add("db-custom-controller", [
T("Orchestral Controller",A,"conduct music|baton + sensors|baton|build|40h|advanced|low-voltage|controller: gesture = dynamics"),
])
add("db-innovative-mouse", [
T("The Foot Pedal Mouse",A,"hands-free click|pedals + head tracking|pedals|build|40h|advanced|none|innovation: feet click, head moves"),
])
add("db-personal-utility-belt", [
T("Photographer's Belt",A,"gear at hand|lens + body pouches|belt|build|16h|advanced|none|carry: weight on hips"),
])
add("db-modular-backpack", [
T("Convertible (Backpack+Duffel)",C,"carry vs haul|straps hide|pack|sew|18h|intermediate|none|pack: back panel hides"),
T("Rolling Backpack",A,"wheel or wear|wheels + handle|pack|build|24h|advanced|none|pack: travel hybrid"),
])
add("gen-pocket-workshop", [
T("Pocket Caliper",A,"measure precise|6in digital|caliper|study|2h|advanced|none|workshop: 0.01mm anywhere"),
])
add("db-portable-lab", [
T("Soil Respiration Kit",C,"soil alive?|CO2 trap|kit|build|10h|intermediate|none|lab: biology breathing"),
T("Plankton Net",A,"tiny sea life|fine mesh tow|net|build|12h|advanced|water safety|lab: tow slowly"),
])
add("gen-mobile-creator-studio", [
T("360 Camera Kit",C,"all directions|camera + stitch|kit|study|8h|intermediate|none|studio: hide the tripod"),
T("Field Monitor",A,"see clearly|7in + hood|monitor|build|12h|advanced|none|studio: 1000 nits daylight"),
])
add("gen-diy-instrument-maker", [
T("Bowed Psaltery",A,"bowed melody|triangle + strings|psaltery|build|40h|advanced|string|instrument: bow the edge"),
])
add("db-desk-pet-invention", [
T("Kinetic Desk Toy (Gears)",C,"watch work|gear + crank|toy|build|12h|intermediate|pinch|pet: crank calm"),
T("Desk Fountain (Tiny)",A,"water calm|pump + stones|fountain|build|10h|advanced|water+electric|pet: white noise"),
])
add("db-ambient-display", [
T("Laundry Room Glow",C,"dryer done?|vibration + light|sensor|build|10h|intermediate|low-voltage|display: fold reminder"),
T("Fridge Door Ajar",C,"door open?|sensor + chime|sensor|build|8h|intermediate|none|display: gentle nag"),
])
add("db-home-energy-display", [
T("Solar Monitor",C,"make + use|solar + app|monitor|install|8h|intermediate|electrical pro|energy: self-consume first"),
T("EV Charging Timer",C,"cheap miles|off-peak schedule|timer|set|2h|intermediate|electrical|energy: midnight electrons"),
])
add("db-personal-safety-gadget", [
T("Bike Radar",C,"cars behind|radar + display|radar|install|4h|intermediate|none|safety: see threats early"),
])
add("db-kid-friendly-learning-gadget", [
T("Math Card Game",C,"facts fun|deck + rules|game|make|4h|intermediate|none|learn: 10 min daily"),
T("Geography Puzzle",C,"world pieces|floor map|puzzle|study|4h|intermediate|none|learn: continents first"),
])
add("db-pet-tech-invention", [
T("Cat Wheel",A,"indoor zoomies|exercise wheel|wheel|build|20h|advanced|none|pet: train with treats"),
])
add("db-garden-gadget", [
T("Greenhouse Controller",C,"auto climate|temp + vent + water|controller|build|16h|intermediate|low-voltage|garden: 75F day target"),
T("Compost Aerator",C,"turn easy|corkscrew tool|tool|study|1h|intermediate|none|garden: weekly turn"),
])
add("db-kitchen-innovation", [
T("Sourdough Station",C,"bread ritual|starter + tools|station|bake|10h|intermediate|food safety|kitchen: feed the starter"),
T("Sprouting Kit",C,"fresh greens|jars + seeds|kit|grow|4h|intermediate|food safety|kitchen: rinse twice daily"),
])
add("db-reusable-product", [
T("Safety Razor (Women's)",C,"smooth + waste-free|long handle|razor|learn|2h|intermediate|blade|reuse: no pressure"),
T("Period Underwear",C,"backup + planet|absorbent|underwear|use|2h|intermediate|hygiene|reuse: rinse cold"),
])
add("db-repairability-design", [
T("Toaster Repair",C,"heat again|element + clean|toaster|repair|3h|intermediate|electrical|repair: unplug, obviously"),
])
print("fill1:", {k: len(v) for k,v in TOPICS.items()})
