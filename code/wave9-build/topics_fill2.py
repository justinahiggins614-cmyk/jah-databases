#!/usr/bin/env python3
"""Fill topics for short money items. Same spec as money files."""
F,C,A="foundations","compounded","advanced"
def T(title,tier,spec): return (title,tier,spec)
TOPICS = {}
def add(slug, lst): TOPICS[slug] = lst

add("db-collectors", [
T("Photographing for Insurance",C,"proof of value|photos + list|shoot|file|6h|intermediate|none|angle + detail shots"),
])
add("db-banknote-art", [
T("Serial Number Ladders",C,"fancy numbers|patterns premium|study|hunt|8h|intermediate|none|solids + ladders"),
])
add("db-toy-collectors", [
T("Plastic Color Variants",C,"chase variants|color + stamp|study|collect|10h|intermediate|none|variants multiply"),
T("Box Art Gallery",A,"art before plastic|displays|study|collect|16h|advanced|space|frame the art"),
])
add("db-vintage-gadget", [
T("Telegraph Key",C,"dots + dashes|restore + learn|key|restore|10h|intermediate|none|learn CW"),
T("Adding Machine",C,"crank math|oil + use|machine|restore|12h|intermediate|none|satisfying ka-chunk"),
T("Slide Rule",A,"logarithmic genius|learn + use|rule|study|16h|advanced|none|3 significant figures"),
])
add("db-art-collecting-explorer", [
T("Outsider Art",C,"raw vision|self-taught|study|collect|12h|intermediate|none|authenticity rules"),
T("Digital Art (NFTs?)",A,"pixels ownable|research + caution|study|analyze|16h|advanced|speculation|understand before buy"),
])
add("db-rock-and-mineral-collector", [
T("Zeolites",C,"delicate crystals|basalt quarries|study|collect|10h|intermediate|none|fragile beauties"),
T("Copper Minerals",C,"blue + green|oxidation zones|study|collect|10h|intermediate|mine safety|malachite + azurite"),
T("Pegmatite Hunting",A,"giant crystals|pegmatite dikes|study|hunt|30h|advanced|dig safety|tourmaline dreams"),
T("Systematic Collection",A,"science order|Dana classification|organize|catalog|30h|advanced|none|one of each family"),
])
add("db-fossil-collector", [
T("Echinoids",C,"sea urchins|symmetry|study|collect|8h|intermediate|none|5-part symmetry"),
T("Graptolites",C,"saw blades|shale bedding|study|find|10h|intermediate|none|index fossils"),
T("Dinosaur Trackways",A,"walk with giants|sites + casts|visit|study|20h|advanced|permits|Paluxy river"),
T("Preparation Lab Setup",A,"pro prep|tools + dust|build|prep|30h|advanced|dust|air abrasive pro"),
])
add("db-meteorite-discovery", [
T("Achondrites",C,"melted asteroids|basaltic|study|research|12h|intermediate|none|Vesta visitors"),
T("Impact Glass",C,"earth melted|tektites|study|collect|10h|intermediate|none|moldavite green"),
T("Shocking History",A,"craters story|structures|study|visit|20h|advanced|none|Meteor Crater AZ"),
])
add("db-world-s-most-expensive-objects", [
T("Most Expensive Sneakers",C,"$2.2M Nike|Moon Shoe|study|read|4h|intermediate|none|1972 waffle"),
T("Most Expensive Comic",C,"$3.2M Action #1|Superman debut|study|read|4h|intermediate|none|9.0 grade"),
T("Most Expensive Dress",A,"$12M Marilyn|subway grate|study|read|6h|advanced|none|auction legend"),
])
add("db-luxury-design", [
T("The Trunk (Vuitton)",C,"travel icon|craft + history|study|admire|8h|intermediate|none|flat-top innovation"),
T("Porcelain (Meissen)",C,"white gold|crossed swords|study|collect|12h|intermediate|none|1710 first"),
T("The Private Library",A,"book sanctuary|design + curation|study|build|40h|advanced|none|leather + ladder"),
])
add("db-bargain-hunter", [
T("Price Mistakes",C,"glitch deals|alerts + speed|hunt|buy|8h|intermediate|honor|act fast, polite"),
T("Open-Box Deals",C,"new-ish less|inspect + warranty|hunt|buy|6h|intermediate|none|ask about returns"),
T("Demo Units",C,"tried, true|floor + demo|hunt|buy|6h|intermediate|none|20-30% off"),
T("Coupon Apps",F,"phone savings|stack apps|install|save|4h|beginner|none|one trip, many apps"),
T("Buy Nothing Groups",F,"free first|local groups|join|take|4h|beginner|none|give before take"),
])
add("db-business-idea-treasure-chest", [
T("Vending Routes",C,"passive-ish|locations + machines|research|launch|40h|intermediate|theft|cash businesses"),
T("Laundromat (Study)",C,"cashflow classic|math + location|study|analyze|20h|intermediate|none|water bills!"),
T("Storage Units",A,"rent boxes|develop + manage|study|analyze|40h|advanced|debt|occupancy math"),
T("Car Wash (Express)",A,"subscriptions|site + systems|study|analyze|40h|advanced|none|membership model"),
])
add("db-side-project-idea", [
T("Notion Templates",C,"sell systems|pack + sell|create|sell|30h|intermediate|none|SEO + twitter"),
T("Icon Pack",C,"pixels pay|design + sell|create|sell|40h|intermediate|none|dribbble launch"),
T("Wedding Films",A,"love stories|shoot + edit|film|deliver|80h|advanced|contracts|book 6mo out"),
T("SaaS (Indie Hacker)",A,"tiny team, real MRR|build + launch|build|grow|200h|advanced|none|7-day streaks"),
])
add("db-product-opportunity-finder", [
T("API Opportunities",C,"build on platforms|gaps + docs|study|list|12h|intermediate|platform risk|app store gaps"),
T("Aging Tech Replacement",C,"old systems die|migrate + modernize|study|list|12h|intermediate|none|boring = profitable"),
T("Niche SaaS Mining",C,"tiny markets|100 users x $100|study|list|12h|intermediate|none|vertical depth"),
T("Service Arbitrage",A,"buy low sell high|offshore + local|study|list|20h|advanced|quality|manage quality"),
T("Roll-Up Data",A,"fragmented markets|acquire + systemize|study|list|30h|advanced|debt|boring industries"),
])
add("db-everyday-problem-solver", [
T("Smelly Shoes",C,"odor out|baking soda + sun|fix|fresh|2h|intermediate|none|tea bags overnight"),
T("Foggy Mirror",C,"see after shower|shaving cream trick|fix|clear|1h|intermediate|none|buff off"),
T("Static Cling",C,"cling off|safety pin trick|fix|smooth|1h|intermediate|none|pin in hem"),
])
add("db-future-market-idea", [
T("Pet Humanization",C,"pets = family|premium + tech|study|list|10h|intermediate|none|$300B market"),
T("Sleep Economy",C,"rest = wealth|track + optimize|study|list|10h|intermediate|none|third of life"),
T("Death Tech",A,"end well|planning + legacy|study|list|16h|advanced|sensitivity|green burial"),
T("Attention Reclaim",A,"focus scarce|tools + spaces|study|list|16h|advanced|none|dumb phones rise"),
])
add("db-million-dollar-idea-reality-check", [
T("The Coffee Shop Dream",C,"caffeine dream|location math|reality-check|decide|12h|intermediate|none|200 cups/day breakeven"),
T("The Food Truck",C,"wheels + food|permits + commissary|reality-check|decide|12h|intermediate|none|14hr days"),
T("The Bar",A,"nightlife dream|liquor license|reality-check|decide|16h|advanced|legal|licenses $$$"),
T("The Gym Dream",A,"fitness passion|retention math|reality-check|decide|16h|advanced|none|January lie"),
])
print("fill2:", {k: len(v) for k,v in TOPICS.items()})
