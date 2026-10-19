#!/usr/bin/env python3
"""Entries for the Unsolved Political Science databases (batch 4).

34 famous open problems in political science, ladder-ordered by accessibility.
ID prefixes: JAH-USPO- (public) and JAH-USPOS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="political-science-01",
        name="Why Do Democracies Backslide",
        group="Democracy",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Why do established democracies erode from within - through "
                 "elected leaders hollowing out courts, media, and electoral "
                 "rules - and can backsliding be predicted or stopped?"),
        background=("The third wave of democratization has partially reversed: "
                    "Hungary, Venezuela, Turkey, and others slid toward "
                    "authoritarianism via legal means. Theories blame economic "
                    "grievance, cultural backlash, institutional design, elite "
                    "strategy, and disinformation. But backsliding is uneven - "
                    "similar grievances produce resilience elsewhere - and "
                    "early-warning models remain weak."),
        why_it_matters=("Democracy now retreats more than it advances. Understanding "
                        "erosion is the precondition for defending self-government."),
        sig_lens=("The Signature lens treats backsliding as a guardrail ledger: "
                  "the Signature approach asks which guardrails actually bind "
                  "when tested."),
        sig_body=("The Signature proposal models backsliding as guardrail "
                  "sequencing. Assumptions: (1) democracies rest on layered "
                  "guardrails (courts, media, parties, norms); (2) would-be "
                  "autocrats capture them in order of vulnerability; (3) "
                  "each capture lowers the cost of the next. Reasoning path: "
                  "the proposal shows erosion follows a predictable sequence - "
                  "media and electoral administration first, courts later - "
                  "predicting that early intervention must target the first "
                  "captured layer, not the last. Resilience then depends on "
                  "guardrail independence, not guardrail number. Limits: the "
                  "sequence varies; the model needs cross-case testing."),
        pointer=('The Signature system models backsliding as sequential guardrail capture, with intervention targeting the first captured layer. The Signature test: erosion sequences match the predicted capture order. It would be refuted if backsliding strikes the strongest guardrails first.'),
        key_points=[
            "Backsliding proceeds through legal means, not coups.",
            "Guardrail capture follows observable sequences.",
            "Similar grievances produce resilience in some democracies.",
            "Early-warning models remain weak.",
        ],
        requirements=[
            "A predictive model of erosion sequences.",
            "An account of resilient counterexamples.",
            "Separation of institutional from cultural causes.",
        ],
        standards=[
            "Claims checked against the democratic-erosion literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Levitsky S, Ziblatt D. How Democracies Die. Crown; 2018.",
            "Bermeo N. On democratic backsliding. Journal of Democracy; 2016.",
        ],
        hypotheses=[
            "Sequential guardrail capture explains erosion patterns.",
            "Economic grievance is the prime mover.",
            "Cultural backlash drives the process.",
            "Institutional design determines vulnerability.",
        ],
        confirm="Erosion sequences match the predicted capture order.",
        refute="Backsliding strikes the strongest guardrails first.",
    ),
    dict(
        key="political-science-02",
        name="Are Voters Rational",
        group="Behavior",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Do voters choose on policy and performance - or on identity, "
                 "emotion, and misinformation - and how much does it matter?"),
        background=("The Michigan model found party identity drives votes; "
                    "retrospective voting models found performance matters; "
                    "recent work finds widespread misinformation and "
                    "identity-protective reasoning. Achen and Bartels argued "
                    "voters are worse than assumed - myopic, tribal, "
                    "manipulable. Defenders reply that heuristics work well "
                    "enough and that elite cues are informative shortcuts."),
        why_it_matters=("Democracy's legitimacy rests on voter competence. If "
                        "voters cannot judge, democratic theory needs "
                        "rebuilding."),
        sig_lens=("The Signature lens treats voting as an information ledger: "
                  "the Signature approach asks what voters can cheaply know "
                  "versus what democracy needs them to know."),
        sig_body=("The Signature proposal models voters as rationally "
                  "ignorant but socially informed. Assumptions: (1) policy "
                  "detail is costly to learn; (2) group cues are cheap and "
                  "often informative; (3) retrospective judgment (am I better "
                  "off?) needs little information. Reasoning path: the "
                  "proposal shows democratic competence does not require "
                  "informed voters - only voters whose cheap heuristics "
                  "track performance, which they often do. Breakdowns occur "
                  "when cues mislead systematically (disinformation) or when "
                  "identity decouples from interest. Limits: the model is "
                  "optimistic about heuristics; misinformation effects are "
                  "hard to bound."),
        pointer=('The Signature system models voters as rationally ignorant but heuristically competent, with breakdowns when cues mislead. The Signature test: heuristic-based votes track performance measures. It would be refuted if voters systematically punish good performance and reward bad.'),
        key_points=[
            "Party identity strongly predicts votes.",
            "Retrospective performance voting also works.",
            "Misinformation and identity reasoning are documented.",
            "Heuristics often track interests well enough.",
        ],
        requirements=[
            "An account of both competence and failure.",
            "Bounds on misinformation effects.",
            "A standard for 'good enough' democratic judgment.",
        ],
        standards=[
            "Claims checked against the voting-behavior literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Achen CH, Bartels LM. Democracy for Realists. Princeton University Press; 2016.",
            "Campbell A et al. The American Voter. Wiley; 1960.",
        ],
        hypotheses=[
            "Cheap heuristics sustain adequate democratic competence.",
            "Voters are systematically worse than theory needs.",
            "Elite cues are informative shortcuts, not manipulation.",
            "Identity has displaced interest as the voting basis.",
        ],
        confirm="Heuristic-based votes track performance measures.",
        refute="Voters systematically punish good performance and reward bad.",
    ),
    dict(
        key="political-science-03",
        name="Why Do Parties Polarize",
        group="Behavior",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("Why have parties polarized so sharply in many democracies - "
                 "and is mass polarization real or elite-driven?"),
        background=("American parties are more ideologically sorted than in "
                    "decades; similar patterns appear in Europe, Latin America, "
                    "and Asia. Debate splits: elite polarization (parties and "
                    "media moved; voters followed) versus mass polarization "
                    "(voters genuinely divided); causes proposed include "
                    "inequality, social sorting, media fragmentation, and "
                    "institutional incentives. Affective polarization - "
                    "hating the other side - may outrun policy disagreement."),
        why_it_matters=("Polarization paralyzes governance and corrodes "
                        "democratic norms. Its source determines the remedy."),
        sig_lens=("The Signature lens treats polarization as a sorting ledger: "
                  "the Signature approach asks what sorted the parties and "
                  "what sorted the people."),
        sig_body=("The Signature proposal models two polarizations with "
                  "different motors. Assumptions: (1) elites respond to "
                  "primary electorates and donors; (2) voters sort socially "
                  "by lifestyle and geography; (3) media amplifies conflict. "
                  "Reasoning path: the proposal shows elite polarization is "
                  "institutionally driven (primaries, money) while mass "
                  "affective polarization is socially driven (sorting, "
                  "identity) - predicting they can diverge, which matches "
                  "cases where elites are polarized but voters are merely "
                  "sorted. Remedies then differ by level. Limits: the "
                  "interaction between levels is strong; the model needs "
                  "better causal identification."),
        pointer=('The Signature system separates elite polarization (institutional) from mass affective polarization (social), with different remedies. The Signature test: elite and mass measures diverge as predicted. It would be refuted if mass policy polarization matches elite polarization exactly.'),
        key_points=[
            "Parties polarized sharply in many democracies.",
            "Elite-driven versus mass-driven accounts compete.",
            "Affective polarization may outrun policy disagreement.",
            "Social sorting by geography and lifestyle intensifies divides.",
        ],
        requirements=[
            "Separation of elite from mass polarization.",
            "Causal accounts, not just correlations.",
            "Cross-national testing of mechanisms.",
        ],
        standards=[
            "Claims checked against the polarization literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "McCarty N, Poole KT, Rosenthal H. Polarized America. MIT Press; 2006.",
            "Iyengar S et al. The origins and consequences of affective polarization. 2019.",
        ],
        hypotheses=[
            "Elite and mass polarization have different motors.",
            "Inequality drives the whole process.",
            "Media fragmentation is the prime mover.",
            "Institutions (primaries, electoral rules) drive it.",
        ],
        confirm="Elite and mass measures diverge as predicted.",
        refute="Mass policy polarization matches elite polarization exactly.",
    ),
    dict(
        key="political-science-04",
        name="Why Is Turnout What It Is",
        group="Behavior",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Why do turnout rates vary so enormously - from under 50 "
                 "percent to over 90 percent - and what actually mobilizes "
                 "voters?"),
        background=("The paradox of voting: one vote never decides, yet "
                    "millions vote. Turnout tracks institutions (compulsory "
                    "voting, registration ease, proportional representation), "
                    "mobilization (parties, unions), and social norms - but "
                    "the weights are disputed, and turnout has fallen in many "
                    "established democracies while rising in some new ones. "
                    "What moves the needle remains partly mysterious."),
        why_it_matters=("Turnout determines whose voices count. Unequal "
                        "turnout means unequal representation - democracy's "
                        "core promise broken quietly."),
        sig_lens=("The Signature lens treats turnout as a cost-benefit ledger "
                  "with social interest: the Signature approach asks what "
                  "makes voting feel obligatory."),
        sig_body=("The Signature proposal models turnout as norm-driven with "
                  "institutional multipliers. Assumptions: (1) instrumental "
                  "benefit of one vote is near zero; (2) social norms and "
                  "identity supply the motive; (3) institutions multiply or "
                  "suppress the norm. Reasoning path: the proposal shows "
                  "turnout variation follows norm strength times institutional "
                  "ease - predicting compulsory voting and easy registration "
                  "raise turnout most where norms are weakest, which matches "
                  "the data. Mobilization works by activating norms, not by "
                  "informing. Limits: norm strength is hard to measure "
                  "independently; the model underplays habit."),
        pointer=('The Signature system models turnout as social norms times institutional ease, with mobilization activating norms rather than informing. The Signature test: institutional ease multiplies turnout most where norms are weak. It would be refuted if turnout tracks instrumental stakes alone.'),
        key_points=[
            "Turnout ranges from under 50 to over 90 percent.",
            "The paradox of voting: one vote never decides.",
            "Institutions (compulsory voting, registration) matter hugely.",
            "Turnout inequality skews representation.",
        ],
        requirements=[
            "An account of the instrumental paradox.",
            "Weights for institutions, mobilization, and norms.",
            "An explanation of turnout inequality.",
        ],
        standards=[
            "Claims checked against the turnout literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Blais A. To Vote or Not to Vote. University of Pittsburgh Press; 2000.",
            "Franklin MN. Voter Turnout and the Dynamics of Electoral Competition. Cambridge University Press; 2004.",
        ],
        hypotheses=[
            "Norms times institutions explain the variation.",
            "Habit formed early is the main driver.",
            "Mobilization contact is decisive.",
            "Stakes (closeness, importance) dominate.",
        ],
        confirm="Institutional ease multiplies turnout most where norms are weak.",
        refute="Turnout tracks instrumental stakes alone.",
    ),
    dict(
        key="political-science-05",
        name="Does Deliberation Change Minds",
        group="Behavior",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("Can structured deliberation - citizens reasoning together - "
                 "change political minds, or does it merely polarize?"),
        background=("Deliberative polls and citizens' assemblies show opinion "
                    "shifts after facilitated discussion - Ireland's assemblies "
                    "preceded landmark referendums. But critics note selection "
                    "effects, facilitator influence, and the gap between "
                    "lab-like settings and real politics. Whether deliberation "
                    "scales from dozens of citizens to millions remains the "
                    "open question."),
        why_it_matters=("If deliberation works at scale, democracy can be more "
                        "than voting - it can be collective reasoning. If not, "
                        "deliberative reforms are theater."),
        sig_lens=("The Signature lens treats deliberation as a conditions "
                  "ledger: the Signature approach asks what settings make "
                  "reasoning beat rationalization."),
        sig_body=("The Signature proposal models deliberation effects as "
                  "condition-dependent. Assumptions: (1) people reason to "
                  "justify identities under threat; (2) structured settings "
                  "reduce threat (balanced information, diverse groups, "
                  "facilitation); (3) effects decay without reinforcement. "
                  "Reasoning path: the proposal predicts deliberation shifts "
                  "opinions exactly where conditions neutralize identity "
                  "threat - explaining both the assembly successes and the "
                  "failures in polarized real-world settings. Scale then "
                  "requires reproducing the conditions, not just the format. "
                  "Limits: the model needs long-term follow-up data; "
                  "facilitator effects are under-studied."),
        pointer=('The Signature system models deliberation as condition-dependent, working where identity threat is neutralized. The Signature test: opinion shifts track threat-neutralization measures. It would be refuted if well-designed deliberation fails to shift opinions.'),
        key_points=[
            "Deliberative polls and assemblies show opinion shifts.",
            "Ireland's assemblies preceded landmark referendums.",
            "Selection and facilitator effects are concerns.",
            "Scaling from dozens to millions is unproven.",
        ],
        requirements=[
            "Conditions separating success from failure.",
            "Long-term follow-up on opinion shifts.",
            "A scalable institutional design.",
        ],
        standards=[
            "Claims checked against the deliberation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fishkin JS. When the People Speak. Oxford University Press; 2009.",
            "Farrell DM et al. The Irish citizens assemblies. 2019.",
        ],
        hypotheses=[
            "Deliberation works where identity threat is neutralized.",
            "Effects are facilitator artifacts.",
            "Deliberation polarizes as often as it persuades.",
            "Mini-publics can scale through institutional design.",
        ],
        confirm="Opinion shifts track threat-neutralization measures.",
        refute="Well-designed deliberation fails to shift opinions.",
    ),
    dict(
        key="political-science-06",
        name="The Democratic Peace: What Is the Mechanism",
        group="Conflict",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Democracies rarely fight each other - but why? Norms, "
                 "institutions, economics, or statistical artifact?"),
        background=("The democratic peace is the strongest empirical "
                    "regularity in international relations, yet its mechanism "
                    "is disputed: shared norms of compromise, institutional "
                    "constraints (leaders face voters), economic "
                    "interdependence, or alliance patterns. Critics note "
                    "democracies fight non-democracies readily, covert action "
                    "exceptions, and definitional stretching. The mechanism "
                    "matters because it determines whether spreading democracy "
                    "spreads peace."),
        why_it_matters=("If the mechanism is norms, peace needs culture; if "
                        "institutions, it needs design; if economics, it needs "
                        "trade. The policy implications diverge completely."),
        sig_lens=("The Signature lens treats the peace as a credibility ledger: "
                  "the Signature approach asks what lets democracies trust "
                  "each other's commitments."),
        sig_body=("The Signature proposal models the democratic peace as "
                  "audience-cost credibility. Assumptions: (1) war needs "
                  "credible commitments to avoid; (2) democratic leaders face "
                  "public punishment for bluffing; (3) this makes democratic "
                  "signals credible. Reasoning path: the proposal shows "
                  "democracies can trust each other's peaceful signals "
                  "because backing down is costly - predicting the peace "
                  "should be strongest where audience costs are highest "
                  "(competitive democracies), which matches the data. Norms "
                  "and trade then reinforce but do not create the peace. "
                  "Limits: audience-cost evidence is indirect; the model "
                  "struggles with covert-action exceptions."),
        pointer=('The Signature system models the democratic peace as audience-cost credibility, strongest where leaders face real public punishment. The Signature test: peace strength tracks audience-cost measures. It would be refuted if high-audience-cost democracies fight each other.'),
        key_points=[
            "Democracies rarely fight each other - the strongest IR regularity.",
            "Norms, institutions, and economics compete as mechanisms.",
            "Democracies fight non-democracies readily.",
            "The mechanism determines whether spreading democracy spreads peace.",
        ],
        requirements=[
            "A mechanism distinguishing democracy-democracy from mixed dyads.",
            "An account of covert-action exceptions.",
            "Testable predictions separating the rival mechanisms.",
        ],
        standards=[
            "Claims checked against the democratic-peace literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Russett B. Grasping the Democratic Peace. Princeton University Press; 1993.",
            "Rosato S. The flawed logic of democratic peace theory. American Political Science Review; 2003.",
        ],
        hypotheses=[
            "Audience-cost credibility is the core mechanism.",
            "Shared liberal norms do the work.",
            "Economic interdependence explains the pattern.",
            "The finding is definitional artifact.",
        ],
        confirm="Peace strength tracks audience-cost measures.",
        refute="High-audience-cost democracies fight each other.",
    ),
    dict(
        key="political-science-07",
        name="Why Do Civil Wars Recur",
        group="Conflict",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("Why do civil wars recur in the same countries - with "
                 "post-conflict states relapsing at alarming rates?"),
        background=("About half of civil wars recur within a decade. "
                    "Explanations: unresolved grievances, weak states, "
                    "lootable resources, neighborhood effects, and the "
                    "'conflict trap' (Collier) where war destroys the "
                    "economy that might prevent war. Peacekeeping and power-"
                    "sharing help sometimes; what distinguishes durable "
                    "peace from relapse remains unclear."),
        why_it_matters=("Civil wars kill millions and displace tens of "
                        "millions. Breaking the recurrence cycle is the "
                        "highest-stakes problem in conflict studies."),
        sig_lens=("The Signature lens treats recurrence as a trap ledger: "
                  "the Signature approach asks what war destroys that peace "
                  "needs."),
        sig_body=("The Signature proposal models recurrence as a destroyed-"
                  "capital trap. Assumptions: (1) war destroys physical, "
                  "human, and social capital; (2) peace needs that capital "
                  "to deliver dividends; (3) young men with no prospects "
                  "are recruitable. Reasoning path: the proposal shows war "
                  "lowers the opportunity cost of rebellion while raising "
                  "grievances - a trap where each war makes the next more "
                  "likely, predicting recurrence should track capital "
                  "destruction and youth unemployment, which matches the "
                  "data. Breaking the trap needs capital injection plus "
                  "credible commitment. Limits: the model underplays "
                  "ideological and ethnic drivers; commitment problems are "
                  "hard to solve."),
        pointer=('The Signature system models recurrence as a destroyed-capital trap, with each war lowering the opportunity cost of the next. The Signature test: recurrence tracks capital destruction and youth opportunity. It would be refuted if recurrence is highest where capital is intact.'),
        key_points=[
            "About half of civil wars recur within a decade.",
            "The conflict trap: war destroys the economy that prevents war.",
            "Grievance, greed, and state weakness all have support.",
            "Peacekeeping and power-sharing help inconsistently.",
        ],
        requirements=[
            "A mechanism for the recurrence rate.",
            "An account of durable-peace counterexamples.",
            "Separation of economic from ideological drivers.",
        ],
        standards=[
            "Claims checked against the civil-war literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Collier P et al. Breaking the Conflict Trap. World Bank; 2003.",
            "Walter BF. Conflict Relapse and the Sustainability of Post-Conflict Peace. 2010.",
        ],
        hypotheses=[
            "Destroyed capital plus recruitable youth drives recurrence.",
            "Unresolved grievances are primary.",
            "Lootable resources fund relapse.",
            "Credible commitment failure is the core problem.",
        ],
        confirm="Recurrence tracks capital destruction and youth opportunity.",
        refute="Recurrence is highest where capital is intact.",
    ),
    dict(
        key="political-science-08",
        name="Why Do Revolutions Succeed or Fail",
        group="Revolution",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Why do some revolutionary movements topple regimes while "
                 "most fail - and can success be predicted?"),
        background=("Structural theories (Skocpol: state breakdown plus "
                    "peasant revolt), agency theories (leadership, strategy), "
                    "and recent work on nonviolent campaigns (Chenoweth: "
                    "3.5 percent participation predicts success) compete. "
                    "Yet revolutions surprise: Tunisia 2011 succeeded where "
                    "models predicted stability; Syria's uprising became "
                    "catastrophe. The interaction of structure, strategy, "
                    "and contingency resists modeling."),
        why_it_matters=("Revolutions remake states and kill millions. "
                        "Understanding them is understanding political "
                        "change at its most extreme."),
        sig_lens=("The Signature lens treats revolution as a coordination "
                  "ledger: the Signature approach asks what lets millions "
                  "act together against armed regimes."),
        sig_body=("The Signature proposal models revolution as a preference-"
                  "cascade with a participation threshold. Assumptions: (1) "
                  "most citizens privately oppose the regime but fear acting; "
                  "(2) visible participation reduces fear; (3) regimes fall "
                  "when security forces defect. Reasoning path: the proposal "
                  "shows success follows when early movers make participation "
                  "visibly safe - the 3.5 percent finding marks the cascade "
                  "point - predicting that nonviolent discipline matters "
                  "because it maximizes participation. Structure sets the "
                  "dryness of the tinder; strategy lights it. Limits: the "
                  "model struggles with armed revolutions; contingency "
                  "remains large."),
        pointer=('The Signature system models revolution as a preference cascade, with nonviolent discipline maximizing the participation that triggers it. The Signature test: participation levels predict outcomes across cases. It would be refuted if high participation consistently fails; low participation succeeds.'),
        key_points=[
            "Structural, agency, and nonviolence theories compete.",
            "About 3.5 percent participation predicts nonviolent success.",
            "Revolutions repeatedly surprise forecasters.",
            "Security-force defection is often decisive.",
        ],
        requirements=[
            "An account of both structure and contingency.",
            "A mechanism for the participation threshold.",
            "Consistency with failed-uprising cases.",
        ],
        standards=[
            "Claims checked against the revolution literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Skocpol T. States and Social Revolutions. Cambridge University Press; 1979.",
            "Chenoweth E, Stephan MJ. Why Civil Resistance Works. Columbia University Press; 2011.",
        ],
        hypotheses=[
            "Preference cascades past participation thresholds explain success.",
            "State breakdown is the necessary structural condition.",
            "Nonviolent discipline is the decisive strategic variable.",
            "Revolutions are fundamentally unpredictable.",
        ],
        confirm="Participation levels predict outcomes across cases.",
        refute="High participation consistently fails; low participation succeeds.",
    ),
    dict(
        key="political-science-09",
        name="Why Do Some States Fail",
        group="State",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("Why do some states collapse into failure - losing the "
                 "monopoly of force and basic services - while neighbors "
                 "survive similar shocks?"),
        background=("State failure clusters in explanations: colonial "
                    "borders, resource curses, ethnic fragmentation, bad "
                    "leadership, external intervention. But similar "
                    "conditions produce survival elsewhere - Botswana versus "
                    "its neighbors, for instance. The field lacks a "
                    "predictive theory; failure indices describe more than "
                    "they explain."),
        why_it_matters=("Failed states breed war, terror, and refugee crises. "
                        "Prevention needs prediction, and prediction needs "
                        "theory."),
        sig_lens=("The Signature lens treats statehood as a bargain ledger: "
                  "the Signature approach asks what citizens get for their "
                  "compliance."),
        sig_body=("The Signature proposal models state survival as a "
                  "compliance bargain. Assumptions: (1) states need "
                  "quasi-voluntary compliance, not just coercion; (2) "
                  "compliance follows perceived fairness and service "
                  "delivery; (3) coercion alone is expensive and brittle. "
                  "Reasoning path: the proposal shows states fail when the "
                  "bargain breaks - extraction without services, or "
                  "exclusion of major groups - predicting failure should "
                  "track legitimacy collapse more than poverty or "
                  "fragmentation alone. Botswana survived because the "
                  "bargain held. Limits: legitimacy is hard to measure "
                  "prospectively; the model needs better early indicators."),
        pointer=('The Signature system models state survival as a compliance bargain, with failure tracking legitimacy collapse. The Signature test: failure follows measured legitimacy collapse. It would be refuted if high-legitimacy states fail; low-legitimacy ones endure.'),
        key_points=[
            "State failure explanations cluster but do not predict.",
            "Similar conditions produce survival and failure.",
            "Failure indices describe more than they explain.",
            "Botswana-style counterexamples challenge every theory.",
        ],
        requirements=[
            "A predictive theory, not just correlates.",
            "An account of resilient counterexamples.",
            "Early indicators of bargain breakdown.",
        ],
        standards=[
            "Claims checked against the state-failure literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rotberg RI. When States Fail. Princeton University Press; 2004.",
            "Acemoglu D, Robinson JA. Why Nations Fail. Crown; 2012.",
        ],
        hypotheses=[
            "Legitimacy-bargain breakdown predicts failure.",
            "Colonial institutional legacies determine outcomes.",
            "Leadership quality is decisive.",
            "External intervention is the main driver.",
        ],
        confirm="Failure follows measured legitimacy collapse.",
        refute="High-legitimacy states fail; low-legitimacy ones endure.",
    ),
    dict(
        key="political-science-10",
        name="The Resource Curse: Which Mechanism",
        group="Political Economy",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Why do resource-rich countries often grow slower and govern "
                 "worse - and which mechanism of the resource curse is real?"),
        background=("Oil and mineral wealth correlates with authoritarianism, "
                    "corruption, and slow growth - but Norway and Botswana "
                    "escaped. Proposed mechanisms: Dutch disease (currency "
                    "effects), rentier politics (no taxation, no "
                    "representation), volatility, and conflict over rents. "
                    "Recent work questions whether the curse is conditional "
                    "on institutions - making the mechanism debate the whole "
                    "game."),
        why_it_matters=("The curse shapes the fate of billions in resource-rich "
                        "poor countries. The mechanism determines the cure."),
        sig_lens=("The Signature lens treats resource wealth as a revenue "
                  "ledger: the Signature approach asks what changes when "
                  "rulers do not need taxpayers."),
        sig_body=("The Signature proposal models the curse as a taxation-"
                  "bargain collapse. Assumptions: (1) rulers who tax must "
                  "bargain with citizens; (2) resource rents replace "
                  "taxation; (3) without the bargain, accountability "
                  "atrophies. Reasoning path: the proposal shows the "
                  "political curse follows directly - no taxation, no "
                  "representation - predicting the curse should bite "
                  "hardest where pre-resource institutions were weakest, "
                  "which matches Norway/Botswana (strong institutions) "
                  "versus the cursed cases. The economic channels (Dutch "
                  "disease, volatility) are secondary. Limits: the model "
                  "needs pre-boom institutional measures; some cursed "
                  "states had decent institutions."),
        pointer=('The Signature system models the curse as taxation-bargain collapse: rents replace taxes, and accountability atrophies. The Signature test: curse severity tracks pre-boom institutional weakness. It would be refuted if strong-institution states suffer the full curse.'),
        key_points=[
            "Resource wealth correlates with worse governance and growth.",
            "Norway and Botswana are famous exceptions.",
            "Dutch disease, rentier, volatility, and conflict mechanisms compete.",
            "The curse may be conditional on institutions.",
        ],
        requirements=[
            "A mechanism explaining the exceptions.",
            "Separation of economic from political channels.",
            "Pre-boom institutional measures.",
        ],
        standards=[
            "Claims checked against the resource-curse literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ross ML. The Oil Curse. Princeton University Press; 2012.",
            "Sachs JD, Warner AM. Natural resource abundance and economic growth. 1995.",
        ],
        hypotheses=[
            "Taxation-bargain collapse is the core mechanism.",
            "Dutch disease drives the economic curse.",
            "Price volatility is the main channel.",
            "There is no curse, only bad institutions.",
        ],
        confirm="Curse severity tracks pre-boom institutional weakness.",
        refute="Strong-institution states suffer the full curse.",
    ),
    dict(
        key="political-science-11",
        name="Why Does Corruption Persist",
        group="Governance",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Why does corruption persist where everyone condemns it - "
                 "and why do anti-corruption reforms so often fail?"),
        background=("Corruption is universally condemned and widely "
                    "practiced. Principal-agent models prescribe monitoring "
                    "and punishment; collective-action models note that when "
                    "everyone is corrupt, honesty does not pay. Reforms "
                    "fail because they assume principals want clean agents - "
                    "but the principals are often the beneficiaries. The "
                    "persistence puzzle is really an equilibrium puzzle."),
        why_it_matters=("Corruption taxes the poor, deters investment, and "
                        "corrodes states. Breaking the equilibrium is "
                        "development's hardest problem."),
        sig_lens=("The Signature lens treats corruption as an equilibrium "
                  "ledger: the Signature approach asks what each player "
                  "gains by staying corrupt."),
        sig_body=("The Signature proposal models corruption as a stable "
                  "equilibrium, not a moral failure. Assumptions: (1) "
                  "when corruption is the norm, honest players lose; (2) "
                  "reformers face collective-action problems; (3) "
                  "beneficiaries block monitoring. Reasoning path: the "
                  "proposal shows anti-corruption fails because it targets "
                  "agents while principals benefit - predicting reforms "
                  "work only when they change the payoff structure (as in "
                  "Georgia's police reform) or when norms tip. The cure "
                  "is equilibrium shift, not moral exhortation. Limits: "
                  "the model needs measures of norm tipping points; "
                  "cultural factors resist formalization."),
        pointer=('The Signature system models corruption as a stable equilibrium, with reform requiring payoff-structure change rather than monitoring. The Signature test: reforms succeed where payoff structures change. It would be refuted if monitoring alone sustains clean government.'),
        key_points=[
            "Corruption is universally condemned, widely practiced.",
            "Principal-agent remedies assume clean principals.",
            "Collective-action models explain persistence as equilibrium.",
            "Reforms usually fail; Georgia-style successes are rare.",
        ],
        requirements=[
            "An equilibrium account of persistence.",
            "An explanation for rare reform successes.",
            "A theory of norm tipping.",
        ],
        standards=[
            "Claims checked against the corruption literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rose-Ackerman S. Corruption and Government. Cambridge University Press; 1999.",
            "Mungiu-Pippidi A. The Quest for Good Governance. Cambridge University Press; 2015.",
        ],
        hypotheses=[
            "Equilibrium payoffs, not morals, sustain corruption.",
            "Monitoring and punishment suffice if principals are clean.",
            "Norm tipping can flip equilibria rapidly.",
            "Corruption is cultural and slow to change.",
        ],
        confirm="Reforms succeed where payoff structures change.",
        refute="Monitoring alone sustains clean government.",
    ),
    dict(
        key="political-science-12",
        name="Why Do Authoritarian Regimes Survive",
        group="Authoritarianism",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Why do many authoritarian regimes survive for decades - "
                 "holding elections, tolerating some opposition - instead of "
                 "collapsing or democratizing?"),
        background=("The old totalitarian model gave way to 'competitive "
                    "authoritarianism' and 'electoral autocracy': regimes "
                    "that win rigged elections, co-opt oppositions, and "
                    "manage media. Theories: legitimation strategies, "
                    "repression-calibration, elite power-sharing, economic "
                    "performance, and international support. Yet survival "
                    "varies enormously - and breakdowns surprise."),
        why_it_matters=("Most humans live under authoritarian or hybrid "
                        "rule. Understanding durability is understanding "
                        "the modal political condition."),
        sig_lens=("The Signature lens treats authoritarianism as a "
                  "portfolio ledger: the Signature approach asks how "
                  "regimes diversify their survival bets."),
        sig_body=("The Signature proposal models regime survival as "
                  "portfolio management. Assumptions: (1) regimes face "
                  "threats from masses, elites, and outsiders; (2) no "
                  "single tool handles all three; (3) tools interact. "
                  "Reasoning path: the proposal shows durable regimes "
                  "diversify - legitimation for masses, power-sharing for "
                  "elites, repression calibrated to avoid backlash - "
                  "predicting that single-tool regimes (pure repression, "
                  "pure performance) are brittle. Breakdown follows "
                  "portfolio failure, often when economic crisis removes "
                  "the legitimation leg. Limits: the model needs "
                  "measures of each tool's strength; ideology's role is "
                  "understated."),
        pointer=('The Signature system models authoritarian durability as a diversified survival portfolio, with breakdown following portfolio failure. The Signature test: breakdown follows portfolio-leg failure. It would be refuted if single-tool regimes prove as durable as diversified ones.'),
        key_points=[
            "Many autocracies hold elections and tolerate limited opposition.",
            "Legitimation, co-optation, and calibrated repression combine.",
            "Single-tool regimes prove brittle.",
            "Breakdowns often follow economic crisis.",
        ],
        requirements=[
            "An account of the electoral-autocracy toolkit.",
            "An explanation for breakdown timing.",
            "Separation of the survival tools' contributions.",
        ],
        standards=[
            "Claims checked against the authoritarianism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Levitsky S, Way LA. Competitive Authoritarianism. Cambridge University Press; 2010.",
            "Geddes B. What do we know about democratization after twenty years? 1999.",
        ],
        hypotheses=[
            "Diversified survival portfolios explain durability.",
            "Economic performance is the load-bearing leg.",
            "Elite power-sharing is decisive.",
            "International support sustains most durable autocracies.",
        ],
        confirm="Breakdown follows portfolio-leg failure.",
        refute="Single-tool regimes prove as durable as diversified ones.",
    ),
    dict(
        key="political-science-13",
        name="The China Model: Generalizable",
        group="Authoritarianism",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("Is China's combination of authoritarian politics and "
                 "market economics a generalizable development model - or a "
                 "unique historical conjuncture?"),
        background=("China grew spectacularly under one-party rule, "
                    "challenging the modernization-theory link between "
                    "markets and democracy. Admirers see a model; skeptics "
                    "see unique conditions (size, diaspora, timing, prior "
                    "state capacity). Attempts to copy it have mostly "
                    "failed. Whether authoritarian modernization works "
                    "generally remains the debate."),
        why_it_matters=("The answer shapes development policy for billions - "
                        "and the ideological contest of the 21st century."),
        sig_lens=("The Signature lens treats the China case as a conditions "
                  "ledger: the Signature approach asks which ingredients "
                  "were necessary versus incidental."),
        sig_body=("The Signature proposal models the China outcome as a "
                  "conjuncture of rare conditions. Assumptions: (1) growth "
                  "needed state capacity, which China had; (2) it needed "
                  "global market access at the right moment; (3) it needed "
                  "a disciplined party apparatus. Reasoning path: the "
                  "proposal shows the combination - high capacity plus "
                  "market opening plus demographic dividend plus WTO timing "
                  "- is historically rare, predicting that partial copies "
                  "(markets without capacity, capacity without opening) "
                  "fail. The 'model' is then mostly non-transferable. "
                  "Limits: the model is retrospective; China's future "
                  "tests whether the combination is stable."),
        pointer=("The Signature system models China's outcome as a rare conjuncture, predicting partial copies fail. The Signature test: partial copies fail systematically. It would be refuted if a dissimilar country replicates the full combination."),
        key_points=[
            "Spectacular growth under one-party rule.",
            "Modernization theory predicted markets would bring democracy.",
            "Copy attempts have mostly failed.",
            "Unique conditions versus general model is the dispute.",
        ],
        requirements=[
            "Separation of necessary from incidental conditions.",
            "An account of the failed copies.",
            "A test for the model's future stability.",
        ],
        standards=[
            "Claims checked against the development literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Naughton B. The Chinese Economy. MIT Press; 2007.",
            "Halper S. The Beijing Consensus. Basic Books; 2010.",
        ],
        hypotheses=[
            "A rare conjuncture, mostly non-transferable.",
            "Authoritarian modernization is generally viable.",
            "State capacity, not regime type, is the key variable.",
            "The model is unstable and will democratize or stall.",
        ],
        confirm="Partial copies fail systematically.",
        refute="A dissimilar country replicates the full combination.",
    ),
    dict(
        key="political-science-14",
        name="Federalism Versus Unitary Performance",
        group="Institutions",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("Do federal systems govern better than unitary ones - and "
                 "for which tasks?"),
        background=("Federalism promises laboratories of democracy, "
                    "tailored policies, and tyranny prevention; critics "
                    "cite duplication, race-to-the-bottom, and blame "
                    "shifting. Empirical comparisons are confounded: "
                    "federal countries differ systematically (size, "
                    "diversity). Whether decentralization improves "
                    "services, growth, or democracy remains contested."),
        why_it_matters=("Constitutional designers choose between these "
                        "systems for billions. The evidence should guide "
                        "the choice."),
        sig_lens=("The Signature lens treats federalism as a matching "
                  "ledger: the Signature approach asks which tasks fit "
                  "which level."),
        sig_body=("The Signature proposal models federal performance as "
                  "task-matching. Assumptions: (1) tasks differ in scale "
                  "economies and preference heterogeneity; (2) federalism "
                  "matches heterogeneous tasks to local levels; (3) "
                  "mismatch causes the pathologies. Reasoning path: the "
                  "proposal predicts federalism outperforms where "
                  "preferences vary locally (education, policing) and "
                  "underperforms where scale dominates (defense, "
                  "macroeconomics) - explaining the mixed empirical "
                  "record as task-composition effects. Limits: the model "
                  "needs task-level outcome data; political dynamics "
                  "(blame shifting) cut across tasks."),
        pointer=('The Signature system models federal performance as task-matching, explaining mixed results as task-composition effects. The Signature test: outcomes track task-level matching predictions. It would be refuted if federalism outperforms uniformly across tasks.'),
        key_points=[
            "Federalism promises experimentation and tyranny prevention.",
            "Critics cite duplication and blame shifting.",
            "Comparisons are confounded by country differences.",
            "The empirical record is mixed.",
        ],
        requirements=[
            "Task-level outcome comparisons.",
            "An account of the confounds.",
            "Separation of design from implementation.",
        ],
        standards=[
            "Claims checked against the federalism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Riker WH. Federalism: Origin, Operation, Significance. Little Brown; 1964.",
            "Weingast BR. The economic role of political institutions. 1995.",
        ],
        hypotheses=[
            "Task-matching explains the mixed record.",
            "Federalism generally outperforms unitary rule.",
            "Unitary systems govern more effectively.",
            "Culture dominates; institutions are secondary.",
        ],
        confirm="Outcomes track task-level matching predictions.",
        refute="Federalism outperforms uniformly across tasks.",
    ),
    dict(
        key="political-science-15",
        name="The Incumbency Advantage Causes",
        group="Institutions",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Why do incumbents win reelection so disproportionately - "
                 "and how much is skill versus structural advantage?"),
        background=("Incumbents win at rates far above challengers across "
                    "democracies. Causes proposed: name recognition, "
                    "fundraising networks, constituency service, media "
                    "access, gerrymandering, and scare-off effects "
                    "(quality challengers do not run). Disentangling these "
                    "matters because the advantage may entrench mediocrity "
                    "or reward experience."),
        why_it_matters=("The incumbency advantage shapes who governs. If it "
                        "is mostly structural, elections are less "
                        "competitive than they appear."),
        sig_lens=("The Signature lens treats incumbency as a resource ledger: "
                  "the Signature approach asks what incumbents accumulate "
                  "that challengers cannot buy."),
        sig_body=("The Signature proposal models the advantage as "
                  "accumulated non-transferable capital. Assumptions: (1) "
                  "name recognition, donor networks, and casework capacity "
                  "accumulate with time; (2) challengers start at zero; (3) "
                  "scare-off compounds the gap. Reasoning path: the "
                  "proposal shows the advantage should grow with tenure "
                  "and be largest where personal vote matters (single-"
                  "member districts) - predicting the observed patterns. "
                  "Gerrymandering then amplifies but does not create the "
                  "advantage. Limits: the model needs better measures of "
                  "the personal vote; candidate quality confounds "
                  "everything."),
        pointer=('The Signature system models incumbency as accumulated non-transferable capital, with gerrymandering amplifying rather than creating it. The Signature test: advantage tracks tenure and personal-vote measures. It would be refuted if term-limited incumbents show no advantage.'),
        key_points=[
            "Incumbents win far above challenger rates.",
            "Recognition, money, service, and scare-off all contribute.",
            "The advantage grows with tenure.",
            "Gerrymandering's role is debated.",
        ],
        requirements=[
            "Disentangling the advantage's components.",
            "An account of the tenure gradient.",
            "Separation of candidate quality from structural advantage.",
        ],
        standards=[
            "Claims checked against the elections literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mayhew DR. Congress: The Electoral Connection. Yale University Press; 1974.",
            "Erikson RS. The advantage of incumbency in congressional elections. 1971.",
        ],
        hypotheses=[
            "Accumulated non-transferable capital explains the advantage.",
            "Gerrymandering is the primary driver.",
            "Candidate quality differences dominate.",
            "The advantage is mostly name recognition.",
        ],
        confirm="Advantage tracks tenure and personal-vote measures.",
        refute="Term-limited incumbents show no advantage.",
    ),
    dict(
        key="political-science-16",
        name="Do Electoral Systems Shape Everything",
        group="Institutions",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("How much do electoral rules - proportional versus majoritarian "
                 "- shape party systems, policy, and democratic quality?"),
        background=("Duverger's law links plurality rules to two-party systems "
                    "and PR to multiparty ones. Beyond party counts, scholars "
                    "claim electoral systems shape welfare states, corruption, "
                    "representation of women, and democratic satisfaction. But "
                    "electoral systems are chosen by the powerful, confounding "
                    "cause and effect - and culture may drive both rules and "
                    "outcomes."),
        why_it_matters=("Electoral reform is democracy's most available lever. "
                        "Knowing what it can and cannot change is essential."),
        sig_lens=("The Signature lens treats electoral rules as a filter "
                  "ledger: the Signature approach asks what the filter lets "
                  "through and what it blocks."),
        sig_body=("The Signature proposal models electoral systems as "
                  "mechanical filters with downstream effects. Assumptions: "
                  "(1) rules mechanically shape seat-vote translation; (2) "
                  "parties adapt strategies to the rules; (3) adaptation "
                  "propagates to policy. Reasoning path: the proposal shows "
                  "the mechanical effects (party counts, proportionality) "
                  "are strong and predictable, while downstream effects "
                  "(welfare, corruption) are mediated and weaker - "
                  "predicting reform changes party systems reliably but "
                  "policy only conditionally. Culture then moderates, not "
                  "determines. Limits: the endogeneity of rule choice "
                  "remains the fundamental identification problem."),
        pointer=('The Signature system models electoral rules as mechanical filters with strong proximate but mediated downstream effects. The Signature test: reforms change party systems as mechanically predicted. It would be refuted if identical rules produce opposite party systems.'),
        key_points=[
            "Duverger's law links rules to party-system shape.",
            "PR correlates with multiparty systems and welfare states.",
            "Rules are chosen endogenously by the powerful.",
            "Culture-versus-institutions remains disputed.",
        ],
        requirements=[
            "Causal identification despite endogenous rule choice.",
            "Separation of mechanical from downstream effects.",
            "An account of reform cases.",
        ],
        standards=[
            "Claims checked against the electoral-systems literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Duverger M. Political Parties. Wiley; 1954.",
            "Lijphart A. Patterns of Democracy. Yale University Press; 1999.",
        ],
        hypotheses=[
            "Mechanical effects are strong; downstream effects mediated.",
            "Electoral systems shape policy profoundly.",
            "Culture drives both rules and outcomes.",
            "Reform effects are mostly unpredictable.",
        ],
        confirm="Reforms change party systems as mechanically predicted.",
        refute="Identical rules produce opposite party systems.",
    ),
    dict(
        key="political-science-17",
        name="Judicial Independence: Can It Be Measured",
        group="Institutions",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Can judicial independence - courts deciding free of political "
                 "pressure - actually be measured, or do our measures just "
                 "capture formal rules?"),
        background=("De jure independence (tenure, appointment rules) often "
                    "diverges from de facto independence (actual decisions). "
                    "Measures proliferate - expert surveys, case outcomes, "
                    "text analysis - but correlate weakly. Autocrats have "
                    "learned to keep the forms while capturing the substance. "
                    "Without valid measurement, claims about courts' effects "
                    "rest on sand."),
        why_it_matters=("Courts are democracy's last guardrail. If we cannot "
                        "measure their independence, we cannot defend it."),
        sig_lens=("The Signature lens treats independence as a behavior ledger: "
                  "the Signature approach asks what courts do when rulings "
                  "hurt the powerful."),
        sig_body=("The Signature proposal models independence as revealed in "
                  "hard cases. Assumptions: (1) formal rules are cheap to "
                  "adopt; (2) true independence shows when courts rule "
                  "against incumbents; (3) case selection is strategic. "
                  "Reasoning path: the proposal shows valid measurement must "
                  "weight against-government rulings in high-stakes cases - "
                  "predicting that de facto measures based on hard cases "
                  "will diverge from de jure indices exactly where capture "
                  "is subtlest. The measure is behavioral, not "
                  "institutional. Limits: hard cases are rare; strategic "
                  "case selection biases the sample."),
        pointer=('The Signature system measures independence behaviorally, weighting rulings against incumbents in high-stakes cases. The Signature test: hard-case measures predict guardrail performance. It would be refuted if formal-rule indices predict outcomes just as well.'),
        key_points=[
            "De jure and de facto independence often diverge.",
            "Existing measures correlate weakly with each other.",
            "Autocrats preserve forms while capturing substance.",
            "Hard cases are the revealing test.",
        ],
        requirements=[
            "Behavioral measures, not just formal rules.",
            "An account of strategic case selection.",
            "Validation against known capture cases.",
        ],
        standards=[
            "Claims checked against the judicial-politics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Larkins CM. Judicial independence and democratization. 1996.",
            "Linzer DA, Staton JK. A global measure of judicial independence. 2015.",
        ],
        hypotheses=[
            "Hard-case behavior is the valid measure.",
            "Formal rules predict behavior adequately.",
            "Independence is too contextual to measure globally.",
            "Text analysis of opinions can reveal pressure.",
        ],
        confirm="Hard-case measures predict guardrail performance.",
        refute="Formal-rule indices predict outcomes just as well.",
    ),
    dict(
        key="political-science-18",
        name="Does Foreign Aid Work Politically",
        group="Political Economy",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Does foreign aid build better governance - or prop up the "
                 "bad governance it aims to fix?"),
        background=("Aid's economic effects are debated; its political effects "
                    "may be worse: budget support can relieve rulers of "
                    "taxation pressure (the aid curse), fund repression, and "
                    "distort accountability toward donors. Yet targeted aid "
                    "(health, education) shows results, and some studies find "
                    "democracy-aid works. The fungibility problem - aid "
                    "frees other money for bad uses - haunts every claim."),
        why_it_matters=("Billions in aid flow annually. Whether it helps or "
                        "harms governance decides the ethics of the "
                        "enterprise."),
        sig_lens=("The Signature lens treats aid as a revenue ledger: the "
                  "Signature approach asks whom the ruler must please to "
                  "stay funded."),
        sig_body=("The Signature proposal models aid's political effect "
                  "through the revenue bargain. Assumptions: (1) rulers "
                  "respond to whoever funds them; (2) budget aid replaces "
                  "taxation; (3) project aid is less fungible. Reasoning "
                  "path: the proposal predicts budget support harms "
                  "accountability (rulers answer to donors, not citizens) "
                  "while targeted project aid helps - explaining the mixed "
                  "record as composition effects. The policy implication: "
                  "channel determines consequence. Limits: fungibility is "
                  "hard to measure; donor motives confound the analysis."),
        pointer=('The Signature system models aid through the revenue bargain: budget aid harms accountability, project aid helps. The Signature test: accountability tracks the budget-aid share. It would be refuted if budget aid correlates with improving governance.'),
        key_points=[
            "Budget aid may relieve taxation pressure (aid curse).",
            "Fungibility lets aid free money for bad uses.",
            "Targeted health and education aid shows results.",
            "Democracy-aid findings are mixed.",
        ],
        requirements=[
            "Separation of budget from project aid effects.",
            "Fungibility measures.",
            "An account of donor-motive confounds.",
        ],
        standards=[
            "Claims checked against the aid-effectiveness literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Easterly W. The White Man's Burden. Penguin; 2006.",
            "Moyo D. Dead Aid. FSG; 2009.",
        ],
        hypotheses=[
            "Channel determines consequence: budget harms, project helps.",
            "All aid is fungible; all aid harms governance.",
            "Aid works when conditioned on governance.",
            "Aid's political effects are overstated.",
        ],
        confirm="Accountability tracks the budget-aid share.",
        refute="Budget aid correlates with improving governance.",
    ),
    dict(
        key="political-science-19",
        name="The Middle-Income Trap: Political Roots",
        group="Political Economy",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("Why do so many countries stall at middle income - and are "
                 "the causes political rather than economic?"),
        background=("The middle-income trap describes growth slowdowns after "
                    "easy catch-up gains are exhausted. Economists cite "
                    "innovation deficits and human-capital gaps; political "
                    "economists point to institutions: cronyism, weak "
                    "competition, education systems serving elites. South "
                    "Korea and Taiwan escaped; most of Latin America and "
                    "Southeast Asia did not. Whether the trap is real or a "
                    "statistical artifact is itself debated."),
        why_it_matters=("The trap, if real, condemns billions to permanent "
                        "second-tier status. Its political roots would make "
                        "it a governance problem, not a fate."),
        sig_lens=("The Signature lens treats the trap as a coalition ledger: "
                  "the Signature approach asks who benefits from the "
                  "status quo."),
        sig_body=("The Signature proposal models the trap as a political "
                  "equilibrium. Assumptions: (1) catch-up growth needs only "
                  "basic institutions; (2) innovation-led growth needs "
                  "competition, rule of law, and broad education; (3) "
                  "incumbent elites profit from the existing arrangement. "
                  "Reasoning path: the proposal shows the trap is a "
                  "coalition problem - elites who thrived on crony "
                  "catch-up block the reforms innovation needs, predicting "
                  "escape requires political disruption of the old "
                  "coalition (as in Korea and Taiwan). Economics describes "
                  "the trap; politics locks it. Limits: the model needs "
                  "better measures of elite blocking; some traps may be "
                  "purely economic."),
        pointer=('The Signature system models the trap as an elite-coalition equilibrium, with escape requiring political disruption. The Signature test: escapes follow political disruption of old coalitions. It would be refuted if countries escape with coalitions intact.'),
        key_points=[
            "Many countries stall after catch-up growth ends.",
            "Korea and Taiwan escaped; most others did not.",
            "Innovation needs competition and broad education.",
            "Whether the trap is real or artifact is debated.",
        ],
        requirements=[
            "A test distinguishing trap from normal slowdown.",
            "An account of the escape cases.",
            "Measures of elite blocking.",
        ],
        standards=[
            "Claims checked against the trap literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Gill I, Kharas H. An East Asian Renaissance. World Bank; 2007.",
            "Doner RF, Schneider BR. The middle-income trap. World Politics; 2016.",
        ],
        hypotheses=[
            "Elite coalitions lock the trap; disruption escapes it.",
            "Human-capital deficits are the primary cause.",
            "The trap is a statistical artifact.",
            "Global value-chain position determines outcomes.",
        ],
        confirm="Escapes follow political disruption of old coalitions.",
        refute="Countries escape with coalitions intact.",
    ),
    dict(
        key="political-science-20",
        name="Money in Politics: What Does It Buy",
        group="Political Economy",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("What does campaign money actually buy - votes, access, or "
                 "just the appearance of influence?"),
        background=("The US spends billions on campaigns; lobbying dwarfs even "
                    "that. Yet political science finds surprisingly weak "
                    "effects of spending on vote shares (the money paradox). "
                    "Money may buy access rather than votes, agenda-setting "
                    "rather than positions, or insurance rather than "
                    "influence. The gap between public certainty and scholarly "
                    "uncertainty is itself a puzzle."),
        why_it_matters=("Campaign finance reform rests on claims about what "
                        "money does. The evidence should discipline the "
                        "debate."),
        sig_lens=("The Signature lens treats money as an access ledger: the "
                  "Signature approach asks what donors get that non-donors "
                  "do not."),
        sig_body=("The Signature proposal models money as buying access and "
                  "agenda, not votes. Assumptions: (1) voters are hard to "
                  "persuade with ads; (2) legislators ration their time; "
                  "(3) donors buy time and attention. Reasoning path: the "
                  "proposal shows the weak vote-share effects are compatible "
                  "with strong access effects - money does not change minds, "
                  "it changes whose problems get heard, predicting policy "
                  "should track donor interests on low-salience issues where "
                  "voters are not watching. Limits: access is hard to "
                  "observe; the model needs better lobbying data."),
        pointer=('The Signature system models money as buying access and agenda on low-salience issues, not votes. The Signature test: policy tracks donor interests on low-salience issues. It would be refuted if donor access shows no policy correlation.'),
        key_points=[
            "Campaign spending shows weak effects on vote shares.",
            "Lobbying expenditures dwarf campaign spending.",
            "Access and agenda-setting are the likely channels.",
            "Public certainty exceeds scholarly certainty.",
        ],
        requirements=[
            "Separation of vote-buying from access-buying.",
            "Lobbying data linking money to policy.",
            "An account of the money paradox.",
        ],
        standards=[
            "Claims checked against the money-and-politics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ansolabehere S et al. Why is there so little money in US politics? Journal of Economic Perspectives; 2003.",
            "Gilens M. Affluence and Influence. Princeton University Press; 2012.",
        ],
        hypotheses=[
            "Money buys access and agenda, not votes.",
            "Money's effects are genuinely small.",
            "Money matters most in primaries and low-information races.",
            "The real action is in lobbying, not campaigns.",
        ],
        confirm="Policy tracks donor interests on low-salience issues.",
        refute="Donor access shows no policy correlation.",
    ),
    dict(
        key="political-science-21",
        name="Clientelism: Why Does It Persist",
        group="Political Economy",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Why does clientelism - votes traded for favors - persist "
                 "even where voters condemn it and parties promise to end "
                 "it?"),
        background=("Clientelism is widespread in young democracies and "
                    "persists in pockets of old ones. Voters often prefer "
                    "programmatic policies in surveys yet accept clientelist "
                    "deals in practice. Explanations: poverty makes the "
                    "trade rational, monitoring is hard, brokers solve "
                    "collective-action problems, and incumbents control the "
                    "resources. Breaking the equilibrium has proven "
                    "extraordinarily hard."),
        why_it_matters=("Clientelism distorts representation toward private "
                        "favors over public goods. Its persistence blocks "
                        "development."),
        sig_lens=("The Signature lens treats clientelism as a contract ledger: "
                  "the Signature approach asks why voters trust the deal."),
        sig_body=("The Signature proposal models clientelism as a credible-"
                  "commitment equilibrium. Assumptions: (1) poor voters "
                  "value certain private goods over uncertain public ones; "
                  "(2) brokers monitor compliance; (3) programmatic promises "
                  "are not credible from untrusted parties. Reasoning path: "
                  "the proposal shows the trade is rational for poor voters "
                  "given credibility constraints - predicting clientelism "
                  "fades only when parties can credibly commit to programs "
                  "or when incomes rise enough to change the calculus. "
                  "Moral condemnation misses the economics. Limits: the "
                  "model needs better measures of credibility; cultural "
                  "factors matter."),
        pointer=('The Signature system models clientelism as a rational credibility equilibrium for poor voters, fading with income or credible programs. The Signature test: clientelism fades with income or credible programmatic parties. It would be refuted if rich voters with credible alternatives still choose clientelism.'),
        key_points=[
            "Clientelism persists despite universal condemnation.",
            "Poor voters rationally prefer certain favors to uncertain programs.",
            "Brokers solve monitoring problems.",
            "Breaking the equilibrium is extraordinarily hard.",
        ],
        requirements=[
            "An account of voter rationality in the trade.",
            "A theory of equilibrium breaking.",
            "Separation of poverty from credibility effects.",
        ],
        standards=[
            "Claims checked against the clientelism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Stokes SC et al. Brokers, Voters, and Clientelism. Cambridge University Press; 2013.",
            "Kitschelt H, Wilkinson SI. Patrons, Clients, and Policies. Cambridge University Press; 2007.",
        ],
        hypotheses=[
            "Credibility-constrained rationality sustains the trade.",
            "Poverty alone explains persistence.",
            "Broker organizations are the load-bearing element.",
            "Culture, not economics, sustains clientelism.",
        ],
        confirm="Clientelism fades with income or credible programmatic parties.",
        refute="Rich voters with credible alternatives still choose clientelism.",
    ),
    dict(
        key="political-science-22",
        name="The Selectorate Theory Limits",
        group="Theory",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("How far does selectorate theory - leaders survive by "
                 "rewarding their winning coalition - actually explain, and "
                 "where does it break?"),
        background=("Bueno de Mesquita's selectorate theory elegantly predicts "
                    "that small-coalition leaders buy loyalty with private "
                    "goods and large-coalition leaders with public goods. It "
                    "organizes much of comparative politics - but critics "
                    "note it struggles with ideology, institutional detail, "
                    "leader personality, and cases where small-coalition "
                    "leaders provide public goods. Is it a general theory or "
                    "an elegant partial one?"),
        why_it_matters=("If the theory is general, much of politics reduces to "
                        "coalition arithmetic. Its limits mark where ideas "
                        "and institutions matter independently."),
        sig_lens=("The Signature lens treats the theory as a scope ledger: "
                  "the Signature approach asks where coalition logic binds "
                  "and where it bends."),
        sig_body=("The Signature proposal models selectorate logic as a "
                  "constraint, not a complete theory. Assumptions: (1) "
                  "leaders need their coalition's support; (2) coalition "
                  "size shapes goods provision; (3) ideology, institutions, "
                  "and shocks also operate. Reasoning path: the proposal "
                  "shows coalition logic sets the incentive gradient - "
                  "predicting the private-versus-public goods pattern - "
                  "while ideology and institutions determine how leaders "
                  "move along it. The theory is then a first-order "
                  "approximation, powerful but incomplete. Limits: the "
                  "model needs better coalition-size measures; the "
                  "approximation's error bounds are unknown."),
        pointer=('The Signature system treats selectorate logic as a first-order incentive gradient, with ideology and institutions determining movement along it. The Signature test: goods provision tracks coalition size across regimes. It would be refuted if coalition size shows no systematic relationship to provision.'),
        key_points=[
            "Small coalitions predict private goods; large predict public goods.",
            "The theory organizes much of comparative politics.",
            "Ideology and institutional detail challenge it.",
            "Small-coalition public-goods cases are anomalies.",
        ],
        requirements=[
            "A scope statement for the theory.",
            "An account of the anomalies.",
            "Better coalition-size measures.",
        ],
        standards=[
            "Claims checked against the selectorate literature and critics.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bueno de Mesquita B et al. The Logic of Political Survival. MIT Press; 2003.",
            "Clarke KA, Stone RW. Democracy, dictatorship, and decision. 2008.",
        ],
        hypotheses=[
            "Coalition logic is a powerful first-order approximation.",
            "Ideology systematically overrides coalition incentives.",
            "Institutions mediate everything; the theory is underspecified.",
            "The theory fails its own empirical tests.",
        ],
        confirm="Goods provision tracks coalition size across regimes.",
        refute="Coalition size shows no systematic relationship to provision.",
    ),
    dict(
        key="political-science-23",
        name="Nationalism: Why Does It Persist",
        group="Theory",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Why does nationalism persist - and resurge - in a globalized "
                 "world that was supposed to transcend it?"),
        background=("Modernization theory expected nationalism to fade; instead "
                    "it resurged across continents. Theories: nationalism as "
                    "elite invention (Gellner, Anderson), as psychological "
                    "need, as rational coordination device, as backlash to "
                    "globalization's dislocations. Each explains episodes; "
                    "none explains the persistence across such different "
                    "contexts."),
        why_it_matters=("Nationalism drives war, secession, and the politics of "
                        "the 21st century. Its persistence defeats every "
                        "prediction of its demise."),
        sig_lens=("The Signature lens treats nationalism as a coordination "
                  "ledger: the Signature approach asks what problem the "
                  "nation solves that nothing else does."),
        sig_body=("The Signature proposal models nationalism as the "
                  "largest-scale trust technology. Assumptions: (1) "
                  "large-scale cooperation needs shared identity; (2) "
                  "globalization disrupts local identities without replacing "
                  "them; (3) the nation is the biggest available "
                  "we-group. Reasoning path: the proposal shows nationalism "
                  "resurges exactly where other identities fail - predicting "
                  "its strength tracks the gap between disruption and "
                  "replacement. It persists because nothing else coordinates "
                  "at that scale. Limits: the model underplays elite "
                  "manipulation; the emotional power needs separate "
                  "accounting."),
        pointer=('The Signature system models nationalism as the largest available trust technology, resurging where other identities fail. The Signature test: nationalist strength tracks identity-disruption gaps. It would be refuted if strong alternative identities eliminate nationalism.'),
        key_points=[
            "Nationalism resurged despite globalization predictions.",
            "Elite-invention, psychological, and backlash theories compete.",
            "No account covers the full range of cases.",
            "The nation remains the largest effective we-group.",
        ],
        requirements=[
            "An account of persistence across diverse contexts.",
            "Separation of elite manipulation from popular demand.",
            "A theory of resurgence timing.",
        ],
        standards=[
            "Claims checked against the nationalism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Anderson B. Imagined Communities. Verso; 1983.",
            "Gellner E. Nations and Nationalism. Blackwell; 1983.",
        ],
        hypotheses=[
            "Nationalism is the largest-scale trust technology available.",
            "Elite invention drives each wave.",
            "Globalization backlash is the current motor.",
            "Psychological needs make it permanent.",
        ],
        confirm="Nationalist strength tracks identity-disruption gaps.",
        refute="Strong alternative identities eliminate nationalism.",
    ),
    dict(
        key="political-science-24",
        name="State Capacity: Where Does It Come From",
        group="State",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("What builds state capacity - the ability to tax, enforce, "
                 "and deliver - and can it be built deliberately?"),
        background=("State capacity predicts development, but its origins are "
                    "disputed: war-making (Tilly), colonial legacies, "
                    "geography, early bureaucratization, or political "
                    "settlements. State-building interventions (Afghanistan, "
                    "Iraq) mostly failed, suggesting capacity cannot be "
                    "installed. Yet some states built it fast (Meiji Japan, "
                    "South Korea). The recipe remains unknown."),
        why_it_matters=("Capacity is the difference between a state that "
                        "governs and one that merely rules. Building it is "
                        "development's central challenge."),
        sig_lens=("The Signature lens treats capacity as an investment ledger: "
                  "the Signature approach asks who paid to build the "
                  "bureaucracy and why."),
        sig_body=("The Signature proposal models capacity as a byproduct of "
                  "elite survival needs. Assumptions: (1) bureaucracies are "
                  "expensive; (2) elites build them when survival demands "
                  "(war, competition); (3) once built, capacity persists. "
                  "Reasoning path: the proposal shows capacity emerges "
                  "where rulers needed it to survive - predicting war, "
                  "geopolitical competition, and developmental urgency "
                  "should predict capacity, which matches the cases. "
                  "External state-building fails because it supplies the "
                  "form without the survival motive. Limits: the model "
                  "needs better historical capacity measures; peaceful "
                  "builders need separate accounting."),
        pointer=('The Signature system models capacity as a byproduct of elite survival needs, explaining why external state-building fails. The Signature test: capacity tracks survival-pressure measures historically. It would be refuted if high capacity emerges with no survival pressure.'),
        key_points=[
            "Capacity predicts development outcomes strongly.",
            "War, colonialism, and geography compete as origins.",
            "External state-building mostly failed.",
            "Meiji Japan and South Korea built capacity fast.",
        ],
        requirements=[
            "Historical capacity measures.",
            "An account of fast builders and failed interventions.",
            "Separation of capacity from regime type.",
        ],
        standards=[
            "Claims checked against the state-capacity literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Tilly C. Coercion, Capital, and European States. Blackwell; 1990.",
            "Besley T, Persson T. Pillars of Prosperity. Princeton University Press; 2011.",
        ],
        hypotheses=[
            "Elite survival needs build capacity as a byproduct.",
            "War-making is the historical engine.",
            "Colonial legacies determine capacity.",
            "Capacity can be deliberately built with right sequencing.",
        ],
        confirm="Capacity tracks survival-pressure measures historically.",
        refute="High capacity emerges with no survival pressure.",
    ),
    dict(
        key="political-science-25",
        name="Measuring the Rule of Law",
        group="Governance",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("Can the rule of law - government bound by law - be measured "
                 "validly across countries, or do indices measure something "
                 "else?"),
        background=("World Bank, World Justice Project, and other indices "
                    "rank rule of law globally, but they correlate suspiciously "
                    "with wealth, rely on expert perceptions, and may measure "
                    "liberal outcomes rather than legal constraint. Autocrats "
                    "game the formal indicators. Whether the concept travels "
                    "across legal traditions is itself disputed."),
        why_it_matters=("Rule-of-law scores drive aid, investment, and reform. "
                        "Invalid measures misdirect billions."),
        sig_lens=("The Signature lens treats the rule of law as a constraint "
                  "ledger: the Signature approach asks when law actually "
                  "binds the powerful."),
        sig_body=("The Signature proposal models rule of law as observable "
                  "constraint events. Assumptions: (1) the concept means law "
                  "binding rulers; (2) this shows in cases where rulers lose; "
                  "(3) perceptions follow events with lag. Reasoning path: "
                  "the proposal shows valid measurement must count "
                  "constraint events - adverse rulings obeyed, "
                  "expropriations reversed - predicting perception indices "
                  "will diverge from event measures where capture is "
                  "subtle. The measure is behavioral and rare-event based. "
                  "Limits: constraint events are rare; the sample problem "
                  "is severe."),
        pointer=('The Signature system measures rule of law through observable constraint events rather than perceptions. The Signature test: event measures predict outcomes perceptions miss. It would be refuted if perception indices predict constraint events well.'),
        key_points=[
            "Indices correlate suspiciously with wealth.",
            "Expert perceptions may measure liberal outcomes, not constraint.",
            "Autocrats game formal indicators.",
            "Cross-tradition validity is disputed.",
        ],
        requirements=[
            "Behavioral measures of actual constraint.",
            "Separation from wealth correlates.",
            "Validation across legal traditions.",
        ],
        standards=[
            "Claims checked against the rule-of-law literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "World Justice Project. Rule of Law Index. 2024.",
            "Ginsburg T. Pitfalls of measuring the rule of law. 2011.",
        ],
        hypotheses=[
            "Constraint events are the valid measure.",
            "Perception indices track reality adequately.",
            "The concept does not travel across traditions.",
            "De facto and de jure measures can be reconciled.",
        ],
        confirm="Event measures predict outcomes perceptions miss.",
        refute="Perception indices predict constraint events well.",
    ),
    dict(
        key="political-science-26",
        name="Why Do Sanctions (Not) Work",
        group="Conflict",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("When do economic sanctions change state behavior - and why "
                 "do they so often fail or backfire?"),
        background=("Sanctions rarely achieve their stated goals (South "
                    "Africa and Iran are debated successes; Cuba, North "
                    "Korea, Russia are not). They often rally populations "
                    "around rulers and hurt civilians most. Theories of "
                    "success invoke multilateral cooperation, targeted "
                    "'smart' sanctions, and regime-type vulnerability - but "
                    "prediction remains poor and the humanitarian costs are "
                    "real."),
        why_it_matters=("Sanctions are the West's weapon of choice short of "
                        "war. Their record determines whether they are "
                        "statecraft or cruelty."),
        sig_lens=("The Signature lens treats sanctions as a pain ledger: the "
                  "Signature approach asks who feels the pain and who "
                  "decides."),
        sig_body=("The Signature proposal models sanctions through the "
                  "pain-decision gap. Assumptions: (1) sanctions hurt "
                  "populations more than deciders; (2) rulers can shift "
                  "pain downward; (3) rally effects raise the ruler's "
                  "domestic standing. Reasoning path: the proposal shows "
                  "sanctions work only when pain reaches the decision-"
                  "making coalition - predicting broad sanctions fail "
                  "against insulated autocrats while targeted financial "
                  "measures against elite assets can bite. The humanitarian "
                  "critique follows directly. Limits: the model needs "
                  "better data on elite pain transmission; multilateral "
                  "cooperation effects are hard to isolate."),
        pointer=('The Signature system models sanctions through the pain-decision gap: they work only when pain reaches the ruling coalition. The Signature test: success tracks elite pain exposure. It would be refuted if broad sanctions succeed against insulated autocrats.'),
        key_points=[
            "Sanctions rarely achieve stated goals.",
            "Rally effects and civilian harm are documented.",
            "Targeted sanctions are theorized to work better.",
            "Multilateral cooperation is considered key.",
        ],
        requirements=[
            "A theory predicting success versus failure.",
            "Measures of pain transmission to elites.",
            "Humanitarian cost accounting.",
        ],
        standards=[
            "Claims checked against the sanctions literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hufbauer GC et al. Economic Sanctions Reconsidered. Peterson Institute; 2007.",
            "Drezner DW. The Sanctions Paradox. Cambridge University Press; 1999.",
        ],
        hypotheses=[
            "Pain must reach the decision coalition to work.",
            "Multilateral cooperation is the decisive variable.",
            "Sanctions never work; they only signal.",
            "Smart sanctions solve the humanitarian problem.",
        ],
        confirm="Success tracks elite pain exposure.",
        refute="Broad sanctions succeed against insulated autocrats.",
    ),
    dict(
        key="political-science-27",
        name="Does Peacekeeping Work",
        group="Conflict",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("Does UN peacekeeping actually keep peace - or does it go "
                 "where peace was already likely?"),
        background=("Studies find peacekeeping reduces conflict recurrence, "
                    "but selection bias haunts the finding: missions deploy "
                    "where peace is feasible. Recent work with better "
                    "identification finds real effects, especially for "
                    "protecting civilians - but missions also fail "
                    "catastrophically (Rwanda, Srebrenica), and the "
                    "mechanisms (deterrence, commitment, information) are "
                    "disputed."),
        why_it_matters=("Peacekeeping is the international community's main "
                        "conflict tool. Its effectiveness decides budgets "
                        "and lives."),
        sig_lens=("The Signature lens treats peacekeeping as a commitment "
                  "ledger: the Signature approach asks what the blue "
                  "helmets change about each side's calculations."),
        sig_body=("The Signature proposal models peacekeeping as a "
                  "commitment technology. Assumptions: (1) post-conflict "
                  "peace fails on commitment problems; (2) peacekeepers "
                  "raise the cost of surprise attack; (3) they verify "
                  "compliance. Reasoning path: the proposal shows missions "
                  "work where the binding constraint is commitment, not "
                  "where one side seeks total victory - predicting "
                  "success in stalemates and failure in ongoing wars, "
                  "which matches the record. Selection bias is then real "
                  "but not the whole story. Limits: the model needs "
                  "better mandate-strength measures; civilian protection "
                  "mechanisms need separate study."),
        pointer=('The Signature system models peacekeeping as a commitment technology that works in stalemates, not ongoing wars. The Signature test: success tracks stalemate conditions and mandate strength. It would be refuted if missions succeed equally in ongoing wars.'),
        key_points=[
            "Studies find reduced recurrence, but selection bias looms.",
            "Catastrophic failures (Rwanda, Srebrenica) scar the record.",
            "Deterrence, commitment, and information mechanisms compete.",
            "Recent identification strategies find real effects.",
        ],
        requirements=[
            "Causal identification handling selection bias.",
            "Mechanism tests separating deterrence from commitment.",
            "Mandate-strength measures.",
        ],
        standards=[
            "Claims checked against the peacekeeping literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fortna VP. Does Peacekeeping Work? Princeton University Press; 2008.",
            "Hultman L et al. UN peacekeeping and civilian protection. 2013.",
        ],
        hypotheses=[
            "Commitment technology explains the successes.",
            "Selection bias explains most of the finding.",
            "Deterrence is the main mechanism.",
            "Only robust mandates work; traditional ones do not.",
        ],
        confirm="Success tracks stalemate conditions and mandate strength.",
        refute="Missions succeed equally in ongoing wars.",
    ),
    dict(
        key="political-science-28",
        name="Democratization Waves: What Drives Them",
        group="Democracy",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Why does democratization come in waves - and what drives "
                 "each wave's rise and retreat?"),
        background=("Huntington's three waves describe global democratization "
                    "surges followed by reversals. Drivers proposed: "
                    "economic development, diffusion and demonstration "
                    "effects, international pressure, elite splits, and "
                    "hegemonic cycles. But waves are uneven - some regions "
                    "surf, others do not - and the current reverse wave "
                    "challenges every driver theory."),
        why_it_matters=("Waves are democracy's climate. Understanding them "
                        "tells us whether the current retreat is cyclical "
                        "or structural."),
        sig_lens=("The Signature lens treats waves as a contagion ledger: "
                  "the Signature approach asks what transmits across "
                  "borders and what blocks it."),
        sig_body=("The Signature proposal models waves as demonstration-"
                  "plus-structural contagion. Assumptions: (1) successful "
                  "transitions demonstrate possibility; (2) demonstration "
                  "needs receptive structures (urbanization, media, "
                  "opposition networks); (3) reversals follow when "
                  "demonstrations fail. Reasoning path: the proposal shows "
                  "waves spread where structures are receptive and stall "
                  "where they are not - predicting the Arab Spring's "
                  "uneven outcomes from pre-existing opposition strength. "
                  "The current reverse wave then reflects demonstration "
                  "failure (Iraq, Libya) plus authoritarian learning. "
                  "Limits: the model needs better structure measures; "
                  "hegemonic-cycle effects are hard to test."),
        pointer=('The Signature system models waves as demonstration contagion gated by receptive structures, with reversals following demonstration failure. The Signature test: transitions follow demonstration where structures are receptive. It would be refuted if waves occur with no demonstration or diffusion pattern.'),
        key_points=[
            "Democratization historically came in waves with reversals.",
            "Diffusion, development, and pressure compete as drivers.",
            "Waves are regionally uneven.",
            "The current reverse wave challenges driver theories.",
        ],
        requirements=[
            "A contagion mechanism with blocking conditions.",
            "An account of regional unevenness.",
            "A test for cyclical versus structural retreat.",
        ],
        standards=[
            "Claims checked against the democratization literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Huntington SP. The Third Wave. University of Oklahoma Press; 1991.",
            "Gleditsch KS, Ward MD. Diffusion and the international context of democratization. 2006.",
        ],
        hypotheses=[
            "Demonstration gated by structures explains wave patterns.",
            "Economic development is the master driver.",
            "Hegemonic cycles drive the waves.",
            "Each wave has unique causes; no general theory exists.",
        ],
        confirm="Transitions follow demonstration where structures are receptive.",
        refute="Waves occur with no demonstration or diffusion pattern.",
    ),
    dict(
        key="political-science-29",
        name="The Political Business Cycle: Real or Myth",
        group="Political Economy",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("Do politicians manipulate the economy for elections - and "
                 "can voters be fooled repeatedly?"),
        background=("Nordhaus proposed pre-election booms; rational-"
                    "expectations critics replied that voters would anticipate "
                    "manipulation. Evidence: some cycles in some countries, "
                    "none in others; central-bank independence was supposed "
                    "to end it but cycles persist in fiscal policy. Whether "
                    "the cycle is real, rational, or myth remains disputed."),
        why_it_matters=("If the cycle is real, elections distort the economy. "
                        "If myth, a major critique of democracy dissolves."),
        sig_lens=("The Signature lens treats the cycle as an expectations "
                  "ledger: the Signature approach asks what voters can see "
                  "through and what they cannot."),
        sig_body=("The Signature proposal models a conditional cycle. "
                  "Assumptions: (1) voters notice broad outcomes "
                  "(unemployment) more than instruments (deficits); (2) "
                  "politicians manipulate what voters notice least; (3) "
                  "institutions constrain instruments. Reasoning path: the "
                  "proposal predicts cycles should appear in fiscal "
                  "composition (visible spending, hidden deficits) rather "
                  "than monetary policy where central banks are independent "
                  "- matching the mixed evidence. Voters are not fooled "
                  "about outcomes; they are inattentive to instruments. "
                  "Limits: the model needs better fiscal-composition data; "
                  "competent-manipulator assumptions are strong."),
        pointer=('The Signature system models a conditional cycle in fiscal composition, where voters notice outcomes but not instruments. The Signature test: fiscal composition cycles track electoral calendars. It would be refuted if no electoral pattern in any instrument anywhere.'),
        key_points=[
            "Pre-election economic manipulation is often alleged.",
            "Rational-expectations theory says voters should anticipate it.",
            "Evidence is mixed across countries and instruments.",
            "Central-bank independence was supposed to end monetary cycles.",
        ],
        requirements=[
            "Separation of monetary from fiscal cycles.",
            "A voter-expectations account.",
            "Cross-institutional testing.",
        ],
        standards=[
            "Claims checked against the political-economy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Nordhaus WD. The political business cycle. Review of Economic Studies; 1975.",
            "Rogoff K, Sibert A. Elections and macroeconomic policy cycles. 1988.",
        ],
        hypotheses=[
            "Conditional fiscal cycles exist; monetary ones are tamed.",
            "Voter rationality eliminates all cycles.",
            "The cycle is real and broad.",
            "What looks like cycles is economic coincidence.",
        ],
        confirm="Fiscal composition cycles track electoral calendars.",
        refute="No electoral pattern in any instrument anywhere.",
    ),
    dict(
        key="political-science-30",
        name="Gender and Representation: Does It Change Policy",
        group="Behavior",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("Does electing more women change policy outcomes - or do "
                 "institutions and parties swamp individual differences?"),
        background=("Quotas spread globally; women's representation rose. "
                    "Studies find effects on health, education, and "
                    "violence-against-women policy in some contexts (India's "
                    "panchayats, Rwanda's parliament) but null effects "
                    "elsewhere. Critical-mass theory, critical-actors theory, "
                    "and institutional mediation compete. Whether descriptive "
                    "representation yields substantive representation remains "
                    "open."),
        why_it_matters=("Quotas are the most widespread institutional reform "
                        "of recent decades. Their justification depends on "
                        "the answer."),
        sig_lens=("The Signature lens treats representation as a channel "
                  "ledger: the Signature approach asks when a "
                  "representative's identity can move policy."),
        sig_body=("The Signature proposal models representation effects as "
                  "institutionally gated. Assumptions: (1) representatives "
                  "have preferences shaped partly by identity; (2) "
                  "institutions filter whose preferences become policy; (3) "
                  "agenda control matters most. Reasoning path: the proposal "
                  "predicts effects should appear where representatives "
                  "control agendas (local councils, committees) and vanish "
                  "where parties dictate (strong party discipline) - "
                  "matching the India/Rwanda positives and the nulls "
                  "elsewhere. Quotas work through positions, not just "
                  "numbers. Limits: the model needs better agenda-control "
                  "measures; preference differences themselves are "
                  "debated."),
        pointer=('The Signature system models representation effects as institutionally gated, appearing where representatives control agendas. The Signature test: policy effects track agenda-control measures. It would be refuted if no policy differences at any institutional configuration.'),
        key_points=[
            "Quotas spread globally; women's representation rose.",
            "Policy effects found in some contexts, null in others.",
            "Critical-mass versus critical-actors theories compete.",
            "Party discipline may swamp individual differences.",
        ],
        requirements=[
            "Institutional conditioning of the effects.",
            "Separation of descriptive from substantive representation.",
            "Agenda-control measures.",
        ],
        standards=[
            "Claims checked against the representation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Chattopadhyay R, Duflo E. Women as policy makers. Econometrica; 2004.",
            "Wang V. Women changing policy. 2013.",
        ],
        hypotheses=[
            "Effects are real but institutionally gated.",
            "Descriptive representation reliably yields substantive change.",
            "Party institutions swamp individual differences.",
            "Critical actors matter more than critical mass.",
        ],
        confirm="Policy effects track agenda-control measures.",
        refute="No policy differences at any institutional configuration.",
    ),
    dict(
        key="political-science-31",
        name="Media Effects: How Much Power",
        group="Behavior",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("How much do media - old and new - actually move votes and "
                 "opinions, versus merely reflecting them?"),
        background=("Minimal-effects theory dominated for decades; then came "
                    "agenda-setting, framing, and priming findings; then "
                    "social media panics about manipulation. Field "
                    "experiments find real but modest persuasion effects; "
                    "echo chambers may be overstated; disinformation's "
                    "electoral impact is debated. The field cannot agree on "
                    "the order of magnitude."),
        why_it_matters=("Media regulation, platform governance, and campaign "
                        "strategy all assume an answer. The magnitude "
                        "determines the policy."),
        sig_lens=("The Signature lens treats media as an attention ledger: "
                  "the Signature approach asks what media can make salient "
                  "versus what it can make believed."),
        sig_body=("The Signature proposal models media power as salience "
                  "without persuasion. Assumptions: (1) media strongly "
                  "shapes what people think about (agenda-setting); (2) "
                  "persuasion requires trust and repetition; (3) "
                  "partisans filter hostile messages. Reasoning path: the "
                  "proposal predicts large agenda effects but modest "
                  "persuasion effects - explaining both the panic (real "
                  "salience power) and the null findings (weak "
                  "persuasion). Disinformation then matters most for "
                  "agenda and turnout, not conversion. Limits: the model "
                  "needs better trust measures; algorithmic amplification "
                  "is understudied."),
        pointer=('The Signature system models media as powerful on salience but modest on persuasion, with disinformation mattering for agenda and turnout. The Signature test: agenda effects dwarf persuasion effects experimentally. It would be refuted if large persuasion effects appear consistently.'),
        key_points=[
            "Agenda-setting effects are large and robust.",
            "Persuasion effects are real but modest.",
            "Echo-chamber claims may be overstated.",
            "Disinformation's electoral impact is debated.",
        ],
        requirements=[
            "Separation of salience from persuasion effects.",
            "Trust and exposure measures.",
            "An account of algorithmic amplification.",
        ],
        standards=[
            "Claims checked against the media-effects literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "McCombs ME, Shaw DL. The agenda-setting function of mass media. 1972.",
            "Prior M. Post-Broadcast Democracy. Cambridge University Press; 2007.",
        ],
        hypotheses=[
            "Salience power is large; persuasion power modest.",
            "Media effects are minimal overall.",
            "Social media transformed the magnitudes.",
            "Framing effects are the main channel.",
        ],
        confirm="Agenda effects dwarf persuasion effects experimentally.",
        refute="Large persuasion effects appear consistently.",
    ),
    dict(
        key="political-science-32",
        name="Constitutional Endurance: Why Do Some Last",
        group="Institutions",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("Why do some constitutions endure for centuries while most "
                 "die young - and can endurance be designed?"),
        background=("The average constitution lasts about 19 years; the US "
                    "one is over 230. Elkins, Ginsburg, and Melton found "
                    "endurance tracks flexibility (amendment ease), "
                    "specificity, and inclusive drafting - but the US case "
                    "defies easy generalization, and endurance may reflect "
                    "the politics around the text more than the text. "
                    "Whether designers can engineer longevity is open."),
        why_it_matters=("Constitutional moments are rare and precious. If "
                        "endurance can be designed, designers need the "
                        "blueprint."),
        sig_lens=("The Signature lens treats constitutions as bargain ledgers: "
                  "the Signature approach asks whose deal the text "
                  "records."),
        sig_body=("The Signature proposal models endurance as "
                  "self-enforcing bargain. Assumptions: (1) constitutions "
                  "survive when powerful actors prefer them to the "
                  "alternative; (2) flexibility lets bargains adapt; (3) "
                  "inclusion broadens the coalition with stakes in "
                  "survival. Reasoning path: the proposal shows endurance "
                  "follows when the text records a bargain all major "
                  "players still prefer - predicting inclusive, flexible "
                  "texts outlast imposed, rigid ones. The US endured "
                  "because its bargain adapted, not because its text is "
                  "magic. Limits: the model needs better bargain "
                  "measures; some enduring texts are imposed."),
        pointer=('The Signature system models endurance as a self-enforcing bargain, with inclusive flexible texts outlasting imposed rigid ones. The Signature test: survival tracks bargain-inclusiveness measures. It would be refuted if imposed rigid texts endure as often as inclusive ones.'),
        key_points=[
            "Average constitution lasts about 19 years.",
            "Flexibility, specificity, and inclusion predict endurance.",
            "The US case is an outlier in multiple dimensions.",
            "Politics around the text may matter more than the text.",
        ],
        requirements=[
            "Bargain measures independent of survival.",
            "An account of the US outlier.",
            "Design principles testable in new constitutions.",
        ],
        standards=[
            "Claims checked against the constitutional-endurance literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Elkins Z, Ginsburg T, Melton J. The Endurance of National Constitutions. Cambridge University Press; 2009.",
            "Lutz DS. Toward a theory of constitutional amendment. 1994.",
        ],
        hypotheses=[
            "Self-enforcing bargains explain endurance.",
            "Textual design features are decisive.",
            "Endurance is mostly luck and context.",
            "Endurance can be engineered by designers.",
        ],
        confirm="Survival tracks bargain-inclusiveness measures.",
        refute="Imposed rigid texts endure as often as inclusive ones.",
    ),
    dict(
        key="political-science-33",
        name="Decentralization: Does It Help",
        group="Governance",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("Does decentralizing power to local governments improve "
                 "services and democracy - or just decentralize corruption?"),
        background=("Decentralization swept the developing world as reform "
                    "doctrine. Results are mixed: better local information "
                    "and accountability in some cases (Bolivia, Indonesia), "
                    "elite capture and fragmented services in others. "
                    "Whether decentralization helps depends on local "
                    "capacity, accountability, and fiscal design - but the "
                    "conditional theory remains incomplete."),
        why_it_matters=("Decentralization is the default reform prescription. "
                        "Its conditions of success need specifying."),
        sig_lens=("The Signature lens treats decentralization as an "
                  "accountability ledger: the Signature approach asks who "
                  "watches the local government."),
        sig_body=("The Signature proposal models decentralization as "
                  "accountability relocation. Assumptions: (1) local "
                  "governments have better information; (2) they face "
                  "weaker oversight; (3) outcomes depend on which effect "
                  "dominates. Reasoning path: the proposal predicts "
                  "decentralization helps where local accountability "
                  "(media, competition, civic groups) is strong and harms "
                  "where elites capture the local state - explaining the "
                  "Bolivia-Indonesia successes and the capture failures "
                  "as accountability differences. Fiscal design (own "
                  "revenues versus transfers) conditions everything. "
                  "Limits: the model needs local-accountability measures; "
                  "sequencing effects are understudied."),
        pointer=('The Signature system models decentralization as accountability relocation, helping where local oversight is strong. The Signature test: outcomes track local-accountability measures. It would be refuted if decentralization helps regardless of local conditions.'),
        key_points=[
            "Decentralization was adopted as reform doctrine worldwide.",
            "Results are mixed: successes and elite capture both documented.",
            "Local information versus local capture is the core tradeoff.",
            "Fiscal design conditions the outcomes.",
        ],
        requirements=[
            "Local-accountability measures.",
            "A conditional theory of success.",
            "Fiscal-design analysis.",
        ],
        standards=[
            "Claims checked against the decentralization literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Faguet JP. Decentralization and Popular Democracy. University of Michigan Press; 2012.",
            "Treisman D. The Architecture of Government. Cambridge University Press; 2007.",
        ],
        hypotheses=[
            "Local accountability determines success or failure.",
            "Decentralization generally improves services.",
            "It generally worsens governance through capture.",
            "Fiscal autonomy is the decisive variable.",
        ],
        confirm="Outcomes track local-accountability measures.",
        refute="Decentralization helps regardless of local conditions.",
    ),
    dict(
        key="political-science-34",
        name="A General Theory of Politics",
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can political science produce a general theory - covering "
                 "democracy, autocracy, war, and economy in one framework - "
                 "or is politics permanently fragmented?"),
        background=("Selectorate theory, institutionalism, behavioralism, "
                    "and political economy each illuminate parts. Attempts "
                    "at grand theory (Easton's systems, grand rational "
                    "choice) faded. The field rewards mid-range theory and "
                    "empirical work. Whether a unified framework is possible "
                    "or even desirable remains political science's "
                    "foundational question."),
        why_it_matters=("This is the discipline's capstone: the answer "
                        "determines what political science is and what it "
                        "can become."),
        sig_lens=("The Signature lens treats the fragmentation as a levels "
                  "ledger: the Signature approach asks what each level of "
                  "politics needs that others cannot supply."),
        sig_body=("The Signature proposal models politics as nested "
                  "bargains. Assumptions: (1) all politics involves "
                  "bargaining over power and resources; (2) bargains nest "
                  "(individual, group, institutional, international); (3) "
                  "each level has emergent properties. Reasoning path: "
                  "the proposal shows a general theory is possible as a "
                  "theory of nested bargaining - with selectorate logic "
                  "at the leader level, institutionalism at the rules "
                  "level, and so on - unified by the bargain concept "
                  "rather than one mechanism. Generality comes from "
                  "architecture, not reduction. Limits: the framework is "
                  "programmatic; its predictions need development."),
        pointer=('The Signature system proposes nested bargaining as the unifying architecture, with generality from structure rather than reduction. The Signature test: nested-bargain models predict across levels. It would be refuted if levels prove irreducible to any common framework.'),
        key_points=[
            "Mid-range theories dominate; grand theory faded.",
            "Each paradigm illuminates what others miss.",
            "The field rewards empirical over theoretical work.",
            "Whether unification is possible is foundational.",
        ],
        requirements=[
            "A framework spanning levels of politics.",
            "Testable predictions from the unified picture.",
            "An account of each paradigm's domain.",
        ],
        standards=[
            "Claims checked against the theoretical literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Easton D. A Systems Analysis of Political Life. Wiley; 1965.",
            "Bueno de Mesquita B et al. The Logic of Political Survival. MIT Press; 2003.",
        ],
        hypotheses=[
            "Nested bargaining unifies the field architecturally.",
            "No general theory is possible or needed.",
            "One paradigm will eventually absorb the rest.",
            "Formal modeling will provide the unification.",
        ],
        confirm="Nested-bargain models predict across levels.",
        refute="Levels prove irreducible to any common framework.",
    ),
]
