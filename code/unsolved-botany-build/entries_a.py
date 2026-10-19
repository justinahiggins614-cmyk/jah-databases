#!/usr/bin/env python3
"""Entries 1-9 (ladder ranks 1-9, Foundations) for the Unsolved Botany databases.

Every entry: key, name, group, ladder_rank, ladder_tier, problem, background,
why_it_matters, sig_pointer (public half), sig_solution (signature half, full
treatment opening with the exact honesty label), citations, demo_params.
"""

SIG_TAIL = ("Signature original - his original Signature solution method: every "
            "unsolved problem an open door, every proposed solution a labeled "
            "pathway with its confirm and refute conditions written down in "
            "advance, never presented as established science. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_LEE = ("Lee DW et al. Pigment dynamics and autumn leaf senescence in a "
           "New England deciduous forest, eastern USA. Ecol Res; 2003.")
CIT_HOCH = ("Hoch WA et al. Resorption protection. Anthocyanins facilitate "
            "nutrient recovery in autumn by shielding leaves from potentially "
            "damaging light levels. Plant Physiol; 2001.")
CIT_DARWIN = ("Darwin C. Insectivorous Plants. London: John Murray; 1875.")
CIT_BOHM = ("Boehm J et al. The Venus flytrap Dionaea muscipula counts prey "
            "induced action potentials to induce sodium uptake. Curr Biol; 2016.")
CIT_CHRISTIE = ("Christie JM. Phototropin blue-light receptors. Annu Rev Plant "
                "Biol; 2007.")
CIT_DARWIN2 = ("Darwin C, Darwin F. The Power of Movement in Plants. London: "
               "John Murray; 1880.")
CIT_FINCH = ("Finch-Savage WE, Leubner-Metzger G. Seed dormancy and the "
             "control of germination. New Phytol; 2006.")
CIT_TAMAKI = ("Tamaki S et al. Hd3a protein is a mobile flowering signal in "
              "rice. Science; 2007.")
CIT_AN = ("An H et al. CONSTANS acts in the phloem to regulate a systemic "
          "signal that induces photoperiodic flowering of Arabidopsis. "
          "Development; 2004.")
CIT_GIVNISH = ("Givnish TJ et al. Carnivory in the bromeliad Brocchinia "
               "reducta, with a cost/benefit model for the general restriction "
               "of carnivorous plants to sunny, moist, nutrient-poor habitats. "
               "Am Nat; 1984.")
CIT_ALBERT = ("Albert VA et al. The carnivorous bladderwort (Utricularia "
              "gibba) genome. Mol Biol Evol; 2010.")
CIT_KARBAN = ("Karban R et al. Communication between plants: induced resistance "
              "in wild tobacco plants following clipping of neighboring sagebrush. "
              "Oecologia; 2000.")
CIT_HEIL = ("Heil M, Karban R. Explaining evolution of plant communication by "
            "airborne signals. Trends Ecol Evol; 2010.")
CIT_SUNG = ("Sung S, Amasino RM. Vernalization in Arabidopsis thaliana is "
            "mediated by the PHD finger protein VIN3. Nature; 2004.")
CIT_ANGEL = ("Angel A et al. A Polycomb-based switch underlying quantitative "
             "epigenetic memory. Nature; 2011.")
CIT_SCHULMAN = ("Schulman E. Bristlecone pine, oldest known living thing. "
                "Natl Geogr Mag; 1958.")
CIT_CONNOR = ("Connor KF, Lanner RM. Effects of tree age on pollen, seed, and "
              "seedling characteristics in Great Basin bristlecone pine "
              "(Pinus longaeva). Tree Physiol; 1990.")

ENTRIES_A = [
    {
        "key": "autumn-colors",
        "name": "Why Leaves Turn Color in Autumn",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "problem": ("Why do deciduous leaves turn yellow, orange, and red in autumn? "
                    "The chlorophyll drains away to reveal yellow carotenoids that were "
                    "there all along, but the brilliant reds are anthocyanins that the "
                    "leaf spends energy to manufacture on its way out. Why would a "
                    "dying leaf invest precious resources in new pigment?"),
        "background": (
            "People have watched autumn color for millennia, but the physiology was "
            "only worked out in the 20th century. As days shorten, trees seal off "
            "leaves and break down chlorophyll to recover its nitrogen, unmasking "
            "the yellow and orange carotenoids. The red anthocyanins are different: "
            "they are synthesized fresh during senescence, which costs the leaf "
            "energy at the very moment it is shutting down. Two camps explain this "
            "spending: the photoprotection hypothesis holds that red pigments shade "
            "the dismantling photosynthetic machinery from damaging light so nutrient "
            "recovery can finish, while others argue the reds are a warning signal to "
            "insects or a byproduct of sugar chemistry with no special job. "
            "Measurements show anthocyanin-rich leaves do resorb nitrogen more "
            "efficiently in some species, but the pattern is patchy across species "
            "and climates, and no single explanation covers every red autumn leaf."),
        "why_it_matters": (
            "Autumn color is the most visible nutrient-recycling program on Earth: "
            "forests recover a large share of leaf nitrogen before dropping them, "
            "and whatever improves that recovery improves forest growth. Settling "
            "why leaves make red pigments would clarify how plants balance light "
            "damage against nutrient salvage - a tradeoff breeders could exploit. "
            "It is also the friendliest doorway into plant physiology: anyone can "
            "watch it happen every fall."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for testing the photoprotection hypothesis "
            "against its rivals, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: anthocyanin synthesis during senescence is costly enough "
            "that natural selection would not preserve it without a payoff, so the "
            "payoff should be measurable as extra recovered nitrogen or carbon. "
            "Reasoning: the photoprotection hypothesis makes a testable prediction - "
            "leaves that make more red pigment should dismantle chlorophyll longer "
            "under high light and resorb more nitrogen than their yellow neighbors - "
            "while the warning-signal hypothesis predicts insect behavior differences "
            "instead. Proposed method: track matched red and yellow leaves of the "
            "same species through senescence, measuring pigment levels, "
            "photosystem-II efficiency, and leaf nitrogen week by week, and run the "
            "same comparison inside light-exclusion bags to separate light effects "
            "from chemistry. What would confirm it: a consistent correlation between "
            "anthocyanin content and nitrogen recovery that vanishes when light is "
            "removed. What would kill it: red and yellow leaves recovering identical "
            "nitrogen under identical light, or insect-exclusion experiments showing "
            "the reds change nothing about herbivory. What this does NOT claim: it "
            "does not claim every red leaf is photoprotective, does not claim the "
            "insect-warning idea is wrong, and does not propose a breeding program "
            "until the mechanism is settled."),
        "citations": [CIT_LEE, CIT_HOCH],
        "demo_params": {"red_gain": 0.18, "yellow_gain": 0.10, "n_reps": 6},
    },
    {
        "key": "flytrap-counts",
        "name": "How the Venus Flytrap Counts Its Prey",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "problem": ("The Venus flytrap snaps shut only after a hair is touched twice "
                    "within about thirty seconds, and only starts digesting after about "
                    "five touches. How does a plant with no brain count to five?"),
        "background": (
            "Charles Darwin called the Venus flytrap one of the most wonderful plants "
            "in the world and spent years testing what triggers it. Each trap lobe "
            "carries a few sensitive trigger hairs; bending one fires an electrical "
            "action potential, and two potentials within a short window spring the "
            "trap. Modern work showed the plant keeps a running tally: each action "
            "potential raises cytosolic calcium, and the calcium level acts like a "
            "memory register - two touches arm the trap, three to five switch on "
            "jasmonate signaling, sodium uptake, and the digestive enzyme program. "
            "The counting mechanism itself, how precisely the calcium register "
            "integrates successive touches and resets, and how the trap distinguishes "
            "a struggling insect from wind-blown debris, remain incompletely mapped. "
            "The trap is one of the fastest movements in the plant kingdom, yet its "
            "electrical language is still being decoded."),
        "why_it_matters": (
            "The flytrap is proof that plants process sequential information without "
            "neurons - a working example of computation in soft tissue. Understanding "
            "its counter would illuminate how all plants integrate signals over time, "
            "from root navigation to flowering decisions. The mechanism also inspires "
            "bioengineers building touch-responsive soft robots and sensors."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for mapping the flytrap counting register, "
            "with adjustable assumptions and written-down confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: the trap's memory is a calcium-concentration register in "
            "the trigger-hair sensory cells, with each action potential adding a "
            "fixed increment that decays over roughly thirty seconds. Reasoning: if "
            "the register is real, the number of touches needed to trigger each "
            "downstream program should shift predictably when calcium dynamics are "
            "slowed or sped up. Proposed method: image cytosolic calcium in living "
            "trigger hairs during controlled touch sequences, fit the increment and "
            "decay constants, then perturb them with calcium-channel blockers and "
            "temperature shifts and check whether the touch-count thresholds for "
            "closure, jasmonate induction, and digestion move as the model predicts. "
            "What would confirm it: threshold touch counts shifting in quantitative "
            "agreement with the fitted calcium model across all three programs. "
            "What would kill it: jasmonate or digestion thresholds that move "
            "independently of the calcium register, implying parallel counting "
            "circuits. What this does NOT claim: it does not claim the register is "
            "the whole story, does not claim flytraps are conscious, and does not "
            "propose engineering the counter until the natural one is mapped."),
        "citations": [CIT_DARWIN, CIT_BOHM],
        "demo_params": {"increment": 1.2, "decay_tau_s": 30.0, "closure_threshold": 2.0},
    },
    {
        "key": "phototropism",
        "name": "How Plants Find the Light",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "problem": ("A seedling in a dark box bends toward the smallest slit of light. "
                    "The bending is driven by the hormone auxin, but the complete chain "
                    "from blue-light sensor to asymmetric growth - every link, every "
                    "feedback - is still not fully mapped."),
        "background": (
            "Darwin and his son showed in 1880 that the tip of a seedling senses "
            "light and sends a message down to the bending zone. A century later the "
            "Cholodny-Went theory named the messenger: auxin accumulating on the "
            "shaded side, where it loosens cell walls so that side grows faster. "
            "The blue-light receptors, the phototropins, were identified around 2000, "
            "and the auxin transport machinery - PIN proteins pumping auxin from cell "
            "to cell - has been mapped in increasing detail. Yet the full loop has "
            "gaps: exactly how phototropin activation relocates PIN proteins within "
            "minutes, how the gradient is maintained against diffusion, and how "
            "mechanical feedback from the bending itself feeds back into the signal "
            "are still active research questions. Phototropism is the textbook "
            "example of plant sensing, and its wiring diagram still has blank boxes."),
        "why_it_matters": (
            "Every crop on Earth is a light-hunting machine, and the efficiency of "
            "that hunting sets yields. Completing the phototropism circuit would give "
            "breeders knobs for canopy architecture - leaves angled to catch light "
            "without shading neighbors. The signaling logic also teaches a general "
            "lesson: how a decentralized organism converts a gradient into motion."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for closing the phototropin-to-PIN wiring "
            "gap, with adjustable assumptions and written-down confirm and refute "
            "conditions."),
        "sig_solution": (
            "Assumptions: the missing links are fast post-translational events - "
            "phosphorylation and vesicle traffic - rather than undiscovered genes. "
            "Reasoning: the bending starts within minutes of light exposure, too fast "
            "for new protein synthesis, so the machinery must already be in place and "
            "waiting for a switch. Proposed method: fluorescently tag PIN proteins "
            "and phototropin targets in living hypocotyls, apply a sharp blue-light "
            "gradient, and record the relocation sequence frame by frame; then "
            "knock out candidate kinases one by one and watch which step stalls. "
            "What would confirm it: a complete time-ordered chain from phototropin "
            "activation to PIN relocalization to auxin asymmetry to wall loosening, "
            "with each step necessary. What would kill it: bending that persists when "
            "the candidate phosphorylation steps are blocked, forcing the search "
            "toward unknown components. What this does NOT claim: it does not claim "
            "the genes are all known, does not claim mechanical feedback is minor, "
            "and does not propose redesigning canopy architecture before the loop "
            "is closed."),
        "citations": [CIT_DARWIN2, CIT_CHRISTIE],
        "demo_params": {"light_angle_deg": 45.0, "auxin_ratio": 2.4, "bend_rate": 0.8},
    },
    {
        "key": "seed-dormancy",
        "name": "How a Seed Knows When to Wake Up",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "problem": ("A seed can wait years in the soil and then germinate on exactly "
                    "the right spring morning. It weighs temperature, moisture, light, "
                    "and time through the balance of two hormones - abscisic acid "
                    "keeping it asleep, gibberellin waking it - but the full "
                    "environmental integrator that computes the decision is unsolved."),
        "background": (
            "Seed dormancy is a survival bet: germinate too early and the seedling "
            "freezes; wait too long and competitors take the light. Physiologists "
            "established the core tug-of-war - abscisic acid (ABA) enforces dormancy "
            "while gibberellins (GA) promote germination - and mapped how cold, "
            "after-ripening, and light shift the balance. What remains open is the "
            "integration: how the embryo combines noisy, fluctuating signals over "
            "months into one irreversible decision, how deeply dormant seeds track "
            "the passage of seasons, and why closely related species set such "
            "different thresholds. Climate change has made the question urgent: "
            "warming winters are scrambling the cold cues many seeds depend on, and "
            "germination timing is shifting in ways the current models cannot fully "
            "predict."),
        "why_it_matters": (
            "Germination timing decides which plants win the spring race - in "
            "natural ecosystems and in every farmer's field. A complete dormancy "
            "model would let seed banks predict viability, let breeders tune "
            "germination to new climates, and let restoration ecologists time "
            "sowing for success. It is also a pure decision-theory problem solved "
            "by an embryo with no nervous system."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for cracking the seed's environmental "
            "integrator, with adjustable assumptions and written-down confirm and "
            "refute conditions."),
        "sig_solution": (
            "Assumptions: the seed computes a running score from its environment, "
            "with ABA/GA ratio as the readout and temperature history as the main "
            "input, updated on daily timescales. Reasoning: dormancy breaking looks "
            "like evidence accumulation - long cold steadily lowers the germination "
            "threshold rather than flipping a switch - so it should be modelable as "
            "a leaky integrator with a threshold. Proposed method: expose seed "
            "batches to programmed temperature and moisture histories, log the "
            "ABA/GA ratio at intervals, and fit an integrator model; then test it "
            "against real field winters and against mutants with shifted hormone "
            "sensitivity. What would confirm it: the same integrator parameters "
            "predicting germination timing across different winters and genotypes. "
            "What would kill it: germination decisions that depend on signal "
            "sequences the integrator cannot represent, implying a more complex "
            "state machine. What this does NOT claim: it does not claim the "
            "hormone list is complete, does not claim all species use the same "
            "integrator, and does not propose field prescriptions until the model "
            "is validated outdoors."),
        "citations": [CIT_FINCH],
        "demo_params": {"cold_days": 60, "aba": 3.2, "ga": 1.1, "threshold": 0.5},
    },
    {
        "key": "florigen",
        "name": "What Tells a Plant It Is Time to Flower",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "problem": ("For decades botanists hunted florigen, the mysterious mobile "
                    "signal that tells a distant shoot tip to make flowers. The "
                    "protein FT was caught red-handed in 2007 - but the full "
                    "delivery network, and how dozens of signals converge on one "
                    "decision, is still being mapped."),
        "background": (
            "Grafting experiments in the 1930s proved a leaf exposed to the right "
            "day length could make a grafted partner flower, so a mobile signal - "
            "florigen - had to exist. The hunt lasted seventy years until 2007, "
            "when the rice protein Hd3a and its Arabidopsis cousin FT were shown "
            "to travel through the phloem from leaf to shoot apex and flip the "
            "flowering switch. Since then the cast has grown: antiflorigens that "
            "oppose FT, age and sugar and temperature inputs feeding into the same "
            "apex, and florigen-like signals in trees that must coordinate "
            "flowering across massive canopies. Open questions remain about how "
            "the FT signal is loaded, protected, and unloaded during its long "
            "journey, how the apex counts the signal against competing repressors, "
            "and how perennials reset the system year after year."),
        "why_it_matters": (
            "Flowering time decides whether a crop matures before drought, frost, "
            "or the end of the season - it is one of the highest-value traits in "
            "breeding. Completing the florigen network would let breeders tune "
            "flowering to any latitude or shifting climate with precision. It is "
            "also a model of long-distance communication in a body with no nerves."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for mapping the complete florigen "
            "delivery network, with adjustable assumptions and written-down confirm "
            "and refute conditions."),
        "sig_solution": (
            "Assumptions: the apex decides by comparing the arriving FT dose "
            "against locally produced repressors, with the ratio - not the "
            "absolute FT level - as the trigger. Reasoning: plants flower across a "
            "wide range of sizes and vigor, so the decision must be normalized "
            "against the plant's own state rather than keyed to a fixed FT amount. "
            "Proposed method: graft FT-reporter scions onto stocks with tuned FT "
            "production, image FT arrival at the apex in real time, and record the "
            "exact FT-to-repressor ratio at the moment of the floral transition "
            "across day lengths, temperatures, and plant ages. What would confirm "
            "it: a single critical ratio predicting flowering across all "
            "conditions. What would kill it: flowering at wildly different ratios "
            "under different conditions, implying parallel decisive pathways. What "
            "this does NOT claim: it does not claim FT is the only mobile signal, "
            "does not claim the ratio model covers trees, and does not propose "
            "flowering-time engineering until the network is complete."),
        "citations": [CIT_TAMAKI, CIT_AN],
        "demo_params": {"ft_dose": 12.0, "repressor": 8.0, "critical_ratio": 1.5},
    },
    {
        "key": "carnivory",
        "name": "Why Some Plants Eat Animals",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "problem": ("Hundreds of plant species trap and digest insects, yet "
                    "carnivory evolved independently many times and only in poor "
                    "soils. What genomic switch turns a leaf into a stomach, and "
                    "why did evolution flip it so often - and only there?"),
        "background": (
            "Darwin's 1875 book on insectivorous plants proved that sundews and "
            "flytraps genuinely digest their prey, absorbing nitrogen and "
            "phosphorus through specialized glands. The cost-benefit model "
            "explains the habitat pattern: traps are expensive, so carnivory pays "
            "only where sunlight and water are plentiful but soil nutrients are "
            "scarce. Genomics has since revealed that carnivorous plants "
            "repeatedly recruited the same gene families - defense and stress "
            "genes repurposed for digestion - yet the regulatory switch that "
            "converts a flat leaf into a pitcher, snap-trap, or sticky tentacle "
            "is not fully understood. Neither is the deeper puzzle: with at least "
            "ten independent origins, carnivory is one of evolution's favorite "
            "reinventions, and the genomic preconditions that make a lineage "
            "'carnivory-ready' are still being mapped."),
        "why_it_matters": (
            "Carnivorous plants are evolution caught in the act of inventing the "
            "same organ repeatedly - a natural experiment in how novelty arises. "
            "The digestive enzymes they evolved are of interest for biotechnology, "
            "and their nutrient economics inform how all plants budget scarce "
            "resources. Understanding the switch could even inspire crops that "
            "supplement their own nitrogen."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for finding the carnivory switch, with "
            "adjustable assumptions and written-down confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: the switch is regulatory, not a new gene - a rewiring of "
            "existing defense and developmental programs - and lineages become "
            "'carnivory-ready' when they already express digestive enzymes in "
            "roots or wounded leaves. Reasoning: carnivory evolved too many times "
            "for each origin to require rare new genes; the cheapest path is "
            "repurposing. Proposed method: compare the genomes and trap-development "
            "transcriptomes of closely related carnivorous and non-carnivorous "
            "pairs across several independent origins, hunting for convergent "
            "regulatory changes; then test candidates by activating them in a "
            "non-carnivorous relative. What would confirm it: the same regulatory "
            "rewiring appearing at multiple independent origins and producing "
            "trap-like structures when activated. What would kill it: each origin "
            "using entirely different genetic routes with no shared regulatory "
            "logic. What this does NOT claim: it does not claim carnivory can be "
            "installed in crops, does not claim the habitat model is wrong, and "
            "does not propose engineering until the natural switch is found."),
        "citations": [CIT_GIVNISH, CIT_ALBERT],
        "demo_params": {"origins": 10, "shared_genes": 42, "benefit_cost": 1.8},
    },
    {
        "key": "plant-warning",
        "name": "Do Plants Warn Each Other of Attack",
        "group": "Foundations",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "problem": ("When insects chew a leaf, the plant releases volatile chemicals "
                    "into the air, and neighboring plants sometimes toughen their "
                    "defenses in response. Is this genuine plant-to-plant warning, or "
                    "are neighbors just eavesdropping on a signal meant for the "
                    "attacked plant itself?"),
        "background": (
            "In the 1980s, experiments suggested that damaged trees made their "
            "neighbors unpalatable to herbivores, launching decades of work on "
            "airborne plant signaling. Careful field studies showed that volatiles "
            "from clipped sagebrush induce defense responses in neighboring wild "
            "tobacco, reducing herbivore damage. But critics raised a sharp "
            "alternative: the volatiles may be internal signals that leak into the "
            "air, with neighbors merely eavesdropping - and true communication, "
            "which requires the sender to benefit, is hard to demonstrate because "
            "helping competitors is evolutionarily costly. The ecological relevance "
            "is also debated: laboratory effects are clear, but whether airborne "
            "warning meaningfully changes herbivory in real, windy plant "
            "communities remains contested, with effects that are real but modest "
            "and condition-dependent."),
        "why_it_matters": (
            "If plants routinely warn kin and neighbors, it changes how we model "
            "ecosystems, plant competition, and crop protection - fields of "
            "'talking' crops could prime each other's defenses without pesticides. "
            "The debate is also a masterclass in evolutionary reasoning: it forces "
            "a precise definition of communication versus eavesdropping."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for settling the warning-versus-"
            "eavesdropping debate, with adjustable assumptions and written-down "
            "confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: the decisive test is fitness, not chemistry - "
            "communication requires the emitter to gain inclusive fitness from the "
            "receiver's response. Reasoning: chemistry alone cannot distinguish "
            "warning from leakage, but a kin-selection experiment can: emitters "
            "should benefit more when receivers are relatives. Proposed method: "
            "grow emitter plants surrounded by kin versus strangers in field plots, "
            "trigger herbivory on the emitter, and measure the emitter's lifetime "
            "seed production in both arrangements, with volatile-blocking controls "
            "to isolate the airborne channel. What would confirm it: emitters "
            "producing more surviving offspring when surrounded by responding kin "
            "than by non-responding strangers. What would kill it: no emitter "
            "fitness difference in any arrangement, reducing the phenomenon to "
            "eavesdropping. What this does NOT claim: it does not claim volatiles "
            "are useless to neighbors, does not claim all species behave alike, "
            "and does not propose volatile-based crop protection until the "
            "evolutionary logic is settled."),
        "citations": [CIT_KARBAN, CIT_HEIL],
        "demo_params": {"kin_gain": 0.12, "stranger_gain": 0.02, "wind_loss": 0.6},
    },
    {
        "key": "vernalization",
        "name": "How Plants Remember Winter",
        "group": "Foundations",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "problem": ("Many plants must experience weeks of cold before they can "
                    "flower - and they remember that winter for months afterward. "
                    "The memory is written in chromatin, not neurons. How does a "
                    "plant measure winter and keep the record?"),
        "background": (
            "Farmers have known for centuries that winter wheat sown in spring "
            "refuses to flower; it needs the cold. Molecular biology traced the "
            "memory to a single gene, FLC, which represses flowering until winter "
            "silences it. During prolonged cold, the protein VIN3 accumulates and "
            "recruits Polycomb machinery that wraps the FLC locus in repressive "
            "histone marks - an epigenetic off-switch that persists through cell "
            "divisions into spring. Quantitative work showed the silencing is "
            "graded: longer cold silences FLC in more cells, giving the plant a "
            "proportional memory of winter length. Open questions remain about "
            "how the cold is measured cell by cell, how the memory survives DNA "
            "replication but resets in the next generation's embryos, and how "
            "warming winters are already scrambling this system in crops and "
            "wildflowers."),
        "why_it_matters": (
            "Vernalization is the clearest example of environmental memory without "
            "a brain - a molecular winter diary. As winters warm, crops that "
            "miscount the cold flower at the wrong time or not at all, threatening "
            "yields. Understanding the memory mechanism would let breeders retune "
            "it for new climates and give synthetic biologists a proven design for "
            "long-term cellular memory."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for reading the plant's winter diary, "
            "with adjustable assumptions and written-down confirm and refute "
            "conditions."),
        "sig_solution": (
            "Assumptions: each cell independently accumulates a cold signal, and the "
            "whole-plant memory is the fraction of cells that have flipped FLC off. "
            "Reasoning: the graded, proportional memory and its stability through "
            "mitosis point to a cell-autonomous bistable switch rather than a "
            "central counter. Proposed method: track FLC silencing in individual "
            "cells of the shoot apex through a programmed winter using fluorescent "
            "reporters, build the single-cell switching statistics, and test "
            "whether the population fraction predicts flowering time; then perturb "
            "the Polycomb machinery to shift the switching threshold. What would "
            "confirm it: flowering time predicted quantitatively by the silenced "
            "cell fraction across cold durations and genotypes. What would kill it: "
            "coordinated all-or-nothing switching across the apex, implying a "
            "tissue-level signal instead. What this does NOT claim: it does not "
            "claim the mechanism is identical in cereals, does not claim warming "
            "effects are fully predictable, and does not propose memory "
            "engineering before the natural switch is fully mapped."),
        "citations": [CIT_SUNG, CIT_ANGEL],
        "demo_params": {"cold_weeks": 6, "switch_prob": 0.35, "cells": 200},
    },
    {
        "key": "bristlecone-longevity",
        "name": "Why Bristlecone Pines Live Five Millennia",
        "group": "Foundations",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "problem": ("Great Basin bristlecone pines live nearly 5,000 years - the "
                    "oldest known non-clonal organisms on Earth. They grow in some "
                    "of the harshest conditions on the planet. What lets a tree "
                    "survive fifty centuries when most organisms manage a fraction "
                    "of one?"),
        "background": (
            "In the 1950s, Edmund Schulman cross-dated bristlecone pine rings and "
            "found trees over 4,000 years old; the Methuselah tree is about 4,800. "
            "They achieve this in cold, dry, dolomite soils where almost nothing "
            "else grows - extremely slow growth, dense resinous wood, and a "
            "strategy of letting parts of the tree die while a thin living strip "
            "carries on. Remarkably, studies found no decline in pollen viability "
            "or seed quality with tree age - a 4,000-year-old tree reproduces as "
            "well as a young one, defying the usual senescence. The genomic basis "
            "of this longevity is still open: candidate mechanisms include "
            "exceptional DNA repair, relentless pathogen defense, and modular "
            "growth that quarantines damage, but the full genetic architecture "
            "of millennia-scale life has not been mapped."),
        "why_it_matters": (
            "Bristlecones are the extreme case of biological longevity - a system "
            "that solved aging without medicine. Whatever they do has lessons for "
            "understanding senescence everywhere, and their rings are the gold "
            "standard archive of past climate. Protecting and studying them is "
            "protecting a 5,000-year experiment that cannot be repeated."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for mapping the bristlecone longevity "
            "program, with adjustable assumptions and written-down confirm and "
            "refute conditions."),
        "sig_solution": (
            "Assumptions: longevity is modular - the tree survives because damage "
            "is quarantined in disposable sectors while meristems stay pristine - "
            "and the genome carries enhanced maintenance machinery. Reasoning: "
            "the absence of reproductive decline with age rules out whole-organism "
            "senescence and points to continuous renewal of the growing tips. "
            "Proposed method: sequence bristlecone genomes across ages and compare "
            "DNA-repair, pathogen-defense, and meristem-maintenance gene families "
            "against short-lived pines; measure mutation accumulation in ancient "
            "versus young meristems; and map how the tree compartmentalizes "
            "damage. What would confirm it: expanded repair gene families plus "
            "near-zero mutation buildup in millennia-old meristems. What would "
            "kill it: mutation loads that rise with age just like short-lived "
            "trees, implying longevity is purely ecological luck. What this does "
            "NOT claim: it does not claim a single longevity gene, does not claim "
            "the findings transfer to animals, and does not propose harvesting "
            "ancient trees for study - only non-destructive sampling."),
        "citations": [CIT_SCHULMAN, CIT_CONNOR],
        "demo_params": {"age_years": 4800, "mutation_rate": 0.02, "repair_genes": 214},
    },
]
