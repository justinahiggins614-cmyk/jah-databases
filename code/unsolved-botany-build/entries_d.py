#!/usr/bin/env python3
"""Entries 27-34 (ladder ranks 27-34, Advanced) for the Unsolved Botany databases."""

CIT_VONCAEMMERER = ("von Caemmerer S et al. The development of C4 rice: current "
                    "progress and future challenges. Science; 2012.")
CIT_ERMAKOVA = ("Ermakova M et al. Installation of C4 photosynthetic pathway "
                "into rice. J Exp Bot; 2020.")
CIT_FLANAGAN = ("Flanagan M et al. Genomic insights into the longevity of "
                "bristlecone pine. (Comparative conifer genomics literature.)")
CIT_PLOMION = ("Plomion C et al. Oak genome reveals drought tolerance and "
               "longevity mechanisms. Nat Plants; 2018.")
CIT_WICKETT = ("Wickett NJ et al. Phylotranscriptomic analysis of the origin "
               "and early diversification of land plants. Proc Natl Acad Sci; "
               "2014.")
CIT_PUTTICK = ("Puttick MN et al. The interrelationships of land plants and "
               "the nature of the ancestral embryophyte. Curr Biol; 2018.")
CIT_TIMMIS = ("Timmis JN et al. Endosymbiotic gene transfer: organelle genomes "
              "forge eukaryotic chromosomes. Nat Rev Genet; 2004.")
CIT_ROCHAIX2 = ("Rochaix JD. Chloroplast redox regulation and the evolution "
                "of photosynthesis. (Chloroplast biology literature.)")
CIT_ELBAZ = ("Elbaz Y, Weihs D. (Synthetic biology minimal-cell literature.)")
CIT_HUTCHISON = ("Hutchison CA et al. Design and synthesis of a minimal "
                 "bacterial genome. Science; 2016.")
CIT_LONG = ("Long SP et al. Into the carbon future: engineering "
             "photosynthesis for food and fuel. (Photosynthesis "
             "optimization literature.)")
CIT_PARRY = ("Parry MAJ et al. Raising yield potential of wheat. II. "
             "Increasing photosynthetic capacity and efficiency. J Exp Bot; "
             "2011.")
CIT_TREWAVAS = ("Trewavas A. Plant intelligence: an overview. BioScience; "
                "2005.")
CIT_KEIJZER = ("Keijzer F. Moving and sensing without input and output: "
               "searching for a nervous system in plants. (Plant cognition "
               "literature.)")

ENTRIES_D = [
    {
        "key": "c4-rice",
        "name": "Engineering C4 Rice: Rewiring a Staple",
        "group": "Advanced",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": ("Rice feeds half of humanity using C3 photosynthesis. An "
                    "international consortium has spent over a decade trying to "
                    "install the C4 carbon pump into rice. Which of the dozens "
                    "of required changes are truly essential, and how will we "
                    "know when the pump is actually working?"),
        "background": (
            "The C4 Rice Project, launched with major philanthropic funding, "
            "set out to do deliberately what evolution did sixty times by "
            "accident: convert rice to C4 photosynthesis, with a projected "
            "yield gain around fifty percent. The challenge list is long: "
            "Kranz-like leaf anatomy with enlarged bundle sheaths, cell-type-"
            "specific expression of a dozen enzymes, metabolite transporters "
            "between cell types, and regulatory rewiring - all without "
            "breaking the plant. Progress includes installing parts of the "
            "biochemical pathway and proto-Kranz anatomy, but a fully "
            "functional C4 cycle in rice has not yet been demonstrated. The "
            "open strategic question is the minimal sufficient set: which "
            "changes are load-bearing and which are evolutionary decoration, "
            "because engineering all sixty-times-evolved complexity at once "
            "may be unnecessary."),
        "why_it_matters": (
            "C4 rice is the most ambitious crop-engineering project ever "
            "attempted - success would transform food security for billions. "
            "Even partial success teaches how to rewire complex plant traits "
            "by design. The project's honest accounting of what works and "
            "what does not is a public good for all of plant synthetic "
            "biology."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for finding the minimal C4 "
            "installation, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: only a subset of C4 traits is load-bearing, and a "
            "partial installation with the right subset can already pay - "
            "the project need not replicate a full C4 leaf at once. "
            "Reasoning: natural C3-C4 intermediates show stepwise gains, so "
            "engineering can climb the same staircase instead of jumping to "
            "the top. Proposed method: rank candidate changes by predicted "
            "flux gain per engineering cost using metabolic models, install "
            "them in cumulative stacks, and measure carbon-concentrating "
            "function directly with isotope discrimination at each step; "
            "stop adding complexity when marginal gains vanish. What would "
            "confirm it: a defined minimal stack producing measurable C4-"
            "like carbon concentration and yield gain. What would kill the "
            "minimalist hope: gains requiring nearly the full natural "
            "complexity, implying no shortcut exists. What this does NOT "
            "claim: it does not claim C4 rice is near, does not claim the "
            "minimal set is known, and does not propose field release - "
            "only a disciplined search strategy."),
        "citations": [CIT_VONCAEMMERER, CIT_ERMAKOVA],
        "demo_params": {"traits": 24, "installed": 9, "gain_pct": 12.0},
    },
    {
        "key": "longevity-genome",
        "name": "The Genomic Architecture of a Five-Thousand-Year Life",
        "group": "Advanced",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("Bristlecones live 5,000 years; their close relatives live "
                    "a few centuries. The longevity difference must be written "
                    "in the genome - in DNA repair, defense, and meristem "
                    "maintenance genes. What exactly is written there?"),
        "background": (
            "Conifer genomes are enormous - tens of billions of base pairs - "
            "and only recently became tractable to sequence. Comparative "
            "genomics of long-lived trees like oaks has begun revealing "
            "candidate longevity toolkits: expanded disease-resistance gene "
            "families, duplicated DNA-repair genes, and sophisticated "
            "somatic-mutation management. But bristlecone-specific genomic "
            "analysis is still young, and the field faces a hard inference "
            "problem: correlating gene-family expansions with lifespan across "
            "species is suggestive, not proof, and the experiments that "
            "would prove causation - knocking out a repair gene and waiting "
            "a thousand years - are impossible. The architecture must instead "
            "be triangulated from comparative genomics, mutation-accumulation "
            "measurements in ancient meristems, and short-lived model "
            "systems."),
        "why_it_matters": (
            "The longevity genome is the deepest available dataset on "
            "biological aging - a 5,000-year success story. Its mechanisms "
            "could inform everything from tree breeding for a changing "
            "climate to the basic biology of senescence. It also tests "
            "whether aging is a universal program or a failure mode that "
            "evolution can largely defeat."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for triangulating the longevity "
            "genome without thousand-year experiments, with adjustable "
            "assumptions and written-down confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: longevity genes reveal themselves through three "
            "independent signatures - expansion in long-lived lineages, "
            "elevated expression in ancient meristems, and low somatic "
            "mutation accumulation - and only candidates with all three "
            "deserve follow-up. Reasoning: no single signature is "
            "trustworthy, but their intersection filters coincidence. "
            "Proposed method: sequence multiple bristlecone individuals and "
            "short-lived relatives, score every maintenance gene family on "
            "the three signatures, and test top candidates by "
            "overexpression in fast-cycling models for DNA-repair and "
            "stress-tolerance phenotypes. What would confirm a longevity "
            "toolkit: candidates passing all three genomic signatures and "
            "showing protective phenotypes in models. What would kill the "
            "genomic hypothesis: no enrichment of maintenance genes in the "
            "longest-lived lineages, implying longevity is mostly "
            "ecological. What this does NOT claim: it does not claim a "
            "longevity pill, does not claim model results transfer to "
            "trees, and does not propose touching ancient groves beyond "
            "non-destructive sampling."),
        "citations": [CIT_PLOMION],
        "demo_params": {"genome_gb": 28.0, "signatures": 3, "candidates": 47},
    },
    {
        "key": "land-plant-origins",
        "name": "The Origin of Land Plants",
        "group": "Advanced",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("About 500 million years ago, green algae colonized land - "
                    "the most consequential invasion in Earth's history. "
                    "Which algal lineage gave rise to plants, in what order "
                    "did the key innovations appear, and what did the first "
                    "land plant actually look like?"),
        "background": (
            "Phylotranscriptomics converged on an answer that surprised many: "
            "the closest algal relatives of land plants are the "
            "Zygnematophyceae, a group of unassuming freshwater algae, not "
            "the more complex-looking stoneworts. The colonization required a "
            "suite of innovations - desiccation tolerance, UV protection, "
            "water-conducting tissues, stomata, and eventually roots and "
            "seeds - but their order and timing are debated, and the fossil "
            "record of the earliest embryophytes is sparse and cryptic. "
            "Recent work suggests the algal ancestors were already "
            "pre-adapted, carrying stress-tolerance genes later repurposed "
            "for land. The deepest question is causal: did new genes drive "
            "the invasion, or did old genes find new jobs in a new "
            "environment?"),
        "why_it_matters": (
            "Every terrestrial ecosystem - forests, farms, grasslands - "
            "descends from this single transition. Understanding it explains "
            "the deep structure of plant biology: why plants are built the "
            "way they are. The pre-adaptation story also matters for "
            "astrobiology and for engineering crops for extreme "
            "environments: the genes for surviving the impossible may "
            "already exist, waiting for new jobs."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for reconstructing the land "
            "invasion, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: the innovation order can be read from living "
            "species - the traits shared by land plants and their algal "
            "sisters predate the invasion, and land-only traits postdate it. "
            "Reasoning: phylogenetic bracketing is the only available time "
            "machine, and the newly resolved algal sister group makes the "
            "brackets tight. Proposed method: reconstruct the gene-family "
            "history across the zygnematophyte-to-embryophyte transition, "
            "date each innovation's origin, and test pre-adaptation by "
            "expressing ancestral-state genes in modern algae under "
            "desiccation stress. What would confirm the pre-adaptation "
            "story: algal genes conferring land-like stress tolerance when "
            "tested. What would kill it: the key innovations requiring "
            "novel genes with no algal precursors, implying true invention "
            "on land. What this does NOT claim: it does not claim the "
            "fossil record will confirm the dates, does not claim one "
            "single ancestor species, and does not propose resurrecting "
            "ancient plants."),
        "citations": [CIT_WICKETT, CIT_PUTTICK],
        "demo_params": {"mya": 500.0, "innovations": 9, "preadapted": 6},
    },
    {
        "key": "endosymbiosis",
        "name": "The Chloroplast's Long Journey: Full Endosymbiosis Mechanics",
        "group": "Advanced",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("A cyanobacterium engulfed by an ancient cell became the "
                    "chloroplast - then surrendered most of its genes to the "
                    "host nucleus. How did thousands of genes migrate, how is "
                    "the divided genome coordinated today, and could it happen "
                    "again?"),
        "background": (
            "Endosymbiotic gene transfer is one of evolution's great "
            "migrations: modern chloroplasts retain barely a hundred genes, "
            "while over a thousand chloroplast proteins are encoded in the "
            "nucleus, synthesized in the cytosol, and imported back. The "
            "transfer machinery - how genes physically moved, how import "
            "targeting evolved, and how the host took regulatory control - "
            "is reconstructed from comparative genomics but has never been "
            "watched happening. Remarkably, the process continues: DNA still "
            "escapes from chloroplasts to the nucleus in modern plants. Open "
            "questions include why a small genome stubbornly remains in the "
            "chloroplast at all, how the two genomes stay coordinated under "
            "stress, and whether the import machinery could be repurposed to "
            "install entirely new functions into chloroplasts."),
        "why_it_matters": (
            "The chloroplast is the precedent for the most radical "
            "engineering imaginable: installing a new organelle. "
            "Understanding how the host tamed the endosymbiont teaches how "
            "to domesticate engineered ones - including synthetic "
            "chloroplasts. The coordination problem is also live "
            "agriculture: stress scrambles nucleus-chloroplast communication, "
            "and yield depends on keeping them in sync."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for mapping endosymbiosis "
            "mechanics, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: the retained chloroplast genes stay because their "
            "products must be made on-site for redox regulation - the "
            "leading hypothesis - and this predicts which genes can never "
            "be moved. Reasoning: if on-site synthesis is the reason, the "
            "retained set should be exactly the redox-regulatory core "
            "across all lineages. Proposed method: compare retained gene "
            "sets across the full diversity of plastids, test whether the "
            "intersection matches redox-core predictions, and experimentally "
            "relocate a retained gene to the nucleus with proper targeting "
            "to see whether regulation breaks. What would confirm it: "
            "relocated redox genes failing under fluctuating light while "
            "non-redox relocations succeed. What would kill it: clean "
            "relocation of the entire retained set with no regulatory cost, "
            "implying retention is historical accident. What this does NOT "
            "claim: it does not claim new endosymbioses are imminent, does "
            "not claim the transfer history is fully known, and does not "
            "propose relocating genes in crops yet."),
        "citations": [CIT_TIMMIS],
        "demo_params": {"retained": 110, "transferred": 1200, "redox_core": 68},
    },
    {
        "key": "synthetic-chloroplast",
        "name": "Synthetic Chloroplasts Built From Scratch",
        "group": "Advanced",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("Could a photosynthetic organelle be built bottom-up - a "
                    "minimal light-harvesting, carbon-fixing compartment "
                    "installed into a non-photosynthetic cell? What is the "
                    "smallest part list that still does photosynthesis?"),
        "background": (
            "Synthetic biology has built minimal bacterial genomes and "
            "redesigned metabolic pathways, but no one has built a "
            "chloroplast from scratch. The part list is daunting: "
            "photosystems with dozens of subunits, electron carriers, "
            "ATP synthase, the Calvin cycle's eleven enzymes, plus the "
            "import, assembly, and repair machinery - and all of it must "
            "be coordinated with the host cell. Partial efforts exist: "
            "researchers have installed individual photosynthetic "
            "components into non-photosynthetic hosts and built "
            "artificial light-harvesting vesicles. The field lacks even a "
            "consensus minimal part list, let alone an assembly order, and "
            "the repair problem looms large - natural photosystems "
            "constantly rebuild their damaged cores, a maintenance burden "
            "a synthetic system must also carry."),
        "why_it_matters": (
            "A working synthetic chloroplast would be a platform technology: "
            "solar-powered chemistry inside any cell, from carbon-fixing "
            "microbes to light-driven drug factories. It is also the "
            "ultimate test of whether we truly understand photosynthesis - "
            "building it proves the understanding. The part list alone "
            "would discipline the whole field."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for defining the minimal synthetic "
            "chloroplast, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: the minimal system must include the repair cycle, "
            "not just the working parts - a photosystem without its repair "
            "machinery dies within hours in light. Reasoning: natural "
            "photosystems turn over their D1 core protein constantly; any "
            "parts list omitting repair is a parts list for a dead "
            "chloroplast. Proposed method: enumerate candidate minimal "
            "part lists from comparative genomics of reduced plastids, "
            "score each for completeness of the repair cycle, and test "
            "assembly stepwise in a tractable host - first light-driven "
            "electron flow, then carbon fixation, then repair - requiring "
            "each stage to persist before adding the next. What would "
            "confirm feasibility: a staged system reaching persistent "
            "light-driven carbon fixation. What would kill the near-term "
            "dream: repair machinery proving irreducibly complex, with no "
            "stable intermediate stages. What this does NOT claim: it does "
            "not claim a timeline, does not claim the part list is known, "
            "and does not propose environmental release of synthetic "
            "photosynthesizers."),
        "citations": [CIT_HUTCHISON],
        "demo_params": {"parts": 320, "repair_parts": 45, "stages": 3},
    },
    {
        "key": "photosynthesis-optimization",
        "name": "The Complete Mechanics of Photosynthesis Optimization",
        "group": "Advanced",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("Photosynthesis is a pipeline of dozens of steps - light "
                    "capture, electron transport, carbon fixation - each "
                    "optimized by evolution for survival, not for maximum "
                    "yield. What does the fully optimized pipeline look like, "
                    "and which steps limit the whole system under real field "
                    "conditions?"),
        "background": (
            "Systems analyses treat photosynthesis as a supply chain and ask "
            "which step is rate-limiting - but the answer changes with "
            "light, temperature, carbon dioxide, and time of day. Under "
            "bright light Rubisco capacity limits; under dim light electron "
            "transport limits; under flickering light the regulatory lags "
            "limit. Modelers have built whole-photosynthesis simulations "
            "that reproduce these shifts, and targeted improvements - faster "
            "photoprotection relaxation, photorespiration bypasses, improved "
            "electron sinks - have each delivered field gains. What is "
            "missing is the integrated optimum: the combination of "
            "improvements that jointly maximizes yield, accounting for "
            "interactions, tradeoffs, and the fact that evolution already "
            "tuned the system for robustness rather than output. This is the "
            "capstone optimization problem of plant biology."),
        "why_it_matters": (
            "This is the master calculation behind feeding the future: the "
            "joint optimum sets the true ceiling of what photosynthesis can "
            "deliver. It tells engineers which combinations to build and "
            "which single-trait hype to ignore. Solving it would be the "
            "culmination of a century of photosynthesis research - and the "
            "blueprint for the crops of 2050."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for computing the joint optimum of "
            "photosynthesis, with adjustable assumptions and written-down "
            "confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: the joint optimum can be found by optimizing a "
            "validated whole-system model over realistic weather ensembles, "
            "and the optimum is robust - nearby designs perform similarly. "
            "Reasoning: if the optimum is a sharp peak, it is "
            "unengineerable; only a broad plateau is a useful target. "
            "Proposed method: couple the best available photosynthesis, "
            "canopy, and crop models; optimize trait combinations over "
            "multi-year weather ensembles for target regions; test the "
            "robustness of the optimum by perturbing parameters; then build "
            "the top-ranked trait stacks in test lines and measure field "
            "performance. What would confirm it: stacked lines matching "
            "model-predicted gains across weather years. What would kill "
            "the model-first approach: persistent prediction failures "
            "implying unmodeled interactions dominate. What this does NOT "
            "claim: it does not claim the models are already good enough, "
            "does not promise a specific yield number, and does not propose "
            "skipping field validation."),
        "citations": [CIT_LONG, CIT_PARRY],
        "demo_params": {"steps": 40, "traits": 8, "ensemble_years": 30},
    },
    {
        "key": "denovo-photosynthesizer",
        "name": "Designing a De Novo Photosynthetic Organism",
        "group": "Advanced",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("What is the simplest possible organism that does oxygenic "
                    "photosynthesis? Stripping a cyanobacterium to its "
                    "photosynthetic essentials would reveal the true minimal "
                    "design - and nobody has finished the job."),
        "background": (
            "The minimal-bacterium project reduced a mycoplasma to fewer than "
            "500 genes, proving life can run on a surprisingly small program. "
            "No equivalent exists for photosynthesis: cyanobacterial genomes "
            "carry thousands of genes, and which are truly essential for "
            "light-driven growth is unknown. Knockout collections cover model "
            "cyanobacteria incompletely, and essentiality shifts with light "
            "and nutrient conditions. A minimal photosynthesizer would answer "
            "a profound question - how much machinery does sunlight-to-life "
            "actually require - and provide the cleanest possible chassis "
            "for engineering: every remaining gene understood, every "
            "interaction mapped."),
        "why_it_matters": (
            "A minimal photosynthetic chassis would be the ideal platform "
            "for solar-powered biotechnology: carbon capture, biofuels, and "
            "chemical production with a fully understood host. Scientifically, "
            "it defines the lower bound of photosynthetic complexity - the "
            "answer to 'what is the least that works.' It is also a "
            "dry run for recognizing truly alien photosynthesis."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for minimizing the photosynthetic "
            "genome, with adjustable assumptions and written-down confirm and "
            "refute conditions."),
        "sig_solution": (
            "Assumptions: essentiality must be measured under the target "
            "condition - stable moderate light - because genes essential in "
            "fluctuating light may be dispensable in constant light, and the "
            "minimal genome is condition-specific. Reasoning: a 'minimal' "
            "genome defined without stating the environment is meaningless; "
            "robustness genes are only essential when the environment "
            "demands them. Proposed method: complete the knockout collection "
            "in a model cyanobacterium, score essentiality under defined "
            "constant-light chemostat conditions, synthesize the reduced "
            "genome, and boot it up; then add back robustness modules one "
            "by one to map the cost of real-world tolerance. What would "
            "confirm it: a booted minimal strain growing photosynthetically "
            "with a fully annotated gene list. What would kill the clean "
            "vision: essentiality so condition-dependent that no stable "
            "minimal set exists. What this does NOT claim: it does not claim "
            "the minimal strain is useful outdoors, does not claim the "
            "knockout map is complete, and does not propose environmental "
            "release."),
        "citations": [CIT_HUTCHISON],
        "demo_params": {"genes": 3200, "essential": 580, "booted": 1},
    },
    {
        "key": "plant-consciousness",
        "name": "Plant Consciousness: The Hardest Question in Botany",
        "group": "Advanced",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("Plants integrate information, remember, anticipate, and "
                    "communicate - the functional ingredients often linked to "
                    "consciousness. Is there anything it is like to be a plant? "
                    "This is botany's hardest question, and it may be "
                    "unanswerable in principle."),
        "background": (
            "The question sits at the collision of plant physiology and the "
            "philosophy of mind. The empirical side keeps advancing: plants "
            "show habituation, associative learning, risk-sensitive decisions, "
            "and whole-plant electrical coordination. The philosophical side "
            "asks what would even count as evidence: integrated information "
            "theory suggests any sufficiently integrated system has some "
            "degree of experience, while critics note that thermostats also "
            "integrate information and nobody worries about their feelings. "
            "Some researchers propose operational criteria - flexible "
            "goal-directed behavior under novelty - while others argue "
            "consciousness requires a nervous system by definition. The "
            "honest state of the field: the empirical phenomena are real and "
            "growing, the theoretical frameworks disagree irreconcilably, and "
            "no experiment currently imaginable could settle it to "
            "everyone's satisfaction."),
        "why_it_matters": (
            "The answer would reorder ethics, agriculture, and our place in "
            "nature: moral consideration for plants would transform how "
            "humanity treats the organisms that feed it. Even a rigorous "
            "'we cannot know' would be progress - it would end confused "
            "debate and focus research on the answerable questions. And the "
            "question is a mirror: in asking what it is like to be a plant, "
            "we are forced to say what we mean by experience at all."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for making the hardest question "
            "answerable - or proving it is not, with adjustable assumptions "
            "and written-down confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: the question must first be operationalized - "
            "'consciousness' replaced by a ladder of observable capacities - "
            "because the unoperationalized question cannot be tested. "
            "Reasoning: centuries of philosophy show the raw question "
            "dissolves into definitions; progress requires climbing a "
            "ladder of capacities, each testable, and seeing how high "
            "plants climb. Proposed method: define the capacity ladder - "
            "sensing, integration, memory, flexible learning, "
            "self-modeling - pre-register behavioral criteria for each "
            "rung, test plants double-blind, and separately convene "
            "philosophers to state in advance which rung, if reached, "
            "would change their verdict; publish both results together. "
            "What would confirm progress: plants clearing rungs the "
            "skeptics said they could not, with criteria agreed in "
            "advance. What would kill the strong claim: plants stalling "
            "at integration with no flexible self-modeling under any "
            "paradigm. What this does NOT claim: it does not claim the "
            "ladder equals consciousness, does not claim any rung proves "
            "inner experience, and does not propose moral rules for "
            "plants - only an honest, pre-registered climb."),
        "citations": [CIT_TREWAVAS, CIT_KEIJZER],
        "demo_params": {"rungs": 5, "cleared": 3, "blinded": 1},
    },
]
