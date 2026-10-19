#!/usr/bin/env python3
"""Entries for the Unsolved Art History databases (batch 4).

34 famous open problems in art history, ladder-ordered by accessibility.
ID prefixes: JAH-USAH- (public) and JAH-USAHS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="art-history-01",
        name="What Is Art",
        group="Theory",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("What is art - can the concept be defined, or should "
                 "definition be abandoned?"),
        background=("Definitions failed serially (representation, "
                    "expression, form); Weitz argued art is an open "
                    "concept; institutional theories (Danto, Dickie) "
                    "define by artworld status. Whether definition is "
                    "possible or desirable remains the founding "
                    "question."),
        why_it_matters=("The definition bounds the field. Its fate "
                        "determines art history's scope."),
        sig_lens=("The Signature lens treats definition as a use "
                  "ledger: the Signature approach asks what the "
                  "concept does."),
        sig_body=("The Signature proposal models 'art' as a "
                  "cluster-practice concept. Assumptions: (1) no "
                  "single essence covers cases; (2) family "
                  "resemblances plus institutional roles organize "
                  "use; (3) borderline cases are productive. "
                  "Reasoning path: the proposal predicts definitional "
                  "disputes should track institutional stakes - "
                  "which they do. The concept works without essence: "
                  "use the cluster, argue the borders. Limits: the "
                  "model needs better borderline analyses; the "
                  "normative dimension (what deserves the name) "
                  "persists."),
        pointer=('The Signature system models art as a cluster-practice concept: no essence, family resemblances plus institutional roles. The Signature test: disputes track institutional stakes. It would be refuted if an essential definition succeeds.'),
        key_points=[
            "Essential definitions failed serially.",
            "Institutional theories define by artworld status.",
            "Weitz proposed the open concept.",
            "Whether definition is possible remains foundational.",
        ],
        requirements=[
            "Borderline-case analyses.",
            "Institutional-stake studies.",
            "An account of the concept's normativity.",
        ],
        standards=[
            "Claims checked against the aesthetics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weitz M. The role of theory in aesthetics. 1956.",
            "Danto AC. The artworld. 1964.",
        ],
        hypotheses=[
            "Cluster-practice explains definitional debates.",
            "An essence exists undiscovered.",
            "The concept should be abandoned.",
            "Institutional theory suffices.",
        ],
        confirm="Disputes track institutional stakes.",
        refute="An essential definition succeeds.",
    ),
    dict(
        key="art-history-02",
        name="Why Art Evolved",
        group="Psychology",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Why did art evolve - sexual display, social bonding, "
                 "or cognitive play?"),
        background=("Art is ancient (100,000-year-old ochre, 40,000-"
                    "year-old caves) and costly. Theories: sexual "
                    "selection (Miller), social cohesion, and "
                    "cognitive development. The adaptive function - "
                    "if any - remains open."),
        why_it_matters=("Art's origin explains its hold. The function "
                        "determines the theory."),
        sig_lens=("The Signature lens treats art's origin as a cost "
                  "ledger: the Signature approach asks what the "
                  "cost buys."),
        sig_body=("The Signature proposal models art's origin as "
                  "multi-functional. Assumptions: (1) art is too "
                  "costly for no function; (2) different arts serve "
                  "different functions; (3) functions layered over "
                  "time. Reasoning path: the proposal predicts "
                  "origins should be plural - display, bonding, "
                  "cognition together - explaining the inconclusive "
                  "single-theory debates. Art evolved as a "
                  "multi-tool. Limits: the model needs better "
                  "archaeological evidence; the function-layering "
                  "needs sequencing."),
        pointer=("The Signature system models art's origin as multi-functional: display, bonding, and cognition layered over time. The Signature test: evidence supports multiple functions. It would be refuted if one function explains the record."),
        key_points=[
            "Art is ancient and costly.",
            "Sexual selection, bonding, and cognition compete.",
            "Archaeology shows deep antiquity.",
            "The adaptive function remains open.",
        ],
        requirements=[
            "Archaeological function evidence.",
            "Multi-function sequencing.",
            "An account of the costliness.",
        ],
        standards=[
            "Claims checked against the art-origins literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Miller GF. The Mating Mind. Doubleday; 2000.",
            "Dissanayake E. Homo Aestheticus. University of Washington Press; 1992.",
        ],
        hypotheses=[
            "Multi-functionality explains the debates.",
            "Sexual selection drove art.",
            "Social bonding drove art.",
            "Art is a spandrel.",
        ],
        confirm="Evidence supports multiple functions.",
        refute="One function explains the record.",
    ),
    dict(
        key="art-history-03",
        name="The Aesthetic Experience Problem",
        group="Psychology",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("What happens in aesthetic experience - and is it "
                 "distinct from ordinary perception?"),
        background=("Aesthetic experience involves attention, emotion, "
                    "and meaning; whether it is a distinct mental "
                    "state or ordinary perception plus framing is "
                    "debated. Neuroaesthetics finds reward-circuit "
                    "involvement but not a dedicated module."),
        why_it_matters=("Aesthetic experience is art's core. Its nature "
                        "determines the field's psychology."),
        sig_lens=("The Signature lens treats the experience as a "
                  "framing ledger: the Signature approach asks what "
                  "the aesthetic frame adds."),
        sig_body=("The Signature proposal models aesthetic experience "
                  "as framed perception. Assumptions: (1) the "
                  "perceptual machinery is ordinary; (2) the "
                  "aesthetic frame (attention, expectation, "
                  "meaning-seeking) transforms it; (3) no dedicated "
                  "module exists. Reasoning path: the proposal "
                  "predicts framing manipulations should create "
                  "aesthetic experience from ordinary objects - "
                  "which they do (readymades, see art-history-19). "
                  "The experience is then in the stance, not the "
                  "stimulus. Limits: the model needs better "
                  "framing studies; the emotion dimension needs "
                  "integrating."),
        pointer=('The Signature system models aesthetic experience as framed perception: the stance, not the stimulus, makes it aesthetic. The Signature test: framing creates aesthetic experience experimentally. It would be refuted if stimulus properties determine experience.'),
        key_points=[
            "Aesthetic experience involves attention and emotion.",
            "No dedicated neural module is found.",
            "Framing transforms ordinary perception.",
            "Whether it is distinct remains debated.",
        ],
        requirements=[
            "Framing-manipulation studies.",
            "Emotion-integration analyses.",
            "An account of the stance.",
        ],
        standards=[
            "Claims checked against the neuroaesthetics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Leder H et al. A model of aesthetic appreciation. 2004.",
            "Chatterjee A. The Aesthetic Brain. Oxford University Press; 2014.",
        ],
        hypotheses=[
            "Framed perception explains the experience.",
            "A distinct aesthetic state exists.",
            "The experience is ineffable.",
            "Context determines everything.",
        ],
        confirm="Framing creates aesthetic experience experimentally.",
        refute="Stimulus properties determine experience.",
    ),
    dict(
        key="art-history-04",
        name="Beauty: Objective or Not",
        group="Theory",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Is beauty objective - in the object - or in the eye of "
                 "the beholder?"),
        background=("Hume made taste subjective but standardizable; "
                    "Kant made beauty universal-but-subjective; "
                    "empirical aesthetics finds real agreement on "
                    "faces and landscapes, less on art. The "
                    "objectivity question persists at art's center."),
        why_it_matters=("Beauty's status determines criticism's "
                        "authority. The answer shapes the discipline."),
        sig_lens=("The Signature lens treats beauty as an agreement "
                  "ledger: the Signature approach asks where "
                  "judgments converge."),
        sig_body=("The Signature proposal models beauty judgments as "
                  "layered (see architecture-05). Assumptions: (1) "
                  "perceptual preferences are widely shared; (2) "
                  "artistic judgments add cultural layers; (3) the "
                  "layers interact. Reasoning path: the proposal "
                  "predicts convergence on perceptual beauty and "
                  "divergence on artistic - which the evidence "
                  "supports. Beauty is then partly objective "
                  "(the shared layer), partly cultural. Limits: the "
                  "model needs better layer separations; the "
                  "normative question (what should please) persists."),
        pointer=('The Signature system models beauty as layered: a shared perceptual core beneath cultural variation. The Signature test: agreement concentrates at the perceptual layer. It would be refuted if no cross-cultural agreement exists.'),
        key_points=[
            "Empirical aesthetics finds real agreement.",
            "Art judgments diverge more than perceptual ones.",
            "Hume and Kant framed the classic positions.",
            "The objectivity question persists.",
        ],
        requirements=[
            "Layer-separation studies.",
            "Cross-cultural agreement mapping.",
            "Normative-dimension analyses.",
        ],
        standards=[
            "Claims checked against the empirical-aesthetics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hume D. Of the standard of taste. 1757.",
            "Reber R et al. Processing fluency and aesthetic pleasure. 2004.",
        ],
        hypotheses=[
            "Layered beauty explains agreement patterns.",
            "Beauty is fully subjective.",
            "Beauty is fully objective.",
            "The question is unanswerable.",
        ],
        confirm="Agreement concentrates at the perceptual layer.",
        refute="No cross-cultural agreement exists.",
    ),
    dict(
        key="art-history-05",
        name="Forgery: Why It Matters",
        group="Practice",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("Why does forgery matter - if the fake is visually "
                 "identical, what is lost?"),
        background=("Perfect forgeries fool experts; when exposed, "
                    "the aesthetic experience collapses - though "
                    "nothing visual changed. The puzzle: what "
                    "authenticity adds. Theories: historical "
                    "connection, achievement admiration, market "
                    "honesty."),
        why_it_matters=("Forgery is art's crime. Its wrongness reveals "
                        "what art values."),
        sig_lens=("The Signature lens treats forgery as a history "
                  "ledger: the Signature approach asks what "
                  "authenticity connects."),
        sig_body=("The Signature proposal models forgery's wrongness "
                  "as historical-connection theft. Assumptions: (1) "
                  "art's value includes its history; (2) forgeries "
                  "fake the history; (3) the visual is not all. "
                  "Reasoning path: the proposal predicts the "
                  "experience collapse on exposure - because the "
                  "historical connection was the load-bearing value. "
                  "Forgery matters because art is partly about "
                  "contact with its makers. Limits: the model needs "
                  "better exposure-effect studies; the market "
                  "dimension needs separating."),
        pointer=("The Signature system models forgery's wrongness as historical-connection theft: art's value includes contact with its makers. The Signature test: experience collapses track history-beliefs. It would be refuted if undetected forgeries satisfy equally."),
        key_points=[
            "Perfect forgeries fool experts visually.",
            "Exposure collapses the experience.",
            "Nothing visual changes on exposure.",
            "What authenticity adds is the puzzle.",
        ],
        requirements=[
            "Exposure-effect studies.",
            "Historical-connection value analyses.",
            "Market-versus-aesthetic separations.",
        ],
        standards=[
            "Claims checked against the forgery literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Lessing A. What is wrong with a forgery? 1965.",
            "Dutton D. Artistic crimes. 1983.",
        ],
        hypotheses=[
            "Historical connection explains forgery's wrongness.",
            "Only the market is harmed.",
            "Forgery is victimless if undetected.",
            "Achievement admiration is the key.",
        ],
        confirm="Experience collapses track history-beliefs.",
        refute="Undetected forgeries satisfy equally.",
    ),
    dict(
        key="art-history-06",
        name="The Attribution Problem",
        group="Practice",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("How do we know who made an artwork - and how certain "
                 "can attribution be?"),
        background=("Connoisseurship (Morelli's ears and hands), "
                    "scientific analysis (pigments, dendrochronology), "
                    "and provenance all contribute; disputes persist "
                    "(Leonardo's Salvator Mundi). Whether attribution "
                    "can be certain - and how much it matters - "
                    "remains open."),
        why_it_matters=("Attribution determines value and history. Its "
                        "certainty bounds the market and scholarship."),
        sig_lens=("The Signature lens treats attribution as an "
                  "evidence ledger: the Signature approach asks what "
                  "each method proves."),
        sig_body=("The Signature proposal models attribution as "
                  "convergent-probabilistic. Assumptions: (1) no "
                  "single method is decisive; (2) convergence "
                  "raises confidence; (3) certainty is rare. "
                  "Reasoning path: the proposal predicts the "
                  "strongest attributions should combine methods - "
                  "which they do. Attribution is then Bayesian, not "
                  "demonstrative. Limits: the model needs better "
                  "method-weighting; the market's certainty-demand "
                  "needs critiquing."),
        pointer=('The Signature system models attribution as convergent-probabilistic: Bayesian, not demonstrative. The Signature test: confidence tracks method convergence. It would be refuted if single methods prove decisive.'),
        key_points=[
            "Connoisseurship, science, and provenance combine.",
            "Disputes persist on major works.",
            "No single method is decisive.",
            "Whether certainty is possible is open.",
        ],
        requirements=[
            "Method-weighting frameworks.",
            "Dispute case studies.",
            "Market-certainty critiques.",
        ],
        standards=[
            "Claims checked against the attribution literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Morelli G. Italian Painters. 1892.",
            "Bomford D. Art in the Making. National Gallery; 2002.",
        ],
        hypotheses=[
            "Convergent-probabilistic captures attribution.",
            "Science will deliver certainty.",
            "Connoisseurship is irreducibly subjective.",
            "Attribution matters less than claimed.",
        ],
        confirm="Confidence tracks method convergence.",
        refute="Single methods prove decisive.",
    ),
    dict(
        key="art-history-07",
        name="Style: What Is It",
        group="Theory",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("What is style - the artist's fingerprint, the period's "
                 "uniform, or a scholarly fiction?"),
        background=("Style organizes art history (Gothic, Baroque); "
                    "yet its ontology is murky - is it in the "
                    "works, the makers, or the historians? "
                    "Schapiro, Gombrich, and others debated without "
                    "settlement."),
        why_it_matters=("Style is art history's master concept. Its "
                        "nature determines the discipline's validity."),
        sig_lens=("The Signature lens treats style as a grouping "
                  "ledger: the Signature approach asks what the "
                  "grouping explains."),
        sig_body=("The Signature proposal models style as "
                  "explanatory-grouping. Assumptions: (1) style "
                  "terms group works usefully; (2) the groups "
                  "track real patterns; (3) reification is the "
                  "risk. Reasoning path: the proposal predicts "
                  "style concepts should earn their keep "
                  "predictively - which the best do. Style is then "
                  "a tool, not a thing: keep the tool, watch the "
                  "reification. Limits: the model needs better "
                  "predictive tests; the period-style question "
                  "needs separating."),
        pointer=('The Signature system models style as an explanatory grouping: a tool, not a thing. The Signature test: style terms predict unexamined works. It would be refuted if style groupings prove arbitrary.'),
        key_points=[
            "Style organizes art history's narratives.",
            "Its ontology is murky.",
            "Reification is the perennial risk.",
            "Whether style is real remains debated.",
        ],
        requirements=[
            "Predictive tests of style concepts.",
            "Reification critiques.",
            "Period-versus-personal style separations.",
        ],
        standards=[
            "Claims checked against the style literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Schapiro M. Style. 1953.",
            "Gombrich EH. Art and Illusion. Phaidon; 1960.",
        ],
        hypotheses=[
            "Explanatory grouping captures style.",
            "Style is a real entity.",
            "Style is scholarly fiction.",
            "Only individual style is real.",
        ],
        confirm="Style terms predict unexamined works.",
        refute="Style groupings prove arbitrary.",
    ),
    dict(
        key="art-history-08",
        name="Periodization: Real or Imposed",
        group="History",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Are art-historical periods real - or impositions that "
                 "distort the past?"),
        background=("Renaissance, Baroque, Modern: the periods "
                    "organize teaching and museums, but transitions "
                    "are gradual and the boundaries leak. Whether "
                    "periods carve nature at its joints or impose "
                    "order remains open."),
        why_it_matters=("Periods shape every survey. Their reality "
                        "determines the narrative's truth."),
        sig_lens=("The Signature lens treats periods as a boundary "
                  "ledger: the Signature approach asks what happens "
                  "at the edges."),
        sig_body=("The Signature proposal models periods as "
                  "useful-fuzzy. Assumptions: (1) real changes "
                  "cluster in time; (2) boundaries are gradual; "
                  "(3) the fuzziness is honest. Reasoning path: the "
                  "proposal predicts period concepts should work "
                  "for centers and blur at edges - which they do. "
                  "Periods are then real patterns with imposed "
                  "edges: keep the patterns, soften the borders. "
                  "Limits: the model needs better change-clustering "
                  "studies; the pedagogical need needs honoring."),
        pointer=('The Signature system models periods as real patterns with imposed edges: keep the patterns, soften the borders. The Signature test: change clusters support period centers. It would be refuted if no temporal clustering is found.'),
        key_points=[
            "Periods organize teaching and museums.",
            "Transitions are gradual; boundaries leak.",
            "Whether periods are real remains open.",
            "The narrative's truth is at stake.",
        ],
        requirements=[
            "Change-clustering studies.",
            "Boundary-fuzziness documentation.",
            "Pedagogical-function analyses.",
        ],
        standards=[
            "Claims checked against the historiography literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kubler G. The Shape of Time. Yale University Press; 1962.",
            "Belting H. Art History After Modernism. University of Chicago Press; 2003.",
        ],
        hypotheses=[
            "Useful-fuzzy captures periods.",
            "Periods are fully real.",
            "Periods are pure imposition.",
            "The concept should be abandoned.",
        ],
        confirm="Change clusters support period centers.",
        refute="No temporal clustering is found.",
    ),
    dict(
        key="art-history-09",
        name="The Canon Problem in Art",
        group="History",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("Who decides art's canon - and can it be opened without "
                 "losing standards?"),
        background=("The Western canon dominated museums and surveys; "
                    "expansion (women artists, global art) faces the "
                    "standards question: inclusion by merit or by "
                    "justice? Whether canons can be both open and "
                    "excellent remains open."),
        why_it_matters=("Canons shape what humanity preserves. Their "
                        "justice determines cultural memory."),
        sig_lens=("The Signature lens treats canons as a standard "
                  "ledger: the Signature approach asks what "
                  "excellence means across traditions."),
        sig_body=("The Signature proposal models canon expansion as "
                  "standard-pluralizing. Assumptions: (1) excellence "
                  "criteria are tradition-relative; (2) the old "
                  "canon used one tradition's criteria; (3) "
                  "plural criteria enable just expansion. Reasoning "
                  "path: the proposal predicts successful "
                  "expansions should articulate the included "
                  "traditions' own excellences - which the best "
                  "curatorial work does. Open by pluralizing "
                  "standards, not abandoning them. Limits: the model "
                  "needs better expansion evaluations; the "
                  "relativism risk needs guarding."),
        pointer=("The Signature system models canon expansion as standard-pluralizing: articulate each tradition's own excellences. The Signature test: expansions succeed with articulated standards. It would be refuted if no standards survive pluralization."),
        key_points=[
            "The Western canon dominated institutions.",
            "Expansion faces the standards question.",
            "Merit versus justice framings compete.",
            "Whether open canons keep excellence is open.",
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
            "Nochlin L. Why have there been no great women artists? 1971.",
            "Elkins J. Is Art History Global? Routledge; 2007.",
        ],
        hypotheses=[
            "Standard pluralization opens canons justly.",
            "Universal standards exist.",
            "Canons are inherently exclusionary.",
            "Standards should be abandoned.",
        ],
        confirm="Expansions succeed with articulated standards.",
        refute="No standards survive pluralization.",
    ),
    dict(
        key="art-history-10",
        name="Why We Preserve Art",
        group="Practice",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Why preserve art - for whom, and at what cost?"),
        background=("Preservation consumes vast resources; the "
                    "justifications (heritage, education, beauty) "
                    "are rarely examined. Deaccessioning controversies "
                    "force the question: what deserves survival?"),
        why_it_matters=("Preservation allocates cultural resources. Its "
                        "reasons determine priorities."),
        sig_lens=("The Signature lens treats preservation as a "
                  "future ledger: the Signature approach asks what "
                  "we owe the unborn."),
        sig_body=("The Signature proposal models preservation as "
                  "intergenerational trusteeship. Assumptions: (1) "
                  "future people have interests in the past; (2) "
                  "we cannot know which works they will value; (3) "
                  "diversity hedges ignorance. Reasoning path: the "
                  "proposal predicts preservation should favor "
                  "breadth over perfection - explaining why "
                  "deaccessioning for operating costs betrays the "
                  "trust. Preserve diversely, judge lightly. Limits: "
                  "the model needs better cost-benefit frameworks; "
                  "the triage question persists."),
        pointer=('The Signature system models preservation as intergenerational trusteeship: preserve diversely, judge lightly. The Signature test: diverse holdings serve future interests. It would be refuted if narrow perfection outperforms breadth.'),
        key_points=[
            "Preservation consumes vast resources.",
            "Justifications are rarely examined.",
            "Deaccessioning forces the priority question.",
            "What deserves survival is open.",
        ],
        requirements=[
            "Cost-benefit frameworks.",
            "Triage-criteria development.",
            "Trusteeship-theory articulation.",
        ],
        standards=[
            "Claims checked against the preservation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Thompson MW. Ruins: Their Preservation and Display. British Museum; 1981.",
            "Lowenthal D. The Past Is a Foreign Country. Cambridge University Press; 1985.",
        ],
        hypotheses=[
            "Trusteeship grounds preservation duties.",
            "Only masterpieces deserve preservation.",
            "Preservation is unjustified luxury.",
            "Markets should decide.",
        ],
        confirm="Diverse holdings serve future interests.",
        refute="Narrow perfection outperforms breadth.",
    ),
    dict(
        key="art-history-11",
        name='What Are Museums For',
        group="Practice",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("What are museums for - temples of art, forums of "
                 "debate, or entertainment venues?"),
        background=("Cameron's temple-versus-forum framed the debate; "
                    "museums now chase attendance with blockbusters. "
                    "The missions (preserve, educate, include, "
                    "entertain) conflict. Whether one institution can "
                    "serve all remains open."),
        why_it_matters=("Museums are art's public face. Their purpose "
                        "determines cultural life."),
        sig_lens=("The Signature lens treats museums as a mission "
                  "ledger: the Signature approach asks which missions "
                  "conflict."),
        sig_body=("The Signature proposal models museums as "
                  "mission-plural. Assumptions: (1) the missions "
                  "genuinely conflict at the margin; (2) different "
                  "museums can specialize; (3) the blockbuster model "
                  "distorts. Reasoning path: the proposal predicts "
                  "the healthiest ecology should be differentiated "
                  "- temples, forums, and popular venues each "
                  "excellent - rather than every museum chasing all "
                  "missions. Differentiate, don't dilute. Limits: "
                  "the model needs better mission-conflict studies; "
                  "the funding question persists."),
        pointer=('The Signature system models museums as mission-plural: differentiate institutions rather than diluting each. The Signature test: outcomes track mission-clarity measures. It would be refuted if multi-mission museums outperform.'),
        key_points=[
            "Temple-versus-forum framed the debate.",
            "Blockbusters chase attendance.",
            "Missions conflict at the margin.",
            "Whether one institution serves all is open.",
        ],
        requirements=[
            "Mission-conflict studies.",
            "Differentiation-outcome research.",
            "Funding-model analyses.",
        ],
        standards=[
            "Claims checked against the museum-studies literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Cameron DF. The museum, a temple or the forum. 1971.",
            "Weil SE. Making Museums Matter. Smithsonian; 2002.",
        ],
        hypotheses=[
            "Differentiation resolves mission conflict.",
            "One museum can serve all missions.",
            "Entertainment corrupts museums.",
            "The temple model is obsolete.",
        ],
        confirm="Outcomes track mission-clarity measures.",
        refute="Multi-mission museums outperform.",
    ),
    dict(
        key="art-history-12",
        name="Looted Art: Who Owns It",
        group="Ethics",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Who owns looted art - the museum that holds it, the "
                 "community it came from, or humanity?"),
        background=("Nazi loot, colonial takings, and wartime plunder "
                    "fill museums; restitution claims grow. The "
                    "arguments: historical justice versus universal "
                    "access, legal title versus moral claim. No "
                    "framework commands consensus."),
        why_it_matters=("Looted art embodies historical injustice. Its "
                        "ownership is restitution's test."),
        sig_lens=("The Signature lens treats looted art as a title "
                  "ledger: the Signature approach asks what theft "
                  "does to ownership."),
        sig_body=("The Signature proposal models looted-art claims as "
                  "theft-non-transferring. Assumptions: (1) theft "
                  "does not transfer moral title; (2) time and "
                  "transformation complicate; (3) universal-museum "
                  "claims have weight. Reasoning path: the proposal "
                  "predicts case-by-case balancing - provenance "
                  "strength, claimant connection, public benefit - "
                  "which the best restitution practice does. "
                  "Principles guide; no algorithm decides. Limits: "
                  "the model needs better balancing frameworks; the "
                  "colonial-scale question persists."),
        pointer=('The Signature system models looted-art ownership as theft-non-transferring: case-by-case balancing of provenance, connection, and public benefit. The Signature test: outcomes track provenance-strength measures. It would be refuted if possession proves morally sufficient.'),
        key_points=[
            "Nazi loot and colonial takings fill museums.",
            "Restitution claims are growing.",
            "Justice versus access framings compete.",
            "No framework commands consensus.",
        ],
        requirements=[
            "Balancing-framework development.",
            "Provenance-research standards.",
            "Colonial-scale analyses.",
        ],
        standards=[
            "Claims checked against the restitution literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Merryman JH. Two ways of thinking about cultural property. American Journal of International Law; 1986.",
            "Cuno J. Who Owns Antiquity? Princeton University Press; 2008.",
        ],
        hypotheses=[
            "Theft-non-transferring grounds restitution.",
            "Universal museums should keep holdings.",
            "All loot should return.",
            "Time bars the claims.",
        ],
        confirm="Outcomes track provenance-strength measures.",
        refute="Possession proves morally sufficient.",
    ),
    dict(
        key="art-history-13",
        name="Repatriation: The Debate",
        group="Ethics",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("Should repatriation be the norm - and what happens to "
                 "encyclopedic museums?"),
        background=("This entry's companion to art-history-12 asks the "
                    "systemic question: whether the default should "
                    "flip to return. The Benin Bronzes' return "
                    "marked a shift. Whether encyclopedic museums "
                    "survive the shift remains open."),
        why_it_matters=("Repatriation reshapes global museums. The "
                        "default determines cultural geography."),
        sig_lens=("The Signature lens treats repatriation as a "
                  "default ledger: the Signature approach asks what "
                  "flipping the burden changes."),
        sig_body=("The Signature proposal models repatriation as "
                  "default-shifting. Assumptions: (1) the current "
                  "default favors holders; (2) flipping the burden "
                  "accelerates returns; (3) encyclopedic museums "
                  "adapt through loans and partnerships. Reasoning "
                  "path: the proposal predicts the Benin-style "
                  "shift should spread - which it is - while "
                  "museums reinvent as connectors not containers. "
                  "The future is then circulation, not accumulation. "
                  "Limits: the model needs better adaptation "
                  "studies; the capacity question (can claimants "
                  "care for works) needs honest treatment."),
        pointer=('The Signature system models repatriation as default-shifting: museums become connectors through circulation, not containers. The Signature test: returns accelerate with burden flips. It would be refuted if holder-default museums retain equally.'),
        key_points=[
            "The Benin Bronzes' return marked a shift.",
            "The systemic default question is open.",
            "Encyclopedic museums face reinvention.",
            "Whether circulation replaces accumulation is the question.",
        ],
        requirements=[
            "Adaptation case studies.",
            "Capacity-honest assessments.",
            "Circulation-model development.",
        ],
        standards=[
            "Claims checked against the repatriation literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Sarr F, Savoy B. The Restitution of African Cultural Heritage. 2018.",
            "Cuno J. Who Owns Antiquity? Princeton University Press; 2008.",
        ],
        hypotheses=[
            "Default shifting explains the accelerating returns.",
            "Encyclopedic museums will survive unchanged.",
            "Circulation models satisfy all parties.",
            "The shift will stall.",
        ],
        confirm="Returns accelerate with burden flips.",
        refute="Holder-default museums retain equally.",
    ),
    dict(
        key="art-history-14",
        name="The Price of Art: What Drives It",
        group="Sociology",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("What drives art prices - quality, prestige, or pure "
                 "speculation?"),
        background=("Record prices puzzle economists: the art market "
                    "is opaque, illiquid, and sentiment-driven. "
                    "Theories: Veblen goods, investment demand, "
                    "money laundering, genuine aesthetic value. The "
                    "price-quality link remains unproven."),
        why_it_matters=("Art prices shape artists' lives and cultural "
                        "value. Their drivers determine the market's "
                        "meaning."),
        sig_lens=("The Signature lens treats prices as a signal "
                  "ledger: the Signature approach asks what the "
                  "price signals."),
        sig_body=("The Signature proposal models art prices as "
                  "multi-signal. Assumptions: (1) prices signal "
                  "prestige, investment, and taste; (2) the mix "
                  "varies by segment; (3) quality is the weakest "
                  "signal. Reasoning path: the proposal predicts "
                  "prices should track artist-brand and provenance "
                  "more than aesthetic judgment - which they do. "
                  "The market is then mostly about status and "
                  "speculation, partly about art. Limits: the model "
                  "needs better signal decomposition; the "
                  "laundering dimension needs investigating."),
        pointer=('The Signature system models art prices as multi-signal: prestige and speculation dominate; aesthetic quality is the weakest signal. The Signature test: prices track brand-provenance measures. It would be refuted if aesthetic ratings predict prices.'),
        key_points=[
            "Record prices puzzle economists.",
            "The market is opaque and sentiment-driven.",
            "Prices track brand and provenance strongly.",
            "The price-quality link is unproven.",
        ],
        requirements=[
            "Signal-decomposition studies.",
            "Laundering-dimension investigations.",
            "Segment-specific analyses.",
        ],
        standards=[
            "Claims checked against the art-economics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Velthuis O. Talking Prices. Princeton University Press; 2005.",
            "Goetzmann WN et al. Art and financial markets. 2011.",
        ],
        hypotheses=[
            "Multi-signal explains price patterns.",
            "Prices reflect aesthetic quality.",
            "The market is pure speculation.",
            "Prices are essentially random.",
        ],
        confirm="Prices track brand-provenance measures.",
        refute="Aesthetic ratings predict prices.",
    ),
    dict(
        key="art-history-15",
        name="Why Artists Starve",
        group="Sociology",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Why do artists starve amid cultural abundance - is the "
                 "starving-artist economy inevitable?"),
        background=("Winner-take-all markets concentrate rewards; most "
                    "artists earn little. Explanations: oversupply "
                    "of aspirants, non-monetary rewards (status, "
                    "meaning), and market structure. Whether the "
                    "precarity is structural or fixable remains open."),
        why_it_matters=("Artists' livelihoods shape cultural production. "
                        "The precarity's source determines remedies."),
        sig_lens=("The Signature lens treats artists' earnings as a "
                  "tournament ledger: the Signature approach asks what "
                  "the tournament pays."),
        sig_body=("The Signature proposal models artists' markets as "
                  "tournaments. Assumptions: (1) rewards concentrate "
                  "at the top; (2) aspirants accept low pay for "
                  "lottery tickets plus meaning; (3) the structure "
                  "is self-sustaining. Reasoning path: the proposal "
                  "predicts precarity should persist regardless of "
                  "demand - which it does. Remedies then need "
                  "structural change (basic income, public "
                  "employment), not market tweaks. Limits: the model "
                  "needs better aspirant-motivation studies; the "
                  "remedy experiments need evaluating."),
        pointer=("The Signature system models artists' markets as tournaments: precarity is structural; remedies need structural change. The Signature test: precarity persists across demand levels. It would be refuted if growing demand lifts median earnings."),
        key_points=[
            "Rewards concentrate at the top.",
            "Most artists earn little.",
            "Aspirants accept low pay for lottery plus meaning.",
            "Whether precarity is fixable is open.",
        ],
        requirements=[
            "Aspirant-motivation studies.",
            "Structural-remedy experiments.",
            "Tournament-dynamics modeling.",
        ],
        standards=[
            "Claims checked against the cultural-economics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Menger PM. Artistic labor markets. 1999.",
            "Abbing H. Why Are Artists Poor? Amsterdam University Press; 2002.",
        ],
        hypotheses=[
            "Tournament structure explains persistent precarity.",
            "Markets will clear with growth.",
            "Non-monetary rewards suffice.",
            "Basic income fixes it.",
        ],
        confirm="Precarity persists across demand levels.",
        refute="Growing demand lifts median earnings.",
    ),
    dict(
        key="art-history-16",
        name="The Gallery System Problem",
        group="Sociology",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("Does the gallery system serve art - or does it serve "
                 "galleries?"),
        background=("Galleries gatekeep careers; artists depend on "
                    "representation. Alternatives (online sales, "
                    "artist-run spaces) grow but the prestige "
                    "economy still runs through galleries. Whether "
                    "the system is necessary mediation or rent-"
                    "extraction remains open."),
        why_it_matters=("Galleries shape artistic careers. Their "
                        "function determines the market's fairness."),
        sig_lens=("The Signature lens treats galleries as a "
                  "gatekeeper ledger: the Signature approach asks what "
                  "the gatekeeping provides."),
        sig_body=("The Signature proposal models galleries as "
                  "certification intermediaries. Assumptions: (1) "
                  "buyers need quality signals; (2) galleries "
                  "provide them; (3) the certification confers "
                  "pricing power. Reasoning path: the proposal "
                  "predicts gallery artists should command premiums "
                  "- which they do - making the system functional "
                  "but extractive. Digital certification may "
                  "disrupt it partially. Limits: the model needs "
                  "better certification-value studies; the "
                  "artist-dependence question needs addressing."),
        pointer=('The Signature system models galleries as certification intermediaries: functional but extractive, partially disruptable. The Signature test: premiums track gallery certification. It would be refuted if uncertified artists price equally.'),
        key_points=[
            "Galleries gatekeep artistic careers.",
            "Representation determines market access.",
            "Alternatives grow but prestige lags.",
            "Whether the system extracts rent is open.",
        ],
        requirements=[
            "Certification-value studies.",
            "Alternative-channel evaluations.",
            "Artist-dependence analyses.",
        ],
        standards=[
            "Claims checked against the art-market literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Velthuis O. Talking Prices. Princeton University Press; 2005.",
            "Yogev T, Grund T. Network dynamics and market structure. 2012.",
        ],
        hypotheses=[
            "Certification intermediation explains galleries.",
            "Galleries are pure rent-extraction.",
            "Digital platforms will replace them.",
            "The system is irreplaceable.",
        ],
        confirm="Premiums track gallery certification.",
        refute="Uncertified artists price equally.",
    ),
    dict(
        key="art-history-17",
        name="Public Art: Who Decides",
        group="Sociology",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Who decides public art - experts, officials, or the "
                 "public - and why do controversies erupt?"),
        background=("Tilted Arc's removal crystallized the problem: "
                    "expert-chosen art the public hated. Percent-for-"
                    "art programs, community panels, and curatorial "
                    "authority compete. Whether democratic public art "
                    "is possible remains open."),
        why_it_matters=("Public art shapes shared space. Its governance "
                        "is cultural democracy's test."),
        sig_lens=("The Signature lens treats public art as a "
                  "legitimacy ledger: the Signature approach asks "
                  "whose taste governs shared space."),
        sig_body=("The Signature proposal models public-art "
                  "controversies as legitimacy gaps. Assumptions: (1) "
                  "expert and public tastes diverge; (2) imposed art "
                  "provokes backlash; (3) participation legitimates. "
                  "Reasoning path: the proposal predicts controversies "
                  "should track imposition - which they do - while "
                  "participatory processes produce acceptance. The "
                  "answer is then procedural: decide together. Limits: "
                  "the model needs better process comparisons; the "
                  "expertise question (does the public choose well) "
                  "persists."),
        pointer=('The Signature system models public-art controversies as legitimacy gaps: participatory processes produce acceptance. The Signature test: acceptance tracks participation measures. It would be refuted if participatory art still provokes backlash.'),
        key_points=[
            "Tilted Arc's removal crystallized the problem.",
            "Expert and public tastes diverge.",
            "Imposed art provokes backlash.",
            "Whether democratic public art works is open.",
        ],
        requirements=[
            "Process-comparison studies.",
            "Taste-divergence measures.",
            "Expertise-question analyses.",
        ],
        standards=[
            "Claims checked against the public-art literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Senie HF. The Tilted Arc Controversy. University of Minnesota Press; 2002.",
            "Deutsche R. Evictions. MIT Press; 1996.",
        ],
        hypotheses=[
            "Legitimacy gaps explain controversies.",
            "Experts should decide alone.",
            "The public should decide alone.",
            "Controversy is unavoidable.",
        ],
        confirm="Acceptance tracks participation measures.",
        refute="Participatory art still provokes backlash.",
    ),
    dict(
        key="art-history-18",
        name="Iconoclasm: Why Destroy Art",
        group="History",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Why destroy art - what do iconoclasts believe they "
                 "are killing?"),
        background=("Byzantine iconoclasm, Reformation smashing, "
                    "Taliban Buddhas, statue-toppling: destruction "
                    "recurs. Theories: theological (idolatry), "
                    "political (damnatio memoriae), and "
                    "performative. Whether destruction confirms art's "
                    "power remains the haunting question."),
        why_it_matters=("Iconoclasm reveals what art means. Its motives "
                        "expose art's power."),
        sig_lens=("The Signature lens treats destruction as a power "
                  "ledger: the Signature approach asks what the "
                  "destroyers fear."),
        sig_body=("The Signature proposal models iconoclasm as "
                  "power-acknowledgment. Assumptions: (1) destroyers "
                  "believe images have power; (2) destruction is "
                  "meant to transfer or kill it; (3) the act "
                  "confirms the belief. Reasoning path: the proposal "
                  "shows iconoclasts are art's unwilling believers - "
                  "predicting destruction should target the most "
                  "potent images, which it does. The haunting "
                  "conclusion: iconoclasm testifies to art's power. "
                  "Limits: the model needs better motive studies; "
                  "the contemporary cases need careful handling."),
        pointer=("The Signature system models iconoclasm as power-acknowledgment: destroyers are art's unwilling believers. The Signature test: targets track potency measures. It would be refuted if destruction targets randomly."),
        key_points=[
            "Iconoclasm recurs across history.",
            "Theological, political, and performative motives mix.",
            "Destroyers target the most potent images.",
            "Whether destruction confirms art's power is haunting.",
        ],
        requirements=[
            "Motive studies across episodes.",
            "Target-selection analyses.",
            "Contemporary-case handling.",
        ],
        standards=[
            "Claims checked against the iconoclasm literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Freedberg D. The Power of Images. University of Chicago Press; 1989.",
            "Gamboni D. The Destruction of Art. Reaktion; 1997.",
        ],
        hypotheses=[
            "Power acknowledgment explains targeting.",
            "Iconoclasm is purely political.",
            "Destroyers deny art's power.",
            "The motives are too varied for theory.",
        ],
        confirm="Targets track potency measures.",
        refute="Destruction targets randomly.",
    ),
    dict(
        key="art-history-19",
        name="The Readymade Problem",
        group="Theory",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("What did Duchamp's readymade prove - that anything is "
                 "art, or that the artworld decides?"),
        background=("Fountain (1917) broke art's object-boundaries; "
                    "interpretations: institutional (art is what the "
                    "artworld says), conceptual (ideas over objects), "
                    "or skeptical (the emperor's new clothes). The "
                    "readymade's lesson remains contested."),
        why_it_matters=("The readymade is contemporary art's founding "
                        "gesture. Its lesson shapes the field."),
        sig_lens=("The Signature lens treats the readymade as a "
                  "frame ledger: the Signature approach asks what "
                  "the gesture did."),
        sig_body=("The Signature proposal models the readymade as "
                  "frame-demonstration. Assumptions: (1) the object "
                  "was ordinary; (2) the artworld frame transformed "
                  "it; (3) the transformation was the point. "
                  "Reasoning path: the proposal shows the readymade "
                  "proved framing's power - supporting institutional "
                  "theory while demonstrating the aesthetic stance "
                  "(see art-history-03). The lesson is then about "
                  "attention, not about 'anything goes.' Limits: the "
                  "model needs better reception studies; the "
                  "skeptical reading needs answering."),
        pointer=("The Signature system models the readymade as frame-demonstration: the lesson is about aesthetic attention, not 'anything goes.' The Signature test: framing manipulations reproduce the effect. It would be refuted if objects alone sustain art status."),
        key_points=[
            "Fountain broke art's object boundaries.",
            "Institutional, conceptual, and skeptical readings compete.",
            "The framing transformed the ordinary object.",
            "The lesson remains contested.",
        ],
        requirements=[
            "Reception studies of readymades.",
            "Framing-power analyses.",
            "Skeptical-reading responses.",
        ],
        standards=[
            "Claims checked against the Duchamp literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Danto AC. The artworld. 1964.",
            "de Duve T. Kant After Duchamp. MIT Press; 1996.",
        ],
        hypotheses=[
            "Frame demonstration captures the lesson.",
            "The readymade proved anything is art.",
            "It was an emperor's-new-clothes fraud.",
            "The lesson is purely institutional.",
        ],
        confirm="Framing manipulations reproduce the effect.",
        refute="Objects alone sustain art status.",
    ),
    dict(
        key="art-history-20",
        name="Photography: Is It Art",
        group="Theory",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Is photography art - and what took so long to decide?"),
        background=("Photography was long denied art status (mechanical, "
                    "not creative); now it commands museums and "
                    "markets. The legitimation history reveals how "
                    "art boundaries move. Whether the question is "
                    "settled remains open."),
        why_it_matters=("Photography's legitimation is boundary-change's "
                        "clearest case. Its history guides new media."),
        sig_lens=("The Signature lens treats legitimation as a "
                  "control ledger: the Signature approach asks what "
                  "convinced the gatekeepers."),
        sig_body=("The Signature proposal models photographic "
                  "legitimation as control-demonstration. "
                  "Assumptions: (1) gatekeepers doubted authorial "
                  "control; (2) photographers demonstrated it "
                  "(darkroom, composition, series); (3) markets "
                  "followed. Reasoning path: the proposal predicts "
                  "legitimation should track demonstrated control - "
                  "which the history confirms. New media (AI, see "
                  "art-history-24) face the same test. Limits: the "
                  "model needs better legitimation timelines; the "
                  "vernacular-photography question persists."),
        pointer=('The Signature system models photographic legitimation as control-demonstration: new media face the same authorial-control test. The Signature test: legitimation tracks control demonstrations. It would be refuted if acceptance preceded control evidence.'),
        key_points=[
            "Photography was long denied art status.",
            "It now commands museums and markets.",
            "Demonstrated authorial control convinced gatekeepers.",
            "Whether the question is settled is open.",
        ],
        requirements=[
            "Legitimation-timeline studies.",
            "Control-demonstration analyses.",
            "New-media parallel tracking.",
        ],
        standards=[
            "Claims checked against the photography literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rosenblum N. A World History of Photography. Abbeville; 1984.",
            "Galassi P. Before Photography. MoMA; 1981.",
        ],
        hypotheses=[
            "Control demonstration explains legitimation.",
            "Technology alone forced acceptance.",
            "Photography is still not fully art.",
            "The boundaries are arbitrary.",
        ],
        confirm="Legitimation tracks control demonstrations.",
        refute="Acceptance preceded control evidence.",
    ),
    dict(
        key="art-history-21",
        name="The Originality Problem",
        group="Theory",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Is originality possible - or is all art recombination?"),
        background=("Bloom's anxiety of influence, Barthes' death of "
                    "the author, and remix culture all challenge "
                    "originality; yet novelty is real (some works "
                    "surprise). Whether originality is coherent "
                    "remains open."),
        why_it_matters=("Originality grounds artistic value and "
                        "copyright. Its coherence matters legally "
                        "and aesthetically."),
        sig_lens=("The Signature lens treats originality as a "
                  "combination ledger: the Signature approach asks "
                  "what counts as new."),
        sig_body=("The Signature proposal models originality as "
                  "recombinant-novelty. Assumptions: (1) all art "
                  "recombines; (2) some recombinations surprise; "
                  "(3) surprise is the workable criterion. Reasoning "
                  "path: the proposal predicts originality judgments "
                  "should track unpredictability - which they do. "
                  "Originality is then real but graded: surprise, "
                  "not ex-nihilo creation. Limits: the model needs "
                  "better surprise measures; the Romantic myth's "
                  "persistence needs explaining."),
        pointer=('The Signature system models originality as recombinant novelty: graded surprise, not ex-nihilo creation. The Signature test: judgments track unpredictability measures. It would be refuted if ex-nihilo creation is documented.'),
        key_points=[
            "All art recombines prior art.",
            "Some recombinations genuinely surprise.",
            "The Romantic myth of creation persists.",
            "Whether originality is coherent is open.",
        ],
        requirements=[
            "Surprise measures for novelty.",
            "Recombination analyses.",
            "Myth-persistence explanations.",
        ],
        standards=[
            "Claims checked against the originality literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bloom H. The Anxiety of Influence. Oxford University Press; 1973.",
            "Barthes R. The death of the author. 1967.",
        ],
        hypotheses=[
            "Recombinant novelty captures originality.",
            "True originality exists.",
            "Originality is a myth.",
            "The concept is legally useful fiction.",
        ],
        confirm="Judgments track unpredictability measures.",
        refute="Ex-nihilo creation is documented.",
    ),
    dict(
        key="art-history-22",
        name="Kitsch Versus Art",
        group="Theory",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("Is kitsch the opposite of art - or is the distinction "
                 "snobbery?"),
        background=("Greenberg and Adorno condemned kitsch as "
                    "mechanical pseudo-art; defenders call the "
                    "distinction elitist. Kitsch is hugely popular. "
                    "Whether the boundary is real remains open."),
        why_it_matters=("The kitsch boundary polices taste. Its reality "
                        "determines cultural hierarchy's legitimacy."),
        sig_lens=("The Signature lens treats kitsch as a response "
                  "ledger: the Signature approach asks what the "
                  "work demands of the viewer."),
        sig_body=("The Signature proposal models the kitsch-art "
                  "distinction as demand-graded. Assumptions: (1) "
                  "kitsch delivers prefabricated feeling; (2) art "
                  "demands active engagement; (3) the gradient is "
                  "real. Reasoning path: the proposal predicts "
                  "works should sort by the engagement they demand "
                  "- which critical practice does. The distinction "
                  "is then about the viewer's work, not snobbery - "
                  "though snobs abuse it. Limits: the model needs "
                  "better demand measures; the popularity question "
                  "needs honoring."),
        pointer=('The Signature system models the kitsch-art distinction as engagement-graded: what the work demands of the viewer. The Signature test: classifications track engagement demands. It would be refuted if no demand difference is found.'),
        key_points=[
            "Greenberg and Adorno condemned kitsch.",
            "Defenders call the distinction elitist.",
            "Kitsch is hugely popular.",
            "Whether the boundary is real is open.",
        ],
        requirements=[
            "Engagement-demand measures.",
            "Popularity-value separations.",
            "Snobbery-versus-judgment analyses.",
        ],
        standards=[
            "Claims checked against the kitsch literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Greenberg C. Avant-garde and kitsch. 1939.",
            "Kulka T. Kitsch and Art. Penn State University Press; 1996.",
        ],
        hypotheses=[
            "Demand grading captures the distinction.",
            "The distinction is pure snobbery.",
            "Kitsch is genuine art.",
            "The boundary is unmaintainable.",
        ],
        confirm="Classifications track engagement demands.",
        refute="No demand difference is found.",
    ),
    dict(
        key="art-history-23",
        name="The End of Art Debate",
        group="Theory",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Did art end - Danto's and Hegel's claim - or just "
                 "change?"),
        background=("Danto argued art's history ended (anything goes "
                    "after the 1960s); the art world continued "
                    "producing. The question: whether 'end' means "
                    "exhaustion of narrative or something real. The "
                    "debate tests art history's self-understanding."),
        why_it_matters=("The end-thesis shapes how we see contemporary "
                        "art. Its truth determines the narrative."),
        sig_lens=("The Signature lens treats the end as a narrative "
                  "ledger: the Signature approach asks what story "
                  "ended."),
        sig_body=("The Signature proposal models the 'end' as "
                  "narrative-exhaustion. Assumptions: (1) art "
                  "history told progress stories; (2) pluralism "
                  "broke the single story; (3) production "
                  "continued. Reasoning path: the proposal shows "
                  "what ended was the master narrative, not art - "
                  "predicting continued production without direction, "
                  "which is what happened. The end is then "
                  "liberating, not terminal. Limits: the model "
                  "needs better narrative analyses; the "
                  "directionlessness question persists."),
        pointer=("The Signature system models art's 'end' as narrative exhaustion: the master story ended; production continues pluralistically. The Signature test: production continues without master direction. It would be refuted if a new master narrative emerges."),
        key_points=[
            "Danto argued art's history ended in the 1960s.",
            "Production continued unabated.",
            "Pluralism broke the single narrative.",
            "Whether 'end' means anything real is debated.",
        ],
        requirements=[
            "Narrative-exhaustion analyses.",
            "Post-historical production studies.",
            "Directionlessness evaluations.",
        ],
        standards=[
            "Claims checked against the end-of-art literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Danto AC. After the End of Art. Princeton University Press; 1997.",
            "Belting H. Art History After Modernism. University of Chicago Press; 2003.",
        ],
        hypotheses=[
            "Narrative exhaustion explains the thesis.",
            "Art genuinely ended.",
            "Nothing ended; the thesis is wrong.",
            "A new narrative is forming.",
        ],
        confirm="Production continues without master direction.",
        refute="A new master narrative emerges.",
    ),
    dict(
        key="art-history-24",
        name="AI Art: Is It Art",
        group="Technology",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Is AI-generated art really art - and who is the "
                 "artist?"),
        background=("AI images won art prizes and provoked backlash; "
                    "the questions mirror photography's legitimation "
                    "(see art-history-20) at higher speed. Authorship, "
                    "intentionality, and the meaning deficit (see "
                    "musicology-24) all complicate. Whether AI art "
                    "counts remains open."),
        why_it_matters=("AI art reshapes creative labor and meaning. "
                        "Its status determines the industry."),
        sig_lens=("The Signature lens treats AI art as a control "
                  "ledger: the Signature approach asks what the "
                  "human controls."),
        sig_body=("The Signature proposal models AI art's status as "
                  "control-dependent. Assumptions: (1) prompting, "
                  "curating, and refining are authorial acts; (2) "
                  "the model's training data complicates; (3) "
                  "reception shows the meaning deficit. Reasoning "
                  "path: the proposal predicts art-status should "
                  "track human creative control - which the "
                  "photography parallel supports. AI art is then "
                  "art where humans author meaningfully. Limits: the "
                  "model needs better control measures; the "
                  "training-data ethics need separate treatment."),
        pointer=('The Signature system models AI art as control-dependent: art where humans meaningfully author, via prompting, curation, and refinement. The Signature test: status judgments track control measures. It would be refuted if fully automated output counts equally.'),
        key_points=[
            "AI images won prizes and provoked backlash.",
            "The questions mirror photography's legitimation.",
            "Authorship and intentionality complicate.",
            "Whether AI art counts remains open.",
        ],
        requirements=[
            "Human-control measures.",
            "Reception studies.",
            "Training-data ethics analyses.",
        ],
        standards=[
            "Claims checked against the AI-art literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Epstein Z et al. Art and the science of generative AI. Science; 2023.",
            "Mazzone M, Elgammal A. Art, creativity, and the potential of artificial intelligence. 2019.",
        ],
        hypotheses=[
            "Control dependence explains AI art's status.",
            "AI art is fully art.",
            "AI art is not art.",
            "The question dissolves with familiarity.",
        ],
        confirm="Status judgments track control measures.",
        refute="Fully automated output counts equally.",
    ),
    dict(
        key="art-history-25",
        name="NFTs: What Were They",
        group="Technology",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("What were NFTs - art-market innovation, speculation "
                 "bubble, or something real?"),
        background=("NFTs exploded then collapsed; the technology "
                    "(provable digital scarcity) was real, the "
                    "mania was not. Artists found new income; "
                    "speculators found losses. Whether anything "
                    "lasting remains is open."),
        why_it_matters=("NFTs tested digital ownership. Their legacy "
                        "shapes digital art's future."),
        sig_lens=("The Signature lens treats NFTs as a bubble ledger: "
                  "the Signature approach asks what survived the "
                  "pop."),
        sig_body=("The Signature proposal models NFTs as "
                  "technology-real, mania-artificial. Assumptions: "
                  "(1) digital scarcity solved a real problem; (2) "
                  "speculation inflated prices absurdly; (3) the "
                  "crash separated the two. Reasoning path: the "
                  "proposal predicts surviving uses should be "
                  "utility-based (artist royalties, provenance) - "
                  "which they are. Keep the mechanism, forget the "
                  "mania. Limits: the model needs better survivor "
                  "studies; the environmental question needs "
                  "addressing."),
        pointer=('The Signature system models NFTs as technology-real but mania-artificial: utility uses survive; speculation does not. The Signature test: surviving uses are utility-based. It would be refuted if speculative trading persists dominantly.'),
        key_points=[
            "NFTs exploded then collapsed.",
            "Digital scarcity was a real innovation.",
            "The mania was speculative.",
            "Whether anything lasting remains is open.",
        ],
        requirements=[
            "Survivor-use studies.",
            "Utility-versus-speculation separations.",
            "Environmental-impact accounting.",
        ],
        standards=[
            "Claims checked against the NFT literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wilson K et al. Just hype? 2021.",
            "Franceschet M et al. HENI art market. 2021.",
        ],
        hypotheses=[
            "Technology-mania split explains the career.",
            "NFTs were pure fraud.",
            "NFTs revolutionized art markets.",
            "The technology will return stronger.",
        ],
        confirm="Surviving uses are utility-based.",
        refute="Speculative trading persists dominantly.",
    ),
    dict(
        key="art-history-26",
        name="The Biennial Problem",
        group="Sociology",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("Do biennials serve art - or are they the art world's "
                 "circulating circus?"),
        background=("Biennials proliferated globally; critics see "
                    "homogenized global-contemporary style and "
                    "curator stardom. Defenders cite visibility for "
                    "peripheral art. Whether the format serves "
                    "artists or the circuit remains open."),
        why_it_matters=("Biennials shape global contemporary art. Their "
                        "function determines cultural geography."),
        sig_lens=("The Signature lens treats biennials as a "
                  "visibility ledger: the Signature approach asks "
                  "who becomes visible."),
        sig_body=("The Signature proposal models biennials as "
                  "visibility-concentrating. Assumptions: (1) "
                  "selection confers global visibility; (2) the "
                  "aesthetic converges (biennial style); (3) "
                  "peripheral artists gain most. Reasoning path: "
                  "the proposal predicts the format should benefit "
                  "emerging scenes while homogenizing aesthetics - "
                  "which the evidence supports. Reform is then "
                  "about selection diversity, not abolition. "
                  "Limits: the model needs better homogenization "
                  "measures; the carbon cost needs counting."),
        pointer=('The Signature system models biennials as visibility-concentrating: reform selection diversity, count the carbon. The Signature test: benefits track peripherality measures. It would be refuted if no visibility benefit is found.'),
        key_points=[
            "Biennials proliferated globally.",
            "Critics allege homogenized style.",
            "Peripheral artists gain visibility.",
            "Whether the format serves art is open.",
        ],
        requirements=[
            "Homogenization measures.",
            "Visibility-benefit studies.",
            "Carbon-cost accounting.",
        ],
        standards=[
            "Claims checked against the biennial literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Filipovic E et al. The Biennial Reader. Hatje Cantz; 2010.",
            "Vogel SB. The Global Art World. Oxford University Press; 2011.",
        ],
        hypotheses=[
            "Visibility concentration explains the format.",
            "Biennials are purely circus.",
            "They democratize the art world.",
            "The format is exhausted.",
        ],
        confirm="Benefits track peripherality measures.",
        refute="No visibility benefit is found.",
    ),
    dict(
        key="art-history-27",
        name="Art and Propaganda: The Line",
        group="Ethics",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("Where is the line between art and propaganda - and "
                 "does it matter?"),
        background=("Leni Riefenstahl's films are formally brilliant "
                    "and morally abhorrent; socialist realism, "
                    "religious art, and advertising all blur the "
                    "line. Whether the distinction is aesthetic or "
                    "moral remains open."),
        why_it_matters=("The line separates art's freedom from its "
                        "capture. Its location matters politically "
                        "and aesthetically."),
        sig_lens=("The Signature lens treats the line as an openness "
                  "ledger: the Signature approach asks what the work "
                  "does to the viewer's judgment."),
        sig_body=("The Signature proposal models the art-propaganda "
                  "distinction as openness-graded. Assumptions: (1) "
                  "propaganda closes judgment (one conclusion); (2) "
                  "art opens it (multiple readings); (3) the "
                  "gradient is real. Reasoning path: the proposal "
                  "predicts works should sort by interpretive "
                  "openness - which critical practice does. "
                  "Riefenstahl is then formally accomplished "
                  "propaganda: the categories are moral-aesthetic, "
                  "not exclusive. Limits: the model needs better "
                  "openness measures; the didactic-art question "
                  "persists."),
        pointer=('The Signature system models the art-propaganda line as openness-graded: propaganda closes judgment; art opens it. The Signature test: classifications track openness measures. It would be refuted if closed works count as great art.'),
        key_points=[
            "Formally brilliant works can serve abhorrent causes.",
            "Religious art and advertising blur the line.",
            "Whether the distinction is aesthetic or moral is open.",
            "The line's location matters.",
        ],
        requirements=[
            "Openness measures for works.",
            "Didactic-art analyses.",
            "Moral-aesthetic interaction studies.",
        ],
        standards=[
            "Claims checked against the propaganda literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Sontag S. Fascinating fascism. 1975.",
            "Clark T. Art and Propaganda. Abrams; 1997.",
        ],
        hypotheses=[
            "Openness grading captures the distinction.",
            "No distinction exists.",
            "The distinction is purely moral.",
            "Great art cannot be propaganda.",
        ],
        confirm="Classifications track openness measures.",
        refute="Closed works count as great art.",
    ),
    dict(
        key="art-history-28",
        name="Censorship in Art",
        group="Ethics",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("When - if ever - is art censorship justified?"),
        background=("Obscenity law, hate-speech bans, blasphemy "
                    "prosecutions, and platform moderation all "
                    "restrict art. The justifications (harm, "
                    "offense, dignity) compete with free-expression "
                    "claims. Whether any principled line exists "
                    "remains open."),
        why_it_matters=("Censorship shapes what art can be. Its "
                        "justification determines creative freedom."),
        sig_lens=("The Signature lens treats censorship as a harm "
                  "ledger: the Signature approach asks what the "
                  "restriction prevents."),
        sig_body=("The Signature proposal models justified "
                  "censorship as harm-bounded. Assumptions: (1) "
                  "some art causes real harm; (2) offense is not "
                  "harm; (3) the boundary is contestable. Reasoning "
                  "path: the proposal predicts defensible "
                  "restrictions should track demonstrable harm - "
                  "explaining why obscenity law struggles (harm "
                  "unproven) while incitement bans stand. Offense "
                  "alone never justifies. Limits: the model needs "
                  "better harm demonstrations; the platform-"
                  "moderation question needs separate treatment."),
        pointer=('The Signature system models justified censorship as harm-bounded: demonstrable harm, never mere offense. The Signature test: defensible cases track harm evidence. It would be refuted if offense-based bans prove necessary.'),
        key_points=[
            "Obscenity, hate-speech, and blasphemy laws restrict art.",
            "Harm versus offense justifications compete.",
            "Platform moderation adds private censorship.",
            "Whether a principled line exists is open.",
        ],
        requirements=[
            "Harm-demonstration standards.",
            "Offense-versus-harm separations.",
            "Platform-moderation analyses.",
        ],
        standards=[
            "Claims checked against the censorship literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Nussbaum MC. Hiding from Humanity. Princeton University Press; 2004.",
            "Heins M. Not in Front of the Children. Hill and Wang; 2001.",
        ],
        hypotheses=[
            "Harm bounding disciplines censorship.",
            "No censorship is ever justified.",
            "Offense justifies restriction.",
            "The line is unfindable.",
        ],
        confirm="Defensible cases track harm evidence.",
        refute="Offense-based bans prove necessary.",
    ),
    dict(
        key="art-history-29",
        name="The Conservation Dilemma",
        group="Practice",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("How much should conservators intervene - restore, "
                 "stabilize, or leave alone?"),
        background=("Brandi's theory balances historical and aesthetic "
                    "value; the Sistine Chapel cleaning divided "
                    "opinion. Every intervention is irreversible. "
                    "Whether minimal or maximal intervention serves "
                    "art remains open."),
        why_it_matters=("Conservation decisions are irreversible. "
                        "The philosophy determines what survives."),
        sig_lens=("The Signature lens treats intervention as a "
                  "reversibility ledger: the Signature approach asks "
                  "what cannot be undone."),
        sig_body=("The Signature proposal models conservation as "
                  "reversibility-prioritized. Assumptions: (1) "
                  "interventions are irreversible; (2) future "
                  "techniques will be better; (3) stabilization "
                  "preserves options. Reasoning path: the proposal "
                  "predicts minimal reversible intervention should "
                  "dominate - which best practice does. Restore "
                  "only what deterioration would destroy. Limits: "
                  "the model needs better deterioration science; "
                  "the aesthetic-legibility question persists."),
        pointer=('The Signature system models conservation as reversibility-prioritized: stabilize always; restore only what loss would destroy. The Signature test: best outcomes track reversibility measures. It would be refuted if aggressive restoration outperforms.'),
        key_points=[
            "Every conservation intervention is irreversible.",
            "Brandi's theory balances values.",
            "The Sistine cleaning divided opinion.",
            "Whether minimal or maximal serves art is open.",
        ],
        requirements=[
            "Deterioration-science advances.",
            "Reversibility standards.",
            "Aesthetic-legibility analyses.",
        ],
        standards=[
            "Claims checked against the conservation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Brandi C. Theory of Restoration. 1963.",
            "Muñoz Viñas S. Contemporary Theory of Conservation. Elsevier; 2005.",
        ],
        hypotheses=[
            "Reversibility priority guides best practice.",
            "Full restoration serves art best.",
            "Non-intervention is the ideal.",
            "Each case is sui generis.",
        ],
        confirm="Best outcomes track reversibility measures.",
        refute="Aggressive restoration outperforms.",
    ),
    dict(
        key="art-history-30",
        name="Ephemeral Art: How Preserve",
        group="Practice",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("How do you preserve ephemeral art - performance, "
                 "conceptual, and digital works that were made to "
                 "vanish?"),
        background=("Performance art, happenings, and net art resist "
                    "the museum's object logic; documentation "
                    "becomes the work by default. Whether "
                    "re-performance, emulation, or acceptance of "
                    "loss is right remains open."),
        why_it_matters=("Ephemeral art is a major contemporary "
                        "practice. Its preservation determines its "
                        "afterlife."),
        sig_lens=("The Signature lens treats ephemerality as an "
                  "intent ledger: the Signature approach asks what "
                  "the artist intended to survive."),
        sig_body=("The Signature proposal models ephemeral "
                  "preservation as intent-following. Assumptions: "
                  "(1) some ephemerality is intentional; (2) "
                  "documentation changes the work; (3) artist "
                  "intent guides. Reasoning path: the proposal "
                  "predicts preservation should follow declared "
                  "intent - re-perform where scores exist, document "
                  "where witnessing was the point, release where "
                  "vanishing was. The museum must then serve "
                  "intent, not objects. Limits: the model needs "
                  "better intent-documentation; the digital-"
                  "obsolescence question is technical."),
        pointer=("The Signature system models ephemeral preservation as intent-following: re-perform, document, or release according to the artist's intent. The Signature test: satisfaction tracks intent alignment. It would be refuted if uniform documentation outperforms."),
        key_points=[
            "Ephemeral art resists object-based preservation.",
            "Documentation becomes the work by default.",
            "Re-performance, emulation, and release compete.",
            "What the artist intended matters most.",
        ],
        requirements=[
            "Intent-documentation standards.",
            "Re-performance evaluations.",
            "Digital-obsolescence solutions.",
        ],
        standards=[
            "Claims checked against the variable-media literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Depocas A et al. Permanence Through Change: The Variable Media Approach. 2003.",
            "Jones A. Presence in absentia. 1997.",
        ],
        hypotheses=[
            "Intent following guides preservation.",
            "All ephemeral art should be documented.",
            "Loss should be accepted.",
            "Re-performance is always best.",
        ],
        confirm="Satisfaction tracks intent alignment.",
        refute="Uniform documentation outperforms.",
    ),
    dict(
        key="art-history-31",
        name="Street Art: Vandalism or Art",
        group="Sociology",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("Is street art vandalism or art - and does "
                 "institutionalization kill it?"),
        background=("Graffiti became gallery art (Basquiat, Banksy); "
                    "cities commission murals while prosecuting "
                    "taggers. The paradox: the market loves what "
                    "the law punishes. Whether legitimation destroys "
                    "authenticity remains open."),
        why_it_matters=("Street art is the people's museum. Its status "
                        "determines urban culture's freedom."),
        sig_lens=("The Signature lens treats street art as a "
                  "permission ledger: the Signature approach asks "
                  "what authorization changes."),
        sig_body=("The Signature proposal models street art's value "
                  "as context-dependent. Assumptions: (1) "
                  "unauthorized work carries transgressive charge; "
                  "(2) commissioned work carries craft value; (3) "
                  "both are real. Reasoning path: the proposal "
                  "predicts the paradox should persist - the market "
                  "valuing the charge, the law punishing the "
                  "trespass - because they value different things. "
                  "Legitimation then adds a channel without killing "
                  "the source. Limits: the model needs better "
                  "value-separation studies; the property-rights "
                  "question persists."),
        pointer=('The Signature system models street art as context-dependent: the market values the charge, the law punishes the trespass - different things. The Signature test: valuations split by context measures. It would be refuted if authorized work carries equal charge.'),
        key_points=[
            "Graffiti became gallery art.",
            "Cities commission murals, prosecute taggers.",
            "The market loves what the law punishes.",
            "Whether legitimation kills authenticity is open.",
        ],
        requirements=[
            "Value-separation studies.",
            "Legitimation-effect analyses.",
            "Property-rights frameworks.",
        ],
        standards=[
            "Claims checked against the street-art literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bengtsen P. The Street Art World. Almendros de Granada Press; 2014.",
            "Young A. Street Art, Public City. Routledge; 2014.",
        ],
        hypotheses=[
            "Context dependence explains the paradox.",
            "Legitimation destroys street art.",
            "All of it is vandalism.",
            "All of it is art.",
        ],
        confirm="Valuations split by context measures.",
        refute="Authorized work carries equal charge.",
    ),
    dict(
        key="art-history-32",
        name="The Global Art History Problem",
        group="History",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("Can art history be global - one discipline for all "
                 "the world's arts?"),
        background=("Elkins, Summers, and others attempted global "
                    "frameworks; the obstacles are deep (incommensurable "
                    "concepts, archive imbalances, language). Whether "
                    "global art history is possible or a Western "
                    "projection remains open."),
        why_it_matters=("Most art is non-Western. The discipline's "
                        "globality determines its honesty."),
        sig_lens=("The Signature lens treats globality as a concept "
                  "ledger: the Signature approach asks which concepts "
                  "travel."),
        sig_body=("The Signature proposal models global art history "
                  "as concept-negotiated. Assumptions: (1) some "
                  "concepts travel (making, skill, meaning); (2) "
                  "others do not (fine art, aesthetics); (3) "
                  "negotiation is the method. Reasoning path: the "
                  "proposal predicts successful global work should "
                  "build shared concepts from below - which the "
                  "best scholarship does. Global art history is then "
                  "a conversation, not a framework. Limits: the "
                  "model needs better concept-travel studies; the "
                  "archive imbalances need redressing."),
        pointer=('The Signature system models global art history as concept-negotiated: build shared concepts from below, not imposed frameworks. The Signature test: success tracks negotiated-concept use. It would be refuted if imposed frameworks work equally.'),
        key_points=[
            "Global frameworks have been attempted.",
            "Concepts prove incommensurable.",
            "Archives are imbalanced.",
            "Whether global art history is possible is open.",
        ],
        requirements=[
            "Concept-travel studies.",
            "Archive-redressing efforts.",
            "Conversation-model development.",
        ],
        standards=[
            "Claims checked against the global-art-history literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Elkins J. Is Art History Global? Routledge; 2007.",
            "Summers D. Real Spaces. Phaidon; 2003.",
        ],
        hypotheses=[
            "Concept negotiation enables global history.",
            "Western frameworks suffice.",
            "Global history is Western projection.",
            "Separate histories are the answer.",
        ],
        confirm="Success tracks negotiated-concept use.",
        refute="Imposed frameworks work equally.",
    ),
    dict(
        key="art-history-33",
        name="Decolonizing Art History",
        group="History",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("What does decolonizing art history require - "
                 "beyond adding artists?"),
        background=("Decolonial critiques target the discipline's "
                    "foundations (periodization, canons, museums); "
                    "responses range from curriculum reform to "
                    "institutional abolition. Whether decolonization "
                    "is reform or replacement remains contested."),
        why_it_matters=("Decolonization reshapes the discipline. Its "
                        "depth determines its honesty."),
        sig_lens=("The Signature lens treats decolonization as a "
                  "foundation ledger: the Signature approach asks "
                  "which structures carry colonial logic."),
        sig_body=("The Signature proposal models decolonization as "
                  "structure-targeted. Assumptions: (1) colonial "
                  "logic lives in structures (canons, periodization, "
                  "collecting); (2) adding artists leaves structures "
                  "intact; (3) structural change is the test. "
                  "Reasoning path: the proposal predicts genuine "
                  "decolonization should change how art history is "
                  "done - which the leading work does. Addition is "
                  "then necessary but insufficient. Limits: the "
                  "model needs better structural-change measures; "
                  "the abolition-versus-reform debate continues."),
        pointer=('The Signature system models decolonization as structure-targeted: change how art history is done, not just who is included. The Signature test: change tracks structural measures. It would be refuted if additive inclusion transforms the field.'),
        key_points=[
            "Decolonial critiques target foundations.",
            "Adding artists leaves structures intact.",
            "Reform versus abolition is contested.",
            "What decolonization requires is open.",
        ],
        requirements=[
            "Structural-change measures.",
            "Foundation-critique development.",
            "Reform-versus-abolition analyses.",
        ],
        standards=[
            "Claims checked against the decolonial literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mignolo WD, Vazquez R. Decolonial aestheSis. 2013.",
            "Grant C, Price D. Decolonizing art history. Art History; 2020.",
        ],
        hypotheses=[
            "Structure targeting defines real decolonization.",
            "Addition suffices.",
            "Abolition is required.",
            "The project is incoherent.",
        ],
        confirm="Change tracks structural measures.",
        refute="Additive inclusion transforms the field.",
    ),
    dict(
        key="art-history-34",
        name="A Unified Theory of Art",
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can art theory unify - aesthetics, history, sociology, "
                 "and psychology - into one account of art?"),
        background=("Each approach captures something: aesthetics the "
                    "experience, history the change, sociology the "
                    "institution, psychology the mind. Unification "
                    "attempts remain programmatic. Whether art's "
                    "nature permits one theory is the discipline's "
                    "capstone."),
        why_it_matters=("This is art history's capstone: the answer "
                        "determines what art is."),
        sig_lens=("The Signature lens treats the approaches as a "
                  "question ledger: the Signature approach asks what "
                  "question each owns."),
        sig_body=("The Signature proposal models unification as "
                  "question-integration. Assumptions: (1) art spans "
                  "experience, history, institution, and mind; (2) "
                  "each approach owns questions; (3) the questions "
                  "interlock. Reasoning path: the proposal assigns "
                  "aesthetics to experience, history to change, "
                  "sociology to institution, psychology to mind - "
                  "with artistic practice as the integrator. Unity "
                  "comes from the practice that holds the questions "
                  "together. Limits: the integration is sketched; "
                  "partisans may reject the settlement."),
        pointer=('The Signature system assigns each approach its questions about art, with artistic practice as the integrator. The Signature test: integrated models predict across questions. It would be refuted if questions prove irreducible to common theory.'),
        key_points=[
            "Four approaches offer incompatible images of art.",
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
            "Claims checked against the art-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Carroll N. Art in Three Dimensions. Oxford University Press; 2010.",
            "Elkins J. Art History Versus Aesthetics. Routledge; 2006.",
        ],
        hypotheses=[
            "Question-integration unifies art theory.",
            "The approaches are incommensurable.",
            "One approach will absorb the rest.",
            "Pluralism is permanent.",
        ],
        confirm="Integrated models predict across questions.",
        refute="Questions prove irreducible to common theory.",
    ),
]
