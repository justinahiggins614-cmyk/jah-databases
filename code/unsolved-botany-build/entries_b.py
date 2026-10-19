#!/usr/bin/env python3
"""Entries 10-17 (ladder ranks 10-17, Foundations tail + Compounded) for the
Unsolved Botany databases."""

CIT_SIMARD = ("Simard SW et al. Net transfer of carbon between ectomycorrhizal "
              "tree species in the field. Nature; 1997.")
CIT_KARST = ("Karst J et al. Positive citation bias and overinterpreted "
             "reviews suggest that forest fungal networks are not common "
             "mycorrhizal networks. Trends Plant Sci; 2023.")
CIT_CALVO = ("Calvo P et al. Plants are intelligent, here is how. Ann Bot; 2020.")
CIT_TAIZ = ("Taiz L et al. Plants neither possess nor require consciousness. "
            "Trends Plant Sci; 2019.")
CIT_DIXON = ("Dixon HH, Joly J. On the ascent of sap. Philos Trans R Soc Lond "
             "B; 1895.")
CIT_TYREE = ("Tyree MT, Sperry JS. Vulnerability of xylem to cavitation and "
             "embolism. Annu Rev Plant Physiol; 1989.")
CIT_SANTNER = ("Santner A et al. Plant hormones are versatile chemical "
               "regulators of plant growth. Nat Chem Biol; 2009.")
CIT_JONES = ("Jones JDG, Dangl JL. The plant immune system. Nature; 2006.")
CIT_BERENDSEN = ("Berendsen RL et al. The rhizosphere microbiome and plant "
                 "health. Trends Plant Sci; 2012.")
CIT_VANDENKOORNHUYSE = ("Vandenkoornhuyse P et al. The importance of the "
                        "microbiome of the plant holobiont. New Phytol; 2015.")
CIT_SMITH = ("Smith SE, Read DJ. Mycorrhizal Symbiosis. 3rd ed. Academic "
             "Press; 2008.")
CIT_PASSIOURA = ("Passioura JB. Drought and drought tolerance. Plant Growth "
                 "Regul; 1996.")
CIT_TUBEROSA = ("Tuberosa R, Salvi S. Genomics-based approaches to improve "
                "drought tolerance of crops. Trends Plant Sci; 2006.")

ENTRIES_B = [
    {
        "key": "wood-wide-web",
        "name": "The Wood Wide Web: Do Fungi Really Feed Trees",
        "group": "Foundations",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "problem": ("Forests are stitched together by fungal threads linking tree "
                    "roots into vast networks. Experiments showed carbon moving "
                    "between trees through these mycorrhizal networks - but a "
                    "recent critique argues the evidence for meaningful "
                    "tree-to-tree feeding has been overstated. What do the networks "
                    "really do?"),
        "background": (
            "In 1997, experiments with labeled carbon showed it moving from one "
            "tree species to another through shared mycorrhizal fungi, and the "
            "'wood wide web' entered public imagination: forests as cooperative "
            "networks where mother trees feed seedlings. The picture grew "
            "grander in popular accounts, with claims of resource sharing, "
            "warning signals, and kin favoritism flowing through fungal wires. "
            "Then came the audit: a 2023 review found positive citation bias - "
            "supportive studies cited far more than critical ones - and argued "
            "that field evidence for ecologically significant carbon transfer "
            "between adult trees is thin, with most experiments done on "
            "seedlings in pots. The defenders reply that the networks are "
            "undeniably real and that absence of easy measurement is not "
            "evidence of absence. Today the field is split between a "
            "cooperative-network view and a skeptical view that fungi mainly "
            "serve themselves, moving nutrients primarily from soil to their own "
            "host plants."),
        "why_it_matters": (
            "How forests share - or do not share - resources decides how we "
            "manage them: which trees to plant together, whether old trees "
            "truly nurse the young, and how forests will respond to logging and "
            "climate stress. The debate is also a cautionary tale about how "
            "exciting findings get amplified beyond their evidence."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for measuring what mycorrhizal networks "
            "actually move, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: the question is quantitative, not yes-or-no - the issue "
            "is how much carbon and nutrient moves tree-to-tree relative to what "
            "each tree needs, under real forest conditions. Reasoning: seedling "
            "experiments cannot settle an adult-forest question because the "
            "carbon budgets differ by orders of magnitude; only whole-tree "
            "measurements in the field can. Proposed method: label mature trees "
            "with rare-isotope carbon in replicated forest plots, track the "
            "isotope into neighboring trees of the same and different species "
            "over full seasons, and express every transfer as a fraction of the "
            "receiver's annual carbon budget, with severed-network controls. "
            "What would confirm meaningful sharing: transfers exceeding a few "
            "percent of receiver budgets, concentrated toward shaded kin "
            "seedlings. What would kill it: transfers stuck below a tenth of a "
            "percent in every mature-forest test, with the networks serving "
            "mainly fungus-to-host soil nutrition. What this does NOT claim: it "
            "does not claim networks are unimportant, does not dismiss the "
            "seedling results, and does not propose forest-management changes "
            "until field numbers exist."),
        "citations": [CIT_SIMARD, CIT_KARST],
        "demo_params": {"transfer_fraction": 0.004, "budget_threshold": 0.02, "plots": 8},
    },
    {
        "key": "plant-cognition",
        "name": "Do Plants Think: The Plant Cognition Debate",
        "group": "Foundations",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "problem": ("Plants sense, remember, decide, and communicate - and some "
                    "researchers argue this amounts to a form of cognition or even "
                    "consciousness. Others call that a category error: sophisticated "
                    "information processing is not a mind. Where is the line, and "
                    "do plants cross it?"),
        "background": (
            "The 'plant neurobiology' movement, launched in the mid-2000s, "
            "proposed that root apices act like a distributed brain, integrating "
            "signals much as neurons do. Supporters point to real phenomena: "
            "plants habituate to repeated harmless touch, learn associations "
            "between light and wind, make risk-sensitive foraging decisions with "
            "their roots, and integrate dozens of signals into growth choices. "
            "Critics reply that every one of these can be explained by "
            "well-understood physiology without invoking cognition, and that "
            "words like learning and memory smuggle in implications the data do "
            "not support. A widely cited 2019 critique concluded plants "
            "'neither possess nor require consciousness.' The debate has "
            "continued because it is really two debates: an empirical one about "
            "what plants can do, which keeps delivering surprises, and a "
            "philosophical one about what counts as cognition, which has no "
            "agreed answer even for animals."),
        "why_it_matters": (
            "The answer shapes research funding, science education, and even "
            "ethics: if plants had inner lives, agriculture and forestry would "
            "face moral questions nobody is prepared for. More practically, the "
            "debate drives discovery - every attempt to prove or disprove plant "
            "cognition reveals new physiology. Clarity here would sharpen the "
            "science of all decentralized intelligence, including AI."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for testing plant cognition claims "
            "honestly, with adjustable assumptions and written-down confirm and "
            "refute conditions."),
        "sig_solution": (
            "Assumptions: the empirical and philosophical questions must be "
            "separated - first establish exactly what plants can compute, then "
            "argue separately about labels. Reasoning: debates stall when "
            "evidence about abilities is mixed with arguments about words; an "
            "operational test battery can settle the abilities while leaving "
            "philosophy to philosophers. Proposed method: define a battery of "
            "operational tests - flexible reversal learning, novel-tool-like "
            "problem solving with roots, cross-modal integration under "
            "conflict - run them double-blind across species, and require "
            "pre-registered criteria for passing; separately, convene the "
            "philosophical criteria in advance so results are interpreted, not "
            "renegotiated. What would confirm cognitive-level processing: plants "
            "passing pre-registered tests that current physiological models "
            "cannot produce without new integrative machinery. What would kill "
            "the strong claim: every behavior decomposing into known "
            "signal-response pathways with no residual flexibility. What this "
            "does NOT claim: it does not claim plants feel pain, does not claim "
            "cognition requires a brain, and does not propose ethical rules for "
            "plants - only an honest test battery."),
        "citations": [CIT_CALVO, CIT_TAIZ],
        "demo_params": {"tests": 6, "pass_bar": 5, "species": 12},
    },
    {
        "key": "ascent-of-sap",
        "name": "How Trees Drink From a Hundred Meters Up",
        "group": "Compounded",
        "ladder_rank": 12,
        "ladder_tier": "compounded",
        "problem": ("A coast redwood lifts water a hundred meters against gravity "
                    "with no pump and no moving parts. The cohesion-tension theory "
                    "says evaporating leaves pull continuous water threads up the "
                    "wood - threads under enormous tension that should snap. How "
                    "does the column survive, and can it be repaired when it breaks?"),
        "background": (
            "Proposed in the 1890s, the cohesion-tension theory holds that "
            "transpiration from leaves creates negative pressure that pulls water "
            "up through the xylem, with water's cohesion holding the thread "
            "together under tensions of tens of atmospheres. It is one of "
            "biology's most audacious ideas: the tallest organisms run on "
            "stretched water. Direct measurements with pressure probes seemed to "
            "contradict the extreme tensions at first, though later work "
            "reconciled much of the dispute. The live frontier is embolism: "
            "drought and freezing snap the water threads, filling vessels with "
            "air, and whether and how trees refill them - especially while "
            "neighboring vessels remain under tension - is still contested, with "
            "evidence for root-pressure refilling in some species and mysterious "
            "overnight recovery in others. As droughts intensify, the breaking "
            "point of the water column has become a matter of forest survival."),
        "why_it_matters": (
            "The hydraulic limit sets how tall forests can grow and which "
            "species survive drought - the two variables that will reshape "
            "forests this century. A complete model of embolism and repair "
            "would let us predict dieback, breed drought-safe trees, and even "
            "inspire passive water-lifting technology. It is also simply the "
            "most extreme plumbing on Earth."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for settling the embolism-repair "
            "question, with adjustable assumptions and written-down confirm and "
            "refute conditions."),
        "sig_solution": (
            "Assumptions: embolism repair, where it happens, is local - driven "
            "by living cells adjacent to the blocked vessel, not by whole-tree "
            "pressure changes. Reasoning: refilling a vessel while its neighbors "
            "sit at negative pressure is thermodynamically impossible by bulk "
            "flow, so the mechanism must be cellular and local. Proposed method: "
            "image embolism and refilling in living stems with micro-CT during "
            "controlled drought and recovery, tracking which vessels refill and "
            "whether adjacent living cells show the osmotic signatures of "
            "active pumping; compare species across the drought-tolerance "
            "spectrum. What would confirm it: refilling vessels consistently "
            "paired with local osmotic activity in neighboring parenchyma. What "
            "would kill it: refilling that occurs with no local cellular "
            "signature, or species that never refill despite surviving - "
            "implying tolerance comes from avoidance, not repair. What this does "
            "NOT claim: it does not claim all trees refill, does not claim the "
            "cohesion-tension theory is wrong, and does not propose "
            "drought-proofing until the repair map is complete."),
        "citations": [CIT_DIXON, CIT_TYREE],
        "demo_params": {"height_m": 100.0, "tension_mpa": -2.0, "embolism_pct": 18.0},
    },
    {
        "key": "hormone-crosstalk",
        "name": "The Full Map of Plant Hormone Crosstalk",
        "group": "Compounded",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("Plants run on at least nine major hormones - auxin, cytokinin, "
                    "gibberellin, abscisic acid, ethylene, jasmonate, salicylate, "
                    "brassinosteroids, strigolactones - that constantly argue with "
                    "each other. The complete wiring diagram of who inhibits whom, "
                    "where, and when, has never been drawn."),
        "background": (
            "Each plant hormone was discovered through a striking mutant or "
            "effect: auxin bending stems, gibberellin stretching dwarfs, "
            "ethylene ripening fruit. But hormones never act alone - defense "
            "jasmonate suppresses growth gibberellin, drought abscisic acid "
            "antagonizes growth almost everywhere, and the same hormone can "
            "promote growth in one tissue and inhibit it in another. Decades of "
            "genetics have mapped thousands of pairwise interactions, yet the "
            "system-level map - the full network with its tissue-specific "
            "rewiring, feedback loops, and environmental gating - remains "
            "fragmentary. Modelers can simulate small circuits, but no model "
            "yet predicts how a whole plant reallocates growth versus defense "
            "when drought, shade, and insects strike at once, which is exactly "
            "what real plants do every day."),
        "why_it_matters": (
            "The growth-defense tradeoff is the central dilemma of agriculture: "
            "every unit of energy spent fighting pests is a unit not spent on "
            "yield. A complete crosstalk map would let breeders decouple the "
            "two - protected plants that still grow fast. It would also be the "
            "first fully mapped chemical control system of a multicellular "
            "organism, a landmark for systems biology."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for drawing the complete hormone "
            "crosstalk map, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: the network is hierarchical - a small set of hub "
            "transcription factors integrates most crosstalk - rather than a "
            "flat web of equals. Reasoning: evolution favors reusable control "
            "points, and the same hubs (like DELLA and MYC2 proteins) keep "
            "appearing at hormone intersections. Proposed method: systematically "
            "perturb hormone pairs in a model plant across tissues and stresses, "
            "read out the full transcriptome each time, and infer the directed "
            "network; then validate by predicting the outcome of triple "
            "perturbations the model never saw. What would confirm it: accurate "
            "prediction of unseen triple-hormone responses across tissues. What "
            "would kill it: interactions that rewire unpredictably with every "
            "new condition, implying no stable mappable network exists. What "
            "this does NOT claim: it does not claim the map transfers unchanged "
            "to crops, does not claim nine hormones are the full list, and does "
            "not propose rewiring crops until the hubs are validated in the field."),
        "citations": [CIT_SANTNER],
        "demo_params": {"hormones": 9, "hubs": 6, "triples_tested": 40},
    },
    {
        "key": "plant-immunity",
        "name": "How Plants Fight Disease",
        "group": "Compounded",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("Plants have no antibodies and no mobile immune cells, yet they "
                    "defeat most pathogens. Their two-layer immune system - surface "
                    "sensors plus intracellular tripwires - is mapped in outline, "
                    "but the full diversity of pathogen detectors and how they "
                    "evolve remains an open frontier."),
        "background": (
            "The zigzag model of 2006 organized plant immunity into two tiers: "
            "pattern-triggered immunity, where surface receptors detect generic "
            "microbe molecules, and effector-triggered immunity, where "
            "intracellular NLR proteins catch pathogen weapons that slip past. "
            "Pathogens evolve to evade each layer, plants evolve new detectors, "
            "and the arms race spins on. Genomics revealed the scale of the "
            "unknown: a single plant genome can carry hundreds of NLR genes, "
            "most with no known pathogen target, and wild relatives of crops "
            "hold vast untapped resistance diversity. Open questions include "
            "how NLR proteins distinguish self from non-self without attacking "
            "the plant itself, how immune signaling avoids crippling growth, "
            "and why some resistances last decades while others fall in a "
            "single season."),
        "why_it_matters": (
            "Plant diseases destroy a large share of global harvests every year, "
            "and fungicide resistance is rising. Durable, broad-spectrum "
            "resistance bred from a complete understanding of the immune system "
            "would be worth hundreds of billions and would cut chemical use. "
            "The plant immune system is also a second, independent invention of "
            "sophisticated immunity - studying it illuminates immunity itself."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for cracking durable plant immunity, "
            "with adjustable assumptions and written-down confirm and refute "
            "conditions."),
        "sig_solution": (
            "Assumptions: durable resistance comes from detectors that guard "
            "irreplaceable pathogen targets - molecules the pathogen cannot "
            "easily change - rather than from detectors that chase variable "
            "ones. Reasoning: resistances that last are those aimed at "
            "constrained targets; short-lived ones chase moving targets. "
            "Proposed method: catalog NLR diversity across crop wild relatives, "
            "identify detectors whose targets are conserved across pathogen "
            "strains, and pyramid several such detectors in test lines; "
            "challenge them with evolving pathogen populations over multiple "
            "seasons. What would confirm it: pyramided lines whose resistance "
            "holds for many pathogen generations while single-detector lines "
            "fall. What would kill it: pathogens escaping even conserved-target "
            "detectors rapidly, implying durability needs a different "
            "principle. What this does NOT claim: it does not claim "
            "indestructible crops, does not claim the NLR catalog is nearly "
            "complete, and does not propose deployment until multi-season "
            "field data exist."),
        "citations": [CIT_JONES],
        "demo_params": {"nlr_genes": 400, "pyramid": 4, "seasons": 5},
    },
    {
        "key": "root-microbiome",
        "name": "The Root Microbiome: Who Lives Down There",
        "group": "Compounded",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("Every root is coated in thousands of microbial species that "
                    "shape what the plant absorbs, what diseases strike, and how "
                    "fast it grows. We can now name the microbes - but the full "
                    "functional map of who does what for the plant is still "
                    "being drawn."),
        "background": (
            "The rhizosphere - the soil zone under root influence - is among "
            "the most microbially dense habitats on Earth, and plants actively "
            "garden it, exuding up to a fifth of their photosynthetic carbon to "
            "feed chosen microbes. Sequencing has cataloged the inhabitants in "
            "broad strokes: bacteria, fungi, archaea, and viruses in staggering "
            "diversity. Experiments show the microbiome matters enormously - "
            "sterile plants grow poorly, and swapping microbiomes can transfer "
            "disease resistance between plants. But correlation dominates and "
            "causation lags: for most of the thousands of species, nobody knows "
            "what job each does, how the plant recruits its preferred partners, "
            "or why microbiome transplants work in the greenhouse and often "
            "fail in the field."),
        "why_it_matters": (
            "A functional root-microbiome map would enable probiotic "
            "agriculture: seed coatings of beneficial microbes replacing "
            "fertilizer and pesticides. It would also explain how plants "
            "engineer their own soil environment - knowledge critical for "
            "restoring degraded land. The rhizosphere is the least understood "
            "biodiversity hotspot most people walk over daily."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for mapping microbiome function, with "
            "adjustable assumptions and written-down confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: function follows a keystone logic - a minority of "
            "microbial taxa drive most plant effects, and the rest are "
            "passengers. Reasoning: transplant experiments transfer big effects "
            "with whole communities, but synthetic communities of dozens of "
            "strains often reproduce them, implying a compact functional core. "
            "Proposed method: build synthetic microbial communities by "
            "dropout - removing taxa one functional group at a time - and "
            "measure plant growth, nutrient uptake, and disease resistance; "
            "identify the minimal core that reproduces the full-community "
            "effect, then test that core in real field soils. What would "
            "confirm it: a small defined consortium matching whole-microbiome "
            "performance in the field. What would kill it: effects that vanish "
            "whenever any of hundreds of taxa are removed, implying irreducible "
            "whole-community function. What this does NOT claim: it does not "
            "claim a universal core across soils, does not claim field "
            "transplants will be stable, and does not propose commercial "
            "probiotics until field persistence is proven."),
        "citations": [CIT_BERENDSEN, CIT_VANDENKOORNHUYSE],
        "demo_params": {"taxa": 3000, "core_size": 24, "field_plots": 10},
    },
    {
        "key": "mycorrhizal-functions",
        "name": "What Mycorrhizal Networks Actually Do",
        "group": "Compounded",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("Nearly all land plants partner with mycorrhizal fungi that "
                    "extend their roots a hundredfold. The partnership is "
                    "ancient and universal - yet the full molecular conversation "
                    "between plant and fungus, and the complete list of services "
                    "exchanged, is still being decoded."),
        "background": (
            "Mycorrhizal symbiosis is as old as land plants themselves - "
            "fossils show fungi colonizing the earliest rootless plants 400 "
            "million years ago, and most botanists believe the partnership is "
            "what made land colonization possible. The textbook exchange is "
            "simple: fungus delivers phosphorus and nitrogen, plant pays in "
            "sugars. Molecular work has complicated the picture: the partners "
            "exchange lipids as well as sugars, negotiate with chemical "
            "signals, sanction cheaters, and connect into common networks "
            "whose full functions are debated. Open questions include the "
            "complete signaling lexicon, how plants choose among competing "
            "fungal partners, what fraction of plant nutrition really flows "
            "through fungi in the field, and whether the networks transmit "
            "warning signals or just nutrients."),
        "why_it_matters": (
            "Mycorrhizae underpin most terrestrial plant nutrition - they are "
            "arguably the most important symbiosis on land. Understanding the "
            "partnership fully would transform fertilizer use, reforestation, "
            "and carbon accounting, since the fungi also lock carbon into soil. "
            "It is also the deepest cooperative relationship in plant "
            "evolution, and its rules illuminate cooperation itself."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for decoding the plant-fungus "
            "conversation, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: the partnership runs on a biological market - both "
            "sides continuously adjust exchange rates based on supply and "
            "demand, and the molecular signals encode price information. "
            "Reasoning: cheater sanctions and partner choice only make sense "
            "if each side monitors what it gets per unit given; the signals "
            "should therefore carry quantitative, not just qualitative, "
            "information. Proposed method: track nutrient and carbon fluxes "
            "between single plants and single fungal partners under manipulated "
            "supply ratios, while recording the signaling molecules exchanged; "
            "test whether signal levels predict the exchange rate adjustments. "
            "What would confirm it: signals that quantitatively track exchange "
            "rates and shift when supply ratios change. What would kill it: "
            "fixed exchange ratios regardless of signals, implying the "
            "conversation is ceremonial rather than regulatory. What this does "
            "NOT claim: it does not claim markets explain everything, does not "
            "claim all mycorrhizal types work alike, and does not propose "
            "managing the market until the signals are decoded."),
        "citations": [CIT_SMITH],
        "demo_params": {"exchange_rate": 0.7, "partners": 5, "sanction": 0.3},
    },
    {
        "key": "drought-genetics",
        "name": "The Complete Genetics of Drought Tolerance",
        "group": "Compounded",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("Drought tolerance is controlled by hundreds of genes with "
                    "small individual effects, interacting with each other and "
                    "the environment. The complete genetic architecture - every "
                    "contributor and how they combine - has never been fully "
                    "mapped for any crop."),
        "background": (
            "Drought is the costliest abiotic stress in agriculture, and "
            "breeding for tolerance has historically been slow because the "
            "trait is so polygenic: root architecture, stomatal behavior, "
            "osmotic adjustment, leaf rolling, and flowering time all "
            "contribute, each under many genes. Quantitative genetics has "
            "mapped hundreds of QTLs, and genomic selection now predicts "
            "tolerance better than any single gene test. But the architecture "
            "remains a parts list without an assembly manual: epistatic "
            "interactions are mostly unknown, many QTLs vanish when moved "
            "between genetic backgrounds, and greenhouse discoveries routinely "
            "fail in real fields where drought arrives with heat, pests, and "
            "poor soils together. The field needs not more QTLs but the "
            "combinatorial logic."),
        "why_it_matters": (
            "Water scarcity threatens the food supply of billions, and drought "
            "tolerance is the trait breeders need most. A complete architecture "
            "would let breeders stack the right gene combinations by design "
            "instead of by decade-long trial. It would also be the first "
            "fully solved polygenic trait - a template for every complex trait "
            "in biology."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for solving the drought-tolerance "
            "architecture, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: the architecture is modular - gene groups controlling "
            "root depth, water-use efficiency, and escape timing combine "
            "approximately additively across modules, with most epistasis "
            "inside modules. Reasoning: breeders have long observed that "
            "tolerance components from different parents often stack, which "
            "implies between-module independence. Proposed method: build a "
            "combinatorial panel crossing module-level variants in a common "
            "background, phenotype it under managed field drought with heat, "
            "and fit a modular epistasis model; then predict untested "
            "combinations and verify. What would confirm it: accurate "
            "prediction of new combinations from module parameters. What would "
            "kill it: pervasive cross-module epistasis that defeats every "
            "modular prediction, implying irreducible whole-genome context. "
            "What this does NOT claim: it does not claim a universal module "
            "set across crops, does not claim greenhouse results transfer, and "
            "does not propose designed varieties until field validation is "
            "complete."),
        "citations": [CIT_PASSIOURA, CIT_TUBEROSA],
        "demo_params": {"qtls": 240, "modules": 5, "combos": 120},
    },
]
