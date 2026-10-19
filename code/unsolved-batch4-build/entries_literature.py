#!/usr/bin/env python3
"""Entries for the Unsolved Literature databases (batch 4).

34 famous open problems in literary studies, ladder-ordered by accessibility.
ID prefixes: JAH-USLT- (public) and JAH-USLTS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="literature-01",
        name="Why We Tell Stories",
        group="Theory",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Why do humans tell stories - what is narrative for?"),
        background=("Stories are universal; theories propose "
                    "simulation (practice for life), social bonding, "
                    "and cultural transmission. The adaptive function "
                    "- if any - remains literary Darwinism's open "
                    "question."),
        why_it_matters=("Stories shape minds and societies. Their "
                        "function determines their study."),
        sig_lens=("The Signature lens treats stories as a simulation "
                  "ledger: the Signature approach asks what "
                  "narrative rehearses."),
        sig_body=("The Signature proposal models stories as "
                  "multi-functional. Assumptions: (1) narrative "
                  "simulates social life; (2) simulation builds "
                  "social cognition; (3) transmission preserves "
                  "culture. Reasoning path: the proposal predicts "
                  "story engagement should track social-cognitive "
                  "demand - which the evidence supports. Stories "
                  "are then social simulators. Limits: the model "
                  "needs better simulation tests; the "
                  "entertainment dimension needs honoring."),
        pointer=('The Signature system models stories as social simulators: narrative rehearses the social cognition life demands. The Signature test: engagement tracks social-cognitive measures. It would be refuted if asocial species tell stories equally.'),
        key_points=[
            "Stories are culturally universal.",
            "Simulation, bonding, and transmission compete.",
            "The adaptive function remains open.",
            "Stories shape minds and societies.",
        ],
        requirements=[
            "Simulation-effect tests.",
            "Social-cognition correlations.",
            "Entertainment-dimension analyses.",
        ],
        standards=[
            "Claims checked against the narrative literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Boyd B. On the Origin of Stories. Harvard University Press; 2009.",
            "Gottschall J. The Storytelling Animal. Houghton Mifflin; 2012.",
        ],
        hypotheses=[
            "Social simulation explains storytelling.",
            "Stories are pure entertainment.",
            "Cultural transmission is primary.",
            "No function; spandrel.",
        ],
        confirm="Engagement tracks social-cognitive measures.",
        refute="Asocial species tell stories equally.",
    ),
    dict(
        key="literature-02",
        name="What Is Literature",
        group="Theory",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("What is literature - can the concept be defined?"),
        background=("Definitions failed serially (imaginative writing, "
                    "defamiliarization, institution); the concept "
                    "stretches from sonnets to tweets. Whether "
                    "definition is possible or the concept should "
                    "dissolve remains foundational."),
        why_it_matters=("The definition bounds the discipline. Its fate "
                        "determines literary study's scope."),
        sig_lens=("The Signature lens treats literature as a use "
                  "ledger: the Signature approach asks what the "
                  "concept does."),
        sig_body=("The Signature proposal models 'literature' as a "
                  "cluster-institutional concept. Assumptions: (1) "
                  "no essence covers cases; (2) institutional "
                  "recognition plus textual features organize use; "
                  "(3) borderline cases are productive. Reasoning "
                  "path: the proposal predicts definitional "
                  "disputes should track institutional stakes - "
                  "which they do. Use the cluster, argue the "
                  "borders. Limits: the model needs better "
                  "borderline analyses; the evaluative dimension "
                  "persists."),
        pointer=('The Signature system models literature as a cluster-institutional concept: no essence, productive borders. The Signature test: disputes track institutional stakes. It would be refuted if an essential definition succeeds.'),
        key_points=[
            "Essential definitions failed serially.",
            "The concept stretches from sonnets to tweets.",
            "Institutional recognition organizes use.",
            "Whether definition is possible is foundational.",
        ],
        requirements=[
            "Borderline-case analyses.",
            "Institutional-stake studies.",
            "Evaluative-dimension accounts.",
        ],
        standards=[
            "Claims checked against the literary-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Eagleton T. Literary Theory. University of Minnesota Press; 1983.",
            "Wellek R, Warren A. Theory of Literature. Harcourt; 1949.",
        ],
        hypotheses=[
            "Cluster-institutional explains definitional debates.",
            "An essence exists.",
            "The concept should dissolve.",
            "Institutional theory suffices.",
        ],
        confirm="Disputes track institutional stakes.",
        refute="An essential definition succeeds.",
    ),
    dict(
        key="literature-03",
        name="The Author Problem",
        group="Theory",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("Who is the author - the person, the persona, or a "
                 "function of discourse?"),
        background=("Foucault's author-function, Barthes' death, and "
                    "biographical criticism compete. The author's "
                    "status affects interpretation, attribution, and "
                    "markets. Whether the author matters remains "
                    "theory's live question."),
        why_it_matters=("Authorship shapes interpretation and value. "
                        "Its status determines critical practice."),
        sig_lens=("The Signature lens treats the author as a "
                  "function ledger: the Signature approach asks what "
                  "work the author-concept does."),
        sig_body=("The Signature proposal models authorship as "
                  "function-plural. Assumptions: (1) the author "
                  "organizes interpretation, markets, and law; (2) "
                  "different functions need different author-"
                  "concepts; (3) no single concept serves all. "
                  "Reasoning path: the proposal predicts author-"
                  "debates should track functional stakes - which "
                  "they do. Keep multiple author-concepts for "
                  "multiple jobs. Limits: the model needs better "
                  "function separations; the AI-authorship question "
                  "needs addressing."),
        pointer=('The Signature system models authorship as function-plural: multiple author-concepts for multiple jobs. The Signature test: debates track functional stakes. It would be refuted if one author-concept serves all jobs.'),
        key_points=[
            "Foucault and Barthes challenged the author.",
            "Biographical criticism persists.",
            "Authorship affects markets and law.",
            "Whether the author matters is live.",
        ],
        requirements=[
            "Function-separation analyses.",
            "AI-authorship investigations.",
            "An account of the debates' stakes.",
        ],
        standards=[
            "Claims checked against the authorship literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Foucault M. What is an author? 1969.",
            "Barthes R. The death of the author. 1967.",
        ],
        hypotheses=[
            "Function plurality explains author debates.",
            "The author is dead.",
            "The author is essential.",
            "One concept suffices.",
        ],
        confirm="Debates track functional stakes.",
        refute="One author-concept serves all jobs.",
    ),
    dict(
        key="literature-04",
        name="Fiction: Why Believe It",
        group="Theory",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Why do we believe fiction - engaging with worlds we "
                 "know are unreal?"),
        background=("Coleridge's willing suspension of disbelief; "
                    "Walton's make-believe; the paradox of fiction "
                    "(see literature-05). The mechanism - how "
                    "unbelieved worlds move us - remains open."),
        why_it_matters=("Fiction is humanity's great pretense. Its "
                        "mechanism reveals imagination's workings."),
        sig_lens=("The Signature lens treats fiction as a pretense "
                  "ledger: the Signature approach asks what the "
                  "mind does with the unreal."),
        sig_body=("The Signature proposal models fiction engagement "
                  "as decoupled simulation. Assumptions: (1) the "
                  "mind simulates fictional worlds; (2) belief "
                  "systems stay tagged as fictional; (3) emotions "
                  "run on the simulation. Reasoning path: the "
                  "proposal predicts emotional response without "
                  "belief - which is what happens. We believe "
                  "fiction by simulating without endorsing. Limits: "
                  "the model needs better decoupling studies; the "
                  "imagination-belief boundary needs mapping."),
        pointer=('The Signature system models fiction engagement as decoupled simulation: simulate without endorsing. The Signature test: emotion dissociates from belief measures. It would be refuted if belief always accompanies emotion.'),
        key_points=[
            "We engage worlds we know are unreal.",
            "Emotions run without belief.",
            "Make-believe theories dominate.",
            "The mechanism remains open.",
        ],
        requirements=[
            "Decoupling studies.",
            "Imagination-belief boundary mapping.",
            "An account of emotional response.",
        ],
        standards=[
            "Claims checked against the fiction literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Walton KL. Mimesis as Make-Believe. Harvard University Press; 1990.",
            "Coleridge ST. Biographia Literaria. 1817.",
        ],
        hypotheses=[
            "Decoupled simulation explains engagement.",
            "We genuinely (if briefly) believe.",
            "The paradox is illusory.",
            "Emotions need no mechanism.",
        ],
        confirm="Emotion dissociates from belief measures.",
        refute="Belief always accompanies emotion.",
    ),
    dict(
        key="literature-05",
        name="The Paradox of Fiction",
        group="Psychology",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("How can we fear fictional monsters - feeling real "
                 "emotions toward unreal beings?"),
        background=("Radford's paradox: we pity Anna Karenina while "
                    "believing she does not exist. Solutions: "
                    "irrationality, thought-theory, illusion theory. "
                    "No solution commands consensus."),
        why_it_matters=("The paradox tests emotion theory. Its "
                        "solution clarifies feeling's logic."),
        sig_lens=("The Signature lens treats the paradox as a "
                  "simulation ledger: the Signature approach asks "
                  "what the emotions respond to."),
        sig_body=("The Signature proposal models fictional emotions "
                  "as simulation-responses. Assumptions: (1) "
                  "emotions respond to simulated scenarios; (2) "
                  "belief is not required; (3) the responses are "
                  "rational. Reasoning path: the proposal dissolves "
                  "the paradox: emotions track imagined situations, "
                  "not beliefs about existence - which matches "
                  "how emotions work generally. Pitying Anna is "
                  "then no more paradoxical than fearing a "
                  "hypothetical. Limits: the model needs better "
                  "simulation-emotion studies; the rationality "
                  "question persists."),
        pointer=('The Signature system dissolves the paradox: emotions track imagined situations, not existence beliefs. The Signature test: emotions track imagined-situation measures. It would be refuted if existence beliefs gate emotional response.'),
        key_points=[
            "We feel real emotions toward unreal beings.",
            "Radford posed the paradox.",
            "Multiple solutions compete.",
            "No consensus solution exists.",
        ],
        requirements=[
            "Simulation-emotion studies.",
            "Rationality analyses.",
            "An account of the paradox's persistence.",
        ],
        standards=[
            "Claims checked against the paradox literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Radford C. How can we be moved by the fate of Anna Karenina? 1975.",
            "Walton KL. Mimesis as Make-Believe. Harvard University Press; 1990.",
        ],
        hypotheses=[
            "Simulation-response dissolves the paradox.",
            "Fictional emotions are irrational.",
            "Thought-theory solves it.",
            "The paradox is genuine and unsolved.",
        ],
        confirm="Emotions track imagined-situation measures.",
        refute="Existence beliefs gate emotional response.",
    ),
    dict(
        key="literature-06",
        name="Why We Read Sad Stories",
        group="Psychology",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Why do we read tragedies - seeking sorrow we avoid in "
                 "life?"),
        background=("The paradox of tragedy in literature: Aristotle's "
                    "catharsis, Hume's conversion, and modern safe-"
                    "context theories. The pleasure in literary "
                    "suffering remains debated."),
        why_it_matters=("Tragedy is literature's high form. Its pleasure "
                        "explains art's function."),
        sig_lens=("The Signature lens treats tragedy as a safety "
                  "ledger: the Signature approach asks what the "
                  "frame adds."),
        sig_body=("The Signature proposal models tragic pleasure as "
                  "safe-suffering (see musicology-07). Assumptions: "
                  "(1) real suffering involves threat; (2) fiction "
                  "removes threat; (3) the emotions reward. Reasoning "
                  "path: the proposal predicts tragic enjoyment "
                  "should track empathy and the safety frame - which "
                  "it does. We read tragedies to feel safely. Limits: "
                  "the model needs better frame studies; the "
                  "catharsis question persists."),
        pointer=('The Signature system models tragic pleasure as safe suffering: feel deeply without threat. The Signature test: enjoyment tracks safety-empathy measures. It would be refuted if threat presence does not reduce enjoyment.'),
        key_points=[
            "We seek sorrow in fiction we avoid in life.",
            "Catharsis, conversion, and safety theories compete.",
            "The pleasure in suffering is debated.",
            "Tragedy is literature's high form.",
        ],
        requirements=[
            "Safety-frame studies.",
            "Empathy-correlation research.",
            "Catharsis investigations.",
        ],
        standards=[
            "Claims checked against the tragedy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Aristotle. Poetics. 4th century BCE.",
            "Hume D. Of tragedy. 1757.",
        ],
        hypotheses=[
            "Safe-suffering explains tragic pleasure.",
            "Catharsis purges emotion.",
            "Conversion transforms pain to pleasure.",
            "The paradox is overstated.",
        ],
        confirm="Enjoyment tracks safety-empathy measures.",
        refute="Threat presence does not reduce enjoyment.",
    ),
    dict(
        key="literature-07",
        name="The Canon Problem in Literature",
        group="History",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("Who decides literature's canon - and can it be opened "
                 "without losing judgment?"),
        background=("Bloom defended the Western canon; critics "
                    "exposed its exclusions. Expansion efforts face "
                    "the standards question. Whether canons can be "
                    "just remains literature's institutional debate."),
        why_it_matters=("Canons shape education and memory. Their "
                        "justice determines cultural transmission."),
        sig_lens=("The Signature lens treats canons as a standard "
                  "ledger: the Signature approach asks what "
                  "excellence means across traditions."),
        sig_body=("The Signature proposal models canon expansion as "
                  "standard-pluralizing (see art-history-09). "
                  "Assumptions: (1) excellence criteria are "
                  "tradition-relative; (2) the old canon used one "
                  "tradition's; (3) plural criteria enable just "
                  "expansion. Reasoning path: the proposal predicts "
                  "successful expansions should articulate included "
                  "traditions' excellences - which the best "
                  "curricular work does. Limits: the model needs "
                  "better expansion evaluations; the relativism "
                  "risk needs guarding."),
        pointer=("The Signature system models canon expansion as standard-pluralizing: articulate each tradition's own excellences. The Signature test: expansions succeed with articulated standards. It would be refuted if no standards survive pluralization."),
        key_points=[
            "Bloom defended the Western canon.",
            "Critics exposed systematic exclusions.",
            "Expansion faces the standards question.",
            "Whether just canons are possible is debated.",
        ],
        requirements=[
            "Expansion-evaluation studies.",
            "Tradition-relative excellence frameworks.",
            "Relativism guards.",
        ],
        standards=[
            "Claims checked against the canon literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bloom H. The Western Canon. Harcourt; 1994.",
            "Gates HL. The Signifying Monkey. Oxford University Press; 1988.",
        ],
        hypotheses=[
            "Standard pluralization opens canons justly.",
            "Universal standards exist.",
            "Canons are inherently exclusionary.",
            "Judgment should be abandoned.",
        ],
        confirm="Expansions succeed with articulated standards.",
        refute="No standards survive pluralization.",
    ),
    dict(
        key="literature-08",
        name="Genre: Real or Imposed",
        group="Theory",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Are genres real - in the texts - or imposed by "
                 "critics and markets?"),
        background=("Genres organize publishing and reading; yet "
                    "texts blend and defy them. Fowler, Derrida, "
                    "and others debated genre's ontology. Whether "
                    "genres describe or prescribe remains open."),
        why_it_matters=("Genres shape writing and reading. Their "
                        "reality determines criticism's categories."),
        sig_lens=("The Signature lens treats genre as a contract "
                  "ledger: the Signature approach asks what "
                  "expectations the label sets."),
        sig_body=("The Signature proposal models genre as "
                  "expectation-contract. Assumptions: (1) genre "
                  "labels set reader expectations; (2) texts "
                  "negotiate with them; (3) the negotiation is "
                  "the meaning. Reasoning path: the proposal "
                  "predicts genre effects should track "
                  "expectation - which reception studies confirm. "
                  "Genres are then real as contracts, not as "
                  "essences. Limits: the model needs better "
                  "contract-violation studies; the market's role "
                  "needs analyzing."),
        pointer=('The Signature system models genre as expectation-contract: real as agreements between texts and readers, not as essences. The Signature test: reception tracks genre-expectation measures. It would be refuted if genre labels show no reception effect.'),
        key_points=[
            "Genres organize publishing and reading.",
            "Texts blend and defy genre boundaries.",
            "Expectations shape reception.",
            "Whether genres are real is debated.",
        ],
        requirements=[
            "Expectation-effect studies.",
            "Contract-violation analyses.",
            "Market-role investigations.",
        ],
        standards=[
            "Claims checked against the genre literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fowler A. Kinds of Literature. Harvard University Press; 1982.",
            "Derrida J. The law of genre. 1980.",
        ],
        hypotheses=[
            "Expectation-contract captures genre.",
            "Genres are textual essences.",
            "Genres are pure marketing.",
            "The concept is useless.",
        ],
        confirm="Reception tracks genre-expectation measures.",
        refute="Genre labels show no reception effect.",
    ),
    dict(
        key="literature-09",
        name="The Meaning Problem in Interpretation",
        group="Theory",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("What makes an interpretation correct - authorial "
                 "intent, textual evidence, or reader response?"),
        background=("Hirsch defended authorial meaning; Gadamer "
                    "made understanding historical; Fish made it "
                    "communal. The correctness question divides "
                    "hermeneutics. Whether interpretations can be "
                    "right remains open."),
        why_it_matters=("Interpretation is literary study's act. Its "
                        "correctness determines the discipline's "
                        "knowledge."),
        sig_lens=("The Signature lens treats interpretation as a "
                  "constraint ledger: the Signature approach asks "
                  "what constrains readings."),
        sig_body=("The Signature proposal models interpretation as "
                  "constraint-satisfying. Assumptions: (1) texts "
                  "constrain (not all readings fit); (2) multiple "
                  "constraints (intent, text, context) interact; "
                  "(3) correctness is constraint satisfaction. "
                  "Reasoning path: the proposal predicts the best "
                  "interpretations should satisfy the most "
                  "constraints - which critical practice rewards. "
                  "Interpretations are then better or worse, not "
                  "right or wrong absolutely. Limits: the model "
                  "needs better constraint theories; the "
                  "relativism question persists."),
        pointer=('The Signature system models interpretation as constraint satisfaction: better or worse, not absolutely right or wrong. The Signature test: quality judgments track constraint satisfaction. It would be refuted if constraint-free readings succeed equally.'),
        key_points=[
            "Authorial intent, text, and reader compete.",
            "Hermeneutic traditions divide on correctness.",
            "Texts constrain but do not determine readings.",
            "Whether interpretations can be right is open.",
        ],
        requirements=[
            "Constraint-theory development.",
            "Interpretation-ranking studies.",
            "Relativism responses.",
        ],
        standards=[
            "Claims checked against the hermeneutics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hirsch ED. Validity in Interpretation. Yale University Press; 1967.",
            "Fish S. Is There a Text in This Class? Harvard University Press; 1980.",
        ],
        hypotheses=[
            "Constraint satisfaction captures correctness.",
            "Authorial intent decides.",
            "Readers decide.",
            "No interpretation is better than another.",
        ],
        confirm="Quality judgments track constraint satisfaction.",
        refute="Constraint-free readings succeed equally.",
    ),
    dict(
        key="literature-10",
        name="Close Reading Versus Distant Reading",
        group="Method",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Can distant reading - computational analysis of "
                 "thousands of texts - replace or complement close "
                 "reading?"),
        background=("Moretti proposed distant reading; traditionalists "
                    "defended close attention. The methods answer "
                    "different questions (patterns versus meanings). "
                    "Whether they integrate remains the method "
                    "question."),
        why_it_matters=("Method determines what literary study knows. "
                        "The integration shapes the field's future."),
        sig_lens=("The Signature lens treats the methods as a scale "
                  "ledger: the Signature approach asks what each "
                  "scale reveals."),
        sig_body=("The Signature proposal models the methods as "
                  "scale-complementary. Assumptions: (1) distant "
                  "reading finds patterns; (2) close reading finds "
                  "meanings; (3) patterns need meanings and vice "
                  "versa. Reasoning path: the proposal predicts the "
                  "best work should cycle between scales - which "
                  "it does. The debate is then a false choice: use "
                  "both, each for its questions. Limits: the model "
                  "needs better integration exemplars; the "
                  "institutional resistance needs addressing."),
        pointer=('The Signature system models close and distant reading as scale-complementary: cycle between patterns and meanings. The Signature test: best work cycles between scales. It would be refuted if single-scale work suffices.'),
        key_points=[
            "Distant reading finds large-scale patterns.",
            "Close reading finds textual meanings.",
            "The methods answer different questions.",
            "Whether they integrate is the method question.",
        ],
        requirements=[
            "Integration exemplars.",
            "Scale-appropriate question taxonomies.",
            "Resistance analyses.",
        ],
        standards=[
            "Claims checked against the digital-humanities literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Moretti F. Distant Reading. Verso; 2013.",
            "Jockers ML. Macroanalysis. University of Illinois Press; 2013.",
        ],
        hypotheses=[
            "Scale complementarity resolves the debate.",
            "Distant reading replaces close reading.",
            "Close reading is irreplaceable.",
            "The methods are incommensurable.",
        ],
        confirm="Best work cycles between scales.",
        refute="Single-scale work suffices.",
    ),
    dict(
        key="literature-11",
        name="Why Poetry Is Hard",
        group="Theory",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Why is poetry hard - and is the difficulty essential "
                 "or elitist?"),
        background=("Modern poetry's difficulty alienates readers; "
                    "defenders call difficulty the point (complex "
                    "thought needs complex form). The accessibility "
                    "debate - whether poetry should be hard - "
                    "remains unresolved."),
        why_it_matters=("Poetry's difficulty shapes its audience. The "
                        "verdict determines its future."),
        sig_lens=("The Signature lens treats difficulty as a demand "
                  "ledger: the Signature approach asks what the "
                  "difficulty buys."),
        sig_body=("The Signature proposal models poetic difficulty "
                  "as demand-graded. Assumptions: (1) some "
                  "difficulty is gratuitous; (2) some enables "
                  "thought unavailable plainly; (3) readers can "
                  "tell the difference. Reasoning path: the "
                  "proposal predicts valued difficulty should "
                  "reward effort - which the best difficult poetry "
                  "does. The answer is then discriminate: keep "
                  "the difficulty that pays, cut the rest. Limits: "
                  "the model needs better reward studies; the "
                  "elitism charge needs answering."),
        pointer=('The Signature system models poetic difficulty as graded: keep the difficulty that rewards effort, cut the gratuitous. The Signature test: valuation tracks difficulty-reward measures. It would be refuted if gratuitous difficulty pleases equally.'),
        key_points=[
            "Modern poetry's difficulty alienates readers.",
            "Defenders call difficulty essential.",
            "Critics call it elitist.",
            "Whether difficulty pays remains the question.",
        ],
        requirements=[
            "Difficulty-reward studies.",
            "Gratuitous-versus-essential separations.",
            "Elitism-charge responses.",
        ],
        standards=[
            "Claims checked against the poetics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Steiner G. On difficulty. 1978.",
            "Perloff M. Differentials. University of Alabama Press; 2004.",
        ],
        hypotheses=[
            "Demand grading disciplines the debate.",
            "Difficulty is essential to poetry.",
            "Difficulty is elitist gatekeeping.",
            "Readers should work harder.",
        ],
        confirm="Valuation tracks difficulty-reward measures.",
        refute="Gratuitous difficulty pleases equally.",
    ),
    dict(
        key="literature-12",
        name="The Death of the Author Debate",
        group="Theory",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Is the author dead - and what died, exactly?"),
        background=("Barthes' 1967 provocation attacked authorial "
                    "authority; the slogan outran the argument. "
                    "What remains: the critique of biographical "
                    "reduction, not the author's disappearance. "
                    "Whether anything died remains debated."),
        why_it_matters=("The death-slogan shaped theory. Its precise "
                        "meaning determines its legacy."),
        sig_lens=("The Signature lens treats the death as a "
                  "slogan ledger: the Signature approach asks what "
                  "the provocation did."),
        sig_body=("The Signature proposal models the 'death' as "
                  "authority-critique. Assumptions: (1) Barthes "
                  "attacked the author-as-origin; (2) the "
                  "author-as-person survived; (3) the slogan "
                  "confused the two. Reasoning path: the proposal "
                  "shows what died was interpretive tyranny, not "
                  "authorship - explaining both the essay's force "
                  "and its overreading. Keep the critique, retire "
                  "the slogan. Limits: the model needs better "
                  "reception histories; the AI-authorship question "
                  "revives it."),
        pointer=("The Signature system models the author's 'death' as authority-critique: interpretive tyranny died, authorship survived. The Signature test: critical practice dropped biographical reduction. It would be refuted if authorial intent still rules interpretation."),
        key_points=[
            "Barthes' 1967 essay attacked authorial authority.",
            "The slogan outran the argument.",
            "Biographical reduction was the target.",
            "Whether anything died is debated.",
        ],
        requirements=[
            "Reception histories.",
            "Authority-versus-person separations.",
            "AI-authorship implications.",
        ],
        standards=[
            "Claims checked against the theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Barthes R. The death of the author. 1967.",
            "Burke S. The Death and Return of the Author. Edinburgh University Press; 1998.",
        ],
        hypotheses=[
            "Authority-critique captures the essay.",
            "The author genuinely died.",
            "Nothing changed.",
            "The author returned.",
        ],
        confirm="Critical practice dropped biographical reduction.",
        refute="Authorial intent still rules interpretation.",
    ),
    dict(
        key="literature-13",
        name="Intentional Fallacy: Still Standing",
        group="Theory",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("Does the intentional fallacy still stand - is authorial "
                 "intent irrelevant to meaning?"),
        background=("Wimsatt and Beardsley banished intent; "
                    "Hirsch and others readmitted it. The current "
                    "state: intent matters but does not rule. "
                    "Whether the fallacy names a real error remains "
                    "open."),
        why_it_matters=("Intent's status shapes interpretation. The "
                        "fallacy's fate determines critical method."),
        sig_lens=("The Signature lens treats intent as an evidence "
                  "ledger: the Signature approach asks what intent "
                  "evidence proves."),
        sig_body=("The Signature proposal models intent as "
                  "evidence-not-verdict. Assumptions: (1) intent "
                  "evidence constrains interpretation; (2) texts "
                  "exceed intent; (3) both matter. Reasoning path: "
                  "the proposal predicts the best interpretations "
                  "should use intent as one constraint among many - "
                  "which they do. The fallacy is then real (intent "
                  "does not equal meaning) but limited (intent "
                  "informs meaning). Limits: the model needs better "
                  "intent-evidence standards; the unconscious-"
                  "intention question persists."),
        pointer=('The Signature system models authorial intent as evidence, not verdict: it constrains interpretation without ruling it. The Signature test: interpretations use intent as constraint. It would be refuted if intent evidence never constrains.'),
        key_points=[
            "Wimsatt and Beardsley banished intent.",
            "Hirsch readmitted it partially.",
            "Current state: intent informs but does not rule.",
            "Whether the fallacy names real error is open.",
        ],
        requirements=[
            "Intent-evidence standards.",
            "Unconscious-intention analyses.",
            "Constraint-interaction studies.",
        ],
        standards=[
            "Claims checked against the hermeneutics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wimsatt WK, Beardsley MC. The intentional fallacy. 1946.",
            "Hirsch ED. Validity in Interpretation. Yale University Press; 1967.",
        ],
        hypotheses=[
            "Evidence-not-verdict captures intent's role.",
            "Intent is irrelevant.",
            "Intent determines meaning.",
            "The fallacy was a mistake.",
        ],
        confirm="Interpretations use intent as constraint.",
        refute="Intent evidence never constrains.",
    ),
    dict(
        key="literature-14",
        name="The Affective Fallacy Question",
        group="Theory",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("Is the affective fallacy a fallacy - does reader "
                 "emotion distort or constitute literary meaning?"),
        background=("Wimsatt and Beardsley warned against confusing "
                    "the poem with its effects; reader-response "
                    "theorists made effects the meaning. Whether "
                    "emotion is evidence or noise remains open."),
        why_it_matters=("Emotion's status shapes criticism. The "
                        "fallacy's fate determines reader-response's "
                        "validity."),
        sig_lens=("The Signature lens treats emotion as a signal "
                  "ledger: the Signature approach asks what "
                  "feelings indicate."),
        sig_body=("The Signature proposal models reader emotion as "
                  "signal-not-verdict. Assumptions: (1) emotions "
                  "respond to textual features; (2) they mislead "
                  "when idiosyncratic; (3) patterns across readers "
                  "signal. Reasoning path: the proposal predicts "
                  "shared emotional responses should track textual "
                  "features - which they do. Emotion is then "
                  "evidence when shared, noise when private. Limits: "
                  "the model needs better shared-response studies; "
                  "the idiosyncrasy question persists."),
        pointer=('The Signature system models reader emotion as signal when shared across readers, noise when idiosyncratic. The Signature test: shared emotions track textual features. It would be refuted if emotional responses prove random.'),
        key_points=[
            "The affective fallacy warned against effect-confusion.",
            "Reader-response made effects central.",
            "Shared responses may signal textual features.",
            "Whether emotion is evidence remains open.",
        ],
        requirements=[
            "Shared-response studies.",
            "Idiosyncrasy analyses.",
            "Signal-versus-noise frameworks.",
        ],
        standards=[
            "Claims checked against the reader-response literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wimsatt WK, Beardsley MC. The affective fallacy. 1949.",
            "Fish S. Is There a Text in This Class? Harvard University Press; 1980.",
        ],
        hypotheses=[
            "Signal-not-verdict captures emotion's role.",
            "Emotion is pure noise.",
            "Emotion constitutes meaning.",
            "The fallacy stands fully.",
        ],
        confirm="Shared emotions track textual features.",
        refute="Emotional responses prove random.",
    ),
    dict(
        key="literature-15",
        name="Unreliable Narrators: How Detect",
        group="Narrative",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("How do readers detect unreliable narrators - and how "
                 "reliable is the detection?"),
        background=("Booth defined unreliability against the implied "
                    "author's norms; readers use inconsistencies, "
                    "other characters, and genre cues. Whether "
                    "detection is reliable - and what unreliability "
                    "means - remains open."),
        why_it_matters=("Unreliability is narrative's great game. Its "
                        "detection determines reading's skill."),
        sig_lens=("The Signature lens treats unreliability as a "
                  "signal ledger: the Signature approach asks what "
                  "cues readers use."),
        sig_body=("The Signature proposal models detection as "
                  "cue-convergent. Assumptions: (1) no single cue "
                  "is decisive; (2) readers combine inconsistencies, "
                  "corroboration, and norms; (3) convergence "
                  "determines confidence. Reasoning path: the "
                  "proposal predicts confident detection should "
                  "follow cue convergence - which reader studies "
                  "support. Unreliability is then a reading "
                  "achievement, not a textual property alone. "
                  "Limits: the model needs better reader studies; "
                  "the implied-author question persists."),
        pointer=('The Signature system models unreliability detection as cue-convergent: a reading achievement, not a textual property alone. The Signature test: confidence tracks cue convergence. It would be refuted if readers detect without cues.'),
        key_points=[
            "Booth defined unreliability against implied norms.",
            "Readers combine multiple cues.",
            "No single cue is decisive.",
            "Whether detection is reliable is open.",
        ],
        requirements=[
            "Reader detection studies.",
            "Cue-weighting analyses.",
            "Implied-author investigations.",
        ],
        standards=[
            "Claims checked against the narratology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Booth WC. The Rhetoric of Fiction. University of Chicago Press; 1961.",
            "Phelan J, Martin MP. The lessons of Weymouth. 1999.",
        ],
        hypotheses=[
            "Cue convergence explains detection.",
            "Unreliability is textual fact.",
            "Detection is unreliable.",
            "The concept is incoherent.",
        ],
        confirm="Confidence tracks cue convergence.",
        refute="Readers detect without cues.",
    ),
    dict(
        key="literature-16",
        name="Free Indirect Discourse Problem",
        group="Narrative",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("What is free indirect discourse - whose voice speaks "
                 "when narration blends with character?"),
        background=("The technique (Austen, Flaubert, Woolf) merges "
                    "narrator and character voices; linguists and "
                    "narratologists debate its structure. Whether "
                    "it is dual-voiced or a distinct mode remains "
                    "open."),
        why_it_matters=("Free indirect discourse is the novel's great "
                        "technique. Its nature determines narrative "
                        "theory."),
        sig_lens=("The Signature lens treats the technique as a "
                  "voice ledger: the Signature approach asks what "
                  "the blending does."),
        sig_body=("The Signature proposal models free indirect "
                  "discourse as voice-blended. Assumptions: (1) "
                  "the technique merges perspectives; (2) the "
                  "merging creates irony and intimacy; (3) the "
                  "blend is gradient. Reasoning path: the proposal "
                  "predicts effects should track blend degree - "
                  "which stylistic analysis supports. The technique "
                  "is then a spectrum, not a category. Limits: the "
                  "model needs better blend measures; the "
                  "cross-linguistic question persists."),
        pointer=('The Signature system models free indirect discourse as a voice-blend spectrum: effects track blending degree. The Signature test: effects track blend measures. It would be refuted if categorical boundaries hold.'),
        key_points=[
            "The technique merges narrator and character voices.",
            "Austen, Flaubert, and Woolf mastered it.",
            "Dual-voice versus distinct-mode is debated.",
            "Whether it is a spectrum remains open.",
        ],
        requirements=[
            "Blend-degree measures.",
            "Cross-linguistic studies.",
            "Effect-tracking analyses.",
        ],
        standards=[
            "Claims checked against the narratology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Banfield A. Unspeakable Sentences. Routledge; 1982.",
            "Cohn D. Transparent Minds. Princeton University Press; 1978.",
        ],
        hypotheses=[
            "Spectrum model captures the technique.",
            "It is strictly dual-voiced.",
            "It is a distinct mode.",
            "The concept is dispensable.",
        ],
        confirm="Effects track blend measures.",
        refute="Categorical boundaries hold.",
    ),
    dict(
        key="literature-17",
        name="The Plot Problem",
        group="Narrative",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("What is plot - and why do we crave what happens next?"),
        background=("Forster distinguished story from plot; Brooks "
                    "made plot desire-driven; cognitive approaches "
                    "study suspense mechanisms. The craving for "
                    "narrative - and plot's structure - remains "
                    "partially open."),
        why_it_matters=("Plot drives narrative engagement. Its mechanism "
                        "is storytelling's engine."),
        sig_lens=("The Signature lens treats plot as a desire ledger: "
                  "the Signature approach asks what keeps readers "
                  "turning pages."),
        sig_body=("The Signature proposal models plot as "
                  "desire-structured. Assumptions: (1) readers "
                  "desire resolutions; (2) plots delay and shape "
                  "desire; (3) the shaping is the art. Reasoning "
                  "path: the proposal predicts engagement should "
                  "track desire-management - which suspense studies "
                  "support. Plot is then the architecture of "
                  "narrative desire. Limits: the model needs better "
                  "desire measures; the anti-plot traditions need "
                  "honoring."),
        pointer=('The Signature system models plot as the architecture of narrative desire: delay and shape, not just sequence. The Signature test: engagement tracks desire-management measures. It would be refuted if plotless narratives engage equally.'),
        key_points=[
            "Forster distinguished story from plot.",
            "Brooks made plot desire-driven.",
            "Suspense mechanisms are studied cognitively.",
            "The craving's structure remains partially open.",
        ],
        requirements=[
            "Desire-management studies.",
            "Suspense-mechanism research.",
            "Anti-plot tradition analyses.",
        ],
        standards=[
            "Claims checked against the narratology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Forster EM. Aspects of the Novel. 1927.",
            "Brooks P. Reading for the Plot. Harvard University Press; 1984.",
        ],
        hypotheses=[
            "Desire structure explains plot engagement.",
            "Plot is mere sequence.",
            "Character drives everything.",
            "The craving is unanalyzable.",
        ],
        confirm="Engagement tracks desire-management measures.",
        refute="Plotless narratives engage equally.",
    ),
    dict(
        key="literature-18",
        name="Character: Real or Function",
        group="Narrative",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Are characters real - persons we know - or functions "
                 "of plot?"),
        background=("Readers grieve for characters; structuralists "
                    "reduced them to actants. The paradox: treating "
                    "the unreal as persons. Whether character "
                    "personhood is illusion or achievement remains "
                    "open."),
        why_it_matters=("Characters are fiction's people. Their status "
                        "determines narrative's humanity."),
        sig_lens=("The Signature lens treats character as a "
                  "simulation ledger: the Signature approach asks "
                  "what the mind builds."),
        sig_body=("The Signature proposal models characters as "
                  "person-simulations. Assumptions: (1) readers "
                  "build person-models from textual cues; (2) the "
                  "models support social cognition; (3) the "
                  "richness varies. Reasoning path: the proposal "
                  "predicts character engagement should track "
                  "model richness - which it does. Characters are "
                  "then real as simulations: the personhood is "
                  "constructed but genuine. Limits: the model needs "
                  "better simulation studies; the actant critique "
                  "needs answering."),
        pointer=('The Signature system models characters as person-simulations: constructed personhood, genuinely felt. The Signature test: engagement tracks model-richness measures. It would be refuted if functional characters engage equally.'),
        key_points=[
            "Readers grieve for fictional persons.",
            "Structuralists reduced characters to functions.",
            "The personhood paradox persists.",
            "Whether personhood is illusion remains open.",
        ],
        requirements=[
            "Person-model studies.",
            "Richness-engagement correlations.",
            "Actant-critique responses.",
        ],
        standards=[
            "Claims checked against the character literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Phelan J. Reading People, Reading Plots. University of Chicago Press; 1989.",
            "Margolin U. Character. 2007.",
        ],
        hypotheses=[
            "Person-simulation explains character engagement.",
            "Characters are pure functions.",
            "The personhood is delusional.",
            "Flat characters work equally.",
        ],
        confirm="Engagement tracks model-richness measures.",
        refute="Functional characters engage equally.",
    ),
    dict(
        key="literature-19",
        name="The Ending Problem",
        group="Narrative",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("What makes an ending work - and why do endings "
                 "disappoint so often?"),
        background=("Endings must satisfy and surprise; Kermode "
                    "studied the sense of an ending. The "
                    "disappointment pattern - great novels, weak "
                    "endings - suggests structural difficulty. "
                    "Whether good endings follow principles remains "
                    "open."),
        why_it_matters=("Endings seal narrative meaning. Their craft "
                        "determines the whole's success."),
        sig_lens=("The Signature lens treats endings as a "
                  "resolution ledger: the Signature approach asks "
                  "what must be resolved."),
        sig_body=("The Signature proposal models endings as "
                  "desire-resolution. Assumptions: (1) plots open "
                  "desires; (2) endings must resolve the central "
                  "ones; (3) surprise needs inevitability. "
                  "Reasoning path: the proposal predicts satisfying "
                  "endings should resolve opened desires "
                  "surprisingly-yet-inevitably - which the best "
                  "endings do. The disappointment pattern then "
                  "reflects desire-mismanagement. Limits: the model "
                  "needs better resolution studies; the open-"
                  "ending tradition needs honoring."),
        pointer=('The Signature system models endings as desire-resolution: surprising yet inevitable closure of opened desires. The Signature test: satisfaction tracks resolution measures. It would be refuted if unresolved endings satisfy equally.'),
        key_points=[
            "Endings must satisfy and surprise.",
            "Great novels often have weak endings.",
            "Kermode studied the sense of an ending.",
            "Whether principles exist remains open.",
        ],
        requirements=[
            "Resolution-satisfaction studies.",
            "Open-ending analyses.",
            "Desire-tracking research.",
        ],
        standards=[
            "Claims checked against the narrative literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kermode F. The Sense of an Ending. Oxford University Press; 1967.",
            "Torgovnick M. Closure in the Novel. Princeton University Press; 1981.",
        ],
        hypotheses=[
            "Desire-resolution captures ending quality.",
            "Endings are arbitrary conventions.",
            "Open endings are superior.",
            "No principles exist.",
        ],
        confirm="Satisfaction tracks resolution measures.",
        refute="Unresolved endings satisfy equally.",
    ),
    dict(
        key="literature-20",
        name="Translation: Can It Be Faithful",
        group="Practice",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Can translation be faithful - and faithful to what: "
                 "words, meaning, or effect?"),
        background=("Traduttore traditore: translators betray. "
                    "Theories propose equivalence types (formal, "
                    "dynamic, foreignizing). Whether faithfulness "
                    "is coherent remains translation studies' "
                    "founding question."),
        why_it_matters=("Translation carries world literature. Its "
                        "faithfulness determines cross-cultural "
                        "understanding."),
        sig_lens=("The Signature lens treats translation as a "
                  "loyalty ledger: the Signature approach asks what "
                  "the translator serves."),
        sig_body=("The Signature proposal models translation as "
                  "loyalty-negotiated. Assumptions: (1) multiple "
                  "loyalties compete (author, reader, text); (2) "
                  "no translation serves all; (3) the negotiation "
                  "is visible. Reasoning path: the proposal predicts "
                  "good translations should declare their loyalties "
                  "- which the best do. Faithfulness is then to a "
                  "chosen loyalty, honestly pursued. Limits: the "
                  "model needs better loyalty analyses; the "
                  "untranslatable (see literature-21) bounds it."),
        pointer=('The Signature system models translation as loyalty-negotiated: faithful to a chosen loyalty, honestly pursued. The Signature test: quality tracks loyalty-clarity measures. It would be refuted if loyalty-declared translations fail equally.'),
        key_points=[
            "Translators betray by necessity.",
            "Equivalence types compete.",
            "Multiple loyalties conflict.",
            "Whether faithfulness is coherent is foundational.",
        ],
        requirements=[
            "Loyalty-declaration studies.",
            "Equivalence evaluations.",
            "Untranslatable-boundary mapping.",
        ],
        standards=[
            "Claims checked against the translation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Venuti L. The Translator's Invisibility. Routledge; 1995.",
            "Steiner G. After Babel. Oxford University Press; 1975.",
        ],
        hypotheses=[
            "Loyalty negotiation captures translation.",
            "Faithfulness is impossible.",
            "Formal equivalence suffices.",
            "Readers should learn languages.",
        ],
        confirm="Quality tracks loyalty-clarity measures.",
        refute="Loyalty-declared translations fail equally.",
    ),
    dict(
        key="literature-21",
        name="The Untranslatable Problem",
        group="Practice",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Is anything truly untranslatable - and what does "
                 "untranslatability mean?"),
        background=("Cassin's dictionary catalogs philosophical "
                    "untranslatables; poets claim untranslatability "
                    "routinely. The question: whether the barriers "
                    "are linguistic, cultural, or absolute."),
        why_it_matters=("Untranslatability bounds cross-cultural "
                        "understanding. Its nature determines "
                        "translation's limits."),
        sig_lens=("The Signature lens treats untranslatability as a "
                  "gap ledger: the Signature approach asks what "
                  "exactly fails to cross."),
        sig_body=("The Signature proposal models untranslatability "
                  "as gap-specific. Assumptions: (1) some gaps are "
                  "linguistic (no equivalent term); (2) some are "
                  "cultural (no shared practice); (3) explanation "
                  "bridges both partially. Reasoning path: the "
                  "proposal predicts untranslatables should yield "
                  "to paraphrase-plus-context - which they do. "
                  "Nothing is absolutely untranslatable; some "
                  "things need paragraphs, not words. Limits: the "
                  "model needs better gap typologies; the poetic "
                  "dimension (sound, rhythm) resists most."),
        pointer=('The Signature system models untranslatability as gap-specific: nothing is absolute; some things need paragraphs, not words. The Signature test: paraphrase bridges catalogued gaps. It would be refuted if gaps resist all paraphrase.'),
        key_points=[
            "Philosophical untranslatables are cataloged.",
            "Poets claim untranslatability routinely.",
            "Linguistic, cultural, and absolute barriers differ.",
            "What untranslatability means is open.",
        ],
        requirements=[
            "Gap typologies.",
            "Paraphrase-success studies.",
            "Poetic-dimension analyses.",
        ],
        standards=[
            "Claims checked against the translation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Cassin B. Dictionary of Untranslatables. Princeton University Press; 2014.",
            "Apter E. Against World Literature. Verso; 2013.",
        ],
        hypotheses=[
            "Gap specificity explains untranslatability claims.",
            "Some things are absolutely untranslatable.",
            "Everything translates with effort.",
            "Poetry is untranslatable.",
        ],
        confirm="Paraphrase bridges catalogued gaps.",
        refute="Gaps resist all paraphrase.",
    ),
    dict(
        key="literature-22",
        name="World Literature: What Is It",
        group="History",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("What is world literature - all literature, or "
                 "literature that circulates globally?"),
        background=("Damrosch defined it as circulation; Moretti as "
                    "distant reading's object; critics warn of "
                    "market-driven homogenization. Whether the "
                    "concept serves understanding or hegemony "
                    "remains open."),
        why_it_matters=("World literature organizes global study. Its "
                        "definition determines the field's politics."),
        sig_lens=("The Signature lens treats world literature as a "
                  "circulation ledger: the Signature approach asks "
                  "what travels and why."),
        sig_body=("The Signature proposal models world literature "
                  "as circulation-shaped. Assumptions: (1) "
                  "translation and markets select; (2) selection "
                  "is power-laden; (3) the selected corpus is not "
                  "the world's literature. Reasoning path: the "
                  "proposal predicts the canon should reflect "
                  "circulation power - which it does. World "
                  "literature is then a useful but ideological "
                  "category: study the circulation, not just the "
                  "books. Limits: the model needs better "
                  "circulation studies; the pedagogical use needs "
                  "guiding."),
        pointer=('The Signature system models world literature as circulation-shaped: study the selection powers, not just the selected books. The Signature test: corpus composition tracks circulation power. It would be refuted if selection proves meritocratic.'),
        key_points=[
            "Damrosch defined world literature as circulation.",
            "Markets and translation select powerfully.",
            "The selected corpus is not the world's literature.",
            "Whether the concept serves hegemony is open.",
        ],
        requirements=[
            "Circulation-power studies.",
            "Selection-bias documentation.",
            "Pedagogical-guidance development.",
        ],
        standards=[
            "Claims checked against the world-literature literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Damrosch D. What Is World Literature? Princeton University Press; 2003.",
            "Moretti F. Conjectures on world literature. 2000.",
        ],
        hypotheses=[
            "Circulation shaping explains the corpus.",
            "World literature is genuinely global.",
            "The concept is hegemonic.",
            "The concept should be abandoned.",
        ],
        confirm="Corpus composition tracks circulation power.",
        refute="Selection proves meritocratic.",
    ),
    dict(
        key="literature-23",
        name="The Novel: Why Dominant",
        group="History",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Why did the novel dominate - and is its dominance "
                 "ending?"),
        background=("The novel rose with print, bourgeois readers, "
                    "and individualism; it now competes with screens. "
                    "Theories of the rise (Watt, McKeon) and of "
                    "decline both circulate. Whether the novel's "
                    "era is passing remains open."),
        why_it_matters=("The novel is modernity's form. Its fate "
                        "signals cultural change."),
        sig_lens=("The Signature lens treats the novel as a medium "
                  "ledger: the Signature approach asks what the "
                  "form did that others could not."),
        sig_body=("The Signature proposal models the novel's rise "
                  "as medium-matched. Assumptions: (1) print "
                  "enabled long private reading; (2) the novel "
                  "exploited interiority and social detail; (3) "
                  "screens compete for the same attention. "
                  "Reasoning path: the proposal predicts the novel "
                  "should persist where its strengths (sustained "
                  "interiority) are irreplaceable - which they "
                  "are. Dominance may fade; the form endures. "
                  "Limits: the model needs better medium-"
                  "competition studies; the global-novel question "
                  "persists."),
        pointer=('The Signature system models the novel as medium-matched: dominance may fade, but sustained interiority is irreplaceable. The Signature test: persistence tracks interiority-demand measures. It would be refuted if screen narratives replace novels fully.'),
        key_points=[
            "The novel rose with print and bourgeois readers.",
            "It now competes with screens.",
            "Rise and decline theories both circulate.",
            "Whether its era is passing is open.",
        ],
        requirements=[
            "Medium-competition studies.",
            "Irreplaceability analyses.",
            "Global-novel investigations.",
        ],
        standards=[
            "Claims checked against the novel-studies literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Watt I. The Rise of the Novel. University of California Press; 1957.",
            "McKeon M. The Origins of the English Novel. Johns Hopkins University Press; 1987.",
        ],
        hypotheses=[
            "Medium matching explains the novel's career.",
            "The novel is dying.",
            "The novel will dominate indefinitely.",
            "New forms will replace it.",
        ],
        confirm="Persistence tracks interiority-demand measures.",
        refute="Screen narratives replace novels fully.",
    ),
    dict(
        key="literature-24",
        name="AI Writing: Is It Literature",
        group="Technology",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Is AI-generated writing literature - and who is the "
                 "author?"),
        background=("AI systems write fluently; the questions mirror "
                    "music and art (see musicology-24, art-history-24): "
                    "authorship, intentionality, and the meaning "
                    "deficit. Whether machine prose counts as "
                    "literature remains open."),
        why_it_matters=("AI writing reshapes literary labor and meaning. "
                        "Its status determines the industry."),
        sig_lens=("The Signature lens treats AI writing as a "
                  "control ledger: the Signature approach asks what "
                  "the human controls."),
        sig_body=("The Signature proposal models AI writing's status "
                  "as control-dependent. Assumptions: (1) prompting, "
                  "selecting, and editing are authorial; (2) raw "
                  "output lacks intention; (3) reception shows the "
                  "meaning deficit. Reasoning path: the proposal "
                  "predicts literature-status should track human "
                  "creative control - which the photography parallel "
                  "supports. AI writing is then literature where "
                  "humans author meaningfully. Limits: the model "
                  "needs better control measures; the labor "
                  "questions need separate treatment."),
        pointer=('The Signature system models AI writing as control-dependent: literature where humans meaningfully author. The Signature test: status judgments track control measures. It would be refuted if raw output counts equally.'),
        key_points=[
            "AI writes fluently.",
            "Authorship and intentionality complicate.",
            "The meaning deficit appears in reception.",
            "Whether machine prose counts is open.",
        ],
        requirements=[
            "Human-control measures.",
            "Reception studies.",
            "Labor-impact analyses.",
        ],
        standards=[
            "Claims checked against the AI-writing literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bender EM et al. On the dangers of stochastic parrots. 2021.",
            "Underwood T. Distant Horizons. University of Chicago Press; 2019.",
        ],
        hypotheses=[
            "Control dependence explains AI writing's status.",
            "AI writing is fully literature.",
            "AI writing is not literature.",
            "The question dissolves with familiarity.",
        ],
        confirm="Status judgments track control measures.",
        refute="Raw output counts equally.",
    ),
    dict(
        key="literature-25",
        name="The Copyright Problem in Literature",
        group="Technology",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("Can copyright handle literary borrowing - influence, "
                 "allusion, and fan transformation?"),
        background=("Literature has always borrowed; the law draws "
                    "lines the practice ignores. Fan fiction, "
                    "retellings, and AI training all press the "
                    "boundaries. Whether the system can adapt "
                    "remains open."),
        why_it_matters=("Copyright shapes what writers dare. Its fit "
                        "determines creative freedom."),
        sig_lens=("The Signature lens treats copyright as a "
                  "borrowing ledger: the Signature approach asks "
                  "what the practice needs."),
        sig_body=("The Signature proposal models literary copyright "
                  "as practice-mismatched. Assumptions: (1) "
                  "borrowing is constitutive; (2) the law treats "
                  "it as exceptional; (3) chilling effects are "
                  "real. Reasoning path: the proposal predicts "
                  "the law should protect transformative use "
                  "broadly - which fair use does unevenly. Reform "
                  "is then borrowing-tolerant rules. Limits: the "
                  "model needs better chilling studies; the AI-"
                  "training question needs settling."),
        pointer=('The Signature system models literary copyright as practice-mismatched: reform toward borrowing-tolerant rules. The Signature test: chilling tracks legal-uncertainty measures. It would be refuted if writers ignore the legal risk.'),
        key_points=[
            "Literature has always borrowed.",
            "Fan fiction and retellings press boundaries.",
            "AI training raises new questions.",
            "Whether the system can adapt is open.",
        ],
        requirements=[
            "Chilling-effect studies.",
            "Borrowing-tolerance reforms.",
            "AI-training resolutions.",
        ],
        standards=[
            "Claims checked against the copyright literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Jaszi P. Toward a theory of copyright. 1991.",
            "Tushnet R. Legal fictions. 1997.",
        ],
        hypotheses=[
            "Practice mismatch explains dysfunction.",
            "Strong copyright protects authors.",
            "Borrowing tolerance harms originators.",
            "The system works adequately.",
        ],
        confirm="Chilling tracks legal-uncertainty measures.",
        refute="Writers ignore the legal risk.",
    ),
    dict(
        key="literature-26",
        name="Fan Fiction: Literature",
        group="Sociology",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("Is fan fiction literature - and what does it reveal "
                 "about authorship and reading?"),
        background=("Fan fiction is massive, skilled, and legally "
                    "gray; scholars debate its status. It reveals "
                    "reading as rewriting and communities as "
                    "co-authors. Whether it belongs in literary "
                    "study remains contested."),
        why_it_matters=("Fan fiction is the largest literary practice "
                        "few study. Its status determines the field's "
                        "breadth."),
        sig_lens=("The Signature lens treats fan fiction as a "
                  "participation ledger: the Signature approach asks "
                  "what readers do."),
        sig_body=("The Signature proposal models fan fiction as "
                  "participatory literature. Assumptions: (1) "
                  "readers rewrite; (2) communities judge quality; "
                  "(3) the practice is literary by function. "
                  "Reasoning path: the proposal predicts fan works "
                  "should show literary craft - which they do. "
                  "The boundary is then institutional, not "
                  "aesthetic: study the practice, not the "
                  "prejudice. Limits: the model needs better "
                  "quality studies; the legal question persists."),
        pointer=('The Signature system models fan fiction as participatory literature: the boundary is institutional, not aesthetic. The Signature test: craft measures match commercial fiction. It would be refuted if fan works show no literary craft.'),
        key_points=[
            "Fan fiction is massive and often skilled.",
            "It reveals reading as rewriting.",
            "Communities function as co-authors.",
            "Whether it belongs in literary study is contested.",
        ],
        requirements=[
            "Quality evaluations.",
            "Community-practice studies.",
            "Legal-status analyses.",
        ],
        standards=[
            "Claims checked against the fan-studies literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Jenkins H. Textual Poachers. Routledge; 1992.",
            "Derecho A. Archontic literature. 2006.",
        ],
        hypotheses=[
            "Participatory literature captures fan fiction.",
            "It is derivative non-literature.",
            "It surpasses commercial fiction.",
            "The legal gray zone defines it.",
        ],
        confirm="Craft measures match commercial fiction.",
        refute="Fan works show no literary craft.",
    ),
    dict(
        key="literature-27",
        name="The Bestseller Problem",
        group="Sociology",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("Why do bestsellers sell - quality, marketing, or "
                 "cumulative advantage?"),
        background=("Bestseller lists show extreme concentration; "
                    "the causes debated: quality signals, marketing "
                    "spend, or rich-get-richer dynamics (Salganik's "
                    "music-lab). Whether the market rewards the best "
                    "remains open."),
        why_it_matters=("Bestsellers shape what gets read. Their "
                        "drivers determine cultural selection."),
        sig_lens=("The Signature lens treats bestsellers as a "
                  "cumulative ledger: the Signature approach asks "
                  "what the cascade needs."),
        sig_body=("The Signature proposal models bestsellers as "
                  "cumulative-advantage. Assumptions: (1) initial "
                  "visibility is partly random; (2) visibility "
                  "breeds visibility; (3) quality sets a threshold. "
                  "Reasoning path: the proposal predicts success "
                  "should be unpredictable but quality-filtered - "
                  "which the evidence supports. The market then "
                  "rewards the good-enough lucky. Limits: the model "
                  "needs better threshold studies; the marketing-"
                  "spend question needs separating."),
        pointer=('The Signature system models bestsellers as cumulative advantage: the market rewards the good-enough lucky. The Signature test: success tracks visibility-cascade measures. It would be refuted if quality alone predicts bestsellers.'),
        key_points=[
            "Bestseller lists show extreme concentration.",
            "Quality, marketing, and cascades compete as explanations.",
            "Success is unpredictable but quality-filtered.",
            "Whether the market rewards the best is open.",
        ],
        requirements=[
            "Threshold studies.",
            "Marketing-spend separations.",
            "Cascade experiments.",
        ],
        standards=[
            "Claims checked against the cultural-markets literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Salganik MJ et al. Experimental study of inequality and unpredictability. Science; 2006.",
            "Thompson JB. Merchants of Culture. Polity; 2010.",
        ],
        hypotheses=[
            "Cumulative advantage explains bestsellers.",
            "Quality determines success.",
            "Marketing determines success.",
            "Success is pure luck.",
        ],
        confirm="Success tracks visibility-cascade measures.",
        refute="Quality alone predicts bestsellers.",
    ),
    dict(
        key="literature-28",
        name="Prize Culture: Does It Work",
        group="Sociology",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Do literary prizes serve literature - or distort it?"),
        background=("Prizes consecrate and sell; critics allege they "
                    "homogenize (prize-friendly novels) and entrench "
                    "networks. Whether the prize system helps readers "
                    "find quality or narrows literature remains open."),
        why_it_matters=("Prizes shape literary prestige and sales. "
                        "Their effects determine cultural selection."),
        sig_lens=("The Signature lens treats prizes as a "
                  "consecration ledger: the Signature approach asks "
                  "what the prize does to the book."),
        sig_body=("The Signature proposal models prizes as "
                  "consecration-with-distortion. Assumptions: (1) "
                  "prizes signal quality usefully; (2) writers "
                  "anticipate judging tastes; (3) the anticipation "
                  "homogenizes. Reasoning path: the proposal "
                  "predicts prize-winning should boost sales while "
                  "narrowing the aesthetic - which the evidence "
                  "supports. Reform is then about judging "
                  "diversity, not abolition. Limits: the model "
                  "needs better homogenization measures; the "
                  "counterfactual (no prizes) needs imagining."),
        pointer=('The Signature system models prizes as consecration with distortion: useful signals that narrow aesthetics; diversify judging. The Signature test: aesthetics narrow with prize anticipation. It would be refuted if prized books show full diversity.'),
        key_points=[
            "Prizes consecrate and boost sales.",
            "Critics allege homogenization.",
            "Writers anticipate judging tastes.",
            "Whether prizes help or narrow is open.",
        ],
        requirements=[
            "Homogenization measures.",
            "Judging-diversity evaluations.",
            "Counterfactual analyses.",
        ],
        standards=[
            "Claims checked against the prize literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "English JF. The Economy of Prestige. Harvard University Press; 2005.",
            "Norris S. The Booker Prize. 2015.",
        ],
        hypotheses=[
            "Consecration-distortion explains prize effects.",
            "Prizes purely serve literature.",
            "Prizes purely distort.",
            "Abolition is the answer.",
        ],
        confirm="Aesthetics narrow with prize anticipation.",
        refute="Prized books show full diversity.",
    ),
    dict(
        key="literature-29",
        name="The MFA Problem",
        group="Sociology",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("Do MFA programs help or harm literature - professionalizing "
                 "or homogenizing it?"),
        background=("MFAs proliferated; graduates dominate publishing. "
                    "Critics allege workshop homogenization (the "
                    "'MFA style'); defenders cite craft transmission. "
                    "Whether the programs narrow American fiction "
                    "remains open."),
        why_it_matters=("MFAs train most published writers. Their "
                        "effects shape national literature."),
        sig_lens=("The Signature lens treats MFAs as a training "
                  "ledger: the Signature approach asks what the "
                  "workshop teaches."),
        sig_body=("The Signature proposal models MFA effects as "
                  "craft-plus-convergence. Assumptions: (1) "
                  "workshops teach real craft; (2) peer "
                  "environments converge aesthetics; (3) both "
                  "operate. Reasoning path: the proposal predicts "
                  "graduates should write competently and similarly "
                  "- which the evidence supports. The programs are "
                  "then good for craft, risky for diversity. Limits: "
                  "the model needs better convergence measures; the "
                  "access question (who can afford MFAs) needs "
                  "centering."),
        pointer=('The Signature system models MFA effects as craft plus convergence: good for technique, risky for aesthetic diversity. The Signature test: graduate work shows craft plus similarity. It would be refuted if mFA graduates write diversely.'),
        key_points=[
            "MFAs proliferated; graduates dominate publishing.",
            "Critics allege workshop homogenization.",
            "Defenders cite craft transmission.",
            "Whether programs narrow fiction is open.",
        ],
        requirements=[
            "Convergence measures.",
            "Craft-transmission evaluations.",
            "Access-equity analyses.",
        ],
        standards=[
            "Claims checked against the creative-writing literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "McGurl M. The Program Era. Harvard University Press; 2009.",
            "Aldridge JW. Talents and Technicians. 1992.",
        ],
        hypotheses=[
            "Craft-convergence explains MFA effects.",
            "MFAs purely help literature.",
            "MFAs purely harm it.",
            "The effects are overstated.",
        ],
        confirm="Graduate work shows craft plus similarity.",
        refute="MFA graduates write diversely.",
    ),
    dict(
        key="literature-30",
        name="Reading in the Digital Age",
        group="Technology",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("How is digital reading changing comprehension - and "
                 "should we worry?"),
        background=("Screen reading shows shallower comprehension "
                    "in studies (the shallowing hypothesis); "
                    "e-books, audiobooks, and phones reshape habits. "
                    "Whether the effects are medium-specific or "
                    "practice-specific remains open."),
        why_it_matters=("Reading is cognition's foundation. The "
                        "medium's effects determine literacy's "
                        "future."),
        sig_lens=("The Signature lens treats reading as a practice "
                  "ledger: the Signature approach asks what "
                  "readers do differently."),
        sig_body=("The Signature proposal models digital-reading "
                  "effects as practice-mediated. Assumptions: (1) "
                  "screens invite skimming; (2) skimming shallows "
                  "comprehension; (3) the medium enables but does "
                  "not force. Reasoning path: the proposal predicts "
                  "deep reading should survive on screens with "
                  "intentional practice - which the evidence "
                  "supports. The worry is then about habits, not "
                  "hardware. Limits: the model needs better "
                  "practice studies; the developmental effects "
                  "need tracking."),
        pointer=('The Signature system models digital-reading effects as practice-mediated: habits, not hardware, determine depth. The Signature test: comprehension tracks practice measures. It would be refuted if medium alone determines depth.'),
        key_points=[
            "Screen reading shows shallower comprehension.",
            "E-books and audiobooks reshape habits.",
            "The shallowing hypothesis is debated.",
            "Whether effects are medium or practice remains open.",
        ],
        requirements=[
            "Practice-mediation studies.",
            "Developmental tracking.",
            "Deep-reading intervention trials.",
        ],
        standards=[
            "Claims checked against the reading literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mangen A et al. Reading linear texts on paper versus computer screen. 2013.",
            "Wolf M. Reader, Come Home. Harper; 2018.",
        ],
        hypotheses=[
            "Practice mediation explains the effects.",
            "Screens inherently shallow reading.",
            "No real effect exists.",
            "Audiobooks change everything.",
        ],
        confirm="Comprehension tracks practice measures.",
        refute="Medium alone determines depth.",
    ),
    dict(
        key="literature-31",
        name="The Attention Problem in Reading",
        group="Psychology",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("Can sustained reading survive the attention economy - "
                 "and what does it need?"),
        background=("Deep reading needs sustained attention; the "
                    "attention economy fragments it. Readers report "
                    "declining capacity for long books. Whether the "
                    "capacity is lost or the habit is neglected "
                    "remains open."),
        why_it_matters=("Sustained reading underpins thought. Its "
                        "survival determines intellectual culture."),
        sig_lens=("The Signature lens treats reading attention as a "
                  "habit ledger: the Signature approach asks what "
                  "practices sustain it."),
        sig_body=("The Signature proposal models reading attention "
                  "as habit-maintained. Assumptions: (1) attention "
                  "is trainable; (2) environments shape habits; (3) "
                  "the capacity persists. Reasoning path: the "
                  "proposal predicts readers with protected "
                  "practices should sustain depth - which they do. "
                  "The answer is then attention hygiene, not "
                  "lamentation. Limits: the model needs better "
                  "habit studies; the structural (platform) "
                  "question needs addressing."),
        pointer=('The Signature system models reading attention as habit-maintained: protected practices sustain depth. The Signature test: depth tracks practice-protection measures. It would be refuted if protected readers decline equally.'),
        key_points=[
            "Deep reading needs sustained attention.",
            "The attention economy fragments it.",
            "Readers report declining capacity.",
            "Whether capacity or habit is the issue is open.",
        ],
        requirements=[
            "Habit-sustenance studies.",
            "Attention-hygiene trials.",
            "Structural-platform analyses.",
        ],
        standards=[
            "Claims checked against the attention literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wolf M. Reader, Come Home. Harper; 2018.",
            "Mark G. Attention Span. Hanover Square; 2023.",
        ],
        hypotheses=[
            "Habit maintenance explains sustained reading.",
            "Capacity is genuinely declining.",
            "Technology makes depth impossible.",
            "The worry is moral panic.",
        ],
        confirm="Depth tracks practice-protection measures.",
        refute="Protected readers decline equally.",
    ),
    dict(
        key="literature-32",
        name="Literature and Empathy: Proven",
        group="Psychology",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("Does reading literature increase empathy - and is the "
                 "evidence convincing?"),
        background=("Kidd and Castano found literary fiction boosts "
                    "theory of mind; replications were mixed. The "
                    "current state: small effects, contested "
                    "mechanisms. Whether literature builds empathy "
                    "remains psychology's literary question."),
        why_it_matters=("Empathy is literature's great claim. Its "
                        "proof determines the humanities' defense."),
        sig_lens=("The Signature lens treats the effect as a "
                  "simulation ledger: the Signature approach asks "
                  "what reading rehearses."),
        sig_body=("The Signature proposal models empathy effects as "
                  "simulation-practice. Assumptions: (1) fiction "
                  "simulates minds; (2) simulation practices "
                  "mind-reading; (3) practice transfers modestly. "
                  "Reasoning path: the proposal predicts small "
                  "but real effects - which the meta-analyses "
                  "support. Literature then modestly builds "
                  "empathy: the claim is true but smaller than "
                  "hoped. Limits: the model needs better "
                  "transfer studies; the mechanism needs "
                  "tightening."),
        pointer=("The Signature system models literature's empathy effect as real but small: simulation practice transfers modestly. The Signature test: effects track simulation-demand measures. It would be refuted if no effect survives preregistration."),
        key_points=[
            "Initial findings showed theory-of-mind boosts.",
            "Replications were mixed.",
            "Meta-analyses find small effects.",
            "Whether the claim holds remains contested.",
        ],
        requirements=[
            "Transfer studies.",
            "Mechanism investigations.",
            "Dose-response analyses.",
        ],
        standards=[
            "Claims checked against the empathy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kidd DC, Castano E. Reading literary fiction improves theory of mind. Science; 2013.",
            "Dodell-Feder D, Tamir DI. Fiction reading has a small positive impact. 2018.",
        ],
        hypotheses=[
            "Simulation practice explains the small effect.",
            "The effect is illusory.",
            "The effect is large but unmeasured.",
            "Only literary fiction works.",
        ],
        confirm="Effects track simulation-demand measures.",
        refute="No effect survives preregistration.",
    ),
    dict(
        key="literature-33",
        name="The Postcolonial Canon",
        group="History",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("What does a postcolonial canon look like - beyond "
                 "adding writers?"),
        background=("Postcolonial literature reshaped English studies; "
                    "the deeper question is structural: canons, "
                    "periods, and genres built on empire. Whether "
                    "decolonization transforms or merely expands "
                    "remains contested."),
        why_it_matters=("Postcolonial canons reshape global literary "
                        "study. Their depth determines honesty."),
        sig_lens=("The Signature lens treats postcolonial canons as a "
                  "structure ledger: the Signature approach asks "
                  "which structures carry empire."),
        sig_body=("The Signature proposal models postcolonial "
                  "canonization as structure-targeted. Assumptions: "
                  "(1) imperial logic lives in categories; (2) "
                  "adding writers leaves categories intact; (3) "
                  "structural change is the test. Reasoning path: "
                  "the proposal predicts genuine transformation "
                  "should remake periods and genres - which the "
                  "leading work does. Addition is necessary but "
                  "insufficient. Limits: the model needs better "
                  "structural-change measures; the nativism risk "
                  "needs guarding."),
        pointer=('The Signature system models postcolonial canonization as structure-targeted: remake categories, not just rosters. The Signature test: change tracks structural measures. It would be refuted if additive inclusion transforms the field.'),
        key_points=[
            "Postcolonial literature reshaped English studies.",
            "Imperial logic lives in categories.",
            "Adding writers leaves structures intact.",
            "Whether transformation or expansion is happening is contested.",
        ],
        requirements=[
            "Structural-change measures.",
            "Category-remaking studies.",
            "Nativism guards.",
        ],
        standards=[
            "Claims checked against the postcolonial literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Said EW. Culture and Imperialism. Knopf; 1993.",
            "Spivak GC. Death of a Discipline. Columbia University Press; 2003.",
        ],
        hypotheses=[
            "Structure targeting defines real change.",
            "Addition suffices.",
            "The categories are neutral.",
            "Decolonization is incoherent.",
        ],
        confirm="Change tracks structural measures.",
        refute="Additive inclusion transforms the field.",
    ),
    dict(
        key="literature-34",
        name="A Unified Theory of Literature",
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can literary theory unify - formalism, history, "
                 "sociology, and psychology - into one account?"),
        background=("Each approach captures something: formalism the "
                    "text, history the change, sociology the "
                    "institution, psychology the reader. Unification "
                    "attempts remain programmatic. Whether "
                    "literature's nature permits one theory is the "
                    "discipline's capstone."),
        why_it_matters=("This is literary study's capstone: the answer "
                        "determines what literature is."),
        sig_lens=("The Signature lens treats the approaches as a "
                  "question ledger: the Signature approach asks what "
                  "question each owns."),
        sig_body=("The Signature proposal models unification as "
                  "question-integration. Assumptions: (1) literature "
                  "spans text, history, institution, and reader; "
                  "(2) each approach owns questions; (3) the "
                  "questions interlock. Reasoning path: the proposal "
                  "assigns formalism to text, history to change, "
                  "sociology to institution, psychology to reader - "
                  "with literary practice as the integrator. Unity "
                  "comes from the practice that holds the questions "
                  "together. Limits: the integration is sketched; "
                  "partisans may reject the settlement."),
        pointer=('The Signature system assigns each approach its questions about literature, with literary practice as the integrator. The Signature test: integrated models predict across questions. It would be refuted if questions prove irreducible to common theory.'),
        key_points=[
            "Four approaches offer incompatible images of literature.",
            "Each captures what the others miss.",
            "Unification attempts remain programmatic.",
            "Whether one theory is possible is foundational.",
        ],
        requirements=[
            "A question architecture for the approaches.",
            "An account of question interlock.",
            "Testable implications of the integration.",
        ],
        standards=[
            "Claims checked against the literary-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Eagleton T. Literary Theory. University of Minnesota Press; 1983.",
            "Culler J. Literary Theory: A Very Short Introduction. Oxford University Press; 1997.",
        ],
        hypotheses=[
            "Question-integration unifies literary theory.",
            "The approaches are incommensurable.",
            "One approach will absorb the rest.",
            "Pluralism is permanent.",
        ],
        confirm="Integrated models predict across questions.",
        refute="Questions prove irreducible to common theory.",
    ),
]
