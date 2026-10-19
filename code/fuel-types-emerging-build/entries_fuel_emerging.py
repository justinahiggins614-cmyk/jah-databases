#!/usr/bin/env python3
"""Entries for The Emerging Fuel Types Database (fuel track 2 of 3, 2026-10-17).

Manon's 2026-10-17 17:55 order: "New types of fuel databases" - three
tracks: established fuels (track 1, sibling), NEW/EMERGING fuels (this
build, track 2), speculated fuels (track 3, sibling). This build keeps its
records strictly to emerging fuels: production routes that are real and
documented but not yet deployed at the scale of conventional fuels -
pilot, demonstration, first-commercial, and early-commercial stage.

34 public records (public-harvest: real, fact-checked emerging-fuel
knowledge - status, technology readiness level, production routes, and
honest maturity framing; pilot-stage technology is NEVER presented as
deployed; standard references: IEA, IRENA, U.S. DOE, NREL, ASTM, ISO,
ICAO CORSIA, plus the landmarks cited per record) + 34 Signature records
(his original Signature fuel designs and pathway analyses: Signature
re-engineerings of each emerging pathway - optimized reactor concepts,
Signature efficiency analyses, and original deployment designs; src
signature, titles suffixed " (Signature Edition)", clearly labeled
Signature-made, never presented as authentic public record).

Ladder: ranks 1-34, one rank per record, foundations (1-12) ->
compounded (13-23) -> advanced (24-34). The shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-FUE- (public) and JAH-FUES- (signature), verified free
in the manifest id_prefix values and in every data-1 shard index record
ID (zero hits), and the fuel-types-emerging slugs are absent from the
manifest and from the data-1 data dirs. Distinct from track 1
(fuel-types) and track 3 (fuel-types-speculated) by title and subject.

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_fuel_emerging.py). Every demo prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker naming the record; the build machine-executes all 68 demos.

Screened: nothing hate-adjacent, profane, or inappropriate; no religious
talk. Nothing on neutralizing or defeating military or defense-grade
systems. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature fuel design and "
            "pathway analysis: a Signature re-engineering of the emerging "
            "fuel pathway with optimized reactor concepts, Signature "
            "efficiency analysis, and original deployment designs. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_IEA_H2 = ("International Energy Agency. Global Hydrogen Review 2024. "
              "IEA, Paris.")
CIT_IEA_ETP = ("International Energy Agency. Energy Technology Perspectives "
               "2024. IEA, Paris.")
CIT_IRENA_H2 = ("International Renewable Energy Agency. Green Hydrogen Cost "
                "Reduction: Scaling up Electrolysers to Meet the 1.5C Climate "
                "Goal. IRENA, Abu Dhabi, 2020.")
CIT_DOE_H2 = ("U.S. Department of Energy. Hydrogen Shot: 1 1 1 - $1 per 1 kg "
              "in 1 decade. Hydrogen Program Plan, 2021.")
CIT_ISO_14687 = ("ISO 14687:2019. Hydrogen fuel quality - Product "
                 "specification.")
CIT_IEA_NH3 = ("International Energy Agency. Ammonia Technology Roadmap: "
                "Towards More Sustainable Nitrogen Fertiliser Production. "
                "IEA, Paris, 2021.")
CIT_IRENA_NH3 = ("International Renewable Energy Agency. Innovation Outlook: "
                 "Renewable Ammonia. IRENA, Abu Dhabi, 2022.")
CIT_IEA_SAF = ("International Energy Agency. Sustainable Aviation Fuels. "
                "IEA Energy Technology RD&D / tracking report, 2024.")
CIT_ASTM_D7566 = ("ASTM D7566-24. Standard Specification for Aviation Turbine "
                  "Fuel Containing Synthesized Hydrocarbons.")
CIT_CORSIA = ("International Civil Aviation Organization. CORSIA Eligible "
               "Fuels - life cycle assessment methodology; ICAO document "
               "CORSIA-SARPs.")
CIT_DOE_SAF = ("U.S. Department of Energy. Sustainable Aviation Fuel Grand "
               "Challenge Roadmap: Flight Plan for Sustainable Aviation Fuel, "
               "2022.")
CIT_ASTM_D975 = ("ASTM D975-24. Standard Specification for Diesel Fuel.")
CIT_EN15940 = ("EN 15940:2023. Automotive fuels - Paraffinic diesel fuel from "
               "synthesis or hydrotreatment - Requirements and test methods.")
CIT_DOE_BIO = ("U.S. Department of Energy, Bioenergy Technologies Office. "
               "Biofuel technology readiness assessments; Multi-Year Program "
               "Plan, 2023.")
CIT_NREL = ("National Renewable Energy Laboratory. Techno-economic analyses "
             "of emerging biofuel pathways. NREL, Golden, Colorado.")
CIT_IRENA_BIO = ("International Renewable Energy Agency. Advanced biofuels: "
                 "What holds them back? IRENA, Abu Dhabi, 2019.")
CIT_IEA_BIO = ("International Energy Agency. Renewables 2024 - Bioenergy "
               "chapter: transport biofuels. IEA, Paris.")
CIT_ISO_15403 = ("ISO 15403:2006. Natural gas - Natural gas for use as a "
                 "compressed fuel for vehicles.")
CIT_IEA_LOHC = ("International Energy Agency. The Future of Hydrogen, "
                 "Chapter 3: Hydrogen transport and storage. IEA, Paris, "
                 "2019.")
CIT_DOE_FC = ("U.S. Department of Energy, Fuel Cell Technologies Office. "
               "Fuel cell technology status and targets; solid oxide fuel "
               "cell program records.")

ENTRIES = [
    {
        "key": "green_h2_electrolysis",
        "name": "Green Hydrogen from Water Electrolysis",
        "group": "Hydrogen and Power-to-X",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Green hydrogen is hydrogen produced by splitting water with "
            "electricity from renewable sources, so that no carbon dioxide "
            "is emitted in the production step itself. It is the foundation "
            "molecule of the emerging fuel economy: nearly every other "
            "record in this database - green ammonia, e-methanol, e-fuels, "
            "synthetic methane, LOHC charging, ammonia cracking feedstock - "
            "starts from it. Water electrolysis itself is a mature "
            "technology (TRL 9 for the stack), but GREEN hydrogen at "
            "industrial scale is still emerging: dedicated renewable-powered "
            "electrolyzer plants in the hundreds of megawatts are under "
            "construction or recently commissioned, while the great majority "
            "of the roughly 95 million tonnes of hydrogen used worldwide "
            "each year is still grey hydrogen from steam methane reforming. "
            "Honest framing: electrolysis works; cheap, abundant green "
            "hydrogen does not yet exist at the scale the roadmaps assume."
        ),
        "how_it_works": (
            "An electrolyzer passes direct current through water, splitting "
            "it into hydrogen at the cathode and oxygen at the anode: "
            "2 H2O -> 2 H2 + O2. Three stack families dominate: alkaline "
            "(liquid KOH electrolyte, the workhorse, ~60-70 percent "
            "efficiency on a lower-heating-value basis), proton-exchange "
            "membrane or PEM (solid polymer electrolyte, fast response, "
            "suited to variable renewables), and solid-oxide electrolysis "
            "(high-temperature ceramic cells, highest electrical efficiency "
            "but still pre-commercial at scale). Producing one kilogram of "
            "hydrogen - which carries 33.3 kWh of lower-heating-value "
            "energy - takes about 50 to 55 kWh of electricity in a "
            "commercial system, the rest lost as heat. The hydrogen is "
            "dried, compressed (typically 350 or 700 bar for mobility, or "
            "fed to pipelines), and must meet ISO 14687 purity for fuel "
            "cell use."
        ),
        "key_points": [
            "Energy content: 33.3 kWh per kg lower heating value (120 MJ/kg); 39.4 kWh/kg higher heating value.",
            "Commercial electrolyzers consume roughly 50-55 kWh of electricity per kg of hydrogen (60-70 percent LHV efficiency).",
            "Three stack families: alkaline (mature), PEM (flexible, renewable-following), solid-oxide (highest efficiency, emerging).",
            "Green means renewable electricity in; the same stack fed by grid electricity is not green.",
            "Fuel-cell-grade hydrogen must meet ISO 14687 purity (contaminants poison PEM fuel cells).",
            "Status: stack technology TRL 9; gigawatt-scale green hydrogen plants TRL 7-8 (demonstration to first commercial).",
        ],
        "requirements": [
            "Renewable electricity supply matched to electrolyzer capacity (capacity factor drives cost).",
            "Purified water feed (about 9 litres stoichiometric per kg H2; real plants use more with cooling).",
            "Hydrogen drying, compression, and storage or offtake infrastructure.",
            "Safety systems for hydrogen handling (leak detection, ventilation, materials rated for embrittlement).",
        ],
        "standards": [
            "ISO 14687:2019 - hydrogen fuel quality specification.",
            "ISO 19880 series - gaseous hydrogen fueling stations.",
            "IEC 62282 series - fuel cell technologies (stack safety and performance).",
        ],
        "citations": [CIT_IEA_H2, CIT_IRENA_H2, CIT_DOE_H2, CIT_ISO_14687],
        "sig_lens": (
            "Signature re-engineering: a Signature electrolyzer plant "
            "architecture that pairs oversized PEM capacity with curtailed "
            "renewable power, adds waste-heat capture from compression "
            "intercoolers to preheat feed water, and schedules stack "
            "operation against a Signature price-signal controller so the "
            "plant only draws power below a target electricity price. The "
            "Signature efficiency analysis shows where the 50-55 kWh/kg "
            "budget goes - stack overpotential, power electronics, drying, "
            "compression - and sizes each stage so no single stage dominates "
            "losses."
        ),
    },
    {
        "key": "green_ammonia",
        "name": "Green Ammonia by Renewable Haber-Bosch",
        "group": "Hydrogen and Power-to-X",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Green ammonia is ammonia (NH3) synthesized from green hydrogen "
            "and nitrogen separated from air, using renewable electricity "
            "for the whole chain. Ammonia matters as a fuel because it is a "
            "practical hydrogen carrier: it liquefies at minus 33 C at "
            "atmospheric pressure (or about 10 bar at room temperature), "
            "carries 17.6 percent hydrogen by mass, and already moves around "
            "the world in a mature 180-million-tonne-per-year trade for "
            "fertilizer. Grey ammonia - made with hydrogen from natural gas "
            "- is TRL 9 and fully commercial; GREEN ammonia is emerging, "
            "with first large plants (hundreds of thousands of tonnes per "
            "year) under construction and smaller demonstration plants "
            "operating. Honest framing: the synthesis loop is proven, but "
            "no green ammonia plant has yet run a full year at nameplate on "
            "variable renewables."
        ),
        "how_it_works": (
            "Nitrogen is separated from air (cryogenic distillation or "
            "pressure-swing adsorption), green hydrogen comes from water "
            "electrolysis, and the two feed the Haber-Bosch loop: "
            "N2 + 3 H2 -> 2 NH3 over an iron-based catalyst at 400-500 C "
            "and 150-250 bar. Only about 15 percent converts per pass, so "
            "unreacted gases are recycled. The loop is happiest running "
            "steady, which clashes with variable renewable power - the "
            "central engineering challenge of green ammonia is buffering "
            "(hydrogen storage, flexible operation) so the synthesis loop "
            "sees stable feed. Ammonia's lower heating value is 18.6 MJ/kg; "
            "as a fuel it burns slowly and needs combustion support or "
            "cracking back to hydrogen (see the ammonia records later in "
            "this database)."
        ),
        "key_points": [
            "Ammonia carries 17.6 wt percent hydrogen and liquefies at -33 C (1 atm) or ~10 bar at 25 C.",
            "Haber-Bosch: N2 + 3 H2 -> 2 NH3, iron catalyst, 400-500 C, 150-250 bar, ~15 percent per-pass conversion.",
            "Lower heating value 18.6 MJ/kg - less than half of diesel, so fuel use needs volume.",
            "A global ammonia trade, terminals, and safety practice already exist from the fertilizer industry.",
            "Key challenge: steady-state synthesis loop versus variable renewable power (buffering required).",
            "Status: grey ammonia TRL 9; green ammonia plants TRL 7-8 (first large plants under construction).",
        ],
        "requirements": [
            "Green hydrogen supply at the scale of the synthesis loop.",
            "Air separation unit for nitrogen.",
            "Hydrogen buffering (storage or oversized electrolysis) to smooth renewable variability.",
            "Ammonia storage (refrigerated tanks) and handling to fertilizer-industry safety practice.",
        ],
        "standards": [
            "ISO 13847 / industry practice for ammonia handling and storage.",
            "Fertilizer-grade specifications (e.g. ISO 20944) adapted for fuel-grade ammonia definitions in development.",
        ],
        "citations": [CIT_IEA_NH3, CIT_IRENA_NH3, CIT_IEA_H2],
        "sig_lens": (
            "Signature re-engineering: a Signature green-ammonia train that "
            "replaces the single giant steady loop with modular medium-"
            "pressure synthesis converters that can turn down to 40 percent "
            "load, fed by a Signature hydrogen buffer sized from a full "
            "year of site wind and solar data rather than rules of thumb. "
            "The Signature pathway analysis prices the buffering three "
            "ways - steel tanks, salt caverns where geology allows, and "
            "oversized electrolysis - and picks the cheapest per site."
        ),
    },
    {
        "key": "e_methanol",
        "name": "E-Methanol from Green Hydrogen and Captured CO2",
        "group": "Hydrogen and Power-to-X",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "E-methanol is methanol synthesized from green hydrogen and "
            "captured carbon dioxide, a liquid fuel at room temperature "
            "that can serve shipping, chemicals, and gasoline blending. It "
            "is one of the most advanced power-to-X fuels: a commercial "
            "demonstration plant has run in Iceland since 2012 using "
            "geothermal CO2, and several larger e-methanol plants aimed at "
            "marine fuel are under construction. Methanol's lower heating "
            "value is 19.9 MJ/kg (15.8 MJ per litre) - roughly half of "
            "diesel by volume - and it is toxic and burns with a nearly "
            "invisible flame, which shapes handling rules. Honest framing: "
            "the chemistry is proven and first plants run, but e-methanol "
            "remains several times the price of fossil methanol, and "
            "greenhouse-gas benefit depends entirely on the CO2 source "
            "being biogenic or atmospheric rather than fossil."
        ),
        "how_it_works": (
            "Carbon dioxide (from biogas upgrading, biomass plants, or "
            "direct air capture) reacts with green hydrogen over a "
            "copper-zinc catalyst: CO2 + 3 H2 -> CH3OH + H2O at roughly "
            "200-300 C and 50-100 bar. The reaction is the same family as "
            "conventional methanol synthesis, which normally uses syngas "
            "(CO + H2); feeding CO2 directly shifts the equilibrium and "
            "produces water that must be distilled out. Because methanol is "
            "liquid at ambient conditions, storage and transport use "
            "ordinary tankage with materials compatible with methanol "
            "(it attacks some elastomers and aluminum). In engines it has a "
            "high octane number (around 109 RON) but about half the "
            "volumetric energy of gasoline, so fuel systems must deliver "
            "roughly twice the volume."
        ),
        "key_points": [
            "Reaction: CO2 + 3 H2 -> CH3OH + H2O over Cu/Zn catalyst, 200-300 C, 50-100 bar.",
            "Lower heating value 19.9 MJ/kg (15.8 MJ/L) - liquid at room temperature, easy to store.",
            "High octane (~109 RON); about half the volumetric energy of gasoline.",
            "Toxic by ingestion and burns with a near-invisible flame - handling rules differ from gasoline.",
            "Climate benefit depends on CO2 source: biogenic or atmospheric CO2 required for deep cuts.",
            "Status: TRL 7-8 - demonstration plants operating, first large marine-fuel plants under construction.",
        ],
        "requirements": [
            "Green hydrogen supply.",
            "Concentrated CO2 source (biogenic or direct air capture) with documented origin.",
            "Methanol synthesis loop and distillation for water removal.",
            "Methanol-compatible materials and toxicity-aware handling procedures.",
        ],
        "standards": [
            "IMPCA methanol reference specifications (chemical grade; fuel-grade specs evolving).",
            "Maritime handling: IGF Code interim guidelines for methyl/ethyl alcohol as fuel (MSC.1/Circ.1621).",
        ],
        "citations": [CIT_IEA_ETP, CIT_IRENA_H2, CIT_IEA_H2],
        "sig_lens": (
            "Signature re-engineering: a Signature e-methanol flowsheet "
            "that co-locates the plant with a biogas upgrader so the CO2 is "
            "already separated and biogenic, recycles the reaction water to "
            "the electrolyzer feed treatment, and runs the synthesis loop "
            "on a Signature load-following controller that tracks "
            "electrolyzer output. The Signature efficiency analysis traces "
            "every megawatt from wind turbine to methanol tank and sizes "
            "the distillation column for the actual water make, not the "
            "textbook case."
        ),
    },
    {
        "key": "ptl_ft_efuels",
        "name": "Power-to-Liquid E-Fuels via Fischer-Tropsch",
        "group": "Hydrogen and Power-to-X",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Power-to-liquid e-fuels are synthetic liquid hydrocarbons made "
            "from green hydrogen and captured CO2 via Fischer-Tropsch "
            "synthesis - drop-in e-diesel, e-kerosene, and e-gasoline that "
            "work in existing engines and aircraft with no modification. "
            "The Fischer-Tropsch reaction itself is TRL 9 (it made fuel "
            "from coal and gas for decades), but the POWER-TO-LIQUID chain "
            "- renewable hydrogen plus captured CO2 feeding it - is "
            "emerging, with demonstration plants operating and first "
            "commercial e-fuel plants under construction. Overall "
            "electricity-to-fuel efficiency is roughly 50 percent, which is "
            "why e-fuels are the most electricity-hungry fuel pathway in "
            "this database. Honest framing: the fuels are real and "
            "certifiable, but at current costs they are a premium product "
            "for aviation and other hard-to-electrify uses, not a "
            "replacement for pump fuel."
        ),
        "how_it_works": (
            "Green hydrogen and carbon monoxide (made from CO2 by reverse "
            "water-gas shift: CO2 + H2 -> CO + H2O) form syngas, which "
            "passes over cobalt or iron catalysts at 200-350 C and 10-40 "
            "bar. The Fischer-Tropsch reaction chains carbon atoms together: "
            "n CO + 2n H2 -> (CH2)n + n H2O, producing a waxy syncrude that "
            "is hydrocracked and distilled into diesel, kerosene, and "
            "naphtha fractions. Product selectivity is tuned by catalyst "
            "and conditions; aviation kerosene fractions can then be "
            "certified under ASTM D7566 Annex A1 (FT-SPK). The chain's "
            "enemies are cost: every conversion step - electrolysis, shift, "
            "synthesis, upgrading - takes its efficiency cut, and the CO2 "
            "feedstock dominates operating cost."
        ),
        "key_points": [
            "Chain: green H2 + CO2 -> syngas (reverse water-gas shift) -> Fischer-Tropsch syncrude -> hydrocracking/distillation.",
            "Products are true drop-in hydrocarbons: e-diesel, e-kerosene, e-gasoline for unmodified engines.",
            "Overall power-to-fuel efficiency roughly 50 percent - the most electricity-intensive pathway here.",
            "Aviation fraction certifiable under ASTM D7566 Annex A1 (FT-SPK), up to 50 percent blend.",
            "CO2 source and cost dominate economics; biogenic or atmospheric CO2 needed for climate benefit.",
            "Status: FT synthesis TRL 9; integrated power-to-liquid plants TRL 7-8.",
        ],
        "requirements": [
            "Green hydrogen at scale plus a concentrated CO2 source.",
            "Reverse water-gas shift reactor and Fischer-Tropsch synthesis loop.",
            "Product upgrading: hydrocracking, isomerization, distillation.",
            "Fuel certification testing for the target fraction (e.g. ASTM D7566 for jet).",
        ],
        "standards": [
            "ASTM D7566 Annex A1 - Fischer-Tropsch synthetic paraffinic kerosene.",
            "ASTM D975 / EN 590 for the diesel fraction; EN 15940 for paraffinic diesel.",
        ],
        "citations": [CIT_IEA_ETP, CIT_ASTM_D7566, CIT_IEA_SAF],
        "sig_lens": (
            "Signature re-engineering: a Signature power-to-liquid train "
            "that replaces the standalone reverse water-gas shift with a "
            "co-electrolysis front end (see the e-kerosene record), recycles "
            "FT tail gas to the shift reactor instead of flaring it, and "
            "uses a Signature product-slate optimizer that picks the "
            "diesel/kerosene/naphtha split from live market prices rather "
            "than fixed catalyst selectivity. The Signature analysis "
            "publishes the full energy balance per litre of e-kerosene so "
            "the 50-percent-chain-efficiency claim is checkable."
        ),
    },
    {
        "key": "synthetic_methane_ptg",
        "name": "Synthetic Methane by Power-to-Gas Methanation",
        "group": "Hydrogen and Power-to-X",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Synthetic methane is pipeline-grade natural gas made from "
            "green hydrogen and captured CO2 via the Sabatier reaction - a "
            "power-to-gas fuel that can be injected into the existing gas "
            "grid, stored in the vast gas storage system, and burned in any "
            "gas appliance or CNG vehicle with zero changes. Demonstration "
            "plants have injected synthetic methane into national grids "
            "since the mid-2010s. Its appeal is infrastructure: no new "
            "pipelines, no new burners, seasonal storage for free. Its "
            "penalty is thermodynamics: each conversion step sheds energy, "
            "so round-trip electricity-to-gas-to-power efficiency is poor, "
            "and the climate case stands or falls on the CO2 source. Honest "
            "framing: the technology works and the grid accepts the "
            "product, but it is an expensive way to store electricity "
            "compared with batteries for short durations."
        ),
        "how_it_works": (
            "The Sabatier reaction, CO2 + 4 H2 -> CH4 + 2 H2O, runs over a "
            "nickel catalyst at 300-400 C, releasing substantial heat that "
            "must be removed to protect the catalyst. Biological methanation "
            "is the alternative: archaea (methanogens) perform the same "
            "reaction at near-ambient conditions in a bioreactor, tolerating "
            "impurities better but reacting more slowly. The product methane "
            "(lower heating value 50 MJ/kg) is dried, odorized, and "
            "injected to the gas grid, where it is chemically "
            "indistinguishable from fossil methane - which is exactly the "
            "point, and also why certification of origin (guarantees of "
            "origin / mass balancing) is the whole climate accounting."
        ),
        "key_points": [
            "Sabatier: CO2 + 4 H2 -> CH4 + 2 H2O, nickel catalyst, 300-400 C; biological route uses methanogen archaea near ambient.",
            "Product is grid-ready methane (LHV 50 MJ/kg) - zero changes to pipelines, storage, or burners.",
            "Leverages the gas grid as enormous seasonal energy storage.",
            "Round-trip electricity-gas-power efficiency is low; best used as fuel, not as electricity storage.",
            "Climate benefit requires biogenic or atmospheric CO2 and certified guarantees of origin.",
            "Status: TRL 7-8 - grid-injecting demonstration plants operating since the mid-2010s.",
        ],
        "requirements": [
            "Green hydrogen supply and concentrated CO2.",
            "Methanation reactor (catalytic) or bioreactor (biological) with heat management.",
            "Gas drying, quality monitoring, and odorization for grid injection.",
            "Guarantee-of-origin certification and grid-injection agreement.",
        ],
        "standards": [
            "EN 16723 / national gas-quality standards for grid injection.",
            "ISO 15403 - natural gas for use as compressed fuel for vehicles (for the mobility route).",
        ],
        "citations": [CIT_IEA_ETP, CIT_IEA_H2, CIT_ISO_15403],
        "sig_lens": (
            "Signature re-engineering: a Signature methanation module that "
            "captures the Sabatier reaction heat into a district heating "
            "loop instead of rejecting it, turning the exotherm from a "
            "cooling cost into a revenue stream. The Signature design pairs "
            "a catalytic first stage with a biological polishing stage that "
            "eats the last unconverted hydrogen, and the Signature "
            "accounting model tracks each megawatt-hour of methane back to "
            "its wind turbine and CO2 source for audit-ready origin proof."
        ),
    },
    {
        "key": "saf_hefa",
        "name": "Sustainable Aviation Fuel via HEFA",
        "group": "Sustainable Aviation Fuel Pathways",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "description": (
            "HEFA - hydroprocessed esters and fatty acids - is the "
            "commercial workhorse of sustainable aviation fuel: waste fats, "
            "oils, and greases (used cooking oil, animal tallow) are "
            "hydrotreated into paraffinic kerosene certified under ASTM "
            "D7566 Annex A2 for blends up to 50 percent with conventional "
            "jet fuel. It is the only SAF pathway at full commercial scale "
            "today, with multi-hundred-thousand-tonne plants operating on "
            "three continents, and typical life-cycle greenhouse-gas "
            "reductions around 80 percent versus fossil jet when made from "
            "genuine wastes. Honest framing: HEFA is deployed, not "
            "experimental - but its feedstock pool is finite, fraud in used-"
            "cooking-oil supply chains is a documented problem, and HEFA "
            "alone cannot supply aviation's fuel demand, which is why the "
            "other SAF pathways in this database exist."
        ),
        "how_it_works": (
            "Triglyceride feedstocks are deoxygenated with hydrogen over a "
            "catalyst (hydrodeoxygenation), saturating the chains into "
            "n-paraffins; the straight chains are then isomerized "
            "(hydroisomerization) to branched paraffins so the fuel meets "
            "jet fuel freeze-point requirements (minus 47 C for Jet A-1). "
            "Fractionation cuts the kerosene range. The product, HEFA-SPK, "
            "is chemically a clean paraffinic kerosene - no sulfur, no "
            "aromatics - which is why the 50 percent blend cap exists: "
            "engines and seals were qualified with aromatic-containing "
            "fuel, and 100 percent paraffinic fuel needs separate "
            "certification (test programs are underway). Life-cycle "
            "analysis under ICAO CORSIA assigns HEFA from used cooking oil "
            "roughly 13-20 gCO2e/MJ versus about 89 for fossil jet."
        ),
        "key_points": [
            "Feedstocks: used cooking oil, animal fats, tall oil - genuine wastes give the best GHG numbers.",
            "Process: hydrodeoxygenation then hydroisomerization; product is HEFA-SPK paraffinic kerosene.",
            "Certified under ASTM D7566 Annex A2, up to 50 percent blend with conventional jet.",
            "Typical life-cycle GHG reduction ~80 percent versus fossil jet (CORSIA values).",
            "Feedstock pool is finite; documented fraud in waste-oil supply chains requires chain-of-custody auditing.",
            "Status: TRL 9 - the only fully commercial SAF pathway, operating at scale.",
        ],
        "requirements": [
            "Certified waste-oil/fat feedstock with chain-of-custody documentation.",
            "Hydrotreating complex with hydrogen supply and isomerization unit.",
            "ASTM D7566 Annex A2 qualification testing of the product.",
            "CORSIA-eligible sustainability certification (e.g. ISCC, RSB).",
        ],
        "standards": [
            "ASTM D7566 Annex A2 - HEFA synthetic paraffinic kerosene.",
            "ASTM D1655 - aviation turbine fuel (the blend it joins).",
            "ICAO CORSIA sustainability criteria and life-cycle values.",
        ],
        "citations": [CIT_ASTM_D7566, CIT_IEA_SAF, CIT_CORSIA, CIT_DOE_SAF],
        "sig_lens": (
            "Signature re-engineering: a Signature HEFA plant design that "
            "integrates feedstock forensics - a Signature lab protocol that "
            "fingerprints each waste-oil batch by fatty-acid profile and "
            "contaminant markers to catch virgin-oil fraud before it enters "
            "the reactor. The Signature pathway analysis models the true "
            "collectable waste-oil pool per region so the plant is sized to "
            "real feedstock, and the Signature isomerization study tunes "
            "branching for freeze point with minimum hydrogen consumption."
        ),
    },
    {
        "key": "saf_atj",
        "name": "Sustainable Aviation Fuel via Alcohol-to-Jet",
        "group": "Sustainable Aviation Fuel Pathways",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "description": (
            "Alcohol-to-jet converts ethanol (or isobutanol) into jet-range "
            "hydrocarbons: dehydration to ethylene, oligomerization to "
            "longer olefins, then hydrogenation to paraffins - certified "
            "under ASTM D7566 Annex A5 for blends up to 50 percent. Its "
            "strategic value is feedstock flexibility: the alcohol can come "
            "from sugar fermentation, cellulosic ethanol, or even steel-mill "
            "off-gas fermentation, linking the huge global ethanol industry "
            "to aviation. First commercial-scale plants began operating in "
            "the mid-2020s. Honest framing: the chemistry chain is proven, "
            "but the economics hinge on cheap low-carbon ethanol, and "
            "several announced plants have slipped schedules - alcohol-to-"
            "jet is first-commercial, not yet routine."
        ),
        "how_it_works": (
            "Ethanol is dehydrated over an acid catalyst to ethylene "
            "(CH3CH2OH -> C2H4 + H2O), the ethylene is oligomerized over "
            "nickel or zeolite catalysts into C8-C16 olefins, and the "
            "olefins are hydrogenated to paraffins and distilled to the jet "
            "cut. Each step is a known refinery operation; the art is "
            "selectivity - maximizing the jet fraction while minimizing "
            "light gases and heavy wax. The carbon intensity of the jet "
            "fuel is dominated by the ethanol's origin: corn ethanol gives "
            "modest savings, cellulosic or waste-gas ethanol gives deep "
            "savings, and the CORSIA life-cycle value follows the alcohol, "
            "not the jet plant."
        ),
        "key_points": [
            "Chain: ethanol -> ethylene (dehydration) -> C8-C16 olefins (oligomerization) -> paraffins (hydrogenation).",
            "Certified under ASTM D7566 Annex A5, up to 50 percent blend.",
            "Feedstock-flexible: sugar, cellulosic, or waste-gas-fermented ethanol all qualify.",
            "Climate benefit follows the ethanol source - the jet plant cannot fix a dirty alcohol.",
            "Byproduct light gases can fuel the plant; heavy cut can go to diesel or be recycled.",
            "Status: TRL 7-8 - first commercial-scale plants operating, several more announced.",
        ],
        "requirements": [
            "Low-carbon ethanol supply with documented life-cycle value.",
            "Dehydration, oligomerization, hydrogenation, and fractionation units.",
            "Hydrogen supply for the final hydrogenation step.",
            "ASTM D7566 Annex A5 qualification and CORSIA sustainability certification.",
        ],
        "standards": [
            "ASTM D7566 Annex A5 - alcohol-to-jet synthetic paraffinic kerosene.",
            "ASTM D4806 - denatured fuel ethanol (feedstock quality reference).",
        ],
        "citations": [CIT_ASTM_D7566, CIT_IEA_SAF, CIT_DOE_SAF, CIT_DOE_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature alcohol-to-jet design "
            "that feeds the oligomerization reactor with ethanol made on "
            "site from steel-mill off-gas fermentation, closing the loop "
            "between heavy industry and aviation in one facility. The "
            "Signature selectivity study maps catalyst choice against the "
            "jet-fraction yield curve, and the Signature carbon model "
            "computes the fuel's CORSIA value from measured inputs rather "
            "than default factors."
        ),
    },
    {
        "key": "saf_ft_spk",
        "name": "Sustainable Aviation Fuel via Fischer-Tropsch (FT-SPK)",
        "group": "Sustainable Aviation Fuel Pathways",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "description": (
            "FT-SPK is jet fuel made by Fischer-Tropsch synthesis from "
            "syngas derived from biomass gasification or from green "
            "hydrogen plus captured CO2 - certified under ASTM D7566 Annex "
            "A1 for blends up to 50 percent. It is the most feedstock-"
            "flexible SAF route in principle: municipal waste, forestry "
            "residues, or power-to-liquid inputs all become the same "
            "paraffinic kerosene. In practice it is also the hardest SAF "
            "route to finance: gasification at aviation-fuel quality is "
            "demanding, and the highest-profile waste-to-jet projects have "
            "missed targets or failed financially - honest framing matters "
            "here. FT-SPK is certified and real, but as of the mid-2020s it "
            "remains a demonstration-to-first-commercial pathway, not a "
            "volume supplier."
        ),
        "how_it_works": (
            "Biomass or waste is gasified to syngas (CO + H2), the syngas is "
            "cleaned to parts-per-billion contaminant levels (sulfur, tars, "
            "particulates poison FT catalysts), then Fischer-Tropsch "
            "synthesis builds hydrocarbon chains that are hydrocracked to "
            "the jet cut. The power-to-liquid variant skips gasification: "
            "green hydrogen plus CO2 become syngas via reverse water-gas "
            "shift (see the e-fuels record). Gas cleanup is the make-or-"
            "break unit - a gasifier produces a dirty, tarry syngas and the "
            "FT catalyst demands a clean one. Product properties mirror "
            "HEFA-SPK: clean paraffinic kerosene, same 50 percent blend "
            "limit for the same aromatics reasons."
        ),
        "key_points": [
            "Routes: biomass/waste gasification to syngas, or power-to-liquid (green H2 + CO2).",
            "Certified under ASTM D7566 Annex A1, up to 50 percent blend.",
            "Syngas cleanup to ppb contaminant levels is the critical, expensive step.",
            "Most feedstock-flexible SAF route in principle; hardest to finance in practice.",
            "Several flagship projects missed targets - maturity framing must stay honest.",
            "Status: TRL 7 - certified fuel, demonstration plants, not yet a volume supplier.",
        ],
        "requirements": [
            "Gasifier (or PtL front end) plus deep syngas cleanup train.",
            "Fischer-Tropsch synthesis with cobalt or iron catalyst.",
            "Hydrocracking and fractionation to the jet cut.",
            "ASTM D7566 Annex A1 qualification; feedstock sustainability certification.",
        ],
        "standards": [
            "ASTM D7566 Annex A1 - Fischer-Tropsch synthetic paraffinic kerosene.",
            "Gasifier syngas quality targets per catalyst vendor specifications.",
        ],
        "citations": [CIT_ASTM_D7566, CIT_IEA_SAF, CIT_IEA_ETP],
        "sig_lens": (
            "Signature re-engineering: a Signature FT-SPK plant that pairs "
            "a small modular gasifier array (instead of one giant gasifier) "
            "with a shared deep-cleanup train, so a single gasifier can be "
            "serviced without stopping fuel production. The Signature "
            "cleanup study ranks contaminants by catalyst-poisoning cost and "
            "spends the cleanup budget where poisoning is most expensive, "
            "and the Signature finance model stress-tests the plant against "
            "the actual failure modes of the flagship projects."
        ),
    },
    {
        "key": "renewable_diesel_hvo",
        "name": "Renewable Diesel (HVO)",
        "group": "Renewable Diesel and Drop-In Biofuels",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "description": (
            "HVO - hydrotreated vegetable oil, also called renewable diesel "
            "or green diesel - is a drop-in diesel made by hydrotreating "
            "fats, oils, and greases. Unlike biodiesel (FAME), which is a "
            "blend-limited ester, HVO is a pure paraffinic hydrocarbon that "
            "meets diesel specifications outright and can be used at 100 "
            "percent in unmodified diesel engines. It is fully commercial "
            "(TRL 9): multi-million-tonne plants operate worldwide, and "
            "life-cycle greenhouse-gas reductions of 70-90 percent are "
            "documented for waste feedstocks. Honest framing: the fuel is "
            "mature, but it is still the emerging REPLACEMENT for fossil "
            "diesel - it supplies single-digit percentages of diesel "
            "demand, and its growth is feedstock-limited exactly like "
            "HEFA's, since both compete for the same waste oils."
        ),
        "how_it_works": (
            "The chemistry mirrors HEFA-SPK but targets the diesel cut: "
            "triglycerides are hydrodeoxygenated to n-paraffins, then "
            "mildly isomerized for cold-flow performance and distilled to "
            "the diesel boiling range. The product has a cetane number "
            "typically 70-90 (versus ~50 for fossil diesel), zero sulfur, "
            "zero aromatics, and excellent storage stability - it is "
            "chemically a premium diesel, which is why engines need no "
            "modification and no blend wall applies. It is specified under "
            "EN 15940 for paraffinic diesel and accepted under ASTM D975. "
            "The same plant hardware that makes HVO can swing to HEFA-SPK "
            "jet production, which is why renewable-diesel and SAF capacity "
            "planning are one conversation."
        ),
        "key_points": [
            "Pure paraffinic hydrocarbon - 100 percent drop-in, no blend wall, no engine changes.",
            "Cetane typically 70-90; zero sulfur, zero aromatics; outstanding storage stability.",
            "Specified under EN 15940 (paraffinic diesel) and accepted under ASTM D975.",
            "Life-cycle GHG cuts of 70-90 percent documented for waste feedstocks.",
            "Same hardware can swing between renewable diesel and HEFA jet - capacity is fungible.",
            "Status: TRL 9 commercial; emerging as a diesel replacement (single-digit share of demand).",
        ],
        "requirements": [
            "Waste oil/fat feedstock with chain-of-custody certification.",
            "Hydrotreating unit with hydrogen supply and isomerization.",
            "Cold-flow additive strategy for winter grades where needed.",
            "Sustainability certification (ISCC, RSB) for regulated markets.",
        ],
        "standards": [
            "EN 15940:2023 - paraffinic diesel fuel requirements.",
            "ASTM D975 - diesel fuel specification (HVO accepted).",
        ],
        "citations": [CIT_EN15940, CIT_ASTM_D975, CIT_IEA_BIO, CIT_IRENA_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature renewable-diesel plant "
            "with a swing-distillation column that shifts the product slate "
            "between diesel and jet cuts on a Signature price signal, so "
            "the plant always makes the higher-value certified fuel. The "
            "Signature cold-flow study maps isomerization severity against "
            "winter operability grades, and the Signature feedstock model "
            "contracts waste oils by measured fatty-acid profile rather "
            "than by volume alone."
        ),
    },
    {
        "key": "cellulosic_ethanol",
        "name": "Advanced Cellulosic Ethanol",
        "group": "Renewable Diesel and Drop-In Biofuels",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "description": (
            "Cellulosic ethanol is ethanol fermented from the sugars locked "
            "in lignocellulosic biomass - corn stover, wheat straw, "
            "forestry residues, energy grasses - instead of from food crops. "
            "It promises ethanol without the food-versus-fuel conflict and "
            "with life-cycle greenhouse-gas cuts of 60-90 percent. The "
            "honest history must be told straight: the 2010s wave of first "
            "commercial plants mostly failed - flagship facilities were "
            "sold, idled, or converted after struggling with feedstock "
            "logistics, pretreatment costs, and enzyme economics. The "
            "technology is therefore best described as demonstrated but not "
            "yet commercially proven: TRL 7-8, with a second wave of "
            "projects applying the hard lessons. It stays in the emerging "
            "database precisely because the prize - fuel from agricultural "
            "waste at scale - is real and the chemistry works."
        ),
        "how_it_works": (
            "Lignocellulose is pretreated (steam explosion, dilute acid, or "
            "ammonia fiber expansion) to open the fiber structure, enzymes "
            "(cellulases) hydrolyze cellulose and hemicellulose to sugars, "
            "and yeast or bacteria ferment the sugars to ethanol, which is "
            "distilled. The lignin residue - about a third of the biomass - "
            "cannot be fermented and is burned for process heat and power, "
            "which is central to the good carbon balance. The difficulty "
            "stack is physical before it is chemical: collecting, storing "
            "without rot, and feeding thousands of tonnes per day of bulky "
            "straw or stover to a continuous plant. Enzyme cost, once the "
            "headline barrier, fell substantially; feedstock logistics and "
            "pretreatment capital are the remaining dragons."
        ),
        "key_points": [
            "Feedstocks: corn stover, wheat straw, forestry residues, energy grasses - no food crops.",
            "Chain: pretreatment -> enzymatic hydrolysis -> fermentation -> distillation; lignin fuels the plant.",
            "Life-cycle GHG cuts of 60-90 percent versus gasoline when the chain is well run.",
            "The 2010s first-commercial wave mostly failed on logistics and capital cost - honest TRL 7-8.",
            "Enzyme costs fell; feedstock collection/storage and pretreatment remain the barriers.",
            "Product meets ASTM D4806 fuel ethanol specs; can feed alcohol-to-jet for SAF.",
        ],
        "requirements": [
            "Contracted agricultural-residue supply with storage that prevents spoilage.",
            "Pretreatment, hydrolysis, fermentation, and distillation train.",
            "Lignin-fired combined heat and power for the energy balance.",
            "Fuel ethanol quality testing to ASTM D4806.",
        ],
        "standards": [
            "ASTM D4806 - denatured fuel ethanol for blending.",
            "EN 15376 - automotive fuel ethanol specifications (European market).",
        ],
        "citations": [CIT_DOE_BIO, CIT_NREL, CIT_IRENA_BIO, CIT_IEA_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature cellulosic plant that "
            "attacks the true failure point - feedstock logistics - with "
            "satellite depots that densify stover into pellets within "
            "haul distance of the fields, feeding the central plant a "
            "uniform, storable feed. The Signature pretreatment study "
            "selects the method by measured inhibitor formation per tonne "
            "of local stover, and the Signature finance model carries the "
            "full 2010s failure-mode list as explicit risk line items."
        ),
    },
    {
        "key": "biomethane_rng",
        "name": "Biomethane / Renewable Natural Gas",
        "group": "Biogas and Waste Pathways",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "description": (
            "Biomethane - renewable natural gas, RNG - is biogas upgraded "
            "to pipeline-quality methane (typically over 96 percent CH4). "
            "It is chemically interchangeable with fossil natural gas, so it "
            "flows through the same pipelines, fuels the same CNG/LNG "
            "trucks, and heats the same buildings, while its life-cycle "
            "greenhouse-gas profile can be strongly negative when it "
            "captures methane that would otherwise escape from manure or "
            "landfills. Upgrading is TRL 9 and fully commercial, with "
            "thousands of plants injecting to grids worldwide. It counts as "
            "emerging here because its ROLE is still expanding: from a "
            "niche green-gas product toward a structural decarbonization "
            "fuel for heavy transport and industry, with production still a "
            "small fraction of gas demand."
        ),
        "how_it_works": (
            "Anaerobic digesters (or landfill wells) produce raw biogas - "
            "roughly 55-65 percent methane, the rest mostly CO2 with traces "
            "of H2S, siloxanes, and water. Upgrading strips the CO2: "
            "pressure-swing adsorption, membrane separation, amine "
            "scrubbing, or water scrubbing, each with different methane "
            "slip (lost methane) and energy use - slip matters enormously "
            "because methane is a potent greenhouse gas and leaks destroy "
            "the climate case. The biomethane is dried, odorized, "
            "quality-checked to grid code, and injected; the separated CO2 "
            "stream is increasingly captured for use (greenhouses, "
            "e-fuels) rather than vented. Manure-based biomethane routinely "
            "scores negative carbon intensity because it avoids open-lagoon "
            "methane emissions."
        ),
        "key_points": [
            "Raw biogas (~60 percent CH4) upgraded to >96 percent methane - pipeline-interchangeable.",
            "Upgrading routes: PSA, membranes, amine or water scrubbing; methane slip is the key performance metric.",
            "Manure and landfill routes can score negative life-cycle carbon intensity (avoided methane).",
            "Separated CO2 can be captured for e-fuel synthesis instead of vented.",
            "End uses: grid injection, CNG/LNG trucking, industry - zero equipment changes.",
            "Status: TRL 9 commercial; emerging in role - still a small share of gas supply.",
        ],
        "requirements": [
            "Biogas source: digesters (manure, food waste, sewage) or landfill gas collection.",
            "Upgrading unit with measured methane-slip control.",
            "Gas quality monitoring, odorization, and grid-injection agreement.",
            "Digestate management plan (the nutrient loop must close).",
        ],
        "standards": [
            "EN 16723 - gas quality for grid injection and vehicle use.",
            "ISO 15403 - natural gas as compressed vehicle fuel.",
        ],
        "citations": [CIT_IEA_BIO, CIT_ISO_15403, CIT_DOE_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature biomethane plant where "
            "the upgrader's separated CO2 feeds a co-located methanation or "
            "e-methanol unit, so no carbon leaves the site except as fuel. "
            "The Signature slip-control protocol measures methane at every "
            "flange with a standing leak budget, and the Signature "
            "digestate plan returns nutrients to the farms that supplied "
            "the manure, closing the loop the carbon accounting assumes."
        ),
    },
    {
        "key": "bio_lng",
        "name": "Bio-LNG (Liquefied Biomethane)",
        "group": "Biogas and Waste Pathways",
        "ladder_rank": 12,
        "ladder_tier": "foundations",
        "description": (
            "Bio-LNG is biomethane liquefied at minus 162 C into a cryogenic "
            "liquid fuel for long-haul trucking and shipping - the "
            "renewable twin of fossil LNG. Liquefaction shrinks methane to "
            "1/600th of its gas volume, giving trucks a practical 1,000-plus-"
            "kilometre range on a fuel whose life-cycle emissions can be "
            "70-100 percent below diesel when made from manure or organic "
            "waste. Small-scale liquefaction is TRL 8-9: plants operate in "
            "Europe and North America feeding growing bio-LNG truck fleets. "
            "Honest framing: the fuel is proven and trucks are on the road, "
            "but bio-LNG is still a small premium market - liquefaction "
            "adds cost and energy, and supply depends on the biomethane "
            "pool, which is itself still scaling."
        ),
        "how_it_works": (
            "Biomethane (see the previous record) is further purified - "
            "CO2 must be removed to trace levels or it freezes solid in the "
            "cryogenic exchanger - then liquefied in a small-scale plant "
            "(nitrogen-expansion or mixed-refrigerant cycles are common at "
            "this scale) and stored in vacuum-insulated cryogenic tanks. "
            "The liquid (lower heating value about 50 MJ/kg, density ~450 "
            "kg per cubic metre) is dispensed to trucks with cryogenic "
            "tanks feeding high-pressure direct-injection gas engines. "
            "Boil-off gas management matters: tanks vent as they warm, so "
            "stations and trucks recapture or use the vapor rather than "
            "releasing methane. Energy penalty of liquefaction is roughly "
            "10 percent of the fuel's energy content."
        ),
        "key_points": [
            "Biomethane liquefied at -162 C; 1/600th the volume of gas - practical long-haul range.",
            "Lower heating value ~50 MJ/kg; density ~450 kg/m3 as liquid.",
            "CO2 must be removed to trace levels before liquefaction (freeze-out risk).",
            "Boil-off management is essential - vented methane destroys the climate benefit.",
            "Life-cycle cuts of 70-100 percent versus diesel for manure/waste feedstocks.",
            "Status: TRL 8-9 - plants operating, truck fleets running; still a premium niche market.",
        ],
        "requirements": [
            "Biomethane supply with deep CO2 removal.",
            "Small-scale liquefaction plant and cryogenic storage.",
            "Cryogenic dispensing stations and LNG-capable trucks.",
            "Boil-off capture or utilization at every storage point.",
        ],
        "standards": [
            "ISO 16924 - LNG fueling stations; ISO 16923 - CNG stations (adjacent practice).",
            "EN 16723 gas quality; ADR regulations for cryogenic road transport.",
        ],
        "citations": [CIT_IEA_BIO, CIT_ISO_15403, CIT_IEA_ETP],
        "sig_lens": (
            "Signature re-engineering: a Signature bio-LNG chain that "
            "co-locates liquefaction with the biomethane upgrader to avoid "
            "a transport leg, recovers liquefaction cold for the upgrader's "
            "CO2 separation, and instruments every tank with a Signature "
            "boil-off ledger so venting events are counted, priced, and "
            "engineered out. The Signature station design recaptures truck-"
            "tank vapor during fueling instead of releasing it."
        ),
    },
    {
        "key": "algae_phototrophic",
        "name": "Algae Phototrophic Biofuels",
        "group": "Algae and Advanced Biomass",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "description": (
            "Microalgae grown photosynthetically can accumulate 20-50 "
            "percent of their dry weight as oils, yielding far more fuel "
            "per hectare than any land crop in principle - the theoretical "
            "case that has attracted decades of research and billions in "
            "investment. The honest record: after the 2008-2012 boom, "
            "nearly every venture-scale algae fuel company pivoted to "
            "nutraceuticals, specialty oils, or shut down, because "
            "harvesting microscopic cells from dilute ponds and drying them "
            "costs more energy and money than the oil is worth. Current "
            "status is TRL 4-6: the biology works, pilot ponds and "
            "photobioreactors run, but no one has demonstrated sustained "
            "fuel-only production at competitive cost. Algae stays in this "
            "database as the highest-potential, hardest-to-crack biomass "
            "pathway."
        ),
        "how_it_works": (
            "Selected strains (Chlorella, Nannochloropsis, Scenedesmus and "
            "others) grow in open raceway ponds or closed photobioreactors, "
            "fed with CO2, nutrients, and sunlight; nitrogen starvation "
            "triggers lipid accumulation. Harvesting - the economic crux - "
            "uses flocculation, dissolved-air flotation, or centrifugation "
            "to concentrate cells from grams-per-litre broth, then drying "
            "and lipid extraction (hexane or supercritical CO2), with the "
            "oil hydrotreated to renewable diesel or jet. The residual "
            "biomass can be digested to biogas. Energy balance analyses "
            "consistently show that drying and harvesting dominate costs; "
            "the credible routes minimize both - wet extraction, "
            "hydrothermal liquefaction of whole wet algae, or high-value "
            "co-products carrying the economics."
        ),
        "key_points": [
            "Lipid content 20-50 percent of dry weight; theoretical yields dwarf land crops.",
            "Grows on non-arable land with saline or wastewater - no farmland competition in principle.",
            "Harvesting and drying dilute cultures is the economic crux - the historic failure point.",
            "Credible routes: wet extraction, HTL of whole algae, or co-products subsidizing fuel.",
            "The 2008-2012 venture wave mostly pivoted away from fuel - costs beat the biology.",
            "Status: TRL 4-6 - pilots run; no sustained competitive fuel-only production demonstrated.",
        ],
        "requirements": [
            "Selected high-lipid strain and contamination management strategy.",
            "CO2 supply, water rights, and nutrient sourcing (wastewater integration helps).",
            "Low-energy harvesting and wet-processing route - drying must be minimized.",
            "Honest techno-economic model with harvesting energy fully counted.",
        ],
        "standards": [
            "Product standards follow the fuel made: EN 15940 / ASTM D975 for renewable diesel; ASTM D7566 for jet.",
            "No standalone algae-fuel standard; sustainability certification (ISCC, RSB) expected.",
        ],
        "citations": [CIT_DOE_BIO, CIT_NREL, CIT_IRENA_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature algae concept that "
            "abandons drying entirely - wet algal slurry goes straight to "
            "hydrothermal liquefaction, and the aqueous byproduct recycles "
            "nutrients to the ponds. The Signature strain-selection protocol "
            "screens for harvestability (self-flocculating strains) before "
            "lipid content, because the historical record shows harvesting "
            "kills projects, not biology. The Signature energy ledger "
            "counts every kilowatt of paddlewheel and pump against the oil."
        ),
    },
    {
        "key": "macroalgae_seaweed",
        "name": "Macroalgae (Seaweed) Biofuels",
        "group": "Algae and Advanced Biomass",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "description": (
            "Seaweed - macroalgae like kelp and sargassum - is the ocean's "
            "answer to energy crops: it needs no land, no freshwater, and no "
            "fertilizer, growing up to half a metre per day in suitable "
            "waters. As a fuel feedstock it is converted by anaerobic "
            "digestion to biomethane, fermentation to ethanol or butanol, or "
            "hydrothermal liquefaction to bio-crude. Status is early: TRL "
            "3-5. Ocean farming at fuel scale is unproven, nearshore space "
            "competes with other uses, and seaweed's high water and ash "
            "content (salts) complicate conversion. Honest framing: an "
            "abundant, elegant feedstock whose supply chain - seeding, ocean "
            "farming, harvest, transport of wet biomass - has never been "
            "built at fuel scale."
        ),
        "how_it_works": (
            "Kelp is farmed on longlines seeded in hatcheries, harvested "
            "mechanically, and processed wet: anaerobic digestion handles "
            "the high moisture naturally, producing biogas; alternatively "
            "the carbohydrates (alginate, laminarin, mannitol) are "
            "hydrolyzed and fermented. Salt is the process enemy - it "
            "inhibits fermentation and corrodes equipment, so washing or "
            "salt-tolerant conversion is required. Hydrothermal "
            "liquefaction sidesteps drying by processing wet seaweed "
            "directly into bio-crude. Yields per hectare of ocean can "
            "theoretically exceed land crops several-fold, but the numbers "
            "that matter - cost per tonne of harvested, delivered, "
            "dewatered-equivalent biomass - remain research-grade."
        ),
        "key_points": [
            "No land, freshwater, or fertilizer needed; very fast growth rates in suitable waters.",
            "Conversion routes: anaerobic digestion, fermentation, or hydrothermal liquefaction (wet-friendly).",
            "Salt content inhibits fermentation and corrodes equipment - washing or tolerance required.",
            "Ocean farming, harvest, and wet-biomass transport at fuel scale are unproven.",
            "Nearshore space competes with fisheries, conservation, and other ocean uses.",
            "Status: TRL 3-5 - research and pilot farming; no fuel-scale supply chain exists.",
        ],
        "requirements": [
            "Suitable coastal waters with permits and hatchery seed supply.",
            "Harvest and wet-transport logistics designed before the conversion plant.",
            "Salt-management strategy in the conversion process.",
            "Marine environmental assessment for farm scale-up.",
        ],
        "standards": [
            "Product standards follow the fuel made (biomethane, ethanol, bio-crude upgrading).",
            "Marine aquaculture permitting per national regulations.",
        ],
        "citations": [CIT_DOE_BIO, CIT_IRENA_BIO, CIT_NREL],
        "sig_lens": (
            "Signature re-engineering: a Signature seaweed-fuel concept "
            "that processes kelp at the dock - mobile HTL barges convert "
            "wet harvest to bio-crude at the farm, so only dense crude "
            "travels ashore instead of 90-percent-water kelp. The Signature "
            "farm design uses the nutrient plume under fish farms (integrated "
            "multi-trophic aquaculture) to fertilize the kelp for free, and "
            "the Signature salt loop recovers salts as a co-product."
        ),
    },
    {
        "key": "fast_pyrolysis_biooil",
        "name": "Fast Pyrolysis Bio-Oils",
        "group": "Thermochemical Bio-Oils",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "description": (
            "Fast pyrolysis heats dry biomass to about 500 C in the absence "
            "of oxygen for a couple of seconds, condensing the vapors into "
            "a dark liquid - bio-oil - at yields up to 75 percent by weight "
            "of the feed. It is the fastest way to turn solid biomass into "
            "a pumpable liquid, and commercial plants sell bio-oil for heat "
            "and as a refinery feed. But raw bio-oil is a difficult fuel: "
            "acidic (pH ~2-3), oxygen-rich (35-40 percent oxygen), viscous, "
            "thermally unstable, and immiscible with hydrocarbons. Honest "
            "framing: pyrolysis the PROCESS is commercial (TRL 8-9 for "
            "bio-oil production); pyrolysis oil as a TRANSPORTATION fuel is "
            "emerging (TRL 6-7), because upgrading it to stable drop-in "
            "fuel is where the cost and difficulty live."
        ),
        "how_it_works": (
            "Dried, ground biomass (<10 percent moisture, millimetre-scale "
            "particles) enters a fluidized-bed or ablative reactor at ~500 "
            "C with vapor residence time under 2 seconds; rapid quenching "
            "condenses a two-phase liquid. The oil's oxygen - in acids, "
            "aldehydes, phenols, and water (15-30 percent water) - is what "
            "makes it unstable and low-energy (lower heating value 16-19 "
            "MJ/kg versus 43 for diesel). Upgrading means hydrodeoxygenation: "
            "reacting the oil with hydrogen at high pressure to strip "
            "oxygen as water, a hydrogen-hungry step that dominates cost. "
            "Milder uses - boiler fuel, or co-processing up to a few "
            "percent in refineries - are closer to market than full "
            "hydrotreating to diesel."
        ),
        "key_points": [
            "Fast pyrolysis: ~500 C, <2 s vapor residence, up to 75 wt percent liquid yield.",
            "Raw bio-oil: acidic, 35-40 percent oxygen, unstable, LHV 16-19 MJ/kg - not an engine fuel as-is.",
            "Upgrading by hydrodeoxygenation strips oxygen as water but consumes large hydrogen quantities.",
            "Nearer-term outlets: boiler fuel, refinery co-processing at low blend rates.",
            "Biochar co-product can sequester carbon or serve as soil amendment.",
            "Status: pyrolysis TRL 8-9; transport-fuel upgrading TRL 6-7.",
        ],
        "requirements": [
            "Dry (<10 percent moisture), uniformly sized biomass feed.",
            "Fast-pyrolysis reactor with rapid vapor quench.",
            "Upgrading route selected: hydrotreating, co-processing, or direct-use markets.",
            "Hydrogen supply if full hydrodeoxygenation is chosen.",
        ],
        "standards": [
            "ASTM D7544 - pyrolysis liquid biofuel specifications (burner fuel grades).",
            "Upgraded products must meet ASTM D975 / EN 590 diesel or EN 15940 paraffinic diesel.",
        ],
        "citations": [CIT_DOE_BIO, CIT_NREL, CIT_IEA_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature pyrolysis design that "
            "stages condensation - collecting the watery light fraction "
            "separately from the energy-dense heavy fraction - so only the "
            "heavy fraction goes to expensive hydrotreating while the light "
            "acids feed a Signature fermentation to recoverable chemicals. "
            "The Signature hydrogen analysis sizes hydrotreating from the "
            "measured oxygen content of each feedstock, and the Signature "
            "biochar plan banks the carbon as a documented sequestration "
            "credit."
        ),
    },
    {
        "key": "catalytic_hydropyrolysis",
        "name": "Hydrotreated and Catalytic Pyrolysis Oils",
        "group": "Thermochemical Bio-Oils",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "description": (
            "Catalytic hydropyrolysis runs pyrolysis in hydrogen with a "
            "catalyst present, deoxygenating the vapors as they form - "
            "producing a far more stable, less oxygenated oil than "
            "conventional fast pyrolysis. Variants include catalytic fast "
            "pyrolysis (zeolite catalysts upgrading vapors before "
            "condensation) and hydropyrolysis plus vapor-phase upgrading. "
            "The prize is a bio-oil that needs far less downstream "
            "hydrotreating, or even none, to become refinery-ready. Status "
            "is firmly emerging: TRL 5-6, with pilot plants demonstrating "
            "the chemistry and long-duration runs still needed to prove "
            "catalyst life against biomass ash, alkali metals, and coking. "
            "Honest framing: the concept elegantly attacks bio-oil's core "
            "weakness, but catalyst deactivation by real biomass "
            "contaminants is the known killer of elegant pyrolysis "
            "concepts."
        ),
        "how_it_works": (
            "In hydropyrolysis, biomass devolatilizes in a hydrogen "
            "atmosphere (typically 350-500 C, 10-30 bar H2) over catalysts "
            "that hydrogenate reactive oxygenates in the vapor phase before "
            "they can polymerize into coke or acids. Catalytic fast "
            "pyrolysis instead passes conventional pyrolysis vapors over "
            "zeolites (e.g. HZSM-5) at near-atmospheric pressure, cracking "
            "and aromatizing the vapors into a more hydrocarbon-like oil "
            "with significant coke make on the catalyst. Both routes trade "
            "liquid yield for quality: oxygen content can fall from ~40 "
            "percent to under 10 percent, at the cost of 10-20 points of "
            "yield and continuous catalyst regeneration. The product still "
            "needs finishing hydrotreatment for transport fuel, but a much "
            "lighter one."
        ),
        "key_points": [
            "Deoxygenation happens in the vapor phase, before condensation - attacking instability at its source.",
            "Oxygen can drop from ~40 percent to under 10 percent; yield falls 10-20 points in exchange.",
            "Catalyst deactivation by alkali, ash, and coking is the central technical risk.",
            "Product needs lighter finishing hydrotreatment than raw bio-oil.",
            "Hydrogen consumption is significant - pairs naturally with low-cost green hydrogen.",
            "Status: TRL 5-6 - pilot demonstrations; long-duration catalyst-life data still needed.",
        ],
        "requirements": [
            "Hydrogen supply at pressure for hydropyrolysis variants.",
            "Catalyst inventory and continuous regeneration system.",
            "Feedstock specification limiting alkali and ash (catalyst poisons).",
            "Finishing hydrotreater sized for the partially-upgraded oil.",
        ],
        "standards": [
            "Upgraded products to ASTM D975 / EN 15940 as applicable.",
            "ASTM D7544 for intermediate pyrolysis liquid grades.",
        ],
        "citations": [CIT_DOE_BIO, CIT_NREL, CIT_IRENA_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature hydropyrolysis design "
            "with a guard-bed stage that captures alkali metals before they "
            "reach the precious main catalyst, extending catalyst life by "
            "design rather than by hope. The Signature operating protocol "
            "schedules regeneration from measured coke-make rates per "
            "feedstock, and the Signature yield-quality optimizer picks the "
            "deoxygenation depth where the marginal hydrogen cost equals "
            "the marginal upgrading saving."
        ),
    },
    {
        "key": "htl_biocrude",
        "name": "Hydrothermal Liquefaction (HTL) Bio-Crude",
        "group": "Thermochemical Bio-Oils",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "description": (
            "Hydrothermal liquefaction cooks wet biomass - sewage sludge, "
            "manure, food waste, wet algae - in hot compressed water "
            "(300-350 C, 150-200 bar) into a bio-crude oil, turning the "
            "water that ruins other processes into the reaction medium. It "
            "is the thermochemical answer to wastes that are too wet to "
            "burn or pyrolyze economically. Bio-crude yields of 30-50 "
            "percent by dry weight are reported, with lower oxygen than "
            "pyrolysis oil. Status: TRL 5-6 - continuous pilot plants run, "
            "including on sewage sludge, but no commercial-scale transport-"
            "fuel plant operates yet. Honest framing: HTL elegantly solves "
            "the wet-feedstock problem, but high-pressure hot-water "
            "processing at scale is its own engineering mountain, and "
            "upgrading bio-crude to drop-in fuel is still being proven."
        ),
        "how_it_works": (
            "Wet feedstock (no drying needed - typically 80-90 percent "
            "water) is pressurized and heated to 300-350 C, where water "
            "becomes a reactive medium: hydrolysis, depolymerization, and "
            "repolymerization convert the organics to a water-immiscible "
            "bio-crude that separates by gravity. The aqueous byproduct "
            "carries dissolved organics and most nutrients - recycling it "
            "improves yields but concentrates inhibitors. Bio-crude "
            "(oxygen typically 10-20 percent, LHV ~30-35 MJ/kg) still needs "
            "hydrotreating for transport fuel. The process heat integration "
            "is critical: heating that much water is energetically "
            "expensive, so efficient heat exchangers make or break the "
            "energy balance."
        ),
        "key_points": [
            "Conditions: 300-350 C, 150-200 bar in water; wet feeds need no drying.",
            "Bio-crude yields 30-50 percent of dry feed; oxygen 10-20 percent; LHV ~30-35 MJ/kg.",
            "Ideal feeds: sewage sludge, manure, food waste, wet algae - wastes too wet for pyrolysis.",
            "Aqueous byproduct recycles nutrients but concentrates inhibitors.",
            "Heat integration decides the energy balance - heating water is expensive.",
            "Status: TRL 5-6 - continuous pilots; no commercial transport-fuel plant yet.",
        ],
        "requirements": [
            "Wet waste feedstock with gate-fee or negative-cost economics.",
            "High-pressure HTL reactor with corrosion-resistant metallurgy.",
            "Heat-recovery exchangers and aqueous-phase treatment/recycle.",
            "Hydrotreating capacity for bio-crude upgrading.",
        ],
        "standards": [
            "Upgraded products to ASTM D975 / EN 15940 / ASTM D7566 as applicable.",
            "Pressure equipment to ASME BPVC or equivalent.",
        ],
        "citations": [CIT_DOE_BIO, CIT_NREL, CIT_IEA_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature HTL plant sited at a "
            "wastewater treatment works, taking sludge at zero transport "
            "cost and returning treated water to the works. The Signature "
            "heat-exchanger network is designed for the actual slurry "
            "fouling rates measured in pilot runs, with clean-in-place "
            "cycles scheduled from pressure-drop data, and the Signature "
            "aqueous-phase loop recovers ammonia as fertilizer before "
            "recycle."
        ),
    },
    {
        "key": "waste_gasification_syngas",
        "name": "Waste Gasification to Syngas Fuels",
        "group": "Biogas and Waste Pathways",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "description": (
            "Gasification converts municipal solid waste, refuse-derived "
            "fuel, or mixed residues into syngas (CO + H2) at 800-1000 C "
            "with limited oxygen - a bridge from the waste problem to the "
            "fuel market via Fischer-Tropsch, methanol, or ethanol "
            "synthesis. The concept is decades old and the failures are "
            "well documented: tar formation, feedstock heterogeneity, and "
            "contaminants have idled or bankrupted high-profile waste-to-"
            "fuel ventures. Honest framing is essential here: waste "
            "gasification for POWER is commercial; waste gasification to "
            "CLEAN syngas for FUEL synthesis is TRL 6-8 depending on the "
            "design, with a graveyard of first plants proving that the "
            "gap between power-grade and synthesis-grade syngas is where "
            "projects die."
        ),
        "how_it_works": (
            "Sorted waste is gasified in fluidized-bed or entrained-flow "
            "reactors; the raw syngas carries tars, particulates, HCl, H2S, "
            "alkali, and heavy metals that must be removed to the parts-per-"
            "billion level for catalytic fuel synthesis. Cleanup trains - "
            "scrubbers, guard beds, reformers - routinely cost as much as "
            "the gasifier. The clean syngas then feeds Fischer-Tropsch "
            "(diesel/jet), methanol synthesis, or mixed-alcohol synthesis. "
            "Plasma gasification is a variant using plasma torches for very "
            "high temperatures and tar destruction, at high electricity "
            "cost. The economic logic only works with tipping fees for the "
            "waste plus fuel revenue - neither alone usually suffices."
        ),
        "key_points": [
            "Gasification: 800-1000 C, limited oxygen; waste -> syngas -> fuels via FT, methanol, or alcohols.",
            "Synthesis-grade syngas needs ppb-level cleanup; cleanup can cost as much as the gasifier.",
            "Power-grade gasification is commercial; fuel-synthesis grade is TRL 6-8 with notable failures.",
            "Economics need tipping fees PLUS fuel revenue - neither alone usually suffices.",
            "Feedstock heterogeneity (chlorine, metals, moisture swings) is the operational enemy.",
            "Status: emerging - proven concept, unproven as a repeatable commercial fuel business.",
        ],
        "requirements": [
            "Waste supply contracts with tipping fees and composition limits.",
            "Gasifier plus full synthesis-grade cleanup train.",
            "Fuel synthesis unit (FT, methanol, or mixed alcohols).",
            "Residue/ash handling with heavy-metal management.",
        ],
        "standards": [
            "Fuel products to ASTM D975 / D7566 / methanol specs as applicable.",
            "Emissions to waste-incineration directives (e.g. EU IED) where applicable.",
        ],
        "citations": [CIT_DOE_BIO, CIT_IEA_ETP, CIT_IRENA_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature waste-to-fuel design "
            "that refuses mixed MSW at the gate - it contracts "
            "pre-sorted commercial and industrial residues with measured "
            "chlorine and ash caps, the variable the failed plants "
            "ignored. The Signature cleanup train is instrumented per "
            "contaminant with bypass-able guard beds, and the Signature "
            "contract model shares tipping-fee revenue with the fuel "
            "offtaker so both sides survive feedstock shocks."
        ),
    },
    {
        "key": "uco_dropin",
        "name": "Used Cooking Oil to Drop-In Fuels",
        "group": "Biogas and Waste Pathways",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "description": (
            "Used cooking oil (UCO) is the premier waste feedstock of the "
            "emerging fuel economy: collected from restaurants and food "
            "processors, filtered, and hydrotreated into renewable diesel "
            "or HEFA jet. Because the carbon was already emitted to grow "
            "the food, UCO fuels score among the lowest carbon intensities "
            "of any biofuel and command premium prices under low-carbon "
            "fuel policies. The honest complication is fraud: UCO's premium "
            "has driven documented cases of virgin palm oil mislabeled as "
            "used oil, triggering anti-dumping investigations and tougher "
            "chain-of-custody rules. The CONVERSION is TRL 9 and routine; "
            "the SUPPLY CHAIN integrity is the emerging discipline, and "
            "this record covers both."
        ),
        "how_it_works": (
            "Collection networks aggregate oil from food outlets; the oil "
            "is filtered, dewatered, and tested (free fatty acids, "
            "moisture, impurities, and increasingly forensic markers). "
            "Pretreatment removes phosphorus, metals, and chlorides that "
            "poison hydrotreating catalysts - UCO is dirtier than virgin "
            "oils and needs robust guard beds. Hydrodeoxygenation plus "
            "isomerization yields renewable diesel (EN 15940) or, with "
            "jet-cut fractionation, HEFA-SPK (ASTM D7566 Annex A2). "
            "Mass-balance chain-of-custody tracks certified tonnes through "
            "shared infrastructure. Emerging forensics - fatty-acid "
            "profiling, contaminant markers, radiocarbon dating to prove "
            "recent biological origin - are becoming part of serious "
            "procurement."
        ),
        "key_points": [
            "Premier waste feedstock: lowest carbon-intensity scores among biofuels, premium policy value.",
            "Conversion is TRL 9 and routine; supply-chain integrity is the emerging discipline.",
            "Documented fraud (virgin oil sold as UCO) triggered anti-dumping cases and stricter auditing.",
            "Pretreatment must handle phosphorus, metals, chlorides - UCO is harder on catalysts than virgin oil.",
            "Forensic procurement: fatty-acid profiles, contaminant markers, radiocarbon dating.",
            "Products: renewable diesel (EN 15940) or HEFA-SPK jet (ASTM D7566 Annex A2).",
        ],
        "requirements": [
            "Collection network with documented chain of custody to the fryer.",
            "Pretreatment and forensic testing capability for fraud screening.",
            "Hydrotreating complex with guard beds sized for waste-oil contaminants.",
            "Mass-balance certification under a recognized scheme (ISCC, RSB).",
        ],
        "standards": [
            "EN 15940 / ASTM D975 for renewable diesel; ASTM D7566 Annex A2 for jet.",
            "ISCC / RSB chain-of-custody and mass-balance rules.",
        ],
        "citations": [CIT_IEA_BIO, CIT_ASTM_D7566, CIT_EN15940],
        "sig_lens": (
            "Signature re-engineering: a Signature UCO procurement system "
            "that tests every inbound batch with a rapid forensic panel - "
            "fatty-acid profile, polymer markers from frying, radiocarbon - "
            "before it unloads, rejecting fraud at the gate instead of "
            "auditing it later. The Signature collection model pays "
            "restaurants on measured oil quality, aligning incentives, and "
            "the Signature ledger publishes aggregate fraud-rejection "
            "statistics so buyers can see the integrity they are paying for."
        ),
    },
    {
        "key": "plastic_pyrolysis_fuel",
        "name": "Plastic Waste Pyrolysis to Fuel Oil",
        "group": "Biogas and Waste Pathways",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "description": (
            "Pyrolysis of waste plastic heats sorted polyolefins to "
            "400-500 C without oxygen, cracking the long polymer chains "
            "back into liquid hydrocarbons - essentially running the "
            "refinery in reverse. It addresses plastics that mechanical "
            "recycling cannot handle (films, mixed polyolefins), producing "
            "a pyrolysis oil usable as refinery feed or, after upgrading, "
            "fuel. Status is TRL 6-7: plants operate, but economics are "
            "tight and the regulatory question - does pyrolysis oil count "
            "as recycled content, and under what mass-balance attribution "
            "rules - is still being settled in major markets. Honest "
            "framing: the chemistry works and plants run, but plastic "
            "pyrolysis is not yet a proven money-maker, and chlorine from "
            "PVC contamination is the ever-present operational hazard."
        ),
        "how_it_works": (
            "Sorted polyolefin waste (PE, PP; polystyrene also cracks well) "
            "is shredded, melted, and pyrolyzed; the vapors condense to a "
            "waxy oil rich in olefins and paraffins. PVC must be excluded "
            "or removed - its chlorine becomes HCl that corrodes equipment "
            "and poisons downstream catalysts - so feed sorting and HCl "
            "scrubbing are essential. The raw oil is typically sold as "
            "refinery or steam-cracker feed (where mass-balance attribution "
            "rules decide how much counts as recycled) or hydrotreated to "
            "fuel. Yields of 60-80 percent liquid are achievable on clean "
            "polyolefin feed; real mixed-waste yields are lower."
        ),
        "key_points": [
            "Cracks polyolefins (PE, PP) back to hydrocarbon liquids - handles plastics mechanical recycling cannot.",
            "PVC/chlorine contamination is the operational hazard - sorting and HCl scrubbing essential.",
            "Typical outlet: refinery or cracker feed under mass-balance attribution rules (still being settled).",
            "Yields 60-80 percent liquid on clean feed; lower on real mixed waste.",
            "Regulatory status of pyrolysis oil as recycled content varies by market.",
            "Status: TRL 6-7 - plants operating; commercial economics not yet proven at scale.",
        ],
        "requirements": [
            "Sorted polyolefin feed with PVC exclusion and chlorine monitoring.",
            "Pyrolysis reactor with HCl scrubbing and wax handling.",
            "Offtake as refinery feed or hydrotreating for fuel use.",
            "Mass-balance accounting compliant with the target market's rules.",
        ],
        "standards": [
            "Mass-balance attribution per market rules (e.g. EU, US state programs - evolving).",
            "Fuel products to applicable ASTM/EN specs after upgrading.",
        ],
        "citations": [CIT_IEA_ETP, CIT_DOE_BIO, CIT_IRENA_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature plastic-pyrolysis plant "
            "with inline chlorine detection that diverts suspect feed "
            "before it reaches the reactor, protecting the metallurgy that "
            "chlorine destroys. The Signature sorting specification sets "
            "measured PVC limits per bale rather than trusting supplier "
            "labels, and the Signature mass-balance ledger is built for "
            "auditors from day one, tracking every kilogram from bale to "
            "oil."
        ),
    },
    {
        "key": "bio_butanol",
        "name": "Bio-Butanol by Advanced Fermentation",
        "group": "Renewable Diesel and Drop-In Biofuels",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "description": (
            "Bio-butanol is a four-carbon alcohol fermented from sugars or "
            "cellulosic feedstocks, superior to ethanol as a fuel in almost "
            "every physical respect: higher energy density (29.2 MJ/kg, "
            "26.9 MJ per litre), lower water affinity, higher octane "
            "blending value, and compatibility with existing gasoline "
            "infrastructure at higher blend rates. The classic ABE "
            "(acetone-butanol-ethanol) fermentation is a century old; the "
            "emerging part is engineered microbes and continuous recovery "
            "that make it economic - butanol is toxic to the microbes that "
            "make it, capping titers around 2 percent. Status: TRL 7-8. "
            "Demonstration and first-commercial plants have operated, but "
            "bio-butanol has not yet broken through to commodity scale, "
            "partly because cheap ethanol owns the oxygenate market."
        ),
        "how_it_works": (
            "Engineered Clostridia or other hosts ferment sugars via the "
            "ABE pathway; because butanol kills the culture above ~2 "
            "percent, product must be removed during fermentation - gas "
            "stripping, pervaporation, or adsorption (in-situ product "
            "recovery). The recovered butanol is distilled; the acetone "
            "and ethanol co-products are sold or converted. Isobutanol "
            "variants (via engineered yeast or E. coli) are preferred for "
            "gasoline blending and as an alcohol-to-jet feedstock. "
            "Cellulosic sugars as feedstock deepen the carbon savings but "
            "add the pretreatment/hydrolysis chain. Energy content: "
            "n-butanol LHV 33.1 MJ/kg gravimetric, 26.9 MJ/L volumetric - "
            "about 83 percent of gasoline's volumetric energy versus "
            "ethanol's 67 percent."
        ),
        "key_points": [
            "Four-carbon alcohol: 26.9 MJ/L volumetric - far closer to gasoline than ethanol.",
            "Low water affinity and high blend compatibility with existing gasoline infrastructure.",
            "Butanol toxicity caps fermentation titers ~2 percent - in-situ product recovery is mandatory.",
            "Isobutanol preferred for blending and as alcohol-to-jet feedstock.",
            "Classic ABE fermentation is old; engineered hosts and continuous recovery are the emerging part.",
            "Status: TRL 7-8 - demonstrated and first-commercial; not yet commodity scale.",
        ],
        "requirements": [
            "Sugar or cellulosic-sugar feedstock supply.",
            "Fermentation with in-situ product recovery (stripping, pervaporation, or adsorption).",
            "Distillation and co-product handling for acetone and ethanol.",
            "Fuel quality testing for the target blend specification.",
        ],
        "standards": [
            "ASTM D7862 - butanol for blending with gasoline.",
            "EN 228 gasoline specification for blended fuels.",
        ],
        "citations": [CIT_DOE_BIO, CIT_NREL, CIT_IRENA_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature bio-butanol plant that "
            "couples fermentation to a pervaporation membrane sized from "
            "measured toxicity curves, holding the broth permanently below "
            "the inhibition threshold so the culture never stalls. The "
            "Signature host-selection protocol screens engineered strains "
            "on the actual hydrolysate, not clean glucose, and the "
            "Signature co-product plan converts the acetone stream to "
            "isopropanol fuel blendstock instead of selling it at chemical "
            "prices."
        ),
    },
    {
        "key": "marine_biofuels",
        "name": "Sustainable Marine Biofuels (Bio-Bunker Blends)",
        "group": "Renewable Diesel and Drop-In Biofuels",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "description": (
            "Bio-bunker fuels bring drop-in biofuels to shipping: used-"
            "cooking-oil methyl ester, HVO, or pyrolysis-derived blends "
            "mixed with conventional marine fuel to cut a vessel's "
            "greenhouse-gas intensity without engine changes. With the IMO's "
            "carbon-intensity rules tightening and the EU folding shipping "
            "into emissions trading, bio-bunker demand went from "
            "demonstration trials to routine commercial supply at major "
            "ports within a few years - one of the fastest "
            "demonstration-to-market transitions in this database. Honest "
            "framing: the fuels work and ships burn them daily, but supply "
            "is still a small fraction of bunker demand, sustainability "
            "certification is mandatory to prevent the UCO fraud problems "
            "migrating to sea, and long-term the sector eyes ammonia and "
            "methanol."
        ),
        "how_it_works": (
            "Bio-components (typically FAME biodiesel from waste oils, HVO, "
            "or advanced blends) are mixed with very-low-sulfur fuel oil or "
            "marine gasoil at terminals, commonly in B20-B30 blends "
            "(20-30 percent bio), and bunkered like ordinary fuel. Quality "
            "control follows ISO 8217 marine fuel specs plus bio-component "
            "checks (oxidation stability, cold flow, microbial growth - "
            "biodiesel's known issues at sea). Greenhouse-gas accounting "
            "uses well-to-wake life-cycle values; a B30 waste-oil blend "
            "typically cuts well-to-wake CO2e by roughly a quarter. "
            "Ports with bio-bunker supply chains (Singapore, Rotterdam, "
            "and others) handle certification, segregation, and mass-"
            "balance documentation."
        ),
        "key_points": [
            "Drop-in blends (commonly B20-B30) cut vessel GHG intensity with no engine changes.",
            "Feedstocks: waste-oil FAME, HVO, advanced blends - sustainability certification mandatory.",
            "Quality control to ISO 8217 plus bio-specific checks (stability, cold flow, microbes).",
            "B30 waste-oil blend typically cuts well-to-wake CO2e by roughly 25 percent.",
            "Fastest demonstration-to-market transition here - routine commercial supply at major ports.",
            "Status: TRL 9 for the blends; emerging in scale - still a small share of bunker demand.",
        ],
        "requirements": [
            "Certified sustainable bio-component supply (ISCC or equivalent).",
            "Terminal blending with ISO 8217 quality control.",
            "Well-to-wake GHG documentation for regulatory compliance.",
            "Crew procedures for biofuel handling (stability, water, microbes).",
        ],
        "standards": [
            "ISO 8217 - marine fuel specifications.",
            "IMO CII/EEXI and EU FuelEU Maritime / ETS accounting rules.",
        ],
        "citations": [CIT_IEA_BIO, CIT_IEA_ETP],
        "sig_lens": (
            "Signature re-engineering: a Signature bio-bunker supply model "
            "that blends at the port from segregated certified tanks with "
            "batch-level GHG documentation, so each stem carries its own "
            "well-to-wake number instead of a fleet average. The Signature "
            "quality protocol tests oxidation stability and microbial "
            "contamination on every barge, and the Signature procurement "
            "rule buys only bio-components with farm-to-funnel traceability."
        ),
    },
    {
        "key": "renewable_mtg",
        "name": "Renewable Methanol-to-Gasoline",
        "group": "Renewable Diesel and Drop-In Biofuels",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "description": (
            "Methanol-to-gasoline (MTG) converts methanol - including "
            "renewable or e-methanol - into high-octane gasoline over "
            "zeolite catalysts, producing a true drop-in gasoline with no "
            "blend limit. The process ran commercially on natural-gas-"
            "derived methanol in New Zealand in the 1980s-90s, proving the "
            "chemistry at scale; the RENEWABLE variant, fed by biomass- or "
            "waste-derived methanol, is the emerging application, with "
            "plants operating in China on coal- and coke-oven-gas methanol "
            "and renewable-methanol projects in development. Honest "
            "framing: MTG the process is proven history; renewable MTG is "
            "emerging because it waits on affordable renewable methanol - "
            "the fuel is only as green as its methanol feed."
        ),
        "how_it_works": (
            "Methanol is dehydrated to dimethyl ether, then converted over "
            "HZSM-5 zeolite at 350-400 C: the shape-selective catalyst "
            "builds the C1 fragments into the gasoline boiling range "
            "(C5-C11), rich in aromatics and branched paraffins for octane. "
            "Roughly 40 percent of the methanol mass becomes gasoline, "
            "with LPG-range byproducts and water; the exothermic reaction "
            "needs careful heat management across adiabatic beds. The "
            "gasoline meets conventional specs (EN 228 / ASTM D4814) "
            "directly - it IS gasoline, just made from methanol. Catalyst "
            "deactivation by coking requires periodic regeneration, a "
            "solved operational routine from the commercial plants."
        ),
        "key_points": [
            "Converts methanol to true drop-in gasoline over HZSM-5 zeolite - no blend limit.",
            "Proven commercially in the 1980s-90s on fossil methanol; renewable feed is the emerging part.",
            "About 40 percent of methanol mass becomes gasoline; LPG and water are byproducts.",
            "Product meets EN 228 / ASTM D4814 directly - chemically ordinary gasoline.",
            "Climate benefit comes entirely from the methanol source - the plant cannot fix dirty methanol.",
            "Status: process TRL 9 (historical); renewable-methanol MTG TRL 7-8.",
        ],
        "requirements": [
            "Renewable or e-methanol supply with documented carbon intensity.",
            "MTG reactor section with catalyst regeneration capability.",
            "Product fractionation and gasoline specification testing.",
            "Heat management for the exothermic conversion beds.",
        ],
        "standards": [
            "EN 228 / ASTM D4814 - gasoline specifications for the product.",
            "Methanol feed quality per process licensor specification.",
        ],
        "citations": [CIT_IEA_ETP, CIT_DOE_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature renewable-MTG complex "
            "that makes its own methanol from biomass gasification on the "
            "same site, so the gasoline's carbon story is auditable fence-"
            "to-funnel. The Signature catalyst-management protocol tracks "
            "coking rates per feedstock batch and schedules regeneration "
            "from measured activity, and the Signature LPG byproduct is "
            "routed to a renewable-LPG fuel product instead of being "
            "flared or sold at fuel-gas value."
        ),
    },
    {
        "key": "dme_fuel",
        "name": "Dimethyl Ether (Bio-DME and E-DME)",
        "group": "Hydrogen Carriers and Novel Fuels",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "description": (
            "Dimethyl ether (CH3OCH3) is the simplest ether - a clean-"
            "burning, high-cetane fuel that can replace diesel in "
            "compression-ignition engines or LPG in heating. Bio-DME is made "
            "by dehydrating bio-methanol or directly from biomass syngas; "
            "e-DME from green hydrogen and captured CO2 via methanol. Its "
            "magic is combustion: no carbon-carbon bonds means essentially "
            "no soot, and with exhaust-gas recirculation it can meet "
            "stringent NOx limits without complex aftertreatment. Status: "
            "TRL 7-8. Demonstration truck fleets ran on bio-DME in Sweden, "
            "and DME is a commercial chemical; as a FUEL at scale it "
            "remains emerging, held back by the need for dedicated fuel "
            "systems (it is a gas at ambient conditions, stored as a liquid "
            "under ~5 bar like LPG) and by methanol-feedstock economics."
        ),
        "how_it_works": (
            "Methanol is dehydrated over alumina or zeolite catalysts "
            "(2 CH3OH -> CH3OCH3 + H2O), or syngas converts directly in a "
            "single-step process. DME liquefies at about 5 bar at room "
            "temperature, so storage and handling mirror LPG practice - "
            "pressure tanks, sealed systems. In a diesel engine, DME's "
            "cetane number of 55-60 gives excellent ignition, and soot-free "
            "combustion slashes particulate emissions; its lower heating "
            "value (28.4 MJ/kg, ~19 MJ per litre as liquid) means larger "
            "fuel tanks and modified injection (DME attacks some seals and "
            "has low lubricity, requiring additives). As an LPG substitute "
            "it burns in existing burner designs with minor adjustments."
        ),
        "key_points": [
            "Simplest ether fuel; cetane 55-60; essentially soot-free combustion (no C-C bonds).",
            "LHV 28.4 MJ/kg (~19 MJ/L liquid); stored at ~5 bar like LPG.",
            "Low lubricity and seal compatibility need additives and material selection.",
            "Routes: bio-methanol dehydration, direct biomass-syngas synthesis, or e-DME via green H2 + CO2.",
            "Demonstration truck fleets operated; commercial chemical, emerging fuel.",
            "Status: TRL 7-8 - proven in fleets, awaiting fuel-system scale and feedstock economics.",
        ],
        "requirements": [
            "Bio- or e-methanol supply, or biomass syngas with DME synthesis.",
            "DME dehydration/synthesis unit and LPG-type storage.",
            "DME-compatible fuel systems (seals, lubricity additive, larger tanks).",
            "Engine calibration for DME combustion characteristics.",
        ],
        "standards": [
            "ISO 16861 - DME fuel specifications (under development/harmonization).",
            "LPG handling practice (pressure equipment, odorization where required).",
        ],
        "citations": [CIT_IEA_ETP, CIT_DOE_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature DME fuel system that "
            "solves the lubricity problem with a metered bio-based "
            "lubricity additive package validated on the actual injection "
            "hardware, and a Signature single-step syngas-to-DME reactor "
            "design that skips the methanol intermediate to cut capital "
            "cost. The Signature fleet protocol instruments fuel "
            "consumption against diesel baselines on identical routes so "
            "the efficiency claim is measured, not modeled."
        ),
    },
    {
        "key": "formic_acid_carrier",
        "name": "Formic Acid as Hydrogen Carrier",
        "group": "Hydrogen Carriers and Novel Fuels",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "description": (
            "Formic acid (HCOOH) is a liquid at room temperature that "
            "releases hydrogen on demand by catalytic dehydrogenation "
            "(HCOOH -> H2 + CO2) - a hydrogen carrier you can pour. It "
            "carries 4.4 percent hydrogen by weight (53 g H2 per litre), "
            "stores and ships in ordinary chemical tankage, and its "
            "dehydrogenation runs at modest temperatures with ruthenium or "
            "iridium catalysts. The round trip is elegant: CO2 "
            "hydrogenation makes formic acid, dehydrogenation returns "
            "hydrogen plus the same CO2, so the carrier loop can be "
            "carbon-neutral. Status: TRL 4-6 - laboratory and pilot "
            "demonstrations, including formic-acid-powered fuel cell "
            "concepts. Honest framing: a clever carrier chemistry still "
            "proving durability, catalyst cost, and system efficiency "
            "outside the lab."
        ),
        "how_it_works": (
            "Charging: CO2 + H2 -> HCOOH over catalysts at moderate "
            "pressure, ideally using the CO2 that will later be released. "
            "Release: formic acid passes over a dehydrogenation catalyst "
            "(60-120 C) yielding hydrogen and CO2; the competing "
            "dehydration path (HCOOH -> CO + H2O) must be suppressed because "
            "carbon monoxide poisons PEM fuel cells - selectivity is the "
            "catalyst's whole job. The hydrogen/CO2 mixture feeds a fuel "
            "cell directly or is purified. Direct formic acid fuel cells "
            "(DFAFC) skip the release step, oxidizing the acid "
            "electrochemically. The 4.4 wt percent capacity looks low next "
            "to LOHC or ammonia, but the liquid handling and mild "
            "conditions are the compensation."
        ),
        "key_points": [
            "Liquid at room temperature; releases H2 by catalytic dehydrogenation at 60-120 C.",
            "Capacity 4.4 wt percent H2 (53 g/L); ordinary chemical tankage suffices.",
            "Catalyst must suppress the CO-forming path - CO poisons PEM fuel cells.",
            "Round trip (CO2 hydrogenation / dehydrogenation) can be carbon-neutral in CO2.",
            "Direct formic acid fuel cells oxidize the carrier electrochemically.",
            "Status: TRL 4-6 - lab and pilot demonstrations; durability and cost still being proven.",
        ],
        "requirements": [
            "Formic acid synthesis from CO2 and hydrogen (charging infrastructure).",
            "Selective dehydrogenation catalyst with CO suppression demonstrated.",
            "CO cleanup or tolerant fuel cell if feeding PEM systems.",
            "Materials compatible with formic acid (corrosive to some metals).",
        ],
        "standards": [
            "Hydrogen product purity to ISO 14687 if feeding fuel cells.",
            "Chemical handling practice for corrosive liquids.",
        ],
        "citations": [CIT_IEA_LOHC, CIT_IEA_H2],
        "sig_lens": (
            "Signature re-engineering: a Signature formic-acid power unit "
            "that pairs the dehydrogenation reactor with a selective "
            "methanation guard bed, converting any trace CO to methane "
            "before it reaches the fuel cell - solving the poisoning "
            "problem by design. The Signature catalyst program targets "
            "iron-based formulations to escape ruthenium cost, and the "
            "Signature round-trip analysis measures the full charge-"
            "release efficiency on a bench loop before any scale claims."
        ),
    },
    {
        "key": "lohc",
        "name": "Liquid Organic Hydrogen Carriers (LOHC)",
        "group": "Hydrogen Carriers and Novel Fuels",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "description": (
            "LOHC systems store hydrogen by chemically binding it to a "
            "reusable organic liquid - hydrogenation loads the carrier, "
            "dehydrogenation releases pure hydrogen at the destination, "
            "and the unloaded liquid ships back for another cycle. The "
            "leading carrier, dibenzyltoluene (a heat-transfer oil), holds "
            "6.2 percent hydrogen by weight and handles like diesel: "
            "non-toxic, barely flammable, shippable in ordinary tankers at "
            "ambient temperature and pressure. That ordinariness is the "
            "whole value proposition: hydrogen logistics using the "
            "existing liquid-fuel infrastructure. Status: TRL 6-7 - "
            "pilot plants charge and release hydrogen, and commercial "
            "offerings exist, but no large-scale LOHC hydrogen trade runs "
            "yet. The penalty is heat: dehydrogenation needs 250-320 C, "
            "an energy cost paid at every release."
        ),
        "how_it_works": (
            "Hydrogenation: the lean carrier (e.g. dibenzyltoluene) reacts "
            "with hydrogen over platinum or nickel catalysts at 100-200 C "
            "and moderate pressure, becoming the hydrogen-rich form "
            "(perhydro-dibenzyltoluene). The charged liquid is stored and "
            "transported at ambient conditions. Dehydrogenation: heating to "
            "250-320 C over catalyst releases the hydrogen; the heat "
            "requirement - roughly a quarter to a third of the hydrogen's "
            "energy - is the system's thermodynamic tax, ideally paid with "
            "waste heat at the release site. Toluene/methylcyclohexane was "
            "the early carrier but toluene's toxicity and volatility favor "
            "dibenzyltoluene. Carrier degradation over hundreds of cycles "
            "is the durability question under test."
        ),
        "key_points": [
            "Dibenzyltoluene carrier: 6.2 wt percent H2; ambient liquid handling like diesel.",
            "Hydrogenation at 100-200 C; release at 250-320 C - heat is the thermodynamic tax (~25-30 percent).",
            "Uses existing tanker, tank, and port infrastructure - no cryogenics, no high pressure.",
            "Carrier is reusable; degradation over hundreds of cycles is the durability question.",
            "Best economics where waste heat is available at the release site.",
            "Status: TRL 6-7 - pilots operating and commercial offerings exist; no large-scale trade yet.",
        ],
        "requirements": [
            "Hydrogenation plant at the hydrogen source; dehydrogenation unit at the user.",
            "Carrier inventory (dibenzyltoluene) and cycle-life monitoring.",
            "Heat source for dehydrogenation (waste heat preferred).",
            "Hydrogen purification to ISO 14687 after release if feeding fuel cells.",
        ],
        "standards": [
            "ISO 14687 hydrogen purity after release.",
            "Chemical transport practice for heat-transfer oils (non-dangerous goods classification).",
        ],
        "citations": [CIT_IEA_LOHC, CIT_IEA_H2],
        "sig_lens": (
            "Signature re-engineering: a Signature LOHC release unit that "
            "integrates with industrial waste-heat streams - the "
            "dehydrogenation heat comes free from a neighboring plant's "
            "exhaust, flipping the thermodynamic tax into a heat-recovery "
            "credit. The Signature carrier-management protocol samples and "
            "reconditions the dibenzyltoluene on a measured degradation "
            "curve, and the Signature logistics model runs the charged and "
            "lean legs on backhaul tanker capacity."
        ),
    },
    {
        "key": "ammonia_cracking",
        "name": "Ammonia Cracking for Hydrogen Release",
        "group": "Hydrogen Carriers and Novel Fuels",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "description": (
            "Ammonia cracking reverses the Haber-Bosch reaction - "
            "2 NH3 -> N2 + 3 H2 at 400-600 C over ruthenium or nickel "
            "catalysts - releasing hydrogen from ammonia at the point of "
            "use. It is the missing half of the ammonia hydrogen economy: "
            "ammonia ships hydrogen across oceans cheaply (see the green "
            "ammonia record), and cracking liberates it for fuel cells, "
            "industry, or power where the hydrogen is needed. Status: TRL "
            "6-7 - cracking is old industrial chemistry (it made "
            "nitriding atmospheres for decades), but large-scale, "
            "high-purity, load-following crackers for the hydrogen economy "
            "are still in demonstration. The honest challenges: the heat "
            "demand, ruthenium catalyst cost, and purifying the hydrogen to "
            "fuel-cell grade (ammonia slip poisons PEM cells at parts-per-"
            "million levels)."
        ),
        "how_it_works": (
            "Vaporized ammonia passes over catalyst beds at 400-600 C "
            "(ruthenium most active, nickel cheaper); conversion per pass "
            "is equilibrium-limited, so efficient designs recycle or stage "
            "the beds. The product is 75 percent hydrogen, 25 percent "
            "nitrogen plus unconverted ammonia slip - fuel cells need the "
            "ammonia removed to below ~0.1 ppm, typically by adsorbents or "
            "membranes, because ammonia irreversibly poisons PEM membranes. "
            "The endothermic heat (about 30 kJ per mole of ammonia) can come "
            "from burning some ammonia or hydrogen, or from waste heat. "
            "System efficiency - ammonia in to fuel-cell-grade hydrogen out "
            "- lands around 70-80 percent for well-designed units, before "
            "counting the ammonia's own production energy."
        ),
        "key_points": [
            "Reaction: 2 NH3 -> N2 + 3 H2, 400-600 C, Ru or Ni catalyst - the reverse of Haber-Bosch.",
            "Completes the ammonia hydrogen chain: ship as ammonia, release as hydrogen at use.",
            "Ammonia slip must be removed to ~0.1 ppm - it irreversibly poisons PEM fuel cells.",
            "Heat demand ~30 kJ/mol NH3; ruthenium cost is the catalyst question.",
            "Industrial cracking is old chemistry; hydrogen-economy crackers are TRL 6-7.",
            "Status: demonstration units operating; large-scale fuel-cell-grade crackers emerging.",
        ],
        "requirements": [
            "Ammonia supply (green for a green hydrogen product).",
            "Cracker with heat supply and staged catalyst beds.",
            "Ammonia-slip purification to fuel-cell grade.",
            "Safety systems for ammonia handling at the release site.",
        ],
        "standards": [
            "ISO 14687 hydrogen purity for fuel cell use.",
            "Ammonia handling per fertilizer-industry practice.",
        ],
        "citations": [CIT_IEA_NH3, CIT_IEA_H2, CIT_ISO_14687],
        "sig_lens": (
            "Signature re-engineering: a Signature cracker that burns a "
            "metered slipstream of its own ammonia for reaction heat, "
            "making the unit thermally self-sufficient, followed by a "
            "Signature two-stage purification (adsorbent then membrane) "
            "with online ammonia-slip monitoring that trips the fuel cell "
            "feed before poisoning levels are reached. The Signature "
            "catalyst program tests nickel formulations against ruthenium "
            "on measured conversion-per-cost, not just conversion."
        ),
    },
    {
        "key": "ammonia_direct_combustion",
        "name": "Ammonia Direct Combustion (Maritime)",
        "group": "Hydrogen Carriers and Novel Fuels",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "description": (
            "Instead of cracking ammonia back to hydrogen, ammonia can be "
            "burned directly in marine two-stroke engines - the leading "
            "candidate for deep-sea shipping's zero-carbon fuel, since "
            "ammonia's energy density and existing global trade solve the "
            "bunkering problem that sinks most marine fuel candidates. "
            "Engine makers have demonstrated ammonia combustion in test "
            "engines and the first ammonia-capable vessels are under "
            "construction. The honest difficulties: ammonia burns slowly "
            "with a narrow flammability range (needs a pilot fuel, "
            "typically ~5-15 percent diesel or biodiesel), its nitrogen "
            "content can form fuel-NOx and the potent greenhouse gas N2O "
            "if combustion is poorly controlled, and it is toxic - "
            "bunkering safety is a serious new discipline. Status: TRL "
            "5-6 - test engines run; commercial service is just beginning."
        ),
        "how_it_works": (
            "Ammonia is stored as a refrigerated liquid (-33 C) or "
            "pressurized liquid (~10 bar) in the ship's fuel tanks, fed to "
            "a dual-fuel two-stroke engine where a small pilot injection "
            "of diesel ignites the ammonia charge (ammonia's autoignition "
            "temperature ~651 C is far too high for compression ignition "
            "alone). Combustion tuning walks a tightrope: hot enough to "
            "burn out N2O and unburned ammonia slip, cool or staged enough "
            "to limit NOx, with selective catalytic reduction cleaning up "
            "the rest. Ammonia slip past the engine must be near zero - "
            "both for toxicity and because N2O has ~273 times the warming "
            "potential of CO2. Fuel systems need ammonia-compatible "
            "materials and double-walled piping with leak detection."
        ),
        "key_points": [
            "Leading zero-carbon candidate for deep-sea shipping: bunkers like LPG, trades globally already.",
            "Needs pilot fuel (~5-15 percent diesel) - ammonia will not compression-ignite alone.",
            "Emissions tightrope: control fuel-NOx and N2O (GWP ~273) while eliminating ammonia slip.",
            "Toxic fuel - bunkering safety, double-walled piping, leak detection are new disciplines.",
            "Lower heating value 18.6 MJ/kg means roughly three and a half times the tank volume of fuel oil for equal energy.",
            "Status: TRL 5-6 - test engines demonstrated; first ammonia-capable vessels under construction.",
        ],
        "requirements": [
            "Green ammonia bunker supply with certification.",
            "Ammonia-capable dual-fuel engine and ammonia fuel-gas system.",
            "Exhaust aftertreatment (SCR) tuned for ammonia combustion.",
            "Crew training and safety procedures for toxic fuel handling.",
        ],
        "standards": [
            "IMO IGF Code interim guidelines for ammonia as fuel (in development).",
            "Classification society rules for ammonia-fueled vessels.",
        ],
        "citations": [CIT_IEA_NH3, CIT_IEA_ETP, CIT_IRENA_NH3],
        "sig_lens": (
            "Signature re-engineering: a Signature ammonia marine engine "
            "concept that replaces fossil pilot fuel with a biodiesel "
            "pilot injection, making the combustion event fully renewable, "
            "and adds a Signature N2O monitoring loop that trims injection "
            "timing in real time to hold N2O at its minimum. The Signature "
            "bunkering design uses a closed loading arm with vapor return "
            "so no ammonia escapes during fueling, and the Signature crew "
            "trainer is a full-mission simulator for ammonia emergencies."
        ),
    },
    {
        "key": "sofc_multifuel",
        "name": "Solid-Oxide Fuel Cell Multi-Fuels",
        "group": "Hydrogen Carriers and Novel Fuels",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "description": (
            "Solid-oxide fuel cells run at 800-1000 C on ceramic "
            "electrolytes, and that heat makes them fuel-flexible: they "
            "internally reform natural gas, biomethane, ammonia, or even "
            "diesel into hydrogen at the anode, generating electricity at "
            "50-65 percent electrical efficiency - the highest of any fuel "
            "cell family. As an EMERGING FUEL story, the SOFC is the device "
            "that lets tomorrow's fuels (biomethane, ammonia, e-methane) "
            "make power in buildings, data centers, and ships without "
            "waiting for a hydrogen pipeline. SOFC products are commercial "
            "(TRL 8-9 for natural-gas units); operation on ammonia and raw "
            "biogas is the emerging frontier (TRL 6-7). Honest framing: "
            "the cells work and warranties exist, but cost, slow start-up "
            "(hours to reach temperature), and thermal-cycling durability "
            "limit them to steady baseload roles."
        ),
        "how_it_works": (
            "Oxide ions (O2-) migrate through the yttria-stabilized "
            "zirconia electrolyte from cathode to anode, where they "
            "oxidize fuel - hydrogen, carbon monoxide, or internally "
            "reformed hydrocarbons and ammonia. Internal reforming uses "
            "the stack's own waste heat: CH4 + H2O -> CO + 3 H2 on the "
            "nickel anode, so methane enters and electricity leaves with "
            "no external reformer. Ammonia cracks thermally at SOFC "
            "temperatures, feeding hydrogen directly. Electrical "
            "efficiencies of 50-65 percent (LHV) are routine, with total "
            "efficiency over 90 percent in combined heat and power. The "
            "ceramic cells dislike thermal cycling - start-up takes hours "
            "and rapid temperature swings crack seals - so SOFCs serve "
            "continuous loads."
        ),
        "key_points": [
            "800-1000 C ceramic cells; 50-65 percent electrical efficiency, >90 percent in CHP.",
            "Internal reforming: methane, biomethane, ammonia, e-methane all usable without external reformer.",
            "Ammonia cracks thermally at stack temperature - direct ammonia SOFC is real.",
            "Slow start-up (hours) and thermal-cycling limits confine SOFCs to steady baseload.",
            "Natural-gas SOFC products are commercial; ammonia/biogas operation is TRL 6-7.",
            "Status: TRL 8-9 for the device; emerging as the power device for tomorrow's fuels.",
        ],
        "requirements": [
            "Fuel supply: biomethane, ammonia, e-methane, or natural gas during transition.",
            "Continuous baseload application (thermal cycling must be minimized).",
            "Heat-recovery integration for CHP economics.",
            "Desulfurization for sulfur-bearing fuels (anode poison).",
        ],
        "standards": [
            "IEC 62282 series - fuel cell safety and performance.",
            "Stationary fuel-cell installation codes per jurisdiction.",
        ],
        "citations": [CIT_DOE_FC, CIT_IEA_ETP],
        "sig_lens": (
            "Signature re-engineering: a Signature SOFC installation that "
            "runs on biomethane from the site's own waste and exports both "
            "power and high-grade heat to the process that made the fuel, "
            "closing the loop. The Signature thermal-management design "
            "keeps the stack at temperature through fuel-supply "
            "interruptions with a phase-change heat buffer, and the "
            "Signature fuel-blend controller shifts between biomethane and "
            "ammonia feed based on live fuel prices."
        ),
    },
    {
        "key": "iron_powder_combustion",
        "name": "Iron Powder Combustion Cycle (Metal Fuels)",
        "group": "Advanced Conversion Concepts",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "description": (
            "Iron powder burns: fine iron particles combust in air to iron "
            "oxide, releasing heat with zero carbon dioxide - a recyclable "
            "metal fuel. The oxide is then reduced back to iron with green "
            "hydrogen, closing a carbon-free cycle: energy goes in as "
            "hydrogen during reduction, comes out as heat during "
            "combustion, and the iron shuttles back and forth indefinitely. "
            "Iron's volumetric energy density (~57 MJ per litre of solid) "
            "rivals fossil fuels, though its gravimetric density (7.4 "
            "MJ/kg) does not. Status: TRL 4-5 - laboratory and pilot "
            "burners have fired iron powder for industrial heat, and the "
            "reduction step is proven metallurgy. Honest framing: an "
            "elegant circular concept still proving round-trip efficiency, "
            "particle handling at scale, and economics against direct "
            "hydrogen use."
        ),
        "how_it_works": (
            "Micron-scale iron powder is pneumatically conveyed into a "
            "burner and combusts: 4 Fe + 3 O2 -> 2 Fe2O3, releasing about "
            "7.4 MJ per kg of iron as high-temperature heat for steam or "
            "industrial processes. The flame temperature and particle "
            "behavior resemble pulverized-coal combustion closely enough "
            "that retrofitted coal burners are the development path. The "
            "spent oxide is collected and reduced back to iron powder - "
            "with green hydrogen (Fe2O3 + 3 H2 -> 2 Fe + 3 H2O) or in "
            "future direct electrolytic reduction. Round-trip efficiency "
            "depends on the reduction step; the combustion step itself is "
            "just heat. Nanoparticle sintering and oxide collection "
            "efficiency are the practical research fronts."
        ),
        "key_points": [
            "Burns iron to iron oxide with zero CO2; oxide reduced back with green hydrogen - a circular fuel.",
            "Volumetric energy density ~57 MJ/L rivals fossil fuels; gravimetric 7.4 MJ/kg does not.",
            "Burner technology parallels pulverized coal - retrofit path for coal plants exists in principle.",
            "Round-trip efficiency hinges on the reduction step, not the combustion.",
            "Particle sintering and oxide collection efficiency are the research fronts.",
            "Status: TRL 4-5 - pilot burners fired; economics versus direct hydrogen unproven.",
        ],
        "requirements": [
            "Micron-scale iron powder supply and pneumatic handling.",
            "Burner/boiler adapted for metal-fuel combustion and oxide collection.",
            "Green hydrogen (or electrolytic) reduction capacity to close the cycle.",
            "Oxide collection and powder reconditioning loop.",
        ],
        "standards": [
            "Combustible-dust handling practice (iron powder is a combustible dust).",
            "Boiler/pressure equipment codes for the heat-recovery side.",
        ],
        "citations": [CIT_IEA_ETP, CIT_IEA_H2],
        "sig_lens": (
            "Signature re-engineering: a Signature iron-fuel retrofit for "
            "a retired coal boiler - same steam cycle, new burners, with "
            "the oxide collected in the existing ash-handling system. The "
            "Signature particle specification defines the size distribution "
            "that burns out completely without sintering, measured in a "
            "Signature drop-tube furnace, and the Signature cycle analysis "
            "prices the hydrogen reduction step against direct hydrogen "
            "firing so the circular case is honestly compared."
        ),
    },
    {
        "key": "ekerosene_coelectrolysis",
        "name": "E-Kerosene by High-Temperature Co-Electrolysis",
        "group": "Hydrogen and Power-to-X",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "description": (
            "High-temperature co-electrolysis feeds steam and CO2 together "
            "into solid-oxide electrolysis cells at 700-850 C, producing "
            "syngas (H2 + CO) in a single step - the most electrically "
            "efficient front end for e-kerosene, because the heat does part "
            "of the splitting work that electricity does in low-temperature "
            "electrolyzers. The syngas feeds Fischer-Tropsch synthesis to "
            "jet fuel. Status: TRL 6-7 - co-electrolysis stacks run at "
            "pilot scale and e-kerosene demonstration projects are "
            "operating, but the ceramic stacks are still proving lifetime "
            "at scale. Honest framing: the efficiency advantage is real "
            "and measured, yet the technology is younger than PEM/alkaline "
            "electrolysis, and e-kerosene's cost still needs both cheap "
            "electricity and a cheap CO2 source."
        ),
        "how_it_works": (
            "In a solid-oxide cell, oxide ions cross the ceramic "
            "electrolyte: H2O + CO2 + electricity + heat -> H2 + CO + O2-. "
            "At 700-850 C the thermodynamics favor the split, so "
            "electrical efficiency can exceed 90 percent (LHV) with a free "
            "or cheap heat source - far above low-temperature "
            "electrolysis. The H2/CO ratio is tuned for Fischer-Tropsch "
            "(about 2:1), and the syngas goes straight to FT synthesis and "
            "upgrading to jet cut, certifiable under ASTM D7566 Annex A1. "
            "Degradation mechanisms - nickel coarsening, chromium poisoning "
            "from interconnects, seal failures - are the lifetime research "
            "front, with stack targets of 40,000+ hours."
        ),
        "key_points": [
            "Co-electrolyzes steam + CO2 to syngas in one step at 700-850 C - most efficient e-fuel front end.",
            "Electrical efficiency can exceed 90 percent LHV with cheap heat - thermodynamics favors high temperature.",
            "Syngas ratio tuned (~2:1 H2:CO) for direct Fischer-Tropsch to jet.",
            "Stack lifetime (Ni coarsening, Cr poisoning, seals) is the research front; 40,000 h targets.",
            "Product certifiable under ASTM D7566 Annex A1 (FT-SPK).",
            "Status: TRL 6-7 - pilot stacks and e-kerosene demos; scale-up of stack lifetime ongoing.",
        ],
        "requirements": [
            "Solid-oxide co-electrolysis stacks with heat integration.",
            "Steam and concentrated CO2 supply.",
            "Fischer-Tropsch synthesis and jet-cut upgrading.",
            "ASTM D7566 Annex A1 qualification for the kerosene.",
        ],
        "standards": [
            "ASTM D7566 Annex A1 - FT synthetic paraffinic kerosene.",
            "IEC 62282 electrolyzer-adjacent safety practice (high-temperature systems).",
        ],
        "citations": [CIT_IEA_ETP, CIT_ASTM_D7566, CIT_IEA_SAF],
        "sig_lens": (
            "Signature re-engineering: a Signature co-electrolysis plant "
            "sited at a geothermal or nuclear heat source so the 700-850 C "
            "heat is nearly free, maximizing the high-temperature "
            "advantage. The Signature stack-monitoring protocol tracks "
            "degradation per thousand hours against the 40,000-hour target "
            "and schedules stack replacement as a planned operating cost, "
            "and the Signature syngas-ratio controller trims steam/CO2 feed "
            "in real time for the FT reactor's preferred ratio."
        ),
    },
    {
        "key": "microbial_electrosynthesis",
        "name": "Microbial Electrosynthesis of Fuels",
        "group": "Advanced Conversion Concepts",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "description": (
            "Microbial electrosynthesis feeds electricity directly to "
            "microbes: electroactive bacteria take electrons from a cathode "
            "and reduce CO2 into acetate, methane, or longer-chain fuels - "
            "growing fuel from electricity and carbon dioxide at room "
            "temperature and pressure, with the microbe as the catalyst. "
            "Laboratory systems have made acetate, butyrate, and methane "
            "this way; companies run power-to-gas with biocatalysts at "
            "pilot scale. Status: TRL 3-4 for fuel synthesis proper - "
            "current densities and production rates are orders of magnitude "
            "below industrial needs. Honest framing: the most biologically "
            "elegant fuel concept in this database and the least ready; it "
            "belongs here as the research frontier, not as a coming "
            "product."
        ),
        "how_it_works": (
            "In a bioelectrochemical reactor, cathode-dwelling microbes "
            "(acetogens like Sporomusa ovata, or methanogenic archaea) "
            "accept electrons - directly or via evolved hydrogen - and fix "
            "CO2 through the Wood-Ljungdahl pathway into acetyl-CoA, then "
            "to acetate, which can be elongated to butyrate/caproate or "
            "converted onward. Methanogens short-circuit the chain to "
            "methane. The cathode replaces the hydrogen supply: instead of "
            "making H2 in an electrolyzer and feeding it to biology, the "
            "biology drinks electrons directly. Rates today are measured "
            "in grams per square metre of electrode per day - the "
            "fundamental challenge is electron-transfer kinetics at the "
            "biofilm interface, plus keeping the microbes happy for months "
            "of continuous operation."
        ),
        "key_points": [
            "Microbes reduce CO2 to fuels using cathode-supplied electrons - room temperature and pressure.",
            "Products demonstrated: acetate, butyrate, caproate, methane via the Wood-Ljungdahl pathway.",
            "Cathode replaces the electrolyzer - biology drinks electrons directly.",
            "Rates are grams per m2 per day - orders of magnitude below industrial needs.",
            "Electron-transfer kinetics at the biofilm interface is the fundamental challenge.",
            "Status: TRL 3-4 - research frontier; belongs here as science, not as a coming product.",
        ],
        "requirements": [
            "Bioelectrochemical reactor with high-surface-area cathodes.",
            "Selected electroactive culture and sterile-ish operating discipline.",
            "CO2 supply and downstream separation for the dilute products.",
            "Patience: this is a research platform, not a plant design.",
        ],
        "standards": [
            "No fuel-product standards apply yet; research-grade reporting per bioelectrochemistry literature.",
        ],
        "citations": [CIT_DOE_BIO, CIT_NREL],
        "sig_lens": (
            "Signature re-engineering: a Signature research program - not "
            "a plant - that attacks the rate problem with 3D-printed "
            "high-surface-area cathodes and a Signature strain-selection "
            "pipeline screening wild acetogens for current density before "
            "any genetic work. The Signature reporting protocol publishes "
            "full electron balances (coulombic efficiency to each product) "
            "so rate claims are checkable, and the Signature milestone "
            "plan kills the program honestly if rates miss targets."
        ),
    },
    {
        "key": "solar_thermochemical",
        "name": "Solar Thermochemical Fuels",
        "group": "Advanced Conversion Concepts",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "description": (
            "Solar thermochemical fuel plants concentrate sunlight to "
            "1,500 C and beyond, driving metal-oxide redox cycles that "
            "split water and CO2 into syngas - fuel from sunlight, heat, "
            "and air, with no electricity intermediate. Ceria (cerium "
            "oxide) cycles between oxidized and reduced states: the hot "
            "reduction step releases oxygen, the cooler oxidation step "
            "strips oxygen from H2O and CO2, yielding hydrogen and carbon "
            "monoxide for Fischer-Tropsch or methanol synthesis. "
            "Demonstration reactors have produced syngas on sun, and "
            "pilot plants aim at solar kerosene. Status: TRL 5-6. Honest "
            "framing: the physics is beautiful and demonstrated, but "
            "efficiency (single-digit percentages sun-to-fuel so far), "
            "materials surviving thousands of thermal cycles, and the sheer "
            "mirror field required keep it a long-horizon pathway."
        ),
        "how_it_works": (
            "Heliostats focus sunlight into a cavity receiver containing "
            "cerium oxide structures. Reduction: CeO2 -> CeO2-x + x/2 O2 "
            "at ~1,500 C. Oxidation: the reduced ceria reacts with steam "
            "and CO2 at ~800-1,000 C, CeO2-x + x H2O -> CeO2 + x H2 "
            "(and analogously for CO2 -> CO). The mixed H2/CO syngas feeds "
            "conventional fuel synthesis. The cycle's elegance is the "
            "separation: oxygen leaves in one step, fuel gases form in "
            "another, so no gas separation is needed. Efficiency losses "
            "come from re-radiation at 1,500 C, incomplete reduction, and "
            "sensible heating of the solid each cycle; reactor designs "
            "(rotating, particle, or membrane) all fight these three."
        ),
        "key_points": [
            "Concentrated sunlight (>1,500 C) drives ceria redox cycles splitting H2O and CO2 - no electricity step.",
            "Two-step cycle separates O2 release from fuel-gas formation - no gas separation needed.",
            "Demonstrated: solar syngas produced on-sun; pilot plants target solar kerosene.",
            "Sun-to-fuel efficiency in single digits so far; thermal cycling of materials is the durability front.",
            "Mirror-field scale required is enormous - a land-area reality check applies.",
            "Status: TRL 5-6 - beautiful demonstrated physics; long-horizon pathway.",
        ],
        "requirements": [
            "High-DNI solar site and heliostat field.",
            "Redox reactor (ceria structures) with gas handling for both steps.",
            "Fuel synthesis unit (FT or methanol) for the syngas.",
            "Materials qualified for thousands of 800-1,500 C cycles.",
        ],
        "standards": [
            "Fuel products to ASTM D7566 / D975 as applicable.",
            "Concentrated-solar safety practice for the heliostat field.",
        ],
        "citations": [CIT_IEA_ETP, CIT_DOE_BIO],
        "sig_lens": (
            "Signature re-engineering: a Signature solar-thermochemical "
            "design that pairs the redox reactor with thermal storage in "
            "the ceria bed itself, smoothing cloud transients without "
            "stopping the cycle. The Signature materials program tests "
            "redox structures to 10,000 measured cycles before scale-up "
            "claims, and the Signature site analysis sizes the mirror "
            "field from measured DNI data with honest sun-to-fuel "
            "efficiency - publishing the land-area-per-litre number "
            "upfront."
        ),
    },
    {
        "key": "artificial_photosynthesis",
        "name": "Artificial Photosynthesis Fuel Systems",
        "group": "Advanced Conversion Concepts",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "description": (
            "Artificial photosynthesis integrates light capture and fuel-"
            "forming catalysis into a single device - a photoelectrochemical "
            "cell that turns sunlight, water, and CO2 directly into fuels "
            "like hydrogen, carbon monoxide, formate, or methanol, the way "
            "a leaf makes sugar. Laboratory devices have demonstrated each "
            "half of the trick and some full devices; solar-to-fuel "
            "efficiencies above 10 percent have been reported for hydrogen, "
            "lower for carbon fuels. Status: TRL 3-4, firmly research. The "
            "honest challenges: catalysts that are simultaneously active, "
            "selective, stable for years outdoors, and made of abundant "
            "materials do not yet exist in one device; and every "
            "demonstration runs on pure feeds, not air and river water. "
            "This record closes the database at the frontier - the fuel "
            "concept furthest from market, included because the research "
            "direction matters."
        ),
        "how_it_works": (
            "A photoelectrochemical device couples a light absorber "
            "(semiconductor junction) to electrocatalysts: photons create "
            "electron-hole pairs, holes oxidize water to oxygen at the "
            "anode, electrons reduce water to hydrogen or CO2 to carbon "
            "products at the cathode. Photocatalyst-particle suspensions "
            "(photocatalytic sheets) are the simpler variant: powder in "
            "water under sunlight evolves fuel gases without wires. CO2 "
            "reduction selectivity is the hard catalysis problem - copper "
            "catalysts make a soup of products (CO, formate, ethylene, "
            "ethanol) and separating them costs more than the fuel is "
            "worth. Device architectures under test range from wired PV-"
            "plus-electrolyzer hybrids (really just solar electrolysis) to "
            "true integrated photoelectrodes."
        ),
        "key_points": [
            "Single device turns sunlight + water + CO2 into fuel - the leaf as engineering goal.",
            "Lab solar-to-hydrogen above 10 percent reported; carbon fuels lower and less selective.",
            "CO2-reduction selectivity is the hard problem - copper makes product soups.",
            "No device yet combines activity, selectivity, years-long stability, and abundant materials.",
            "Demonstrations use pure feeds; air and natural water remain unproven inputs.",
            "Status: TRL 3-4 - research frontier; closes this database at the far edge of emerging.",
        ],
        "requirements": [
            "Research laboratory with photoelectrochemistry capability.",
            "Abundant-material catalyst development program.",
            "Long-duration outdoor stability testing protocol.",
            "Full product analysis - every carbon product quantified, not just the headline fuel.",
        ],
        "standards": [
            "No product standards apply; solar-to-fuel efficiency reporting per peer-reviewed protocols.",
        ],
        "citations": [CIT_DOE_BIO, CIT_IEA_ETP],
        "sig_lens": (
            "Signature re-engineering: a Signature research roadmap - not "
            "a device claim - that sequences the problem honestly: first "
            "a stable water-splitting photoelectrode on abundant materials "
            "with a 5-year outdoor target, then CO2 reduction as a second "
            "program only after the first ships data. The Signature "
            "reporting rule requires every carbon product quantified and "
            "the full device energy balance published, so selectivity "
            "soups cannot hide behind a headline efficiency."
        ),
    },
]
