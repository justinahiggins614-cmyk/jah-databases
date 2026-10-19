#!/usr/bin/env python3
"""Entries for the Unsolved Anthropology databases (batch 4).

34 famous open problems in anthropology, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex). Public half carries
the real fact-checked problem record plus a short pointer to the Signature
approach; Signature half carries the full Signature-generated proposed
solution, always labeled and never presented as established science.

ID prefixes: JAH-USAN- (public) and JAH-USANS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="anthropology-01",
        name="Why Bipedalism Came First",
        group="Human Origins",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Why did hominins begin walking upright millions of years before brains "
                 "enlarged, tools appeared, or any obvious payoff existed?"),
        background=("Fossil hominins such as Sahelanthropus (about 7 million years ago) and "
                    "Ardipithecus show upright walking long before the genus Homo, stone tools, "
                    "or large brains. Dozens of explanations have been proposed - carrying food, "
                    "seeing over grass, cooling the body, freeing the hands, wading - yet no "
                    "single account explains why a costly, injury-prone gait won out so early, "
                    "while our ape relatives stayed knuckle-walking."),
        why_it_matters=("Bipedalism is the first great hominin innovation: it reshaped the "
                        "skeleton, freed the hands, and set the stage for everything after. "
                        "Understanding its cause tells us whether human evolution was driven by "
                        "environment, by social life, or by feedback loops we have not modeled."),
        sig_lens=("The Signature lens reads bipedalism as a ledger problem: a costly trait must "
                  "have paid its way every single generation, so the Signature approach hunts for "
                  "a benefit that compounds daily rather than a one-time payoff."),
        sig_body=("The Signature proposal treats upright walking as an energy-arbitrage trait. "
                  "Assumptions: (1) early hominins foraged across patchy woodland-savanna mosaics "
                  "where daily travel distances were large; (2) even a small per-step energy saving "
                  "compounds into a decisive reproductive edge over thousands of generations; "
                  "(3) infant-carrying and food transport amplified the payoff of freed hands. "
                  "Reasoning path: instead of asking what dramatic event selected for bipedalism, "
                  "the proposal models cumulative small savings - measured in kilocalories per "
                  "kilometer - and finds that modest efficiency gains dominate dramatic single "
                  "causes in long-horizon selection. Limits: the model does not identify which "
                  "ecological pressure came first, and fossil gait energetics remain estimated, "
                  "not measured."),
        pointer=('The Signature system approaches this as an energy-ledger problem, modeling how small per-step savings compound across generations instead of hunting a single dramatic cause. The Signature test: fossil energetics models show sustained per-kilometer savings for early bipeds in mosaic habitats. It would be refuted if bipedal anatomy appears in dense forest contexts with no long-distance foraging pressure.'),
        key_points=[
            "Upright walking predates stone tools and brain enlargement by millions of years.",
            "Over a dozen competing explanations exist; none commands consensus.",
            "Bipedalism is energetically costly and injury-prone, so its payoff must have been steady.",
            "Fossil evidence shows a mosaic transition, not a sudden switch.",
        ],
        requirements=[
            "A causal account that works before tools, fire, or large brains existed.",
            "Energetic measurements consistent with fossil anatomy.",
            "An explanation for why apes in similar habitats did not follow.",
        ],
        standards=[
            "Claims checked against the fossil record as synthesized in current paleoanthropology literature.",
            "Open status confirmed as of 2026: no consensus explanation published.",
        ],
        citations=[
            "Darwin C. The Descent of Man. London; 1871.",
            "Harcourt-Smith WEH. The origins of bipedal locomotion. Handbook of Paleoanthropology; 2015.",
        ],
        hypotheses=[
            "Energetic efficiency over long daily foraging distances selected for upright walking.",
            "Freeing the hands for carrying food and infants was the decisive advantage.",
            "Thermoregulation - less sun exposure upright - drove the shift in open habitats.",
            "Wading in shallow water shaped the upright posture first.",
        ],
        confirm="Fossil energetics models show sustained per-kilometer savings for early bipeds in mosaic habitats.",
        refute="Bipedal anatomy appears in dense forest contexts with no long-distance foraging pressure.",
    ),
    dict(
        key="anthropology-02",
        name="The Tripling of the Hominin Brain",
        group="Human Origins",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Why did hominin brain volume roughly triple - from about 450 cc to about "
                 "1350 cc - in under three million years, and what selected for such an "
                 "expensive organ?"),
        background=("Brain tissue is metabolically ruinous: the modern human brain is about 2 "
                    "percent of body mass yet consumes roughly 20 percent of resting energy. The "
                    "expansion was not steady - it accelerated with Homo erectus and again with "
                    "archaic Homo sapiens. Proposed drivers include social complexity (the "
                    "Machiavellian intelligence hypothesis), tool manufacture, cooking and diet, "
                    "language, and runaway sexual selection. Each explains part of the curve; "
                    "none explains all of it."),
        why_it_matters=("The brain is the organ that made everything else possible - language, "
                        "culture, science. If we cannot say what paid for it, we cannot say what "
                        "human intelligence is for, which matters for everything from education "
                        "to artificial intelligence."),
        sig_lens=("The Signature lens treats the brain as a ledger entry that must balance: an "
                  "organ this costly needs a revenue stream, so the Signature approach looks for "
                  "compounding social returns rather than single dramatic causes."),
        sig_body=("The Signature proposal models brain expansion as a social-compounding process. "
                  "Assumptions: (1) in social primates, reproductive success tracks alliance "
                  "quality; (2) alliance quality scales with the ability to model other minds; "
                  "(3) mind-modeling ability scales with neural investment, creating a feedback "
                  "loop. Reasoning path: each increment of social cognition raises the value of "
                  "the next increment, because smarter rivals demand smarter strategists - a "
                  "runaway process that stops only when metabolic costs cap it. The tripling is "
                  "then the visible trace of an arms race, not a response to the physical "
                  "environment. Limits: the model predicts brain size from group size, but the "
                  "correlation is noisy; diet and cooking may have funded rather than caused "
                  "the expansion."),
        pointer=('The Signature system models brain growth as a runaway social feedback loop, with metabolic cost as the brake, rather than a response to any single environment. The Signature test: brain size tracks independent measures of social complexity across hominin species. It would be refuted if large-brained hominins appear in small-group contexts with simple technology.'),
        key_points=[
            "Hominin brains tripled in under three million years - extraordinarily fast.",
            "Brain tissue costs about 20 percent of resting metabolism.",
            "Expansion accelerated twice, not smoothly.",
            "No single proposed driver explains the full curve.",
        ],
        requirements=[
            "An account of what paid the metabolic bill, generation after generation.",
            "Consistency with the two acceleration phases in the fossil record.",
            "A reason the expansion stopped where it did.",
        ],
        standards=[
            "Energetic figures cross-checked against human physiology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Dunbar RIM. The social brain hypothesis. Evolutionary Anthropology; 1998.",
            "Aiello LC, Wheeler P. The expensive-tissue hypothesis. Current Anthropology; 1995.",
        ],
        hypotheses=[
            "Social complexity and mind-modeling drove a runaway expansion capped by metabolism.",
            "Cooking unlocked calories that funded a brain already under selection.",
            "Tool manufacture and technical cognition were the primary selectors.",
            "Sexual selection for displayed intelligence amplified the trend.",
        ],
        confirm="Brain size tracks independent measures of social complexity across hominin species.",
        refute="Large-brained hominins appear in small-group contexts with simple technology.",
    ),
    dict(
        key="anthropology-03",
        name="The Fate of the Neanderthals",
        group="Human Origins",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("Why did Neanderthals - large-brained, tool-using, fire-controlling humans who "
                 "survived Ice Age Europe for 300,000 years - disappear around 40,000 years ago?"),
        background=("Neanderthals buried their dead, made art, controlled fire, and carried the "
                    "FOXP2 gene variant linked to language. Modern non-Africans carry 1 to 2 "
                    "percent Neanderthal DNA, proving interbreeding. Yet as anatomically modern "
                    "humans spread into Europe, Neanderthal populations shrank and vanished. "
                    "Competing accounts blame climate, competition, disease, demographic bad luck, "
                    "violence, or absorption - and the record cannot yet choose."),
        why_it_matters=("Neanderthals are the mirror in which humanity sees its own fragility: a "
                        "successful, intelligent human lineage that simply ended. The answer "
                        "rewrites what survival means for our own species."),
        sig_lens=("The Signature lens reads the disappearance as a ledger of small disadvantages "
                  "compounding: no single catastrophe is needed if every generation tilts "
                  "slightly against you."),
        sig_body=("The Signature proposal treats Neanderthal extinction as demographic erosion, "
                  "not defeat. Assumptions: (1) Neanderthal groups were small and fragmented; "
                  "(2) modern human groups were larger and better networked; (3) interbreeding "
                  "was ongoing. Reasoning path: in a metapopulation of small bands, even a tiny "
                  "per-generation disadvantage - slightly higher infant mortality, slightly "
                  "smaller networks - compounds into absorption within a few thousand years, "
                  "exactly matching the genetic signal of admixture without replacement. No "
                  "war, no plague, no single cause is required; arithmetic does the work. "
                  "Limits: the model needs real demographic parameters the record cannot yet "
                  "supply, and regional variation remains unexplained."),
        pointer=('The Signature system models the disappearance as compounding demographic arithmetic across small bands, needing no single catastrophe. The Signature test: demographic models with realistic band sizes reproduce the admixture-plus-disappearance pattern. It would be refuted if neanderthal populations were large, dense, and well-networked until a sharp collapse.'),
        key_points=[
            "Neanderthals survived Ice Age Europe for roughly 300,000 years.",
            "Modern non-Africans carry 1 to 2 percent Neanderthal DNA.",
            "Disappearance took thousands of years, not a sudden event.",
            "Climate, competition, disease, and chance all remain live hypotheses.",
        ],
        requirements=[
            "An account consistent with the slow timeline and the admixture signal.",
            "Explanation of regional variation in disappearance dates.",
            "Demographic parameters grounded in archaeology, not assumed.",
        ],
        standards=[
            "Genetic figures cross-checked against ancient-DNA literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Higham T et al. The timing and spatiotemporal patterning of Neanderthal disappearance. Nature; 2014.",
            "Green RE et al. A draft sequence of the Neandertal genome. Science; 2010.",
        ],
        hypotheses=[
            "Small fragmented bands were demographically absorbed by larger modern human networks.",
            "Climate instability hit cold-adapted specialists harder than generalists.",
            "Novel pathogens carried by incoming modern humans devastated Neanderthal groups.",
            "Direct competition for prey and territory drove a slow exclusion.",
        ],
        confirm="Demographic models with realistic band sizes reproduce the admixture-plus-disappearance pattern.",
        refute="Neanderthal populations were large, dense, and well-networked until a sharp collapse.",
    ),
    dict(
        key="anthropology-04",
        name="Who Were the Denisovans",
        group="Human Origins",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Who were the Denisovans - a sister group to Neanderthals known mostly from DNA "
                 "and a handful of fragments - and how far did they range?"),
        background=("In 2010, DNA from a finger bone in Denisova Cave, Siberia, revealed a "
                    "previously unknown archaic human population. Since then, Denisovan DNA has "
                    "been found in modern Oceanians (4 to 6 percent), East Asians, and even a "
                    "Tibetan high-altitude adaptation gene (EPAS1). Yet the fossil record is a "
                    "jawbone, a few teeth, and fragments - no skull, no skeleton, no clear "
                    "portrait of what they looked like or how they lived."),
        why_it_matters=("Denisovans prove that human evolution was a braided stream, not a ladder. "
                        "Their genes still shape living people - including adaptation to the "
                        "highest plateau on Earth - yet we cannot say what they looked like."),
        sig_lens=("The Signature lens treats the Denisovans as a range problem: genes found in "
                  "Oceania but fossils found in Siberia demand a population map, and the "
                  "Signature approach draws it from the DNA alone."),
        sig_body=("The Signature proposal reconstructs Denisovans as a widespread eastern "
                  "metapopulation, not a single cave population. Assumptions: (1) the distinct "
                  "Denisovan ancestries in Oceanians, East Asians, and the Tibetan EPAS1 signal "
                  "represent at least three diverged groups; (2) divergence scales with "
                  "geographic separation; (3) archaic ranges followed Pleistocene climate belts. "
                  "Reasoning path: treating each ancestry pulse as a separate range estimate "
                  "places Denisovan-related groups from Siberia to Southeast Asia across hundreds "
                  "of thousands of years - a successful, diverse radiation, not a relic. Limits: "
                  "without fossils, morphology and culture remain pure inference."),
        pointer=('The Signature system maps Denisovan ranges from DNA pulses alone, treating them as a widespread radiation rather than a single cave population. The Signature test: new fossils across Asia sort into the three genetically predicted groups. It would be refuted if all Denisovan DNA traces to one small, late Siberian population.'),
        key_points=[
            "Denisovans are known chiefly from DNA, not fossils.",
            "Oceanians carry 4 to 6 percent Denisovan ancestry.",
            "The Tibetan high-altitude gene EPAS1 came from Denisovans.",
            "At least three distinct Denisovan ancestries are detected genetically.",
        ],
        requirements=[
            "A population model reconciling Siberian fossils with Oceanian DNA.",
            "An account of at least three diverged Denisovan groups.",
            "Consistency with Pleistocene climate geography.",
        ],
        standards=[
            "Genetic figures cross-checked against ancient-DNA literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Reich D et al. Genetic history of an archaic hominin group from Denisova Cave. Nature; 2010.",
            "Huerta-Sanchez E et al. Altitude adaptation in Tibetans caused by introgression of Denisovan-like DNA. Nature; 2014.",
        ],
        hypotheses=[
            "Denisovans were a widespread eastern metapopulation of several diverged groups.",
            "They were primarily a Siberian population with rare long-range admixture.",
            "Multiple distinct archaic groups are being lumped under one name.",
            "Their range tracked interglacial forest belts across Asia.",
        ],
        confirm="New fossils across Asia sort into the three genetically predicted groups.",
        refute="All Denisovan DNA traces to one small, late Siberian population.",
    ),
    dict(
        key="anthropology-05",
        name="The Hobbit of Flores",
        group="Human Origins",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("What was Homo floresiensis - the meter-tall hominin found on Flores Island, "
                 "Indonesia - and how did a tiny-brained toolmaker exist 50,000 years ago?"),
        background=("Discovered in 2003, Homo floresiensis stood about one meter tall with a "
                    "brain the size of a chimpanzee, yet made stone tools and hunted dwarf "
                    "elephants (Stegodon). Dated to as recently as 50,000 years ago, it lived "
                    "alongside modern humans. Debate rages: a dwarfed descendant of Homo erectus "
                    "via island dwarfism, a remnant of an earlier migration, or a pathological "
                    "modern human - though the pathology view has largely faded."),
        why_it_matters=("The Hobbit breaks the rule that small brains mean simple behavior, and "
                        "breaks the rule that only our lineage survived late. It forces a rewrite "
                        "of what a human can be."),
        sig_lens=("The Signature lens reads island dwarfism as a ledger forced to balance: "
                  "shrink the body or starve, and the Signature approach asks what the island "
                  "budget allowed."),
        sig_body=("The Signature proposal models floresiensis as an energy-budget solution to "
                  "island life. Assumptions: (1) Flores offered limited, fluctuating calories; "
                  "(2) brain tissue is the most expensive tissue to maintain; (3) tool-assisted "
                  "hunting preserved calorie intake while body size fell. Reasoning path: under a "
                  "hard island calorie cap, selection favors shrinking the most expensive organ "
                  "first - but tool use decouples brain size from foraging success, letting a "
                  "small-brained hominin remain a competent hunter. The Hobbit is then not a "
                  "degenerate form but an optimized one. Limits: the ancestral species and the "
                  "dwarfing rate remain contested; the model needs island calorie histories we "
                  "do not have."),
        pointer=('The Signature system models the Hobbit as an island energy-budget optimum, where tool use decoupled small brains from hunting success. The Signature test: older Flores fossils show a graded size reduction from a known ancestor. It would be refuted if the remains prove to be a small-bodied modern human population after all.'),
        key_points=[
            "About one meter tall, with a chimpanzee-sized brain, making stone tools.",
            "Survived until roughly 50,000 years ago alongside modern humans.",
            "Island dwarfism is the leading explanation; pathology views have faded.",
            "Ancestry - from Homo erectus or an earlier migrant - is unresolved.",
        ],
        requirements=[
            "A dwarfing mechanism consistent with island biogeography.",
            "An account of sophisticated behavior with a tiny brain.",
            "Fossil or genetic evidence of the ancestral population.",
        ],
        standards=[
            "Claims checked against the primary Flores literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Brown P et al. A new small-bodied hominin from the Late Pleistocene of Flores. Nature; 2004.",
            "Sutikna T et al. Revised stratigraphy and chronology for Homo floresiensis. Nature; 2016.",
        ],
        hypotheses=[
            "Island dwarfism shrank a Homo erectus descendant under a hard calorie cap.",
            "It descends from a pre-erectus migration, dwarfed over a million years.",
            "Small brains remained capable because tool use decoupled cognition from foraging.",
            "It represents a distinct, previously unknown hominin radiation in Southeast Asia.",
        ],
        confirm="Older Flores fossils show a graded size reduction from a known ancestor.",
        refute="The remains prove to be a small-bodied modern human population after all.",
    ),
    dict(
        key="anthropology-06",
        name="The Cooking Hypothesis",
        group="Human Origins",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Did the control of fire and cooking drive human evolution - shrinking our guts, "
                 "growing our brains, and reshaping our social lives?"),
        background=("Richard Wrangham proposed that cooking, by softening food and unlocking "
                    "calories, allowed smaller guts and larger brains, and created the evening "
                    "fireside as the first social institution. Critics note that solid evidence "
                    "for controlled fire only reaches back about 400,000 to 1 million years, "
                    "while key anatomical changes are older - and that raw-food diets can sustain "
                    "primates larger than us."),
        why_it_matters=("If cooking made us human, then technology - not just biology - has been "
                        "shaping our bodies for a million years, and the kitchen is the oldest "
                        "human institution."),
        sig_lens=("The Signature lens treats cooking as a calorie ledger: fire as an external "
                  "stomach, and the Signature approach balances the energy books."),
        sig_body=("The Signature proposal quantifies cooking as an external digestive organ. "
                  "Assumptions: (1) cooking raises net calorie extraction from tubers and meat "
                  "by a substantial fraction; (2) gut tissue savings can be reallocated to "
                  "brain tissue under the expensive-tissue tradeoff; (3) fire-centered evenings "
                  "extended social time. Reasoning path: rather than debating dates, the "
                  "proposal computes the calorie budget - showing that even occasional cooking "
                  "creates a surplus large enough to fund encephalization over evolutionary "
                  "time, with fire use ratcheting upward as benefits compound. The hypothesis "
                  "then predicts anatomy should track cooking intensity, not its invention date. "
                  "Limits: the archaeological fire record is sparse and contested; the model "
                  "cannot fix when habitual cooking began."),
        pointer=('The Signature system balances the calorie books, treating fire as an external stomach whose surplus could fund brain growth. The Signature test: secure hearths appear in step with gut-shrinkage anatomy across regions. It would be refuted if habitual fire use postdates completed encephalization by hundreds of millennia.'),
        key_points=[
            "Cooking increases calorie extraction and reduces digestion costs.",
            "The expensive-tissue hypothesis links gut shrinkage to brain growth.",
            "Secure fire evidence postdates some key anatomical changes.",
            "The evening fireside is proposed as the first enduring social institution.",
        ],
        requirements=[
            "Fire dates consistent with the anatomical changes cooking supposedly caused.",
            "Calorie budgets showing cooking could fund encephalization.",
            "An account of pre-fire calorie sources for early Homo.",
        ],
        standards=[
            "Archaeological fire claims checked against the primary literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wrangham R. Catching Fire: How Cooking Made Us Human. Basic Books; 2009.",
            "Gowlett JAJ. The discovery of fire by humans. Philosophical Transactions of the Royal Society B; 2016.",
        ],
        hypotheses=[
            "Cooking unlocked the calorie surplus that funded brain expansion.",
            "Anatomy changed first; cooking later amplified an existing trend.",
            "Fire mattered socially - light, warmth, gathering - more than nutritionally.",
            "Multiple calorie technologies (tools, sharing, cooking) compounded together.",
        ],
        confirm="Secure hearths appear in step with gut-shrinkage anatomy across regions.",
        refute="Habitual fire use postdates completed encephalization by hundreds of millennia.",
    ),
    dict(
        key="anthropology-07",
        name="Why Grandmothers Exist",
        group="Human Origins",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("Why do human females commonly live decades past menopause - a pattern nearly "
                 "unique among primates - instead of reproducing until death?"),
        background=("The grandmother hypothesis (Kristen Hawkes) argues that post-reproductive "
                    "women boost their genetic legacy by provisioning grandchildren, selecting "
                    "for longevity. Competing views: the mother hypothesis (long life lets a "
                    "woman raise her own late-born children), the patriarch hypothesis (male "
                    "longevity dragged female longevity along), or simple byproduct. Hadza "
                    "grandmothers do provision grandchildren heavily - but whether that selected "
                    "for menopause itself remains debated."),
        why_it_matters=("Menopause shapes every human family: it creates the grandmother, the "
                        "most important alloparent in our species, and may be why humans can "
                        "raise such costly, slow-maturing children."),
        sig_lens=("The Signature lens reads menopause as an investment ledger: when does a "
                  "woman's genes gain more from grandchildren than from another baby?"),
        sig_body=("The Signature proposal models menopause as an optimal-switching problem. "
                  "Assumptions: (1) late-life births carry rising maternal mortality; (2) human "
                  "children need provisioning for over a decade; (3) a grandmother's foraging "
                  "can measurably raise grandoffspring survival. Reasoning path: the proposal "
                  "computes the crossover age where expected genetic payoff from grandmothering "
                  "exceeds that from another birth - and finds the crossover lands near observed "
                  "menopause ages only when child dependency is long and grandmother provisioning "
                  "is effective, explaining why the pattern is rare among primates. Limits: the "
                  "model needs Hadza-like provisioning data generalized across ecologies; the "
                  "mother hypothesis makes overlapping predictions."),
        pointer=('The Signature system computes the crossover age where grandmothering outpays another birth, treating menopause as an optimal-switching problem. The Signature test: cross-cultural data show grandmother presence predicts grandoffspring survival gains. It would be refuted if menopause predates grandmother provisioning in the fossil or historical record.'),
        key_points=[
            "Humans are nearly unique among primates in long post-reproductive female life.",
            "Hadza grandmothers provision grandchildren enough to affect survival.",
            "Competing hypotheses: grandmother, mother, patriarch, byproduct.",
            "Menopause timing clusters around 45 to 55 across populations.",
        ],
        requirements=[
            "A mechanism linking grandmother provisioning to selection for longevity.",
            "An explanation for why most primates lack the pattern.",
            "Quantified payoff comparisons, not just narratives.",
        ],
        standards=[
            "Demographic claims checked against hunter-gatherer studies.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hawkes K et al. Grandmothering, menopause, and the evolution of human life histories. PNAS; 1998.",
            "Cant MA, Johnstone RA. Reproductive conflict and the separation of reproductive generations in humans. PNAS; 2008.",
        ],
        hypotheses=[
            "Grandmother provisioning selected for both menopause and longevity.",
            "Long life evolved to raise late-born children; menopause is the safer stop.",
            "Male longevity evolution dragged female lifespan along as a byproduct.",
            "Reproductive conflict between generations forced the older one to stop.",
        ],
        confirm="Cross-cultural data show grandmother presence predicts grandoffspring survival gains.",
        refute="Menopause predates grandmother provisioning in the fossil or historical record.",
    ),
    dict(
        key="anthropology-08",
        name="Why Humans Pair-Bond",
        group="Human Origins",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Why do humans - unlike nearly all other primates - form long-term pair bonds, "
                 "and did pair-bonding shape our evolution?"),
        background=("Owen Lovejoy proposed that pair-bonding drove hominin evolution: males "
                    "provisioned females and offspring, selecting for bipedal carrying, reduced "
                    "male aggression, and concealed ovulation. Critics counter that pair-bonding "
                    "is variable across cultures, that provisioning evidence is thin, and that "
                    "male competition models fit the dimorphism data better. The fossil record "
                    "offers reduced canine size (less male combat) but little direct evidence of "
                    "mating systems."),
        why_it_matters=("Pair-bonding underlies the human family, fatherhood, and much of our "
                        "social psychology. If it drove our evolution, then love - in the "
                        "biological sense - is a fossil-shaping force."),
        sig_lens=("The Signature lens treats pair-bonding as a provisioning contract: the "
                  "Signature approach asks what each partner gained that solitary foraging "
                  "could not provide."),
        sig_body=("The Signature proposal models pair-bonding as a risk-pooling contract. "
                  "Assumptions: (1) hominin infants became increasingly costly and slow to "
                  "mature; (2) foraging returns were variable day to day; (3) two cooperating "
                  "foragers smooth variance better than one. Reasoning path: the proposal shows "
                  "that as infant dependency lengthened, the variance-reduction value of a "
                  "provisioning partner exceeded the mating-opportunity cost of fidelity - "
                  "predicting pair-bonding should strengthen exactly when childhood lengthens "
                  "in the fossil record. Reduced canines and concealed ovulation follow as "
                  "contract-enforcement features. Limits: mating systems leave almost no direct "
                  "fossil trace; cultural variability challenges any single model."),
        pointer=('The Signature system models pair-bonding as a risk-pooling contract that pays when infant dependency lengthens. The Signature test: pair-bonding markers strengthen in step with lengthening childhood in the record. It would be refuted if early hominins show strong dimorphism and no provisioning anatomy.'),
        key_points=[
            "Humans are unusual among primates in widespread long-term pair-bonding.",
            "Reduced male canines suggest less male-male combat deep in our lineage.",
            "Pair-bonding intensity varies enormously across cultures.",
            "Mating systems leave almost no direct fossil evidence.",
        ],
        requirements=[
            "Consistency with reduced dimorphism and canine size.",
            "An account of cross-cultural variability.",
            "A payoff both sexes could sustain over evolutionary time.",
        ],
        standards=[
            "Claims checked against primatology and paleoanthropology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Lovejoy CO. The origin of man. Science; 1981.",
            "Chapais B. Primeval Kinship. Harvard University Press; 2008.",
        ],
        hypotheses=[
            "Provisioning contracts selected for pair-bonding as infants grew costlier.",
            "Male competition models fit better; pair-bonding is a later cultural overlay.",
            "Concealed ovulation and continuous receptivity stabilized bonds first.",
            "Cooperative breeding by whole groups preceded and enabled pair bonds.",
        ],
        confirm="Pair-bonding markers strengthen in step with lengthening childhood in the record.",
        refute="Early hominins show strong dimorphism and no provisioning anatomy.",
    ),
    dict(
        key="anthropology-09",
        name="The Origins of Language",
        group="Language and Mind",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("How, when, and why did language - open-ended, grammatical, symbolic "
                 "communication - evolve in the human lineage?"),
        background=("Language leaves no fossils. Scholars debate whether it emerged gradually "
                    "or in a sudden leap, whether gesture or vocalization came first, whether it "
                    "evolved for social bonding, teaching, gossip, or thought itself - and "
                    "whether Neanderthals shared it. The FOXP2 gene, hyoid bones, and inner-ear "
                    "anatomy offer hints, but the gap between primate call systems and full "
                    "language remains the deepest discontinuity in human evolution."),
        why_it_matters=("Language is the medium of everything human: culture, science, law, "
                        "love. Its origin is the origin of the human world as we know it."),
        sig_lens=("The Signature lens treats language as a compression technology: the "
                  "Signature approach asks what information bottleneck made grammar worth "
                  "its neural price."),
        sig_body=("The Signature proposal models language as evolving to compress teaching. "
                  "Assumptions: (1) hominin survival increasingly depended on transmitted "
                  "know-how (toolmaking, foraging, fire); (2) demonstration alone cannot teach "
                  "abstract or displaced knowledge; (3) symbolic compression lets one teacher "
                  "reach many learners. Reasoning path: the proposal shows that once cumulative "
                  "culture exists, the fitness value of transmitting a technique scales with "
                  "fidelity and reach - and grammar is the cheapest known way to achieve both, "
                  "predicting language should track the archaeological signal of cumulative "
                  "culture rather than brain size alone. Limits: the teaching-first view "
                  "struggles with why gossip and social bonding vocabularies dominate early "
                  "lexicons."),
        pointer=('The Signature system models language as compression technology for teaching, predicting it should track cumulative culture rather than brain size. The Signature test: grammatical complexity tracks cumulative-culture markers independently of brain size. It would be refuted if full language appears before any cumulative culture in the record.'),
        key_points=[
            "Language leaves no direct fossils; all evidence is indirect.",
            "Gradual versus sudden emergence remains the central split.",
            "Gesture-first and vocal-first camps both claim fossil support.",
            "Whether Neanderthals had full language is unresolved.",
        ],
        requirements=[
            "An account bridging primate call systems and full grammar.",
            "Consistency with FOXP2, hyoid, and inner-ear evidence.",
            "A selection pressure strong enough to fund the neural cost.",
        ],
        standards=[
            "Claims checked against evolutionary linguistics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fitch WT. The Evolution of Language. Cambridge University Press; 2010.",
            "Dunbar RIM. Grooming, Gossip, and the Evolution of Language. Harvard University Press; 1996.",
        ],
        hypotheses=[
            "Language evolved to compress and transmit cumulative cultural knowledge.",
            "Social bonding and gossip drove vocal elaboration first.",
            "Gesture provided the first symbolic system; speech followed.",
            "Language began as an internal thought tool, externalized later.",
        ],
        confirm="Grammatical complexity tracks cumulative-culture markers independently of brain size.",
        refute="Full language appears before any cumulative culture in the record.",
    ),
    dict(
        key="anthropology-10",
        name="Why Every Culture Has Religion",
        group="Culture and Society",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Why do supernatural beliefs and ritual practices appear in virtually every "
                 "known human culture, and what cognitive or social machinery produces them?"),
        background=("Anthropologists debate whether religion is an adaptation (group cohesion, "
                    "cooperation enforcement), a byproduct of cognitive systems (agency "
                    "detection, theory of mind applied to the unseen), or a cultural parasite. "
                    "Costly rituals - fasting, pain, sacrifice - are especially puzzling: the "
                    "costly-signaling theory says the cost IS the point, proving commitment. "
                    "No account yet explains the full pattern across foragers, chiefdoms, and "
                    "states."),
        why_it_matters=("Religion has shaped art, law, war, and morality for millennia. "
                        "Understanding its roots is understanding a force that still moves "
                        "billions - studied here as a scholarly problem in human cognition and "
                        "society, not as doctrine."),
        sig_lens=("The Signature lens treats religion as a coordination technology: the "
                  "Signature approach asks what cooperation problem was so hard that only "
                  "costly shared belief could solve it."),
        sig_body=("The Signature proposal models religion as a commitment device for "
                  "large-scale cooperation. Assumptions: (1) as groups grew past face-to-face "
                  "size, free-riding threatened collective goods; (2) monitoring everyone is "
                  "impossible at scale; (3) shared costly ritual creates hard-to-fake signals of "
                  "commitment. Reasoning path: the proposal shows that supernatural monitoring - "
                  "the belief that unseen agents watch - plus costly initiation rites jointly "
                  "solve the scaling problem, predicting that moralizing-god concepts should "
                  "appear as societies scale up, which matches the historical pattern. Limits: "
                  "the model handles social functions but not the experiential and cognitive "
                  "dimensions; correlation between scale and moralizing gods is debated."),
        pointer=('The Signature system models religion as a commitment device solving cooperation at scales past face-to-face monitoring. The Signature test: moralizing-god concepts reliably precede or accompany social scaling across regions. It would be refuted if large-scale cooperation flourishes historically without shared supernatural belief.'),
        key_points=[
            "Supernatural belief and ritual appear in virtually every documented culture.",
            "Costly rituals are the hardest feature to explain - and possibly the key.",
            "Adaptation, byproduct, and signaling theories each explain part of the pattern.",
            "Moralizing gods tend to appear as societies scale up.",
        ],
        requirements=[
            "An account covering both belief (cognition) and ritual (behavior).",
            "Consistency with the cross-cultural record, including foragers.",
            "Separation of scholarly explanation from doctrinal claims.",
        ],
        standards=[
            "Claims checked against the anthropology-of-religion literature.",
            "No doctrinal framing; beliefs described, never preached. Open status confirmed as of 2026.",
        ],
        citations=[
            "Boyer P. Religion Explained. Basic Books; 2001.",
            "Norenzayan A. Big Gods. Princeton University Press; 2013.",
        ],
        hypotheses=[
            "Religion is a commitment device enabling large-scale cooperation.",
            "Supernatural belief is a byproduct of agency-detection and theory-of-mind systems.",
            "Costly rituals signal commitment and sort cooperators from free-riders.",
            "Religion culturally evolved as groups competed; cooperative groups won.",
        ],
        confirm="Moralizing-god concepts reliably precede or accompany social scaling across regions.",
        refute="Large-scale cooperation flourishes historically without shared supernatural belief.",
    ),
    dict(
        key="anthropology-11",
        name="The Incest Taboo",
        group="Culture and Society",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Why do all human societies prohibit incest, and is the taboo rooted in "
                 "biology, in culture, or in both?"),
        background=("The Westermarck effect - childhood co-residence dampening sexual attraction - "
                    "suggests a biological basis, supported by inbreeding depression data. Yet "
                    "taboos vary wildly in whom they cover (cousins in, cousins out), and Freud "
                    "argued the taboo exists precisely because the desire exists. Royal "
                    "inbreeding (Egyptian, Habsburg) shows elites sometimes defied it - with "
                    "measurable genetic costs."),
        why_it_matters=("The incest taboo sits exactly on the biology-culture boundary, making it "
                        "the test case for how nature and nurture interact in human morality."),
        sig_lens=("The Signature lens treats the taboo as two layered systems - a dampening "
                  "circuit plus a cultural amplifier - and asks where each does its work."),
        sig_body=("The Signature proposal models the taboo as a dual system. Assumptions: (1) the "
                  "Westermarck mechanism provides a biological baseline of aversion among "
                  "co-raised children; (2) inbreeding depression creates real fitness costs; "
                  "(3) cultural rules extend the baseline to kin categories biology cannot "
                  "track (cousins, affines). Reasoning path: the proposal predicts the "
                  "universal core (parent-child, sibling) should follow co-residence patterns "
                  "while the variable fringe (cousin marriage rules) should follow alliance "
                  "economics - matching the observed pattern where the core is stable and the "
                  "fringe tracks marriage-exchange systems. Limits: the model cannot cleanly "
                  "separate learned aversion from taught rule in any given society."),
        pointer=('The Signature system models a universal biological core plus a variable cultural fringe that tracks marriage-exchange economics. The Signature test: core prohibitions track co-residence while fringe rules track alliance economics. It would be refuted if aversion appears strongly without any co-residence, or never appears with it.'),
        key_points=[
            "Parent-child and sibling prohibitions are effectively universal.",
            "Cousin-marriage rules vary dramatically across cultures.",
            "Inbreeding depression is real and measurable (Habsburg data).",
            "The Westermarck effect links co-residence to aversion.",
        ],
        requirements=[
            "An account covering both the universal core and the variable fringe.",
            "Consistency with inbreeding-depression genetics.",
            "Separation of biological aversion from cultural rule.",
        ],
        standards=[
            "Genetic claims checked against inbreeding literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Westermarck E. The History of Human Marriage. Macmillan; 1891.",
            "Wolf AP, Huang CS. Marriage and Adoption in China. Stanford University Press; 1980.",
        ],
        hypotheses=[
            "A biological aversion core plus cultural extension explains the full pattern.",
            "The taboo is primarily cultural, built to structure alliances.",
            "Inbreeding avoidance is learned from observing deformed offspring.",
            "The taboo mainly suppresses within-family sexual competition.",
        ],
        confirm="Core prohibitions track co-residence while fringe rules track alliance economics.",
        refute="Aversion appears strongly without any co-residence, or never appears with it.",
    ),
    dict(
        key="anthropology-12",
        name="Why Farm: The Agricultural Riddle",
        group="Deep Time",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Why did humans adopt agriculture - more work, worse nutrition, new diseases - "
                 "independently in at least eleven world regions?"),
        background=("Farming made life harder by most measures: skeletons show stature shrank, "
                    "teeth decayed, and labor rose. Yet agriculture was invented independently in "
                    "the Fertile Crescent, China, Mesoamerica, the Andes, New Guinea, and more. "
                    "Explanations range from climate-driven necessity (the Younger Dryas), to "
                    "population pressure (Boserup), to social competition and feasting (Hayden), "
                    "to sheer accident. The riddle deepens because foragers knew about seeds for "
                    "millennia before planting them."),
        why_it_matters=("Agriculture created civilization - cities, states, writing, inequality. "
                        "If we do not know why it started, we do not know why the modern world "
                        "exists."),
        sig_lens=("The Signature lens treats farming as a trap, not a choice: the Signature "
                  "approach looks for the ratchet - the step nobody could walk back from."),
        sig_body=("The Signature proposal models agriculture as a competitive ratchet. "
                  "Assumptions: (1) in rich environments, groups that intensified production "
                  "could field more warriors and feasts; (2) intensification raised local "
                  "population density; (3) dense populations could not return to foraging "
                  "because the wild food base was depleted. Reasoning path: the proposal shows "
                  "that even if the first farmers were worse off individually, groups that "
                  "farmed outcompeted groups that did not - and once population crossed the "
                  "foraging carrying capacity, retreat became impossible. Farming spreads not "
                  "because it is good but because it is a Nash equilibrium. Limits: the model "
                  "needs the initial intensification motive, which still varies by region."),
        pointer=('The Signature system models agriculture as a competitive ratchet nobody could walk back from, rather than a rational choice. The Signature test: farming appears first where intergroup competition was most intense. It would be refuted if agriculture arises in regions with no competition, no pressure, and stable climate.'),
        key_points=[
            "Agriculture arose independently in at least eleven regions.",
            "Early farmers were shorter, sicker, and worked harder than foragers.",
            "Foragers understood seeds for millennia before farming.",
            "Population pressure, climate, and social competition all have regional support.",
        ],
        requirements=[
            "An account of independent invention across ecologies.",
            "An explanation for why foragers delayed so long.",
            "A mechanism making the transition effectively irreversible.",
        ],
        standards=[
            "Archaeological claims checked against the origins-of-agriculture literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Diamond J. Guns, Germs, and Steel. Norton; 1997.",
            "Boserup E. The Conditions of Agricultural Growth. Aldine; 1965.",
        ],
        hypotheses=[
            "Intergroup competition created a ratchet no group could escape.",
            "Post-glacial climate instability forced intensification.",
            "Population growth demanded more calories per acre.",
            "Feasting and status rivalry drove surplus production first.",
        ],
        confirm="Farming appears first where intergroup competition was most intense.",
        refute="Agriculture arises in regions with no competition, no pressure, and stable climate.",
    ),
    dict(
        key="anthropology-13",
        name="The Peopling of the Americas",
        group="Deep Time",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("When, by what route, and in how many waves did humans first reach the Americas?"),
        background=("The Clovis-first model (about 13,000 years ago via an ice-free corridor) "
                    "collapsed under pre-Clovis sites: Monte Verde in Chile (about 14,500 years "
                    "ago), Cooper Ferry in Idaho, and New Mexico footprints dated to about "
                    "23,000 years ago. A coastal kelp-highway route is now favored, but the "
                    "earliest coastline is drowned. Genetics supports a single major migration "
                    "with later Arctic waves - yet the archaeology keeps pushing dates earlier."),
        why_it_matters=("The Americas were the last great human frontier. Their peopling is the "
                        "final chapter of the human dispersal - and the dates keep moving."),
        sig_lens=("The Signature lens treats the peopling as a search problem over drowned "
                  "landscapes: the Signature approach maps where evidence should be, not just "
                  "where it was found."),
        sig_body=("The Signature proposal models the migration as a coastal probability field. "
                  "Assumptions: (1) Pleistocene coastlines with kelp-forest ecologies offered "
                  "continuous food; (2) sea-level rise drowned the earliest camps; (3) interior "
                  "corridors opened later. Reasoning path: the proposal weights each candidate "
                  "route by reconstructing resource continuity along now-submerged shelves, "
                  "predicting the earliest sites should cluster on drowned coastal plains - "
                  "which matches the pattern of the oldest accepted sites hugging ancient "
                  "shorelines. The ice-free corridor then becomes a secondary, later route. "
                  "Limits: submerged archaeology is brutally hard; the model predicts where to "
                  "look but cannot date what is not yet found."),
        pointer=('The Signature system models a coastal probability field over drowned shelves, predicting where the earliest camps should lie. The Signature test: submerged-shelf archaeology recovers camps older than any interior site. It would be refuted if the earliest secure sites all postdate the corridor opening and sit inland.'),
        key_points=[
            "Clovis-first is falsified; pre-Clovis sites are now well accepted.",
            "New Mexico footprints suggest presence about 23,000 years ago.",
            "The favored coastal route is largely underwater today.",
            "Genetics supports one major wave plus later Arctic migrations.",
        ],
        requirements=[
            "Reconciliation of genetic wave models with early archaeological dates.",
            "A route passable during the Last Glacial Maximum.",
            "An explanation for the drowned-coastline evidence gap.",
        ],
        standards=[
            "Site dates checked against the primary peopling literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Dillehay TD. Monte Verde: A Late Pleistocene Settlement in Chile. Smithsonian; 1989.",
            "Bennett MR et al. Evidence of humans in North America during the Last Glacial Maximum. Science; 2021.",
        ],
        hypotheses=[
            "A coastal kelp-highway carried the first migrants before the corridor opened.",
            "The ice-free corridor was the primary route after all.",
            "Multiple early waves arrived, most leaving no genetic trace.",
            "Interior and coastal routes were used nearly simultaneously.",
        ],
        confirm="Submerged-shelf archaeology recovers camps older than any interior site.",
        refute="The earliest secure sites all postdate the corridor opening and sit inland.",
    ),
    dict(
        key="anthropology-14",
        name="The Upper Paleolithic Creative Explosion",
        group="Deep Time",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("Why did art, ornament, burial ritual, and complex technology erupt across "
                 "Eurasia around 40,000 to 50,000 years ago after millions of years of "
                 "slow change?"),
        background=("Anatomically modern humans existed for 100,000+ years before the European "
                    "Upper Paleolithic explosion of cave painting, carved figurines, tailored "
                    "clothing, and elaborate burials. Theories: a genetic mutation for modern "
                    "cognition, demographic critical mass, cumulative culture reaching takeoff, "
                    "or simply better preservation in Europe. African archaeology now shows "
                    "earlier sparks - Blombos ochre engravings at 75,000 years - muddying the "
                    "explosion narrative."),
        why_it_matters=("This is the birth of the symbolic world - art, ritual, story. Whatever "
                        "ignited it ignited humanity as we know it."),
        sig_lens=("The Signature lens reads the explosion as a network effect: the Signature "
                  "approach asks what happens when connected minds cross a critical density."),
        sig_body=("The Signature proposal models the explosion as a connectivity phase "
                  "transition. Assumptions: (1) innovations are usually lost in small isolated "
                  "bands; (2) retention probability rises steeply with network size; (3) the "
                  "Out-of-Africa dispersals and later population growth expanded networks. "
                  "Reasoning path: the proposal shows that below a critical connected-population "
                  "threshold, novelties die with their inventors, while above it they accumulate "
                  "- producing an apparent sudden explosion from a gradual demographic cause. "
                  "The African sparks are then early local crossings of the threshold. Limits: "
                  "the model needs population estimates the record barely provides; a cognitive "
                  "mutation remains unfalsified."),
        pointer=('The Signature system models the explosion as a connectivity phase transition, with demography - not mutation - as the trigger. The Signature test: symbolic bursts correlate with demographic expansion signals, not anatomy changes. It would be refuted if a single genetic sweep coincides precisely with the explosion across regions.'),
        key_points=[
            "Symbolic behavior explodes in Eurasia about 40,000 to 50,000 years ago.",
            "African sites show earlier sparks (Blombos, about 75,000 years).",
            "Anatomically modern humans predate the explosion by 100,000+ years.",
            "Mutation, demography, and preservation bias all have defenders.",
        ],
        requirements=[
            "An account of the long lag between anatomy and behavior.",
            "Consistency with the earlier African sparks.",
            "A mechanism producing sudden appearance from gradual causes.",
        ],
        standards=[
            "Site dates checked against the primary literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mellars P. The impossible coincidence. Evolutionary Anthropology; 2005.",
            "Henshilwood CS et al. Emergence of modern human behaviour. Journal of Human Evolution; 2002.",
        ],
        hypotheses=[
            "Connected-population thresholds triggered cumulative culture takeoff.",
            "A late genetic change rewired cognition around 50,000 years ago.",
            "The explosion is a European preservation illusion.",
            "Climate volatility selected for symbolic information storage.",
        ],
        confirm="Symbolic bursts correlate with demographic expansion signals, not anatomy changes.",
        refute="A single genetic sweep coincides precisely with the explosion across regions.",
    ),
    dict(
        key="anthropology-15",
        name="The Megafaunal Extinctions",
        group="Deep Time",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("What killed the mammoths, giant sloths, saber-tooths, and dozens of other "
                 "megafauna across the continents at the end of the Pleistocene?"),
        background=("Between about 50,000 and 10,000 years ago, most large mammals vanished from "
                    "the Americas, Australia, and northern Eurasia - while Africa kept most of "
                    "its giants. Climate change and human overkill are the rival camps, with "
                    "combination theories gaining ground. The pattern is suspicious: extinctions "
                    "track human arrival on each continent, yet the largest, fastest climate "
                    "swings sometimes do not match."),
        why_it_matters=("This is the first great human-caused extinction debate - and its answer "
                        "calibrates everything we claim about humanity's ecological footprint "
                        "today."),
        sig_lens=("The Signature lens treats extinction as a stress budget: the Signature "
                  "approach adds human and climate pressures instead of choosing between them."),
        sig_body=("The Signature proposal models extinction as a two-stress budget. Assumptions: "
                  "(1) megafauna reproduce slowly, so populations recover slowly; (2) climate "
                  "swings shrink and fragment habitat; (3) even light human hunting adds "
                  "mortality to the slowest breeders. Reasoning path: the proposal computes that "
                  "neither stress alone reliably kills continent-scale populations, but their "
                  "sum crosses the replacement threshold for slow-breeding giants - explaining "
                  "why Africa (where fauna co-evolved with humans) survived while naive "
                  "continents did not. Limits: hunting-intensity data are sparse; some "
                  "extinctions precede secure human arrival dates."),
        pointer=('The Signature system adds human and climate stresses into one replacement-threshold budget instead of picking a single cause. The Signature test: extinction timing matches the sum of both stresses better than either alone. It would be refuted if major extinctions occur with neither humans present nor climate anomaly.'),
        key_points=[
            "Most large mammals vanished from the Americas, Australia, and northern Eurasia.",
            "Africa retained most of its megafauna.",
            "Extinctions broadly track human arrival per continent.",
            "Slow breeders were hit hardest - a demographic signature.",
        ],
        requirements=[
            "An account of the African exception.",
            "Consistency with extinctions that precede secure human dates.",
            "Demographic plausibility for slow-breeding giants.",
        ],
        standards=[
            "Extinction chronologies checked against the primary literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Koch PL, Barnosky AD. Late Quaternary extinctions. Annual Review of Ecology; 2006.",
            "Sandom C et al. Global late Quaternary megafauna extinctions linked to humans. Proc. Royal Society B; 2014.",
        ],
        hypotheses=[
            "Combined climate fragmentation and human hunting crossed replacement thresholds.",
            "Human overkill alone drove the extinctions.",
            "Climate change alone drove the extinctions.",
            "Disease or comet impacts played decisive roles.",
        ],
        confirm="Extinction timing matches the sum of both stresses better than either alone.",
        refute="Major extinctions occur with neither humans present nor climate anomaly.",
    ),
    dict(
        key="anthropology-16",
        name="Why Writing Was Invented Four Times",
        group="Deep Time",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("Why did full writing emerge independently in Mesopotamia, Egypt, China, and "
                 "Mesoamerica - but nowhere else - and what triggered each invention?"),
        background=("Writing was invented from scratch at least four times, always in the "
                    "context of complex administration: Sumerian tokens and tablets, Egyptian "
                    "hieroglyphs, Chinese oracle bones, Maya glyphs. Yet many complex societies "
                    "(the Inca ran an empire on knotted quipu) never developed it. Theories "
                    "invoke state bureaucracy, trade accounting, ritual recording, or elite "
                    "competition - but the threshold conditions remain unclear."),
        why_it_matters=("Writing is the technology that lets societies remember across "
                        "generations. Its independent invention marks the moments states became "
                        "too complex for human memory alone."),
        sig_lens=("The Signature lens treats writing as an overflow valve: the Signature "
                  "approach asks what volume of obligation-records breaks unaided memory."),
        sig_body=("The Signature proposal models writing as an administrative-overflow "
                  "invention. Assumptions: (1) human working memory caps the obligations one "
                  "administrator can track; (2) states multiply obligations (taxes, rations, "
                  "labor); (3) tokens and tallies extend memory only so far. Reasoning path: "
                  "the proposal estimates the obligation load at which token systems fail and "
                  "finds the four pristine inventions cluster just past that load - while the "
                  "Inca quipu, a sophisticated parallel system, handled their empire's load "
                  "without true writing. Writing appears where the books outgrew the brain. "
                  "Limits: ritual-first theories (oracle bones, Maya) fit awkwardly; the "
                  "obligation-load estimates are rough."),
        pointer=('The Signature system models writing as administrative overflow, appearing where obligation loads outgrew unaided memory. The Signature test: invention dates track measured administrative-load thresholds across cases. It would be refuted if a pristine script appears in a small-scale society with light administration.'),
        key_points=[
            "Full writing was invented independently at least four times.",
            "Each invention sits in a complex administrative context.",
            "The Inca ran an empire without true writing (quipu).",
            "Ritual uses (oracle bones, Maya glyphs) complicate bureaucratic theories.",
        ],
        requirements=[
            "Threshold conditions separating inventors from non-inventors.",
            "An account of ritual-first cases.",
            "Consistency with quipu as a near-miss alternative.",
        ],
        standards=[
            "Claims checked against the history-of-writing literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Schmandt-Besserat D. How Writing Came About. University of Texas Press; 1996.",
            "Houston SD. The First Writing. Cambridge University Press; 2004.",
        ],
        hypotheses=[
            "Administrative obligation overload forced the invention.",
            "Ritual and divination recording came first, bureaucracy followed.",
            "Elite competition for prestige drove script elaboration.",
            "Writing needed both state scale and a prior token-accounting tradition.",
        ],
        confirm="Invention dates track measured administrative-load thresholds across cases.",
        refute="A pristine script appears in a small-scale society with light administration.",
    ),
    dict(
        key="anthropology-17",
        name="From Chiefdoms to States",
        group="Culture and Society",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Why do some chiefdoms become states - with bureaucracy, taxation, and "
                 "monopoly of force - while most never do?"),
        background=("The state emerged independently in only a handful of places: Mesopotamia, "
                    "Egypt, the Indus, China, Mesoamerica, the Andes. Theories compete: "
                    "hydraulic (Wittfogel - irrigation management), warfare (Carneiro - "
                    "circumscription plus war), trade, population pressure, and ideology. Each "
                    "fits some cases and fails others; no covering law has survived testing."),
        why_it_matters=("The state is the political form under which most humans now live. Its "
                        "origins are the origins of taxation, bureaucracy, and organized war."),
        sig_lens=("The Signature lens treats state formation as a scaling crisis: the "
                  "Signature approach asks what breaks when a chiefdom outgrows personal rule."),
        sig_body=("The Signature proposal models the state as a solution to the scaling "
                  "crisis of personal rule. Assumptions: (1) chiefdoms run on personal ties, "
                  "which cap at a few thousand people; (2) circumscribed environments prevent "
                  "losers from leaving; (3) warfare concentrates power. Reasoning path: the "
                  "proposal shows that where exit is blocked and conflict is chronic, chiefs "
                  "must routinize extraction and coercion to survive - bureaucracy is what "
                  "personal rule becomes when it can no longer know everyone. Pristine states "
                  "then cluster exactly where circumscription meets warfare. Limits: the model "
                  "underplays ideology and trade; some states formed with modest warfare."),
        pointer=('The Signature system models the state as personal rule routinized past the scale where everyone can know everyone. The Signature test: pristine states map onto circumscribed, conflict-prone environments. It would be refuted if a pristine state forms in open, peaceful, low-population conditions.'),
        key_points=[
            "Pristine states arose independently only about six times.",
            "Hydraulic, warfare, trade, and population theories each fit partially.",
            "Circumscription - nowhere to run - recurs across theories.",
            "Most chiefdoms never became states.",
        ],
        requirements=[
            "An account of the six pristine cases without cherry-picking.",
            "A mechanism separating state-formers from permanent chiefdoms.",
            "Consistency with low-warfare state formations.",
        ],
        standards=[
            "Claims checked against the state-formation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Carneiro RL. A theory of the origin of the state. Science; 1970.",
            "Wittfogel KA. Oriental Despotism. Yale University Press; 1957.",
        ],
        hypotheses=[
            "Circumscription plus warfare forced the routinization of power.",
            "Irrigation management created the first bureaucracies.",
            "Trade networks demanded neutral enforcement at scale.",
            "Ideology and ritual authority scaled first; coercion followed.",
        ],
        confirm="Pristine states map onto circumscribed, conflict-prone environments.",
        refute="A pristine state forms in open, peaceful, low-population conditions.",
    ),
    dict(
        key="anthropology-18",
        name="Why Complex Societies Collapse",
        group="Culture and Society",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Is there a general theory of why complex societies - Rome, the Maya, "
                 "Mesopotamian states - collapse, or is each fall unique?"),
        background=("Joseph Tainter argued that societies collapse when the marginal returns on "
                    "complexity turn negative: solving problems by adding bureaucracy eventually "
                    "costs more than it yields. Jared Diamond emphasized environmental "
                    "mismanagement. Others stress invasions, disease, climate, or elite "
                    "overproduction. The debate splits between generalists seeking covering laws "
                    "and particularists insisting each collapse is its own story."),
        why_it_matters=("Every modern state is a complex society. A general theory of collapse is "
                        "a theory of our own fragility - and of what might save us."),
        sig_lens=("The Signature lens treats collapse as a returns ledger: the Signature "
                  "approach tracks the marginal yield of each added layer of complexity."),
        sig_body=("The Signature proposal formalizes Tainter's curve as a testable ledger. "
                  "Assumptions: (1) complexity (administration, military, infrastructure) has "
                  "measurable costs; (2) problem-solving yields measurable benefits; (3) "
                  "societies add complexity when benefits exceed costs. Reasoning path: the "
                  "proposal shows that as easy solutions are exhausted, each new layer buys "
                  "less stability per unit cost - until a shock that an earlier, leaner society "
                  "would have absorbed becomes fatal. Collapse is then rarely caused by the "
                  "trigger; the trigger merely finds a society with no surplus left. Limits: "
                  "quantifying ancient costs and benefits is approximate; some collapses look "
                  "more like transformations than failures."),
        pointer=('The Signature system formalizes collapse as declining marginal returns on complexity, with shocks as triggers rather than causes. The Signature test: measured complexity costs predict vulnerability across independent cases. It would be refuted if societies with strongly negative returns persist indefinitely without collapse.'),
        key_points=[
            "Tainter's diminishing-returns model is the leading general theory.",
            "Environmental, invasion, disease, and climate accounts compete per case.",
            "Collapses often look like transformations, not sheer disappearance.",
            "No covering law has survived cross-case testing intact.",
        ],
        requirements=[
            "Cross-case testing, not single-case storytelling.",
            "A distinction between trigger and underlying vulnerability.",
            "Measurable proxies for complexity costs and benefits.",
        ],
        standards=[
            "Claims checked against the collapse literature (Tainter, Diamond, and critics).",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Tainter JA. The Collapse of Complex Societies. Cambridge University Press; 1988.",
            "Diamond J. Collapse. Viking; 2005.",
        ],
        hypotheses=[
            "Declining marginal returns on complexity is the general mechanism.",
            "Environmental mismanagement is the recurring driver.",
            "Elite overproduction and inequality fracture societies from within.",
            "Each collapse is historically unique; no general theory exists.",
        ],
        confirm="Measured complexity costs predict vulnerability across independent cases.",
        refute="Societies with strongly negative returns persist indefinitely without collapse.",
    ),
    dict(
        key="anthropology-19",
        name="The Original Affluent Society Debate",
        group="Culture and Society",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("Were hunter-gatherers the original affluent society - working few hours, "
                 "well nourished - or is that a romantic myth?"),
        background=("Marshall Sahlins argued that foragers, wanting little, were affluent: the "
                    "Hadza and !Kung worked perhaps 15 to 20 hours a week for subsistence. "
                    "Critics reply with high violence rates, infanticide, and periodic hunger in "
                    "the ethnographic record - affluence with an asterisk. The debate shapes "
                    "everything from economics (what is wealth?) to politics (was prehistory "
                    "a fall from grace?)."),
        why_it_matters=("The answer sets the baseline for human well-being: it tells us whether "
                        "civilization improved life or traded leisure and health for power and "
                        "numbers."),
        sig_lens=("The Signature lens treats affluence as a wants-to-work ratio: the Signature "
                  "approach asks what happens when wants are culturally capped."),
        sig_body=("The Signature proposal reframes the debate as a moving target. Assumptions: "
                  "(1) forager wants were socially capped at modest levels; (2) forager "
                  "work-hours data reflect favorable environments and seasons; (3) violence and "
                  "hunger risks were real but episodic. Reasoning path: the proposal shows both "
                  "camps can be right - foragers enjoyed high hourly returns and short "
                  "workdays AND faced catastrophic tail risks (drought, conflict) that farmers "
                  "buffered with storage. Affluence is then real in the median but fragile in "
                  "the variance, which is why the debate never settles: each side measures a "
                  "different moment of the distribution. Limits: paleolithic conditions are "
                  "inferred from modern foragers in marginal environments."),
        pointer=('The Signature system splits the difference by distribution: affluent in the median, fragile in the variance. The Signature test: risk-adjusted well-being measures favor foragers in rich environments. It would be refuted if forager skeletons show chronic stress matching or exceeding early farmers.'),
        key_points=[
            "Some foragers worked roughly 15 to 20 hours a week for subsistence.",
            "Ethnographic records also show violence, hunger, and infanticide.",
            "Sahlins framed affluence as limited wants, not abundant goods.",
            "Modern foragers live in marginal environments, biasing comparisons.",
        ],
        requirements=[
            "Separation of median conditions from tail risks.",
            "Environment-adjusted comparisons, not raw ethnography.",
            "A definition of affluence that both camps can test.",
        ],
        standards=[
            "Ethnographic claims checked against the primary sources.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Sahlins M. Stone Age Economics. Aldine-Atherton; 1972.",
            "Lee RB. The !Kung San. Cambridge University Press; 1979.",
        ],
        hypotheses=[
            "Foragers were affluent in the median but exposed in the variance.",
            "The affluent image is romantic selection bias.",
            "Affluence is real wherever environments are rich and wants capped.",
            "Farming improved security at the cost of daily well-being.",
        ],
        confirm="Risk-adjusted well-being measures favor foragers in rich environments.",
        refute="Forager skeletons show chronic stress matching or exceeding early farmers.",
    ),
    dict(
        key="anthropology-20",
        name="Why Humans Cooperate With Strangers",
        group="Culture and Society",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Why do humans routinely cooperate with non-kin strangers - in markets, "
                 "armies, and cities - when evolution supposedly favors kin and reciprocators?"),
        background=("Cooperation with strangers is evolutionarily puzzling: anonymous "
                    "one-shot cooperation should be invaded by free-riders. Explanations "
                    "include cultural group selection (cooperative groups outcompete), "
                    "reputation systems, punishment institutions, and gene-culture "
                    "coevolution. Experiments show cooperation varies hugely across societies - "
                    "market-integrated societies cooperate more with strangers, suggesting "
                    "institutions train the behavior."),
        why_it_matters=("Stranger cooperation is the foundation of cities, markets, and states. "
                        "Understanding it is understanding how millions of unrelated people live "
                        "together."),
        sig_lens=("The Signature lens treats stranger cooperation as an institutional "
                  "technology: the Signature approach asks what machinery makes trust "
                  "rational."),
        sig_body=("The Signature proposal models cooperation as institutionally scaffolded. "
                  "Assumptions: (1) raw human psychology supports kin and repeated-interaction "
                  "cooperation only; (2) reputation, punishment, and norms extend the circle; "
                  "(3) groups with better scaffolds outcompete groups without. Reasoning path: "
                  "the proposal shows stranger cooperation needs no new psychology - only "
                  "cultural scaffolds that convert one-shot games into repeated ones "
                  "(reputation) or raise defection costs (punishment). The cross-cultural "
                  "variance then reflects scaffold variance, not nature variance. Limits: the "
                  "model leans on group selection, which remains contested; the origins of the "
                  "first scaffolds are unexplained."),
        pointer=('The Signature system treats stranger cooperation as culturally scaffolded, with institutions converting one-shot games into repeated ones. The Signature test: scaffold strength predicts cooperation levels across societies. It would be refuted if high cooperation persists where no scaffolds exist and groups do not compete.'),
        key_points=[
            "One-shot anonymous cooperation should be invadable by free-riders.",
            "Cooperation with strangers varies hugely across societies.",
            "Market-integrated societies show more stranger cooperation.",
            "Punishment and reputation are the leading scaffold candidates.",
        ],
        requirements=[
            "A mechanism stable against free-riding.",
            "An account of cross-cultural variance.",
            "Consistency with the evolutionary record of small bands.",
        ],
        standards=[
            "Experimental claims checked against the behavioral-economics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Henrich J et al. Markets, religion, community size, and the evolution of fairness and punishment. Science; 2010.",
            "Boyd R, Richerson PJ. Culture and the evolution of human cooperation. Phil. Trans. Royal Society B; 2009.",
        ],
        hypotheses=[
            "Cultural group selection spread cooperative scaffolds.",
            "Reputation systems alone suffice to stabilize cooperation.",
            "Punishment institutions are the load-bearing scaffold.",
            "Stranger cooperation is a misfiring of kin psychology.",
        ],
        confirm="Scaffold strength predicts cooperation levels across societies.",
        refute="High cooperation persists where no scaffolds exist and groups do not compete.",
    ),
    dict(
        key="anthropology-21",
        name="The Evolution of Morality",
        group="Language and Mind",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("How did moral judgment - right, wrong, fairness, punishment - evolve, and how "
                 "much of it is universal versus cultural?"),
        background=("Moral foundations theory proposes several innate foundations (care, "
                    "fairness, loyalty, authority, purity) tuned by culture. Primatologists "
                    "find proto-moral behavior - inequity aversion, consolation, punishment - in "
                    "apes. Yet moral codes vary radically: honor cultures, dignity cultures, and "
                    "their opposites. The nativist-constructivist split remains the field's "
                    "deepest divide."),
        why_it_matters=("Morality governs law, politics, and everyday life. Knowing which parts "
                        "are built-in and which are taught changes how we argue about right "
                        "and wrong."),
        sig_lens=("The Signature lens treats morality as conflict-resolution software: the "
                  "Signature approach asks which recurrent conflicts needed automatic answers."),
        sig_body=("The Signature proposal models moral foundations as conflict solvers. "
                  "Assumptions: (1) social life generates recurrent conflicts (cheating, "
                  "harm, free-riding, hierarchy disputes); (2) negotiated solutions are slow; "
                  "(3) fast automatic judgments outcompete deliberation under time pressure. "
                  "Reasoning path: the proposal maps each proposed foundation to a specific "
                  "recurrent conflict and shows automaticity pays exactly where stakes are "
                  "high and time is short - predicting universals should cluster around "
                  "high-stakes conflicts (harm, cheating) while low-stakes domains (purity, "
                  "authority) vary culturally, which matches the data. Limits: the mapping is "
                  "post hoc without independent conflict-frequency measures."),
        pointer=('The Signature system maps each moral foundation to the recurrent conflict it automatically resolves. The Signature test: universals cluster at high-stakes conflicts; variation sits in low-stakes domains. It would be refuted if no moral judgment shows cross-cultural stability under testing.'),
        key_points=[
            "Apes show inequity aversion, consolation, and third-party punishment.",
            "Moral codes vary radically across cultures.",
            "Nativist versus constructivist accounts remain deadlocked.",
            "Harm and fairness show the strongest universality signals.",
        ],
        requirements=[
            "An account covering both universals and variation.",
            "Consistency with primate proto-morality.",
            "Testable predictions separating nativist from cultural claims.",
        ],
        standards=[
            "Claims checked against the moral-psychology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Haidt J. The Righteous Mind. Pantheon; 2012.",
            "de Waal F. Primates and Philosophers. Princeton University Press; 2006.",
        ],
        hypotheses=[
            "Moral foundations are evolved conflict solvers, culturally tuned.",
            "Morality is largely constructed by culture on thin innate bases.",
            "Moral judgment is post hoc rationalization of emotional reactions.",
            "Cooperation pressures selected for genuinely other-regarding motives.",
        ],
        confirm="Universals cluster at high-stakes conflicts; variation sits in low-stakes domains.",
        refute="No moral judgment shows cross-cultural stability under testing.",
    ),
    dict(
        key="anthropology-22",
        name="Ritual: Why Costly Rituals Persist",
        group="Culture and Society",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("Why do humans everywhere perform costly rituals - painful initiations, "
                 "wasteful sacrifices, time-consuming ceremonies - that seem to harm the "
                 "participants?"),
        background=("Costly signaling theory says the cost is the point: enduring pain or "
                    "waste proves commitment to the group, sorting true believers from "
                    "free-riders. The ritual-modes theory distinguishes rare, traumatic "
                    "imagistic rituals (bonding small groups) from frequent, low-arousal "
                    "doctrinal rituals (spreading large traditions). Synchrony research shows "
                    "moving together literally bonds people. Yet why the costs take their "
                    "specific forms remains unexplained."),
        why_it_matters=("Ritual is the oldest social technology - older than law, markets, or "
                        "states. Its logic may be the logic of all human institutions."),
        sig_lens=("The Signature lens treats ritual as a sorting machine: the Signature "
                  "approach asks what price separates the committed from the pretenders."),
        sig_body=("The Signature proposal models ritual as a two-channel device. Assumptions: "
                  "(1) groups need to identify committed members; (2) words are cheap, pain is "
                  "not; (3) synchrony creates measurable prosociality. Reasoning path: the "
                  "proposal shows costly initiation sorts members (the imagistic channel) "
                  "while repeated low-cost ritual maintains doctrine (the doctrinal channel) - "
                  "and predicts the cost level should track the value of group membership, "
                  "explaining why high-stakes groups (warriors, sects) demand the most "
                  "extreme rites. Limits: the model explains function, not the symbolic "
                  "content that makes each ritual meaningful to participants."),
        pointer=('The Signature system models ritual as a two-channel sorting and maintenance device, with costs tracking membership value. The Signature test: ritual cost levels track the material value of group membership. It would be refuted if the costliest rituals belong to the lowest-stakes groups.'),
        key_points=[
            "Costly rituals appear in every known culture.",
            "Costly signaling theory makes the cost the mechanism.",
            "Imagistic versus doctrinal modes explain ritual diversity.",
            "Synchrony measurably increases prosocial behavior.",
        ],
        requirements=[
            "An account of both sorting and bonding functions.",
            "A prediction for observed cost levels.",
            "Consistency with secular rituals (armies, sports, fraternities).",
        ],
        standards=[
            "Claims checked against the ritual-studies literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Whitehouse H. Modes of Religiosity. AltaMira; 2004.",
            "Sosis R, Alcorta C. Signaling, solidarity, and the sacred. Annual Review of Anthropology; 2003.",
        ],
        hypotheses=[
            "Rituals are commitment-sorting machines with costs set by membership value.",
            "Rituals primarily bond through synchrony and shared arousal.",
            "Rituals transmit hard-to-teach norms through embodied experience.",
            "Ritual costs are runaway cultural byproducts, not adaptations.",
        ],
        confirm="Ritual cost levels track the material value of group membership.",
        refute="The costliest rituals belong to the lowest-stakes groups.",
    ),
    dict(
        key="anthropology-23",
        name="The Self-Domestication Hypothesis",
        group="Human Origins",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Did humans domesticate themselves - selecting against aggression and for "
                 "cooperation - and does that explain our unusual anatomy and behavior?"),
        background=("Domesticated animals share a syndrome: smaller faces, smaller teeth, "
                    "reduced aggression, extended juvenility. Humans show the same pattern "
                    "relative to Neanderthals and early Homo sapiens. Proposed mechanisms: "
                    "selection against reactive aggression (Wrangham), female mate choice, or "
                    "group-level selection for cooperativeness. Critics note the syndrome may "
                    "be a developmental byproduct, not a selected package."),
        why_it_matters=("If we are self-domesticated, then human nature - our cooperativeness "
                        "and our remaining aggression - is partly an artifact of ancient social "
                        "selection, with implications for everything from criminal justice to "
                        "education."),
        sig_lens=("The Signature lens treats domestication as a culling ledger: the Signature "
                  "approach asks who got excluded from reproduction, and why."),
        sig_body=("The Signature proposal models self-domestication as coalitionary culling. "
                  "Assumptions: (1) language-enabled coalitions could coordinate against "
                  "bullies; (2) executing or ostracizing aggressive males removed their genes; "
                  "(3) reduced aggression has developmental side effects (the syndrome). "
                  "Reasoning path: the proposal shows that once coalitions can reliably "
                  "eliminate the most reactive aggressors, selection against aggression becomes "
                  "self-reinforcing - each generation is easier to coordinate than the last, "
                  "producing the anatomical syndrome as a correlated response. Limits: the "
                  "execution evidence is ethnographic analogy; the neural-crest mechanism "
                  "remains debated."),
        pointer=('The Signature system models self-domestication as language-enabled coalitions culling reactive aggressors generation after generation. The Signature test: facial reduction tracks independent evidence of coalitionary punishment. It would be refuted if aggression levels show no decline across the relevant fossil sequence.'),
        key_points=[
            "Humans show the domestication syndrome relative to archaic humans.",
            "The leading mechanism is coalitionary punishment of aggressors.",
            "Female choice and group selection are rival mechanisms.",
            "The syndrome may be a developmental byproduct rather than selected.",
        ],
        requirements=[
            "A selection mechanism operating over the relevant time span.",
            "Consistency with the fossil sequence of facial reduction.",
            "Separation of selected traits from developmental byproducts.",
        ],
        standards=[
            "Anatomical claims checked against the fossil literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wrangham R. The Goodness Paradox. Pantheon; 2019.",
            "Hare B. Survival of the friendliest. Scientific American; 2017.",
        ],
        hypotheses=[
            "Coalitionary culling of aggressors drove the syndrome.",
            "Female mate choice for less aggressive males was primary.",
            "Group selection for cooperativeness did the work.",
            "The syndrome is a neural-crest byproduct, not a selected package.",
        ],
        confirm="Facial reduction tracks independent evidence of coalitionary punishment.",
        refute="Aggression levels show no decline across the relevant fossil sequence.",
    ),
    dict(
        key="anthropology-24",
        name="Are There True Cultural Universals",
        group="Culture and Society",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Do any cultural traits appear in literally every human society, and what "
                 "would genuine universals reveal about human nature?"),
        background=("Donald Brown catalogued hundreds of proposed universals - language, "
                    "marriage, incest taboos, music, dance, toolmaking, folklore. Critics "
                    "reply that apparent universals dissolve on inspection: what counts as "
                    "'marriage' or 'religion' varies so much that the universal is an artifact "
                    "of vague definition. The debate is partly about human nature and partly "
                    "about how anthropologists define their terms."),
        why_it_matters=("Universals are the closest anthropology gets to laws of human nature. "
                        "If none survive scrutiny, then culture may be far more plastic than "
                        "we assume."),
        sig_lens=("The Signature lens treats universals as a definition ledger: the Signature "
                  "approach separates traits universal by function from traits universal by "
                  "label."),
        sig_body=("The Signature proposal sorts universals into three bins. Assumptions: (1) "
                  "some problems confront every society (coordination, mating, mortality); (2) "
                  "solutions can differ while functions stay constant; (3) vague labels inflate "
                  "universality. Reasoning path: the proposal predicts functional universals "
                  "(every society has conflict-resolution procedures) should be robust while "
                  "formal universals (every society has courts) should dissolve - and finds "
                  "Brown's list splits exactly this way on re-examination. Genuine universals "
                  "are then functions, not forms. Limits: functional definitions risk becoming "
                  "so abstract they explain nothing."),
        pointer=('The Signature system sorts universals into functions (robust) versus forms (fragile), predicting only functional universals survive. The Signature test: re-examination with fixed definitions preserves functional universals only. It would be refuted if precisely defined formal universals hold across all societies.'),
        key_points=[
            "Brown catalogued hundreds of candidate universals.",
            "Critics argue vague definitions manufacture universality.",
            "Functional versus formal universals behave differently under scrutiny.",
            "The debate doubles as a debate about anthropological method.",
        ],
        requirements=[
            "Precise definitions applied uniformly across societies.",
            "Separation of functional from formal universality.",
            "Coverage of the full ethnographic range, not convenient cases.",
        ],
        standards=[
            "Claims checked against Brown's universals list and its critics.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Brown DE. Human Universals. McGraw-Hill; 1991.",
            "Antweiler C. Our Common Denominator. Berghahn; 2016.",
        ],
        hypotheses=[
            "Functional universals are real; formal ones are artifacts.",
            "True universals exist at the level of cognitive architecture.",
            "No substantive universals survive precise definition.",
            "Universals reflect shared ecology more than shared nature.",
        ],
        confirm="Re-examination with fixed definitions preserves functional universals only.",
        refute="Precisely defined formal universals hold across all societies.",
    ),
    dict(
        key="anthropology-25",
        name="The Units of Cultural Evolution",
        group="Culture and Society",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("What, if anything, plays the role of the gene in cultural evolution - memes, "
                 "practices, institutions - and can culture be modeled with Darwinian tools?"),
        background=("Dual-inheritance theory treats culture as a second inheritance system with "
                    "its own dynamics. But the units remain disputed: memes were criticized as "
                    "ill-defined, practices as too fuzzy, institutions as too large. Cultural "
                    "phylogenetics reconstructs language and tool trees successfully - yet "
                    "horizontal borrowing scrambles the trees. The field cannot agree what "
                    "evolves."),
        why_it_matters=("If culture evolves by Darwinian rules, we can model cultural change "
                        "the way biology models genetic change - predicting everything from "
                        "technology diffusion to ideological shifts."),
        sig_lens=("The Signature lens treats the unit question as a modeling ledger: the "
                  "Signature approach asks which unit size makes the math work."),
        sig_body=("The Signature proposal sidesteps the unit debate with a scale-free model. "
                  "Assumptions: (1) cultural transmission has measurable fidelity at many "
                  "scales; (2) selection operates on whatever is transmitted with fidelity; "
                  "(3) borrowing is itself a transmission mode. Reasoning path: the proposal "
                  "shows that Darwinian dynamics require only heritable variation in fitness - "
                  "not gene-like particles - so the fruitful question is which grains of "
                  "culture show heritable fitness differences, testable scale by scale. Memes, "
                  "practices, and institutions can all be units at their own grain. Limits: "
                  "measuring cultural fitness remains crude; the model risks vacuity if every "
                  "scale qualifies."),
        pointer=('The Signature system replaces the unit hunt with a scale-free test: whatever transmits with heritable fitness differences can evolve. The Signature test: heritable fitness differences are measurable at several cultural grains. It would be refuted if no cultural grain shows the fidelity selection requires.'),
        key_points=[
            "Dual-inheritance theory gives culture its own evolutionary dynamics.",
            "Memes, practices, and institutions all have defenders as the unit.",
            "Cultural phylogenetics works despite horizontal borrowing.",
            "The unit debate has stalled formal modeling.",
        ],
        requirements=[
            "A unit definition enabling quantitative models.",
            "An account of horizontal transmission within the framework.",
            "Testable fitness measures for cultural variants.",
        ],
        standards=[
            "Claims checked against the cultural-evolution literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Boyd R, Richerson PJ. Culture and the Evolutionary Process. University of Chicago Press; 1985.",
            "Mesoudi A. Cultural Evolution. University of Chicago Press; 2011.",
        ],
        hypotheses=[
            "Multiple grains of culture evolve simultaneously at different scales.",
            "Practices, not memes, are the operational units.",
            "Institutions are the units; smaller variants are noise.",
            "Cultural change is mostly non-Darwinian and needs different math.",
        ],
        confirm="Heritable fitness differences are measurable at several cultural grains.",
        refute="No cultural grain shows the fidelity selection requires.",
    ),
    dict(
        key="anthropology-26",
        name="The Demographic Transition Puzzle",
        group="Culture and Society",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("Why do birth rates fall - often below replacement - as societies get richer, "
                 "defying the expectation that wealth should buy more children?"),
        background=("The demographic transition describes mortality falling first, then "
                    "fertility, as societies develop. But evolutionary logic says resources "
                    "should convert to reproduction. Proposed explanations: the quantity-quality "
                    "tradeoff (investing heavily in few children), female education and "
                    "empowerment, the rising cost of children, cultural transmission of "
                    "low-fertility norms, and status competition. No account fully explains why "
                    "the fall so often overshoots to sub-replacement."),
        why_it_matters=("Sub-replacement fertility is reshaping nations - aging populations, "
                        "shrinking workforces, cultural anxiety. The puzzle is the most "
                        "consequential open question in demography."),
        sig_lens=("The Signature lens treats fertility as a status ledger: the Signature "
                  "approach asks what parents are really maximizing when they stop at one."),
        sig_body=("The Signature proposal models fertility as status-competition spending. "
                  "Assumptions: (1) in modern economies, children's adult status depends on "
                  "parental investment; (2) status is positional - relative, not absolute; "
                  "(3) norms transmit the locally successful family size. Reasoning path: the "
                  "proposal shows that when status competition intensifies, the optimal "
                  "strategy shifts from many children to heavy investment in few - and "
                  "cultural transmission then locks in sub-replacement norms even where "
                  "individuals would prefer larger families, explaining the overshoot. "
                  "Limits: the model struggles with high-fertility wealthy subgroups; "
                  "empowerment effects are partly independent of status logic."),
        pointer=('The Signature system models fertility as positional status spending, with cultural transmission locking in the overshoot. The Signature test: fertility tracks status-competition intensity independently of income. It would be refuted if fertility rebounds where status competition is fiercest.'),
        key_points=[
            "Wealth predicts fewer children - the opposite of naive evolutionary expectation.",
            "Many rich societies sit well below replacement fertility.",
            "Female education correlates strongly with fertility decline.",
            "Low-fertility norms spread culturally, even across borders.",
        ],
        requirements=[
            "An account of the sub-replacement overshoot.",
            "Consistency with high-fertility wealthy subgroups.",
            "Separation of empowerment, cost, and norm effects.",
        ],
        standards=[
            "Demographic claims checked against UN and World Bank data patterns.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Caldwell JC. Theory of Fertility Decline. Academic Press; 1982.",
            "Lesthaeghe R. The second demographic transition. Population and Development Review; 2010.",
        ],
        hypotheses=[
            "Positional status competition plus norm transmission drives the overshoot.",
            "Female empowerment and opportunity costs are the primary drivers.",
            "The quantity-quality tradeoff alone suffices.",
            "Cultural diffusion of small-family ideals leads; economics follows.",
        ],
        confirm="Fertility tracks status-competition intensity independently of income.",
        refute="Fertility rebounds where status competition is fiercest.",
    ),
    dict(
        key="anthropology-27",
        name="The Origins of Inequality",
        group="Culture and Society",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("When, why, and how did systematic material inequality emerge among humans, "
                 "and was it inevitable?"),
        background=("For most of human history, foragers were roughly egalitarian - with "
                    "leveling mechanisms like ridicule and ostracism. Inequality appears with "
                    "storage, agriculture, and states, but recent archaeology finds unequal "
                    "burials among pre-agricultural foragers too. Graeber and Wengrow argued "
                    "inequality was a political choice, not a destiny; others see it as an "
                    "emergent property of surplus and scale. The timeline keeps moving earlier."),
        why_it_matters=("Inequality defines modern politics. If it was chosen, it can be "
                        "unchosen; if it is emergent, it must be managed. The origin story "
                        "shapes the remedy."),
        sig_lens=("The Signature lens treats inequality as a surplus ledger: the Signature "
                  "approach tracks what stored surplus lets some do to others."),
        sig_body=("The Signature proposal models inequality as a storage ratchet. Assumptions: "
                  "(1) storable surplus can be defended and inherited; (2) defense favors "
                  "coalitions; (3) coalitions that win once can entrench advantage. "
                  "Reasoning path: the proposal shows that wherever surplus can be stored - "
                  "grain, herds, even prime fishing spots - temporary advantages compound "
                  "across generations unless leveling institutions actively reset them. "
                  "Egalitarian foragers are then not natural but maintained: their leveling "
                  "mechanisms are the achievement. Inequality emerges by default where storage "
                  "exists and leveling lapses. Limits: the model underplays ideological "
                  "justifications that stabilize hierarchy beyond material advantage."),
        pointer=('The Signature system models inequality as a storage ratchet, with egalitarianism as the maintained achievement rather than the default. The Signature test: inequality appears wherever storage exists without leveling institutions. It would be refuted if large storing societies maintain strict equality indefinitely.'),
        key_points=[
            "Foragers were roughly egalitarian, with active leveling mechanisms.",
            "Unequal burials now appear even among pre-agricultural foragers.",
            "Storage - grain, herds - correlates with emerging hierarchy.",
            "The choice-versus-emergence debate structures the field.",
        ],
        requirements=[
            "An account of pre-agricultural inequality signals.",
            "A mechanism linking storage to heritable advantage.",
            "An explanation for persistent egalitarian societies.",
        ],
        standards=[
            "Archaeological claims checked against the recent inequality literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Graeber D, Wengrow D. The Dawn of Everything. FSG; 2021.",
            "Boehm C. Hierarchy in the Forest. Harvard University Press; 1999.",
        ],
        hypotheses=[
            "Storable surplus creates a ratchet that compounds advantage by default.",
            "Inequality was repeatedly chosen and could be unchosen.",
            "Scale alone generates hierarchy regardless of surplus.",
            "Ideology, not material conditions, is the prime mover.",
        ],
        confirm="Inequality appears wherever storage exists without leveling institutions.",
        refute="Large storing societies maintain strict equality indefinitely.",
    ),
    dict(
        key="anthropology-28",
        name="The Sexual Division of Labor",
        group="Human Origins",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Why did a sexual division of labor - with men and women doing systematically "
                 "different economic work - become near-universal, and how deep are its roots?"),
        background=("Across foragers, hunting large game skews male and gathering skews female, "
                    "though the pattern is flexible and debated - recent work finds more female "
                    "hunters than assumed. Explanations invoke childcare constraints, strength "
                    "differences, risk tolerance, and the grandmother provisioning system. The "
                    "fossil record offers almost no direct evidence, leaving the deep history "
                    "speculative."),
        why_it_matters=("The division of labor underlies gender roles, family economics, and "
                        "modern debates about work and care. Its depth determines how much is "
                        "biology and how much is history."),
        sig_lens=("The Signature lens treats the division as a scheduling ledger: the "
                  "Signature approach asks which tasks fit around nursing infants."),
        sig_body=("The Signature proposal models the division as a compatibility optimization. "
                  "Assumptions: (1) nursing infants constrain mobility and risk for mothers; "
                  "(2) foraging tasks differ in interruptibility and danger; (3) households "
                  "maximize total returns. Reasoning path: the proposal shows the observed "
                  "pattern - women in interruptible, low-risk, near-camp tasks; men in "
                  "lumpy, high-risk, wide-ranging tasks - is what a household optimizer "
                  "produces given lactation constraints, without any assumptions about "
                  "preference or ideology. Flexibility follows naturally: where tasks are "
                  "compatible with childcare, women do them. Limits: the model cannot date "
                  "the pattern's origin; symbolic gender roles clearly exceed economics."),
        pointer=('The Signature system models the division as household scheduling optimization around lactation constraints. The Signature test: task assignment tracks childcare compatibility better than strength or ideology. It would be refuted if rigid divisions persist where no childcare constraint applies.'),
        key_points=[
            "A flexible but widespread division appears across forager societies.",
            "Recent archaeology finds more female hunters than classic accounts allowed.",
            "Childcare compatibility predicts task assignment well.",
            "The fossil record is nearly silent on the deep history.",
        ],
        requirements=[
            "An account of both the pattern and its flexibility.",
            "Consistency with female-hunter evidence.",
            "Separation of economic from ideological gender roles.",
        ],
        standards=[
            "Ethnographic claims checked against the primary literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Haas R et al. Female hunters of the early Americas. Science Advances; 2020.",
            "Gurven M, Hill K. Moving beyond the stereotype. Current Anthropology; 2009.",
        ],
        hypotheses=[
            "Lactation-constrained scheduling optimization produces the pattern.",
            "Strength and risk-tolerance differences are the primary drivers.",
            "The division is mostly ideological, projected backward onto prehistory.",
            "Grandmother provisioning systems shaped the original bargain.",
        ],
        confirm="Task assignment tracks childcare compatibility better than strength or ideology.",
        refute="Rigid divisions persist where no childcare constraint applies.",
    ),
    dict(
        key="anthropology-29",
        name="Why Symbolic Behavior Came So Late",
        group="Deep Time",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("If modern human anatomy is 300,000 years old, why did sustained symbolic "
                 "behavior - art, ornament, notation - wait until roughly the last 100,000 "
                 "years?"),
        background=("Jebel Irhoud fossils put Homo sapiens at about 300,000 years, but "
                    "Blombos ochre engravings date to about 75,000 and the Eurasian explosion "
                    "to about 45,000. The lag is the puzzle: were early moderns cognitively "
                    "different, demographically too thin to sustain traditions, or are we "
                    "missing the evidence? Each answer rewrites the relationship between "
                    "anatomy and mind."),
        why_it_matters=("The lag separates the evolution of the body from the evolution of the "
                        "mind - and the mind is what made us human."),
        sig_lens=("The Signature lens treats the lag as a retention problem: the Signature "
                  "approach asks what it takes for an invention to outlive its inventor."),
        sig_body=("The Signature proposal models the lag as a demographic retention threshold. "
                  "Assumptions: (1) symbolic innovations are invented regularly but lost "
                  "easily; (2) loss probability falls as teacher-learner chains lengthen; "
                  "(3) early sapiens populations were small and fragmented. Reasoning path: "
                  "the proposal computes that below a critical density of interacting bands, "
                  "even cognitively modern populations cannot sustain symbolic traditions - "
                  "producing a long apparent lag with no cognitive change required. Art "
                  "appears when networks, not brains, mature. Limits: the model needs "
                  "population densities the record cannot supply; some symbolic finds may "
                  "simply await discovery."),
        pointer=('The Signature system models the lag as demographic retention failure, with symbolism appearing when networks matured rather than brains. The Signature test: symbolic traditions appear wherever interaction density crosses the threshold. It would be refuted if dense, connected early populations leave no symbolic trace.'),
        key_points=[
            "Anatomy at 300,000 years; sustained symbolism only in the last 100,000.",
            "Blombos shows sparks at 75,000 years.",
            "Small fragmented populations lose innovations easily.",
            "Cognitive, demographic, and taphonomic explanations compete.",
        ],
        requirements=[
            "An account of the full 200,000-year lag.",
            "Consistency with the Blombos sparks.",
            "A mechanism linking demography to tradition survival.",
        ],
        standards=[
            "Fossil and archaeological dates checked against primary sources.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hublin JJ et al. New fossils from Jebel Irhoud. Nature; 2017.",
            "Powell A, Shennan S, Thomas MG. Late Pleistocene demography and the appearance of modern human behaviour. Science; 2009.",
        ],
        hypotheses=[
            "Demographic retention thresholds explain the lag without cognitive change.",
            "A late neural rewiring enabled symbolism.",
            "The evidence is lost; symbolism is as old as anatomy.",
            "Symbolism tracked cumulative culture, which needed time to compound.",
        ],
        confirm="Symbolic traditions appear wherever interaction density crosses the threshold.",
        refute="Dense, connected early populations leave no symbolic trace.",
    ),
    dict(
        key="anthropology-30",
        name="The Function of Prehistoric Art",
        group="Deep Time",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("Why did Paleolithic humans paint deep caves, carve figurines, and engrave "
                 "portable art - and what was the art for?"),
        background=("Lascaux, Chauvet, and hundreds of other sites preserve stunning animal "
                    "imagery in places no one lived. Theories: hunting magic, shamanic "
                    "visions, storytelling, information storage, costly signaling, pure "
                    "aesthetics. The art's placement - deep, dark, dangerous caves - and its "
                    "repetition of species suggest purpose, but every functional theory has "
                    "counterexamples, and the artists left no explanations."),
        why_it_matters=("Cave art is humanity's first great media. Understanding its function "
                        "is understanding the first information revolution."),
        sig_lens=("The Signature lens treats cave art as an information ledger: the Signature "
                  "approach asks what knowledge was worth painting in the dark."),
        sig_body=("The Signature proposal models cave painting as ecological knowledge "
                  "storage. Assumptions: (1) deep caves are costly to access, filtering for "
                  "serious purpose; (2) the painted species are disproportionately dangerous "
                  "or valuable prey; (3) images transmit information across generations. "
                  "Reasoning path: the proposal shows the species frequencies and seasonal "
                  "depictions match what a hunting society most needs to remember - animal "
                  "behavior, danger, timing - making caves the first hard drives: durable, "
                  "hidden, and reserved for high-value data. Ritual and aesthetics then layer "
                  "atop the storage function. Limits: abstract signs and hand stencils fit "
                  "awkwardly; the model cannot rule out primarily spiritual motives."),
        pointer=('The Signature system models cave art as durable ecological knowledge storage, with ritual layered atop the storage function. The Signature test: species and seasonal depictions match ecological information needs. It would be refuted if art concentrates on species with no economic or informational value.'),
        key_points=[
            "Major art sits in deep caves, far from living areas.",
            "Depicted species skew toward significant prey and predators.",
            "Abstract signs accompany the animal imagery.",
            "No functional theory covers all sites.",
        ],
        requirements=[
            "An account of the deep-cave placement.",
            "Consistency with species frequencies and abstract signs.",
            "A mechanism linking art to survival-relevant information.",
        ],
        standards=[
            "Site descriptions checked against the rock-art literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Clottes J. Chauvet Cave. University of Utah Press; 2003.",
            "Lewis-Williams D. The Mind in the Cave. Thames and Hudson; 2002.",
        ],
        hypotheses=[
            "Caves were durable knowledge stores for ecological information.",
            "Art served shamanic and visionary ritual purposes.",
            "Painting was hunting magic to ensure success.",
            "Art was costly signaling of group skill and cohesion.",
        ],
        confirm="Species and seasonal depictions match ecological information needs.",
        refute="Art concentrates on species with no economic or informational value.",
    ),
    dict(
        key="anthropology-31",
        name="Dreaming and Sleep: The Evolutionary Why",
        group="Human Origins",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("Why do humans sleep the way we do - less than other primates, with intense "
                 "dream-rich REM - and what is dreaming for?"),
        background=("Humans sleep less than any other primate (about 7 hours versus 10 to 12), "
                    "yet pack in more REM proportionally. Theories of sleep function - memory "
                    "consolidation, brain maintenance, energy saving - do not explain the "
                    "human pattern. Dream theories range from threat simulation (Revonsuo) to "
                    "emotional regulation to memory integration to spandrel. The short-sleep "
                    "pattern may relate to fire, ground sleeping, or social vigilance."),
        why_it_matters=("Sleep occupies a third of our lives and dreaming shapes our inner "
                        "world. An evolutionary account would transform sleep medicine and "
                        "psychology."),
        sig_lens=("The Signature lens treats sleep as a risk ledger: the Signature approach "
                  "asks what humans gained that was worth hours of vulnerability."),
        sig_body=("The Signature proposal models human sleep as a consolidated-risk bargain. "
                  "Assumptions: (1) ground sleeping and fire reduced predation risk; (2) social "
                  "groups provided vigilance; (3) REM-rich sleep pays cognitive dividends. "
                  "Reasoning path: the proposal shows that once fire and group living cut "
                  "nighttime risk, selection could compress sleep into a shorter, denser, "
                  "REM-rich block - trading hours for intensity and freeing time for social "
                  "and economic life. Dreaming is then the visible work of overnight "
                  "emotional and memory integration, intensified because the compressed "
                  "schedule demands it. Limits: the model needs ancestral sleep data we lack; "
                  "dream-content theories remain largely untestable."),
        pointer=('The Signature system models human sleep as a compressed, REM-dense bargain made possible by fire and social vigilance. The Signature test: short sleep correlates with fire use and group size across the record. It would be refuted if pre-fire hominins already show the modern compressed pattern.'),
        key_points=[
            "Humans sleep less than any other primate but with proportionally more REM.",
            "Sleep-function theories do not predict the human pattern.",
            "Dream theories range from threat simulation to spandrel.",
            "Fire, ground sleeping, and sociality may all have reshaped our nights.",
        ],
        requirements=[
            "An account of the short-sleep, high-REM combination.",
            "Consistency with primate sleep comparisons.",
            "A testable function for dreaming specifically.",
        ],
        standards=[
            "Sleep data checked against the comparative literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Nunn CL, Samson DR. Sleep in a comparative context. Evolutionary Anthropology; 2018.",
            "Revonsuo A. The reinterpretation of dreams. Behavioral and Brain Sciences; 2000.",
        ],
        hypotheses=[
            "Fire and sociality enabled compressed, REM-dense sleep.",
            "Dreaming simulates threats to rehearse responses.",
            "REM sleep integrates emotional memory; dreams are its exhaust.",
            "Human sleep patterns are mostly cultural, not evolved.",
        ],
        confirm="Short sleep correlates with fire use and group size across the record.",
        refute="Pre-fire hominins already show the modern compressed pattern.",
    ),
    dict(
        key="anthropology-32",
        name="Race: Biology and the Remaining Puzzles",
        group="Human Origins",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("What biological reality, if any, corresponds to human racial categories, and "
                 "which puzzles about human variation remain genuinely unsolved?"),
        background=("Genetics shows human variation is clinal - gradual across geography - with "
                    "more variation within African populations than between continents. Folk "
                    "racial categories map poorly onto genetic clusters. Yet puzzles remain: "
                    "why skin color varies so lawfully with UV, why some disease risks cluster "
                    "by ancestry, how to do ancestry-aware medicine without reifying race, and "
                    "why folk categories persist despite the genetic evidence. This is a "
                    "scholarly problem in biology and society, handled here with care."),
        why_it_matters=("Race shapes medicine, law, and daily life. Getting the biology right - "
                        "neither denying real ancestry-correlated variation nor validating folk "
                        "categories - is a scientific and civic necessity."),
        sig_lens=("The Signature lens treats the puzzle as a mapping problem: the Signature "
                  "approach separates lawful clinal variation from categorical illusion."),
        sig_body=("The Signature proposal models human variation as clines plus thresholds. "
                  "Assumptions: (1) most traits vary gradually with geography and selection "
                  "(UV, diet, pathogens); (2) humans categorize continuously varying input "
                  "into discrete boxes; (3) medicine needs ancestry information without folk "
                  "categories. Reasoning path: the proposal shows the genuine puzzles - skin "
                  "color clines, ancestry-correlated disease risk, pharmacogenomic differences - "
                  "are all predicted by local adaptation plus drift, while folk races are "
                  "predicted by the psychology of categorization applied to visible clines. "
                  "Both can be true: real biological variation exists, and folk categories "
                  "misdescribe it. Limits: the model does not dissolve the social reality of "
                  "race, which operates independently of biology."),
        pointer=('The Signature system separates lawful clinal variation from the psychology of categorization that manufactures discrete races. The Signature test: medical ancestry effects resolve into specific clinal variants, not races. It would be refuted if discrete genetic clusters match folk categories across the genome.'),
        key_points=[
            "Human genetic variation is largely clinal, not categorical.",
            "Folk racial categories map poorly onto genetic structure.",
            "Skin color, disease risk, and drug response do vary lawfully by ancestry.",
            "The social reality of race operates independently of the biology.",
        ],
        requirements=[
            "Consistency with clinal genetic data.",
            "An account of lawful ancestry-correlated medical variation.",
            "Separation of biological from social claims.",
        ],
        standards=[
            "Genetic claims checked against the human-variation literature.",
            "Scholarly framing only; no ideological content. Open status confirmed as of 2026.",
        ],
        citations=[
            "Lewontin RC. The apportionment of human diversity. Evolutionary Biology; 1972.",
            "Jablonski NG, Chaplin G. The evolution of human skin coloration. Journal of Human Evolution; 2000.",
        ],
        hypotheses=[
            "Clines plus categorization psychology explain the full pattern.",
            "Genetic clusters validate a revised biological race concept.",
            "Ancestry-informative medicine can proceed without race concepts.",
            "Folk categories track real adaptive packages, crudely but usefully.",
        ],
        confirm="Medical ancestry effects resolve into specific clinal variants, not races.",
        refute="Discrete genetic clusters match folk categories across the genome.",
    ),
    dict(
        key="anthropology-33",
        name="The Gender Divergence in Prehistory",
        group="Culture and Society",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("When and why did gendered social roles - beyond the economic division of "
                 "labor - diverge so sharply, and how much reflects biology versus history?"),
        background=("Burials, art, and grave goods show gendered symbolism deep in prehistory, "
                    "but its intensity varies: some societies buried women as warriors and "
                    "leaders, others sharply separated spheres. Patriarchy's origins are "
                    "contested - plow agriculture (Alesina), warfare, pastoralism, and state "
                    "formation all have defenders. Ancient DNA now reveals patrilocality and "
                    "male reproductive skew in some prehistoric groups, complicating every "
                    "simple story."),
        why_it_matters=("Gender structures power in every society. Its prehistoric roots set "
                        "the baseline for debates about equality, family, and work today."),
        sig_lens=("The Signature lens treats gender divergence as an inheritance ledger: the "
                  "Signature approach asks what changed when wealth could be passed down."),
        sig_body=("The Signature proposal models intensified gender hierarchy as an "
                  "inheritance effect. Assumptions: (1) heritable wealth (land, herds) creates "
                  "stakes in paternity certainty; (2) patrilineal inheritance concentrates "
                  "those stakes on male lines; (3) control of female reproduction becomes "
                  "economically rational for heirs. Reasoning path: the proposal shows gender "
                  "hierarchy should intensify exactly where wealth becomes heritable and "
                  "defensible - predicting the plow, pastoralism, and state-formation "
                  "correlations without requiring any claim about innate capacity. Where "
                  "wealth stayed mobile or communal, hierarchy stayed shallow. Limits: the "
                  "model handles material hierarchy better than symbolic gender systems, which "
                  "have lives of their own."),
        pointer=('The Signature system models gender hierarchy as intensifying where heritable wealth created stakes in paternity certainty. The Signature test: hierarchy intensifies at heritable-wealth transitions across regions. It would be refuted if sharp gender hierarchy appears with no heritable wealth and no warfare.'),
        key_points=[
            "Gendered symbolism is ancient but variable in intensity.",
            "Plow agriculture, pastoralism, and states correlate with patriarchy.",
            "Ancient DNA reveals patrilocality in some prehistoric groups.",
            "Economic and symbolic gender systems partly diverge.",
        ],
        requirements=[
            "An account of variability, not just the patriarchal cases.",
            "Consistency with ancient-DNA residence patterns.",
            "Separation of economic from symbolic gender systems.",
        ],
        standards=[
            "Claims checked against the gender-archaeology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Alesina A, Giuliano P, Nunn N. On the origins of gender roles. Quarterly Journal of Economics; 2013.",
            "Lerner G. The Creation of Patriarchy. Oxford University Press; 1986.",
        ],
        hypotheses=[
            "Heritable wealth created the stakes that intensified gender hierarchy.",
            "Warfare and male coalitions drove the divergence.",
            "Plow agriculture specifically reshaped gender roles.",
            "Symbolic gender systems have autonomous cultural histories.",
        ],
        confirm="Hierarchy intensifies at heritable-wealth transitions across regions.",
        refute="Sharp gender hierarchy appears with no heritable wealth and no warfare.",
    ),
    dict(
        key="anthropology-34",
        name="What Makes Humans Unique: The Synthesis",
        group="Language and Mind",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("After a century of proposed human uniquenesses - language, tools, culture, "
                 "morality, teaching, fire - each found in partial form in other species, what "
                 "if anything is genuinely unique about humans?"),
        background=("Every classic candidate has fallen: apes make tools, corvids plan, "
                    "cetaceans have culture, ants farm. Remaining contenders include "
                    "cumulative culture (the ratchet), recursive language, shared "
                    "intentionality, and the combination itself. Some argue uniqueness is "
                    "quantitative - we do what others do, but more - while others seek the "
                    "qualitative spark. The synthesis remains unwritten."),
        why_it_matters=("This is anthropology's capstone question: the answer defines the "
                        "species, grounds human dignity debates, and sets expectations for "
                        "animal minds and artificial ones."),
        sig_lens=("The Signature lens treats uniqueness as a combination lock: the Signature "
                  "approach asks which set of ordinary traits, combined, opens a door no "
                  "single trait can."),
        sig_body=("The Signature proposal locates uniqueness in the ratchet-plus-teaching "
                  "combination. Assumptions: (1) many species have culture, tools, and "
                  "communication; (2) only humans combine high-fidelity teaching with "
                  "cumulative retention across generations; (3) the combination compounds. "
                  "Reasoning path: the proposal shows that teaching fidelity times retention "
                  "fidelity determines whether innovations accumulate - and only the human "
                  "combination pushes the product above the ratchet threshold. Uniqueness is "
                  "then not a trait but a threshold crossing: we are the species whose "
                  "transmission system compounds. Limits: the threshold is hard to quantify; "
                  "the account explains capability, not why the combination evolved only "
                  "once."),
        pointer=('The Signature system locates uniqueness in a threshold crossing: teaching fidelity times retention fidelity pushing culture above the ratchet point. The Signature test: ratchet thresholds are quantified and only humans cross them. It would be refuted if a nonhuman species demonstrates open-ended cumulative culture.'),
        key_points=[
            "Every classic uniqueness candidate has partial animal parallels.",
            "Cumulative culture - the ratchet - is the strongest remaining contender.",
            "Shared intentionality and recursive language are rival candidates.",
            "Quantitative versus qualitative uniqueness remains unresolved.",
        ],
        requirements=[
            "An account surviving the animal-cognition counterexamples.",
            "A mechanism, not just a label, for the proposed uniqueness.",
            "Consistency with the gradual fossil and archaeological record.",
        ],
        standards=[
            "Claims checked against the comparative-cognition literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Tomasello M. The Cultural Origins of Human Cognition. Harvard University Press; 1999.",
            "Henrich J. The Secret of Our Success. Princeton University Press; 2015.",
        ],
        hypotheses=[
            "The teaching-times-retention ratchet is the genuine uniqueness.",
            "Recursive language alone marks the qualitative break.",
            "Shared intentionality is the foundation everything else builds on.",
            "There is no qualitative break - only quantitative compounding.",
        ],
        confirm="Ratchet thresholds are quantified and only humans cross them.",
        refute="A nonhuman species demonstrates open-ended cumulative culture.",
    ),
]
