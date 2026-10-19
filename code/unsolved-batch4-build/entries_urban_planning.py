#!/usr/bin/env python3
"""Entries for the Unsolved Urban Planning databases (batch 4).

34 famous open problems in urban planning, ladder-ordered by accessibility.
ID prefixes: JAH-USUP- (public) and JAH-USUPS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="urban-planning-01",
        name="Why Cities Exist",
        group="Theory",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Why do cities exist - what makes agglomeration worth "
                 "its costs?"),
        background=("Economists cite agglomeration economies (matching, "
                    "sharing, learning); the costs are congestion, "
                    "rents, and disease. The puzzle: why the benefits "
                    "so consistently outweigh the costs - and whether "
                    "remote work breaks the logic."),
        why_it_matters=("Cities house most of humanity. Their reason "
                        "determines their future."),
        sig_lens=("The Signature lens treats the city as a matching "
                  "ledger: the Signature approach asks what proximity "
                  "matches."),
        sig_body=("The Signature proposal models cities as "
                  "matching-machines. Assumptions: (1) proximity "
                  "improves matching (workers-jobs, ideas-ideas); (2) "
                  "matching gains exceed congestion costs; (3) digital "
                  "matching substitutes partially. Reasoning path: the "
                  "proposal predicts cities should persist where "
                  "matching is complex (innovation, culture) and "
                  "weaken where it is routine - explaining the "
                  "pandemic pattern. Cities are then for the "
                  "unplannable encounter. Limits: the model needs "
                  "better matching measures; the remote-substitution "
                  "question continues."),
        pointer=('The Signature system models cities as matching-machines for complex, unplannable encounters - persisting where matching resists digitization. The Signature test: persistence tracks matching-complexity measures. It would be refuted if routine-matching cities persist equally.'),
        key_points=[
            "Agglomeration economies: matching, sharing, learning.",
            "Costs: congestion, rents, disease.",
            "Benefits consistently outweigh costs.",
            "Remote work tests the logic.",
        ],
        requirements=[
            "Matching-gain measures by sector.",
            "Remote-substitution studies.",
            "An account of the persistence puzzle.",
        ],
        standards=[
            "Claims checked against the urban-economics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Glaeser EL. Triumph of the City. Penguin; 2011.",
            "Duranton G, Puga D. Micro-foundations of urban agglomeration economies. 2004.",
        ],
        hypotheses=[
            "Matching complexity explains urban persistence.",
            "Cities are obsolete with digital matching.",
            "Consumption, not production, drives cities now.",
            "The costs will eventually win.",
        ],
        confirm="Persistence tracks matching-complexity measures.",
        refute="Routine-matching cities persist equally.",
    ),
    dict(
        key="urban-planning-02",
        name="The Optimal City Size",
        group="Theory",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Is there an optimal city size - and do megacities "
                 "overshoot it?"),
        background=("Theory suggests an inverted-U: agglomeration "
                    "benefits rise, then congestion costs dominate. "
                    "Empirically, bigger cities stay more productive - "
                    "no clear optimum appears. Whether megacities are "
                    "efficient or pathological remains open."),
        why_it_matters=("City size shapes policy (growth limits, new "
                        "towns). The optimum determines planning's "
                        "stance."),
        sig_lens=("The Signature lens treats size as a net ledger: the "
                  "Signature approach asks whether the costs ever "
                  "catch the benefits."),
        sig_body=("The Signature proposal models city size as "
                  "benefit-dominant. Assumptions: (1) agglomeration "
                  "gains scale with size; (2) congestion costs scale "
                  "too; (3) adaptation (transit, governance) offsets "
                  "costs. Reasoning path: the proposal predicts no "
                  "stable optimum - because adaptation moves the "
                  "tradeoff - explaining the missing inverted-U. "
                  "Megacities are then manageable with good "
                  "governance, not inherently oversized. Limits: the "
                  "model needs better adaptation measures; the "
                  "developing-world megacity question is harder."),
        pointer=('The Signature system models city size as benefit-dominant with adaptation: no stable optimum; governance determines livability. The Signature test: livability tracks governance-adaptation measures. It would be refuted if net benefits decline past some size.'),
        key_points=[
            "Theory predicts an inverted-U of net benefits.",
            "Empirically, bigger stays more productive.",
            "No clear optimum appears.",
            "Whether megacities overshoot is open.",
        ],
        requirements=[
            "Adaptation measures by city.",
            "Congestion-cost decompositions.",
            "Developing-world megacity studies.",
        ],
        standards=[
            "Claims checked against the urban-economics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Henderson JV. The sizes and types of cities. American Economic Review; 1974.",
            "Combes PP et al. The productivity advantages of large cities. 2012.",
        ],
        hypotheses=[
            "Adaptation explains the missing optimum.",
            "An optimum exists but is unmeasured.",
            "Megacities are pathologically oversized.",
            "Size does not matter; governance does.",
        ],
        confirm="Livability tracks governance-adaptation measures.",
        refute="Net benefits decline past some size.",
    ),
    dict(
        key="urban-planning-03",
        name="Zoning: Help or Harm",
        group="Policy",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("Does zoning help cities - or is it the primary cause of "
                 "the housing crisis?"),
        background=("Zoning began for health and safety; it became "
                    "exclusionary (single-family zones, height limits). "
                    "Glaeser and others blame zoning for shortages; "
                    "defenders cite neighborhood character and "
                    "planning order. Whether zoning's harms exceed its "
                    "benefits is the live fight."),
        why_it_matters=("Zoning shapes every American city. Its net "
                        "effect determines reform's urgency."),
        sig_lens=("The Signature lens treats zoning as an exclusion "
                  "ledger: the Signature approach asks who the rules "
                  "keep out."),
        sig_body=("The Signature proposal models zoning as "
                  "exclusion-dominant. Assumptions: (1) early zoning "
                  "served health; (2) modern zoning serves "
                  "exclusion; (3) the costs (shortage, segregation) "
                  "are measurable. Reasoning path: the proposal "
                  "predicts housing costs should track restrictiveness "
                  "- which they do strongly. Reform (upzoning, "
                  "by-right approval) is then the highest-leverage "
                  "housing policy. Limits: the model needs better "
                  "benefit measures; the political economy of reform "
                  "is the binding constraint."),
        pointer=('The Signature system models zoning as exclusion-dominant: housing costs track restrictiveness; reform is the highest-leverage policy. The Signature test: costs track restrictiveness measures. It would be refuted if restrictive cities house affordably.'),
        key_points=[
            "Zoning began for health; became exclusionary.",
            "Housing costs track restrictiveness strongly.",
            "Defenders cite character and order.",
            "Whether harms exceed benefits is the live fight.",
        ],
        requirements=[
            "Restrictiveness-cost studies.",
            "Reform outcome evaluations.",
            "Political-economy analyses.",
        ],
        standards=[
            "Claims checked against the land-use literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Glaeser EL et al. Why is Manhattan so expensive? 2005.",
            "Fischel WA. The Homevoter Hypothesis. Harvard University Press; 2001.",
        ],
        hypotheses=[
            "Exclusion dominance explains the cost pattern.",
            "Zoning's benefits justify its costs.",
            "Only some zoning is harmful.",
            "Abolition beats reform.",
        ],
        confirm="Costs track restrictiveness measures.",
        refute="Restrictive cities house affordably.",
    ),
    dict(
        key="urban-planning-04",
        name="The Housing Shortage: Why",
        group="Housing",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Why do prosperous cities have housing shortages - and "
                 "is the shortage real or distributional?"),
        background=("Coastal American cities underbuild amid high "
                    "demand; the causes debated: zoning (supply-side), "
                    "investor demand, construction costs, or labor "
                    "shortages. Whether building more suffices - or "
                    "whether demand is insatiable - remains open."),
        why_it_matters=("Housing shortage drives the affordability "
                        "crisis. Its causes determine the fix."),
        sig_lens=("The Signature lens treats shortage as a supply "
                  "ledger: the Signature approach asks what blocks "
                  "building."),
        sig_body=("The Signature proposal models shortage as "
                  "regulation-blocked supply. Assumptions: (1) demand "
                  "for prosperous cities is strong; (2) supply "
                  "elasticity varies with regulation; (3) elastic "
                  "cities stay affordable. Reasoning path: the "
                  "proposal predicts affordability should track "
                  "supply elasticity - which it does (Houston versus "
                  "San Francisco). Building more suffices where "
                  "regulation allows; the shortage is then policy-"
                  "made. Limits: the model needs better elasticity "
                  "measures; the construction-cost dimension needs "
                  "separating."),
        pointer=('The Signature system models housing shortage as regulation-blocked supply: affordability tracks supply elasticity. The Signature test: affordability tracks elasticity measures. It would be refuted if elastic cities face equal shortages.'),
        key_points=[
            "Prosperous cities underbuild amid high demand.",
            "Supply elasticity varies hugely by regulation.",
            "Elastic cities stay affordable.",
            "Whether building suffices is debated.",
        ],
        requirements=[
            "Supply-elasticity measures.",
            "Construction-cost decompositions.",
            "Demand-insatiability tests.",
        ],
        standards=[
            "Claims checked against the housing-economics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Glaeser EL, Gyourko J. The economic implications of housing supply. 2018.",
            "Saiz A. The geographic determinants of housing supply. Quarterly Journal of Economics; 2010.",
        ],
        hypotheses=[
            "Regulation-blocked supply explains shortages.",
            "Demand is insatiable in superstar cities.",
            "Construction costs are the binding constraint.",
            "Investor demand drives the crisis.",
        ],
        confirm="Affordability tracks elasticity measures.",
        refute="Elastic cities face equal shortages.",
    ),
    dict(
        key="urban-planning-05",
        name="Rent Control: Does It Work",
        group="Housing",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("Does rent control help tenants - or hurt them by "
                 "shrinking supply?"),
        background=("Economists traditionally opposed rent control "
                    "(supply reduction, misallocation); newer studies "
                    "find tenant benefits with smaller supply effects "
                    "than feared - but also gentrification acceleration "
                    "as landlords convert. The net welfare question "
                    "remains contested."),
        why_it_matters=("Rent control is tenants' most demanded policy. "
                        "Its net effect determines its wisdom."),
        sig_lens=("The Signature lens treats rent control as a "
                  "time-horizon ledger: the Signature approach asks "
                  "when benefits arrive versus when costs do."),
        sig_body=("The Signature proposal models rent control as "
                  "short-term help, long-term harm. Assumptions: (1) "
                  "current tenants gain immediately; (2) supply "
                  "responses take years; (3) conversions accelerate "
                  "gentrification. Reasoning path: the proposal "
                  "predicts the policy should help incumbents while "
                  "hurting future tenants - which the evidence "
                  "supports. The design question is then tenant "
                  "protection without supply damage (vouchers, "
                  "stabilization with new-construction exemption). "
                  "Limits: the model needs better long-term studies; "
                  "the political popularity needs explaining."),
        pointer=('The Signature system models rent control as helping incumbents while hurting future tenants: protect tenants without damaging supply. The Signature test: benefits accrue to incumbents; costs to future supply. It would be refuted if no supply effect is found long-term.'),
        key_points=[
            "Traditional economics opposed rent control.",
            "Newer studies find real tenant benefits.",
            "Supply and conversion effects are real.",
            "Net welfare remains contested.",
        ],
        requirements=[
            "Long-term supply studies.",
            "Incumbent-versus-future-tenant welfare analyses.",
            "Alternative protection evaluations.",
        ],
        standards=[
            "Claims checked against the rent-control literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Diamond R et al. The effects of rent control expansion on tenants, landlords, and inequality. 2019.",
            "Jenkins B. Rent control: do economists agree? 2009.",
        ],
        hypotheses=[
            "Time-horizon split explains the debate.",
            "Rent control is net beneficial.",
            "Rent control is net harmful.",
            "Design details determine everything.",
        ],
        confirm="Benefits accrue to incumbents; costs to future supply.",
        refute="No supply effect is found long-term.",
    ),
    dict(
        key="urban-planning-06",
        name="Gentrification: Inevitable",
        group="Housing",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Is gentrification inevitable in growing cities - and "
                 "can its benefits be kept without displacement?"),
        background=("Neighborhood upgrading brings investment and "
                    "displacement; the displacement magnitude is "
                    "debated (some find modest direct displacement, "
                    "others large exclusionary effects). Policies "
                    "(community land trusts, inclusionary zoning) "
                    "attempt the split. Whether upgrading without "
                    "displacement is possible remains open."),
        why_it_matters=("Gentrification reshapes neighborhoods and lives. "
                        "Its inevitability determines policy."),
        sig_lens=("The Signature lens treats gentrification as a "
                  "rent-gap ledger: the Signature approach asks where "
                  "the investment incentive comes from."),
        sig_body=("The Signature proposal models gentrification as "
                  "rent-gap driven. Assumptions: (1) disinvested "
                  "areas offer profit potential; (2) investment "
                  "follows the gap; (3) displacement follows "
                  "investment without protections. Reasoning path: the "
                  "proposal predicts displacement should track "
                  "rent gaps and tenant protections - which it does. "
                  "Upgrading without displacement is then possible "
                  "with tenure protections, not inevitable either "
                  "way. Limits: the model needs better displacement "
                  "measures; the exclusionary (not just direct) "
                  "effects need quantifying."),
        pointer=('The Signature system models gentrification as rent-gap driven: upgrading without displacement is possible with tenure protections. The Signature test: displacement tracks gap-protection measures. It would be refuted if upgrading never displaces with protections.'),
        key_points=[
            "Upgrading brings investment and displacement.",
            "Displacement magnitude is debated.",
            "Rent gaps drive the investment.",
            "Policies attempt to split benefits from harms.",
        ],
        requirements=[
            "Displacement measures (direct and exclusionary).",
            "Protection-policy evaluations.",
            "Rent-gap quantifications.",
        ],
        standards=[
            "Claims checked against the gentrification literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Smith N. The New Urban Frontier. Routledge; 1996.",
            "Freeman L. There Goes the Hood. Temple University Press; 2006.",
        ],
        hypotheses=[
            "Rent-gap plus protections explains outcomes.",
            "Gentrification is inevitable.",
            "Displacement is overstated.",
            "Only anti-growth prevents it.",
        ],
        confirm="Displacement tracks gap-protection measures.",
        refute="Upgrading never displaces with protections.",
    ),
    dict(
        key="urban-planning-07",
        name="The Suburb Problem",
        group="Form",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("Are suburbs a problem to solve - or a revealed "
                 "preference to respect?"),
        background=("Critics condemn suburbs (sprawl, car dependence, "
                    "segregation); defenders note families choose "
                    "them for space, schools, and safety. The "
                    "question: whether suburban form reflects "
                    "preference or subsidy (highways, mortgage "
                    "deduction, zoning)."),
        why_it_matters=("Suburbs house most Americans. Their future "
                        "shapes land, climate, and society."),
        sig_lens=("The Signature lens treats suburbs as a subsidy "
                  "ledger: the Signature approach asks what the "
                  "choice would be at true prices."),
        sig_body=("The Signature proposal models suburbanization as "
                  "subsidy-amplified. Assumptions: (1) some "
                  "preference for space is real; (2) subsidies "
                  "(roads, deductions, exclusionary zoning) amplify "
                  "it; (3) true-price choices would differ. Reasoning "
                  "path: the proposal predicts suburban form should "
                  "track subsidy levels - which cross-country "
                  "comparisons support. The policy answer is then "
                  "price the externalities, respect residual "
                  "preference. Limits: the model needs better "
                  "subsidy quantifications; the preference "
                  "measurement is hard."),
        pointer=('The Signature system models suburbs as subsidy-amplified preference: price the externalities, respect residual choice. The Signature test: form tracks subsidy measures. It would be refuted if unsubsidized suburbs dominate equally.'),
        key_points=[
            "Critics condemn sprawl, car dependence, segregation.",
            "Families choose suburbs for space and schools.",
            "Subsidies (highways, deductions) amplify the choice.",
            "Whether preference or subsidy dominates is the question.",
        ],
        requirements=[
            "Subsidy quantifications.",
            "True-price preference studies.",
            "Cross-country form comparisons.",
        ],
        standards=[
            "Claims checked against the suburban literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Jackson KT. Crabgrass Frontier. Oxford University Press; 1985.",
            "Bruegmann R. Sprawl: A Compact History. University of Chicago Press; 2005.",
        ],
        hypotheses=[
            "Subsidy amplification explains suburban dominance.",
            "Preference alone explains it.",
            "Suburbs are inherently unsustainable.",
            "Suburbs can be retrofitted green.",
        ],
        confirm="Form tracks subsidy measures.",
        refute="Unsubsidized suburbs dominate equally.",
    ),
    dict(
        key="urban-planning-08",
        name="Sprawl: Can It Be Stopped",
        group="Form",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Can sprawl be stopped - and should it be?"),
        background=("Growth boundaries (Portland), greenbelts (London), "
                    "and smart growth all attempt containment; "
                    "results are mixed (leapfrogging, price effects). "
                    "Bruegmann argues sprawl is benign and "
                    "inevitable. Whether containment works - and at "
                    "what cost - remains open."),
        why_it_matters=("Sprawl shapes land use and emissions. "
                        "Containment's feasibility determines strategy."),
        sig_lens=("The Signature lens treats sprawl as a price ledger: "
                  "the Signature approach asks what contains growth "
                  "versus what displaces it."),
        sig_body=("The Signature proposal models containment as "
                  "displacement-prone. Assumptions: (1) demand for "
                  "growth persists; (2) boundaries redirect it; (3) "
                  "redirection can leapfrog. Reasoning path: the "
                  "proposal predicts boundaries should raise inside "
                  "prices and push growth outward - which the "
                  "evidence partly confirms. Effective anti-sprawl "
                  "then needs inside accommodation (density), not "
                  "just boundaries. Limits: the model needs better "
                  "leapfrog measures; the desirability question "
                  "needs separating."),
        pointer=('The Signature system models containment as displacement-prone: boundaries need inside density accommodation to work. The Signature test: growth redirects measurably around boundaries. It would be refuted if boundaries contain without displacement.'),
        key_points=[
            "Growth boundaries and greenbelts attempt containment.",
            "Results are mixed: leapfrogging, price effects.",
            "Some argue sprawl is benign.",
            "Whether containment works at acceptable cost is open.",
        ],
        requirements=[
            "Leapfrog-effect studies.",
            "Inside-accommodation analyses.",
            "Desirability-versus-feasibility separation.",
        ],
        standards=[
            "Claims checked against the sprawl literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bruegmann R. Sprawl: A Compact History. University of Chicago Press; 2005.",
            "Neuman M. The compact city fallacy. 2005.",
        ],
        hypotheses=[
            "Displacement explains containment's limits.",
            "Containment works with proper design.",
            "Sprawl is benign and unstoppable.",
            "Only pricing (not boundaries) works.",
        ],
        confirm="Growth redirects measurably around boundaries.",
        refute="Boundaries contain without displacement.",
    ),
    dict(
        key="urban-planning-09",
        name="The 15-Minute City Debate",
        group="Form",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("Is the 15-minute city a planning ideal - or a "
                 "conspiracy-prone overreach?"),
        background=("Moreno's concept (daily needs within 15 minutes) "
                    "won planning acclaim, then bizarre conspiracy "
                    "theories (climate lockdowns). The substantive "
                    "questions: whether the model fits all cities, "
                    "whether it increases or decreases choice, and "
                    "whether implementation needs coercion."),
        why_it_matters=("The 15-minute city guides major planning. Its "
                        "substance determines its value."),
        sig_lens=("The Signature lens treats the concept as a "
                  "proximity ledger: the Signature approach asks what "
                  "nearness provides."),
        sig_body=("The Signature proposal models the 15-minute city as "
                  "proximity-good, coercion-unnecessary. Assumptions: "
                  "(1) nearness reduces travel and builds local life; "
                  "(2) the benefits need no restrictions on movement; "
                  "(3) the conspiracies confuse amenity with control. "
                  "Reasoning path: the proposal separates the "
                  "planning ideal (complete neighborhoods) from the "
                  "paranoia - predicting the ideal works as "
                  "amenity strategy. Implementation is then about "
                  "adding local completeness, not restricting "
                  "mobility. Limits: the model needs better "
                  "completeness measures; the retrofit challenge is "
                  "real."),
        pointer=('The Signature system models the 15-minute city as amenity strategy: add local completeness, never restrict mobility. The Signature test: outcomes track completeness, not restrictions. It would be refuted if completeness needs mobility limits.'),
        key_points=[
            "The concept won planning acclaim.",
            "Conspiracy theories distorted the debate.",
            "Proximity reduces travel and builds local life.",
            "Whether it needs coercion is the substantive question.",
        ],
        requirements=[
            "Completeness measures by neighborhood.",
            "Amenity-versus-coercion separations.",
            "Retrofit feasibility studies.",
        ],
        standards=[
            "Claims checked against the proximity-planning literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Moreno C. Urban Life and Proximity. 2020.",
            "Pozoukidou G, Chatziyiannaki Z. 15-minute city: decomposing the new urban planning eutopia. Sustainability; 2021.",
        ],
        hypotheses=[
            "Amenity framing captures the value.",
            "The concept requires coercion.",
            "It fits only dense European cities.",
            "The conspiracies revealed real overreach.",
        ],
        confirm="Outcomes track completeness, not restrictions.",
        refute="Completeness needs mobility limits.",
    ),
    dict(
        key="urban-planning-10",
        name="Streets: Who Are They For",
        group="Mobility",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Who are streets for - cars, people, commerce, or all - "
                 "and how should the space be divided?"),
        background=("Streets were multi-use until cars claimed them; "
                    "complete-streets movements reclaim space for "
                    "walking, biking, and lingering. The allocation "
                    "fights (bike lanes, pedestrianization) are "
                    "fierce. The optimal division by context remains "
                    "open."),
        why_it_matters=("Streets are the city's largest public space. "
                        "Their allocation shapes urban life."),
        sig_lens=("The Signature lens treats streets as an allocation "
                  "ledger: the Signature approach asks who uses the "
                  "space versus who claims it."),
        sig_body=("The Signature proposal models street allocation as "
                  "efficiency-plus-life. Assumptions: (1) moving "
                  "people (not vehicles) is the efficiency metric; "
                  "(2) streets also host social life; (3) car "
                  "allocation is historically contingent. Reasoning "
                  "path: the proposal predicts reallocations toward "
                  "walking, biking, and transit should improve both "
                  "throughput and liveliness - which the evidence "
                  "supports. The division is then context-specific "
                  "but directionally clear. Limits: the model needs "
                  "better context typologies; the freight and "
                  "access needs need honoring."),
        pointer=('The Signature system models street allocation as moving people plus hosting life: reallocate from cars contextually. The Signature test: reallocations improve throughput and liveliness. It would be refuted if car allocation maximizes street performance.'),
        key_points=[
            "Cars claimed streets historically; movements reclaim them.",
            "Allocation fights are fierce.",
            "Moving people beats moving vehicles as metric.",
            "The optimal division by context is open.",
        ],
        requirements=[
            "Context typologies for allocation.",
            "Throughput-plus-liveliness studies.",
            "Freight and access accommodation.",
        ],
        standards=[
            "Claims checked against the complete-streets literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Appleyard D. Livable Streets. University of California Press; 1981.",
            "NACTO. Urban Street Design Guide. Island Press; 2013.",
        ],
        hypotheses=[
            "People-throughput plus life guides allocation.",
            "Car priority remains optimal.",
            "Full pedestrianization is the answer.",
            "Context determines everything.",
        ],
        confirm="Reallocations improve throughput and liveliness.",
        refute="Car allocation maximizes street performance.",
    ),
    dict(
        key="urban-planning-11",
        name="Parking: How Much",
        group="Mobility",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("How much parking should cities require - and is free "
                 "parking the problem Shoup says it is?"),
        background=("Minimum parking requirements subsidize driving and "
                    "waste land; Shoup's work showed the high cost of "
                    "free parking. Reforms (eliminating minimums, "
                    "pricing curb space) spread. Whether the reforms "
                    "deliver - and what replaces the minimums - remains "
                    "open."),
        why_it_matters=("Parking policy shapes driving, land use, and "
                        "housing cost. Reform's effects determine its "
                        "spread."),
        sig_lens=("The Signature lens treats parking as a price ledger: "
                  "the Signature approach asks what free parking costs."),
        sig_body=("The Signature proposal models parking as "
                  "mispriced. Assumptions: (1) free parking "
                  "subsidizes driving; (2) minimums inflate housing "
                  "costs; (3) priced curb space allocates "
                  "efficiently. Reasoning path: the proposal predicts "
                  "reforms (no minimums, market-priced curb) should "
                  "cut costs without chaos - which early evidence "
                  "supports. The answer is then price parking right, "
                  "require none. Limits: the model needs longer "
                  "reform evaluations; the spillover politics need "
                  "managing."),
        pointer=('The Signature system models parking as mispriced: eliminate minimums, price the curb at market. The Signature test: reforms cut costs without chaos. It would be refuted if eliminating minimums creates shortages.'),
        key_points=[
            "Minimums subsidize driving and inflate housing costs.",
            "Free parking has high hidden costs.",
            "Reforms are spreading.",
            "Whether they deliver remains open.",
        ],
        requirements=[
            "Long-term reform evaluations.",
            "Spillover-effect studies.",
            "Curb-pricing design research.",
        ],
        standards=[
            "Claims checked against the parking literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Shoup D. The High Cost of Free Parking. APA Planners Press; 2005.",
            "Manville M. Parking requirements and housing development. 2013.",
        ],
        hypotheses=[
            "Mispricing explains the harms; pricing fixes them.",
            "Minimums are necessary.",
            "Reforms cause parking chaos.",
            "The politics make reform impossible.",
        ],
        confirm="Reforms cut costs without chaos.",
        refute="Eliminating minimums creates shortages.",
    ),
    dict(
        key="urban-planning-12",
        name="Transit: Why America Fails",
        group="Mobility",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Why does America build transit so badly - slow, costly, "
                 "and rarely - compared to peers?"),
        background=("US transit costs multiples of European and Asian "
                    "peers; projects take decades. Explanations: "
                    "fragmented governance, litigation, consultant "
                    "capture, lack of expertise, and political "
                    "structures. Whether the failure is fixable "
                    "remains open."),
        why_it_matters=("Transit shapes climate and equity. America's "
                        "failure is a policy emergency."),
        sig_lens=("The Signature lens treats transit as a governance "
                  "ledger: the Signature approach asks who can say "
                  "no."),
        sig_body=("The Signature proposal models US transit failure as "
                  "veto-point accumulation. Assumptions: (1) every "
                  "stakeholder gets a veto; (2) vetoes multiply cost "
                  "and time; (3) peer countries concentrate authority. "
                  "Reasoning path: the proposal predicts costs should "
                  "track veto points - which they do. The fix is "
                  "then governance reform (streamlined approvals, "
                  "in-house expertise), not more money. Limits: the "
                  "model needs better veto-point measures; the "
                  "political feasibility is the binding constraint."),
        pointer=('The Signature system models US transit failure as veto-point accumulation: reform governance, not just funding. The Signature test: costs track veto-point measures. It would be refuted if streamlined projects cost equally.'),
        key_points=[
            "US transit costs multiples of peer countries.",
            "Projects take decades.",
            "Fragmented governance and vetoes are blamed.",
            "Whether the failure is fixable is open.",
        ],
        requirements=[
            "Veto-point cost studies.",
            "Governance-reform pilots.",
            "Peer-comparison institutional analyses.",
        ],
        standards=[
            "Claims checked against the transit literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Eno Center for Transportation. Saving time and making cents. 2021.",
            "Gordon P, Kolesar P. Why transit fails. 2011.",
        ],
        hypotheses=[
            "Veto-point accumulation explains costs.",
            "Labor costs are the driver.",
            "Geography makes US transit hard.",
            "The failure is unfixable.",
        ],
        confirm="Costs track veto-point measures.",
        refute="Streamlined projects cost equally.",
    ),
    dict(
        key="urban-planning-13",
        name="Congestion Pricing: Does It Work",
        group="Mobility",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("Does congestion pricing work - and is it fair?"),
        background=("London, Stockholm, and Singapore show pricing cuts "
                    "congestion; New York's saga shows the politics. "
                    "Equity objections (regressive burdens) compete "
                    "with efficiency gains. Whether pricing is the "
                    "answer - and how to make it fair - remains open."),
        why_it_matters=("Congestion wastes time and pollutes. Pricing's "
                        "verdict determines traffic policy."),
        sig_lens=("The Signature lens treats pricing as a distribution "
                  "ledger: the Signature approach asks who pays and "
                  "who gains."),
        sig_body=("The Signature proposal models congestion pricing as "
                  "efficient-but-distributional. Assumptions: (1) "
                  "pricing cuts congestion (proven); (2) burdens fall "
                  "regressively without design; (3) revenue can "
                  "compensate. Reasoning path: the proposal predicts "
                  "fairness should track revenue use - pricing with "
                  "transit investment is progressive overall. The "
                  "answer is then price plus invest, not price alone. "
                  "Limits: the model needs better distributional "
                  "studies; the political path needs mapping."),
        pointer=('The Signature system models congestion pricing as efficient with distributional design: price the roads, invest the revenue in transit. The Signature test: net progressivity tracks revenue investment. It would be refuted if pricing harms the poor regardless of design.'),
        key_points=[
            "London, Stockholm, Singapore show congestion cuts.",
            "Equity objections are serious.",
            "New York's politics were tortuous.",
            "Whether pricing is fair remains open.",
        ],
        requirements=[
            "Distributional impact studies.",
            "Revenue-use evaluations.",
            "Political-path analyses.",
        ],
        standards=[
            "Claims checked against the congestion-pricing literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Eliasson J. Lessons from the Stockholm congestion charging trial. 2008.",
            "Santos G. Road pricing: theory and evidence. 2005.",
        ],
        hypotheses=[
            "Price-plus-invest resolves the fairness question.",
            "Pricing is inherently regressive.",
            "The efficiency gains justify any distribution.",
            "Politics make pricing impossible.",
        ],
        confirm="Net progressivity tracks revenue investment.",
        refute="Pricing harms the poor regardless of design.",
    ),
    dict(
        key="urban-planning-14",
        name="The Bike Lane Wars",
        group="Mobility",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("Do bike lanes help cities - and why do they provoke such "
                 "fierce opposition?"),
        background=("Protected lanes raise cycling and safety; opponents "
                    "cite congestion, business harm, and culture war. "
                    "Evidence favors the lanes (businesses often gain), "
                    "but the politics are toxic. Whether the wars are "
                    "about transportation or identity remains open."),
        why_it_matters=("Cycling is green transport. The wars determine "
                        "its future."),
        sig_lens=("The Signature lens treats bike lanes as an identity "
                  "ledger: the Signature approach asks what the lane "
                  "symbolizes."),
        sig_body=("The Signature proposal models the wars as "
                  "identity-plus-interest. Assumptions: (1) lanes "
                  "threaten car identity; (2) concentrated opponents "
                  "out-organize diffuse beneficiaries; (3) the "
                  "transport evidence favors lanes. Reasoning path: "
                  "the proposal predicts opposition should track "
                  "car-identity strength, not traffic data - which "
                  "it does. The strategy is then depoliticized "
                  "trials (pilots with data), not persuasion. Limits: "
                  "the model needs better identity measures; the "
                  "business-impact evidence needs spreading."),
        pointer=('The Signature system models bike-lane wars as identity-driven: run depoliticized pilots with data, not persuasion campaigns. The Signature test: opposition tracks identity measures. It would be refuted if opposition follows traffic data.'),
        key_points=[
            "Protected lanes raise cycling and safety.",
            "Opposition cites congestion and business harm.",
            "Evidence favors the lanes.",
            "The politics are disproportionately fierce.",
        ],
        requirements=[
            "Identity-versus-interest decomposition.",
            "Pilot-with-data evaluations.",
            "Business-impact dissemination.",
        ],
        standards=[
            "Claims checked against the cycling literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Pucher J, Buehler R. Making cycling irresistible. Transport Reviews; 2008.",
            "Sztabinski F. Bike lanes and business. 2009.",
        ],
        hypotheses=[
            "Identity explains the disproportionate politics.",
            "Traffic concerns are genuine.",
            "Pilots with data resolve conflicts.",
            "The wars are unwinnable.",
        ],
        confirm="Opposition tracks identity measures.",
        refute="Opposition follows traffic data.",
    ),
    dict(
        key="urban-planning-15",
        name="High-Speed Rail: Why Not America",
        group="Mobility",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Why does America lack high-speed rail - and can it ever "
                 "build it?"),
        background=("Peers built thousands of miles; California's "
                    "project became a cautionary tale (cost, delay). "
                    "Explanations: car culture, federalism, litigation, "
                    "and the transit-cost disease (see "
                    "urban-planning-12). Whether HSR is viable in "
                    "America remains open."),
        why_it_matters=("HSR could transform intercity travel and "
                        "emissions. Its viability determines investment."),
        sig_lens=("The Signature lens treats HSR as a corridor ledger: "
                  "the Signature approach asks where the demand "
                  "concentrates."),
        sig_body=("The Signature proposal models HSR viability as "
                  "corridor-specific. Assumptions: (1) HSR needs "
                  "dense city pairs; (2) America has few ideal "
                  "corridors; (3) costs reflect governance, not "
                  "technology. Reasoning path: the proposal predicts "
                  "viability in corridors like the Northeast - where "
                  "demand is proven - while the California route "
                  "choice compounded governance problems. Build "
                  "where demand is densest, fix governance first. "
                  "Limits: the model needs better corridor analyses; "
                  "the political economy needs addressing."),
        pointer=('The Signature system models HSR as corridor-specific: build the Northeast first, fix governance before routes. The Signature test: viability tracks corridor-demand measures. It would be refuted if dense corridors prove unviable too.'),
        key_points=[
            "Peers built thousands of miles of HSR.",
            "California's project became a cautionary tale.",
            "Car culture, federalism, and costs are blamed.",
            "Whether HSR is viable in America is open.",
        ],
        requirements=[
            "Corridor demand analyses.",
            "Governance-reform prerequisites.",
            "Peer cost-structure comparisons.",
        ],
        standards=[
            "Claims checked against the HSR literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "de Rus G. Economic Analysis of High Speed Rail in Europe. 2009.",
            "Levinson DM. High-speed rail in the US. 2012.",
        ],
        hypotheses=[
            "Corridor specificity plus governance explains the record.",
            "America cannot build HSR.",
            "Any corridor works with funding.",
            "Cars and planes suffice.",
        ],
        confirm="Viability tracks corridor-demand measures.",
        refute="Dense corridors prove unviable too.",
    ),
    dict(
        key="urban-planning-16",
        name="The Downtown Problem",
        group="Form",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("What is downtown for now - after remote work emptied "
                 "offices?"),
        background=("Downtowns were job centers; hybrid work cut office "
                    "demand structurally. Options: convert to housing, "
                    "double down on experience, or manage decline. "
                    "Whether downtowns recover their centrality or "
                    "become something new remains open."),
        why_it_matters=("Downtowns anchor transit and identity. Their "
                        "future shapes cities."),
        sig_lens=("The Signature lens treats downtown as a use ledger: "
                  "the Signature approach asks what functions need "
                  "centrality."),
        sig_body=("The Signature proposal models downtown's future as "
                  "use-rebalanced. Assumptions: (1) routine office "
                  "work decentralizes; (2) experience, culture, and "
                  "collaboration centralize; (3) housing adds "
                  "resilience. Reasoning path: the proposal predicts "
                  "downtowns should pivot to mixed experience-housing "
                  "districts - which leading cases do. The office "
                  "monoculture is then obsolete; the center persists "
                  "in new form. Limits: the model needs better "
                  "conversion economics; the transit-funding "
                  "implications need addressing."),
        pointer=("The Signature system models downtown's future as mixed experience-housing districts: the office monoculture is obsolete. The Signature test: recovery tracks mixed-use measures. It would be refuted if office monocultures recover equally."),
        key_points=[
            "Hybrid work cut office demand structurally.",
            "Conversion, experience, or decline are the options.",
            "Leading downtowns are pivoting to mixed use.",
            "Whether centrality recovers is open.",
        ],
        requirements=[
            "Conversion-economics studies.",
            "Experience-district evaluations.",
            "Transit-funding implication analyses.",
        ],
        standards=[
            "Claims checked against the downtown literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Florida R. The Rise of the Creative Class. Basic Books; 2002.",
            "Glaeser EL. Triumph of the City. Penguin; 2011.",
        ],
        hypotheses=[
            "Use rebalancing explains downtown trajectories.",
            "Offices will return fully.",
            "Downtowns are obsolete.",
            "Only housing conversion works.",
        ],
        confirm="Recovery tracks mixed-use measures.",
        refute="Office monocultures recover equally.",
    ),
    dict(
        key="urban-planning-17",
        name="Mixed Use: Does It Work",
        group="Form",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Does mixed-use development deliver its promises - "
                 "liveliness, sustainability, community - or just "
                 "expensive ground-floor retail?"),
        background=("Planners mandate mixed use; the results are "
                    "mixed: lively where demand exists, vacant "
                    "storefronts where mandated without markets. "
                    "Whether mixed use works by design or only by "
                    "market remains open."),
        why_it_matters=("Mixed use is planning orthodoxy. Its true "
                        "effects determine its mandates."),
        sig_lens=("The Signature lens treats mixed use as a demand "
                  "ledger: the Signature approach asks whether the "
                  "market supports the mix."),
        sig_body=("The Signature proposal models mixed-use success as "
                  "demand-contingent. Assumptions: (1) retail needs "
                  "foot traffic; (2) mandates without traffic create "
                  "vacancy; (3) residential above works broadly. "
                  "Reasoning path: the proposal predicts lively mixed "
                  "use where demand supports retail - explaining the "
                  "vacant-mandate problem. The policy is then enable "
                  "mix where viable, not mandate everywhere. Limits: "
                  "the model needs better demand measures; the "
                  "gentrification dimension needs addressing."),
        pointer=('The Signature system models mixed-use success as demand-contingent: enable where viable, not mandated everywhere. The Signature test: success tracks demand measures. It would be refuted if mandated mix succeeds without demand.'),
        key_points=[
            "Planners mandate mixed use widely.",
            "Results are mixed: lively or vacant.",
            "Retail needs foot traffic.",
            "Whether design or market drives success is open.",
        ],
        requirements=[
            "Demand-viability measures.",
            "Mandate-versus-market comparisons.",
            "Gentrification-dimension analyses.",
        ],
        standards=[
            "Claims checked against the mixed-use literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Jacobs J. The Death and Life of Great American Cities. Random House; 1961.",
            "Grant J. Mixed use in theory and practice. 2002.",
        ],
        hypotheses=[
            "Demand contingency explains outcomes.",
            "Mandates create their own demand.",
            "Mixed use always works.",
            "The concept is overrated.",
        ],
        confirm="Success tracks demand measures.",
        refute="Mandated mix succeeds without demand.",
    ),
    dict(
        key="urban-planning-18",
        name="Density: How Much Is Enough",
        group="Form",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("How much density is enough - for transit, liveliness, "
                 "and sustainability - and when is it too much?"),
        background=("Thresholds exist (transit needs ~30 units/acre); "
                    "beyond them, marginal benefits shrink while costs "
                    "(congestion, shadows) grow. The 'missing middle' "
                    "debate asks whether gentle density suffices. The "
                    "optimal density by goal remains unquantified."),
        why_it_matters=("Density targets shape zoning reform. The "
                        "optimum determines policy."),
        sig_lens=("The Signature lens treats density as a threshold "
                  "ledger: the Signature approach asks what each "
                  "increment buys."),
        sig_body=("The Signature proposal models density benefits as "
                  "thresholded. Assumptions: (1) key benefits "
                  "(transit, retail) need minimum densities; (2) "
                  "beyond thresholds, gains diminish; (3) costs rise "
                  "steadily. Reasoning path: the proposal predicts "
                  "the highest returns from reaching thresholds "
                  "(missing middle) rather than maximizing density - "
                  "explaining the gentle-density movement. Enough is "
                  "then threshold-plus, not maximum. Limits: the "
                  "model needs better threshold measures by goal; "
                  "the cultural acceptance question persists."),
        pointer=('The Signature system models density as thresholded: the highest returns come from reaching viability thresholds (missing middle). The Signature test: benefits inflect at threshold measures. It would be refuted if benefits scale linearly with density.'),
        key_points=[
            "Transit and retail need minimum densities.",
            "Beyond thresholds, marginal benefits shrink.",
            "The missing-middle debate centers gentle density.",
            "Optimal density by goal is unquantified.",
        ],
        requirements=[
            "Threshold measures by urban goal.",
            "Diminishing-returns quantifications.",
            "Cultural-acceptance studies.",
        ],
        standards=[
            "Claims checked against the density literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Newman P, Kenworthy J. Sustainability and Cities. Island Press; 1999.",
            "Angel S et al. The dimensions of global urban expansion. 2016.",
        ],
        hypotheses=[
            "Threshold model guides optimal density.",
            "Maximum density is optimal.",
            "Gentle density suffices for all goals.",
            "Density does not matter much.",
        ],
        confirm="Benefits inflect at threshold measures.",
        refute="Benefits scale linearly with density.",
    ),
    dict(
        key="urban-planning-19",
        name="The Greenbelt Question",
        group="Policy",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("Do greenbelts protect nature - or just push growth "
                 "further out?"),
        background=("London's greenbelt is iconic; critics show it "
                    "raised prices and pushed leapfrog development. "
                    "Defenders cite recreation and identity. Whether "
                    "greenbelts serve the environment or harm housing "
                    "remains contested."),
        why_it_matters=("Greenbelts shape regional growth. Their net "
                        "effect determines their future."),
        sig_lens=("The Signature lens treats greenbelts as a "
                  "displacement ledger: the Signature approach asks "
                  "where the growth goes."),
        sig_body=("The Signature proposal models greenbelts as "
                  "growth-displacing. Assumptions: (1) demand persists; "
                  "(2) belts redirect it outward; (3) leapfrogging "
                  "worsens environmental outcomes. Reasoning path: the "
                  "proposal predicts greenbelts should raise inside "
                  "prices and extend commutes - which the evidence "
                  "supports. Targeted environmental protection beats "
                  "blanket belts. Limits: the model needs better "
                  "leapfrog quantifications; the amenity value needs "
                  "honest pricing."),
        pointer=('The Signature system models greenbelts as growth-displacing: targeted protection beats blanket belts. The Signature test: growth redirects measurably outward. It would be refuted if greenbelts contain without displacement.'),
        key_points=[
            "Greenbelts are iconic planning tools.",
            "Critics show price effects and leapfrogging.",
            "Defenders cite recreation and identity.",
            "Net environmental effect is contested.",
        ],
        requirements=[
            "Leapfrog quantifications.",
            "Amenity-value pricing.",
            "Targeted-versus-blanket comparisons.",
        ],
        standards=[
            "Claims checked against the greenbelt literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Amati M, Taylor L. From green belts to green infrastructure. Planning Practice and Research; 2010.",
            "Cheshire P. Broken market or broken policy? 2014.",
        ],
        hypotheses=[
            "Displacement explains greenbelt outcomes.",
            "Greenbelts protect the environment net.",
            "Reform (not abolition) is the answer.",
            "The amenity value justifies costs.",
        ],
        confirm="Growth redirects measurably outward.",
        refute="Greenbelts contain without displacement.",
    ),
    dict(
        key="urban-planning-20",
        name="Eminent Domain: Just",
        group="Policy",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("When is eminent domain just - and did Kelo stretch "
                 "'public use' beyond recognition?"),
        background=("Kelo allowed takings for economic development; "
                    "backlash produced state reforms. The questions: "
                    "whether economic-development takings are ever "
                    "justified, what compensation is fair, and whether "
                    "the reforms worked."),
        why_it_matters=("Eminent domain takes homes for others' gain. "
                        "Its justice is property's frontier."),
        sig_lens=("The Signature lens treats takings as a distribution "
                  "ledger: the Signature approach asks who gains and "
                  "who loses."),
        sig_body=("The Signature proposal models eminent-domain "
                  "justice as distribution-sensitive. Assumptions: (1) "
                  "takings concentrate costs on the displaced; (2) "
                  "benefits diffuse to developers and cities; (3) "
                  "compensation rarely covers true loss. Reasoning "
                  "path: the proposal predicts economic-development "
                  "takings should face the highest bar - explaining "
                  "the Kelo backlash. Genuine public uses (roads, "
                  "schools) clear it; private-benefit takings do not. "
                  "Limits: the model needs better compensation "
                  "studies; the reform evaluations need completing."),
        pointer=('The Signature system models eminent-domain justice as distribution-sensitive: genuine public uses clear the bar; private-benefit takings do not. The Signature test: opposition tracks distribution measures. It would be refuted if compensated takings prove unobjectionable.'),
        key_points=[
            "Kelo allowed economic-development takings.",
            "Backlash produced state reforms.",
            "Compensation rarely covers true loss.",
            "Whether the reforms worked is open.",
        ],
        requirements=[
            "Compensation-adequacy studies.",
            "Reform evaluations.",
            "Distribution analyses by taking type.",
        ],
        standards=[
            "Claims checked against the takings literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kelo v. City of New London. 545 U.S. 469; 2005.",
            "Somin I. The Grasping Hand. University of Chicago Press; 2015.",
        ],
        hypotheses=[
            "Distribution sensitivity guides just takings.",
            "Economic-development takings are never just.",
            "Compensation can make them just.",
            "Kelo was correctly decided.",
        ],
        confirm="Opposition tracks distribution measures.",
        refute="Compensated takings prove unobjectionable.",
    ),
    dict(
        key="urban-planning-21",
        name="Tax Increment Financing: Fair",
        group="Policy",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Is tax increment financing fair - or a subsidy machine "
                 "for developers?"),
        background=("TIF diverts future tax gains to fund current "
                    "development; critics show it subsidizes projects "
                    "that would happen anyway and starves schools. "
                    "Defenders cite blight removal. Whether TIF's "
                    "benefits exceed its diversions remains open."),
        why_it_matters=("TIF directs billions in public money. Its "
                        "fairness determines its legitimacy."),
        sig_lens=("The Signature lens treats TIF as a but-for ledger: "
                  "the Signature approach asks whether the "
                  "development needed the subsidy."),
        sig_body=("The Signature proposal models TIF as "
                  "but-for dependent. Assumptions: (1) TIF is "
                  "justified only if development would not occur "
                  "otherwise; (2) the but-for test is rarely applied; "
                  "(3) diversions harm overlapping jurisdictions. "
                  "Reasoning path: the proposal predicts TIF should "
                  "show benefits only with strict but-for tests - "
                  "which the evidence supports. Reform is then "
                  "test enforcement, not abolition. Limits: the model "
                  "needs better but-for studies; the school-funding "
                  "impacts need quantifying."),
        pointer=("The Signature system models TIF as justified only with strict but-for tests: enforce the test, don't just abolish. The Signature test: benefits appear only with but-for tests. It would be refuted if tIF succeeds without the test."),
        key_points=[
            "TIF diverts future taxes to current development.",
            "Critics allege subsidies for inevitable projects.",
            "Schools lose diverted revenue.",
            "Whether benefits exceed diversions is open.",
        ],
        requirements=[
            "But-for test studies.",
            "School-impact quantifications.",
            "Reform evaluations.",
        ],
        standards=[
            "Claims checked against the TIF literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weber R, O'Neill-Kohl S. The historical logic of TIF. 2013.",
            "Dye RF, Merriman DF. The effects of TIF on economic development. 2000.",
        ],
        hypotheses=[
            "But-for enforcement rescues TIF.",
            "TIF is inherently a giveaway.",
            "Abolition is the answer.",
            "The benefits justify the diversions.",
        ],
        confirm="Benefits appear only with but-for tests.",
        refute="TIF succeeds without the test.",
    ),
    dict(
        key="urban-planning-22",
        name="Participatory Planning: Real",
        group="Policy",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("Is participatory planning real democracy - or capture "
                 "by the loudest neighbors?"),
        background=("Participation mandates proliferated; critics show "
                    "meetings overrepresent older homeowners (the "
                    "NIMBY mechanism). Deliberative innovations "
                    "(citizen assemblies) promise better. Whether "
                    "participation democratizes or distorts remains "
                    "open."),
        why_it_matters=("Participation legitimates planning. Its reality "
                        "determines its value."),
        sig_lens=("The Signature lens treats participation as a "
                  "representation ledger: the Signature approach asks "
                  "who shows up."),
        sig_body=("The Signature proposal models participation as "
                  "representation-skewed. Assumptions: (1) meeting "
                  "attendees skew homeowner-older; (2) the skew "
                  "biases outcomes toward the status quo; (3) "
                  "sortition fixes representation. Reasoning path: "
                  "the proposal predicts deliberative (sortition-"
                  "based) processes should outperform open meetings - "
                  "which the evidence supports. Democratize "
                  "participation itself. Limits: the model needs "
                  "better outcome comparisons; the scale-up question "
                  "persists."),
        pointer=('The Signature system models participation as representation-skewed: sortition-based deliberation outperforms open meetings. The Signature test: outcomes track representation measures. It would be refuted if open meetings represent broadly.'),
        key_points=[
            "Participation mandates proliferated.",
            "Meetings overrepresent older homeowners.",
            "The skew biases toward the status quo.",
            "Deliberative innovations promise better.",
        ],
        requirements=[
            "Representation audits of processes.",
            "Deliberative-versus-open comparisons.",
            "Scale-up studies.",
        ],
        standards=[
            "Claims checked against the participation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Arnstein SR. A ladder of citizen participation. 1969.",
            "Einstein KL et al. Neighborhood Defenders. Cambridge University Press; 2019.",
        ],
        hypotheses=[
            "Representation skew explains participation's failures.",
            "Participation is genuinely democratic.",
            "Sortition fixes the skew.",
            "Participation should be reduced.",
        ],
        confirm="Outcomes track representation measures.",
        refute="Open meetings represent broadly.",
    ),
    dict(
        key="urban-planning-23",
        name="The NIMBY Problem",
        group="Housing",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Why do neighborhoods block housing - and can the NIMBY "
                 "dynamic be broken?"),
        background=("Homeowners block development to protect values and "
                    "amenities; the collective result is shortage. "
                    "Explanations: rational self-interest, loss "
                    "aversion, and institutional design (local vetoes). "
                    "Reforms (state preemption, by-right approval) "
                    "attempt the fix. Whether the dynamic is breakable "
                    "remains open."),
        why_it_matters=("NIMBYism drives the housing crisis. Breaking it "
                        "is reform's key."),
        sig_lens=("The Signature lens treats NIMBY as an incentive "
                  "ledger: the Signature approach asks what "
                  "homeowners gain from blocking."),
        sig_body=("The Signature proposal models NIMBY as "
                  "institutionally enabled self-interest. Assumptions: "
                  "(1) blocking protects values; (2) local vetoes "
                  "empower blockers; (3) the costs diffuse regionally. "
                  "Reasoning path: the proposal predicts blocking "
                  "should fall where vetoes are removed (by-right "
                  "approval, state preemption) - which reform "
                  "evidence supports. The fix is then institutional: "
                  "move decisions up, make approvals by-right. Limits: "
                  "the model needs better reform evaluations; the "
                  "democratic-legitimacy question needs answering."),
        pointer=('The Signature system models NIMBY as institutionally enabled: remove local vetoes through by-right approval and state preemption. The Signature test: building tracks veto-removal measures. It would be refuted if reforms fail to increase building.'),
        key_points=[
            "Homeowners block to protect values and amenities.",
            "The collective result is regional shortage.",
            "Local vetoes empower blockers.",
            "Reforms attempt institutional fixes.",
        ],
        requirements=[
            "Reform evaluations.",
            "Veto-point analyses.",
            "Legitimacy-framework development.",
        ],
        standards=[
            "Claims checked against the land-use politics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fischel WA. The Homevoter Hypothesis. Harvard University Press; 2001.",
            "Einstein KL et al. Neighborhood Defenders. Cambridge University Press; 2019.",
        ],
        hypotheses=[
            "Institutional vetoes explain NIMBY power.",
            "Self-interest alone suffices.",
            "Persuasion can overcome NIMBY.",
            "The dynamic is unbreakable.",
        ],
        confirm="Building tracks veto-removal measures.",
        refute="Reforms fail to increase building.",
    ),
    dict(
        key="urban-planning-24",
        name="The YIMBY Answer",
        group="Housing",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Is YIMBYism the answer to the housing crisis - and what "
                 "are its limits?"),
        background=("YIMBY movements won upzoning reforms; critics argue "
                    "supply alone will not deliver affordability "
                    "(filtering is slow, luxury dominates) and that "
                    "YIMBY ignores tenant protections. Whether the "
                    "supply-side answer suffices remains the housing "
                    "debate's center."),
        why_it_matters=("YIMBY is housing reform's vanguard. Its limits "
                        "determine the full policy mix."),
        sig_lens=("The Signature lens treats YIMBY as a time ledger: "
                  "the Signature approach asks how fast filtering "
                  "works."),
        sig_body=("The Signature proposal models YIMBY as "
                  "necessary-but-insufficient. Assumptions: (1) supply "
                  "lowers prices at the margin; (2) filtering to "
                  "affordability takes decades; (3) tenant protections "
                  "address the interim. Reasoning path: the proposal "
                  "predicts supply should help broadly while the "
                  "poorest need direct support - explaining both "
                  "YIMBY's wins and its critics' point. The answer is "
                  "then supply plus protections plus subsidies. Limits: "
                  "the model needs better filtering-speed studies; "
                  "the political coalition needs holding."),
        pointer=('The Signature system models YIMBY as necessary but insufficient: supply plus protections plus subsidies. The Signature test: affordability tracks full-mix measures. It would be refuted if supply alone delivers affordability quickly.'),
        key_points=[
            "YIMBY won significant upzoning reforms.",
            "Filtering to affordability is slow.",
            "Critics demand tenant protections.",
            "Whether supply suffices is the center debate.",
        ],
        requirements=[
            "Filtering-speed studies.",
            "Full-mix policy evaluations.",
            "Coalition-maintenance analyses.",
        ],
        standards=[
            "Claims checked against the housing literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rosenthal SS. Are private markets and filtering a viable source of low-income housing? 2014.",
            "Been V et al. Supply skepticism. 2019.",
        ],
        hypotheses=[
            "Supply-plus explains the needed mix.",
            "Supply alone suffices.",
            "Supply cannot help affordability.",
            "The coalition will fracture.",
        ],
        confirm="Affordability tracks full-mix measures.",
        refute="Supply alone delivers affordability quickly.",
    ),
    dict(
        key="urban-planning-25",
        name="Social Housing: The Models",
        group="Housing",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("Which social-housing model works - Vienna, Singapore, "
                 "or something new?"),
        background=("Vienna's broad public housing and Singapore's "
                    "leasehold model are admired; America's project "
                    "model is the cautionary tale. The variables: "
                    "breadth (universal versus targeted), management, "
                    "and financing. Which model transfers remains open."),
        why_it_matters=("Social housing is the direct affordability "
                        "answer. The model determines its success."),
        sig_lens=("The Signature lens treats social housing as a "
                  "breadth ledger: the Signature approach asks who "
                  "the housing serves."),
        sig_body=("The Signature proposal models success as "
                  "breadth-dependent. Assumptions: (1) targeted "
                  "programs stigmatize and lose political support; "
                  "(2) broad programs sustain quality constituencies; "
                  "(3) management determines outcomes. Reasoning path: "
                  "the proposal predicts Vienna-style breadth should "
                  "outperform targeted projects - which the record "
                  "supports. The transfer question is then political "
                  "(building broad coalitions), not technical. Limits: "
                  "the model needs better transfer studies; the "
                  "financing scale needs solving."),
        pointer=('The Signature system models social-housing success as breadth-dependent: broad programs sustain quality; targeted ones stigmatize. The Signature test: outcomes track breadth measures. It would be refuted if targeted programs outperform broad ones.'),
        key_points=[
            "Vienna and Singapore are admired models.",
            "America's projects are the cautionary tale.",
            "Breadth, management, and financing are the variables.",
            "Which model transfers is open.",
        ],
        requirements=[
            "Breadth-outcome studies.",
            "Transfer-feasibility analyses.",
            "Financing-scale solutions.",
        ],
        standards=[
            "Claims checked against the social-housing literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Scanlon K et al. Social Housing in Europe. Wiley; 2014.",
            "Vale LJ. From the Puritans to the Projects. Harvard University Press; 2000.",
        ],
        hypotheses=[
            "Breadth dependence explains model outcomes.",
            "Targeting the neediest is best.",
            "Management alone determines success.",
            "No model transfers across contexts.",
        ],
        confirm="Outcomes track breadth measures.",
        refute="Targeted programs outperform broad ones.",
    ),
    dict(
        key="urban-planning-26",
        name="Homelessness: What Ends It",
        group="Housing",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("What ends homelessness - housing first, treatment "
                 "first, or something else?"),
        background=("Housing First (Finland, US trials) houses without "
                    "preconditions and shows strong retention; critics "
                    "argue it needs housing supply to scale and that "
                    "addiction/mental-health services lag. Whether the "
                    "model ends homelessness at scale remains open."),
        why_it_matters=("Homelessness is the housing crisis's sharp end. "
                        "The effective model saves lives."),
        sig_lens=("The Signature lens treats homelessness as a housing "
                  "ledger: the Signature approach asks whether the "
                  "shortage is of homes or of treatment."),
        sig_body=("The Signature proposal models homelessness as "
                  "housing-shortage driven. Assumptions: (1) "
                  "homelessness tracks housing costs, not addiction "
                  "rates; (2) Housing First works individually; (3) "
                  "scale needs supply. Reasoning path: the proposal "
                  "predicts homelessness should follow rents - which "
                  "it does strongly - making supply the systemic "
                  "answer with Housing First as the individual "
                  "protocol. Limits: the model needs better "
                  "causal studies; the services dimension needs "
                  "integrating."),
        pointer=('The Signature system models homelessness as housing-shortage driven: supply is the systemic answer, Housing First the individual protocol. The Signature test: rates track housing-cost measures. It would be refuted if homelessness ignores housing costs.'),
        key_points=[
            "Housing First shows strong individual retention.",
            "Homelessness tracks housing costs strongly.",
            "Scale needs housing supply.",
            "Whether the model ends homelessness at scale is open.",
        ],
        requirements=[
            "Rent-homelessness causal studies.",
            "At-scale Housing First evaluations.",
            "Services-integration analyses.",
        ],
        standards=[
            "Claims checked against the homelessness literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Tsemberis S. Housing First. Hazelden; 2010.",
            "Colburn G, Aldern CP. Homelessness Is a Housing Problem. University of California Press; 2022.",
        ],
        hypotheses=[
            "Housing shortage explains homelessness rates.",
            "Treatment-first is needed.",
            "Housing First scales fully.",
            "The causes are too complex for one model.",
        ],
        confirm="Rates track housing-cost measures.",
        refute="Homelessness ignores housing costs.",
    ),
    dict(
        key="urban-planning-27",
        name="Climate Migration and Cities",
        group="Theory",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("How should cities prepare for climate migration - the "
                 "coming population movements?"),
        background=("Projections suggest large climate-driven movements; "
                    "receiving cities are unprepared. Questions: "
                    "which cities gain, how to plan for influx, and "
                    "whether managed retreat can work. The planning "
                    "frameworks are nascent."),
        why_it_matters=("Climate migration will reshape cities. "
                        "Preparation determines whether it is managed "
                        "or chaotic."),
        sig_lens=("The Signature lens treats migration as a receiving "
                  "ledger: the Signature approach asks which cities "
                  "can absorb growth."),
        sig_body=("The Signature proposal models climate migration as "
                  "receiving-capacity dependent. Assumptions: (1) "
                  "movements follow habitability and opportunity; (2) "
                  "receiving cities need housing and infrastructure "
                  "headroom; (3) planning lags. Reasoning path: the "
                  "proposal predicts orderly outcomes where receiving "
                  "cities build headroom - making proactive upzoning "
                  "and infrastructure the preparation. Managed retreat "
                  "needs honest triage. Limits: the model needs better "
                  "migration projections; the political will is "
                  "lacking."),
        pointer=('The Signature system models climate migration as receiving-capacity dependent: build headroom in likely receiving cities now. The Signature test: orderly outcomes track headroom measures. It would be refuted if unprepared cities absorb smoothly.'),
        key_points=[
            "Large climate-driven movements are projected.",
            "Receiving cities are unprepared.",
            "Managed retreat frameworks are nascent.",
            "Preparation determines order versus chaos.",
        ],
        requirements=[
            "Migration-projection planning data.",
            "Receiving-capacity assessments.",
            "Managed-retreat triage frameworks.",
        ],
        standards=[
            "Claims checked against the climate-migration literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rigaud KK et al. Groundswell. World Bank; 2018.",
            "Hauer ME. Migration induced by sea-level rise. 2017.",
        ],
        hypotheses=[
            "Receiving capacity determines outcomes.",
            "Migration will be smaller than projected.",
            "No preparation can manage the scale.",
            "Sending-region adaptation prevents movement.",
        ],
        confirm="Orderly outcomes track headroom measures.",
        refute="Unprepared cities absorb smoothly.",
    ),
    dict(
        key="urban-planning-28",
        name="The Smart City Problem",
        group="Theory",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Do smart cities serve citizens - or do they serve the "
                 "vendors and the surveillance?"),
        background=("Sidewalk Labs' Toronto failure crystallized the "
                    "critique: sensor-driven urbanism for corporate "
                    "gain. Defenders cite genuine efficiencies "
                    "(traffic, energy). Whether urban intelligence can "
                    "be democratized remains open."),
        why_it_matters=("Smart-city contracts shape urban governance. "
                        "Their terms determine who the city serves."),
        sig_lens=("The Signature lens treats smartness as a governance "
                  "ledger: the Signature approach asks who owns the "
                  "data and decides."),
        sig_body=("The Signature proposal models smart-city value as "
                  "governance-dependent. Assumptions: (1) sensors "
                  "create real efficiencies; (2) vendor control "
                  "captures the value; (3) public data trusts could "
                  "redirect it. Reasoning path: the proposal predicts "
                  "benefits should accrue publicly under public "
                  "governance - explaining the Toronto backlash as "
                  "governance failure, not technology failure. The "
                  "answer is then civic data trusts. Limits: the "
                  "model needs better governance pilots; the "
                  "surveillance dimension needs separate treatment."),
        pointer=('The Signature system models smart-city value as governance-dependent: civic data trusts redirect benefits publicly. The Signature test: public benefits track governance measures. It would be refuted if vendor-led projects benefit publics equally.'),
        key_points=[
            "Sensor urbanism promises efficiencies.",
            "Vendor capture and surveillance are the critiques.",
            "Toronto's failure crystallized opposition.",
            "Whether intelligence can be democratized is open.",
        ],
        requirements=[
            "Data-trust pilots.",
            "Benefit-distribution studies.",
            "Surveillance-impact analyses.",
        ],
        standards=[
            "Claims checked against the smart-city literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Green B. The Smart Enough City. MIT Press; 2019.",
            "Kitchin R. The Data Revolution. Sage; 2014.",
        ],
        hypotheses=[
            "Governance determines who benefits.",
            "Smart cities are inherently corporate.",
            "The efficiencies justify the model.",
            "The concept is bankrupt.",
        ],
        confirm="Public benefits track governance measures.",
        refute="Vendor-led projects benefit publics equally.",
    ),
    dict(
        key="urban-planning-29",
        name="Surveillance Urbanism",
        group="Theory",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("How should planning handle surveillance urbanism - the "
                 "sensor-and-camera city?"),
        background=("Cameras, license readers, and predictive policing "
                    "reshape urban space; the benefits (safety) and "
                    "harms (chilling, bias) are both real. Planning "
                    "has no framework for the surveilled city. Whether "
                    "regulation can civilize it remains open."),
        why_it_matters=("Surveillance shapes who feels free in public "
                        "space. Planning's response determines urban "
                        "liberty."),
        sig_lens=("The Signature lens treats surveillance as a liberty "
                  "ledger: the Signature approach asks whose behavior "
                  "changes."),
        sig_body=("The Signature proposal models surveillance effects "
                  "as distribution-sensitive. Assumptions: (1) "
                  "surveillance chills the marginal and vulnerable "
                  "most; (2) safety benefits are real but uneven; (3) "
                  "opacity compounds harm. Reasoning path: the "
                  "proposal predicts planning should treat "
                  "surveillance as a land-use question - regulating "
                  "where and how sensing happens. The framework is "
                  "then spatial: surveillance zoning. Limits: the "
                  "model needs better chilling-effect studies; the "
                  "technology outpaces regulation."),
        pointer=('The Signature system models surveillance as a land-use question: regulate where and how sensing happens - surveillance zoning. The Signature test: harms track opacity-distribution measures. It would be refuted if surveillance shows no chilling effects.'),
        key_points=[
            "Sensors and cameras reshape urban space.",
            "Safety benefits and chilling harms are both real.",
            "Planning lacks a framework.",
            "Whether regulation can civilize it is open.",
        ],
        requirements=[
            "Chilling-effect studies.",
            "Surveillance-zoning frameworks.",
            "Distribution-sensitive impact analyses.",
        ],
        standards=[
            "Claims checked against the surveillance literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Zuboff S. The Age of Surveillance Capitalism. PublicAffairs; 2019.",
            "Brayne S. Predict and Surveil. Oxford University Press; 2020.",
        ],
        hypotheses=[
            "Spatial regulation civilizes surveillance.",
            "Surveillance is inherently oppressive.",
            "Safety justifies the sensors.",
            "Technology outpaces any regulation.",
        ],
        confirm="Harms track opacity-distribution measures.",
        refute="Surveillance shows no chilling effects.",
    ),
    dict(
        key="urban-planning-30",
        name="The Post-Pandemic City",
        group="Theory",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("What did the pandemic permanently change about cities - "
                 "and what snapped back?"),
        background=("Remote work, e-commerce, and outdoor dining "
                    "reshaped cities; some changes stuck (hybrid work), "
                    "others reversed (transit recovers slowly). The "
                    "question: which pandemic adaptations are permanent "
                    "features versus temporary expedients."),
        why_it_matters=("The pandemic was urbanism's great experiment. "
                        "Its lessons guide the next decades."),
        sig_lens=("The Signature lens treats the pandemic as a "
                  "stickiness ledger: the Signature approach asks "
                  "which changes stuck."),
        sig_body=("The Signature proposal models pandemic change as "
                  "stickiness-filtered. Assumptions: (1) changes "
                  "persist where they serve underlying trends "
                  "(hybrid work, e-commerce); (2) reversals happen "
                  "where they fought trends; (3) the filter is "
                  "still running. Reasoning path: the proposal "
                  "predicts the permanent set should be the "
                  "trend-accelerating changes - which matches the "
                  "record. Plan for the accelerated trends, not the "
                  "emergency. Limits: the model needs longer "
                  "observation; the equity dimension (who bore the "
                  "costs) needs centering."),
        pointer=('The Signature system models pandemic change as stickiness-filtered: permanent where it accelerated underlying trends. The Signature test: persistence tracks trend-alignment measures. It would be refuted if changes persist randomly.'),
        key_points=[
            "Remote work, e-commerce, outdoor dining reshaped cities.",
            "Some changes stuck; others reversed.",
            "Transit recovers slowly.",
            "Which adaptations are permanent is the question.",
        ],
        requirements=[
            "Stickiness tracking by change type.",
            "Trend-acceleration analyses.",
            "Equity-dimension centering.",
        ],
        standards=[
            "Claims checked against the post-pandemic literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Florida R et al. The pandemic and cities. 2021.",
            "Glaeser EL et al. The economic effects of the pandemic on cities. 2022.",
        ],
        hypotheses=[
            "Trend acceleration explains stickiness.",
            "Most changes will reverse.",
            "The pandemic transformed cities permanently.",
            "It is too early to tell.",
        ],
        confirm="Persistence tracks trend-alignment measures.",
        refute="Changes persist randomly.",
    ),
    dict(
        key="urban-planning-31",
        name="Shrinking Cities: The Response",
        group="Theory",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("How should planning handle shrinking cities - the "
                 "Detroits and beyond?"),
        background=("Deindustrialization shrank many cities; planning "
                    "assumes growth. Responses: right-sizing "
                    "(demolition, greening), consolidation, or "
                    "managed decline. Whether shrinkage can be "
                    "graceful remains open."),
        why_it_matters=("Shrinking cities house millions. Their "
                        "planning determines dignity in decline."),
        sig_lens=("The Signature lens treats shrinkage as a "
                  "right-sizing ledger: the Signature approach asks "
                  "what the smaller city needs."),
        sig_body=("The Signature proposal models shrinkage response "
                  "as right-sizing. Assumptions: (1) infrastructure "
                  "built for more people burdens the fewer; (2) "
                  "greening vacant land helps; (3) dignity needs "
                  "honesty. Reasoning path: the proposal predicts "
                  "graceful shrinkage should follow planned "
                  "consolidation - which the best cases show. "
                  "Planning for less, well, beats pretending growth. "
                  "Limits: the model needs better right-sizing "
                  "evaluations; the racial-justice dimension (who "
                  "was abandoned) needs centering."),
        pointer=('The Signature system models shrinkage as right-sizing: plan for less, well, rather than pretending growth. The Signature test: outcomes track right-sizing measures. It would be refuted if unplanned shrinkage performs equally.'),
        key_points=[
            "Deindustrialization shrank many cities.",
            "Planning assumes growth.",
            "Right-sizing, greening, and consolidation are responses.",
            "Whether shrinkage can be graceful is open.",
        ],
        requirements=[
            "Right-sizing evaluations.",
            "Vacant-land strategy studies.",
            "Racial-justice integration.",
        ],
        standards=[
            "Claims checked against the shrinking-cities literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ryan BD. Design After Decline. University of Pennsylvania Press; 2012.",
            "Schilling J, Logan J. Greening the rust belt. 2008.",
        ],
        hypotheses=[
            "Planned right-sizing enables graceful shrinkage.",
            "Growth will return; wait it out.",
            "Shrinkage is unmanageable.",
            "Only regional solutions work.",
        ],
        confirm="Outcomes track right-sizing measures.",
        refute="Unplanned shrinkage performs equally.",
    ),
    dict(
        key="urban-planning-32",
        name="The Global South City",
        group="Theory",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("Does planning theory - built on Western cities - fit "
                 "the Global South city?"),
        background=("Southern urbanism (informality, rapid growth, "
                    "different states) challenges Northern theory. "
                    "Watson, Roy, and others argue for Southern theory; "
                    "critics warn of relativism. Whether planning needs "
                    "decolonizing or universalizing remains open."),
        why_it_matters=("Most urban growth is Southern. Theory's fit "
                        "determines its usefulness."),
        sig_lens=("The Signature lens treats theory as a context "
                  "ledger: the Signature approach asks what "
                  "travels and what does not."),
        sig_body=("The Signature proposal models theory transfer as "
                  "mechanism-specific. Assumptions: (1) some "
                  "mechanisms are universal (agglomeration); (2) "
                  "institutions differ profoundly; (3) informality is "
                  "structural, not transitional. Reasoning path: the "
                  "proposal predicts Northern tools should work "
                  "where mechanisms match and fail where "
                  "institutions differ - explaining the mixed "
                  "record. The answer is then mechanism-based "
                  "theory, neither wholesale import nor wholesale "
                  "rejection. Limits: the model needs better "
                  "mechanism mapping; the decolonial critique needs "
                  "engaging."),
        pointer=('The Signature system models theory transfer as mechanism-specific: keep universal mechanisms, rebuild institutional assumptions. The Signature test: tool success tracks mechanism-match measures. It would be refuted if northern tools work uniformly.'),
        key_points=[
            "Southern urbanism challenges Northern theory.",
            "Informality is structural, not transitional.",
            "Decolonial critiques demand new theory.",
            "Whether to decolonize or universalize is open.",
        ],
        requirements=[
            "Mechanism-mapping studies.",
            "Southern-theory development.",
            "Decolonial-critique engagement.",
        ],
        standards=[
            "Claims checked against the Southern-urbanism literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Roy A. Why India cannot plan its cities. Planning Theory; 2009.",
            "Watson V. Seeing from the South. Urban Studies; 2009.",
        ],
        hypotheses=[
            "Mechanism specificity guides transfer.",
            "Northern theory is universally applicable.",
            "Southern theory must replace it.",
            "The debate is unresolvable.",
        ],
        confirm="Tool success tracks mechanism-match measures.",
        refute="Northern tools work uniformly.",
    ),
    dict(
        key="urban-planning-33",
        name="Planning and Justice",
        group="Policy",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("Can planning deliver justice - or does it inherently "
                 "serve power?"),
        background=("Planning's history includes redlining, urban "
                    "renewal clearance, and highway bisection; "
                    "equity planning (Davidoff, Krumholz) fights back. "
                    "Whether the tools can be turned to justice or "
                    "the field is structurally captured remains open."),
        why_it_matters=("Planning shapes who gets what in cities. Its "
                        "justice determines its legitimacy."),
        sig_lens=("The Signature lens treats planning as a power "
                  "ledger: the Signature approach asks who the tools "
                  "serve."),
        sig_body=("The Signature proposal models planning justice as "
                  "tool-plus-politics. Assumptions: (1) tools are "
                  "pliable (zoning excludes or includes); (2) "
                  "politics determine the direction; (3) equity "
                  "planning shows alternative uses. Reasoning path: "
                  "the proposal predicts just outcomes where "
                  "equity-organized politics wield the tools - "
                  "explaining both the harms (captured planning) and "
                  "the wins. Justice is then a political achievement "
                  "using planning tools. Limits: the model needs "
                  "better equity-outcome studies; the structural-"
                  "capture thesis needs answering."),
        pointer=('The Signature system models planning justice as tool-plus-politics: just outcomes where equity-organized politics wield the tools. The Signature test: just outcomes track equity-organization measures. It would be refuted if tools determine outcomes regardless of politics.'),
        key_points=[
            "Planning's history includes redlining and clearance.",
            "Equity planning fights back.",
            "Tools are pliable; politics direct them.",
            "Whether the field is captured remains open.",
        ],
        requirements=[
            "Equity-outcome studies.",
            "Capture-mechanism analyses.",
            "Alternative-practice documentation.",
        ],
        standards=[
            "Claims checked against the equity-planning literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Davidoff P. Advocacy and pluralism in planning. 1965.",
            "Krumholz N, Forester J. Making Equity Planning Work. Temple University Press; 1990.",
        ],
        hypotheses=[
            "Tool-plus-politics explains justice outcomes.",
            "Planning is structurally captured.",
            "Equity planning transforms the field.",
            "Justice is beyond planning's reach.",
        ],
        confirm="Just outcomes track equity-organization measures.",
        refute="Tools determine outcomes regardless of politics.",
    ),
    dict(
        key="urban-planning-34",
        name="A Unified Theory of Cities",
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can urban theory unify - economics, sociology, "
                 "geography, and planning - into one account of cities?"),
        background=("Each discipline captures something: economics the "
                    "agglomeration, sociology the community, geography "
                    "the space, planning the intervention. Unification "
                    "attempts (complexity theory, urban scaling) are "
                    "promising but partial. Whether one theory of "
                    "cities is possible is the field's capstone."),
        why_it_matters=("This is urbanism's capstone: the answer "
                        "determines what a city is."),
        sig_lens=("The Signature lens treats the disciplines as a "
                  "scale ledger: the Signature approach asks what "
                  "scale each owns."),
        sig_body=("The Signature proposal models unification as "
                  "scale-integration. Assumptions: (1) cities span "
                  "individual, neighborhood, metropolitan, and "
                  "system scales; (2) each discipline owns scales; "
                  "(3) scaling laws connect them. Reasoning path: "
                  "the proposal assigns economics to agglomeration, "
                  "sociology to community, geography to space, "
                  "planning to intervention - with urban scaling "
                  "theory as the bridge. Unity comes from the city "
                  "that holds the scales together. Limits: the "
                  "integration is sketched; the social dimensions "
                  "resist scaling."),
        pointer=('The Signature system assigns each discipline its scales of the city, with urban scaling theory as the bridge. The Signature test: integrated models predict across scales. It would be refuted if scales prove irreducible to common theory.'),
        key_points=[
            "Four disciplines offer incompatible images of cities.",
            "Each captures what the others miss.",
            "Scaling theory offers a partial bridge.",
            "Whether one theory is possible is foundational.",
        ],
        requirements=[
            "A scale architecture for the disciplines.",
            "Scaling-law extensions to social dimensions.",
            "Testable implications of the integration.",
        ],
        standards=[
            "Claims checked against the urban-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bettencourt LMA. The origins of scaling in cities. Science; 2013.",
            "Jacobs J. The Death and Life of Great American Cities. Random House; 1961.",
        ],
        hypotheses=[
            "Scale-integration unifies urban theory.",
            "The disciplines are incommensurable.",
            "Complexity theory will unify them.",
            "Pluralism is permanent.",
        ],
        confirm="Integrated models predict across scales.",
        refute="Scales prove irreducible to common theory.",
    ),
]
