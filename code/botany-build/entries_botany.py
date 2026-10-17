#!/usr/bin/env python3
"""Seed entries for the Botany field build (field #4, taxonomy order).

Verified 2026-10-17: the manifest holds an `everything-biology` database
with 12 records, only ONE of which is botany ("Botany: Photosynthesis and
Plant Structure") — thin, single-record coverage of a whole discipline.
So this build creates two NEW databases:

  botany              — The Botany Database (public-harvest: real,
                        fact-checked botany — plant anatomy and morphology,
                        photosynthesis, plant physiology, taxonomy and
                        systematics (APG IV), plant ecology, plant genetics,
                        plant pathology, economic botany, bryophytes, ferns,
                        gymnosperms, angiosperms)
  botany-signature    — The Botany Signature Database (his original
                        Signature interpretation; src signature, titles
                        suffixed " (Signature Edition)", never presented as
                        authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

# Shared citation tails
CIT_RAVEN = ("Raven, P. H., Evert, R. F., & Eichhorn, S. E. (2013). "
             "'Biology of Plants', 8th ed. W. H. Freeman.")
CIT_TAIZ = ("Taiz, L. & Zeiger, E. (2018). 'Plant Physiology and "
            "Development', 6th ed. Sinauer Associates.")
CIT_MAUSETH = ("Mauseth, J. D. (2019). 'Botany: An Introduction to Plant "
               "Biology', 7th ed. Jones & Bartlett.")
CIT_JUDD = ("Judd, W. S. et al. (2016). 'Plant Systematics: A Phylogenetic "
            "Approach', 4th ed. Sinauer Associates.")
CIT_APG = ("APG IV (2016). 'An update of the Angiosperm Phylogeny Group "
           "classification for the orders and families of flowering plants.' "
           "Botanical Journal of the Linnean Society, 181(1), 1-20.")
CIT_AGRIOS = ("Agrios, G. N. (2005). 'Plant Pathology', 5th ed. Elsevier "
              "Academic Press.")
CIT_SIMPSON = ("Simpson, M. G. (2019). 'Plant Systematics', 3rd ed. "
               "Academic Press.")
CIT_KEW = ("'State of the World's Plants' reports, Royal Botanic Gardens, "
           "Kew — global plant diversity estimates.")
CIT_STD = "Standard botany literature (peer-reviewed textbooks and journals)."
SIG_TAIL = ("Signature editions are original Signature interpretations of "
            "botany, written in the Signature system — clearly labeled "
            "Signature-made, never presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-plant", "name": "What Is a Plant: The Green Kingdom",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Plants are multicellular, mostly photosynthetic eukaryotes that form the "
  "kingdom Plantae in the broad sense — the green lineage that includes "
  "green algae, bryophytes, ferns, gymnosperms, and flowering plants. Every "
  "plant shares a defining toolkit: chlorophyll a and b as photosynthetic "
  "pigments, cellulose-reinforced cell walls, starch as the storage "
  "carbohydrate, and a life cycle with an alternation of multicellular "
  "generations. Land plants — the embryophytes — number roughly 374,000 "
  "described species, with about 2,000 new species described each year. "
  "Flowering plants dominate at roughly 295,000 species, about three "
  "quarters of all vascular plants. Plants anchor nearly every terrestrial "
  "food web, produce the oxygen in the atmosphere through photosynthesis, "
  "and store roughly 450 gigatonnes of carbon — about 80 percent of all "
  "biomass on Earth. They are sessile, so every plant solves the problems "
  "of survival — light capture, water, minerals, reproduction, defense — "
  "without moving."),
 "how_it_works": (
  "A plant works as an integrated solar-powered system. Leaves intercept "
  "light and carbon dioxide; roots absorb water and minerals from soil; the "
  "stem holds the structure upright and moves materials between the two. "
  "Photosynthesis in the leaf converts light energy into chemical energy, "
  "fixing carbon dioxide into sugars that fuel growth, storage, and "
  "reproduction. Because plants cannot walk away from drought, shade, "
  "herbivores, or cold, they respond with chemistry and architecture "
  "instead: deep roots for water, thick cuticles against drying, toxins "
  "against grazers, dormancy against winter. Growth happens at meristems — "
  "small regions of perpetually dividing cells at shoot and root tips — so "
  "a plant adds new organs for its entire life, unlike animals that grow to "
  "a fixed body plan."),
 "key_points": [
  "Plants are multicellular photosynthetic eukaryotes with chlorophyll a and b, cellulose walls, and starch storage.",
  "Land plants (embryophytes) number about 374,000 described species; flowering plants are roughly three quarters of vascular plants.",
  "Plants hold about 80 percent of Earth's biomass — roughly 450 gigatonnes of carbon.",
  "Every plant alternates multicellular generations: a spore-producing sporophyte and a gamete-producing gametophyte.",
  "Sessile life is solved with chemistry and architecture: roots for water, cuticles against drying, toxins against grazers, dormancy against cold."],
 "requirements": [
  "No prior botany needed — this is the entry point of the ladder.",
  "Comfort with big numbers (species counts, gigatonnes) helps."],
 "standards": ["ICNafp nomenclature for plant names", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH, CIT_KEW],
 "demo_kind": "plant_diversity",
 "sig_lens": (
  "The Signature reading treats the plant as the original engineered solar "
  "system: a root intake module, a stem scaffold, a leaf solar array, and a "
  "seed payload package. Every Signature botany record keeps that "
  "engineering discipline — intake, structure, energy, payload — while "
  "staying clearly labeled as his original interpretation."),
},
{
 "key": "plant-cell", "name": "The Plant Cell: Wall, Vacuole, and Plastids",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "The plant cell differs from the animal cell in three decisive "
  "structures. The cell wall — a strong composite of cellulose microfibrils "
  "embedded in hemicellulose and pectin, later reinforced with lignin in "
  "woody tissue — gives the cell its shape and resists enormous internal "
  "pressure. The central vacuole, a giant water-filled sac, can occupy 90 "
  "percent of the cell's volume; by pushing the cytoplasm against the wall "
  "it creates turgor pressure, typically 0.5 to 1.5 megapascals, which is "
  "what keeps a non-woody plant upright. Plastids are the third signature: "
  "chloroplasts run photosynthesis with stacked thylakoid membranes full of "
  "chlorophyll, chromoplasts make the colors of ripe fruit and flowers, and "
  "leucoplasts store starch. Plant cells also connect through plasmodesmata "
  "— cytoplasmic channels through the walls — so the whole plant is one "
  "continuous living network called the symplast."),
 "how_it_works": (
  "Water flows into the cell by osmosis because the vacuole holds dissolved "
  "sugars and salts. The incoming water inflates the vacuole, pressing the "
  "cell membrane against the rigid wall; the wall pushes back, and that "
  "balance is turgor — the hydraulic skeleton of herbaceous plants. When "
  "water is scarce, turgor drops and the plant wilts; watering restores it. "
  "Meanwhile chloroplasts capture light: their thylakoid membranes host the "
  "photosystems that split water and build energy carriers, while the "
  "surrounding stroma fixes carbon dioxide into sugar. Primary walls are "
  "thin and stretchy for growing cells; once growth stops, many cells lay "
  "down a thick secondary wall impregnated with lignin, the polymer that "
  "makes wood strong and waterproof."),
 "key_points": [
  "Three structures define the plant cell: the cellulose cell wall, the giant central vacuole, and plastids (chloroplasts and others).",
  "Turgor pressure — water pushing the membrane against the wall, typically 0.5-1.5 MPa — is the hydraulic skeleton of non-woody plants.",
  "Chloroplasts run photosynthesis: thylakoid membranes capture light, the stroma fixes CO2.",
  "Plasmodesmata link all plant cells into one continuous symplast.",
  "Secondary walls reinforced with lignin make wood strong and waterproof."],
 "requirements": [
  "The 'What Is a Plant' record above.",
  "Basic idea of osmosis (high-school biology level)."],
 "standards": ["Standard cell-biology terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_TAIZ],
 "demo_kind": "turgor_pressure",
 "sig_lens": (
  "The Signature reading treats the plant cell as a pressurized module: the "
  "wall is the pressure vessel, the vacuole is the hydraulic tank, and the "
  "chloroplast is the onboard power plant. Signature botany keeps that "
  "systems-engineering view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "roots", "name": "Roots: Anchorage and Absorption",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Roots do two jobs at once: they anchor the plant against wind and "
  "gravity, and they absorb the water and mineral nutrients the shoot "
  "cannot reach. A root grows from its tip, where a protective root cap "
  "shields the apical meristem — the dividing cells that extend the root "
  "through soil. Behind the tip, cells elongate to push the tip forward, "
  "then mature in the zone of maturation, where thousands of root hairs — "
  "thin extensions of single epidermal cells — multiply the absorptive "
  "surface area roughly fivefold. Two architectures dominate: taproot "
  "systems (a deep central root with branches, as in carrots and oaks) and "
  "fibrous systems (a dense mat of similar-sized roots, as in grasses and "
  "wheat). Roots also store reserves — the carrot and sweet potato are "
  "swollen roots — and partner with fungi and bacteria that extend their "
  "reach far beyond what root hairs alone can do."),
 "how_it_works": (
  "Water enters root hairs by osmosis and travels inward through the "
  "cortex to the xylem, the plant's water pipeline to the shoot. Minerals "
  "arrive dissolved in soil water; the root actively pumps the scarce ones "
  "inward, concentrating them far above soil levels. A waxy barrier called "
  "the Casparian strip in the endodermis forces everything entering the "
  "central cylinder to pass through cell membranes — the root's quality "
  "checkpoint that blocks toxins and selects nutrients. Root tips sense "
  "gravity and moisture: statoliths (dense starch grains) settle to the "
  "bottom of sensing cells, steering growth downward (gravitropism), while "
  "auxin redistributes to bend roots toward water. A single rye plant can "
  "grow over 600 kilometers of roots with 14 billion root hairs — an "
  "absorptive surface larger than a tennis court."),
 "key_points": [
  "Roots anchor the plant and absorb water and minerals; they grow from a protected apical meristem at the tip.",
  "Root hairs multiply absorptive surface area about fivefold.",
  "Taproot systems (carrots, oaks) go deep; fibrous systems (grasses, wheat) spread wide.",
  "The Casparian strip forces all incoming water through cell membranes — the root's quality checkpoint.",
  "Storage roots (carrot, sweet potato) stockpile reserves; mycorrhizal fungi and nitrogen-fixing bacteria extend root reach."],
 "requirements": [
  "The 'What Is a Plant' and 'Plant Cell' records above."],
 "standards": ["ICNafp nomenclature for plant names", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_TAIZ],
 "demo_kind": "root_surface",
 "sig_lens": (
  "The Signature reading treats the root as the intake and foundation "
  "module: a self-extending drill that anchors the structure, filters the "
  "supply, and stockpiles reserves. Signature botany keeps that "
  "engineering view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "stems", "name": "Stems: Support and Transport",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "The stem is the plant's scaffold and highway system. It holds leaves up "
  "into the light, carries water and minerals from roots to leaves through "
  "the xylem, and distributes sugars from leaves to the rest of the plant "
  "through the phloem. Stems are built from repeating units: nodes, where "
  "leaves and branches attach, and internodes, the segments between them. "
  "Growth in length comes from the shoot apical meristem at the tip, which "
  "also produces new leaves and suppresses side branches through apical "
  "dominance. Growth in girth — secondary growth — comes from the vascular "
  "cambium, a cylinder of dividing cells that lays down wood (secondary "
  "xylem) inward and bark (secondary phloem) outward, year after year. "
  "Herbaceous stems stay soft and green; woody stems accumulate years of "
  "wood and become trunks and branches that can stand for centuries."),
 "how_it_works": (
  "Inside the stem, vascular tissue is arranged by lineage: eudicots "
  "typically carry their bundles in a ring, monocots scatter them through "
  "the ground tissue. Xylem vessels and tracheids are dead, hollow tubes "
  "with lignified walls — water columns pulled upward by transpiration move "
  "through them with little resistance. Phloem sieve tubes are living cells "
  "that push sugar-rich sap from sources (mature leaves) to sinks (roots, "
  "fruits, growing tips) by pressure flow: loading sugar at the source "
  "draws water in by osmosis, building pressure that drives sap toward the "
  "sink, where sugar is unloaded. Prune the tip and apical dominance breaks "
  "— side buds awaken and the plant branches. Girdle the bark and the "
  "phloem is cut while the xylem still carries water, a classic "
  "demonstration that the two pipelines are separate."),
 "key_points": [
  "Stems hold leaves to the light and carry xylem (water up) and phloem (sugar to sinks).",
  "Nodes bear leaves and branches; internodes set the spacing; the shoot apical meristem extends the tip.",
  "The vascular cambium adds wood inward and bark outward — secondary growth that builds trunks.",
  "Eudicots ring their vascular bundles; monocots scatter them.",
  "Apical dominance: the tip suppresses side branches until it is removed."],
 "requirements": [
  "The 'What Is a Plant' record above.",
  "The 'Roots' record helps (xylem/phloem introduced)."],
 "standards": ["Standard plant-anatomy terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH],
 "demo_kind": "internode_growth",
 "sig_lens": (
  "The Signature reading treats the stem as the load-bearing chassis with "
  "dual plumbing: an upward water main (xylem) and a two-way sugar freight "
  "line (phloem). Signature botany keeps that infrastructure view while "
  "staying clearly labeled as his original interpretation."),
},
{
 "key": "leaves", "name": "Leaves: The Solar Collectors",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "The leaf is the plant's solar collector and gas-exchange surface, "
  "shaped by one brutal trade-off: it must open pores to take in carbon "
  "dioxide, but every open pore leaks water. A typical leaf has a broad "
  "flat blade to catch light, a stalk (petiole) that positions it, and an "
  "internal anatomy built for the job: a transparent upper epidermis, a "
  "palisade mesophyll of tightly packed chloroplast-rich cells where most "
  "photosynthesis happens, a spongy mesophyll full of air spaces that let "
  "CO2 diffuse to every cell, and a lower epidermis studded with stomata — "
  "pores flanked by guard cells that open and close them. Veins of xylem "
  "and phloem deliver water and export sugar. Leaf arrangement (phyllotaxis) "
  "follows mathematical patterns — often Fibonacci spirals — that minimize "
  "self-shading. A forest canopy typically carries 3 to 6 square meters of "
  "leaf per square meter of ground, the leaf area index."),
 "how_it_works": (
  "Guard cells work as hydraulic valves: when they pump potassium ions in, "
  "water follows by osmosis, they swell, and their curved shape bows apart "
  "to open the pore; when potassium leaves, they deflate and the pore "
  "closes. Stomata open in daylight for CO2 and close in drought to save "
  "water — abscisic acid from drying roots is the closing signal. Light "
  "fades exponentially through a canopy (Beer's law): each layer of leaves "
  "absorbs a fraction, so lower leaves live in deep shade and shed when "
  "they cost more than they earn. In autumn, deciduous trees dismantle "
  "chlorophyll, recover the nitrogen and magnesium, seal the leaf stalk "
  "with an abscission layer, and drop the leaf — revealing the carotenoid "
  "yellows and anthocyanin reds underneath."),
 "key_points": [
  "Leaves trade CO2 intake against water loss through stomata — the central compromise of leaf design.",
  "Palisade mesophyll photosynthesizes; spongy mesophyll distributes CO2; veins supply water and export sugar.",
  "Guard cells open and close stomata hydraulically, driven by potassium and water.",
  "Leaf area index (leaf m² per ground m²) is typically 3-6 in forests; light fades exponentially through the canopy.",
  "Autumn color is revealed when chlorophyll is dismantled and recovered before leaf drop."],
 "requirements": [
  "The 'What Is a Plant' and 'Plant Cell' records above."],
 "standards": ["Standard plant-anatomy terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_TAIZ],
 "demo_kind": "leaf_area_index",
 "sig_lens": (
  "The Signature reading treats the leaf as a deployable solar panel with "
  "an active cooling and gas-exchange valve system (stomata) and a "
  "self-optimizing tilt and spacing algorithm (phyllotaxis). Signature "
  "botany keeps that device view while staying clearly labeled as his "
  "original interpretation."),
},
{
 "key": "light-reactions", "name": "Photosynthesis I: The Light Reactions",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The light reactions are the front end of photosynthesis: they capture "
  "photons and convert light energy into the chemical currencies ATP and "
  "NADPH, releasing oxygen as a by-product. They run in the thylakoid "
  "membranes of the chloroplast, where two photosystems work in series. "
  "Photosystem II absorbs light, energizes electrons stripped from water — "
  "the famous photolysis that splits 2H2O into O2, protons, and electrons — "
  "and passes them down an electron transport chain that pumps protons "
  "into the thylakoid interior. Photosystem I re-energizes the electrons "
  "with a second photon and hands them to NADP+, making NADPH. The proton "
  "gradient then drives ATP synthase, the rotary enzyme that manufactures "
  "ATP. A minimum of about 8 to 10 photons is needed per oxygen molecule "
  "evolved. Chlorophyll absorbs red and blue light and reflects green — "
  "the reason plants look green."),
 "how_it_works": (
  "Think of it as a two-stage pump. Stage one (photosystem II): a photon "
  "kicks an electron to a high energy level; the electron's vacancy is "
  "filled by splitting water, which is why oxygen bubbles off. The "
  "energized electron travels through carriers (plastoquinone, cytochrome "
  "b6f, plastocyanin), and at each step protons are pumped across the "
  "membrane — building a gradient like water behind a dam. Stage two "
  "(photosystem I): a second photon boosts the electron again, and it "
  "reduces NADP+ to NADPH, the hydrogen-carrier the Calvin cycle will "
  "spend. The dammed-up protons flow back through ATP synthase, which "
  "spins like a turbine and bolts phosphate onto ADP to make ATP. Net "
  "output per oxygen released: roughly 3 ATP and 2 NADPH — the exact fuel "
  "mix the carbon-fixing reactions demand."),
 "key_points": [
  "Light reactions run in thylakoid membranes; they make ATP and NADPH and release O2 from water.",
  "Photosystem II splits water (photolysis); Photosystem I makes NADPH.",
  "An electron transport chain pumps protons; ATP synthase harvests the gradient to make ATP.",
  "Minimum ~8-10 photons per O2 evolved.",
  "Chlorophyll absorbs red and blue, reflects green — plants are green by subtraction."],
 "requirements": [
  "The 'Plant Cell' and 'Leaves' records above.",
  "Basic energy concepts (high-school chemistry level)."],
 "standards": ["Standard photosynthesis terminology", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_RAVEN],
 "demo_kind": "photon_energy",
 "sig_lens": (
  "The Signature reading treats the thylakoid as a two-stage photonic "
  "power converter: photon in, water split, electron current pumped, ATP "
  "turbine spun. Signature botany keeps that power-engineering view while "
  "staying clearly labeled as his original interpretation."),
},
{
 "key": "calvin-cycle", "name": "Photosynthesis II: The Calvin Cycle",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The Calvin cycle is the back end of photosynthesis: it takes the ATP "
  "and NADPH made by the light reactions and spends them to fix carbon "
  "dioxide into sugar. It runs in the chloroplast stroma and needs no "
  "light directly — though it depends on the light reactions' products. "
  "The cycle has three phases. First, carboxylation: the enzyme RuBisCO — "
  "probably the most abundant protein on Earth — attaches CO2 to the "
  "five-carbon acceptor RuBP, forming an unstable six-carbon compound that "
  "splits into two molecules of 3-phosphoglycerate. Second, reduction: ATP "
  "and NADPH convert 3-phosphoglycerate into glyceraldehyde-3-phosphate "
  "(G3P), the three-carbon sugar that is the cycle's net product. Third, "
  "regeneration: most G3P is spent rebuilding RuBP so the cycle can turn "
  "again. Per glucose equivalent assembled, the cycle consumes 6 CO2, 18 "
  "ATP, and 12 NADPH."),
 "how_it_works": (
  "Follow one turn for three CO2 molecules: RuBisCO fixes 3 CO2 onto 3 "
  "RuBP, yielding 6 molecules of 3-phosphoglycerate. Reduction spends 6 "
  "ATP and 6 NADPH to make 6 G3P. Five of those G3P are recycled — at a "
  "cost of 3 more ATP — to regenerate the 3 RuBP acceptors; the sixth G3P "
  "exits as net product, the raw material for glucose, starch, cellulose, "
  "and every other carbon compound the plant builds. RuBisCO is famously "
  "slow (a few turnovers per second) and sometimes grabs oxygen instead of "
  "CO2 — the wasteful side reaction called photorespiration, which C4 and "
  "CAM plants evolved elaborate workarounds to suppress. The overall "
  "equation: 6CO2 + 6H2O, powered by light, yields C6H12O6 + 6O2."),
 "key_points": [
  "The Calvin cycle fixes CO2 into sugar in the stroma, spending ATP and NADPH from the light reactions.",
  "Three phases: carboxylation (RuBisCO fixes CO2 to RuBP), reduction (to G3P), regeneration (of RuBP).",
  "Cost per glucose: 6 CO2 + 18 ATP + 12 NADPH.",
  "RuBisCO is Earth's most abundant protein — slow, and prone to wasteful photorespiration.",
  "G3P is the net product: the feedstock for glucose, starch, cellulose, and all plant carbon compounds."],
 "requirements": [
  "The 'Light Reactions' record above.",
  "Comfort with simple chemical bookkeeping."],
 "standards": ["Standard biochemistry terminology", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_RAVEN],
 "demo_kind": "calvin_stoichiometry",
 "sig_lens": (
  "The Signature reading treats the Calvin cycle as a carbon-assembly "
  "loop: a catalytic fixer (RuBisCO) bonds atmospheric CO2 onto a recycled "
  "carrier, paid for in ATP and NADPH minted by the light reactions. "
  "Signature botany keeps that process-engineering view while staying "
  "clearly labeled as his original interpretation."),
},
{
 "key": "transpiration", "name": "Water Transport: Transpiration and the Xylem",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "A large tree can lift hundreds of liters of water a day from roots to "
  "leaves with no pump at all. The engine is transpiration: water "
  "evaporating from leaf cell walls into air spaces and out through "
  "stomata pulls on the continuous water columns in the xylem, and the "
  "extraordinary cohesion of water molecules transmits that pull all the "
  "way down to the roots. This is the cohesion-tension theory. Water's "
  "hydrogen bonds give it immense tensile strength — a 100-meter column "
  "hangs under nearly a megapascal of tension without snapping. Adhesion "
  "to xylem walls narrows the risk of the column breaking. When tension "
  "gets too extreme, air bubbles (embolisms) can snap the column; plants "
  "fight back with narrow vessels, redundant pathways, and in some "
  "species, overnight root pressure that refills them."),
 "how_it_works": (
  "The chain starts in the leaf: evaporation from moist cell walls lowers "
  "water potential at the top, and water is drawn up the xylem to replace "
  "it. Cohesion between water molecules means the whole column moves as "
  "one rope — pull the top, the bottom follows. The soil-root interface "
  "completes the circuit: roots absorb water where soil water potential "
  "exceeds root water potential, and the transpiration pull propagates the "
  "demand downward. Stomata throttle the whole system: open stomata mean "
  "fast flow and fast photosynthesis but heavy water loss; closed stomata "
  "conserve water but starve the leaf of CO2. At night, when stomata close "
  "and transpiration stops, root pressure can push water upward and force "
  "droplets out of leaf margins — the phenomenon called guttation."),
 "key_points": [
  "Transpiration pull — evaporation from leaves — is the engine that lifts water tens of meters with no pump.",
  "Cohesion-tension theory: water's hydrogen bonds transmit the pull as one unbroken column.",
  "A 100 m water column hangs under ~1 MPa of tension; embolisms (air bubbles) are the failure mode.",
  "Stomata throttle the system, trading CO2 intake against water loss.",
  "Root pressure at night can refill vessels and cause guttation droplets on leaf margins."],
 "requirements": [
  "The 'Roots', 'Stems', and 'Leaves' records above."],
 "standards": ["Standard plant-physiology terminology", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_RAVEN],
 "demo_kind": "transpiration_rate",
 "sig_lens": (
  "The Signature reading treats the xylem as a passive hydraulic lift: "
  "solar evaporation at the top pulls a tensioned water rope up from the "
  "soil, throttled by stomatal valves and protected by redundant narrow "
  "pipelines. Signature botany keeps that hydraulics view while staying "
  "clearly labeled as his original interpretation."),
},
{
 "key": "life-cycles", "name": "Plant Life Cycles: Annuals, Biennials, and Perennials",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Plants schedule their lives three ways. Annuals — wheat, rice, "
  "marigolds — germinate, flower, set seed, and die within a single growing "
  "season, betting everything on one reproductive burst. Biennials — "
  "carrots, cabbage, foxglove — spend the first year building a storage "
  "root or rosette of leaves, overwinter on those reserves, then flower, "
  "seed, and die in year two. Perennials — oaks, grasses, lavender — live "
  "many years, flowering repeatedly; herbaceous perennials die back to "
  "underground organs each winter while woody perennials keep their "
  "aboveground skeleton. The strategy is an energy wager: annuals invest "
  "everything in seeds now, perennials invest in structures that pay off "
  "over decades. Gardeners exploit the schedule — vernalization (a cold "
  "period) is the cue many biennials and winter annuals need before they "
  "will flower."),
 "how_it_works": (
  "Flowering is triggered by internal and environmental signals converging "
  "on the shoot meristem: day length (photoperiodism), accumulated cold "
  "(vernalization), plant age, and hormones like florigen. Short-day "
  "plants (chrysanthemums) flower when nights lengthen past a critical "
  "threshold; long-day plants (spinach) flower as nights shorten; "
  "day-neutral plants (tomatoes) ignore day length. Once the meristem "
  "commits to flowering, it is usually irreversible — the vegetative "
  "program shuts down and floral organs form. Annuals pour resources into "
  "that single flowering because there is no next year; perennials hold "
  "reserves back in roots, rhizomes, bulbs, or wood so they can leaf out "
  "again. Dormancy — buds sealed with scales, seeds with hard coats — lets "
  "perennials and seed banks wait out hostile seasons."),
 "key_points": [
  "Annuals live one season and bet everything on seed; biennials store in year one and flower in year two; perennials live many years.",
  "Herbaceous perennials die back to underground organs; woody perennials keep an aboveground skeleton.",
  "Flowering is triggered by photoperiod, vernalization (cold), age, and florigen.",
  "Short-day, long-day, and day-neutral plants read night length differently.",
  "Dormancy in buds and seeds lets plants wait out hostile seasons."],
 "requirements": [
  "The 'What Is a Plant' record above."],
 "standards": ["Standard horticultural terminology", "SI units throughout"],
 "citations": [CIT_MAUSETH, CIT_TAIZ],
 "demo_kind": "life_cycle_table",
 "sig_lens": (
  "The Signature reading treats life-cycle strategy as scheduling "
  "software: annuals run a single sprint to seed, biennials a two-phase "
  "store-then-spend, perennials a long-horizon loop with winter "
  "hibernation subroutines. Signature botany keeps that systems view "
  "while staying clearly labeled as his original interpretation."),
},
]
# ------------------------------------------------------------------ COMPOUNDED
ENTRIES += [
{
 "key": "alternation", "name": "Alternation of Generations: Two Bodies, One Life Cycle",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Every land plant lives two lives in one: a diploid sporophyte (2n) "
  "that makes spores by meiosis, and a haploid gametophyte (n) that makes "
  "gametes by mitosis. Fertilization fuses two gametes into a diploid "
  "zygote that grows into the sporophyte; meiosis in the sporophyte's "
  "sporangia produces haploid spores that grow into the gametophyte — and "
  "the wheel turns. The great story of plant evolution is the shifting "
  "balance between these two bodies. In mosses the leafy green plant you "
  "see is the gametophyte, with the sporophyte a small stalk dependent on "
  "it. In ferns both are free-living, but the big frondy plant is the "
  "sporophyte. In seed plants the gametophyte has shrunk to microscopic: "
  "a few cells inside pollen (male) and inside the ovule (female), "
  "completely dependent on the towering sporophyte. Animals have no "
  "equivalent — our haploid phase is just the gametes themselves."),
 "how_it_works": (
  "The cycle turns on two cell divisions with opposite jobs. Meiosis "
  "halves the chromosome number: a diploid spore-mother cell in the "
  "sporangium divides into four haploid spores, each genetically unique. "
  "Each spore grows by mitosis into a multicellular gametophyte that "
  "produces gametes — also by mitosis, so the gametes are clones of the "
  "gametophyte. Fertilization restores diploidy: sperm plus egg make a 2n "
  "zygote, which grows by mitosis into the sporophyte. Which generation "
  "dominates determines the plant's whole ecology: dominant gametophytes "
  "(mosses) stay small and need surface water for swimming sperm; dominant "
  "sporophytes (ferns, seed plants) can grow tall, and seed plants "
  "eliminated the swimming sperm entirely with pollen tubes."),
 "key_points": [
  "Sporophyte (2n) makes spores by meiosis; gametophyte (n) makes gametes by mitosis; fertilization restores 2n.",
  "Mosses: dominant gametophyte, dependent sporophyte. Ferns: dominant sporophyte, free-living gametophyte.",
  "Seed plants shrank the gametophyte to a few cells inside pollen and ovules.",
  "The evolutionary trend is toward sporophyte dominance and gametophyte reduction.",
  "Animals have no multicellular haploid phase — this alternation is a plant (and algal) signature."],
 "requirements": [
  "The 'What Is a Plant' record above.",
  "Basic meiosis vs mitosis (high-school biology level)."],
 "standards": ["Standard life-cycle terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH],
 "demo_kind": "alternation_table",
 "sig_lens": (
  "The Signature reading treats alternation as a two-phase build cycle: "
  "a diploid manufacturing body that mass-produces haploid starter kits "
  "(spores), each of which builds a gamete factory that ships the final "
  "assembly (zygote) back to diploid. Signature botany keeps that "
  "production-line view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "bryophytes", "name": "Bryophytes: Mosses, Liverworts, and Hornworts",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Bryophytes are the amphibians of the plant kingdom: the first land "
  "plants' surviving relatives, still tied to water for reproduction. "
  "They comprise three lineages — mosses (about 12,000 species), "
  "liverworts (about 7,500), and hornworts (about 200) — united by a "
  "gametophyte-dominant life cycle: the green carpet you see is the "
  "haploid gametophyte, and the sporophyte is a slender stalk (seta) with "
  "a capsule, usually dependent on the gametophyte for nutrition. "
  "Bryophytes have no true roots, stems, or leaves — they anchor with "
  "rhizoids and absorb water directly across their surfaces — and no "
  "lignified vascular tissue, which keeps them small. Yet they are "
  "ecological heavyweights: Sphagnum (peat moss) covers about 3 percent of "
  "Earth's land surface and stores more carbon than all the world's "
  "vegetation combined in some estimates, and mosses can absorb up to 20 "
  "times their dry weight in water."),
 "how_it_works": (
  "Because they lack vascular plumbing, bryophytes are poikilohydric: "
  "their water content tracks the environment, and they survive drying by "
  "simply shutting down and reviving when rain returns — some mosses "
  "revive after years desiccated. Reproduction still needs a film of "
  "water: the male antheridia release flagellated sperm that swim to the "
  "egg in the archegonium. After fertilization, the dependent sporophyte "
  "grows its seta, and the capsule at the tip ripens spores; a toothed "
  "peristome around the capsule mouth flexes with humidity changes, "
  "flicking spores out gradually in dry air for wind dispersal. Sphagnum "
  "builds peatlands by a chemical trick: it exchanges hydrogen ions for "
  "nutrients, acidifying the bog, and its dead lower parts resist decay, "
  "accumulating as peat — a carbon vault thousands of years deep."),
 "key_points": [
  "Three lineages: mosses (~12,000 spp.), liverworts (~7,500), hornworts (~200); gametophyte-dominant life cycle.",
  "No true roots/stems/leaves or lignified vascular tissue — rhizoids anchor, surfaces absorb.",
  "Poikilohydric: they dry out and revive; some survive years desiccated.",
  "Flagellated sperm still need a water film to reach the egg.",
  "Sphagnum builds peatlands, acidifies bogs, and locks away vast carbon stores."],
 "requirements": [
  "The 'Alternation of Generations' record above."],
 "standards": ["ICNafp nomenclature for plant names", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH],
 "demo_kind": "moss_water",
 "sig_lens": (
  "The Signature reading treats bryophytes as the rugged minimal build: "
  "no plumbing, no skeleton — just a water-responsive mat that shuts down "
  "when dry and reboots when wet, with a spore catapult tuned to humidity. "
  "Signature botany keeps that minimal-systems view while staying clearly "
  "labeled as his original interpretation."),
},
{
 "key": "ferns", "name": "Ferns and Horsetails: The Seedless Vascular Plants",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Ferns were the first plants to stand tall: with true lignified "
  "vascular tissue — xylem and phloem — plus true roots, stems, and "
  "leaves, they grew into the great coal forests of the Carboniferous, "
  "about 300 million years ago. Modern ferns number roughly 10,500 "
  "species, from tiny floating duckweed-sized species to tree ferns 20 "
  "meters tall. Their life cycle flips the bryophyte balance: the big "
  "leafy plant is the diploid sporophyte, while the gametophyte is a tiny "
  "free-living heart-shaped prothallus, usually under a centimeter. Ferns "
  "reproduce by spores, not seeds: sporangia clustered in dots (sori) on "
  "the frond underside catapult spores — a single leptosporangiate "
  "sporangium typically holds 64 spores, and one frond can release "
  "millions. Horsetails (Equisetum), the 15 surviving species of a once "
  "giant lineage, are ferns' closest living relatives: jointed, silica-"
  "armored stems that were tree-sized in the Carboniferous."),
 "how_it_works": (
  "The spore is the fern's dispersal gamble: microscopic, tough-walled, "
  "and wind-borne. Landing in moist soil, it germinates into the "
  "prothallus, a thin photosynthetic gametophyte bearing both archegonia "
  "(egg chambers) and antheridia (sperm chambers). Sperm still swim — "
  "ferns need water for fertilization, the ancient constraint they never "
  "escaped. The fertilized egg grows into the sporophyte, which nurses on "
  "the prothallus briefly, then outgrows it into the familiar fronded "
  "plant. Fronds unroll from fiddleheads (circinate vernation), and new "
  "sporangia form on their undersides to close the loop. The sporangium's "
  "catapult is mechanical: a ring of thick-walled annulus cells dries, "
  "snaps back, and flings the spores — one of the fastest plant movements "
  "known."),
 "key_points": [
  "First tall plants: true vascular tissue, roots, stems, leaves; ruled the Carboniferous coal forests.",
  "~10,500 fern species today; the leafy plant is the diploid sporophyte, the gametophyte a tiny free-living prothallus.",
  "Spores in sori catapult from sporangia (typically 64 spores each); one frond can release millions.",
  "Fertilization still needs water for swimming sperm — the constraint ferns never escaped.",
  "Horsetails (Equisetum, 15 species) are silica-armored survivors of a giant extinct lineage."],
 "requirements": [
  "The 'Alternation of Generations' and 'Bryophytes' records above."],
 "standards": ["ICNafp nomenclature for plant names", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_JUDD],
 "demo_kind": "spore_counts",
 "sig_lens": (
  "The Signature reading treats the fern as the first vertical platform: "
  "vascular plumbing enables height, the sporangium catapult is a "
  "mechanical spore launcher, and the whole system still runs on the "
  "legacy water-dependent fertilization protocol. Signature botany keeps "
  "that platform view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "gymnosperms", "name": "Gymnosperms: The Naked-Seed Plants",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Gymnosperm means 'naked seed': their ovules sit exposed on cone scales "
  "rather than enclosed in an ovary. Four living lineages survive — "
  "conifers (about 615 species: pines, spruces, firs, redwoods), cycads "
  "(about 340 species), the single ginkgo species (Ginkgo biloba), and "
  "the gnetophytes (about 110 species) — totaling roughly 1,100 species. "
  "Their great innovation was the seed: an embryo packaged with a food "
  "supply and a protective coat, able to wait out drought and travel "
  "before germinating. Combined with pollen — the male gametophyte "
  "reduced to a few cells carried by wind — seeds freed gymnosperms from "
  "the water-dependent fertilization that chains ferns and mosses to "
  "moist habitats. Conifers dominate the boreal forest, the largest "
  "terrestrial biome; a bristlecone pine can live over 4,800 years, among "
  "the oldest living organisms."),
 "how_it_works": (
  "Reproduction centers on cones. Male cones shed clouds of pollen — a "
  "single pine can release millions of grains, each with air bladders for "
  "wind travel. Female cones bear ovules on their scales; a pollen grain "
  "landing near an ovule grows a pollen tube that delivers sperm directly "
  "to the egg — no swimming, no surface water needed. Fertilization makes "
  "a diploid embryo, and the ovule matures into the seed: embryo, stored "
  "food (the female gametophyte tissue), and seed coat. Conifer needles "
  "are drought engineering: thick cuticle, sunken stomata, and a small "
  "surface area let boreal forests photosynthesize through freezing, dry "
  "winters. Many pines add fire engineering — serotinous cones sealed "
  "with resin that open only in a fire's heat, sowing seeds onto the "
  "freshly cleared, ash-fertilized ground."),
 "key_points": [
  "Naked seeds on cone scales; four lineages: conifers (~615 spp.), cycads (~340), ginkgo (1), gnetophytes (~110).",
  "The seed — embryo plus food plus protective coat — freed plants from germinating immediately.",
  "Pollen delivers sperm by tube: no swimming, no surface water needed for fertilization.",
  "Conifers dominate the boreal forest, Earth's largest land biome.",
  "Needles are drought engineering; serotinous cones use fire as a sowing signal; bristlecones exceed 4,800 years."],
 "requirements": [
  "The 'Alternation of Generations' and 'Ferns' records above."],
 "standards": ["ICNafp nomenclature for plant names", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_JUDD],
 "demo_kind": "cone_seeds",
 "sig_lens": (
  "The Signature reading treats the gymnosperm as the hardened field "
  "unit: a seed payload with rations and armor, delivered by wind-borne "
  "pollen drones, built to colonize cold and dry ground the flowering "
  "plants leave alone. Signature botany keeps that rugged-systems view "
  "while staying clearly labeled as his original interpretation."),
},
{
 "key": "flower", "name": "The Flower: Structure and Function",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "The flower is a short, determinate shoot whose leaves have been "
  "repurposed for sex. Its organs sit in four concentric whorls: the "
  "calyx of sepals (usually green, protective in bud), the corolla of "
  "petals (often colorful, advertising to pollinators), the androecium "
  "of stamens (each a filament holding an anther that makes pollen), and "
  "the gynoecium of carpels (each with an ovary holding ovules, a style, "
  "and a stigma that catches pollen). A lily shows the classic numbers: "
  "3+3 tepals, 6 stamens, 3 fused carpels. Flowers may be complete (all "
  "four whorls), incomplete, perfect (both sexes), or imperfect (separate "
  "male and female flowers, as in squash and oaks). Their symmetry — "
  "radial like a daisy or bilateral like an orchid — is a billboard tuned "
  "to a specific pollinator's senses, and nectar guides, scents, and "
  "ultraviolet patterns invisible to us steer the visitors precisely."),
 "how_it_works": (
  "Pollination begins when a pollen grain lands on a compatible stigma. "
  "It germinates a pollen tube that grows down the style, guided by "
  "chemical signals, carrying two sperm cells to the ovule. Then comes "
  "the flowering plants' signature trick — double fertilization: one "
  "sperm fuses with the egg to make the diploid zygote (the embryo), "
  "while the second fuses with the central cell's two nuclei to make the "
  "triploid endosperm, a built-in food tissue that will nurse the embryo. "
  "The ovule becomes the seed; the ovary wall becomes the fruit. Floral "
  "development is switched by ABC-model genes: A-class genes specify "
  "sepals, A+B petals, B+C stamens, C carpels — mutate them and petals "
  "turn into stamens, proving the whorls are one toolkit redeployed."),
 "key_points": [
  "Four whorls: sepals (calyx), petals (corolla), stamens (androecium), carpels (gynoecium).",
  "Double fertilization: one sperm makes the embryo (2n), the other makes the endosperm (3n) food tissue.",
  "Ovule becomes seed; ovary wall becomes fruit.",
  "Floral symmetry, scent, color, and UV patterns are pollinator-targeted billboards.",
  "The ABC model: A/B/C gene classes assign each whorl's identity — mutate them, swap the organs."],
 "requirements": [
  "The 'Gymnosperms' record above (contrast naked vs enclosed seeds)."],
 "standards": ["Standard floral-formula terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH],
 "demo_kind": "flower_parts",
 "sig_lens": (
  "The Signature reading treats the flower as a precision docking "
  "station: advertising arrays (petals) summon specific courier drones "
  "(pollinators), the stigma is the landing pad, the pollen tube a "
  "guided delivery line, and double fertilization packages both the "
  "product (embryo) and its rations (endosperm) in one operation. "
  "Signature botany keeps that logistics view while staying clearly "
  "labeled as his original interpretation."),
},
{
 "key": "angiosperms", "name": "Angiosperms: The Flowering Revolution",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Angiosperms — the flowering plants — are the most successful plant "
  "lineage ever: roughly 295,000 species, about 75 percent of all vascular "
  "plants, dominating nearly every terrestrial habitat from rainforest "
  "canopies to deserts to the Arctic tundra. They exploded in diversity "
  "during the Cretaceous, about 140 to 100 million years ago, in "
  "co-evolution with insect pollinators. Three innovations drove the "
  "takeover: the flower, which recruits animals as precision pollinators; "
  "double fertilization with endosperm, which provisions the embryo far "
  "faster than gymnosperm seeds; and vessels — wide, efficient water "
  "pipes — plus a faster life cycle that lets many species flower within "
  "a year of germination. The group splits into the ANA grade (Amborella, "
  "water lilies), magnoliids, monocots (grasses, orchids, palms), and "
  "eudicots (roses, oaks, daisies) — the last two holding the vast "
  "majority of species."),
 "how_it_works": (
  "The angiosperm advantage is speed and precision. Animal pollinators "
  "deliver pollen directly to a mate instead of broadcasting it to the "
  "wind, so a flower can be fertilized by a single bee visit while a pine "
  "must release millions of wasted grains. Endosperm — the triploid food "
  "tissue made in double fertilization — starts feeding the embryo "
  "immediately, so angiosperm seeds germinate and establish faster than "
  "gymnosperm seeds living off slower female-gametophyte reserves. Vessels "
  "move water with far less resistance than gymnosperm tracheids, "
  "supporting higher photosynthetic rates and faster growth. Fruits then "
  "close the loop: the ovary wall ripens into a package that pays animals "
  "to carry seeds away — flesh for mammals and birds, hooks for fur, "
  "wings and parachutes for wind."),
 "key_points": [
  "~295,000 species, ~75% of vascular plants; radiated in the Cretaceous alongside insect pollinators.",
  "Three winning innovations: the flower, double fertilization with endosperm, and vessel-based water transport.",
  "Animal pollination beats wind: targeted delivery vs broadcast waste.",
  "Fruits pay animals to disperse seeds — flesh, hooks, wings, parachutes.",
  "Major clades: ANA grade, magnoliids, monocots, eudicots (APG IV system)."],
 "requirements": [
  "The 'Flower' and 'Gymnosperms' records above."],
 "standards": ["APG IV nomenclature", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_JUDD, CIT_APG],
 "demo_kind": "angiosperm_share",
 "sig_lens": (
  "The Signature reading treats the angiosperm as the disruptive "
  "platform upgrade: outsourced precision logistics (pollinators), "
  "just-in-time embryo provisioning (endosperm), high-throughput plumbing "
  "(vessels), and a fruit-based distribution network. Signature botany "
  "keeps that platform view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "pollination", "name": "Pollination: Partnerships and Strategies",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Pollination is the delivery of pollen to a receptive stigma, and "
  "plants have hired nearly every available courier. About 87 percent of "
  "flowering plant species use animals — bees above all, plus flies, "
  "beetles, moths, butterflies, birds, and bats — while the rest use wind "
  "(grasses, oaks), and a few use water. Each partnership has a syndrome: "
  "bee flowers are blue or yellow with nectar guides and landing "
  "platforms; moth flowers are white, fragrant, and open at night; bird "
  "flowers are red, tubular, and odorless with copious dilute nectar; bat "
  "flowers are large, pale, and musky, opening after dark; wind flowers "
  "are small, green, scentless, and produce enormous pollen loads with "
  "feathery stigmas to catch it. Roughly three quarters of the world's "
  "leading food crops depend on animal pollinators, making pollination a "
  "multi-hundred-billion-dollar ecosystem service."),
 "how_it_works": (
  "The partnership runs on honest advertising and precise mechanics. "
  "Nectar and pollen are the payment; color, scent, shape, and "
  "ultraviolet patterns are the signs. Many flowers enforce fidelity: "
  "bilateral (irregular) flowers admit only the right-sized bee; orchids "
  "glue pollen packets (pollinia) onto exact spots on the visitor's "
  "body; yucca moths and fig wasps are obligate partners — each plant "
  "species has its single pollinator species, and neither reproduces "
  "without the other. Self-pollination is the backup plan: when "
  "pollinators fail, some flowers pollinate themselves, trading genetic "
  "diversity for guaranteed seed. Plants also police cheating — flowers "
  "that receive no legitimate visits may reabsorb nectar, and some "
  "orchids that offer no reward at all lure males with fake female "
  "pheromones."),
 "key_points": [
  "~87% of flowering plants use animal pollinators; wind serves grasses and many trees; water serves a few aquatics.",
  "Pollination syndromes match flower traits to couriers: bee, moth, bird, bat, wind.",
  "Obligate partnerships (yucca-yucca moth, fig-fig wasp) are one-to-one co-evolution.",
  "~75% of leading food crops depend on animal pollinators — a vast ecosystem service.",
  "Self-pollination is the backup: guaranteed seed at the cost of genetic diversity."],
 "requirements": [
  "The 'Flower' and 'Angiosperms' records above."],
 "standards": ["Standard pollination-ecology terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH, CIT_KEW],
 "demo_kind": "pollination_matrix",
 "sig_lens": (
  "The Signature reading treats pollination as a contracted courier "
  "network: the flower posts a job spec (syndrome), pays in nectar, and "
  "gets precision delivery — with exclusivity contracts (fig wasps), "
  "fidelity locks (bilateral flowers), and a self-delivery fallback. "
  "Signature botany keeps that logistics view while staying clearly "
  "labeled as his original interpretation."),
},
{
 "key": "seed-dispersal", "name": "Fruits and Seed Dispersal: Getting Away",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "A seed that falls under its parent competes with its siblings and "
  "inherits its parent's pests — so plants invest heavily in dispersal. "
  "The fruit, the ripened ovary wall (sometimes plus accessory tissue), "
  "is the dispersal device. Wind fruits grow wings (maple samaras "
  "autorotate like helicopters), parachutes (dandelion pappus), or dust-"
  "fine seeds (orchids). Animal fruits offer flesh: berries and drupes "
  "pay birds and mammals to carry seeds away in their guts, while burs "
  "and stick-tights hitchhike on fur. Some plants fire their seeds: "
  "touch-me-not (Impatiens) and violets use explosive dehiscence, "
  "flinging seeds meters. Water disperses coconuts across oceans — the "
  "fibrous husk floats and the seed stays viable for months at sea. Ants "
  "carry seeds with fatty elaiosomes back to their nests, planting them "
  "in nutrient-rich refuse piles (myrmecochory)."),
 "how_it_works": (
  "Each dispersal mode is physics tuned by selection. A maple samara's "
  "asymmetric wing makes it spin, and spinning slows its fall "
  "(autorotation) so wind carries it farther — drop height times glide "
  "ratio sets the dispersal radius. Dandelion pappus creates a separated "
  "vortex ring above the bristles, a parachute far more efficient than "
  "its feathery look suggests. Ballistic fruits store elastic energy in "
  "drying pod walls until the tension snaps the pod open — a catapult "
  "with a range set by launch velocity and angle. Fleshy fruits time "
  "ripening with color and scent signals, and many seeds are chemically "
  "armored to survive gut passage — some even require it, germinating "
  "better after scarification in a digestive tract. The payoff is "
  "measured in escape: from parent competition, from seed predators, "
  "and into new habitat."),
 "key_points": [
  "Seeds must escape the parent's shadow: competition, pests, and pathogens concentrate beneath it.",
  "Wind: wings (maple samaras), parachutes (dandelion pappus), dust seeds (orchids).",
  "Animals: fleshy fruits pay gut-carriers; burs hitchhike on fur; ants plant elaiosome seeds (myrmecochory).",
  "Ballistic fruits (Impatiens, violets) fling seeds with drying-pod catapults; coconuts cross oceans by floating.",
  "Gut passage scarifies some seeds — the carrier is also the germination trigger."],
 "requirements": [
  "The 'Flower' and 'Angiosperms' records above."],
 "standards": ["Standard fruit-classification terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH],
 "demo_kind": "dispersal_range",
 "sig_lens": (
  "The Signature reading treats the fruit as a launch and delivery "
  "vehicle: helicopter wings, parachutes, ballistic catapults, paid "
  "courier contracts (fleshy fruit), and ocean-going flotation hulls "
  "(coconut) — each tuned to escape the parent's zone. Signature botany "
  "keeps that delivery-systems view while staying clearly labeled as his "
  "original interpretation."),
},
{
 "key": "germination", "name": "Seeds and Germination: The Waiting Game",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "A seed is a paused life: an embryo, a food supply (endosperm or "
  "cotyledons), and a protective coat, all dehydrated to about 5-15 "
  "percent water so metabolism nearly stops. In that state seeds can "
  "wait — some for decades, a few (like the 2,000-year-old Judean date "
  "palm seed that germinated in 2005) for millennia. Dormancy is the "
  "lock: physical dormancy (a waterproof coat), physiological dormancy "
  "(chemical inhibitors like abscisic acid), or a required cue — cold "
  "stratification for temperate species, fire or smoke chemicals for "
  "chaparral species, light for tiny seeds that must germinate at the "
  "soil surface. Germination itself starts with imbibition: the seed "
  "drinks water, swells, enzymes activate, the radicle (embryonic root) "
  "breaks the coat first to anchor and drink, then the shoot emerges. "
  "Seed testing labs certify lots by germination percentage — typically "
  "85 percent or better for commercial seed."),
 "how_it_works": (
  "The lock-and-key logic prevents fatal mistakes. A seed shed in autumn "
  "that germinated immediately would face winter as a seedling; "
  "physiological dormancy plus a chilling requirement forces it to wait "
  "for spring. Abscisic acid (ABA) maintains dormancy while gibberellins "
  "break it — the ABA/GA ratio is the seed's internal vote, tipped by "
  "environmental cues. Imbibition is purely physical at first: dry "
  "colloids in the seed pull water in with enormous force, rehydrating "
  "membranes and proteins. Then metabolism restarts: stored starch and "
  "oils are mobilized by enzymes (amylases, lipases), respiration "
  "surges, and the radicle elongates by cell expansion, not division, "
  "at first. Epigeal germinators (beans) lift their cotyledons above "
  "ground; hypogeal ones (peas, oaks) leave them buried as a pantry."),
 "key_points": [
  "A seed is embryo + food + coat, dehydrated to ~5-15% water — a paused life that can wait decades.",
  "Dormancy types: physical (waterproof coat), physiological (ABA inhibitors), cue-required (cold, fire, light).",
  "The ABA/gibberellin ratio is the internal vote; environment tips it.",
  "Germination starts with imbibition (physical water uptake), then enzyme mobilization, radicle first.",
  "Epigeal (beans) vs hypogeal (peas, oaks) emergence; commercial lots test at 85%+ germination."],
 "requirements": [
  "The 'Flower' and 'Plant Life Cycles' records above."],
 "standards": ["ISTA seed-testing terminology", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_MAUSETH],
 "demo_kind": "germination_test",
 "sig_lens": (
  "The Signature reading treats the seed as a hibernation capsule: "
  "dehydrated payload, ration pack, and armored shell, with a multi-"
  "factor launch lock (water AND temperature AND light AND chemistry) "
  "so it never deploys into certain death. Signature botany keeps that "
  "capsule view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "hormones", "name": "Plant Hormones: Auxin to Ethylene",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Plants coordinate a body with no brain and no nerves using hormones — "
  "chemical messengers active at minute concentrations that tell cells "
  "when to divide, elongate, differentiate, or die. The classic five: "
  "auxin (made in shoot tips; drives cell elongation, apical dominance, "
  "and root initiation — and bends stems toward light), gibberellins "
  "(stem elongation, seed germination, breaking dormancy), cytokinins "
  "(cell division, delaying leaf aging), abscisic acid or ABA (drought "
  "response — closes stomata — plus seed dormancy and winter bud "
  "dormancy), and ethylene (a gas; fruit ripening, leaf drop, and the "
  "triple response of seedlings pushing through soil). Newer members "
  "include brassinosteroids, jasmonates (wound and defense signaling), "
  "and salicylic acid (pathogen defense). The same hormone does opposite "
  "jobs in different tissues — auxin elongates shoots but inhibits roots "
  "at the same concentration — because the response depends on the "
  "tissue's sensitivity, not just the signal."),
 "how_it_works": (
  "Hormones work by changing gene expression or cell biophysics. Auxin "
  "loosens cell walls: it activates proton pumps that acidify the wall "
  "(the acid-growth hypothesis), letting the cell's turgor stretch it "
  "longer — and it accumulates on the shaded side of a stem, so that side "
  "elongates faster and the stem bends toward light. ABA closes stomata "
  "by a faster route: it opens ion channels in guard cells, potassium "
  "and water rush out, the cells deflate, and the pore shuts within "
  "minutes of drought stress. Ethylene, being a gas, diffuses between "
  "cells and even between fruits — one ripe banana's ethylene ripens the "
  "whole bunch, which is why shippers scrub it from containers and "
  "ripening rooms dose it deliberately. Synthetic auxins (2,4-D) are "
  "weedkillers: at herbicide doses they overdrive growth until the plant "
  "literally grows itself to death."),
 "key_points": [
  "Five classic hormones: auxin, gibberellins, cytokinins, abscisic acid (ABA), ethylene — plus jasmonates, salicylic acid, brassinosteroids.",
  "Auxin from shoot tips drives elongation, apical dominance, and phototropic bending via asymmetric distribution.",
  "ABA closes stomata within minutes of drought and maintains seed/bud dormancy.",
  "Ethylene is a gas: one fruit's ripening signal spreads to its neighbors.",
  "Same hormone, opposite effects in different tissues — response depends on sensitivity; synthetic auxins (2,4-D) are herbicides."],
 "requirements": [
  "The 'Stems', 'Leaves', and 'Seeds and Germination' records above."],
 "standards": ["Standard plant-hormone nomenclature", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_RAVEN],
 "demo_kind": "auxin_dose_response",
 "sig_lens": (
  "The Signature reading treats hormones as the plant's broadcast "
  "control protocol: low-bandwidth chemical messages, tissue-specific "
  "receivers, and gas-phase networking (ethylene) — a distributed "
  "control system with no central processor. Signature botany keeps "
  "that controls view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "tropisms", "name": "Tropisms and Nastic Movements: Plants in Motion",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Plants move — slowly, but deliberately. Tropisms are directional "
  "growth responses: phototropism (toward light), gravitropism (roots "
  "down, shoots up), thigmotropism (touch — tendrils coiling around "
  "supports), hydrotropism (toward water), and chemotropism (toward "
  "chemicals, as pollen tubes grow toward ovules). Nastic movements are "
  "non-directional and reversible: the Venus flytrap snaps shut, mimosa "
  "leaves fold when touched, prayer plants raise and lower leaves daily, "
  "and many flowers open and close on a circadian rhythm. Darwin and his "
  "son Francis proved in 1880 that the bending signal in phototropism "
  "travels from the tip — decapitate a seedling and it cannot bend "
  "toward light. The signal, isolated decades later, was auxin."),
 "how_it_works": (
  "Phototropism runs on blue-light receptors called phototropins in the "
  "shoot tip. Light on one side activates them, and auxin transporters "
  "redirect auxin flow to the shaded side; there auxin loosens walls "
  "and cells elongate faster, curving the shoot toward the light — "
  "differential growth as a steering mechanism. Gravitropism uses "
  "statoliths: dense starch-filled amyloplasts that settle to the "
  "bottom of sensing cells, telling the root which way is down; auxin "
  "then accumulates on the lower side, where — roots being auxin-"
  "sensitive — it inhibits growth, so the upper side outgrows it and "
  "the root bends down. The Venus flytrap is the speed champion among "
  "nastic movements: trigger hairs fired twice within ~20 seconds flip "
  "the trap's lobes from convex to concave (a snap-buckling instability) "
  "in about a tenth of a second — then, only if the prey struggles, "
  "does the trap seal and digest."),
 "key_points": [
  "Tropisms are directional growth: photo- (light), gravi- (gravity), thigmo- (touch), hydro- (water), chemo- (chemicals).",
  "Nastic movements are non-directional and reversible: flytrap snap, mimosa folding, sleep movements.",
  "Phototropism: blue-light phototropins redirect auxin to the shaded side, which elongates faster.",
  "Gravitropism: settling statoliths orient the response; auxin inhibits the root's lower side so it bends down.",
  "Venus flytrap snap is snap-buckling physics in ~0.1 s, armed only after two trigger-hair touches."],
 "requirements": [
  "The 'Plant Hormones' record above (auxin mechanism)."],
 "standards": ["Standard plant-physiology terminology", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_RAVEN],
 "demo_kind": "phototropism_angle",
 "sig_lens": (
  "The Signature reading treats tropisms as guidance software: sensor "
  "arrays (phototropins, statoliths) feed a chemical actuator (auxin "
  "gradients) that steers growth, with the flytrap as a hair-trigger "
  "snap mechanism with a two-factor authentication. Signature botany "
  "keeps that guidance view while staying clearly labeled as his "
  "original interpretation."),
},
{
 "key": "c3-c4-cam", "name": "C3, C4, and CAM: Photosynthetic Strategies",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Most plants fix carbon the straightforward way — C3 photosynthesis, "
  "named for the three-carbon compound RuBisCO makes first — but in hot, "
  "dry, or bright conditions RuBisCO's flaw (it grabs oxygen too, wasting "
  "energy in photorespiration) becomes expensive. Two upgrades evolved. "
  "C4 plants (maize, sugarcane, sorghum) run a carbon-concentrating pump: "
  "in outer mesophyll cells, PEP carboxylase — which ignores oxygen — "
  "fixes CO2 into a four-carbon acid, shuttles it into inner bundle-"
  "sheath cells (the Kranz anatomy), and releases the CO2 there at high "
  "concentration right onto RuBisCO, nearly eliminating photorespiration. "
  "CAM plants (cacti, agaves, pineapples, many orchids) split the work in "
  "time instead of space: they open stomata at night, fix CO2 into malic "
  "acid stored in the vacuole, then close stomata by day and feed the "
  "stored CO2 to the Calvin cycle behind sealed pores — extreme water "
  "savings at the cost of slow growth."),
 "how_it_works": (
  "The economics decide. C4's pump costs extra ATP (about 2 more per CO2 "
  "than C3), so in cool, moist conditions C3 wins on efficiency — but "
  "above roughly 25-30°C, photorespiration's waste exceeds the pump's "
  "cost and C4 wins, which is why tropical grasses dominate hot "
  "savannas. Water-use efficiency tells the same story: C3 plants fix "
  "roughly 1-3 grams of biomass per kilogram of water transpired, C4 "
  "about 2-4, CAM up to 4-10 — CAM plants are the misers of the plant "
  "kingdom, growing slowly on almost no water. Some plants are "
  "flexible: certain succulents run C3 when water is plentiful and "
  "switch to CAM in drought (facultative CAM). Engineers are now trying "
  "to install the C4 pump into rice — a C4 rice could yield far more "
  "grain per drop of water."),
 "key_points": [
  "C3 is the default; photorespiration wastes energy when RuBisCO grabs O2 instead of CO2 in heat.",
  "C4 (maize, sugarcane): PEP carboxylase pre-fixes CO2, Kranz anatomy concentrates it on RuBisCO — space separation.",
  "CAM (cacti, agaves): night CO2 uptake stored as malic acid, day fixation behind closed stomata — time separation.",
  "Water-use efficiency: C3 ~1-3, C4 ~2-4, CAM ~4-10 g biomass per kg water.",
  "C4 pays extra ATP per CO2; it wins above ~25-30°C where photorespiration costs more than the pump."],
 "requirements": [
  "The 'Calvin Cycle' record above (RuBisCO, photorespiration)."],
 "standards": ["Standard photosynthesis terminology", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_RAVEN],
 "demo_kind": "water_use_efficiency",
 "sig_lens": (
  "The Signature reading treats C4 and CAM as two engineering patches "
  "for the same leaky valve: C4 adds a pre-compressor stage with "
  "dedicated plumbing (Kranz), CAM adds a night-shift intake with "
  "chemical battery storage (malic acid) — both trading energy for "
  "water. Signature botany keeps that retrofit view while staying "
  "clearly labeled as his original interpretation."),
},
{
 "key": "mendel", "name": "Mendel and Plant Genetics: The Pea Experiments",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Modern genetics began in a monastery garden. Between 1856 and 1863, "
  "Gregor Mendel crossed some 28,000 pea plants, tracking seven traits — "
  "seed shape, flower color, stem length, and others — and counting the "
  "offspring with mathematical care. From the ratios he derived the two "
  "founding laws. The law of segregation: each plant carries two copies "
  "(alleles) of each hereditary factor, and they separate so each gamete "
  "gets one — hence the 3:1 ratio when two hybrids cross (three showing "
  "the dominant trait to one showing the recessive). The law of "
  "independent assortment: different traits sort independently — hence "
  "the 9:3:3:1 dihybrid ratio. Mendel published in 1866 and was ignored "
  "until 1900, when three botanists independently rediscovered his work. "
  "Peas were the perfect instrument: self-fertilizing for pure lines, "
  "easily cross-pollinated by hand, fast-growing, with sharply distinct "
  "traits."),
 "how_it_works": (
  "The ratios fall out of probability. Cross two heterozygotes (Aa x Aa): "
  "each parent's gametes are 1/2 A and 1/2 a, so offspring are 1/4 AA, "
  "1/2 Aa, 1/4 aa — and since A dominates, 3/4 show the dominant trait "
  "and 1/4 the recessive: 3:1. For two traits (AaBb x AaBb), multiply the "
  "independent 3:1 ratios: 9/16 both dominant, 3/16 first dominant only, "
  "3/16 second dominant only, 1/16 both recessive — 9:3:3:1. Geneticists "
  "test real crosses against these expectations with the chi-square "
  "statistic: sum of (observed minus expected)² over expected across "
  "classes. If chi-square exceeds the critical value (7.815 for 3 "
  "degrees of freedom at 95% confidence), the deviation is too big to "
  "blame on chance and the simple model is rejected — linkage or "
  "selection is suspected."),
 "key_points": [
  "Mendel's pea crosses (1856-1863, ~28,000 plants) founded genetics; ignored until rediscovery in 1900.",
  "Law of segregation: allele pairs separate into gametes — monohybrid cross gives 3:1.",
  "Law of independent assortment: traits sort independently — dihybrid cross gives 9:3:3:1.",
  "Chi-square tests observed ratios against Mendelian expectations; 7.815 is the 95% cutoff at 3 degrees of freedom.",
  "Peas worked because they self-fertilize (pure lines), cross easily, and show sharply distinct traits."],
 "requirements": [
  "The 'Flower' record above (pollination mechanics).",
  "Basic probability (high-school level)."],
 "standards": ["Standard genetics terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH],
 "demo_kind": "mendel_chi_square",
 "sig_lens": (
  "The Signature reading treats Mendel's garden as the first controlled "
  "heredity experiment: pure-line inputs, hand-executed crosses, counted "
  "outputs — and probability as the decoding key that revealed the "
  "discrete units of inheritance. Signature botany keeps that "
  "experimental view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "mycorrhizae", "name": "Mycorrhizae and Nitrogen Fixation: Root Alliances",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Most plants do not forage alone. About 80 percent of land plant "
  "species partner with mycorrhizal fungi: the fungus threads its "
  "hyphae through the soil far beyond the root's reach, mining "
  "phosphorus, zinc, and water, and trades them to the plant for sugars "
  "— typically 4 to 20 percent of the plant's photosynthate. Two main "
  "forms: arbuscular mycorrhizae (the ancient type, penetrating root "
  "cells with tree-shaped arbuscules) associate with most crops and "
  "herbs, while ectomycorrhizae sheath the root tips of pines, oaks, "
  "and birches in a fungal mantle. Separately, legumes (beans, peas, "
  "clover, soybeans) house Rhizobium bacteria in root nodules that fix "
  "atmospheric nitrogen — breaking the ultra-stable N2 triple bond with "
  "the nitrogenase enzyme — into ammonia the plant can use, fixing "
  "roughly 100-200 kg of nitrogen per hectare per year in good stands. "
  "The plant feeds the bacteria sugar; the bacteria pay in nitrogen."),
 "how_it_works": (
  "The trade is negotiated chemically. A phosphorus-hungry root exudes "
  "strigolactones that wake dormant fungal spores and guide hyphae to "
  "the root; the fungus answers with Myc factors, and the root builds "
  "the interface. Inside, the arbuscule's finely branched membrane "
  "maximizes exchange surface: phosphate flows to the plant down its "
  "concentration gradient, sugars flow to the fungus. Ectomycorrhizal "
  "mantles go further, exuding enzymes that digest organic matter "
  "directly — a second stomach for the tree. In legume nodules, the "
  "plant builds a low-oxygen chamber (nitrogenase is destroyed by "
  "oxygen) and supplies leghemoglobin — the pink pigment that carries "
  "oxygen like blood hemoglobin — to keep respiration running while "
  "nitrogenase works. Farmers rotate legumes precisely to bank this "
  "free nitrogen for the next crop."),
 "key_points": [
  "~80% of land plants partner with mycorrhizal fungi, trading 4-20% of their sugar for phosphorus, zinc, and water.",
  "Arbuscular mycorrhizae penetrate cells (most crops); ectomycorrhizae sheath root tips (pines, oaks, birches).",
  "Legume-Rhizobium nodules fix ~100-200 kg N/ha/year via nitrogenase breaking the N2 triple bond.",
  "Nodules are low-oxygen chambers; leghemoglobin (pink) manages oxygen like blood hemoglobin.",
  "Strigolactone signals negotiate the fungal partnership; crop rotation banks fixed nitrogen."],
 "requirements": [
  "The 'Roots' record above."],
 "standards": ["Standard symbiosis terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_TAIZ],
 "demo_kind": "nutrient_exchange",
 "sig_lens": (
  "The Signature reading treats these alliances as outsourced "
  "subsystems: a fungal mining contractor (hyphae beyond root reach) "
  "paid in sugar, and a bacterial nitrogen refinery (nodules) run as a "
  "joint venture — the plant keeps the core business of photosynthesis. "
  "Signature botany keeps that outsourcing view while staying clearly "
  "labeled as his original interpretation."),
},
{
 "key": "plant-ecology", "name": "Plant Ecology: Communities and Succession",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Plant ecology studies plants where they live: how species assemble "
  "into communities, compete, and replace one another over time. The "
  "master process is succession. Primary succession starts on bare "
  "ground — a lava flow, a retreating glacier: lichens and mosses "
  "pioneer, their acids and accumulating debris build soil, grasses and "
  "herbs follow, then shrubs, then forest. Secondary succession replays "
  "it faster after disturbance clears existing vegetation, starting "
  "from surviving seeds and roots. Each stage changes the conditions: "
  "pioneers need full sun and tolerate poor soil; late-successional "
  "species tolerate shade but need the soil the pioneers built. The "
  "endpoint, the climax community, holds until disturbance resets the "
  "clock — which is why ecologists now see many landscapes as patch "
  "mosaics of different successional ages rather than one stable "
  "climax. Competition for light drives forest architecture: the "
  "canopy, understory, and forest floor are light niches, and gap "
  "dynamics — a fallen tree opening a light well — regenerate the "
  "forest tree by tree."),
 "how_it_works": (
  "Succession runs on facilitation and competition. Pioneers facilitate: "
  "their roots break rock, their litter builds organic matter, nitrogen-"
  "fixers enrich the soil — each generation terraforms for the next. "
  "Then competition takes over: taller species shade shorter ones, and "
  "shade tolerance decides who survives under a closing canopy. Species "
  "richness typically rises through succession, peaks, and may dip "
  "slightly at climax as a few dominants exclude the rest. Disturbance "
  "regimes set the tempo: fire-return intervals in savannas, flood "
  "pulses in bottomlands, windthrow in temperate forests. Modern "
  "management mimics this — prescribed burns maintain fire-adapted "
  "communities, and foresters use shelterwood cuts to regenerate "
  "shade-tolerant species in staged light. Invasive species short-"
  "circuit succession by arriving without their natural enemies and "
  "outcompeting natives at every stage."),
 "key_points": [
  "Primary succession builds soil from bare ground (lava, glacial till); secondary succession regrows after disturbance from seeds and roots.",
  "Pioneers facilitate (build soil, fix nitrogen); later species compete, especially for light.",
  "Climax communities persist until disturbance resets the clock; landscapes are mosaics of successional ages.",
  "Forest layers (canopy, understory, floor) are light niches; fallen-tree gaps regenerate forests tree by tree.",
  "Disturbance regimes (fire, flood, windthrow) set the tempo; invasives short-circuit succession."],
 "requirements": [
  "The 'What Is a Plant' and 'Plant Life Cycles' records above."],
 "standards": ["Standard ecology terminology", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH],
 "demo_kind": "succession_richness",
 "sig_lens": (
  "The Signature reading treats succession as a self-assembling "
  "construction sequence: pioneer crews terraform bare ground, each "
  "trade builds on the last, and disturbance is the scheduled "
  "demolition that restarts the build — managed today with prescribed "
  "burns and staged cuts. Signature botany keeps that construction "
  "view while staying clearly labeled as his original interpretation."),
},
{
 "key": "taxonomy-apg", "name": "Plant Taxonomy: The APG IV System",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Plant taxonomy names and orders the green world, and its modern "
  "foundation is DNA. The Angiosperm Phylogeny Group's APG IV system "
  "(2016) classifies flowering plants into orders and families by "
  "evolutionary relationships reconstructed from multiple genes — "
  "replacing older systems built on flower appearance, which often "
  "grouped unrelated look-alikes. The APG IV tree: the ANA grade "
  "branches first (Amborella, a single New Caledonian shrub; then water "
  "lilies; then Austrobaileyales), followed by the magnoliids "
  "(magnolias, laurels, black pepper), then the great split into "
  "monocots (grasses, orchids, palms, lilies) and eudicots — the "
  "eudicots dividing further into rosids (roses, oaks, beans) and "
  "asterids (daisies, mints, potatoes). Every scientific name follows "
  "the International Code of Nomenclature for algae, fungi, and plants: "
  "a Latin binomial (Quercus alba, white oak) with priority to the "
  "oldest validly published name."),
 "how_it_works": (
  "Molecular systematics builds trees from shared derived mutations: "
  "align the same gene across species, count the differences, and group "
  "by most recent common ancestry — clades, each containing an ancestor "
  "and all its descendants. APG IV recognizes 64 orders and 416 "
  "families; DNA reshuffled many: the old Scrophulariaceae (figworts) "
  "splintered, with snapdragons moved to Plantaginaceae alongside "
  "plantains. Identification still runs on morphology in the field: "
  "dichotomous keys ask yes-or-no questions (woody or herbaceous? "
  "leaves opposite or alternate? petals 4 or 5?) to walk down to "
  "species. Herbaria — pressed, labeled, archived specimens, some "
  "centuries old — are the physical vouchers behind every name, and "
  "DNA barcoding (short standard gene regions like rbcL and matK) now "
  "identifies fragments, powders, and seedlings that keys cannot."),
 "key_points": [
  "APG IV (2016) classifies flowering plants by DNA phylogeny: 64 orders, 416 families.",
  "Tree order: ANA grade (Amborella, water lilies) -> magnoliids -> monocots + eudicots (rosids, asterids).",
  "DNA replaced appearance-based systems; look-alikes were often unrelated (figwort family splintered).",
  "Names follow the ICNafp: Latin binomials with priority to the oldest valid publication.",
  "Field ID uses dichotomous keys; herbaria voucher every name; DNA barcodes (rbcL, matK) identify fragments."],
 "requirements": [
  "The 'Angiosperms' record above."],
 "standards": ["APG IV nomenclature", "ICNafp rules"],
 "citations": [CIT_APG, CIT_JUDD, CIT_SIMPSON],
 "demo_kind": "apg_clade_lookup",
 "sig_lens": (
  "The Signature reading treats APG IV as a refactor of the plant "
  "codebase: DNA diffing replaced the old appearance-based filing, "
  "clades are the true module boundaries, and barcodes are the "
  "checksums that identify any fragment. Signature botany keeps that "
  "systems view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "carnivorous", "name": "Carnivorous Plants: Traps and Lures",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "About 800 plant species in 5 orders supplement photosynthesis by "
  "eating animals — an adaptation to sunny, waterlogged, nitrogen-poor "
  "bogs where prey is fertilizer. Five trap architectures evolved "
  "independently. Pitfall traps (pitcher plants: Sarracenia, Nepenthes) "
  "are rolled leaves holding digestive fluid; slippery rims and downward "
  "hairs make escape nearly impossible — giant tropical pitchers can "
  "hold over a liter and occasionally trap frogs and rats. Snap traps "
  "(Venus flytrap, waterwheel plant) shut in a tenth of a second. "
  "Flypaper traps (sundews, butterworts) glue prey with sticky tentacles "
  "that slowly curl around it. Suction traps (bladderworts, all aquatic "
  "or mud-dwelling) are the fastest: a trigger hair trips a trapdoor "
  "and the bladder sucks prey in within a millisecond, resetting by "
  "pumping water out. Lobster-pot traps (corkscrew plants, Genlisea) "
  "guide prey along inward hairs into a digestive chamber. Digestion "
  "uses the same enzymes animals use — proteases, phosphatases — and "
  "the plant absorbs the released nitrogen and phosphorus."),
 "how_it_works": (
  "The economics must balance: a trap costs carbon to build and "
  "photosynthetic area to operate, so it pays only where soil nitrogen "
  "is scarce and light is abundant. The Venus flytrap runs the "
  "tightest budget — each trap fires only a few times before it dies, "
  "so it authenticates: two trigger-hair touches within ~20 seconds "
  "arm the snap, and only continued struggling seals the trap and "
  "starts digestion, a process taking 1-2 weeks. Bladderworts run a "
  "hydraulic trick: they actively pump water out of the bladder, "
  "storing elastic energy in the walls; a prey touch opens the "
  "trapdoor and the pressure differential slams water — and prey — "
  "inward in under a millisecond, among the fastest plant movements "
  "known. Pitcher plants outsource: many host mosquito larvae and "
  "bacteria that shred prey, and the plant absorbs the stew."),
 "key_points": [
  "~800 carnivorous species in 5 orders; five trap types: pitfall, snap, flypaper, suction, lobster-pot.",
  "Adaptation to nitrogen-poor, sunny bogs — prey is fertilizer, not energy.",
  "Venus flytrap: two-touch authentication, ~0.1 s snap-buckling, digestion only if prey struggles.",
  "Bladderwort suction traps fire in under a millisecond via stored hydraulic energy.",
  "Digestion uses animal-like enzymes (proteases, phosphatases); pitchers host helper larvae and bacteria."],
 "requirements": [
  "The 'Tropisms' and 'Leaves' records above."],
 "standards": ["ICNafp nomenclature for plant names", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH],
 "demo_kind": "trap_economics",
 "sig_lens": (
  "The Signature reading treats carnivory as a supplemental procurement "
  "program: five independently evolved trap mechanisms, each with "
  "authentication (flytrap's two-touch rule), speed engineering "
  "(bladderwort hydraulics), and outsourcing (pitcher inquilines) — "
  "profitable only where the soil market fails. Signature botany keeps "
  "that procurement view while staying clearly labeled as his original "
  "interpretation."),
},
# ------------------------------------------------------------------ ADVANCED
{
 "key": "pathology", "name": "Plant Pathology: Disease and Defense",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Plant diseases have starved nations: the potato late blight "
  "(Phytophthora infestans) caused the Irish famine of the 1840s, "
  "killing a million people and displacing millions more; wheat stem "
  "rust (Puccinia graminis) has repeatedly threatened harvests; "
  "American chestnut blight erased 4 billion trees in decades. Plant "
  "pathology studies the agents — fungi (the majority), oomycetes, "
  "bacteria, viruses, phytoplasmas, nematodes, and parasitic plants — "
  "and the conditions that let them win, summarized in the disease "
  "triangle: a susceptible host, a virulent pathogen, and a favorable "
  "environment must coincide. Remove any corner and there is no "
  "disease. Plants fight back without antibodies: physical barriers "
  "(thick cuticles, lignified walls), chemical weapons (phytoalexins "
  "synthesized on attack), and a two-layer immune system — surface "
  "receptors that detect common microbial patterns, and intracellular "
  "R proteins that detect specific pathogen effectors and trigger the "
  "hypersensitive response, sacrificing infected cells to save the "
  "plant. A warning signal (salicylic acid) then immunizes the whole "
  "plant — systemic acquired resistance."),
 "how_it_works": (
  "Epidemics follow the same mathematics as human outbreaks: the "
  "logistic curve, where new infections are proportional to both "
  "infected and still-healthy tissue. Early blight spots seem trivial "
  "until the exponential phase — a lesson in why scouting and early "
  "fungicide timing matter more than late heroics. Control integrates "
  "all three triangle corners: resistant varieties (host), crop "
  "rotation and sanitation (pathogen), and irrigation timing or "
  "canopy management (environment). The gene-for-gene model explains "
  "resistance breeding: each plant R gene recognizes one pathogen "
  "avirulence gene, so breeders stack multiple R genes to slow the "
  "pathogen's evolution around them — an arms race formalized in the "
  "1970s and still the basis of wheat rust and potato blight "
  "programs. Quarantines and clean-seed certification stop "
  "long-distance jumps; the global seed trade is the modern "
  "pathogen highway."),
 "key_points": [
  "Historic toll: potato late blight (Irish famine), wheat stem rust, chestnut blight (4 billion trees).",
  "Disease triangle: susceptible host + virulent pathogen + favorable environment — remove one corner, no disease.",
  "Plant immunity: pattern receptors, R-protein effector detection, hypersensitive cell sacrifice, systemic acquired resistance.",
  "Epidemics follow logistic growth — early detection and timing beat late intervention.",
  "Gene-for-gene resistance breeding stacks R genes; quarantine and clean seed block long-distance spread."],
 "requirements": [
  "The 'What Is a Plant' and 'Plant Ecology' records above.",
  "Comfort with exponential/logistic growth ideas."],
 "standards": ["Standard plant-pathology terminology", "SI units throughout"],
 "citations": [CIT_AGRIOS, CIT_TAIZ],
 "demo_kind": "disease_triangle_epi",
 "sig_lens": (
  "The Signature reading treats plant defense as a layered security "
  "architecture: perimeter hardening (cuticle, lignin), intrusion "
  "detection (pattern receptors), targeted countermeasures "
  "(R-protein effector matching with scorched-earth containment), and "
  "network-wide alerting (systemic acquired resistance). Signature "
  "botany keeps that security view while staying clearly labeled as "
  "his original interpretation."),
},
{
 "key": "economic-botany", "name": "Economic Botany: Crops that Feed the World",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Human civilization runs on about a dozen plants. Just three grasses "
  "— wheat, rice, and maize — supply roughly half of all human calories, "
  "with wheat feeding more people than any other single crop. Add "
  "potatoes, soybeans, cassava, sweet potatoes, sorghum, millets, and "
  "bananas, and a handful of species carry the species. Beyond food: "
  "cotton clothes the world, timber builds it, rubber (from Hevea "
  "brasiliensis) moves it, and sugar, coffee, tea, and cacao flavor it. "
  "The economics are stark: global wheat yields average around 3.5 "
  "tonnes per hectare, and at roughly 3,400 kilocalories per kilogram, "
  "one hectare feeds about a dozen people for a year at 2,500 kcal per "
  "day. The Green Revolution (1960s-70s) doubled and tripled yields with "
  "semi-dwarf varieties, fertilizer, and irrigation — Norman Borlaug's "
  "wheat is credited with saving a billion lives — but the next "
  "doubling must come with less water, less fertilizer, and a hotter "
  "climate."),
 "how_it_works": (
  "Yield is applied plant physiology: yield equals light intercepted "
  "times conversion efficiency times harvest index (the fraction of "
  "biomass that is grain). The Green Revolution mostly raised harvest "
  "index — semi-dwarf wheat puts energy into grain instead of straw — "
  "and fertilizer lifted the ceiling on conversion. Modern breeding "
  "pushes all three terms: canopy architecture for light capture, C4-"
  "like efficiency gains, and grain fill. The calorie math is "
  "unforgiving: feeding 8 billion people needs on the order of 7-8 "
  "quadrillion kilocalories a year from crops, and every percentage "
  "point of yield lost to drought, heat, or disease is hundreds of "
  "millions of human rations. Seed systems carry the genetics — "
  "certified seed, gene banks (Svalbard holds over a million seed "
  "samples as backup), and increasingly, precision breeding. Economic "
  "botany also prices the non-foods: natural rubber, fibers, oils, "
  "and the emerging bioeconomy of plant-based materials."),
 "key_points": [
  "Wheat, rice, and maize supply ~half of human calories; about a dozen species carry civilization.",
  "Wheat at 3.5 t/ha and ~3,400 kcal/kg: one hectare feeds roughly a dozen people for a year.",
  "Yield = light intercepted × conversion efficiency × harvest index; the Green Revolution raised harvest index.",
  "Borlaug's semi-dwarf wheat credited with saving a billion lives; the next doubling must use less water and fertilizer.",
  "Svalbard's vault backs up 1M+ seed samples; cotton, timber, rubber, and stimulant crops run the non-food economy."],
 "requirements": [
  "The 'Photosynthesis' and 'C3, C4, and CAM' records above."],
 "standards": ["FAO crop statistics conventions", "SI units throughout"],
 "citations": [CIT_MAUSETH, CIT_KEW, CIT_STD],
 "demo_kind": "crop_calories",
 "sig_lens": (
  "The Signature reading treats the global crop system as critical "
  "infrastructure: a dozen species as the power grid, yield as the "
  "output spec (light × efficiency × harvest index), gene banks as "
  "the backup servers, and breeding as the upgrade program. Signature "
  "botany keeps that infrastructure view while staying clearly labeled "
  "as his original interpretation."),
},
{
 "key": "secondary-metabolites", "name": "Secondary Metabolites: Medicine from Plants",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Plants are master chemists: beyond the primary metabolism every "
  "living thing needs, they manufacture tens of thousands of secondary "
  "metabolites — compounds made for defense, signaling, and "
  "attraction — that humans harvest as medicines, poisons, flavors, "
  "and materials. Three great classes: alkaloids (nitrogen-containing, "
  "often potent — morphine from poppy, quinine from cinchona bark "
  "against malaria, caffeine, nicotine, vincristine from Madagascar "
  "periwinkle against leukemia), terpenoids (built from isoprene units "
  "— menthol, taxol from Pacific yew against cancer, artemisinin from "
  "sweet wormwood against malaria, rubber), and phenolics (tannins, "
  "flavonoids, lignin — aspirin descends from willow-bark salicin). "
  "Roughly a quarter of modern prescription drugs derive from plant "
  "compounds or their templates. The same chemistry is warfare: "
  "nicotine is an insecticide, tannins make leaves indigestible, and "
  "allelopathic chemicals (black walnut's juglone) poison competitors' "
  "seedlings."),
 "how_it_works": (
  "Secondary metabolism branches off primary pathways: the shikimate "
  "pathway yields phenolics and many alkaloids; the mevalonate and "
  "MEP pathways build terpenoids. Production is inducible — a chewed "
  "leaf ramps up jasmonate signaling and floods tissues with toxins "
  "within hours — and often concentrated where it matters: young "
  "leaves, seeds, and bark carry the heaviest doses. Extraction is "
  "dose arithmetic: dried cinchona bark runs ~5-8 percent quinine, so "
  "a kilogram yields 50-80 grams — thousands of antimalarial doses at "
  "hundreds of milligrams each. Modern pharmacognosy screens plant "
  "extracts against disease targets, then chemists optimize the lead: "
  "artemisinin's sesquiterpene structure was decoded from a 4th-"
  "century Chinese herbal text and earned a Nobel Prize in 2015. "
  "Conservation matters: the Madagascar periwinkle's habitat shrinks "
  "while its alkaloids treat childhood leukemia — biodiversity is the "
  "library."),
 "key_points": [
  "Three classes: alkaloids (morphine, quinine, caffeine), terpenoids (taxol, artemisinin, rubber), phenolics (tannins, salicin→aspirin).",
  "~25% of prescription drugs derive from plant compounds or their templates.",
  "Production is inducible via jasmonate signaling; heaviest doses guard young leaves, seeds, bark.",
  "Extraction is dose arithmetic: % content × biomass ÷ dose = treatments.",
  "Artemisinin (Nobel 2015) came from a 4th-century herbal text — biodiversity is the drug library."],
 "requirements": [
  "The 'Plant Hormones' (jasmonate signaling) record above.",
  "Basic chemistry (molecules, doses) helps."],
 "standards": ["Standard pharmacognosy terminology", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_STD],
 "demo_kind": "extraction_yield",
 "sig_lens": (
  "The Signature reading treats secondary metabolism as the plant's "
  "chemical R&D division: inducible weapons factories (alkaloids), "
  "materials labs (terpenoids), and a compound library humans mine "
  "for medicine — with biodiversity as the archive that must not be "
  "deleted. Signature botany keeps that R&D view while staying clearly "
  "labeled as his original interpretation."),
},
{
 "key": "drought-physiology", "name": "Drought Physiology: How Plants Survive Dry",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Drought is the most limiting stress in agriculture, and plants "
  "survive it three ways: escape (finish the life cycle before the dry "
  "season — desert annuals), avoidance (keep tissues hydrated despite "
  "dry soil — deep roots, water-storing succulence, stomatal closure, "
  "leaf shedding), and tolerance (survive dehydration itself — "
  "resurrection plants like Selaginella lepidophylla revive from 5 "
  "percent water content). The physics is water potential: water "
  "always flows from higher (less negative) to lower (more negative) "
  "potential, and a plant must keep its leaf water potential below the "
  "soil's to keep drinking. As soil dries, its potential falls; the "
  "plant answers with osmotic adjustment — accumulating proline, "
  "sugars, and ions to lower its own potential — and with ABA, the "
  "drought hormone that closes stomata within minutes. Succulents "
  "take avoidance to the extreme: CAM photosynthesis plus massive "
  "parenchyma water tanks let a barrel cactus sit out months of "
  "drought."),
 "how_it_works": (
  "Water potential (Ψ) sums solute potential (Ψs, negative from "
  "dissolved substances) and pressure potential (Ψp, positive from "
  "turgor). A well-watered leaf sits near -0.5 MPa; dry soil can fall "
  "below -1.5 MPa (the permanent wilting point for most crops), and "
  "then no gradient favors the plant — water stops coming. Osmotic "
  "adjustment synthesizes compatible solutes that lower Ψs without "
  "poisoning enzymes, buying a few tenths of a megapascal. Meanwhile "
  "ABA from drying roots signals guard cells to dump potassium, "
  "deflate, and seal the stomata — photosynthesis pauses, but the "
  "plant lives. At the extreme, resurrection plants deploy LEA "
  "proteins and sugars that vitrify the cytoplasm into a biological "
  "glass, freezing molecular structure intact until rain returns. "
  "Breeders select for all of it: deeper roots, waxy cuticles, "
  "osmotic adjustment, and stay-green traits."),
 "key_points": [
  "Three strategies: escape (finish before drought), avoidance (stay hydrated), tolerance (survive dehydration).",
  "Water flows from higher to lower water potential; the plant must stay below soil potential to drink.",
  "Permanent wilting point ~-1.5 MPa for most crops — below it, uptake stops.",
  "Osmotic adjustment (proline, sugars) lowers internal potential; ABA closes stomata in minutes.",
  "Resurrection plants vitrify their cytoplasm into biological glass and revive from ~5% water."],
 "requirements": [
  "The 'Transpiration' and 'Plant Hormones' records above."],
 "standards": ["Standard water-relations terminology", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_RAVEN],
 "demo_kind": "water_potential",
 "sig_lens": (
  "The Signature reading treats drought survival as a three-mode "
  "resilience protocol — sprint (escape), bunker (avoidance), and "
  "hibernate (tolerance with cytoplasmic glass) — governed by a "
  "pressure-differential sensor network (water potential) and an "
  "emergency shutdown signal (ABA). Signature botany keeps that "
  "resilience view while staying clearly labeled as his original "
  "interpretation."),
},
{
 "key": "tissue-culture", "name": "Plant Tissue Culture and Micropropagation",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A single plant cell can rebuild a whole plant — totipotency — and "
  "tissue culture exploits it to clone plants by the thousand in "
  "sterile jars. The recipe, standardized by Murashige and Skoog in "
  "1962, is a nutrient gel with sugars, minerals, vitamins, and "
  "precisely tuned hormones: high cytokinin-to-auxin grows shoots, "
  "high auxin-to-cytokinin grows roots. A speck of meristem goes in; "
  "weeks later dozens of shoots come out; each is rooted, hardened "
  "off, and planted — genetically identical to the parent. "
  "Micropropagation multiplies elite plants exponentially: 5 "
  "explants making 4 shoots per cycle reach 20,480 plants in 6 "
  "cycles. The industry runs on it: bananas (all Cavendish are "
  "clones), orchids, strawberries, and forestry clones. Meristem "
  "culture also cleans viruses — the tiny meristem tip usually "
  "outgrows infection — producing certified virus-free potatoes, "
  "garlic, and fruit trees. Somatic embryogenesis and synthetic "
  "seeds (embryos in gel capsules) extend the toolkit."),
 "how_it_works": (
  "The protocol has four stages. Initiation: surface-sterilize the "
  "explant (bleach, alcohol) and place it on sterile medium — "
  "contamination is the constant enemy, so all work happens in "
  "laminar-flow hoods. Multiplication: cytokinin-rich medium forces "
  "axillary buds to branch instead of staying dormant; each subculture "
  "multiplies the shoot count geometrically. Rooting: shoots move to "
  "auxin-rich medium, which triggers adventitious roots. "
  "Acclimatization: plantlets leave the jar's 100-percent humidity "
  "for the greenhouse in stages, or they desiccate — lab leaves have "
  "thin cuticles and lazy stomata. Hormone ratios are the control "
  "knobs, but genotype matters: some cultivars multiply eagerly, "
  "others refuse. Cryopreservation of shoot tips in liquid nitrogen "
  "now backs up collections — including recalcitrant seeds that "
  "cannot be dried and banked."),
 "key_points": [
  "Totipotency: one cell can rebuild a whole plant; Murashige & Skoog (1962) medium standardized the recipe.",
  "Hormone ratios steer fate: high cytokinin/auxin → shoots; high auxin/cytokinin → roots.",
  "Four stages: initiation (sterile), multiplication (geometric), rooting, acclimatization.",
  "Exponential cloning: 5 explants × 4 shoots/cycle → 20,480 plants in 6 cycles.",
  "Meristem culture cleans viruses (virus-free potatoes, garlic); cryopreservation backs up collections."],
 "requirements": [
  "The 'Plant Cell' and 'Plant Hormones' records above."],
 "standards": ["Standard tissue-culture terminology", "SI units throughout"],
 "citations": [CIT_TAIZ, CIT_MAUSETH],
 "demo_kind": "micropropagation_math",
 "sig_lens": (
  "The Signature reading treats tissue culture as a clean-room "
  "manufacturing line: sterile inputs, hormone-ratio control knobs, "
  "geometric multiplication, and a hardening-off QA stage — with "
  "virus-cleaning as the decontamination pass and cryopreservation as "
  "cold backup. Signature botany keeps that manufacturing view while "
  "staying clearly labeled as his original interpretation."),
},
{
 "key": "grafting", "name": "Grafting and Vegetative Propagation",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Grafting joins two plants into one: the scion (the desired variety's "
  "shoot) fused onto the rootstock (chosen for roots, disease "
  "resistance, or dwarfing). Every Honeycrisp apple, every wine grape "
  "variety, nearly every citrus tree is a grafted clone — because "
  "apples and grapes grown from seed do not come true to type. The "
  "union works only if the cambium layers align: the living cambium "
  "of stock and scion must touch so callus bridges the wound and "
  "differentiates into continuous xylem and phloem. Compatibility "
  "follows relatedness — same species usually works, same genus "
  "often, same family sometimes, beyond that almost never. Rootstocks "
  "are the hidden half of orchards: dwarfing apple rootstocks (the "
  "Malling series) shrink trees to pickable size and fruit years "
  "earlier; phylloxera-resistant American grape rootstocks saved "
  "European wine in the 19th century. Other vegetative propagation — "
  "cuttings, layering, division, runners — clones plants without the "
  "union: willows root from a stick pushed in mud, strawberries "
  "colonize via stolons."),
 "how_it_works": (
  "A graft heals like a surgical join. The cut faces are bound so "
  "cambium meets cambium; parenchyma cells proliferate into callus "
  "that fills the gap; then the callus differentiates — new cambium "
  "forms across the bridge, laying down xylem inward and phloem "
  "outward until the plumbing is continuous. The scion keeps its "
  "genetics (the fruit is the scion's variety) while the rootstock "
  "imposes its traits: vigor, dwarfing, cold hardiness, soil "
  "tolerance, disease resistance. Signals cross the union both ways "
  "— dwarfing rootstocks restrict auxin and water flow, which is "
  "partly how they shrink the scion. Timing matters: graft in late "
  "winter when both partners are dormant but the cambium is about to "
  "wake, and the spring sap surge welds the union. Failed grafts "
  "usually trace to cambium misalignment, desiccation of the scion, "
  "or incompatible partners whose tissues reject."),
 "key_points": [
  "Graft = scion (fruit variety) on rootstock (roots, resistance, dwarfing); every named apple and wine grape is a grafted clone.",
  "The union needs cambium-to-cambium contact; callus bridges, then differentiates into continuous xylem/phloem.",
  "Compatibility follows relatedness: species > genus > family; beyond family, almost never.",
  "Dwarfing rootstocks (Malling series) shrink trees for picking and early fruit; American rootstocks saved European wine from phylloxera.",
  "Cuttings, layering, division, and runners clone without a union — willows root from sticks, strawberries via stolons."],
 "requirements": [
  "The 'Stems' record above (cambium, xylem/phloem)."],
 "standards": ["Standard horticultural terminology", "SI units throughout"],
 "citations": [CIT_MAUSETH, CIT_STD],
 "demo_kind": "graft_compatibility",
 "sig_lens": (
  "The Signature reading treats grafting as modular assembly: a "
  "fruit-module (scion) hot-swapped onto a chassis-module (rootstock) "
  "with a cambium-to-cambium weld spec, compatibility gated by "
  "relatedness, and the rootstock as the performance tune — dwarfing, "
  "hardening, disease-proofing. Signature botany keeps that modular "
  "view while staying clearly labeled as his original interpretation."),
},
{
 "key": "dendrochronology", "name": "Dendrochronology: Reading Tree Rings",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Each year a temperate tree lays down one growth ring — light, "
  "fast-grown earlywood in spring, dark dense latewood in summer — "
  "and the ring's width records the year's conditions: wide rings "
  "mean wet, favorable years; narrow rings mean drought or cold. "
  "Dendrochronology reads these records by cross-dating: matching "
  "the distinctive pattern of wide and narrow rings across many "
  "trees to build a continuous master chronology. Overlaps extend "
  "the record far beyond any single tree's life — bristlecone pine "
  "chronologies reach back over 8,000 years. The applications are "
  "remarkable: dating wooden buildings, ships, and art panels to "
  "the exact year (and sometimes season) the tree was felled; "
  "reconstructing droughts, fires, and insect outbreaks centuries "
  "before instruments; and calibrating radiocarbon dating, since "
  "rings of known age revealed that atmospheric carbon-14 has "
  "varied over time."),
 "how_it_works": (
  "Cross-dating is pattern matching. Take cores from living trees, "
  "dead snags, and old beams; measure every ring width to 0.01 mm; "
  "then slide the sequences against each other until the signature "
  "years — a famous drought, a volcanic cold snap — line up across "
  "all samples. Statistical correlation confirms the match "
  "(typically r > 0.6 for a solid cross-date). Once anchored to the "
  "present by living trees, the floating chronology of dead wood "
  "locks into calendar years. Climate reconstruction inverts the "
  "logic: with the chronology fixed, ring width becomes a proxy "
  "thermometer and rain gauge — regressed against instrumental "
  "records where they overlap, then extended backward. The "
  "bristlecone record exposed the medieval warm period and the "
  "Little Ice Age in the American West; European oak chronologies "
  "date Neolithic trackways and Viking ships."),
 "key_points": [
  "One ring per year in temperate trees: wide = favorable, narrow = drought/cold.",
  "Cross-dating matches ring patterns across trees to build master chronologies; bristlecones exceed 8,000 years.",
  "Dates wooden artifacts to the exact felling year — buildings, ships, art panels.",
  "Ring width is a climate proxy: reconstructs droughts, fires, and insect outbreaks pre-instruments.",
  "Tree rings calibrate radiocarbon dating by revealing past atmospheric carbon-14 variation."],
 "requirements": [
  "The 'Stems' record above (secondary growth, cambium).",
  "Basic correlation idea (high-school statistics level)."],
 "standards": ["Standard dendrochronology terminology", "SI units throughout"],
 "citations": [CIT_STD, CIT_RAVEN],
 "demo_kind": "ring_climate_corr",
 "sig_lens": (
  "The Signature reading treats each trunk as a write-once log "
  "drive: one ring appended per year, bandwidth encoding the "
  "season's conditions, with cross-dating as the checksum that "
  "syncs overlapping logs into an 8,000-year master timeline. "
  "Signature botany keeps that data-systems view while staying "
  "clearly labeled as his original interpretation."),
},
{
 "key": "epiphytes", "name": "Epiphytes: Life in the Canopy",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Epiphytes are plants that live on other plants without parasitizing "
  "them — tenants, not thieves. In tropical rainforests they can make "
  "up a third of all plant species: orchids (the largest plant family, "
  "mostly epiphytic), bromeliads, ferns, mosses, and lichens carpeting "
  "branches from trunk to crown. The canopy is a desert in the sky: "
  "no soil, violent wet-dry cycles, intense light. Epiphytes answer "
  "with specialized gear. Tank bromeliads (like Tillandsia) form "
  "watertight leaf rosettes that impound rain — a single plant can "
  "hold a liter — complete with its own miniature ecosystem of "
  "tadpoles, insects, and absorbed nutrients from drowned debris. "
  "Orchids and many ferns grow velamen, a spongy multi-layered root "
  "covering that drinks rain in seconds and seals against drying. "
  "Staghorn ferns build shield fronds that trap falling leaves into "
  "self-made compost. Some, like Spanish moss, absorb everything "
  "through trichome-covered leaves and need no roots at all."),
 "how_it_works": (
  "Survival is water budgeting between storms. Velamen works as a "
  "rapid sponge: dead, air-filled cells wick water by capillarity "
  "the instant rain hits, then the living cells beneath drink from "
  "the sponge while the outer layer dries into an insulating seal — "
  "uptake in minutes, storage for days. Tank bromeliads run the "
  "opposite strategy: impound bulk water in the rosette and absorb "
  "it slowly through leaf-base scales (trichomes), while the trapped "
  "detritus and its decomposers supply nitrogen and phosphorus the "
  "air cannot. Many epiphytes are CAM plants, sealing stomata by day "
  "to survive the canopy's drying winds. Nutrient capture is "
  "opportunistic: dust, leached throughfall, ant colonies nesting "
  "in hollow tubers (myrmecophytes like Hydnophytum trade housing "
  "for fertilizer), and canopy soils — mats of decomposed epiphyte "
  "debris that accumulate on old branches."),
 "key_points": [
  "Epiphytes live on plants without parasitizing; up to a third of rainforest plant species.",
  "The canopy is a sky desert: no soil, wet-dry cycles, intense light.",
  "Tank bromeliads impound ~1 L of rain in leaf rosettes with their own mini-ecosystems.",
  "Velamen (orchids, aroids) is a sponge root-cover: drinks in minutes, seals against drying.",
  "CAM photosynthesis, trichome absorption, ant partnerships, and canopy soils complete the toolkit."],
 "requirements": [
  "The 'C3, C4, and CAM' and 'Leaves' records above."],
 "standards": ["ICNafp nomenclature for plant names", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_MAUSETH],
 "demo_kind": "canopy_tank_water",
 "sig_lens": (
  "The Signature reading treats the epiphyte as an off-grid rooftop "
  "installation: rainwater harvesting tanks (bromeliads), sponge "
  "intake membranes (velamen), compost reactors (staghorn shields), "
  "and tenant-farmer contracts with ants — all running the CAM "
  "low-power mode. Signature botany keeps that off-grid view while "
  "staying clearly labeled as his original interpretation."),
},
{
 "key": "paleobotany", "name": "Paleobotany: The Fossil Record of Plants",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Paleobotany reads the 470-million-year history of plants from "
  "fossils. The timeline: the first land plants (cryptospores and "
  "tiny liverwort-like pioneers) around 470 million years ago; "
  "Cooksonia, the first vascular plant with upright stems, about 425 "
  "million years ago; the first forests of giant horsetails and "
  "progymnosperms by 390 million; seeds by 360 million; the great "
  "Carboniferous coal forests of lycopod giants (Lepidodendron, 30+ "
  "meters) 300 million years ago — their buried remains became the "
  "coal that powered the industrial revolution. Gymnosperms rose in "
  "the Permian; then, about 140 million years ago, angiosperms "
  "appeared and radiated explosively through the Cretaceous. The "
  "asteroid at 66 million years ago that ended the dinosaurs also "
  "extinguished roughly half of plant species — ferns, the disaster "
  "taxa, blanketed the post-impact world in a 'fern spike' before "
  "forests recovered."),
 "how_it_works": (
  "Plant fossils are mostly fragments — leaves, wood, pollen, spores "
  "— preserved where burial was fast: river deltas, volcanic ash, "
  "peat bogs. Pollen and spores are the workhorses: their sporopollenin "
  "walls are nearly indestructible, so a gram of sediment can hold "
  "thousands of identifiable grains, letting palynologists track "
  "vegetation and climate through entire geological periods. Whole-"
  "plant reconstruction is detective work — a trunk, leaf, and cone "
  "found separately may belong to one species, linked by co-"
  "occurrence and anatomy. Fossil stomatal density records ancient "
  "CO2: fewer stomata mean higher CO2, calibrating greenhouse climates "
  "of the deep past. The coal measures are the economic payoff: "
  "Carboniferous forests that never fully decayed (lignin-digesting "
  "fungi had not yet evolved) became coal seams — fossilized "
  "photosynthesis, burned 300 million years later."),
 "key_points": [
  "470 mya: first land plants; 425 mya: Cooksonia (first vascular plant); 360 mya: seeds; 300 mya: coal forests.",
  "Carboniferous lycopod giants became the coal of the industrial revolution (lignin-eaters had not yet evolved).",
  "~140 mya: angiosperms appear and radiate through the Cretaceous; 66 mya: asteroid wipes out ~half of plant species.",
  "Pollen/spore walls (sporopollenin) are nearly indestructible — palynology tracks vegetation across deep time.",
  "Fossil stomatal density records ancient CO2; fragment assembly reconstructs whole extinct plants."],
 "requirements": [
  "The 'Bryophytes', 'Ferns', 'Gymnosperms', and 'Angiosperms' records above."],
 "standards": ["Standard geologic time scale", "SI units throughout"],
 "citations": [CIT_RAVEN, CIT_STD],
 "demo_kind": "fossil_timeline",
 "sig_lens": (
  "The Signature reading treats the fossil record as the version "
  "history of the plant platform: commit 470 mya (land), 425 mya "
  "(vascular), 360 mya (seed), 140 mya (flower) — with the coal "
  "measures as archived energy and the K-Pg boundary as the crash "
  "log. Signature botany keeps that version-history view while "
  "staying clearly labeled as his original interpretation."),
},
{
 "key": "breeding", "name": "Plant Breeding and Crop Improvement",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Every crop is a human-edited plant: teosinte's tiny ear became "
  "maize, wild mustard became cabbage, broccoli, kale, and "
  "cauliflower, and a weedy grass became wheat. Plant breeding is "
  "the science of directing that evolution. Classical breeding "
  "crosses parents with complementary traits and selects the best "
  "offspring over generations — the breeder's equation predicts the "
  "gain: response equals heritability times the selection "
  "differential (R = h²S). If a trait is 40 percent heritable and "
  "you select parents 10 units above the mean, expect ~4 units of "
  "gain per generation. Hybrid breeding exploits heterosis (hybrid "
  "vigor): cross two inbred lines and the F1 outyields both, which "
  "is why nearly all commercial maize is hybrid seed replanted "
  "yearly. Modern tools accelerate the cycle: marker-assisted "
  "selection tracks DNA markers instead of waiting for the trait, "
  "genomic selection predicts performance from whole-genome data, "
  "doubled haploids produce instant inbred lines, and gene editing "
  "(CRISPR) makes precise changes without foreign DNA."),
 "how_it_works": (
  "A breeding program is a numbers game. Cross hundreds of parent "
  "combinations, grow thousands of progeny in replicated trials "
  "across locations and years, measure yield, disease, quality — "
  "and select the top fraction. The breeder's equation sets the "
  "tempo: high heritability plus intense selection equals fast "
  "gain, which is why highly heritable traits (plant height) move "
  "fast and low-heritability ones (yield itself) move slowly. "
  "Backcrossing moves one gene — say a rust-resistance gene from a "
  "wild relative — into an elite variety: cross, then repeatedly "
  "cross back to the elite parent while selecting for the gene, "
  "recovering the elite genome plus the new trait in ~6 generations. "
  "Mutation breeding (radiation or chemicals) and wide crosses "
  "inject new variation when the gene pool runs dry. Every release "
  "is tested for distinctness, uniformity, and stability before "
  "certification — the seed that reaches the farmer is the product "
  "of a decade or more of selection."),
 "key_points": [
  "All crops are human-edited: teosinte→maize, wild mustard→cabbage/broccoli/kale, wild grass→wheat.",
  "Breeder's equation: R = h²S — response = heritability × selection differential.",
  "Hybrid vigor (heterosis): F1 of two inbreds outyields both parents — why maize seed is replanted yearly.",
  "Backcrossing moves one gene (e.g., rust resistance) into an elite variety in ~6 generations.",
  "Modern stack: marker-assisted and genomic selection, doubled haploids, CRISPR editing."],
 "requirements": [
  "The 'Mendel and Plant Genetics' record above.",
  "Comfort with the heritability concept."],
 "standards": ["Standard plant-breeding terminology", "SI units throughout"],
 "citations": [CIT_STD, CIT_RAVEN],
 "demo_kind": "breeders_equation",
 "sig_lens": (
  "The Signature reading treats breeding as directed evolution with "
  "a control equation: heritability and selection pressure as the "
  "tuning knobs, backcrossing as a targeted patch, hybrids as "
  "performance builds, and gene editing as the precision refactor — "
  "each release a versioned, certified product. Signature botany "
  "keeps that release-engineering view while staying clearly labeled "
  "as his original interpretation."),
},
]
