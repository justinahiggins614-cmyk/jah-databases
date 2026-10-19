#!/usr/bin/env python3
"""Entries 18-26 (ladder ranks 18-26, Compounded tail + Advanced) for the
Unsolved Botany databases."""

CIT_SAGE = ("Sage RF. The evolution of C4 photosynthesis. New Phytol; 2004.")
CIT_EDWARDS = ("Edwards EJ et al. C4 photosynthesis and the evolutionary "
               "assembly of a complex trait. Curr Opin Plant Biol; 2010.")
CIT_SOUTH = ("South PF et al. Synthetic glycolate metabolism pathways "
             "stimulate crop growth and productivity in the field. Science; 2019.")
CIT_PETERHANSEL = ("Peterhansel C et al. Photorespiration. Arabidopsis Book; "
                   "2010.")
CIT_BEATTY = ("Beatty PH, Good AG. Future prospects for cereals that fix "
              "nitrogen. Science; 2011.")
CIT_OLDROYD = ("Oldroyd GED. Speak, friend, and enter: signalling systems that "
               "promote beneficial symbiotic associations in plants. Nat Rev "
               "Microbiol; 2013.")
CIT_ROCHAIX = ("Rochaix JD. Regulation and dynamics of the light-harvesting "
               "system. Annu Rev Plant Biol; 2014.")
CIT_MULLER = ("Muller P et al. Non-photochemical quenching. A response to "
              "excess light energy. Plant Physiol; 2001.")
CIT_HEARD = ("Heard E, Martienssen RA. Transgenerational epigenetic "
             "inheritance: myths and mechanisms. Cell; 2014.")
CIT_PASZKOWSKI = ("Paszkowski J, Grossniklaus U. Selected aspects of "
                  "transgenerational epigenetic inheritance and resetting in "
                  "plants. Curr Opin Plant Biol; 2011.")
CIT_FROMM = ("Fromm J, Lautner S. Electrical signals and their physiological "
             "significance in plants. Plant Cell Environ; 2007.")
CIT_ZIMMERMANN = ("Zimmermann MR et al. Systemic signalling and adaptive "
                   "responses in plants. Trends Plant Sci; 2009.")
CIT_ZHU = ("Zhu XG et al. What is the maximum efficiency with which "
           "photosynthesis can convert solar energy into biomass? Curr Opin "
           "Biotechnol; 2008.")
CIT_ORT = ("Ort DR et al. Redesigning photosynthesis to sustainably meet "
           "global food and bioenergy demand. Proc Natl Acad Sci; 2015.")
CIT_TCHERKEZ = ("Tcherkez GGB et al. Despite slow catalysis and confused "
                "substrate specificity, all ribulose bisphosphate "
                "carboxylases may be nearly perfectly optimized. Proc Natl "
                "Acad Sci; 2006.")

ENTRIES_C = [
    {
        "key": "c4-convergence",
        "name": "Why C4 Photosynthesis Evolved More Than Sixty Times",
        "group": "Compounded",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("C4 photosynthesis - the turbocharged carbon pump used by "
                    "maize and sugarcane - evolved independently more than sixty "
                    "times in different plant families. What preconditions make "
                    "a lineage ready to reinvent it, and why did so many succeed?"),
        "background": (
            "C4 plants concentrate carbon dioxide around Rubisco, suppressing "
            "wasteful photorespiration and thriving in hot, dry climates. The "
            "astonishing fact is its repeatability: at least sixty independent "
            "origins across grasses, sedges, and eudicots, each assembling "
            "similar anatomy and biochemistry from different starting points. "
            "Evolutionary studies revealed a pattern of enabling preconditions - "
            "certain anatomical and physiological traits that precede each "
            "origin - suggesting C4 is less an invention than an attractor "
            "that lineages fall into. But the full enabling sequence, why some "
            "preconditioned lineages never made the jump, and the exact order "
            "of the dozens of required changes, remain incompletely resolved. "
            "Each origin is a natural replicate experiment in complex-trait "
            "evolution, and the dataset keeps growing."),
        "why_it_matters": (
            "If evolution reinvented C4 sixty times, engineers might manage it "
            "once - in rice. The C4 rice project aims to install the carbon "
            "pump into the world's most important food crop, and the natural "
            "origins are the instruction manual. Understanding convergence also "
            "answers a deep question: how predictable is evolution?"),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for reading the C4 instruction manual, "
            "with adjustable assumptions and written-down confirm and refute "
            "conditions."),
        "sig_solution": (
            "Assumptions: every C4 origin follows the same enabling sequence - "
            "anatomical preconditions first, then biochemical recruitment - and "
            "the order is constrained, not free. Reasoning: if the sequence is "
            "constrained, intermediate species (C3-C4 intermediates) should "
            "cluster at the same waystations across independent origins. "
            "Proposed method: assemble the trait-state sequences of all known "
            "C3-C4 intermediate lineages, test whether waystations are shared "
            "across origins more than chance allows, and reconstruct the "
            "minimal enabling order; then check whether preconditioned "
            "non-C4 lineages are missing a specific predicted step. What would "
            "confirm it: a single dominant waystation sequence shared across "
            "most origins. What would kill it: origins reaching C4 by "
            "scrambled, lineage-specific routes with no shared order. What this "
            "does NOT claim: it does not claim C4 engineering is around the "
            "corner, does not claim all sixty origins are fully documented, "
            "and does not propose installing C4 until the enabling sequence is "
            "confirmed."),
        "citations": [CIT_SAGE, CIT_EDWARDS],
        "demo_params": {"origins": 62, "waystations": 4, "shared": 0.78},
    },
    {
        "key": "photorespiration",
        "name": "Photorespiration: The Wasteful Flaw",
        "group": "Compounded",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("Rubisco, the enzyme that captures carbon dioxide, "
                    "frequently grabs oxygen instead - forcing plants to run "
                    "photorespiration, a costly salvage pathway that can waste a "
                    "quarter of photosynthetic energy. Can this ancient flaw be "
                    "fixed, bypassed, or removed?"),
        "background": (
            "Photorespiration is evolution's legacy bug: Rubisco evolved when "
            "the atmosphere had almost no oxygen, and it never fully learned "
            "to tell oxygen from carbon dioxide. The salvage pathway spans "
            "three organelles and burns energy to recover the carbon, "
            "reducing yields - especially in hot weather, when oxygenation "
            "worsens. For decades textbooks called it unavoidable; then "
            "engineers built synthetic bypasses - shortcut pathways that "
            "metabolize the toxic byproduct more cheaply - and field trials "
            "showed real biomass gains. But the bypasses are add-ons, not "
            "fixes: the ideal solution, a Rubisco that stops confusing the "
            "two gases or a plant that never oxygenates, remains elusive, "
            "and some evidence suggests photorespiration also serves "
            "protective roles that a naive deletion would destroy."),
        "why_it_matters": (
            "Photorespiration is one of the largest single efficiency losses "
            "in global agriculture - recovering even part of it would be "
            "worth millions of tons of grain. It is also a test case for "
            "whether evolution's 'good enough' solutions can be beaten by "
            "design. The protective-role evidence is a warning: optimization "
            "without understanding breaks things."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for taming photorespiration safely, "
            "with adjustable assumptions and written-down confirm and refute "
            "conditions."),
        "sig_solution": (
            "Assumptions: the safe target is the salvage pathway's efficiency, "
            "not Rubisco's chemistry - evolution has already explored Rubisco "
            "sequence space for billions of years. Reasoning: bypass "
            "experiments improved yields without touching Rubisco, while "
            "Rubisco engineering has repeatedly hit the "
            "speed-versus-specificity tradeoff. Proposed method: systematically "
            "compare synthetic bypass designs for energy cost and side effects "
            "under combined heat and drought, measure any loss of the "
            "proposed protective functions, and select bypasses whose gains "
            "persist across stresses and seasons. What would confirm it: a "
            "bypass that raises yield under all tested stresses with no "
            "protective-function penalty. What would kill it: every bypass "
            "showing hidden costs under some stress, implying the native "
            "pathway's inefficiency is load-bearing. What this does NOT claim: "
            "it does not claim Rubisco cannot be improved, does not claim "
            "bypasses are risk-free, and does not propose deployment until "
            "multi-stress field data exist."),
        "citations": [CIT_SOUTH, CIT_PETERHANSEL],
        "demo_params": {"waste_fraction": 0.25, "bypass_gain": 0.15, "stresses": 4},
    },
    {
        "key": "nitrogen-fixation-cereals",
        "name": "Nitrogen Fixation for Cereals",
        "group": "Compounded",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("Legumes host bacteria that pull nitrogen from the air, but "
                    "cereals - wheat, rice, maize - cannot. They depend on "
                    "synthetic fertilizer made with fossil fuels. Can cereals be "
                    "given the power to fix their own nitrogen?"),
        "background": (
            "The Haber-Bosch process feeds roughly half of humanity and "
            "consumes a few percent of global energy while polluting waterways "
            "with runoff. Legumes escape this through root nodules housing "
            "nitrogen-fixing rhizobia - a symbiosis built on an elaborate "
            "molecular dialogue. Two engineering routes are pursued: transfer "
            "the nodulation program into cereals, or engineer cereals to "
            "associate with free-living nitrogen fixers. Both face the oxygen "
            "problem - the nitrogenase enzyme is destroyed by oxygen, yet "
            "roots need oxygen - and the energy problem, since fixation is "
            "expensive and cereals run on thin margins. Progress is real but "
            "incremental: signaling steps have been transferred, associative "
            "fixers show modest contributions, and no cereal yet fixes "
            "agronomically meaningful nitrogen on its own."),
        "why_it_matters": (
            "Self-fertilizing cereals would be among the most valuable "
            "inventions in agricultural history - slashing energy use, "
            "fertilizer costs, and nutrient pollution at once, especially for "
            "smallholder farmers who cannot afford fertilizer. It is also the "
            "grand challenge of symbiosis engineering: installing a whole "
            "organ-level partnership by design."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for engineering cereal nitrogen "
            "fixation, with adjustable assumptions and written-down confirm and "
            "refute conditions."),
        "sig_solution": (
            "Assumptions: the viable path is enhancing associative fixation by "
            "root-associated bacteria, not building full nodules - nodules are "
            "a developmental program of daunting complexity, while association "
            "already occurs at low levels. Reasoning: evolution built nodules "
            "once in legumes over millions of years; the nearer engineering "
            "target is upgrading an existing weak interaction. Proposed "
            "method: screen cereal varieties for root exudates that best feed "
            "diazotrophs, breed for exudate chemistry that recruits them, and "
            "engineer the bacteria for oxygen-protected nitrogenase; measure "
            "fixed nitrogen with isotope dilution in field plots. What would "
            "confirm it: isotope-proven fixation supplying a substantial "
            "fraction of crop nitrogen across seasons. What would kill it: "
            "fixed nitrogen stuck at a few percent regardless of exudate or "
            "bacterial engineering, implying a hard energetic ceiling. What "
            "this does NOT claim: it does not claim nodules in cereals are "
            "impossible, does not claim associative fixation will replace "
            "fertilizer soon, and does not propose release until field "
            "nitrogen budgets are proven."),
        "citations": [CIT_BEATTY, CIT_OLDROYD],
        "demo_params": {"n_need_kg_ha": 150.0, "fixed_kg_ha": 25.0, "oxygen_limit": 0.4},
    },
    {
        "key": "photoprotection",
        "name": "How Leaves Rewire Light Capture",
        "group": "Compounded",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("Full sunlight delivers far more energy than photosynthesis "
                    "can use, and the surplus can destroy the machinery. Leaves "
                    "defend themselves with non-photochemical quenching - "
                    "dumping excess energy as heat - but the full dynamics of "
                    "this photoprotective rewiring, and its cost to yield, are "
                    "still being worked out."),
        "background": (
            "The light reactions of photosynthesis saturate at a fraction of "
            "full sunlight; beyond that, excess excitation generates reactive "
            "oxygen that damages photosystem II. Plants respond with a suite of "
            "quenching mechanisms, the fastest governed by the PsbS protein "
            "and the xanthophyll cycle, which reversibly reconfigure the "
            "light-harvesting antennae to shed energy as heat. The system has "
            "a lag problem: quenching switches on fast in bright light but "
            "relaxes slowly in shade, so leaves in flickering light waste "
            "usable photons. Engineers who sped up the relaxation recovered "
            "significant biomass in field trials. Yet the complete control "
            "logic - how the many quenching components are coordinated, what "
            "sets their kinetics, and how much yield is truly lost to the lag "
            "- remains an active frontier."),
        "why_it_matters": (
            "Flickering light is the normal condition of every crop canopy, so "
            "the quenching lag taxes global yields every day. Tuning "
            "photoprotection is one of the few proven routes to raising "
            "photosynthetic efficiency in the field. The control logic is "
            "also a beautiful example of real-time energy management without "
            "a central controller."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for tuning photoprotection without "
            "losing safety, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: the quenching system is over-conservative by design - "
            "it protects against rare extreme light at the cost of common "
            "moderate light - so there is tunable headroom. Reasoning: "
            "relaxation-speedup experiments gained yield without apparent "
            "damage, implying the safety margin exceeds what field conditions "
            "require. Proposed method: map quenching kinetics across diverse "
            "genotypes under realistic flicker regimes, identify the "
            "genetic knobs controlling relaxation speed, and test tuned lines "
            "for both yield gain and damage markers under combined light and "
            "drought stress. What would confirm it: tuned lines gaining yield "
            "with damage markers indistinguishable from controls across "
            "stresses. What would kill it: yield gains that always come with "
            "elevated damage under some stress, implying the margin is already "
            "optimal. What this does NOT claim: it does not claim all "
            "quenching is wasteful, does not claim one tuning fits all "
            "climates, and does not propose deployment until stress-tested."),
        "citations": [CIT_ROCHAIX, CIT_MULLER],
        "demo_params": {"lag_minutes": 12.0, "flicker_gain": 0.14, "damage_index": 1.0},
    },
    {
        "key": "epigenetic-memory",
        "name": "The Epigenetic Memory of Plants",
        "group": "Compounded",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("Plants exposed to stress sometimes produce offspring that "
                    "handle the same stress better - without any change in DNA "
                    "sequence. How much of this transgenerational memory is real, "
                    "how is it written and erased, and can breeders rely on it?"),
        "background": (
            "The vernalization system proves plants can hold epigenetic memory "
            "within a lifetime, but memory across generations is far more "
            "contested. Experiments report stress-primed offspring in several "
            "species, with DNA methylation and small RNAs as candidate "
            "carriers - yet plants aggressively reset epigenetic marks during "
            "reproduction, and many striking claims have failed to replicate "
            "or faded within a generation or two. The field now distinguishes "
            "carefully: intergenerational effects (mother's environment shaping "
            "seed provisioning) are common and real, while true "
            "transgenerational epigenetic inheritance - marks surviving the "
            "embryonic reset for multiple unstressed generations - has only a "
            "handful of solid cases. The molecular rules of what survives the "
            "reset, and why, are still being established."),
        "why_it_matters": (
            "If stress memory could be reliably inherited, breeders could prime "
            "crops for drought or heat without changing a single gene - and "
            "seed companies could sell 'trained' seed. If it cannot, chasing it "
            "wastes effort better spent on genetics. Either answer reshapes "
            "breeding strategy, and the question tests the limits of the "
            "modern synthesis itself."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for separating real epigenetic memory "
            "from maternal effects, with adjustable assumptions and written-down "
            "confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: most reported cases are maternal provisioning effects, "
            "and the honest path is a strict experimental filter that separates "
            "them from true epigenetic inheritance. Reasoning: seed size, "
            "nutrient loading, and seed-coat effects all flow from mother to "
            "offspring without any epigenetic mark, and they explain many "
            "claimed memories. Proposed method: run candidate stress-memory "
            "lines through reciprocal crosses, embryo rescue, and "
            "multiple unstressed generations with molecular tracking of "
            "methylation marks; only marks that survive the reset and "
            "co-segregate with the phenotype count. What would confirm real "
            "inheritance: marks and phenotypes persisting three unstressed "
            "generations after embryo rescue. What would kill a claim: the "
            "effect vanishing after controlling for seed provisioning. What "
            "this does NOT claim: it does not claim transgenerational memory "
            "is impossible, does not dismiss the solid cases, and does not "
            "propose 'trained seed' products until the filter is passed."),
        "citations": [CIT_HEARD, CIT_PASZKOWSKI],
        "demo_params": {"generations": 3, "reset_rate": 0.92, "maternal_share": 0.7},
    },
    {
        "key": "plant-electricity",
        "name": "The Electrical Language of Plants",
        "group": "Compounded",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("Wound a leaf and an electrical signal races through the "
                    "plant, switching on defenses in distant tissues within "
                    "minutes. Plants use action potentials, calcium waves, and "
                    "hydraulic signals - but the full vocabulary of this "
                    "electrical language, and how much information it really "
                    "carries, is unknown."),
        "background": (
            "Plant electrophysiology dates to the 19th century, but only "
            "modern imaging revealed its richness: glutamate-triggered calcium "
            "waves sweeping through wounded leaves, slow wave potentials "
            "traveling the vasculature, and rapid systemic signals coordinating "
            "defense across the whole plant. The Venus flytrap's counting "
            "shows plants can encode numbers electrically. Yet fundamental "
            "questions persist: how many distinct signal types exist, whether "
            "different stresses produce distinguishable electrical signatures "
            "or just one generic alarm, how the signals are decoded at their "
            "destination, and whether the electrical network integrates "
            "information the way a nervous system does or merely broadcasts "
            "alerts. The instrumentation to eavesdrop on whole-plant "
            "electrical chatter in the field barely exists."),
        "why_it_matters": (
            "Cracking the electrical code would give agriculture an early "
            "warning system: electrodes detecting pest attack or drought "
            "stress before visible symptoms. It would also settle how "
            "close plants come to genuine signal integration - the empirical "
            "core of the cognition debate. A plant's electrical chatter may "
            "be the richest undecoded communication channel in biology."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for decoding plant electrical "
            "signals, with adjustable assumptions and written-down confirm and "
            "refute conditions."),
        "sig_solution": (
            "Assumptions: different stresses produce measurably different "
            "electrical signatures, and the plant's response machinery can "
            "tell them apart. Reasoning: a single generic alarm cannot explain "
            "stress-specific defense responses; the decoding machinery must "
            "extract more than 'something happened.' Proposed method: record "
            "surface potentials and calcium waves during controlled wounding, "
            "drought, heat, and pathogen attack; train classifiers on the "
            "waveforms; then test whether the plant's own gene-expression "
            "response matches the classifier's stress identification. What "
            "would confirm a real vocabulary: classifiers that identify the "
            "stressor from the signal alone, with plant responses matching. "
            "What would kill it: all stresses producing one indistinguishable "
            "alarm with specificity added later by local chemistry. What this "
            "does NOT claim: it does not claim plants feel the signals, does "
            "not claim a plant brain, and does not propose field electrodes "
            "until the vocabulary is validated."),
        "citations": [CIT_FROMM, CIT_ZIMMERMANN],
        "demo_params": {"signal_types": 4, "classifier_acc": 0.86, "speed_cm_min": 8.0},
    },
    {
        "key": "field-efficiency-gap",
        "name": "The Field Efficiency Gap: Why Crops Capture Barely One Percent of Sunlight",
        "group": "Advanced",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "problem": ("Theory says C3 crops could convert over four percent of "
                    "sunlight into biomass; real fields manage about one "
                    "percent. Where exactly does the other three-quarters go, "
                    "and how much of the gap is truly recoverable?"),
        "background": (
            "Energy-budget analyses trace sunlight's fate step by step: half "
            "the spectrum is unusable, most of the rest misses the canopy or "
            "arrives when leaves are saturated, and respiration, "
            "photorespiration, and incomplete canopy closure take further "
            "cuts. The theoretical maximum for C3 photosynthesis is around "
            "4.6 percent of total solar energy; the best crops in the best "
            "years reach roughly a third of that, and average fields far "
            "less. Each loss has been measured, but the losses interact: "
            "closing the canopy earlier changes water use, speeding "
            "photoprotection changes stress tolerance. No integrated model "
            "yet shows which combination of improvements is jointly "
            "achievable, so the recoverable fraction of the gap - the number "
            "that decides how much food the planet can grow - remains an "
            "open systems question."),
        "why_it_matters": (
            "The recoverable gap is the ceiling of future food production "
            "without new farmland. If half the gap can be closed, feeding ten "
            "billion people gets dramatically easier; if only a tenth can, "
            "the world needs a different plan. Every proposed "
            "photosynthesis improvement should be judged against this "
            "budget - it is the scoreboard for the entire field."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for auditing the efficiency gap, with "
            "adjustable assumptions and written-down confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: the losses can be ranked by joint recoverability - "
            "some are thermodynamically hard, others are merely unoptimized - "
            "and the ranking is stable across environments. Reasoning: "
            "single-loss analyses overpromise because they ignore "
            "interactions; only a coupled budget reveals the true headroom. "
            "Proposed method: build a coupled canopy-photosynthesis model "
            "with every major loss term, calibrate it against multi-year "
            "field energy budgets, then computationally close each loss alone "
            "and in combination to rank joint recoverability; validate the "
            "top-ranked combinations with targeted field experiments. What "
            "would confirm it: model predictions matching measured gains when "
            "combinations are actually built. What would kill it: persistent "
            "mismatch between predicted and realized gains, implying unknown "
            "loss terms or interactions. What this does NOT claim: it does "
            "not claim the theoretical maximum is reachable, does not promise "
            "any specific yield gain, and does not propose engineering "
            "targets until the audit is validated."),
        "citations": [CIT_ZHU, CIT_ORT],
        "demo_params": {"theoretical": 4.6, "field": 1.1, "recoverable": 1.4},
    },
    {
        "key": "rubisco-engineering",
        "name": "Rubisco: Engineering the World's Slowest Enzyme",
        "group": "Advanced",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": ("Rubisco fixes carbon dioxide at a glacial few reactions per "
                    "second and cannot reliably distinguish it from oxygen. "
                    "Billions of years of evolution have not fixed it. Can "
                    "engineering succeed where evolution stalled - or is Rubisco "
                    "already optimal?"),
        "background": (
            "Rubisco is the most abundant protein on Earth and arguably the "
            "worst important enzyme: slow, confused by oxygen, and so "
            "inefficient that plants manufacture it in enormous quantities to "
            "compensate. Surveys of natural Rubiscos reveal a cruel tradeoff: "
            "faster versions are less picky about carbon dioxide, and pickier "
            "versions are slower - suggesting evolution has already pushed "
            "each lineage to its local optimum. Engineering efforts include "
            "transplanting faster algal Rubiscos into crops, directed "
            "evolution in the lab, and computational redesign; results so far "
            "are modest, and the tradeoff curve has not been broken. A "
            "provocative analysis argues all Rubiscos may be nearly perfectly "
            "optimized given their chemistry - in which case the enzyme is "
            "not a flaw to fix but a constraint to design around."),
        "why_it_matters": (
            "If the tradeoff can be broken, every photosynthetic organism "
            "gets faster - the single highest-leverage enzyme edit in "
            "biology. If it cannot, the field must redirect effort toward "
            "bypasses and carbon-concentrating mechanisms instead of "
            "wasting decades on an impossible enzyme. Knowing which is true "
            "is worth billions in research direction alone."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for testing whether Rubisco can be "
            "beaten, with adjustable assumptions and written-down confirm and "
            "refute conditions."),
        "sig_solution": (
            "Assumptions: the honest test is whether any engineered Rubisco "
            "beats the natural tradeoff curve, not whether it beats one "
            "reference enzyme. Reasoning: beating a slow reference while "
            "staying on the tradeoff curve proves nothing; the curve itself "
            "is the hypothesis under test. Proposed method: plot turnover "
            "rate against specificity for the full natural diversity plus "
            "all engineered variants, fit the tradeoff frontier, and score "
            "each new design by its distance beyond the frontier; require "
            "winners to function inside living chloroplasts, not just in "
            "test tubes. What would confirm breakability: engineered "
            "variants sitting clearly beyond the natural frontier and working "
            "in planta. What would kill the engineering dream: every "
            "functional variant landing on or inside the frontier after "
            "exhaustive search, supporting near-perfect optimization. What "
            "this does NOT claim: it does not claim the search is exhausted, "
            "does not claim algal transplants are useless, and does not "
            "propose abandoning Rubisco work - only scoring it honestly."),
        "citations": [CIT_TCHERKEZ],
        "demo_params": {"turnover": 3.2, "specificity": 92.0, "frontier_gap": 0.0},
    },
    {
        "key": "yield-ceilings",
        "name": "Crop Yield Ceilings: How Much Can a Field Ever Give",
        "group": "Advanced",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": ("Every crop in every climate has a theoretical yield "
                    "potential - the maximum physics and physiology allow. "
                    "How close are the best farms, where exactly is the "
                    "remaining headroom, and which ceilings are hard laws "
                    "versus soft limits?"),
        "background": (
            "Yield potential analysis combines solar radiation, temperature, "
            "and crop physiology to compute the ceiling for a given place "
            "and season. The best farmers reach 70 to 80 percent of "
            "potential for major cereals; global averages sit near half. "
            "The gap decomposes into water limits, nutrient limits, pests, "
            "and management - but the decomposition shifts with climate, "
            "and warming is moving the ceilings themselves: heat stress "
            "lowers potential even as carbon dioxide fertilization raises "
            "it. Open questions include how yield potential should be "
            "defined under increasingly variable weather, whether the "
            "70-to-80-percent farm ceiling is economic or biological, and "
            "how much genetic improvement can still lift the ceiling "
            "versus merely closing the gap to it."),
        "why_it_matters": (
            "Yield ceilings are the hard numbers behind food-security "
            "planning: they tell us whether breeding, agronomy, or new "
            "farmland must do the heavy lifting this century. Misjudging "
            "the ceiling means misallocating billions in research. A "
            "rigorous ceiling framework also disciplines hype - every "
            "'breakthrough' yield claim can be checked against it."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for mapping true yield ceilings, with "
            "adjustable assumptions and written-down confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: ceilings must be computed probabilistically - as "
            "distributions over weather years, not single numbers - because "
            "variability, not averages, now binds. Reasoning: a ceiling "
            "defined for average weather misleads in a climate of extremes; "
            "farmers experience the bad years. Proposed method: compute "
            "yield-potential distributions from decades of weather records "
            "and crop models for major breadbaskets, decompose observed "
            "yields into gap components, and project how the distributions "
            "shift under warming scenarios; validate against the best "
            "commercial farms. What would confirm the framework: farm data "
            "tracking the predicted distributions and gap decomposition "
            "across regions. What would kill it: systematic divergence "
            "between modeled ceilings and the best real farms, implying "
            "missing physiology. What this does NOT claim: it does not "
            "claim ceilings are fixed, does not predict specific harvests, "
            "and does not propose policy on model output alone."),
        "citations": [CIT_ZHU, CIT_ORT],
        "demo_params": {"potential_t_ha": 14.0, "best_farm": 11.2, "global_avg": 6.8},
    },
]
