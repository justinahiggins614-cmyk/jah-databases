#!/usr/bin/env python3
"""Entries for The Unsolved Agriculture Database (34 problems) and its
Signature edition. Both halves cover the SAME 34 unsolved agricultural
problems, ladder-ordered by accessibility (ladder_rank 1-34).

Public halves: real, fact-checked problems - feeding 10 billion sustainably,
nitrogen-use efficiency, drought-proof staple crops, soil microbiome
management, closing the yield gap without new land, phosphorus, soil erosion,
irrigation water, post-harvest loss, pesticide resistance, livestock methane,
pollinators, nitrogen-fixing cereals, C4 rice, heat sterility, salinity,
groundwater, genetic base, mycotoxins, land competition, nitrous oxide, the
precision-ag digital divide, seed systems, apomixis, perennial grains,
orphan crops, synthetic symbiosis, crop wild relatives, multi-stress stacking,
the rhizosphere signaling code, regenerative agriculture at scale,
controlled-environment staples, One Health, and the ultimate yield ceiling -
each with problem, background, why-it-matters, and a short pointer to the
Signature proposed solution.

Signature halves: the same 34 problems through the Signature lens, titles
suffixed " (Signature Edition)", src 'signature', every signature_solution
opening with the EXACT label "Signature-generated proposed solution \u2014 not
established science", and never claiming proof or peer acceptance.

Honesty rule (throughout): the problems are OPEN in established science;
Signature proposals are proposed paths, labeled as such.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_agriculture.py). Every demo is a
solution-explorer walkthrough: interactive steps, adjustable assumptions,
real computed values, tight-bounds asserts (never float exact-equality),
a confirm/refute panel, and the OK marker.

No website references. No Facebook.
"""

SIG_LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry his original proposed solution "
            "approaches to each unsolved agricultural problem - clearly labeled "
            "Signature-generated proposed solutions, never presented as "
            "established science or peer-accepted results.")

CIT_BASE = [
    "FAO. The State of Food and Agriculture. Food and Agriculture "
    "Organization of the United Nations; Rome (annual).",
    "FAO. The State of Food Security and Nutrition in the World. FAO, IFAD, "
    "UNICEF, WFP and WHO; Rome (annual).",
]

ENTRIES = [
    # ------------------------------------------------- 1 FOUNDATIONS
    {
        "key": "feed-10-billion",
        "name": "Feeding 10 Billion People Sustainably",
        "group": "Foundations",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "problem": ("The world must feed roughly 10 billion people within a "
                    "few decades while staying inside planetary boundaries, "
                    "and no one has a verified plan for doing both at once. "
                    "United Nations projections put the population near 10 "
                    "billion by the 2050s, FAO assessments estimate food "
                    "production must rise by roughly half against a 2012 "
                    "baseline, and yet agriculture already drives most "
                    "deforestation, most freshwater withdrawals, and a large "
                    "share of greenhouse-gas emissions. The unsolved core is "
                    "not growing more calories in a laboratory but growing "
                    "enough nutritious food, for everyone, on the land and "
                    "water we already use, without wrecking the systems that "
                    "make farming possible."),
        "background": ("Thomas Malthus framed the fear in 1798 that food "
                       "supply could not keep pace with population, and every "
                       "generation since has had to outrun him. The Green "
                       "Revolution of the 1960s and 1970s did exactly that: "
                       "Norman Borlaug's semi-dwarf wheat, IR8 rice from the "
                       "International Rice Research Institute, synthetic "
                       "fertilizer, and irrigation roughly tripled cereal "
                       "output per hectare while the population doubled. But "
                       "the second doubling looks harder, because the first "
                       "one spent down easy gains: yield growth rates for "
                       "major cereals have slowed in many regions, arable "
                       "land expansion has nearly stopped in most of the "
                       "world, and the environmental bills - dead zones from "
                       "nitrogen runoff, drained aquifers, deforested "
                       "frontiers - are coming due at the same time. "
                       "Scenarios from FAO and the global modeling community "
                       "show the math can close, but only with simultaneous "
                       "wins on diets, waste, yields, and land use that no "
                       "country has yet achieved together."),
        "why_it_matters": ("If the arithmetic fails, the failure arrives as "
                           "hunger, price spikes, and land conflict, hitting "
                           "the poorest first. If it succeeds only by "
                           "clearing more forest and draining more aquifers, "
                           "the climate and water systems that farming "
                           "depends on degrade further, which makes the next "
                           "decade's arithmetic worse. This is the master "
                           "problem of agriculture: every other unsolved "
                           "problem in this database is a piece of it."),
        "sig_pointer": ("The Signature edition proposes a 'ladder of "
                        "closure' walkthrough that prices every gap-closing "
                        "lever in the same units and stacks them cheapest "
                        "first on real farm data. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) food demand can be "
                     "decomposed into population times diet composition "
                     "divided by the fraction of produced food actually "
                     "eaten; (2) every gap-closing lever - waste reduction, "
                     "yield-gap closure, diet shifts, new production systems "
                     "- can be priced per delivered calorie on real farm "
                     "ledgers, not model averages; (3) levers interact, so "
                     "the stack must be ordered cheapest-first to avoid "
                     "double-counting. Reasoning path: start from the "
                     "production multiplier the arithmetic demands, ledger "
                     "each lever's real per-calorie cost and realistic "
                     "ceiling from field measurements, then stack them until "
                     "the multiplier is met or the stack runs out - which "
                     "reveals exactly how large the remaining gap is. "
                     "Proposed mechanism: a public 'closure ledger' per "
                     "country where each lever is entered with its measured "
                     "cost, ceiling, and side effects, and the cheapest "
                     "unclaimed lever is always the next policy target. What "
                     "would confirm it: national ledgers whose stacked "
                     "levers reproduce observed production trends, and "
                     "pilot regions that close their gap on the predicted "
                     "cheapest-first sequence. What would kill it: levers "
                     "whose field ceilings fall far below laboratory "
                     "claims, or interactions that make the stacked total "
                     "systematically unattainable. What it does NOT claim: "
                     "that technology alone closes the gap, that any single "
                     "lever is sufficient, or that the ledger is a substitute "
                     "for political decisions about diets and land."),
        "key_points": [
            "Population heads toward roughly 10 billion while arable land barely expands.",
            "Food output must rise on the order of half again versus 2012, per FAO scenarios.",
            "Agriculture already dominates freshwater use and drives deforestation and a large emissions share.",
            "No country has yet closed all four levers - diets, waste, yields, land - simultaneously.",
        ],
        "requirements": [
            "Frame demand as population times diet divided by the fraction of food actually eaten.",
            "Price every gap-closing lever per delivered calorie on real farm data.",
            "Order levers cheapest-first and correct for interactions so totals are not double-counted.",
        ],
        "standards": [
            "United Nations World Population Prospects; FAO State of Food and Agriculture scenarios.",
        ],
        "citations": CIT_BASE,
        "demo": {
            "calc": "prod", "quantity": "Required food-production multiplier vs 2012",
            "unit": "multiplier", "formula": "pop_factor * diet_factor * loss_cut",
            "assumptions": [
                ("Population growth factor to 2050s", 1.25, [1.10, 1.25, 1.40]),
                ("Diet intensification factor", 1.15, [1.00, 1.15, 1.30]),
                ("Food-loss reduction factor", 0.90, [0.75, 0.90, 1.00]),
            ],
            "checks": [((1.10, 1.00, 1.00), 1.10, 1e-9),
                       ((1.40, 1.30, 0.75), 1.365, 1e-6)],
            "steps": [
                "Step 1: set the population factor from demographic projections.",
                "Step 2: set the diet factor from income-driven diet shifts.",
                "Step 3: set the loss-reduction factor from waste interventions.",
                "Step 4: multiply the three levers into one demand multiplier.",
                "Step 5: compare the multiplier against the stacked supply levers.",
            ],
            "confirm": [
                "National closure ledgers reproduce observed production trends.",
                "Pilot regions close their gap on the predicted cheapest-first sequence.",
            ],
            "refute": [
                "Field ceilings for waste and yield levers fall far below lab claims.",
                "Lever interactions make the stacked total systematically unattainable.",
            ],
            "note": "Demand-multiplier explorer for the feeding-10-billion problem.",
        },
    },
    # ------------------------------------------------- 2 FOUNDATIONS
    {
        "key": "yield-gap",
        "name": "Closing the Yield Gap Without New Land",
        "group": "Foundations",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "problem": ("On most of the world's farmland, farmers harvest far "
                    "less than the land and climate could deliver with known "
                    "methods, and the gap between actual and attainable yield "
                    "remains one of the largest untapped food sources on "
                    "Earth. Yield-gap atlases show gaps of 30 to 50 percent "
                    "or more for cereals across much of sub-Saharan Africa, "
                    "Eastern Europe, and parts of Asia, while global studies "
                    "estimate that closing gaps to 80 percent of potential "
                    "could add several hundred million tonnes of grain "
                    "without clearing a hectare. The unsolved part is not "
                    "knowing the gap exists but knowing why it persists on "
                    "each farm - soils, water, seed, nutrients, knowledge, "
                    "credit, risk - and which lever to pull first, farm by "
                    "farm, without the blanket fertilizer-and-water recipe "
                    "that created the environmental problems of the Green "
                    "Revolution."),
        "background": ("The yield-gap concept was formalized in the 2000s "
                       "and 2010s by researchers including Martin van "
                       "Ittersum's group, who built the Global Yield Gap "
                       "Atlas from weather, soil, and crop-model data, and "
                       "by Mueller and colleagues, whose 2012 Nature analysis "
                       "mapped nutrient and water limits on attainable "
                       "yields worldwide. The atlas showed a striking pattern: "
                       "the biggest gaps sit where farmers are poorest and "
                       "extension services thinnest, which means the gap is "
                       "as much an economic and institutional problem as a "
                       "biological one. Attempts to close gaps with "
                       "one-size-fits-all input packages have repeatedly "
                       "raised yields but also raised nitrogen runoff and "
                       "debt, and precision-agriculture tools that could "
                       "target the true constraint per field remain out of "
                       "reach for most smallholders."),
        "why_it_matters": ("Closing yield gaps is the single largest lever "
                           "for feeding 10 billion without expanding "
                           "farmland into forests and savannas. Done "
                           "precisely, it raises farmer incomes and spares "
                           "land; done bluntly, it repeats the pollution "
                           "and debt traps of the first Green Revolution. "
                           "The difference between those two outcomes is "
                           "diagnosis."),
        "sig_pointer": ("The Signature edition proposes a per-field "
                        "constraint-diagnosis walkthrough that scores each "
                        "limiting factor separately and closes the cheapest "
                        "binding constraint first. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the yield gap on a "
                     "given field decomposes into separable constraints - "
                     "water, nutrients, seed genetics, pests, management - "
                     "that can be ranked by which binds first; (2) a "
                     "low-cost field test exists or can be built for each "
                     "constraint; (3) closing a non-binding constraint "
                     "wastes money and sometimes pollutes, so sequencing "
                     "matters. Reasoning path: measure attainable yield "
                     "from local weather and soil, measure actual yield, "
                     "then run the cheapest diagnostic per constraint in "
                     "order of expected bindingness until the binding "
                     "constraint is found and closed, then re-diagnose. "
                     "Proposed mechanism: a field-level 'gap ledger' app "
                     "that records each diagnostic result and each "
                     "intervention's yield response, so the true "
                     "constraint sequence is learned per farm, not "
                     "assumed from regional averages. What would confirm "
                     "it: pilot farms where the ledger's recommended "
                     "sequence closes more gap per dollar than blanket "
                     "packages, with lower nutrient surplus. What would "
                     "kill it: constraints that refuse to separate - "
                     "where closing one always requires closing several, "
                     "destroying the sequencing advantage. What it does NOT "
                     "claim: that diagnosis replaces good seed and inputs, "
                     "or that gaps can close to 100 percent of potential "
                     "anywhere."),
        "key_points": [
            "Yield gaps of 30-50 percent or more persist across much of Africa, Eastern Europe, and Asia.",
            "Closing gaps to 80 percent of potential could add hundreds of millions of tonnes of grain.",
            "The biggest gaps sit where farmers are poorest and extension is thinnest.",
            "Blanket input packages close gaps but raise pollution and debt; precision diagnosis is the missing step.",
        ],
        "requirements": [
            "Measure attainable yield from local weather and soil, not regional averages.",
            "Rank constraints by which binds first and test cheapest-first.",
            "Record every intervention's yield response so the sequence is learned per farm.",
        ],
        "standards": [
            "Global Yield Gap Atlas methodology (van Ittersum et al.); Mueller et al., Nature 2012.",
        ],
        "citations": CIT_BASE + [
            "Mueller ND et al. Closing yield gaps through nutrient and water "
            "management. Nature; 2012.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Closable yield gap after soil discount",
            "unit": "t/ha", "formula": "(attainable - actual) * (1 - soil_discount)",
            "expr": "(a0 - a1) * (1 - a2)",
            "assumptions": [
                ("Attainable yield", 9.0, [8.0, 9.0, 10.0]),
                ("Actual farm yield", 5.0, [4.0, 5.0, 6.0]),
                ("Soil degradation discount", 0.5, [0.2, 0.5, 0.8]),
            ],
            "checks": [((8.0, 4.0, 0.2), 3.2, 1e-9),
                       ((10.0, 6.0, 0.8), 0.8, 1e-9)],
            "steps": [
                "Step 1: compute attainable yield from local weather and soil.",
                "Step 2: subtract actual yield to get the raw gap.",
                "Step 3: discount for degraded soils that cap the ceiling.",
                "Step 4: rank the binding constraints behind the remainder.",
                "Step 5: close the cheapest binding constraint first, then re-diagnose.",
            ],
            "confirm": [
                "Ledger-guided farms close more gap per dollar than blanket packages.",
                "Nutrient surplus falls while yields rise on diagnosed fields.",
            ],
            "refute": [
                "Constraints refuse to separate: closing one always needs several.",
                "Diagnosed sequences cost more than blanket packages for the same gain.",
            ],
            "note": "Yield-gap diagnosis explorer for closing gaps without new land.",
        },
    },
    # ------------------------------------------------- 3 FOUNDATIONS
    {
        "key": "nitrogen-efficiency",
        "name": "Nitrogen-Use Efficiency",
        "group": "Foundations",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "problem": ("Roughly half of the nitrogen fertilizer spread on "
                    "fields never reaches a crop, and that lost half "
                    "becomes nitrous oxide in the air, nitrate in drinking "
                    "water, and dead zones in coastal seas. Global "
                    "nitrogen-use efficiency - the share of applied nitrogen "
                    "recovered in harvest - hovers near 40 to 50 percent, "
                    "meaning farmers buy twice the nitrogen their crops "
                    "actually use. The unsolved problem is timing and "
                    "placement: crops need nitrogen in pulses that match "
                    "their growth stages, but fertilizer is mostly applied "
                    "in one or two blunt doses that the soil cannot hold. "
                    "Raising efficiency toward 70 percent would cut "
                    "emissions, save farmers billions, and shrink the "
                    "dead zones, but no universal recipe works across "
                    "soils, climates, and crops."),
        "background": ("The Haber-Bosch process, commercialized in 1913, "
                       "made synthetic nitrogen abundant, and Erisman and "
                       "colleagues estimated in 2008 that about half the "
                       "world's population is fed because of it. The "
                       "efficiency problem was documented as applications "
                       "grew: Lassaletta and others showed nitrogen-use "
                       "efficiency falling in intensifying regions even as "
                       "total use rose, and the planetary-boundaries "
                       "framework lists the nitrogen cycle as one of the "
                       "most severely transgressed limits. Agronomists "
                       "responded with the '4R' framework - right source, "
                       "right rate, right time, right place - plus split "
                       "applications, urease and nitrification inhibitors, "
                       "and slow-release coatings, all of which work in "
                       "trials. The gap between trial efficiency and field "
                       "efficiency remains stubborn because timing "
                       "decisions depend on weather forecasts, labor, and "
                       "credit that smallholders often lack."),
        "why_it_matters": ("Nitrogen is the nutrient that most limits "
                           "yields and the pollutant that most damages "
                           "water and climate. Every percentage point of "
                           "efficiency gained is fertilizer not bought, "
                           "emissions not released, and rivers not "
                           "poisoned. It is the cheapest large climate and "
                           "water win in agriculture, if the timing problem "
                           "can be solved."),
        "sig_pointer": ("The Signature edition proposes an in-season "
                        "nitrogen ledger that senses crop need in real time "
                        "and releases fertilizer only into the crop's "
                        "uptake windows. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the crop's nitrogen "
                     "demand curve through the season is knowable from "
                     "growth stage plus a cheap leaf-color or canopy "
                     "sensor reading; (2) soil cannot hold large nitrate "
                     "pulses, so any dose beyond the next uptake window is "
                     "mostly loss; (3) inhibitors and coatings shift the "
                     "release curve but do not fix bad timing. Reasoning "
                     "path: model each field's demand curve, dose only "
                     "the next window's need, verify with a mid-season "
                     "sensor reading, and log the recovery rate in a "
                     "ledger that learns the field's true efficiency. "
                     "Proposed mechanism: a 'just-in-time nitrogen' "
                     "protocol - small split doses keyed to sensor "
                     "readings, with inhibitors only where the ledger "
                     "shows leaching losses dominate. What would confirm "
                     "it: ledger farms sustaining yields at 60 to 70 "
                     "percent recovery with lower total nitrogen applied. "
                     "What would kill it: sensor readings that fail to "
                     "predict uptake across soil types, or labor and "
                     "logistics costs that exceed the fertilizer savings. "
                     "What it does NOT claim: that efficiency gains are "
                     "free, that inhibitors alone solve timing, or that "
                     "organic sources escape the same arithmetic."),
        "key_points": [
            "Global nitrogen-use efficiency sits near 40-50 percent; half the applied nitrogen is lost.",
            "About half the world's population is fed because of synthetic nitrogen fertilizer.",
            "The nitrogen cycle is one of the most transgressed planetary boundaries.",
            "4R practices, split doses, and inhibitors work in trials but stall on real farms.",
        ],
        "requirements": [
            "Dose only the next uptake window's nitrogen need, keyed to growth stage and sensors.",
            "Verify mid-season with a cheap canopy or leaf reading and log the recovery rate.",
            "Use inhibitors and coatings only where the ledger shows leaching dominates.",
        ],
        "standards": [
            "4R Nutrient Stewardship framework; Lassaletta et al. nitrogen-use efficiency trends.",
        ],
        "citations": CIT_BASE + [
            "Erisman JW et al. How a century of ammonia synthesis changed the "
            "world. Nature Geoscience; 2008.",
        ],
        "demo": {
            "calc": "ratio", "quantity": "Nitrogen applied per unit taken up",
            "unit": "kg applied / kg taken up", "formula": "applied_N / uptake_N",
            "assumptions": [
                ("Nitrogen applied per hectare", 180, [120, 180, 240]),
                ("Nitrogen recovered in harvest", 90, [60, 90, 120]),
            ],
            "checks": [((120, 60), 2.0, 1e-9),
                       ((240, 120), 2.0, 1e-9)],
            "steps": [
                "Step 1: record nitrogen applied and nitrogen recovered in harvest.",
                "Step 2: compute the applied-per-uptake ratio - the waste multiple.",
                "Step 3: identify which doses fell outside uptake windows.",
                "Step 4: re-time doses into the crop demand curve with sensor checks.",
                "Step 5: re-measure recovery and update the field ledger.",
            ],
            "confirm": [
                "Ledger farms hold yields at 60-70 percent recovery with less total nitrogen.",
                "Nitrate runoff and nitrous oxide fall in step with the ratio.",
            ],
            "refute": [
                "Sensor readings fail to predict uptake across soil types.",
                "Labor and logistics costs exceed the fertilizer savings.",
            ],
            "note": "Nitrogen waste-multiple explorer for just-in-time nitrogen.",
        },
    },
    # ------------------------------------------------- 4 FOUNDATIONS
    {
        "key": "peak-phosphorus",
        "name": "Peak Phosphorus and Closed Nutrient Loops",
        "group": "Foundations",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "problem": ("Phosphorus has no substitute in plant nutrition, no "
                    "atmospheric form to fix, and a finite mineable reserve, "
                    "yet modern farming runs it through fields once and "
                    "flushes most of it into rivers and seas. Cordell and "
                    "colleagues warned in 2009 that easily accessible rock "
                    "phosphate could peak this century, and reserves are "
                    "concentrated in a handful of countries, which makes "
                    "phosphorus both a resource-security and a pollution "
                    "problem. The unsolved challenge is closing the loop: "
                    "recovering phosphorus from manure, food waste, and "
                    "wastewater at a cost and purity farmers will accept, "
                    "and redesigning fertilizer use so soils are fed from "
                    "recycled stocks instead of mines."),
        "background": ("Phosphorus fertilizer comes overwhelmingly from "
                       "phosphate rock mined in Morocco and the Western "
                       "Sahara, China, and the United States, and the "
                       "'peak phosphorus' debate since 2009 has swung "
                       "between warnings of imminent scarcity and "
                       "reassurances that reserves will last centuries at "
                       "current rates. Both camps agree on the flow "
                       "problem: only a fraction of mined phosphorus ends "
                       "up in food, with the rest accumulating in soils, "
                       "eroding into waterways, or buried in landfills. "
                       "Recovery technologies exist - struvite "
                       "precipitation from wastewater, manure processing, "
                       "bone-meal and food-waste composting - but they "
                       "compete against cheap mined rock, face "
                       "contamination worries, and lack the collection "
                       "infrastructure that would make them routine."),
        "why_it_matters": ("Without phosphorus there are no crops, and "
                           "without closed loops the fertilizer system "
                           "depends on a depleting, geopolitically "
                           "concentrated mine. Every tonne recovered from "
                           "waste is a tonne not mined and a tonne not "
                           "feeding an algal bloom. Phosphorus is where "
                           "agriculture's linear economy is most visibly "
                           "unsustainable."),
        "sig_pointer": ("The Signature edition proposes a catchment-scale "
                        "phosphorus ledger that tracks every tonne from "
                        "mine or recovery plant to field to waterway, and "
                        "prices recovery against the true cost of mining "
                        "plus pollution. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) phosphorus flows can "
                     "be fully inventoried at catchment scale - imports, "
                     "manure, wastewater, crop offtake, losses; (2) "
                     "recovered phosphorus becomes competitive once the "
                     "avoided water-treatment cost and mine depletion are "
                     "priced in; (3) farmers adopt recovered products when "
                     "purity and price are guaranteed, not before. "
                     "Reasoning path: build the catchment ledger, find "
                     "where the largest recoverable flows are (usually "
                     "wastewater and concentrated livestock manure), "
                     "build recovery at those nodes first, and certify "
                     "output purity so farmers trust it like mined "
                     "product. Proposed mechanism: a 'phosphorus "
                     "circularity exchange' per catchment where "
                     "wastewater plants and livestock operations sell "
                     "certified recovered phosphorus into the same market "
                     "as mined fertilizer, with the ledger publishing "
                     "circularity rates. What would confirm it: catchments "
                     "where recovered phosphorus displaces mined imports "
                     "year over year while water phosphorus loads fall. "
                     "What would kill it: recovery costs that stay above "
                     "mined prices even with pollution priced in, or "
                     "contaminant scares that destroy farmer trust. What "
                     "it does NOT claim: that recovery alone meets demand "
                     "soon, or that 'peak phosphorus' timing is settled."),
        "key_points": [
            "Phosphorus is irreplaceable in plant nutrition and has no atmospheric source.",
            "Mineable reserves are finite and concentrated in a few countries.",
            "Most mined phosphorus is used once and lost to soils, waters, or landfills.",
            "Recovery technologies exist but lose to cheap mined rock without priced pollution.",
        ],
        "requirements": [
            "Inventory all phosphorus flows at catchment scale before building recovery.",
            "Build recovery first at the largest concentrated flows: wastewater and manure.",
            "Certify purity of recovered phosphorus so farmers trust it like mined product.",
        ],
        "standards": [
            "Cordell et al., Global Environmental Change 2009; EU Circular Economy fertilizer rules.",
        ],
        "citations": CIT_BASE + [
            "Cordell D, Drangert JO, White S. The story of phosphorus: global "
            "food security and food for thought. Global Environmental Change; "
            "2009.",
        ],
        "demo": {
            "calc": "sum", "quantity": "Phosphorus recovered toward a closed loop",
            "unit": "percent of applied P", "formula": "crop_uptake + manure_return + struvite_recovery",
            "assumptions": [
                ("Crop uptake share", 60, [40, 60, 80]),
                ("Manure return share", 15, [5, 15, 25]),
                ("Struvite recovery share", 8, [0, 8, 20]),
            ],
            "checks": [((40, 5, 0), 45, 1e-9),
                       ((80, 25, 20), 125, 1e-9)],
            "steps": [
                "Step 1: ledger all phosphorus flows in the catchment.",
                "Step  2: score crop uptake, manure return, and struvite recovery shares.",
                "Step 3: sum the recovered shares toward the 100-percent loop.",
                "Step 4: price recovery against mined rock plus avoided pollution.",
                "Step 5: expand the cheapest recovery node first.",
            ],
            "confirm": [
                "Recovered phosphorus displaces mined imports year over year.",
                "Water phosphorus loads fall as circularity rises.",
            ],
            "refute": [
                "Recovery costs stay above mined prices even with pollution priced in.",
                "Contaminant scares destroy farmer trust in recovered product.",
            ],
            "note": "Phosphorus circularity explorer for closing nutrient loops.",
        },
    },
    # ------------------------------------------------- 5 FOUNDATIONS
    {
        "key": "drought-proof-crops",
        "name": "Drought-Proof Staple Crops",
        "group": "Foundations",
        "ladder_rank": 5, "ladder_tier": "foundations",
        "problem": ("Drought is the single largest cause of cereal yield "
                    "loss worldwide, and breeding has never produced a "
                    "staple crop that truly shrugs off a serious drought. "
                    "Decades of work have delivered incremental gains - "
                    "deeper roots, quicker stomatal closure, stay-green "
                    "traits - but a drought that hits at flowering can still "
                    "wipe out a maize or rice crop in days. The unsolved "
                    "problem is physiological: drought tolerance and high "
                    "yield under good conditions trade off against each "
                    "other, because the same conservative water use that "
                    "survives a drought caps photosynthesis when water is "
                    "plentiful. Climate change is making rainfall more "
                    "erratic at the same time, which raises the value of a "
                    "breakthrough and the difficulty of achieving one."),
        "background": ("Drought breeding began in earnest in the 1970s and "
                       "1980s with programs selecting for yield under "
                       "managed water stress, and landmarks include "
                       "drought-tolerant maize for Africa from CIMMYT and "
                       "IITA, upland rice varieties from IRRI, and the "
                       "identification of major drought-response genes such "
                       "as DREB transcription factors in the 1990s. "
                       "Marker-assisted selection accelerated the work, and "
                       "more recently gene editing has let breeders tweak "
                       "stomatal and root traits directly. Yet field "
                       "results keep showing the same pattern: gains of 10 "
                       "to 20 percent under moderate stress, collapse "
                       "under severe stress, and a yield penalty in good "
                       "years for the most conservative varieties. Farmers "
                       "rationally choose the high-yielding variety and "
                       "gamble on rain, which is why adoption of "
                       "'drought-tolerant' seed stays below its promise."),
        "why_it_matters": ("Most of the world's staple calories are "
                           "rainfed, and rainfall is getting more erratic. "
                           "A genuinely drought-proof staple would be the "
                           "single most valuable seed trait on Earth - "
                           "worth more than any fertilizer - because it "
                           "converts climate risk into food security for "
                           "the poorest farmers first."),
        "sig_pointer": ("The Signature edition proposes breeding for "
                        "'stress-stage insurance' - scoring varieties by "
                        "their worst growth-stage yield, not their average, "
                        "and stacking stage-specific protections. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) drought damage is "
                     "stage-specific, with flowering the lethal window for "
                     "cereals; (2) a variety's value under erratic rain is "
                     "set by its worst stage, not its mean - the "
                     "weakest-link principle; (3) stage-specific traits "
                     "(root depth for vegetative, pollen protection for "
                     "flowering, remobilization for grain fill) can be "
                     "scored and stacked independently. Reasoning path: "
                     "score every candidate variety by minimum stage yield "
                     "under controlled stress, identify which stage sets "
                     "the minimum, add the trait that protects that "
                     "stage, and re-score - iterating the weakest link "
                     "upward. Proposed mechanism: a 'weakest-link "
                     "breeding index' that replaces average-stress yield "
                     "as the selection target, forcing breeding programs "
                     "to fix the lethal stage first. What would confirm "
                     "it: varieties selected on the index that hold yield "
                     "in bad years without the good-year penalty of "
                     "conservative types. What would kill it: stage "
                     "protections that always trade off against each "
                     "other, or stress timing so unpredictable that no "
                     "stage-specific stack helps. What it does NOT claim: "
                     "that any crop can survive a total rain failure, or "
                     "that breeding replaces water management."),
        "key_points": [
            "Drought is the largest single cause of cereal yield loss globally.",
            "Drought tolerance trades off against yield in good years - the core physiological bind.",
            "Decades of breeding deliver 10-20 percent gains under moderate stress, collapse under severe stress.",
            "Flowering is the lethal window: stress at anthesis can wipe out a crop in days.",
        ],
        "requirements": [
            "Score varieties by worst growth-stage yield under stress, not average yield.",
            "Fix the lethal stage first with stage-specific traits, then re-score.",
            "Verify no good-year yield penalty before release.",
        ],
        "standards": [
            "CIMMYT/IITA drought maize trials; IRRI drought rice breeding protocols.",
        ],
        "citations": CIT_BASE + [
            "CIMMYT. Drought-tolerant maize for Africa: breeding and adoption "
            "reports. Mexico (series).",
        ],
        "demo": {
            "calc": "min", "quantity": "Yield under the worst stress stage",
            "unit": "t/ha", "formula": "min(stage yields)",
            "assumptions": [
                ("Vegetative-stage yield under stress", 6.5, [5.0, 6.5, 7.5]),
                ("Flowering-stage yield under stress", 4.2, [3.0, 4.2, 6.0]),
                ("Grain-fill-stage yield under stress", 5.8, [4.5, 5.8, 7.0]),
            ],
            "checks": [((6.5, 3.0, 5.8), 3.0, 1e-9),
                       ((6.5, 6.0, 5.8), 5.8, 1e-9)],
            "steps": [
                "Step 1: stress-test the variety at each growth stage separately.",
                "Step 2: take the minimum - the weakest link sets the variety's value.",
                "Step 3: add the trait that protects the weakest stage.",
                "Step 4: re-score; the minimum should rise without good-year penalty.",
                "Step 5: release only when no stage is lethal.",
            ],
            "confirm": [
                "Index-selected varieties hold yield in bad years with no good-year penalty.",
                "Adoption rises because farmers no longer gamble on rain.",
            ],
            "refute": [
                "Stage protections always trade off against each other.",
                "Stress timing is so unpredictable that no stage stack helps.",
            ],
            "note": "Weakest-link drought explorer for stress-stage breeding.",
        },
    },
    # ------------------------------------------------- 6 FOUNDATIONS
    {
        "key": "soil-erosion",
        "name": "Soil Erosion: Losing Soil Faster Than It Forms",
        "group": "Foundations",
        "ladder_rank": 6, "ladder_tier": "foundations",
        "problem": ("Agriculture is losing soil 10 to 100 times faster than "
                    "new soil forms, which means farming is mining its own "
                    "foundation. David Montgomery's synthesis showed "
                    "typical soil formation rates of well under a tonne per "
                    "hectare per year while tilled fields erode at tens of "
                    "tonnes, and water erosion alone strips billions of "
                    "tonnes of topsoil annually. The unsolved problem is "
                    "not knowing how to stop erosion - cover crops, contour "
                    "plowing, terraces, and no-till all work - but making "
                    "conservation pay on the timescale a farmer lives on, "
                    "when the cost of erosion is diffuse and delayed and "
                    "the cost of prevention is immediate."),
        "background": ("The American Dust Bowl of the 1930s made erosion "
                       "the first great soil crisis of industrial "
                       "agriculture, and Hugh Hammond Bennett's campaign "
                       "created the Soil Conservation Service in 1935. "
                       "The technical answers have been known for nearly a "
                       "century: keep soil covered, slow water, disturb "
                       "less. No-till farming spread from the 1970s onward "
                       "and now covers well over 100 million hectares "
                       "globally, cutting erosion dramatically where it is "
                       "practiced well. Yet adoption stalls where it "
                       "matters most: on steep tropical slopes farmed by "
                       "the poor, where residue is needed for livestock "
                       "feed and fuel, herbicides for weed control are "
                       "unaffordable or unavailable, and a terrace built "
                       "today pays back over decades a tenant farmer may "
                       "not have."),
        "why_it_matters": ("Topsoil holds the nutrients, water, and biology "
                           "that crops live on, and it forms on geological "
                           "timescales. A civilization that erodes its "
                           "soil is borrowing against every future harvest. "
                           "Stopping erosion is the oldest unsolved problem "
                           "in agriculture, and still the most fundamental."),
        "sig_pointer": ("The Signature edition proposes pricing erosion "
                        "into the farm's annual accounts - a soil-capital "
                        "ledger where every tonne lost is booked as a cost, "
                        "so conservation competes fairly with this year's "
                        "yield. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) erosion can be "
                     "measured cheaply enough per field to ledger - "
                     "sediment traps, rill surveys, or calibrated models "
                     "tied to rainfall; (2) farmers respond to booked "
                     "costs, not to distant warnings; (3) soil formation "
                     "rates are effectively zero on human timescales, so "
                     "any net loss is capital consumption. Reasoning path: "
                     "measure each field's erosion-to-formation multiple, "
                     "convert lost tonnes into replacement cost (nutrients "
                     "plus water-holding capacity), book it annually, and "
                     "let conservation practices bid against the booked "
                     "loss. Proposed mechanism: a 'soil-capital account' "
                     "per farm where erosion is depreciated like "
                     "machinery, making a cover crop or terrace legible "
                     "as an investment with a payback period instead of "
                     "a moral appeal. What would confirm it: farms where "
                     "booked erosion costs shift practice adoption and "
                     "measured erosion multiples fall toward one. What "
                     "would kill it: measurement costs that exceed the "
                     "booked losses on small farms, or farmers who "
                     "discount the future so steeply that no booked cost "
                     "changes behavior. What it does NOT claim: that "
                     "ledgers replace terracing and cover, or that "
                     "erosion can reach zero on steep land."),
        "key_points": [
            "Tilled fields erode 10-100 times faster than soil forms.",
            "Technical fixes - cover, contour, terraces, no-till - have been known for a century.",
            "No-till covers 100M+ hectares but stalls on steep tropical slopes farmed by the poor.",
            "The bind is economic: prevention costs now, erosion costs later and diffusely.",
        ],
        "requirements": [
            "Measure each field's erosion-to-formation multiple with cheap field methods.",
            "Book lost soil as an annual capital cost in the farm accounts.",
            "Let conservation practices bid against the booked loss on payback terms.",
        ],
        "standards": [
            "USDA soil loss tolerance (T values); Montgomery, PNAS 2007 synthesis.",
        ],
        "citations": CIT_BASE + [
            "Montgomery DR. Soil erosion and agricultural sustainability. "
            "Proceedings of the National Academy of Sciences; 2007.",
        ],
        "demo": {
            "calc": "ratio", "quantity": "Erosion vs formation multiple",
            "unit": "times formation rate", "formula": "erosion_rate / formation_rate",
            "assumptions": [
                ("Field erosion rate", 12, [5, 12, 30]),
                ("Soil formation rate", 0.5, [0.2, 0.5, 1.0]),
            ],
            "checks": [((5, 0.5), 10.0, 1e-9),
                       ((30, 0.2), 150.0, 1e-9)],
            "steps": [
                "Step 1: measure the field's annual erosion rate.",
                "Step 2: take the local soil formation rate as the baseline.",
                "Step 3: compute the multiple - how many years of formation one year of farming burns.",
                "Step 4: book the lost tonnes as a capital cost.",
                "Step 5: adopt the conservation practice with the fastest payback against that cost.",
            ],
            "confirm": [
                "Booked erosion costs shift practice adoption on pilot farms.",
                "Measured erosion multiples fall toward one where ledgers run.",
            ],
            "refute": [
                "Measurement costs exceed booked losses on small farms.",
                "Steep farmer discounting makes no booked cost change behavior.",
            ],
            "note": "Soil-capital explorer for the erosion multiple.",
        },
    },
    # ------------------------------------------------- 7 FOUNDATIONS
    {
        "key": "irrigation-water",
        "name": "Irrigation: Farming Drinks 70 Percent of Freshwater",
        "group": "Foundations",
        "ladder_rank": 7, "ladder_tier": "foundations",
        "problem": ("Agriculture withdraws roughly 70 percent of the "
                    "world's freshwater, and in many breadbaskets it "
                    "withdraws more than rivers and aquifers can renew. "
                    "Flood irrigation - still the dominant method - "
                    "delivers water with efficiencies as low as 40 "
                    "percent, losing the rest to evaporation, runoff, and "
                    "deep percolation. The unsolved problem is the "
                    "efficiency paradox: drip irrigation and precision "
                    "scheduling can cut water use per hectare "
                    "dramatically, but the saved water is often used to "
                    "expand irrigated area instead of restoring rivers "
                    "and aquifers, so basin-level consumption barely "
                    "falls. Technology exists; the accounting that would "
                    "turn efficiency into real savings does not."),
        "background": ("Large-scale irrigation built the Green Revolution: "
                       "the Indus, the North China Plain, the Ogallala, "
                       "and California's Central Valley became the "
                       "world's granaries on pumped water. FAO's AQUASTAT "
                       "documents agriculture's roughly 70-percent share "
                       "of withdrawals, and satellite gravimetry (GRACE) "
                       "since the 2000s has revealed the scale of "
                       "groundwater depletion beneath the biggest "
                       "irrigated regions. Drip irrigation, invented in "
                       "its modern form in Israel in the 1960s, can exceed "
                       "90 percent application efficiency, and soil-moisture "
                       "sensors plus weather-based scheduling add further "
                       "savings. Yet basin studies repeatedly find the "
                       "rebound effect: efficient farms pump the same "
                       "volume or more, because water saved is water that "
                       "can irrigate new land under most water rights."),
        "why_it_matters": ("Rivers are running dry, aquifers are falling, "
                           "and cities and ecosystems are competing with "
                           "farms for the same water. Feeding 10 billion "
                           "will need more crop per drop, not just more "
                           "drops - and efficiency that does not reduce "
                           "consumption is an illusion of progress."),
        "sig_pointer": ("The Signature edition proposes basin-level water "
                        "ledgers where efficiency gains are retired as "
                        "real savings - unpumped water credited back to "
                        "the aquifer - instead of being re-spent on new "
                        "land. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) what matters is "
                     "consumptive use at basin scale, not application "
                     "efficiency per field; (2) farmers expand irrigation "
                     "with saved water because water rights reward use, "
                     "not conservation; (3) unpumped water can be measured "
                     "and credited via metering plus satellite "
                     "verification. Reasoning path: ledger every farm's "
                     "withdrawals and consumption, convert efficiency "
                     "gains into quantified savings, and require that a "
                     "fixed share of savings be retired - legally "
                     "unpumpable - with the farmer paid for the retired "
                     "water. Proposed mechanism: a 'save-and-retire' "
                     "water market where efficiency upgrades generate "
                     "credits only when metered pumping actually falls, "
                     "and retired water is protected by the ledger. What "
                     "would confirm it: basins where efficiency programs "
                     "produce falling total pumping and stabilizing "
                     "water tables. What would kill it: water rights "
                     "regimes that cannot legally recognize retired "
                     "water, or metering costs that swamp the credit "
                     "value on small farms. What it does NOT claim: that "
                     "markets alone allocate water fairly, or that any "
                     "technology repeals the rebound effect without "
                     "accounting."),
        "key_points": [
            "Agriculture accounts for roughly 70 percent of global freshwater withdrawals.",
            "Flood irrigation efficiency can be as low as 40 percent; drip can exceed 90 percent.",
            "GRACE satellite data reveals large-scale groundwater depletion under major breadbaskets.",
            "The rebound effect: saved water is usually spent irrigating more land, not restoring aquifers.",
        ],
        "requirements": [
            "Ledger withdrawals and consumptive use at basin scale, not just field efficiency.",
            "Retire a fixed share of efficiency savings as legally unpumpable water.",
            "Pay farmers for retired water so conservation competes with expansion.",
        ],
        "standards": [
            "FAO AQUASTAT; GRACE satellite groundwater assessments.",
        ],
        "citations": CIT_BASE + [
            "FAO. AQUASTAT - FAO's Global Information System on Water and "
            "Agriculture. Rome (database).",
        ],
        "demo": {
            "calc": "sum", "quantity": "Stacked irrigation water savings",
            "unit": "percent of irrigation water", "formula": "drip_saves + scheduling_saves + deficit_irr_saves",
            "assumptions": [
                ("Drip conversion savings", 35, [20, 35, 50]),
                ("Sensor scheduling savings", 15, [5, 15, 25]),
                ("Deficit irrigation savings", 12, [0, 12, 20]),
            ],
            "checks": [((20, 5, 0), 25, 1e-9),
                       ((50, 25, 20), 95, 1e-9)],
            "steps": [
                "Step 1: meter current withdrawals and estimate consumptive use.",
                "Step 2: stack the savings from drip, scheduling, and deficit irrigation.",
                "Step 3: split savings between farm retention and basin retirement.",
                "Step 4: verify retired water with meters and satellite data.",
                "Step 5: pay the farmer for retired water and re-ledger annually.",
            ],
            "confirm": [
                "Efficiency programs produce falling total pumping and stabilizing water tables.",
                "Retired-water credits trade at prices that reward conservation.",
            ],
            "refute": [
                "Water rights cannot legally recognize retired water.",
                "Metering costs swamp credit value on small farms.",
            ],
            "note": "Save-and-retire water explorer for basin-level savings.",
        },
    },
    # ------------------------------------------------- 8 FOUNDATIONS
    {
        "key": "post-harvest-loss",
        "name": "Post-Harvest Loss: A Third of Food Never Eaten",
        "group": "Foundations",
        "ladder_rank": 8, "ladder_tier": "foundations",
        "problem": ("About a third of all food produced for people is "
                    "lost or wasted, and in developing regions most of it "
                    "is lost after harvest - to pests, mold, and rot in "
                    "storage - before it ever reaches a market. FAO "
                    "estimates put post-harvest losses for cereals in "
                    "sub-Saharan Africa at 10 to 20 percent or more, and "
                    "for fruits, vegetables, and roots far higher. The "
                    "unsolved problem is the 'last mile of the harvest': "
                    "hermetic storage bags, metal silos, cold chains, and "
                    "drying technologies all exist and pay for themselves "
                    "in trials, yet losses persist because the technologies "
                    "require upfront cash, trust, and market access that "
                    "smallholders lack at exactly the moment of harvest, "
                    "when they are cash-poorest."),
        "background": ("Post-harvest loss became a global agenda item with "
                       "FAO's 2011 'Global food losses and food waste' "
                       "study, which put the one-third figure on the map, "
                       "and with the African Union's Malabo Declaration "
                       "target of halving post-harvest losses by 2025. "
                       "The technical toolkit is mature: Purdue Improved "
                       "Crop Storage (PICS) triple-layer hermetic bags, "
                       "developed in the 1980s-2000s, kill storage insects "
                       "without chemicals; metal silos protect grain for "
                       "years; solar dryers and small cold rooms extend "
                       "shelf life. Adoption studies show the pattern "
                       "clearly: where farmers can buy the bag or silo on "
                       "credit and sell stored grain later at higher "
                       "prices, losses collapse; where harvest-time cash "
                       "pressure forces immediate sale, the grain - and "
                       "the investment case - never enters storage."),
        "why_it_matters": ("Every tonne saved after harvest is a tonne "
                           "that needed no extra land, water, or "
                           "fertilizer - the cheapest, cleanest food "
                           "there is. For smallholders, stored grain is "
                           "also food security and bargaining power: it "
                           "turns a forced harvest-time sale at rock-"
                           "bottom prices into a choice."),
        "sig_pointer": ("The Signature edition proposes harvest-time "
                        "storage credit - the stored grain itself as "
                        "collateral - so the cash constraint that blocks "
                        "storage disappears at the moment it binds. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the binding "
                     "constraint is harvest-time liquidity, not ignorance "
                     "of storage technology; (2) stored grain in "
                     "verifiable hermetic storage is sound collateral; "
                     "(3) post-harvest price rises reliably exceed "
                     "storage plus interest costs in most staple "
                     "markets. Reasoning path: offer the farmer storage "
                     "plus an immediate partial cash advance against the "
                     "stored grain, verify the store with a sealed-bag "
                     "or silo receipt, and let the farmer sell when "
                     "prices recover. Proposed mechanism: a "
                     "'harvest bridge' contract - bag or silo provided "
                     "now, cash advance now, grain sold later, with the "
                     "receipt as collateral and the price spread shared. "
                     "What would confirm it: adoption and loss rates in "
                     "bridge-contract villages versus control villages, "
                     "with farmer incomes rising. What would kill it: "
                     "price seasonality too weak to cover costs, or "
                     "default cascades if stored grain spoils despite "
                     "the technology. What it does NOT claim: that "
                     "credit fixes losses where there is no market to "
                     "sell into, or that storage replaces better drying "
                     "and handling."),
        "key_points": [
            "About a third of food produced is lost or wasted; much is lost after harvest.",
            "Cereal post-harvest losses in sub-Saharan Africa run 10-20 percent or more.",
            "Hermetic bags, metal silos, and dryers exist and pay for themselves in trials.",
            "The binding constraint is harvest-time cash: farmers sell immediately at low prices.",
        ],
        "requirements": [
            "Provide storage technology and a cash advance together at harvest time.",
            "Use the stored grain itself, verifiably sealed, as the collateral.",
            "Share the post-harvest price spread so the farmer gains from waiting.",
        ],
        "standards": [
            "FAO Global food losses and food waste 2011; AU Malabo Declaration loss targets.",
        ],
        "citations": CIT_BASE + [
            "FAO. Global food losses and food waste: extent, causes and "
            "prevention. Rome; 2011.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Food reaching consumers after losses",
            "unit": "Mt", "formula": "harvested * (1 - loss_pct/100)",
            "expr": "a0 * (1 - a1 / 100.0)",
            "assumptions": [
                ("Grain harvested", 4000, [3000, 4000, 5000]),
                ("Post-harvest loss percent", 33, [25, 33, 45]),
            ],
            "checks": [((3000, 25), 2250.0, 1e-9),
                       ((5000, 45), 2750.0, 1e-9)],
            "steps": [
                "Step 1: weigh the harvest and record current loss rates.",
                "Step 2: compute food reaching consumers after losses.",
                "Step 3: offer hermetic storage plus a harvest-time cash advance.",
                "Step 4: verify sealed storage and issue the grain receipt.",
                "Step 5: sell when prices recover and split the spread.",
            ],
            "confirm": [
                "Bridge-contract villages show lower losses and higher farmer incomes.",
                "Repayment rates stay high because the collateral is the grain itself.",
            ],
            "refute": [
                "Price seasonality is too weak to cover storage plus interest.",
                "Stored grain spoils despite the technology, triggering defaults.",
            ],
            "note": "Harvest-bridge explorer for post-harvest loss.",
        },
    },
    # ------------------------------------------------- 9 FOUNDATIONS
    {
        "key": "pesticide-resistance",
        "name": "Pesticide Resistance: The Arms Race",
        "group": "Foundations",
        "ladder_rank": 9, "ladder_tier": "foundations",
        "problem": ("Pests, weeds, and diseases evolve resistance to "
                    "pesticides faster than new chemistry arrives, and "
                    "the treadmill is accelerating. The International "
                    "Survey of Herbicide Resistant Weeds documents "
                    "resistance in hundreds of weed species to most major "
                    "herbicide modes of action, insecticide resistance "
                    "threatens malaria control and crop protection alike, "
                    "and fungicide resistance is rising in cereal "
                    "pathogens. The unsolved problem is evolutionary: "
                    "every pesticide is a selection pressure, resistance "
                    "is inevitable, and the industry pipeline of new "
                    "modes of action has slowed to a trickle - no major "
                    "new herbicide mode of action reached farmers for "
                    "decades. Farming needs a strategy for winning a race "
                    "it cannot win by chemistry alone."),
        "background": ("Resistance was first documented within years of "
                       "DDT's introduction in the 1940s, and Rachel "
                       "Carson's Silent Spring (1962) made the ecological "
                       "costs famous. Integrated pest management (IPM), "
                       "developed in the 1960s-70s, offered the "
                       "alternative: monitor pests, use thresholds, "
                       "rotate chemistry, preserve refuges of susceptible "
                       "pests to dilute resistance genes. The refuge "
                       "strategy famously delayed resistance to Bt crops "
                       "for years where it was enforced. But IPM is "
                       "knowledge-intensive and its benefits are "
                       "collective - one farmer's refuge protects the "
                       "neighbor's crop - so adoption lags, resistance "
                       "management is underfunded relative to new-product "
                       "development, and the newest tools (RNA "
                       "interference, gene drives) face regulatory and "
                       "ecological questions of their own."),
        "why_it_matters": ("When chemistry fails, yields fall and farmers "
                           "spray more of older, harsher products - or "
                           "lose the crop. Resistance already costs "
                           "billions annually and threatens the "
                           "effectiveness of the few tools organic and "
                           "conventional farmers share. An evolutionary "
                           "strategy for pest control is as fundamental "
                           "as the chemistry itself."),
        "sig_pointer": ("The Signature edition proposes managing "
                        "resistance as a shared evolutionary commons - "
                        "ledgers of selection pressure per landscape, with "
                        "refuges and rotations coordinated across farms. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) resistance risk in a "
                     "landscape is a function of total selection pressure "
                     "minus refuge dilution, and can be scored per season; "
                     "(2) individual farmers under-invest in resistance "
                     "management because the benefits spill over to "
                     "neighbors; (3) coordinated rotation and refuge "
                     "compliance can be verified cheaply (seed purchase "
                     "records, satellite refuge checks). Reasoning path: "
                     "score each landscape's resistance-risk multiplier "
                     "from chemistry use, refuge area, and rotation "
                     "history; coordinate the cheapest risk-reducing "
                     "actions across farms; verify compliance and "
                     "publish the landscape score. Proposed mechanism: a "
                     "'resistance commons ledger' where farms in a "
                     "landscape share one risk score, coordinated "
                     "rotations and refuges lower everyone's score, and "
                     "input suppliers offer discounts tied to the "
                     "landscape score - making cooperation pay. What "
                     "would confirm it: landscapes where the ledger runs "
                     "and resistance onset is delayed versus matched "
                     "controls. What would kill it: free-riding that "
                     "collapses cooperation, or verification costs that "
                     "exceed the delayed-resistance value. What it does "
                     "NOT claim: that resistance can be prevented "
                     "forever, or that coordination replaces new "
                     "chemistry."),
        "key_points": [
            "Hundreds of weed species resist most major herbicide modes of action.",
            "No major new herbicide mode of action reached farmers for decades.",
            "Every pesticide is a selection pressure; resistance is evolutionarily inevitable.",
            "Refuge strategies delayed Bt resistance where enforced; IPM adoption lags for lack of coordination.",
        ],
        "requirements": [
            "Score resistance risk per landscape from chemistry use, refuges, and rotations.",
            "Coordinate rotations and refuges across farms, not farm by farm.",
            "Verify compliance cheaply and publish the landscape score.",
        ],
        "standards": [
            "International Survey of Herbicide Resistant Weeds (Heap); IRAC resistance management guidelines.",
        ],
        "citations": CIT_BASE + [
            "Heap I. The International Survey of Herbicide Resistant Weeds "
            "(database, ongoing).",
        ],
        "demo": {
            "calc": "sum1", "quantity": "Landscape resistance-risk multiplier",
            "unit": "multiplier", "formula": "1 + selection_pressure + refuge_absence + rotation_gaps",
            "assumptions": [
                ("Selection pressure index", 0.6, [0.2, 0.6, 0.9]),
                ("Refuge absence index", 0.5, [0.1, 0.5, 0.8]),
                ("Rotation gap index", 0.4, [0.1, 0.4, 0.7]),
            ],
            "checks": [((0.2, 0.1, 0.1), 1.4, 1e-9),
                       ((0.9, 0.8, 0.7), 3.4, 1e-9)],
            "steps": [
                "Step 1: score the landscape's selection pressure from chemistry records.",
                "Step 2: score refuge absence and rotation gaps.",
                "Step 3: compute the resistance-risk multiplier.",
                "Step 4: coordinate the cheapest risk-reducing actions across farms.",
                "Step 5: verify compliance and republish the score each season.",
            ],
            "confirm": [
                "Ledger landscapes delay resistance onset versus matched controls.",
                "Input discounts tied to the score sustain cooperation.",
            ],
            "refute": [
                "Free-riding collapses cross-farm cooperation.",
                "Verification costs exceed the value of delayed resistance.",
            ],
            "note": "Resistance-commons explorer for the pesticide arms race.",
        },
    },
]

ENTRIES += [
    # ------------------------------------------------- 10 FOUNDATIONS
    {
        "key": "livestock-methane",
        "name": "Livestock Methane: The Enteric Fermentation Problem",
        "group": "Foundations",
        "ladder_rank": 10, "ladder_tier": "foundations",
        "problem": ("Cattle, sheep, and goats burp methane as a byproduct "
                    "of digesting grass, and that enteric fermentation is "
                    "one of the largest single sources of agricultural "
                    "greenhouse gases. FAO's 2013 assessment attributed "
                    "about 14.5 percent of human-caused emissions to "
                    "livestock supply chains, with enteric methane the "
                    "biggest piece. The unsolved problem is scale and "
                    "biology: over a billion ruminants, mostly in systems "
                    "where feed additives and intensive management are "
                    "impractical, and a rumen microbiome that has been "
                    "making methane for 50 million years. Feed additives "
                    "like 3-NOP and red seaweed cut methane sharply in "
                    "trials, but delivering a daily dose to grazing "
                    "animals across the world's rangelands remains "
                    "unsolved."),
        "background": ("Methane from livestock entered climate accounting "
                       "with the IPCC's early assessments, but the "
                       "landmark was FAO's 2006 'Livestock's Long Shadow' "
                       "and its 2013 successor 'Tackling Climate Change "
                       "Through Livestock', which put the 14.5 percent "
                       "figure and the mitigation potentials on record. "
                       "The science of the rumen advanced in parallel: "
                       "methanogenic archaea were identified as the "
                       "culprits, and inhibitors targeting their enzymes "
                       "- notably 3-nitrooxypropanol (3-NOP, "
                       "commercialized as Bovaer) - showed 30 percent "
                       "reductions in dairy trials, while the red seaweed "
                       "Asparagopsis showed even larger cuts in beef "
                       "trials. Regulatory approvals for 3-NOP began in "
                       "the 2020s in several regions. The gap is "
                       "delivery: additives work in feedlots and dairies "
                       "with total mixed rations, but most of the world's "
                       "ruminants graze extensively, where daily dosing "
                       "is logistically and economically out of reach."),
        "why_it_matters": ("Methane is short-lived but potent, so cutting "
                           "it cools the climate fast - within a decade, "
                           "unlike CO2 cuts. Livestock methane is the "
                           "largest agricultural methane source and the "
                           "most tractable fast lever in food-system "
                           "emissions. Solving delivery to grazing systems "
                           "would unlock the biggest near-term climate win "
                           "in agriculture."),
        "sig_pointer": ("The Signature edition proposes slow-release "
                        "rumen boluses and mineral-lick delivery that "
                        "dose grazing animals for months, paired with a "
                        "methane ledger that pays herders for verified "
                        "cuts. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the binding "
                     "constraint is delivery to grazing animals, not "
                     "inhibitor efficacy, which is proven in confined "
                     "systems; (2) a slow-release bolus or lick can hold "
                     "an effective dose for 3 to 6 months at a cost below "
                     "the carbon value of the avoided methane; (3) "
                     "methane cuts can be verified per herd with "
                     "periodic breath or barn sensors plus rumen "
                     "microbiome markers. Reasoning path: formulate the "
                     "proven inhibitors into long-acting boluses, verify "
                     "the dose curve in grazing trials, then pay herders "
                     "per verified tonne of avoided methane so the "
                     "economics work without feedlot infrastructure. "
                     "Proposed mechanism: a 'grazing methane ledger' - "
                     "bolus in, sensor verification out, carbon payment "
                     "per verified cut - that turns the world's "
                     "rangelands into a methane-mitigation asset. What "
                     "would confirm it: grazing trials showing sustained "
                     "30 percent cuts with bolus delivery and herder "
                     "incomes rising from carbon payments. What would "
                     "kill it: bolus dose curves that fade too fast in "
                     "real rumens, or verification costs that exceed "
                     "the carbon value per animal. What it does NOT "
                     "claim: that methane cuts excuse deforestation for "
                     "pasture, or that additives replace better grazing "
                     "management."),
        "key_points": [
            "Livestock supply chains account for about 14.5 percent of human-caused emissions (FAO 2013).",
            "Enteric fermentation is the largest piece; methane cools fast when cut.",
            "3-NOP and Asparagopsis seaweed cut methane sharply in confined trials.",
            "Delivery to grazing animals - most of the world's ruminants - is the unsolved step.",
        ],
        "requirements": [
            "Formulate proven inhibitors into 3-6 month slow-release boluses or licks.",
            "Verify cuts per herd with breath/barn sensors plus microbiome markers.",
            "Pay herders per verified tonne so the economics work without feedlots.",
        ],
        "standards": [
            "FAO Tackling Climate Change Through Livestock 2013; IPCC AR6 methane accounting.",
        ],
        "citations": CIT_BASE + [
            "Gerber PJ et al. Tackling climate change through livestock: a "
            "global assessment of emissions and mitigation opportunities. FAO; "
            "2013.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Annual enteric methane after mitigation",
            "unit": "Mt CH4", "formula": "head_M * per_head_kg / 1000 * (1 - mitigation_pct/100)",
            "expr": "a0 * a1 / 1000.0 * (1 - a2 / 100.0)",
            "assumptions": [
                ("Ruminant head count (millions)", 1500, [1000, 1500, 2000]),
                ("Methane per head per year (kg)", 55, [40, 55, 70]),
                ("Mitigation percent from delivery", 0, [0, 20, 40]),
            ],
            "checks": [((1000, 40, 0), 40.0, 1e-9),
                       ((2000, 70, 40), 84.0, 1e-9)],
            "steps": [
                "Step 1: count the herd and set per-head methane from diet data.",
                "Step 2: compute baseline enteric methane.",
                "Step 3: apply the mitigation percent from bolus delivery.",
                "Step 4: verify cuts with herd sensors.",
                "Step 5: pay per verified tonne through the grazing ledger.",
            ],
            "confirm": [
                "Grazing trials show sustained 30 percent cuts with bolus delivery.",
                "Herder incomes rise from carbon payments per verified cut.",
            ],
            "refute": [
                "Bolus dose curves fade too fast in real rumens.",
                "Verification costs exceed the carbon value per animal.",
            ],
            "note": "Grazing-methane ledger explorer for enteric fermentation.",
        },
    },
    # ------------------------------------------------- 11 FOUNDATIONS
    {
        "key": "pollinator-decline",
        "name": "Pollinator Decline and Crop Pollination",
        "group": "Foundations",
        "ladder_rank": 11, "ladder_tier": "foundations",
        "problem": ("About three-quarters of the world's leading food "
                    "crops benefit from animal pollination, and wild "
                    "pollinators are declining across much of the "
                    "farmed world. Klein and colleagues' 2007 synthesis "
                    "showed how dependent global food production is on "
                    "bees, flies, beetles, and other pollinators, while "
                    "monitoring since has documented steep losses - "
                    "habitat destruction, pesticides (especially "
                    "neonicotinoids), parasites like Varroa, and climate "
                    "shifts scrambling the timing of flowers and "
                    "foragers. The unsolved problem is economic "
                    "accounting: pollination is a free service worth "
                    "hundreds of billions, but no farmer is paid to "
                    "protect it and no market punishes its destruction, "
                    "so the service erodes farm by farm while yields of "
                    "pollinator-dependent crops quietly suffer."),
        "background": ("Pollination ecology matured in the 2000s with "
                       "global syntheses quantifying crop dependence, "
                       "and the alarm sharpened with colony collapse "
                       "disorder reports from 2006 onward and European "
                       "wild-bee monitoring showing widespread declines. "
                       "The IPBES 2016 assessment on pollinators "
                       "consolidated the evidence: pollinator declines "
                       "are real, drivers are multiple and interacting, "
                       "and the economic value of pollination runs to "
                       "hundreds of billions of dollars annually. Policy "
                       "responses have been partial - neonicotinoid "
                       "restrictions in the EU, pollinator habitat "
                       "programs in the US and UK - while the core "
                       "economic problem persists: the farmer who sprays "
                       "at bloom or plows the hedgerow captures the "
                       "private gain, and the pollination loss is shared "
                       "by the whole landscape."),
        "why_it_matters": ("Fruits, vegetables, nuts, and oilseeds - the "
                           "most nutritious and highest-value crops - are "
                           "the most pollinator-dependent. Losing "
                           "pollinators does not just cut yields; it "
                           "narrows diets toward wind-pollinated staples "
                           "and erodes the nutritional quality of the "
                           "food supply."),
        "sig_pointer": ("The Signature edition proposes landscape "
                        "pollination ledgers that score each farm's "
                        "contribution to pollinator habitat and pay for "
                        "verified pollination service. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) pollination service "
                     "to a landscape can be measured - pan traps, flower "
                     "visitation rates, and yield comparisons with "
                     "pollinator exclusion; (2) habitat area and pesticide "
                     "practice predict service levels well enough to "
                     "price; (3) farmers respond to payments for measured "
                     "service. Reasoning path: measure baseline "
                     "pollination service per landscape, score each "
                     "farm's habitat contribution and spray practices, "
                     "then pay farms per unit of verified service "
                     "delivered to neighboring crops. Proposed mechanism: "
                     "a 'pollination service market' where fruit and "
                     "vegetable growers buy verified pollination units "
                     "from habitat-providing neighbors, with the ledger "
                     "publishing service levels so the price reflects "
                     "real scarcity. What would confirm it: landscapes "
                     "where the market runs and pollinator-dependent "
                     "yields rise while pesticide-at-bloom use falls. "
                     "What would kill it: measurement costs that exceed "
                     "the service value, or mobile pollinators that make "
                     "farm-level attribution impossible. What it does NOT "
                     "claim: that markets replace pesticide regulation, "
                     "or that managed honeybees substitute for wild "
                     "pollinator diversity."),
        "key_points": [
            "About 75 percent of leading food crops benefit from animal pollination.",
            "Wild pollinators are declining from habitat loss, pesticides, parasites, and climate shifts.",
            "Pollination service is worth hundreds of billions but priced at zero.",
            "The most nutritious crops - fruits, vegetables, nuts - are the most dependent.",
        ],
        "requirements": [
            "Measure pollination service per landscape with traps, visitation, and exclusion trials.",
            "Score each farm's habitat contribution and spray practices.",
            "Pay farms per verified unit of pollination service delivered to neighbors.",
        ],
        "standards": [
            "IPBES 2016 pollinators assessment; Klein et al., Proc. R. Soc. B 2007.",
        ],
        "citations": CIT_BASE + [
            "Klein AM et al. Importance of pollinators in changing landscapes "
            "for world crops. Proceedings of the Royal Society B; 2007.",
        ],
        "demo": {
            "calc": "prod", "quantity": "Pollination-dependent yield share secured",
            "unit": "share of potential", "formula": "crop_dependence * pollinator_abundance * habitat_buffer",
            "assumptions": [
                ("Crop pollinator dependence", 0.35, [0.20, 0.35, 0.60]),
                ("Pollinator abundance index", 0.80, [0.40, 0.80, 1.00]),
                ("Habitat buffer index", 0.90, [0.50, 0.90, 1.00]),
            ],
            "checks": [((0.20, 0.40, 0.50), 0.04, 1e-9),
                       ((0.60, 1.00, 1.00), 0.60, 1e-9)],
            "steps": [
                "Step 1: measure the crop's pollinator dependence.",
                "Step 2: survey pollinator abundance in the landscape.",
                "Step 3: score the habitat buffer around fields.",
                "Step 4: multiply into the secured yield share.",
                "Step 5: pay habitat providers per verified service unit.",
            ],
            "confirm": [
                "Market landscapes show rising pollinator-dependent yields.",
                "Pesticide-at-bloom use falls where service is priced.",
            ],
            "refute": [
                "Measurement costs exceed the service value.",
                "Mobile pollinators make farm-level attribution impossible.",
            ],
            "note": "Pollination-service market explorer.",
        },
    },
    # ------------------------------------------------- 12 COMPOUNDED
    {
        "key": "nitrogen-fixing-cereals",
        "name": "Nitrogen-Fixing Cereals: Crops That Fertilize Themselves",
        "group": "Compounded",
        "ladder_rank": 12, "ladder_tier": "compounded",
        "problem": ("Legumes fix their own nitrogen with the help of "
                    "rhizobia bacteria, but cereals - the crops that feed "
                    "the world - cannot, and after half a century of "
                    "research no commercial nitrogen-fixing cereal "
                    "exists. The prize is enormous: cereals that fix even "
                    "a fraction of their nitrogen would slash fertilizer "
                    "demand, cut nitrous oxide emissions, and free "
                    "smallholders from fertilizer markets they cannot "
                    "afford. The unsolved problem is one of the hardest "
                    "in plant biology: nitrogenase, the enzyme that fixes "
                    "nitrogen, is destroyed by oxygen, yet cereal cells "
                    "run on oxygen-dependent photosynthesis - and "
                    "engineering the entire symbiotic signaling, "
                    "infection, and nodule-development program into a "
                    "non-legume has defeated every attempt so far."),
        "background": ("The dream dates to the 1970s, when the first "
                       "nitrogenase genes were characterized and "
                       "researchers imagined transferring them into "
                       "plants. Two schools emerged: the 'nodule' school, "
                       "trying to engineer legume-like symbiosis into "
                       "cereals (notably the Gates-funded ENSA project "
                       "and work at the John Innes Centre), and the "
                       "'direct' school, trying to express nitrogenase "
                       "in plant cells or organelles shielded from "
                       "oxygen. Progress has been real but partial: "
                       "key symbiotic signaling genes have been "
                       "identified, nitrogenase components have been "
                       "expressed in yeast and plant mitochondria, and "
                       "associative nitrogen-fixing bacteria are "
                       "commercially sold. But the full package - a "
                       "cereal that fixes agronomically meaningful "
                       "nitrogen, reliably, in the field - remains "
                       "undemonstrated, and skeptics note the energy "
                       "cost of fixation itself may limit the payoff."),
        "why_it_matters": ("A nitrogen-fixing cereal would be the "
                           "single most transformative crop trait ever "
                           "bred - bigger than dwarfing, bigger than "
                           "hybrid vigor. It would rewrite fertilizer "
                           "economics, pollution, and food security at "
                           "once. Its absence after fifty years is a "
                           "measure of how hard plant biology's "
                           "grand challenges really are."),
        "sig_pointer": ("The Signature edition proposes a staged "
                        "de-risking ladder - associative fixers first, "
                        "engineered symbiosis second, direct nitrogenase "
                        "last - with each stage required to pay "
                        "agronomically before the next is funded. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the fastest path to "
                     "field impact is the least ambitious biology that "
                     "still moves the needle - improved associative "
                     "bacteria beat perfect engineered nodules on "
                     "timeline; (2) each stage must demonstrate "
                     "agronomic nitrogen delivery in real fields, not "
                     "just gene expression; (3) the energy cost of "
                     "fixation sets a ceiling on how much nitrogen a "
                     "cereal can fix without yield penalty. Reasoning "
                     "path: stage one - optimize associative "
                     "nitrogen-fixing bacteria for cereals and measure "
                     "real nitrogen delivery; stage two - engineer "
                     "enhanced signaling so cereals host bacteria more "
                     "effectively; stage three - full nitrogenase "
                     "expression, attempted only with the delivery and "
                     "measurement infrastructure from stages one and "
                     "two. Proposed mechanism: a 'fixation ladder' "
                     "research program where funding advances only when "
                     "the current stage hits field-verified nitrogen "
                     "delivery targets, forcing the science toward "
                     "agronomy instead of publications. What would "
                     "confirm it: stage-one products delivering "
                     "measured nitrogen to cereals at scale, and "
                     "stage-two lines outperforming them. What would "
                     "kill it: the energy-cost ceiling proving that "
                     "meaningful fixation always costs more yield than "
                     "it is worth in cereals. What it does NOT claim: "
                     "that engineered fixation is near, or that it "
                     "would eliminate fertilizer rather than reduce it."),
        "key_points": [
            "No commercial nitrogen-fixing cereal exists after 50 years of research.",
            "Nitrogenase is destroyed by oxygen, clashing with photosynthetic cells.",
            "Two schools: engineered legume-like symbiosis vs direct nitrogenase expression.",
            "Associative nitrogen-fixing bacteria are sold commercially but deliver modest nitrogen.",
        ],
        "requirements": [
            "Stage the research: associative fixers first, engineered symbiosis second, direct nitrogenase last.",
            "Require field-verified nitrogen delivery, not just gene expression, to advance stages.",
            "Respect the energy-cost ceiling: fixation must not cost more yield than it is worth.",
        ],
        "standards": [
            "ENSA project milestones; John Innes Centre symbiosis engineering criteria.",
        ],
        "citations": CIT_BASE + [
            "Beatty PH, Good AG. Future prospects for cereals that fix "
            "nitrogen. Science; 2011.",
        ],
        "demo": {
            "calc": "gain", "quantity": "Yield of nitrogen-fixing cereal line",
            "unit": "t/ha", "formula": "baseline_yield / (1 - n_fix_gain)",
            "planck": 5.0, "f_base": 0.0,
            "assumptions": [
                ("Effective fixed-nitrogen gain factor", 0.30, [0.10, 0.30, 0.50]),
            ],
            "checks": [((0.10,), 5.555556, 1e-6),
                       ((0.50,), 10.0, 1e-9)],
            "steps": [
                "Step 1: set the baseline cereal yield without fixation.",
                "Step 2: set the effective nitrogen gain from the fixation stage.",
                "Step 3: compute the yield through the gain formula.",
                "Step 4: check the gain against the energy-cost ceiling.",
                "Step 5: advance the research stage only on field-verified delivery.",
            ],
            "confirm": [
                "Stage-one products deliver measured nitrogen to cereals at scale.",
                "Stage-two engineered lines outperform associative bacteria in the field.",
            ],
            "refute": [
                "The energy-cost ceiling makes meaningful fixation uneconomic in cereals.",
                "Field delivery never matches controlled-condition nitrogen fixation.",
            ],
            "note": "Fixation-ladder explorer for nitrogen-fixing cereals.",
        },
    },
    # ------------------------------------------------- 13 COMPOUNDED
    {
        "key": "c4-rice",
        "name": "C4 Rice: Rebuilding Photosynthesis",
        "group": "Compounded",
        "ladder_rank": 13, "ladder_tier": "compounded",
        "problem": ("Rice uses C3 photosynthesis, an ancient and wasteful "
                    "system that loses a large share of fixed carbon to "
                    "photorespiration, while maize and sorghum use the C4 "
                    "system, which concentrates CO2 and is roughly 50 "
                    "percent more efficient. Converting rice to C4 could "
                    "raise yields by a third or more with less water and "
                    "nitrogen - but C4 is not a single gene; it is a "
                    "complex anatomy of specialized bundle-sheath cells, "
                    "transporters, and enzymes that took nature millions "
                    "of years to evolve. The C4 Rice Project at IRRI has "
                    "pursued it since 2008 with major funding, yet a "
                    "fully functional C4 rice remains unbuilt, making it "
                    "a defining test of whether plant engineering can "
                    "outrun evolution."),
        "background": ("C4 photosynthesis evolved independently more than "
                       "60 times in nature, always by rewiring leaf "
                       "anatomy (Kranz anatomy) plus biochemistry. The "
                       "C4 Rice Project, launched at the International "
                       "Rice Research Institute in 2008 with Gates "
                       "Foundation support, set out to install the full "
                       "system in rice - the most ambitious plant "
                       "engineering project ever attempted. Milestones "
                       "have accumulated: C4 enzymes expressed in rice, "
                       "increased vein density, partial CO2-concentrating "
                       "mechanisms in model plants. But the integrated "
                       "system - anatomy plus biochemistry plus regulation "
                       "working together to actually concentrate CO2 "
                       "around Rubisco in a rice leaf - has not been "
                       "demonstrated, and each added component interacts "
                       "with the others in ways that are hard to predict."),
        "why_it_matters": ("Rice feeds half of humanity, and a 30-plus "
                           "percent yield jump with lower water and "
                           "nitrogen demand would transform food security "
                           "in Asia and Africa. More profoundly, C4 rice "
                           "would prove that humanity can redesign "
                           "photosynthesis itself - opening every crop "
                           "to the same upgrade."),
        "sig_pointer": ("The Signature edition proposes building C4 in "
                        "measured modules - biochemistry, anatomy, "
                        "regulation - with each module required to show a "
                        "standalone efficiency gain before integration. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) C4's efficiency gain "
                     "decomposes into separable modules - the biochemical "
                     "pump, Kranz-like anatomy, and regulatory tuning - "
                     "that can be built and tested independently; (2) a "
                     "module that shows no standalone gain will not "
                     "magically gain one in combination; (3) partial C4 "
                     "systems have agronomic value even before the full "
                     "system works. Reasoning path: build each module in "
                     "rice, measure its standalone effect on "
                     "photorespiration and water-use efficiency, keep "
                     "only modules that pay, then integrate the paying "
                     "modules stepwise with a measurement gate at each "
                     "integration. Proposed mechanism: a 'module ledger' "
                     "for the C4 build where every genetic change is "
                     "scored for standalone gain, and integration "
                     "proceeds only through modules with positive "
                     "ledgers - plus release of the best partial-C4 "
                     "lines as products in their own right. What would "
                     "confirm it: module lines with measured efficiency "
                     "gains, and integrated lines that concentrate CO2 "
                     "around Rubisco in a rice leaf. What would kill it: "
                     "modules that only work in combination, making "
                     "stepwise measurement impossible, or anatomical "
                     "changes that rice development fundamentally "
                     "resists. What it does NOT claim: that C4 rice is "
                     "near, or that it would suit all rice environments."),
        "key_points": [
            "C4 photosynthesis is roughly 50 percent more efficient than rice's C3 system.",
            "C4 is a full anatomical and biochemical system, not a single gene.",
            "The IRRI C4 Rice Project has run since 2008 without a fully functional C4 rice.",
            "Partial modules may have standalone agronomic value before the full system works.",
        ],
        "requirements": [
            "Build C4 as separable modules: biochemistry, anatomy, regulation.",
            "Require each module to show standalone efficiency gain before integration.",
            "Release the best partial-C4 lines as products, not just stepping stones.",
        ],
        "standards": [
            "C4 Rice Project (IRRI) module milestones; Kranz anatomy benchmarks.",
        ],
        "citations": CIT_BASE + [
            "Hibberd JM, Sheehy JE, Langdale JA. Using C4 photosynthesis to "
            "increase the yield of rice - rationale and feasibility. Current "
            "Opinion in Plant Biology; 2008.",
        ],
        "demo": {
            "calc": "sum1", "quantity": "Photosynthetic efficiency gain from C4 modules",
            "unit": "multiplier", "formula": "1 + co2_gain + photoresp_cut + canopy_gain",
            "assumptions": [
                ("CO2-concentration gain", 0.30, [0.10, 0.30, 0.50]),
                ("Photorespiration cut", 0.25, [0.10, 0.25, 0.40]),
                ("Canopy architecture gain", 0.10, [0.00, 0.10, 0.20]),
            ],
            "checks": [((0.10, 0.10, 0.00), 1.20, 1e-9),
                       ((0.50, 0.40, 0.20), 2.10, 1e-9)],
            "steps": [
                "Step 1: score the biochemical pump module's standalone gain.",
                "Step 2: score the anatomical module's standalone gain.",
                "Step 3: score the regulatory tuning module's standalone gain.",
                "Step 4: sum the paying modules into the efficiency multiplier.",
                "Step 5: integrate stepwise with a measurement gate at each step.",
            ],
            "confirm": [
                "Module lines show measured standalone efficiency gains.",
                "Integrated lines concentrate CO2 around Rubisco in rice leaves.",
            ],
            "refute": [
                "Modules only work in combination, defeating stepwise measurement.",
                "Rice development fundamentally resists the anatomical changes.",
            ],
            "note": "C4 module-ledger explorer for rebuilding photosynthesis.",
        },
    },
    # ------------------------------------------------- 14 COMPOUNDED
    {
        "key": "soil-microbiome",
        "name": "Managing the Soil Microbiome",
        "group": "Compounded",
        "ladder_rank": 14, "ladder_tier": "compounded",
        "problem": ("A teaspoon of healthy soil holds more microbes than "
                    "there are people on Earth, and those microbes govern "
                    "nutrient cycling, disease suppression, and soil "
                    "structure - yet farming manages them mostly by "
                    "accident. The soil microbiome is the least understood "
                    "and least managed part of agriculture: thousands of "
                    "interacting species, most unculturable, responding to "
                    "every tillage pass, fertilizer dose, and crop choice "
                    "in ways science cannot yet predict. Commercial "
                    "'biologicals' - microbial inoculants - are a "
                    "booming market with inconsistent field results, "
                    "because a microbe that thrives in a greenhouse "
                    "often fails to establish in a living soil already "
                    "occupied by competitors."),
        "background": ("Soil microbiology was revolutionized by DNA "
                       "sequencing in the 2000s-2010s, which revealed the "
                       "staggering diversity that culturing had missed - "
                       "the Earth Microbiome Project and similar efforts "
                       "catalogued tens of thousands of soil taxa. "
                       "Landmark findings followed: the rhizosphere "
                       "microbiome shapes plant health as strongly as "
                       "genetics in some trials, mycorrhizal networks move "
                       "nutrients between plants, and suppressive soils "
                       "that naturally resist pathogens are microbially "
                       "mediated. The commercial response - microbial seed "
                       "treatments and soil inoculants from startups and "
                       "agribusiness - has grown into a multi-billion-"
                       "dollar market. But field efficacy remains the "
                       "industry's open wound: establishment failure is "
                       "common, effects are context-dependent, and "
                       "regulation lags behind marketing claims."),
        "why_it_matters": ("The microbiome is the engine room of soil "
                           "fertility. Managing it deliberately could cut "
                           "fertilizer and pesticide needs while building "
                           "soil health - or, mismanaged through hype, "
                           "could waste billions on products that do not "
                           "work. The difference is measurement."),
        "sig_pointer": ("The Signature edition proposes managing the "
                        "microbiome by outcomes - diversity, activity, and "
                        "disease suppression measured in the field - "
                        "rather than by which microbes are added. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) what matters "
                     "agronomically is microbiome function - nutrient "
                     "cycling rate, pathogen suppression, aggregate "
                     "stability - not the species list; (2) function can "
                     "be measured cheaply enough per field with enzyme "
                     "assays, respiration tests, and disease bioassays; "
                     "(3) management (rotation, cover, tillage, organic "
                     "inputs) shifts function more reliably than "
                     "inoculants do. Reasoning path: baseline each "
                     "field's microbiome function scores, apply "
                     "management changes or inoculants, re-measure "
                     "function, and keep only interventions that move "
                     "the scores - a function ledger per field. "
                     "Proposed mechanism: a 'microbiome function index' "
                     "reported alongside soil tests, with biological "
                     "products required to show index movement in "
                     "independent field trials before claims are "
                     "allowed. What would confirm it: fields where "
                     "index-guided management cuts fertilizer and "
                     "pesticide use while holding yield, and inoculants "
                     "that move the index consistently. What would kill "
                     "it: function assays too noisy or costly for field "
                     "use, or microbiomes so context-specific that no "
                     "index generalizes. What it does NOT claim: that "
                     "the species-level science is settled, or that "
                     "inoculants never work."),
        "key_points": [
            "A teaspoon of soil holds more microbes than there are people on Earth.",
            "The microbiome governs nutrient cycling, disease suppression, and soil structure.",
            "Most soil microbes are unculturable; field behavior is hard to predict.",
            "Commercial biologicals boom while field efficacy stays inconsistent.",
        ],
        "requirements": [
            "Manage by measured function - cycling, suppression, structure - not species lists.",
            "Baseline each field's microbiome function scores before intervening.",
            "Require biological products to move the index in independent trials before claims.",
        ],
        "standards": [
            "Earth Microbiome Project protocols; enzyme/respiration assay standards.",
        ],
        "citations": CIT_BASE + [
            "Berendsen RL, Pieterse CMJ, Bakker PAHM. The rhizosphere "
            "microbiome and plant health. Trends in Plant Science; 2012.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Microbiome function management score",
            "unit": "index", "formula": "diversity * activity + legacy_bonus",
            "expr": "a0 * a1 + a2",
            "assumptions": [
                ("Microbial diversity index", 0.70, [0.30, 0.70, 0.95]),
                ("Microbial activity index", 0.60, [0.20, 0.60, 0.90]),
                ("Legacy carbon bonus", 0.20, [0.00, 0.20, 0.50]),
            ],
            "checks": [((0.30, 0.20, 0.00), 0.06, 1e-9),
                       ((0.95, 0.90, 0.50), 1.355, 1e-6)],
            "steps": [
                "Step 1: baseline the field's diversity and activity scores.",
                "Step 2: add the legacy carbon bonus from soil organic matter.",
                "Step 3: compute the microbiome function score.",
                "Step 4: apply management or inoculant and re-measure.",
                "Step 5: keep only interventions that move the score.",
            ],
            "confirm": [
                "Index-guided fields cut inputs while holding yield.",
                "Some inoculants move the index consistently across sites.",
            ],
            "refute": [
                "Function assays prove too noisy or costly for field use.",
                "No index generalizes across soil contexts.",
            ],
            "note": "Microbiome function-index explorer.",
        },
    },
    # ------------------------------------------------- 15 COMPOUNDED
    {
        "key": "heat-sterility",
        "name": "Heat Sterility: When Heat Waves Strike Flowering",
        "group": "Compounded",
        "ladder_rank": 15, "ladder_tier": "compounded",
        "problem": ("A few days of extreme heat during flowering can "
                    "sterilize a rice or wheat crop even when the plants "
                    "look healthy - pollen dies, grain never forms, and "
                    "the season is lost. Researchers including Krishna "
                    "Jagadish showed that rice spikelet fertility "
                    "collapses above about 35 degrees Celsius during "
                    "anthesis, and similar thresholds afflict wheat and "
                    "maize. The unsolved problem is that heat tolerance "
                    "at flowering is genetically complex, hard to screen "
                    "for, and often disconnected from vegetative heat "
                    "tolerance - a variety can survive heat as a plant "
                    "and still fail as a parent. With heat waves "
                    "intensifying, flowering-stage sterility is becoming "
                    "the dominant climate risk for cereals."),
        "background": ("The physiology was mapped in the 2000s-2010s: "
                       "high temperatures desiccate pollen, disrupt "
                       "anther dehiscence, and impair fertilization "
                       "within a narrow window of hours around anthesis. "
                       "Breeding programs began screening for spikelet "
                       "fertility under controlled heat, and donors of "
                       "tolerance were identified in rice germplasm. But "
                       "progress is slow because the trait is "
                       "polygenic, screening requires precise heat "
                       "chambers timed to flowering, and field heat "
                       "waves are unpredictable in timing and duration. "
                       "Meanwhile climate models project sharp increases "
                       "in the frequency of flowering-stage heat stress "
                       "across South Asia's rice-wheat systems and other "
                       "breadbaskets within decades."),
        "why_it_matters": ("Yield losses from heat sterility arrive "
                           "suddenly and completely - a farmer can lose "
                           "everything in a week. As heat waves "
                           "intensify, this single trait may determine "
                           "whether tropical cereal systems remain viable "
                           "where hundreds of millions farm."),
        "sig_pointer": ("The Signature edition proposes screening "
                        "directly for pollen survival under heat - the "
                        "mechanism itself - rather than for yield under "
                        "vague 'heat stress'. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) flowering-stage "
                     "sterility is dominated by pollen viability under "
                     "heat, which is measurable directly and cheaply; "
                     "(2) selecting on the mechanism (pollen survival) "
                     "is faster than selecting on the outcome (yield "
                     "under heat); (3) early-morning flowering - which "
                     "escapes peak heat - is a heritable avoidance "
                     "trait worth stacking with tolerance. Reasoning "
                     "path: screen germplasm for pollen viability after "
                     "controlled heat shock at anthesis, select the "
                     "survivors, stack with early-morning flowering, and "
                     "validate in field heat-wave trials. Proposed "
                     "mechanism: a 'pollen-first' breeding pipeline "
                     "where every candidate is scored for heat-shocked "
                     "pollen viability before any yield trial, cutting "
                     "years from the selection cycle. What would confirm "
                     "it: pollen-selected lines that hold spikelet "
                     "fertility through real heat waves. What would kill "
                     "it: pollen viability that fails to predict field "
                     "fertility, or tolerance genes with unacceptable "
                     "linkage drag. What it does NOT claim: that any "
                     "variety survives unlimited heat, or that breeding "
                     "replaces shifting sowing dates and irrigation."),
        "key_points": [
            "Rice spikelet fertility collapses above about 35 C during anthesis.",
            "A plant can survive heat vegetatively and still fail reproductively.",
            "Heat tolerance at flowering is polygenic and hard to screen.",
            "Heat waves are intensifying across South Asia's rice-wheat systems.",
        ],
        "requirements": [
            "Screen germplasm directly for pollen viability after heat shock at anthesis.",
            "Stack tolerance with early-morning flowering as a heat-avoidance trait.",
            "Validate selections in real field heat-wave trials.",
        ],
        "standards": [
            "IRRI heat-tolerance screening protocols; controlled anthesis heat-shock assays.",
        ],
        "citations": CIT_BASE + [
            "Jagadish SVK et al. Heat stress during flowering in cereals: "
            "effects and adaptation. (series of rice heat-tolerance studies, "
            "IRRI).",
        ],
        "demo": {
            "calc": "min", "quantity": "Fertile fraction across heat windows",
            "unit": "share", "formula": "min(window fertilities)",
            "assumptions": [
                ("Pre-anthesis fertility under heat", 0.95, [0.80, 0.95, 1.00]),
                ("Anthesis fertility under heat", 0.55, [0.20, 0.55, 0.90]),
                ("Post-anthesis fertility under heat", 0.90, [0.70, 0.90, 1.00]),
            ],
            "checks": [((0.95, 0.20, 0.90), 0.20, 1e-9),
                       ((0.95, 0.90, 0.90), 0.90, 1e-9)],
            "steps": [
                "Step 1: heat-shock pollen at each flowering window.",
                "Step 2: take the minimum fertility - the lethal window sets the line's value.",
                "Step 3: select for pollen survival in the weakest window.",
                "Step 4: stack with early-morning flowering avoidance.",
                "Step 5: validate through real field heat waves.",
            ],
            "confirm": [
                "Pollen-selected lines hold spikelet fertility through real heat waves.",
                "Selection cycles shorten versus yield-based heat screening.",
            ],
            "refute": [
                "Pollen viability fails to predict field fertility.",
                "Tolerance genes carry unacceptable linkage drag.",
            ],
            "note": "Pollen-first heat explorer for flowering-stage sterility.",
        },
    },
    # ------------------------------------------------- 16 COMPOUNDED
    {
        "key": "salinity-intrusion",
        "name": "Salinity Intrusion in Coastal Farmland",
        "group": "Compounded",
        "ladder_rank": 16, "ladder_tier": "compounded",
        "problem": ("Sea-level rise is pushing saltwater into some of the "
                    "world's most productive coastal farmland - the "
                    "Mekong and Ganges-Brahmaputra deltas, the Nile "
                    "delta, Bangladesh's coast - while irrigation without "
                    "drainage salinizes soils inland. FAO estimates "
                    "about a fifth of irrigated land is salt-affected, "
                    "and rice, the staple of the deltas, is "
                    "salt-sensitive at exactly the seedling and "
                    "flowering stages. The unsolved problem is "
                    "compounding: salt-tolerant varieties exist but yield "
                    "less, drainage infrastructure is expensive and "
                    "unbuilt, and the sea keeps rising - so the "
                    "question is not just breeding but deciding which "
                    "land to defend, which to adapt, and which to "
                    "surrender."),
        "background": ("Salinity research accelerated as the scale became "
                       "clear: the Saltol QTL for rice salinity tolerance, "
                       "mapped in the 2000s, was bred into varieties now "
                       "grown on millions of hectares in South Asia, a "
                       "genuine success. But Saltol-class tolerance "
                       "handles moderate salinity; the advancing "
                       "seawater in delta regions brings levels beyond "
                       "what current varieties survive, and tolerance "
                       "mechanisms (salt exclusion, tissue tolerance) "
                       "each carry yield costs. Meanwhile "
                       "infrastructure - polders, sluices, drainage - "
                       "decays or was never built, and in places like "
                       "coastal Bangladesh, farmers are already shifting "
                       "from rice to shrimp farming as the sea wins. The "
                       "science of tolerance is ahead of the strategy "
                       "for retreat."),
        "why_it_matters": ("Deltas feed hundreds of millions and are "
                           "sinking and salinizing simultaneously. "
                           "Getting the defend-adapt-retreat decision "
                           "wrong wastes billions on land the sea will "
                           "take, or abandons land that breeding and "
                           "drainage could have saved."),
        "sig_pointer": ("The Signature edition proposes a "
                        "defend-adapt-retreat ledger per coastal district "
                        "that prices each option against measured salinity "
                        "trajectories. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) salinity trajectories "
                     "per district are measurable and projectable from "
                     "tide gauges, groundwater monitoring, and sea-level "
                     "scenarios; (2) each option - defend (polders and "
                     "drainage), adapt (salt-tolerant varieties and "
                     "shrimp-rice systems), retreat (managed transition) "
                     "- has a knowable cost per protected hectare-year; "
                     "(3) decisions must be revisable as trajectories "
                     "change. Reasoning path: map the salinity "
                     "trajectory per district, price the three options "
                     "against it, choose the cheapest per "
                     "hectare-year of productive land, and re-ledger "
                     "every five years. Proposed mechanism: a coastal "
                     "land ledger that publishes each district's "
                     "trajectory and the priced options, forcing the "
                     "defend-adapt-retreat choice into the open instead "
                     "of drifting by default. What would confirm it: "
                     "districts where ledger-guided choices preserve "
                     "more productive land per dollar than ad-hoc "
                     "responses. What would kill it: salinity "
                     "trajectories too uncertain to price, or political "
                     "refusal to publish retreat options. What it does "
                     "NOT claim: that any ledger stops the sea, or that "
                     "retreat is avoidable everywhere."),
        "key_points": [
            "About a fifth of irrigated land is salt-affected (FAO).",
            "Sea-level rise salinizes the Mekong, Ganges-Brahmaputra, and Nile deltas.",
            "Saltol rice tolerance is a real success but handles only moderate salinity.",
            "The missing piece is strategy: defend vs adapt vs retreat, priced per district.",
        ],
        "requirements": [
            "Map and project salinity trajectories per coastal district.",
            "Price defend, adapt, and retreat per hectare-year of productive land.",
            "Re-ledger every five years and publish the options openly.",
        ],
        "standards": [
            "FAO salt-affected soils assessments; IPCC AR6 sea-level scenarios.",
        ],
        "citations": CIT_BASE + [
            "FAO. Salt-affected soils portal and global assessments. Rome.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Salt-free productive area remaining",
            "unit": "Mha", "formula": "coastal_farmland * (1 - salt_affected_pct/100)",
            "expr": "a0 * (1 - a1 / 100.0)",
            "assumptions": [
                ("Coastal farmland", 120, [80, 120, 160]),
                ("Salt-affected percent", 20, [10, 20, 40]),
            ],
            "checks": [((80, 10), 72.0, 1e-9),
                       ((160, 40), 96.0, 1e-9)],
            "steps": [
                "Step 1: map coastal farmland and current salt-affected share.",
                "Step 2: project the salinity trajectory from gauges and sea-level scenarios.",
                "Step 3: compute remaining productive area under each option.",
                "Step 4: price defend, adapt, and retreat per hectare-year.",
                "Step 5: choose, publish, and re-ledger every five years.",
            ],
            "confirm": [
                "Ledger-guided districts preserve more productive land per dollar.",
                "Retreat decisions happen by plan instead of by disaster.",
            ],
            "refute": [
                "Salinity trajectories prove too uncertain to price options.",
                "Politics blocks publication of retreat options.",
            ],
            "note": "Defend-adapt-retreat explorer for coastal salinity.",
        },
    },
    # ------------------------------------------------- 17 COMPOUNDED
    {
        "key": "groundwater-depletion",
        "name": "Falling Water Tables and Groundwater Depletion",
        "group": "Compounded",
        "ladder_rank": 17, "ladder_tier": "compounded",
        "problem": ("The aquifers beneath the North China Plain, the "
                    "Indo-Gangetic Plain, and the Ogallala are falling by "
                    "meters per year, and the grain they irrigate feeds "
                    "billions. Gleeson and colleagues' 2012 Nature "
                    "analysis put the global groundwater footprint at 3.5 "
                    "times the actual aquifer area - humanity pumps far "
                    "beyond recharge. The unsolved problem is governance: "
                    "groundwater is invisible, unmetered, and effectively "
                    "open-access in most of the world, so every farmer's "
                    "rational choice is to pump before the neighbor does. "
                    "Technology for recharge and efficient use exists; "
                    "the institutions that would make pumping sustainable "
                    "mostly do not."),
        "background": ("Groundwater irrigation exploded from the 1970s "
                       "with cheap pumps and rural electrification - "
                       "India alone has tens of millions of tube wells, "
                       "the world's largest groundwater irrigation "
                       "economy. The GRACE satellites, launched in 2002, "
                       "made depletion visible from space, showing "
                       "alarming losses over northwest India, the North "
                       "China Plain, and California's Central Valley. "
                       "Responses have been tried: electricity rationing "
                       "for pumps in parts of India, managed aquifer "
                       "recharge in the US and Australia, water markets "
                       "in a few basins. But metering remains rare, "
                       "rights are undefined, and recharge can only "
                       "offset a fraction of current overdraft - the "
                       "arithmetic requires pumping less, which requires "
                       "governing the invisible."),
        "why_it_matters": ("When the wells run dry, the grain stops - "
                           "and there is no second aquifer underneath. "
                           "Depletion is a slow-motion crisis measured in "
                           "decades, which makes it politically invisible "
                           "until wells fail. The breadbaskets at risk "
                           "feed a large share of humanity."),
        "sig_pointer": ("The Signature edition proposes aquifer "
                        "accounts with declining pumping budgets per "
                        "farmer, metered and tradable, so the invisible "
                        "becomes ledgered. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) aquifer storage and "
                     "recharge can be estimated well enough per basin - "
                     "GRACE plus well monitoring plus hydrology - to set "
                     "a sustainable pumping budget; (2) farmers accept "
                     "budgets they help set far more than ones imposed; "
                     "(3) tradable budgets move water to its highest-"
                     "value use, softening the cut. Reasoning path: "
                     "assess the aquifer's safe yield, allocate declining "
                     "pumping budgets per farmer over a 20-year glide "
                     "path, meter withdrawals, allow trading, and let "
                     "the ledger publish each farm's balance. Proposed "
                     "mechanism: an 'aquifer account' per farmer - "
                     "annual pumping budget, metered use, tradable "
                     "surplus - with the basin budget ratcheting down "
                     "to recharge on a published schedule. What would "
                     "confirm it: basins where accounts stabilize water "
                     "tables while farm incomes hold through trading and "
                     "efficiency. What would kill it: metering costs or "
                     "political resistance that keep pumping unmeasured, "
                     "or recharge estimates too uncertain to set "
                     "credible budgets. What it does NOT claim: that "
                     "budgets alone create alternative livelihoods, or "
                     "that every depleted aquifer can recover."),
        "key_points": [
            "The global groundwater footprint is 3.5 times actual aquifer area (Gleeson et al. 2012).",
            "Water tables fall meters per year under major breadbaskets.",
            "Groundwater is mostly unmetered and open-access - a classic commons problem.",
            "GRACE satellites made depletion visible from space since 2002.",
        ],
        "requirements": [
            "Set a sustainable basin pumping budget from storage, recharge, and monitoring.",
            "Allocate declining per-farmer budgets on a published 20-year glide path.",
            "Meter withdrawals, allow trading, and publish every farm's balance.",
        ],
        "standards": [
            "GRACE groundwater assessments; Gleeson et al., Nature 2012 footprint method.",
        ],
        "citations": CIT_BASE + [
            "Gleeson T et al. Water balance of global aquifers revealed by "
            "groundwater footprint. Nature; 2012.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Aquifer storage after the planning horizon",
            "unit": "km3", "formula": "storage_now - deficit_rate * years",
            "expr": "a0 - a1 * a2",
            "assumptions": [
                ("Current aquifer storage", 400, [200, 400, 600]),
                ("Annual overdraft (deficit rate)", 15, [5, 15, 25]),
                ("Planning horizon (years)", 20, [10, 20, 30]),
            ],
            "checks": [((200, 5, 10), 150.0, 1e-9),
                       ((600, 25, 30), -150.0, 1e-9)],
            "steps": [
                "Step 1: estimate current storage and the annual overdraft.",
                "Step 2: project storage at the planning horizon under business as usual.",
                "Step 3: set the sustainable budget and the glide path down to it.",
                "Step 4: allocate metered, tradable per-farmer accounts.",
                "Step 5: publish balances and ratchet the basin budget on schedule.",
            ],
            "confirm": [
                "Account basins stabilize water tables while farm incomes hold.",
                "Trading moves water to higher-value uses, softening the cuts.",
            ],
            "refute": [
                "Metering costs or politics keep pumping unmeasured.",
                "Recharge estimates are too uncertain for credible budgets.",
            ],
            "note": "Aquifer-account explorer for groundwater depletion.",
        },
    },
    # ------------------------------------------------- 18 COMPOUNDED
    {
        "key": "narrow-genetic-base",
        "name": "The Narrow Genetic Base: Monoculture Vulnerability",
        "group": "Compounded",
        "ladder_rank": 18, "ladder_tier": "compounded",
        "problem": ("A handful of varieties now dominate each major crop "
                    "across entire continents, and that uniformity is an "
                    "invitation to catastrophe. The Irish potato famine "
                    "is the classic warning - one susceptible variety, "
                    "one pathogen, one million dead - and modern "
                    "agriculture has repeated the pattern at larger "
                    "scale: the Cavendish banana faces Tropical Race 4, "
                    "wheat stem rust Ug99 threatened global wheat, and "
                    "single-cross maize hybrids blanket the US Corn Belt. "
                    "FAO's biodiversity assessments document ongoing "
                    "genetic erosion as landraces vanish from fields. The "
                    "unsolved problem is economic: uniformity pays - "
                    "same seed, same management, same market - while "
                    "diversity is an insurance policy nobody wants to "
                    "buy until the disaster arrives."),
        "background": ("The genetic vulnerability debate began with the "
                       "1970 US southern corn leaf blight, which "
                       "destroyed 15 percent of the crop because most "
                       "hybrids shared the same susceptible cytoplasm - "
                       "the National Research Council's 'Genetic "
                       "Vulnerability of Major Crops' (1972) was the "
                       "direct result. Gene banks were built as the "
                       "answer: the Svalbard Global Seed Vault opened in "
                       "2008 as the backup of backups, and CGIAR centers "
                       "hold hundreds of thousands of accessions. But "
                       "conservation is not use - most accessions sit "
                       "uncharacterized, breeders reach for the same "
                       "elite parents, and on-farm diversity keeps "
                       "falling as landraces are replaced. The diversity "
                       "exists in cold storage; the vulnerability grows "
                       "in the field."),
        "why_it_matters": ("The next Ug99 or Panama disease will not "
                           "announce itself politely. Genetic uniformity "
                           "turns a manageable disease into a continental "
                           "crop failure, and climate change is moving "
                           "pathogens into new territory. Diversity is "
                           "the cheapest catastrophe insurance in "
                           "agriculture, and it is lapsing."),
        "sig_pointer": ("The Signature edition proposes pricing genetic "
                        "vulnerability into seed markets - a diversity "
                        "score per variety, with insurance-style rewards "
                        "for planting mosaics. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) landscape-level "
                     "genetic vulnerability can be scored - varietal "
                     "concentration indices plus known susceptibility "
                     "genes; (2) mosaic planting (multiple varieties, "
                     "multilines, mixtures) demonstrably slows epidemics; "
                     "(3) farmers will diversify if the insurance value "
                     "is priced, not preached. Reasoning path: score "
                     "each major crop region's vulnerability index, "
                     "publish it like a weather forecast, and pay "
                     "diversity premiums - seed discounts, insurance "
                     "rebates - to farms that plant qualifying mosaics. "
                     "Proposed mechanism: a 'diversity dividend' market "
                     "where the premium tracks the published "
                     "vulnerability score: the more uniform the region, "
                     "the higher the payment for diversifying. What "
                     "would confirm it: regions where the dividend runs "
                     "and epidemic losses fall relative to uniform "
                     "controls. What would kill it: premiums too small "
                     "to offset the convenience of uniformity, or "
                     "mosaics that complicate harvest and marketing "
                     "beyond what premiums cover. What it does NOT "
                     "claim: that diversity prevents all epidemics, or "
                     "that gene banks alone solve field vulnerability."),
        "key_points": [
            "A handful of varieties dominate each major crop across continents.",
            "The 1970 corn blight destroyed 15 percent of the US crop from shared susceptibility.",
            "Ug99 wheat rust and banana Tropical Race 4 show the pattern repeating.",
            "Gene banks conserve diversity in cold storage while fields grow more uniform.",
        ],
        "requirements": [
            "Score genetic vulnerability per crop region and publish it openly.",
            "Pay diversity premiums - seed discounts, insurance rebates - for mosaic planting.",
            "Let the premium track the vulnerability score: more uniform, higher payment.",
        ],
        "standards": [
            "NRC Genetic Vulnerability of Major Crops 1972; FAO biodiversity assessments.",
        ],
        "citations": CIT_BASE + [
            "FAO. The State of the World's Biodiversity for Food and "
            "Agriculture. Rome; 2019.",
        ],
        "demo": {
            "calc": "sum", "quantity": "Diversity coverage stack",
            "unit": "index points", "formula": "landraces_conserved + wild_relatives_banked + breeding_use",
            "assumptions": [
                ("Landraces conserved and characterized", 30, [10, 30, 50]),
                ("Wild relatives banked", 20, [5, 20, 35]),
                ("Diversity used in active breeding", 10, [2, 10, 25]),
            ],
            "checks": [((10, 5, 2), 17, 1e-9),
                       ((50, 35, 25), 110, 1e-9)],
            "steps": [
                "Step 1: score the region's varietal concentration and susceptibility.",
                "Step 2: publish the vulnerability index like a forecast.",
                "Step 3: stack conserved, banked, and actively-used diversity.",
                "Step 4: pay diversity premiums scaled to the vulnerability score.",
                "Step 5: re-score after planting season and adjust premiums.",
            ],
            "confirm": [
                "Dividend regions show lower epidemic losses than uniform controls.",
                "Premiums sustain mosaic planting year over year.",
            ],
            "refute": [
                "Premiums cannot offset the convenience of uniformity.",
                "Mosaics complicate harvest and marketing beyond what premiums cover.",
            ],
            "note": "Diversity-dividend explorer for genetic vulnerability.",
        },
    },
]

ENTRIES += [
    # ------------------------------------------------- 19 COMPOUNDED
    {
        "key": "mycotoxins",
        "name": "Mycotoxins and Food Safety Under Warming",
        "group": "Compounded",
        "ladder_rank": 19, "ladder_tier": "compounded",
        "problem": ("Mold toxins - aflatoxin, fumonisin, deoxynivalenol - "
                    "contaminate a large share of the world's grain, and "
                    "warming is pushing the most dangerous ones into new "
                    "territory. Aflatoxin, produced by Aspergillus fungi in "
                    "hot conditions, is a potent liver carcinogen; FAO "
                    "estimates that a significant share of food crops are "
                    "affected by mycotoxins, and surveys find aflatoxin "
                    "above safe limits in staple maize and groundnuts "
                    "across the tropics. The unsolved problem is "
                    "compounding: climate change expands the warm zone "
                    "where aflatoxin thrives, smallholders lack drying "
                    "and testing, and contaminated grain that cannot be "
                    "sold is often eaten anyway - turning a food-safety "
                    "problem into a public-health crisis."),
        "background": ("Aflatoxin's danger was discovered in 1960 when "
                       "100,000 turkeys died in England from contaminated "
                       "Brazilian groundnut meal - the 'Turkey X disease' "
                       "that launched mycotoxicology. Since then, "
                       "regulatory limits have been set worldwide (the EU "
                       "has the strictest), biocontrol with atoxigenic "
                       "Aspergillus strains (Aflasafe, developed by IITA "
                       "and USDA) has shown 80-plus percent reductions in "
                       "African trials, and rapid test kits have brought "
                       "detection closer to the farm. But the climate link "
                       "is the new front: modeling studies project "
                       "aflatoxin risk rising in Southern Europe, the US "
                       "Corn Belt, and across the tropics as temperatures "
                       "climb, while testing and biocontrol reach only a "
                       "fraction of at-risk farmers."),
        "why_it_matters": ("Aflatoxin exposure is linked to liver cancer "
                           "and child stunting, and it strikes hardest "
                           "where people already face hunger - the "
                           "cruelest overlap in food safety. Contaminated "
                           "grain also locks farmers out of premium "
                           "markets, so mycotoxins tax both health and "
                           "income."),
        "sig_pointer": ("The Signature edition proposes mycotoxin-risk "
                        "maps updated each season, with biocontrol and "
                        "drying deployed by forecast - prevention aimed "
                        "where the risk will be, not where it was. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) aflatoxin risk for a "
                     "coming season is predictable from weather "
                     "forecasts plus soil Aspergillus load - good enough "
                     "to target interventions; (2) atoxigenic biocontrol "
                     "and proper drying prevent most contamination when "
                     "applied before the risk window; (3) farmers adopt "
                     "when the intervention is delivered, not just "
                     "recommended. Reasoning path: forecast seasonal "
                     "mycotoxin risk per district from climate data, "
                     "pre-position biocontrol and drying capacity in "
                     "high-risk districts, verify with rapid tests at "
                     "harvest, and publish the risk maps so markets can "
                     "price safety. Proposed mechanism: a seasonal "
                     "'mycotoxin forecast and response' system - risk "
                     "map out, biocontrol and dryers in, tested grain "
                     "certified - that treats contamination as a "
                     "predictable event to be intercepted. What would "
                     "confirm it: forecast districts showing lower "
                     "contamination rates and fewer rejected lots than "
                     "unforecast controls. What would kill it: "
                     "forecasts too coarse to target villages, or "
                     "biocontrol supply chains that cannot scale to "
                     "forecast demand. What it does NOT claim: that "
                     "forecasting replaces testing, or that any system "
                     "makes visibly moldy grain safe."),
        "key_points": [
            "Aflatoxin is a potent liver carcinogen thriving in hot conditions.",
            "A significant share of world food crops is affected by mycotoxins.",
            "Warming expands the aflatoxin risk zone into Southern Europe and the US Corn Belt.",
            "Aflasafe biocontrol cuts contamination 80+ percent in trials but reaches few farmers.",
        ],
        "requirements": [
            "Forecast seasonal mycotoxin risk per district from weather and fungal load.",
            "Pre-position biocontrol and drying capacity in high-risk districts before the season.",
            "Verify with rapid tests at harvest and certify tested grain.",
        ],
        "standards": [
            "Codex Alimentarius mycotoxin limits; EU aflatoxin regulations.",
        ],
        "citations": CIT_BASE + [
            "FAO. Mycotoxins in food: detection and control assessments. "
            "Rome (series).",
        ],
        "demo": {
            "calc": "expr", "quantity": "Harvest tonnage entering the risk zone",
            "unit": "Mt", "formula": "warm_zone_harvest * (1 + expansion_pct/100)",
            "expr": "a0 * (1 + a1 / 100.0)",
            "assumptions": [
                ("Harvest in warm zones", 800, [500, 800, 1200]),
                ("Risk-zone expansion percent", 25, [10, 25, 50]),
            ],
            "checks": [((500, 10), 550.0, 1e-9),
                       ((1200, 50), 1800.0, 1e-9)],
            "steps": [
                "Step 1: tally harvest tonnage in current warm zones.",
                "Step 2: project the risk-zone expansion from warming scenarios.",
                "Step 3: compute tonnage entering the risk zone.",
                "Step 4: pre-position biocontrol and drying by forecast.",
                "Step 5: verify with rapid tests and certify safe grain.",
            ],
            "confirm": [
                "Forecast districts show lower contamination than unforecast controls.",
                "Certified safe grain earns market premiums that fund the system.",
            ],
            "refute": [
                "Forecasts prove too coarse to target villages.",
                "Biocontrol supply cannot scale to forecast demand.",
            ],
            "note": "Mycotoxin forecast-and-response explorer.",
        },
    },
    # ------------------------------------------------- 20 COMPOUNDED
    {
        "key": "land-competition",
        "name": "Land Competition: Food vs Fuel vs Forest",
        "group": "Compounded",
        "ladder_rank": 20, "ladder_tier": "compounded",
        "problem": ("The same hectare is claimed by food, biofuel, "
                    "forests, cities, and solar farms, and the claims "
                    "are growing faster than the land. Biofuel mandates "
                    "divert tens of millions of hectares of crops to "
                    "fuel tanks; forest restoration pledges claim "
                    "hundreds of millions of hectares; urbanization "
                    "paves prime farmland. The indirect land-use change "
                    "(ILUC) debate showed the trap: biofuel grown on "
                    "'spare' land can displace food production into "
                    "forests elsewhere, erasing its climate benefit. "
                    "The unsolved problem is allocation without a "
                    "referee - no institution prices the competing "
                    "claims in common units, so the loudest lobby "
                    "wins and the food system absorbs the residual."),
        "background": ("The food-versus-fuel fight erupted in 2007-2008 "
                       "when US corn ethanol expansion coincided with "
                       "record food prices, and researchers showed "
                       "that ILUC could make some biofuels worse than "
                       "gasoline for the climate. The EU responded by "
                       "capping food-based biofuels; the US kept its "
                       "Renewable Fuel Standard. In parallel, the Bonn "
                       "Challenge (2011) and kindred pledges promised "
                       "to restore hundreds of millions of hectares of "
                       "degraded land - noble, but restoration and "
                       "farming compete for the same landscapes. "
                       "Integrated assessment models try to optimize "
                       "across claims, but their land-allocation "
                       "answers depend on contested assumptions about "
                       "yields, diets, and the value of nature."),
        "why_it_matters": ("Every misallocated hectare is food not "
                           "grown, forest not standing, or fuel that "
                           "costs more carbon than it saves. With "
                           "arable land essentially fixed, allocation "
                           "mistakes compound for decades - a biofuel "
                           "mandate or restoration pledge written today "
                           "shapes land use to 2050."),
        "sig_pointer": ("The Signature edition proposes a common-unit "
                        "land ledger - calories, carbon, and biodiversity "
                        "scored per hectare - so competing claims bid "
                        "transparently instead of lobbying silently. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) each land claim can "
                     "be scored per hectare in three currencies - "
                     "delivered calories, net carbon, biodiversity "
                     "value - well enough to compare; (2) transparent "
                     "scoring changes political outcomes even without "
                     "a single global referee; (3) multifunctional "
                     "land uses (agrivoltaics, silvopasture, "
                     "restoration grazing) can score in multiple "
                     "currencies at once. Reasoning path: score every "
                     "major land claim per hectare in the three "
                     "currencies, publish the ledger nationally, and "
                     "require new mandates to show their ledger "
                     "balance - what is gained, what is displaced, "
                     "where. Proposed mechanism: a public 'land-claim "
                     "ledger' where biofuel mandates, restoration "
                     "pledges, and farm expansion each book their "
                     "hectares and their three-currency scores, with "
                     "ILUC-style displacement estimated openly. What "
                     "would confirm it: mandates revised or redesigned "
                     "after ledger publication, and multifunctional "
                     "uses expanding where they outscore single uses. "
                     "What would kill it: scoring disputes so deep "
                     "that no ledger is trusted, or political actors "
                     "ignoring published ledgers entirely. What it "
                     "does NOT claim: that one ledger settles values "
                     "disputes, or that scoring replaces democratic "
                     "choice."),
        "key_points": [
            "Food, biofuel, forest restoration, cities, and solar compete for fixed land.",
            "ILUC can erase biofuels' climate benefit by displacing food into forests.",
            "Restoration pledges claim hundreds of millions of hectares.",
            "No institution prices the competing claims in common units.",
        ],
        "requirements": [
            "Score every land claim per hectare in calories, net carbon, and biodiversity.",
            "Publish the ledger nationally and require new mandates to show their balance.",
            "Estimate displacement (ILUC-style) openly for each claim.",
        ],
        "standards": [
            "EU ILUC accounting rules; Bonn Challenge restoration tracking.",
        ],
        "citations": CIT_BASE + [
            "Searchinger T et al. Use of U.S. croplands for biofuels increases "
            "greenhouse gases through emissions from land-use change. Science; "
            "2008.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Total land demand across claims",
            "unit": "Mha", "formula": "food_land + biofuel_land + forest_target",
            "expr": "a0 + a1 + a2",
            "assumptions": [
                ("Food production land", 1600, [1400, 1600, 1800]),
                ("Biofuel mandate land", 80, [20, 80, 150]),
                ("Forest restoration target", 350, [200, 350, 500]),
            ],
            "checks": [((1400, 20, 200), 1620, 1e-9),
                       ((1800, 150, 500), 2450, 1e-9)],
            "steps": [
                "Step 1: tally land claimed by food, fuel, and forest targets.",
                "Step 2: score each claim per hectare in calories, carbon, biodiversity.",
                "Step 3: estimate displacement - what each claim pushes elsewhere.",
                "Step 4: publish the three-currency ledger.",
                "Step 5: revise mandates against the published balance.",
            ],
            "confirm": [
                "Mandates are revised or redesigned after ledger publication.",
                "Multifunctional land uses expand where they outscore single uses.",
            ],
            "refute": [
                "Scoring disputes are so deep no ledger is trusted.",
                "Political actors ignore published ledgers entirely.",
            ],
            "note": "Land-claim ledger explorer for food vs fuel vs forest.",
        },
    },
    # ------------------------------------------------- 21 COMPOUNDED
    {
        "key": "nitrous-oxide",
        "name": "Nitrous Oxide: The Long-Lived Fertilizer Emission",
        "group": "Compounded",
        "ladder_rank": 21, "ladder_tier": "compounded",
        "problem": ("Every tonne of nitrogen fertilizer carries a "
                    "hidden climate cost: soil microbes convert a "
                    "fraction of it to nitrous oxide, a greenhouse gas "
                    "around 273 times as potent as CO2 that lingers in "
                    "the atmosphere for over a century. N2O is now the "
                    "dominant ozone-depleting emission as CFCs fade, and "
                    "agriculture is its largest human source. The "
                    "unsolved problem is variability: the emission "
                    "factor swings wildly with soil, weather, and timing "
                    "- a rainstorm after fertilizing can multiply "
                    "emissions tenfold - so neither farmers nor "
                    "policymakers can manage what they cannot predict, "
                    "and mitigation (inhibitors, timing, placement) "
                    "works unevenly across conditions."),
        "background": ("N2O's potency was established in atmospheric "
                       "chemistry in the 1970s-80s, and the IPCC's "
                       "default emission factor - about 1 percent of "
                       "applied nitrogen lost as N2O - became the "
                       "global accounting standard, even though field "
                       "studies show the real factor ranging from near "
                       "zero to several percent. The 2000s-2010s brought "
                       "a mitigation toolkit: nitrification inhibitors "
                       "(DCD, DMPP), split application, subsurface "
                       "placement, and improved drainage all cut N2O in "
                       "trials. But adoption is thin because N2O is "
                       "invisible - no farmer sees it, no market pays "
                       "for cutting it - and because the science of "
                       "predicting hot moments (the rainstorm after "
                       "fertilizing) remains too coarse for field "
                       "decisions."),
        "why_it_matters": ("N2O will outlive everyone reading this in "
                           "the atmosphere, and its emissions grow with "
                           "every tonne of fertilizer the 10-billion "
                           "future requires. It is also now the biggest "
                           "threat to the ozone layer. Cutting N2O is "
                           "permanent climate protection, not a "
                           "temporary offset."),
        "sig_pointer": ("The Signature edition proposes hot-moment "
                        "forecasting - weather-linked N2O risk scores "
                        "that tell farmers when NOT to fertilize - plus "
                        "payments for verified cuts. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) most N2O comes in "
                     "hot moments - warm, wet, recently fertilized "
                     "soil - which are forecastable from weather plus "
                     "application records; (2) avoiding fertilization "
                     "just before hot moments cuts emissions more "
                     "cheaply than any product; (3) verified cuts can "
                     "be credited if hot-moment models are calibrated "
                     "per region. Reasoning path: build regional "
                     "hot-moment models from weather and soil data, "
                     "issue N2O-risk forecasts to farmers like weather "
                     "alerts, shift applications away from high-risk "
                     "windows, and verify with seasonal flux "
                     "measurements. Proposed mechanism: an 'N2O "
                     "forecast service' - risk scores per field-week, "
                     "application timing advice, and carbon payments "
                     "for measured seasonal reductions. What would "
                     "confirm it: forecast-guided farms showing "
                     "lower seasonal N2O with equal yields, and "
                     "payments covering the management cost. What "
                     "would kill it: hot moments too stochastic to "
                     "forecast usefully, or verification costs that "
                     "exceed the carbon value. What it does NOT "
                     "claim: that timing eliminates N2O, or that "
                     "inhibitors are unnecessary."),
        "key_points": [
            "N2O is about 273 times as potent as CO2 and lasts over a century.",
            "Agriculture is the largest human N2O source; it is now the top ozone-depleting emission.",
            "The IPCC 1-percent default hides real emission factors from near zero to several percent.",
            "Most emissions come in hot moments - warm, wet, recently fertilized soil.",
        ],
        "requirements": [
            "Build regional hot-moment models from weather, soil, and application data.",
            "Issue N2O-risk forecasts and shift applications away from high-risk windows.",
            "Verify seasonal cuts and pay farmers per verified tonne.",
        ],
        "standards": [
            "IPCC emission factor methodology; AR6 N2O global warming potentials.",
        ],
        "citations": CIT_BASE + [
            "IPCC. Climate Change 2021: The Physical Science Basis. WG I "
            "contribution to AR6. Cambridge University Press; 2021.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Seasonal N2O emissions",
            "unit": "Mt CO2e", "formula": "n_applied * ef_pct * gwp / 1000",
            "expr": "a0 * a1 * a2 / 1000.0",
            "assumptions": [
                ("Nitrogen applied (Mt N)", 120, [80, 120, 160]),
                ("Emission factor (percent of N)", 1.0, [0.5, 1.0, 1.6]),
                ("N2O global warming potential", 273, [265, 273, 298]),
            ],
            "checks": [((80, 0.5, 265), 10.6, 1e-9),
                       ((160, 1.6, 298), 76.288, 1e-6)],
            "steps": [
                "Step 1: record nitrogen applied and the regional emission factor.",
                "Step 2: convert to CO2-equivalent with the N2O warming potential.",
                "Step 3: forecast hot moments from weather and application timing.",
                "Step 4: shift applications away from high-risk windows.",
                "Step 5: verify seasonal cuts and pay per verified tonne.",
            ],
            "confirm": [
                "Forecast-guided farms cut seasonal N2O with equal yields.",
                "Carbon payments cover the management cost of re-timing.",
            ],
            "refute": [
                "Hot moments prove too stochastic to forecast usefully.",
                "Verification costs exceed the carbon value of cuts.",
            ],
            "note": "N2O hot-moment explorer for fertilizer emissions.",
        },
    },
    # ------------------------------------------------- 22 COMPOUNDED
    {
        "key": "precision-digital-divide",
        "name": "The Precision Agriculture Digital Divide",
        "group": "Compounded",
        "ladder_rank": 22, "ladder_tier": "compounded",
        "problem": ("Precision agriculture - GPS guidance, variable-rate "
                    "application, drone scouting, soil sensors - can cut "
                    "inputs 10 to 30 percent while holding yields, but "
                    "it serves the largest, richest farms and bypasses "
                    "the 500 million smallholders who farm most of the "
                    "developing world's land. The technology assumes "
                    "connectivity, capital, literacy in its interfaces, "
                    "and fields big enough for the machinery - "
                    "assumptions that fail on a two-hectare farm with "
                    "patchy signal. The unsolved problem is not the "
                    "sensor but the delivery model: how to put "
                    "precision's benefits - the right dose, in the right "
                    "place, at the right time - into the hands of "
                    "farmers who cannot buy the hardware."),
        "background": ("Precision ag began in the 1990s with GPS-guided "
                       "tractors in the US Midwest and spread through "
                       "yield monitors, satellite imagery, and "
                       "variable-rate technology. The 2010s added cheap "
                       "drones, phone-based advisories, and satellite "
                       "data made free by programs like Copernicus. "
                       "Pilot projects for smallholders followed - "
                       "phone-based pest alerts, satellite crop "
                       "monitoring, shared-equipment models - and showed "
                       "real gains where they ran. But the business "
                       "models keep failing at scale: hardware is "
                       "designed for 500-hectare farms, data plans cost "
                       "too much, interfaces assume literacy and "
                       "connectivity, and the farmers who most need "
                       "precision are the least able to pay for it."),
        "why_it_matters": ("Smallholders produce a large share of the "
                           "food in Africa and Asia on the least "
                           "efficient input use. If precision's benefits "
                           "stay locked in rich-country broadacres, the "
                           "yield gap, the nitrogen problem, and the "
                           "water problem all stay unsolved where they "
                           "are worst."),
        "sig_pointer": ("The Signature edition proposes precision as a "
                        "service - shared drones, sensors, and advisories "
                        "sold per hectare per season, with the phone as "
                        "the only hardware the farmer needs. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the value of "
                     "precision is information - where to dose, how "
                     "much - not ownership of hardware; (2) a service "
                     "model (drone flyover, sensor network, phone "
                     "advisory) can deliver that information per "
                     "hectare at smallholder prices; (3) farmers pay "
                     "for measured input savings, not for technology. "
                     "Reasoning path: unbundle precision into "
                     "per-hectare services - scouting, soil mapping, "
                     "variable-rate prescriptions executed by shared "
                     "equipment - price each against the input savings "
                     "it delivers, and deliver advice through the "
                     "phones farmers already own. Proposed mechanism: "
                     "a 'precision cooperative' where one drone-and-"
                     "sensor team serves hundreds of small farms, "
                     "each paying per hectare per season from measured "
                     "savings. What would confirm it: cooperatives "
                     "where members cut inputs 15-plus percent with "
                     "steady yields and renew subscriptions. What would "
                     "kill it: service costs that exceed smallholder "
                     "savings, or connectivity gaps that break the "
                     "advisory loop. What it does NOT claim: that "
                     "services replace farmer knowledge, or that "
                     "connectivity builds itself."),
        "key_points": [
            "Precision ag can cut inputs 10-30 percent but serves mainly large rich farms.",
            "Some 500 million smallholders farm most of the developing world's land.",
            "The technology assumes connectivity, capital, and big fields.",
            "Pilots show gains; business models fail at scale.",
        ],
        "requirements": [
            "Unbundle precision into per-hectare services: scouting, mapping, prescriptions.",
            "Price each service against measured input savings, not hardware cost.",
            "Deliver through phones farmers own, with shared equipment doing the field work.",
        ],
        "standards": [
            "FAO digital agriculture guidelines; smallholder service-model pilots.",
        ],
        "citations": CIT_BASE + [
            "FAO. Digital agriculture and smallholder inclusion assessments. "
            "Rome (series).",
        ],
        "demo": {
            "calc": "prod", "quantity": "Smallholder precision adoption share",
            "unit": "share", "formula": "device_access * connectivity * affordability",
            "assumptions": [
                ("Device access share", 0.60, [0.20, 0.60, 0.90]),
                ("Connectivity share", 0.50, [0.10, 0.50, 0.80]),
                ("Affordability share", 0.70, [0.30, 0.70, 0.95]),
            ],
            "checks": [((0.20, 0.10, 0.30), 0.006, 1e-9),
                       ((0.90, 0.80, 0.95), 0.684, 1e-6)],
            "steps": [
                "Step 1: score device access, connectivity, and affordability.",
                "Step 2: multiply into the adoption share - the weakest link binds.",
                "Step 3: fix the binding constraint first (usually affordability).",
                "Step 4: launch the per-hectare service cooperative.",
                "Step 5: renew only where measured savings exceed fees.",
            ],
            "confirm": [
                "Cooperatives cut member inputs 15+ percent with steady yields.",
                "Subscription renewals prove the savings are real.",
            ],
            "refute": [
                "Service costs exceed smallholder savings at scale.",
                "Connectivity gaps break the advisory loop.",
            ],
            "note": "Precision-as-a-service explorer for the digital divide.",
        },
    },
    # ------------------------------------------------- 23 COMPOUNDED
    {
        "key": "seed-systems",
        "name": "Seed Systems for Smallholder Farmers",
        "group": "Compounded",
        "ladder_rank": 23, "ladder_tier": "compounded",
        "problem": ("The best new varieties - drought-tolerant maize, "
                    "Saltol rice, disease-resistant cassava - mean "
                    "nothing if seed never reaches the farmer, and for "
                    "most smallholders it does not. Formal seed systems "
                    "supply a small fraction of seed in much of Africa "
                    "and Asia; the rest comes from farm-saved seed and "
                    "informal exchange, which is affordable and trusted "
                    "but slow to carry improved genetics and vulnerable "
                    "to seed-borne disease. The unsolved problem is the "
                    "middle: building seed enterprises that multiply "
                    "improved varieties, keep quality high, and sell at "
                    "prices smallholders can pay - in places where "
                    "roads, credit, and regulation are all thin."),
        "background": ("The Green Revolution ran on public seed systems: "
                       "national programs multiplied breeder seed and "
                       "sold it cheaply. Structural adjustment in the "
                       "1980s-90s privatized or defunded many of them, "
                       "and private companies filled the gap only where "
                       "hybrids (which must be repurchased yearly) made "
                       "business sense - maize, vegetables - leaving "
                       "self-pollinated staples like rice, wheat, beans, "
                       "and cassava to the informal system. Community "
                       "seed banks, quality-declared seed schemes, and "
                       "small seed enterprises have been piloted for "
                       "decades with real successes, but scaling them "
                       "runs into the same wall: quality assurance "
                       "without expensive certification, and distribution "
                       "without dealer networks."),
        "why_it_matters": ("Seed is the delivery vehicle for every "
                           "genetic gain in this database - drought "
                           "tolerance, heat tolerance, disease "
                           "resistance, nutrition. A variety that exists "
                           "only in a gene bank or a breeder's trial is "
                           "not a solution; it is a press release. The "
                           "seed system is the last mile of plant "
                           "breeding."),
        "sig_pointer": ("The Signature edition proposes quality-declared "
                        "community seed enterprises with light-touch "
                        "verification - germination and purity tested "
                        "locally, reputation tracked openly. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) full certification "
                     "is too costly for small seed enterprises, but "
                     "buyers need some quality signal; (2) local "
                     "germination and purity tests, done transparently, "
                     "are a sufficient signal for most staple seed; (3) "
                     "enterprises survive on margin from varieties "
                     "farmers actually rebuy - quality must be real. "
                     "Reasoning path: license community enterprises to "
                     "multiply improved varieties, require public "
                     "batch-level germination and purity results, track "
                     "reputation across seasons, and let the market - "
                     "not inspectors - reward quality. Proposed "
                     "mechanism: a 'quality-declared seed' marketplace "
                     "where every lot carries its test results and "
                     "every seller carries a public reputation score, "
                     "audited by spot-checks. What would confirm it: "
                     "enterprise zones where improved-variety adoption "
                     "and seed quality rise together, with enterprises "
                     "profitable. What would kill it: test fraud that "
                     "destroys trust faster than spot-checks restore "
                     "it, or margins too thin for enterprises to "
                     "survive. What it does NOT claim: that informal "
                     "exchange should be replaced, or that light-touch "
                     "quality suits hybrid or vegetable seed equally."),
        "key_points": [
            "Formal seed systems supply a small fraction of smallholder seed in Africa and Asia.",
            "Improved varieties are useless if seed never reaches the farmer.",
            "Private companies serve hybrids; self-pollinated staples rely on informal systems.",
            "Quality assurance without expensive certification is the missing middle.",
        ],
        "requirements": [
            "License community enterprises to multiply improved varieties locally.",
            "Require public batch-level germination and purity test results.",
            "Track seller reputation openly and audit with spot-checks.",
        ],
        "standards": [
            "FAO Quality Declared Seed system; community seed bank guidelines.",
        ],
        "citations": CIT_BASE + [
            "FAO. Quality declared seed system. FAO Plant Production and "
            "Protection Paper 117 (revised). Rome.",
        ],
        "demo": {
            "calc": "sum", "quantity": "Smallholder seed access score",
            "unit": "points", "formula": "formal_seed + community_seed + saved_seed_quality",
            "assumptions": [
                ("Formal seed channel", 25, [10, 25, 40]),
                ("Community enterprise seed", 45, [25, 45, 65]),
                ("Saved-seed quality score", 20, [10, 20, 35]),
            ],
            "checks": [((10, 25, 10), 45, 1e-9),
                       ((40, 65, 35), 140, 1e-9)],
            "steps": [
                "Step 1: score the formal, community, and saved-seed channels.",
                "Step 2: sum into the access score.",
                "Step 3: license community enterprises for improved varieties.",
                "Step 4: publish batch test results and reputation scores.",
                "Step 5: track adoption and quality together each season.",
            ],
            "confirm": [
                "Enterprise zones show rising adoption and seed quality together.",
                "Seed enterprises stay profitable on real quality.",
            ],
            "refute": [
                "Test fraud destroys trust faster than spot-checks restore it.",
                "Margins prove too thin for enterprises to survive.",
            ],
            "note": "Quality-declared seed explorer for the last mile of breeding.",
        },
    },
    # ------------------------------------------------- 24 ADVANCED
    {
        "key": "apomixis",
        "name": "Apomixis: Cloning Hybrid Vigor Through Seed",
        "group": "Advanced",
        "ladder_rank": 24, "ladder_tier": "advanced",
        "problem": ("Hybrid crops outyield their parents by 15 to 50 "
                    "percent, but the vigor vanishes in the next "
                    "generation - farmers must buy fresh hybrid seed "
                    "every year. Apomixis, asexual reproduction through "
                    "seed, would freeze hybrid vigor permanently: plant "
                    "the harvest, get the same hybrid again. It occurs "
                    "naturally in some grasses and citrus relatives, and "
                    "its genetics have been partly decoded, but "
                    "engineering reliable apomixis into rice, maize, or "
                    "wheat remains undone. The unsolved problem is "
                    "developmental: apomixis requires rewiring meiosis, "
                    "embryo initiation, and endosperm development in "
                    "concert - three programs that must all switch "
                    "together or the seed fails."),
        "background": ("Apomixis research accelerated in the 1990s-2000s "
                       "as the genes behind natural apomixis in "
                       "grasses were mapped, and the breakthrough "
                       "concept - 'MiMe', turning meiosis into mitosis "
                       "by knocking out three meiotic genes - was "
                       "demonstrated in Arabidopsis and rice in the "
                       "2010s. In 2019, two groups reported synthetic "
                       "apomixis-like reproduction in rice by combining "
                       "MiMe with embryo-initiating genes, producing "
                       "clonal seeds at measurable rates. But rates "
                       "remain low, fertility is impaired, and no "
                       "system yet produces clonal hybrid seed reliably "
                       "enough for agriculture. The field is arguably "
                       "the closest of plant biology's grand challenges "
                       "- and still not closed."),
        "why_it_matters": ("Apomixis would democratize hybrid vigor: any "
                           "farmer could replant hybrids, seed companies' "
                           "monopoly on vigor would break, and breeding "
                           "gains would reach smallholders at the cost "
                           "of saved seed. It is the trait that would "
                           "restructure the entire seed industry."),
        "sig_pointer": ("The Signature edition proposes scoring "
                        "apomixis systems by clonal-seed rate times "
                        "fertility - the only product that matters - and "
                        "funding strictly against that metric. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the only metric "
                     "that matters is field-usable clonal seed: rate of "
                     "clonal seeds times seed fertility times agronomic "
                     "performance; (2) partial apomixis (low clonal "
                     "rates) has no product value, so research must be "
                     "scored on the full package; (3) the three "
                     "developmental programs - MiMe, parthenogenesis, "
                     "endosperm - interact, and must be optimized as a "
                     "system. Reasoning path: define the composite "
                     "product metric, score every apomixis line on it, "
                     "fund only lines that move the metric, and treat "
                     "each developmental program as a module to be "
                     "tuned against the composite. Proposed mechanism: "
                     "an 'apomixis product ledger' where funding "
                     "follows the composite metric quarter by quarter, "
                     "forcing the science toward the seed farmers "
                     "would plant. What would confirm it: rice or "
                     "maize lines producing high-rate clonal hybrid "
                     "seed with competitive yields in field trials. "
                     "What would kill it: developmental interactions "
                     "that cap clonal rates below product thresholds "
                     "no matter the tuning. What it does NOT claim: "
                     "that apomixis is near, or that it would end "
                     "plant breeding - breeders would still make the "
                     "hybrids worth cloning."),
        "key_points": [
            "Hybrid vigor (15-50 percent) vanishes in the next generation; seed must be repurchased.",
            "Apomixis would freeze hybrid vigor permanently through clonal seed.",
            "MiMe plus embryo-initiating genes produced clonal rice seeds in 2019 - at low rates.",
            "Meiosis, embryo, and endosperm programs must all switch together or the seed fails.",
        ],
        "requirements": [
            "Score apomixis lines on the composite product metric: clonal rate times fertility times yield.",
            "Fund only lines that move the composite metric, quarter by quarter.",
            "Optimize the three developmental programs as one interacting system.",
        ],
        "standards": [
            "MiMe genotype benchmarks; clonal-seed rate and fertility assays.",
        ],
        "citations": CIT_BASE + [
            "Wang C et al. Clonal seeds from hybrid rice by simultaneous "
            "editing of three meiotic genes. Nature Biotechnology; 2019.",
        ],
        "demo": {
            "calc": "gain", "quantity": "Yield of apomictic hybrid line",
            "unit": "t/ha", "formula": "baseline_yield / (1 - heterosis_retained)",
            "planck": 4.0, "f_base": 0.0,
            "assumptions": [
                ("Heterosis retained through apomixis", 0.35, [0.10, 0.35, 0.60]),
            ],
            "checks": [((0.10,), 4.444444, 1e-6),
                       ((0.60,), 10.0, 1e-9)],
            "steps": [
                "Step 1: set the baseline inbred yield.",
                "Step 2: set the heterosis fraction the apomixis system retains.",
                "Step 3: compute the clonal hybrid yield through the gain formula.",
                "Step 4: score the line on the composite product metric.",
                "Step 5: fund only lines that move the metric.",
            ],
            "confirm": [
                "Rice or maize lines produce high-rate clonal hybrid seed in field trials.",
                "Yields compete with conventional hybrids while seed is replantable.",
            ],
            "refute": [
                "Developmental interactions cap clonal rates below product thresholds.",
                "Fertility penalties erase the heterosis advantage.",
            ],
            "note": "Apomixis product-ledger explorer for cloning hybrid vigor.",
        },
    },
    # ------------------------------------------------- 25 ADVANCED
    {
        "key": "perennial-grains",
        "name": "Perennial Grain Agriculture: Farming Like the Prairie",
        "group": "Advanced",
        "ladder_rank": 25, "ladder_tier": "advanced",
        "problem": ("Almost all grain comes from annual plants that must "
                    "be replanted yearly, leaving soil bare and eroding "
                    "between crops - yet nature's most productive "
                    "grasslands are perennial. The Land Institute's "
                    "Kernza (intermediate wheatgrass) proves perennial "
                    "grain is possible, but yields are a fraction of "
                    "annual wheat and the grain is small. The unsolved "
                    "problem is the perennial-yield paradox: perennials "
                    "invest in roots and persistence, annuals invest "
                    "everything in seed, and fifty years of selection "
                    "have not closed the gap. Two paths compete - "
                    "domesticate wild perennials, or perennialize "
                    "annual crops - and neither has yet produced a "
                    "perennial staple that feeds people at scale."),
        "background": ("Wes Jackson founded The Land Institute in 1976 "
                       "on the radical premise that agriculture should "
                       "mimic the prairie: perennial polycultures "
                       "instead of annual monocultures. Decades of "
                       "breeding produced Kernza, now grown on "
                       "thousands of hectares and sold in niche "
                       "products, with yields around a tonne per "
                       "hectare versus 3-8 for wheat. The second path - "
                       "perennial rice, perennial wheat via wide "
                       "hybridization - has produced experimental "
                       "lines, including perennial rice regrowing for "
                       "multiple seasons in Chinese trials. The "
                       "ecological payoff is proven: perennials build "
                       "soil carbon, stop erosion, and need less "
                       "fertilizer. The yield gap is the wall."),
        "why_it_matters": ("Perennial staples would end the annual "
                           "tillage-erosion cycle, sequester carbon at "
                           "continental scale, and cut fertilizer needs "
                           "- the closest thing to a free lunch in "
                           "agriculture. But only if yields reach the "
                           "point where farmers choose them over annuals."),
        "sig_pointer": ("The Signature edition proposes breeding "
                        "perennials against an explicit yield-parity "
                        "roadmap with soil-carbon payments bridging the "
                        "gap years. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the yield gap is "
                     "quantitative and closable - wild annual grains "
                     "were also low-yielding before domestication; (2) "
                     "perennials' ecosystem payments (carbon, erosion, "
                     "nitrogen) are real and monetizable during the "
                     "breeding decades; (3) farmers adopt on yield plus "
                     "payments, not on ecology alone. Reasoning path: "
                     "set a yield-parity roadmap (e.g., 60 percent of "
                     "annual wheat by year 10, 80 percent by year 20), "
                     "breed strictly against it, and pay growers the "
                     "ecosystem value of perennial acres so early "
                     "adoption is economic before parity arrives. "
                     "Proposed mechanism: a 'perennial bridge fund' - "
                     "carbon and soil payments that top up perennial "
                     "grain income to annual-crop parity, declining as "
                     "breeding closes the yield gap. What would confirm "
                     "it: roadmap milestones hit on schedule and bridge-"
                     "fund acres expanding. What would kill it: a "
                     "biological ceiling where perennial allocation to "
                     "roots permanently caps seed yield below adoption "
                     "thresholds. What it does NOT claim: that "
                     "perennials suit all environments, or that annuals "
                     "disappear."),
        "key_points": [
            "Nearly all grain is annual; nature's most productive grasslands are perennial.",
            "Kernza proves perennial grain works but yields a fraction of wheat.",
            "Perennials build soil carbon, stop erosion, and need less fertilizer.",
            "Two paths: domesticate wild perennials, or perennialize annual crops.",
        ],
        "requirements": [
            "Breed perennials against an explicit yield-parity roadmap with dated milestones.",
            "Pay growers ecosystem value (carbon, erosion, nitrogen) during the gap years.",
            "Decline the bridge payments as breeding closes the yield gap.",
        ],
        "standards": [
            "Land Institute perennial breeding targets; soil carbon MRV protocols.",
        ],
        "citations": CIT_BASE + [
            "The Land Institute. Perennial grain breeding and Kernza "
            "development reports. Salina, Kansas (series).",
        ],
        "demo": {
            "calc": "expr", "quantity": "Cumulative soil carbon gain under perennials",
            "unit": "t CO2e/ha", "formula": "annual_soc * stand_years",
            "expr": "a0 * a1",
            "assumptions": [
                ("Annual soil carbon gain", 1.2, [0.4, 1.2, 2.5]),
                ("Perennial stand lifetime (years)", 12, [5, 12, 20]),
            ],
            "checks": [((0.4, 5), 2.0, 1e-9),
                       ((2.5, 20), 50.0, 1e-9)],
            "steps": [
                "Step 1: set the annual soil carbon gain under perennial cover.",
                "Step 2: set the stand lifetime in years.",
                "Step 3: compute cumulative carbon gain per hectare.",
                "Step 4: price the gain into bridge-fund payments.",
                "Step 5: track breeding against the yield-parity roadmap.",
            ],
            "confirm": [
                "Roadmap yield milestones are hit on schedule.",
                "Bridge-fund acres expand as payments make early adoption economic.",
            ],
            "refute": [
                "A biological ceiling caps perennial seed yield below adoption thresholds.",
                "Carbon payments never reach levels that bridge the income gap.",
            ],
            "note": "Perennial bridge-fund explorer.",
        },
    },
    # ------------------------------------------------- 26 ADVANCED
    {
        "key": "orphan-crops",
        "name": "Re-Domesticating Orphan Crops",
        "group": "Advanced",
        "ladder_rank": 26, "ladder_tier": "advanced",
        "problem": ("The world eats from about a dozen crops, but "
                    "thousands of nutritious, climate-tough plants - "
                    "millets, teff, bambara groundnut, amaranth - "
                    "remain 'orphans': unimproved, under-researched, "
                    "and shackled by wild traits like shattering and "
                    "tiny seeds. These crops already survive the heat, "
                    "drought, and poor soils where major cereals "
                    "struggle, which makes them natural climate "
                    "insurance. The unsolved problem is speed: "
                    "traditional domestication took millennia, and "
                    "even with gene editing compressing it to years "
                    "in the lab, no de novo domesticated orphan has "
                    "yet reached farmers at scale - the pipeline from "
                    "edited wild plant to adopted variety is still "
                    "being invented."),
        "background": ("De novo domestication became plausible in the "
                       "2010s when CRISPR let researchers edit "
                       "domestication genes directly: landmark papers "
                       "edited wild tomato relatives for larger fruit "
                       "and compact growth, and groundcherry was "
                       "rapidly improved the same way. The African "
                       "Orphan Crops Consortium began sequencing 101 "
                       "orphan crops to give breeders the genomic "
                       "maps. But editing is the easy part - field "
                       "testing, seed systems, processing, markets, "
                       "and consumer acceptance for a 'new' old crop "
                       "take years, and funding still flows "
                       "overwhelmingly to the major cereals. The "
                       "orphans have the genes; they lack the pipeline."),
        "why_it_matters": ("Diet diversity and climate resilience both "
                           "demand more than a dozen crops. Orphan "
                           "crops are pre-adapted to the hot, dry, poor "
                           "soils of the future - improving them is "
                           "faster than forcing wheat to survive where "
                           "millet already thrives."),
        "sig_pointer": ("The Signature edition proposes a de novo "
                        "domestication pipeline scored on "
                        "farmer-ready traits per year - shattering, "
                        "seed size, uniformity - with market-building "
                        "running in parallel. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the domestication "
                     "syndrome - non-shattering, larger seeds, uniform "
                     "ripening, compact growth - is controlled by a "
                     "tractable number of genes in most orphans; (2) "
                     "gene editing can install the syndrome in years, "
                     "not millennia; (3) a crop fails without "
                     "processing and markets, so those must be built "
                     "alongside the genetics. Reasoning path: pick "
                     "orphans by climate-fit plus nutrition, edit the "
                     "domestication syndrome, field-test for "
                     "farmer-ready traits, and build processing and "
                     "market channels in parallel - scoring the "
                     "pipeline on traits-delivered-per-year. Proposed "
                     "mechanism: an 'orphan pipeline ledger' where "
                     "each crop's progress - edited traits, trial "
                     "yields, market pilots - is published, and "
                     "funding follows the fastest-moving crops. What "
                     "would confirm it: edited orphan lines reaching "
                     "farmers with adoption and market uptake. What "
                     "would kill it: domestication traits that prove "
                     "polygenic and intractable in key orphans, or "
                     "consumer rejection of unfamiliar grains. What it "
                     "does NOT claim: that orphans replace major "
                     "cereals, or that editing alone domesticates a "
                     "crop."),
        "key_points": [
            "Humanity eats from about a dozen crops; thousands of tough nutritious orphans exist.",
            "Orphans are pre-adapted to heat, drought, and poor soils.",
            "CRISPR de novo domestication worked in wild tomato and groundcherry in the lab.",
            "No de novo domesticated orphan has yet reached farmers at scale.",
        ],
        "requirements": [
            "Pick orphans by climate fit plus nutrition, not by research fashion.",
            "Edit the domestication syndrome and score traits-delivered-per-year.",
            "Build processing and market channels in parallel with the genetics.",
        ],
        "standards": [
            "African Orphan Crops Consortium sequencing resources; de novo domestication trial protocols.",
        ],
        "citations": CIT_BASE + [
            "African Orphan Crops Consortium. Genome sequencing of 101 orphan "
            "crops (program reports).",
        ],
        "demo": {
            "calc": "sum", "quantity": "De novo domestication trait progress",
            "unit": "traits fixed", "formula": "yield_traits + shattering_fixed + nutrition_traits",
            "assumptions": [
                ("Yield-related traits fixed", 4, [1, 4, 8]),
                ("Shattering-resistance traits fixed", 3, [0, 3, 6]),
                ("Nutrition traits fixed", 2, [0, 2, 5]),
            ],
            "checks": [((1, 0, 0), 1, 1e-9),
                       ((8, 6, 5), 19, 1e-9)],
            "steps": [
                "Step 1: sequence the orphan and map domestication genes.",
                "Step 2: edit the syndrome: shattering, seed size, uniformity.",
                "Step 3: field-test for farmer-ready traits.",
                "Step 4: build processing and market pilots in parallel.",
                "Step 5: publish pipeline progress and fund the fastest movers.",
            ],
            "confirm": [
                "Edited orphan lines reach farmers with real adoption.",
                "Market pilots show consumer acceptance of the improved orphan.",
            ],
            "refute": [
                "Key domestication traits prove polygenic and intractable.",
                "Consumers reject unfamiliar grains despite improvement.",
            ],
            "note": "Orphan-pipeline explorer for de novo domestication.",
        },
    },
]

ENTRIES += [
    # ------------------------------------------------- 27 ADVANCED
    {
        "key": "synthetic-symbiosis",
        "name": "Synthetic Symbiosis: Engineering New Plant-Microbe Partnerships",
        "group": "Advanced",
        "ladder_rank": 27, "ladder_tier": "advanced",
        "problem": ("Legumes get nitrogen from rhizobia through a "
                    "symbiosis refined over 60 million years; cereals "
                    "get nothing comparable. Startups now sell "
                    "'nitrogen-fixing' microbes for maize and wheat, "
                    "but field nitrogen delivery is modest and "
                    "inconsistent - the microbes colonize poorly, fix "
                    "little, or lose to native competitors. The "
                    "unsolved problem is engineering reliability: "
                    "building synthetic partnerships - edited microbes, "
                    "engineered signaling, even synthetic organelles - "
                    "that deliver agronomic nitrogen to cereals as "
                    "dependably as rhizobia do to soybeans. It is the "
                    "pragmatic cousin of nitrogen-fixing cereals, "
                    "attacking the microbe side instead of the plant "
                    "side, and it is equally unclosed."),
        "background": ("The commercial starting gun was associative "
                       "nitrogen fixers like Azospirillum, sold for "
                       "decades with mixed results. The 2010s brought "
                       "venture-backed entrants - Pivot Bio's edited "
                       "Klebsiella for maize, Joyn Bio's engineered "
                       "microbes - with real science: microbes edited "
                       "to fix nitrogen in the presence of fertilizer, "
                       "colonizing cereal roots. Field results show "
                       "real but variable nitrogen delivery, typically "
                       "tens of kilograms per hectare - meaningful, "
                       "but far from replacing fertilizer. Academic "
                       "work pushes further: engineering nodule-like "
                       "structures on cereals, synthetic signaling "
                       "cascades, and nitrogenase in plant-associated "
                       "bacteria. The gap between 'microbe that fixes "
                       "nitrogen in a flask' and 'partnership that "
                       "feeds a maize crop' remains the industry's "
                       "central frustration."),
        "why_it_matters": ("If synthetic symbiosis worked reliably, it "
                           "would cut synthetic nitrogen demand "
                           "dramatically without waiting for the "
                           "harder plant-engineering breakthroughs. "
                           "Microbes are easier to iterate than crops - "
                           "a working partnership could deploy in "
                           "years, not decades."),
        "sig_pointer": ("The Signature edition proposes scoring "
                        "synthetic partnerships on delivered nitrogen "
                        "per hectare in real fields - colonization "
                        "times fixation times transfer - and funding "
                        "only what moves that product. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) delivered nitrogen "
                     "is the product of three measurable factors - "
                     "root colonization rate, nitrogen fixed per "
                     "microbe, and transfer efficiency to the plant; "
                     "(2) the binding factor is usually colonization "
                     "and persistence against native competitors, not "
                     "fixation biochemistry; (3) field measurement of "
                     "delivered nitrogen (15N tracing, yield response) "
                     "is the only score that matters. Reasoning path: "
                     "measure the three factors for each candidate "
                     "partnership in real fields, find the binding "
                     "factor, engineer specifically against it, and "
                     "re-measure - a product ledger per partnership. "
                     "Proposed mechanism: an independent 'delivered-"
                     "nitrogen registry' where every commercial "
                     "biological publishes third-party field nitrogen "
                     "delivery, and R&D funding follows the registry "
                     "leaders. What would confirm it: partnerships "
                     "delivering 50-plus kg N/ha reliably across "
                     "sites, with the registry separating winners "
                     "from hype. What would kill it: native soil "
                     "competition proving unbeatable - no introduced "
                     "microbe persists at functional densities. What "
                     "it does NOT claim: that microbes replace "
                     "fertilizer entirely, or that the registry "
                     "replaces regulation."),
        "key_points": [
            "Commercial nitrogen-fixing microbes deliver modest, inconsistent nitrogen to cereals.",
            "Delivered nitrogen = colonization x fixation rate x transfer efficiency.",
            "The binding factor is usually persistence against native competitors.",
            "Microbes iterate faster than crops - a working partnership could deploy in years.",
        ],
        "requirements": [
            "Measure all three factors - colonization, fixation, transfer - in real fields.",
            "Engineer specifically against the binding factor, then re-measure.",
            "Publish third-party delivered-nitrogen results in an open registry.",
        ],
        "standards": [
            "15N isotope tracing for nitrogen delivery; multi-site field trial standards.",
        ],
        "citations": CIT_BASE + [
            "Rosenblueth M, Martinez-Romero E. Bacterial endophytes and "
            "their interactions with hosts. Molecular Plant-Microbe "
            "Interactions; 2006.",
        ],
        "demo": {
            "calc": "prod", "quantity": "Engineered nitrogen supply share of crop need",
            "unit": "share", "formula": "colonization * fixation_rate * transfer_eff",
            "assumptions": [
                ("Root colonization rate", 0.70, [0.30, 0.70, 0.95]),
                ("Fixation rate index", 0.50, [0.10, 0.50, 0.80]),
                ("Transfer efficiency to plant", 0.60, [0.20, 0.60, 0.90]),
            ],
            "checks": [((0.30, 0.10, 0.20), 0.006, 1e-9),
                       ((0.95, 0.80, 0.90), 0.684, 1e-6)],
            "steps": [
                "Step 1: measure root colonization in the field.",
                "Step 2: measure nitrogen fixed per microbe.",
                "Step 3: measure transfer efficiency to the plant.",
                "Step 4: multiply into the delivered-nitrogen share.",
                "Step 5: engineer against the binding factor and re-measure.",
            ],
            "confirm": [
                "Partnerships deliver 50+ kg N/ha reliably across sites.",
                "The registry separates real winners from hype.",
            ],
            "refute": [
                "Native competition proves unbeatable for introduced microbes.",
                "Field delivery never approaches flask-level fixation.",
            ],
            "note": "Synthetic-symbiosis product explorer.",
        },
    },
    # ------------------------------------------------- 28 ADVANCED
    {
        "key": "crop-wild-relatives",
        "name": "Crop Wild Relatives: Mining the Gene Pool Before It Vanishes",
        "group": "Advanced",
        "ladder_rank": 28, "ladder_tier": "advanced",
        "problem": ("The wild cousins of crops hold the genes for "
                    "drought, heat, salt, and disease resistance that "
                    "breeding desperately needs - and they are going "
                    "extinct in the wild while sitting uncollected in "
                    "gene banks. Crop wild relatives (CWR) have "
                    "delivered some of breeding's greatest hits: "
                    "disease resistance in wheat, salt tolerance in "
                    "rice, drought genes in tomato. But collection "
                    "gaps are huge, many accessions are "
                    "uncharacterized, and habitat destruction erases "
                    "populations faster than collectors reach them. "
                    "The unsolved problem is triage at global scale: "
                    "which wild populations to collect, characterize, "
                    "and pre-breed first, before the genes are gone."),
        "background": ("CWR conservation became systematic with the "
                       "Global Crop Diversity Trust and the 2010s "
                       "Harlan-and-de-Wet inventory work, which mapped "
                       "how poorly wild relatives are represented in "
                       "gene banks - many taxa have zero or a handful "
                       "of accessions. Success stories prove the value: "
                       "the Sub1 submergence-tolerance gene came from "
                       "an Indian landrace, wheat's Sr resistance genes "
                       "from wild relatives, tomato's drought tolerance "
                       "from wild Solanum. Pre-breeding - moving wild "
                       "genes into usable breeding lines - is the slow "
                       "bridge between conservation and varieties, and "
                       "it is chronically underfunded because its "
                       "payoffs arrive decades later. Meanwhile "
                       "climate change shifts wild habitats, and "
                       "populations adapted to extreme conditions - "
                       "exactly the genes needed - are the most "
                       "threatened."),
        "why_it_matters": ("Every future breeding breakthrough for "
                           "heat, drought, salt, and new diseases will "
                           "likely come from wild genes. Losing CWR "
                           "populations is like burning a library of "
                           "solutions before reading it - and the fire "
                           "is already lit."),
        "sig_pointer": ("The Signature edition proposes a global CWR "
                        "triage ledger - threat times trait value times "
                        "collection gap - directing collectors to the "
                        "highest-priority populations first. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) priority can be "
                     "scored as extinction threat times breeding value "
                     "of likely traits times current collection gap; "
                     "(2) characterization (genotyping plus "
                     "phenotyping for stress traits) multiplies a "
                     "collection's value more than raw accession "
                     "counts; (3) pre-breeding must start at "
                     "collection, not decades later. Reasoning path: "
                     "score every CWR taxon-population on the triage "
                     "index, collect highest-priority first, "
                     "characterize immediately for stress traits, and "
                     "feed the best into pre-breeding pipelines. "
                     "Proposed mechanism: a public 'gene-pool triage "
                     "ledger' ranking wild populations by priority "
                     "score, with collection expeditions, "
                     "characterization, and pre-breeding funded "
                     "strictly in ledger order. What would confirm "
                     "it: priority populations secured before "
                     "extinction, and pre-bred lines delivering "
                     "stress traits to breeding programs. What would "
                     "kill it: trait values too uncertain to score, "
                     "or political barriers blocking collection in "
                     "priority regions. What it does NOT claim: that "
                     "collection replaces in-situ conservation, or "
                     "that every wild gene is usable."),
        "key_points": [
            "Crop wild relatives hold the stress-resistance genes breeding needs most.",
            "Many CWR taxa have zero or a handful of gene-bank accessions.",
            "Sub1, wheat Sr genes, and tomato drought genes all came from wild relatives.",
            "Habitat destruction erases extreme-adapted populations fastest.",
        ],
        "requirements": [
            "Score wild populations by threat times trait value times collection gap.",
            "Collect in ledger order; characterize for stress traits immediately.",
            "Start pre-breeding at collection, not decades later.",
        ],
        "standards": [
            "Harlan-and-de-Wet CWR inventory; Global Crop Diversity Trust priorities.",
        ],
        "citations": CIT_BASE + [
            "Dempewolf H et al. Past and future use of wild relatives in crop "
            "breeding. Crop Science; 2017.",
        ],
        "demo": {
            "calc": "min", "quantity": "Conservation chain bottleneck",
            "unit": "share", "formula": "min(collection chain shares)",
            "assumptions": [
                ("Priority populations collected", 0.60, [0.20, 0.60, 0.90]),
                ("Accessions viably stored", 0.85, [0.60, 0.85, 0.98]),
                ("Accessions characterized and usable", 0.50, [0.10, 0.50, 0.80]),
            ],
            "checks": [((0.20, 0.85, 0.10), 0.10, 1e-9),
                       ((0.90, 0.85, 0.80), 0.80, 1e-9)],
            "steps": [
                "Step 1: score wild populations on the triage index.",
                "Step 2: measure collection, storage, and characterization shares.",
                "Step 3: take the minimum - the bottleneck sets the system's value.",
                "Step 4: fund the bottleneck stage first.",
                "Step 5: feed characterized material into pre-breeding.",
            ],
            "confirm": [
                "Priority populations are secured before extinction.",
                "Pre-bred lines deliver stress traits to breeding programs.",
            ],
            "refute": [
                "Trait values prove too uncertain to score priorities.",
                "Political barriers block collection in priority regions.",
            ],
            "note": "Gene-pool triage explorer for crop wild relatives.",
        },
    },
    # ------------------------------------------------- 29 ADVANCED
    {
        "key": "multi-stress-stacking",
        "name": "Multi-Stress Stacking: Heat Plus Drought Plus Salt",
        "group": "Advanced",
        "ladder_rank": 29, "ladder_tier": "advanced",
        "problem": ("Real fields do not deliver one stress at a time: "
                    "heat arrives with drought, drought with salinity, "
                    "pests with all three - yet breeding still selects "
                    "for tolerance to single stresses in isolation. "
                    "Stress combinations interact unpredictably: a "
                    "gene that helps under drought alone can hurt "
                    "under drought-plus-heat, because the plant's "
                    "responses conflict. The unsolved problem is "
                    "combinatorial: testing every stress combination "
                    "is impossible, the physiology of combined stress "
                    "is poorly understood, and climate change is "
                    "making multi-stress seasons the norm rather than "
                    "the exception."),
        "background": ("Plant stress physiology grew up studying one "
                       "stress at a time - drought trials, heat "
                       "trials, salt trials - and the first systematic "
                       "studies of combined stresses in the 2000s-2010s "
                       "revealed the conflicts: drought demands stomatal "
                       "closure to save water while heat demands "
                       "transpiration to cool leaves, so "
                       "drought-plus-heat is not the sum of its parts "
                       "but a new stress entirely. Breeding programs "
                       "have begun multi-environment trials that "
                       "capture natural stress combinations, and "
                       "genomic selection can handle the complexity "
                       "statistically, but deliberately stacking "
                       "tolerance to three or four simultaneous "
                       "stresses in one variety remains rare. The "
                       "field reality keeps moving: the seasons that "
                       "break records are multi-stress seasons."),
        "why_it_matters": ("The variety that survives drought alone "
                           "dies in drought-plus-heat - which is what "
                           "the future actually delivers. Until "
                           "breeding targets stress combinations, "
                           "climate adaptation is aimed at a past that "
                           "no longer exists."),
        "sig_pointer": ("The Signature edition proposes breeding "
                        "directly against recorded multi-stress seasons "
                        "- selecting in the combinations, not the "
                        "components. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the relevant "
                     "selection environments are real multi-stress "
                     "seasons, which can be identified from historical "
                     "weather-plus-yield data; (2) tolerance to a "
                     "combination must be selected under that "
                     "combination - component tolerances do not "
                     "predict it; (3) managed-stress facilities can "
                     "reproduce the key combinations reproducibly. "
                     "Reasoning path: mine historical data for the "
                     "stress combinations that actually caused losses, "
                     "build managed environments reproducing the top "
                     "combinations, and select strictly under "
                     "combined stress - scoring varieties by "
                     "worst-combination performance. Proposed "
                     "mechanism: a 'combination-first' breeding "
                     "protocol where no variety advances on "
                     "single-stress merit alone, and release "
                     "requires performance under the region's "
                     "documented worst combinations. What would "
                     "confirm it: combination-selected varieties "
                     "outyielding component-selected ones in real "
                     "multi-stress seasons. What would kill it: "
                     "combinations too variable year to year for "
                     "any selection to target, or managed "
                     "environments that fail to reproduce field "
                     "combinations. What it does NOT claim: that "
                     "all combinations can be covered, or that "
                     "single-stress research was wasted."),
        "key_points": [
            "Real fields deliver stress combinations; breeding selects for single stresses.",
            "Drought-plus-heat is a new stress, not the sum of its parts.",
            "A gene helping under drought alone can hurt under drought-plus-heat.",
            "Record-breaking seasons are multi-stress seasons.",
        ],
        "requirements": [
            "Identify the stress combinations that actually caused losses from historical data.",
            "Select strictly under combined stress in managed environments.",
            "Require release performance under the region's documented worst combinations.",
        ],
        "standards": [
            "Multi-environment trial standards; managed-stress phenotyping protocols.",
        ],
        "citations": CIT_BASE + [
            "Mittler R. Abiotic stress, the field environment and stress "
            "combination. Trends in Plant Science; 2006.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Stacked-stress survival yield",
            "unit": "t/ha", "formula": "base_yield * heat_retention * drought_retention",
            "expr": "a0 * a1 * a2",
            "assumptions": [
                ("Base yield, no stress", 8.0, [6.0, 8.0, 10.0]),
                ("Yield retained under heat", 0.70, [0.40, 0.70, 0.90]),
                ("Yield retained under drought", 0.60, [0.30, 0.60, 0.85]),
            ],
            "checks": [((6.0, 0.40, 0.30), 0.72, 1e-9),
                       ((10.0, 0.90, 0.85), 7.65, 1e-6)],
            "steps": [
                "Step 1: identify the region's loss-causing stress combinations.",
                "Step 2: set retention under each component stress.",
                "Step 3: multiply into the combined-stress yield.",
                "Step 4: select new lines under the actual combination.",
                "Step 5: release only on worst-combination performance.",
            ],
            "confirm": [
                "Combination-selected varieties outyield component-selected ones in real seasons.",
                "Managed environments reproduce field combinations faithfully.",
            ],
            "refute": [
                "Combinations vary too much year to year to target.",
                "Managed environments fail to reproduce field combinations.",
            ],
            "note": "Combination-first explorer for multi-stress stacking.",
        },
    },
    # ------------------------------------------------- 30 ADVANCED
    {
        "key": "rhizosphere-signaling",
        "name": "The Rhizosphere Signaling Code",
        "group": "Advanced",
        "ladder_rank": 30, "ladder_tier": "advanced",
        "problem": ("Plant roots conduct a chemical conversation with "
                    "soil microbes - exudates, signals, quorum cues - "
                    "that decides which microbes colonize, which "
                    "nutrients unlock, and which pathogens are repelled. "
                    "Fragments of the code are known: strigolactones "
                    "summon mycorrhizal fungi (and parasitic weeds), "
                    "flavonoids beckon rhizobia, root exudates shape "
                    "entire communities. But the full grammar - who "
                    "says what to whom, in what order, with what "
                    "effect - remains undeciphered. The unsolved "
                    "problem is translation: reading and writing the "
                    "rhizosphere dialogue would let breeders select "
                    "for beneficial conversations instead of hoping "
                    "they happen."),
        "background": ("The molecular era began with the decoding of "
                       "Nod factors (lipochitooligosaccharides) in "
                       "rhizobia-legume signaling in the 1990s and "
                       "strigolactones as mycorrhizal signals in the "
                       "2000s. Metabolomics then revealed root exudates "
                       "as complex cocktails - sugars, amino acids, "
                       "secondary metabolites - that shift with plant "
                       "stress and development. Recent work shows "
                       "plants actively recruit beneficial microbes "
                       "under attack ('cry for help') and that "
                       "exudate profiles are heritable, hence "
                       "breedable. But the signal space is vast, "
                       "most exudate compounds are unidentified, "
                       "microbial responses are context-dependent, and "
                       "no one has yet bred a variety specifically for "
                       "its rhizosphere dialogue."),
        "why_it_matters": ("Whoever decodes the signaling code gains "
                           "a new breeding target as powerful as yield "
                           "itself: crops that assemble their own "
                           "beneficial microbiome, suppress their own "
                           "pathogens, and unlock their own nutrients. "
                           "It is the operating system beneath the "
                           "microbiome."),
        "sig_pointer": ("The Signature edition proposes decoding the "
                        "code in three ledgers - exudate chemistry, "
                        "microbial receptors, plant responses - and "
                        "breeding for dialogue traits once the ledgers "
                        "fill. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the signaling code "
                     "decomposes into three measurable ledgers: what "
                     "roots exude, which microbial receptors respond, "
                     "and what the plant gains; (2) exudate profiles "
                     "are heritable enough to breed for; (3) "
                     "decoding enough of the code enables 'dialogue "
                     "breeding' - selecting varieties for beneficial "
                     "microbial recruitment. Reasoning path: profile "
                     "exudates across diverse germplasm, map "
                     "microbial responses to key signals, link "
                     "signal variants to field outcomes "
                     "(nutrient uptake, disease), and select for the "
                     "signal variants that recruit help. Proposed "
                     "mechanism: a 'signal atlas' - open database of "
                     "root exudate compounds, microbial responses, "
                     "and field effects - feeding dialogue-trait "
                     "selection in breeding programs. What would "
                     "confirm it: varieties bred for signal variants "
                     "that assemble measurably better microbiomes "
                     "and outyield controls in low-input fields. "
                     "What would kill it: exudate heritability too "
                     "low to breed for, or microbial responses too "
                     "context-dependent to predict. What it does NOT "
                     "claim: that the full code will be decoded soon, "
                     "or that signaling replaces nutrition."),
        "key_points": [
            "Roots chemically summon mycorrhizae, rhizobia, and defenders - the code is partly known.",
            "Strigolactones and Nod factors are decoded fragments; most exudate compounds are unidentified.",
            "Exudate profiles are heritable, hence breedable in principle.",
            "No variety has yet been bred specifically for its rhizosphere dialogue.",
        ],
        "requirements": [
            "Build three ledgers: exudate chemistry, microbial receptors, plant responses.",
            "Link signal variants to field outcomes: nutrient uptake and disease.",
            "Select for signal variants that recruit beneficial microbiomes.",
        ],
        "standards": [
            "Metabolomics reporting standards; rhizosphere sampling protocols.",
        ],
        "citations": CIT_BASE + [
            "Venturi V, Keel C. Signaling in the rhizosphere. Trends in "
            "Plant Science; 2016.",
        ],
        "demo": {
            "calc": "sum1", "quantity": "Signal decoding completeness",
            "unit": "multiplier", "formula": "1 + exudate_map + receptor_map + response_map",
            "assumptions": [
                ("Exudate chemistry mapped", 0.30, [0.10, 0.30, 0.60]),
                ("Microbial receptors mapped", 0.25, [0.05, 0.25, 0.50]),
                ("Plant responses mapped", 0.20, [0.05, 0.20, 0.45]),
            ],
            "checks": [((0.10, 0.05, 0.05), 1.20, 1e-9),
                       ((0.60, 0.50, 0.45), 2.55, 1e-9)],
            "steps": [
                "Step 1: profile root exudates across diverse germplasm.",
                "Step 2: map microbial receptor responses to key signals.",
                "Step 3: link signal variants to field outcomes.",
                "Step 4: sum the three ledgers into decoding completeness.",
                "Step 5: breed for the signal variants that recruit help.",
            ],
            "confirm": [
                "Dialogue-bred varieties assemble better microbiomes in low-input fields.",
                "Signal variants predict nutrient uptake and disease outcomes.",
            ],
            "refute": [
                "Exudate heritability proves too low to breed for.",
                "Microbial responses are too context-dependent to predict.",
            ],
            "note": "Signal-atlas explorer for the rhizosphere code.",
        },
    },
    # ------------------------------------------------- 31 ADVANCED
    {
        "key": "regenerative-scale",
        "name": "Regenerative Agriculture at Global Scale",
        "group": "Advanced",
        "ladder_rank": 31, "ladder_tier": "advanced",
        "problem": ("Regenerative agriculture - cover crops, no-till, "
                    "diverse rotations, managed grazing - promises to "
                    "rebuild soil carbon while farming, but at global "
                    "scale the claims outrun the measurements. Soil "
                    "carbon gains are real but slow, reversible, and "
                    "hard to verify: a tonne sequestered this decade "
                    "can be re-released by one tillage pass, and "
                    "measurement costs often exceed the carbon value. "
                    "The unsolved problem is MRV at scale - "
                    "measurement, reporting, verification cheap and "
                    "honest enough for carbon markets - plus the "
                    "deeper question of which practices actually "
                    "build stable carbon versus merely cycling it."),
        "background": ("The '4 per 1000' initiative, launched at COP21 "
                       "in 2015, proposed raising soil carbon 0.4 "
                       "percent yearly to offset emissions - a "
                       "galvanizing target that scientists quickly "
                       "qualified as optimistic. Carbon programs "
                       "paying farmers for soil carbon multiplied in "
                       "the 2020s, but controversies followed: "
                       "additionality disputes, reversal risks, and "
                       "sampling costs that eat the payment. The "
                       "science meanwhile sharpened: stable carbon "
                       "forms through microbial necromass and mineral "
                       "association, not just raw organic matter, "
                       "which means not all 'regenerative' practices "
                       "build lasting carbon equally. Remote sensing "
                       "and modeling promise cheaper MRV, but ground "
                       "truth remains expensive."),
        "why_it_matters": ("Soils hold more carbon than the atmosphere "
                           "and vegetation combined - small percentage "
                           "gains are globally huge. But a carbon "
                           "market built on unverifiable claims "
                           "discredits the whole enterprise and wastes "
                           "the decade. Honest MRV is the difference "
                           "between a climate solution and a "
                           "greenwashing machine."),
        "sig_pointer": ("The Signature edition proposes paying only "
                        "for verified, reversal-discounted carbon - "
                        "with the discount published - so honest MRV "
                        "outcompetes inflated claims. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) soil carbon can be "
                     "verified at scale by combining sparse ground "
                     "sampling with remote sensing and calibrated "
                     "models - at a cost below the carbon value; (2) "
                     "reversal risk is real and must be priced as a "
                     "discount, not ignored; (3) markets that pay "
                     "only verified tonnes will drive MRV innovation "
                     "faster than markets that pay claims. Reasoning "
                     "path: enroll fields, baseline carbon with "
                     "ground truth, track practice and remote-sensing "
                     "indicators annually, re-sample on a schedule, "
                     "apply a published reversal discount, and pay "
                     "only the verified net tonnes. Proposed "
                     "mechanism: a 'verified-tonne standard' where "
                     "every soil carbon credit carries its MRV method "
                     "and reversal discount on its face, letting "
                     "buyers price honesty. What would confirm it: "
                     "credit prices converging on verified tonnes, "
                     "and enrolled fields showing measured gains "
                     "net of reversals. What would kill it: MRV "
                     "costs that permanently exceed carbon prices, "
                     "or reversal rates so high that net gains "
                     "vanish. What it does NOT claim: that soil "
                     "carbon offsets fossil emissions one-to-one, or "
                     "that every regenerative practice builds stable "
                     "carbon."),
        "key_points": [
            "Soils hold more carbon than atmosphere and vegetation combined.",
            "Soil carbon gains are slow, reversible, and costly to verify.",
            "The 4-per-1000 target galvanized action but was scientifically optimistic.",
            "Stable carbon forms via microbial necromass and mineral association - not all practices build it.",
        ],
        "requirements": [
            "Verify with ground sampling plus remote sensing and calibrated models.",
            "Apply a published reversal discount to every credited tonne.",
            "Pay only verified net tonnes; put the MRV method on the credit's face.",
        ],
        "standards": [
            "4 per 1000 initiative; Verra/Gold Standard soil carbon methodologies.",
        ],
        "citations": CIT_BASE + [
            "Minasny B et al. Soil carbon 4 per mille. Geoderma; 2017.",
        ],
        "demo": {
            "calc": "expr", "quantity": "Verified soil carbon credits per year",
            "unit": "Mt CO2e/yr", "formula": "enrolled_area * per_ha_t * (1 - reversal_discount_pct/100)",
            "expr": "a0 * a1 * (1 - a2 / 100.0)",
            "assumptions": [
                ("Enrolled area (Mha)", 500, [100, 500, 1000]),
                ("Carbon per hectare per year (t)", 0.8, [0.3, 0.8, 1.5]),
                ("Reversal discount percent", 20, [10, 20, 40]),
            ],
            "checks": [((100, 0.3, 10), 27.0, 1e-9),
                       ((1000, 1.5, 40), 900.0, 1e-9)],
            "steps": [
                "Step 1: enroll fields and baseline carbon with ground truth.",
                "Step 2: track practices and remote-sensing indicators annually.",
                "Step 3: compute gross tonnes and apply the reversal discount.",
                "Step 4: re-sample on schedule to verify.",
                "Step 5: pay only verified net tonnes.",
            ],
            "confirm": [
                "Credit prices converge on verified tonnes.",
                "Enrolled fields show measured gains net of reversals.",
            ],
            "refute": [
                "MRV costs permanently exceed carbon prices.",
                "Reversal rates erase net gains.",
            ],
            "note": "Verified-tonne explorer for regenerative scale.",
        },
    },
    # ------------------------------------------------- 32 ADVANCED
    {
        "key": "controlled-environment-staples",
        "name": "Controlled-Environment Staples at Calorie Scale",
        "group": "Advanced",
        "ladder_rank": 32, "ladder_tier": "advanced",
        "problem": ("Vertical farms grow lettuce brilliantly and go "
                    "bankrupt quietly: the economics work for leafy "
                    "greens and herbs, not for the calorie crops - "
                    "wheat, rice, maize - that feed humanity. Staples "
                    "need roughly 100 times more energy per calorie "
                    "than greens, because photosynthesis is "
                    "inefficient and sunlight is free. The unsolved "
                    "problem is physics plus economics: controlled "
                    "environments can perfect the growing conditions, "
                    "but they cannot repeal the energy cost of turning "
                    "photons into starch. Dozens of vertical-farm "
                    "startups have failed learning this; the question "
                    "is whether any configuration - ultra-cheap "
                    "energy, dwarf cereals, hybrid greenhouse-vertical "
                    "systems - can ever grow calories competitively."),
        "background": ("Plant factories emerged in Japan in the 2000s-"
                       "2010s, and the 2010s-2020s saw a venture boom: "
                       "AeroFarms, Plenty, Bowery and others raised "
                       "billions to grow greens indoors. The technology "
                       "is genuinely impressive - 95 percent less water, "
                       "no pesticides, year-round harvests. But the "
                       "bankruptcies of the 2020s exposed the calorie "
                       "wall: analyses show vertical wheat would cost "
                       "tens of times field wheat even with optimistic "
                       "LED efficiency, because a kilogram of wheat "
                       "needs far more photons than a kilogram of "
                       "lettuce. Research continues on dwarf cereals "
                       "for indoor systems and on using controlled "
                       "environments for seed production and breeding "
                       "speed rather than bulk calories."),
        "why_it_matters": ("If controlled environments could grow "
                           "staples economically, farming could retreat "
                           "from marginal land, survive any climate, "
                           "and stack vertically near cities. If they "
                           "cannot, billions in investment are chasing "
                           "greens while the calorie problem stays in "
                           "the field. Honest accounting decides which."),
        "sig_pointer": ("The Signature edition proposes a calorie-cost "
                        "ledger - cost per food calorie by system - "
                        "that kills or validates each configuration "
                        "against physics before capital is spent. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the binding "
                     "constraint is energy per calorie, set by "
                     "photosynthetic efficiency and LED costs - "
                     "physics, not business models; (2) honest "
                     "comparison requires full cost per delivered "
                     "calorie against field production; (3) "
                     "controlled environments may still win at "
                     "non-calorie roles: seed, breeding speed, "
                     "nurseries, high-value crops. Reasoning path: "
                     "compute the photon-to-calorie cost for each "
                     "configuration (vertical, greenhouse, hybrid), "
                     "compare against field cost per calorie, fund "
                     "only configurations within striking distance, "
                     "and redirect the rest to seed and breeding "
                     "roles where the economics work. Proposed "
                     "mechanism: a public 'calorie-cost ledger' "
                     "publishing cost-per-calorie for every major "
                     "controlled-environment configuration, updated "
                     "as LED and energy costs move. What would "
                     "confirm it: a configuration reaching cost "
                     "parity for a staple in some market, or the "
                     "ledger cleanly redirecting capital to "
                     "seed-and-breeding roles. What would kill it: "
                     "energy costs that never fall enough, or "
                     "dwarf-cereal yields indoors that never "
                     "justify the facility. What it does NOT "
                     "claim: that vertical farms are worthless - "
                     "only that calories are the wrong product for "
                     "most of them."),
        "key_points": [
            "Vertical farms excel at greens but fail at calorie crops.",
            "Staples need roughly 100x more energy per calorie than lettuce.",
            "2020s bankruptcies exposed the calorie wall.",
            "Dwarf cereals and seed/breeding roles may be the viable indoor niches.",
        ],
        "requirements": [
            "Compute full cost per delivered calorie for each configuration.",
            "Compare honestly against field production before spending capital.",
            "Redirect non-competitive configurations to seed and breeding roles.",
        ],
        "standards": [
            "Photon-efficacy benchmarks; cost-per-calorie accounting standards.",
        ],
        "citations": CIT_BASE + [
            "Asseng S et al. Wheat yield potential in controlled-environment "
            "agriculture. (controlled-environment crop analyses).",
        ],
        "demo": {
            "calc": "expr", "quantity": "Cost per calorie multiple vs field",
            "unit": "multiple", "formula": "facility_cost / (energy_eff * light_util)",
            "expr": "a0 / (a1 * a2)",
            "assumptions": [
                ("Facility cost index", 40, [20, 40, 80]),
                ("Energy efficiency index", 0.5, [0.2, 0.5, 0.9]),
                ("Light utilization index", 0.8, [0.4, 0.8, 1.0]),
            ],
            "checks": [((20, 0.2, 0.4), 250.0, 1e-9),
                       ((80, 0.9, 1.0), 88.888889, 1e-6)],
            "steps": [
                "Step 1: set the facility cost index for the configuration.",
                "Step 2: set energy efficiency and light utilization.",
                "Step 3: compute the cost-per-calorie multiple vs field.",
                "Step 4: fund only configurations within striking distance of parity.",
                "Step 5: redirect the rest to seed and breeding roles.",
            ],
            "confirm": [
                "A configuration reaches cost parity for a staple in some market.",
                "The ledger redirects capital to viable indoor roles.",
            ],
            "refute": [
                "Energy costs never fall enough for calorie parity.",
                "Indoor dwarf-cereal yields never justify the facility.",
            ],
            "note": "Calorie-cost ledger explorer for controlled-environment staples.",
        },
    },
    # ------------------------------------------------- 33 ADVANCED
    {
        "key": "one-health-farm",
        "name": "One Health at the Farm Gate: AMR and Spillover",
        "group": "Advanced",
        "ladder_rank": 33, "ladder_tier": "advanced",
        "problem": ("Intensive livestock is a crucible for the two "
                    "greatest biological threats of the century: "
                    "antimicrobial resistance (AMR) and zoonotic "
                    "spillover. Agriculture uses the majority of the "
                    "world's antibiotics by volume, much of it for "
                    "growth promotion and routine prevention, "
                    "accelerating resistant bacteria that then reach "
                    "people through food, water, and workers. "
                    "Meanwhile crowded animals near wildlife and "
                    "people create spillover interfaces for novel "
                    "pathogens. The unsolved problem is structural: "
                    "the economic logic of intensive production "
                    "rewards the very practices - crowding, routine "
                    "antibiotics, weak biosecurity - that generate "
                    "the risks, and surveillance is thinnest where "
                    "production is growing fastest."),
        "background": ("The AMR alarm was raised by the 2014-2016 "
                       "O'Neill Review, which projected 10 million "
                       "annual deaths by 2050 if resistance keeps "
                       "rising, and by WHO's listing of resistant "
                       "pathogens as critical priorities. Agriculture's "
                       "share was documented in sales data: most "
                       "antibiotics by volume go to animals. The EU "
                       "banned growth promoters in 2006; the US ended "
                       "them in 2017 - and production did not collapse, "
                       "proving alternatives exist. On spillover, "
                       "Nipah virus (1998, pigs), H5N1 avian influenza, "
                       "and African swine fever showed how farm "
                       "interfaces seed pandemics and panzootics. One "
                       "Health - the doctrine that human, animal, and "
                       "environmental health are one system - is now "
                       "official policy in many countries, but farm-"
                       "gate implementation lags far behind the "
                       "rhetoric."),
        "why_it_matters": ("AMR already kills over a million people a "
                           "year; the next pandemic may well come "
                           "through a farm. Food production that "
                           "breeds untreatable infections or novel "
                           "viruses is not feeding the future - it is "
                           "endangering it."),
        "sig_pointer": ("The Signature edition proposes farm-gate One "
                        "Health scores - biosecurity, antibiotic "
                        "stewardship, surveillance - published per "
                        "operation and priced into markets. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) farm-level AMR and "
                     "spillover risk can be scored from auditable "
                     "practices: antibiotic use records, biosecurity "
                     "measures, surveillance participation, wildlife "
                     "interface management; (2) buyers and insurers "
                     "will pay for low-risk supply when the score is "
                     "credible; (3) the transition is affordable - the "
                     "EU and US growth-promoter bans prove production "
                     "survives stewardship. Reasoning path: define "
                     "the farm-gate score, audit operations, publish "
                     "scores, and let procurement contracts and "
                     "insurance premiums reward low-risk farms - "
                     "making One Health a market advantage instead of "
                     "a cost. Proposed mechanism: a 'One Health "
                     "ledger' per operation with public scores, where "
                     "retailers commit to sourcing thresholds and "
                     "insurers discount premiums for high scores. "
                     "What would confirm it: scored supply chains "
                     "showing falling antibiotic use and fewer "
                     "outbreaks with stable production. What would "
                     "kill it: audit fraud, or buyers refusing to "
                     "pay any premium for scored supply. What it does "
                     "NOT claim: that scoring eliminates spillover "
                     "risk, or that extensive systems are risk-free."),
        "key_points": [
            "Agriculture uses most of the world's antibiotics by volume.",
            "AMR already kills over a million people yearly; farm practices accelerate it.",
            "Growth-promoter bans in the EU and US did not collapse production.",
            "Crowded farm interfaces seed zoonotic spillover: Nipah, H5N1, African swine fever.",
        ],
        "requirements": [
            "Score each operation on biosecurity, stewardship, and surveillance.",
            "Publish farm-gate One Health scores openly.",
            "Reward low-risk farms through procurement thresholds and insurance discounts.",
        ],
        "standards": [
            "WHO AMR surveillance standards; OIE/WOAH biosecurity guidelines.",
        ],
        "citations": CIT_BASE + [
            "O'Neill J. Review on Antimicrobial Resistance: final report. "
            "2016.",
        ],
        "demo": {
            "calc": "sum", "quantity": "Spillover-risk reduction stack",
            "unit": "points", "formula": "biosecurity + surveillance + amr_stewardship",
            "assumptions": [
                ("Biosecurity score", 30, [10, 30, 50]),
                ("Surveillance score", 25, [5, 25, 45]),
                ("AMR stewardship score", 20, [5, 20, 40]),
            ],
            "checks": [((10, 5, 5), 20, 1e-9),
                       ((50, 45, 40), 135, 1e-9)],
            "steps": [
                "Step 1: audit the operation's biosecurity, surveillance, and stewardship.",
                "Step 2: sum into the One Health score.",
                "Step 3: publish the score on the farm-gate ledger.",
                "Step 4: link procurement and insurance to the score.",
                "Step 5: re-audit annually and track outbreak trends.",
            ],
            "confirm": [
                "Scored supply chains show falling antibiotic use and fewer outbreaks.",
                "Production holds steady under stewardship, as the bans proved.",
            ],
            "refute": [
                "Audit fraud destroys score credibility.",
                "Buyers refuse any premium for scored supply.",
            ],
            "note": "One Health ledger explorer for the farm gate.",
        },
    },
    # ------------------------------------------------- 34 ADVANCED
    {
        "key": "yield-ceiling",
        "name": "The Ultimate Yield Ceiling: Theoretical Limits of Crops",
        "group": "Advanced",
        "ladder_rank": 34, "ladder_tier": "advanced",
        "problem": ("Every crop has a theoretical maximum yield set by "
                    "physics - sunlight intercepted, photosynthetic "
                    "efficiency, harvest index - and in the best "
                    "farms, major cereals are approaching it. Dutch "
                    "and Australian wheat growers, Japanese rice "
                    "farmers, and US maize producers already harvest "
                    "80 percent or more of estimated potential in "
                    "good years. The unsolved problem is what comes "
                    "after the ceiling: if conventional breeding "
                    "and management can only asymptotically approach "
                    "a fixed limit, then future food growth must come "
                    "from raising the ceiling itself - redesigned "
                    "photosynthesis, new crop architectures, novel "
                    "production systems - and no one knows which "
                    "ceiling-raising bets will pay, or when the "
                    "current ceiling binds globally."),
        "background": ("Yield potential theory was formalized by De "
                       "Wit, Evans, and Fischer from the 1960s-80s: "
                       "potential yield equals intercepted radiation "
                       "times conversion efficiency times harvest "
                       "index. The numbers are sobering - C3 crops "
                       "convert at best about 4.6 percent of "
                       "intercepted sunlight to biomass long-term "
                       "(Zhu, Long, and Ort's 2010 analysis), and "
                       "harvest indices near 0.6 are already achieved. "
                       "This frames every other entry in this database: "
                       "C4 rice, perennial grains, and photosynthesis "
                       "upgrades are all ceiling-raising bets, while "
                       "yield-gap closure merely approaches the "
                       "existing ceiling. The strategic question - "
                       "how to split investment between approaching "
                       "the ceiling and raising it - has no settled "
                       "answer, and the answer differs by crop and "
                       "decade."),
        "why_it_matters": ("This is the master equation behind the "
                           "master problem: feeding 10 billion depends "
                           "on whether the ceiling can be raised "
                           "faster than population and diets press "
                           "against it. Misjudging the ceiling means "
                           "either underinvesting in breakthrough "
                           "research or overselling incremental gains."),
        "sig_pointer": ("The Signature edition proposes a "
                        "ceiling-watch system - tracking each major "
                        "crop's approach to its theoretical limit - "
                        "that shifts research funding from "
                        "ceiling-approaching to ceiling-raising work "
                        "as the gap closes. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) each major crop-"
                     "region system has an estimable theoretical "
                     "ceiling from radiation, efficiency, and harvest "
                     "index; (2) the distance to the ceiling is "
                     "measurable from top-farm yields versus modeled "
                     "potential; (3) research portfolios should shift "
                     "weight from approaching to raising the ceiling "
                     "as the distance shrinks. Reasoning path: "
                     "compute the ceiling per crop-region, track the "
                     "approach rate from trial and farm data, and "
                     "rebalance funding - more ceiling-raising bets "
                     "(photosynthesis, architecture, new systems) as "
                     "approach nears completion. Proposed mechanism: "
                     "a published 'ceiling watch' per crop that "
                     "reports distance-to-ceiling and the portfolio "
                     "split, forcing research strategy into the open. "
                     "What would confirm it: ceiling-raising bets "
                     "delivering measured potential gains as top "
                     "farms plateau. What would kill it: ceilings "
                     "so uncertain that the watch misguides funding, "
                     "or ceiling-raising research that never "
                     "delivers. What it does NOT claim: that the "
                     "ceiling is known precisely, or that approaching "
                     "it is finished anywhere yet."),
        "key_points": [
            "Top farms already harvest 80+ percent of estimated yield potential.",
            "C3 crops convert at best ~4.6 percent of intercepted sunlight long-term.",
            "Harvest indices near 0.6 are already achieved in cereals.",
            "Future growth must come from raising the ceiling, not just approaching it.",
        ],
        "requirements": [
            "Compute the theoretical ceiling per crop-region from radiation, efficiency, harvest index.",
            "Track the approach rate from top-farm and trial data.",
            "Rebalance research funding toward ceiling-raising bets as the gap closes.",
        ],
        "standards": [
            "De Wit / Evans / Fischer yield potential theory; Zhu, Long, and Ort efficiency limits.",
        ],
        "citations": CIT_BASE + [
            "Zhu XG, Long SP, Ort DR. Improving photosynthetic efficiency for "
            "greater yield. Annual Review of Plant Biology; 2010.",
        ],
        "demo": {
            "calc": "gain", "quantity": "Yield at ceiling approach",
            "unit": "t/ha", "formula": "baseline_yield / (1 - ceiling_approach)",
            "planck": 3.0, "f_base": 0.0,
            "assumptions": [
                ("Ceiling approach factor", 0.60, [0.30, 0.60, 0.85]),
            ],
            "checks": [((0.30,), 4.285714, 1e-6),
                       ((0.85,), 20.0, 1e-9)],
            "steps": [
                "Step 1: compute the theoretical ceiling for the crop-region.",
                "Step 2: set the approach factor from top-farm yields.",
                "Step 3: compute yield at the current approach.",
                "Step 4: track the approach rate over years.",
                "Step 5: shift funding to ceiling-raising bets as the gap closes.",
            ],
            "confirm": [
                "Ceiling-raising bets deliver measured potential gains as top farms plateau.",
                "Portfolio splits track the published ceiling watch.",
            ],
            "refute": [
                "Ceilings prove too uncertain; the watch misguides funding.",
                "Ceiling-raising research never delivers measured gains.",
            ],
            "note": "Ceiling-watch explorer for the ultimate yield limit.",
        },
    },
]
