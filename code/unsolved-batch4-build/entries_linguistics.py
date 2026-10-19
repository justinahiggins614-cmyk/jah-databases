#!/usr/bin/env python3
"""Entries for the Unsolved Linguistics databases (batch 4).

34 famous open problems in linguistics, ladder-ordered by accessibility.
ID prefixes: JAH-USLN- (public) and JAH-USLNS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="linguistics-01",
        name="The Origin of Language",
        group="Origins",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("How did language - open-ended, grammatical, symbolic communication - "
                 "first evolve, and why only in our lineage?"),
        background=("Language leaves no fossils, so the field works from indirect "
                    "evidence: primate calls, child acquisition, creoles, genetics "
                    "(FOXP2), and archaeology. Rival accounts invoke social bonding, "
                    "teaching, gossip, toolmaking instruction, or thought itself. The "
                    "1866 ban by the Paris Linguistic Society on origin speculation "
                    "lasted a century; the modern field is bolder but no closer to "
                    "consensus."),
        why_it_matters=("Language is the infrastructure of human thought and society. "
                        "Its origin is the deepest puzzle in the human sciences."),
        sig_lens=("The Signature lens treats language as a bottleneck technology: the "
                  "Signature approach asks what information problem made grammar "
                  "worth its cost."),
        sig_body=("The Signature proposal models language as evolving to transmit "
                  "unobservable knowledge. Assumptions: (1) hominin survival "
                  "increasingly depended on know-how that cannot be seen (tracking, "
                  "tool properties, social obligations); (2) demonstration fails for "
                  "the unobservable; (3) symbols compress teaching. Reasoning path: "
                  "the proposal shows the selection pressure for language scales "
                  "with the fraction of survival-relevant knowledge that is "
                  "unobservable - predicting language should emerge with cumulative "
                  "technical culture, not with brain size alone. Limits: the model "
                  "cannot date the emergence; social-bonding accounts make rival "
                  "predictions."),
        pointer=('The Signature system models language as evolving to transmit unobservable knowledge, predicting emergence with cumulative culture. The Signature test: grammatical complexity tracks cumulative culture independently of brain size. It would be refuted if full language predates cumulative culture in the record.'),
        key_points=[
            "Language leaves no direct fossils; evidence is entirely indirect.",
            "Rival pressures: bonding, teaching, gossip, thought.",
            "FOXP2 and anatomy give hints, not answers.",
            "No account commands consensus after 150 years of debate.",
        ],
        requirements=[
            "A selection pressure strong enough to fund the neural cost.",
            "Consistency with primate communication baselines.",
            "A bridge from call systems to full grammar.",
        ],
        standards=[
            "Claims checked against the language-evolution literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fitch WT. The Evolution of Language. Cambridge University Press; 2010.",
            "Christiansen MH, Kirby S. Language Evolution. Oxford University Press; 2003.",
        ],
        hypotheses=[
            "Teaching unobservable know-how drove the evolution.",
            "Social bonding and gossip came first.",
            "Gesture provided the first symbols; speech followed.",
            "Language began as internal thought, externalized later.",
        ],
        confirm="Grammatical complexity tracks cumulative culture independently of brain size.",
        refute="Full language predates cumulative culture in the record.",
    ),
    dict(
        key="linguistics-02",
        name="Gesture First or Voice First",
        group="Origins",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Did the first symbolic communication use the hands or the voice - "
                 "and why did speech win?"),
        background=("Apes gesture flexibly but vocalize inflexibly, suggesting "
                    "gesture-first (Corballis). But speech is hands-free, works in "
                    "the dark, and carries further - and the vocal anatomy for "
                    "speech evolved gradually. Mirror-neuron research briefly "
                    "favored gesture, then faded. The debate now centers on whether "
                    "the first symbols were manual, vocal, or multimodal from the "
                    "start."),
        why_it_matters=("The answer determines what the first language looked like - "
                        "and whether sign languages are a window into our linguistic "
                        "past."),
        sig_lens=("The Signature lens treats the question as a channel ledger: the "
                  "Signature approach asks which channel carried the first "
                  "symbols under Pleistocene constraints."),
        sig_body=("The Signature proposal models a multimodal origin with vocal "
                  "takeover. Assumptions: (1) early symbols used whatever channel "
                  "was available; (2) hands were increasingly occupied by tools "
                  "and carrying; (3) vocal control improved gradually. Reasoning "
                  "path: the proposal shows gesture-first and voice-first are both "
                  "half right - symbols likely began multimodally, and speech won "
                  "as hands became busy and vocal control improved. The prediction: "
                  "the earliest symbolic systems should show manual-vocal "
                  "redundancy, like modern co-speech gesture. Limits: the model "
                  "cannot be tested against direct evidence; it predicts a "
                  "pattern, not a date."),
        pointer=('The Signature system models a multimodal origin with vocal takeover as hands became occupied by tools. The Signature test: early symbolic behavior shows manual-vocal redundancy. It would be refuted if full grammar appears in one channel with no trace of the other.'),
        key_points=[
            "Apes gesture flexibly, vocalize inflexibly.",
            "Speech is hands-free and works in darkness.",
            "Mirror-neuron evidence for gesture-first has weakened.",
            "Modern co-speech gesture shows the multimodal baseline.",
        ],
        requirements=[
            "An account of why speech eventually dominated.",
            "Consistency with ape communication baselines.",
            "A role for sign languages in the story.",
        ],
        standards=[
            "Claims checked against the evolutionary-linguistics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Corballis MC. From Hand to Mouth. Princeton University Press; 2002.",
            "Tomasello M. Origins of Human Communication. MIT Press; 2008.",
        ],
        hypotheses=[
            "Multimodal symbols first; speech won as hands got busy.",
            "Gesture was the first true symbolic system.",
            "Vocal symbols came first; gesture is secondary.",
            "The distinction is meaningless; communication was always multimodal.",
        ],
        confirm="Early symbolic behavior shows manual-vocal redundancy.",
        refute="Full grammar appears in one channel with no trace of the other.",
    ),
    dict(
        key="linguistics-03",
        name="The Evolution of Syntax",
        group="Origins",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("How did syntax - hierarchical, recursive sentence structure - evolve "
                 "from simpler communication systems?"),
        background=("Animal call systems lack hierarchical syntax; human languages "
                    "all have it. Theories: gradual elaboration from protolanguage "
                    "(Bickerton), sudden emergence via a single mutation (Chomsky's "
                    "Minimalist Program), cultural evolution shaping learnable "
                    "structures (Kirby), or syntax as a byproduct of thought, not "
                    "communication. The Piraha debate over recursion made the "
                    "question empirical - and hotter."),
        why_it_matters=("Syntax is the engine of human thought's expressiveness. Its "
                        "evolution is the evolution of the mind's operating system."),
        sig_lens=("The Signature lens treats syntax as a compression ledger: the "
                  "Signature approach asks what message complexity forced "
                  "hierarchy."),
        sig_body=("The Signature proposal models syntax as evolving under message "
                  "complexity pressure. Assumptions: (1) early symbols named "
                  "things; (2) survival-relevant messages grew complex (who did "
                  "what to whom, when); (3) flat sequences become ambiguous past a "
                  "complexity threshold. Reasoning path: the proposal shows "
                  "hierarchical structure is the cheapest solution to the "
                  "ambiguity problem - predicting syntax should elaborate exactly "
                  "where messages carry multiple participants and relations, which "
                  "matches the archaeological signal of growing social-technical "
                  "complexity. Limits: the model handles communication-driven "
                  "syntax; thought-first accounts remain rivals."),
        pointer=('The Signature system models syntax as the cheapest solution to message ambiguity past a complexity threshold. The Signature test: syntactic elaboration tracks message-complexity demands. It would be refuted if full syntax appears before any complex messaging need.'),
        key_points=[
            "All human languages have hierarchical syntax; no animal system does.",
            "Gradual, sudden, cultural, and thought-first accounts compete.",
            "The Piraha recursion debate made the question empirical.",
            "Message complexity is the leading functional pressure.",
        ],
        requirements=[
            "A bridge from flat sequences to hierarchy.",
            "An account of recursion specifically.",
            "Consistency with creole and acquisition data.",
        ],
        standards=[
            "Claims checked against the syntax-evolution literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bickerton D. Language and Species. University of Chicago Press; 1990.",
            "Kirby S. Syntax without natural selection. 2017.",
        ],
        hypotheses=[
            "Message-complexity pressure selected for hierarchy.",
            "A single cognitive leap created recursive syntax.",
            "Cultural evolution shaped syntax for learnability.",
            "Syntax is thought externalized, not communication optimized.",
        ],
        confirm="Syntactic elaboration tracks message-complexity demands.",
        refute="Full syntax appears before any complex messaging need.",
    ),
    dict(
        key="linguistics-04",
        name="Why Do Languages Change",
        group="Change",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Why do languages change constantly - sounds shifting, meanings "
                 "drifting, grammars eroding - even without outside contact?"),
        background=("The Great Vowel Shift remade English pronunciation; Latin "
                    "became French, Spanish, Italian. Change is universal and "
                    "ceaseless, yet its motor is debated: articulatory laziness, "
                    "childhood mislearning, social identity marking, frequency "
                    "effects, or random drift amplified by networks. Weinreich, "
                    "Labov, and Herzog framed the constraints - the actuation, "
                    "transition, embedding, and evaluation problems - but the "
                    "engine room remains disputed."),
        why_it_matters=("Language change is the clock of linguistic history and the "
                        "laboratory of cultural evolution. Its mechanism is the "
                        "mechanism of all cultural change."),
        sig_lens=("The Signature lens treats change as a transmission ledger: the "
                  "Signature approach asks what survives the journey from mouth "
                  "to ear to child."),
        sig_body=("The Signature proposal models change as imperfect replication "
                  "plus social selection. Assumptions: (1) every utterance is "
                  "copied with noise; (2) learners regularize the noise; (3) "
                  "social identity rewards some variants. Reasoning path: the "
                  "proposal shows that even tiny per-generation biases compound "
                  "into systematic change - the same math as genetic drift with "
                  "selection - predicting that high-frequency words should change "
                  "slowest (more replication, less drift), which matches the "
                  "data. Social meaning then steers which variants win. Limits: "
                  "the model explains gradual change better than sudden "
                  "restructurings."),
        pointer=('The Signature system models change as noisy replication plus social selection, predicting high-frequency words change slowest. The Signature test: change rates track replication noise and social-selection measures. It would be refuted if change occurs with zero transmission noise in controlled settings.'),
        key_points=[
            "All languages change constantly, even in isolation.",
            "The Great Vowel Shift and Latin-to-Romance are classic cases.",
            "Weinreich, Labov, and Herzog framed the core problems.",
            "High-frequency words resist change - a key datum.",
        ],
        requirements=[
            "A mechanism operating without external contact.",
            "An account of the frequency effect.",
            "Separation of actuation from spread.",
        ],
        standards=[
            "Claims checked against the historical-linguistics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weinreich U, Labov W, Herzog MI. Empirical foundations for a theory of language change. 1968.",
            "Labov W. Principles of Linguistic Change. Blackwell; 1994.",
        ],
        hypotheses=[
            "Noisy replication plus social selection drives change.",
            "Childhood mislearning is the primary engine.",
            "Articulatory economy drives sound change.",
            "Social identity marking drives most change.",
        ],
        confirm="Change rates track replication noise and social-selection measures.",
        refute="Change occurs with zero transmission noise in controlled settings.",
    ),
    dict(
        key="linguistics-05",
        name="The Actuation Problem",
        group="Change",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("Why does a particular language change begin exactly when and where "
                 "it does - the actuation problem?"),
        background=("We can describe how changes spread once started, but not why a "
                    "given vowel starts shifting in one city in one decade. "
                    "Weinreich, Labov, and Herzog named it the deepest problem in "
                    "historical linguistics. Candidate triggers: contact, social "
                    "upheaval, prestige shifts, random fluctuation crossing a "
                    "threshold - but prediction remains impossible, and identical "
                    "conditions produce change in one place and stability in "
                    "another."),
        why_it_matters=("Actuation is the origin of every language change. Solving it "
                        "would make linguistic history predictive rather than "
                        "retrospective."),
        sig_lens=("The Signature lens treats actuation as a threshold ledger: the "
                  "Signature approach asks what tips a stable system into "
                  "motion."),
        sig_body=("The Signature proposal models actuation as a critical-mass "
                  "phenomenon. Assumptions: (1) variant pronunciations always "
                  "exist as low-level noise; (2) social networks amplify or damp "
                  "variants; (3) prestige and identity weight the amplification. "
                  "Reasoning path: the proposal shows stable systems sit in "
                  "equilibrium until network structure or prestige weights shift "
                  "past a tipping point - predicting actuation should follow "
                  "social-network disruptions (migration, new media, prestige "
                  "reversals) more than linguistic conditions. The 'why here, why "
                  "now' becomes a network question. Limits: tipping points are "
                  "easier to invoke than to measure prospectively."),
        pointer=('The Signature system models actuation as a network tipping point, predicting change follows social disruption rather than linguistic conditions. The Signature test: changes actuate after measurable network disruptions. It would be refuted if actuation occurs with no network or prestige change.'),
        key_points=[
            "Spread is describable; actuation is not predictable.",
            "Identical conditions yield change in one place, stability in another.",
            "Named by Weinreich, Labov, and Herzog as the deepest problem.",
            "Candidate triggers all have counterexamples.",
        ],
        requirements=[
            "A predictive account of when and where change starts.",
            "Separation of linguistic from social triggers.",
            "Testability against stable counterexamples.",
        ],
        standards=[
            "Claims checked against the sociolinguistics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weinreich U, Labov W, Herzog MI. Empirical foundations for a theory of language change. 1968.",
            "Milroy J, Milroy L. Linguistic change, social network and speaker innovation. 1985.",
        ],
        hypotheses=[
            "Network tipping points trigger actuation.",
            "Contact is the universal trigger.",
            "Prestige reversals actuate most changes.",
            "Actuation is fundamentally stochastic and unpredictable.",
        ],
        confirm="Changes actuate after measurable network disruptions.",
        refute="Actuation occurs with no network or prestige change.",
    ),
    dict(
        key="linguistics-06",
        name="Why Do Languages Diversify",
        group="Change",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Why did one or a few original languages splinter into 7,000 "
                 "mutually unintelligible tongues instead of staying one?"),
        background=("Latin alone became dozens of Romance languages; the world's "
                    "7,000 languages cluster in families from common ancestors. "
                    "Diversification follows isolation plus change, but the rate "
                    "varies wildly - New Guinea packs 800 languages into one "
                    "island while vast steppes share few. Ecology, social "
                    "structure, identity marking, and chance all shape the "
                    "outcome, but no model predicts diversification rates."),
        why_it_matters=("Diversification is why humanity does not share one tongue. "
                        "Its logic is the logic of cultural speciation itself."),
        sig_lens=("The Signature lens treats diversification as a speciation "
                  "ledger: the Signature approach asks what isolates speech "
                  "communities the way mountains isolate finches."),
        sig_body=("The Signature proposal models diversification as identity-driven "
                  "speciation. Assumptions: (1) linguistic difference marks group "
                  "identity; (2) identity marking intensifies under competition; "
                  "(3) isolation reduces the cost of divergence. Reasoning path: "
                  "the proposal shows diversification rate should track social "
                  "fragmentation times identity competition - predicting New "
                  "Guinea's density (fragmented, competitive) and the steppes' "
                  "uniformity (mobile, integrated). Languages speciate like "
                  "organisms where identity is the selection pressure. Limits: "
                  "the model needs independent measures of prehistoric social "
                  "fragmentation."),
        pointer=('The Signature system models diversification as identity-driven speciation, predicting rates from social fragmentation. The Signature test: diversification rates track social fragmentation measures. It would be refuted if high-fragmentation regions show low diversification.'),
        key_points=[
            "About 7,000 languages from far fewer ancestors.",
            "New Guinea: 800 languages on one island; steppes: few across continents.",
            "Isolation plus change is necessary but not predictive.",
            "Identity marking is the leading social accelerator.",
        ],
        requirements=[
            "A predictive model of diversification rates.",
            "An account of the New Guinea versus steppe contrast.",
            "Separation of ecological from social drivers.",
        ],
        standards=[
            "Claims checked against the linguistic-diversity literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Nettle D. Linguistic Diversity. Oxford University Press; 1999.",
            "Nichols J. Linguistic Diversity in Space and Time. University of Chicago Press; 1992.",
        ],
        hypotheses=[
            "Identity competition drives diversification rates.",
            "Ecological risk and isolation are the primary drivers.",
            "Diversification is mostly random drift over time.",
            "Social network structure predicts divergence.",
        ],
        confirm="Diversification rates track social fragmentation measures.",
        refute="High-fragmentation regions show low diversification.",
    ),
    dict(
        key="linguistics-07",
        name="How Do Children Learn Language So Fast",
        group="Acquisition",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("How do children master the full complexity of grammar by age four "
                 "from limited, messy input - the poverty of the stimulus?"),
        background=("Children hear fragments, false starts, and baby talk, yet "
                    "extract hierarchical grammar, avoid countless plausible "
                    "errors, and do it on every continent. Nativists invoke "
                    "built-in Universal Grammar; usage-based theorists invoke "
                    "powerful statistical learning plus social cognition; "
                    "recent work shows input is richer than assumed (child-"
                    "directed speech is structured). The stimulus may be less "
                    "poor than advertised - but the learning feat remains "
                    "astonishing."),
        why_it_matters=("Acquisition is the existence proof that grammar is "
                        "learnable. Its mechanism decides the nativism debate - "
                        "and informs every theory of learning."),
        sig_lens=("The Signature lens treats acquisition as a data-efficiency "
                  "ledger: the Signature approach asks what prior makes the "
                  "input sufficient."),
        sig_body=("The Signature proposal models acquisition as Bayesian inference "
                  "with strong social priors. Assumptions: (1) children bring "
                  "powerful intention-reading and pattern-finding; (2) "
                  "child-directed speech is statistically structured; (3) "
                  "learners prefer simpler grammars consistent with data. "
                  "Reasoning path: the proposal shows that intention-reading "
                  "plus statistical learning can close most of the poverty gap "
                  "without language-specific innate grammar - predicting that "
                  "acquisition difficulty should track input structure quality, "
                  "which matches variation across cultures. A thin innate bias "
                  "toward hierarchical patterns may remain. Limits: the model "
                  "struggles with the uniformity of acquisition despite wildly "
                  "varying input."),
        pointer=('The Signature system models acquisition as Bayesian inference with social priors, predicting difficulty tracks input structure. The Signature test: acquisition difficulty tracks input-structure measures. It would be refuted if children acquire structures absent from any input.'),
        key_points=[
            "Full grammar by age four from messy, fragmentary input.",
            "Nativist versus usage-based accounts remain deadlocked.",
            "Child-directed speech is more structured than assumed.",
            "Acquisition is strikingly uniform across cultures.",
        ],
        requirements=[
            "An account of the poverty-of-the-stimulus gap.",
            "Consistency with cross-cultural uniformity.",
            "Testable predictions about input effects.",
        ],
        standards=[
            "Claims checked against the acquisition literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Chomsky N. Aspects of the Theory of Syntax. MIT Press; 1965.",
            "Tomasello M. Constructing a Language. Harvard University Press; 2003.",
        ],
        hypotheses=[
            "Social cognition plus statistics closes the gap.",
            "Innate Universal Grammar guides learning.",
            "Input is richer than nativists admit.",
            "A thin hierarchical bias plus learning suffices.",
        ],
        confirm="Acquisition difficulty tracks input-structure measures.",
        refute="Children acquire structures absent from any input.",
    ),
    dict(
        key="linguistics-08",
        name="Is There a Critical Period",
        group="Acquisition",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Is there a biologically fixed window for language acquisition - "
                 "and what exactly closes when it shuts?"),
        background=("Feral-child cases (Genie) and late first-language learners "
                    "(Nicaraguan Sign Language cohorts) show profound deficits "
                    "after delayed exposure. Second-language phonology clearly "
                    "declines with age of arrival. But the boundaries are fuzzy: "
                    "adults learn vocabulary fine, late learners achieve "
                    "functional fluency, and the neural mechanisms (pruning? "
                    "lateralization? entrenchment?) are disputed. How critical is "
                    "the period, and for which subsystems?"),
        why_it_matters=("The answer shapes deaf education, immigration policy, and "
                        "theories of brain plasticity - and reveals how the brain "
                        "budgets its learning."),
        sig_lens=("The Signature lens treats the period as a plasticity ledger: "
                  "the Signature approach asks what the brain trades away when "
                  "it commits."),
        sig_body=("The Signature proposal models the critical period as neural "
                  "commitment, not decay. Assumptions: (1) the brain overproduces "
                  "synapses then prunes by use; (2) first-language patterns get "
                  "entrenched through massive early use; (3) entrenchment aids "
                  "fluency but blocks reorganization. Reasoning path: the proposal "
                  "shows phonology - the most practiced subsystem - should "
                  "entrench hardest, predicting the observed hierarchy (phonology "
                  "most age-sensitive, vocabulary least). The 'period' is then "
                  "the cost of expertise, not a timer. Limits: the model needs "
                  "neural measures of entrenchment; feral cases confound "
                  "deprivation with delay."),
        pointer=('The Signature system models the critical period as the cost of neural entrenchment, predicting phonology is most age-sensitive. The Signature test: entrenchment measures predict age effects by subsystem. It would be refuted if age effects appear without any prior entrenchment.'),
        key_points=[
            "Delayed first-language exposure causes profound deficits.",
            "L2 phonology declines with age of arrival.",
            "Vocabulary remains learnable throughout life.",
            "The neural mechanism is disputed.",
        ],
        requirements=[
            "An account of the subsystem hierarchy (phonology > syntax > vocabulary).",
            "Separation of delay effects from deprivation effects.",
            "A neural mechanism, not just a behavioral window.",
        ],
        standards=[
            "Claims checked against the critical-period literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Lenneberg EH. Biological Foundations of Language. Wiley; 1967.",
            "Johnson JS, Newport EL. Critical period effects in second language learning. Cognitive Psychology; 1989.",
        ],
        hypotheses=[
            "Entrenchment through use closes plasticity subsystem by subsystem.",
            "A maturational timer shuts language learning down.",
            "First-language interference, not lost plasticity, explains L2 limits.",
            "The period is social-cognitive, not neural.",
        ],
        confirm="Entrenchment measures predict age effects by subsystem.",
        refute="Age effects appear without any prior entrenchment.",
    ),
    dict(
        key="linguistics-09",
        name="The Piraha Recursion Debate",
        group="Theory",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("Does the Piraha language of the Amazon lack recursion - and if so, "
                 "does that falsify the claim that recursion is the core of "
                 "human language?"),
        background=("Daniel Everett reported that Piraha lacks embedded clauses, "
                    "numerals, and color terms, constrained by an 'immediacy of "
                    "experience' principle. Chomsky's camp replied that recursion "
                    "is a capacity of the mind, not a requirement of every "
                    "language - and disputed the data. The debate became linguistics' "
                    "most public brawl, touching fieldwork ethics, the nature of "
                    "evidence, and whether Universal Grammar survives a "
                    "counterexample."),
        why_it_matters=("If recursion is not universal, the Minimalist Program's "
                        "core claim falls - and with it the dominant theory of "
                        "what language is."),
        sig_lens=("The Signature lens treats the debate as an evidence ledger: "
                  "the Signature approach asks what would count as proof on "
                  "either side."),
        sig_body=("The Signature proposal reframes the debate as a capacity-versus-"
                  "use distinction. Assumptions: (1) a mental capacity can exist "
                  "unused, like perfect pitch in non-musicians; (2) cultural "
                  "constraints can suppress structures; (3) fieldwork data are "
                  "theory-laden. Reasoning path: the proposal shows both camps "
                  "can be right - Piraha speakers possess recursive cognition "
                  "(needed for their kinship and river navigation) while the "
                  "language conventionally avoids embedding. The empirical test "
                  "becomes non-linguistic recursion tasks, not sentence "
                  "judgments. Limits: the distinction risks making Universal "
                  "Grammar unfalsifiable; the field data remain contested."),
        pointer=('The Signature system reframes the debate as capacity versus use, testable through non-linguistic recursion tasks. The Signature test: piraha speakers show recursive cognition in non-linguistic tasks. It would be refuted if no recursive cognition appears in any domain.'),
        key_points=[
            "Everett reported no clausal embedding in Piraha.",
            "Chomskyans replied recursion is mental capacity, not surface requirement.",
            "The debate spans data, theory, and fieldwork ethics.",
            "No resolution has emerged after two decades.",
        ],
        requirements=[
            "Agreement on what counts as evidence for recursion.",
            "Non-linguistic tests of recursive cognition.",
            "Separation of capacity claims from usage claims.",
        ],
        standards=[
            "Claims checked against both sides of the literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Everett DL. Cultural constraints on grammar and cognition in Piraha. Current Anthropology; 2005.",
            "Nevins A, Pesetsky D, Rodrigues C. Piraha exceptionality: a reassessment. Language; 2009.",
        ],
        hypotheses=[
            "Capacity-versus-use dissolves the contradiction.",
            "Piraha genuinely lacks recursion; UG is falsified.",
            "The data are wrong; Piraha has embedding after all.",
            "Culture constrains grammar more deeply than theory admits.",
        ],
        confirm="Piraha speakers show recursive cognition in non-linguistic tasks.",
        refute="No recursive cognition appears in any domain.",
    ),
    dict(
        key="linguistics-10",
        name="Is There a Universal Grammar",
        group="Theory",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Do all human languages share an innate grammatical blueprint - "
                 "Universal Grammar - or does linguistic diversity run all the "
                 "way down?"),
        background=("Chomsky proposed that children could not learn language so "
                    "fast without built-in grammatical knowledge. Decades of "
                    "fieldwork then revealed staggering diversity - languages "
                    "without clear nouns and verbs, without embedding, without "
                    "tenses. Defenders retreated to abstract principles; critics "
                    "(Evans and Levinson) declared diversity's end to UG. The "
                    "field's central schism persists, now fought with "
                    "computational models and large typological databases."),
        why_it_matters=("Universal Grammar is the boldest claim ever made about the "
                        "human mind. Its fate decides whether linguistics is a "
                        "branch of biology or of cultural history."),
        sig_lens=("The Signature lens treats UG as a learnability ledger: the "
                  "Signature approach asks what minimal innate bias makes "
                  "acquisition work."),
        sig_body=("The Signature proposal models UG as a hierarchy of biases, not "
                  "a rulebook. Assumptions: (1) acquisition needs some prior; "
                  "(2) the prior can be thin (prefer hierarchy, prefer "
                  "regularity); (3) cultural evolution shapes the rest. "
                  "Reasoning path: the proposal shows a thin bias set - toward "
                  "hierarchical, compositional, learnable systems - suffices for "
                  "computational models to acquire grammar from realistic input, "
                  "predicting that universals should be statistical tendencies "
                  "(Greenberg's word-order correlations) rather than absolute "
                  "laws. Both camps then capture half the truth. Limits: "
                  "'thin' biases are hard to distinguish from general cognition; "
                  "the model needs large-scale acquisition simulations."),
        pointer=('The Signature system models UG as thin learnability biases, predicting statistical universals rather than absolute laws. The Signature test: acquisition models succeed with thin biases on realistic input. It would be refuted if a structure appears that no thin bias could learn.'),
        key_points=[
            "Chomsky proposed innate grammatical knowledge to explain acquisition speed.",
            "Fieldwork revealed far more diversity than early theory allowed.",
            "Defenders retreated to abstract principles; critics declared UG dead.",
            "Typological databases now test universals at scale.",
        ],
        requirements=[
            "An account of acquisition without hand-waving.",
            "Consistency with documented diversity.",
            "Testable predictions distinguishing thin from rich innateness.",
        ],
        standards=[
            "Claims checked against both sides of the literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Chomsky N. Knowledge of Language. Praeger; 1986.",
            "Evans N, Levinson SC. The myth of language universals. Behavioral and Brain Sciences; 2009.",
        ],
        hypotheses=[
            "Thin learnability biases plus culture explain everything.",
            "Rich innate grammar is real but abstract.",
            "No language-specific innateness exists.",
            "Universals are statistical, not absolute.",
        ],
        confirm="Acquisition models succeed with thin biases on realistic input.",
        refute="A structure appears that no thin bias could learn.",
    ),
    dict(
        key="linguistics-11",
        name="Gradience Versus Categories",
        group="Theory",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Is grammar made of discrete categories (noun, verb, grammatical, "
                 "ungrammatical) or gradient continua - and can linguistics survive "
                 "the answer?"),
        background=("Speakers judge sentences on a sliding scale, sound change is "
                    "phonetically gradual, and categories like 'word' dissolve "
                    "cross-linguistically. Yet grammatical theory runs on discrete "
                    "symbols. Exemplar models and usage-based linguistics embrace "
                    "gradience; formalists insist categories are real and "
                    "gradience is performance noise. The dispute is about what "
                    "kind of thing a language is."),
        why_it_matters=("If grammar is gradient, the last century of grammatical "
                        "theory needs rebuilding on probabilistic foundations - "
                        "which is exactly what is happening."),
        sig_lens=("The Signature lens treats the dispute as a resolution ledger: "
                  "the Signature approach asks at what grain categories emerge "
                  "from gradients."),
        sig_body=("The Signature proposal models categories as emergent from "
                  "gradient use. Assumptions: (1) usage is gradient (frequency, "
                  "similarity, context); (2) learners discretize for efficient "
                  "storage; (3) discretization thresholds vary. Reasoning path: "
                  "the proposal shows discrete categories can be stable "
                  "attractors in a gradient system - like colors from "
                  "wavelengths - predicting that category boundaries should be "
                  "sharpest where communicative stakes are highest. Formal "
                  "grammar then describes the attractors, not the substrate. "
                  "Limits: the emergence math is easier to sketch than to "
                  "prove for real grammars."),
        pointer=('The Signature system models categories as stable attractors in gradient usage, sharpest where communicative stakes are highest. The Signature test: category boundaries track communicative-stakes measures. It would be refuted if sharp boundaries appear where stakes are lowest.'),
        key_points=[
            "Acceptability judgments are gradient, not binary.",
            "Sound change is phonetically gradual.",
            "Formal theory requires discrete symbols.",
            "Exemplar and usage-based models embrace gradience.",
        ],
        requirements=[
            "An account of both gradient data and categorical intuitions.",
            "A mechanism for category emergence.",
            "Testable boundary-sharpness predictions.",
        ],
        standards=[
            "Claims checked against the theoretical literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bybee J. Phonology and Language Use. Cambridge University Press; 2001.",
            "Aarts B. Syntactic Gradience. Oxford University Press; 2007.",
        ],
        hypotheses=[
            "Categories are attractors emerging from gradient use.",
            "Grammar is fundamentally discrete; gradience is noise.",
            "Probability is the native format of grammar.",
            "Different subsystems differ: phonetics gradient, syntax discrete.",
        ],
        confirm="Category boundaries track communicative-stakes measures.",
        refute="Sharp boundaries appear where stakes are lowest.",
    ),
    dict(
        key="linguistics-12",
        name="The Sapir-Whorf Question",
        group="Mind",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("How strongly does language shape thought - does speaking a "
                 "different language mean thinking differently?"),
        background=("Strong Whorfianism (language determines thought) is dead; "
                    "the live question is the strength of weak effects. Evidence "
                    "exists: Russian blues, Guugu Yimithirr cardinal directions, "
                    "grammatical gender effects, numerical language effects. But "
                    "effects are small, task-dependent, and sometimes "
                    "unreplicable. The field oscillates between 'language "
                    "profoundly shapes cognition' and 'effects are lab "
                    "curiosities.'"),
        why_it_matters=("The answer determines whether translation is possible in "
                        "principle, whether AI needs language to think, and how "
                        "much of the mind is culturally made."),
        sig_lens=("The Signature lens treats Whorfian effects as an attention "
                  "ledger: the Signature approach asks what language makes "
                  "habitually easy to notice."),
        sig_body=("The Signature proposal models language as an attention habit. "
                  "Assumptions: (1) languages obligatorily encode some "
                  "distinctions (tense, gender, direction); (2) habitual "
                  "encoding trains attention; (3) attention shapes memory and "
                  "reasoning. Reasoning path: the proposal predicts Whorfian "
                  "effects should be strongest exactly where grammar forces "
                  "encoding - Russian blues, absolute direction - and weakest "
                  "where language merely allows description. The effects are "
                  "then real but bounded: language tunes the spotlight, it does "
                  "not build the theater. Limits: the model needs independent "
                  "measures of habitual encoding; some effects resist the "
                  "attention account."),
        pointer=('The Signature system models language as habitual attention training, with effects strongest where grammar forces encoding. The Signature test: effect sizes track obligatoriness of encoding across languages. It would be refuted if large effects appear where grammar encodes nothing.'),
        key_points=[
            "Strong determinism is abandoned; weak effects are the live question.",
            "Real effects documented: color, space, gender, number.",
            "Effects are small and task-dependent.",
            "Replication has been uneven.",
        ],
        requirements=[
            "An account predicting where effects appear and where not.",
            "Separation of habitual from momentary effects.",
            "Cross-linguistic replication.",
        ],
        standards=[
            "Claims checked against the relativity literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Whorf BL. Language, Thought, and Reality. MIT Press; 1956.",
            "Boroditsky L. Does language shape thought? Cognitive Psychology; 2001.",
        ],
        hypotheses=[
            "Language trains habitual attention; effects are real but bounded.",
            "Effects are lab artifacts with no real-world weight.",
            "Language shapes thought profoundly in some domains.",
            "Thought is universal; language merely expresses it.",
        ],
        confirm="Effect sizes track obligatoriness of encoding across languages.",
        refute="Large effects appear where grammar encodes nothing.",
    ),
    dict(
        key="linguistics-13",
        name="Language and Number",
        group="Mind",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("How does language shape numerical cognition - and what can "
                 "humans think about numbers without number words?"),
        background=("The Piraha and Munduruku lack exact number words past small "
                    "quantities, and struggle with exact arithmetic while handling "
                    "approximate quantities fine. The approximate number system "
                    "is ancient and shared with animals; exact arithmetic seems "
                    "to need linguistic scaffolding. But how much - and whether "
                    "number words create or merely label exact concepts - remains "
                    "open."),
        why_it_matters=("Numbers underlie mathematics, science, and markets. If "
                        "exact number is a linguistic invention, then language "
                        "built mathematics."),
        sig_lens=("The Signature lens treats number words as a precision ledger: "
                  "the Signature approach asks what exactness costs without "
                  "words."),
        sig_body=("The Signature proposal models number words as precision "
                  "tools. Assumptions: (1) the approximate number system is "
                  "innate and noisy; (2) exact arithmetic needs stable symbols "
                  "for exact values; (3) words provide the cheapest stable "
                  "symbols. Reasoning path: the proposal shows exact number "
                  "concepts should be impossible without external symbols - "
                  "words, tallies, or fingers - predicting that anumeric "
                  "cultures fail exact tasks but pass approximate ones, which "
                  "matches the Amazonian data. Number words do not label "
                  "pre-existing exact concepts; they create them. Limits: the "
                  "model needs finer data on intermediate systems (body-count "
                  "numerals, tallies)."),
        pointer=('The Signature system models number words as precision tools that create exact concepts rather than labeling them. The Signature test: exact-task failure tracks symbol absence across systems. It would be refuted if anumeric individuals perform exact arithmetic without symbols.'),
        key_points=[
            "Anumeric cultures handle approximate but not exact number.",
            "The approximate number system is shared with animals.",
            "Exact arithmetic seems to require linguistic scaffolding.",
            "Body-part and tally systems are intermediate cases.",
        ],
        requirements=[
            "An account of the approximate-exact divide.",
            "Consistency with Amazonian field data.",
            "A mechanism for symbol-created concepts.",
        ],
        standards=[
            "Claims checked against the numerical-cognition literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Gordon P. Numerical cognition without words. Science; 2004.",
            "Dehaene S. The Number Sense. Oxford University Press; 1997.",
        ],
        hypotheses=[
            "Number words create exact concepts; without them only approximation exists.",
            "Exact concepts are innate; words merely label them.",
            "Tallies and fingers suffice; spoken words are secondary.",
            "The divide is cultural practice, not linguistic capacity.",
        ],
        confirm="Exact-task failure tracks symbol absence across systems.",
        refute="Anumeric individuals perform exact arithmetic without symbols.",
    ),
    dict(
        key="linguistics-14",
        name="Color Across Languages",
        group="Mind",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("Why do color vocabularies evolve in a predictable sequence across "
                 "unrelated languages - and what does it reveal about perception?"),
        background=("Berlin and Kay found color terms enter languages in a "
                    "near-universal order: black/white, then red, then green/yellow, "
                    "then blue. The World Color Survey confirmed the pattern "
                    "broadly, with critics noting exceptions and the role of "
                    "technology (dyes) and environment. The sequence suggests "
                    "perception constrains vocabulary - but how, and why this "
                    "order?"),
        why_it_matters=("Color naming is the best-documented universal in "
                        "linguistics. Its explanation would be the template for "
                        "all language-cognition interactions."),
        sig_lens=("The Signature lens treats color terms as a salience ledger: "
                  "the Signature approach asks which distinctions pay their "
                  "naming cost first."),
        sig_body=("The Signature proposal models the sequence as communicative "
                  "payoff ordering. Assumptions: (1) naming a distinction costs "
                  "learning effort; (2) the payoff is successful reference; (3) "
                  "some distinctions matter more universally (blood, night, "
                  "vegetation). Reasoning path: the proposal shows the Berlin-Kay "
                  "order matches a payoff ranking - light-dark and red first "
                  "because they carry the most survival-relevant information - "
                  "predicting that technological change (dyes, screens) should "
                  "accelerate later terms, which matches the data. Perception "
                  "sets the menu; communicative need orders it. Limits: the "
                  "payoff ranking is partly post hoc; some languages violate "
                  "the sequence."),
        pointer=('The Signature system models the color-term sequence as communicative payoff ordering over a perceptual menu. The Signature test: term order tracks independent payoff measures across languages. It would be refuted if payoff-irrelevant distinctions enter early and systematically.'),
        key_points=[
            "Color terms enter languages in a near-universal sequence.",
            "The World Color Survey broadly confirmed the pattern.",
            "Technology and environment modulate the sequence.",
            "Exceptions exist and fuel the debate.",
        ],
        requirements=[
            "An account of the specific order, not just universality.",
            "Consistency with the documented exceptions.",
            "Separation of perceptual from communicative factors.",
        ],
        standards=[
            "Claims checked against the color-naming literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Berlin B, Kay P. Basic Color Terms. University of California Press; 1969.",
            "Regier T, Kay P, Khetarpal N. Color naming reflects optimal partitions of color space. PNAS; 2007.",
        ],
        hypotheses=[
            "Communicative payoff orders the perceptual menu.",
            "Perceptual salience alone determines the sequence.",
            "Technology and dyes drive the later terms.",
            "The sequence is an artifact of sampling and analysis.",
        ],
        confirm="Term order tracks independent payoff measures across languages.",
        refute="Payoff-irrelevant distinctions enter early and systematically.",
    ),
    dict(
        key="linguistics-15",
        name="The Bilingual Advantage Debate",
        group="Mind",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Does bilingualism improve executive function - and did the "
                 "famous bilingual advantage evaporate under scrutiny?"),
        background=("Early studies found bilinguals outperformed monolinguals on "
                    "conflict tasks, attributed to constant language-control "
                    "exercise. Then came replication failures, publication-bias "
                    "exposures, and confound hunting (immigration, SES). The "
                    "current state: small effects in some populations, none in "
                    "others, with the field split between 'real but tiny' and "
                    "'methodological artifact.'"),
        why_it_matters=("Millions of parents and educators make decisions on this "
                        "claim. Its fate is also a case study in replication and "
                        "bias."),
        sig_lens=("The Signature lens treats the debate as a confound ledger: "
                  "the Signature approach asks what bilingualism correlates "
                  "with besides language control."),
        sig_body=("The Signature proposal models the advantage as a dose-and-"
                  "context effect. Assumptions: (1) language control exercises "
                  "executive function; (2) exercise effects are dose-dependent; "
                  "(3) immigrant and SES confounds are real. Reasoning path: "
                  "the proposal predicts advantages should appear where "
                  "switching is frequent and demanding (balanced bilinguals, "
                  "dense code-switching communities) and vanish where it is "
                  "not - reconciling positive and null findings as sampling "
                  "different doses. The effect is real but narrow. Limits: "
                  "dose is hard to measure retrospectively; the model needs "
                  "preregistered dose-response studies."),
        pointer=('The Signature system models the advantage as dose-dependent, reconciling positive and null findings as different switching doses. The Signature test: preregistered studies show dose-response effects. It would be refuted if large preregistered studies find zero effect at all doses.'),
        key_points=[
            "Early studies found executive-function advantages for bilinguals.",
            "Replication failures and publication bias followed.",
            "Immigration and SES confounds are documented.",
            "Current state: small effects in some samples, none in others.",
        ],
        requirements=[
            "Preregistered designs with confound control.",
            "A dose-response account reconciling mixed findings.",
            "Separation of switching practice from bilingualism per se.",
        ],
        standards=[
            "Claims checked against the full debate literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bialystok E et al. Bilingualism, aging, and cognitive control. Neuropsychology; 2004.",
            "Paap KR, Greenberg ZI. There is no coherent evidence for a bilingual advantage. 2013.",
        ],
        hypotheses=[
            "The advantage is real but dose-dependent and narrow.",
            "It is entirely a confound artifact.",
            "It exists only in dense code-switching contexts.",
            "It protects against cognitive aging specifically.",
        ],
        confirm="Preregistered studies show dose-response effects.",
        refute="Large preregistered studies find zero effect at all doses.",
    ),
    dict(
        key="linguistics-16",
        name="Animal Communication Versus Language",
        group="Mind",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("What exactly separates human language from the richest animal "
                 "communication - and is the gap qualitative or quantitative?"),
        background=("Prairie dogs encode predator details; bees dance vectors; "
                    "apes learn hundreds of signs; songbirds show finite-state "
                    "syntax. Yet no animal system shows open-ended hierarchical "
                    "generativity. Candidates for the Rubicon: recursion, "
                    "displacement, theory of mind, teaching, or simply the "
                    "combination. Each has been challenged by new animal "
                    "findings."),
        why_it_matters=("The boundary defines what language is - and what "
                        "artificial systems would need to cross it."),
        sig_lens=("The Signature lens treats the boundary as a combination "
                  "ledger: the Signature approach asks which set of ordinary "
                  "abilities, combined, crosses the line."),
        sig_body=("The Signature proposal models the gap as a threshold in "
                  "combinatorial power. Assumptions: (1) many components exist "
                  "in animals (reference, learning, sociality); (2) components "
                  "interact multiplicatively; (3) open-endedness needs the full "
                  "set. Reasoning path: the proposal shows no single Rubicon "
                  "survives the animal data - but the combination of "
                  "hierarchical cognition, shared intentionality, and vocal "
                  "learning crosses a threshold where generativity explodes. "
                  "The gap is then a phase transition, appearing qualitative "
                  "from either side. Limits: the threshold is hard to "
                  "quantify; the model predicts intermediates that are "
                  "scarce."),
        pointer=('The Signature system models the human-animal gap as a combinatorial phase transition rather than a single Rubicon. The Signature test: intermediate systems show partial generativity as predicted. It would be refuted if an animal system demonstrates full open-ended generativity.'),
        key_points=[
            "Rich animal systems exist: prairie dogs, bees, apes, songbirds.",
            "No animal system shows open-ended hierarchical generativity.",
            "Every proposed Rubicon has animal counterexamples.",
            "The combination-of-traits view is gaining ground.",
        ],
        requirements=[
            "An account surviving the animal counterexamples.",
            "A mechanism for the apparent qualitative gap.",
            "Testable predictions about intermediate systems.",
        ],
        standards=[
            "Claims checked against the comparative-communication literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hauser MD, Chomsky N, Fitch WT. The faculty of language. Science; 2002.",
            "Tomasello M. Origins of Human Communication. MIT Press; 2008.",
        ],
        hypotheses=[
            "A combinatorial threshold creates the apparent qualitative gap.",
            "Recursion alone is the Rubicon.",
            "Shared intentionality is the key difference.",
            "The gap is quantitative; more data will close it.",
        ],
        confirm="Intermediate systems show partial generativity as predicted.",
        refute="An animal system demonstrates full open-ended generativity.",
    ),
    dict(
        key="linguistics-17",
        name="Music and Language: Shared Origins",
        group="Mind",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Do music and language share evolutionary origins - and what "
                 "neural machinery do they share today?"),
        background=("The 'musilanguage' hypothesis proposes a common ancestor: "
                    "holistic, emotive vocalizations that split into "
                    "propositional language and musical expression. Evidence: "
                    "shared neural resources, infant-directed song-speech, the "
                    "universality of both, and structural parallels (hierarchy, "
                    "rhythm). Skeptics note music lacks propositional meaning "
                    "and language lacks music's social bonding power - the "
                    "split may be ancient and complete."),
        why_it_matters=("A shared origin would mean the human voice evolved once "
                        "for expressive sound - and that music is not a luxury "
                        "but a sibling of speech."),
        sig_lens=("The Signature lens treats the split as a function ledger: "
                  "the Signature approach asks what job each half took when "
                  "the system divided."),
        sig_body=("The Signature proposal models a functional split from a "
                  "common vocal system. Assumptions: (1) early hominin "
                  "vocalization was holistic and emotive; (2) propositional "
                  "precision and social bonding are different optimization "
                  "targets; (3) neural reuse is cheaper than new systems. "
                  "Reasoning path: the proposal shows one vocal system cannot "
                  "simultaneously maximize precision and emotional contagion - "
                  "so the system split, with language taking reference and "
                  "music taking bonding. Shared neural machinery is then "
                  "inheritance, and infant-directed communication (song-speech) "
                  "is the living fossil. Limits: the split's timing is "
                  "unknown; the model needs comparative primate data."),
        pointer=('The Signature system models music and language as a functional split from one ancestral vocal system, with infant song-speech as the living fossil. The Signature test: shared neural substrates handle the overlapping functions. It would be refuted if no shared machinery exists beyond generic audition.'),
        key_points=[
            "The musilanguage hypothesis proposes a common ancestor.",
            "Neural resources overlap partially.",
            "Infant-directed communication blends song and speech.",
            "Music lacks propositional meaning; language lacks music's bonding power.",
        ],
        requirements=[
            "An account of the split's functional logic.",
            "Neural evidence of shared versus distinct machinery.",
            "Comparative primate data on vocal precursors.",
        ],
        standards=[
            "Claims checked against the music-language literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Brown S. The musilanguage model of music evolution. 2000.",
            "Fitch WT. The biology and evolution of music. Cognition; 2006.",
        ],
        hypotheses=[
            "One ancestral system split into referential and bonding functions.",
            "Music and language evolved independently.",
            "Music is a spandrel of language machinery.",
            "Language is a spandrel of musical protolanguage.",
        ],
        confirm="Shared neural substrates handle the overlapping functions.",
        refute="No shared machinery exists beyond generic audition.",
    ),
    dict(
        key="linguistics-18",
        name="Basque Origins",
        group="Isolates",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Where did Basque - Europe's great language isolate, unrelated to "
                 "any living tongue - come from?"),
        background=("Basque (Euskara) is the only surviving pre-Indo-European "
                    "language of western Europe. Ancient DNA links modern Basques "
                    "to local Iron Age populations, suggesting the language is "
                    "a genuine relic - but of what? Aquitanian inscriptions "
                    "provide a relative; deeper relatives are unknown. Theories "
                    "range from Paleolithic continuity to a Neolithic farmer "
                    "language that survived the Indo-European wave."),
        why_it_matters=("Basque is the last voice of pre-Indo-European western "
                        "Europe. Its origin is the origin story of the continent's "
                        "first languages."),
        sig_lens=("The Signature lens treats Basque as a survival ledger: the "
                  "Signature approach asks what let one language outlive its "
                  "entire family."),
        sig_body=("The Signature proposal models Basque survival as geographic "
                  "plus social refuge. Assumptions: (1) the Pyrenees provided "
                  "terrain refuge; (2) Basque speakers maintained distinct "
                  "identity through the Indo-European expansion; (3) relic "
                  "languages survive where assimilation pressure is low. "
                  "Reasoning path: the proposal shows isolate survival "
                  "correlates with refuge terrain plus persistent identity "
                  "boundaries - predicting Basque should show deep local "
                  "continuity (confirmed by DNA) with Aquitanian as the "
                  "nearest lost relative. The language is then a mountain "
                  "relic, not a migrant. Limits: the deeper family remains "
                  "unknown; the model cannot name the original spread."),
        pointer=('The Signature system models Basque as a mountain-refuge relic with deep local continuity, Aquitanian as its nearest lost relative. The Signature test: ancient DNA finds the language-family boundary matching refuge terrain. It would be refuted if basque proves to be a recent arrival, not a deep relic.'),
        key_points=[
            "Basque is unrelated to any living language.",
            "Ancient DNA shows deep local continuity.",
            "Aquitanian inscriptions provide the only known relative.",
            "Paleolithic versus Neolithic origin debated.",
        ],
        requirements=[
            "Reconciliation of linguistic isolation with genetic continuity.",
            "An account of survival through the Indo-European expansion.",
            "Deeper relatives or a principled relic account.",
        ],
        standards=[
            "Claims checked against the Basque literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Trask RL. The History of Basque. Routledge; 1997.",
            "Olalde I et al. The genomic history of the Iberian Peninsula. Science; 2019.",
        ],
        hypotheses=[
            "Basque is a refuge relic of pre-Indo-European Europe.",
            "It arrived with Neolithic farmers and survived in the mountains.",
            "Deeper relatives await discovery in ancient DNA.",
            "It descends from a wider Aquitanian-Pyrenean family.",
        ],
        confirm="Ancient DNA finds the language-family boundary matching refuge terrain.",
        refute="Basque proves to be a recent arrival, not a deep relic.",
    ),
    dict(
        key="linguistics-19",
        name="How Far Back Can We Reconstruct",
        group="Deep Reconstruction",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("What is the time limit of the comparative method - how far back "
                 "can we reliably reconstruct proto-languages?"),
        background=("Indo-European is reconstructed to about 4500 BCE with "
                    "confidence; Afroasiatic and Austronesian reach similar "
                    "depths. Beyond 8,000 to 10,000 years, sound changes "
                    "overwrite the evidence - the signal decays into noise. "
                    "Long-rangers propose Nostratic, Dene-Caucasian, and even "
                    "Proto-World; mainstream historical linguists consider these "
                    "beyond the method's horizon. The limit itself is the "
                    "dispute."),
        why_it_matters=("The reconstruction horizon is the edge of linguistic "
                        "knowledge - beyond it lies most of human language "
                        "history, unreachable by current methods."),
        sig_lens=("The Signature lens treats reconstruction as a signal-decay "
                  "ledger: the Signature approach asks where the signal "
                  "drowns in noise."),
        sig_body=("The Signature proposal models the horizon as information-"
                  "theoretic decay. Assumptions: (1) each sound change erases "
                  "some information; (2) changes accumulate roughly with time; "
                  "(3) the method needs signal above chance. Reasoning path: "
                  "the proposal computes that with realistic change rates, "
                  "cognate signal falls to chance around 8,000 to 10,000 years "
                  "- predicting exactly the observed wall, and predicting that "
                  "morphological paradigms (more redundant) should reach "
                  "slightly further than sounds. Long-range proposals then "
                  "fail not from lack of trying but from physics. Limits: "
                  "change rates vary; the model needs better rate "
                  "calibration."),
        pointer=('The Signature system models the reconstruction horizon as information decay, predicting the wall near 10,000 years. The Signature test: decay models predict the observed wall quantitatively. It would be refuted if a deep reconstruction verifies against independent evidence.'),
        key_points=[
            "Secure reconstruction reaches about 6,000 to 8,000 years.",
            "Beyond 10,000 years, signal decays toward chance.",
            "Long-range proposals (Nostratic, Proto-World) are disputed.",
            "Morphology may preserve signal slightly longer than sound.",
        ],
        requirements=[
            "A quantitative model of signal decay.",
            "An account of why morphology might outlast phonology.",
            "Testable predictions about the horizon.",
        ],
        standards=[
            "Claims checked against the historical-linguistics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ringe D. On calculating the factor of chance in language comparison. 1992.",
            "Nichols J. Linguistic Diversity in Space and Time. University of Chicago Press; 1992.",
        ],
        hypotheses=[
            "Information decay sets a hard horizon near 10,000 years.",
            "Better methods can push significantly further.",
            "Morphological reconstruction extends the horizon.",
            "The horizon varies too much for a single number.",
        ],
        confirm="Decay models predict the observed wall quantitatively.",
        refute="A deep reconstruction verifies against independent evidence.",
    ),
    dict(
        key="linguistics-20",
        name="The Nostratic Hypothesis",
        group="Deep Reconstruction",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Was there a Nostratic macro-family uniting Indo-European, "
                 "Uralic, Altaic, Afroasiatic, and others - and can it be "
                 "proven?"),
        background=("Proposed by Pedersen and developed by Soviet linguists, "
                    "Nostratic would push reconstruction to 15,000+ years ago. "
                    "Supporters cite pronouns, basic vocabulary, and "
                    "morphological parallels; critics cite chance resemblances, "
                    "semantic latitude, and the time-depth problem. The "
                    "hypothesis sits exactly on the reconstruction horizon - "
                    "which is why it cannot be settled."),
        why_it_matters=("Nostratic would be the deepest proven language family - "
                        "a window into the languages of the Ice Age's end."),
        sig_lens=("The Signature lens treats Nostratic as a chance ledger: the "
                  "Signature approach asks how many resemblances chance "
                  "alone produces."),
        sig_body=("The Signature proposal models the Nostratic evidence against "
                  "a chance baseline. Assumptions: (1) unrelated languages "
                  "show chance resemblances at a computable rate; (2) "
                  "proponents select the best matches; (3) semantic latitude "
                  "inflates hit rates. Reasoning path: the proposal shows "
                  "that with enough languages and loose semantics, chance "
                  "produces Nostratic-scale resemblance lists - predicting "
                  "that the hypothesis can only be saved by morphological "
                  "paradigms (harder to fake by chance) rather than word "
                  "lists. The verdict hinges on paradigms, not vocabulary. "
                  "Limits: the chance baseline needs better calibration; "
                  "paradigm evidence is thin."),
        pointer=('The Signature system tests Nostratic against a computed chance baseline, arguing only morphological paradigms could save it. The Signature test: paradigmatic morphology matches across families above chance. It would be refuted if calibrated chance models reproduce all cited resemblances.'),
        key_points=[
            "Nostratic would unite most of Eurasia's families.",
            "Proposed time depth exceeds the secure reconstruction horizon.",
            "Supporters cite pronouns and basic vocabulary.",
            "Critics cite chance and semantic latitude.",
        ],
        requirements=[
            "Resemblances exceeding a calibrated chance baseline.",
            "Morphological paradigms, not just word lists.",
            "Regular sound correspondences across the macro-family.",
        ],
        standards=[
            "Claims checked against the long-range literature on both sides.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Pedersen H. Linguistic Science in the Nineteenth Century. 1931.",
            "Bomhard AR. Reconstructing Proto-Nostratic. Brill; 2008.",
        ],
        hypotheses=[
            "Chance explains the resemblances; Nostratic is unprovable.",
            "Morphological paradigms will eventually confirm it.",
            "A shallower Eurasiatic grouping is provable; Nostratic is not.",
            "New methods will break the time barrier.",
        ],
        confirm="Paradigmatic morphology matches across families above chance.",
        refute="Calibrated chance models reproduce all cited resemblances.",
    ),
    dict(
        key="linguistics-21",
        name="The Mother Tongue Hypothesis",
        group="Deep Reconstruction",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Did all human languages descend from a single original tongue - "
                 "and could we ever know?"),
        background=("Monogenesis (one origin) versus polygenesis (many origins) "
                    "is linguistics' deepest historical question. Genetics "
                    "suggests a single human origin population, which favors "
                    "monogenesis - but language could have emerged multiple "
                    "times, or emerged once and been reinvented. Proto-World "
                    "word lists (Ruhlen) are dismissed by mainstream linguists "
                    "as chance. The question may be permanently unanswerable."),
        why_it_matters=("A single mother tongue would mean every human word ever "
                        "spoken descends from one ancestral vocabulary - the "
                        "ultimate linguistic unity."),
        sig_lens=("The Signature lens treats the question as an information "
                  "ledger: the Signature approach asks what could possibly "
                  "survive 100,000 years of change."),
        sig_body=("The Signature proposal models monogenesis as untestable with "
                  "current methods. Assumptions: (1) the reconstruction "
                  "horizon is about 10,000 years; (2) language is at least "
                  "50,000 years old; (3) only extraordinary evidence could "
                  "bridge the gap. Reasoning path: the proposal shows the "
                  "information gap exceeds the method's reach by an order of "
                  "magnitude - like reconstructing a whisper from echoes "
                  "across a canyon. Monogenesis is then plausible (given "
                  "genetic unity) but scientifically undecidable, a question "
                  "for philosophy, not linguistics. Limits: a breakthrough "
                  "method could reopen it; the model assumes current "
                  "methods."),
        pointer=('The Signature system models monogenesis as plausible but scientifically undecidable given the reconstruction horizon. The Signature test: a new method bridges the information gap verifiably. It would be refuted if no method can bridge it; the question leaves science.'),
        key_points=[
            "Genetic unity favors one origin population.",
            "The reconstruction horizon is far shallower than language's age.",
            "Proto-World lists are rejected by mainstream linguists.",
            "The question may be permanently unanswerable.",
        ],
        requirements=[
            "A method bridging a 5x-10x information gap.",
            "Separation of plausibility from testability.",
            "An account of polygenesis alternatives.",
        ],
        standards=[
            "Claims checked against the literature; untestability stated plainly.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ruhlen M. The Origin of Language. Wiley; 1994.",
            "Bickerton D. More than Nature Needs. Harvard University Press; 2009.",
        ],
        hypotheses=[
            "Monogenesis is true but unprovable with current methods.",
            "Language emerged multiple times independently.",
            "One origin plus later reinventions.",
            "A breakthrough method will eventually decide it.",
        ],
        confirm="A new method bridges the information gap verifiably.",
        refute="No method can bridge it; the question leaves science.",
    ),
    dict(
        key="linguistics-22",
        name="The Limits of the Comparative Method",
        group="Deep Reconstruction",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("What are the principled limits of the comparative method - and "
                 "which apparent reconstructions exceed them?"),
        background=("The comparative method rebuilt Indo-European from its "
                    "daughters - linguistics' greatest triumph. But its limits "
                    "are debated: it assumes tree-like divergence (borrowing "
                    "violates it), needs sufficient data, and cannot recover "
                    "what left no trace. Computational phylogenetics extends "
                    "its reach but inherits its assumptions. Knowing the "
                    "method's boundaries is knowing what linguistic history "
                    "can ever deliver."),
        why_it_matters=("Every claim about language prehistory rests on this "
                        "method. Its limits are the limits of the field's "
                        "knowledge."),
        sig_lens=("The Signature lens treats the method as an instrument "
                  "ledger: the Signature approach asks what the instrument "
                  "cannot measure by design."),
        sig_body=("The Signature proposal maps the method's blind spots. "
                  "Assumptions: (1) the method reconstructs what daughters "
                  "share; (2) borrowing mimics inheritance; (3) extinct "
                  "branches leave no signal. Reasoning path: the proposal "
                  "shows three principled limits - the borrowing blind spot "
                  "(areal features reconstructed as inherited), the extinction "
                  "blind spot (lost branches invisible), and the time-decay "
                  "limit - predicting that reconstructions are systematically "
                  "biased toward the survivors' common core. Proto-languages "
                  "are then minimum viable ancestors, not full languages. "
                  "Limits: quantifying the biases needs better borrowing "
                  "models."),
        pointer=('The Signature system maps three blind spots - borrowing, extinction, time-decay - arguing proto-languages are minimum viable ancestors. The Signature test: bias corrections change reconstructions systematically. It would be refuted if borrowing proves fully separable from inheritance.'),
        key_points=[
            "The comparative method is linguistics' greatest success.",
            "It assumes tree-like divergence; borrowing violates the assumption.",
            "Extinct branches leave no recoverable signal.",
            "Computational methods extend reach but inherit assumptions.",
        ],
        requirements=[
            "A principled map of the method's blind spots.",
            "Borrowing models separating contact from inheritance.",
            "An account of what reconstructions systematically miss.",
        ],
        standards=[
            "Claims checked against the historical-methods literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Meillet A. Introduction a l'etude comparative des langues indo-europeennes. 1903.",
            "Campbell L. Historical Linguistics. MIT Press; 2013.",
        ],
        hypotheses=[
            "Three blind spots bound the method; proto-languages are minima.",
            "Computational methods will dissolve the borrowing problem.",
            "The method is sounder than its critics allow.",
            "Areal linguistics needs equal status with family trees.",
        ],
        confirm="Bias corrections change reconstructions systematically.",
        refute="Borrowing proves fully separable from inheritance.",
    ),
    dict(
        key="linguistics-23",
        name="Why Are Some Sounds Rare",
        group="Sound",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Why do some speech sounds - clicks, ejectives, front rounded "
                 "vowels - occur in few languages while others are nearly "
                 "universal?"),
        background=("About 7 percent of languages use clicks; ejectives cluster "
                    "in the Caucasus, the Americas, and Africa; front rounded "
                    "vowels are a Eurasian specialty. Explanations invoke "
                    "articulatory difficulty, perceptual salience, areal spread, "
                    "and plain historical accident. But difficulty alone fails - "
                    "children master clicks easily - and some rare sounds are "
                    "articulatorily simple."),
        why_it_matters=("Sound inventories are the raw material of language. "
                        "Their distribution reveals the physics, biology, and "
                        "history shaping speech."),
        sig_lens=("The Signature lens treats sound rarity as a cost-benefit "
                  "ledger: the Signature approach asks what each sound costs "
                  "to keep."),
        sig_body=("The Signature proposal models inventories as economies. "
                  "Assumptions: (1) each sound costs learning and production "
                  "effort; (2) sounds pay by distinguishing words; (3) "
                  "areal contact spreads successful inventories. Reasoning "
                  "path: the proposal shows rare sounds persist where they "
                  "carry high functional load (clicks distinguishing many "
                  "words in Khoisan) or where areal prestige sustains them - "
                  "predicting rarity tracks cost-benefit ratios, not raw "
                  "difficulty. Children learn clicks easily because the "
                  "learning cost is paid once; the maintenance cost is what "
                  "matters. Limits: functional load is hard to measure "
                  "historically; accident plays a real role."),
        pointer=('The Signature system models sound inventories as economies where rarity tracks cost-benefit ratios, not raw difficulty. The Signature test: rarity tracks measured cost-benefit ratios. It would be refuted if high-benefit sounds remain rare without areal explanation.'),
        key_points=[
            "Clicks occur in about 7 percent of languages.",
            "Children master even 'difficult' sounds easily.",
            "Rare sounds cluster areally.",
            "Difficulty, salience, spread, and accident all have defenders.",
        ],
        requirements=[
            "An account separating learning cost from maintenance cost.",
            "Consistency with areal clustering.",
            "Functional-load measures for rare sounds.",
        ],
        standards=[
            "Claims checked against the phonological-typology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Maddieson I. Patterns of Sounds. Cambridge University Press; 1984.",
            "Ladefoged P, Maddieson I. The Sounds of the World's Languages. Blackwell; 1996.",
        ],
        hypotheses=[
            "Cost-benefit ratios determine inventory membership.",
            "Articulatory difficulty is the primary filter.",
            "Areal spread explains most rarity patterns.",
            "Historical accident dominates; no deep explanation exists.",
        ],
        confirm="Rarity tracks measured cost-benefit ratios.",
        refute="High-benefit sounds remain rare without areal explanation.",
    ),
    dict(
        key="linguistics-24",
        name="The Origin of Clicks",
        group="Sound",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Where did click consonants come from - and why are they "
                 "concentrated in southern Africa with outliers in East Africa?"),
        background=("Clicks are the rarest major sound class, centered on Khoisan "
                    "languages with Bantu borrowings (Zulu, Xhosa) and the "
                    "East African outliers Hadza and Sandawe. Theories: clicks "
                    "are ancient retentions from the first languages, areal "
                    "innovations that spread, or avoidance-register sounds that "
                    "became phonemic. Genetic data links click-speaking "
                    "populations deep in time - but correlation is not "
                    "causation."),
        why_it_matters=("If clicks are retentions, they may be the oldest sounds "
                        "in human language - echoes of the first speech."),
        sig_lens=("The Signature lens treats clicks as a retention ledger: the "
                  "Signature approach asks what survives 100,000 years of "
                  "change."),
        sig_body=("The Signature proposal models clicks as stable retentions in "
                  "isolated populations. Assumptions: (1) clicks are "
                  "perceptually salient and articulatorily distinct; (2) "
                  "distinct sounds resist merger; (3) isolation preserves "
                  "archaisms. Reasoning path: the proposal shows clicks' "
                  "salience makes them unusually merger-resistant - predicting "
                  "they should survive longest exactly where populations were "
                  "most isolated, which matches the Khoisan distribution. The "
                  "Bantu borrowings then show clicks can spread as prestige "
                  "features. Whether they are THE original sounds remains "
                  "beyond proof. Limits: the retention model cannot date the "
                  "origin; the data are consistent with later innovation."),
        pointer=('The Signature system models clicks as merger-resistant retentions surviving longest in isolated populations. The Signature test: click stability correlates with isolation depth. It would be refuted if clicks prove to be recent innovations everywhere.'),
        key_points=[
            "Clicks centered on Khoisan; outliers in Hadza and Sandawe.",
            "Bantu languages borrowed clicks (Zulu, Xhosa).",
            "Genetic data links click populations deep in time.",
            "Retention, innovation, and avoidance-register theories compete.",
        ],
        requirements=[
            "An account of the geographic concentration.",
            "A mechanism for 100,000-year sound stability.",
            "Separation of retention from spread explanations.",
        ],
        standards=[
            "Claims checked against the Khoisan literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Gueldemann T, Elderkin ED. On external genealogical relationships of the Khoe family. 2010.",
            "Sands B. The linguistic geography of Africa. 2017.",
        ],
        hypotheses=[
            "Clicks are ancient retentions in isolated populations.",
            "They are areal innovations that spread.",
            "They began as avoidance-register sounds.",
            "They are the oldest sounds in human language.",
        ],
        confirm="Click stability correlates with isolation depth.",
        refute="Clicks prove to be recent innovations everywhere.",
    ),
    dict(
        key="linguistics-25",
        name="Tonogenesis: Where Tones Come From",
        group="Sound",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("How do tone systems - where pitch changes word meaning - emerge "
                 "from non-tonal ancestors?"),
        background=("Tonogenesis is the best-understood sound change: consonant "
                    "contrasts (voiced versus voiceless) collapse, and pitch "
                    "differences left on the vowels become phonemic tone. "
                    "Documented in Vietnamese, Chinese, Punjabi, and Athabaskan. "
                    "But the details puzzle: why do some collapses produce tone "
                    "and others not, why do tone systems then evolve in "
                    "predictable directions, and can tonogenesis run in "
                    "reverse?"),
        why_it_matters=("Tone covers half the world's languages. Its birth is "
                        "the clearest window into how sound systems reorganize."),
        sig_lens=("The Signature lens treats tonogenesis as a conservation "
                  "ledger: the Signature approach asks what happens to the "
                  "information when a consonant contrast dies."),
        sig_body=("The Signature proposal models tonogenesis as information "
                  "conservation. Assumptions: (1) consonant voicing perturbs "
                  "following vowel pitch; (2) when voicing is lost, the pitch "
                  "perturbation remains; (3) listeners reanalyze the pitch as "
                  "the contrast. Reasoning path: the proposal shows tone "
                  "emerges exactly when a redundant cue becomes the sole cue "
                  "- predicting tonogenesis should follow voicing mergers "
                  "only where the pitch perturbation was already perceptible, "
                  "which matches the documented cases. Tone is then recycled "
                  "information, not new information. Limits: the model needs "
                  "phonetic measurements of pre-tonal stages that are rarely "
                  "available."),
        pointer=('The Signature system models tonogenesis as information conservation: redundant pitch cues become the contrast when consonants merge. The Signature test: pre-merger pitch perturbations predict tonal outcomes. It would be refuted if tone emerges with no prior consonantal source.'),
        key_points=[
            "Tone emerges when consonant contrasts collapse.",
            "Documented in Vietnamese, Chinese, Punjabi, Athabaskan.",
            "Not all voicing mergers produce tone.",
            "Tone systems evolve in predictable directions afterward.",
        ],
        requirements=[
            "An account of why some mergers tone and others do not.",
            "Phonetic evidence from pre-tonal stages.",
            "An account of tone-system evolution after birth.",
        ],
        standards=[
            "Claims checked against the tonogenesis literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Haudricourt A. De l'origine des tons en vietnamien. 1954.",
            "Hombert JM et al. Development of tonal systems. 1979.",
        ],
        hypotheses=[
            "Tone is recycled redundant pitch information.",
            "Perceptual salience thresholds determine which mergers tone.",
            "Contact accelerates tonogenesis.",
            "Tone can de-tonogenize back to non-tonal systems.",
        ],
        confirm="Pre-merger pitch perturbations predict tonal outcomes.",
        refute="Tone emerges with no prior consonantal source.",
    ),
    dict(
        key="linguistics-26",
        name="Creole Genesis",
        group="Contact",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("How do creoles - full languages born in a generation from "
                 "pidgin chaos - get their grammar, and how fast can it "
                 "happen?"),
        background=("Haitian Creole, Tok Pisin, and others developed complete "
                    "grammars within decades from contact jargons. Bickerton "
                    "proposed children imposed innate bioprogram grammar; "
                    "substratists credit the grammar of enslaved peoples' "
                    "languages; gradualists argue for slower development. "
                    "Nicaraguan Sign Language showed a new language emerging "
                    "before researchers' eyes - but spoken creoles' birth "
                    "records are thinner."),
        why_it_matters=("Creoles are language creation observed in history. "
                        "Their genesis reveals the minimum ingredients of a "
                        "full language."),
        sig_lens=("The Signature lens treats creolization as a bootstrapping "
                  "ledger: the Signature approach asks what the first "
                  "generation had to work with."),
        sig_body=("The Signature proposal models creolization as iterated "
                  "learning under pressure. Assumptions: (1) pidgins provide "
                  "vocabulary with minimal grammar; (2) children regularize "
                  "and expand; (3) adult substrate languages supply "
                  "templates. Reasoning path: the proposal shows the three "
                  "sources combine - bioprogram-like defaults where input is "
                  "thinnest, substrate transfer where it is available - "
                  "predicting creole grammars should look like substrate "
                  "languages spoken with superstrate words, which matches "
                  "the best-documented cases. Speed follows from the "
                  "intensity of the communicative need. Limits: the "
                  "bioprogram-versus-substrate weights remain disputed; "
                  "birth records are incomplete."),
        pointer=('The Signature system models creolization as children regularizing pidgin input using substrate templates under communicative pressure. The Signature test: creole grammars match substrate structures systematically. It would be refuted if creoles show grammatical features from none of the inputs.'),
        key_points=[
            "Creoles developed full grammars within decades.",
            "Bioprogram, substrate, and gradualist accounts compete.",
            "Nicaraguan Sign Language showed language birth in real time.",
            "Birth records for spoken creoles are incomplete.",
        ],
        requirements=[
            "An account of the speed of grammaticalization.",
            "Weights for innate, substrate, and superstrate contributions.",
            "Consistency with the Nicaraguan Sign Language case.",
        ],
        standards=[
            "Claims checked against the creolistics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bickerton D. Roots of Language. Karoma; 1981.",
            "Mufwene SS. The Ecology of Language Evolution. Cambridge University Press; 2001.",
        ],
        hypotheses=[
            "Children regularize pidgin using substrate templates.",
            "An innate bioprogram supplies default grammar.",
            "Creolization is gradual, not single-generation.",
            "Superstrate simplification, not child creation, dominates.",
        ],
        confirm="Creole grammars match substrate structures systematically.",
        refute="Creoles show grammatical features from none of the inputs.",
    ),
    dict(
        key="linguistics-27",
        name="Why Do Pidgins Simplify",
        group="Contact",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("Why do pidgins - contact languages for trade - strip grammar "
                 "to a minimum, and what does the simplification reveal about "
                 "language's core?"),
        background=("Pidgins worldwide converge on similar simplifications: no "
                    "inflection, fixed word order, minimal phonology. Theories: "
                    "adults cannot learn complex morphology (imperfect learning), "
                    "simplification aids mutual intelligibility, or pidgins "
                    "reveal the unmarked defaults of grammar. The uniformity "
                    "across unrelated lexifiers is the striking datum."),
        why_it_matters=("Pidgins may expose language's load-bearing walls - what "
                        "remains when everything optional is stripped away."),
        sig_lens=("The Signature lens treats pidgins as a stripping ledger: the "
                  "Signature approach asks what survives when learning is "
                  "hard and need is urgent."),
        sig_body=("The Signature proposal models pidgin structure as the "
                  "intersection of learnability and need. Assumptions: (1) "
                  "adult learners acquire analytic structures more easily "
                  "than synthetic ones; (2) trade needs reference more than "
                  "nuance; (3) shared simplifications reflect shared "
                  "constraints. Reasoning path: the proposal shows pidgin "
                  "uniformity follows from universal adult-learning "
                  "bottlenecks - predicting that the stripped core (fixed "
                  "order, no inflection, analytic marking) should match what "
                  "second-language learners find easiest, which it does. "
                  "Pidgins are then natural experiments in learnability. "
                  "Limits: the model underplays the role of the specific "
                  "lexifier and substrate."),
        pointer=('The Signature system models pidgins as the intersection of adult learnability bottlenecks and trade communicative need. The Signature test: pidgin features match L2-easiest structures. It would be refuted if pidgins preserve complex morphology their learners lack.'),
        key_points=[
            "Pidgins worldwide show similar simplifications.",
            "No inflection, fixed order, minimal phonology recur.",
            "Adult learning limits are the leading explanation.",
            "The uniformity across lexifiers is the key datum.",
        ],
        requirements=[
            "An account of cross-pidgin uniformity.",
            "Consistency with second-language acquisition data.",
            "Separation of universal from lexifier-specific features.",
        ],
        standards=[
            "Claims checked against the pidgin literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bakker P. Pidgins. 2008.",
            "Siegel J. The Emergence of Pidgin and Creole Languages. Oxford University Press; 2008.",
        ],
        hypotheses=[
            "Adult learning bottlenecks determine pidgin structure.",
            "Mutual intelligibility pressure drives simplification.",
            "Pidgins reveal universal grammatical defaults.",
            "Each pidgin mainly reflects its lexifier.",
        ],
        confirm="Pidgin features match L2-easiest structures.",
        refute="Pidgins preserve complex morphology their learners lack.",
    ),
    dict(
        key="linguistics-28",
        name="Sign Language Origins",
        group="Modality",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("How do sign languages emerge - and what does their rapid "
                 "grammaticalization reveal about language in a new modality?"),
        background=("Nicaraguan Sign Language emerged among deaf children in "
                    "the 1980s, developing spatial grammar within cohorts. "
                    "Village sign languages (Al-Sayyid, Kata Kolok) arise in "
                    "high-deafness communities. Homesign systems show "
                    "individual invention. The modality is new but the "
                    "grammatical solutions converge - suggesting deep "
                    "constraints on what language must be, regardless of "
                    "channel."),
        why_it_matters=("Sign emergence is language genesis under observation. "
                        "It separates what is essential to language from what "
                        "is an accident of speech."),
        sig_lens=("The Signature lens treats sign emergence as a modality "
                  "ledger: the Signature approach asks what changes when the "
                  "channel is visual-spatial."),
        sig_body=("The Signature proposal models sign grammars as modality-"
                  "optimized solutions. Assumptions: (1) the visual channel "
                  "affords simultaneous spatial encoding; (2) learners "
                  "converge on efficient solutions; (3) cohorts accumulate "
                  "complexity. Reasoning path: the proposal shows sign "
                  "languages exploit spatial simultaneity (classifier "
                  "constructions, spatial agreement) exactly where speech "
                  "uses sequence - predicting modality-specific features "
                  "should appear first and fastest, which matches the "
                  "Nicaraguan cohorts. Language is then channel-shaped but "
                  "not channel-determined. Limits: the model needs more "
                  "village-sign data; the speed record is still short."),
        pointer=('The Signature system models sign grammars as modality-optimized solutions, with spatial simultaneity exploited first. The Signature test: modality-specific features lead in every emerging case. It would be refuted if emerging sign languages copy spoken-language structures.'),
        key_points=[
            "Nicaraguan Sign Language developed spatial grammar within cohorts.",
            "Village sign languages arise in high-deafness communities.",
            "Modality-specific features appear fastest.",
            "Grammatical convergence across independent cases is striking.",
        ],
        requirements=[
            "An account of cohort-driven grammaticalization.",
            "Separation of modality effects from universal effects.",
            "More village-sign documentation.",
        ],
        standards=[
            "Claims checked against the sign-emergence literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Senghas A, Coppola M. Children creating language. Psychological Science; 2001.",
            "Meir I et al. Emerging sign languages. 2010.",
        ],
        hypotheses=[
            "Modality optimization drives the fastest innovations.",
            "Universal grammar shapes all emerging languages equally.",
            "Cohort interaction, not modality, is the key variable.",
            "Sign languages recapitulate spoken-language evolution.",
        ],
        confirm="Modality-specific features lead in every emerging case.",
        refute="Emerging sign languages copy spoken-language structures.",
    ),
    dict(
        key="linguistics-29",
        name="The Invention of Writing: Why So Rare",
        group="Writing",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("Why was full writing invented independently only a handful of "
                 "times when speech is universal?"),
        background=("Writing emerged in Mesopotamia, Egypt, China, Mesoamerica "
                    "- and arguably nowhere else independently. Many complex "
                    "societies (Inca, with quipu) managed without it. Theories "
                    "invoke administrative need, the cognitive difficulty of "
                    "the symbol-sound insight, and the sufficiency of memory "
                    "plus tallies. The rarity is the puzzle: if writing is so "
                    "useful, why did so few invent it?"),
        why_it_matters=("Writing's rarity reveals what it really is - not a "
                        "natural extension of speech but a hard invention with "
                        "specific preconditions."),
        sig_lens=("The Signature lens treats writing as an invention ledger: "
                  "the Signature approach asks what problem was painful "
                  "enough to force the insight."),
        sig_body=("The Signature proposal models writing as a painful-need "
                  "invention. Assumptions: (1) the sound-symbol insight is "
                  "cognitively unnatural; (2) only sustained administrative "
                  "pressure justifies the invention cost; (3) partial systems "
                  "(tallies, tokens) suffice for most needs. Reasoning path: "
                  "the proposal shows pristine inventions cluster where "
                  "obligation loads exceeded token-system capacity - predicting "
                  "writing appears exactly at the administrative breaking "
                  "point, which matches the four cases. Rarity follows: few "
                  "societies hit the breaking point. Limits: ritual-first "
                  "cases (oracle bones) fit awkwardly; the cognitive-cost "
                  "claim needs testing."),
        pointer=('The Signature system models writing as appearing at the administrative breaking point where token systems fail. The Signature test: inventions track administrative-load thresholds. It would be refuted if a pristine script appears with light administration.'),
        key_points=[
            "Full writing invented independently only about four times.",
            "Complex societies like the Inca managed without it.",
            "Administrative need is the leading precondition.",
            "The sound-symbol insight may be cognitively unnatural.",
        ],
        requirements=[
            "Threshold conditions separating inventors from non-inventors.",
            "An account of ritual-first cases.",
            "A measure of the cognitive cost of the insight.",
        ],
        standards=[
            "Claims checked against the writing-origins literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Schmandt-Besserat D. How Writing Came About. University of Texas Press; 1996.",
            "Houston SD. The First Writing. Cambridge University Press; 2004.",
        ],
        hypotheses=[
            "Administrative breaking points force the invention.",
            "The cognitive insight is the bottleneck, not need.",
            "Ritual recording came first in most cases.",
            "Writing diffused too fast for more inventions.",
        ],
        confirm="Inventions track administrative-load thresholds.",
        refute="A pristine script appears with light administration.",
    ),
    dict(
        key="linguistics-30",
        name="Why Do Dialects Form",
        group="Society",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("Why does one language splinter into dialects - and what "
                 "determines whether dialects diverge into languages or "
                 "converge back?"),
        background=("Dialects form through isolation, identity marking, and "
                    "network structure; they merge through mobility, media, "
                    "and standardization. The outcomes vary wildly: Norwegian "
                    "dialects remain mutually intelligible across mountains, "
                    "while Chinese 'dialects' are mutually unintelligible. "
                    "Political will often decides what counts as a language. "
                    "No model predicts the diverge-converge balance."),
        why_it_matters=("Dialect dynamics are language change in real time - "
                        "and the politics of recognition for millions of "
                        "speakers."),
        sig_lens=("The Signature lens treats dialects as a network ledger: "
                  "the Signature approach asks who talks to whom, how "
                  "often."),
        sig_body=("The Signature proposal models dialect as network structure "
                  "made audible. Assumptions: (1) accommodation converges "
                  "speech within interaction networks; (2) weak ties spread "
                  "innovations; (3) identity marks boundaries. Reasoning path: "
                  "the proposal shows dialect boundaries should map onto "
                  "network communities - predicting isoglosses follow "
                  "interaction patterns (commuting, marriage, trade) better "
                  "than geography alone, which matches modern dialectometry. "
                  "Media convergence then follows from network rewiring. "
                  "Limits: historical networks are hard to reconstruct; "
                  "identity effects resist quantification."),
        pointer=('The Signature system models dialect boundaries as network communities, with isoglosses following interaction patterns. The Signature test: isoglosses track interaction networks better than geography. It would be refuted if sharp dialect boundaries appear with dense interaction.'),
        key_points=[
            "Dialects form through isolation, identity, and networks.",
            "Mutual intelligibility varies independently of linguistic distance.",
            "Politics often decides language versus dialect status.",
            "Modern dialectometry maps variation quantitatively.",
        ],
        requirements=[
            "Network measures predicting dialect boundaries.",
            "An account of the diverge-converge balance.",
            "Separation of linguistic from political classification.",
        ],
        standards=[
            "Claims checked against the dialectology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Chambers JK, Trudgill P. Dialectology. Cambridge University Press; 1998.",
            "Nerbonne J. Data-driven dialectology. 2009.",
        ],
        hypotheses=[
            "Interaction networks determine dialect structure.",
            "Identity marking is the primary driver.",
            "Geography dominates; networks are secondary.",
            "Media is dissolving dialects everywhere.",
        ],
        confirm="Isoglosses track interaction networks better than geography.",
        refute="Sharp dialect boundaries appear with dense interaction.",
    ),
    dict(
        key="linguistics-31",
        name="Can Endangered Languages Be Revived",
        group="Society",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("Can a dying or sleeping language be genuinely revived - and "
                 "what counts as success?"),
        background=("Hebrew is the famous success - revived from liturgical to "
                    "native language. Hawaiian, Maori, and Welsh show partial "
                    "revivals; Cornish and Manx were reconstructed from "
                    "records. But revived languages differ from their "
                    "ancestors (Modern Hebrew is not Biblical Hebrew), and "
                    "most revitalization efforts fail. The linguistics of "
                    "success versus failure is poorly understood."),
        why_it_matters=("A language dies about every two weeks. Revival is the "
                        "only answer to extinction - if it works."),
        sig_lens=("The Signature lens treats revival as a transmission ledger: "
                  "the Signature approach asks what it takes to restart "
                  "intergenerational transmission."),
        sig_body=("The Signature proposal models revival as transmission "
                  "restart. Assumptions: (1) a language lives only in "
                  "child acquisition; (2) revival needs domains of use, not "
                  "just classes; (3) identity motivation fuels the effort. "
                  "Reasoning path: the proposal shows successful revivals "
                  "(Hebrew, Hawaiian immersion) share one feature: children "
                  "acquiring the language as a living medium in schools and "
                  "homes - predicting that documentation without transmission "
                  "fails, which matches the record. The revived language will "
                  "differ from its ancestor; that is success, not failure. "
                  "Limits: the model cannot manufacture motivation; political "
                  "conditions dominate outcomes."),
        pointer=('The Signature system models revival as restarting child acquisition, predicting documentation without transmission fails. The Signature test: transmission metrics predict revival outcomes. It would be refuted if a revival succeeds with no child acquisition.'),
        key_points=[
            "Hebrew is the only full revival to native language.",
            "Hawaiian, Maori, Welsh show partial success.",
            "Revived languages differ from their ancestors.",
            "Most revitalization efforts fail.",
        ],
        requirements=[
            "Intergenerational transmission, not just documentation.",
            "Domains of real use beyond the classroom.",
            "An account of why most efforts fail.",
        ],
        standards=[
            "Claims checked against the revitalization literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hinton L, Hale K. The Green Book of Language Revitalization. Academic Press; 2001.",
            "Zuckermann G. Language Contact and Lexical Enrichment in Israeli Hebrew. 2003.",
        ],
        hypotheses=[
            "Child acquisition restart is the necessary and sufficient condition.",
            "Political autonomy determines outcomes more than method.",
            "Documentation quality is the bottleneck.",
            "Revival always produces a new language, never the old one.",
        ],
        confirm="Transmission metrics predict revival outcomes.",
        refute="A revival succeeds with no child acquisition.",
    ),
    dict(
        key="linguistics-32",
        name="Why Is Word Order the Way It Is",
        group="Typology",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("Why do languages cluster into a few word-order types (SOV, SVO...) "
                 "- and why are some orders vanishingly rare?"),
        background=("About 45 percent of languages are SOV, 42 percent SVO; OVS "
                    "and OSV are vanishingly rare. Greenberg's universals "
                    "linked order to harmony (prepositions with verb-object). "
                    "Processing explanations invoke dependency-length "
                    "minimization; historical explanations invoke branching "
                    "direction. The rare orders remain the puzzle: what "
                    "forbids them?"),
        why_it_matters=("Word order is the skeleton of syntax. Its distribution "
                        "reveals the deep constraints on how minds linearize "
                        "thought."),
        sig_lens=("The Signature lens treats word order as a processing ledger: "
                  "the Signature approach asks what orders the brain can "
                  "parse efficiently."),
        sig_body=("The Signature proposal models order as processing "
                  "optimization. Assumptions: (1) working memory is limited; "
                  "(2) keeping dependents near heads eases parsing; (3) "
                  "historical accidents get filtered by learnability. "
                  "Reasoning path: the proposal shows SOV and SVO both "
                  "minimize dependency lengths under different branching "
                  "choices, while OVS and OSV force long dependencies - "
                  "predicting the observed frequency ranking from parsing "
                  "cost alone. Rare orders are then possible but disfavored, "
                  "explaining their scarcity without forbidding them. Limits: "
                  "the model needs parsing-cost measures across diverse "
                  "structures; discourse factors also shape order."),
        pointer=('The Signature system models word-order frequencies as parsing-cost optimization, with rare orders disfavored but not forbidden. The Signature test: parsing costs predict the frequency ranking. It would be refuted if a high-cost order proves frequent and stable.'),
        key_points=[
            "SOV about 45 percent, SVO about 42 percent; OVS/OSV vanishingly rare.",
            "Greenberg's universals linked order to structural harmony.",
            "Dependency-length minimization is the leading processing account.",
            "Rare orders exist but barely.",
        ],
        requirements=[
            "A quantitative account of the frequency ranking.",
            "An explanation for rare but attested orders.",
            "Separation of processing from historical factors.",
        ],
        standards=[
            "Claims checked against the typological literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Greenberg JH. Some universals of grammar. 1963.",
            "Dryer MS. The Greenbergian word order correlations. Language; 1992.",
        ],
        hypotheses=[
            "Parsing-cost optimization determines the distribution.",
            "Historical branching direction is primary.",
            "Discourse pragmatics shapes basic order.",
            "The distribution is mostly historical accident.",
        ],
        confirm="Parsing costs predict the frequency ranking.",
        refute="A high-cost order proves frequent and stable.",
    ),
    dict(
        key="linguistics-33",
        name="Quine Indeterminacy: Can Translation Be Exact",
        group="Theory",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("Is translation between languages ever fully determinate - or "
                 "does Quine's indeterminacy show that multiple incompatible "
                 "translations always fit the evidence?"),
        background=("Quine's 'gavagai' argument: a native's utterance at a "
                    "rabbit could mean rabbit, undetached rabbit part, or "
                    "rabbit-stage - and no behavioral evidence decides. "
                    "Davidson replied with charity (assume rationality); "
                    "Chomskyans with shared UG. Machine translation's "
                    "successes suggest practical determinacy, but the "
                    "philosophical question - whether meaning is fixed by "
                    "use - remains open."),
        why_it_matters=("Indeterminacy threatens the very idea of shared meaning. "
                        "Its resolution decides what translation - human or "
                        "machine - can achieve."),
        sig_lens=("The Signature lens treats translation as a constraint "
                  "ledger: the Signature approach asks what evidence could "
                  "ever close the gap."),
        sig_body=("The Signature proposal models translation as converging "
                  "constraints. Assumptions: (1) behavioral evidence "
                  "underdetermines reference; (2) converging evidence "
                  "sources (use, inference, culture) narrow the options; "
                  "(3) practical success needs only sufficient "
                  "determinacy. Reasoning path: the proposal shows "
                  "indeterminacy is real but bounded - 'gavagai' options "
                  "collapse once the full web of use is considered, "
                  "predicting that translation indeterminacy shrinks with "
                  "corpus size and context richness. Machine translation "
                  "works because big data approximates the full web. "
                  "Limits: the philosophical residue - whether residual "
                  "indeterminacy is real or artifactual - persists."),
        pointer=('The Signature system models translation as converging constraints, with indeterminacy shrinking as evidence grows. The Signature test: translation quality tracks evidence richness monotonically. It would be refuted if incompatible translations persist at full evidence.'),
        key_points=[
            "Quine's gavagai argument shows behavioral underdetermination.",
            "Davidson and Chomsky offered rival escapes.",
            "Machine translation achieves practical determinacy.",
            "The philosophical residue persists.",
        ],
        requirements=[
            "An account of how much indeterminacy is real.",
            "Consistency with machine-translation success.",
            "A criterion for sufficient determinacy.",
        ],
        standards=[
            "Claims checked against the philosophy-of-language literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Quine WVO. Word and Object. MIT Press; 1960.",
            "Davidson D. Inquiries into Truth and Interpretation. Oxford University Press; 1984.",
        ],
        hypotheses=[
            "Indeterminacy is real but bounded and shrinking with evidence.",
            "Charity plus rationality fully determines translation.",
            "Shared biology fixes reference; indeterminacy is illusory.",
            "Radical indeterminacy holds; translation is always stipulation.",
        ],
        confirm="Translation quality tracks evidence richness monotonically.",
        refute="Incompatible translations persist at full evidence.",
    ),
    dict(
        key="linguistics-34",
        name="A Unified Theory of Language",
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can linguistics unify its warring paradigms - formal, "
                 "functional, cognitive, social - into one theory of what "
                 "language is?"),
        background=("Generative grammar, construction grammar, usage-based "
                    "linguistics, and sociolinguistics offer incompatible "
                    "pictures: language as computation, as inventory, as "
                    "habit, as social action. Each explains what the others "
                    "cannot. Unification attempts (Jackendoff's parallel "
                    "architecture, usage-based formalisms) remain "
                    "programmatic. The field's fragmentation mirrors its "
                    "subject's complexity - or its immaturity."),
        why_it_matters=("This is linguistics' capstone: the answer determines "
                        "whether the field is one science or several sharing "
                        "a name."),
        sig_lens=("The Signature lens treats the paradigms as a levels ledger: "
                  "the Signature approach asks which level each paradigm "
                  "owns."),
        sig_body=("The Signature proposal models unification as levels "
                  "integration. Assumptions: (1) language spans neural, "
                  "cognitive, social, and historical levels; (2) each "
                  "paradigm captures one level well; (3) levels interact "
                  "bidirectionally. Reasoning path: the proposal assigns "
                  "computation to the cognitive level, inventory to the "
                  "cultural level, habit to the processing level, and action "
                  "to the social level - with cultural evolution as the "
                  "bridge mechanism translating between them. Unity comes "
                  "from a shared architecture of levels, not a single "
                  "formalism. Limits: the bridge mechanisms are sketched, "
                  "not proven; partisans may reject the settlement."),
        pointer=('The Signature system assigns each paradigm its level, with cultural evolution as the bridge mechanism between them. The Signature test: bridge theories produce verified cross-level predictions. It would be refuted if level interactions prove irreducible to any architecture.'),
        key_points=[
            "Generative, construction, usage-based, and social paradigms conflict.",
            "Each explains what the others cannot.",
            "Unification attempts remain programmatic.",
            "The fragmentation may reflect the subject or the field.",
        ],
        requirements=[
            "A levels architecture assigning each paradigm its domain.",
            "Bridge mechanisms between levels.",
            "Testable predictions from the unified picture.",
        ],
        standards=[
            "Claims checked against the theoretical literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Jackendoff R. Foundations of Language. Oxford University Press; 2002.",
            "Croft W. Radical Construction Grammar. Oxford University Press; 2001.",
        ],
        hypotheses=[
            "Levels integration can unify the paradigms.",
            "The paradigms are incommensurable; no unification possible.",
            "One paradigm will absorb the others.",
            "Unification needs new mathematics, not new arguments.",
        ],
        confirm="Bridge theories produce verified cross-level predictions.",
        refute="Level interactions prove irreducible to any architecture.",
    ),
]
