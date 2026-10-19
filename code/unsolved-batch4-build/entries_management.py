#!/usr/bin/env python3
"""Entries for the Unsolved Management databases (batch 4).

34 famous open problems in management, ladder-ordered by accessibility.
ID prefixes: JAH-USMG- (public) and JAH-USMGS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="management-01",
        name="Why Do Firms Exist",
        group="Organizations",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Why do firms exist at all - why is production organized "
                 "in hierarchies rather than pure markets?"),
        background=("Coase's 1937 question founded the theory of the firm: "
                    "transaction costs make markets expensive, so "
                    "hierarchies emerge. Later theories added property "
                    "rights, capabilities, and knowledge. Yet the "
                    "boundary - what belongs inside versus outside the "
                    "firm - keeps shifting with technology."),
        why_it_matters=("The firm-market boundary shapes the economy. Its "
                        "theory determines what organizations should do."),
        sig_lens=("The Signature lens treats the firm as a cost ledger: "
                  "the Signature approach asks what hierarchies save."),
        sig_body=("The Signature proposal models firm boundaries as "
                  "transaction-cost plus capability. Assumptions: (1) "
                  "markets cost (search, bargaining, enforcement); (2) "
                  "hierarchies cost (bureaucracy, agency); (3) "
                  "capabilities are sticky. Reasoning path: the proposal "
                  "predicts activities should internalize where "
                  "transaction costs exceed hierarchy costs - explaining "
                  "outsourcing waves as cost shifts. Digital platforms "
                  "then redraw the boundary again. Limits: the model "
                  "needs better transaction-cost measures; the "
                  "capability view needs integration."),
        pointer=('The Signature system models firm boundaries as transaction-cost plus capability, redrawn by each technology wave. The Signature test: boundaries track cost-capability measures. It would be refuted if boundaries ignore transaction costs.'),
        key_points=[
            "Coase founded the theory with transaction costs.",
            "Property-rights and capability theories followed.",
            "The boundary keeps shifting with technology.",
            "Outsourcing waves reflect cost shifts.",
        ],
        requirements=[
            "Transaction-cost measures by activity.",
            "Boundary-shift case studies.",
            "Capability-theory integration.",
        ],
        standards=[
            "Claims checked against the theory-of-the-firm literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Coase RH. The nature of the firm. Economica; 1937.",
            "Williamson OE. Markets and Hierarchies. Free Press; 1975.",
        ],
        hypotheses=[
            "Cost-plus-capability explains boundaries.",
            "Transaction costs alone suffice.",
            "Capabilities alone suffice.",
            "The question is obsolete for platforms.",
        ],
        confirm="Boundaries track cost-capability measures.",
        refute="Boundaries ignore transaction costs.",
    ),
    dict(
        key="management-02",
        name="The Principal-Agent Problem",
        group="Organizations",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("How can owners ensure managers act for them - and is the "
                 "agency problem solvable or inherent?"),
        background=("Berle and Means separated ownership from control; "
                    "Jensen and Meckling formalized agency costs. "
                    "Solutions - boards, incentives, takeovers - help but "
                    "never eliminate the gap: agents know more than "
                    "principals. Whether the problem is manageable or "
                    "inherent remains the field's core tension."),
        why_it_matters=("Agency costs shape every corporation. Their "
                        "manageability determines governance design."),
        sig_lens=("The Signature lens treats agency as an information "
                  "ledger: the Signature approach asks what principals "
                  "cannot see."),
        sig_body=("The Signature proposal models agency as "
                  "information-asymmetry with partial remedies. "
                  "Assumptions: (1) agents hold private information; "
                  "(2) monitoring is costly; (3) incentives distort. "
                  "Reasoning path: the proposal predicts no remedy "
                  "fully closes the gap - each (boards, pay, takeovers) "
                  "trades one cost for another - making residual "
                  "agency costs inherent. Governance is then cost-"
                  "minimization, not problem-solving. Limits: the "
                  "model needs better residual-cost measures; "
                  "cultural remedies need study."),
        pointer=('The Signature system models agency costs as inherent: governance minimizes, never eliminates, the gap. The Signature test: residual costs persist across remedies. It would be refuted if some remedy eliminates the gap.'),
        key_points=[
            "Ownership separated from control in modern corporations.",
            "Boards, incentives, and takeovers are partial remedies.",
            "Each remedy trades one cost for another.",
            "Whether the problem is solvable is the core tension.",
        ],
        requirements=[
            "Residual agency-cost measures.",
            "Remedy tradeoff analyses.",
            "Cultural-remedy studies.",
        ],
        standards=[
            "Claims checked against the agency literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Jensen MC, Meckling WH. Theory of the firm: managerial behavior, agency costs. 1976.",
            "Berle AA, Means GC. The Modern Corporation and Private Property. 1932.",
        ],
        hypotheses=[
            "Residual costs are inherent.",
            "Better incentives can solve agency.",
            "Boards can solve it with reform.",
            "Takeover markets discipline adequately.",
        ],
        confirm="Residual costs persist across remedies.",
        refute="Some remedy eliminates the gap.",
    ),
    dict(
        key="management-03",
        name="What Makes Teams Work",
        group="Leadership",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("What makes some teams brilliant and others dysfunctional - "
                 "and can team effectiveness be engineered?"),
        background=("Google's Project Aristotle found psychological safety "
                    "mattered most; research adds clear goals, "
                    "interdependence, and composition. But the findings "
                    "are correlational, the mechanisms fuzzy, and "
                    "interventions to build safety show mixed results. "
                    "Whether effectiveness can be engineered remains "
                    "open."),
        why_it_matters=("Teams do the work of organizations. Their "
                        "effectiveness is management's central question."),
        sig_lens=("The Signature lens treats teams as a safety ledger: "
                  "the Signature approach asks what lets members risk "
                  "speaking up."),
        sig_body=("The Signature proposal models team effectiveness as "
                  "safety-enabled coordination. Assumptions: (1) complex "
                  "work needs candid information; (2) candor needs "
                  "safety; (3) safety is built by leader behavior. "
                  "Reasoning path: the proposal predicts safety should "
                  "mediate the leader-to-performance link - which the "
                  "evidence supports. Engineering effectiveness then "
                  "means training leaders to build safety, not "
                  "selecting for composition. Limits: the model needs "
                  "better safety interventions; the causality needs "
                  "tighter tests."),
        pointer=('The Signature system models team effectiveness as safety-enabled coordination, built by leader behavior. The Signature test: safety mediates leader-to-performance links. It would be refuted if safety shows no causal effect.'),
        key_points=[
            "Psychological safety emerged as the top predictor.",
            "Clear goals and interdependence also matter.",
            "Findings are largely correlational.",
            "Safety-building interventions are mixed.",
        ],
        requirements=[
            "Causal tests of safety interventions.",
            "Leader-behavior measures.",
            "Composition-versus-process decomposition.",
        ],
        standards=[
            "Claims checked against the teams literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Edmondson A. Psychological safety and learning behavior in work teams. 1999.",
            "Duhigg C. What Google learned from its quest to build the perfect team. 2016.",
        ],
        hypotheses=[
            "Safety-enabled coordination explains effectiveness.",
            "Composition determines outcomes.",
            "Safety cannot be engineered.",
            "Task design dominates team factors.",
        ],
        confirm="Safety mediates leader-to-performance links.",
        refute="Safety shows no causal effect.",
    ),
    dict(
        key="management-04",
        name="Leadership Versus Management",
        group="Leadership",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Is leadership distinct from management - or is the "
                 "distinction a rhetorical invention?"),
        background=("Kotter, Bennis, and Zaleznik drew the line: managers "
                    "cope with complexity, leaders with change. Critics "
                    "reply the distinction romanticizes leadership and "
                    "that the same people do both. Whether the "
                    "constructs are separable - and measurably so - "
                    "remains debated."),
        why_it_matters=("The distinction shapes training, selection, and "
                        "billions in leadership development. Its reality "
                        "determines the industry's value."),
        sig_lens=("The Signature lens treats the distinction as a "
                  "behavior ledger: the Signature approach asks what "
                  "leaders do that managers do not."),
        sig_body=("The Signature proposal models leadership and "
                  "management as roles, not persons. Assumptions: (1) "
                  "organizations need both stability and change; (2) "
                  "the behaviors differ (planning versus vision); (3) "
                  "individuals blend them. Reasoning path: the proposal "
                  "predicts the distinction should hold at the "
                  "behavioral level but dissolve at the person level - "
                  "which the evidence supports. The industry's error is "
                  "then personifying roles. Limits: the model needs "
                  "better behavioral measures; the development "
                  "implications need working out."),
        pointer=('The Signature system models leadership and management as roles, not persons: the distinction holds behaviorally, dissolves personally. The Signature test: behaviors separate; persons blend. It would be refuted if no behavioral separation is found.'),
        key_points=[
            "Kotter and Bennis drew the classic distinction.",
            "Critics call it romanticized rhetoric.",
            "The same people typically do both.",
            "Billions ride on leadership development.",
        ],
        requirements=[
            "Behavioral measures separating the roles.",
            "Person-level blending studies.",
            "Development-outcome evaluations.",
        ],
        standards=[
            "Claims checked against the leadership literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kotter JP. What leaders really do. Harvard Business Review; 1990.",
            "Mintzberg H. Managing. Berrett-Koehler; 2009.",
        ],
        hypotheses=[
            "Role-not-person resolves the debate.",
            "Leadership is distinct and measurable.",
            "The distinction is empty rhetoric.",
            "Context determines which is needed.",
        ],
        confirm="Behaviors separate; persons blend.",
        refute="No behavioral separation is found.",
    ),
    dict(
        key="management-05",
        name="Motivation: What Drives Workers",
        group="People",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("What really motivates workers - money, meaning, mastery, "
                 "autonomy - and in what mix?"),
        background=("Taylor bet on money; Mayo on belonging; Herzberg on "
                    "the work itself; Deci and Ryan on autonomy, mastery, "
                    "purpose. The evidence: extrinsic rewards work for "
                    "routine tasks but can crowd out intrinsic motivation "
                    "for creative work. The optimal mix by task and person "
                    "remains the open design question."),
        why_it_matters=("Motivation design shapes every job. The mix "
                        "determines performance and well-being."),
        sig_lens=("The Signature lens treats motivation as a crowding "
                  "ledger: the Signature approach asks when rewards help "
                  "and when they harm."),
        sig_body=("The Signature proposal models motivation as "
                  "task-contingent. Assumptions: (1) routine tasks need "
                  "extrinsic structure; (2) creative tasks need "
                  "intrinsic drive; (3) rewards can crowd out the "
                  "intrinsic. Reasoning path: the proposal predicts "
                  "pay-for-performance should work for routine work and "
                  "backfire for creative work - which the evidence "
                  "supports. The design rule is then match rewards to "
                  "task type. Limits: the model needs better task "
                  "typing; individual differences need integration."),
        pointer=('The Signature system models motivation as task-contingent: match rewards to task type, with crowding-out as the key risk. The Signature test: reward effects reverse by task type. It would be refuted if one reward scheme works across tasks.'),
        key_points=[
            "Extrinsic rewards work for routine tasks.",
            "They can crowd out intrinsic motivation for creative work.",
            "Autonomy, mastery, and purpose drive knowledge workers.",
            "The optimal mix remains the design question.",
        ],
        requirements=[
            "Task-typing frameworks.",
            "Crowding-out boundary studies.",
            "Individual-difference integration.",
        ],
        standards=[
            "Claims checked against the motivation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Deci EL et al. A meta-analytic review of experiments examining the effects of extrinsic rewards. 1999.",
            "Pink DH. Drive. Riverhead; 2009.",
        ],
        hypotheses=[
            "Task contingency explains the pattern.",
            "Money motivates universally.",
            "Intrinsic motivation dominates always.",
            "The mix is purely individual.",
        ],
        confirm="Reward effects reverse by task type.",
        refute="One reward scheme works across tasks.",
    ),
    dict(
        key="management-06",
        name="The Hawthorne Effect: Real",
        group="People",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Was the Hawthorne effect real - do people improve when "
                 "observed - and what does it mean for management "
                 "research?"),
        background=("The Hawthorne studies founded human-relations "
                    "management; then came the debunking (the data were "
                    "messy, the effect possibly artifactual). Modern "
                    "work finds observation effects are real but "
                    "conditional. Whether the founding myth survives "
                    "matters for how the field reads its own history."),
        why_it_matters=("Hawthorne is management's origin story. Its truth "
                        "calibrates the field's self-understanding."),
        sig_lens=("The Signature lens treats Hawthorne as a history "
                  "ledger: the Signature approach asks what the studies "
                  "actually showed."),
        sig_body=("The Signature proposal models the Hawthorne story as "
                  "myth-with-kernel. Assumptions: (1) the original data "
                  "were flawed; (2) observation effects are nonetheless "
                  "real; (3) the field needed a founding narrative. "
                  "Reasoning path: the proposal shows the specific "
                  "claims were overstated while the general phenomenon "
                  "(attention affects behavior) holds - explaining both "
                  "the debunking and the persistence. Management "
                  "research is then built on a productive myth. Limits: "
                  "the model needs better historical data; the "
                  "implications for current methods need drawing."),
        pointer=('The Signature system models Hawthorne as myth-with-kernel: overstated claims, real phenomenon, productive founding narrative. The Signature test: observation effects replicate conditionally. It would be refuted if no observation effect is found.'),
        key_points=[
            "The Hawthorne studies founded human-relations management.",
            "Debunkers found messy data and possible artifacts.",
            "Observation effects are real but conditional.",
            "The field's origin story is at stake.",
        ],
        requirements=[
            "Historical reanalysis of the data.",
            "Modern observation-effect studies.",
            "An account of the myth's function.",
        ],
        standards=[
            "Claims checked against the Hawthorne literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mayo E. The Human Problems of an Industrial Civilization. 1933.",
            "Levitt SD, List JA. Was there really a Hawthorne effect? 2011.",
        ],
        hypotheses=[
            "Myth-with-kernel explains the historiography.",
            "The effect was entirely artifactual.",
            "The original findings stand.",
            "The myth harmed the field.",
        ],
        confirm="Observation effects replicate conditionally.",
        refute="No observation effect is found.",
    ),
    dict(
        key="management-07",
        name="Pay for Performance: Does It Work",
        group="People",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("Does pay for performance improve performance - or "
                 "distort it?"),
        background=("Incentive pay works for simple, measurable tasks "
                    "(piece rates) but shows gaming, short-termism, and "
                    "crowding-out for complex work. Executive pay "
                    "exploded without clear performance links. Whether "
                    "incentives can be designed for knowledge work "
                    "remains the open question."),
        why_it_matters=("Incentive pay shapes behavior across the economy. "
                        "Its design determines its effects."),
        sig_lens=("The Signature lens treats incentives as a gaming "
                  "ledger: the Signature approach asks what gets "
                  "measured and what gets gamed."),
        sig_body=("The Signature proposal models incentive effects as "
                  "measurability-dependent. Assumptions: (1) people "
                  "optimize measured metrics; (2) complex work has "
                  "unmeasured dimensions; (3) gaming fills the gap. "
                  "Reasoning path: the proposal predicts incentives "
                  "should work where output is fully measurable and "
                  "distort where it is not - explaining piece-rate "
                  "success and executive-pay failure together. The "
                  "design rule: incentivize only what is fully "
                  "measurable. Limits: the model needs better "
                  "multitask studies; team incentives need analysis."),
        pointer=('The Signature system models incentive pay as measurability-dependent: works where output is fully measurable, distorts elsewhere. The Signature test: effects track measurability measures. It would be refuted if incentives work equally for unmeasurable work.'),
        key_points=[
            "Piece rates work for simple measurable tasks.",
            "Complex-work incentives show gaming and short-termism.",
            "Executive pay exploded without performance links.",
            "Knowledge-work incentive design remains open.",
        ],
        requirements=[
            "Multitask incentive studies.",
            "Gaming measures by design.",
            "Team-incentive analyses.",
        ],
        standards=[
            "Claims checked against the incentives literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Lazear EP. Performance pay and productivity. American Economic Review; 2000.",
            "Holmstrom B, Milgrom P. Multitask principal-agent analyses. 1991.",
        ],
        hypotheses=[
            "Measurability dependence explains the pattern.",
            "Incentives always work with good design.",
            "Incentives always distort complex work.",
            "Intrinsic motivation makes incentives unnecessary.",
        ],
        confirm="Effects track measurability measures.",
        refute="Incentives work equally for unmeasurable work.",
    ),
    dict(
        key="management-08",
        name="Why Mergers Fail",
        group="Strategy",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Why do most mergers fail to create value - and can the "
                 "failure rate be fixed?"),
        background=("Most M&A destroys shareholder value: overpayment, "
                    "culture clash, integration failure. Yet deals "
                    "continue - driven by executive incentives, "
                    "overconfidence, and investment-bank fees. Whether "
                    "the failure is fixable or structural remains open."),
        why_it_matters=("M&A reshapes industries. Its failure rate is "
                        "capitalism's expensive puzzle."),
        sig_lens=("The Signature lens treats mergers as an incentive "
                  "ledger: the Signature approach asks who gains when "
                  "deals destroy value."),
        sig_body=("The Signature proposal models merger failure as "
                  "incentive-misaligned. Assumptions: (1) acquirer "
                  "executives gain from deals (pay, empire); (2) "
                  "targets capture the premium; (3) integration is "
                  "hard. Reasoning path: the proposal predicts deals "
                  "should continue despite failure - because the "
                  "decision-makers benefit - which they do. The "
                  "failure is then structural to the incentives, "
                  "fixable only by changing who decides. Limits: the "
                  "model needs better incentive measures; some "
                  "mergers do succeed and need explaining."),
        pointer=('The Signature system models merger failure as incentive-misaligned: decision-makers benefit from value-destroying deals. The Signature test: deal volume tracks executive incentives. It would be refuted if aligned incentives still produce failures.'),
        key_points=[
            "Most M&A destroys acquirer shareholder value.",
            "Overpayment, culture clash, and integration failure recur.",
            "Deals continue despite the record.",
            "Executive incentives and overconfidence drive volume.",
        ],
        requirements=[
            "Decision-maker incentive measures.",
            "Success-case analyses.",
            "Governance reforms tested.",
        ],
        standards=[
            "Claims checked against the M&A literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Moeller SB et al. Wealth destruction on a massive scale. 2005.",
            "Roll R. The hubris hypothesis of corporate takeovers. 1986.",
        ],
        hypotheses=[
            "Incentive misalignment explains persistence.",
            "Integration can be fixed with better methods.",
            "Hubris is the primary driver.",
            "The failure rate is overstated.",
        ],
        confirm="Deal volume tracks executive incentives.",
        refute="Aligned incentives still produce failures.",
    ),
    dict(
        key="management-09",
        name='The Dilemma of the Innovator',
        group="Strategy",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("Why do great companies fail at disruption - and can the "
                 "dilemma be escaped?"),
        background=("Christensen showed incumbents rationally ignore "
                    "disruptive innovations that underserve their best "
                    "customers - until the disruptors move upmarket. "
                    "Solutions (spinouts, ambidexterity) help sometimes. "
                    "Whether the dilemma is escapable or inherent to "
                    "good management remains debated."),
        why_it_matters=("Disruption decides industry leadership. The "
                        "dilemma's escapability determines strategy."),
        sig_lens=("The Signature lens treats disruption as a customer "
                  "ledger: the Signature approach asks whose needs the "
                  "incumbent serves."),
        sig_body=("The Signature proposal models the dilemma as "
                  "rational customer-capture. Assumptions: (1) "
                  "incumbents optimize for best customers; (2) "
                  "disruptions start beneath those customers' needs; "
                  "(3) resource allocation follows current "
                  "profitability. Reasoning path: the proposal shows "
                  "failure is rational given the incentive structure - "
                  "predicting that structural separation (spinouts) "
                  "should help, which it sometimes does. The dilemma "
                  "is then escapable only by changing whose needs "
                  "govern investment. Limits: the model needs better "
                  "disruption predictions; the theory's boundaries "
                  "are contested."),
        pointer=('The Signature system models the dilemma as rational customer-capture, escapable only by changing whose needs govern investment. The Signature test: escape attempts track structural separation. It would be refuted if integrated incumbents disrupt successfully.'),
        key_points=[
            "Incumbents rationally ignore early disruptions.",
            "Disruptors move upmarket over time.",
            "Spinouts and ambidexterity are partial solutions.",
            "Whether the dilemma is escapable is debated.",
        ],
        requirements=[
            "Disruption prediction tests.",
            "Spinout success analyses.",
            "Boundary-condition studies.",
        ],
        standards=[
            "Claims checked against the disruption literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Christensen CM. The Innovator's Dilemma. Harvard Business School Press; 1997.",
            "King AA, Baatartogtokh B. How useful is the theory of disruptive innovation? 2015.",
        ],
        hypotheses=[
            "Customer-capture explains the pattern.",
            "The dilemma is escapable with structure.",
            "The dilemma is inherent to good management.",
            "The theory is overstated.",
        ],
        confirm="Escape attempts track structural separation.",
        refute="Integrated incumbents disrupt successfully.",
    ),
    dict(
        key="management-10",
        name="Core Competence: What Is It",
        group="Strategy",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("What exactly is a core competence - and can the concept "
                 "guide strategy or only rationalize it?"),
        background=("Prahalad and Hamel's core competence promised "
                    "strategy from strengths; critics found the concept "
                    "tautological (successful firms have competences "
                    "because they succeed). The resource-based view "
                    "formalized it but the identification problem - "
                    "spotting competences before success - persists."),
        why_it_matters=("Competence talk shapes strategy. Its emptiness or "
                        "substance determines its value."),
        sig_lens=("The Signature lens treats competence as a prediction "
                  "ledger: the Signature approach asks whether the "
                  "concept predicts or only explains."),
        sig_body=("The Signature proposal models core competence as "
                  "retrospective unless operationalized. Assumptions: "
                  "(1) competences are identified from success; (2) "
                  "success has many causes; (3) prediction needs "
                  "independent measures. Reasoning path: the proposal "
                  "predicts competence claims should fail prospective "
                  "tests - which they do - unless grounded in "
                  "observable routines (see management-31). The concept "
                  "is then useful only when tied to specific "
                  "capabilities. Limits: the model needs prospective "
                  "tests; the routines grounding needs development."),
        pointer=('The Signature system models core competence as retrospective unless tied to observable routines. The Signature test: prospective tests fail without routine grounding. It would be refuted if competence claims predict success prospectively.'),
        key_points=[
            "Core competence promised strategy from strengths.",
            "Critics allege tautology.",
            "The identification problem persists.",
            "The resource-based view formalized but did not solve it.",
        ],
        requirements=[
            "Prospective prediction tests.",
            "Routine-level operationalization.",
            "An account of the concept's persistence.",
        ],
        standards=[
            "Claims checked against the strategy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Prahalad CK, Hamel G. The core competence of the corporation. Harvard Business Review; 1990.",
            "Barney J. Firm resources and sustained competitive advantage. 1991.",
        ],
        hypotheses=[
            "Retrospective-unless-operationalized explains the debate.",
            "Competences are real and identifiable.",
            "The concept is empty.",
            "Dynamic capabilities rescue it.",
        ],
        confirm="Prospective tests fail without routine grounding.",
        refute="Competence claims predict success prospectively.",
    ),
    dict(
        key="management-11",
        name="Why Strategies Fail in Execution",
        group="Strategy",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Why do good strategies die in execution - and is the "
                 "formulation-execution split the problem?"),
        background=("Execution failures are legion: misaligned incentives, "
                    "middle-management resistance, capability gaps. "
                    "Some argue the split itself is false - strategy "
                    "emerges from execution (Mintzberg). Whether "
                    "execution is a distinct discipline or strategy done "
                    "right remains open."),
        why_it_matters=("Strategies are cheap; execution is dear. The "
                        "failure pattern determines management's focus."),
        sig_lens=("The Signature lens treats execution as a feedback "
                  "ledger: the Signature approach asks whether plans "
                  "learn from contact with reality."),
        sig_body=("The Signature proposal models execution failure as "
                  "feedback-breakdown. Assumptions: (1) plans meet "
                  "friction; (2) adaptation needs fast feedback; (3) "
                  "hierarchies slow it. Reasoning path: the proposal "
                  "predicts execution should succeed where feedback "
                  "loops are tight - explaining both the failures "
                  "(rigid plans) and Mintzberg's emergent strategy. "
                  "The formulation-execution split is then the "
                  "problem: strategy must be adaptive. Limits: the "
                  "model needs better feedback measures; the "
                  "discipline question needs settling."),
        pointer=('The Signature system models execution failure as feedback breakdown: strategy must be adaptive, not split from execution. The Signature test: success tracks feedback-tightness. It would be refuted if rigid plans execute successfully.'),
        key_points=[
            "Execution failures are legion and patterned.",
            "Misaligned incentives and resistance recur.",
            "Mintzberg argued strategy emerges from execution.",
            "Whether execution is distinct remains open.",
        ],
        requirements=[
            "Feedback-loop measures in strategy processes.",
            "Emergent-versus-deliberate comparisons.",
            "An account of the split's costs.",
        ],
        standards=[
            "Claims checked against the strategy-process literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mintzberg H. Crafting strategy. Harvard Business Review; 1987.",
            "Bossidy L, Charan R. Execution. Crown; 2002.",
        ],
        hypotheses=[
            "Feedback breakdown explains the failures.",
            "Execution is a distinct discipline.",
            "The split itself causes failure.",
            "Formulation quality determines execution.",
        ],
        confirm="Success tracks feedback-tightness.",
        refute="Rigid plans execute successfully.",
    ),
    dict(
        key="management-12",
        name="Organizational Culture: Can It Be Managed",
        group="Organizations",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Can leaders deliberately change organizational culture - "
                 "or is culture unmanageable by definition?"),
        background=("Culture-change programs usually fail; yet cultures do "
                    "change (sometimes after crises or leadership "
                    "turnover). Schein's model says culture is layered "
                    "(artifacts, values, assumptions) - with the deep "
                    "layers resistant. Whether management can reach the "
                    "deep layers remains open."),
        why_it_matters=("Culture eats strategy. Its manageability "
                        "determines change programs' fate."),
        sig_lens=("The Signature lens treats culture as a layer ledger: "
                  "the Signature approach asks which layers leaders can "
                  "touch."),
        sig_body=("The Signature proposal models culture change as "
                  "layer-limited. Assumptions: (1) artifacts and "
                  "espoused values are manageable; (2) basic assumptions "
                  "change only through shared experience; (3) leaders "
                  "shape experiences. Reasoning path: the proposal "
                  "predicts direct culture programs should fail while "
                  "experience-shaping (new routines, crises survived "
                  "together) succeeds - which matches the evidence. "
                  "Culture is then managed indirectly, through "
                  "experience design. Limits: the model needs better "
                  "layer measures; the ethics of manipulation need "
                  "addressing."),
        pointer=('The Signature system models culture as manageable only indirectly, through experience design rather than direct programs. The Signature test: change tracks experience-shaping, not programs. It would be refuted if direct programs change deep assumptions.'),
        key_points=[
            "Culture-change programs usually fail.",
            "Cultures do change after crises and turnover.",
            "Deep assumptions resist direct management.",
            "Leaders shape the experiences that shape culture.",
        ],
        requirements=[
            "Layer-specific change measures.",
            "Experience-design case studies.",
            "Ethics analyses of cultural management.",
        ],
        standards=[
            "Claims checked against the culture literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Schein EH. Organizational Culture and Leadership. Jossey-Bass; 1985.",
            "Kotter JP, Heskett JL. Corporate Culture and Performance. Free Press; 1992.",
        ],
        hypotheses=[
            "Layer-limited manageability explains the pattern.",
            "Culture is fully manageable.",
            "Culture is unmanageable.",
            "Only selection (hiring) shapes culture.",
        ],
        confirm="Change tracks experience-shaping, not programs.",
        refute="Direct programs change deep assumptions.",
    ),
    dict(
        key="management-13",
        name="The Span of Control Problem",
        group="Organizations",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("What is the optimal span of control - and does "
                 "delayering help or harm?"),
        background=("Classical theory said narrow spans; modern firms "
                    "widened them (delayering) to cut costs. Evidence: "
                    "wide spans work for routine work but overload "
                    "managers of complex work. The optimal span by task "
                    "complexity remains unquantified."),
        why_it_matters=("Spans determine hierarchy shape and managerial "
                        "load. The optimum shapes organization design."),
        sig_lens=("The Signature lens treats span as a load ledger: the "
                  "Signature approach asks what managers actually do "
                  "with subordinates."),
        sig_body=("The Signature proposal models optimal span as "
                  "complexity-contingent. Assumptions: (1) managerial "
                  "attention is finite; (2) complex work needs more of "
                  "it; (3) routine work needs less. Reasoning path: the "
                  "proposal predicts wide spans should succeed for "
                  "routine operations and fail for knowledge work - "
                  "which the evidence supports. Delayering is then "
                  "conditionally good. Limits: the model needs better "
                  "complexity measures; the cost-quality tradeoff "
                  "needs quantifying."),
        pointer=('The Signature system models optimal span as complexity-contingent: wide for routine work, narrow for knowledge work. The Signature test: outcomes track span-complexity fit. It would be refuted if span shows no contingent effects.'),
        key_points=[
            "Classical theory favored narrow spans.",
            "Delayering cut costs but overloaded some managers.",
            "Routine work tolerates wide spans.",
            "The optimum by complexity is unquantified.",
        ],
        requirements=[
            "Complexity measures by unit.",
            "Managerial-load studies.",
            "Cost-quality tradeoff quantification.",
        ],
        standards=[
            "Claims checked against the organization-design literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Graicunas VA. Relationship in organization. 1933.",
            "Dalton DR et al. Organization structure and performance. 1980.",
        ],
        hypotheses=[
            "Complexity contingency explains span effects.",
            "Wide spans are always efficient.",
            "Narrow spans are always better.",
            "Technology eliminated the tradeoff.",
        ],
        confirm="Outcomes track span-complexity fit.",
        refute="Span shows no contingent effects.",
    ),
    dict(
        key="management-14",
        name="Centralization Versus Decentralization",
        group="Organizations",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("When should decisions centralize and when decentralize - "
                 "and why do firms oscillate between the two?"),
        background=("Firms centralize for coordination, decentralize for "
                    "responsiveness - then reverse when the costs bite. "
                    "The oscillation suggests no stable optimum. "
                    "Information technology was supposed to settle it "
                    "(centralize information, decentralize decisions) "
                    "but the pendulum swings on."),
        why_it_matters=("The centralization choice shapes agility and "
                        "control. The oscillation wastes reorganization "
                        "energy."),
        sig_lens=("The Signature lens treats the choice as an information "
                  "ledger: the Signature approach asks where the "
                  "relevant knowledge sits."),
        sig_body=("The Signature proposal models the choice as "
                  "knowledge-location dependent. Assumptions: (1) "
                  "decisions should sit with knowledge; (2) knowledge "
                  "location shifts with strategy and technology; (3) "
                  "reorganizations lag. Reasoning path: the proposal "
                  "predicts oscillation should track knowledge shifts "
                  "- which it does - making the pendulum rational "
                  "adaptation, not failure. The design rule: allocate "
                  "decisions to knowledge, and expect to reallocate. "
                  "Limits: the model needs better knowledge-location "
                  "measures; the reorganization costs are real."),
        pointer=('The Signature system models centralization as knowledge-location dependent, with oscillation as rational adaptation. The Signature test: reorganizations track knowledge shifts. It would be refuted if centralization choices ignore knowledge location.'),
        key_points=[
            "Firms oscillate between centralization and decentralization.",
            "IT was supposed to settle the question.",
            "The pendulum swings regardless.",
            "Knowledge location may be the underlying variable.",
        ],
        requirements=[
            "Knowledge-location measures.",
            "Oscillation-timing analyses.",
            "Reorganization-cost studies.",
        ],
        standards=[
            "Claims checked against the organization-design literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hayek FA. The use of knowledge in society. 1945.",
            "Jensen MC, Meckling WH. Specific and general knowledge. 1992.",
        ],
        hypotheses=[
            "Knowledge location explains the oscillation.",
            "One structure is inherently superior.",
            "The oscillation is managerial faddism.",
            "Technology will eventually settle it.",
        ],
        confirm="Reorganizations track knowledge shifts.",
        refute="Centralization choices ignore knowledge location.",
    ),
    dict(
        key="management-15",
        name="Why Organizations Bureaucratize",
        group="Organizations",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Why do organizations bureaucratize as they grow - and is "
                 "the iron law of oligarchy escapable?"),
        background=("Weber saw bureaucracy as rational; Michels saw "
                    "oligarchy as inevitable. Startups vow to stay flat, "
                    "then add process. The pattern is near-universal, "
                    "but exceptions (long-flat firms) exist. Whether "
                    "bureaucratization is inherent to scale or a failure "
                    "of design remains open."),
        why_it_matters=("Bureaucratization shapes every growing firm. Its "
                        "necessity determines organizational futures."),
        sig_lens=("The Signature lens treats bureaucratization as a "
                  "coordination ledger: the Signature approach asks what "
                  "growth demands."),
        sig_body=("The Signature proposal models bureaucratization as "
                  "coordination-cost driven. Assumptions: (1) informal "
                  "coordination scales poorly; (2) formal process "
                  "substitutes; (3) the substitution has side costs "
                  "(rigidity). Reasoning path: the proposal predicts "
                  "bureaucratization should track coordination load - "
                  "which it does - while technology (lowering "
                  "coordination costs) should enable flatter scale, "
                  "explaining the exceptions. The iron law is then "
                  "conditional, not absolute. Limits: the model needs "
                  "better coordination-cost measures; the rigidity "
                  "costs need fuller accounting."),
        pointer=('The Signature system models bureaucratization as coordination-cost driven, with technology enabling conditional exceptions. The Signature test: flatness tracks coordination-cost measures. It would be refuted if bureaucratization occurs without coordination load.'),
        key_points=[
            "Growth reliably brings bureaucracy.",
            "Michels declared oligarchy inevitable.",
            "Long-flat exceptions exist.",
            "Whether the pattern is necessary is open.",
        ],
        requirements=[
            "Coordination-cost measures by size.",
            "Exception case studies.",
            "Rigidity-cost accounting.",
        ],
        standards=[
            "Claims checked against the bureaucracy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weber M. Economy and Society. 1922.",
            "Michels R. Political Parties. Free Press; 1962.",
        ],
        hypotheses=[
            "Coordination costs explain the pattern.",
            "Oligarchy is inevitable.",
            "Design can prevent bureaucratization.",
            "Technology already solved it.",
        ],
        confirm="Flatness tracks coordination-cost measures.",
        refute="Bureaucratization occurs without coordination load.",
    ),
    dict(
        key="management-16",
        name="The Glass Ceiling: What Sustains It",
        group="People",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("What sustains the glass ceiling - and why do pipeline "
                 "fixes keep failing?"),
        background=("Women's representation thins at each level despite "
                    "pipeline gains. Explanations: bias in promotion, "
                    "network exclusion, work-family structures, and "
                    "homophily in mentoring. Interventions (bias "
                    "training, quotas) show mixed results. The "
                    "sustaining mechanism remains contested."),
        why_it_matters=("The ceiling wastes talent at scale. Its mechanism "
                        "determines the remedy."),
        sig_lens=("The Signature lens treats the ceiling as a network "
                  "ledger: the Signature approach asks who sponsors whom."),
        sig_body=("The Signature proposal models the ceiling as "
                  "sponsorship-network driven. Assumptions: (1) "
                  "advancement needs sponsors; (2) sponsors favor the "
                  "similar; (3) networks reproduce themselves. "
                  "Reasoning path: the proposal predicts the ceiling "
                  "should persist where sponsorship is informal and "
                  "homophilous - which matches the pattern - while "
                  "formal sponsorship programs should crack it. Bias "
                  "training fails because the mechanism is network "
                  "structure, not individual prejudice. Limits: the "
                  "model needs better network data; the work-family "
                  "dimension needs integration."),
        pointer=('The Signature system models the glass ceiling as sponsorship-network driven, with formal sponsorship as the remedy. The Signature test: advancement tracks sponsorship-network position. It would be refuted if networks show no gender pattern.'),
        key_points=[
            "Representation thins at each level.",
            "Pipeline gains did not break the ceiling.",
            "Bias training shows mixed results.",
            "The sustaining mechanism is contested.",
        ],
        requirements=[
            "Sponsorship-network data by level.",
            "Formal-sponsorship program evaluations.",
            "Work-family integration analyses.",
        ],
        standards=[
            "Claims checked against the gender-and-organizations literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Morrison AM et al. Breaking the Glass Ceiling. Addison-Wesley; 1987.",
            "Ibarra H et al. How to overcome the network gap. 2010.",
        ],
        hypotheses=[
            "Sponsorship networks explain the ceiling.",
            "Individual bias is the mechanism.",
            "Work-family structures dominate.",
            "The pipeline will eventually fix it.",
        ],
        confirm="Advancement tracks sponsorship-network position.",
        refute="Networks show no gender pattern.",
    ),
    dict(
        key="management-17",
        name="Diversity: Does It Improve Performance",
        group="People",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Does workforce diversity improve firm performance - and "
                 "under what conditions?"),
        background=("The business case for diversity is asserted widely; "
                    "the evidence is mixed: diversity aids innovation and "
                    "decision quality in some studies, correlates with "
                    "conflict in others. The contingency - when diversity "
                    "helps versus harms - is the open question."),
        why_it_matters=("Diversity policy rides on the business case. Its "
                        "truth determines honest advocacy."),
        sig_lens=("The Signature lens treats diversity as a process "
                  "ledger: the Signature approach asks what diverse "
                  "teams do differently."),
        sig_body=("The Signature proposal models diversity effects as "
                  "process-mediated. Assumptions: (1) diversity brings "
                  "cognitive variety; (2) variety needs inclusive "
                  "process to become performance; (3) without it, "
                  "variety becomes conflict. Reasoning path: the "
                  "proposal predicts diversity should help where "
                  "inclusive processes exist and harm where they do "
                  "not - explaining the mixed evidence. The business "
                  "case is then conditional, not automatic. Limits: "
                  "the model needs better process measures; the "
                  "justice case stands regardless."),
        pointer=('The Signature system models diversity effects as conditional on inclusive processes: variety becomes performance or conflict. The Signature test: effects track inclusive-process measures. It would be refuted if diversity effects ignore process quality.'),
        key_points=[
            "The business case is widely asserted.",
            "Evidence is mixed: innovation gains, conflict costs.",
            "Inclusive process may be the moderator.",
            "The justice case is separate from the business case.",
        ],
        requirements=[
            "Process-moderator studies.",
            "Cognitive-variety measures.",
            "Justice-versus-business-case separation.",
        ],
        standards=[
            "Claims checked against the diversity literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Page SE. The Difference. Princeton University Press; 2007.",
            "van Knippenberg D et al. Work group diversity and performance. 2004.",
        ],
        hypotheses=[
            "Process mediation explains the mixed evidence.",
            "Diversity inherently improves performance.",
            "Diversity inherently harms cohesion.",
            "The effects are too small to matter.",
        ],
        confirm="Effects track inclusive-process measures.",
        refute="Diversity effects ignore process quality.",
    ),
    dict(
        key="management-18",
        name="Remote Work: The Productivity Question",
        group="People",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Does remote work raise or lower productivity - and for "
                 "whom, doing what?"),
        background=("The pandemic experiment showed remote work sustaining "
                    "output for many knowledge workers; but collaboration, "
                    "mentoring, and innovation suffered. Studies find "
                    "task-dependent effects: focused work improves, "
                    "collaborative work degrades. The optimal hybrid "
                    "design remains open."),
        why_it_matters=("Remote work reshapes organizations and cities. "
                        "Its productivity truth determines the future of "
                        "work."),
        sig_lens=("The Signature lens treats remote work as a task ledger: "
                  "the Signature approach asks which tasks need "
                  "presence."),
        sig_body=("The Signature proposal models remote effects as "
                  "task-dependent. Assumptions: (1) focused individual "
                  "work benefits from quiet; (2) collaborative and "
                  "apprenticeship work needs presence; (3) workers "
                  "differ. Reasoning path: the proposal predicts "
                  "productivity should rise for focused tasks and fall "
                  "for collaborative ones - matching the evidence. "
                  "The design answer is then task-based hybridity, not "
                  "blanket policy. Limits: the model needs better "
                  "collaboration measures; the long-term innovation "
                  "effects need tracking."),
        pointer=('The Signature system models remote-work effects as task-dependent, with task-based hybridity as the design answer. The Signature test: effects track task-type measures. It would be refuted if remote effects are uniform across tasks.'),
        key_points=[
            "Output was sustained for many knowledge workers.",
            "Collaboration and mentoring suffered.",
            "Focused work improves remotely; collaborative work degrades.",
            "Optimal hybrid design remains open.",
        ],
        requirements=[
            "Task-type productivity comparisons.",
            "Collaboration-quality measures.",
            "Long-term innovation tracking.",
        ],
        standards=[
            "Claims checked against the remote-work literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bloom N et al. Does working from home work? Quarterly Journal of Economics; 2015.",
            "Gibbs M et al. Remote work and productivity. 2021.",
        ],
        hypotheses=[
            "Task dependence explains the pattern.",
            "Remote work is uniformly better.",
            "Office work is uniformly better.",
            "Selection effects explain everything.",
        ],
        confirm="Effects track task-type measures.",
        refute="Remote effects are uniform across tasks.",
    ),
    dict(
        key="management-19",
        name="The Gig Economy: Efficient or Exploitative",
        group="People",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("Is gig work efficient flexibility or exploitative "
                 "precarity - and can it be both?"),
        background=("Platforms match workers to tasks efficiently; workers "
                    "gain flexibility but lose security, benefits, and "
                    "bargaining power. The classification battles "
                    "(employee versus contractor) rage globally. Whether "
                    "a third way - portable benefits, flexible security "
                    "- can work remains open."),
        why_it_matters=("Gig work is growing fast. Its nature determines "
                        "labor law's future."),
        sig_lens=("The Signature lens treats gig work as a risk ledger: "
                  "the Signature approach asks who bears the risk."),
        sig_body=("The Signature proposal models gig work as "
                  "risk-shifted efficiency. Assumptions: (1) platforms "
                  "create real matching efficiency; (2) they shift risk "
                  "to workers; (3) workers value flexibility "
                  "heterogeneously. Reasoning path: the proposal "
                  "predicts gig work should benefit risk-tolerant "
                  "flexibility-seekers while harming risk-averse "
                  "dependents - which the evidence supports. Both "
                  "narratives are then true for different workers; "
                  "portable benefits address the risk shift without "
                  "killing flexibility. Limits: the model needs better "
                  "worker-heterogeneity data; the portable-benefits "
                  "experiments need evaluation."),
        pointer=('The Signature system models gig work as risk-shifted efficiency, with portable benefits as the third way. The Signature test: outcomes track worker risk-preference measures. It would be refuted if gig effects are uniform across workers.'),
        key_points=[
            "Platforms create real matching efficiency.",
            "Risk shifts from firms to workers.",
            "Worker preferences are heterogeneous.",
            "Classification battles rage globally.",
        ],
        requirements=[
            "Worker-heterogeneity studies.",
            "Portable-benefits evaluations.",
            "Risk-shift quantification.",
        ],
        standards=[
            "Claims checked against the gig-economy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Harris SD, Krueger AB. A proposal for modernizing labor laws. 2015.",
            "Wood AJ et al. Good gig, bad gig. 2019.",
        ],
        hypotheses=[
            "Risk-shift plus heterogeneity explains the debate.",
            "Gig work is efficient for all.",
            "Gig work is exploitative for all.",
            "Portable benefits resolve the tension.",
        ],
        confirm="Outcomes track worker risk-preference measures.",
        refute="Gig effects are uniform across workers.",
    ),
    dict(
        key="management-20",
        name="Why Change Programs Fail",
        group="Leadership",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Why do most organizational change programs fail - and "
                 "what distinguishes the successes?"),
        background=("The 70-percent failure figure is famous (and "
                    "methodologically shaky), but change efforts do "
                    "disappoint routinely. Kotter's stages, Beer and "
                    "Nohria's theories E and O, and countless frameworks "
                    "compete. Whether failure is the norm and what "
                    "distinguishes success remains open."),
        why_it_matters=("Change is constant; failure is expensive. The "
                        "success factors determine leadership practice."),
        sig_lens=("The Signature lens treats change as a coalition "
                  "ledger: the Signature approach asks who must change "
                  "behavior and why they would."),
        sig_body=("The Signature proposal models change success as "
                  "behavior-coalition dependent. Assumptions: (1) "
                  "change needs behavior change by many; (2) people "
                  "change for reasons, not announcements; (3) "
                  "coalitions sustain effort. Reasoning path: the "
                  "proposal predicts programs should succeed where "
                  "they build genuine coalitions around compelling "
                  "reasons - explaining Kotter's emphasis on urgency "
                  "and guiding coalitions. The frameworks are then "
                  "approximations of coalition-building. Limits: the "
                  "model needs better coalition measures; the "
                  "70-percent figure needs retiring."),
        pointer=('The Signature system models change success as coalition-dependent: build genuine coalitions around compelling reasons. The Signature test: success tracks coalition-strength measures. It would be refuted if programs succeed without coalitions.'),
        key_points=[
            "Change programs disappoint routinely.",
            "The 70-percent figure is famous but shaky.",
            "Kotter's stages dominate practitioner thinking.",
            "Success factors remain contested.",
        ],
        requirements=[
            "Coalition measures in change efforts.",
            "Success-factor comparative studies.",
            "A retirement of the 70-percent myth.",
        ],
        standards=[
            "Claims checked against the change literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kotter JP. Leading Change. Harvard Business School Press; 1996.",
            "Beer M, Nohria N. Cracking the code of change. Harvard Business Review; 2000.",
        ],
        hypotheses=[
            "Coalition dependence explains success patterns.",
            "Kotter's stages are sufficient.",
            "Change is inherently likely to fail.",
            "Context determines everything.",
        ],
        confirm="Success tracks coalition-strength measures.",
        refute="Programs succeed without coalitions.",
    ),
    dict(
        key="management-21",
        name="Charismatic Leadership: Real or Myth",
        group="Leadership",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Is charismatic leadership a real causal force - or "
                 "attribution after success?"),
        background=("Charismatic CEOs get credit for turnarounds; but "
                    "attribution theory warns success creates the "
                    "charisma perception, not vice versa. The romance of "
                    "leadership literature documents the bias. Whether "
                    "charisma causes performance or follows it remains "
                    "the field's embarrassment."),
        why_it_matters=("Charisma drives CEO selection and pay. Its "
                        "reality determines whether the market is "
                        "rational."),
        sig_lens=("The Signature lens treats charisma as an attribution "
                  "ledger: the Signature approach asks when the "
                  "perception precedes the results."),
        sig_body=("The Signature proposal models charisma as "
                  "partly-real, partly-attributed. Assumptions: (1) "
                  "expressive behavior genuinely motivates; (2) success "
                  "amplifies charisma perceptions; (3) the two "
                  "compound. Reasoning path: the proposal predicts "
                  "charisma should predict effort and morale (real "
                  "effect) while its link to firm performance runs "
                  "partly through attribution - explaining the "
                  "mixed evidence. Boards then overpay for the "
                  "attributed portion. Limits: the model needs better "
                  "charisma measures independent of outcomes; the "
                  "causal tests are hard."),
        pointer=('The Signature system models charisma as partly real (motivating) and partly attributed (success-created), with boards overpaying for the latter. The Signature test: charisma predicts morale beyond performance. It would be refuted if charisma shows no outcome-independent effect.'),
        key_points=[
            "Charismatic CEOs get credit for turnarounds.",
            "Attribution theory warns of reverse causation.",
            "The romance of leadership documents the bias.",
            "Whether charisma causes or follows success is open.",
        ],
        requirements=[
            "Charisma measures independent of outcomes.",
            "Causal tests of charismatic effects.",
            "Attribution-bias quantification.",
        ],
        standards=[
            "Claims checked against the charisma literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Meindl JR et al. The romance of leadership. 1985.",
            "Conger JA, Kanungo RN. Charismatic Leadership. Jossey-Bass; 1998.",
        ],
        hypotheses=[
            "Partly-real-partly-attributed explains the evidence.",
            "Charisma is a genuine causal force.",
            "Charisma is pure attribution.",
            "The question is unanswerable.",
        ],
        confirm="Charisma predicts morale beyond performance.",
        refute="Charisma shows no outcome-independent effect.",
    ),
    dict(
        key="management-22",
        name="Succession: Why CEOs Fail",
        group="Leadership",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("Why do so many CEO successions fail - and can boards "
                 "pick better?"),
        background=("Outsider successions underperform; insider "
                    "successions do better but entrench. Boards pick for "
                    "charisma and track record, which predict poorly. "
                    "The succession paradox: the skills that win the job "
                    "differ from the skills the job needs."),
        why_it_matters=("CEO succession is the board's most consequential "
                        "decision. Its failure rate is governance's "
                        "scandal."),
        sig_lens=("The Signature lens treats succession as a selection "
                  "ledger: the Signature approach asks what boards "
                  "select for versus what the role needs."),
        sig_body=("The Signature proposal models succession failure as "
                  "selection-mismatch. Assumptions: (1) boards select "
                  "for visibility (charisma, track record); (2) the "
                  "role needs context-specific judgment; (3) outsiders "
                  "lack context. Reasoning path: the proposal predicts "
                  "insider successions should outperform (context "
                  "knowledge) - which they do - and that boards "
                  "should select for learning ability over track "
                  "record. The paradox is then a selection-design "
                  "problem. Limits: the model needs better "
                  "learning-ability measures; the insider-entrenchment "
                  "risk needs managing."),
        pointer=('The Signature system models succession failure as selection mismatch: select for learning ability and context, not charisma and track record. The Signature test: outcomes track selection-criteria measures. It would be refuted if charisma-selected CEOs outperform.'),
        key_points=[
            "Outsider successions tend to underperform.",
            "Boards select for charisma and track record.",
            "The winning skills differ from the needed skills.",
            "Insider entrenchment is the counter-risk.",
        ],
        requirements=[
            "Learning-ability measures for candidates.",
            "Succession-outcome studies by type.",
            "Selection-process redesigns.",
        ],
        standards=[
            "Claims checked against the succession literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Zhang Y, Rajagopalan N. Once an outsider, always an outsider? 2010.",
            "Khurana R. Searching for a Corporate Savior. Princeton University Press; 2002.",
        ],
        hypotheses=[
            "Selection mismatch explains the failure pattern.",
            "Outsiders fail from lack of context.",
            "Boards cannot pick better; luck dominates.",
            "The paradox is overstated.",
        ],
        confirm="Outcomes track selection-criteria measures.",
        refute="Charisma-selected CEOs outperform.",
    ),
    dict(
        key="management-23",
        name="Stakeholder Versus Shareholder",
        group="Strategy",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Should firms serve shareholders alone or all stakeholders - "
                 "and does the choice affect performance?"),
        background=("Friedman declared shareholder primacy; the Business "
                    "Roundtable embraced stakeholders in 2019. Evidence "
                    "on performance effects is mixed; critics call "
                    "stakeholder talk woke-washing. Whether the "
                    "doctrine matters for behavior or is just rhetoric "
                    "remains open."),
        why_it_matters=("Corporate purpose shapes decisions affecting "
                        "millions. The doctrine's reality determines its "
                        "stakes."),
        sig_lens=("The Signature lens treats the debate as a rhetoric "
                  "ledger: the Signature approach asks whether doctrine "
                  "changes behavior."),
        sig_body=("The Signature proposal models the doctrine as "
                  "behaviorally weak. Assumptions: (1) incentives "
                  "drive behavior; (2) doctrine rarely changes "
                  "incentives; (3) long-term shareholder value "
                  "already requires stakeholder care. Reasoning path: "
                  "the proposal predicts stakeholder rhetoric should "
                  "change little - because enlightened shareholder "
                  "value already covers it - which the evidence "
                  "supports. The real variable is then time horizon, "
                  "not stakeholder doctrine. Limits: the model needs "
                  "better behavior measures; the legal duties need "
                  "separate analysis."),
        pointer=('The Signature system models the stakeholder debate as behaviorally weak: time horizon, not doctrine, is the real variable. The Signature test: behavior tracks time-horizon measures. It would be refuted if doctrine shifts change measured behavior.'),
        key_points=[
            "Friedman declared shareholder primacy in 1970.",
            "The Business Roundtable embraced stakeholders in 2019.",
            "Performance evidence is mixed.",
            "Whether doctrine changes behavior is the question.",
        ],
        requirements=[
            "Behavior measures around doctrine shifts.",
            "Time-horizon analyses.",
            "Legal-duty examinations.",
        ],
        standards=[
            "Claims checked against the corporate-purpose literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Friedman M. The social responsibility of business. 1970.",
            "Bebchuk LA, Tallarita R. The illusory promise of stakeholder governance. 2020.",
        ],
        hypotheses=[
            "Time horizon, not doctrine, drives behavior.",
            "Stakeholder governance improves outcomes.",
            "Shareholder primacy is optimal.",
            "The debate is pure rhetoric.",
        ],
        confirm="Behavior tracks time-horizon measures.",
        refute="Doctrine shifts change measured behavior.",
    ),
    dict(
        key="management-24",
        name="The Purpose of the Corporation",
        group="Strategy",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("What is the corporation for - the deepest version of the "
                 "purpose debate, beyond shareholder versus stakeholder?"),
        background=("This entry's companion to management-23 asks the "
                    "foundational question: is the corporation a nexus "
                    "of contracts, a social institution, a person, or a "
                    "commons? Each ontology implies different duties. "
                    "The metaphysics of the firm remains management "
                    "theory's unresolved foundation."),
        why_it_matters=("Corporate ontology grounds every governance "
                        "choice. The foundation shapes the edifice."),
        sig_lens=("The Signature lens treats the firm as an ontology "
                  "ledger: the Signature approach asks what kind of "
                  "thing a corporation is."),
        sig_body=("The Signature proposal models the corporation as "
                  "institutionally plural. Assumptions: (1) firms "
                  "function as contracts, institutions, and "
                  "communities simultaneously; (2) different problems "
                  "activate different aspects; (3) no single ontology "
                  "fits all cases. Reasoning path: the proposal "
                  "predicts purpose disputes should track which aspect "
                  "is salient - explaining the debate's intractability. "
                  "The answer is then pluralist: purpose depends on "
                  "the question asked. Limits: the model needs better "
                  "aspect-activation theory; legal personality needs "
                  "integration."),
        pointer=('The Signature system models corporate purpose as institutionally plural: purpose depends on which aspect of the firm is salient. The Signature test: disputes track aspect-salience measures. It would be refuted if one ontology explains all cases.'),
        key_points=[
            "Competing ontologies: contracts, institution, person, commons.",
            "Each ontology implies different duties.",
            "The purpose debate tracks aspect salience.",
            "The metaphysics remains unresolved.",
        ],
        requirements=[
            "Aspect-activation theory.",
            "Legal-personality integration.",
            "An account of the debate's intractability.",
        ],
        standards=[
            "Claims checked against the corporate-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Coase RH. The nature of the firm. Economica; 1937.",
            "Mayer C. Prosperity. Oxford University Press; 2018.",
        ],
        hypotheses=[
            "Institutional pluralism resolves the debate.",
            "One ontology is correct.",
            "The question is meaningless.",
                       "Law will settle it.",
        ],
        confirm="Disputes track aspect-salience measures.",
        refute="One ontology explains all cases.",
    ),
    dict(
        key="management-25",
        name="ESG: Does It Work",
        group="Strategy",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("Does ESG investing and management improve outcomes - or "
                 "is it marketing with measurement problems?"),
        background=("ESG assets grew enormously; then came the backlash: "
                    "ratings disagree, greenwashing is rampant, and "
                    "performance evidence is mixed. Whether ESG changes "
                    "corporate behavior or merely relabels it remains "
                    "the open empirical question."),
        why_it_matters=("ESG directs trillions. Its reality determines "
                        "whether the capital is working."),
        sig_lens=("The Signature lens treats ESG as a measurement "
                  "ledger: the Signature approach asks what the ratings "
                  "measure."),
        sig_body=("The Signature proposal models ESG as "
                  "measurement-first, impact-second. Assumptions: (1) "
                  "ratings measure disclosure and policies, not "
                  "outcomes; (2) rater disagreement reflects construct "
                  "fuzziness; (3) capital follows ratings. Reasoning "
                  "path: the proposal predicts ESG should change "
                  "disclosure more than behavior - which the evidence "
                  "supports. The fix is then outcome-based metrics, "
                  "not more disclosure ratings. Limits: the model "
                  "needs better outcome measures; the backlash "
                  "politics need accounting."),
        pointer=('The Signature system models ESG as disclosure-driven: the fix is outcome-based metrics, not more ratings. The Signature test: behavior tracks outcome metrics, not ratings. It would be refuted if ratings predict real behavior change.'),
        key_points=[
            "ESG assets grew enormously, then backlash came.",
            "Ratings disagree substantially.",
            "Greenwashing is widespread.",
            "Performance evidence is mixed.",
        ],
        requirements=[
            "Outcome-based ESG metrics.",
            "Behavior-change studies.",
            "Rater-disagreement decomposition.",
        ],
        standards=[
            "Claims checked against the ESG literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Berg F et al. Aggregate confusion: the divergence of ESG ratings. 2022.",
            "Raghunandan A, Rajgopal S. Do ESG funds make stakeholder-friendly investments? 2022.",
        ],
        hypotheses=[
            "Measurement reform would make ESG real.",
            "ESG is inherently marketing.",
            "ESG already changes behavior.",
            "The backlash will kill it regardless.",
        ],
        confirm="Behavior tracks outcome metrics, not ratings.",
        refute="Ratings predict real behavior change.",
    ),
    dict(
        key="management-26",
        name="Platform Power in Markets",
        group="Strategy",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("How should strategy handle platform power - when the "
                 "marketplace itself is the competitor?"),
        background=("Platforms (app stores, marketplaces, ad systems) "
                    "govern the markets they host - setting rules, "
                    "taxing transactions, competing with participants. "
                    "Traditional strategy assumes markets; platform "
                    "strategy must handle private governance. Whether "
                    "existing frameworks adapt remains open."),
        why_it_matters=("Platforms govern digital commerce. Strategy must "
                        "handle private power."),
        sig_lens=("The Signature lens treats platforms as a governance "
                  "ledger: the Signature approach asks what rules the "
                  "platform sets."),
        sig_body=("The Signature proposal models platform strategy as "
                  "governance competition. Assumptions: (1) platforms "
                  "are private regulators; (2) participants strategize "
                  "around platform rules; (3) platforms compete with "
                  "their own participants. Reasoning path: the proposal "
                  "predicts participant strategy should focus on "
                  "platform-rule arbitrage and multi-homing - which "
                  "successful sellers do. Strategy is then partly "
                  "constitutional (shaping the rules) not just "
                  "competitive. Limits: the model needs better "
                  "rule-effect studies; antitrust overlays complicate."),
        pointer=('The Signature system models platform strategy as governance competition: rule-shaping plus multi-homing. The Signature test: success tracks rule-arbitrage measures. It would be refuted if platform rules do not affect participant outcomes.'),
        key_points=[
            "Platforms govern the markets they host.",
            "They tax, rule-set, and compete with participants.",
            "Traditional strategy assumes neutral markets.",
            "Whether frameworks adapt is open.",
        ],
        requirements=[
            "Platform-rule effect studies.",
            "Multi-homing strategy analyses.",
            "Antitrust-strategy integration.",
        ],
        standards=[
            "Claims checked against the platform literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Parker GG et al. Platform Revolution. Norton; 2016.",
            "Khan LM. Amazon's antitrust paradox. Yale Law Journal; 2017.",
        ],
        hypotheses=[
            "Governance competition captures platform strategy.",
            "Traditional frameworks suffice.",
            "Platforms need breaking up, not strategizing.",
            "Participants have no strategic options.",
        ],
        confirm="Success tracks rule-arbitrage measures.",
        refute="Platform rules do not affect participant outcomes.",
    ),
    dict(
        key="management-27",
        name="The Attention Economy Firm",
        group="Strategy",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("How should firms strategize when attention is the scarce "
                 "resource - and what does it do to the firm itself?"),
        background=("Attention-economy firms monetize engagement; the "
                    "logic (maximize time-on-site) shapes products, "
                    "metrics, and culture. Critics argue it corrupts "
                    "missions (news, education, sociality). Whether "
                    "attention-based business models are compatible with "
                    "healthy missions remains open."),
        why_it_matters=("Attention firms shape public discourse and "
                        "well-being. Their strategy logic has social "
                        "consequences."),
        sig_lens=("The Signature lens treats attention as a mission "
                  "ledger: the Signature approach asks what the "
                  "engagement metric does to purpose."),
        sig_body=("The Signature proposal models attention strategy as "
                  "metric-corrupted. Assumptions: (1) engagement "
                  "metrics reward outrage and addiction; (2) missions "
                  "need different metrics; (3) the metric governs "
                  "behavior. Reasoning path: the proposal predicts "
                  "mission drift should track engagement-dependence - "
                  "which the record supports. The strategic answer is "
                  "then metric reform: measure mission outcomes, not "
                  "attention. Limits: the model needs better "
                  "mission-drift measures; the business-model "
                  "alternatives need development."),
        pointer=('The Signature system models attention strategy as metric-corrupted: measure mission outcomes, not engagement. The Signature test: drift tracks engagement-dependence. It would be refuted if attention firms sustain healthy missions.'),
        key_points=[
            "Attention firms monetize engagement.",
            "Engagement metrics reward outrage and addiction.",
            "Mission drift follows engagement dependence.",
            "Whether the models are compatible with health is open.",
        ],
        requirements=[
            "Mission-drift measures.",
            "Alternative metric designs.",
            "Business-model alternative studies.",
        ],
        standards=[
            "Claims checked against the attention-economy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wu T. The Attention Merchants. Knopf; 2016.",
            "Hwang T, Levy K. The theory of the platform. 2015.",
        ],
        hypotheses=[
            "Metric reform resolves the tension.",
            "Attention models are inherently corrupting.",
            "Engagement and mission can align.",
            "Regulation is the only answer.",
        ],
        confirm="Drift tracks engagement-dependence.",
        refute="Attention firms sustain healthy missions.",
    ),
    dict(
        key="management-28",
        name="Algorithmic Management: Fair",
        group="People",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Can algorithmic management - AI bosses assigning, rating, "
                 "and firing - be fair?"),
        background=("Platforms and warehouses manage by algorithm: "
                    "opaque, unappealable, optimizing metrics workers "
                    "cannot see. Workers report stress and unfairness; "
                    "firms report efficiency. Whether transparency and "
                    "appeal rights can make algorithmic management just "
                    "remains open."),
        why_it_matters=("Algorithmic bosses govern millions. Their "
                        "fairness is labor justice's new frontier."),
        sig_lens=("The Signature lens treats algorithmic management as "
                  "a due-process ledger: the Signature approach asks "
                  "what workers can contest."),
        sig_body=("The Signature proposal models fairness as "
                  "contestability. Assumptions: (1) workers accept "
                  "decisions they can understand and appeal; (2) "
                  "opacity prevents both; (3) efficiency does not "
                  "require opacity. Reasoning path: the proposal "
                  "predicts perceived fairness should track "
                  "contestability features - which early evidence "
                  "supports. The design answer is then due process "
                  "for algorithms: explanation plus appeal. Limits: "
                  "the model needs better contestability studies; "
                  "the efficiency costs need measuring."),
        pointer=('The Signature system models algorithmic-management fairness as contestability: explanation plus appeal rights. The Signature test: fairness perceptions track contestability. It would be refuted if contestability shows no fairness effect.'),
        key_points=[
            "Algorithmic managers are opaque and unappealable.",
            "Workers report stress and unfairness.",
            "Firms report efficiency gains.",
            "Whether transparency can make it just is open.",
        ],
        requirements=[
            "Contestability-feature experiments.",
            "Efficiency-cost measures.",
            "Worker-outcome tracking.",
        ],
        standards=[
            "Claims checked against the algorithmic-management literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rosenblat A, Stark L. Algorithmic labor and information asymmetries. 2016.",
            "Mohlmann M, Zalmanson L. Hands on the wheel. 2017.",
        ],
        hypotheses=[
            "Contestability delivers fairness.",
            "Algorithmic management is inherently unfair.",
            "Efficiency requires opacity.",
            "Workers will adapt and accept.",
        ],
        confirm="Fairness perceptions track contestability.",
        refute="Contestability shows no fairness effect.",
    ),
    dict(
        key="management-29",
        name="Unions: Do They Help Firms",
        group="People",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("Do unions help or harm firm performance - the "
                 "productivity, voice, and monopoly faces of unionism?"),
        background=("Freeman and Medoff's two faces: unions raise wages "
                    "(monopoly face, hurting profits) but also give "
                    "voice (reducing turnover, improving communication). "
                    "Net productivity effects are debated and "
                    "context-dependent. Whether modern unions help firms "
                    "remains empirically open."),
        why_it_matters=("Union decline reshaped labor markets. The "
                        "productivity truth determines policy."),
        sig_lens=("The Signature lens treats unions as a voice ledger: "
                  "the Signature approach asks when voice outweighs "
                  "monopoly."),
        sig_body=("The Signature proposal models union effects as "
                  "context-contingent. Assumptions: (1) voice mechanisms "
                  "help where communication is poor; (2) monopoly costs "
                  "hurt where competition is fierce; (3) the balance "
                  "varies. Reasoning path: the proposal predicts unions "
                  "should help in low-trust, poor-communication firms "
                  "and harm where they entrench rigidities - matching "
                  "the mixed evidence. The question is then not "
                  "unions-good-or-bad but when. Limits: the model needs "
                  "better voice measures; the modern organizing wave "
                  "needs study."),
        pointer=('The Signature system models union effects as context-contingent: voice helps where communication is poor; monopoly costs hurt where competition is fierce. The Signature test: effects track voice-need measures. It would be refuted if union effects are uniform across contexts.'),
        key_points=[
            "Two faces: monopoly (wages up, profits down) and voice.",
            "Net productivity effects are debated.",
            "Effects appear context-dependent.",
            "Modern organizing waves need study.",
        ],
        requirements=[
            "Voice-mechanism measures.",
            "Context-contingency studies.",
            "Modern-wave outcome tracking.",
        ],
        standards=[
            "Claims checked against the unions literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Freeman RB, Medoff JL. What Do Unions Do? Basic Books; 1984.",
            "DiNardo J, Lee DS. Economic impacts of new unionization. Quarterly Journal of Economics; 2004.",
        ],
        hypotheses=[
            "Context contingency explains the mixed evidence.",
            "Unions help productivity via voice.",
            "Unions harm via monopoly rigidities.",
            "The effects washed out long ago.",
        ],
        confirm="Effects track voice-need measures.",
        refute="Union effects are uniform across contexts.",
    ),
    dict(
        key="management-30",
        name="The Four-Day Week Evidence",
        group="People",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("Does the four-day week maintain output - and what does "
                 "the evidence actually show?"),
        background=("Trials (Iceland, UK, Spain) report maintained output "
                    "with improved well-being. But selection effects "
                    "(enthusiastic firms volunteer), Hawthorne effects, "
                    "and short durations cloud the findings. Whether the "
                    "results generalize remains the open question."),
        why_it_matters=("Work-time is civilization's bargain. The evidence "
                        "determines its future."),
        sig_lens=("The Signature lens treats the trials as a selection "
                  "ledger: the Signature approach asks who volunteers."),
        sig_body=("The Signature proposal models trial results as "
                  "selection-inflated but directionally real. "
                  "Assumptions: (1) volunteering firms are "
                  "better-managed; (2) intensity effects are real "
                  "(Parkinson's law in reverse); (3) both operate. "
                  "Reasoning path: the proposal predicts genuine but "
                  "smaller effects in representative samples - "
                  "explaining enthusiasm plus skepticism. The "
                  "four-day week is then viable for focused work, "
                  "not universal. Limits: the model needs "
                  "representative trials; the long-term effects need "
                  "tracking."),
        pointer=('The Signature system models four-day-week results as selection-inflated but directionally real: viable for focused work, not universal. The Signature test: effects shrink but persist representatively. It would be refuted if no effect in representative samples.'),
        key_points=[
            "Trials report maintained output, improved well-being.",
            "Selection and Hawthorne effects cloud findings.",
            "Durations are short.",
            "Generalizability remains open.",
        ],
        requirements=[
            "Representative-sample trials.",
            "Long-term effect tracking.",
            "Task-contingency analyses.",
        ],
        standards=[
            "Claims checked against the work-time literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Haraldsson GD, Kellam J. Going Public: Iceland's Journey to a Shorter Working Week. 2021.",
            "Autonomy. The UK four-day week pilot. 2023.",
        ],
        hypotheses=[
            "Selection-inflated but directionally real.",
            "The effects are entirely artifactual.",
            "Four-day weeks work universally.",
            "Intensity effects explain everything.",
        ],
        confirm="Effects shrink but persist representatively.",
        refute="No effect in representative samples.",
    ),
    dict(
        key="management-31",
        name="Organizational Learning: How",
        group="Organizations",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("How do organizations actually learn - and why do they "
                 "keep making the same mistakes?"),
        background=("Argyris distinguished single-loop (fix the error) "
                    "from double-loop (fix the thinking) learning; "
                    "defensive routines block the latter. Knowledge "
                    "management systems capture documents, not wisdom. "
                    "Whether organizations can learn double-loop "
                    "remains the open question."),
        why_it_matters=("Organizational learning determines adaptation. "
                        "Its mechanisms determine survival."),
        sig_lens=("The Signature lens treats learning as a defense "
                  "ledger: the Signature approach asks what blocks "
                  "honest reflection."),
        sig_body=("The Signature proposal models learning failure as "
                  "defense-driven. Assumptions: (1) double-loop "
                  "learning threatens identities; (2) defensive "
                  "routines protect them; (3) psychological safety "
                  "lowers defenses. Reasoning path: the proposal "
                  "predicts learning should track safety and "
                  "structured reflection - linking to management-03 "
                  "and explaining why knowledge systems fail (they "
                  "skip the defenses). Organizations learn when it "
                  "is safe to be wrong. Limits: the model needs "
                  "better defense measures; the scaling of "
                  "reflection practices needs study."),
        pointer=('The Signature system models organizational learning as defense-limited: organizations learn when it is safe to be wrong. The Signature test: learning tracks safety-reflection measures. It would be refuted if learning occurs without safety.'),
        key_points=[
            "Single-loop fixes errors; double-loop fixes thinking.",
            "Defensive routines block double-loop learning.",
            "Knowledge systems capture documents, not wisdom.",
            "Whether double-loop learning is achievable is open.",
        ],
        requirements=[
            "Defensive-routine measures.",
            "Reflection-practice evaluations.",
            "Safety-learning link tests.",
        ],
        standards=[
            "Claims checked against the organizational-learning literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Argyris C, Schon DA. Organizational Learning. Addison-Wesley; 1978.",
            "Edmondson A. Psychological safety and learning behavior in work teams. 1999.",
        ],
        hypotheses=[
            "Defense limitation explains learning failures.",
            "Organizations cannot double-loop learn.",
            "Systems can substitute for safety.",
            "Learning is individual, not organizational.",
        ],
        confirm="Learning tracks safety-reflection measures.",
        refute="Learning occurs without safety.",
    ),
    dict(
        key="management-32",
        name="The Multinational: How Governed",
        group="Organizations",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("How should multinationals govern across borders - global "
                 "integration versus local responsiveness?"),
        background=("Bartlett and Ghoshal's transnational solution "
                    "promised both; in practice firms oscillate. "
                    "Subsidiary initiative, headquarters control, and "
                    "cultural distance complicate. The digital era "
                    "(remote coordination) was supposed to help but "
                    "created new control problems."),
        why_it_matters=("Multinationals organize global production. Their "
                        "governance shapes development and control."),
        sig_lens=("The Signature lens treats the multinational as a "
                  "knowledge ledger: the Signature approach asks where "
                  "knowledge is created versus used."),
        sig_body=("The Signature proposal models MNC governance as "
                  "knowledge-flow dependent. Assumptions: (1) "
                  "subsidiaries create local knowledge; (2) "
                  "headquarters hold global knowledge; (3) flows need "
                  "governance. Reasoning path: the proposal predicts "
                  "governance should follow knowledge flows - "
                  "explaining why the transnational ideal works where "
                  "flows are genuinely two-way. Digital tools help "
                  "flows but not the politics of control. Limits: the "
                  "model needs better flow measures; the power "
                  "dimension needs fuller treatment."),
        pointer=('The Signature system models multinational governance as knowledge-flow dependent: follow the flows, manage the politics. The Signature test: governance tracks flow measures. It would be refuted if governance ignores knowledge flows.'),
        key_points=[
            "The transnational ideal promises integration plus responsiveness.",
            "Firms oscillate in practice.",
            "Subsidiary initiative complicates headquarters control.",
            "Digital coordination created new control problems.",
        ],
        requirements=[
            "Knowledge-flow measures.",
            "Governance-flow fit studies.",
            "Power-dimension analyses.",
        ],
        standards=[
            "Claims checked against the international-business literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bartlett CA, Ghoshal S. Managing Across Borders. Harvard Business School Press; 1989.",
            "Doz YL et al. From Global to Metanational. Harvard Business School Press; 2001.",
        ],
        hypotheses=[
            "Knowledge-flow dependence explains governance patterns.",
            "The transnational is achievable generally.",
            "Headquarters control is always needed.",
            "Subsidiaries should be fully autonomous.",
        ],
        confirm="Governance tracks flow measures.",
        refute="Governance ignores knowledge flows.",
    ),
    dict(
        key="management-33",
        name="Crisis Leadership: What Works",
        group="Leadership",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("What leadership works in crisis - and does crisis "
                 "reveal or distort leadership quality?"),
        background=("Crises demand fast decisions under uncertainty; "
                    "research finds decisive communication, visible "
                    "presence, and adaptive learning matter. But crisis "
                    "also rewards authoritarianism and punishes "
                    "deliberation - with long-term costs. Whether "
                    "crisis leadership generalizes to normal times "
                    "remains open."),
        why_it_matters=("Crises test leaders. The lessons determine "
                        "preparedness."),
        sig_lens=("The Signature lens treats crisis as a tempo ledger: "
                  "the Signature approach asks what speed the "
                  "situation demands."),
        sig_body=("The Signature proposal models crisis leadership as "
                  "tempo-matched. Assumptions: (1) crises compress "
                  "decision time; (2) different crises need different "
                  "tempos; (3) leaders have tempo habits. Reasoning "
                  "path: the proposal predicts effectiveness should "
                  "track tempo matching - decisive where speed "
                  "matters, deliberative where learning matters - "
                  "explaining why crisis heroes often fail afterward. "
                  "The skill is then tempo flexibility, not "
                  "decisiveness. Limits: the model needs better tempo "
                  "measures; the authoritarianism risk needs "
                  "addressing."),
        pointer=('The Signature system models crisis leadership as tempo-matched: the skill is tempo flexibility, not decisiveness. The Signature test: effectiveness tracks tempo-match measures. It would be refuted if decisive leaders succeed across crisis types.'),
        key_points=[
            "Crises compress decision time under uncertainty.",
            "Decisive communication and presence matter.",
            "Crisis rewards authoritarianism with long-term costs.",
            "Crisis heroes often fail in normal times.",
        ],
        requirements=[
            "Tempo measures by crisis type.",
            "Flexibility assessments.",
            "Long-term cost studies.",
        ],
        standards=[
            "Claims checked against the crisis-leadership literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Boin A et al. The Politics of Crisis Management. Cambridge University Press; 2005.",
            "James EH, Wooten LP. Leadership as (un)usual. 2005.",
        ],
        hypotheses=[
            "Tempo matching explains effectiveness.",
            "Decisiveness is the crisis virtue.",
            "Crisis reveals true leadership quality.",
            "Crisis distorts leadership evaluation.",
        ],
        confirm="Effectiveness tracks tempo-match measures.",
        refute="Decisive leaders succeed across crisis types.",
    ),
    dict(
        key="management-34",
        name="A Unified Theory of Management",
        group="Leadership",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can management theory unify - scientific, human-"
                 "relations, systems, and critical schools - into one "
                 "account?"),
        background=("Each school captures something: scientific "
                    "management the task, human relations the people, "
                    "systems the interconnection, critical theory the "
                    "power. Unification attempts remain programmatic. "
                    "Whether management's nature permits one theory is "
                    "the field's capstone question."),
        why_it_matters=("This is management's capstone: the answer "
                        "determines what management is."),
        sig_lens=("The Signature lens treats the schools as a level "
                  "ledger: the Signature approach asks what level each "
                  "school owns."),
        sig_body=("The Signature proposal models unification as "
                  "level-integration. Assumptions: (1) managing spans "
                  "task, person, system, and power levels; (2) each "
                  "school owns a level; (3) levels interact. Reasoning "
                  "path: the proposal assigns scientific management to "
                  "tasks, human relations to people, systems theory to "
                  "interconnection, critical theory to power - with "
                  "managerial practice as the integrator. Unity comes "
                  "from the practice that holds the levels together, "
                  "not one school's victory. Limits: the integration "
                  "is sketched; partisans may reject the settlement."),
        pointer=('The Signature system assigns each school its level of managing, with practice as the integrator. The Signature test: integrated models predict across levels. It would be refuted if levels prove irreducible to common theory.'),
        key_points=[
            "Four schools offer incompatible images of management.",
            "Each captures what the others miss.",
            "Unification attempts remain programmatic.",
            "Whether one theory is possible is foundational.",
        ],
        requirements=[
            "A level architecture for the schools.",
            "An account of level interaction.",
            "Testable implications of the integration.",
        ],
        standards=[
            "Claims checked against the management-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Taylor FW. The Principles of Scientific Management. 1911.",
            "Parker LD, Ritson PA. Fads, stereotypes and management gurus. 2005.",
        ],
        hypotheses=[
            "Level-integration unifies management theory.",
            "The schools are incommensurable.",
            "One school will absorb the rest.",
            "Pluralism is permanent.",
        ],
        confirm="Integrated models predict across levels.",
        refute="Levels prove irreducible to common theory.",
    ),
]
