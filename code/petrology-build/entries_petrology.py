#!/usr/bin/env python3
"""Seed entries for the Petrology field build (field #9, taxonomy order).

Verified 2026-10-17: NO database covers petrology as a science. Manifest
slug 'rocks-minerals' is a 52-record seed-generated specimen catalog (rock
overviews, FAQs, applications) with no igneous/metamorphic/sedimentary
petrology, no IUGS classification, no phase equilibria, no metamorphic
facies science, and no petrographic microscopy; 'geology' is the broad
generated geology database, not a dedicated petrology science database.
'petroleum-engineers' / 'public-petroleum-engineers' are oil-and-gas
industry databases, unrelated to petrology the science. So this build
creates two NEW databases:

  petrology              — The Petrology Database (public-harvest: real,
                           fact-checked petrology — igneous, sedimentary,
                           and metamorphic petrology; magma genesis;
                           Bowen's reaction series; IUGS, QAP, and TAS
                           classification; textures and structures;
                           sedimentary provenance and diagenesis;
                           carbonate petrology; metamorphic grade, facies,
                           and textures; phase equilibria and the lever
                           rule; geothermobarometry; petrographic
                           microscopy; igneous geochemistry; ophiolites;
                           granite petrogenesis; P-T-t paths; experimental
                           and field petrology)
  petrology-signature    — The Petrology Signature Database (his original
                           Signature interpretation; src signature, titles
                           suffixed " (Signature Edition)", never presented
                           as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

# Shared citation constants (standard petrology literature)
CIT_BOWEN = ("Bowen, N. L. (1928). 'The Evolution of the Igneous Rocks'. "
             "Princeton University Press.")
CIT_BEST = ("Best, M. G. (2002). 'Igneous and Metamorphic Petrology', "
            "2nd ed. Wiley-Blackwell.")
CIT_WINTER = ("Winter, J. D. (2013). 'Principles of Igneous and Metamorphic "
              "Petrology', 2nd ed. Pearson.")
CIT_PHILPOTTS = ("Philpotts, A. R. & Ague, J. J. (2009). 'Principles of "
                 "Igneous and Metamorphic Petrology', 2nd ed. Cambridge "
                 "University Press.")
CIT_LEMAITRE = ("Le Maitre, R. W. et al. (2002). 'Igneous Rocks: A "
                "Classification and Glossary of Terms', 2nd ed. Cambridge "
                "University Press (IUGS Subcommission on the Systematics of "
                "Igneous Rocks).")
CIT_TUCKER = ("Tucker, M. E. (2001). 'Sedimentary Petrology', 3rd ed. "
              "Wiley-Blackwell.")
CIT_BOGGS = ("Boggs, S. (2009). 'Petrology of Sedimentary Rocks', 2nd ed. "
             "Cambridge University Press.")
CIT_FOLK = ("Folk, R. L. (1974). 'Petrology of Sedimentary Rocks'. Hemphill "
            "Publishing, Austin.")
CIT_DUNHAM = ("Dunham, R. J. (1962). 'Classification of carbonate rocks "
              "according to depositional texture.' AAPG Memoir 1: 108-121.")
CIT_YARDLEY = ("Yardley, B. W. D. & Warren, C. (2021). 'An Introduction to "
               "Metamorphic Petrology', 2nd ed. Cambridge University Press.")
CIT_SPEAR = ("Spear, F. S. (1993). 'Metamorphic Phase Equilibria and "
             "Pressure-Temperature-Time Paths.' Mineralogical Society of "
             "America Monograph.")
CIT_MIYASHIRO = ("Miyashiro, A. (1994). 'Metamorphic Petrology'. Oxford "
                 "University Press.")
CIT_NESSE = ("Nesse, W. D. (2012). 'Introduction to Optical Mineralogy', "
             "4th ed. Oxford University Press.")
CIT_DICKINSON = ("Dickinson, W. R. & Suczek, C. A. (1979). 'Plate tectonics "
                 "and sandstone compositions.' AAPG Bulletin 63: 2164-2182.")
CIT_FERRY = ("Ferry, J. M. & Spear, F. S. (1978). 'Experimental calibration "
             "of the partitioning of Fe and Mg between biotite and garnet.' "
             "Contributions to Mineralogy and Petrology 66: 113-117.")
CIT_CHAPPELL = ("Chappell, B. W. & White, A. J. R. (1974). 'Two contrasting "
                "granite types.' Pacific Geology 8: 173-174.")
CIT_HUTTON = ("Hutton, J. (1788). 'Theory of the Earth.' Transactions of the "
              "Royal Society of Edinburgh.")
CIT_ESKOLA = ("Eskola, P. (1915). 'The minerals of the Norwegian "
              "anorthosites compared with those of other basic rocks.' "
              "Videnskapsselskapets Skrifter, Kristiania.")
CIT_STD = ("Standard petrology literature (peer-reviewed textbooks and "
           "journals).")
SIG_TAIL = ("Signature editions are original Signature interpretations of "
            "petrology, written in the Signature system — clearly labeled "
            "Signature-made, never presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-petrology", "name": "What Is Petrology: The Science of Rocks",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Petrology is the science of rocks — their origin, composition, texture, "
  "structure, and history. It has three linked branches: petrography, the "
  "systematic description and classification of rocks; petrogenesis, the study "
  "of how rocks form; and experimental petrology, which recreates rock-forming "
  "conditions in the laboratory. The science divides naturally into igneous "
  "petrology (rocks from molten magma), sedimentary petrology (rocks from "
  "accumulated sediment), and metamorphic petrology (rocks transformed by heat "
  "and pressure). Petrologists read rocks the way historians read documents: "
  "a granite records a cooling magma chamber kilometers deep, a sandstone "
  "records an ancient river or beach, a schist records a mountain belt being "
  "built. Every rock is a physical record of temperature, pressure, chemistry, "
  "and time, and petrology is the toolkit for decoding it."),
 "how_it_works": (
  "Petrology works by working backward from the observable to the process. "
  "A petrologist starts with a hand sample or thin section: What minerals are "
  "present, in what proportions, with what textures and structures? Those "
  "observations are classified — an igneous rock by its IUGS name, a "
  "sedimentary rock by grain size and composition, a metamorphic rock by its "
  "facies and grade. Then the interpretation step asks what conditions those "
  "observations demand: this mineral assemblage is only stable at certain "
  "pressures and temperatures, this texture means fast or slow cooling, this "
  "sedimentary structure means a river, not a deep sea. Phase diagrams, "
  "geothermobarometers, and isotopic data turn qualitative reading into "
  "quantitative pressure-temperature-time paths. The loop closes when the "
  "inferred history predicts something testable — a hidden ore body, the age "
  "of a mountain belt, the depth of a magma chamber."),
 "key_points": [
  "Petrology: the science of rocks — origin, composition, texture, structure, and history",
  "Three branches: petrography (description/classification), petrogenesis (origins), experimental petrology (lab recreation)",
  "Three rock families: igneous (from magma), sedimentary (from sediment), metamorphic (transformed by heat and pressure)",
  "Every rock is a physical record of temperature, pressure, chemistry, and time",
  "Method: observe minerals and textures, classify, then invert the observations into formation conditions",
  "Quantitative tools: phase diagrams, geothermobarometers, isotopic dating, P-T-t paths",
 ],
 "requirements": [
  "Curiosity about what rocks are made of and where they come from",
  "A hand lens and a few rock samples (granite, basalt, sandstone, schist) to compare",
  "Basic chemistry: elements, minerals, and simple formulas",
  "Willingness to learn the three rock families before the details",
 ],
 "standards": [
  "IUGS classification conventions for igneous rocks (Le Maitre et al. 2002)",
  "Three-fold rock division per standard petrology textbooks (Best 2002; Winter 2013)",
 ],
 "citations": [CIT_BEST, CIT_WINTER],
 "sig_lens": (
  "Signature edition: petrology reframed as his original rock-reading "
  "operating system — every rock decoded as a solved record of deep time, "
  "with his Signature framework for inverting any hand sample into its "
  "formation story."),
 "demo_kind": "petro_branches",
},
{
 "key": "rock-cycle", "name": "The Rock Cycle: How Rocks Transform Into Each Other",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "The rock cycle is the grand loop connecting the three rock families: "
  "magma cools to form igneous rock; igneous rock weathers and erodes into "
  "sediment; sediment compacts and cements into sedimentary rock; sedimentary "
  "rock buried deep is heated and squeezed into metamorphic rock; metamorphic "
  "rock can melt back into magma — and any rock can be uplifted and weathered "
  "back to sediment. James Hutton grasped the cycle's essence in 1788: with "
  "\"no vestige of a beginning, no prospect of an end,\" Earth's materials "
  "recycle endlessly. There is no required order and no starting point — a "
  "metamorphic rock can weather directly to sediment, an igneous rock can be "
  "metamorphosed without ever becoming sediment. The cycle is driven by "
  "Earth's internal heat (melting, metamorphism) and by surface processes "
  "powered by the Sun and gravity (weathering, erosion, deposition)."),
 "how_it_works": (
  "Each arrow in the rock cycle is a real physical process with a direction. "
  "Cooling and crystallization turn magma into igneous rock — fast at the "
  "surface (volcanic), slow deep underground (plutonic). Weathering (chemical "
  "breakdown) plus erosion (physical removal) turn any exposed rock into "
  "sediment, which is transported and deposited in layers. Lithification — "
  "compaction under burial plus cementation by mineral-rich groundwater — "
  "turns sediment into sedimentary rock. Burial to depths where temperatures "
  "exceed about 200°C and pressures climb turns sedimentary or igneous rock "
  "into metamorphic rock without melting it. Heating past the solidus melts "
  "rock back into magma. Uplift and erosion can intercept any rock at any "
  "stage and return it to sediment. Reading a landscape means spotting which "
  "arrows are active: a volcano is magma-to-igneous, a canyon is "
  "rock-to-sediment, a mountain belt is rock-to-metamorphic."),
 "key_points": [
  "The rock cycle links magma, igneous, sediment, sedimentary, and metamorphic rock in a continuous loop",
  "Hutton (1788): Earth's materials recycle with 'no vestige of a beginning, no prospect of an end'",
  "No required order — any rock can become sediment via uplift, weathering, and erosion",
  "Internal heat drives melting and metamorphism; Sun and gravity drive weathering, erosion, and deposition",
  "Each arrow is a named process: crystallization, weathering, erosion, deposition, lithification, metamorphism, melting",
  "Igneous rock can be metamorphosed directly without ever passing through sediment",
 ],
 "requirements": [
  "One sample each of igneous, sedimentary, and metamorphic rock to handle",
  "Understanding that the cycle has no start and no end",
  "Basic vocabulary: weathering, erosion, deposition, lithification, metamorphism, melting",
  "A sketch of the cycle to annotate as each process is learned",
 ],
 "standards": [
  "Rock-cycle process definitions per standard petrology texts (Best 2002; Winter 2013)",
  "Hutton's uniformitarian framing of deep-time cycling (Hutton 1788)",
 ],
 "citations": [CIT_HUTTON, CIT_BEST],
 "sig_lens": (
  "Signature edition: the rock cycle rebuilt as his original circulation "
  "engine — Earth's materials tracked as conserved inventory flowing between "
  "five reservoirs, with his Signature accounting of what each arrow costs "
  "in heat, pressure, and time."),
 "demo_kind": "rock_cycle",
},
{
 "key": "igneous-rocks", "name": "Igneous Rocks: Born from Molten Magma",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Igneous rocks form when molten magma or lava cools and solidifies. They "
  "split two ways: by where they cool — intrusive (plutonic) rocks like "
  "granite cool slowly deep underground and grow large visible crystals, "
  "while extrusive (volcanic) rocks like basalt cool fast at the surface and "
  "freeze with tiny or no crystals — and by chemistry, measured as silica "
  "(SiO2) content: felsic rocks (over 63% silica, e.g., granite, rhyolite) "
  "are light-colored and rich in quartz and feldspar; intermediate rocks "
  "(52-63%, e.g., diorite, andesite); mafic rocks (45-52%, e.g., gabbro, "
  "basalt) are dark and rich in olivine and pyroxene; ultramafic rocks "
  "(under 45%, e.g., peridotite) are the dense green rocks of Earth's "
  "mantle. Silica controls almost everything: high-silica magmas are cool, "
  "thick, and explosive; low-silica magmas are hot, runny, and effusive."),
 "how_it_works": (
  "An igneous rock records its magma's chemistry and its cooling history in "
  "its minerals and grain size. As magma cools, minerals crystallize in a "
  "predictable order (Bowen's reaction series): olivine and calcium-rich "
  "plagioclase first at high temperature, quartz and potassium feldspar last. "
  "Slow cooling deep underground gives atoms time to migrate to growing "
  "crystals, producing the coarse interlocking grains of granite and gabbro. "
  "Fast cooling at the surface freezes the melt before crystals can grow, "
  "giving the fine grains of basalt or the glass of obsidian. Chemistry sets "
  "the mineral menu — a silica-poor magma simply cannot grow quartz, so it "
  "grows olivine and pyroxene instead. Petrologists therefore read an igneous "
  "rock in two passes: grain size reveals where and how fast it cooled, "
  "mineralogy reveals what the magma was made of."),
 "key_points": [
  "Igneous rocks crystallize from magma (underground) or lava (at the surface)",
  "Intrusive/plutonic (granite): slow cooling, large crystals; extrusive/volcanic (basalt): fast cooling, tiny crystals",
  "Chemistry ladder by silica: felsic >63%, intermediate 52-63%, mafic 45-52%, ultramafic <45%",
  "Silica controls behavior: high-silica magmas are viscous and explosive; low-silica magmas are fluid and effusive",
  "Minerals crystallize in a predictable temperature order (Bowen's reaction series)",
  "Grain size reads cooling history; mineralogy reads magma chemistry",
 ],
 "requirements": [
  "Hand samples of granite (coarse, light) and basalt (fine, dark) side by side",
  "Understanding of silica percentage as the master chemical variable",
  "A hand lens to see that granite's 'speckles' are individual interlocking crystals",
  "Knowledge that obsidian is quenched melt — volcanic glass, not a mineral",
 ],
 "standards": [
  "Silica-based chemical divisions per IUGS conventions (Le Maitre et al. 2002)",
  "Intrusive/extrusive textural definitions per standard texts (Best 2002; Winter 2013)",
 ],
 "citations": [CIT_LEMAITRE, CIT_BEST],
 "sig_lens": (
  "Signature edition: igneous rocks decoded as his original freeze-frame "
  "system — each specimen read as a stopped clock showing exactly when and "
  "where its magma's cooling was arrested."),
 "demo_kind": "igneous_classes",
},
{
 "key": "sedimentary-rocks", "name": "Sedimentary Rocks: Layers of Earth's History",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Sedimentary rocks form from accumulated sediment — the broken, dissolved, "
  "and biological debris of older rocks. They fall into three groups: "
  "clastic rocks built from fragments (conglomerate from gravel, sandstone "
  "from sand, shale from mud), chemical rocks precipitated from water "
  "(limestone, rock salt, gypsum), and organic rocks from living things "
  "(coal from plants, some limestones from shells). Their journey has four "
  "stages: weathering breaks rock down, erosion and transport move the "
  "debris, deposition lays it down in layers, and lithification — compaction "
  "plus cementation — turns loose sediment into solid rock. Because they "
  "form layer by layer at Earth's surface, sedimentary rocks are the "
  "archive: they hold fossils, record ancient rivers, beaches, deserts, and "
  "seas, and stack into the stratigraphic record geologists read like pages."),
 "how_it_works": (
  "Sedimentary petrology works by reversing the four-stage journey. Grain "
  "size tells transport energy: gravel needs a torrent, mud settles only in "
  "still water. Grain roundness and sorting tell transport distance — long "
  "journeys round and sort grains, short ones leave them angular and mixed. "
  "Composition tells the source: quartz-rich sand means a long-lived "
  "continental source, feldspar-rich sand means rapid erosion near its "
  "origin. Sedimentary structures — cross-bedding, ripples, mud cracks — "
  "record the depositional environment directly: dunes in a desert, ripples "
  "on a beach, mud cracks on a drying flat. Fossils and layer order give "
  "age and environment together. Lithification's fingerprints — compacted "
  "grains, cement-filled pores — reveal burial history. Each observation is "
  "one reversed step from rock back to the landscape that made it."),
 "key_points": [
  "Three groups: clastic (fragments), chemical (precipitates), organic (biological remains)",
  "Four stages: weathering, erosion/transport, deposition, lithification (compaction + cementation)",
  "Grain size records transport energy; roundness and sorting record transport distance",
  "Sedimentary structures (cross-bedding, ripples, mud cracks) record depositional environments",
  "Sedimentary rocks are the stratigraphic archive: fossils, ancient landscapes, and geologic time",
  "Composition fingerprints the source rocks (provenance)",
 ],
 "requirements": [
  "Samples of sandstone, shale, and limestone to compare grain and layering",
  "Understanding of the Wentworth grain-size scale (gravel, sand, silt, clay)",
  "Basic vocabulary: weathering, transport, deposition, compaction, cementation",
  "Awareness that fossils occur essentially only in sedimentary rocks",
 ],
 "standards": [
  "Clastic/chemical/organic division and Wentworth scale per standard texts (Tucker 2001; Boggs 2009)",
  "Lithification process definitions per sedimentary petrology conventions",
 ],
 "citations": [CIT_TUCKER, CIT_BOGGS],
 "sig_lens": (
  "Signature edition: sedimentary rocks rebuilt as his original surface-"
  "memory system — every layer read as a stored frame of an ancient "
  "landscape, with his Signature method for replaying deposition in reverse."),
 "demo_kind": "sediment_classes",
},
{
 "key": "metamorphic-rocks", "name": "Metamorphic Rocks: Transformed by Heat and Pressure",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Metamorphic rocks are older rocks transformed by heat, pressure, and "
  "chemically active fluids — without melting. The original rock, called "
  "the protolith, can be igneous (a granite becomes a gneiss), sedimentary "
  "(a shale becomes a schist, a limestone becomes a marble, a sandstone "
  "becomes a quartzite), or already metamorphic. Three agents do the work: "
  "heat (above roughly 200°C) speeds atomic diffusion so new minerals can "
  "grow; directed pressure squeezes minerals into aligned, foliated fabrics; "
  "hot fluids carry dissolved ions that rebuild mineralogy. Low-grade "
  "metamorphism (slate from shale) barely changes the rock; high-grade "
  "metamorphism (gneiss, migmatite) rebuilds it completely, and at the "
  "extreme the rock begins to melt. Metamorphic rocks are the roots of "
  "mountain belts, exposed where deep crust has been uplifted and eroded."),
 "how_it_works": (
  "Metamorphism works as solid-state recrystallization: atoms rearrange "
  "without the rock ever becoming liquid. Heat provides the energy for "
  "diffusion; pressure does two jobs — confining pressure (equal from all "
  "sides) favors denser minerals, while directed pressure (stronger in one "
  "direction, as in colliding plates) rotates and flattens minerals into "
  "foliation, the aligned fabric of slates, schists, and gneisses. Fluids "
  "act as catalysts and transport, dissolving unstable minerals and "
  "precipitating stable ones. The protolith's chemistry limits the outcome: "
  "a shale (aluminum-rich) grows garnet, staurolite, and kyanite with grade; "
  "a limestone (calcium carbonate) recrystallizes to marble almost "
  "regardless of grade. Petrologists read the mineral assemblage to find the "
  "pressure-temperature conditions, the texture to find the deformation "
  "history, and the protolith to reconstruct what was there before the "
  "mountain belt cooked it."),
 "key_points": [
  "Metamorphism transforms rock in the solid state — heat, pressure, and fluids, never melting",
  "The protolith (original rock) can be igneous, sedimentary, or already metamorphic",
  "Heat enables diffusion; directed pressure creates foliation; fluids catalyze mineral reactions",
  "Grade ladder: slate (low) → schist → gneiss → migmatite (high, near melting)",
  "Protolith chemistry controls the product: shale → schist, limestone → marble, sandstone → quartzite",
  "Metamorphic rocks expose the deep roots of mountain belts",
 ],
 "requirements": [
  "Samples of slate, schist, and gneiss showing increasing foliation",
  "Understanding that metamorphism is solid-state (melting = igneous, not metamorphic)",
  "Basic vocabulary: protolith, foliation, grade, recrystallization",
  "Awareness of the three agents: heat, pressure, chemically active fluids",
 ],
 "standards": [
  "Metamorphic agent and grade definitions per standard texts (Yardley & Warren 2021; Winter 2013)",
  "Protolith-product naming conventions per metamorphic petrology usage",
 ],
 "citations": [CIT_YARDLEY, CIT_WINTER],
 "sig_lens": (
  "Signature edition: metamorphism decoded as his original solid-state "
  "rebuild protocol — the protolith tracked as input inventory, the "
  "metamorphic rock as output, with his Signature ledger of what heat, "
  "pressure, and fluids added or removed."),
 "demo_kind": "metamorphic_agents",
},
{
 "key": "magma-and-lava", "name": "Magma and Lava: The Molten Source",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Magma is molten rock underground; lava is the same material once it "
  "reaches the surface — the only difference is location. Magmas range "
  "from about 700°C (cool, silica-rich rhyolitic magma) to about 1300°C "
  "(hot, silica-poor basaltic magma). Silica content is the master control "
  "on behavior: silica tetrahedra polymerize into chains and networks, so "
  "high-silica magma is thousands of times more viscous than low-silica "
  "magma. That is why basaltic lava flows like thin syrup across Hawaii "
  "while rhyolitic magma plugs volcanic throats, pressurizes, and explodes. "
  "Magma also carries dissolved volatiles — mostly water and carbon dioxide "
  "— which stay dissolved under deep pressure but exsolve into bubbles as "
  "magma rises, driving both gentle fountaining and catastrophic "
  "explosions. Eruption style is thus written in the magma's chemistry "
  "before it ever erupts."),
 "how_it_works": (
  "Magma behavior follows from three properties: temperature, composition, "
  "and volatile content. Temperature sets how much of the system is molten "
  "versus crystalline — most magmas are crystal-liquid mushes, not pure "
  "liquids. Silica content sets viscosity through polymerization: each added "
  "percent of SiO2 links more tetrahedra together, stiffening the melt "
  "exponentially. Dissolved water and CO2 act oppositely — they depolymerize "
  "the melt, lowering viscosity — but they are the explosive charge: as "
  "magma ascends, falling pressure lets volatiles exsolve into bubbles, and "
  "bubble growth in a stiff, high-silica melt fragments it into ash and "
  "pumice. In runny basaltic melt the bubbles escape easily, giving "
  "fountains and flows. Petrologists therefore predict eruption style from "
  "chemistry: measure the silica and volatiles, and the volcano's temperament "
  "is largely known."),
 "key_points": [
  "Magma (underground) and lava (surface) are the same material — location is the only difference",
  "Temperature range: ~700°C (rhyolitic) to ~1300°C (basaltic)",
  "Silica polymerizes the melt: high silica = high viscosity = explosive; low silica = fluid = effusive",
  "Dissolved volatiles (H2O, CO2) exsolve as bubbles during ascent and drive explosions",
  "Most magmas are crystal-liquid mushes, not pure liquids",
  "Eruption style is largely predictable from magma chemistry",
 ],
 "requirements": [
  "Understanding that viscosity differences span orders of magnitude with silica",
  "Basic chemistry: silica tetrahedra and polymerization (qualitative is enough)",
  "Familiarity with two end members: Hawaiian basalt flows vs. explosive rhyolitic eruptions",
  "Awareness that volatiles stay dissolved only under pressure",
 ],
 "standards": [
  "Magma temperature and composition ranges per standard igneous texts (Best 2002; Philpotts & Ague 2009)",
  "Viscosity-silica relationship per experimental petrology literature",
 ],
 "citations": [CIT_BEST, CIT_PHILPOTTS],
 "sig_lens": (
  "Signature edition: magma reframed as his original variable-viscosity "
  "transport medium — temperature, silica, and volatiles tuned as three "
  "dials that set every volcano's behavior in his Signature eruption model."),
 "demo_kind": "magma_viscosity",
},
{
 "key": "rock-forming-minerals", "name": "The Rock-Forming Minerals: Petrology's Building Blocks",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "A handful of minerals builds nearly every rock on Earth. The silicates "
  "dominate: olivine (the green mantle mineral, first to crystallize from "
  "basaltic magma), pyroxene and amphibole (the dark chain silicates of "
  "gabbros, basalts, and schists), biotite mica (dark, flaky, water-bearing), "
  "potassium feldspar and plagioclase feldspar (together about 60% of "
  "Earth's crust — the pale workhorses of granites and gabbros), and quartz "
  "(pure silica, the last to crystallize, the survivor of weathering). "
  "Beyond silicates: calcite builds limestones and marbles, dolomite builds "
  "dolostones, clay minerals are the microscopic products of weathering "
  "that become shales, and iron oxides color and stain. Learning to "
  "recognize these ten or so minerals in hand sample and thin section is "
  "the single highest-leverage skill in petrology — everything else is "
  "built from them."),
 "how_it_works": (
  "Rock-forming minerals work as a limited alphabet that spells every rock. "
  "Each has a stability field: olivine is stable hot and dry (mantle, "
  "basalts) but weathers fast at the surface; quartz is stable cool and "
  "silica-rich and survives weathering nearly forever — which is why beach "
  "sand is mostly quartz. Feldspars span the whole igneous range because "
  "calcium-rich plagioclase crystallizes hot and sodium-rich cold. Micas and "
  "amphiboles carry water (OH) in their structures, so their presence "
  "records water in the magma or metamorphic fluid. Carbonates record "
  "surface or low-grade conditions; clays record weathering. A petrologist "
  "identifies the minerals present, notes which are stable together, and "
  "reads the assemblage: olivine + pyroxene + Ca-plagioclase spells gabbro "
  "and a hot mafic origin; quartz + K-feldspar + biotite spells granite and "
  "a cool felsic one."),
 "key_points": [
  "About ten minerals build nearly all rocks: olivine, pyroxene, amphibole, biotite, K-feldspar, plagioclase, quartz, calcite, clays, iron oxides",
  "Feldspars alone make up ~60% of Earth's crust",
  "Each mineral has a stability field: olivine = hot/dry, quartz = cool/silica-rich, micas/amphiboles = water-bearing",
  "Quartz survives weathering — that is why sand is mostly quartz",
  "Mineral assemblages are diagnostic: olivine+pyroxene+Ca-plagioclase = gabbro; quartz+K-feldspar+biotite = granite",
  "Recognizing these minerals is petrology's highest-leverage skill",
 ],
 "requirements": [
  "A mineral identification kit mindset: color, luster, cleavage, hardness, habit",
  "Hand samples showing olivine (green), quartz (glassy), feldspar (blocky cleavage), mica (flakes)",
  "Understanding that the same mineral can occur in igneous, sedimentary, and metamorphic rocks",
  "A thin-section image set helps, but hand-sample skill comes first",
 ],
 "standards": [
  "Rock-forming mineral definitions and stability relations per standard texts (Deer, Howie & Zussman; Best 2002)",
  "Crustal abundance figures per geochemical literature",
 ],
 "citations": [CIT_BEST, CIT_WINTER],
 "sig_lens": (
  "Signature edition: the rock-forming minerals cataloged as his original "
  "ten-piece construction set — each mineral profiled as a Signature "
  "component with its stability envelope, so any rock can be read as an "
  "assembly of parts."),
 "demo_kind": "rock_formers",
},
{
 "key": "intrusive-vs-extrusive", "name": "Intrusive vs. Extrusive: Where Magma Cools Decides Everything",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The same magma makes two completely different rocks depending on where "
  "it cools. Intrusive (plutonic) rocks crystallize slowly kilometers "
  "underground, insulated by surrounding rock: atoms have time to migrate "
  "to growing crystals, producing coarse, visible, interlocking grains — "
  "granite, diorite, gabbro. Extrusive (volcanic) rocks erupt at the "
  "surface and quench in air or water: crystals barely nucleate before the "
  "melt freezes, producing fine grains invisible to the eye — rhyolite, "
  "andesite, basalt — or no crystals at all, as in obsidian glass. "
  "Porphyritic rocks record both: large phenocrysts grown slowly at depth, "
  "then carried up and frozen in a fine groundmass. Cooling rate is thus "
  "the great textural divide of igneous petrology, and grain size is its "
  "direct readout."),
 "how_it_works": (
  "Cooling rate controls texture through the race between nucleation (new "
  "crystals starting) and growth (existing crystals getting bigger). Deep "
  "underground, cooling takes thousands to millions of years: few nuclei "
  "form, each grows large — phaneritic texture, every grain visible. At the "
  "surface, cooling takes minutes to days: countless nuclei form at once, "
  "none grows — aphanitic texture, grains microscopic. Quenching in water or "
  "air can outrun nucleation entirely, freezing disorder into volcanic "
  "glass. Two-stage cooling makes porphyry: slow growth of phenocrysts in a "
  "chamber, then eruption freezes the remaining liquid as fine groundmass. "
  "Because grain size maps so directly onto cooling rate, a petrologist can "
  "hold a rock and know whether its magma died deep underground or in the "
  "open air — and porphyritic rocks even reveal the two-stage journey."),
 "key_points": [
  "Same magma, different cooling site: intrusive = slow/deep/coarse, extrusive = fast/surface/fine",
  "Phaneritic (visible grains) means plutonic; aphanitic (microscopic) means volcanic; glassy means quenched",
  "Nucleation vs. growth race: slow cooling favors growth (few large crystals), fast cooling favors nucleation (many tiny ones)",
  "Porphyritic texture records two-stage cooling: phenocrysts grown at depth, groundmass frozen at eruption",
  "Granite/rhyolite, diorite/andesite, gabbro/basalt are the three great intrusive/extrusive pairs",
  "Grain size is the direct readout of cooling history",
 ],
 "requirements": [
  "Side-by-side samples: granite vs. rhyolite, gabbro vs. basalt",
  "A hand lens to confirm basalt's grains are real crystals, just tiny",
  "Understanding of nucleation and crystal growth (qualitative)",
  "One porphyritic sample showing phenocrysts in fine groundmass",
 ],
 "standards": [
  "Phaneritic/aphanitic/porphyritic textural definitions per IUGS usage (Le Maitre et al. 2002)",
  "Intrusive/extrusive pairs per standard igneous texts",
 ],
 "citations": [CIT_LEMAITRE, CIT_BEST],
 "sig_lens": (
  "Signature edition: cooling site decoded as his original depth-clock — "
  "grain size read as elapsed cooling time, with his Signature chart "
  "converting any texture into the depth where its magma stopped."),
 "demo_kind": "cooling_grain",
},
{
 "key": "igneous-textures", "name": "Reading Igneous Textures: What Grain Patterns Reveal",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Texture — the size, shape, and arrangement of crystals — is an igneous "
  "rock's autobiography. Phaneritic texture (all grains visible) means slow "
  "plutonic cooling. Aphanitic (grains microscopic) means rapid volcanic "
  "cooling. Porphyritic (large phenocrysts in a fine groundmass) means "
  "two-stage cooling. Glassy (no crystals, as in obsidian) means the melt "
  "quenched so fast that atoms froze in disorder. Vesicular texture (frozen "
  "bubble holes, as in pumice and scoria) records gas escaping from the "
  "magma. Pyroclastic texture (angular fragments welded or cemented, as in "
  "tuff) records explosive shattering. Pegmatitic texture (giant crystals, "
  "sometimes meters long) records water-rich residual melt crystallizing "
  "slowly. Each texture is a process frozen mid-step, and naming the "
  "texture is the first act of petrogenetic interpretation."),
 "how_it_works": (
  "Reading texture works as a decision tree run with eyes and hand lens. "
  "First: are crystals visible? If yes and all roughly the same size, the "
  "rock cooled slowly at depth (phaneritic). If some crystals dwarf the "
  "rest, it cooled in two stages (porphyritic) — the big ones are "
  "phenocrysts, the fine ones groundmass. If no grains are visible, check "
  "for glass (smooth, conchoidal fracture → quenched), bubbles (vesicular → "
  "gas-rich eruption), or fragments (pyroclastic → explosive shattering). "
  "Crystal shape adds a second read: euhedral (well-formed) crystals grew "
  "freely in melt and crystallized early; anhedral (shapeless) grains filled "
  "leftover spaces and crystallized late. Grain boundaries tell the "
  "crystallization order — a mineral enclosed by another crystallized "
  "first. Texture plus mineralogy together name the rock and reconstruct "
  "its cooling path."),
 "key_points": [
  "Texture = size, shape, and arrangement of crystals; it records cooling history",
  "Phaneritic (slow/deep), aphanitic (fast/surface), porphyritic (two-stage), glassy (quenched)",
  "Vesicular = frozen gas bubbles; pyroclastic = explosive fragments; pegmatitic = giant water-rich crystals",
  "Euhedral crystals grew early and freely; anhedral grains filled late spaces",
  "Enclosure relationships reveal crystallization order",
  "Naming the texture is the first step of petrogenetic interpretation",
 ],
 "requirements": [
  "A hand lens (10x) — essential for aphanitic vs. glassy vs. fine phaneritic calls",
  "Reference samples of each texture: granite, basalt, porphyry, obsidian, pumice, tuff",
  "Understanding that texture is independent of composition (a felsic and a mafic rock can share a texture)",
  "Practice describing before naming: size, shape, arrangement first",
 ],
 "standards": [
  "Igneous textural terminology per IUGS glossary (Le Maitre et al. 2002)",
  "Phenocryst/groundmass and euhedral/anhedral definitions per standard texts",
 ],
 "citations": [CIT_LEMAITRE, CIT_PHILPOTTS],
 "sig_lens": (
  "Signature edition: igneous textures systematized as his original "
  "process-fingerprint key — every grain pattern matched to the cooling "
  "event that froze it, in his Signature decision tree."),
 "demo_kind": "texture_classify",
},
# ------------------------------------------------------------------ COMPOUNDED
{
 "key": "bowens-reaction-series", "name": "Bowen's Reaction Series: The Order of Crystallization",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "In the 1910s-1920s, N. L. Bowen melted and crystallized synthetic magmas "
  "in the laboratory and discovered that minerals crystallize from a cooling "
  "magma in a fixed order — Bowen's reaction series, published in 'The "
  "Evolution of the Igneous Rocks' (1928). It has two branches. The "
  "discontinuous branch: olivine crystallizes first, then reacts with the "
  "melt to become pyroxene, which reacts to become amphibole, which reacts "
  "to become biotite — each step a reaction between early crystals and "
  "remaining melt. The continuous branch: calcium-rich plagioclase "
  "crystallizes first and reacts continuously toward sodium-rich "
  "plagioclase as cooling proceeds. The branches converge: potassium "
  "feldspar, then muscovite, then quartz crystallize last from the "
  "coolest, most silica-rich residual melt. The series explains why "
  "olivine never coexists stably with quartz (they would react), why "
  "mafic rocks are olivine/pyroxene-rich and felsic rocks quartz/feldspar-"
  "rich, and how one parent magma differentiates into many rock types."),
 "how_it_works": (
  "Bowen's series works because crystallization is a sequence of reactions, "
  "not just freezing. In the discontinuous branch, each mineral is unstable "
  "in the evolving melt once temperature falls past its reaction point: "
  "olivine + melt → pyroxene, pyroxene + melt → amphibole (with water), "
  "amphibole + melt → biotite. If early crystals are removed — by settling "
  "or filter-pressing — the reaction cannot run backward, and the remaining "
  "melt evolves toward silica-rich compositions: this is fractional "
  "crystallization, the engine of magma differentiation. In the continuous "
  "branch, plagioclase forms a solid solution, so a single crystal zones "
  "from calcium-rich core to sodium-rich rim as it reacts with cooling melt. "
  "The practical use is prediction: given a magma's composition, the series "
  "predicts the crystallization order; given a rock's minerals, it reveals "
  "whether equilibrium or fractionation dominated. Normal zoning in "
  "plagioclase (Ca core, Na rim) is the series caught in the act."),
 "key_points": [
  "Bowen (1928): minerals crystallize from cooling magma in a fixed, experimentally determined order",
  "Discontinuous branch: olivine → pyroxene → amphibole → biotite (each reacts with melt to make the next)",
  "Continuous branch: Ca-rich plagioclase → Na-rich plagioclase (solid-solution reaction)",
  "Convergence: K-feldspar → muscovite → quartz crystallize last from cool, silica-rich melt",
  "Removing early crystals (fractionation) drives residual melt toward felsic compositions",
  "Explains mineral incompatibilities (olivine vs. quartz) and zoned plagioclase",
 ],
 "requirements": [
  "Understanding of the igneous mineral set from the foundations tier",
  "Concept of a reaction between crystals and melt (not just freezing)",
  "Familiarity with solid solution (plagioclase Ca-Na series)",
  "Bowen's 'The Evolution of the Igneous Rocks' as the original reference",
 ],
 "standards": [
  "Bowen's reaction series as published (Bowen 1928)",
  "Mineral stability relations per standard igneous texts (Best 2002; Winter 2013)",
 ],
 "citations": [CIT_BOWEN, CIT_BEST],
 "sig_lens": (
  "Signature edition: Bowen's series operationalized as his original "
  "crystallization sequencer — any magma composition fed in, the mineral "
  "parade predicted out, with his Signature flag for where fractionation "
  "breaks the equilibrium order."),
 "demo_kind": "bowen_order",
},
{
 "key": "iugs-classification", "name": "IUGS Classification: The Official Naming of Igneous Rocks",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "The International Union of Geological Sciences (IUGS) Subcommission on "
  "the Systematics of Igneous Rocks gives petrology its official naming "
  "rules (Le Maitre et al., 2002). The foundation is modal mineralogy — "
  "the actual measured percentages of minerals in the rock. For plutonic "
  "rocks with less than 90% mafic minerals (M < 90), classification uses "
  "the QAPF double triangle: Q (quartz), A (alkali feldspar), P "
  "(plagioclase), F (feldspathoids) — the rock's name is read from where "
  "its normalized Q-A-P or F-A-P proportions plot. Volcanic rocks, usually "
  "too fine-grained for modal counting, are classified chemically with the "
  "TAS (total alkalis vs. silica) diagram. Ultramafic rocks (M > 90) use "
  "the olivine-pyroxene-hornblende triangle instead. The system replaced "
  "centuries of local and commercial rock names with one global language: "
  "a granite in Scotland and a granite in Japan are the same precisely "
  "defined thing."),
 "how_it_works": (
  "IUGS classification works as a strict decision procedure. Step one: "
  "measure or estimate the mode — point-count 1,000+ points in thin section "
  "for plutonic rocks. Step two: check the mafic mineral percentage M. If "
  "M exceeds 90%, use the ultramafic triangle. Otherwise, normalize "
  "Q + A + P (or F + A + P) to 100% and plot on the QAPF diagram — the "
  "field the point falls in is the rock's name (granite, granodiorite, "
  "diorite, gabbro, syenite, and so on). For volcanic rocks, get a chemical "
  "analysis and plot total alkalis (Na2O + K2O) against SiO2 on the TAS "
  "diagram — the field gives the name (basalt, andesite, dacite, rhyolite, "
  "trachyte, phonolite). Special rules cover edge cases: glassy rocks, "
  "pyroclastic rocks, and carbonatites each have their own IUGS "
  "recommendations. The discipline of the system is its power — two "
  "petrologists on different continents, given the same mode or analysis, "
  "must arrive at the same name."),
 "key_points": [
  "IUGS (Le Maitre et al. 2002) is the global official naming system for igneous rocks",
  "Based on modal mineralogy (measured mineral percentages), not field appearance",
  "Plutonic rocks with M < 90%: QAPF double triangle (quartz, alkali feldspar, plagioclase, feldspathoids)",
  "Volcanic rocks: TAS diagram (total alkalis vs. silica) from chemical analysis",
  "Ultramafic rocks (M > 90): olivine-pyroxene-hornblende triangle",
  "One global language: the same mode or analysis gives the same name anywhere on Earth",
 ],
 "requirements": [
  "Ability to identify quartz, alkali feldspar, and plagioclase in hand sample or thin section",
  "Understanding of modal percentage (point counting)",
  "The QAPF and TAS diagrams as reference charts",
  "Familiarity with the intrusive/extrusive pairs from the foundations tier",
 ],
 "standards": [
  "IUGS systematics per Le Maitre et al. (2002)",
  "QAPF and TAS field boundaries per IUGS Subcommission recommendations",
 ],
 "citations": [CIT_LEMAITRE, CIT_WINTER],
 "sig_lens": (
  "Signature edition: the IUGS system implemented as his original naming "
  "engine — mode or analysis in, official rock name out, with his "
  "Signature audit trail showing every decision the classification took."),
 "demo_kind": "iugs_check",
},
{
 "key": "qap-diagram", "name": "The QAP Diagram: Classifying Plutonic Rocks by Their Minerals",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "The QAP (Streckeisen) diagram is the working heart of IUGS plutonic "
  "classification: an equilateral triangle with quartz (Q) at the top, "
  "alkali feldspar (A) at bottom left, and plagioclase (P) at bottom right. "
  "A plutonic rock's normalized Q-A-P percentages plot as a single point, "
  "and the field containing the point names the rock. High quartz with "
  "balanced feldspars: granite. High quartz with plagioclase dominant: "
  "granodiorite, then tonalite as alkali feldspar vanishes. Low quartz "
  "with balanced feldspars: syenite and monzonite. Low quartz with "
  "plagioclase dominant: diorite — and when that plagioclase is "
  "calcium-rich (more than 50% anorthite), the same point becomes gabbro. "
  "The diagram encodes petrogenesis: moving down and right across it "
  "tracks magmas from felsic to mafic, from continental crust toward the "
  "mantle's compositions."),
 "how_it_works": (
  "Using the QAP diagram is a three-step measurement. First, determine the "
  "mode: point-count a thin section (or estimate carefully in hand sample) "
  "to get volume percentages of quartz, alkali feldspar, and plagioclase. "
  "Second, normalize: divide each by (Q + A + P) and multiply by 100, "
  "discarding mafic minerals for the plot. Third, locate the point: quartz "
  "above 20% puts you in the granite-granodiorite-tonalite row; the ratio "
  "P/(A+P) then decides — below 10% alkali-feldspar granite, 10-65% "
  "granite, 65-90% granodiorite, above 90% tonalite. Below 20% quartz the "
  "same feldspar ratio separates syenite, monzonite, and diorite; below 5% "
  "quartz, plagioclase composition (anorthite content above or below 50%) "
  "splits diorite from gabbro. The diagram thus turns three measured "
  "numbers into a name — and the name into a petrogenetic statement."),
 "key_points": [
  "QAP triangle: quartz (top), alkali feldspar (bottom-left), plagioclase (bottom-right)",
  "Normalize Q+A+P to 100%, then read the field: granite, granodiorite, tonalite, syenite, monzonite, diorite, gabbro",
  "Quartz ≥20%: granite family; the P/(A+P) ratio picks granite vs. granodiorite vs. tonalite",
  "Low quartz + plagioclase dominant: diorite; if plagioclase is Ca-rich (An>50): gabbro",
  "Requires measured modal mineralogy (point counting), not guesses",
  "Traversing the diagram tracks magmas from felsic continental to mafic mantle-like compositions",
 ],
 "requirements": [
  "Measured or estimated Q, A, P percentages (point-count data ideal)",
  "A printed QAP (Streckeisen) diagram for reference",
  "Understanding of normalization to 100%",
  "Knowledge of plagioclase composition (anorthite content) for the diorite/gabbro split",
 ],
 "standards": [
  "QAP field boundaries per IUGS (Le Maitre et al. 2002; Streckeisen diagrams)",
  "Anorthite 50% diorite/gabbro boundary per IUGS convention",
 ],
 "citations": [CIT_LEMAITRE, CIT_BEST],
 "sig_lens": (
  "Signature edition: the QAP triangle rebuilt as his original plutonic "
  "positioning system — any Q-A-P triple plotted, named, and placed on his "
  "Signature felsic-to-mafic traverse in one operation."),
 "demo_kind": "qap_classify",
},
{
 "key": "tas-classification", "name": "TAS Classification: Naming Volcanic Rocks by Chemistry",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Volcanic rocks are usually too fine-grained to count minerals, so the "
  "IUGS classifies them chemically with the TAS diagram — total alkalis "
  "(Na2O + K2O, vertical axis) plotted against silica (SiO2, horizontal "
  "axis), both in weight percent. The diagram's fields name the rock: "
  "low-silica, low-alkali basalts; basaltic andesites and andesites "
  "climbing in silica; dacites and rhyolites at the high-silica end; and "
  "the alkaline series — trachybasalts, trachyandesites, trachytes, and "
  "phonolites — rising in alkalis above the subalkaline trend. The TAS "
  "diagram is the chemical mirror of the QAP diagram: basalt is the "
  "volcanic equivalent of gabbro, andesite of diorite, dacite of "
  "granodiorite, rhyolite of granite. Because a single chemical analysis "
  "gives the name, TAS is the workhorse of volcanic petrology worldwide."),
 "how_it_works": (
  "TAS classification runs on two numbers from a whole-rock chemical "
  "analysis: SiO2 and Na2O + K2O, recalculated volatile-free (analyses are "
  "normalized to 100% on an anhydrous basis first). Plot the point: silica "
  "below about 45% with low alkalis is picrobasalt; 45-52% basalt; 52-57% "
  "basaltic andesite; 57-63% andesite; 63-69% dacite; above 69% rhyolite — "
  "provided alkalis stay on the subalkaline trend. Points plotting high in "
  "alkalis fall into the alkaline fields: trachybasalt, basaltic "
  "trachyandesite, trachyandesite, trachyte, and at the extreme, phonolite. "
  "The diagram also separates the two great magma series: the subalkaline "
  "(tholeiitic and calc-alkaline) trend below, the alkaline trend above. "
  "A petrologist reads a TAS plot the way a doctor reads a chart — the "
  "field gives the diagnosis, the trend gives the prognosis for the "
  "magmatic system."),
 "key_points": [
  "TAS = total alkalis (Na2O+K2O) vs. silica (SiO2), weight percent, volatile-free basis",
  "Subalkaline ladder: basalt → basaltic andesite → andesite → dacite → rhyolite",
  "Alkaline series: trachybasalt → trachyandesite → trachyte → phonolite",
  "Volcanic equivalents of plutonic rocks: basalt= gabbro, andesite=diorite, dacite=granodiorite, rhyolite=granite",
  "One chemical analysis is enough to name the rock — no thin section required",
  "The diagram separates subalkaline from alkaline magma series",
 ],
 "requirements": [
  "A whole-rock chemical analysis (XRF or equivalent) with SiO2, Na2O, K2O",
  "Understanding of volatile-free recalculation (normalize to 100% anhydrous)",
  "A printed TAS diagram with IUGS field boundaries",
  "Awareness that altered rocks can mislead — fresh samples classify best",
 ],
 "standards": [
  "TAS field boundaries per IUGS (Le Maitre et al. 2002)",
  "Volatile-free recalculation convention per IUGS recommendations",
 ],
 "citations": [CIT_LEMAITRE, CIT_PHILPOTTS],
 "sig_lens": (
  "Signature edition: TAS classification running as his original chemical "
  "naming engine — analysis in, volcanic name out, with his Signature "
  "series-tracker flagging subalkaline vs. alkaline affinity automatically."),
 "demo_kind": "tas_classify",
},
{
 "key": "magma-genesis", "name": "Magma Genesis: How Magmas Are Born",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Magmas are born when solid mantle or crust crosses its melting curve, "
  "and there are exactly three ways to make that happen. Decompression "
  "melting: hot mantle rises beneath mid-ocean ridges and hotspots, "
  "pressure drops, and the solidus falls below the mantle's temperature — "
  "this makes the basalts that pave the ocean floors. Flux melting: water "
  "released from a subducting slab infiltrates the overlying mantle wedge, "
  "dramatically lowering its melting point — this makes the andesites and "
  "dacites of volcanic arcs. Heat-transfer melting: rising basaltic magma "
  "bakes adjacent crust past its (lower) solidus, generating felsic melts — "
  "this contributes to continental granites. Each mechanism has a tectonic "
  "address, a characteristic magma chemistry, and a volcanic expression, so "
  "a rock's chemistry points back to the melting process that made it."),
 "how_it_works": (
  "Melting happens when temperature exceeds the solidus — the temperature "
  "where melting begins at a given pressure and composition. Decompression "
  "melting works because the solidus rises steeply with pressure: a parcel "
  "of mantle rising adiabatically (cooling only slightly) crosses its "
  "solidus from below, typically beginning to melt around 60-80 km depth "
  "beneath ridges. Flux melting works because water breaks silicate "
  "polymerization: even a few percent water can drop the peridotite solidus "
  "by hundreds of degrees, so the hydrated mantle wedge above a slab melts "
  "where dry mantle would not. Heat-transfer melting works by contrast: "
  "basaltic magma at ~1200°C intrudes crust whose solidus may be only "
  "~700°C (especially if water is present), and the crust melts. "
  "Petrologists diagnose the mechanism from chemistry and setting: "
  "ridge basalts (decompression), water-rich arc andesites (flux), "
  "crustal granites with inherited zircons (heat transfer)."),
 "key_points": [
  "Three melting mechanisms: decompression, flux (water-added), heat transfer",
  "Decompression melting: rising mantle under ridges and hotspots → ocean-floor basalts",
  "Flux melting: slab water lowers the mantle wedge solidus → arc andesites and dacites",
  "Heat-transfer melting: hot basalt bakes fusible crust → continental granites",
  "The solidus (melting-start temperature) rises with pressure and falls with water content",
  "Chemistry + tectonic setting diagnose which mechanism made a magma",
 ],
 "requirements": [
  "Concept of the solidus and how pressure and water shift it",
  "Basic plate-tectonic settings: ridges, subduction zones, hotspots, continents",
  "Understanding that the mantle is solid rock that can melt, not a magma ocean",
  "Familiarity with basalt/andesite/granite as the three mechanism signatures",
 ],
 "standards": [
  "Melting mechanisms per standard igneous texts (Best 2002; Winter 2013; Philpotts & Ague 2009)",
  "Solidus systematics per experimental petrology literature",
 ],
 "citations": [CIT_BEST, CIT_WINTER],
 "sig_lens": (
  "Signature edition: magma genesis modeled as his original three-trigger "
  "ignition system — decompression, flux, or heat transfer, each with its "
  "tectonic address and chemical signature in his Signature melting atlas."),
 "demo_kind": "melting_mechanisms",
},
{
 "key": "partial-melting-fractionation", "name": "Partial Melting and Fractional Crystallization: The Twin Engines",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Two complementary processes generate Earth's chemical diversity. "
  "Partial melting: when mantle or crust melts, it melts incompletely — "
  "typically 1-20% — and the first melt is always more silica- and "
  "alkali-rich than its source, because the most fusible minerals melt "
  "first. Elements that prefer the melt are called incompatible (they "
  "concentrate enormously in small melt fractions); elements that prefer "
  "the residual crystals are compatible (they stay behind). Fractional "
  "crystallization is the mirror: as magma cools, early crystals are "
  "removed (by settling or separation), and the remaining liquid evolves — "
  "incompatible elements enrich further while compatible elements deplete. "
  "Batch melting follows C_l = C_0 / (D + F(1−D)) and Rayleigh "
  "fractionation follows C_l = C_0 · F^(D−1), where D is the bulk "
  "partition coefficient and F the melt fraction remaining."),
 "how_it_works": (
  "Both engines run on partitioning — each element's preference for melt "
  "versus crystals, quantified by the partition coefficient D "
  "(concentration in solid / concentration in melt). In partial melting, a "
  "tiny melt fraction (F = 0.05) of mantle with an incompatible element "
  "(D = 0.01) enriches that element roughly 15-fold in the melt — which is "
  "why ocean basalts carry far more rare-earth elements than the mantle "
  "they came from. In fractional crystallization, removing olivine and "
  "pyroxene (which take Mg, Fe, Ni, Cr) leaves the residual liquid enriched "
  "in silica, alkalis, and incompatible elements — the Rayleigh equation "
  "quantifies it: at F = 0.5 with D = 0.01, the melt holds roughly twice "
  "the original incompatible-element concentration. Petrologists invert "
  "these equations: measured trace-element patterns in a lava reveal the "
  "melt fraction that made it and how much crystallization it suffered — "
  "reading process from chemistry."),
 "key_points": [
  "Partial melting (1-20%) makes melts more felsic than their source; first melts take the fusible components",
  "Incompatible elements (low D) enrich in melts; compatible elements (high D) stay in the residue",
  "Batch melting: C_l = C_0 / (D + F(1−D)); Rayleigh fractionation: C_l = C_0 · F^(D−1)",
  "Small melt fractions enormously enrich incompatible elements (ore deposits start here)",
  "Fractional crystallization removes early crystals, driving residual melt toward felsic compositions",
  "Trace-element patterns in lavas invert to reveal melt fraction and crystallization history",
 ],
 "requirements": [
  "Algebra comfort: working with the batch-melting and Rayleigh equations",
  "Concept of the partition coefficient D (solid/melt concentration ratio)",
  "Understanding of incompatible vs. compatible elements",
  "Bowen's reaction series (which minerals crystallize first, hence fractionate first)",
 ],
 "standards": [
  "Batch melting and Rayleigh equations per standard igneous geochemistry (Winter 2013; Best 2002)",
  "Partition coefficient conventions per geochemical literature",
 ],
 "citations": [CIT_WINTER, CIT_BEST],
 "sig_lens": (
  "Signature edition: the twin engines running as his original "
  "concentration machinery — batch melting and Rayleigh fractionation "
  "coded as his Signature calculators that turn any trace-element pattern "
  "into a melt fraction and crystallization history."),
 "demo_kind": "batch_melting",
},
{
 "key": "magma-differentiation", "name": "Magma Differentiation: How One Magma Makes Many Rocks",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "A single parent magma can produce an entire family of rocks — basalt, "
  "andesite, dacite, rhyolite — through differentiation. Fractional "
  "crystallization is the main engine: early mafic crystals (olivine, "
  "pyroxene, Ca-plagioclase) settle out or are otherwise removed, and the "
  "residual liquid marches toward felsic compositions, exactly as Bowen's "
  "series predicts. Magma mixing blends two magmas (often mafic and felsic) "
  "into hybrids with telltale disequilibrium textures — resorbed "
  "phenocrysts, reverse zoning, mafic enclaves in granite. Assimilation "
  "melts and incorporates wall rock, contaminating the magma with crustal "
  "chemistry (detectable in isotopes). Liquid immiscibility — one melt "
  "splitting into two, like oil and water — is rare but makes some "
  "carbonatites and sulfide ores. Real magma chambers usually combine "
  "several: the AFC model (assimilation-fractional crystallization) "
  "describes chambers that crystallize while digesting their walls."),
 "how_it_works": (
  "Differentiation works by separating what crystallizes from what remains "
  "liquid. In a cooling chamber, dense olivine and pyroxene sink "
  "(gravitational settling) or growing crystals are left behind as melt is "
  "squeezed out (filter pressing, flow segregation) — either way the "
  "liquid loses Mg, Fe, Ca and gains Si, Na, K relatively. Thermodynamic "
  "models (MELTS and its successors) compute the liquid line of descent: "
  "the exact composition path a cooling magma follows. Mixing is diagnosed "
  "by straight lines on element-element plots and by disequilibrium "
  "textures; assimilation by isotopic shifts toward crustal values "
  "(elevated strontium-87/86, lowered neodymium-143/144) that "
  "fractionation alone cannot produce. Petrologists test differentiation "
  "hypotheses quantitatively: can the observed daughter compositions be "
  "reached from the proposed parent by removing the observed phenocryst "
  "phases? Mass-balance and trace-element models give a yes-or-no answer."),
 "key_points": [
  "One parent magma → many daughter rocks via differentiation",
  "Fractional crystallization (main engine): remove early mafic crystals, residual melt goes felsic",
  "Magma mixing: blended magmas, diagnosed by disequilibrium textures and linear element trends",
  "Assimilation: wall-rock contamination, diagnosed by crustal isotopic signatures",
  "AFC (assimilation + fractional crystallization) models real chambers doing both at once",
  "Differentiation hypotheses are testable by mass-balance and trace-element modeling",
 ],
 "requirements": [
  "Bowen's reaction series (which phases crystallize and can be removed)",
  "The batch/Rayleigh equations from the partial-melting record",
  "Basic isotope literacy: Sr-Nd systems as contamination tracers",
  "Concept of a liquid line of descent",
 ],
 "standards": [
  "Differentiation processes per standard igneous texts (Best 2002; Winter 2013)",
  "AFC formulation per DePaolo (1981) as used in petrology literature",
 ],
 "citations": [CIT_BEST, CIT_WINTER],
 "sig_lens": (
  "Signature edition: differentiation tracked as his original lineage "
  "engine — every daughter rock traced to its parent magma, with his "
  "Signature tests distinguishing fractionation from mixing from "
  "assimilation on the evidence."),
 "demo_kind": "rayleigh",
},
{
 "key": "volcanic-textures", "name": "Volcanic Textures: Reading Eruptions in Stone",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Volcanic rocks freeze eruption dynamics into texture. Vesicular texture "
  "— frozen bubble holes — records volatiles exsolving as magma depressurized; "
  "pumice is so vesicular it floats, scoria is its darker basaltic cousin, "
  "and amygdaloidal texture forms when later minerals fill the vesicles. "
  "Flow banding — streaky aligned bands in rhyolite and obsidian — records "
  "viscous lava stretching as it flowed. Pillow lavas — stacked, "
  "radially-cracked tubes — record lava erupting underwater, each pillow a "
  "quenched skin around a molten core. Pyroclastic textures record "
  "explosions: tuff is consolidated ash, lapilli tuff holds pea-sized "
  "fragments, volcanic breccia holds blocks, and welded tuff (ignimbrite) "
  "records a pyroclastic flow so hot its glass shards fused back together. "
  "Columnar jointing — the hexagonal pillars of places like the Giant's "
  "Causeway — records slow, even contraction of a thick cooling lava flow."),
 "how_it_works": (
  "Each volcanic texture is read as a frozen process. Vesicle size and "
  "abundance quantify degassing: many small vesicles mean rapid "
  "decompression of volatile-rich magma; stretched vesicles mean the "
  "bubble-bearing melt was still flowing when it froze. Flow banding's "
  "stretched bands map shear in the moving lava — tight isoclinal folds in "
  "banding record extreme viscosity. Pillow shapes record water depth and "
  "eruption rate: the quenched rind, radial cooling cracks, and stacked "
  "geometry are unmistakable subaqueous signatures. In pyroclastic rocks, "
  "fragment types diagnose the explosion: juvenile (fresh magma), "
  "cognate (earlier solidified magma), and accidental (shattered wall "
  "rock) clasts in one deposit record vent-widening during eruption. "
  "Welding intensity in ignimbrites maps emplacement temperature — densely "
  "welded bases were hottest. Together these textures let a petrologist "
  "reconstruct an eruption never witnessed."),
 "key_points": [
  "Vesicular/pumice/scoria: frozen gas bubbles record degassing; amygdales are mineral-filled vesicles",
  "Flow banding: stretched bands record viscous lava flow and shear",
  "Pillow lavas: quenched tubes record subaqueous eruption",
  "Tuff, lapilli tuff, volcanic breccia: consolidated explosion fragments by size",
  "Welded tuff (ignimbrite): hot pyroclastic flow whose shards fused back together",
  "Columnar jointing: contraction columns record slow even cooling of thick flows",
 ],
 "requirements": [
  "Samples or images: pumice, scoria, obsidian with flow banding, tuff",
  "Understanding of volatile exsolution from the magma record",
  "Vocabulary: vesicle, amygdale, juvenile/cognate/accidental clasts, welding",
  "Familiarity with explosive vs. effusive eruption styles",
 ],
 "standards": [
  "Pyroclastic terminology per IUGS recommendations (Le Maitre et al. 2002)",
  "Volcanic textural terms per standard volcanology/petrology texts",
 ],
 "citations": [CIT_LEMAITRE, CIT_PHILPOTTS],
 "sig_lens": (
  "Signature edition: volcanic textures filed as his original eruption "
  "forensics kit — every bubble, band, pillow, and shard matched to the "
  "eruption dynamics that froze it, in his Signature reconstruction "
  "sequence."),
 "demo_kind": "vesicle_porosity",
},
{
 "key": "sedimentary-provenance", "name": "Sedimentary Provenance: Reading the Source Rocks in Sand",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Every sandstone is a letter from its source rocks, and provenance "
  "analysis reads it. The workhorse is the QFL ternary diagram — quartz "
  "(Q), feldspar (F), and lithic fragments (L) normalized to 100% — "
  "pioneered for tectonic interpretation by Dickinson and Suczek (1979). "
  "Quartz-rich sands plot near the Q corner: the signature of stable "
  "continental interiors (cratons), where long transport destroys "
  "everything but quartz. Feldspar- and lithic-rich sands plot toward F "
  "and L: the signature of magmatic arcs, where young volcanoes shed fresh, "
  "unstable debris. Intermediate compositions mark recycled orogens — "
  "mountain belts shedding their own sedimentary cover. Heavy minerals "
  "(zircon, tourmaline, rutile) add a second read: zircon ages fingerprint "
  "the exact source terranes. Provenance turns a beach sand into a "
  "tectonic address."),
 "how_it_works": (
  "Provenance analysis works by point-counting 300-500 framework grains in "
  "thin section, classifying each as quartz (monocrystalline or "
  "polycrystalline), feldspar (K-feldspar or plagioclase), or lithic "
  "fragment (volcanic, sedimentary, or metamorphic rock chips). The "
  "percentages normalize to Q + F + L = 100% and plot on the ternary "
  "diagram, whose empirical fields — continental block, recycled orogen, "
  "magmatic arc (Dickinson & Suczek 1979) — were calibrated on modern sands "
  "of known tectonic setting. Quartz enrichment tracks weathering "
  "intensity and transport distance (maturity); feldspar preservation "
  "tracks rapid erosion and arid or cold climates; lithic types name the "
  "source lithology directly — volcanic lithics mean a volcanic source, "
  "no interpretation needed. Detrital zircon geochronology extends the "
  "method: each zircon's U-Pb age is a timestamp from a specific source "
  "event, and the age spectrum is the source region's barcode."),
 "key_points": [
  "QFL ternary (quartz-feldspar-lithics) is the master provenance diagram (Dickinson & Suczek 1979)",
  "Q-rich: stable continental interiors; F/L-rich: magmatic arcs; intermediate: recycled orogens",
  "Point-count 300-500 grains per thin section for statistical validity",
  "Quartz = maturity and long transport; feldspar = rapid erosion; lithic type names the source lithology",
  "Heavy minerals (zircon, tourmaline, rutile) add a durability-weighted second read",
  "Detrital zircon U-Pb ages barcode the exact source terranes",
 ],
 "requirements": [
  "Thin-section point-counting skill (or published QFL data to practice on)",
  "Ability to distinguish quartz, feldspar, and lithic fragments under the microscope",
  "The Dickinson QFL diagram with tectonic fields",
  "Understanding that diagenesis can dissolve feldspars — count carefully",
 ],
 "standards": [
  "QFL fields per Dickinson & Suczek (1979)",
  "Gazzi-Dickinson point-counting method per sedimentary petrology convention",
 ],
 "citations": [CIT_DICKINSON, CIT_BOGGS],
 "sig_lens": (
  "Signature edition: provenance run as his original source-tracing bureau "
  "— any sandstone's QFL count converted to a tectonic address, with his "
  "Signature confidence rating on each assignment."),
 "demo_kind": "qfl_provenance",
},
{
 "key": "sedimentary-structures", "name": "Sedimentary Structures: Reading Ancient Environments",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Sedimentary structures are the depositional environment caught in the "
  "act. Bedding — layering itself — records episodic deposition. "
  "Cross-bedding (inclined layers within a bed) records migrating dunes: "
  "large-scale trough cross-beds mean river channels or desert dunes, and "
  "the dip direction is the ancient current direction (paleocurrent). "
  "Graded bedding (coarse at the base, fine at the top) records a single "
  "waning flow — the classic signature of turbidity currents in deep water. "
  "Ripple marks record waves (symmetric) or currents (asymmetric) at the "
  "sediment surface. Mud cracks record subaerial drying; sole marks "
  "(flutes, grooves) on bed bases record turbulent scour. Trace fossils — "
  "burrows and tracks — record organisms' behavior. Together these "
  "structures let a petrologist stand in an outcrop and see the river, "
  "beach, or deep-sea fan that was there millions of years ago."),
 "how_it_works": (
  "Reading structures works by matching geometry to process physics. "
  "Cross-bed foresets dip down-current at the angle of repose (~30°), so "
  "measuring dozens of foreset orientations and plotting them on a rose "
  "diagram reveals the paleoflow — unimodal for rivers, bimodal for tidal "
  "flats. Graded beds are read base-to-top as a decelerating flow's "
  "time series; stacked graded beds (Bouma sequences: massive sand → "
  "parallel lamination → ripple lamination → mud) diagnose turbidity "
  "currents specifically. Ripple symmetry separates waves from currents: "
  "oscillating water builds symmetric ripples with a ripple index "
  "(wavelength/height) around 6-7, while unidirectional currents build "
  "asymmetric ripples with higher indices. Mud cracks demand drying — "
  "proof of exposure above water. The assemblage, not any single "
  "structure, names the environment: cross-bedded sandstones with mud "
  "cracks spell river floodplain; graded Bouma sequences spell deep-sea fan."),
 "key_points": [
  "Cross-bedding records migrating dunes; foreset dip direction = paleocurrent",
  "Graded bedding (coarse→fine upward) records waning flows; Bouma sequences diagnose turbidity currents",
  "Symmetric ripples = waves; asymmetric ripples = currents (ripple index distinguishes them)",
  "Mud cracks prove subaerial drying; sole marks record turbulent scour on bed bases",
  "Trace fossils (burrows, tracks) record organism behavior, not bodies",
  "Environment is diagnosed from the assemblage of structures, never one alone",
 ],
 "requirements": [
  "Outcrop or core photos showing bedding, cross-bedding, and ripples",
  "A compass-clinometer (or the concept) for measuring foreset orientations",
  "Understanding of the Bouma sequence (Ta-Te divisions)",
  "Vocabulary: foreset, paleocurrent, graded bedding, sole mark, trace fossil",
 ],
 "standards": [
  "Sedimentary structure terminology per standard texts (Tucker 2001; Boggs 2009)",
  "Bouma sequence per Bouma (1962) as used in turbidite literature",
 ],
 "citations": [CIT_TUCKER, CIT_BOGGS],
 "sig_lens": (
  "Signature edition: sedimentary structures compiled as his original "
  "environment decoder ring — every bedform, crack, and burrow keyed to "
  "the water, wind, and organisms that made it, in his Signature field "
  "guide."),
 "demo_kind": "bedform",
},
{
 "key": "diagenesis", "name": "Diagenesis: From Loose Sediment to Solid Rock",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Diagenesis is everything that happens to sediment after deposition and "
  "before metamorphism — the quiet transformation of loose grains into "
  "rock. Compaction squeezes grains together under accumulating overburden: "
  "a freshly deposited mud may be 70-80% water, but at 2-3 km depth its "
  "porosity has collapsed toward 10-20%, following roughly exponential "
  "decay with depth. Cementation fills the remaining pores: groundwater "
  "carrying dissolved silica, calcite, or iron oxides precipitates "
  "minerals between grains, gluing them into sandstone. Recrystallization "
  "rebuilds unstable minerals — aragonite shells invert to calcite, "
  "smectite clays convert to illite with burial temperature. Dissolution "
  "can do the opposite, leaching grains and cements to create secondary "
  "porosity — the pore space that holds much of the world's oil and "
  "groundwater. Diagenesis decides whether a sand becomes a reservoir or "
  "a seal."),
 "how_it_works": (
  "Diagenesis works through burial-driven chemistry and physics. "
  "Mechanical compaction rearranges grains into tighter packing and then "
  "deforms them (pressure solution at grain contacts dissolves quartz "
  "where grains press hardest, reprecipitating it nearby as overgrowths). "
  "Chemical compaction and cementation are controlled by pore-water "
  "chemistry, which evolves with depth and temperature: shallow meteoric "
  "waters precipitate calcite cements, deeper hotter brines precipitate "
  "quartz overgrowths (typically above ~80°C). Petrologists read the "
  "paragenetic sequence — the order cements and alterations formed — from "
  "cross-cutting relationships in thin section: which cement coats which "
  "grain, which fracture cuts which cement. Porosity-depth curves "
  "(phi = phi_0 · e^(−cz)) quantify the burial history. The economic "
  "payoff: predicting where primary porosity survived and where secondary "
  "porosity was created is how reservoir quality is mapped before drilling."),
 "key_points": [
  "Diagenesis: post-depositional, pre-metamorphic transformation of sediment to rock",
  "Compaction: porosity decays roughly exponentially with burial depth (70-80% → 10-20%)",
  "Cementation: silica, calcite, or iron-oxide precipitation glues grains (quartz overgrowths above ~80°C)",
  "Recrystallization: aragonite→calcite, smectite→illite with burial",
  "Dissolution creates secondary porosity — the space holding oil and groundwater",
  "Paragenetic sequence (cement order from cross-cutting relations) reconstructs the burial history",
 ],
 "requirements": [
  "Thin-section images showing cement types and grain contacts",
  "Basic chemistry: dissolution and precipitation, pressure solution",
  "Algebra comfort for the porosity-depth exponential",
  "Understanding that diagenesis stops where metamorphism begins (~200°C)",
 ],
 "standards": [
  "Diagenetic process definitions per standard texts (Tucker 2001; Boggs 2009)",
  "Paragenetic-sequence reading conventions per sedimentary petrology practice",
 ],
 "citations": [CIT_TUCKER, CIT_BOGGS],
 "sig_lens": (
  "Signature edition: diagenesis tracked as his original burial "
  "transformation log — every compaction, cement, and dissolution event "
  "sequenced in his Signature paragenetic ledger from seafloor to "
  "reservoir."),
 "demo_kind": "compaction",
},
{
 "key": "carbonate-petrology", "name": "Carbonate Petrology: Limestones, Dolostones, and Reefs",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Carbonate rocks — limestones and dolostones — are the chemical and "
  "biological sediments of warm shallow seas, and they play by different "
  "rules than sandstones. Their grains are allochems (Folk 1974): ooids "
  "(concentrically coated spheres formed in agitated shallows), peloids "
  "(fecal and micritized pellets), bioclasts (shell and skeleton "
  "fragments), and intraclasts (ripped-up chips of nearby sediment), all "
  "set in micrite (lime mud) or sparry calcite cement. The Dunham (1962) "
  "classification names the rock by depositional texture: mudstone "
  "(mud-supported, <10% grains), wackestone (mud-supported, >10% grains), "
  "packstone (grain-supported with mud), grainstone (grain-supported, no "
  "mud), boundstone (organisms bound it during deposition — reefs), and "
  "crystalline carbonate (recrystallized beyond recognition). Dolostones "
  "form when magnesium-rich brines replace calcite with dolomite, often "
  "creating the porosity that makes carbonate oil reservoirs."),
 "how_it_works": (
  "Carbonate petrology works by separating depositional texture from "
  "later diagenesis. First, identify the allochems: ooids mean agitated "
  "shallow water (they need constant rolling to coat evenly); diverse "
  "bioclasts mean normal-marine conditions; micrite envelopes on grains "
  "mean microbial micritization in quiet water. Then apply Dunham: is the "
  "rock mud-supported or grain-supported? That single call separates "
  "low-energy (wackestone) from high-energy (grainstone) deposition — the "
  "energy map of an ancient carbonate platform. Then strip the diagenetic "
  "overprint: neomorphism recrystallizes micrite to spar, dolomitization "
  "replaces calcite (often fabric-selective, preserving ghosts of the "
  "original), and dissolution creates vuggy and moldic porosity. Because "
  "carbonates are so diagenetically reactive, the petrologist's hardest "
  "job is seeing through the alteration to the depositional rock — "
  "staining (Alizarin Red-S) distinguishes calcite from dolomite, and "
  "cathodoluminescence reveals cement generations."),
 "key_points": [
  "Allochems (Folk): ooids, peloids, bioclasts, intraclasts in micrite mud or sparry cement",
  "Dunham (1962) by depositional texture: mudstone → wackestone → packstone → grainstone → boundstone",
  "Mud-supported vs. grain-supported is the master energy call (quiet vs. agitated water)",
  "Boundstones are organically bound during deposition — the reef facies",
  "Dolomitization (Mg-brine replacement of calcite) often creates reservoir porosity",
  "Carbonates are diagenetically reactive: the petrologist must see through alteration to deposition",
 ],
 "requirements": [
  "Thin-section or hand-sample views of oolitic and fossiliferous limestones",
  "The Dunham classification chart as a reference",
  "Understanding of micrite vs. sparry calcite",
  "Awareness that dolomite vs. calcite is testable (acid reaction, staining)",
 ],
 "standards": [
  "Dunham classification (Dunham 1962)",
  "Allochem terminology per Folk (1974)",
 ],
 "citations": [CIT_DUNHAM, CIT_FOLK, CIT_TUCKER],
 "sig_lens": (
  "Signature edition: carbonate platforms decoded as his original "
  "shallow-sea mapping system — allochems, Dunham textures, and "
  "diagenetic overprints layered in his Signature platform model from "
  "reef to lagoon."),
 "demo_kind": "dunham",
},
{
 "key": "metamorphic-grade", "name": "Metamorphic Grade and Index Minerals: Reading Temperature in Stone",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Metamorphic grade — the intensity of metamorphism, essentially "
  "temperature — is read from index minerals: minerals that appear at "
  "specific grades in rocks of suitable composition. In aluminum-rich "
  "metapelites (metamorphosed shales), George Barrow mapped the classic "
  "sequence in the Scottish Highlands: chlorite zone (lowest grade) → "
  "biotite → garnet → staurolite → kyanite → sillimanite (highest grade). "
  "Each index mineral's first appearance (its isograd) marks a reaction "
  "crossed: chlorite + muscovite react to make biotite; garnet appears "
  "via chlorite breakdown; staurolite, kyanite, and sillimanite — all "
  "aluminosilicates — mark successively hotter conditions, with kyanite "
  "vs. sillimanite also recording pressure (kyanite is the high-pressure "
  "polymorph). Mapping isograds across a terrain draws the ancient "
  "geothermal gradient in map view — the mountain belt's thermal anatomy."),
 "how_it_works": (
  "Index minerals work because each is stable only above (or within) a "
  "temperature window for a given bulk composition. The petrologist maps "
  "a region's metapelites, recording the highest-grade index mineral in "
  "each outcrop; lines connecting first appearances of the same mineral "
  "are isograds — lines of equal metamorphic grade. The sequence only "
  "works in the right chemistry: a quartzite or marble will never grow "
  "staurolite no matter how hot it gets, so grade is always read in "
  "comparable protoliths (metapelites are the standard). The "
  "kyanite-sillimanite transition doubles as a barometer: kyanite stable "
  "at higher pressure, sillimanite at higher temperature/lower pressure, "
  "with andalusite the low-pressure third polymorph. Modern work "
  "calibrates each isograd reaction experimentally, turning Barrow's "
  "relative zones into absolute temperatures — the chlorite-out/biotite-in "
  "reaction near ~400°C, sillimanite-in near ~600-650°C at moderate "
  "pressure."),
 "key_points": [
  "Index minerals mark metamorphic grade: chlorite → biotite → garnet → staurolite → kyanite → sillimanite (Barrovian sequence)",
  "Each first appearance (isograd) is a mineral reaction crossed at a specific temperature",
  "Isograd maps draw the ancient geothermal gradient across a mountain belt",
  "Sequence requires the right chemistry — read grade in metapelites (Al-rich shales)",
  "Kyanite vs. sillimanite vs. andalusite: the aluminosilicate polymorphs also record pressure",
  "Calibrated reactions turn relative zones into absolute temperatures",
 ],
 "requirements": [
  "Hand samples or images: garnet schist, staurolite schist, kyanite/sillimanite gneiss",
  "Understanding of isograds as map lines of equal grade",
  "The aluminosilicate (kyanite-sillimanite-andalusite) phase diagram",
  "Awareness that bulk composition gates which index minerals can appear",
 ],
 "standards": [
  "Barrovian zones per Barrow's Highland mapping as codified in standard texts (Yardley & Warren 2021)",
  "Aluminosilicate phase relations per experimental petrology",
 ],
 "citations": [CIT_YARDLEY, CIT_MIYASHIRO],
 "sig_lens": (
  "Signature edition: index minerals deployed as his original "
  "paleothermometer array — the Barrovian sequence read as a calibrated "
  "temperature ladder, with his Signature isograd maps drawing ancient "
  "heat flow in plan view."),
 "demo_kind": "barrovian_order",
},
{
 "key": "metamorphic-facies", "name": "Metamorphic Facies: Pressure-Temperature Fingerprints",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "A metamorphic facies is a set of mineral assemblages that records a "
  "particular range of pressure-temperature conditions, regardless of "
  "protolith — the concept introduced by Pentti Eskola (1915). The great "
  "facies: zeolite and prehnite-pumpellyite (very low grade); greenschist "
  "(chlorite + albite + epidote — the green rocks of low-grade belts); "
  "amphibolite (hornblende + plagioclase — the workhorse of mountain "
  "roots); granulite (pyroxene-bearing, water-poor — hot deep crust); "
  "blueschist (glaucophane-bearing — cold, high-pressure subduction "
  "zones); and eclogite (garnet + omphacite — very high pressure, the "
  "subducted oceanic crust). Facies series map to tectonic settings: "
  "high-P/low-T (blueschist-eclogite) means subduction; medium-P/medium-T "
  "(greenschist-amphibolite) means collisional mountain belts; low-P/high-T "
  "(hornfels-granulite) means contact aureoles and rifts. A facies name is "
  "a P-T address."),
 "how_it_works": (
  "Facies assignment works by matching the observed assemblage to the "
  "diagnostic minerals of each facies, then plotting on the P-T diagram. "
  "Glaucophane (blue amphibole) + lawsonite can only mean blueschist "
  "facies — high pressure, low temperature, hence a subduction zone. "
  "Omphacite (sodic pyroxene) + garnet with no plagioclase means eclogite "
  "— pressures of subducted slabs. Hornblende + plagioclase (without "
  "pyroxene) means amphibolite facies — the classic mountain-belt root. "
  "Orthopyroxene appearing in mafic rocks means granulite — hot, dry, "
  "deep crust. Because the same P-T conditions produce different "
  "assemblages in different protoliths (a basalt and a shale at "
  "amphibolite facies look nothing alike), petrologists memorize the "
  "mafic-rock assemblage as the facies reference and calibrate the rest "
  "against it. Facies series — the sequence of facies across a terrain — "
  "then diagnose the tectonic setting that cooked the belt."),
 "key_points": [
  "Facies = mineral assemblages recording a P-T range, independent of protolith (Eskola 1915)",
  "Greenschist (low grade) → amphibolite (medium) → granulite (hot deep); blueschist → eclogite (subduction P-T)",
  "Diagnostic minerals: glaucophane = blueschist, omphacite+garnet = eclogite, orthopyroxene = granulite",
  "Facies series diagnose tectonics: high-P/low-T = subduction, medium-P/T = collision, low-P/high-T = rifts/contacts",
  "Mafic-rock assemblages are the facies reference; other protoliths are calibrated against them",
  "A facies name is a pressure-temperature address",
 ],
 "requirements": [
  "The metamorphic facies P-T diagram as a wall reference",
  "Familiarity with the diagnostic minerals (glaucophane, omphacite, orthopyroxene)",
  "Understanding that one facies looks different in basalt vs. shale protoliths",
  "Index-mineral/grade concepts from the previous record",
 ],
 "standards": [
  "Facies definitions per Eskola (1915) as codified in modern texts (Yardley & Warren 2021; Spear 1993)",
  "P-T facies boundaries per experimental calibrations",
 ],
 "citations": [CIT_ESKOLA, CIT_YARDLEY, CIT_SPEAR],
 "sig_lens": (
  "Signature edition: metamorphic facies run as his original P-T "
  "addressing system — any assemblage resolved to its facies and "
  "tectonic setting, with his Signature facies-series maps diagnosing "
  "subduction, collision, or rift at a glance."),
 "demo_kind": "facies_lookup",
},
{
 "key": "metamorphic-textures", "name": "Metamorphic Textures: Foliation, Porphyroblasts, and Deformation",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Metamorphic texture records directed pressure and recrystallization. "
  "Foliation — the planar alignment of minerals — intensifies with grade: "
  "slaty cleavage (microscopic mica alignment splitting slate into "
  "roofing sheets) → schistosity (visible aligned micas defining schist) → "
  "gneissic banding (segregated light/dark mineral bands in gneiss). "
  "Porphyroblasts — large new crystals like garnet or staurolite grown "
  "during metamorphism — overgrow the foliation and timestamp "
  "deformation: pre-tectonic porphyroblasts are wrapped by foliation, "
  "syn-tectonic ones spiral it into snowball garnets, post-tectonic ones "
  "overgrow it undeformed. Granoblastic texture (equant interlocking "
  "grains, no foliation — as in marble and quartzite) records "
  "recrystallization without directed pressure. Mylonites — "
  "fine-grained, streaky fault rocks — record extreme shearing. Reading "
  "these textures reconstructs the deformation history the minerals alone "
  "cannot tell."),
 "how_it_works": (
  "Texture reading starts with the foliation ladder: can the rock be split "
  "along planes? Microscopic alignment only (slaty cleavage) means low "
  "grade and weak deformation; visible mica alignment (schistosity) means "
  "medium grade; compositional banding (gneissic) means high grade with "
  "mineral segregation by diffusion. Next, the porphyroblast test: trace "
  "the foliation (or inclusion trails) through a garnet — trails continuous "
  "with the matrix foliation but undeformed inside mean post-tectonic "
  "growth; spiraled trails mean the garnet grew while the rock sheared "
  "(syn-tectonic); foliation wrapping around the crystal means it predates "
  "deformation. Pressure shadows (quartz/calcite beards on rigid grains) "
  "point along the stretching direction. In thin section, undulose "
  "extinction and subgrain formation in quartz record dislocation creep — "
  "the crystal-plastic deformation of deep fault zones. Texture plus "
  "assemblage together give the full P-T-deformation-time story."),
 "key_points": [
  "Foliation intensifies with grade: slaty cleavage → schistosity → gneissic banding",
  "Porphyroblasts timestamp deformation: pre/syn/post-tectonic from foliation relationships",
  "Snowball garnets (spiraled inclusion trails) record syn-tectonic growth during shearing",
  "Granoblastic texture (marble, quartzite) = recrystallization without directed pressure",
  "Mylonites record extreme ductile shearing in fault zones",
  "Pressure shadows and undulose extinction map stretching directions and creep mechanisms",
 ],
 "requirements": [
  "Samples or images: slate, schist, gneiss, garnet schist with porphyroblasts",
  "A hand lens to see schistosity vs. gneissic banding",
  "Concept of inclusion trails continuing matrix foliation",
  "Vocabulary: porphyroblast, foliation, lineation, mylonite, pressure shadow",
 ],
 "standards": [
  "Metamorphic textural terminology per standard texts (Yardley & Warren 2021; Winter 2013)",
  "Porphyroblast timing criteria per microstructural geology conventions",
 ],
 "citations": [CIT_YARDLEY, CIT_WINTER],
 "sig_lens": (
  "Signature edition: metamorphic textures read as his original "
  "deformation time-stamper — foliation graded, porphyroblasts dated "
  "against shearing, with his Signature timeline assembling the rock's "
  "structural history."),
 "demo_kind": "foliation_grade",
},
# ------------------------------------------------------------------ ADVANCED
{
 "key": "phase-equilibria-binary", "name": "Phase Equilibria: Reading Binary Phase Diagrams",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Phase diagrams are petrology's maps of stability: they show which "
  "minerals (phases) coexist at each temperature and composition. The "
  "binary eutectic diagram — temperature vs. composition for a two-"
  "component system like diopside-anorthite — is the prototype: the "
  "liquidus curve marks where crystallization begins on cooling, the "
  "solidus where melting ends, and the eutectic point is the lowest "
  "temperature at which liquid exists, where two solids crystallize "
  "simultaneously. The Gibbs phase rule, F = C − P + 2, counts the "
  "degrees of freedom: at the eutectic (two components, three phases — "
  "two solids plus liquid), F = 1, so at fixed pressure the eutectic "
  "temperature is invariant. Binary solid-solution diagrams (like "
  "plagioclase Ab-An) show the loop between liquidus and solidus that "
  "drives continuous-reaction zoning. Peritectic diagrams show "
  "incongruent melting — olivine melting to pyroxene plus liquid, the "
  "diagram form of Bowen's discontinuous reactions. Mastering these "
  "diagrams is mastering the thermodynamics of crystallization."),
 "how_it_works": (
  "Reading a binary diagram is a cooling-path exercise. Start with a bulk "
  "composition on the composition axis at high temperature (all liquid). "
  "Cool vertically: the first solid appears where the path hits the "
  "liquidus — its composition read from the solidus at that temperature. "
  "Continued cooling moves the liquid composition along the liquidus "
  "toward the eutectic while the solid's composition follows the solidus. "
  "At the eutectic temperature, the remaining liquid crystallizes "
  "isothermally as an intergrowth of both solids — the graphic texture of "
  "granophyres. The lever rule (next record) quantifies the solid/liquid "
  "proportions at any point. For solid-solution systems, the loop's width "
  "measures how far liquid and solid compositions diverge — wide loop, "
  "strong zoning. Petrologists use real multi-component diagrams "
  "(forsterite-diopside-silica and beyond) the same way, tracking "
  "crystallization paths across cotectics where two or three phases "
  "co-crystallize — the diagram is the thermodynamic script that "
  "Bowen's experiments performed live."),
 "key_points": [
  "Phase diagrams map stable mineral assemblages across temperature and composition",
  "Liquidus: crystallization starts; solidus: melting ends; eutectic: lowest-T liquid, simultaneous two-solid crystallization",
  "Gibbs phase rule F = C − P + 2 counts degrees of freedom (invariant eutectic at fixed pressure)",
  "Solid-solution loops (plagioclase) drive continuous zoning; peritectics record incongruent melting",
  "Cooling paths: liquid follows the liquidus to the eutectic, then crystallizes isothermally",
  "Real systems extend the same reading to ternary and multi-component diagrams",
 ],
 "requirements": [
  "The diopside-anorthite eutectic diagram as the reference example",
  "Algebra-level comfort with the Gibbs phase rule",
  "Understanding of solidus, liquidus, and eutectic vocabulary",
  "Bowen's reaction series (the experimental reality behind the diagrams)",
 ],
 "standards": [
  "Phase-rule and eutectic systematics per standard texts (Best 2002; Winter 2013; Philpotts & Ague 2009)",
  "Experimentally determined binary systems per petrology literature",
 ],
 "citations": [CIT_BEST, CIT_PHILPOTTS],
 "sig_lens": (
  "Signature edition: phase diagrams deployed as his original stability "
  "atlases — every binary system readable as a cooling script, with his "
  "Signature path-tracer following any bulk composition from liquidus to "
  "solidus."),
 "demo_kind": "gibbs_phase_rule",
},
{
 "key": "lever-rule", "name": "The Lever Rule: Quantifying Phase Diagrams",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "The lever rule turns a phase diagram from a picture into numbers: at "
  "any temperature in a two-phase field, it gives the exact proportions "
  "of the two coexisting phases. If a bulk composition C_0 lies between "
  "solid composition C_s and liquid composition C_l, the mass fraction of "
  "liquid is (C_0 − C_s)/(C_l − C_s) — the length of the opposite lever "
  "arm divided by the total. The rule is pure mass balance: the bulk "
  "composition must equal the weighted average of the phase compositions. "
  "Petrologists use it to compute how much has crystallized at each "
  "temperature along a cooling path, to read modal proportions from a "
  "diagram, and to check mass balance in experiments. Combined with the "
  "batch-melting equation, it also quantifies partial melting: the same "
  "lever that reads crystals-vs-melt on cooling reads melt-vs-residue on "
  "heating."),
 "how_it_works": (
  "Apply the lever rule in three steps. One: draw the isothermal tie-line "
  "through the bulk composition at the temperature of interest, reading "
  "the two phase compositions where it meets the phase boundaries (C_s on "
  "the solidus, C_l on the liquidus). Two: measure the segments — the "
  "fraction of liquid equals the segment from bulk to solid divided by the "
  "whole tie-line; the fraction of solid equals the segment from bulk to "
  "liquid divided by the whole. Three: verify by mass balance — "
  "f_solid · C_s + f_liquid · C_l must equal C_0. Worked example: bulk 40% "
  "An, solid 80% An, liquid 20% An at some temperature → liquid fraction "
  "= (40−80)/(20−80) = 2/3, solid = 1/3; check: (1/3)(80) + (2/3)(20) = 40. "
  "The rule generalizes: in ternary diagrams the same mass balance is "
  "done with areas (the triangular lever rule), and in melting problems "
  "it gives the melt fraction directly. It is the quantitative backbone "
  "under every crystallization calculation."),
 "key_points": [
  "Lever rule: phase fractions from the tie-line segments — opposite arm over total",
  "Liquid fraction = (C_0 − C_s)/(C_l − C_s); solid fraction = (C_l − C_0)/(C_l − C_s)",
  "Pure mass balance: bulk = weighted average of phase compositions (always verify)",
  "Quantifies crystallization progress along any cooling path",
  "Same rule reads melt fraction in partial-melting problems",
  "Extends to ternary diagrams via the triangular (area) lever rule",
 ],
 "requirements": [
  "A binary phase diagram with a drawn tie-line to practice on",
  "Algebra comfort: ratios and weighted averages",
  "Understanding of solidus/liquidus/tie-line vocabulary",
  "The habit of mass-balance verification on every calculation",
 ],
 "standards": [
  "Lever-rule formulation per standard petrology texts (Best 2002; Winter 2013)",
  "Mass-balance conventions per thermodynamics literature",
 ],
 "citations": [CIT_BEST, CIT_WINTER],
 "sig_lens": (
  "Signature edition: the lever rule implemented as his original "
  "proportion engine — any tie-line in, exact phase fractions out, with "
  "his Signature mass-balance audit verifying every answer."),
 "demo_kind": "lever_rule",
},
{
 "key": "ternary-phase-diagrams", "name": "Ternary Phase Diagrams: Three-Component Crystallization",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Ternary diagrams add a third component — the equilateral triangle where "
  "each corner is 100% of one component and every interior point sums to "
  "100%. The classic petrological ternary is forsterite-diopside-silica "
  "(Mg2SiO4–CaMgSi2O6–SiO2): its liquidus surface is divided into primary "
  "phase fields (olivine, pyroxene, silica minerals, plus the reaction "
  "curve where olivine reacts to pyroxene), meeting at cotectics (two "
  "phases co-crystallizing) and the ternary eutectic (three phases). "
  "Cooling paths curve across the diagram: a melt in the olivine field "
  "crystallizes olivine until it hits the olivine-pyroxene reaction curve, "
  "then follows the cotectic down to the eutectic. The forsterite-silica "
  "join shows the peritectic: olivine + liquid react to make enstatite — "
  "Bowen's discontinuous reaction drawn as geometry. Ternary diagrams are "
  "where binary intuition becomes real magma behavior."),
 "how_it_works": (
  "Reading a ternary diagram starts with plotting: each component's "
  "percentage is measured parallel to the opposite side, and the three "
  "always sum to 100%. Identify which primary phase field holds the bulk "
  "composition — that mineral crystallizes first. Follow cooling: the "
  "liquid composition moves directly away from the crystallizing phase "
  "(mass balance), until it strikes a cotectic curve — then two phases "
  "co-crystallize and the liquid follows the curve downhill to the "
  "eutectic, where three phases crystallize together until liquid is "
  "gone. Reaction curves need care: at the olivine-pyroxene peritectic, "
  "olivine is consumed to make pyroxene — if fractionation removed the "
  "olivine, the reaction cannot complete and the liquid overshoots toward "
  "silica, eventually crystallizing quartz. This single mechanism — "
  "reaction relationship plus crystal removal — is the diagram-language "
  "statement of how basaltic magmas differentiate toward andesitic and "
  "rhyolitic compositions."),
 "key_points": [
  "Ternary triangle: three components, every point sums to 100%",
  "Forsterite-diopside-silica is the classic teaching system (olivine, pyroxene, silica fields)",
  "Primary phase fields → cotectics (2 phases) → ternary eutectic (3 phases) along cooling",
  "Liquid moves away from the crystallizing phase; at cotectics it follows the curve downhill",
  "Peritectic reaction curves (olivine + liquid → pyroxene) are Bowen's reactions as geometry",
  "Fractionation at a reaction curve drives liquids toward silica enrichment",
 ],
 "requirements": [
  "Skill at plotting and reading ternary coordinates",
  "The Fo-Di-SiO2 diagram as the reference example",
  "Binary eutectic/peritectic reading skill from the previous records",
  "Understanding that reaction curves can be crossed or followed depending on fractionation",
 ],
 "standards": [
  "Ternary constructions per standard igneous texts (Best 2002; Philpotts & Ague 2009)",
  "Fo-Di-SiO2 systematics per experimental petrology literature",
 ],
 "citations": [CIT_BEST, CIT_PHILPOTTS],
 "sig_lens": (
  "Signature edition: ternary diagrams run as his original three-"
  "component navigator — any bulk composition plotted, its cooling path "
  "traced across fields and cotectics, with his Signature flag marking "
  "where fractionation diverts the path."),
 "demo_kind": "ternary_normalize",
},
{
 "key": "geothermobarometry", "name": "Geothermobarometry: Thermometers and Barometers in Minerals",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Geothermobarometry extracts absolute pressures and temperatures from "
  "mineral chemistry. The thermometers exploit temperature-sensitive "
  "element exchange: the garnet-biotite Fe-Mg exchange thermometer "
  "(calibrated experimentally by Ferry and Spear, 1978) reads temperature "
  "from how iron and magnesium partition between coexisting garnet and "
  "biotite — hotter means more equal partitioning. The barometers exploit "
  "pressure-sensitive net-transfer reactions: GASP (garnet–aluminosilicate–"
  "silica–plagioclase) reads pressure from the anorthite content of "
  "plagioclase coexisting with garnet, kyanite/sillimanite, and quartz. "
  "Used together on one rock, thermometer plus barometer pin a single "
  "P-T point; applied to zoned minerals (garnet cores vs. rims), they "
  "trace the P-T path the rock traveled. Every calibration carries "
  "uncertainty (±50°C, ±1-2 kbar typical), so petrologists cross-check "
  "multiple thermobarometers and demand consistency."),
 "how_it_works": (
  "A thermobarometer is an experimentally calibrated equilibrium: "
  "measure the mineral compositions (by electron microprobe), insert them "
  "into the calibration equation, get P or T. For garnet-biotite, compute "
  "K_D = (Fe/Mg)_garnet / (Fe/Mg)_biotite from microprobe analyses; the "
  "Ferry-Spear calibration converts K_D (and pressure) to temperature — "
  "typical K_D values of 4-7 give 550-650°C at mid-crustal pressures. For "
  "GASP, the equilibrium grossular + kyanite + quartz = 3 anorthite shifts "
  "with pressure: measure garnet's grossular content and plagioclase's "
  "anorthite content, and the calibration returns pressure. Critical "
  "practice: analyze rim compositions of touching minerals (cores may "
  "record earlier conditions), check for retrograde resetting (Fe-Mg "
  "exchange continues during cooling, so thermometers often record "
  "closure temperatures, not peaks), and never trust a single "
  "thermobarometer — a P-T point earned by two independent systems is "
  "worth ten from one."),
 "key_points": [
  "Geothermobarometry converts mineral chemistry into absolute P and T",
  "Garnet-biotite Fe-Mg exchange (Ferry & Spear 1978): the classic thermometer",
  "GASP (garnet-aluminosilicate-silica-plagioclase): the classic barometer",
  "Thermometer + barometer on one rock = one P-T point; zoned minerals = a P-T path",
  "Analyze touching rims, watch for retrograde resetting during cooling",
  "Typical uncertainties ±50°C and ±1-2 kbar — cross-check with independent systems",
 ],
 "requirements": [
  "Electron-microprobe mineral analyses (or published data to practice on)",
  "Understanding of equilibrium, partition coefficients, and closure temperature",
  "The Ferry-Spear and GASP calibrations as reference equations",
  "Metamorphic facies/grade context to sanity-check results",
 ],
 "standards": [
  "Ferry & Spear (1978) garnet-biotite calibration",
  "GASP barometer per thermobarometry literature; uncertainty conventions per Spear (1993)",
 ],
 "citations": [CIT_FERRY, CIT_SPEAR],
 "sig_lens": (
  "Signature edition: geothermobarometry operated as his original "
  "mineral-instrument panel — microprobe analyses in, P-T points out, "
  "with his Signature cross-check protocol demanding multi-system "
  "agreement before any point is trusted."),
 "demo_kind": "garnet_biotite",
},
{
 "key": "petrographic-microscopy", "name": "Petrographic Microscopy: Reading Thin Sections",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "The petrographic microscope is petrology's core instrument, and the "
  "thin section — a rock slice ground to exactly 30 micrometers thick and "
  "mounted on glass — is its sample. At 30 µm, most minerals become "
  "transparent, and the microscope's polarized light interrogates their "
  "crystal optics. In plane-polarized light (PPL), the petrologist reads "
  "relief (how strongly the mineral stands out against the mounting "
  "medium), color and pleochroism (color change on stage rotation — "
  "biotite's brown-to-pale is unmistakable), cleavage, and habit. "
  "Crossed polars (XPL) add interference colors, extinction behavior, and "
  "twins. A practiced petrologist identifies every mineral in a thin "
  "section, estimates modes, reads textures and reaction relationships, "
  "and names the rock — all from a slice thinner than a human hair. The "
  "microscope routine is the discipline's central craft skill."),
 "how_it_works": (
  "The thin-section routine runs in a fixed order so nothing is missed. "
  "In PPL at low magnification: scan for texture and grain size, note "
  "relief (high-relief minerals like garnet and olivine stand out boldly; "
  "quartz and feldspar are low-relief), check color and pleochroism by "
  "rotating the stage, and map cleavage and habit. Switch to XPL: read "
  "interference colors (first-order grays for quartz/feldspar, vivid "
  "second/third-order for olivine and pyroxene — a direct readout of "
  "birefringence at standard thickness), check extinction (minerals go "
  "dark four times per rotation; the extinction angle identifies "
  "plagioclase composition and pyroxene type), and look for twins "
  "(plagioclase's polysynthetic stripes, microcline's tartan). Use the "
  "accessory plates (gypsum plate, quartz wedge) to determine optic sign "
  "and elongation. Then synthesize: mineralogy + texture + structures = "
  "the rock name and its story. The routine is deliberately exhaustive — "
  "the mineral you skip is the one that names the facies."),
 "key_points": [
  "Thin sections are ground to exactly 30 µm — thin enough for minerals to transmit light",
  "Plane-polarized light: relief, color, pleochroism, cleavage, habit",
  "Crossed polars: interference colors, extinction angles, twinning",
  "Interference colors at 30 µm directly encode birefringence (quartz gray, olivine vivid)",
  "Extinction angles identify plagioclase composition and pyroxene varieties",
  "Fixed routine order (PPL scan → XPL optics → synthesis) so no mineral is missed",
 ],
 "requirements": [
  "Access to a polarizing microscope and a teaching set of thin sections",
  "The 30-µm standard and why it matters (interference colors are thickness-calibrated)",
  "Michel-Lévy interference color chart as a reference",
  "Patience: the routine is a practiced craft, learned at the microscope",
 ],
 "standards": [
  "Thin-section preparation and 30-µm standard per petrographic convention",
  "Optical procedures per Nesse (2012) and standard petrography texts",
 ],
 "citations": [CIT_NESSE, CIT_BEST],
 "sig_lens": (
  "Signature edition: the petrographic microscope run as his original "
  "thin-slice interrogator — the fixed PPL-to-XPL routine codified as "
  "his Signature scan protocol that misses no mineral and misnames no rock."),
 "demo_kind": "thin_section",
},
{
 "key": "optical-properties", "name": "Optical Properties in Thin Section: Birefringence and Extinction",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Between crossed polars, minerals paint themselves in interference "
  "colors — and those colors are quantitative. Light entering an "
  "anisotropic mineral splits into two rays traveling at different "
  "speeds; the birefringence (δ) is the difference between the two "
  "refractive indices. On exiting, the rays are out of phase by the "
  "retardation Δ = thickness × birefringence; at the standard 30 µm "
  "thickness, retardation depends only on the mineral. The Michel-Lévy "
  "chart maps retardation to color: quartz (δ ≈ 0.009) gives ~270 nm — "
  "first-order gray-white; olivine (δ ≈ 0.035) gives ~1050 nm — vivid "
  "second-order colors. Extinction — going dark four times per stage "
  "rotation — measures crystallographic orientation: the extinction "
  "angle of plagioclase (Michel-Lévy method) determines its anorthite "
  "content, and pyroxene extinction angles separate augite from "
  "pigeonite. Optics turn the microscope into a measuring instrument."),
 "how_it_works": (
  "Quantitative optics runs on the retardation equation and the "
  "Michel-Lévy chart. Measure (or estimate) the interference color, read "
  "its retardation in nanometers from the chart, divide by the 30 µm "
  "thickness to get birefringence — or run it backward: known "
  "birefringence predicts the color, which identifies the mineral "
  "(calcite's extreme birefringence gives pearly pastel 'twinkling'; "
  "quartz stays first-order gray). The Becke line test in PPL pins "
  "refractive index relative to the mounting medium (n ≈ 1.54): the "
  "bright halo moves into the higher-index material when the focus is "
  "raised. For extinction angles, align a cleavage or twin plane "
  "north-south, rotate to extinction, read the angle — plagioclase "
  "albite twins give maximum extinction angles that map directly to "
  "An content via the Michel-Lévy curves. Sign of elongation (using the "
  "gypsum plate) and optic sign (interference figures) complete the "
  "optical fingerprint — every mineral identified by numbers, not "
  "impressions."),
 "key_points": [
  "Birefringence δ = difference between the mineral's two refractive indices",
  "Retardation Δ = thickness × δ; at 30 µm it depends only on the mineral",
  "Michel-Lévy chart maps retardation (nm) to interference color order",
  "Quartz ~270 nm (first-order gray); olivine ~1050 nm (vivid second-order)",
  "Becke line test determines refractive index relative to the mount (n ≈ 1.54)",
  "Plagioclase extinction angles (Michel-Lévy method) give anorthite content quantitatively",
 ],
 "requirements": [
  "A polarizing microscope with rotating stage and accessory slot",
  "The Michel-Lévy interference color chart",
  "Understanding of polarized light, retardation, and extinction",
  "Practice minerals: quartz, olivine, calcite, plagioclase with albite twins",
 ],
 "standards": [
  "Optical methods per Nesse (2012)",
  "Michel-Lévy chart and extinction-angle curves per optical mineralogy convention",
 ],
 "citations": [CIT_NESSE, CIT_STD],
 "sig_lens": (
  "Signature edition: thin-section optics run as his original light-"
  "measurement bench — retardation computed, colors decoded, extinction "
  "angles converted to composition in his Signature optical pipeline."),
 "demo_kind": "retardation",
},
{
 "key": "igneous-geochemistry", "name": "Igneous Geochemistry: Trace Elements and Isotopes",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Major elements name the rock; trace elements and isotopes tell its "
  "history. The rare-earth elements (REE: lanthanum through lutetium), "
  "normalized to chondritic meteorite abundances and plotted in atomic-"
  "number order, give every magma a fingerprint: steep light-REE-enriched "
  "patterns mean small melt fractions or enriched sources; flat patterns "
  "mean large melt fractions of depleted mantle; europium anomalies record "
  "plagioclase fractionation (Eu²⁺ hides in plagioclase). Incompatible-"
  "element spider diagrams flag subduction input (niobium-tantalum "
  "depletion) or crustal contamination. Radiogenic isotopes (strontium, "
  "neodymium, lead, hafnium) are immune to fractionation — they fingerprint "
  "the source itself: depleted mantle, enriched mantle, or continental "
  "crust have distinct, time-integrated isotopic signatures. Geochemistry "
  "is how petrology sees through differentiation to the source."),
 "how_it_works": (
  "Geochemical interpretation layers three plots. First, the chondrite-"
  "normalized REE pattern: divide each measured REE by its chondritic "
  "abundance and plot log-scale vs. atomic number — the slope (La/Yb "
  "ratio), the absolute level, and the Eu anomaly are read directly. "
  "Garnet in the residue holds back heavy REE, so depleted heavy REE "
  "means melting was deep (garnet stable); a negative Eu anomaly means "
  "plagioclase was removed. Second, the multi-element spider diagram "
  "(elements ordered by incompatibility): troughs at Nb-Ta diagnose "
  "subduction-zone magmas worldwide. Third, isotope ratios: plot "
  "⁸⁷Sr/⁸⁶Sr vs. ¹⁴³Nd/¹⁴⁴Nd — mantle-derived magmas plot in the depleted "
  "quadrant, crustal contaminants pull compositions toward high Sr and "
  "low Nd. Because isotopes don't fractionate during melting or "
  "crystallization, any isotopic shift must be source or contamination — "
  "the constraint that keeps petrogenetic models honest."),
 "key_points": [
  "REE patterns (chondrite-normalized) fingerprint melt fraction, source enrichment, and residual minerals",
  "Eu anomalies record plagioclase fractionation; heavy-REE depletion records residual garnet (deep melting)",
  "Spider diagrams: Nb-Ta troughs diagnose subduction-zone magmas",
  "Radiogenic isotopes (Sr, Nd, Pb, Hf) fingerprint sources — immune to fractionation effects",
  "⁸⁷Sr/⁸⁶Sr vs. ¹⁴³Nd/¹⁴⁴Nd separates depleted mantle from crustal contamination",
  "Geochemistry sees through differentiation to the magma's source",
 ],
 "requirements": [
  "Whole-rock trace-element and isotope data (ICP-MS analyses)",
  "Chondrite normalization values as a reference table",
  "Understanding of incompatibility ordering and partition coefficients",
  "Log-scale plotting comfort for REE patterns",
 ],
 "standards": [
  "Chondrite normalization per standard geochemical convention",
  "Isotope systematics per standard igneous geochemistry (Winter 2013; Best 2002)",
 ],
 "citations": [CIT_WINTER, CIT_BEST],
 "sig_lens": (
  "Signature edition: igneous geochemistry run as his original source-"
  "fingerprint laboratory — REE patterns, spider diagrams, and isotope "
  "ratios layered in his Signature provenance stack that sees through "
  "differentiation to the source."),
 "demo_kind": "ree_normalize",
},
{
 "key": "ophiolites-mantle", "name": "Ophiolites and Mantle Petrology: Slices of Ocean Floor on Land",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Ophiolites are slabs of oceanic lithosphere thrust onto continents — "
  "the mantle and ocean crust you can walk on. The Penrose (1972) "
  "sequence, bottom to top: ultramafic tectonite (deformed mantle "
  "peridotite, often serpentinized), layered and isotropic gabbro (the "
  "frozen magma chamber), sheeted dike complex (100% dikes, each chilling "
  "against the last — the spreading center's plumbing), pillow basalts "
  "(erupted under the sea), capped by deep-sea sediments (chert, pelagic "
  "limestone). Finding this exact stack on land proves an ancient ocean "
  "closed there. Mantle petrology studies the bottom of the stack: "
  "peridotite mineralogy (olivine + orthopyroxene + clinopyroxene ± "
  "garnet/spinel), melting residues (harzburgite left after basalt "
  "extraction), and mantle xenoliths — accidental peridotite fragments "
  "carried up in basalts and kimberlites, our only direct samples of the "
  "deep mantle."),
 "how_it_works": (
  "Ophiolite analysis works by matching the observed stack to the Penrose "
  "template and reading each unit's petrology. The sheeted dikes are the "
  "diagnostic heart: measure dike orientations — true sheeted complexes "
  "show one-way chilling (each dike chilled against the previous), proving "
  "seafloor spreading rather than random intrusion. Gabbro layering "
  "records magma-chamber processes (fractional crystallization in situ); "
  "the petrologic Moho (crust-mantle boundary) is picked where gabbro "
  "gives way to tectonite peridotite. Mantle tectonite fabrics — deformed "
  "olivine with lattice-preferred orientation — record solid-state mantle "
  "flow beneath the ridge. Geochemistry ties it together: ophiolite "
  "basalts with arc signatures (Nb-Ta depletion) mark suprasubduction "
  "spreading, the setting of most preserved ophiolites. The complete "
  "reading turns a mountain of green rock into a vanished ocean's birth "
  "certificate."),
 "key_points": [
  "Ophiolite = obducted oceanic lithosphere; the Penrose (1972) sequence is the template",
  "Bottom→top: mantle tectonite → gabbro → sheeted dikes → pillow basalt → deep-sea sediment",
  "Sheeted dike complex (one-way chilled dikes) is the diagnostic spreading-center proof",
  "Mantle tectonite: deformed peridotite recording solid-state flow beneath ridges",
  "Mantle xenoliths in basalts/kimberlites are direct deep-mantle samples",
  "Arc-signature chemistry marks suprasubduction-zone ophiolites (most preserved examples)",
 ],
 "requirements": [
  "The Penrose ophiolite stratigraphy as a reference column",
  "Understanding of seafloor spreading and obduction",
  "Peridotite mineralogy (olivine, pyroxenes, garnet/spinel)",
  "Familiarity with sheeted-dike chilling criteria",
 ],
 "standards": [
  "Penrose ophiolite definition (Penrose Conference 1972) per petrology literature",
  "Mantle petrology systematics per standard texts (Best 2002; Winter 2013)",
 ],
 "citations": [CIT_BEST, CIT_WINTER],
 "sig_lens": (
  "Signature edition: ophiolites surveyed as his original vanished-ocean "
  "recovery program — the Penrose stack verified unit by unit, with his "
  "Signature checklist certifying each ancient spreading center."),
 "demo_kind": "ophiolite_order",
},
{
 "key": "granite-petrogenesis", "name": "Granite Petrogenesis: The Granite Problem",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Granites are the most abundant plutonic rocks of the continents — and "
  "the most debated. The 'granite problem' asks how huge bodies of "
  "high-silica magma form: by extreme fractionation of basalt, by melting "
  "of crust, or by mixing of both? The I-S-A-M classification (Chappell "
  "and White 1974, extended by later workers) organizes the answers by "
  "source. I-type granites derive from igneous protoliths: metaluminous, "
  "hornblende-bearing, with magnetite. S-type granites derive from "
  "sedimentary protoliths: peraluminous, muscovite/garnet/cordierite-"
  "bearing, with ilmenite — the melted metasediments of collisional belts. "
  "A-type granites are anorogenic/alkaline: hot, dry, iron-rich, "
  "associated with rifts and hotspots. M-type granites are rare mantle-"
  "derived plagiogranites of ophiolites. Isotopes adjudicate: S-types "
  "carry the crustal isotopic signature of their sedimentary source; I-"
  "types carry more mantle-like values. Most real batholiths are hybrids."),
 "how_it_works": (
  "Granite typing works as a multi-criteria diagnosis. Mineralogy first: "
  "hornblende + titanite + magnetite points I-type; muscovite + garnet "
  "± cordierite + ilmenite points S-type; arfvedsonite/aegirine or "
  "annite-rich biotite with fluorite points A-type. Chemistry second: "
  "compute the alumina saturation index (ASI = molar "
  "Al2O3/(CaO+Na2O+K2O)) — metaluminous (<1.0) suggests I-type, "
  "peraluminous (>1.0) demands S-type (excess aluminum must come from a "
  "sedimentary source). Isotopes third: initial ⁸⁷Sr/⁸⁶Sr above ~0.708 or "
  "negative epsilon-Nd marks crustal (S-type) sources. Field relations "
  "fourth: S-types carry metasedimentary enclaves and sit in collisional "
  "belts; A-types sit in rifts with bimodal basalt-rhyolite associations. "
  "The modern synthesis: most granites blend mantle heat and crustal "
  "melting — the I/S/A/M types are end members of a continuum, and "
  "classifying a granite means locating it on that continuum."),
 "key_points": [
  "The granite problem: how voluminous felsic magmas form — fractionation, crustal melting, or both",
  "I-type: igneous source, metaluminous, hornblende + magnetite",
  "S-type: sedimentary source, peraluminous, muscovite/garnet + ilmenite, collisional belts",
  "A-type: anorogenic/alkaline, hot-dry-Fe-rich, rifts and hotspots; M-type: rare mantle plagiogranites",
  "Alumina saturation index (ASI) and Sr-Nd isotopes adjudicate I vs. S origin",
  "Real batholiths are usually hybrids — the types are end members of a continuum",
 ],
 "requirements": [
  "Whole-rock major-element analysis (for ASI) and mineralogy",
  "Sr-Nd isotope literacy for source fingerprinting",
  "The Chappell & White criteria as a reference table",
  "Understanding that peraluminous chemistry requires an aluminous (sedimentary) source",
 ],
 "standards": [
  "I-S classification per Chappell & White (1974); A/M extensions per petrology literature",
  "ASI formulation per Shand (1927) as used in granite literature",
 ],
 "citations": [CIT_CHAPPELL, CIT_BEST],
 "sig_lens": (
  "Signature edition: granite petrogenesis run as his original source "
  "court — mineralogy, ASI chemistry, and isotopes heard as evidence, "
  "with his Signature verdict placing every granite on the I-S-A-M "
  "continuum."),
 "demo_kind": "granite_types",
},
{
 "key": "ptt-paths", "name": "Metamorphic P-T-t Paths: Clockwise, Counterclockwise, and What They Mean",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A P-T-t path is the pressure-temperature-time trajectory a rock "
  "followed through metamorphism — its journey plotted on the P-T "
  "diagram with time as the hidden third axis (Spear 1993). Clockwise "
  "paths are the collisional signature: burial first (pressure rises "
  "while temperature lags — the rock is cold for its depth), then heating "
  "(thermal relaxation catches up), then near-isothermal decompression "
  "(rapid exhumation while still hot), then cooling. Zoned garnets record "
  "it: manganese-rich cores grown early, magnesium-rich rims grown at "
  "peak. Counterclockwise paths — heating before deep burial — mark "
  "magmatic arcs and contact settings, where intrusions heat the crust "
  "before thickening buries it. Hairpin paths with isothermal "
  "decompression record extensional collapse of overthickened crust. "
  "Reading a P-T-t path turns a static assemblage into a tectonic movie."),
 "how_it_works": (
  "Reconstructing a P-T-t path combines thermobarometry with "
  "geochronology on zoned minerals. Garnet is the flight recorder: its "
  "growth zoning (Mn decreasing, Mg increasing core→rim in prograde "
  "growth) is read by microprobe traverses, and each zone's composition "
  "fed to thermobarometers gives a P-T point — core points plot the early "
  "path, rim points the peak. Monazite or zircon inclusions in specific "
  "garnet zones, dated by U-Pb, pin absolute times to the path (the 't'). "
  "Inclusion suites add constraints: kyanite inclusions in garnet cores "
  "with sillimanite in the matrix record decompression through the "
  "aluminosilicate triple point. Diffusion modeling of relaxed zoning "
  "profiles gives cooling rates. The assembled path is then matched to "
  "tectonic models: clockwise + isothermal decompression = collisional "
  "thickening then extensional exhumation; counterclockwise = arc "
  "magmatism. The path is the orogeny's autobiography, written in one "
  "garnet."),
 "key_points": [
  "P-T-t paths plot a rock's pressure-temperature journey through time (Spear 1993)",
  "Clockwise: burial → heating → isothermal decompression → cooling = collisional belts",
  "Counterclockwise: heating before deep burial = magmatic arcs and contact settings",
  "Zoned garnet is the flight recorder: core→rim chemistry = early→peak conditions",
  "Monazite/zircon inclusions dated by U-Pb pin absolute time to the path",
  "Inclusion suites (kyanite cores, sillimanite matrix) record decompression through phase boundaries",
 ],
 "requirements": [
  "Thermobarometry skill (garnet-biotite, GASP) from the earlier record",
  "Electron-microprobe garnet zoning traverses (or published data)",
  "U-Pb geochronology literacy (monazite, zircon)",
  "The aluminosilicate phase diagram for decompression interpretation",
 ],
 "standards": [
  "P-T-t path concepts per Spear (1993)",
  "Garnet zoning interpretation per metamorphic petrology literature",
 ],
 "citations": [CIT_SPEAR, CIT_YARDLEY],
 "sig_lens": (
  "Signature edition: P-T-t paths reconstructed as his original tectonic "
  "flight-recorder playback — garnet zones decoded into a dated journey, "
  "with his Signature matching of each path shape to its orogenic setting."),
 "demo_kind": "ptt_interpret",
},
{
 "key": "experimental-petrology", "name": "Experimental Petrology: Recreating Deep Earth in the Laboratory",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Experimental petrology recreates the unreachable: the pressures and "
  "temperatures inside Earth, in presses small enough to hold. The "
  "piston-cylinder apparatus squeezes millimeter samples to ~4 GPa "
  "(~120 km depth) at up to 2000°C — the workhorse for magma genesis, "
  "phase equilibria, and thermobarometer calibration. Multi-anvil presses "
  "reach ~25 GPa (lower mantle) for deep phase transitions like olivine → "
  "wadsleyite → ringwoodite → perovskite. Diamond-anvil cells reach "
  "beyond 300 GPa — core pressures — on microgram samples heated by "
  "laser, with synchrotron X-rays watching structures change live. "
  "Cold-seal and internally heated pressure vessels handle volatile-rich "
  "systems at crustal conditions. Every phase diagram, every "
  "thermobarometer calibration, and Bowen's reaction series itself came "
  "from such experiments: the lab is where petrology's numbers are earned."),
 "how_it_works": (
  "High-pressure experiments work by trading sample size for pressure: "
  "pressure = force / area, so shrinking the anvil face multiplies the "
  "pressure from the same press. A piston-cylinder run: pack the starting "
  "powder (a synthetic rock composition) into a precious-metal capsule "
  "(welded shut to control volatiles), load it in the pressure assembly, "
  "pressurize, heat with a graphite furnace, hold for hours to days "
  "(diffusion must reach equilibrium — the eternal experimental worry), "
  "then quench (cut power; the sample freezes in milliseconds, preserving "
  "the high-P-T assemblage). Analyze the run products by microprobe and "
  "X-ray diffraction: which phases grew, what compositions — one point on "
  "a phase diagram. Bracket every boundary with runs from both sides "
  "(growing vs. consuming the phase) to prove equilibrium rather than "
  "sluggish kinetics. Reversal brackets are the gold standard: a boundary "
  "believed only when approached from above and below in temperature."),
 "key_points": [
  "Piston-cylinder: ~4 GPa / 2000°C — magma genesis, phase diagrams, thermobarometer calibration",
  "Multi-anvil: ~25 GPa — mantle transition-zone phase changes",
  "Diamond-anvil cell: 300+ GPa — core pressures, laser-heated, synchrotron-observed",
  "Pressure = force / area: smaller anvils trade sample size for pressure",
  "Run procedure: capsule → pressurize → heat → hold for equilibrium → quench → analyze",
  "Reversal brackets (approaching boundaries from both sides) prove equilibrium",
 ],
 "requirements": [
  "Understanding of pressure units (GPa, kbar) and depth equivalents",
  "The P = F/A relationship and why anvil size matters",
  "Concept of equilibrium vs. kinetics (why long holds and reversals matter)",
  "Familiarity with quenching as assemblage preservation",
 ],
 "standards": [
  "Apparatus capabilities per experimental petrology literature",
  "Reversal-bracket practice per high-pressure experimental convention",
 ],
 "citations": [CIT_BOWEN, CIT_STD],
 "sig_lens": (
  "Signature edition: experimental petrology run as his original deep-"
  "Earth simulator bay — piston-cylinder to diamond-anvil, each apparatus "
  "profiled in his Signature facility guide with its pressure range and "
  "the equilibria it earned."),
 "demo_kind": "pressure_calc",
},
{
 "key": "field-petrology", "name": "Field Petrology: Mapping and Sampling Like a Petrologist",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "All petrology begins in the field, and field method is a discipline of "
  "its own. Mapping records what rock is where: contacts between units "
  "are walked and drawn, distinguishing intrusive contacts (chilled "
  "margins, cross-cutting, baked aureoles) from depositional contacts "
  "(conformable layering) and faults (offset markers, gouge, breccia). "
  "Orientation is measured with compass-clinometer: strike (the compass "
  "direction of a horizontal line on the plane) and dip (the steepest "
  "angle below horizontal), recorded by the right-hand rule (dip direction "
  "is 90° clockwise from strike). Sampling is strategic, not souvenir: "
  "fresh, representative, documented with location, orientation, "
  "relationships, and a field number tied to notebook, photo, and map. "
  "The field test of every lab result is the outcrop — a thin section "
  "never overrules a contact relationship seen in place."),
 "how_it_works": (
  "Field petrology works as a documentation pipeline. At each outcrop: "
  "describe before interpreting — lithology, grain size, minerals, "
  "textures, structures, alteration, then the interpretation. Measure "
  "orientations systematically: strike and dip of bedding, foliation, "
  "contacts, and joints, plotted on stereonets back at camp to find fold "
  "axes and stress directions. Trace contacts along strike to map unit "
  "geometry; note every cross-cutting relationship (the cutter is younger "
  "— the fundamental relative-dating rule). Sample with purpose: one "
  "sample per distinct lithology per outcrop minimum, plus oriented "
  "samples for microstructural work and fresh material for geochemistry "
  "(weathered rinds lie about chemistry). Photograph with scale, north "
  "arrow, and sample number visible. The notebook is the primary data "
  "record — the map, the thin sections, and the analyses all hang from "
  "field observations, and a lost field number orphans every downstream "
  "result."),
 "key_points": [
  "Field method: describe first, interpret second — lithology, texture, structure, then meaning",
  "Contact types diagnose relationships: intrusive (chilled margins, aureoles), depositional, fault",
  "Strike/dip by the right-hand rule; stereonets extract fold axes and stress directions",
  "Cross-cutting relationships give relative age (the cutter is younger)",
  "Sample fresh, representative, and documented — field number ties notebook, photo, map, and lab",
  "The outcrop overrules the lab: contact relationships seen in place are primary evidence",
 ],
 "requirements": [
  "A geological compass-clinometer and a field notebook (paper, weatherproof)",
  "Understanding of strike, dip, and the right-hand rule",
  "Hand lens and rock hammer; safety glasses and field safety practice",
  "The habit of scale + north + sample number in every outcrop photo",
 ],
 "standards": [
  "Field measurement conventions (right-hand rule) per geological mapping practice",
  "Contact-relationship criteria per standard field geology texts",
 ],
 "citations": [CIT_STD, CIT_BEST],
 "sig_lens": (
  "Signature edition: field petrology codified as his original outcrop "
  "protocol — the describe-first pipeline, contact diagnostics, and "
  "sampling chain-of-custody in his Signature field manual that keeps "
  "every lab result anchored to rock seen in place."),
 "demo_kind": "strike_dip",
},
]
