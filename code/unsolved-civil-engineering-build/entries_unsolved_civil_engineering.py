#!/usr/bin/env python3
"""Entries for the Unsolved Civil Engineering databases (Manon 2026-10-17
16:15 orders, Unsolved Problems Solved series).

Verified 2026-10-17: whole-system dedupe sweep over the full manifest plus
the shared exact-title gate: all 68 final titles (34 public + 34
" (Signature Edition)") are gate-clean; zero title-fragment hits in the
manifest. Two NEW databases, 34 ladder-ordered records each:

  unsolved-civil-engineering            - The Unsolved Civil Engineering
                                          Database (public-harvest: real,
                                          fact-checked famous unsolved
                                          civil engineering problems -
                                          century-durable concrete,
                                          earthquake-proof megastructures,
                                          self-healing infrastructure,
                                          underground city engineering,
                                          flood-proof coastal cities -
                                          every record carrying the problem
                                          statement, its history, why it
                                          matters, and a short pointer to
                                          the Signature proposed solution)
  unsolved-civil-engineering-signature  - The Unsolved Civil Engineering
                                          Signature Database (his original
                                          Signature Civil Engineering
                                          Method applied to the same 34
                                          problems: every record carries
                                          the full Signature-generated
                                          proposed solution, opening with
                                          the exact honesty label, laying
                                          out assumptions, reasoning path,
                                          proposed mechanism, confirm/kill
                                          evidence, and what it does NOT
                                          claim; src signature, titles
                                          suffixed " (Signature Edition)",
                                          never presented as established
                                          science or authentic public
                                          record)

34 records each, ordered by the teaching ladder (ladder_rank 1-34,
ladder_tier approachable/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-USCV- (public) and JAH-USCVS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Standing exclusion honored: nothing on neutralizing or defeating military
or defense-grade systems - every problem is civilian infrastructure. No
religious talk. Nothing hate-adjacent, profane, or inappropriate.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_civil_engineering.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), walks
the Signature solution approach as a solution-explorer, and ends with the
OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature original - his original Signature Civil Engineering "
            "Method applied to famous unsolved civil engineering problems: "
            "proposed solution approaches with stated assumptions, a "
            "reasoning path, a proposed mechanism, what evidence would "
            "confirm or kill the approach, and what it does not claim. "
            "Clearly labeled Signature-made, never presented as established "
            "science or authentic public record.")

CIT_ASCE21 = ("American Society of Civil Engineers. Report Card for "
              "America's Infrastructure; 2021. Forty-two percent of more "
              "than 617,000 bridges are at least 50 years old; 7.5 percent "
              "are structurally deficient; a water main breaks every two "
              "minutes and an estimated six billion gallons of treated "
              "water are lost to leaks each day.")
CIT_AAA = ("American Automobile Association. Pothole damage report; 2016. "
           "Pothole damage costs United States drivers about three billion "
           "dollars per year in vehicle repairs.")
CIT_SALT = ("Federal Highway Administration winter maintenance surveys and "
            "U.S. Geological Survey chloride studies: on the order of twenty "
            "million tons of road salt are spread on United States roadways "
            "each winter, driving chloride-induced corrosion of bridges and "
            "pavements.")
CIT_BAZALGETTE = ("London's Bazalgette interceptor sewer system, completed "
                  "1875 under engineer Joseph Bazalgette: brick and concrete "
                  "tunnels still carrying the city's sewage after more than "
                  "150 years of continuous service.")
CIT_PANTHEON = ("The Pantheon, Rome, completed circa 125 AD: unreinforced "
                "concrete dome standing nearly two thousand years. Modern "
                "studies of Roman marine concrete (Jackson et al.) identify "
                "aluminum-tobermorite crystal growth that strengthens the "
                "material over centuries.")
CIT_FEMA_FLOOD = ("Federal Emergency Management Agency. Floodproofing "
                  "guidance and the National Flood Insurance Program: dry "
                  "floodproofing, wet floodproofing, elevation, and "
                  "relocation as the standard residential strategies.")
CIT_SPONGE = ("Ministry of Housing and Urban-Rural Development, China. "
              "Sponge City program, launched 2015: thirty pilot cities "
              "tasked with absorbing and reusing the majority of urban "
              "rainfall through permeable surfaces, bioswales, wetlands, "
              "and storage.")
CIT_QUAKE_SCHOOL = ("Japan's nationwide school seismic retrofit program "
                    "after the 1995 Kobe earthquake; California Senate Bill "
                    "1953 (1994) requiring acute-care hospitals to meet "
                    "strict seismic performance standards.")
CIT_USACE_LEVEE = ("U.S. Army Corps of Engineers National Levee Database; "
                   "ASCE Hurricane Katrina External Review Panel, 2007: the "
                   "2005 New Orleans levee failures were engineering "
                   "failures of design and maintenance, not just storm "
                   "strength.")
CIT_DELTA = ("Netherlands Delta Works; the Maeslantkering storm surge "
             "barrier, operational 1997; the Thames Barrier, London, "
             "operational 1982; the MOSE mobile barriers, Venice, first "
             "full operation 2020.")
CIT_TAIPEI = ("Taipei 101, Taiwan: a 660-tonne tuned mass damper suspended "
              "between the 87th and 92nd floors, among the largest such "
              "devices ever installed in a building.")
CIT_SKYTREE = ("Tokyo Skytree, 634 meters, completed 2012: a central "
               "reinforced-concrete shinbashira column, structurally "
               "independent of the outer steel tower, damps seismic motion.")
CIT_SHAKEALERT = ("U.S. Geological Survey. ShakeAlert earthquake early "
                  "warning system, public operation in California from "
                  "2019; Japan Meteorological Agency emergency earthquake "
                  "warning system.")
CIT_NORWAY_TUNNEL = ("Norwegian Public Roads Administration. E39 "
                     "fjord-crossing program: submerged floating tunnel "
                     "concepts studied for crossings including the "
                     "Bjornafjorden, where depths and widths rule out "
                     "conventional bridges and bored tunnels.")
CIT_MONTREAL = ("Montreal RESO: roughly 33 kilometers of interconnected "
                "underground pedestrian ways, among the largest underground "
                "cities in the world.")
CIT_HELSINKI = ("City of Helsinki Underground Master Plan: a legally "
                "binding allocation of subsurface space for transit, "
                "parking, utilities, and future public facilities.")
CIT_BURJ = ("Burj Khalifa, Dubai, 828 meters, completed 2010; Jeddah "
            "Tower, Saudi Arabia, planned above 1,000 meters - projects "
            "that define the engineering frontier of the supertall.")
CIT_TIMBER = ("Mjostarnet, Norway, 85.4 meters, completed 2019; Ascent, "
              "Milwaukee, 86.6 meters, completed 2022: the tallest "
              "mass-timber buildings standing, testing fire and height "
              "limits of engineered wood.")
CIT_JAKARTA = ("Jakarta, Indonesia: northern districts subsiding at rates "
               "measured in tens of centimeters per year, driven by "
               "groundwater extraction; Indonesia announced the capital "
               "relocation to Nusantara in 2019.")
CIT_LOUISIANA = ("U.S. Geological Survey: coastal Louisiana has lost on the "
                 "order of two thousand square miles of land since the "
                 "1930s to subsidence, sea-level rise, and sediment "
                 "starvation.")
CIT_JAPAN_TSUNAMI = ("The 2011 Tohoku earthquake and tsunami; Japan's "
                     "post-2011 program of roughly four hundred kilometers "
                     "of coastal seawalls, some reaching 14.7 meters, plus "
                     "vertical evacuation towers and hardened warning "
                     "systems.")
CIT_OROVILLE = ("Oroville Dam spillway crisis, California, 2017; the U.S. "
                "National Inventory of Dams lists more than ninety thousand "
                "dams with an average age above sixty years.")
CIT_PERMAFROST = ("IPCC Sixth Assessment Report on permafrost thaw; "
                  "thermosyphon foundations and elevated pile construction "
                  "as practiced on the Trans-Alaska Pipeline System and in "
                  "Arctic settlements.")
CIT_OCEANIX = ("Oceanix Busan: the UN-Habitat-backed floating-city "
               "prototype designed by BIG, announced 2021, planned as a "
               "modular flood-proof settlement for ten thousand residents.")
CIT_CST = ("Cargo Sous Terrain, Switzerland: the planned roughly "
           "500-kilometer automated underground freight network intended "
           "to move goods beneath cities and highways.")
CIT_ROOM_RIVER = ("Netherlands Room for the River program: widening "
                  "floodplains and relocating dikes to give rivers space, "
                  "completed as a national flood-safety strategy.")
CIT_DELFT_ASPHALT = ("Delft University of Technology self-healing asphalt "
                     "research (Schlangen group): steel-fiber asphalt "
                     "rejuvenated by induction heating, plus capsule-based "
                     "rejuvenator systems tested on Dutch highways.")
CIT_AMPHIBIOUS = ("Amphibious housing at Maasbommel, Netherlands "
                  "(DuraVermeer); the UK amphibious house by Baca "
                  "Architects, completed 2014: dwellings that rest on the "
                  "ground in dry weather and float on floodwater.")
CIT_ISO15686 = ("ISO 15686, Buildings and constructed assets - Service "
                "life planning: the international standard framework for "
                "designing, predicting, and managing service life.")
CIT_CABLE = ("Post-Tensioning Institute and fib recommendations on stay "
              "cables: cable-stayed bridge stays commonly require major "
              "intervention or full replacement within thirty to fifty "
              "years of service.")
CIT_DERINKUYU = ("Derinkuyu, Cappadocia: the ancient multi-level "
                 "underground city, descending some sixty meters, that "
                 "sheltered tens of thousands - proof that deep "
                 "habitability long predates modern engineering.")
CIT_KONE = ("KONE UltraRope: carbon-fiber elevator hoisting technology "
            "that roughly doubles practical travel height versus steel "
            "ropes, a key enabler studied for kilometer-class towers.")

ENTRIES = [
    {
        "key": "pothole_roads",
        "name": "Pothole-Proof Roads",
        "group": "Urban Infrastructure",
        "ladder_rank": 1,
        "ladder_tier": "approachable",
        "problem": ("Every winter, freeze-thaw cycles and heavy traffic tear "
                    "millions of potholes into paved roads, costing drivers "
                    "billions in repairs and cities billions more in "
                    "patching. The problem is to build road surfaces that "
                    "resist pothole formation for decades instead of "
                    "seasons."),
        "background": ("Potholes form when water seeps into cracks in the "
                       "pavement, freezes and expands, then thaws - each "
                       "cycle prying the surface further apart until traffic "
                       "knocks chunks loose. American drivers pay about "
                       "three billion dollars a year for pothole damage to "
                       "tires, wheels, and suspensions, and municipal crews "
                       "re-patch the same streets every spring in an endless "
                       "cycle. Asphalt is a viscoelastic material that "
                       "slowly heals micro-cracks on its own when warm, but "
                       "modern traffic loads and colder, wetter winters "
                       "outpace that natural healing. Researchers have "
                       "tested self-healing asphalt with steel fibers that "
                       "can be re-melted by induction heating, and "
                       "capsules of rejuvenating oil that break open inside "
                       "cracks, with trials on Dutch highways. Yet no "
                       "pavement system in routine commercial use survives "
                       "decades of freeze-thaw without potholing, and the "
                       "economics of premium pavements still lose to cheap "
                       "asphalt plus endless patching."),
        "why_it_matters": ("Pothole-proof roads would end one of the most "
                           "visible failures of public infrastructure and "
                           "free the billions spent on reactive patching "
                           "for real improvements. Smoother long-life "
                           "pavements also cut fuel use, tire wear, and "
                           "crash risk. A road that heals itself is the "
                           "gateway technology for every other "
                           "self-maintaining infrastructure idea."),
        "signature_solution": (
            "Step one, the assumptions: potholes are a fatigue-and-moisture "
            "problem, not a strength problem, so the fix is healing speed, "
            "not thicker pavement; a pavement that re-seals every crack "
            "within one freeze-thaw cycle never develops a pothole. Step "
            "two, the reasoning path: asphalt already self-heals when warm, "
            "so the engineering task is to trigger that healing on demand "
            "in winter - induction heating of steel-fiber asphalt, as "
            "demonstrated in Dutch trials, can re-melt binder around "
            "micro-cracks in minutes. Step three, the proposed mechanism: "
            "a three-layer pavement - a waterproof membrane base that "
            "starves cracks of water, a steel-fiber structural asphalt "
            "course, and a sacrificial wearing course - swept nightly in "
            "winter by induction-heater trucks that re-seal the day's "
            "micro-cracking before water can enter. Step four, what would "
            "confirm it: a five-winter instrumented trial on a "
            "freeze-thaw corridor showing pothole counts per lane-kilometer "
            "at least ninety percent below a control section, with "
            "heating energy and truck costs audited per lane-kilometer. "
            "Step five, what would kill it: if induction energy costs "
            "exceed the patching budget it replaces, or if the membrane "
            "layer delaminates under traffic and becomes a new failure "
            "mode. What this does not claim: it does not claim roads that "
            "never wear - the wearing course is still replaced on "
            "schedule; the claim is zero potholes between resurfacings."),
        "sig_pointer": ("The Signature edition proposes a "
                        "heal-before-it-freezes pavement: waterproof "
                        "membrane base, induction-healable steel-fiber "
                        "asphalt, and nightly heater-truck passes that "
                        "re-seal micro-cracks within one freeze-thaw cycle."),
        "citations": [CIT_AAA, CIT_DELFT_ASPHALT],
    },
    {
        "key": "bridge_deck",
        "name": "Bridge Deck Deterioration",
        "group": "Bridges and Tunnels",
        "ladder_rank": 2,
        "ladder_tier": "approachable",
        "problem": ("The driving surface of a bridge - its deck - typically "
                    "fails decades before the bridge structure itself, "
                    "cracking and spalling as deicing salts eat the "
                    "reinforcing steel inside. The problem is to make bridge "
                    "decks last as long as the bridges they sit on."),
        "background": ("Bridge decks live the hardest life of any concrete "
                       "element: direct traffic impact, standing water, and "
                       "winter salt all at once. Chloride ions diffuse "
                       "through the concrete cover toward the steel "
                       "reinforcement; once they reach a critical "
                       "concentration the steel corrodes, expands, and "
                       "blows the concrete off in spalls. More than forty "
                       "percent of America's bridges are at least fifty "
                       "years old, and deck replacement is the most common "
                       "major rehabilitation - expensive, disruptive, and "
                       "repeated every few decades. Engineers have tried "
                       "epoxy-coated rebar, thicker covers, sealers, "
                       "cathodic protection, and stainless or "
                       "fiber-reinforced-polymer reinforcement, each helping "
                       "but none making deck replacement obsolete. The deck "
                       "remains the sacrificial part of the bridge, "
                       "accepted as consumable."),
        "why_it_matters": ("Decks that match structural lifespan would "
                           "eliminate the most frequent major surgery "
                           "bridges undergo, saving billions and avoiding "
                           "years of lane closures. It would also prove "
                           "that chloride exposure - the great killer of "
                           "reinforced concrete - can be engineered around "
                           "rather than merely slowed."),
        "signature_solution": (
            "Step one, the assumptions: the deck fails because chlorides "
            "reach steel, so a deck with no corrodible steel in the "
            "chloride zone cannot spall; the fix is material separation, "
            "not better coatings. Step two, the reasoning path: "
            "fiber-reinforced-polymer bars do not corrode at any chloride "
            "level, and ultra-high-performance concrete has chloride "
            "diffusion rates orders of magnitude below conventional "
            "concrete - combine them and the corrosion clock effectively "
            "stops. Step three, the proposed mechanism: a deck built as a "
            "sandwich - ultra-high-performance concrete bottom layer "
            "carrying the reinforcement (non-metallic), a replaceable thin "
            "wearing course on top that takes the traffic abuse, and "
            "embedded chloride sensors that report the one number that "
            "matters: has anything reached the bars. Step four, what would "
            "confirm it: accelerated chloride-ponding tests plus "
            "ten-year field decks showing zero delamination and sensor "
            "chloride readings flat at background. Step five, what would "
            "kill it: if the polymer bars creep or lose bond under "
            "decades of cyclic truck loading, or if the sandwich "
            "delaminates at the layer interface. What this does not "
            "claim: it does not claim maintenance-free bridges - bearings, "
            "joints, and the wearing course still need care; the claim is "
            "a deck that never needs structural replacement."),
        "sig_pointer": ("The Signature edition proposes a corrosion-proof "
                        "deck sandwich: non-metallic reinforcement in "
                        "ultra-high-performance concrete, a replaceable "
                        "wearing course, and embedded chloride sensors."),
        "citations": [CIT_ASCE21, CIT_SALT],
    },
    {
        "key": "floodproof_homes",
        "name": "Flood-Proof Homes for Ordinary Families",
        "group": "Water and Flood",
        "ladder_rank": 3,
        "ladder_tier": "approachable",
        "problem": ("Floods are the most common and costly natural disaster "
                    "for homeowners, yet ordinary houses are still built as "
                    "if water will never come. The problem is to make "
                    "flood-resilient homes affordable for regular families, "
                    "not just showcase projects."),
        "background": ("Standard residential construction puts living "
                       "space, electrical systems, and furnaces at or below "
                       "grade, exactly where floodwater goes. When rivers "
                       "rise, families lose everything on the ground floor, "
                       "then wait months for drying, mold remediation, and "
                       "rebuilds. Flood insurance programs strain under "
                       "repeat claims on the same properties, and buyout "
                       "programs cannot relocate whole neighborhoods. "
                       "Engineers know the answers - elevation, wet "
                       "floodproofing that lets water pass through "
                       "sacrificial lower levels, dry floodproofing with "
                       "sealed walls, and amphibious foundations that let "
                       "houses float up guideposts during floods - and "
                       "amphibious homes have been built in the Netherlands "
                       "and Britain. But these remain bespoke projects; the "
                       "production homebuilder market has no standard, "
                       "code-blessed, mortgage-friendly flood-proof house "
                       "design."),
        "why_it_matters": ("Affordable flood-proof homes would break the "
                           "flood-damage-rebuild cycle that impoverishes "
                           "families and exhausts disaster budgets. As "
                           "heavier rainfall pushes floods into areas that "
                           "never flooded before, resilient-by-default "
                           "housing is becoming a necessity rather than a "
                           "luxury."),
        "signature_solution": (
            "Step one, the assumptions: the barrier is cost and code, not "
            "physics - amphibious and elevated houses already work; the "
            "unsolved part is a repeatable design a production builder can "
            "sell at near-normal cost. Step two, the reasoning path: "
            "amphibious foundations are the most family-friendly option "
            "because the house looks and lives like a normal house until "
            "water arrives, unlike stilts which change the streetscape and "
            "accessibility. Step three, the proposed mechanism: a "
            "standardized amphibious chassis - a buoyant concrete hull "
            "foundation, four guideposts, flexible utility umbilicals - "
            "manufactured in a factory and dropped onto any lot, with the "
            "stick-built house above it completely conventional so "
            "builders, insurers, and code officials face nothing exotic. "
            "Step four, what would confirm it: a production run of at "
            "least one hundred homes, sold at less than fifteen percent "
            "above comparable conventional homes, that ride out a real "
            "flood event with zero living-space damage, documented by "
            "independent surveyors. Step five, what would kill it: if the "
            "hull and guidepost system cannot be insured at normal rates, "
            "or if debris impact during floods damages hulls faster than "
            "modeled. What this does not claim: it does not claim safety "
            "in catastrophic flash floods or against floating debris "
            "fields - the claim is survival of slow-rise riverine and "
            "coastal flooding up to the design depth."),
        "sig_pointer": ("The Signature edition proposes a factory-built "
                        "amphibious foundation chassis - buoyant hull, "
                        "guideposts, flexible utilities - carrying an "
                        "otherwise conventional house, sold near normal "
                        "cost."),
        "citations": [CIT_FEMA_FLOOD, CIT_AMPHIBIOUS],
    },
    {
        "key": "sponge_cities",
        "name": "Sponge Cities That Drink the Rain",
        "group": "Water and Flood",
        "ladder_rank": 4,
        "ladder_tier": "approachable",
        "problem": ("Modern cities are paved nearly watertight, so every "
                    "heavy rain becomes flash flooding in the streets. The "
                    "problem is to redesign the urban surface itself - "
                    "pavements, parks, rooftops - to absorb, store, and "
                    "slowly release stormwater instead of shedding it."),
        "background": ("A natural landscape absorbs most rainfall; a paved "
                       "city sheds nearly all of it into drains that were "
                       "sized for milder storms. When cloudbursts exceed "
                       "drain capacity, water sheets through streets, "
                       "floods subways, and overwhelms treatment plants "
                       "with combined sewage. China launched the Sponge "
                       "City program in 2015 across thirty pilot cities, "
                       "deploying permeable pavements, rain gardens, "
                       "bioswales, sunken green spaces, and underground "
                       "storage at district scale. Early results show "
                       "real runoff reduction, but maintenance of "
                       "permeable surfaces - which clog with sediment - "
                       "and the sheer retrofit cost across existing cities "
                       "remain unsolved at full urban scale. No major "
                       "metropolis has yet converted enough of its surface "
                       "to ride out its design storm without flooding."),
        "why_it_matters": ("Sponge surfaces attack urban flooding at the "
                           "source instead of at the drain, while also "
                           "recharging groundwater, cooling heat islands, "
                           "and filtering pollutants. Cracked at city "
                           "scale, it turns the pavement problem into the "
                           "drainage solution."),
        "signature_solution": (
            "Step one, the assumptions: the failure mode is clogging and "
            "neglect, not hydraulics - permeable systems work when new and "
            "die when unmaintained; the fix is maintenance designed in, "
            "not better pores. Step two, the reasoning path: streets are "
            "already swept and vacuumed by municipal fleets, so the sponge "
            "layer should be cleaned by the same passes that clean the "
            "street - make permeability restoration part of routine "
            "street sweeping rather than a specialist operation. Step "
            "three, the proposed mechanism: a two-layer street section - "
            "structural permeable base with storage voids sized for the "
            "local design storm, topped by permeable pavers - plus "
            "vacuum-sweeper trucks fitted with infiltration test heads "
            "that measure and log every block's absorption rate each "
            "pass, flagging clogged blocks for deep cleaning before the "
            "storm season. Step four, what would confirm it: a "
            "district-scale trial where measured runoff coefficients stay "
            "below target for five years under the sweeper-integrated "
            "regime, with street-flooding complaints at or near zero. "
            "Step five, what would kill it: if sediment loads in real "
            "traffic clog pavers faster than any feasible sweeping "
            "frequency can clear, or if freeze-thaw destroys permeable "
            "surfaces in cold climates. What this does not claim: it "
            "does not claim handling storms beyond the design event - the "
            "claim is a city surface that absorbs its design storm "
            "year after year without degradation."),
        "sig_pointer": ("The Signature edition proposes sponge streets "
                        "with maintenance designed in: permeable sections "
                        "restored by the same sweeper fleet that cleans "
                        "them, with per-block infiltration logging."),
        "citations": [CIT_SPONGE],
    },
    {
        "key": "quake_safe_schools",
        "name": "Quake-Safe Schools and Hospitals",
        "group": "Seismic Design",
        "ladder_rank": 5,
        "ladder_tier": "approachable",
        "problem": ("The buildings society needs most during an earthquake "
                    "- schools full of children, hospitals full of patients "
                    "- are often the oldest and weakest structures in "
                    "seismic zones. The problem is to retrofit them all, "
                    "affordably, without closing them for years."),
        "background": ("Modern seismic codes protect new buildings well, "
                       "but the existing stock predates them: unreinforced "
                       "masonry schools, non-ductile concrete hospital "
                       "towers, soft-story ground floors. Past earthquakes "
                       "keep teaching the same lesson - Kobe in 1995 drove "
                       "Japan's nationwide school retrofit program, and "
                       "California's hospital seismic law set hard "
                       "deadlines after Northridge in 1994, yet compliance "
                       "has been extended repeatedly as costs mounted. "
                       "Retrofit techniques exist - steel bracing, fiber "
                       "wraps, base isolation, damping walls - but they "
                       "are engineered one building at a time, priced one "
                       "building at a time, and installed while the "
                       "building tries to stay open. The unsolved part is "
                       "industrializing the retrofit: standard kits, "
                       "standard pricing, minimal disruption, applied to "
                       "thousands of buildings."),
        "why_it_matters": ("Children should not die in school collapses "
                           "and hospitals should not go dark in the hour "
                           "they are needed most. An industrialized "
                           "retrofit method would convert the world's most "
                           "vulnerable public buildings into its most "
                           "reliable shelters within a generation."),
        "signature_solution": (
            "Step one, the assumptions: every school and hospital of a "
            "given era and structural type fails in similar ways, so "
            "retrofits can be standardized by archetype instead of "
            "custom-engineered per building. Step two, the reasoning "
            "path: the construction industry already productizes "
            "complexity - curtain walls, elevators, prefab bathrooms - "
            "so seismic retrofit can be productized the same way, as "
            "catalog kits per archetype. Step three, the proposed "
            "mechanism: a retrofit kit system - laser-scanned archetype "
            "libraries, pre-engineered steel-brace and damper modules "
            "sized from the scan, installed during summer breaks by "
            "certified crews following a fixed procedure, with "
            "fixed per-square-foot pricing published like a catalog. Step "
            "four, what would confirm it: three archetypes retrofitted "
            "across at least fifty buildings each, on schedule and on "
            "catalog price, with post-retrofit analysis showing "
            "life-safety performance in the design earthquake. Step five, "
            "what would kill it: if hidden conditions in old buildings "
            "defeat standardization and every job reverts to custom "
            "engineering, or if kit stiffness changes a building's "
            "dynamics in ways the archetype model missed. What this does "
            "not claim: it does not claim zero damage - the claim is "
            "life safety and continued operation, with repairable "
            "rather than catastrophic damage."),
        "sig_pointer": ("The Signature edition proposes catalog retrofit "
                        "kits per building archetype: laser-scanned "
                        "libraries, pre-engineered brace and damper "
                        "modules, fixed pricing, installed during school "
                        "breaks."),
        "citations": [CIT_QUAKE_SCHOOL],
    },
    {
        "key": "salt_free_winter_roads",
        "name": "Winter Roads Without Salt Damage",
        "group": "Urban Infrastructure",
        "ladder_rank": 6,
        "ladder_tier": "approachable",
        "problem": ("Road salt keeps winter traffic moving but poisons "
                    "waterways and eats bridges, cars, and pavements from "
                    "the inside. The problem is to keep winter roads safe "
                    "without the twenty-million-ton salt habit."),
        "background": ("Deicing salt - mostly sodium chloride - is spread "
                       "by the tens of millions of tons each winter across "
                       "northern roadways. It works, and it is cheap, but "
                       "chloride washes into streams and groundwater where "
                       "it persists essentially forever, and it drives the "
                       "corrosion that destroys bridge decks and "
                       "reinforcement. Alternatives exist - calcium "
                       "magnesium acetate, beet-juice blends that reduce "
                       "salt rates, brine pre-wetting that cuts total use - "
                       "but each costs more per storm than rock salt, and "
                       "no alternative matches salt's price at continental "
                       "scale. Corrosion inhibitors help steel but do "
                       "nothing for the environment. The result is a known "
                       "trade: safe winter roads today, corroded "
                       "infrastructure and salted watersheds tomorrow."),
        "why_it_matters": ("Ending the salt habit would add decades to the "
                           "life of every bridge and pavement in the snow "
                           "belt while letting freshwater ecosystems "
                           "recover. It is also the cheapest "
                           "corrosion-protection program ever proposed - "
                           "stop feeding the corrosion instead of fighting "
                           "it."),
        "signature_solution": (
            "Step one, the assumptions: salt is used by habit and price, "
            "not because alternatives cannot work - the unsolved part is "
            "matching salt's cost per safe lane-mile, storm after storm. "
            "Step two, the reasoning path: most salt is wasted - spread "
            "too early, bounced off the road, or applied to storms where "
            "less would do - so precision application can cut tonnage "
            "dramatically before any chemistry changes. Step three, the "
            "proposed mechanism: a precision winter-maintenance system - "
            "road-weather sensors every few kilometers feeding a "
            "storm model, spreader trucks with GPS rate control applying "
            "pre-wet brine only where the model says ice will form, and "
            "heated-pavement sections at the worst spots (bridges, steep "
            "grades) that eliminate salt locally. Step four, what would "
            "confirm it: a state-scale deployment showing equal or better "
            "crash rates with at least sixty percent less chloride "
            "applied per winter, audited by truck logs and stream "
            "monitoring. Step five, what would kill it: if sensor-model "
            "errors cause under-treatment and crash spikes in any "
            "storm class, or if heated sections cost more per "
            "lane-kilometer than the corrosion they prevent. What this "
            "does not claim: it does not claim zero chloride - the claim "
            "is dramatic reduction with equal safety, plus a path to "
            "phase out the remainder."),
        "sig_pointer": ("The Signature edition proposes precision winter "
                        "maintenance: sensor-driven storm models, GPS rate-"
                        "controlled brine, and heated pavement at the "
                        "worst spots to cut chloride use by most of it."),
        "citations": [CIT_SALT],
    },
    {
        "key": "century_water_mains",
        "name": "Century Water Mains",
        "group": "Urban Infrastructure",
        "ladder_rank": 7,
        "ladder_tier": "approachable",
        "problem": ("Buried water mains are breaking across the developed "
                    "world - a break every two minutes in the United "
                    "States - spilling treated drinking water into the "
                    "ground. The problem is to build and renew pipe "
                    "networks that reliably serve for a century."),
        "background": ("Much of the buried water network dates to the "
                       "postwar build-out: cast iron and early ductile iron "
                       "pipes with design lives around a century but real "
                       "lives cut short by corrosive soils, pressure "
                       "transients, and deferred maintenance. Utilities "
                       "lose an estimated six billion gallons of treated "
                       "water a day to leaks in the United States alone, "
                       "paying to treat water twice - once to make it, "
                       "once to clean up the street it floods. Replacement "
                       "is brutally expensive and disruptive, so utilities "
                       "run pipes to failure and patch the breaks. "
                       "Trenchless renewal - cured-in-place liners, pipe "
                       "bursting - helps, and acoustic and pressure "
                       "sensors can find leaks, but no utility has a "
                       "proven program that renews its whole network "
                       "ahead of failure at an affordable pace."),
        "why_it_matters": ("Water networks are the most capital-intensive "
                           "infrastructure cities own, and they are "
                           "invisible until they fail. A century-reliable "
                           "renewal method would end the break-patch "
                           "cycle, save the energy and chemicals wasted on "
                           "lost water, and keep streets from becoming "
                           "emergency excavations."),
        "signature_solution": (
            "Step one, the assumptions: utilities cannot afford to dig up "
            "every street, so century reliability must come from renewal "
            "without excavation plus knowing exactly which pipes are "
            "dying. Step two, the reasoning path: pressure transients "
            "(water hammer) do much of the killing, and they are "
            "measurable - a network that sees its own pressure spikes "
            "can calm them with surge control before they break old "
            "iron. Step three, the proposed mechanism: a "
            "renew-ahead-of-failure program - district metered areas with "
            "pressure logging on every main, transient-calming valves and "
            "pump controls to flatten spikes, and trenchless structural "
            "liners applied to mains flagged by the pressure history, "
            "all scheduled by a pipe-health model instead of by break "
            "reports. Step four, what would confirm it: a utility "
            "district showing break rates falling year over year for a "
            "decade while renewal spending stays flat, with water loss "
            "below ten percent. Step five, what would kill it: if liner "
            "longevity in real soils falls short of the century claim, "
            "or if pressure management cannot be retrofitted onto "
            "gravity-fed legacy zones. What this does not claim: it does "
            "not claim pipes that never age - the claim is a managed "
            "network where every main is renewed before it fails, "
            "indefinitely."),
        "sig_pointer": ("The Signature edition proposes renew-ahead-of-"
                        "failure water networks: pressure-transient "
                        "monitoring, surge calming, and trenchless liners "
                        "scheduled by pipe-health models instead of break "
                        "reports."),
        "citations": [CIT_ASCE21],
    },
    {
        "key": "sewer_tunnels_empires",
        "name": "Sewer Tunnels That Outlast Empires",
        "group": "Bridges and Tunnels",
        "ladder_rank": 8,
        "ladder_tier": "approachable",
        "problem": ("The great Victorian sewers still work after 150 "
                    "years, but modern sewer tunnels are designed for far "
                    "shorter lives and fail from corrosion, blockage, and "
                    "overload. The problem is to build new underground "
                    "waterways meant to serve for centuries."),
        "background": ("Sewer tunnels fail in slow, expensive ways: "
                       "hydrogen sulfide gas from sewage corrodes concrete "
                       "crowns, grit and fatbergs choke capacity, and "
                       "combined sewers overflow into rivers in every "
                       "heavy rain. London's Bazalgette interceptors, "
                       "completed in 1875, still carry the city's waste "
                       "because they were massively overbuilt in durable "
                       "materials - an approach modern value engineering "
                       "abandoned. Today's tunnels use thinner sections, "
                       "tighter budgets, and design lives of fifty to one "
                       "hundred years. Megaprojects like new interceptor "
                       "tunnels cost billions precisely because replacing "
                       "underground arteries under a living city is among "
                       "the hardest civil works there is."),
        "why_it_matters": ("A sewer tunnel is nearly impossible to replace "
                           "without tearing the city above it apart, so "
                           "its design life should be measured in "
                           "centuries by default. Century-plus tunnels "
                           "would also end the cycle of emergency "
                           "deep-tunnel megaprojects every generation."),
        "signature_solution": (
            "Step one, the assumptions: the Victorians were right about "
            "durability and wrong about capacity planning - the fix is "
            "their material generosity plus modern corrosion science. "
            "Step two, the reasoning path: crown corrosion from hydrogen "
            "sulfide is the dominant killer, and it is preventable - "
            "calcium-aluminate linings, antimicrobial admixtures, and "
            "ventilation that keeps gas concentrations below the "
            "corrosion threshold attack the actual mechanism. Step three, "
            "the proposed mechanism: a century-tunnel standard - "
            "sacrificial-thickness concrete sections sized for 250-year "
            "corrosion loss, corrosion-proof crown linings, "
            "self-cleansing gradients verified by sediment modeling, and "
            "inspection galleries that let robots survey the full bore "
            "without confined-space human entry. Step four, what would "
            "confirm it: corrosion-coupon arrays and gas monitoring in "
            "new tunnels showing loss rates consistent with multi-century "
            "life, plus robot inspection records with zero unplanned "
            "structural interventions over decades. Step five, what would "
            "kill it: if antimicrobial and lining systems degrade in "
            "real sewage chemistry faster than lab tests suggest, or if "
            "fatberg and grit accumulation defeat self-cleansing "
            "gradients. What this does not claim: it does not claim "
            "freedom from blockages or capacity upgrades - the claim is "
            "structural survival for centuries with maintainable "
            "interiors."),
        "sig_pointer": ("The Signature edition proposes a century-tunnel "
                        "standard: sacrificial-thickness sections, "
                        "corrosion-proof crowns, self-cleansing gradients, "
                        "and robot inspection galleries - Victorian "
                        "durability with modern corrosion science."),
        "citations": [CIT_BAZALGETTE],
    },
    {
        "key": "fireproof_timber_tower",
        "name": "The Fireproof Timber Megatower",
        "group": "Megastructures",
        "ladder_rank": 9,
        "ladder_tier": "approachable",
        "problem": ("Mass timber could make tall buildings carbon-storing "
                    "instead of carbon-emitting, but fire codes and "
                    "engineering caution cap how high wood can go. The "
                    "problem is to prove timber towers safe at heights "
                    "where only steel and concrete rule today."),
        "background": ("Engineered wood - cross-laminated timber and "
                       "glue-laminated beams - is strong, light, and locks "
                       "away carbon for the building's life. The tallest "
                       "timber buildings, Mjostarnet in Norway at 85.4 "
                       "meters and Ascent in Milwaukee at 86.6 meters, "
                       "show what is possible, yet most codes still treat "
                       "wood as a low-rise material. The core worry is "
                       "fire: timber chars at a predictable rate and the "
                       "char layer insulates the wood beneath, but "
                       "connections, concealed spaces, and the sheer fuel "
                       "load of a tall timber frame make fire engineers "
                       "nervous. Full-scale burn tests of timber "
                       "compartments have been encouraging, but the "
                       "profession lacks the decades of fire experience it "
                       "has with steel and concrete."),
        "why_it_matters": ("A proven fire-safe timber megatower would turn "
                           "the most carbon-intensive sector - tall "
                           "buildings - into a carbon sink, while making "
                           "construction faster, quieter, and lighter on "
                           "foundations. It is the single biggest "
                           "lever for decarbonizing the skyline."),
        "signature_solution": (
            "Step one, the assumptions: the char-rate predictability of "
            "heavy timber is an asset, not a risk - the unsolved part is "
            "connections and compartment behavior at scale, which must be "
            "proven by testing, not argued by calculation. Step two, the "
            "reasoning path: aviation certifies new airframes by "
            "full-scale testing to failure; tall timber needs the same "
            "certification culture - burn a full-scale tower section, "
            "measure everything, publish everything. Step three, the "
            "proposed mechanism: a certification protocol - full-scale "
            "multi-story burn tests of the exact connection and "
            "compartment system, non-combustible encapsulation of "
            "connections with verified char-plus-encapsulation ratings, "
            "and sprinkler-plus-detection redundancy sized for the fuel "
            "load - with the test data open to every code body. Step "
            "four, what would confirm it: a full-scale burn test where "
            "the structure survives the complete burnout of its worst "
            "compartment with residual capacity documented, and code "
            "adoption in at least three major jurisdictions. Step five, "
            "what would kill it: if connection failures in real fires "
            "outpace charring models, or if smoldering in concealed "
            "spaces proves uncontrollable. What this does not claim: it "
            "does not claim timber is fireproof - the claim is "
            "predictable, certifiable fire performance equal to "
            "conventional tall buildings."),
        "sig_pointer": ("The Signature edition proposes aviation-style "
                        "certification for tall timber: full-scale burn "
                        "tests of the exact connection system, "
                        "encapsulated connections, and open test data for "
                        "code bodies."),
        "citations": [CIT_TIMBER],
    },
    {
        "key": "cable_stayed_recabling",
        "name": "Cable-Stayed Bridges That Never Need Re-Cabling",
        "group": "Bridges and Tunnels",
        "ladder_rank": 10,
        "ladder_tier": "approachable",
        "problem": ("The elegant fan of cables on a cable-stayed bridge is "
                    "its most vulnerable part: stays corrode, fatigue, and "
                    "typically need replacement within decades. The problem "
                    "is to design stay-cable systems that last the full "
                    "life of the bridge."),
        "background": ("Stay cables carry the entire deck load to the "
                       "towers through high-strength steel strands inside "
                       "protective sheathing. In service they face a "
                       "brutal combination: millions of load cycles from "
                       "traffic and wind, rain and salt intrusion at "
                       "anchorages, and vibration that can fatigue wires. "
                       "Industry guidance expects major stay intervention "
                       "or full replacement within thirty to fifty years, "
                       "a massive operation that closes lanes, costs tens "
                       "of millions, and must be repeated. Engineers have "
                       "improved sheathing, added damping against "
                       "rain-wind vibration, and developed replaceable "
                       "strand systems, but the cable remains a consumable "
                       "with a shorter life than the concrete and steel "
                       "around it."),
        "why_it_matters": ("Stay replacement is the most expensive "
                           "maintenance a cable-stayed bridge will ever "
                           "face, and it arrives just as the bridge "
                           "enters its prime. Cables that truly last a "
                           "century would rewrite the economics of the "
                           "long-span bridges the world keeps building."),
        "signature_solution": (
            "Step one, the assumptions: cables die from the outside in - "
            "water intrusion and vibration - so a permanently dry, "
            "vibration-free cable cannot fail the way current ones do. "
            "Step two, the reasoning path: suspension-bridge main cables "
            "are dehumidified by dry-air injection and last far longer "
            "than stays; the fix is to give every stay the same "
            "treatment plus individual replaceability of strands. Step "
            "three, the proposed mechanism: a dry-cable stay system - "
            "each stay a sealed duct with continuous dry-air circulation "
            "and humidity sensors, internal damping against vibration, "
            "and individually replaceable strands so a single damaged "
            "strand is swapped like a light bulb instead of triggering "
            "whole-cable replacement. Step four, what would confirm it: "
            "instrumented stays on real bridges showing interior "
            "humidity at desert levels for a decade with zero wire "
            "breaks detected by acoustic monitoring. Step five, what "
            "would kill it: if duct seals cannot be maintained at "
            "anchorages under thermal cycling, or if dry air fails to "
            "protect already-microcracked wires. What this does not "
            "claim: it does not claim cables need no inspection - the "
            "claim is that inspection finds nothing to fix, and single "
            "strands are replaceable when it does."),
        "sig_pointer": ("The Signature edition proposes dry-cable stays: "
                        "sealed ducts with dry-air circulation and "
                        "humidity sensing, vibration damping, and "
                        "individually replaceable strands."),
        "citations": [CIT_CABLE],
    },
    {
        "key": "levee_never_breach",
        "name": "Levee Systems That Never Breach",
        "group": "Water and Flood",
        "ladder_rank": 11,
        "ladder_tier": "approachable",
        "problem": ("Levees are the walls between rivers and cities, and "
                    "they fail catastrophically - suddenly, completely, "
                    "and at the worst moment. The problem is to build "
                    "flood-defense systems that cannot breach the way "
                    "earthen levees do."),
        "background": ("Earthen levees fail by overtopping, seepage "
                       "piping beneath them, and slope instability - "
                       "failure modes that give little warning and "
                       "release the full river at once. The 2005 New "
                       "Orleans levee failures, investigated as "
                       "engineering failures of design and maintenance, "
                       "showed how a city's survival can rest on "
                       "structures whose true condition nobody knew. The "
                       "United States holds tens of thousands of miles of "
                       "levees, many built to unknown standards and "
                       "inspected rarely. Engineers have improved "
                       "design - cutoff walls against seepage, armored "
                       "overtopping sections, relief wells - but the "
                       "fundamental architecture remains a long earthen "
                       "wall whose weakest hundred meters determine the "
                       "fate of the city behind it."),
        "why_it_matters": ("A breach-proof flood defense would remove the "
                           "single most terrifying failure mode in "
                           "riverine cities. It would also end the "
                           "cruel arithmetic where protection level is "
                           "set by the worst-maintained reach of wall."),
        "signature_solution": (
            "Step one, the assumptions: the breach is the catastrophe, "
            "not the flood - a defense that fails gracefully by "
            "overtopping in a controlled, armored way cannot drown a "
            "city the way a breach does. Step two, the reasoning path: "
            "dams already use armored spillways that pass extreme flows "
            "without failing; levees need the same philosophy - design "
            "the overtop path, don't just hope it never happens. Step "
            "three, the proposed mechanism: a breach-proof levee "
            "section - deep cutoff wall against piping, clay core, and "
            "a fully armored crest and landside slope that turns "
            "overtopping into a controlled weir, plus fiber-optic "
            "seepage sensing along the entire alignment reporting the "
            "one precursor every breach shows: anomalous pore "
            "pressure. Step four, what would confirm it: full-scale "
            "overtopping tests on armored sections passing design-plus "
            "flows without erosion, and sensor networks catching "
            "seepage anomalies on real levees before any surface sign. "
            "Step five, what would kill it: if armoring costs make the "
            "system unaffordable at the thousands-of-miles scale, or "
            "if foundation conditions vary so much that no standard "
            "section works. What this does not claim: it does not claim "
            "no flooding - the claim is no breach: water may pass over "
            "in the extreme event, but the wall stands and the city "
            "drains afterward."),
        "sig_pointer": ("The Signature edition proposes breach-proof "
                        "levees: deep cutoff walls, fully armored "
                        "overtopping sections that fail gracefully like "
                        "spillways, and fiber-optic seepage sensing along "
                        "the whole alignment."),
        "citations": [CIT_USACE_LEVEE],
    },
    {
        "key": "two_hundred_year_bridge",
        "name": "The Two-Hundred-Year Bridge",
        "group": "Bridges and Tunnels",
        "ladder_rank": 12,
        "ladder_tier": "compounded",
        "problem": ("Bridges are designed for 75 to 100 years, then "
                    "replaced or rebuilt at enormous cost and disruption. "
                    "The problem is to design ordinary bridges for two "
                    "hundred years of service as the economical default."),
        "background": ("Modern bridge codes target design lives around "
                       "seventy-five years - a number chosen as much for "
                       "economic convention as for engineering. The result "
                       "is a replacement treadmill: bridges enter major "
                       "rehabilitation just as their financing is paid "
                       "off, and full replacement means years of "
                       "detours. Some owners already demand more - certain "
                       "Japanese bridges are designed for two hundred "
                       "years - proving it is possible when specified. "
                       "The barriers are economic analysis that discounts "
                       "the future to nothing, details that concentrate "
                       "durability risk (joints, bearings, drainage), and "
                       "a design culture that treats the bridge as a "
                       "product with a warranty rather than a civic "
                       "inheritance."),
        "why_it_matters": ("Two-hundred-year bridges would halve the "
                           "number of replacements each century, saving "
                           "vast sums and sparing cities repeated "
                           "construction trauma. More deeply, they would "
                           "restore the idea that infrastructure is built "
                           "for grandchildren, not for depreciation "
                           "schedules."),
        "signature_solution": (
            "Step one, the assumptions: the economics already favor "
            "long life at realistic discount rates - the barrier is "
            "detailing and institutional habit, not money. Step two, the "
            "reasoning path: bridges die at their details - expansion "
            "joints leak salt water onto everything below, bearings "
            "seize, drainage clogs - so a 200-year bridge is mostly a "
            "bridge with 200-year details. Step three, the proposed "
            "mechanism: a 200-year detailing standard - jointless or "
            "joint-minimized decks, integral abutments, replaceable "
            "bearing cartridges accessible without jacking the whole "
            "span, triple-redundant drainage, and durability-designed "
            "concrete covers - paired with life-cycle procurement that "
            "scores bids on 200-year present worth, forcing the "
            "economics to recognize longevity. Step four, what would "
            "confirm it: pilot bridges built to the standard with "
            "published life-cycle accounts, and inspection regimes "
            "showing detail condition on track for the 200-year "
            "projection at the fifty-year mark. Step five, what would "
            "kill it: if traffic growth renders the bridges "
            "functionally obsolete (too narrow, too weak) long before "
            "they wear out - durability without adaptability is a "
            "white elephant. What this does not claim: it does not "
            "claim bridges need no maintenance - the claim is that "
            "maintenance is planned component renewal, never structural "
            "replacement."),
        "sig_pointer": ("The Signature edition proposes a 200-year "
                        "detailing standard - jointless decks, integral "
                        "abutments, replaceable bearing cartridges - "
                        "plus life-cycle procurement that scores bids on "
                        "200-year present worth."),
        "citations": [CIT_ISO15686, CIT_ASCE21],
    },
    {
        "key": "century_concrete",
        "name": "Century Concrete That Outlives Its Builders",
        "group": "Foundations and Materials",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("Modern concrete structures are designed for decades; "
                    "Roman concrete structures have stood for millennia. "
                    "The problem is to make contemporary concrete reliably "
                    "serve for a century or more in real exposure."),
        "background": ("Reinforced concrete dominates construction, yet "
                       "its service life is limited by carbonation and "
                       "chloride ingress reaching the steel, by "
                       "alkali-silica reaction, and by freeze-thaw damage. "
                       "Design codes typically assume fifty to seventy-five "
                       "years. Meanwhile the Pantheon's unreinforced "
                       "concrete dome, completed around 125 AD, still "
                       "stands, and Roman marine concrete actually grows "
                       "stronger over centuries as rare minerals "
                       "crystallize in its pores. Modern ultra-high-"
                       "performance concretes achieve remarkable density "
                       "and durability in the lab, but they are expensive, "
                       "tricky to place, and lack the century of field "
                       "history that would let engineers trust them with "
                       "a century-long promise."),
        "why_it_matters": ("Concrete is the most consumed material on "
                           "Earth after water; doubling its service life "
                           "halves the demolition waste, the cement "
                           "carbon, and the reconstruction cost of the "
                           "built world. Century concrete would also let "
                           "engineers promise what the Romans delivered: "
                           "structures that outlive their builders."),
        "signature_solution": (
            "Step one, the assumptions: the Romans prove the chemistry "
            "exists - the gap is translating two-thousand-year "
            "durability into modern reinforced construction with modern "
            "schedules. Step two, the reasoning path: durability is "
            "mostly about transport - how fast water, chlorides, and "
            "carbon dioxide move through the concrete - so the century "
            "recipe is a transport recipe: ultra-low permeability plus "
            "self-sealing chemistry. Step three, the proposed mechanism: "
            "a century-concrete specification - pozzolanic blends modeled "
            "on Roman chemistry for long-term strength gain, "
            "crystalline admixtures that seal micro-cracks as they form, "
            "covers sized from measured diffusion rates for the actual "
            "exposure, and non-corroding reinforcement in the outer "
            "zone so the transport battle has a backstop. Step four, "
            "what would confirm it: accelerated aging calibrated against "
            "Roman samples and fifty-year field concretes, plus "
            "instrumented structures showing ingress rates on the "
            "century trajectory at year twenty. Step five, what would "
            "kill it: if the admixture chemistry interferes with "
            "long-term strength gain, or if real construction "
            "variability (curing, compaction) defeats lab-grade "
            "permeability. What this does not claim: it does not claim "
            "Roman concrete for everything - the claim is a "
            "specification and verification regime that makes century "
            "service the engineered outcome, not the lucky one."),
        "sig_pointer": ("The Signature edition proposes a century-"
                        "concrete specification: Roman-inspired pozzolanic "
                        "chemistry, self-sealing admixtures, "
                        "diffusion-sized covers, and non-corroding outer-"
                        "zone reinforcement."),
        "citations": [CIT_PANTHEON, CIT_ISO15686],
    },
    {
        "key": "self_healing_pavement_networks",
        "name": "Self-Healing Pavement Networks",
        "group": "Urban Infrastructure",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("Roads are inspected by eye and repaired after they "
                    "fail. The problem is to build pavement networks that "
                    "continuously sense their own cracking and heal it "
                    "before any pothole or rut appears."),
        "background": ("Pavement management today is reactive: crews "
                       "patch what drivers complain about, and resurfacing "
                       "schedules are set by age and visual surveys. "
                       "Meanwhile the technologies for a different model "
                       "exist in pieces - self-healing asphalt that "
                       "re-melts under induction heating, demonstrated on "
                       "Dutch highways; embedded strain and temperature "
                       "sensors; robotic crack-sealing machines. What "
                       "does not exist is the integrated system: a road "
                       "network that maps its own micro-cracking in real "
                       "time, dispatches healing - heat, rejuvenator, "
                       "robotic sealant - to the exact locations, and "
                       "verifies the repair, all as routine operations. "
                       "The gap is systems engineering and economics, not "
                       "materials."),
        "why_it_matters": ("A self-healing network would end the "
                           "patch-and-repatch economy of road maintenance "
                           "and multiply pavement life at a fraction of "
                           "reconstruction cost. It is also the proof of "
                           "concept for the self-maintaining city: "
                           "infrastructure as a living system, not a "
                           "decaying asset."),
        "signature_solution": (
            "Step one, the assumptions: healing only works if cracks are "
            "found early - the system is an inspection system first and "
            "a healing system second. Step two, the reasoning path: "
            "municipal vehicles already drive every street daily - "
            "buses, sweepers, garbage trucks - so the sensor network "
            "rides on the existing fleet instead of requiring new "
            "infrastructure. Step three, the proposed mechanism: a "
            "closed-loop pavement network - fleet vehicles carrying "
            "ground-penetrating radar and acoustic sensors that map "
            "subsurface cracking nightly, a central model that prioritizes "
            "healing tickets, induction-heater and robotic-sealant "
            "trucks that work the tickets before dawn, and "
            "post-treatment scans that verify each heal. Step four, "
            "what would confirm it: a city district where measured crack "
            "density stays flat year over year with healing cost per "
            "lane-kilometer below the district's historical patching "
            "budget. Step five, what would kill it: if sensor false "
            "positives send healing trucks chasing noise, or if healing "
            "energy and truck time exceed patching costs at network "
            "scale. What this does not claim: it does not claim roads "
            "that never need resurfacing - the claim is that the "
            "surface never reaches the failure state that forces "
            "emergency repair."),
        "sig_pointer": ("The Signature edition proposes closed-loop "
                        "pavement networks: fleet-mounted sensors mapping "
                        "cracks nightly, induction-heater and robotic "
                        "trucks healing tickets before dawn, verified by "
                        "post-treatment scans."),
        "citations": [CIT_DELFT_ASPHALT, CIT_AAA],
    },
    {
        "key": "skyscraper_sway",
        "name": "Skyscrapers That Sway but Never Fall",
        "group": "Megastructures",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("Tall buildings must move in wind and earthquakes - "
                    "a rigid skyscraper would snap - but occupants "
                    "panic at the motion and equipment fails. The problem "
                    "is to let supertalls sway safely while keeping the "
                    "people inside comfortable and the building "
                    "undamaged."),
        "background": ("Every tall building is a giant inverted pendulum "
                       "with a natural sway period of several seconds. "
                       "Wind pushes it into oscillation; earthquakes shake "
                       "its base. Engineers answer with damping: tuned "
                       "mass dampers like Taipei 101's 660-tonne steel "
                       "ball, tuned liquid dampers, viscous dampers in "
                       "outriggers, and aerodynamic shaping that spoils "
                       "the vortices wind sheds off the tower. "
                       "Performance-based design now targets not just "
                       "survival but continued occupancy after the big "
                       "event. Yet damper systems are tuned to models "
                       "that may not match the as-built tower, occupant "
                       "comfort criteria are still crude, and no tower "
                       "has yet ridden out a truly great earthquake at "
                       "close range to validate the designs."),
        "why_it_matters": ("Cities keep building taller on shakier "
                           "ground; the margin between a tower that "
                           "sways and recovers and one that does not is "
                           "the difference between a skyline and a "
                           "graveyard. Comfort matters too - a tower "
                           "people fear is a failed building even if it "
                           "stands."),
        "signature_solution": (
            "Step one, the assumptions: the building's true dynamic "
            "properties differ from the design model, so damping must "
            "adapt to the measured tower, not the modeled one. Step two, "
            "the reasoning path: active and semi-active control - "
            "dampers whose properties change in real time - can track "
            "the real building, but they need power and fail-safe "
            "behavior; the answer is hybrid systems that are excellent "
            "passive dampers and better active ones. Step three, the "
            "proposed mechanism: an adaptive sway system - dense "
            "accelerometer arrays that continuously identify the "
            "tower's real modes, semi-active dampers that retune "
            "themselves to those modes, and aerodynamic "
            "outrigger screens whose porosity adjusts with wind "
            "direction, all defaulting to a safe passive state on "
            "power loss. Step four, what would confirm it: a tower "
            "where measured accelerations in design wind and moderate "
            "quakes stay within comfort and damage thresholds with the "
            "adaptive system demonstrably outperforming its passive "
            "baseline. Step five, what would kill it: if semi-active "
            "components prove unreliable over decades of standby, or "
            "if the control system ever drives the tower instead of "
            "damping it. What this does not claim: it does not claim "
            "motionless towers - the claim is motion kept within "
            "human comfort and zero-damage limits, in wind and in "
            "quakes."),
        "sig_pointer": ("The Signature edition proposes adaptive sway "
                        "control: accelerometer arrays identifying the "
                        "tower's real modes, self-retuning semi-active "
                        "dampers, and adjustable aerodynamic screens - "
                        "fail-safe to passive."),
        "citations": [CIT_TAIPEI, CIT_BURJ],
    },
    {
        "key": "big_one_megastructures",
        "name": "Megastructures That Survive the Big One",
        "group": "Seismic Design",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("Subduction zones like Cascadia and Nankai will one "
                    "day produce magnitude-9 earthquakes beneath major "
                    "cities full of tall buildings, long bridges, and "
                    "critical facilities. The problem is to design "
                    "megastructures that survive the largest physically "
                    "possible shaking, not just the code earthquake."),
        "background": ("Seismic codes design for a probabilistic "
                       "earthquake - typically the shaking with a ten "
                       "percent chance in fifty years - and accept damage "
                       "in rarer events. But subduction megathrusts "
                       "produce shaking far beyond that: minutes of "
                       "long-period motion that resonates with tall "
                       "buildings and long bridges, as the 2011 Tohoku "
                       "quake demonstrated at Tokyo's towers. Tokyo "
                       "Skytree's independent central column shows the "
                       "kind of thinking required. The unsolved problem "
                       "is designing for the deterministic maximum - the "
                       "biggest quake the fault can physically produce - "
                       "while keeping buildings buildable and affordable, "
                       "and proving the design against ground motions no "
                       "instrument has ever recorded at that site."),
        "why_it_matters": ("When the big one comes to a subduction-zone "
                           "city, the survival of its towers, bridges, "
                           "and hospitals determines whether the "
                           "disaster is recoverable or civilizational. "
                           "Designing for the maximum credible event is "
                           "the only honest standard for structures "
                           "meant to stand for a century on a restless "
                           "fault."),
        "signature_solution": (
            "Step one, the assumptions: the maximum credible earthquake "
            "is knowable from fault physics even where it has never "
            "been recorded - the design target is deterministic, not "
            "probabilistic. Step two, the reasoning path: long-period "
            "shaking is the killer of megastructures, and it is best "
            "defeated by keeping the structure's period away from the "
            "ground's - base isolation plus supplemental damping does "
            "exactly this, as proven in instrumented buildings. Step "
            "three, the proposed mechanism: a maximum-credible design "
            "standard - site-specific fault-physics ground motions, "
            "triple-pendulum isolation bearings with displacement "
            "capacity for the worst case, distributed damping tuned to "
            "the isolated period, and structural fuses - replaceable "
            "yielding elements - that concentrate any damage where it "
            "can be inspected and swapped. Step four, what would "
            "confirm it: full-scale bearing and fuse testing to "
            "maximum-credible displacements, and instrumented isolated "
            "buildings riding out the next large subduction event with "
            "measured performance matching prediction. Step five, what "
            "would kill it: if fault-physics models underestimate "
            "long-period energy, or if isolation displacements in the "
            "true maximum exceed any buildable bearing. What this does "
            "not claim: it does not claim undamaged buildings - the "
            "claim is survival with repairable, localized damage and "
            "no collapse, in the largest quake the fault can make."),
        "sig_pointer": ("The Signature edition proposes maximum-credible "
                        "design: fault-physics ground motions, "
                        "triple-pendulum isolation, distributed damping, "
                        "and replaceable structural fuses."),
        "citations": [CIT_SKYTREE, CIT_JAPAN_TSUNAMI],
    },
    {
        "key": "block_isolation",
        "name": "Base Isolation for Entire City Blocks",
        "group": "Seismic Design",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("Base isolation works beautifully for single "
                    "important buildings, but cities are blocks of "
                    "ordinary buildings on shared streets and utilities. "
                    "The problem is to isolate whole city blocks - "
                    "buildings, streets, and lifelines together."),
        "background": ("Base isolation decouples a building from ground "
                       "motion with flexible bearings, letting the earth "
                       "move beneath a nearly still structure - San "
                       "Francisco's City Hall retrofit is a famous "
                       "success. But isolating one building while its "
                       "neighbors pound against it, while streets buckle "
                       "and pipes shear at the property line, limits the "
                       "benefit. Researchers have proposed isolating "
                       "entire blocks on a shared isolation plane, with "
                       "flexible utility connections bridging the moat, "
                       "but no city has built one. The challenges are "
                       "formidable: the isolation gap around a whole "
                       "block, differential movement between isolated and "
                       "non-isolated surroundings, and the sheer cost of "
                       "retrofitting an occupied block."),
        "why_it_matters": ("Block-scale isolation would protect not just "
                           "landmark buildings but the ordinary fabric - "
                           "apartments, shops, clinics - and keep "
                           "streets and utilities functional after the "
                           "quake. It converts seismic safety from a "
                           "luxury of important buildings into a property "
                           "of neighborhoods."),
        "signature_solution": (
            "Step one, the assumptions: new construction is the viable "
            "entry point - retrofitting occupied blocks is a second-"
            "generation problem; prove it on new districts first. Step "
            "two, the reasoning path: the hard parts are the edges - "
            "the moat, the utilities, the streets - so the design "
            "standardizes the edge the way building codes standardized "
            "the fire wall. Step three, the proposed mechanism: an "
            "isolated-block standard - the block's buildings founded on "
            "a shared stiff mat over isolation bearings, a perimeter "
            "moat with sacrificial crushable covers, utility corridors "
            "crossing on flexible loops with automatic shutoffs, and "
            "streets built as articulated segments that tolerate the "
            "design displacement. Step four, what would confirm it: a "
            "pilot district - even a few blocks - built to the standard "
            "and instrumented, showing in the next moderate quake that "
            "the block moves as designed with utilities intact. Step "
            "five, what would kill it: if moat maintenance (debris, "
            "water, unauthorized fill) defeats the isolation in "
            "practice, or if costs exceed premium-building isolation "
            "by multiples. What this does not claim: it does not claim "
            "protection for the surrounding unimproved city - the claim "
            "is a neighborhood that stays standing and functioning "
                           "while the ground moves beneath it."),
        "sig_pointer": ("The Signature edition proposes an isolated-block "
                        "standard: shared isolation mat, perimeter moat "
                        "with crushable covers, flexible utility loops, "
                        "and articulated streets - proven on new "
                        "districts first."),
        "citations": [CIT_QUAKE_SCHOOL],
    },
    {
        "key": "floating_foundations",
        "name": "Floating Foundations for Flood Cities",
        "group": "Foundations and Materials",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("In flood-prone and subsiding cities, conventional "
                    "foundations are either drowned or left hanging as "
                    "the ground sinks. The problem is to found buildings "
                    "so they stay level and usable whether the ground is "
                    "dry, flooded, or sinking."),
        "background": ("Foundations assume stable ground, but in delta "
                       "cities the ground is anything but: floods rise "
                       "meters deep, soft soils consolidate under load, "
                       "and groundwater pumping drops the land itself. "
                       "Piles can reach firm strata but leave buildings "
                       "stranded above sinking streets; rafts settle with "
                       "the ground until services shear. Amphibious "
                       "foundations - buoyant structures that rest on the "
                       "ground normally and float during floods - have "
                       "been demonstrated in the Netherlands, and floating "
                       "districts are rising in Amsterdam's IJburg and "
                       "the Maldives floating-city project. But these "
                       "remain special projects; there is no standard "
                       "foundation system a flood-city builder orders the "
                       "way they order piles."),
        "why_it_matters": ("A standard floating or flood-adaptive "
                           "foundation would let flood-plain cities build "
                           "with confidence instead of dread, and let "
                           "sinking cities keep their buildings level as "
                           "the land drops. It turns the foundation from "
                           "a bet on stable ground into an instrument "
                           "that accommodates the ground's moods."),
        "signature_solution": (
            "Step one, the assumptions: the foundation must handle three "
            "regimes - dry, flooded, and subsiding - with one mechanism, "
            "because flood cities experience all three. Step two, the "
            "reasoning path: buoyancy handles flooding, and adjustable "
            "supports handle subsidence - combine a buoyant base with "
            "screw-jack leveling and one foundation serves all regimes. "
            "Step three, the proposed mechanism: an adaptive foundation "
            "unit - a watertight buoyant basement-box that floats the "
            "building during floods on guideposts, fitted with "
            "instrumented screw jacks that re-level the building as "
            "surveyed settlement accumulates, with flexible service "
            "connections throughout. Step four, what would confirm it: "
            "instrumented buildings over a decade showing level "
            "tolerances maintained through flood events and measured "
            "subsidence, with re-leveling operations logged and costed. "
            "Step five, what would kill it: if buoyant boxes leak or "
            "corrode in real groundwater chemistry, or if differential "
            "settlement across a large footprint exceeds jack travel. "
            "What this does not claim: it does not claim immunity to "
            "extreme scour or liquefaction - the claim is a foundation "
            "that stays level and dry through floods and gradual "
            "subsidence."),
        "sig_pointer": ("The Signature edition proposes adaptive "
                        "foundation units: buoyant basement-boxes on "
                        "guideposts for floods, instrumented screw jacks "
                        "for subsidence - one system for dry, flooded, "
                        "and sinking ground."),
        "citations": [CIT_AMPHIBIOUS, CIT_OCEANIX],
    },
    {
        "key": "storm_surge_megacities",
        "name": "Storm-Surge-Proof Coastal Megacities",
        "group": "Coastal Cities",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("Sea-level rise and stronger storms are sending "
                    "surges deeper into coastal megacities whose barriers "
                    "were designed for a milder century. The problem is "
                    "to protect cities of ten million people against the "
                    "surge of the coming century, not the last one."),
        "background": ("Storm surge barriers are among the great civil "
                       "works: the Thames Barrier has guarded London since "
                       "1982, the Maeslantkering since 1997, and Venice's "
                       "MOSE since 2020. But each was designed around "
                       "historical storm statistics, and sea-level rise "
                       "steadily eats their safety margin while "
                       "urbanization puts more value behind them. "
                       "Proposals for New York, Shanghai, and other "
                       "megacities run into staggering costs, shipping "
                       "lanes that cannot be blocked, and the reality that "
                       "a barrier protects against surge while rainfall "
                       "flooding and rising groundwater attack from "
                       "behind. No coastal megacity has a complete, "
                       "funded, built defense against the 2100 surge."),
        "why_it_matters": ("The world's great coastal cities hold "
                           "trillions in value and hundreds of millions "
                           "of people in the surge zone. A proven "
                           "megacity-scale defense - barrier plus "
                           "drainage plus elevated critical systems - is "
                           "the difference between adaptation and "
                           "abandonment."),
        "signature_solution": (
            "Step one, the assumptions: no single barrier suffices - the "
            "defense must be a system of barriers, and the system must "
            "be designed for the 2100 sea level with upgrade paths, not "
            "for today's. Step two, the reasoning path: the Dutch "
            "layered approach - dunes, barriers, compartmentalization - "
            "is the only proven philosophy; scale it to megacities with "
            "hard engineering where the Dutch use sand. Step three, the "
            "proposed mechanism: a megacity surge-defense system - outer "
            "storm-surge barriers at harbor mouths designed for "
            "upgradeable crest heights, inner compartment dikes that "
            "limit any breach's damage zone, raised and flood-proofed "
            "critical infrastructure (power, hospitals, transit), and a "
            "real-time surge forecast and barrier-operation protocol "
            "drilled like a military exercise. Step four, what would "
            "confirm it: a full system test - barriers closed on "
            "forecast, compartments verified, city functioning - during "
            "a real major storm with damage confined to design "
            "expectations. Step five, what would kill it: if "
            "pluvial flooding behind the barriers overwhelms the "
            "interior drainage in the design storm, or if political "
            "cycles cannot sustain the century-long funding the system "
            "needs. What this does not claim: it does not claim dry "
            "streets in the worst storm - the claim is no catastrophic "
            "inundation, protected critical systems, and a city that "
            "reopens in days."),
        "sig_pointer": ("The Signature edition proposes layered megacity "
                        "surge defense: upgradeable outer barriers, inner "
                        "compartment dikes, flood-proofed critical "
                        "systems, and drilled barrier-operation "
                        "protocols."),
        "citations": [CIT_DELTA],
    },
    {
        "key": "submerged_floating_tunnel",
        "name": "Submerged Floating Tunnels",
        "group": "Bridges and Tunnels",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("Some fjords and straits are too deep for bridges and "
                    "too wide for bored tunnels. The problem is to build "
                    "submerged floating tunnels - tubes suspended in the "
                    "water column - that carry traffic safely for a "
                    "century."),
        "background": ("A submerged floating tunnel, or Archimedes "
                       "bridge, hangs in the water held by buoyancy and "
                       "tethers: positively buoyant tubes anchored down, "
                       "or negatively buoyant tubes hung from pontoons. "
                       "Norway's E39 program has studied the concept "
                       "seriously for fjord crossings like the "
                       "Bjornafjorden, where depths near a kilometer and "
                       "widths of several kilometers defeat both "
                       "conventional bridges and bored tunnels. The "
                       "physics is understood - offshore platforms live "
                       "by the same principles - but no traffic-carrying "
                       "submerged floating tunnel has ever been built. "
                       "The open questions are brutal: century-long "
                       "tether fatigue, ship collision and anchor drag, "
                       "fire and evacuation inside a tube with water on "
                       "all sides, and construction tolerances for "
                       "joining segments in open water."),
        "why_it_matters": ("The concept would unlock crossings the world "
                           "has written off - deep fjords, wide straits - "
                           "at a fraction of the cost of the alternatives, "
                           "and prove a whole new structural family. It "
                           "is the bridge type for the deep-water "
                           "century."),
        "signature_solution": (
            "Step one, the assumptions: the tunnel is an offshore "
            "structure that happens to carry cars - design it to "
            "offshore standards (redundancy, inspection, damage "
            "tolerance), not just bridge standards. Step two, the "
            "reasoning path: the tethers are the life-safety system, so "
            "they get the aerospace treatment - redundant load paths, "
            "continuous tension monitoring, and replaceability without "
            "closing the tunnel. Step three, the proposed mechanism: a "
            "tether-redundant floating tunnel - twin tubes (one per "
            "direction, each an evacuation refuge for the other), "
            "tether groups with monitored tension and sacrificial "
            "outer wires, ship-impact protection zones at the portals, "
            "and segment joints proven in a full-scale prototype "
            "section tested through storm loading. Step four, what "
            "would confirm it: a full-scale prototype tube-tether "
            "system surviving extreme storm and simulated tether-loss "
            "cases with measured motions inside traffic-comfort "
            "limits. Step five, what would kill it: if tether fatigue "
            "in real sea states outpaces inspection and replacement, "
            "or if evacuation modeling shows unacceptable risk in a "
            "tube fire. What this does not claim: it does not claim "
            "the first one will be cheap - the claim is a proven, "
            "certifiable structural system that makes the second one "
            "routine."),
        "sig_pointer": ("The Signature edition proposes treating the "
                        "floating tunnel as an offshore structure: "
                        "twin tubes, redundant monitored tethers with "
                        "replaceable wires, and full-scale prototype "
                        "validation."),
        "citations": [CIT_NORWAY_TUNNEL],
    },
    {
        "key": "underground_freight",
        "name": "Underground Freight Networks",
        "group": "Underground Cities",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("Trucks choke cities with congestion, pollution, and "
                    "crashed bridges, while the goods still have to move. "
                    "The problem is to move urban freight underground on "
                    "automated networks, taking trucks off the streets."),
        "background": ("Urban freight is the fastest-growing traffic: "
                       "e-commerce vans double-park on every block while "
                       "heavy trucks grind through tunnels and over "
                       "bridges never designed for them. Cities have "
                       "dreamed of freight tubes for a century - London's "
                       "Mail Rail carried post underground from 1927 to "
                       "2003 - and Switzerland is planning Cargo Sous "
                       "Terrain, a roughly 500-kilometer automated "
                       "underground freight network. The engineering is "
                       "straightforward tunneling; the unsolved parts are "
                       "economic - the cost per kilometer against truck "
                       "rates - and logistical: the last hundred meters "
                       "from tunnel portal to shop door still needs "
                       "vehicles, and automated loading at thousands of "
                       "endpoints is its own industry to invent."),
        "why_it_matters": ("Underground freight would give cities back "
                           "their streets: less congestion, cleaner air, "
                           "quieter nights, and bridges that stop being "
                           "pounded by overweight trucks. It decouples "
                           "the movement of goods from the quality of "
                           "urban life."),
        "signature_solution": (
            "Step one, the assumptions: the network wins on the trunk, "
            "not the last meter - standardize the container and the "
            "handoff, and let electric vans handle only the final "
            "leg. Step two, the reasoning path: the economics work "
            "where trucks are most expensive - dense cities with "
            "congested streets and strict emission zones - so build "
            "there first and let the network earn its expansion. Step "
            "three, the proposed mechanism: a freight-metro standard - "
            "small-diameter automated tunnels on fixed trunk routes, "
            "standardized pallets that transfer from truck to tunnel "
            "shuttle at edge-of-city terminals, and underground "
            "distribution hubs beneath commercial districts with "
            "elevator handoffs to buildings. Step four, what would "
            "confirm it: a first trunk line carrying contracted freight "
            "volumes at per-pallet cost below truck rates on the same "
            "corridor, with measured street-truck reductions. Step five, "
            "what would kill it: if tunneling costs in real urban "
            "ground exceed the business case, or if shippers refuse the "
            "standard pallet and the network starves for volume. What "
            "this does not claim: it does not claim the end of delivery "
            "vans - the claim is trunk freight underground and only "
            "the last leg on the surface."),
        "sig_pointer": ("The Signature edition proposes a freight-metro "
                        "standard: automated small-diameter trunk "
                        "tunnels, standardized pallets, edge-of-city "
                        "terminals, and underground district hubs."),
        "citations": [CIT_CST],
    },
    {
        "key": "deep_underground_city",
        "name": "Deep Underground Cities for Everyday Life",
        "group": "Underground Cities",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("Cities keep sprawling outward while the space "
                    "beneath them - thermally stable, disaster-sheltered, "
                    "close to everything - goes unused. The problem is to "
                    "make underground urban space genuinely livable: "
                    "daylit, ventilated, and desirable, not merely "
                    "tolerable."),
        "background": ("The underground city already exists in fragments: "
                       "Montreal's 33-kilometer RESO network, Helsinki's "
                       "legally binding underground master plan, and "
                       "underground shopping, transit, and industry "
                       "worldwide. Deep space offers constant "
                       "temperatures, immunity to weather and surface "
                       "disasters, and zero land consumption. But "
                       "underground living fights human psychology - the "
                       "need for daylight, views, and orientation - plus "
                       "hard engineering: ventilation for thousands, fire "
                       "and evacuation safety, groundwater control, and "
                       "the cost of excavation. Ancient Derinkuyu proves "
                       "humans can live deep for generations; modern "
                       "engineering has not yet made it pleasant."),
        "why_it_matters": ("Livable underground space would let cities "
                           "grow without sprawl, shelter populations from "
                           "extreme heat and storms, and free the surface "
                           "for parks and people. In a century of climate "
                           "stress, the third dimension of the city may "
                           "matter as much as the first two."),
        "signature_solution": (
            "Step one, the assumptions: psychology is the governing "
            "constraint - engineering can already build the box; the "
            "unsolved part is making people want to be in it. Step two, "
            "the reasoning path: daylight and orientation are solvable "
            "with light wells, fiber-optic daylighting, and generous "
            "volumes - the failures of underground space are failures "
            "of stinginess, not physics. Step three, the proposed "
            "mechanism: a livability standard for deep urban space - "
            "daylight-equivalent illumination with circadian spectrum "
            "control, minimum volume and ceiling heights that defeat "
            "the bunker feeling, redundant ventilation and smoke "
            "control proven by full-scale fire tests, and direct "
            "daylight connections (atriums, light courts) at regular "
            "intervals - certified like a building code. Step four, "
            "what would confirm it: a pilot underground district where "
            "occupancy, rents, and self-reported wellbeing match "
            "comparable surface space over five years. Step five, what "
            "would kill it: if no illumination technology satisfies "
            "the human need for real sky, or if fire-evacuation "
            "modeling cannot clear deep occupancies in time. What this "
            "does not claim: it does not claim underground is better "
            "than surface - the claim is underground space as good as "
            "surface space, doubling the usable city."),
        "sig_pointer": ("The Signature edition proposes a livability "
                        "standard for deep space: circadian daylighting, "
                        "generous volumes, proven smoke control, and "
                        "regular daylight connections - certified like a "
                        "code."),
        "citations": [CIT_MONTREAL, CIT_HELSINKI, CIT_DERINKUYU],
    },
    {
        "key": "self_healing_dam_faces",
        "name": "Self-Healing Dam Faces",
        "group": "Water and Flood",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("Tens of thousands of aging dams face deterioration "
                    "of their concrete faces - cracking, freeze-thaw, "
                    "alkali-silica reaction - while inspection still "
                    "depends on divers and dewatering. The problem is to "
                    "make dam faces that monitor and repair themselves "
                    "underwater."),
        "background": ("The United States inventory lists more than "
                       "ninety thousand dams with an average age above "
                       "sixty years, and the 2017 Oroville spillway "
                       "crisis showed how fast a concrete water structure "
                       "can go from fine to emergency. Dam faces suffer "
                       "relentlessly: wet-dry cycling, ice, chemical "
                       "attack, and the slow swelling of alkali-silica "
                       "reaction. Inspection is the bottleneck - vast "
                       "submerged surfaces checked by divers or by "
                       "draining, both expensive and infrequent. Repair "
                       "means dewatering or underwater work at "
                       "extraordinary cost. The dam safety community "
                       "knows exactly what is wrong with its structures; "
                       "it lacks the means to watch and fix them "
                       "continuously."),
        "why_it_matters": ("Dam failures kill people and erase towns; "
                           "slow deterioration is the quiet path to the "
                           "same outcome. Self-monitoring, self-repairing "
                           "dam faces would convert dam safety from "
                           "periodic anxiety into continuous assurance."),
        "signature_solution": (
            "Step one, the assumptions: you cannot dewater a reservoir "
            "every time concrete cracks - the repair must come to the "
            "dam, underwater, autonomously. Step two, the reasoning "
            "path: the offshore industry already inspects and repairs "
            "structures underwater with robots; dams need the civil "
            "version of that capability, plus materials that cooperate "
            "with it. Step three, the proposed mechanism: a "
            "self-caring dam face - permanent robotic crawler garages "
            "on the dam, crawlers that map cracking with ultrasound "
            "and apply sealant or cathodic patches underwater, "
            "self-sealing concrete in new facings, and alkali-silica "
            "mitigation by lithium treatment where the chemistry "
            "allows. Step four, what would confirm it: a dam where "
            "crawler surveys show crack growth arrested after "
            "treatment, with intervention costs per square meter "
            "documented below dewatering-based repair. Step five, what "
            "would kill it: if underwater sealants debond in real "
            "reservoir conditions, or if crawlers cannot operate in "
            "the currents and silt of real spillways. What this does "
            "not claim: it does not claim dams that never age - the "
            "claim is faces whose deterioration is continuously found "
            "and arrested before it threatens the structure."),
        "sig_pointer": ("The Signature edition proposes self-caring dam "
                        "faces: resident robotic crawlers mapping and "
                        "sealing cracks underwater, self-sealing "
                        "concrete, and alkali-silica mitigation."),
        "citations": [CIT_OROVILLE],
    },
    {
        "key": "permafrost_cities",
        "name": "Cities on Thawing Permafrost",
        "group": "Foundations and Materials",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "problem": ("Arctic cities and infrastructure were built on ground "
                    "assumed permanently frozen; the ground is thawing. "
                    "The problem is to keep buildings, pipelines, and "
                    "roads standing as permafrost degrades beneath them."),
        "background": ("Permafrost underlies vast inhabited regions, and "
                       "structures there were founded on its strength: "
                       "piles frozen into the ground, buildings elevated "
                       "to keep heat from the soil, thermosyphons - "
                       "passive heat pipes - keeping foundations frozen, "
                       "as on the Trans-Alaska Pipeline. Warming thaws "
                       "the ice that holds the soil together, and the "
                       "ground settles, heaves, and flows. Across the "
                       "Arctic, buildings tilt, roads buckle, and "
                       "pipelines strain; the IPCC documents accelerating "
                       "thaw. Adaptation exists - adjustable foundations, "
                       "deeper piles, active cooling - but it is "
                       "piecemeal, expensive, and always catching up to "
                       "thaw that outpaces projections."),
        "why_it_matters": ("Hundreds of Arctic communities and critical "
                           "energy and transport infrastructure stand on "
                           "thawing ground. Solving the foundation "
                           "problem is the precondition for the Arctic "
                           "remaining inhabited and for its infrastructure "
                           "remaining safe."),
        "signature_solution": (
            "Step one, the assumptions: in many places refreezing the "
            "ground is no longer possible - the design must assume "
            "thawing ground and found accordingly. Step two, the "
            "reasoning path: the two viable strategies are keeping heat "
            "out (where permafrost can still be preserved) and "
            "designing for settlement (where it cannot) - the "
            "engineering choice must be made per site by measurement, "
            "not by hope. Step three, the proposed mechanism: a "
            "permafrost-foundation protocol - ground-temperature "
            "monitoring at every structure, thermosyphon and shading "
            "systems where the thermal model shows preservation is "
            "possible, and where it is not, adjustable pile foundations "
            "with jacking points and settlement-tolerant utility "
            "connections, re-leveled on a surveyed schedule. Step four, "
            "what would confirm it: instrumented Arctic buildings "
            "maintaining serviceability through a decade of measured "
            "thaw, with re-leveling costs tracked against the "
            "do-nothing failure cost. Step five, what would kill it: "
            "if thaw settlement proves too rapid and differential for "
            "any jacking regime, or if thermosyphons cannot hold the "
            "line as air temperatures keep rising. What this does not "
            "claim: it does not claim to stop permafrost thaw - the "
            "claim is structures that remain safe and usable while the "
            "ground changes beneath them."),
        "sig_pointer": ("The Signature edition proposes a permafrost-"
                        "foundation protocol: ground-temperature "
                        "monitoring, thermosyphons where preservation is "
                        "possible, adjustable jacked piles where it is "
                        "not."),
        "citations": [CIT_PERMAFROST],
    },
    {
        "key": "tsunami_coastlines",
        "name": "Tsunami-Proof Coastlines",
        "group": "Coastal Cities",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": ("Tsunamis arrive with forces no ordinary coastal "
                    "structure can resist, yet coastal cities keep "
                    "rebuilding in the inundation zone. The problem is to "
                    "engineer coastlines where the next great tsunami "
                    "destroys property but not communities."),
        "background": ("The 2011 Tohoku tsunami overtopped defenses "
                       "designed for smaller events and erased towns; "
                       "Japan responded with roughly four hundred "
                       "kilometers of seawalls, some nearly fifteen "
                       "meters high, plus vertical evacuation towers and "
                       "hardened warning systems. But walls have limits - "
                       "they block the sea views and economies of "
                       "fishing towns, they can fail catastrophically if "
                       "overtopped, and they protect against the last "
                       "tsunami's height, not the next one's. The deeper "
                       "problem is land use: ports, homes, and schools "
                       "in the zone the water will eventually reclaim. "
                       "No coastline has yet combined walls, forests, "
                       "elevation, evacuation, and land-use retreat into "
                       "a proven survivable system."),
        "why_it_matters": ("The next great subduction earthquake is a "
                           "matter of when, and its tsunami will strike "
                           "coastlines rebuilt since the last one. A "
                           "proven survivable-coastline model would save "
                           "tens of thousands of lives and end the "
                           "rebuild-in-the-kill-zone cycle."),
        "signature_solution": (
            "Step one, the assumptions: no wall stops the maximum "
            "tsunami - survival comes from layered defense plus "
            "evacuation, never from a single barrier. Step two, the "
            "reasoning path: the Japanese experience shows walls buy "
            "time and reduce force, coastal forests dissipate energy "
            "and catch debris, elevation removes people from the "
            "water's reach, and warning plus vertical evacuation "
            "handles the remainder - the system is the solution. Step "
            "three, the proposed mechanism: a survivable-coastline "
            "standard - setback lines based on maximum-credible "
            "inundation modeling, critical facilities and schools on "
            "high ground or vertical-evacuation structures, coastal "
            "forest belts maintained as energy dissipators, seawalls "
            "sized to the probable event with armored overtopping for "
            "the extreme, and evacuation drills tied to the warning "
            "system. Step four, what would confirm it: the next major "
            "tsunami striking a compliant coastline with zero "
            "drowning deaths and damage confined to sacrificial "
            "zones. Step five, what would kill it: if communities "
            "reject setbacks and the coastline redevelops into the "
            "hazard zone, or if warning-system false alarms erode "
            "evacuation compliance. What this does not claim: it does "
            "not claim coasts without damage - the claim is coasts "
            "without mass casualties, where the water takes "
            "buildings, not people."),
        "sig_pointer": ("The Signature edition proposes a survivable-"
                        "coastline standard: maximum-credible setbacks, "
                        "vertical evacuation, forest belts, armored "
                        "seawalls, and drilled warning response - walls "
                        "plus evacuation, never walls alone."),
        "citations": [CIT_JAPAN_TSUNAMI],
    },
    {
        "key": "sinking_cities",
        "name": "Rebuilding Sinking Cities",
        "group": "Coastal Cities",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": ("Some of the world's largest cities are sinking "
                    "faster than the sea is rising - centimeters per "
                    "year - as groundwater pumping collapses the land. "
                    "The problem is to arrest the subsidence and rebuild "
                    "these cities on stable ground."),
        "background": ("Jakarta's northern districts have subsided at "
                       "rates measured in tens of centimeters per year, "
                       "driven by unregulated groundwater extraction; "
                       "Indonesia responded by announcing a new capital, "
                       "Nusantara, in 2019. It is not alone - parts of "
                       "New Orleans, Bangkok, Manila, and Mexico City "
                       "sink for the same reason. Subsidence is largely "
                       "irreversible: once clay layers compact, the land "
                       "does not spring back. Stopping the pumping stops "
                       "the sinking, but cities need water, and "
                       "alternative supplies - piped surface water, "
                       "desalination, managed aquifer recharge - require "
                       "investment on a scale sinking cities struggle to "
                       "muster. Meanwhile the sea keeps rising to meet "
                       "the falling land."),
        "why_it_matters": ("Sinking cities face a slow-motion drowning "
                           "entirely of human making - and therefore "
                           "humanly fixable. Arresting subsidence is the "
                           "cheapest sea-level adaptation available, and "
                           "the alternative is abandoning some of the "
                           "largest urban areas on Earth."),
        "signature_solution": (
            "Step one, the assumptions: subsidence stops when the "
            "pumping stops - the hydrogeology is settled science; the "
            "unsolved part is the political economy of replacing the "
            "water. Step two, the reasoning path: Tokyo stopped its "
            "subsidence in the twentieth century by regulating pumping "
            "and supplying alternative water - the playbook exists and "
            "has worked at megacity scale. Step three, the proposed "
            "mechanism: a subsidence-arrest program - metered wells "
            "with enforced extraction caps, piped surface-water supply "
            "built ahead of the caps so no one goes thirsty, managed "
            "aquifer recharge with treated stormwater to rebuild "
            "pressures, and InSAR satellite monitoring published "
            "publicly so cheating is visible. Step four, what would "
            "confirm it: a sinking district where satellite-measured "
            "subsidence falls to near zero within five years of "
            "enforcement while water access improves. Step five, what "
            "would kill it: if unregulated private wells defeat "
            "metering, or if alternative supply projects stall and "
            "caps become unenforceable. What this does not claim: it "
            "does not claim to raise sunken land - the claim is to "
            "stop the sinking and stabilize the city at its current "
            "elevation, then defend that elevation."),
        "sig_pointer": ("The Signature edition proposes subsidence-arrest "
                        "programs: metered wells with enforced caps, "
                        "alternative supply built first, aquifer "
                        "recharge, and public satellite monitoring - "
                        "the Tokyo playbook, industrialized."),
        "citations": [CIT_JAKARTA],
    },
    {
        "key": "floating_ocean_cities",
        "name": "Floating Ocean Cities",
        "group": "Coastal Cities",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": ("If the sea keeps rising, the ultimate adaptation is "
                    "to live on it. The problem is to engineer floating "
                    "cities - stable, serviced, storm-worthy urban "
                    "districts - as real municipalities, not novelties."),
        "background": ("Floating structures are ancient - from lake "
                       "dwellings to Amsterdam's houseboats - and the "
                       "offshore industry builds floating platforms that "
                       "survive the North Sea. The Oceanix Busan project, "
                       "backed by UN-Habitat and designed by BIG, proposes "
                       "a modular floating city for thousands of "
                       "residents as a climate-adaptation prototype. But "
                       "scaling from platforms to cities means solving "
                       "urban systems on water: drinking water, sewage, "
                       "power, waste, and transport for tens of "
                       "thousands; mooring and breakwaters against "
                       "typhoons; corrosion and biofouling over decades; "
                       "and the legal question of what a floating city "
                       "is under maritime and municipal law. No floating "
                       "settlement has yet operated at city scale through "
                       "a major storm."),
        "why_it_matters": ("Floating cities would turn sea-level rise "
                           "from an existential threat into a design "
                           "parameter - the water can rise and the city "
                           "rises with it. They would also open the "
                           "ocean's surface as humankind's largest "
                           "undeveloped urban land."),
        "signature_solution": (
            "Step one, the assumptions: the city must be a city first "
            "and a vessel second - urban systems (water, waste, power, "
            "governance) are the hard part, flotation is solved "
            "engineering. Step two, the reasoning path: modularity is "
            "the answer to both storms and growth - hexagonal platforms "
            "that flex with waves, detach for maintenance, and multiply "
            "as population grows, exactly as the Oceanix concept "
            "proposes. Step three, the proposed mechanism: a "
            "floating-city standard - modular buoyant platforms with "
            "redundant mooring, breakwater rings sized for the "
            "hundred-year storm, closed-loop water and waste systems "
            "(the ocean forbids the city's pollution), district power "
            "from marine renewables, and detachable modules so any "
            "platform can be towed to dry dock. Step four, what would "
            "confirm it: a thousand-resident pilot operating for five "
            "years including a major storm, with utility costs and "
            "resident satisfaction matching shore districts. Step five, "
            "what would kill it: if biofouling and corrosion drive "
            "maintenance beyond shore-city costs, or if wave-induced "
            "motion proves intolerable for daily urban life. What this "
            "does not claim: it does not claim open-ocean cities in "
            "hurricane alleys - the claim is sheltered-water urban "
            "districts that rise with the sea."),
        "sig_pointer": ("The Signature edition proposes a floating-city "
                        "standard: modular buoyant platforms, storm-"
                        "sized breakwaters, closed-loop utilities, and "
                        "detachable modules - a city first, a vessel "
                        "second."),
        "citations": [CIT_OCEANIX],
    },
    {
        "key": "rewilded_deltas",
        "name": "Rewilded River Deltas That Protect Cities",
        "group": "Coastal Cities",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("Deltas naturally build land that buffers cities "
                    "from storms, but dammed rivers starve them of "
                    "sediment and the land drowns. The problem is to "
                    "re-engineer rivers to rebuild their deltas - "
                    "growing protective wetlands instead of losing "
                    "them."),
        "background": ("Coastal Louisiana has lost on the order of two "
                       "thousand square miles of wetlands since the "
                       "1930s: levees built for flood control channel "
                       "the Mississippi's sediment past the delta and "
                       "into the deep Gulf, while the starved marshes "
                       "subside and drown. The Netherlands' Room for the "
                       "River program showed the alternative philosophy "
                       "- give rivers space and they protect you. "
                       "Sediment diversions, which cut the levee to let "
                       "the river build land again, are the proposed "
                       "fix, but they are slow, their land-building "
                       "rates are uncertain, they disrupt fisheries and "
                       "navigation, and no diversion has yet rebuilt "
                       "wetlands at the scale of the loss."),
        "why_it_matters": ("Every square kilometer of healthy marsh is a "
                           "storm-surge absorber, a fishery, and a "
                           "carbon sink that no seawall can replace. "
                           "Rebuilding deltas is the only coastal defense "
                           "that grows stronger with time instead of "
                           "weaker."),
        "signature_solution": (
            "Step one, the assumptions: the river still carries the "
            "sediment - the problem is plumbing, not supply; the fix "
            "is reconnecting river to delta. Step two, the reasoning "
            "path: land building is slow but relentless once the "
            "connection is restored - the strategy is to start "
            "diversions early, measure relentlessly, and adapt "
            "operations to what the land-building data says. Step "
            "three, the proposed mechanism: an adaptive delta-"
            "building program - gated sediment diversions operable "
            "across flow regimes, dense elevation and ecology "
            "monitoring that scores each diversion's land-building "
            "rate, and operating rules rewritten annually from the "
            "data, with navigation and fisheries compensated from "
            "the program budget. Step four, what would confirm it: "
            "diversions showing net land gain - measured by lidar "
            "surveys - exceeding the regional loss rate within two "
            "decades, with marsh health indices improving. Step five, "
            "what would kill it: if sediment loads prove too fine or "
            "too small to build land faster than subsidence and sea-"
            "level rise destroy it, or if diversions silt the "
            "navigation channel they were meant to spare. What this "
            "does not claim: it does not claim restoring the "
            "pre-levee delta - the claim is a managed, growing "
            "wetland buffer that outpaces loss."),
        "sig_pointer": ("The Signature edition proposes adaptive delta-"
                        "building: gated sediment diversions, lidar-"
                        "measured land-building scores, and operating "
                        "rules rewritten annually from the data."),
        "citations": [CIT_LOUISIANA, CIT_ROOM_RIVER],
    },
    {
        "key": "kilometer_tower",
        "name": "Kilometer-Tall Towers",
        "group": "Megastructures",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("The Burj Khalifa reaches 828 meters; the "
                    "kilometer tower remains unbuilt. The problem is to "
                    "engineer buildings a full kilometer tall that are "
                    "safe, usable, and economically sane."),
        "background": ("Height brings compounding penalties: wind loads "
                       "grow with the square of wind speed and the "
                       "exposed area, elevators consume ever more core "
                       "space (steel ropes become too heavy for their "
                       "own length, which carbon-fiber ropes like KONE's "
                       "UltraRope address), concrete must be pumped to "
                       "unprecedented heights, and vortex shedding can "
                       "shake a tower like a reed. The Jeddah Tower, "
                       "planned above one kilometer, has stalled - a "
                       "reminder that the barrier is as much economic "
                       "and logistical as technical. Structural systems "
                       "exist on paper - bundled tubes, diagrids, "
                       "buttressed cores - but none has been proven at "
                       "kilometer scale, and the usable floor area "
                       "shrinks as structure and elevators eat the plan."),
        "why_it_matters": ("The kilometer tower is the frontier that "
                           "forces every tall-building technology to "
                           "mature: materials, damping, vertical "
                           "transport, fire safety. Solving it unlocks "
                           "the vertical city - density without sprawl "
                           "taken to its logical conclusion."),
        "signature_solution": (
            "Step one, the assumptions: the tower must earn its height "
            "- a kilometer of vanity office space is unbuildable, but "
            "a kilometer of mixed-use vertical city with its own "
            "economy can be. Step two, the reasoning path: the "
            "penalties compound, so the design must attack all of them "
            "at once - aerodynamic form against vortex shedding, "
            "carbon-fiber hoisting against rope weight, sky lobbies "
            "against elevator core sprawl, and a structural system "
            "with proven damping. Step three, the proposed mechanism: "
            "a kilometer-tower reference design - tapered aerodynamic "
            "form verified in wind-tunnel and CFD campaigns, "
            "buttressed-core structure with distributed damping, "
            "multi-deck carbon-rope elevators with sky-lobby "
            "transfers, refuge floors with independent fire and smoke "
            "control every twenty stories, and construction logistics "
            "(pumping, craneage, worker transport) engineered before "
            "the first foundation pour. Step four, what would confirm "
            "it: a completed, occupied kilometer tower with measured "
            "wind and seismic performance matching the design models "
            "and elevator service meeting high-rise standards. Step "
            "five, what would kill it: if usable floor efficiency "
            "falls below the economic threshold, or if evacuation "
            "modeling cannot clear the tower within tenable time. "
            "What this does not claim: it does not claim kilometer "
            "towers everywhere - the claim is one proven reference "
            "design that makes the second one financeable."),
        "sig_pointer": ("The Signature edition proposes a kilometer-"
                        "tower reference design: aerodynamic tapered "
                        "form, buttressed core with damping, carbon-rope "
                        "elevators with sky lobbies, and refuge floors - "
                        "all engineered before the first pour."),
        "citations": [CIT_BURJ, CIT_KONE],
    },
    {
        "key": "quake_early_warning_buildings",
        "name": "Earthquake Early Warning Baked Into Every Building",
        "group": "Seismic Design",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("Earthquake early warning can give seconds to a "
                    "minute of notice before shaking arrives - but only "
                    "if buildings know what to do with it. The problem "
                    "is to wire every building in seismic zones to act "
                    "automatically on warning."),
        "background": ("Systems like Japan's emergency earthquake "
                       "warning and the USGS ShakeAlert, operating "
                       "publicly in California since 2019, detect the "
                       "fast, weak P-wave and broadcast alerts before "
                       "the damaging S-wave arrives. Seconds are enough "
                       "to stop elevators at the nearest floor, shut off "
                       "gas valves, halt surgery, and get people under "
                       "cover - if the building is listening. Today only "
                       "a fraction of buildings integrate warnings: most "
                       "alerts go to phones, where they startle more "
                       "than they protect. The unsolved problem is "
                       "ubiquity and automation - building systems that "
                       "receive, trust, and act on warnings without "
                       "human intervention, robust against false alarms."),
        "why_it_matters": ("Seconds of automated action across millions "
                           "of buildings would prevent the secondary "
                           "disasters - fires from broken gas lines, "
                           "elevator entrapments, surgical catastrophes - "
                           "that multiply earthquake casualties. It turns "
                           "early warning from a phone notification into "
                           "a building reflex."),
        "signature_solution": (
            "Step one, the assumptions: false alarms are the enemy of "
            "trust - the system must be tuned so that automated actions "
            "are safe even when the warning is wrong. Step two, the "
            "reasoning path: buildings already have automation "
            "infrastructure - fire panels, elevator controllers, "
            "building management systems - so warning integration is a "
            "protocol and a relay, not a new industry. Step three, the "
            "proposed mechanism: a building-warning standard - a "
            "certified warning receiver in every commercial and "
            "multi-family building in seismic zones, wired to a "
            "graded action list (elevators to nearest floor, gas and "
            "hazardous processes to safe state, announcements, "
            "doors unlocked), with actions tiered by alert confidence "
            "so low-confidence alerts trigger only reversible steps. "
            "Step four, what would confirm it: a seismic zone where "
            "building integration is code-required, showing in the "
            "next damaging quake measurable reductions in elevator "
            "entrapments and gas-fed fires versus comparable "
            "non-integrated areas. Step five, what would kill it: if "
            "false-alarm rates cause occupants to disable the systems, "
            "or if liability fears keep building owners from "
            "connecting. What this does not claim: it does not claim "
            "to protect structures from shaking - the claim is "
            "protecting people and systems in the seconds before it "
            "arrives."),
        "sig_pointer": ("The Signature edition proposes a building-"
                        "warning standard: certified receivers in every "
                        "seismic-zone building, graded automated actions "
                        "tiered by alert confidence - a building reflex, "
                        "not a phone notification."),
        "citations": [CIT_SHAKEALERT],
    },
    {
        "key": "five_hundred_year_standard",
        "name": "The 500-Year Infrastructure Standard",
        "group": "Foundations and Materials",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("Infrastructure economics discounts the future so "
                    "steeply that building for centuries looks "
                    "irrational on paper. The problem is to create "
                    "design, procurement, and accounting standards that "
                    "make 500-year infrastructure the rational choice."),
        "background": ("Cathedrals were built for eternity; modern "
                       "infrastructure is built for depreciation "
                       "schedules. The mathematics of discounting means "
                       "a dollar of benefit in year 200 is worth pennies "
                       "today at standard rates, so procurement rewards "
                       "the cheapest adequate bid and punishes durability "
                       "investment. ISO 15686 provides service-life "
                       "planning methods, and life-cycle costing is "
                       "standard in theory, but in practice the "
                       "low-bid, short-horizon logic dominates public "
                       "works. The result is a built world optimized for "
                       "the next election cycle. Changing this requires "
                       "not new concrete but new institutions: "
                       "procurement rules, accounting standards, and "
                       "stewardship bodies that outlive political terms."),
        "why_it_matters": ("Every other problem in this database is "
                           "cheaper to solve under a 500-year standard - "
                           "durability investments finally pencil out, "
                           "and the replacement treadmill stops. It is "
                           "the meta-problem: fix the time horizon and "
                           "the engineering follows."),
        "signature_solution": (
            "Step one, the assumptions: institutions, not equations, "
            "are the barrier - the math of long horizons is known; "
            "what is missing is owners with long horizons. Step two, "
            "the reasoning path: endowments and cathedrals prove "
            "perpetual stewardship is possible - infrastructure needs "
            "its equivalent: owners legally bound to the long term. "
            "Step three, the proposed mechanism: a 500-year "
            "stewardship framework - infrastructure trusts that own "
            "major assets with charters requiring century-scale "
            "maintenance reserves, procurement scored on 200-year "
            "present worth at a mandated low social discount rate, "
            "and durability audits published like financial audits, "
            "with the trust's engineers holding veto over "
            "value-engineering that shortens life. Step four, what "
            "would confirm it: trust-owned assets showing, over "
            "decades, lower total cost per service-year than "
            "conventionally procured equivalents, with published "
            "accounts. Step five, what would kill it: if political "
            "authorities raid the reserves or dissolve the trusts - "
            "the failure mode is governance, not engineering. What "
            "this does not claim: it does not claim to make "
            "politicians think long-term - the claim is to move "
            "stewardship into institutions designed to outlast them."),
        "sig_pointer": ("The Signature edition proposes 500-year "
                        "stewardship: infrastructure trusts with "
                        "century-scale reserves, procurement scored on "
                        "200-year present worth, and published "
                        "durability audits."),
        "citations": [CIT_ISO15686],
    },
    {
        "key": "transoceanic_tunnel",
        "name": "The Transoceanic Tunnel",
        "group": "Bridges and Tunnels",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("Oceans still separate continents by days of travel; "
                    "a tunnel beneath one would join them by hours. The "
                    "problem is to determine whether a transoceanic "
                    "tunnel - under the Atlantic or the Bering Strait - "
                    "can actually be engineered and afforded."),
        "background": ("The idea is old - Victorian engineers sketched "
                       "Atlantic tunnels - and the components exist in "
                       "embryo: the Channel Tunnel proved long undersea "
                       "bored tunnels, immersed tubes cross wide "
                       "waterways, and vacuum-tube transport concepts "
                       "promise the speeds that would make the distance "
                       "worthwhile. The Bering Strait, only about 85 "
                       "kilometers wide at its narrowest, is the "
                       "plausible first candidate; a true transatlantic "
                       "tunnel would be thousands of kilometers through "
                       "abyssal depths. The barriers are staggering: "
                       "pressure at depth, construction logistics mid-"
                       "ocean, ventilation and safety over continental "
                       "distances, and costs in the trillions against "
                       "aircraft that already fly the route in hours."),
        "why_it_matters": ("Even proving the transoceanic tunnel "
                           "impossible at acceptable cost would be "
                           "valuable - it would settle a century of "
                           "speculation with engineering. Proving it "
                           "possible would join continents the way "
                           "railways joined nations, with freight and "
                           "passenger consequences hard to overstate."),
        "signature_solution": (
            "Step one, the assumptions: honesty requires staging - "
            "the Bering Strait crossing first as the proving ground, "
            "the Atlantic only if the economics of the first work. "
            "Step two, the reasoning path: the tunnel is three "
            "problems - the tube (pressure, construction), the "
            "train (speed, safety), and the money - and each must "
            "close independently before the project is real. Step "
            "three, the proposed mechanism: a staged feasibility "
            "program - a Bering Strait reference design (immersed "
            "tube in the shallow strait, conventional rail first, "
            "vacuum upgrade later), full-scale pressure testing of "
            "tube segments, and an honest published cost model "
            "including mid-ocean construction logistics; the Atlantic "
            "concept advances only on the Bering's measured numbers. "
            "Step four, what would confirm it: a financed, permitted "
            "Bering crossing under construction with costs tracking "
            "the reference model. Step five, what would kill it: if "
            "the reference design's cost per kilometer exceeds any "
            "plausible freight and passenger revenue, or if "
            "geopolitics makes the strait unbuildable regardless of "
            "engineering. What this does not claim: it does not claim "
            "the Atlantic tunnel is buildable - the claim is a "
            "disciplined path that finds out, starting where the "
            "ocean is narrowest."),
        "sig_pointer": ("The Signature edition proposes staged honesty: "
                        "a Bering Strait reference design as proving "
                        "ground, full-scale pressure testing, published "
                        "cost models - the Atlantic only on measured "
                        "numbers."),
        "citations": [CIT_NORWAY_TUNNEL],
    },
    {
        "key": "subterranean_climate_refuge",
        "name": "Subterranean Climate-Refuge Cities",
        "group": "Underground Cities",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("Extreme heat is making parts of the world "
                    "uninhabitable for months each year, and air "
                    "conditioning the outdoors is impossible. The "
                    "problem is to build underground districts where "
                    "populations can live, work, and wait out the "
                    "unlivable season in comfort."),
        "background": ("Underground temperatures stabilize just meters "
                       "down - cool in summer, warm in winter - a "
                       "fact humans have exploited from Derinkuyu to "
                       "Coober Pedy. As wet-bulb temperatures approach "
                       "human survivability limits in South Asia, the "
                       "Gulf, and beyond, the underground offers the "
                       "only passive refuge: no energy required to stay "
                       "cool. Helsinki and other cities already put "
                       "infrastructure underground at scale, and data "
                       "centers prove deep facilities can be built and "
                       "operated. What does not exist is the urban "
                       "version: whole districts designed as seasonal "
                       "refuges, with housing, workplaces, schools, and "
                       "public life underground, ready to absorb "
                       "populations when the surface becomes dangerous."),
        "why_it_matters": ("Climate refuge is becoming a habitability "
                           "question for hundreds of millions of people. "
                           "Underground districts would provide the one "
                           "refuge that needs no fuel, never fails in a "
                           "blackout, and lasts as long as the rock "
                           "itself."),
        "signature_solution": (
            "Step one, the assumptions: the refuge must be ordinary "
            "urban space most of the year - single-use bunkers will "
            "not be maintained; dual-use districts will. Step two, the "
            "reasoning path: the livability standard from underground "
            "cities applies, plus thermal design - the rock is the "
            "air conditioner, so the district's cooling comes from "
            "ground coupling, not chillers. Step three, the proposed "
            "mechanism: a refuge-district standard - underground "
            "mixed-use districts in heat-threatened cities, thermally "
            "coupled to stable ground temperatures, with independent "
            "water and power, vertical evacuation-equivalent egress, "
            "and surface parks above that double as emergency "
            "mustering grounds; occupied year-round as normal "
            "neighborhoods, surged during heat emergencies. Step four, "
            "what would confirm it: a district riding out a record "
            "heat season with indoor conditions in the comfort range "
            "on ground coupling alone, and residents choosing to stay "
            "underground by preference. Step five, what would kill it: "
            "if excavation costs in the cities that need refuge most "
            "prove unaffordable, or if groundwater and geology rule "
            "out the candidate sites. What this does not claim: it "
            "does not claim to air-condition cities - the claim is "
            "refuge districts where life continues comfortably while "
            "the surface is unlivable."),
        "sig_pointer": ("The Signature edition proposes refuge-district "
                        "standards: underground mixed-use neighborhoods "
                        "cooled by ground coupling, dual-use year-round, "
                        "surged during heat emergencies."),
        "citations": [CIT_DERINKUYU, CIT_HELSINKI],
    },
    {
        "key": "self_maintaining_city",
        "name": "The Self-Maintaining City",
        "group": "Urban Infrastructure",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("Every infrastructure system in a city decays, is "
                    "inspected sporadically by humans, and is repaired "
                    "after failure. The problem is to integrate sensing, "
                    "modeling, and robotic repair across all urban "
                    "infrastructure into a city that maintains itself."),
        "background": ("The pieces exist: structural health monitoring "
                       "with accelerometers and fiber optics, digital "
                       "twins of bridges and tunnels, self-healing "
                       "materials, inspection drones and crawlers, and "
                       "the pavement, dam, and water networks described "
                       "earlier in this database. What does not exist is "
                       "the integration - one city-scale system that "
                       "ingests every sensor, prioritizes every defect by "
                       "risk, dispatches robotic or human repair, and "
                       "learns from every intervention. Cities remain "
                       "collections of separately managed assets, each "
                       "with its own inspection backlog. The "
                       "self-maintaining city is the compounding of "
                       "every solution in this database into a single "
                       "operating philosophy: find everything early, fix "
                       "everything cheaply, never let failure surprise "
                       "you."),
        "why_it_matters": ("This is the capstone of civil engineering's "
                           "unsolved problems: infrastructure that "
                           "outlives its builders because it tends "
                           "itself. A city that maintains itself frees "
                           "its wealth from the repair treadmill and "
                           "hands its grandchildren assets, not "
                           "liabilities."),
        "signature_solution": (
            "Step one, the assumptions: the city cannot be rebuilt at "
            "once - the self-maintaining city is a retrofit philosophy "
            "applied asset by asset, with the integration layer built "
            "first. Step two, the reasoning path: maintenance is an "
            "information problem before it is a wrench problem - the "
            "city that knows the condition of everything can maintain "
            "everything; the city that guesses, cannot. Step three, "
            "the proposed mechanism: a municipal maintenance operating "
            "system - a city digital twin ingesting structural, "
            "hydraulic, and pavement sensor data; risk models that "
            "turn measurements into prioritized work orders; robotic "
            "fleets (crawlers, drones, heater trucks, sealant robots) "
            "executing the routine tickets; and human crews reserved "
            "for what robots cannot do - with every intervention "
            "feeding back into the models. Step four, what would "
            "confirm it: a pilot city where infrastructure condition "
            "indices improve year over year while maintenance spending "
            "per asset falls, and where no major failure occurs "
            "without prior warning in the system. Step five, what "
            "would kill it: if sensor maintenance itself becomes the "
            "new treadmill, or if institutional silos refuse to share "
            "data with the twin. What this does not claim: it does "
            "not claim humans leave the loop - the claim is humans "
            "elevated to judgment and oversight while machines handle "
            "the watching and the routine fixing."),
        "sig_pointer": ("The Signature edition proposes a municipal "
                        "maintenance operating system: a city digital "
                        "twin, risk-prioritized work orders, robotic "
                        "repair fleets, and humans elevated to judgment "
                        "- the compounding of this whole database."),
        "citations": [CIT_ASCE21, CIT_ISO15686],
    },
]
