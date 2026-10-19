#!/usr/bin/env python3
"""Entries for the Unsolved Musicology databases (batch 4).

34 famous open problems in musicology, ladder-ordered by accessibility.
ID prefixes: JAH-USMU- (public) and JAH-USMUS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="musicology-01",
        name="Why Music Moves Us",
        group="Psychology",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Why does music move us - producing chills, tears, and "
                 "joy from mere patterns of sound?"),
        background=("Music activates reward circuits (dopamine), "
                    "violates and fulfills expectations, and synchronizes "
                    "bodies. Yet the depth of the response - grief at a "
                    "melody, ecstasy at a chord - remains disproportionate "
                    "to the stimulus. The explanatory gap is "
                    "musicology's founding puzzle."),
        why_it_matters=("Music's power is universal. Its explanation is "
                        "the field's deepest question."),
        sig_lens=("The Signature lens treats musical emotion as an "
                  "expectation ledger: the Signature approach asks what "
                  "the music promises and delivers."),
        sig_body=("The Signature proposal models musical emotion as "
                  "expectation-dynamics. Assumptions: (1) listeners "
                  "form predictions; (2) violations and resolutions "
                  "drive arousal; (3) the reward system tags the "
                  "patterns. Reasoning path: the proposal predicts "
                  "chills should track expectation-violation points - "
                  "which the evidence supports. Music moves us because "
                  "it plays the prediction machine. Limits: the model "
                  "needs better individual-difference accounts; the "
                  "cultural learning dimension needs integrating."),
        pointer=("The Signature system models musical emotion as expectation dynamics: music moves us by playing the brain's prediction machine. The Signature test: chills track violation-resolution points. It would be refuted if emotion ignores expectation structure."),
        key_points=[
            "Music activates reward circuits.",
            "Expectation violation and fulfillment drive arousal.",
            "Chills track specific musical moments.",
            "The depth of response remains puzzling.",
        ],
        requirements=[
            "Expectation-violation mapping studies.",
            "Individual-difference accounts.",
            "Cultural-learning integration.",
        ],
        standards=[
            "Claims checked against the music-psychology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Huron D. Sweet Anticipation. MIT Press; 2006.",
            "Blood AJ, Zatorre RJ. Intensely pleasurable responses to music. PNAS; 2001.",
        ],
        hypotheses=[
            "Expectation dynamics explain musical emotion.",
            "The response is purely associative learning.",
            "Social bonding is the primary function.",
            "The puzzle is unanswerable.",
        ],
        confirm="Chills track violation-resolution points.",
        refute="Emotion ignores expectation structure.",
    ),
    dict(
        key="musicology-02",
        name="The Origins of Music",
        group="History",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Why did music evolve - sexual selection, social bonding, "
                 "or something else?"),
        background=("Darwin proposed sexual selection; modern theories "
                    "favor social bonding (synchrony builds groups) or "
                    "credible signaling. Archaeological finds (40,000-"
                    "year-old flutes) show music's antiquity but not "
                    "its function. The adaptive question remains open."),
        why_it_matters=("Music's origin explains its power. The "
                        "function determines the theory."),
        sig_lens=("The Signature lens treats origins as a function "
                  "ledger: the Signature approach asks what music does "
                  "that nothing else does."),
        sig_body=("The Signature proposal models music's origin as "
                  "bonding-through-synchrony. Assumptions: (1) "
                  "synchronized movement builds trust; (2) music "
                  "enables large-group synchrony; (3) the advantage "
                  "is collective. Reasoning path: the proposal "
                  "predicts musicality should track group-coordination "
                  "demands - which comparative evidence supports. "
                  "Music evolved to make groups cohere. Limits: the "
                  "model needs better comparative data; the sexual-"
                  "selection evidence needs weighing."),
        pointer=("The Signature system models music's origin as bonding-through-synchrony: music evolved to make groups cohere. The Signature test: musicality tracks coordination demands. It would be refuted if solitary species show equal musicality."),
        key_points=[
            "Darwin proposed sexual selection.",
            "Social-bonding theories dominate now.",
            "40,000-year-old flutes show antiquity.",
            "The adaptive function remains open.",
        ],
        requirements=[
            "Comparative synchrony studies.",
            "Group-coordination demand analyses.",
            "Sexual-selection evidence weighing.",
        ],
        standards=[
            "Claims checked against the music-origins literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mithen S. The Singing Neanderthals. Harvard University Press; 2006.",
            "Dunbar R. On the evolutionary function of song and dance. 2012.",
        ],
        hypotheses=[
            "Bonding-through-synchrony explains origins.",
            "Sexual selection drove music.",
            "Music is a spandrel of language.",
            "Multiple functions co-evolved.",
        ],
        confirm="Musicality tracks coordination demands.",
        refute="Solitary species show equal musicality.",
    ),
    dict(
        key="musicology-03",
        name="Universals in Music",
        group="Theory",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("Are there musical universals - features of all human "
                 "music - and what are they?"),
        background=("Brown and others proposed universals (octave "
                    "equivalence, phrase structure); the big "
                    "cross-cultural study (Mehr) found them thin but "
                    "real. The debate: whether universals reflect "
                    "biology or convergent function."),
        why_it_matters=("Universals reveal music's nature. Their source "
                        "determines the theory."),
        sig_lens=("The Signature lens treats universals as a "
                  "constraint ledger: the Signature approach asks what "
                  "constrains all music-making."),
        sig_body=("The Signature proposal models universals as "
                  "constraint-products. Assumptions: (1) vocal "
                  "physiology constrains singing; (2) auditory "
                  "physiology constrains hearing; (3) social "
                  "functions constrain form. Reasoning path: the "
                  "proposal predicts universals should cluster at "
                  "physiological constraints (octave, phrase length) "
                  "- which they do. Universals are then what biology "
                  "and function force, not deep grammar. Limits: the "
                  "model needs better cross-cultural data; the "
                  "function-versus-biology split needs refining."),
        pointer=('The Signature system models musical universals as constraint products: what physiology and function force on all music. The Signature test: universals cluster at constraint points. It would be refuted if universals appear without constraints.'),
        key_points=[
            "Proposed universals include octave equivalence.",
            "Cross-cultural studies find them thin but real.",
            "Biology versus convergent function is debated.",
            "The constraint question is central.",
        ],
        requirements=[
            "Expanded cross-cultural sampling.",
            "Constraint-mechanism studies.",
            "Function-versus-biology decomposition.",
        ],
        standards=[
            "Claims checked against the universals literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mehr SA et al. Universality and diversity in human song. Science; 2019.",
            "Brown S, Jordania J. Universals in the world's musics. Psychology of Music; 2013.",
        ],
        hypotheses=[
            "Constraint products explain universals.",
            "A deep musical grammar exists.",
            "Universals are illusory.",
            "Function alone explains them.",
        ],
        confirm="Universals cluster at constraint points.",
        refute="Universals appear without constraints.",
    ),
    dict(
        key="musicology-04",
        name="Absolute Music: What Does It Mean",
        group="Aesthetics",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("What does absolute music - music without words or "
                 "program - mean, if anything?"),
        background=("Hanslick said music's content is 'tonally moving "
                    "forms'; others hear narratives, emotions, or "
                    "nothing. The meaning question divides aestheticians: "
                    "formalists, expressionists, and skeptics. Whether "
                    "instrumental music means remains open."),
        why_it_matters=("Most classical music is absolute. Its meaning "
                        "determines how we listen."),
        sig_lens=("The Signature lens treats meaning as a construal "
                  "ledger: the Signature approach asks what listeners "
                  "do with the sounds."),
        sig_body=("The Signature proposal models musical meaning as "
                  "construal-dependent. Assumptions: (1) music "
                  "affords multiple construals; (2) listeners "
                  "construct meaning actively; (3) no construal is "
                  "mandatory. Reasoning path: the proposal predicts "
                  "meaning reports should vary with listener framing "
                  "- which they do. Absolute music then means what "
                  "listening makes of it: the meaning is in the "
                  "act, not the notes. Limits: the model needs better "
                  "construal studies; the composer-intention question "
                  "persists."),
        pointer=("The Signature system models absolute music's meaning as construal-dependent: meaning lives in the listening act. The Signature test: meaning reports track framing manipulations. It would be refuted if meanings prove stable across framings."),
        key_points=[
            "Hanslick: tonally moving forms.",
            "Expressionists hear emotions and narratives.",
            "Skeptics deny meaning entirely.",
            "Whether instrumental music means is open.",
        ],
        requirements=[
            "Listener-construal studies.",
            "Composer-intention analyses.",
            "An account of meaning's variability.",
        ],
        standards=[
            "Claims checked against the musical-aesthetics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hanslick E. On the Musically Beautiful. 1854.",
            "Kivy P. Music Alone. Cornell University Press; 1990.",
        ],
        hypotheses=[
            "Construal dependence explains meaning debates.",
            "Music has intrinsic expressive meaning.",
            "Music is meaningless form.",
            "The question is ill-posed.",
        ],
        confirm="Meaning reports track framing manipulations.",
        refute="Meanings prove stable across framings.",
    ),
    dict(
        key="musicology-05",
        name="The Work Concept Problem",
        group="Aesthetics",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("What is a musical work - the score, the performances, "
                 "or something else?"),
        background=("Goehr showed the work-concept is historical "
                    "(emerging around 1800); jazz, rock, and oral "
                    "traditions fit it poorly. Ontologists debate "
                    "whether works are types, classes, or fictions. "
                    "The concept's scope remains contested."),
        why_it_matters=("The work concept organizes classical music. Its "
                        "limits determine its reach."),
        sig_lens=("The Signature lens treats the work as a history "
                  "ledger: the Signature approach asks when the "
                  "concept emerged and why."),
        sig_body=("The Signature proposal models the work-concept as "
                  "historically specific. Assumptions: (1) the "
                  "concept emerged with print and concert culture; "
                  "(2) it fits notated art music; (3) other "
                  "traditions need other concepts. Reasoning path: "
                  "the proposal predicts work-talk should fail for "
                  "improvised and recorded traditions - which it "
                  "does. The concept is then a useful local tool, "
                  "not a universal ontology. Limits: the model "
                  "needs better tradition comparisons; the "
                  "digital-work question needs addressing."),
        pointer=('The Signature system models the musical work as a historically specific tool: useful for notated art music, not universal. The Signature test: work-talk fails systematically outside art music. It would be refuted if the concept applies across traditions.'),
        key_points=[
            "The work-concept emerged around 1800.",
            "Jazz, rock, and oral traditions fit poorly.",
            "Ontologists debate works' metaphysics.",
            "The concept's scope is contested.",
        ],
        requirements=[
            "Tradition-comparison studies.",
            "Digital-work analyses.",
            "An account of the concept's function.",
        ],
        standards=[
            "Claims checked against the musical-ontology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Goehr L. The Imaginary Museum of Musical Works. Oxford University Press; 1992.",
            "Davies S. Musical Works and Performances. Oxford University Press; 2001.",
        ],
        hypotheses=[
            "Historical specificity explains the concept's limits.",
            "Works are universal musical entities.",
            "The concept should be abandoned.",
            "Digital media need a new concept.",
        ],
        confirm="Work-talk fails systematically outside art music.",
        refute="The concept applies across traditions.",
    ),
    dict(
        key="musicology-06",
        name="Musical Emotion: Real or Perceived",
        group="Psychology",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Do we feel the emotions music expresses - or merely "
                 "perceive them?"),
        background=("Gabrielsson distinguished perceived from felt "
                    "emotion; Juslin's BRECVEMA model lists mechanisms. "
                    "The puzzle: sad music is perceived as sad but "
                    "felt as pleasurable. Whether felt emotion matches "
                    "perceived remains open."),
        why_it_matters=("The perceived-felt gap is emotion theory's "
                        "music case. Its resolution clarifies both."),
        sig_lens=("The Signature lens treats the gap as a mechanism "
                  "ledger: the Signature approach asks which "
                  "mechanism produces which feeling."),
        sig_body=("The Signature proposal models the gap as "
                  "mechanism-divergent. Assumptions: (1) perception "
                  "uses expressive cues; (2) feeling uses reward and "
                  "memory mechanisms; (3) the mechanisms dissociate. "
                  "Reasoning path: the proposal predicts sad music "
                  "should be perceived sad (cues) but felt pleasant "
                  "(reward, safe context) - which it is. The gap is "
                  "then normal mechanism divergence, not paradox. "
                  "Limits: the model needs better mechanism "
                  "isolation; the individual differences need "
                  "mapping."),
        pointer=('The Signature system models the perceived-felt gap as mechanism divergence: perception reads cues, feeling runs reward. The Signature test: dissociations track mechanism manipulations. It would be refuted if felt-perceived correlations prove high.'),
        key_points=[
            "Perceived and felt emotion dissociate.",
            "Sad music is perceived sad, felt pleasant.",
            "Multiple mechanisms are proposed.",
            "Whether felt matches perceived is open.",
        ],
        requirements=[
            "Mechanism-isolation studies.",
            "Individual-difference mapping.",
            "An account of the pleasure-in-sadness.",
        ],
        standards=[
            "Claims checked against the music-emotion literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Juslin PN, Vastfjall D. Emotional responses to music. Behavioral and Brain Sciences; 2008.",
            "Gabrielsson A. Emotion perceived and emotion felt. Musicae Scientiae; 2001.",
        ],
        hypotheses=[
            "Mechanism divergence explains the gap.",
            "Felt always matches perceived.",
            "The gap is measurement artifact.",
            "Context determines everything.",
        ],
        confirm="Dissociations track mechanism manipulations.",
        refute="Felt-perceived correlations prove high.",
    ),
    dict(
        key="musicology-07",
        name="Why We Like Sad Music",
        group="Psychology",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("Why do we enjoy sad music - seeking out the emotion we "
                 "avoid in life?"),
        background=("The paradox of tragedy in music: sad songs "
                    "console, move, and please. Theories: safe "
                    "context (no real threat), empathy rewards, "
                    "mood regulation, and aesthetic distance. No "
                    "single account commands consensus."),
        why_it_matters=("Sad music is hugely popular. Its pleasure "
                        "explains art's function."),
        sig_lens=("The Signature lens treats sad-music pleasure as a "
                  "safety ledger: the Signature approach asks what "
                  "the safety adds."),
        sig_body=("The Signature proposal models sad-music pleasure "
                  "as safe-sadness. Assumptions: (1) real sadness "
                  "involves threat; (2) music removes threat while "
                  "keeping feeling; (3) the feeling itself rewards. "
                  "Reasoning path: the proposal predicts sad-music "
                  "liking should track empathy and rumination traits "
                  "- which it does. We like sad music because it "
                  "lets us feel safely. Limits: the model needs "
                  "better threat-removal tests; the cultural "
                  "variation needs mapping."),
        pointer=('The Signature system models sad-music pleasure as safe sadness: feeling without threat, tracking empathy traits. The Signature test: liking tracks empathy-safety measures. It would be refuted if threat presence does not reduce liking.'),
        key_points=[
            "Sad music consoles and pleases.",
            "The paradox: seeking avoided emotions.",
            "Safe-context theories dominate.",
            "No single account commands consensus.",
        ],
        requirements=[
            "Threat-removal tests.",
            "Trait-correlation studies.",
            "Cultural-variation mapping.",
        ],
        standards=[
            "Claims checked against the sad-music literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Sachs ME et al. The pleasures of sad music. 2015.",
            "Taruffi L, Koelsch S. The paradox of music-evoked sadness. 2014.",
        ],
        hypotheses=[
            "Safe-sadness explains the pleasure.",
            "Empathy rewards drive liking.",
            "Mood regulation is the function.",
            "The paradox is overstated.",
        ],
        confirm="Liking tracks empathy-safety measures.",
        refute="Threat presence does not reduce liking.",
    ),
    dict(
        key="musicology-08",
        name="The Earworm Problem",
        group="Psychology",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Why do tunes get stuck in our heads - and what makes "
                 "some melodies stickier than others?"),
        background=("Involuntary musical imagery is near-universal; "
                    "stickiness correlates with melodic simplicity, "
                    "repetition, and recent exposure. Theories invoke "
                    "memory loops and attentional capture. The "
                    "mechanism - and why some suffer more - remains "
                    "open."),
        why_it_matters=("Earworms are music cognition's window. Their "
                        "mechanism reveals memory's workings."),
        sig_lens=("The Signature lens treats earworms as a loop ledger: "
                  "the Signature approach asks what keeps the loop "
                  "spinning."),
        sig_body=("The Signature proposal models earworms as "
                  "incomplete-processing loops. Assumptions: (1) the "
                  "brain rehearses unresolved patterns; (2) simple "
                  "repetitive melodies trigger rehearsal; (3) "
                  "completion (hearing the whole song) stops it. "
                  "Reasoning path: the proposal predicts earworms "
                  "should follow interrupted exposure - which they "
                  "do. The cure is then completion or competing "
                  "cognitive load. Limits: the model needs better "
                  "loop measures; the individual-difference question "
                  "persists."),
        pointer=('The Signature system models earworms as incomplete-processing loops: completion or cognitive load breaks them. The Signature test: earworms follow interruption manipulations. It would be refuted if complete exposure triggers equally.'),
        key_points=[
            "Involuntary musical imagery is near-universal.",
            "Stickiness tracks simplicity and repetition.",
            "Interrupted exposure triggers earworms.",
            "The mechanism remains open.",
        ],
        requirements=[
            "Loop-interruption experiments.",
            "Individual-difference studies.",
            "Cure-efficacy tests.",
        ],
        standards=[
            "Claims checked against the earworm literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Williamson VJ et al. Sticky tunes. 2012.",
            "Beaman CP, Williams TI. Earworms. 2010.",
        ],
        hypotheses=[
            "Incomplete processing explains earworms.",
            "Attentional capture is the mechanism.",
            "Memory strength alone explains it.",
            "Earworms serve a function.",
        ],
        confirm="Earworms follow interruption manipulations.",
        refute="Complete exposure triggers equally.",
    ),
    dict(
        key="musicology-09",
        name="Perfect Pitch: Nature or Nurture",
        group="Psychology",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("Is perfect pitch nature or nurture - and why is it "
                 "rarer in the West?"),
        background=("Perfect pitch correlates with early training and "
                    "tonal-language exposure; genetics contribute. "
                    "The critical-period evidence is strong. Whether "
                    "it is an ability or a learned label-memory "
                    "remains debated."),
        why_it_matters=("Perfect pitch illuminates auditory learning. "
                        "Its origins reveal critical periods."),
        sig_lens=("The Signature lens treats perfect pitch as a "
                  "labeling ledger: the Signature approach asks what "
                  "early exposure labels."),
        sig_body=("The Signature proposal models perfect pitch as "
                  "early-labeled pitch memory. Assumptions: (1) "
                  "infants can retain pitch; (2) labels (note names, "
                  "tonal categories) fix it; (3) the window closes "
                  "early. Reasoning path: the proposal predicts "
                  "perfect pitch should track early labeled exposure "
                  "- explaining the tonal-language and early-"
                  "training correlations. It is then learned "
                  "memory, not special hearing. Limits: the model "
                  "needs better genetic-contribution studies; the "
                  "adult-acquisition question persists."),
        pointer=('The Signature system models perfect pitch as early-labeled pitch memory: learned, not special hearing. The Signature test: acquisition tracks early-label measures. It would be refuted if late training produces genuine perfect pitch.'),
        key_points=[
            "Perfect pitch tracks early training and tonal language.",
            "Critical-period evidence is strong.",
            "Genetics contribute modestly.",
            "Whether it is ability or memory is debated.",
        ],
        requirements=[
            "Genetic-contribution studies.",
            "Adult-acquisition trials.",
            "Label-mechanism tests.",
        ],
        standards=[
            "Claims checked against the perfect-pitch literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Deutsch D et al. Absolute pitch among American and Chinese conservatory students. 2006.",
            "Levitin DJ. Absolute memory for musical pitch. 1994.",
        ],
        hypotheses=[
            "Early-labeled memory explains the pattern.",
            "Perfect pitch is primarily genetic.",
            "Adults can acquire it fully.",
            "It is not a unitary ability.",
        ],
        confirm="Acquisition tracks early-label measures.",
        refute="Late training produces genuine perfect pitch.",
    ),
    dict(
        key="musicology-10",
        name="Rhythm: Why We Move",
        group="Theory",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Why does rhythm make us move - and why do humans "
                 "entrain when other animals mostly do not?"),
        background=("Beat entrainment is rare in animals (some parrots, "
                    "sea lions); humans do it spontaneously. Theories: "
                    "vocal-learning linkage, social bonding, predictive "
                    "timing. The neural mechanism - and its "
                    "uniqueness - remains open."),
        why_it_matters=("Rhythm drives dance and music's social power. "
                        "Its mechanism is music's motor mystery."),
        sig_lens=("The Signature lens treats entrainment as a "
                  "prediction ledger: the Signature approach asks what "
                  "the beat lets the brain predict."),
        sig_body=("The Signature proposal models entrainment as "
                  "predictive timing. Assumptions: (1) the brain "
                  "predicts beat times; (2) prediction enables "
                  "synchronized movement; (3) vocal learning built "
                  "the circuitry. Reasoning path: the proposal "
                  "predicts entrainment should track vocal-learning "
                  "ability across species - which it does. Humans "
                  "move to rhythm because prediction machinery "
                  "meets social motivation. Limits: the model needs "
                  "better neural-mechanism data; the bonding "
                  "function needs separating."),
        pointer=('The Signature system models rhythm entrainment as predictive timing built on vocal-learning circuitry. The Signature test: entrainment tracks vocal-learning measures. It would be refuted if non-vocal learners entrain equally.'),
        key_points=[
            "Beat entrainment is rare in animals.",
            "Humans entrain spontaneously.",
            "Vocal learning correlates with entrainment.",
            "The neural mechanism remains open.",
        ],
        requirements=[
            "Cross-species entrainment studies.",
            "Neural-mechanism investigations.",
            "Bonding-function separations.",
        ],
        standards=[
            "Claims checked against the rhythm literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Patel AD et al. Experimental evidence for synchronization to a musical beat in a nonhuman animal. 2009.",
            "Large EW, Snyder JS. Pulse and meter as neural resonance. 2009.",
        ],
        hypotheses=[
            "Predictive timing explains entrainment.",
            "Vocal learning is the prerequisite.",
            "Social bonding drove the evolution.",
            "The mechanism is fully known.",
        ],
        confirm="Entrainment tracks vocal-learning measures.",
        refute="Non-vocal learners entrain equally.",
    ),
    dict(
        key="musicology-11",
        name="Consonance: Nature or Culture",
        group="Theory",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Is consonance natural - built into hearing - or "
                 "cultural convention?"),
        background=("Harmonicity theories say consonance reflects the "
                    "overtone series; cultural theories note dissonant "
                    "traditions (Balkan singing, Gamelan). Recent "
                    "work finds both: roughness perception is "
                    "biological, preferences are learned. The mix "
                    "remains contested."),
        why_it_matters=("Consonance grounds harmony. Its source "
                        "determines music theory's foundation."),
        sig_lens=("The Signature lens treats consonance as a two-part "
                  "ledger: the Signature approach asks what is heard "
                  "versus what is liked."),
        sig_body=("The Signature proposal models consonance as "
                  "perception-biological, preference-cultural. "
                  "Assumptions: (1) roughness detection is "
                  "auditory; (2) liking is learned; (3) the two "
                  "dissociate. Reasoning path: the proposal predicts "
                  "roughness judgments should be universal while "
                  "preferences vary - which the evidence supports. "
                  "Harmony theory then rests on biology for "
                  "detection, culture for valuation. Limits: the "
                  "model needs better cross-cultural preference "
                  "data; the learning mechanisms need specifying."),
        pointer=('The Signature system models consonance as biologically detected but culturally valued: roughness is heard, liking is learned. The Signature test: detection universality with preference variation. It would be refuted if preferences prove universal too.'),
        key_points=[
            "Roughness perception appears biological.",
            "Consonance preferences vary culturally.",
            "Dissonant traditions exist and thrive.",
            "The nature-culture mix is contested.",
        ],
        requirements=[
            "Cross-cultural preference studies.",
            "Learning-mechanism specifications.",
            "Detection-versus-preference separations.",
        ],
        standards=[
            "Claims checked against the consonance literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "McDermott JH et al. Indifference to dissonance in native Amazonians. Nature; 2016.",
            "Parncutt R. Harmony: A Psychoacoustical Approach. Springer; 1989.",
        ],
        hypotheses=[
            "Two-part model explains the evidence.",
            "Consonance is fully natural.",
            "Consonance is fully cultural.",
            "The distinction is unmeasurable.",
        ],
        confirm="Detection universality with preference variation.",
        refute="Preferences prove universal too.",
    ),
    dict(
        key="musicology-12",
        name="The Mozart Effect Myth",
        group="Psychology",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Was the Mozart effect real - and what does its career "
                 "teach about science communication?"),
        background=("The 1993 finding (Mozart boosts spatial reasoning) "
                    "became a parenting industry; the effect proved "
                    "small, brief, and arousal-mediated. The episode "
                    "became the case study in overhyped psychology."),
        why_it_matters=("The Mozart effect shaped parenting and policy. "
                        "Its fate calibrates science communication."),
        sig_lens=("The Signature lens treats the episode as a hype "
                  "ledger: the Signature approach asks what the "
                  "finding actually showed."),
        sig_body=("The Signature proposal models the Mozart effect as "
                  "arousal-mislabeled. Assumptions: (1) enjoyable "
                  "music raises arousal; (2) arousal aids performance "
                  "briefly; (3) Mozart was incidental. Reasoning path: "
                  "the proposal predicts any enjoyable stimulus "
                  "should work - which it does. The lesson is then "
                  "about communication: small lab effects become "
                  "parenting industries without friction. Limits: "
                  "the model needs better communication-failure "
                  "analyses; the long-term music-training effects "
                  "need separating."),
        pointer=('The Signature system models the Mozart effect as arousal mislabeled: the lesson is about science communication, not music. The Signature test: effects track arousal, not Mozart. It would be refuted if mozart outperforms matched stimuli.'),
        key_points=[
            "The 1993 finding became a parenting industry.",
            "The effect proved small and arousal-mediated.",
            "Any enjoyable stimulus works similarly.",
            "The episode is the overhype case study.",
        ],
        requirements=[
            "Communication-failure analyses.",
            "Long-term training-effect separations.",
            "An account of the industry's growth.",
        ],
        standards=[
            "Claims checked against the Mozart-effect literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rauscher FH et al. Music and spatial task performance. Nature; 1993.",
            "Pietschnig J et al. Mozart effect-Shmozart effect. Intelligence; 2010.",
        ],
        hypotheses=[
            "Arousal mislabeling explains the episode.",
            "A real Mozart-specific effect exists.",
            "The hype was harmless.",
            "Science communication is unfixable.",
        ],
        confirm="Effects track arousal, not Mozart.",
        refute="Mozart outperforms matched stimuli.",
    ),
    dict(
        key="musicology-13",
        name="Music and Memory: Why Songs Stick",
        group="Psychology",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("Why does music stick in memory - preserving songs for "
                 "decades when facts fade?"),
        background=("Melody aids text recall (the song-stuck-in-head, "
                    "Alzheimer's patients singing); theories invoke "
                    "dual encoding, emotional tagging, and motor "
                    "memory. The mechanism - and its therapeutic use - "
                    "remains open."),
        why_it_matters=("Musical memory outlasts other memory. Its "
                        "mechanism has therapeutic promise."),
        sig_lens=("The Signature lens treats musical memory as an "
                  "encoding ledger: the Signature approach asks what "
                  "music adds to the trace."),
        sig_body=("The Signature proposal models musical memory as "
                  "multiply-encoded. Assumptions: (1) melody adds "
                  "auditory-motor encoding; (2) emotion tags the "
                  "trace; (3) repetition consolidates. Reasoning path: "
                  "the proposal predicts songs should resist "
                  "dementia longer than facts - which they do. "
                  "Therapeutic use then follows the encoding: sing "
                  "what must be remembered. Limits: the model needs "
                  "better encoding-decomposition; the "
                  "Alzheimer's applications need trials."),
        pointer=('The Signature system models musical memory as multiply encoded: melody, emotion, and motor traces resist decay together. The Signature test: durability tracks encoding-multiplicity. It would be refuted if unemotional melodies persist equally.'),
        key_points=[
            "Songs outlast facts in memory.",
            "Alzheimer's patients retain singing.",
            "Melody aids text recall.",
            "The mechanism remains open.",
        ],
        requirements=[
            "Encoding-decomposition studies.",
            "Therapeutic trials.",
            "An account of the resistance to decay.",
        ],
        standards=[
            "Claims checked against the music-memory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wallace WT. Memory for music. 1994.",
            "Simmons-Stern NR et al. Music and memory in Alzheimer's. 2010.",
        ],
        hypotheses=[
            "Multiple encoding explains durability.",
            "Emotion alone explains it.",
            "Repetition alone explains it.",
            "The effect is overstated.",
        ],
        confirm="Durability tracks encoding-multiplicity.",
        refute="Unemotional melodies persist equally.",
    ),
    dict(
        key="musicology-14",
        name="The Canon Problem",
        group="History",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("Who decides the musical canon - and can it be opened "
                 "without losing coherence?"),
        background=("The classical canon is narrow (dead white European "
                    "males); expansion efforts face the coherence "
                    "question: what holds a canon together? The "
                    "politics of inclusion meet the aesthetics of "
                    "judgment. Whether canons can be just remains "
                    "open."),
        why_it_matters=("Canons shape education and performance. Their "
                        "justice determines whose music lives."),
        sig_lens=("The Signature lens treats canons as a selection "
                  "ledger: the Signature approach asks what the "
                  "selection served."),
        sig_body=("The Signature proposal models canons as "
                  "institution-serving. Assumptions: (1) canons "
                  "organized concert life and pedagogy; (2) the "
                  "selection reflected power; (3) expansion needs "
                  "new organizing principles. Reasoning path: the "
                  "proposal predicts successful expansions should "
                  "offer alternative coherences (traditions, "
                  "practices) not just additions - which the best "
                  "curricular reforms do. Open the canon by "
                  "pluralizing its principles. Limits: the model "
                  "needs better expansion evaluations; the "
                  "judgment question persists."),
        pointer=('The Signature system models canons as institution-serving: open them by pluralizing organizing principles, not just adding names. The Signature test: successful expansions offer new coherences. It would be refuted if additions alone sustain canons.'),
        key_points=[
            "The classical canon is demographically narrow.",
            "Expansion faces the coherence question.",
            "Politics meets aesthetics in the debate.",
            "Whether canons can be just is open.",
        ],
        requirements=[
            "Expansion-evaluation studies.",
            "Alternative-coherence frameworks.",
            "An account of judgment's role.",
        ],
        standards=[
            "Claims checked against the canon literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weber W. The rise of musical classics in 18th-century England. 1992.",
            "Citron M. Gender and the Musical Canon. Cambridge University Press; 1993.",
        ],
        hypotheses=[
            "Principle pluralization opens canons coherently.",
            "Canons are inherently exclusionary.",
            "Addition suffices.",
            "Judgment should be abandoned.",
        ],
        confirm="Successful expansions offer new coherences.",
        refute="Additions alone sustain canons.",
    ),
    dict(
        key="musicology-15",
        name="Authorship in Early Music",
        group="History",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Who wrote early music - and does authorship matter for "
                 "chant, troubadours, and anonymous masters?"),
        background=("Much early music is anonymous or misattributed; "
                    "the work-concept fits poorly (see "
                    "musicology-05). Yet attribution drives recording "
                    "and scholarship. Whether the authorship question "
                    "is appropriate for these repertoires remains open."),
        why_it_matters=("Attribution shapes the early-music industry. "
                        "Its appropriateness determines honest "
                        "scholarship."),
        sig_lens=("The Signature lens treats authorship as a "
                  "tradition ledger: the Signature approach asks what "
                  "the tradition valued."),
        sig_body=("The Signature proposal models early authorship as "
                  "tradition-mismatched. Assumptions: (1) many "
                  "traditions valued transmission over origination; "
                  "(2) modern scholarship imposes authorship; (3) "
                  "the imposition distorts. Reasoning path: the "
                  "proposal predicts attribution disputes should "
                  "concentrate where the tradition was collective - "
                  "which they do. Scholarship should then describe "
                  "transmission, not hunt authors. Limits: the model "
                  "needs better tradition studies; the recording "
                  "industry's needs need acknowledging."),
        pointer=('The Signature system models early authorship as tradition-mismatched: describe transmission rather than hunting authors. The Signature test: disputes concentrate in collective traditions. It would be refuted if attribution succeeds systematically.'),
        key_points=[
            "Much early music is anonymous or misattributed.",
            "Traditions valued transmission over origination.",
            "Attribution drives the recording industry.",
            "Whether authorship fits remains open.",
        ],
        requirements=[
            "Transmission-focused scholarship models.",
            "Attribution-dispute analyses.",
            "Industry-need acknowledgments.",
        ],
        standards=[
            "Claims checked against the early-music literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Goehr L. The Imaginary Museum of Musical Works. Oxford University Press; 1992.",
            "Butterfield A. Poetry and Music in Medieval France. Cambridge University Press; 2002.",
        ],
        hypotheses=[
            "Tradition mismatch explains attribution problems.",
            "Authors can be recovered with method.",
            "Anonymity is the honest answer.",
            "The industry needs authors regardless.",
        ],
        confirm="Disputes concentrate in collective traditions.",
        refute="Attribution succeeds systematically.",
    ),
    dict(
        key="musicology-16",
        name="Improvisation Versus Composition",
        group="History",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("Is improvisation composition's opposite - or its "
                 "origin and twin?"),
        background=("Western art music separated the composer from the "
                    "performer; jazz, Indian classical, and Baroque "
                    "practice blur the line. Nettl and others show "
                    "improvisation is prepared, composition is "
                    "revised improvisation. Whether the distinction "
                    "holds remains open."),
        why_it_matters=("The distinction organizes music education and "
                        "value. Its collapse reforms both."),
        sig_lens=("The Signature lens treats the pair as a time ledger: "
                  "the Signature approach asks what speed of "
                  "creation changes."),
        sig_body=("The Signature proposal models improvisation and "
                  "composition as speed-differentiated creation. "
                  "Assumptions: (1) both draw on prepared materials; "
                  "(2) time pressure changes the process; (3) the "
                  "products overlap. Reasoning path: the proposal "
                  "predicts the cognitive processes should be "
                  "largely shared - which neuroscience supports. "
                  "The distinction is then institutional (who gets "
                  "credit), not cognitive. Limits: the model needs "
                  "better process comparisons; the notation "
                  "question needs integrating."),
        pointer=('The Signature system models improvisation and composition as speed-differentiated creation: the distinction is institutional, not cognitive. The Signature test: processes overlap in neural measures. It would be refuted if distinct cognitive systems are found.'),
        key_points=[
            "Art music separated composer from performer.",
            "Many traditions blur the line.",
            "Improvisation is prepared; composition revises.",
            "Whether the distinction holds is open.",
        ],
        requirements=[
            "Cognitive-process comparisons.",
            "Institutional analyses of the split.",
            "Notation-integration studies.",
        ],
        standards=[
            "Claims checked against the improvisation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Nettl B. In the Course of Performance. University of Chicago Press; 1998.",
            "Berliner P. Thinking in Jazz. University of Chicago Press; 1994.",
        ],
        hypotheses=[
            "Speed differentiation explains the pair.",
            "The distinction is cognitively real.",
            "Improvisation is superior creation.",
            "Composition is superior creation.",
        ],
        confirm="Processes overlap in neural measures.",
        refute="Distinct cognitive systems are found.",
    ),
    dict(
        key="musicology-17",
        name="The Notation Problem",
        group="Theory",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("What does notation capture - and what does it destroy?"),
        background=("Staff notation enabled complex art music but "
                    "excludes timbre, groove, and microtonality; "
                    "oral traditions preserve what notation cannot. "
                    "Whether notation's gains exceed its losses - "
                    "and for whom - remains open."),
        why_it_matters=("Notation shapes what music can be. Its "
                        "tradeoffs determine musical possibilities."),
        sig_lens=("The Signature lens treats notation as a filter "
                  "ledger: the Signature approach asks what passes "
                  "through and what is lost."),
        sig_body=("The Signature proposal models notation as "
                  "enabling-filter. Assumptions: (1) notation "
                  "enables complexity and transmission; (2) it "
                  "filters out unnotatable parameters; (3) the "
                  "filtered parameters atrophy in literate "
                  "traditions. Reasoning path: the proposal predicts "
                  "literate traditions should be weak in groove and "
                  "timbre nuance - which they are. The answer is "
                  "then plural notation (or post-notation) for "
                  "plural musics. Limits: the model needs better "
                  "atrophy studies; the digital-notation question "
                  "needs addressing."),
        pointer=('The Signature system models notation as an enabling filter: it builds complexity while starving unnotatable parameters. The Signature test: weaknesses track notation-filtered parameters. It would be refuted if literate traditions excel in groove.'),
        key_points=[
            "Staff notation enabled complex art music.",
            "It excludes timbre, groove, microtonality.",
            "Literate traditions atrophy in filtered parameters.",
            "Whether gains exceed losses is open.",
        ],
        requirements=[
            "Atrophy studies across traditions.",
            "Plural-notation experiments.",
            "Digital-notation analyses.",
        ],
        standards=[
            "Claims checked against the notation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kerman J. Contemplating Music. Harvard University Press; 1985.",
            "Seeger C. Prescriptive and descriptive music-writing. 1958.",
        ],
        hypotheses=[
            "Enabling-filter explains notation's effects.",
            "Notation is purely beneficial.",
            "Notation damaged music.",
            "Digital tools resolve the tradeoffs.",
        ],
        confirm="Weaknesses track notation-filtered parameters.",
        refute="Literate traditions excel in groove.",
    ),
    dict(
        key="musicology-18",
        name="Tuning Systems: The Compromise",
        group="Theory",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Why did equal temperament win - and what did music lose "
                 "in the compromise?"),
        background=("Equal temperament enables modulation at the cost "
                    "of pure intervals; meantone and just systems "
                    "sound sweeter in limited keys. The victory was "
                    "practical (keyboard music, ensemble playing). "
                    "Whether the loss matters - and whether "
                    "alternatives deserve revival - remains open."),
        why_it_matters=("Tuning shapes harmony's sound. The compromise "
                        "determines what we hear."),
        sig_lens=("The Signature lens treats tuning as a compromise "
                  "ledger: the Signature approach asks what was "
                  "traded for what."),
        sig_body=("The Signature proposal models equal temperament as "
                  "modulation-bought. Assumptions: (1) pure intervals "
                  "sound better; (2) modulation needs compromise; (3) "
                  "the repertoire exploited modulation. Reasoning "
                  "path: the proposal shows the tradeoff was worth "
                  "it for the common-practice repertoire - "
                  "explaining the victory - while historically "
                  "informed performance rightly revives alternatives "
                  "for earlier music. Tuning should then be "
                  "repertoire-matched. Limits: the model needs "
                  "better perceptual studies; the contemporary-"
                  "composition question persists."),
        pointer=('The Signature system models tuning as repertoire-matched compromise: equal temperament for modulatory music, alternatives for earlier repertoires. The Signature test: preferences track repertoire-tuning fit. It would be refuted if one temperament suits all repertoires.'),
        key_points=[
            "Equal temperament enables modulation, spoils purity.",
            "Meantone and just systems sound sweeter narrowly.",
            "The victory was practical.",
            "Whether the loss matters is open.",
        ],
        requirements=[
            "Perceptual comparison studies.",
            "Repertoire-tuning fit analyses.",
            "Contemporary-composition explorations.",
        ],
        standards=[
            "Claims checked against the tuning literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Barbour JM. Tuning and Temperament. Michigan State College Press; 1951.",
            "Duffin RW. How Equal Temperament Ruined Harmony. Norton; 2007.",
        ],
        hypotheses=[
            "Repertoire matching explains tuning history.",
            "Equal temperament is optimal universally.",
            "The loss was tragic.",
            "Listeners cannot hear the difference.",
        ],
        confirm="Preferences track repertoire-tuning fit.",
        refute="One temperament suits all repertoires.",
    ),
    dict(
        key="musicology-19",
        name="Timbre: The Neglected Parameter",
        group="Theory",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("Why did music theory neglect timbre - and can it be "
                 "theorized?"),
        background=("Theory formalized pitch and rhythm; timbre remained "
                    "'tone color' - ineffable. Yet timbre drives "
                    "genre identity, emotion, and modern production. "
                    "Spectral analysis now enables description. Whether "
                    "a theory of timbre is possible remains open."),
        why_it_matters=("Timbre is music's most immediate parameter. "
                        "Its theory completes music analysis."),
        sig_lens=("The Signature lens treats timbre as a description "
                  "ledger: the Signature approach asks what became "
                  "describable."),
        sig_body=("The Signature proposal models timbre's neglect as "
                  "notation-caused. Assumptions: (1) theory followed "
                  "notation; (2) notation ignores timbre; (3) "
                  "recording made timbre manipulable. Reasoning path: "
                  "the proposal predicts timbre theory should emerge "
                  "from production practice - which it is. The "
                  "theory will then be production-based (spectral, "
                  "gestural) not score-based. Limits: the model "
                  "needs better perceptual-timbre studies; the "
                  "formalization challenge is real."),
        pointer=('The Signature system models timbre theory as emerging from production practice: spectral and gestural, not score-based. The Signature test: timbre effects yield to spectral description. It would be refuted if timbre resists systematic description.'),
        key_points=[
            "Theory formalized pitch and rhythm, not timbre.",
            "Timbre drives genre and emotion.",
            "Spectral analysis enables description.",
            "Whether timbre can be theorized is open.",
        ],
        requirements=[
            "Perceptual-timbre mapping studies.",
            "Production-based theory development.",
            "Formalization-attempt evaluations.",
        ],
        standards=[
            "Claims checked against the timbre literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Grey JM. Multidimensional perceptual scaling of musical timbres. 1977.",
            "Fales C. The paradox of timbre. Ethnomusicology; 2002.",
        ],
        hypotheses=[
            "Production-based theory will succeed.",
            "Timbre is untheorizable.",
            "Score-based extensions suffice.",
            "The neglect was justified.",
        ],
        confirm="Timbre effects yield to spectral description.",
        refute="Timbre resists systematic description.",
    ),
    dict(
        key="musicology-20",
        name="The Album Problem",
        group="Sociology",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Is the album dead - and what does its decline mean for "
                 "musical form?"),
        background=("Streaming unbundled the album into tracks; artists "
                    "debate whether the long form survives. The album "
                    "was itself a technological artifact (LP length). "
                    "Whether its passing impoverishes music or frees "
                    "it remains open."),
        why_it_matters=("The album organized popular music for decades. "
                        "Its fate shapes musical form."),
        sig_lens=("The Signature lens treats the album as a format "
                  "ledger: the Signature approach asks what the "
                  "container did to the content."),
        sig_body=("The Signature proposal models the album as "
                  "format-contingent. Assumptions: (1) the LP "
                  "length shaped the album form; (2) streaming "
                  "rewards tracks; (3) artists adapt to incentives. "
                  "Reasoning path: the proposal predicts long-form "
                  "ambition should persist where audiences reward it "
                  "- which it does (vinyl revival, concept "
                  "albums). The album is then one format among many, "
                  "not a lost golden age. Limits: the model needs "
                  "better format-effect studies; the attention-"
                  "economy question persists."),
        pointer=('The Signature system models the album as format-contingent: one container among many, persisting where audiences reward ambition. The Signature test: long forms track audience-reward measures. It would be refuted if albums thrive regardless of incentives.'),
        key_points=[
            "Streaming unbundled albums into tracks.",
            "The album was an LP-length artifact.",
            "Long-form ambition persists in niches.",
            "Whether the passing impoverishes remains open.",
        ],
        requirements=[
            "Format-effect studies.",
            "Audience-reward analyses.",
            "Attention-economy investigations.",
        ],
        standards=[
            "Claims checked against the popular-music literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Shuker R. Understanding Popular Music. Routledge; 2001.",
            "Marshall L. The sociology of popular music. 2011.",
        ],
        hypotheses=[
            "Format contingency explains the album's career.",
            "The album's death impoverishes music.",
            "Tracks liberate musicians.",
            "Formats do not matter much.",
        ],
        confirm="Long forms track audience-reward measures.",
        refute="Albums thrive regardless of incentives.",
    ),
    dict(
        key="musicology-21",
        name="Popular Versus Classical: The Divide",
        group="Sociology",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Is the popular-classical divide real - or an "
                 "institutional fiction?"),
        background=("The divide organizes education, funding, and "
                    "prestige; musicians increasingly cross it. "
                    "Historians show it is recent (19th century). "
                    "Whether the distinction tracks anything musical "
                    "or only social remains open."),
        why_it_matters=("The divide allocates prestige and money. Its "
                        "reality determines cultural policy."),
        sig_lens=("The Signature lens treats the divide as an "
                  "institution ledger: the Signature approach asks "
                  "what the boundary does."),
        sig_body=("The Signature proposal models the divide as "
                  "institutional. Assumptions: (1) the musical "
                  "differences are gradients; (2) institutions "
                  "harden them into kinds; (3) crossing is "
                  "increasing. Reasoning path: the proposal predicts "
                  "the boundary should track funding and education "
                  "structures - which it does. The divide is then "
                  "real as social fact, fictional as musical fact. "
                  "Limits: the model needs better gradient studies; "
                  "the prestige economy needs analyzing."),
        pointer=('The Signature system models the popular-classical divide as institutional: real as social fact, fictional as musical fact. The Signature test: boundaries track institutional measures. It would be refuted if musical analysis sustains the divide.'),
        key_points=[
            "The divide organizes funding and prestige.",
            "Musicians increasingly cross it.",
            "Historians date it to the 19th century.",
            "Whether it tracks anything musical is open.",
        ],
        requirements=[
            "Musical-gradient studies.",
            "Institutional-boundary analyses.",
            "Prestige-economy investigations.",
        ],
        standards=[
            "Claims checked against the popular-music literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weber W. Music and the Middle Class. 1975.",
            "Levine LW. Highbrow/Lowbrow. Harvard University Press; 1988.",
        ],
        hypotheses=[
            "Institutional hardening explains the divide.",
            "The divide tracks real musical differences.",
            "The divide is dissolving.",
            "The divide serves necessary functions.",
        ],
        confirm="Boundaries track institutional measures.",
        refute="Musical analysis sustains the divide.",
    ),
    dict(
        key="musicology-22",
        name="Music and Identity",
        group="Sociology",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("How does music shape identity - and does our taste "
                 "reveal or construct who we are?"),
        background=("Subcultures form around music; taste correlates "
                    "with personality and politics. The causal "
                    "direction - selection versus socialization - is "
                    "debated. Whether music expresses or makes "
                    "identity remains open."),
        why_it_matters=("Music-identity links shape social life. Their "
                        "direction determines the theory."),
        sig_lens=("The Signature lens treats identity as a badge "
                  "ledger: the Signature approach asks what the "
                  "taste signals."),
        sig_body=("The Signature proposal models music-identity as "
                  "bidirectional. Assumptions: (1) people select "
                  "music fitting identity; (2) music socializes "
                  "identity in groups; (3) both operate. Reasoning "
                  "path: the proposal predicts selection should "
                  "dominate individually and socialization in "
                  "subcultures - which the evidence supports. Taste "
                  "then both reveals and constructs. Limits: the "
                  "model needs better causal studies; the "
                  "streaming-personalization effect needs studying."),
        pointer=('The Signature system models music-identity as bidirectional: selection reveals, subcultures construct. The Signature test: effects split by individual-versus-group level. It would be refuted if one direction explains all links.'),
        key_points=[
            "Subcultures form around musical taste.",
            "Taste correlates with personality and politics.",
            "Selection versus socialization is debated.",
            "Whether music expresses or makes identity is open.",
        ],
        requirements=[
            "Causal-direction studies.",
            "Subculture-socialization research.",
            "Streaming-personalization effects.",
        ],
        standards=[
            "Claims checked against the music-sociology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Frith S. Performing Rites. Harvard University Press; 1996.",
            "Rentfrow PJ, Gosling SD. The do re mi's of everyday life. 2003.",
        ],
        hypotheses=[
            "Bidirectionality explains the links.",
            "Selection dominates.",
            "Socialization dominates.",
            "The links are spurious.",
        ],
        confirm="Effects split by individual-versus-group level.",
        refute="One direction explains all links.",
    ),
    dict(
        key="musicology-23",
        name="The Cover Song Question",
        group="Sociology",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("What is a cover - tribute, theft, or new work?"),
        background=("Covers range from faithful to transformative; law "
                    "treats them as licensed copies, artists as "
                    "interpretations. The ontology (see "
                    "musicology-05) and the economics (who profits) "
                    "both complicate. Whether covers are derivative "
                    "or original remains open."),
        why_it_matters=("Covers are a huge musical practice. Their "
                        "status determines credit and pay."),
        sig_lens=("The Signature lens treats covers as a "
                  "transformation ledger: the Signature approach asks "
                  "what the cover adds."),
        sig_body=("The Signature proposal models covers as "
                  "transformation-graded. Assumptions: (1) covers "
                  "vary in transformation; (2) the value added "
                  "varies with it; (3) law ignores the gradient. "
                  "Reasoning path: the proposal predicts cultural "
                  "and economic credit should track transformation "
                  "- which informal norms do. The law is then "
                  "cruder than the practice. Limits: the model "
                  "needs better transformation measures; the "
                  "licensing reform question persists."),
        pointer=('The Signature system models covers as transformation-graded: credit should track what the cover adds. The Signature test: credit tracks transformation measures. It would be refuted if audiences treat all covers equally.'),
        key_points=[
            "Covers range from faithful to transformative.",
            "Law treats them as licensed copies.",
            "Artists treat them as interpretations.",
            "Whether they are derivative or original is open.",
        ],
        requirements=[
            "Transformation measures.",
            "Credit-attribution studies.",
            "Licensing-reform analyses.",
        ],
        standards=[
            "Claims checked against the popular-music literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Plasketes G. Play It Again: Cover Songs in Popular Music. Ashgate; 2010.",
            "Mosser K. Cover songs. 2008.",
        ],
        hypotheses=[
            "Transformation grading captures cover value.",
            "Covers are inherently derivative.",
            "Great covers are original works.",
            "The law handles covers fine.",
        ],
        confirm="Credit tracks transformation measures.",
        refute="Audiences treat all covers equally.",
    ),
    dict(
        key="musicology-24",
        name="AI Composition: Is It Music",
        group="Technology",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Is AI-generated music really music - and who is the "
                 "composer?"),
        background=("AI systems compose convincingly; the questions "
                    "multiply: authorship, authenticity, and whether "
                    "machine output counts as music. Listeners often "
                    "cannot tell. Whether the composer matters to the "
                    "music remains open."),
        why_it_matters=("AI composition reshapes musical labor and "
                        "meaning. Its status determines the industry."),
        sig_lens=("The Signature lens treats AI music as a reception "
                  "ledger: the Signature approach asks what changes "
                  "when the composer is known to be a machine."),
        sig_body=("The Signature proposal models AI music's status as "
                  "reception-dependent. Assumptions: (1) the sounds "
                  "can be indistinguishable; (2) knowledge of "
                  "machine origin changes reception; (3) the change "
                  "is about meaning, not sound. Reasoning path: the "
                  "proposal predicts devaluation should track "
                  "origin-knowledge - which experiments confirm. AI "
                  "music is then music with a meaning deficit, not a "
                  "sound deficit. Limits: the model needs better "
                  "reception studies; the labor questions need "
                  "separate treatment."),
        pointer=('The Signature system models AI music as reception-dependent: indistinguishable sound with a meaning deficit. The Signature test: valuation tracks origin-knowledge. It would be refuted if origin knowledge shows no effect.'),
        key_points=[
            "AI composes convincingly.",
            "Listeners often cannot distinguish.",
            "Knowledge of machine origin changes reception.",
            "Authorship and labor questions multiply.",
        ],
        requirements=[
            "Origin-knowledge reception experiments.",
            "Labor-impact studies.",
            "An account of the meaning deficit.",
        ],
        standards=[
            "Claims checked against the AI-music literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Briot JP et al. Deep Learning Techniques for Music Generation. Springer; 2020.",
            "Moffat DC, Kelly M. An investigation into people's bias against computational creativity. 2006.",
        ],
        hypotheses=[
            "Reception dependence explains AI music's status.",
            "AI music is fully music.",
            "AI music is not music.",
            "The question will dissolve with familiarity.",
        ],
        confirm="Valuation tracks origin-knowledge.",
        refute="Origin knowledge shows no effect.",
    ),
    dict(
        key="musicology-25",
        name="The Copyright Problem in Music",
        group="Technology",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("Can copyright handle musical borrowing - sampling, "
                 "interpolation, and the blurry line of influence?"),
        background=("The 'Blurred Lines' verdict chilled songwriting; "
                    "sampling law is a thicket. Music has always "
                    "borrowed; the law draws lines the practice "
                    "ignores. Whether the system can be fixed remains "
                    "open."),
        why_it_matters=("Copyright shapes what musicians dare. Its fit "
                        "determines creative freedom."),
        sig_lens=("The Signature lens treats copyright as a borrowing "
                  "ledger: the Signature approach asks what the "
                  "practice needs."),
        sig_body=("The Signature proposal models music copyright as "
                  "practice-mismatched. Assumptions: (1) borrowing "
                  "is constitutive of music; (2) the law treats it "
                  "as exceptional; (3) chilling effects are real. "
                  "Reasoning path: the proposal predicts the law "
                  "should distinguish transformative borrowing from "
                  "mere copying - which it does poorly. Reform is "
                  "then borrowing-tolerant rules (wider fair use, "
                  "compulsory licenses). Limits: the model needs "
                  "better chilling-effect studies; the compensation "
                  "question needs solving."),
        pointer=('The Signature system models music copyright as practice-mismatched: reform toward borrowing-tolerant rules. The Signature test: chilling tracks legal-uncertainty measures. It would be refuted if songwriters ignore the legal risk.'),
        key_points=[
            "The 'Blurred Lines' verdict chilled songwriting.",
            "Sampling law is a thicket.",
            "Borrowing is constitutive of musical practice.",
            "Whether the system can be fixed is open.",
        ],
        requirements=[
            "Chilling-effect studies.",
            "Borrowing-tolerance reform designs.",
            "Compensation-mechanism solutions.",
        ],
        standards=[
            "Claims checked against the music-copyright literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Arewa OB. From J.C. Bach to hip hop. 2006.",
            "Schumacher TG. This is a sampling sport. 1995.",
        ],
        hypotheses=[
            "Practice mismatch explains the dysfunction.",
            "Strong copyright protects creators.",
            "Borrowing tolerance harms originators.",
            "Compulsory licensing solves it.",
        ],
        confirm="Chilling tracks legal-uncertainty measures.",
        refute="Songwriters ignore the legal risk.",
    ),
    dict(
        key="musicology-26",
        name="Streaming: What It Did to Music",
        group="Sociology",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("What did streaming do to music - democratize, "
                 "impoverish, or transform it?"),
        background=("Streaming pays fractions of pennies; it also "
                    "gave global distribution to all. Song lengths "
                    "shrank, intros shortened (skip rates), and "
                    "playlists replaced albums. Whether the net "
                    "effect is good remains fiercely debated."),
        why_it_matters=("Streaming is music's economy. Its effects "
                        "determine musicians' livelihoods."),
        sig_lens=("The Signature lens treats streaming as an "
                  "incentive ledger: the Signature approach asks what "
                  "the payment model rewards."),
        sig_body=("The Signature proposal models streaming effects "
                  "as incentive-driven. Assumptions: (1) per-stream "
                  "payments reward quantity and skip-avoidance; (2) "
                  "artists adapt songcraft; (3) the long tail "
                  "benefits obscure artists. Reasoning path: the "
                  "proposal predicts songcraft should shift toward "
                  "streaming incentives - which it has (shorter "
                  "songs, quick hooks). The system is then neither "
                  "pure democratization nor pure exploitation but "
                  "incentive-shaped. Limits: the model needs better "
                  "payment-fairness analyses; the cultural effects "
                  "need longer study."),
        pointer=('The Signature system models streaming as incentive-shaped: per-stream payments reshape songcraft while democratizing distribution. The Signature test: songcraft tracks payment-incentive measures. It would be refuted if songcraft ignores streaming incentives.'),
        key_points=[
            "Streaming pays fractions of pennies per play.",
            "Global distribution became universal.",
            "Songs shortened; intros vanished.",
            "Whether the net effect is good is fiercely debated.",
        ],
        requirements=[
            "Payment-fairness analyses.",
            "Songcraft-change studies.",
            "Long-tail benefit quantifications.",
        ],
        standards=[
            "Claims checked against the streaming literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hesmondhalgh D. Streaming's effects on music culture. 2020.",
            "MaasO. The economics of music streaming. 2021.",
        ],
        hypotheses=[
            "Incentive shaping explains streaming's effects.",
            "Streaming democratized music.",
            "Streaming impoverished musicians.",
            "User-centric payments fix the fairness.",
        ],
        confirm="Songcraft tracks payment-incentive measures.",
        refute="Songcraft ignores streaming incentives.",
    ),
    dict(
        key="musicology-27",
        name="The Live Music Problem",
        group="Sociology",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("Why is live music simultaneously booming and broken - "
                 "record revenues alongside artist struggles?"),
        background=("Concert revenues hit records while mid-tier "
                    "artists struggle with costs; dynamic pricing "
                    "angers fans; festivals consolidate. The "
                    "paradox: the top thrives, the middle vanishes. "
                    "Whether the market is healthy remains open."),
        why_it_matters=("Live music is musicians' main income. Its "
                        "structure determines careers."),
        sig_lens=("The Signature lens treats live music as a "
                  "concentration ledger: the Signature approach asks "
                  "where the money goes."),
        sig_body=("The Signature proposal models live music as "
                  "winner-take-all. Assumptions: (1) demand "
                  "concentrates on stars; (2) costs (travel, crew) "
                  "hit mid-tier hardest; (3) platforms amplify "
                  "concentration. Reasoning path: the proposal "
                  "predicts the middle should hollow - which it "
                  "has. The market is then efficient for fans of "
                  "stars, broken as a career ladder. Limits: the "
                  "model needs better cost studies; the policy "
                  "responses need developing."),
        pointer=('The Signature system models live music as winner-take-all: efficient for star fans, broken as a career ladder. The Signature test: outcomes track concentration measures. It would be refuted if mid-tier thrives equally.'),
        key_points=[
            "Concert revenues hit records.",
            "Mid-tier artists struggle with costs.",
            "Dynamic pricing angers fans.",
            "Whether the market is healthy is open.",
        ],
        requirements=[
            "Cost-structure studies by tier.",
            "Concentration measures over time.",
            "Policy-response development.",
        ],
        standards=[
            "Claims checked against the live-music literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Krueger AB. Rockonomics. Currency; 2019.",
            "Connolly M, Krueger AB. Rockonomics: the economics of popular music. 2006.",
        ],
        hypotheses=[
            "Winner-take-all explains the paradox.",
            "The market is healthy overall.",
            "Costs will adjust downward.",
            "Streaming caused the concentration.",
        ],
        confirm="Outcomes track concentration measures.",
        refute="Mid-tier thrives equally.",
    ),
    dict(
        key="musicology-28",
        name="Music Therapy: Does It Work",
        group="Psychology",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Does music therapy work - and for what, specifically?"),
        background=("Trials show benefits for depression, autism, "
                    "dementia, and pain; but blinding is hard, "
                    "controls are weak, and mechanisms are vague. "
                    "Whether the effects are music-specific or "
                    "social-attention effects remains open."),
        why_it_matters=("Music therapy is widely practiced. Its "
                        "specificity determines its prescription."),
        sig_lens=("The Signature lens treats therapy as a mechanism "
                  "ledger: the Signature approach asks what the music "
                  "adds beyond attention."),
        sig_body=("The Signature proposal models music-therapy "
                  "effects as partly specific. Assumptions: (1) "
                  "social attention explains some benefits; (2) "
                  "rhythm and melody add motor and memory effects; "
                  "(3) the mix varies by condition. Reasoning path: "
                  "the proposal predicts music-specific effects "
                  "where rhythm entrains movement or melody cues "
                  "memory - which the evidence supports. Therapy is "
                  "then genuinely musical for some indications. "
                  "Limits: the model needs better controlled trials; "
                  "the mechanism mapping needs completing."),
        pointer=('The Signature system models music therapy as partly music-specific: rhythm and melody add real effects beyond social attention. The Signature test: effects persist with attention controlled. It would be refuted if no music-specific effect is found.'),
        key_points=[
            "Trials show benefits across conditions.",
            "Blinding and controls are weak.",
            "Mechanisms are vaguely specified.",
            "Whether effects are music-specific is open.",
        ],
        requirements=[
            "Better-controlled trials.",
            "Mechanism-mapping studies.",
            "Indication-specific evaluations.",
        ],
        standards=[
            "Claims checked against the music-therapy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bradt J et al. Music interventions for anxiety. Cochrane; 2013.",
            "Sihvonen AJ et al. Music-based interventions in neurological rehabilitation. 2017.",
        ],
        hypotheses=[
            "Partial specificity explains the evidence.",
            "All effects are social attention.",
            "Music is uniquely therapeutic.",
            "The field is pseudoscientific.",
        ],
        confirm="Effects persist with attention controlled.",
        refute="No music-specific effect is found.",
    ),
    dict(
        key="musicology-29",
        name="The Evolution of Musical Style",
        group="History",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("Why do musical styles evolve - and can the evolution "
                 "be modeled?"),
        background=("Styles change through influence, technology, and "
                    "social forces; computational studies now trace "
                    "lineages (the 'evolution' of pop). Whether "
                    "style change follows Darwinian dynamics or "
                    "other logics remains open."),
        why_it_matters=("Style evolution is music history's engine. Its "
                        "logic determines the field's theory."),
        sig_lens=("The Signature lens treats style as a transmission "
                  "ledger: the Signature approach asks what gets "
                  "copied and why."),
        sig_body=("The Signature proposal models style evolution as "
                  "biased transmission. Assumptions: (1) musicians "
                  "copy selectively; (2) biases (prestige, novelty, "
                  "function) shape copying; (3) technology changes "
                  "the fidelity. Reasoning path: the proposal "
                  "predicts stylistic lineages should track "
                  "transmission biases - which computational studies "
                  "confirm. Evolution is then cultural-evolutionary, "
                  "not strictly Darwinian. Limits: the model needs "
                  "better bias measures; the intentionality question "
                  "persists."),
        pointer=('The Signature system models style evolution as biased cultural transmission: track what gets copied and why. The Signature test: lineages track bias measures. It would be refuted if style change shows no transmission pattern.'),
        key_points=[
            "Styles change through influence and technology.",
            "Computational studies trace lineages.",
            "Whether Darwinian dynamics apply is debated.",
            "The logic of change remains open.",
        ],
        requirements=[
            "Transmission-bias measures.",
            "Computational lineage studies.",
            "Intentionality analyses.",
        ],
        standards=[
            "Claims checked against the cultural-evolution literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Savage PE. Cultural evolution of music. 2019.",
            "Mauch M et al. The evolution of popular music. Royal Society Open Science; 2015.",
        ],
        hypotheses=[
            "Biased transmission explains style evolution.",
            "Darwinian selection applies strictly.",
            "Great individuals drive change.",
            "Technology determines style.",
        ],
        confirm="Lineages track bias measures.",
        refute="Style change shows no transmission pattern.",
    ),
    dict(
        key="musicology-30",
        name="Lost Music: What We Cannot Hear",
        group="History",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("How much music is lost - and can we reconstruct what "
                 "we cannot hear?"),
        background=("Most music ever made vanished (no notation, no "
                    "recording); reconstructions of ancient music are "
                    "educated guesses. The question: whether "
                    "reconstruction is scholarship or fiction - and "
                    "what the losses mean for music history."),
        why_it_matters=("Lost music is history's silence. "
                        "Reconstruction's honesty determines its value."),
        sig_lens=("The Signature lens treats loss as an evidence "
                  "ledger: the Signature approach asks what the "
                  "fragments support."),
        sig_body=("The Signature proposal models reconstruction as "
                  "evidence-graded. Assumptions: (1) fragments "
                  "support limited inferences; (2) the gaps invite "
                  "imagination; (3) honesty needs grading. "
                  "Reasoning path: the proposal predicts "
                  "reconstructions should be presented with "
                  "uncertainty grades - which the best scholarship "
                  "does. The losses then humble music history: we "
                  "study the surviving fraction. Limits: the model "
                  "needs better grading standards; the "
                  "imagination's role needs acknowledging."),
        pointer=('The Signature system models reconstruction as evidence-graded: present uncertainty honestly; remember we study the surviving fraction. The Signature test: best work grades uncertainty explicitly. It would be refuted if reconstructions prove accurate.'),
        key_points=[
            "Most music ever made vanished.",
            "Reconstructions are educated guesses.",
            "Whether reconstruction is scholarship or fiction is debated.",
            "The losses humble music history.",
        ],
        requirements=[
            "Uncertainty-grading standards.",
            "Fragment-evidence analyses.",
            "An account of imagination's role.",
        ],
        standards=[
            "Claims checked against the historical-performance literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "West ML. Ancient Greek Music. Oxford University Press; 1992.",
            "Hagel S. Ancient Greek Music: A New Technical History. Cambridge University Press; 2009.",
        ],
        hypotheses=[
            "Evidence grading disciplines reconstruction.",
            "Reconstruction is fiction.",
            "Enough survives for confident history.",
            "The losses do not matter.",
        ],
        confirm="Best work grades uncertainty explicitly.",
        refute="Reconstructions prove accurate.",
    ),
    dict(
        key="musicology-31",
        name="The Future of the Orchestra",
        group="Sociology",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("Does the orchestra have a future - or is it a museum "
                 "sustained by subsidy?"),
        background=("Audiences age, costs rise, and relevance is "
                    "questioned; yet orchestras innovate (film scores, "
                    "education, new venues). Whether the institution "
                    "adapts or declines remains open."),
        why_it_matters=("Orchestras are classical music's flagship. "
                        "Their fate determines the tradition."),
        sig_lens=("The Signature lens treats the orchestra as a "
                  "relevance ledger: the Signature approach asks what "
                  "only orchestras provide."),
        sig_body=("The Signature proposal models the orchestra's "
                  "future as relevance-dependent. Assumptions: (1) "
                  "the orchestral sound is irreproducible; (2) "
                  "relevance needs community connection; (3) the "
                  "museum model decays. Reasoning path: the proposal "
                  "predicts survival where orchestras embed locally "
                  "- which the thriving cases show. The future is "
                  "then civic, not canonical. Limits: the model "
                  "needs better embedding measures; the funding "
                  "question persists."),
        pointer=("The Signature system models the orchestra's future as civic: survive through community embedding, not canonical preservation. The Signature test: survival tracks embedding measures. It would be refuted if isolated orchestras thrive equally."),
        key_points=[
            "Audiences age and costs rise.",
            "Orchestras are innovating in response.",
            "The orchestral sound is irreproducible.",
            "Whether the institution adapts is open.",
        ],
        requirements=[
            "Community-embedding measures.",
            "Innovation-outcome studies.",
            "Funding-model analyses.",
        ],
        standards=[
            "Claims checked against the orchestral literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Boerner S, Krause DE. Managing the symphony orchestra. 2002.",
            "Kaiser MM. The Art of the Turnaround. Brandeis University Press; 2008.",
        ],
        hypotheses=[
            "Civic embedding explains survival.",
            "The orchestra is doomed.",
            "Subsidy sustains it indefinitely.",
            "Only the canon matters.",
        ],
        confirm="Survival tracks embedding measures.",
        refute="Isolated orchestras thrive equally.",
    ),
    dict(
        key="musicology-32",
        name="Notation After the Digital Turn",
        group="Technology",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("What becomes of notation after the digital turn - "
                 "when the recording is the score?"),
        background=("DAWs made the recording the primary text; "
                    "notation software serves a shrinking art-music "
                    "niche. New notations (graphic, interactive) "
                    "proliferate. Whether notation survives as a "
                    "general tool or becomes a specialty remains open."),
        why_it_matters=("Notation's fate shapes musical literacy. Its "
                        "future determines what musicians learn."),
        sig_lens=("The Signature lens treats notation as a medium "
                  "ledger: the Signature approach asks what each "
                  "medium does best."),
        sig_body=("The Signature proposal models post-digital notation "
                  "as medium-plural. Assumptions: (1) recordings "
                  "capture what notation cannot; (2) notation "
                  "enables what recordings cannot (analysis, "
                  "complex transmission); (3) each persists where "
                  "superior. Reasoning path: the proposal predicts "
                  "notation should survive for analysis and complex "
                  "coordination - which it does. The future is then "
                  "plural media, not notation's death. Limits: the "
                  "model needs better medium-comparison studies; "
                  "the literacy question persists."),
        pointer=('The Signature system models post-digital notation as medium-plural: recordings and notation persist where each is superior. The Signature test: notation persists in analysis-coordination niches. It would be refuted if notation vanishes from practice.'),
        key_points=[
            "DAWs made recordings the primary text.",
            "Notation serves analysis and complex coordination.",
            "New notations proliferate.",
            "Whether notation survives generally is open.",
        ],
        requirements=[
            "Medium-comparison studies.",
            "Literacy-outcome research.",
            "New-notation evaluations.",
        ],
        standards=[
            "Claims checked against the notation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Magnusson T. Sonic Writing. Bloomsbury; 2019.",
            "Kerman J. Contemplating Music. Harvard University Press; 1985.",
        ],
        hypotheses=[
            "Medium pluralism describes the future.",
            "Notation is dying.",
            "Notation will be revived digitally.",
            "Recordings suffice for all purposes.",
        ],
        confirm="Notation persists in analysis-coordination niches.",
        refute="Notation vanishes from practice.",
    ),
    dict(
        key="musicology-33",
        name="The Ontology of Recorded Music",
        group="Aesthetics",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("What is a recording - document of a performance, or the "
                 "work itself?"),
        background=("Recordings began as documents; studio production "
                    "made them constructions. Gracyk argued rock "
                    "recordings are the works. The ontology affects "
                    "authorship, authenticity, and live-versus-"
                    "recorded value. Whether recordings are works "
                    "remains open."),
        why_it_matters=("Recordings are how most hear music. Their "
                        "ontology determines musical reality."),
        sig_lens=("The Signature lens treats recordings as a "
                  "production ledger: the Signature approach asks how "
                  "the sounds were made."),
        sig_body=("The Signature proposal models recording ontology "
                  "as production-dependent. Assumptions: (1) "
                  "documentary recordings point to performances; (2) "
                  "constructed recordings are the musical objects; "
                  "(3) the distinction matters. Reasoning path: the "
                  "proposal predicts rock/pop recordings should "
                  "function as works - which they do (covers copy "
                  "recordings, not scores). The ontology is then "
                  "genre-relative. Limits: the model needs better "
                  "genre comparisons; the live-authenticity question "
                  "persists."),
        pointer=('The Signature system models recording ontology as production-dependent: constructed recordings are the works in studio genres. The Signature test: work-status tracks construction measures. It would be refuted if listeners treat all recordings as documents.'),
        key_points=[
            "Recordings began as documents.",
            "Studio production made them constructions.",
            "Covers copy recordings, not scores.",
            "Whether recordings are works is open.",
        ],
        requirements=[
            "Genre-relative ontology studies.",
            "Production-process analyses.",
            "Live-versus-recorded value research.",
        ],
        standards=[
            "Claims checked against the recording literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Gracyk T. Rhythm and Noise. Duke University Press; 1996.",
            "Eisenberg E. The Recording Angel. Yale University Press; 2005.",
        ],
        hypotheses=[
            "Production dependence explains recording status.",
            "All recordings are documents.",
            "All recordings are works.",
            "The distinction does not matter.",
        ],
        confirm="Work-status tracks construction measures.",
        refute="Listeners treat all recordings as documents.",
    ),
    dict(
        key="musicology-34",
        name="A Unified Theory of Music",
        group="Aesthetics",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can musicology unify - psychology, history, theory, "
                 "and sociology - into one account of music?"),
        background=("Each subfield captures something: psychology the "
                    "hearing, history the change, theory the "
                    "structure, sociology the use. Unification attempts "
                    "remain programmatic. Whether music's nature "
                    "permits one theory is the discipline's capstone."),
        why_it_matters=("This is musicology's capstone: the answer "
                        "determines what music is."),
        sig_lens=("The Signature lens treats the subfields as a "
                  "question ledger: the Signature approach asks what "
                  "question each owns."),
        sig_body=("The Signature proposal models unification as "
                  "question-integration. Assumptions: (1) music spans "
                  "hearing, structure, history, and use; (2) each "
                  "subfield owns questions; (3) the questions "
                  "interlock. Reasoning path: the proposal assigns "
                  "psychology to hearing, theory to structure, "
                  "history to change, sociology to use - with "
                  "musical practice as the integrator. Unity comes "
                  "from the practice that holds the questions "
                  "together. Limits: the integration is sketched; "
                  "partisans may reject the settlement."),
        pointer=('The Signature system assigns each subfield its questions about music, with musical practice as the integrator. The Signature test: integrated models predict across questions. It would be refuted if questions prove irreducible to common theory.'),
        key_points=[
            "Four subfields offer incompatible images of music.",
            "Each captures what the others miss.",
            "Unification attempts remain programmatic.",
            "Whether one theory is possible is foundational.",
        ],
        requirements=[
            "A question architecture for the subfields.",
            "An account of question interlock.",
            "Testable implications of the integration.",
        ],
        standards=[
            "Claims checked against the musicological literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kerman J. Contemplating Music. Harvard University Press; 1985.",
            "Cook N, Everist M. Rethinking Music. Oxford University Press; 1999.",
        ],
        hypotheses=[
            "Question-integration unifies musicology.",
            "The subfields are incommensurable.",
            "One subfield will absorb the rest.",
            "Pluralism is permanent.",
        ],
        confirm="Integrated models predict across questions.",
        refute="Questions prove irreducible to common theory.",
    ),
]
