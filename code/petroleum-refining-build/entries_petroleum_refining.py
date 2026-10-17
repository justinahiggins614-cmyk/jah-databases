#!/usr/bin/env python3
"""Entries for the Petroleum Refining field databases (field #22, taxonomy order).

Verified 2026-10-17: NO database covers petroleum refining as a discipline.
- Manifest-wide regex search (petroleum.?refin|refiner|crude.?distill|
  catalytic.?crack|hydrocrack|reforming|alkylation|isomeri|delayed.?cok|
  hydrotreat|desulfuri|naphtha|asphalt|base.?oil|octane|reformate|FCC):
  only career-profile databases ('petroleum-engineers', 4 records;
  'public-petroleum-engineers', 5 records) and rock-science 'petrology'
  (36 records) - zero discipline-level refining coverage. 'energy',
  'energy-systems', 'energy-basics', 'everything-energy' are general-energy
  and contain no refining-unit records. 'biofuels-*' cover biofuels, not
  petroleum refining.
- Fields #11-21 shard indexes (volcanology, climatology,
  atmospheric-science, hydrology, meteorology, calculus, combinatorics,
  econometrics, psychometrics, turbomachinery, electromagnetics):
  direct whole-shard title scans for petrol|refin|crude|distill|crack|
  reformer|alkylation|isomeriz|coking|hydrotreat|desulfur|asphalt|
  lubricant|petrochem|gasoline|diesel|jet.?fuel|octane|kerosene|naphtha|
  fuel.?oil|lpg|propane = zero hits.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main repo
  rebuilt 2026-10-17 08:04 UTC, covering fields through #10; fields #11-21
  cross-checked directly above): every record checked + admitted at build
  time.

So this build creates two NEW databases, 32 ladder-ordered records each:

  petroleum-refining             - The Petroleum Refining Database
                                   (public-harvest: real, fact-checked
                                   refining; citations Speight, Gary/
                                   Handwerk/Kaiser, Fahim, Meyers, Riazi,
                                   Ancheyta, Sadeghbeigi, Robinson/Hsu,
                                   API Technical Data Book, ASTM methods,
                                   OSHA PSM, EPA NSPS)
  petroleum-refining-signature   - The Petroleum Refining Signature Database
                                   (his original Signature interpretation of
                                   the discipline; src signature, titles
                                   suffixed " (Signature Edition)", never
                                   presented as authentic public record)

Subtitle disambiguation (fields #13-22 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "Atmospheric
Distillation: The Crude Distillation Unit" and "Alkylation: The Finest
Gasoline Molecule".
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "petroleum refining, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_SPEIGHT = ("Speight, James G. 'The Chemistry and Technology of Petroleum', "
             "5th ed. CRC Press, 2014.")
C_GARY = ("Gary, James H., Handwerk, Glenn E., and Kaiser, Mark J. "
          "'Petroleum Refining: Technology and Economics', 5th ed. "
          "CRC Press, 2007.")
C_FAHIM = ("Fahim, Mohamed A., Al-Sahhaf, Tahir A., and Elkilani, Amal S. "
           "'Fundamentals of Petroleum Refining'. Elsevier, 2010.")
C_MEYERS = ("Meyers, Robert A., ed. 'Handbook of Petroleum Refining "
            "Processes', 4th ed. McGraw-Hill, 2016.")
C_RIAZI = ("Riazi, M. R. 'Characterization and Properties of Petroleum "
           "Fractions'. ASTM International, 2005.")
C_ANCHEYTA = ("Ancheyta, Jorge. 'Modeling and Simulation of Catalytic "
              "Reactors for Petroleum Refining'. Wiley, 2011.")
C_SADEGHBEIGI = ("Sadeghbeigi, Reza. 'Fluid Catalytic Cracking Handbook', "
                 "4th ed. Butterworth-Heinemann, 2020.")
C_ROBINSON = ("Robinson, Paul R. and Hsu, Chang S., eds. 'Springer Handbook "
              "of Petroleum Technology'. Springer, 2017.")
C_API_TDB = ("American Petroleum Institute. 'API Technical Data Book - "
             "Petroleum Refining', 6th ed. API, 1997 with updates.")
C_ASTM = ("ASTM International. Petroleum test methods: D86 distillation, "
          "D287/D4052 density, D445 viscosity, D4294/D5453 sulfur, D4814 "
          "gasoline, D975 diesel, D1655 jet fuel.")
C_OSHA_PSM = ("OSHA. 29 CFR 1910.119, Process Safety Management of Highly "
              "Hazardous Chemicals; API RP 750/14C heritage.")
C_EPA_NSPS = ("U.S. EPA. 40 CFR 60 Subpart Ja - New Source Performance "
              "Standards for Petroleum Refineries; NESHAP Subpart CC.")

ENTRIES = [
    {
        "key": "what_is_refining",
        "name": "What Petroleum Refining Is: From Black Crude to Clear Products",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Petroleum refining is the industrial art and science of "
            "separating crude oil into useful products and reshaping its "
            "molecules into the fuels and materials the world runs on. A "
            "barrel of crude oil is a chaotic mixture of thousands of "
            "hydrocarbon molecules - from light gases to asphalt - and it "
            "is nearly useless in that form. The refinery's job is "
            "threefold: separate (distillation splits crude by boiling "
            "point into naphtha, kerosene, diesel, and resid), convert "
            "(cracking, coking, reforming, and alkylation break big, "
            "low-value molecules into small, high-value ones and rebuild "
            "them into high-octane gasoline), and treat (hydrotreating "
            "strips out sulfur, nitrogen, and metals so products burn "
            "cleanly and meet law). A modern full-conversion refinery turns "
            "a barrel of heavy, sulfurous crude into gasoline, diesel, jet "
            "fuel, liquefied petroleum gas, lubricants, asphalt, and "
            "petrochemical feedstocks - often more than a barrel of product "
            "per barrel of crude, because hydrogen addition and density "
            "changes create processing gain. Refining is one of the "
            "largest, most capital-intensive manufacturing industries on "
            "earth: a single complex refinery processes hundreds of "
            "thousands of barrels per day through dozens of interacting "
            "process units, balanced like an orchestra."
        ),
        "how_it_works": (
            "Crude oil arrives by pipeline or tanker and first passes "
            "through desalting, where wash water and an electric field "
            "strip out salt that would corrode downstream equipment. The "
            "desalted crude is heated and fed to the atmospheric crude "
            "distillation unit, the refinery's front door, which separates "
            "it into straight-run fractions by boiling point. The heavy "
            "bottom, atmospheric resid, goes to vacuum distillation for a "
            "second separation under reduced pressure. Distillation alone "
            "cannot satisfy the market - it makes too much heavy fuel oil "
            "and not enough gasoline - so conversion units reshape the "
            "molecules: fluid catalytic cracking and hydrocracking break "
            "heavy gas oils into gasoline and diesel; delayed coking cooks "
            "the residuum into lighter liquids plus solid petroleum coke; "
            "catalytic reforming turns low-octane naphtha into high-octane "
            "reformate plus hydrogen; alkylation and isomerization build "
            "premium gasoline components. Hydrotreaters then remove sulfur "
            "and nitrogen from nearly every stream, and the blending system "
            "mixes components to exact product specifications before "
            "shipment."
        ),
        "key_points": [
            "Refining has three jobs: separate (distillation), convert (cracking, reforming, coking, alkylation), and treat (hydrotreating, sweetening).",
            "Distillation alone makes the wrong product slate - too much heavy fuel oil, too little gasoline - so conversion units reshape molecules to match demand.",
            "A complex refinery can yield more than one barrel of product per barrel of crude (processing gain) through hydrogen addition and molecular rearrangement.",
            "Every refinery is a mass- and energy-balanced network: hydrogen, fuel gas, steam, and heat flow between units as deliberately as the oil does.",
            "Refining economics are driven by the crack spread - the price difference between crude oil and refined products - and by refinery complexity.",
        ],
        "requirements": [
            "Crude oil composition (the hydrocarbon family record).",
            "The crude assay (what each barrel actually contains).",
            "Basic mass-balance thinking (in = out, plus hydrogen).",
        ],
        "standards": [
            "API Technical Data Book conventions for refinery calculations.",
            "ASTM D86/D287/D4052 for distillation and density measurement.",
        ],
        "citations": [C_SPEIGHT, C_GARY, C_FAHIM],
        "sig_lens": (
            "Signature take: the refinery is the Signature alchemy engine - "
            "black chaos in, ordered civilization out. His framing treats "
            "every unit as a negotiation with the molecule: distillation "
            "asks politely by boiling point, cracking persuades with "
            "catalysts, and hydrotreating evicts the sulfur that would "
            "poison the party."
        ),
    },
    {
        "key": "crude_composition",
        "name": "Crude Oil Composition: The Hydrocarbon Family",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Crude oil is not one substance - it is a mixture of thousands "
            "of hydrocarbon molecules built from carbon and hydrogen, plus "
            "small amounts of sulfur, nitrogen, oxygen, and metals such as "
            "nickel and vanadium. The hydrocarbons fall into families. "
            "Paraffins (alkanes) are straight or branched chains - clean "
            "burning, high in natural gas and light crudes. Naphthenes "
            "(cycloalkanes) are ring structures - good reformer feed for "
            "making aromatics and hydrogen. Aromatics are ring molecules "
            "with alternating double bonds - high octane, but limited in "
            "products by regulation. Olefins (alkenes) are almost absent in "
            "crude itself but are created by cracking and are the reactive "
            "building blocks of alkylation and petrochemicals. Heteroatoms "
            "matter out of proportion to their amount: sulfur becomes "
            "corrosive compounds and air pollution, nitrogen poisons "
            "catalysts, and metals deposit on catalysts and destroy them. "
            "Crudes are classified by density (API gravity), sulfur content "
            "(sweet under about 0.5 percent, sour above), and character - "
            "paraffinic, naphthenic, aromatic, or mixed-base - which "
            "determines what the refinery can make from them."
        ),
        "how_it_works": (
            "Geologists and refiners characterize crude with a few "
            "powerful numbers. API gravity measures density relative to "
            "water: light crudes above 31.1 degrees API flow easily and "
            "yield more gasoline and diesel; heavy crudes below 22.3 need "
            "deep conversion. The UOP characterization factor K - the cube "
            "root of the mean average boiling point in Rankine divided by "
            "specific gravity - classifies chemical character: around 12.5 "
            "to 13.0 means paraffinic, 11.5 to 12.0 naphthenic, 10.5 to "
            "11.5 aromatic. Sulfur content decides the treating bill: a "
            "sour crude carries percent-level sulfur that every hydrotreater "
            "must remove. The true boiling point curve, measured in a "
            "laboratory distillation, reveals how much of each product cut "
            "the crude contains - the refiner's first look at value."
        ),
        "key_points": [
            "Crude oil is thousands of molecules in four hydrocarbon families: paraffins, naphthenes, aromatics, and (after cracking) olefins.",
            "Sulfur, nitrogen, oxygen, nickel, and vanadium are present in small amounts but dominate corrosion, pollution, and catalyst poisoning.",
            "API gravity classifies density (light > 31.1, heavy < 22.3); the UOP K factor classifies chemical character (paraffinic ~12.5-13, aromatic ~10.5-11.5).",
            "Sweet crudes (< 0.5% sulfur) cost less to refine; sour crudes demand heavy hydrotreating investment.",
            "The true boiling point curve is the crude's product-yield fingerprint.",
        ],
        "requirements": [
            "Basic chemistry: atoms, molecules, hydrocarbons.",
            "Density and boiling point concepts.",
            "The 'what is refining' record (why composition drives unit choice).",
        ],
        "standards": [
            "ASTM D287/D4052 for API gravity and density.",
            "ASTM D4294/D5453 for sulfur content.",
        ],
        "citations": [C_SPEIGHT, C_RIAZI, C_GARY],
        "sig_lens": (
            "Signature take: crude is a molecule crowd, and every crowd has "
            "a character. His framing reads the UOP K factor like a "
            "personality test - paraffinic crudes are the straight "
            "shooters, aromatics the intense ones - and designs the "
            "refinery to bring out each barrel's best self."
        ),
    },
    {
        "key": "crude_assay",
        "name": "Reading a Crude Assay: An Oil's DNA",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A crude assay is the complete laboratory fingerprint of a "
            "crude oil - the document a refiner reads before buying a "
            "single cargo. It reports the true boiling point distillation "
            "curve: exactly what fraction of the crude boils off at each "
            "temperature, which translates directly into yields of naphtha, "
            "kerosene, diesel, gas oil, and residuum. It gives whole-crude "
            "properties - API gravity, sulfur, nitrogen, pour point, metals "
            "(nickel and vanadium), salt content, and viscosity - and then "
            "repeats key properties cut by cut: the sulfur and nitrogen in "
            "each fraction, the octane of the naphtha, the smoke point of "
            "the kerosene, the cetane of the diesel, the Conradson carbon "
            "of the residuum. With an assay, the refiner's linear-program "
            "planning model can predict what a refinery will make from that "
            "crude, what it will cost to treat, and what it is worth - "
            "before the ship docks. Assays are why two crudes at the same "
            "price can have very different value: a light sweet assay "
            "promises easy, high-value barrels; a heavy sour assay promises "
            "work, but at a discount."
        ),
        "how_it_works": (
            "The laboratory performs a standardized true boiling point "
            "distillation (ASTM D2892 at atmospheric pressure, then D5236 "
            "under vacuum for the heavy end) and records cumulative volume "
            "percent distilled against temperature. Interpolating between "
            "cut points gives fraction yields: everything boiling below "
            "about 190 degrees Fahrenheit is light naphtha, 190 to 380 "
            "heavy naphtha, 380 to 520 kerosene, 520 to 650 diesel, and so "
            "on - the exact cut points are the refiner's choice. Each "
            "narrow cut is analyzed for density, sulfur, nitrogen, and "
            "relevant quality tests. Planners load the assay into the "
            "refinery planning model, which simulates every unit and "
            "computes product yields, hydrogen consumption, utility loads, "
            "and profit. A refinery typically keeps assays for dozens of "
            "candidate crudes and re-optimizes its crude slate monthly or "
            "weekly as prices move."
        ),
        "key_points": [
            "A crude assay combines the true boiling point curve with cut-by-cut properties: sulfur, nitrogen, metals, octane, cetane, carbon residue.",
            "Interpolating the TBP curve between cut points predicts straight-run yields of every product fraction.",
            "Assays feed the refinery planning model, which values each crude before purchase.",
            "Two crudes at the same market price can differ sharply in refinery value - the assay reveals the difference.",
            "Heavy sour assays trade at discounts because they demand conversion and treating capacity.",
        ],
        "requirements": [
            "Crude composition (hydrocarbon families and heteroatoms).",
            "Distillation basics (boiling point separation).",
            "Interpolation and mass-balance arithmetic.",
        ],
        "standards": [
            "ASTM D2892/D5236 for true boiling point distillation.",
            "ASTM D86 for product distillation curves.",
        ],
        "citations": [C_RIAZI, C_GARY, C_ROBINSON],
        "sig_lens": (
            "Signature take: the assay is the barrel's resume - every "
            "number a claim about what it can do. His framing treats crude "
            "selection like hiring: read the assay, check the references "
            "(sulfur, metals, carbon residue), and never buy on price "
            "alone."
        ),
    },
    {
        "key": "api_gravity_properties",
        "name": "API Gravity, Density, and Viscosity: The First Measurements",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Before a refiner knows anything fancy about a crude, three "
            "numbers tell most of the story: API gravity, density, and "
            "viscosity. API gravity is the petroleum industry's density "
            "scale, defined so that water is 10 degrees API and lighter "
            "oils read higher: API = 141.5 / specific gravity - 131.5. A "
            "light crude at 38 degrees API has a specific gravity near "
            "0.83; a heavy crude at 15 degrees API sits near 0.97, barely "
            "floating on water. Density converts the traded unit - the "
            "42-gallon barrel, a volume - into mass, which is what "
            "equipment, catalysts, and chemistry actually handle. Viscosity "
            "measures resistance to flow and decides whether a stream can "
            "be pumped, atomized in a burner, or poured at winter "
            "temperatures; it falls steeply as temperature rises, which is "
            "why heavy fuel oils are heated for handling. Together with "
            "pour point - the temperature below which the oil stops flowing "
            "- these first measurements classify the crude, size the "
            "pumps, and set the heating bill before a single molecule is "
            "separated."
        ),
        "how_it_works": (
            "Density is measured by hydrometer, digital density meter, or "
            "pycnometer and converted to API gravity by the defining "
            "formula; specific gravity is density relative to water at 60 "
            "degrees Fahrenheit. Kinematic viscosity is measured in a "
            "calibrated capillary viscometer (ASTM D445): the oil flows "
            "through a thin tube and the efflux time converts to "
            "centistokes. Because viscosity changes with temperature, "
            "grades are specified at reference temperatures - 40 and 100 "
            "degrees Celsius for lubricants, 50 or 100 for fuel oils - and "
            "the viscosity index (ASTM D2270) scores how little the "
            "viscosity changes with temperature. The Walther equation, "
            "log(log(nu + 0.7)) = A - B log(T), linearizes the "
            "temperature dependence so two measurements predict viscosity "
            "at any temperature. Pour point (ASTM D97) is found by cooling "
            "the oil until it just stops pouring - waxy crudes can have "
            "pour points above room temperature."
        ),
        "key_points": [
            "API gravity = 141.5/SG - 131.5; light crudes read above 31.1, heavy crudes below 22.3 degrees API.",
            "Density turns traded volume (barrels) into handled mass (kilograms) for equipment and catalyst sizing.",
            "Viscosity is measured in capillary viscometers (ASTM D445) and falls steeply with temperature.",
            "The viscosity index scores temperature stability of viscosity; the Walther equation predicts viscosity at any temperature from two points.",
            "Pour point marks where waxy oils stop flowing - a handling and specification limit.",
        ],
        "requirements": [
            "Density, specific gravity, and unit conversions.",
            "Logarithms (for the Walther equation).",
            "The crude composition record (why paraffinic vs aromatic matters for viscosity).",
        ],
        "standards": [
            "ASTM D287/D4052 density and API gravity; ASTM D445 kinematic viscosity.",
            "ASTM D2270 viscosity index; ASTM D97 pour point.",
        ],
        "citations": [C_RIAZI, C_ASTM, C_FAHIM],
        "sig_lens": (
            "Signature take: three numbers and the barrel introduces "
            "itself - how heavy, how thick, how stubborn in winter. His "
            "framing treats API gravity as the crude's handshake: firm and "
            "light means easy business; heavy and viscous means the "
            "refinery earns its margin."
        ),
    },
    {
        "key": "refinery_flow",
        "name": "The Modern Refinery: Units, Flow, and Block Diagrams",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A modern refinery is a network of process units connected by "
            "pipes, and its block flow diagram is the map every refiner "
            "learns to read. Crude enters the crude distillation unit and "
            "leaves as gases, naphtha, kerosene, diesel, atmospheric gas "
            "oil, and residuum. The vacuum unit takes the residuum and "
            "pulls out vacuum gas oil, leaving vacuum resid. Conversion "
            "units then upgrade the heavy streams: the fluid catalytic "
            "cracker turns gas oils into gasoline and light olefins, the "
            "hydrocracker makes premium diesel and jet from heavier feeds "
            "with hydrogen, the delayed coker destroys the residuum into "
            "lighter liquids and solid coke, the catalytic reformer turns "
            "naphtha into high-octane reformate and hydrogen, and "
            "alkylation plus isomerization build elite gasoline "
            "components. Treating units - hydrotreaters, amine units, "
            "sulfur recovery, sour water strippers - clean every stream. "
            "The refinery's complexity is measured by the Nelson complexity "
            "index, which weights each unit's cost relative to crude "
            "distillation: a simple topping refinery scores near 2, a "
            "deep-conversion refinery above 10. Complexity buys the ability "
            "to profit from cheap heavy sour crudes."
        ),
        "how_it_works": (
            "Oil flows downhill in boiling point through the separation "
            "train, then sideways through conversion: heavy molecules are "
            "broken into light ones that rejoin the product streams. "
            "Hydrogen flows the other way in value - produced by the "
            "reformer and dedicated hydrogen plants, consumed by "
            "hydrocrackers and hydrotreaters - and the hydrogen balance is "
            "one of the refinery's master constraints. Fuel gas made in the "
            "units fires the furnaces; steam raised in waste-heat boilers "
            "drives turbines and reboilers. The block diagram is "
            "quantified in the planning model: each unit has yields, "
            "utilities, and constraints, and a linear program picks crude "
            "slates and unit severities to maximize margin. Reading the "
            "diagram means tracing three networks at once - oil, hydrogen, "
            "and energy - because a bottleneck in any one idles the others."
        ),
        "key_points": [
            "The refinery is three networks at once: oil flow, hydrogen flow, and energy/utility flow.",
            "Separation units split by boiling point; conversion units reshape molecules; treating units remove contaminants.",
            "The Nelson complexity index scores a refinery's upgrading power: ~2 for topping, 10+ for deep conversion.",
            "Hydrogen balance is a master constraint - reformers and hydrogen plants feed hydrocrackers and hydrotreaters.",
            "The planning model (linear program) optimizes crude slate and unit operation for maximum margin.",
        ],
        "requirements": [
            "The 'what is refining' record (separate/convert/treat).",
            "Mass balances (in = out).",
            "Basic economics: margins and constraints.",
        ],
        "standards": [
            "Nelson complexity index conventions (Oil & Gas Journal).",
            "API RP 14C / process flow diagram symbology (ISA 5.1).",
        ],
        "citations": [C_GARY, C_FAHIM, C_ROBINSON],
        "sig_lens": (
            "Signature take: the block diagram is the refinery's sheet "
            "music - dozens of units playing oil, hydrogen, and heat in "
            "time. His framing treats the planner as the conductor: one "
            "wrong note in the hydrogen balance and the whole orchestra "
            "goes quiet."
        ),
    },
    {
        "key": "desalting",
        "name": "Crude Desalting: The First Line of Defense",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Crude oil arrives carrying dissolved and suspended salt - "
            "mostly sodium, calcium, and magnesium chlorides from formation "
            "water - and the desalter's job is to wash it out before it can "
            "do harm. Salt seems harmless until heat turns it dangerous: "
            "in the crude preheat train and furnace, magnesium and calcium "
            "chlorides hydrolyze into hydrogen chloride, which condenses "
            "with water in the tower overhead system as hydrochloric acid "
            "and eats carbon steel. Sodium chloride deposits foul heat "
            "exchangers and furnace tubes, insulating them until tubes "
            "overheat and fail. The desalter mixes the crude with wash "
            "water, forms an emulsion, then breaks it with heat, "
            "demulsifier chemicals, and a high-voltage electric field that "
            "makes water droplets coalesce and settle. A single-stage "
            "desalter removes 90 to 95 percent of salt; two stages in "
            "series reach 99 percent, taking 20 pounds of salt per thousand "
            "barrels down to a fraction of a pound. It is the cheapest "
            "corrosion insurance in the refinery."
        ),
        "how_it_works": (
            "Wash water - 4 to 6 percent of crude volume - is mixed into "
            "the crude through a mixing valve that creates fine droplets "
            "with large surface area to dissolve the salt. The emulsion "
            "enters a horizontal vessel where electrodes impose an "
            "alternating electric field of 10,000 to 30,000 volts: water "
            "droplets, being polar, stretch, collide, and coalesce into "
            "drops heavy enough to settle. Demulsifier chemicals, dosed in "
            "parts per million, weaken the oil-water interface film so "
            "coalescence wins over stability. Heated to 200 to 300 degrees "
            "Fahrenheit, the lower viscosity speeds settling. The salty "
            "brine leaves the bottom for wastewater treatment while "
            "desalted crude leaves the top for the preheat train. Operators "
            "watch the interface level, the brine salt content, and the "
            "crude outlet salt - typically specified below 1 pound per "
            "thousand barrels - and adjust water rate, chemical dose, and "
            "voltage to hold it."
        ),
        "key_points": [
            "Salt hydrolyzes to hydrochloric acid in hot equipment and deposits foul exchangers and furnaces - desalting is corrosion prevention.",
            "Wash water dissolves salt; heat, demulsifier, and a high-voltage field coalesce and settle the brine out.",
            "Two-stage desalting reaches ~99% salt removal, typically to below 1 PTB (pound per thousand barrels).",
            "Key controls: wash-water rate, mixing intensity, demulsifier dose, temperature, voltage, interface level.",
            "The effluent brine goes to wastewater treatment - desalting trades corrosion for a water-treatment load.",
        ],
        "requirements": [
            "Emulsions and coalescence concepts.",
            "Basic electrostatics (why the field coalesces water drops).",
            "Corrosion basics (why chloride is feared).",
        ],
        "standards": [
            "ASTM D3230 for salt in crude (electrometric).",
            "Typical refinery spec: desalted crude < 1.0 PTB salt, < 0.1% water.",
        ],
        "citations": [C_SPEIGHT, C_MEYERS, C_FAHIM],
        "sig_lens": (
            "Signature take: the desalter is the bouncer at the refinery's "
            "front door - salt doesn't get past the velvet rope. His "
            "framing loves the elegance: thirty thousand volts doing the "
            "delicate work of convincing water droplets to hold hands and "
            "leave."
        ),
    },
    {
        "key": "atmospheric_distillation",
        "name": "Atmospheric Distillation: The Crude Distillation Unit",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The crude distillation unit, the CDU, is the refinery's front "
            "door: every barrel passes through it, and every downstream "
            "unit lives on what it produces. Desalted crude is heated to "
            "about 650 to 700 degrees Fahrenheit in a fired furnace and "
            "flashed into a tall fractionating tower with 30 to 50 trays. "
            "Vapor rises, liquid reflux falls, and at each tray the two "
            "phases exchange heat and mass until each tray holds a "
            "temperature where only molecules boiling near that point "
            "remain. Side streams are drawn at increasing depths: light "
            "naphtha near the top, heavy naphtha, kerosene, diesel, and "
            "atmospheric gas oil lower down, with atmospheric residuum - "
            "everything too heavy to vaporize at atmospheric pressure - "
            "leaving the bottom. A preflash tower often removes the "
            "lightest ends first to unload the main tower. Side strippers "
            "use steam to strip light components from each draw, sharpening "
            "the cut. The CDU sets the refinery's capacity - '100,000 "
            "barrels per day' means the CDU's crude charge rate - and its "
            "fractionation quality echoes through every product made "
            "downstream."
        ),
        "how_it_works": (
            "Separation works on vapor-liquid equilibrium: at a given "
            "temperature and pressure, lighter molecules prefer the vapor "
            "and heavier ones the liquid. Each tray is a miniature "
            "equilibrium stage - vapor bubbles through liquid, the phases "
            "approach equilibrium, and the vapor leaving is slightly "
            "lighter than the vapor entering. Stack 40 such stages and "
            "slight becomes decisive: the top is light, the bottom heavy, "
            "with a smooth temperature gradient between. Reflux - cooled "
            "liquid returned to the top - provides the downflowing liquid "
            "that washes heavies out of the rising vapor; pump-around "
            "circuits withdraw liquid mid-tower, cool it against incoming "
            "crude (recovering heat), and return it, flattening the "
            "temperature profile and saving furnace fuel. Steam stripping "
            "in the side strippers lowers the hydrocarbon partial pressure "
            "so light ends vaporize out of the product draws. Operators "
            "control cut points by adjusting draw rates, reflux, and tower "
            "temperatures against laboratory distillation tests."
        ),
        "key_points": [
            "The CDU fractionates crude by boiling point into gases, naphtha, kerosene, diesel, gas oil, and residuum using 30-50 equilibrium trays.",
            "Each tray is a vapor-liquid equilibrium stage; stacked stages turn slight volatility differences into sharp separations.",
            "Reflux and pump-around circuits provide internal liquid flow, sharpen cuts, and recover heat into incoming crude.",
            "Side strippers use steam to strip light ends from product draws, sharpening fractionation.",
            "CDU charge rate defines refinery capacity; its cut quality propagates to every downstream unit.",
        ],
        "requirements": [
            "Vapor-liquid equilibrium and boiling point.",
            "The crude assay record (what the cuts should be).",
            "Heat exchangers (why pump-around heat recovery matters).",
        ],
        "standards": [
            "ASTM D86 for product distillation quality control.",
            "API 650 for storage; column design per standard fractionation practice.",
        ],
        "citations": [C_GARY, C_FAHIM, C_MEYERS],
        "sig_lens": (
            "Signature take: the CDU is the refinery's sorting hat - forty "
            "trays of rising vapor, and every molecule finds its house. "
            "His framing admires the patience of it: no chemistry, no "
            "catalysts, just temperature, pressure, and equilibrium doing "
            "what they have always done."
        ),
    },
    {
        "key": "vacuum_distillation",
        "name": "Vacuum Distillation: The Second Cut",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Atmospheric residuum - the bottom of the crude tower - still "
            "holds 40 to 50 percent of many crudes' value, but it cannot be "
            "distilled at atmospheric pressure: heating it past about 700 "
            "degrees Fahrenheit cracks the molecules instead of vaporizing "
            "them. The vacuum distillation unit solves this by lowering the "
            "pressure to roughly 10 to 40 millimeters of mercury, about "
            "one-twentieth of atmospheric, which drops boiling points by "
            "hundreds of degrees so heavy gas oils vaporize intact at "
            "furnace outlet temperatures near 750 degrees. The tower draws "
            "light vacuum gas oil, heavy vacuum gas oil, and sometimes wax "
            "or lube distillates as side streams, leaving vacuum residuum - "
            "asphalt, fuel oil, or coker feed - at the bottom. Vacuum gas "
            "oil is the premium feed for the fluid catalytic cracker and "
            "hydrocracker; vacuum resid feeds the delayed coker or becomes "
            "asphalt. Steam ejectors or liquid-ring vacuum pumps hold the "
            "vacuum, and because the vapor volumes are enormous at low "
            "pressure, vacuum towers are the fattest vessels in the "
            "refinery - wide, short, and unmistakable."
        ),
        "how_it_works": (
            "Boiling point falls with pressure according to vapor-pressure "
            "thermodynamics: at 25 millimeters of mercury, a hydrocarbon "
            "that boils at 1000 degrees Fahrenheit at atmospheric pressure "
            "vaporizes near 700. The Maxwell-Bonnell correlation converts "
            "between atmospheric-equivalent and vacuum boiling temperatures "
            "for refinery calculations. Inside, the tower works like the "
            "atmospheric unit - trays or structured packing, wash oil, side "
            "draws - but with much larger diameter because vapor at low "
            "pressure occupies far more volume. Ejectors use high-pressure "
            "motive steam expanding through nozzles to entrain tower vapors "
            "in stages, each stage compressing to the next, holding the top "
            "at deep vacuum. Wash oil sprayed above the feed zone scrubs "
            "entrained resid droplets and metals out of the rising vapor "
            "so the gas oils stay clean for catalytic units. Cut points are "
            "controlled by tower pressure profile, wash rates, and draw "
            "temperatures, targeting residuum softening point for asphalt "
            "or Conradson carbon for coker feed."
        ),
        "key_points": [
            "Vacuum lowers boiling points hundreds of degrees, letting heavy gas oils vaporize without thermal cracking.",
            "Products: light and heavy vacuum gas oil (cracker feeds), lube distillates, and vacuum resid (asphalt, coker feed, fuel oil).",
            "Low-pressure vapor needs huge volume - vacuum towers are the refinery's widest vessels.",
            "Steam ejectors or vacuum pumps hold 10-40 mmHg; wash oil keeps metals and resid out of the gas oils.",
            "The Maxwell-Bonnell correlation translates between vacuum and atmospheric-equivalent temperatures.",
        ],
        "requirements": [
            "Atmospheric distillation (the first cut and its residuum).",
            "Vapor pressure vs temperature (Clausius-Clapeyron idea).",
            "Thermal cracking basics (why temperature must stay limited).",
        ],
        "standards": [
            "ASTM D5236 for vacuum true boiling point distillation.",
            "ASTM D189/D4530 Conradson/micro carbon residue for resid quality.",
        ],
        "citations": [C_GARY, C_SPEIGHT, C_RIAZI],
        "sig_lens": (
            "Signature take: the vacuum tower is the refinery's deep-sea "
            "diver - descending into pressure where heavy molecules can "
            "finally boil without burning. His framing treats vacuum as a "
            "time machine: it lets the refinery distill the ancient heavy "
            "end as gently as the light."
        ),
    },
]
ENTRIES += [
    {
        "key": "light_ends",
        "name": "Light Ends Recovery: LPG, Fuel Gas, and the Gas Plant",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The lightest molecules in the refinery - methane, ethane, "
            "propane, butanes, and light olefins - leave the crude tower "
            "as gases and are gathered from every unit into the gas plant, "
            "the refinery's light-ends recovery system. These streams are "
            "too valuable to burn indiscriminately: propane and butane "
            "become liquefied petroleum gas (LPG) for heating and cooking "
            "fuel; isobutane feeds the alkylation unit; propylene and "
            "butylenes feed alkylation and petrochemical plants; ethane "
            "goes to ethylene crackers; and the remaining methane and "
            "ethane become refinery fuel gas for the furnaces. The gas "
            "plant separates them in a train of fractionators - deethanizer, "
            "depropanizer, debutanizer, and often a deisobutanizer - each "
            "splitting one key pair by distillation under pressure, since "
            "these light hydrocarbons only liquefy under pressure at "
            "ordinary temperatures. Amine treaters upstream strip hydrogen "
            "sulfide so the products are sweet. Light-ends handling is also "
            "a safety discipline: LPG is stored under pressure in spheres "
            "and bullets, and its vapors are heavier than air, demanding "
            "rigorous leak prevention."
        ),
        "how_it_works": (
            "Wet gas from the crude unit, the FCC, the coker, and the "
            "reformer is compressed and fed to an absorber-stripper system "
            "that recovers C3 and heavier into a liquid while fuel gas "
            "(C1/C2) leaves the top. The debutanizer splits the stream into "
            "overhead LPG-range material and bottoms gasoline. The "
            "depropanizer then separates propane and propylene overhead "
            "from butanes bottoms; the deisobutanizer splits isobutane - "
            "the alkylation feed - from normal butane. Because relative "
            "volatilities are small between close boilers like propane and "
            "propylene, these towers run many trays (often 40 to 80) at "
            "elevated pressure with full reflux control. Product specs are "
            "tight: HD-5 propane for engine fuel limits propylene content, "
            "and alkylation-grade isobutane must be high purity. Unsaturated "
            "gas plants add sponge absorbers and extra fractionation to "
            "handle the olefin-rich FCC offgas separately from saturated "
            "streams."
        ),
        "key_points": [
            "The gas plant recovers C1-C4 streams from every unit and fractionates them into fuel gas, LPG, alkylation feed, and petrochemical feedstocks.",
            "Deethanizer, depropanizer, debutanizer, and deisobutanizer split light ends under pressure with high tray counts.",
            "Propane/butane become LPG; isobutane feeds alkylation; propylene and butylenes feed alkylation and petrochemicals.",
            "Amine treating sweetens the streams; tight specs (HD-5 propane, alkylation-grade isobutane) govern operation.",
            "LPG storage and handling is a pressure-safety discipline - vapors are heavier than air.",
        ],
        "requirements": [
            "Atmospheric distillation (where the light ends originate).",
            "Vapor-liquid equilibrium at elevated pressure.",
            "Alkylation and FCC records (the downstream consumers).",
        ],
        "standards": [
            "GPA 2140 / HD-5 specification for propane.",
            "ASME Section VIII for LPG pressure storage.",
        ],
        "citations": [C_GARY, C_MEYERS, C_FAHIM],
        "sig_lens": (
            "Signature take: the gas plant is the refinery's sorting office "
            "for its lightest mail - every molecule routed, none wasted. "
            "His framing admires the thrift: yesterday's fuel gas is "
            "today's alkylate, and the lightest barrel often earns the "
            "highest margin."
        ),
    },
    {
        "key": "thermal_cracking",
        "name": "Thermal Cracking and Visbreaking: Heat as a Hammer",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Long before catalysts, refiners learned that heat alone breaks "
            "big hydrocarbon molecules: thermal cracking. Heat a heavy "
            "molecule hot enough and its carbon-carbon bonds vibrate apart "
            "in a free-radical chain reaction, splitting one large molecule "
            "into smaller ones - gas, naphtha, and a heavier residue. "
            "Visbreaking, short for viscosity breaking, is thermal "
            "cracking's mild, modern form: vacuum resid is heated to about "
            "850 to 900 degrees Fahrenheit for a few minutes, just enough "
            "to crack the longest chains and slash the residuum's viscosity "
            "so it can be sold as fuel oil without expensive cutter stock. "
            "Conversion is deliberately limited - pushing further makes "
            "coke that fouls the heater tubes - so visbreaking is a "
            "viscosity play, not a gasoline play. Full thermal cracking "
            "still runs in some refineries as a simple, low-capital route "
            "to cracked naphtha and distillate, but catalytic processes "
            "have taken its premium roles. The kinetics are first-order "
            "Arrhenius: rate doubles roughly every 15 to 25 degrees "
            "Fahrenheit, which is why furnace temperature control is the "
            "whole game."
        ),
        "how_it_works": (
            "A hydrocarbon bond breaks homolytically - one electron to "
            "each fragment - creating two radicals. Radicals are hungry: "
            "each abstracts hydrogen or splits at the beta bond, making a "
            "smaller olefin plus a new radical, and the chain propagates "
            "until two radicals combine and terminate it. Because the "
            "chemistry is statistical, products follow a broad distribution "
            "rather than a selective one - the fundamental weakness of "
            "thermal cracking versus catalytic. In a visbreaker, residuum "
            "passes through a fired heater coil into a soaker drum that "
            "provides residence time at temperature, then is quenched to "
            "stop the reaction before coke forms. Severity - the "
            "temperature-time integral - is the control knob: too mild and "
            "viscosity barely moves, too severe and asphaltenes precipitate "
            "as coke, first fouling tubes, then plugging them. Operators "
            "watch fuel oil viscosity, stability (the cracked resid must "
            "not drop sludge in storage), and heater tube metal "
            "temperatures."
        ),
        "key_points": [
            "Thermal cracking splits molecules by heat through free-radical chain reactions - no catalyst, broad product distribution.",
            "Visbreaking mildly cracks vacuum resid to cut its viscosity for fuel oil blending, avoiding coke formation.",
            "First-order Arrhenius kinetics: rate roughly doubles every 15-25 F, making furnace temperature the control knob.",
            "Severity must stay below the coke-formation threshold - asphaltene precipitation fouls and plugs heater tubes.",
            "Catalytic cracking displaced thermal cracking for premium products because catalysts are selective where heat is statistical.",
        ],
        "requirements": [
            "Vacuum distillation (the residuum feed).",
            "Free radicals and Arrhenius kinetics.",
            "Fuel oil blending (the visbroken product's home).",
        ],
        "standards": [
            "ASTM D445 viscosity and D97 pour point for fuel oil products.",
            "API 530/530M for fired heater tube design.",
        ],
        "citations": [C_SPEIGHT, C_GARY, C_ANCHEYTA],
        "sig_lens": (
            "Signature take: visbreaking is the refinery's restraint - "
            "heating the residuum just enough to thin it, never enough to "
            "break it. His framing treats severity as a dare: flirt with "
            "the coke line for profit, but never cross it, because coke "
            "does not negotiate."
        ),
    },
    {
        "key": "fcc",
        "name": "Fluid Catalytic Cracking: The Beating Heart of the Refinery",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The fluid catalytic cracker, the FCC, is the most important "
            "conversion unit in most refineries - the beating heart that "
            "turns heavy, low-value gas oils into gasoline, light olefins, "
            "and diesel. Hot, powdered zeolite catalyst - particles finer "
            "than sand - meets vaporized heavy feed in a riser reactor, "
            "where carbenium-ion chemistry cracks big molecules in about "
            "two to four seconds at roughly 950 to 1000 degrees Fahrenheit. "
            "The cracked vapors go to a fractionator for separation while "
            "the coke-coated catalyst flows to a regenerator, where air "
            "burns the coke off at 1250 to 1400 degrees, reheating the "
            "catalyst for the next pass. The catalyst circulates "
            "continuously - tons per minute - fluidized like a liquid, "
            "which is where the 'fluid' in the name comes from. Conversion "
            "typically runs 70 to 85 percent, with gasoline selectivity "
            "near 50 weight percent of feed. The FCC is also the refinery's "
            "great olefin factory: its propylene and butylenes feed "
            "alkylation and petrochemical units. Heat balance governs "
            "everything - the regenerator must burn exactly enough coke to "
            "supply the riser's heat demand."
        ),
        "how_it_works": (
            "Zeolite Y catalyst provides strong acid sites inside "
            "molecular-sized cages. A heavy molecule adsorbs, forms a "
            "carbenium ion, and undergoes beta scission - splitting at the "
            "bond two atoms from the charge - producing a smaller olefin "
            "and a smaller ion; hydrogen transfer then saturates products "
            "into the high-octane branched paraffins and aromatics that "
            "make FCC gasoline valuable. The riser gives plug-flow contact "
            "for seconds; a stripper then steams entrained hydrocarbons "
            "off the catalyst before regeneration. In the regenerator, "
            "controlled air burns coke to CO and CO2 - full-combustion "
            "units add a CO boiler to recover the heat. The catalyst-to-oil "
            "ratio, typically 5 to 10 by weight, sets severity: more "
            "catalyst, more conversion, more coke, more regenerator heat. "
            "Fresh catalyst makeup replaces losses and metals-poisoned "
            "inventory; equilibrium catalyst activity is managed by "
            "addition rate. Main fractionator, gas plant, and light-ends "
            "systems separate the reactor effluent into fuel gas, LPG, "
            "gasoline, light cycle oil (diesel blending), heavy cycle oil "
            "(recycle or fuel), and slurry (coker feed or fuel)."
        ),
        "key_points": [
            "FCC cracks heavy gas oils over zeolite catalyst in a 2-4 second riser contact at ~950-1000 F, converting 70-85%.",
            "Carbenium-ion chemistry (beta scission + hydrogen transfer) makes selective, high-octane products unlike thermal cracking.",
            "Catalyst circulates continuously between reactor and regenerator, where coke burn-off reheats it - heat balance rules the unit.",
            "Products: fuel gas, LPG/olefins, high-octane gasoline, light cycle oil, heavy cycle oil, slurry, and coke (fuel).",
            "Catalyst-to-oil ratio sets severity; metals (Ni, V) from resid feeds poison the catalyst and make extra coke and hydrogen.",
        ],
        "requirements": [
            "Vacuum distillation (the gas oil feed).",
            "Catalysis basics: acid sites, adsorption, deactivation.",
            "The gas plant record (where FCC light ends go).",
        ],
        "standards": [
            "ASTM D5758 / catalyst testing conventions; E-cat equilibrium activity practice.",
            "API 941/934 for high-temperature hydrogen and materials guidance heritage.",
        ],
        "citations": [C_SADEGHBEIGI, C_MEYERS, C_ANCHEYTA],
        "sig_lens": (
            "Signature take: the FCC is controlled lightning - tons of "
            "catalyst raining through vapor, cracking molecules in seconds "
            "and resurrecting itself in fire. His framing sees the "
            "regenerator as the unit's heart muscle: burn the coke, pump "
            "the heat, keep the circulation alive."
        ),
    },
    {
        "key": "hydrocracking",
        "name": "Hydrocracking: Premium Barrels from Heavy Feed",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Hydrocracking is catalytic cracking under high-pressure "
            "hydrogen - the refinery's premium conversion route. Where the "
            "FCC rejects carbon as coke, the hydrocracker adds hydrogen, "
            "so nearly every feed molecule becomes liquid product: volume "
            "yields routinely exceed 100 percent, sometimes 115 to 120 "
            "percent, because hydrogen mass and density shifts add up. "
            "Operating at 1500 to 3000 psi and 650 to 800 degrees "
            "Fahrenheit over dual-function catalysts (acid cracking sites "
            "plus metal hydrogenation sites), it converts vacuum gas oil - "
            "even heavy, high-sulfur feeds the FCC cannot handle - into "
            "ultra-clean diesel, jet fuel, naphtha, and LPG with almost "
            "no sulfur, nitrogen, or aromatics. The products are the "
            "cleanest the refinery makes: hydrocracked diesel needs "
            "little further treating, and hydrocracker unconverted oil is "
            "the world's finest lube base-oil and ethylene-cracker feed. "
            "The price is hydrogen - 1000 to 2500 standard cubic feet per "
            "barrel of feed - and capital: hydrocrackers are thick-walled, "
            "high-pressure, expensive machines. Refineries run them hard "
            "when diesel margins are strong."
        ),
        "how_it_works": (
            "The catalyst pairs zeolite or amorphous silica-alumina acid "
            "sites, which crack carbon-carbon bonds via carbenium ions, "
            "with nickel-molybdenum or nickel-tungsten sulfide metals, "
            "which hydrogenate. Cracking makes olefins and smaller "
            "fragments; hydrogenation immediately saturates them before "
            "they can condense into coke - the chemical reason coke "
            "yields are near zero and catalyst life stretches for years. "
            "High hydrogen partial pressure also suppresses aromatics "
            "formation and strips sulfur and nitrogen as hydrogen sulfide "
            "and ammonia in the same vessel. Most units run two stages: "
            "the first does hydrotreating and partial conversion, the "
            "second finishes cracking over cleaner catalyst. Recycle of "
            "unconverted oil pushes overall conversion toward 100 percent "
            "for maximum diesel, or the unit runs once-through for lube "
            "base oil. Fractionation separates the effluent into light "
            "ends, naphtha, kerosene/jet, and diesel, with product slates "
            "tunable by temperature, pressure, and recycle rate."
        ),
        "key_points": [
            "Hydrocracking = catalytic cracking + high-pressure hydrogen: near-zero coke, 100%+ volume yields, ultra-clean products.",
            "Dual-function catalysts pair acid cracking sites with hydrogenation metals (Ni-Mo, Ni-W).",
            "Converts feeds too heavy or dirty for the FCC into premium diesel, jet, naphtha, and lube-quality unconverted oil.",
            "Hydrogen consumption (1000-2500 SCF/bbl) and high-pressure capital are the costs; diesel margins pay them.",
            "Two-stage designs with recycle tune the slate from maximum diesel to maximum jet or lube base oil.",
        ],
        "requirements": [
            "The FCC record (catalytic cracking without hydrogen).",
            "Hydrotreating (the sulfur/nitrogen removal chemistry).",
            "The hydrogen network record (where the H2 comes from).",
        ],
        "standards": [
            "ASTM D975 diesel and D1655 jet specifications for products.",
            "API 941 for high-pressure hydrogen service steels.",
        ],
        "citations": [C_MEYERS, C_ANCHEYTA, C_ROBINSON],
        "sig_lens": (
            "Signature take: hydrocracking is the refinery's generosity - "
            "instead of rejecting carbon as coke, it donates hydrogen and "
            "keeps every molecule. His framing treats the hydrogen bill as "
            "tuition: expensive, but it graduates the dirtiest feed into "
            "the cleanest barrel."
        ),
    },
    {
        "key": "catalytic_reforming",
        "name": "Catalytic Reforming: Octane and Hydrogen from Naphtha",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Catalytic reforming takes low-octane heavy straight-run "
            "naphtha - research octane around 50 - and rearranges its "
            "molecules into high-octane reformate near 95 to 100 RON plus "
            "a stream of byproduct hydrogen. It is the refinery's octane "
            "factory and, in many refineries, its largest hydrogen "
            "producer. Over platinum-rhenium or platinum-tin catalyst at "
            "850 to 1000 degrees Fahrenheit and 50 to 500 psi, four "
            "reactions run at once: naphthenes dehydrogenate to aromatics "
            "(fast, hydrogen-releasing, octane-creating), paraffins "
            "isomerize and dehydrocyclize more slowly, and hydrocracking "
            "trims the heavies while consuming hydrogen. Semi-regenerative "
            "units shut down periodically to burn coke off the catalyst; "
            "continuous-regeneration (CCR) units circulate catalyst to an "
            "external regenerator without stopping, running at lower "
            "pressure for higher aromatics yield and more hydrogen. "
            "Reformate's aromatics - benzene, toluene, xylenes - are "
            "gasoline gold but regulated: benzene in gasoline is capped "
            "near 0.62 volume percent in the United States, so modern "
            "reformers often fractionate or saturate benzene out."
        ),
        "how_it_works": (
            "The chemistry is a tug-of-war. Dehydrogenation of naphthenes "
            "(for example methylcyclohexane to toluene plus three "
            "hydrogen molecules) is strongly endothermic and favored by "
            "high temperature and low pressure - the reaction that makes "
            "both octane and hydrogen. Isomerization reshuffles paraffins "
            "into branched isomers with modest octane gain. "
            "Dehydrocyclization closes paraffin chains into aromatic rings "
            "slowly. Hydrocracking side-reactions consume hydrogen and "
            "make light gas - favored by high pressure, which is why low "
            "pressure raises hydrogen yield but also coking rate. The "
            "feed must be deeply hydrotreated first: sulfur, nitrogen, "
            "and metals poison the platinum, and even a few parts per "
            "million upset the unit. Three or four adiabatic reactors in "
            "series with interheaters manage the endothermic temperature "
            "drop - the first reactor does the fast naphthene conversion "
            "and cools sharply, the last does the slow paraffin chemistry. "
            "A stabilizer then separates reformate from hydrogen-rich "
            "recycle gas and LPG."
        ),
        "key_points": [
            "Reforming upgrades ~50 RON naphtha to 95-100 RON reformate while producing byproduct hydrogen.",
            "Naphthene dehydrogenation to aromatics is the key reaction: fast, endothermic, hydrogen-releasing.",
            "Low pressure favors aromatics and hydrogen but accelerates coking; CCR units regenerate catalyst continuously to run low-pressure.",
            "Feed must be ultra-clean (hydrotreated) - sulfur, nitrogen, and metals poison platinum catalysts.",
            "Benzene limits in gasoline constrain reformate use; benzene is extracted or saturated to meet regulations.",
        ],
        "requirements": [
            "Hydrotreating (why the feed must be clean).",
            "Octane and gasoline blending (where reformate goes).",
            "Chemical equilibrium: temperature and pressure effects.",
        ],
        "standards": [
            "ASTM D2699/D2700 for RON/MON octane measurement.",
            "EPA MSAT2 benzene limit (~0.62 vol%) in gasoline.",
        ],
        "citations": [C_MEYERS, C_GARY, C_ANCHEYTA],
        "sig_lens": (
            "Signature take: the reformer is the refinery's alchemist - "
            "straight chains in, aromatic rings out, hydrogen as the "
            "applause. His framing treats platinum as the talent scout: it "
            "finds the naphthene with star potential and introduces it to "
            "its aromatic destiny."
        ),
    },
    {
        "key": "alkylation",
        "name": "Alkylation: The Finest Gasoline Molecule",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Alkylation builds the finest gasoline molecule in the "
            "refinery: isobutane plus light olefins (propylene, butylenes, "
            "amylenes) combine under strong acid catalysis into branched "
            "C7-C9 paraffins - alkylate - with research octane of 94 to 98, "
            "near-zero sulfur, no aromatics, no olefins, and low vapor "
            "pressure. Refiners call it liquid gold, and it is the "
            "backbone of premium gasoline blending. The reaction runs at "
            "near-ambient temperatures in concentrated sulfuric acid "
            "(96-98 percent) or hydrofluoric acid, which protonates the "
            "olefin into a carbenium ion that attacks isobutane. The "
            "isobutane-to-olefin ratio, typically 8:1 or higher, suppresses "
            "olefin polymerization side reactions that would make heavy, "
            "low-octane polymers instead. Sulfuric acid units consume acid "
            "(around 10-20 pounds per barrel of alkylate) and regenerate "
            "it offsite; HF units regenerate acid internally but demand "
            "extreme safety discipline because hydrogen fluoride is "
            "acutely toxic. Solid-acid alkylation technologies are emerging "
            "to escape liquid acids entirely. Every alkylation unit lives "
            "on FCC olefins - the two units are economic partners."
        ),
        "how_it_works": (
            "In the reactor - a stirred contactor, Stratco-style, or "
            "cascade - olefin feed disperses into a circulating acid "
            "emulsion. The acid protonates the olefin to a carbenium ion; "
            "the ion abstracts a hydride from isobutane, forming the "
            "branched paraffin product and a new tert-butyl cation that "
            "continues the chain. High isobutane concentration keeps the "
            "chain propagating on isobutane rather than polymerizing "
            "olefins together. Refrigeration holds sulfuric-acid units "
            "near 40-50 degrees Fahrenheit for selectivity; HF units run "
            "warmer, near 70-100. A settler separates hydrocarbon product "
            "from acid by gravity; the hydrocarbon goes to fractionation "
            "(deisobutanizer recycles excess isobutane, debutanizer takes "
            "alkylate overhead), and spent sulfuric acid - diluted by "
            "reaction water and heavy polymers - goes to regeneration. "
            "Operators guard acid strength, the isobutane-to-olefin ratio, "
            "temperature, and feed contaminants (butadiene and water kill "
            "selectivity)."
        ),
        "key_points": [
            "Alkylation combines isobutane with light olefins under strong acid to make 94-98 RON alkylate: the premium gasoline component.",
            "Sulfuric acid (96-98%) or hydrofluoric acid catalyzes via carbenium ions at near-ambient temperature.",
            "Isobutane-to-olefin ratio ~8:1+ suppresses polymerization side reactions that destroy octane.",
            "HF alkylation demands extreme safety discipline (acutely toxic acid); solid-acid technologies aim to replace liquid acids.",
            "The unit's economy is chained to FCC olefin supply - alkylation and the cat cracker rise together.",
        ],
        "requirements": [
            "The FCC record (the olefin source).",
            "Carbenium-ion chemistry basics.",
            "Gasoline blending (where alkylate earns its premium).",
        ],
        "standards": [
            "ASTM D2699/D2700 octane; alkylate typically 94-98 RON, 90-94 MON.",
            "API RP 751 for HF alkylation safe practices.",
        ],
        "citations": [C_MEYERS, C_GARY, C_ROBINSON],
        "sig_lens": (
            "Signature take: alkylation is molecular matchmaking - "
            "introducing isobutane to olefins under acid supervision and "
            "getting perfect branched children. His framing calls alkylate "
            "the valedictorian molecule: top of the class in octane, "
            "manners (low RVP), and cleanliness."
        ),
    },
    {
        "key": "isomerization",
        "name": "Isomerization: Upgrading Light Straight-Run Naphtha",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Light straight-run naphtha - mostly normal pentane and normal "
            "hexane - has miserable octane: n-pentane rates about 62 RON, "
            "n-hexane about 25. Isomerization rearranges these straight "
            "chains into their branched isomers - isopentane at 93 RON, "
            "2,2-dimethylbutane near 94 - lifting the stream by 15 to 25 "
            "octane numbers with no yield loss and no hydrogen consumed "
            "in the ideal case. Over platinum on chlorided alumina or "
            "zeolite catalyst at 200 to 400 degrees Fahrenheit, the "
            "reaction approaches thermodynamic equilibrium, and because "
            "branching is favored at low temperature, the coolest "
            "operating catalysts give the highest octane. Chlorided-alumina "
            "units need continuous chloride injection and ultra-dry, "
            "sulfur-free feed; zeolite units tolerate more but run hotter "
            "with slightly lower equilibrium octane. Deisohexanizer "
            "fractionation can recycle the unconverted normal paraffins "
            "for a second pass, pushing the product toward the equilibrium "
            "limit. Isomerate is the clean light end of the gasoline pool: "
            "no aromatics, no olefins, low benzene, moderate vapor "
            "pressure - exactly what modern gasoline specifications reward."
        ),
        "how_it_works": (
            "On the acid sites, n-paraffin forms a carbenium ion that "
            "rearranges through protonated cyclopropane intermediates into "
            "the branched skeleton, then picks up hydrogen from the metal "
            "sites to desorb as isoparaffin - the classic dual-function "
            "mechanism. Hydrogen is co-fed at low partial pressure not as "
            "a reactant but to suppress coking and keep the metal sites "
            "clean. Equilibrium sets the ceiling: at lower temperature the "
            "branched isomers dominate more completely, which is why "
            "catalyst activity at low temperature is the technology race. "
            "Feed must be hydrotreated and dried - water and sulfur kill "
            "chlorided alumina, and even zeolites suffer. A stabilizer "
            "removes light ends; the deisohexanizer then splits high-octane "
            "branched C5/C6 overhead from low-octane normal paraffins "
            "bottoms, and the bottoms recycle to extinction. The product - "
            "isomerate near 83-93 RON depending on configuration - goes "
            "straight to gasoline blending."
        ),
        "key_points": [
            "Isomerization rearranges n-pentane/n-hexane (~62/25 RON) into branched isomers (~93 RON) with no yield loss.",
            "Dual-function catalysts (acid rearrangement + metal hydrogenation); low temperature favors branching equilibrium.",
            "Chlorided alumina gives the highest octane but needs ultra-dry, sulfur-free feed and chloride injection.",
            "Deisohexanizer recycle of normal paraffins pushes conversion toward the equilibrium limit.",
            "Isomerate is the clean light gasoline component: no aromatics, no olefins, low benzene.",
        ],
        "requirements": [
            "Chemical equilibrium and Le Chatelier's principle.",
            "Octane measurement (RON/MON).",
            "Hydrotreating (why feed must be clean and dry).",
        ],
        "standards": [
            "ASTM D2699/D2700 octane; typical isomerate 83-93 RON.",
            "EPA benzene and toxics limits shaping light-naphtha upgrading.",
        ],
        "citations": [C_MEYERS, C_ANCHEYTA, C_GARY],
        "sig_lens": (
            "Signature take: isomerization is the refinery's chiropractor - "
            "no molecules added or removed, just straightened spines into "
            "branches. His framing loves the free lunch: same atoms, "
            "twenty more octane numbers, courtesy of thermodynamics."
        ),
    },
    {
        "key": "delayed_coking",
        "name": "Delayed Coking: Cooking the Bottom of the Barrel",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Delayed coking is the refinery's last resort and its deepest "
            "conversion: vacuum residuum - the bottom of the bottom, rich "
            "in asphaltenes, metals, and Conradson carbon - is heated to "
            "about 900 to 950 degrees Fahrenheit and fed into giant coke "
            "drums, where it soaks for hours and thermally cracks into "
            "lighter liquids while the heaviest fraction condenses into "
            "solid petroleum coke. Nothing is wasted: the drum effluent "
            "fractionates into coker naphtha, coker gas oils (which feed "
            "the FCC or hydrocracker after hydrotreating), and fuel gas, "
            "while the coke - 20 to 30 weight percent of feed - is cut out "
            "of the drum with high-pressure water jets, then sold as fuel-"
            "grade coke for power and cement or, from clean feeds, as "
            "anode-grade coke for aluminum smelting and needle coke for "
            "electric-arc furnace electrodes. Drums operate in pairs, "
            "alternating between filling and decoking on roughly a 24-hour "
            "cycle - one of the most dramatic batch operations in "
            "continuous refining. Delayed coking lets a refinery destroy "
            "its residuum entirely, eliminating low-value heavy fuel oil "
            "from the slate."
        ),
        "how_it_works": (
            "The 'delayed' in the name is the trick: the feed is heated in "
            "the furnace but cracking is delayed until the drum, so coke "
            "forms in the vessel designed for it rather than fouling the "
            "heater tubes. In the drum, free-radical thermal cracking "
            "splits side chains off the asphaltene cores; the cracked "
            "liquids vaporize and leave, while the stripped aromatic cores "
            "condense and polymerize into solid coke that builds up in "
            "layers. Coke yield tracks the feed's Conradson carbon residue "
            "roughly 1.5 to 1.6 times over - a 20-percent-CCR resid makes "
            "about 30 percent coke. When the drum fills, it is steamed, "
            "water-quenched, unheaded, and drilled: a pilot hole is cut "
            "down the center, then high-pressure water jets carve the coke "
            "out in chunks that fall to a pit or pad. The fractionator "
            "recovers the vapors; coker naphtha is olefinic and needs "
            "hydrotreating, and coker gas oil carries the cracked "
            "character - high nitrogen, high aromatics - to upgrading "
            "units."
        ),
        "key_points": [
            "Delayed coking thermally cracks vacuum resid in coke drums at ~900-950 F, making light liquids plus 20-30 wt% solid petroleum coke.",
            "Cracking is 'delayed' to the drum so coke forms in the vessel, not in the furnace tubes.",
            "Coke yield ~1.5-1.6x the feed's Conradson carbon residue; products need hydrotreating (olefinic, high nitrogen).",
            "Coke grades: fuel-grade (power, cement), anode-grade (aluminum smelting), needle coke (steel electrodes).",
            "Paired drums alternate fill/decoke on ~24-hour cycles - batch decoking inside continuous refining.",
        ],
        "requirements": [
            "Thermal cracking kinetics (free-radical chemistry).",
            "Vacuum distillation (the residuum feed).",
            "Conradson carbon residue as a coking predictor.",
        ],
        "standards": [
            "ASTM D189/D4530 carbon residue; anode coke specs (Al smelter requirements).",
            "API 934/941 materials guidance for high-temperature service.",
        ],
        "citations": [C_SPEIGHT, C_MEYERS, C_GARY],
        "sig_lens": (
            "Signature take: the coker is where the refinery faces its "
            "demons - the residuum nobody wants, cooked until it confesses "
            "its last light molecules. His framing respects the water "
            "jet: thousands of psi carving solid carbon out of a drum, the "
            "most honest labor in the plant."
        ),
    },
    {
        "key": "hydrotreating",
        "name": "Hydrotreating: Desulfurizing the Streams",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Hydrotreating is the refinery's cleaning department: nearly "
            "every intermediate stream passes over cobalt-molybdenum or "
            "nickel-molybdenum catalyst under hydrogen pressure, and "
            "sulfur, nitrogen, oxygen, and metals come out as hydrogen "
            "sulfide, ammonia, water, and metal deposits. Without it, "
            "modern fuels could not exist - regulations demand diesel "
            "below 15 parts per million sulfur and gasoline below 10, down "
            "from percent levels a generation ago. The chemistry is "
            "hydrodesulfurization (HDS): organic sulfur compounds react "
            "with hydrogen on the catalyst's sulfided metal sites, "
            "snipping carbon-sulfur bonds. Reactivity varies enormously: "
            "mercaptans and sulfides vanish easily, while sterically "
            "hindered dibenzothiophenes - sulfur tucked inside a molecular "
            "pocket - need severe conditions and are the reason deep "
            "desulfurization is hard. Hydrodenitrogenation (HDN) needs "
            "even more severity, which is why FCC feed hydrotreaters run "
            "hot and high-pressure. Hydrotreating also saturates olefins "
            "and some aromatics, improving color, stability, and cetane - "
            "but it consumes hydrogen and slightly reduces octane in "
            "cracked naphthas, a tradeoff refiners manage carefully."
        ),
        "how_it_works": (
            "Feed and hydrogen-rich recycle gas mix, heat against reactor "
            "effluent, and enter a fixed bed of sulfided Co-Mo or Ni-Mo on "
            "alumina at 550 to 750 degrees Fahrenheit and 300 to 2000 psi "
            "depending on service. On the catalyst, sulfur compounds "
            "adsorb, C-S bonds hydrogenolyze, and H2S desorbs; nitrogen "
            "compounds hydrogenate through intermediates to ammonia. "
            "Kinetics are roughly first-order in the sulfur species, so "
            "each halving of product sulfur needs a fixed increment of "
            "severity - going from 500 to 10 ppm takes far more than going "
            "from 2 percent to 500 ppm, the cruel mathematics of deep "
            "desulfurization. The reactor effluent is cooled, separated, "
            "and stripped: H2S leaves with the recycle gas to the amine "
            "unit, and the sweetened liquid goes to fractionation or "
            "blending. Catalyst deactivates by coking and metals; cycle "
            "length runs one to several years, ended by a regeneration or "
            "changeout. Hydrogen consumption runs 50 to 200 standard cubic "
            "feet per barrel for naphtha and distillate, far more for "
            "resid service."
        ),
        "key_points": [
            "Hydrotreating strips S, N, O, and metals as H2S, NH3, H2O over Co-Mo/Ni-Mo catalysts under hydrogen pressure.",
            "Regulations drive it: ULSD <= 15 ppm sulfur, gasoline <= 10 ppm - from percent-level crudes.",
            "Sterically hindered dibenzothiophenes set the severity needed for deep desulfurization; kinetics are ~first-order in sulfur.",
            "Also saturates olefins/aromatics (better stability, cetane) but can cost octane in cracked naphtha.",
            "H2S goes to amine treating and sulfur recovery; catalyst cycles run 1+ years before regeneration.",
        ],
        "requirements": [
            "Catalysis and hydrogenation basics.",
            "The hydrogen network record (the H2 supply).",
            "Sulfur chemistry in crude (why it's there).",
        ],
        "standards": [
            "EPA ULSD (15 ppm) and Tier 3 gasoline (10 ppm) sulfur rules.",
            "ASTM D5453/D4294 sulfur measurement.",
        ],
        "citations": [C_ANCHEYTA, C_MEYERS, C_ROBINSON],
        "sig_lens": (
            "Signature take: the hydrotreater is the refinery's conscience - "
            "every stream scrubbed until it can face the tailpipe. His "
            "framing notes the moral math: the last 10 ppm of sulfur "
            "costs more than the first 10,000, and the refinery pays it "
            "anyway."
        ),
    },
    {
        "key": "hydrogen_network",
        "name": "The Refinery Hydrogen Network: Balancing Producers and Consumers",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Hydrogen is the refinery's second currency - invisible, "
            "essential, and chronically short. Producers: the catalytic "
            "reformer makes hydrogen as a byproduct of aromatization, and "
            "dedicated steam-methane reformer (SMR) hydrogen plants make "
            "the rest by reacting natural gas with steam over nickel "
            "catalyst. Consumers: hydrocrackers gulp 1000 to 2500 standard "
            "cubic feet per barrel of feed, hydrotreaters take 50 to 500, "
            "and isomerization sips a little. A deep-conversion refinery "
            "can consume over 100 million standard cubic feet per day - a "
            "gas business hidden inside the oil business. The network "
            "operates at several purity headers: high-purity hydrogen "
            "(>99 percent) from the SMR and pressure-swing adsorption "
            "units feeds the hungriest consumers, while lower-purity "
            "reformer offgas cascades to less demanding hydrotreaters. "
            "Pinch analysis of the hydrogen network - matching sources to "
            "sinks by purity, like heat integration matches hot to cold - "
            "minimizes fresh hydrogen make. When hydrogen runs short, the "
            "whole refinery slows: hydrocrackers cut rate, desulfurization "
            "slips, and margins bleed. Managing the balance is a daily "
            "optimization."
        ),
        "how_it_works": (
            "The steam-methane reformer reacts methane with steam at 1500 "
            "to 1600 degrees Fahrenheit over nickel catalyst: CH4 + H2O -> "
            "CO + 3H2, followed by the water-gas shift, CO + H2O -> CO2 + "
            "H2, roughly doubling the hydrogen. Pressure-swing adsorption "
            "then purifies the stream to 99.9 percent by cycling adsorbent "
            "beds through high-pressure adsorption and low-pressure "
            "desorption. Reformer net gas, typically 70 to 90 percent "
            "hydrogen, joins the network after compression. Consumers draw "
            "from headers matched to their purity needs; purge streams "
            "bleed off accumulating light ends and H2S to the fuel gas "
            "system. The planner's hydrogen balance sums producers "
            "against consumers plus purges and losses: the inequality must "
            "hold every day, and the SMR rate is the swing variable. "
            "Emerging practice adds hydrogen recovery membranes and "
            "considers electrolytic hydrogen, but SMR remains the economic "
            "workhorse wherever natural gas is cheap."
        ),
        "key_points": [
            "Hydrogen producers: catalytic reformer byproduct + steam-methane reformer plants; consumers: hydrocrackers, hydrotreaters, isomerization.",
            "SMR chemistry: CH4 + H2O -> CO + 3H2, then water-gas shift; PSA purifies to 99.9%.",
            "Networks run multiple purity headers; reformer offgas cascades to less demanding users (hydrogen pinch).",
            "A deep-conversion refinery can consume 100+ MMSCFD - a gas business inside the oil business.",
            "Hydrogen shortage idles conversion and breaks sulfur specs - the balance is a daily optimization constraint.",
        ],
        "requirements": [
            "Catalytic reforming (the byproduct source).",
            "Hydrocracking and hydrotreating (the consumers).",
            "Stoichiometry and gas-law arithmetic.",
        ],
        "standards": [
            "Typical SMR/PSA design practice; hydrogen purity specs by consumer.",
            "API 941 materials for hydrogen service.",
        ],
        "citations": [C_MEYERS, C_GARY, C_ROBINSON],
        "sig_lens": (
            "Signature take: hydrogen is the refinery's breath - produced "
            "in one lung, consumed in the other, and the plant suffocates "
            "without it. His framing treats the hydrogen pinch like "
            "household budgeting: match every source to a sink before "
            "buying fresh."
        ),
    },
]
ENTRIES += [
    {
        "key": "amine_sulfur",
        "name": "Amine Treating and Sulfur Recovery: Taming Hydrogen Sulfide",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Every hydrotreater and hydrocracker exhales hydrogen sulfide - "
            "toxic, corrosive, and smelling of rotten eggs at parts per "
            "billion - and the amine-sulfur complex exists to capture it "
            "and turn it into something sellable. Amine treating washes "
            "sour gas and LPG with aqueous alkanolamines (MEA, DEA, MDEA) "
            "that chemically absorb H2S and CO2 at low temperature and "
            "release them when heated, regenerating the solvent in a "
            "continuous loop. The concentrated acid gas then feeds the "
            "Claus sulfur recovery unit, where roughly one-third of the "
            "H2S is burned to sulfur dioxide and the rest reacts with it "
            "over alumina catalyst: 2H2S + SO2 -> 3S + 2H2O. Staged "
            "converters with sulfur condensers between them recover 94 to "
            "97 percent of the sulfur as bright yellow liquid, sold for "
            "sulfuric acid and fertilizer. Tail gas treating (SCOT-type "
            "units) hydrogenates the leftovers and recycles them, pushing "
            "overall recovery past 99.5 percent to meet air-quality "
            "permits. Sour water strippers handle the ammonia-laden "
            "wastewater in parallel. The complex is environmental "
            "compliance made physical - and the refinery's largest sulfur "
            "source is also a revenue stream."
        ),
        "how_it_works": (
            "In the absorber, sour gas flows up through trays or packing "
            "against downflowing lean amine; the amine's nitrogen grabs the "
            "acidic H2S in a reversible reaction favored cold. Rich amine "
            "leaves the bottom, heats against lean amine, and enters the "
            "regenerator, where reboiler steam drives the equilibrium "
            "backward, stripping concentrated acid gas overhead while lean "
            "amine returns to the absorber. Selectivity matters: MDEA "
            "absorbs H2S preferentially over CO2, useful when only sulfur "
            "must be removed. In the Claus unit, the thermal stage burns a "
            "third of the H2S at 1800 to 2500 degrees Fahrenheit; the "
            "catalytic stages then run the Claus reaction at 400 to 650 "
            "degrees, condensing liquid sulfur after each stage to pull "
            "equilibrium forward. Overall recovery follows the staging: "
            "two catalytic stages reach about 96 percent, three about 97. "
            "Tail gas units hydrogenate residual sulfur species back to "
            "H2S, absorb it in amine, and recycle to the Claus feed - the "
            "loop that breaks 99 percent. Operators watch amine strength, "
            "circulation rate, regenerator energy, Claus air demand ratio, "
            "and sulfur rundown temperature (kept above freezing point to "
            "avoid solid plugs)."
        ),
        "key_points": [
            "Amine units absorb H2S/CO2 cold and strip them hot, regenerating the solvent continuously (MDEA is H2S-selective).",
            "The Claus process: burn 1/3 of H2S to SO2, then react 2H2S + SO2 -> 3S + 2H2O over catalyst in staged converters.",
            "Staged Claus with condensers recovers 94-97% of sulfur as saleable liquid; tail gas treating pushes past 99.5%.",
            "Sour water strippers handle ammonia-laden wastewater in parallel with the gas train.",
            "The complex converts a toxic waste into fertilizer and acid feedstock - compliance as revenue.",
        ],
        "requirements": [
            "Hydrotreating (the H2S source).",
            "Acid-base equilibrium and Le Chatelier's principle.",
            "The hydrogen network record (where acid gas competes for attention).",
        ],
        "standards": [
            "EPA NSPS Subpart Ja and NESHAP Subpart CC sulfur recovery requirements.",
            "Typical permit: 99%+ sulfur recovery, < 250 ppm SO2 in tail gas.",
        ],
        "citations": [C_MEYERS, C_GARY, C_ROBINSON],
        "sig_lens": (
            "Signature take: the sulfur complex is the refinery's "
            "conscience with a business plan - poison in, yellow gold out. "
            "His framing admires the Claus reaction's thrift: burn a "
            "third, marry it to the rest, and sell the wedding sulfur."
        ),
    },
    {
        "key": "gasoline_blending",
        "name": "Gasoline Blending: The Octane Recipe",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "No refinery unit makes finished gasoline - the blender does. "
            "Gasoline is a recipe of six to ten blendstocks: reformate "
            "(high octane, high aromatics), FCC gasoline (high octane, "
            "olefinic, sulfurous), alkylate (the premium: 94-98 RON, clean), "
            "isomerate (clean light octane), straight-run naphtha (cheap, "
            "low octane), butane (cheap octane and vapor pressure), and "
            "oxygenates like ethanol (octane and renewable credit). The "
            "blender must hit a dozen specifications at once: research and "
            "motor octane (the pump number is their average), Reid vapor "
            "pressure (volatility for starting versus vapor lock, varying "
            "by season and region), distillation points (driveability), "
            "sulfur (10 ppm), benzene (0.62 percent), aromatics and "
            "olefins limits, and oxidation stability. Blending is done "
            "in-line with analyzers and a multivariable controller that "
            "adjusts component ratios in real time - or in tanks for "
            "smaller plants. The economics are sharp: each octane-barrel "
            "has a value, and the optimizer gives away as little quality "
            "as possible while meeting every spec. Butane is the classic "
            "lever - cheap octane in winter when vapor pressure limits are "
            "loose, forbidden in summer."
        ),
        "how_it_works": (
            "Most properties blend nearly linearly by volume: the blend's "
            "property is the volume-weighted average of the components'. "
            "Octane is the famous exception - it blends nonlinearly, so "
            "refiners use laboratory-measured blending octane numbers for "
            "each component in each recipe rather than pure-component "
            "octanes. Vapor pressure also deviates from linearity and is "
            "handled with blending indices (the Chevron RVP index method). "
            "The blend optimizer solves a small linear program: minimize "
            "cost subject to meeting every specification with a safety "
            "margin, respecting component availabilities. In-line blending "
            "adds feedback: a near-infrared analyzer measures the running "
            "blend's octane, RVP, and distillation every minute or two, "
            "and the controller trims ratios to hold specs dead-on, "
            "capturing the giveaway that tank blending wastes. Ethanol is "
            "usually splash-blended at the terminal (E10) rather than at "
            "the refinery, because ethanol cannot travel in petroleum "
            "pipelines - it picks up water. The finished gasoline is "
            "certified by laboratory test before release."
        ),
        "key_points": [
            "Finished gasoline is blended from 6-10 stocks (reformate, FCC gasoline, alkylate, isomerate, naphtha, butane, ethanol) - no unit makes it directly.",
            "Specs: (R+M)/2 octane, RVP by season, distillation, sulfur 10 ppm, benzene 0.62%, aromatics/olefins limits.",
            "Most properties blend linearly by volume; octane and RVP need blending numbers/indices for nonlinearity.",
            "In-line blending with NIR analyzers and multivariable control minimizes quality giveaway versus tank blending.",
            "Ethanol is splash-blended at terminals (E10) because it cannot ship in petroleum pipelines.",
        ],
        "requirements": [
            "Octane and the reforming/alkylation/isomerization records (the blendstocks).",
            "Linear programming basics (the optimizer).",
            "Vapor pressure and distillation concepts.",
        ],
        "standards": [
            "ASTM D4814 gasoline specification; D2699/D2700 octane; D5191 RVP.",
            "EPA Tier 3 sulfur/benzene limits; seasonal RVP rules.",
        ],
        "citations": [C_GARY, C_MEYERS, C_ASTM],
        "sig_lens": (
            "Signature take: the blender is the refinery's chef - ten "
            "ingredients, twelve specs, one perfect pour. His framing "
            "treats giveaway as the enemy: every octane number above spec "
            "is money left on the table, and the optimizer is the "
            "accountant with a whisk."
        ),
    },
    {
        "key": "diesel_jet_specs",
        "name": "Diesel and Jet Fuel: Specifications That Matter",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Diesel and jet fuel are specified for the engines that burn "
            "them, and the specifications read like engine biographies. "
            "Diesel's headline property is cetane number - the opposite of "
            "octane: it measures how readily the fuel auto-ignites under "
            "compression, with higher cetane giving quicker, cleaner cold "
            "starts. The cetane index, calculated from density and "
            "distillation (ASTM D4737), estimates it without an engine "
            "test. Lubricity matters because modern high-pressure fuel "
            "injection runs on the fuel itself as lubricant - ultra-low-"
            "sulfur processing strips natural lubricity, so additives "
            "restore it. Cold flow properties - cloud point, pour point, "
            "and cold filter plugging point - decide whether a truck "
            "starts in January. Jet fuel (Jet A/A-1) adds aviation's "
            "non-negotiables: freeze point below -40 (Jet A) or -47 "
            "degrees Celsius (Jet A-1), flash point above 38, strict "
            "thermal stability (JFTOT test) so fuel doesn't coke in hot "
            "engine plumbing, and rigorous contamination control - water "
            "and particles are filtered and tested because at altitude "
            "there is no roadside assistance. Both fuels are capped at "
            "trace sulfur and tightly limited in aromatics behavior."
        ),
        "how_it_works": (
            "Cetane number is measured in a test engine (ASTM D613) by "
            "comparing ignition delay against reference blends, but "
            "refineries control it with the cetane index from routine lab "
            "data: density plus mid-boiling points predict it well enough "
            "for blending. Hydrocracking and deep hydrotreating raise "
            "cetane by saturating aromatics; FCC light cycle oil, rich in "
            "aromatics, drags it down and needs upgrading or dilution. "
            "Lubricity is restored with parts-per-million fatty-acid or "
            "ester additives, verified by the high-frequency reciprocating "
            "rig (HFRR) wear-scar test. Cold flow is managed by cut point "
            "(lighter cuts flow colder) and by cold-flow improver "
            "additives that modify wax crystal growth. Jet fuel's thermal "
            "stability is proven in the JFTOT: fuel flows over a heated "
            "tube at 260 degrees Celsius and the deposits are scored - "
            "hydrotreated and hydrocracked stocks pass easily, which is "
            "why they dominate the jet pool. Every batch is certified: "
            "the lab result, not the unit's word, releases the fuel."
        ),
        "key_points": [
            "Diesel: cetane number (ignition quality, opposite of octane), lubricity, cold flow, ULSD 15 ppm sulfur.",
            "Cetane index (D4737) estimates cetane from density + distillation; hydrocracking raises it, FCC LCO lowers it.",
            "ULSD processing strips natural lubricity - ppm-level additives restore it (HFRR wear-scar test).",
            "Jet A/A-1: freeze point -40/-47 C, flash > 38 C, JFTOT thermal stability, extreme contamination control.",
            "Both fuels are batch-certified by laboratory test before release - the lab, not the unit, has the last word.",
        ],
        "requirements": [
            "Hydrocracking and hydrotreating (how the specs are achieved).",
            "Distillation and density (the cetane index inputs).",
            "Combustion basics (why cetane and octane oppose).",
        ],
        "standards": [
            "ASTM D975 diesel; D1655 jet fuel; D613 cetane; D4737 cetane index.",
            "EPA ULSD 15 ppm sulfur; DEF STAN 91-091 / Jet A-1.",
        ],
        "citations": [C_GARY, C_ASTM, C_ROBINSON],
        "sig_lens": (
            "Signature take: diesel and jet specs are engine biographies - "
            "cetane for the compression-ignition handshake, freeze point "
            "for the stratosphere. His framing treats the JFTOT tube as "
            "the fuel's job interview: pass the hot tube, get the wings."
        ),
    },
    {
        "key": "lubricants",
        "name": "Lubricants and Base Oils: The Quiet Products",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Lubricants are the refinery's quiet aristocrats - small in "
            "volume, high in value, and made to far tighter molecular "
            "specifications than fuels. A finished lubricant is 75 to 90 "
            "percent base oil plus an additive package (detergents, "
            "dispersants, anti-wear, antioxidants, viscosity modifiers, "
            "pour point depressants). Base oils are classified by the API "
            "into Groups: Group I (solvent-refined, higher sulfur, VI "
            "80-120), Group II (hydroprocessed, low sulfur, VI 80-120), "
            "Group III (severely hydrocracked, VI above 120 - the "
            "'synthetic' workhorse), Group IV (polyalphaolefins, true "
            "synthetics), and Group V (everything else, including "
            "esters). The traditional route deasphalts vacuum resid, "
            "solvent-extracts aromatics with furfural or NMP, dewaxes with "
            "cold solvents (MEK/toluene) or catalytic isomerization, and "
            "hydrofinishes; the modern route hydrocracks vacuum gas oil "
            "directly into Group II/III stocks. The headline property is "
            "the viscosity index - how little viscosity changes with "
            "temperature - because an engine oil must flow at cold start "
            "and protect at operating temperature. Multigrade oils like "
            "5W-30 achieve this with viscosity-modifier polymers that "
            "uncoil when hot."
        ),
        "how_it_works": (
            "Solvent refining exploits selectivity: furfural dissolves "
            "aromatics preferentially, leaving paraffinic raffinate with "
            "higher VI; the extract becomes aromatic process oil. "
            "Dewaxing removes normal paraffins that would crystallize in "
            "the cold - either by chilling in solvent and filtering the "
            "wax crystals (which become a saleable wax product) or by "
            "catalytically isomerizing the wax into branched, low-pour "
            "molecules. Hydrocracker-based lube plants instead convert "
            "waxy vacuum gas oil over shape-selective catalysts "
            "directly into high-VI base oil, with unconverted oil "
            "recycled. Hydrofinishing saturates remaining aromatics and "
            "removes color bodies. Blending then hits the SAE viscosity "
            "grades: kinematic viscosity at 100 C defines the grade "
            "(a 30-grade spans 9.3-12.5 cSt), cold-cranking simulator "
            "viscosity sets the winter 'W' rating, and the additive "
            "package is dosed by formulation. Quality control runs "
            "oxidation, wear, foam, and elastomer-compatibility bench "
            "tests before the oil earns its API service classification."
        ),
        "key_points": [
            "Finished lubricants are 75-90% base oil + additive package; base oils are API Group I-V by sulfur, saturates, and VI.",
            "Routes: solvent refining (furfural extraction, solvent dewaxing) or hydrocracker-based (catalytic dewaxing to Group II/III).",
            "Viscosity index is the headline property - stable viscosity from cold start to operating temperature.",
            "Dewaxing removes or isomerizes wax paraffins; the wax itself is a saleable product.",
            "SAE grades (e.g., 5W-30) combine 100 C viscosity with winter cranking performance; additives complete the formulation.",
        ],
        "requirements": [
            "Viscosity index and the Walther equation (the properties record).",
            "Hydrocracking (the modern base-oil route).",
            "Solvent extraction and crystallization basics.",
        ],
        "standards": [
            "API 1509 base oil groups; SAE J300 viscosity grades.",
            "ASTM D445 viscosity, D2270 VI, D97 pour point.",
        ],
        "citations": [C_MEYERS, C_SPEIGHT, C_ASTM],
        "sig_lens": (
            "Signature take: base oil is the refinery's tailored suit - "
            "cut to the molecule, pressed by dewaxing, finished by "
            "hydrogen. His framing treats Group III as the quiet triumph: "
            "severely hydrocracked mineral oil out-performing yesterday's "
            "synthetics."
        ),
    },
    {
        "key": "heavy_products",
        "name": "Asphalt, Coke, and Heavy Products: Nothing Wasted",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "At the bottom of the barrel, the refinery still finds value. "
            "Vacuum residuum becomes asphalt - the binder in the pavement "
            "under every highway - graded by performance: the Superpave "
            "PG system (for example PG 64-22) specifies the high and low "
            "pavement temperatures the binder must survive, tested with "
            "the dynamic shear rheometer for rutting resistance and the "
            "bending beam rheometer for low-temperature cracking. Air "
            "blowing oxidizes soft resid into harder roofing and "
            "industrial asphalts. Petroleum coke from the delayed coker "
            "splits into fuel grade (power plants, cement kilns) and "
            "premium grades: anode coke for aluminum smelting, where "
            "purity and density are paramount, and needle coke for the "
            "graphite electrodes of electric-arc steel furnaces - one of "
            "the highest-value carbons the refinery makes. Heavy fuel oil, "
            "once the residuum's main home, is shrinking under marine "
            "sulfur regulations (IMO 2020 capped bunker sulfur at 0.5 "
            "percent), pushing more resid into cokers. Even sulfur finds "
            "its market. The deep-conversion refinery's creed is simple: "
            "the barrel has no bottom, only products not yet separated."
        ),
        "how_it_works": (
            "Asphalt grading moved from empirical penetration tests to "
            "fundamental rheology: the DSR oscillates a binder sample at "
            "high service temperatures and requires a minimum complex "
            "modulus over sin(delta) to resist rutting; the BBR bends a "
            "beam at low temperature and limits stiffness and relaxation "
            "to resist thermal cracking. Air blowing bubbles air through "
            "hot resid, oxidizing and polymerizing asphaltenes to raise "
            "softening point for roofing grades. Coke quality is set in "
            "the drum: low metals and low sulfur feeds make anode-grade "
            "sponge coke, calcined at 2000+ degrees Fahrenheit to drive "
            "off volatiles before smelter use; special aromatic feeds make "
            "needle coke with its aligned, graphitizable structure. Fuel "
            "oil blending cuts resid with cutter stock to hit viscosity "
            "and sulfur specs - visbreaking reduces the cutter need. "
            "Marketing these products is its own discipline: asphalt "
            "demand is seasonal and local (it ships hot, in insulated "
            "trucks), while coke and sulfur move globally."
        ),
        "key_points": [
            "Vacuum resid becomes PG-graded asphalt (Superpave: DSR for rutting, BBR for thermal cracking) or air-blown roofing grades.",
            "Petroleum coke grades: fuel (power/cement), anode (aluminum smelting), needle (steel electrodes) - purity sets value.",
            "IMO 2020's 0.5% marine sulfur cap shrank heavy fuel oil's home, pushing resid toward cokers.",
            "Coke calcining and needle-coke structure show the bottom of the barrel reaching the highest-tech markets.",
            "Asphalt is seasonal and local (ships hot); coke and sulfur trade globally.",
        ],
        "requirements": [
            "Vacuum distillation (the residuum source).",
            "Delayed coking (the coke source).",
            "Rheology basics (for asphalt grading).",
        ],
        "standards": [
            "AASHTO M 320 Superpave PG grading; ASTM D946 penetration grading (legacy).",
            "IMO 2020 marine fuel sulfur cap (MARPOL Annex VI).",
        ],
        "citations": [C_SPEIGHT, C_MEYERS, C_GARY],
        "sig_lens": (
            "Signature take: the heavy end is the refinery's proof of "
            "character - highways, aluminum, and steel electrodes from "
            "what the tower couldn't boil. His framing calls asphalt the "
            "barrel's final exam: nothing wasted, everything placed."
        ),
    },
    {
        "key": "petrochemical_integration",
        "name": "Petrochemical Integration: Where Refinery Meets Chemical Plant",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The fence between a refinery and a petrochemical plant is "
            "increasingly imaginary. Refinery streams are ideal chemical "
            "feedstocks: naphtha steam-cracks into ethylene, propylene, "
            "butadiene, and aromatics; FCC propylene feeds "
            "polypropylene; reformate yields benzene, toluene, and xylenes "
            "- the BTX aromatics at the root of polystyrene, nylon, and "
            "polyester; and refinery hydrogen feeds ammonia and methanol "
            "ambitions. Integration runs both directions: the aromatics "
            "complex extracts BTX from reformate and pyrolysis gasoline, "
            "returning raffinate to the gasoline pool; the steam cracker "
            "returns pyrolysis gasoline and fuel oil to the refinery; "
            "shared utilities, hydrogen networks, and fuel gas systems "
            "cut both plants' costs. The economics are compelling - "
            "chemicals typically earn higher, more stable margins than "
            "fuels - which is why new mega-refineries are designed as "
            "refinery-petrochemical complexes from the first drawing, "
            "with crude-to-chemicals configurations pushing chemical "
            "yields toward 40 percent and beyond. For the refiner, "
            "integration is a hedge: when fuel demand softens, molecules "
            "flow to plastics, fibers, and resins instead."
        ),
        "how_it_works": (
            "Steam cracking heats naphtha or ethane with steam to 1500 "
            "degrees Fahrenheit for fractions of a second: the thermal "
            "shock shatters molecules into ethylene, propylene, and "
            "butadiene, quenched instantly to freeze the product slate. "
            "Typical naphtha yields run about 30 percent ethylene, 14 "
            "percent propylene, with the rest as butadiene, aromatics-rich "
            "pyrolysis gasoline, and fuel oil. The aromatics complex takes "
            "reformate through extraction (sulfolane or similar solvents "
            "pull aromatics from paraffins), then fractionates benzene, "
            "toluene, and mixed xylenes; disproportionation and "
            "transalkylation then rebalance toluene into more benzene and "
            "xylenes to match market demand, and isomerization maximizes "
            "para-xylene - the polyester precursor. Propylene from the FCC "
            "is purified in a C3 splitter (superfractionation, 150+ trays) "
            "to polymer grade. Shared-site integration optimizes the whole: "
            "the linear program spans both plants, routing each molecule "
            "to its highest-value home."
        ),
        "key_points": [
            "Refinery streams feed petrochemicals: naphtha to steam crackers, FCC propylene to polypropylene, reformate to BTX aromatics.",
            "Steam cracking: ~1500 F thermal shock gives ~30% ethylene, ~14% propylene from naphtha plus butadiene and pyrolysis gasoline.",
            "The aromatics complex extracts BTX and rebalances them (disproportionation, transalkylation, xylene isomerization) to market demand.",
            "Integration shares utilities, hydrogen, fuel gas, and planning - new complexes are designed as one plant from day one.",
            "Crude-to-chemicals configurations push chemical yields toward 40%+ as a hedge against softening fuel demand.",
        ],
        "requirements": [
            "Catalytic reforming (the BTX source).",
            "The FCC record (the propylene source).",
            "Naphtha and light-ends handling.",
        ],
        "standards": [
            "Polymer-grade propylene specs (typically 99.5%+ purity).",
            "Para-xylene and benzene product specifications (ASTM D2359, D4492).",
        ],
        "citations": [C_MEYERS, C_ROBINSON, C_GARY],
        "sig_lens": (
            "Signature take: integration erases the fence - the refinery "
            "and the chemical plant become one molecule market. His "
            "framing treats crude-to-chemicals as the barrel's career "
            "change: from burner fuel to the shirt on your back."
        ),
    },
    {
        "key": "refinery_safety",
        "name": "Refinery Safety: HAZOP, Relief, and Process Safety Management",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A refinery concentrates the fire triangle - fuel, heat, and "
            "oxygen - at industrial scale, so safety is engineered in "
            "layers, not wished for. Process Safety Management (OSHA "
            "1910.119) is the legal backbone in the United States: "
            "fourteen elements including process hazard analysis, "
            "operating procedures, management of change, and incident "
            "investigation, applied to every highly hazardous process. "
            "The HAZOP study is the workhorse: a multidisciplinary team "
            "walks each line of the plant with guidewords - MORE flow, "
            "LESS pressure, REVERSE composition - and asks what breaks, "
            "what ignites, what poisons, recording safeguards and "
            "recommendations node by node. Pressure relief devices - "
            "spring-loaded valves and rupture disks sized per API 520/521 - "
            "are the last mechanical defense against overpressure, venting "
            "to flare systems that burn releases safely. Safety instrumented "
            "systems (interlocks rated by SIL, safety integrity level) "
            "detect excursions and drive the plant to a safe state "
            "automatically. Layers of protection analysis (LOPA) quantifies "
            "it: each independent layer - alarms, interlocks, relief, "
            "containment - multiplies down the risk by its probability of "
            "failure on demand."
        ),
        "how_it_works": (
            "A relief valve is sized for the worst credible contingency: "
            "for a vessel engulfed in fire, API 521 computes the heat input "
            "from the wetted surface area and converts it to a vapor "
            "relief rate; the valve orifice area then follows from the "
            "critical-flow equation using the relieving pressure, "
            "temperature, molecular weight, and compressibility. The "
            "discharge goes to a flare header sized for the combined "
            "worst-case load, with knockout drums to catch liquid and a "
            "flare tip designed to burn smokelessly with steam assist. "
            "LOPA starts from an initiating event frequency (say, cooling "
            "failure at 0.1 per year), multiplies by each protection "
            "layer's probability of failure on demand (a SIL 1 interlock "
            "at 0.1, a relief valve at 0.01), and checks the mitigated "
            "frequency against the corporate risk target - typically 1 in "
            "10,000 to 1 in 1,000,000 years for fatalities. If the math "
            "fails, add layers or redesign. Management of change ensures "
            "no valve, setpoint, or procedure changes without hazard "
            "review - because most incidents trace to an unreviewed "
            "change."
        ),
        "key_points": [
            "OSHA PSM (1910.119) mandates hazard analysis, procedures, management of change, and incident investigation.",
            "HAZOP systematically applies guidewords (MORE/LESS/REVERSE of flow, pressure, temperature) to every plant node.",
            "Relief devices sized per API 520/521 vent worst-case loads to flare systems - the last mechanical defense.",
            "Safety instrumented systems (SIL-rated interlocks) drive the plant to safe state automatically.",
            "LOPA quantifies risk: initiating frequency x PFD of each independent layer must beat the risk target.",
        ],
        "requirements": [
            "Pressure, relief, and flare concepts.",
            "Probability basics (for LOPA multiplication).",
            "Refinery unit operations (what is being protected).",
        ],
        "standards": [
            "OSHA 29 CFR 1910.119 PSM; EPA Risk Management Program 40 CFR 68.",
            "API 520/521 relief sizing; API 521 flare systems; IEC 61511 SIS.",
        ],
        "citations": [C_OSHA_PSM, C_MEYERS, C_ROBINSON],
        "sig_lens": (
            "Signature take: process safety is the refinery's humility "
            "engineered - every HAZOP guideword an admission that smart "
            "people miss things. His framing treats the relief valve as "
            "the plant's conscience: silent for decades, correct for one "
            "terrible minute."
        ),
    },
    {
        "key": "environmental_controls",
        "name": "Emissions and Environmental Controls: The Clean Refinery",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The modern refinery operates inside a tightening envelope of "
            "air, water, and waste regulation, and environmental control "
            "is now a process discipline of its own. Air emissions center "
            "on sulfur dioxide (from fuel gas and FCC regenerators), "
            "nitrogen oxides (furnaces and boilers), volatile organic "
            "compounds (storage tanks, loading, fugitive leaks), "
            "particulates (catalyst fines), and benzene and other air "
            "toxics. Controls are layered: low-NOx burners and selective "
            "catalytic reduction cut furnace NOx; FCC regenerators get CO "
            "boilers, electrostatic precipitators, and wet gas scrubbers; "
            "floating-roof tanks and vapor recovery units capture tank "
            "breathing losses; leak detection and repair (LDAR) programs "
            "hunt fugitive emissions valve by valve with analyzers; flares "
            "must meet combustion efficiency rules with continuous "
            "monitoring. Wastewater goes through API separators, dissolved "
            "air flotation, and biological treatment before discharge "
            "under permit limits. Solid wastes - spent catalyst, tank "
            "sludges, coker fines - are recycled, regenerated, or disposed "
            "as hazardous waste. Fenceline monitoring for benzene now "
            "watches the plant's boundary in real time. Compliance is "
            "continuous, measured, and public."
        ),
        "how_it_works": (
            "A wet gas scrubber on an FCC regenerator sprays alkaline "
            "slurry into the flue gas: SO2 absorbs and oxidizes to sulfate, "
            "particulates are captured by impaction, and removal exceeds "
            "95 percent. Low-NOx burners stage fuel and air to keep flame "
            "temperatures below the thermal-NOx formation threshold; SCR "
            "injects ammonia over catalyst to reduce remaining NOx to "
            "nitrogen and water. Floating roofs ride on the liquid surface "
            "in storage tanks, eliminating the vapor space that fixed "
            "roofs breathe; rim seals and deck fittings are the residual "
            "leak paths LDAR monitors. Flare combustion efficiency - "
            "targeted above 98 percent destruction - is assured by "
            "maintaining adequate heating value in the vent gas and proper "
            "steam assist, verified by video and parametric monitoring. "
            "Wastewater treatment trains remove oil and solids physically, "
            "then biodegrade dissolved organics in activated-sludge "
            "basins; the discharge permit sets limits on oil, COD, "
            "ammonia, phenols, and metals. Continuous emissions monitors "
            "on major stacks report to regulators in near-real time."
        ),
        "key_points": [
            "Regulated pollutants: SO2, NOx, VOCs, particulates, benzene/air toxics; permits set hard numeric limits.",
            "FCC regenerators: CO boilers, ESPs, wet scrubbers (>95% SO2/particulate removal). Furnaces: low-NOx burners + SCR.",
            "Floating-roof tanks, vapor recovery, and LDAR programs control storage and fugitive VOC emissions.",
            "Flares must sustain >98% combustion efficiency with monitoring; wastewater gets physical + biological treatment.",
            "Fenceline benzene monitoring and continuous stack monitors make compliance visible in real time.",
        ],
        "requirements": [
            "The FCC and furnace operations (the emission sources).",
            "Amine/sulfur recovery (the sulfur control route).",
            "Combustion chemistry basics.",
        ],
        "standards": [
            "EPA NSPS Subpart Ja; NESHAP Subpart CC; fenceline monitoring rule.",
            "NPDES wastewater discharge permits; RCRA hazardous waste rules.",
        ],
        "citations": [C_EPA_NSPS, C_ROBINSON, C_MEYERS],
        "sig_lens": (
            "Signature take: the clean refinery is the industry's apology "
            "made mechanical - scrubbers, seals, and monitors turning "
            "compliance into craft. His framing treats fenceline benzene "
            "monitors as the plant's report card, posted where the "
            "neighbors can read it."
        ),
    },
    {
        "key": "refinery_economics",
        "name": "Refinery Economics: Margins, Complexity, and Linear Programming",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Refineries are price-takers in brutal commodity markets, and "
            "their economics reduce to a few sharp numbers. The gross "
            "refining margin - product revenues minus crude cost per barrel "
            "- is the headline; the crack spread (for example, 3-2-1: "
            "three barrels of crude into two of gasoline and one of "
            "distillate) is its market shorthand. Net margin subtracts "
            "operating costs: energy (often the largest), catalysts and "
            "chemicals, labor, and maintenance - typically a few dollars "
            "per barrel. Complexity decides who wins which crude: the "
            "Nelson complexity index weights each unit's investment cost "
            "against crude distillation, so a coker or hydrocracker "
            "contributes far more than its capacity share. A complex "
            "refinery buys discounted heavy sour crudes and upgrades them "
            "into light products, capturing the light-heavy and sweet-sour "
            "differentials as profit; a simple refinery must buy light "
            "sweet crude and lives on thinner spreads. The planning tool "
            "is linear programming: the LP model encodes every unit's "
            "yields, capacities, and constraints plus product specs and "
            "prices, then optimizes crude slate, unit severities, and "
            "product blending for maximum margin - re-run whenever prices "
            "move. Turnarounds, the multi-week shutdowns for maintenance "
            "every 3 to 6 years, are the great margin events: planned, "
            "expensive, and unavoidable."
        ),
        "how_it_works": (
            "The Nelson index sums, over all units, (unit capacity / crude "
            "capacity) x complexity factor: crude distillation is 1.0 by "
            "definition, vacuum distillation about 2, FCC about 6, "
            "hydrocracking about 6, coking about 6, reforming about 5 - a "
            "deep-conversion refinery totals 10 to 14. The LP model is "
            "built from assay data: each crude's yields through each unit "
            "at each severity become linear coefficients, and the solver "
            "maximizes margin = sum(product volumes x prices) - crude cost "
            "- operating cost, subject to unit capacities, hydrogen "
            "balance, product specifications, and term commitments. "
            "Shadow prices from the solution reveal bottlenecks: a "
            "hydrocracker with a high shadow price is the next "
            "debottleneck project. Margin math is unforgiving - a dollar "
            "per barrel on 200,000 barrels per day is 73 million dollars a "
            "year, which is why planners chase fractions. Hedging with "
            "futures locks crack spreads for forward production, turning "
            "price risk into a managed variable."
        ),
        "key_points": [
            "Gross margin = products minus crude per barrel; the 3-2-1 crack spread is the market's shorthand.",
            "Nelson complexity index (unit cost-weighting vs crude distillation) measures upgrading power: 10-14 for deep conversion.",
            "Complex refineries profit from light-heavy and sweet-sour crude discounts; simple refineries need light sweet crude.",
            "Linear programming optimizes crude slate, severities, and blending; shadow prices expose the next bottleneck.",
            "$1/bbl on 200,000 bpd is $73M/year - planners chase fractions, and turnarounds are the great margin events.",
        ],
        "requirements": [
            "The refinery flow record (units and their roles).",
            "Linear programming / optimization basics.",
            "Crude assay (how crudes are valued).",
        ],
        "standards": [
            "Nelson complexity conventions (Oil & Gas Journal).",
            "Standard LP planning practice (PIMS/RPMS-class models).",
        ],
        "citations": [C_GARY, C_FAHIM, C_ROBINSON],
        "sig_lens": (
            "Signature take: refinery economics is arbitrage with "
            "furnaces - buy the barrel the market disrespects, sell the "
            "molecules it craves. His framing treats the LP shadow price "
            "as the plant whispering where to spend the next dollar."
        ),
    },
    {
        "key": "quality_testing",
        "name": "Product Quality Testing: Proving the Barrel",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "In refining, the laboratory has the last word: no product "
            "ships until tested against its specification, and the test "
            "methods are ASTM standards recognized worldwide. Distillation "
            "(D86) remains the signature test - the curve of temperature "
            "versus percent evaporated predicts driveability, cold "
            "starting, and vapor lock behavior. Octane engines (D2699 "
            "research, D2700 motor) knock-test gasoline against reference "
            "fuels; cetane engines do the same for diesel ignition "
            "quality. Flash point (D93) sets the safe-handling "
            "temperature; Reid vapor pressure (D5191) governs volatility "
            "by season. Sulfur has gone trace-level: D5453 ultraviolet "
            "fluorescence measures parts per million. Compositional tests "
            "- PIONA or DHA gas chromatography - split naphtha into "
            "paraffins, isoparaffins, olefins, naphthenes, and aromatics "
            "carbon number by carbon number, the data blenders and "
            "reformer operators live on. Metals (D5708 ICP), nitrogen "
            "(D5762 chemiluminescence), gum, oxidation stability, corrosion "
            "(copper strip D130), and water separation (MSEP) complete "
            "the battery. Modern labs are automated and LIMS-driven, with "
            "results flowing straight to the blending controllers and "
            "certificates of quality that travel with every cargo."
        ),
        "how_it_works": (
            "A D86 distillation charges 100 milliliters to a flask, heats "
            "at a standardized rate, and records vapor temperature at each "
            "percent recovered - the initial boiling point, the 10/50/90 "
            "percent points, and the end point become the product's "
            "fingerprint. The CFR octane engine compresses the fuel-air "
            "mixture at 600 rpm (research) or 900 rpm with heated intake "
            "(motor), and the operator brackets the knock intensity "
            "between reference blends of isooctane (100) and n-heptane "
            "(0) - the match point is the octane number. UV fluorescence "
            "for sulfur combusts the sample, converts sulfur to SO2, and "
            "measures its ultraviolet emission - sensitive to single-digit "
            "ppm. DHA chromatography sends vaporized naphtha through a "
            "100-meter capillary column, identifying hundreds of "
            "individual hydrocarbons by retention time against standards. "
            "Statistical quality control charts track each analyzer's "
            "repeatability; a test out of control invalidates the batch "
            "until resolved. In-line NIR analyzers extend the lab to the "
            "pipe, predicting octane, RVP, and distillation from spectra "
            "every minute for blend control."
        ),
        "key_points": [
            "No product ships until lab-tested: ASTM methods are the global referee (D86, D2699/D2700, D613, D5453...).",
            "D86 distillation predicts driveability; CFR engines measure octane/cetane by knock bracketing against reference fuels.",
            "Trace sulfur (D5453 UV fluorescence) and DHA chromatography (PIONA by carbon number) are the modern workhorses.",
            "Flash point, RVP, corrosion, gum, stability, and water-separation tests cover safety and handling.",
            "In-line NIR analyzers bring lab predictions to the pipe every minute for real-time blend control.",
        ],
        "requirements": [
            "Distillation and octane/cetane concepts.",
            "Gasoline blending and diesel/jet specs (what is tested).",
            "Basic statistics (repeatability, control charts).",
        ],
        "standards": [
            "ASTM D86, D2699, D2700, D613, D5453, D5191, D130, D2274.",
            "ISO 17025 laboratory accreditation practice.",
        ],
        "citations": [C_ASTM, C_RIAZI, C_GARY],
        "sig_lens": (
            "Signature take: the lab is the refinery's courtroom - every "
            "barrel innocent until tested, guilty until certified. His "
            "framing treats the certificate of quality as the barrel's "
            "passport: no stamp, no travel."
        ),
    },
    {
        "key": "corrosion_materials",
        "name": "Corrosion and Materials: The Refinery's Slow Enemy",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Refineries are corrosion battlegrounds: hot sulfur compounds, "
            "naphthenic acids, chlorides, hydrogen, and cyanides attack "
            "steel through a dozen distinct mechanisms, and materials "
            "selection is a core engineering discipline. Sulfidation "
            "thins carbon steel above about 500 degrees Fahrenheit as "
            "sulfur compounds form iron sulfide scale - predictable by the "
            "McConomy curves, fought with chromium: 5-chrome, 9-chrome, "
            "and stainless steels resist progressively better. "
            "Naphthenic acid corrosion carves localized pits and grooves "
            "in hot high-acid crude service, worst around 450 to 750 "
            "degrees, and is managed with upgraded metallurgy, "
            "neutralizers, or crude blending. Chloride stress-corrosion "
            "cracking threatens austenitic stainless in chloride service; "
            "polythionic acid cracking attacks sensitized stainless during "
            "shutdowns. High-temperature hydrogen attack decarburizes "
            "steel above the Nelson-curve limits - the reason hydrocracker "
            "reactors are clad in stainless and built from vanadium-"
            "modified chrome-moly. Corrosion is monitored with ultrasonic "
            "thickness gauging, corrosion coupons (weight loss converted "
            "to mils per year), and electrical-resistance probes, feeding "
            "inspection programs (API 570/571/580) that schedule "
            "replacements before failures. Every major refinery incident "
            "with a corrosion root cause traces to a defeated barrier - "
            "missed inspection, wrong metallurgy, or an unreviewed change."
        ),
        "how_it_works": (
            "A corrosion coupon - a weighed steel strip exposed in the "
            "process stream for a known time - converts weight loss to "
            "corrosion rate by the formula: mpy = 534 x W / (D x A x T), "
            "with W in milligrams, D density in g/cm3, A area in square "
            "inches, T time in hours. Rates below 5 mils per year are "
            "generally acceptable for carbon steel; above 20 demands "
            "action. The McConomy curves plot sulfidation rate against "
            "temperature for carbon steel through stainless, letting "
            "engineers pick the minimum alloy for a predicted 10-year "
            "life. The Nelson curves do the same for hydrogen attack: "
            "each steel has a temperature-pressure boundary, and operating "
            "above it invites decarburization and fissuring. Naphthenic "
            "acid corrosion is quantified by the total acid number (TAN, "
            "mg KOH/g) of the crude fractions - high-TAN crudes above "
            "about 0.5 trigger alloy upgrades in hot zones. Inspection "
            "is risk-based (API 580): high-consequence, high-rate circuits "
            "get the most attention, and fitness-for-service assessment "
            "(API 579) decides whether thinned equipment runs, repairs, "
            "or retires."
        ),
        "key_points": [
            "Mechanisms: sulfidation (McConomy curves), naphthenic acid attack, chloride SCC, polythionic acid cracking, high-temp hydrogen attack (Nelson curves).",
            "Chromium content is the defense ladder: carbon steel < 5Cr < 9Cr < stainless for sulfidation service.",
            "Corrosion coupons convert weight loss to mils per year (mpy = 534W/DAT); UT gauging and ER probes track it live.",
            "High-TAN crudes (>0.5 mg KOH/g) demand alloy upgrades in hot zones.",
            "API 570/571/580 inspection and API 579 fitness-for-service schedule replacement before failure.",
        ],
        "requirements": [
            "Desalting (the chloride source).",
            "Hydrotreating/hydrocracking (hydrogen and sulfur service).",
            "Basic electrochemistry and metallurgy.",
        ],
        "standards": [
            "API 571 damage mechanisms; API 570 piping inspection; API 580 risk-based inspection.",
            "NACE SP0472 / ISO 15156 materials in sour service.",
        ],
        "citations": [C_MEYERS, C_ROBINSON, C_API_TDB],
        "sig_lens": (
            "Signature take: corrosion is the refinery's slow enemy - "
            "patient, chemical, and utterly honest. His framing treats "
            "the McConomy curves as weather forecasts for steel: read "
            "them, dress the metal accordingly, and never blame the rain."
        ),
    },
    {
        "key": "energy_integration",
        "name": "Energy Integration: Furnaces, Exchangers, and Pinch",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Refining is applied thermodynamics at scale: a large refinery "
            "burns 5 to 8 percent of its crude intake as fuel just to run "
            "itself, so energy integration is pure margin. The crude "
            "preheat train is the showcase - hot product and pump-around "
            "streams heat incoming crude through a network of shell-and-"
            "tube exchangers, recovering tens of megawatts before the "
            "fired heater adds the final lift. Fired heaters (furnaces) "
            "supply the high-temperature heat distillation and reaction "
            "need; their efficiency - typically 85 to 92 percent on a "
            "lower-heating-value basis - is set by stack temperature and "
            "excess air, with air preheaters squeezing the last useful "
            "degrees from flue gas. Pinch analysis is the design science: "
            "composite curves of all hot and cold streams reveal the "
            "pinch point, the minimum temperature approach, and the "
            "theoretical minimum hot and cold utility - any design using "
            "more is wasting fuel by crossing the pinch. Steam systems "
            "tie it together: high-pressure steam raised in waste-heat "
            "boilers drives turbines and lets down through the headers to "
            "reboilers and strippers. Fouling is the eternal tax - "
            "exchangers lose performance as deposits build, and cleaning "
            "schedules are an optimization of their own."
        ),
        "how_it_works": (
            "Each exchanger's duty follows Q = m-dot x cp x delta-T, and "
            "the train is sequenced so the coldest crude meets the "
            "coolest available hot stream first, preserving temperature "
            "driving force - the counter-current principle at network "
            "scale. Furnace efficiency is computed by the stack-loss "
            "method: 100 percent minus dry flue-gas loss (a function of "
            "stack temperature and excess oxygen), moisture loss, and "
            "radiation loss - operators tune excess air to about 10-15 "
            "percent (2-3 percent stack oxygen) balancing complete "
            "combustion against heat carried up the stack. Pinch analysis "
            "constructs hot and cold composite curves on a temperature-"
            "enthalpy diagram; shifting them until the minimum approach "
            "(typically 10-20 F in refineries) sets the utility targets, "
            "and the grand composite curve shows where each steam level "
            "should interface. Exchanger monitoring tracks the fouling "
            "factor: as the overall heat-transfer coefficient decays, "
            "furnace duty rises to compensate - the signal to schedule "
            "cleaning. Steam traps, condensate return, and insulation "
            "complete the unglamorous but lucrative heat-conservation "
            "program."
        ),
        "key_points": [
            "A refinery burns 5-8% of intake as fuel; the crude preheat train recovers tens of MW before the fired heater.",
            "Furnace efficiency (85-92% LHV) is set by stack temperature and excess air - tuned to ~2-3% stack O2.",
            "Pinch analysis (composite curves, minimum approach) computes the theoretical minimum fuel and cooling.",
            "Steam systems cascade high-pressure steam through turbines down to reboiler levels.",
            "Fouling steadily degrades exchangers; cleaning schedules are a margin optimization.",
        ],
        "requirements": [
            "Heat transfer: conduction, convection, Q = m cp dT.",
            "Distillation (the heat loads being integrated).",
            "Basic thermodynamics: enthalpy and efficiency.",
        ],
        "standards": [
            "API 530/560 fired heater design and efficiency testing.",
            "TEMA standards for shell-and-tube exchangers.",
        ],
        "citations": [C_GARY, C_FAHIM, C_API_TDB],
        "sig_lens": (
            "Signature take: pinch analysis is the refinery's diet plan - "
            "every hot stream matched to a cold one, no calorie wasted. "
            "His framing treats the preheat train as the plant's memory: "
            "it never forgets a degree it already paid for."
        ),
    },
    {
        "key": "wastewater",
        "name": "Wastewater Treatment: Cleaning the Refinery's Water",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A refinery is a water factory in reverse: desalters, steam "
            "strippers, cooling towers, and storm runoff generate millions "
            "of gallons of oily, sulfidic, ammonia- and phenol-bearing "
            "wastewater daily, and none of it leaves untreated. Treatment "
            "runs in stages. Primary: API gravity separators - long, "
            "shallow basins where oil floats and solids settle by gravity "
            "alone - remove free oil down to about 100 parts per million. "
            "Secondary: dissolved air flotation (DAF) floats emulsified "
            "oil with microbubbles, and equalization basins smooth the "
            "wild swings of refinery life. Biological treatment - "
            "activated sludge basins full of oil-eating microbes - "
            "biodegrades dissolved organics, phenols, and ammonia to "
            "carbon dioxide, water, and nitrate. Tertiary polishing "
            "(filtration, sometimes granular activated carbon) takes the "
            "effluent to permit limits: typically below 15 ppm oil, "
            "single-digit ammonia, and strict COD, phenol, sulfide, and "
            "metals caps under the NPDES discharge permit. Sour water "
            "strippers upstream keep the worst - H2S and ammonia - out of "
            "the biotreatment, where they would poison the microbes. "
            "Sludges go to dewatering and disposal or coking. Modern "
            "refineries recycle aggressively: treated effluent returns as "
            "cooling tower makeup and wash water, cutting intake toward "
            "near-zero liquid discharge in arid sites."
        ),
        "how_it_works": (
            "The API separator is applied Stokes' law: oil droplets rise "
            "at a velocity set by droplet size and the oil-water density "
            "difference, so basin length and depth are sized for the "
            "design droplet (typically 150 microns) at the design flow - "
            "too fast and droplets carry over. DAF dissolves air under "
            "pressure, then releases it as 30-50 micron bubbles that "
            "attach to oil flocs and float them; chemical coagulants "
            "first break the emulsions. In activated sludge, aeration "
            "basins hold mixed liquor at a controlled food-to-microbe "
            "ratio: the microbes oxidize organics (measured as BOD/COD), "
            "nitrifiers convert ammonia to nitrate, and clarifiers settle "
            "the biomass for recycle - the sludge age, typically 10-20 "
            "days, is the master control. Sour water strippers steam-strip "
            "H2S and ammonia overhead to the sulfur complex before the "
            "water reaches biology. Operators watch oil-in-water, dissolved "
            "oxygen, mixed-liquor suspended solids, and final effluent "
            "toxicity; a refinery upset upstream becomes a treatment-plant "
            "emergency downstream, so the two plants coordinate hourly."
        ),
        "key_points": [
            "Treatment stages: API gravity separation (free oil) -> DAF (emulsified oil) -> activated sludge (dissolved organics) -> polishing.",
            "API separators are sized by Stokes' law for ~150-micron droplets; DAF uses microbubbles + coagulants.",
            "Activated sludge microbes biodegrade phenols, organics, and ammonia; sludge age (10-20 days) is the master control.",
            "Sour water strippers keep H2S/ammonia out of biotreatment, where they would poison the microbes.",
            "NPDES permits cap oil, COD, ammonia, phenols, sulfides, metals; recycle pushes toward near-zero discharge.",
        ],
        "requirements": [
            "Desalting (a major wastewater source).",
            "Amine/sulfur recovery (where stripped H2S goes).",
            "Basic microbiology and Stokes' law.",
        ],
        "standards": [
            "EPA NPDES refinery effluent guidelines (40 CFR 419).",
            "API 42102 / separator design practice.",
        ],
        "citations": [C_ROBINSON, C_EPA_NSPS, C_MEYERS],
        "sig_lens": (
            "Signature take: the treatment plant is the refinery's kidney - "
            "filtering the process blood, feeding the microbes, returning "
            "clean water. His framing respects the activated sludge most: "
            "trillions of invisible workers, and the whole permit depends "
            "on their appetite."
        ),
    },
    {
        "key": "catalysts",
        "name": "Catalysts: The Refinery's Invisible Workforce",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Nothing in a modern refinery works without catalysts - the "
            "invisible workforce that makes reactions fast, selective, "
            "and possible at sane conditions. Zeolite Y, the faujasite "
            "crystal with its molecular cages and strong acid sites, "
            "cracks gas oil in the FCC; ZSM-5 additive boosts propylene "
            "and octane. Amorphous silica-alumina and zeolites pair with "
            "nickel-molybdenum and nickel-tungsten sulfides in "
            "hydrocracking and hydrotreating; cobalt-molybdenum favors "
            "desulfurization while nickel-molybdenum favors "
            "denitrogenation and aromatic saturation. Platinum-rhenium "
            "and platinum-tin reform naphtha; platinum on chlorided "
            "alumina or zeolite isomerizes light paraffins. Catalysts die "
            "three deaths: coking (carbon covers the sites - reversible "
            "by burning), poisoning (sulfur, nitrogen, metals, arsenic "
            "bind permanently or semi-permanently), and sintering or "
            "dealumination (heat collapses the structure - irreversible). "
            "Management is an economic art: FCC catalyst is added and "
            "withdrawn continuously to hold equilibrium activity; fixed "
            "beds run cycles of one to several years between "
            "regenerations; and spent catalyst - tons of metals-bearing "
            "solid - is reclaimed or disposed as hazardous waste. A "
            "catalyst selection can swing a unit's margin by millions: "
            "activity, selectivity, stability - pick two is the old joke, "
            "and the industry spends billions chasing all three."
        ),
        "how_it_works": (
            "Activity is measured as the rate constant for a standard "
            "test reaction; selectivity as the desired product's share; "
            "stability as the deactivation rate - typically modeled as "
            "first-order decay of activity with time on stream or with "
            "coke laid down. In the FCC, fresh catalyst makeup rate sets "
            "the equilibrium between fresh high-activity and aged "
            "metals-laden inventory: more makeup raises conversion but "
            "costs catalyst dollars, and nickel from resid feed "
            "specifically boosts unwanted coke and hydrogen - antimony or "
            "bismuth passivation ties the nickel up. Fixed-bed "
            "hydroprocessing catalysts are sulfided in situ (the oxide "
            "precursor converts to the active metal sulfide under H2S) "
            "and run until pressure drop, activity loss, or the turnaround "
            "schedule forces changeout; some units regenerate by "
            "controlled coke burn. Guard beds - cheap sacrificial catalyst "
            "or adsorbents upstream - catch silicon, arsenic, and metals "
            "before they reach the expensive main bed. Catalyst vendors "
            "qualify products in pilot plants and in commercial "
            "'trial and monitor' runs, with performance guarantees tied "
            "to the refiner's actual feed."
        ),
        "key_points": [
            "Key families: zeolite Y (FCC), ZSM-5 (propylene/octane additive), Ni-Mo/Co-Mo (hydroprocessing), Pt-Re/Pt-Sn (reforming), Pt/chlorided alumina (isomerization).",
            "Catalysts die by coking (reversible), poisoning (S, N, metals, As), and sintering/dealumination (irreversible).",
            "FCC equilibrium activity is managed by continuous makeup; fixed beds run 1+ year cycles between regenerations.",
            "Nickel contamination boosts coke and hydrogen - passivation or higher makeup counters it.",
            "Guard beds sacrifice themselves to protect expensive main-bed catalyst from silicon, arsenic, and metals.",
        ],
        "requirements": [
            "The FCC, hydrocracking, reforming, and isomerization records (the catalyst users).",
            "Catalysis: active sites, deactivation kinetics.",
            "Basic inorganic chemistry (zeolites, transition metals).",
        ],
        "standards": [
            "ASTM D5758/D3907 microactivity testing for FCC catalyst.",
            "Vendor qualification and performance-guarantee practice.",
        ],
        "citations": [C_SADEGHBEIGI, C_ANCHEYTA, C_MEYERS],
        "sig_lens": (
            "Signature take: catalysts are the refinery's quiet geniuses - "
            "tons of powder doing the thinking for millions of barrels. "
            "His framing treats equilibrium catalyst like a sports roster: "
            "rookies in, veterans out, and the coach watching the metals "
            "like injuries."
        ),
    },
]
