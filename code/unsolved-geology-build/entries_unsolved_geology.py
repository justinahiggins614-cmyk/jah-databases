#!/usr/bin/env python3
"""34 unsolved geology problems (Unsolved Problems Solved series, batch 1;
Manon 2026-10-17 16:15 EDT).

Field scope: unsolved geological problems - the onset of plate tectonics,
the exact core composition, supercontinent cycle mechanics, mass-extinction
triggers beyond impacts, the deep water cycle, plus the geology canon
(stratigraphy, petrology, mineralogy, paleontology, orogeny, geomorphology).

Each entry: problem (real, fact-checked), background (3-8 sentences),
why_it_matters (2-4 sentences), sig_pointer (short public-half pointer),
sig_lens (Signature framing line for the signature half), signature_solution
(full proposed approach WITHOUT the honesty label - build.py prepends it),
citations, and an explorer spec driving the solution-explorer demo.

Ladder order: rank 1 = most approachable, rank 34 = most compounded.
Tiers: foundations (1-9), compounded (10-19), advanced (20-34).

Distinctness: titles and angles are geology-lens framings, checked against
all 34 Unsolved Earth Science titles (JAH-USES-*) - no near-duplicates.
"""

ENTRIES = [
# ---------------------------------------------------------------- 1
{
 "key": "ocean-floor-age",
 "name": "Why Is No Ocean Floor Older Than 200 Million Years?",
 "group": "Tectonics",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": ("Continental rocks reach back 4.03 billion years, yet no piece of ocean "
             "floor anywhere on Earth is older than about 200 million years. The entire "
             "seafloor is recycled on a geologically short clock, while the continents "
             "keep their oldest records."),
 "background": ("The oldest known oceanic crust sits in the western Pacific and the "
             "western Atlantic and dates to the Jurassic, roughly 180 to 200 million "
             "years ago. In the 1960s the Vine-Matthews-Morley hypothesis explained the "
             "striped magnetic pattern of the seafloor as a tape recording of geomagnetic "
             "reversals, giving geologists a clock for ocean crust. That clock showed "
             "spreading centers constantly manufacture new crust while subduction zones "
             "swallow the old - a conveyor belt with no memory older than about 200 "
             "million years. By contrast the Acasta Gneiss in Canada is 4.03 billion "
             "years old, and detrital zircons from Jack Hills, Australia, are 4.4 "
             "billion years old, so the continents preserve twenty times more history. "
             "The sharp contrast raises a live question: has subduction always run at "
             "roughly this recycling rate, or was early Earths conveyor slower, faster, "
             "or intermittent?"),
 "why_it_matters": ("The recycling rate of the seafloor sets how fast heat escapes "
             "Earths interior, how sea level has risen and fallen, and how quickly "
             "carbon and water cycle between surface and mantle. If the conveyor ran "
             "differently in the Archean, every model of early climate and early life "
             "shifts with it. It is also the cleanest everyday proof that plate "
             "tectonics is real - and the cleanest measure of its tempo."),
 "sig_pointer": ("The Signature system proposes a deep-time recycling census: compile "
             "every dated ophiolite and craton margin, and test whether the 200-million-"
             "year limit is a steady-state law or a recent accident. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the 200-million-year ceiling "
             "as a measurement of a planetary conveyor belt - and asks whether the belt "
             "ever ran at a different speed, using the oldest surviving fragments as "
             "the speedometer."),
 "signature_solution": (
     "Proposed approach. Step 1: build an open census of the oldest oceanic crust "
     "fragments on every continent - ophiolites, high-pressure belts, and accreted "
     "terranes - with uniform radiometric dating and uncertainty bars, published as "
     "one versioned dataset. Step 2: reconstruct the age distribution of destroyed "
     "ocean crust from the fragments that survived obduction, correcting for the "
     "preservation bias that favors young, buoyant crust. Step 3: model the recycling "
     "rate backward in time under three regimes - steady conveyor, episodic "
     "overturn, and sluggish early lid - and score each against the fragment census "
     "and heat-flow history. Step 4: test the winning regime against independent "
     "proxies: the strontium isotope curve of seawater, the timing of the first "
     "blueschists, and the secular cooling curve of the mantle.\n"
     "Assumptions: that ophiolite ages sample the destroyed ocean record fairly "
     "enough to constrain the rate (biased but correctable); that magnetic and "
     "radiometric clocks agree on spreading history (well tested for the last 200 "
     "million years, extrapolated beyond); that mantle cooling models are not "
     "missing a major heat source.\n"
     "What would confirm it: a fragment census whose oldest ages cluster at a "
     "boundary that moves systematically with the modeled regime, plus agreement "
     "from at least two independent proxies.\n"
     "What would kill it: oldest fragments showing no regime structure at all, or "
     "independent proxies contradicting the census (for example strontium isotopes "
     "demanding a fast conveyor while fragments demand a slow one).\n"
     "What this does NOT claim: it does not claim subduction started at any "
     "particular date; it does not claim the modern rate applied in the Archean; "
     "it is not established science and is not peer-accepted."),
 "citations": [
     "Vine F J, Matthews D H. Magnetic anomalies over oceanic ridges. Nature; 1963.",
     "Muller R D et al. Ocean basin evolution and global-scale plate reorganization events. Annu Rev Earth Planet Sci; 2016.",
     "Bowring S A, Williams I S. Priscoan (4.00-4.03 Ga) orthogneisses from northwestern Canada. Contrib Mineral Petrol; 1999."],
 "explorer": {
   "blurb": ("A conveyor-belt calculator: it turns the 200-million-year ceiling into "
             "a recycling rate, compares it with continental preservation, and shows "
             "how many times the ocean floor has been rebuilt since Earth formed."),
   "assumptions": {"max_ocean_age_Ma": 200.0, "max_continental_age_Ma": 4030.0,
                   "earth_age_Ma": 4540.0, "subduction_rate_cm_yr": 5.0},
   "model_src": (
     "def run(A):\n"
     "    oc = A[\"max_ocean_age_Ma\"]\n"
     "    cc = A[\"max_continental_age_Ma\"]\n"
     "    ea = A[\"earth_age_Ma\"]\n"
     "    ocean_age_fraction = oc / ea\n"
     "    continental_age_fraction = cc / ea\n"
     "    recycling_turnovers = ea / oc\n"
     "    recycling_cm = A[\"subduction_rate_cm_yr\"] * oc * 1e6 / 1e5\n"
     "    return {\"ocean_age_fraction\": ocean_age_fraction,\n"
     "            \"continental_age_fraction\": continental_age_fraction,\n"
     "            \"recycling_turnovers\": recycling_turnovers,\n"
     "            \"crust_recycled_km\": recycling_cm}\n"),
   "steps": [("Fraction of Earth history the oldest ocean floor records", "ocean_age_fraction", ""),
             ("Fraction preserved by the oldest continents", "continental_age_fraction", ""),
             ("Times the seafloor has been fully rebuilt", "recycling_turnovers", "turnovers"),
             ("Crust consumed at 5 cm/yr over 200 Myr", "crust_recycled_km", "km")],
   "confirm": ["The global ophiolite census shows a systematic oldest-age structure matching one recycling regime.",
               "At least two independent proxies (strontium isotopes, heat flow) agree on the regime."],
   "refute": ["Oldest surviving fragments show no regime structure - the ceiling looks like pure preservation bias.",
              "Independent proxies demand mutually incompatible recycling rates."],
   "checks": [("ocean_age_fraction", 0.01, 0.1),
              ("continental_age_fraction", 0.8, 1.0),
              ("recycling_turnovers", 15.0, 30.0),
              ("crust_recycled_km", 5000.0, 20000.0)],
   "honesty": ("We do not know whether the conveyor always ran at the modern rate; "
               "this explorer only converts the observed ceiling into a rate so the "
               "question can be tested against the rock record.")}
},
# ---------------------------------------------------------------- 2
{
 "key": "grand-canyon",
 "name": "What Carved the Grand Canyon, and How Fast?",
 "group": "Geomorphology",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": ("The Grand Canyon is a mile deep, yet geologists still argue about when "
             "the Colorado River cut it: the classic view says about 6 million years "
             "ago, while thermochronology hints parts of the canyon are 70 million "
             "years old. Both cannot be the whole story."),
 "background": ("John Wesley Powell first descended the canyon in 1869 and treated it "
             "as the Colorado Rivers handiwork, and for a century the 6-million-year "
             "age stood nearly unchallenged. Then uranium-thorium-helium dating of "
             "apatite - a thermometer that records when rock cooled as overlying rock "
             "eroded away - suggested the western canyon began incising in the "
             "Cretaceous, around 70 million years ago. Competing studies using the "
             "same methods on nearby samples returned young ages, and the field split "
             "into the young-canyon and old-canyon camps. The modern synthesis leans "
             "toward a hybrid: an ancient western canyon later integrated with a young "
             "eastern canyon when the Colorado River captured the whole drainage "
             "about 5 to 6 million years ago. But the exact paleo-drainage map, and "
             "which segment is how old, remain contested."),
 "why_it_matters": ("The canyon is the type example of how rivers cut rock, and its "
             "age calibrates every model of landscape evolution, uplift of the "
             "Colorado Plateau, and the integration of continental drainages. Getting "
             "it right decides whether a mile of rock can vanish in 6 million years "
             "or needs ten times longer - a basic fact about how fast geology works."),
 "sig_pointer": ("The Signature system proposes a canyon-segment dating matrix: "
             "thermochronology transects on both rims of every segment, fused with "
             "paleo-drainage modeling, to date each reach independently. See the "
             "Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the canyon not as one age "
             "but as several canyons stitched together - and proposes dating each "
             "stitch on its own evidence."),
 "signature_solution": (
     "Proposed approach. Step 1: sample apatite thermochronology transects down both "
     "walls of each major canyon reach - western, central, eastern - with identical "
     "lab protocols so ages are directly comparable. Step 2: date the river "
     "gravels stranded on the rims (the Shivwits, the Hualapai) with cosmogenic "
     "nuclides to pin when each reach was abandoned by the river. Step 3: run "
     "paleo-drainage models that must reproduce both datasets at once: thermochron "
     "cooling histories and stranded gravel ages, with the drainage capture point "
     "as a free parameter. Step 4: blind-test the model - hide one reachs data, "
     "predict it, then reveal.\n"
     "Assumptions: that helium diffusion kinetics in apatite are understood well "
     "enough to convert cooling to erosion (the crux of the whole debate); that "
     "rim gravels are truly river deposits and not reworked; that no undocumented "
     "faulting shuffled the samples.\n"
     "What would confirm it: every reach yielding a self-consistent age that the "
     "drainage model predicts blind, with the capture point converging near 5 to "
     "6 million years.\n"
     "What would kill it: irreconcilable age scatter within single reaches, or a "
     "model that fits the west only by breaking the east.\n"
     "What this does NOT claim: it does not claim either camp was wrong about "
     "their own samples; it does not set the canyons age by authority; it is not "
     "established science."),
 "citations": [
     "Flowers R M, Farley K A. Apatite 4He/3He and (U-Th)/He evidence for an ancient Grand Canyon. Science; 2012.",
     "Karlstrom K E et al. Formation of the Grand Canyon 5 to 6 million years ago through integration of older palaeocanyons. Nature Geosci; 2014.",
     "Powell J W. Exploration of the Colorado River of the West. Smithsonian; 1875."],
 "explorer": {
   "blurb": ("An incision-rate calculator: given canyon depth and rival ages, it "
             "computes the implied erosion rate for each camp and shows which rate "
             "matches measured river incision elsewhere."),
   "assumptions": {"canyon_depth_m": 1600.0, "young_age_Ma": 6.0, "old_age_Ma": 70.0,
                   "river_sediment_load_Mt_yr": 65.0},
   "model_src": (
     "def run(A):\n"
     "    d = A[\"canyon_depth_m\"]\n"
     "    young_rate = d / (A[\"young_age_Ma\"] * 1e6) * 1000.0\n"
     "    old_rate = d / (A[\"old_age_Ma\"] * 1e6) * 1000.0\n"
     "    rate_ratio = young_rate / old_rate\n"
     "    return {\"young_rate_mm_yr\": young_rate, \"old_rate_mm_yr\": old_rate,\n"
     "            \"rate_ratio\": rate_ratio,\n"
     "            \"sediment_Mt\": A[\"river_sediment_load_Mt_yr\"]}\n"),
   "steps": [("Implied rate if the canyon is 6 Myr old", "young_rate_mm_yr", "mm/yr"),
             ("Implied rate if the canyon is 70 Myr old", "old_rate_mm_yr", "mm/yr"),
             ("How many times faster the young model must cut", "rate_ratio", "x"),
             ("Modern river sediment load", "sediment_Mt", "Mt/yr")],
   "confirm": ["All reaches return internally consistent ages that the drainage model predicts blind.",
               "The capture point converges near 5 to 6 million years across independent methods."],
   "refute": ["Irreconcilable age scatter within single reaches, or the model fitting one reach only by breaking another."],
   "checks": [("young_rate_mm_yr", 0.1, 1.0),
              ("old_rate_mm_yr", 0.01, 0.1),
              ("rate_ratio", 5.0, 20.0)],
   "honesty": ("We do not know the canyons true age; this explorer only converts "
               "the rival ages into erosion rates so they can be compared with what "
               "rivers are observed to do.")}
},
# ---------------------------------------------------------------- 3
{
 "key": "gold-origin",
 "name": "Where Does Earths Gold Really Come From?",
 "group": "Mineral Resources",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": ("Nearly all the gold humanity has ever mined sits in a handful of deposit "
             "types, yet geologists still argue about where the metal came from: "
             "leached out of ordinary crust by hot water, or tapped from deep "
             "mantle-derived fluids rising along ancient faults."),
 "background": ("Orogenic gold deposits - the mother-lode veins of California, the "
             "camps of Western Australia, the great reefs of the Canadian Shield - "
             "formed 2.7 to 2.0 billion years ago during mountain building, when "
             "gold-bearing fluids moved through crustal-scale fault zones. One school "
             "holds the gold was leached from the surrounding greenstone rocks by "
             "metamorphic fluids; another traces distinctive fluid chemistry to a "
             "sub-crustal, possibly mantle, source. The Witwatersrand Basin of South "
             "Africa, source of roughly a third of all gold ever mined, adds a second "
             "fight: ancient river placer versus hydrothermal upgrading of a placer. "
             "Isotope geochemistry keeps narrowing the options but has not closed "
             "the case, because gold is so rare - parts per billion in average crust "
             "- that tiny fluid volumes and tiny source differences decide "
             "everything."),
 "why_it_matters": ("Gold exploration is a multi-billion-dollar industry that drills "
             "on conceptual models: if the source is deep and structural, explorers "
             "chase ancient fault plumbing; if it is local and metamorphic, they "
             "chase rock chemistry. The answer also decides how Earths rarest metals "
             "concentrated at all - a basic question about how planets differentiate."),
 "sig_pointer": ("The Signature system proposes a gold-source fingerprint atlas: "
             "uniform isotopic and fluid-inclusion measurements across all major "
             "orogenic camps to test crustal versus deep sources head to head. See "
             "the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats gold deposits as crime "
             "scenes - and proposes dusting every one of them for the same "
             "fingerprints so the sources can be compared on equal evidence."),
 "signature_solution": (
     "Proposed approach. Step 1: assemble a global orogenic-gold sample set - "
     "fifty major camps, ore plus host rock plus fluid inclusions - analyzed in "
     "one laboratory campaign with identical protocols for gold, sulfur, lead, "
     "and osmium isotopes. Step 2: measure fluid-inclusion gas chemistry "
     "(CO2, CH4, N2 ratios) as an independent deep-versus-shallow discriminant. "
     "Step 3: run blind classification - can an algorithm trained on half the "
     "camps predict the source assignment of the other half from chemistry alone? "
     "Step 4: map the winners and losers onto crustal architecture: do deep-source "
     "camps sit on lithosphere-scale faults and shallow-source camps on local "
     "metamorphic gradients?\n"
     "Assumptions: that isotopic fingerprints survive 2-billion-year alteration "
     "well enough to read (partly true, partly hopeful); that the sampled camps "
     "represent the global population; that metamorphic and mantle fluids have "
     "non-overlapping signatures in at least one measured system.\n"
     "What would confirm it: blind classification succeeding above 90 percent, "
     "with the same source assignment from isotopes and gas chemistry "
     "independently.\n"
     "What would kill it: fingerprints scattering with no camp-level structure, "
     "or isotope and gas systems assigning the same camp to opposite sources.\n"
     "What this does NOT claim: it does not claim gold is mantle-derived today; "
     "it does not locate any new deposit; it is not established science."),
 "citations": [
     "Goldfarb R J, Groves D I. Orogenic gold: common or evolving fluid and metal sources. Ore Geol Rev; 2015.",
     "Frimmel H E. Earths continental crustal gold endowment. Earth Planet Sci Lett; 2008.",
     "Groves D I et al. Orogenic gold deposits: a proposed classification. Econ Geol; 1998."],
 "explorer": {
   "blurb": ("An enrichment calculator: from average crustal gold abundance it "
             "computes how many times over gold must be concentrated to make an "
             "orebody, and how much rock a fluid must leach to do it."),
   "assumptions": {"crust_ppb": 4.0, "ore_grade_ppm": 5.0, "deposit_tonnes": 500.0,
                   "leach_efficiency": 0.1},
   "model_src": (
     "def run(A):\n"
     "    enrichment = (A[\"ore_grade_ppm\"] * 1000.0) / A[\"crust_ppb\"]\n"
     "    gold_kg = A[\"deposit_tonnes\"] * 1000.0 * A[\"ore_grade_ppm\"] / 1e6\n"
     "    rock_needed_Mt = (gold_kg / 1000.0) / (A[\"crust_ppb\"] / 1e9) / A[\"leach_efficiency\"] / 1e6\n"
     "    return {\"enrichment_factor\": enrichment, \"gold_in_deposit_kg\": gold_kg,\n"
     "            \"rock_leached_Mt\": rock_needed_Mt}\n"),
   "steps": [("Concentration factor, crust to ore", "enrichment_factor", "x"),
             ("Gold contained in 500 tonnes of ore", "gold_in_deposit_kg", "kg"),
             ("Rock that must be leached at 10 percent efficiency", "rock_leached_Mt", "Mt")],
   "confirm": ["Blind classification of camps by source succeeds above 90 percent across two independent chemical systems.",
               "Source assignments map cleanly onto crustal architecture."],
   "refute": ["Fingerprints scatter with no camp-level structure, or isotope and gas systems contradict each other."],
   "checks": [("enrichment_factor", 500.0, 5000.0),
              ("gold_in_deposit_kg", 1.0, 10.0),
              ("rock_leached_Mt", 1.0, 100.0)],
   "honesty": ("We do not know golds ultimate source; this explorer only quantifies "
               "how extreme the concentration process must be, which is the fact "
               "any source theory has to explain.")}
},
# ---------------------------------------------------------------- 4
{
 "key": "granite-unique",
 "name": "Why Is Granite Nearly Unique to Earth?",
 "group": "Petrology",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": ("Granite - the pale speckled rock of continents - is almost unknown "
             "elsewhere in the solar system. The Moon, Mars, and Venus are built of "
             "basalt, while Earth alone grew continents of granite. Why the "
             "difference is still debated."),
 "background": ("Granite forms when basaltic magma differentiates: dense minerals "
             "crystallize and sink, leaving a silica-rich, water-bearing residue that "
             "rises to form continental crust. Water is the key ingredient - it "
             "lowers melting points and drives the chemical separation. The Moon has "
             "no water and no granite continents; Mars shows only rare, small "
             "granitic patches. In the Archean, Earth made a different felsic rock - "
             "tonalite-trondhjemite-granodiorite, or TTG - by melting hydrated basalt "
             "at depth, and true granite only became common after about 2.5 billion "
             "years ago. The open question is which came first: did plate tectonics "
             "make granite possible by recycling water, or did an early water-rich "
             "crust make plate tectonics possible? The rocks record the transition "
             "but not its cause."),
 "why_it_matters": ("Granite is the physical foundation of continents, and continents "
             "are the foundation of stable land, soils, and much of the biosphere. "
             "Understanding why only Earth made granite is understanding why only "
             "Earth has continents - and therefore one of the boundary conditions "
             "for a habitable planet."),
 "sig_pointer": ("The Signature system proposes a granite-transition survey: date "
             "the TTG-to-granite switch on every craton and test whether it tracks "
             "water, tectonics, or mantle cooling. See the Signature Edition record "
             "for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats granites uniqueness as a "
             "planetary experiment with one positive result - and proposes reading "
             "the transition in the rocks to find which variable flipped."),
 "signature_solution": (
     "Proposed approach. Step 1: compile every dated TTG and granite suite on all "
     "major cratons into one database with uniform age, chemistry, and oxygen-"
     "isotope data (oxygen isotopes track water involvement). Step 2: for each "
     "craton, date the local TTG-to-true-granite transition and the first local "
     "evidence of subduction (blueschists, ophiolites, paired metamorphic belts). "
     "Step 3: test the ordering - does granite follow subduction everywhere, "
     "precede it anywhere, or track mantle cooling curves instead? Step 4: compare "
     "with the Moon and Mars as negative controls: same differentiation physics, "
     "no water, no granite continents.\n"
     "Assumptions: that oxygen isotopes faithfully record water in ancient magmas "
     "(broadly true, with caveats); that craton records are complete enough to "
     "order events (survivor bias is real); that TTG chemistry really requires a "
     "different melting regime than granite.\n"
     "What would confirm it: the transition tracking one variable - water "
     "proxies, subduction evidence, or cooling - consistently across cratons, "
     "with the negative controls behaving as predicted.\n"
     "What would kill it: transitions scattered with no correlation to any "
     "variable, or a craton where true granite long predates any subduction "
     "evidence.\n"
     "What this does NOT claim: it does not claim plate tectonics caused "
     "granite; it does not claim water alone is sufficient; it is not established "
     "science."),
 "citations": [
     "Moyen J F, Martin H. Forty years of TTG research. Lithos; 2012.",
     "Hawkesworth C J et al. The generation and evolution of the continental crust. J Geol Soc; 2010.",
     "Condie K C. Earth as an Evolving Planetary System. 3rd ed. Academic Press; 2015."],
 "explorer": {
   "blurb": ("A differentiation calculator: it shows how much basalt must "
             "crystallize to leave a granite residue, and how water changes the "
             "melting budget."),
   "assumptions": {"basalt_sio2_pct": 50.0, "granite_sio2_pct": 70.0,
                   "residue_sio2_pct": 45.0, "water_wt_pct": 2.0},
   "model_src": (
     "def run(A):\n"
     "    granite_fraction = (A[\"basalt_sio2_pct\"] - A[\"residue_sio2_pct\"]) / (A[\"granite_sio2_pct\"] - A[\"residue_sio2_pct\"])\n"
     "    f = 1.0 - granite_fraction\n"
     "    melt_depression_C = A[\"water_wt_pct\"] * 40.0\n"
     "    return {\"crystallized_fraction\": f, \"granite_yield_fraction\": granite_fraction,\n"
     "            \"water_melting_depression_C\": melt_depression_C}\n"),
   "steps": [("Fraction of magma that must crystallize out", "crystallized_fraction", ""),
             ("Granite yielded per unit of basalt magma", "granite_yield_fraction", ""),
             ("Melting-point depression from 2 wt percent water", "water_melting_depression_C", "C")],
   "confirm": ["The TTG-to-granite transition tracks one variable consistently across all cratons.",
               "The Moon and Mars negative controls behave as the water hypothesis predicts."],
   "refute": ["Transitions scatter with no correlation, or true granite predates subduction evidence on some craton."],
   "checks": [("crystallized_fraction", 0.5, 0.99),
              ("granite_yield_fraction", 0.01, 0.5),
              ("water_melting_depression_C", 40.0, 200.0)],
   "honesty": ("We do not know which variable flipped first; this explorer only "
               "quantifies how much differentiation granite demands, which any "
               "origin theory must supply.")}
},
# ---------------------------------------------------------------- 5
{
 "key": "deep-diamonds",
 "name": "How Deep Do the Deepest Diamonds Come From?",
 "group": "Mineralogy",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": ("Most diamonds crystallize 150 to 200 kilometers down, but a rare class "
             "of super-deep diamonds carries inclusions of minerals stable only near "
             "700 kilometers - proof that some diamonds, and the carbon in them, "
             "cycle through the deep mantle. How deep the cycle goes is unknown."),
 "background": ("Diamonds are time capsules: the tiny mineral grains trapped inside "
             "them record the pressure and chemistry of their birthplace. Ordinary "
             "gem diamonds carry peridotite and eclogite inclusions from the cool "
             "lithospheric keel, 150 to 200 kilometers deep. Super-deep diamonds, "
             "found at localities like Juina in Brazil, instead trap former "
             "bridgmanite, calcium silicate perovskite, and ringwoodite - minerals "
             "that only exist in the transition zone and lower mantle, down to about "
             "700 kilometers. Their carbon isotopes are unusually light, hinting the "
             "carbon was once at Earths surface - subducted oceanic crust carrying "
             "carbonates down, then returning as diamond. Whether this deep carbon "
             "conveyor is a rare curiosity or a major planetary cycle is the open "
             "question."),
 "why_it_matters": ("If surface carbon routinely reaches the lower mantle and "
             "returns, the deep carbon cycle is far more vigorous than textbooks "
             "say, with consequences for mantle chemistry, diamond exploration, and "
             "the long-term climate thermostat. Super-deep diamonds are also the "
             "only direct samples humanity has of the deep mantle."),
 "sig_pointer": ("The Signature system proposes a super-deep diamond census: "
             "systematic inclusion barometry on every known occurrence to map the "
             "true depth distribution of the deep carbon conveyor. See the "
             "Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats each super-deep diamond "
             "as a depth probe that survived the trip - and proposes reading all of "
             "them together to map how deep the carbon conveyor runs."),
 "signature_solution": (
     "Proposed approach. Step 1: gather super-deep diamonds from all known "
     "localities into one inclusion database - host mineral, inclusion phases, "
     "elastic barometry pressures, carbon and nitrogen isotopes, all measured to "
     "one protocol. Step 2: convert inclusion assemblages to formation depths "
     "with the latest high-pressure phase diagrams, with full uncertainty "
     "propagation. Step 3: test the subduction hypothesis statistically - do "
     "light-carbon diamonds sit deeper and cluster near ancient subduction zones "
     "reconstructed by plate models? Step 4: estimate the flux - what fraction "
     "of diamonds are super-deep, and what carbon tonnage does that imply per "
     "million years?\n"
     "Assumptions: that inclusions record formation conditions and not later "
     "re-equilibration (elastic barometry corrects for this, imperfectly); that "
     "the known localities sample the global population; that plate "
     "reconstructions are reliable back to the diamonds formation ages.\n"
     "What would confirm it: depth and isotope systematics correlating with "
     "reconstructed subduction geometry, and a flux estimate that matters to the "
     "mantle carbon budget.\n"
     "What would kill it: super-deep diamonds showing no geographic or isotopic "
     "structure, or formation depths collapsing to shallow values under better "
     "barometry.\n"
     "What this does NOT claim: it does not claim most mantle carbon is recycled "
     "surface carbon; it does not date the start of the conveyor; it is not "
     "established science."),
 "citations": [
     "Shirey S B, Shigley J E. Recent advances in understanding the geology of diamonds. Gems Gemol; 2013.",
     "Smith E M et al. Large gem diamonds from metallic liquid in Earths deep mantle. Science; 2016.",
     "Stachel T, Harris J W. The origin of cratonic diamonds. Lithos; 2008."],
 "explorer": {
   "blurb": ("A depth-probe calculator: from inclusion mineralogy it estimates "
             "formation pressure and depth, and compares the deep carbon flux with "
             "surface volcanic outgassing."),
   "assumptions": {"pressure_GPa": 25.0, "superdeep_fraction": 0.01,
                   "diamond_production_ct_yr": 130000000.0, "carat_g": 0.2},
   "model_src": (
     "def run(A):\n"
     "    depth_km = A[\"pressure_GPa\"] * 30.0\n"
     "    superdeep_ct = A[\"diamond_production_ct_yr\"] * A[\"superdeep_fraction\"]\n"
     "    carbon_t_yr = superdeep_ct * A[\"carat_g\"] / 1e6\n"
     "    return {\"formation_depth_km\": depth_km,\n"
     "            \"superdeep_carats_yr\": superdeep_ct,\n"
     "            \"implied_carbon_t_yr\": carbon_t_yr}\n"),
   "steps": [("Formation depth at 25 GPa", "formation_depth_km", "km"),
             ("Super-deep carats per year at 1 percent", "superdeep_carats_yr", "carats/yr"),
             ("Implied deep carbon sampled per year", "implied_carbon_t_yr", "tonnes/yr")],
   "confirm": ["Depth-isotope systematics correlate with reconstructed subduction geometry.",
               "The flux estimate is large enough to matter to the mantle carbon budget."],
   "refute": ["No geographic or isotopic structure, or formation depths collapse under better barometry."],
   "checks": [("formation_depth_km", 400.0, 900.0),
              ("superdeep_carats_yr", 100000.0, 10000000.0),
              ("implied_carbon_t_yr", 0.01, 10.0)],
   "honesty": ("We do not know how deep the carbon conveyor runs; this explorer "
               "only converts pressures to depths and production to tonnages so the "
               "scale of the question is visible.")}
},
# ---------------------------------------------------------------- 6
{
 "key": "cambrian-explosion",
 "name": "What Caused the Cambrian Explosion?",
 "group": "Paleontology",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": ("About 541 million years ago, nearly all major animal body plans appear "
             "in the fossil record within a few tens of millions of years - the "
             "Cambrian explosion. After three billion years of mostly microbes, "
             "animals diversified explosively, and no single trigger is proven."),
 "background": ("Darwin himself called the sudden appearance of complex fossils his "
             "greatest objection to gradual evolution. The Burgess Shale and Chinas "
             "Chengjiang deposits preserve the explosion in exquisite detail: "
             "arthropods, chordates, and bizarre experiments like Hallucigenia, all "
             "within roughly 20 to 30 million years. Candidate triggers abound - "
             "rising oxygen crossing a metabolic threshold, the evolution of Hox "
             "genes enabling body plans, the ecological arms race once predation "
             "and eyes evolved, and increased calcium permitting skeletons. Each has "
             "evidence and each has problems: oxygen proxies disagree, genes "
             "predate the explosion by molecular clocks, and ecology explains the "
             "pattern better than the onset. Most researchers now favor a "
             "multi-cause cascade, but the weighting - and the spark - remain open."),
 "why_it_matters": ("The explosion set the body-plan menu for all later animal "
             "evolution, including vertebrates and ultimately humans. Understanding "
             "its trigger is understanding what turns a microbial planet into an "
             "animal planet - the most relevant precedent for how complex life "
             "might arise elsewhere."),
 "sig_pointer": ("The Signature system proposes a trigger-weighting program: rank "
             "each candidate cause against the highest-resolution fossil and "
             "geochemical timelines to find which leads and which follows. See the "
             "Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the explosion as a "
             "cascade with a spark - and proposes timing every candidate trigger "
             "against the fossil record to find which one fired first."),
 "signature_solution": (
     "Proposed approach. Step 1: build a unified timeline at million-year "
     "resolution for the Ediacaran-Cambrian boundary interval - fossil first "
     "appearances, oxygen proxies (iron speciation, molybdenum isotopes), "
     "seawater chemistry, and trace-fossil complexity - with all uncertainties "
     "explicit. Step 2: for each candidate trigger, state its predicted lead-lag "
     "signature in advance: oxygen-first predicts geochemical shift before "
     "diversification; genes-first predicts cryptic molecular divergence before "
     "fossils; ecology-first predicts trace-fossil escalation leading body "
     "fossils. Step 3: score each prediction against the timeline with formal "
     "model comparison, penalizing extra assumptions. Step 4: test the winner "
     "on a second interval - the Great Ordovician biodiversification - as an "
     "out-of-sample check.\n"
     "Assumptions: that the fossil record at this resolution is not dominated by "
     "preservation artifacts (the strongest objection); that geochemical proxies "
     "record global ocean state rather than local basins; that molecular clock "
     "dates are meaningful to tens of millions of years.\n"
     "What would confirm it: one trigger consistently leading the others across "
     "multiple basins, with the model comparison favoring it decisively and the "
     "Ordovician check agreeing.\n"
     "What would kill it: all proxies moving synchronously within dating error - "
     "no lead, no lag, no spark identifiable - or the timeline dissolving under "
     "better dating.\n"
     "What this does NOT claim: it does not claim a single cause; it does not "
     "dismiss preservation bias; it does not resolve the molecular-versus-fossil "
     "clock dispute by fiat; it is not established science."),
 "citations": [
     "Erwin D H et al. The Cambrian conundrum: early divergence and later ecological success. Science; 2011.",
     "Marshall C R. Explaining the Cambrian explosion of animals. Annu Rev Earth Planet Sci; 2006.",
     "Sperling E A et al. Oxygen, ecology, and the Cambrian radiation of animals. PNAS; 2013."],
 "explorer": {
   "blurb": ("A diversification-rate calculator: from species counts and interval "
             "lengths it computes how fast body plans appeared, and compares the "
             "explosion with background rates."),
   "assumptions": {"phyla_appeared": 35.0, "interval_Ma": 25.0,
                   "background_phyla_per_Ma": 0.05, "ediacaran_Ma": 100.0},
   "model_src": (
     "def run(A):\n"
     "    explosion_rate = A[\"phyla_appeared\"] / A[\"interval_Ma\"]\n"
     "    background_total = A[\"background_phyla_per_Ma\"] * A[\"ediacaran_Ma\"]\n"
     "    speedup = explosion_rate / A[\"background_phyla_per_Ma\"]\n"
     "    return {\"phyla_per_Ma\": explosion_rate,\n"
     "            \"background_expected_phyla\": background_total,\n"
     "            \"rate_speedup\": speedup}\n"),
   "steps": [("Body plans appearing per million years", "phyla_per_Ma", "phyla/Ma"),
             ("Expected at background rate over 100 Myr", "background_expected_phyla", "phyla"),
             ("How many times faster than background", "rate_speedup", "x")],
   "confirm": ["One trigger leads the others across multiple basins and wins formal model comparison.",
               "The Ordovician out-of-sample check agrees."],
   "refute": ["All proxies move synchronously within dating error, or the timeline dissolves under better dating."],
   "checks": [("phyla_per_Ma", 0.5, 5.0),
              ("background_expected_phyla", 1.0, 20.0),
              ("rate_speedup", 5.0, 100.0)],
   "honesty": ("We do not know the trigger; this explorer only measures how "
               "extraordinary the rate was, which is the fact every trigger theory "
               "must explain.")}
},
# ---------------------------------------------------------------- 7
{
 "key": "lost-continents",
 "name": "How Do We Reconstruct Continents That No Longer Exist?",
 "group": "Paleogeography",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": ("Geologists draw maps of supercontinents like Rodinia and Pannotia that "
             "broke apart a billion years ago, yet the method - paleomagnetism - "
             "cannot measure ancient longitude at all. The maps rest on an "
             "unprovable assumption, and rival reconstructions disagree wildly."),
 "background": ("When volcanic rocks cool, magnetic minerals freeze in the direction "
             "of Earths field, recording the latitude where the rock formed - but "
             "never the longitude, because the field is symmetric around the spin "
             "axis. Apparent polar wander paths track a continents drift in "
             "latitude and rotation, and geologists slide continents east-west until "
             "geological features line up: matching mountain belts, matching rift "
             "margins, matching fossil provinces. For Rodinia, the matches are "
             "ambiguous enough that published reconstructions place Australia "
             "against North America in completely different orientations. True polar "
             "wander - the whole solid Earth tipping relative to its spin axis - "
             "can further scramble the record. The maps in textbooks are therefore "
             "best-fit hypotheses, some of them barely better than educated art."),
 "why_it_matters": ("Paleogeography underpins everything about ancient climate, "
             "ocean circulation, and evolution: where the continents sat decides "
             "whether an ice age was possible and which species could meet. If the "
             "maps are wrong, the stories built on them - Snowball Earth, the "
             "Cambrian explosion geography - rest on sand."),
 "sig_pointer": ("The Signature system proposes a reconstruction bake-off: score "
             "rival supercontinent maps against independent geological tests and "
             "publish the uncertainty honestly. See the Signature Edition record "
             "for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats paleogeographic maps as "
             "competing hypotheses - and proposes grading them like hypotheses, "
             "with the longitude problem stated up front instead of hidden."),
 "signature_solution": (
     "Proposed approach. Step 1: collect the leading Rodinia and Pannotia "
     "reconstructions into one digital atlas with identical data layers - "
     "paleomagnetic poles with error ellipses, piercing points, large igneous "
     "province matches. Step 2: define independent tests each reconstruction must "
     "pass: do proposed conjugate margins share rift-to-drift stratigraphy, do "
     "detrital zircon age spectra match across the join, do the implied ocean "
     "widths fit spreading-rate limits? Step 3: score every reconstruction "
     "blind against the tests, with longitude freedom penalized explicitly - a "
     "map that needs an untestable longitude shift scores lower. Step 4: publish "
     "a consensus-uncertainty map showing where all surviving reconstructions "
     "agree and where they do not.\n"
     "Assumptions: that paleomagnetic poles are primary and not reset (the "
     "chronic worry); that zircon age spectra are distinctive enough to "
     "fingerprint margins; that true polar wander can be detected and corrected "
     "rather than silently absorbed.\n"
     "What would confirm it: one reconstruction passing tests the others fail, "
     "with agreement zones covering most continental blocks.\n"
     "What would kill it: all reconstructions failing different tests - "
     "evidence the data cannot yet choose - or the consensus map shrinking to "
     "nearly nothing.\n"
     "What this does NOT claim: it does not claim paleomagnetism can measure "
     "longitude; it does not endorse any published Rodinia; it is not "
     "established science."),
 "citations": [
     "Li Z X et al. Assembly, configuration, and break-up history of Rodinia. Precambrian Res; 2008.",
     "Evans D A D. True polar wander and supercontinents. Tectonophysics; 2003.",
     "Meert J G, Torsvik T H. The making and unmaking of a supercontinent: Rodinia revisited. Tectonophysics; 2003."],
 "explorer": {
   "blurb": ("A longitude-uncertainty visualizer: it computes how far a continent "
             "can slide east-west without violating paleomagnetic data, showing "
             "why rival maps coexist."),
   "assumptions": {"latitude_deg": 30.0, "pole_error_deg": 10.0,
                   "earth_circumference_km": 40075.0, "candidate_longitude_shift_deg": 60.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    lat_km_per_deg = A[\"earth_circumference_km\"] / 360.0 * math.cos(math.radians(A[\"latitude_deg\"]))\n"
     "    latitude_slop_km = A[\"pole_error_deg\"] * A[\"earth_circumference_km\"] / 360.0\n"
     "    longitude_slop_km = A[\"candidate_longitude_shift_deg\"] * lat_km_per_deg\n"
     "    return {\"km_per_degree_longitude\": lat_km_per_deg,\n"
     "            \"latitude_uncertainty_km\": latitude_slop_km,\n"
     "            \"free_longitude_slide_km\": longitude_slop_km}\n"),
   "steps": [("Kilometers per degree of longitude at 30 deg latitude", "km_per_degree_longitude", "km/deg"),
             ("Latitude uncertainty from a 10 deg pole error", "latitude_uncertainty_km", "km"),
             ("How far a continent may slide east-west, unconstrained", "free_longitude_slide_km", "km")],
   "confirm": ["One reconstruction passes independent tests the others fail, with broad agreement zones.",
               "Longitude penalties separate the maps cleanly."],
   "refute": ["All reconstructions fail different tests, or the consensus map shrinks to nearly nothing."],
   "checks": [("km_per_degree_longitude", 50.0, 120.0),
              ("latitude_uncertainty_km", 500.0, 2000.0),
              ("free_longitude_slide_km", 2000.0, 8000.0)],
   "honesty": ("We do not know the true maps; this explorer only quantifies the "
               "longitude freedom that lets rival reconstructions coexist.")}
},
# ---------------------------------------------------------------- 8
{
 "key": "rising-mountains",
 "name": "Why Do Some Mountains Keep Rising After Collision Ends?",
 "group": "Orogeny",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": ("The Alps finished colliding with Europe tens of millions of years "
             "ago, yet GPS shows they are still rising about a millimeter a year. "
             "Several mountain belts keep growing long after the tectonic crash "
             "that built them ended - and the engine is disputed."),
 "background": ("When continents collide, crust thickens and mountains rise; when "
             "collision stops, erosion should win and the range should sink. The "
             "Alps, the Pyrenees, and parts of the Appalachians defy this: they "
             "rise today with no active convergence. Candidate engines include "
             "isostatic rebound as erosion unloads the crust, delamination - the "
             "dense lower lithosphere peeling off and sinking, letting the crust "
             "bob up - and the melting away of glaciers since the last ice age, "
             "which unloaded the crust only thousands of years ago. In the Alps, "
             "about half the measured uplift is explained by erosion-driven "
             "rebound and deglaciation, but the rest needs a deeper engine, and "
             "seismic images of a possible detaching slab keep the delamination "
             "hypothesis alive without proving it."),
 "why_it_matters": ("Post-collisional uplift decides how long mountains shape "
             "climate - the Alps steer European weather - and how sedimentary "
             "basins fill with eroded debris that becomes oil and gas reservoirs. "
             "It is also the cleanest natural experiment in how the deep "
             "lithosphere and the surface talk to each other."),
 "sig_pointer": ("The Signature system proposes an uplift-budget audit: measure "
             "every uplift component - erosion, ice, deep engine - in one range "
             "until the millimeters add up or the missing engine is exposed. See "
             "the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats rising mountains as an "
             "accounting problem - every millimeter per year must come from "
             "somewhere, and proposes auditing each source until the books "
             "balance."),
 "signature_solution": (
     "Proposed approach. Step 1: in a target range (the western Alps), measure "
     "the full uplift budget with one campaign - GPS vertical rates, erosion "
     "rates from cosmogenic nuclides, ice-unloading history from glacial "
     "geology, and crustal thickness from seismic profiles. Step 2: compute the "
     "predicted rebound from erosion plus deglaciation with a flexural model, "
     "and subtract from observed uplift - the residual is the deep engine, "
     "quantified. Step 3: image the deep lithosphere with receiver functions "
     "and tomography to test for a detaching slab beneath the residual-uplift "
     "zone. Step 4: repeat in a second range with different history (the "
     "Pyrenees) to test whether the same engine generalizes.\n"
     "Assumptions: that GPS vertical rates are tectonic and not hydrological "
     "noise (a real contamination); that cosmogenic erosion rates average "
     "correctly over the GPS epoch; that flexural models capture the isostatic "
     "response.\n"
     "What would confirm it: the residual uplift matching the location and "
     "magnitude predicted by an imaged detaching slab, in both ranges.\n"
     "What would kill it: residuals scattering with no relation to deep "
     "structure, or the budget closing fully with erosion plus ice and no deep "
     "engine needed.\n"
     "What this does NOT claim: it does not claim delamination is happening; it "
     "does not project uplift into the future; it is not established science."),
 "citations": [
     "Sternai P et al. On the influence of the Alpine orogeny on erosion-driven uplift. Earth Planet Sci Lett; 2012.",
     "Champagnac J D et al. Erosion-driven uplift of the modern Central Alps. Tectonophysics; 2007.",
     "Lyon-Caen H, Molnar P. Gravity anomalies, flexure of the Indian plate. J Geophys Res; 1983."],
 "explorer": {
   "blurb": ("An uplift-budget calculator: it subtracts erosion-driven rebound "
             "and ice unloading from observed GPS uplift, exposing the residual "
             "that needs a deep engine."),
   "assumptions": {"gps_uplift_mm_yr": 1.2, "erosion_rebound_mm_yr": 0.5,
                   "ice_rebound_mm_yr": 0.2, "measurement_noise_mm_yr": 0.3},
   "model_src": (
     "def run(A):\n"
     "    residual = A[\"gps_uplift_mm_yr\"] - A[\"erosion_rebound_mm_yr\"] - A[\"ice_rebound_mm_yr\"]\n"
     "    significant = residual > A[\"measurement_noise_mm_yr\"]\n"
     "    deep_fraction = residual / A[\"gps_uplift_mm_yr\"]\n"
     "    return {\"residual_uplift_mm_yr\": residual,\n"
     "            \"deep_fraction\": deep_fraction,\n"
     "            \"residual_significant\": 1.0 if significant else 0.0}\n"),
   "steps": [("Uplift unexplained by erosion and ice", "residual_uplift_mm_yr", "mm/yr"),
             ("Fraction of uplift needing a deep engine", "deep_fraction", ""),
             ("Residual above measurement noise (1=yes)", "residual_significant", "")],
   "confirm": ["The residual matches the location and magnitude predicted by an imaged detaching slab in two ranges.",
               "The budget refuses to close without a deep component."],
   "refute": ["Residuals scatter with no relation to deep structure, or the budget closes with erosion plus ice alone."],
   "checks": [("residual_uplift_mm_yr", 0.1, 1.0),
              ("deep_fraction", 0.1, 0.9)],
   "honesty": ("We do not know the deep engine; this explorer only isolates how "
               "much uplift is left over after the known sources are subtracted.")}
},
# ---------------------------------------------------------------- 9
{
 "key": "missing-old-rocks",
 "name": "Why Are There So Few Rocks Older Than Four Billion Years?",
 "group": "Precambrian",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": ("Earth is 4.54 billion years old, yet the oldest intact rocks - the "
             "Acasta Gneiss - are only 4.03 billion years old. Half a billion "
             "years of Earth history survives only as sand-sized zircon grains, "
             "and what erased the rest is debated."),
 "background": ("The Hadean eon, Earths first 600 million years, left no intact "
             "rock formations anywhere. The oldest survivors are detrital zircons "
             "from Jack Hills, Australia, dated to 4.4 billion years, which prove "
             "continental-type crust and liquid water existed astonishingly early. "
             "Candidates for the erasure include the Late Heavy Bombardment "
             "pulverizing the early crust, vigorous early plate tectonics or "
             "overturn recycling it into the mantle, and a magma-ocean aftermath "
             "that simply never stabilized a lasting crust. Each predicts a "
             "different Hadean: bombardment implies a battered but stable crust, "
             "recycling implies a dynamic young planet, and the zircon oxygen "
             "isotopes - which suggest cool, wet surface conditions - constrain "
             "but do not choose between them."),
 "why_it_matters": ("The missing half-billion years contains the origin of the "
             "continents, the oceans, and possibly life itself. Whatever erased "
             "the Hadean crust set the initial conditions for everything geology "
             "studies afterward - it is the lost first chapter of the planet."),
 "sig_pointer": ("The Signature system proposes a Hadean survivor census: "
             "systematic dating of every pre-4.0-billion-year fragment worldwide "
             "to test whether the erasure was global and synchronous or patchy. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the missing Hadean as "
             "a forensic cold case - and proposes cataloguing every surviving "
             "fragment to reconstruct what destroyed the rest."),
 "signature_solution": (
     "Proposed approach. Step 1: build a global database of all Hadean-age "
     "materials - Jack Hills-type detrital zircons, Acasta gneisses, Nuvvuagittuq "
     "candidates, lunar and Martian Hadean-equivalent samples as controls - with "
     "uniform U-Pb ages and hafnium and oxygen isotopes. Step 2: test the "
     "bombardment hypothesis against impact-reset age spectra: a late spike "
     "should reset ages across fragments globally at the same time. Step 3: "
     "test the recycling hypothesis against hafnium model ages: wholesale crustal "
     "recycling predicts a characteristic depleted-mantle extraction signature. "
     "Step 4: run the two hypotheses as competing Bayesian models and report "
     "which the survivor census actually favors, with the losing hypothesis "
     "stated plainly.\n"
     "Assumptions: that detrital zircons sample Hadean crust representatively "
     "(they sample what survived erosion, a bias); that impact resetting has a "
     "recognizable age signature; that the lunar bombardment record applies to "
     "Earth with scaling.\n"
     "What would confirm it: a globally synchronous reset age in the census, or "
     "a recycling signature no bombardment model can produce - one clear "
     "winner.\n"
     "What would kill it: survivor ages scattering with no global pattern, or "
     "both models fitting equally well - the data simply cannot choose.\n"
     "What this does NOT claim: it does not claim to recover Hadean geology; it "
     "does not date the Late Heavy Bombardment from Earth rocks alone; it is "
     "not established science."),
 "citations": [
     "Wilde S A et al. Evidence from detrital zircons for the existence of continental crust and oceans on the Earth 4.4 Gyr ago. Nature; 2001.",
     "Harrison T M. The Hadean crust. Annu Rev Earth Planet Sci; 2009.",
     "O'Neill C, Debaille V. The evolution of Hadean-Eoarchaean geodynamics. Earth Planet Sci Lett; 2014."],
 "explorer": {
   "blurb": ("A survivor-fraction calculator: it converts the known Hadean "
             "fragments into an estimated survival fraction and compares "
             "bombardment versus recycling erasure rates."),
   "assumptions": {"earth_age_Ga": 4.54, "oldest_rock_Ga": 4.03,
                   "zircon_oldest_Ga": 4.4, "hadean_end_Ga": 4.0},
   "model_src": (
     "def run(A):\n"
     "    missing_Ga = A[\"earth_age_Ga\"] - A[\"oldest_rock_Ga\"]\n"
     "    hadean_Ga = A[\"earth_age_Ga\"] - A[\"hadean_end_Ga\"]\n"
     "    recorded_fraction = (A[\"oldest_rock_Ga\"] - A[\"hadean_end_Ga\"]) / hadean_Ga\n"
     "    return {\"missing_history_Ga\": missing_Ga,\n"
     "            \"hadean_duration_Ga\": hadean_Ga,\n"
     "            \"hadean_recorded_fraction\": recorded_fraction}\n"),
   "steps": [("Billions of years with no intact rocks", "missing_history_Ga", "Ga"),
             ("Duration of the Hadean eon", "hadean_duration_Ga", "Ga"),
             ("Fraction of the Hadean with any rock record", "hadean_recorded_fraction", "")],
   "confirm": ["The survivor census shows a globally synchronous reset age, or a recycling signature no bombardment model produces.",
               "One hypothesis wins the Bayesian comparison decisively."],
   "refute": ["Survivor ages scatter with no global pattern, or both models fit equally well."],
   "checks": [("missing_history_Ga", 0.3, 0.8),
              ("hadean_duration_Ga", 0.4, 0.7),
              ("hadean_recorded_fraction", 0.0, 0.2)],
   "honesty": ("We do not know what erased the Hadean; this explorer only "
               "measures how much is missing, which is the quantity every erasure "
               "theory must account for.")}
},
]


# ---------------------------------------------------------------- combined
from entries_10_19 import ENTRIES_10_19
from entries_20_34 import ENTRIES_20_34

ENTRIES.extend(ENTRIES_10_19)
ENTRIES.extend(ENTRIES_20_34)

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
assert [e["ladder_rank"] for e in ENTRIES] == list(range(1, 35)), "ladder ranks must be 1..34 in order"
assert len({e["key"] for e in ENTRIES}) == 34, "duplicate keys"
