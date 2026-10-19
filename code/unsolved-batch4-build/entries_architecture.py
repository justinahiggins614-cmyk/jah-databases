#!/usr/bin/env python3
"""Entries for the Unsolved Architecture databases (batch 4).

34 famous open problems in architecture, ladder-ordered by accessibility.
ID prefixes: JAH-USAC- (public) and JAH-USACS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="architecture-01",
        name="Form Follows Function: True",
        group="Design",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Is 'form follows function' true - or architecture's most "
                 "productive falsehood?"),
        background=("Sullivan's slogan became modernism's creed; yet "
                    "functions change while forms persist, and many "
                    "beautiful buildings serve functions poorly. The "
                    "slogan's truth - as description versus aspiration "
                    "- remains architecture's founding debate."),
        why_it_matters=("The slogan shaped a century of building. Its "
                        "truth determines design's foundation."),
        sig_lens=("The Signature lens treats the slogan as a time "
                  "ledger: the Signature approach asks what happens "
                  "when functions change."),
        sig_body=("The Signature proposal models the slogan as "
                  "aspiration-mistaken-for-description. Assumptions: (1) "
                  "forms outlive functions; (2) good forms accommodate "
                  "many functions; (3) the slogan described an ideal. "
                  "Reasoning path: the proposal predicts the best "
                  "buildings should be functionally loose-fit - "
                  "explaining why strict functionalism ages badly. "
                  "Form should then follow adaptability, not function. "
                  "Limits: the model needs better loose-fit measures; "
                  "some functions genuinely shape form."),
        pointer=('The Signature system recasts the slogan: form should follow adaptability, not function - loose-fit buildings outlive strict ones. The Signature test: longevity tracks loose-fit measures. It would be refuted if strictly functional buildings outlast.'),
        key_points=[
            "Sullivan's slogan became modernism's creed.",
            "Functions change; forms persist.",
            "Strict functionalism ages badly.",
            "Whether the slogan describes or prescribes is the debate.",
        ],
        requirements=[
            "Loose-fit measures across buildings.",
            "Functional-change case studies.",
            "An account of the slogan's persistence.",
        ],
        standards=[
            "Claims checked against the architectural-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Sullivan LH. The tall office building artistically considered. 1896.",
            "Forty A. Words and Buildings. Thames and Hudson; 2000.",
        ],
        hypotheses=[
            "Loose-fit explains building longevity.",
            "Function genuinely determines good form.",
            "The slogan is empty rhetoric.",
            "Adaptability is the true principle.",
        ],
        confirm="Longevity tracks loose-fit measures.",
        refute="Strictly functional buildings outlast.",
    ),
    dict(
        key="architecture-02",
        name="The Ornament Question",
        group="Design",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Is ornament crime (Loos) or architecture's soul - and "
                 "why did the debate define modernism?"),
        background=("Loos declared ornament criminal; modernists stripped "
                    "buildings bare; postmodernists brought decoration "
                    "back. Neuroscience now suggests humans crave visual "
                    "complexity. Whether ornament is essential or "
                    "expendable remains open."),
        why_it_matters=("Ornament decides what buildings look like. The "
                        "answer shapes the built world."),
        sig_lens=("The Signature lens treats ornament as a cognition "
                  "ledger: the Signature approach asks what the eye "
                  "wants."),
        sig_body=("The Signature proposal models ornament preference as "
                  "cognitive. Assumptions: (1) humans prefer visual "
                  "complexity at certain scales; (2) bare surfaces "
                  "understimulate; (3) the preference is measurable. "
                  "Reasoning path: the proposal predicts ornamented "
                  "buildings should test better on well-being measures "
                  "- which emerging evidence supports. Loos was then "
                  "wrong about human nature, right about dishonest "
                  "applied decoration. Limits: the model needs better "
                  "well-being studies; cultural variation needs "
                  "mapping."),
        pointer=('The Signature system models ornament preference as cognitive: humans need visual complexity, honestly integrated. The Signature test: well-being tracks complexity measures. It would be refuted if bare buildings test equally well.'),
        key_points=[
            "Loos declared ornament criminal in 1908.",
            "Modernists stripped buildings; postmodernists redecorated.",
            "Humans appear to crave visual complexity.",
            "Whether ornament is essential remains open.",
        ],
        requirements=[
            "Well-being studies by facade complexity.",
            "Cultural-variation mapping.",
            "An account of honest versus applied ornament.",
        ],
        standards=[
            "Claims checked against the architectural literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Loos A. Ornament and crime. 1908.",
            "Salingaros NA. A Theory of Architecture. Umbau-Verlag; 2006.",
        ],
        hypotheses=[
            "Cognitive preference explains ornament's return.",
            "Ornament is culturally arbitrary.",
            "Minimalism suits modern cognition.",
            "The debate is purely ideological.",
        ],
        confirm="Well-being tracks complexity measures.",
        refute="Bare buildings test equally well.",
    ),
    dict(
        key="architecture-03",
        name="Why Buildings Fail",
        group="Practice",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("Why do buildings fail - leak, crack, disappoint - and is "
                 "failure built into how we build?"),
        background=("Building failures follow patterns: water ingress, "
                    "material incompatibility, value-engineered details. "
                    "The causes are organizational (fragmented "
                    "responsibility, lowest-bidder procurement) as much "
                    "as technical. Whether the industry's structure "
                    "guarantees failure remains the open question."),
        why_it_matters=("Building failure wastes billions and endangers "
                        "lives. Its causes determine reform."),
        sig_lens=("The Signature lens treats failure as a responsibility "
                  "ledger: the Signature approach asks who owns the "
                  "details."),
        sig_body=("The Signature proposal models failure as "
                  "fragmentation-driven. Assumptions: (1) buildings are "
                  "systems; (2) responsibility is fragmented across "
                  "trades; (3) interfaces fail first. Reasoning path: "
                  "the proposal predicts failures should concentrate "
                  "at trade interfaces - which forensic studies "
                  "confirm. Integrated delivery (one team owning the "
                  "whole) then reduces failure. Limits: the model "
                  "needs better interface-failure data; the "
                  "procurement reforms need testing."),
        pointer=('The Signature system models building failure as fragmentation-driven, with integrated delivery as the remedy. The Signature test: failures concentrate at interfaces. It would be refuted if integrated teams fail equally.'),
        key_points=[
            "Failures follow patterns: water, materials, details.",
            "Causes are organizational as much as technical.",
            "Interfaces between trades fail first.",
            "Whether the structure guarantees failure is open.",
        ],
        requirements=[
            "Interface-failure forensic data.",
            "Integrated-delivery outcome studies.",
            "Procurement-reform evaluations.",
        ],
        standards=[
            "Claims checked against the building-pathology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Brand S. How Buildings Learn. Viking; 1994.",
            "Atkinson AR. The pathology of building defects. 2003.",
        ],
        hypotheses=[
            "Fragmentation explains failure patterns.",
            "Technical complexity is the cause.",
            "Lowest-bid procurement is the cause.",
            "Failure rates are acceptable.",
        ],
        confirm="Failures concentrate at interfaces.",
        refute="Integrated teams fail equally.",
    ),
    dict(
        key="architecture-04",
        name='The Authority Problem in Architecture',
        group="Practice",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("What authority should architects have - artist, technician, "
                 "or coordinator - and why has the profession lost ground?"),
        background=("Architects once led building; now developers, "
                    "contractors, and consultants fragment the role. "
                    "Fees fell, liability rose, and design-build "
                    "marginalized the architect. Whether the profession "
                    "can reclaim authority - and on what basis - remains "
                    "open."),
        why_it_matters=("The architect's role shapes building quality. "
                        "Its decline affects the built environment."),
        sig_lens=("The Signature lens treats authority as a value ledger: "
                  "the Signature approach asks what architects provide "
                  "that others cannot."),
        sig_body=("The Signature proposal models the decline as "
                  "value-unproven. Assumptions: (1) authority follows "
                  "demonstrated value; (2) architects claim aesthetic "
                  "value; (3) clients measure financial value. "
                  "Reasoning path: the proposal predicts architects "
                  "should regain authority where they prove "
                  "performance value (energy, well-being, asset value) "
                  "- which leading firms do. The profession's future "
                  "is then evidence-based, not art-based. Limits: the "
                  "model needs better value demonstrations; the "
                  "art-versus-service tension persists."),
        pointer=('The Signature system models architectural authority as value-dependent: prove performance value to regain the lead. The Signature test: authority tracks demonstrated value. It would be refuted if aesthetic authority alone sustains practices.'),
        key_points=[
            "Architects lost ground to developers and contractors.",
            "Fees fell while liability rose.",
            "Design-build marginalized the role.",
            "Whether authority can be reclaimed is open.",
        ],
        requirements=[
            "Value-demonstration studies.",
            "Authority-outcome correlations.",
            "An account of the art-service tension.",
        ],
        standards=[
            "Claims checked against the profession literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Gutman R. Architectural Practice: A Critical View. Princeton Architectural Press; 1988.",
            "Cuff D. Architecture: The Story of Practice. MIT Press; 1991.",
        ],
        hypotheses=[
            "Value demonstration restores authority.",
            "The decline is irreversible.",
            "Art-based authority suffices.",
            "Coordination is the future role.",
        ],
        confirm="Authority tracks demonstrated value.",
        refute="Aesthetic authority alone sustains practices.",
    ),
    dict(
        key="architecture-05",
        name="What Makes a Building Beautiful",
        group="Theory",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("What makes a building beautiful - is beauty objective, "
                 "cultural, or personal?"),
        background=("Philosophers debate beauty's objectivity; "
                    "environmental psychology finds surprising agreement "
                    "on preferred buildings (complexity, coherence, "
                    "natural elements). Yet architectural elites and "
                    "publics disagree sharply. Whether a science of "
                    "architectural beauty is possible remains open."),
        why_it_matters=("Beauty judgments shape cities. Their basis "
                        "determines design's legitimacy."),
        sig_lens=("The Signature lens treats beauty as an agreement "
                  "ledger: the Signature approach asks where people "
                  "agree and where they diverge."),
        sig_body=("The Signature proposal models beauty judgments as "
                  "layered: shared perceptual preferences (complexity, "
                  "coherence, nature) plus cultural and personal "
                  "variation. Assumptions: (1) the perceptual layer is "
                  "widely shared; (2) elites are trained away from it; "
                  "(3) the layers interact. Reasoning path: the "
                  "proposal predicts public-elite disagreement should "
                  "concentrate where training overrides perception - "
                  "which the evidence supports. A partial science of "
                  "beauty is then possible at the perceptual layer. "
                  "Limits: the model needs better cross-cultural data; "
                  "the elite-formation mechanism needs study."),
        pointer=('The Signature system models architectural beauty as layered: shared perceptual preferences beneath cultural and trained variation. The Signature test: agreement concentrates at the perceptual layer. It would be refuted if no cross-cultural agreement is found.'),
        key_points=[
            "Environmental psychology finds real agreement on buildings.",
            "Elites and publics disagree sharply.",
            "Complexity, coherence, and nature predict preference.",
            "Whether a science of beauty is possible is open.",
        ],
        requirements=[
            "Cross-cultural preference studies.",
            "Elite-formation analyses.",
            "Perceptual-layer isolation tests.",
        ],
        standards=[
            "Claims checked against the aesthetics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kaplan R, Kaplan S. The Experience of Nature. Cambridge University Press; 1989.",
            "Nasar JL. The Evaluative Image of the City. Sage; 1998.",
        ],
        hypotheses=[
            "Layered beauty explains agreement patterns.",
            "Beauty is purely subjective.",
            "Beauty is fully objective.",
            "Elite taste is the valid standard.",
        ],
        confirm="Agreement concentrates at the perceptual layer.",
        refute="No cross-cultural agreement is found.",
    ),
    dict(
        key="architecture-06",
        name="Proportion: The Golden Ratio Myth",
        group="Theory",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Does the golden ratio govern beauty - or is it "
                 "architecture's most persistent myth?"),
        background=("The golden ratio's beauty claims are mostly myth: "
                    "studies find weak or no preference, and historical "
                    "uses are often retrofitted. Yet proportion clearly "
                    "matters - buildings with coherent proportional "
                    "systems please more. What proportional principles "
                    "actually work remains open."),
        why_it_matters=("Proportion systems guide design. The myth's "
                        "debunking clears the way for real principles."),
        sig_lens=("The Signature lens treats proportion as an evidence "
                  "ledger: the Signature approach asks what the studies "
                  "actually show."),
        sig_body=("The Signature proposal models the golden ratio as "
                  "myth-with-kernel. Assumptions: (1) the specific "
                  "ratio claims fail; (2) proportional coherence "
                  "matters; (3) the myth persists from narrative "
                  "appeal. Reasoning path: the proposal shows "
                  "coherence (related parts) predicts preference "
                  "better than any ratio - explaining both the myth's "
                  "failure and proportion's importance. Designers "
                  "should then seek relational systems, not magic "
                  "numbers. Limits: the model needs better coherence "
                  "measures; cultural proportional traditions need "
                  "respect."),
        pointer=('The Signature system debunks the golden ratio while affirming proportional coherence: seek relational systems, not magic numbers. The Signature test: coherence outperforms ratio in prediction. It would be refuted if golden-ratio buildings test preferred.'),
        key_points=[
            "Golden-ratio beauty claims mostly fail testing.",
            "Historical uses are often retrofitted.",
            "Proportional coherence does predict preference.",
            "The myth persists from narrative appeal.",
        ],
        requirements=[
            "Coherence-versus-ratio preference tests.",
            "Historical-use audits.",
            "Cultural proportional-tradition studies.",
        ],
        standards=[
            "Claims checked against the proportion literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Livio M. The Golden Ratio. Broadway; 2002.",
            "Green CD. All that glitters: a review of psychological research on the aesthetics of the golden section. 1995.",
        ],
        hypotheses=[
            "Coherence, not ratio, drives preference.",
            "The golden ratio has real effects.",
            "Proportion is culturally arbitrary.",
            "The myth is harmless.",
        ],
        confirm="Coherence outperforms ratio in prediction.",
        refute="Golden-ratio buildings test preferred.",
    ),
    dict(
        key="architecture-07",
        name="Light as a Building Material",
        group="Design",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("How should architects design with light - and why is "
                 "daylighting still more art than science?"),
        background=("Light shapes experience profoundly (Ando, Kahn, "
                    "Holl); daylighting science quantifies illuminance "
                    "but not delight. The gap between measured light and "
                    "felt light - between lux and atmosphere - remains "
                    "architecture's luminous puzzle."),
        why_it_matters=("Light is architecture's cheapest powerful "
                        "material. Its mastery defines great buildings."),
        sig_lens=("The Signature lens treats light as an experience "
                  "ledger: the Signature approach asks what measured "
                  "light misses."),
        sig_body=("The Signature proposal models luminous experience as "
                  "contrast-and-change. Assumptions: (1) the eye "
                  "adapts to absolute levels; (2) contrast and temporal "
                  "change drive experience; (3) metrics miss both. "
                  "Reasoning path: the proposal predicts delight "
                  "should track contrast choreography, not illuminance "
                  "- explaining the masters' effects. Daylighting "
                  "science then needs experience metrics. Limits: the "
                  "model needs better experience measures; the "
                  "energy-daylighting tradeoff needs managing."),
        pointer=('The Signature system models luminous delight as contrast and change, not illuminance: choreograph contrast. The Signature test: delight tracks contrast measures. It would be refuted if illuminance predicts delight fully.'),
        key_points=[
            "Light shapes architectural experience profoundly.",
            "Daylighting science measures illuminance, not delight.",
            "Contrast and change may drive experience.",
            "The lux-atmosphere gap remains.",
        ],
        requirements=[
            "Experience-based light metrics.",
            "Contrast-choreography studies.",
            "Energy-daylighting tradeoff analyses.",
        ],
        standards=[
            "Claims checked against the daylighting literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Holl S. Parallax. Princeton Architectural Press; 2000.",
            "Boyce PR. Human Factors in Lighting. CRC Press; 2014.",
        ],
        hypotheses=[
            "Contrast-and-change explains luminous delight.",
            "Illuminance suffices with good design.",
            "Light experience is unmeasurable.",
            "Cultural variation dominates.",
        ],
        confirm="Delight tracks contrast measures.",
        refute="Illuminance predicts delight fully.",
    ),
    dict(
        key="architecture-08",
        name="The Staircase Problem",
        group="Design",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Why are stairs architecture's hardest element - "
                 "simultaneously circulation, sculpture, and safety "
                 "hazard?"),
        background=("Stairs injure more people than any building element "
                    "except floors; yet they are architecture's great "
                    "sculptural opportunity (Vatican, Apple stores). "
                    "Codes constrain dimensions tightly. The tension "
                    "between safety, function, and beauty makes stairs "
                    "the proving ground of design."),
        why_it_matters=("Stairs injure thousands yearly. Their design is "
                        "safety-critical art."),
        sig_lens=("The Signature lens treats stairs as a tolerance "
                  "ledger: the Signature approach asks how much "
                  "variation the foot tolerates."),
        sig_body=("The Signature proposal models stair safety as "
                  "uniformity-dependent. Assumptions: (1) the gait "
                  "expects consistent risers; (2) single deviations "
                  "cause falls; (3) beauty tempts variation. Reasoning "
                  "path: the proposal predicts injuries should "
                  "concentrate at non-uniform stairs - which the data "
                  "confirm. Sculptural ambition must then work within "
                  "uniformity: the art is in the consistent gesture. "
                  "Limits: the model needs better fall-data; "
                  "accessibility (ramps, lifts) needs integration."),
        pointer=('The Signature system models stair safety as uniformity-dependent: sculptural ambition must work within consistent dimensions. The Signature test: injuries concentrate at non-uniform stairs. It would be refuted if varied stairs prove equally safe.'),
        key_points=[
            "Stairs are a leading cause of building injuries.",
            "They are also architecture's sculptural opportunity.",
            "Codes tightly constrain dimensions.",
            "Uniformity appears safety-critical.",
        ],
        requirements=[
            "Fall-data by stair uniformity.",
            "Sculptural-within-uniformity case studies.",
            "Accessibility integration analyses.",
        ],
        standards=[
            "Claims checked against the stair-safety literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Templer J. The Staircase. MIT Press; 1992.",
            "Roys MS. Serious stair injuries. 2001.",
        ],
        hypotheses=[
            "Uniformity dependence explains injury patterns.",
            "Beauty and safety inherently conflict.",
            "Codes are over-restrictive.",
            "Behavior, not design, causes falls.",
        ],
        confirm="Injuries concentrate at non-uniform stairs.",
        refute="Varied stairs prove equally safe.",
    ),
    dict(
        key="architecture-09",
        name="Threshold Design: The Entrance",
        group="Design",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("What makes an entrance work - welcoming, legible, and "
                 "memorable at once?"),
        background=("Entrances are architecture's handshake: they orient, "
                    "impress, and control. Yet many buildings hide their "
                    "doors (minimalism, security). The psychology of "
                    "arrival - prospect, refuge, legibility - suggests "
                    "principles, but the synthesis remains craft, not "
                    "science."),
        why_it_matters=("Entrances shape first impressions and access. "
                        "Their design is hospitality built."),
        sig_lens=("The Signature lens treats entrances as a transition "
                  "ledger: the Signature approach asks what the "
                  "threshold does to the visitor."),
        sig_body=("The Signature proposal models entrance experience as "
                  "graded transition. Assumptions: (1) abrupt "
                  "inside-outside shifts disorient; (2) graded "
                  "thresholds (porch, lobby, sequence) ease arrival; "
                  "(3) legibility needs visual prospect. Reasoning "
                  "path: the proposal predicts well-being and "
                  "orientation should track threshold grading - which "
                  "the evidence supports. Entrances should then be "
                  "sequences, not doors. Limits: the model needs "
                  "better arrival-experience measures; security "
                  "needs constrain."),
        pointer=('The Signature system models entrances as graded transitions: design sequences, not doors. The Signature test: experience tracks threshold grading. It would be refuted if single-door entrances test equally well.'),
        key_points=[
            "Entrances orient, impress, and control.",
            "Many contemporary buildings hide their doors.",
            "Graded thresholds ease arrival.",
            "The synthesis remains craft, not science.",
        ],
        requirements=[
            "Arrival-experience measures.",
            "Threshold-grading studies.",
            "Security-hospitality tradeoff analyses.",
        ],
        standards=[
            "Claims checked against the environmental-psychology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Alexander C et al. A Pattern Language. Oxford University Press; 1977.",
            "Kaplan R, Kaplan S. The Experience of Nature. Cambridge University Press; 1989.",
        ],
        hypotheses=[
            "Graded transition explains entrance quality.",
            "Minimal hidden entrances work fine.",
            "Cultural variation dominates.",
            "Security makes good entrances impossible.",
        ],
        confirm="Experience tracks threshold grading.",
        refute="Single-door entrances test equally well.",
    ),
    dict(
        key="architecture-10",
        name="The Facade Problem",
        group="Design",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("What should a facade do - express structure, please the "
                 "street, or disappear?"),
        background=("Facades are buildings' public face: structural "
                    "expressionists show the bones, contextualists blend "
                    "in, minimalists dematerialize. The facade's duties "
                    "(to occupants, street, city) conflict. No theory "
                    "reconciles them."),
        why_it_matters=("Facades make the city. Their duties determine "
                        "urban beauty."),
        sig_lens=("The Signature lens treats facades as a duty ledger: "
                  "the Signature approach asks whom the face serves."),
        sig_body=("The Signature proposal models facade duties as "
                  "multi-principal. Assumptions: (1) occupants need "
                  "light and view; (2) streets need coherence and "
                  "interest; (3) cities need identity. Reasoning path: "
                  "the proposal predicts the best facades should "
                  "satisfy all three - explaining why single-duty "
                  "facades (pure expression, pure context) disappoint. "
                  "The design problem is then multi-objective "
                  "optimization. Limits: the model needs better "
                  "multi-duty evaluations; the tradeoffs need "
                  "mapping."),
        pointer=('The Signature system models facades as multi-duty: serve occupants, street, and city together. The Signature test: quality tracks multi-duty satisfaction. It would be refuted if single-duty facades test best.'),
        key_points=[
            "Facades serve occupants, streets, and cities.",
            "The duties conflict.",
            "Single-duty facades disappoint.",
            "No theory reconciles the duties.",
        ],
        requirements=[
            "Multi-duty facade evaluations.",
            "Tradeoff mapping studies.",
            "An account of facade failures.",
        ],
        standards=[
            "Claims checked against the facade literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Forty A. Words and Buildings. Thames and Hudson; 2000.",
            "Ellis W. The facade. 1986.",
        ],
        hypotheses=[
            "Multi-objective optimization captures facade quality.",
            "One duty should dominate.",
            "Facades are arbitrary fashion.",
            "Context always wins.",
        ],
        confirm="Quality tracks multi-duty satisfaction.",
        refute="Single-duty facades test best.",
    ),
    dict(
        key="architecture-11",
        name="Materials Honesty: Must It Hold",
        group="Theory",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Must materials be honest - expressing their nature - or "
                 "is the honesty doctrine itself dishonest?"),
        background=("Modernists demanded honest materials (concrete as "
                    "concrete); yet concrete is often painted, steel "
                    "clad, and timber faked. The doctrine's rigidity "
                    "clashes with craft traditions of transformation "
                    "(Japanese lacquer, Venetian stucco). Whether "
                    "honesty is principle or prejudice remains open."),
        why_it_matters=("Material honesty shapes tectonic expression. "
                        "Its status determines design freedom."),
        sig_lens=("The Signature lens treats honesty as a craft ledger: "
                  "the Signature approach asks what transformation "
                  "traditions knew."),
        sig_body=("The Signature proposal models material honesty as "
                  "craft-relative. Assumptions: (1) all building "
                  "transforms materials; (2) traditions judge "
                  "transformation by craft standards; (3) modernism "
                  "imposed one standard. Reasoning path: the proposal "
                  "shows the doctrine confuses a particular craft "
                  "ethic with universality - explaining the clash "
                  "with transformation traditions. Honesty is then "
                  "about craft integrity, not material nudity. Limits: "
                  "the model needs better craft-ethic comparisons; "
                  "the sustainability dimension needs adding."),
        pointer=('The Signature system recasts material honesty as craft integrity, not material nudity. The Signature test: judgments track craft-ethic measures. It would be refuted if material nudity universally preferred.'),
        key_points=[
            "Modernists demanded honest material expression.",
            "Craft traditions transform materials elaborately.",
            "The doctrine clashes with those traditions.",
            "Whether honesty is principle or prejudice is open.",
        ],
        requirements=[
            "Craft-ethic comparative studies.",
            "Transformation-tradition documentation.",
            "Sustainability-dimension analyses.",
        ],
        standards=[
            "Claims checked against the tectonics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Frampton K. Studies in Tectonic Culture. MIT Press; 1995.",
            "Forty A. Concrete and Culture. Reaktion; 2012.",
        ],
        hypotheses=[
            "Craft-relativity explains the clash.",
            "Honesty is universal principle.",
            "The doctrine is modernist prejudice.",
            "Sustainability reframes the question.",
        ],
        confirm="Judgments track craft-ethic measures.",
        refute="Material nudity universally preferred.",
    ),
    dict(
        key="architecture-12",
        name="Brutalism: Failure or Triumph",
        group="Styles",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Was Brutalism a failure of inhuman concrete - or a "
                 "triumph now being demolished by fashion?"),
        background=("Brutalist buildings won awards then public hatred; "
                    "now preservationists fight demolitions while "
                    "critics cheer. The questions: whether the "
                    "failures were architectural (materials, scale) or "
                    "social (maintenance, stigma), and whether the "
                    "reappraisal is taste-cycle or truth."),
        why_it_matters=("Brutalist demolitions are irreversible. The "
                        "verdict determines what survives."),
        sig_lens=("The Signature lens treats Brutalism as an attribution "
                  "ledger: the Signature approach asks what failed - "
                  "the concrete or the care."),
        sig_body=("The Signature proposal models Brutalism's reception "
                  "as maintenance-mediated. Assumptions: (1) concrete "
                  "weathers badly without care; (2) stigmatized "
                  "buildings lose maintenance; (3) the spiral is "
                  "self-fulfilling. Reasoning path: the proposal "
                  "predicts well-maintained Brutalist buildings should "
                  "test well - which they do (Barbican, Boston City "
                  "Hall debates). The failure was then custodial, not "
                  "architectural. Limits: the model needs better "
                  "maintenance-outcome data; the scale question "
                  "persists."),
        pointer=("The Signature system models Brutalism's failure as custodial: well-maintained concrete tests well; stigma starved maintenance. The Signature test: reception tracks maintenance measures. It would be refuted if well-kept Brutalism still tests hated."),
        key_points=[
            "Brutalism won awards, then public hatred, now reappraisal.",
            "Demolitions are irreversible.",
            "Maintenance histories track reception.",
            "Whether reappraisal is taste or truth is open.",
        ],
        requirements=[
            "Maintenance-outcome studies.",
            "Stigma-spiral analyses.",
            "Preservation decision frameworks.",
        ],
        standards=[
            "Claims checked against the Brutalism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Calder B. Raw Concrete. William Heinemann; 2016.",
            "Clement A. Brutalism: Post-War British Architecture. Crowood; 2011.",
        ],
        hypotheses=[
            "Maintenance mediation explains reception.",
            "Brutalism is inherently inhuman.",
            "The reappraisal is pure taste cycle.",
            "Scale, not maintenance, is the issue.",
        ],
        confirm="Reception tracks maintenance measures.",
        refute="Well-kept Brutalism still tests hated.",
    ),
    dict(
        key="architecture-13",
        name='The Social Promise of Modernism',
        group="Styles",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("Did modernism's social promise - better life through "
                 "better building - fail, and if so, why?"),
        background=("Modernists promised light, air, and equality; the "
                    "tower blocks became symbols of failure. Explanations: "
                    "the architecture was fine but management failed; "
                    "the architecture itself was anti-social; the "
                    "promise was always ideology. The attribution "
                    "remains contested."),
        why_it_matters=("The verdict shapes housing policy and "
                        "architectural ambition. The promise's fate is "
                        "modernism's trial."),
        sig_lens=("The Signature lens treats the promise as a "
                  "management ledger: the Signature approach asks what "
                  "happened after the architects left."),
        sig_body=("The Signature proposal models the failure as "
                  "post-occupancy. Assumptions: (1) modernist housing "
                  "needed management; (2) management was underfunded; "
                  "(3) concentrated poverty overwhelmed design. "
                  "Reasoning path: the proposal predicts well-managed "
                  "modernist estates should succeed - which they do "
                  "(Barbican again, many co-ops). Architecture was "
                  "then necessary but insufficient; the social promise "
                  "needed social investment. Limits: the model needs "
                  "better management-outcome data; the design "
                  "critiques need separate evaluation."),
        pointer=("The Signature system models modernism's social failure as post-occupancy: architecture needed social investment it did not get. The Signature test: outcomes track management measures. It would be refuted if well-managed estates still fail."),
        key_points=[
            "Modernists promised better life through building.",
            "Tower blocks became failure symbols.",
            "Management and poverty confound the verdict.",
            "Well-managed estates succeed.",
        ],
        requirements=[
            "Management-outcome studies.",
            "Design-versus-management decomposition.",
            "An account of the promise's ideology.",
        ],
        standards=[
            "Claims checked against the modernism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bristol K. The Pruitt-Igoe myth. 1991.",
            "Hanley L. Estates: An Intimate History. Granta; 2007.",
        ],
        hypotheses=[
            "Post-occupancy factors explain the failure.",
            "The architecture was inherently anti-social.",
            "The promise was always ideological.",
            "Design and management share blame.",
        ],
        confirm="Outcomes track management measures.",
        refute="Well-managed estates still fail.",
    ),
    dict(
        key="architecture-14",
        name="Postmodernism: What Was It",
        group="Styles",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("What was postmodernism - serious architectural movement "
                 "or ironic fashion - and what did it leave?"),
        background=("Venturi's complexity-and-contradiction, Graves's "
                    "playful classicism, then the 1980s excesses and "
                    "the fall. Historians now reassess: postmodernism "
                    "legitimated context, history, and meaning after "
                    "modernist bans. Whether it was a correction or a "
                    "detour remains debated."),
        why_it_matters=("Postmodernism's legacy shapes current practice. "
                        "Its meaning determines what was learned."),
        sig_lens=("The Signature lens treats postmodernism as a "
                  "correction ledger: the Signature approach asks what "
                  "modernism banned that needed return."),
        sig_body=("The Signature proposal models postmodernism as "
                  "corrective, not alternative. Assumptions: (1) "
                  "modernism banned history, ornament, and meaning; "
                  "(2) the bans impoverished architecture; (3) "
                  "postmodernism restored them. Reasoning path: the "
                  "proposal predicts postmodernism's lasting "
                  "contributions should be the restorations (context, "
                  "meaning) not the ironies - which matches current "
                  "practice. It was then a necessary correction with "
                  "expendable style. Limits: the model needs better "
                  "legacy analyses; the irony question persists."),
        pointer=('The Signature system models postmodernism as a necessary correction: its lasting gifts are context and meaning, not irony. The Signature test: practice retains the restorations, not the ironies. It would be refuted if no lasting contribution is found.'),
        key_points=[
            "Postmodernism restored history, ornament, and meaning.",
            "The 1980s excesses discredited it.",
            "Historians now reassess its contributions.",
            "Whether correction or detour is debated.",
        ],
        requirements=[
            "Legacy analyses by contribution.",
            "Context-and-meaning practice studies.",
            "An account of the irony dimension.",
        ],
        standards=[
            "Claims checked against the postmodernism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Venturi R. Complexity and Contradiction in Architecture. MoMA; 1966.",
            "Jencks C. The Language of Post-Modern Architecture. Rizzoli; 1977.",
        ],
        hypotheses=[
            "Corrective model explains the legacy.",
            "Postmodernism was mere fashion.",
            "It was a full alternative paradigm.",
            "Its irony was the point.",
        ],
        confirm="Practice retains the restorations, not the ironies.",
        refute="No lasting contribution is found.",
    ),
    dict(
        key="architecture-15",
        name="Vernacular Architecture: The Lesson",
        group="Styles",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("What should architects learn from vernacular building - "
                 "and can its lessons transfer to modern practice?"),
        background=("Rudofsky celebrated architecture without architects; "
                    "vernacular buildings show climate wisdom, material "
                    "economy, and cultural fit. But romanticizing "
                    "poverty building is suspect, and modern codes and "
                    "programs differ. Which lessons transfer remains "
                    "open."),
        why_it_matters=("Vernacular wisdom could green and humanize "
                        "practice. Its transferability determines its "
                        "value."),
        sig_lens=("The Signature lens treats vernacular as a climate "
                  "ledger: the Signature approach asks what problem "
                  "each tradition solved."),
        sig_body=("The Signature proposal models vernacular lessons as "
                  "problem-specific. Assumptions: (1) each tradition "
                  "solved local climate and material problems; (2) "
                  "the solutions are extractable as principles; (3) "
                  "modern contexts differ. Reasoning path: the "
                  "proposal predicts transfer should work at the "
                  "principle level (thermal mass, shading, local "
                  "materials) not the form level - which successful "
                  "adaptations confirm. Learn the physics, not the "
                  "picturesque. Limits: the model needs better "
                  "principle-extraction studies; the romanticization "
                  "risk needs guarding."),
        pointer=('The Signature system models vernacular lessons as principle-level: learn the physics, not the picturesque. The Signature test: success tracks principle application. It would be refuted if principle transfer fails in modern contexts.'),
        key_points=[
            "Vernacular buildings show climate and material wisdom.",
            "Romanticizing poverty building is suspect.",
            "Principle-level transfer works; form copying does not.",
            "Which lessons transfer remains open.",
        ],
        requirements=[
            "Principle-extraction studies.",
            "Transfer success analyses.",
            "Anti-romanticization guards.",
        ],
        standards=[
            "Claims checked against the vernacular literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rudofsky B. Architecture Without Architects. MoMA; 1964.",
            "Oliver P. Encyclopedia of Vernacular Architecture of the World. Cambridge University Press; 1997.",
        ],
        hypotheses=[
            "Principle-level transfer captures the value.",
            "Vernacular is inapplicable to modernity.",
            "Form-level imitation suffices.",
            "The lessons are overstated.",
        ],
        confirm="Success tracks principle application.",
        refute="Principle transfer fails in modern contexts.",
    ),
    dict(
        key="architecture-16",
        name="The Skyscraper Problem",
        group="Design",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("Are skyscrapers good city-building - or monuments to "
                 "ego that damage the street?"),
        background=("Towers concentrate jobs and enable density; they "
                    "also create wind, shadow, and dead streets. The "
                    "supertall luxury tower sharpens the question: "
                    "density for whom? Whether towers serve cities or "
                    "investors remains contested."),
        why_it_matters=("Towers reshape skylines and streets. Their "
                        "urban value determines planning's stance."),
        sig_lens=("The Signature lens treats towers as a street ledger: "
                  "the Signature approach asks what the tower gives "
                  "the sidewalk."),
        sig_body=("The Signature proposal models tower quality as "
                  "street-contingent. Assumptions: (1) density benefits "
                  "are real; (2) street damage is design-dependent; "
                  "(3) luxury supertalls capture little public value. "
                  "Reasoning path: the proposal predicts towers should "
                  "be judged by their street interface - explaining "
                  "why some towers enrich cities and others deaden "
                  "them. The policy answer is then street-performance "
                  "standards, not height limits. Limits: the model "
                  "needs better street-impact measures; the housing "
                  "economics need separating."),
        pointer=('The Signature system judges towers by their street interface: street-performance standards, not height limits. The Signature test: urban value tracks street-interface measures. It would be refuted if tower design shows no street effect.'),
        key_points=[
            "Towers enable density but can damage streets.",
            "Wind, shadow, and dead frontages are the costs.",
            "Luxury supertalls sharpen the for-whom question.",
            "Whether towers serve cities is contested.",
        ],
        requirements=[
            "Street-impact measures by tower design.",
            "Density-benefit quantifications.",
            "Housing-economics separation.",
        ],
        standards=[
            "Claims checked against the tall-buildings literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Willis C. Form Follows Finance. Princeton Architectural Press; 1995.",
            "Graham S. Vertical. Verso; 2016.",
        ],
        hypotheses=[
            "Street contingency explains tower outcomes.",
            "Towers are inherently anti-urban.",
            "Density justifies any tower.",
            "Height limits are the answer.",
        ],
        confirm="Urban value tracks street-interface measures.",
        refute="Tower design shows no street effect.",
    ),
    dict(
        key="architecture-17",
        name="Housing: Why So Ugly",
        group="Practice",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Why is so much new housing ugly - and whose fault is "
                 "it?"),
        background=("Volume housebuilders produce repetitive boxes; "
                    "architects blame developers, developers blame "
                    "buyers and planners, buyers blame architects. The "
                    "economics (land costs, risk, standardization) "
                    "push toward the mean. Whether good design can "
                    "survive the economics remains open."),
        why_it_matters=("Housing is most people's architecture. Its "
                        "quality is everyone's environment."),
        sig_lens=("The Signature lens treats housing as a margin "
                  "ledger: the Signature approach asks where design "
                  "money goes."),
        sig_body=("The Signature proposal models housing quality as "
                  "margin-squeezed. Assumptions: (1) land and finance "
                  "costs dominate; (2) design is a small, cuttable "
                  "margin; (3) buyers cannot judge plans well. "
                  "Reasoning path: the proposal predicts quality "
                  "should appear where margins allow (custom, "
                  "high-end) and vanish where squeezed - which "
                  "matches the market. The fixes are then structural "
                  "(design codes, pattern books) not hortatory. "
                  "Limits: the model needs better margin analyses; "
                  "the buyer-judgment question needs study."),
        pointer=('The Signature system models housing ugliness as margin-squeezed: structural fixes like design codes, not exhortation. The Signature test: quality tracks margin measures. It would be refuted if well-funded volume housing stays ugly.'),
        key_points=[
            "Volume housing is repetitive and often ugly.",
            "Blame circulates among architects, developers, buyers.",
            "Land and finance costs squeeze design margins.",
            "Whether good design can survive is open.",
        ],
        requirements=[
            "Margin analyses by housing type.",
            "Design-code effectiveness studies.",
            "Buyer-judgment research.",
        ],
        standards=[
            "Claims checked against the housing literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Parnell S. Housing design: the economics. 2015.",
            "Pollalis S et al. Housing and economics. 2018.",
        ],
        hypotheses=[
            "Margin squeeze explains the pattern.",
            "Architects failed housing.",
            "Buyers prefer the boxes.",
            "Regulation is the main cause.",
        ],
        confirm="Quality tracks margin measures.",
        refute="Well-funded volume housing stays ugly.",
    ),
    dict(
        key="architecture-18",
        name="The Public Space Problem",
        group="Urban",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("What makes public space work - and why do so many plazas "
                 "sit empty?"),
        background=("Whyte showed people attract people (sittable space, "
                    "food, sun); Gehl documented life between buildings. "
                    "Yet developers keep building windswept plazas. "
                    "Whether the knowledge is ignored or the incentives "
                    "misaligned remains the question."),
        why_it_matters=("Public space is democracy's stage. Its success "
                        "determines urban life."),
        sig_lens=("The Signature lens treats plazas as an incentive "
                  "ledger: the Signature approach asks who benefits "
                  "from the empty plaza."),
        sig_body=("The Signature proposal models empty plazas as "
                  "incentive-misaligned. Assumptions: (1) the "
                  "knowledge of good space exists (Whyte, Gehl); (2) "
                  "plazas are built for approvals, not people; (3) "
                  "nobody is accountable for life. Reasoning path: the "
                  "proposal predicts lively spaces where someone owns "
                  "the outcome - explaining the knowledge-practice "
                  "gap. The fix is then accountability (post-"
                  "occupancy requirements), not more research. Limits: "
                  "the model needs better accountability studies; "
                  "cultural variation needs mapping."),
        pointer=('The Signature system models empty plazas as incentive-misaligned: assign accountability for liveliness, not just more research. The Signature test: liveliness tracks accountability measures. It would be refuted if accountable plazas still sit empty.'),
        key_points=[
            "Whyte and Gehl established what works.",
            "Empty plazas keep being built.",
            "Sittable space, food, and sun attract people.",
            "Whether knowledge or incentives are the gap is the question.",
        ],
        requirements=[
            "Accountability-mechanism studies.",
            "Post-occupancy liveliness requirements.",
            "Cultural-variation mapping.",
        ],
        standards=[
            "Claims checked against the public-space literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Whyte WH. The Social Life of Small Urban Spaces. Conservation Foundation; 1980.",
            "Gehl J. Life Between Buildings. Island Press; 1987.",
        ],
        hypotheses=[
            "Incentive misalignment explains the gap.",
            "The knowledge is insufficient.",
            "Developers know but do not care.",
            "Regulations force bad plazas.",
        ],
        confirm="Liveliness tracks accountability measures.",
        refute="Accountable plazas still sit empty.",
    ),
    dict(
        key="architecture-19",
        name="Monuments: Who Decides",
        group="Urban",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("Who decides what monuments stand - and what should "
                 "happen to contested ones?"),
        background=("Monument controversies (Confederate statues, "
                    "colonial figures) forced the question: whose "
                    "history gets stone? Options: remove, contextualize, "
                    "counter-monument, or leave. No democratic theory of "
                    "monuments commands consensus."),
        why_it_matters=("Monuments shape collective memory. Their "
                        "governance is democracy's self-portrait."),
        sig_lens=("The Signature lens treats monuments as a memory "
                  "ledger: the Signature approach asks whose past the "
                  "stone serves."),
        sig_body=("The Signature proposal models monument decisions as "
                  "memory-politics. Assumptions: (1) monuments encode "
                  "a past generation's values; (2) values change; (3) "
                  "no neutral procedure exists. Reasoning path: the "
                  "proposal predicts contestation should track value "
                  "change - which it does - and that the stable "
                  "solution is periodic democratic review, not "
                  "permanent verdicts. Monuments are then conversations "
                  "across generations, not conclusions. Limits: the "
                  "model needs better review-process designs; the "
                  "vandalism-versus-process question persists."),
        pointer=('The Signature system models monuments as cross-generational conversations: periodic democratic review, not permanent verdicts. The Signature test: contestation tracks value-change measures. It would be refuted if permanent decisions prove stable.'),
        key_points=[
            "Monument controversies forced the governance question.",
            "Options: remove, contextualize, counter-monument, leave.",
            "No democratic theory commands consensus.",
            "Values change; stone does not.",
        ],
        requirements=[
            "Review-process designs.",
            "Contestation-pattern analyses.",
            "Counter-monument evaluations.",
        ],
        standards=[
            "Claims checked against the memory-studies literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Savage K. Standing Soldiers, Kneeling Slaves. Princeton University Press; 1997.",
            "Doss E. Memorial Mania. University of Chicago Press; 2010.",
        ],
        hypotheses=[
            "Periodic review stabilizes monument politics.",
            "Removal is the just answer.",
            "Contextualization suffices.",
            "Monuments should be permanent.",
        ],
        confirm="Contestation tracks value-change measures.",
        refute="Permanent decisions prove stable.",
    ),
    dict(
        key="architecture-20",
        name="Preservation Versus Progress",
        group="Urban",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("When should old buildings be preserved - and when does "
                 "preservation become the enemy of the good city?"),
        background=("Preservation saved treasures and froze cities; "
                    "housing crises blame historic districts for "
                    "shortage. The question: which past deserves "
                    "protection, and who decides? The balance between "
                    "memory and need remains unstruck."),
        why_it_matters=("Preservation shapes what cities can become. The "
                        "balance determines urban futures."),
        sig_lens=("The Signature lens treats preservation as a scarcity "
                  "ledger: the Signature approach asks what protection "
                  "costs."),
        sig_body=("The Signature proposal models preservation as "
                  "costly memory. Assumptions: (1) protection has "
                  "opportunity costs (housing, growth); (2) not all "
                  "old fabric is significant; (3) significance needs "
                  "criteria. Reasoning path: the proposal predicts "
                  "preservation should protect the significant while "
                  "releasing the ordinary - explaining both the "
                  "treasures saved and the housing blocked. The answer "
                  "is then tiered protection, not blanket districts. "
                  "Limits: the model needs better significance "
                  "criteria; the political economy resists tiering."),
        pointer=('The Signature system models preservation as tiered: protect the significant, release the ordinary. The Signature test: outcomes track tiering measures. It would be refuted if blanket protection outperforms tiering.'),
        key_points=[
            "Preservation saved treasures and froze cities.",
            "Housing crises implicate historic districts.",
            "Significance criteria are contested.",
            "The memory-need balance is unstruck.",
        ],
        requirements=[
            "Significance criteria development.",
            "Opportunity-cost quantifications.",
            "Tiered-protection pilots.",
        ],
        standards=[
            "Claims checked against the preservation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Tyler N et al. Historic Preservation. Norton; 2009.",
            "Glaeser EL. Triumph of the City. Penguin; 2011.",
        ],
        hypotheses=[
            "Tiered protection balances memory and need.",
            "Preservation is generally beneficial.",
            "Preservation generally harms cities.",
            "Significance is undefinable.",
        ],
        confirm="Outcomes track tiering measures.",
        refute="Blanket protection outperforms tiering.",
    ),
    dict(
        key="architecture-21",
        name="The Museum Problem",
        group="Practice",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Should museums be iconic objects or quiet backgrounds - "
                 "and does starchitecture serve art?"),
        background=("The Bilbao effect made icons the museum strategy; "
                    "critics argue the building upstages the art and "
                    "that quiet galleries serve better. The evidence on "
                    "visitor experience is mixed. Whether the icon helps "
                    "or harms the mission remains open."),
        why_it_matters=("Museums are architecture's prestige commissions. "
                        "The icon question shapes cultural building."),
        sig_lens=("The Signature lens treats museums as an attention "
                  "ledger: the Signature approach asks what visitors "
                  "remember - the art or the building."),
        sig_body=("The Signature proposal models the icon tradeoff as "
                  "mission-dependent. Assumptions: (1) icons attract "
                  "visitors; (2) strong architecture competes with art "
                  "for attention; (3) missions differ. Reasoning path: "
                  "the proposal predicts icons should suit "
                  "contemporary/experiential missions and harm "
                  "contemplative ones - explaining the mixed evidence. "
                  "The answer is then mission-matched architecture. "
                  "Limits: the model needs better visitor-attention "
                  "studies; the fundraising dimension needs "
                  "acknowledging."),
        pointer=('The Signature system models museum architecture as mission-matched: icons for experiential missions, quiet for contemplative ones. The Signature test: outcomes track mission-fit measures. It would be refuted if iconic museums outperform regardless of mission.'),
        key_points=[
            "The Bilbao effect made icons the strategy.",
            "Critics say buildings upstage art.",
            "Visitor-experience evidence is mixed.",
            "Whether icons serve missions is open.",
        ],
        requirements=[
            "Visitor-attention studies.",
            "Mission-architecture fit analyses.",
            "Fundraising-dimension accounting.",
        ],
        standards=[
            "Claims checked against the museum-architecture literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Foster H. The Art-Architecture Complex. Verso; 2011.",
            "Newhouse V. Towards a New Museum. Monacelli; 1998.",
        ],
        hypotheses=[
            "Mission matching explains the mixed evidence.",
            "Icons always help museums.",
            "Icons always harm art.",
            "The building does not matter much.",
        ],
        confirm="Outcomes track mission-fit measures.",
        refute="Iconic museums outperform regardless of mission.",
    ),
    dict(
        key="architecture-22",
        name="Sacred Space Design",
        group="Design",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("How should sacred spaces be designed in plural "
                 "societies - and can architecture serve the holy "
                 "without doctrine?"),
        background=("Sacred architecture served specific faiths; now "
                    "plural societies need contemplative spaces for "
                    "many or none. Designers find shared elements "
                    "(light, verticality, quiet, procession) but the "
                    "translation from doctrine to design remains craft. "
                    "Whether the sacred is designable remains open."),
        why_it_matters=("Contemplative space is a human need. Its design "
                        "serves plural societies."),
        sig_lens=("The Signature lens treats the sacred as an attention "
                  "ledger: the Signature approach asks what architecture "
                  "does to awareness."),
        sig_body=("The Signature proposal models sacred experience as "
                  "attention-shaped. Assumptions: (1) architecture "
                  "shapes attention (light, scale, quiet); (2) shaped "
                  "attention enables contemplation; (3) the mechanisms "
                  "are shared across traditions. Reasoning path: the "
                  "proposal predicts contemplative effects should "
                  "track attentional design features - which the "
                  "evidence supports. The sacred is then partially "
                  "designable through attention architecture. Limits: "
                  "the model needs better contemplative measures; the "
                  "doctrine question persists."),
        pointer=('The Signature system models sacred experience as attention-shaped: designable through light, scale, quiet, and procession. The Signature test: effects track attentional-design measures. It would be refuted if no design feature predicts contemplative effects.'),
        key_points=[
            "Sacred architecture served specific faiths.",
            "Plural societies need shared contemplative space.",
            "Light, verticality, and quiet recur across traditions.",
            "Whether the sacred is designable is open.",
        ],
        requirements=[
            "Contemplative-effect measures.",
            "Cross-tradition design analyses.",
            "An account of the doctrine dimension.",
        ],
        standards=[
            "Claims checked against the sacred-architecture literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Barrie T. The Sacred In-Between. Routledge; 2010.",
            "Jones L. The Hermeneutics of Sacred Architecture. 2000.",
        ],
        hypotheses=[
            "Attention shaping explains sacred effects.",
            "The sacred needs doctrine.",
            "Shared elements suffice for plural space.",
            "Sacred experience is unmeasurable.",
        ],
        confirm="Effects track attentional-design measures.",
        refute="No design feature predicts contemplative effects.",
    ),
    dict(
        key="architecture-23",
        name="The Kitchen Problem",
        group="Design",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Why is the kitchen architecture's most contested room - "
                 "and what does it reveal about design and domestic "
                 "life?"),
        background=("The kitchen moved from hidden service to open "
                    "showpiece; the Frankfurt Kitchen rationalized it, "
                    "open plans dissolved it. Feminist critics note the "
                    "kitchen's gendered history. Whether the open "
                    "kitchen serves cooking or status remains debated."),
        why_it_matters=("Kitchens shape domestic life daily. Their design "
                        "is lived architecture."),
        sig_lens=("The Signature lens treats kitchens as a labor ledger: "
                  "the Signature approach asks whose work the design "
                  "serves."),
        sig_body=("The Signature proposal models kitchen design as "
                  "labor-visible. Assumptions: (1) kitchen layouts "
                  "encode who cooks; (2) open kitchens display labor "
                  "as lifestyle; (3) the ergonomics matter "
                  "independently. Reasoning path: the proposal predicts "
                  "satisfaction should track ergonomic fit more than "
                  "openness fashion - which the evidence supports. "
                  "Design for the cook, not the photograph. Limits: "
                  "the model needs better ergonomic studies; the "
                  "gender history needs honoring."),
        pointer=('The Signature system models kitchen quality as ergonomic: design for the cook, not the photograph. The Signature test: satisfaction tracks ergonomic measures. It would be refuted if openness predicts satisfaction best.'),
        key_points=[
            "Kitchens moved from hidden to showpiece.",
            "The Frankfurt Kitchen rationalized domestic labor.",
            "Open plans dissolved kitchen boundaries.",
            "The gendered history complicates the story.",
        ],
        requirements=[
            "Ergonomic-fit studies.",
            "Open-versus-closed outcome comparisons.",
            "Gender-history integration.",
        ],
        standards=[
            "Claims checked against the domestic-architecture literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hayden D. The Grand Domestic Revolution. MIT Press; 1981.",
            "Cieraad I. At Home: An Anthropology of Domestic Space. Syracuse University Press; 1999.",
        ],
        hypotheses=[
            "Ergonomic fit explains satisfaction.",
            "Open kitchens serve status, not cooking.",
            "The Frankfurt model remains optimal.",
            "Cultural variation dominates.",
        ],
        confirm="Satisfaction tracks ergonomic measures.",
        refute="Openness predicts satisfaction best.",
    ),
    dict(
        key="architecture-24",
        name="Parametricism: The Promise",
        group="Styles",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Did parametricism deliver a new architectural paradigm - "
                 "or just expensive curves?"),
        background=("Schumacher proclaimed parametricism the new style; "
                    "critics saw formal indulgence enabled by software. "
                    "The achievements (complex geometries buildable) are "
                    "real; the urban and social contributions are "
                    "thinner. Whether the paradigm claim holds remains "
                    "open."),
        why_it_matters=("Parametricism shaped two decades of practice. "
                        "Its verdict guides digital design's future."),
        sig_lens=("The Signature lens treats parametricism as a tool "
                  "ledger: the Signature approach asks what the tools "
                  "enabled versus what the style claimed."),
        sig_body=("The Signature proposal models parametricism as "
                  "tool-real, paradigm-thin. Assumptions: (1) the "
                  "tools genuinely expanded buildable geometry; (2) "
                  "the style claims exceeded the tools; (3) the "
                  "urban contribution lagged. Reasoning path: the "
                  "proposal predicts the lasting value should be "
                  "technical (fabrication, optimization) not stylistic "
                  "- which matches practice's evolution. Keep the "
                  "tools, retire the manifesto. Limits: the model "
                  "needs better contribution analyses; the "
                  "sustainability uses need developing."),
        pointer=('The Signature system models parametricism as tool-real but paradigm-thin: keep the tools, retire the manifesto. The Signature test: value concentrates in technical applications. It would be refuted if parametric urbanism proves successful.'),
        key_points=[
            "Parametricism was proclaimed the new paradigm.",
            "Complex geometries became buildable.",
            "Urban and social contributions are thin.",
            "Whether the paradigm claim holds is open.",
        ],
        requirements=[
            "Contribution analyses by dimension.",
            "Fabrication-advance documentation.",
            "Sustainability-application studies.",
        ],
        standards=[
            "Claims checked against the digital-architecture literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Schumacher P. The Autopoiesis of Architecture. Wiley; 2011.",
            "Carpo M. The Alphabet and the Algorithm. MIT Press; 2011.",
        ],
        hypotheses=[
            "Tool-real-paradigm-thin explains the record.",
            "Parametricism is a genuine paradigm.",
            "It was mere formal indulgence.",
            "The tools will redeem the style.",
        ],
        confirm="Value concentrates in technical applications.",
        refute="Parametric urbanism proves successful.",
    ),
    dict(
        key="architecture-25",
        name="Biomimicry in Architecture",
        group="Design",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("Can biomimicry move beyond metaphor - from termite-mound "
                 "imagery to genuine biological design principles?"),
        background=("Biomimetic claims are often skin-deep (a facade "
                    "like a leaf); genuine transfers (passive cooling "
                    "principles, material efficiency) are rarer. The "
                    "question: whether biology offers architecture "
                    "real design principles or just inspiration images."),
        why_it_matters=("Biology solved design problems over eons. Real "
                        "transfer could transform building."),
        sig_lens=("The Signature lens treats biomimicry as a transfer "
                  "ledger: the Signature approach asks what actually "
                  "transfers."),
        sig_body=("The Signature proposal models biomimicry as "
                  "principle-transferable, form-misleading. Assumptions: "
                  "(1) biological forms serve biological functions; (2) "
                  "the principles (not forms) transfer; (3) "
                  "metaphorical use dominates. Reasoning path: the "
                  "proposal predicts successful cases should apply "
                  "principles (thermoregulation, structural efficiency) "
                  "- which they do. The discipline is then real but "
                  "demanding: understand the biology deeply. Limits: "
                  "the model needs better transfer case studies; the "
                  "metaphor problem needs policing."),
        pointer=('The Signature system models biomimicry as principle-transfer: understand the biology deeply, copy principles not forms. The Signature test: success tracks principle-depth measures. It would be refuted if form-copying performs equally well.'),
        key_points=[
            "Biomimetic claims are often skin-deep.",
            "Genuine principle transfers are rarer.",
            "Form copying misleads; principle transfer works.",
            "Whether biology offers real principles is the question.",
        ],
        requirements=[
            "Transfer case-study documentation.",
            "Principle-versus-form analyses.",
            "Deep-biology collaboration models.",
        ],
        standards=[
            "Claims checked against the biomimicry literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Benyus JM. Biomimicry. William Morrow; 1997.",
            "Pawlyn M. Biomimicry in Architecture. RIBA; 2011.",
        ],
        hypotheses=[
            "Principle transfer captures the real value.",
            "Biomimicry is mostly metaphor.",
            "Biology offers a full design paradigm.",
            "The transfers are coincidental.",
        ],
        confirm="Success tracks principle-depth measures.",
        refute="Form-copying performs equally well.",
    ),
    dict(
        key="architecture-26",
        name="The Carbon Problem in Building",
        group="Practice",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("How can construction - responsible for nearly 40 percent "
                 "of emissions - decarbonize without stopping building?"),
        background=("Embodied carbon (materials) and operational carbon "
                    "(energy use) both matter; concrete and steel "
                    "dominate the former. Solutions exist (mass timber, "
                    "low-carbon concrete, passive design) but scale "
                    "slowly. Whether the industry can transform in time "
                    "remains the open question."),
        why_it_matters=("Buildings are a huge emissions share. "
                        "Decarbonizing construction is climate-critical."),
        sig_lens=("The Signature lens treats carbon as a lifecycle "
                  "ledger: the Signature approach asks where the "
                  "emissions actually sit."),
        sig_body=("The Signature proposal models building carbon as "
                  "lifecycle-distributed. Assumptions: (1) embodied "
                  "and operational both matter; (2) the balance shifts "
                  "as grids clean; (3) materials are the hard part. "
                  "Reasoning path: the proposal predicts priorities "
                  "should shift from operational to embodied as grids "
                  "decarbonize - which leading practice does. The "
                  "transformation needs material innovation plus "
                  "adaptive reuse (the greenest building is existing). "
                  "Limits: the model needs better lifecycle data; the "
                  "scale-up economics need solving."),
        pointer=('The Signature system models building carbon as lifecycle-distributed: shift focus to embodied carbon and adaptive reuse as grids clean. The Signature test: priorities track grid-carbon measures. It would be refuted if embodied carbon proves negligible.'),
        key_points=[
            "Construction is nearly 40 percent of emissions.",
            "Embodied and operational carbon both matter.",
            "Low-carbon solutions exist but scale slowly.",
            "Whether transformation is fast enough is open.",
        ],
        requirements=[
            "Lifecycle carbon databases.",
            "Material-innovation scaling studies.",
            "Reuse-versus-rebuild analyses.",
        ],
        standards=[
            "Claims checked against the green-building literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "IEA. Buildings: tracking report. 2023.",
            "Pomponi F, Moncaster A. Embodied carbon. 2017.",
        ],
        hypotheses=[
            "Lifecycle shifting guides priorities correctly.",
            "Operational carbon remains primary.",
            "Material innovation will suffice.",
            "Only reduced building works.",
        ],
        confirm="Priorities track grid-carbon measures.",
        refute="Embodied carbon proves negligible.",
    ),
    dict(
        key="architecture-27",
        name="Architecture and Climate Adaptation",
        group="Practice",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("How should architecture adapt to the climate already "
                 "changing - heat, flood, fire, and storm?"),
        background=("Design assumed stable climate; now heat waves, "
                    "floods, and fires demand resilient design. "
                    "Vernacular traditions offer passive-cooling wisdom "
                    "(see architecture-15); modern codes lag. Whether "
                    "adaptation can keep buildings habitable remains "
                    "open."),
        why_it_matters=("Climate adaptation is survival design. "
                        "Architecture's response protects lives."),
        sig_lens=("The Signature lens treats adaptation as a hazard "
                  "ledger: the Signature approach asks which threats "
                  "each place faces."),
        sig_body=("The Signature proposal models adaptation as "
                  "hazard-specific. Assumptions: (1) threats vary by "
                  "place (heat, flood, fire); (2) design responses "
                  "differ; (3) codes assume the past. Reasoning path: "
                  "the proposal predicts resilient design should be "
                  "place-hazard matched - explaining why generic "
                  "green building misses adaptation. The answer is "
                  "then hazard-led design plus code reform. Limits: "
                  "the model needs better hazard-projection data; "
                  "the equity dimension (who gets protection) needs "
                  "centering."),
        pointer=('The Signature system models climate adaptation as hazard-specific: place-matched resilient design plus code reform. The Signature test: resilience tracks hazard matching. It would be refuted if generic designs adapt equally well.'),
        key_points=[
            "Design assumed a stable climate.",
            "Heat, flood, fire, and storm demand responses.",
            "Vernacular traditions offer passive wisdom.",
            "Codes lag the changing reality.",
        ],
        requirements=[
            "Hazard-projection design data.",
            "Place-matched resilient prototypes.",
            "Equity-centered adaptation analyses.",
        ],
        standards=[
            "Claims checked against the resilience literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "IPCC. Climate Change: Impacts, Adaptation and Vulnerability. 2022.",
            "Roaf S et al. Adapting Buildings and Cities for Climate Change. Routledge; 2009.",
        ],
        hypotheses=[
            "Hazard specificity guides adaptation.",
            "Generic resilience suffices.",
            "Vernacular revival is the answer.",
            "Technology will protect regardless.",
        ],
        confirm="Resilience tracks hazard matching.",
        refute="Generic designs adapt equally well.",
    ),
    dict(
        key="architecture-28",
        name="The Smart Building Problem",
        group="Practice",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Do smart buildings serve occupants - or do the sensors "
                 "serve the building's owners?"),
        background=("Smart systems promise efficiency and comfort; "
                    "occupants report frustration (uncontrollable "
                    "environments) and surveillance concerns. The "
                    "performance gap (designed versus actual energy) "
                    "persists. Whether intelligence serves inhabitants "
                    "remains open."),
        why_it_matters=("Smart buildings are the industry's future. "
                        "Their occupant effects determine its value."),
        sig_lens=("The Signature lens treats smartness as a control "
                  "ledger: the Signature approach asks who controls "
                  "the environment."),
        sig_body=("The Signature proposal models smart-building success "
                  "as occupant-control dependent. Assumptions: (1) "
                  "comfort needs perceived control; (2) automation "
                  "removes it; (3) the efficiency gains are real but "
                  "secondary. Reasoning path: the proposal predicts "
                  "satisfaction should track occupant override "
                  "capability - which the evidence supports. Smart "
                  "buildings should then be occupant-governed, not "
                  "algorithm-governed. Limits: the model needs better "
                  "control-satisfaction studies; the privacy dimension "
                  "needs addressing."),
        pointer=('The Signature system models smart buildings as occupant-governed: preserve override capability or lose satisfaction. The Signature test: satisfaction tracks override measures. It would be refuted if full automation satisfies most.'),
        key_points=[
            "Smart systems promise efficiency and comfort.",
            "Occupants report frustration and surveillance concerns.",
            "The performance gap persists.",
            "Whether intelligence serves inhabitants is open.",
        ],
        requirements=[
            "Override-capability studies.",
            "Privacy-impact analyses.",
            "Performance-gap investigations.",
        ],
        standards=[
            "Claims checked against the smart-buildings literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ghaffarianhoseini A et al. Intelligent buildings. 2016.",
            "Leaman A, Bordass B. Assessing building performance. 2007.",
        ],
        hypotheses=[
            "Occupant control explains satisfaction patterns.",
            "Automation maximizes comfort.",
            "Smart buildings are net negative.",
            "The problems are transitional.",
        ],
        confirm="Satisfaction tracks override measures.",
        refute="Full automation satisfies most.",
    ),
    dict(
        key="architecture-29",
        name="Designing for Neurodiversity",
        group="Design",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("How should architecture serve neurodiverse occupants - "
                 "and what does it teach about design for all?"),
        background=("Sensory environments overwhelm many autistic "
                    "people; ADHD, dyslexia, and other differences also "
                    "interact with space. Pioneering projects (sensory "
                    "design for schools) show promise. Whether "
                    "neurodiversity needs separate standards or "
                    "universal sensory design remains open."),
        why_it_matters=("Neurodiverse people inhabit every building. "
                        "Inclusive sensory design serves everyone."),
        sig_lens=("The Signature lens treats sensory design as a "
                  "gradient ledger: the Signature approach asks where "
                  "the overwhelm threshold sits."),
        sig_body=("The Signature proposal models sensory needs as "
                  "gradients, not categories. Assumptions: (1) "
                  "sensory sensitivity varies continuously; (2) "
                  "overwhelming environments harm many; (3) choice "
                  "and retreat help. Reasoning path: the proposal "
                  "predicts universal sensory design (quiet rooms, "
                  "adjustable stimuli, clear wayfinding) should help "
                  "broadly - which early evidence supports. "
                  "Neurodiversity then extends universal design's "
                  "logic to the senses. Limits: the model needs "
                  "better sensory-outcome studies; the "
                  "individual variation needs honoring."),
        pointer=('The Signature system models sensory needs as gradients: universal sensory design with choice and retreat serves all. The Signature test: outcomes track sensory-gradient measures. It would be refuted if categorical standards outperform universal design.'),
        key_points=[
            "Sensory environments overwhelm many neurodiverse people.",
            "Pioneering sensory-design projects show promise.",
            "Sensitivity varies continuously.",
            "Separate standards versus universal design is the question.",
        ],
        requirements=[
            "Sensory-outcome studies.",
            "Universal-design evaluations.",
            "Individual-variation accommodation research.",
        ],
        standards=[
            "Claims checked against the inclusive-design literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mostafa M. An architecture for autism. 2014.",
            "Heylighen A, Herssens J. Designing for diverse minds. 2014.",
        ],
        hypotheses=[
            "Gradient-universal design serves best.",
            "Separate standards are needed.",
            "Current accessibility covers it.",
            "The needs are too individual for design.",
        ],
        confirm="Outcomes track sensory-gradient measures.",
        refute="Categorical standards outperform universal design.",
    ),
    dict(
        key="architecture-30",
        name="The Aging Building Stock",
        group="Urban",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("What should happen to the aging building stock - "
                 "retrofit, replace, or manage decline?"),
        background=("Most future buildings already exist; they are "
                    "energy-inefficient and often unloved. Retrofit "
                    "scales slowly (cost, disruption); replacement "
                    "wastes embodied carbon. The triage - which "
                    "buildings deserve investment - lacks frameworks."),
        why_it_matters=("The existing stock is the climate and housing "
                        "opportunity. Its fate shapes cities' futures."),
        sig_lens=("The Signature lens treats the stock as a triage "
                  "ledger: the Signature approach asks which buildings "
                  "repay investment."),
        sig_body=("The Signature proposal models stock decisions as "
                  "triage by potential. Assumptions: (1) retrofit "
                  "potential varies (structure, location); (2) "
                  "embodied carbon favors retention; (3) some stock "
                  "is beyond saving. Reasoning path: the proposal "
                  "predicts optimal strategies should sort buildings "
                  "by retrofit potential - explaining why blanket "
                  "policies misfire. The greenest building is the "
                  "one already built, where it can be saved. Limits: "
                  "the model needs better potential assessments; the "
                  "financing mechanisms need inventing."),
        pointer=('The Signature system models stock decisions as triage: sort by retrofit potential; the greenest building is the existing one worth saving. The Signature test: outcomes track potential-sorted strategies. It would be refuted if uniform policies outperform triage.'),
        key_points=[
            "Most future buildings already exist.",
            "Retrofit scales slowly; replacement wastes carbon.",
            "Triage frameworks are lacking.",
            "The existing stock is the opportunity.",
        ],
        requirements=[
            "Retrofit-potential assessments.",
            "Triage framework development.",
            "Financing-mechanism innovation.",
        ],
        standards=[
            "Claims checked against the retrofit literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Brand S. How Buildings Learn. Viking; 1994.",
            "Webb AL. Energy retrofits. 2017.",
        ],
        hypotheses=[
            "Potential-based triage optimizes outcomes.",
            "Blanket retrofit mandates work.",
            "Replacement is generally better.",
            "The stock will manage itself.",
        ],
        confirm="Outcomes track potential-sorted strategies.",
        refute="Uniform policies outperform triage.",
    ),
    dict(
        key="architecture-31",
        name="Informal Settlements: The Design Response",
        group="Urban",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("How should architecture respond to informal settlements - "
                 "upgrade, replace, or learn from them?"),
        background=("A billion people live in informal settlements; "
                    "architects oscillate between upgrading (in-situ "
                    "improvement) and clearance. The settlements show "
                    "remarkable adaptive intelligence (incremental "
                    "building, social networks). Whether formal "
                    "architecture can help without destroying remains "
                    "open."),
        why_it_matters=("Informal urbanism houses a seventh of humanity. "
                        "The design response affects a billion lives."),
        sig_lens=("The Signature lens treats informality as an "
                  "intelligence ledger: the Signature approach asks "
                  "what the settlements do right."),
        sig_body=("The Signature proposal models informal settlements "
                  "as adaptive systems. Assumptions: (1) incremental "
                  "building matches incomes; (2) social networks "
                  "substitute for services; (3) clearance destroys "
                  "both. Reasoning path: the proposal predicts "
                  "in-situ upgrading should outperform clearance - "
                  "which the evidence supports. Architects should "
                  "then enable incrementality (sites, services, "
                  "technical aid) not impose finished form. Limits: "
                  "the model needs better upgrading evaluations; the "
                  "land-tenure question dominates."),
        pointer=('The Signature system models informal settlements as adaptive: enable incrementality through upgrading, not clearance. The Signature test: outcomes track incrementality support. It would be refuted if clearance outperforms upgrading.'),
        key_points=[
            "A billion people live in informal settlements.",
            "Upgrading outperforms clearance in evidence.",
            "Incremental building matches incomes.",
            "Whether formal architecture can help is open.",
        ],
        requirements=[
            "Upgrading outcome evaluations.",
            "Incrementality-enabling design research.",
            "Land-tenure analyses.",
        ],
        standards=[
            "Claims checked against the informal-urbanism literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Turner JFC. Housing by People. Marion Boyars; 1976.",
            "Dovey K et al. Atlas of Informal Settlement. 2020.",
        ],
        hypotheses=[
            "Adaptive-systems framing guides good responses.",
            "Clearance and replacement work better.",
            "Architects should stay out.",
            "Upgrading needs land tenure first.",
        ],
        confirm="Outcomes track incrementality support.",
        refute="Clearance outperforms upgrading.",
    ),
    dict(
        key="architecture-32",
        name="Architecture After Capitalism",
        group="Theory",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("What would architecture be after capitalism - and does "
                 "the question even make sense?"),
        background=("Architecture serves markets (developers, "
                    "speculation); critics imagine post-capitalist "
                    "building (commons, decommodified housing). The "
                    "question tests whether architectural form follows "
                    "economic form - and what alternatives are "
                    "thinkable."),
        why_it_matters=("The thought experiment reveals architecture's "
                        "economic dependencies. Its answers inform "
                        "reform."),
        sig_lens=("The Signature lens treats the question as a "
                  "dependency ledger: the Signature approach asks what "
                  "capitalism provides architecture."),
        sig_body=("The Signature proposal models the dependency as "
                  "financing-plus-demand. Assumptions: (1) capitalism "
                  "finances most building; (2) it shapes demand "
                  "(speculation, luxury); (3) alternatives exist "
                  "partially (co-ops, public housing). Reasoning path: "
                  "the proposal shows post-capitalist architecture "
                  "already exists at the margins - predicting that "
                  "scaling it needs financing innovation, not design "
                  "innovation. The question is then economic, not "
                  "architectural. Limits: the model needs better "
                  "alternative-financing studies; the speculation "
                  "question is political."),
        pointer=('The Signature system models post-capitalist architecture as a financing question: alternatives exist at the margins; scaling needs capital innovation. The Signature test: alternative projects track financing innovation. It would be refuted if design innovation alone scales alternatives.'),
        key_points=[
            "Architecture serves markets and speculation.",
            "Post-capitalist alternatives exist at the margins.",
            "The question tests form's economic dependence.",
            "Whether the question makes sense is debated.",
        ],
        requirements=[
            "Alternative-financing case studies.",
            "Dependency analyses.",
            "Reform-path development.",
        ],
        standards=[
            "Claims checked against the political-economy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Harvey D. Rebel Cities. Verso; 2012.",
            "Deamer P. Architecture and Capitalism. Routledge; 2013.",
        ],
        hypotheses=[
            "Financing, not design, is the binding constraint.",
            "Architecture transcends economic systems.",
            "Post-capitalist building is unimaginable.",
            "Reform within capitalism suffices.",
        ],
        confirm="Alternative projects track financing innovation.",
        refute="Design innovation alone scales alternatives.",
    ),
    dict(
        key="architecture-33",
        name="The Authorship Problem",
        group="Theory",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("Who authors a building - the starchitect, the team, the "
                 "client, or the users who remake it?"),
        background=("Star architects sign buildings teams design for "
                    "clients who constrain them, then users transform "
                    "them (Brand's shearing layers). The authorship "
                    "myth serves marketing but misdescribes production. "
                    "Whether architecture needs authors remains open."),
        why_it_matters=("Authorship shapes credit, liability, and "
                        "education. Its truth reforms the profession."),
        sig_lens=("The Signature lens treats authorship as a credit "
                  "ledger: the Signature approach asks who did what."),
        sig_body=("The Signature proposal models building production "
                  "as collective. Assumptions: (1) many hands shape "
                  "every building; (2) the star system credits one; "
                  "(3) users continue authoring after occupancy. "
                  "Reasoning path: the proposal shows the single "
                  "author is marketing fiction - predicting that "
                  "credit reform (team recognition, user "
                  "acknowledgment) would change practice incentives. "
                  "Architecture is then inherently co-authored. Limits: "
                  "the model needs better production ethnographies; "
                  "the liability question needs the fiction."),
        pointer=('The Signature system models buildings as co-authored: reform credit toward teams and users, retire the single-author myth. The Signature test: production studies show distributed authorship. It would be refuted if single architects drive outcomes.'),
        key_points=[
            "Star architects sign team-designed buildings.",
            "Clients constrain; users transform.",
            "The authorship myth serves marketing.",
            "Whether architecture needs authors is open.",
        ],
        requirements=[
            "Production ethnographies.",
            "Credit-reform experiments.",
            "Liability-framework analyses.",
        ],
        standards=[
            "Claims checked against the profession literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Brand S. How Buildings Learn. Viking; 1994.",
            "Cuff D. Architecture: The Story of Practice. MIT Press; 1991.",
        ],
        hypotheses=[
            "Collective production describes reality.",
            "Single authorship is necessary fiction.",
            "Users are the true authors.",
            "Authorship does not matter.",
        ],
        confirm="Production studies show distributed authorship.",
        refute="Single architects drive outcomes.",
    ),
    dict(
        key="architecture-34",
        name="A Unified Theory of Architecture",
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can architectural theory unify - art, science, craft, "
                 "and social practice - into one account of building?"),
        background=("Each tradition captures something: art the "
                    "expression, science the performance, craft the "
                    "making, sociology the inhabitation. Unification "
                    "attempts remain programmatic. Whether building's "
                    "nature permits one theory is the discipline's "
                    "capstone question."),
        why_it_matters=("This is architecture's capstone: the answer "
                        "determines what architecture is."),
        sig_lens=("The Signature lens treats the traditions as a phase "
                  "ledger: the Signature approach asks what phase of "
                  "building each tradition owns."),
        sig_body=("The Signature proposal models unification as "
                  "phase-integration. Assumptions: (1) building spans "
                  "imagining, making, performing, and inhabiting; (2) "
                  "each tradition owns a phase; (3) phases interact. "
                  "Reasoning path: the proposal assigns art to "
                  "imagining, craft to making, science to performing, "
                  "sociology to inhabiting - with the building's life "
                  "as the integrator. Unity comes from the building "
                  "that holds the phases together, not one "
                  "tradition's victory. Limits: the integration is "
                  "sketched; partisans may reject the settlement."),
        pointer=("The Signature system assigns each tradition its phase of building, with the building's life as the integrator. The Signature test: integrated models predict across phases. It would be refuted if phases prove irreducible to common theory."),
        key_points=[
            "Four traditions offer incompatible images of architecture.",
            "Each captures what the others miss.",
            "Unification attempts remain programmatic.",
            "Whether one theory is possible is foundational.",
        ],
        requirements=[
            "A phase architecture for the traditions.",
            "An account of phase interaction.",
            "Testable implications of the integration.",
        ],
        standards=[
            "Claims checked against the architectural-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Vitruvius. De Architectura. 1st century BCE.",
            "Forty A. Words and Buildings. Thames and Hudson; 2000.",
        ],
        hypotheses=[
            "Phase-integration unifies architectural theory.",
            "The traditions are incommensurable.",
            "One tradition will absorb the rest.",
            "Pluralism is permanent.",
        ],
        confirm="Integrated models predict across phases.",
        refute="Phases prove irreducible to common theory.",
    ),
]
