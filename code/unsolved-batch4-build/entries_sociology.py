#!/usr/bin/env python3
"""Entries for the Unsolved Sociology databases (batch 4).

34 famous open problems in sociology, ladder-ordered by accessibility.
ID prefixes: JAH-USSO- (public) and JAH-USSOS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="sociology-01",
        name="The Secularization Puzzle",
        group="Culture",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Is religion really declining with modernity - and why is "
                 "the United States so religious and Europe so secular?"),
        background=("Classical secularization theory predicted modernity "
                    "would kill religion. Europe secularized; the US stayed "
                    "devout; much of the world grew more religious. Revised "
                    "theories invoke existential security (Norris and "
                    "Inglehart), religious markets (Stark), and state "
                    "regulation. The American-European divergence remains "
                    "the central anomaly."),
        why_it_matters=("Secularization was sociology's founding prediction. "
                        "Its fate decides whether the discipline's core "
                        "theory survives."),
        sig_lens=("The Signature lens treats religion as a security ledger: "
                  "the Signature approach asks what people need that "
                  "religion provides."),
        sig_body=("The Signature proposal models religiosity as a function "
                  "of existential security plus supply. Assumptions: (1) "
                  "insecurity raises demand for meaning and community; (2) "
                  "religious markets supply it where unregulated; (3) "
                  "welfare states supply security directly. Reasoning path: "
                  "the proposal shows Europe secularized where welfare "
                  "states delivered security, while American insecurity "
                  "(inequality, weak safety nets) sustains demand - and "
                  "America's unregulated religious market supplies it "
                  "vibrantly. Both theories are then half right. Limits: "
                  "the model struggles with highly religious poor "
                  "societies with strong states; measurement of "
                  "religiosity is contested."),
        pointer=('The Signature system models religiosity as existential insecurity times religious-market supply, explaining the US-Europe split. The Signature test: religiosity tracks insecurity where markets are free. It would be refuted if secure societies with free markets stay highly religious.'),
        key_points=[
            "Europe secularized; the US stayed religious; much of the world did not secularize.",
            "Existential security and religious markets are the rival theories.",
            "The American-European divergence is the central anomaly.",
            "Religiosity measurement itself is contested.",
        ],
        requirements=[
            "An account of the US-Europe divergence.",
            "Separation of demand from supply factors.",
            "Valid cross-national religiosity measures.",
        ],
        standards=[
            "Claims checked against the secularization literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Norris P, Inglehart R. Sacred and Secular. Cambridge University Press; 2004.",
            "Stark R, Finke R. Acts of Faith. University of California Press; 2000.",
        ],
        hypotheses=[
            "Security plus supply explains the patterns.",
            "Religious markets alone explain it.",
            "Secularization is a European exception, not a rule.",
            "Modernity transforms rather than kills religion.",
        ],
        confirm="Religiosity tracks insecurity where markets are free.",
        refute="Secure societies with free markets stay highly religious.",
    ),
    dict(
        key="sociology-02",
        name="The Decline of Social Capital",
        group="Culture",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Is social capital - trust, networks, civic participation - "
                 "really declining, and what is replacing it?"),
        background=("Putnam's Bowling Alone documented falling civic "
                    "participation in America. Critics reply that "
                    "participation moved online, that the decline is "
                    "generational not societal, and that new forms (gaming "
                    "guilds, online communities) build real capital. Whether "
                    "digital ties substitute for bowling leagues remains "
                    "the open question."),
        why_it_matters=("Social capital predicts health, democracy, and "
                        "prosperity. Its fate is society's fate."),
        sig_lens=("The Signature lens treats social capital as a portfolio "
                  "ledger: the Signature approach asks what forms replaced "
                  "the old ones."),
        sig_body=("The Signature proposal models a transformation, not a "
                  "decline. Assumptions: (1) people still need belonging "
                  "and reciprocity; (2) the forms follow opportunity "
                  "structures; (3) digital ties differ in kind. Reasoning "
                  "path: the proposal shows bridging capital (diverse, "
                  "civic) declined while bonding capital (like-minded, "
                  "online) grew - predicting the observed pattern of "
                  "loneliness amid connectivity. The crisis is then "
                  "compositional: we replaced bridges with bunkers. "
                  "Limits: the model needs better digital-capital "
                  "measures; generational effects confound the trends."),
        pointer=('The Signature system models a compositional shift: bridging capital fell while bonding capital grew, producing loneliness amid connectivity. The Signature test: bridging measures fall while bonding measures rise. It would be refuted if all forms of social capital prove stable.'),
        key_points=[
            "Civic participation fell in America per Putnam.",
            "Participation may have moved online.",
            "Bridging versus bonding capital behave differently.",
            "Loneliness rose amid connectivity.",
        ],
        requirements=[
            "Measures of digital social capital.",
            "Separation of generational from societal change.",
            "An account of bridging versus bonding trends.",
        ],
        standards=[
            "Claims checked against the social-capital literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Putnam RD. Bowling Alone. Simon and Schuster; 2000.",
            "Paxton P. Is social capital declining in the United States? 1999.",
        ],
        hypotheses=[
            "Composition shifted from bridging to bonding capital.",
            "Genuine decline across all forms.",
            "Digital ties fully substitute for old forms.",
            "The decline is generational and will reverse.",
        ],
        confirm="Bridging measures fall while bonding measures rise.",
        refute="All forms of social capital prove stable.",
    ),
    dict(
        key="sociology-03",
        name="The Culture of Poverty Debate",
        group="Culture",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("Does a 'culture of poverty' - values and behaviors that "
                 "perpetuate deprivation - exist, or is the concept "
                 "victim-blaming?"),
        background=("Oscar Lewis proposed that poverty generates a "
                    "self-perpetuating culture; critics called it blaming "
                    "the victim. The debate revived with work on scarcity "
                    "psychology (Mullainathan and Shafir: poverty taxes "
                    "bandwidth) and neighborhood effects. The current "
                    "question is precise: do cultural adaptations to "
                    "poverty exist independently of the conditions that "
                    "create them?"),
        why_it_matters=("The answer determines whether anti-poverty policy "
                        "should change conditions, culture, or both - and "
                        "whether the concept itself does harm."),
        sig_lens=("The Signature lens treats the debate as an adaptation "
                  "ledger: the Signature approach asks which behaviors "
                  "are rational responses to scarcity."),
        sig_body=("The Signature proposal models poverty behaviors as "
                  "scarcity adaptations. Assumptions: (1) scarcity taxes "
                  "cognitive bandwidth; (2) adaptations that help under "
                  "scarcity can persist; (3) culture transmits successful "
                  "adaptations. Reasoning path: the proposal shows the "
                  "observed patterns - present orientation, distrust of "
                  "institutions - are rational under chronic scarcity, "
                  "predicting they should fade when scarcity lifts (as "
                  "Moving to Opportunity partly showed). 'Culture' is "
                  "then real but derivative: change the conditions with "
                  "sustained security, and the culture follows. Limits: "
                  "the model needs long-horizon data; some adaptations "
                  "may persist independently."),
        pointer=('The Signature system models poverty behaviors as rational scarcity adaptations that fade when scarcity lifts. The Signature test: behaviors fade when scarcity is durably lifted. It would be refuted if behaviors persist generations after conditions change.'),
        key_points=[
            "Lewis proposed a self-perpetuating culture of poverty.",
            "Critics called it victim-blaming.",
            "Scarcity psychology shows poverty taxes bandwidth.",
            "Neighborhood-effect studies show context matters.",
        ],
        requirements=[
            "Separation of adaptation from independent culture.",
            "Long-horizon data on scarcity removal.",
            "An account of persistence mechanisms.",
        ],
        standards=[
            "Claims checked against the poverty literature; stigma avoided.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Lewis O. La Vida. Random House; 1966.",
            "Mullainathan S, Shafir E. Scarcity. Times Books; 2013.",
        ],
        hypotheses=[
            "Behaviors are scarcity adaptations; they fade with security.",
            "An independent culture of poverty exists and persists.",
            "Structural conditions fully explain the patterns.",
            "The concept itself is harmful and should be abandoned.",
        ],
        confirm="Behaviors fade when scarcity is durably lifted.",
        refute="Behaviors persist generations after conditions change.",
    ),
    dict(
        key="sociology-04",
        name="Homophily Versus Influence",
        group="Networks",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("When friends resemble each other, is it homophily (birds "
                 "of a feather flock together) or influence (friends make "
                 "each other similar)?"),
        background=("Network studies constantly face this confounding: "
                    "obese friends, happy friends, voting friends - "
                    "selection or contagion? Shalizi and Thomas proved the "
                    "two are generically confounded in observational data. "
                    "Natural experiments and randomized trials help, but "
                    "most network findings cannot separate the mechanisms - "
                    "undermining claims about social contagion."),
        why_it_matters=("The answer determines whether networks spread "
                        "behaviors (target the network) or merely sort "
                        "people (target individuals)."),
        sig_lens=("The Signature lens treats the problem as an "
                  "identification ledger: the Signature approach asks "
                  "what design could ever separate the twins."),
        sig_body=("The Signature proposal models homophily and influence "
                  "as jointly operating with separable signatures. "
                  "Assumptions: (1) both mechanisms operate simultaneously; "
                  "(2) they leave different temporal signatures (selection "
                  "precedes tie formation; influence follows it); (3) "
                  "exogenous shocks break the symmetry. Reasoning path: "
                  "the proposal shows longitudinal data with tie-formation "
                  "timestamps can separate the mechanisms - predicting "
                  "that influence effects should appear after tie "
                  "formation controlling for prior similarity. Most "
                  "claimed contagion findings then shrink but do not "
                  "vanish. Limits: the data requirements are severe; "
                  "most existing studies cannot be salvaged."),
        pointer=('The Signature system separates the mechanisms through tie-formation timestamps, with influence appearing after ties form. The Signature test: influence effects survive timestamp controls. It would be refuted if no influence effect survives proper identification.'),
        key_points=[
            "Homophily and influence are generically confounded.",
            "Shalizi and Thomas proved the identification problem.",
            "Most contagion claims cannot separate the mechanisms.",
            "Longitudinal data with timestamps can help.",
        ],
        requirements=[
            "Tie-formation timestamps in network data.",
            "Exogenous shocks for identification.",
            "Reanalysis of classic contagion findings.",
        ],
        standards=[
            "Claims checked against the network literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Shalizi CR, Thomas AC. Homophily and contagion are generically confounded. 2011.",
            "Christakis NA, Fowler JH. The spread of obesity in a large social network. NEJM; 2007.",
        ],
        hypotheses=[
            "Timestamped longitudinal data separates the mechanisms.",
            "Most contagion findings are homophily artifacts.",
            "Both operate; influence is real but smaller than claimed.",
            "The mechanisms are inseparable even in principle.",
        ],
        confirm="Influence effects survive timestamp controls.",
        refute="No influence effect survives proper identification.",
    ),
    dict(
        key="sociology-05",
        name="How Do Networks Spread Behaviors",
        group="Networks",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("Why do some behaviors cascade through networks while "
                 "identical-seeming ones fizzle - and what makes a "
                 "contagion complex?"),
        background=("Simple contagions (disease, information) need one "
                    "contact; complex contagions (behaviors, norms) need "
                    "multiple reinforcing contacts (Centola). Network "
                    "structure matters: clustered networks spread complex "
                    "contagions better, random networks spread simple ones. "
                    "But predicting which behaviors are complex, and "
                    "designing networks for spread, remains more art than "
                    "science."),
        why_it_matters=("Behavior change at scale - health, politics, "
                        "innovation - runs through networks. The spread "
                        "rules are the levers."),
        sig_lens=("The Signature lens treats spread as a threshold ledger: "
                  "the Signature approach asks how many friends it takes "
                  "to change a mind."),
        sig_body=("The Signature proposal models adoption as a "
                  "reinforcement-threshold process. Assumptions: (1) "
                  "behaviors carry social risk; (2) risk falls with each "
                  "adopting contact; (3) thresholds vary by behavior and "
                  "person. Reasoning path: the proposal shows complex "
                  "contagions need clustered networks because only "
                  "clusters deliver multiple simultaneous exposures - "
                  "predicting that health behaviors spread through "
                  "tight-knit communities while information spreads "
                  "through broadcast networks. Intervention design then "
                  "follows: match the network to the contagion type. "
                  "Limits: threshold heterogeneity is hard to measure; "
                  "online networks blur the structures."),
        pointer=('The Signature system models adoption as reinforcement thresholds, with clustered networks spreading complex contagions. The Signature test: spread success tracks network-contagion matching. It would be refuted if network structure shows no systematic effect on spread.'),
        key_points=[
            "Simple contagions need one contact; complex need several.",
            "Clustered networks favor complex contagion.",
            "Centola's experiments demonstrated the difference.",
            "Predicting contagion type remains difficult.",
        ],
        requirements=[
            "A predictive theory of contagion complexity.",
            "Threshold measures for real behaviors.",
            "Network designs for intended spread.",
        ],
        standards=[
            "Claims checked against the diffusion literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Centola D. How Behavior Spreads. Princeton University Press; 2018.",
            "Granovetter M. Threshold models of collective behavior. 1978.",
        ],
        hypotheses=[
            "Reinforcement thresholds plus network structure explain spread.",
            "Influencer targeting beats network design.",
            "Content properties dominate network properties.",
            "Online networks have changed the rules fundamentally.",
        ],
        confirm="Spread success tracks network-contagion matching.",
        refute="Network structure shows no systematic effect on spread.",
    ),
    dict(
        key="sociology-06",
        name="The Strength of Weak Ties: Limits",
        group="Networks",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Where does Granovetter's 'strength of weak ties' hold - "
                 "and where do strong ties matter more?"),
        background=("Weak ties bridge communities, carrying novel "
                    "information (jobs); strong ties carry trust and "
                    "support. The theory is among sociology's most cited "
                    "- but its boundaries are fuzzy: weak ties help job "
                    "seekers but may not help the poorest; strong ties "
                    "matter for emotional support and risky activism. "
                    "When each tie type wins remains underspecified."),
        why_it_matters=("The theory guides everything from job programs to "
                        "organizing. Its limits determine when to build "
                        "bridges versus deepen bonds."),
        sig_lens=("The Signature lens treats ties as a resource ledger: the "
                  "Signature approach asks what each tie type delivers "
                  "that the other cannot."),
        sig_body=("The Signature proposal models tie value as "
                  "resource-specific. Assumptions: (1) weak ties deliver "
                  "novel information; (2) strong ties deliver trust, "
                  "support, and enforcement; (3) needs vary by situation. "
                  "Reasoning path: the proposal predicts weak ties win "
                  "for information problems (job search) while strong "
                  "ties win for commitment problems (activism, care) - "
                  "explaining why the theory's successes cluster in "
                  "labor markets. The poor may lack the weak ties that "
                  "carry opportunity. Limits: the model needs better "
                  "measures of tie content; digital weak ties may "
                  "behave differently."),
        pointer=('The Signature system models tie value as resource-specific: weak ties for information, strong ties for commitment. The Signature test: tie-type advantage tracks resource type. It would be refuted if weak ties outperform even for commitment problems.'),
        key_points=[
            "Weak ties bridge communities with novel information.",
            "Strong ties carry trust and support.",
            "The theory's successes cluster in labor markets.",
            "Boundaries of applicability remain fuzzy.",
        ],
        requirements=[
            "A resource-specific theory of tie value.",
            "Measures of tie content, not just structure.",
            "An account of digital weak ties.",
        ],
        standards=[
            "Claims checked against the networks literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Granovetter M. The strength of weak ties. American Journal of Sociology; 1973.",
            "Granovetter M. Getting a Job. Harvard University Press; 1974.",
        ],
        hypotheses=[
            "Resource-specificity bounds the theory correctly.",
            "Weak ties dominate across all domains.",
            "Strong ties matter more than the literature admits.",
            "Digital networks have rewritten the rules.",
        ],
        confirm="Tie-type advantage tracks resource type.",
        refute="Weak ties outperform even for commitment problems.",
    ),
    dict(
        key="sociology-07",
        name="Why Did Crime Fall in the 90s",
        group="Deviance",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("Why did violent crime fall by half in the US during the "
                 "1990s - and why did experts fail to predict it?"),
        background=("The great crime drop surprised everyone; experts had "
                    "predicted a bloodbath. Candidate causes: mass "
                    "incarceration, policing innovations, lead removal, "
                    "abortion legalization (Donohue-Levitt), crack epidemic "
                    "burnout, economic boom, demographics. Each explains "
                    "part; the weights are fiercely disputed, and the "
                    "international pattern (drops without US policies) "
                    "challenges American explanations."),
        why_it_matters=("The answer determines crime policy: if lead removal "
                        "did it, environmental policy is crime policy; if "
                        "incarceration did it, the costs were enormous."),
        sig_lens=("The Signature lens treats the drop as an attribution "
                  "ledger: the Signature approach asks what varied "
                  "across the countries that all saw drops."),
        sig_body=("The Signature proposal models the drop as multi-causal "
                  "with lead as the common thread. Assumptions: (1) many "
                  "countries saw drops without US policies; (2) lead "
                  "exposure fell globally on similar timelines; (3) lead "
                  "impairs impulse control. Reasoning path: the proposal "
                  "shows the international pattern isolates the common "
                  "cause - lead removal - while US-specific factors "
                  "(incarceration, policing) explain the US margin above "
                  "the common trend. Attribution then follows the "
                  "variation. Limits: lead-crime causality is "
                  "ecological; the weights remain estimated."),
        pointer=('The Signature system attributes the common international drop to lead removal, with US policies explaining the American margin. The Signature test: crime drops track lead-removal timelines internationally. It would be refuted if countries without lead removal show identical drops.'),
        key_points=[
            "Violent crime halved in the 1990s, surprising experts.",
            "Many countries saw drops without US policies.",
            "Lead, incarceration, policing, abortion, and crack-burnout compete.",
            "Attribution weights are fiercely disputed.",
        ],
        requirements=[
            "An account of the international pattern.",
            "Causal (not ecological) evidence on lead.",
            "Weights for the competing causes.",
        ],
        standards=[
            "Claims checked against the criminology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Zimring FE. The Great American Crime Decline. Oxford University Press; 2007.",
            "Nevin R. How lead exposure relates to temporal changes in IQ and crime. 2007.",
        ],
        hypotheses=[
            "Lead removal is the common cause; US policies add the margin.",
            "Mass incarceration did most of the work.",
            "Policing innovations were decisive.",
            "The crack epidemic's burnout explains the timing.",
        ],
        confirm="Crime drops track lead-removal timelines internationally.",
        refute="Countries without lead removal show identical drops.",
    ),
    dict(
        key="sociology-08",
        name="The Marriage Decline",
        group="Family",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Why has marriage declined - delayed, foregone, replaced by "
                 "cohabitation - and what are the consequences?"),
        background=("Marriage rates fell across rich countries; age at first "
                    "marriage rose sharply. Explanations: women's economic "
                    "independence, the disappearing marriageable-man "
                    "(Wilson), cultural individualization, housing costs, "
                    "and the decoupling of marriage from childbearing. "
                    "The class divide is stark: college graduates still "
                    "marry; the less educated increasingly do not."),
        why_it_matters=("Marriage shapes child outcomes, inequality, and "
                        "the social fabric. Its decline concentrates "
                        "advantage."),
        sig_lens=("The Signature lens treats marriage as a bargain ledger: "
                  "the Signature approach asks what each partner gains "
                  "that singlehood cannot provide."),
        sig_body=("The Signature proposal models marriage as a "
                  "specialization bargain under changing terms. "
                  "Assumptions: (1) marriage historically pooled income "
                  "and specialized labor; (2) women's earnings changed "
                  "the gains; (3) marriage now requires economic "
                  "prerequisites. Reasoning path: the proposal shows "
                  "marriage persists where the bargain still pays - the "
                  "educated, who pool high incomes - and fades where "
                  "men's economic prospects collapsed, predicting the "
                  "class divide exactly. Culture follows economics with "
                  "a lag. Limits: the model underplays the cultural "
                  "devaluation of marriage; same-sex marriage expansion "
                  "complicates the bargain story."),
        pointer=("The Signature system models marriage as a specialization bargain whose terms changed with women's earnings, predicting the class divide. The Signature test: marriage tracks the economic bargain gradient. It would be refuted if marriage falls equally where the bargain still pays."),
        key_points=[
            "Marriage delayed and declined across rich countries.",
            "The class divide is stark: graduates marry, others less so.",
            "Women's independence and male economic decline compete as causes.",
            "Cohabitation replaced much marriage functionally.",
        ],
        requirements=[
            "An account of the class gradient.",
            "Separation of economic from cultural causes.",
            "Consequence measures for children and inequality.",
        ],
        standards=[
            "Claims checked against the family-demography literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wilson WJ. The Truly Disadvantaged. University of Chicago Press; 1987.",
            "Cherlin AJ. The Marriage-Go-Round. Knopf; 2009.",
        ],
        hypotheses=[
            "Changed bargain terms explain the class-divided decline.",
            "Cultural individualization is the primary driver.",
            "Male economic decline is the main cause.",
            "Housing and precarity block family formation.",
        ],
        confirm="Marriage tracks the economic bargain gradient.",
        refute="Marriage falls equally where the bargain still pays.",
    ),
    dict(
        key="sociology-09",
        name="The Bystander Effect: How Real",
        group="Behavior",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("How real is the bystander effect - and did the Kitty "
                 "Genovese story that founded it ever happen as told?"),
        background=("The 1964 Genovese murder supposedly saw 38 witnesses "
                    "do nothing; later reporting showed the story was "
                    "exaggerated. Lab experiments confirmed diffusion of "
                    "responsibility, but field replications are mixed, and "
                    "recent work finds intervention is common - especially "
                    "with clear emergencies and competent bystanders. The "
                    "textbook phenomenon may be smaller and more "
                    "conditional than taught."),
        why_it_matters=("The bystander effect is sociology's most famous "
                        "finding. Its true size determines what we teach "
                        "about human nature."),
        sig_lens=("The Signature lens treats helping as a clarity ledger: "
                  "the Signature approach asks what bystanders need to "
                  "know before acting."),
        sig_body=("The Signature proposal models intervention as a "
                  "clarity-threshold process. Assumptions: (1) helping "
                  "needs emergency recognition; (2) recognition needs "
                  "clear cues; (3) crowds obscure cues. Reasoning path: "
                  "the proposal predicts the effect appears exactly where "
                  "ambiguity is high - explaining both the lab findings "
                  "(ambiguous situations) and the field nulls (clear "
                  "emergencies get help). The Genovese myth then inflated "
                  "a conditional effect into a law of apathy. Limits: "
                  "the model needs better field data; danger and "
                  "competence also gate helping."),
        pointer=('The Signature system models helping as a clarity threshold: the effect appears where ambiguity is high, not as a law of apathy. The Signature test: intervention tracks emergency clarity in field data. It would be refuted if clear emergencies still show strong bystander inhibition.'),
        key_points=[
            "The Genovese story was substantially exaggerated.",
            "Lab experiments confirmed diffusion of responsibility.",
            "Field replications are mixed; intervention is often common.",
            "Ambiguity, danger, and competence condition helping.",
        ],
        requirements=[
            "Separation of myth from measured effect.",
            "Field data on real emergencies.",
            "A conditional theory of intervention.",
        ],
        standards=[
            "Claims checked against the bystander literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Darley JM, Latane B. Bystander intervention in emergencies. Journal of Personality and Social Psychology; 1968.",
            "Fischer P et al. The bystander-effect: a meta-analytic review. 2011.",
        ],
        hypotheses=[
            "The effect is real but conditional on ambiguity.",
            "The textbook effect is mostly myth.",
            "Danger, not diffusion, is the main inhibitor.",
            "Modern surveillance has changed the dynamics.",
        ],
        confirm="Intervention tracks emergency clarity in field data.",
        refute="Clear emergencies still show strong bystander inhibition.",
    ),
    dict(
        key="sociology-10",
        name="The Fundamental Cause of Health Inequality",
        group="Inequality",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Why do health inequalities by class and race persist even "
                 "as diseases change - the fundamental-cause puzzle?"),
        background=("Link and Phelan proposed that social conditions are "
                    "'fundamental causes': when one disease is cured, "
                    "advantage finds new pathways (knowledge, money, "
                    "connections, prestige). Smoking, then obesity, then "
                    "COVID - the gradient persists across changing "
                    "mechanisms. Critics ask whether the theory is "
                    "unfalsifiable: what would disprove a cause that "
                    "works through any mechanism?"),
        why_it_matters=("If the theory is right, medical progress alone "
                        "cannot close health gaps - only social change "
                        "can."),
        sig_lens=("The Signature lens treats advantage as a flexible-"
                  "resource ledger: the Signature approach asks what "
                  "money, knowledge, and connections buy in each era."),
        sig_body=("The Signature proposal models health inequality as "
                  "resource-flexibility in action. Assumptions: (1) "
                  "flexible resources (money, knowledge, prestige, "
                  "connections) can be deployed against any health "
                  "threat; (2) new threats appear continuously; (3) "
                  "deploying resources requires agency the disadvantaged "
                  "lack. Reasoning path: the proposal predicts the "
                  "gradient should persist across disease eras but vary "
                  "with the preventability of each disease - which "
                  "matches the data (highly preventable diseases show "
                  "steeper gradients). The theory is then falsifiable: "
                  "unpreventable diseases should show no gradient. "
                  "Limits: the model needs better resource measures; "
                  "the preventability test is partial."),
        pointer=("The Signature system models health gaps as flexible resources deployed against each era's threats, predicting steeper gradients for preventable diseases. The Signature test: gradients track disease preventability. It would be refuted if unpreventable diseases show equally steep gradients."),
        key_points=[
            "Health gradients persist across changing diseases.",
            "Fundamental-cause theory invokes flexible resources.",
            "Critics charge unfalsifiability.",
            "Preventable diseases show steeper gradients.",
        ],
        requirements=[
            "Falsifiable predictions from the theory.",
            "Resource measures independent of outcomes.",
            "An account of gradient variation by disease.",
        ],
        standards=[
            "Claims checked against the health-inequality literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Link BG, Phelan J. Social conditions as fundamental causes of disease. Journal of Health and Social Behavior; 1995.",
            "Phelan JC et al. Fundamental causes of health inequalities. 2010.",
        ],
        hypotheses=[
            "Flexible resources explain the persistent gradient.",
            "The theory is unfalsifiable as stated.",
            "Specific mechanisms, not fundamental causes, do the work.",
            "Healthcare access differences explain most of the gradient.",
        ],
        confirm="Gradients track disease preventability.",
        refute="Unpreventable diseases show equally steep gradients.",
    ),
    dict(
        key="sociology-11",
        name="Social Mobility: How Stuck Are We",
        group="Inequality",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("How much social mobility actually exists - and why do "
                 "Americans overestimate it while Europeans underestimate "
                 " theirs?"),
        background=("Chetty's work showed the American Dream is geographically "
                    "variable: some places offer high mobility, others "
                    "almost none. Absolute mobility fell (90 percent of "
                    "1940s children out-earned parents; 50 percent today). "
                    "Relative mobility is lower in the US than Scandinavia. "
                    "What drives place effects - schools, segregation, "
                    "social capital, family structure - is the open "
                    "question."),
        why_it_matters=("Mobility is the moral core of market societies. Its "
                        "geography determines where opportunity lives."),
        sig_lens=("The Signature lens treats mobility as a place ledger: "
                  "the Signature approach asks what high-mobility places "
                  "have that low-mobility ones lack."),
        sig_body=("The Signature proposal models mobility as an ecology "
                  "of childhood. Assumptions: (1) adult outcomes reflect "
                  "childhood environments cumulatively; (2) places differ "
                  "in schools, segregation, capital, and norms; (3) "
                  "families cannot fully offset place. Reasoning path: "
                  "the proposal shows place effects compound - good "
                  "schools plus integration plus social capital multiply "
                  "- predicting the observed geographic variance and the "
                  "childhood-exposure gradients Chetty found. Mobility "
                  "policy then means place policy. Limits: the model "
                  "needs causal place-effect identification; family "
                  "selection confounds everything."),
        pointer=('The Signature system models mobility as a compounding ecology of childhood place effects. The Signature test: outcomes track childhood-exposure dose. It would be refuted if place effects vanish controlling for family.'),
        key_points=[
            "Absolute mobility fell from 90 to 50 percent across cohorts.",
            "Mobility varies enormously by place.",
            "Childhood exposure duration predicts outcomes.",
            "The drivers of place effects are disputed.",
        ],
        requirements=[
            "Causal identification of place effects.",
            "An account of the absolute-mobility decline.",
            "Separation of family from place effects.",
        ],
        standards=[
            "Claims checked against the mobility literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Chetty R et al. Where is the land of opportunity? Quarterly Journal of Economics; 2014.",
            "Chetty R et al. The fading American dream. Science; 2017.",
        ],
        hypotheses=[
            "Compounding childhood ecologies explain place effects.",
            "Schools alone drive the differences.",
            "Family structure is the key variable.",
            "Mobility is mostly genetic and unchangeable.",
        ],
        confirm="Outcomes track childhood-exposure dose.",
        refute="Place effects vanish controlling for family.",
    ),
    dict(
        key="sociology-12",
        name="The Gender Pay Gap: What Explains It",
        group="Inequality",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("What explains the persistent gender pay gap - and how much "
                 "is discrimination versus choices versus structure?"),
        background=("Women earn roughly 80 cents on the male dollar in the "
                    "US; the gap narrows with controls for occupation, "
                    "hours, and experience but does not vanish. Goldin's "
                    "work points to temporal flexibility: jobs rewarding "
                    "long, inflexible hours penalize caregivers. "
                    "Discrimination, negotiation differences, and "
                    "occupational sorting all contribute - the weights "
                    "are disputed."),
        why_it_matters=("The gap is the most-cited inequality statistic in "
                        "public life. Its decomposition determines the "
                        "remedy."),
        sig_lens=("The Signature lens treats the gap as a flexibility ledger: "
                  "the Signature approach asks what inflexibility costs "
                  "and who pays it."),
        sig_body=("The Signature proposal models the gap as a flexibility "
                  "price. Assumptions: (1) some jobs pay premiums for "
                  "long, inflexible, on-call hours; (2) caregiving falls "
                  "disproportionately on women; (3) the premium reflects "
                  "coordination value. Reasoning path: the proposal shows "
                  "the residual gap concentrates in inflexible-hour "
                  "occupations - predicting that temporal flexibility "
                  "(remote work, team coverage) should narrow the gap, "
                  "which recent data support. Discrimination then explains "
                  "the remainder, not the bulk. Limits: the model needs "
                  "better flexibility measures; occupational sorting "
                  "itself may reflect discrimination."),
        pointer=('The Signature system models the gap as a flexibility price, predicting remote work and team coverage narrow it. The Signature test: gap narrows where flexibility rises. It would be refuted if the gap persists fully in flexible occupations.'),
        key_points=[
            "The raw gap is about 80 cents on the dollar.",
            "Controls narrow but do not eliminate it.",
            "Temporal flexibility is Goldin's key variable.",
            "Discrimination, sorting, and negotiation compete as explanations.",
        ],
        requirements=[
            "Decomposition of the gap's components.",
            "Flexibility measures by occupation.",
            "An account of occupational sorting's causes.",
        ],
        standards=[
            "Claims checked against the labor-economics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Goldin C. A grand gender convergence. American Economic Review; 2014.",
            "Blau FD, Kahn LM. The gender wage gap. Journal of Economic Literature; 2017.",
        ],
        hypotheses=[
            "Temporal inflexibility is the main driver.",
            "Discrimination dominates the residual.",
            "Occupational sorting reflects preferences.",
            "Negotiation differences explain the gap.",
        ],
        confirm="Gap narrows where flexibility rises.",
        refute="The gap persists fully in flexible occupations.",
    ),
    dict(
        key="sociology-13",
        name="The Racial Wealth Gap",
        group="Inequality",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("Why does the racial wealth gap persist and even widen - "
                 "with typical Black families holding cents on the white "
                 "dollar - despite civil-rights gains?"),
        background=("Wealth gaps dwarf income gaps: historical dispossession "
                    "(slavery, redlining, exclusion from New Deal programs), "
                    "ongoing discrimination, and the dynamics of wealth "
                    "itself (returns compound for holders). Recent work "
                    "shows the gap widening at the top. Whether policy can "
                    "close it - baby bonds, reparations, housing reform - "
                    "is fiercely debated."),
        why_it_matters=("Wealth is security, opportunity, and power. The gap "
                        "is the material ledger of American history."),
        sig_lens=("The Signature lens treats wealth as a compounding ledger: "
                  "the Signature approach asks what history set in motion "
                  "that markets now run on their own."),
        sig_body=("The Signature proposal models the gap as historical "
                  "compounding. Assumptions: (1) wealth begets wealth "
                  "through returns; (2) historical exclusions set initial "
                  "conditions near zero for Black families; (3) ongoing "
                  "discrimination adds a flow deficit. Reasoning path: the "
                  "proposal shows even with zero current discrimination, "
                  "the initial-conditions gap compounds - predicting "
                  "persistence without new injustice, which matches the "
                  "data. Closing it then requires stock interventions "
                  "(baby bonds, reparations), not just flow fairness. "
                  "Limits: the model needs better historical wealth "
                  "series; the policy debate is normative as well as "
                  "empirical."),
        pointer=('The Signature system models the gap as historical compounding from near-zero initial conditions, requiring stock interventions. The Signature test: gap persists in models with zero current discrimination. It would be refuted if wealth converges rapidly once flows equalize.'),
        key_points=[
            "Wealth gaps dwarf income gaps.",
            "Historical dispossession set initial conditions.",
            "Returns compound for existing holders.",
            "The gap persists and widens despite civil-rights gains.",
        ],
        requirements=[
            "Historical wealth series by group.",
            "Separation of stock from flow effects.",
            "Policy simulations of closing mechanisms.",
        ],
        standards=[
            "Claims checked against the wealth-inequality literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Oliver ML, Shapiro TM. Black Wealth/White Wealth. Routledge; 1995.",
            "Derenoncourt E et al. Wealth of two nations. 2022.",
        ],
        hypotheses=[
            "Historical compounding explains persistence.",
            "Ongoing discrimination is the main driver.",
            "Savings-behavior differences matter.",
            "Only stock interventions can close the gap.",
        ],
        confirm="Gap persists in models with zero current discrimination.",
        refute="Wealth converges rapidly once flows equalize.",
    ),
    dict(
        key="sociology-14",
        name="Neighborhood Effects: How Much",
        group="Inequality",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("How much do neighborhoods themselves shape life outcomes - "
                 "separate from the families who live in them?"),
        background=("Moving to Opportunity showed moving poor families to "
                    "better neighborhoods helped young children long-term. "
                    "Chetty's work finds large childhood-exposure effects. "
                    "But selection haunts the field: families choose "
                    "neighborhoods, and unmeasured family traits confound "
                    "everything. The causal magnitude of place remains the "
                    "central dispute."),
        why_it_matters=("If place is causal, housing policy is opportunity "
                        "policy - and segregation is a machine for "
                        "inequality."),
        sig_lens=("The Signature lens treats neighborhoods as an exposure "
                  "ledger: the Signature approach asks what each year in "
                  "a place deposits in a child."),
        sig_body=("The Signature proposal models neighborhood effects as "
                  "cumulative exposure. Assumptions: (1) neighborhoods "
                  "differ in schools, safety, norms, and networks; (2) "
                  "effects accumulate with exposure duration; (3) young "
                  "children are most plastic. Reasoning path: the proposal "
                  "predicts effects should scale with years of childhood "
                  "exposure - which Chetty's data confirm - and that "
                  "moving adolescents helps little. Place is then a "
                  "childhood investment with compound returns. Limits: "
                  "the model needs the active ingredients isolated; "
                  "selection remains the fundamental threat."),
        pointer=('The Signature system models neighborhood effects as cumulative childhood exposure with compound returns. The Signature test: outcomes scale with exposure duration. It would be refuted if no exposure gradient appears in experimental data.'),
        key_points=[
            "Moving to Opportunity showed long-term gains for young movers.",
            "Childhood-exposure duration predicts outcomes.",
            "Selection confounds most neighborhood research.",
            "The active ingredients are unidentified.",
        ],
        requirements=[
            "Causal identification of place effects.",
            "Exposure-duration gradients.",
            "Isolation of the active ingredients.",
        ],
        standards=[
            "Claims checked against the neighborhoods literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Chetty R, Hendren N. The impacts of neighborhoods on intergenerational mobility. 2018.",
            "Sampson RJ. Great American City. University of Chicago Press; 2012.",
        ],
        hypotheses=[
            "Cumulative exposure explains the effects.",
            "Selection explains most observed differences.",
            "Schools are the active ingredient.",
            "Norms and networks are the active ingredients.",
        ],
        confirm="Outcomes scale with exposure duration.",
        refute="No exposure gradient appears in experimental data.",
    ),
    dict(
        key="sociology-15",
        name="The Cultural Omnivore Thesis",
        group="Culture",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Has elite taste shifted from highbrow snobbery to "
                 "omnivorous breadth - and what does it signal about "
                 "class?"),
        background=("Peterson found high-status Americans increasingly "
                    "consume both opera and hip-hop - omnivores, not "
                    "snobs. The thesis: breadth itself became the status "
                    "signal. Critics reply that omnivorousness is itself "
                    "a class performance, that genre hierarchies persist "
                    "within breadth, and that digital abundance changed "
                    "what breadth means."),
        why_it_matters=("Taste is class made visible. The omnivore shift - "
                        "if real - rewrites how status works."),
        sig_lens=("The Signature lens treats taste as a signal ledger: the "
                  "Signature approach asks what breadth proves that "
                  "snobbery cannot."),
        sig_body=("The Signature proposal models omnivorousness as a "
                  "costly signal of cosmopolitan capital. Assumptions: "
                  "(1) status needs hard-to-fake signals; (2) snobbery "
                  "became fakable (anyone can name-drop opera); (3) "
                  "genuine breadth across distant genres is costly to "
                  "acquire. Reasoning path: the proposal predicts elites "
                  "should display breadth spanning high-low divides - "
                  "which the data show - while genre hierarchies persist "
                  "in how breadth is performed. Omnivorousness is then "
                  "snobbery 2.0, not its end. Limits: the model needs "
                  "better measures of genuine versus performed breadth; "
                  "streaming changed the cost structure."),
        pointer=('The Signature system models omnivorousness as a costly signal of cosmopolitan capital - snobbery 2.0 rather than its end. The Signature test: breadth spans high-low divides among elites specifically. It would be refuted if breadth shows no class gradient.'),
        key_points=[
            "High-status taste increasingly spans high and low genres.",
            "Breadth itself became the status signal.",
            "Critics see class performance in the breadth.",
            "Digital abundance changed what breadth costs.",
        ],
        requirements=[
            "Measures of genuine versus performed breadth.",
            "An account of persistent genre hierarchies.",
            "Cross-national testing of the thesis.",
        ],
        standards=[
            "Claims checked against the culture-and-class literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Peterson RA, Kern RM. Changing highbrow taste. American Sociological Review; 1996.",
            "Lizardo O, Skiles S. Highbrow omnivorousness. 2012.",
        ],
        hypotheses=[
            "Omnivorousness is costly signaling of cosmopolitan capital.",
            "Democratization genuinely flattened taste hierarchies.",
            "Digital abundance made breadth meaningless as signal.",
            "The thesis is an American artifact.",
        ],
        confirm="Breadth spans high-low divides among elites specifically.",
        refute="Breadth shows no class gradient.",
    ),
    dict(
        key="sociology-16",
        name="Emotion Work and Emotional Labor",
        group="Culture",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("How does the commercialization of feeling - emotional labor "
                 "- shape workers, and has the concept been stretched too "
                 "thin?"),
        background=("Hochschild showed flight attendants and bill collectors "
                    "manage feelings for pay, with costs to the self. The "
                    "term escaped into popular use meaning any emotional "
                    "effort, diluting its analytic power. The live questions: "
                    "which jobs exact the highest costs, how workers resist, "
                    "and whether the concept survives its popularization."),
        why_it_matters=("Service work dominates modern economies. Its "
                        "emotional costs are a hidden tax on workers."),
        sig_lens=("The Signature lens treats emotional labor as an "
                  "alienation ledger: the Signature approach asks when "
                  "managed feeling stops feeling like one's own."),
        sig_body=("The Signature proposal models emotional labor costs as "
                  "dissonance-driven. Assumptions: (1) jobs require "
                  "display rules; (2) dissonance between felt and displayed "
                  "emotion is costly; (3) autonomy reduces the cost. "
                  "Reasoning path: the proposal predicts costs should be "
                  "highest where display rules are rigid and autonomy low "
                  "(call centers) and lowest where workers control the "
                  "performance (skilled care) - matching the evidence. "
                  "The popular dilution then obscures the mechanism: it "
                  "is not effort but unfreedom that wounds. Limits: the "
                  "model needs better dissonance measures; resistance "
                  "strategies need study."),
        pointer=('The Signature system models emotional-labor costs as dissonance under rigid display rules, worst where autonomy is lowest. The Signature test: costs track dissonance-autonomy measures. It would be refuted if high-autonomy emotional work proves equally costly.'),
        key_points=[
            "Hochschild documented managed feeling as paid work.",
            "The term diluted into meaning any emotional effort.",
            "Costs concentrate where display rules are rigid.",
            "Autonomy appears to buffer the costs.",
        ],
        requirements=[
            "A precise concept separated from popular dilution.",
            "Dissonance measures by occupation.",
            "An account of worker resistance.",
        ],
        standards=[
            "Claims checked against the emotions-at-work literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hochschild AR. The Managed Heart. University of California Press; 1983.",
            "Wharton AS. The sociology of emotional labor. 2009.",
        ],
        hypotheses=[
            "Dissonance under low autonomy drives the costs.",
            "All emotional effort is costly regardless of autonomy.",
            "The concept is too diluted to be useful.",
            "Workers routinely resist and reshape display rules.",
        ],
        confirm="Costs track dissonance-autonomy measures.",
        refute="High-autonomy emotional work proves equally costly.",
    ),
    dict(
        key="sociology-17",
        name="The McDonaldization Limits",
        group="Institutions",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Where does McDonaldization - efficiency, calculability, "
                 "predictability, control - hit its limits?"),
        background=("Ritzer argued rationalization was conquering social "
                    "life, producing the 'irrationality of rationality.' "
                    "But counter-trends appeared: customization, "
                    "experience economies, artisanal revivals, and "
                    "algorithmic personalization that is rationalized yet "
                    "individualized. Whether McDonaldization describes the "
                    "present or a passing phase is open."),
        why_it_matters=("The thesis predicted the texture of modern life. "
                        "Its limits mark where humanity pushes back."),
        sig_lens=("The Signature lens treats rationalization as an "
                  "efficiency ledger: the Signature approach asks what "
                  "rationalization cannot efficiently produce."),
        sig_body=("The Signature proposal models McDonaldization as "
                  "bounded by authenticity demand. Assumptions: (1) "
                  "rationalization lowers costs; (2) consumers also value "
                  "authenticity, surprise, and meaning; (3) these are "
                  "hard to rationalize. Reasoning path: the proposal "
                  "predicts rationalization dominates where consumers "
                  "prioritize price and predictability, while artisanal "
                  "and experience markets grow where they prioritize "
                  "meaning - explaining the simultaneous advance of both. "
                  "The irrationality of rationality then appears exactly "
                  "where meaning was the product. Limits: the model "
                  "needs better authenticity measures; algorithmic "
                  "personalization blurs the categories."),
        pointer=('The Signature system models rationalization as bounded by authenticity demand, with artisanal markets growing alongside it. The Signature test: artisanal markets grow where meaning is the product. It would be refuted if rationalization conquers even authenticity markets.'),
        key_points=[
            "Ritzer identified efficiency, calculability, predictability, control.",
            "Counter-trends: artisanal, experience, personalization economies.",
            "The irrationality of rationality: systems defeating their purposes.",
            "Whether the thesis describes the present is disputed.",
        ],
        requirements=[
            "An account of simultaneous rationalization and artisanal growth.",
            "Authenticity measures.",
            "An account of algorithmic personalization.",
        ],
        standards=[
            "Claims checked against the rationalization literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ritzer G. The McDonaldization of Society. Pine Forge; 1993.",
            "Bryman A. McDonaldization revisited. 2003.",
        ],
        hypotheses=[
            "Authenticity demand bounds rationalization.",
            "Rationalization continues unchecked.",
            "Personalization is McDonaldization 2.0.",
            "The thesis was always overstated.",
        ],
        confirm="Artisanal markets grow where meaning is the product.",
        refute="Rationalization conquers even authenticity markets.",
    ),
    dict(
        key="sociology-18",
        name="The Iron Law of Oligarchy: Still True",
        group="Institutions",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Does Michels' iron law - all organizations become "
                 "oligarchies - still hold in the age of digital "
                 "decentralization?"),
        background=("Michels argued that organization necessitates "
                    "leadership, which entrenches itself. Tests are mixed: "
                    "parties and unions oligarchize, but digital movements "
                    "(Occupy, open source) experimented with leaderlessness "
                    "- mostly failing or recentralizing. Whether technology "
                    "breaks the law or just changes its form is the live "
                    "question."),
        why_it_matters=("The iron law is democracy's pessimistic theorem. "
                        "Its truth determines whether democratic "
                        "organization is possible."),
        sig_lens=("The Signature lens treats oligarchy as a coordination "
                  "ledger: the Signature approach asks what leadership "
                  "provides that members cannot provide themselves."),
        sig_body=("The Signature proposal models oligarchy as a "
                  "coordination-cost outcome. Assumptions: (1) collective "
                  "action needs coordination; (2) coordination has costs; "
                  "(3) leaders capture the surplus of coordination. "
                  "Reasoning path: the proposal shows digital tools lower "
                  "coordination costs but do not eliminate them - "
                  "predicting leaderless movements should succeed at "
                  "mobilization but fail at sustained strategy, which "
                  "matches Occupy and similar cases. The law then bends "
                  "but does not break: oligarchy reappears wherever "
                  "sustained coordination is needed. Limits: the model "
                  "needs better coordination-cost measures; blockchain "
                  "governance is an untested case."),
        pointer=('The Signature system models oligarchy as a coordination-cost outcome that digital tools bend but do not break. The Signature test: leaderless movements fail at sustained strategy. It would be refuted if a large organization sustains leaderless strategy long-term.'),
        key_points=[
            "Michels: organization necessitates entrenched leadership.",
            "Digital movements attempted leaderlessness.",
            "Most recentralized or failed strategically.",
            "Whether technology breaks the law is open.",
        ],
        requirements=[
            "Coordination-cost measures across organizations.",
            "An account of digital movement trajectories.",
            "A test of blockchain governance claims.",
        ],
        standards=[
            "Claims checked against the organizations literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Michels R. Political Parties. Free Press; 1962.",
            "Freeman J. The tyranny of structurelessness. 1972.",
        ],
        hypotheses=[
            "Coordination costs sustain oligarchy despite technology.",
            "Digital tools genuinely break the law.",
            "The law holds for strategy, not mobilization.",
            "Oligarchy was always overstated.",
        ],
        confirm="Leaderless movements fail at sustained strategy.",
        refute="A large organization sustains leaderless strategy long-term.",
    ),
    dict(
        key="sociology-19",
        name="Bureaucracy: Can It Be Humane",
        group="Institutions",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("Can bureaucracy - rule-bound, hierarchical administration - "
                 "be humane, or does the iron cage always win?"),
        background=("Weber saw bureaucracy as technically superior and "
                    "humanly stifling. Reform efforts (street-level "
                    "discretion, New Public Management, human-centered "
                    "design) aim to soften it, but goal displacement, "
                    "red tape, and dehumanization recur. Whether the "
                    "pathologies are inherent or contingent remains "
                    "the dispute."),
        why_it_matters=("Bureaucracy administers modern life. Its human "
                        "possibility determines the texture of the state "
                        "citizens meet."),
        sig_lens=("The Signature lens treats bureaucracy as a discretion "
                  "ledger: the Signature approach asks where rules help "
                  "and where judgment must."),
        sig_body=("The Signature proposal models humane bureaucracy as "
                  "discretion architecture. Assumptions: (1) rules ensure "
                  "fairness at scale; (2) rigid rules misfire on "
                  "exceptions; (3) frontline discretion handles "
                  "exceptions but risks bias. Reasoning path: the "
                  "proposal predicts humane outcomes where discretion is "
                  "structured - guided, reviewed, accountable - rather "
                  "than eliminated or unlimited, explaining why both "
                  "rule-fundamentalism and discretion-romanticism fail. "
                  "The cage is then a design choice, not destiny. "
                  "Limits: the model needs better discretion-quality "
                  "measures; political pressures distort designs."),
        pointer=('The Signature system models humane bureaucracy as structured discretion - guided and accountable rather than eliminated or unlimited. The Signature test: structured-discretion designs outperform both extremes. It would be refuted if all large bureaucracies converge on dehumanization.'),
        key_points=[
            "Weber: bureaucracy is efficient and stifling.",
            "Reforms target discretion, design, and humanity.",
            "Pathologies (displacement, red tape) recur.",
            "Whether they are inherent or contingent is disputed.",
        ],
        requirements=[
            "Discretion-quality measures.",
            "An account of reform successes and failures.",
            "Separation of design from political distortion.",
        ],
        standards=[
            "Claims checked against the organizations literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weber M. Economy and Society. 1922.",
            "Lipsky M. Street-Level Bureaucracy. Russell Sage; 1980.",
        ],
        hypotheses=[
            "Structured discretion makes bureaucracy humane.",
            "The iron cage is inherent to scale.",
            "Technology can dissolve the dilemmas.",
            "Small scale is the only humane answer.",
        ],
        confirm="Structured-discretion designs outperform both extremes.",
        refute="All large bureaucracies converge on dehumanization.",
    ),
    dict(
        key="sociology-20",
        name="The Credential Society",
        group="Institutions",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Does schooling build skills or merely sort people - and "
                 "has credential inflation broken the education bargain?"),
        background=("Collins argued education is mostly credentialism: "
                    "degrees signal status, and requirements ratchet upward "
                    "without skill gains. Human-capital theory replies that "
                    "schooling builds productive skills. Credential "
                    "inflation - jobs requiring degrees that once needed "
                    "high school - suggests the sorting view, but the "
                    "productivity evidence is mixed."),
        why_it_matters=("Education is the largest public investment in most "
                        "societies. Its true function determines whether "
                        "the money builds or merely sorts."),
        sig_lens=("The Signature lens treats credentials as a signal ledger: "
                  "the Signature approach asks what employers learn from "
                  "a degree that they could not learn otherwise."),
        sig_body=("The Signature proposal models schooling as both signal "
                  "and skill, with the mix varying. Assumptions: (1) "
                  "degrees signal perseverance and conformity cheaply; (2) "
                  "some schooling builds real skills; (3) employers use "
                  "the cheapest reliable signal. Reasoning path: the "
                  "proposal predicts credential inflation where signals "
                  "are cheap and skills hard to verify - explaining the "
                  "ratchet - while skill-building dominates where "
                  "competence is directly testable. Policy then differs "
                  "by sector: test skills where possible, tax the signal "
                  "where not. Limits: the model needs better skill-versus-"
                  "signal decomposition; sheepskin effects are debated."),
        pointer=('The Signature system models schooling as a skill-signal mix varying by sector, with inflation where signals are cheap. The Signature test: inflation concentrates where skills are unverifiable. It would be refuted if degrees predict productivity equally everywhere.'),
        key_points=[
            "Credential requirements ratchet upward over time.",
            "Human-capital versus signaling theories compete.",
            "Sheepskin effects suggest signaling matters.",
            "The productivity evidence is mixed.",
        ],
        requirements=[
            "Skill-versus-signal decomposition.",
            "An account of the inflation ratchet.",
            "Sector-specific policy implications.",
        ],
        standards=[
            "Claims checked against the education-and-work literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Collins R. The Credential Society. Academic Press; 1979.",
            "Becker GS. Human Capital. University of Chicago Press; 1964.",
        ],
        hypotheses=[
            "The mix varies by sector; signals dominate where skills are hard to test.",
            "Schooling is mostly signaling.",
            "Schooling is mostly skill-building.",
            "Credential inflation reflects real skill demands.",
        ],
        confirm="Inflation concentrates where skills are unverifiable.",
        refute="Degrees predict productivity equally everywhere.",
    ),
    dict(
        key="sociology-21",
        name="Moral Panics: Why Do They Erupt",
        group="Deviance",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Why do moral panics - disproportionate societal reactions "
                 "to deviance - erupt when they do, and why about those "
                 "targets?"),
        background=("Cohen's folk devils and moral panics model describes "
                    "exaggeration, prediction, and symbolization - from "
                    "mods and rockers to satanic panics to modern online "
                    "versions. But the model describes better than it "
                    "predicts: why this deviance, why now? Elite "
                    "engineering, grassroots anxiety, and media "
                    "amplification all have cases."),
        why_it_matters=("Moral panics drive policy - from drug laws to "
                        "internet regulation. Understanding eruption "
                        "means understanding manufactured consent."),
        sig_lens=("The Signature lens treats panics as an anxiety ledger: "
                  "the Signature approach asks what free-floating fear "
                  "the folk devil gives a name."),
        sig_body=("The Signature proposal models panics as anxiety "
                  "displacement. Assumptions: (1) societies carry "
                  "free-floating anxieties (change, decline, youth); (2) "
                  "a folk devil concretizes the anxiety; (3) media and "
                  "elites amplify for their own reasons. Reasoning path: "
                  "the proposal predicts panics erupt where anxiety is "
                  "high and a vivid symbol is available - explaining "
                  "timing better than target selection. The panic then "
                  "reveals the anxiety, not the deviance. Limits: the "
                  "model needs anxiety measures independent of the "
                  "panic; elite orchestration cases need separate "
                  "accounting."),
        pointer=('The Signature system models panics as anxiety displacement onto available folk devils, revealing the anxiety rather than the deviance. The Signature test: panic timing tracks anxiety measures. It would be refuted if panics erupt with no measurable background anxiety.'),
        key_points=[
            "Cohen's model: exaggeration, prediction, symbolization.",
            "The model describes better than it predicts.",
            "Elite, grassroots, and media accounts compete.",
            "Online panics accelerate the dynamics.",
        ],
        requirements=[
            "Anxiety measures independent of panics.",
            "A predictive account of timing and targets.",
            "An account of elite versus grassroots initiation.",
        ],
        standards=[
            "Claims checked against the moral-panics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Cohen S. Folk Devils and Moral Panics. MacGibbon and Kee; 1972.",
            "Goode E, Ben-Yehuda N. Moral Panics. Blackwell; 1994.",
        ],
        hypotheses=[
            "Anxiety displacement explains eruption timing.",
            "Elite engineering drives most panics.",
            "Media amplification is the sufficient cause.",
            "Panics are rational responses to real threats.",
        ],
        confirm="Panic timing tracks anxiety measures.",
        refute="Panics erupt with no measurable background anxiety.",
    ),
    dict(
        key="sociology-22",
        name="The Labeling Theory Limits",
        group="Deviance",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("How far does labeling theory go - does the deviant label "
                 "create the deviance, or does real behavior come first?"),
        background=("Becker argued deviance is created by social reaction; "
                    "labels become master statuses that trap people. "
                    "Critics reply that the theory ignores primary "
                    "deviation - people do bad things before being labeled "
                    "- and cannot explain who gets labeled. The current "
                    "synthesis grants labeling secondary effects while "
                    "insisting on prior behavior, but the weights are "
                    "disputed."),
        why_it_matters=("Labeling theory underlies diversion, restorative "
                        "justice, and record-clearing reforms. Its true "
                        "scope determines criminal-justice policy."),
        sig_lens=("The Signature lens treats labeling as a feedback ledger: "
                  "the Signature approach asks when the label amplifies "
                  "versus merely marks."),
        sig_body=("The Signature proposal models labeling as a feedback "
                  "loop with gates. Assumptions: (1) primary deviation "
                  "has its own causes; (2) labels change opportunities "
                  "and identities; (3) the loop needs open gates (record "
                  "visibility, stigma). Reasoning path: the proposal "
                  "predicts labeling effects should be largest where "
                  "gates are open - visible records, strong stigma - and "
                  "smallest where reintegration is structured, matching "
                  "the evidence. The theory is then true but bounded: "
                  "labels amplify, they rarely originate. Limits: the "
                  "model needs better gate measures; identity effects "
                  "are hard to isolate."),
        pointer=('The Signature system models labeling as a gated feedback loop: labels amplify where gates are open, rarely originating deviance. The Signature test: labeling effects track gate-openness measures. It would be refuted if large labeling effects appear with gates closed.'),
        key_points=[
            "Becker: deviance is created by social reaction.",
            "Critics: primary deviation precedes labels.",
            "The synthesis grants secondary effects.",
            "Policy (diversion, record-clearing) assumes the theory.",
        ],
        requirements=[
            "Separation of primary from secondary deviation.",
            "Gate measures for the feedback loop.",
            "Policy-relevant effect sizes.",
        ],
        standards=[
            "Claims checked against the deviance literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Becker HS. Outsiders. Free Press; 1963.",
            "Bernburg JG, Krohn MD. Labeling, life chances, and adult crime. 2003.",
        ],
        hypotheses=[
            "Gated feedback explains labeling's true scope.",
            "Labeling effects are large and primary.",
            "Labeling effects are negligible.",
            "The theory is unfalsifiable as stated.",
        ],
        confirm="Labeling effects track gate-openness measures.",
        refute="Large labeling effects appear with gates closed.",
    ),
    dict(
        key="sociology-23",
        name="Anomie in the Digital Age",
        group="Theory",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Does the digital age produce anomie - normlessness - and "
                 "what does Durkheim's concept mean when norms multiply "
                 "instead of dissolving?"),
        background=("Durkheim's anomie described deregulation: desires "
                    "unbounded by norms. Digital life offers infinite "
                    "choice, collapsed contexts, and competing normative "
                    "orders - which some read as hyper-anomie and others "
                    "as hyper-nomia (too many norms). The concept "
                    "stretches; whether it still explains suicide, "
                    "alienation, and extremism is open."),
        why_it_matters=("Anomie was sociology's diagnosis of modernity. Its "
                        "digital form would be the diagnosis of our time."),
        sig_lens=("The Signature lens treats digital anomie as a context "
                  "ledger: the Signature approach asks what happens when "
                  "every audience is present at once."),
        sig_body=("The Signature proposal models digital life as context "
                  "collapse producing normative overload. Assumptions: "
                  "(1) norms are audience-specific; (2) platforms merge "
                  "audiences; (3) merged audiences make every act "
                  "norm-violating somewhere. Reasoning path: the proposal "
                  "shows the result is not normlessness but "
                  "norm-impossibility - predicting anxiety, "
                  "self-censorship, and retreat to bounded groups, which "
                  "matches observed patterns. Durkheim's deregulation "
                  "becomes over-regulation by incompatible regulators. "
                  "Limits: the model needs better context-collapse "
                  "measures; generational adaptation may dissolve the "
                  "effects."),
        pointer=('The Signature system models digital anomie as normative overload from collapsed contexts, not normlessness. The Signature test: malaise tracks context-collapse exposure. It would be refuted if heavy platform users show no normative stress.'),
        key_points=[
            "Durkheim's anomie: desires unbounded by norms.",
            "Digital life merges audiences and multiplies norms.",
            "Hyper-anomie versus hyper-nomia readings compete.",
            "Context collapse is the leading mechanism.",
        ],
        requirements=[
            "Context-collapse measures.",
            "An account of anxiety and retreat patterns.",
            "Generational comparisons.",
        ],
        standards=[
            "Claims checked against the theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Durkheim E. Suicide. 1897.",
            "Marwick AE, boyd d. I tweet honestly, I tweet passionately. 2011.",
        ],
        hypotheses=[
            "Normative overload explains digital malaise.",
            "Digital life is genuinely anomic.",
            "New digital norms are forming adequately.",
            "The concept no longer applies.",
        ],
        confirm="Malaise tracks context-collapse exposure.",
        refute="Heavy platform users show no normative stress.",
    ),
    dict(
        key="sociology-24",
        name="The Great Gatsby Curve Mechanism",
        group="Inequality",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Why do more unequal societies have less mobility - the "
                 "Great Gatsby Curve - and what is the mechanism?"),
        background=("Corak documented the cross-country correlation: "
                    "inequality up, mobility down. But correlation is not "
                    "mechanism. Candidates: unequal investment in children, "
                    "segregation, political capture, credit constraints, "
                    "and the simple math that wider rungs are harder to "
                    "climb. Which mechanisms carry the correlation remains "
                    "the open question."),
        why_it_matters=("The curve links the two great inequalities - of "
                        "outcomes and of opportunity. Its mechanism "
                        "determines whether redistribution can restore "
                        "mobility."),
        sig_lens=("The Signature lens treats the curve as an investment "
                  "ledger: the Signature approach asks how inequality "
                  "changes what parents can buy for children."),
        sig_body=("The Signature proposal models the curve through "
                  "parental-investment divergence. Assumptions: (1) "
                  "child outcomes respond to investment; (2) rich "
                  "parents invest more when returns are high; (3) "
                  "inequality raises the returns to investment. "
                  "Reasoning path: the proposal shows inequality "
                  "widens the investment gap mechanically - predicting "
                  "the curve should be steepest where education "
                  "returns are highest, which matches the data. "
                  "Segregation and capture then amplify. Limits: the "
                  "model needs investment measures; the political "
                  "channel needs separate study."),
        pointer=('The Signature system models the curve through parental-investment divergence, steepest where education returns are highest. The Signature test: curve steepness tracks education-return measures. It would be refuted if mobility is equal where investment is equal but inequality high.'),
        key_points=[
            "Inequality correlates negatively with mobility across countries.",
            "The correlation's mechanisms are disputed.",
            "Investment, segregation, capture, and math all have defenders.",
            "Whether redistribution restores mobility is the policy question.",
        ],
        requirements=[
            "Mechanism tests separating the candidates.",
            "Investment measures by class.",
            "Cross-country identification.",
        ],
        standards=[
            "Claims checked against the inequality literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Corak M. Income inequality, equality of opportunity, and intergenerational mobility. 2013.",
            "Krueger AB. The rise and consequences of inequality. 2012.",
        ],
        hypotheses=[
            "Parental-investment divergence is the core mechanism.",
            "Political capture drives the curve.",
            "Credit constraints are primary.",
            "The curve is mostly mathematical.",
        ],
        confirm="Curve steepness tracks education-return measures.",
        refute="Mobility is equal where investment is equal but inequality high.",
    ),
    dict(
        key="sociology-25",
        name="Intersectionality: From Theory to Measurement",
        group="Theory",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("Can intersectionality - the interaction of race, class, "
                 "gender, and other axes - be measured quantitatively, or "
                 "does quantification betray it?"),
        background=("Crenshaw's framework transformed how scholars think "
                    "about compounded disadvantage. But quantitative "
                    "sociology struggles: interaction terms in regressions "
                    "are a thin translation, and the theory's qualitative "
                    "richness resists variables. Recent methods (MAIHDA, "
                    "intersectional machine learning) attempt bridges, but "
                    "whether the theory survives operationalization is "
                    "open."),
        why_it_matters=("Intersectionality shapes law, policy, and activism. "
                        "Its measurability determines whether it can guide "
                        "empirical social science."),
        sig_lens=("The Signature lens treats intersectionality as an "
                  "interaction ledger: the Signature approach asks what "
                  "is lost when lived compounding becomes a coefficient."),
        sig_body=("The Signature proposal models intersectional effects "
                  "as configural, not additive. Assumptions: (1) "
                  "disadvantages interact, not just add; (2) the "
                  "interactions are context-specific; (3) standard "
                  "regressions assume additivity. Reasoning path: the "
                  "proposal shows quantitative methods can capture "
                  "intersectionality only by modeling configurations - "
                  "predicting that MAIHDA-style approaches, which estimate "
                  "stratum-specific effects, will outperform interaction "
                  "terms. The theory then survives as a claim about "
                  "configural causation. Limits: the model needs better "
                  "stratum data; the qualitative core may still resist."),
        pointer=('The Signature system models intersectional effects as configural, with stratum-specific methods outperforming interaction terms. The Signature test: stratum methods reveal effects interaction terms miss. It would be refuted if no configural effect survives controls.'),
        key_points=[
            "Crenshaw's framework transformed disadvantage analysis.",
            "Interaction terms are a thin quantitative translation.",
            "MAIHDA and related methods attempt bridges.",
            "Whether operationalization betrays the theory is disputed.",
        ],
        requirements=[
            "Configural quantitative methods.",
            "Stratum-specific effect estimates.",
            "A criterion for successful translation.",
        ],
        standards=[
            "Claims checked against the intersectionality literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Crenshaw K. Demarginalizing the intersection of race and sex. 1989.",
            "Bauer GR. Incorporating intersectionality theory into population health research. 2014.",
        ],
        hypotheses=[
            "Configural methods can operationalize the theory.",
            "Quantification necessarily betrays it.",
            "Interaction terms suffice pragmatically.",
            "The theory is qualitative by nature.",
        ],
        confirm="Stratum methods reveal effects interaction terms miss.",
        refute="No configural effect survives controls.",
    ),
    dict(
        key="sociology-26",
        name="Structuration: Can It Be Tested",
        group="Theory",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("Can Giddens' structuration theory - structure and agency "
                 "as mutually constitutive - be tested empirically, or is "
                 "it untestable by design?"),
        background=("Structuration resolved the structure-agency dualism "
                    "philosophically: structures are both medium and outcome "
                    "of action. But the theory's very elegance makes it "
                    "hard to test - it predicts everything in general and "
                    "nothing in particular. Critics call it "
                    "unfalsifiable; defenders call it a sensitizing "
                    "framework. Whether it can generate testable "
                    "propositions remains open."),
        why_it_matters=("Structuration is the most ambitious solution to "
                        "sociology's core dualism. Its testability decides "
                        "whether it is science or philosophy."),
        sig_lens=("The Signature lens treats structuration as a loop ledger: "
                  "the Signature approach asks where the loop can be cut "
                  "for measurement."),
        sig_body=("The Signature proposal models structuration as testable "
                  "at the loop's joints. Assumptions: (1) the duality "
                  "holds in general; (2) specific loops have measurable "
                  "nodes (rules, resources, actions); (3) interventions "
                  "can perturb the loop. Reasoning path: the proposal "
                  "shows that while the theory as a whole is "
                  "unfalsifiable, specific structuration loops - a rule "
                  "change propagating through action back to structure - "
                  "generate predictions, predicting that institutional "
                  "reforms should show the predicted recursion. The "
                  "theory then works as a generator of middle-range "
                  "hypotheses. Limits: the model concedes the grand "
                  "theory is untestable; the hypotheses need better "
                  "loop measures."),
        pointer=('The Signature system treats structuration as a generator of testable middle-range loop hypotheses rather than a testable grand theory. The Signature test: reform interventions show predicted recursive effects. It would be refuted if no derived hypothesis survives testing.'),
        key_points=[
            "Structuration resolved structure-agency philosophically.",
            "The theory predicts everything generally, nothing particularly.",
            "Critics charge unfalsifiability.",
            "Defenders claim sensitizing value.",
        ],
        requirements=[
            "Middle-range hypotheses derived from the theory.",
            "Loop measures: rules, resources, actions.",
            "Intervention studies perturbing loops.",
        ],
        standards=[
            "Claims checked against the theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Giddens A. The Constitution of Society. Polity; 1984.",
            "Archer MS. Realist Social Theory. Cambridge University Press; 1995.",
        ],
        hypotheses=[
            "Specific loops generate testable predictions.",
            "The theory is untestable by design.",
            "It works as sensitizing framework only.",
            "Archer's morphogenesis supersedes it.",
        ],
        confirm="Reform interventions show predicted recursive effects.",
        refute="No derived hypothesis survives testing.",
    ),
    dict(
        key="sociology-27",
        name="The Social Construction of Reality: Limits",
        group="Theory",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("What are the limits of social construction - which parts "
                 "of reality resist being constructed?"),
        background=("Berger and Luckmann showed how reality is built "
                    "through interaction; strong constructionism extended "
                    "the claim to science, gender, and nature itself. "
                    "Critics (realists, Hacking) insist on the "
                    "recalcitrant: disease kills regardless of meaning, "
                    "bridges fall regardless of discourse. Where "
                    "construction stops remains the fault line."),
        why_it_matters=("The limit of construction is the limit of the "
                        "social - and the beginning of everything "
                        "sociology cannot explain."),
        sig_lens=("The Signature lens treats construction as a resistance "
                  "ledger: the Signature approach asks what pushes back."),
        sig_body=("The Signature proposal models construction as bounded "
                  "by recalcitrance. Assumptions: (1) meanings are "
                  "constructed through interaction; (2) physical and "
                  "biological realities constrain meanings; (3) the "
                  "constraint varies by domain. Reasoning path: the "
                  "proposal predicts construction should be total where "
                  "recalcitrance is low (money, status) and thin where "
                  "it is high (disease, engineering) - which matches "
                  "the pattern of successful versus failed "
                  "constructionist claims. Hacking's looping kinds then "
                  "mark the middle zone. Limits: the model needs "
                  "recalcitrance measures; the middle zone is large."),
        pointer=('The Signature system bounds construction by recalcitrance: total where resistance is low, thin where it is high. The Signature test: construction claims succeed inversely to recalcitrance. It would be refuted if strong construction succeeds for highly recalcitrant domains.'),
        key_points=[
            "Constructionism shows reality built through interaction.",
            "Strong versions extended the claim to science and nature.",
            "Realists insist on the recalcitrant.",
            "The boundary remains the fault line.",
        ],
        requirements=[
            "A principled account of the boundary.",
            "Recalcitrance measures by domain.",
            "An account of looping kinds.",
        ],
        standards=[
            "Claims checked against the constructionism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Berger PL, Luckmann T. The Social Construction of Reality. Doubleday; 1966.",
            "Hacking I. The Social Construction of What? Harvard University Press; 1999.",
        ],
        hypotheses=[
            "Recalcitrance bounds construction domain by domain.",
            "Everything is constructed all the way down.",
            "Realism defeats constructionism entirely.",
            "Looping kinds dissolve the boundary.",
        ],
        confirm="Construction claims succeed inversely to recalcitrance.",
        refute="Strong construction succeeds for highly recalcitrant domains.",
    ),
    dict(
        key="sociology-28",
        name="Collective Memory: How Societies Remember",
        group="Culture",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("How do societies remember - and forget - and who decides "
                 "what the past means?"),
        background=("Halbwachs founded the field: memory is social. "
                    "Nations remember through monuments, textbooks, and "
                    "rituals; they forget through silence. Memory politics "
                    "- statues, apologies, curricula - are among the most "
                    "contested politics alive. But the mechanisms of "
                    "collective forgetting, and whether societies can "
                    "remember truthfully, remain open."),
        why_it_matters=("Collective memory shapes identity, legitimacy, and "
                        "reconciliation. Its mechanics are the mechanics of "
                        "historical justice."),
        sig_lens=("The Signature lens treats memory as an institutional "
                  "ledger: the Signature approach asks who maintains the "
                  "record and who benefits from the gaps."),
        sig_body=("The Signature proposal models collective memory as "
                  "maintained infrastructure. Assumptions: (1) remembering "
                  "needs institutions (schools, monuments, media); (2) "
                  "institutions serve present interests; (3) forgetting is "
                  "active, not passive. Reasoning path: the proposal "
                  "predicts memory should track institutional maintenance "
                  "- predicting that well-funded commemorations persist "
                  "while unfunded ones fade, regardless of truth. "
                  "Forgetting is then defunding. Truthful memory needs "
                  "institutions with truth mandates. Limits: the model "
                  "needs maintenance measures; grassroots memory resists "
                  "institutional accounts."),
        pointer=('The Signature system models collective memory as maintained infrastructure, with forgetting as defunding. The Signature test: remembrance tracks maintenance investment. It would be refuted if unfunded memories persist; funded ones fade.'),
        key_points=[
            "Memory is socially maintained through institutions.",
            "Forgetting is active, not passive.",
            "Memory politics are intensely contested.",
            "Whether truthful collective memory is possible is open.",
        ],
        requirements=[
            "Institutional maintenance measures.",
            "An account of grassroots versus official memory.",
            "A theory of truthful remembrance.",
        ],
        standards=[
            "Claims checked against the memory-studies literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Halbwachs M. On Collective Memory. University of Chicago Press; 1992.",
            "Olick JK. The Politics of Regret. Routledge; 2007.",
        ],
        hypotheses=[
            "Institutional maintenance explains remembering and forgetting.",
            "Grassroots memory resists institutional control.",
            "Truthful collective memory is achievable with right institutions.",
            "All collective memory is presentist myth.",
        ],
        confirm="Remembrance tracks maintenance investment.",
        refute="Unfunded memories persist; funded ones fade.",
    ),
    dict(
        key="sociology-29",
        name="The Sociology of Time",
        group="Culture",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("How do societies construct time - and what does the "
                 "acceleration of social life do to human experience?"),
        background=("From Durkheim's social time to Rosa's acceleration "
                    "theory: modernity speeds up life, desynchronizes "
                    "institutions, and produces burnout. Clock time "
                    "disciplined industrial society; digital time fragments "
                    "it. Whether acceleration is real or perceived, and "
                    "what it does to agency, remains debated."),
        why_it_matters=("Time is the medium of social life. Its social "
                        "construction shapes everything from work to "
                        "meaning."),
        sig_lens=("The Signature lens treats time as a coordination ledger: "
                  "the Signature approach asks what shared rhythms make "
                  "society possible."),
        sig_body=("The Signature proposal models social time as "
                  "coordination infrastructure. Assumptions: (1) "
                  "collective action needs shared rhythms; (2) clocks "
                  "standardized industrial rhythms; (3) digital media "
                  "fragment them. Reasoning path: the proposal predicts "
                  "that rhythm fragmentation should raise coordination "
                  "costs - predicting the observed burnout and the "
                  "retreat into algorithmic feeds that re-synchronize "
                  "attention artificially. Acceleration is then partly "
                  "real (more events) and partly desynchronization. "
                  "Limits: the model needs rhythm measures; subjective "
                  "acceleration is hard to separate from objective."),
        pointer=('The Signature system models social time as coordination infrastructure, with digital fragmentation raising coordination costs. The Signature test: malaise tracks desynchronization measures. It would be refuted if fragmented societies show no coordination costs.'),
        key_points=[
            "Clock time disciplined industrial society.",
            "Acceleration theory claims modernity speeds up life.",
            "Digital media fragment shared rhythms.",
            "Burnout may reflect desynchronization.",
        ],
        requirements=[
            "Rhythm and synchronization measures.",
            "Separation of real from perceived acceleration.",
            "An account of algorithmic re-synchronization.",
        ],
        standards=[
            "Claims checked against the time-sociology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rosa H. Social Acceleration. Columbia University Press; 2013.",
            "Zerubavel E. Hidden Rhythms. University of Chicago Press; 1981.",
        ],
        hypotheses=[
            "Rhythm fragmentation explains modern malaise.",
            "Acceleration is mostly perceived, not real.",
            "New digital rhythms are forming adequately.",
            "Time discipline is loosening, not fragmenting.",
        ],
        confirm="Malaise tracks desynchronization measures.",
        refute="Fragmented societies show no coordination costs.",
    ),
    dict(
        key="sociology-30",
        name="Why Do Social Movements Succeed",
        group="Change",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("Why do some social movements win while most fail - and "
                 "can success be predicted from movement characteristics?"),
        background=("Political-process theory (opportunities, mobilizing "
                    "structures, framing), resource mobilization, and "
                    "newer work on nonviolent discipline compete. "
                    "Chenoweth's 3.5 percent finding was striking, but "
                    "most movements never approach it. The interaction of "
                    "strategy, structure, and contingency resists "
                    "modeling - and digital organizing changed the "
                    "terrain."),
        why_it_matters=("Movements are how the powerless change history. "
                        "Their success formula is the most practical "
                        "knowledge sociology can offer."),
        sig_lens=("The Signature lens treats movements as a leverage ledger: "
                  "the Signature approach asks what small force moves "
                  "the large structure."),
        sig_body=("The Signature proposal models movement success as "
                  "leverage on elite divisions. Assumptions: (1) "
                  "elites rarely concede to pressure alone; (2) "
                  "movements win by splitting elites or raising costs; "
                  "(3) nonviolent discipline maximizes participation. "
                  "Reasoning path: the proposal predicts success where "
                  "movements create elite splits or make the status quo "
                  "costly - explaining why disruptive nonviolence "
                  "outperforms both violence and pure persuasion. "
                  "Digital tools lower mobilization costs but also lower "
                  "commitment. Limits: the model needs better elite-"
                  "division measures; contingency remains large."),
        pointer=('The Signature system models movement success as leverage on elite divisions, with nonviolent disruption maximizing participation. The Signature test: success tracks elite-split measures. It would be refuted if united elites concede to movements regularly.'),
        key_points=[
            "Most movements fail; a few transform societies.",
            "Nonviolent discipline predicts success.",
            "Elite divisions are often decisive.",
            "Digital organizing lowered mobilization costs and commitment.",
        ],
        requirements=[
            "Elite-division measures.",
            "A theory of tactical choice effects.",
            "An account of digital-era changes.",
        ],
        standards=[
            "Claims checked against the movements literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "McAdam D. Political Process and the Development of Black Insurgency. University of Chicago Press; 1982.",
            "Chenoweth E, Stephan MJ. Why Civil Resistance Works. Columbia University Press; 2011.",
        ],
        hypotheses=[
            "Elite-division leverage explains success.",
            "Nonviolent discipline is sufficient.",
            "Resources determine outcomes.",
            "Framing is the decisive variable.",
        ],
        confirm="Success tracks elite-split measures.",
        refute="United elites concede to movements regularly.",
    ),
    dict(
        key="sociology-31",
        name="The Diffusion of Innovations: What Spreads",
        group="Change",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("Why do some innovations diffuse rapidly while superior "
                 "ones languish - and what really drives adoption?"),
        background=("Rogers' diffusion theory identified adopter categories "
                    "and S-curves, but the interesting failures - better "
                    "technologies losing - remain puzzling. Network "
                    "structure, compatibility, observability, and status "
                    "all matter, but their weights shift by domain. The "
                    "QWERTY and VHS cases suggest path dependence can "
                    "defeat superiority."),
        why_it_matters=("Diffusion is how societies improve - or fail to. "
                        "Its rules determine whether the best wins."),
        sig_lens=("The Signature lens treats diffusion as a coordination "
                  "ledger: the Signature approach asks what adopters need "
                  "from each other."),
        sig_body=("The Signature proposal models diffusion as "
                  "coordination-dependent. Assumptions: (1) innovations "
                  "have standalone and network value; (2) adoption is "
                  "risky; (3) early adopters signal safety. Reasoning "
                  "path: the proposal predicts network-value innovations "
                  "diffuse through coordination cascades (explaining "
                  "QWERTY lock-in) while standalone-value innovations "
                  "diffuse through demonstration - so superiority wins "
                  "only where network effects are weak. Policy then "
                  "targets coordination, not just quality. Limits: the "
                  "model needs network-value measures; status effects "
                  "need separate accounting."),
        pointer=('The Signature system models diffusion as coordination-dependent, with superiority winning only where network effects are weak. The Signature test: adoption tracks coordination incentives over quality. It would be refuted if superior standalone innovations consistently win.'),
        key_points=[
            "Rogers identified S-curves and adopter categories.",
            "Superior technologies sometimes lose (QWERTY, VHS).",
            "Network effects can defeat quality.",
            "Domain differences in diffusion drivers are large.",
        ],
        requirements=[
            "Network-value versus standalone-value measures.",
            "An account of path-dependent lock-in.",
            "Domain-specific diffusion models.",
        ],
        standards=[
            "Claims checked against the diffusion literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rogers EM. Diffusion of Innovations. Free Press; 1962.",
            "Arthur WB. Competing technologies, increasing returns. Economic Journal; 1989.",
        ],
        hypotheses=[
            "Coordination dynamics explain diffusion better than quality.",
            "Relative advantage dominates.",
            "Status and compatibility are primary.",
            "Diffusion is fundamentally unpredictable.",
        ],
        confirm="Adoption tracks coordination incentives over quality.",
        refute="Superior standalone innovations consistently win.",
    ),
    dict(
        key="sociology-32",
        name="Tipping Points in Social Change",
        group="Change",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("Do social tipping points really exist - and can they be "
                 "identified before they tip?"),
        background=("Threshold models (Granovetter), tipping in "
                    "segregation (Schelling), and Gladwell's popularization "
                    "suggest sudden change from gradual pressure. But "
                    "prospective identification remains elusive: tipping "
                    "points are clearest in retrospect. Critical slowing "
                    "down and other early-warning signals are being tested, "
                    "but social systems may be too reflexive for physics-"
                    "style prediction."),
        why_it_matters=("Tipping points would make social change "
                        "foreseeable - the holy grail of applied social "
                        "science."),
        sig_lens=("The Signature lens treats tipping as a cascade ledger: "
                  "the Signature approach asks what accumulates invisibly "
                  "before the visible break."),
        sig_body=("The Signature proposal models tipping as preference-"
                  "falsification collapse. Assumptions: (1) many people "
                  "hide true preferences; (2) hidden preferences "
                  "accumulate; (3) a trigger reveals them. Reasoning path: "
                  "the proposal predicts tipping where falsification is "
                  "widespread - predicting sudden norm change (smoking, "
                  "same-sex marriage) follows hidden-preference "
                  "accumulation, which surveys can detect prospectively. "
                  "The early-warning signal is the preference gap. "
                  "Limits: the model needs hidden-preference measures; "
                  "not all change is tipping."),
        pointer=('The Signature system models tipping as preference-falsification collapse, with the preference gap as the early-warning signal. The Signature test: norm changes follow measured preference gaps. It would be refuted if tipping occurs with no preference gap.'),
        key_points=[
            "Threshold models predict sudden change from gradual pressure.",
            "Tipping points are clearest in retrospect.",
            "Early-warning signals are being tested.",
            "Social reflexivity may defeat prediction.",
        ],
        requirements=[
            "Hidden-preference measures.",
            "Prospective tests of tipping predictions.",
            "An account of reflexivity effects.",
        ],
        standards=[
            "Claims checked against the threshold literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Granovetter M. Threshold models of collective behavior. 1978.",
            "Kuran T. Private Truths, Public Lies. Harvard University Press; 1995.",
        ],
        hypotheses=[
            "Preference-falsification gaps predict tipping.",
            "Tipping points are retrospective illusions.",
            "Critical slowing down works for social systems.",
            "Reflexivity makes social tipping unpredictable.",
        ],
        confirm="Norm changes follow measured preference gaps.",
        refute="Tipping occurs with no preference gap.",
    ),
    dict(
        key="sociology-33",
        name="The Attention Economy and Social Order",
        group="Change",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("How does the attention economy - platforms monetizing "
                 "human attention - reshape social order itself?"),
        background=("Platforms optimize for engagement, amplifying outrage, "
                    "conspiracy, and extremes. Theories of the effects "
                    "range from democratic crisis to moral panic: the "
                    "empirical record shows real but contested impacts on "
                    "polarization, teen mental health, and institutional "
                    "trust. Whether platforms cause or merely reveal "
                    "social pathologies is the live dispute."),
        why_it_matters=("The attention economy is the new public sphere. "
                        "Its social physics determines democratic "
                        "possibility."),
        sig_lens=("The Signature lens treats attention as a scarce-resource "
                  "ledger: the Signature approach asks what the "
                  "optimization function selects for."),
        sig_body=("The Signature proposal models platform effects as "
                  "selection by engagement. Assumptions: (1) platforms "
                  "maximize engagement; (2) outrage and novelty engage "
                  "most; (3) users adapt to the selection environment. "
                  "Reasoning path: the proposal predicts the public "
                  "sphere should shift toward high-arousal content - "
                  "which the data show - while noting that selection "
                  "amplifies pre-existing tendencies rather than "
                  "creating them. The crisis is then real but "
                  "misattributed: platforms industrialize human "
                  "biases. Limits: the model needs better causal "
                  "identification; user agency is understated."),
        pointer=('The Signature system models platform effects as engagement selection industrializing pre-existing human biases. The Signature test: content shifts track engagement-optimization measures. It would be refuted if pathologies appear identically without platforms.'),
        key_points=[
            "Platforms optimize for engagement.",
            "Outrage and extremes are amplified.",
            "Effects on polarization and mental health are contested.",
            "Cause versus revelation is the live dispute.",
        ],
        requirements=[
            "Causal identification of platform effects.",
            "Separation of amplification from creation.",
            "An account of user agency.",
        ],
        standards=[
            "Claims checked against the platform literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Zuboff S. The Age of Surveillance Capitalism. PublicAffairs; 2019.",
            "Haidt J. The anxious generation. 2024.",
        ],
        hypotheses=[
            "Engagement selection industrializes human biases.",
            "Platforms create pathologies that did not exist.",
            "Effects are overstated moral panic.",
            "User agency dominates platform design.",
        ],
        confirm="Content shifts track engagement-optimization measures.",
        refute="Pathologies appear identically without platforms.",
    ),
    dict(
        key="sociology-34",
        name="A Unified Theory of the Social",
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can sociology unify its paradigms - functionalism, "
                 "conflict, interactionism, rational choice - into one "
                 "theory of social life?"),
        background=("Sociology's paradigms offer incompatible images: "
                    "society as system, as domination, as negotiated "
                    "meaning, as aggregation. Attempts at synthesis "
                    "(Giddens, Bourdieu, analytical sociology) advanced "
                    "the discussion without ending it. Whether unification "
                    "is possible or the paradigms capture irreducible "
                    "aspects remains the discipline's foundational "
                    "question."),
        why_it_matters=("This is sociology's capstone: the answer determines "
                        "whether the field is one science or a federation."),
        sig_lens=("The Signature lens treats the paradigms as a levels "
                  "ledger: the Signature approach asks what each level "
                  "of social reality needs."),
        sig_body=("The Signature proposal models unification as "
                  "mechanism-based levels integration. Assumptions: (1) "
                  "social reality spans micro, meso, and macro levels; "
                  "(2) each paradigm captures mechanisms at one level; "
                  "(3) mechanisms compose across levels. Reasoning path: "
                  "the proposal assigns interactionism to micro "
                  "mechanisms, networks and organizations to meso, and "
                  "functionalism-conflict to macro patterns - with "
                  "analytical sociology's mechanism focus as the bridge. "
                  "Unity comes from mechanism composition, not "
                  "paradigm victory. Limits: the composition rules are "
                  "sketched, not proven; partisans may reject the "
                  "settlement."),
        pointer=('The Signature system assigns each paradigm its level, with mechanism composition as the bridge to unity. The Signature test: cross-level mechanism models verify predictions. It would be refuted if levels prove irreducible to common mechanisms.'),
        key_points=[
            "Four paradigms offer incompatible images of the social.",
            "Synthesis attempts advanced without ending the debate.",
            "Each paradigm captures what others miss.",
            "Whether unification is possible is foundational.",
        ],
        requirements=[
            "A levels architecture for the paradigms.",
            "Mechanism-composition rules.",
            "Testable cross-level predictions.",
        ],
        standards=[
            "Claims checked against the theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Giddens A. The Constitution of Society. Polity; 1984.",
            "Hedstrom P, Swedberg R. Social Mechanisms. Cambridge University Press; 1998.",
        ],
        hypotheses=[
            "Mechanism-based levels integration unifies the field.",
            "The paradigms are incommensurable.",
            "One paradigm will absorb the rest.",
            "Pluralism is the permanent condition.",
        ],
        confirm="Cross-level mechanism models verify predictions.",
        refute="Levels prove irreducible to common mechanisms.",
    ),
]
