#!/usr/bin/env python3
"""Entries for the Unsolved Zoology databases (Manon's 16:15 orders).

34 famous unsolved zoology problems, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex). Public half carries
the real fact-checked problem record plus a short pointer to the Signature
approach; Signature half carries the full Signature-generated proposed
solution, always labeled and never presented as established science.

Field scope: animal consciousness and sentience markers, migration
navigation, the evolution of eusociality, why sex persists, language
origins in non-humans, plus the wider canon of famous open questions in
animal biology: flight origins, regeneration, the vertebrate jaw, aging,
the Cambrian explosion, the root of the animal tree, and the predictability
of evolution.

ID prefixes: JAH-USZO- (public) and JAH-USZOS- (signature), verified free
in the manifest id_prefix values and across all shard index files in
jah-databases-data-1 (zero hits, 2026-10-17).

Every demo is a solution-explorer walkthrough: real, runnable,
stdlib-only Python that computes concrete evidence, walks the Signature
approach with adjustable assumptions, prints an explicit CONFIRM / REFUTE
panel, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Honesty rule: the signature_solution opens with the exact label
"Signature-generated proposed solution — not established science" and
never claims proof, peer acceptance, or settled status.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature solution method: every "
            "unsolved problem approached as a covenant between the known and the "
            "unknown, the proposed path walked step by step with its assumptions "
            "declared, its confirm and refute conditions stated, and its limits "
            "honestly marked. Clearly labeled Signature-made, never presented as "
            "established science or authentic public record.")

CIT_DARWIN = ("Darwin C. On the Origin of Species. John Murray; 1859.")
CIT_SIMMONS = ("Simmons RE, Scheepers L. Winning by a neck: sexual selection in the "
               "evolution of the giraffe. American Naturalist; 1996.")
CIT_CARO14 = ("Caro T, Izzo A, Reiner RC, Walker H, Stankowich T. The function of "
              "zebra stripes. Nature Communications; 2014.")
CIT_CARO16 = ("Caro T. Zebra Stripes. University of Chicago Press; 2016.")
CIT_SIEGEL = ("Siegel JM. Clues to the functions of mammalian sleep. Nature; 2005.")
CIT_SCHMIDT = ("Schmidt MH. The energy allocation function of sleep: a unifying "
               "theory. Sleep Medicine Reviews; 2014.")
CIT_MOURITSEN = ("Mouritsen H. Long-distance navigation and magnetoreception in "
                 "migratory animals. Nature; 2018.")
CIT_HEINZE = ("Heinze S, Reppert SM. Sun compass integration of skylight cues in "
              "migratory monarch butterflies. Neuron; 2011.")
CIT_DINGLE = ("Dingle H, Drake VA. What is migration? BioScience; 2007.")
CIT_QUINN = ("Quinn TP. The Behavior and Ecology of Pacific Salmon and Trout. "
             "UBC Press; 2005.")
CIT_WEHNER = ("Wehner R. Desert ant navigation: how miniature brains solve complex "
              "tasks. Journal of Comparative Physiology A; 2003.")
CIT_HAMILTON = ("Hamilton WD. The genetical evolution of social behaviour I, II. "
                "Journal of Theoretical Biology; 1964.")
CIT_NOWAK = ("Nowak MA, Tarnita CE, Wilson EO. The evolution of eusociality. "
             "Nature; 2010.")
CIT_MAYNARD_SEX = ("Maynard Smith J. The Evolution of Sex. Cambridge University "
                   "Press; 1978.")
CIT_BELL = ("Bell G. The Masterpiece of Nature. Croom Helm; 1982.")
CIT_DUDLEY = ("Dudley R. The Biomechanics of Insect Flight. Princeton University "
              "Press; 2000.")
CIT_TEELING = ("Teeling EC, Springer MS, Madsen O, Bates P, O'Brien SJ, Murphy WJ. "
               "A molecular phylogeny for bats illuminates biogeography and the "
               "fossil record. Science; 2005.")
CIT_BROCKES = ("Brockes JP, Kumar A. Comparative aspects of animal regeneration. "
               "Annual Review of Cell and Developmental Biology; 2008.")
CIT_MALLATT = ("Mallatt J. The origin of the vertebrate jaw: neural crest, orbit "
               "and the timing of vertebrate cranial evolution. Zoologischer "
               "Anzeiger; 2008.")
CIT_KIRKWOOD = ("Kirkwood TBL. Understanding the odd science of aging. Cell; 2005.")
CIT_POULIN = ("Poulin R. Evolutionary Ecology of Parasites. 2nd ed. Princeton "
              "University Press; 2007.")
CIT_GRIFFIN = ("Griffin DR. Animal Minds. University of Chicago Press; 1992.")
CIT_CAMBRIDGE = ("Low P et al. The Cambridge Declaration on Consciousness. "
                 "Cambridge; 2012.")
CIT_HAUSER = ("Hauser MD, Chomsky N, Fitch WT. The faculty of language: what is "
              "it, who has it, and how did it evolve? Science; 2002.")
CIT_FITCH = ("Fitch WT. The Evolution of Language. Cambridge University Press; "
             "2010.")
CIT_GWINNER = ("Gwinner E. Circannual Clocks. Springer; 1986.")
CIT_ERWIN = ("Erwin DH, Valentine JW. The Cambrian Explosion. Roberts and "
             "Company; 2013.")
CIT_KING = ("King N. The unicellular ancestry of animal development. "
            "Developmental Cell; 2004.")
CIT_DUNN = ("Dunn CW, Hejnol A, Matus DQ et al. Broad phylogenomic sampling "
            "improves resolution of the animal tree of life. Nature; 2008.")
CIT_RYAN = ("Ryan JF, Pang K, Schnitzler CE et al. The genome of the ctenophore "
            "Mnemiopsis leidyi and its implications for cell type evolution. "
            "Science; 2013.")
CIT_JABLONSKI = ("Jablonski D. Survival without recovery after mass extinctions. "
                 "Proceedings of the National Academy of Sciences; 2002.")
CIT_DIAL = ("Dial KP. Wing-assisted incline running and the evolution of flight. "
            "Science; 2003.")
CIT_FINCH = ("Finch CE. Longevity, Senescence, and the Genome. University of "
             "Chicago Press; 1990.")
CIT_LOSOS = ("Losos JB. Improbable Destinies: Fate, Chance, and the Future of "
             "Evolution. Riverhead; 2017.")
CIT_BLOUNT = ("Blount ZD, Borland CZ, Lenski RE. Historical contingency and the "
              "evolution of a key innovation in an experimental population of "
              "Escherichia coli. PNAS; 2008.")

LABEL = "Signature-generated proposed solution — not established science."

ENTRIES = [
    {
        "key": "giraffe-neck",
        "name": "Why Giraffes Have Long Necks",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "problem": ("Giraffes have necks up to two meters long. Why? The textbook answer is "
                    "feeding competition: longer necks reach leaves other herbivores cannot. But a rival "
                    "hypothesis says the neck is a weapon and display for sexual selection: males club each "
                    "other with their necks and heads, and females prefer long-necked males. Both stories "
                    "sound plausible, and the evidence has not settled which one drove the evolution."),
        "background": ("Darwin himself used the giraffe in On the Origin of Species as a showcase of "
                       "natural selection acting on feeding reach, arguing that longer-necked animals survived "
                       "lean seasons by browsing high acacia foliage. For a century that feeding story went "
                       "unchallenged. In 1996, Robert Simmons and Lue Scheepers published the rival account, "
                       "'Winning by a neck,' showing that male giraffes fight by swinging their heavy heads "
                       "like clubs in contests called necking, that larger males win more matings, and that "
                       "females show no strong browsing-height advantage over males of the same species. "
                       "Later fieldwork complicated both stories: female giraffes often feed at shoulder "
                       "height, not at maximum reach, which weakens the pure feeding account; and sexual "
                       "dimorphism in neck mass is consistent with, but does not prove, sexual selection. "
                       "Most researchers now suspect both pressures acted together, but their relative "
                       "contributions remain genuinely open."),
        "why_it_matters": ("The giraffe neck is the single most famous textbook example of evolution by "
                           "natural selection, so what actually selected it shapes how the public understands "
                           "evolution itself. If sexual selection rather than feeding drove the trait, it is a "
                           "vivid case of how mating competition can build extreme anatomy. Resolving it would "
                           "sharpen methods for testing competing adaptive stories across all of animal form."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the giraffe neck as a dual-covenant trait: the neck promised "
                     "food to the hungry and dominance to the mating male, and the Signature approach separates "
                     "the two promises by testing each against its own unique prediction rather than against "
                     "each other."),
        "sig_solution": (
            LABEL + " Approach S-01: dual-promise decomposition. "
            "Assumptions: (A1) feeding and sexual selection leave different signatures: feeding predicts "
            "foraging-height use by both sexes proportional to neck length, sexual selection predicts "
            "necking win-rate and mating success proportional to neck and head mass in males only; "
            "(A2) long-term individual tracking data can separate the two; (A3) neither pressure acts alone. "
            "Reasoning path: (S1) quantify each male necking contest and link winners to lifetime reproductive "
            "success; (S2) measure leaf-access energy budgets across sexes and heights to price the feeding "
            "advantage; (S3) compare neck investment (mass, vertebrae proportions) between sexes and against "
            "okapi, the short-necked relative; (S4) test whether females with relatively longer necks gain "
            "survival advantage in droughts independent of mating. "
            "Proposed mechanism: a partition of selection gradients - feeding explains the ancestral "
            "elongation baseline, sexual selection explains the extreme male overshoot, tested by "
            "sex-specific fitness components. "
            "What would confirm it: males with longer necks winning measurably more contests and matings "
            "with no feeding deficit for shorter-necked females. What would kill it: necking contest outcome "
            "showing zero correlation with neck length or mating success. "
            "What it does NOT claim: a verdict on which pressure came first, peer acceptance, or settled "
            "status. This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: is the giraffe neck built by feeding competition, sexual selection, or both?",
            "Darwin used the giraffe as his showcase of selection on feeding reach; that story stood for a century.",
            "Simmons and Scheepers (1996) proposed the rival 'necks for sex' account based on male necking combat.",
            "Females often browse at shoulder height, which weakens the pure feeding story.",
            "This walkthrough compares the energy budget of browsing against contest-win returns.",
        ],
        "requirements": [
            "A verdict needs individual lifetime fitness data, not just one-season observations.",
            "The feeding account must show long necks pay their own energy and predation costs.",
            "The sexual-selection account must link necking success to actual reproductive success.",
            "Fossil neck-proportion series could separate the pressures in deep time.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent field replication.",
        ],
        "citations": [CIT_DARWIN, CIT_SIMMONS],
    },
    {
        "key": "zebra-stripes",
        "name": "Why Zebras Have Stripes",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "problem": ("No other hoofed mammal wears bold black-and-white stripes. Explanations on offer include "
                    "camouflage against lions, social signaling among herd members, cooling by convection "
                    "currents, and repelling blood-sucking flies. Each has some support and none has won "
                    "outright, making the zebra the most photographed unsolved wardrobe mystery in zoology."),
        "background": ("Naturalists have argued about zebra stripes since the 1800s. Camouflage was the early "
                       "favorite, but experiments have repeatedly shown lions hunt by movement and scent more "
                       "than fine pattern, and stripes do not hide a zebra from a lion at strike distance. "
                       "The thermoregulation idea, that stripes set up tiny air currents that cool the animal, "
                       "gained traction in the 2010s but large-scale field studies have failed to find "
                       "consistent cooling benefits. The strongest evidence to date supports the biting-fly "
                       "hypothesis: Tim Caro and colleagues showed in 2014 that striped surfaces confuse "
                       "horseflies and tsetse flies, and that striping correlates geographically with fly "
                       "pressure across equid ranges. Even so, flies alone struggle to explain stripe "
                       "variation within species and the social display functions documented in herds. "
                       "The consensus today is partial: flies explain a lot, but a single complete account "
                       "of stripes does not exist."),
        "why_it_matters": ("Stripes are an icon of African wildlife, so the question carries enormous public "
                           "weight for science communication. Methodologically it is a model case of how to test "
                           "competing adaptive hypotheses with field experiments, comparative data, and "
                           "geographic correlations. A resolution would also improve wildlife management, since "
                           "fly-borne disease is a real cost stripes may be paying down."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads zebra stripes as a layered garment: each proposed function is "
                     "a layer, and the Signature approach peels them apart by testing each layer in the "
                     "environment where it should matter most."),
        "sig_solution": (
            LABEL + " Approach S-02: layered-function peel. "
            "Assumptions: (A1) multiple functions can stack on one trait; (A2) each function predicts a "
            "different geographic or behavioral signature - flies predict striping tracks fly pressure, cooling "
            "predicts striping tracks heat, camouflage predicts striping tracks predator density; (A3) the "
            "dominant layer is the one whose predicted signature explains the most variance across all seven "
            "living equid taxa. "
            "Reasoning path: (S1) map stripe density and width against fly abundance, temperature, and "
            "predation across the full equid range; (S2) run controlled fly-landing experiments on striped "
            "versus plain horse models in the field; (S3) test thermography predictions on live zebras at "
            "different times of day; (S4) assign residual variance to social signaling by comparing herding "
            "species against solitary equids. "
            "Proposed mechanism: variance partitioning - the fly-repellent layer carries most of the "
            "explanatory weight, with cooling and social display as secondary layers. "
            "What would confirm it: stripe width and density tracking fly pressure with near-zero residual "
            "for the other predictors. What would kill it: controlled trials where flies land equally on "
            "striped and unstriped coats. "
            "What it does NOT claim: that one function explains every stripe, peer acceptance, or settled "
            "status. This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: which selection pressure built zebra stripes - flies, heat, camouflage, or social display?",
            "Camouflage against lions has weak experimental support; lions hunt by movement and scent.",
            "Caro et al. (2014) gave the biting-fly hypothesis its strongest evidence to date.",
            "Cooling-by-stripes studies have produced inconsistent results.",
            "This walkthrough models stripe value as a sum of competing benefit layers.",
        ],
        "requirements": [
            "Any resolution must test hypotheses against each other, not one at a time.",
            "Geographic correlations need all seven living equid taxa, not just plains zebras.",
            "Controlled experiments must use real flies and real coats, not simulations alone.",
            "Social-display claims need individual recognition experiments in herds.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent field replication.",
        ],
        "citations": [CIT_CARO14, CIT_CARO16],
    },
    {
        "key": "why-animals-sleep",
        "name": "Why Animals Sleep",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "problem": ("Nearly every animal studied so far does something sleep-like, and prolonged sleep "
                    "deprivation kills. Yet no single agreed function of sleep exists. Memory consolidation, "
                    "brain waste clearance, energy allocation, and synaptic pruning are all on the table, "
                    "and sleep scientists openly debate which, if any, is the primary reason animals sleep."),
        "background": ("Sleep is one of the great embarrassments of biology: universal, costly, dangerous "
                       "while it happens, and unexplained. Jerome Siegel argued in 2005 that sleep serves "
                       "adaptive inactivity, reducing energy use when being awake has no payoff, a view that "
                       "explains why sleep patterns differ so wildly across species. Markus Schmidt proposed "
                       "in 2014 that sleep exists to reallocate energy, switching the brain into a "
                       "low-consumption state so resources can be directed elsewhere. The glymphatic "
                       "hypothesis, that sleep clears metabolic waste from the brain, gained support in the "
                       "2010s from rodent studies but has proven hard to confirm in humans and other species. "
                       "Memory research shows sleep consolidates learning, but animals with tiny brains also "
                       "sleep, and jellyfish sleep without brains at all. The honest state of the field: "
                       "sleep does many things, and which one explains its existence is still open."),
        "why_it_matters": ("Sleep disorders afflict hundreds of millions of people, and every treatment is "
                           "guesswork without a true theory of function. For animal welfare and conservation, "
                           "knowing what sleep is for changes how we house, transport, and protect animals. "
                           "A real answer would be one of the landmark findings in all of biology."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads sleep as a budget meeting: the animal shuts down its most "
                     "expensive operations to spend the budget elsewhere, and the Signature approach prices "
                     "each candidate function in energy terms to see which one can pay for the behavior."),
        "sig_solution": (
            LABEL + " Approach S-03: energy-budget pricing. "
            "Assumptions: (A1) sleep evolved once under a dominant selection pressure, with other benefits "
            "added later; (A2) the dominant pressure is the one whose energy value exceeds the combined "
            "costs of sleep - vulnerability, lost foraging, lost mating - in the most species; (A3) brainless "
            "sleepers like jellyfish set a floor: any proposed primary function must work without a brain. "
            "Reasoning path: (S1) build energy budgets for sleeping versus awake-quiet animals across taxa; "
            "(S2) test whether the brainless-sleeper floor eliminates memory consolidation as the original "
            "function; (S3) quantify waste-clearance rates during sleep versus wake in multiple species; "
            "(S4) check whether species with the largest energy savings sleep the most. "
            "Proposed mechanism: adaptive inactivity as the original function - sleep as enforced energy "
            "conservation - with waste clearance and memory consolidation as later exaptations. "
            "What would confirm it: sleep duration tracking the marginal value of wakefulness across species "
            "better than any other predictor. What would kill it: a brainless species that never sleeps, "
            "proving sleep is a brain-only invention. "
            "What it does NOT claim: that one function rules out the others, peer acceptance, or settled "
            "status. This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: which function of sleep explains why the behavior evolved at all?",
            "Sleep is universal and costly; deprivation kills, yet its core purpose is unsettled.",
            "Siegel (2005) argued adaptive inactivity; Schmidt (2014) argued energy allocation.",
            "Brainless animals sleep, which constrains brain-only theories of function.",
            "This walkthrough prices candidate functions against sleep costs in an energy budget.",
        ],
        "requirements": [
            "A verdict needs comparative data across brainless, simple, and complex animals.",
            "Energy models must be tested experimentally, not just fitted.",
            "The glymphatic clearance claim needs confirmation beyond rodents.",
            "Sleep-deprivation harm must be separated into per-function deficits.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_SIEGEL, CIT_SCHMIDT],
    },
    {
        "key": "pigeon-homing",
        "name": "How Homing Pigeons Navigate",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "problem": ("A homing pigeon released hundreds of kilometers from home, in country it has never seen, "
                    "finds its way back. Pigeons clearly use the sun, the stars, smell, and the magnetic field, "
                    "but nobody knows how these senses fuse into a map, and nobody knows what the pigeon "
                    "actually senses of the magnetic field. The animal's compass has several needles and the "
                    "integration is the mystery."),
        "background": ("Pigeon homing has been studied since the 1950s, and the evidence for a magnetic sense "
                       "is strong: pigeons with magnets glued to their heads get confused on overcast days, "
                       "and lesions to the trigeminal nerve impair magnetic map use. Yet the receptor remains "
                       "unidentified - magnetite crystals in the beak were once the leading candidate, then "
                       "shown to be macrophages, and the cryptochrome-based compass in the eye is still "
                       "debated. The olfactory map hypothesis, championed by Floriano Papi, holds that pigeons "
                       "learn wind-borne odor gradients at the home loft and navigate by smell, with strong "
                       "support from anosmia experiments. The modern view is multi-modal: sun compass for "
                       "direction, magnetic and olfactory cues for the map, landmarks for the final approach. "
                       "How the brain weights and switches among these systems, and what the magnetic receptor "
                       "is, remain open."),
        "why_it_matters": ("Magnetoreception is one of the great unsolved senses; finding the receptor would "
                           "be a Nobel-caliber discovery. Understanding multi-sense fusion would inform "
                           "robotics and autonomous navigation. And pigeon homing is the gateway to the wider "
                           "mystery of animal navigation that runs through monarchs, salmon, and sea turtles."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the pigeon as a navigator with layered maps: a coarse magnetic "
                     "chart, a fine olfactory chart, and a sky compass, and the Signature approach decodes "
                     "which chart the bird trusts at each leg of the journey home."),
        "sig_solution": (
            LABEL + " Approach S-04: chart-switching decode. "
            "Assumptions: (A1) the pigeon brain maintains separate magnetic, olfactory, and visual maps; "
            "(A2) cue conflict experiments reveal the hierarchy by showing which cue the bird follows when "
            "maps disagree; (A3) the magnetic receptor is a real protein or mineral structure awaiting "
            "identification. "
            "Reasoning path: (S1) create cue conflicts - shift the magnetic field while holding odors "
            "constant, and vice versa - at different distances from home; (S2) map which cue dominates at "
            "which range, building the switching profile; (S3) screen retinal and trigeminal candidate "
            "molecules with magnetic-field-dependent assays; (S4) record from candidate brain areas during "
            "cue conflicts. "
            "Proposed mechanism: range-dependent hierarchy - magnetic map for the coarse leg, olfactory map "
            "for the middle leg, visual landmarks for the final approach, with the sun compass as the "
            "always-on directional reference. "
            "What would confirm it: a consistent switching profile replicated across lofts and terrains, plus "
            "a confirmed receptor molecule. What would kill it: cue conflicts producing random, "
            "unstructured behavior rather than a stable hierarchy. "
            "What it does NOT claim: identification of the receptor today, peer acceptance, or settled "
            "status. This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: how do pigeons fuse sun, magnetic, olfactory, and visual cues into one homing map?",
            "Magnetic sense is proven behaviorally; the receptor itself is unidentified.",
            "Anosmic pigeons fail at homing, proving smell matters; the beak magnetite turned out to be macrophages.",
            "The field suspects a range-dependent hierarchy of cues.",
            "This walkthrough simulates cue-conflict releases to map the hierarchy.",
        ],
        "requirements": [
            "The receptor must be identified at the molecular or mineral level.",
            "Cue-conflict experiments need replication across different home lofts.",
            "Neural recordings must show map switching in real time.",
            "Any receptor candidate must respond to Earth-strength fields.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_MOURITSEN],
    },
    {
        "key": "monarch-migration",
        "name": "How Monarch Butterflies Migrate",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "problem": ("Eastern monarch butterflies fly up to 4,000 kilometers to a handful of mountain groves "
                    "in Mexico, and no butterfly making the journey has ever been there before. The "
                    "southbound migrants are the great-grandchildren of the northbound ones. How does a "
                    "brain the size of a pinhead inherit a 4,000-kilometer route it has never flown?"),
        "background": ("The monarch migration was only fully mapped in 1975, when the Mexican overwintering "
                       "sites were found. Since then, work by Steven Reppert and colleagues has decoded the "
                       "compass: monarchs integrate the sun's position with polarized skylight patterns using "
                       "a time-compensated sun compass in the central complex of the brain, with the "
                       "antennae carrying the circadian clock that corrects for the sun's movement. Magnetic "
                       "compass cues appear to serve as backup on cloudy days. But the compass is only half "
                       "the story. The map - what tells a naive butterfly where Mexico is - remains "
                       "unexplained. No experiment has shown how the overwintering destination is encoded "
                       "across generations, and the navigational target may be a direction plus a "
                       "latitude trigger rather than a true map. Declining eastern populations have added "
                       "urgency to every open question."),
        "why_it_matters": ("The monarch is the flagship of insect migration and a conservation icon; "
                           "understanding its navigation is essential to protecting it. It is also the purest "
                           "test case for inherited navigation: if a pinhead brain can encode a continental "
                           "route, the mechanism must be exquisitely simple. Finding it would rewrite what "
                           "we think small nervous systems can do."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the monarch as a courier with a compass but no map: the "
                     "Signature approach asks what minimal inherited rule - direction plus triggers - can "
                     "reproduce the whole 4,000-kilometer journey without a stored destination."),
        "sig_solution": (
            LABEL + " Approach S-05: minimal inherited rule. "
            "Assumptions: (A1) the southbound route can be generated by a compass heading plus "
            "environmental stop and turn triggers, with no stored map of Mexico; (A2) the heading and "
            "triggers are genetically encoded and selected across generations; (A3) the sun compass plus "
            "magnetic backup plus photoperiod triggers are sufficient inputs. "
            "Reasoning path: (S1) build an agent-based simulation with only compass, clock, and trigger "
            "rules and see whether virtual monarchs converge on the real overwintering zone; (S2) test "
            "which trigger set - temperature drops, day length, magnetic inclination - best reproduces "
            "tracked routes; (S3) displace captive-reared migrants and check whether they correct toward "
            "a destination (map) or hold their heading (compass-only); (S4) search for the genetic "
            "differences between migratory and non-migratory monarch populations. "
            "Proposed mechanism: compass-plus-triggers - an inherited southwesterly heading corrected by "
            "the time-compensated sun compass, with temperature and day-length thresholds triggering "
            "descent and clustering behavior. "
            "What would confirm it: displaced migrants holding heading instead of correcting, and a "
            "minimal-rule simulation converging on the real groves. What would kill it: displaced migrants "
            "correcting toward Mexico, proving a true map. "
            "What it does NOT claim: that the map is settled, peer acceptance, or settled status. This is "
            "a proposed path, honestly labeled, and the question stays open until a real resolution exists."),
        "key_points": [
            "Statement: how do naive monarchs navigate 4,000 km to groves they have never seen?",
            "The time-compensated sun compass (Heinze and Reppert, 2011) is decoded; the map is not.",
            "Southbound migrants are the great-grandchildren of the northbound generation.",
            "Magnetic cues appear to back up the sun compass on cloudy days.",
            "This walkthrough simulates compass-plus-trigger agents against real tracked routes.",
        ],
        "requirements": [
            "Displacement experiments must distinguish map correction from heading holding.",
            "The genetic basis of migratory behavior needs population-level comparison.",
            "Any proposed trigger must be testable in the field, not just the lab.",
            "Simulations must reproduce the real overwintering geography.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_HEINZE, CIT_DINGLE],
    },
    {
        "key": "salmon-homing",
        "name": "How Salmon Find Their Birth River",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "problem": ("Pacific salmon spend years feeding in the open ocean, then swim thousands of kilometers "
                    "back to the exact stream where they hatched to spawn and die. The leading account says "
                    "they imprint on the smell of their home stream as juveniles and follow a magnetic map "
                    "across the ocean. Both halves of the story have gaps: the imprinted odor cocktail is "
                    "unidentified, and the magnetic map sense is still mysterious."),
        "background": ("Arthur Hasler proposed the olfactory imprinting hypothesis in the 1950s, and "
                       "experiments since have shown that salmon deprived of smell stray far more than intact "
                       "fish, and that artificial odorants added to hatchery water steer returning adults. "
                       "Thomas Quinn's long-term work has documented the astonishing precision of homing and "
                       "its genetic and environmental components. But the specific chemical signature of a "
                       "stream - the unique blend of amino acids, bile salts, and watershed chemistry that a "
                       "smolt memorizes - has never been fully identified. Meanwhile the ocean phase relies "
                       "on something else: juvenile salmon exposed to the magnetic field of distant ocean "
                       "regions orient as if displaced, suggesting a magnetic map, but the receptor is as "
                       "unknown as in pigeons. Climate change is now shifting stream temperatures and ocean "
                       "conditions, making the mechanism urgent as well as fascinating."),
        "why_it_matters": ("Salmon are ecological and economic keystones across the Pacific rim; hatchery "
                           "management, dam operations, and climate adaptation all depend on understanding "
                           "homing. The salmon system is also the best vertebrate model of true navigation "
                           "with both a map and a compass, making it a flagship for the whole migration "
                           "mystery."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the salmon as a fish with two passports: a magnetic one for "
                     "the ocean and a chemical one for the river, and the Signature approach stamps each "
                     "passport by isolating the exact cues the fish carries."),
        "sig_solution": (
            LABEL + " Approach S-06: two-passport decode. "
            "Assumptions: (A1) ocean navigation is magnetic-map based and river navigation is odor based, "
            "with a handoff zone at the river mouth; (A2) the imprinted odor is a learnable chemical "
            "cocktail, not a single compound; (A3) the magnetic receptor will be found in the same "
            "candidate tissues as in birds. "
            "Reasoning path: (S1) fractionate stream water and test smolt imprinting on each fraction to "
            "isolate the memorized cocktail; (S2) run magnetic displacement experiments on ocean-phase "
            "juveniles to map the magnetic coordinate system; (S3) screen olfactory receptor gene "
            "expression in imprinting smolts for the upregulated set; (S4) track the handoff by releasing "
            "fish with one sense blocked at the river mouth. "
            "Proposed mechanism: learned odor library plus inherited magnetic grid - the smolt memorizes "
            "its stream chemistry, the adult crosses the ocean on a magnetic map, and the odor library "
            "takes over at the coast. "
            "What would confirm it: synthetic odor cocktails that steer adults to arbitrary release points, "
            "plus mapped magnetic displacement responses. What would kill it: smolts imprinting on single "
            "compounds with no cocktail effect, or magnetic displacement producing no orientation change. "
            "What it does NOT claim: identification of the odor or receptor today, peer acceptance, or "
            "settled status. This is a proposed path, honestly labeled, and the question stays open until "
            "a real resolution exists."),
        "key_points": [
            "Statement: how do salmon cross an ocean and find one stream - magnetic map plus imprinted odor?",
            "Hasler's olfactory imprinting hypothesis (1950s) is supported but the odor cocktail is unidentified.",
            "Magnetic displacement experiments suggest an ocean-phase magnetic map.",
            "Quinn's long-term studies document the precision and its genetic components.",
            "This walkthrough models the magnetic-plus-odor handoff at the river mouth.",
        ],
        "requirements": [
            "The imprinted chemical signature must be isolated by fractionation, not assumed.",
            "Magnetic experiments need field-strength, ecologically realistic exposures.",
            "Handoff-zone experiments must block senses independently.",
            "Findings must hold across multiple salmon species and watersheds.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_QUINN, CIT_MOURITSEN],
    },
    {
        "key": "whale-strandings",
        "name": "Why Whales Strand Themselves",
        "group": "Foundations",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "problem": ("Healthy whales and dolphins sometimes swim ashore in groups and die, a behavior that "
                    "seems to defy survival. Mass strandings cluster in certain places and times, and "
                    "naval sonar has been linked to some events, but most strandings have no sonar nearby. "
                    "Geomagnetic anomalies, sick leaders followed by loyal pods, and disorienting "
                    "topography are all suspects, and the trigger for most events is unknown."),
        "background": ("Mass strandings have been recorded for centuries, with certain coastlines - parts "
                       "of New Zealand, Tasmania, Cape Cod - seeing repeated events. The sonar connection "
                       "was established in the early 2000s when beaked whales stranded after naval "
                       "exercises, with necropsies showing gas-bubble lesions consistent with panic "
                       "ascents, and several navies have since restricted sonar near known habitats. But "
                       "sonar explains only a minority of strandings. The follow-the-leader hypothesis holds "
                       "that highly social species will follow a sick or disoriented individual ashore, "
                       "supported by observations of pods refusing to leave stranded companions. The "
                       "geomagnetic hypothesis notes that stranding hotspots often sit where magnetic "
                       "contours meet the coast, which could confuse a magnetic navigator, though the "
                       "correlation is disputed. Shallow, gently sloping beaches may also return misleading "
                       "echolocation, since the sonar picture of a gradual slope looks like open water. No "
                       "single account covers the observed pattern."),
        "why_it_matters": ("Strandings kill animals that are often endangered, and every event is a "
                           "welfare emergency for responders. Understanding triggers would let managers "
                           "predict and prevent events, regulate sonar and shipping, and design better "
                           "rescue responses. The mystery also touches navigation, social bonds, and how "
                           "whales perceive coastlines."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads a stranding as a navigation failure compounded by loyalty: "
                     "the Signature approach separates the disorienting trigger from the social amplifier "
                     "that turns one lost whale into a mass event."),
        "sig_solution": (
            LABEL + " Approach S-07: trigger-plus-amplifier separation. "
            "Assumptions: (A1) most mass strandings need both a navigational trigger and a social "
            "amplifier; (A2) triggers differ by species and site - sonar, magnetic anomalies, topography; "
            "(A3) strandings are recorded well enough to test trigger correlations. "
            "Reasoning path: (S1) compile the global stranding record with sonar exercise logs, magnetic "
            "maps, and bathymetry to correlate triggers with events; (S2) test the follow-the-leader "
            "amplifier by comparing stranding sizes in highly social versus solitary species; (S3) model "
            "echolocation returns from stranding-prone beaches to check the acoustic-trap prediction; "
            "(S4) examine whether magnetic-anomaly sites predict strandings after controlling for "
            "coastline shape. "
            "Proposed mechanism: disorientation trigger plus social cascade - one confused animal, often "
            "the leader, draws the bonded pod ashore. "
            "What would confirm it: trigger variables predicting stranding hotspots out of sample, and "
            "acoustic modeling reproducing the trap beaches. What would kill it: strandings showing no "
            "correlation with any trigger variable and no leader-follower structure. "
            "What it does NOT claim: a single cause for all strandings, peer acceptance, or settled "
            "status. This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: what triggers mass strandings - sonar, magnetic confusion, acoustic traps, or social following?",
            "Naval sonar is proven for some beaked-whale events but explains only a minority.",
            "Stranding hotspots recur at the same coastlines for centuries.",
            "Social species strand in groups; the follow-the-leader amplifier is well observed.",
            "This walkthrough correlates global stranding records against trigger variables.",
        ],
        "requirements": [
            "Trigger correlations must be tested out of sample, not just fitted.",
            "Sonar logs and stranding records need to be openly shared and complete.",
            "Acoustic-trap models must use real beach bathymetry.",
            "Species differences must be explained, not averaged away.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_MOURITSEN],
    },
    {
        "key": "lemming-cycles",
        "name": "Why Lemming Populations Cycle",
        "group": "Foundations",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "problem": ("Lemming populations explode and crash on a rough three-to-four-year cycle across the "
                    "Arctic, dragging predators and plants along with them. Predator-prey dynamics, food "
                    "quality, disease, and stress physiology have all been blamed. After a century of study, "
                    "no single driver explains the cycle, and climate change is now disrupting it in ways "
                    "that test every theory at once."),
        "background": ("The lemming cycle is one of ecology's oldest puzzles, noted by naturalists since "
                       "the 1800s and mythologized by the false story of mass suicide leaps into the sea. "
                       "The predator hypothesis, championed through the 20th century, holds that specialist "
                       "predators like stoats and owls lag behind lemming booms and drive the crash; "
                       "predator-exclusion experiments support a role for predation but rarely reproduce the "
                       "full cycle. The plant hypothesis argues that lemmings overgraze and degrade their "
                       "food, with plant chemical defenses and recovery times setting the period. Disease "
                       "and stress models add further layers. Long-term monitoring in Scandinavia and "
                       "Greenland now shows some cycles dampening or collapsing as winters warm and snow "
                       "cover - the lemmings' subnivean refuge - thins, which is consistent with every "
                       "hypothesis and decisive for none. The modern consensus is multi-causal, which is "
                       "honest but not a resolution."),
        "why_it_matters": ("Lemmings are the engine of the Arctic food web; their cycles drive snowy owls, "
                           "Arctic foxes, and the plants they eat. Understanding the cycle is a test of "
                           "ecology's ability to explain population dynamics anywhere, and the climate-driven "
                           "collapse of cycles is a live warning about ecosystem stability."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the lemming cycle as a machine with several gears - predators, "
                     "plants, weather - and the Signature approach measures which gear sets the period by "
                     "watching the machine run with one gear removed at a time."),
        "sig_solution": (
            LABEL + " Approach S-08: gear-removal decomposition. "
            "Assumptions: (A1) the cycle is multi-causal but one driver sets the period while others set "
            "amplitude; (A2) exclusion experiments and natural climate variation act as gear removals; "
            "(A3) long-term datasets are sufficient to fit competing models. "
            "Reasoning path: (S1) fit predator-driven, plant-driven, and weather-driven models to the "
            "multi-decade datasets from Greenland and Scandinavia; (S2) use predator-exclusion and plant "
            "manipulation experiments as decisive tests of each model's core prediction; (S3) exploit the "
            "natural experiment of warming winters as a snow-cover gear removal; (S4) check whether the "
            "period stays constant while amplitude changes, which separates period-setters from "
            "amplitude-setters. "
            "Proposed mechanism: specialist predators set the three-to-four-year period through lagged "
            "numerical response, while plant quality and winter snow set the amplitude and the cycle's "
            "persistence. "
            "What would confirm it: models with predator lag reproducing the period across sites while "
            "plant and snow variables explain amplitude. What would kill it: cycles persisting unchanged "
            "with predators fully excluded. "
            "What it does NOT claim: that predation alone explains everything, peer acceptance, or settled "
            "status. This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: which driver - predators, plants, disease, or weather - generates the lemming cycle?",
            "The cycle has run for recorded history; the mass-suicide story is a myth.",
            "Predator-exclusion experiments implicate predation but do not reproduce the full cycle.",
            "Warming winters are dampening some cycles - a natural experiment on all hypotheses.",
            "This walkthrough fits competing cycle models to long-term Arctic datasets.",
        ],
        "requirements": [
            "Models must be fit to multi-decade data, not single cycles.",
            "Exclusion experiments need proper controls and multi-year runs.",
            "The warming-winter natural experiment must be analyzed, not just noted.",
            "Period and amplitude must be explained separately.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_DINGLE],
    },
    {
        "key": "desert-ant-navigation",
        "name": "How Desert Ants Navigate",
        "group": "Foundations",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "problem": ("Desert ants forage across featureless sand in blazing heat, then run straight home "
                    "from hundreds of meters away. They do it with path integration: a polarized-light "
                    "compass in the sky plus a step-counter odometer, continuously summed into a home vector. "
                    "Rudiger Wehner decoded the system over decades, but the neural circuit that performs "
                    "the vector math - in a brain smaller than a grain of sand - is still not fully mapped."),
        "background": ("Wehner's work on Cataglyphis ants, beginning in the 1960s, is one of the triumphs "
                       "of animal behavior research. He showed that ants read the polarization pattern of "
                       "the sky through specialized eye regions, count their steps with a stride integrator, "
                       "and combine the two into a continuously updated home vector - proven by the classic "
                       "experiments that put stilts or stumps on ants' legs and watched them overshoot or "
                       "undershoot home. The compass and odometer are settled. What remains open is the "
                       "neural implementation: how the central complex of the insect brain represents the "
                       "vector, performs the integration, and corrects for wind drift and uneven terrain. "
                       "Recent work has identified candidate ring-neuron circuits in fruit flies, but the "
                       "ant's full path-integration circuit, with its odometer input and error correction, "
                       "has not been completely traced. It is a solved system with an unsolved brain."),
        "why_it_matters": ("Path integration is the purest example of an animal doing vector mathematics "
                           "with minimal hardware, and mapping the circuit would be a landmark for "
                           "neuroscience. The principles feed directly into small-robot navigation and "
                           "neuromorphic computing. It is also the clearest window into how much "
                           "computation a tiny brain can really do."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the ant as a surveyor with a sky compass and a pedometer, "
                     "and the Signature approach traces the surveyor's arithmetic down into the brain's "
                     "wiring to find where the home vector lives."),
        "sig_solution": (
            LABEL + " Approach S-09: circuit-tracing ascent. "
            "Assumptions: (A1) the home vector is represented in the central complex as a bump of "
            "neural activity; (A2) compass input arrives via polarization-sensitive pathways and odometer "
            "input via proprioceptive stride signals; (A3) the circuit is homologous to the mapped "
            "fruit-fly heading circuit. "
            "Reasoning path: (S1) record from central-complex neurons while ants walk on treadmills under "
            "rotated polarization patterns; (S2) trace the stride-signal pathway from legs to brain with "
            "genetic and anatomical tools; (S3) build a spiking-neuron model of the integrator and test it "
            "against the stilt-and-stump error patterns; (S4) perturb candidate integrator neurons and "
            "measure homing errors. "
            "Proposed mechanism: ring-attractor heading representation plus leaky vector integration - the "
            "brain keeps a moving bump for direction and accumulates stride-scaled steps into a home vector. "
            "What would confirm it: a complete traced circuit whose simulation reproduces real homing errors. "
            "What would kill it: homing persisting after silencing the entire candidate circuit. "
            "What it does NOT claim: that the circuit is mapped today, peer acceptance, or settled status. "
            "This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: how does the ant brain implement path integration - the compass-plus-odometer vector math?",
            "Wehner (from the 1960s) decoded the compass and odometer; the neural circuit is the open part.",
            "Stilt and stump experiments proved the stride integrator exists.",
            "Fruit-fly work has mapped a heading circuit; the ant integrator is still being traced.",
            "This walkthrough simulates vector integration with adjustable compass and odometer noise.",
        ],
        "requirements": [
            "Neural recordings must happen during real walking, not restrained preparations.",
            "Perturbation experiments must target the integrator specifically.",
            "Models must reproduce the classic stilt-and-stump error patterns.",
            "Findings must generalize across Cataglyphis species.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_WEHNER],
    },
    {
        "key": "electroreception",
        "name": "How Electric Fish Sense Electricity",
        "group": "Foundations",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "problem": ("Electric fish generate weak electric fields and read distortions in them to navigate, "
                    "hunt, and communicate in muddy water where eyes are useless. The physics and the "
                    "electroreceptors are well described, but the evolutionary origins are open: electric "
                    "organs evolved independently at least six times in fish, from muscle tissue, and nobody "
                    "fully understands what sequence of small steps turns a muscle into a battery."),
        "background": ("African mormyrids and South American gymnotiforms - the knifefishes - evolved "
                       "electrogenesis independently, and both groups use it for electrolocation and "
                       "electrocommunication, with species-specific discharge patterns functioning like "
                       "dialects. The electric organ derives from skeletal muscle: electrocytes are modified "
                       "muscle cells that lost contractility and stacked their membranes to sum voltages. "
                       "Comparative genomics has begun tracing the regulatory changes, but the stepwise "
                       "path - which mutations came first, how a half-electric organ paid its way - is "
                       "reconstructed only in outline. The communication side is equally open: how the "
                       "brain decodes conspecific discharge patterns, jamming avoidance responses, and the "
                       "social meaning of electric chatter are active research areas. Electroreception is a "
                       "sense humans lack entirely, which makes its evolution a window into genuinely alien "
                       "animal experience."),
        "why_it_matters": ("Independent evolution of the same complex system six times is a natural "
                           "experiment in convergent evolution, and decoding it would illuminate how "
                           "novel organs originate. The signal-processing feats of the electrosensory brain "
                           "inspire engineered sensors. And understanding electric communication matters for "
                           "conservation of these diverse freshwater faunas."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the electric organ as a muscle that quit contracting and "
                     "started signaling, and the Signature approach rewinds the tape to find the first "
                     "profitable step from twitch to transmission."),
        "sig_solution": (
            LABEL + " Approach S-10: muscle-to-battery rewind. "
            "Assumptions: (A1) electroreception preceded electrogenesis - passive sensing of other "
            "animals' fields came first; (A2) each independent origin followed a similar regulatory "
            "rewiring of muscle genes; (A3) intermediate stages are visible in living weakly electric "
            "species. "
            "Reasoning path: (S1) compare electric-organ transcriptomes across all six independent "
            "origins to find the shared regulatory rewiring; (S2) reconstruct ancestral electrocyte "
            "states from weakly electric intermediates; (S3) test which first step - passive sensing "
            "amplification or weak discharge - pays for itself in murky-water foraging models; (S4) decode "
            "the communication code by correlating discharge patterns with social outcomes. "
            "Proposed mechanism: passive-first stepwise conversion - electroreception evolved for prey "
            "detection, weak discharges arose as social signals, and selection then stacked electrocytes "
            "for power. "
            "What would confirm it: shared regulatory changes across independent origins and intermediates "
            "showing the predicted sequence. What would kill it: electric organs with no trace of the "
            "muscle regulatory program, implying a different origin. "
            "What it does NOT claim: the full stepwise fossil of each origin, peer acceptance, or settled "
            "status. This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: what stepwise path turns muscle into an electric organ, six times independently?",
            "Electric organs are modified muscle; electrocytes are stacked non-contracting cells.",
            "Mormyrids and gymnotiforms converged on electrolocation and electrocommunication.",
            "Discharge patterns act as species dialects; the social code is still being decoded.",
            "This walkthrough models the passive-sensing-first stepwise conversion.",
        ],
        "requirements": [
            "Transcriptome comparisons must cover all six independent origins.",
            "Intermediate species must show the predicted stepwise states.",
            "First-step models must show a real fitness payoff, not just plausibility.",
            "Communication decoding needs controlled social experiments.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_DINGLE],
    },
    {
        "key": "no-wheels",
        "name": "Why There Are No Wheels in Nature",
        "group": "Foundations",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "problem": ("Wheels are humanity's greatest locomotion invention, yet no animal has ever evolved a "
                    "true rotating wheel for travel. Tumbleweeds roll, dung beetles roll balls, and "
                    "bacterial flagella spin like propellers - but no multicellular animal rolls on "
                    "body-part wheels. The standard answer is that a freely rotating part cannot stay "
                    "connected to the body's blood and nerves, but whether that constraint is truly "
                    "absolute remains an open question in evolutionary biomechanics."),
        "background": ("The puzzle is old and the near-misses are famous. The bacterial flagellum is a "
                       "genuine rotary motor, proof that evolution can build rotation at the molecular "
                       "scale, where no plumbing problem exists. Pangolins and armadillos curl into balls "
                       "and roll downhill, and some spiders cartwheel down dunes - whole-body rolling, not "
                       "wheeled limbs. The continuity argument, formalized by biomechanists, holds that a "
                       "wheel needs an axle, and an axle needs bearings, and bearings need the rotating "
                       "part to be disconnected from the body - impossible for a limb that needs blood, "
                       "nerves, and muscles. But critics note that evolution could in principle route "
                       "around this: a wheel could be dead tissue grown and shed like a shell, or powered "
                       "inductively, or the whole animal could be the wheel. The question has never been "
                       "settled by a formal impossibility proof; it rests on plausibility and the "
                       "suspicious completeness of the absence."),
        "why_it_matters": ("The no-wheels puzzle is the sharpest test of how constraints shape evolution: "
                           "it asks what evolution cannot do, not just what it has done. A formal answer "
                           "would bound the space of possible animal forms. And the near-misses - flagella, "
                           "rolling spiders, ball-rolling beetles - each illuminate a different workaround."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the missing wheel as a forbidden design: the Signature "
                     "approach maps the exact constraint boundary to see whether the wheel is truly "
                     "impossible or merely unprofitable."),
        "sig_solution": (
            LABEL + " Approach S-11: constraint-boundary mapping. "
            "Assumptions: (A1) the continuity constraint - blood, nerves, and muscle must cross any "
            "joint - is the primary barrier; (A2) workarounds like dead-tissue wheels or whole-body "
            "rolling define the boundary of the possible; (A3) a design is impossible if no stepwise "
            "path of small advantageous mutations reaches it. "
            "Reasoning path: (S1) enumerate all proposed wheel architectures and test each against the "
            "continuity constraint; (S2) model the fitness landscape: would a half-wheel - a rocking "
            "disk, a partial roller - pay for itself; (S3) examine the near-misses to see which "
            "constraint each one evades; (S4) test whether any environment - flat hard desert, say - "
            "would make wheels profitable enough to select for. "
            "Proposed mechanism: unprofitable-intermediate blockade - wheels are not physically "
            "impossible but unreachable, because every halfway design is worse than legs and no "
            "workaround beats the continuity cost. "
            "What would confirm it: fitness models showing all partial wheels lose to legs in every "
            "tested environment. What would kill it: a discovered animal with a true rotating "
            "locomotory structure, or a viable engineering workaround biology could plausibly grow. "
            "What it does NOT claim: a formal impossibility proof, peer acceptance, or settled status. "
            "This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: is the wheel truly impossible for animals, or just unreachable by small steps?",
            "The bacterial flagellum proves evolution can build rotary motors at molecular scale.",
            "The continuity argument: a wheel cannot stay plumbed with blood and nerves.",
            "Near-misses - rolling spiders, ball-rolling beetles - evade rather than solve the constraint.",
            "This walkthrough models the fitness of partial-wheel intermediates against legs.",
        ],
        "requirements": [
            "Any impossibility claim needs a formal constraint argument, not just absence.",
            "Partial-wheel models must be tested across environments, not one.",
            "Near-misses must be analyzed for which constraint each evades.",
            "A single true wheel in nature would end the debate instantly.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_DARWIN],
    },
    {
        "key": "cephalopod-camouflage",
        "name": "How Cephalopods Change Color and Texture",
        "group": "Foundations",
        "ladder_rank": 12,
        "ladder_tier": "foundations",
        "problem": ("An octopus can match the color, pattern, brightness, and even three-dimensional "
                    "texture of its surroundings in under a second, and most cephalopods are colorblind. "
                    "Chromatophores, iridophores, and leucophores are the hardware, but the control "
                    "software - how the brain decides what pattern to wear, and how it senses the "
                    "background without color vision - is still not fully understood."),
        "background": ("The hardware has been described since the 19th century: chromatophores are "
                       "pigment sacs stretched by radial muscles under direct neural control, giving "
                       "cephalopods the fastest color change in the animal kingdom; iridophores reflect "
                       "light structurally; leucophores scatter it white. Papillae under muscular control "
                       "raise the skin into spikes and ridges for texture. The paradox is sensory: "
                       "behavioral tests show most cephalopods cannot distinguish colors, yet they match "
                       "colored backgrounds. The leading resolution is that they sense brightness, "
                       "contrast, and possibly polarization patterns and match those, which suffices for "
                       "camouflage against predators that also key on contrast. But the central question "
                       "remains open: how does the brain compute the target pattern, and where is the "
                       "pattern library stored? Work on cuttlefish shows pattern selection involves the "
                       "optic lobes and responds to visual features like edges and contrast, yet the "
                       "complete sensorimotor loop from eye to skin has not been traced."),
        "why_it_matters": ("Cephalopod camouflage is the gold standard for adaptive materials, and "
                           "understanding the control loop would transform camouflage technology, soft "
                           "robotics, and displays. Biologically, it is the deepest case study of "
                           "brain-to-body pattern generation, and of perception without the senses we "
                           "assume are required."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the octopus as a painter that cannot see color: the "
                     "Signature approach asks what minimal visual vocabulary - edges, contrast, "
                     "polarization - suffices to paint a convincing forgery of the seafloor."),
        "sig_solution": (
            LABEL + " Approach S-12: minimal-vocabulary decode. "
            "Assumptions: (A1) background matching uses brightness, contrast, edges, and polarization, "
            "not color; (A2) the brain holds a finite library of pattern components combined on demand; "
            "(A3) the eye-to-skin loop is traceable through the optic lobes. "
            "Reasoning path: (S1) test pattern matching against backgrounds that isolate color from "
            "contrast and polarization; (S2) record optic-lobe activity while animals match controlled "
            "patterns; (S3) enumerate the pattern-component library by clustering observed camouflage "
            "displays; (S4) build a sensorimotor model that takes a background image and outputs a skin "
            "pattern, and test it against live animals. "
            "Proposed mechanism: contrast-grammar camouflage - the brain parses the background into a "
            "grammar of light and dark components and assembles the matching display from a finite "
            "component set, with papillae adding the texture channel. "
            "What would confirm it: a model that predicts the animal's pattern from background features "
            "alone, plus isolated polarization-only matching. What would kill it: successful color "
            "matching on backgrounds equated for brightness, contrast, and polarization - proving true "
            "color vision. "
            "What it does NOT claim: the traced circuit today, peer acceptance, or settled status. This "
            "is a proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: how does a colorblind animal match colored backgrounds in under a second?",
            "Chromatophores, iridophores, leucophores, and muscular papillae are the hardware.",
            "Most cephalopods fail color-discrimination tests yet match colored backgrounds.",
            "The leading account: they match brightness, contrast, edges, and polarization instead.",
            "This walkthrough tests which visual vocabulary suffices for background matching.",
        ],
        "requirements": [
            "Backgrounds must isolate color from contrast and polarization.",
            "Neural recordings must cover the full eye-to-skin loop.",
            "The pattern-component library must be enumerated, not assumed.",
            "Predictive models must be tested against live animals.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_DINGLE],
    },
    {
        "key": "consciousness-markers",
        "name": "What Marks an Animal as Conscious",
        "group": "Compounded",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("Which animals are conscious, and how would we know? Behavior suggests rich inner "
                    "lives in mammals and birds, and increasingly in octopuses, fish, and even insects - "
                    "but behavior can be mimicked by reflex. The field needs objective markers of "
                    "sentience: neural, behavioral, or computational signatures that distinguish "
                    "experience from automation. No agreed marker set exists."),
        "background": ("Donald Griffin reopened the scientific study of animal minds in the 1970s and "
                       "1980s, arguing that the taboo on animal consciousness was unscientific. The "
                       "Cambridge Declaration on Consciousness in 2012, signed by prominent neuroscientists, "
                       "stated that mammals, birds, and octopuses possess the neural substrates of "
                       "consciousness. Since then the evidence has widened: bees show pessimism biases "
                       "after stress, fish show emotional fever, crabs show anxiety-like states, and "
                       "octopuses play and explore. But skeptics note that every behavior cited - "
                       "self-recognition, metacognition, affective bias - can in principle be implemented "
                       "without subjective experience, and there is no agreed test that separates the "
                       "two. The hard problem of consciousness in humans bleeds directly into the animal "
                       "question: without a theory of what consciousness is, markers are educated guesses."),
        "why_it_matters": ("The answer sets the moral boundary of the animal kingdom: which species deserve "
                           "welfare protection, humane treatment, and legal standing. Billions of farmed "
                           "fish, crustaceans, and insects hang on this question. Scientifically, markers of "
                           "animal consciousness would constrain theories of consciousness itself."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads sentience as a signature written across behavior, brain, "
                     "and computation: the Signature approach looks for the convergent fingerprint where "
                     "all three agree, rather than trusting any single witness."),
        "sig_solution": (
            LABEL + " Approach S-13: convergent-fingerprint markers. "
            "Assumptions: (A1) consciousness leaves correlated traces across behavior, neural "
            "architecture, and information integration; (A2) no single marker is decisive, but a "
            "convergent set is; (A3) human report calibrates the markers, animal data extends them. "
            "Reasoning path: (S1) assemble the candidate marker set - global-workspace-like broadcasting, "
            "recurrent processing, affective bias, metacognition, flexible learning, self-modeling; "
            "(S2) score each marker across taxa from insects to primates; (S3) test which markers cluster "
            "together across species, defining the fingerprint; (S4) validate the fingerprint against "
            "human clinical cases of disrupted consciousness. "
            "Proposed mechanism: graded sentience - consciousness is not binary but a graded property, "
            "and species carry different depths of the fingerprint, from minimal affective states in "
            "simple animals to full self-models in great apes, corvids, and cephalopods. "
            "What would confirm it: markers clustering tightly across independent taxa and predicting "
            "welfare-relevant outcomes. What would kill it: markers scattering randomly, or full marker "
            "sets in animals with no behavioral flexibility. "
            "What it does NOT claim: a solved hard problem, peer acceptance, or settled status. This is "
            "a proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: what objective markers distinguish conscious experience from complex reflex?",
            "The Cambridge Declaration (2012) affirmed neural substrates of consciousness in mammals, birds, and octopuses.",
            "Bees, fish, and crabs show affective-bias behaviors once thought to require human-like minds.",
            "Every behavioral marker can in principle be implemented without experience - the core difficulty.",
            "This walkthrough scores candidate markers across taxa to find the convergent fingerprint.",
        ],
        "requirements": [
            "Markers must be calibrated against human consciousness cases first.",
            "No single marker can be decisive; convergence is required.",
            "Behavioral tests need controls for non-conscious implementation.",
            "The framework must handle graded, not binary, sentience.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_GRIFFIN, CIT_CAMBRIDGE],
    },
    {
        "key": "animal-language",
        "name": "Do Non-Human Animals Have Language",
        "group": "Compounded",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("Prairie dogs have distinct calls for different predators, even describing their speed "
                    "and color. Vervet monkeys have separate alarm calls for eagles, leopards, and snakes. "
                    "Whales sing songs that evolve culturally. But do any of these systems have what makes "
                    "human language special - open-ended, recursive, combinatorial meaning? The origin of "
                    "language in non-humans is one of the most contested questions in science."),
        "background": ("The modern debate was framed by Hauser, Chomsky, and Fitch in 2002, distinguishing "
                       "the faculty of language in the broad sense - shared with other animals - from the "
                       "narrow sense, recursion, claimed as uniquely human. Fieldwork keeps complicating "
                       "the picture: Con Slobodchikoff's prairie dog research documented calls that encode "
                       "predator type, size, speed, and even the color of human clothing; Campbell's "
                       "monkeys combine calls with different meanings; humpback whale songs show cultural "
                       "transmission across ocean basins. Laboratory work with apes, parrots, and dolphins "
                       "has shown impressive symbol use but never spontaneous recursive syntax. The "
                       "evolutionary question is equally open: did language evolve gradually from animal "
                       "communication, or did a single cognitive leap create it? W. Tecumseh Fitch's "
                       "comparative program has shown many language components - vocal learning, "
                       "intentionality, combinatorial calls - distributed across species, but the assembly "
                       "of the full system remains unexplained."),
        "why_it_matters": ("Language is the trait humans cite most for their uniqueness; its origin story "
                           "defines our place in nature. Practically, understanding animal communication "
                           "systems improves conservation, welfare, and human-animal interaction. The "
                           "question also drives linguistics, cognitive science, and AI research on "
                           "communication."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads animal communication as a set of components scattered "
                     "across species: the Signature approach inventories the components and asks what "
                     "assembly rule turns a communication system into a language."),
        "sig_solution": (
            LABEL + " Approach S-14: component-assembly inventory. "
            "Assumptions: (A1) language decomposes into components - vocal learning, reference, "
            "combination, recursion, intentionality, cultural transmission; (A2) components are "
            "distributed across taxa and can be scored independently; (A3) the uniquely human assembly "
            "is the open question, not the components. "
            "Reasoning path: (S1) score each component across primates, cetaceans, birds, and other "
            "vocal learners; (S2) test combinatorial meaning rigorously: do combined calls mean the "
            "combination of parts, or a new whole; (S3) search for recursion-like embedding in natural "
            "sequences with formal analysis; (S4) model which assembly of components yields open-ended "
            "meaning and check which species approach it. "
            "Proposed mechanism: gradual assembly - no single leap; components accumulated across "
            "lineages, and the human system is the only known full assembly, with recursion as the "
            "last-added piece. "
            "What would confirm it: a non-human species demonstrating productive combinatorial meaning "
            "with novel combinations understood by naive listeners. What would kill the gradual view: "
            "a demonstrated cognitive wall - no animal ever combining signals productively despite "
            "possessing all components. "
            "What it does NOT claim: that any animal has language today, peer acceptance, or settled "
            "status. This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: do any non-human communication systems have open-ended combinatorial meaning?",
            "Prairie dogs encode predator type, speed, and size; vervets have predator-specific alarms.",
            "Hauser, Chomsky, and Fitch (2002) framed the broad-versus-narrow faculty of language.",
            "Whale songs show cultural evolution; ape symbol use shows no spontaneous recursive syntax.",
            "This walkthrough scores language components across taxa to map the assembly gap.",
        ],
        "requirements": [
            "Combinatorial meaning needs playback tests with novel combinations.",
            "Recursion claims need formal sequence analysis, not anecdote.",
            "Component scoring must be independent across species.",
            "Cultural transmission must be separated from genetic encoding.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_HAUSER, CIT_FITCH],
    },
    {
        "key": "eusociality",
        "name": "How Eusociality Evolved",
        "group": "Compounded",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("Ants, bees, wasps, and termites built societies where most individuals never reproduce, "
                    "devoting their lives to a queen's offspring. Darwin called this a special difficulty "
                    "for his theory: how can sterility evolve by natural selection? Hamilton's kin "
                    "selection answered with relatedness math, but a 2010 broadside by Nowak, Tarnita, and "
                    "Wilson declared kin selection unnecessary and wrong - igniting the fiercest debate in "
                    "modern evolutionary biology, still unresolved."),
        "background": ("Darwin's difficulty stood for a century until W. D. Hamilton's 1964 papers showed "
                       "that genes for altruism spread when the benefit to relatives, discounted by "
                       "relatedness, exceeds the cost - Hamilton's rule, rb greater than c. Haplodiploidy, "
                       "the sex-determination system of ants, bees, and wasps where sisters share "
                       "three-quarters of their genes, seemed to explain why eusociality evolved repeatedly "
                       "in the Hymenoptera. Then came termites, which are diploid and eusocial, and the "
                       "2010 Nature paper by Martin Nowak, Corina Tarnita, and E. O. Wilson arguing that "
                       "haplodiploidy was incidental, kin selection theory was mathematically broken, and "
                       "eusociality evolved through group-level advantages of defended nests and "
                       "pre-adapted parental care. The rebuttals were ferocious - over a hundred "
                       "biologists signed responses defending inclusive fitness. The field has since "
                       "accumulated genomic and phylogenetic data, but no consensus on the relative roles "
                       "of kinship, ecology, and group selection exists."),
        "why_it_matters": ("Eusociality produced the most ecologically dominant animals on Earth - ants "
                           "alone may outweigh humans in biomass. The debate is really about the levels at "
                           "which selection operates, one of evolution's deepest questions. Resolving it "
                           "would unify a century of social-evolution theory."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads eusociality as a fortress problem: the Signature approach "
                     "asks what combination of kinship math and fortress ecology makes a sterile worker "
                     "caste the winning strategy, and which ingredient came first."),
        "sig_solution": (
            LABEL + " Approach S-15: fortress-first sequencing. "
            "Assumptions: (A1) eusociality requires both a pre-adaptation (parental care at a defended "
            "nest) and a genetic system that rewards helping; (A2) phylogenetic reconstructions can "
            "order the steps; (A3) Hamilton's rule and group-benefit models are complementary, not "
            "contradictory. "
            "Reasoning path: (S1) reconstruct the ancestral states of all eusocial lineages to order "
            "nest defense, parental care, and reproductive division; (S2) test whether eusocial origins "
            "cluster in fortress-like ecologies - wood, soil, defended cavities; (S3) measure relatedness "
            "asymmetries at each origin to test the haplodiploidy boost; (S4) model the transition as a "
            "sequence and check which ordering fits the most origins. "
            "Proposed mechanism: fortress-first, kinship-locked - defended nests with parental care made "
            "helping profitable, and high relatedness then locked in irreversibility; haplodiploidy "
            "accelerated the Hymenoptera but was not required. "
            "What would confirm it: fortress ecology preceding reproductive division at most origins, with "
            "relatedness predicting irreversibility. What would kill it: eusocial origins with no "
            "fortress phase and no relatedness asymmetry. "
            "What it does NOT claim: an end to the kin-selection debate, peer acceptance, or settled "
            "status. This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: what combination of kinship and ecology produces sterile worker castes?",
            "Darwin called sterile castes a special difficulty; Hamilton (1964) answered with kin selection.",
            "Nowak, Tarnita, and Wilson (2010) ignited the fiercest debate in modern evolutionary biology.",
            "Termites are diploid and eusocial, complicating the haplodiploidy story.",
            "This walkthrough orders the steps - fortress ecology, parental care, reproductive division - at each origin.",
        ],
        "requirements": [
            "Ancestral reconstructions must cover all eusocial origins, not just ants and bees.",
            "The debate needs decisive phylogenetic tests, not more theory papers.",
            "Relatedness must be measured at origins, not in modern derived species.",
            "Models must allow kinship and group benefits to combine.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_HAMILTON, CIT_NOWAK],
    },
    {
        "key": "maintenance-of-sex",
        "name": "Why Sex Persists Despite the Twofold Cost",
        "group": "Compounded",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("Sex is wildly inefficient: a sexual female produces half as many gene copies as an "
                    "asexual female, since males do not bear offspring. This twofold cost means any "
                    "asexual mutant should sweep through a population. Yet sex dominates the animal "
                    "kingdom, and asexual lineages are rare and short-lived. Why the most expensive "
                    "reproductive system ever invented persists is one of evolution's greatest unsolved "
                    "problems."),
        "background": ("John Maynard Smith formalized the paradox in The Evolution of Sex (1978): all else "
                       "equal, an asexual female doubles her genetic representation each generation "
                       "relative to a sexual one. The leading explanations all invoke enemies and change. "
                       "The Red Queen hypothesis, developed by Leigh Van Valen and championed by Graham "
                       "Bell and William Hamilton, holds that parasites adapt to common host genotypes, "
                       "so sex's shuffling of genes keeps hosts one step ahead - supported by the famous "
                       "New Zealand snail studies where sexual snails dominate parasite-heavy lakes and "
                       "asexuals dominate parasite-free ones. Muller's ratchet argues that asexual "
                       "lineages irreversibly accumulate deleterious mutations, while sex purges them "
                       "through recombination. DNA repair theories note that meiosis repairs double-strand "
                       "breaks. Each has evidence and each has gaps: the Red Queen needs the right "
                       "parasite dynamics, the ratchet needs small populations, and none explains every "
                       "case. The honest consensus is that several forces maintain sex in different "
                       "lineages, with no universal answer."),
        "why_it_matters": ("Sex shapes the entire genetic architecture of animals - recombination, "
                           "chromosomes, mating systems, sexual dimorphism all flow from it. Understanding "
                           "its maintenance would unify evolutionary genetics and explain why asexual "
                           "scandals like bdelloid rotifers are the exceptions. It is also the deepest "
                           "question about the cost-benefit logic of evolution itself."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads sex as an arms-race tax: the Signature approach prices "
                     "the twofold cost against the parasite bill to find the conditions where paying for "
                     "sex is cheaper than going asexual."),
        "sig_solution": (
            LABEL + " Approach S-16: arms-race pricing. "
            "Assumptions: (A1) the twofold cost is real and must be paid by a benefit of equal size; "
            "(A2) parasite pressure is the most general candidate benefit; (A3) different lineages may "
            "pay the cost with different currencies - parasites, mutation purging, repair. "
            "Reasoning path: (S1) model the Red Queen race and compute the parasite virulence and "
            "turnover needed to offset exactly a twofold cost; (S2) test the model's predictions against "
            "the snail, lizard, and fish systems with natural sexual-asexual contrasts; (S3) measure "
            "mutation accumulation in asexual lineages to price the ratchet contribution; (S4) check "
            "whether lineages with weak parasites and large populations - where both theories predict "
            "sex should fail - actually keep it, which would demand a third explanation. "
            "Proposed mechanism: parasite-driven maintenance as the general rule, with mutation purging "
            "as the backup in small populations - sex persists because standing still means losing the "
            "race. "
            "What would confirm it: parasite pressure predicting sexual versus asexual dominance across "
            "independent systems with the twofold threshold. What would kill it: thriving asexual "
            "lineages in parasite-heavy environments with no compensating advantage. "
            "What it does NOT claim: a single universal answer, peer acceptance, or settled status. This "
            "is a proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: what benefit pays the twofold cost of males every generation?",
            "Maynard Smith (1978) formalized the paradox; asexual mutants should win, but do not.",
            "The Red Queen: parasites punish common genotypes, favoring genetic shuffling.",
            "New Zealand snails support the Red Queen; Muller's ratchet covers small populations.",
            "This walkthrough prices the parasite bill against the twofold cost in a race model.",
        ],
        "requirements": [
            "Any explanation must quantitatively offset the full twofold cost.",
            "Natural sexual-asexual contrasts are the decisive test systems.",
            "The ratchet contribution needs direct mutation-accumulation measurement.",
            "A universal claim must survive the asexual scandals like bdelloid rotifers.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_MAYNARD_SEX, CIT_BELL],
    },
    {
        "key": "insect-flight",
        "name": "How Insect Flight Evolved",
        "group": "Compounded",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("Insects were the first animals to fly, some 350 million years ago, and flight made "
                    "them the most diverse animals on Earth. But wings do not fossilize in halfway "
                    "states, and the origin is disputed: did wings evolve from leg-like gill plates used "
                    "for skimming water, from paranotal lobes used for gliding, or from something else "
                    "entirely? The first wingstroke remains one of paleontology's great missing scenes."),
        "background": ("Two classic hypotheses have dueled for a century. The paranotal hypothesis holds "
                       "that lobes on the thorax, originally for thermoregulation or display, enlarged "
                       "into gliding surfaces and then flapping wings. The gill hypothesis, tracing to "
                       "early 20th-century morphologists, argues that wings are modified abdominal gills "
                       "of aquatic nymphs, co-opted for skimming across water before true flight. "
                       "Developmental genetics complicated both: wing-patterning genes like vestigial and "
                       "apterous are expressed in both leg and gill tissues, suggesting wings recruited "
                       "genetic modules from multiple sources. Robin Dudley's biomechanical work showed "
                       "that even small protowings generate useful aerodynamic force, and that "
                       "surface-skimming insects like stoneflies may preserve the transitional behavior. "
                       "Fossils of early winged insects show nearly modern wings, so the transitional "
                       "forms are missing and the sequence is inferred, not observed."),
        "why_it_matters": ("Insect flight launched the most successful radiation in animal history; its "
                           "origin story is the origin story of terrestrial biodiversity. Understanding "
                           "how a novel organ assembles from repurposed parts is a template for all "
                           "evolutionary novelty. The biomechanics also inform micro-air-vehicle design."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the insect wing as a committee product - gill genes, leg "
                     "genes, and aerodynamic demand all at the table - and the Signature approach "
                     "reconstructs the committee's first meeting from the genes and the physics."),
        "sig_solution": (
            LABEL + " Approach S-17: committee-product reconstruction. "
            "Assumptions: (A1) wings recruited gene networks from both gill and leg tissues; (A2) each "
            "intermediate stage - skimming, gliding, flapping - paid its own aerodynamic way; (A3) "
            "living skimming insects preserve transitional biomechanics. "
            "Reasoning path: (S1) map wing-patterning gene expression across gills, legs, and wings in "
            "basal insects to trace the recruitment; (S2) measure aerodynamic force on protowing models "
            "at each size stage to find the first profitable size; (S3) study surface-skimming in living "
            "stoneflies as the behavioral bridge; (S4) test whether the gill-to-wing or lobe-to-wing "
            "path better predicts the gene-expression pattern. "
            "Proposed mechanism: aquatic-skimming origin - gill plates used for water-surface skimming "
            "enlarged under selection for longer skims, then carried the insect into the air. "
            "What would confirm it: gene-expression data nesting wings within gill development, plus "
            "aerodynamic models showing skimming pays before gliding. What would kill it: wing genes "
            "showing no gill ancestry and protowings generating no useful force until near-modern size. "
            "What it does NOT claim: the transitional fossils, peer acceptance, or settled status. This "
            "is a proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: did insect wings evolve from gills, from thoracic lobes, or from a recruited mix?",
            "Insects flew 350 million years ago; no halfway wings exist in the fossil record.",
            "Wing genes are expressed in gill and leg tissues, suggesting a committee origin.",
            "Dudley's biomechanics showed small protowings generate useful force.",
            "This walkthrough tests which origin story the gene-expression pattern supports.",
        ],
        "requirements": [
            "Gene-expression comparisons must use basal insects, not just fruit flies.",
            "Aerodynamic models must test every intermediate size, not just modern wings.",
            "Living skimmers must be studied as behavioral models of transition.",
            "Any origin story must pay its way at each stage.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_DUDLEY],
    },
    {
        "key": "bat-echolocation",
        "name": "How Bats Evolved Flight and Echolocation",
        "group": "Compounded",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("Bats are the only mammals that truly fly, and most navigate by echolocation - "
                    "shouting into the dark and reading the echoes. Which came first, flight or "
                    "echolocation? The oldest bat fossil, Onychonycteris, could fly but shows no "
                    "echolocation anatomy, suggesting flight came first. But molecular phylogenies and "
                    "the independent evolution of echolocation in whales complicate the story, and the "
                    "sequence of this double invention is still debated."),
        "background": ("Bats appeared around 52 million years ago, and the Eocene fossil Onychonycteris "
                       "had wings for powered flight but a cochlea too small for echolocation - the key "
                       "evidence for flight-first. Yet the story is not clean: some researchers argue "
                       "echolocation could have evolved first for orientation in cluttered forests, with "
                       "flight following. Molecular work by Teeling and colleagues placed bats within "
                       "Laurasiatheria and showed echolocation-related genes like prestin under strong "
                       "selection in both bats and toothed whales - a stunning convergence of the same "
                       "molecular machinery in two independent origins. The larynx, cochlea, and brain "
                       "all had to be rebuilt for sonar, and the order of those rebuilds relative to "
                       "wing evolution is reconstructed from fragmentary fossils and gene trees, not "
                       "observed."),
        "why_it_matters": ("The bat double-invention is the premier case study of how two complex systems "
                           "co-evolve: flight demands navigation, navigation rewards flight. Understanding "
                           "the sequence illuminates correlated evolution generally. The convergent "
                           "molecular evolution with whales is one of the deepest findings in modern "
                           "genomics."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the bat as a double invention with an order: the Signature "
                     "approach sequences the inventions by asking which one pays for itself alone."),
        "sig_solution": (
            LABEL + " Approach S-18: invention-order sequencing. "
            "Assumptions: (A1) each invention had to pay its own way before the other existed; (A2) "
            "Onychonycteris represents a genuine flight-without-sonar stage; (A3) convergent prestin "
            "evolution in whales reveals the molecular path of sonar. "
            "Reasoning path: (S1) model the fitness of gliding-plus-vision, flight-plus-vision, and "
            "gliding-plus-sonar intermediates to find the profitable order; (S2) date the prestin and "
            "cochlear gene-selection events relative to wing fossils on the bat tree; (S3) test whether "
            "nocturnal insect abundance could have selected for flight alone; (S4) compare with the "
            "whale sequence, where echolocation evolved in already-aquatic animals. "
            "Proposed mechanism: flight-first, sonar-second - nocturnal flight into insect-rich night "
            "skies paid for wings, then selection for navigating cluttered forests at speed built "
            "echolocation on the flight platform. "
            "What would confirm it: gene-selection dates for sonar machinery postdating the earliest "
            "flight fossils, and fitness models favoring flight-alone over sonar-alone. What would kill "
            "it: a fossil or gene signal of sonar anatomy predating powered flight. "
            "What it does NOT claim: the complete fossil sequence, peer acceptance, or settled status. "
            "This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: which evolved first in bats - powered flight or echolocation?",
            "Onychonycteris (52 million years ago) flew but shows no sonar anatomy: the flight-first evidence.",
            "Prestin and other sonar genes converged between bats and toothed whales.",
            "Teeling et al. (2005) placed bats phylogenetically and dated the radiation.",
            "This walkthrough prices each invention alone to find the profitable order.",
        ],
        "requirements": [
            "Fossil cochlea measurements must be the anatomical standard.",
            "Gene-selection dates need calibrated molecular clocks.",
            "Fitness models must test every intermediate combination.",
            "The whale convergence must be explained, not just noted.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_TEELING],
    },
    {
        "key": "regeneration",
        "name": "Why Some Animals Regenerate and Mammals Cannot",
        "group": "Compounded",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("A salamander regrows a perfect leg - bone, muscle, nerves, skin - in weeks. A zebrafish "
                    "regrows its heart. A human cannot regrow so much as a fingertip past childhood. The "
                    "genes for regeneration exist in mammals but are silenced or repurposed, and nobody "
                    "fully understands what switch was thrown in our lineage, or why evolution would "
                    "discard such a useful ability."),
        "background": ("Regeneration is ancient and widespread: salamanders regrow limbs, tails, jaws, and "
                       "even parts of the heart; zebrafish regrow fins and cardiac muscle; planarian "
                       "flatworms regrow their entire bodies from fragments. Jeremy Brockes and Anoop "
                       "Kumar's comparative reviews established that regeneration uses a blastema - a mass "
                       "of dedifferentiated cells - plus positional memory that tells the regrowing limb "
                       "where it is. Mammals form scars instead of blastemas: fibroblasts rush in and "
                       "seal the wound, blocking regeneration. The leading explanations for the mammalian "
                       "loss invoke trade-offs: rapid wound sealing prevents infection and cancer, and the "
                       "tumor-suppressor systems that protect long-lived warm-blooded animals may "
                       "inherently block the cell plasticity regeneration needs. But the exact genetic "
                       "switches, and whether they could be flipped without unleashing cancer, remain "
                       "open. The axolotl genome, sequenced in 2018, gave researchers the full parts list "
                       "for the first time."),
        "why_it_matters": ("Regenerative medicine is the most direct human payoff: understanding the "
                           "mammalian block could one day let us regrow organs instead of transplanting "
                           "them. The cancer-regeneration trade-off is also a fundamental question about "
                           "why complex animals accept permanent injury. It is biology's most practical "
                           "unsolved problem."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads mammalian scarring as a locked door with the key still in "
                     "the lock: the Signature approach compares the locked and unlocked genomes to find "
                     "exactly which tumblers differ."),
        "sig_solution": (
            LABEL + " Approach S-19: lock-and-key comparison. "
            "Assumptions: (A1) mammals retain the regeneration gene toolkit in silenced form; (A2) the "
            "block is regulatory - scarring outruns blastema formation - rather than loss of genes; "
            "(A3) the cancer trade-off is real and constrains any unlocking. "
            "Reasoning path: (S1) compare axolotl and mouse wound-response transcriptomes hour by hour "
            "to find the divergence point; (S2) test whether delaying mammalian scarring permits "
            "blastema-like formation; (S3) identify the positional-memory signals salamanders use and "
            "check for their mammalian remnants; (S4) model the cancer risk of each candidate switch to "
            "find unlocks that do not unleash tumors. "
            "Proposed mechanism: scarring-outruns-blastema - mammals sealed wounds fast to survive "
            "infection and cancer, and the speed of the scar response competitively excludes the "
            "slower blastema program; the unlock is timing, not new genes. "
            "What would confirm it: delayed-scarring mammals forming blastemas and regenerating patterned "
            "tissue. What would kill it: no blastema formation under any scarring delay, implying the "
            "program is truly lost. "
            "What it does NOT claim: a therapy, a safe unlock, peer acceptance, or settled status. This "
            "is a proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: what genetic and regulatory switches block mammalian regeneration?",
            "Salamanders regrow limbs, jaws, and heart tissue; mammals scar instead.",
            "Brockes and Kumar established the blastema and positional-memory framework.",
            "The leading account: fast scarring and tumor suppression trade off against regeneration.",
            "The axolotl genome (2018) gave the first complete parts list for a regenerator.",
            "This walkthrough compares wound-response timelines to find the divergence point.",
        ],
        "requirements": [
            "Comparisons must be hour-by-hour transcriptomes, not single snapshots.",
            "Any unlock must be tested for cancer risk, not just regrowth.",
            "Positional memory must be demonstrated, not just cell proliferation.",
            "Findings must hold across mammalian models, not one strain.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_BROCKES],
    },
    {
        "key": "vertebrate-jaw",
        "name": "How the Vertebrate Jaw Evolved",
        "group": "Compounded",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("Jaws made vertebrates the dominant predators of the seas and then the land - but "
                    "jaws evolved from gill arches, structures built for breathing, not biting. How a "
                    "respiratory arch became a hinged, muscled, toothed jaw is one of the great "
                    "transformations in animal history, and the developmental and fossil details are "
                    "still being worked out."),
        "background": ("The classical account, refined over a century, holds that the mandibular arch - "
                       "the frontmost gill arch of jawless fishes - was co-opted and hinged to form the "
                       "upper and lower jaws, with the next arch back becoming the hyoid support. Fossils "
                       "of early jawed fishes like placoderms show the transition in progress, with "
                       "bony plates around the mouth becoming true jaws. Developmental biology added the "
                       "mechanism: neural crest cells pattern the arches, and Hox gene expression "
                       "boundaries define which arch becomes what - J. Mallatt's synthesis showed how "
                       "shifts in these patterning systems could transform arch identity. Yet open "
                       "questions persist: which came first, the hinge joint or the bite musculature; how "
                       "teeth, which evolved separately as skin denticles, were recruited onto jaws; and "
                       "whether the transformation happened once or in parallel across early fish "
                       "lineages. The jaw is a composite invention, and its assembly order is the "
                       "mystery."),
        "why_it_matters": ("Jaws underpin the entire vertebrate radiation - every predator from sharks to "
                           "lions to humans bites with this invention. Understanding its assembly is a "
                           "template for how complex structures evolve by repurposing parts. The "
                           "developmental genetics also illuminate birth defects of the human face and "
                           "jaw."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the jaw as a breathing arch promoted to weapon: the "
                     "Signature approach reconstructs the promotion order - hinge, muscle, teeth - from "
                     "fossils and embryos together."),
        "sig_solution": (
            LABEL + " Approach S-20: promotion-order reconstruction. "
            "Assumptions: (A1) the mandibular arch is the jaw precursor and the hyoid arch the support; "
            "(A2) hinge, musculature, and teeth were recruited in a definite order; (A3) living "
            "jawless fishes preserve the pre-jaw arch patterning. "
            "Reasoning path: (S1) map neural-crest and Hox patterning across lamprey, shark, and bony "
            "fish embryos to find the patterning shifts; (S2) order fossil jaw elements from placoderms "
            "through early sharks to sequence hinge versus muscle versus teeth; (S3) test which "
            "recruitment order is developmentally plausible by perturbing arch patterning in model "
            "fish; (S4) check whether teeth joined jaws once or repeatedly. "
            "Proposed mechanism: hinge-first assembly - the arch joint formed for improved ventilation "
            "pumping, bite musculature followed to exploit the hinge, and dermal teeth were recruited "
            "last onto the biting margins. "
            "What would confirm it: fossils showing hinged arches without bite musculature, and "
            "developmental perturbations reproducing the sequence. What would kill it: simultaneous "
            "appearance of all three components with no transitional fossils. "
            "What it does NOT claim: the complete fossil series, peer acceptance, or settled status. "
            "This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: in what order were hinge, musculature, and teeth assembled into the jaw?",
            "The mandibular gill arch is the accepted jaw precursor; neural crest patterns the arches.",
            "Placoderm fossils show the transition in progress 400 million years ago.",
            "Mallatt's synthesis linked Hox patterning shifts to arch transformation.",
            "Teeth evolved separately as skin denticles before joining jaws.",
            "This walkthrough orders the assembly from fossil and embryo evidence.",
        ],
        "requirements": [
            "Fossil ordering needs complete jaw apparatuses, not isolated elements.",
            "Developmental models must be tested in multiple fish lineages.",
            "The teeth-recruitment question needs denticle-to-tooth transitional fossils.",
            "Single versus parallel origins must be tested phylogenetically.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_MALLATT],
    },
    {
        "key": "why-animals-age",
        "name": "Why Animals Age",
        "group": "Compounded",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("Evolution selects for survival and reproduction, so why does it build animals that "
                    "fall apart? Aging looks like the opposite of adaptation: bodies decay, fertility "
                    "fades, and death follows on a schedule. The evolutionary theories - mutation "
                    "accumulation, antagonistic pleiotropy, disposable soma - explain why selection "
                    "tolerates aging, but which one dominates, and why some species barely age at all, "
                    "remains open."),
        "background": ("Peter Medawar's mutation accumulation theory (1952) argued that selection weakens "
                       "with age, so late-acting harmful mutations accumulate. George Williams' "
                       "antagonistic pleiotropy (1957) proposed that genes beneficial early in life are "
                       "favored even if they cause decay later - the classic example being genes that "
                       "boost early growth at the cost of late cancer risk. Tom Kirkwood's disposable "
                       "soma theory (1977) framed aging as an energy bargain: maintenance and repair are "
                       "expensive, so animals invest in reproduction instead and let the body decay. All "
                       "three have support, and Kirkwood's 2005 review showed they are complementary "
                       "rather than rival. The molecular damage theories - telomere shortening, "
                       "mitochondrial decay, epigenetic drift - describe how aging happens, not why "
                       "evolution permits it. The deepest puzzle is negligible senescence: some turtles, "
                       "clams, and sharks show almost no aging, proving that slow decay is biologically "
                       "possible and raising the question of why most animals do not do it."),
        "why_it_matters": ("Aging is the largest cause of human suffering and death; its evolutionary "
                           "logic constrains every medical intervention. Understanding why selection "
                           "permits decay - and how some species escape it - is the foundation of "
                           "geroscience. It is also one of evolution's most profound paradoxes."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads aging as a budget decision written by evolution: the "
                     "Signature approach audits the maintenance-versus-reproduction ledger across species "
                     "to find which account evolution actually balances."),
        "sig_solution": (
            LABEL + " Approach S-21: ledger audit. "
            "Assumptions: (A1) aging is permitted, not programmed, by weakening selection; (A2) the "
            "disposable-soma bargain is the general framework, with mutation accumulation and "
            "antagonistic pleiotropy as its mechanisms; (A3) negligibly senescent species reveal the "
            "price of escaping decay. "
            "Reasoning path: (S1) compare maintenance investment - DNA repair, protein turnover, "
            "antioxidant systems - against reproductive output across the lifespan spectrum; (S2) test "
            "whether negligibly senescent species pay with slow reproduction, as the bargain predicts; "
            "(S3) measure selection gradients at old ages in wild populations to test Medawar's "
            "weakening-selection claim; (S4) identify antagonistic-pleiotropy genes and check whether "
            "their early benefits explain their persistence. "
            "Proposed mechanism: maintenance-budget evolution - species evolve the repair budget that "
            "maximizes lifetime reproduction, and aging is the unrepaired remainder; negligible "
            "senescence evolves where reproduction is slow enough to afford full maintenance. "
            "What would confirm it: repair investment predicting lifespan across taxa with reproductive "
            "rate as the trade-off variable. What would kill it: short-lived species with full repair "
            "budgets aging anyway, or long-lived species with cheap maintenance. "
            "What it does NOT claim: a cure for aging, peer acceptance, or settled status. This is a "
            "proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: which evolutionary logic - mutation accumulation, antagonistic pleiotropy, or disposable soma - best explains aging?",
            "Medawar (1952), Williams (1957), and Kirkwood (1977) framed the three great theories.",
            "Kirkwood (2005) showed the theories are complementary, not rival.",
            "Negligible senescence in some turtles, clams, and sharks proves slow decay is possible.",
            "This walkthrough audits the maintenance-versus-reproduction ledger across species.",
        ],
        "requirements": [
            "Theories must be tested comparatively across the lifespan spectrum.",
            "Negligibly senescent species are the critical test cases.",
            "Selection gradients at old age must be measured in the wild.",
            "Molecular damage must be linked to evolutionary cause, not just correlated.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_KIRKWOOD, CIT_FINCH],
    },
    {
        "key": "parasite-manipulation",
        "name": "How Parasites Control Host Behavior",
        "group": "Compounded",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("Parasites rewrite host behavior with surgical precision: a fungus drives ants to "
                    "climb and bite leaves at the perfect height for spore dispersal; a flatworm makes "
                    "ants' abdomens look like berries to attract birds; a protozoan makes rats lose their "
                    "fear of cats. These manipulations are real and well documented, but the molecular "
                    "mechanisms - how a parasite reaches into a brain and presses specific behavioral "
                    "buttons - are largely unknown."),
        "background": ("The textbook cases are spectacular. Ophiocordyceps fungi infect carpenter ants, "
                       "drive them to elevated biting positions, then fruit through their heads; recent "
                       "work shows the fungus invades muscle, not brain, manipulating behavior from the "
                       "periphery. The lancet fluke Dicrocoelium drives ants to climb grass blades at "
                       "night, where grazing animals eat them. Toxoplasma gondii, infecting a third of "
                       "humanity, removes rats' innate fear of cat odor - with measurable changes in "
                       "amygdala function. Robert Poulin's syntheses document hundreds of such systems. "
                       "But for most, the manipulation is a black box: the parasite's secreted molecules, "
                       "the host receptors they target, and whether the behavior is active manipulation "
                       "or host sickness response are unresolved. Distinguishing true manipulation from "
                       "side effects of infection is the field's central methodological battle."),
        "why_it_matters": ("Behavioral manipulation is the most extreme form of the extended phenotype - "
                           "one genome controlling another's body. Understanding it would illuminate "
                           "neurobiology, since parasites have found the brain's control levers by trial "
                           "and error over millions of years. Toxoplasma's effects on mammals, including "
                           "possible human behavioral links, make the mechanisms a public-health question "
                           "too."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the manipulated host as a hijacked machine: the Signature "
                     "approach traces the hijacker's wires from secreted molecule to behavior to find the "
                     "exact control levers."),
        "sig_solution": (
            LABEL + " Approach S-22: hijack-wire tracing. "
            "Assumptions: (A1) true manipulation uses specific parasite molecules targeting host neural "
            "pathways; (A2) manipulation can be separated from sickness by comparing infected hosts with "
            "and without the behavior; (A3) the levers parasites find reveal conserved neural control "
            "points. "
            "Reasoning path: (S1) profile parasite secretions during the manipulation window to list "
            "candidate molecules; (S2) test candidates by injecting them into uninfected hosts and "
            "scoring the behavior; (S3) map the host neural targets with receptor screens; (S4) apply "
            "the manipulation-versus-sickness test: does the behavior increase parasite transmission "
            "specifically. "
            "Proposed mechanism: peripheral-hijack plus neuromodulation - parasites like Ophiocordyceps "
            "act on muscle and peripheral nerves while others like Toxoplasma modulate central fear "
            "circuits; both converge on hijacking conserved motor and affective pathways. "
            "What would confirm it: isolated parasite molecules reproducing the behavior in healthy hosts "
            "with identified receptors. What would kill it: the behaviors proving to be generic sickness "
            "responses with no transmission benefit. "
            "What it does NOT claim: the molecules identified today, peer acceptance, or settled status. "
            "This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: by what molecular mechanisms do parasites rewrite specific host behaviors?",
            "Ophiocordyceps drives ants to bite leaves; the fungus invades muscle, not brain.",
            "Toxoplasma removes rats' fear of cats via amygdala changes.",
            "Poulin documented hundreds of manipulation systems across taxa.",
            "The central battle: true manipulation versus side effects of sickness.",
            "This walkthrough traces candidate molecules from secretion to behavior.",
        ],
        "requirements": [
            "Candidate molecules must reproduce the behavior when injected alone.",
            "Manipulation must be shown to increase transmission specifically.",
            "Sickness-response controls are mandatory in every experiment.",
            "Host neural targets must be identified, not just inferred.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_POULIN],
    },
    {
        "key": "tool-use",
        "name": "How Tool Use Evolved in Animals",
        "group": "Compounded",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("Chimpanzees crack nuts with stone hammers, crows bend wire into hooks, sea otters "
                    "use rocks as anvils, and octopuses carry coconut shells as armor. Yet most animals, "
                    "including most primates, never use tools at all. What cognitive and ecological "
                    "ingredients separate the tool users from everyone else - and why is the club so "
                    "exclusive?"),
        "background": ("Jane Goodall's 1960s discovery of chimpanzee termite-fishing forced science to "
                       "redefine humanity's uniqueness. Since then the tool-use catalog has grown: New "
                       "Caledonian crows manufacture hooked tools and pass designs down culturally; sea "
                       "otters use stones to crack shellfish; dolphins wear sponges on their beaks while "
                       "foraging; octopuses carry portable shelters. But the distribution is puzzling: "
                       "tool use clusters in extractive foragers - animals that dig embedded foods out of "
                       "substrates - rather than tracking brain size alone. Gorillas rarely use tools "
                       "despite large brains; small-brained crows are master toolmakers. The cognitive "
                       "prerequisites are debated: causal understanding, planning, imitation, or simply "
                       "persistent exploration plus dexterous bodies. Whether animal tool use reflects "
                       "true causal reasoning or trial-and-error refined by social learning remains open, "
                       "and the evolutionary sequence - which ingredient came first - is unresolved."),
        "why_it_matters": ("Tool use was long claimed as the Rubicon of humanity; its presence in other "
                           "species rewrites the story of human uniqueness. Understanding its prerequisites "
                           "illuminates the evolution of intelligence itself. For AI and robotics, animal "
                           "tool use is a natural curriculum for physical reasoning."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads tool use as a recipe with required ingredients: the "
                     "Signature approach tests each ingredient - need, dexterity, cognition, culture - "
                     "across species to find which ones are truly necessary."),
        "sig_solution": (
            LABEL + " Approach S-23: ingredient-necessity testing. "
            "Assumptions: (A1) tool use needs ecological opportunity plus manipulative ability plus "
            "cognitive capacity; (A2) the ingredients can be separated by comparing species that have "
            "some but not all; (A3) cultural transmission amplifies but does not originate tool use. "
            "Reasoning path: (S1) score need (extractive foraging), dexterity, brain measures, and "
            "social learning across tool users and non-users; (S2) test which ingredient best predicts "
            "tool use in a comparative model; (S3) run causal-reasoning experiments that separate true "
            "understanding from trial-and-error; (S4) track how tool designs spread socially to measure "
            "culture's role. "
            "Proposed mechanism: need-first assembly - extractive foraging creates the selective "
            "pressure, manipulative bodies and persistent exploration provide the means, and causal "
            "cognition plus social learning refine the results; no single cognitive Rubicon exists. "
            "What would confirm it: ecological need predicting tool use better than brain size across "
            "taxa. What would kill it: a tool-using species with no extractive foraging and no "
            "manipulative specialization. "
            "What it does NOT claim: that all tool use involves causal reasoning, peer acceptance, or "
            "settled status. This is a proposed path, honestly labeled, and the question stays open "
            "until a real resolution exists."),
        "key_points": [
            "Statement: which ingredients - ecological need, dexterity, cognition, culture - are necessary for tool use?",
            "Goodall's chimpanzee termite-fishing discovery redefined human uniqueness in the 1960s.",
            "New Caledonian crows manufacture hooks; octopuses carry coconut-shell armor.",
            "Tool use tracks extractive foraging better than brain size alone.",
            "This walkthrough tests ingredient necessity across tool users and non-users.",
        ],
        "requirements": [
            "Causal understanding needs experiments separating reasoning from trial-and-error.",
            "Comparisons must include non-tool-users with similar brains and bodies.",
            "Cultural transmission must be measured, not assumed.",
            "Ecological need must be quantified, not narrated.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_GRIFFIN],
    },
    {
        "key": "migration-clocks",
        "name": "How Animals Time Their Migration",
        "group": "Compounded",
        "ladder_rank": 24,
        "ladder_tier": "compounded",
        "problem": ("Captive birds with no view of the sky become restless each autumn and spring, "
                    "fluttering toward their migratory direction on schedule - driven by an internal "
                    "circannual clock that runs without external cues. These clocks keep roughly yearly "
                    "time for years in constant laboratory conditions. But the molecular machinery of a "
                    "year-long timer - how cells count to 365 - is unknown, and how the clock is set by "
                    "day length remains only partly understood."),
        "background": ("Eberhard Gwinner's classic experiments, summarized in his 1986 monograph, proved "
                       "that migratory restlessness (Zugunruhe) and the associated fattening and molt are "
                       "driven endogenously: hand-raised warblers kept in constant day length still "
                       "migrated on schedule, and their clocks free-ran with periods near but not exactly "
                       "a year. Photoperiod entrains the clock - changing day length resets it - but the "
                       "entrainment pathway and the timer itself are open. Circadian clocks are "
                       "understood down to the transcription-translation feedback loops of clock genes, "
                       "but no circannual equivalent has been found; the year-timer may be an emergent "
                       "property of interacting circadian and physiological systems rather than a single "
                       "molecular loop. Climate change is scrambling the cues: migrants now arrive to "
                       "find their food peaks shifted, making the clock's calibration a conservation "
                       "emergency as well as a basic mystery."),
        "why_it_matters": ("Phenological mismatch - migrants mistiming their journeys - is one of climate "
                           "change's sharpest threats to biodiversity. Understanding the clock would let "
                           "conservation predict which species can adjust. Fundamentally, a year-long "
                           "biological timer with no known mechanism is one of physiology's great open "
                           "problems."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the circannual clock as a calendar with no visible pages: "
                     "the Signature approach looks for the calendar in the interaction of daily clocks "
                     "with slow physiology rather than in a single year-gene."),
        "sig_solution": (
            LABEL + " Approach S-24: emergent-calendar search. "
            "Assumptions: (A1) no single circannual gene exists; the timer emerges from coupled "
            "circadian and endocrine systems; (A2) photoperiod entrains the system through melatonin "
            "signaling; (A3) the free-running period near one year is the diagnostic signature. "
            "Reasoning path: (S1) profile gene expression, hormones, and physiology across the full "
            "annual cycle in a model migrant; (S2) perturb candidate coupling pathways and measure "
            "shifts in the free-running period; (S3) build a coupled-oscillator model of circadian plus "
            "slow endocrine loops and test whether year-long periods emerge; (S4) test entrainment by "
            "shifting photoperiod and mapping the reset pathway. "
            "Proposed mechanism: coupled-slow-loop calendar - circadian clock genes drive slow "
            "endocrine feedback loops whose combined dynamics produce a stable near-year period, "
            "entrained by photoperiod via melatonin. "
            "What would confirm it: a coupled model reproducing the free-running period and entrainment, "
            "with perturbations shifting the period predictably. What would kill it: discovery of a "
            "single dedicated circannual molecular loop. "
            "What it does NOT claim: the timer identified today, peer acceptance, or settled status. "
            "This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: what molecular machinery counts out a year in the circannual clock?",
            "Gwinner (1986) proved endogenous circannual rhythms in migratory birds.",
            "Captive birds show migratory restlessness on schedule with no sky cues.",
            "Circadian clocks are solved molecularly; no circannual equivalent is known.",
            "Climate-driven phenological mismatch makes the clock a conservation emergency.",
            "This walkthrough models the year-timer as coupled slow oscillators.",
        ],
        "requirements": [
            "Gene and hormone profiles must cover the full annual cycle.",
            "Perturbations must shift the free-running period, not just correlate.",
            "Models must reproduce both the period and photoperiod entrainment.",
            "Findings must be tested across migratory and resident populations.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_GWINNER, CIT_DINGLE],
    },
    {
        "key": "cambrian-explosion",
        "name": "What Caused the Cambrian Explosion",
        "group": "Advanced",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": ("Around 541 million years ago, nearly all major animal body plans appeared in the "
                    "fossil record within a geologically brief span of 20 to 25 million years - after "
                    "billions of years of microbial and simple multicellular life. Eyes, legs, shells, "
                    "jaws, and brains all debuted in this burst. What triggered it - oxygen, genes, "
                    "ecology, or some combination - is the deepest event-question in animal evolution."),
        "background": ("Darwin worried about the Cambrian in On the Origin of Species, calling the sudden "
                       "appearance of complex animals a difficulty for his theory. Modern dating has only "
                       "sharpened the puzzle: the Ediacaran biota before it were mostly soft-bodied and "
                       "enigmatic, then the Cambrian delivered arthropods, molluscs, chordates, and "
                       "nearly every other phylum in rapid succession. Candidate triggers abound. Rising "
                       "oxygen may have crossed the threshold for large active bodies. The evolution of "
                       "Hox gene clusters and developmental toolkits may have unlocked body-plan "
                       "innovation. Ecological feedbacks - the first predators driving arms races in armor, "
                       "speed, and senses - could have accelerated diversification once it started. Erwin "
                       "and Valentine's synthesis argues for a combination: permissive environment plus "
                       "developmental possibility plus ecological escalation. But the relative weights, "
                       "and whether the 'explosion' is partly an artifact of newly fossilizable hard "
                       "parts, remain genuinely open."),
        "why_it_matters": ("The Cambrian explosion is the founding event of animal biodiversity - every "
                           "body plan alive today traces to it. Understanding its trigger would reveal "
                           "how major evolutionary transitions ignite. It is also the ultimate test of "
                           "whether evolution is gradual or punctuated by revolutions."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the Cambrian as a detonation needing fuel, spark, and "
                     "oxygen: the Signature approach separates the permissive conditions from the actual "
                     "trigger to find what lit the fuse."),
        "sig_solution": (
            LABEL + " Approach S-25: fuel-spark-oxygen separation. "
            "Assumptions: (A1) the explosion needed permissive conditions (oxygen, developmental "
            "toolkit) plus an active trigger; (A2) the trigger is identifiable in the fossil and "
            "geochemical record; (A3) the hard-parts artifact question must be settled first. "
            "Reasoning path: (S1) correct diversification rates for fossilization bias using "
            "soft-bodied Lagerstatten; (S2) align oxygen proxies, Hox-cluster duplications, and first "
            "predator fossils on a single timeline; (S3) test whether diversification accelerates "
            "after the first predators appear, as arms-race theory predicts; (S4) model whether "
            "oxygen alone, genes alone, or ecology alone can reproduce the observed rate. "
            "Proposed mechanism: ecological-escalation trigger on a prepared stage - oxygen and the "
            "developmental toolkit made complex bodies possible, but the first active predators lit "
            "the arms race that drove the burst. "
            "What would confirm it: diversification rates spiking after predator appearance even "
            "controlling for fossilization. What would kill it: the burst dissolving under "
            "fossilization-bias correction, or oxygen rising long after diversification began. "
            "What it does NOT claim: a single cause, peer acceptance, or settled status. This is a "
            "proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: what triggered the geologically sudden appearance of animal body plans 541 million years ago?",
            "Darwin himself flagged the Cambrian as a difficulty for gradual evolution.",
            "Candidate triggers: oxygen rise, Hox developmental toolkits, predator-driven arms races.",
            "Erwin and Valentine argue for a combination; the weights are open.",
            "The hard-parts fossilization artifact must be corrected before any verdict.",
            "This walkthrough aligns oxygen, genes, and predators on one timeline.",
        ],
        "requirements": [
            "Diversification rates must be corrected for fossilization bias.",
            "Oxygen proxies, gene duplications, and fossils need a common timeline.",
            "The predator-first prediction must be tested, not assumed.",
            "No single-cause claim can survive without quantitative weighting.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_DARWIN, CIT_ERWIN],
    },
    {
        "key": "multicellular-origin",
        "name": "How Multicellular Animals Originated",
        "group": "Advanced",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": ("Animals are multicellular, with specialized cell types cooperating in one body - but "
                    "their closest living relatives, the choanoflagellates, are single cells or simple "
                    "colonies. Somewhere in deep time, a choanoflagellate-like ancestor crossed the "
                    "threshold to true animal multicellularity: division of labor, adhesion, and "
                    "communication between cells. How that first transition happened is unknown."),
        "background": ("Nicole King's work established choanoflagellates as the closest unicellular "
                       "relatives of animals, and showed they already possess genes for cell adhesion "
                       "and signaling - cadherins, tyrosine kinases - once thought to be animal "
                       "inventions. This means the molecular toolkit for multicellularity predates "
                       "animals; the transition was regulatory, not the invention of new genes. "
                       "Choanoflagellates form rosette colonies and even differentiate cell types "
                       "within colonies, hinting at the raw materials. But the actual steps - what "
                       "selective pressure favored sticking together, how division of labor evolved, "
                       "how cheaters were suppressed - are inferred, not observed. Sponges, the "
                       "simplest living animals, show what early animal organization may have looked "
                       "like, but the billion-year gap between choanoflagellates and the first animal "
                       "fossils leaves the transition itself in darkness."),
        "why_it_matters": ("The origin of animals is the origin of bodies - of development, of cell "
                           "cooperation, of everything zoology studies. Understanding it would reveal how "
                           "major transitions in individuality occur, a question that spans from cells to "
                           "societies. It is the deepest 'how did we get here' question in biology."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the first animal as a colony that signed a contract: "
                     "the Signature approach asks what the contract's first clause was - and what "
                     "penalty kept cheaters in line."),
        "sig_solution": (
            LABEL + " Approach S-26: first-contract reconstruction. "
            "Assumptions: (A1) the adhesion and signaling toolkit predates animals; (A2) the transition "
            "was driven by ecological advantage of colonies - feeding, size refuge - plus cheater "
            "control; (A3) living choanoflagellate colonies and sponges bracket the transition. "
            "Reasoning path: (S1) measure the fitness advantages of choanoflagellate colony formation "
            "under predation and feeding competition; (S2) identify the regulatory changes that "
            "converted colony genes into developmental programs in early animals; (S3) model cheater "
            "invasion in proto-multicellular colonies to find the required policing; (S4) test whether "
            "sponge cell-type regulation preserves the ancestral contract. "
            "Proposed mechanism: predation-driven contract - colonies survived filter-feeding predators "
            "better than single cells, and the colony then evolved division of labor with policing by "
            "adhesion-dependent signaling. "
            "What would confirm it: colony fitness advantages under predation plus identifiable "
            "regulatory rewiring at the animal root. What would kill it: colonies showing no advantage "
            "under any tested ecological pressure. "
            "What it does NOT claim: the observed transition, peer acceptance, or settled status. This "
            "is a proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: what selective steps converted a choanoflagellate-like ancestor into the first animal?",
            "King showed the multicellularity toolkit predates animals; the transition was regulatory.",
            "Choanoflagellates form colonies with cell differentiation - the raw materials.",
            "The billion-year gap to the first animal fossils leaves the steps unobserved.",
            "This walkthrough models colony fitness and cheater policing at the transition.",
        ],
        "requirements": [
            "Colony advantages must be measured experimentally, not assumed.",
            "Regulatory rewiring must be identified at the animal root.",
            "Cheater-control mechanisms must be demonstrated, not hand-waved.",
            "Sponges must be tested as brackets, not assumed as models.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_KING],
    },
    {
        "key": "bilateral-symmetry",
        "name": "Why Bilateral Symmetry Dominates Animals",
        "group": "Advanced",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": ("Nearly all large active animals - worms, insects, fish, humans - are bilaterally "
                    "symmetric: left mirrors right, with a head at the front. Yet radial symmetry works "
                    "fine for jellyfish and starfish, and asymmetry works for sponges and flatfish. Why "
                    "did one symmetry win the animal kingdom so completely, and why did it evolve in the "
                    "first place?"),
        "background": ("Bilateral symmetry is tied to directed movement: a body with a front and back, "
                       "left and right, can streamline, concentrate senses in a head, and coordinate "
                       "paired limbs. The standard story holds that cephalization - the concentration of "
                       "nervous tissue at the front - coevolved with bilateral symmetry as animals began "
                       "moving purposefully through the world. But the causal arrow is debated: did "
                       "directed locomotion select for bilateral bodies, or did bilateral developmental "
                       "programs enable directed locomotion? Developmental genetics shows that bilateral "
                       "symmetry is deeply wired - the same left-right patterning systems operate across "
                       "bilaterians - suggesting a single ancient origin. Yet some bilaterians secondarily "
                       "abandoned it: flatfish, with both eyes on one side, and snails with coiled "
                       "asymmetry, proving the program is flexible. The Ediacaran fossil record contains "
                       "both bilateral and stranger symmetries, and which came first in deep time is "
                       "still contested."),
        "why_it_matters": ("Body symmetry is the most basic fact of animal architecture; explaining its "
                           "dominance explains the shape of the living world. The question links "
                           "development, locomotion, and deep time - and its answer constrains what alien "
                           "or synthetic animal forms might look like."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads bilateral symmetry as a chassis for purposeful motion: the "
                     "Signature approach tests whether the chassis was built for the motion or the motion "
                     "for the chassis."),
        "sig_solution": (
            LABEL + " Approach S-27: chassis-direction test. "
            "Assumptions: (A1) bilateral symmetry, cephalization, and directed locomotion form a "
            "correlated suite; (A2) the Ediacaran fossil record can order their appearance; (A3) "
            "developmental patterning reveals whether the program is one invention or many. "
            "Reasoning path: (S1) order symmetry, head structures, and locomotion traces in Ediacaran "
            "and early Cambrian fossils; (S2) test whether directed burrowing traces precede bilateral "
            "body fossils, which would favor locomotion-first; (S3) compare left-right patterning genes "
            "across bilaterians for single versus multiple origins; (S4) model the fitness of bilateral "
            "versus radial bodies under directed-movement selection. "
            "Proposed mechanism: locomotion-first - directed movement through sediment selected for "
            "streamlined front-back bodies, and cephalization followed as senses concentrated at the "
            "leading end; the developmental program then locked in. "
            "What would confirm it: burrowing traces predating bilateral body fossils, and fitness "
            "models favoring bilateral bodies only under directed movement. What would kill it: "
            "bilateral developmental patterning predating any locomotion, implying the chassis came "
            "first. "
            "What it does NOT claim: the observed sequence, peer acceptance, or settled status. This is "
            "a proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: did directed locomotion select for bilateral bodies, or did bilateral development enable locomotion?",
            "Bilateral symmetry correlates with cephalization and paired limbs across the animal kingdom.",
            "Flatfish and snails prove the bilateral program can be secondarily abandoned.",
            "Ediacaran fossils preserve both bilateral and stranger symmetries.",
            "This walkthrough orders symmetry, heads, and locomotion traces in deep time.",
        ],
        "requirements": [
            "Fossil ordering needs trace fossils and body fossils on a common timeline.",
            "Gene comparisons must test single versus multiple origins.",
            "Fitness models must compare symmetries under identical selection.",
            "Secondary losses must be explained by the same theory.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_ERWIN, CIT_DUNN],
    },
    {
        "key": "animal-root",
        "name": "Which Animal Branched Off First",
        "group": "Advanced",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("The animal family tree has a contested root: sponges or comb jellies? Traditional "
                    "morphology puts sponges - simple, sessile filter-feeders - at the base. But several "
                    "large phylogenomic studies place ctenophores, the comb jellies with complex nerves "
                    "and muscles, as the sister group to all other animals. The two answers imply "
                    "radically different histories of nervous systems and muscles."),
        "background": ("For over a century, sponges were the unquestioned first branch: no nerves, no "
                       "muscles, no gut - the simplest possible animal. Then phylogenomics arrived. Dunn "
                       "and colleagues' 2008 broad sampling began the modern era, and Ryan and "
                       "colleagues' 2013 ctenophore genome analysis supported ctenophores-first, implying "
                       "that nerves and muscles either evolved twice or were lost in sponges. The debate "
                       "has seesawed with each new dataset and method: some analyses recover "
                       "sponges-first with better models of sequence evolution, others hold firm on "
                       "ctenophores-first. The stakes are enormous. If ctenophores branched first, the "
                       "last common ancestor of animals may have been more complex than sponges, and "
                       "nervous systems may have evolved independently in ctenophores and other animals - "
                       "or been lost in sponges and placozoans. The root of the animal tree determines "
                       "the starting point of all animal evolution, and it is still disputed."),
        "why_it_matters": ("The root sets the ancestral state for every trait animals have: nerves, "
                           "muscles, guts, symmetry. Getting it wrong means misreading the entire history "
                           "of animal complexity. It is also the flagship case of phylogenomics disagreeing "
                           "with morphology, testing the methods themselves."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the contested root as a forensic case: the Signature "
                     "approach weighs the genomic fingerprints - gene losses versus independent gains - to "
                     "find which history requires fewer miracles."),
        "sig_solution": (
            LABEL + " Approach S-28: miracle-counting forensics. "
            "Assumptions: (A1) the true tree minimizes implausible events - massive independent gains "
            "or massive losses; (A2) rare genomic changes like gene-order rearrangements are more "
            "reliable than sequence data alone; (A3) method artifacts like long-branch attraction can "
            "be diagnosed. "
            "Reasoning path: (S1) count the implied nervous-system gains versus losses under each "
            "rooting; (S2) test for long-branch attraction and compositional bias in ctenophore-first "
            "datasets; (S3) use rare genomic changes - intron positions, synteny, microRNAs - as "
            "independent arbiters; (S4) examine whether ctenophore nerves use the same molecular "
            "machinery as other animals, which would favor common origin. "
            "Proposed mechanism: sponges-first with method-artifact correction - the ctenophore-first "
            "signal is driven by the comb jellies' fast-evolving genomes attracting them to the "
            "outgroup, and rare genomic changes will ultimately confirm sponges at the base. "
            "What would confirm it: rare genomic changes unanimously supporting sponges-first, with "
            "the sequence signal collapsing under better evolutionary models. What would kill it: "
            "rare changes supporting ctenophores-first, forcing acceptance of convergent nerves or "
            "massive sponge losses. "
            "What it does NOT claim: the settled root, peer acceptance, or settled status. This is a "
            "proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: are sponges or comb jellies the sister group to all other animals?",
            "Sponges-first is the traditional view; ctenophores-first is the phylogenomic challenger.",
            "Dunn et al. (2008) opened the modern era; Ryan et al. (2013) sequenced the ctenophore genome.",
            "The rooting decides whether nerves evolved once, twice, or were lost in sponges.",
            "This walkthrough counts implied gains versus losses under each rooting.",
        ],
        "requirements": [
            "Rare genomic changes must arbitrate, not just sequence data.",
            "Long-branch attraction must be explicitly diagnosed.",
            "Ctenophore nerve molecular machinery must be compared, not assumed convergent.",
            "The verdict must survive multiple datasets and methods.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_DUNN, CIT_RYAN],
    },
    {
        "key": "extinction-selectivity",
        "name": "What Selects Survivors of Mass Extinctions",
        "group": "Advanced",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("The asteroid that ended the dinosaurs 66 million years ago killed all non-avian "
                    "dinosaurs but spared birds, mammals, crocodiles, and turtles. Why them? Body size, "
                    "diet, habitat, and geographic range have all been proposed as survival traits, but "
                    "no single selectivity rule explains who lives and who dies across the Big Five mass "
                    "extinctions - and the selectivity seems to differ each time."),
        "background": ("David Jablonski's work showed that mass extinctions select differently than "
                       "background extinctions: traits that protect species in normal times, like wide "
                       "geographic range, matter less during catastrophes. At the Cretaceous-Paleogene "
                       "boundary, the pattern is striking: no land animal over about 25 kilograms "
                       "survived, burrowers and freshwater feeders did well, and detritus-based food "
                       "webs outperformed photosynthesis-based ones in the impact winter. But the rule "
                       "shifts per event: the end-Permian favored different traits than the end-Triassic, "
                       "and some groups survive one catastrophe only to die in the next. The emerging view "
                       "is that selectivity depends on the kill mechanism - impact winter, anoxia, "
                       "acidification - interacting with ecology. Yet a general theory of extinction "
                       "selectivity, one that predicts survivors from traits plus kill mechanism, does "
                       "not exist. With the current biodiversity crisis underway, the question is no "
                       "longer academic."),
        "why_it_matters": ("We are living through a sixth mass extinction; knowing what selected survivors "
                           "in past events is the best guide to what will survive this one. The question "
                           "also tests whether macroevolution follows rules or is dominated by contingency. "
                           "Conservation triage depends on getting the selectivity right."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads each mass extinction as a filter with a different mesh: "
                     "the Signature approach characterizes each filter's mesh from its kill mechanism and "
                     "predicts which traits pass through."),
        "sig_solution": (
            LABEL + " Approach S-29: filter-mesh characterization. "
            "Assumptions: (A1) each extinction's selectivity follows from its kill mechanism; (A2) "
            "survivor traits can be scored from the fossil record; (A3) the kill mechanisms of the Big "
            "Five are known well enough to model. "
            "Reasoning path: (S1) score body size, diet, habitat, range, and physiology for victims and "
            "survivors at each Big Five boundary; (S2) model each kill mechanism - impact winter, ocean "
            "anoxia, acidification, volcanism - as a trait filter; (S3) test whether the filter models "
            "predict the observed survivors better than chance; (S4) apply the filters to modern taxa "
            "under current kill mechanisms. "
            "Proposed mechanism: kill-mechanism filters - impact winters select for small, burrowing, "
            "detritus-feeding generalists; anoxic events select for hypoxia tolerance; there is no "
            "universal survivor trait, only mechanism-matched traits. "
            "What would confirm it: filter models predicting survivors at multiple boundaries out of "
            "sample. What would kill it: survivor traits showing no relationship to kill mechanisms - "
            "pure lottery. "
            "What it does NOT claim: a universal survivor formula, peer acceptance, or settled status. "
            "This is a proposed path, honestly labeled, and the question stays open until a real "
            "resolution exists."),
        "key_points": [
            "Statement: what trait rules select survivors, and why do they differ per extinction?",
            "Jablonski showed mass extinctions select differently than background extinctions.",
            "At the K-Pg boundary, nothing over ~25 kg on land survived; burrowers and detritivores did well.",
            "Selectivity shifts with kill mechanism: impact winter, anoxia, acidification.",
            "This walkthrough models each kill mechanism as a trait filter.",
        ],
        "requirements": [
            "Survivor traits must be scored at every Big Five boundary, not just the K-Pg.",
            "Filter models must predict out of sample.",
            "Kill mechanisms must be independently constrained by geology.",
            "The pure-lottery null must be tested, not dismissed.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_JABLONSKI],
    },
    {
        "key": "bird-flight",
        "name": "How Birds Evolved Flight",
        "group": "Advanced",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("Birds are living dinosaurs, and their flight evolved from feathered, ground-running "
                    "predators. But how? The trees-down hypothesis says gliding from heights came first; "
                    "the ground-up hypothesis says running and flapping came first. Ken Dial's "
                    "wing-assisted incline running showed a third path: half-wings help chicks run up "
                    "steep slopes. The fossils are spectacular, yet the sequence of the first "
                    "powered flight remains disputed."),
        "background": ("The discovery of feathered dinosaurs in China's Jehol biota proved that feathers "
                       "evolved before flight - for insulation and display - removing the oldest "
                       "objection to the dinosaur-bird link. Archaeopteryx, with its asymmetric flight "
                       "feathers, could at least glide, and possibly fly weakly. Ken Dial's work on "
                       "chukar chicks showed that even immature wings generate aerodynamic force used to "
                       "run up inclines, providing a functional halfway stage: wings as climbing aids "
                       "before wings as flight organs. Four-winged fossils like Microraptor showed "
                       "gliding stages with leg feathers. Yet the launch sequence is unresolved: did "
                       "powered flight evolve from the trees down, from the ground up, or via incline "
                       "running? Each has fossil and biomechanical support, and the earliest true "
                       "flapping flight is not preserved in the act. The evolution of the flight stroke "
                       "itself - the unique avian supracoracoideus pulley system - adds a second "
                       "unsolved transformation."),
        "why_it_matters": ("Bird flight is the most refined locomotion in nature and the direct ancestor "
                           "of every bird alive; its origin is the dinosaur-to-bird story's climax. "
                           "Understanding the sequence illuminates how complex locomotor systems assemble. "
                           "The biomechanics feed directly into flapping-wing drone design."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the bird wing as a climber's tool promoted to a flyer's: "
                     "the Signature approach tests each proposed promotion - gliding, running, climbing - "
                     "for whether it pays its aerodynamic way."),
        "sig_solution": (
            LABEL + " Approach S-30: promotion-path pricing. "
            "Assumptions: (A1) feathers predate flight and were co-opted; (A2) each intermediate - "
            "glider, runner-flapper, incline-runner - had to be aerodynamically profitable; (A3) the "
            "Jehol fossils sample the transitional morphologies. "
            "Reasoning path: (S1) model the aerodynamics of feathered dinosaurs at each fossil stage to "
            "find which behaviors each morphology could perform; (S2) test Dial's incline-running "
            "hypothesis across more species and inclines; (S3) sequence the morphologies from "
            "four-winged gliders through Archaeopteryx to modern birds; (S4) reconstruct the flight "
            "stroke's musculoskeletal evolution. "
            "Proposed mechanism: incline-running bridge - feathered dinosaurs used protowings to run up "
            "steep surfaces, the aerodynamic force grew with feather size, and the transition to "
            "powered flight passed through this profitable halfway house. "
            "What would confirm it: aerodynamic models showing each fossil stage profitable at its "
            "proposed behavior, with incline running as the continuous bridge. What would kill it: "
            "fossil stages whose aerodynamics fit only gliding, with no profitable running "
            "intermediate. "
            "What it does NOT claim: the observed launch, peer acceptance, or settled status. This is a "
            "proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: trees-down, ground-up, or incline-running - which path led to powered avian flight?",
            "Feathered dinosaurs proved feathers predate flight.",
            "Dial (2003) showed half-wings aid incline running - a functional halfway stage.",
            "Microraptor's four wings document a gliding stage.",
            "The flight stroke's pulley system is a second unsolved transformation.",
            "This walkthrough prices each intermediate aerodynamically.",
        ],
        "requirements": [
            "Aerodynamic models must use real fossil morphologies.",
            "Incline-running tests need multiple species and inclines.",
            "The sequence must be continuous - no unprofitable gaps.",
            "The stroke mechanism's evolution must be reconstructed too.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_DIAL],
    },
    {
        "key": "negligible-senescence",
        "name": "Why Some Species Live for Centuries",
        "group": "Advanced",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("A Greenland shark can live 400 years. Ocean quahog clams reach 500. Some turtles "
                    "show no measurable aging at all. Yet a mouse, with the same basic mammalian "
                    "machinery, is old at two. What do the centuries-long species have - or lack - that "
                    "lets them nearly escape senescence, and why did most animals not follow them?"),
        "background": ("Caleb Finch's syntheses documented the extraordinary range of animal lifespans, "
                       "from days to centuries, and the phenomenon of negligible senescence: species "
                       "whose mortality and fertility do not worsen with age. The Greenland shark's "
                       "400-year lifespan, established by radiocarbon dating of eye lenses, made it the "
                       "longest-lived vertebrate known. Candidate mechanisms for extreme longevity "
                       "include superior DNA repair, as seen in bowhead whales; efficient proteostasis; "
                       "slow metabolisms in cold environments; and negligible telomere shortening. But "
                       "correlation is not mechanism, and the evolutionary question is sharper than the "
                       "molecular one: if negligible senescence is possible, why is it rare? The "
                       "disposable-soma answer is that these species pay with glacial reproduction - "
                       "Greenland sharks do not mature until around 150 - but testing that bargain "
                       "across the longevity spectrum is incomplete. The genetics of extreme longevity "
                       "remain largely unmapped."),
        "why_it_matters": ("Extreme-longevity species are nature's successful experiments in beating "
                           "aging; their mechanisms are the most promising leads in geroscience. "
                           "Understanding the evolutionary bargain - what centuries of life cost - "
                           "constrains every anti-aging intervention. It is also a profound question "
                           "about life's possibilities."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads centuries-long life as a purchased luxury: the Signature "
                     "approach finds the price tag by comparing what the long-lived gave up against what "
                     "the short-lived spend."),
        "sig_solution": (
            LABEL + " Approach S-31: luxury price-tag audit. "
            "Assumptions: (A1) negligible senescence is purchased with slow life histories; (A2) the "
            "molecular mechanisms - repair, proteostasis, telomere maintenance - are identifiable by "
            "comparison; (A3) the bargain is quantitative: lifespan trades against reproductive rate. "
            "Reasoning path: (S1) compare DNA repair capacity, proteostasis, and telomere dynamics "
            "across the lifespan spectrum; (S2) test whether age at maturity and reproductive rate "
            "predict lifespan as the bargain requires; (S3) sequence extreme-longevity genomes for "
            "positive selection on repair pathways; (S4) check whether cold environments explain the "
            "pattern or merely correlate. "
            "Proposed mechanism: slow-life purchase - extreme longevity evolves where extrinsic "
            "mortality is low enough that selection favors maintenance over reproduction, paid for "
            "with delayed maturity and slow breeding; the molecular currency is upgraded repair. "
            "What would confirm it: repair investment and reproductive slowness jointly predicting "
            "lifespan across taxa. What would kill it: fast-reproducing species with negligible "
            "senescence, breaking the bargain. "
            "What it does NOT claim: a longevity therapy, peer acceptance, or settled status. This is "
            "a proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: what mechanisms and evolutionary bargains produce negligible senescence?",
            "Greenland sharks live ~400 years; ocean quahogs reach ~500; some turtles do not measurably age.",
            "Finch documented the lifespan spectrum and the negligible-senescence phenomenon.",
            "Candidates: superior DNA repair, proteostasis, slow cold-water metabolisms.",
            "The bargain hypothesis: centuries of life are purchased with glacial reproduction.",
            "This walkthrough audits the price tag across the lifespan spectrum.",
        ],
        "requirements": [
            "Mechanisms must be compared across the full lifespan spectrum.",
            "The reproduction-longevity bargain needs quantitative testing.",
            "Extreme-longevity genomes must be sequenced and analyzed.",
            "Cold-environment correlation must be separated from causation.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_FINCH, CIT_KIRKWOOD],
    },
    {
        "key": "predictable-evolution",
        "name": "Can We Predict Animal Evolution",
        "group": "Advanced",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("Stephen Jay Gould argued that replaying life's tape would give a different world - "
                    "evolution is dominated by contingency. Simon Conway Morris countered that "
                    "convergence is everywhere: eyes, wings, and intelligence evolved repeatedly, so "
                    "evolution finds the same solutions. Can we actually predict how animals will evolve - "
                    "under climate change, in the lab, on islands - or is the future of life "
                    "fundamentally unpredictable?"),
        "background": ("The predictability debate is evolution's deepest philosophical divide. Gould's "
                       "Wonderful Life (1989) used the Burgess Shale to argue that survival was a "
                       "lottery and replaying the tape would erase humans. Conway Morris replied that "
                       "convergence - the independent evolution of camera eyes in octopuses and "
                       "vertebrates, of echolocation in bats and whales, of eusociality in insects and "
                       "shrimp - shows that selection finds the same peaks repeatedly. Jonathan Losos's "
                       "work on Anolis lizards showed predictable ecomorph evolution on different "
                       "islands, while Zachary Blount's E. coli experiments showed a key innovation "
                       "depending on rare potentiating mutations - contingency at the molecular level. "
                       "The modern synthesis emerging is scale-dependent: short-term, constrained "
                       "predictions work; deep-time replays do not. But no quantitative theory of "
                       "evolutionary predictability exists, and the question matters urgently as "
                       "humans try to forecast evolution under climate change, antibiotic resistance, "
                       "and pest management."),
        "why_it_matters": ("Predicting evolution would transform medicine (resistance forecasting), "
                           "agriculture (pest evolution), and conservation (evolutionary rescue). "
                           "Philosophically, it decides whether life's history is law-like or "
                           "lottery-like. It is the question Gould and Conway Morris made famous, still "
                           "unsettled."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads evolution as a landscape of peaks and lotteries: the "
                     "Signature approach maps which features of the landscape are predictable and which "
                     "draws are chance, to find the horizon of forecasting."),
        "sig_solution": (
            LABEL + " Approach S-32: forecast-horizon mapping. "
            "Assumptions: (A1) predictability is scale-dependent: traits under strong selection in "
            "constrained spaces are predictable, deep novelties are not; (A2) convergence frequency "
            "measures the landscape's peak structure; (A3) experimental evolution tests short-horizon "
            "prediction. "
            "Reasoning path: (S1) quantify convergence rates across traits to map the landscape's "
            "repeatability; (S2) run replicate experimental-evolution lines and measure divergence - "
            "the Blount test of contingency; (S3) test island-replicate predictions like Losos's "
            "Anolis work in new systems; (S4) build predictive models for short-horizon cases - "
            "pesticide resistance, thermal adaptation - and score their accuracy. "
            "Proposed mechanism: constrained predictability - evolution is predictable within "
            "adaptive zones and over short timescales, where selection dominates, and contingent "
            "across zones and deep time, where rare innovations and lotteries dominate. "
            "What would confirm it: short-horizon models beating chance consistently while deep "
            "replays diverge. What would kill it: either perfect long-term predictability or total "
            "short-term unpredictability. "
            "What it does NOT claim: a law of evolution, peer acceptance, or settled status. This is "
            "a proposed path, honestly labeled, and the question stays open until a real resolution "
            "exists."),
        "key_points": [
            "Statement: is animal evolution predictable, contingent, or scale-dependent?",
            "Gould argued contingency rules; Conway Morris argued convergence rules.",
            "Losos showed predictable lizard ecomorphs on replicate islands.",
            "Blount's E. coli work showed key innovations depending on rare chance mutations.",
            "This walkthrough maps the forecast horizon from experiments and convergence data.",
        ],
        "requirements": [
            "Predictions must be scored against chance, not just narrated.",
            "Convergence rates need systematic quantification.",
            "Experimental replicates must test contingency directly.",
            "Short-horizon and deep-time claims must be kept separate.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_LOSOS, CIT_BLOUNT],
    },
    {
        "key": "consciousness-evolution",
        "name": "How Consciousness Evolved",
        "group": "Advanced",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("If some animals are conscious, consciousness evolved - but from what, and when? Did "
                    "subjective experience appear with the first nervous systems, with the first brains, "
                    "with warm-blooded sociality, or only once? The evolution of consciousness is the "
                    "hard problem of consciousness crossed with the fossil record, and neither side has "
                    "yielded."),
        "background": ("The question sits at the intersection of neuroscience, philosophy, and "
                       "paleontology, which is why it is so hard. One camp traces consciousness to the "
                       "Cambrian, when the first active predators needed integrated sensory worlds to "
                       "hunt - the ecological argument that experience evolved for action. Another camp "
                       "places it much later, with the complex social cognition of mammals and birds, or "
                       "even later still. The ctenophore-first versus sponges-first debate matters here: "
                       "if nerves evolved twice, consciousness-relevant circuitry may have too. "
                       "Comparative work keeps pushing candidate markers deeper: insects show attention-"
                       "like processes and affective states, which would put the roots of experience near "
                       "the base of bilaterians if the markers are valid. But without a theory of what "
                       "consciousness is physically, dating its origin is guesswork layered on "
                       "mystery - the most compounded problem in this database."),
        "why_it_matters": ("The origin of consciousness is the origin of inner life - arguably the "
                           "deepest question in science. Its answer would constrain theories of "
                           "consciousness, set the moral scope of the animal kingdom across deep time, "
                           "and inform the debate over machine consciousness."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads consciousness as a trait with an origin date: the "
                     "Signature approach triangulates the date from markers, fossils, and ecology, "
                     "treating each line of evidence as a witness to be cross-examined."),
        "sig_solution": (
            LABEL + " Approach S-33: three-witness triangulation. "
            "Assumptions: (A1) consciousness has a real evolutionary origin, not a gradual "
            "meaningless fade; (A2) the marker fingerprint from S-13 can be projected onto extinct "
            "taxa via neural and behavioral proxies; (A3) ecology - predation, sociality - provides "
            "the selection pressure. "
            "Reasoning path: (S1) apply the convergent marker fingerprint to living taxa to date the "
            "deepest node showing the full set; (S2) examine Cambrian fossils for the neural and "
            "sensory complexity the markers require; (S3) test the ecological trigger: does the "
            "marker depth correlate with predatory versus sessile lifestyles; (S4) check the "
            "ctenophore question - if nerves evolved twice, test both origins for marker depth. "
            "Proposed mechanism: Cambrian action-awakening - subjective experience emerged with active "
            "predation, when integrated sensory-motor control first paid for an inner world; social "
            "complexity later deepened it in mammals, birds, and cephalopods. "
            "What would confirm it: marker depth tracking predatory lifestyle across independent "
            "origins, with Cambrian fossils showing the required neural complexity. What would kill "
            "it: full marker sets in sessile filter-feeders with no action demands, or no correlation "
            "with ecology at all. "
            "What it does NOT claim: a solution to the hard problem, a date, peer acceptance, or "
            "settled status. This is a proposed path, honestly labeled, and the question stays open "
            "until a real resolution exists."),
        "key_points": [
            "Statement: when and from what did subjective experience first evolve?",
            "The Cambrian-predation hypothesis ties experience to the needs of active hunting.",
            "Insect affective states would push the roots near the bilaterian base - if markers are valid.",
            "The ctenophore root debate could mean consciousness-relevant circuitry evolved twice.",
            "This walkthrough triangulates markers, fossils, and ecology to date the origin.",
        ],
        "requirements": [
            "Marker validity must be established before projecting into deep time.",
            "Fossil neural complexity must be assessed, not assumed.",
            "Ecological correlations need independent origins as replicates.",
            "The hard problem must be acknowledged as unsolved throughout.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_GRIFFIN, CIT_CAMBRIDGE, CIT_ERWIN],
    },
    {
        "key": "last-common-ancestor",
        "name": "What the Last Common Ancestor of Animals Looked Like",
        "group": "Advanced",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("Every animal alive - sponge, insect, human - descends from one ancestral species, "
                    "the urmetazoan, that lived over 600 million years ago. What did it look like? Was "
                    "it a simple filter-feeding blob like a sponge, a tiny swimming larva-like creature, "
                    "or something stranger? Reconstructing the ancestor of all animals is the most "
                    "compounded reconstruction problem in zoology, depending on the contested tree root, "
                    "the fossil record's silence, and the interpretation of every living phylum."),
        "background": ("The urmetazoan problem compounds every hard question in this database. Its "
                       "answer depends on the sponges-first versus ctenophores-first root: a sponge-like "
                       "ancestor implies nerves and muscles evolved later, while a ctenophore-like "
                       "ancestor implies they were ancestral and lost in sponges. It depends on the "
                       "origin of multicellularity, the Cambrian explosion's triggers, and the "
                       "bilaterian radiation. Competing reconstructions paint different portraits: the "
                       "placula hypothesis sees a flat filter-feeding sheet; the planula hypothesis sees "
                       "a swimming ciliated larva; genomic comparisons suggest a surprisingly complex "
                       "ancestor with a rich developmental toolkit. Ediacaran fossils offer candidates "
                       "but no consensus. The reconstruction must integrate phylogenomics, developmental "
                       "genetics, and paleontology - three fields that often disagree - making this the "
                       "fitting summit of the ladder."),
        "why_it_matters": ("The urmetazoan is the starting point of all animal history; every "
                           "evolutionary story in zoology begins where this reconstruction ends. Getting "
                           "it right anchors the Cambrian explosion, the root debate, and the origin of "
                           "complexity itself. It is the single most integrative question in animal "
                           "biology."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the urmetazoan as a portrait painted by three artists - "
                     "genes, embryos, and fossils - who disagree: the Signature approach finds where "
                     "their brushstrokes overlap and treats only the overlap as portrait."),
        "sig_solution": (
            LABEL + " Approach S-34: three-artist overlap portrait. "
            "Assumptions: (A1) the ancestor is reconstructible by ancestral-state methods applied to "
            "genomes, development, and morphology jointly; (A2) the tree root must be settled first, "
            "with both rootings carried as alternatives; (A3) only traits supported by at least two "
            "independent lines count as portrait. "
            "Reasoning path: (S1) reconstruct the ancestral developmental toolkit from comparative "
            "genomics across all phyla; (S2) reconstruct ancestral cell types from single-cell atlases "
            "of sponges, ctenophores, cnidarians, and bilaterians; (S3) test Ediacaran fossil candidates "
            "against the genomic portrait; (S4) build both rootings' portraits and identify the "
            "overlap - the robust core. "
            "Proposed mechanism: toolkit-rich simpleton - the genomic portrait shows a surprisingly "
            "complex developmental toolkit in a morphologically simple body: a small, likely "
            "filter-feeding or grazing organism with differentiated cell types and the regulatory "
            "potential that the Cambrian later unleashed. "
            "What would confirm it: genomic, cell-type, and fossil lines converging on the same "
            "portrait under both rootings. What would kill it: the lines diverging irreconcilably, "
            "proving the ancestor is beyond reconstruction. "
            "What it does NOT claim: the portrait completed, the root settled, peer acceptance, or "
            "settled status. This is a proposed path, honestly labeled, and the question stays open "
            "until a real resolution exists."),
        "key_points": [
            "Statement: what did the single ancestral species of all animals look like?",
            "The portrait depends on the sponges-first versus ctenophores-first root.",
            "Genomics suggests a rich developmental toolkit in a simple body.",
            "Competing hypotheses: placula (flat sheet) versus planula (swimming larva).",
            "Ediacaran fossils offer candidates but no consensus.",
            "This walkthrough builds the portrait from genomes, cell types, and fossils jointly.",
        ],
        "requirements": [
            "All three lines - genomic, developmental, fossil - must be integrated.",
            "Both rootings must be carried as alternatives until settled.",
            "Only traits with two independent lines of support count.",
            "Irreconcilable divergence must be reported as failure, not fudged.",
        ],
        "standards": [
            "Standard: a claimed resolution must survive refereed publication and independent replication.",
        ],
        "citations": [CIT_KING, CIT_DUNN, CIT_RYAN, CIT_ERWIN],
    },
]

assert len(ENTRIES) == 34, "expected 34 entries"
assert [e["ladder_rank"] for e in ENTRIES] == list(range(1, 35)), "ladder ranks must be 1..34"
