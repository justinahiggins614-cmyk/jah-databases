#!/usr/bin/env python3
"""Entries for the Unsolved Chemical Engineering databases (Manon 16:15 orders, batch 1).

34 famous unsolved chemical-engineering problems, ladder-ordered by
accessibility (rank 1 = most approachable, rank 34 = most complex).
Public half = fact-checked problems; signature half = the same problems
with the Signature system's proposed solution approach, titles suffixed
" (Signature Edition)", src signature, clearly labeled Signature-made.

Field scope: direct air capture at scale, green ammonia and steel,
plastic upcycling chemistry, continuous pharmaceutical manufacturing,
desalination energy floors, and the wider unsolved problems of the
discipline.

ID prefixes: JAH-USKE- (public) and JAH-USKES- (signature), verified free
2026-10-17 in the manifest id_prefix values and across all shard index
files (zero hits).

Honesty rule (series canon): the signature_solution OPENS WITH THE EXACT
LABEL "Signature-generated proposed solution - not established science."
Never claim proof, never imply peer acceptance, never present speculation
as settled.

Citations are real publications/editions (textbooks, reviews, landmark
papers). Never the words "bat belt" anywhere. No website references.
No Facebook.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature original - his original Signature solution approach: "
            "every unsolved problem treated as a covenant of evidence, the "
            "solution path walked step by step with adjustable assumptions "
            "and a confirm-or-refute panel. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_LEVENSPIEL = ("Levenspiel O. Chemical Reaction Engineering. 3rd ed. "
                  "Wiley; 1999.")
CIT_SATTERFIELD = ("Satterfield CN. Heterogeneous Catalysis in Industrial "
                   "Practice. 2nd ed. McGraw-Hill; 1991.")
CIT_SEADER = ("Seader JD, Henley EJ, Roper DK. Separation Process Principles. "
              "4th ed. Wiley; 2016.")
CIT_SMITH_DESIGN = ("Smith R. Chemical Process Design and Integration. "
                    "2nd ed. Wiley; 2016.")
CIT_TOWLER = ("Towler G, Sinnott R. Chemical Engineering Design. 2nd ed. "
              "Butterworth-Heinemann; 2012.")
CIT_SMIL = ("Smil V. Enriching the Earth: Fritz Haber, Carl Bosch, and the "
            "Transformation of World Food Production. MIT Press; 2001.")
CIT_KEITH = ("Keith DW, Holmes G, St Angelo D, Heidel K. A process for "
             "capturing CO2 from the atmosphere. Joule 2, 1573-1594; 2018.")
CIT_FASIHI = ("Fasihi M, Efimova O, Breyer C. Techno-economic assessment of "
              "CO2 direct air capture plants. Journal of Cleaner Production "
              "224, 957-980; 2019.")
CIT_GEYER = ("Geyer R, Jambeck JR, Law KL. Production, use, and fate of all "
             "plastics ever made. Science Advances 3, e1700782; 2017.")
CIT_RAGAERT = ("Ragaert K, Delva L, Van Geem K. Mechanical and chemical "
               "recycling of solid plastic waste. Waste Management 69, 24-58; "
               "2017.")
CIT_COATES = ("Coates GW, Getzler YDL. Chemical recycling to monomer for an "
              "ideal, circular polymer economy. Nature Reviews Materials 5, "
              "501-516; 2020.")
CIT_JEHANNO = ("Jehanno C et al. Critical advances and future opportunities "
               "in upcycling commodity polymers. Nature 603, 803-814; 2022.")
CIT_LEE_PHARMA = ("Lee SL et al. Modernizing pharmaceutical manufacturing: "
                  "from batch to continuous production. Journal of "
                  "Pharmaceutical Innovation 10, 191-199; 2015.")
CIT_ELIMELECH = ("Elimelech M, Phillip WA. The future of seawater "
                 "desalination: energy, technology, and the environment. "
                 "Science 333, 712-717; 2011.")
CIT_VOUTCHKOV = ("Voutchkov N. Desalination Engineering: Planning and "
                 "Design. McGraw-Hill; 2013.")
CIT_LEWIS_NOCERA = ("Lewis NS, Nocera DG. Powering the planet: Chemical "
                    "challenges in solar energy utilization. Proceedings of "
                    "the National Academy of Sciences 103, 15729-15735; 2006.")
CIT_BARBER = ("Barber J. Photosynthetic energy conversion: natural and "
              "artificial. Chemical Society Reviews 38, 185-196; 2009.")
CIT_DAVIS = ("Davis SJ et al. Net-zero emissions energy systems. Science "
             "360, eaas9793; 2018.")
CIT_ALLWOOD = ("Allwood JM, Cullen JM. Sustainable Materials: With Both Eyes "
               "Open. UIT Cambridge; 2012.")
CIT_ROCHELLE = ("Rochelle GT. Amine scrubbing for CO2 capture. Science 325, "
                "1652-1654; 2009.")
CIT_BUI = ("Bui M et al. Carbon capture and storage (CCS): the way forward. "
           "Energy and Environmental Science 11, 1062-1176; 2018.")
CIT_HAUCH = ("Hauch A et al. Recent advances in solid oxide cell technology "
             "for electrolysis. Science 370, eaba6118; 2020.")
CIT_DELUNA = ("De Luna P et al. What would it take for renewably powered "
              "electrosynthesis to displace petrochemical processes? Science "
              "364, eaav3506; 2019.")
CIT_ARESTA = ("Aresta M, Dibenedetto A, Angelini A. Catalysis for the "
              "valorization of exhaust carbon: from CO2 to chemicals and "
              "fuels. Chemical Reviews 114, 1709-1742; 2014.")
CIT_STANKIEWICZ = ("Stankiewicz AI, Moulijn JA. Process intensification: "
                   "transforming chemical engineering. Chemical Engineering "
                   "Progress 96(1), 22-34; 2000.")
CIT_JENSEN = ("Jensen KF. Microreaction engineering - is small better? "
              "Chemical Engineering Science 56, 293-303; 2001.")
CIT_EHRFELD = ("Ehrfeld W, Hessel V, Loewe H. Microreactors. Wiley-VCH; 2000.")
CIT_FRIDMAN = ("Fridman A. Plasma Chemistry. Cambridge University Press; "
               "2008.")
CIT_ZAKZESKI = ("Zakzeski J, Bruijnincx PCA, Jongerius AL, Weckhuysen BM. The "
                "catalytic valorization of lignin for the production of "
                "renewable chemicals. Chemical Reviews 110, 3552-3599; 2010.")
CIT_RAGAUSKAS = ("Ragauskas AJ et al. Lignin valorization: improving lignin "
                 "processing in the biorefinery. Science 344, 1246843; 2014.")
CIT_EISAMAN = ("Eisaman MD et al. CO2 extraction from seawater using bipolar "
               "membrane electrodialysis. Energy and Environmental Science 5, "
               "7346-7352; 2012.")
CIT_STEPHANOPOULOS = ("Stephanopoulos G, Reklaitis GV. Process systems "
                      "engineering: from Solvay to modern bio- and "
                      "nanotechnology. Chemical Engineering Science 66, "
                      "4272-4292; 2011.")
CIT_VENKAT = ("Venkatasubramanian V. The promise of artificial intelligence "
              "in chemical engineering. AIChE Journal 65, e16430; 2019.")
CIT_NIELSEN = ("Nielsen J, Keasling JD. Engineering cellular metabolism. "
               "Cell 164, 1185-1197; 2016.")
CIT_CHU = ("Chu S, Cui Y, Liu N. The path towards sustainable energy. "
           "Nature Materials 16, 16-22; 2016.")
CIT_CUSSLER = ("Cussler EL, Moggridge GD. Chemical Product Design. 2nd ed. "
               "Cambridge University Press; 2011.")

ENTRIES = [
    {
        "key": "fertilizer_energy",
        "name": "Why Is Making Fertilizer So Energy-Hungry?",
        "group": "Approachable",
        "ladder_rank": 1,
        "ladder_tier": "approachable",
        "problem": (
            "Half the nitrogen in your body passed through the Haber-Bosch "
            "process, and that process eats roughly 1 to 2 percent of all "
            "human energy use. Nitrogen gas is famously unreactive - its "
            "triple bond is one of the strongest in chemistry - so breaking "
            "it demands 400 to 500 degrees Celsius and 150 to 300 atmospheres "
            "of pressure, sustained day and night in giant plants fed by "
            "natural gas. The unsolved problem: how to fix nitrogen into "
            "ammonia at mild conditions, with renewable energy, at a cost "
            "that can feed the world without cooking the climate."
        ),
        "background": (
            "Fritz Haber demonstrated ammonia synthesis from nitrogen and "
            "hydrogen in 1909; Carl Bosch scaled it at BASF by 1913, solving "
            "the materials and catalyst problems of extreme pressure. Vaclav "
            "Smil's history shows the process now makes about 180 million "
            "tonnes of ammonia a year and underwrites roughly half of global "
            "food production. The iron-based catalyst is essentially the one "
            "Mittasch discovered a century ago, improved but not replaced. "
            "Decades of catalyst research, including ruthenium systems and "
            "electride-supported catalysts, have shaved the conditions only "
            "at the margins. The energy bill - mostly the hydrogen made from "
            "natural gas - remains, and with it about 1.5 percent of global "
            "carbon dioxide emissions."
        ),
        "why_it_matters": (
            "Fertilizer is food. Any route to ammonia that runs on "
            "electricity instead of gas would decarbonize one of industry's "
            "largest emission sources and let fertilizer be made wherever "
            "there is sun, wind, and air - including regions that today "
            "depend on imported gas. Solving it rewrites the economics of "
            "farming and the carbon ledger of civilization at once."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the energy-ledger model of nitrogen fixation, and "
            "the confirm-or-refute panel. In one line: the Signature approach "
            "treats the triple bond as an energy ledger - counting every "
            "kilojoule from N2 to NH3 - and proposes the coupled "
            "plasma-catalyst experiment that would decide whether mild-"
            "condition fixation can ever beat Haber-Bosch on energy."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats nitrogen fixation as an "
            "energy ledger problem: every proposed route must beat roughly "
            "30 gigajoules per tonne of ammonia, the modern plant benchmark, "
            "and the ledger must be drawn from N2 in the air to NH3 in the "
            "tank with no hidden subsidies.\\n\\n"
            "ASSUMPTIONS: (1) The comparison basis is one tonne of ammonia "
            "delivered at fertilizer grade. (2) Electricity is counted at its "
            "real cost including intermittency; hydrogen is counted at its "
            "real production energy. (3) Catalyst lifetime is counted - a "
            "catalyst that dies in a week is not a solution. (4) The triple "
            "bond dissociation energy, 945 kilojoules per mole of N2, is the "
            "floor no chemistry can duck.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Draw the ledger: the "
            "reaction N2 + 3H2 -> 2NH3 releases 92 kJ per mole of N2, yet "
            "plants consume about 30 GJ per tonne because making the hydrogen "
            "and fighting the kinetic barrier costs far more than the "
            "thermodynamics demand. Step 2 - Split the bill: separate the "
            "hydrogen cost from the activation cost; any challenger must say "
            "which half it attacks. Step 3 - Test each family against the "
            "ledger: thermal catalysis, electrochemical nitrogen reduction, "
            "plasma activation, photochemical routes. Step 4 - Apply the "
            "lifetime filter: divide claimed energy by demonstrated catalyst "
            "hours.\\n\\n"
            "PROPOSED MECHANISM: the ledger shows the activation half is the "
            "smaller prize and the hydrogen half the larger - so the highest-"
            "leverage path is green hydrogen feeding an improved thermal "
            "loop first, with plasma-assisted or electrochemical routes as "
            "the long bet. The demo walks the ledger numerically and shows "
            "how the numbers move as each assumption changes.\\n\\n"
            "WHAT WOULD CONFIRM IT: a published full-ledger comparison in "
            "which an alternative route beats 30 GJ per tonne including "
            "hydrogen production and catalyst replacement. WHAT WOULD KILL "
            "IT: a route that wins on paper but collapses once hydrogen cost "
            "and catalyst lifetime enter the ledger - or a demonstration that "
            "no activation method undercuts the thermal barrier by the "
            "needed factor.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim Haber-Bosch is "
            "obsolete, does not claim any single alternative wins today, and "
            "does not claim the ledger constants are universal - local "
            "electricity prices move the winner."
        ),
        "key_points": [
            "Haber-Bosch consumes 1-2% of world energy and emits about 1.5% of global CO2, all to break nitrogen's triple bond.",
            "The reaction itself releases energy; the cost is almost entirely making hydrogen and overcoming the kinetic barrier at 400-500 C and 150-300 bar.",
            "The catalyst is essentially a century-old iron formulation, improved but never replaced.",
            "Any challenger must beat roughly 30 GJ per tonne of ammonia on a full ledger - hydrogen cost and catalyst lifetime included.",
            "The Signature approach draws that ledger step by step and proposes the decisive comparison experiment.",
        ],
        "citations": [CIT_SMIL, CIT_SATTERFIELD],
    },
    {
        "key": "dac_intro",
        "name": "Why Can't We Just Pull CO2 Out of the Air?",
        "group": "Approachable",
        "ladder_rank": 2,
        "ladder_tier": "approachable",
        "problem": (
            "Carbon dioxide is only about 420 parts per million of air - "
            "roughly one molecule in 2,400. To capture a tonne of it, a "
            "machine must process well over a million cubic metres of air, "
            "find the rare CO2 molecules, and then spend energy releasing "
            "them from whatever caught them. The unsolved problem: how to do "
            "this at a cost anywhere near what the climate math requires - "
            "on the order of one hundred dollars a tonne - when today's "
            "plants cost several times that and the thermodynamic minimum is "
            "set by the sheer dilution."
        ),
        "background": (
            "Direct air capture was a laboratory curiosity until Klaus "
            "Lackner's early-2000s work framed it as a serious climate "
            "option. David Keith's 2018 Joule paper described a full "
            "industrial process - air contactor, pellet reactor, calciner - "
            "and estimated costs falling toward one hundred dollars a tonne "
            "at scale. Companies built pilot and commercial plants in the "
            "2010s and 2020s using two main chemistries: liquid hydroxide "
            "solvents regenerated at about 900 C, and solid amine sorbents "
            "regenerated with low-grade heat. Techno-economic studies, "
            "notably Fasihi's 2019 assessment, put realistic near-term costs "
            "several hundred dollars per tonne. The gap between promise and "
            "plant remains the field's central tension."
        ),
        "why_it_matters": (
            "Most climate pathways that hold warming near 1.5 C assume "
            "billions of tonnes of CO2 removal per year by mid-century. "
            "There is no other technology that can address dispersed and "
            "historical emissions at that scale. If direct air capture cannot "
            "get cheap, those pathways collapse - so the cost curve of this "
            "one machine is a climate variable."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the dilution-energy model, and the confirm-or-"
            "refute panel. In one line: the Signature approach computes the "
            "unavoidable energy price of 420-ppm dilution and proposes the "
            "sorbent-cycle experiment that would decide whether any chemistry "
            "can close the gap to one hundred dollars a tonne."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats direct air capture as a "
            "dilution tax problem: the physics of 420 ppm sets a minimum "
            "energy bill, and every real plant pays a multiple of it. The "
            "question is whether the multiple can shrink far enough.\\n\\n"
            "ASSUMPTIONS: (1) Ambient air at 420 ppm CO2, 25 C. (2) The "
            "minimum separation work is RT ln(1/420e-6) per mole of CO2, "
            "about 19 kJ per mole or 0.44 GJ per tonne. (3) Regeneration "
            "energy dominates real plants; fan energy is secondary but not "
            "negligible. (4) Costs are counted per tonne net of the plant's "
            "own emissions.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Compute the dilution "
            "tax: over 1.3 million cubic metres of air per tonne of CO2, and "
            "a thermodynamic floor near 0.44 GJ per tonne. Step 2 - Measure "
            "the multiple: today's plants spend roughly 5 to 9 GJ per tonne, "
            "a multiple of 10 to 20 over the floor. Step 3 - Decompose the "
            "multiple into sorbent binding energy, sensible heating of "
            "equipment, and incomplete recovery. Step 4 - Ask which terms "
            "scale down with learning and which are chemistry-locked.\\n\\n"
            "PROPOSED MECHANISM: the binding-energy term is the softest "
            "target - sorbents that release CO2 with smaller temperature or "
            "pressure swings attack the biggest slice of the multiple. The "
            "demo walks the numbers and shows how the cost moves as sorbent "
            "working capacity and cycle energy change.\\n\\n"
            "WHAT WOULD CONFIRM IT: a sorbent-plant combination demonstrating "
            "under 3 GJ per tonne total energy at pilot scale with measured "
            "degradation rates. WHAT WOULD KILL IT: a proof that the "
            "sensible-heat and binding terms cannot jointly fall below the "
            "cost target no matter the sorbent - the dilution tax is simply "
            "too steep.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim any current plant is "
            "economic, does not claim the thermodynamic floor is reachable, "
            "and does not claim costs will fall on any schedule."
        ),
        "key_points": [
            "At 420 ppm, capturing one tonne of CO2 means processing over 1.3 million cubic metres of air.",
            "The thermodynamic minimum work is only about 0.44 GJ per tonne - but real plants spend 5-9 GJ per tonne.",
            "The gap is a multiple of 10-20 over the floor, dominated by sorbent regeneration energy.",
            "Two chemistries lead: liquid hydroxides regenerated near 900 C, and solid amines regenerated with low-grade heat.",
            "The Signature approach decomposes the multiple and targets the binding-energy term as the softest.",
        ],
        "citations": [CIT_KEITH, CIT_FASIHI],
    },
    {
        "key": "green_steel_intro",
        "name": "Why Is Iron Still Made With Coal?",
        "group": "Approachable",
        "ladder_rank": 3,
        "ladder_tier": "approachable",
        "problem": (
            "Every tonne of steel made the classic way - the blast furnace - "
            "emits roughly 1.8 tonnes of CO2, because carbon is both the "
            "fuel and the chemical that rips oxygen off iron ore. Steel is "
            "about 8 percent of global CO2 emissions, and demand keeps "
            "rising. The unsolved problem: how to make iron without carbon "
            "as the reductant - with hydrogen, electricity, or something "
            "entirely new - at the scale of nearly two billion tonnes a "
            "year and at a price the world will pay."
        ),
        "background": (
            "The blast furnace is a medieval technology perfected: coke "
            "reduces iron ore at around 1500 C while supplying the heat. "
            "Direct reduced iron (DRI) plants, which use natural gas instead "
            "of coke, cut emissions roughly in half and have operated for "
            "decades. The green-steel push of the 2020s aims to swap the gas "
            "for hydrogen made with renewable electricity - the HYBRIT "
            "project in Sweden produced its first fossil-free sponge iron in "
            "2021. Allwood and Cullen's materials analysis shows the deeper "
            "issue: even with clean ironmaking, the sheer scale of steel "
            "demand means efficiency, scrap use, and longer-lived products "
            "must carry part of the load."
        ),
        "why_it_matters": (
            "Steel is the skeleton of civilization - buildings, bridges, "
            "cars, wind turbines. There is no decarbonization without "
            "decarbonized steel, and no substitute material at anything like "
            "its scale and price. Cracking green steel unlocks the "
            "construction of the clean-energy future itself."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the reductant ledger, and the confirm-or-refute "
            "panel. In one line: the Signature approach counts the "
            "kilograms of hydrogen and megawatt-hours per tonne of iron for "
            "every carbon-free route and proposes the pilot-plant "
            "comparison that would decide which route scales."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats green steel as a "
            "reductant ledger: every route must supply the oxygen-removal "
            "chemistry and the heat, and the ledger decides which route can "
            "plausibly reach two billion tonnes a year.\\n\\n"
            "ASSUMPTIONS: (1) Comparison basis is one tonne of crude steel at "
            "today's quality grades. (2) Hydrogen is counted at 50 kWh per "
            "kilogram, the realistic electrolyzer figure, not the "
            "thermodynamic ideal. (3) Ore quality is held constant - "
            "hydrogen DRI needs high-grade ore, and ore grade is a "
            "constraint, not a footnote. (4) Grid electricity is counted "
            "with its real carbon intensity unless dedicated renewables are "
            "contracted.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Write the chemistry: "
            "Fe2O3 + 3H2 -> 2Fe + 3H2O needs about 60 kg of hydrogen per "
            "tonne of iron in theory; practice needs more. Step 2 - Price "
            "the hydrogen: at 50 kWh per kg, that is 3 MWh per tonne of "
            "steel before heat and rolling. Step 3 - Audit the ore "
            "constraint: hydrogen DRI demands pellet-grade ore, which is a "
            "minority of supply. Step 4 - Compare the ledger against "
            "alternatives: molten oxide electrolysis, hydrogen plasma, and "
            "the scrap-electric-arc route.\\n\\n"
            "PROPOSED MECHANISM: the ore-grade constraint is the binding one "
            "most analyses underweight - so the highest-leverage work is "
            "routes tolerant of lower-grade ore, plus scrap maximization. "
            "The demo walks the ledger numerically.\\n\\n"
            "WHAT WOULD CONFIRM IT: a hydrogen-DRI plant publishing full ore-"
            "grade, energy, and cost data at commercial scale. WHAT WOULD "
            "KILL IT: ore-grade limits capping hydrogen DRI far below "
            "replacement scale, or electricity prices holding green steel "
            "permanently above the blast-furnace cost plus carbon price.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim hydrogen steel is "
            "economic today, does not claim ore constraints are solved, and "
            "does not claim any single route wins."
        ),
        "key_points": [
            "Blast-furnace steel emits about 1.8 tonnes of CO2 per tonne of steel - roughly 8% of global emissions.",
            "Hydrogen can replace carbon as the reductant, but needs about 60 kg H2 per tonne of iron in theory - 3 MWh of electricity per tonne of steel in practice.",
            "Hydrogen-based ironmaking demands high-grade ore, which is a minority of world supply.",
            "Scrap-fed electric arc furnaces are already clean-ish, but scrap supply caps their share.",
            "The Signature approach ledgers every route on hydrogen, heat, ore grade, and cost.",
        ],
        "citations": [CIT_ALLWOOD, CIT_DAVIS],
    },
    {
        "key": "plastic_waste",
        "name": "Why Do We Throw Away Most Plastic Instead of Recycling It?",
        "group": "Approachable",
        "ladder_rank": 4,
        "ladder_tier": "approachable",
        "problem": (
            "Of the roughly 400 million tonnes of plastic made each year, "
            "Geyer's landmark accounting found only about 9 percent has ever "
            "been recycled; most is landfilled, incinerated, or leaked to "
            "the environment. The chemistry is the obstacle: mechanical "
            "recycling shreds and remelts plastic, and each cycle shortens "
            "the polymer chains, so quality falls - downcycling, not "
            "recycling. Mixed, dirty, multi-layer plastics defeat sorting "
            "entirely. The unsolved problem: a chemistry that turns waste "
            "plastic back into virgin-quality material, economically, at "
            "planetary scale."
        ),
        "background": (
            "Plastics recycling began with simple remelting in the 1970s, "
            "and the resin identification codes stamped on packaging date to "
            "1988 - a sorting aid, not a solution. Ragaert's 2017 review "
            "documents why mechanical recycling stalls: contamination, "
            "polymer mixing, and chain degradation. Chemical recycling - "
            "pyrolysis, gasification, solvolysis - breaks polymers back to "
            "monomers or feedstocks, but historically at high energy cost "
            "and poor selectivity. The 2020s brought new catalysts: Coates "
            "and Getzler's review frames the ideal of chemical recycling to "
            "monomer, and Jehanno's 2022 Nature review surveys catalytic "
            "upcycling routes that aim above virgin quality rather than "
            "below it."
        ),
        "why_it_matters": (
            "Plastic waste is a materials tragedy and an environmental one - "
            "oceans, food chains, microplastics. Virgin plastic is cheap "
            "because oil is cheap; until recycled or upcycled material can "
            "compete on price and quality, the waste stream grows by "
            "hundreds of millions of tonnes a year. Solving the chemistry "
            "turns the world's largest waste stream into a feedstock."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the chain-length ledger, and the confirm-or-refute "
            "panel. In one line: the Signature approach models recycling as "
            "a chain-length ledger - every cycle must preserve or restore "
            "molecular weight - and proposes the mixed-stream experiment "
            "that would decide whether catalytic routes beat sorting plus "
            "remelting."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats plastic recycling as a "
            "chain-length ledger: mechanical recycling shortens chains, and "
            "only chemistry that restores chain length counts as true "
            "recycling. Everything else is delayed landfilling.\\n\\n"
            "ASSUMPTIONS: (1) Comparison basis is one tonne of mixed "
            "post-consumer packaging plastic. (2) 'Recycled' means "
            "molecular weight and properties within 10 percent of virgin. "
            "(3) Contamination levels are real-world, not laboratory-clean. "
            "(4) Energy and catalyst cost are counted in the ledger.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Measure the decay: each "
            "mechanical cycle cuts average chain length; after two to three "
            "cycles the material is unusable for its original purpose. Step "
            "2 - Test the chemical routes: pyrolysis gives mixed oils, "
            "glycolysis targets PET, hydrogenolysis can be selective - each "
            "audited for selectivity and energy. Step 3 - Price the "
            "sorting: no chemical route escapes the mixed-stream problem; "
            "sorting cost enters every ledger. Step 4 - Check the "
            "upcycling premium: routes that make higher-value products can "
            "afford costlier chemistry.\\n\\n"
            "PROPOSED MECHANISM: selective catalytic depolymerization back "
            "to monomer is the only route that truly closes the loop; "
            "pyrolysis to fuel is downcycling with extra steps. The demo "
            "walks the chain-length ledger and the cost comparison.\\n\\n"
            "WHAT WOULD CONFIRM IT: a mixed-stream plant publishing "
            "monomer yield, energy, and cost per tonne with third-party "
            "audit. WHAT WOULD KILL IT: catalyst poisoning by real-world "
            "contaminants proving unavoidable at scale, or energy costs "
            "holding chemical recycling permanently above virgin resin "
            "prices.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim mechanical recycling "
            "is worthless, does not claim any chemical route is economic "
            "today, and does not claim sorting can be skipped."
        ),
        "key_points": [
            "Only about 9% of all plastic ever made has been recycled; each mechanical cycle shortens polymer chains.",
            "Mixed, dirty, multi-layer plastics defeat both sorting and simple remelting.",
            "Chemical recycling breaks polymers to monomers or oils, but historically at high energy cost and poor selectivity.",
            "True recycling must restore chain length - selective depolymerization to monomer is the bar.",
            "The Signature approach ledgers chain length, sorting cost, energy, and catalyst lifetime together.",
        ],
        "citations": [CIT_GEYER, CIT_RAGAERT, CIT_COATES, CIT_JEHANNO],
    },
    {
        "key": "pharma_cost",
        "name": "Why Are Medicines So Expensive to Manufacture?",
        "group": "Approachable",
        "ladder_rank": 5,
        "ladder_tier": "approachable",
        "problem": (
            "Most drugs are still made the way they were a century ago: in "
            "batches, one giant kettle at a time, with each step stopped, "
            "tested, cleaned, and restarted. Batch plants sit idle between "
            "steps, waste is enormous - the pharmaceutical E-factor, "
            "kilograms of waste per kilogram of product, runs 25 to 100 or "
            "more - and quality is tested after the fact, so whole batches "
            "get scrapped. The unsolved problem: how to manufacture drugs "
            "continuously, like an oil refinery makes fuel, with quality "
            "built in and verified in real time."
        ),
        "background": (
            "Batch manufacturing dominates pharma for regulatory reasons as "
            "much as technical ones: regulators approved batch processes, "
            "and changing an approved process is expensive. The FDA began "
            "actively encouraging continuous manufacturing in the 2010s; "
            "Lee's 2015 review lays out the agency's modernization push. "
            "Early continuous lines - notably for drugs like Vertex's "
            "Orkambi and later Janssen's Prezista - proved the concept: "
            "smaller footprint, faster throughput, tighter control. But the "
            "industry remains overwhelmingly batch. The hard parts are "
            "real-time quality measurement, handling solids in flow, and "
            "revalidating decades of batch know-how."
        ),
        "why_it_matters": (
            "Manufacturing cost is a large slice of drug prices, and batch "
            "failures cause the shortages that empty pharmacy shelves. "
            "Continuous plants could be smaller, cheaper, faster to build, "
            "and more reliable - and could make essential medicines locally "
            "instead of in a handful of distant mega-plants. It is a "
            "resilience problem as much as a cost problem."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the waste ledger, and the confirm-or-refute panel. "
            "In one line: the Signature approach counts the E-factor "
            "kilogram by kilogram and proposes the solids-handling "
            "experiment that would decide whether continuous lines can take "
            "over mainstream drug production."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats pharma manufacturing as "
            "a waste ledger: every kilogram of waste per kilogram of drug "
            "is counted by step, and continuous processing must beat batch "
            "on the ledger, not just in principle.\\n\\n"
            "ASSUMPTIONS: (1) Comparison basis is one kilogram of finished "
            "active ingredient at pharmacopeia purity. (2) The E-factor "
            "counts solvents, failed batches, and cleaning - everything. "
            "(3) Regulatory revalidation cost is a real term in the ledger. "
            "(4) Solids handling - crystallization, filtration, drying - is "
            "the binding technical constraint.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Audit a batch route "
            "step by step: solvents dominate the E-factor, often 80 percent "
            "or more. Step 2 - Map each unit operation to its continuous "
            "equivalent: flow reactors for synthesis exist; continuous "
            "crystallization and filtration are the frontier. Step 3 - "
            "Price the control layer: process analytical technology must "
            "verify quality in real time or the line cannot run. Step 4 - "
            "Add the regulatory term: the ledger must include revalidation "
            "or the comparison is fantasy.\\n\\n"
            "PROPOSED MECHANISM: solvent recovery and continuous "
            "crystallization are the two highest-leverage targets - they "
            "attack the largest waste terms. The demo walks the E-factor "
            "ledger for a batch versus continuous route.\\n\\n"
            "WHAT WOULD CONFIRM IT: a continuous line publishing full "
            "E-factor, cost, and rejection-rate data beating its batch "
            "predecessor for the same molecule. WHAT WOULD KILL IT: solids "
            "handling proving fundamentally unreliable in flow for complex "
            "molecules, or regulatory costs permanently erasing the "
            "operating advantage.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim batch is obsolete, "
            "does not claim continuous fits every molecule, and does not "
            "claim the regulatory term can be wished away."
        ),
        "key_points": [
            "Pharma's E-factor runs 25-100+ kg of waste per kg of drug, mostly solvents, with whole batches scrapped on failure.",
            "Continuous manufacturing promises smaller plants, less waste, and real-time quality - the FDA has pushed it since the 2010s.",
            "Solids handling (crystallization, filtration, drying) in flow is the binding technical constraint.",
            "Regulatory revalidation cost is a real term that most technical comparisons omit.",
            "The Signature approach ledgers waste, control cost, and regulation step by step.",
        ],
        "citations": [CIT_LEE_PHARMA, CIT_CUSSLER],
    },
    {
        "key": "desalination_energy",
        "name": "Why Is Desalination So Energy-Hungry?",
        "group": "Approachable",
        "ladder_rank": 6,
        "ladder_tier": "approachable",
        "problem": (
            "Taking the salt out of seawater sounds simple, but physics "
            "charges a toll: separating salt from water fights entropy, and "
            "the thermodynamic minimum for seawater is about 1 kilowatt-"
            "hour per cubic metre. Real reverse-osmosis plants use three to "
            "four times that, and thermal plants far more. The unsolved "
            "problem: how close to the thermodynamic floor can real "
            "desalination get, and is there any fundamentally different "
            "separation - not pressure, not heat - that rewrites the floor "
            "itself?"
        ),
        "background": (
            "Desalination scaled up in the oil-rich 1960s with thermal "
            "distillation; reverse osmosis took over from the 1980s as "
            "membranes improved, and today RO dominates new capacity. "
            "Elimelech and Phillip's 2011 Science review framed the field's "
            "central question as energy: RO had already captured most of the "
            "easy gains, and further progress needed new membrane "
            "chemistries or new process configurations. Voutchkov's design "
            "handbook documents the practical plant: pretreatment, high-"
            "pressure pumps, energy recovery devices, and brine disposal - "
            "each a cost and an energy term. The thermodynamic minimum "
            "itself depends on recovery rate, which is why the floor is a "
            "curve, not a number."
        ),
        "why_it_matters": (
            "Two billion people face water stress, and desalination is the "
            "only rainfall-independent water source. Energy is most of its "
            "cost - so the energy floor is the water price. Every fraction "
            "of a kilowatt-hour shaved off a cubic metre multiplies across "
            "the tens of millions of cubic metres desalinated daily."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the entropy ledger, and the confirm-or-refute "
            "panel. In one line: the Signature approach computes the true "
            "thermodynamic floor as a function of recovery and proposes "
            "the membrane experiment that would decide how much of the "
            "remaining gap is closable."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats desalination as an "
            "entropy ledger: the minimum work is fixed by thermodynamics, "
            "and every real plant pays a multiple of it. The honest "
            "question is which parts of the multiple are removable.\\n\\n"
            "ASSUMPTIONS: (1) Seawater at 35 grams per litre, 25 C. (2) The "
            "minimum work at 50 percent recovery is about 1.06 kWh per cubic "
            "metre of product - and it rises steeply with recovery. (3) "
            "Pumps, membranes, and energy recovery devices are counted at "
            "real efficiencies. (4) Pretreatment and brine disposal energy "
            "are in the ledger.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Compute the floor: the "
            "osmotic pressure of seawater is about 25 bar, and the minimum "
            "work follows from it. Step 2 - Measure the multiple: best RO "
            "plants run near 3 kWh per cubic metre, roughly triple the "
            "floor. Step 3 - Decompose: pump inefficiency, membrane "
            "resistance, concentration polarization, and the recovery "
            "trade-off each take a slice. Step 4 - Test the alternatives: "
            "any non-RO process must beat the RO multiple, not the "
            "thermodynamic floor.\\n\\n"
            "PROPOSED MECHANISM: the recovery trade-off is the deepest "
            "term - pushing recovery raises the floor itself - so the "
            "highest-leverage work is staged RO and batch RO designs that "
            "track the floor curve. The demo walks the floor-versus-reality "
            "numbers.\\n\\n"
            "WHAT WOULD CONFIRM IT: a plant or pilot demonstrating under 2 "
            "kWh per cubic metre at 50 percent recovery with measured "
            "membrane life. WHAT WOULD KILL IT: proof that fouling and "
            "polarization losses are irreducible at the needed flux, "
            "locking the multiple near 3 indefinitely.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the floor is "
            "reachable, does not claim thermal processes can compete on "
            "energy, and does not claim membranes improve on any schedule."
        ),
        "key_points": [
            "The thermodynamic minimum for seawater desalination is about 1 kWh per cubic metre at 50% recovery - and it rises with recovery.",
            "Best reverse-osmosis plants use about 3 kWh per cubic metre, roughly triple the floor.",
            "The gap decomposes into pump losses, membrane resistance, concentration polarization, and the recovery trade-off.",
            "Pushing recovery raises the thermodynamic floor itself - a deep, not incidental, term.",
            "The Signature approach ledgers each loss term and targets staged designs that track the floor curve.",
        ],
        "citations": [CIT_ELIMELECH, CIT_VOUTCHKOV],
    },
    {
        "key": "catalyst_death",
        "name": "Why Do Catalysts Die?",
        "group": "Approachable",
        "ladder_rank": 7,
        "ladder_tier": "approachable",
        "problem": (
            "Catalysts are supposed to be forever - they speed reactions "
            "without being consumed. In real plants they die: poisoned by "
            "trace sulfur, coked by carbon buildup, sintered by heat into "
            "useless lumps, or simply worn away. A refinery catalyst charge "
            "can cost millions and last months. The unsolved problem: how to "
            "design catalysts that resist all four death modes at once - or "
            "at least predict their lifetime accurately enough to schedule "
            "replacement without surprise shutdowns."
        ),
        "background": (
            "Satterfield's classic text catalogs the death modes - poisoning, "
            "fouling, sintering, attrition - that have plagued industrial "
            "catalysis since the beginning. The catalytic converter in your "
            "car carries extra precious metal partly as insurance against "
            "poisoning. Refinery catalysts are regenerated by burning off "
            "coke, a violent treatment that itself ages them. Modern "
            "research attacks each mode: sulfur-tolerant formulations, "
            "coke-resistant pore architectures, sinter-resistant "
            "encapsulation. But the modes interact - a fix for coking can "
            "worsen sintering - and lifetime prediction remains more art "
            "than science."
        ),
        "why_it_matters": (
            "Catalysts touch the overwhelming majority of manufactured "
            "goods. Every unplanned catalyst death is a plant shutdown, "
            "lost production, and wasted precious metals. Longer-lived, "
            "predictable catalysts mean cheaper chemicals, less mining, and "
            "plants that run instead of stop."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the four-death-mode model, and the confirm-or-"
            "refute panel. In one line: the Signature approach models each "
            "death mode as a competing decay rate and proposes the "
            "accelerated-aging protocol that would decide whether lifetimes "
            "can be predicted rather than discovered."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats catalyst death as four "
            "competing decay processes - poisoning, coking, sintering, "
            "attrition - and insists on modeling all four together, because "
            "real catalysts die of the combination.\\n\\n"
            "ASSUMPTIONS: (1) Activity follows a separable decay model: "
            "each mode contributes a rate, and the fastest dominates. (2) "
            "Poison levels are measured in the real feed, not assumed from "
            "spec sheets. (3) Regeneration cycles are counted - each burn-"
            "off ages the catalyst. (4) 'Lifetime' means time above the "
            "minimum economic activity, not time to zero.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Measure the four rates "
            "independently in accelerated tests: poison uptake isotherms, "
            "coking rates, sintering kinetics, attrition in a test loop. "
            "Step 2 - Combine: the plant lifetime is set by whichever mode "
            "wins under real feed conditions. Step 3 - Check the "
            "interactions: does the anti-coking pore structure accelerate "
            "sintering? Step 4 - Validate against plant history: the model "
            "must retrodict past catalyst lives before it predicts new "
            "ones.\\n\\n"
            "PROPOSED MECHANISM: the interaction terms are the missing "
            "science - single-mode tests systematically overpredict life. "
            "The demo walks a four-rate decay model and shows how the "
            "winner changes with feed conditions.\\n\\n"
            "WHAT WOULD CONFIRM IT: an accelerated protocol whose lifetime "
            "predictions match three or more independent plant histories "
            "within 20 percent. WHAT WOULD KILL IT: interaction effects "
            "proving too feed-specific to generalize - every plant a unique "
            "snowflake, prediction permanently artisanal.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim immortal catalysts "
            "exist, does not claim the four modes are independent, and does "
            "not claim accelerated tests capture everything."
        ),
        "key_points": [
            "Catalysts die four ways: poisoning, coking/fouling, sintering, and attrition - and the modes interact.",
            "A fix for one death mode often worsens another; single-mode tests systematically overpredict lifetime.",
            "Regeneration itself ages catalysts - each coke burn-off costs future life.",
            "Lifetime prediction remains more art than science across the industry.",
            "The Signature approach models all four decay rates together and validates against plant history.",
        ],
        "citations": [CIT_SATTERFIELD, CIT_LEVENSPIEL],
    },
    {
        "key": "scaleup_gap",
        "name": "Why Doesn't a Lab Recipe Work at Factory Scale?",
        "group": "Approachable",
        "ladder_rank": 8,
        "ladder_tier": "approachable",
        "problem": (
            "A reaction that sings in a one-litre flask can sulk, run away, "
            "or explode in a ten-thousand-litre reactor. Heat removal scales "
            "with surface area while heat generation scales with volume; "
            "mixing that takes seconds in a beaker takes minutes in a tank; "
            "tiny impurities become tonnes of byproduct. Chemical engineers "
            "call this the scale-up problem, and it is why new processes "
            "climb a painful ladder of pilot plants. The unsolved problem: "
            "how to predict plant behavior from laboratory data reliably - "
            "or design reactors that simply do not need scaling up."
        ),
        "background": (
            "Scale-up disasters are an old industry education: "
            "exothermic reactions that were docile at bench scale have "
            "destroyed pilot plants. The classical answer is dimensional "
            "analysis and pilot plants at intermediate scale - expensive, "
            "slow, and still sometimes wrong. Levenspiel's reaction "
            "engineering text formalizes what changes with scale: mixing "
            "times, heat transfer area per volume, residence time "
            "distributions. The modern alternative gaining ground is to "
            "stop scaling up at all: microreactors and flow systems where "
            "'scale-up' means numbering up - running many identical small "
            "units, as Jensen's 2001 paper argued."
        ),
        "why_it_matters": (
            "Scale-up is where good chemistry goes to die - years and "
            "fortunes lost between a promising lab result and a working "
            "plant. Faster, more reliable scale-up means new medicines, "
            "materials, and clean technologies reach the world years "
            "earlier. It is the translation layer of the entire chemical "
            "industry."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the surface-to-volume scaling model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "quantifies exactly which phenomena break with scale and "
            "proposes the numbering-up comparison that would decide whether "
            "the pilot plant can be retired."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats scale-up as a "
            "surface-to-volume audit: list every rate in the process, sort "
            "by how it scales with size, and the breakage points reveal "
            "themselves before the pilot plant is built.\\n\\n"
            "ASSUMPTIONS: (1) Geometric similarity is assumed unless stated "
            "- real scale-up often breaks it deliberately. (2) Heat "
            "generation scales with volume, removal with area: the ratio "
            "falls as 1 over length scale. (3) Mixing time grows with scale; "
            "reaction time does not. (4) Numbering-up is counted honestly: N "
            "small units need N sets of pumps, sensors, and maintenance.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Compute the "
            "surface-to-volume ratio at lab, pilot, and plant scale for the "
            "actual vessel shapes. Step 2 - Compare the heat removal "
            "capacity against the reaction heat at each scale - the scale "
            "where removal loses is the danger scale. Step 3 - Compare "
            "mixing time to reaction time: when mixing is slower than "
            "reaction, selectivity collapses. Step 4 - Price numbering-up "
            "against one big vessel including the maintenance burden.\\n\\n"
            "PROPOSED MECHANISM: most scale-up failures are heat-removal or "
            "mixing failures, both predictable from the 1/L ratio - the "
            "audit catches them on paper. The demo walks the ratios across "
            "three scales.\\n\\n"
            "WHAT WOULD CONFIRM IT: a set of historical scale-up failures "
            "retrodicted by the audit - the danger scale identified in "
            "advance. WHAT WOULD KILL IT: failures dominated by phenomena "
            "the audit cannot see from lab data, like trace-impurity "
            "effects that only appear at scale.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim pilot plants are "
            "obsolete, does not claim numbering-up is always cheaper, and "
            "does not claim every scale effect is predictable."
        ),
        "key_points": [
            "Heat removal scales with area, heat generation with volume - the ratio falls as 1/length, which is why big reactors run away.",
            "Mixing time grows with scale while reaction time does not; slow mixing kills selectivity.",
            "Classical scale-up uses dimensional analysis plus expensive pilot plants - slow and sometimes still wrong.",
            "Numbering-up (many small identical reactors) sidesteps scale-up but multiplies maintenance.",
            "The Signature approach audits every rate by its scaling law before steel is ordered.",
        ],
        "citations": [CIT_LEVENSPIEL, CIT_JENSEN, CIT_TOWLER],
    },
    {
        "key": "waste_heat",
        "name": "Why Is Waste Heat So Hard to Reuse?",
        "group": "Approachable",
        "ladder_rank": 9,
        "ladder_tier": "approachable",
        "problem": (
            "Industry throws away staggering amounts of heat - flue gases, "
            "cooling water, hot exhaust - much of it at temperatures too low "
            "to be useful but too high to ignore. Thermodynamics sets a hard "
            "ceiling: heat at 150 C can at best convert about 30 percent of "
            "its energy to work, and real devices do far worse. The unsolved "
            "problem: how to economically harvest low-grade waste heat - "
            "which is most of it - and either upgrade it, store it, or use "
            "it directly without the economics collapsing."
        ),
        "background": (
            "Heat recovery is as old as the economizer on a boiler, and "
            "pinch analysis - Linnhoff's 1970s method systematized in Smith's "
            "design text - taught industry to match hot and cold streams "
            "instead of wasting both. Combined heat and power plants capture "
            "high-grade heat well. The frontier is low-grade heat below "
            "about 200 C: organic Rankine cycles, thermoelectric "
            "generators, and heat pumps that upgrade waste heat to useful "
            "temperatures. Each works in the laboratory; each struggles "
            "against the Carnot limit and capital cost in the field. "
            "Meanwhile whole sectors - data centers, for example - are new "
            "giant sources of low-grade heat looking for a use."
        ),
        "why_it_matters": (
            "Waste heat is arguably the world's largest unused energy "
            "resource - recovering even a fraction would cut fuel use "
            "across industry. It is also the key to electrifying heat: heat "
            "pumps that upgrade waste heat can deliver industrial "
            "temperatures from electricity far more efficiently than "
            "resistance heating."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the Carnot-ledger model, and the confirm-or-"
            "refute panel. In one line: the Signature approach draws the "
            "temperature-versus-quantity map of a plant's waste heat and "
            "proposes the cascade design that would decide what fraction is "
            "truly recoverable."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats waste heat as a "
            "temperature-quantity map: every stream plotted by temperature "
            "and duty, and recovery options matched to the map instead of "
            "chasing the hottest stream alone.\\n\\n"
            "ASSUMPTIONS: (1) All heat duties and temperatures are measured, "
            "not estimated from nameplates. (2) The Carnot efficiency at "
            "each temperature is the ceiling; real devices are counted at "
            "demonstrated fractions of Carnot. (3) Capital cost per "
            "recovered kilowatt is in the ledger. (4) Heat has no value "
            "without a simultaneous use - storage or transport counts if "
            "needed.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Build the map: composite "
            "curves of all hot streams, the classic pinch picture. Step 2 - "
            "Apply the Carnot ceiling at each temperature band to get the "
            "theoretical recoverable work. Step 3 - Derate by demonstrated "
            "device performance: ORC at 10-15 percent of Carnot, "
            "thermoelectrics lower. Step 4 - Optimize the cascade: direct "
            "use first, heat pumping second, power generation last.\\n\\n"
            "PROPOSED MECHANISM: direct use and heat-pump upgrading beat "
            "power generation for low-grade heat on economics - the cascade "
            "order matters more than the device. The demo walks a "
            "three-stream plant through the cascade.\\n\\n"
            "WHAT WOULD CONFIRM IT: plant case studies where the cascade "
            "design recovers the predicted fraction at the predicted "
            "payback. WHAT WOULD KILL IT: device costs refusing to fall, "
            "leaving the recoverable fraction permanently uneconomic below "
            "200 C.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim all waste heat is "
            "recoverable, does not claim power generation from low-grade "
            "heat is economic, and does not claim the map replaces detailed "
            "design."
        ),
        "key_points": [
            "Most industrial waste heat is low-grade (below 200 C), where the Carnot ceiling is punishing - about 30% at 150 C.",
            "Pinch analysis already captures the easy high-grade matches; the frontier is low-grade heat.",
            "Organic Rankine cycles, thermoelectrics, and heat pumps each work but struggle against Carnot and capital cost.",
            "Direct use and heat-pump upgrading beat power generation on economics for low-grade heat.",
            "The Signature approach maps every stream by temperature and duty, then optimizes the recovery cascade.",
        ],
        "citations": [CIT_SMITH_DESIGN, CIT_CHU],
    },
    {
        "key": "hydrogen_logistics",
        "name": "Why Is Hydrogen So Hard to Store and Move?",
        "group": "Approachable",
        "ladder_rank": 10,
        "ladder_tier": "approachable",
        "problem": (
            "Hydrogen is the universe's simplest fuel and an engineer's "
            "nightmare to handle: the lightest molecule, it leaks through "
            "seals, embrittles steel, and packs almost no energy by volume - "
            "a cubic metre of hydrogen at atmospheric pressure holds about "
            "3 kilowatt-hours, versus 9,000 for gasoline. Compressing it to "
            "700 bar or liquefying it at minus 253 C costs 10 to 35 percent "
            "of its energy. The unsolved problem: how to store and move "
            "hydrogen densely, safely, and cheaply enough for it to serve "
            "as the backbone of clean steel, ammonia, and fuels."
        ),
        "background": (
            "Hydrogen has been an industrial chemical for a century - "
            "refineries and ammonia plants move it by pipeline today. The "
            "new challenge is energy-scale hydrogen: volumes orders of "
            "magnitude larger, moved to places without pipelines. Options "
            "each pay a tax: compression (fast, but bulky and energy-hungry), "
            "liquefaction (dense, but a third of the energy can go to "
            "cooling), metal hydrides and LOHCs - liquid organic hydrogen "
            "carriers - (safe and dense, but heavy and needing heat to "
            "release the hydrogen), and ammonia as a carrier (existing "
            "infrastructure, but toxic and needing cracking back to "
            "hydrogen). Chu's 2017 review frames storage as one of the "
            "gating problems of the energy transition."
        ),
        "why_it_matters": (
            "Green hydrogen is the leading candidate to decarbonize steel, "
            "shipping, aviation fuel, and chemicals - but only if it can "
            "travel from sunny deserts and windy coasts to factories. "
            "Storage and transport can be half the delivered cost. Solve "
            "the logistics and the hydrogen economy unlocks; fail and it "
            "stays a local curiosity."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the energy-tax ledger for each carrier, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "prices every storage route in percent of hydrogen energy lost "
            "and dollars per kilogram delivered, and proposes the "
            "route-comparison that would decide the winner by distance."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats hydrogen logistics as "
            "an energy-tax ledger: every carrier pays to pack the hydrogen "
            "and pays again to unpack it, and the honest comparison counts "
            "both taxes plus the container.\\n\\n"
            "ASSUMPTIONS: (1) Comparison basis is one kilogram of hydrogen "
            "delivered at fuel-cell purity. (2) Energy taxes are counted "
            "against hydrogen's lower heating value, 33.3 kWh per kg. (3) "
            "Carrier mass and return logistics are counted - a heavy "
            "carrier that must be shipped back pays twice. (4) Safety "
            "systems are costed, not assumed free.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Compute the packing "
            "tax: compression to 700 bar costs roughly 10-15 percent of "
            "LHV; liquefaction 25-35 percent. Step 2 - Compute the unpacking "
            "tax: LOHC dehydrogenation needs heat; ammonia cracking needs "
            "700-900 C. Step 3 - Add the container: gravimetric and "
            "volumetric density including the tank or carrier fluid. Step 4 "
            "- Sort by distance: pipelines win short, ships need dense "
            "carriers, and the crossover distances fall out of the ledger.\\n\\n"
            "PROPOSED MECHANISM: no carrier wins everywhere - the ledger "
            "predicts distance bands, with ammonia or LOHC for inter-"
            "continental shipping and pipelines or compressed gas locally. "
            "The demo walks the tax ledger for four carriers.\\n\\n"
            "WHAT WOULD CONFIRM IT: delivered-cost data from operating "
            "hydrogen supply chains matching the predicted distance bands. "
            "WHAT WOULD KILL IT: a new storage medium - solid-state or "
            "otherwise - beating all bands at once, collapsing the "
            "distance-sorted picture.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim any carrier is "
            "economic today at scale, does not claim the taxes are "
            "fundamental limits, and does not claim safety costs are fully "
            "known."
        ),
        "key_points": [
            "Hydrogen packs almost no energy by volume - about 3 kWh per cubic metre at atmospheric pressure.",
            "Compression to 700 bar costs 10-15% of its energy; liquefaction costs 25-35%.",
            "Carriers (LOHCs, ammonia, hydrides) pay an unpacking tax - heat or high temperature to release the hydrogen.",
            "The honest comparison counts both taxes plus carrier return logistics.",
            "The Signature approach ledgers every route and predicts distance bands where each wins.",
        ],
        "citations": [CIT_CHU, CIT_DAVIS],
    },
    {
        "key": "membrane_limits",
        "name": "Why Can't Filters Catch Everything?",
        "group": "Approachable",
        "ladder_rank": 11,
        "ladder_tier": "approachable",
        "problem": (
            "Membranes are chemistry's sieves - they desalinate seawater, "
            "purify drugs, and separate gases. But every membrane faces the "
            "same cruel bargain: the more it lets through (permeability), "
            "the less choosy it is (selectivity). Push for purity and flux "
            "collapses; push for flux and impurities slip through. Fouling - "
            "the slow crusting of the surface - then degrades even that "
            "compromise. The unsolved problem: how to break the "
            "permeability-selectivity trade-off, or at least predict and "
            "defeat fouling well enough for membranes to replace "
            "energy-hungry distillation."
        ),
        "background": (
            "The trade-off was formalized for gas separations by Robeson's "
            "upper bound (1991, revised 2008): plot selectivity against "
            "permeability for hundreds of polymers and they all fall under "
            "one curve. Researchers have spent decades trying to beat it "
            "with mixed-matrix membranes, carbon molecular sieves, and "
            "graphene-based films. Reverse osmosis membranes improved "
            "steadily through the 1990s and 2000s, then progress slowed - "
            "the field Elimelech and Phillip described as approaching "
            "practical limits. Fouling remains the operational tax: "
            "pretreatment chemistry is often more complex than the "
            "membrane itself."
        ),
        "why_it_matters": (
            "Separations consume a staggering share of industrial energy - "
            "distillation alone is estimated at 10 to 15 percent of US "
            "industrial energy. Membranes that could replace even a "
            "fraction of distillation would be a climate-scale energy "
            "saving. Better membranes also mean cheaper water, purer drugs, "
            "and captured carbon."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the trade-off curve model, and the confirm-or-"
            "refute panel. In one line: the Signature approach plots every "
            "candidate membrane against the upper bound and proposes the "
            "fouling experiment that would decide whether the bound is "
            "chemistry or just history."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats membranes as a "
            "position on the trade-off curve plus a fouling clock: where a "
            "membrane sits on the permeability-selectivity plot, and how "
            "fast fouling moves it off that point.\\n\\n"
            "ASSUMPTIONS: (1) Selectivity and permeability are measured at "
            "real operating conditions, not ideal single-gas tests. (2) The "
            "Robeson upper bound is treated as an empirical regularity, not "
            "a law - it has moved before. (3) Fouling rate is feed-"
            "specific and measured, not extrapolated. (4) The economic "
            "comparison is against distillation energy, the incumbent.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Place the incumbent "
            "membrane on the trade-off plot for the target separation. Step "
            "2 - Measure the fouling clock: flux decline per thousand hours "
            "on the real feed. Step 3 - Audit the challengers: mixed-matrix, "
            "carbon molecular sieve, 2D materials - each placed on the same "
            "plot with the same fouling test. Step 4 - Price the "
            "replacement: membrane life and cleaning chemistry in the "
            "ledger.\\n\\n"
            "PROPOSED MECHANISM: the bound moves when the transport "
            "mechanism changes - molecular sieving instead of solution-"
            "diffusion - so the search should target mechanism change, not "
            "incremental polymer tuning. The demo walks the trade-off plot "
            "and the fouling clock.\\n\\n"
            "WHAT WOULD CONFIRM IT: a membrane holding position above the "
            "current upper bound for 8,000+ hours on a real industrial "
            "feed. WHAT WOULD KILL IT: every above-bound material fouling "
            "or aging back below the bound within months - the bound as "
            "practical law.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the bound is "
            "fundamental, does not claim fouling is solvable in general, "
            "and does not claim membranes will replace distillation soon."
        ),
        "key_points": [
            "Every membrane trades permeability against selectivity - the Robeson upper bound has held across decades of polymers.",
            "Pushing for purity collapses flux; pushing for flux lets impurities through.",
            "Fouling is the operational tax: flux declines on real feeds, and cleaning chemistry is its own science.",
            "The bound has moved before - always when the transport mechanism changed, not by tuning.",
            "The Signature approach plots candidates on the bound and times their fouling clocks on real feeds.",
        ],
        "citations": [CIT_SEADER, CIT_ELIMELECH],
    },
    {
        "key": "battery_fade",
        "name": "Why Do Batteries Degrade Every Cycle?",
        "group": "Approachable",
        "ladder_rank": 12,
        "ladder_tier": "approachable",
        "problem": (
            "Every rechargeable battery is born dying: each cycle grows the "
            "passivation layer on the anode, cracks the cathode particles, "
            "and traps a little more lithium where it can never work again. "
            "Electric cars lose range year by year; grid batteries face the "
            "same slow fade. The unsolved problem: how to build lithium "
            "batteries - or their successors - whose capacity barely fades "
            "over thousands of cycles, and how to predict remaining life "
            "accurately enough to value a used battery."
        ),
        "background": (
            "The lithium-ion battery commercialized by Sony in 1991 won on "
            "energy density, not longevity. Peled's 1979 work identified the "
            "solid-electrolyte interphase - the SEI layer - as both the "
            "enabler of the graphite anode and the thief that consumes "
            "lithium every cycle. Two decades of materials science - silicon "
            "anodes, high-nickel cathodes, solid electrolytes - each "
            "promised more cycles; each introduced new degradation modes. "
            "Battery management systems now estimate state of health from "
            "voltage curves, but the estimates drift, and the second-life "
            "market for used EV batteries is held back by the inability to "
            "grade them cheaply and accurately."
        ),
        "why_it_matters": (
            "Batteries are the buffer of the renewable grid and the heart "
            "of electric transport. Degradation is a tax on both: it forces "
            "oversizing, early replacement, and waste. A battery that "
            "lasted twice as long would roughly halve the materials needed "
            "for the energy transition's storage."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the lithium-inventory ledger, and the confirm-or-"
            "refute panel. In one line: the Signature approach counts every "
            "lost lithium ion by mechanism and proposes the cycling protocol "
            "that would decide which degradation mode dominates in real "
            "use."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats battery fade as a "
            "lithium-inventory ledger: the battery starts with a fixed "
            "lithium budget, and every degradation mode spends from it. "
            "Find the biggest spender and you find the fix.\\n\\n"
            "ASSUMPTIONS: (1) The ledger basis is one amp-hour of initial "
            "capacity. (2) SEI growth, cathode cracking, lithium plating, "
            "and electrolyte dry-out are counted separately. (3) Calendar "
            "aging and cycle aging are separated - a parked battery still "
            "dies. (4) 'End of life' is 80 percent of initial capacity, the "
            "industry standard.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Open the ledger: measure "
            "capacity loss per 100 cycles and split it by mechanism using "
            "differential voltage analysis. Step 2 - Separate calendar from "
            "cycle: store identical cells at various states of charge and "
            "temperatures. Step 3 - Identify the dominant spender for the "
            "actual use profile - fast charging shifts the winner toward "
            "plating. Step 4 - Test the fix against the ledger: does the "
            "new electrolyte reduce total spending or just move it between "
            "modes?\\n\\n"
            "PROPOSED MECHANISM: most 'breakthrough' materials reduce one "
            "spending mode while increasing another - the ledger catches the "
            "shell game. The demo walks a four-mode fade model.\\n\\n"
            "WHAT WOULD CONFIRM IT: a cell chemistry whose ledger shows all "
            "four modes suppressed together over 2,000+ measured cycles. "
            "WHAT WOULD KILL IT: the modes proving fundamentally coupled - "
            "suppressing one always feeding another - making fade a "
            "conservation law in practice.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim any chemistry is "
            "immortal, does not claim lab cycles equal real-world years, "
            "and does not claim state-of-health estimation is solved."
        ),
        "key_points": [
            "Every cycle spends lithium: SEI growth, cathode cracking, plating, and electrolyte loss each take a cut.",
            "Calendar aging kills parked batteries too - cycling is only half the ledger.",
            "New materials often suppress one fade mode while feeding another - a shell game the ledger exposes.",
            "Used-battery grading is held back by unreliable state-of-health estimates.",
            "The Signature approach counts lost lithium by mechanism and finds the dominant spender for each use profile.",
        ],
        "citations": [CIT_CHU],
    },
    {
        "key": "dac_floor",
        "name": "The 400-ppm Wall: The Thermodynamic Minimum of Direct Air Capture",
        "group": "Deep",
        "ladder_rank": 13,
        "ladder_tier": "deep",
        "problem": (
            "Strip away the engineering and direct air capture is a "
            "thermodynamics exam: unmixing CO2 from air at 420 parts per "
            "million costs a minimum of about 0.44 gigajoules per tonne, "
            "and no sorbent, no process, no cleverness can go below it. Real "
            "plants spend 10 to 20 times that. The unsolved problem is the "
            "decomposition: exactly which terms - sorbent binding, sensible "
            "heat, air moving, incomplete recovery - make up the multiple, "
            "which are removable by better chemistry, and whether the "
            "irreducible remainder still allows hundred-dollar-tonne "
            "capture."
        ),
        "background": (
            "The minimum-work calculation is textbook thermodynamics - RT "
            "times the log of the concentration ratio - known long before "
            "direct air capture existed. What is new is the forensic "
            "accounting of real plants: Keith's 2018 process analysis put "
            "the calciner's 900 C heat as the dominant term for hydroxide "
            "systems, while solid-sorbent systems trade that for the "
            "sensible heat of cycling tonnes of contactor material. "
            "Fasihi's techno-economic work showed the cost stack is "
            "dominated by energy and capital together. The field's "
            "uncomfortable question, rarely stated plainly: if the multiple "
            "over the floor cannot fall below about 5, the energy alone "
            "exceeds the cost target at any plausible electricity price."
        ),
        "why_it_matters": (
            "This is the audit behind the promise. If the multiple is "
            "compressible, direct air capture can scale to gigatonnes; if "
            "it is chemistry-locked, climate plans built on cheap DAC need "
            "rewriting now, not in 2040. Getting the decomposition right "
            "directs billions in research toward the terms that can "
            "actually move."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the term-by-term decomposition, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "derives the floor from first principles, measures each term "
            "of the multiple, and proposes the sorbent-cycle test that "
            "would decide how low the multiple can go."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the DAC energy multiple "
            "as a forensic accounting problem: derive the floor exactly, "
            "then subpoena every joule above it until each is assigned to a "
            "physical cause.\\n\\n"
            "ASSUMPTIONS: (1) Air at 420 ppm CO2, 25 C, 1 atm; product CO2 "
            "at 1 atm, 95+ percent purity. (2) Minimum work W_min = RT "
            "ln(1/420e-6) per mole, 19.3 kJ/mol, 0.44 GJ per tonne. (3) "
            "Real plant data is used where published; where proprietary, "
            "bounds are stated. (4) Second-law efficiency is defined "
            "against this floor, not against a process ideal.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Derive the floor "
            "rigorously, including the effect of product purity and "
            "recovery fraction. Step 2 - Tabulate published plant energy "
            "use: hydroxide-calciner systems near 8-9 GJ per tonne, amine "
            "solids near 5-7 GJ per tonne. Step 3 - Decompose: binding "
            "enthalpy of the sorbent, sensible heat of the contactor mass, "
            "fan work for 1.3 million cubic metres of air per tonne, "
            "losses from incomplete desorption. Step 4 - Classify each "
            "term: chemistry-locked (binding enthalpy has a floor set by "
            "selectivity), engineering-soft (sensible heat falls with "
            "better heat integration), or scale-soft (capital learning "
            "curves).\\n\\n"
            "PROPOSED MECHANISM: the binding-enthalpy term is the "
            "chemistry-locked core - a sorbent selective enough to grab "
            "420-ppm CO2 must bind it strongly enough to cost energy "
            "releasing it. The demo computes the floor and the decomposition "
            "for both leading chemistries.\\n\\n"
            "WHAT WOULD CONFIRM IT: independent plant data converging on a "
            "multiple below 6 with a published term-by-term breakdown. "
            "WHAT WOULD KILL IT: a rigorous proof that selectivity at 420 "
            "ppm demands binding enthalpies locking the multiple above 8 - "
            "the cost target unreachable by thermodynamics, not engineering.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the floor derivation "
            "is novel, does not claim current multiples are optimal, and "
            "does not claim cost targets are impossible - only that the "
            "decomposition decides."
        ),
        "key_points": [
            "The thermodynamic floor for DAC is about 0.44 GJ per tonne - derivable from RT ln(1/420e-6).",
            "Real plants spend 5-9 GJ per tonne: a multiple of 10-20 over the floor.",
            "The multiple decomposes into sorbent binding enthalpy, sensible heat, fan work, and incomplete recovery.",
            "Binding enthalpy is partly chemistry-locked: grabbing 420-ppm CO2 selectively demands strong binding, which costs energy to reverse.",
            "The Signature approach classifies each term as locked, engineering-soft, or scale-soft.",
        ],
        "citations": [CIT_KEITH, CIT_FASIHI, CIT_BUI],
    },
    {
        "key": "amine_scrubbing",
        "name": "Amine Scrubbing: Capture Chemistry That Eats Itself",
        "group": "Deep",
        "ladder_rank": 14,
        "ladder_tier": "deep",
        "problem": (
            "The workhorse of carbon capture - bubbling flue gas through "
            "amine solutions that grab CO2 and release it on heating - is "
            "chemically self-destructive. Oxygen degrades the amines into "
            "heat-stable salts; the CO2 itself forms corrosive species; "
            "regeneration at 120 C slowly cooks the solvent. Plants must "
            "continuously purge and replace degraded amine, and the "
            "regeneration energy - about 3.5 gigajoules per tonne of CO2 - "
            "is a permanent tax on the power plant. The unsolved problem: a "
            "capture solvent that is fast, high-capacity, low-energy to "
            "regenerate, and chemically immortal - pick any three is the "
            "current state of the art."
        ),
        "background": (
            "Amine scrubbing dates to the 1930s gas industry; Rochelle's "
            "2009 Science review made the case for its readiness for power-"
            "plant CO2 capture and named its costs honestly. The Boundary "
            "Dam and Petra Nova projects proved it works at scale - and "
            "proved the energy penalty, roughly a quarter of a coal plant's "
            "output, and the solvent management burden. Two decades of "
            "solvent development - hindered amines, phase-change solvents, "
            "amino acid salts - have trimmed the regeneration energy but not "
            "the degradation chemistry. The degradation products themselves "
            "are an environmental question: nitrosamines and aerosols from "
            "amine plants are monitored, not yet fully understood."
        ),
        "why_it_matters": (
            "Point-source capture is the only near-term way to decarbonize "
            "cement, steel, and existing gas plants - sectors with no "
            "alternative. If amine scrubbing's energy penalty and solvent "
            "turnover cannot be cut substantially, carbon capture stays a "
            "boutique add-on instead of a climate tool. The solvent is the "
            "product."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the degradation-ledger model, and the confirm-or-"
            "refute panel. In one line: the Signature approach counts "
            "solvent loss by degradation pathway and proposes the "
            "accelerated-aging test that would decide whether any amine "
            "can be both fast and immortal."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats amine scrubbing as a "
            "solvent ledger: every kilogram of amine lost to oxidation, "
            "thermal degradation, or aerosol escape is counted, and the "
            "regeneration energy is counted per tonne net of solvent "
            "replacement.\\n\\n"
            "ASSUMPTIONS: (1) Basis is one tonne of CO2 captured at 90 "
            "percent capture rate from coal flue gas. (2) Degradation rates "
            "are measured in the presence of oxygen and real contaminants, "
            "not clean lab gas. (3) Regeneration energy counts reboiler "
            "duty plus solvent makeup production. (4) Aerosol and "
            "nitrosamine emissions are counted as constraints, not "
            "externalities.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Ledger the loss "
            "pathways: oxidative degradation dominates with oxygen present; "
            "thermal degradation dominates in the reboiler; aerosol escape "
            "is the wildcard. Step 2 - Measure the regeneration energy "
            "floor for the solvent: reaction enthalpy plus sensible heat "
            "plus stripping steam. Step 3 - Test the trade: faster kinetics "
            "need more reactive amines, which degrade faster - map the "
            "Pareto front. Step 4 - Audit the challengers: phase-change and "
            "non-aqueous solvents must beat the ledger, not just the "
            "reboiler duty.\\n\\n"
            "PROPOSED MECHANISM: the kinetics-stability trade-off is the "
            "binding constraint - the Pareto front, not any single "
            "solvent, is the thing to move. The demo walks the degradation "
            "ledger and the energy decomposition.\\n\\n"
            "WHAT WOULD CONFIRM IT: a solvent demonstrating under 2.5 GJ "
            "per tonne regeneration with measured degradation below 0.5 kg "
            "per tonne CO2 over 5,000 hours on real flue gas. WHAT WOULD "
            "KILL IT: the Pareto front proving immovable - every "
            "low-energy solvent degrading fast, every stable solvent "
            "energy-hungry.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim amines are doomed, "
            "does not claim degradation is fully understood, and does not "
            "claim the energy penalty can reach zero."
        ),
        "key_points": [
            "Amine scrubbing works at scale but pays about 3.5 GJ per tonne of CO2 in regeneration energy.",
            "Oxygen and heat degrade the solvent into heat-stable salts; plants continuously purge and replace it.",
            "Faster, more reactive amines degrade faster - a kinetics-stability Pareto front binds the field.",
            "Degradation products (nitrosamines, aerosols) are monitored but not fully understood environmentally.",
            "The Signature approach ledgers every loss pathway and maps the Pareto front rather than chasing one solvent.",
        ],
        "citations": [CIT_ROCHELLE, CIT_BUI],
    },
    {
        "key": "co2_electrolysis",
        "name": "Turning CO2 Into Fuel With Electricity",
        "group": "Deep",
        "ladder_rank": 15,
        "ladder_tier": "deep",
        "problem": (
            "In principle, electricity plus water plus CO2 equals fuel - "
            "electrochemical CO2 reduction could make carbon monoxide, "
            "ethylene, or ethanol from waste CO2 and renewable power. In "
            "practice, the reaction competes with hydrogen evolution at "
            "every turn, selectivity to any single product is poor, current "
            "densities that matter industrially destroy the catalysts, and "
            "the best lab results use pure CO2 feeds nobody can afford. The "
            "unsolved problem: an electrolyzer that converts CO2 to a "
            "chosen product at industrial current density, high selectivity, "
            "and thousand-hour stability."
        ),
        "background": (
            "Hori's 1980s work on copper electrodes showed CO2 could be "
            "reduced to hydrocarbons - copper remains, decades later, the "
            "only metal that makes C2+ products in useful amounts, and "
            "nobody fully understands why. The 2010s brought gas-diffusion "
            "electrodes pushing current densities toward 1 amp per square "
            "centimetre, and the 2020s brought membrane-electrode assemblies "
            "chasing stability. De Luna's 2019 Science analysis set the "
            "economic bar: electrosynthesis must beat petrochemical routes "
            "on cost, which demands cheap electricity, cheap CO2, and "
            "efficient cells all at once. Carbonate formation - CO2 "
            "reacting with the alkaline electrolyte instead of reducing - "
            "silently eats feedstock in most designs."
        ),
        "why_it_matters": (
            "Aviation, shipping, and chemicals need dense liquid fuels and "
            "feedstocks with no electric alternative. CO2 electrolysis "
            "could close the carbon loop: capture CO2, add renewable "
            "electricity, get fuel. It is one of very few paths to "
            "carbon-neutral hydrocarbons."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the electron-ledger model, and the confirm-or-"
            "refute panel. In one line: the Signature approach counts every "
            "electron by destination - product, hydrogen, carbonate, heat - "
            "and proposes the durability test that would decide whether "
            "copper's selectivity can survive industrial conditions."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats CO2 electrolysis as an "
            "electron ledger: of every 100 electrons, count how many reach "
            "the target product, how many make hydrogen, how many are lost "
            "to carbonate, and how many heat the cell.\\n\\n"
            "ASSUMPTIONS: (1) Basis is one mole of target product at "
            "industrial current density, 0.5+ A per square centimetre. (2) "
            "Faradaic efficiency is measured on the full product slate, "
            "including hydrogen - no cherry-picked products. (3) Carbonate "
            "loss is counted as feedstock cost. (4) Stability means "
            "constant selectivity, not just constant current.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Write the competing "
            "reactions: CO2 reduction versus hydrogen evolution, with "
            "thermodynamics favoring hydrogen at most conditions. Step 2 - "
            "Ledger a reported result: Faradaic efficiency to the target, "
            "cell voltage versus the thermodynamic minimum, carbonate "
            "crossover. Step 3 - Stress it: raise current density and watch "
            "which ledger entries move - selectivity usually collapses "
            "first. Step 4 - Price the system: electricity, CO2 feed, and "
            "separation of the product mixture.\\n\\n"
            "PROPOSED MECHANISM: carbonate formation is the silent ledger "
            "thief most papers undercount - designs that avoid bulk "
            "alkalinity attack the largest hidden loss. The demo walks the "
            "electron ledger for a copper cell.\\n\\n"
            "WHAT WOULD CONFIRM IT: 1,000 hours at 0.5+ A/cm2 with "
            "sustained 70%+ Faradaic efficiency to a single C2+ product and "
            "audited carbonate losses. WHAT WOULD KILL IT: selectivity "
            "proving fundamentally coupled to the copper surface "
            "reconstructions that industrial conditions impose - the lab "
            "result unscalable in principle.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim copper's mechanism "
            "is understood, does not claim the economics work at any "
            "electricity price, and does not claim carbonate losses are "
            "avoidable in all designs."
        ),
        "key_points": [
            "Copper is the only metal making C2+ products from CO2 in useful amounts - and its mechanism is still debated.",
            "Hydrogen evolution competes at every turn; carbonate formation silently eats feedstock in alkaline designs.",
            "Lab selectivities collapse at industrial current densities; thousand-hour stability is rare.",
            "De Luna's economic bar demands cheap electricity, cheap CO2, and efficient cells simultaneously.",
            "The Signature approach ledgers every electron by destination and stresses cells until the ledger breaks.",
        ],
        "citations": [CIT_DELUNA, CIT_ARESTA],
    },
    {
        "key": "nitrogen_electroreduction",
        "name": "Making Ammonia From Air, Water, and Electricity",
        "group": "Deep",
        "ladder_rank": 16,
        "ladder_tier": "deep",
        "problem": (
            "If nitrogen could be reduced to ammonia electrochemically at "
            "room temperature - the way nature's nitrogenase does it - "
            "fertilizer could be made anywhere with a solar panel. The "
            "reality is brutal: nitrogen reduction competes with hydrogen "
            "evolution, and hydrogen wins almost every time. Reported "
            "Faradaic efficiencies are usually single digits, ammonia "
            "yields are often contamination artifacts, and the field "
            "endured a reproducibility crisis in the late 2010s. The "
            "unsolved problem: a nitrogen-reduction catalyst and cell that "
            "produce ammonia selectively, verifiably, and at rates that "
            "matter."
        ),
        "background": (
            "Electrochemical nitrogen reduction has been attempted since "
            "the 1980s with little to show. The 2010s brought a flood of "
            "papers claiming breakthroughs - most of which failed the "
            "isotope test: run the cell on nitrogen-15 and the ammonia "
            "should carry the label, proving it came from N2 and not from "
            "contamination. Many did not. The community responded with "
            "rigorous protocols around 2019-2020, and credible results "
            "remain modest: low efficiencies, low rates. Meanwhile "
            "lithium-mediated nitrogen reduction - a hybrid "
            "electrochemical-chemical cycle - emerged as the most promising "
            "route, with its own energy and lithium-recycling challenges."
        ),
        "why_it_matters": (
            "Decentralized ammonia would transform agriculture in regions "
            "without gas infrastructure and decarbonize fertilizer where "
            "Haber-Bosch cannot reach. It is also the cleanest conceptual "
            "route to green ammonia for shipping fuel. The prize is "
            "enormous; the credibility bar, after the contamination years, "
            "is appropriately brutal."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the selectivity ledger, and the confirm-or-refute "
            "panel. In one line: the Signature approach applies the isotope "
            "standard to every claim and proposes the lithium-mediated "
            "cycle audit that would decide whether the route can ever beat "
            "Haber-Bosch on energy."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats nitrogen electroreduction "
            "as a credibility-first ledger: no number is admitted without "
            "the isotope test, and then every electron and every joule is "
            "counted.\\n\\n"
            "ASSUMPTIONS: (1) Only isotope-verified ammonia counts - "
            "nitrogen-15 in, labeled ammonia out. (2) Faradaic efficiency "
            "is measured against total current including hydrogen. (3) The "
            "lithium-mediated route counts lithium recycling energy. (4) "
            "Rates are normalized per geometric area and per catalyst mass "
            "- both, not whichever flatters.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Apply the isotope "
            "filter: discard every claim without nitrogen-15 verification. "
            "Step 2 - Ledger the survivors: Faradaic efficiency, partial "
            "current density to ammonia, cell voltage. Step 3 - Audit the "
            "lithium-mediated cycle end to end: plating, nitridation, "
            "protonation, lithium recovery - the energy sum, not the best "
            "step. Step 4 - Compare against the Haber-Bosch ledger from "
            "record 1: the challenger must beat 30 GJ per tonne, not merely "
            "exist.\\n\\n"
            "PROPOSED MECHANISM: the lithium-mediated cycle is the only "
            "family with non-negligible verified rates - so the decisive "
            "work is its full-cycle energy audit, not more catalyst "
            "screening. The demo walks the selectivity ledger.\\n\\n"
            "WHAT WOULD CONFIRM IT: isotope-verified ammonia at 50%+ "
            "Faradaic efficiency and Haber-Bosch-beating full-cycle energy. "
            "WHAT WOULD KILL IT: the hydrogen-evolution competition proving "
            "thermodynamically inescapable at the needed overpotentials - "
            "selectivity capped in principle.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the field's past "
            "results are all invalid, does not claim lithium-mediated routes "
            "are economic, and does not claim contamination explains every "
            "failure."
        ),
        "key_points": [
            "Nitrogen reduction competes with hydrogen evolution - and hydrogen wins almost every time.",
            "The field suffered a contamination crisis; only nitrogen-15 isotope-verified results count.",
            "Credible Faradaic efficiencies remain in the single digits for direct routes.",
            "The lithium-mediated cycle is the most promising family but must audit lithium recycling energy.",
            "The Signature approach filters by isotope proof first, then ledgers energy against Haber-Bosch.",
        ],
        "citations": [CIT_SMIL, CIT_SATTERFIELD],
    },
    {
        "key": "depolymerization",
        "name": "Unzipping Plastics Back to Monomers",
        "group": "Deep",
        "ladder_rank": 17,
        "ladder_tier": "deep",
        "problem": (
            "Every plastic was once monomers that polymerized - releasing "
            "energy downhill. Running the reaction backward means climbing "
            "back up that hill, and for polyolefins like polyethylene - "
            "half of all plastic - the hill is steep: the polymerization "
            "is strongly favored, so depolymerization needs aggressive "
            "conditions that shred selectivity. PET and polystyrene unzip "
            "more cooperatively; polyethylene resists. The unsolved problem: "
            "catalysts that cut polyolefin chains selectively back to "
            "valuable monomers or narrow product slates, at temperatures "
            "and costs that beat making virgin resin."
        ),
        "background": (
            "Pyrolysis - simply cooking plastic - is old, and gives a messy "
            "oil. The modern push is catalytic: hydrogenolysis over "
            "ruthenium or platinum catalysts that snip chains into alkanes, "
            "and newer tandem systems aiming for monomers. Coates and "
            "Getzler's 2020 review defined the ideal: chemical recycling to "
            "monomer, a true closed loop. Jehanno's 2022 survey showed the "
            "field moving from degradation to upcycling - making products "
            "worth more than the waste. The thermodynamic obstacle is the "
            "ceiling temperature: above it, polymer unzips spontaneously; "
            "for polyethylene the ceiling temperature is high and the "
            "unzipping unselective, which is why catalysts must do the "
            "work that heat alone cannot do cleanly."
        ),
        "why_it_matters": (
            "Polyolefins are the bulk of the waste stream and the hardest "
            "to recycle chemically. A selective depolymerization for "
            "polyethylene would convert the largest plastic waste flow on "
            "Earth into feedstock. Without it, 'circular plastics' covers "
            "everything except the plastics we actually throw away most."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the ceiling-temperature model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "computes the thermodynamic price of unzipping each polymer and "
            "proposes the selectivity test that would decide whether "
            "catalysis can beat the ceiling-temperature trap."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats depolymerization as a "
            "ceiling-temperature ledger: each polymer's thermodynamics sets "
            "the price of unzipping, and catalysts can only spend that "
            "budget more cleverly, not erase it.\\n\\n"
            "ASSUMPTIONS: (1) Basis is one tonne of clean polyolefin waste; "
            "contamination is a separate ledger entry. (2) The ceiling "
            "temperature Tc = dH/dS for each polymer sets the spontaneity "
            "boundary. (3) 'Selective' means 70%+ of product in a usable "
            "narrow slate. (4) Catalyst cost and lifetime are counted.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Compute the "
            "thermodynamics: for polyethylene, polymerization is favored by "
            "roughly 100 kJ per mole of ethylene - the hill to climb. Step "
            "2 - Compare polymer families: PET and polystyrene have "
            "accessible unzipping chemistry; polyolefins do not. Step 3 - "
            "Audit the catalytic routes: hydrogenolysis, tandem cracking-"
            "alkylation, each scored on selectivity, temperature, and "
            "catalyst turnover. Step 4 - Price against virgin: the "
            "depolymerization cost per tonne must beat virgin resin plus "
            "collection.\\n\\n"
            "PROPOSED MECHANISM: tandem catalysis - one site cracks, "
            "another functionalizes - is the most promising way to narrow "
            "the product slate from polyolefins. The demo walks the "
            "ceiling-temperature numbers and the selectivity ledger.\\n\\n"
            "WHAT WOULD CONFIRM IT: a polyolefin depolymerization at under "
            "250 C with 70%+ selectivity to a narrow product slate and "
            "measured catalyst turnover above 10,000. WHAT WOULD KILL IT: "
            "the thermodynamics proving that selective low-temperature "
            "unzipping of polyethylene demands catalysts too exotic or "
            "short-lived to ever beat virgin resin economics.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim pyrolysis is "
            "worthless, does not claim all polymers are equally hard, and "
            "does not claim catalysts can repeal thermodynamics."
        ),
        "key_points": [
            "Polymerization runs downhill; depolymerization must climb back up - for polyethylene the hill is steep.",
            "Ceiling temperature sets the spontaneity boundary: PET and polystyrene unzip cooperatively, polyolefins resist.",
            "Pyrolysis gives messy oils; the prize is selective catalytic routes to monomers or narrow slates.",
            "Catalysts can spend the thermodynamic budget cleverly but cannot erase it.",
            "The Signature approach ledgers thermodynamics, selectivity, catalyst turnover, and virgin-resin price together.",
        ],
        "citations": [CIT_COATES, CIT_JEHANNO, CIT_RAGAERT],
    },
    {
        "key": "mixed_plastic_sorting",
        "name": "The Mixed-Plastic Sorting Problem",
        "group": "Deep",
        "ladder_rank": 18,
        "ladder_tier": "deep",
        "problem": (
            "No recycling chemistry works on a mystery mixture - yet the "
            "waste stream is exactly that: polyethylene films tangled with "
            "PET bottles, black plastics invisible to optical sorters, "
            "multi-layer pouches that are five polymers in one. Sorting is "
            "the unglamorous gatekeeper of the whole circular-plastics "
            "vision, and it is a chemistry problem: how to identify and "
            "separate mixed, dirty, composite plastics fast enough and "
            "cheaply enough that the downstream chemistry gets a clean "
            "feed."
        ),
        "background": (
            "Materials recovery facilities sort by a cascade: magnets, eddy "
            "currents, air jets, and near-infrared (NIR) spectroscopy that "
            "identifies polymer type by its molecular vibrations. NIR "
            "fails on black plastics - carbon black absorbs the signal - "
            "which is why black food trays are effectively unsortable in "
            "most plants. Multi-layer films, the fastest-growing packaging "
            "format, defeat every bulk method. Research directions include "
            "fluorescent markers embedded at manufacture, digital watermarks "
            "read by high-speed cameras, and solvent-based selective "
            "dissolution that separates by chemistry rather than optics. "
            "Each adds cost to a stream whose economics are already brutal."
        ),
        "why_it_matters": (
            "Every downstream recycling technology - mechanical or chemical "
            "- assumes a sorted feed. Sorting is the bottleneck that makes "
            "or breaks the economics of all of them. Solve sorting and "
            "dozens of recycling chemistries become viable; fail and they "
            "starve for feedstock."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the sorting mass-balance model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "balances a sorting plant stream by stream and proposes the "
            "tracer experiment that would decide whether embedded markers "
            "can pay for themselves."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats sorting as a mass-"
            "balance ledger: every stream in, every stream out, purity and "
            "recovery measured per polymer - because a sorter that is 95 "
            "percent accurate on 90 percent of the stream still fails the "
            "plant.\\n\\n"
            "ASSUMPTIONS: (1) Basis is one tonne per hour of mixed rigid "
            "packaging waste at real contamination levels. (2) Purity is "
            "measured per output stream; recovery is measured per polymer. "
            "(3) Black plastics and multi-layer films are counted at their "
            "real mass fractions, not excluded. (4) Marker or watermark "
            "schemes count the cost of marking at manufacture.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Characterize the feed: "
            "polymer fractions, black-plastic share, film share, dirt "
            "loading. Step 2 - Model the cascade: each stage's recovery and "
            "purity multiply - three 90-percent stages give 73 percent "
            "overall recovery. Step 3 - Find the leaks: which polymers and "
            "formats escape, and where they go. Step 4 - Price the fixes: "
            "tracers, watermarks, and solvent separation each enter the "
            "ledger with costs and purity gains.\\n\\n"
            "PROPOSED MECHANISM: the cascade multiplication is the key "
            "insight - sorting needs fewer, better stages, not more "
            "mediocre ones. The demo walks the mass balance of a three-"
            "stage plant.\\n\\n"
            "WHAT WOULD CONFIRM IT: a sorting line demonstrating 95%+ "
            "purity and 90%+ recovery per major polymer including black "
            "plastics, at published cost per tonne. WHAT WOULD KILL IT: "
            "the economics proving that high-purity sorting always costs "
            "more than the sorted material is worth - the stream "
            "fundamentally uneconomic to untangle.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim current MRFs are "
            "useless, does not claim markers will be adopted industry-wide, "
            "and does not claim solvent separation scales cheaply."
        ),
        "key_points": [
            "No recycling chemistry works on mystery mixtures - sorting is the gatekeeper of circular plastics.",
            "Near-infrared sorters are blind to black plastics; multi-layer films defeat bulk methods entirely.",
            "Stage recoveries multiply: three 90% stages give only 73% overall recovery.",
            "Tracers, digital watermarks, and solvent separation are the candidate fixes - each with a cost.",
            "The Signature approach mass-balances the whole cascade and prices each fix against purity gained.",
        ],
        "citations": [CIT_RAGAERT, CIT_GEYER],
    },
    {
        "key": "continuous_pharma_deep",
        "name": "Continuous Pharma: Proving Quality in Real Time",
        "group": "Deep",
        "ladder_rank": 19,
        "ladder_tier": "deep",
        "problem": (
            "A continuous drug plant never stops - which means quality "
            "cannot be tested after the fact, the way batch plants do it. "
            "It must be measured in the flowing stream, in real time, with "
            "instruments that see impurities at parts-per-million while "
            "tonnes of material rush past. Process analytical technology - "
            "spectroscopy, particle sizing, in-line chromatography - is the "
            "nervous system of continuous pharma, and it is not yet reliable "
            "enough for the hardest cases: crystallizations that decide "
            "purity, polymorphs that decide bioavailability. The unsolved "
            "problem: real-time quality assurance rigorous enough that "
            "regulators - and patients - trust the stream."
        ),
        "background": (
            "The FDA's PAT initiative dates to 2004, urging industry toward "
            "real-time quality, but batch habits persisted. Continuous "
            "pioneers learned the control lessons the hard way: residence "
            "time distributions mean a disturbance echoes through the line "
            "for hours, and without fast analytics the plant makes "
            "off-spec material before anyone knows. Model predictive "
            "control, borrowed from petrochemicals, is being adapted to "
            "pharma's tighter specs and smaller volumes. Crystallization - "
            "where the drug's solid form is born - remains the least "
            "controllable continuous unit operation, and the solid form "
            "determines whether the pill works."
        ),
        "why_it_matters": (
            "Real-time quality is the load-bearing wall of continuous "
            "manufacturing: without it, the economic and resilience case "
            "collapses back to batch. It is also the template for every "
            "regulated continuous process to come - the methods proven on "
            "drugs will serve food, fine chemicals, and beyond."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the disturbance-propagation model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models how a disturbance travels down the line and proposes "
            "the upset-recovery test that would decide whether control is "
            "fast enough to trust."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats continuous quality as "
            "a race between disturbance and detection: an upset enters "
            "upstream, and the control system must see it and correct "
            "before off-spec material reaches the outlet.\\n\\n"
            "ASSUMPTIONS: (1) The line is modeled as units in series with "
            "measured residence time distributions. (2) Analytics have "
            "known measurement delays - spectroscopy is fast, in-line "
            "chromatography is slow. (3) 'Off-spec' is defined by the "
            "registered impurity limits, not internal targets. (4) The "
            "disturbance set includes feed variation, the realistic upset, "
            "not just setpoint changes.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Map the line: each "
            "unit's residence time distribution sets how disturbances "
            "smear and propagate. Step 2 - Time the analytics: detection "
            "delay plus control action must beat the disturbance's travel "
            "time to the outlet. Step 3 - Test the hard case: a "
            "crystallization upset, where the analytics are slowest and "
            "the quality attribute matters most. Step 4 - Define the "
            "diversion logic: when the race is lost, off-spec material "
            "must be diverted automatically - and the diverted fraction is "
            "a cost term.\\n\\n"
            "PROPOSED MECHANISM: the detection-delay budget is the design "
            "variable - placing fast analytics at the right points matters "
            "more than making any single analyzer faster. The demo walks a "
            "disturbance down a three-unit line.\\n\\n"
            "WHAT WOULD CONFIRM IT: a continuous line publishing upset-"
            "recovery data - disturbance in, detection time, diverted "
            "fraction - meeting registered specs. WHAT WOULD KILL IT: "
            "crystallization proving fundamentally too slow to control in "
            "flow for complex molecules, forcing hybrid batch-continuous "
            "plants permanently.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim analytics are "
            "adequate today, does not claim regulators will accept every "
            "design, and does not claim the batch comparison is settled."
        ),
        "key_points": [
            "Continuous plants cannot test quality after the fact - it must be measured in the flowing stream.",
            "Disturbances propagate down the line smeared by residence time distributions; detection must beat them to the outlet.",
            "Crystallization is the least controllable continuous unit operation - and it decides whether the pill works.",
            "Diversion logic for off-spec material is a real cost term most analyses omit.",
            "The Signature approach races disturbance against detection and budgets the detection delay.",
        ],
        "citations": [CIT_LEE_PHARMA, CIT_STEPHANOPOULOS],
    },
    {
        "key": "brine_problem",
        "name": "Brine: The Concentrate Nobody Wants",
        "group": "Deep",
        "ladder_rank": 20,
        "ladder_tier": "deep",
        "problem": (
            "Every litre of desalinated water leaves behind roughly a litre "
            "of brine - twice as salty as the sea, laced with pretreatment "
            "chemicals. Dumping it back offshore damages marine ecosystems; "
            "inland plants have nowhere to put it at all. Zero liquid "
            "discharge - evaporating the brine to solid salt - works but at "
            "brutal energy cost, since evaporating water is far hungrier "
            "than reverse osmosis. The unsolved problem: what to do with "
            "brine at scale - minimize it, valorize it, or dispose of it "
            "without ecological cost."
        ),
        "background": (
            "Brine disposal was an afterthought in desalination's early "
            "decades - outfall pipes and dilution were the answer. As "
            "plants multiplied along sensitive coastlines, regulators began "
            "restricting discharge, and inland brackish-water plants faced "
            "the problem with no ocean at all. Research split three ways: "
            "high-recovery RO and closed-circuit designs that shrink brine "
            "volume; selective recovery of magnesium, lithium, and other "
            "values from brine - the 'mining seawater' dream; and "
            "crystallizers for zero liquid discharge, proven in industry "
            "but energy-intensive. The lithium-from-brine story illustrates "
            "the economics: the lithium is there, but at parts-per-million "
            "it costs more to extract than it is worth - usually."
        ),
        "why_it_matters": (
            "Brine is desalination's shadow - the industry cannot double "
            "without doubling its waste stream. Coastal ecosystems near "
            "outfalls already show stress. Inland desalination, the only "
            "option for much of the water-stressed world, is impossible "
            "without a brine answer. The concentrate problem is the water "
            "problem's other half."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the brine mass-and-energy ledger, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "ledgers brine volume, salt mass, and disposal energy together "
            "and proposes the recovery experiment that would decide whether "
            "brine is waste or ore."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats brine as a mass ledger "
            "with three exits - minimize, valorize, dispose - and prices "
            "each exit per cubic metre of freshwater produced.\\n\\n"
            "ASSUMPTIONS: (1) Basis is one cubic metre of freshwater from "
            "seawater RO at 50 percent recovery: one cubic metre of brine "
            "at 70 grams per litre. (2) Disposal options are counted with "
            "their real constraints: ocean outfall needs dilution modeling, "
            "inland needs evaporation ponds or crystallizers. (3) Mineral "
            "recovery counts extraction cost against commodity prices. (4) "
            "Ecological cost is a constraint, not an externality.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Shrink it: high-"
            "recovery and closed-circuit RO cut brine volume, but the "
            "thermodynamic floor rises with recovery - the energy ledger "
            "from record 6 applies. Step 2 - Mine it: compute the contained "
            "value per cubic metre - magnesium, potassium, lithium - "
            "against selective extraction costs. Step 3 - Dry it: zero "
            "liquid discharge energy is dominated by evaporating water at "
            "roughly 630 kWh per cubic metre of brine. Step 4 - Compare "
            "the exits: the cheapest compliant exit wins, and 'compliant' "
            "is doing heavy lifting.\\n\\n"
            "PROPOSED MECHANISM: brine minimization at the RO stage beats "
            "brine treatment after it - every cubic metre not made is the "
            "cheapest to dispose of. The demo walks the three-exit ledger.\\n\\n"
            "WHAT WOULD CONFIRM IT: a selective extraction process "
            "publishing cost per kilogram recovered below commodity price "
            "at pilot scale. WHAT WOULD KILL IT: extraction costs proving "
            "structurally above commodity values at brine concentrations - "
            "brine permanently waste, and disposal the only exit.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim brine mining is "
            "economic today, does not claim zero liquid discharge is "
            "affordable, and does not claim outfall impacts are fully "
            "understood."
        ),
        "key_points": [
            "Every litre of desalinated seawater leaves about a litre of double-salinity brine with treatment chemicals.",
            "Ocean discharge stresses coastal ecosystems; inland plants have no ocean at all.",
            "Zero liquid discharge works but costs roughly 630 kWh per cubic metre of brine evaporated.",
            "'Mining' brine for lithium or magnesium usually costs more than the minerals are worth.",
            "The Signature approach ledgers minimize, valorize, and dispose per cubic metre of freshwater.",
        ],
        "citations": [CIT_ELIMELECH, CIT_VOUTCHKOV],
    },
    {
        "key": "forward_osmosis",
        "name": "Forward Osmosis and the Search for Low-Energy Desalination",
        "group": "Deep",
        "ladder_rank": 21,
        "ladder_tier": "deep",
        "problem": (
            "Forward osmosis promises desalination without high pressure: a "
            "super-salty 'draw' solution pulls water across the membrane by "
            "osmosis alone. The catch the brochures underplay: now you have "
            "diluted draw solution, and separating the fresh water back out "
            "of it costs energy - often as much as reverse osmosis would "
            "have. The unsolved problem: a draw solute - or a draw recovery "
            "method - whose regeneration is genuinely cheaper than the RO "
            "it replaces, not merely relocated."
        ),
        "background": (
            "Forward osmosis is old - it was studied for desalination in "
            "the 1970s - and periodically revived by new draw solutes: "
            "thermolytic salts like ammonium bicarbonate that decompose "
            "with gentle heat, magnetic nanoparticles pulled out with "
            "magnets, polyelectrolytes, switchable solvents. Each revival "
            "foundered on the same ledger: the draw regeneration step. "
            "Elimelech and Phillip's analysis showed FO's niche is not "
            "seawater desalination but applications where the draw solution "
            "itself is the product - fertilizer-drawn FO for irrigation, "
            "for example - or where fouling resistance matters more than "
            "energy. The dream of low-energy seawater FO remains unmet."
        ),
        "why_it_matters": (
            "If a genuinely low-energy desalination existed, water "
            "economics would transform overnight. FO is the most credible "
            "challenger concept to pressure-driven RO - understanding "
            "exactly why it keeps failing focuses the field on what a "
            "real breakthrough must look like, and its niches (fertigation, "
            "fouling-resistant concentration) are valuable in their own "
            "right."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the draw-regeneration ledger, and the confirm-or-"
            "refute panel. In one line: the Signature approach counts the "
            "full FO cycle including draw recovery and proposes the "
            "head-to-head test that would decide whether any draw solute "
            "beats RO."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats forward osmosis as a "
            "two-step ledger: the osmosis step is nearly free, and the "
            "regeneration step is where the bill hides. Any honest "
            "comparison counts both.\\n\\n"
            "ASSUMPTIONS: (1) Basis is one cubic metre of freshwater from "
            "seawater. (2) The draw solution must be regenerated to its "
            "original concentration - diluted draw is not a product. (3) "
            "Membrane area and fouling are counted; FO membranes foul "
            "differently, not negligibly. (4) The comparison is against "
            "best RO at 3 kWh per cubic metre.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Compute the osmosis "
            "step: water flux driven by the osmotic pressure difference, "
            "genuinely low-energy. Step 2 - Compute the regeneration: "
            "thermolytic salts need heat to decompose; nanoparticles need "
            "magnetic separation plus washing; every option has a bill. "
            "Step 3 - Add the hidden terms: reverse solute flux - draw "
            "solute leaking into the feed - contaminates and must be made "
            "up. Step 4 - Compare full-cycle energy and cost against RO.\\n\\n"
            "PROPOSED MECHANISM: the regeneration step dominates in every "
            "credible analysis - so draw-solute research should optimize "
            "for cheap regeneration first, high osmotic pressure second. "
            "The demo walks the two-step ledger for a thermolytic draw.\\n\\n"
            "WHAT WOULD CONFIRM IT: a full-cycle FO demonstration under 2 "
            "kWh per cubic metre including draw regeneration at pilot "
            "scale. WHAT WOULD KILL IT: regeneration thermodynamics "
            "proving that no draw solute can be both strong enough to pull "
            "seawater and cheap enough to regenerate - the concept "
            "fundamentally ledger-negative.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim FO is useless - its "
            "niches are real - does not claim RO is unimprovable, and does "
            "not claim any draw solute is close."
        ),
        "key_points": [
            "Forward osmosis pulls water across the membrane with no high pressure - but the diluted draw solution must be regenerated.",
            "Draw regeneration usually costs as much energy as the RO it was meant to replace.",
            "Reverse solute flux - draw leaking into the feed - is a hidden cost and contamination term.",
            "FO's real niches are where the draw is the product (fertilizer for irrigation) or fouling resistance matters.",
            "The Signature approach ledgers both steps and optimizes draw solutes for cheap regeneration first.",
        ],
        "citations": [CIT_ELIMELECH, CIT_SEADER],
    },
    {
        "key": "process_intensification",
        "name": "Process Intensification: Doing More With Smaller Plants",
        "group": "Deep",
        "ladder_rank": 22,
        "ladder_tier": "deep",
        "problem": (
            "Chemical plants are cathedrals of steel - distillation columns "
            "tens of metres tall, reactor trains sprawling over hectares. "
            "Process intensification asks: what if reaction and separation "
            "happened in one unit, at a tenth the size? Reactive "
            "distillation, dividing-wall columns, spinning disc reactors - "
            "each proven somewhere, none routine. The unsolved problem: how "
            "to design intensified units predictably, control their coupled "
            "dynamics, and convince a conservative industry to bet "
            "billion-dollar plants on them."
        ),
        "background": (
            "Stankiewicz and Moulijn's 2000 manifesto defined the field: "
            "smaller, cleaner, more energy-efficient processing through "
            "multifunctional units. Reactive distillation - reacting while "
            "distilling - is the flagship success, commercial for fuel "
            "ethers like MTBE since the 1980s. Dividing-wall columns, which "
            "do the work of two columns in one shell, followed. But each "
            "success took decades of dedicated development, and the design "
            "methods remain bespoke: coupling reaction and separation "
            "couples their dynamics too, making control harder and scale-up "
            "riskier. Industry's conservatism is rational - a failed "
            "intensified unit fails the whole plant."
        ),
        "why_it_matters": (
            "Intensified plants use less steel, less energy, less land, and "
            "less inventory of hazardous material - inherently safer as well "
            "as cheaper. For distributed manufacturing - small plants near "
            "feedstocks or markets - intensification is enabling, not just "
            "improving. It is the difference between chemical production as "
            "megaproject and as appliance."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the coupling-complexity model, and the confirm-or-"
            "refute panel. In one line: the Signature approach scores each "
            "intensification by size saved versus control complexity added, "
            "and proposes the dynamics test that would decide whether the "
            "coupling is controllable."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats intensification as a "
            "trade ledger: every unit operation merged saves size and "
            "energy but adds dynamic coupling - and the coupling is where "
            "projects die.\\n\\n"
            "ASSUMPTIONS: (1) The baseline is the conventional separate-"
            "units flowsheet for the same product and capacity. (2) Size, "
            "energy, and inventory reductions are counted from published "
            "case studies. (3) Control complexity is counted honestly: "
            "coupled dynamics need multivariable control. (4) The risk "
            "premium of novel units is a real term - first-of-a-kind costs "
            "more.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Map the conventional "
            "flowsheet and identify merge candidates: reaction with "
            "separation is the classic. Step 2 - Compute the prize: typical "
            "reactive distillation saves 20-80 percent of capital and "
            "energy for suitable systems. Step 3 - Model the coupled "
            "dynamics: the merged unit has interacting time constants - "
            "simulate disturbances, not just steady state. Step 4 - Price "
            "the control layer and the risk premium against the savings.\\n\\n"
            "PROPOSED MECHANISM: the winners are systems where reaction "
            "and separation help each other - equilibrium-limited reactions "
            "where removing product drives conversion. The demo walks a "
            "reactive-distillation case with its dynamics.\\n\\n"
            "WHAT WOULD CONFIRM IT: a first-of-a-kind intensified plant "
            "publishing capital, energy, and controllability data beating "
            "the conventional baseline. WHAT WOULD KILL IT: coupled "
            "dynamics proving uncontrollable at commercial scale for all "
            "but a handful of forgiving chemistries - intensification "
            "permanently niche.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim intensification fits "
            "every process, does not claim the design methods are mature, "
            "and does not claim industry conservatism is irrational."
        ),
        "key_points": [
            "Merging reaction and separation can cut plant size and energy dramatically - reactive distillation is the proven flagship.",
            "Merged units have coupled dynamics: harder to control, harder to scale up, riskier to bet on.",
            "The winners are equilibrium-limited reactions where removing product drives conversion.",
            "Design methods remain bespoke; each success took decades of dedicated development.",
            "The Signature approach ledgers size saved versus control complexity added.",
        ],
        "citations": [CIT_STANKIEWICZ, CIT_SMITH_DESIGN],
    },
    {
        "key": "beyond_distillation",
        "name": "Replacing Distillation: Separations Without Boiling",
        "group": "Deep",
        "ladder_rank": 23,
        "ladder_tier": "deep",
        "problem": (
            "Distillation - boiling mixtures apart - is the most energy-"
            "hungry unit operation in industry, estimated at 10 to 15 "
            "percent of US industrial energy. It is also gloriously "
            "reliable, which is why it survives. Membranes, adsorption, "
            "extraction, and electrochemical separations each promise to "
            "do the job without the boiling - and each has beaten "
            "distillation somewhere, yet distillation still dominates. The "
            "unsolved problem: which separations can actually displace "
            "distillation at scale, and what combination of new materials "
            "and process designs gets there."
        ),
        "background": (
            "The 'separations grand challenge' was articulated in a 2016 "
            "US DOE-linked analysis: separations are the hidden energy "
            "sink of manufacturing. Successes exist - membranes for "
            "nitrogen generation, pressure-swing adsorption for hydrogen "
            "purification, pervaporation for ethanol dehydration - but they "
            "are islands. The pattern: alternatives win where the mixture "
            "is dilute, the product valuable, or the boiling points close "
            "(where distillation is weakest). Electrochemical separations - "
            "using voltage instead of heat to drive selective transport - "
            "are the newest contender, promising to separate with "
            "electrons the way distillation does with steam."
        ),
        "why_it_matters": (
            "Separations are the invisible energy tax inside every chemical "
            "product. Displacing even a quarter of distillation duty would "
            "be among the largest single industrial energy savings "
            "available. It is also the enabler for electrified chemical "
            "plants: electrons replacing steam as the separation driver."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the separation-difficulty map, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "maps every major industrial separation by difficulty and "
            "proposes the pilot test that would decide whether "
            "electrochemical methods can take the hardest cases."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the distillation-"
            "replacement problem as a difficulty map: rank industrial "
            "separations by how hard distillation finds them, and attack "
            "from the hard end - because the easy ones are already "
            "replaced.\\n\\n"
            "ASSUMPTIONS: (1) The separation set is the major industrial "
            "duties: olefin-paraffin, ethanol-water, xylene isomers, air "
            "separation, CO2 capture. (2) Difficulty is scored by relative "
            "volatility or equivalent - close boilers are distillation's "
            "weakness. (3) Alternatives are counted with their real "
            "selectivities and fluxes, not ideal values. (4) The incumbent "
            "distillation energy is the bar, including heat integration.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Rank the duties: "
            "propylene-propane splitting, with relative volatility near "
            "1.1, needs 100+ trays - distillation at its worst. Step 2 - "
            "Match alternatives to duties: membranes for olefin-paraffin, "
            "adsorption for xylenes, pervaporation for azeotropes. Step 3 - "
            "Score the electrochemical contenders on the same map: where "
            "does voltage-driven separation beat heat-driven? Step 4 - "
            "Price the hybrids: membrane-distillation combinations often "
            "beat either alone.\\n\\n"
            "PROPOSED MECHANISM: the close-boiling separations are the "
            "beachhead - distillation is weakest there, so alternatives "
            "need the smallest advantage to win. The demo walks the "
            "difficulty map for five major duties.\\n\\n"
            "WHAT WOULD CONFIRM IT: an electrochemical or membrane system "
            "displacing a commercial olefin-paraffin splitter with "
            "published energy and cost data. WHAT WOULD KILL IT: the "
            "alternatives proving unable to reach the purities distillation "
            "delivers - 99.9%+ - at any scale, capping them as pre-"
            "concentrators forever.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim distillation will "
            "disappear, does not claim any alternative is ready for the "
            "hardest duties, and does not claim hybrids are always optimal."
        ),
        "key_points": [
            "Distillation consumes an estimated 10-15% of US industrial energy - the hidden tax in every chemical product.",
            "Alternatives (membranes, adsorption, pervaporation) have won islands - nitrogen, hydrogen, ethanol dehydration - but not the mainland.",
            "Distillation is weakest at close-boiling separations like propylene-propane: the beachhead for alternatives.",
            "Electrochemical separations promise voltage-driven instead of heat-driven separation.",
            "The Signature approach maps separations by difficulty and attacks from the hard end.",
        ],
        "citations": [CIT_SEADER, CIT_CHU],
    },
    {
        "key": "solid_oxide_electrolysis",
        "name": "High-Temperature Electrolysis: Letting Heat Pay Part of the Bill",
        "group": "Deep",
        "ladder_rank": 24,
        "ladder_tier": "deep",
        "problem": (
            "Splitting water or CO2 with electricity gets cheaper when it "
            "gets hotter: at 800 C, heat supplies about a fifth of the "
            "reaction energy for steam electrolysis. Solid oxide "
            "electrolysis cells exploit this - but they are ceramic "
            "devices running near 1000 C, and ceramics crack, seals fail, "
            "and stacks degrade. The unsolved problem: solid oxide cells "
            "durable enough for decades of thermal cycling, cheap enough "
            "to manufacture at scale, and integrated with real heat "
            "sources - nuclear, solar thermal, or industrial waste heat."
        ),
        "background": (
            "High-temperature electrolysis was demonstrated in the 1980s "
            "HotElly project, then languished as cheap natural gas made "
            "hydrogen from reforming. The 2020s revived it: Hauch's 2020 "
            "Science review documented rapid progress in cell performance "
            "and the remaining durability gap. The thermodynamic advantage "
            "is real - at 800 C roughly a fifth of steam-electrolysis "
            "energy can come as heat - but the engineering is brutal: chromium "
            "poisoning from interconnects, nickel coarsening, seal "
            "failures, and degradation rates still above the 0.5 percent "
            "per thousand hours the industry wants. Integration with a "
            "heat source adds a whole second plant to the project."
        ),
        "why_it_matters": (
            "If durable, solid oxide electrolysis makes the cheapest green "
            "hydrogen wherever high-temperature heat exists - and enables "
            "co-electrolysis of water and CO2 directly to syngas, the "
            "feedstock for synthetic fuels. It is the bridge between the "
            "heat world and the hydrogen world."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the heat-electricity split model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "computes exactly how much heat displaces electricity at each "
            "temperature and proposes the durability test that would "
            "decide whether the ceramic gamble pays."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats high-temperature "
            "electrolysis as a heat-electricity split: thermodynamics "
            "sets how much of the energy can be heat at each temperature, "
            "and durability decides whether the split is bankable.\\n\\n"
            "ASSUMPTIONS: (1) The split follows dG = dH - T*dS: as "
            "temperature rises, the electrical share (dG) falls and the "
            "heat share (T*dS) rises. (2) Heat is counted at its real cost "
            "- free waste heat versus built-for-purpose nuclear heat are "
            "different ledgers. (3) Degradation is measured as voltage "
            "rise per thousand hours at constant current. (4) Thermal "
            "cycling - not just steady operation - is in the test.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Compute the split: for "
            "steam electrolysis, at 800 C roughly 20 percent of the "
            "energy can be heat. Step 2 - Price the heat: with free industrial "
            "waste heat the economics transform; with dedicated heat they "
            "may not. Step 3 - Measure the decay: chromium poisoning, "
            "nickel coarsening, seal leaks - each a degradation rate. Step "
            "4 - Compare system cost against low-temperature electrolysis "
            "plus cheap electricity: the high-temp route must win on total "
            "hydrogen cost, not on elegance.\\n\\n"
            "PROPOSED MECHANISM: the heat source is the decision variable "
            "- co-location with nuclear or solar thermal is where the "
            "thermodynamic advantage becomes an economic one. The demo "
            "walks the split and the degradation ledger.\\n\\n"
            "WHAT WOULD CONFIRM IT: a stack demonstrating under 0.5 percent "
            "per thousand hours degradation through thermal cycles, with "
            "published hydrogen cost beating low-temp electrolysis at the "
            "same site. WHAT WOULD KILL IT: ceramic degradation proving "
            "intrinsic to the temperature - the materials science "
            "fundamentally unable to deliver decades of hot operation.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the thermodynamic "
            "advantage is free, does not claim heat sources are abundant "
            "where needed, and does not claim durability is close."
        ),
        "key_points": [
            "At 800 C, heat can supply roughly a fifth of steam-electrolysis energy - less electricity needed per kg of hydrogen.",
            "Ceramic cells near 1000 C face chromium poisoning, nickel coarsening, seal failures, and thermal-cycle cracking.",
            "Degradation rates remain above the 0.5% per thousand hours the industry wants.",
            "The heat source decides the economics: free waste heat transforms the ledger, dedicated heat may not.",
            "The Signature approach splits heat from electricity thermodynamically, then ledgers durability against it.",
        ],
        "citations": [CIT_HAUCH, CIT_CHU],
    },
    {
        "key": "artificial_photosynthesis",
        "name": "Artificial Photosynthesis at Industrial Scale",
        "group": "Frontier",
        "ladder_rank": 25,
        "ladder_tier": "frontier",
        "problem": (
            "Plants turn sunlight, water, and CO2 into fuel at planetary "
            "scale - but at about 1 percent efficiency, far too diffuse "
            "for industry. Artificial photosynthesis aims to do the same "
            "chemistry at ten times the efficiency in a device: photo-"
            "electrochemical cells that make hydrogen or carbon fuels "
            "directly from sunlight. Lab devices have hit impressive solar-"
            "to-hydrogen numbers, yet none survive the triple demand of "
            "efficiency, stability, and cost at once. The unsolved problem: "
            "a solar-fuels device that is efficient, durable for years "
            "outdoors, and cheap enough to matter."
        ),
        "background": (
            "Fujishima and Honda's 1972 water-splitting on titanium dioxide "
            "launched the field. Lewis and Nocera's 2006 'powering the "
            "planet' paper framed the scale: storing solar energy as fuel "
            "is the central chemical challenge of the energy transition. "
            "Barber's work on natural photosynthesis showed how Photosystem "
            "II splits water - the blueprint everyone copies and nobody "
            "matches for durability. The 2010s produced record devices: "
            "tandem absorbers over 19 percent solar-to-hydrogen, buried-"
            "junction designs, protective coatings. The failures are "
            "always the same two: the best absorbers corrode in water, and "
            "the stable ones are inefficient or made of rare elements."
        ),
        "why_it_matters": (
            "Solar fuels would solve renewable energy's storage problem at "
            "its root - sunlight in, storable fuel out, no batteries or "
            "grid required. For remote regions, islands, and eventually "
            "the whole fuels market, it is the most elegant answer ever "
            "proposed. Elegance is not enough; the device must also "
            "survive rain."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the photon-budget model, and the confirm-or-"
            "refute panel. In one line: the Signature approach counts "
            "photons from sun to fuel and proposes the outdoor durability "
            "test that would decide whether any device chemistry can pass "
            "all three demands."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats artificial "
            "photosynthesis as a photon budget: of every 100 photons "
            "arriving, count how many become fuel molecules - and count "
            "the device cost per photon processed.\\n\\n"
            "ASSUMPTIONS: (1) Solar input is AM1.5, 1000 W per square "
            "metre; efficiency is solar-to-fuel, end to end. (2) "
            "Durability means outdoor operation with day-night and weather "
            "cycling, not lab steady-state. (3) Cost is counted per square "
            "metre of device including balance of systems. (4) The fuel "
            "must be storable and separable - hydrogen that cannot be "
            "collected is not a product.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Draw the photon "
            "budget: absorption, charge separation, catalysis - losses at "
            "each stage multiply. Step 2 - Map the trilemma: efficient "
            "absorbers (silicon, III-Vs) corrode; stable oxides absorb "
            "poorly; protective coatings add cost and optical loss. Step 3 "
            "- Price the device per photon: the fuel value per square "
            "metre per year sets the allowable device cost. Step 4 - Test "
            "outdoors: the lab-to-roof gap has killed every champion "
            "device so far.\\n\\n"
            "PROPOSED MECHANISM: decoupling - PV plus electrolyzer, each "
            "optimized separately - currently beats integrated devices on "
            "all three demands; the integrated device must prove a "
            "decoupling-beating advantage. The demo walks the photon "
            "budget and the cost ceiling.\\n\\n"
            "WHAT WOULD CONFIRM IT: an integrated device holding 10%+ "
            "solar-to-fuel for 5,000+ outdoor hours at a published device "
            "cost under the fuel-value ceiling. WHAT WOULD KILL IT: the "
            "corrosion-efficiency trade-off proving fundamental - no "
            "absorber simultaneously efficient, stable in water, and "
            "earth-abundant.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim PV-plus-electrolyzer "
            "is the final answer, does not claim the trilemma is "
            "fundamental, and does not claim lab records predict outdoor "
            "life."
        ),
        "key_points": [
            "Plants do solar fuels at 1% efficiency; industry needs devices near 10%+ that survive years outdoors.",
            "The trilemma: efficient absorbers corrode in water, stable oxides absorb poorly, coatings add cost.",
            "Lab records (19%+ solar-to-hydrogen) have all died on the lab-to-roof gap.",
            "Decoupled PV-plus-electrolyzer currently beats integrated devices on efficiency, stability, and cost.",
            "The Signature approach budgets photons end-to-end and prices the device against fuel value per square metre.",
        ],
        "citations": [CIT_LEWIS_NOCERA, CIT_BARBER],
    },
    {
        "key": "ocean_capture",
        "name": "Direct Ocean Capture of CO2",
        "group": "Frontier",
        "ladder_rank": 26,
        "ladder_tier": "frontier",
        "problem": (
            "The ocean holds about 50 times as much carbon as the "
            "atmosphere, at roughly 100 times the concentration of air - "
            "about 2.2 millimoles of dissolved inorganic carbon per "
            "kilogram of seawater. Extracting CO2 from seawater should be "
            "far easier than from air - and the ocean reabsorbs from the "
            "atmosphere to replace it. The unsolved problem: how to strip "
            "CO2 from seawater at scale without the energy, the "
            "electrochemistry, or the ecological side effects eating the "
            "benefit."
        ),
        "background": (
            "Ocean CO2 extraction was proposed in the 1990s and "
            "demonstrated at lab scale in the 2010s, notably Eisaman's "
            "2012 bipolar-membrane electrodialysis work. The chemistry "
            "lever: shifting seawater pH converts bicarbonate to CO2 gas "
            "that can be stripped - but shifting the pH of millions of "
            "cubic metres of water takes energy and electrodes, and the "
            "acid-base balance must be restored before discharge or local "
            "ecosystems suffer. Startups in the 2020s began piloting "
            "electrochemical ocean capture, while the research community "
            "debates the energy ledger and the monitoring problem: proving "
            "that extracted CO2 is actually replaced by atmospheric drawdown "
            "and stays out."
        ),
        "why_it_matters": (
            "If the energy math works, ocean capture sidesteps DAC's "
            "dilution tax - the ocean already did the concentrating. It "
            "could also counter ocean acidification locally. But 'if the "
            "energy math works' is doing enormous work in that sentence, "
            "and the ocean is not a laboratory beaker."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the pH-swing energy ledger, and the confirm-or-"
            "refute panel. In one line: the Signature approach computes "
            "the energy price of the pH swing per tonne of CO2 and proposes "
            "the discharge-monitoring experiment that would decide whether "
            "the ocean really refills what is taken."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats ocean capture as a "
            "pH-swing ledger: the ocean's concentration advantage is real, "
            "and the price is the energy to swing pH down to release CO2 "
            "and back up for safe discharge.\\n\\n"
            "ASSUMPTIONS: (1) Seawater dissolved inorganic carbon near 2.2 "
            "mmol per kg; extraction efficiency per pass is measured, not "
            "assumed. (2) The pH swing energy is counted electrochemically "
            "- bipolar membranes, electrolysis - at real cell voltages. "
            "(3) Discharge water must return within regulatory pH bounds. "
            "(4) Atmospheric refill is counted only when measured, via "
            "tracers or monitoring, not assumed from equilibrium.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Compute the "
            "concentration advantage: 100x over air means 100x less water "
            "to process per tonne than air to process for DAC. Step 2 - "
            "Compute the swing price: acidifying to release CO2 then "
            "re-alkalizing, in kWh per tonne. Step 3 - Audit the side "
            "effects: electrode degradation in seawater, chlorine "
            "evolution, mineral scaling, local pH plumes. Step 4 - Verify "
            "the refill: the climate benefit exists only if the ocean "
            "draws down replacement CO2 from the air on relevant "
            "timescales.\\n\\n"
            "PROPOSED MECHANISM: the pH-swing energy is the binding term - "
            "if it exceeds the DAC dilution tax it was meant to dodge, "
            "the advantage evaporates. The demo walks the swing ledger "
            "against DAC.\\n\\n"
            "WHAT WOULD CONFIRM IT: a pilot publishing kWh per tonne "
            "below DAC benchmarks with monitored discharge and measured "
            "atmospheric refill. WHAT WOULD KILL IT: the swing energy "
            "plus side-effect mitigation proving permanently above DAC - "
            "or refill timescales proving too slow for the carbon to "
            "count.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the ocean is an "
            "infinite free concentrator, does not claim ecological safety "
            "is proven, and does not claim monitoring is easy."
        ),
        "key_points": [
            "The ocean holds 50x the carbon of the atmosphere at about 100x the concentration of air.",
            "The lever is pH: acidify seawater to release CO2 as gas, then restore alkalinity before discharge.",
            "The price is the electrochemical pH-swing energy - plus electrodes, scaling, chlorine, and pH plumes.",
            "Climate benefit requires measured atmospheric refill, not assumed equilibrium.",
            "The Signature approach ledgers the swing energy against the DAC dilution tax it was meant to dodge.",
        ],
        "citations": [CIT_EISAMAN, CIT_KEITH],
    },
    {
        "key": "lignin_valorization",
        "name": "Lignin: The Forgotten Half of Biomass",
        "group": "Frontier",
        "ladder_rank": 27,
        "ladder_tier": "frontier",
        "problem": (
            "A tree is roughly one-quarter lignin - the complex aromatic "
            "polymer that makes wood stiff - and the pulp, paper, and "
            "biorefinery industries produce about 50 million tonnes of it "
            "a year. Over 98 percent is simply burned for low-value heat. "
            "Lignin is the largest renewable source of aromatics on Earth, "
            "yet its irregular, cross-linked structure resists clean "
            "breakdown into useful chemicals. The unsolved problem: how to "
            "deconstruct lignin selectively into valuable aromatics at "
            "scale, instead of burning the most chemically interesting "
            "fraction of biomass."
        ),
        "background": (
            "Lignin's resistance is legendary - it evolved to resist "
            "degradation. Zakzeski's 2010 Chemical Reviews survey "
            "cataloged the catalytic strategies: hydrogenolysis, oxidation, "
            "pyrolysis, each giving complex mixtures. Ragauskas's 2014 "
            "Science paper reframed the problem: the lignin that leaves a "
            "pulp mill is already degraded by the pulping process - the "
            "real prize is 'native-like' lignin captured before harsh "
            "processing, as in lignin-first biorefining. Startups now "
            "chase lignin-derived carbon fiber, binders, and aromatic "
            "monomers, but selectivity and scale remain the twin walls."
        ),
        "why_it_matters": (
            "Aromatics - benzene, toluene, xylene - are the foundation of "
            "plastics, resins, and countless chemicals, all currently from "
            "oil. Lignin is the only large-scale renewable aromatic "
            "source. Cracking it would decarbonize a swath of the chemical "
            "industry and turn a waste stream worth pennies into products "
            "worth dollars."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the bond-cleavage selectivity model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "maps lignin's bond types by cleavability and proposes the "
            "lignin-first experiment that would decide whether selectivity "
            "is achievable at scale."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats lignin as a bond "
            "inventory: the polymer's linkages differ in cleavability, and "
            "selective valorization means cutting the weak ones while "
            "leaving the strong ones - or redesigning the upstream process "
            "to preserve cleavable bonds.\\n\\n"
            "ASSUMPTIONS: (1) Basis is one tonne of lignin at the "
            "biorefinery gate; pulping history is specified because it "
            "changes everything. (2) The beta-O-4 ether linkage is the "
            "cleavable target - up to 50 percent of native lignin bonds. "
            "(3) 'Selective' means a product slate narrow enough to "
            "separate economically. (4) The counterfactual - burning for "
            "process heat - is priced as the opportunity cost.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Inventory the bonds: "
            "native lignin is rich in cleavable ether linkages; kraft "
            "pulping destroys most of them. Step 2 - Compare strategies: "
            "deconstruct degraded lignin (hard) versus lignin-first "
            "processing that preserves the bonds (re-engineers the mill). "
            "Step 3 - Score the catalytic routes on selectivity and "
            "catalyst cost per tonne of product. Step 4 - Price the "
            "separation: complex mixtures are worthless without affordable "
            "fractionation.\\n\\n"
            "PROPOSED MECHANISM: lignin-first biorefining is the key move - "
            "the selectivity problem is largely created upstream by "
            "pulping, so the fix is upstream too. The demo walks the bond "
            "inventory and the selectivity ledger.\\n\\n"
            "WHAT WOULD CONFIRM IT: a lignin-first plant publishing "
            "aromatic monomer yields, selectivity, and cost per tonne at "
            "pilot scale. WHAT WOULD KILL IT: the product mixtures proving "
            "inseparable at any affordable cost - valorization permanently "
            "stuck at low-value materials like binders and carbon fiber "
            "feed.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim degraded lignin is "
            "worthless, does not claim lignin-first mills are cheap to "
            "build, and does not claim aromatics markets will absorb the "
            "volume."
        ),
        "key_points": [
            "About 50 million tonnes of lignin are produced yearly; over 98% is burned for low-value heat.",
            "Lignin is Earth's largest renewable source of aromatics - the foundation of plastics and resins.",
            "Pulping destroys the cleavable ether linkages; the selectivity problem is largely created upstream.",
            "Lignin-first biorefining preserves the bonds - the fix is upstream, not just better catalysts.",
            "The Signature approach inventories bonds by cleavability and ledgers selectivity against separation cost.",
        ],
        "citations": [CIT_ZAKZESKI, CIT_RAGAUSKAS],
    },
    {
        "key": "plasma_chemistry",
        "name": "Plasma Chemistry for Nitrogen Fixation and Methane Conversion",
        "group": "Frontier",
        "ladder_rank": 28,
        "ladder_tier": "frontier",
        "problem": (
            "A century ago, the Birkeland-Eyde process fixed nitrogen with "
            "electric arcs - and lost to Haber-Bosch on energy, 60 "
            "gigajoules per tonne of nitrogen versus 30. Plasma chemistry "
            "is back: non-thermal plasmas excite nitrogen's triple bond "
            "with electrons while the gas stays cool, promising fixation "
            "without 500 C and 300 bar. The same plasmas can activate "
            "methane, another stubborn molecule. The unsolved problem: "
            "whether plasma routes can beat the energy ledgers of the "
            "thermal incumbents instead of repeating Birkeland-Eyde's "
            "defeat with better marketing."
        ),
        "background": (
            "Fridman's Plasma Chemistry text systematized what plasmas do "
            "to molecules: electron impact creates radicals, excited "
            "states, and ions far from equilibrium. The 2010s saw a "
            "research surge in plasma nitrogen fixation - gliding arcs, "
            "dielectric barrier discharges - with reported energy costs "
            "approaching Haber-Bosch territory in the best cases, usually "
            "at tiny scale with idealized feeds. Plasma methane reforming "
            "and partial oxidation chase the same prize: activating "
            "methane without a furnace. The field's credibility problem "
            "is scale-up: plasma uniformity and energy efficiency both "
            "degrade as reactors grow."
        ),
        "why_it_matters": (
            "Plasma processes run on electricity and switch on and off "
            "instantly - ideal partners for intermittent renewables, "
            "unlike thermal plants that must run continuously. If the "
            "energy ledger closes, plasma enables small, distributed, "
            "renewable-driven chemical production: fertilizer where the "
            "wind blows, methane conversion where the gas is stranded."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the plasma energy ledger, and the confirm-or-"
            "refute panel. In one line: the Signature approach puts plasma "
            "routes on the same gigajoule-per-tonne ledger as Haber-Bosch "
            "and proposes the scale-up test that would decide whether the "
            "lab numbers survive growth."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats plasma chemistry as an "
            "energy ledger with history: Birkeland-Eyde's 60 GJ per tonne "
            "of nitrogen is the ghost at the table, and every plasma claim "
            "is measured against it and against Haber-Bosch's 30.\\n\\n"
            "ASSUMPTIONS: (1) Basis is one tonne of fixed nitrogen as "
            "nitric acid or ammonia equivalent. (2) Energy is counted "
            "wall-plug to product, including power supply losses - plasma "
            "power electronics are not free. (3) Feed is air or realistic "
            "gas, not pure nitrogen lab feeds. (4) Scale effects are "
            "counted: uniformity and efficiency at 1 kW do not transfer "
            "to 1 MW automatically.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Write the history: "
            "Birkeland-Eyde at 60 GJ per tonne lost to Haber-Bosch at 30; "
            "the gap is the target. Step 2 - Ledger the modern claims: "
            "best reported plasma nitrogen fixation near 20-40 GJ per "
            "tonne at lab scale - examine the feed and scale footnotes. "
            "Step 3 - Model the scale-up penalty: plasma uniformity "
            "degrades with volume; power supply efficiency matters at "
            "scale. Step 4 - Price the intermittency advantage: instant "
            "on-off has real value with renewable electricity that the "
            "GJ ledger alone misses.\\n\\n"
            "PROPOSED MECHANISM: the scale-up penalty is the decisive "
            "unknown - plasma physics favors small, and the field must "
            "prove numbering-up beats the penalty. The demo walks the "
            "ledger from Birkeland-Eyde to modern claims.\\n\\n"
            "WHAT WOULD CONFIRM IT: a plasma nitrogen unit at 100+ kW "
            "publishing wall-plug GJ per tonne on air feed within striking "
            "distance of Haber-Bosch. WHAT WOULD KILL IT: the scale-up "
            "penalty proving structural - efficiency collapsing with size "
            "in every reactor geometry tried.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim plasmas cannot win, "
            "does not claim Birkeland-Eyde's fate is sealed for all "
            "geometries, and does not claim the intermittency advantage "
            "outweighs a bad ledger."
        ),
        "key_points": [
            "Birkeland-Eyde's electric-arc nitrogen fixation lost to Haber-Bosch a century ago on energy: 60 vs 30 GJ per tonne.",
            "Non-thermal plasmas excite nitrogen with electrons while the gas stays cool - no 500 C, no 300 bar.",
            "Best modern lab claims approach Haber-Bosch territory - at tiny scale, on idealized feeds.",
            "Plasma uniformity and efficiency degrade with reactor size; the scale-up penalty is the decisive unknown.",
            "The Signature approach ledgers wall-plug energy against history and prices the intermittency advantage.",
        ],
        "citations": [CIT_FRIDMAN, CIT_SMIL],
    },
    {
        "key": "process_heat",
        "name": "Very-High-Temperature Process Heat Without Fire",
        "group": "Frontier",
        "ladder_rank": 29,
        "ladder_tier": "frontier",
        "problem": (
            "Cement needs 1450 C, steel 1600 C, glass 1500 C - temperatures "
            "no heat pump can reach and few electric heaters can sustain "
            "economically. Industry gets them from fire, and fire means "
            "carbon. Electrifying low-temperature heat is nearly solved; "
            "the frontier is very-high-temperature process heat: how to "
            "deliver 1000 C-plus heat from electricity, nuclear, or "
            "concentrated sun at industrial scale and cost."
        ),
        "background": (
            "High-temperature heat is the hardest part of industrial "
            "decarbonization - Davis's 2018 net-zero analysis flags the "
            "sectors where no alternative to combustion currently exists. "
            "Candidates: resistive and induction heating (proven at "
            "smaller scales, expensive at 1500 C), nuclear process heat "
            "from high-temperature gas reactors (designed, never "
            "commercialized for industry), concentrated solar thermal "
            "(demonstrated for cement and lime in pilot solar furnaces), "
            "and hydrogen combustion (clean at point of use, but hydrogen "
            "is expensive heat). Each faces the same ledger: the cost per "
            "megawatt-hour of high-temperature heat versus a gas flame."
        ),
        "why_it_matters": (
            "Cement and steel alone are about 15 percent of global CO2, "
            "and most of it is heat plus process chemistry. Without a "
            "clean very-high-temperature heat source, these sectors cannot "
            "decarbonize - full stop. This is the problem the energy "
            "transition cannot route around."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the heat-cost ledger by temperature band, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "prices clean heat per megawatt-hour in each temperature band "
            "and proposes the pilot comparison that would decide which "
            "source wins where."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats process heat as a "
            "temperature-band ledger: each band - 500, 1000, 1500 C - has "
            "different candidate sources, and the winner differs by band.\\n\\n"
            "ASSUMPTIONS: (1) Heat is compared per megawatt-hour thermal "
            "delivered at the required temperature, not per megawatt-hour "
            "electric. (2) Capacity factor counts: solar thermal needs "
            "storage or backup; nuclear runs flat out. (3) Retrofit versus "
            "greenfield are different ledgers - existing kilns constrain "
            "options. (4) The gas-flame baseline includes a carbon price "
            "scenario, stated explicitly.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Band the demand: which "
            "industries need which temperatures - cement 1450 C, steel "
            "1600 C, chemicals mostly below 800 C. Step 2 - Price each "
            "candidate per band: resistive electric, nuclear heat, solar "
            "thermal, hydrogen flame. Step 3 - Apply the constraints: "
            "solar needs storage for 24/7 kilns; nuclear needs siting and "
            "licensing; electric needs grid capacity. Step 4 - Find the "
            "crossovers: the carbon price at which each candidate beats "
            "gas in each band.\\n\\n"
            "PROPOSED MECHANISM: there is no single winner - the ledger "
            "predicts a band-by-band split, with electric winning low, "
            "nuclear and solar contesting high, hydrogen as the flexible "
            "backup. The demo walks the band ledger.\\n\\n"
            "WHAT WOULD CONFIRM IT: pilot plants publishing cost per "
            "tonne of clinker or steel for each heat source at temperature. "
            "WHAT WOULD KILL IT: all clean sources proving permanently "
            "above gas plus plausible carbon prices in the top band - the "
            "1500 C problem structurally unsolved.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim any source is ready "
            "today, does not claim the bands have sharp boundaries, and "
            "does not claim carbon prices will reach the crossover."
        ),
        "key_points": [
            "Cement needs 1450 C, steel 1600 C - temperatures heat pumps cannot reach and electric heaters struggle to sustain economically.",
            "Candidates: resistive/induction electric, nuclear process heat, concentrated solar thermal, hydrogen combustion.",
            "Each band has a different winner; there is no single clean-heat source.",
            "Solar needs storage for 24/7 kilns; nuclear needs licensing; electric needs massive grid capacity.",
            "The Signature approach ledgers cost per MWh thermal by temperature band and finds the carbon-price crossovers.",
        ],
        "citations": [CIT_DAVIS, CIT_ALLWOOD],
    },
    {
        "key": "numbering_up",
        "name": "Numbered-Up Manufacturing: A Thousand Small Reactors",
        "group": "Frontier",
        "ladder_rank": 30,
        "ladder_tier": "frontier",
        "problem": (
            "The scale-up problem (record 8) has a radical answer: don't "
            "scale up - number up. Run a thousand identical microreactors "
            "in parallel instead of one giant vessel. Each unit keeps its "
            "perfect heat transfer and mixing; capacity grows by adding "
            "units. The unsolved problem: the systems engineering of "
            "numbering-up - flow distribution across thousands of "
            "channels, maintenance without shutting the plant, control "
            "of a thousand units as one, and cost that beats the big "
            "vessel."
        ),
        "background": (
            "Jensen's 2001 paper asked 'is small better?' and the "
            "microreactor field spent two decades answering: for fast, "
            "exothermic, or hazardous chemistry, yes - spectacularly. "
            "Ehrfeld's microreactor work showed the transport advantages "
            "are real. What lagged is the plant-level engineering: "
            "distributing flow evenly to thousands of parallel channels "
            "(maldistribution kills the advantage), detecting and isolating "
            "a failed unit among thousands, and the control architecture. "
            "The pharmaceutical and fine-chemical industries, with small "
            "volumes and high values, are the natural first adopters; "
            "commodity chemicals at million-tonne scale remain the "
            "unconquered territory."
        ),
        "why_it_matters": (
            "Numbering-up would retire the pilot plant, collapse the "
            "lab-to-market timeline from years to months, and make chemical "
            "production modular - built in factories, shipped in "
            "containers, deployed where needed. It is the manufacturing "
            "paradigm shift the field has promised for twenty years."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the parallel-reliability model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models a thousand-unit plant's reliability and cost, and "
            "proposes the maldistribution test that would decide whether "
            "the parallel advantage survives at scale."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats numbering-up as a "
            "reliability and distribution problem: a thousand perfect "
            "reactors are only as good as the manifold feeding them and "
            "the system tolerating their failures.\\n\\n"
            "ASSUMPTIONS: (1) Basis is a plant of 1,000 parallel units at "
            "a target total throughput. (2) Each unit has a measured "
            "failure rate; failures are independent unless shown "
            "otherwise. (3) Flow maldistribution is measured, with a "
            "tolerance band for acceptable non-uniformity. (4) Maintenance "
            "means hot-swapping units without stopping the plant.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Compute the "
            "reliability: with 1,000 units and realistic failure rates, "
            "several units are always down - the plant must be designed "
            "for N-minus-k operation. Step 2 - Model the manifold: flow "
            "distribution across parallel channels, and how one blocked "
            "channel redistributes flow to its neighbors. Step 3 - Design "
            "the control: a thousand units need hierarchical control, not "
            "a thousand controllers. Step 4 - Price it: manifolds, valves, "
            "sensors, and spares against the avoided cost of the big "
            "vessel and its pilot plant.\\n\\n"
            "PROPOSED MECHANISM: the manifold is the product - unit "
            "chemistry is solved; uniform distribution and graceful "
            "degradation are not. The demo walks the reliability math and "
            "the maldistribution model.\\n\\n"
            "WHAT WOULD CONFIRM IT: a thousand-channel plant publishing "
            "uptime, distribution uniformity, and cost per tonne beating "
            "the conventional route. WHAT WOULD KILL IT: maldistribution "
            "or maintenance complexity proving to scale worse than the "
            "units themselves - the parallel plant permanently more "
            "trouble than the big vessel.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim microreactors are "
            "always better, does not claim the manifold problem is solved, "
            "and does not claim commodity scale is near."
        ),
        "key_points": [
            "Numbering-up sidesteps scale-up: capacity grows by adding identical small units, each with perfect transport.",
            "The hard problems move to the manifold: flow distribution, failure isolation, hierarchical control.",
            "With 1,000 units, several are always down - the plant must be designed for graceful degradation.",
            "Fine chemicals and pharma are the natural first adopters; commodity scale is unconquered.",
            "The Signature approach models reliability and maldistribution before the plant is built.",
        ],
        "citations": [CIT_JENSEN, CIT_EHRFELD],
    },
    {
        "key": "inverse_catalyst_design",
        "name": "Inverse Catalyst Design: Designing the Active Site First",
        "group": "Frontier",
        "ladder_rank": 31,
        "ladder_tier": "frontier",
        "problem": (
            "Catalyst discovery is still largely Edisonian: make hundreds "
            "of formulations, test them, keep the winner, repeat. "
            "Computational catalysis promised to invert this - compute the "
            "ideal active site from theory, then synthesize it. Density "
            "functional theory can now screen thousands of surfaces, and "
            "descriptor-based 'volcano plots' predict optimal binding "
            "energies. Yet the designed catalysts that actually work in "
            "plants remain rare. The unsolved problem: closing the loop "
            "from computation to a working, stable, manufacturable "
            "catalyst - the 'materials genome' dream for catalysis."
        ),
        "background": (
            "The Sabatier principle - not too strong, not too weak binding "
            "- was quantified into volcano plots relating activity to "
            "adsorption energies, a triumph of the 2000s computational "
            "catalysis wave. Norskov and colleagues showed descriptors "
            "could screen alloy catalysts computationally. The Materials "
            "Project and similar databases made structures and energies "
            "searchable. But the gaps persist: DFT errors are comparable "
            "to the energy differences that matter; real catalysts "
            "restructure under reaction conditions, invalidating the "
            "computed surface; and synthesizing the predicted site "
            "atom-by-atom is often impossible. Machine learning now "
            "accelerates the screening - but screening is not design."
        ),
        "why_it_matters": (
            "Every catalyst in this database's other records - ammonia, "
            "CO2, plastics, steel - could in principle be designed rather "
            "than discovered. Inverse design working would compress "
            "decades of trial-and-error into computation, and it is the "
            "prerequisite for catalysts too complex to find by luck."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the volcano-plot model, and the confirm-or-"
            "refute panel. In one line: the Signature approach computes "
            "the volcano optimum, audits the error bars, and proposes the "
            "closed-loop test that would decide whether computation can "
            "truly lead synthesis."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats inverse design as an "
            "error-bar problem: the volcano plot points to the optimum, "
            "but DFT uncertainty is as wide as the peak - and the "
            "synthesis step is where predictions go to be tested.\\n\\n"
            "ASSUMPTIONS: (1) The Sabatier volcano is the organizing "
            "model: activity peaks at intermediate binding energy. (2) "
            "DFT adsorption-energy errors near 0.1-0.2 eV are counted "
            "honestly against volcano widths. (3) Surface restructuring "
            "under reaction conditions is assumed unless proven absent. "
            "(4) 'Designed' means synthesized as predicted and active as "
            "predicted - not merely screened.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Build the volcano: "
            "compute the descriptor-activity relation for the reaction "
            "family. Step 2 - Audit the error bars: overlay DFT "
            "uncertainty on the volcano peak - if the peak is narrower "
            "than the error, the prediction is noise. Step 3 - Check "
            "restructuring: does the predicted surface survive the "
            "reaction environment? Step 4 - Close the loop: synthesize "
            "the top candidates and measure - the hit rate is the metric "
            "of the whole enterprise.\\n\\n"
            "PROPOSED MECHANISM: the error-bar audit is the missing "
            "discipline - most 'designed' catalysts were lucky screens. "
            "The demo builds a volcano plot with honest error bars.\\n\\n"
            "WHAT WOULD CONFIRM IT: a documented campaign where "
            "computation-first candidates beat Edisonian baselines at a "
            "published hit rate, with the winners stable in operando. "
            "WHAT WOULD KILL IT: restructuring and error bars proving "
            "that computation can rank but never truly lead - design "
            "permanently downstream of experiment.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim DFT is useless, "
            "does not claim the volcano model is wrong, and does not "
            "claim machine learning changes the error bars by itself."
        ),
        "key_points": [
            "Catalyst discovery remains largely trial-and-error despite decades of computational screening.",
            "Volcano plots predict optimal binding energies - but DFT error bars are often as wide as the peak.",
            "Real catalysts restructure under reaction conditions, invalidating the computed surface.",
            "Synthesizing a predicted active site atom-by-atom is often impossible.",
            "The Signature approach audits error bars against volcano width and measures the closed-loop hit rate.",
        ],
        "citations": [CIT_SATTERFIELD, CIT_LEVENSPIEL],
    },
    {
        "key": "digital_twin_plant",
        "name": "The Digital Twin Plant: Controlling the Uncontrollable",
        "group": "Frontier",
        "ladder_rank": 32,
        "ladder_tier": "frontier",
        "problem": (
            "A modern chemical plant has thousands of sensors and "
            "control loops, yet operators still run it conservatively - "
            "far from optimal - because no model captures the whole "
            "beast. The digital twin promises a live, physics-based mirror "
            "of the plant: every unit operation simulated in real time, "
            "predicting upsets before they happen, optimizing continuously. "
            "The unsolved problem: a twin faithful enough to trust with "
            "real decisions - and the control architecture that acts on it "
            "without a human in the loop for every move."
        ),
        "background": (
            "Model predictive control has optimized refineries since the "
            "1980s, but always on reduced models of pieces of the plant. "
            "The digital-twin concept - a full-fidelity live mirror - "
            "arrived with cheap computing and industrial IoT sensors in "
            "the 2010s. Venkatasubramanian's 2019 AIChE perspective "
            "surveyed AI's promise for chemical engineering: fault "
            "diagnosis, soft sensors, optimization. The hard parts are "
            "model maintenance (the twin drifts from the plant as "
            "equipment ages), the computational cost of full-fidelity "
            "simulation in real time, and trust: no operator bets a "
            "billion-dollar plant on a model they cannot interrogate."
        ),
        "why_it_matters": (
            "Plants run conservatively waste energy, make off-spec "
            "product, and respond slowly to upsets. A trustworthy twin "
            "would squeeze percent-level efficiency from every plant on "
            "Earth - and percent-level, times the whole chemical "
            "industry, is gigatonne-level. It is also the prerequisite "
            "for autonomous chemical plants."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the twin-fidelity model, and the confirm-or-"
            "refute panel. In one line: the Signature approach measures "
            "twin drift against plant reality and proposes the upset-"
            "prediction test that would decide whether the twin earns "
            "control authority."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the digital twin as a "
            "fidelity ledger: the twin's predictions are scored against "
            "plant measurements continuously, and control authority is "
            "earned in proportion to demonstrated fidelity - never "
            "granted.\\n\\n"
            "ASSUMPTIONS: (1) Fidelity is measured per unit operation and "
            "per operating regime - a twin faithful at steady state may "
            "lie during upsets. (2) Model drift is expected: fouling, "
            "catalyst aging, and sensor drift move the plant away from "
            "the twin. (3) Control actions proposed by the twin are "
            "simulated against safety constraints before execution. (4) "
            "The human operator retains veto; autonomy is graduated.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Score the twin: "
            "prediction error on held-out plant data, by unit and regime. "
            "Step 2 - Track the drift: re-score continuously; schedule "
            "recalibration when fidelity decays. Step 3 - Test upset "
            "prediction: the twin must foresee a set of historical upsets "
            "before it advises on future ones. Step 4 - Graduate "
            "authority: advisory, then supervisory with veto, then closed-"
            "loop on bounded decisions - each step gated on measured "
            "performance.\\n\\n"
            "PROPOSED MECHANISM: graduated authority gated on measured "
            "fidelity is the trust architecture - the industry's "
            "conservatism is a feature to design with, not a bug to "
            "override. The demo simulates a twin tracking a drifting "
            "plant.\\n\\n"
            "WHAT WOULD CONFIRM IT: a plant publishing twin fidelity "
            "scores and the efficiency gains under graduated autonomous "
            "control. WHAT WOULD KILL IT: drift proving faster than "
            "recalibration in real plants - the twin permanently a step "
            "behind the reality it must control.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim full autonomy is "
            "near, does not claim models can replace operators, and does "
            "not claim fidelity is achievable for all units."
        ),
        "key_points": [
            "Plants run conservatively because no model captures the whole process; the twin promises a live physics mirror.",
            "Model drift - fouling, aging, sensor decay - moves the plant away from the twin continuously.",
            "Upset prediction, not steady-state matching, is the fidelity test that matters.",
            "Trust requires graduated authority: advisory, then supervised, then bounded closed-loop.",
            "The Signature approach scores fidelity per unit and regime, and gates authority on measured scores.",
        ],
        "citations": [CIT_STEPHANOPOULOS, CIT_VENKAT],
    },
    {
        "key": "biomanufacturing_scale",
        "name": "Biomanufacturing at Chemical-Plant Scale",
        "group": "Frontier",
        "ladder_rank": 33,
        "ladder_tier": "frontier",
        "problem": (
            "Engineered microbes can now make an astonishing catalog - "
            "fuels, plastics monomers, fragrances, drugs - from sugar. But "
            "almost all of it happens at pilot scale: titers too low, "
            "rates too slow, and separation costs that devour the "
            "economics. Scaling fermentation from a 10-litre lab vessel "
            "to a 500-cubic-metre production fermenter reintroduces every "
            "scale-up demon, plus biological ones: mutation, contamination, "
            "and cells that simply stop producing. The unsolved problem: "
            "precision fermentation that competes with petrochemistry on "
            "cost at real scale."
        ),
        "background": (
            "Industrial biotechnology has genuine wins: insulin, amino "
            "acids, and more recently bio-based 1,3-propanediol and "
            "farnesene at commercial scale. Nielsen and Keasling's 2016 "
            "review mapped the metabolic engineering toolkit that made "
            "them possible. But the wins share a pattern - high-value, "
            "low-volume products. Commodity chemicals need grams per "
            "litre per hour at cents per kilogram, and the titer-rate-yield "
            "triangle binds: pushing titer usually costs rate, pushing "
            "rate costs yield. Downstream separation from dilute "
            "fermentation broth is often the dominant cost, and biology "
            "adds failure modes chemistry never had."
        ),
        "why_it_matters": (
            "Biomanufacturing is the renewable route to the entire "
            "chemical product slate - drop-in replacements for "
            "petrochemicals made from biomass instead of oil. If the "
            "scale economics close, it decouples chemicals from fossil "
            "feedstocks without rebuilding every downstream process."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the titer-rate-yield triangle model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "prices the fermentation plus separation as one system and "
            "proposes the scale-translation test that would decide whether "
            "lab metrics predict plant economics."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats biomanufacturing as a "
            "system ledger: fermentation metrics and separation costs are "
            "one coupled economy, and lab numbers are translated to plant "
            "numbers with explicit scale penalties.\\n\\n"
            "ASSUMPTIONS: (1) The metric triple is titer (g/L), rate "
            "(g/L/h), and yield (g product per g feedstock) - all three, "
            "not the best one. (2) Separation cost is estimated from the "
            "broth concentration: dilute broth means expensive recovery. "
            "(3) Scale penalties apply: mixing, oxygen transfer, and "
            "sterility all degrade with fermenter size. (4) Strain "
            "stability is measured over production-relevant generations, "
            "not lab timescales.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Score the strain on "
            "all three metrics; the triangle binds - titer, rate, and "
            "yield trade against each other. Step 2 - Price the "
            "separation: at 50 g/L the recovery looks nothing like at 5 "
            "g/L. Step 3 - Apply scale penalties: oxygen transfer and "
            "mixing at 500 cubic metres versus 10 litres. Step 4 - "
            "Compare against the petrochemical incumbent per kilogram, "
            "including feedstock cost scenarios.\\n\\n"
            "PROPOSED MECHANISM: separation from dilute broth is usually "
            "the dominant cost - so strain engineering should optimize "
            "for titer first, even at some cost to rate. The demo walks "
            "the triangle and the system cost.\\n\\n"
            "WHAT WOULD CONFIRM IT: a commodity molecule produced by "
            "fermentation at published cost parity with the petrochemical "
            "route, with full titer-rate-yield and separation data. WHAT "
            "WOULD KILL IT: the triangle proving too tight - no strain "
            "achieving all three metrics at once for commodity targets, "
            "capping biomanufacturing at specialties permanently.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim fermentation will "
            "replace petrochemistry broadly, does not claim the wins to "
            "date generalize, and does not claim biology's failure modes "
            "are tamed."
        ),
        "key_points": [
            "Engineered microbes make an astonishing catalog - but almost all at pilot scale, for high-value products.",
            "The titer-rate-yield triangle binds: pushing one metric usually costs the others.",
            "Separation from dilute broth is often the dominant cost - titer matters more than rate.",
            "Scale-up adds biological failure modes: mutation, contamination, production loss.",
            "The Signature approach ledgers fermentation plus separation as one coupled economy.",
        ],
        "citations": [CIT_NIELSEN, CIT_CUSSLER],
    },
    {
        "key": "grand_electrified_industry",
        "name": "The Grand Compound Challenge: A Fully Electrified, Carbon-Neutral Chemical Industry",
        "group": "Frontier",
        "ladder_rank": 34,
        "ladder_tier": "frontier",
        "problem": (
            "This is the compound problem that contains all the others: "
            "the chemical industry - 10 percent or more of global CO2, "
            "the maker of everything - rebuilt to run on electricity and "
            "renewable carbon instead of fossil fuels and fire. It demands "
            "clean hydrogen at scale, very-high-temperature heat without "
            "combustion, electrified separations, carbon-neutral "
            "feedstocks, and plants redesigned around electrons instead of "
            "steam. No single technology does it; the unsolved problem is "
            "the system: which combination, in which order, at what cost, "
            "on what timeline - and whether the pieces fit together at "
            "all."
        ),
        "background": (
            "Davis's 2018 Science analysis laid out the net-zero energy "
            "system and named the hard sectors honestly. The chemical "
            "industry's emissions split roughly three ways: energy for "
            "heat and power, process chemistry (like cement's "
            "calcination), and feedstock carbon embedded in products. Each "
            "record in this database attacks one piece - hydrogen, heat, "
            "separations, feedstocks, capture. The systems literature - "
            "Stephanopoulos and Reklaitis on process systems engineering - "
            "provides the integration methods, but the full-plant, "
            "full-sector electrified designs exist mostly as scenarios, "
            "not blueprints. The open question is compositional: the "
            "pieces are studied separately, and nobody has shown they "
            "compose."
        ),
        "why_it_matters": (
            "Everything is downstream of this. Plastics, fertilizer, "
            "steel, cement, fuels - the material basis of civilization - "
            "either get remade carbon-neutral or the climate math fails. "
            "This record is the map of the whole territory the other 33 "
            "records explore."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the sector-composition model, and the confirm-or-"
            "refute panel. In one line: the Signature approach assembles "
            "the industry's emissions piece by piece, assigns each piece "
            "to its best challenger technology, and proposes the "
            "integration test that would decide whether the pieces compose."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the electrified "
            "chemical industry as a composition problem: decompose "
            "emissions by sector and cause, assign each piece the best "
            "challenger from this database's records, and check whether "
            "the assignments are mutually consistent.\\n\\n"
            "ASSUMPTIONS: (1) Industry emissions near 10 percent of global "
            "CO2, split into heat, process chemistry, and feedstock "
            "carbon. (2) Each challenger technology is counted at its "
            "demonstrated performance, not its roadmap. (3) Electricity "
            "supply is counted: a fully electrified industry needs "
            "multiple times today's clean electricity. (4) Timeline "
            "matters: plant lifetimes are 30-50 years, so the transition "
            "is paced by capital turnover.\\n\\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Decompose: ammonia, "
            "steel, cement, ethylene, and the rest - each with its "
            "emissions split. Step 2 - Assign: green hydrogen to ammonia "
            "and steel, clean heat to cement, electrified separations "
            "across the board, biomass or captured CO2 for feedstocks. "
            "Step 3 - Check consistency: do the assignments compete for "
            "the same clean electricity? For the same biomass? Step 4 - "
            "Sequence: which pieces must come first because others depend "
            "on them - hydrogen before green steel, for example.\\n\\n"
            "PROPOSED MECHANISM: the binding constraints are clean-"
            "electricity supply and capital turnover pace - technology "
            "readiness is necessary but not sufficient. The demo walks "
            "the sector decomposition and the consistency check.\\n\\n"
            "WHAT WOULD CONFIRM IT: integrated roadmaps where sector "
            "assignments pass the consistency check with published "
            "electricity and biomass budgets. WHAT WOULD KILL IT: the "
            "constraints proving mutually unsatisfiable - not enough "
            "clean electricity, not enough biomass, not enough capital "
            "turnover - making full electrification a physical "
            "impossibility on the needed timeline.\\n\\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the transition is "
            "on track, does not claim any timeline is achievable, and "
            "does not claim the pieces compose - that is exactly what is "
            "being tested."
        ),
        "key_points": [
            "The chemical industry is 10%+ of global CO2: heat, process chemistry, and feedstock carbon together.",
            "Every record in this database attacks one piece; this record asks whether the pieces compose.",
            "Assignments must pass consistency checks: they compete for the same clean electricity and biomass.",
            "Plant lifetimes of 30-50 years pace the transition through capital turnover.",
            "The Signature approach decomposes by sector, assigns challengers, and tests mutual consistency.",
        ],
        "citations": [CIT_DAVIS, CIT_STEPHANOPOULOS, CIT_CHU],
    },
]

assert len(ENTRIES) == 34, "need exactly 34 entries, got %d" % len(ENTRIES)
assert [e["ladder_rank"] for e in ENTRIES] == list(range(1, 35)), "ladder ranks must be 1..34"
